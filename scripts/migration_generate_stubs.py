#!/usr/bin/env python3
"""Generate compatibility stubs at the old nested grading path."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create moved-note stubs at the old grading path.")
    parser.add_argument("--old-root", type=Path, required=True)
    parser.add_argument("--new-root", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, help="Path mapping CSV for audit reference.")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--dry-run", action="store_true")
    action.add_argument("--apply", action="store_true")
    return parser.parse_args()


def stub_text(title: str, new_path: Path) -> str:
    return f"""# {title}

This file is a compatibility stub.

The canonical TA grading workspace moved to:

`{new_path}`

Migration date: {datetime.now().strftime("%Y-%m-%d")}

Use the standalone private grading repo for rubrics, scores, student notes,
deduction logs, reports, scripts, and submission mappings. This old path remains
only to preserve older planning links.
"""


def planned_stubs(old_root: Path, new_root: Path) -> list[tuple[Path, str]]:
    return [
        (old_root / "README.md", stub_text("TA Grading Workspace Moved", new_root)),
        (
            old_root / "docs" / "hw5-rubric.md",
            stub_text("HW5 Rubric Moved", new_root / "docs" / "hw5_rubric.md"),
        ),
        (
            old_root / "docs" / "hw6-rubric.md",
            stub_text("HW6 Rubric Moved", new_root / "docs" / "hw6_rubric.md"),
        ),
        (
            old_root / "docs" / "hw5_rubric.md",
            stub_text("HW5 Rubric Moved", new_root / "docs" / "hw5_rubric.md"),
        ),
        (
            old_root / "docs" / "hw6_rubric.md",
            stub_text("HW6 Rubric Moved", new_root / "docs" / "hw6_rubric.md"),
        ),
        (
            old_root / "docs" / "grading_policy.md",
            stub_text("Grading Policy Moved", new_root / "docs" / "grading_policy.md"),
        ),
    ]


def main() -> int:
    args = parse_args()
    old_root = args.old_root.resolve()
    new_root = args.new_root.resolve()

    if old_root.exists() and any(old_root.iterdir()):
        existing = sorted(path.name for path in old_root.iterdir())
        allowed = {"README.md", "docs"}
        if any(name not in allowed for name in existing):
            print(f"Refusing to write stubs into non-empty old root: {old_root}")
            print("Move the original repo to a timestamped backup first.")
            return 1

    for path, text in planned_stubs(old_root, new_root):
        print(f"{'write' if args.apply else 'would write'}: {path}")
        if args.apply:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    if args.mapping:
        print(f"Mapping reference: {args.mapping}")
    if not args.apply:
        print("Dry-run only. Re-run with --apply after the original repo is backed up.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

