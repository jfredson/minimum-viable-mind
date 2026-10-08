*This is file 7 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 6 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 6 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
1. **Content transplant, re-worded so it cannot veto the entangled arm.**
   Transplant the complement of the nominated subspace at the same sites.
   *On arm T it holds*: the action must not follow the donor's identity above
   the no-transplant rate plus the 0.018 room of section 6.4 (on the toy:
   0.0000 on every seed). *On arms C, M and F it is reported and cannot
   veto.* On an entangled arm the complement carries the ownership signal by
   construction, since in a system where ownership multiplies content at
   every layer there is no ownership-free complement to transplant, so on
   such an arm the complement is expected to reproduce the counterfactual
   almost as well as the whole state does. On the toy it does: arm C's
   complement moves 0.5450, 0.5625 and 0.5312 of trials against whole-state
   shares of 0.5400, 0.5550 and 0.5463; arm M's moves 0.3875, 0.3762 and
   0.4288 against about 0.78, about half, which is what a mixture would give
   (ARGUED); arm F's, for description only, 0.4838, 0.5637 and 0.5400 against
   0.4850, 0.5675 and 0.5300 (MEASURED: the controls re-run at `821f154`,
   sections 2 and 4). As version 1 wrote it, this control would have vetoed
   the reading on exactly the arm the control battery exists to validate, and
   on arm F it would have vetoed whatever the free arm turned out to be,
   which is the thing being measured. Its value on arms C, M and F is a
   description of how much of the identity-driven difference lives outside
   the nominated subspace, which is the reading itself seen from the other
   side.
2. **Another agent's representation: a reported description with no pass
   line; not applicable on arms T and M (ruled, the repairs rulings, item 5;
   and `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1).**
   Nominate, by the identical procedure with the named agent's marker word as
   the label and the named-other action as the anchor, a representation of
   the named agent who is not acting, and transplant it from a twin that
   differs only in which agent is named. **What is reported: how often the
   own-directed action moves under the named agent's piece, beside how often
   it moves under twenty random pieces of the same size at the same sites,
   reported as control 3 reports its twenty (median, 95th percentile, and
   the counts below, equal and above).**
   - **It has no pass line.** Version 3 proposed a tolerance of 0.05 over the
     random piece (its decision 15); John agreed to it on the morning of
     2026-10-03 and withdrew it the same day after the controls re-run. No
     number is registered for this control, so nothing about it is a
     pre-stated quantity the rehearsal failed to exercise, in the sense of
     item 5 of the 2026-09-21 ruling.
   - **The registration says in terms: this control never ran at toy scale.**
     It runs only on an arm that has learned the named-other condition
     (passes the section 8.1 bar on it), and only where a piece of the named
     agent's read reaches four fifths. Arms T and M are not applicable by
     ruling: they hold the named agent outside the running state by
     construction, so no transplant into the state can move that action. Of
     the other six toy models, five have not learned the named-other
     condition (arm C at 760, 751 and 708 of 3,000 and arm F seeds 1 and 2 at
     781 and 746, against 790). The one that has, arm F seed 0 (994), has a
     read of the named agent's marker that misses the floor: the whole read
     is right on at most 137 of 180 held-out episodes and the best piece on
     139, against 144 needed (MEASURED: the controls re-run at `821f154`,
     section 5, from `out-controls-rerun/measure_F_seed0.json`, `control2`;
     the check at `e184a6e`, section 3). That would have been a no verdict
     under version 3's rule too. Four attempts to repair the named-other
     condition have not produced a toy model that learns it (section 4.4).
   - **A no verdict is the expected result at registered scale too**, and is
     reported as "no verdict" with which of the two reasons applies.
   - **The part of its code after the floor has run once, and that run is NOT
     A RESULT.** The function has three early exits, and the controls re-run
     took all three: "not applicable" on the six separable and mixed models,
     "has not learned" on five, and the floor on arm F seed 0. What had never
     run was everything after the floor (the check of the short run, finding
     15). So that the registered run is not the first time that code
     executes, the
     re-run's own function for the control was called once on arm F seed 0
     with the piece's accuracy floor switched off for that one call, at $0.
     It ran without error and returned its figures: a site at layer 1, the
     action position and the three before it, 8 directions, a piece right on
     92 of 180 (the floor would have asked for 144); the own-directed action
     moved in 0.0012 of trials, under a random piece in 0.0063, and the
     named-other action in 0.0962. **Those figures are evidence that the code
     ran. They are not a pass or a fail of anything**, because the piece
     transplanted is not known to carry the named agent at all (**NOT A
     RESULT**, and **checked: the check of the short run at `53c8100`**:
     `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 5, from
     `out-short-prestated-run/part_c_NOT_A_RESULT.json`). What is still true
     after it: the control has never been exercised on a model whose read of
     the named agent clears its floor.
   - **Twenty random pieces, not one (ruled 2026-10-03, late evening, ruling
     5).** The re-run's code compares against a single random piece, drawn
     with its own seed (the check at `e184a6e`, section 4, item 4). John
     ruled that the registered description uses twenty. **That is a change to
     the control's code, owed with the registered measurement, so the code
     path that ran once on 2026-10-03, with a single random piece, is not
     quite the one registered.** The alternative that was put and not taken:
     leave it at one draw.

   The alternative that was put to John and not taken: exercising the control
   on a made-up case built for the purpose. This is the successor's own
   obligation, not the closed design's control run on 2026-09-21 (the review
   of version 1, finding RT-181).
