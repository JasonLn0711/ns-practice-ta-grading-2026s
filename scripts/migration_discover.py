#!/usr/bin/env python3
"""Inventory the grading repo and create migration planning reports."""

from __future__ import annotations

import argparse
from pathlib import Path

from migration_common import (
    DEFAULT_TARGET,
    category_for,
    iter_files,
    md_table,
    planned_action_for,
    read_csv,
    rel,
    sensitivity_for,
    sha256_short,
    write_csv,
    write_text,
)


MAPPING_FIELDS = [
    "old_path",
    "new_path",
    "relative_path",
    "category",
    "sensitivity",
    "action_taken",
    "old_path_still_exists",
    "stub_created",
    "links_rewritten",
    "linked_by_parent_markdown",
    "notes",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create migration inventory and path mapping.")
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--reports-dir", type=Path, default=Path("migration_reports"))
    parser.add_argument("--reference-index", type=Path)
    parser.add_argument("--write", action="store_true", help="Write inventory and mapping reports.")
    return parser.parse_args()


def linked_paths(index_path: Path | None) -> set[str]:
    linked: set[str] = set()
    if not index_path or not index_path.exists():
        return linked
    for row in read_csv(index_path):
        old = row.get("referenced_path", "")
        if old.startswith("ns-practice-ta-grading-2026s/"):
            linked.add(old.removeprefix("ns-practice-ta-grading-2026s/"))
        elif old == "ns-practice-ta-grading-2026s":
            linked.add("")
    return linked


def build_rows(source: Path, target: Path, linked: set[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in iter_files(source, include_git=False):
        relative = rel(path, source)
        if relative in linked:
            linked_status = "yes"
        elif "" in linked:
            linked_status = "root_reference_only"
        else:
            linked_status = "no"
        rows.append(
            {
                "old_path": str(path),
                "new_path": str(target / relative),
                "relative_path": relative,
                "category": category_for(relative),
                "sensitivity": sensitivity_for(relative),
                "action_taken": planned_action_for(relative),
                "old_path_still_exists": "yes",
                "stub_created": "planned_if_referenced_markdown",
                "links_rewritten": "planned_high_confidence_only",
                "linked_by_parent_markdown": linked_status,
                "notes": f"sha256={sha256_short(path)}",
            }
        )
    return rows


def inventory_report(rows: list[dict[str, str]], source: Path, target: Path) -> str:
    by_category: dict[str, int] = {}
    by_sensitivity: dict[str, int] = {}
    exact_linked = 0
    root_reference_only = 0
    for row in rows:
        by_category[row["category"]] = by_category.get(row["category"], 0) + 1
        by_sensitivity[row["sensitivity"]] = by_sensitivity.get(row["sensitivity"], 0) + 1
        if row["linked_by_parent_markdown"] == "yes":
            exact_linked += 1
        elif row["linked_by_parent_markdown"] == "root_reference_only":
            root_reference_only += 1

    sensitive_samples = [
        [row["relative_path"], row["category"], row["sensitivity"], row["action_taken"]]
        for row in rows
        if row["sensitivity"] != "public_safe_within_private_repo"
    ][:40]
    return f"""# Migration Inventory

Source grading repo: `{source}`

Candidate destination: `{target}`

## Summary

- Files inventoried, excluding `.git`: {len(rows)}
- Files explicitly linked by parent Markdown scan: {exact_linked}
- Files covered only by root-level subtree references: {root_reference_only}
- Migration posture: copy first, verify, then create compatibility stubs.

## File Categories

{md_table(["category", "count"], [[key, str(value)] for key, value in sorted(by_category.items())])}

## Sensitivity Classes

{md_table(["sensitivity", "count"], [[key, str(value)] for key, value in sorted(by_sensitivity.items())])}

## Sensitive Or Private Samples

{md_table(["relative_path", "category", "sensitivity", "planned_action"], sensitive_samples) if sensitive_samples else "- none"}

## Public-Safe Within Private Repo

Docs, scripts, templates, reports, and repository indexes are suitable for
versioning inside the private standalone grading repo. They are not intended to
be public course materials.

## Audit Rule

Every copied file is recorded in `path_mapping.csv` with old path, new path,
sensitivity, planned action, and a short SHA-256 digest.
"""


def mapping_markdown(rows: list[dict[str, str]]) -> str:
    table_rows = [
        [
            row["relative_path"],
            row["category"],
            row["sensitivity"],
            row["action_taken"],
            row["linked_by_parent_markdown"],
        ]
        for row in rows[:120]
    ]
    extra = "" if len(rows) <= 120 else f"\n\nOnly first 120 of {len(rows)} rows shown; see CSV for full mapping."
    return f"""# Path Mapping

Machine-readable source of truth: `path_mapping.csv`.

{md_table(["relative_path", "category", "sensitivity", "action", "linked"], table_rows)}
{extra}
"""


def target_design_report(source: Path, target: Path) -> str:
    return f"""# Target Repo Design

Source: `{source}`

Target: `{target}`

## Design Choice

The migration keeps the existing grading repo structure. It does not add root
`scores/`, `feedback/`, or `review_notes/` folders because `grading/hw5/` and
`grading/hw6/` already separate scores, feedback, review notes, evidence, and
deduction logs by homework.

## Canonical Areas

- `docs/`: grading policy, evidence levels, rubrics, assignment requirements.
- `grading/hw5/` and `grading/hw6/`: versioned scores, evidence, deduction logs,
  and per-student notes.
- `submissions/<hw>/`: raw, renamed, and extracted student submissions; bulky
  files remain ignored while mapping CSVs are versioned.
- `course_materials/<hw>/`: assignment/reference metadata is versioned; bulky
  raw/renamed course files remain ignored.
- `scripts/`: safe helpers for grading and migration.
- `migration_reports/`: migration inventory, mapping, link scan, and verification
  records.

## Privacy Boundary

The standalone repo is private. Audit metadata is versioned for traceability;
raw submissions and bulky course binaries stay out of Git to reduce exposure
risk.
"""


def migration_plan_report(source: Path, target: Path) -> str:
    return f"""# Migration Plan

## Strategy

1. Copy `{source}` to `{target}` including `.git` and ignored local files.
2. Verify file counts, SHA-256 digests, Git history, and ignored-file policy.
3. Rename the old nested directory to a timestamped local backup.
4. Create small compatibility stubs at the old path.
5. Rewrite only high-confidence parent Markdown references.
6. Commit standalone repo changes and parent compatibility changes separately.

## File Classification

- Move/copy directly: docs, scripts, templates, reports, README files.
- Copy first, verify later: raw submissions, renamed binaries, extracted
  archives, bulky course materials.
- Leave stub or redirect note: old root README and common rubric paths.
- Leave in place for now: timestamped backup until Jason confirms cleanup.
- Ignore/exclude from version control: raw, renamed, extracted, caches, bulky
  course binary folders.
- Manual review required: ambiguous prose mentions and code-block path mentions.

## Non-Destructive Rule

The scripts never delete the source by default. The old repo is renamed only
after the sibling copy passes verification.
"""


def link_strategy_report(target: Path) -> str:
    return f"""# Link Preservation Strategy

Canonical standalone repo: `{target}`

## Stub Strategy

Create a small `README.md` at the old nested path and short stubs for legacy
rubric filenames. The stubs explain that the canonical grading workspace moved,
include the migration date, and point to the new sibling repo.

## Rewrite Strategy

Rewrite only high-confidence references in parent Markdown files. The current
scan found references in the project note and the 2026-04-20 daily note. Code
block references and ambiguous text are reported, not changed.

## Compatibility Rule

The parent planning repo remains usable even if an older note still points to
`ns-practice-ta-grading-2026s/`: the old path contains a redirect note, not
private grading data.
"""


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    reports_dir = args.reports_dir if args.reports_dir.is_absolute() else source / args.reports_dir
    linked = linked_paths(args.reference_index)
    rows = build_rows(source, target, linked)

    write_csv(reports_dir / "path_mapping.csv", rows, MAPPING_FIELDS, args.write)
    write_text(reports_dir / "path_mapping.md", mapping_markdown(rows), args.write)
    write_text(reports_dir / "01_inventory.md", inventory_report(rows, source, target), args.write)
    write_text(reports_dir / "03_target_repo_design.md", target_design_report(source, target), args.write)
    write_text(reports_dir / "04_migration_plan.md", migration_plan_report(source, target), args.write)
    write_text(reports_dir / "05_link_preservation_strategy.md", link_strategy_report(target), args.write)

    print(f"Inventoried files: {len(rows)}")
    print(f"Reports dir: {reports_dir}")
    if not args.write:
        print("Dry-run only. Re-run with --write to create reports.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
