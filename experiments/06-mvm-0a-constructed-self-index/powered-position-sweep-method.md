# Powered eleven-position sweep — method, committed before the run

*2026-09-20. **UNREGISTERED**, diagnostic only. No verdict is read and no
cell here feeds one. Local, inference only, no training, no network, $0
[C1/C2]. Reads no registered verdict and touches no registered text.
Fresh output file per checkpoint, nothing overwritten [C6].*

*Committed before the sweep produces any output. The cells were fixed
while nobody knew which would fire.*

## Why

Two things are now established and one is not.

**Established.** The generator's agent index cannot be recovered in
principle, so every probe that used it was asking an unanswerable
question (`position-sweep-findings.md`). And with a well-posed target,
adequate power and a null that can resolve the bar, own-agent identity is
**not linearly present at the registered probe position** —
NOT CARRIED on both arms, all three checkpoints, thirty tests spanning
−1.85 to +0.49 standard deviations (`powered-target-test-findings.md`).

**Not established.** Whether it is carried *anywhere else*. The
eleven-position sweep that asked that question was run against the
unrecoverable target and came back SWEEP INVALID, so it answered nothing.
This reruns it properly: the same eleven positions, the two well-posed
targets, and the powered settings.

**This is the last run in this line.** It reports which positions clear,
if any, and stops.

## What is measured

Identical machinery to the powered anchor test, widened from two
positions to eleven.

- **Checkpoints.** The three A3 30-million-parameter checkpoints,
  verified by checksum: pilot `a3_30m_seed0.pt` (`f751228c…`), seed 1
  `a3_30m_seed1.pt` (`eeed93b8…`), seed 2 `a3_30m_seed2.pt`
  (`f1f131cb…`).
- **Episodes.** 2,000 paired episodes at content seed 20260917, giving
  **4,000 episodes**. About 160 examples per marker word. Capture is
  chunked; the model is causal and each episode is encoded
  independently, so chunking changes nothing.
- **Layers.** 3, 4, 5, 7, 8.
- **Draws.** 1,000 per test.
- **Read.** The plain difference-of-averages read, held-out
  nearest-average accuracy as the cell-bearing statistic, macro
  separation reported beside it. Everything fitted on training folds
  only, four folds.
- **Arms.** Two, run through identical procedures: the model's **own
  marker word** (25 classes, majority-class rate about 0.0475) and its
  **register index** (4 classes, majority-class rate about 0.258).

The vectorised scorer is verified against the original before any run
reports, on a noise case and a planted-signal case, and the run refuses
on disagreement. That check is carried over unchanged and its result is
recorded in every output file.

## The eleven positions, and which of them can be read for carrying

A turn renders as `assign {item} to {value} by {marker}` — the marker
comes **after** the value.

| # | position | role |
|---|---|---|
| 1 | `own_assign_1_value` | **negative control** — see below |
| 2 | `own_assign_2_value` | testable |
| 3 | `own_revision_decision` | testable — the registered anchor |
| 4 | `own_revision_value` | testable |
| 5 | `own_revision_by` | testable |
| 6 | `own_revision_marker` | **positive control** — the input token |
| 7 | `before_own_revision_turn` | testable |
| 8 | `other_revision_decision` | testable |
| 9 | `other_revision_value` | testable |
| 10 | `query_answer_decision` | testable |
| 11 | `query_answer_value` | testable |

**Position 6 is the positive control.** The model's own marker word sits
there as an input token. A checkpoint where it fails to clear is
**VOID** and its other positions are reported without interpretation.
The control is the marker-word arm at position 6, and it governs both
arms, because what it tests is the read.

**Position 1 is a negative control, and this is new.** At the value token
of the model's *first* own turn, the model's own marker **has not yet
appeared anywhere in the episode** — its own marker is emitted two tokens
later, and no other agent's turn carries it. So the target is not
determinable from anything the model has seen. The same holds for the
register index, which needs the model's own marker before it can be
ranked.

A clearance at position 1 therefore cannot be identity being carried
forward; it would mean something is leaking the answer — most plausibly
the acting channel, which injects at exactly that token. Stated in
advance: **a clearance at position 1 is reported, is treated as evidence
of a leak rather than of carrying, and is excluded from the cells.** If
it happens, it is the finding, and it would put every other position on
that checkpoint in doubt.

**The nine testable positions** are the rest. "Non-input" in the cells
below means these nine: not position 6, where the answer is the token,
and not position 1, where the answer is not yet knowable.

