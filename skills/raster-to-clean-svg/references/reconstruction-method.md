# Raster-to-SVG reconstruction method

## Contents

- [Toolchain](#toolchain)
- [Preserve the coordinate system](#preserve-the-coordinate-system)
- [Estimate background and foreground](#estimate-background-and-foreground)
- [Recover solid fills through alpha reconstruction](#recover-solid-fills-through-alpha-reconstruction)
- [Extract measurable geometry](#extract-measurable-geometry)
- [Model the SVG](#model-the-svg)
- [Fit and optimize](#fit-and-optimize)
- [Compare raster and SVG](#compare-raster-and-svg)
- [Validate native vector content](#validate-native-vector-content)
- [Lessons from three reconstructed archetypes](#lessons-from-three-reconstructed-archetypes)
- [Failure modes](#failure-modes)
- [What exact means](#what-exact-means)

## Toolchain

The recovered workflow used Python, Pillow, NumPy, OpenCV, scikit-image, SciPy, CairoSVG, `xml.etree.ElementTree`, and visual inspection. The recorded environment was Python 3.13.5, Pillow 12.3.0, NumPy 2.3.5, OpenCV 4.13.0, scikit-image 0.26.0, SciPy 1.17.0, and CairoSVG 2.8.2. Treat those versions as provenance, not mandatory pins.

Use tools by role:

- Pillow and NumPy: image loading, sampling, masks, and diagnostics.
- OpenCV: contours, connected components, bounding boxes, rotated rectangles, and shape statistics.
- scikit-image: medial axes and SSIM.
- SciPy: optional low-dimensional geometry optimization.
- CairoSVG: rasterize each SVG candidate at an exact size in the recovered workflow. On Windows without the native Cairo DLL, use `resvg_py`, whose wheels bundle a cross-platform Rust renderer.
- ElementTree: XML and element validation.
- Image viewer: inspect the reference, masks, component crops, candidate renders, differences, and side-by-side comparisons.

Generic autotracing is intentionally not the primary method. It tends to preserve raster defects, create excessive nodes, and obscure the intended primitive structure.

## Preserve the coordinate system

Set the SVG viewBox to the raster dimensions:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 479 363">
```

With a one-unit-per-pixel coordinate system, contour points, bounding boxes, rotations, centers, corner radii, and rendered comparisons use the same frame. Do not resize the source before measuring. If a larger production size is required, scale at export time rather than changing the reconstruction coordinate system.

## Estimate background and foreground

For a mostly uniform background, estimate its RGB value from several corner patches and use the median to suppress isolated compression or antialiasing noise:

```python
from PIL import Image
import numpy as np

image = Image.open("reference.png").convert("RGB")
rgb = np.asarray(image, dtype=np.float32)

corner_pixels = np.concatenate([
    rgb[:15, :15].reshape(-1, 3),
    rgb[:15, -15:].reshape(-1, 3),
    rgb[-15:, :15].reshape(-1, 3),
    rgb[-15:, -15:].reshape(-1, 3),
])
background = np.median(corner_pixels, axis=0)

distance = np.linalg.norm(rgb - background, axis=2)
foreground_mask = distance > 12
```

The `12` threshold was effective for near-white logo backgrounds in the recovered examples; it is a starting value, not a constant of nature. Inspect the mask and change it when low-contrast artwork disappears or background artifacts appear.

If corners contain artwork, transparency, texture, or a gradient, sample known background regions manually or supply an explicit background. A single global threshold is inappropriate for a complex photographic background.

## Recover solid fills through alpha reconstruction

Exact RGB matching fails at antialiased edges. For foreground fill `F`, background `B`, and coverage `alpha`, an edge pixel is approximately:

```text
P = alpha * F + (1 - alpha) * B
```

Estimate alpha by projecting each pixel onto the RGB line between background and fill:

```python
def alpha_from_fill(rgb, background, fill):
    background = np.asarray(background, dtype=np.float32)
    fill = np.asarray(fill, dtype=np.float32)
    direction = fill - background
    denominator = np.dot(direction, direction)
    alpha = np.sum((rgb - background) * direction, axis=2) / denominator
    return np.clip(alpha, 0.0, 1.0)
```

Measure how well each candidate fill can explain a pixel:

```python
def residual_to_fill(rgb, background, fill):
    alpha = alpha_from_fill(rgb, background, fill)
    reconstructed = background + alpha[..., None] * (fill - background)
    return np.linalg.norm(rgb - reconstructed, axis=2)
```

For several known fills, assign each pixel to the fill with the lowest residual, subject to a minimum alpha and maximum residual. This correctly groups pale edge pixels with their solid component. Sample canonical colors from high-alpha interior regions, not blended boundaries.

Classify a variation as a real gradient only when it persists across interior pixels, has a coherent direction, and is not explained by edge coverage or compression. When the user states colors are plain, treat small deviations as raster artifacts unless strong contradictory evidence exists.

## Extract measurable geometry

### Contours and hierarchy

Use full-resolution contours for measurement:

```python
import cv2

mask_u8 = foreground_mask.astype(np.uint8) * 255
contours, hierarchy = cv2.findContours(
    mask_u8,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_NONE,
)
```

Use `RETR_TREE` when holes or nesting matter. Use contour area, perimeter, extrema, and hierarchy to associate visible components. Avoid copying every contour point into SVG.

### Connected components

Use connected components for separated tiles, dots, nodes, or color regions:

```python
count, labels, stats, centroids = cv2.connectedComponentsWithStats(
    component_mask.astype(np.uint8),
    connectivity=8,
)
```

Record each component's bounding box, area, centroid, and relation to repeated components. Repeated bounds often reveal a shared width, height, corner radius, or spacing that should become one parameter.

### Rotated rectangles

For rotated tiles, use a minimum-area rectangle:

```python
center, size, angle = cv2.minAreaRect(contour)
```

Represent the result as an editable rounded rectangle when the visible contour supports it:

```xml
<rect x="36.5" y="178.9" width="49.5" height="34.1" rx="7.3" transform="rotate(-23.2 61.25 195.95)"/>
```

OpenCV angle conventions change with rectangle orientation, so verify the rendered rotation visually.

### Straight-edge fitting

Fit long contour sections rather than eyeballing their slope:

```python
def fit_line_xy(points):
    x = points[:, 0].astype(float)
    y = points[:, 1].astype(float)
    slope, intercept = np.polyfit(x, y, 1)
    predicted = slope * x + intercept
    rmse = np.sqrt(np.mean((y - predicted) ** 2))
    return slope, intercept, rmse
```

Use intersections of fitted lines as anchors. Replace sharp raster corners with short cubic transitions when the pixels show a rounded tip. In one recovered paper-plane example, major straight edges fitted with roughly 0.3-0.9 px RMSE.

### Medial axes and local width

For chevrons and curved bands, use a medial axis as a guide to centerline and width:

```python
from skimage.morphology import medial_axis

skeleton, distance = medial_axis(component_mask, return_distance=True)
ys, xs = np.where(skeleton)
local_half_width = distance[ys, xs]
```

Do not assume the final SVG should be a stroke. Use the skeleton to understand width and flow, then build a closed filled path when caps, joins, central turns, or local widening require explicit outline control.

## Model the SVG

### Layered shapes instead of a monolith

Split a folded or overlapping mark into visual layers:

```xml
<path fill="url(#mainBody)" d="..."/>
<path fill="url(#upperWing)" d="..."/>
<path fill="url(#centralFold)" d="..."/>
<path fill="url(#innerFold)" d="..."/>
```

This preserves editability and overlap semantics. Prefer unpainted negative space between layers to a white patch over the artwork.

### Compound paths for holes

Represent a ring or hollow diamond with an outer and inner subpath:

```xml
<path d="M ... outer ... Z M ... inner ... Z" fill="#01E2F1" fill-rule="evenodd"/>
```

Keep independent dots or nodes as `<circle>` elements rather than merging everything into one path.

### Filled paths instead of strokes

Use a closed outline for irregular bands and chevrons when a stroke creates cap, miter, or width mismatches:

```xml
<path d="M ... C ... L ... C ... Z" fill="#8148FA"/>
```

A filled outline gives direct control over the top cap, central turn, lower cap, and local width.

### Continuous connected components

When a branch grows from a rounded tile, build one continuous path. A separate tile plus connector polygon can create an antialiased seam, overlap bump, or wrong branch-root contour.

### Gradients

Use small, explicit gradients only when interior sampling proves real directional variation:

```xml
<linearGradient id="upperWing" gradientUnits="userSpaceOnUse" x1="95" y1="150" x2="440" y2="40">
  <stop offset="0" stop-color="#02C1FE"/>
  <stop offset="1" stop-color="#00C0FE"/>
</linearGradient>
```

`gradientUnits="userSpaceOnUse"` keeps sampled positions aligned with source coordinates.

### Shadows

Use a low-opacity vector duplicate and a narrowly bounded Gaussian blur only when the reference visibly contains a shadow:

```xml
<filter id="softBlur" x="-25%" y="-25%" width="160%" height="165%">
  <feGaussianBlur stdDeviation="4.2"/>
</filter>
```

The recovered paper-plane example used approximately 0.06 opacity for the main shadow and 0.08 for tile shadows. Treat these as example magnitudes, not defaults.

## Fit and optimize

Start with measured primitives and manually meaningful anchors. When a regular design remains slightly off, optimize a small parameter vector such as shared width, height, radius, spacing, connector endpoints, and a few Bézier handles.

Use mask XOR as a simple loss:

```python
def mask_loss(target, candidate):
    return np.count_nonzero(np.logical_xor(target, candidate))
```

Use IoU as a normalized score:

```python
def intersection_over_union(target, candidate):
    intersection = np.count_nonzero(target & candidate)
    union = np.count_nonzero(target | candidate)
    return intersection / union if union else 1.0
```

SciPy offers both global and local optimizers:

```python
from scipy.optimize import differential_evolution, minimize
```

Use global search only for a bounded, low-dimensional problem. Follow it with local refinement if useful. Rasterize every candidate at the source size. Optimize individual component masks when full-image metrics hide local shape errors. Retain semantic equality constraints for repeated components instead of allowing each copy to drift independently.

## Compare raster and SVG

Rasterize with CairoSVG at the exact reference dimensions:

```python
import cairosvg
from PIL import Image

original = Image.open("reference.png").convert("RGB")
cairosvg.svg2png(
    url="candidate.svg",
    write_to="candidate.png",
    output_width=original.width,
    output_height=original.height,
)
```

Compute complementary metrics.

Mean absolute error:

```python
mae = np.mean(np.abs(original_rgb.astype(np.float32) - rendered_rgb.astype(np.float32)))
```

Foreground-mask IoU:

```python
original_mask = np.linalg.norm(original_rgb - background, axis=2) > 12
rendered_mask = np.linalg.norm(rendered_rgb - background, axis=2) > 12
intersection = np.count_nonzero(original_mask & rendered_mask)
union = np.count_nonzero(original_mask | rendered_mask)
iou = intersection / union
```

Structural similarity:

```python
from skimage.metrics import structural_similarity

ssim = structural_similarity(
    original_rgb.astype(np.uint8),
    rendered_rgb.astype(np.uint8),
    channel_axis=2,
    data_range=255,
)
```

Always inspect diagnostic images after numerical comparison:

- source and candidate side by side
- amplified absolute RGB difference
- binary foreground XOR
- zoomed difficult corners, caps, overlaps, and connector roots
- individual component masks

Full-image SSIM can look strong because a large blank background matches. A one-value metric can also penalize harmless rasterizer antialiasing differences. Geometry should be judged with silhouette and per-component masks plus visual inspection.

## Validate native vector content

Parse XML and reject raster payloads:

```python
from pathlib import Path
import xml.etree.ElementTree as ET

svg_path = Path("candidate.svg")
tree = ET.parse(svg_path)
root = tree.getroot()

def local_name(tag):
    return tag.rsplit("}", 1)[-1]

for element in root.iter():
    assert local_name(element.tag) != "image"

text = svg_path.read_text(encoding="utf-8")
assert "data:image/" not in text.lower()
assert "base64," not in text.lower()
```

Also reject `<foreignObject>`, scripts, and external `href` values. Report primitive, gradient, and filter counts. Validate the final variants independently after packaging.

For a white-background variant, keep artwork unchanged and add only:

```xml
<rect width="440" height="381" fill="#FFFFFF"/>
```

The transparent variant omits that rectangle.

## Lessons from three reconstructed archetypes

### Layered paper plane

- Source: 479 x 363.
- Separate the main body, upper wing, central fold, inner fold, rotated trailing tiles, and subtle shadows.
- Use color-family masks, full contours, line fits, and `minAreaRect` for the tiles.
- Preserve real smooth variation with seven small gradients.
- Use short cubic transitions at apparently sharp but visibly rounded tips.
- Final recorded structure: five paths, six rectangles, seven gradients, two blur filters, and zero raster images.
- Recorded final comparison: MAE 1.81/255, SSIM 0.9565, foreground IoU 0.9604.

### Rounded diamond and chevrons

- Source: 440 x 381.
- Treat small edge variations as antialiasing and keep three canonical solid colors.
- Use alpha/residual reconstruction for color masks.
- Use a compound even-odd path for the hollow rounded diamond, a separate circle for the center dot, and one filled path per chevron.
- Use a medial axis and distance transform to guide band centerlines and widths; the recovered purple band was about 22-23 px wide through most of its length.
- Final recorded structure: three paths, one circle, no gradients, no filters, and no raster images.
- Recorded final comparison: MAE 2.71/255, SSIM 0.9649, foreground IoU 0.9631.

### Connected regular grid

- Source: 440 x 427.
- Use color-specific connected components and shared rounded-rectangle parameters.
- Represent ordinary tiles as `<rect rx>`.
- Represent each tile-plus-diagonal-branch as one continuous Bézier path to avoid seams.
- Optimize a small geometry parameter set against component masks.
- Recorded component IoUs ranged from 0.9785 to 0.9983; irregular connector transitions scored lower than regular tiles.
- Final recorded structure: two custom paths, three teal rounded rectangles, one lime rounded rectangle, no gradients, no filters, and no raster images.
- Recorded final comparison: MAE 2.30/255, SSIM 0.9709, foreground IoU 0.9737.

These scores are case-study evidence, not universal acceptance thresholds. They include renderer antialiasing and slight background-color differences.

## Failure modes

- One-click trace: too many nodes, wobbly lines, and preserved raster noise. Rebuild semantics instead.
- Exact RGB masks: lose antialiased edges. Use alpha reconstruction and residuals.
- One giant path: obscures layers and makes editing harder. Split by visual structure.
- Stroked chevron: cap, miter, and width mismatch. Use a filled outline.
- Separate branch and tile: seam or overlap bump. Use one continuous path.
- Unjustified gradients: encode compression or antialiasing as design. Inspect interior trends.
- White patch for negative space: breaks transparent variants. Leave space unpainted or use a compound path.
- Arbitrary-size comparisons: add resampling error. Render at source dimensions.
- SSIM-only acceptance: large backgrounds can dominate. Add IoU, component masks, and visual diagnostics.
- Metric chasing: a noisy trace may score well but be a poor editable SVG. Preserve intentional geometry and low node count.
- Claiming original-vector recovery: pixels do not contain the original node graph, handles, or layer metadata.

## What exact means

A raster does not encode the original SVG nodes, Bézier handles, corner-radius values, gradients, or layer structure. Literal source recovery is impossible without the original vector. Aim to match canvas dimensions, visible contours, positions, proportions, colors, intentional gradients, corner radii, cap shapes, overlaps, layer order, and negative space while avoiding raster artifacts and unnecessary nodes. Describe the result as a close, measured reconstruction of the visible raster appearance.
