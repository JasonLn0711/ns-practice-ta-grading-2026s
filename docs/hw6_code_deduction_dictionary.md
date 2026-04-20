# HW6(code) Deduction Dictionary

Use these tags in `grading/hw6/code_scores.csv`, `grading/hw6/code_deduction_log.csv`, and per-student feedback notes. Every non-full code category must have a written reason tied to one or more tags.

| Tag | Precise description | Affected item / typical impact | Manual review | Required note format |
| --- | --- | --- | --- | --- |
| `CODE_ARCH_REPLACEMENT_INCOMPLETE` | The original fully connected layer replacement or required `2 more hidden layers` is incomplete, not used, or not the requested topology. | Code-1, typically `3-15` points | if architecture intent or policy is ambiguous | `Architecture issue: <observable mismatch>; evidence: <file/cell>.` |
| `CODE_FORWARD_INCOMPLETE` | Forward pass is absent, partial, disconnected from the added layers, or not traceable from flatten/features to output. | Code-1B, typically `2-8` points | if hidden layers may be used indirectly | `Forward issue: <observable gap>; evidence: <file/cell>.` |
| `CODE_BACKPROP_INCOMPLETE` | Backward/gradient flow does not cover the added hidden layers or cannot be verified. | Code-1C, typically `1-7` points | if autograd/manual gradient evidence is unclear | `Backward issue: <observable gap>; evidence: <file/cell>.` |
| `CODE_GRAPH_NOTATION_MISMATCH` | Graph notation, layer names, or variables cannot be mapped to code. | Code-2A, typically `2-8` points | if mismatch changes score interpretation | `Notation mismatch: <observable mismatch>; evidence: <graph/code>.` |
| `CODE_FORWARD_GRAPH_MISMATCH` | Graph forward flow and code forward flow do not match. | Code-2B, typically `2-6` points | if graph/code mismatch affects architecture scoring | `Forward graph mismatch: <observable mismatch>; evidence: <graph/code>.` |
| `CODE_BACKWARD_GRAPH_MISMATCH` | Graph backward relationships and code backward/update logic do not match. | Code-2C, typically `2-6` points | if backward evidence is policy-sensitive | `Backward graph mismatch: <observable mismatch>; evidence: <graph/code>.` |
| `CODE_MINIBATCH_MISSING` | Mini-batch stochastic training is missing, fake, or unverifiable. | Code-3A, typically `2-8` points | if batch logic is hidden/ambiguous | `Mini-batch issue: <observable issue>; evidence: <file/cell>.` |
| `CODE_MOMENTUM_MISSING` | Momentum state/accumulation is absent, only claimed, or replaced with an unapproved optimizer. | Code-3B, typically `3-10` points | if optimizer interpretation is unclear | `Momentum issue: <observable issue>; evidence: <file/cell>.` |
| `CODE_UPDATE_RULE_UNCLEAR` | Parameter update rule is missing, wrong direction, inconsistent, or not tied to model parameters. | Code-3C, typically `1-7` points | if score depends on update interpretation | `Update rule unclear: <observable issue>; evidence: <file/cell>.` |
| `CODE_ACCURACY_BELOW_TARGET` | Credible MNIST test accuracy is below `98%`. | Code-4, according to accuracy band | if near threshold or conflicting outputs | `Accuracy <value/band> below target; evidence: <output/log>.` |
| `CODE_RESULT_BAND_BELOW_FULL` | Credible MNIST test accuracy reaches `98%` but is below the full-credit `98.50%` band. | Code-4, `1-3` points | no unless values conflict | `Accuracy band <band> earns <score>/20; evidence: <output/log>.` |
| `CODE_RESULT_NOT_VERIFIABLE` | Claimed accuracy/result is not traceable to submitted code, test data, or model. | Code-4/5, typically `5-20` points | yes if result credit depends on it | `Result not verifiable: <claim>; missing evidence: <what>.` |
| `CODE_TEST_PIPELINE_UNCLEAR` | Train/test distinction, MNIST test split, or evaluation procedure is unclear. | Code-4/5, typically `2-10` points | if result credit depends on it | `Test pipeline unclear: <observable issue>; evidence: <file/cell>.` |
| `CODE_INCOMPLETE` | Code is missing, broken, screenshot-only, or too incomplete to support grading. | Any code category, up to `100` points | yes if core file is absent | `Code incomplete: <observable issue>; evidence: <file/path>.` |
| `CODE_POSSIBLE_COPYING_MANUAL_REVIEW` | Similarity or suspicious duplication requires instructor review. This tag records concern only; it is not an accusation. | Manual review; no automatic penalty | yes | `Manual review: similar code in <students/files>; no accusation made.` |

Rubric point allocations are controlling; deduction ranges are guides for consistent written reasoning.
