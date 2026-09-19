# Amendment A4 to MVM-0a: a comparison that can be computed

> # WITHDRAWN — NOT REGISTERED, AND NOT A CANDIDATE
>
> **Ruled by John, 2026-09-19 (second ruling of the day).** The
> independent red-team pass (`red-team-a4.md`, 22 findings, merged to
> main at `770c142`) is **fatal on F1, F2, F6, F14 and F15**. Amendment
> A4 is not registered and the seeds 3, 4 and 5 wave does not launch.
> **A3 stays open, not closed.**
>
> This file is parked on this branch so the work is not lost and cannot
> be mistaken for registered text. **It is not a draft awaiting repair.**
> John's instruction was explicit: no version two tonight. Anyone
> picking this up should read `red-team-a4.md` first, and in particular
> should not assume the five fatal findings are patchable.
>
> The five, in one line each:
>
> - **F1.** Under the input-channel lesion the generic-binding cell is
>   arithmetically **unreachable**: the comparator has about a fifth of
>   the self-directed battery's room to fall, so the clause can only
>   lose if an already replicated result fails to replicate a fourth
>   time.
> - **F2.** "Matched content" is not a matched condition. The
>   self-directed score is read at the own revision position — exactly
>   where the lesion strikes — and the other-directed score at a
>   question appended after the episode. A position-local disruption
>   carrying nothing about ownership satisfies the clause.
> - **F6.** The threshold is self-normalizing and lands near 2 on any
>   substrate, so the calibration decides nothing; the quantity that
>   actually decides is left unspecified and therefore choosable after
>   the lock.
> - **F14.** Condition (f) fails by construction: the random
>   matched-subspace draws *define* the threshold as their own 95th
>   percentile, so one draw in twenty exceeds it.
> - **F15.** Two of the three calibration substrates cannot run at all.
>   The twins use a different tokenizer. **Verified independently:** 70
>   of the 103 shared tokens carry different ids, two A3 tokens have no
>   id in the twins' vocabulary, and their embedding table is 103 wide
>   against A3's 105.

**STATUS: WITHDRAWN. NOT REGISTERED.** *(The line below is the text as it
stood when the ruling came; it is left unedited.)*

**STATUS: DRAFT, NOT REGISTERED.** This text becomes registered when it
is committed, and **the registration commit is held** at John's
instruction of 2026-09-19 until the findings of an independent red-team
pass, running in another session, are handed over and folded in. Nothing
in this document authorises spend. Nothing launches without John's go in
his own words, quoted in the ledger row.

*Drafted 2026-09-19 against John's ruling of the same day, after
red-team pass 1 (`a4-red-team-pass-1.md`, fifteen items, all folded in
below). Proposal it comes from:
`docs/control-clause-proposal-2026-09-19.md`.*

---

## 0. John's ruling, quoted

> "B: register Amendment A4. Three fresh seeds, 3, 4 and 5, as one wave.
> The partial-damage ladder is reported on this wave, not binding. Order:
> registration commit before launch; the threshold lock before any
> endpoint is read, and the registration states that order explicitly.
> Two additions to the registered text: (1) state the prior now, before
> the seeds exist: under input-channel removal, H_self-location is the
> predicted cell, and the informative application of this clause is a
> localized-subspace lesion; (2) require the measured spread of Δother to
> be reported alongside the verdict, so a comparator that did not fall is
> a number, not a sentence. Hold the registration commit until I hand you
> the findings from an independent red-team pass running in another
> session; fold in anything it catches, then proceed to steps 2 through 6
> of §8. Nothing launches without my verbatim go."
> — John, 2026-09-19

---

## 1. Why this amendment exists

The registered Amendment A3 clause for the central prediction asked for
the primary battery's damage **minus the control battery's**. Measured on
2026-09-17 (`ceiling-measurement-findings.md`), the control battery's
ownership-blind ceiling — the score reachable by a solver that knows
nothing about which agent the model is — is **1.0**, reached
independently by two solvers. The registered damage measure divides by
the distance from a battery's score to that ceiling and requires that
distance to be at least 0.10, so a defined figure for the control needs a
score of **1.10**. No model can reach it. **The clause was unsatisfiable
from the day it was registered**, months before a checkpoint existed, and
its failure had nothing to do with whether the control battery learned.

