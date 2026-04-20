# CYBERSEC 2026 Slide Blueprint

Baseline: existing `v0.9` 23-slide deck.

Rule: no filler slides. Every slide must support at least one of: trust, repairability, evidence, clinical continuity, or the audience's next action.

Timing target: reach slide 23 by `27:50`, finish spoken content by `28:30`, keep `1:30` buffer.

## Slide-Level Design Rules

- One slide, one controlling message.
- Dense slides are allowed only as public-download references; the speaker still speaks one spine.
- Slide 2 is required organizer compliance, not part of the narrative arc.
- Do not add proprietary code, sensitive client details, private hospital details, student grading data, or patent-sensitive mechanics.
- If a slide causes overtime, cut spoken detail before deleting the slide, except in the emergency version.
- No recommendation is accepted unless it explains the audience-cognition purpose and rubric contribution.
- Avoid decorative AI/security formulas: no circuit wallpaper, no unexplained icon grids, no outline-only slide that consumes stage time, no contact-only close.

## Slide Acceptance Gate

Before a slide is accepted, it must answer five questions:

| Gate | Required Answer | If It Fails |
| --- | --- | --- |
| Audience job | What should the audience understand, feel, or decide after this slide? | Rewrite objective or remove slide |
| Scoring job | Which rubric categories does this slide improve? | Remove unsupported recommendation |
| Visual job | Why is the chosen visual form better than bullets for this idea? | Replace with process, contrast, architecture, metric, or roadmap form |
| Timing job | Why does this slide deserve its speaking time? | Cut spoken detail or merge in emergency route |
| Memory job | Does it reinforce product scale, evidence logic, Patch SLA, or first 90 days? | Reframe around one of the talk's durable mental models |

Bullets are acceptable only when they expose evidence, decision options, timing, or action sequence. A slide with decorative bullets but no decision value should be redesigned as a diagram or cut.

## Canonical Slide Plan

### 1. AI 軟體醫材的資安實戰

- Slide objective: Establish speaker identity, conference setting, and professional seriousness.
- Core message: This is a practical talk about turning FDA 524B, threat modeling, and Patch SLA into AI SaMD product work.
- Audience understanding: The talk will be concrete and evidence-oriented, not a broad AI security lecture.
- Recommended visual form: Title slide.
- Recommendation justification: A restrained title slide protects Structure and Narrative Design and Stage Presence by opening with authority and context.
- On screen: Title, speaker name/affiliation, CYBERSEC 2026 Healthcare Security Forum, date/time/place.
- Not on screen: Outline paragraph, long biography, sponsor-style claims.
- Speaking time: `0:10`.
- Transition in: Walk on calmly; let the title land.
- Transition out: `關鍵字看起來很多，但今天我只想留下三件事：信任、修補、證據。`
- Rubric support: Structure and Narrative Design, Delivery Quality (Language and Voice Expression), Stage Presence, Audience Impact.

### 2. Required CYBERSEC Disclaimer

- Slide objective: Satisfy organizer requirement without damaging the opening rhythm.
- Core message: Official disclaimer is acknowledged and visible.
- Audience understanding: This is a formal conference artifact with public-use boundaries.
- Recommended visual form: Required full-slide disclaimer image.
- Recommendation justification: Treating this as a compliance beat protects Stage Rhythm and Time Control; overexplaining it would weaken the opening hook.
- On screen: Official CYBERSEC disclaimer image only.
- Not on screen: Speaker commentary, interpretation, extra legal explanation.
- Speaking time: `0:20`.
- Transition in: `這是大會必要的 disclaimer。`
- Transition out: `接下來我們直接進入今天真正的問題。`
- Rubric support: Structure and Narrative Design, Stage Rhythm and Time Control, Visual Design of Slides.

### 3. 開場：你賣的不是模型

