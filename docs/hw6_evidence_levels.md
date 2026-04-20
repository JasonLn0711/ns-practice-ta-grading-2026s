# HW6 Dual-Score Evidence Levels

Evidence level records how reliably a TA can verify the submitted work. It does
not replace rubric scoring, but it caps evidence-sensitive categories.

## Levels

| Level | Meaning | Code evidence cap | Figure explainability cap |
| --- | --- | ---: | ---: |
| A | Code, runnable-looking logic, output/logs, result evidence, and figure/code alignment are verifiable. | 10/10 | 15/15 |
| B | Code and result evidence are present, but logs, graph alignment, or visual traceability are partial. | 7/10 | 10/15 |
| C | Evidence is weak or incomplete; grading is possible but conservative. | 4/10 | 6/15 |
| D | Submission exists but cannot support reliable grading. | 2/10 | 3/15 |

## Rules

- No score without evidence.
- Unsupported claims cannot receive full result or evidence credit.
- Final screenshots without enough code evidence cap code evidence at Level C.
- Code without figure deliverables does not protect the figure score.
- Figures without working code evidence do not protect the code score.
- If graph and code do not align, cap code evidence at Level B and deduct in
  both the code and figure rubrics.
- If plagiarism or suspicious duplication is suspected, keep the score evidence
  conservative and open a manual review note without deciding guilt.

## TODO: Instructor Confirmation

- Whether TAs must rerun notebooks before final release.
- Whether screenshots are accepted as primary evidence.
- Late-policy effects on evidence and final scores.
