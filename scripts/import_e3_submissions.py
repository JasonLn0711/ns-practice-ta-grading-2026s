#!/usr/bin/env python3
"""Import an E3 assignment ZIP export into private grading folders.

Default mode is dry-run. Use --apply to copy the E3 PDF/ZIP, extract a raw
archive view, create flattened renamed submission files, and write private maps.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from datetime import date
from pathlib import PurePosixPath, Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import E3 assignment submissions.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--archive", type=Path, required=True, help="E3 ZIP export.")
    parser.add_argument("--e3-pdf", type=Path, help="E3 submissions-page PDF snapshot.")
    parser.add_argument(
        "--snapshot-date",
        default=date.today().strftime("%Y%m%d"),
        help="Date label for the E3 PDF snapshot, formatted as YYYYMMDD.",
    )
    parser.add_argument("--apply", action="store_true", help="Actually write files.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing targets.")
    args = parser.parse_args()
    if not re.fullmatch(r"\d{8}", args.snapshot_date):
        parser.error("--snapshot-date must use YYYYMMDD, for example 20260420.")
    return args


def safe_member_path(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if path.is_absolute() or any(part == ".." for part in path.parts):
        raise ValueError(f"unsafe zip member path: {name}")
    return path


def slugify(text: str, fallback: str = "submission") -> str:
    base = "".join(ch.lower() if ch.isascii() and ch.isalnum() else "-" for ch in text)
    base = re.sub(r"-+", "-", base).strip("-")
    return (base or fallback)[:70]


def suffixes_for(name: str) -> str:
    return "".join(Path(name).suffixes).lower()


def stem_for(name: str) -> str:
    suffix = suffixes_for(name)
    return name[: -len(suffix)] if suffix and name.endswith(suffix) else Path(name).stem


def student_id_from(label: str) -> str:
    match = re.search(r"(?<!\d)(\d{9})(?!\d)", label)
    return match.group(1) if match else "unknown"


def submission_id_from(label: str) -> str:
    match = re.search(r"_(\d+)_assignsubmission_file", label)
    return match.group(1) if match else ""


def export_timestamp_from(path: Path) -> str:
    zip_match = re.search(r"-(\d{6})\.zip$", path.name)
    if zip_match:
        return zip_match.group(1)
    return ""


def copy_file(source: Path, target: Path, apply: bool, overwrite: bool) -> str:
    if target.exists() and not overwrite:
        return "exists"
    if apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return "copied" if apply else "planned"


def write_zip_member(zip_file: ZipFile, member_name: str, target: Path, overwrite: bool) -> str:
    if target.exists() and not overwrite:
        return "exists"
    target.parent.mkdir(parents=True, exist_ok=True)
    with zip_file.open(member_name) as source, target.open("wb") as dest:
        shutil.copyfileobj(source, dest)
    return "copied"


def plan_export_files(
    homework: str, archive: Path, e3_pdf: Path | None, snapshot_date: str
) -> list[tuple[Path, str, str]]:
    timestamp = export_timestamp_from(archive)
    planned: list[tuple[Path, str, str]] = [
        (
            archive,
            f"{homework}_e3-submissions-archive-{timestamp or 'export'}.zip",
            "E3 ZIP export containing submitted files.",
        )
    ]
    if e3_pdf is not None:
        planned.append(
            (
                e3_pdf,
                f"{homework}_e3-submissions-snapshot-{snapshot_date}.pdf",
                "E3 submissions-page PDF snapshot; includes status/late/no-submission rows.",
            )
        )
    return planned


def main() -> int:
    args = parse_args()
    if not args.archive.exists():
        print(f"Archive not found: {args.archive}")
        return 1
    if args.e3_pdf and not args.e3_pdf.exists():
        print(f"E3 PDF not found: {args.e3_pdf}")
        return 1

    hw_root = ROOT / "submissions" / args.homework
    raw_dir = hw_root / "raw"
    renamed_dir = hw_root / "renamed"
    extracted_root = hw_root / "extracted" / "e3_export_raw"
    rename_map_path = hw_root / "rename_map.csv"
    student_map_path = hw_root / "student_file_map.csv"

    for path in [raw_dir, renamed_dir, extracted_root]:
        if args.apply:
            path.mkdir(parents=True, exist_ok=True)

    rename_rows: list[dict[str, str]] = []
    student_rows: list[dict[str, str]] = []

    for source, new_name, note in plan_export_files(
        args.homework, args.archive, args.e3_pdf, args.snapshot_date
    ):
        raw_status = copy_file(source, raw_dir / source.name, args.apply, args.overwrite)
        renamed_status = copy_file(source, renamed_dir / new_name, args.apply, args.overwrite)
        print(f"{raw_status}: raw {source.name}")
        print(f"{renamed_status}: renamed {new_name}")
        rename_rows.append(
            {
                "original_filename": source.name,
                "new_filename": new_name,
                "notes": note,
            }
        )

    per_student_counts: dict[str, int] = {}
    with ZipFile(args.archive) as zip_file:
        members = [info for info in zip_file.infolist() if not info.is_dir()]
        for info in members:
            member_path = safe_member_path(info.filename)
            parts = member_path.parts
            label = parts[0] if parts else ""
            original_short = parts[-1] if parts else info.filename
            student_id = student_id_from(label)
            submission_id = submission_id_from(label)
            per_student_counts[student_id] = per_student_counts.get(student_id, 0) + 1
            seq = per_student_counts[student_id]
            suffix = suffixes_for(original_short)
            short_slug = slugify(stem_for(original_short))
            new_name = f"{args.homework}_{student_id}_{seq:02d}_{short_slug}{suffix}"

            raw_extract_target = extracted_root / member_path
            renamed_target = renamed_dir / new_name
            if args.apply:
                raw_status = write_zip_member(zip_file, info.filename, raw_extract_target, args.overwrite)
                renamed_status = write_zip_member(zip_file, info.filename, renamed_target, args.overwrite)
            else:
                raw_status = "planned"
                renamed_status = "planned"

            print(f"{renamed_status}: {info.filename} -> {new_name}")
            rename_rows.append(
                {
                    "original_filename": info.filename,
                    "new_filename": new_name,
                    "notes": f"student_id={student_id}; submission_id={submission_id}; from E3 ZIP",
                }
            )
            student_rows.append(
                {
                    "homework": args.homework,
                    "student_id": student_id,
                    "student_label": label,
                    "assignment_submission_id": submission_id,
                    "original_zip_path": info.filename,
                    "original_filename": original_short,
                    "new_filename": new_name,
                    "raw_extracted_path": raw_extract_target.as_posix(),
                    "renamed_path": renamed_target.as_posix(),
                    "notes": "private identity-bearing map",
                }
            )

    if args.apply:
        with rename_map_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, ["original_filename", "new_filename", "notes"])
            writer.writeheader()
            writer.writerows(rename_rows)

        with student_map_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                [
                    "homework",
                    "student_id",
                    "student_label",
                    "assignment_submission_id",
                    "original_zip_path",
                    "original_filename",
                    "new_filename",
                    "raw_extracted_path",
                    "renamed_path",
                    "notes",
                ],
            )
            writer.writeheader()
            writer.writerows(student_rows)
        print(f"Wrote private maps: {rename_map_path}, {student_map_path}")
    else:
        print("Dry-run only. Re-run with --apply to write files and maps.")

    unique_students = sorted({row["student_id"] for row in student_rows})
    print(f"Imported plan for {len(student_rows)} files across {len(unique_students)} student ids.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
