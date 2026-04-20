# CYBERSEC 2026 Timed Stage Script And Cue Cards

Purpose: provide a clock-safe delivery script for the `30:00` CYBERSEC talk.

Use this file for timed rehearsal after the slide visuals have been checked against `slide_visual_production_spec.md`. It is not a paragraph manuscript. It is a stage-control document: what must be said, when to say it, how to sound, and what to cut when the timer is tight.

## 1. Timing Control Rules

Normal target: `28:30` spoken content plus `1:30` buffer.

Hard checkpoints:

| Checkpoint | Cumulative Time | Must Be Complete |
| --- | ---: | --- |
| Opening thesis | `1:50` | Slides 1-3, including `你賣的不是模型` |
| Product map | `5:20` | Slides 4-6, four product scales clear |
| Evidence compass | `13:00` | Slides 7-12, regulation translated into evidence |
| Product scale | `20:15` | Slides 13-17, patient-safety peak delivered |
| Patch SLA | `25:10` | Slides 18-20, vulnerability workflow delivered |
| Final close | `28:30` | Slides 21-23, final line complete |

If any checkpoint is late by more than `0:30`, cut details immediately from the next flexible slide. Never cut slides 3, 6, 17, 20, or 23.

## 2. Slide-By-Slide Timed Script

### Slide 1. Title

- Timebox: `0:00-0:10`
- Cue card: `Topic. Name. Calm start.`
- Required line: `各位好，我是林家聖。今天的題目是 AI 軟體醫材的資安實戰。`
- Voice move: Calm, low-speed, no rush.
- Cut if late: Nothing; keep to one sentence.
- Rubric protected: Stage Presence, Structure and Narrative Design.

### Slide 2. Disclaimer

- Timebox: `0:10-0:30`
- Cue card: `Disclaimer. Pause. Move on.`
- Required line: `這是大會必要的 disclaimer，我在這裡停一下，讓大家看見。接下來我們直接進入今天真正的問題。`
- Voice move: Neutral and brief.
- Cut if late: Do not add commentary.
- Rubric protected: Stage Rhythm and Time Control.

### Slide 3. 你賣的不是模型

- Timebox: `0:30-1:50`
- Cue card: `Not model. Trust / patch / evidence.`
- Required line: `你賣的不是模型。你賣的是一個在醫療情境中可被信任、可被修補、可被稽核的系統。`
- Supporting line: `醫師看到的是結果，病人承受的是後果，公司要負責的是整個使用情境。`
- Voice move: Slow down before the thesis; pause after it.
- Cut if late: Remove the setup sentence about teams saying `我們只是提供模型`.
- Rubric protected: Structure and Narrative Design, Delivery Quality, Audience Impact.

### Slide 4. AI Is Infrastructure

- Timebox: `1:50-3:00`
- Cue card: `AI now runs as infrastructure.`
- Required line: `2026 年 AI 的語言正在從模型變成基礎設施。對醫療 AI 來說，這代表資安不能停在 algorithm。`
- Supporting line: `它會接 runtime、資料、更新、雲端、供應鏈，最後接到臨床流程。`
- Voice move: Medium pace; gesture down the stack once.
- Cut if late: Remove supply-chain mention; keep model/runtime/infrastructure.
- Rubric protected: Content Depth and Value.

### Slide 5. Care Disruption

- Timebox: `3:00-4:00`
- Cue card: `Cyber incident -> care disruption.`
- Required line: `醫療資安已經不只是 IT 後台問題。當 AI 進入醫療，cyber incident 很快就會變成 care disruption。`
- Supporting line: `診所可能停擺，醫院系統可能降級，供應商也可能變成全院風險。`
- Voice move: Controlled urgency; no alarmism.
- Cut if late: Keep only the required line.
- Rubric protected: Audience Impact, Content Depth and Value.

### Slide 6. Four Product Scales

