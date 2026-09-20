revision position) and the other-directed query (the control battery,
asking the same rule's verdict for a named other agent on an item that
agent did not revise). Episodes in which the model does not revise carry
no self-directed query and are excluded. At 800 episodes, about 400
matched cells result, which is the registered verdict size.

**Damage operation.** Written `L` below. The clause is written once and
applies to whichever damage operation is being read — the input-channel
removal (zeroing the acting channel) or a localized-subspace removal.

For each matched cell `e`, with every score being 1 for correct and 0 for
incorrect:

- `Δself(e)` = self-directed score intact − self-directed score under `L`
- `Δother(e)` = other-directed score intact − other-directed score under `L`
- `D(e)` = `Δself(e) − Δother(e)`

**Separation score.**

    S(L) = mean over cells of D(e)  ÷  spread_null(L)

where `spread_null(L)` is the standard deviation of that same mean across
the matched-strength content-blind random-damage baseline described in
§5.4 — random removals of the same rank and the same norm, at the same
layers, which should not move behaviour.

**No ceiling appears anywhere in `S`.** Its denominator is a measured
spread, not a distance to a ceiling, so it cannot go to zero by
construction the way the registered clause did. It is measured rather
than asserted, and every record stores the baseline it used.

### 5.2 The clause

> **H_self-location (ownership-specific damage).** Under damage operation
> `L`, on a given checkpoint, the clause holds when **all** of the
> following hold:
>
> **(a) Separation.** `S(L) ≥ σ`, where `σ` is the separation threshold
> locked under §5.5 before any fresh checkpoint is read.
>
> **(b) Direction.** The mean of `Δself(e)` is greater than zero. An
> improvement never counts as damage. *(Carries John's 2026-09-19 signed
> degradation ruling into the new clause.)*
>
> **(c) Second comparator.** The same statistic, computed with the
> ownership-free **state battery** in place of the other-directed query
> and paired within the same episodes, also reaches `σ`. The state
> battery is ownership-free and, unlike the control battery, it learned;
> the control battery is ownership-free and content-matched. **Both are
> required**, so that the verdict cannot rest on a comparator that is
> matched but inert, nor on one that is lively but unmatched.
>
> **(d) Engagement precondition.** The other-directed query's intact
> score must exceed its chance floor of 0.125 by at least **0.10**, the
> registered floor margin, reused unchanged. If it does not, the
> checkpoint is **NOT TESTABLE** on this clause and no verdict is read
> from it.
>
> **(e) Controls, unchanged from the registration.** Neither the matched
> other-agent damage test nor the random matched-subspace damage tests
> may themselves reach `σ` on the self-directed query.
>
> **(f) Validity gates, carried over verbatim from Amendment A3 §3.3.**
> The neutral-episode likelihood bound, the long-generation degeneracy
> probe, and the out-of-distribution-inconclusive branch for any damage
> operation that breaches them.
>
> **(g) Within-run baseline.** The observed `S(L)` must fall outside the
> 95% band of the condition-shuffling baseline of §5.4(b), computed on
> the checkpoint being read.
>
> **(h) Across seeds.** The clause is read on fresh checkpoints only —
> seeds 3 and 4 — and must hold on **both**.
>
> **Sample size.** At least 800 episodes, with intact and damaged
> readings taken on the same episodes, per the 2026-09-19 ruling.

**The outcome cells, with no dead cell in the set:**

| cell | condition | reading |
|---|---|---|
| **H_self-location** | (a) through (h) hold | the damage is specific to the ownership-dependent condition on matched content |
| **H_generic-binding** | mean `Δself` > 0, and `S(L) < σ` | the damage hits self- and other-directed binding alike: a "who did what" tracker, not a self-index |
| **LOCATED, WRONG STRUCTURE** | `S(L) ≤ −σ` | the damage hurts the other-directed condition *more*; carries over the fourth cell added by the 2026-09-19 ruling |
| **NOT TESTABLE** | (d), (f) or (g) fails | reported as such, with the failing condition named |

