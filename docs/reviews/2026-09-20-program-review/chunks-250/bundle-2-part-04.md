   d(T_act) − d(T_other) ≥ δ. The control finished at 0.299, below its own
   0.3227 ceiling, so under the registered floor rule its drop is
   undefined and the clause cannot be evaluated. **A clause that cannot be
   evaluated has not passed.** Seed 0 is NOT-TESTABLE on the differential
   clause and cannot land in H_self-location.
2. The discriminators that do not depend on the control still run and are
   reported as **partial** discriminators on seed 0: the matched
   other-agent subspace lesion, the random matched subspaces, and the swap
   probe.
3. The benign argument — that no generic binder was learned, so a
   primary-battery positive cannot be generic binding — is recorded as a
   **supplementary, unregistered reading only**. It does not substitute
   for the registered discriminator.

**The consequence, stated before the ruling and accepted:** under the
ratified three-seeds, three-of-three rule, with the bin required to hold
on every trained seed, **A3 as registered can no longer return a full
registered positive on H_self-location, regardless of seeds 1 and 2.** A
pre-stated eligibility rule counting only seeds whose control clears its
ceiling was considered and set aside on cost.

### The seeds, as revised the same day

*Entries: "RULED 2026-09-16 — A3 seeds 1 and 2: yes in principle…"
(`fcceae59`) and its same-day revision, "RULED 2026-09-16 (revision) — A3
seeds 1 and 2 launch as ONE WAVE on a single fresh go" (`1c2cc109`). Both
decided-by mixed.*

**Withdrawn:** the sequential condition (seed 1 first, seed 2 decided
after its pre-lesion baseline). It existed only to keep about $11
optional, and cost is not the constraint.

**Standing:** seeds 1 and 2 launch together as **one wave on a single
fresh verbatim go**, matching §4.3's "seeds 1 and 2 (C2 go per wave)".
Both process fixes are committed before any launch. John's threshold lock
commit comes before the seeds. **Neither ruling is a launch go.** No L1
lesion is run or read before the lock. Registered text, including the
$100 hard stop, is unchanged.

**Why the seeds are still worth about $22 after the strict-reading
ruling**, in the entries' own terms: they are **no longer steps toward a
three-of-three positive**; they are a test of whether the primary
battery's learnability replicates and whether the control is a seed
lottery. A seed whose control learns is fully testable and yields a
per-seed verdict, though the across-seed bin still caps at seed-dependent
or not-testable.

**Recorded case against:** the modal outcome is the control flat on both,
leaving three seeds not-testable on the differential clause plus partial
discriminators — a reportable null with a named cause.

**Cost correction** (from the revision entry): an earlier note said seven
seeds would run past the $100 hard stop. At the registered $9–13 per run,
seven seeds total roughly **$77–105 including the $13.92 already spent,
borderline rather than clearly over**. Optional extra seeds on a separate
go remain a live route to a checkpoint whose control learned, bounded by
the hard stop and the $80 account limit, **to be decided after seeds 1 and
2 report**.

---

## What needed John, and what still does

All three items that stood open on 2026-09-16 morning are **ruled**, above:
the bin (recorded as described, not binned), the undefined control drop
(strict reading, seed 0 not-testable on the differential clause), and the
seeds (one wave, on a fresh verbatim go).

**What still needs John**, in the order the registered procedure takes it:

1. **The threshold lock commit.** Reserved to him by §3.3. The thresholds
   are measured and waiting (`null-calibration/a3_pilot_seed0.json`):
   0.1777 on the primary battery, 0.2368 on the one computable
   differential. `lock_guard.py` refuses any localized-subspace run until
   that commit exists.
2. **A fresh verbatim go for the seeds 1 and 2 wave.** Neither ruling is
   one, and the go is quoted in the ledger row before spend.
3. **After seeds 1 and 2 report**, whether optional extra seeds run. The
   revision entry reopened this: seven seeds total roughly $77–105
   including the $13.92 spent, borderline rather than clearly past the
   $100 hard stop, so a checkpoint whose control learned stays a live
   route.


===== FILE: experiments/06-mvm-0a-constructed-self-index/seeds-endpoint-findings.md =====

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


===== FILE: experiments/06-mvm-0a-constructed-self-index/register-lesion-findings.md =====

# Register-lesion + item-level diagnostics (anomaly threads 3 & 4)

*2026-08-19. Status: **diagnostic record, not adjudicated** — these are
the cheap threads the twin-binding anomaly note queued; nothing here is
a registered result and nothing here emits a verdict on H_load-bearing.
That read, and the wave-3 disposition, are John's. All runs local and
$0 [C1/C2]; per-run outputs in `lesion-results/`, no committed record
overwritten [C6]. Code: `src/lesion_register.py`, `src/item_analysis.py`,
`src/pick_analysis.py`.*

## Thread 4 — the register lesion: binding survives everything