The defect generalises: a control designed to be answerable without
ownership has an ownership-blind ceiling of 1.0 by construction, so **a
ceiling-corrected damage measure and an ownership-free control are
incompatible by construction**. Any repair that still divides by a
ceiling distance on the control inherits the same defect.

A4 therefore replaces the measure, not the design.

**The precondition John set on any A4 is satisfied.** He ruled on
2026-09-17 that the control battery's ceiling — registered as verified by
the attack sweep, and never actually verified — must be measured properly
before any amendment opens. It has been. The measuring harness reproduced
both registered known-answer checks to four decimal places before
reporting anything new.

---

## 2. What A4 changes, and what it does not

**Changed:** one clause, and the scoring script that computes it.

**Unchanged, and keeping their registered status:** the grammar, the
tokenizer, the trainer, the frozen batteries, the cue gates, the attack
sweep, the null-calibration script, the launcher, the corrigibility
commitments, the $100 hard stop, and John's existing threshold lock. The
primary battery's locked bite threshold of **0.1777** is unchanged and
keeps governing the primary result; the separation threshold added here
is a second, separate number and neither replaces the other.

**No training change. No grammar change. No re-freezing of batteries. No
new attack sweep.** The matched contrast this clause needs already exists
inside the registered grammar by construction: every episode carries both
the self-directed query, scored at the model's own revision position, and
the other-directed query, asking the same rule's verdict for a named
other agent. Same turns, same items, same rule, same episode — only the
agent whose commitment is queried differs.

---

## 3. Definitions

**Matched cell.** An evaluation episode carrying both queries. Episodes
in which the model does not revise carry no self-directed query and are
excluded. Because the model revises in half of episodes, **1,600
episodes yield about 800 matched cells**, which is the evaluation size
this amendment requires (§3.1).

**Damage operation**, written `L`. The clause is written once and applies
to whichever damage operation is read — removal of the input channel that
tells the model which agent it is, or removal of a localized subspace.

For each matched cell `e`, every score being 1 for correct and 0 for
incorrect:

- `Δself(e)` = self-directed score intact − self-directed score under `L`
- `Δother(e)` = other-directed score intact − other-directed score under `L`
- `D(e)` = `Δself(e) − Δother(e)`

**Separation score.**

    S(L) = ( mean over cells of D(e) )  ÷  spread(L)

    spread(L) = max( spread_null(L) , standard error of the paired mean )

`spread_null(L)` is the spread of that same mean across the
matched-strength content-blind random-damage baseline of §4(a), **measured
on the checkpoint being read**. The standard error of the paired mean is
the ordinary one, computed from the observed per-cell spread of `D(e)` at
the evaluation size.

**The floor under the denominator is load-bearing and is why it is there.**
Random damage at matched strength is chosen precisely because it should
not move behaviour, so its spread can be very small and in a degenerate
case approach zero — and **a denominator that can reach zero is exactly
how the A3 clause died.** Taking the larger of a measured null spread and
a sampling floor cannot vanish for non-degenerate data, and taking the
larger is conservative in the right direction: it makes the clause harder
to satisfy, never easier. Every record states which of the two governed.

**No ceiling appears anywhere in `S`.** Its denominator is a measured
spread with a sampling floor, not a distance to a ceiling.

### 3.1 Evaluation size

**1,600 episodes**, giving about 800 matched cells, with intact and
damaged readings taken on the same episodes. This exceeds the 2026-09-19
ruling's requirement of at least 800 paired readings, and it exceeds it
**in the cells the statistic is actually computed over**, not merely in
episodes. It is local inference on checkpoints already fetched: more
wall-clock, no dollars, no pods.

---

## 4. The two baselines

