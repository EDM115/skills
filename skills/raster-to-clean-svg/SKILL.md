---
name: raster-to-clean-svg
description: Use when reconstructing a raster logo, icon, glyph, or flat illustration as a faithful, editable native SVG, or when validating its geometry, colors, transparency, and raster-versus-vector fidelity.
metadata:
  author: EDM115
---

# Reconstruct raster artwork as clean SVG
Infer the simplest design system that explains the pixels, rebuild it as intentional geometry, and compare an exact-size render with the source. Preserve domain structure rather than tracing export noise.

## Output contract and modes
- Keep the source raster immutable. Use its width and height as the SVG `viewBox` whenever practical so one unit equals one source pixel.
- **Native-vector mode is the default:** deliver editable primitives and deliberate paths, with no embedded raster, `<image>`, Base64 payloads, or external image dependencies. Preserve true holes, negative space, layer order, and intentional gradients/shadows. Respect a user's statement that fills are plain.
- **Hybrid output is outside native-vector mode:** use it only when the user explicitly requests or permits raster-backed texture. Existing explicit permission is sufficient; disclose which parts are raster-backed and that the result is not fully native vector. The bundled validator enforces native mode and rejects hybrid files; do not bypass it or label hybrid output as passing native checks. Validate authorized hybrid XML, dependencies, dimensions, and rendered appearance separately with an appropriate renderer.
- Use local reconstruction for this native-SVG task. Do not substitute ImageGen or generic autotracing for editable geometry. Follow an explicit change in the user's requested output mode.
- Validate syntax and appearance before handoff. Describe the result as reconstructed visible design; original control points and layer metadata cannot be recovered from pixels alone.

## Reconstruction loop
1. **Inspect:** view the source and necessary crops; establish dimensions, transparency/background, components, colors, repeated geometry, symmetries, and stacking. Derive requested variants from the brief. Keep task-local masks/renders separate from deliverables.
2. **Model:** choose topology before fitting coordinates, using the table below. For a simple solid circle or rounded tile, direct center/radius/bounds measurements can be enough; the probe and detailed references are optional when they would not resolve uncertainty.
3. **Build:** establish main anchors and large silhouettes, then holes and internal layers. Share parameters for repeated elements. Use lines for straight spans and a small number of Bézier nodes for bends. Fit low-dimensional parameters instead of hundreds of contour points.
4. **Compare:** render at the original dimensions, inspect side-by-side, directional mask differences, and zoomed residuals. For transparent sources compare alpha geometry separately from RGB appearance composited onto identical backgrounds.
5. **Refine:** fix silhouette, placement/scale, spacing, corners/caps, overlaps, then colors and effects. Escalate model complexity only for coherent visible residuals. Stop when meaningful discrepancies are resolved and remaining differences are attributable to source uncertainty or rasterizer antialiasing; document those limits instead of chasing a universal metric threshold.

## Choose geometry deliberately
| Raster structure | Preferred SVG model |
| --- | --- |
| Rounded tile, rotated or repeated | `<rect rx>` with transforms/shared dimensions |
| Circular node or dot | `<circle>` or `<ellipse>` |
| True hole or ring | Compound `<path fill-rule="evenodd">` |
| Gapped circular/elliptical annulus | Independently fitted inner and outer `A` arcs |
| Smooth organic closed blade | Periodic spline converted to closed cubic Béziers |
| Sharp tips/notches joined to long curves | Semantically segmented piecewise Bézier path |
| Fused branch and tile | One continuous path to avoid seams |
| Folded/layered mark | Simple closed paths in visual stacking order |
| Intentional color variation or soft shadow | Small gradient or low-opacity vector duplicate with bounded blur |
Prefer filled outlines when stroke caps, joins, or varying widths cannot explain the source. Leave negative space unpainted or form a true hole; a white knockout changes a transparent design. Escalate from primitives through transformed/repeated and compound geometry to parametric curves, piecewise Béziers, periodic splines, and finally contour fitting.