3. **Matched random subspaces: the twenty-draw null. Reported, not gated
   (ruled, the rulings on the review of version 2, RT-214, items 1 and 2, as
   refined on 2026-09-26 by refinement item 1).** Twenty random subspaces of
   the same rank and the same norm at the same sites are each transplanted in
   place of the nominated subspace, on every arm and seed. The reporting
   table prints the median and 95th percentile of the twenty random donor
   shares, the ownership-only transplant's own donor share, and how many of
   the twenty draws fall below, equal and above it. The fixed 0.0175 room of
   version 2 is dropped from this control. **The reason it is reported and
   not gated, as recorded in the refinement: a gate on this control cannot
   pass a separable arm and an entangled arm in the same direction.** An
   entangled arm's ownership-only transplant is meant to move nothing, so it
   can never beat random subspaces; on the earlier re-run's first pass, which
   gated on it, arm C seed 0's read fit at 1.000 and was blocked only by this
   control (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 2,
   first pass, sections 6.2 and 7). Its job of catching a leaky site set is
   done by the whole-state floor and the no-transplant rule. **This reporting
   rule was clarified after the re-run of 2026-09-26, with the first pass's
   figures in hand, and is not called pre-stated here** (the check at
   `70be9fb`, section 1.3). *What the toy shows (MEASURED: the controls
   re-run at `821f154`, sections 2 and 4):* on arms T and M the
   ownership-only transplant sits above all twenty draws on every seed (arm M
   0.37 to 0.41 against random medians of 0.015 to 0.019); on arm C it sits
   below all twenty on seed 0 and among them on seeds 1 and 2; on arm F it
   sits among the draws on every seed, which is consistent with a piece that
   holds nothing, though arm F's verdict comes from its floor and not from
   this control.
