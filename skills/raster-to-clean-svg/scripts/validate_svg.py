# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "cairosvg>=2.7",
#   "numpy>=1.26",
#   "opencv-python-headless>=4.9",
#   "pillow>=10",
#   "resvg_py>=0.3,<1.0",
#   "scikit-image>=0.22",
# ]
# ///

"""Validate native SVG content and optionally compare it with a raster reference."""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from skimage.color import deltaE_ciede2000, rgb2lab
from skimage.metrics import structural_similarity

HEX_COLOR = re.compile(r"^#?([0-9a-fA-F]{6})$")
FORBIDDEN_ELEMENTS = {"image", "foreignObject", "script"}
XLINK_HREF = "{http://www.w3.org/1999/xlink}href"
NON_FINITE_NUMBER = re.compile(r"(?<![A-Za-z])(?:nan|[+-]?inf(?:inity)?)(?![A-Za-z])", re.IGNORECASE)


def parse_color(value: str) -> np.ndarray:
    match = HEX_COLOR.fullmatch(value.strip())
    if not match:
        raise argparse.ArgumentTypeError(f"Expected #RRGGBB, received {value!r}")
    raw = match.group(1)
    return np.asarray([int(raw[index : index + 2], 16) for index in (0, 2, 4)], dtype=np.float32)


