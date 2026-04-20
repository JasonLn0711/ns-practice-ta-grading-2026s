# CYBERSEC 2026 Detailed Talk Execution Spec

Purpose: convert the strategic package into a production-grade talk plan for slide editing, rehearsal, and final delivery.

This file is the next layer after `slide_blueprint.md` and `speaker_manuscript_outline.md`. It does not replace them. It tells the speaker and slide editor exactly what each slide must do on screen, what must be said, what must be cut when time is tight, and which scoring categories the decision protects.

## 1. Whole-Talk Control Spine

The talk must feel like one professional risk briefing, not a sequence of cybersecurity mini-lectures.

Core control sentence:

> AI SaMD risk grows when a model becomes a clinical system; credible teams earn trust by producing evidence, making vulnerability decisions, and protecting clinical continuity before audit or incident pressure arrives.

Use this sentence to test every slide. If a slide does not advance product scale, evidence, vulnerability decision-making, or clinical continuity, it must be tightened or cut.

## 2. Audience Journey

| Moment | Audience Question | Talk Answer | Rubric Protection |
| --- | --- | --- | --- |
| Slides 1-3 | Is this worth my attention? | This is not a model talk; it is a product-trust talk | Structure and Narrative Design, Stage Presence |
| Slides 4-6 | Why now, and how do I track the scope? | AI is infrastructure; medical cyber risk becomes care disruption; use four product scales | Content Depth and Value, Audience Impact |
| Slides 7-12 | What do regulators and frameworks actually require? | They require traceable evidence: risk, control, test, fix, archive | Content Depth and Value, Delivery Quality |
| Slides 13-17 | How does scope change with architecture? | Each layer adds attack surface and evidence burden | Structure and Narrative Design, Visual Design of Slides |
| Slides 18-20 | What does the team actually do? | Test early, validate externally, govern findings with Patch SLA | Content Depth and Value, Audience Impact |
| Slides 21-23 | What should I do tomorrow? | Build minimum evidence, automate cheap checks, run a 30/60/90 plan | Audience Impact, Stage Rhythm and Time Control |

## 3. Detailed Slide Execution Plan

### Slide 1. AI 軟體醫材的資安實戰

- Screen contract: Formal, restrained title slide. The title must be the dominant signal; speaker name and affiliation should be secondary.
- Spoken spine: `各位好，我是林家聖。今天的題目是 AI 軟體醫材的資安實戰。`
- Stage cue: Stand still, face audience, do not gesture yet.
- Cut rule: Never expand biography here. If extra context is needed, prove credibility through later content.
- Scoring job: Stage Presence and Structure and Narrative Design.
- Justification: A calm title opening frames the talk as a serious professional session rather than a self-introduction segment.

### Slide 2. Required CYBERSEC Disclaimer

- Screen contract: Full official disclaimer image, no added interpretation.
- Spoken spine: `這是大會必要的 disclaimer，我在這裡停一下，讓大家看見。`
- Stage cue: Pause for one beat; do not read the disclaimer.
- Cut rule: Keep at `0:20`; do not explain legal meaning.
- Scoring job: Stage Rhythm and Time Control, Visual Design of Slides.
- Justification: Compliance is handled cleanly without stealing energy from the opening.

### Slide 3. 開場：你賣的不是模型

- Screen contract: One dominant phrase: `你賣的不是模型`. Three small anchors: `Trust`, `Patch`, `Evidence`.
- Spoken spine: `你賣的是一個在醫療情境中可被信任、可被修補、可被稽核的系統。`
- Stage cue: Slow down before `你賣的不是模型`; pause after the phrase.
- Cut rule: Do not add SaMD taxonomy or model-performance examples.
- Scoring job: Structure and Narrative Design, Delivery Quality, Audience Impact.
- Justification: This is the first memory point and the core reframing that prevents the talk from becoming a generic AI security talk.

### Slide 4. 2026 趨勢：AI 不只是模型，而是基礎設施

- Screen contract: Three-layer visual: `Model`, `Runtime`, `Infrastructure`. Minimal trend cues only.
- Spoken spine: `2026 年 AI 的語言正在從模型變成基礎設施。`
- Stage cue: Medium pace. Use one hand gesture downward through the stack.
- Cut rule: Do not become a GTC recap or vendor trend summary.
- Scoring job: Content Depth and Value, Structure and Narrative Design.
- Justification: The slide earns the right to discuss runtime, supply chain, and update risk without drifting into hype.

