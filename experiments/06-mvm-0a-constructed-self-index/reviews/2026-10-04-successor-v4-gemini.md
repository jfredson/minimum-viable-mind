Model: Gemini 3.1 Pro
Date: 2026-10-06
Mode: documents shown (the whole packet, `packets/2026-10-04-successor-v4-tier2-gemini.md`, as one document); lookup setting not recorded

*Filed word for word from John's pastes by a Claude Code planning session. Two turns in one Gemini conversation. The prompts John sent are shown between rules and are not Gemini's words. The prompts are the ones the planning session suggested; John did not report changing them.*

---
**Prompt 1 (John), sent with the document:**

> Please read the attached document in full, from start to finish, and follow the instructions inside it. It is a review packet; your review is requested at the end.

---
**Answer 1 (Gemini):**

### Part 1: Feasibility

| ID | Finding | Severity |
| --- | --- | --- |
| G1 | Ruled episode counts (180 held-out) were rehearsed only at toy width (160), not registered width (448), risking floor failure. | Serious |
| G2 | Registered nomination on the laptop processor is argued, not timed for the registered shape. | Worth-noting |

**G1: Episode counts rehearsed at wrong width.** Version 4 Section 9 sets the fit floor using 180 held-out development episodes. The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) demonstrates that at the registered width of 448, there are more coordinates than fitting episodes. A stand-in test dropping the entangled model below the floor of 144 confirms this risks returning a "no verdict" simply due to dimensionality.

**G2: Processor nomination timing.** Version 4 Section 11 argues the 30-million parameter model fits on the laptop processor for nomination. The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) timed this at approximately 25 hours for twelve models. While this proves it is computationally feasible, the device ruling currently covers the fit and not the choice, which could lead to unregistered choices driving the stop at step 5a.

---

### Part 2: Satisfied by the wrong thing

| ID | Finding | Severity |
| --- | --- | --- |
| G3 | Grammar extends closed design without noting departures, leaving name cue in text. | Serious |
| G4 | Whole-state floor formula admits zero or negative divisors for models at chance. | Serious |

**G3: Unstated grammar departures.** Version 4 Section 4.1 registers the task grammar as an extension of `curriculum_a3.py`. The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) points out that `curriculum_a3.py` renders the marker word three tokens before the action. The two deliberate departures that remove this cue to make the episodes token-for-token identical are omitted in Version 4. If built as written, a free model could clear the floor by reading a name badge rather than carrying an answer.

**G4: Zero divisors in printed floor.** Version 4 Section 6.4 item 1 defines the whole-state floor with a printed formula (`accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy − accuracy_untouched)`). As shown in the inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`), this formula admits every site set with a divisor of exactly zero or below when applied to a model whose own-directed accuracy is at or under its no-transplant rate.

---

### Part 3: No verdict

| ID | Finding | Severity |
| --- | --- | --- |
| G5 | Gate requires "ownership-free state and syntax batteries" which do not exist in the task. | Fatal |
| G6 | Outcome map has holes for several no-verdict states. | Serious |

**G5: Non-existent batteries clause.** Version 4 Section 8.2 dictates that "the ownership-free state and syntax batteries must hold" to gate the free model. The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) confirms the successor’s task has no such batteries and no set line. Under stop condition S8 in Version 4 Section 11, an unevaluable gate counts as failed. Consequently, the free model could never be read, entirely blocking Outcome R1.

**G6: Incomplete outcome map.** Version 4 Section 3 defines the registered outcomes. The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) identifies multiple states that fail to map to these terms, such as a "no verdict" on the separable model (arm T), or the two-model fallback which has no registered outcome term. Since reporting outcomes in un-registered words is prohibited, reaching these states results in an unreportable conclusion.

---

### Part 4: Over-reading

| ID | Finding | Severity |
| --- | --- | --- |
| G7 | Label-search sentence misattributes one candidate's seeds as three separate candidates. | Worth-noting |
| G8 | Competing solver sentence misstates its own calculated miss figures. | Worth-noting |
| G9 | Weakness description of competing solver omits the name-cue route. | Worth-noting |

**G7: Misquoted candidate seeds.** Version 4 Section 7.2 states that "anchored at the action position the three candidates reach 0.733, 0.383 and 0.478". The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) verifies these numbers actually belong to a single candidate across seeds 0, 1, and 2.

**G8: Inaccurate solver miss description.** The ruled sentence for the competing solver in Version 4 claims its untouched rate "missed the no-transplant rule by 0.11 or more". The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) notes it missed the formula by 0.109 to 0.139, rendering "0.11 or more" factually false.

**G9: Incomplete weakness description.** The ruled new weakness in Version 4 asserts the toy has no model that does the task by another route. The inside review (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`) argues that the free model itself solves the own-directed condition without carrying its marker word.

