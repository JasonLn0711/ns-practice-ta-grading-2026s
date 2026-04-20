# HW6(圖) 詳細評分基準

Total score: `100`.

這一份分數只評「學生是否把題目要求的圖真正畫對、畫完整、畫得可驗證」。不要用 code 成果、accuracy、或視覺美觀直接替代 figure deliverables。

## First-principle grading rules

- No score without evidence.
- No deduction without a written reason.
- Figure score is independent from code score.
- A polished image is not enough; it must be the required computational graph, learned filters, or intermediate feature maps.
- If graph and code do not match, deduct in both `HW6(code)` and `HW6(圖)` according to `docs/hw6_cross_rules.md`.

## Category Breakdown

| Category | Points |
| --- | ---: |
| Figure-1. Computational graph 正確性與完整性 | 40 |
| Figure-2. learned filters 視覺化 | 20 |
| Figure-3. intermediate feature maps 視覺化 | 25 |
| Figure-4. 圖像證據與可稽核性 | 15 |

## Figure-1. Computational graph 正確性與完整性: 40

題目要求畫出 `similar to slide 48` 的 graph，並與實作 notation 一致。課堂投影片中，CNN 的 forward / backprop computational graph 是整個 HW6 的核心。

### 1A. 架構完整性: 10

| Score | Check condition |
| ---: | --- |
| 10 | Graph 包含 conv / activation / pool / flatten / 3 hidden blocks / output。 |
| 8 | 主要結構齊，但少少量缺漏。 |
| 6 | 有主要骨架，但不夠完整。 |
| 3 | 只有概略示意。 |
| 0 | 未提供。 |

Required evidence: rendered graph, notebook graph cell/output, PDF/image, or clearly structured graph artifact attributable to the submission.

Manual-review triggers: graph appears reused, graph represents a different architecture, or instructor policy is needed for text-only/source-comment graph evidence.

### 1B. notation 正確性: 10

| Score | Check condition |
| ---: | --- |
| 10 | 符號、層間變數、矩陣/feature map 命名清楚且一致。 |
| 8 | 大致正確，少量不一致。 |
| 6 | 部分正確。 |
| 3 | 符號很混亂。 |
| 0 | 沒有可用 notation。 |

Required evidence: graph notation that can be mapped to code variables, layer names, tensors, matrices, or feature maps.

Manual-review triggers: notation is generic, copied from slides without adaptation, or cannot be matched to code.

### 1C. forward flow 表達: 10

| Score | Check condition |
| ---: | --- |
| 10 | 從 input 到 output 的運算流清楚。 |
| 8 | 大致清楚，少量斷點。 |
| 6 | 主流程可辨識。 |
| 3 | 只能看出部分流程。 |
| 0 | 不可判讀。 |

Required evidence: ordered graph flow through input, convolution/activation/pooling, flatten, hidden layers, and output.

Manual-review triggers: graph arrows or stage ordering contradict the submitted code.

### 1D. backward / gradient 關係表達: 10

| Score | Check condition |
| ---: | --- |
| 10 | 有清楚呈現反向/梯度關係或能支撐 code 實作。 |
| 8 | 大部分有。 |
| 6 | 有部分 backward 訊息。 |
| 3 | 只有 forward 圖，幾乎無 backward 支援。 |
| 0 | 完全無法支撐 backprop。 |

Required evidence: backward arrows, gradient notation, update relations, or graph relationships sufficient for code alignment.

Manual-review triggers: graph claims backward relationships that are absent from code, or graph-only evidence may materially change the grade.

## Figure-2. learned filters 視覺化: 20

題目明確要求畫 `learned filters`。

### 2A. learned filters 是否存在: 8

| Score | Check condition |
| ---: | --- |
| 8 | 有明確 learned filters 圖。 |
| 6 | 有圖但不夠完整。 |
| 3 | 疑似有，但很模糊。 |
| 0 | 沒有。 |

