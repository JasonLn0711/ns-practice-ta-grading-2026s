# Instructor Email Draft

Generated: `2026-04-20`
Prepared by: `Jason`
Status: `draft / not sent`

## Suggested Subject

`BEBN20024 HW5/HW6 grading completed - policy confirmation needed before release`

## Suggested Email Body

Dear Professor,

I have completed the HW5 and HW6 grading records under a consistent evidence-based
rubric. Before releasing scores or student-facing feedback, I would like to
confirm a few policy points that could affect the final release.

Current grading status:

| Homework | Graded submissions | Average | Min | Max | Manual review holds |
| --- | ---: | ---: | ---: | ---: | ---: |
| HW5 | 21 | 90.76 | 63 | 100 | 0 |
| HW6 | 21 | 89.43 | 59 | 100 | 0 |

The grading policy I used was:

- grade submitted evidence rather than unsupported claims;
- do not give full credit for required items that are missing or unverifiable;
- do not let target accuracy alone override missing development, architecture,
  graph, or visualization evidence;
- record every deduction with a written reason;
- keep per-student notes, evidence logs, score rows, and deduction logs for audit;
- mark suspicious copying for manual review rather than deciding guilt
  automatically. No manual review holds are currently recorded.

Could you please confirm the following before I generate final feedback or import
scores?

HW5:

1. Should HW5 be graded from submitted evidence only, or should TAs rerun notebooks before release?
2. If a student reaches `98%` accuracy but has weak or missing hyperparameter-search evidence, should the current requirement/evidence deductions remain?
3. How strict should we be when the official MNIST test set is tuned on, split, or partially used as validation data?
4. Which evidence formats should be accepted for full credit: notebook outputs, scripts, PDF reports, screenshots, or combinations?
5. Is there any late-policy adjustment to apply before LMS import?

HW6:

1. What computational graph formats should receive full graph credit?
2. Does "replace the fully connected layer with 2 more hidden layers" mean three hidden fully connected layers total after convolution/pooling, or two hidden layers total?
3. Should PyTorch implementations receive full credit when architecture, momentum, graph, result, and visualization evidence are present?
4. Should dense non-CNN submissions receive full architecture/filter/feature-map credit if they reach `98%` accuracy?
5. Is there any late-policy adjustment to apply before LMS import?

My default recommendation is to keep the current grading policy unless you want
a different interpretation. If you approve the current policy, I will freeze the
score CSVs, generate student-facing feedback, and prepare the LMS release.

I can also provide the instructor reports, score CSVs, deduction logs, or
student-level notes if you would like to inspect any specific cases.

Best,
Jason

## Optional Short Reply Prompt

If useful, the instructor can reply in this compact format:

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

## Send Notes

- Do not attach raw submissions, renamed submissions, extracted archives, or bulky course files.
- If attaching files, prefer the instructor reports and policy packet first.
- Attach score CSVs or deduction logs only if the instructor asks for detailed audit evidence.
- After sending, record date, recipient, and any reply in `reports/release_decision_log.md`.
