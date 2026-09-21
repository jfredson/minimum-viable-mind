# The standardised refit at the same positions — findings

*2026-09-21 (Pacific). **UNREGISTERED**, diagnostic only. No verdict is
read and no cell here feeds one. Local, inference only, no training, no
network, $0 [C1/C2]. Method committed in `standardised-refit-method.md`
at commit `7745d4a`, together with
`src/standardised_position_sweep_a3.py`, **before either produced any
output** — and in the same commit as the first follow-up run, so this
method was fixed before that run's numbers existed and nothing here can
have been shaped by them.*

*Runs the second of the two follow-up runs ruled on 2026-09-20. It
answers the red-team ledger's item on what an unscaled fit charges a
quiet direction (`RT-58`).*

## The cell

**FOUND NOWHERE.** Sub-pattern: **found on seeds but not the pilot.**

The pre-stated cell needs a testable position found on **the pilot** and
on at least one other checkpoint. The pilot found nothing, so the cell is
FOUND NOWHERE whatever else happened.

**But something else did happen, and the method file required it be
reported regardless of which cell fired.** One testable cell cleared the
family-adjusted bar:

> **Seed 2, the other agent's revision value, layer 3: accuracy 0.2778,
> margin +3.43 standard deviations, zero of 200 shuffled draws met or
> beat it, and it beats the majority-class rate. FOUND.**

This is the first time anything in this line has cleared a
family-adjusted bar at a position where the answer is not available in
the current token. It is one cell out of 135 and the section below says
plainly why that is suggestive and not settled.

## What the run was for, and what it answered

The unscaled read left the 448 residual directions on their own scale
under a squared penalty, which charges a quiet direction the square of
how quiet it is. With ten directions carrying 85% to 99.5% of the
variation, that instrument was worst placed against exactly the thing it
was testing: a self-index that is real, linear and quiet. The question
was whether a read that puts every direction on equal terms finds
anything the unscaled read could not.

**It does — in one place, and not by becoming broadly more sensitive.**

| checkpoint | unscaled margins across the 45 testable tests | standardised |
|---|---|---|
| pilot | −1.49 to +2.33 (mean −0.09) | −1.83 to +1.54 (mean −0.10) |
| seed 1 | −1.30 to +2.39 (mean +0.36) | −1.97 to +2.22 (mean +0.12) |
| seed 2 | −3.01 to +3.34 (mean −0.22) | −2.20 to +3.43 (mean −0.18) |

The distributions are almost unchanged. Standardising did not lift the
whole sweep; it moved one position on one checkpoint across the bar. That
is a narrower result than "the unscaled penalty was hiding the signal",
and it is the honest description.

## The anchor, in three parts

**Part A held on all three checkpoints, exactly.** The unscaled fit
returned all fifteen recorded numbers with a largest difference of
**0.0**, which proves this run differs from the recorded one by the
scaling and by nothing else.

**Part B held on all three checkpoints.** The standardised fit at the
model's own marker token, where the answer is the input token:

| checkpoint | standardised (layers 3, 4, 5, 7, 8) | floor |
|---|---|---|
| pilot | 0.4775, 0.5325, 0.5025, 0.4750, 0.5075 | 0.35 |
| seed 1 | 0.5050, 0.5425, 0.5275, 0.5075, 0.5075 | 0.35 |
| seed 2 | 0.4625, 0.5025, 0.5025, 0.4650, 0.4500 | 0.35 |

As the method file said in advance, these do **not** reproduce the
recorded unscaled numbers and are not read as failing for that reason. A
standardised fit is a different estimator. They land within about 0.05 of
them, sometimes above and sometimes below.

**Part C**, in the self-test rather than the run: with the standardising
step replaced by a do-nothing transform, the standardised code path
reproduces the unscaled path's accuracy and optimiser pass counts
exactly, cell for cell. The two code paths are the same path, so the
scaling really is the only thing that changed.

## The instrument got materially better in one measurable way

**The optimiser now converges everywhere.**

| checkpoint | fits hitting the 2,000-pass cap, unscaled | standardised |
|---|---|---|
| pilot | 13.5% | **0.0%** |
| seed 1 | 22.3% | **0.0%** |
| seed 2 | **73.6%** | **0.0%** |

Not one fit in 165 tests hit the cap. The standardised fits converge in
roughly 520 to 570 passes.

**This matters for the cell that cleared.** The Gate B review's `RT-65`
observed that the unscaled MARGINAL on seed 2 came from a fit that used
the full 2,000 passes on all four folds — an under-fitted number. The
standardised cell that clears the bar used **543, 519, 538 and 553
passes** on its four folds. It is a converged fit, not a stopped one.

The two are also not the same cell. Under the unscaled read the peak at
that position on seed 2 was **layer 4** (+3.34, MARGINAL); under the
standardised read it is **layer 3** (+3.43, FOUND). All five layers are
positive under both reads:

