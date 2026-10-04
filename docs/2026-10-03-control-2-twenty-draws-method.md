# The other-agent control compared with twenty random pieces: method, committed before any output

*Written 2026-10-03 (Pacific) by a Claude Code session, on branch
`w2b-job2-control-2-twenty-draws`, cut from the main line at `41b0bd3`.
**Committed and pushed before the code it describes is run on any committed
model.** The commit that carries this file and the code carries no output;
the findings, with the command and what it printed, are a later commit.
Laptop only, on the processor. Nothing is rented, nothing is trained and
nothing is spent: $0.*

*Written under the workspace plain-language rule.*

**THE RUN THIS FILE DESCRIBES IS A TEST THAT THE CODE RUNS END TO END. IT IS
NOT A RESULT.** Its figures are not a pass or a fail of anything, and nothing
may be concluded from them about any model.

**What this session opened and what it did not.** Committed files only, at
`41b0bd3`: `docs/rulings/2026-10-03-version-4-questions-rulings.md` and
`docs/rulings/2026-10-03-seven-questions-reconciliation.md`; the controls
re-run's method, code and findings; the short pre-stated run's code and
findings and the head of its method; the rehearsal code those call; and
section 7.3, item 2, of version 4 of the proposal with a few other passages
found by search. It did not open the other record of the ruling, any ruling
packet, or any chat or transcript of another session. It wrote none of those
files. It is the same session that wrote and ran the competing-solver run
(branch `w2b-job1-competing-solver-run`), which shares no code or figure with
this one.

## 1. Why this exists

The other-agent control (control 2) asks whether transplanting the piece of
the state that holds *the named agent* disturbs the model's *own-directed*
action. John ruled on 2026-10-03 that it is a reported description with no
pass line. The committed code (`rerun_controls.control2`) prints the real
figure beside one random piece. Ruling 5 of
`docs/rulings/2026-10-03-version-4-questions-rulings.md` says:

> Control 2 reports how often the own-directed action moves under the named
> agent's piece, beside twenty random pieces of the same size at the same
> sites: their middle value, their 95th percentile, and where the real figure
> sits among them. No pass line [...] The code changes accordingly, and the
> code test of 2026-10-03 is run once more on the changed code, labelled a
> test of the code and not a result.

The earlier code test is part (c) of the short pre-stated run
(`docs/2026-10-03-short-prestated-run.md`, section 5;
`src/short_prestated_run.py`, `part_c`).

## 2. What this session already knows, said before it runs anything

**Already seen, in committed files:** what the earlier code test returned on
the free model's seed 0 with the floor switched off. Site set: layer 1, the
action position and the three before it, 8 directions (piece right on 92 of
180, whole read on 95). Own-directed action moved in 0.0012 of trials; under
the one random piece 0.0063; named-other action moved in 0.0962. Also the
named agent's read on that model at every layer and size (the re-run's
findings, section 5).

**Also seen: a test of the new code on a model with untrained, freshly drawn
weights and a made-up piece** (`control2_twenty_draws.py --smoke`, which
loads no committed model or read and writes no file). It ran in 9 seconds and
every share was 0.0000, as expected of a model whose action a small
transplant does not move.

**Not seen:** how often the free model's own-directed action moves under any
of the twenty random pieces.

## 3. What changes, and what does not

The change is in a new file,
`experiments/rehearsal-successor-measure/src/control2_twenty_draws.py`. No
committed script is edited.

- **Unchanged, and imported from the re-run's code:** who the control applies
  to and its two early exits (not applicable on the separable and mixed
  models; no verdict where the named-other condition was not learned, below
  790 of 3,000); the nomination by the identical procedure with the named
  agent's marker word as the label and the named-other action as the anchor
  (`rerun_controls.accuracies`, `grid`, `pick`); the transplant from a twin
  that differs only in which agent is named; the real figure, which is the
  share of fresh trials whose own-directed action changes.
- **Changed:** the one random piece (drawn with its own seed, 100 plus the
  model's seed) is replaced by **twenty random pieces of the same size at the
  same layers, drawn by `rerun_v3.random_bases`**, the function the
  twenty-draw control (control 3) uses. Reported, as control 3 reports its
  twenty: the **middle value** (median), the **95th percentile**
  (`numpy.percentile(..., 95)`), and **how many of the twenty fall below,
  equal to and above the real figure**. The twenty shares are also printed.
- **Removed:** the "pass" or "fail" the old function attached, and its 0.05
  tolerance. The status of a model the control runs on is "reported; no pass
  line".
- **Kept beside it, for laying the two runs side by side:** the one random
  piece exactly as the earlier code drew it.

*(This session's readings, for John to overturn.)* "Drawn the way the
twenty-draw control already draws them" is taken literally: the same function
with the same seeds, so for a given model seed, size and set of layers these
are the same twenty pieces control 3 uses. "Where the real figure sits among
them" is reported as the three counts and not as a rank or a percentile of
its own.

## 4. The run

One call, on the free model's seed 0
(`out-repairs/models/ckpt_F_base_seed0.pt`, fingerprint checked first), **with
the piece's accuracy floor switched off for that call**, as the earlier code
test did. Without that the control returns no verdict on this model, because
the named agent's read misses its floor, and the changed lines would not run.
So the piece transplanted here is not known to carry the named agent at all.
The same episodes and seeds as before: development seed 4242, fresh seed 777,
the named-agent swaps at seeds 4243 and 781; the committed read of the named
agent; the gate from `out-v3-rules/gate.json`.

Outputs: `experiments/rehearsal-successor-measure/out-control-2-twenty-draws/`
(`code_test_NOT_A_RESULT.json`, `table.md`, `stdout.txt`).

## 5. What is expected, stated before the run

- **It runs end to end and returns the site set, the real figure, twenty
  shares and their summary.** This is the only thing the run is for.
- **The parts that are unchanged reproduce the earlier code test exactly:**
  the same site set, 0.0012 for the own-directed action, 0.0063 for the one
  random piece as the earlier code drew it, 0.0962 for the named-other
  action. These were seen beforehand, so this is a check that the path is the
  same and not a prediction.
- **The twenty.** Not predicted in any way that matters, and not interpreted.
  For the record, a guess: each between 0.000 and about 0.02, with more of
  them above the real figure than below it, since 0.0012 is one trial of 800.

## 6. Stops

- **D1.** The model file's fingerprint does not match the committed list. The
  run stops.
- **D2.** The call returns no verdict or raises an error. Then the code path
  has not run; the findings say so and the code is not patched in this run.
- **D3.** An unchanged figure differs from the earlier code test's. It is
  written down as it stands; it would mean the new function is not the old
  one with one change, and that goes in the findings ahead of anything else.

The code is not changed after the commit that carries this file. A surprising
figure is written down and nothing is changed to remove it.

## 7. What this does not do

It does not edit the proposal, any ruling, registered text or protocol text,
`STATUS.md`, `data/project.toml` or any committed script. It does not exercise
the control on a model whose read of the named agent clears its floor: no toy
model has one, and that remains true afterwards. It is owed a check by a
session that did not write it.