- Slide objective: Reframe AI SaMD from model output to accountable clinical system.
- Core message: The product being sold is a trustworthy, patchable, auditable medical system, not only a model.
- Audience understanding: Model accuracy is insufficient once the product touches clinical workflow.
- Recommended visual form: Contrast / thesis slide.
- Recommendation justification: Contrast makes the reframing memorable and gives the audience the first mental model.
- On screen: `你賣的不是模型` plus three anchors: trust, patch, evidence.
- Not on screen: Long SaMD taxonomy, regulatory clauses, model performance metrics.
- Speaking time: `1:20`.
- Transition in: `很多 AI 團隊一開始會說：我們只是提供模型。`
- Transition out: `所以我們先看 2026 年的大環境為什麼讓這件事更急。`
- Rubric support: Structure and Narrative Design, Content Depth and Value, Delivery Quality (Language and Voice Expression), Audience Impact.

### 4. 2026 趨勢：AI 不只是模型，而是基礎設施

- Slide objective: Use macro AI/security trends to justify full-stack medical AI security.
- Core message: AI security has moved from model protection to system-stack protection.
- Audience understanding: Medical AI inherits risk from runtime, infrastructure, supply chain, and updates.
- Recommended visual form: Three-layer stack or market-signal bridge.
- Recommendation justification: The stack format prevents trend content from becoming hype and ties macro signals to product responsibility.
- On screen: Model / Runtime / Infrastructure as the dominant visual; short trend cues only.
- Not on screen: Vendor recap, product screenshots, hype language.
- Speaking time: `1:10`.
- Transition in: `2026 年很有意思，AI 的語言正在從模型變成基礎設施。`
- Transition out: `這不是抽象趨勢；在醫療場域，資安事件已經會變成照護中斷。`
- Rubric support: Content Depth and Value, Structure and Narrative Design, Audience Impact.

### 5. 為什麼是現在：資安事件已經變成照護中斷

- Slide objective: Establish urgency without fearmongering.
- Core message: Healthcare cyber incidents affect care delivery, operations, and vendor trust.
- Audience understanding: Cybersecurity in healthcare is a continuity-of-care issue, not only an IT issue.
- Recommended visual form: Incident consequence slide.
- Recommendation justification: Consequence framing creates relevance while avoiding sensationalism.
- On screen: Three consequence labels: clinic closure, hospital disruption, vendor dependency.
- Not on screen: Graphic attack imagery, unverifiable breach detail, long news timeline.
- Speaking time: `1:00`.
- Transition in: `為什麼現在要談？因為醫療資安已經不只是後台問題。`
- Transition out: `要管理這件事，我們需要一張簡單的產品地圖。`
- Rubric support: Content Depth and Value, Audience Impact, Stage Rhythm and Time Control.

### 6. 四種產品尺度：風險會跟架構一起長大

- Slide objective: Give the audience the central map for the talk.
- Core message: Every added product layer adds attack surface and evidence burden.
- Audience understanding: Risk scope must be determined by product architecture.
- Recommended visual form: Framework / architecture ladder.
- Recommendation justification: The ladder becomes the talk's navigational spine and supports pacing because later sections point back to it.
- On screen: Model only -> Model + viewer -> Platform/database -> Connected medical system.
- Not on screen: Full threat lists for every layer, compliance tables, tool names.
- Speaking time: `1:20`.
- Transition in: `請大家先記四層就好。`
- Transition out: `有了這張地圖，我們再看法規到底在要求什麼。`
- Rubric support: Structure and Narrative Design, Content Depth and Value, Visual Design of Slides, Audience Impact.

### 7. 法規要的是證據，不是口號

