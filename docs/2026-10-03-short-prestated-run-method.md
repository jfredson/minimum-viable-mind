# The short pre-stated run: method, committed before any output

*Written 2026-10-03 (Pacific) by a Claude Code checking session, on branch
`w2a-job2-short-prestated-run`, cut from the main line at `7c403b0`.
**Committed and pushed before the code it describes is run.** The commit that
carries this file and the code carries no output; the findings, with the
command and what it printed, are a later commit. Laptop only, on the
processor. Nothing is rented, nothing is trained and nothing is spent: $0.*

*Written under the workspace plain-language rule. This is a rehearsal record
on twelve particular trained toy models, not a result about the scientific
question, and no number it produces is a bar for anything.*

**What this session opened and what it did not.** It opened committed files
only: the two rulings files and two ruling packets of 2026-10-03, the controls
re-run's method, findings, code and outputs, the after-the-fact diagnostic
`src/posthoc_control4.py`, section 7.3 of the proposal, and the rehearsal code
those call. It did not open any chat or transcript of the session that wrote
them. It is not the session that wrote the diagnostic.

## 1. Why this run exists

John ruled on 2026-10-03 (`docs/rulings/2026-10-03-controls-rerun-rulings.md`)
that before the registration review there is one more short run, method first
and then output, by a session that did not write the diagnostic. It has three
parts:

- **(a)** the too-early-position control (control 4) as redefined: positions
  before **both** twins' first own turns. It is now a control that holds.
- **(b)** a new reported column: the chosen piece's accuracy at the other
  positions of its site, beside its accuracy at the action position. No pass
  line.
- **(c)** the other-agent control's (control 2's) code path, run once on the
  free model's seed 0 with the accuracy floor switched off. **This is a test
  that the code runs end to end. It is not a result.**

"The re-run" below is the controls re-run, `docs/2026-10-03-controls-rerun.md`,
with outputs in `experiments/rehearsal-successor-measure/out-controls-rerun/`.

## 2. What this session already knows, said before it runs anything

A prediction of a figure already seen is not a prediction, so this is what has
been seen.

