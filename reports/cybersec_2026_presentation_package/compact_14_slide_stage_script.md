# CYBERSEC 2026 Compact 14-Slide Stage Script

Purpose: provide the delivery script for the recommended compact `14`-slide CYBERSEC deck.

Use this after `compact_14_slide_deck_plan.md`. The deck plan defines what each slide is; this file defines how to say it on stage under a `30:00` conference clock.

Stage language: Taiwan Traditional Chinese, with English technical terms where they are standard in industry.

## 1. Performance Contract

The compact version has fewer slides, so the speaker must not compensate by speaking faster. The design goal is the opposite: fewer slide changes, stronger section turns, more controlled pauses, and clearer memory anchors.

| Requirement | Stage Behavior | Rubric Protected |
| --- | --- | --- |
| Preserve five memory anchors | Slow down on slides 3, 5, 10, 12, 14 | Audience Impact, Stage Presence |
| Keep technical credibility | Explain artifacts and decisions, not tool catalogs | Content Depth and Value |
| Avoid classroom report posture | Use decision language: `風險在哪裡`, `證據怎麼接`, `finding 最後去哪裡` | Delivery Quality |
| Protect time | Use cutable detail markers; never improvise extra examples after slide 10 | Stage Rhythm and Time Control |
| Keep the close clean | No new framework, reference, or contact explanation after slide 14 line | Structure and Narrative Design |

## 2. Timing And Energy Map

| Slide | Timebox | Energy | Delivery Job |
| ---: | ---: | --- | --- |
| 1 | `0:00-0:10` | Calm | Establish presence |
| 2 | `0:10-0:30` | Neutral | Clear compliance |
| 3 | `0:30-2:20` | Controlled authority | Reframe product responsibility |
| 4 | `2:20-4:30` | Alert | Connect AI infrastructure to care disruption |
| 5 | `4:30-6:30` | Slow / clear | Install the four-scale map |
| 6 | `6:30-10:40` | Authoritative | Translate regulation into evidence chain |
| 7 | `10:40-14:00` | Practical | Bridge Taiwan, governance, and AI stack |
| 8 | `14:00-16:40` | Efficient | Explain model and viewer scope |
| 9 | `16:40-19:20` | Decisive | Explain platform and clinical integration risk |
| 10 | `19:20-20:40` | Slow / still | Deliver patient-safety peak |
| 11 | `20:40-23:00` | Crisp | Contrast white-box and black-box |
| 12 | `23:00-25:10` | Strong | Deliver Patch SLA climax |
| 13 | `25:10-27:40` | Constructive | Give `30/60/90` implementation path |
| 14 | `27:40-28:30` | Slow / final | End with trust-before-audit principle |

## 3. Full Compact Stage Script

### Slide 1. Title

各位好，我是林家聖。今天的題目是 AI 軟體醫材的資安實戰。

Cut marker: stop here. Do not add biography.

Transition:

`關鍵字很多，但今天我只想留下三件事：信任、修補、證據。`

### Slide 2. Required CYBERSEC Disclaimer

這是大會必要的 disclaimer，我在這裡停一下，讓大家看見。

接下來我們直接進入今天真正的問題。

Cut marker: if timing is tight, say only the first sentence and move on.

### Slide 3. 你賣的不是模型

很多 AI 團隊一開始會說：我們只是提供模型。可是醫療現場不會這樣看。

醫師看到的是結果，病人承受的是後果，公司要負責的是整個使用情境。

所以第一個轉念是：你賣的不是模型。

Pause.

你賣的是一個在醫療情境中可被信任、可被修補、可被稽核的系統。

今天所有的 FDA 524B、Threat Modeling、Patch SLA，其實都是從這個轉念開始：產品不是只有準，而是要能被信任；不是只有上線，而是要能被修補；不是只有宣稱安全，而是要拿得出證據。

Cut marker: if late, remove the first two setup sentences and start directly from `所以第一個轉念是`.

Transition:

`如果這是真的，我們就要問：為什麼 2026 年這件事更急？`

