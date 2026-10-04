# The ordinary competing solver under the rules as now ruled: method, committed before any output

*Written 2026-10-03 (Pacific) by a Claude Code session, on branch
`w2b-job1-competing-solver-run`, cut from the main line at `41b0bd3`.
**Committed and pushed before the code it describes is run on any committed
model.** The commit that carries this file and the code carries no output;
the findings, with the command and what it printed, are a later commit.
Laptop only, on the processor. Nothing is rented, nothing is trained and
nothing is spent: $0.*

*Written under the workspace plain-language rule. This is a rehearsal record
on three particular trained toy models, not a result about the scientific
question, and no number it produces is a bar for anything.*

**What this session opened and what it did not.** Committed files only, at
`41b0bd3`: the two records of the seven-question ruling's outcome that the
brief names (`docs/rulings/2026-10-03-version-4-questions-rulings.md` and
`docs/rulings/2026-10-03-seven-questions-reconciliation.md`); the controls
re-run's method, code and findings; the short pre-stated run's code and
findings and the head of its method; the rehearsal code (`training.py`,
`arms.py`, `repairs.py`, `transplant.py`, and the parts of `grammar.py`,
`rehearse.py` and `rerun_v3.py` those call); the list of model fingerprints
and the note beside it; the competing solver's rows of
`out-repairs/gate_base.json` and one of its training records; and the
passages of version 4 of the proposal that mention the competing solver or
the other-agent control (found by search; the document was not read through).
It did not open the other record of the ruling
(`2026-10-03-proposal-v4-seven-questions-rulings.md`), any ruling packet, or
any chat or transcript of another session. It wrote none of the files above.

## 1. Why this run exists

John ruled on 2026-10-03, late evening (ruling 7 of
`docs/rulings/2026-10-03-version-4-questions-rulings.md`), that the three
committed toy models trained with no acting channel are put through the
nomination and the reading as now ruled, before the registration review. The
acting channel is the signal that tells a model "this turn is yours". These
three models are the *ordinary competing solver*: a system with none of the
structure the measure claims to detect. The measure should return nothing on
it. Until now it has been scored on the task only, never put through the
measurement.

The template is the controls re-run: its method
`docs/controls-rerun-method-2026-10-03.md`, its code
`experiments/rehearsal-successor-measure/src/rerun_controls.py`, its findings
`docs/2026-10-03-controls-rerun.md`. "The re-run" below means that run.

## 2. What this session already knows, said before it runs anything

**Already seen, in committed files:**

- The solver's accuracy on the task, taken on the laptop's graphics chip on
  2026-09-25 with the acting channel removed
  (`out-repairs/gate_base.json`): 702, 715 and 702 of 3,000 right on the
  own-directed condition (seeds 0, 1, 2), and 712, 726 and 650 on the
  named-other condition. The bar is 790. It fails on every seed.
- Every figure in the re-run's findings and the short pre-stated run's
  findings, for the other twelve models. In particular the free model's best
  piece is right on at most 34 of 180.
- **A test of this code on a model with untrained, freshly drawn weights**
  (`competing_solver_run.py --smoke`, which loads no committed model and
  writes no file). It ran end to end in 238 seconds. On those untrained
  weights no site set cleared the whole-state floor under either reading
  below, the read was right on 13 to 43 of 180 with the channel left on, and
  the twins' states were identical with the channel removed. Those are
  figures about random weights and say nothing about the three trained
  models, but this session has seen them.

**Not seen:** any read, nomination, transplant or control figure for any of
the three competing-solver models. No committed file holds one; the re-run
did not load them.

## 3. This session's reading of the ruled terms, for John to overturn

The ruling asks the method to state what "the model's own turn" and its twin
pairing mean for a solver with no acting channel.

**How the solver was built and scored (from the code).** It has the free
model's architecture (`repairs.build_for("blind")` builds arm F), including
the one vector the acting channel adds to the input. It was trained by
`training.train_arm(..., blind=True)`, which sets the acting channel to zero
on every training episode, and scored by `training.accuracy(..., blind=True)`,
which does the same. So the vector for the channel exists in the file and was
never used: no training step ever passed a signal through it.

