---
name: raster-to-clean-svg
description: Use this skill to reconstruct a raster logo, icon, glyph, or flat illustration from PNG, JPEG, or WebP as a clean, editable, native SVG. Trigger when the user wants faithful geometry, colors, curves, gradients, shadows, or transparent and white-background variants; forbids ImageGen or generic autotracing; requires no embedded raster; or asks for quantitative raster-versus-SVG validation.
metadata:
  author: EDM115
---

# Reconstruct raster artwork as clean SVG

Recover the visible design as intentional SVG geometry. Treat the task as inverse vector graphics: infer the simplest design system that could have generated the pixels, reconstruct that system, render it at the original size, compare it with the source, and iterate. Do not treat an autotrace or a PNG wrapped in `<image>` as a successful result.

## Non-negotiable rules

- Keep the source raster immutable.
- Use the source width and height as the SVG `viewBox` whenever practical so one SVG unit equals one source pixel.
- Do not use ImageGen unless the user explicitly reverses that constraint.
- Do not embed raster data, external images, Base64 payloads, or `<image>` elements.
- Prefer a small number of editable `<rect>`, `<circle>`, `<ellipse>`, gradient, and deliberate `<path>` elements over contour noise.
- Reconstruct visual appearance, layer order, and negative space. Do not claim to recover unavailable original control points or layer metadata.
- Distinguish intentional gradients and shadows from antialiasing, compression, and resampling artifacts. Respect a user's statement that colors are plain.
- Validate both syntax and appearance before calling the result complete.

## Prepare the work

1. Inspect the raster visually, including zoomed crops. Record its pixel dimensions, background behavior, visible components, likely symmetries, repeated dimensions, colors, and layer order.
2. Decide which deliverables are required: transparent SVG, on-white SVG, preview PNG, comparison images, and optional ZIP.
3. Create a task-local working directory for masks, renders, and diagnostics. Keep these intermediate files out of the final deliverables unless the user asks for them.
4. Read [references/reconstruction-method.md](references/reconstruction-method.md) before measuring or fitting geometry. It contains the core recovered formulas, SVG patterns, worked archetypes, and metric interpretation.
5. Read [references/advanced-fitting.md](references/advanced-fitting.md) when the artwork contains elliptical rings, organic closed blades, mixed sharp-and-curved rails, subtle spatial gradients, or geometry that needs component-specific fitting.
6. Read [references/generalization-playbook.md](references/generalization-playbook.md) when choosing between competing models, diagnosing structured residuals, handling typography, perspective, pixel art, low-resolution or compressed sources, occlusion, woven marks, translucent layers, texture, or planning multi-background, multi-scale, and multi-renderer validation.

## Measure the raster

Run the bundled probe when Python and `uv` are available:

```bash
uv run scripts/probe_raster.py reference.png --out-dir work/probe
```

For known solid fills, pass each expected color so the probe classifies antialiased edge pixels by alpha reconstruction instead of exact RGB equality:

```bash
uv run scripts/probe_raster.py reference.png --out-dir work/probe --fill "#01E2F1" --fill "#0161FA" --fill "#8148FA"
```

Use the report, masks, component overlay, and visual inspection together. Measurements are evidence, not an automatic tracing result. Tune `--threshold`, `--corner-size`, and `--residual-threshold` when the background is textured, compressed, or not close to uniform.

## Choose geometry deliberately

Use the simplest primitive that preserves the visible contour:

| Raster structure                               | Preferred SVG model                                             |
| ---------------------------------------------- | --------------------------------------------------------------- |
| Axis-aligned or rotated rounded tile           | `<rect rx>` with an optional rotation                           |
| Circular node or dot                           | `<circle>` or `<ellipse>`                                       |
| Ring or shape with a true hole                 | Compound `<path fill-rule="evenodd">`                           |
| Gapped circular or elliptical annulus          | Independently fitted outer and inner SVG `A` arcs               |
| Smooth organic closed blade                    | Periodic cubic B-spline converted to closed cubic Béziers       |
| Rail with sharp tips, notches, and long curves | Semantically segmented, piecewise Bézier path                   |
| Chevron, ribbon, blade, fold, or irregular cap | Closed filled Bézier path                                       |
| Branch fused into a tile                       | One continuous path, not overlapping pieces that can form seams |
| Layered folded mark                            | Several simple paths in visual stacking order                   |
| Real smooth color variation                    | Small `userSpaceOnUse` linear or radial gradient                |
| Real soft shadow                               | Low-opacity vector duplicate and a narrowly bounded blur filter |

Prefer filled outlines over stroked polylines when line caps, joins, turns, or local width changes do not match the raster. Create negative space by leaving an area unpainted or by using a compound path; avoid painting white shapes unless the source truly contains a white layer.

