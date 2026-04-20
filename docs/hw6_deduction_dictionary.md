# HW6 Deduction Dictionary

Use these tags in score rows, deduction logs, student notes, and feedback.

| Tag | Description | Typical Deduction | Manual Review | Required Note Format |
| --- | --- | ---: | --- | --- |
| `MISSING_REQUIRED_FILE` | Required code/notebook/graph/result/plot artifact is missing. | 5-40 | yes if core file is absent | `Missing <file/evidence>; affected category: <category>.` |
| `CANNOT_VERIFY_RESULT` | Accuracy/result claim cannot be connected to code/output. | 5-15 | yes if score impact is unclear | `Claimed result <value/unknown> cannot be verified from <evidence>.` |
| `ACCURACY_BELOW_TARGET` | MNIST test accuracy is below `98%`. | 3-10 | yes if near threshold | `Reported MNIST test accuracy <value> is below 98%.` |
| `COMPUTATIONAL_GRAPH_MISSING` | Required computational graph is absent. | 8-15 | no unless format dispute exists | `Computational graph missing from <files reviewed>.` |
| `MOMENTUM_NOT_IMPLEMENTED` | Momentum is missing or only mentioned without implementation. | 5-20 | yes if implementation is ambiguous | `Momentum evidence insufficient: <observable issue>.` |
| `FILTER_PLOT_MISSING` | Learned filter plot is absent or not identifiable. | 4-7 | no unless embedded output is unclear | `Learned filter plot missing/unclear in <files reviewed>.` |
| `FEATURE_MAP_MISSING` | Intermediate feature-map plot is absent or not identifiable. | 4-7 | no unless embedded output is unclear | `Feature-map plot missing/unclear in <files reviewed>.` |
| `CODE_INCOMPLETE` | Code is partial, broken, or lacks key HW6 implementation. | 5-30 | yes if intent is ambiguous | `Code incomplete because <observable issue>.` |
| `TEST_PIPELINE_UNCLEAR` | Train/test distinction or MNIST test evaluation is unclear. | 3-10 | yes if result credit depends on it | `Test pipeline unclear: <observable issue>.` |
| `POSSIBLE_COPYING_MANUAL_REVIEW` | Similarity or duplication concern requires instructor review. | 0 pending decision | yes | `Manual review: observed similarity in <files/sections>; no accusation made.` |

## Notes

- Deduction ranges are guides; apply the rubric category cap first.
- Deduct graph, training, and visualization issues separately only when they are
  independently observable.
- Confirm academic-integrity outcomes with the instructor before assigning an
  integrity penalty.
