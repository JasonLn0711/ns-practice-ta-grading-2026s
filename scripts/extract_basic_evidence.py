#!/usr/bin/env python3
"""Extract basic objective evidence indicators from submissions.

This is not a grader. It scans text-bearing submissions for keywords, accuracy
claims, and checksums so manual grading starts from repeatable evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".py", ".ipynb", ".txt", ".md", ".json", ".csv", ".html"}
CODE_SUFFIXES = {".py", ".ipynb"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract basic evidence indicators.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--submission-dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true", help="Write CSV output.")
    return parser.parse_args()


def files_under(path: Path) -> list[Path]:
    return sorted(file for file in path.rglob("*") if file.is_file())


def read_text(path: Path) -> str:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="ignore").lower()[:2_000_000]
    except OSError:
        return ""


def checksum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bool_text(value: bool) -> str:
    return "yes" if value else "no"


def accuracy_values(text: str) -> list[str]:
    values = []
    for match in re.finditer(r"(?:accuracy|acc)[^0-9]{0,40}([0-9]+(?:\.[0-9]+)?)\s*%?", text):
        values.append(match.group(1))
    return values[:5]


def row_for(homework: str, submission_dir: Path, files: list[Path]) -> dict[str, str]:
    text = "\n".join(read_text(path) for path in files)
    code_present = any(path.suffix.lower() in CODE_SUFFIXES for path in files)
    result_present = "accuracy" in text or "acc" in text
    accuracy = ";".join(accuracy_values(text))
    base = {
        "student_id": "unknown",
        "hw_id": homework,
        "submission_path": submission_dir.as_posix(),
        "evidence_level": "",
        "code_present": bool_text(code_present),
        "result_present": bool_text(result_present),
        "accuracy_value": accuracy,
        "file_count": str(len(files)),
        "sha256_manifest": ";".join(f"{path.name}:{checksum(path)[:12]}" for path in files[:20]),
        "manual_review_needed": "no",
        "notes": "",
    }
    if homework == "hw5":
        base.update(
            {
                "configuration_present": bool_text("configuration" in text or "def config" in text),
                "hyperparameter_terms_present": bool_text(
                    all(term in text for term in ["hidden", "learning", "batch", "epoch"])
                ),
            }
        )
    else:
        base.update(
            {
                "graph_present": bool_text("graph" in text or any("graph" in path.name.lower() for path in files)),
                "momentum_present": bool_text("momentum" in text),
                "filter_plot_present": bool_text("filter" in text or any("filter" in path.name.lower() for path in files)),
                "feature_map_present": bool_text("feature map" in text or any("feature" in path.name.lower() for path in files)),
            }
        )
    return base


def fieldnames(homework: str) -> list[str]:
    common = [
        "student_id",
        "hw_id",
        "submission_path",
        "evidence_level",
        "code_present",
        "result_present",
        "accuracy_value",
    ]
    if homework == "hw5":
        middle = ["configuration_present", "hyperparameter_terms_present"]
    else:
        middle = ["graph_present", "momentum_present", "filter_plot_present", "feature_map_present"]
    return common + middle + ["file_count", "sha256_manifest", "manual_review_needed", "notes"]


def main() -> int:
    args = parse_args()
    submission_dir = args.submission_dir or ROOT / "submissions" / args.homework / "renamed"
    output = args.output or ROOT / "grading" / args.homework / "evidence.csv"

    if not submission_dir.exists():
        print(f"Submission directory does not exist: {submission_dir}")
        return 1

    files = files_under(submission_dir)
    row = row_for(args.homework, submission_dir, files)
    print(f"Scanned {len(files)} files under {submission_dir}")
    for key in fieldnames(args.homework):
        print(f"{key}: {row.get(key, '')}")

    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames(args.homework))
            writer.writeheader()
            writer.writerow(row)
        print(f"Wrote: {output}")
    else:
        print("Dry-run only. Re-run with --write to write CSV output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