- Slide objective: Translate regulation into evidence logic.
- Core message: FDA, TFDA, and NIST all point toward traceable lifecycle risk management.
- Audience understanding: Compliance is a chain of evidence, not a slogan.
- Recommended visual form: Evidence-chain slide.
- Recommendation justification: The evidence chain converts regulatory abstraction into an actionable sequence.
- On screen: Risk -> Control -> Test -> Fix -> Evidence.
- Not on screen: Full legal quotations, long standard-number lists, unreadable regulatory text.
- Speaking time: `1:10`.
- Transition in: `我用一句話講法規：法規要的是證據，不是口號。`
- Transition out: `先從 FDA 524B，用商業語言講就很直接。`
- Rubric support: Content Depth and Value, Structure and Narrative Design, Delivery Quality (Language and Voice Expression).

### 8. FDA 524B：一句商業語言

- Slide objective: Make FDA 524B understandable to business and product audiences.
- Core message: Connected cyber devices must prepare monitoring, patching, disclosure, and SBOM evidence before market entry.
- Audience understanding: Postmarket responsibility begins before product launch.
- Recommended visual form: Regulation-to-business translation slide.
- Recommendation justification: Translation prevents legal recitation and makes FDA 524B legible to executives, PMs, and engineers.
- On screen: Monitor, Patch, Disclose, SBOM.
- Not on screen: Clause-by-clause law reading.
- Speaking time: `1:10`.
- Transition in: `FDA 524B 可以講得很法律，也可以講得很商業。`
- Transition out: `但審查者不會只看一份掃描報告。`
- Rubric support: Content Depth and Value, Delivery Quality (Language and Voice Expression), Audience Impact.

### 9. FDA 2025 Cybersecurity Guidance：審查者會看什麼

- Slide objective: Explain what credible submission-oriented cybersecurity evidence looks like.
- Core message: Reviewers look for connected traceability across risk, architecture, controls, tests, and finding decisions.
- Audience understanding: Documents are only useful if they connect decisions.
- Recommended visual form: Traceability process slide.
- Recommendation justification: Traceability is the scoring-critical insight of the regulatory section.
- On screen: Threat model, architecture, controls, testing, finding disposition.
- Not on screen: Exhaustive guidance requirements or tiny checklists.
- Speaking time: `1:30`.
- Transition in: `審查者不會只看工具有沒有跑。`
- Transition out: `回到台灣，TFDA 的 AI/ML SaMD 視角也在問類似的證據問題。`
- Rubric support: Content Depth and Value, Structure and Narrative Design, Stage Rhythm and Time Control.

### 10. TFDA 視角：AI/ML SaMD 要說清楚模型與證據

- Slide objective: Localize the talk for Taiwan medical AI product teams.
- Core message: AI/ML SaMD must explain intended use, data, model behavior, validation, and usage limitations.
- Audience understanding: Cybersecurity must connect to model documentation and software validation.
- Recommended visual form: Local regulatory lens slide.
- Recommendation justification: A Taiwan-specific lens increases relevance while keeping the slide tied to evidence artifacts.
- On screen: Intended use, data, algorithm, V&V, clinical performance.
- Not on screen: Full TFDA submission form detail.
- Speaking time: `1:20`.
- Transition in: `在台灣，AI 模型不是黑盒子傳奇。`
- Transition out: `NIST 的價值，是把這些工程問題翻譯成管理語言。`
- Rubric support: Content Depth and Value, Audience Impact, Delivery Quality (Language and Voice Expression).

### 11. NIST 視角：給老闆聽得懂的管理語言

- Slide objective: Give leaders and managers a shared governance vocabulary.
- Core message: NIST frameworks translate cybersecurity into ownership, process, detection, response, and recovery.
- Audience understanding: Security becomes manageable when leaders, PM, RD, QA, and regulatory teams share language.
- Recommended visual form: Governance framework slide.
- Recommendation justification: Governance language gives managers a role in the talk and turns engineering work into accountable ownership.
- On screen: Govern, Identify, Protect, Detect, Respond, Recover.
- Not on screen: Full NIST control catalog.
- Speaking time: `1:00`.
- Transition in: `NIST 不替產品拿證照，但它讓公司可以講同一種語言。`
- Transition out: `接下來，我把 AI security 再壓成三層。`
- Rubric support: Content Depth and Value, Delivery Quality (Language and Voice Expression), Audience Impact.

