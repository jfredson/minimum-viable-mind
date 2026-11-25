*Filed 2026-11-20 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design nor the fixes. It worked read-only in a detached worktree at commit 7760fda and changed nothing in the repository. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.2

*Reviewer: a fresh Claude Code session. I did not write the design or its fixes. I worked read-only in the detached worktree `closure-loop-design-2026-11-20` at commit 7760fda and changed nothing in the repository. My three scratch scripts are in my session's scratchpad folder, outside git, and none of them writes a file. No model or tokeniser was downloaded and nothing was spent. New findings continue the red-team numbering from RT-358.*

---

**What I opened.**
- **Read in full:**
  - the target, `docs/loop-removal-test-design-2026-11-20.md` (version 0.2, including its change log);
  - the inside review of version 0.1, `docs/reviews/2026-11-20-loop-removal-test-design-gate-c-tier1-claude-code.md`, including the filer's check, which I read as the author's note and not as part of the review;
  - the split test's battery generators, `experiments/09-split-removal-test/src/batteries.py`.
- **Read in part:**
  - version 0.1 of the design (`git show 4f68df5:...`), sections 2 to 5;
  - `docs/outside-review-protocol.md`, the tier 1 description and the section "The closure rule, which is the new part";
  - the first 60 lines of the battery authoring specification;
  - the lines of the three-hypotheses proposal that state H1, the hypothesis being tested;
  - the "Ablation method" bullet of experiment 01's pre-registration;
  - the first passages of the committed pilot neutral set (`batteries/pilot/neutral.json`) and of the committed pilot prompt-rule file.
- **Ran:**
  - `twins.py`, which builds twin pairs the way version 0.2 describes and measures their lengths, the span a same-kind donor swap changes, how many donors each item can have, and what the 10% swap-size matching rule does;
  - `pools_power.py`, which counts the half-B pools under version 0.2's rules and simulates outcome A with and without the "depends on one kind" readings;
  - `avgdef.py`, which checks whether the new average is defined at every position an item uses;
  - two one-off checks: a word-list check of the letter-code kind, and a grep of the target.

**What I did not open.** I did not open the three external pages: the model card, the Hugging Face page, or Goodfire's write-up. The changes made for the finding about external-page claims (RT-355) withdraw or narrow claims and add none, so reopening the pages was not needed to judge them. I did not open the design note, the split removal test design, the split test's rehearsal records, the positions ledger, `STATUS.md`, or any code under `src/mvm/`. The model's own chat template and tokeniser are not in the repository. Every token count below therefore comes from a stand-in splitter, and every template comes from a stand-in template. I say so at each place it matters.

**How the twin pairs were built.** Version 0.2's new prompt-rule kinds have no code yet, so I wrote stand-in generators from the design's own descriptions, using the committed pools in `batteries.py` (the syllables, nouns, countries, opposites and operator symbols):
- the invented operator, as in the split test;
- the invented unit ("1 zibvam is 3 tovjots. How many tovjots are 4 zibvams?");
- the lookup in a table of three to six invented words and colours;
- the letter code: a one-place shift of a three-letter noun, with a table for the letters used, asked as a decoding.

Each routine twin carries its partner's rule word for word, followed by a routine question of a kind drawn at random from the five routine kinds. The design does not say how routine kinds are paired with rule kinds.

The stand-in splitter counts these as one token each: common words, numbers, and the real nouns, countries and capitals. Any other word is split every three letters, which stands in for the invented words breaking into several tokens. The stand-in template adds 12 tokens before the user text and 4 after it, the same assumption the version 0.1 review made. I built 300 pairs, 75 for each prompt-rule kind.

---

## Verdicts on RT-335 to RT-357

