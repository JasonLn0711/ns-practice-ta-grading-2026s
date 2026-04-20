#!/usr/bin/env python3
"""Generate Taiwan Traditional Chinese student grading notes for HW5 and HW6.

The English audit notes remain the source history. This script rebuilds a
separate zh-TW view from the versioned score and deduction CSVs so repeated
generation is consistent and auditable.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_AT = datetime.now().astimezone().isoformat(timespec="seconds")


HW5_SCORE_FIELDS = [
    ("completeness_score", "繳交完整性", 10),
    ("requirement_score", "需求達成度", 30),
    ("technical_score", "技術正確性", 30),
    ("result_score", "結果品質", 15),
    ("evidence_score", "證據與可稽核性", 15),
    ("penalty_score", "額外扣分", 0),
]

HW6_CODE_FIELDS = [
    ("architecture_score", "Code-1. 架構修改正確性", 25),
    ("graph_code_alignment_score", "Code-2. 計算圖與程式一致性", 20),
    ("training_method_score", "Code-3. 訓練法正確性", 25),
    ("result_score", "Code-4. 結果達成度", 20),
    ("evidence_score", "Code-5. 證據與可稽核性", 10),
    ("code_penalty", "程式額外扣分", 0),
]

HW6_FIGURE_FIELDS = [
    ("graph_score", "Figure-1. 計算圖正確性與完整性", 40),
    ("filters_score", "Figure-2. 已學得濾波器視覺化", 20),
    ("feature_maps_score", "Figure-3. 中間特徵圖視覺化", 25),
    ("figure_evidence_score", "Figure-4. 圖像證據與可稽核性", 15),
    ("figure_penalty", "圖像額外扣分", 0),
]

CATEGORY_ZH = {
    "completeness_score": "繳交完整性",
    "requirement_score": "需求達成度",
    "technical_score": "技術正確性",
    "result_score": "結果品質",
    "evidence_score": "證據與可稽核性",
    "architecture_score": "架構修改正確性",
    "graph_code_alignment_score": "計算圖與程式一致性",
    "training_method_score": "訓練法正確性",
    "code_penalty": "Code 額外扣分",
    "graph_score": "計算圖正確性與完整性",
    "filters_score": "已學得濾波器視覺化",
    "feature_maps_score": "中間特徵圖視覺化",
    "figure_evidence_score": "圖像證據與可稽核性",
    "figure_penalty": "Figure 額外扣分",
}

TAG_ZH = {
    "ACCURACY_BELOW_TARGET": "MNIST test accuracy 低於作業目標或未達滿分級距。",
    "CODE_ACCURACY_BELOW_TARGET": "HW6(code) 的 test accuracy 低於作業目標或未達滿分級距。",
    "CODE_ARCH_REPLACEMENT_INCOMPLETE": "架構替換未完整符合 HW6 要求。",
    "CODE_BACKPROP_INCOMPLETE": "backward / gradient flow 證據不完整。",
    "CODE_FORWARD_GRAPH_MISMATCH": "forward flow 與 computational graph 無法完整對應。",
    "CODE_GRAPH_NOTATION_MISMATCH": "計算圖標記與程式命名或實作無法充分對應。",
    "CODE_INCOMPLETE": "code 或必要實作流程不完整。",
    "CODE_MOMENTUM_MISSING": "未能驗證 mini-batch gradient with momentum 的實作。",
    "CODE_RESULT_BAND_BELOW_FULL": "accuracy 已達標或接近達標，但依官方細分級距未取得結果滿分。",
    "FIG_FEATURE_MAPS_UNCLEAR": "中間特徵圖存在但標示、層次或可解釋性不足。",
    "FIG_FILTERS_MISSING": "未找到可驗證的已學得濾波器圖。",
    "FIG_GRAPH_CODE_MISMATCH": "圖與 code 的架構或 hidden-layer 數量不一致。",
    "FIG_GRAPH_INCOMPLETE": "computational graph 不完整或只呈現部分資訊。",
    "FIG_GRAPH_MISSING": "未找到計算圖。",
    "FIG_LABELING_INSUFFICIENT": "圖的標題、標籤或圖說不足，降低可稽核性。",
    "FIG_NOT_AUDITABLE": "圖像證據不足以讓另一位 TA 獨立回查。",
    "NO_HYPERPARAMETER_SEARCH_EVIDENCE": "缺少可回查的 hyperparameter search / configuration development 證據。",
    "TEST_PIPELINE_UNCLEAR": "MNIST test / validation 流程不夠清楚或與官方測試集使用方式有疑義。",
    "WEAK_AUDIT_EVIDENCE": "證據可用但不夠完整，需依證據等級保守給分。",
}

TERM_REPLACEMENTS = [
    ("computational graph artifact", "計算圖證據"),
    ("computational graph", "計算圖"),
    ("graph-consistent implementation", "與計算圖一致的實作"),
    ("graph/code/result", "計算圖 / 程式 / 結果"),
    ("code / graph / result", "程式 / 計算圖 / 結果"),
    ("code / graph", "程式 / 計算圖"),
    ("graph / code", "計算圖 / 程式"),
    ("Graph-to-code", "計算圖與程式"),
    ("Graph/code", "計算圖 / 程式"),
    ("Graph", "計算圖"),
    ("graph", "計算圖"),
    ("notation alignment", "標記對齊"),
    ("notation", "標記"),
    ("alignment", "對齊"),
    ("Code", "程式"),
    ("code", "程式"),
    ("Figure", "圖像"),
    ("figure", "圖像"),
    ("learned convolution filters", "已學得卷積濾波器"),
    ("learned-filter plot", "已學得濾波器圖"),
    ("learned filters", "已學得濾波器"),
    ("feature-map", "特徵圖"),
    ("feature maps", "特徵圖"),
    ("filters", "濾波器"),
    ("filter", "濾波器"),
    ("maps", "特徵圖"),
    ("visualizations", "視覺化輸出"),
    ("visualization", "視覺化"),
    ("visuals", "視覺化輸出"),
    ("visual outputs", "視覺化輸出"),
    ("visual", "視覺化"),
    ("artifact", "證據"),
    ("evidence level", "證據等級"),
    ("evidence", "證據"),
    ("auditability", "可稽核性"),
    ("traceability", "可追溯性"),
    ("traceable", "可追溯"),
    ("auditable", "可稽核"),
    ("trained", "訓練後的"),
    ("missing", "缺少"),
    ("target-reaching", "達標"),
    ("accuracy", "準確率"),
    ("result", "結果"),
    ("Result band correction", "結果級距修正"),
    ("retained", "保留的"),
    ("outputs", "輸出"),
    ("output", "輸出"),
    ("training", "訓練"),
    ("workflow", "流程"),
    ("development", "開發"),
    ("implementation", "實作"),
    ("consistency", "一致性"),
    ("matching", "相符的"),
    ("generated", "產生的"),
    ("updates", "更新"),
    ("deliverables", "繳交項目"),
    ("labels", "標籤"),
    ("complete", "完整"),
    ("strong", "強"),
    ("dense-layer responses", "dense 層反應"),
    ("dense weights", "dense 權重"),
    ("CNN intermediate", "CNN 中間"),
    ("dense model", "dense 模型"),
    ("dense-network", "dense-network"),
    ("configuration", "設定"),
    ("function", "函式"),
    ("hyperparameter search", "超參數搜尋"),
    ("hyperparameter grid", "超參數網格"),
    ("grid-search", "網格搜尋"),
    ("per-epoch logs", "每個 epoch 的記錄"),
    ("logs", "記錄"),
    ("hidden layers", "隱藏層"),
    ("hidden-layer", "隱藏層"),
    ("fully connected layers", "全連接層"),
    ("source comments", "原始碼註解"),
    ("source cell", "原始碼儲存格"),
    ("text-only", "純文字"),
    ("rendered", "轉成圖像的"),
    ("slide-style", "投影片風格"),
    ("Level ", "等級 "),
]

CLEANUP_REPLACEMENTS = [
    ("程式 或", "程式或"),
    ("有 超參數", "有超參數"),
    ("的 設定流程", "的設定流程"),
    ("沒有 計算圖證據", "沒有計算圖證據"),
    ("程式 與", "程式與"),
    ("缺少 計算圖", "缺少計算圖"),
    ("未找到 計算圖", "未找到計算圖"),
    ("有 特徵圖", "有特徵圖"),
    ("圖像 證據", "圖像證據"),
    ("程式 證據等級", "程式證據等級"),
    ("與計算圖一致的實作 給", "與計算圖一致的實作給"),
    ("訓練後的 濾波器", "訓練後的濾波器"),
    ("濾波器 的", "濾波器的"),
    ("濾波器s", "濾波器"),
    ("輸出s", "輸出"),
    ("項目s", "項目"),
    ("標籤s", "標籤"),
    ("filter 圖像 證據", "濾波器圖像證據"),
    ("計算圖 / 濾波器 圖像 證據", "計算圖 / 濾波器圖像證據"),
    ("濾波器 圖像證據", "濾波器圖像證據"),
    ("特徵圖 圖像證據", "特徵圖圖像證據"),
    ("只有部分 特徵圖", "只有部分特徵圖"),
    ("缺少計算圖 與", "缺少計算圖與"),
    ("圖像證據 偏弱", "圖像證據偏弱"),
    ("設定 流程", "設定流程"),
    ("網格搜尋 結果", "網格搜尋結果"),
    ("訓練後的濾波器 的", "訓練後的濾波器的"),
    ("訓練後的濾波器的 已學得濾波器圖", "訓練後模型的已學得濾波器圖"),
    ("可連到 訓練後模型", "可連到訓練後模型"),
    ("圖像證據 可稽核", "圖像證據可稽核"),
    ("程式 / 計算圖 標記", "程式 / 計算圖標記"),
    ("程式 / 計算圖 / 結果", "程式 / 計算圖 / 結果"),
    ("計算圖 標記 是", "計算圖標記是"),
    ("計算圖 標記 只有", "計算圖標記只有"),
    ("相符的 程式", "相符的程式"),
    ("產生的 計算圖", "產生的計算圖"),
    ("視覺化 輸出", "視覺化輸出"),
    ("視覺化s", "視覺化輸出"),
    ("有 網格", "有網格"),
    ("沒有 每個", "沒有每個"),
    ("記錄 或", "記錄或"),
    ("的 設定流程", "的設定流程"),
    ("計算圖 描述", "計算圖描述"),
    ("視覺化的是 dense 權重", "視覺化的是 dense 權重"),
    ("CNN 中間 特徵圖", "CNN 中間特徵圖"),
    ("特徵圖證據 的問題", "特徵圖證據的問題"),
]

NOTE_ZH = {
    # HW5 deduction notes.
    "Hyperparameter search exists, but the expected configuration workflow is not packaged as a named configuration() function.": "有 hyperparameter search，但預期的 configuration 流程沒有包成明確命名的 `configuration()` function。",
    "Retained output shows grid-search results, but not per-epoch logs or a stronger audit summary.": "保留的輸出有 grid-search 結果，但沒有 per-epoch logs 或更完整的稽核摘要。",
    "No retained configuration/search evidence for choosing hidden nodes, learning rate, batch size, or iteration count.": "沒有保留用來選擇 hidden nodes、learning rate、batch size 或 iteration count 的 configuration/search 證據。",
    "Required epoch-style configuration is replaced by a fixed iteration count.": "題目需要的 epoch-style configuration 被固定 iteration count 取代。",
    "Official test set is split into validation/test halves, so the reported test accuracy is on a 5k held-out test subset.": "官方 test set 被切成 validation/test halves，因此回報的 test accuracy 是在 5k held-out test subset 上，而不是完整 10k test set。",
    "Result logs are retained, but configuration/development evidence is incomplete.": "有保留結果 logs，但 configuration/development 證據不完整。",
    "Final notebook output shows test accuracy 97.90%, below the 98% target.": "notebook 最終輸出顯示 test accuracy 為 97.90%，低於 98% 目標。",
    "Configuration workflow is defined but not connected to the final retained run.": "有定義 configuration workflow，但無法連到最後保留的實際執行結果。",
    "No retained search/comparison output shows that final hard-coded parameters were selected by the configuration workflow.": "沒有保留 search/comparison 輸出可證明最後 hard-coded parameters 是由 configuration workflow 選出。",
    "Final result is retained, but development/search evidence is incomplete.": "有保留最終結果，但 development/search 證據不完整。",
    "Hyperparameter grid exists, but the expected configuration workflow is not packaged as a named configuration() function.": "有 hyperparameter grid，但預期的 configuration 流程沒有包成明確命名的 `configuration()` function。",
    "Implementation uses a simpler one-hidden-layer network rather than a clearly HW4-style multi-hidden-layer path.": "實作使用較簡化的 one-hidden-layer network，而不是清楚延續 HW4 風格的 multi-hidden-layer path。",
    "Evaluation uses an OpenML train/test split rather than the official MNIST test files used by the assignment materials.": "評估使用 OpenML train/test split，而不是作業材料中的官方 MNIST test files。",
    "Best retained accuracy is about 90.16%, below the 98% target.": "保留的最佳 accuracy 約為 90.16%，低於 98% 目標。",
    "Retained evidence is limited to grid-search final rows; no epoch logs or stronger execution trace.": "保留證據只到 grid-search final rows，沒有 epoch logs 或更完整的 execution trace。",
    "No retained configuration/search evidence for choosing hidden nodes, learning rate, batch size, or epochs.": "沒有保留用來選擇 hidden nodes、learning rate、batch size 或 epochs 的 configuration/search 證據。",
    "Implementation is a fixed one-hidden-layer run and does not show the requested development/configuration workflow.": "實作是固定 one-hidden-layer run，沒有呈現題目要求的 development/configuration workflow。",
    "Highest visible retained test accuracy is about 97.83%, below the 98% target.": "可見的最高保留 test accuracy 約為 97.83%，低於 98% 目標。",
    "Logs are retained, but no configuration/development evidence or final summary is retained.": "有保留 logs，但沒有 configuration/development 證據或 final summary。",
    "Best printed test accuracy is 97.86%, below the 98% target.": "印出的最佳 test accuracy 為 97.86%，低於 98% 目標。",
    "Retained outputs show per-configuration final accuracy, but no per-epoch logs or full training trace.": "保留輸出有 per-configuration final accuracy，但沒有 per-epoch logs 或完整 training trace。",
    "Notebook shows final configuration values and training logs, but no comparison/search/trial evidence for hyperparameter selection.": "notebook 有 final configuration values 與 training logs，但沒有用於 hyperparameter selection 的 comparison/search/trial 證據。",
    "Final test accuracy is 0.9792 (97.92%), below the 98% target.": "final test accuracy 為 0.9792（97.92%），低於 98% 目標。",
    "Notebook splits the official MNIST test set into validation/test halves, so the retained final accuracy is on a 5k held-out subset rather than the original 10k test set.": "notebook 將官方 MNIST test set 切成 validation/test halves，因此保留的 final accuracy 是在 5k held-out subset 上，而不是原始 10k test set。",
    "Configuration trials evaluate directly on the official MNIST test set, so the test set is used for tuning rather than reserved for a final check.": "configuration trials 直接在官方 MNIST test set 上評估，因此 test set 被用於 tuning，而不是保留作為 final check。",
    "No retained configuration/search evidence for choosing hidden-layer sizes, learning rate, batch size, or epoch/iteration budget.": "沒有保留用來選擇 hidden-layer sizes、learning rate、batch size 或 epoch/iteration budget 的 configuration/search 證據。",
    "Training is a fixed iteration-based run and does not implement the requested configuration/development workflow.": "training 是固定 iteration-based run，沒有實作題目要求的 configuration/development workflow。",
    "Result logs are retained, but configuration/search and epoch-based development evidence are missing.": "有保留 result logs，但缺少 configuration/search 與 epoch-based development 證據。",
    "Configuration trials are retained, but the search is narrow and varies learning rate only while hidden layers, batch size, and epochs remain fixed.": "有保留 configuration trials，但 search 範圍狹窄，只調整 learning rate；hidden layers、batch size 與 epochs 維持固定。",
    "Notebook splits the official MNIST test set into validation/test halves, so final accuracy is on a 5k held-out subset rather than the original 10k test set.": "notebook 將官方 MNIST test set 切成 validation/test halves，因此 final accuracy 是在 5k held-out subset 上，而不是原始 10k test set。",
    "Notebook uses one fixed hyperparameter dictionary but no retained candidate comparison/search output showing how those values were selected.": "notebook 使用一組固定 hyperparameter dictionary，但沒有保留 candidate comparison/search 輸出來說明這些值如何被選出。",
    "Final logs and result are retained, but development evidence for the chosen configuration is incomplete.": "有保留 final logs 與 result，但 chosen configuration 的 development evidence 不完整。",
    "Configuration experiments evaluate directly on the official MNIST test set, so the test set is used during tuning rather than reserved for a separate final check.": "configuration experiments 直接在官方 MNIST test set 上評估，因此 test set 在 tuning 階段就被使用，而不是保留作為獨立 final check。",
    "Required epoch-based configuration is weak: development runs are time-based and the final retained run uses fixed iterations.": "題目要求的 epoch-based configuration 證據偏弱：development runs 是 time-based，最後保留的 run 使用 fixed iterations。",
    "Configuration outputs show weak/non-convergent training for the development runs and the final run is not cleanly summarized.": "configuration outputs 顯示 development runs 訓練偏弱或未收斂，且 final run 沒有清楚摘要。",
    "Highest visible retained accuracy is about 97.79%, below the 98% target.": "可見的最高保留 accuracy 約為 97.79%，低於 98% 目標。",
    "Logs are retained, but final result and configuration-to-result traceability are weak.": "有保留 logs，但 final result 與 configuration-to-result traceability 偏弱。",
    "best_cfg is stated as observed from experiments, but no retained candidate search/comparison output shows how it was selected.": "`best_cfg` 被描述為從 experiments 觀察而來，但沒有保留 candidate search/comparison 輸出說明如何選出。",
    # HW6 code notes.
    "Complete code evidence: architecture, graph-aligned implementation, momentum training, 98%+ result, and retained outputs.": "code 證據完整：包含架構、與 graph 對齊的實作、momentum training、98% 以上結果，以及保留的輸出。",
    "Momentum is implemented through beta/m variables even though the literal word momentum is absent; result and code are traceable.": "雖然沒有直接出現 `momentum` 這個字，但已透過 beta/m variables 實作 momentum；結果與 code 可以追溯。",
    "Strong code/result evidence, but no computational graph artifact exists, so graph-consistent implementation receives zero and Level B code evidence applies.": "code 與結果證據很強，但沒有 computational graph artifact，因此 graph-consistent implementation 給 0，code evidence level 採 Level B。",
    "Complete code evidence with graph-matching notation and momentum updates. Result band correction: Verified accuracy is in the 98.30-98.49% band, so result earns 19/20.": "code 證據完整，包含與 graph 相符的 notation 與 momentum updates。結果級距修正：已驗證 accuracy 落在 98.30-98.49% 級距，因此 result 得 19/20。",
    "Code has result, filters, and maps, but architecture lacks the required added hidden layers, graph is missing, and Adam is used instead of explicit momentum.": "code 有結果、filters 與 maps，但架構缺少題目要求新增的 hidden layers，graph 缺失，且使用 Adam 而不是明確的 momentum。",
    "Complete W-style architecture, graph alignment, momentum updates, and target-reaching result. Result band correction: Verified accuracy is in the 98.30-98.49% band, so result earns 19/20.": "W-style architecture、graph alignment、momentum updates 與達標結果完整。結果級距修正：已驗證 accuracy 落在 98.30-98.49% 級距，因此 result 得 19/20。",
    "Architecture and momentum are strong, but no graph artifact exists and retained test accuracy is 97.62%. Result band correction: Retained test accuracy is 97.62%, below the 98% target and in the 97.60-97.79% band.": "architecture 與 momentum 證據強，但沒有 graph artifact，且保留的 test accuracy 為 97.62%。結果級距修正：97.62% 低於 98% 目標，落在 97.60-97.79% 級距。",
    "Complete notebook markdown graph, matching code, momentum updates, and 98%+ result. Result band correction: Verified accuracy is in the 98.10-98.29% band, so result earns 18/20.": "notebook markdown graph、matching code、momentum updates 與 98% 以上結果完整。結果級距修正：已驗證 accuracy 落在 98.10-98.29% 級距，因此 result 得 18/20。",
    "Code is strong and target-reaching, but graph-consistent implementation cannot be verified because graph evidence is missing. Result band correction: Verified accuracy is in the 98.30-98.49% band, so result earns 19/20.": "code 強且結果達標，但因缺少 graph evidence，無法驗證 graph-consistent implementation。結果級距修正：已驗證 accuracy 落在 98.30-98.49% 級距，因此 result 得 19/20。",
    "Complete PyTorch CNN, Graphviz graph, SGD momentum, 99.09% result, filters, and maps.": "PyTorch CNN、Graphviz graph、SGD momentum、99.09% 結果、filters 與 maps 都完整。",
    "Code and graph show two hidden fully connected layers total; current rubric expects two additional hidden layers.": "code 與 graph 顯示 total 為 two hidden fully connected layers；目前 rubric 解讀要求 two additional hidden layers。",
    "Complete generated graph, PyTorch CNN, SGD momentum, result, filters, and maps.": "generated graph、PyTorch CNN、SGD momentum、結果、filters 與 maps 都完整。",
    "Complete PDF graph, matching code, momentum updates, and target-reaching accuracy. Result band correction: Verified accuracy is in the 98.30-98.49% band, so result earns 19/20.": "PDF graph、matching code、momentum updates 與達標 accuracy 完整。結果級距修正：已驗證 accuracy 落在 98.30-98.49% 級距，因此 result 得 19/20。",
    "Code is strong and target-reaching, but graph-consistent implementation cannot be verified because graph evidence is missing.": "code 強且結果達標，但因缺少 graph evidence，無法驗證 graph-consistent implementation。",
    "Code is complete and graph notation is aligned, but graph evidence is text-only in an unexecuted source cell.": "code 完整且 graph notation 對齊，但 graph evidence 只是在未執行 source cell 中的文字。",
    "Submission has strong dense-network evidence, but it does not implement the required CNN convolution/pooling workflow.": "submission 有強的 dense-network 證據，但沒有實作題目要求的 CNN convolution/pooling workflow。",
    "Complete PDF graph, matching code, momentum updates, result, filters, and maps. Result band correction: Verified accuracy is in the 98.10-98.29% band, so result earns 18/20.": "PDF graph、matching code、momentum updates、結果、filters 與 maps 完整。結果級距修正：已驗證 accuracy 落在 98.10-98.29% 級距，因此 result 得 18/20。",
    "Graph shows three hidden layers, but code uses two hidden fully connected layers before output.": "graph 顯示 three hidden layers，但 code 在 output 前使用 two hidden fully connected layers。",
    "Code is complete and graph notation is aligned, but graph evidence appears only as source comments.": "code 完整且 graph notation 對齊，但 graph evidence 只以 source comments 形式出現。",
    # HW6 figure notes.
    "Complete figure evidence: graph, learned filters, feature maps, and traceable labels.": "圖像證據完整：包含 graph、learned filters、feature maps 與可追溯的 labels。",
    "PDF graph, filters, and feature maps are complete and auditable.": "PDF graph、filters 與 feature maps 完整且可稽核。",
    "Feature maps are present, but the computational graph and learned-filter plot are missing; figure evidence is weak.": "有 feature maps，但缺少 computational graph 與 learned-filter plot；figure evidence 偏弱。",
    "Complete graph/PDF and visualization evidence.": "graph/PDF 與 visualization evidence 完整。",
    "Filters and feature maps are present, but the computational graph is missing.": "有 filters 與 feature maps，但缺少 computational graph。",
    "Complete PDF graph, learned filters, and y1/y2/y3 feature-map evidence.": "PDF graph、learned filters 與 y1/y2/y3 feature-map evidence 完整。",
    "Filters and feature maps are present, but computational graph evidence is missing.": "有 filters 與 feature maps，但缺少 computational graph evidence。",
    "Complete graph, learned filters, and feature maps.": "graph、learned filters 與 feature maps 完整。",
    "Filters and feature maps are present, but no graph artifact exists.": "有 filters 與 feature maps，但沒有 graph artifact。",
    "Complete generated graph and visualization evidence.": "generated graph 與 visualization evidence 完整。",
    "Figure deliverables are complete and consistent with the submitted code.": "figure deliverables 完整，且與提交的 code 一致。",
    "Complete PDF graph, learned filters, and feature maps.": "PDF graph、learned filters 與 feature maps 完整。",
    "Text-only graph notation is model-specific, but not a rendered slide-style graph artifact.": "text-only graph notation 與模型相關，但不是 render 出來的 slide-style graph artifact。",
    "Graph and visual outputs are traceable but correspond to a dense model, not CNN filters/feature maps.": "graph 與 visual outputs 可追溯，但對應的是 dense model，不是 CNN filters / feature maps。",
    "Complete graph and visualization evidence.": "graph 與 visualization evidence 完整。",
    "Graph is visible but does not fully match code hidden-layer count.": "graph 可見，但 hidden-layer count 與 code 未完全一致。",
    "Source-comment graph notation is model-specific, but not a rendered slide-style graph artifact.": "source-comment graph notation 與模型相關，但不是 render 出來的 slide-style graph artifact。",
    # HW6 deduction notes.
    "No computational graph artifact was found, so code/graph notation alignment cannot be verified.": "未找到 computational graph artifact，因此無法驗證 code / graph notation alignment。",
    "Missing graph prevents full code/graph/result traceability.": "缺少 graph，導致 code / graph / result 無法完整追溯。",
    "Accuracy band 98.30-98.49 earns 19/20. Verified accuracy is in the 98.30-98.49% band, so result earns 19/20.": "accuracy 落在 98.30-98.49 級距時 result 得 19/20；已驗證 accuracy 在此級距，所以 result 得 19/20。",
    "Submitted model has one hidden fully connected layer plus output rather than two added hidden layers.": "提交模型是 one hidden fully connected layer 加 output，而不是 two added hidden layers。",
    "No computational graph artifact was found.": "未找到 computational graph artifact。",
    "Training uses Adam rather than mini-batch stochastic gradient with historical momentum accumulation.": "training 使用 Adam，而不是具有 historical momentum accumulation 的 mini-batch stochastic gradient。",
    "Missing graph and missing required momentum evidence cap code auditability.": "缺少 graph 且缺少題目要求的 momentum evidence，因此限制 code auditability 分數。",
    "Accuracy band 97.60-97.79 earns 15/20. Retained test accuracy is 97.62%, below the 98% target and in the 97.60-97.79% band.": "accuracy 落在 97.60-97.79 級距時 result 得 15/20；保留 test accuracy 為 97.62%，低於 98% 目標並落在此級距。",
    "Accuracy band 98.10-98.29 earns 18/20. Verified accuracy is in the 98.10-98.29% band, so result earns 18/20.": "accuracy 落在 98.10-98.29 級距時 result 得 18/20；已驗證 accuracy 在此級距，所以 result 得 18/20。",
    "Missing graph caps code auditability.": "缺少 graph，因此限制 code auditability 分數。",
    "Architecture shows two hidden fully connected layers total instead of two additional hidden layers under current rubric interpretation.": "依目前 rubric 解讀，architecture 顯示 total 為 two hidden fully connected layers，而不是 two additional hidden layers。",
    "Graph notation is text-only source, so implementation/graph consistency is less independently auditable.": "graph notation 是 text-only source，因此 implementation / graph consistency 較難由另一位 TA 獨立稽核。",
    "Code implements a dense 4-layer MNIST network rather than the required CNN architecture.": "code 實作的是 dense 4-layer MNIST network，而不是題目要求的 CNN architecture。",
    "Graph/code are aligned to a dense model, not the required CNN workflow.": "graph / code 對齊的是 dense model，而不是題目要求的 CNN workflow。",
    "Evidence is traceable but tied to the wrong architecture.": "證據可追溯，但對應的是錯誤架構。",
    "Notebook code implements two hidden fully connected layers while current rubric expects two additional hidden layers.": "notebook code 實作 two hidden fully connected layers，但目前 rubric 要求 two additional hidden layers。",
    "Submitted graph and code disagree on hidden-layer count.": "提交的 graph 與 code 在 hidden-layer count 上不一致。",
    "Graph/code mismatch caps code auditability.": "graph / code mismatch 限制 code auditability 分數。",
    "Graph notation is source comments only, so implementation/graph consistency is less independently auditable.": "graph notation 只有 source comments，因此 implementation / graph consistency 較難由另一位 TA 獨立稽核。",
    "No learned-filter plot tied to trained filters was found.": "未找到可連到 trained filters 的 learned-filter plot。",
    "Feature maps are present but not enough to compensate for missing graph/filter figure evidence.": "有 feature maps，但不足以補足缺少 graph / filter figure evidence 的問題。",
    "Only partial feature-map figure evidence is auditable.": "只有部分 feature-map figure evidence 可稽核。",
    "Figures are partially auditable but graph traceability is absent.": "figures 可部分稽核，但缺少 graph traceability。",
    "Visualization evidence is present, but graph traceability is absent.": "有 visualization evidence，但缺少 graph traceability。",
    "Graph evidence is text-only source rather than a rendered slide-style graph artifact.": "graph evidence 是 text-only source，而不是 render 出來的 slide-style graph artifact。",
    "Text-only graph format caps figure explainability.": "text-only graph format 限制 figure explainability 分數。",
    "Graph describes the submitted dense model rather than the required CNN workflow.": "graph 描述的是提交的 dense model，而不是題目要求的 CNN workflow。",
    "Dense weights are visualized, not learned convolution filters.": "視覺化的是 dense weights，不是 learned convolution filters。",
    "Dense-layer responses are visualized, not CNN intermediate feature maps.": "視覺化的是 dense-layer responses，不是 CNN intermediate feature maps。",
    "Visuals are auditable but not tied to CNN deliverables.": "visuals 可稽核，但不是對應 CNN deliverables。",
    "Graph shows a different hidden-layer count from the submitted code.": "graph 顯示的 hidden-layer count 與提交的 code 不同。",
    "Graph/code mismatch caps figure explainability.": "graph / code mismatch 限制 figure explainability 分數。",
    "Graph evidence appears as source comments rather than a rendered slide-style graph artifact.": "graph evidence 以 source comments 形式出現，而不是 render 出來的 slide-style graph artifact。",
    "Source-comment graph format caps figure explainability.": "source-comment graph format 限制 figure explainability 分數。",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate zh-TW student grading notes.")
    parser.add_argument("--homework", choices=["hw5", "hw6", "all"], default="all")
    parser.add_argument("--apply", action="store_true", help="Write files instead of dry-run.")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def group_by(rows: list[dict[str, str]], key: str) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row.get(key, "")].append(row)
    return grouped


def yn(value: str) -> str:
    normalized = (value or "").strip().lower()
    if normalized in {"yes", "true", "1"}:
        return "是"
    if normalized in {"no", "false", "0"}:
        return "否"
    return value or "未記錄"


def note_zh(note: str) -> str:
    note = (note or "").strip()
    if not note:
        return "無額外備註。"
    if note in NOTE_ZH:
        return localize_terms(NOTE_ZH[note])
    result = note
    replacements = [
        ("Code: ", "Code："),
        ("Figure: ", "Figure："),
        ("Complete", "完整"),
        ("evidence", "證據"),
        ("missing", "缺少"),
        ("graph", "graph"),
        ("code", "code"),
        ("result", "結果"),
        ("accuracy", "accuracy"),
        ("traceable", "可追溯"),
    ]
    for old, new in replacements:
        result = result.replace(old, new)
    return localize_terms(result)


def tag_zh(tag: str) -> str:
    tag = tag.strip()
    return localize_terms(TAG_ZH.get(tag, "此扣分標籤的中文說明尚未在字典中定義；請依英文原始稽核檔回查。"))


def localize_terms(text: str) -> str:
    parts = re.split(r"(`[^`]*`)", text)
    localized: list[str] = []
    for part in parts:
        if part.startswith("`") and part.endswith("`"):
            localized.append(part)
            continue
        for old, new in TERM_REPLACEMENTS:
            part = part.replace(old, new)
        for old, new in CLEANUP_REPLACEMENTS:
            part = part.replace(old, new)
        localized.append(part)
    return "".join(localized)


def tag_list(raw: str) -> list[str]:
    return [part.strip() for part in (raw or "").split(";") if part.strip()]


def rows_for_tags(tags: list[str], deductions: list[dict[str, str]]) -> list[dict[str, str]]:
    if not tags:
        return []
    return [row for row in deductions if row.get("deduction_tag") in tags]


def score_table(fields: list[tuple[str, str, int]], row: dict[str, str]) -> list[str]:
    lines = [
        "| 評分項目 | 得分 | 滿分 |",
        "| --- | ---: | ---: |",
    ]
    for field, label, max_score in fields:
        value = row.get(field, "")
        max_text = "依扣分紀錄" if max_score == 0 else str(max_score)
        lines.append(f"| {label} | {value} | {max_text} |")
    return lines


def deduction_table(deductions: list[dict[str, str]], hw6: bool = False) -> list[str]:
    if not deductions:
        return ["- 無扣分紀錄。"]
    lines = [
        "| 標籤 | 評分項目 | 扣分 | 證據路徑 | 中文原因 |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for row in deductions:
        category = CATEGORY_ZH.get(row.get("category", ""), row.get("category", ""))
        tag = row.get("deduction_tag", "")
        points = row.get("points_deducted", "")
        evidence = row.get("evidence_path", "") or row.get("submission_path", "")
        reason = note_zh(row.get("note", ""))
        lines.append(f"| `{tag}` | {category} | {points} | `{evidence}` | {reason} |")
    return lines


def tag_summary_lines(tags: list[str]) -> list[str]:
    if not tags:
        return ["- 無。"]
    return [f"- `{tag}`：{tag_zh(tag)}" for tag in tags]


def render_hw5(row: dict[str, str], deductions: list[dict[str, str]]) -> str:
    tags = tag_list(row.get("deduction_summary", ""))
    matched = rows_for_tags(tags, deductions)
    lines = [
        f"# HW5 學生評分紀錄（繁體中文） - {row.get('student_id', 'unknown')}",
        "",
        "## 基本資料",
        "",
        f"- 學生姓名：{row.get('student_name') or '未記錄'}",
        f"- 學號：`{row.get('student_id')}`",
        "- 作業：`HW5`",
        f"- 繳交路徑：`{row.get('submission_path')}`",
        f"- 評分者：{row.get('grader')}",
        f"- 原始評分時間：`{row.get('graded_at')}`",
        f"- 中文版本產生時間：`{GENERATED_AT}`",
        f"- 證據等級：`{row.get('evidence_level')}`",
        f"- 是否需要人工複審：{yn(row.get('manual_review_needed'))}",
        "",
        "## 評分紀律",
        "",
        "- 每一項給分都必須有可回查證據。",
        "- 每一項非滿分都必須有扣分標籤與文字理由。",
        "- 缺少或無法驗證的必要項目不得給滿分。",
        "- 準確率達標不能自動抵消開發 / 設定證據不足。",
        "",
        "## 分數拆解",
        "",
        *score_table(HW5_SCORE_FIELDS, row),
        f"| 總分 | {row.get('total_score')} | 100 |",
        "",
        "## 扣分標籤摘要",
        "",
        *tag_summary_lines(tags),
        "",
        "## 扣分明細",
        "",
        *deduction_table(matched),
        "",
        "## 證據與可稽核性說明",
        "",
        f"- 本紀錄依據 `grading/hw5/scores.csv` 與 `grading/hw5/deduction_log.csv` 產生。",
        f"- 證據等級為 `{row.get('evidence_level')}`；此等級代表提交內容的重現性與可回查程度。",
        "- 若學生對分數有疑問，應先回查繳交檔案、扣分標籤與本表中的證據路徑。",
        "",
        "## 給學生的簡短說明",
        "",
        f"本次 HW5 分數為 `{row.get('total_score')}/100`。分數主要依據繳交完整性、需求達成度、技術正確性、結果品質，以及證據與可稽核性評定。非滿分項目已在上方列出扣分標籤與原因。",
        "",
        "## TA / 教師稽核說明",
        "",
        "本中文檔是英文原始稽核紀錄的台灣繁體中文版本；英文原件仍保留作為歷史來源。本檔不新增新的評分判斷，只把既有分數 CSV 與扣分紀錄轉成可讀的中文稽核紀錄。",
        "",
    ]
    return "\n".join(lines)


def render_hw6(
    combined: dict[str, str],
    code: dict[str, str],
    figure: dict[str, str],
    code_deductions: list[dict[str, str]],
    figure_deductions: list[dict[str, str]],
) -> str:
    code_tags = tag_list(code.get("code_deduction_tags", ""))
    figure_tags = tag_list(figure.get("figure_deduction_tags", ""))
    student = combined.get("student_name") or code.get("student_name") or figure.get("student_name")
    student_id = combined.get("student_id") or code.get("student_id") or figure.get("student_id")
    lines = [
        f"# HW6 學生評分回饋（繁體中文） - {student}",
        "",
        "## 基本資料",
        "",
        f"- 學生姓名：{student}",
        f"- 學號：`{student_id}`",
        "- 作業：`HW6`",
        f"- 繳交路徑：`{combined.get('submission_path')}`",
        f"- 評分者：{code.get('grader') or figure.get('grader')}",
        f"- 原始評分時間：`{code.get('graded_at') or figure.get('graded_at')}`",
        f"- 中文版本產生時間：`{GENERATED_AT}`",
        f"- 證據等級：`{combined.get('evidence_level')}`",
        f"- 是否需要人工複審：{yn(combined.get('manual_review_needed'))}",
        "",
        "## 最終獨立分數",
        "",
        f"- `HW6(code)`：`{combined.get('hw6_code_score')}` / 100",
        f"- `HW6(圖)`：`{combined.get('hw6_figure_score')}` / 100",
        "",
        "## HW6(code，程式) 分數拆解",
        "",
        *score_table(HW6_CODE_FIELDS, code),
        f"| HW6(code) 總分 | {code.get('hw6_code_score')} | 100 |",
        "",
        "## HW6(code，程式) 扣分標籤",
        "",
        *tag_summary_lines(code_tags),
        "",
        "## HW6(code，程式) 扣分明細",
        "",
        *deduction_table(rows_for_tags(code_tags, code_deductions), hw6=True),
        "",
        "## HW6(code，程式) 證據說明",
        "",
        f"- 中文備註：{note_zh(code.get('notes', ''))}",
        f"- 證據等級：`{code.get('evidence_level')}`",
        "- 程式分數只評估實作是否完成、是否正確、是否可驗證；不以圖像美觀程度加分。",
        "",
        "## HW6(圖，圖像) 分數拆解",
        "",
        *score_table(HW6_FIGURE_FIELDS, figure),
        f"| HW6(圖) 總分 | {figure.get('hw6_figure_score')} | 100 |",
        "",
        "## HW6(圖，圖像) 扣分標籤",
        "",
        *tag_summary_lines(figure_tags),
        "",
        "## HW6(圖，圖像) 扣分明細",
        "",
        *deduction_table(rows_for_tags(figure_tags, figure_deductions), hw6=True),
        "",
        "## HW6(圖，圖像) 證據說明",
        "",
        f"- 中文備註：{note_zh(figure.get('notes', ''))}",
        f"- 證據等級：`{figure.get('evidence_level')}`",
        "- 圖像分數只評估計算圖、已學得濾波器、中間特徵圖與圖像可稽核性；不以版面漂亮程度取代必要證據。",
        "",
        "## 交叉規則提醒",
        "",
        "- 如果計算圖與程式不一致，程式端與圖像端都需要依對應項目扣分。",
        "- 準確率達標不代表程式可自動滿分；架構、momentum、計算圖與程式一致性證據仍需成立。",
        "- 圖很完整不代表圖像分數可自動滿分；必須是真正已學得濾波器與中間特徵圖，且可與提交內容對應。",
        "- 沒有證據或證據無法驗證時，不給必要項目滿分。",
        "",
        "## 給學生的簡短說明",
        "",
        f"本次 HW6 以兩個獨立分數呈現：`HW6(code)` 為 `{combined.get('hw6_code_score')}/100`，`HW6(圖)` 為 `{combined.get('hw6_figure_score')}/100`。程式分數依架構、計算圖與程式一致性、訓練法、結果與證據評定；圖像分數依計算圖、已學得濾波器、中間特徵圖與可稽核性評定。非滿分項目已在上方列出扣分標籤與原因。",
        "",
        "## TA / 教師稽核說明",
        "",
        "本中文檔是英文原始稽核紀錄的台灣繁體中文版本；英文原件仍保留作為歷史來源。本檔不新增新的評分判斷，只把既有程式 / 圖像分數 CSV 與扣分紀錄轉成可讀的中文稽核紀錄。",
        "",
    ]
    return "\n".join(lines)


def write_or_print(path: Path, text: str, apply: bool) -> None:
    print(f"{'write' if apply else 'would write'}: {path.relative_to(ROOT)}")
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def generate_hw5(apply: bool) -> int:
    scores = read_csv(ROOT / "grading" / "hw5" / "scores.csv")
    deductions = group_by(read_csv(ROOT / "grading" / "hw5" / "deduction_log.csv"), "student_id")
    out_dir = ROOT / "grading" / "hw5" / "student_notes_zh_tw"
    readme = "\n".join([
        "# HW5 學生評分紀錄（繁體中文）",
        "",
        "本資料夾由 `scripts/generate_zh_tw_student_notes.py` 產生。",
        "英文原始稽核檔仍保留在 `grading/hw5/student_notes/`。",
        "中文檔只翻譯與重排既有分數 CSV / 扣分紀錄，不新增新的評分判斷。",
        "",
    ])
    write_or_print(out_dir / "README.md", readme, apply)
    for row in scores:
        student_id = row["student_id"]
        write_or_print(out_dir / f"{student_id}.md", render_hw5(row, deductions.get(student_id, [])), apply)
    return len(scores)


def generate_hw6(apply: bool) -> int:
    combined_rows = read_csv(ROOT / "grading" / "hw6" / "combined_summary.csv")
    code_by_id = {row["student_id"]: row for row in read_csv(ROOT / "grading" / "hw6" / "code_scores.csv")}
    figure_by_id = {row["student_id"]: row for row in read_csv(ROOT / "grading" / "hw6" / "figure_scores.csv")}
    code_deductions = group_by(read_csv(ROOT / "grading" / "hw6" / "code_deduction_log.csv"), "student_id")
    figure_deductions = group_by(read_csv(ROOT / "grading" / "hw6" / "figure_deduction_log.csv"), "student_id")
    out_dir = ROOT / "grading" / "hw6" / "feedback_zh_tw"
    readme = "\n".join([
        "# HW6 學生評分回饋（繁體中文）",
        "",
        "本資料夾由 `scripts/generate_zh_tw_student_notes.py` 產生。",
        "英文原始稽核檔仍保留在 `grading/hw6/feedback/`。",
        "中文檔只翻譯與重排既有雙分數 CSV / 扣分紀錄，不新增新的評分判斷。",
        "",
    ])
    write_or_print(out_dir / "README.md", readme, apply)
    for row in combined_rows:
        student_id = row["student_id"]
        name = row["student_name"]
        safe_name = name.replace("/", "_")
        write_or_print(
            out_dir / f"{student_id}_{safe_name}.md",
            render_hw6(
                row,
                code_by_id[student_id],
                figure_by_id[student_id],
                code_deductions.get(student_id, []),
                figure_deductions.get(student_id, []),
            ),
            apply,
        )
    return len(combined_rows)


def write_report(hw5_count: int, hw6_count: int, apply: bool) -> None:
    report = "\n".join([
        "# 繁體中文學生評分檔產生報告",
        "",
        f"產生時間：`{GENERATED_AT}`",
        "",
        "## 結果",
        "",
        f"- HW5 中文學生評分紀錄：`{hw5_count}` 份",
        f"- HW6 中文學生評分回饋：`{hw6_count}` 份",
        "",
        "## 輸出位置",
        "",
        "- `grading/hw5/student_notes_zh_tw/`",
        "- `grading/hw6/feedback_zh_tw/`",
        "",
        "## 原則",
        "",
        "- 英文原始檔不覆蓋。",
        "- 中文檔使用台灣繁體中文撰寫。",
        "- 分數、扣分標籤與扣分理由均來自既有 CSV / 扣分紀錄。",
        "- 本次產生不新增新的評分判斷。",
        "",
    ])
    write_or_print(ROOT / "reports" / "zh_tw_student_notes_generation_report.md", report, apply)


def main() -> int:
    args = parse_args()
    hw5_count = 0
    hw6_count = 0
    if args.homework in {"hw5", "all"}:
        hw5_count = generate_hw5(args.apply)
    if args.homework in {"hw6", "all"}:
        hw6_count = generate_hw6(args.apply)
    write_report(hw5_count, hw6_count, args.apply)
    if not args.apply:
        print("Dry-run only. Re-run with --apply to write files.")
    print(f"Summary: hw5={hw5_count}, hw6={hw6_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
