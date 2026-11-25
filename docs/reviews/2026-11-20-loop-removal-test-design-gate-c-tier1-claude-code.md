*Filed 2026-11-20 by the session that wrote the target, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, working read-only in a detached worktree at commit 4f68df5, and it changed nothing in the repository. Nothing in its text was changed in filing. The filer's check of the findings follows the review, below a rule, and is not part of it.*

---

# Gate C, tier 1 (the inside pass): the loop removal test design, version 0.1

*Reviewer: a fresh Claude Code session, working in the detached worktree `review-loop-design-2026-11-20` at commit 4f68df5. It changed nothing in the repository. Its scratch scripts are in its own scratchpad folder, outside git. Its findings continue the red-team numbering, as RT-335 to RT-357.*

---

**What I opened.**
- **Read in full:** the target, `docs/loop-removal-test-design-2026-11-20.md`. I also read in full the design note (`docs/2026-11-20-loop-removal-design-note.md`), the three-hypotheses proposal, the split removal test design (version 0.6), the battery authoring specification, the battery generators (`experiments/09-split-removal-test/src/batteries.py`) and the split test's rehearsal phase-1 findings.
- **Read in part:** `docs/outside-review-protocol.md`, the two sections named in the brief and the list of headings. I read the earlier Gate C tier 1 review for its format.
- **External pages, opened through a page-fetching tool that returns a summary and quotes rather than the raw page:**
  - Thinking Machines' Inkling 2 Mini announcement;
  - the TML-d24-varloop-research model card;
  - its Hugging Face page;
  - Goodfire's "Interpreting Inkling 2 Mini", including the appendix formulas.
  Where a finding rests on a quote from these pages, the quote came back through that tool, so it is lookup, flagged as such.
- **Ran:** three scratch scripts that import the split test's generators without writing any file. They measure item lengths, how much donor and recipient items overlap, pool sizes and overlap between the two halves, and the paired sample size. Each is reported under its finding.

**What I did not open:** the chart images on the Thinking Machines pages, so the per-pass numbers drawn only in charts are unchecked. I also did not open `experiments/09-split-removal-test/rehearsal-method.md`, `run-notes.md` or the July experiment 01 records, and I did not read the positions ledger, `STATUS.md` or any code under `src/mvm/`. No model was downloaded and nothing was spent.

**One thing I checked and found to hold.** The press point was whether "mixing bypassed reproduces one pass" is true. On Goodfire's formulas it is true, given three conditions that Goodfire does not state outright (finding RT-342).
- Goodfire gives the mixing step as x′ = κ ⊙ x + γ ⊙ m. Here x is the layer's ordinary input and m is the message. The keep setting is κ = 1 − tanh(Fz), the gain setting is γ = tanh(Gz), and z = P[RMSNorm(x); RMSNorm(m)].
- The ordinary input in pass t is a mix over the word embeddings, block 1's sum and that pass's own block 2 and 3 sums only. Goodfire writes these as v0, v1, v2[t] and v3[t].
- Goodfire says "all of this is over a single token", with ordinary attention across positions inside each layer.
- So if the mixing step is skipped, the previous pass has no route into the current one, and passes 2 and 3 repeat pass 1.

---