The second row is the point of the repair. Under the registered clause
the generic-binding cell **could not fire**, because it was defined by a
difference one of whose terms did not exist.

### 5.3 What is *not* changed

The grammar, the tokenizer, the trainer, the frozen batteries, the cue
gates, the attack sweep, the null-calibration script, the lock guard and
the launcher are all unchanged and keep their registered status. The
corrigibility commitments are unchanged. The $100 A3 hard stop is
unchanged and A4 spends inside it. The primary battery's locked bite
threshold of 0.1777 is unchanged and keeps governing the primary result;
the separation threshold is a **second, separate** number, and neither
replaces the other.

### 5.4 The baselines against which the score is judged

Two, and both are pre-stated.

**(a) The matched-strength content-blind random-damage baseline — sets
the threshold.** The Gate 0 machinery, reused unchanged: layers 3, 4, 5,
7 and 8; ranks 4, 8 and 16; the two residual operators (random-mean and
random-noise); 20 seeds; 95th percentile. For each draw, recompute the
mean of `D(e)` over 800 episodes. The spread of that quantity across
draws is `spread_null`, and the 95th percentile of the absolute
separation score is what `σ` is set from. This baseline answers: *how
large a separation appears when this much damage is done to something
that is not ownership?*

**(b) The condition-shuffling baseline — a within-run check.** Shuffle
the self/other labels across matched cells and recompute the separation
score, 1,000 shuffles. This baseline answers: *how large a separation
appears when the damage is real but the two conditions are
interchangeable?* It is computed on the checkpoint being read, after the
lock, so it cannot be fitted to. Condition (g) requires it to be cleared.

### 5.5 Threshold calibration — twin and untrained checkpoints only

**The rule.** `σ` is calibrated on checkpoints from which no verdict is
ever read, and **on no other data**. Seeds 0, 1 and 2 are excluded
entirely: not their battery scores, not their measured noise, not their
damage records.

**The three calibration substrates**, all local, inference-only, no
spend:

1. **The register-less twin checkpoint from the earlier wave, seed 0**
   (`artifacts/pilot_a1_30m_seed0_twin/pilot_a1_30m_seed0_twin.pt`).
2. **The register-less twin checkpoint from the earlier wave, seed 1**
   (`artifacts/pilot_a1_30m_seed1_twin/pilot_a1_30m_seed1_twin.pt`).
3. **An untrained model at the A3 twin configuration** — the same
   architecture, randomly initialized at a stated seed, never trained.
   Constructed locally at no cost; it carries no learned ownership
   structure by construction, so any separation it shows is machinery and
   noise.

The two twins are trained models, but they were trained on the *earlier*
grammar, so on the A3 batteries they are out of distribution and the
amendment already labels them exploratory-only with no verdict readable
from them. Gate 0 used the existing checkpoints as its calibration
substrate in exactly this way, so this is the precedent rather than a new
liberty.

**The procedure.**

1. On each of the three substrates, run baseline (a) at every
   layer/rank/operator combination at 800 episodes and record the
   distribution of the separation score.
2. Set **`σ` = the maximum, across the three substrates, of the 95th
   percentile of the absolute separation score**, rounded up to three
   decimal places. The maximum, not the mean: the most permissive
   substrate sets the bar, so the threshold cannot be softened by
   averaging in a quiet one.
3. Write `σ` into a lock file through the existing lock-guard machinery,
   carrying the hash of the calibration record it came from, the
   checkpoints it was computed on, and a field recording the exclusion of
   seeds 0, 1 and 2 — so the exclusion is checkable rather than asserted.
4. **John commits the lock**, as he committed the existing one. The
   scoring script refuses to run without a valid lock, by the same
   mechanism that already enforces this.