**(a) Matched-strength content-blind random damage — measured per
checkpoint.** The Gate 0 machinery reused unchanged: layers 3, 4, 5, 7
and 8; ranks 4, 8 and 16; the two residual operators; 20 seeds; the 95th
percentile. For each draw, recompute the mean of `D(e)`. The spread of
that quantity across draws is `spread_null(L)`. It answers: *how large a
mean paired difference appears when this much damage is done to something
that is not ownership?*

**This spread is measured on the checkpoint being read, never inherited
from the calibration substrates of §5.** What is locked in advance is the
**threshold on the standardized score**; what is measured per checkpoint
is the **spread it is standardized by**. Importing a noise estimate from
models that learned a different task would be wrong. Measuring a
content-blind noise null on a fresh checkpoint before its verdict is read
is not fitting, and is what Gate 0 did per checkpoint.

**(b) The sign-flip paired test — a within-run check on the checkpoint
being read.** Randomly flip the sign of each cell's `D(e)`, 1,000 draws,
and take the spread of the resulting means. This tests the null the
clause needs — *the damage falls equally on both conditions, so the
paired difference is centred on zero* — and assumes nothing about the two
conditions having equal base rates. It is computed after the lock and is
therefore unavailable to fitting.

> **Correction on the record.** The proposal this amendment comes from
> specified, at its §5.4(b), a baseline that shuffled the self/other
> labels across matched cells. **That was wrong and is corrected here
> rather than quietly rewritten.** The two conditions are not
> exchangeable — intact, the self-directed query scores about 0.57 and
> the other-directed about 0.30 — so a label shuffle would have tested
> whether those two levels are exchangeable, which they plainly are not
> and which nobody asked. The sign-flip test above is the correct paired
> test. Caught by red-team pass 1, item RT-A4-03.

---

## 5. The clause

