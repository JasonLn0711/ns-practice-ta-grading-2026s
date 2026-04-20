# CYBERSEC 2026 Main Presentation Strategy

Talk: `AI 軟體醫材的資安實戰：從美國 FDA 524B 規範到 Threat Modeling 與 Patch SLA 的完整落地`

Target: `30:00` conference session, designed as `28:30` spoken content plus `1:30` buffer.

Language strategy: English for design and evaluation artifacts; Taiwan Traditional Chinese for stage language and rehearsal cues.

Public-safety rule: keep the public deck free of proprietary code, sensitive client examples, private hospital details, student grading data, and patent-sensitive implementation mechanics.

## Conference Quality Contract

Every design decision must pass this gate before it enters the deck, manuscript, or rehearsal plan.

| Constraint | Operational Enforcement | Rubric Protection |
| --- | --- | --- |
| No non-specific presentation advice | A recommendation must name a slide range, audience cognition problem, timing effect, or scoring category; otherwise cut it | Structure and Narrative Design, Content Depth and Value |
| No classroom-style speaking posture | Speaking cues must sound like a conference risk briefing: decision problem, evidence translation, operating move | Delivery Quality (Language and Voice Expression), Stage Presence |
| No low-value bullet accumulation | Bullets are allowed only for evidence, decision choices, timing paths, or action steps; otherwise use contrast, process, or architecture visuals | Visual Design of Slides, Stage Rhythm and Time Control |
| Every section must be actionable | Each section must create a slide decision, cut rule, rehearsal cue, scoring rule, or audience-facing action | Content Depth and Value, Audience Impact |
| Every slide recommendation must be justified | Each slide must explain its objective, audience understanding, visual form, and rubric support | Structure and Narrative Design, Visual Design of Slides |
| Every major suggestion must tie to the rubric | If a suggestion cannot name the scoring category it improves, it is not part of the official package | All categories |
| Premium, serious, technical tone | Use evidence maps, architecture, process flows, and decision rules; avoid decorative spectacle and pitch-deck language | Content Depth and Value, Visual Design of Slides, Stage Presence |
| Avoid template-like AI/security slide structure | Do not use ornamental circuit backgrounds, unexplained icon grids, abstract "AI brain" imagery, or outline-only slides | Visual Design of Slides, Audience Impact |
| Prioritize clarity, credibility, pacing, and memorability | Prefer one strong mental model and a few repeated lines over adding more material | Structure and Narrative Design, Stage Rhythm and Time Control, Audience Impact |

Practical enforcement: before accepting any slide or paragraph, ask what score it protects and what audience problem it solves. If neither answer is clear, rewrite or remove it.

## 1. Context And Failure-Mode Analysis

### Likely Audience And Conference Context

This is a CYBERSEC 2026 healthcare-security forum talk for a mixed professional audience: medical-device leaders, SaMD founders, product managers, security engineers, regulatory/quality teams, hospital IT/security staff, and clinical stakeholders. The audience will expect technical seriousness, practical relevance, and a visible bridge between regulation, engineering, and healthcare operations.

The talk is not a class report and not a research paper reading. It must perform like a professional risk briefing: clear thesis, strong pacing, credible evidence, practical operating model, and a close that gives the audience a next move.

### 30-Minute Constraints

- The audience has enough time for one serious mental model, not many disconnected frameworks.
- Heavy regulatory content must be translated into product decisions quickly.
- Technical credibility must come from traceable artifacts and operating processes, not from tool-name density.
- The ending must not be rushed; the final `30/60/90` path and Patch SLA memory must survive any time cut.

### Failure Modes To Design Against

| Failure Mode | Why It Hurts The Score | Design Countermeasure |
| --- | --- | --- |
| Too much detail | The audience loses the narrative and evaluators penalize rhythm | Use one spoken spine per dense slide; move details into public-download/reference meaning |
| Weak narrative | The talk feels like a list of regulations and tools | Use one arc: regulation -> threat -> architecture -> engineering response -> field implementation |
| Overloaded technical slides | Visual score drops and the speaker reads | One-slide-one-message; diagrams for architecture/process; bullets only when they expose decisions |
| Not enough practical relevance | Managers and founders cannot act | End every major technical block with what the team should produce or decide |
| Poor pacing | Heavy sections exhaust attention | Follow regulatory and architecture-heavy blocks with simplification slides and reset sentences |
| Forgettable ending | Audience remembers the topic but not the action | Close with Patch SLA, `30/60/90`, and one final principle |

## 2. Presentation Design Brief

### Talk Title Candidates