## 1. Feasibility

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-335 | The average method cannot be computed for most positions of the prompt-rule items, because the neutral passages are much shorter than the items | fatal | MEASURED |
| RT-336 | Scoring by five candidates is left undefined, and so is the swap at the candidates' own positions | serious | ARGUED |
| RT-337 | Nothing shows that the block sums can be hooked on a 32 GB card in the shipped number formats | serious | ARGUED (lookup) |
| RT-338 | Whether the result can be read at all hangs on one unmeasured ratio in the normal-range check, and the split design's "room under the bound" rule was dropped | serious | ARGUED |
| RT-339 | Matching on damage may be impossible to reach, and the noise is not defined for the control coordinates | worth-noting | ARGUED (lookup) |
| RT-340 | The figure of about 120 items per cell carries over only in good cases, and the routine pool for test items caps the cell at 134 | serious | MEASURED |
| RT-341 | Pilot and test items overlap in two kinds, against the authoring specification and the design's "half B is unused" | serious | MEASURED |
| RT-342 | The mixing-bypassed check is sound in principle, but it rests on three facts no page states, and its 0.01 limit has no measured noise floor | worth-noting | ARGUED (lookup) |
| RT-343 | The amount of work is undercounted | worth-noting | ARGUED |
| RT-344 | The rule that at least three kinds of prompt-rule problem must survive, under the confidence filter and with no written reasoning, may not be reachable | serious | ARGUED (lookup) |

**RT-335, the average method cannot be computed (MEASURED).** Section 3(b) replaces the block sums with "their average over the neutral text, taken separately for each pass and each position up to the longest item". The neutral passages come from the split test's generator, `gen_neutral`. My script generated them and the pilot and test prompts, without writing any file:

```
python3 -I lengths.py .../experiments/09-split-removal-test/src
  R words per prompt: min 11 median 11 max 14
  P words per prompt: min 25 median 40.0 max 50
  neutral words: min 17 median 19.0 max 22
```

(The figures are the same for half A and half B.)

- **Too short.** The prompt-rule prompts run 25 to 50 words before any chat template is added. Not one neutral passage is longer than 22 words. So at every position past about the 22nd word there is no neutral data to average. That covers the second half of a typical prompt-rule item, which is where the question and the answer position sit.
- **No chat template.** The neutral passages also have no chat template. Their position 5 is the middle of a sentence like "The orchard draws visitors…", while an item's position 5 is a template token.
- **Result.** As written, method (b) cannot be run on the cell that decides outcome A. It is fixable, with a neutral set at least as long as the longest item and given the same template. But then the method no longer "follows experiment 01's mean-ablation" in any useful sense, because that method averaged directions, not positions.

**RT-336, five-candidate scoring is undefined.** Section 5 says the model's answer is "the candidate it gives the highest probability to after the prompt". The probability is "among the five" for the confidence filter. Three things are left open.
- **Multi-token candidates.** Many candidates run to several tokens: "Buenos Aires", the invented tokens built from syllables (such as *zibvam*), and some numbers. The design does not say whether a candidate is scored by the sum of its tokens' log-probabilities, by their mean, or by the first token only. Summing penalises longer candidates. First-token scoring cannot tell apart invented tokens that share a first syllable, which the list and ring kinds produce by construction (`token()` joins two syllables from one small pool).
- **"Among the five".** The design does not say how this is normalised, so the 0.9 confidence filter has no fixed meaning.
- **Positions.** The stated reason for the format is that "every position is known in advance". That is only half true. Scoring five candidates means five different continuations, each with its own positions, and each position needs a donor message during the swap. The design does not say which donor positions supply the recipient's candidate tokens, or whether "at least as long as the recipient" counts the candidate.

**RT-337, hooking and memory (lookup).** Section 2 says the Hugging Face software "is the usual route for reading and changing activity inside a model while it runs".
- **What the pages give.** The Hugging Face page lists Hugging Face among the frameworks. Its usage snippet loads the model with `AutoModelForSeq2SeqLM`, a class for a different kind of model. That reads as a generic, automatically made snippet, not a tested route. Neither page names a way to set the number of passes or to read activity inside the model.
- **Memory.** The card gives the formats as expert layers in NVFP4, the last four layers in MXFP8, and the rest in BF16, with "at least 32GB". If the hooks need ordinary code in place of the fused 4-bit kernels, the weights may have to be unpacked to BF16. At 26.4 billion parameters that is about 53 GB, more than the 32 GB card the design sizes the job for.
- **Record.** None exists. The cost line in section 8 depends on this. The first priced step should be "load, hook and run the identity check", not "a few hours".