Escalate through primitive, transformed/repeated primitive, compound or Boolean structure, parametric curve, piecewise Bézier, periodic spline, and only then general contour fitting. Accept a more complex model when the simpler one leaves a coherent visible residual, not merely because a scalar score improves fractionally.

## Build and refine

1. Select a topology-appropriate model before fitting. Do not treat every component as the same contour-smoothing problem.
2. Establish the main anchors from contour extrema, line fits, centroids, repeated spacing, symmetry, and primitive bounds.
3. Build large silhouettes first. Add internal layers, holes, gradients, and shadows only after the outer geometry is stable.
4. Use cubic Bézier curves only where the contour bends. Keep long straight edges as lines and minimize nodes.
5. Parameterize repeated dimensions and uncertain control points. For regular geometry, optimize a small parameter vector against mask XOR or per-component IoU; do not optimize hundreds of raw contour points.
6. Rasterize every meaningful candidate at the exact source dimensions. Avoid comparing after arbitrary resizing because it adds another resampling layer.
7. Inspect the original and candidate side by side, then inspect the XOR mask, amplified pixel difference, and zoomed problem areas.
8. Refine in this order: overall silhouette, placement and scale, component spacing, corner radii and cap shapes, internal overlaps, colors, then subtle gradients or shadows.

## Validate the candidate

Run the validator against the source raster:

```bash
uv run scripts/validate_svg.py candidate.svg --reference reference.png --out-dir work/validation
```

The validator parses XML, detects forbidden raster/script content, non-finite attributes, and external references, rasterizes at source dimensions with CairoSVG when available or the portable `resvg_py` fallback, reports element counts, and produces MAE, SSIM, foreground-mask IoU, matched connected-component IoU, symmetric boundary median/p95/max distance, eroded-interior RGB MAE and CIEDE2000, side-by-side, amplified difference, and directional mask-difference diagnostics.

Interpret the metrics carefully:

- Use full-image MAE to detect broad color or background errors.
- Treat full-image SSIM as secondary for logos with large uniform backgrounds.
- Use foreground IoU for overall silhouette agreement.
- Prefer per-component IoU and zoomed visual inspection when geometry is composed of separate regular parts.
- Use eroded-interior color MAE to judge fills and gradients without conflating them with renderer-specific edge antialiasing.
- Do not invent a universal pass threshold. A visually faithful, editable reconstruction with a few antialiasing differences can be better than a noisy high-node trace with a slightly better pixel score.

## Deliver

Provide the requested SVG variants and a rendered preview. If both transparent and white variants are needed, keep the artwork identical and add only a background rectangle to the white version. Before handoff, verify:

- XML parses successfully.
- The `viewBox` and output dimensions match the source.
- No `<image>`, `<foreignObject>`, script, data-image URI, Base64 raster, or external `href` exists.
- Paths are closed where intended and the SVG remains editable.
- Gradients, filters, and masks exist only when visually justified.
- Final renders were compared at the source size.
- Transparent construction was inspected on light, dark, mid-gray, and checkerboard backgrounds when negative space, transparency, masks, filters, or overlaps make the result background-sensitive.
- The artwork was also inspected at a practical small size and enlarged scale, and a second renderer was used for complex arcs, fills, strokes, masks, filters, clips, transforms, or `<use>` when portability matters.
- Reported metrics come from the final files, not an earlier candidate.

Use this concise completion report:

```text
Canvas: <width> x <height>
Composition: <primitive counts, gradients, filters>
Native-vector checks: PASS/FAIL
Comparison: MAE=<value>, SSIM=<value>, foreground IoU=<value>
Variants: <transparent, white, preview, archive>
Limit: reconstructed from pixels; unavailable original nodes cannot be recovered literally
```

## Bundled helpers

- `scripts/probe_raster.py` — estimate background, create a foreground mask, inventory contours and connected components, estimate dominant interior colors, and optionally classify known solid fills through alpha/residual fitting.
- `scripts/fit_closed_contour.py` — smooth one organic binary component, extract its subpixel half-coverage contour, fit a periodic cubic B-spline, and export equivalent editable SVG cubic Béziers.
- `scripts/validate_svg.py` — enforce native-vector checks, render the SVG, compute comparison metrics, and emit diagnostic images plus JSON.
- `references/reconstruction-method.md` — load before reconstruction for formulas, code patterns, fitting strategies, worked archetypes, and failure modes.
- `references/advanced-fitting.md` — load for topology-specific analytical arcs, periodic splines, piecewise paths, spatial gradient models, and component-specific validation.
- `references/generalization-playbook.md` — load for model escalation, residual diagnosis, unseen topology/source playbooks, regularization, and broader validation strategy.
