# CYBERSEC 2026 Speaker Manuscript Architecture

Purpose: turn the v0.9 deck into a stage-ready 30-minute talk.

Stage language: Taiwan Traditional Chinese, with selected English technical terms where they are standard in industry.

Performance target: `28:30` spoken content plus `1:30` buffer.

Core emotional contract: serious but solvable; technically credible but not intimidating.

## 1. Whole-Talk Speaking System

### Speaker Identity On Stage

Sound like a clinician-engineer / security translator: calm, precise, practical, and evidence-driven. The audience should feel that the speaker has done the hard sorting work for them.

This is a professional conference posture. Do not announce the structure mechanically, do not read the slides as proof of preparation, and do not use `next I will introduce` transitions unless the transition adds meaning. The posture is: state the decision problem, translate the evidence, then show the operating move.

### Repeated Core Lines

- `信任、修補、證據`
- `你賣的不是模型。`
- `法規要的是證據，不是口號。`
- `Cyber Safety is Patient Safety.`
- `沒有 decision，就沒有治理；沒有證據，就沒有信任。`
- `先把安全做進產品，法規文件才會自然長出來。`

### Global Delivery Rules

- Speak the first sentence of each major section slowly.
- Pause after each core line; do not explain over the audience's absorption moment.
- On dense slides, speak only the controlling message and one example.
- Use framework names as proof, not as the story.
- Never apologize for technical content. Translate it.
- Do not add new material after the closing line.
- Every delivery choice must protect a scoring category: Structure and Narrative Design for transitions, Content Depth and Value for technical precision, Stage Rhythm and Time Control for pace, Delivery Quality for language control, Stage Presence for authority, or Audience Impact for memorability.
- Avoid classroom phrasing such as `this slide talks about`, `let me introduce`, and `in conclusion I learned`. Replace it with conference phrasing: `the decision problem is`, `the risk changes here`, `the evidence has to connect`, and `the first operating move is`.

### Delivery Quality Gate

Every speaking cue must be actionable on stage. A cue is acceptable only if it tells the speaker what to do with time, voice, emphasis, or audience attention.

| Cue Type | Acceptable Form | Rubric Protected |
| --- | --- | --- |
| Transition | Names why the next section is necessary | Structure and Narrative Design |
| Technical explanation | Translates a framework into a product decision or evidence artifact | Content Depth and Value |
| Pace cue | Says where to slow, accelerate, pause, or reset attention | Stage Rhythm and Time Control |
| Voice cue | Names the intended tone: authoritative, conversational, decisive, or calm | Delivery Quality (Language and Voice Expression) |
| Presence cue | Names where to use eye contact, stillness, or controlled gesture | Stage Presence |
| Memory cue | Reinforces a durable phrase or operating model | Audience Impact |

Reject cues that only say `be confident`, `explain clearly`, or `make it engaging` without specifying the stage behavior that creates that effect.

## 2. Section-Level Intent

| Section | Slides | Intent | Audience State | Tone | Delivery Cue |
| --- | --- | --- | --- | --- | --- |
| Opening contract | 1-3 | Reframe the talk from model to accountable medical system | Curious, deciding whether this is useful | Calm, precise | Slow down on `信任、修補、證據` |
| Why now / map | 4-6 | Create urgency and give the central map | Alert but may fear hype | Controlled urgency | Point to four product scales as the talk map |
| Evidence compass | 7-12 | Translate regulation and frameworks into evidence workflow | At risk of cognitive overload | Authoritative, simplifying | Use `risk -> control -> test -> fix -> evidence` |
| Product scale | 13-17 | Show how risk grows with architecture | Following the map, needs concrete examples | Practical, explanatory | Repeat `這一層多了什麼風險？` |
| Testing and Patch SLA | 18-20 | Convert security work into operating process | Ready for implementation | Strong, decisive | Pause before Patch SLA line |
| Playbook and close | 21-23 | Give action path and final memory | Wants useful next step | Encouraging, confident | End cleanly after final sentence |

## 3. Slide-Level Delivery Cues

### Slides 1-3: Opening Contract

- Speaking objective: Earn trust and frame the talk as practical evidence design.
- Emotional tone: Calm confidence.
- Slow down: `今天我只想留下三件事：信任、修補、證據。`
- Pause: After `你賣的不是模型`.
- Conversational mode: Describe how teams say `我們只是提供模型`.
- Authority mode: Define the product as a system that must be trusted, patched, and audited.
- Absorption beat: One beat after `醫師看到的是結果，病人承受的是後果`.