**RT-338, the normal-range check.** Section 4 bounds the main removal's rise in surprise at ordinary text by random noise "of the same size", meaning the same length as the difference between the true and replaced sums. It then requires every comparison, matched on damage, to pass the same bound.
- **Why that reduces to one ratio.** Take a swap that does more harm, per unit of length, than random noise does. It fails the bound itself. Its matched random comparison then needs noise longer than the bound's noise, so the comparison is likely to fail too. Take a swap that does no more harm than noise of its length. Then everything passes. So whether the result can be read comes down to one ratio that nobody has measured: how much harm the swap does per unit of length, compared with noise.
- **The October record.** The split test's phase 1 measured that ratio for a structured removal on the bench model, at about 9.4 times random (phase-1 findings, damage table). The design note's hope that the loop "may avoid the problem that stopped the last removal test" applies to fewer passes, not to the swap, which is an edit inside the model judged by the same rule.
- **A dropped safeguard.** The split design required the rehearsal to report the room left under the bound, and to return to John if it was too little (its finding RT-327). That sentence is missing here, and section 9's list of return-to-John triggers does not include a failed normal-range check.

**RT-339, matching on damage (lookup).** Goodfire's formulas normalise every block sum before it is read (v̂ = v / RMS(v)), and the gain setting is capped between −1 and 1.
- **A ceiling on noise.** Past a certain size, adding more noise to the block sums stops increasing the damage: the readers see a normalised random direction, however large the noise. If the swap does more harm than that ceiling, no draw can be matched, and "fewer than 10 of 20 matched" makes the result not testable.
- **Control coordinates.** The design does not say whether the matched noise spares the control coordinates, as the main removal does. This matters, because one of them carries close to half of the normalised activity (RT-348).
- **The outside-the-loop comparison.** It is not said whether this comparison counts as "a needed comparison" under stage one.

**RT-340, sample size (MEASURED).** I simulated the outcome-A rule as section 6 states it, for both methods, with a true gap of 0.20. Routines lose nothing beyond the random comparison, and prompt-rule problems lose 0.20 more. The random comparison's loss was set at 0.05, 0.10 or 0.20, averaged over 20 draws. A shared item fragility of 0 (independent) or 0.6 sets how much an item's fragility carries across conditions. The intervals are a normal approximation, not 10,000 bootstrap resamples, and there were 300 simulated runs per row.

```
python3 -I power.py
comparison loss 0.10, fragility 0.0: n 120 -> A on both methods 0.81 ; n 80 -> 0.58
comparison loss 0.10, fragility 0.6: n 120 -> 0.93
comparison loss 0.20, fragility 0.0: n 120 -> 0.52 ; n 200 -> 0.80
comparison loss 0.20, fragility 0.6: n 120 -> 0.85
comparison loss 0.05, fragility 0.0: n 120 -> 0.98
```

- **When 120 is enough.** About 120 items per cell reaches 80% only when the comparison's own loss is about 0.10 or less. If the comparison loses 0.20, about 200 items are needed.
- **The cap.** The routine pool for the test half holds only 134 candidates (RT-341), so the cell cannot exceed 134. The confidence filter and the matching can only lower that. If the committed simulation asks for more than about 130, the design cannot meet it, and it has no rule for that case.
- **The scoring changed.** The 120 figure came from the split design, which scored generated answers starting from zero. Here every item has a 0.20 chance floor, so the spread of losses is different and the figure should not be assumed to carry over.

**RT-341, pilot and test overlap (MEASURED).** I generated half A (seed 1) and half B (a scratch seed) with the committed generators:

```
half B R candidates 134 {'r_add': 55, 'r_capital': 12, 'r_mul': 32, 'r_next_day': 7, 'r_opposite': 10, 'r_plural': 18}
R prompts identical across halves: 7 ['r_next_day']
p_operator answer values shared across halves: 26 of 28
```