- Timebox: `4:00-5:20`
- Cue card: `Four scales. Risk grows. Evidence grows.`
- Required line: `請大家先記四層：Model、Viewer、Platform / Database、Connected Medical System。`
- Supporting line: `每加一層，產品能力變強，攻擊面也變大，證據需求也跟著變大。`
- Voice move: Slow and deliberate; point through all four layers.
- Cut if late: Never cut the four layers; cut only the rhetorical question.
- Rubric protected: Structure and Narrative Design, Visual Design of Slides, Audience Impact.

### Slide 7. Evidence, Not Slogans

- Timebox: `5:20-6:30`
- Cue card: `Risk -> control -> test -> fix -> evidence.`
- Required line: `我用一句話講法規：法規要的是證據，不是口號。`
- Supporting line: `你要知道風險在哪裡，有控制措施，有測試，有修補，最後留下可追溯紀錄。`
- Voice move: Authoritative; pause after the required line.
- Cut if late: Do not list frameworks here.
- Rubric protected: Content Depth and Value, Delivery Quality.

### Slide 8. FDA 524B

- Timebox: `6:30-7:40`
- Cue card: `Monitor / patch / disclose / SBOM before launch.`
- Required line: `FDA 524B 用商業語言講，就是連線醫材在上市前就要準備好上市後怎麼監控、修補、告知，以及說清楚軟體組成。`
- Supporting line: `Postmarket responsibility does not start after launch; it starts in product design.`
- Voice move: Concise, executive-readable.
- Cut if late: Remove English supporting line.
- Rubric protected: Content Depth and Value, Audience Impact.

### Slide 9. FDA 2025 Traceability

- Timebox: `7:40-9:10`
- Cue card: `Reviewer checks traceability, not tool output.`
- Required line: `審查者不會只看工具有沒有跑；他會看 architecture、threat model、controls、tests 和 finding disposition 有沒有接起來。`
- Supporting line: `這條線接不起來，文件再多也只是資料夾。`
- Voice move: Slow, precise; this is cognitive-heavy.
- Cut if late: Remove one artifact name but preserve the traceability sentence.
- Rubric protected: Content Depth and Value, Stage Rhythm and Time Control.

### Slide 10. TFDA Lens

- Timebox: `9:10-10:30`
- Cue card: `AI model must be explainable in use context.`
- Required line: `回到台灣，AI 模型不是黑盒子傳奇；醫療產品要說清楚 intended use、資料怎麼來、模型怎麼驗證、限制在哪裡。`
- Supporting line: `Cybersecurity must connect back to model documentation and software validation.`
- Voice move: Conversational but serious.
- Cut if late: Keep intended use, data, validation, limitation; skip the English sentence.
- Rubric protected: Audience Impact, Content Depth and Value.

### Slide 11. NIST Management Language

- Timebox: `10:30-11:30`
- Cue card: `Shared language for company ownership.`
- Required line: `NIST 的價值，是讓董事會、PM、RD、法規和客服可以講同一種風險語言。`
- Supporting line: `Govern 是誰負責；Respond 和 Recover 是出了事之後怎麼保護服務連續性。`
- Voice move: Lighter, as a recovery beat.
- Cut if late: Use only the required line.
- Rubric protected: Stage Rhythm and Time Control, Audience Impact.

### Slide 12. AI Security Stack

- Timebox: `11:30-13:00`
- Cue card: `Model / runtime / infrastructure.`
- Required line: `醫療 AI 要安全，model、runtime、infrastructure 不能只挑一層做。`
- Supporting line: `Model 看 provenance 和 evaluation；runtime 看 isolation 和 secrets；infrastructure 看 identity 和 updates。`
- Voice move: Layer-by-layer, measured.
- Cut if late: Keep the three-layer sentence; drop examples.
- Rubric protected: Visual Design of Slides, Content Depth and Value.

### Slide 13. Scale 1: Model

- Timebox: `13:00-14:30`
- Cue card: `Small scope, still evidence.`
- Required line: `如果你真的只有 AI model，範圍最小，但不是沒有資安責任。`
- Supporting line: `至少要說清楚 model artifact、資料 lineage、dependency / SBOM，以及更新邊界。`
- Voice move: Efficient; start repeated scale pattern.
- Cut if late: Keep artifact and update boundary; skip dependency examples.
- Rubric protected: Content Depth and Value.

