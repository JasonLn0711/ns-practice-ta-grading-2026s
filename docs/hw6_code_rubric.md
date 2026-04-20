# HW6(code) Rubric

Total score: `100`.

HW6(code) grades implementation, training, result evidence, and auditability. It
does not award figure credit.

## Category Breakdown

| Category | Points |
| --- | ---: |
| Architecture implementation correctness | 25 |
| Computational-graph-consistent implementation | 20 |
| Training algorithm correctness | 25 |
| Result quality | 20 |
| Evidence and auditability | 10 |

## Architecture Implementation Correctness: 25

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Replaces the original fully connected part | 8 | Original fully connected layer path is visibly replaced in the submitted model. | 4-7 for plausible but incomplete replacement. | 0 if unchanged or not inspectable. |
| Implements two additional hidden layers | 10 | Two more hidden layers are implemented and used in the forward/training path. | 6-9 for mostly correct layer count with minor ambiguity; 2-5 for partial/single extra hidden layer. | 0 if missing. |
| Shape and data-flow correctness | 5 | Layer dimensions and MNIST/CNN data flow are internally consistent. | 2-4 for incomplete but plausible shape evidence. | 0 if flow cannot be verified. |
| Real implementation, not naming-only | 2 | Layers are used in computation, not only declared or named. | 1 for weak usage evidence. | 0 for superficial naming only. |

Caps:

- No code-like artifact: max `5`.
- Prose/screenshot-only architecture: max `10`.
- Dense non-CNN architecture: max `15` unless instructor accepts it.

Manual-review triggers: unreadable core code, contradictory architecture claims,
or near-identical architecture structure across submissions.

## Computational-Graph-Consistent Implementation: 20

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Variable notation maps to graph | 6 | Code variable names or comments map clearly to graph notation. | 3-5 for partial mapping. | 0 if no graph or no mapping. |
| Forward pass aligns with graph | 6 | Forward layer transitions match the graph. | 3-5 for minor mismatch. | 0 if absent or unrelated. |
| Backward/gradient relationships align | 5 | Gradient/update logic can be aligned with graph relationships. | 2-4 for incomplete alignment. | 0 if not inspectable. |
| Graph/code consistency is documented | 3 | Student submission or TA note can trace graph to code. | 1-2 for weak traceability. | 0 if no traceable link. |

Caps:

- Missing graph: category score `0`.
- Graph exists but is generic or not tied to code: max `8`.
- Graph and code disagree on architecture: max `12`.

Manual-review triggers: graph copied from another source without adaptation,
or graph/code mismatch that changes score interpretation.

## Training Algorithm Correctness: 25

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Mini-batch stochastic training | 6 | Code constructs and trains on mini-batches. | 3-5 if batching is likely but incomplete. | 0 if full-batch only or absent. |
| Momentum state/history | 8 | Update rule uses historical velocity/momentum accumulation. | 4-7 if momentum is partial or ambiguous. | 0 if only claimed or absent. |
| Parameter update correctness | 6 | Parameters are updated with the intended gradients and momentum state. | 3-5 for partial update correctness. | 0 if updates are disconnected or wrong. |
| Train/test logic | 3 | Training and test/evaluation phases are distinguishable. | 1-2 if likely but unclear. | 0 if not distinguishable. |
| Tied to submitted HW6 model | 2 | Training loop updates the model being graded. | 1 if weakly tied. | 0 if disconnected. |

Caps:

- Momentum claimed but no historical accumulation: momentum sub-item max `2/8`.
- Non-momentum optimizer such as Adam without explicit accepted policy: training
  category max `15`.
- Training loop disconnected from HW6 architecture: category max `10`.

Manual-review triggers: optimizer ambiguity, hidden external training, or
similar training code across submissions.

## Result Quality: 20

| Test accuracy evidence | Points |
| --- | ---: |
| `>= 98.00%`, traceable to submitted HW6 model and test/evaluation data | 20 |
| `97.50-97.99%`, traceable and otherwise valid | 18 |
| `97.00-97.49%`, traceable and otherwise valid | 16 |
| `95.00-96.99%`, traceable and otherwise valid | 12-15 |
| `<95.00%`, traceable partial result | 4-11 |
| Claim only, no output/log/screenshot | max 6 |
| No result evidence | 0 |

Caps:

- Train/test distinction unclear: max `15`.
- Result not tied to submitted model: max `8`.
- Result produced by a different architecture: max `10`.

Manual-review triggers: suspicious result formatting, implausible output without
logs, or conflicting reported accuracies.

## Evidence and Auditability: 10

| Item | Points | Full credit | Partial credit | Zero credit |
| --- | ---: | --- | --- | --- |
| Code/result traceability | 3 | Code, training, and result can be traced by file/cell/output. | 1-2 for partial traceability. | 0 if disconnected. |
| Logs or notebook outputs retained | 2 | Logs/outputs support implementation and result. | 1 for weak outputs. | 0 if absent. |
| Graph/code traceability | 2 | Graph-to-code connection is auditable. | 1 for weak connection. | 0 if missing. |
| Deduction traceability | 2 | Every lost point has a tag and written reason. | 1 if incomplete. | 0 if missing. |
| Per-student note exists | 1 | Dual-score note records evidence and final score. | 0.5 if thin. | 0 if missing. |

Evidence caps are defined in `docs/hw6_evidence_levels.md`.
