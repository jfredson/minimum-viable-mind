# A3 seeds 1 and 2 — registered L0 endpoint

*2026-09-17. Local, $0, inference only. Run through `endpoint_a3.py`,
which was validated against the pilot first and reproduces its published
endpoint to the digit. Gated on John's threshold lock, which supplies
θ = 0.1777 on the primary battery and carries no threshold at all for the
control battery. Checkpoints verified by checksum.*

## What the wave was for, and what it answered

The ledger row staked the wave on two questions: whether the primary
battery's learnability **replicates**, and whether the control battery's
failure is a **seed lottery**. Both now have answers.

**Learnability replicates.** **The control is not a lottery; it fails on
every seed.**

## The primary battery

Across six independent evaluation seeds at n=800, reported as a spread
rather than a single draw:

| checkpoint | intact | under L0 | ceiling-corrected drop | vs θ |
|---|---|---|---|---|
| pilot (seed 0) | 0.5683 (sd 0.0076) | 0.1988 (sd 0.0173) | 1.337 (sd 0.057) | 7.5× |
| seed 1 | 0.5633 (sd 0.0316) | 0.2015 (sd 0.0215) | 1.342 (sd 0.103) | 7.6× |
| seed 2 | 0.5738 (sd 0.0284) | 0.1447 (sd 0.0127) | 1.528 (sd 0.068) | 8.6× |

Three checkpoints trained from different seeds land within 0.011 of each
other on the intact score. Zeroing the acting channel collapses all three.
Every drop clears the locked threshold by between seven and nine times,
and a drop above 1.0 means the lesion took the battery **below** what an
ownership-blind solver reaches.

This is as clean a replication as the design can produce. The objective is
learnable and the learning genuinely depends on ownership.

## The ownership-free controls

| checkpoint | state battery drop | syntax battery drop |
|---|---|---|
| pilot (seed 0) | +0.0018 | 0.0000 |
| seed 1 | +0.0002 | 0.0000 |
| seed 2 | **+0.0769** | 0.0000 |

The syntax battery does not move at all on any checkpoint. The state
battery is untouched on two and moves 0.0769 on seed 2, which is forty
times the others.

**That does not fire** — the locked threshold for the state battery is
0.1172 and 0.0769 is well inside it — but it is reported rather than
rounded away, because it is the only asymmetry in the table and a
write-up that shows the other two without it would be flattering.

## The control battery, which is the finding

| checkpoint | intact | its ownership-blind ceiling | learned? |
|---|---|---|---|
| pilot (seed 0) | 0.2877 (sd 0.0302) | 0.3227 | no |
| seed 1 | 0.3057 (sd 0.0281) | 0.3227 | no |
| seed 2 | 0.3195 (sd 0.0150) | 0.3227 | no |

**On all three checkpoints the control battery sits below its own
ownership-blind ceiling.** A battery scoring under the level a solver
reaches without knowing which agent it is has not learned the task. Seed
2 comes closest, 0.3195 against 0.3227, and still does not clear it.

The consequence is mechanical. The registered floor rule leaves a
battery's drop **undefined** when its baseline is below its ceiling, so
the control's drop is undefined on every checkpoint, and the registered
differential clause — the primary's drop minus the control's — **cannot
be evaluated on any of the three.**

> **CORRECTION, 2026-09-17.** The sentence above understates the bar and
> is corrected here rather than rewritten. The floor rule is not
> "baseline below ceiling"; it is **baseline minus ceiling below 0.10**.
> So the control needs **0.4227**, not 0.3227, for its drop to be
> defined, and the three checkpoints miss by 0.135, 0.117 and 0.103
> rather than by the 0.035, 0.017 and 0.003 the table implies.
>
> No conclusion changes — the clause is uncomputable either way — but the
> gap is four to forty times wider than the table suggests, and an
> Amendment A4 that merely cleared the ceiling would still leave the drop
> undefined. See `control-battery-proposal.md`.

John ruled seed 0 not testable on the differential clause on 2026-09-16.
That ruling now extends to the whole wave, not by a further ruling but by
the same arithmetic applied to two more checkpoints.

## What this settles, and what it does not

**Settled: the control battery does not learn under this design.** Three
seeds, one outcome. It was the modal case the ledger recorded against the
wave before the go was given, and it came true. A recorded case-against
that comes true is worth more than a prediction that does not, and this
one removes the remaining hope that the control was a lottery.

**Therefore A3 as registered cannot return a positive on any checkpoint
it has.** Not because the primary failed — it succeeded on all three, by a
wide margin — but because the clause that compares it to a control cannot
be computed when the control never learned.

> **ANNOTATION, 2026-09-17. The conclusion stands; the reason given here
> is wrong and is corrected.** The clause cannot be computed **whether or
> not the control learned**. Its ownership-blind ceiling is 1.0, so a
> defined drop would need a baseline of 1.10 and no model can reach it.
> The clause was unsatisfiable from registration, months before any
> checkpoint existed, and the control's failure to learn is beside the
> point. Measured at `ceiling-measurement-findings.md`.

**Not settled, and not touched here: where ownership lives.** L0 removes
an input channel. It shows the action depends on ownership; it does not
show the network built an internal structure carrying it. That is the
question the localization work was for, and yesterday's runs leave it
open, with the stack unvalidated at this scale.

## For the 2026-10-04 decision

The control-battery question now has its evidence. The choice is between a
registered Amendment A4 that makes the control learn, and closing A3 with
partial discriminators and saying so plainly. Whichever way it goes, the
proposal should carry three facts from this wave: the primary replicates
tightly across seeds, the control fails on all three rather than some, and
the ceiling adjudication permits exactly one amendment to the compute cap,
so an A4 needing new runs must make that argument explicitly.

> **CORRECTION, 2026-09-17. The last clause is withdrawn as misleading.**
> The single-amendment rule bars a **raise** above the $400 ceiling. An
> Amendment A4 that fits inside the existing ceiling is not a raise and
> needs no cap amendment at all. Three retrained seeds cost $27 to $39
> against $184.3 of remaining headroom and $65.69 left on the A3 stop, so
> money is not the binding constraint on this decision and I should not
> have implied it was.

## Method notes, recorded honestly

- Every figure is a mean across six evaluation seeds with its spread, not
  a single draw. Intact and lesioned are paired within each seed, so the
  drop is not exposed to between-seed noise even though the levels are.
- The pilot's published 0.506 and its 1.515 drop both came from the single
  default evaluation seed. Its typical values are 0.5683 and 1.337, so
  that seed flatters twice. The conclusion is unaffected; the headline
  number was simply lucky.
- The six seeds used here are the first six of the twelve in yesterday's
  noise measurement, so the spreads quoted understate the fuller estimate
  at this sample size. The wider one is the better figure.
- The control battery is reported and never read for a verdict, which is
  what the lock enforces by carrying no threshold for it.