### 12. AI Security Stack：Model / Runtime / Infrastructure

- Slide objective: Simplify AI security into a practical 2026 mental model.
- Core message: Medical AI security must cover model, runtime, infrastructure, and update chain.
- Audience understanding: Protecting the model alone is not enough.
- Recommended visual form: Three-layer stack diagram.
- Recommendation justification: A stack diagram compresses complex AI-security scope into a memorable model.
- On screen: Model: provenance/evaluation; Runtime: isolation/secrets; Infrastructure: identity/updates.
- Not on screen: Confidential-computing deep dive, cloud architecture overload.
- Speaking time: `1:30`.
- Transition in: `Model security 問一件事；runtime security 問另一件事；infrastructure 又是第三件事。`
- Transition out: `現在回到四種產品尺度，從最小的 model 開始。`
- Rubric support: Structure and Narrative Design, Content Depth and Value, Visual Design of Slides.

### 13. Scale 1：只有 AI Model

- Slide objective: Define minimum credible security evidence for the smallest product scope.
- Core message: Model-only products still need provenance, dependency, SBOM, update, and limitation evidence.
- Audience understanding: Small scope is not zero responsibility.
- Recommended visual form: Product-scale card / checklist slide.
- Recommendation justification: A tightly scoped card shows that even the smallest product needs evidence without overstating obligations.
- On screen: Artifact, data lineage, dependency/SBOM, update boundary.
- Not on screen: Platform controls that do not apply yet.
- Speaking time: `1:30`.
- Transition in: `如果你真的只有 AI model，範圍最小，但不是沒有資安。`
- Transition out: `一旦加上 viewer，世界就變了。`
- Rubric support: Content Depth and Value, Audience Impact.

### 14. Scale 2：AI Model + Viewer

- Slide objective: Show how UI, files, and local behavior expand risk.
- Core message: The viewer adds parser, file, UI, cache, export, and misuse risks.
- Audience understanding: Attackers may target the product wrapper, not the model.
- Recommended visual form: Before/after attack-surface slide.
- Recommendation justification: The before/after form makes the added viewer risk visible and prevents this section from becoming repetitive.
- On screen: File parser, UI, local storage, output limitation.
- Not on screen: Sensitive medical image examples or real client UI.
- Speaking time: `1:30`.
- Transition in: `攻擊者不一定攻擊模型，他可以攻擊 viewer。`
- Transition out: `平台化之後，資安就變成公司營運風險。`
- Rubric support: Content Depth and Value, Audience Impact.

### 15. Scale 3：Viewer + Platform + Database

- Slide objective: Connect platform features to business and privacy risk.
- Core message: Once the product has accounts, APIs, roles, cloud, logs, and database, security becomes operating risk.
- Audience understanding: Platform risk is business risk, not only engineering risk.
- Recommended visual form: Platform architecture risk map.
- Recommendation justification: Mapping platform components to risks shows why platform security becomes business and privacy risk.
- On screen: Identity, RBAC, API, database, audit log, backup.
- Not on screen: Real database schemas, credentials, private architecture.
- Speaking time: `1:30`.
- Transition in: `有平台，就有身份、權限、資料庫和 API。`
- Transition out: `進入醫院網路後，這件事再升級一次。`
- Rubric support: Content Depth and Value, Audience Impact.

### 16. Scale 4：完整 Connected AI Medical System

