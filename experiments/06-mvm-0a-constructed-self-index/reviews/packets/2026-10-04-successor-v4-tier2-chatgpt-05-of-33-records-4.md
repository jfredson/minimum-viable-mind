*This is file 5 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 4 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 4 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
- `accuracy_whole`: the share of transplant trials where the action is the
  value the donor's identity dictates, under the whole-state transplant.
- `accuracy_ownership_only`: the same share under the ownership-only
  transplant.
- `accuracy_untouched`: the same share with no transplant at all: the
  no-transplant rate. Section 6.4 says what it must be near.

**The reading is the chance-corrected form** (ruled 2026-09-25, the queue
ruling, page 2):

    degree = (accuracy_whole − accuracy_ownership_only) / (accuracy_whole − accuracy_untouched)

**with the raw difference and both accuracies always reported beside it**, and
the no-transplant rate with them. Zero means fully separable: transplanting
the ownership answer alone does everything transplanting the whole state
does. One means the ownership-only transplant did nothing at all: the act
resists being pulled apart at these sites. The separation bar (section 9, 1a)
and the floor (1c) are written on this scale.

**Why this form and not version 1's.** Version 1 divided by `accuracy_whole`
alone. A no-transplant rate that sits under both terms does not cancel in
that ratio, so the largest value version 1's reading could return was
different for every arm: the ceiling failure of Amendment A3 with the zero
replaced by a moving number (the Gate C review of version 1, finding RT-172,
the per-arm-ceiling finding, in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`;
failure 1 of `docs/known-failure-modes.md`). The rehearsal confirmed it and
demonstrated the repair: on two made-up systems with the same true share
outside the subspace, 0.5, and different transplant strengths, version 1's
form read 0.4323 and 0.3222, and the chance-corrected form read 0.5018 and
0.5013 (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`, section
5, from `out/denominator_simulated.json`). The top of the chance-corrected
scale is 1 on every arm; section 17, failure 1, prints it for all twelve
toy arm-and-seed pairs under this version's rules.

**Readings outside 0 to 1 are reported as observed and never clipped** (the
repairs rulings, the paragraph after item 5). A negative reading means the
ownership-only transplant moved the action more than the whole-state one; a
reading above 1 means the ownership-only transplant landed below the
no-transplant rate. Both are sampling noise around "the subspace does
nothing" when small (arm C reads 1.0051 at one toy seed; the controls re-run
at `821f154`, section 2) and a warning about the instrument when large. The
rehearsal showed a negative value is reachable (rehearsal item R-4).

### 6.4 When the measure returns no verdict

The closed Amendment A3 design registered a comparison whose denominator was
zero from the day it was registered, and nobody noticed for four days after a
red-team pass had said so in plain words (ledger item RT-21, the unequal
ceilings finding). This measure has a denominator, so it gets explicit
no-verdict rules, written before it runs:

