# HW6 Dual-Score Evidence Levels

Evidence level records how reliably another TA or the instructor can verify the submitted work. It does not replace rubric scoring; it caps evidence-sensitive categories.

## Levels And Caps

| Level | Meaning | Code evidence cap | Figure evidence cap | Result score policy |
| --- | --- | ---: | ---: | --- |
| A | Code + outputs/logs + result evidence + graph/figure/code consistency can be checked. | 10/10 | 15/15 | Use the official accuracy band if tied to test data and submitted model. |
| B | Code + result evidence exist, but some traceability is missing. | 7/10 | 10/15 | Use the band only if the result is still credible; otherwise cap conservatively. |
| C | Weak or partial evidence. | 4/10 | 6/15 | Do not award full result credit; unsupported claims should receive low or zero result credit. |
| D | Submission exists but cannot support reliable grading. | 2/10 | 3/15 | Result score is normally `0` unless a credible, traceable output exists. |

## Mandatory Rules

- No full credit for any required deliverable that is missing or unverifiable.
- Unsupported claims cannot receive full result or evidence credit.
- Final screenshots without enough code evidence cap code evidence at Level C.
- Code without figure deliverables does not protect the figure score.
- Figures without working code evidence do not protect the code score.
- If graph and code do not align, cap the affected evidence-sensitive categories conservatively and deduct in both rubrics.
- If plagiarism or suspicious duplication is suspected, keep scores evidence-based and create a manual review note without deciding guilt.

## TODO: Instructor Confirmation

- Whether TAs must rerun notebooks before final release.
- Whether screenshots are accepted as primary evidence.
- Late-policy effects on evidence and final scores.
- Whether text-only/source-comment computational graphs can ever receive full figure graph credit.
