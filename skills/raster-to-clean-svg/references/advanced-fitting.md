# Advanced topology-specific fitting

## Contents

- [Choose a reconstruction model by topology](#choose-a-reconstruction-model-by-topology)
- [Fit a gapped elliptical annulus](#fit-a-gapped-elliptical-annulus)
- [Fit organic closed blades with periodic splines](#fit-organic-closed-blades-with-periodic-splines)
- [Fit mixed sharp and curved rails piecewise](#fit-mixed-sharp-and-curved-rails-piecewise)
- [Optimize a rotated rounded rectangle](#optimize-a-rotated-rounded-rectangle)
- [Model spatially varying foreground colors](#model-spatially-varying-foreground-colors)
- [Validate by component and interior color](#validate-by-component-and-interior-color)
- [Case-study evidence](#case-study-evidence)
- [Advanced gotchas](#advanced-gotchas)

## Choose a reconstruction model by topology

Do not reduce every raster-to-SVG task to generic contour fitting. First classify the component's topology and meaningful geometric regions:

| Topology                                                                   | Preferred reconstruction model                                                                                 |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Gapped circular or orbital ring with overlapping nodes                     | Independently fitted outer and inner ellipses exported as SVG elliptical arcs, plus layered ellipses for nodes |
| Smooth organic closed blade with no meaningful corners                     | Smoothed subpixel contour, periodic cubic B-spline, then exact cubic Bézier conversion                         |
| Rail containing long curves, sharp tips, angled edges, and concave notches | Semantic contour segmentation and piecewise Bézier fitting                                                     |
| Rotated rounded tile                                                       | `minAreaRect` initialization followed by low-dimensional optimization while retaining `<rect rx transform>`    |
| Folded or overlapping mark                                                 | Several semantic vector layers rather than one traced union                                                    |

Use global smoothing only for shapes whose entire boundary is meant to be smooth. Preserve meaningful discontinuities and high-curvature regions through segmentation or analytical primitives.

## Fit a gapped elliptical annulus

An apparently circular ring may be slightly elliptical after non-uniform scaling, rotation, rasterization, or earlier transformations. The outer and inner boundaries may also have different centers, radii, and rotations. Measure rather than forcing concentric circles.

### Exclude occlusions and gap caps

Remove contour regions occupied by overlapping nodes and by the intentional gap before fitting the annulus. The exact bounds are image-specific:

```python
px = contour[:, 0].astype(float)
py = contour[:, 1].astype(float)

exclude = (
    ((px >= node_1_x0) & (px <= node_1_x1) & (py >= node_1_y0) & (py <= node_1_y1))
    | ((px >= node_2_x0) & (px <= node_2_x1) & (py >= node_2_y0) & (py <= node_2_y1))
    | ((px >= node_3_x0) & (px <= node_3_x1) & (py >= node_3_y0) & (py <= node_3_y1))
    | ((px >= gap_x0) & (px <= gap_x1) & (py >= gap_y0) & (py <= gap_y1))
)

ring_points = contour[~exclude].astype(float)
```

Use masks or polygonal exclusion regions instead of rectangles when components overlap more tightly.

### Separate inner and outer samples

Classify points relative to a provisional middle ellipse. For an axis-aligned provisional model:

```python
q = np.sqrt(
    ((ring_points[:, 0] - center_x) / radius_x) ** 2
    + ((ring_points[:, 1] - center_y) / radius_y) ** 2
)

outer_points = ring_points[q > 1.02]
inner_points = ring_points[q < 0.98]
```

Rotate the samples into the provisional ellipse's local coordinate frame when the ellipse is rotated. Leave a small dead band around `q == 1` so uncertain points do not contaminate either fit.

Fit the outer and inner ellipses independently. Use a bounded global optimizer such as `scipy.optimize.differential_evolution` for uncertain initialization, then refine the parameters against the extracted component mask with `least_squares` or `minimize`.

### Export native elliptical arcs

Represent a gapped annulus with an outer `A` command, one gap edge, an inner `A` command in the opposite direction, and the second gap edge:

```xml
<path d="
  M outer_start_x outer_start_y
  A outer_rx outer_ry outer_rotation large_arc_flag sweep_flag outer_end_x outer_end_y
  L inner_end_x inner_end_y
  A inner_rx inner_ry inner_rotation large_arc_flag reverse_sweep inner_start_x inner_start_y
  Z
"/>
```

This is more compact and editable than approximating the entire ring with dozens of cubic segments. Examine the gap contour separately and fit straight cap regions independently from the elliptical portions; a RANSAC-style line fit can help reject nearby arc samples.

### Decompose overlapping semantic objects

One connected raster component can represent several objects whose visible union overlaps. Build the ring first, layer separately fitted node ellipses over it, then add the center tile. Do not trace the fused union unless the union itself is the intended editable object.

Fit visually circular nodes as `<ellipse>` when measured `rx` and `ry` differ. A shape that began as a circle may no longer rasterize as one after scaling.

## Fit organic closed blades with periodic splines

Use this method only for genuinely smooth closed silhouettes whose widths, inner and outer curves, and endpoints vary organically. Do not apply it to contours with intentional sharp tips, corners, or notches.

### Clean the component before extracting a contour

Keep the largest connected component, apply a small Gaussian blur, then extract a subpixel contour at half coverage:

```python
import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.measure import find_contours

def cleaned_contour(mask, sigma=0.8, level=0.5):
    mask_u8 = mask.astype(np.uint8)
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask_u8, connectivity=8)
    if count <= 1:
        raise ValueError("Mask contains no foreground component")

    component_index = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
    component = (labels == component_index).astype(float)
    smoothed = gaussian_filter(component, sigma=sigma)
    contours = sorted(find_contours(smoothed, level), key=len, reverse=True)
    if not contours:
        raise ValueError("No contour found at the requested level")

    # skimage returns y, x; convert to x, y.
    return np.column_stack([contours[0][:, 1], contours[0][:, 0]])
```

The `0.5` level approximately follows the half-coverage boundary of an antialiased raster silhouette. A small `sigma` such as `0.8` suppresses one-pixel stair-stepping without intentionally redesigning the contour.

### Fit a periodic cubic B-spline

```python
from scipy.interpolate import splprep

tck, _ = splprep(
    [points[:, 0], points[:, 1]],
    s=smoothing_amount,
    per=True,
    k=3,
)
```

Sweep Gaussian `sigma`, spline smoothing `s`, segment count, and mask IoU together:

- Too little smoothing preserves pixel noise and creates excessive segments.
- Too much smoothing moves tips and local curvature.
- Choose the smallest path that preserves the measured silhouette and distinctive local shape.

Do not select `s` from appearance alone. Render each candidate, record the number of resulting cubic segments, measure component IoU, and inspect sensitive endpoints at high zoom.

### Convert each spline interval to an SVG cubic Bézier

SVG does not store a SciPy B-spline directly. Convert every non-zero knot interval through its endpoint positions and derivatives:

```python
import numpy as np
from scipy.interpolate import BSpline

def bspline_to_cubic_segments(tck):
    knots, coefficients, degree = tck
    if degree != 3:
        raise ValueError("Expected a cubic B-spline")

    coefficients = np.asarray(coefficients).T
    curve = BSpline(knots, coefficients, degree)
    derivative = curve.derivative()
    valid_end = len(coefficients)
    breaks = np.unique(knots[degree : valid_end + 1])
    segments = []

    for u0, u1 in zip(breaks[:-1], breaks[1:]):
        if u1 <= u0:
            continue
        delta = u1 - u0
        p0 = curve(u0)
        p3 = curve(u1)
        p1 = p0 + derivative(u0) * delta / 3.0
        p2 = p3 - derivative(u1) * delta / 3.0
        segments.append((p0, p1, p2, p3))

    return segments
```

For each interval, the Hermite-to-Bézier relationship is:

```text
P1 = P0 + derivative(u0) * (u1 - u0) / 3
P2 = P3 - derivative(u1) * (u1 - u0) / 3
```

Write one `M`, one `C` per interval, and `Z`. Run `scripts/fit_closed_contour.py` for this operation, then validate the exported path against the component mask.

## Fit mixed sharp and curved rails piecewise

A global periodic spline is inappropriate when one contour contains both smooth arcs and meaningful discontinuities. Plot contour indices and mark semantic transition points such as:

- upper tip
- straight or nearly straight upper edge
- notch entrance
- concave rounded notch
- notch exit
- long outer arc
- tapered lower tip
- inner return curve

Split at those points and choose a model for each region: line, analytical arc, or cubic Bézier. Join adjacent pieces with the continuity the design requires; do not force tangent continuity at an intentional corner.

Sweep the curve-fitting tolerance and retain a compactness-versus-fidelity table. One recorded experiment produced:

```text
Error tolerance 0.6 px -> 34 cubic segments
Error tolerance 0.8 px -> 28 cubic segments
Error tolerance 1.0 px -> 23 cubic segments
Error tolerance 1.5 px -> 19 cubic segments
Error tolerance 2.0 px -> 16 cubic segments
```

Inspect sharp tips and concave notches at every tolerance. Global smoothing can round tips or partially fill notches even while overall IoU remains strong.

Integrate notches into the closed path. Do not fake them with white or background-colored overlays: that breaks transparent variants and can create antialiasing seams. Use explicit concave path geometry, a compound-path hole, a vector Boolean subtraction, or a transparency-preserving mask when truly necessary.

## Optimize a rotated rounded rectangle

Initialize with OpenCV:

```python
initial_rect = cv2.minAreaRect(contour[:, None, :].astype(np.float32))
```

Refine the semantic parameters `cx`, `cy`, `width`, `height`, `corner_radius`, and `rotation` against the target mask:

```python
from scipy.optimize import minimize

def loss(parameters):
    candidate_mask = rasterize_rotated_rounded_rect(parameters)
    xor = np.count_nonzero(candidate_mask ^ target_mask)
    area_penalty = abs(candidate_mask.sum() - target_mask.sum())
    return xor + 0.1 * area_penalty

result = minimize(loss, initial_parameters, method="Powell")
```

Retain the result as `<rect rx transform="rotate(...)"/>` rather than converting it to an arbitrary outline path.

OpenCV can swap the reported width and height and change its angle convention according to orientation. Normalize equivalent rectangle representations or render both before optimization. Never copy the raw angle into SVG without visual and mask verification.

## Model spatially varying foreground colors

Fixed-fill alpha reconstruction assumes one foreground RGB value:

```text
pixel = alpha * foreground + (1 - alpha) * background
```

For a real smooth gradient, model the foreground as a function of position:

```text
pixel(x, y) = alpha(x, y) * foreground(x, y) + (1 - alpha(x, y)) * background
```

Fit an RGB plane to deeply interior pixels:

```python
import numpy as np
from sklearn.linear_model import LinearRegression

yy, xx = np.mgrid[0:height, 0:width]
samples = interior_mask
positions = np.column_stack([xx[samples], yy[samples]])
colors = rgb[samples].astype(float)

model = LinearRegression().fit(positions, colors)
predicted_foreground = model.predict(
    np.column_stack([xx.ravel(), yy.ravel()])
).reshape(height, width, 3)
```

Estimate per-pixel coverage and residual using the predicted foreground:

```python
direction = predicted_foreground - background
pixel_delta = rgb.astype(float) - background
denominator = np.sum(direction * direction, axis=2)
alpha = np.sum(pixel_delta * direction, axis=2) / np.maximum(denominator, 1e-9)
alpha = np.clip(alpha, 0.0, 1.0)
reconstructed = background + alpha[..., None] * direction
residual = np.linalg.norm(rgb.astype(float) - reconstructed, axis=2)
```

Do not export the arbitrary three-channel regression plane directly. Determine its dominant color-change direction and compress the measured variation into a conventional two-stop SVG linear gradient. Keep a solid fill when the spatial variation is weak, inconsistent, or better explained by raster artifacts.

## Validate by component and interior color

### Composite over the measured source background

Reference backgrounds are often close to, but not exactly, white. Composite a transparent candidate over the measured background before calculating global metrics. Rendering directly with that background color is equivalent when the renderer supports it.

### Match connected components

Report global foreground IoU, then match each target component with the rendered component that maximizes IoU. Use those scores to find one weak blade, node, rail, or tile hidden by a strong whole-image score. Treat fused semantic objects as a signal to evaluate purpose-built component masks rather than trusting connected-component labels.

### Separate color error from edge geometry

Erode the target mask before comparing colors:

```python
kernel = np.ones((9, 9), dtype=np.uint8)
interior = cv2.erode(target_mask.astype(np.uint8), kernel).astype(bool)
color_mae = np.abs(
    candidate_rgb[interior].astype(float)
    - source_rgb[interior].astype(float)
).mean(axis=0)
```

This answers two different questions:

1. Does the silhouette match?
2. Do the interior fills or gradients match?

Without erosion, renderer-specific edge antialiasing mixes these errors. Adjust the erosion kernel to component scale; a `9 x 9` kernel is inappropriate for very thin components.

### Keep local diagnostics

Inspect source and candidate side by side, the candidate alone, per-component XOR, amplified RGB difference, contour overlays with point indices, and crops around notches, tips, gaps, and intersections.

## Case-study evidence

### Circular nodes and orbit

- Source canvas: 618 x 558.
- Final structure: one compound elliptical-arc path for the gapped annulus, three ellipses for nodes, one rounded rectangle for the orange center, solid fills, and no filters or raster content.
- Semantic layering replaced a trace of the connected ring-and-node union.

### Five-blade pinwheel

- Source canvas: 682 x 771.
- Final structure: five closed cubic-Bézier blade paths, one rounded center rectangle, and six subtle two-stop gradients.
- Recorded per-blade IoU during smoothing sweeps: approximately 0.973-0.989.
- Recorded final whole-silhouette IoU: approximately 0.980; SSIM: approximately 0.977.

### Dual rails and rotated lime rectangle

- Hybrid piecewise fitting preserved long arcs, sharp upper tips, concave notches, angled edges, and tapered lower endpoints.
- The lime object remained an optimized, editable rotated rounded rectangle.
- Recorded component IoU: lime rectangle 0.992, purple rail 0.979, cyan rail 0.977.
- Recorded full-image SSIM: approximately 0.981; component scores were considered more informative.

These values are evidence from particular reconstructions, not universal thresholds.

## Advanced gotchas

- A visible circle may fit better as an ellipse after source scaling or transformation.
- The inner and outer boundaries of a rasterized ring may not be concentric; fit them independently.
- One connected raster component may represent several semantic vector objects; decompose by design intent.
- Global smoothing damages meaningful tips, notches, angled edges, and corners.
- Periodic smoothing is appropriate for organic closed contours, not every closed contour.
- White overlays are not valid transparent-vector construction.
- `minAreaRect` width, height, and angle conventions must be normalized and rendered before acceptance.
- Gradient models should be fitted from eroded interior pixels, then simplified for SVG export.
- Whole-image SSIM can hide weak foreground geometry; inspect component IoU.
- Availability checks for Potrace or other tracing libraries are environment-specific. The recorded conversions used SciPy and custom conversion code instead of depending on those packages.