1. **The whole-state floor (ruled, the queue ruling, page 1c; refined by the
   repairs rulings, item 4).** A site set is usable only if the whole-state
   transplant clears **four fifths of the arm's own own-directed accuracy on
   the same fresh episodes**, written on the chance-corrected scale:

       accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy − accuracy_untouched)

   The plain form, `accuracy_whole ≥ 0.8 × own_directed_accuracy`, is
   printed beside it everywhere, so a reader can see whether the two readings
   of the ruled sentence ever disagree; on the toy they never did (MEASURED: 0
   disagreements across all site sets, arms and seeds, the repairs findings at
   `882f252`, section 3; the re-run records both forms on every row,
   `out-v3-rules/measure_*_seed*.json`, `reading.floor`). *Turning the ruled
   sentence into the first form is this design's choice and is marked ARGUED
   in the repairs method note.* If no site set clears the floor for an arm,
   that arm returns **no verdict** at nomination, and that is recorded rather
   than repaired. The floor keeps the denominator away from zero by
   construction: on an arm that has learned the task,
   `own_directed_accuracy − accuracy_untouched` is large, and the denominator
   is at least four fifths of it.

   **The floor is applied twice, on different episodes (the review of
   version 3, RT-234, accepted 2026-10-03, page 3).** At nomination it is
   applied on development episodes, to decide which site sets are candidates.
   At the reading it is applied again, on the fresh episodes. **A site set
   that clears on development episodes and misses on fresh ones returns "no
   verdict: floor missed on fresh episodes"**; the nomination is frozen by
   then and is not redone. On the toy the two agree on all twelve arm-and-seed
   pairs, and the narrowest margin is arm F seed 0 on development episodes,
   0.4433 against 0.4280 needed, which is 9 episodes of 600 (MEASURED: the
   review, RT-234; the controls re-run at `821f154`, section 4, "the
   whole-state floor on fresh episodes clears on all twelve").
2. **The fit floor, on the piece that is transplanted (ruled, the rulings on
   the review of version 2, RT-212, item 1; applied per arm and seed, ruled
   2026-09-26 on decision 21; moved from the whole read to the piece by the
   rulings of 2026-10-03, page 1).** Only a size of piece whose own held-out
   accuracy reaches **four fifths** on development episodes may be chosen
   (section 7.2, item 3, gives the rule in full). An arm and seed with no
   size that reaches it returns **"no verdict, read failed its floor"**, and
   the transplant arithmetic is not reported as a reading. The piece's count
   and the whole read's count are both printed in the reporting table, with
   the label-permutation null beside them as a reference and not as the bar.
   **The floor is on the piece only (ruled 2026-10-03, late evening, ruling
   1).** The ruling of 2026-09-26 put the floor on the whole read, at the
   worst layer of the nominated site set. The morning ruling of 2026-10-03
   moved it to the piece and did not say whether the whole read must still
   clear four fifths in its own right. John ruled that it need not: the
   whole read's count is printed beside the piece's and is not a second
   condition. That is how the controls re-run ran
   (`experiments/rehearsal-successor-measure/src/rerun_controls.py`,
   `PIECE_MIN`; its method, rule 9). On the toy the two readings give the
   same twelve verdicts: every chosen piece's whole read is right on 176 or
   more of 180, and arm F misses both. They can differ in principle, because
   a piece can score above its whole read by an episode or two (on arm F seed
   1, 17 against 12; on the named agent's read of section 7.3, item 2, 139
   against 137). The alternative that was put and not taken: require both.
3. **The no-transplant sanity rule, with the review's formula and the
   allowance as re-worded (ruled, the Gate C rulings, RT-222).** Version 1
   said the no-transplant rate "should be near the one-in-eight guessing
   rate; if it is not, the pairing is broken and nothing is read". With
   distinct values that rule is pointed the wrong way round: a model that has
   learned nothing lands near one in eight and a model that has learned the
   task lands far below it (the Gate C review of version 1, finding RT-173;
   failure 3 of `docs/known-failure-modes.md`). The registered rule is the
   review's formula: with *p* the arm's own-directed accuracy on the same fresh
   episodes, the no-transplant rate should be near

       (1 − p) / 7

   because an untransplanted model lands on the donor's answer only by erring
   onto exactly that one of the seven other slots. **The rule carries room
   for a miss of at most the largest measured miss, rounded up to 0.018.**
   The largest miss the rehearsal measured against this formula was 0.017536,
   on the free arm at one seed (MEASURED:
   `docs/2026-09-21-successor-measure-rehearsal.md`, section 5, from
   `out/denominator_floor.json`); version 2 wrote the allowance as 0.0175,
   which that very case fails (the Gate C review, RT-222). On the repairs'
   fresh episodes every miss was inside 0.0132 (the repairs findings at
   `882f252`, section 6.4). A measured no-transplant rate more than 0.018 from
   the formula's value means the pairing is suspect, and nothing is read for
   that arm. **The detection margin at the bar is printed in the reporting
   table**: if a pairing is broken so that the donor's answer is unrelated to
   the recipient, an untouched model hits it one time in eight, and at an
   own-directed accuracy of 0.2633 (the learn-both bar) the formula gives
   0.1052, so the rule flags the broken pairing by 0.0198, a margin of only
   0.0018 over the allowance; at 0.56, the toy free arm's level, the margin
   is 0.0441 (MEASURED: section 17, failure 3). The mechanism is not changed
   this weekend.
4. **A reading outside 0 to 1** is reported as observed (section 6.3), not
   clipped and not suppressed.
5. **If a control that holds fails** (section 7.3: the null transplant,
   control 7; the content transplant, control 1, on arm T only; and the
   too-early-position control, control 4, as redefined), the reading is not
   made for that arm and seed. **A requirement on the registered code: it
   withholds the reading itself.** The toy re-run's code computed each of
   these as a true-or-false field and printed the reading regardless; every
   one passed, so no reading was printed that should not have been, but the
   withholding was left to the reader of the table (the check at `e184a6e`,
   section 4, item 3). In the registered code a failed control that holds, a
   no-transplant miss outside its allowance, or a floor missed on fresh
   episodes replaces the reading with "no verdict" and its reason, in the
   output file and in the table.

**The only subtraction anywhere in this design is of the measured
no-transplant rate, in the chance-corrected form of section 6.3, and nothing
wider.** No ownership-blind ceiling is estimated, subtracted or divided by
anywhere. (This sentence replaces version 1's "No normalisation by an
ownership-blind ceiling anywhere", as the queue ruling's page 2 directs: the
outside review's one-line warning still stands, and the programme has already
paid for the lesson once; what has changed is that the no-transplant rate is
a measured quantity of the pairing, not a ceiling, and subtracting it is what
gives every arm the same top of scale.)

---

## 7. The measurement procedure

### 7.1 Data split, and what "fresh" means

Three disjoint sets, generated from separate seeds and committed before use:

- **Training episodes**: what the arms are trained on.
- **Development episodes**: the only data on which anything is chosen: the
  site set, the nominated subspace, its rank, and any tuning at all. **The
  straight-line reads are fitted on development episodes, written to disk and
  reloaded**; they are never refitted on the episodes the reading is taken
  from (the rehearsal caught itself doing that and fixed it before any result
  was read: `docs/2026-09-21-successor-measure-rehearsal.md`, section 9, item 3).
  The fit of section 7.2, item 1, is scored on a held-out part of the
  development episodes (on the toy, the last 180 of 600), never on the fresh
  episodes.
- **Fresh episodes and confirmation seeds**: evaluated once, after the freeze.

**"Fresh" is disambiguated, as the rehearsal required** (its section 7, item
4). Version 1 asked for "marker and content combinations that appear in
neither of the other two sets", and that phrase has two readings. **The
registered reading is the weak one: unseen *combinations* of marker words,
items and values that the arm has each seen in training**, the rehearsal
grammar's pool named `fresh`, which draws from the training vocabulary with
its own seed (`experiments/rehearsal-successor-measure/src/grammar.py`, the
`POOLS` table). The strong reading, marker words the arm has never seen, is
**kept as a named diagnostic and is never the evaluation set**: under it the
separable arm's own accuracy fell to 0.7612, 0.6512 and 0.6512, the
whole-state transplant was capped there, and the reading went negative on two
seeds of three (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`,
section 7, item 4; the pool named `unseen-vocabulary` in the same grammar
file). The registration says which reading it means in these words.

### 7.2 Choosing the candidate ownership representation: one instrument

On development episodes only, for each arm, **identically**: one function,
which takes no argument that names an arm, called the same way for every arm
(the repairs' `experiments/rehearsal-successor-measure/src/repairs.py` and the
re-run's `src/rerun_v3.py`, both at `9d9d31a`, and the controls re-run's
`src/rerun_controls.py` at `821f154`, do this, and their nomination tables
show one rule applied throughout). **The registration says in one
sentence that the rule's outputs differ per arm, and differ by seed within
arms C, F and M** (ruled, the queue ruling, page 3; MEASURED on the toy: arm C
is nominated at layer 2 at the action position, layer 1 at the action
position and the three before it, and layer 1 from the first own turn to the
action, on its three seeds; the controls re-run at `821f154`, section 3).

1. **The label, its route to the states, and the fit floor.** The
   straight-line read is fitted against **which marker word is the model's
   own**. *The route by which that quantity reaches the model's states, in one
   sentence:* the marker word is the input token at every turn the model's own
   assignments are spoken on, so it is carried by the token into the running
   state; and on an arm whose slot is built from it (arms T and M) or which
   multiplies it into content (arm C), the read recovers it at 0.96 or better
   from the first block onward. **What version 2's route sentence went on to
   claim, that which marker word is the model's own is forced by the loss at
   the own-directed action, is false for a freely trained system and is
   struck** (the Gate C review, RT-212): an own-directed action can be solved
   by attending to the value tokens on the turns the acting channel marked,
   without knowing which marker word those turns carry, and the toy free arm
   does exactly that (section 5.4). Ruled 2026-09-23
   (`docs/rulings/2026-09-23-nomination-label.md`; fixed in code as well as in
   text: the repairs code's `READ_LABEL = "marker-word"`, and the successor's
   measurement code when written, per the queue ruling, page 3). The label
   was ruled on the separable arm alone, which is the one arm whose slot is
   made of the label by construction (that ruling's section 4), and it is the
   only one of the three readings of "which agent is acting" that recovers a
   degree known independently of the instrument; the other two, the agent's
   slot and the marker's rank, put an arm whose degree is zero by construction
   at the entangled end of the scale.

   **The fit floor (ruled, the rulings on the review of version 2, RT-212,
   item 1; moved to the piece by the rulings of 2026-10-03, page 1, item
   1).** In the ruling's words: "only sizes whose own held-out accuracy
   clears four fifths may be chosen, and that accuracy is printed in the
   reporting table", beside the whole read's. "The accuracy of a piece is the
   held-out accuracy of a read given only the state's coordinates inside that
   piece, on the same development episodes and split as the whole read. An
   arm and seed with no size that clears returns 'no verdict, read failed its
   floor'." The floor is absolute, the same convention as the whole-state
   floor. The label-permutation null, the fit the whole read reaches when the
   labels are shuffled (two hundred shuffles at toy scale; its 95th and 99th
   percentiles), is reported beside it and is not the bar. The reason
   recorded in the ruling of 2026-09-26: a permutation null alone would
   likely certify a read at 0.172, which recovers the label on about one
   episode in six, and that is not an instrument worth transplanting. **The
   floor applies per arm and seed** (ruled 2026-09-26 on decision 21,
   recorded in the rulings file at `9ed9f8c`): an arm's three seeds are
   reported one by one, each a reading or a no verdict, and the across-seed
   spread of section 9 is taken over the seeds that read. The whole read's
   count is printed and is not a second floor (section 6.4, item 2).

   **How the accuracy is stated, and on what it is computed (the review of
   version 3, RT-232; accepted 2026-10-03, page 3, as the review states the
   fix).** Every fit in the registration and in the reporting table is
   **stated as a count of held-out episodes** (on the toy, of 180; the floor
   there is 144). **The registration names the device and the number format
   the registered fit is computed on, and the figure on that device is the
   registered one.** The reason: the floor is a hard line, per arm and seed,
   and on the toy two of twelve reads moved by exactly one held-out episode
   between the laptop's processor and its graphics chip (arm F, 32 against 31
   and 18 against 19; the other ten were identical; MEASURED: the review,
   RT-232; the controls re-run at `821f154`, section 3), so a fit within an
   episode or two of four fifths could pass on one device and fail on the
   other. **Ruled 2026-10-03, late evening (ruling 3):** the registered fit is
   computed on the laptop's **processor**, never its graphics chip; the
   model's states are computed in the model's own 32-bit floating-point
   format; the read is scikit-learn's logistic regression, which fits in
   64-bit; and the versions of torch, scikit-learn and numpy are recorded in
   the output file, as the controls re-run did (torch 2.12.1, scikit-learn
   1.9.0, numpy 2.5.0, `out-controls-rerun/summary.json`). **Reconciled
   2026-10-03 (night): those versions are also pinned, in a committed file
   named in the registration**, in the way `.venv-lock-2026-08-28.txt` does
   for the project's environment, so that a line read to one episode does not
   move because a library was upgraded between the registration and the
   reading (`docs/rulings/2026-10-03-version-4-questions-rulings.md`, ruling
   3; `docs/rulings/2026-10-03-seven-questions-reconciliation.md`). The processor is the device the
   controls re-run and the short pre-stated run, which supply every toy
   figure in this version, ran on. The alternative that was put and not
   taken: the graphics chip. **In the registered run the
   read is fitted once, on that device, written to disk and reloaded
   (section 7.1); the printed whole-read count and the transplanted
   directions come from that one fit.** On the toy re-run they came from two
   fits of the same read: the directions from the coefficients committed
   earlier on the graphics chip, and the printed count from a fresh fit on
   the processor (the check at `e184a6e`, section 4, item 2); on the built
   arms nothing turns on it.

   **The toy demonstration (MEASURED: the controls re-run at `821f154`,
   sections 2 and 3; reproduced by the check at `e184a6e`, section 3).** The
   floor returns no verdict on arm F and a reading on arms T, C and M. Right
   of 180 held-out episodes at the action position, whole read then chosen
   piece: arm T 180 and 180 on every seed; arm C 180 and 180, 177 and 172,
   176 and 150; arm M 180 and 180 on every seed; arm F 32, 12 and 18 for the
   whole read, with no piece above 34 at any layer or size. The lowest piece
   among those that clear is 150 of 180. The permutation null's 95th
   percentile sat at 0.111 to 0.128 (about 20 to 23 of 180) across all twelve
   pairs on the earlier re-run (`docs/2026-09-26-toy-rerun-v3-rules.md` at
   `9d9d31a`, Part 1, section 1.3; the check at `70be9fb`, section 3.2; that
   null is for the whole read, on the graphics chip, and was not recomputed
   on 2026-10-03). **One clause of the rulings file's refinement item 2 was
   wrong on this point and carries an annotation** (the rulings file at
   `da41c20`, pull request 68): it said that under the layer-0 removal "arms
   C and F still fall to the fit floor"; arm C does not, and only arm F falls
   to the floor. Nothing ruled depends on the clause.

   **The route (b) investigation, and what it found (the Gate C rulings,
   RT-212, item 3; the result ruled 2026-09-26).** Route (b) asked for a label
   the own-directed loss does force on a free system, which a straight-line
   read can recover on arm F at four fifths. The free-arm label search
   (`docs/2026-09-26-free-arm-label-search.md`, main line at `a97c12b`, pull
   request 66; laptop only, $0,
   nothing retrained, on the committed arm F models) tried three candidates
   under the registered site-set rule at toy scale, with a floor of 0.80 on
   held-out fit and a 200-shuffle label-permutation null at each site.
   **None clears the four-fifths floor on arm F, at any site set, on any
   seed.** The best is 0.789, from candidate 1 (which earlier turns are the
   model's own), and that from position spans that start at one of the
   model's own turns, so that where the span starts gives part of the answer
   away; anchored at the action position the three candidates reach 0.733,
   0.383 and 0.478. All three sit well above their shuffle null, so they are
   carried by the free arm, just not at the floor (MEASURED: the search's
   findings at `a97c12b`, sections 1 and 2; its check,
   `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`,
   main line at `ecd2b6c`, pull request 70,
   recomputed every best fit, shuffle summary and verdict from the committed
   files with no disagreement, and confirmed the twelve models against the
   committed fingerprint list; its section 6 narrows the search's closing
   sentence to "none of three candidates chosen in advance", which is how it
   is stated here). **John's ruling of 2026-09-26 (the rulings file at
   `a11f1d3`, "RT-212 item 3 resolved", items 1 to 5): this version registers
   with the fit floor alone; the ruled label, which marker word is the model's
   own, stays the one registered read; the three candidates enter the toy
   record as exploratory fits, not as registered reads; the experiment
   proceeds; and the first release's single arm F run reports its nomination
   fit against the floor, a miss being a stop before the second release
   draws** (section 11, step 5a). The reason recorded there: the fits rising to
   0.79 above a 0.10 shuffle baseline on the small toy model is the argument
   that the deeper registered model may clear the floor, and $44 is the price
   of finding out before $130 is spent. **The depths, stated the same way in
   both places (the review of version 3, RT-236; accepted 2026-10-03, page
   3): the toy has four blocks and five running states; the registered model
   has twelve blocks and thirteen running states.** The ruling as recorded
   calls the toy "a five-layer model" and the registered one "twelve-layer",
   which counts states for one and blocks for the other; the rulings file
   carries a dated note beside the phrase and stands as recorded. Like for
   like, the registered model is three times as deep, not two and a half. **The search also printed a
   fit for the ruled label on arm F of 0.556, 0.483 and 0.433 over its 60 site
   sets, which is not the 0.172 the Gate C review and the re-run report. The
   check reconciled the two: they are different reads of the same models,
   episodes, split and fitter.** The registered rule fits one read per layer
   at the action position only and reports the worst layer of the nominated
   set; the search fitted one read per site set, with the layers and
   positions of the set laid end to end and the post-identity span averaged,
   and all three of its higher figures come from that averaged span at layers
   0 to 1 or 0, which starts at the model's own marker word and which the
   layer-0 removal of item 2 excludes. On the search's own cell for the
   registered read (layer 1, the action position) it prints 0.172, 0.067 and
   0.106 to the digit (MEASURED: the check at `ecd2b6c`, "Verdict" and section
   2). Item 3 registers which read is meant, so the two cannot be confused
   again; the 0.172 is the registered read's figure as the graphics chip
   computed it, and on the processor the same read is right on 32 of 180.

===== END OF RECORD 4, part 4 =====

