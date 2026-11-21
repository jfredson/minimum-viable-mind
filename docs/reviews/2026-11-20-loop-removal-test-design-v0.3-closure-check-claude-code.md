*Filed 2026-11-20 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the two earlier reviews. It worked read-only in a detached worktree at commit 8bd34cd and changed nothing in the repository. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.3

*Reviewer: a fresh Claude Code session. I did not write the design, any of its fixes, or the two earlier reviews. I worked read-only in the detached worktree `closure2-loop-design-2026-11-20` at commit 8bd34cd and changed nothing in the repository. My scratch scripts are in my session's scratchpad folder, `/private/tmp/claude-501/-Users-john--claude-spares-spare-d40STS/5395ec4e-ea35-4396-b824-dbb33c4ff595/scratchpad/`, outside git, and none of them writes a file. No model or tokeniser was downloaded, and nothing was spent. New findings continue the red-team numbering from RT-370.*

---

**What I opened.**
- **Read in full:**
  - the target, `docs/loop-removal-test-design-2026-11-20.md` (version 0.3, with both change logs);
  - the closure check of version 0.2, `docs/reviews/2026-11-20-loop-removal-test-design-v0.2-closure-check-claude-code.md`. I read its filer's check as the author's note, not as part of the review;
  - the split test's battery generators, `experiments/09-split-removal-test/src/batteries.py`.
- **Read in part:**
  - `docs/outside-review-protocol.md`: the tier 1 description and the section "The closure rule, which is the new part";
  - the opening and the first findings table of the inside review of version 0.1 (`docs/reviews/2026-11-20-loop-removal-test-design-gate-c-tier1-claude-code.md`);
  - the first lines of the committed pilot neutral set (`batteries/pilot/neutral.json`), which my scripts load in full;
  - the list of files changed between version 0.2 (commit 7760fda) and version 0.3 (`git diff --stat`).
- **Ran** five scratch scripts, each reported under the finding it bears on:
  - `twins3.py`, which builds twin pairs under version 0.3's rules, applies the donor rule by pairs, and measures the changed span and a proxy swap size in each rule kind. `twins3b.py` finds where the imbalance comes from;
  - `pools3.py`, which counts the half-B routine pools and checks whether the pairing exclusions can be met under the 25% cap;
  - `power3.py` and `power3c.py`, a sample-size simulation of outcome A under the narrower "depends on one kind" rule;
  - `code3.py`, which checks the letter-code kind against the system word list;
  - `slots3.py`, which checks averaging by template slot, the fallback bins, the plural candidates and the donors for neutral passages.
- **Searched the target** (grep) for rules that appear only in a change log, and for wording left over from earlier versions.

**What I did not open.** I did not open the external pages: the model card, the Hugging Face page and Goodfire's write-up. Version 0.3 adds no new claim from them. I did not open the split removal test design, the three-hypotheses proposal, the design note, the split test's rehearsal records, `STATUS.md` or any code under `src/mvm/`. The model's chat template and tokeniser are not in the repository. **Every token count below therefore comes from a stand-in splitter and a stand-in template, and every "swap size" below is a proxy, not a measurement on the model.** I repeat this wherever it matters.

**The stand-ins.**
- **Splitter.** Common words, numbers, real nouns, countries, colours and three-letter words count as one token each. Any other word is split every three letters, which stands in for invented words breaking into several tokens.
- **Template.** 12 tokens go before the user text and 4 after it. Where reasoning has to be suppressed, an empty-reasoning block of 4 more tokens is added.
- **Pools.** These are enlarged to version 0.3's minimums (150 countries, 240 nouns, 160 adjectives). Single-token placeholders fill the places beyond the committed lists.
- **Prompt-rule kinds.** These are written from section 5's descriptions: the operator, the invented unit, a lookup in a table of five to seven invented words with distinct colours, and decoding a three-letter word with an invented substitution table.
- **Twins.** Each routine twin carries its partner's rule word for word, followed by a routine question. The question is drawn from the routine kinds that section 5 allows for that rule kind, in turn.
- **Size.** 75 pairs for each rule kind, 300 in all, built from half B.

---

## Verdicts on the findings the second change log answers