- **Next weekday.** `gen_routine` draws the weekday from all seven days in both halves. So every next-weekday test prompt is a pilot prompt.
- **Invented operator.** `gen_prompt_rule` draws the operands and the four rule shapes from the same ranges in both halves, and only the operator symbol differs. So almost every answer value repeats across halves.
- **The rule broken.** Section 1 of the authoring specification says "No word, symbol table or answer value used in a pilot item can appear in a test item". The design's "half B is unused" is true only in that half B was never generated.
- **Arithmetic.** Sums and products make up 87 of the 134 routine candidates, about 65%. So "routine" is mostly arithmetic.

**RT-342, the mixing-bypassed check (lookup).** On Goodfire's formulas the argument holds (see "One thing I checked" above), but it rests on three facts that no page states.
1. **Pass 1 skips the mixing step.** Goodfire writes only "in loops t≥2, each looped layer has four inputs". The announcement says the gate "initially blocks the entire message", which may describe how training started rather than what pass 1 does. If pass 1 instead computes x′ = κ ⊙ x with an empty message, then skipping the step on passes 2 and 3 is not the same as pass 1, and the check fails for a harmless reason.
2. **Block sums restart at zero on each pass.** Goodfire's per-pass notation (v2[t]) suggests this, but the text says only "starting from zero".
3. **Each pass has its own attention keys and values.** Goodfire does not discuss a cache shared across passes.

The fix is to define the bypass from the code as "do on passes 2 and 3 exactly what the code does on pass 1". Separately, the 0.01 limit on log-probability has no measured noise floor. With experts chosen 8 out of 128 and 4-bit kernels, two unaltered runs may differ. The identity and bypass checks should first measure two unaltered runs against each other.

**RT-343, the amount of work.** Section 8 counts "roughly 60 conditions". Counting what the design names on task items gives about 90:
- the main removal under two methods;
- 20 random draws and 20 outside-the-loop draws, each matched per method, so 80 runs;
- two runs with fewer passes, the identity check, the bypass check, and the secondary run that swaps the control coordinates under both methods.

It also leaves out the search over noise size during damage matching and the baseline runs without the rule sentence. The second model would need its own baselines, bound and matching (RT-351). The order of magnitude may hold, but the figure should be recounted before an estimate goes to John.

**RT-344, three kinds of prompt-rule problem (lookup).**
- **No written reasoning.** Scoring with no written reasoning makes the letter code, the two-rule list and the ring much harder than on the bench model, where they already failed with free generation (phase-1 findings: 1, 2 and 0 items kept). By the makers' own measure, this model's no-reasoning task length is 16 seconds of human work at one pass and 37 seconds at three. Reversing a list, replacing a token and indexing it, all with nothing written down, may be beyond that.
- **The wrong answers decide the check.** Whether the "rule is needed" check passes depends on how the four wrong answers are built, which is not yet specified. In the letter code, the right answer is always a common English noun. If the wrong answers are not nouns, the model can pick the noun without the table, and the kind is dropped.
- **Result.** "Fewer than three kinds survive" is a likely path to not testable. The design does at least commit the candidate sets before any item (section 9, step 3), so they cannot be tuned to make a kind survive.

---

## 2. Satisfied by the wrong thing

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-345 | The swap changes more of each prompt-rule item than of each routine item, and the prompt-rule items are 2 to 4 times longer; the random comparison corrects for neither | fatal | MEASURED |
| RT-346 | The swap supplies another item's working, so the donor's answer can intrude among the five candidates | serious | ARGUED |
| RT-347 | The confidence bins are too coarse to stop the prompt-rule items from simply failing first | serious | ARGUED |
| RT-348 | Keeping the control coordinates at their true values keeps a large part of the message, against the "exact by construction" claim | serious | ARGUED (lookup) |
| RT-349 | Five-candidate scoring changes what a "loss" in each cell means | serious | ARGUED |

