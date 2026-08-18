# Generalization playbook for inverse vector graphics

## Contents

- [Use topology and residuals to select the model](#use-topology-and-residuals-to-select-the-model)
- [Regularize toward design intent](#regularize-toward-design-intent)
- [Handle source and topology families](#handle-source-and-topology-families)
- [Validate several kinds of correctness](#validate-several-kinds-of-correctness)
- [Use the component worksheet](#use-the-component-worksheet)

## Use topology and residuals to select the model

Before fitting coordinates, inventory connected components, holes and their nesting, open gaps, true subtractions, touching and overlap relations, occlusion order, and the required `nonzero` or `evenodd` fill behavior. A white knockout that looks correct on white is not a hole and will fail on transparent or dark backgrounds.
Choose a model independently for each semantic component. One mark can legitimately combine transformed primitives, analytical arcs, periodic splines, piecewise paths, and layered effects.
Use this escalation ladder:

```text
SVG primitive
-> transformed primitive
-> repeated primitive with shared parameters
-> compound or Boolean primitive
-> low-dimensional parametric curve
-> semantically segmented piecewise Bézier path
-> periodic spline for a globally smooth closed contour
-> simplified general contour fit as a last resort
```

Do not escalate because the next model is available or improves one aggregate metric slightly. Escalate when the simpler model leaves a stable, coherent residual that corresponds to visible structure.

### Read the shape of the residual

| Residual pattern                                           | Likely diagnosis                                                  | Next test                                               |
| ---------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| Errors at all four rounded corners                         | Corner radius or rectangle dimensions are wrong                   | Refit a shared `rx`, width, and height                  |
| Alternating inside/outside errors around four quadrants    | A presumed circle is elliptical, rotated, or non-uniformly scaled | Compare circle and ellipse hypotheses                   |
| Opposite-sign errors along the two boundaries of a band    | Centerline placement or width is wrong                            | Measure a medial axis and width profile                 |
| Error follows the full length of a nominally straight span | A free curve is absorbing what should be a line                   | Fit the span with robust line regression                |
| Error clusters at tips, notches, cusps, or folds           | Global smoothing is destroying semantic discontinuities           | Split the contour and use `C0` joins where intentional  |
| Error exists only on a one-pixel antialiased fringe        | Geometry may already be correct and the renderer differs          | Compare a second renderer and enlarged contour overlays |
| Error repeats at every transformed copy                    | A shared master parameter is wrong                                | Optimize the master before allowing per-copy deviations |

Use `C0` continuity at deliberate corners, `C1` tangent continuity at smooth joins, and `C2` only when the design visibly benefits. Never force smoothness through a cap, cusp, notch, or fold.

## Regularize toward design intent

A clean vector should explain the raster without fossilizing export defects. Conceptually optimize:

```text
loss = geometry error
     + color error
     + topology penalty
     + path-complexity penalty
     + unsupported-asymmetry penalty
```

When the evidence supports it, share radii, widths, spacing, rotation intervals, alignment lines, and mirrored control handles. Permit deviations only when they are systematic and visible. Preserve deliberate irregularity in hand-drawn or brush marks; regularization is a hypothesis, not permission to sterilize the artwork.
Fit coarse-to-fine. At reduced resolution optimize centers, major radii, rotation, width, and endpoints. At source resolution refine radii, notch depth, tangent handles, cap shapes, and pixel alignment. Inspect the result at a practical small size and at 4x or greater zoom so an apparent source-size match does not hide overfitting to one antialiasing pattern.
Reject pathological exported geometry: microscopic segments, nearly duplicate points, backtracking handles, unintended loops or self-intersections, and excessive decimals. Round only after the rendered result is accepted.

## Handle source and topology families

### Text and wordmarks

Use OCR only to identify characters. Determine whether the mark uses a font or custom lettering; obtain the source font when possible; reconstruct baselines, kerning, counters, stem consistency, and overshoots. Keep live `<text>` only when the exact font and deployment/licensing conditions are known. Otherwise convert verified glyph geometry to paths. Blind contour tracing preserves raster softness and damages typographic systems.

### Perspective, non-uniform backgrounds, and photographs

For signage, packaging, screens, or other planar captures, detect the plane, estimate a homography, rectify to a frontal view, then vectorize. Do not bake photographic perspective into a reusable logo unless the distortion is intentional. On textured or spatially varying backgrounds, estimate a local background field or use segmentation/matting; do not force a global corner median or mistake background texture for artwork.

### Very low resolution and compression

Upscaling interpolates pixels; it does not recover geometry. Compare several constrained hypotheses using symmetry, tangency, shared radii, repetition, and grid alignment, then prefer the simplest plausible design and label inferred details. For JPEGs and screenshots, estimate ringing from a larger crop, favor evidence accumulated over long spans, and treat comparison against a lightly blurred reference only as a secondary diagnostic.

### Pixel art

Use a separate grid model. Detect the source cell size, snap to integer coordinates, reconstruct with rectangles or polygons, avoid Gaussian smoothing and splines, optionally set `shape-rendering="crispEdges"`, and validate without antialiasing.

### Constant-width, variable-width, and calligraphic bands

Choose among a centerline stroke, a centerline plus a width function, two independently fitted boundaries, or one closed outline. Use an SVG stroke only when width, caps, joins, and renderer behavior are sufficiently constant. A tapered rail or calligraphic mark generally needs a filled outline.

### Woven marks, knots, and self-intersections

Build a crossing graph and determine over/under order at each crossing. Split the design into layered ribbon segments rather than relying on one self-intersecting outline. Use masks or clips only when semantic layering cannot express the topology cleanly, and validate on non-white backgrounds.

### Clipped, occluded, and incomplete shapes

For an exact visible reconstruction, hidden geometry is unnecessary. For a reusable editable asset, reconstruct full hidden primitives only when symmetry, repetition, or a clear continuation strongly supports the inference. Record uncertain hidden geometry instead of presenting it as measured fact.

### Isometric and three-dimensional marks

Separate visible faces and infer shared parallel line families, face adjacency, and affine transformations. Treat shading boundaries as fills on semantic faces, not arbitrary contour splits. Preserve a consistent layer order at overlaps.

### Translucent overlaps

Observed color can be the result of compositing rather than an independent fill:

```text
pixel = alpha * foreground + (1 - alpha) * background
```

With multiple translucent layers, order is part of the model. Fit geometry and alpha-bearing layers jointly enough to explain overlap colors, but score core silhouettes separately from compositing effects.

### Shadows, glows, blur, texture, and painterly marks

Keep a core geometry mask separate from an effect-inclusive visual mask. Rebuild intentional shadows or glows as separate low-opacity vector layers with bounded filters; never let blur redefine the core silhouette or conceal inaccurate geometry. For texture, first agree whether strict native SVG or hybrid output is required. Under a native-vector constraint, preserve recognizable structure and approximate texture with a small number of gradients, patterns, or filters rather than thousands of tiny paths. Embed raster texture only with explicit permission and disclose it.

## Validate several kinds of correctness

No single score proves a good reconstruction. Separate these checks:

### Structural

- Parse XML and test-render the SVG.
- Confirm the `viewBox`, positive finite dimensions, and finite coordinates.
- Reject forbidden `<image>`, Base64/data-image payloads, scripts, external references, empty geometry, and accidental off-canvas objects.
- Keep a self-contained generator or verified numeric specification so the final asset does not depend on unsaved interactive state.

### Topological

- Compare component count, hole count and nesting, containment, adjacency, overlap, and fill behavior.
- Repeat connectivity checks at several nearby alpha or luminance thresholds because one antialiased threshold can merge or split components spuriously.
- Composite transparent output on light, black, mid-gray, and checkerboard backgrounds to expose white knockouts, halos, seams, and unintended opacity.

### Geometric

- Report global and per-component IoU, but inspect the spatial residual too.
- Measure symmetric boundary distance in both directions and report median, p95, and maximum. A good median can hide one failed tip or notch.
- For difficult geometry, add signed-distance-field error and landmark displacement at extrema, corners, caps, and semantic junctions.

### Color and effects

- Compare RGB and perceptual CIEDE2000 error on an eroded intersection of target and rendered interiors.
- Adjust erosion to component scale; a fixed large kernel can erase thin artwork.
- Compare constant and low-dimensional spatial color models before accepting a gradient.
- Score core geometry separately from shadow/glow-inclusive appearance.

### Renderer and scale portability

- Use another renderer for masks, filters, clip paths, complex joins, elliptical arcs and flags, unusual fill rules, nested transforms, or `<use>` when compatibility matters.
- Inspect source resolution, a practical small icon size, and 4x or greater zoom.
- Treat metric ranges as case evidence, never universal pass/fail thresholds. Report ambiguity when several clean models explain the pixels.

## Use the component worksheet

Record one worksheet per semantic foreground component:

```text
Component:
Color family:
Bounding box:
Connected to / overlaps / occluded by:
Contains holes and required fill rule:

Boundary evidence:
- straight spans:
- constant-curvature spans:
- sharp corners, cusps, and notches:
- symmetry or repetition:
- width profile:

Candidate models, simplest first:
1.
2.
3.

Structured residual that rejects the simpler model:
Chosen SVG representation:
Shared parameters and constraints:
Measured facts versus inferred geometry:

Validation:
- component IoU:
- symmetric boundary median / p95 / max:
- eroded-interior RGB MAE / CIEDE2000:
- topology threshold sweep:
- light / dark / gray / checkerboard:
- small / source / enlarged renders:
- second renderer when needed:
```
