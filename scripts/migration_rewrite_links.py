#!/usr/bin/env python3
"""Rewrite high-confidence parent Markdown references to the new grading repo."""

from __future__ import annotations

import argparse
from pathlib import Path

from migration_common import DEFAULT_TARGET, SUBTREE_NAME, read_csv, write_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rewrite high-confidence grading repo references.")
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--new-root", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--confidence", choices=["high"], default="high")
    parser.add_argument("--report", type=Path)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--dry-run", action="store_true")
    action.add_argument("--apply", action="store_true")
    return parser.parse_args()


def rewrite_text(text: str, new_root: Path) -> tuple[str, int]:
    replacements = 0
    new_lines: list[str] = []
    in_code_block = False
    for line in text.splitlines(keepends=True):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
        if in_code_block or SUBTREE_NAME not in line:
            new_lines.append(line)
            continue
        updated = line.replace(f"{SUBTREE_NAME}/docs/hw5-rubric.md", f"{new_root}/docs/hw5_rubric.md")
        updated = updated.replace(f"{SUBTREE_NAME}/docs/hw6-rubric.md", f"{new_root}/docs/hw6_rubric.md")
        updated = updated.replace(f"{SUBTREE_NAME}/docs/grading-policy.md", f"{new_root}/docs/grading_policy.md")
        updated = updated.replace(f"{SUBTREE_NAME}/", f"{new_root}/")
        updated = updated.replace(SUBTREE_NAME, str(new_root))
        if updated != line:
            replacements += 1
        new_lines.append(updated)
    return "".join(new_lines), replacements


def main() -> int:
    args = parse_args()
    parent = args.parent.resolve()
    rows = [
        row
        for row in read_csv(args.index)
        if row.get("confidence") == args.confidence and row.get("context") != "code_block"
    ]
    files = sorted({parent / row["source_markdown_file"] for row in rows})
    report_lines = [
        "# Link Rewrite Report",
        "",
        f"Parent repo: `{parent}`",
        f"New grading repo: `{args.new_root.resolve()}`",
        "",
        "| file | replacements | action |",
        "| --- | ---: | --- |",
    ]
    total_replacements = 0
    for path in files:
        original = path.read_text(encoding="utf-8")
        updated, replacements = rewrite_text(original, args.new_root.resolve())
        total_replacements += replacements
        action = "unchanged"
        if replacements:
            action = "rewritten" if args.apply else "would rewrite"
            if args.apply:
                path.write_text(updated, encoding="utf-8")
        print(f"{action}: {path} ({replacements} line replacements)")
        report_lines.append(f"| `{path.relative_to(parent).as_posix()}` | {replacements} | {action} |")

    report_lines.extend(
        [
            "",
            f"Total candidate rows from index: {len(rows)}",
            f"Total line replacements: {total_replacements}",
            "",
            "Code-block references were not rewritten.",
        ]
    )
    report = args.report or args.index.with_name("06_link_rewrite_report.md")
    write_text(report, "\n".join(report_lines) + "\n", args.apply)
    if not args.apply:
        print("Dry-run only. Re-run with --apply to rewrite parent Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

