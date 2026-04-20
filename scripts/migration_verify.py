#!/usr/bin/env python3
"""Verify the sibling grading repo migration."""

from __future__ import annotations

import argparse
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

- Target HEAD: `{git_head or "unknown"}`
- Target tracked status: `{git_status or "clean"}`
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
    checked, missing, missing_samples = check_mapping(rows)
    _, status = run_git(target, "status", "--short") if target.exists() else (1, "target missing")
    _, head = run_git(target, "rev-parse", "--short", "HEAD") if target.exists() else (1, "")
    violations = raw_tracking_violations(target) if target.exists() else ["target missing"]

    report = report_text(
        parent=parent,
        target=target,
        mapping_path=args.mapping.resolve(),
        old_root=args.old_root.resolve() if args.old_root else None,
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