| Finding | Verdict | Label |
|---|---|---|
| RT-335 (fatal), the averaging method could not be computed: its three conditions | **Closed.** The third condition is owed at step 3 | MEASURED (stand-in template) |
| RT-336, five-candidate scoring: drop rates by kind | Closed, with the condition owed at step 3 | ARGUED |
| RT-339, matching on damage | Closed (through RT-366) | ARGUED |
| RT-340, sample size and the pool cap | **Closed, with conditions** | MEASURED |
| RT-341, pilot and test overlap | Closed | ARGUED |
| RT-345 (fatal), the swap's dose differed between the cells | **Not closed. Cannot be closed on paper.** The proxy predicts that the step-4b check will fail in two rule kinds (RT-370) | MEASURED (proxy) |
| RT-346, the donor's answer intruding | Closed | ARGUED |
| RT-348, the pass-counting coordinates | Closed, with one small text gap (RT-379) | MEASURED (grep) |
| RT-349, what a loss means under five candidates | **Not closed for plurals** (RT-373). Closed for the other kinds | MEASURED |
| RT-352, a rule written only in the change log | Closed for the neutral donors. A related gap is in RT-378 | MEASURED (grep) |
| RT-358, the donor rule for routine twins was ambiguous | Closed as a rule. Its effect is carried under RT-345 and RT-370 | MEASURED (proxy) |
| RT-359, matching by dropping single items | Closed, with a condition (RT-375) | ARGUED |
| RT-360, margin matching broke the pairs | Closed for the pairing. The overlap of the margins is owed at step 4b (RT-375) | ARGUED |
| RT-361, 300 pairs not available under the cap | Closed | MEASURED |
| RT-362, the cap and the prompt-rule cell | Closed | ARGUED |
| RT-363, the leave-one-kind-out rule halved the chance of a clean A | **Closed**, but the narrower rule leaks (RT-371) | MEASURED |
| RT-364, no fallback for the average | Closed, with conditions (RT-376) | ARGUED |
| RT-365, a routine question behind an irrelevant rule also tests ignoring the rule | Closed, with conditions (RT-374) | ARGUED |
| RT-366, rules missing from the body | Closed | MEASURED (grep) |
| RT-367, the bites check could be passed by generic damage | Closed | ARGUED |
| RT-368, building the candidates | **Not closed for the letter code** (RT-372) or the lookup table (RT-377). Closed for numbers | MEASURED in part |
| RT-369, donors for the longest items, and the count of runs | Closed for items. Neutral passages lack the same rule (RT-378) | ARGUED |

### The two fatal findings

**RT-335, the averaging method could not be computed: closed (MEASURED, with a stand-in template).** The last check closed this finding on three conditions. Version 0.3 writes all three into the body:
- **Same template tokens.** Section 3 says the neutral set is rendered with every template token the items use.
- **Averaged by slot.** Template positions are averaged by their place in the template, counted from the start of the opening part and from the end of the closing part.
- **Re-run at step 3.** The check is to be repeated with the real template and committed (sections 5 and 9).

The single measurement that would come out wrong if the slot definition were wrong is this: some position an item uses would have no average, or a repeated template token would still share one average across different slots. I rendered the 200 committed neutral passages and all 600 stand-in items. The template included a generation prompt and an empty-reasoning block. Positions were keyed by slot as section 3 defines it.

```
python3 -I slots3.py .../batteries/pilot/neutral.json <scratchpad> .../experiments/09-split-removal-test/src
neutral passages 200; item positions with no slot or text average: none
template tokens that fill more than one slot, each now with its own average: {'<|im_start|>': 3, '\n': 4, '<|im_end|>': 2, '\n\n': 2}
```

The output matches the closure claim. Every position has an average, and the candidates' positions are included. The newline, which fills four slots, now gets four separate averages. The third condition can only be met at step 3, with the real template and tokeniser, and it stays owed there. Experiment 01's sentence is withdrawn, as the last check asked.

**RT-345, the swap's dose differed between the two task groups: not closed, and cannot be closed on paper (MEASURED, proxy).** Version 0.3 states this finding as open. Its fix is the donor rule by pairs. Its closure is a measurement on the model at step 4b. I judge that closure rule first, and then report the paper measurement the brief asked for.