| Finding | Verdict | Label |
|---|---|---|
| RT-335 (fatal): the average method could not be computed | **Closed, with conditions** | MEASURED (stand-in template) |
| RT-336: five-candidate scoring left undefined | Closed, with conditions | ARGUED |
| RT-337: nothing showed the block sums can be hooked on a 32 GB card | Cannot be checked on paper; owed at step 4a | ARGUED |
| RT-338: the normal-range check and the dropped "room under the bound" rule | Closed on paper; the ratio is owed at step 4b | ARGUED |
| RT-339: matching on damage may be unreachable, and the noise was undefined | Closed, with conditions (see RT-366) | ARGUED |
| RT-340: the sample size and the cap on the routine pool | **Not closed** (see RT-361 and RT-363) | MEASURED |
| RT-341: pilot and test items overlapped | Closed, with conditions | MEASURED in part |
| RT-342: the bypass check rested on three unstated facts and had no noise floor | Closed on paper; the facts are owed at step 4a | ARGUED |
| RT-343: the amount of work was undercounted | Closed as a disposition (see RT-369) | ARGUED |
| RT-344: three prompt-rule kinds may not survive | Cannot be checked without the model; owed at step 4b | ARGUED |
| RT-345 (fatal): the swap's dose and the item lengths differed between the cells | **Not closed.** The length half closes; the dose half is reopened in the other direction | MEASURED (word and token proxy) |
| RT-346: the donor's answer could intrude among the candidates | Closed, with a condition | ARGUED |
| RT-347: the confidence bins were too coarse | Closed in intent; conflicts with the pairing (RT-360) | ARGUED |
| RT-348: keeping the pass-counting coordinates kept half the message | Closed | ARGUED |
| RT-349: five-candidate scoring changes what a loss means | Closed, with conditions (see RT-368) | ARGUED |
| RT-350: the two methods differ in kind | Closed as a rule; likely to trigger (RT-364) | ARGUED |
| RT-351: the second model could not pass stage one | Closed | ARGUED |
| RT-352: rules left undefined | **Not closed**: one fix is only in the change log | MEASURED (grep) |
| RT-353: the "extra computing, not feedback" sentence | Closed | ARGUED |
| RT-354: outcome D had no check behind it | Closed, with a condition (RT-367) | ARGUED |
| RT-355: claims that went beyond the external pages | Closed | ARGUED |
| RT-356: a per-word loop would be read as the shared workspace | Closed | ARGUED |
| RT-357: one maker and one pretraining run | Closed | ARGUED |

### The two fatal findings

**RT-335, the average method could not be computed: closed, with conditions (MEASURED).** Version 0.1 averaged at each position, and the neutral passages were far shorter than the items, so most positions had no data. Version 0.2 pools the average over positions, separately for each pass and each block sum. Template positions are averaged by template token. The single measurement that would come out wrong if this fix were wrong is whether any position an item uses, candidates included, is left without a defined average. I rendered the committed 200 neutral passages and an operator item in a stand-in chat template, under three ways the neutral set might be rendered:

```
python3 -I avgdef.py .../batteries/pilot/neutral.json
[neutral as user turn + generation prompt] item positions 40; template positions with no template average: none;
  text and candidate positions use the pooled prose average over 4265 neutral text positions
[neutral as user turn, no generation prompt] ... template positions with no template average: ['assistant']
[items need an empty-reasoning block, neutral does not have it] ... no template average: ['<think>', '\n\n', '</think>', '\n\n']
template tokens filling more than one slot in one item: {'<|im_start|>': [1, 36], '\n': [3, 35, 38], '\n\n': [40, 42]}
committed neutral passages: 200, text tokens min 19 max 25
```

The output matches the closure's claim on one condition. When the neutral set carries every template token the items carry, every position has a defined average at any length, and that includes the candidate positions, which get the pooled prose average. So the method can now be computed, and the fatal part of RT-335 closes. It closes on these conditions:
1. **Same template tokens.** The neutral set must be rendered with every template token the items use. That includes the generation prompt and any block used to suppress written reasoning, which step 4a has not settled yet. If it is not, those positions have no average.
2. **"By template token" needs a definition.** In one item the newline fills three different slots of the template. The design must say whether the average is pooled by token identity, which mixes those slots, or by template slot.
3. **Re-run with the real template.** This check must be run again with the model's real template and tokeniser at step 3, and the result committed.

Two things this check does not cover:
- **Damage.** Whether the pooled average does far more damage than the swap can only be measured on the model (RT-364).
- **Experiment 01.** The sentence saying experiment 01's mean-ablation pooled over positions "in effect" is unchecked. Experiment 01's pre-registration says it mean-ablated "located components" and does not say how positions were treated.

**RT-345, the swap's dose and the item lengths differed: not closed (MEASURED, with a token proxy).** The finding had two halves, length and dose.

*Length: closes.* The twin design matches the two cells on length:

```
python3 -I twins.py .../experiments/09-split-removal-test/src
pairs 300; length incl. template+candidate: P median 50.0 R median 52.0
within-pair |P-R| tokens: median 2.0 max 5; share <=3: 0.64
```

