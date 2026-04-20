#!/usr/bin/env python3
"""Unpack homework archives into submissions/<hw>/extracted.

Default mode is dry-run. Use --apply to unpack. RAR archives require either
`unrar` or `7z` to be installed locally.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Unpack homework archives safely.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], default="hw5")
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--dest-dir", type=Path)
    parser.add_argument("--apply", action="store_true", help="Actually unpack archives.")
    return parser.parse_args()


def archive_output_dir(dest_dir: Path, archive: Path) -> Path:
    name = archive.name
    for suffix in reversed(archive.suffixes):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
    safe = "".join(char if char.isalnum() else "-" for char in name.lower()).strip("-")
    return dest_dir / (safe or archive.stem)


def is_supported_archive(path: Path) -> bool:
    suffixes = [suffix.lower() for suffix in path.suffixes]
    return any(
        suffixes[-len(pattern) :] == list(pattern)
        for pattern in [
            (".zip",),
            (".tar",),
            (".tar", ".gz"),
            (".tgz",),
            (".rar",),
        ]
    )


def unpack_with_python(archive: Path, out_dir: Path) -> None:
    shutil.unpack_archive(str(archive), str(out_dir))


def unpack_rar(archive: Path, out_dir: Path) -> bool:
    unrar = shutil.which("unrar")
    if unrar:
        subprocess.run([unrar, "x", "-o-", str(archive), str(out_dir)], check=True)
        return True

    seven_zip = shutil.which("7z")
    if seven_zip:
        subprocess.run([seven_zip, "x", str(archive), f"-o{out_dir}"], check=True)
        return True

    return False


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir or ROOT / "submissions" / args.homework / "renamed"
    dest_dir = args.dest_dir or ROOT / "submissions" / args.homework / "extracted"

    if not source_dir.exists():
        print(f"Source directory does not exist: {source_dir}")
        return 1

    dest_dir.mkdir(parents=True, exist_ok=True)
    archives = [p for p in sorted(source_dir.iterdir()) if p.is_file() and is_supported_archive(p)]

    unpacked = 0
    skipped = 0
    failed = 0

    for archive in archives:
        out_dir = archive_output_dir(dest_dir, archive)
        if out_dir.exists():
            print(f"skip existing: {archive.name} -> {out_dir.name}")
            skipped += 1
            continue

        action = "unpack" if args.apply else "would unpack"
        print(f"{action}: {archive.name} -> {out_dir}")

        if not args.apply:
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        try:
            if archive.suffix.lower() == ".rar":
                if not unpack_rar(archive, out_dir):
                    print(f"cannot unpack RAR without unrar or 7z: {archive.name}")
                    failed += 1
                    continue
            else:
                unpack_with_python(archive, out_dir)
            unpacked += 1
        except (OSError, shutil.ReadError, subprocess.CalledProcessError) as exc:
            print(f"failed: {archive.name}: {exc}")
            failed += 1

    if not args.apply:
        print("Dry-run only. Re-run with --apply to unpack archives.")

    print(
        f"Archives found: {len(archives)}; unpacked: {unpacked}; "
        f"skipped: {skipped}; failed: {failed}."
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
