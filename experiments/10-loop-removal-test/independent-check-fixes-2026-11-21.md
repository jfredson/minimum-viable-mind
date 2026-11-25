*Filed 2026-11-21 by the session that wrote the generator and its fixes, verbatim as the checker returned it. The checker was a fresh Claude Code session with no history of this conversation, which wrote none of the design, the specification, the lists, the generator, the pilot, the fixes, or any earlier review or check. It worked read-only in a detached worktree at commit 0879327, using only its own scratch folder, which was created empty for it, and it had no web access. Nothing in its text was changed in filing. One sentence under RT-433 ("That is 14 fewer than...") is garbled in the original and is left as returned. The filer's check follows, below a rule, and is not part of it.*

---

# Independent check: the four generator fixes and the regenerated pilot set

*Checked 2026-11-21 by a session that wrote none of the design, the battery specification, the generator, the content lists, the pilot set, the fixes, or any earlier review or check. Commit checked: 0879327, in the read-only worktree `.claude/worktrees/check-fixes-2026-11-21`. Nothing was run on the model, nothing was downloaded and nothing was spent.*

## What I opened

- **The previous check,** `experiments/10-loop-removal-test/independent-check-2026-11-21.md`, all of it, including the author's note at the bottom.
- **The specification,** `battery-authoring-spec.md`, all of it, with section 14 (the amendments) read closely.
- **The three scripts,** all of them, line by line:
  - `src/build.py`, the generator;
  - `src/check_overlap.py`, the check that keeps the pilot half and the test half apart;
  - `src/step3_checks.py`, the free step-3 checks.
- **The history.** The output of `git log`, and `git diff c02b763 0879327` for the code. I also unpacked five commits into my scratch folder with `git archive`, so that I could run each one's generator: c02b763 (the generator behind the first pilot), b7fea23 (the first fix), d4171f1 (the regenerated pilot), 54fa782 (the place fix) and 0879327 (the checked commit). I took the first pilot's files from commit 889f9e4 with `git show`, to compare old against new.
- **Every file in `batteries/pilot/`.** Scripts parsed every line of every file. I read a sample of whole chained items and the build report's donor tables.
- **The findings.** The addendum at the end of `step3-findings-2026-11-21.md` in full, and that file's sections on donors, dose, tail shares, the average and the chained items.
- **The design,** `docs/loop-removal-test-design-2026-11-20.md`, only lines 222 to 256 (the average method and its fallback) and lines 698 to 712 (the bites check). I found them by searching.
- **The research model's tokeniser and chat template,** only through the `tokenizers` and `jinja2` libraries, by way of the generator's own `Model` class.

## What I did not open

- The content files in `data/`. I used them only as the generator loads them.
- The other sections of the design, every other review and closure check, and `docs/outside-review-protocol.md`.
- Any outside source. I had no web access.

## Where I worked

I used only my own scratch folder, `/private/tmp/claude-501/loop-review10-KSSVeD`, for every script and every output. I opened no other scratchpad or tmp folder.

One thing needs recording. My first runs of the overlap check and the step-3 checks import `build.py`, so Python wrote a bytecode cache folder, `experiments/10-loop-removal-test/src/__pycache__/`, into the worktree. Git ignores that folder, so `git status` did not show it. I deleted it, and I ran every later script with `-B` so that no cache was written. The worktree now shows no changed, untracked or ignored files, and HEAD is still 0879327.

## What is reproduced, and what is judgement

**Reproduced exactly (MEASURED).**
- **The pilot.** I ran `build.py --half A --seed 1` at 0879327 with the real tokeniser into my scratch folder. All six output files are byte-identical to the committed pilot: `pairs.jsonl`, `donor_only.jsonl`, `chained.jsonl`, `chained_donor_only.jsonl`, `neutral.jsonl` and `build-report.json`.
- **The overlap check.** It passes on my copy (exit 0), and its output is identical to the committed `overlap-check.json`.
- **The step-3 checks.** On my copy they write a `step3-results.json` that is byte-identical to the committed one.
- **The author's account of the order of commits.** It is confirmed:
  - The generator at 54fa782 is byte-identical to the one at 0879327, and run with half A and seed 1 it reproduces every committed pilot file byte for byte.
  - Between d4171f1 and 54fa782, only `build.py` changed. No pilot file changed.
  - The generator at b7fea23 does not reproduce the pilot. Its unit items put 11 of 30 right answers in the middle place, which matches the author's account of the first, discarded version of the place fix.
  - So the committed pilot was made by code committed later, in 54fa782, as the addendum says.