*Is the step-4b closure rule a sound and decisive test?* In kind, yes. The fix claims that, under the pair donor rule, both cells receive the same dose of the swap. The real per-item swap sizes, read from the model's own block sums, are the one measurement that would come out wrong if that claim were wrong. Nothing on paper can stand in for it, because the swap size is a distance between real block sums. Reading the measurement within each rule kind, rather than over the whole cell, is also right, because the dropping of pairs happens within each rule kind. The rule has five gaps, and all of them can be fixed in text:
1. **Only one method is named.** The rule speaks of "the two cells' mean swap sizes" under the pair rule. But section 3 measures a swap size for each method, and section 5 matches on it for each method. The finding is about dose, so the average method's dose must be in the closure too. For the average, the changed span is the whole item, not just the part after the donor and recipient diverge.
2. **"A tenth" has no stated base.** Pairs are lost before swap matching in three ways: margin matching, the confidence filter, and pairs with no eligible donor. The rule does not say whether the tenth counts from before or after those losses.
3. **The tenth is only in step 9.** Sections 5 and 6 allow matching to drop up to a third of a kind's pairs before the design returns to John. In effect the stricter limit governs the pilot, but section 5's text does not say so. Nothing says what happens if the test set, at the registered run, needs more than a tenth.
4. **Which pairs are dropped is not checked.** RT-370 below shows that the dropped pairs would be those with longer routine questions, which means particular routine kinds. The person closing the finding should also report the routine-kind mix of the dropped pairs, not only the count.
5. **The step-3 estimate has no threshold.** Section 9 commits a word-level estimate of the changed span at step 3, before anything is rented. But nothing says what an imbalance in that estimate triggers. Unless it triggers a fix to the twin construction, the imbalance described below would first be met at step 4b, after money has been spent.

*The paper measurement.* I applied the pair donor rule exactly as section 3 states it:
- donor pairs are of the same rule kind;
- each twin takes the matching twin of the donor pair;
- each twin of the donor pair must be at least as long as its recipient's prompt plus its longest candidate;
- the donor's right answer is never one of the recipient's candidates;
- five donor pairs are drawn for each recipient pair.

The "changed span" counts the positions from the first token where recipient and donor differ, through the candidate. The proxy swap size counts 1 for each changed position whose token differs from the donor's, and a smaller weight for each changed position whose token is the same. I used the last check's weight of 0.3, and 0.0 and 0.6 to test how much the weight matters. **This is a proxy.** The real distances need the model.

```
python3 -I twins3.py .../experiments/09-split-removal-test/src
== pair donor rule, same-token weight 0.3
  op    pairs 75 (no donor 0) len P 48.0 R 52.0 | span P 29.0 R 33.5 | same-token share P 0.80 R 0.74 | proxy size P 12.9 R 15.7 ratio R/P 1.223 | drops to 10%: 20
  unit  pairs 75 (no donor 0) len P 44.5 R 43.5 | span P 31.4 R 31.0 | same-token share P 0.47 R 0.49 | proxy size P 21.0 R 20.3 ratio R/P 0.967 | drops to 10%: 0
  code  pairs 75 (no donor 0) len P 48.8 R 50.5 | span P 31.7 R 33.4 | same-token share P 0.74 R 0.65 | proxy size P 15.2 R 18.0 ratio R/P 1.190 | drops to 10%: 25
  look  pairs 74 (no donor 1, <5 donors 7) len P 72.4 R 73.2 | span P 59.3 R 60.5 | proxy size P 51.9 R 53.5 ratio R/P 1.032 | drops to 10%: 0
  seeds 1, 2, 3 R/P ratio: op 1.223 1.209 1.204; unit 0.967 0.951 0.952; code 1.190 1.175 1.194; look 1.032 1.028 1.030
== same-token weight 0.0:  op 1.368 (drops 12), unit 0.948, code 1.421 (drops 30), look 1.038
== same-token weight 0.6:  op 1.180 (drops 73), unit 0.979, code 1.106 (drops 4),  look 1.026
== variant, donor pair also of the same routine kind: op 0.993, unit 0.870 (drops 20), code 1.042, look 1.017 (no donor 5, <5 donors 20)
```

The proxy dose differs by kind:
- **Within 10%:** the unit and lookup kinds, under every weight.
- **Beyond 10%:** the operator and letter-code kinds. There the routine cell takes 19% to 22% more of the proxy dose at weight 0.3, and 10% to 42% more across the three weights.

Matching to 10% would then drop:
- 20 to 25 of the 75 pairs in those two kinds at weight 0.3 (27% and 33%), far beyond step 4b's tenth;
- 30 pairs, which is beyond section 5's third, in the letter-code kind at weight 0.0;
- 73 pairs in the operator kind at weight 0.6.