### Slide 4. AI 變成基礎設施，資安變成照護連續性

2026 年 AI 的語言正在從模型變成基礎設施。

大家不只談模型多大、跑分多高，而是談模型怎麼部署、怎麼更新、怎麼被隔離、怎麼被監控、怎麼接到真實 workflow。

對醫療 AI 來說，這件事更直接。因為醫療不是把 model 放上雲端就結束，它會接 runtime、資料、使用者、更新鏈，最後接到臨床流程。

所以醫療資安也已經不只是 IT 後台問題。當 AI 進入醫療，cyber incident 很快就會變成 care disruption：診所可能停擺，系統可能降級，供應商也可能變成醫院端的連續性風險。

Cut marker: if late, keep only three sentences: AI is infrastructure; medical AI connects to workflow; cyber incident becomes care disruption.

Transition:

`所以我們需要一張產品尺度地圖，先決定風險到底長在哪裡。`

### Slide 5. 四種產品尺度：風險會跟架構一起長大

請大家先記四層就好。

第一層，只有 model。第二層，model 加 viewer。第三層，有 platform 和 database。第四層，進入 connected medical system。

每加一層，產品能力變強，攻擊面也變大，證據需求也變大。

這張圖很重要，因為等一下我們講法規、testing、Patch SLA，都不是抽象清單，而是要回來問：你的產品到底在哪一層？這一層多了什麼風險？你有沒有相稱的證據？

Pause after naming all four layers.

Cut marker: never cut the four layers; cut only the final explanatory sentence if late.

Transition:

`有了這張地圖，我們再看法規到底在要求什麼。`

### Slide 6. 法規要的是一條證據鏈

我用一句話講法規：法規要的是證據，不是口號。

Pause.

FDA 524B 如果用商業語言講，就是：如果你的醫材會連線，上市前就要準備好上市後怎麼 monitor、怎麼 patch、怎麼 disclose，以及用 SBOM 說清楚軟體組成。

這件事的重點不是多交一份文件，而是公司在產品設計階段，就要知道上市後漏洞怎麼被看見、誰判斷、誰修補、怎麼通知、怎麼留下紀錄。

FDA 2025 guidance 再往下問的是 traceability。你的 architecture 在哪裡？Threat model 怎麼畫？Controls 對應到哪些風險？Testing 有沒有真的打到攻擊面？每個 finding 最後去哪裡了？

所以我會把它壓成一條線：risk、control、test、fix、evidence。

這條線接不起來，文件再多也只是資料夾；這條線接得起來，法規文件才像是工程工作自然留下來的證據。

Cut marker: if late, keep FDA 524B four verbs and the risk-control-test-fix-evidence sentence; remove the architecture/threat-model details.

Transition:

`回到台灣和公司內部治理，這條證據鏈還需要兩種語言：模型語言和管理語言。`

### Slide 7. 台灣團隊需要同時說清楚模型、治理與 AI stack

在台灣，AI/ML SaMD 不是黑盒子傳奇。團隊要說清楚 intended use：誰用、在哪裡用、不能怎麼用。

也要說清楚 data 怎麼來，algorithm 怎麼設計，V&V 怎麼做，clinical performance 怎麼證明。

但這些模型語言還不夠。公司內部還需要管理語言。NIST 的價值，就是讓董事會、PM、RD、法規、客服可以講同一種風險語言：誰 govern，誰 identify，誰 protect，出事時誰 respond、誰 recover。

最後，AI security 不能只挑 model 做。Model 要看 provenance 和 evaluation；runtime 要看 isolation 和 secrets；infrastructure 要看 identity 和 updates。

這三件事接起來，才是醫療 AI team 真正能拿去討論、治理、送審、跟客戶溝通的 security language。

Cut marker: if late, keep one sentence per column: TFDA model evidence, NIST governance language, model/runtime/infrastructure.

Transition:

`接下來回到剛才的四層產品尺度，看每一層到底多了什麼風險。`

