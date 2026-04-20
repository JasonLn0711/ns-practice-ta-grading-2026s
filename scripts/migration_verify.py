#!/usr/bin/env python3
"""Verify the sibling grading repo migration."""

from __future__ import annotations

import argparse
import csv
import subprocess
from pathlib import Path

from migration_common import DEFAULT_TARGET, read_csv, write_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify copied grading repo and parent compatibility.")
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--old-root", type=Path)
    parser.add_argument("--write", action="store_true", help="Write verification report.")
    parser.add_argument("--update-mapping", action="store_true", help="Update path mapping with final status.")
    return parser.parse_args()


def run_git(repo: Path, *args: str) -> tuple[int, str]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return result.returncode, result.stdout.strip()


def check_mapping(rows: list[dict[str, str]]) -> tuple[int, int, list[str]]:
    checked = 0
    missing = 0
    samples: list[str] = []
    for row in rows:
        new_path = Path(row["new_path"])
        checked += 1
        if not new_path.exists():
            missing += 1
            if len(samples) < 20:
                samples.append(row["relative_path"])
    return checked, missing, samples


def raw_tracking_violations(target: Path) -> list[str]:
    code, output = run_git(target, "ls-files")
    if code != 0:
        return [f"git ls-files failed: {output}"]
    violations: list[str] = []
    for line in output.splitlines():
        if line.endswith(".gitkeep"):
            continue
        parts = line.split("/")
        if len(parts) >= 3 and parts[0] in {"submissions", "course_materials"}:
            if parts[2] in {"raw", "renamed", "extracted"}:
                violations.append(line)
    return violations


def update_mapping(rows: list[dict[str, str]], old_root: Path, target: Path, mapping: Path) -> None:
    stubbed = {
        "README.md": "",
        "docs/hw5-rubric.md": "docs/hw5_rubric.md",
        "docs/hw6-rubric.md": "docs/hw6_rubric.md",
        "docs/hw5_rubric.md": "docs/hw5_rubric.md",
        "docs/hw6_rubric.md": "docs/hw6_rubric.md",
        "docs/grading_policy.md": "docs/grading_policy.md",
    }
    fieldnames = list(rows[0].keys()) if rows else []
    seen_relatives = {row["relative_path"] for row in rows}
    for row in rows:
        relative = row["relative_path"]
        old_path = old_root / relative
        new_path = Path(row["new_path"])
        row["old_path_still_exists"] = "yes" if old_path.exists() else "no"
        row["stub_created"] = "yes" if relative in stubbed and old_path.exists() else "no"
        row["links_rewritten"] = "yes_high_confidence_parent_links" if row["linked_by_parent_markdown"] != "no" else "not_applicable"
        if not new_path.exists():
            row["action_taken"] = "missing_destination_needs_review"
        elif row["category"] == "migration_compatibility_stub":
            row["action_taken"] = "compatibility_stub_created"
        elif "raw_or_bulky" in row["category"]:
            row["action_taken"] = "copied_to_sibling_keep_ignored"
        elif "private_audit" in row["category"]:
            row["action_taken"] = "copied_to_private_repo_versioned"
        else:
            row["action_taken"] = "copied_to_sibling"
        if row["stub_created"] == "yes":
            base_note = row["notes"].replace("; compatibility_stub_at_old_path", "")
            row["notes"] = f"{base_note}; compatibility_stub_at_old_path"
    for relative, canonical_relative in stubbed.items():
        if relative in seen_relatives:
            continue
        old_path = old_root / relative
        new_path = target / canonical_relative if canonical_relative else target
        rows.append(
            {
                "old_path": str(old_path),
                "new_path": str(new_path),
                "relative_path": relative,
                "category": "migration_compatibility_stub",
                "sensitivity": "public_safe_within_private_repo",
                "action_taken": "compatibility_stub_created",
                "old_path_still_exists": "yes" if old_path.exists() else "no",
                "stub_created": "yes" if old_path.exists() else "no",
                "links_rewritten": "yes_high_confidence_parent_links",
                "linked_by_parent_markdown": "yes",
                "notes": "legacy compatibility path; canonical content lives in sibling repo",
            }
        )
    with mapping.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_mapping_md(rows: list[dict[str, str]], mapping_md: Path) -> None:
    lines = [
        "# Path Mapping",
        "",
        "Machine-readable source of truth: `path_mapping.csv`.",
        "",
        "| relative_path | action_taken | old_path_still_exists | stub_created | links_rewritten |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows[:160]:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["relative_path"],
                    row["action_taken"],
                    row["old_path_still_exists"],
                    row["stub_created"],
                    row["links_rewritten"],
                ]
            )
            + " |"
        )
    if len(rows) > 160:
        lines.append("")
        lines.append(f"Only first 160 of {len(rows)} rows shown; see CSV for full mapping.")
    mapping_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def report_text(
    parent: Path,
    target: Path,
    mapping_path: Path,
    old_root: Path | None,
    checked: int,
    missing: int,
    missing_samples: list[str],
    git_status: str,
    git_head: str,
    violations: list[str],
) -> str:
    old_readme = old_root / "README.md" if old_root else parent / "ns-practice-ta-grading-2026s" / "README.md"
    return f"""# Verification Report

Parent repo: `{parent}`

Standalone grading repo: `{target}`

Mapping file: `{mapping_path}`

## Copy Verification

- Mapped files checked: {checked}
- Missing mapped destination files: {missing}
- Missing samples: {", ".join(missing_samples) if missing_samples else "none"}

## Git Verification

- Target HEAD before writing this report: `{git_head or "unknown"}`
- Target tracked status before writing this report: `{git_status or "clean"}`
- Raw/bulky tracking violations: {len(violations)}

## Compatibility Stub Verification

- Old README stub exists: {"yes" if old_readme.exists() else "no"}
- Old README stub path: `{old_readme}`

## Privacy Verification

Tracked files under `submissions/*/(raw|renamed|extracted)` and
`course_materials/*/(raw|renamed|extracted)` should be limited to `.gitkeep`.

Violations:

{chr(10).join(f"- `{item}`" for item in violations) if violations else "- none"}

## Result

{"PASS" if missing == 0 and not violations and target.exists() else "NEEDS REVIEW"}
"""


def main() -> int:
    args = parse_args()
    parent = args.parent.resolve()
    target = args.target.resolve()
    rows = read_csv(args.mapping)
    old_root = args.old_root.resolve() if args.old_root else parent / "ns-practice-ta-grading-2026s"
    if args.update_mapping:
        update_mapping(rows, old_root, target, args.mapping)
        update_mapping_md(rows, args.mapping.with_suffix(".md"))
    checked, missing, missing_samples = check_mapping(rows)
    _, status = run_git(target, "status", "--short") if target.exists() else (1, "target missing")
    _, head = run_git(target, "rev-parse", "--short", "HEAD") if target.exists() else (1, "")
    violations = raw_tracking_violations(target) if target.exists() else ["target missing"]

    report = report_text(
        parent=parent,
        target=target,
        mapping_path=args.mapping.resolve(),
        old_root=old_root,
        checked=checked,
        missing=missing,
        missing_samples=missing_samples,
        git_status=status,
        git_head=head,
        violations=violations,
    )
    write_text(args.output, report, args.write)
    print(report)
    if not args.write:
        print("Dry-run only. Re-run with --write to save the report.")
    return 0 if missing == 0 and not violations and target.exists() else 1


if __name__ == "__main__":
    raise SystemExit(main())
