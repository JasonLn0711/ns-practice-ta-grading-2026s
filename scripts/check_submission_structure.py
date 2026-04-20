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
    parser.add_argument("--output", type=Path)
    parser.add_argument("--write", action="store_true", help="Write CSV output.")
    return parser.parse_args()


def all_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if path.is_file())


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
    output = args.output or ROOT / "grading" / args.homework / "structure_check.csv"

    if not submission_dir.exists():
        print(f"Submission directory does not exist: {submission_dir}")
        return 1

    files = all_files(submission_dir)
    rows = []
    for label, ok, note in checks(args.homework, files):
        rows.append({"hw_id": args.homework, "check": label, "status": "ok" if ok else "missing", "note": note})
        print(f"{'OK' if ok else 'MISSING'}: {label} - {note}")

    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, ["hw_id", "check", "status", "note"])
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote: {output}")
    else:
        print("Dry-run only. Re-run with --write to write CSV output.")

    missing = sum(1 for row in rows if row["status"] == "missing")
    print(f"Summary: files={len(files)} checks={len(rows)} missing={missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