4. **Positions before both twins' first own turns. Holds (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 2, which
   reverses that morning's ruling on version 3's decision 16).**
   - **What is run.** At the layers of the arm's nominated site set, the
     donor twin's whole state is transplanted into the recipient at every
     position before the earlier of the two twins' first own turns. A twin's
     first own turn is the first position at which its acting channel is on.
     The control takes the site set's layers and not its positions.
   - **The pass line: the transplant changes nothing.** The model's outputs
     at its two action positions (its scores over the vocabulary there, which
     is what the null transplant has always compared) with the transplant are
     compared with the same outputs without it, on every pair, and must be
     bit-identical. "Outputs" here and wherever this control is described
     means those, and not the outputs at every position (the check of the
     short run, finding 7). Reported
     beside it: the share of trials landing on the donor's value with the
     transplant, the no-transplant share, and the number of trials whose
     action changed. **A failure withholds the reading for that arm and
     seed.**
   - **What this control is, said plainly: a known-answer test of the pairing
     and of the code, like the null transplant.** The twins are the same
     text. They differ only in which turns carry the acting channel. The
     models read left to right. So until one twin's channel first comes on,
     both have had exactly the same input, their internal states are the same
     numbers, and transplanting one into the other puts back what was already
     there. **It cannot fail on a correctly built model with correctly built
     pairs, and a pass says nothing about any model.** It is right that a
     failure withholds a reading, because a failure means the pairing, the
     left-to-right property or the transplant code is broken. It is not
     evidence that a model does not yet know its identity at those positions,
     and no report of this experiment describes it that way.
   - **What is withdrawn.** Version 3 defined this control on the positions
     before the *recipient's* first own turn, found it above the
     no-transplant rate on arms C and F, and explained that by saying those
     arms "receive the ownership signal by other routes at those sites".
     **That sentence is withdrawn** (ruling 2, item 3). The control as then
     defined was transplanting at positions where identity was already known,
     in the donor: in 407 of 800 matched pairs (0.5088) the donor twin's
     first own turn comes before the recipient's. Under that definition the
     re-run found the control above the no-transplant rate by 0.065 to 0.10
     on six of the twelve toy models and by 0.005 or less on the other six
     (MEASURED: the controls re-run at `821f154`, section 6).
   - **The evidence the redefinition rests on.** The diagnostic that
     suggested it was written after the re-run's output was seen and was not
     pre-stated (`src/posthoc_control4.py`). The ruling said that if the
     check of the re-run found the diagnostic wrong, the ruling returned to
     John. The check did not find it wrong. With separately written code that
     shares only the episode generator, the model loader and the model's
     forward pass, it found on all twelve models: the twins' inputs and
     states are identical before both first own turns, at every layer; the
     outputs with the redefined transplant are bit-identical to the outputs
     without it; and all of the old definition's excess is in the pairs where
     the donor's first own turn comes first (MEASURED: the check at
     `e184a6e`, section 5, from its script `independent_control4.py`).
   - **The pre-stated run the ruling required** (method and code committed
     before output, by a session that did not write the diagnostic): the
     redefined control **holds on all twelve toy models**. The outputs are
     bit-identical; the donor-value share equals the no-transplant share on
     every line; no trial's action changes; a null transplant at the same
     positions is bit-identical; and across the 800 pairs the control
     transplants at between 1 and 21 positions per pair, about 5 on average,
     never none, so it is never an empty test (MEASURED, **checked: the check of the short run at `53c8100`**: `docs/2026-10-03-short-prestated-run.md` at
     `853988f`, section 3, from `out-short-prestated-run/part_a.json`). The
     method said in advance that this was not a blind prediction: the session
     had already observed it with different code while checking the re-run.
     **The check of that run** ran it again from the committed code and got
     byte-identical output files, found the same thing with separately
     written code at all five running states of every model, and showed the
     test is not empty: with random noise added to the donor's state at the
     same positions the outputs change on all twelve models, so the
     transplant does write there, and it changes nothing in the real control
     because what it writes is what was already there (findings 4, 8 and 9).
     **One limit the check records on the word "pre-stated"** (finding 3):
     the record shows that the method and code were committed and pushed
     before the output, 2 minutes 39 seconds apart; no committed file can
     show that the script was never run before the method was committed.
     Little turns on it, because this control cannot fail on correctly built
     pairs whenever it is run.

   The alternative that was put to John and not taken: redefining the
   positions and keeping the control reported only.
