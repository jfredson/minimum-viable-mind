# The controls re-run under the registered rules: method, committed before any output

*Written 2026-10-03 (Pacific) by a Claude Code session, on branch
`controls-rerun-2026-10-03`, cut from the main line at `56a5a86`. **Committed
before the code it describes is run.** The commit that carries this file and
the code carries no output; the findings, with every command and its output,
are a later commit. Laptop only, on the processor. Nothing is rented and
nothing is spent: $0. Nothing is trained: the twelve committed base-recipe
toy models are loaded and measured.*

*Written under the workspace plain-language rule. This is a rehearsal record,
not a result about the scientific question, and no number it produces is a
bar for anything.*

## 1. Why this run exists

John ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, pages 1 and 2):

- only transplanted pieces that themselves carry the label at four fifths may
  be chosen (the review's finding RT-230, option (b));
- the re-run of the rehearsal under the registered rules, with that rule in
  it, is a precondition of the registration review. It covers controls 1, 2,
  4 and 6 on the entangled, free and mixed models (arms C, F and M) at the
  site sets the rule nominates, and control 7, the null transplant, at every
  nominated site set.

"The proposal" below is `docs/successor-experiment-proposal-2026-09-26-v3.md`.
"The review" is
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`.

## 2. What this session already knows, said before it runs anything

This session wrote the review, the ruling packet and the ruling record. So
some of what this run will print is not new to it, and a prediction of those
figures is not a prediction.

**Already seen by this session** (the review's three output blocks): the
whole-read and piece accuracies of every arm and seed at the proposal's
nominated layers; arm C's fresh-episode reading at every size of piece
(seed 0: 1.0000, 1.0000, 1.0000, 1.0051 at 1, 2, 4 and 8 directions; seed 1:
1.0025, 1.0025, 0.9975, 0.9975; seed 2: 1.0000, 0.9949, 0.9974, 0.9897); arm
M's blind, oracle and route-formula readings at its nominated site set; the
whole-state floor's margins; and the development-episode ownership-only
shares at each arm's nominated site, as the committed re-run recorded them on
the laptop's graphics chip.

**Not seen by this session:** any figure for controls 1, 2, 4, 6 or 7 at any
site set, old or new; the rider; any figure for the named agent's read; any
nomination grid recomputed on the processor.

## 3. The rules, as run

Everything is the proposal's section 7.2 as ruled, with page 1's rule added.
Where this session had to choose how to turn a ruled sentence into code, the
choice is marked **(this session's reading)** and is John's to overturn.

1. **Models.** The twelve files `ckpt_{T,C,F,M}_base_seed{0,1,2}.pt` under
   `experiments/rehearsal-successor-measure/out-repairs/models/`. Each file's
   fingerprint is checked against `SHA256SUMS` in that folder before it is
   loaded. A mismatch stops the run (stop K1).
2. **Episodes.** Development: 600 matched pairs, seed 4242, pool `dev`; the
   last 180 are held out for every accuracy of a read. Fresh: 800 pairs, seed
   777, pool `fresh`. The relaxed set for control 6: 800 pairs, seed 778, pool
   `fresh`, with one shared value per episode. Control 2's donors: the fresh
   pairs with the named agent swapped, seed 781 (development: seed 4243).
   These are the seeds the earlier runs used.
3. **The read.** The committed coefficients in
   `out-repairs/reads_{arm}_base_seed{seed}.npz`: one read per layer at the
   action position, labelled with the model's own marker word (for control 2:
   the named agent's marker word, at the named-other action). They are not
   refitted. Their held-out accuracy is recomputed on the processor and
   printed as a count of 180 beside the committed figure (finding RT-232).
4. **The family.** Every contiguous set of the five running states at the four
   position sets (`action`, `action+ans`, `action+3`, `post-identity`), with
   every site set containing layer 0 removed at every position set other than
   `action`: 45 site sets, 180 comparisons at four sizes. Asserted in code.
5. **The whole-state floor,** on development episodes: four fifths of the
   arm's accuracy, on the chance-corrected scale (`repairs.floor_check`).
6. **The layer set:** per position set, the fewest layers that clear the
   floor, ties to the earliest.
7. **Page 1's rule (new).** For each remaining site set and each size (1, 2,
   4, 8 directions), **the piece's own accuracy** is the held-out accuracy of
   a fresh straight-line read given only the state's coordinates inside the
   piece, at the action position, on the same split; for a site set with more
   than one layer it is the worst layer's. **A size is a candidate only if
   its piece's accuracy is at least 144 of 180.** *(This session's reading:
   the piece's accuracy is taken at the action position, where the registered
   read is fitted, not at the other positions of a multi-position set; and the
   requirement is applied after the layer set is chosen, so it filters sizes
   and never changes which layers are used.)*
8. **The choice.** Among candidates, the highest development ownership-only
   share; ties to the smaller size, then the earlier position set.
9. **No verdict at nomination,** two kinds, printed with which: no site set
   clears the whole-state floor; or site sets clear and no size's piece
   reaches four fifths ("read failed its floor").
10. **The stricter row:** the same with every layer-0 site set removed.
11. **The reading,** on fresh episodes: the chance-corrected form, with the
    whole-state floor applied again on fresh episodes. A site set that cleared
    on development episodes and misses on fresh ones is printed as "no
    verdict: floor missed on fresh episodes" (finding RT-234).
12. **Where an arm and seed returns no verdict at nomination for want of a
    piece** (expected: arm F on every seed), its controls are still run, **at
    the site set and size the rule would choose with requirement 7 switched
    off**, and every such row is labelled "reported for description; no
    reading". *(This session's reading: the ruling asks for controls on arm F
    "at the site sets the rule nominates", and under page 1's rule it
    nominates none.)*

## 4. What is computed at each nominated site set, and what is expected

Stated before the run. "Holds" means a failure withholds the reading for that
arm and seed. "Reported" means it cannot. Expectations for the controls are
the proposal's (section 7.3); this session has seen no figure for them.

| Quantity | On which arms | Holds or reported | Expectation, stated now |
|---|---|---|---|
| Nomination under rule 7 | all | — | Arm T: layer 0, `action`, 8 directions. Arm M: layer 1, `post-identity`, 8 directions. Arm C: layers 2, 4 and 1; sizes 8, 8 and 4 (already inferred by this session from figures it has seen; the grid is recomputed on the processor and could differ by an episode). Arm F: no size reaches four fifths on any seed |
| Reading | all | — | Arm T 0.0000. Arm C 1.0051, 0.9975, 0.9974 if the nomination is as above (seen). Arm M 0.4886, 0.4860, 0.5449 (seen). Arm F none |
| Separation, arm C minus arm T | — | — | At least 0.5 on every seed |
| Control 1, the complement of the piece | all | **holds on arm T**; reported on C, F, M | Arm T: at most the no-transplant rate plus 0.018. Arm C: close to the whole-state share. Arms M and F: not predicted |
| Control 2, the named agent's representation | arm C and arm F seeds that clear the named-other bar (790 of 3,000 in the committed `out-v3-rules/gate.json`) | reported | Run by the identical procedure, rules 4 to 9, with the named agent's marker as the label and the named-other action as the anchor. Pass line: the own-directed action moves in no more trials than under a random piece of the same size at the same sites, plus 0.05. Expected to run on arm F seed 0 only; arm C and arm F seeds 1 and 2 return "no verdict: the arm has not learned the named-other condition"; arms T and M are not applicable by ruling. Its outcome on arm F seed 0 is not predicted |
| Control 3, twenty random pieces | all | reported | Arms T and M: the ownership-only share above all twenty. Arm C: at or below the draws. Arm F: among them |
| Control 4, a position before the identity can be known | all | reported | "Nothing happens" means the no-transplant rate. The proposal warns it did not come back at nothing on arms C and F at earlier sites. Not predicted |
| Control 6, same value against different value, on the relaxed set | all | reported | Arm T: the same-value cell moves in 0.000 of trials and the different-value cell in 1.000. Arms C and M: the same-value cell is expected to move too. Arm F: not predicted. Both cells must have trials |
| Control 7, the null transplant | all | **holds** | Every output bit-identical, at the primary site set, the stricter one, and arm F's described one |
| The true-slot reading | arms T and M | reported | Arm M's blind reading within 0.10 of it (seen at 8 directions: 0.0049, 0.0099, 0.0529) |
| The rider: the reading at arm T's site set and size | all | reported | Arms C and F: no verdict, the whole-state transplant at the no-transplant rate. Arm M: no verdict, a miss of the floor with about 0.4 moved |
| The no-transplant rate against (1 − accuracy) / 7 | all | **holds** (allowance 0.018) | Inside the allowance on every arm and seed |

## 5. Stops

- **K1.** A model file's fingerprint does not match the committed list. The
  run stops.
- **K2.** Control 7 fails anywhere. No reading is reported from this run; it
  goes to John as a fault in the transplant code.
- **K3.** Under rule 7 an arm T, C or M seed returns no verdict. It is
  reported as it stands: the toy would then no longer show a reading on that
  anchor on every seed, which is for John to rule on, not for this session to
  repair.
- **K4.** Arm F reads on any seed. Reported as it stands; it would contradict
  the committed record and wants a second look before anything is built on it.

Nothing is tuned after output. If a figure is surprising, the surprise is
written down and the code is not changed to remove it.

## 6. What is committed, and when

1. This file and `experiments/rehearsal-successor-measure/src/rerun_controls.py`,
   with no output (this commit).
2. The outputs under `experiments/rehearsal-successor-measure/out-controls-rerun/`
   and the findings `docs/2026-10-03-controls-rerun.md`, with the commands and
   what they printed.
3. A check by a session that did not write or run this: it re-runs the script
   from the committed code and compares.

## 7. What this run does not do

It does not edit the proposal, any ruling, registered text or protocol text.
It does not retrain anything, so it says nothing new about whether the
other-agent condition can be learned. It does not re-run the gate, which is
read from the committed `out-v3-rules/gate.json`. It is one run on one set of
trained models: figures for arms C, F and M are properties of those models,
not of the code (`docs/rulings/2026-09-23-range-and-direction-only.md`).