### Slides 4-6: Why Now And The Map

- Speaking objective: Move from trend to urgency to a usable map.
- Emotional tone: Alert but not alarmist.
- Increase energy: Slide 5 care-disruption examples.
- Slow down: Slide 6 four product scales.
- Rhetorical question: `如果產品每多一層，風險也多一層，那證據是不是也要跟著多一層？`
- Reset sentence: `不要記所有細節，先記四層就好。`

### Slides 7-12: Evidence Compass

- Speaking objective: Make regulation operational.
- Emotional tone: Authoritative and simplifying.
- Slow down: `法規要的是證據，不是口號。`
- Pause: After `risk -> control -> test -> fix`.
- Authority mode: FDA 524B and FDA 2025 expectations.
- Conversational mode: NIST as `給老闆聽得懂的管理語言`.
- Absorption beat: After slide 12, let the audience accept model/runtime/infrastructure before returning to product scale.

### Slides 13-17: Product-Scale Deepening

- Speaking objective: Show the audience how to scope security work without panic.
- Emotional tone: Practical and structured.
- Accelerate: Repeat the same slide pattern so the section does not drag.
- Decelerate: Slide 16, where connected systems become patient-safety risk.
- Strong line: `產品能力變強，攻擊面也變大。`
- Pause: After `Cyber Safety is Patient Safety`.
- Audience reaction time: Slide 17 should breathe; it is the emotional center.

### Slides 18-20: Testing And Patch SLA

- Speaking objective: Connect testing outputs to remediation governance.
- Emotional tone: Engineering clarity.
- Contrast: White-box sees internal repairable problems; black-box validates external exploitable exposure.
- Increase energy: Slide 20 Patch SLA.
- Strategic silence: After `如果只能帶走一個營運流程，我會選 Patch SLA。`
- Strong line: `沒有 decision，就沒有治理；沒有證據，就沒有信任。`

### Slides 21-23: Implementation And Close

- Speaking objective: Make the talk useful tomorrow morning.
- Emotional tone: Constructive and confident.
- Conversational mode: `我知道很多小團隊聽到 FDA、TFDA、NIST 會覺得壓力很大。`
- Reset sentence: `不需要第一天就做成大型制度。`
- Slow down: `30 天、60 天、90 天`.
- Final pause: After `先把安全做進產品，法規文件才會自然長出來。`
- Stop condition: Say thanks and stop; do not add new technical content.

## 4. Structured Manuscript Outline

### Act 1: The Shift

1. Title and disclaimer.
2. Establish contract: this is not a law lecture; it is a product risk map.
3. Reframe: AI SaMD teams do not only sell models; clinical sites receive systems.
4. Introduce the three anchors: trust, patch, evidence.

### Act 2: The Pressure

1. AI is becoming infrastructure.
2. Healthcare cyber incidents can become care-disruption events.
3. Four product scales explain why risk grows.

### Act 3: The Evidence Compass

1. FDA, TFDA, and NIST ask for traceable evidence.
2. FDA 524B means postmarket responsibilities must be planned before launch.
3. FDA 2025 guidance expects architecture, threat model, testing, and finding disposition.
4. TFDA asks AI/ML SaMD teams to explain intended use, model/data evidence, and validation.
5. NIST gives management language.
6. AI stack = model / runtime / infrastructure.

### Act 4: The Product-Scale Walkthrough

1. Scale 1: model evidence.
2. Scale 2: viewer and file/UI risks.
3. Scale 3: platform, account, API, and database risks.
4. Scale 4: connected clinical system and multi-patient impact.
5. Synthesis: cyber safety is patient safety.

### Act 5: The Operating System

1. White-box testing finds early repairable internal problems.
2. Black-box testing validates external attack paths.
3. Patch SLA turns findings into governance decisions.
4. Small teams begin with evidence folder, CI gates, and outsourced independent review where needed.
5. `30/60/90` roadmap.
6. Close: build trust before audit.

## 5. Semi-Scripted Version

### Opening: Slides 1-3

各位好，我是林家聖。今天的題目是 AI 軟體醫材的資安實戰。

關鍵字看起來很多：FDA 524B、Threat Modeling、Patch SLA。但今天我只想留下三件事：信任、修補、證據。

