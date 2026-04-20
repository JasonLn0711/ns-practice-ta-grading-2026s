# HW5 Deduction Dictionary

Use these tags in score rows, deduction logs, student notes, and feedback.

| Tag | Description | Typical Deduction | Manual Review | Required Note Format |
| --- | --- | ---: | --- | --- |
| `MISSING_REQUIRED_FILE` | Required code/notebook/result artifact is missing. | 5-40 | yes if core file is absent | `Missing <file/evidence>; affected category: <category>.` |
| `CANNOT_VERIFY_RESULT` | Accuracy/result claim cannot be connected to code/output. | 5-20 | yes if score impact is unclear | `Claimed result <value/unknown> cannot be verified from <evidence>.` |
| `ACCURACY_BELOW_TARGET` | MNIST test accuracy is below `98%`. | 3-15 | yes if near threshold | `Reported MNIST test accuracy <value> is below 98%.` |
| `NO_HYPERPARAMETER_SEARCH_EVIDENCE` | Hyperparameter choices are missing or not visibly determined. | 4-20 | no | `Missing/weak evidence for <hidden nodes/lr/batch/epoch/search>.` |
| `CODE_INCOMPLETE` | Code is partial, broken, or lacks key HW5 implementation. | 5-30 | yes if intent is ambiguous | `Code incomplete because <observable issue>.` |
| `TEST_PIPELINE_UNCLEAR` | Train/test distinction or MNIST test evaluation is unclear. | 3-15 | yes if result credit depends on it | `Test pipeline unclear: <observable issue>.` |
| `POSSIBLE_COPYING_MANUAL_REVIEW` | Similarity or duplication concern requires instructor review. | 0 pending decision | yes | `Manual review: observed similarity in <files/sections>; no accusation made.` |

## Notes

- Deduction ranges are guides; apply the rubric category cap first.
- Do not stack multiple tags for the same root cause unless they affect distinct
  rubric categories.
- Confirm academic-integrity outcomes with the instructor before assigning an
  integrity penalty.
