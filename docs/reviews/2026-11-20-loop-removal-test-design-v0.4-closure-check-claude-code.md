*Filed 2026-11-20 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the three earlier reviews. It worked read-only in a detached worktree at commit ddc5031 and changed nothing in the repository. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.4

*Reviewer: a fresh Claude Code session. I did not write the design, any of its fixes, or any of the three earlier reviews. I worked read-only in the detached worktree `closure3-loop-design-2026-11-20` at commit ddc5031, and I changed nothing in the repository. My scratch scripts are in my session's scratchpad folder, `/private/tmp/claude-501/-Users-john--claude-spares-spare-d40STS/5395ec4e-ea35-4396-b824-dbb33c4ff595/scratchpad/`, outside git, and none of them writes a file. No model or tokeniser was downloaded, and nothing was spent. New findings continue the red-team numbering from RT-380.*

*One fact about independence: that scratchpad folder already held the scripts of the reviewer of version 0.3 (`twins3.py`, `power3.py`, `pools3.py`, `code3.py` and others). I read them. I reused their stand-in token splitter, stand-in template and simulation skeleton so that my numbers can be compared with theirs. Everything that version 0.4 changes, I wrote new. The design's author wrote none of this code.*

---

**What I opened.**
- **Read in full:**
  - the target, `docs/loop-removal-test-design-2026-11-20.md` (version 0.4, with all three change logs);
  - the closure check of version 0.3, `docs/reviews/2026-11-20-loop-removal-test-design-v0.3-closure-check-claude-code.md`. I read its filer's check as the author's note, not as part of the review.
- **Read in part:**
  - `docs/outside-review-protocol.md`: the tier 1 description and the section "The closure rule, which is the new part";
  - `experiments/09-split-removal-test/src/batteries.py`. I listed its definitions and imported its pools (countries, opposites, invented syllables, operator symbols) into my scripts;
  - the list of files changed between commits 8bd34cd and ddc5031 (`git diff --stat`). I did not read the line-by-line diff, because I read version 0.4 and its third change log in full.
- **Ran** the following scripts, each reported under the item it bears on:
  - `twins4.py`, with three helpers (`twins4b.py`, `twins4c.py`, and inline variants). It builds twin pairs under version 0.4's construction and applies the version 0.4 donor rule. It measures the changed span and the proxy swap size in each rule kind against the new step-3 threshold;
  - `power4.py`, a sample-size simulation under version 0.4's "depends on one kind" rule;
  - `pools4.py`, which does the pool arithmetic with plurals replaced by everyday colours;
  - `code4.py` and `code4b.py`, which test whether letter-code items can be built and whether they leave cues;
  - inline checks of the number candidates against the copying rule, and a toy test of the margin fallback.
- **Searched the target** (grep) for rules left over from earlier versions and for rules stated only in a change log.

