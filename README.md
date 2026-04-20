# NS Practice TA Grading 2026 Spring

Standalone local Git repo for Jason's HW5/HW6 TA grading work.

## Purpose

This workspace makes grading quantitative, consistent, and auditable. Scores are
not based on vague impression. Each non-full score should trace to:

- a rubric category
- an evidence level
- one or more deduction tags
- a written reason
- a score row and, when needed, a per-student note

## Core Workflow

1. Put raw LMS/E3 exports in `submissions/<hw>/raw/`.
2. Keep raw files untouched.
3. Use `scripts/import_e3_submissions.py` or `scripts/rename_submissions.py` to
   create stable working names and mapping CSVs.
4. Extract archives only when needed with `scripts/unpack_archives.py`.
5. Run objective checks with `scripts/check_submission_structure.py`.
6. Extract basic evidence with `scripts/extract_basic_evidence.py`.
7. Grade manually with the HW-specific rubric.
8. Record scores in `grading/<hw>/scores.csv`.
9. Record deductions in `grading/<hw>/deduction_log.csv`.
10. Update the per-student note in `grading/<hw>/student_notes/`.
11. Run `scripts/validate_grading_records.py`.
12. Build audit and instructor reports with `scripts/build_audit_report.py`.
13. Review `reports/release_readiness_review.md` before releasing scores.
14. Generate student-facing feedback only after instructor policy questions are resolved.

## Where Things Go

| Need | Location | Git policy |
| --- | --- | --- |
| Raw submissions | `submissions/<hw>/raw/` | ignored |
| Renamed working submissions | `submissions/<hw>/renamed/` | ignored |
| Extracted submissions | `submissions/<hw>/extracted/` | ignored |
| Submission maps | `submissions/<hw>/rename_map.csv`, `student_file_map.csv` | versioned |
| Course/reference files | `course_materials/<hw>/` | maps/docs versioned, binaries ignored |
| Score sheet | `grading/<hw>/scores.csv` | versioned |
| Evidence sheet | `grading/<hw>/evidence.csv` | versioned |
| Deduction log | `grading/<hw>/deduction_log.csv` | versioned |
| Student notes | `grading/<hw>/student_notes/` | versioned |
| Feedback | `grading/<hw>/feedback/` | versioned |
| Reports | `reports/` | versioned |
| Rubrics and policy | `docs/` | versioned |

## Rubrics

- HW5 rubric: `docs/hw5_rubric.md`
- HW6 rubric: `docs/hw6_rubric.md`
- Evidence levels: `docs/evidence_levels.md`
- Deduction dictionaries:
  - `docs/hw5_deduction_dictionary.md`
  - `docs/hw6_deduction_dictionary.md`

Unknown assignment or policy details are marked as TODO. Do not invent rules.

## Scripts

Dry-run first:

```bash
python3 scripts/rename_submissions.py --homework hw5
python3 scripts/unpack_archives.py --homework hw5
python3 scripts/check_submission_structure.py --homework hw5
python3 scripts/extract_basic_evidence.py --homework hw5
```

Apply only after reviewing the dry-run:

```bash
python3 scripts/rename_submissions.py --homework hw5 --apply
python3 scripts/unpack_archives.py --homework hw5 --apply
```

Generate outputs:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/generate_student_feedback.py --homework hw5
python3 scripts/summarize_scores.py --homework hw5
python3 scripts/build_audit_report.py --homework hw5
```

Validation enforces the grading discipline: no score without evidence metadata,
no non-full score without a written deduction reason, evidence-level caps, and a
per-student note for every graded row.

## Manual Judgment

Scripts can identify files, keywords, checksums, missing outputs, and score
summaries. Humans must decide:

- whether the implementation satisfies the assignment
- whether the result is credible and traceable
- whether graph/plot evidence matches the code
- whether partial credit is fair
- whether suspicious similarity needs instructor review

## Before Releasing Scores

- Confirm the rubric version.
- Confirm late-policy handling.
- Review every `manual_review_needed=yes` row.
- Review `reports/release_readiness_review.md` for instructor policy questions.
- Confirm no student received a custom standard.
- Ensure every deduction has a tag and reason.
- Run `scripts/validate_grading_records.py --homework hw5` and repeat for HW6.
- Build the audit and instructor reports.
- If policy changes, adjust only the affected rows and record a new commit.
- Keep raw submissions and bulky binaries out of Git.

## Remote

This repo is local-only for now. See `docs/remote_setup.md` before adding any
private remote.