1. AI SaMD Cybersecurity in Practice: From FDA 524B to Threat Modeling and Patch SLA
2. Beyond the Model: Building Trust, Evidence, and Patchability into AI Medical Devices
3. Cyber Safety Is Patient Safety: A Practical Security Model for AI SaMD
4. From Model to Clinical System: How AI Medical Product Risk Grows
5. The Evidence Path: Threat Modeling, Testing, and Patch SLA for AI Medical Devices
6. Before the Audit: How Small Teams Can Build Credible AI SaMD Cybersecurity
7. Trust Before Submission: Practical Cybersecurity for AI Medical Software

### Positioning Statement

This talk helps healthcare AI and medical-device teams move from abstract cybersecurity and regulatory language into a concrete operating model: product architecture, threat modeling, testing, vulnerability decisions, Patch SLA, evidence archive, and first 90 days of execution.

### Intended Audience Segments

| Segment | Primary Concern | What The Talk Must Give Them |
| --- | --- | --- |
| Medical-device and SaMD executives | Submission risk, customer trust, budget, liability | A business-readable map of what must be funded and governed |
| Security engineers / consultants | Threat model, attack surface, testing scope, remediation | A product-scale framework that avoids shallow checklist work |
| Product managers / founders | What to do first without creating bureaucracy | A minimum viable evidence package and `30/60/90` path |
| Regulatory / quality teams | Traceability, V&V, risk controls, evidence archive | A bridge from FDA/TFDA language to engineering artifacts |
| Hospital / clinical stakeholders | Continuity of care, vendor risk, patient safety | A way to discuss cybersecurity as clinical operating risk |

### Audience Knowledge Assumptions

- They know cybersecurity matters, but many do not know how AI SaMD product architecture changes the evidence burden.
- They may have heard terms such as SBOM, threat modeling, vulnerability management, penetration testing, and Zero Trust without seeing how those artifacts connect.
- Some may confuse model accuracy with product trustworthiness.
- Some may treat regulation as paperwork instead of an engineering evidence system.

### Primary Audience Pain Points

- "We know security matters, but what should we do first?"
- "How does FDA 524B change our product process?"
- "How do we avoid paying for isolated scans that do not improve submission readiness?"
- "How do we explain security budget to leadership without sounding alarmist?"
- "How can a small team build credible evidence without a large compliance department?"

### Desired Audience Takeaways

- AI SaMD cybersecurity is not only model security; it expands across runtime, infrastructure, supply chain, hospital deployment, and clinical continuity.
- Regulation asks for evidence, not slogans.
- Product architecture determines the right testing and documentation scope.
- White-box testing, black-box testing, SBOM, threat modeling, Patch SLA, and vulnerability logs are connected parts of one operating system.
- Small teams can start with a minimum viable evidence folder and a finding-decision workflow.

### Core Thesis

AI medical software earns trust not by claiming it has no vulnerabilities, but by proving that risk is owned, findings are decided, patches are controlled, evidence is preserved, and clinical continuity is considered before incidents and audits arrive.

### Why This Topic Matters Now

- AI medical products are becoming infrastructure, not isolated models.
- FDA Section 524B and the 2025 final cybersecurity guidance raise expectations for monitoring, patching, disclosure, SBOM evidence, and premarket cybersecurity content.
- Medical cyber incidents increasingly affect clinical service continuity, not only IT back-office operations.
- Healthcare AI teams need a practical bridge from regulation to engineering workflow.

### What Makes This Talk Different

- It uses product scale as the organizing principle: model, viewer, platform/database, connected clinical system.
- It treats regulation as evidence design rather than legal recitation.
- It turns findings into decisions: fix now, compensate, defer with timeline, or non-applicable with rationale.
- It ends with a practical `30/60/90` roadmap instead of a vague warning.

### Speaker Advantage / Authority Angle

The speaker can credibly stand at the intersection of biomedical AI research, SaMD governance, cybersecurity risk thinking, and attacker-perspective analysis. The authority should be demonstrated through structured judgment and practical translation, not through inflated claims.

### Risk Factors And Mitigation

| Risk | Why It Weakens The Talk | Mitigation |
| --- | --- | --- |
| Regulatory detail becomes a legal lecture | Audience loses the action logic | Translate FDA/TFDA/NIST into `risk -> control -> test -> fix -> evidence` |
| AI infrastructure trend drifts into trend recap | Topic focus weakens | Use trends only to justify model/runtime/infrastructure scope |
| Technical bullets become a PDF reading | Rhythm and visual scores drop | Speak one spine; leave detail as reference |
| Vendor-like tone | Trust drops | Emphasize evidence, tradeoffs, and decision logic |
| Weak close | Impact score drops | End on Patch SLA, first 90 days, and trust before audit |
| Overtime | Roadmap gets compressed | Cut incident detail and scale-slide examples first; never cut Patch SLA or close |