So, on this proxy, the closure rule in step 4b would fail. RT-345 would stay open, and the design would return to John after the rented steps had been paid for. RT-370 below gives the cause and a fix that can be made on paper.

### The other findings

- **RT-336, five-candidate scoring: closed, with the condition owed at step 3 (ARGUED).** Sections 5 and 9 report the equal-length rule's drop rates by kind, and the spread of right answers before and after.
- **RT-339, matching on damage: closed (ARGUED),** through the RT-366 fixes below.
- **RT-340, sample size and the pool cap: closed, with conditions (MEASURED).** The simulation must target a clean A after every renaming check, and it now does. My re-run is under RT-363 below. A true normalised gap of 0.20 reaches 80% at about 120 pairs when the comparison loses 0.10, and at about 200 pairs when it loses 0.20. Both sizes are inside what half B can supply (RT-361). The conditions:
  - the committed simulation must use the measured spread and the measured comparison loss;
  - the count after every filter, including the drops that RT-370 predicts, must still reach the simulated size;
  - my simulation assumes the four rule kinds survive in equal numbers. If one is dropped, the simulation must be re-run with three.
- **RT-341, pilot and test overlap: closed (ARGUED).** Answer values are compared within each kind, and test candidates may come only from half B (section 5).
- **RT-346, the donor's answer intruding: closed (ARGUED).** Section 3 reports the first-token overlap.
- **RT-348, the pass-counting coordinates: closed, with a text gap (MEASURED by grep).** The change log says the report covers how much these coordinates vary "by item and position". Section 3, line 161, says only "from item to item" (RT-379).
- **RT-349, what a loss means under five candidates: not closed for plurals (MEASURED).** Version 0.2 answered this finding by building the routine wrong answers to be close, "so that recognition needs the fact". For plurals, version 0.3 makes the wrong answers "real plurals of other nouns from the same pool". The right answer is then the only candidate that begins with the noun asked about (RT-373), so recognising it needs no fact at all. Capitals, opposites and numbers do need the fact.
- **RT-352, a rule written only in the change log: closed (MEASURED by grep).** Section 3, lines 170 to 173, now gives the donor rule for neutral passages. The phrase "similar length" survives only in the first change log, at line 668 (RT-379).
- **RT-358, the donor rule was ambiguous: closed as a rule (MEASURED, proxy).** Section 3 now states one reading: pairs, of the same rule kind, twin to twin. The rule does make the preambles diverge at the same place in both cells. Its effect on dose is not yet enough (RT-370).
- **RT-359, matching dropped single items: closed, with a condition (ARGUED).** Pairs are now dropped whole, within each rule kind, and losing more than a third of a kind returns the design to John. The condition is that the direction of "largest difference" must be stated (RT-375).
- **RT-360, margin matching broke the pairs: closed for the pairing (ARGUED).** Pairs are kept or dropped whole. The concern that matching could leave only routine items with thin margins is now reported, and it is limited by the one-third rule. Whether the margins overlap at all is owed at step 4b (RT-375).
- **RT-361, 300 pairs not available under the cap: closed (MEASURED).**

  ```
  python3 -I pools3.py
  sums half B: answer>50 1176, answer>=50 1223; products half B: answer>40 60 ordered (30 distinct answers)
  cap only, no exclusions: 428 pairs
  cap + v0.3 exclusions: 428 pairs
  routine questions in half B at N=300 under cap: 360
  ```

  The design's arithmetic is right: 75 + 60 + 75 + 75 + 75 = 360 distinct routine questions at a 300-pair cell. Because the cap grows with the cell, the true ceiling is about 428 pairs. So the design's "at most about 360" is conservative, not wrong. The pairing exclusions can be met at full counts (RT-374 gives the edge cases).