### Slide 14. Scale 2: Model + Viewer

- Timebox: `14:30-16:00`
- Cue card: `Wrapper becomes attack surface.`
- Required line: `一旦加上 viewer，攻擊者不一定攻擊模型，他可以攻擊檔案解析、upload、暫存、輸出呈現和使用者理解。`
- Supporting line: `所以這一層的安全問題，是 wrapper 和使用流程一起進入產品責任。`
- Voice move: Slight energy increase; make the risk concrete.
- Cut if late: Keep parser/upload/output; skip cache.
- Rubric protected: Content Depth and Value, Audience Impact.

### Slide 15. Scale 3: Platform

- Timebox: `16:00-17:30`
- Cue card: `Platform = identity, API, data, operations.`
- Required line: `平台化之後，資安就變成公司風險：身份、權限、API、資料庫、log、backup 都進來了。`
- Supporting line: `這不是只有 RD 的問題，也是營運、法規和品牌信任的問題。`
- Voice move: Decisive; speak to executives and PMs.
- Cut if late: Keep identity, API, database.
- Rubric protected: Content Depth and Value, Audience Impact.

### Slide 16. Scale 4: Connected Medical System

- Timebox: `17:30-19:00`
- Cue card: `Hospital integration turns cyber into continuity.`
- Required line: `當產品進入醫院網路，資安就不只是產品保護，而是臨床營運連續性。`
- Supporting line: `它可能接 PACS、HIS、更新伺服器、遠端服務；出事時影響的不只是一台機器。`
- Voice move: Decelerate; prepare emotional peak.
- Cut if late: Keep the required line and one example only.
- Rubric protected: Content Depth and Value, Stage Presence.

### Slide 17. Cyber Safety Is Patient Safety

- Timebox: `19:00-20:15`
- Cue card: `Patient safety line. Silence.`
- Required line: `Cyber Safety is Patient Safety.`
- Supporting line: `醫療 AI 出事時，受影響的不只是模型績效，而是病人、醫院營運、供應商責任與臨床流程。`
- Voice move: Stop moving; say slowly; hold silence after the required line.
- Cut if late: Do not cut this slide; cut one detail from slide 18.
- Rubric protected: Audience Impact, Stage Presence, Delivery Quality.

### Slide 18. White-Box Testing

- Timebox: `20:15-21:55`
- Cue card: `Inside-out: cheap, repairable evidence.`
- Required line: `White-box testing 的價值，是在 release 前找到便宜、可修、可追溯的問題。`
- Supporting line: `看 code、config、secrets、dependency、container、cloud setting，也看 AI pipeline 有沒有資料洩漏或更新邊界不清。`
- Voice move: Engineering clarity; no tool catalog.
- Cut if late: Keep code/config/dependency; skip container/cloud examples.
- Rubric protected: Content Depth and Value.

### Slide 19. Black-Box Testing

- Timebox: `21:55-23:35`
- Cue card: `Outside-in: can it be attacked?`
- Required line: `Black-box testing 問的是：從外部看，真的打得進來嗎？幾個小問題能不能串成攻擊路徑？`
- Supporting line: `White-box 是早期修問題，black-box 是 release 或送審前驗證真實暴露。`
- Voice move: Crisp contrast, slightly faster than slide 18.
- Cut if late: Keep contrast sentence only.
- Rubric protected: Delivery Quality, Content Depth and Value.

### Slide 20. Patch SLA

- Timebox: `23:35-25:10`
- Cue card: `Every finding needs a decision.`
- Required line: `如果只能帶走一個營運流程，我會選 Patch SLA。`
- Supporting line: `真正的資安不是沒有漏洞，而是每個漏洞進來後，公司知道誰負責、多久判斷、多久修補、怎麼通知、怎麼重測、證據放哪裡。`
- Final punch: `沒有 decision，就沒有治理；沒有證據，就沒有信任。`
- Voice move: Decisive; pause after required line and after final punch.
- Cut if late: Never cut final punch; shorten the middle sentence.
- Rubric protected: Content Depth and Value, Audience Impact, Structure and Narrative Design.