The twins differ by 2 stand-in tokens at the median and by 5 at most. That matches the design's "a few tokens at most". So the specific route to a false outcome A that RT-345 named, prompt-rule items simply being two to four times longer, is closed.

*Dose: does not close.* The swap only changes positions after the first token where donor and recipient differ. Positions where the two have the same token also change less. Version 0.2 draws donors from "the same kind and the same cell", and for a routine twin that phrase has two readings. Kind could mean the routine question's kind (a sum, say), whose donor then carries a preamble of any rule kind. Or it could mean the rule kind of the preamble. I measured both readings with five donors per item. The "proxy swap size" counts 1 for each changed position with a different token and 0.3 for each changed position with the same token. Those weights are my assumption; the real distances need the model.

```
[R donors by routine kind] P: mean changed span 31.1 tok, same-token share in span 0.49, no eligible donor 1, fewer than 5 donors 4, proxy swap size 20.5
[R donors by routine kind] R: mean changed span 35.5 tok, same-token share in span 0.25, no eligible donor 5, fewer than 5 donors 15, proxy swap size 30.2
[R donors by routine kind] proxy swap size ratio larger/smaller: 1.476
[R donors by preamble rule kind] P: ... proxy swap size 20.7 ;  R: ... proxy swap size 23.1
[R donors by preamble rule kind] proxy swap size ratio larger/smaller: 1.118
seeds 1, 2, 3: routine-kind reading 1.461, 1.470, 1.490; rule-kind reading 1.133, 1.128, 1.147
```

The twins match on length but not on the span the swap changes. A prompt-rule donor of the same kind shares its rule's fixed wording at the same positions. A routine donor shares less:
- **Routine-kind reading.** The donor's preamble is often of another rule kind, so about half as many changed positions keep the same token (0.25 against 0.49), and the proxy dose is about 47% larger in the routine cell.
- **Rule-kind reading.** The gap is still 12% to 15%, beyond the 10% the design allows.

The imbalance now runs the other way from version 0.1, so it no longer manufactures outcome A. It could instead push the result toward B (selective loss on routine questions, read as the prediction failing) or C (general loss). Scaling the noise to each item corrects for this only if the structured swap and the noise cost the same per unit of distance, which nobody has measured.

*Dropping items to match makes it worse.* I applied the design's rule: drop items from the cell with the larger swap sizes, largest first, until the cells' means are within 10%. I then counted the twins left without their partner.

```
[match, R donors by kind, bump none] ratio 1.48; larger cell R; dropped 175 of 295;
  rule kinds {operator 75, unit 75, lookup 70, code 75} -> {operator 34, unit 34, lookup 0, code 52}; twins left unpaired 179
[match, R donors by rulekind, bump none] ratio 1.13; dropped 6 of 299; lookup 74 -> 68; twins left unpaired 6
[match, R donors by rulekind, R 15% larger per position] ratio 1.30; dropped 38; lookup 74 -> 36; twins left unpaired 38
```

The dropping rule falls on the items with long preambles of varying length, which here are the lookup tables. Under the routine-kind reading it removes every routine twin that carries a lookup preamble. The lookup items stay in the prompt-rule cell, so the cells stop being twins in layout. The rule also leaves 6 to 179 partners without a twin, even though the analysis resamples by pair.

So the decisive measurement is owed: the real per-item swap sizes, in the model's own block sums, on the pilot pairs, under a fixed donor rule. It cannot be made without the model, and it belongs at step 4b. Before then, the donor rule and the matching rule need fixing (RT-358, RT-359). **RT-345 stays open.**

### The serious and worth-noting findings