- **RT-362, the cap and the prompt-rule cell: closed (ARGUED).** The cap now applies to routine kinds only.
- **RT-363, the leave-one-kind-out rule: closed (MEASURED).** I re-ran outcome A on both methods under the narrower rule: an A is renamed only if a reading with one rule kind left out, and its twins with it, lands in B, C or D. The simulation's assumptions:
  - items start right, and a broken item still picks right one time in five;
  - the swap averages five donors, the average method is a single fixed replacement, and the comparison averages twenty draws;
  - intervals are normal approximations over pairs;
  - each row is 2,000 runs;
  - the true gap of 0.20 is the same in every kind.

  ```
  python3 -I power3.py 2000 equal
  pairs 120, comparison loss 0.10: A on both methods 0.80; clean A after leave-one-kind-out 0.80; renamed 0.00
  pairs 200, comparison loss 0.10: 0.94; 0.94; renamed 0.00
  pairs 300, comparison loss 0.10: 0.99; 0.96; renamed 0.03
  pairs 120, comparison loss 0.20: 0.57; 0.55; renamed 0.02
  pairs 200, comparison loss 0.20: 0.83; 0.83; renamed 0.00
  pairs 300, comparison loss 0.20: 0.94; 0.94; renamed 0.01
  (with a shared item fragility of 0.6: 0.82/0.82, 0.96/0.95, 0.99/0.96, 0.63/0.60, 0.84/0.84, 0.95/0.94)
  ```

  Under the narrower rule, a true equal effect is renamed at most 3% of the time, against the roughly 50% the last check found. 80% is reached at 120 pairs when the comparison's loss is 0.10, and at about 200 pairs when it is 0.20. Both are within the pool. So the rule no longer swallows true effects. Whether it still catches one kind acting alone is RT-371.
- **RT-364, no fallback for the average: closed, with conditions (ARGUED).** One fallback is now named in advance, and John is asked in advance what happens if it also fails (section 10, choice 5). The fallback's definition has gaps (RT-376).
- **RT-365, a routine question behind an irrelevant rule: closed, with conditions (ARGUED).** Each of the four fixes the last check asked for is in the body (sections 1, 5 and 10). The conditions are in RT-374.
- **RT-366, rules missing from the body: closed (MEASURED by grep).**
  - Neutral donors and their five-donor average are in section 3, lines 170 to 173.
  - The noise is spread in proportion to each position's swap distance (section 4's table, line 206).
  - Stage one is restated for one shared factor (line 426).
- **RT-367, the bites check could be passed by generic damage: closed (ARGUED).** The bites check now requires the main removal's loss on chained lookup, minus the random comparison's, to be at least half of what one pass costs, with its interval above zero.
- **RT-368, building the candidates: not closed for the letter code or the lookup table (MEASURED in part).**
  - **Numbers:** answered. The wrong numbers keep the same number of digits, and the drop rates are reported.
  - **Letter code:** decoding now gives a real word and the table is not a shift. But the table reveals the answer's letters (RT-372).
  - **Lookup:** "other colours from the same table" needs at least five distinct colours in every table, and the design does not say so (RT-377).
- **RT-369, donors for the longest items, and the count of runs: closed (ARGUED).** Pairs with fewer than five donors use all the eligible ones, pairs with none are dropped, and both are counted. In the proxy, one lookup pair had no donor and seven had fewer than five. The count is restated at about 330,000 continuations. The same rule is missing for neutral passages (RT-378).

---

## New findings

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-370 | Under the pair donor rule, the routine cell still takes about a fifth more swap in the operator and letter-code kinds, because the routine questions are longer and differ more between donors | serious | MEASURED (proxy) |
| RT-371 | The narrower "depends on one kind" rule lets one kind alone produce outcome A whenever the bites check fails, and some of the time at 120 pairs | serious | MEASURED |
| RT-372 | The letter-code kind can be answered by spotting which candidate is spelled with the letters listed in the table, without decoding | serious | MEASURED |
| RT-373 | Plurals can be answered by copying the noun, so recognition needs no fact; and no check reads the outcome with a routine kind left out | serious | MEASURED |
| RT-374 | The "answered as well behind its rule" check leaves single failing items undecided, and its pairing rules meet the cap at the edge | worth-noting | MEASURED (arithmetic) / ARGUED |
| RT-375 | "Largest difference" has no stated direction, and margin matching may well trip the one-third limit | worth-noting | ARGUED |
| RT-376 | The relative-position fallback leaves the candidates' positions undefined, and the average's damage is measured on the passages it was built from | worth-noting | MEASURED (stand-in) / ARGUED |
| RT-377 | The lookup table must hold at least five distinct colours, which is not stated | worth-noting | ARGUED |
| RT-378 | The neutral passages have no rule for fewer than five donors, or for none | worth-noting | MEASURED (stand-in) |
| RT-379 | One rule the change log claims is not in the body, and the first change log keeps superseded rules unmarked | worth-noting | MEASURED (grep) |

