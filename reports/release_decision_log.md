# Release Decision Log

Generated: `2026-04-20`
Prepared by: `Jason`
Status: `pending instructor confirmation`

## Purpose

This log records instructor decisions that affect grade release. It exists so a
future TA or the instructor can understand why any post-grading score adjustment
was or was not made.

## Rules

- Do not release student-facing feedback until the pending decisions below are resolved.
- Do not change scores without a recorded policy decision or concrete correction reason.
- If a score changes, update the score row, student note, and deduction log or adjustment note.
- Adjust only affected rows; do not reopen unrelated students for custom exceptions.
- Keep raw submissions and bulky files out of Git; keep score/evidence/decision metadata versioned.
- Treat the generated HW6 scored workbook as a draft until instructor approval;
  the original workbook remains untouched.

## Pending Decisions

| Decision ID | Homework | Question | Current treatment | Potentially affected rows | Status | Instructor decision | Follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HW5-D1 | HW5 | Submitted evidence only, or rerun notebooks before release? | Graded from submitted evidence only. | all HW5 rows if rerun required | pending | TODO | If rerun required, define reproducible environment and rerun scope before changing scores. |
| HW5-D2 | HW5 | Should weak/missing hyperparameter-search evidence lose requirement/evidence points even when accuracy reaches target? | Keep deductions for weak or missing development evidence. | rows with `NO_HYPERPARAMETER_SEARCH_EVIDENCE` or `WEAK_AUDIT_EVIDENCE` | pending | TODO | If changed, adjust only affected rows and preserve original deduction notes. |
| HW5-D3 | HW5 | How strict should MNIST test-pipeline ambiguity be? | Apply `TEST_PIPELINE_UNCLEAR`; no automatic zero or hold. | rows with `TEST_PIPELINE_UNCLEAR` | pending | TODO | If stricter/looser, adjust only affected rows. |
| HW5-D4 | HW5 | Which evidence formats are accepted for full credit? | Accept traceable notebook/script/report evidence. | rows with weak evidence tags | pending | TODO | Update rubric note if instructor narrows/expands accepted formats. |
| HW5-D5 | HW5 | What late policy should be applied? | No late penalties applied. | all HW5 rows if late data exists | pending | TODO | Apply only after official late data is available. |
| HW6-D1 | HW6 | What graph formats receive full credit? | Full for separate/rendered aligned graph; partial for text/comment graph; zero for missing graph. | 314264024, 514661019, graph-deduction rows | pending | TODO | If text/comment graph accepted for full credit, adjust targeted rows only. |
| HW6-D2 | HW6 | Does HW6 require three hidden fully connected layers total or two hidden layers total? | Three hidden fully connected layers total after convolution/pooling. | 314264011 and architecture-deduction rows | pending | TODO | If two total is accepted, adjust targeted architecture rows only. |
| HW6-D3 | HW6 | Are PyTorch implementations accepted for full credit when evidence is complete? | Yes. | PyTorch-based submissions | pending | TODO | If not accepted, instructor must define framework penalty before any changes. |
| HW6-D4 | HW6 | Should dense non-CNN submissions receive full CNN architecture/filter/feature-map credit if accuracy reaches target? | No. | 314264029 | pending | TODO | If instructor accepts dense non-CNN, adjust architecture/visualization rows only. |
| HW6-D5 | HW6 | What late policy should be applied? | No late penalties applied. | all HW6 rows if late data exists | pending | TODO | Apply only after official late data is available. |

## Decision Record Template

Use this format when the instructor replies:

```text
Date:
Instructor/source:
Decision IDs resolved:
Decision summary:
Rows adjusted:
Files changed:
Validation run:
Commit:
Notes:
```

## Send Events

Use this section after sending the confirmation message. Do not mark decisions
approved until the instructor reply is received.

Pre-send verification:

- 2026-04-20: Syllabus text confirms lecturer `吳育德` but does not expose a
  reliable email address. The instructor packet remains ready, but sending is
  blocked until the recipient address is confirmed from E3, a prior course
  email, or the instructor directly.

```text
Date sent:
Recipient:
Subject:
Files sent or pasted:
Pending decisions:
Notes:
```

## Reply Processing

After the instructor replies, use
`reports/post_instructor_reply_runbook.md` before changing scores. Classify the
reply as one of:

- `approval_without_changes`
- `approval_with_late_policy`
- `policy_change_required`
- `needs_more_evidence`

If the reply changes policy, adjust only affected rows and preserve the original
deduction rationale in the student-level audit trail.

## Change Ledger

- 2026-04-20: HW6 was revised into independent `HW6(code)` and
  `HW6(圖)` score records. A separate local scored workbook copy was
  generated from those records, with `21` exact name matches updated and `4`
  no-evidence workbook students left unchanged. No instructor release-policy
  score changes have been applied yet.