**Measured by my own scripts.** These are the counts behind every finding below:
- a parser that follows each chain from each start name;
- the shortcut tests;
- simulations of 20,000 draws for each number kind, made with the generator's own functions;
- the copying-rule trace;
- the donor recounts;
- the order check over 2,000 seeded streams;
- comparisons with the c02b763 generator, in both halves.

**Judgement (ARGUED).** Whether a model would use a cue, how the length of the chained items bears on the average method and on the bites check (the check that the removal really hurts chained lookup), and how serious each point is.

## The four fixes

### RT-415 and RT-426: the chained lookups, and their donors. Closed.

**The structure (MEASURED).** I parsed all 102 chained items: the 40 scored ones and the 62 kept only to serve as donors. In every one:
- there are exactly five chains, each starting from a name that no row points to;
- no name is pointed to twice, and no name sits on two chains;
- there are no loops, and no row lies off a chain;
- each of the five candidate colours appears in exactly one "is colour" row, and is reached by exactly one chain.

Following the chain from the stated start name gives the stored answer in all 102 items, in exactly the stored number of steps. All candidates are single tokens.

**The shortcuts I tried (MEASURED, on the 40 scored items).** Picking by any rule that does not follow the chain is right at about the chance rate of 8 in 40:

| Shortcut | Right |
|---|---|
| The first colour in the text | 4 |
| The last colour in the text | 8 |
| The colour row nearest the start name's row | 6 |
| The first colour row after the start name's row | 7 |
| The last row is a colour row and holds the answer | 1 |
| The answer's chain is the unique longest | 4 |
| The answer's chain is the unique shortest | 2 |
| The only chain end that shares a syllable with the start name | 7 |

Some other cues give nothing away either:
- **The order of the rows.** The start name's row sits evenly among the five start rows (7, 10, 9, 8 and 6), and so does the answer's colour row among the five colour rows (4, 9, 10, 9 and 8).
- **Names that appear only once.** Exactly four names appear only once in each item's text. They are the four other chains' start names, because the target's start name also appears in the question, so they do not point to the answer.
- **Chain lengths.** The other chains' lengths are spread evenly from two to six steps (31, 37, 32, 34 and 26 chains), the same spread as the target chains. So a chain's length does not mark the target.
- **Shared syllables.** The answer's end name shares a syllable with the start name in 15 of 40 items. Chance is about 11 of 40, so this is within chance. The generator draws names with no link between them.

**Donors (MEASURED).** I wrote my own version of the stated rule: same number of steps, a prompt at least one token longer, and the donor's answer not among the recipient's candidates. Under it, every scored chained item has 5 to 15 eligible donors, with a mean of 8.35, which agrees with the build report. The rule is well defined. The code adds a bar on exact copies, which is harmless.

### RT-416: where the right number sits. Closed as specified.

**The fix (MEASURED).** The generator now draws the right number's place before it draws the numbers, and it keeps that place while it redraws them. In 20,000 simulated draws for each kind at 0879327, every place holds 19.4% to 20.4% of right answers. No draw failed, so none fell back to a new place. On the pilot, a chi-square test of the place counts gives p = 0.91 for operator items, 0.32 for unit items, 0.74 for sums and 0.20 for products. At c02b763 it gave 0.005, 0.01, 0.001 and 0.12.

I confirmed the author's two figures:
- In half A, a product answer can fill the five places in 18, 17, 16, 15 and 14 of the 22 possible answers.
- The chance of no product answer at the top place, across 15 items, is 0.8^15 = 3.5%.