這張是大會必要的 disclaimer，我在這邊停一下，讓大家看見。接下來我們直接進入今天真正的問題。

很多 AI 團隊一開始會說：我們只是提供模型。可是醫療現場不會這樣看。醫師看到的是結果，病人承受的是後果，公司要負責的是整個使用情境。

所以第一個轉念是：你賣的不是模型。你賣的是一個在醫療情境中可被信任、可被修補、可被稽核的系統。這就是今天所有法規、測試和治理的起點。

### Why Now And The Map: Slides 4-6

2026 年很有意思。整個 AI 產業的語言正在改變。大家不只談模型多大、跑分多高，而是談 AI 怎麼被部署、怎麼被管理、怎麼被更新、怎麼被保護。

對醫療 AI 來說，這件事更直接。因為醫療不是把模型放上雲端就結束；它會接資料、接 workflow、接醫院網路，最後接到病人照護。

為什麼現在要談？因為醫療資安已經不只是 IT 後台的問題。勒索攻擊可以讓診所關閉、手術取消；醫院端系統異常會讓臨床工作降級；供應鏈公司被攻擊也可能影響全球客戶。

這些案例不是要製造恐慌，而是提醒我們：當 AI 進入醫療，cyber incident 很快就會變成 care disruption。

要管理這件事，請大家先記四層就好：AI model、model 加 viewer、viewer 加平台和資料庫、完整 connected AI medical system。

每加一層，產品能力變強，攻擊面也變大。法規要看的，不是你說自己安全，而是你能不能拿出跟這個尺度相稱的證據。

### Evidence Compass: Slides 7-12

我用一句話講法規：法規要的是證據，不是口號。

FDA、TFDA、NIST 用的語言不完全一樣，但方向很一致：你要知道風險在哪裡，你要有控制措施，你要測試，你要修補，你要留下紀錄。

FDA 524B 如果用商業語言講，就是：如果你的醫材會連線，上市前就要準備好上市後怎麼監控漏洞、怎麼修補、怎麼告知客戶，以及你的軟體裡到底有哪些元件。

審查者不會只看一份掃描報告。他們會問：你的 threat model 在哪裡？architecture 怎麼畫？控制措施對應到哪些風險？測試有沒有真的打到攻擊面？每個 finding 最後去哪裡了？

這就是從 risk 到 control，到 test，到 fix 的一條線。這條線接不起來，文件再多也只是資料夾。

回到台灣，TFDA 的 AI/ML SaMD 視角提醒我們：AI 模型不是黑盒子傳奇。你要說清楚 intended use，誰用、在哪裡用、不能怎麼用；資料怎麼來；訓練、驗證、測試怎麼切；臨床性能怎麼證明。

NIST 的價值，是把工程問題翻譯成管理語言。Govern 是誰負責。Identify 是有哪些資產和風險。Protect、Detect、Respond、Recover，讓董事會、PM、RD、法規和客服可以講同一種語言。

接下來我把 AI security 壓成三層：model、runtime、infrastructure。醫療 AI 要安全，這三層不能只挑一層做。

### Product Scale: Slides 13-17

如果你真的只有 AI model，範圍最小，但不是沒有資安。你要保護 model artifact、資料 lineage、dependency、SBOM，以及更新邊界。

一旦加上 viewer，世界就變了。攻擊者不一定攻擊模型，他可以攻擊檔案解析、upload、暫存資料、UI 呈現，甚至攻擊使用者怎麼理解輸出。

平台化之後，資安就變成公司風險。你開始有帳號、角色、API、資料庫、雲端、log、backup。這裡開始是營運風險、法規風險，也是品牌信任風險。

當產品進入醫院網路，事情再升級一次。它可能接 PACS、HIS、醫療設備、遠端服務、更新伺服器。如果這一層出事，可能同時影響多名病人和臨床營運。

所以這句話我希望大家帶走：Cyber Safety is Patient Safety。

醫療 AI 出事時，受影響的不只是模型績效，而是病人、醫院營運、供應商責任與臨床流程。

### Testing And Patch SLA: Slides 18-20

接下來進入最實作的部分。

White-box testing 的精神很簡單：在 release 前，從內部把便宜、可修、可追溯的問題找出來。看 code、看 config、看 secrets、看 dependencies、看 container、看 cloud 設定，也看 AI pipeline 有沒有資料洩漏或更新邊界不清。

