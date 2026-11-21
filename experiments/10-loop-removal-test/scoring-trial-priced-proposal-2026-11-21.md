# The scoring trial: priced proposal

*Written 2026-11-21. The trial is set out in section 15 of `battery-authoring-spec.md`. John chose to try the
answer-only instruction first ("Answer-only instruction"), after the step-4a findings showed near-chance
accuracy when the answer is forced as the reply's first token. Nothing is rented until John gives his go.*

## What the trial asks

Does adding "Answer with the single word or number only." to each question lift the forced answers far enough
for the test to go on? The instruction is tried in two places: at the end, after the final question, and at the
start, before the rule. The unchanged pilot is run alongside, so that all three sets are measured on the same
machine in the same run.

## What is ready, and checked for free

- **The generator** (`src/build.py`) has an `--instruction` option. With it off, the pilot it makes is byte for
  byte the committed one, all six files (commit 8c9dcd0).
- **The two trial sets** are in `batteries/trial-instruction-end/` and `batteries/trial-instruction-start/`:
  120 pairs, 204 donor-only items, 40 chained lookups and 200 neutral items each, the same draws as the pilot.
- **The free checks pass on both sets.** The overlap check finds no problem. All 120 twin pairs are of equal
  length. The stand-in dose ratio stays between 0.993 and 1.0 for every rule kind.
- **The trial script** (`src/scoring_trial.py`) reuses step 4a's loading, hooks and scoring. A dry run on this
  Mac loaded all 280 items of each set and turned every candidate into a single token, with no error.

## What the run does

For each of the three sets it measures:
- accuracy at 1, 2 and 3 passes, by kind;
- the share of items that are right with a margin of at least 2.2 at three passes (the confidence filter);
- accuracy on chains of four to six steps at one pass and at three, and the difference between them.

The instruction works well enough to go on if all three of section 15's criteria hold for one placement:
- routine twins are right at least 80% of the time at three passes;
- at least half of the items pass the confidence filter;
- chains of four to six steps are right at least 50% of the time at three passes.

These are pilot figures that decide only whether the scoring works. No outcome of the test is read from them.

## The machine and the cost

- **The card.** The model needs about 49 GB at 16-bit, so an RTX 5090 (32 GB) cannot hold it. The proposal is
  the same card as step 4a: one RTX PRO 6000 (96 GB), RunPod secure cloud, $2.69 an hour.
- **The time.** In step 4a one pass over 280 items took 65 seconds. The trial does nine such passes (three sets,
  three pass settings), so about 11 minutes of work. Setting up took about 25 minutes in step 4a: installing
  the libraries, downloading the model and loading it. Allowing for that, about 40 minutes in all.
- **The expected cost** is about **$1.80**.
- **The proposed ceiling** is **$5**, which covers nearly two hours. RunPod's own stop-after setting would be
  set to 1 hour 45 minutes, so the machine cannot run past the ceiling.
- **Lessons from step 4a are already in the commands:** load at 16-bit, and the wait check that does not match
  its own command line.

## After the run

The findings are written up in plain words, the cost goes in the spending record, and the pod is deleted by
hand as soon as the results are copied back. If neither placement meets the criteria, the next option in the
step-4a findings, a fixed answer lead-in such as "The answer is", is designed and priced before anything else
is spent.
