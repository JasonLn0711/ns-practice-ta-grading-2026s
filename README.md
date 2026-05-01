<p align="left">
  <a href="https://github.com/JasonLn0711/ns-practice-ta-grading-2026s">
    <img alt="GitHub repository" src="https://img.shields.io/badge/GitHub-Private_TA_Grading-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <img alt="Audit ready" src="https://img.shields.io/badge/Audit_Ready-Evidence_First-0B6E4F?style=for-the-badge&logo=readthedocs&logoColor=white">
  <img alt="Python utilities" src="https://img.shields.io/badge/Python_3-Standard_Library-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Markdown workspace" src="https://img.shields.io/badge/Markdown-Plain_Text-000000?style=for-the-badge&logo=markdown&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-All_Rights_Reserved-B42318?style=for-the-badge&logo=creativecommons&logoColor=white">
</p>

# NS Practice TA Grading 2026 Spring

Private, auditable grading workspace for Jason's 2026 Spring deep-learning TA
work on HW5 and HW6.

## Purpose

This repo exists to make grading explainable later. It keeps the operational
record for scores, evidence, deductions, feedback notes, workbook write-back,
and instructor-facing reports.

The README is intentionally only an entrypoint. Detailed rules live in `docs/`,
machine-readable grading records live in `grading/`, and generated summaries
live in `reports/`.

## First Principles

- No score without evidence.
- No deduction without a written reason.
- No full credit for a missing or unverifiable required item.
- Grade requirement fulfillment, not effort or confidence.
- Separate objective file checks from manual grading judgment.
- Keep HW6 code and figure scores independent.
- Use manual-review notes for suspicious similarity; do not decide plagiarism
  without instructor confirmation.
- Keep raw submissions and bulky course files out of Git.

## Current Scope

| Area | Canonical record |
| --- | --- |
| Course context | `docs/course-context.md` |
| General grading policy | `docs/grading_policy.md` |
| HW5 requirements | `docs/hw5_assignment_requirements.md` |
| HW5 rubric | `docs/hw5_rubric.md` |
| HW6 requirements | `docs/hw6_assignment_requirements.md` |
| HW6 dual-score policy | `docs/hw6_grading_policy.md` |
| HW6 code rubric | `docs/hw6_code_rubric.md` |
| HW6 figure rubric | `docs/hw6_figure_rubric.md` |
| HW6 cross-deduction rules | `docs/hw6_cross_rules.md` |
| Evidence levels | `docs/evidence_levels.md`, `docs/hw6_evidence_levels.md` |
| Versioning and privacy | `docs/versioning_policy.md` |

HW6 is graded as two separate 100-point scores:

- `HW6(code)`: implementation, graph-to-code alignment, training method,
  accuracy evidence, and code auditability.
- `HW6(圖)`: computational graph, learned filters, intermediate feature maps,
  labels/captions, and figure auditability.

## Repo Map

| Path | Purpose | Git policy |
| --- | --- | --- |
| `docs/` | Policies, rubrics, evidence rules, assignment facts | versioned |
| `scripts/` | Safe helper scripts for import, validation, reports, workbook output | versioned |
| `templates/` | Feedback, manual-review, and grading-note templates | versioned |
| `grading/` | Score CSVs, deduction logs, per-student notes, feedback | versioned |
| `reports/` | Audit reports, release checks, instructor packets | versioned |
| `migration_reports/` | Standalone-repo migration records | versioned |
| `ta_notes/` | TA operating notes and attendance notes | versioned |
| `submissions/*/raw/` | Original LMS/E3 exports | ignored except `.gitkeep` |
| `submissions/*/renamed/` | Stable working copies of submissions | ignored except `.gitkeep` |
| `submissions/*/extracted/` | Extracted archives for review | ignored except `.gitkeep` |
| `course_materials/*/raw/` | Original course/reference files | ignored except `.gitkeep` |
| `course_materials/*/renamed/` | Renamed course/reference binaries | ignored except `.gitkeep` |
| `release_packets/` | Local generated handoff bundles | ignored |

## Grading Workflow

1. Place raw exports under `submissions/<hw>/raw/`.
2. Keep raw files unchanged.
3. Import or rename submissions to create stable working names and mapping CSVs.
4. Extract archives only into `submissions/<hw>/extracted/`.
5. Run structure and evidence checks before manual scoring.
6. Grade with the rubric and record every deduction.
7. Validate score CSVs, deduction logs, and per-student notes.
8. Build audit reports before releasing or writing grades to a workbook.

## Common Commands

Inspect and prepare submissions:

```bash
python3 scripts/import_e3_submissions.py --homework hw5
python3 scripts/rename_submissions.py --homework hw5
python3 scripts/unpack_archives.py --homework hw5
python3 scripts/check_submission_structure.py --homework hw5
python3 scripts/extract_basic_evidence.py --homework hw5
```

Validate and report HW5:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/generate_student_feedback.py --homework hw5
python3 scripts/summarize_scores.py --homework hw5
python3 scripts/build_audit_report.py --homework hw5
```

Regenerate and validate HW6 dual-score records:

```bash
python3 scripts/rebuild_hw6_dual_grading.py
python3 scripts/validate_hw6_dual_grading.py
python3 scripts/build_hw6_dual_reports.py
```

Write scores to a workbook copy only:

```bash
python3 scripts/write_hw5_hw6_scores_to_workbook.py --dry-run
python3 scripts/write_hw5_hw6_scores_to_workbook.py --apply
```

Do not overwrite original workbooks. Workbook binaries and scored workbook
copies are local working artifacts, not versioned source records.

## Release Gate

Before releasing scores or sending materials to the instructor:

- Confirm the rubric version used for every student.
- Review every `manual_review_needed=yes` row.
- Resolve or explicitly document instructor-confirmation TODOs.
- Confirm every non-full category has a deduction tag and written reason.
- Confirm per-student notes exist for graded rows.
- Review `reports/release_readiness_review.md` and the relevant HW audit report.
- Run `git status --short --ignored` and confirm ignored raw/binary files are
  not staged.

## Privacy And License

This is a private grading workspace. It may contain student identifiers, grades,
deduction notes, workbook-derived metadata, and course-context records. See
`LICENSE` and `docs/versioning_policy.md`.

In short:

- raw submissions and bulky course binaries stay out of Git;
- score CSVs, evidence summaries, deduction logs, reports, and grading notes are
  versioned because auditability depends on them;
- nothing here should be published publicly;
- do not push to any remote unless it is confirmed private and authorized by the
  course owner or instructor.

## Remote

A GitHub remote may be configured for convenience, but this repo should be
treated as private by default. Before pushing, read `docs/remote_setup.md` and
confirm the remote privacy setting.