> **H_self-location (ownership-specific damage).** Under damage operation
> `L`, on a given checkpoint, the clause holds when **all** of the
> following hold:
>
> **(a) Separation.** `S(L) ≥ σ`, where `σ` is the separation threshold
> locked under §6.
>
> **(b) Magnitude.** The self-directed battery's damage, under the
> registered ceiling-corrected measure, reaches the locked bite threshold
> of **0.1777**. *(The registered instrument and John's existing locked
> number, unchanged. Without this condition the clause would be satisfied
> by a tiny but perfectly specific effect, since every other condition is
> about specificity rather than size.)*
>
> **(c) Direction.** The mean of `Δself(e)` is greater than zero. An
> improvement never counts as damage. *(John's ruling of 2026-09-19.)*
>
> **(d) Second comparator.** The same statistic, computed with the
> ownership-free **state battery** in place of the other-directed query
> and paired within the same episodes, also reaches `σ`. The state
> battery is ownership-free and learned; the control battery is
> ownership-free and content-matched. **Both are required**, so the
> verdict cannot rest on a comparator that is matched but inert, nor on
> one that is lively but unmatched.
>
> **(e) Engagement precondition.** The other-directed query's intact
> score exceeds its chance floor of 0.125 by at least **0.10**, the
> registered floor margin reused unchanged. If it does not, the
> checkpoint is **NOT TESTABLE** and no verdict is read from it.
>
> **(f) Controls, unchanged from the registration.** Neither the matched
> other-agent damage test nor the random matched-subspace damage tests
> may themselves reach `σ` on the self-directed query.
>
> **(g) Validity gates, carried over verbatim from Amendment A3 §3.3.**
> The neutral-episode likelihood bound, the long-generation degeneracy
> probe, and the out-of-distribution-inconclusive branch.
>
> **(h) Within-run baseline.** The observed `S(L)` falls outside the 95%
> band of the sign-flip paired test of §4(b), computed on the checkpoint
> being read.
>
> **(i) Across seeds.** The clause is read on fresh checkpoints only —
> **seeds 3, 4 and 5** — and must hold on **all three**. See §9.

### 5.1 The outcome cells

| cell | condition | reading |
|---|---|---|
| **H_self-location** | (a) through (i) hold | the damage is specific to the ownership-dependent condition on matched content |
| **H_generic-binding** | mean `Δself` > 0, magnitude condition met, and `S(L) < σ` | the damage hits self- and other-directed binding alike: a "who did what" tracker, not a self-index |
| **LOCATED, WRONG STRUCTURE** | `S(L) ≤ −σ` | the damage hurts the other-directed condition *more*; the fourth cell added by John's ruling of 2026-09-19 |
| **NOT TESTABLE** | (e), (g) or (h) fails, or §7.2 applies | reported as such, naming the failing condition |

The second row is the point of the repair. Under the A3 clause the
generic-binding cell **could not fire**, because it was defined by a
difference one of whose two terms did not exist. A design in which the
boring explanation cannot be selected is not a test.

---

## 6. The separation threshold, and the lock

**Calibration substrates**, all local, inference-only, no spend:

1. the register-less twin checkpoint from the earlier wave, seed 0;
2. the register-less twin checkpoint from the earlier wave, seed 1;
3. an untrained model at the A3 twin configuration — same architecture,
   randomly initialized at a stated seed, never trained.

On each, run baseline §4(a) at every layer, rank and operator combination
at the §3.1 evaluation size and record the distribution of `S`. **`σ` is
the maximum, across the three substrates, of the 95th percentile of the
absolute separation score**, rounded up to three decimal places. The
maximum rather than the mean, so the bar cannot be softened by averaging
in a quiet substrate.

**Seeds 0, 1 and 2 contribute nothing to this calibration** — not their
battery scores, not their measured noise, not their damage records. The
lock file records that exclusion as a field, so the claim is checkable
rather than asserted.

**The lock file** gains the separation threshold, the evaluation size,
the matched-cell definition, the substrates used, and the exclusion
field, alongside the existing thresholds. **The lock guard is extended to
refuse a lock that lacks a separation threshold when a separation reading
is what is being asked for** — otherwise a lock with no separation
threshold in it would pass the guard, and the clause would be governed by
intention rather than by mechanism, which is the exact thing the guard
was built to end. **John commits the lock**, as he committed the existing
one.

### 6.1 What the calibration does and does not buy — stated plainly

The separation score is standardized **against its own null**, so under
that null it has a mean near zero and a spread near one by construction,
and the 95th percentile of its absolute value will land **near 2 on any
substrate whatever**. The calibration confirms the machinery behaves and
produces a number locked before the data exists, which is a real
discipline. **It is closer to a formality than the proposal implied, and
the proposal oversold it.**

The protection actually lives in four other places, and the registered
text says so rather than resting on the calibration:

1. the magnitude condition (b), tied to the already-locked 0.1777;
2. the sign-flip paired test (h), computed on the checkpoint being read,
   after the lock, and therefore unavailable to fitting;
3. the second, learned comparator (d);
4. the existing matched-other-agent and random-subspace controls (f).

---

## 7. The prior, stated before the seeds exist

*John's first addition, 2026-09-19.*

### 7.1 The predicted cell, and what a positive there is worth

**Under removal of the input channel, H_self-location is the predicted
cell.** This is recorded now, before seeds 3, 4 and 5 exist.

**And it is therefore weak evidence, which the registered text states so
that no write-up can quote it as a confirmation.** Zeroing the channel
that tells the model which agent it is obviously damages a task that
requires knowing which agent it is; the existing result already shows
that collapse, at seven to nine times the bite threshold, on three
checkpoints. A positive in this cell is **near-certain in advance and is
evidence that the instrument works, not evidence for the hypothesis.**

**The informative application of this clause is a localized-subspace
lesion**, which asks whether the network built an internal structure
carrying ownership rather than whether it uses the input that supplies
it.

### 7.2 If the informative application cannot be run

The localization stack has so far found nothing anywhere: its probes fell
below their own permutation baselines on a checkpoint where ownership is
measured to be load-bearing, the blind arm was not flagged and landed on
the worse half of that outcome, and one damage test improved the battery
it was meant to hurt. There is a live chance there is nothing to lesion.

**Pre-stated now rather than improvised later:** if the localization
procedure's probe fails its own permutation baseline on a fresh
checkpoint, the clause is **NOT TESTABLE** under the localized lesion on
that checkpoint and is reported as such, and the input-channel reading
stands alone carrying the weak-evidence label of §7.1.

### 7.3 Layer and rank selection

The localization procedure selects its layer by probe accuracy over five
candidate layers. Selection inflates false positives, and the defence is
that **this selection is blind to the clause's outcome** — it is made on
probe accuracy using own-agent labels and never sees a battery score. The
layer and rank are fixed by that outcome-blind rule **before** the clause
is read. If the clause is ever read at more than one site, a multiplicity
correction is pre-stated at that time.

---

## 8. Reporting requirements

*John's second addition, 2026-09-19: "require the measured spread of
Δother to be reported alongside the verdict, so a comparator that did not
fall is a number, not a sentence."*

Every verdict carries, for **both** conditions and for the paired
difference — that is, for `Δself`, `Δother` and `D` — all of:

- the intact score and the damaged score;
- the mean change across matched cells;
- the **standard deviation** across matched cells;
- the **standard error of the paired mean**;
- the matched-cell count.

So the sentence "the ownership-free comparator did not fall" never
appears without a mean and a spread attached, and a reader can judge for
themselves whether it *could* have fallen.

The same block is reported for the second comparator of clause (d), and
`spread(L)` is reported with a statement of **which of its two terms
governed** — the measured null spread, or the sampling floor.

---

## 9. Seeds, and the across-seed rule

**Three fresh seeds — 3, 4 and 5 — launched as one wave** (John,
2026-09-19). Three fresh seeds restore the registered across-seed
strength, which the registration set at three.

**The across-seed outcome requires all three fresh seeds to be testable
and all three to hold.** If any one is not testable, the across-seed
outcome is **NOT TESTABLE**, reported as such, naming the seed and the
condition it failed. There is no partial credit and no "two of the three
testable" fallback. *(Claude's call under red-team item RT-A4-06, flagged
as such; John may overturn it. What may not happen is leaving it
unwritten until the data arrives.)*