5. **Fresh marker and content combinations**, per section 7.1. By construction.
6. **Who is acting, versus which value. Reported, on the relaxed set.** The
   discriminating control. Trials are split into pairs whose donor identity
   dictates *the same* value as the recipient's and pairs where it dictates a
   *different* value. A transplant that has moved who is acting changes the
   action in the second group and not the first; a transplant that has
   smuggled a value across changes the action in both. **The first cell is
   empty by construction on the distinctness-preserving grammar** (0 of
   4,000 trials: MEASURED, `docs/2026-09-21-successor-measure-rehearsal.md`,
   section 5, from `out/denominator_control6.json`; the Gate C review of
   version 1, finding RT-173; failure 3 of `docs/known-failure-modes.md`), so
   control 6 runs on the **separately generated relaxed set** of section 4.2,
   in which one item per episode has two agents sharing a value. On that set
   both cells have trials: 81 same-value and 719 different-value trials of 800
   per arm and seed on the toy, on all four arms (MEASURED: the `controls`
   fields of `out-repairs/measure_base_*.json` at `882f252`; section 17,
   failure 3, prints them). Both cells are pre-stated and both are reported,
   with the one-in-four reference for a solver that cannot tell which agent it
   is restated for the relaxed set, where it rises (on the toy, from 0.2467 to
   0.3095 on exactly the trials the relaxation adds; the 2026-09-21 rehearsal,
   section 5). Pre-stated expectation: the separable arm moves nothing in the
   same-value cell and everything in the different-value cell; an entangled
   arm is expected to move the same-value cell too, and that is reported as
   the caveat it is (weakness W11): on those arms the whole-state transplant
   carries something besides identity. *What the toy shows under the
   registered rules (MEASURED: the controls re-run at `821f154`, sections 2
   and 4):* arm T moves 0.0000 of the same-value cell and 1.0000 of the
   different-value cell on every seed; the same-value cell moves on arm C
   (0.5062, 0.6296 and 0.5679), on arm M (0.2222, 0.2716 and 0.3210) and, for
   description, on arm F (0.7284, 0.6790 and 0.6296); the different-value
   cell moves in 0.82 to 0.95 of trials on those three arms.
7. **Null transplant. Holds.** Transplant the recipient's own state into
   itself. Every logit must be bit-identical. This is the known-answer test
   for the transplanting code and it runs before any result is read. **On the
   toy it holds at every place it was run, fifteen different places:** the
   twelve primary site sets (arm F's three being the described ones) and the
   three stricter-row site sets that differ from their primary, which are arm
   T's (MEASURED: the controls re-run at `821f154`, section 4; the check at
   `e184a6e`, section 3, which corrects the re-run's own count: its "twelve,
   nine and three" names fifteen different places, not twenty-four). That
   closes the citation gap version 3 recorded, that the null transplant had
   not been run at the site sets that changed. It is run again at the
   registered site sets before any registered reading.

**The ordinary competing solver has not yet been measured under the piece
rule, and it will be before the registration review opens (ruled 2026-10-03,
late evening, ruling 7).** The controls re-run did not load the
ownership-blind solver's three models, and read the gate from the committed
file (the check at `e184a6e`, section 4, item 8). The figures section 8.1
quotes for that solver and for the name-only solver are their accuracies on
the two conditions, from `out-repairs/gate_base.json` at `882f252`, taken
before the piece rule existed. Those are accuracies on the task and do not
pass through the nomination, so the piece rule does not change them; but
neither solver has been put through the nomination and the transplants under
the rule as now registered. **What is owed:** the ownership-blind solver's
three committed toy models, put through the nomination and the reading as
section 7.2 now states them, on the laptop at $0, with the method committed
before the output, by a session other than the one that drafted this
version, and checked like any other run. **The expected result, stated now:
no verdict**, because a solver with no acting channel should have no read of
its own marker word that reaches four fifths. **This version quotes no figure
for it. When the run is done its result is written in here, and until then
this text does not go to the registration review.** The alternative that was
put and not taken: state in the registration that it was not measured, and
leave it to the reviewer. In the registered experiment both solvers are
scored on both conditions on the registered episodes, as section 8.1 says.

### 7.4 What is frozen, and when

Committed to git, with the commit hash recorded in the registration file,
**before a single fresh episode is evaluated**:

- the label (which marker word), in code and in text, as the one registered
  read; the three route (b) candidates recorded as exploratory fits and not
  frozen as reads;
- **the fit floor: four fifths of held-out development episodes, on the piece
  that is transplanted and on the piece only, at the action position, stated
  as a count; the device the registered fit is computed on, the laptop's
  processor, and its number format (section 7.2, item 1);
  and the permutation null beside it**;
- **the piece's accuracy at the other positions of its site, both ways (each
  position, and the average over them), as reported figures with no pass
  line, and the method by which each is computed** (section 7.2, item 3);
