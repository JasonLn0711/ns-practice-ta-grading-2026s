# HW6 Cross-Deduction Rules

These rules keep `HW6(code)` and `HW6(圖)` independent while preventing inconsistent evidence from receiving unearned full credit.

## Rule 1: graph and code mismatch deducts both sides

If the computational graph and code do not match:

- deduct on the code side under Code-2 `Graph-to-code 一致性`
- deduct on the figure side under Figure-1 `Computational graph 正確性與完整性`
- record the reason with `CODE_GRAPH_NOTATION_MISMATCH`, `CODE_FORWARD_GRAPH_MISMATCH`, `CODE_BACKWARD_GRAPH_MISMATCH`, or `FIG_GRAPH_CODE_MISMATCH`

## Rule 2: high accuracy does not guarantee high code score

If a student achieves `>= 98%` accuracy but the required architecture change is incomplete, momentum is missing, or graph-to-code alignment cannot be verified:

- award result points according to the accuracy band only if the result is credible
- do not award full architecture, graph-to-code, or training-method points
- record the exact missing requirement in the deduction log

## Rule 3: polished figures do not guarantee high figure score

If figures are visually polished but are not actually learned filters, true intermediate feature maps, or a usable computational graph:

- deduct under the relevant figure category
- cap figure evidence/auditability if source traceability is weak
- do not use visual polish to replace missing deliverables

## Rule 4: no evidence means no full credit

Missing or unverifiable evidence cannot receive full credit. Unsupported claims must be capped or scored zero according to `docs/hw6_evidence_levels.md`.

## Rule 5: manual review is not automatic guilt

If possible copying or suspicious duplication is observed:

- create a manual-review note
- use the appropriate `*_POSSIBLE_COPYING_MANUAL_REVIEW` tag
- do not decide academic-integrity guilt or penalties without instructor review