**RT-345, the swap's dose differs between the cells (MEASURED, with a stated assumption).** In a model that reads text left to right, two prompts that start with the same words have identical activity at those positions. So the swap changes the message only from the first word where donor and recipient differ. I drew a same-kind donor at least as long as each test-half item. I counted, in words, the share of positions after the first difference, assuming 12 words of fixed template before the user text and 4 after:

```
python3 -I dose.py .../experiments/09-split-removal-test/src
R fraction of positions whose message the swap actually changes: mean 0.43 (total positions median 27)
P fraction ...: mean 0.54 (total positions median 56)
```

- **Dose.** The swap changes about 12 positions in a typical routine item and about 30 in a typical prompt-rule item.
- **Alignment.** At the word level, 84% to 93% of routine positions get a donor message from the very same word, against 73% to 81% for prompt-rule items. Counted in tokens the gap will be wider, because the invented tokens split into a variable number of pieces, which shifts every later position.
- **Why the comparison does not catch it.** The random comparison adds one noise size to every item, set on neutral text. It does not grow with how much of a given item the swap changes.
- **The result.** A model whose loop does nothing special for rule-following would still lose more on prompt-rule items under the swap. Those items have more of their message replaced, and more context depends on it. That is outcome A, reached by the wrong thing.
- **Length.** Apart from the swap, prompt-rule items are 25 to 50 words and routine items 11 to 14. A loop that helps any long context will show this pattern, and the confidence matching does nothing about length.
- **Fixes.**
  - Report how far the swap moves the block sums for each item, and match that or adjust for it across the cells.
  - Scale the random comparison per item to that item's swap size.
  - Add a long routine control: routine questions behind a rule-length preamble the question does not need.

**RT-346, the donor's answer can intrude.** The swap does not give the model "no feedback". It gives it another item's feedback, including that item's working at the operand and answer positions. If the donor's right answer is among the recipient's five candidates, for example a nearby sum, the model may pick it. The loss then comes from misleading content, not from losing a place to hold this item's contents together. The design should report how often the chosen candidate is the donor's answer, and build the wrong answers so that donors' answers are excluded or tracked.

**RT-347, the confidence bins.** Items are matched in two bins, 0.90 to 0.95 and above 0.95, on the probability among the five.
- **Margins differ.** Routine items on a 26-billion-parameter model will sit near 0.999. Prompt-rule items may sit near 0.96. Both land in the top bin, but their margins are very different, and the thinner one flips first under any disturbance.
- **Why subtraction does not fix it.** Subtracting the random comparison cancels this only if the swap and the noise disturb items in the same way. They do not: one is a structured replacement, the other spread-out noise.
- **Fix.** Match on the log-odds gap between the right candidate and the best wrong one, in narrower bins.

**RT-348, the control coordinates (lookup).**
- **The size of what is kept.** Goodfire reports that coordinate 2027 has "an average normalized value of +32.4" and accounts for "about 46% of the squared norm" of block 3's normalised activity.
- **It steers the block choice.** For the first block-3 layer's readers, it is "the largest (or 2nd largest) contributor" to the term that decides which block is read. The top five coordinates account for 30% to 62% of that term.
- **It steers keep and gain.** The keep and gain settings are computed from RMSNorm(m). So a message whose largest coordinates keep their true values keeps much of its true direction, its choice of block, and its keep and gain settings.
- **A contradiction.** Section 3 says the swap "changes both what the message adds and the keep and gain settings". Lines 107 to 108 say "the message the readers receive is computed only from another input, or from an average". Neither is true while the control coordinates are kept.
- **A possible leak.** If the coordinates' values vary from item to item or position to position, they also carry some of the true input's information.
- **What it allows.** Outcome D can then come from a partial swap.
- **What the rehearsal should report.** How much the control coordinates vary from item to item. And what share of the message's normalised length, and of the keep and gain settings, the swap actually changes.