Black-box testing 問的是另一個問題：如果我不知道你的原始碼，只從外部看，我能不能打穿產品？能不能繞過登入？能不能上傳奇怪檔案讓 viewer 出錯？能不能把幾個小問題串成一條攻擊路徑？

所以 white-box 是早期修問題，black-box 是 release 或送審前驗證真實暴露。兩個不是互相取代，而是前後接力。

如果只能帶走一個營運流程，我會選 Patch SLA。

真正的資安不是「沒有漏洞」，而是每個漏洞進來後，公司知道誰負責、多久判斷、多久修補、怎麼通知、怎麼重測、證據放哪裡。

這裡的四種結果很重要：fix now、compensate、defer with timeline、non-applicable with rationale。

沒有 decision，就沒有治理；沒有證據，就沒有信任。

### Implementation And Close: Slides 21-23

我知道很多公司聽到 FDA、TFDA、NIST 會覺得壓力很大。但小團隊不需要第一天就蓋大型制度。

先建立 minimum viable regulatory evidence folder：intended use、architecture、data-flow、SBOM、threat model、test reports、vulnerability log、Patch SLA、release history。

然後把便宜的檢查自動化：dependency scan、secret scan、SAST、container scan。需要獨立性的事情，再外包：penetration test、regulatory review、高風險架構 review。

最後把它變成 30、60、90 天。

30 天，先盤點：資產、SBOM、資料流程、intended use、已知漏洞。

60 天，建立節奏：threat model、CI security gates、finding workflow、customer security note。

90 天，做外部驗證：penetration test、Patch SLA、CVD process、retest evidence、release history。

今天我們從一個 model 開始，走到 connected medical system。每往前一步，產品更有價值，也更需要被信任、被修補、被稽核。

所以我想用一句話結束：先把安全做進產品，法規文件才會自然長出來。

真正成熟的團隊，不是文件最多的團隊，而是每一個風險都知道怎麼證明、怎麼修、怎麼追的團隊。謝謝大家。

## 6. Concise Speaker Cue Version

### 0:00-1:50 Opening

- `信任、修補、證據`
- Disclaimer: stop briefly, move on.
- `你賣的不是模型`
- Product = trusted, patchable, auditable clinical system.

### 1:50-5:20 Why Now / Map

- AI is now infrastructure.
- Healthcare cyber = care disruption.
- Four scales:
  - Model
  - Viewer
  - Platform/database
  - Connected medical system
- `風險會跟架構一起長大`

### 5:20-13:00 Evidence Compass

- `法規要的是證據，不是口號`
- FDA 524B = monitor, patch, disclose, SBOM.
- FDA 2025 = threat model, architecture, testing, finding disposition.
- TFDA = intended use, data, algorithm, V&V, clinical performance.
- NIST = management language.
- AI stack = model / runtime / infrastructure.

### 13:00-20:15 Product Scale

- Scale 1: artifact, data lineage, dependency, update.
- Scale 2: parser, file, UI, cache, output limitation.
- Scale 3: identity, API, database, audit, backup.
- Scale 4: PACS/HIS, hospital network, update server, multi-patient impact.
- `Cyber Safety is Patient Safety`

### 20:15-25:10 Testing / Patch SLA

- White-box = internal, early, repairable.
- Black-box = external attack path, real exposure.
- Patch SLA = intake, triage, decision, patch, retest, archive.
- `沒有 decision，就沒有治理；沒有證據，就沒有信任`

### 25:10-28:30 Playbook / Close

- Minimum evidence folder.
- Automate cheap checks.
- Outsource independence.
- `30/60/90`.
- `先把安全做進產品，法規文件才會自然長出來`
- Stop.

## 7. Delivery Markers For Rehearsal

| Marker | Where | Action |
| --- | --- | --- |
| Slow | Slide 3 | Before and after `你賣的不是模型` |
| Pause | Slide 6 | After naming the four scales |
| Authority | Slides 7-9 | Regulation as evidence logic |
| Conversational | Slide 11 | Explain NIST as shared company language |
| Energy | Slide 17 | Make patient safety line memorable |
| Silence | Slide 20 | After choosing Patch SLA as the one process |
| Summary | Slide 22 | `30/60/90` should sound executable |
| Final stop | Slide 23 | End after thanks; no extra technical points |