- Slide objective: Show when cybersecurity clearly becomes patient-safety and operational-continuity risk.
- Core message: Connected systems can affect hospital networks, clinical workflow, updates, and multiple patients.
- Audience understanding: The evidence burden grows sharply when the product enters clinical infrastructure.
- Recommended visual form: Connected clinical system diagram.
- Recommendation justification: The clinical system diagram shows why hospital integration changes risk severity and evidence needs.
- On screen: PACS/HIS, hospital LAN/VLAN, update server, remote service, multi-patient impact.
- Not on screen: Specific hospital network maps or deployment details.
- Speaking time: `1:30`.
- Transition in: `當產品進入醫院網路，事情再升級一次。`
- Transition out: `所以我想把這句話放在中間：Cyber Safety is Patient Safety。`
- Rubric support: Content Depth and Value, Audience Impact, Structure and Narrative Design.

### 17. Medical AI Trend：Cyber Safety Is Patient Safety

- Slide objective: Create the emotional and ethical center of the talk.
- Core message: Medical AI cybersecurity is shared risk across vendor, hospital, and clinical workflow.
- Audience understanding: Security is not only device protection; it is care-continuity protection.
- Recommended visual form: Full-screen phrase / clinical continuity slide.
- Recommendation justification: A full-screen phrase creates the emotional peak and gives the audience one sentence to remember.
- On screen: `Cyber Safety Is Patient Safety` plus vendor-hospital-continuity cues.
- Not on screen: New technical frameworks or dense lists.
- Speaking time: `1:15`.
- Transition in: `醫療 AI 出事時，受影響的不只是模型績效。`
- Transition out: `接下來進入最實作的部分：怎麼測，怎麼修，怎麼留下證據。`
- Rubric support: Audience Impact, Delivery Quality (Language and Voice Expression), Stage Presence.

### 18. White-Box Testing：從內部看見可修的問題

- Slide objective: Explain white-box testing as early, cheap, traceable risk reduction.
- Core message: White-box work finds internal problems before release and creates repairable evidence.
- Audience understanding: White-box testing is not paperwork; it helps engineering fix earlier.
- Recommended visual form: Internal inspection / evidence output slide.
- Recommendation justification: Framing white-box testing around outputs keeps the slide technical and useful instead of becoming a tool catalog.
- On screen: Code/config, supply chain, AI pipeline, finding list, SBOM.
- Not on screen: Long tool catalog, code snippets, secret examples.
- Speaking time: `1:40`.
- Transition in: `White-box testing 的精神很簡單：在 release 前，從內部把便宜可修的問題找出來。`
- Transition out: `Black-box testing 問的是另一個問題：外部真的打得進來嗎？`
- Rubric support: Content Depth and Value, Audience Impact.

### 19. Black-Box Testing：從攻擊者視角驗證真實暴露

- Slide objective: Contrast black-box testing against white-box testing.
- Core message: Black-box testing validates externally visible attack paths and real exploitable exposure.
- Audience understanding: White-box and black-box are complementary, not substitutes.
- Recommended visual form: Contrast slide.
- Recommendation justification: Contrast is the clearest way to separate white-box and black-box value.
- On screen: Entry points, abuse paths, scope/method, severity, retest evidence.
- Not on screen: Exploit instructions or sensitive attack recipes.
- Speaking time: `1:40`.
- Transition in: `Black-box testing 的問題不同。`
- Transition out: `但 finding 出來以後，真正的治理才開始。`
- Rubric support: Content Depth and Value, Stage Rhythm and Time Control, Delivery Quality (Language and Voice Expression).

### 20. Patch SLA 與漏洞處理流程

- Slide objective: Deliver the operational climax.
- Core message: Every finding needs intake, triage, decision, patch, retest, notice, and archive.
- Audience understanding: Vulnerability management is the core operating process behind credible security.
- Recommended visual form: Finding journey / process flow.
- Recommendation justification: A process flow makes Patch SLA the operational climax and shows how findings become governed decisions.
- On screen: Intake -> Triage -> Decision -> Patch -> Retest -> Archive; four decision outcomes.
- Not on screen: Complex ticket-system screenshot, vendor SLA claims, legal disclaimers.
- Speaking time: `1:35`.
- Transition in: `如果只能帶走一個營運流程，我會選 Patch SLA。`
- Transition out: `我知道很多小團隊會覺得這太大，所以最後把它壓成最小可做版本。`
- Rubric support: Content Depth and Value, Audience Impact, Structure and Narrative Design, Delivery Quality (Language and Voice Expression).