### Slide 21. Small Team Playbook

- Timebox: `25:10-26:30`
- Cue card: `Do not build bureaucracy first.`
- Required line: `小團隊不需要第一天就蓋大型制度；先建立 minimum viable evidence folder。`
- Supporting line: `先放 intended use、architecture、data flow、SBOM、threat model、test reports、vulnerability log、Patch SLA、release history。`
- Voice move: Conversational; reduce pressure.
- Cut if late: Say evidence folder, cheap checks, independent review only.
- Rubric protected: Audience Impact, Stage Rhythm and Time Control.

### Slide 22. 30 / 60 / 90

- Timebox: `26:30-27:50`
- Cue card: `30 inventory. 60 workflow. 90 validation.`
- Required line: `重點不是三個月變完美，而是三個月後公司開始自動留下可信證據。`
- Supporting line: `30 天盤點資產、SBOM、資料流程；60 天建立 threat model、CI gates、finding workflow；90 天做 pen test、Patch SLA、retest evidence。`
- Voice move: Measured cadence; pause between 30, 60, 90.
- Cut if late: One output per bucket.
- Rubric protected: Audience Impact, Structure and Narrative Design.

### Slide 23. Closing

- Timebox: `27:50-28:30`
- Cue card: `Trust before audit. Stop.`
- Required line: `先把安全做進產品，法規文件才會自然長出來。`
- Supporting line: `真正成熟的團隊，不是文件最多的團隊，而是每一個風險都知道怎麼證明、怎麼修、怎麼追的團隊。謝謝大家。`
- Voice move: Slow, centered; no new technical content after final sentence.
- Cut if late: Keep required line and `謝謝大家`; remove supporting line.
- Rubric protected: Audience Impact, Stage Presence, Delivery Quality.

## 3. Pocket Cue Card

Use this for late-stage rehearsal when the manuscript is no longer needed.

```text
0:00  Title: topic only.
0:10  Disclaimer: pause, move on.
0:30  Not model. Trust / patch / evidence.
1:50  AI is infrastructure.
3:00  Cyber -> care disruption.
4:00  Four scales: model, viewer, platform, connected system.
5:20  Evidence, not slogans.
6:30  FDA 524B: monitor, patch, disclose, SBOM.
7:40  FDA 2025: traceability, finding disposition.
9:10  TFDA: intended use, data, validation, limits.
10:30 NIST: shared management language.
11:30 Stack: model / runtime / infrastructure.
13:00 Scale 1: model evidence.
14:30 Scale 2: viewer wrapper.
16:00 Scale 3: platform operations.
17:30 Scale 4: clinical continuity.
19:00 Cyber Safety is Patient Safety.
20:15 White-box: early repairable evidence.
21:55 Black-box: external exposure.
23:35 Patch SLA: every finding needs a decision.
25:10 Small team: minimum evidence folder.
26:30 30 / 60 / 90.
27:50 Trust before audit. Stop.
```

## 4. Recovery Scripts

### If Running Late At Slide 12

Say:

`接下來我不展開每一個細節，我用四個產品尺度把風險快速走完。`

Then use only the required line for slides 13-16 and preserve slide 17.

### If Running Late At Slide 18

Say:

`Testing 的重點不是工具名稱，而是 finding 最後怎麼變成 decision。`

Then compress slides 18-19 to one contrast sentence each and preserve slide 20.

### If Slide Or Mic Issue Interrupts

Say:

`我們回到今天的主線：產品每多一層，證據也要多一層。`

Then resume at the nearest product-scale or Patch SLA point. Do not apologize repeatedly.

## 5. Final Run Acceptance Gate

The run is ready only if all conditions are true:

- [ ] Slide 6 is reached by `4:00` and finished by `5:20`.
- [ ] Slide 12 is finished by `13:00`.
- [ ] Slide 17 is delivered with a pause.
- [ ] Slide 20 is not rushed and includes `沒有 decision，就沒有治理；沒有證據，就沒有信任。`
- [ ] Slide 23 starts by `27:50`.
- [ ] No extra content is added after the closing.
