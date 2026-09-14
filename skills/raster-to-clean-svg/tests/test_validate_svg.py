"""Focused regressions; run using the validator's declared dependencies."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import numpy as np
from PIL import Image

spec = importlib.util.spec_from_file_location('validator', Path(__file__).parents[1] / 'scripts' / 'validate_svg.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class ValidatorTests(unittest.TestCase):
    def test_one_to_one_merge_and_extra(self):
        target = np.zeros((12, 12), bool)
        target[1:3, 1:3] = True
        target[1:3, 5:7] = True
        candidate = target.copy()
        candidate[1, 3:5] = True
        candidate[8:10, 8:10] = True
        records = v.matched_component_ious(target, candidate, 1)
        self.assertEqual(sum(r['match_status'] == 'matched' for r in records), 1)
        self.assertEqual(sum(r['match_status'] == 'unmatched_target' for r in records), 1)
        self.assertEqual(sum(r['match_status'] == 'unmatched_rendered' for r in records), 1)

    def test_empty_assignments_and_exponent_size(self):
        empty = np.zeros((3, 3), bool)
        filled = np.ones((3, 3), bool)
        self.assertEqual(v.matched_component_ious(empty, empty, 1), [])
        self.assertEqual(v.matched_component_ious(empty, filled, 1)[0]['match_status'], 'unmatched_rendered')
        self.assertEqual(v.matched_component_ious(filled, empty, 1)[0]['match_status'], 'unmatched_target')
        self.assertEqual(v.infer_svg_size(v.ET.fromstring('<svg width="1e2px" height=".5e2px"/>')), (100, 50))

    def test_resvg_fallback_preserves_alpha(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            svg = root / 'input.svg'
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="8" height="8"><rect x="2" y="2" width="4" height="4" fill="black"/></svg>')
            with patch.dict('sys.modules', {'cairosvg': None}):
                self.assertEqual(v.render_svg(svg, root / 'rendered.png', 8, 8), 'resvg_py')
            rgba = Image.open(root / 'rendered.png').convert('RGBA')
            self.assertEqual(rgba.getpixel((0, 0))[3], 0)
            self.assertEqual(rgba.getpixel((3, 3)), (0, 0, 0, 255))

    def test_tiny_opaque_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            svg = root / 'input.svg'
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="2" height="2"><rect width="1" height="1" fill="black"/></svg>')
            reference = np.full((2, 2, 3), 255, dtype=np.uint8)
            reference[0, 0] = 0
            image = root / 'reference.png'
            Image.fromarray(reference).save(image)
            with patch('sys.argv', ['validate', str(svg), '--reference', str(image), '--out-dir', directory, '--background', '#FFFFFF', '--min-component-area', '1']), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(v.main(), 0)
            metrics = json.loads((root / 'validation.json').read_text())['metrics']
            self.assertEqual(metrics['foreground_mask_basis'], 'background_rgb_distance')
            self.assertEqual(metrics['foreground_iou'], 1)
            self.assertEqual(metrics['mae_0_to_255'], 0)
            self.assertIsNone(metrics['ssim'])
            self.assertIsNone(metrics['alpha_mae_0_to_255'])
            self.assertIsNone(metrics['appearance_by_background'][0]['ssim'])

    def test_hidden_rgb_is_ignored(self):
        rgba = np.array([[[250, 20, 10, 0], [0, 0, 0, 128]]], dtype=np.uint8)
        self.assertEqual(v.composite_rgba(rgba, np.array([255]*3)).tolist(), [[[255]*3, [127]*3]])

    def test_preflight(self):
        invalid = [
            '<svg viewBox="0 0 -1 10"/>', '<svg viewBox="0 0 1e999 10"/>',
            '<svg width="0"/>', '<svg height="NaN"/>', '<svg width="10garbage"/>',
            '<svg><style>@import "https://example.com/a.css";</style></svg>',
            '<svg><path fill="url(https://example.com/x)"/></svg>',
            '<svg><path style="fill:url(https://example.com/a)"/></svg>',
            '<svg xmlns:xml="http://www.w3.org/XML/1998/namespace" xml:base="https://example.com/"/>',
        ]
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'input.svg'
            for xml in invalid:
                with self.subTest(xml=xml):
                    p.write_text(xml)
                    self.assertFalse(v.validate_native_svg(p)[1]['native_vector_pass'])
                    with patch.object(v, 'render_svg') as render, patch('sys.argv', ['validate', str(p), '--out-dir', directory]), contextlib.redirect_stdout(io.StringIO()):
                        self.assertEqual(v.main(), 2)
                        render.assert_not_called()
            p.write_text('<svg viewBox="-1 -1 10 10" width="1e2px"><path fill="url(#local)"/></svg>')
            self.assertTrue(v.validate_native_svg(p)[1]['native_vector_pass'])
            p.write_text('<svg><style>.a {fill: url("#local")}</style><path style="fill:red; stroke:url(#local)"/></svg>')
            self.assertTrue(v.validate_native_svg(p)[1]['native_vector_pass'])
        self.assertTrue(v.css_resource_violations(r'fill:u\72l(https://example.com/a)'))
        self.assertTrue(v.css_resource_violations(r'@im\70ort "https://example.com/a.css";'))

    def test_real_render_transparency_and_opacity_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            svg = root / 'input.svg'
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"><rect x="4" y="4" width="8" height="8" fill="black"/></svg>')
            reference = np.zeros((16, 16, 4), dtype=np.uint8)
            reference[:, :, :3] = [123, 42, 231]
            reference[4:12, 4:12] = [0, 0, 0, 255]
            image = root / 'reference.png'
            Image.fromarray(reference).save(image)
            argv = ['validate', str(svg), '--reference', str(image), '--out-dir', directory, '--min-component-area', '1', '--comparison-background', '#000000', '--comparison-background', '#808080']
            with patch('sys.argv', argv), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(v.main(), 0)
            report = json.loads((root / 'validation.json').read_text())
            self.assertEqual(report['metrics']['foreground_iou'], 1)
            self.assertEqual(report['metrics']['mae_0_to_255'], 0)
            self.assertEqual(report['metrics']['alpha_mae_0_to_255'], 0)
            self.assertEqual(Image.open(root / 'rendered.png').convert('RGBA').getpixel((0, 0))[3], 0)
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"><rect width="16" height="16" fill="white"/><rect x="4" y="4" width="8" height="8" fill="black"/></svg>')
            with patch('sys.argv', argv), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(v.main(), 0)
            report = json.loads((root / 'validation.json').read_text())
            self.assertEqual(report['metrics']['mae_0_to_255'], 0)
            self.assertLess(report['metrics']['foreground_iou'], 1)
            self.assertGreater(report['metrics']['alpha_mae_0_to_255'], 0)
            appearances = report['metrics']['appearance_by_background']
            self.assertEqual([item['background'] for item in appearances], ['#FFFFFF', '#000000', '#808080'])
            self.assertEqual(appearances[0]['mae_0_to_255'], 0)
            self.assertGreater(appearances[1]['mae_0_to_255'], appearances[2]['mae_0_to_255'])
            self.assertGreater(appearances[2]['mae_0_to_255'], 0)

if __name__ == '__main__':
    unittest.main()
