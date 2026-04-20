#!/usr/bin/env python3
"""Copy the grading repo to its standalone sibling location.

The default mode is dry-run. The script never deletes the source. `--mode move`
is intentionally a logged rename-only operation and still refuses to overwrite
an existing target.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy or rename the grading repo safely.")
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--mode", choices=["copy", "move"], default="copy")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--dry-run", action="store_true", help="Show planned action.")
    action.add_argument("--apply", action="store_true", help="Perform the action.")
    return parser.parse_args()


def count_files(root: Path) -> int:
    return sum(1 for path in root.rglob("*") if path.is_file())


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    target = args.target.resolve()

    if not source.exists():
        print(f"Source does not exist: {source}")
        return 1
    if target.exists():
        print(f"Refusing to overwrite existing target: {target}")
        return 1

    planned_files = count_files(source)
    print(f"Mode: {args.mode}")
    print(f"Source: {source}")
    print(f"Target: {target}")
    print(f"Files planned, including .git and ignored local files: {planned_files}")

    if not args.apply:
        print("Dry-run only. Re-run with --apply after reviewing the target path.")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    if args.mode == "copy":
        shutil.copytree(source, target, symlinks=True)
    else:
        shutil.move(str(source), str(target))
    print(f"Completed {args.mode}: {source} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