**RT-370, the pair donor rule leaves two rule kinds unmatched (serious, MEASURED with a proxy).** The pair rule makes the preambles diverge at the same place in both cells, as intended. But the dose still differs, because of the question parts that follow the preamble:

```
python3 -I twins3b.py   (run with the src path)
op    twins' shared preamble 32.0 tok; question part P 15.0 R 19.0; R question longer than P in 75/75
unit  twins' shared preamble 21.5 tok; question part P 22.0 R 21.0; R question longer than P in 0/75
code  twins' shared preamble 32.8 tok; question part P 15.0 R 16.7; R question longer than P in 75/75
look  twins' shared preamble 53.9 tok; question part P 17.6 R 18.4; R question longer than P in 36/75
```

There are two causes:
- **Length.** The operator and letter-code rules are only allowed with routine kinds whose questions are longer than the rule's own question. "What is the capital city of X?" is longer than "What is 14 ◇ 17?". Each routine question is longer in all 75 pairs of both kinds. Because the preambles share many tokens with their donors' preambles, these few extra tokens are a large share of what the swap changes.
- **Variety.** A prompt-rule item and its donor share a question template. A routine twin's donor often asks a different routine kind, so more of its tokens differ.

"The twins differ by a few tokens at most" is true of the whole item. It is not true of the changed span, and the changed span is what sets the dose.

I tried one fix. When donor pairs are also required to share the routine kind, the operator and letter-code kinds come within 5%. But the unit kind then goes to 0.87, and the lookup kind loses donors. So no donor rule I tried matches all four kinds.

The fix more likely to work is in the construction: build each pair so that the routine question and the rule question have the same token count. Then set a threshold on the step-3 estimate, which, if crossed, changes the construction before anything is rented. These numbers are a proxy. The real swap sizes could weight the same-token positions differently, and step 4b remains the closure.

**RT-371, the narrower "depends on one kind" rule leaks (serious, MEASURED).** The narrower rule renames an A only when a leave-one-kind-out reading lands in B, C or D. Suppose one kind carries the whole effect. Leaving that kind out then gives no excess loss in either cell, which reads as D, and the A is renamed, as intended. But section 6 reads D only if the main removal passed the bites check. If it did not, the same reading is "too weak to read", which renames nothing. Outcome A itself does not need the bites check.

```
python3 -I power3c.py 1000        and        python3 -I power3.py 2000 onekind
one kind carries all (true gaps [0.80,0,0,0]), A survives the rule:  bites passed 0.00 / 0.00 / 0.00;  bites failed 0.81 / 0.95 / 0.96   (120 / 200 / 300 pairs)
true gaps [0.65, 0.05, 0.05, 0.05]: A survives the rule 0.21 / 0.08 / 0.02
true gaps [0.71, 0.03, 0.03, 0.03]: A survives the rule 0.04 / 0.00 / 0.00
true gaps [0.50, 0.10, 0.10, 0.10]: A survives 0.74 / 0.87 / 0.87  (no single kind carries it; surviving is intended)
```

When the bites check passes, the rule catches one kind acting alone. When the bites check fails, the rule almost never does. In that case an A produced by one rule kind is reported as the prediction holding. At 120 pairs there is a second, smaller leak: if the other kinds carry a small effect (0.05), the reading with the big kind left out often lands in E, and the A survives 21% of the time.

The fix is to read the leave-one-kind-out readings on their P and R intervals alone, so that "no excess loss" counts as definite whatever the bites check gave. Alternatively, an A could be reported as "depends on one kind" whenever any reading with one kind left out fails to be A, while E still does not rename when the bites check passed.

**RT-372, the letter code can be answered without decoding (serious, MEASURED).** Section 5's construction is a table such as "q stands for c, x for a, v for t", which lists exactly the answer's three letters on its right-hand side, with wrong answers that are other real three-letter words.

```
python3 -I code3.py
three-letter lowercase entries in the system word list: 1142; common stand-in pool 60
  answers with at least one anagram in common pool: 0/60
  items where the right answer is the only candidate spelled with the table's letters: 1.000
  answers with at least one anagram in whole word list: 39/60; four or more other words using only the answer's letters: 30/60
  word-list entries outside the common pool: 1083 (sample: fat, bra, lin, eer, wok, try, vet, rub, ife, dar, wha, apt)
```

