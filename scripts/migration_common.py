#!/usr/bin/env python3
"""Shared helpers for safe TA grading workspace migration scripts."""

from __future__ import annotations

import csv
import hashlib
import re
from datetime import datetime
from pathlib import Path


SUBTREE_NAME = "ns-practice-ta-grading-2026s"
DEFAULT_TARGET = Path("/home/jnclaw/every_on_git_jnclaw/ns-practice-ta-grading-2026s")
TODAY = datetime.now().strftime("%Y-%m-%d")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str, apply: bool) -> None:
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str], apply: bool) -> None:
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def iter_files(root: Path, include_git: bool = False) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not include_git and ".git" in path.parts:
            continue
        if path.is_file():
            files.append(path)
    return files


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def sha256_short(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()[:16]


def is_raw_or_bulky(rel_path: str) -> bool:
    return bool(
        re.match(r"^(submissions|course_materials)/[^/]+/(raw|renamed|extracted)/", rel_path)
    )


def is_private_audit(rel_path: str) -> bool:
    private_patterns = [
        r"^submissions/[^/]+/(rename_map|student_file_map)\.csv$",
        r"^grading/[^/]+/(scores|evidence|deduction_log)\.csv$",
        r"^grading/[^/]+/student_notes/",
        r"^grading/[^/]+/feedback/",
        r"^grading/[^/]+/review_notes/",
        r"^ta_notes/",
    ]
    return any(re.match(pattern, rel_path) for pattern in private_patterns)


def category_for(rel_path: str) -> str:
    if rel_path.startswith(".git/"):
        return "git_history"
    if is_raw_or_bulky(rel_path):
        return "raw_or_bulky_private_data"
    if is_private_audit(rel_path):
        return "private_audit_metadata"
    if rel_path.startswith("docs/"):
        return "policy_or_rubric_doc"
    if rel_path.startswith("scripts/"):
        return "automation_script"
    if rel_path.startswith("templates/"):
        return "template"
    if rel_path.startswith("reports/"):
        return "audit_report"
    if rel_path.startswith("course_materials/"):
        return "course_material_metadata"
    if rel_path.startswith("migration_reports/") or rel_path == "README_migration.md":
        return "migration_artifact"
    return "repo_metadata_or_index"


def sensitivity_for(rel_path: str) -> str:
    if is_raw_or_bulky(rel_path):
        return "sensitive_unversioned"
    if is_private_audit(rel_path):
        return "sensitive_versioned_private_repo"
    if rel_path.startswith("course_materials/"):
        return "course_material_private_or_license_bound"
    return "public_safe_within_private_repo"


def planned_action_for(rel_path: str) -> str:
    if is_raw_or_bulky(rel_path):
        return "copy_first_verify_later_keep_ignored"
    if rel_path == "README.md" or rel_path.startswith("docs/"):
        return "copy_to_new_repo_leave_compatibility_stub_if_referenced"
    if is_private_audit(rel_path):
        return "copy_and_version_in_private_repo"
    return "copy_directly"


def suggested_target_path(old_text: str, target_root: Path = DEFAULT_TARGET) -> str:
    if SUBTREE_NAME not in old_text:
        return ""
    rest = old_text.split(SUBTREE_NAME, 1)[1].lstrip("/")
    rest = rest.rstrip("`.,);")
    legacy_map = {
        "docs/hw5-rubric.md": "docs/hw5_rubric.md",
        "docs/hw6-rubric.md": "docs/hw6_rubric.md",
        "docs/grading-policy.md": "docs/grading_policy.md",
    }
    rest = legacy_map.get(rest, rest)
    return str(target_root / rest) if rest else str(target_root)


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell.replace("\n", " ") for cell in row) + " |")
    return "\n".join(lines)