- **RT-336, five-candidate scoring left undefined: closed, with conditions (ARGUED).** Candidates are now of equal token length, scored by the sum of their tokens' log-probabilities, and compared by a softmax over the five. The donor runs on its own prompt and right answer, so its sums exist at the candidates' positions. What remains is how many items the equal-length rule drops in each kind, and what that does to the answer values kept (RT-368). This can be measured at step 3 once the tokeniser is available.
- **RT-337, hooking unproven: cannot be checked on paper.** Feasibility is now the first step and is priced on its own (step 4a), and a failure returns the design to John. This is the right order. The measurement itself is owed at step 4a.
- **RT-338, the normal-range check: closed on paper.** The "room under the bound" rule is restored, with the damage ratio reported, and a failed or tight bound returns the design to John. The ratio itself is owed at step 4b.
- **RT-339, matching on damage: closed, with conditions.** The noise now goes in before normalisation and touches every coordinate. Too low a damage ceiling returns the design to John, and an unmatched outside-the-loop comparison renames an A or B "specificity not checked". The conditions are in RT-366.
- **RT-340, sample size and the pool cap: not closed (MEASURED).** My simulation reproduces the review's figures: a 0.79 chance of outcome A on both methods at 120 pairs when the comparison loses 0.10, and 0.80 at 200 pairs when it loses 0.20. But the design's claim that half B can supply at least 300 pairs fails under its own 25% cap on any one kind (RT-361). The committed simulation also leaves out the "depends on one kind" rule (RT-363).
- **RT-341, pilot and test overlap: closed, with conditions (MEASURED in part).** The next-weekday kind is gone. Splits with no shared answers are feasible: sums of 2 to 49 split at an answer of 50 leave 1,176 ordered pairs in half B, and products split at 40 leave 60. The conditions:
  - The overlap script checks "answer values" with no limit by kind. If it compares across kinds, it fails at once: 6 of the 31 possible pilot unit answers (2 to 9 times 2 to 9) equal some half-B sum.
  - The script must also say whether wrong candidates drawn from half A count as overlap, for example neighbouring capitals.
- **RT-342, the bypass check: closed on paper.** The check is now defined from the code, the three facts it needs are confirmed first, and the tolerance comes from a measured noise floor. The facts are owed at step 4a.
- **RT-343, the amount of work: closed as a disposition.** The count is to be redone from the committed code. One arithmetic point is in RT-369.
- **RT-344, prompt-rule kinds surviving: cannot be checked without the model.** One-step kinds are a sensible answer, and the return-to-John rule protects the design. One kind has a construction problem that can be seen on paper (RT-368).
- **RT-346, the donor's answer intruding: closed, with a condition.** Donors' right answers are excluded from the candidates. With multi-token answers, a candidate that shares the donor answer's first token can still be favoured. The condition is that the rehearsal reports how often the chosen candidate shares a first token with the donor's answer.
- **RT-347, the confidence bins: closed in intent.** Matching on the margin between the right candidate and the best wrong one, in bins 0.5 wide, answers the finding. It breaks the pairing, though (RT-360).
- **RT-348, the kept coordinates: closed.** Dropping the "keep true values" rule is justified. A donor ran three passes, so its pass-counting values are a real three-pass signal, and nothing of the recipient leaks through them. If those values hardly vary between items, the swap leaves much of the normalised message as it was. That is the message's honest content, not a leak. The bites check, which asks whether the removal costs the one task known to need the loop, is what guards against a swap too gentle to matter. The rehearsal's report of how much these coordinates vary by position and by item stays a condition.
- **RT-349, what a loss means under five candidates: closed, with conditions.** The normalised scale and the recognition statement answer the finding. Close wrong answers of equal token length are hard to build for plurals and opposites (RT-368).
- **RT-350, the two methods differ in kind: closed as a rule.** The factor-of-two return to John answers the finding. RT-364 explains why the rule is likely to be triggered.
- **RT-351, the second model: closed.** It is descriptive only and keeps its own checks.
- **RT-352, rules left undefined: not closed (MEASURED by grep).** The change log says "donors on the neutral set are other neutral passages of similar length". Searching the target for "similar length" finds that phrase only at line 543, inside the change log. Sections 3 and 4, which govern the work, never say how donors are drawn on neutral passages. Yet the swap's damage on the neutral set, the per-passage swap size and the damage matching all need such a donor. The other items under RT-352 are fixed in the body: donors from the same kind and cell, five donors, sums from the donor's unaltered run, the leave-one-kind-out rule, and the sentence on the chat template.
- **RT-353, "extra computing": closed.** Section 1 now says the test cannot separate feedback from computing, and section 7's allowed sentence speaks only of what survives the swap.
- **RT-354, outcome D's check: closed, with a condition (RT-367).** The new "too weak to read" outcome is the right answer.
- **RT-355, the external pages: closed.** The claims are withdrawn or narrowed, and the facts taken from Goodfire are moved to step 4a.
- **RT-356, the workspace: closed.** Section 1 says the per-word loop is narrower than a shared workspace, and section 7 bars both phrases from every summary.
- **RT-357, the shared pretraining: closed.** Every summary must say the second model shares pretraining.

---