### Slide 5. 為什麼是現在：資安事件已經變成照護中斷

- Screen contract: Three consequence labels: `clinic closure`, `system disruption`, `vendor dependency`.
- Spoken spine: `當 AI 進入醫療，cyber incident 很快就會變成 care disruption。`
- Stage cue: Add controlled urgency; do not sound dramatic.
- Cut rule: Use one consequence sentence, not a long incident story.
- Scoring job: Audience Impact, Content Depth and Value.
- Justification: The audience must feel relevance before the regulatory section begins.

### Slide 6. 四種產品尺度：風險會跟架構一起長大

- Screen contract: Four-step product ladder: `Model -> Viewer -> Platform -> Connected Medical System`.
- Spoken spine: `每加一層，產品能力變強，攻擊面也變大，證據需求也變大。`
- Stage cue: Slow down and point through the ladder once.
- Cut rule: Never skip this map in any version of the talk.
- Scoring job: Structure and Narrative Design, Visual Design of Slides, Audience Impact.
- Justification: This is the navigation map for the whole talk and the main defense against audience confusion.

### Slide 7. 法規要的是證據，不是口號

- Screen contract: Evidence chain: `Risk -> Control -> Test -> Fix -> Evidence`.
- Spoken spine: `法規要的是證據，不是口號。`
- Stage cue: Pause after the line; then walk the chain in one sentence.
- Cut rule: Do not name every standard here.
- Scoring job: Content Depth and Value, Delivery Quality.
- Justification: Converts regulation into an operational sequence, protecting technical seriousness without legal overload.

### Slide 8. FDA 524B：一句商業語言

- Screen contract: Four obligations as large verbs: `Monitor`, `Patch`, `Disclose`, `SBOM`.
- Spoken spine: `如果你的醫材會連線，上市前就要準備上市後怎麼監控、修補、告知，以及說清楚軟體組成。`
- Stage cue: Authoritative, concise.
- Cut rule: No clause-by-clause explanation.
- Scoring job: Content Depth and Value, Audience Impact.
- Justification: Makes the U.S. regulatory trigger understandable to executives and product teams.

### Slide 9. FDA 2025 Cybersecurity Guidance：審查者會看什麼

- Screen contract: Traceability diagram connecting `architecture`, `threat model`, `controls`, `tests`, `finding disposition`.
- Spoken spine: `審查者不會只看工具有沒有跑；他會看風險、控制、測試和 finding 最後有沒有接起來。`
- Stage cue: Slow and precise; this is a cognitive-heavy slide.
- Cut rule: Cut examples first; preserve traceability.
- Scoring job: Content Depth and Value, Stage Rhythm and Time Control.
- Justification: This is the main evidence-quality point in the regulatory block.

### Slide 10. TFDA 視角：AI/ML SaMD 要說清楚模型與證據

- Screen contract: Local evidence lens: `intended use`, `data`, `algorithm`, `V&V`, `clinical performance`.
- Spoken spine: `AI 模型不是黑盒子傳奇；醫療產品要說清楚誰用、在哪裡用、資料怎麼來、限制在哪裡。`
- Stage cue: Conversational but serious; make it feel locally relevant.
- Cut rule: Do not list forms or submission mechanics.
- Scoring job: Audience Impact, Content Depth and Value.
- Justification: Localizes the talk for Taiwan while staying connected to evidence.

### Slide 11. NIST 視角：給老闆聽得懂的管理語言

- Screen contract: Governance verbs: `Govern`, `Identify`, `Protect`, `Detect`, `Respond`, `Recover`.
- Spoken spine: `NIST 的價值，是讓董事會、PM、RD、法規和客服可以講同一種風險語言。`
- Stage cue: More conversational; this is a recovery beat after FDA/TFDA detail.
- Cut rule: Do not open the control catalog.
- Scoring job: Stage Rhythm and Time Control, Audience Impact.
- Justification: Brings managers back into the talk and reduces cognitive load.

### Slide 12. AI Security Stack：Model / Runtime / Infrastructure