Required evidence: visualization of trained filters/weights from the submitted model, preferably in notebook output or submitted figure file.

Manual-review triggers: figure may be generic, unrelated, or copied; dense weights are submitted as filters without instructor policy.

### 2B. 數量/排版/可辨識性: 6

| Score | Check condition |
| ---: | --- |
| 6 | Filter grid 清楚，數量足夠，能看出差異。 |
| 4 | 大致可辨識。 |
| 2 | 可辨識度低。 |
| 0 | 幾乎無法判讀。 |

Required evidence: readable plotted filter grid or equivalent visual arrangement.

Manual-review triggers: image is too degraded to judge or the plotted objects are not identifiable as filters.

### 2C. 與模型的對應性: 6

| Score | Check condition |
| ---: | --- |
| 6 | 可看出是該模型學到的 filters，不是隨便貼圖。 |
| 4 | 大致合理。 |
| 2 | 證據不足。 |
| 0 | 無法確認。 |

Required evidence: notebook/code output linkage, layer labels, or file context tying filters to the trained HW6 model.

Manual-review triggers: filters are visually present but not traceable to the model.

## Figure-3. intermediate feature maps 視覺化: 25

題目要求 `for an arbitrary input digit`。

### 3A. 有明確 input digit: 5

| Score | Check condition |
| ---: | --- |
| 5 | 輸入 digit 清楚標示。 |
| 3 | 有輸入圖但未清楚標記。 |
| 1 | 疑似有輸入。 |
| 0 | 沒有。 |

Required evidence: input digit image, label, or explicit reference to the input used for feature-map visualization.

Manual-review triggers: feature maps exist but input source cannot be identified.

### 3B. feature maps 是否存在: 8

| Score | Check condition |
| ---: | --- |
| 8 | 確實有中間 feature maps。 |
| 6 | 大部分有。 |
| 3 | 只有少量。 |
| 0 | 沒有。 |

Required evidence: plotted intermediate activations/feature maps from the submitted model.

Manual-review triggers: figures may be final outputs, filters, or dense activations rather than intermediate feature maps.

### 3C. 層次/階段是否清楚: 6

| Score | Check condition |
| ---: | --- |
| 6 | 能看出至少對應某層或某階段，例如 conv 後 / ReLU 後 / pool 後。 |
| 4 | 有些層次資訊。 |
| 2 | 圖存在但無層次標示。 |
| 0 | 不可判讀。 |

Required evidence: labels, captions, cell context, or code-output context identifying the layer/stage.

Manual-review triggers: maps are visually present but cannot be located in the model pipeline.

### 3D. 可解釋性: 6

| Score | Check condition |
| ---: | --- |
| 6 | TA 能理解這些 maps 是怎麼來的。 |
| 4 | 大致可理解。 |
| 2 | 可理解度低。 |
| 0 | 無法解釋。 |

Required evidence: traceable relationship among input digit, model stage, and plotted maps.

Manual-review triggers: maps look fabricated, generic, or disconnected from model execution.

## Figure-4. 圖像證據與可稽核性: 15

### 4A. 標題/標籤/圖說: 5

| Score | Check condition |
| ---: | --- |
| 5 | 每張主要圖有標題、標籤或圖說。 |
| 4 | 大部分有。 |
| 2 | 只有部分。 |
| 0 | 沒有。 |

### 4B. 與 code / notebook 對應: 5

| Score | Check condition |
| ---: | --- |
| 5 | 圖與 code / notebook output 明確可對應。 |
| 4 | 大致可對應。 |
| 2 | 弱對應。 |
| 0 | 無法對應。 |

### 4C. 可回查性: 5

| Score | Check condition |
| ---: | --- |
| 5 | 另一位 TA 可以根據提交檔案回查。 |
| 4 | 大致可回查。 |
| 2 | 回查困難。 |
| 0 | 不可回查。 |

Evidence caps are defined in `docs/hw6_evidence_levels.md`.
