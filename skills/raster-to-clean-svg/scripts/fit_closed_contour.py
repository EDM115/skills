# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy>=1.26",
#   "opencv-python-headless>=4.9",
#   "pillow>=10",
#   "scikit-image>=0.22",
#   "scipy>=1.11",
# ]
# ///

"""Fit one smooth binary component as periodic cubic Béziers and export a candidate SVG."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from scipy.interpolate import BSpline, splprep
from scipy.ndimage import gaussian_filter
from skimage.measure import find_contours


def largest_component(mask: np.ndarray) -> np.ndarray:
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), connectivity=8)
    if count <= 1:
        raise ValueError("Mask contains no foreground component")
    component_index = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    return labels == component_index


def cleaned_contour(mask: np.ndarray, sigma: float, level: float) -> tuple[np.ndarray, np.ndarray]:
    component = largest_component(mask)
    smoothed = gaussian_filter(component.astype(float), sigma=sigma)
    contours = sorted(find_contours(smoothed, level=level), key=len, reverse=True)
    if not contours:
        raise ValueError(f"No contour found at level {level}; adjust --threshold, --sigma, or --level")
    points_yx = contours[0]
    points_xy = np.column_stack([points_yx[:, 1], points_yx[:, 0]])
    return component, points_xy


def fit_periodic_spline(points: np.ndarray, smoothing: float) -> tuple[np.ndarray, np.ndarray, int]:
    if len(points) < 4:
        raise ValueError("At least four contour points are required for a cubic periodic spline")
    tck, _ = splprep([points[:, 0], points[:, 1]], s=smoothing, per=True, k=3)
    knots, coefficients, degree = tck
    return np.asarray(knots), np.asarray(coefficients), int(degree)


def bspline_to_cubic_segments(tck: tuple[np.ndarray, np.ndarray, int]) -> list[tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]:
    knots, coefficients, degree = tck
    if degree != 3:
        raise ValueError("Expected a cubic B-spline")
    coefficients_xy = np.asarray(coefficients).T
    curve = BSpline(knots, coefficients_xy, degree)
    derivative = curve.derivative()
    valid_end = len(coefficients_xy)
    breaks = np.unique(knots[degree : valid_end + 1])
    segments: list[tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = []
    for u0, u1 in itertools.pairwise(breaks):
        if u1 <= u0:
            continue
        delta = float(u1 - u0)
        p0 = np.asarray(curve(u0), dtype=float)
        p3 = np.asarray(curve(u1), dtype=float)
        p1 = p0 + np.asarray(derivative(u0), dtype=float) * delta / 3.0
        p2 = p3 - np.asarray(derivative(u1), dtype=float) * delta / 3.0
        segments.append((p0, p1, p2, p3))
    if not segments:
        raise ValueError("The fitted spline produced no non-zero knot intervals")
    return segments


def format_number(value: float, precision: int) -> str:
    text = f"{value:.{precision}f}"
    return text.rstrip("0").rstrip(".") if "." in text else text


def svg_path_data(segments: list[tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]], precision: int) -> str:
    start = segments[0][0]
    commands = [f"M {format_number(start[0], precision)} {format_number(start[1], precision)}"]
    for _, p1, p2, p3 in segments:
        commands.append(
            "C "
            f"{format_number(p1[0], precision)} {format_number(p1[1], precision)} "
            f"{format_number(p2[0], precision)} {format_number(p2[1], precision)} "
            f"{format_number(p3[0], precision)} {format_number(p3[1], precision)}"
        )
    commands.append("Z")
    return "\n    ".join(commands)


def sampled_spline_mask(tck: tuple[np.ndarray, np.ndarray, int], shape: tuple[int, int], sample_count: int) -> np.ndarray:
    knots, coefficients, degree = tck
    coefficients_xy = np.asarray(coefficients).T
    curve = BSpline(knots, coefficients_xy, degree)
    start = float(knots[degree])
    end = float(knots[len(coefficients_xy)])
    parameters = np.linspace(start, end, num=sample_count, endpoint=False)
    points = np.rint(curve(parameters)).astype(np.int32)
    candidate = np.zeros(shape, dtype=np.uint8)
    cv2.fillPoly(candidate, [points[:, None, :]], color=1)
    return candidate.astype(bool)


def intersection_over_union(target: np.ndarray, candidate: np.ndarray) -> float:
    intersection = int(np.count_nonzero(target & candidate))
    union = int(np.count_nonzero(target | candidate))
    return float(intersection / union) if union else 1.0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mask", type=Path, help="Binary or grayscale component mask")
    parser.add_argument("--out-svg", type=Path, required=True, help="Candidate SVG to write")
    parser.add_argument("--report", type=Path, help="Optional JSON report path")
    parser.add_argument("--threshold", type=int, default=127, help="Foreground threshold from 0 to 255")
    parser.add_argument("--invert", action="store_true", help="Treat values below the threshold as foreground")
    parser.add_argument("--sigma", type=float, default=0.8, help="Gaussian mask smoothing")
    parser.add_argument("--level", type=float, default=0.5, help="Subpixel contour level after smoothing")
    parser.add_argument("--smoothing", type=float, default=10.0, help="SciPy splprep smoothing value")
    parser.add_argument("--fill", default="#000000", help="SVG fill color or paint value")
    parser.add_argument("--precision", type=int, default=3, help="Decimal places in path coordinates")
    parser.add_argument("--samples", type=int, default=4096, help="Spline samples for approximate mask IoU")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.mask.is_file():
        raise SystemExit(f"Mask does not exist or is not a file: {args.mask}")
    if not 0 <= args.threshold <= 255:
        raise SystemExit("--threshold must be between 0 and 255")
    if args.sigma < 0 or not 0 < args.level < 1 or args.smoothing < 0:
        raise SystemExit("--sigma and --smoothing must be non-negative; --level must be between 0 and 1")
    if args.precision < 0 or args.samples < 32:
        raise SystemExit("--precision must be non-negative and --samples must be at least 32")

    image = Image.open(args.mask).convert("L")
    values = np.asarray(image, dtype=np.uint8)
    mask = values < args.threshold if args.invert else values > args.threshold
    component, points = cleaned_contour(mask, args.sigma, args.level)
    tck = fit_periodic_spline(points, args.smoothing)
    segments = bspline_to_cubic_segments(tck)
    path_data = svg_path_data(segments, args.precision)

    args.out_svg.parent.mkdir(parents=True, exist_ok=True)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {image.width} {image.height}" '
        f'width="{image.width}" height="{image.height}">\n'
        f'  <path fill="{args.fill}" d="\n    {path_data}\n  "/>\n'
        "</svg>\n"
    )
    args.out_svg.write_text(svg, encoding="utf-8")

    candidate_mask = sampled_spline_mask(tck, component.shape, args.samples)
    report = {
        "mask": str(args.mask.resolve()),
        "out_svg": str(args.out_svg.resolve()),
        "width": image.width,
        "height": image.height,
        "foreground_pixels": int(np.count_nonzero(component)),
        "raw_contour_points": len(points),
        "cubic_segments": len(segments),
        "sigma": args.sigma,
        "level": args.level,
        "smoothing": args.smoothing,
        "approximate_sampled_mask_iou": round(intersection_over_union(component, candidate_mask), 8),
    }
    if args.report is not None:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
