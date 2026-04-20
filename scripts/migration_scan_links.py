#!/usr/bin/env python3
"""Scan parent Markdown files for references to the grading subtree.

Default mode prints a summary only. Use --write to create the CSV and Markdown
scan report. The scanner does not rewrite files.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from migration_common import DEFAULT_TARGET, SUBTREE_NAME, md_table, suggested_target_path, write_csv, write_text


FIELDS = [
    "source_markdown_file",
    "line",
    "context",
    "reference_type",
    "referenced_text",
    "referenced_path",
    "resolved_target_path",
    "exists_now",
    "migration_action_needed",
    "suggested_new_path",
    "confidence",
]


MARKDOWN_LINK = re.compile(r"(?P<full>\[[^\]]+\]\((?P<path>[^)]+)\))")
WIKI_LINK = re.compile(r"(?P<full>\[\[(?P<path>[^\]]+)\]\])")
RAW_PATH = re.compile(r"(?P<path>ns-practice-ta-grading-2026s(?:/[^\s`),;]*)?)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan Markdown references to the grading subtree.")
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--subtree", default=SUBTREE_NAME)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--write", action="store_true", help="Write CSV and Markdown report.")
    return parser.parse_args()


def iter_markdown(parent: Path, subtree: str) -> list[Path]:
    skip_names = {".git", subtree}
    files: list[Path] = []
    for path in sorted(parent.rglob("*.md")):
        if any(part in skip_names for part in path.parts):
            continue
        if any(part.startswith(f"{subtree}.migrated-backup-") for part in path.parts):
            continue
        files.append(path)
    return files


def resolve_reference(parent: Path, source: Path, referenced_path: str) -> tuple[str, str]:
    clean = referenced_path.strip().strip("`")
    if clean.startswith("http://") or clean.startswith("https://"):
        return clean, "false"
    if clean.startswith("/"):
        resolved = Path(clean)
    elif clean.startswith(SUBTREE_NAME):
        resolved = parent / clean
    else:
        resolved = source.parent / clean
    return str(resolved), "true" if resolved.exists() else "false"


def row_for(
    parent: Path,
    source: Path,
    line_no: int,
    context: str,
    ref_type: str,
    referenced_text: str,
    referenced_path: str,
    target: Path,
) -> dict[str, str]:
    resolved, exists_now = resolve_reference(parent, source, referenced_path)
    suggested = suggested_target_path(referenced_path, target)
    if context == "code_block":
        action = "report_only_code_block"
        confidence = "medium"
    elif suggested:
        action = "rewrite_or_stub"
        confidence = "high" if exists_now == "true" else "medium"
    else:
        action = "manual_review"
        confidence = "low"
    return {
        "source_markdown_file": source.relative_to(parent).as_posix(),
        "line": str(line_no),
        "context": context,
        "reference_type": ref_type,
        "referenced_text": referenced_text,
        "referenced_path": referenced_path,
        "resolved_target_path": resolved,
        "exists_now": exists_now,
        "migration_action_needed": action,
        "suggested_new_path": suggested,
        "confidence": confidence,
    }


def scan(parent: Path, subtree: str, target: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source in iter_markdown(parent, subtree):
        in_code_block = False
        for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), start=1):
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
            if subtree not in line:
                continue
            context = "code_block" if in_code_block else "prose"
            seen_spans: set[tuple[int, int]] = set()
            for regex, ref_type in [(MARKDOWN_LINK, "markdown_link"), (WIKI_LINK, "wiki_link")]:
                for match in regex.finditer(line):
                    if subtree not in match.group("path"):
                        continue
                    seen_spans.add(match.span())
                    rows.append(
                        row_for(
                            parent,
                            source,
                            line_no,
                            context,
                            ref_type,
                            match.group("full"),
                            match.group("path"),
                            target,
                        )
                    )
            for match in RAW_PATH.finditer(line):
                if any(start <= match.start() and match.end() <= end for start, end in seen_spans):
                    continue
                rows.append(
                    row_for(
                        parent,
                        source,
                        line_no,
                        context,
                        "raw_path_mention",
                        match.group("path"),
                        match.group("path"),
                        target,
                    )
                )
    return rows


def report_text(rows: list[dict[str, str]], parent: Path, target: Path) -> str:
    by_file: dict[str, int] = {}
    for row in rows:
        by_file[row["source_markdown_file"]] = by_file.get(row["source_markdown_file"], 0) + 1
    table_rows = [[path, str(count)] for path, count in sorted(by_file.items())]
    sample_rows = [
        [
            row["source_markdown_file"],
            row["line"],
            row["reference_type"],
            row["confidence"],
            row["referenced_path"],
            row["suggested_new_path"],
        ]
        for row in rows[:25]
    ]
    return f"""# Markdown Reference Scan

Generated for parent repo: `{parent}`

Target standalone repo: `{target}`

## Summary

- References found: {len(rows)}
- Source Markdown files with references: {len(by_file)}
- Action: report first; rewrite only high-confidence references after review.

## References By Source File

{md_table(["source_markdown_file", "references"], table_rows) if table_rows else "- none"}

## Sample Reference Rows

{md_table(["source", "line", "type", "confidence", "old", "suggested"], sample_rows) if sample_rows else "- none"}

## Notes

- `code_block` references are reported but not rewritten automatically.
- Missing legacy filenames such as `hw5-rubric.md` are mapped to underscore
  canonical filenames when a known equivalent exists.
- The machine-readable index is `markdown_reference_index.csv`.
"""


def main() -> int:
    args = parse_args()
    rows = scan(args.parent.resolve(), args.subtree, args.target.resolve())
    report = args.report or args.output.with_name("02_markdown_reference_scan.md")
    write_csv(args.output, rows, FIELDS, args.write)
    write_text(report, report_text(rows, args.parent.resolve(), args.target.resolve()), args.write)
    print(f"References found: {len(rows)}")
    print(f"CSV: {args.output}")
    print(f"Report: {report}")
    if not args.write:
        print("Dry-run only. Re-run with --write to write reports.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
