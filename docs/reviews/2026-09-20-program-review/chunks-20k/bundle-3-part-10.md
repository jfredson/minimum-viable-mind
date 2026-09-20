- The other-directed score is read **at the answer position of a
  question appended after the whole episode** (`model.score_choices`,
  the `<ans>` position), several turns downstream of every injection.
- The self-directed answer requires identifying which of four earlier
  assignments is the model's own; the other-directed answer is one
  visible turn plus the rule, which the ceiling measurement showed a
  name-keyed lookup solves at 1.0.

The input-channel lesion zeroes the injection at the model's own act
positions. It changes the residual stream at the very tokens where the
self-directed score is read and leaves the appended question's tokens
unaltered except through attention. Any disruption that is local to the
altered positions, whether or not it carries anything about ownership,
lowers the self-directed score more than the other-directed one and
satisfies (a), (b), (g) and (h). The random baseline in §5.4(a) cannot
catch this: the Gate 0 operators act at **all** non-pad positions at
layers 3, 4, 5, 7 and 8 (`null_calibration.install_residual`), so the
null describes damage spread evenly, and a position-concentrated lesion
is outside the family the null was drawn from.

The record already says the lesion is at least partly a general
disruption. Under the input-channel lesion the control falls on every
seen seed, by about 0.06 to 0.07 raw (F5), and the state battery, which
has nothing to do with ownership, falls about 0.07 raw on seed 2 (the
corrected drop of 0.0769 reported in the endpoint findings, against a
state-battery range of about 0.93). Everything falls; the clause asks
only whether the self-directed condition falls most, and F1 says it
must.

The registered text already concedes the point for this lesion.
Registration revision 8 of Amendment A3 says the acting channel "marks
positions, and attending back to marked positions is a re-readable
pointer rather than a carried binding. Both routes need the channel, so
the wire lesion cannot separate them." A4 proposes to read its verdict
on the wire lesion.

### F3 — Under a localized lesion, the clause has dropped every discriminator the registered positive bin carried

**Severity: serious. ARGUED.**

The registered H_self-location signature in A3 §3.5 required, besides
the differential: the other-index control (a subspace localized for a
named non-self agent, matched in rank and probe accuracy) below
threshold; the random controls below threshold; the swap probe moving
the action with the patched identity; probe-patching convergence; and
for the tag bin, the mid-episode re-indexing probe. §5.2's cell
requires (a) to (h), none of which is the swap probe, the convergence
requirement or the re-indexing probe. Condition (e) names the other-
agent damage test, but only as a non-firing requirement, and see F14 on
whether it can be evaluated at all.

So under a localized lesion the following satisfy (a) to (h) with no
self-index anywhere:

- **An act-marker echo** (A3 red-team item R1): a subspace carrying
  "this position was enacted", propagated forward. Removing it hurts the
  self-directed query, which needs to find the enacted turn, and not the
  other-directed query, which does not. S is large, direction positive,
  the state battery untouched.
- **A mine-bit tag** (A3 red-team item R4 and the H_tag bin): an
  indispensable address. The registered discriminator for it, the
  re-indexing probe, is not in the clause.

The A4 table has no H_tag cell, no H_self-reference-only cell and no
H_diffuse cell. A localized-lesion positive under A4 is therefore a
weaker claim than a localized-lesion positive under A3, while carrying
the same name (F9).

### F4 — The second comparator fails in the same way as the first

**Severity: serious. ARGUED, with one measured number.**

Condition (c) requires the same statistic with the state battery in
place of the other-directed query to reach σ too, "so that the verdict
cannot rest on a comparator that is matched but inert, nor on one that
is lively but unmatched." The state battery is: not content-matched (it
asks about the last parcel mentioned or a count of slot uses); not
chance-matched (0.091 against 0.125); not position-matched (read at the
appended question, like the control and unlike the self-directed
query); and at ceiling, 0.998 intact. It fails the F2 test for the same
reason the control does, and it fails an F1-style test in the opposite
direction: a battery at 0.998 with a range of 0.93 can fall far, but a
disruption that spares appended questions will not move it. And it did
move under the input-channel lesion: about 0.07 raw on seed 2
(MEASURED, from the seed-2 endpoint record,
`a3-gates/endpoint_a3_30m_seed2.json`, via the corrected drop reported
in `seeds-endpoint-findings.md`). The clause's (c) still passes on that
seed by arithmetic, because 0.37 minus 0.07 over a spread of a few
hundredths is far above 2. Two comparators that pass for the same
structural reason are one check.

---

## (b) Ways the clause is fitted to seeds 0 to 2 despite the exclusion

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
  stack has found no ownership structure on any seed and the blind
  positive control returned NOT TESTABLE (`blind-control-findings.md`).
  If no other-index subspace can be localized, (e) cannot be evaluated,
  and the text does not say whether that is NOT TESTABLE or (e) waived.
  Under the input-channel lesion there is no defined other-agent
  analogue at all (the channel injects only at own positions; the
  re-indexing probe is the nearest thing and is not named).

### F15 — The two twin calibration substrates cannot run as written

**Severity: fatal against §5.5 as written. MEASURED.**

§5.5's substrates 1 and 2 are the register-less twin checkpoints from
the earlier wave, `artifacts/pilot_a1_30m_seed0_twin/…` and
`…seed1_twin/…`, to be run on the A3 batteries at 800 episodes. Static
checks:

- The twins were trained under `encoding.py`; the A3 harness encodes
  with `encoding_a3.py`. Comparing the two vocabularies: **103 tokens
  against 105, and 72 of the 105 A3 tokens carry a different id** in
  the old vocabulary or none at all. The A3 tokenizer inserts "by"
  before the item names, so every item name, every one of the eight
  answer slots and every query word is shifted. Under the A3 encoding
  the twin reads `parcel_1` as its `parcel_2`, `bay_A` as its `bay_B`,
  `bay_H` as its `where`, and ids 103 and 104 fall outside its table.
- "by" appears in every A3 turn (`assign <item> to <value> by
  <marker>`, registration revision 2). The old vocabulary has no id for
  it.
- The checkpoints' stored configuration: twin `vocab: 103`, A3 seed 0
