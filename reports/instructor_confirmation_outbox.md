# Instructor Confirmation Outbox

Generated: `2026-04-20`
Prepared by: `Jason`
Status: `ready to paste / not sent`

## Purpose

This is the copy-pasteable outgoing message for instructor policy confirmation.
It is intentionally limited to summary and policy questions. Do not include raw
submissions, extracted archives, or workbook binaries unless the instructor asks
for them through an appropriate channel.

## Recipient

吳育德老師 <ytwu@nycu.edu.tw>

Local source check: Gmail search found prior messages from `吳 (Wu)育德
(Yu-Te) <ytwu@nycu.edu.tw>`, and the inspected E3 course announcement confirms
the course lecturer context as `吳育德`.

## Subject

```text
BEBN20024 HW5/HW6 grading completed - policy confirmation needed before release
```

## Email Body

```text
Dear Professor,

I have completed the HW5 and HW6 grading records under a consistent evidence-based rubric. Before releasing scores or student-facing feedback, I would like to confirm a few policy points that could affect the final release.

Current grading status:

- HW5: 21 graded submissions, average 90.76, manual review holds 0
- HW6(code): 21 graded submissions, average 88.38, manual review holds 0
- HW6(圖): 21 graded submissions, average 78.38, manual review holds 0

The grading policy I used was:

- grade submitted evidence rather than unsupported claims;
- do not give full credit for required items that are missing or unverifiable;
- do not let target accuracy alone override missing development, architecture, graph, or visualization evidence;
- record every deduction with a written reason;
- keep per-student notes, evidence logs, score rows, and deduction logs for audit;
- mark suspicious copying for manual review rather than deciding guilt automatically. No manual review holds are currently recorded.

Could you please confirm the following before I generate final feedback or import scores?

HW5:

1. Should HW5 be graded from submitted evidence only, or should TAs rerun notebooks before release?
2. If a student reaches 98% accuracy but has weak or missing hyperparameter-search evidence, should the current requirement/evidence deductions remain?
3. How strict should we be when the official MNIST test set is tuned on, split, or partially used as validation data?
4. Which evidence formats should be accepted for full credit: notebook outputs, scripts, PDF reports, screenshots, or combinations?
5. Is there any late-policy adjustment to apply before LMS import?

HW6:

1. What computational graph formats should receive full graph credit?
2. Does "replace the fully connected layer with 2 more hidden layers" mean three hidden fully connected layers total after convolution/pooling, or two hidden layers total?
3. Should PyTorch implementations receive full credit when architecture, momentum, graph, result, and visualization evidence are present?
4. Should dense non-CNN submissions receive full architecture/filter/feature-map credit if they reach 98% accuracy?
5. Is there any late-policy adjustment to apply before LMS import?

My default recommendation is to keep the current grading policy unless you want a different interpretation. If you approve the current policy, I will freeze the score CSVs and use the generated workbook copy with separate HW6(圖) and HW6(code) columns for release preparation. Four workbook rows currently remain unchanged because no reliable HW6 grading evidence row exists for those students.

I can also provide the instructor reports, score CSVs, deduction logs, or student-level notes if you would like to inspect any specific cases.

Best,
Jason
```

## Default Attachments

Attach files from the sanitized local packet folder by default:

```text
release_packets/instructor_confirmation_2026-04-20/
```

The packet folder contains copies of these summary/policy files, or you can
paste the policy packet inline:

| File | Purpose |
| --- | --- |
| `reports/instructor_policy_confirmation_packet.md` | policy questions and current TA treatment |
| `reports/hw5_instructor_report.md` | HW5 instructor summary |
| `reports/hw6_instructor_report.md` | HW6 dual-score instructor summary |
| `reports/hw6_master_audit_report.md` | HW6 audit summary and workbook write-back status |

Optional supporting files if the instructor wants more detail:

| File | Purpose |
| --- | --- |
| `reports/hw6_code_audit_report.md` | HW6(code) category and deduction detail |
| `reports/hw6_figure_audit_report.md` | HW6(圖) category and deduction detail |
| `reports/hw6_workbook_writeback_report.md` | workbook copy/write-back summary |

Do not attach these by default:

| Path pattern | Reason |
| --- | --- |
| `submissions/*/raw/` | raw student submissions |
| `submissions/*/renamed/` | renamed student submissions |
| `submissions/*/extracted/` | extracted student submissions |
| `course_materials/*/raw/` | source workbook/course materials |
| `course_materials/*/renamed/` | local workbook output copies |
| `grading/*/feedback/` | detailed per-student notes |
| `grading/*/student_notes/` | detailed per-student notes |
| `grading/*/*scores.csv` | student-level score rows |
| `grading/*/*deduction*.csv` | student-level deduction rows |

## Post-Send Log Snippet

After sending, paste this into `reports/release_decision_log.md` under a new
send event entry:

```text
Date sent: 2026-04-20
Recipient:
Subject: BEBN20024 HW5/HW6 grading completed - policy confirmation needed before release
Files sent or pasted:
- release_packets/instructor_confirmation_2026-04-20/instructor_confirmation_outbox.md
- release_packets/instructor_confirmation_2026-04-20/instructor_policy_confirmation_packet.md
- release_packets/instructor_confirmation_2026-04-20/hw5_instructor_report.md
- release_packets/instructor_confirmation_2026-04-20/hw6_instructor_report.md
- release_packets/instructor_confirmation_2026-04-20/hw6_master_audit_report.md
Pending decisions: HW5-D1 through HW5-D5, HW6-D1 through HW6-D5
Notes: Waiting for instructor policy confirmation before student-facing release or LMS import.
```

## Reply Shortcut

The shortest useful instructor reply is:

```text
I approve the current TA grading policy for HW5/HW6 as described, with these changes:

HW5:
- rerun notebooks? yes/no
- weak hyperparameter-search evidence: keep deductions / adjust
- MNIST test-pipeline ambiguity: keep deductions / adjust
- accepted evidence formats:
- late policy:

HW6:
- accepted graph formats:
- hidden-layer interpretation:
- PyTorch accepted for full credit? yes/no
- dense non-CNN treatment:
- late policy:
```