**Reading A, this session's primary reading: the channel is removed, as it
was in training and scoring.** *(This session's reading.)*

- **The model's own turn** is a fact about the episode, not something the
  solver is told. The episode generator still decides which of the four
  agents the model is, and that decides the right answer and the label. The
  positions the rule transplants at ("from the model's first own turn to the
  action", and so on) are taken from the episode's true acting channel, the
  same positions as for every other model.
- **The twin pairing** is the same matched pairs as for every other model
  (same seeds). The two twins of a pair have the same text and differ only in
  the acting channel. With the channel removed, **the solver is given the
  same input for both twins**. The donor's states are then the recipient's
  states, and every transplant puts back what was already there.
- **The read** is a straight-line read of the model's own marker word (the
  label ruled on 2026-09-23), at the own-directed action position, one per
  layer. The label comes from the episode; the solver's input has no trace of
  it beyond what the text allows by elimination.

**Reading B, for description: the channel is left on in the solver's input.**
*(This session's addition.)* A registered procedure handed a model file would
feed it the acting channel like any other model. Under this reading the
unused, untrained vector is added to the input at the model's own turns, the
twins get slightly different inputs, and the transplants do move something.
This is the less tidy case and the more informative one: under reading A the
"no verdict" follows from the pairing alone, and under reading B it has to
come from the model. Reading B is run in full and reported beside reading A.

**Which of the two the registration should cite is John's.** Stop B2 below
applies to both.

**The read is not a committed file for this solver** (the repairs fitted
reads for the other four kinds of model only). It is fitted here, as the
registered rule says: on the 600 development episodes, the first 420 for
fitting and the last 180 held out, by the same call the repairs used
(scikit-learn's logistic regression, 3,000 iterations at most, C = 1.0). The
fitted coefficients are saved in the output folder, then applied unchanged to
fresh episodes. One read is fitted per reading, since the states differ.

## 4. The rules, as run

Everything is the re-run's section 3, with the differences forced by
section 3 above. The rule that chooses (`rerun_controls.pick`), the family,
the floors and the function that counts a read's held-out accuracy are
imported from the re-run's code and not copied.

1. **Models.** `ckpt_blind_base_seed{0,1,2}.pt` under
   `experiments/rehearsal-successor-measure/out-repairs/models/`. Each file's
   fingerprint is checked against `SHA256SUMS` in that folder before any
   model is loaded. A mismatch stops the run (stop B1).
2. **Episodes.** Development: 600 matched pairs, seed 4242, pool `dev`; the
   last 180 held out for every accuracy of a read. Fresh: 800 pairs, seed
   777, pool `fresh`. The gate: 3,000 development episodes, seed 99. The
   re-run's seeds.
3. **The read.** Fitted here (section 3).
4. **The family.** The re-run's 45 site sets at four sizes, 180 comparisons.
5. **The whole-state floor,** on development episodes: four fifths of the
   model's accuracy on the chance-corrected scale (`repairs.floor_check`).
6. **The layer set:** per position set, the fewest layers that clear the
   floor, ties to the earliest.
7. **The piece rule (rulings 1 and 2).** A size may be chosen only if its
   piece is itself right on at least 144 of 180, at the action position, at
   the worst layer of its site set. Applied after the layers are chosen. The
   whole read's count is printed beside it and is not a second condition.
8. **The choice,** the stricter row (no site set containing layer 0), and
   the two kinds of no verdict at nomination: as the re-run's rules 8 to 10.
9. **The reading, on fresh episodes,** with the whole-state floor applied
   again. Computed only if the rule nominates a site set.
10. **The gate on learning** is recomputed on the processor under each
    reading and printed. **The nomination is run whatever the gate says**,
    because the ruling asks for it; in the registered experiment a model that
    fails the gate is not read at all.
11. **The null transplant** (the recipient's own states put back) is run at
    all 45 site sets on fresh episodes under each reading.

**Not run:** the re-run's controls 1, 2, 3, 4 and 6, the rider and the
true-slot reference. The ruling and the brief ask for the nomination and the
reading; if no site set is nominated there is nothing to run those at.

## 5. What is reported for each seed, under each reading

- The whole read's count and each piece's count of 180, at every layer, and
  the band sampling alone puts around the best piece's count (ruling 4).
- How many of the 45 site sets clear the whole-state floor, on development
  and on fresh episodes.
- The nomination's status, the stricter row's, and the final status.
- The gate, the null transplant, whether the twins' states are identical, and
  the no-transplant rate beside its formula.
- **Labelled DESCRIPTION ONLY: what the arithmetic would have returned.** The
  number is (whole − piece) ÷ (whole − untouched). With no floor applied it is
  printed for all 180 comparisons on fresh episodes as: how many are a
  division by zero, and the smallest, middle and largest of the rest. If site
  sets clear the floor and only the piece rule blocks, the figure at the site
  the rule would choose with the piece rule switched off is printed too, in
  parentheses, as the re-run did for the free model. **None of these is a
  reading.**

## 6. What is expected, stated before the run

| Quantity | Reading A, channel removed | Reading B, channel left on |
|---|---|---|
| The gate | Close to the committed 702, 715, 702 and 712, 726, 650 (seen; the processor may differ by a few episodes). Fails | Not seen. Expected under 790 on both conditions; the untrained vector may shift it either way |
| The twins' states | **Identical, by construction** | Differ slightly |
| Site sets clearing the whole-state floor | **None of 45, on development or fresh, by construction:** the transplant changes nothing, so "whole" equals "untouched" exactly, and the floor needs it to exceed "untouched" | Expected none. Less sure: the solver's accuracy and its untouched rate are both near one in four, so the room the floor asks for is close to zero and a transplant that shifts a handful of episodes the right way could clear it by chance. This session puts that at perhaps one in six per seed |
| The read, whole and pieces | Far below 144 at every layer and size. A guess at the range: 10 to 65 of 180 (one in twelve marker words is 15; picking one of the four in the episode is 45) | Far below 144. A guess: 10 to 70. **A piece at 144 or more anywhere would be a real surprise** |
| The nomination | No verdict: no site set clears the whole-state floor. Every seed | No verdict on every seed, of one kind or the other |
| The arithmetic, description only | 0 ÷ 0 at all 180 comparisons | Mostly small numbers over small numbers; not predicted, and not meaningful |
| The null transplant | Bit-identical at all 45 | Bit-identical at all 45 |
| The no-transplant rate against (1 − accuracy) ÷ 7 | **Expected outside the 0.018 allowance:** about 0.25 against about 0.11. The formula assumes wrong answers spread evenly over the seven other values; this solver's wrong answers should fall on the other agents' values, one of which is the donor's. On the other models that rule holds a reading back, so this would be a second, independent reason for no verdict | The same |

**The expected result, as the ruling states it: no verdict on every seed.**
Under reading A this session's confidence is as near certain as code allows,
because it follows from the pairing. That also means reading A, on its own,
tests the pairing and the code more than it tests the solver. Under reading B
it is a prediction that could fail.

## 7. Stops

- **B1.** A model file's fingerprint does not match the committed list. The
  run stops before loading anything.
- **B2.** **A reading is returned on any seed, under either reading.** It is
  said at the top of the findings, nothing further is done on this job, and
  it goes to John before anything else moves. A site set nominated on
  development episodes that then misses the floor on fresh ones is not a
  reading, but it is also said at the top.
- **B3.** Under reading A the twins' inputs or states are not identical. That
  is a fault in this code or in this session's account of how the solver was
  built; no figure from the run is reported as a finding.
- **B4.** The null transplant is not bit-identical somewhere. A fault in the
  transplant code; it goes to John.

The code is not changed after the commit that carries this file. If a figure
is surprising, the surprise is written down and nothing is changed to remove
it.

## 8. What is committed, and when

1. This file and
   `experiments/rehearsal-successor-measure/src/competing_solver_run.py`,
   with no output (this commit, pushed).
2. The outputs under
   `experiments/rehearsal-successor-measure/out-competing-solver-run/` and
   the findings `docs/2026-10-03-competing-solver-run.md`, with the command
   and what it printed.
3. A check by a session that did not write or run this, which the ruling
   requires before the registration review.

## 9. What this run does not do

It does not edit the proposal, any ruling, registered text or protocol text,
`STATUS.md` or `data/project.toml`. It trains no model. It does not measure
the second competing solver, the one that reads only the name: that one is
computed from the episodes and has no states to transplant
(`training.name_only_solver`). It is one run on three trained models; its
figures are properties of those models.