**RT-349, what a "loss" means under five candidates.**
- **A different task.** Choosing among five is recognition, not recall. An item whose information is completely destroyed still scores right 20% of the time, or at whatever rate the wrong answers allow a lucky guess. So the most a cell can lose is about 0.80, and that ceiling may differ by kind.
- **Routines get easier.** A disturbed model may still recognise "Paris" among five capitals long after it could no longer produce it. That keeps routine losses small for a reason that has nothing to do with practice.
- **Thresholds inherited.** The δ of 0.10 and the target gap of 0.20 were set for generated answers starting from zero. They should be re-justified on this scale.

---

## 3. No verdict

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-350 | The two methods differ in kind, so "methods disagree" is a likely result | serious | ARGUED |
| RT-351 | The second model cannot complete stage one as written | serious | ARGUED |
| RT-352 | Rules left undefined | worth-noting | ARGUED |

The no-verdict paths already listed are:
- the normal-range check (RT-338);
- damage that cannot be matched (RT-339);
- fewer than three kinds of prompt-rule problem surviving (RT-344);
- a bypass check that fails for a harmless reason (RT-342);
- a required sample size above the pool (RT-340);
- the average method that cannot be computed (RT-335).

**RT-350, the two methods differ in kind.**
- **In the split design**, the two methods were close cousins: mean-ablation and projection of the same directions.
- **Here they differ in kind.** The swap gives a real message of the right sort, from an item of the same kind. The average gives a position-wise mean taken from text with no template and no task (RT-335). Even once it is fixed, the average remains a blurred message that no real input produces.
- **Result.** The two can be expected to differ in harshness, and so to land in different outcomes, which is read as "could not decide". The rehearsal should report each method's damage and swap size side by side, before registration, so that John can judge in advance whether agreement is plausible.

**RT-351, the second model.** On Inkling 2 Mini, section 8 runs "only the main removal, its comparisons and the identity check".
- **Two checks cannot run.** Stage one makes the result not testable if the mixing-bypassed check or the chained-lookup check fails. Both compare against a one-pass run, which Inkling 2 Mini does not have.
- **Missing steps.** The baseline filtering, the normal-range bound, the damage matching and the search for the control coordinates are not listed for it either.
- **Result.** As written, the second model's result has no route through stage one. Either stage one needs a version for Inkling 2 Mini, or its result should be labelled descriptive.

**RT-352, rules left undefined.**
- **Donor pool.** Section 3 draws donors from "the same kind" and then from "the same cell". The two differ a great deal: a capital can be swapped into a sum.
- **Donors on neutral text.** The design does not say how donors are drawn on neutral text, where damage matching is done.
- **Pass 3.** It does not say whether the donor's pass-2 sums come from the donor's unaltered run, or whether the "true" control values on pass 3 come from the recipient's unaltered run or its altered one.
- **"Typical coordinate".** The 10-times threshold is not defined, and the answer differs a lot when one coordinate holds 46% of the squared norm.
- **Leaving one kind out.** "Read with each kind left out in turn" has no rule for what happens when a reading with one kind left out differs.
- **Chat template.** Section 5 says the chat template must be settled to suppress reasoning. Section 6 says "no chat template is in play here".
- **One donor per item.** There is one donor draw per item, so the variation from which donor is drawn is not in the intervals. Several donors per item, averaged, would put it there.

---

## 4. Over-reading

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-353 | "The loop's value is the extra computing, not the feedback" contradicts the design's own arithmetic | serious | ARGUED |
| RT-354 | Outcome D is read as "the prediction failed for this placement" with no check that the swap removed what the loop supplies | serious | ARGUED |
| RT-355 | Several claims about the external pages go beyond what the pages say | worth-noting | ARGUED (lookup) |
| RT-356 | A per-word loop will be read as "the shared workspace" | worth-noting | ARGUED |
| RT-357 | One maker and one pretraining run, so the second model is not independent | worth-noting | ARGUED |