**Remaining cues.** These are covered in RT-432 and RT-433 below.

### RT-418: the copying rule. Closed, with no harmful over-blocking.

**The fix (MEASURED).** The code's list of ignored words is exactly the specification's list of 20 function words. I wrote the rule again independently and applied it to all 324 pairs, scored and donor-only. No candidate in either cell contains, or is contained in, a content word of the routine fact or of either final question. The cross-cell rules also hold in all 324: neither twin's right answer is among the other twin's candidates. The first pilot had 3 breaches under the new rule, all "give".

**Over-blocking (MEASURED).** I traced every block made while the pilot was built.
- **Scored pairs.** Building them caused only 3 drops for too few wrong answers and 1 for a right answer that copied a word.
- **Donor-only pairs.** The rise in drops (102 and 142) comes from the donor-only stage. That stage made 9,754 draws, against 6,753 before. The new rule's own block in it is "give", blocked 116 times. All three opposites pairings have "give" in one of their questions. So the opposite of "take" can no longer be a right or a wrong answer in any opposites group. That loses 1 of 76 opposite questions.
- **Other blocks.** These come from object or country names in the routine fact, or from the opposites list, and are allowed by the rule: "blue" in "blueberry", "lean" in "clean", "nut" in "walnut", "ant" in "elephant".
- **Effect on the groups.** Every group filled. The counts of distinct right answers are close to the first pilot's: 30 capitals and 30 opposites in both; 9 everyday colours against 11; 12 sums against 15; 13 products against 12; 21 letter-code words against 20. Nothing points to a skew.

### RT-422: the order of an odd group's extra pair. Closed.

**The fix (MEASURED).** The extra pair's order is now drawn from the seeded stream. Across 2,000 streams and the six odd groups, the extra pair put the rule's facts last 51.0% of the time. In the pilot it did so in 2 of 6 groups (operator with capitals, and lookup with sums), which gives the totals of 59 and 61.

## Other checks that passed (MEASURED)

**The pairs.** In all 324 pairs, scored and donor-only:
- both twins are the shared context plus their own question;
- the two twins have equal token lengths;
- every candidate is a single token;
- there are five different candidates, with the right answer among them;
- the stored prompt tokens recount equal.

**Donor-only pairs.** None serves no scored pair, and no eligible donor copies its recipient's rule content or routine fact.

**The stand-in figures** match the addendum:
- **Dose ratio** (the routine cell's swap size divided by the prompt-rule cell's): 0.994 to 1.000.
- **Tail shares** (the part of the changed span that comes after the shared context): 0.28, 0.34, 0.17 and 0.17.
- **The average-method token counts** (RT-387): equal, with a largest difference of 0.

**Template slots.** The chained items carry the same 12 template tokens before the text and 3 after it as the neutral passages, in 102 of 102.

**Copying the item's own numbers** (RT-429, the copying lure). It is not made worse. Wrong numbers equal to a number in the item's own text fell from 11 scored items to 5.

## Findings

**RT-430 (worth noting, MEASURED): in the chained items, a donor's text usually names some of the recipient's candidate colours, and step 3 does not report it.**

Each chained text names five colours. So for five donors drawn at random, as step 4b will draw them:
- a donor names the recipient's right answer 91 times in 200 (46%);
- it names each wrong candidate 292 times in 800 (36%).

This is the chained version of the lookup case in RT-411 (colours named in donors' tables). The bites check's swap reading should carry the same note beside it. Step 3's check 9 (candidate words in donors' contexts) covers only the scored pairs, so it should add the chained items.

**RT-431 (worth noting, ARGUED from measured lengths): the fix makes the neutral set's shortfall much worse for the chained items (RT-425).**

- **The lengths.** The chained items now run 195 to 284 tokens, with 20 to 30 rows. The scored pairs run 50 to 97 tokens, and the neutral passages 39 to 95. Before the fix, the chained items ran 78 to 116 tokens.
- **The average is still defined.** The pooled average is defined at any length (design, the average method). The ten-bin fallback uses relative position, and I confirmed the template slots match.
- **But it is untested at these lengths.** Both the average and its damage would be built and judged only on passages of at most 95 tokens, and then applied to texts up to three times longer. The bites check compares the main removal with a random comparison under the same method, which may cancel part of any mismatch. Whether it does is not measured.

