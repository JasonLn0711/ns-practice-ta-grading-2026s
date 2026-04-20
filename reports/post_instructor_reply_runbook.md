# Post-Instructor Reply Runbook

Generated: `2026-04-20`
Prepared by: `Jason`
Status: `waiting for instructor reply`

## Purpose

Use this runbook after the instructor replies to the HW5/HW6 policy confirmation
email. The goal is to avoid ad hoc score changes: record the decision, apply
only the required changes, re-run validation, then freeze the release state.

## Inputs

Required:

- instructor reply or meeting note
- `reports/release_decision_log.md`
- `reports/instructor_policy_confirmation_packet.md`
- `reports/instructor_confirmation_outbox.md`

Useful supporting files:

- `reports/hw5_instructor_report.md`
- `reports/hw6_instructor_report.md`
- `reports/hw6_master_audit_report.md`
- `grading/hw5/scores.csv`
- `grading/hw6/code_scores.csv`
- `grading/hw6/figure_scores.csv`
- `grading/hw6/combined_summary.csv`

## Step 1 - Capture The Reply

Copy the instructor reply into `reports/release_decision_log.md` as a dated
entry. Include:

- date received
- instructor/source
- whether the current policy is approved
- any changed policy interpretation
- late-policy decision
- any rows or patterns that must be adjusted

Do not change scores yet.

## Step 2 - Classify The Reply

Choose exactly one path first:

| Path | Meaning | Score changes? |
| --- | --- | --- |
| `approval_without_changes` | Instructor approves current policy and no late penalty is needed. | no |
| `approval_with_late_policy` | Instructor approves rubric but gives a late-policy rule. | yes, if late data exists |
| `policy_change_required` | Instructor changes one or more HW5/HW6 grading interpretations. | yes, targeted rows only |
| `needs_more_evidence` | Instructor asks to inspect details before deciding. | no immediate score change |

If the reply is ambiguous, record it as `needs_more_evidence` and ask one
follow-up question rather than guessing.

## Step 3A - Approval Without Changes

Use this path when the instructor approves the current policy and no late policy
adjustment is required.

1. Mark all pending decisions in `reports/release_decision_log.md` as approved.
2. Add a change-ledger entry: "Instructor approved current policy; no score
   changes."
3. Re-run validation:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/validate_hw6_dual_grading.py
python3 scripts/build_hw6_dual_reports.py
python3 -m py_compile scripts/*.py
git diff --check
```

4. Generate final HW5 student-facing feedback:

```bash
python3 scripts/generate_student_feedback.py --homework hw5 --apply
```

5. Keep HW6 feedback in `grading/hw6/feedback/`.
6. Commit the release state:

```bash
git status --short
git add reports/release_decision_log.md grading/hw5/feedback reports grading/hw5 grading/hw6
git commit -m "chore: finalize HW5 HW6 grading release after approval"
```

Review the staged diff before committing. Do not stage raw submissions,
extracted archives, or workbook binaries.

## Step 3B - Approval With Late Policy

Use this path when the instructor approves the rubric but provides a late
penalty or grace rule.

1. Record the exact late-policy rule in `reports/release_decision_log.md`.
2. Confirm the official late-submission source before changing scores.
3. Apply late penalties only where the official source supports them.
4. For each adjusted student, update:
   - score CSV row
   - deduction log or adjustment note
   - per-student note
   - instructor report summary
5. Re-run validation and reports.
6. Commit with a message that names the policy:

```bash
git commit -m "chore: apply instructor late policy to grading release"
```

TODO: the exact late-policy formula is not currently known and must come from
the instructor or official course policy.

## Step 3C - Policy Change Required

Use this path when the instructor changes one of the pending interpretations.

Only adjust rows affected by that decision. Do not reopen all students.

| Decision ID | Likely affected rows or files |
| --- | --- |
| `HW5-D1` | all HW5 rows if notebooks must be rerun |
| `HW5-D2` | rows with `NO_HYPERPARAMETER_SEARCH_EVIDENCE` or `WEAK_AUDIT_EVIDENCE` |
| `HW5-D3` | rows with `TEST_PIPELINE_UNCLEAR` |
| `HW5-D4` | rows with weak or alternate evidence formats |
| `HW5-D5` | rows affected by official late data |
| `HW6-D1` | `314264024`, `514661019`, and graph-format deduction rows |
| `HW6-D2` | `314264011` and architecture-deduction rows |
| `HW6-D3` | PyTorch-based submissions if the instructor rejects framework parity |
| `HW6-D4` | `314264029` |
| `HW6-D5` | rows affected by official late data |

For every changed score:

- write the policy reason in the student note
- update the relevant score CSV
- update the relevant deduction log or add an adjustment note
- regenerate summary reports
- record the changed rows in `reports/release_decision_log.md`

Validation commands:

```bash
python3 scripts/validate_grading_records.py --homework hw5
python3 scripts/validate_hw6_dual_grading.py
python3 scripts/summarize_scores.py --homework hw5
python3 scripts/build_hw6_dual_reports.py
python3 -m py_compile scripts/*.py
git diff --check
```

Commit policy changes separately:

```bash
git commit -m "chore: apply instructor grading policy adjustments"
```

## Step 3D - Needs More Evidence

Use this path when the instructor asks for student-level evidence or wants to
inspect a specific case.

Send the smallest sufficient evidence set:

1. instructor reports and policy packet first
2. score CSVs and deduction logs second
3. per-student notes for named students only
4. raw submissions only if explicitly requested and shared through an
   appropriate secure channel

Record what was sent in `reports/release_decision_log.md`.

## Step 4 - Final Freeze Checklist

Before release or LMS import:

- [ ] All pending decisions in `reports/release_decision_log.md` are resolved.
- [ ] Late policy is either applied or explicitly marked not applicable.
- [ ] HW5 validation passes.
- [ ] HW6 dual-score validation passes.
- [ ] Reports reflect any changes.
- [ ] Student-facing feedback has been generated only after policy confirmation.
- [ ] The scored workbook copy is current if HW6 scores changed.
- [ ] Raw submissions, renamed submissions, extracted archives, and workbook
  binaries are not staged.
- [ ] Final release commit exists in the private grading repo.

## Output State After Completion

The release is ready when these are true:

- `reports/release_decision_log.md` records the instructor decision.
- `grading/hw5/scores.csv` and HW5 feedback are final.
- `grading/hw6/code_scores.csv`, `grading/hw6/figure_scores.csv`, and
  `grading/hw6/combined_summary.csv` are final.
- `reports/hw6_workbook_writeback_report.md` matches the current workbook copy.
- `git status --short` is clean except intentionally ignored local workbook
  output files.
