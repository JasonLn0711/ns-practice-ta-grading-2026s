#!/usr/bin/env python3
"""Check objective submission-structure evidence.

This script does not grade. It records whether expected evidence indicators are
present so the TA can grade consistently.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".py", ".ipynb", ".txt", ".md", ".json", ".csv", ".html"}
CODE_SUFFIXES = {".py", ".ipynb"}
GRAPH_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".svg"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check submission structure.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], required=True)
    parser.add_argument("--submission-dir", type=Path)
    parser.add_argument("--student-map", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true", help="Write CSV output.")
    return parser.parse_args()


def all_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


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


def text_for(path: Path) -> str:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="ignore").lower()[:1_000_000]
    except OSError:
        return ""


def any_suffix(files: list[Path], suffixes: set[str]) -> bool:
    return any(path.suffix.lower() in suffixes for path in files)


def any_name(files: list[Path], terms: list[str], suffixes: set[str] | None = None) -> bool:
    for path in files:
        if suffixes and path.suffix.lower() not in suffixes:
            continue
        name = path.name.lower()
        if all(term in name for term in terms):
            return True
    return False


def any_text(files: list[Path], terms: list[str]) -> bool:
    for path in files:
        text = text_for(path)
        if text and all(term.lower() in text for term in terms):
            return True
    return False


def checks(homework: str, files: list[Path]) -> list[tuple[str, bool, str]]:
    if homework == "hw5":
        return [
            ("code_present", any_suffix(files, CODE_SUFFIXES), "Expect notebook or Python code."),
            ("configuration_present", any_text(files, ["configuration"]) or any_text(files, ["def config"]), "Configuration workflow evidence."),
            ("hyperparameters_present", any_text(files, ["hidden"]) and any_text(files, ["learning"]) and any_text(files, ["batch"]) and any_text(files, ["epoch"]), "Hidden nodes, learning rate, batch size, epoch."),
            ("accuracy_present", any_text(files, ["accuracy"]) and any_text(files, ["98"]), "MNIST accuracy evidence near target."),
        ]
    return [
        ("code_present", any_suffix(files, CODE_SUFFIXES), "Expect notebook or Python code."),
        ("graph_present", any_name(files, ["graph"], GRAPH_SUFFIXES) or any_text(files, ["computational graph"]), "Computational graph evidence."),
        ("momentum_present", any_text(files, ["momentum"]), "Momentum evidence."),
        ("filter_plot_present", any_name(files, ["filter"], GRAPH_SUFFIXES) or any_text(files, ["filter"]), "Learned filter plot evidence."),
        ("feature_map_present", any_name(files, ["feature"], GRAPH_SUFFIXES) or any_text(files, ["feature map"]), "Feature-map evidence."),
        ("accuracy_present", any_text(files, ["accuracy"]) and any_text(files, ["98"]), "MNIST accuracy evidence near target."),
    ]


def main() -> int:
    args = parse_args()
    submission_dir = args.submission_dir or ROOT / "submissions" / args.homework / "renamed"
    map_path = args.student_map or ROOT / "submissions" / args.homework / "student_file_map.csv"
    output = args.output or ROOT / "grading" / args.homework / "structure_check.csv"

    if not submission_dir.exists():
        print(f"Submission directory does not exist: {submission_dir}")
        return 1

    groups = mapped_groups(args.homework, submission_dir, map_path)
    if not groups:
        groups = [{"student_id": "unknown", "student_name": "", "files": all_files(submission_dir)}]

    rows = []
    missing = 0
    for group in groups:
        files = list(group["files"])
        submission_files = ";".join(path.name for path in files)
        for label, ok, note in checks(args.homework, files):
            rows.append(
                {
                    "student_id": str(group["student_id"]),
                    "student_name": str(group["student_name"]),
                    "hw_id": args.homework,
                    "submission_files": submission_files,
                    "check": label,
                    "status": "ok" if ok else "missing",
                    "note": note,
                }
            )
            if not ok:
                missing += 1
            print(f"{group['student_id']} {'OK' if ok else 'MISSING'}: {label} - {note}")

    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                ["student_id", "student_name", "hw_id", "submission_files", "check", "status", "note"],
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote: {output}")
    else:
        print("Dry-run only. Re-run with --write to write CSV output.")

    file_count = sum(len(group["files"]) for group in groups)
    print(f"Summary: students={len(groups)} files={file_count} checks={len(rows)} missing={missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
