# Amendment to the cue-detector instrument: both arms drawn the same way

**Dated 2026-09-15. Ruled by John the same day.** This amends a
registered instrument, the RT-08 cue detector of `cue_detector.py`, and
so is itself a registered amendment. It changes how the detector draws
its two comparison arms. It changes no bound, no classifier, no episode
count, and no positive control.

## Say the trigger first

**This change was prompted by a grammar failing the old detector.** The
A3 Candidate A grammar with two of four agents revising failed cue runs
(i) and (ii) at about 0.53 and 0.54 against an equivalence bound of
[0.45, 0.55]. Investigating that failure is what surfaced the
inconsistency described below.

Recording the trigger is not a formality. Changing an instrument after it
fails your design is the exact move registration exists to prevent, and a
reader is entitled to weigh that. The case for the change has to stand on
the instrument being wrong, not on the grammar being inconvenient, and
the two ways this document tries to earn that are: the justification is a
property registered long before this grammar existed, and every verdict
from here on reports both numbers so the override is visible rather than
silent.

## What is wrong with the instrument

The detector builds one balanced pair per episode: one turn belonging to
the model, one turn belonging to somebody else. **The two arms are drawn
by different rules.**

- The model's arm is drawn **agent-first**: there is one such agent, and
  one of its turns is picked.
- The comparison arm is drawn **turn-first**: every turn of all three
  other agents goes into a pool and one is picked from it.

A turn-first draw is size-biased. An agent that speaks more contributes
more turns to the pool and is therefore picked more often. An agent-first
draw carries no such weighting. So whenever agents differ in how much
they speak, the two arms are not samples of the same kind of thing, and
the detector is comparing two sampling schemes rather than comparing the
model against the others.

The detector's null is **exchangeability**: relabel which agent is the
model's and the distribution of the episode is unchanged. That property
was registered with the design and holds for every grammar here. A
detector whose null is exchangeability has to draw both arms the same
way, or the null it is testing is not the null it states.

**Measured on the current grammar**, where revisers take three turns and
non-revisers take two:

| quantity | value |
|---|---|
| share of the model's sampled turns whose agent has three turns | 0.4992 |
| same, comparison turn pooled over the other three agents | 0.5839 |
| same, comparison agent drawn uniformly first | 0.5021 |

Turn count is balanced across all turns, 0.596 against 0.601. The 0.5839
is produced by the sampler, not by the data.

## Why the thing it flags is not a cue

Two further reasons the flagged signal should not count, both of which
matter more than the arithmetic.

**It is already priced.** The turn-count difference between revisers and
non-revisers is the same structure the shortcut ceiling charges for: an
agent that has revised cannot be the one revising now, and that
elimination is exactly what the measured ceiling of 0.29 accounts for. A
cue detector earns its place by finding cues *beyond* the structural ones
the ceiling has already charged for. Counting the same structure twice,
once in the ceiling and once as a gate failure, is double-billing.

**The model is never in a position to see it.** Size-biased pool
membership is a property of a sampling procedure the model does not
perform. The model sees a transcript and its own role in it. A cue is
something exploitable from that position. Nothing about "an agent with
more turns is over-represented in a pool I never draw from" is available
to it.

## The change

**Both arms are drawn agent-first.** The model's arm is unchanged: one of
the model's turns, drawn uniformly. The comparison arm now draws one
other agent uniformly, then one of that agent's turns.

Unchanged: the equivalence bound [0.45, 0.55], the positive-control floor
of 0.70, the classifier family and capacity, the episode count, the
feature sets, and the leaky-grammar and register-reindex positive
controls. Implemented as `_pick_other(..., agent_uniform=True)` in
`src/cue_detector_a3.py`.

**Every verdict reports both samplers side by side.** The amended sampler
carries the verdict; the registered sampler's number is printed beside it
in the same record, so a reader can see what the original instrument said
and decide whether to accept the override. `gate()` returns both and
names which one the verdict came from.

**A second change, carried in the same amendment**, from Gate 1's
stability finding: the verdict is taken over five independent samples
rather than one. A single bootstrap interval resamples the test split of
one draw of episodes and is silent on spread between draws; measured
spread is 0.0224 on the tensor run against a bound half-width of 0.05, so
a clean grammar fails a single run about one time in nine. Reporting a
mean and a spread over five draws removes that.

## Regression check

Required by the ruling and recorded in `a3-gates/sampler_regression.json`
with the table reproduced in `gate1-curriculum-findings.md`. The size bias
can cut either way depending on which agents speak more, so a grammar
that passed under the old sampler could have been passing *because* of
the bias. Every grammar the registered sampler passed is re-run under the
amended one:

- **The registered MVM-0a grammar** (`curriculum.py`) — the important
  one, since five trained checkpoints and every result in
  `lesion-results/` and `null-calibration/` rest on its clean verdict.
- **A3 draft 2**, every agent revising, which passed both gates before
  the shortcut sweep found its true ceiling was 0.52.
- **A3 draft 3**, two revisers drawn uniformly, the current grammar.

## What this does not change

No bound, no control, no classifier, no episode count. It does not touch
`cue_detector.py`, whose token-level behaviour the existing records
depend on; the amended sampling lives in the A3 detector, and the
regression check reaches the registered grammar through a local variant
that reuses `cue_detector.py`'s own classifier and bounds.

It does not weaken the detector: the positive controls still fire, and
the regression table shows what the amended sampler says about every
grammar the old one cleared.