## 3. Rubric-To-Design Translation Matrix

| Category | Weight | Design Goal | Observable Success Criteria | Design Tactics | Failure Patterns | Avoid | Slide Influence | Speaking Influence |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| Structure and Narrative Design | 20 | Make the talk feel inevitable: each section answers the question created by the previous section | Audience can summarize the arc as model -> system -> evidence -> testing -> patch workflow -> first 90 days | Use product scale as the map; repeat the thesis at section turns | Sections feel like separate mini lectures | Mechanical outline slides, unexplained framework jumps | Every slide has one controlling message; section slides function as maps | Use transition sentences that name why the next section exists |
| Content Depth and Value | 20 | Deliver technically serious but usable insight | Technical listeners hear substance; managers hear decision logic | Use FDA/TFDA/NIST as evidence anchors; connect tools to outputs and decisions | Tool-name dumping, regulatory name-dropping, vague inspiration | Unsupported claims, private examples, unbounded compliance promises | Dense slides may carry reference detail, but hierarchy must show the single claim | Explain operating meaning before naming frameworks |
| Stage Rhythm and Time Control | 15 | Hold attention through pace variation and load balance | Heavy sections are followed by simplification or action | Peaks at slides 3, 6, 17, 20, 23; recovery after regulatory block | Same tempo for 30 minutes, reading bullets | Long legal explanations, multi-minute examples | Use visual reset slides after dense content | Slow on thesis, speed through lists, pause after memorable lines |
| Delivery Quality (Language and Voice Expression) | 15 | Sound precise, calm, and controlled | Short sentences, clear terms, low filler | Define acronyms only when needed; speak in business/clinical consequences | Overexplaining, apologetic tone, rushing | "This is complicated", "I will quickly go through", hedging | Slides support speech instead of replacing it | Use Taiwan Traditional Chinese with industry-standard English terms |
| Visual Design of Slides | 10 | Make meaning visible within three seconds | Audience can identify the point before the speaker explains | One message per slide, strong diagrams, high contrast | Text-heavy classroom style, decorative AI imagery | Tiny legal text, random icon grids, ornamental gradients | Use diagrams for architecture/process; bullets only for decisions | Do not narrate decoration; point only to meaning-bearing visuals |
| Stage Presence | 10 | Controlled authority without overperformance | Speaker appears calm, prepared, and serious | Stand still during thesis; gesture only for architecture/process | Fidgeting, looking at slides, weak ending posture | Wandering, filler gestures, mic-start rush | Slides must allow eye contact; no paragraphs that force reading | Use pauses and direct eye contact at opening, slide 17, slide 20, closing |
| Audience Impact | 10 | Leave a useful mental model and next action | Audience remembers product scale, Patch SLA, and first 90 days | Memorable lines plus executable roadmap | Interesting but not actionable | Ending with admin clutter or new material | Closing slide is principle/action, not contact-only | End with a short final line and stop |

## 4. 30-Minute Time Architecture

### Normal Version: 28:30 Content + 1:30 Buffer

| Segment | Slides | Time | Cumulative | Reasoning |
| --- | --- | ---: | ---: | --- |
| Opening contract | 1-3 | `1:50` | `1:50` | Fast compliance, then clear reframing: this is not a model-accuracy talk |
| Why now / map | 4-6 | `3:30` | `5:20` | Establish urgency and give the four-scale map before detail begins |
| Regulatory evidence compass | 7-12 | `7:40` | `13:00` | Heavy cognitive section; translate frameworks into one evidence logic |
| Product-scale deepening | 13-17 | `7:15` | `20:15` | Technical core; risk grows with architecture |
| Testing and Patch SLA | 18-20 | `4:55` | `25:10` | Operational climax; connect testing to remediation governance |
| Implementation and close | 21-23 | `3:20` | `28:30` | Leave audience with small-team playbook, roadmap, and final thesis |
| Buffer | Q&A handoff / AV slip / applause | `1:30` | `30:00` | Protect conference timing and prevent rushed ending |

### Emotional Peaks

- Slide 3: reframing peak, `你賣的不是模型`.
- Slide 6: cognitive map peak, four product scales.
- Slide 17: ethical/clinical peak, `Cyber Safety is Patient Safety`.
- Slide 20: operating climax, every finding needs owner, decision, patch, retest, archive.
- Slide 23: closing peak, trust before audit.

### Cognitive Heavy Sections

- Slides 7-12: FDA/TFDA/NIST plus AI security stack.
- Slides 13-16: four product scales.
- Slides 18-20: testing and vulnerability workflow.