**What I did not open.** I did not open:
- the inside review of version 0.1 or the closure check of version 0.2;
- the three-hypotheses proposal or the design note;
- the committed pilot battery files;
- the external pages (the model card, the Hugging Face page and Goodfire's write-up). Version 0.4 adds no new claim from them.

The model's tokeniser and chat template are not in the repository. **So every token count below comes from a stand-in splitter, and every "swap size" below is a proxy, not a measurement on the model.** I repeat this wherever it matters.

**The stand-ins.**
- **Splitter.** Common words, numbers, countries, colours, everyday objects and three-letter words count as one token each. Any other word is cut every three letters, which stands in for invented words breaking into several tokens.
- **Template.** 12 tokens go before the user text. After it come 4 tokens, then 4 more for an empty block that suppresses written reasoning.
- **Pools.** They are enlarged to version 0.4's minimums (150 countries, 160 adjectives, 150 everyday objects). Single-token placeholders fill the places beyond the real lists.
- **Phrasings.** Each kind has five or six phrasings, including the three capital phrasings section 5 gives as examples. A second, extended set adds one or two longer phrasings for each routine kind, and one shorter phrasing for the unit kind. I added those to give the construction a fair chance.
- **Choosing a phrasing.** Two readings of "picks the phrasings that give the same token count", because the text does not say which matching combination is used. In the first, one matching combination is chosen at random. In the second, the most usual phrasings are preferred.
- **Size.** 75 pairs for each rule kind, 300 in all, from half B. I also built 120 and 200 pairs for the donor counts.

---

## Verdicts

| Item | Verdict | Label |
|---|---|---|
| RT-345 (fatal), the swap's dose differed between the two task groups | **Not closed, and it cannot be closed on paper.** The proxy predicts that the new step-3 threshold will trip in the operator and unit kinds, this time with the routine cell taking *less* swap (RT-380) | MEASURED (proxy) |
| RT-345 clarification 1: both methods covered | Closed | MEASURED (grep) |
| RT-345 clarification 2: the base of "a tenth" | Closed | MEASURED (grep) |
| RT-345 clarification 3: the tenth stated in sections 5 and 6 | Closed | MEASURED (grep) |
| RT-345 clarification 4: the rule applied to the test pairs | Closed | MEASURED (grep) |
| RT-345 clarification 5: routine-kind mix reported, and a threshold at step 3 | Closed, with conditions (RT-387, RT-389) | MEASURED (grep and proxy) |
| RT-370, the routine cell took more swap in two rule kinds | **Not closed.** The length half is closed: the changed spans are now equal. The dose half is not (RT-380, RT-381) | MEASURED (proxy) |
| RT-371, the "depends on one kind" rule leaked when the bites check failed | **Closed** | MEASURED |
| RT-372, the letter code could be answered by spotting letters | Closed, with conditions | MEASURED |
| RT-373, plurals could be answered by copying the noun | Closed, with conditions (RT-385) | MEASURED in part |
| RT-374, the "answered as well behind its rule" check | Closed | MEASURED (grep and arithmetic) |
| RT-375, the direction of dropping, and margin matching | Closed for the direction. **Not closed for the fallback** (RT-386) | MEASURED (toy) |
| RT-376, the relative-position fallback | Closed | ARGUED |
| RT-377, the lookup table's size | Closed for size. It now conflicts with the overlap check (RT-383) | ARGUED |
| RT-378, donors for the longest neutral passages | Closed | MEASURED (grep) |
| RT-379, change logs out of step with the body | Closed, with a condition (RT-389) | MEASURED (grep) |

### RT-345, the swap's dose differed between the two task groups

**Not closed. It cannot be closed on paper, and the proxy forecasts a failure (MEASURED, proxy).**

*The five clarifications (MEASURED by grep).* Each one the last check asked for is now in the body:
1. **Both methods.** Section 5 (lines 421 to 425) matches swap size "for each method", and defines the average method's changed span as every position that is not a template slot. Step 4b (line 648) says "under both methods".
2. **The base of the tenth.** It is counted from the pairs left just before swap-size matching, after the confidence check, margin matching and donor eligibility (lines 429 to 430).
3. **Where the tenth is stated.** Section 5 now gives the tenth as the limit (line 428). Section 6's first stage says the same (lines 500 to 501), and the third stays only on margin matching.
4. **The test pairs.** The same rule applies to them unchanged, and exceeding it makes the result not testable (lines 433 to 434).
5. **Reporting and the threshold.** The routine-kind mix of the dropped pairs is reported (lines 435 to 436 and 650). The step-3 estimate now has a threshold that forces the construction to be revised before anything is rented (lines 630 to 634).

*Is the closure rule still the right test?* Yes. The real per-item swap sizes, read from the model's block sums at step 4b, within each rule kind and under both methods, are still the one measurement that would come out wrong if the fix were wrong. Nothing on paper can take their place.

*Are the step-3 threshold and the step-4b rule consistent with each other and with section 5?* Mostly yes:
- **The thresholds fit together.** The step-3 band at weight 0.3 (0.95 to 1.05) is tighter than step 4b's 10%. That is the right order, because the proxy is cruder than the real measurement.
- **The tenth can only make small corrections.** I measured how far dropping a tenth of a kind's pairs, in the direction of the imbalance, moves the proxy ratio. It moves it by 0.5 to 2.5 points:

  ```
  python3 -I -c "...drop a tenth in the direction of the imbalance..."   (twins4 rows, random phrasing choice, extended phrasings)
  pairs per rule kind 30, weight 0.3: op 0.938->0.949 (drop 3 of 30); unit 0.838->0.848 (drop 2 of 20); code 1.012->1.008; look 0.994->1.000
  pairs per rule kind 75, weight 0.3: op 0.955->0.965 (drop 7 of 75); unit 0.859->0.870 (drop 5 of 50); code 1.017->1.012; look 0.996->1.000
  pairs per rule kind 75, weight 0.0: op 0.898->0.920; unit 0.757->0.778; code 1.040->1.028; look 0.994->0.999
  ```

  So in practice step 4b asks the construction to come in within about 10%, or a point or two beyond it, before anything is dropped. Matching can only tidy what remains. This is strict, but it is consistent: the construction carries the burden, and step 3 checks the construction. I do not think the tenth by itself makes registration rare, *if* the construction passes step 3. RT-380 shows that, as written, it does not.
- **The gaps.** Step 3 has an estimate for the swap only, not for the average method (RT-387). "Within 10%" is not defined as a ratio, while step 3 is (RT-389). The pilot's size is never stated, and every one of these limits is applied to pilot pairs (RT-389).

*The paper measurement.* This is reported under RT-370 directly below. In short, the proxy dose now runs the other way, and in the unit kind it is outside both the step-3 band and step 4b's 10% under every weight I tried except 0.6.

### RT-370, the routine cell took more swap in two rule kinds

**Not closed (MEASURED, proxy).** I applied version 0.4's construction as written:
- the two question parts of each pair have equal token counts, chosen from several phrasings per kind;
- donor pairs share the rule kind and the routine kind;
- each twin of a donor pair is at least as long as the matching recipient's prompt plus its candidate;
- no donor's right answer is a recipient's candidate;
- five donors are averaged;
- everyday colours replace plurals, and the pairing exclusions hold.

The proxy swap size counts 1 for each changed position whose token differs from the donor's token at the same place. It counts a smaller weight (0, 0.3 or 0.6) for each changed position whose token is the same. **This is a proxy.**

```
python3 -I twins4.py <src> random one ext        (one matching phrasing combination chosen at random)
weight 0.3, band 0.95-1.05:
  op    span P 33.6 R 33.6 | proxy P 17.95 R 17.14 ratio 0.955 inside  | drops to 10%: 0
  unit  span P 35.4 R 35.4 | proxy P 25.42 R 21.83 ratio 0.859 OUTSIDE | drops to 10%: 17 of 50
  code  span P 61.9 R 61.9 | proxy P 31.89 R 32.43 ratio 1.017 inside  | drops to 10%: 0
  look  span P 62.9 R 62.9 | proxy P 55.44 R 55.21 ratio 0.996 inside  | drops to 10%: 0
  seeds 2, 3: op 0.935* 0.928*; unit 0.845* 0.849*; code 1.015 1.014; look 0.998 0.992      (* = outside the band)
weight 0.0, band 0.90-1.10: op 0.898* 0.858* 0.834*; unit 0.757* 0.727* 0.737*; code 1.040 1.037 1.034; look 0.994 0.997 0.988
weight 0.6, band 0.90-1.10: op 0.981 0.971 0.969; unit 0.931 0.925 0.927; code 1.007 1.006 1.006; look 0.998 0.999 0.996

python3 -I twins4.py <src> first one ext          (the usual phrasings preferred)
weight 0.3: op 0.922*, unit 0.877* to 0.892*, code 1.010, look 0.995 to 0.996
weight 0.0: op 0.741* (matching to 10% would drop 74 of 75), unit 0.765* to 0.801*;   weight 0.6: op 0.970, unit 0.943 to 0.950
```

The results:
- **The length half is closed.** The changed spans of the two cells are now equal in every kind (33.6 and 33.6, 35.4 and 35.4, and so on). That was the cause the last check found.
- **The dose half is not closed.** In the operator and unit kinds, the routine cell now takes *less* proxy swap than the prompt-rule cell. That is the opposite direction from version 0.3.
  - **Unit kind:** outside the step-3 band at weights 0.3 and 0.0 in every seed and under both ways of choosing phrasings. At weight 0.3, matching to 10% would need 13 to 17 of its 50 pairs, far beyond a tenth.
  - **Operator kind:** outside the band at weight 0.3 in two of three seeds with random choice, and in all three when the usual phrasings are preferred.
  - **Letter-code and lookup kinds:** inside every band.
- **What the step-3 threshold would do.** It would trip, which is what it was put there to do. The construction would then go back for revision before any money is spent. The threshold therefore works as a safeguard. The fix it guards does not yet work. RT-380 gives the cause.

*How many pairs the construction costs, by kind (MEASURED, proxy).*
- **The equal-length rule** costs nothing in the operator, letter-code and lookup kinds. In the unit kind it is the main cost (RT-381). With the design's example phrasings, no unit item could be matched with a capitals question or an everyday-colours question in 1,500 attempts each, so only 25 of 75 unit pairs could be built. With my extended phrasings, capitals become possible, but everyday colours still never match, so 50 of 75 were built.
- **Donor eligibility** costs the most in the lookup kind:

  ```
  python3 -I twins4c.py   (same rule kind and routine kind, at least as long, donor answer not a candidate)
  120 pairs: look no donor 3 to 5 of 30, fewer than five 17 to 20; op fewer than five 6 to 13; unit fewer than five 2 to 10; code no donor 1
  200 pairs: look no donor 3 to 4 of 50, fewer than five 16 to 21
  300 pairs: look no donor 2 to 5 of 75, fewer than five 13 to 18; code fewer than five 2 to 4
  ```

  Requiring the same routine kind splits each rule kind into three or four groups. At the 120 pairs the sample size needs, a group has 7 to 10 pairs. The longest pair in a group, which here means the largest lookup tables, then often has no donor at all (RT-388).

### The other findings

- **RT-371, the "depends on one kind" rule leaked when the bites check failed: closed (MEASURED).** The bites check is the check that the removal actually hurts the one task known to need the loop. Section 6 (lines 532 to 536) now reads the left-out readings on their R and P intervals alone. My simulation does the same, and adds the case where the main reading failed the bites check:

  ```
  python3 -I power4.py 1000 onerule
  one rule kind carries the whole effect (gaps [0.80, 0, 0, 0]):
    bites passed: A survives 0.000 / 0.000 / 0.000   (120 / 200 / 300 pairs)
    bites FAILED: A survives 0.001 / 0.000 / 0.000
  gaps [0.65, 0.05, 0.05, 0.05]: bites passed 0.204 / 0.088 / 0.022; bites failed 0.220 / 0.088 / 0.017
  ```

  Last time, 81% to 96% of these A results survived when the bites check failed. Now almost none do, and the result no longer depends on the bites check. That matches the closure claim. A smaller leak remains: at 120 pairs, when the other kinds carry a small effect, about a fifth of A results survive, because the left-out reading lands in E, and by rule E does not rename. That leak is a deliberate trade made in version 0.3, and it shrinks to 2% at 300 pairs. It belongs in the report beside any A at the smaller sizes.

- **RT-372, the letter code could be answered by spotting letters: closed, with conditions (MEASURED).**

  ```
  python3 -I code4.py      (stand-in pool of 168 common three-letter words, 84 in half B)
  random extra letters, half-B pool: items buildable 0.36; right answer the only candidate with no letter in the coded string's place 0.00;
     the only candidate sharing fewest letters with the coded string 0.02; a wrong answer has a repeated letter 0.31; fewest cipher letters 0.05
  chosen extra letters, half-B pool: items buildable 0.98; same cues 0.00 / 0.03; repeated letter 0.20; 0.06
  python3 -I code4b.py
  random: right answer has the most letter overlap with the other candidates 0.37 with ties, 0.08 alone;  chosen: 0.21, 0.04   (chance 0.20)
  ```

  The old cue is gone. Every candidate is now spelled from the table's letters, and none of the shortcuts I tried picks the right answer more often than chance. The conditions:
  - **Say how the five extra letters are chosen.** Drawn at random, only 36% of items can be built from a half-B pool of this size, and a weak cue remains (the right answer is the most central candidate 37% of the time, with ties). Chosen so that the wrong words fit, 98% of items can be built and I found no cue.
  - **Make every wrong answer use three different letters, as the right answer must.** In a fifth to a third of items, a wrong answer such as "egg" or "too" can be ruled out without decoding, because the right answer never repeats a letter.

- **RT-373, plurals could be answered by copying the noun: closed, with conditions (MEASURED in part).**
  - **What is fixed.** Plurals are gone. Routine kinds are now left out in turn as well. I simulated one routine kind that the removal cannot touch, while the other routine kinds lose 0.08:

    ```
    python3 -I power4.py 500 oneroutine
    R loss 0.08 except capitals immune: A on both 0.068 / 0.146 / 0.244; A survives 0.022 / 0.038 / 0.034
    R loss 0.08 except sums immune:     A on both 0.122 / 0.224 / 0.358; A survives 0.038 / 0.050 / 0.036
    (the same with the bites check failed: survives 0.018 / 0.044 / 0.040 and 0.026 / 0.048 / 0.036)
    ```

    Leaving out routine kinds catches about seven in eight of the A results that one immune routine kind produces.
  - **What is not fixed.** The new copying rule needs tighter wording (RT-385).

- **RT-374, the "answered as well behind its rule" check: closed (MEASURED).** In the body:
  - failing pairs within a passing kind are dropped whole (line 403);
  - the pairing table is fixed on the pilot items and written into the registration (lines 404 to 405);
  - the even spread comes after the cap and the pool sizes (lines 371 to 372).

  The pool arithmetic is under item 4 below.

- **RT-375, the direction of dropping, and margin matching: closed for the direction, not closed for the fallback (MEASURED with a toy model).** Both matching steps now drop pairs "in the direction of the imbalance" (lines 414 and 422). The new margin fallback, though, removes more pairs than ordinary matching in every case I tried, so it cannot rescue a kind that ordinary matching fails (RT-386).

- **RT-376, the relative-position fallback: closed (ARGUED).** Lines 163 to 168 define three things:
  - the text span, with the candidates included;
  - the bin, which is ten times the position divided by the span's length, rounded down, giving bins 0 to 9;
  - the template slots, which keep their slot averages.

  Lines 156 to 158 and 471 to 472 split the half in use into 100 passages that build the average and 100 that measure its damage.

- **RT-377, the lookup table's size: closed for size (ARGUED).** Each table has five to seven entries with distinct colours (line 290). That now collides with the overlap check (RT-383).

- **RT-378, donors for the longest neutral passages: closed (MEASURED by grep).** Lines 192 to 194 apply the items' rule to neutral passages: use all eligible donors, leave out a passage with none, and count both.

- **RT-379, change logs out of step with the body: closed, with a condition (MEASURED by grep).** Line 180 now reports the variation of the pass-counting coordinates "from item to item and from position to position". Both earlier change logs open with a note listing the rules later replaced. The notes miss several replaced rules (RT-389).

---

## Sample size under version 0.4's rule (item 3)

**80% for a clean A is reachable within the pool, at about the sizes the last check found (MEASURED).** I used the same simulation as the last check, with version 0.4's rule:
- the outcome is also read with each of the four rule kinds and each of the five routine kinds left out in turn;
- each of those nine readings is judged on its R and P intervals alone, so "no excess loss" counts as D;
- a reading in B, C or D renames the A, and a reading in E does not;
- there are two methods, so 18 readings in all.

Pairs are assigned to (rule kind, routine kind) under the 25% cap and the pairing exclusions. Items start right, a broken item still picks right one time in five, and intervals are normal approximations over pairs. Each row is 1,000 runs, so each figure is good to about ±0.013.

```
python3 -I power4.py 1000 equal          (true gap 0.20 in every kind)
pairs 120, comparison loss 0.10: A on both 0.810; clean A 0.806; renamed 0.004   (fragility 0.6: 0.809 / 0.804)
pairs 200, comparison loss 0.10: 0.944; 0.936; renamed 0.008                     (0.952 / 0.939)
pairs 300, comparison loss 0.10: 0.995; 0.962; renamed 0.033                     (0.990 / 0.943)
pairs 120, comparison loss 0.20: 0.575; 0.541; renamed 0.034                     (0.608 / 0.579)
pairs 200, comparison loss 0.20: 0.820; 0.818; renamed 0.002                     (0.838 / 0.835)
pairs 300, comparison loss 0.20: 0.927; 0.915; renamed 0.012                     (0.950 / 0.925)
```

- **Where 80% is reached.** At about 120 pairs when the random comparison loses 0.10, and at about 200 pairs when it loses 0.20. Adding the five routine-kind readings renames a true equal effect 0.2% to 4.7% of the time. That share grows with size, because more readings can land in C by chance.
- **The pool.** Half B supplies about 360 to 384 pairs (item 4), so both sizes fit.
- **The margin is thin.** At 120 pairs, the figure sits exactly at 80%. The pairs that the unit kind and the lookup kind lose (RT-381, RT-388) come out of the same count. As the design says, the committed simulation must use the measured spread and comparison loss, and it must be run on the pairs that survive the filters.
- **RT-371's leak** is closed, as shown above.

## Pools, pairing exclusions, the letter code and the copying rule (item 4)

```
python3 -I pools4.py
half-B pools: sum 1176, prod 60 (30 distinct answers), cap 75, opp 80, col 75
routine questions available at 300 pairs under the cap: 360;  max pairs, cap + v0.4 exclusions: 384
unpair (unit, col) -> 384;  (unit, col) + (unit, cap) -> 320;  (op, opp) + (unit, opp) -> 300;  (op, col) + (unit, col) -> 300
everyday colours in half B = 60 / 50 / 40: max pairs 364 / 352 / 340
```

- **The arithmetic is right.** The 25% cap allows 75 questions per routine kind at 300 pairs. Opposites are capped at 75 of their 80, so the design's "about 360" is exact. Because the cap grows with the cell, the true ceiling is about 384 pairs.
- **The pairing exclusions can be met.** A feasible table at 300 pairs:
  - the letter-code and lookup kinds take all the sums and products, plus a few capitals, everyday colours and opposites;
  - the operator and unit kinds share capitals, opposites and everyday colours.
- **What that table means.** Two of the four rule kinds then have almost entirely arithmetic routine twins, and the other two have none. So leaving out a rule kind and leaving out a routine kind overlap heavily. That is worth saying in the report, but it breaks nothing.
- **Unpairings the RT-374 check might force.** Losing everyday colours under the unit kind, which the equal-length rule already forces in the proxy (RT-381), costs no ceiling. Any two unpairings that strike one routine kind from both arithmetic rules leave exactly 300 pairs. That is still above the 120 to 200 the simulation needs.
- **The letter code** can be built, and is free of cues, if the extra letters are chosen to fit the wrong words (RT-372 above).
- **The copying rule** breaks no routine kind outright. Its wording, though, catches too much in one place and too little in two others (RT-385).
- **The colour kinds** collide with the overlap check (RT-383), and their object pool is strained (RT-384).

---

## New findings

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-380 | Equal token counts equalise the changed span but not the dose. Rule questions carry item-specific tokens, so the routine cell now takes less proxy swap in the operator and unit kinds | serious | MEASURED (proxy) |
| RT-381 | The unit kind cannot be length-matched with everyday colours, or with capitals using the design's example phrasings. A third to two thirds of its pairs cannot be built | serious | MEASURED (proxy) |
| RT-382 | Choosing phrasings to equalise length gives the two cells different phrasings. No rule says which matching phrasing is chosen, and the choice changes the result | serious | MEASURED (proxy) |
| RT-383 | The overlap check forbids an answer value in both halves of a kind. That cannot be met by lookup tables of up to seven distinct colours, and only barely by everyday colours | serious | ARGUED |
| RT-384 | Everyday colours: 150 objects with one unambiguous typical colour is a strained pool, and no rule keeps out wrong colours the object often has | worth-noting | ARGUED |
| RT-385 | The copying rule's "begins with" misses opposites built with a prefix. Read digit by digit, it would drop half the products | worth-noting | MEASURED |
| RT-386 | The margin fallback removes more pairs than plain matching, so it never rescues a kind. Nothing says what happens on the test pairs | worth-noting | MEASURED (toy) |
| RT-387 | The step-3 estimate covers the swap only. The average method's dose is likely larger in the prompt-rule cell, and nothing free catches it | worth-noting | ARGUED, with a token count |
| RT-388 | Requiring donors of the same routine kind leaves the largest lookup tables without donors, which at 120 pairs is 10% to 17% of the lookup kind | worth-noting | MEASURED (proxy) |
| RT-389 | Text gaps: the pilot size is never stated, "within 10%" is not defined, two sentences in the body are stale, and the change-log notes are incomplete | worth-noting | MEASURED (grep) |

**RT-380, equal length does not give equal dose (serious, MEASURED with a proxy).** Within the question parts, I counted the share of positions whose token matches the donor's at the same place:

```
python3 -I twins4b.py   (random choice, extended phrasings)
op    same-token share within the question part P 0.35 R 0.56
unit  P 0.19 R 0.70
code  P 0.61 R 0.49
look  P 0.07 R 0.10
variant, donors must also use the same two phrasings: weight 0.3 op 0.922, unit 0.891, code 1.009, look 0.998 (look: 24 pairs with no donor)
```

- **Why the dose differs.** A routine question is a fixed template with one changing word, such as "What is the capital city of X?". Its donor asks the same routine kind, so most of its tokens match. A rule question carries several item-specific tokens: two operands and a symbol, or two invented unit names that each break into several tokens. Its donor shares fewer of them.
- **Why the spans match but the dose does not.** Equal token counts make the changed spans equal. They do not make equal the number of tokens that actually differ from the donor's. The real swap distance at a same-token position is unknown, which is why the weight is varied. But a smaller distance at positions where the token is the same is the likely case, so the direction is probably real.
- **A fix I tried.** Requiring donors to share both phrasings does not help.
- **Fixes worth trying, all on paper.**
  - Match each pair on the number of item-specific tokens in its question part, not only on the total length.
  - Or give the routine questions a second changing slot. For example, "What is the capital of X, the country next to Y?".
  - Or make the rule questions repeat content already in the preamble, which the donor's preamble also replaces.
- **The safeguard works.** The step-3 threshold would catch all of this before money is spent, as it is meant to. But the design should not go to step 3 expecting the present construction to pass.

**RT-381, the unit kind cannot be length-matched (serious, MEASURED with a proxy).**

```
python3 -I twins4.py <src> random one base    unit: equal-length failures, capitals 1500 of 1500 attempts, everyday colours 1500 of 1500; pairs built 25 of 75
python3 -I twins4.py <src> random one ext     unit: capitals 0 of 25, everyday colours 1500 of 1500; pairs built 50 of 75
```

A unit question names two invented words, one of them twice, and in the stand-in each invented word is two or three tokens long. So unit questions run 10 to 14 tokens, against 4 to 8 for capitals and everyday colours with the example phrasings. The pairing exclusions allow the unit kind only capitals, opposites and everyday colours. In the proxy, it is therefore left mostly with opposites, plus capitals once long capital phrasings are written for it. Its count falls a third or two thirds short.

The real tokeniser may split invented words differently, so step 3 decides. The battery specification should still fix two things before any item exists: phrasing sets that reach the unit kind's lengths, and the rule for a rule kind that cannot be filled.

**RT-382, phrasing becomes a difference between the cells (serious, MEASURED with a proxy).** Section 5 says the generator "picks the phrasings that give the two question parts the same token count". It does not say which combination is used when several match. The proxy shows that the choice matters, and that either way the cells end up phrased differently:

```
random choice:    op P usual phrasing 28/75, R 6/75;  code P 12/75, R 0/75;  look P 12/75, R 7/75
usual preferred:  op P 75/75, R 25/75;  code P 38/75, R 0/75;  look P 40/75, R 19/75
operator kind, weight 0.3, seed 1: ratio 0.955 (random choice) against 0.922 (usual phrasings preferred)
donor shares the recipient's phrasing (random choice): op P 0.42 R 0.54; unit P 0.22 R 1.00; code P 0.67 R 0.59; look P 0.38 R 0.50
```

The consequences:
- **The routine cell gets the odd phrasings.** It is far more often given a terse or unusual phrasing ("X's capital is?", "Opposite of x?") to fit a short rule question. That difference sits between the cells, so it can move margins and perhaps sensitivity to the removal, and it would show up in G.
- **No check catches it.** The "answered as well behind its rule" check compares a routine question with the same question without a preamble, so the phrasing is held fixed and the check cannot see this.
- **A sentence in section 3 is no longer true.** Section 3, line 130, says each routine twin's donor "shares its question template, just as each prompt-rule item's donor does". Under random choice that holds for only 22% to 67% of donor draws.
- **The fix.**
  - Fix the tie-break rule in the specification.
  - Report the phrasing mix of each cell.
  - Either draw both cells' phrasings from the same range of unusualness, or use a single phrasing for each pairing of rule kind and routine kind and vary the length some other way.

**RT-383, colours cannot be split into two halves as the overlap check demands (serious, ARGUED).** Section 5 (lines 388 to 390) says the check script fails "if any answer value of one kind appears in both halves of that same kind". Test candidates must come from half B's pools (line 297). Two kinds collide with this:
- **The lookup kind.** Its answers are colours. A table of seven entries with distinct colours (line 290) needs seven colours in half B and seven others in half A: fourteen common colour names of equal token length. Only about eleven basic colour names exist.
- **Everyday colours.** Each half needs at least five colours to supply four wrong answers. Splitting the eleven basic colours five and six leaves the rarer colours (blue, purple, pink) in one half, which then has few objects to draw on.

As written, the committed check would fail, or the generator could not satisfy it. The fix is a ruling in the text. One option is to exempt closed sets of answer labels from the answer-value check and keep the check on prompts and objects. The other is to name a set of at least fourteen colours for the lookup kind.

**RT-384, everyday colours as practised knowledge (worth-noting, ARGUED).** The kind is the right idea. A typical object colour is common, practised knowledge, and the colour word can be kept out of the question. Three things need stating:
- **The pool is strained.** Writing the list out, I could find about 120 objects with one typical colour whose name contains no colour word (banana, coal, snow, flamingo, aubergine, and so on). That is before removing the doubtful ones: an egg can be white or brown, a grape green or purple, a squirrel grey or red, and a fire engine is red in some countries and yellow in others.
- **The answers are lopsided.** Green, white, red and brown make up most of the list.
- **Wrong answers can be right.** Section 5 builds wrong answers from "other common colours". No rule keeps out a colour the object often has, so a green apple could be marked wrong.

The battery specification should do three things: list the objects, keep out any wrong colour that is commonly true of the object, and report the spread of right answers.

**RT-385, the wording of the copying rule (worth-noting, MEASURED).** "No candidate may repeat a word of the question, or begin with one" (line 293) has three problems:
- **It misses prefix opposites.** It does not catch "unhappy" for "happy", or "impossible" for "possible". Those contain the word asked about without beginning with it, and they are the copy cue that RT-373 named. It also misses a capital whose name is the start of the country's name, such as "Tunis" for "Tunisia".
- **A digit-by-digit reading would gut the products.**

  ```
  python3 -I -c "..."   products in half B: 60; right answer's digits begin with an operand's: 29 (4x12=48, 5x11=55, ...); sums: 8 of 1176
  ```

  Read on the characters or on digit tokens, the rule drops 29 of the 60 products in half B. Products then supply 31 questions instead of 60.
- **The scope is unclear.** The rule does not say whether "the question" includes the rule preamble. The letter-code preamble is full of single letters, and the operator preamble contains "a" and "b".

The rule should say four things. It applies to the question part only. It works on tokens. It bars a candidate that contains a word of the question, or is contained in one. It does not apply to numbers, whose wrong answers already share their leading digits.

**RT-386, the margin fallback never rescues (worth-noting, MEASURED with a toy model).** The margin is how far the right candidate's score beats the best wrong one. The fallback keeps only pairs whose two margins both lie between 2.2 and the 90th percentile of the prompt-rule margins in that kind, and then matches as before. I drew margins from four plausible pairs of distributions, 75 pairs a kind, 50 trials each:

```
P ~N(4,1),   R ~N(5,1.5): plain matching removes 0.17; fallback removes 0.49
P ~N(4,1),   R ~N(6,2):   0.48; 0.70
P ~N(4,1.5), R ~N(8,2):   0.78; 0.89
P ~N(5,2),   R ~N(6,2):   0.06; 0.29
```

- **Why it fails.** The band throws out at least a tenth of the prompt-rule items by construction. It also throws out every routine twin whose margin is above that 90th percentile, which is exactly the case where routine facts sit higher. So the fallback removes more pairs than plain matching in every case, and it only ever leads back to John.
- **What is unclear.** Whether "that also removes more than a third" counts the band and the matching together is not stated.
- **What is missing.** Nothing says what happens if the test pairs need more than a third, though the tenth now has such a rule.
- **The fix.** Either a band defined on both cells (for example, the overlap between the 10th and 90th percentiles of the two cells' margins), or no fallback and a plain statement that this case returns to John.

**RT-387, step 3 sees the swap only (worth-noting, ARGUED, with a token count).** The free step-3 estimate and its threshold model only the swap. Under the average method, the dose is the distance between each position's true block sums and the neutral average, over the whole text span. That distance is probably larger for invented words and symbols than for common words. In the proxy, the share of question-part tokens that are pieces of invented words or symbols is:
- operator kind: 0.16 in the prompt-rule cell, 0.01 in the routine cell;
- unit kind: 0.55 and 0.00;
- letter-code kind: 0.17 and 0.00;
- lookup kind: 0.32 and 0.00.

Equal length does not touch this. Step 4b measures it, and the closure rule now covers both methods. But an imbalance under the average method would first appear after money has been spent. A word-rarity proxy at step 3 would cost nothing.

**RT-388, donors of the same routine kind (worth-noting, MEASURED with a proxy).** Within a rule kind, each routine kind has 7 to 25 pairs. The donor must be at least as long as the recipient, so the longest pair in each group often has no donor. In the lookup kind, those are the seven-entry tables: 3 to 5 of 30 pairs at 120 pairs in all, and 2 to 5 of 75 at 300. Most other pairs have fewer than five donors. The drops come before the tenth is counted, so they do not threaten the RT-345 limit. But they always remove the longest tables, which changes the mix of the lookup kind. The report should give their count by table size.

**RT-389, text gaps (worth-noting, MEASURED by grep).**
- **The pilot size is never stated.** Step 4b's tenth, the fifth-of-a-kind rule in the "answered as well" check, and the margin third are all applied to pilot pairs. Their noise depends on how many pilot pairs there are.
- **"Within 10%" is not defined** (lines 422, 500 and 648). It could mean a routine-to-prompt-rule ratio between 0.90 and 1.10, as step 3 defines its own band, or the larger over the smaller at most 1.10.
- **Two sentences in the body are stale.** Line 130, the donor sharing "its question template", is wrong under the phrasing rule (RT-382). Line 309, "differ in length by a few tokens at most", is now true only of the candidates.
- **The change-log notes are incomplete.** The first change log's note omits rules that have since been replaced:
  - "donors are drawn from the same kind and cell";
  - "a reading with one kind left out that differs from the full reading renames the outcome";
  - the bites check's "at least half of what one pass costs", which now has the random comparison subtracted (RT-367).

  The second change log's note omits two:
  - donor pairs "of the same rule kind", which now also share the routine kind;
  - the leave-one-kind-out rule of RT-363, which now covers routine kinds and ignores the bites check.

---

## Verdict

Version 0.4 can go to John for his rulings on section 10, with RT-345 (the finding that the swap's dose differed between the two task groups) carried as an open fatal item.
- **What closed.** RT-371 is closed on measurement: an A produced by one kind alone no longer survives, whether or not the bites check passed. 80% for a clean A is still reached at about 120 pairs when the random comparison loses 0.10, and at about 200 pairs when it loses 0.20, within a pool of about 360 to 384 pairs. The letter code and the plurals findings close with conditions. All five clarifications of RT-345's closure rule are in the body.
- **What John should see beside choice 3, the routine twins.** RT-370 is not closed. Equal-length question parts made the changed spans equal. But on the proxy, the routine cell now takes *less* swap in the operator and unit kinds, because rule questions carry more item-specific tokens (RT-380). The new step-3 threshold would therefore trip before any money is spent, which is the safeguard working, not the fix. The construction also cannot fill the unit kind (RT-381). It puts different phrasings in the two cells (RT-382). And its colour kinds cannot meet the overlap check as written (RT-383).
- **Before the rulings.** Nothing found here is fatal, and none of it blocks the section 10 rulings.
- **Before step 3.** Those four serious findings must be fixed in a version 0.5, before the battery specification is committed at step 3. The six worth-noting items can be fixed in the same pass.
---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-20. It closes nothing.*

- **RT-382, the stale sentence in section 3.** Confirmed. Line 130 says each routine twin's donor "shares its question template, just as each prompt-rule item's donor does", which the phrasing rule no longer guarantees.
- **RT-385, the copying rule.** Confirmed as worded. Line 293 bars a candidate that repeats "a word of the question, or begin[s] with one", which misses opposites built with a prefix.
- **A limit on independence that the reviewer partly disclosed, and that the author must state in full.** All four reviewers of this design ran as subagents of the author's session, and they shared one scratchpad folder with it. The reviewer of version 0.4 says it found and reused the scripts of the reviewer of version 0.3. That folder also held files the author wrote: copies of the earlier reviews pulled out for filing, and the request and reply bodies used to update the day's TimeAssembler reflection. Those bodies summarise each version's fixes in the author's own words. No reviewer was told about those files, and none reports reading them. But nothing stopped a reviewer from reading them. The design itself and its change logs say the same things, so the exposure is to the author's framing rather than to hidden information. From the next check onward, each reviewer gets its own empty scratch folder.
- **Where things stand.** Every one of the five clarifications of RT-345's closure rule is in the body. RT-371, the leak in the "depends on one kind" rule, is closed on measurement. RT-345, the finding that the swap's dose differed between the two task groups, stays open. The stand-in measurement now forecasts that the step-3 threshold would trip in the operator and unit kinds, with the routine cell taking less swap (RT-380). The reviewer finds that version 0.4 can go to John for his section 10 rulings with RT-345 carried open. Four serious findings (RT-380 to RT-383) and six worth noting (RT-384 to RT-389) are to be fixed in a version 0.5, before the battery specification is committed at step 3.