The specification asks for neutral lengths spread "to the longest scored item". If the chained items count as scored (they are scored under both methods), the neutral set should reach about 284 tokens.

**RT-432 (worth noting, ARGUED): the rebuilt chained items are much harder, and nothing yet shows the model can do them at three passes.**

- **Harder.** Each item now asks the model to follow up to six steps through 20 to 30 shuffled rows of invented names. The design's bites check needs the one-pass run to cost at least 0.15 on chains of four or more steps. That cannot happen if the full model is already near chance on them, and the confidence check would drop many of them.
- **Not settled yet.** This is not a fault in the fix. It is a risk the fix created, and only step 4b can settle it. A low baseline on the four-to-six-step chains would make the result "not testable" for a reason unrelated to the removal.
- **The design's wording.** The design describes "several lookup tables", while section 14 keeps one list holding five chains. The specification should say that this is deliberate.

**RT-433 (worth noting, MEASURED rates, ARGUED effect): cues in the numbers that the place fix does not touch.**

- **Multiples of n.** In the unit items, the right answer (k × n) is the only candidate that is a multiple of n in 21 of the 30 scored items (70%). The simulation gives 68%. The first pilot had 60%. The version without the rule still says "You have {n} ...". So a model that leans toward multiples of n could beat chance by more than 0.10 without the rule. That would fail the unit kind on the "rule is needed" check, which runs on the model. The check would catch it, so the cost is losing that kind, not a wrong reading.
- **Multiples of 5.** In the simulation, half-A unit answers are multiples of 5 in 35% of items, against 20% of wrong numbers, because k = 5 always gives one. This pilot happens not to show it (20% against 21%).
- **Impossible small numbers.** Wrong numbers of 0 to 3 appear 11 times in the scored unit items, and once in the scored sums, where no answer can be below 4. A model can rule them out. That is 14 fewer than... (in the first pilot there were 14 in the unit items and 3 in the sums), so this is not made worse.
- **The spread of the five numbers.** Someone who saw all five numbers could still guess right 36% to 52% of the time on the pilot, and 39% to 44% in simulation, by picking the number that every other candidate lies within the spread of. The model never sees the candidates, though: each is scored at the answer position. So I judge this harmless, and I raise it only so that it is not mistaken for something RT-416 missed.

**RT-434 (worth noting, MEASURED): the place fix slightly increases the wrong numbers that fall outside their half's range of answers (RT-424, numbers crossing the halves).**

The table shows the share of wrong numbers outside the half's answer range, from 5,000 simulated draws per kind and half:

| | c02b763 | 0879327 |
|---|---|---|
| Half A products | 8.3% | 11.9% |
| Half B products | 6.9% | 8.1% |
| Half B sums | 2.8% | 3.2% |
| Operator and unit items | about the same | about the same |

The cause is the extreme places. An answer at the top or bottom place now draws all four wrong numbers from one side, so items near a range edge spill over. For example, a half-B product of 40 at the top place needs four lower products. Those can only be half-A values, such as 28, 30, 32, 35 and 36. This must be settled with RT-424 before the test set is made.

**RT-435 (worth noting, MEASURED): one scored pair can never have a donor, and under the design it will be dropped.**

The pair is A-0085, letter code with everyday colours, object "a tiger's stripes". At 92 tokens it is the longest pair in its group (the others run 87 to 90).
- **Measured.** I simulated 6,000 donor draws for that group. 5,747 made pairs, but only 7 were long enough, and all 7 had a right answer among A-0085's candidates. None was eligible.
- **Why.** It does not come from the fixes' rules. The new random stream picked the longest object for this group. Raising the draw budget would not help.
- **What happens next.** The design says a pair with no eligible donor is dropped (the swap method). So this group scores 5 pairs, and the letter code 29. The step-4b counts should expect that. A generator that kept each group's longest pair donor-able would avoid it at the test set.