**Written discipline commitment, to be part of the registered text.** The
separation statistic is **not computed on seeds 0, 1 or 2 at any point
before the registration commit and the lock**. Computing it would be
seeing which way the new measure cuts on data already in hand, which is
the move C4 forbids. After the verdict is read on seeds 3 and 4, the
three seen checkpoints may be scored and reported as a consistency check,
labelled as such, never counted toward the outcome.

**Honest limitation of this plan.** The two twins learned a different
task, so the baseline they produce is a noise floor for the *machinery*
of the statistic rather than for a model that learned this objective. A
model that learned more may wobble more, which would make `σ` too
permissive. Two pre-stated mitigations: taking the maximum across three
substrates rather than an average, and requiring condition (g), the
within-run condition-shuffling check, which is measured on the very model
being read and is unavailable to fitting because it comes after the lock.

**On the one number in the clause I did not calibrate.** The engagement
precondition in (d) uses 0.10 above chance. I did not derive that from
the calibration substrates; it is the **registered floor margin, reused
unchanged**, on the same principle that kept the noise-band kill
criterion (K0) at 0.25 after Gate 0 measured the band at about 0.01 — a
pre-stated number keeps its value once you have looked. Stated plainly
so John can weigh it: **I already know this precondition passes on all
three seen checkpoints**
(their intact control scores are 0.288 to 0.320 against a chance floor of
0.125, so margins of 0.16 to 0.19). It is therefore not a live gate on
this wave; it is discipline for any future design, and a reader is
entitled to know I knew that when I wrote it.

### 5.6 Optional bite criterion — the partial-damage ladder

From item 4 of the Pain Axis research note, and the one question John's
2026-09-19 ruling left open.

**What it is.** Instead of one crossing of a threshold, grade the damage:
retain fractions 1.00 (intact), 0.75, 0.50, 0.25 and 0.00 (full damage).
At each rung, compute the self-directed degradation relative to intact,
and the separation score.

**The pre-stated requirement.** The self-directed degradation must be
**non-decreasing as the retained fraction falls**, with ties allowed
inside a tolerance `τ` equal to one standard error of the paired mean at
400 cells, measured on the calibration substrates and locked with `σ`. A
single step that goes the wrong way by more than `τ` fails the ladder.
The full-damage rung must also clear `σ`.

**Why it is worth having.** A curve with a required direction is far
harder for evaluation noise to fake than a single crossing. The noise is
not small relative to the threshold: the bite threshold is about 0.038
raw battery points on this checkpoint, against evaluation spread of
0.0284 at 400 episodes and 0.0169 at 800.

**Cost: $0.** It is local inference on checkpoints already fetched — five
evaluation passes instead of two. No GPU, no pod, no spend.

**Recommended status: run it, report it, do not make it binding on this
wave.** Making it binding adds a second newly-calibrated quantity (`τ`)
to a clause that is already new, and a criterion that has never been run
should not decide a verdict the first time it runs. So: registered as a
**reported** criterion on seeds 3 and 4, with whether it becomes binding
left to a later ruling that carries its own fresh-seed requirement.
*(This is my call, not a ruling; confidence moderate. The strongest
alternative is to make it binding now on the grounds that it is strictly
more informative than a single threshold and costs nothing — I did not
take it because a criterion's first run should not also be its first
verdict.)*

### 5.7 Registered limitation, to be stated in the amendment

> Amendment A4 repairs the **comparison**. It does not repair the
> **localization**. A positive result under removal of the input channel
> says that the ownership input is specifically load-bearing for the
> ownership-dependent condition on matched content — which is more than
> the earlier result said, because it controls content and the rule, but
> it is **not** evidence that the network built an internal structure
> carrying ownership. That question belongs to the localized-subspace
> work, whose instrument has so far found nothing anywhere and remains
> unvalidated at this scale. Any write-up that reads an A4 positive as
> an acquired internal structure is misreading it.

---

