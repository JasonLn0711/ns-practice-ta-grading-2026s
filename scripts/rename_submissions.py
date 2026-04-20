#!/usr/bin/env python3
"""Copy raw homework files into stable renamed filenames.

Default mode is dry-run. Use --apply to actually copy files and write the map.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

COURSE_FILE_NAMES = {
    "hw5": {
        "Homework 5 .pdf": "hw5_course_assignment-spec.pdf",
        "05_Training of Multi-Layer Neural Network.pdf": (
            "hw5_course_lecture05-training-multi-layer-neural-network.pdf"
        ),
        "Lecture 5_Multi_layer neural network_Backprop.rar": (
            "hw5_course_lecture05-backprop-materials.rar"
        ),
        "data.rar": "hw5_course_shared-data-archive.rar",
    },
    "hw6": {
        "Homework 6 .pdf": "hw6_course_assignment-spec.pdf",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rename homework files by copying them.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], default="hw5")
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--dest-dir", type=Path)
    parser.add_argument("--apply", action="store_true", help="Copy files and write rename_map.csv.")
    return parser.parse_args()


def stable_suffix(path: Path) -> str:
    suffix = "".join(path.suffixes)
    return suffix.lower() if suffix else ""


def base_without_suffix(path: Path) -> str:
    suffix = "".join(path.suffixes)
    if suffix and path.name.endswith(suffix):
        return path.name[: -len(suffix)]
    return path.stem


def slugify(text: str, fallback: str = "file") -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return (text or fallback)[:70]


def infer_student_id(name: str) -> str | None:
    match = re.search(r"(?<!\d)(\d{6,10})(?!\d)", name)
    return match.group(1) if match else None


def plan_name(homework: str, path: Path, index: int) -> tuple[str, str]:
    course_name = COURSE_FILE_NAMES.get(homework, {}).get(path.name)
    if course_name:
        return course_name, "course/reference material"

    suffix = stable_suffix(path)
    original_base = base_without_suffix(path)
    original_slug = slugify(original_base)
    student_id = infer_student_id(path.name)

    if student_id:
        name_part = path.name.replace(student_id, " ")
        name_slug = slugify(base_without_suffix(Path(name_part)), fallback="unknown-name")
        return (
            f"{homework}_{student_id}_{name_slug}_{original_slug}{suffix}",
            "student id inferred from filename",
        )

    return (
        f"{homework}_unknown_{index:03d}_{original_slug}{suffix}",
        "student identity not inferred from filename",
    )


def iter_files(path: Path) -> list[Path]:
    return sorted(
        p
        for p in path.iterdir()
        if p.is_file() and p.name != "rename_map.csv" and not p.name.startswith(".")
    )


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir or ROOT / "submissions" / args.homework / "raw"
    dest_dir = args.dest_dir or ROOT / "submissions" / args.homework / "renamed"
    map_path = ROOT / "submissions" / args.homework / "rename_map.csv"

    if not source_dir.exists():
        print(f"Source directory does not exist: {source_dir}")
        return 1

    dest_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []

    for index, source in enumerate(iter_files(source_dir), start=1):
        new_name, note = plan_name(args.homework, source, index)
        target = dest_dir / new_name
        rows.append(
            {
                "original_filename": source.name,
                "new_filename": new_name,
                "notes": note,
            }
        )
        action = "copy" if args.apply else "would copy"
        status = "exists" if target.exists() else "new"
        print(f"{action}: {source.name} -> {target.name} [{status}]")

        if args.apply and not target.exists():
            shutil.copy2(source, target)

    if args.apply:
        with map_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["original_filename", "new_filename", "notes"],
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote map: {map_path}")
    else:
        print("Dry-run only. Re-run with --apply to copy files and write the map.")

    print(f"Planned {len(rows)} files for {args.homework}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