## New findings

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-358 | The donor rule for routine twins has two readings, and under either the routine cell takes a larger swap than the prompt-rule cell | serious | MEASURED (proxy) |
| RT-359 | Matching swap sizes by dropping the largest items removes whole rule kinds from one cell and breaks the pairs | serious | MEASURED (proxy) |
| RT-360 | Matching on margin removes single items, which breaks the pairs the analysis resamples | serious | ARGUED |
| RT-361 | Half B cannot supply 300 pairs of distinct routine questions under the 25% cap | serious | MEASURED |
| RT-362 | The 25% cap cannot hold in the prompt-rule cell if only three kinds survive | worth-noting | MEASURED (arithmetic) |
| RT-363 | The power simulation leaves out the "depends on one kind" readings, which cut the chance of a clean A roughly in half | serious | MEASURED |
| RT-364 | The pooled average gives one constant message at every text position, so it is likely to fail the factor-of-two rule, and no fallback is fixed in advance | serious | ARGUED |
| RT-365 | A routine question behind an irrelevant rule also tests ignoring the rule, which changes what the routine cell measures | serious | ARGUED |
| RT-366 | Rules for neutral donors, matched draws and the spread of noise across positions are missing from the body | worth-noting | MEASURED (grep) |
| RT-367 | The bites check can be passed by generic damage | worth-noting | ARGUED |
| RT-368 | Building the candidates: equal token length, close wrong answers, and the letter-code kind | worth-noting | MEASURED in part |
| RT-369 | The longest items lack donors, and the forward-pass count leaves out the five candidates | worth-noting | MEASURED (proxy) / ARGUED |

**RT-358, the routine twins' donor rule (serious, MEASURED with a proxy).** Section 3 says "a different item of the same kind and the same cell". A routine twin has two kinds: the kind of its question and the kind of its preamble's rule. Under the question-kind reading, the routine cell's proxy dose is about 1.47 times the prompt-rule cell's. Under the rule-kind reading, it is about 1.13 times. Both are beyond the design's 10%, and both runs are under RT-345 above. Either way the cells stop being matched in the span the swap changes, which was the purpose of the twins. One fix to consider is to draw donors by pair: give the prompt-rule item a same-kind donor, and give its routine twin that donor's own twin. Then the preambles diverge in the same place in both cells, and only the question part differs. The design should state the rule and measure the effect on the pilot pairs.

**RT-359, the 10% matching rule biases the cells (serious, MEASURED with a proxy).** Dropping the largest items "from the larger cell" removes the items with long preambles of varying length, here the lookup tables: 70 down to 0 under one reading, 74 down to 36 under a milder one. Their partners stay in the other cell. Two things follow.
- **Kind and layout.** The cells' kind mix and layout drift apart again. A kind can also vanish from one cell, which then interacts with the "depends on one kind" rule and the at-least-three-kinds rule.
- **Pairing.** Partners are left without their twins (6 to 179 in my runs), but section 6 resamples by pair.

A fix should drop or keep pairs, never single items, and match within each rule kind. Alternatively, it could adjust for swap size in the analysis instead of dropping items. Either way, the kind mix before and after should be reported.

**RT-360, margin matching against the pairing (serious, ARGUED).** Section 5 first keeps pairs whose twins both pass, then "the R and P cells are then matched on margin in bins 0.5 wide". Matching cells bin by bin removes single items, which breaks pairs in the same way. There is a second problem. Practised facts are likely to sit at much larger margins than one-step invented rules, and the bins have no top. So matching could leave very few pairs, and the pairs left would be routine items with unusually thin margins. Both the pairing rule and the overlap of the margin distributions must be settled. The overlap is a measurement owed at step 4b.

**RT-361, the claim of 300 pairs fails under the design's own cap (serious, MEASURED).**

```
python3 -I pools_power.py
sums: half B (answers > 50) 1176; products: 121 ordered pairs, 53 distinct answers, half B (answers > 40) 60
capitals half B 30; plurals half B 60; opposites half B 40 (20 pairs, both directions)
  target 300 pairs, 25% cap = 75 per kind: unique routine questions available 265 -> SHORT
  target 240 pairs ... 250 -> OK
```

The pools are set at the design's minimums: 60 countries, 120 nouns and 80 adjectives, halved. No kind may exceed 75 of 300 questions, so half B holds at most 265 distinct routine questions. That is before the equal-length, margin and swap-size filters remove any. There are two ways out:
- **Allow repeats.** Let a routine question repeat behind different preambles. The design must then say so, and the pool sizes are no longer what limits the count.
- **Enlarge the pools.** For example, at least 150 countries, so that 75 fall in each half, and more adjectives.

