# HW6(code) 詳細評分基準

Total score: `100`.

這一份分數只評「實作是否真的完成、是否正確、是否可驗證」。不要用努力程度、敘述自信或排版美觀取代可檢查證據。

## First-principle grading rules

- No score without evidence.
- No deduction without a written reason.
- No full credit for missing or unverifiable required work.
- Grade requirement fulfillment, correctness, reproducibility, and auditability.
- If graph and code do not match, deduct in both `HW6(code)` and `HW6(圖)` according to `docs/hw6_cross_rules.md`.
- If plagiarism or suspicious duplication is suspected, create a manual-review note without deciding guilt.

## Category Breakdown

| Category | Points |
| --- | ---: |
| Code-1. 架構修改正確性 | 25 |
| Code-2. Graph-to-code 一致性 | 20 |
| Code-3. 訓練法正確性 | 25 |
| Code-4. 結果達成度 | 20 |
| Code-5. 證據與可稽核性 | 10 |

## Code-1. 架構修改正確性: 25

題目要求是把原本 red rectangle 的 fully connected layer 改成 blue rectangle 的 `2 more hidden layers`。

### 1A. 層數與拓撲是否正確: 10

| Score | Check condition |
| ---: | --- |
| 10 | 確實新增 `2` 個 hidden layers，且整體連接拓撲正確。 |
| 8 | 新增 `2` 層，但某些層之間連接不完整或 shape/data-flow 有小瑕疵。 |
| 6 | 有明顯新增層，但不是完整的 2-hidden-layer replacement。 |
| 3 | 只有局部修改，看起來接近但核心替換不成立。 |
| 0 | 未完成核心架構替換，或沒有可檢查的 code evidence。 |

Required evidence: submitted notebook/script/model definition, forward path using the layers, and layer dimensions or variable flow that can be traced.

Manual-review triggers: unreadable model code, contradictory hidden-layer claims, near-identical architecture across students, or unclear policy about whether a dense non-CNN replacement should be accepted.

### 1B. forward pass 是否與新架構一致: 8

| Score | Check condition |
| ---: | --- |
| 8 | Forward 流程完整，從 pooling 後 flatten 到多 hidden layers 再到 output，邏輯一致。 |
| 6 | 整體大致正確，但有部分變數流不清。 |
| 4 | 有 forward，但和新架構只部分一致。 |
| 2 | 有片段 code，但無法形成完整 forward。 |
| 0 | 沒有可驗證的 forward。 |

Required evidence: actual executable forward code or notebook cells showing the computation path from input/features to output logits/probabilities.

Manual-review triggers: forward path appears copied but not adapted, hidden layers declared but not used, or graph/code disagreement changes interpretation.

### 1C. backward / gradient flow 是否與新架構一致: 7

| Score | Check condition |
| ---: | --- |
| 7 | 所有新增 hidden layers 都有相對應 backward / gradient path。 |
| 5 | 大部分有，但少一層或少部分梯度。 |
| 3 | 有嘗試做 backprop，但不完整。 |
| 1 | 只有少量片段。 |
| 0 | 沒有可驗證的 backward。 |

Required evidence: gradient code, autograd-backed training loop tied to the submitted model, or manual backprop/update logic that covers the added layers.

Manual-review triggers: optimizer updates only part of the model, hidden layers are outside the gradient path, or backprop is claimed but not inspectable.

## Code-2. Graph-to-code 一致性: 20

題目不是只要畫圖，而是要 `use the notations in this graph to implement your codes`。

### 2A. notation 對應性: 8

| Score | Check condition |
| ---: | --- |
| 8 | 圖上的主要符號、層名、變數名，能在 code 中清楚對應。 |
| 6 | 大部分可對應，但命名有少量偏差。 |
| 4 | 只有部分對應。 |
| 2 | 勉強看得出關聯。 |
| 0 | 看不出圖與 code 對應，或沒有 graph evidence。 |

Required evidence: graph artifact plus code variables/comments/cell text that let another TA trace symbol-to-code correspondence.

Manual-review triggers: graph appears generic, graph belongs to a different architecture, or notation is copied without matching the submitted code.

### 2B. computational graph 的 forward 對應: 6

| Score | Check condition |
| ---: | --- |
| 6 | Graph 中的每個主要運算區塊在 code 中都可找到對應實作。 |
| 4 | 主要區塊可對應，但缺少部分細節。 |
| 2 | 只對得上一半左右。 |
| 0 | 幾乎無法對應。 |

Required evidence: graph forward nodes/edges and code forward operations covering the same model path.

Manual-review triggers: graph/code mismatch affects architecture score or makes the result evidence unreliable.

### 2C. computational graph 的 backward 對應: 6