### Simplification / Recovery Beats

- Slide 6 turns news/trend into one map.
- Slide 12 turns frameworks into model/runtime/infrastructure.
- Slide 17 converts architecture into patient-safety meaning.
- Slide 22 converts the talk into a `30/60/90` path.

### Likely Attention Drops And Recovery

| Risk Moment | Why Attention Drops | Recovery Sentence |
| --- | --- | --- |
| After slide 8 | FDA detail can feel legal | `Let me translate this back into product work.` |
| During slides 13-16 | Four scale slides can feel repetitive | `At this layer, the question is simple: what new risk entered the product?` |
| Before slide 20 | Testing detail may feel like a tool catalog | `If you remember only one operating process, remember Patch SLA.` |
| Final two minutes | Audience expects a routine close | Give first 90 days and stop cleanly |

### Safe Version

- Keep all 23 slides.
- Speak content to `27:45`.
- Cut one example from slide 5, one detailed list from slide 9, and one detail from each scale slide.
- Preserve slides 6, 17, 20, 21, 22, and 23.

### Slightly Rushed Version

- Target `25:30` content.
- Slides 1-6: finish by `4:45`.
- Slides 7-12: finish by `11:15`.
- Slides 13-17: finish by `18:00`.
- Slides 18-20: finish by `22:30`.
- Slides 21-23: finish by `25:30`.
- Cut detailed framework explanation; speak only operating meaning.

### Compressed Emergency Version

- Target `18:00-20:00`.
- Keep slides 1, 2, 3, 6, 7, 12, 17, 20, 21, 22, 23.
- Skip detailed scale slides by summarizing them on slide 6.
- Compress FDA/TFDA/NIST to: `Regulation is asking for traceable evidence.`
- Keep Patch SLA and the `30/60/90` path because they carry practical value.

## 5. Narrative Architecture

### Chosen Mode

Use `regulation -> threat -> architecture -> engineering response -> field implementation`.

This mode fits the CYBERSEC healthcare forum better than a simple problem-solution story because the audience needs proof of seriousness before practical advice. Regulation gives legitimacy, threat gives urgency, architecture gives cognition, engineering response gives substance, and field implementation creates audience value.

### Opening Strategy

Open with a reframing contract:

> 今天不是一堂法規課。今天是一張產品風險地圖：一個 AI model 怎麼長成醫療系統，風險怎麼跟著長大，公司又要怎麼留下可信的證據。

The audience should feel in the first minute: serious, concrete, manageable.

### Tension / Problem Framing

- AI teams may believe they sell a model.
- Clinical reality receives a system.
- Regulators and hospitals need evidence that the system can be trusted, repaired, audited, and kept operational.

### Development Arc

1. Reframe product responsibility.
2. Show why cyber events now affect care continuity.
3. Give the four-scale map.
4. Translate FDA/TFDA/NIST into evidence logic.
5. Map risk growth across product scale.
6. Explain white-box, black-box, and Patch SLA as one remediation system.
7. Close with a small-team first 90 days.

### Key Transition Points

| Transition | Purpose |
| --- | --- |
| Slide 3 -> 4 | Move from product responsibility to market/security pressure |
| Slide 5 -> 6 | Move from incident urgency to the four-scale map |
| Slide 6 -> 7 | Move from architecture scope to evidence requirements |
| Slide 12 -> 13 | Move from AI stack to concrete product scales |
| Slide 17 -> 18 | Move from patient safety claim to practical testing |
| Slide 20 -> 21 | Move from vulnerability workflow to small-team implementation |

### Climax / Strongest Insight

Slide 20 is the operational climax:

> 沒有 decision，就沒有治理；沒有證據，就沒有信任。

This line converts the talk from security awareness into an operating system for risk ownership.

### Closing Structure

- Recap the journey: model to connected medical system.
- Restate the principle: product scale determines evidence burden.
- Give the first move: minimum evidence folder plus Patch SLA.
- End with trust before audit.

Final takeaway:

> 先把安全做進產品，法規文件才會自然長出來。

## 6. Visual Design Strategy

### Style Direction

Premium conference style: restrained, high-contrast, diagram-led, healthcare/security credible. The deck should feel like an expert product-risk briefing, not a startup pitch deck and not a classroom handout.

### Typography Philosophy

- Large slide titles with one clear claim.
- Body text only where it supports public-download reference use.
- Avoid tiny legal/regulatory text except source cues.
- Use English technical terms selectively where industry-standard: SBOM, Patch SLA, Threat Modeling, Runtime, Infrastructure.

### Color Usage Philosophy