**RT-362, the 25% cap in the prompt-rule cell (worth-noting, arithmetic).** The rule reads "No single kind may make up more than 25% of a cell". With four prompt-rule kinds, each must be exactly 25%. With three surviving, which section 5 allows, each is at least 33%. Read literally, the two rules conflict. The fix is to say the cap applies to routine question kinds only.

**RT-363, the power simulation misses the leave-one-kind-out rule (serious, MEASURED).** Outcome A is renamed "depends on one kind" unless every reading with one kind left out (and its twins with it) is also A. I added that requirement to a simulation of the outcome-A rule on both methods. In the simulation, items start right, a broken item still guesses right one time in five, the swap averages five donors and the comparison averages twenty draws, intervals use a normal approximation, and there are 400 runs per row. The effect is assumed equal in every kind, which is the most favourable case.

```
pairs 120, comparison loss 0.10, shared fragility 0.0: A on both methods 0.79; A and every leave-one-kind-out reading also A 0.45
pairs 120, comparison loss 0.10, shared fragility 0.6: 0.92; 0.67
pairs 200, comparison loss 0.10, shared fragility 0.0: 0.94; 0.76
pairs 200, comparison loss 0.20, shared fragility 0.0: 0.80; 0.44
pairs 300, comparison loss 0.20, shared fragility 0.0: 0.91; 0.66
```

The first numbers reproduce the earlier review's figures. With the leave-one-kind-out rule added, a true gap of 0.20 reaches a clean A only 44% to 76% of the time at the sizes the design contemplates. The rest goes mostly to "depends on one kind", which gives no reading. The committed sample-size simulation must include this rule. Otherwise it will certify a size that gives a clean A about half as often as it says. Together with RT-361, this answers the question of whether the design can still return an outcome. It can return A, B, C or D, but at the planned sizes a true effect is about as likely to come back as "no reading" as it is to come back as A. The many return-to-John rules are not the problem. They act in the rehearsal, before registration, which is the right place.

**RT-364, the pooled average and the factor-of-two rule (serious, ARGUED).** Under version 0.2, every non-template position gets the same message on a given pass. That holds for the prompt, the question and the candidates alike. Whatever the readers draw from how the message varies by position is removed. The swap instead keeps a real, position-varying message from another item. The average could therefore be far harsher than the swap, or far milder, because it is a "typical" message. Either way it may well trip the factor-of-two return. No fallback is fixed in advance, such as averaging by bins of relative position, or by token identity outside the template. If the factor-of-two rule triggers, choosing a new average after seeing the rehearsal's damage figures would mean choosing the method from its results. The fix is to name one fallback now, or to say that a trigger ends the average method and the outcome rests on the swap alone. Ending it would need John's ruling, because the "both methods agree" rule would change.

**RT-365, a routine question behind an irrelevant rule (serious, ARGUED).** The twin makes the routine cell "a practised answer while ignoring a rule just read". That is not simply "routine, practised output", the half of H1's prediction that is meant to keep running. Take an operator rule ("a ◇ b means 2 times a, plus b, minus 1") followed by "What is 4 plus 7?". It invites the model to apply the rule. Ignoring a context you have just been given is arguably flexible control, the half H1 predicts will collapse. A swap that weakens it would show up as a routine loss and push the result toward C or B, for a reason that has nothing to do with practice. The section 7 sentence ("routine questions behind the same rule") is honest about this, but section 1 still frames the cell as H1's "routine, practised output". To fix it:
- do not pair an arithmetic rule with an arithmetic question;
- keep the value the rule would give out of the routine twin's candidates;
- add a baseline check that each routine twin is answered as well behind its rule as with no rule;
- say in section 1 what the routine cell now measures.

**RT-366, rules missing from the body (worth-noting, MEASURED by grep).**
- **Neutral donors.** The only statement of how neutral passages get donors is in the change log (RT-352 above).
- **Matched draws.** Stage one still says "fewer than 10 of the 20 random draws can be matched on damage". In version 0.2, though, one shared factor is chosen so that the average damage lands within 20%. With a single factor, a draw being "matched" no longer has a meaning.
- **Spread of the noise.** The noise is scaled to each item's total swap size, but nothing says how it is spread across the changed positions: evenly, or in proportion to each position's own swap distance.
- **Five donors on the neutral set.** It is not said whether the neutral set's swap damage averages five donors, as the items do. If it does not, the damage the noise is matched against has a different dose from the one the items receive.

