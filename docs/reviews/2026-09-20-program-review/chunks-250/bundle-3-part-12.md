
### F5 — The numerator on the seen seeds is already in committed records, including the control under the lesion

**Severity: serious. MEASURED.**

§5.5 commits that "the separation statistic is not computed on seeds 0,
1 or 2 at any point before the registration commit and the lock" and
that the calibration uses "not their battery scores, not their measured
noise, not their damage records." But the endpoint records for all
three seen seeds already store the control battery's score **under the
input-channel lesion**, across six evaluation seeds at 800 episodes:

| checkpoint | control intact | control under the lesion | record |
|---|---|---|---|
| pilot (seed 0) | 0.2877 | 0.2283 | the pilot's endpoint validation record, `a3-gates/endpoint_validation_pilot.json` |
| seed 1 | 0.3057 | 0.2342 | the seed-1 endpoint record, `a3-gates/endpoint_a3_30m_seed1.json` |
| seed 2 | 0.3195 | 0.2617 | the seed-2 endpoint record, `a3-gates/endpoint_a3_30m_seed2.json` |

The same records hold the primary and state batteries intact and under
the lesion. The endpoint findings quote the intact column and omit the
lesioned column, but the numbers are in the committed files, and the
proposal's C1 quotes those same records. So the sign and approximate
size of the separation on the seen seeds, about 0.30 raw in the
numerator, is known to whoever wrote §5, whether or not a script named
"separation" was ever run. The commitment not to compute the statistic
protects only the per-cell pairing and the exact spread. The ruling
annotation's addition, "the prior is stated now: H_self-location is the
predicted cell", is the honest form of this and should be the
registered one: **pre-state the expected value of S on the fresh seeds
from the seen record, and say what result would surprise.** A
prediction made from data in hand is fine when labelled; a claim of
ignorance is not.

### F6 — σ is self-normalizing, so the calibration decides nothing, and the quantity that decides is unspecified

**Severity: fatal against §5.5 as a calibration. ARGUED, with
arithmetic.** *(The ruling annotation on disk says the other pass
reached "the threshold lands near 2" too; this pass reached it
independently and adds the second half, which is where the fitting risk
actually lives.)*

§5.4(a) and §5.5 define, on each calibration substrate: run the random
sweep; for each draw compute the mean of the per-cell difference; take
the standard deviation of that mean across draws as the spread; divide
each draw's mean by the spread to get that draw's S; take the 95th
percentile of |S|. But a set of numbers divided by its own standard
deviation has a 95th percentile of its absolute value near 2 whenever
the numbers are roughly bell-shaped, and near 1.6 to 2.3 across the
shapes 20 to 120 draws can take. **The threshold is a property of the
shape of the null, not of the substrate.** Calibrating it on twins, an
untrained model, or the seen seeds gives the same number to within a
few tenths. Excluding the seen seeds from this step protects nothing,
because the step determines nothing. "The maximum across substrates"
picks whichever null had the heaviest tail, which is not what "most
permissive substrate" means.

What actually sets the bar is the spread used **when S is read on a
fresh seed**, and §5.1 defines it only as "the standard deviation of
that same mean across the matched-strength content-blind random-damage
baseline." It does not say:

1. **On which checkpoint** the spread is measured for a fresh seed: on
   the fresh seed itself (a within-run random sweep after the lock), or
   frozen from the calibration substrates. The two differ a lot: Gate 0
   measured a non-learning twin's null band on a self battery at 0.379
   corrected against 0.0095 on a binder, and an unlearned model's
   answers flip under random damage far more than a learned model's in
   raw terms too. Frozen from twins, the spread is inflated and S on
   the fresh seed is deflated; measured on the fresh seed, the whole
   construction is a within-run z-test with a threshold of 2 that could
   have been written down in one line.
2. **Over which draws**: the 120 draws pooled, or per layer-rank-
   operator cell of 20. Random damage at rank 16 in layer 3 moves
   batteries more than rank 4 in layer 8; the pooled spread and the
   per-cell spreads differ by a factor, and "the" spread is whichever
   is chosen.