## The bar, which binds here in a way it did not last time

Two arms × nine testable positions × five layers × three checkpoints =
**270 discovery tests**. That is nine times the previous run's family and
it changes the arithmetic:

| | previous run (30 tests) | this sweep (270 tests) |
|---|---|---|
| family-wise error if the bar stays at 3.0 sd | 4.0% | **30.6%** |
| family-adjusted bar for 5% family-wise | 2.94 sd (subsumed) | **3.56 sd** |

Last time the three-standard-deviation bar was already family-safe and no
adjustment was needed. **Here it is not**: leaving the bar at three
standard deviations would give roughly a one-in-three chance of a false
clearance somewhere in the sweep, which for a sweep whose whole purpose
is to ask "does anything clear anywhere" is exactly the wrong error to
tolerate.

So, pre-stated:

- **The per-test bar of 3.0 standard deviations is still computed and
  reported**, for continuity with every earlier run.
- **The cells turn on the family-adjusted bar of 3.56 standard
  deviations, together with zero of the 1,000 shuffled draws meeting or
  beating the real score.** A clearance meeting both is **ROBUST**.
- A clearance that passes three standard deviations but not 3.56 is
  **MARGINAL**, is reported, and **does not trigger a cell**.

**An honesty note about what 1,000 draws can and cannot certify.** A
count of zero out of 1,000 establishes a probability below 0.001, which
is equivalent to about 3.09 standard deviations — **below** the 3.56 the
family bar needs. So the count alone cannot certify a family-safe
clearance across 270 tests; the standard-deviation margin supplies the
rest, and that part is a normal approximation to a null measured with
1,000 draws. A single ROBUST clearance should therefore be read as
suggestive and worth a targeted rerun at that one position with far more
draws, not as settled. The findings will say so if it happens.

## Preconditions, stated in advance

Carried forward unchanged: a null with zero spread, a class missing from
a training fold, or accuracy exactly equal to the majority-class rate
makes a test DEGENERATE, and it gets no cell.

## The cells, fixed here

Applied **separately to each arm**, across the three checkpoints. A
checkpoint whose positive control fails is VOID and is excluded; if the
**pilot** is void, the arm is VOID and no cell is assigned.

**CARRIED SOMEWHERE.** At least one of the nine testable positions clears
the family-adjusted bar on **the pilot**, and at least one testable
position clears on **at least one other non-void seed**.

> Reading: own-agent identity is linearly present somewhere in the
> episode, at a position where it has to have been carried rather than
> read off the current token. The positions that clear are the finding
> and they name where to look next. It would still not settle red-team
> objection R1 — what is carried could be the acting channel's trace
> passed forward rather than a self-index.

**CARRIED NOWHERE.** The above does not hold.

> Reading: across eleven positions, five layers, two well-posed targets
> and three checkpoints, own-agent identity is not linearly recoverable
> anywhere in the episode except where it is present as an input token.
> Combined with the anchor result, that closes the linear-read line of
> attack on these checkpoints.

**These two are exhaustive by construction**, which is what was asked
for, and that has a cost worth naming: a pattern like "clears on the
pilot only" lands in CARRIED NOWHERE despite not being nothing. So the
findings will **report the clearing positions per checkpoint regardless
of which cell fires**, and name the sub-pattern explicitly. The cell is a
summary, not the whole result, and nothing gets hidden inside it.

## What this cannot do

One statistic, linear, eleven positions, five layers, 4,000 episodes,
three 30-million-parameter checkpoints on a synthetic grammar. A null
everywhere is consistent with identity being carried non-linearly, or
distributed across positions rather than resident at any one of them, or
at a position not on the list. It does not touch red-team objection R1.
It changes no registered result.

## Cost and where the output goes

Capture is about two minutes per checkpoint per pass, two passes (the
appended-question positions need the question). Scoring is about 0.2
minutes per marker-word test and 0.11 per register-index test, so roughly
fifty minutes of scoring in total. Checkpoints are independent and may be
run as separate processes; the summary is assembled from the per-
checkpoint files afterwards, which is why the run and the summary are
separate steps.

One fresh file per checkpoint under `a3-gates/`, named
`powered_position_sweep_a3_<checkpoint>.json`, plus a summary file and
`powered-position-sweep-findings.md`. Nothing existing is overwritten.

Implementation: `src/powered_position_sweep_a3.py`, committed together
with this file and before either produced any output. Gated on the
known-answer test, and deliberately not on the threshold lock, for the
reason given in `denoised-direction-method.md`.