def color_hex(color: np.ndarray) -> str:
    values = np.clip(np.rint(color), 0, 255).astype(np.uint8)
    return "#" + "".join(f"{int(channel):02X}" for channel in values)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def estimate_background(rgb: np.ndarray, corner_size: int = 15) -> np.ndarray:
    height, width = rgb.shape[:2]
    patch = max(1, min(corner_size, height // 2 or 1, width // 2 or 1))
    corners = np.concatenate(
        [
            rgb[:patch, :patch].reshape(-1, 3),
            rgb[:patch, -patch:].reshape(-1, 3),
            rgb[-patch:, :patch].reshape(-1, 3),
            rgb[-patch:, -patch:].reshape(-1, 3),
        ]
    )
    return np.median(corners, axis=0)


def href_is_external(value: str) -> bool:
    stripped = value.strip()
    return bool(stripped) and not stripped.startswith("#")


def validate_native_svg(svg_path: Path) -> tuple[ET.ElementTree, dict[str, object]]:
    text = svg_path.read_text(encoding="utf-8")
    tree = ET.parse(svg_path)
    root = tree.getroot()
    if local_name(root.tag) != "svg":
        raise ValueError(f"Root element must be <svg>, received <{local_name(root.tag)}>")

    element_counts: Counter[str] = Counter()
    forbidden: list[str] = []
    external_references: list[str] = []
    non_finite_attributes: list[dict[str, str]] = []
    for element in root.iter():
        name = local_name(element.tag)
        element_counts[name] += 1
        if name in FORBIDDEN_ELEMENTS:
            forbidden.append(name)
        for attribute_name, attribute_value in element.attrib.items():
            if (local_name(attribute_name) == "href" or attribute_name == XLINK_HREF) and href_is_external(attribute_value):
                external_references.append(attribute_value)
            if NON_FINITE_NUMBER.search(attribute_value):
                non_finite_attributes.append(
                    {"element": name, "attribute": local_name(attribute_name), "value": attribute_value}
                )

    lower_text = text.lower()
    text_violations = [needle for needle in ("data:image/", "base64,") if needle in lower_text]
    violations = []
    if forbidden:
        violations.append(f"forbidden elements: {sorted(set(forbidden))}")
    if external_references:
        violations.append(f"external href values: {sorted(set(external_references))}")
    if text_violations:
        violations.append(f"embedded raster markers: {text_violations}")
    if non_finite_attributes:
        violations.append(f"non-finite numeric attributes: {non_finite_attributes}")

    return tree, {
        "xml_valid": True,
        "native_vector_pass": not violations,
        "violations": violations,
        "non_finite_attributes": non_finite_attributes,
        "element_counts": dict(sorted(element_counts.items())),
        "viewBox": root.attrib.get("viewBox"),
        "width_attribute": root.attrib.get("width"),
        "height_attribute": root.attrib.get("height"),
    }


def infer_svg_size(root: ET.Element, fallback: tuple[int, int] = (1000, 1000)) -> tuple[int, int]:
    view_box = root.attrib.get("viewBox", "").replace(",", " ").split()
    if len(view_box) == 4:
        try:
            return max(1, round(float(view_box[2]))), max(1, round(float(view_box[3])))
        except ValueError:
            pass

    def numeric_dimension(value: str | None) -> int | None:
        if not value:
            return None
        match = re.match(r"^\s*([0-9]+(?:\.[0-9]+)?)", value)
        return max(1, round(float(match.group(1)))) if match else None

    width = numeric_dimension(root.attrib.get("width"))
    height = numeric_dimension(root.attrib.get("height"))
    return width or fallback[0], height or fallback[1]


def save_side_by_side(original: np.ndarray, rendered: np.ndarray, path: Path) -> None:
    divider = np.full((original.shape[0], 8, 3), 224, dtype=np.uint8)
    Image.fromarray(np.concatenate([original, divider, rendered], axis=1)).save(path)


def mask_boundary(mask: np.ndarray) -> np.ndarray:
    kernel = np.ones((3, 3), dtype=np.uint8)
    eroded = cv2.erode(mask.astype(np.uint8), kernel).astype(bool)
    return mask & ~eroded


def symmetric_boundary_stats(target: np.ndarray, candidate: np.ndarray) -> dict[str, float | None]:
    target_boundary = mask_boundary(target)
    candidate_boundary = mask_boundary(candidate)
    if not np.any(target_boundary) or not np.any(candidate_boundary):
        return {"median": None, "p95": None, "max": None}
    distance_to_candidate = cv2.distanceTransform(
        (~candidate_boundary).astype(np.uint8), cv2.DIST_L2, cv2.DIST_MASK_PRECISE
    )
    distance_to_target = cv2.distanceTransform(
        (~target_boundary).astype(np.uint8), cv2.DIST_L2, cv2.DIST_MASK_PRECISE
    )
    distances = np.concatenate([distance_to_candidate[target_boundary], distance_to_target[candidate_boundary]])
    return {
        "median": round(float(np.median(distances)), 8),
        "p95": round(float(np.percentile(distances, 95)), 8),
        "max": round(float(np.max(distances)), 8),
    }


def mean_ciede2000(reference: np.ndarray, candidate: np.ndarray, mask: np.ndarray) -> float | None:
    if not np.any(mask):
        return None
    reference_samples = reference[mask].astype(np.float32).reshape(-1, 1, 3) / 255.0
    candidate_samples = candidate[mask].astype(np.float32).reshape(-1, 1, 3) / 255.0
    reference_lab = rgb2lab(reference_samples).reshape(-1, 3)
    candidate_lab = rgb2lab(candidate_samples).reshape(-1, 3)
    return round(float(np.mean(deltaE_ciede2000(reference_lab, candidate_lab))), 8)


def save_directional_mask_difference(target: np.ndarray, candidate: np.ndarray, path: Path) -> None:
    diagnostic = np.zeros((*target.shape, 3), dtype=np.uint8)
    diagnostic[target & ~candidate] = (255, 0, 0)
    diagnostic[candidate & ~target] = (0, 120, 255)
    Image.fromarray(diagnostic).save(path)


def matched_component_ious(target: np.ndarray, candidate: np.ndarray, min_area: int) -> list[dict[str, object]]:
    target_count, target_labels, target_stats, _ = cv2.connectedComponentsWithStats(target.astype(np.uint8), connectivity=8)
    candidate_count, candidate_labels, candidate_stats, _ = cv2.connectedComponentsWithStats(candidate.astype(np.uint8), connectivity=8)
    candidate_masks = {
        label: candidate_labels == label
        for label in range(1, candidate_count)
        if int(candidate_stats[label, cv2.CC_STAT_AREA]) >= min_area
    }
    records: list[dict[str, object]] = []
    for target_label in range(1, target_count):
        area = int(target_stats[target_label, cv2.CC_STAT_AREA])
        if area < min_area:
            continue
        target_mask = target_labels == target_label
        best_label: int | None = None
        best_iou = 0.0
        for candidate_label, candidate_mask in candidate_masks.items():
            intersection = int(np.count_nonzero(target_mask & candidate_mask))
            union = int(np.count_nonzero(target_mask | candidate_mask))
            iou = float(intersection / union) if union else 1.0
            if iou > best_iou:
                best_iou = iou
                best_label = candidate_label
        x, y, width, height, _ = map(int, target_stats[target_label])
        records.append(
            {
                "target_label": target_label,
                "target_area": area,
                "target_bounding_box": {"x": x, "y": y, "width": width, "height": height},
                "best_rendered_label": best_label,
                "iou": round(best_iou, 8),
            }
        )
    records.sort(key=lambda item: int(item["target_area"]), reverse=True)
    return records


def render_svg(svg_path: Path, output_path: Path, width: int, height: int, background: np.ndarray) -> str:
    cairo_error: Exception | None = None
    try:
        import cairosvg

        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(output_path),
            output_width=width,
            output_height=height,
            background_color=color_hex(background),
        )
        return "CairoSVG"
    except (ImportError, OSError) as error:
        cairo_error = error

    try:
        import resvg_py

        png_bytes = resvg_py.svg_to_bytes(
            svg_path=str(svg_path),
            width=width,
            height=height,
            background=color_hex(background),
        )
        output_path.write_bytes(png_bytes)
        return "resvg_py"
    except (ImportError, OSError, RuntimeError, ValueError) as resvg_error:
        raise RuntimeError(
            f"No SVG renderer succeeded. CairoSVG: {cairo_error!r}; resvg_py: {resvg_error!r}"
        ) from resvg_error


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path, help="Candidate SVG")
    parser.add_argument("--reference", type=Path, help="Optional raster reference")
    parser.add_argument("--out-dir", type=Path, required=True, help="Directory for the report and diagnostics")
    parser.add_argument("--background", type=parse_color, help="Comparison and render background as #RRGGBB")
    parser.add_argument("--threshold", type=float, default=12.0, help="RGB distance from background for foreground masks")
    parser.add_argument("--corner-size", type=int, default=15, help="Corner patch size for reference background estimation")
    parser.add_argument("--difference-gain", type=float, default=5.0, help="Gain for the amplified RGB difference image")
    parser.add_argument("--interior-kernel", type=int, default=9, help="Square erosion kernel for interior-only color MAE")
    parser.add_argument("--min-component-area", type=int, default=16, help="Minimum target/rendered component area for matched IoU")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.svg.is_file():
        raise SystemExit(f"SVG does not exist or is not a file: {args.svg}")
    if args.reference is not None and not args.reference.is_file():
        raise SystemExit(f"Reference does not exist or is not a file: {args.reference}")
    if args.threshold < 0 or args.corner_size < 1 or args.difference_gain < 0:
        raise SystemExit("Threshold and difference gain must be non-negative; corner size must be positive")
    if args.interior_kernel < 1 or args.min_component_area < 1:
        raise SystemExit("Interior kernel and minimum component area must be positive")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    tree, native_report = validate_native_svg(args.svg)
    root = tree.getroot()

    reference_rgb: np.ndarray | None = None
    if args.reference is not None:
        reference_image = Image.open(args.reference).convert("RGB")
        reference_rgb = np.asarray(reference_image, dtype=np.uint8)
        width, height = reference_image.size
        background = args.background if args.background is not None else estimate_background(reference_rgb.astype(np.float32), args.corner_size)
    else:
        width, height = infer_svg_size(root)
        background = args.background if args.background is not None else np.asarray([255, 255, 255], dtype=np.float32)

    report: dict[str, object] = {
        "svg": str(args.svg.resolve()),
        "reference": str(args.reference.resolve()) if args.reference is not None else None,
        "render_width": width,
        "render_height": height,
        "renderer": None,
        "comparison_background": color_hex(background),
        **native_report,
        "diagnostics": {},
    }

    report_path = args.out_dir / "validation.json"
    if not bool(native_report["native_vector_pass"]):
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2))
        return 2

    rendered_path = args.out_dir / "rendered.png"
    renderer = render_svg(args.svg, rendered_path, width, height, background)
    rendered_rgb = np.asarray(Image.open(rendered_path).convert("RGB"), dtype=np.uint8)
    report["renderer"] = renderer
    diagnostics = report["diagnostics"]
    assert isinstance(diagnostics, dict)
    diagnostics["rendered"] = str(rendered_path.resolve())

    if reference_rgb is not None:
        reference_float = reference_rgb.astype(np.float32)
        rendered_float = rendered_rgb.astype(np.float32)
        absolute_difference = np.abs(reference_float - rendered_float)
        mae = float(np.mean(absolute_difference))
        ssim = float(structural_similarity(reference_rgb, rendered_rgb, channel_axis=2, data_range=255))
        original_mask = np.linalg.norm(reference_float - background, axis=2) > args.threshold
        rendered_mask = np.linalg.norm(rendered_float - background, axis=2) > args.threshold
        intersection = int(np.count_nonzero(original_mask & rendered_mask))
        union = int(np.count_nonzero(original_mask | rendered_mask))
        iou = float(intersection / union) if union else 1.0
        component_ious = matched_component_ious(original_mask, rendered_mask, args.min_component_area)
        boundary_stats = symmetric_boundary_stats(original_mask, rendered_mask)

        kernel = np.ones((args.interior_kernel, args.interior_kernel), dtype=np.uint8)
        eroded_target = cv2.erode(original_mask.astype(np.uint8), kernel).astype(bool)
        interior = eroded_target & rendered_mask
        interior_pixels = int(np.count_nonzero(interior))
        if interior_pixels:
            interior_error_rgb = np.mean(absolute_difference[interior], axis=0)
            interior_color_mae_rgb: list[float] | None = [round(float(value), 8) for value in interior_error_rgb]
            interior_color_mae_mean: float | None = round(float(np.mean(interior_error_rgb)), 8)
            interior_color_delta_e_2000_mean = mean_ciede2000(reference_rgb, rendered_rgb, interior)
        else:
            interior_color_mae_rgb = None
            interior_color_mae_mean = None
            interior_color_delta_e_2000_mean = None

        side_by_side_path = args.out_dir / "side-by-side.png"
        difference_path = args.out_dir / "difference-amplified.png"
        xor_path = args.out_dir / "foreground-xor.png"
        save_side_by_side(reference_rgb, rendered_rgb, side_by_side_path)
        Image.fromarray(np.clip(absolute_difference * args.difference_gain, 0, 255).astype(np.uint8)).save(difference_path)
        save_directional_mask_difference(original_mask, rendered_mask, xor_path)

        report["metrics"] = {
            "mae_0_to_255": round(mae, 8),
            "ssim": round(ssim, 8),
            "foreground_iou": round(iou, 8),
            "foreground_intersection_pixels": intersection,
            "foreground_union_pixels": union,
            "mask_threshold": args.threshold,
            "matched_component_ious": component_ious,
            "symmetric_boundary_distance_px": boundary_stats,
            "interior_color_mae_rgb": interior_color_mae_rgb,
            "interior_color_mae_mean": interior_color_mae_mean,
            "interior_color_delta_e_2000_mean": interior_color_delta_e_2000_mean,
            "interior_pixels": interior_pixels,
            "interior_kernel": args.interior_kernel,
        }
        diagnostics = report["diagnostics"]
        assert isinstance(diagnostics, dict)
        diagnostics.update(
            {
                "side_by_side": str(side_by_side_path.resolve()),
                "difference_amplified": str(difference_path.resolve()),
                "foreground_xor": str(xor_path.resolve()),
                "foreground_xor_legend": {"reference_only": "red", "rendered_only": "blue"},
            }
        )

    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if bool(native_report["native_vector_pass"]) else 2


if __name__ == "__main__":
    raise SystemExit(main())