**RT-367, the bites check can be passed by generic damage (worth-noting, ARGUED).** The check measures the main removal's cost on chained lookup against the unaltered run, not against the random comparison. A removal whose effect on chained lookup is no more than generic damage of its size would still pass it and let outcome D be read. Reporting chained lookup's excess over the matched random comparison beside it, or requiring that excess, would close this.

**RT-368, building the candidates (worth-noting, MEASURED in part).**
- **Numbers.** If the tokeniser splits numbers into single digits, the equal-length rule removes items whose answers sit near 10 or 100. That selects answer values in a way that may differ between kinds.
- **Plurals and opposites.** "Close" wrong plurals ("cates", "caten") are not real words and usually split into more tokens than the right answer, so equal length and closeness pull against each other.
- **The letter code.** The text says a shift is "applied to a three-letter word", with wrong answers that are "real three-letter words". If the right answer is the shifted string, it is almost never a word. None of 20 common three-letter nouns shifts to a listed word, and only 29 of the 1,142 three-letter entries in the system word list do (one-off check against `/usr/share/dict/words`). The right answer would then be the one non-word among five, which can be guessed without the rule. The kind must be asked as a decoding. Even then, a uniform one-place shift is practised knowledge, so the "rule is needed" check may drop the kind.

Drop rates for each kind should be reported at step 3.

**RT-369, smaller gaps (worth-noting).**
- **Donors for the longest items** (MEASURED, proxy). The rule that donors must be at least as long as the recipient left 1 to 5 items with no eligible donor, and 3 to 15 with fewer than five. These are always the longest items in a kind, and they need a stated rule.
- **The forward-pass count** (ARGUED). About 95 runs over roughly 700 items with five candidates each is about 330,000 continuations, unless the candidates share the prompt's computation. That is above the "100,000 to 200,000" in section 8.

---

## Verdict

Version 0.2 should not go to John for rulings yet. One fatal finding closes and the other does not. The average method (RT-335) can now be computed at every position, candidates included. That holds on the conditions that the neutral set carries every template token the items do, that "by template token" is defined, and that the check is repeated with the real template at step 3. The twin design fixes the length half of the swap-dose finding (RT-345), and the twins now differ by a few tokens. But the dose half is not closed. Under either reading of the donor rule, the span the swap changes still differs between the cells by more than the 10% allowed, now with the routine cell taking more (RT-358). The rule for dropping items to match then removes whole rule kinds from one cell and breaks the pairs the analysis rests on (RT-359, RT-360). The decisive check, real swap sizes in the model's own block sums on the pilot pairs, needs the model. It cannot be closed on paper. What can and should be fixed first:
- a donor rule that gives the two cells the same changed span, for example donors drawn by pair;
- matching and filtering that act on whole pairs, within each rule kind;
- the routine-pool arithmetic under the 25% cap, and where that cap applies (RT-361, RT-362);
- a sample-size simulation that includes the "depends on one kind" readings (RT-363);
- a fallback for the average fixed in advance (RT-364);
- the routine-twin construction, so that routine questions do not test ignoring the rule (RT-365);
- moving the neutral-donor rule from the change log into the body (RT-352, RT-366).

Once those are fixed, the remaining choices in section 10 can go to John, with RT-345 carried as an open fatal item. Its closure would then be the reviewer's measurement at step 4b, which must be done before any registration.
---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-20. It closes nothing.*

- **RT-352 and RT-366, the neutral-donor rule is only in the change log.** Confirmed. The phrase "similar length" appears once in the design, at line 543, inside the change log. Sections 3 and 4 do not state the rule.
- **RT-366, "matched" draws.** Confirmed. Stage one (line 327) still says "fewer than 10 of the 20 random draws can be matched on damage", while section 4 now sets one shared factor for all draws, so a single draw being matched has no meaning.
- **Where things stand.** RT-335, the finding that the averaging method could not be computed, is closed with three conditions. RT-345, the finding that the swap's dose and the item lengths differed between the cells, stays open, and the reviewer judges that its decisive check needs the model. Twelve new findings are raised, RT-358 to RT-369: six serious and six worth noting. Version 0.2 does not go to John for rulings until a version 0.3 answers them.