3. **Whether the spread is across draws or across cells.** The text
   says across draws; a reader of §5.1 alone could take the spread of
   D(e) across the 400 cells, which is a different quantity by a factor
   of about 20.

Each of these is a choice that can be made after seeds 0 to 2's random
draws have been looked at (they have been, F7), and each moves S by a
multiplicative factor. This is the route by which the clause can be
fitted, and the seeds 0 to 2 exclusion in §5.5 does not close it,
because it is not in the calibration step.

### F7 — The seen seeds' random-damage draws already exist and were the source of the A3 lock

**Severity: worth noting. MEASURED.**

The A3 pilot's null-calibration record
(`null-calibration/a3_pilot_seed0.json`, 120 draws, 800 episodes, 6,047
seconds on the Mac) stores for every draw the raw accuracy of all four
batteries, including the control. The spread §5.1 divides by is, by
definition, the spread of those raw accuracies' difference across draws
on a checkpoint. So the "measured noise" §5.5 says it excludes is
already on disk for seed 0, it was read to cut John's committed lock of
2026-09-16 (`null-calibration/theta_delta.lock.json`), and its band on
the primary battery, 0.1777 corrected, about 0.049 raw at the 95th
percentile, is quoted in the proposal. The 800-episode and 400-cell
sizes, the choice of spread rather than ceiling in the denominator, and
the expectation that the input-channel lesion clears the bar were all
made with that band visible. None of that is a sin. Writing "on no
other data" as though it were not is.

### F8 — The engagement precondition certifies nothing, and the admitted data-informed choices should be named as such

**Severity: worth noting. ARGUED.**

Condition (d) requires the control's intact score to exceed chance by
0.10, so 0.225. The registered name-blind reference solver scores
0.3227 on this battery, and the control diagnostic of 2026-09-17
(`control-diagnostic-findings.md`) found the seen models bind by name,
partially, and land near that level by coincidence. A checkpoint can
therefore pass "engaged" while scoring below a solver that cannot read
the name in the question. As a floor it certifies that the model is
doing something above guessing; it does not certify that the
comparator can register damage to name-keyed binding, which is what a
comparator is for. The proposal says plainly it knows the margin passes
on all seen seeds and that the second comparator was added knowing
which battery learned; those admissions are the right practice, and
the registered text should carry them, not just the memo.

---

## (c) Ways a verdict later gets over-read

### F9 — The positive cell carries the registered positive bin's name

**Severity: serious. ARGUED.**

A3's H_self-location required a localized subspace, the swap probe,
convergence and the tag discriminator, and read "the network acquired a
structure that indexes its binding to its own center". A4's
H_self-location requires (a) to (h) on the input-channel lesion and,
by §5.7, must not be read as any acquired structure at all. Same
label, weaker claim, and the weaker claim is the one that will be
produced. §5.7 is a paragraph; the cell name is what goes in the
results table, the status file and the write-up's first sentence. The
cell should be named for what it measures, on the order of "the
ownership input is specifically load-bearing for the self-directed
condition", and H_self-location should stay reserved for the registered
localized result.

### F10 — The "located, wrong structure" cell is redefined

**Severity: serious. ARGUED against the ruling text.**

John's ruling of 2026-09-19 (the sensitivity rule, recorded in
`STATUS.md` §5 of the 2026-09-19 section) defines the fourth cell as:
"probe passes and the ablation *improves* the primary battery beyond
noise = located, wrong structure." §5.2's table defines LOCATED, WRONG
STRUCTURE as S at or below minus σ, "the damage hurts the other-directed
condition *more*", and says it "carries over the fourth cell added by
the 2026-09-19 ruling." Those are different events. Under §5.2 an
improvement of the primary battery is excluded from the positive cell
by (b), excluded from generic binding by the same sign requirement, and
lands in the wrong-structure cell only if the separation happens to
fall below minus σ; a small or moderate improvement lands nowhere
(F13). The ruled event has lost its cell while its name was reused for
another. This is the kind of drift the "annotate, never rewrite" rule
exists to catch, and it should be corrected before the text is
registered rather than after a result lands in it.