**The outcome is recorded as "3 of 3 fresh seeds", naming them.** Seeds
0, 1 and 2 are excluded from the outcome by the fresh-seed rule, and any
write-up stating the across-seed result must say which seeds it counted,
which it excluded, and why.

**After the verdict is read**, seeds 0, 1 and 2 may be scored under this
clause and reported as a consistency check, labelled as such, never
counted toward the outcome.

**Discipline commitment, registered.** The separation statistic is **not
computed on seeds 0, 1 or 2 at any point before the registration commit
and the lock.** Computing it would be seeing which way the new measure
cuts on data already in hand.

---

## 10. The partial-damage ladder — reported, not binding

*John's ruling, 2026-09-19.*

**What it is.** Grade the damage rather than applying it whole: retain
fractions 1.00 (intact), 0.75, 0.50, 0.25 and 0.00 (full damage). At each
rung report the self-directed degradation relative to intact and the
separation score.

**What "reported, not binding" means, defined so it cannot drift.** The
five rungs and their numbers appear in the findings. **No outcome cell
turns on any of them.** No sentence in any write-up may present the
ladder as support for a verdict. Whether it becomes binding is a later
ruling carrying its own fresh-seed requirement — a criterion's first run
should not also be its first verdict.

**Cost: $0.** Local inference on checkpoints already fetched.

---

## 11. Order of operations — stated explicitly, as John ruled

1. **Registration commit before launch.** This document is committed
   before any pod is created.
2. **The threshold lock before any endpoint is read.** Training reads
   nothing, so the binding line is *lock before read*, not *lock before
   launch*. The checkpoints take about ten hours to arrive, which is the
   window in which the calibration of §6 runs.
3. Any damage result read before the thresholds are locked **voids the
   lock**, unchanged from the registration, and the lock guard enforces
   it.

**This order is stated here explicitly so that it is a registered choice
rather than a slip**, which is what John's ruling requires of it.

---

## 12. Limitations, registered

**A4 repairs the comparison. It does not repair the localization.** A
positive under removal of the input channel says the ownership input is
specifically load-bearing for the ownership-dependent condition on
matched content — more than the earlier result said, because it controls
content and the rule — but it is **not** evidence that the network built
an internal structure carrying ownership. Any write-up reading it that
way is misreading it. See §7.1.