- Use neutral dark/white base with one security/medical accent color.
- Use red only for risk or disruption, not decoration.
- Keep color semantically meaningful: architecture layer, decision node, or urgency.

### Icon / Diagram Philosophy

- Use diagrams for architecture, process, and scale.
- Use icons sparingly; each icon must label a real concept.
- Avoid decorative AI symbols unless they clarify model/runtime/infrastructure.

### Density Control Rules

- Maximum one message per slide.
- Maximum three visible bullet groups on standard slides.
- If a slide has more than 40 words, the speaker must prepare a one-sentence spoken spine and ignore secondary bullets unless needed.
- Use progressive reveal for model/runtime/infrastructure and finding workflow when editing the PPTX.

### How To Avoid Template-Like Slide Feel

- Avoid neon AI brains, random circuit backgrounds, and content-free gradients.
- Use concrete forms: product-scale ladder, evidence trace, testing contrast, finding journey, `30/60/90` roadmap.
- Make layout decisions based on audience cognition, not decoration.

### How To Avoid Over-Designed Marketing Style

- No exaggerated promises.
- No sales funnel visuals.
- No "world-changing" language.
- No stock-photo emotional manipulation.
- Keep authority in evidence, constraints, and implementation decisions.

### Technical Slide Handling

- Every technical slide must answer: `What decision does this help the audience make?`
- If explaining a standard or framework, translate it into product workflow before naming subparts.
- For testing slides, emphasize output artifacts and decisions, not tool catalogs.

## 7. Audience Impact Design

### Earn Trust In The First Minute

- Start calmly.
- Say what the talk is not: not a law lecture, not a vendor demo, not a model-accuracy talk.
- Promise a usable map and a first `30/60/90` path.

### Create Relevance

- Connect medical cyber incidents to care disruption.
- Connect FDA/TFDA evidence expectations to product and business risk.
- Connect small-team constraints to staged implementation.

### Maintain Attention

- Alternate heavy and simple slides.
- Use memorable lines after dense content.
- Use the four-scale map as a recurring anchor.
- Use `what changes at this scale?` as the repeated question for slides 13-16.

### Memorable Moments

- `你賣的不是模型`
- `法規要的是證據，不是口號`
- `Cyber Safety is Patient Safety`
- `沒有 decision，就沒有治理；沒有證據，就沒有信任`
- `先把安全做進產品，法規文件才會自然長出來`

### Examples That Work Best

- Generic medical imaging viewer/product architecture examples.
- Public incident categories: clinic closure, procedure delay, hospital workstation disruption, vendor disruption.
- Workflow artifacts: SBOM, threat model, vulnerability log, retest evidence, customer security note.

### Examples That Weaken Credibility

- Confidential client or hospital details.
- Unverified breach claims.
- Overly dramatic patient-harm scenarios.
- Tool screenshots without explanation of decisions.
- Vendor claims that sound like sales positioning.

### Technical Depth / Accessibility Balance

- Experts should hear the right artifacts and workflow connections.
- Managers should hear ownership, timing, and evidence.
- Non-specialists should remember the four-scale map and first 90 days.

## 8. Source Anchors

- CYBERSEC session page: <https://cybersec.ithome.com.tw/2026/session/4284>
- CYBERSEC speaker page: <https://cybersec.ithome.com.tw/2026/speaker/2060>
- FDA cybersecurity page: <https://www.fda.gov/medical-devices/digital-health-center-excellence/cybersecurity>
- FDA 2025 final guidance PDF: <https://www.fda.gov/files/guidance%20documents/published/GUI00001825-final-PremarketCybersecurity-2025.pdf>
- Local CYBERSEC source bundle: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/planning-everything-track/data/knowledge/personal/sources/2026-04-09-cybersec-2026-speaker-pre-event-notice/source.md`
- Existing v0.9 deck: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/planning-everything-track/data/projects/2026-04-medical-cybersecurity-tfda-fda-industry-deck/current/cybersec-2026-ai-samd-cybersecurity-lin-jia-sheng-organizer-v0.9-20260422.pptx`
- Existing v0.9 speaker notes: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/planning-everything-track/data/projects/2026-04-medical-cybersecurity-tfda-fda-industry-deck/current/cybersec-2026-ai-samd-cybersecurity-lin-jia-sheng-speaker-notes-v0.9-20260422.md`
- Existing v0.9 rehearsal runbook: `/Users/iKev/Desktop/02_Projects_and_Code/everything_on_git/planning-everything-track/data/projects/2026-04-medical-cybersecurity-tfda-fda-industry-deck/current/cybersec-2026-first-rehearsal-runbook-v0.9-20260422.md`