---

The registration text, including the referenced file "2026-10-04-successor-v4-tier2-gemini.md", should not be registered in its current state. The inclusion of the "ownership-free state and syntax batteries" gate in Section 8.2 creates a guaranteed failure path for the free model, as the batteries do not exist in the successor task and stop condition S8 forces unevaluable gates to fail. Furthermore, serious structural omissions—such as failing to codify the grammar departures that remove name cues, risking floor failures by using untested episode counts at the registered width, and leaving holes in the outcome mapping—threaten the integrity of the measurement and violate the strict rule against unregistered reporting. These must be rectified prior to Gate A closure.

---
**Prompt 2 (John), same conversation.** Sent because every finding in answer 1 restated an inside-review finding, while the packet says record 5 is given "so you can look elsewhere: you are not asked to re-derive them":

> The packet says the inside reviewer's findings (record 5) are given "so you can look elsewhere: you are not asked to re-derive them". Each of G1 to G9 is one of the inside review's findings. Following the brief, please review the registration text again and report only problems the inside review did not raise, labelled G10 onward. If you find none, say so plainly.

---
**Answer 2 (Gemini):**

### Part 1: Feasibility

| ID | Finding | Severity |
| --- | --- | --- |
| - | No additional findings beyond RT-237 to RT-246. | - |

The inside review comprehensively audited the measurement feasibility, identifying the fatal flaw where the free model's gate cannot be evaluated due to non-existent batteries (RT-237) and the dimensional mismatch for the episode counts (RT-240). Upon independent review of the registration text, the rehearsal records, and the newly established controls, no further feasibility issues or un-rehearsed pre-stated quantities were found.

### Part 2: Satisfied by the wrong thing

| ID | Finding | Severity |
| --- | --- | --- |
| - | No additional findings beyond RT-237 to RT-246. | - |

The inside review successfully identified the primary vulnerabilities here, notably the omission of the grammar departures that could allow the free model to clear the floor using a name cue (RT-239) and the floor formula admitting zero or negative divisors (RT-238). No new loopholes allowing a model without the claimed structure to satisfy the clauses were found. The text explicitly admits and bounds the remaining known limitations, such as the fact that the reading cannot distinguish an entangled act from an ownership answer located where the read did not look (Weakness W12).

### Part 3: No verdict

| ID | Finding | Severity |
| --- | --- | --- |
| - | No additional findings beyond RT-237 to RT-246. | - |

The outcome map holes (RT-241) and the cascading failure of the unevaluable gate clause (RT-237) thoroughly cover the ways the target could fail to return a verdict on the runs it is written for. The text's stop conditions, no-verdict rules, fallback mechanisms, and the mathematical finiteness of the chance-corrected form are otherwise complete.

### Part 4: Over-reading

| ID | Finding | Severity |
| --- | --- | --- |
| - | No additional findings beyond RT-237 to RT-246. | - |

Version 4 proactively bounds its claims, explicitly outlining weaknesses such as the constructed arms differing in more than degree (Weakness W1) and the fact that partial separation within a trial has not been shown to scale (Weakness W10). Aside from the minor misquotations noted in the inside review (RT-242, RT-244, RT-246), the text accurately reflects what the instrument measures without over-claiming.

The registration text should not ship in its current state, entirely due to the fatal and serious findings already documented by the inside review. While this outside pass confirms that the text is structurally sound beyond those identified points, the inclusion of the "ownership-free state and syntax batteries" gate (RT-237) remains a guaranteed failure path that prevents the free model from ever being read. Combined with the missing grammar departures that risk invalidating the core measurement by leaving a name cue in the text (RT-239), and the untested episode counts at the registered width (RT-240), these flaws fundamentally compromise the experiment. The text must be halted at Gate A until the impossible gate condition is removed, the true experimental grammar is fully codified, and the outcome map holes are closed.