### Slide 8. Scale 1-2：Model 到 Viewer

第一層，如果你真的只有 AI model，範圍最小，但不是沒有資安責任。

至少要說清楚 model artifact 從哪裡來、data lineage 怎麼追、dependency 和 SBOM 有沒有整理、update boundary 在哪裡。

第二層，一旦加上 viewer，世界就變了。攻擊者不一定攻擊模型，他可以攻擊 file parser、upload、cache、output 呈現，甚至攻擊使用者怎麼理解輸出。

所以 model 到 viewer 的差別，是產品從一個 artifact 變成一個使用情境。Security evidence 也要從模型來源，長到檔案、介面、暫存和輸出的安全邊界。

Cut marker: if late, keep `model evidence` and `viewer attack surface`; remove cache and user-interpretation detail.

Transition:

`如果再往上長成平台，資安就不只是產品問題，而是公司營運和臨床連續性問題。`

### Slide 9. Scale 3-4：Platform 到 Connected Medical System

第三層，viewer 加上 platform 和 database，資安就變成公司風險。

你開始有 identity、RBAC、API、database、audit log、backup。這些不是只有 RD 的問題，也是營運、法規、客服和品牌信任的問題。

第四層，當產品進入 connected medical system，事情再升級一次。

它可能接 PACS、HIS、hospital network、update server、remote service。這時候 cyber risk 不只是產品保護，而是 clinical continuity risk。

如果這一層出事，影響的不只是某一次 model output，而可能是多個臨床流程、醫院端營運、供應商責任和病人照護連續性。

Cut marker: if late, keep identity/API/database and hospital network/update server. Remove secondary examples.

Transition:

`所以醫療 AI 的資安，最後不是一句 IT 口號，而是一句病人安全的話。`

### Slide 10. Cyber Safety Is Patient Safety

Cyber Safety is Patient Safety.

Pause.

醫療 AI 出事時，受影響的不只是模型績效，而是病人、醫院營運、供應商責任與臨床流程。

這也是為什麼我不建議把資安放到產品最後才補。越晚才補，越像文件；越早放進產品，越像真正的安全設計。

Cut marker: never cut the required line or the pause. If late, remove the last sentence.

Transition:

`接下來進入最實作的部分：怎麼測，怎麼修，怎麼留下證據。`

### Slide 11. Testing Strategy：White-box + Black-box

Testing 不是工具名稱競賽。Testing 的價值，是讓風險變成可以修、可以驗證、可以追蹤的 finding。

White-box testing 是在 release 前，從內部找便宜、可修、可追溯的問題。看 code、config、dependency、container、cloud setting，也看 AI pipeline 有沒有資料洩漏或更新邊界不清。

Black-box testing 問的是另一個問題：如果我不知道你的原始碼，只從外部看，我能不能打得進來？能不能繞過登入？能不能把幾個小問題串成攻擊路徑？

所以 white-box 是早期修問題，black-box 是 release 或送審前驗證真實暴露。兩個不是互相取代，而是前後接力。最後都要回到 finding list 和 retest evidence。

Cut marker: if late, say only: white-box finds early repairable problems; black-box validates external exposure; both must create findings and retest evidence.

Transition:

`但 finding 出來以後，真正的治理才開始。`

### Slide 12. Patch SLA：Every Finding Needs A Decision

如果只能帶走一個營運流程，我會選 Patch SLA。

Pause.

真正的資安不是「沒有漏洞」，而是每個漏洞進來後，公司知道誰負責、多久判斷、多久修補、怎麼通知、怎麼重測、證據放哪裡。

這裡最重要的字是 decision。

Finding 進來之後，不是只有修或不修。可能是 fix now，可能是 compensate，可能是 defer with timeline，也可能是 non-applicable with rationale。

沒有 decision，就沒有治理；沒有證據，就沒有信任。

Pause.

Cut marker: never cut `沒有 decision，就沒有治理；沒有證據，就沒有信任。` If late, shorten the middle vulnerability-workflow sentence.

Transition:

