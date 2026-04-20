#!/usr/bin/env python3
"""Check whether HW5/HW6 grading is ready for release.

This script does not change grades. It records objective release blockers so
the TA does not rely on memory before sending grades or importing a workbook.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "reports" / "final_release_gate_report.md"

REQUIRED_FILES = [
    "reports/instructor_confirmation_outbox.md",
    "reports/instructor_confirmation_send_checklist.md",
    "reports/post_instructor_reply_runbook.md",
    "reports/release_decision_log.md",
    "reports/release_packet_manifest.md",
    "reports/release_readiness_review.md",
    "reports/hw5_instructor_report.md",
    "reports/hw6_instructor_report.md",
    "reports/hw6_master_audit_report.md",
    "reports/hw6_workbook_writeback_report.md",
    "grading/hw5/scores.csv",
    "grading/hw5/deduction_log.csv",
    "grading/hw6/code_scores.csv",
    "grading/hw6/figure_scores.csv",
    "grading/hw6/combined_summary.csv",
    "grading/hw6/code_deduction_log.csv",
    "grading/hw6/figure_deduction_log.csv",
]

FORBIDDEN_TRACKED_PARTS = [
    "/raw/",
    "/renamed/",
    "/extracted/",
]

STATUS_IGNORE_PATHS = {"reports/final_release_gate_report.md"}


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check final grading release gate.")
    parser.add_argument(
        "--write",
        action="store_true",
        help=f"Write Markdown report to {REPORT_PATH.relative_to(ROOT)}.",
    )
    return parser.parse_args()


def run(command: list[str]) -> tuple[int, str]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return completed.returncode, completed.stdout.strip()


def status(ok: bool, blocked: bool = False) -> str:
    if blocked:
        return "blocked"
    return "pass" if ok else "fail"


def check_required_files() -> CheckResult:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).exists()]
    if missing:
        return CheckResult("Required release files", "fail", ", ".join(missing))
    return CheckResult("Required release files", "pass", f"{len(REQUIRED_FILES)} files present")


def check_validations() -> list[CheckResult]:
    checks = [
        ("Compile scripts", [sys.executable, "-m", "py_compile", *map(str, sorted((ROOT / "scripts").glob("*.py")))]),
        ("Validate HW5 grading records", [sys.executable, "scripts/validate_grading_records.py", "--homework", "hw5"]),
        ("Validate HW6 dual grading records", [sys.executable, "scripts/validate_hw6_dual_grading.py"]),
        ("Git whitespace check", ["git", "diff", "--check"]),
    ]
    results: list[CheckResult] = []
    for name, command in checks:
        code, output = run(command)
        first_lines = "\n".join(output.splitlines()[:8])
        results.append(CheckResult(name, status(code == 0), first_lines or "ok"))
    return results


def check_git_status() -> CheckResult:
    code, output = run(["git", "status", "--short"])
    if code != 0:
        return CheckResult("Git status", "fail", output)
    filtered: list[str] = []
    for line in output.splitlines():
        path = line[3:].strip()
        if path not in STATUS_IGNORE_PATHS:
            filtered.append(line)
    if filtered:
        return CheckResult("Git status", "fail", "\n".join(filtered))
    return CheckResult("Git status", "pass", "working tree clean")


def check_forbidden_tracked_files() -> CheckResult:
    code, output = run(["git", "ls-files"])
    if code != 0:
        return CheckResult("Tracked private artifacts", "fail", output)
    forbidden: list[str] = []
    for line in output.splitlines():
        normalized = f"/{line}"
        if line.endswith(".gitkeep"):
            continue
        if any(part in normalized for part in FORBIDDEN_TRACKED_PARTS):
            forbidden.append(line)
    if forbidden:
        return CheckResult("Tracked private artifacts", "fail", "\n".join(forbidden[:20]))
    return CheckResult("Tracked private artifacts", "pass", "no tracked raw/renamed/extracted files")


def check_decision_log() -> list[CheckResult]:
    path = ROOT / "reports" / "release_decision_log.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    pending_rows = [
        line for line in text.splitlines()
        if line.startswith("| HW") and "| pending |" in line
    ]
    send_events = [
        line for line in text.splitlines()
        if line.startswith("Date sent:") and line.partition(":")[2].strip()
    ]
    late_pending = any(row.startswith("| HW5-D5") or row.startswith("| HW6-D5") for row in pending_rows)

    results = [
        CheckResult(
            "Instructor decisions",
            status(not pending_rows, blocked=bool(pending_rows)),
            f"{len(pending_rows)} pending decisions" if pending_rows else "all decisions resolved",
        ),
        CheckResult(
            "Confirmation email send event",
            status(bool(send_events), blocked=not send_events),
            "send event recorded" if send_events else "no completed send event recorded",
        ),
        CheckResult(
            "Late policy",
            status(not late_pending, blocked=late_pending),
            "late policy pending" if late_pending else "late policy resolved or not applicable",
        ),
    ]
    return results


def check_workbook_output() -> CheckResult:
    output = ROOT / "course_materials" / "hw6" / "renamed" / "(114下)深度學習成績和分組_hw6_scored.xlsx"
    if not output.exists():
        return CheckResult("HW6 workbook copy", "fail", f"missing {output.relative_to(ROOT)}")
    code, ignored = run(["git", "check-ignore", str(output.relative_to(ROOT))])
    if code != 0:
        return CheckResult("HW6 workbook copy", "fail", "workbook copy exists but is not ignored by Git")
    return CheckResult("HW6 workbook copy", "pass", "output workbook exists and is ignored")


def render_report(results: list[CheckResult]) -> str:
    blockers = [result for result in results if result.status == "blocked"]
    failures = [result for result in results if result.status == "fail"]
    ready = not blockers and not failures

    lines = [
        "# Final Release Gate Report",
        "",
        f"Generated: `{datetime.now().astimezone().isoformat(timespec='seconds')}`",
        f"Release ready: `{'yes' if ready else 'no'}`",
        "",
        "## Summary",
        "",
        f"- Passed checks: `{sum(1 for result in results if result.status == 'pass')}`",
        f"- Blocking checks: `{len(blockers)}`",
        f"- Failed checks: `{len(failures)}`",
        "",
        "## Checks",
        "",
        "| Check | Status | Detail |",
        "| --- | --- | --- |",
    ]
    for result in results:
        detail = result.detail.replace("\n", "<br>")
        lines.append(f"| {result.name} | `{result.status}` | {detail} |")

    lines.extend([
        "",
        "## Current Release Decision",
        "",
    ])
    if ready:
        lines.append("The grading records are ready for final release workflow.")
    else:
        lines.append("Do not release grades yet. Resolve all `blocked` and `fail` checks first.")

    lines.extend([
        "",
        "## Next Action",
        "",
        "- If the only blockers are instructor decisions, send `reports/instructor_confirmation_outbox.md`.",
        "- After the instructor replies, use `reports/post_instructor_reply_runbook.md`.",
        "- Re-run this script after recording the reply and applying any policy changes.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    results: list[CheckResult] = []
    results.append(check_required_files())
    results.extend(check_validations())
    results.append(check_workbook_output())
    results.append(check_forbidden_tracked_files())
    results.append(check_git_status())
    results.extend(check_decision_log())

    report = render_report(results)
    print(report)

    if args.write:
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"Wrote {REPORT_PATH.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
