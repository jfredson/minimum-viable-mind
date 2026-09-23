# Ruling 2026-09-23: what the two arms whose training does not repeat may be quoted as — range and direction only

*Recorded 2026-09-23 (Pacific). The session put the question and three possible
answers to John, and he chose one. Recorded as mixed authorship for that
reason: the choice is his, and none of the wording below — including the wording
of the question and of the three options — is his drafting. No compute was
launched and no money was spent under this ruling.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).*

*Filed as its own dated file, for the same reason the ruling made the same day
on the nomination label (`docs/rulings/2026-09-23-nomination-label.md`) was:
the earlier ruling file on verifying reviews and releasing money in two stages
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`) is a
different day and a different subject, and the standing permission to annotate
a recorded ruling file covers bookkeeping only. Adding a new ruled item to it
would be a different act. This is a new file and nothing in that one is
touched. This ruling is the companion to the nomination-label one: same day,
same evidence, different question.*

---

## What the question was

The measurement rehearsal trained three small models — it calls them arms — and
read each one on a scale that says how spread out a model's answer to "whose
value do I need here" is. Zero means the answer sits in a slot of its own; one
means it is stirred through everything.

On 2026-09-22 the whole rehearsal was re-run from the committed code, from
clean, in a scratch copy outside the repository. The arm built with the
ownership answer in a slot of its own — the separable arm — came back exactly.
The other two, the arm built to be entangled and the freely trained one, did
not. Their training does not give the same answer twice, on the same code, the
same seeds and the same laptop.

That left a question nobody had answered: if the code will not produce those
arms' numbers again, what may the registration say those arms read? The
question put to John, word for word:

> The entangled and free arms' readings change every time the code runs — up to
> 0.0506, against an uncertainty method that reports 0.019. What may the
> registration quote from those two arms?

## The measurement the ruling rests on

The record and the re-run, arm by arm and seed by seed, with the size of the
move:

| arm and seed | the record (2026-09-21) | the re-run (2026-09-22) | how far it moved |
|---|---|---|---|
| entangled, seed 0 | 0.8727 | 0.8565 | 0.0162 |
| entangled, seed 1 | 0.8848 | 0.8537 | 0.0311 |
| entangled, seed 2 | 0.8801 | 0.8295 | **0.0506** |
| free, seed 0 | 0.8863 | 0.8758 | 0.0105 |
| free, seed 1 | 0.8366 | 0.8376 | 0.0010 |
| free, seed 2 | 0.8499 | 0.8939 | **0.0440** |

Against that, the uncertainty method the rehearsal demonstrated reports a
spread of **0.019** on the entangled arm and **0.023** on the free one.

The method cannot see the movement in the table above, and the reason is in how
it is built. It has two candidate ways of putting an uncertainty on a reading,
and neither one trains a model twice:

- the first takes the three seeds' readings — one training run each — and
  measures how far apart they are;
- the second holds one trained model still and resamples its trials.

So the first spans three separate trainings but only one run of each, which
means it cannot tell a seed's own effect apart from the drift between runs; and
the second never retrains at all. Re-running the same seed is the one thing
that produces the movement in the table, and it is the one thing neither
candidate does. The method's own answer is not steady either: the first
candidate's spread, 0.019 and 0.023 in the record, came out at 0.0156 and
0.0102 in the re-run — one of them half what it was.

## 1. Ruled: range and direction only

**Ruled: from the entangled and freely trained arms the registration may quote
a range and a direction, and no decimal as a property of the code.** John's
choice, word for word:

> **Range and direction only** — The registration says the entangled arm reads
> in the range 0.83–0.89 and one seed of three clears the bar — both held
> across three runs — and quotes no decimal as a property of the code. Cheapest
> and most conservative. Cost: no point estimate, so no 'degree d' sentence for
> those arms.

What that permits, and what it is resting on:

- **The range.** Across the record and the re-run, the six readings of the two
  arms run from 0.8295 to 0.8939 — about 0.83 to 0.89. Every one of them sits
  at the entangled end of the scale, and the freely trained arm's readings fall
  inside the entangled arm's range rather than between the two anchors.
- **The direction.** On the learn-both check, each of the two arms clears its
  bar of 0.2630 on exactly one seed of three, in the record and in the re-run
  alike — **but it is a different seed each time**. In the record the entangled
  arm clears on seed 2 and the free arm on seed 1; in the re-run both clear on
  seed 0. So "one seed of three" is quotable and *which* seed is not.

## 2. The two answers turned down, and why that is part of the ruling

What John declined is part of what he decided, so both are on the record word
for word.

> **Mean across independent runs, with across-run spread** — Re-specify the
> uncertainty method to span independent trainings rather than seeds within one,
> then quote a mean with that spread. Scientifically standard and gives a real
> point estimate. Cost: every reading needs repeated trainings, and the seed
> count the method implies goes up rather than down.

> **Fix reproducibility first, then decide** — Find where the nondeterminism
> enters and eliminate it before ruling. Cost: unknown — it may be in
> accelerator kernels that cannot be made deterministic cheaply. And it does not
> solve the underlying problem: one exactly-reproducible run is still one draw
> from the space of trainings.

Neither is ruled out for later. What is ruled is that the registration does not
wait on either of them: it may be written now, on a range and a direction, and
it quotes no decimal from those two arms in the meantime.

## 3. The sharp corollary: the seed count rests on a spread that understates the variation

This part was already in the rehearsal findings, and the ruling makes it
explicit.

The arithmetic the findings demonstrate for how many seeds a reading needs is
the ordinary one: take the measured spread, take a coverage factor of two, and
ask how many runs it takes to pin the answer down to within a chosen tightness.
At the tightness the findings try — plus or minus 0.05 — that arithmetic implies
**one seed**, on both arms. (Checked from the rehearsal's own saved output:
`(2 × 0.0189 ÷ 0.05)² = 0.57` and `(2 × 0.0227 ÷ 0.05)² = 0.82`, each rounded
up to 1.)

So the method as demonstrated would license a single training run, on a spread
that leaves out a source of variation as large as the tightness it was aiming
for. The findings already hedge that entry — the toy arms are far more
repeatable than registered-size runs will be, so the number should not be
carried across without a discount. **That hedge is about scale. This is a
different source and an unmeasured one**, and it is present at toy scale
already.

## 4. The two numbers in the question are not on the same scale

Worth saying plainly, because a later session will otherwise check the
arithmetic and find that it does not quite work.

The 0.0506 is a move in the **reading**, which is a ratio sitting at about 0.88.
The 0.019 is a spread in the **difference between the two transplants**, which
is the quantity the reading is built from, and which sits at about 0.49. As
printed, the largest move is more than twice the reported spread; but they are a
ratio and a difference, and comparing them directly is not exact.

The comparison survives being done properly, which is why the ruling stands:

- Put on the reading's own scale, the record's three entangled readings differ
  from each other by about **0.006**, while the drift between runs reaches
  **0.0506** — roughly eight times as much.
- Converted the other way, a spread of 0.019 in the difference works out at
  roughly 0.035 in reading terms, still less than the largest drift of 0.0506.

Every way of putting the two on one scale points the same direction: the
variation the method does not measure is larger than the variation it does.
What changes is the multiple, not the conclusion.

## 5. The arm this does not touch

**The separable arm is unaffected, and so is the nomination ruling that rests
on it.** Its figures reproduced exactly, to every decimal place: it reads
0.0000 on all three seeds, with the whole-state transplant at 1.0000, the
ownership-only transplant at 1.0000 and the no-transplant rate at 0.0000.

That steadiness is not evidence that its training repeats — it does not. Two
runs of the same seed differ by up to 0.0003 in the saved weights on that arm,
against up to 0.51 on the entangled one. The separable arm is steady because it
answers its task perfectly, and a weight that moves in the fourth decimal place
cannot move a saturated answer.

So the nomination-label ruling made the same day
(`docs/rulings/2026-09-23-nomination-label.md`), every figure of which comes
from the separable arm, is not weakened by anything in this file.

---

## What this ruling does not settle

- **It does not choose which of the two forms of the reading's arithmetic gets
  registered.** The rehearsal reports both everywhere — the one the proposal
  writes and the one corrected for the floor the whole-state transplant has to
  clear — and adopts neither. This ruling adopts neither either.
- **It does not fix the uncertainty method, the seed count, or the separation
  bar.** All three are still on the rehearsal findings' list of numbers waiting
  on John, section 11, and all three stay there. The seed-count entry is now
  known to rest on a spread that understates the variation, which is a reason to
  treat it with more suspicion rather than an answer to it.
- **It does not make the training reproducible.** Nothing here finds where the
  drift enters, and nothing here removes it. What is ruled is what may be
  claimed given that the training is not reproducible.
- **No money was authorised and none was spent.** Nothing was launched. The
  short slice of rented machine time still has no fresh go from John — see the
  launcher-guard ruling (`docs/rulings/2026-09-22-launcher-argument-guard.md`),
  item 4, which is where the earlier go lapsed.

## What follows for the registration text

- **For the entangled and freely trained arms there is no "degree d"
  sentence.** Whatever the registration says about those two arms, it says as a
  range and a direction.
- **The separation bar, if it is set at all, is being set between one arm whose
  reading is exact and two whose readings are a range.** That is a different
  kind of comparison from the one the rehearsal's table makes it look like, and
  whoever writes the bar has to write it knowing that.
- Writing any of this into the proposal is work still owed, and under the
  pairing rule that text is owed a check by a session other than the one that
  writes it.

## Where the figures come from, and how they were checked

Every figure above was verified in this session against the sources rather than
carried over from the brief:

- The record's readings, the learn-both figures and its bar of 0.2630, the list
  of numbers waiting on John, and the hedge on the seed count:
  `docs/2026-09-21-successor-measure-rehearsal.md`, sections 4, 8 and 11.
- The re-run's readings, the weight differences of 0.0003 and 0.51, the
  separable arm reproducing exactly, and which seed cleared the bar in each run:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`.
- The spreads of 0.019 and 0.023, the trial-resampling figures of 0.0198 and
  0.0203, and the seed count of one at a tightness of 0.05, read out of the
  rehearsal's own saved output,
  `experiments/rehearsal-successor-measure/out/uncertainty.json`, and checked
  against the code that writes it,
  `experiments/rehearsal-successor-measure/src/rehearse.py`, which is where the
  two candidate methods are defined and where it is visible that neither
  retrains a model.
- The six moves in the table above were computed by subtraction from the two
  documents and match the figures the question was put with, exactly.

**One caution on the phrase "held across three runs" in the option John chose.**
Two full runs of all three seeds exist — the record and the re-run — and the
range and the direction hold across both. The third run was a single-seed check:
the three arms were trained once more at seed 0 only, and what it reports is the
learn-both accuracies, not the readings. The re-run document states that the
range and the direction held across all three runs; its tables show the third
run's learn-both figures and not a third reading. So the claim rests firmly on
two full runs and on the third run's own account of itself.

## Recorded elsewhere

- `docs/2026-09-21-successor-measure-rehearsal.md`: a note added at the head of
  section 4 in the same commit as this file, saying what may now be quoted from
  those two arms. The findings are a dated record, so that is an addition and
  nothing in them is rewritten.