## Load resources when needed
Resolve the following paths relative to this skill's directory, not the user's project. With `uv`, the scripts declare their own dependencies; otherwise use a compatible Python environment with those dependencies installed.
| Need | Resource |
| --- | --- |
| Measurement formulas, alpha-aware fill estimation, fitting examples, or metric interpretation | [reconstruction-method.md](references/reconstruction-method.md) |
| Elliptical arcs, organic closed contours, mixed sharp/curved rails, or spatial gradients | [advanced-fitting.md](references/advanced-fitting.md) |
| Competing models, structured residuals, typography, perspective, pixel art, occlusion, woven/translucent marks, or texture | [generalization-playbook.md](references/generalization-playbook.md) |
| Background estimate, masks, components, contours, and dominant interior colors | `scripts/probe_raster.py` |
| One smooth organic binary component needing a periodic spline | `scripts/fit_closed_contour.py` |
| Native-vector preflight, exact-size render, quantitative comparison, and diagnostics | `scripts/validate_svg.py` |
Read only the reference needed for the current uncertainty. Preserve specialist formulas and examples in the references rather than loading them for every reconstruction.
```bash
uv run scripts/probe_raster.py reference.png --out-dir work/probe
uv run scripts/probe_raster.py reference.png --out-dir work/probe --fill "#01E2F1" --fill "#0161FA"
uv run scripts/validate_svg.py candidate.svg --reference reference.png --out-dir work/validation
uv run scripts/validate_svg.py candidate.svg --reference reference.png --out-dir work/validation --comparison-background "#000000" --comparison-background "#808080"
```
Known `--fill` colors enable alpha/residual classification of antialiased pixels. Probe masks are evidence, not automatic vector geometry. Use script `--help` for thresholds and fitting options when needed.
The validator preserves alpha in `rendered.png`. For transparent references it defaults to a white appearance background and alpha-based geometry (`--alpha-threshold`, default 0); for opaque references it estimates a background and uses RGB-distance masks. `--background` overrides the primary appearance background, and repeated `--comparison-background` values add MAE/SSIM records without changing the geometry comparison. Checkerboard inspection remains a separate visual check.
For reliable pixel sizing, supply `--reference` or a source-sized `viewBox`. Without either, standalone size inference uses numeric width/height magnitudes and does not convert physical or relative units into pixels.

## Validation and delivery
The native validator performs a structural preflight before rendering with CairoSVG or the portable `resvg_py` fallback. It reports alpha-aware foreground IoU, one-to-one component matches, boundary distances, composited RGB MAE/SSIM, and interior color error, plus JSON and diagnostic images. Check its reported violations and comparison settings; this is a reconstruction checker, not a general-purpose SVG sanitizer or proof that all geometry is sensible.
Preflight checks root dimensions/viewBox, forbidden content, external hrefs and CSS URL/import resources, and non-finite numeric attribute markers. Local fragment URLs and ordinary inline styles are supported; malformed CSS, XML base declarations, DTD/entities, and external stylesheet instructions are rejected. A successful exit indicates native preflight and rendering succeeded, not that fidelity met a threshold. SSIM is unavailable (`null`) for canvases smaller than three pixels on either axis.
- Judge silhouette with foreground/component IoU and boundary median/p95/max; inspect unmatched components and local residuals. Large blank backgrounds can inflate SSIM.
- Judge fills with eroded-interior RGB MAE and CIEDE2000. Keep alpha/opacity errors distinct from background-composited appearance and renderer-specific edge differences.
- Inspect background-sensitive artwork on light, dark, mid-gray, and checkerboard backgrounds. Inspect a practical small size and enlarged scale; use a second renderer when complex SVG features make portability material.
- Confirm source-sized canvas, intended closed paths, sensible finite geometry, no accidental empty/off-canvas objects, and visually justified gradients/filters/masks. Structural success alone cannot establish these visual properties.
- Generate requested transparent/white variants from identical artwork, adding only a white background rectangle. Validate final variants independently, including after packaging; report metrics from the final files.
Provide requested SVGs and a preview; include comparisons or an archive when requested. For native output, use a concise completion report:
```text
Canvas: <width> x <height>
Composition: <primitive counts, gradients, filters>
Native-vector checks: PASS/FAIL
Comparison: <background and alpha/mask basis>, MAE=<value>, SSIM=<value>, foreground IoU=<value>
Variants: <transparent, white, preview, archive>
Limit: <remaining source/renderer uncertainty; original nodes unavailable>
```
For explicitly authorized hybrid output, replace the native-check line with `Mode: hybrid; contains raster-backed <parts>; native-vector validation not applicable` and report the separate appearance/structural checks actually performed.