- Screen contract: Three horizontal bands, each with one label and two keywords.
- Spoken spine: `醫療 AI 要安全，model、runtime、infrastructure 不能只挑一層做。`
- Stage cue: Use progressive reveal if available; otherwise gesture layer by layer.
- Cut rule: Confidential computing and attestation stay as Q&A material only.
- Scoring job: Visual Design of Slides, Content Depth and Value.
- Justification: Prepares the audience to understand why the four product scales require different evidence.

### Slide 13. Scale 1：只有 AI Model

- Screen contract: Tight evidence card: `artifact`, `data lineage`, `dependency/SBOM`, `update boundary`.
- Spoken spine: `範圍最小，不代表沒有責任；至少要說清楚 model 從哪裡來、依賴什麼、怎麼更新。`
- Stage cue: Efficient; this begins the repeated scale pattern.
- Cut rule: Do not discuss platform controls.
- Scoring job: Content Depth and Value, Stage Rhythm and Time Control.
- Justification: Establishes that evidence starts even before the product becomes a full platform.

### Slide 14. Scale 2：AI Model + Viewer

- Screen contract: Before/after attack surface: model alone vs model with viewer.
- Spoken spine: `攻擊者不一定攻擊模型，他可以攻擊 viewer：檔案解析、暫存、輸出呈現和使用者理解。`
- Stage cue: Slight energy increase; make the risk feel concrete.
- Cut rule: No real medical image examples.
- Scoring job: Content Depth and Value, Audience Impact.
- Justification: Shows why product wrapping changes security scope.

### Slide 15. Scale 3：Viewer + Platform + Database

- Screen contract: Platform risk map with `identity`, `RBAC`, `API`, `database`, `audit log`, `backup`.
- Spoken spine: `一有平台，就有身份、權限、API、資料庫和營運責任。`
- Stage cue: Decisive; speak to executives and PMs here.
- Cut rule: Do not show schemas, credentials, or architecture secrets.
- Scoring job: Content Depth and Value, Audience Impact.
- Justification: Converts platform security into business and trust risk.

### Slide 16. Scale 4：完整 Connected AI Medical System

- Screen contract: Connected clinical-system diagram: `PACS/HIS`, hospital network, update server, remote service, multi-patient impact.
- Spoken spine: `當產品進入醫院網路，資安就不只是產品保護，而是臨床營運連續性。`
- Stage cue: Decelerate. This is the bridge to the emotional peak.
- Cut rule: Do not show hospital-specific topology.
- Scoring job: Content Depth and Value, Stage Presence.
- Justification: Establishes why cybersecurity becomes patient-safety and continuity risk.

### Slide 17. Medical AI Trend：Cyber Safety Is Patient Safety

- Screen contract: Full-screen phrase: `Cyber Safety Is Patient Safety`.
- Spoken spine: `醫療 AI 出事時，受影響的不只是模型績效，而是病人、醫院營運、供應商責任與臨床流程。`
- Stage cue: Stop moving; say the line slowly; hold silence after.
- Cut rule: Never add a new framework here.
- Scoring job: Audience Impact, Stage Presence, Delivery Quality.
- Justification: This is the emotional center and should create the most memorable conference line.

### Slide 18. White-Box Testing：從內部看見可修的問題

- Screen contract: Internal evidence outputs: code/config, supply chain, AI pipeline, finding list, SBOM.
- Spoken spine: `White-box testing 的價值，是在 release 前找到便宜、可修、可追溯的問題。`
- Stage cue: Engineering clarity; no drama.
- Cut rule: Do not list tools beyond categories.
- Scoring job: Content Depth and Value.
- Justification: Makes testing feel like evidence production, not vendor tooling.

### Slide 19. Black-Box Testing：從攻擊者視角驗證真實暴露

- Screen contract: Contrast with white-box: external entry points, abuse paths, severity, retest evidence.
- Spoken spine: `Black-box testing 問的是：從外部看，真的打得進來嗎？幾個小問題能不能串成攻擊路徑？`
- Stage cue: Crisp contrast; faster than slide 18.
- Cut rule: No exploit recipe.
- Scoring job: Delivery Quality, Content Depth and Value.
- Justification: Clarifies complementary testing roles and prevents tool confusion.

### Slide 20. Patch SLA 與漏洞處理流程