**RT-353, "extra computing, not feedback".** Section 7 allows this sentence: "If the one-pass run shows a large loss and the main removal shows outcome D, then the loop's value in this model is the extra computing, not the feedback."
- **The contradiction.** The design's own bypass argument shows that passes 2 and 3 without the message are pass 1 repeated. In this architecture, extra computing without feedback adds nothing at all.
- **What the swap separates.** The swap tests a right message against a foreign one. It does not test feedback against computing, and no condition in this design can test that, because the model cannot be given more computing without some message.
- **What the combination would mean.** A large one-pass loss together with D under the swap would mean that what the extra passes need survives the swap. That could be the kept control coordinates (RT-348), the same-kind donor's largely shared content (RT-345), or the mere presence of a message of the right kind.
- **Fix.** The allowed sentence should say that, and nothing about "computing".

**RT-354, outcome D has no check behind it.**
- **The gap.** The positive check on chained lookup tests one pass against three, not the swap. So nothing shows that the main removal takes away what the loop supplies on the one task known to need it.
- **What D could mean.** If the swap leaves chained lookup intact, D on routines and prompt-rule problems says the swap was too weak, not that "the model does not need the feedback". The design would still report it as the prediction failing.
- **Fix.** Add chained lookup under the swap and under the average, as a condition on reading D.

**RT-355, the external pages (lookup).** What held:
- four readers per looped layer, one each for the three attention inputs and the expert sublayer, which gives 48;
- the training mix of 1:2:6:2:1 passes, then three passes only;
- the quoted warning "may behave unpredictably at pass counts other than 3";
- about 20 GB, at least 32 GB of memory, and the RTX 5090 and RTX PRO 6000 Blackwell;
- Hugging Face listed among the frameworks;
- chained lookup scored with five options and nothing written down;
- the message read from blocks 2 and 3 of the previous pass.

What goes beyond the pages:
- **"Same architecture".** "Goodfire describes Inkling 2 Mini, which has the same architecture as the research model." None of the three pages says this. The card calls the research model "a variable-looped counterpart to Inkling 2 Mini" that shares pretraining and the first stage of midtraining. Goodfire does not mention the research model. Its findings on block 3 and coordinate 2027 are about a model whose later training differs.
- **"Almost all of it from block 3".** Goodfire says the model "almost always reads from block 3" and "we often see the model attend mostly to block 3", with no numbers.
- **"The next pass's readers use them".** Goodfire reports this for the readers of the first block-3 layer in pass 2, not for every reader.
- **"On the first pass there is no message".** Goodfire does not state it (RT-342).
- **"A small learned network".** Goodfire gives linear maps passed through tanh, with the keep setting between 0 and 2 and the gain between −1 and 1. The design should give these ranges, because they bear on RT-339.
- **"Formats it was trained in".** The card gives the storage formats. I did not see a statement that the model was trained in them.
- **The design note's figures.** The note's DeepSWE figures (47.4% to 0.7%) and SimpleQA figures (7.3% to 6.3%) are not in the announcement's text as I read it. They may be in charts I did not open. The announcement's text gives Inkling 2 Mini 48.2% on DeepSWE.
- **The 0.15 threshold.** The chained-lookup threshold, a loss of at least 0.15 on chains of four or more lookups, is not traced to any number on the pages. The card's chart for a different task, GraphWalks, reads 23.5 at one pass and 64.3 at three, which suggests the threshold is reachable but does not ground it.

**RT-356, a per-word loop is not the shared workspace.** H1's workspace is one space "that the rest of the system reads from and writes to". The loop's channel is per word ("over a single token"), and the integration across words, done by ordinary attention, is untouched. The required sentence for outcome A is careful. But "the loop does H1's job" will travel as "the model's workspace was found". Prompt-rule problems will also travel as "anything new", which they are narrower than.