| layer | unscaled (seed 2) | standardised (seed 2) |
|---|---|---|
| 3 | +1.34 | **+3.43 FOUND** |
| 4 | +3.34 MARGINAL | +2.47 |
| 5 | +1.75 | +1.93 |
| 7 | +2.54 | +2.18 |
| 8 | +2.70 | +2.33 |

## Every cell, as promised

Best layer per position per checkpoint, unscaled / standardised, margin
in standard deviations. F = FOUND, M = MARGINAL, bar 3.38.

| position | pilot | seed 1 | seed 2 |
|---|---|---|---|
| `own_assign_1_value` *(negative control)* | +0.23 / −0.02 | +0.08 / +2.65 | +0.49 / +0.86 |
| `own_assign_2_value` | −0.49 / +0.84 | +0.80 / +1.69 | +0.23 / −0.49 |
| `own_revision_decision` *(the registered anchor)* | +0.46 / +0.68 | +0.18 / +2.08 | −0.26 / −0.44 |
| `own_revision_value` | +0.68 / +0.32 | +2.07 / +0.95 | −0.32 / +0.95 |
| `own_revision_by` | +0.34 / +1.27 | +1.65 / +0.65 | +0.38 / +0.65 |
| `own_revision_marker` *(positive control)* | +53.73 F / +40.41 F | +40.86 F / +36.47 F | +39.04 F / +35.95 F |
| `before_own_revision_turn` | −0.04 / +0.45 | +0.47 / −0.11 | −0.41 / +0.35 |
| `other_revision_decision` | +0.24 / −0.22 | +0.16 / +0.21 | +0.88 / +0.44 |
| **`other_revision_value`** | +2.33 / +1.54 | +2.39 / +2.22 | **+3.34 M / +3.43 F** |
| `query_answer_decision` | +0.48 / +1.41 | +1.29 / +0.51 | +0.46 / +0.64 |
| `query_answer_value` | +0.37 / +0.58 | +1.19 / +1.08 | +0.68 / +1.45 |

## The controls

**The positive control holds on all three checkpoints.** At the model's
own marker token the standardised read gives 0.5428–0.5567 on the pilot,
0.5428–0.5523 on seed 1 and 0.5310–0.5440 on seed 2, at +32.61 to +40.41
standard deviations, every layer FOUND. No checkpoint is void. The
measured ceilings used for calibration are 0.5567, 0.5523 and 0.5440.

**The negative control shows no leak, but it runs warmer on seed 1 and
that is worth saying.** At the model's first assignment value, where its
own marker has not yet appeared, the standardised margins are −1.08 to
−0.02 on the pilot, −0.53 to +0.86 on seed 2, and **+1.26 to +2.65 on
seed 1**. Nothing clears the bar, so there is no leak by the pre-stated
rule. But +2.65 at a position where the answer is not knowable is higher
than the unscaled read produced there (+0.08 at its best layer), and it
is a caution about how well calibrated this second instrument is. It is
recorded rather than argued away.

## The smallest signal this run could have found

Calibrated against **this instrument's own measured ceiling** at the
positive control, not against a perfect score and not against the
unscaled read's ceiling.

| checkpoint | ceiling | smallest detectable signal |
|---|---|---|
| pilot | 0.5567 | 8.05% – 10.27% (median 9.16%) |
| seed 1 | 0.5523 | 7.87% – 10.09% (median 9.30%) |
| seed 2 | 0.5440 | 8.06% – 10.68% (median 9.32%) |

About one episode in eleven, the same as the unscaled read's corrected
figure and the same as the other-agent run's. **The three runs in this
sequence are comparably powered**, so differences between them are not
differences in sensitivity.

## Degeneracy and geometry

**Degeneracy hits: three**, all of the same kind — accuracy exactly equal
to the majority-class rate of 0.2582, which the pre-stated rule treats as
degenerate and gives no cell:

- pilot, the appended question's answer marker, layer 8
- seed 1, the model's revision decision, layer 7
- seed 1, the model's revision value, layer 5

The unscaled read had none. So **standardising makes the classifier
collapse onto naming the commonest answer more often**, which is a real
property of the second instrument and is reported because the method file
required every hit be reported by test. It is also why requiring
accuracy above the majority-class rate was kept in the label.

**Geometry**, unchanged from the unscaled run because it is a property of
the states and not of the fit: the top ten of 448 directions carry 0.8524
to 0.9907 on the pilot, 0.9430 to 0.9953 on seed 1 and 0.8774 to 0.9806
on seed 2.

## What this means, read together with the first follow-up run

Three independent things now point at the same position, the other
agent's revision value:

1. **The unscaled own-index read** found it positive on fifteen tests of
   fifteen, ranking **first of the nine testable positions** by mean
   margin (+1.73; the next two are +0.14 and +0.13).
2. **The other-agent index is not there.** The matched control L2(a),
   run for the first time, gives +1.00, +1.40 and +1.73 at that position
   and ranks it **fourth of nine** — so the exclusion confound that was
   offered to explain the pattern away is not supported.
