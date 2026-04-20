#!/usr/bin/env python3
"""Run light required-evidence checks for one homework submission folder.

This script does not grade. It only flags evidence that is present or missing.
"""

from __future__ import annotations

import argparse
from pathlib import Path


TEXT_SUFFIXES = {".py", ".ipynb", ".md", ".txt", ".csv", ".json", ".html"}
CODE_SUFFIXES = {".py", ".ipynb"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".pdf", ".svg"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check required homework evidence.")
    parser.add_argument("--homework", choices=["hw5", "hw6"], default="hw5")
    parser.add_argument(
        "--submission-dir",
        type=Path,
        required=True,
        help="Folder containing one student's extracted or submitted files.",
    )
    return parser.parse_args()


def all_files(path: Path) -> list[Path]:
    return sorted(p for p in path.rglob("*") if p.is_file())


def has_suffix(files: list[Path], suffixes: set[str]) -> bool:
    return any(path.suffix.lower() in suffixes for path in files)


def name_contains(files: list[Path], terms: list[str], suffixes: set[str] | None = None) -> bool:
    for path in files:
        if suffixes and path.suffix.lower() not in suffixes:
            continue
        name = path.name.lower()
        if all(term in name for term in terms):
            return True
    return False


def read_text_sample(path: Path) -> str:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:1_000_000].lower()
    except OSError:
        return ""


def content_contains(files: list[Path], terms: list[str]) -> bool:
    for path in files:
        text = read_text_sample(path)
        if text and all(term.lower() in text for term in terms):
            return True
    return False


def checks_for(homework: str, files: list[Path]) -> list[tuple[str, bool, str]]:
    if homework == "hw5":
        return [
            ("code_or_notebook", has_suffix(files, CODE_SUFFIXES), "Expect .ipynb or .py."),
            (
                "configuration_evidence",
                content_contains(files, ["configuration"]) or content_contains(files, ["def config"]),
                "Look for configuration function/workflow.",
            ),
            (
                "hyperparameter_evidence",
                content_contains(files, ["hidden", "learning", "batch", "epoch"]),
                "Look for hidden nodes, learning rate, batch size, and epochs.",
            ),
            (
                "accuracy_evidence",
                content_contains(files, ["accuracy"]) and content_contains(files, ["98"]),
                "Look for MNIST test accuracy near the 98% target.",
            ),
        ]

    return [
        ("code_or_notebook", has_suffix(files, CODE_SUFFIXES), "Expect .ipynb or .py."),
        (
            "graph_evidence",
            name_contains(files, ["graph"], IMAGE_SUFFIXES) or content_contains(files, ["computational graph"]),
            "Look for computational graph evidence.",
        ),
        (
            "momentum_evidence",
            content_contains(files, ["momentum"]),
            "Look for mini-batch SGD with momentum.",
        ),
        (
            "filter_plot_evidence",
            name_contains(files, ["filter"], IMAGE_SUFFIXES) or content_contains(files, ["learned filter"]),
            "Look for learned-filter plot evidence.",
        ),
        (
            "feature_map_evidence",
            name_contains(files, ["feature"], IMAGE_SUFFIXES) or content_contains(files, ["feature map"]),
            "Look for intermediate feature-map plot evidence.",
        ),
        (
            "accuracy_evidence",
            content_contains(files, ["accuracy"]) and content_contains(files, ["98"]),
            "Look for MNIST test accuracy near the 98% target.",
        ),
    ]


def main() -> int:
    args = parse_args()
    if not args.submission_dir.exists():
        print(f"Submission directory does not exist: {args.submission_dir}")
        return 1

    files = all_files(args.submission_dir)
    checks = checks_for(args.homework, files)

    missing = 0
    print(f"Checked {len(files)} files in {args.submission_dir}")
    for label, ok, hint in checks:
        status = "OK" if ok else "MISSING"
        print(f"{status}: {label} - {hint}")
        if not ok:
            missing += 1

    print(f"Summary: {len(checks) - missing}/{len(checks)} checks passed.")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