### F11 — The magnitudes that will be reported invite a many-sigma reading

**Severity: serious. ARGUED.**

By F1's arithmetic, S under the input-channel lesion on a checkpoint
like the seen ones is of order 10, and could be 20 or more if the
within-run spread is small. Reported as "S = 18 against σ = 2.1" it
reads as nine standard deviations of evidence for a self-index. What it
is evidence of is that an input the task was built to require is used
by the model that learned the task, which C1 already established at
seven to nine times a locked threshold. The partial-damage ladder,
reported on the same lesion, will be monotone almost by construction,
because scaling an input's projection by 0.75, 0.5, 0.25 and 0 is a
smooth reduction of the same signal; a clean curve will then be shown
as dose-response evidence of a structure. Two pre-statements would
inoculate: the expected S from the seen record (F5), and the minimum
S reachable under the null hypothesis on this checkpoint (F1's bound
when the control collapses to chance), so a reader can see how far
above "could not lose" the observed number sits.

### F12 — Five of five, and generic binding "ruled out"

**Severity: serious. ARGUED.**

Condition (i) of the recommendation scores seeds 0 to 2 after the
verdict "as a consistency check". Their sign and size are known now
(F5), so they are not checks; adding them to the fresh three produces
"five of five seeds" in a table, and the distinction between seen and
fresh will not survive a second retelling. Report them under a separate
heading, labelled seen and verdict-free, never in the same table.
Likewise, the generic-binding cell not firing will be read as "generic
binding was tested and ruled out". F1 says it could not have fired on
this comparator. The write-up must say which cells were reachable on
the checkpoint read, not only which fired.

---

## (d) Ways no verdict is produced on seeds 3 to 5

### F13 — The outcome table does not partition the outcomes

**Severity: serious. ARGUED.**

§5.2 says "with no dead cell in the set". Four outcomes have no cell:

1. **(a) holds but (c) fails**, the state comparator not reaching σ.
   Not the positive cell (needs all), not generic binding (needs S
   below σ), not wrong structure, not NOT TESTABLE (which names only
   (d), (f) and (g)).
2. **(a) holds but (e) fails**, a control lesion reaching σ. Same gap.
3. **The primary battery improves inside the band**: mean self-directed
   drop at or below zero with S above minus σ. Excluded from every
   named cell by sign.
4. **Two seeds of three satisfy the clause**, or one seed is NOT
   TESTABLE and two pass. (h) requires all; the A3 bins "seed-dependent"
   and "unstable" are not carried into the table.

Red-team pass 3 found the same defect in A3's bins (RT-22, bins neither
exhaustive nor exclusive) and it was fixed by adding cells. The same
fix is needed here before registration, because an outcome with
nowhere to land gets explained away, as the registration revisions of
A3 put it.

### F14 — Condition (e) fails by construction, and half of it cannot be evaluated

**Severity: fatal as written. ARGUED.**

(e) requires that "neither the matched other-agent damage test nor the
random matched-subspace damage tests may themselves reach σ on the
self-directed query."

- The random matched-subspace draws are the population whose 95th
  percentile σ is. On the checkpoint being read, a fresh sweep of 120
  draws will produce about six that exceed σ if the read checkpoint's
  null has the same shape as the calibration substrates', and more if
  it is wider (F6 says it may be). Read literally, (e) fails on every
  checkpoint. It needs a quantifier: the 95th percentile of the fresh
  sweep, the median, or all draws below some other bound.
- "Reach σ on the self-directed query" applies a separation threshold
  to a single-condition quantity. Either it means S computed with the
  random draw as the damage operation, in which case it is the same
  test as (a)'s null, or it means the self-directed drop alone against
  σ, which is in different units.
- The matched other-agent damage test requires an other-index subspace
  localized for a named non-self agent (A3 §3.1, L2a). The localization