- the site-set rule of section 7.2, the printed list it produces for the
  registered architecture (section 18), its two exclusions (all positions;
  layer 0 away from the action position set, as removal from the family), and
  the count of comparisons;
- the stricter layer-0 variant, as the sensitivity row;
- the rank caps (1, 2, 4, 8) and the registered cap (8);
- the nominated subspace and its size, per arm and seed;
- the whole-state layer set, per arm and seed, under the one registered
  reading of "the smallest that clears it", with the repairs-style sensitivity
  row named;
- the transplanting operation, as code, with its self-tests;
- all seven controls, and which hold: **control 7; control 1 on arm T;
  control 4 as redefined, on the positions before both twins' first own
  turns, with its pass line that the outputs are bit-identical**; the
  twenty-draw null of control 3 and its reported statistics; **control 2 as a
  reported description with no pass line, against twenty random pieces, with
  the statement that it never ran at toy scale**; the pre-stated cells, the relaxed set for control 6 and
  its generating seed;
- **that the code withholds a reading when a control that holds fails**
  (section 6.4, item 5);
- the whole-state floor rule (four fifths, on the chance-corrected scale,
  applied on development episodes at nomination and again on fresh episodes
  at the reading) and the no-verdict rules of section 6.4, including the
  no-transplant formula, its 0.018 room and the detection margin printed at
  the bar;
- the separation bar between R1 and R2 (0.5);
- **the five registered outcome terms of section 3, and what a no verdict on
  each arm maps to**;
- the gates of section 8: the own-directed bar on arms T, C and M, the
  learn-both bar on arm F, and the ownership-lesion rule with its two-of-three
  clause;
- the uncertainty method (section 9, 1g) and the seed count (three);
- **the numbers of episodes at the registered size, which are the toy's
  (ruled 2026-10-03, late evening, ruling 4): 600 development episodes with
  the last 180 held out for every fit, so the floor is 144 of 180; 800 fresh
  matched pairs; 800 pairs on the relaxed set; 3,000 held-out episodes for
  the gates, so the bar is 790; 200 shuffles for the permutation null**;
- **(reconciled 2026-10-03, night) the band that sampling alone puts around
  every count taken against the four-fifths floor, printed beside it; the
  committed file that pins the library versions; and the separation as the
  lowest of arm C's readings minus the highest of arm T's**
  (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`);
- **the rule for an arm whose seeds disagree: two of three, the third
  reported** (section 3);
- the reporting table's columns (section 7.5), including the rider;
- the predictions: arm T near zero; arm C high; arm M between 0.3 and 0.7 and
  within 0.10 of its true-slot reading on the same fresh episodes; arm F
  unknown and not predicted, and possibly no verdict.

Nothing on that list may be changed afterwards. If something on it turns out
to be wrong, the registered output is reported as it stands and the correction
is a separate, dated note beside it, the programme's existing practice, and
the process correction the outside review asked for: an immutable registration
is not an immutable scientific conclusion, but the two are kept visibly apart.

### 7.5 The reporting table

One row per arm and seed, with these columns, in this order, so that every
number a no-verdict rule or a caveat depends on is beside the reading it
bears on:

===== END OF RECORD 4, part 6 =====