- **For part (a), nearly everything.** This session checked the re-run before
  writing this file
  (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md`,
  on its own branch). As part of that check it read the diagnostic's printed
  output and wrote its own independent test of it, which found, on all twelve
  models at the layers the re-run nominated: the two twins' internal states
  are identical at every position before both first own turns, and the
  model's outputs with the transplant there are bit-identical to its outputs
  without it. **So the expectation in section 3 is a statement of what has
  already been observed once by this session with different code, not a
  blind prediction.** What this run adds is that the quantity is computed by
  code committed before its output, through the project's own transplant
  function.
- **For part (b):** the figures the rulings file quotes from the review (a
  one-direction piece on the entangled model's seed 2 right on 0.306 at the
  action position and 0.161 to 0.194 at the other positions; the mixed
  model's 8-direction piece right on 1.000 and 0.839 to 0.983). While
  checking those figures against the review for the third job, and before
  this file was committed, this session also saw the lines of the review's
  first output block that sit beside them (the review, lines 137 to 149): at
  the first token of the first own turn and on the average over the span
  (the review's average includes the action position; this run's does not),
  the free model's pieces were right on 0.117 and 0.128 (seed 0, 1
  direction), 0.394 and 0.083 (seed 1, 4 directions) and 0.806 and 0.122
  (seed 2, 8 directions), and the mixed model's on 0.839 to 0.967 and 0.883
  to 0.983. Those are the same sites and sizes this run uses for the free and
  mixed models, so **for those two models the first-own-turn figure is
  already seen, not predicted.** This session has not seen any figure for the
  pieces the re-run actually chose on the entangled model's seeds 1 and 2 (8
  directions and 4 directions) at any position other than the action
  position, nor any figure at the nine other positions this run reports.
- **For part (c):** the named agent's read on the free model's seed 0, as the
  re-run's findings print it (whole read at best 137 of 180; pieces at best
  139). Not seen: which site set the procedure picks with the floor off, or
  any figure for how often an action moves.

## 3. Part (a): the too-early-position control, as redefined

**What is run.** For each of the twelve models (arms T, C, F and M; seeds 0,
1 and 2):

1. The model file's fingerprint is checked against the committed list (the
   re-run's `check_sha`). A mismatch stops the run.
2. The 800 fresh matched pairs are the re-run's (seed 777, pool `fresh`).
3. The site set is the model's `primary` site set in
   `out-controls-rerun/summary.json`. For the free model, which returned no
   verdict, that is the site set the re-run used for description. Only the
   site set's **layers** matter here; the positions are the control's own.
4. The positions are every position before the earlier of the two twins'
   first own turns. A twin's first own turn is the first position at which
   its "this turn is yours" input signal is on.
5. The donor twin's whole state is transplanted into the recipient at those
   layers and positions, by the project's transplant function
   (`repairs.run`, which is `transplant.transplanted_logits`).
6. **The pass line (holds): the model's outputs with the transplant are
   bit-identical to its outputs without it**, on all 800 pairs, compared as
   the null transplant is compared (`torch.equal` on the output tensors).
7. Reported beside it: the share of trials landing on the donor's value with
   the transplant, and the same share with no transplant; the number of
   trials whose chosen action changed; the largest difference between any two
   output numbers.
8. Two supporting figures, reported, with no pass line of their own: whether
   the twins' states at those layers and positions are themselves identical;
   and whether a null transplant at the same positions (the recipient's own
   state into itself) is bit-identical, as a check on the transplant code at
   positions it has not been run at before.

**What is expected.** Bit-identical on all twelve; the two shares equal on
all twelve; zero trials changed; the twins' states identical. Reason (ARGUED):
twins are the same text and differ only in the "this turn is yours" signal;
the models read left to right; so before either twin's signal first comes on,
the two twins have had exactly the same input, their states must be the same,
and the transplant puts back what was already there. **This means the control
as redefined cannot fail on a correctly built model with correctly built
pairs. It is a known-answer test of the pairing and of the code, like the
null transplant, and says nothing about any particular model.** The ruling
packet said this (page 2: "it can only fail if the pairing is broken or if
something in the text gives identity away early"); it is repeated here so
that a pass is not read as more than it is.

**What a failure would mean, and the stop.** If any model's outputs are not
bit-identical, that is a fault in the pairing, the left-to-right property or
the transplant code. Stop S2 below.

## 4. Part (b): the chosen piece's accuracy at the other positions of its site

**What the ruling asks for.** "The chosen piece's accuracy at the other
positions of its site, beside its accuracy at the action position", for the
twelve toy models, with no pass line. The ruling does not say how an accuracy
"at the other positions" is computed. **Everything in this section about how
is this session's reading, and John's to overturn.**

**The reading chosen.**

1. **The piece** is what the re-run transplanted: the leading directions (1,
   2, 4 or 8, as chosen) of the committed read at the site's layer, built by
   the same function (`rehearse.basis_for` on the committed coefficients).
   The site set and size are each model's `primary` in
   `out-controls-rerun/summary.json`.
2. **An accuracy at a position** is computed exactly as the re-run computed it
   at the action position (its `correct_count`), with only the position
   changed: take the model's state at that position on the 600 development
   episodes (seed 4242), keep only its coordinates inside the piece, fit a
   fresh straight-line read of the model's own marker word on the first 420,
   and count how many of the last 180 it gets right. So it is a **fresh read
   fitted at that position**, not the action-position read carried over. The
   same count for the whole state at that position is printed beside it, so a
   low piece figure can be told apart from a position where the label is not
   in the state at all.
3. **Which positions, one figure per position.**
   - Site at the action position only: there are no other positions. Printed
     as "single position".
   - Action position and the token before it: the one position before.
   - Action position and the three before it: each of the three.
   - Everything from the model's first own turn to the action (a span whose
     length differs from episode to episode): the five tokens of the model's
     first own turn, and the five tokens of the action turn before the action
     position. Those ten are the positions that mean the same thing in every
     episode. **The positions between them are not reported one by one**,
     because position 20 in one episode is a different kind of token from
     position 20 in another.
4. **One summary figure per model as well:** the same count taken on the
   average of the state over all the other positions of the site (every
   position of the site except the action position). For a span this is the
   only figure that covers the middle positions.
5. For a site set with more than one layer, the worst layer's figure, as the
   re-run's rule 7 does. (No chosen site set has more than one.)
6. The action-position figure is recomputed and compared with the re-run's
   committed figure for the same piece. They should be equal.

**Readings not taken, so John can see the alternatives.** (i) Carrying the
action-position read to the other positions without refitting it: answers
"does the same read work elsewhere", a stricter question than "is the label
there inside the piece". (ii) One read pooled over every position of the
site. (iii) Only the first own turn and the span average, as the review's
script did.

**What is expected.** Reported only; none of this is a pass line.

- The action-position figures equal the re-run's on all twelve.
- The separable model (every seed) and the entangled model's seed 0: single
  position, nothing to report.
- At the first token of the model's first own turn, the **whole state** is
  right on nearly all 180 on every model with a span site, because that token
  is the model's own marker word.
- The mixed model (8 directions, span site): the piece is right on at least
  144 of 180 at most of the ten positions and on the average (the review's
  0.839 to 0.983, seen).
- The entangled model's seeds 1 and 2: **not seen, and this session's guess
  is that the piece falls below 144 of 180 at one or more of the other
  positions on each.** Confidence low.
- The free model: at the first token of its first own turn, about 21, 71 and
  145 of 180 on seeds 0, 1 and 2 (seen, above: that token is the marker word
  itself, so a large enough piece can pick it up). At the other positions and
  on the average: well under 144, as at the action position. Confidence
  moderate.

## 5. Part (c): the other-agent control's code path. NOT A RESULT

**What is run.** The re-run's own function for the other-agent control
(`rerun_controls.control2`), unchanged, called once for the free model's seed
0 with the same episodes the re-run gave it, and with the piece's accuracy
floor (144 of 180) set to zero for the length of that one call. Nothing else
is switched off: the whole-state floor on development episodes still applies,
and the site set and size are chosen by the same rule.

**What it is for.** To see that the code after the floor runs without error
and returns its figures: the site set chosen, how often the own-directed
action moves under the named agent's piece, how often under a random piece of
the same size, and how often the named-other action moves.

**What it is not.** The read of the named agent's marker on this model misses
its floor, so the piece being transplanted is not known to carry the named
agent. John withdrew the control's pass line on 2026-10-03. **The figures are
printed as evidence that the code ran, and are not a pass or a fail of
anything.** The pass-or-fail label the function attaches is dropped from the
output for that reason; the output file is named `part_c_NOT_A_RESULT.json`.

**What is expected.** It runs end to end and returns the four things above.
No figure is predicted.

## 6. Stops

- **S1.** A model file's fingerprint does not match the committed list. The
  run stops.
- **S2.** Part (a) is not bit-identical on any model. Under the ruling that
  withholds the reading for that arm and seed. Nothing is repaired or re-run;
  it is filed as it stands and goes to John as a fault in the pairing or the
  code.
- **S3.** In part (b) an action-position figure differs from the re-run's
  committed figure for the same piece. Filed as it stands; it would mean this
  script is not measuring the piece the re-run transplanted.
- **S4.** Part (c) returns no verdict even with the floor off (no site set
  clears the whole-state floor), or raises an error. Then the code path has
  still not run end to end; filed as it stands and goes to John.

**The code is not changed after this commit.** It has been checked only for
syntax; it has not been run. If it fails to run at all, the fix is made in a
separate commit that says exactly what was changed and why, before any output
is kept, and the findings say so. If a figure is surprising, the surprise is
written down and the code is not changed to remove it.

## 7. What is committed, and when

1. This file and `experiments/rehearsal-successor-measure/src/short_prestated_run.py`,
   with no output (this commit), pushed.
2. The outputs under `experiments/rehearsal-successor-measure/out-short-prestated-run/`
   and the findings `docs/2026-10-03-short-prestated-run.md`.

## 8. What this run does not do

It does not edit the proposal, any ruling, registered text or protocol text.
It trains no model. It does not re-run the controls re-run. It is one run on
one set of trained models. It was written and run by one session and is owed
the same check as everything else.
