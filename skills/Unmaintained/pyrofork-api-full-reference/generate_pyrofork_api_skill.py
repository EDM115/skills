from __future__ import annotations

import ast
import datetime as dt
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = ROOT / "sources" / "pyrofork" / "pyrogram"
SKILL_ROOT = ROOT / "skills" / "pyrofork-api-full-reference"
REF_ROOT = SKILL_ROOT / "references"


def git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT / "sources" / "pyrofork"), "rev-parse", "HEAD"],
            text=True,
        ).strip()
    except Exception:
        return "unknown"


def esc_md(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("```", "\u0060\u0060\u0060")
    return text.strip()


def render_doc(text: str) -> str:
    cleaned = esc_md(text)
    if not cleaned:
        return "_No docstring._"
    return f"```text\n{cleaned}\n```"


def annotation_to_str(node: ast.AST | None) -> str:
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def function_signature(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    args = []

    def fmt_arg(a: ast.arg, default: ast.AST | None = None) -> str:
        out = a.arg
        ann = annotation_to_str(a.annotation)
        if ann:
            out += f": {ann}"
        if default is not None:
            try:
                out += f" = {ast.unparse(default)}"
            except Exception:
                out += " = ..."
        return out

    pos = fn.args.posonlyargs + fn.args.args
    defaults = [None] * (len(pos) - len(fn.args.defaults)) + list(fn.args.defaults)
    for a, d in zip(pos, defaults):
        args.append(fmt_arg(a, d))

    if fn.args.vararg:
        var = fn.args.vararg
        va = f"*{var.arg}"
        ann = annotation_to_str(var.annotation)
        if ann:
            va += f": {ann}"
        args.append(va)
    elif fn.args.kwonlyargs:
        args.append("*")

    for a, d in zip(fn.args.kwonlyargs, fn.args.kw_defaults):
        args.append(fmt_arg(a, d))

    if fn.args.kwarg:
        kw = fn.args.kwarg
        ka = f"**{kw.arg}"
        ann = annotation_to_str(kw.annotation)
        if ann:
            ka += f": {ann}"
        args.append(ka)

    ret = annotation_to_str(fn.returns)
    is_async = isinstance(fn, ast.AsyncFunctionDef)
    sig = f"{'async ' if is_async else ''}def {fn.name}({', '.join(args)})"
    if ret:
        sig += f" -> {ret}"
    return sig


def class_signature(cls: ast.ClassDef) -> str:
    bases = []
    for b in cls.bases:
        try:
            bases.append(ast.unparse(b))
        except Exception:
            pass
    if bases:
        return f"class {cls.name}({', '.join(bases)})"
    return f"class {cls.name}"


def stable_slug(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return s or "root"


def bucket_for(rel_path: Path) -> str:
    parts = rel_path.parts
    return parts[0] if len(parts) > 1 else "root"


def parse_file(path: Path) -> dict:
    src = path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"module_doc": "", "classes": [], "functions": [], "parse_error": True}

    module_doc = ast.get_docstring(tree) or ""
    classes = []
    functions = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            cdoc = ast.get_docstring(node) or ""
            methods = []
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    methods.append(
                        {
                            "name": item.name,
                            "signature": function_signature(item),
                            "doc": ast.get_docstring(item) or "",
                        }
                    )
            classes.append(
                {
                    "name": node.name,
                    "signature": class_signature(node),
                    "doc": cdoc,
                    "methods": methods,
                }
            )
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(
                {
                    "name": node.name,
                    "signature": function_signature(node),
                    "doc": ast.get_docstring(node) or "",
                }
            )

    return {
        "module_doc": module_doc,
        "classes": classes,
        "functions": functions,
        "parse_error": False,
    }


def write_reference(bucket: str, files: list[Path]) -> str:
    slug = stable_slug(f"api-{bucket}")
    out = REF_ROOT / f"api-{slug}.md"

    lines: list[str] = []
    lines.append("---")
    lines.append(f"name: api-{slug}")
    lines.append(
        "description: Offline API backup extracted from Pyrofork source docstrings."
    )
    lines.append("---")
    lines.append("")
    lines.append(f"# Pyrofork API Backup: `{bucket}`")
    lines.append("")
    lines.append(
        "Extracted from `sources/pyrofork/pyrogram/**.py` using AST parsing of module, class, function, and method docstrings."
    )
    lines.append("")

    for f in sorted(files):
        rel = f.relative_to(SRC_ROOT)
        data = parse_file(f)
        lines.append(f"## File: `{rel.as_posix()}`")
        lines.append("")

        if data["parse_error"]:
            lines.append("_Parse error: unable to parse this file._")
            lines.append("")
            continue

        md = esc_md(data["module_doc"])
        if md:
            lines.append("### Module Docstring")
            lines.append("")
            lines.append(render_doc(md))
            lines.append("")

        if data["functions"]:
            lines.append("### Top-level Functions")
            lines.append("")
            for fn in data["functions"]:
                lines.append(f"#### `{fn['signature']}`")
                lines.append("")
                lines.append(render_doc(fn["doc"]))
                lines.append("")

        if data["classes"]:
            lines.append("### Classes")
            lines.append("")
            for cls in data["classes"]:
                lines.append(f"#### `{cls['signature']}`")
                lines.append("")
                lines.append(render_doc(cls["doc"]))
                lines.append("")
                if cls["methods"]:
                    lines.append("##### Methods")
                    lines.append("")
                    for m in cls["methods"]:
                        lines.append(f"###### `{m['signature']}`")
                        lines.append("")
                        lines.append(render_doc(m["doc"]))
                        lines.append("")
                    lines.append("")

        lines.append("---")
        lines.append("")

    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out.name


def write_skill_index(
    files_by_bucket: dict[str, list[Path]], refs: list[tuple[str, str]]
) -> None:
    today = dt.date.today().isoformat()
    sha = git_sha()

    skill_lines = [
        "---",
        "name: pyrofork-api-full-reference",
        "description: Offline API backup skill for Pyrofork, extracted from source docstrings across pyrogram modules. Warning - the content is massive and should be queried with tools like `rg`/`grep` for specific references rather than read sequentially. Only load sections relevant to your needs.",
        "metadata:",
        "  author: EDM115",
        f'  version: "{today.replace("-", ".")}"',
        '  source: "Generated from https://github.com/Mayuri-Chan/pyrofork source docstrings, using https://github.com/antfu/skills"',
        "---",
        "",
        f"> The skill is based on Pyrofork source SHA `{sha}`, generated at {today}.",
        "",
        "This skill is an offline API backup generated from docstrings in `sources/pyrofork/pyrogram/**.py`.",
        "",
        "## API References",
        "",
        "| Module Bucket | Files | Reference |",
        "|---|---:|---|",
    ]

    for bucket, ref_file in sorted(refs, key=lambda x: x[0]):
        count = len(files_by_bucket[bucket])
        stem = Path(ref_file).stem
        skill_lines.append(
            f"| `{bucket}` | {count} | [{stem}](references/{ref_file}) |"
        )

    skill_lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Content is generated from source docstrings, including module/class/function/method-level docs.",
            "- This is intended for offline reference and agent consumption rather than polished user docs.",
        ]
    )

    (SKILL_ROOT / "SKILL.md").write_text(
        "\n".join(skill_lines).rstrip() + "\n", encoding="utf-8"
    )

    gen_lines = [
        "# Generation Info",
        "",
        "- **Source:** `sources/pyrofork/pyrogram`",
        f"- **Git SHA:** `{sha}`",
        f"- **Generated:** {today}",
        "- **Method:** AST docstring extraction from Python source files, `python ./generate_pyrofork_api_skill.py`",
    ]
    (SKILL_ROOT / "GENERATION.md").write_text(
        "\n".join(gen_lines).rstrip() + "\n", encoding="utf-8"
    )


def main() -> None:
    if not SRC_ROOT.exists():
        raise SystemExit(f"Source not found: {SRC_ROOT}")

    SKILL_ROOT.mkdir(parents=True, exist_ok=True)
    REF_ROOT.mkdir(parents=True, exist_ok=True)

    files = [p for p in SRC_ROOT.rglob("*.py") if p.is_file()]
    buckets: dict[str, list[Path]] = defaultdict(list)
    for f in files:
        rel = f.relative_to(SRC_ROOT)
        buckets[bucket_for(rel)].append(f)

    refs: list[tuple[str, str]] = []
    for bucket, bfiles in sorted(buckets.items(), key=lambda x: x[0]):
        ref_name = write_reference(bucket, bfiles)
        refs.append((bucket, ref_name))

    write_skill_index(buckets, refs)
    print(
        f"Generated pyrofork-api-full-reference skill with {len(files)} source files across {len(buckets)} buckets."
    )


if __name__ == "__main__":
    main()