When the wrong answers come from the same pool of common words, the right answer is the only candidate spelled with the letters the table lists, in every item. A model can pick it by matching letters, without applying the substitution. The "rule is needed" check cannot catch this, because removing the table also removes the cue.

The opposite construction fails too. If the wrong answers come from the whole word list, they can share the answer's letters, but they are mostly rare words ("eer", "ife"), and the frequency of a word is then a cue in its own right.

The fix:
- add rows to the table for letters the coded word does not use;
- spell the wrong answers from the table's plain letters, using common words from the same pool;
- keep the coded string itself out of the candidates;
- list the table rows in a shuffled order, not in the order of the coded word.

**RT-373, the plural candidates need no fact, and no check covers a routine kind (serious, MEASURED).**

```
python3 -I slots3.py ...
plurals: right answer is the only candidate beginning with the asked noun in 1.000 of items
```

With wrong answers that are "real plurals of other nouns from the same pool", the right answer to "What is the plural of 'cat'?" is the only candidate that begins with "cat". The noun can be copied by ordinary attention across words, which this removal does not touch. So the plural kind holds routine losses down for a reason unrelated to practice, which is exactly what RT-349 warned of. That pushes the result toward A, the predicted outcome.

The kind is capped at a quarter of the routine cell. But the "depends on one kind" rule leaves out rule kinds, not routine kinds, so nothing would show whether plurals alone are holding R down.

The fix is either to drop plurals, or to build the wrong answers as other forms of the same noun with the same token count, and to report the outcome with each routine kind left out, at least for description.

**RT-374, the "answered as well behind its rule" check (worth-noting, MEASURED in part).** The check's purpose is sound: at baseline, the rule must not get in the way of the routine question. It has four gaps:
- **Single items.** A routine kind is unpaired from a rule kind if more than a fifth of its items fail. Nothing says whether the failing items within a passing kind are dropped or kept.
- **What it can show.** The check works at baseline only. It cannot show that the removal leaves the ability to ignore the rule intact. Section 1 already states that limit honestly.
- **Where the outcome goes.** The check runs on pilot items at step 4b, so the pairing table it produces must be written into the registration before the test set is generated. The design does not say so.
- **The counts.** Unpairing reaches the edge of the pool.

  ```
  python3 -I pools3.py
  drop (('op','opp'), ('unit','opp')) -> max 300 pairs
  drop (('op','cap'), ('unit','cap')) -> max 320 pairs
  (no single unpairing brings the maximum below 300)
  ```

  Unpairing opposites from both arithmetic rules leaves exactly 300 pairs before any other filter. At the sizes the simulation asks for (120 to 200), there is still room.

Read literally, "spread the routine kinds as evenly as it can" also conflicts with the cap. Capitals are allowed under all four rule kinds, so an even spread at 300 pairs gives 25 + 25 + 25 + 15 = 90 capitals, over both the 75 cap and the 75 countries in half B. The spreading rule should be stated as coming after the cap and the pool sizes.

**RT-375, the direction of the dropping rule, and margin matching (worth-noting, ARGUED).** Both matching steps drop "the pairs with the largest difference between the routine twin's [value] and the prompt-rule item's". If that difference is taken as a size without a sign, the rule can drop pairs that lie on the side opposite to the imbalance. That makes the cells less alike and costs pairs. In my proxy every difference ran the same way, so both readings gave the same drops, but that will not always hold. The rule should say: in the direction of the imbalance.

Separately, routine facts are likely to sit at much larger margins than one-step invented rules. If the gap between the two cells' mean margins is several units, matching them within 0.5 would need far more than a third of each kind's pairs. The design would then return to John at step 4b. The design foresees this ("likely"), but no fallback rule is fixed in advance for this case, as one now is for the average.

**RT-376, the relative-position fallback (worth-noting, MEASURED with a stand-in, and ARGUED).**

```
fallback, candidates outside the text span: neutral bins filled 10/10; shortest neutral text span 29 tokens; candidate positions have no bin defined
fallback, candidates inside the text span: ... candidate positions fall in bin 9
```

Every bin has data, so the fallback can be computed. But three points are undefined:
- **Candidates.** Are the candidates' positions part of "each item's text span"? If they are, they share the last bin with the ends of prose passages. If they are not, they have no average at all.
- **Template slots.** Do the template slots keep their slot averages under the fallback?
- **Bin edges.** How are the bin edges set (for example, position times ten divided by length, rounded down)?

