#!/usr/bin/env python3
"""Copy raw submission files into stable working names.

Default mode is dry-run. Use --apply to copy files and update rename_map.csv.
Raw files are never deleted or modified.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rename homework submissions safely.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--dest-dir", type=Path)
    parser.add_argument("--map", dest="map_path", type=Path)
    parser.add_argument("--apply", action="store_true", help="Copy files and write the map.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing working copies.")
    return parser.parse_args()


def slugify(text: str, fallback: str = "submission") -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return (slug or fallback)[:80]


def suffixes(path: Path) -> str:
    lower = path.name.lower()
    if lower.endswith(".tar.gz"):
        return ".tar.gz"
    return path.suffix.lower()


def stem_without_suffix(path: Path) -> str:
    suffix = suffixes(path)
    return path.name[: -len(suffix)] if suffix and path.name.endswith(suffix) else path.stem


def infer_student_id(text: str) -> str:
    match = re.search(r"(?<!\d)(\d{8,10})(?!\d)", text)
    return match.group(1) if match else "unknown"


def iter_source_files(source_dir: Path) -> list[Path]:
    return sorted(path for path in source_dir.iterdir() if path.is_file() and not path.name.startswith("."))


def planned_name(homework: str, source: Path, index: int) -> tuple[str, str]:
    student_id = infer_student_id(source.name)
    short = slugify(stem_without_suffix(source))
    suffix = suffixes(source)
    if student_id == "unknown":
        return f"{homework}_unknown_{index:03d}_{short}{suffix}", "student id not inferred"
    return f"{homework}_{student_id}_{index:02d}_{short}{suffix}", "student id inferred from filename"


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir or ROOT / "submissions" / args.homework / "raw"
    dest_dir = args.dest_dir or ROOT / "submissions" / args.homework / "renamed"
    map_path = args.map_path or ROOT / "submissions" / args.homework / "rename_map.csv"

    if not source_dir.exists():
        print(f"Source directory does not exist: {source_dir}")
        return 1

    rows: list[dict[str, str]] = []
    copied = 0
    skipped = 0

    for index, source in enumerate(iter_source_files(source_dir), start=1):
        new_name, note = planned_name(args.homework, source, index)
        target = dest_dir / new_name
        status = "would copy"
        if target.exists() and not args.overwrite:
            status = "exists"
            skipped += 1
        elif args.apply:
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            status = "copied"
            copied += 1
        print(f"{status}: {source.name} -> {new_name}")
        rows.append({"original_filename": source.name, "new_filename": new_name, "notes": note})

    if args.apply:
        map_path.parent.mkdir(parents=True, exist_ok=True)
        with map_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, ["original_filename", "new_filename", "notes"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote map: {map_path}")
    else:
        print("Dry-run only. Re-run with --apply to copy files and write the map.")

    print(f"Summary: planned={len(rows)} copied={copied} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