### 21. Small Team Playbook：不要一開始就蓋大型制度

- Slide objective: Make the talk actionable for small and growing teams.
- Core message: Start with a minimum viable evidence folder and automate the cheap checks.
- Audience understanding: They can begin without building a large compliance department.
- Recommended visual form: Practical checklist slide.
- Recommendation justification: The checklist is justified here because it is an action gate, not filler.
- On screen: Evidence package, CI gates, outsource where independence matters.
- Not on screen: Enterprise governance bureaucracy, unrealistic tool stack.
- Speaking time: `1:20`.
- Transition in: `小團隊不需要第一天就蓋大型制度。`
- Transition out: `把它放進時間表，就是 30、60、90 天。`
- Rubric support: Audience Impact, Content Depth and Value, Stage Rhythm and Time Control.

### 22. 30 / 60 / 90 天落地路線圖

- Slide objective: Convert the talk into an executable plan.
- Core message: Make risk visible first, then make evidence creation repeatable.
- Audience understanding: The first 90 days should produce inventory, threat model, gates, workflow, penetration test, Patch SLA, and release evidence.
- Recommended visual form: Roadmap slide.
- Recommendation justification: The roadmap converts the talk into an implementation sequence and strengthens practical usefulness.
- On screen: 30: inventory/SBOM/data flow; 60: threat model/CI gates/finding workflow; 90: pen test/Patch SLA/CVD/retest evidence.
- Not on screen: Long project plan, cost estimate, consulting proposal.
- Speaking time: `1:20`.
- Transition in: `重點不是三個月變完美，而是三個月後公司開始自動留下可信證據。`
- Transition out: `最後，我們回到今天的第一個問題。`
- Rubric support: Audience Impact, Structure and Narrative Design, Content Depth and Value.

### 23. 結語：先建立信任，再面對稽核

- Slide objective: Close with a memorable principle and no new material.
- Core message: Build security into the product first; regulatory documents then become evidence of real work.
- Audience understanding: Mature teams know how to prove, repair, and track each risk.
- Recommended visual form: Conclusion slide.
- Recommendation justification: A minimal conclusion slide protects memorability and Stage Presence by preventing administrative clutter.
- On screen: `先把安全做進產品，法規文件才會自然長出來。`
- Not on screen: Contact-heavy slide, new technical points, new references.
- Speaking time: `0:40`.
- Transition in: `今天我們從一個 model 開始，走到 connected medical system。`
- Transition out: Stop. Thank the audience. Do not add extra content.
- Rubric support: Structure and Narrative Design, Delivery Quality (Language and Voice Expression), Stage Presence, Audience Impact.

## Non-Filler Audit

| Slide Range | Function | Why It Exists |
| --- | --- | --- |
| 1-3 | Trust contract | Establish topic, compliance, and thesis |
| 4-6 | Relevance and map | Explain why the issue matters now and give the audience a framework |
| 7-12 | Evidence compass | Convert regulation and AI security into operating logic |
| 13-17 | Product-scale substance | Show risk growth as product architecture grows |
| 18-20 | Engineering response | Explain testing and finding governance |
| 21-23 | Field implementation | Give small-team path, roadmap, and memorable close |

## Emergency Cut Map

If forced to deliver in `18:00-20:00`, keep only:

1. Slide 1 title.
2. Slide 2 disclaimer.
3. Slide 3 thesis.
4. Slide 6 four product scales.
5. Slide 7 evidence chain.
6. Slide 12 AI security stack.
7. Slide 17 patient-safety peak.
8. Slide 20 Patch SLA.
9. Slides 21-23 playbook, roadmap, close.

Never cut slide 20 or slide 23. Those carry the operating model and final memory.
