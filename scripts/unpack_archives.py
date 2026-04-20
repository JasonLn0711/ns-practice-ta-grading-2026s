#!/usr/bin/env python3
"""Safely unpack ZIP/TAR archives into submissions/<hw>/extracted.

Default mode is dry-run. Use --apply to extract. The script rejects archive
members with absolute paths or parent-directory traversal.
"""

from __future__ import annotations

import argparse
import shutil
import tarfile
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Safely unpack homework archives.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--dest-dir", type=Path)
    parser.add_argument("--apply", action="store_true", help="Actually extract archives.")
    parser.add_argument("--overwrite", action="store_true", help="Remove existing output folder first.")
    return parser.parse_args()


def slugify(text: str) -> str:
    safe = "".join(ch.lower() if ch.isalnum() else "-" for ch in text).strip("-")
    while "--" in safe:
        safe = safe.replace("--", "-")
    return safe or "archive"


def archive_stem(path: Path) -> str:
    name = path.name
    for suffix in reversed(path.suffixes):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
    return slugify(name)


def is_archive(path: Path) -> bool:
    suffixes = [suffix.lower() for suffix in path.suffixes]
    return path.suffix.lower() == ".zip" or suffixes[-2:] == [".tar", ".gz"] or path.suffix.lower() in {".tar", ".tgz"}


def safe_member(name: str) -> bool:
    member = PurePosixPath(name)
    return not member.is_absolute() and ".." not in member.parts


def safe_extract_zip(archive: Path, out_dir: Path) -> int:
    count = 0
    with zipfile.ZipFile(archive) as handle:
        for info in handle.infolist():
            if not safe_member(info.filename):
                raise ValueError(f"unsafe zip member: {info.filename}")
        handle.extractall(out_dir)
        count = sum(1 for info in handle.infolist() if not info.is_dir())
    return count


def safe_extract_tar(archive: Path, out_dir: Path) -> int:
    count = 0
    with tarfile.open(archive) as handle:
        members = handle.getmembers()
        for member in members:
            if not safe_member(member.name):
                raise ValueError(f"unsafe tar member: {member.name}")
        handle.extractall(out_dir)
        count = sum(1 for member in members if member.isfile())
    return count


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir or ROOT / "submissions" / args.homework / "renamed"
    dest_dir = args.dest_dir or ROOT / "submissions" / args.homework / "extracted"

    if not source_dir.exists():
        print(f"Source directory does not exist: {source_dir}")
        return 1

    archives = [path for path in sorted(source_dir.iterdir()) if path.is_file() and is_archive(path)]
    extracted = 0
    skipped = 0
    failed = 0

    for archive in archives:
        out_dir = dest_dir / archive_stem(archive)
        if out_dir.exists() and not args.overwrite:
            print(f"exists: {archive.name} -> {out_dir}")
            skipped += 1
            continue
        print(f"{'extract' if args.apply else 'would extract'}: {archive.name} -> {out_dir}")
        if not args.apply:
            continue
        try:
            if out_dir.exists() and args.overwrite:
                shutil.rmtree(out_dir)
            out_dir.mkdir(parents=True, exist_ok=True)
            if archive.suffix.lower() == ".zip":
                extracted += safe_extract_zip(archive, out_dir)
            else:
                extracted += safe_extract_tar(archive, out_dir)
        except (OSError, ValueError, tarfile.TarError, zipfile.BadZipFile) as exc:
            print(f"failed: {archive.name}: {exc}")
            failed += 1

    if not args.apply:
        print("Dry-run only. Re-run with --apply to extract archives.")
    print(f"Summary: archives={len(archives)} extracted_files={extracted} skipped={skipped} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
