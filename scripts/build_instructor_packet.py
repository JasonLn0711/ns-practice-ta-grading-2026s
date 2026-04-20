#!/usr/bin/env python3
"""Build a sanitized instructor-confirmation packet.

The packet is a local working copy of approved summary/policy files only.
It intentionally excludes raw submissions, workbook binaries, score CSVs,
deduction CSVs, and per-student notes unless the instructor asks later.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKET_NAME = "instructor_confirmation_2026-04-20"
DEFAULT_OUTPUT_DIR = ROOT / "release_packets" / DEFAULT_PACKET_NAME
REPORT_PATH = ROOT / "reports" / "instructor_packet_build_report.md"

DEFAULT_FILES = [
    "reports/instructor_confirmation_outbox.md",
    "reports/instructor_policy_confirmation_packet.md",
    "reports/hw5_instructor_report.md",
    "reports/hw6_instructor_report.md",
    "reports/hw6_master_audit_report.md",
]

OPTIONAL_FILES = [
    "reports/hw6_code_audit_report.md",
    "reports/hw6_figure_audit_report.md",
    "reports/hw6_workbook_writeback_report.md",
]

FORBIDDEN_PARTS = {
    "raw",
    "renamed",
    "extracted",
    "feedback",
    "student_notes",
}
FORBIDDEN_SUFFIXES = {".csv", ".xlsx", ".xls", ".zip", ".gz", ".ipynb", ".pdf"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a safe instructor packet.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Destination packet directory. Defaults to release_packets/instructor_confirmation_2026-04-20.",
    )
    parser.add_argument(
        "--include-optional",
        action="store_true",
        help="Also include optional HW6 detailed reports.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Create/copy files. Without this flag, only print the plan.",
    )
    return parser.parse_args()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_allowed(rel: str) -> None:
    path = Path(rel)
    parts = set(path.parts)
    if parts & FORBIDDEN_PARTS:
        raise SystemExit(f"Refusing to include forbidden path: {rel}")
    if path.suffix.lower() in FORBIDDEN_SUFFIXES:
        raise SystemExit(f"Refusing to include forbidden file type: {rel}")
    if not rel.startswith("reports/"):
        raise SystemExit(f"Refusing to include non-report file: {rel}")


def build_plan(include_optional: bool) -> list[Path]:
    rels = list(DEFAULT_FILES)
    if include_optional:
        rels.extend(OPTIONAL_FILES)

    sources: list[Path] = []
    for rel in rels:
        validate_allowed(rel)
        source = ROOT / rel
        if not source.exists():
            raise SystemExit(f"Missing packet source: {rel}")
        sources.append(source)
    return sources


def packet_path(output_dir: Path) -> Path:
    if output_dir.is_absolute():
        return output_dir
    return ROOT / output_dir


def render_report(sources: list[Path], output_dir: Path, applied: bool) -> str:
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    packet_rel = relative(output_dir) if output_dir.is_relative_to(ROOT) else str(output_dir)
    lines = [
        "# Instructor Packet Build Report",
        "",
        f"Generated: `{timestamp}`",
        f"Packet directory: `{packet_rel}`",
        f"Applied: `{'yes' if applied else 'no'}`",
        "",
        "## Purpose",
        "",
        "This report records the sanitized instructor-confirmation packet. The packet",
        "contains summary/policy Markdown files only; raw submissions, workbook",
        "binaries, score CSVs, deduction CSVs, and per-student notes are excluded.",
        "",
        "## Files Included",
        "",
        "| Source | Packet file | SHA-256 |",
        "| --- | --- | --- |",
    ]
    for source in sources:
        destination = output_dir / source.name
        dest_rel = relative(destination) if destination.is_relative_to(ROOT) else str(destination)
        digest = sha256(source)
        lines.append(f"| `{relative(source)}` | `{dest_rel}` | `{digest}` |")

    lines.extend([
        "",
        "## Files Explicitly Excluded",
        "",
        "- `submissions/*/raw/`",
        "- `submissions/*/renamed/`",
        "- `submissions/*/extracted/`",
        "- `course_materials/*/raw/`",
        "- `course_materials/*/renamed/`",
        "- `grading/*/feedback/`",
        "- `grading/*/student_notes/`",
        "- `grading/*/*scores.csv`",
        "- `grading/*/*deduction*.csv`",
        "",
        "## Next Step",
        "",
        "Attach files from the packet directory only after adding the instructor",
        "recipient to `reports/instructor_confirmation_outbox.md` or the mail client.",
        "Record the send event in `reports/release_decision_log.md`.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    sources = build_plan(args.include_optional)
    output_dir = packet_path(args.output_dir)

    print("Instructor packet plan:")
    print(f"- Output directory: {output_dir}")
    for source in sources:
        print(f"- Include: {relative(source)}")

    if args.apply:
        output_dir.mkdir(parents=True, exist_ok=True)
        for source in sources:
            shutil.copy2(source, output_dir / source.name)
        report = render_report(sources, output_dir, applied=True)
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"Wrote {relative(REPORT_PATH)}")
    else:
        print("Dry run only. Re-run with --apply to copy files and write the report.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