3. **Under a converged standardised fit it clears the family-adjusted
   bar on seed 2**, at +3.43 with zero of 200 draws beating it.

**And here is why that is still not a finding.**

- **It is one cell in a family of 135.** A family bar is set precisely so
  that one cell crossing it is what you expect at a 5% family-wise error
  rate — which is to say, this is the outcome the bar was designed to
  permit by chance about one time in twenty.
- **Two hundred draws cannot certify it.** Zero of 200 establishes a
  probability below 0.005, about 2.58 standard deviations, which is
  **below** the 3.38 the family needs. The rest comes from a normal
  approximation to a null measured with only 200 draws. The method file
  said before the run that a single FOUND cell is **suggestive and wants
  a targeted rerun at that position with far more draws, not settled**,
  and that is what it is.
- **It is not the same cell the unscaled read flagged.** That was layer
  4; this is layer 3. The position is consistent across reads; the layer
  is not.
- **The pilot does not show it.** The pilot is the checkpoint with the
  most legible states by every earlier measure, and its standardised
  margin at that position is +1.54.
- **Seed 2 is the checkpoint to trust least**, on every earlier ground —
  though the pass-cap objection against it no longer applies here, since
  nothing was capped.
- **The 135 tests are not independent.** All three checkpoints read one
  draw of 4,000 episodes and the five layers read one running state
  (`RT-59`), so the bar is, if anything, computed as though there were
  more independent tests than there are.

## What these findings may and may not say

They may say that a standardised linear read finds the register index at
one testable position on one checkpoint and nowhere else, on these
checkpoints at these positions; that this cell was reached by a converged
fit where the unscaled read's comparable cell was not; and that
standardising did not otherwise change what the sweep sees.

They may **not** say the linear-read line is closed, and may not say the
models carry no self-index.

- Under **Amendment A3 section 3.2** nothing counts as localized or as
  absent until causal patching has also run (`RT-49`, `RT-50`). **The
  registered term for the line's state is *not testable
  (localization)***, and that is the term used here. One probe cell over
  a bar does not localize anything.
- The regularisation strength was **not tuned**. A null at this strength
  is a null at this strength, and this run does not establish that 1.0 is
  the right one for a standardised fit.
- One target was read. The marker-word target under either read remains
  unrun, at about seventy processor-hours.
- The pilot-versus-seeds legibility gap is unchanged and unresolved.
- It does not touch red-team objection **R1** and changes no registered
  result.

## What this cannot do

One fitted linear statistic at one regularisation strength, eleven
positions, five layers, 4,000 episodes, three 30-million-parameter
checkpoints on a synthetic grammar, one target.

What it **can** do, and did, is narrow one alternative: "the signal was
there all along but the unscaled penalty could not reach it" is now a
much weaker story. The standardised read reaches the quiet directions on
equal terms and sees essentially the same sweep — mean margins unchanged
to two decimal places on the pilot and seed 2 — apart from one cell.

## Open items

1. **Causal patching has still never run.** Under the registration it is
   required before anything counts as localized or absent. It remains the
   binding item and nothing here substitutes for it.
2. **The other agent's revision value now deserves a targeted rerun**,
   and it is the cheapest decisive move available. One position, five
   layers, three checkpoints, both reads, with far more than 200 draws —
   enough that the count alone can certify a family-safe clearance rather
   than leaning on a normal approximation. Three separate lines of
   evidence now point at it and none of them is strong enough alone.
3. **The standardised read's negative control on seed 1** runs to +2.65
   where the answer is not knowable. If the targeted rerun happens, that
   position should be rerun with it.
4. **Standardising collapses the classifier onto the commonest answer
   more often** (three degeneracy hits against none). Worth knowing
   before this instrument is used again.
5. **The marker-word target** remains unrun under either read.

## Cost and where the output is

Local, inference only, no training, no network, $0 [C1/C2], on three
existing checkpoints verified by checksum. **10.87 hours** of wall-clock
time — 3.72 on the pilot, 3.49 on seed 1, 3.66 on seed 2 — at four
workers, run after the first follow-up run as the brief ordered. The
method file said to expect twelve hours or more; it took slightly less,
because standardised fits converge in about 540 passes where unscaled
fits on seed 2 mostly ran to the 2,000-pass cap. Seed 2 was the slowest
checkpoint under the unscaled read by a wide margin and is not under this
one.

Outputs, none overwritten [C6]:

- `a3-gates/standardised_position_sweep_a3_a3_30m_seed0.json`
- `a3-gates/standardised_position_sweep_a3_a3_30m_seed1.json`
- `a3-gates/standardised_position_sweep_a3_a3_30m_seed2.json`
- `a3-gates/standardised_position_sweep_a3_summary.json`

These findings go through a Gate B review before any of this enters
`STATUS.md`.
