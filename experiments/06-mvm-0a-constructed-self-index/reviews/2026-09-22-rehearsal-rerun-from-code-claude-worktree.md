# Does the code still produce the committed record? — the measurement rehearsal, re-run from scratch

*2026-09-22 (Pacific). **INTERIM RECORD, FILED BEFORE THE LONG RUN.** This file
is committed now, empty of results, so that a re-run of roughly two hours of
laptop time cannot be lost the way the session before this one nearly lost its
own work. Results are appended to this same file when the run finishes.*

*Written under the workspace plain-language rule
(`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30).*

---

## The gap this closes

The measurement rehearsal is merged to the shared main line: the code sits at
`experiments/rehearsal-successor-measure/`, the findings at
`docs/2026-09-21-successor-measure-rehearsal.md`.

Two earlier checking sessions verified every figure in the findings **against
the committed output files**, exhaustively. Both checks ran in one direction
only. What nobody has done is the other direction: whether those committed
output files are what the code actually produces when you run it today.

That distinction is the whole point of this session. A document agreeing with a
record is not the same as the record having come out of the code. The programme
has twice this week been bitten by a number that agreed with everything except
reality.

## What is being done

1. The whole rehearsal is re-run end to end, from the committed code, in a
   scratch copy outside the repository at `~/.cache/mvm-rehearsal-verify/`.
   Nothing under `experiments/rehearsal-successor-measure/` is touched.
2. Every regenerated output file is compared against the committed one, byte
   for byte where the file is deterministic, and number by number where a file
   legitimately cannot be byte-identical (the two files that record wall-clock
   seconds).
3. Particular attention goes to the figures a registration review would be
   argued from: the separable arm reading exactly 0.0000 on three seeds; the
   entangled arm at 0.8727, 0.8848 and 0.8801; the freely trained arm at
   0.8863, 0.8366 and 0.8499; the three readings of the read's label at fits of
   0.256, 0.706 and 1.000, with their transplant readings; and the degree range
   of 0.9817 to 1.0000 that the two failing readings produce for an arm whose
   degree is 0.0000 by construction.
4. Any number that does not come back is reported, however small, with a
   judgement on whether the committed record or the fresh run is the right one.

The training is seeded, so it should come back **identical, not merely close**.
A seeded run that drifts is itself a finding and is reported as one.

## Decision on the half-finished run left behind: start clean

The brief for this session says a previous session got five of the ten toy
models retrained into `/tmp/rehearsal-check/`, and offers that directory for
re-use if its checkpoints can be shown to have come from the same code.

**That directory does not exist.** It is absent from `/tmp`, from
`/private/tmp`, from the per-user temporary folder and from a search of the
user's home directory; nothing anywhere in the repository names it. Whether the
system cleaned it out or it was never written, there is nothing to inspect and
therefore nothing whose origin could be established.

So this session **starts clean**, which is what it would have chosen anyway.
Re-using checkpoints is only safe if you can show which code wrote them, and a
half-finished set of five models out of ten could not have supplied the other
five in any case.

## Cost and limits

Laptop time only. No machine is rented, no vendor is contacted, nothing is
spent. The staged slice of rented time is **not** run and is not touched.

Nothing is fixed. Anything found is reported here and left alone.

*(Results section appended below when the run completes.)*

---

# Results

*Appended 2026-09-23 (Pacific), after the run. The re-run took about one hour
and three quarters of laptop time, not the half hour the brief for this session
estimated — the committed record's own training log adds up to seventy-eight
minutes of training alone, and the findings document says "about two hours",
which is the right figure. Nothing was rented and nothing was spent.*

## Verdict: the committed record is not what the code produces, except on one arm — and the reason is that the code does not produce the same thing twice

The headline is not that somebody wrote a number down wrong. Every number in
the committed output files is a faithful record of a run that really happened.
The headline is that **the run cannot be repeated.**

- **Everything about the separable arm — the arm built with the ownership
  answer in a slot of its own — came back exactly, to every decimal place.**
  That is where the rehearsal's strongest claims live, and all of them survive.
- **Nothing about the entangled arm or the freely trained arm came back.**
  Every figure those two produce moved, some of them a long way.
- **The cause is that the training is not reproducible.** The same code, the
  same seeds, the same laptop, twice in one evening, gives two different
  models. This was measured directly and is not an inference.

## The measurement that settles it

The rehearsal's two constructed arms and its free arm were trained a third
time, from the same code and the same seeds, an hour after the second. Three
runs, three answers:

| arm and seed | committed record | re-run | third run |
|---|---|---|---|
| separable, seed 0 — own-directed | 1.0000 | 1.0000 | 1.0000 |
| separable, seed 0 — named-other | 1.0000 | 1.0000 | 1.0000 |
| entangled, seed 0 — own-directed | 0.5817 | 0.5567 | 0.5743 |
| entangled, seed 0 — named-other | 0.2590 | 0.2677 | 0.2397 |
| free, seed 0 — own-directed | 0.5633 | 0.5767 | 0.5810 |
| free, seed 0 — named-other | 0.2547 | **0.3470** | 0.2583 |

At the level of the saved model files, two runs of the same seed on the same
day differ by **0.0003** at most on the separable arm and by **0.51** at most on
the entangled one. The separable arm's numbers are steady not because its
training is reproducible but because it learns its task perfectly: it answers
1.0000 on both conditions, and a weight that moves in the fourth decimal place
cannot change a saturated answer. The other two arms sit at about 0.56 and
0.25, where a small change in weights does move the count.

Why the training drifts is not established here and is not fixed here. The
architectures, the training budget and the number of parameters are identical
between the runs — the record's own file confirms every one of those — and the
episode generator is exactly reproducible, which is shown by the one solver
that is computed rather than trained returning **0.2380 and 1.0000** in both
runs, and by the two checks that use no model at all coming back byte for byte
identical. What is left is the training arithmetic on the laptop's own
accelerator, which does not guarantee the same sum twice.

## Per-file verdict

| file | verdict |
|---|---|
| the made-up-populations check (`denominator_simulated.json`) | **byte for byte identical** |
| the same-value-cell check (`denominator_control6.json`) | **byte for byte identical** |
| the training log (`train.json`) | identical but for elapsed seconds, which no two runs can share. Parameter counts, step counts and batch sizes all match |
| the learn-both gate (`gate.json`) | separable arm identical, including its lesioned accuracies of 0.2467, 0.2510 and 0.2733. Both other arms moved in every cell |
| the blind nomination (`nominate.json`) | every figure the findings quote for the separable arm identical. Both other arms moved, including which site set and which reading of the label win |
| the reading and the controls (`transplant.json`) | separable arm identical throughout — the reading, all seven controls, and its accuracy on marker words it has never seen. Both other arms moved |
| the made-up outcome cases (`outcomes.json`) | the near-zero case and the no-verdict case identical; the high case moved |
| the spread of the reading (`uncertainty.json`) | separable arm identical at zero spread; both other arms moved |
| the no-transplant rate (`denominator_floor.json`) | separable arm exact at 0.0000; both other arms moved, and **one pre-stated pass turned into a fail** |
| the attenuation check (`denominator_attenuated.json`) | separable arm identical; **the check's verdict reverses on four arm-and-seed pairs** (below) |
| the negative reading (`negative_case.json`) | **the two negative readings, −0.1706 and −0.2755, came back exactly**; they are the separable arm at seeds 0 and 2. The other arms' rows moved |
| the budget question (`budget_check.json`) | moved, and its conclusion reverses (below) |
| the frozen straight-line reads (the nine `reads_*.npz` files) | all nine differ. On the separable arm, under the reading of the label that works, the directions differ by about a millionth to a thousandth — floating-point noise. On the other two arms they differ by 1 to 3, which is to say completely |
| the throughput record (`throughput.json`) | ratios moved: 0.9813 to 0.9888 for the separable arm, 1.0488 to 1.0657 for the entangled one |
| the printed summary (`summary.txt`) | differs, being a printout of the above |
| the self-test record (`self-tests.txt`) | **differs for a different reason entirely** — see the separate finding below |
| the staged rented-slice plan (`rented-slice-plan.txt`) | **deliberately not regenerated.** The staging script reads paths in the experiment directory and this session ran outside it; more to the point, the brief forbids running the staged slice, so it was left alone |

## The figures the registration would be argued from

**These came back exactly, every one of them:**

- The separable arm reads **0.0000** on all three seeds — whole-state
  transplant 1.0000, ownership-only transplant 1.0000, no-transplant rate
  0.0000.
- The three readings of the read's label, on the arm whose answer is in a known
  place: the agent's slot at **0.0117 / 0.0000 / 0.0000**, the marker's rank at
  **0.0050 / 0.0183 / 0.0117**, which marker word at **1.0000** on every seed.
- The degrees those produce: **0.9883, 0.9950, 1.0000, 0.9817, 1.0000,
  0.9883** — the range 0.9817 to 1.0000 that the findings put beside an arm
  whose degree is 0.0000 by construction.
- Two of the three fits: the agent's slot at **0.256** on all three seeds, and
  which marker word at **1.000** on all three.
- The rank curve: **0.1517 / 0.1417 / 0.1667** at rank 1, **0.3350 / 0.3950 /
  0.3350** at rank 2, **0.7783 / 0.8467 / 0.8717** at rank 4 and exactly
  **1.0000** at rank 8.
- All seven controls on the separable arm, including control 6 discriminating
  perfectly — nothing moves in the same-value cell, everything moves in the
  different-value cell, on 81 and 719 trials.
- The separable arm on marker words it has never seen: **0.7612, 0.6512,
  0.6512**.
- The two negative readings, **−0.1706 and −0.2755**.
- The name-only solver at **0.2380 and 1.0000**.

**These did not.**

### 1. The entangled arm's reading — moved by up to 0.05

| seed | committed | re-run |
|---|---|---|
| 0 | 0.8727 | **0.8565** |
| 1 | 0.8848 | **0.8537** |
| 2 | 0.8801 | **0.8295** |

### 2. The freely trained arm's reading — moved by up to 0.044

| seed | committed | re-run |
|---|---|---|
| 0 | 0.8863 | **0.8758** |
| 1 | 0.8366 | **0.8376** |
| 2 | 0.8499 | **0.8939** |

The **finding** both tables support survives: the separable arm still reads
exactly zero, the other two still read between 0.83 and 0.89, and the free arm
still sits inside the entangled arm's range rather than between the two
anchors. What does not survive is any particular decimal. A registration that
quotes 0.8727 as a measured property of the entangled arm is quoting a number
the code will not produce again.

### 3. One of the three fits — small but real

The marker's rank fits at **0.706 / 0.694 / 0.700** in the record and at
**0.711 / 0.694 / 0.694** in the re-run. Two of the three moved, by about half
a hundredth.

### 4. The learn-both gate — every cell on two arms, and the largest single move in the whole comparison

The free arm at seed 0 reads **0.2547** on the named-other condition in the
record and **0.3470** in the re-run. That is a move of more than nine
hundredths on the one condition the rehearsal reports as failing, and it is
three and a half times the largest move anywhere else.

The rehearsal's verdict on that item still holds in the re-run — each of the
two arms clears the bar of 0.2630 on exactly one seed of three, which is what
the record says — **but it is a different seed each time.** In the record the
entangled arm clears on seed 2 and the free arm on seed 1; in the re-run the
entangled arm clears on seed 0 and the free arm on seed 0. Any sentence in the
registration that names *which* seed cleared is naming an accident.

### 5. The attenuation check reverses — this is the most serious of the differences

This is the check that confirms the first of the two findings the proposal
review marked fatal: that the reading divides by an accuracy that has not had
the no-transplant rate taken out of it. Its pre-stated fail line is "the
registered form is the flatter one".

| arm and seed | committed | re-run |
|---|---|---|
| entangled, 0 | floor-corrected | **the registered one** |
| entangled, 1 | floor-corrected | **the registered one** |
| entangled, 2 | floor-corrected | **the registered one** |
| free, 0 | floor-corrected | **the registered one** |
| free, 1 | the registered one | the registered one |
| free, 2 | floor-corrected | floor-corrected |
| separable, all three seeds | dead heat | dead heat |

The record reports this check as failing its pre-stated line on **one** arm and
seed, and says so plainly, which was the right thing to do. In the re-run it
fails on **five**. On real forward passes the re-run points the other way from
the record.

Two things keep this from being fatal to the finding itself, and both belong
in any account of it. The made-up-populations check, which uses no model at
all and is **byte for byte identical** between the two runs, still returns the
true share of 0.5018 and 0.5013 where the registered form returns 0.4323 and
0.3222. And on the separable arm the two forms are the same arithmetic and
cannot disagree. So the case for the correction rests on the model-free
evidence, which is solid and repeatable; the supporting evidence from real
forward passes is not repeatable, and in this run it points the other way.

### 6. A pre-stated pass turns into a fail, and the "worst miss" vanishes

The free arm at seed 2 passes the proposal's no-transplant sanity rule in the
record and fails it in the re-run. And the record's sharpest sentence about the
review's replacement formula — that its worst miss is **0.0762 measured against
0.0587 predicted**, about a third of the value being predicted — does not
reproduce. In the re-run that same arm and seed reads 0.0563 against 0.0607
predicted, a miss of forty-five ten-thousandths. The largest miss anywhere in
the re-run is 0.0117, on a different arm. The record's claim is true of the
record and not true of the code.

### 7. The budget question reverses direction

The record says doubling the training budget moved the named-other condition
from **0.2547 to 0.2657** — up about a point, which is the basis for "more
steps do not fix it". In the re-run the same arm's ordinary-budget figure is
0.3470 and its doubled-budget figure is **0.2717**, so doubling the budget
moved it *down* by three quarters of a point. The conclusion the record draws —
that the shortfall is not mainly a budget limit — is if anything strengthened,
but the arithmetic behind it compares two numbers that each wander by more than
the difference between them. **This comparison cannot carry the weight the
findings put on it**, and that is a limit of the method rather than a mistake
in the record.

### 8. Smaller moves

- The throughput ratios, 0.981 and 1.049 in the record, are 0.989 and 1.066 in
  the re-run. The conclusion — about five per cent, not the 1.55 the money
  estimate inherited — is unharmed.
- The control for transplanting before the identity can be known reads 0.065
  and 0.060 on the two non-saturating arms in the record and **0.1675 and
  0.1625** in the re-run. The record's reading of it as "nothing happens" is
  comfortable at 0.06 and much less so at 0.17, which is above the
  one-in-eight level a guess over the eight value slots reaches.
- The across-seed spread, 0.0189 and 0.0227 in the record against a
  within-seed figure of 0.0198 and 0.0203, becomes 0.0156 and 0.0102 against
  0.0200 and 0.0197. The record's useful finding — that the two ways of
  measuring the spread "agree closely" — is weaker in the re-run, where one of
  them is half the other.

## Which is right, the record or the re-run?

**Neither, and that is the finding.** For the separable arm the question does
not arise: the two agree exactly. For the entangled and free arms, both runs
are honest single draws from a process that gives a different answer every
time, and a third run gave a third answer again. No amount of re-running will
decide between them, because there is nothing there to decide.

What follows is not a correction to any number. It is that **the registration
cannot quote a decimal place from either of the two non-saturating arms as a
property of the code.** What those arms support is a range and a direction —
"between about 0.83 and 0.89", "at the entangled end rather than between the
anchors", "clears the bar on one seed of three" — all of which held across all
three runs. The exact figures are not the instrument's output; they are one
sample of it. Nothing here needs fixing before that is understood, and this
session fixed nothing.

## A separate finding: the committed self-test record is stale

This one has nothing to do with drift and would have been found without any
training at all.

The committed self-test record (`out/self-tests.txt`) reports **63 passes**.
Running the same self-tests against the committed code today gives **64**, and
the difference is one specific check:

    committed:  fresh episodes use markers and items seen in neither other set
    today:      fresh episodes are combinations seen in neither other set
                the unseen-vocabulary pool shares no marker word or item with training

The history explains it exactly. The self-test record was written by the commit
that ran every self-test into the record (`623ef23`). The episode generator was
then changed by the commit that landed the results (`6e8cc08`) — the change that
split the freshness requirement into fresh *combinations* of seen words and a
separate pool of *unseen* words, which is departure 4 in the findings' own
appendix. The self-test record was never regenerated afterwards.

So the committed self-test record describes a version of the generator that is
not the committed one. Nothing it claims is false — all 63 passed then and all
64 pass now — but it is evidence about older code, and the protocol's whole
point is that the record is evidence about the code that is there. **Reported,
not fixed.**

It is also the one piece of good news in the comparison: the results themselves
were produced with the current generator, not the old one. If they had not
been, the computed solver and the two model-free checks could not have come
back identical.

## What was run, and what it cost

In a scratch copy at `~/.cache/mvm-rehearsal-verify/`, from the committed code,
against the repository's own Python environment:

    sh run_self_tests.sh
    python rehearse.py    --stage all
    python denominator.py --stage all
    python negative_case.py
    python budget_check.py
    python summarize.py

and then, to settle whether the drift was in the code or in the running of it,
the separable, entangled and free arms trained once more at seed 0.

Laptop only. **No machine was rented, no vendor was contacted, nothing was
spent, and the staged slice of rented time was not run and not touched.**
Nothing under `experiments/rehearsal-successor-measure/` was modified.