- Screen contract: Finding journey: `Intake -> Triage -> Decision -> Patch -> Retest -> Archive`; decision node visually dominant.
- Spoken spine: `沒有 decision，就沒有治理；沒有證據，就沒有信任。`
- Stage cue: Strategic silence after `如果只能帶走一個營運流程，我會選 Patch SLA。`
- Cut rule: Never cut this slide; cut earlier examples instead.
- Scoring job: Content Depth and Value, Audience Impact, Structure and Narrative Design.
- Justification: This is the operational climax; it converts the talk into a governable process.

### Slide 21. Small Team Playbook：不要一開始就蓋大型制度

- Screen contract: Minimum viable evidence package plus automation/outsourcing split.
- Spoken spine: `小團隊不需要第一天就蓋大型制度；先建立最小可信證據資料夾。`
- Stage cue: Conversational; reduce pressure.
- Cut rule: If short on time, mention only evidence folder, cheap automation, and independent review.
- Scoring job: Audience Impact, Stage Rhythm and Time Control.
- Justification: Makes the talk useful to small teams and founders, not only mature organizations.

### Slide 22. 30 / 60 / 90 天落地路線圖

- Screen contract: Three-step roadmap with no heavy boxes: `30 inventory`, `60 workflow`, `90 validation`.
- Spoken spine: `重點不是三個月變完美，而是三個月後公司開始自動留下可信證據。`
- Stage cue: Measured cadence: 30, pause; 60, pause; 90, pause.
- Cut rule: Keep one output per time bucket if rushed.
- Scoring job: Audience Impact, Structure and Narrative Design.
- Justification: Converts insight into a concrete implementation path.

### Slide 23. 結語：先建立信任，再面對稽核

- Screen contract: One closing sentence, no new information.
- Spoken spine: `先把安全做進產品，法規文件才會自然長出來。`
- Stage cue: Slow, centered, no extra technical point after the final line.
- Cut rule: Never add a second ending.
- Scoring job: Audience Impact, Stage Presence, Delivery Quality.
- Justification: A clean close improves memorability and protects the final impression score.

## 4. Slide Editing Priorities

| Priority | Slides | Edit Decision | Why It Matters |
| --- | --- | --- | --- |
| 1 | 3, 6, 17, 20, 23 | Make these five slides visually distinctive and phrase-led | They carry the talk's memory architecture |
| 2 | 7-12 | Convert framework content into evidence chains and simple lenses | Prevents the talk from becoming a regulation list |
| 3 | 13-16 | Use a consistent scale pattern but vary the risk visual per layer | Makes repetition feel intentional instead of monotonous |
| 4 | 18-20 | Make testing and Patch SLA look like one workflow | Protects the operational climax |
| 5 | 21-22 | Keep the roadmap compact and executable | Preserves the practical value score |

## 5. Rehearsal Scoring Moments

| Timestamp Target | Must Be True | If Not True |
| --- | --- | --- |
| `1:50` | The audience has heard `你賣的不是模型` and the three anchors | Cut opening explanation |
| `5:20` | The four product scales are clear | Slow slide 6; cut slide 5 detail |
| `13:00` | Regulation has been translated into evidence logic | Cut standard details; preserve evidence chain |
| `20:15` | Product scale has reached patient-safety meaning | Accelerate scale details; keep slide 17 |
| `25:10` | Patch SLA has landed as the operating process | Cut testing examples before cutting Patch SLA |
| `28:30` | Final sentence has ended cleanly | Cut from slides 8, 9, 13-16 next run |

## 6. Anticipated Q&A Bridges

Use these only after the talk. Do not insert them into the main 30-minute run.

| Question Type | Short Answer Spine | Why This Protects Credibility |
| --- | --- | --- |
| `Do small teams really need all this?` | Start with minimum viable evidence: intended use, architecture, data flow, SBOM, threat model, finding log, Patch SLA | Shows practicality without lowering the standard |
| `Is this only for FDA submissions?` | No; FDA gives a strong evidence pattern, but the operating logic also helps Taiwan teams, hospital procurement, and customer trust | Prevents over-narrow regulatory framing |
| `White-box or black-box first?` | White-box earlier to fix cheap internal problems; black-box later to validate exposed attack paths before release or submission | Gives a decision rule, not a tool preference |
| `How much detail should be public?` | Public deck can show process and categories; keep proprietary code, client architecture, private hospital details, and exploit recipes out | Signals professional safety judgment |
| `What is the first Monday action?` | Build the evidence folder and write the first finding-decision rule before buying more tools | Reinforces the talk's practical close |