**RT-436 (worth noting, MEASURED by reading the code): the checks do not yet cover the chained files fully (adds to RT-417, the incomplete overlap check).**

- **The overlap check** (`check_overlap.py`) reads only `pairs.jsonl` and `donor_only.jsonl`. It does not read `chained.jsonl`, or the new `chained_donor_only.jsonl`, which the fix added.
- **Step 3's "reached by a chain" count** checks only that an "is colour" row exists for each candidate. It does not follow the chains.
- **Step 3's check 10** (the average is defined everywhere) covers the pairs only.
- **The chained donor report** lists ids only. It omits the content and length place that section 8 asks for when an item has no donor.

On this pilot none of these gaps hides a fault, because my own chain-following and slot checks pass on all 102 items. They should be closed together with RT-417.

## Did the fixes make the findings left open worse?

- **RT-425 (the neutral set):** yes, for the chained items (RT-431).
- **RT-424 (numbers crossing the halves):** slightly (RT-434).
- **RT-417 (the incomplete overlap check):** slightly, through the new file it does not read (RT-436).
- **RT-429 (wrong numbers copying the item's own numbers):** no; it improved.
- **The rest:** I saw no change to RT-419 to RT-421, RT-423, RT-427 or RT-428. All of them stay open for before any test set.

## RT-345 (the swap's dose may differ between the cells)

It stays open. Nothing here bears on it.

## Verdict

**The reproduction.** The regenerated pilot is exactly what the committed code produces. It reproduces byte for byte at 0879327 and at 54fa782, and the author's account of the order of commits is accurate.

**The four fixes are closed.** Each holds by a measurement that would have failed if the fix were wrong:
- every chained item has five disjoint chains, every candidate is reached, the stated answer is found only by following the chain, and no shortcut I tried beats chance;
- every chained item has at least five donors;
- the right number's place is uniform for each number kind;
- the copying rule catches question words in both cells, without thinning any group;
- the odd group's extra order is seeded.

**What the fixes broke.** Nothing at the heart of the pairs: the shared context, equal twin lengths, single-token candidates, the cross-cell rules, the dose ratio, the tail shares and the overlap check all hold.

**Step 4b.** As far as these fixes go, the pilot is fit for step 4b, and nothing must be fixed first. Before step 4b reads its results, three things should be in hand:
- the scored pair A-0085 will be dropped for want of a donor (RT-435);
- the chained bites-check readings carry the donor-colour note (RT-430);
- the risk that the longer, harder chained items fail the bites check for reasons unrelated to the removal is watched for at step 4b (RT-431, RT-432).

**Before any test set.** RT-433, RT-434 and RT-436 join the findings already open: RT-417, RT-419 to RT-421, RT-423 to RT-425, and RT-427 to RT-429. RT-345 stays open regardless.
---

## The filer's check (not part of the independent check)

*Written by the author of the generator, 2026-11-21. It closes nothing.*

- **The checker's worktree.** It was confirmed clean after the check: no changed, untracked or ignored files. That matches the checker's account of removing the `__pycache__` folder it had created.
- **RT-435, the pair with no donor.** Confirmed: the build report lists A-0085 (letter code with everyday colours) as the group's one pair with no eligible donor.
- **The garbled sentence under RT-433.** The intended figures can be read from the same bullet. Impossible small wrong numbers appear 11 times in scored unit items and once in sums, against 14 and 3 in the first pilot, so the fix did not make them worse.
- **Where things stand.** The four fixes (RT-415, RT-416, RT-418, RT-422, RT-426) are closed by measurement. As far as these fixes go, the pilot is fit for step 4b, with three things to have in hand when step 4b reads its results:
  - A-0085 will be dropped (RT-435);
  - the chained bites-check readings carry the donor-colour note (RT-430);
  - a low baseline on the longer chained items would make the bites check fail for reasons unrelated to the removal (RT-431, RT-432).

  RT-433, RT-434 and RT-436 join the findings open for before any test set. RT-345 stays open.