**No comparator in this design is both content-matched and lively.** The
control battery is content-matched and never learned, scoring 0.288 to
0.320 against a chance floor of 0.125 — roughly what a solver that
ignores the name in the question gets. A comparator answering near the
level of blind guessing may be unable to show damage, in which case the
separation score would be driven almost entirely by the self-directed
side collapsing. The state battery comparator of clause (d) learned and
has room to fall, but is not content-matched. §8's reporting requirement
turns this from a hidden assumption into a visible number. **The gap is
real and is stated rather than managed.**

**Two choices in this clause were made with knowledge of the data.**
Adding the second comparator (d), and setting the engagement precondition
(e) at 0.10 above chance. On (d): it makes the clause *harder* to
satisfy, and a change that raises the bar is not the failure mode the
fresh-seed discipline exists to catch. On (e): 0.10 is the registered
floor margin reused unchanged, on the principle that kept the noise-band
kill criterion at 0.25 after Gate 0 measured the band at about 0.01 — and
**it is already known to pass on all three seen checkpoints**, whose
margins are 0.16 to 0.19, so it is discipline for future designs rather
than a live gate on this wave. Both are stated so a reader knows what was
known when.

---

## 13. Budget

Unchanged caps: the **$100 A3 hard stop** and the wider **$400**
envelope. A4 spends inside both and raises neither, so no cap amendment
is required.

Built from the pilot's measured **0.645 seconds per training step**:

| quantity | figure |
|---|---|
| steps per run | 55,116 |
| training time per run | 55,116 × 0.645 s = **9.87 h** |
| pod time above training | +0.3 to +0.5 h (measured on seeds 1 and 2) |
| pod lifetime per run | **10.2 to 10.4 h** |
| three pods, run concurrently | 30.5 to 31.2 pod-hours |
| rate | $0.99/hour, RTX 5090 secure, EU-RO-1 |
| **central estimate** | **$30.5** |
| **estimate band** | **$27 – $39** |
| storage volume drip | ~$0.15 for the run |

| cap | before | after | headroom |
|---|---|---|---|
| A3 hard stop | $34.31 / $100 | ~$64.8 / $100 | ~$35 |
| wider envelope | $215.7 / $400 | ~$246.2 / $400 | ~$154 |

**Wall clock ~10.2 hours**, so a wave launched tonight reports tomorrow
morning.

### 13.1 Pre-launch checks specific to a three-pod wave

**Three concurrent pods is one more than has ever been run.** Two on one
network volume is confirmed working; three is assumed, not tested.

- Confirm the network volume accepts a **third** attachment before the
  third pod is created. If it does not, **stage the third run rather than
  dropping the volume** — the volume is what makes a pod's death
  survivable, and a lost checkpoint costs a whole run.
- Confirm secure-cloud stock for three machines in the one permitted
  region. Community cloud is not permitted for registered spend.
- **Funding rule:** the balance must cover the estimate plus $10 — about
  **$49** at the top of the band. The balance query returned an HTTP 403
  with the stored key during the last wave, so it must be confirmed by
  another route rather than assumed.
- **Idle billing has cost money on four separate occasions**, and three
  pods triple the exposure. The pod-side reaper is armed in the launcher
  but has **never run in production**; the laptop watchdog is still the
  only reap that has ever actually worked. **Keep the Mac powered and the
  lid open overnight.** A worst case of all three pods billing past
  completion adds roughly $13.

---

## 14. What is registered by this amendment

The clause of §5 and its outcome cells; the definitions and evaluation
size of §3; the two baselines of §4; the threshold and lock procedure of
§6; the prior and its reading rule in §7; the reporting requirements of
§8; the seed and across-seed rules of §9; the ladder's reported-only
status in §10; the order of operations in §11; and the limitations in
§12, which are registered as limitations and not as caveats to be dropped
later.

Plus the scoring script that computes the clause, and the extension of
the lock guard described in §6.

*Everything else in the MVM-0a registration and Amendment A3 stands
unchanged.*
