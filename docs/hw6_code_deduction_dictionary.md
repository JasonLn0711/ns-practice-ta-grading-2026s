# HW6(code) Deduction Dictionary

Use these tags in `grading/hw6/code_scores.csv`,
`grading/hw6/code_deduction_log.csv`, student notes, and feedback.

| Tag | Description | Typical impact | Manual review | Required note format |
| --- | --- | ---: | --- | --- |
| `CODE_ARCH_REPLACEMENT_INCOMPLETE` | Fully connected replacement or added hidden layers are incomplete. | 3-15 | if architecture intent is ambiguous | `Architecture issue: <observable mismatch>; evidence: <file/cell>.` |
| `CODE_GRAPH_NOTATION_MISMATCH` | Code variables, forward flow, or backward flow do not align with graph notation. | 3-20 | if mismatch changes policy interpretation | `Graph/code mismatch: <observable mismatch>; evidence: <file/cell>.` |
| `CODE_MINIBATCH_MISSING` | Mini-batch stochastic training is missing or unverifiable. | 3-10 | if evidence is ambiguous | `Mini-batch issue: <observable issue>; evidence: <file/cell>.` |
| `CODE_MOMENTUM_MISSING` | Momentum is absent or only claimed without historical accumulation. | 5-20 | if optimizer interpretation is unclear | `Momentum issue: <observable issue>; evidence: <file/cell>.` |
| `CODE_UPDATE_RULE_UNCLEAR` | Parameter update rule cannot be verified. | 3-12 | if score depends on update interpretation | `Update rule unclear: <observable issue>; evidence: <file/cell>.` |
| `CODE_ACCURACY_BELOW_TARGET` | Traceable MNIST test accuracy is below `98%`. | 1-16 | if near threshold or conflicting outputs | `Accuracy <value> below target; evidence: <output/log>.` |
| `CODE_RESULT_NOT_VERIFIABLE` | Result claim is not traceable to submitted code/output. | 5-20 | yes if result credit depends on it | `Result not verifiable: <claim>; evidence missing: <what>.` |
| `CODE_TEST_PIPELINE_UNCLEAR` | Test/evaluation pipeline is unclear. | 2-10 | if result credit depends on it | `Test pipeline unclear: <observable issue>; evidence: <file/cell>.` |
| `CODE_INCOMPLETE` | Code is missing, broken, or only screenshots/prose. | 5-100 | yes if core file is absent | `Code incomplete: <observable issue>; evidence: <file/path>.` |
| `CODE_POSSIBLE_COPYING_MANUAL_REVIEW` | Code similarity requires instructor review. | 0 pending decision | yes | `Manual review: similar code in <students/files>; no accusation made.` |

Deduction ranges are guides. The rubric category caps are controlling.
