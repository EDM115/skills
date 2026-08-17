# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy>=1.26",
#   "opencv-python-headless>=4.9",
#   "pillow>=10",
# ]
# ///

"""Measure a mostly flat raster logo without automatically tracing it."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw

HEX_COLOR = re.compile(r"^#?([0-9a-fA-F]{6})$")


def parse_color(value: str) -> np.ndarray:
    match = HEX_COLOR.fullmatch(value.strip())
    if not match:
        raise argparse.ArgumentTypeError(f"Expected #RRGGBB, received {value!r}")
    raw = match.group(1)
    return np.asarray([int(raw[index : index + 2], 16) for index in (0, 2, 4)], dtype=np.float32)


def color_hex(color: np.ndarray) -> str:
    values = np.clip(np.rint(color), 0, 255).astype(np.uint8)
    return "#" + "".join(f"{int(channel):02X}" for channel in values)


def safe_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def estimate_background(rgb: np.ndarray, corner_size: int) -> np.ndarray:
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


def alpha_and_residual(rgb: np.ndarray, background: np.ndarray, fill: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    direction = fill - background
    denominator = float(np.dot(direction, direction))
    if denominator < 1e-6:
        raise ValueError(f"Fill {color_hex(fill)} is indistinguishable from background {color_hex(background)}")
    alpha = np.sum((rgb - background) * direction, axis=2) / denominator
    alpha = np.clip(alpha, 0.0, 1.0)
    reconstructed = background + alpha[..., None] * direction
    residual = np.linalg.norm(rgb - reconstructed, axis=2)
    return alpha, residual


def dominant_colors(rgb: np.ndarray, foreground: np.ndarray, limit: int = 12) -> list[dict[str, int | str]]:
    pixels = np.clip(np.rint(rgb[foreground]), 0, 255).astype(np.uint8)
    if pixels.size == 0:
        return []
    quantized = ((pixels.astype(np.uint16) + 4) // 8 * 8).clip(0, 255).astype(np.uint8)
    counts = Counter(map(tuple, quantized.tolist()))
    return [
        {"color": color_hex(np.asarray(color)), "pixels": int(count)}
        for color, count in counts.most_common(limit)
    ]


def contour_inventory(mask_u8: np.ndarray, min_area: float) -> list[dict[str, object]]:
    contours, hierarchy = cv2.findContours(mask_u8, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    parent_by_index: list[int] = []
    if hierarchy is not None:
        parent_by_index = [int(row[3]) for row in hierarchy[0]]
    records: list[dict[str, object]] = []
    for index, contour in enumerate(contours):
        area = float(cv2.contourArea(contour))
        if area < min_area:
            continue
        x, y, width, height = cv2.boundingRect(contour)
        (center_x, center_y), (rect_width, rect_height), angle = cv2.minAreaRect(contour)
        records.append(
            {
                "source_index": index,
                "parent_source_index": parent_by_index[index] if parent_by_index else -1,
                "area": round(area, 3),
                "perimeter": round(float(cv2.arcLength(contour, True)), 3),
                "bounding_box": {"x": x, "y": y, "width": width, "height": height},
                "rotated_rect": {
                    "center": [round(center_x, 3), round(center_y, 3)],
                    "size": [round(rect_width, 3), round(rect_height, 3)],
                    "angle_degrees": round(float(angle), 3),
                },
                "point_count": len(contour),
            }
        )
    records.sort(key=lambda item: float(item["area"]), reverse=True)
    return records


def component_inventory(mask_u8: np.ndarray, min_area: int) -> list[dict[str, object]]:
    count, _, stats, centroids = cv2.connectedComponentsWithStats(mask_u8, connectivity=8)
    components: list[dict[str, object]] = []
    for label in range(1, count):
        x, y, width, height, area = map(int, stats[label])
        if area < min_area:
            continue
        center_x, center_y = centroids[label]
        components.append(
            {
                "label": label,
                "area": area,
                "bounding_box": {"x": x, "y": y, "width": width, "height": height},
                "centroid": [round(float(center_x), 3), round(float(center_y), 3)],
            }
        )
    components.sort(key=lambda item: int(item["area"]), reverse=True)
    return components


def write_component_overlay(image: Image.Image, components: list[dict[str, object]], output: Path) -> None:
    overlay = image.copy().convert("RGB")
    draw = ImageDraw.Draw(overlay)
    for display_index, component in enumerate(components, start=1):
        box = component["bounding_box"]
        x = int(box["x"])
        y = int(box["y"])
        width = int(box["width"])
        height = int(box["height"])
        draw.rectangle((x, y, x + width - 1, y + height - 1), outline=(255, 0, 0), width=2)
        draw.text((x + 3, y + 3), str(display_index), fill=(255, 0, 0), stroke_width=2, stroke_fill=(255, 255, 255))
    overlay.save(output)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Raster image to inspect")
    parser.add_argument("--out-dir", type=Path, required=True, help="Directory for JSON and diagnostic images")
    parser.add_argument("--background", type=parse_color, help="Override estimated background as #RRGGBB")
    parser.add_argument("--corner-size", type=int, default=15, help="Corner patch size for background estimation")
    parser.add_argument("--threshold", type=float, default=12.0, help="RGB distance from background for foreground")
    parser.add_argument("--fill", action="append", type=parse_color, default=[], help="Known solid fill; repeat as needed")
    parser.add_argument("--residual-threshold", type=float, default=10.0, help="Maximum RGB reconstruction residual for known fills")
    parser.add_argument("--min-alpha", type=float, default=0.03, help="Minimum reconstructed coverage for a known fill")
    parser.add_argument("--min-component-area", type=int, default=16, help="Ignore smaller connected components and contours")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.input.is_file():
        raise SystemExit(f"Input does not exist or is not a file: {args.input}")
    if args.corner_size < 1 or args.threshold < 0 or args.residual_threshold < 0 or not 0 <= args.min_alpha <= 1:
        raise SystemExit("Corner size and thresholds must be non-negative; --min-alpha must be between 0 and 1")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    image = Image.open(args.input).convert("RGB")
    rgb = np.asarray(image, dtype=np.float32)
    background = args.background if args.background is not None else estimate_background(rgb, args.corner_size)
    distance = np.linalg.norm(rgb - background, axis=2)
    foreground = distance > args.threshold
    mask_u8 = foreground.astype(np.uint8) * 255

    mask_path = args.out_dir / "foreground-mask.png"
    Image.fromarray(mask_u8).save(mask_path)
    components = component_inventory(mask_u8, args.min_component_area)
    overlay_path = args.out_dir / "components.png"
    write_component_overlay(image, components, overlay_path)

    report: dict[str, object] = {
        "input": str(args.input.resolve()),
        "width": image.width,
        "height": image.height,
        "estimated_background": color_hex(background),
        "foreground_threshold": args.threshold,
        "foreground_pixels": int(np.count_nonzero(foreground)),
        "foreground_fraction": round(float(np.mean(foreground)), 8),
        "dominant_quantized_foreground_colors": dominant_colors(rgb, foreground),
        "components": components,
        "contours": contour_inventory(mask_u8, float(args.min_component_area)),
        "known_fill_masks": [],
        "diagnostics": {
            "foreground_mask": str(mask_path.resolve()),
            "component_overlay": str(overlay_path.resolve()),
        },
    }

    if args.fill:
        alpha_stack: list[np.ndarray] = []
        residual_stack: list[np.ndarray] = []
        for fill in args.fill:
            alpha, residual = alpha_and_residual(rgb, background, fill)
            alpha_stack.append(alpha)
            residual_stack.append(residual)
        alphas = np.stack(alpha_stack, axis=2)
        residuals = np.stack(residual_stack, axis=2)
        best_fill = np.argmin(residuals, axis=2)
        known_fill_records: list[dict[str, object]] = []
        for index, fill in enumerate(args.fill):
            selected = (
                (best_fill == index)
                & (alphas[:, :, index] >= args.min_alpha)
                & (residuals[:, :, index] <= args.residual_threshold)
            )
            fill_hex = color_hex(fill)
            fill_path = args.out_dir / f"fill-{index + 1}-{safe_slug(fill_hex)}.png"
            Image.fromarray(selected.astype(np.uint8) * 255).save(fill_path)
            known_fill_records.append(
                {
                    "fill": fill_hex,
                    "pixels": int(np.count_nonzero(selected)),
                    "mask": str(fill_path.resolve()),
                    "components": component_inventory(selected.astype(np.uint8) * 255, args.min_component_area),
                }
            )
        report["known_fill_masks"] = known_fill_records

    report_path = args.out_dir / "analysis.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"analysis": str(report_path.resolve()), "width": image.width, "height": image.height, "background": color_hex(background)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