| Score | Check condition |
| ---: | --- |
| 6 | 反向傳播在 code 中可對應到 graph 的反向關係。 |
| 4 | 主幹可對應，但細節不足。 |
| 2 | 只有局部對應。 |
| 0 | 無法對應。 |

Required evidence: graph backward/gradient relationships plus code training/backprop/update logic.

Manual-review triggers: graph presents backward relationships that code does not implement, or code uses a different optimizer/update path than the graph implies.

## Code-3. 訓練法正確性: 25

HW6 明確要求用 `mini-batch (stochastic) gradient with momentum`。課堂投影片也區分 mini-batch gradient 與 mini-batch gradient with momentum。

### 3A. mini-batch implementation: 8

| Score | Check condition |
| ---: | --- |
| 8 | 有明確 batch 切分與 batch-level 更新流程。 |
| 6 | 有 mini-batch 概念，但實作略不完整。 |
| 4 | 有 batching 痕跡，但訓練主流程不清。 |
| 2 | 只有變數名像 batch，實際不成立。 |
| 0 | 沒有 mini-batch。 |

Required evidence: batch size, batch iterator/slicing/DataLoader, and parameter updates occurring by batch.

Manual-review triggers: batch code is dead/unreachable, train/test data is mixed, or external training hides batch logic.

### 3B. momentum implementation: 10

| Score | Check condition |
| ---: | --- |
| 10 | 有明確 momentum state / accumulation，符合 momentum 邏輯。 |
| 8 | 有 momentum 公式與狀態，但細節略有瑕疵。 |
| 6 | 有 momentum 雛形，但不穩定或不完整。 |
| 3 | 只有宣稱有 momentum，實作很弱。 |
| 0 | 沒有 momentum。 |

Required evidence: velocity/momentum state, previous-update accumulation, or optimizer configuration that clearly uses momentum on the submitted model parameters.

Manual-review triggers: student claims momentum but update rule does not accumulate prior updates, uses Adam as a substitute without instructor approval, or optimizer configuration is hidden.

### 3C. 參數更新規則正確性: 7

| Score | Check condition |
| ---: | --- |
| 7 | 權重更新順序、方向、變數一致。 |
| 5 | 整體正確，少量瑕疵。 |
| 3 | 更新規則可見，但邏輯不夠穩。 |
| 1 | 更新片段存在，但不足以成立。 |
| 0 | 無法驗證更新規則。 |

Required evidence: optimizer step/manual update tied to all trainable parameters and the declared loss/gradient path.

Manual-review triggers: only some parameters update, update direction is contradictory, or result appears incompatible with the submitted update rule.

## Code-4. 結果達成度: 20

題目要求 `accuracy of MNIST test data` 至少 `98%`。

### 4A. test accuracy 級距: 20

| Score | MNIST test accuracy evidence |
| ---: | --- |
| 20 | `>= 98.50%` |
| 19 | `98.30% - 98.49%` |
| 18 | `98.10% - 98.29%` |
| 17 | `98.00% - 98.09%` |
| 16 | `97.80% - 97.99%` |
| 15 | `97.60% - 97.79%` |
| 14 | `97.40% - 97.59%` |
| 13 | `97.20% - 97.39%` |
| 12 | `97.00% - 97.19%` |
| 10 | `96.50% - 96.99%` |
| 8 | `96.00% - 96.49%` |
| 6 | `95.00% - 95.99%` |
| 3 | `90.00% - 94.99%` |
| 0 | `< 90.00%` or no credible test accuracy evidence |

Required evidence: retained notebook output, log, screenshot, or report that is traceable to the submitted HW6 model and MNIST test/evaluation data.

Evidence policy: if a student only writes an accuracy number without enough supporting evidence, do not award full result credit; cap or reduce according to `docs/hw6_evidence_levels.md`.

Manual-review triggers: conflicting accuracy values, suspicious result formatting, unclear train/test split, or result not tied to submitted architecture.

## Code-5. 證據與可稽核性: 10

### 5A. code 證據完整性: 4

| Score | Check condition |
| ---: | --- |
| 4 | 有完整 code / notebook / script，可回查。 |
| 3 | 主要 code 存在，但少量缺漏。 |
| 2 | 只有部分 code。 |
| 1 | 只有截圖或片段。 |
| 0 | 沒有可用 code 證據。 |

### 5B. 執行證據: 3

| Score | Check condition |
| ---: | --- |
| 3 | 有 log / output / notebook output / print evidence。 |
| 2 | 有部分結果證據。 |
| 1 | 只有單張結果圖。 |
| 0 | 無法驗證。 |

### 5C. 結果可追溯性: 3

| Score | Check condition |
| ---: | --- |
| 3 | TA 能從提交內容追到「這份 code -> 這個結果」。 |
| 2 | 大致可追。 |
| 1 | 關聯薄弱。 |
| 0 | 不可追溯。 |

Evidence caps are defined in `docs/hw6_evidence_levels.md`.