`我知道很多小團隊會覺得這很大，所以最後把它壓成 30、60、90 天。`

### Slide 13. Small Team 30 / 60 / 90

小團隊不需要第一天就蓋大型制度。

30 天，先盤點：assets、SBOM、data flow、intended use、known vulnerabilities。

60 天，建立節奏：threat model、CI security gates、finding workflow、customer security note。

90 天，做外部驗證：penetration test、Patch SLA、CVD process、retest evidence、release history。

重點不是三個月變完美，而是三個月後，公司開始自動留下可信證據。

這就是小團隊比較實際的路徑：先讓風險看得見，再讓 evidence 可以重複產生，最後讓 findings 可以被治理。

Cut marker: if late, use one output per bucket: 30 inventory, 60 workflow, 90 validation.

Transition:

`最後，我們回到今天的第一個問題：怎麼在稽核之前先建立信任。`

### Slide 14. 先建立信任，再面對稽核

今天我們從一個 model 開始，走到 connected medical system。

每往前一步，產品更有價值，也更需要被信任、被修補、被稽核。

所以我想用一句話結束：

先把安全做進產品，法規文件才會自然長出來。

Pause.

真正成熟的團隊，不是文件最多的團隊，而是每一個風險都知道怎麼證明、怎麼修、怎麼追的團隊。

謝謝大家。

Cut marker: if late, say only the closing sentence and `謝謝大家`.

## 4. Compact Pocket Cue Card

```text
0:00  Title. Calm.
0:10  Disclaimer. Pause, move.
0:30  Not model. Trust / patch / evidence.
2:20  AI infrastructure -> care disruption.
4:30  Four scales. Risk grows, evidence grows.
6:30  FDA evidence chain. Monitor / patch / disclose / SBOM.
10:40 Taiwan model evidence + NIST governance + AI stack.
14:00 Scale 1-2: model evidence -> viewer attack surface.
16:40 Scale 3-4: platform risk -> clinical continuity.
19:20 Cyber Safety is Patient Safety. Pause.
20:40 White-box + black-box -> findings + retest evidence.
23:00 Patch SLA. Every finding needs a decision.
25:10 30 inventory / 60 workflow / 90 validation.
27:40 Trust before audit. Stop.
```

## 5. Rehearsal Score Checks For Compact Version

| Check | Pass Condition | If It Fails |
| --- | --- | --- |
| Opening | Slide 3 thesis lands by `2:20` | Cut setup; keep `你賣的不是模型` |
| Map | Four product scales are clear by `6:30` | Slow slide 5; cut slide 4 detail |
| Evidence | Slide 6 explains FDA 524B and traceability without legal overload | Cut artifact list; keep evidence chain |
| Local bridge | Slide 7 connects TFDA, NIST, and AI stack in one coherent bridge | Use one sentence per column |
| Scale logic | Slides 8-9 make product growth obvious | Use the same phrase: `這一層多了什麼風險？` |
| Emotional peak | Slide 10 includes silence after `Cyber Safety is Patient Safety` | Rehearse pause separately |
| Operational climax | Slide 12 includes decision outcomes and final punch line | Shorten testing section, never cut Patch SLA |
| Close | Slide 14 starts by `27:40` | Use one-output-per-bucket on slide 13 |

## 6. Compact Emergency Path

If the session effectively becomes `20:00`, use only these slide beats:

1. Title and disclaimer: `0:30`
2. Slide 3 thesis: `2:00`
3. Slide 5 four product scales: `2:00`
4. Slide 6 evidence chain: `4:00`
5. Slide 7 model/governance/AI-stack bridge: `2:30`
6. Slides 8-9 product-scale risks: `3:30`
7. Slide 10 patient safety: `1:00`
8. Slide 12 Patch SLA: `2:00`
9. Slide 13 `30/60/90`: `1:30`
10. Slide 14 close: `0:30`

Skip compact slide 4 and slide 11 as standalone sections. Mention their core ideas inside slide 5 and slide 12 respectively.
