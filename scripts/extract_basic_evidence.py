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
    parser.add_argument("--student-map", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true", help="Write CSV output.")
    return parser.parse_args()


def files_under(path: Path) -> list[Path]:
    return sorted(file for file in path.rglob("*") if file.is_file())


def read_existing_rows(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {
            row.get("student_id", "").strip(): row
            for row in csv.DictReader(handle)
            if row.get("student_id", "").strip()
        }


def student_name(student_id: str, label: str) -> str:
    remainder = label.replace(student_id, "", 1).strip()
    if not remainder:
        return ""
    return remainder.split()[0]


def mapped_groups(homework: str, submission_dir: Path, map_path: Path) -> list[dict[str, object]]:
    if not map_path.exists():
        return []

    groups: dict[str, dict[str, object]] = {}
    with map_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("homework") != homework:
                continue
            student_id = row.get("student_id", "").strip()
            new_filename = row.get("new_filename", "").strip()
            if not student_id or not new_filename:
                continue
            group = groups.setdefault(
                student_id,
                {
                    "student_id": student_id,
                    "student_name": student_name(student_id, row.get("student_label", "")),
                    "files": [],
                },
            )
            file_path = submission_dir / new_filename
            if file_path.exists():
                group["files"].append(file_path)

    return [groups[key] for key in sorted(groups)]


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


def accuracy_candidates(text: str) -> list[float]:
    """Return plausible accuracy values normalized to percent.

    This deliberately stays conservative. It ignores tiny integers such as
    `acc_1` or loop counters, keeps explicit percentages, keeps decimal
    fractions such as `0.9812`, and keeps plain values that look like percent
    scores such as `98.12`.
    """
    values: list[float] = []

    for match in re.finditer(r"(?:accuracy|acc)[^\n\r]{0,80}?([0-9]+(?:\.[0-9]+)?)\s*%", text):
        value = float(match.group(1))
        if 0 <= value <= 100:
            values.append(value)

    for match in re.finditer(r"(?:accuracy|acc)[^\n\r]{0,80}?([0-9]+(?:\.[0-9]+)?)", text):
        raw = match.group(1)
        value = float(raw)
        if raw.startswith("0.") and 0.5 <= value < 1:
            values.append(value * 100)
        elif 10 <= value <= 100:
            values.append(value)

    unique: list[float] = []
    seen: set[str] = set()
    for value in values:
        key = f"{value:.4f}"
        if key not in seen:
            seen.add(key)
            unique.append(value)
    return unique


def accuracy_values(text: str) -> list[str]:
    return [f"{value:.2f}" for value in accuracy_candidates(text)[:12]]


def row_for(
    homework: str,
    student_id: str,
    name: str,
    submission_dir: Path,
    files: list[Path],
) -> dict[str, str]:
    text = "\n".join(read_text(path) for path in files)
    code_present = any(path.suffix.lower() in CODE_SUFFIXES for path in files)
    result_present = "accuracy" in text or "acc" in text
    accuracy = ";".join(accuracy_values(text))
    candidates = accuracy_candidates(text)
    base = {
        "student_id": student_id,
        "student_name": name,
        "hw_id": homework,
        "submission_path": submission_dir.as_posix(),
        "submission_files": ";".join(path.name for path in files),
        "evidence_level": "",
        "code_present": bool_text(code_present),
        "result_present": bool_text(result_present),
        "logs_present": bool_text("log" in text or "epoch" in text or "loss" in text),
        "accuracy_value": accuracy,
        "max_accuracy_candidate": f"{max(candidates):.2f}" if candidates else "",
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
        "student_name",
        "hw_id",
        "submission_path",
        "submission_files",
        "evidence_level",
        "code_present",
        "result_present",
        "logs_present",
        "accuracy_value",
        "max_accuracy_candidate",
    ]
    if homework == "hw5":
        middle = ["configuration_present", "hyperparameter_terms_present"]
    else:
        middle = ["graph_present", "momentum_present", "filter_plot_present", "feature_map_present"]
    return common + middle + ["file_count", "sha256_manifest", "manual_review_needed", "notes"]


def main() -> int:
    args = parse_args()
    submission_dir = args.submission_dir or ROOT / "submissions" / args.homework / "renamed"
    map_path = args.student_map or ROOT / "submissions" / args.homework / "student_file_map.csv"
    output = args.output or ROOT / "grading" / args.homework / "evidence.csv"

    if not submission_dir.exists():
        print(f"Submission directory does not exist: {submission_dir}")
        return 1

    groups = mapped_groups(args.homework, submission_dir, map_path)
    if not groups:
        groups = [{"student_id": "unknown", "student_name": "", "files": files_under(submission_dir)}]

    existing_rows = read_existing_rows(output)
    rows = []
    for group in groups:
        row = row_for(
            args.homework,
            str(group["student_id"]),
            str(group["student_name"]),
            submission_dir,
            list(group["files"]),
        )
        previous = existing_rows.get(row["student_id"], {})
        for field in ["evidence_level", "manual_review_needed", "notes"]:
            if previous.get(field, "").strip():
                row[field] = previous[field]
        rows.append(row)
    print(f"Scanned {sum(len(group['files']) for group in groups)} mapped files under {submission_dir}")
    for row in rows:
        print(
            "student={student_id} files={file_count} code={code_present} result={result_present} "
            "max_accuracy={max_accuracy_candidate} accuracy={accuracy_value}".format(**row)
        )

    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames(args.homework), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote: {output}")
    else:
        print("Dry-run only. Re-run with --write to write CSV output.")
    print(f"Summary: students={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