Separately, the factor-of-two rule compares damage on the neutral set. But the average is built from the neutral set, and the text does not say which half builds it and which half measures its damage. Measured on the passages it was built from, the average looks milder than it is.

**RT-377, the lookup table's size (worth-noting, ARGUED).** Four wrong colours "from the same table" need at least five entries with five distinct colours. Section 5 gives no table size. A three- or four-entry table, which the last check's stand-in used, cannot supply the candidates.

**RT-378, donors for the longest neutral passages (worth-noting, MEASURED with a stand-in).** Section 3 gives each neutral passage five donors "of the same half at least as long as it". On the committed pilot set, 5 of the 100 passages in a half have fewer than five such donors. In a new set whose lengths are spread up to the longest item, the very longest passage has none, unless its length is tied. The rule for items (use all the eligible donors, drop when there are none, and count both) is not stated for neutral passages.

**RT-379, text in the change logs that does not match the body (worth-noting, MEASURED by grep).**
- **A missing rule.** The second change log says the report of how much the pass-counting coordinates vary is "by item and position" and "stays in section 3". Section 3, line 161, says only "from item to item". This is the one rule I found that is claimed but not in the body.
- **Superseded rules, unmarked.** The first change log still states rules that version 0.3 has replaced:
  - margin bins 0.5 wide (line 641);
  - neutral donors "of similar length" (line 668);
  - template positions "averaged by template token" (line 613);
  - a factor-of-two difference returning the design to John directly, where a fallback now comes first;
  - "no kind above 25% of a cell", where the cap now covers routine kinds only.

  The body governs, but each of these should be marked as superseded, so that the next reader does not take one for a live rule.

---

## Verdict

Version 0.3 can go to John for his rulings on section 10, with RT-345, the finding that the swap's dose differed between the two task groups, carried as an open fatal item.

- **What closed.** The averaging method (RT-335) now has every position defined, and its template slots are kept apart. The sample-size and pool findings (RT-340, RT-361, RT-363) close on measurement: about 120 to 200 pairs give an 80% chance of a clean A, and half B can supply that.
- **The closure rule for RT-345.** It is the right kind of test: real swap sizes, within each rule kind, read by someone who did not write the fix. It needs five clarifications. It should cover both methods. It should give the base of "a tenth". It should put that limit in section 5. It should say what happens on the test set. It should report which routine kinds the dropped pairs belong to.
- **The forecast.** My proxy predicts that the step-4b check will fail in the operator and letter-code kinds (RT-370), because the routine questions are longer than the rule questions. John should see that forecast beside choice 3, the routine twins, because it bears on whether the twin construction does its job and on whether to spend money on step 4.
- **What must be fixed first.** Nothing found here is fatal, and nothing blocks the section 10 rulings. Four serious findings must be fixed in a version 0.4, before the battery specification is committed at step 3:
  - equal token length for the question parts within each pair, plus a threshold on the step-3 estimate (RT-370);
  - leave-one-kind-out readings that stay definite when the bites check fails (RT-371);
  - a letter-code table with extra rows and wrong answers spelled from its letters (RT-372);
  - plurals dropped or rebuilt, with routine kinds reported one at a time (RT-373).

  The six worth-noting items can be fixed in the same pass.
---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-20. It closes nothing.*

- **RT-379, the pass-counting report.** Confirmed. Section 3 (line 161) says the rehearsal reports how much those coordinates vary "from item to item", while the second change log says "by item and position".
- **RT-373, the plural candidates.** Confirmed as a construction. Section 5 (line 266) makes the wrong answers "real plurals of other nouns from the same pool", so the right answer is the only candidate that begins with the noun asked about.
- **Where things stand.** RT-335, the finding that the averaging method could not be computed, is now closed, with its third condition owed at step 3. RT-345, the finding that the swap's dose differed between the two task groups, stays open. The reviewer's stand-in measurement predicts that the step-4b check would fail in the operator and letter-code kinds (RT-370). The reviewer finds that version 0.3 can go to John for his section 10 rulings with RT-345 carried open. Four serious findings (RT-370 to RT-373) and six worth noting (RT-374 to RT-379) are to be fixed in a version 0.4, before the battery specification is committed.