**RT-357, one maker, one pretraining run.** The two models share pretraining. A result on both is close to one result twice. The design says so, and that should be kept in every summary.

---

## Kill case

As drafted, the test's best result would not show what it is named for, and its likeliest result is no verdict.
- **Outcome A without the structure.** The swap changes about 12 of 27 positions in a routine item and about 30 of 56 in a prompt-rule item. The prompt-rule items are also two to four times longer. The random comparison adds one noise size to every item. So a loop with nothing special about rule-following would still produce outcome A. The donor's working can also intrude as a wrong answer that looks like lost flexibility.
- **Outcome D without a test.** Keeping the control coordinates true keeps close to half of the normalised message, and with it most of the choice of block and the keep and gain settings. Nothing checks that the swap removes what the loop supplies even on chained lookup. So D can mean only that the swap was weak, yet it would be reported as the prediction failing.
- **No verdict.** The average method cannot be computed for most prompt-rule positions, because the neutral passages are too short. Whether the result can be read at all comes down to the swap's harm per unit of length compared with noise, the same quantity that sank the split test at 9.4 times. The split design's rule for reporting that margin and returning to John was dropped. The two methods differ in kind, so they are likely to disagree. The routine pool for test items caps the cell at 134, and it overlaps the pilot set in two kinds. The second model cannot pass stage one at all.
- **The central sentence.** The one sentence the design allows beside outcome D, that the loop's value is "the extra computing, not the feedback", contradicts its own bypass arithmetic.

It should not be registered until there is:
- a neutral set long enough, and templated, for the average method;
- a measured swap size for each item, matched or adjusted across the cells, with a long routine control;
- a defined way of scoring the five candidates at their own positions;
- the control-coordinate choice tested for how much of the message it keeps;
- chained lookup under the swap, as a condition on reading D;
- the room-under-the-bound rule restored;
- a sample size checked against the pool;
- a stage one the second model can actually complete.
---

## The filer's check of the findings (not part of the review)

*Written by the design's author, 2026-11-20. It does not close any finding: under the review protocol, closing a finding is the reviewer's check of the fix, not the author's word. It records where the author checked a finding against the record, and two places where the review's account of the external pages is itself wrong.*

**Checked and holds.**
- **RT-335, the neutral passages are too short.** The committed pilot file `experiments/09-split-removal-test/batteries/pilot/neutral.json` holds 200 passages of 17 to 23 words. The review measured a maximum of 22 on freshly generated passages, which makes no difference to the finding.
- **RT-341, pilot and test overlap.** `batteries.py` draws the weekday from one list of all seven days for both halves (`DAYS`, line 33; `r_next_day`, line 125), so every next-weekday test prompt repeats a pilot prompt.
- **RT-353, "extra computing, not feedback".** The review is right. The design's own bypass argument says passes without the message repeat pass 1, so no condition can separate feedback from computing, and the allowed sentence has to go. The design note's framing of the swap as separating the two was wrong in the same way.

**Two places where the review's account of the pages is wrong.**
- **RT-355, the DeepSWE and SimpleQA figures.** The review says the note's figures (DeepSWE 47.4% at three passes and 0.7% at one; SimpleQA Verified 7.3% and 6.3%) are not in the announcement's text. They are not, but they are in the research model's card, in its evaluation table (section 5 of https://thinkingmachines.ai/model-card/tml-d24-varloop-research/, and the same table on the Hugging Face page), which the note and the design cite. They hold.
- **RT-355, "formats it was trained in".** The review says it did not see a statement that the model was trained in its storage formats. The card says: "The model uses the same mixed NVFP4 and MXFP8 precision it was trained in." The design's sentence holds.

The rest of RT-355 stands. Most importantly, no page says the research model has the same architecture as Inkling 2 Mini, so everything the design takes from Goodfire is about a model whose later training differs.
