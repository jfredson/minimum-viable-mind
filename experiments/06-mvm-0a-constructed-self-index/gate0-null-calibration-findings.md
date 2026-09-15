# Gate 0 — the registered null calibration, and the K0 reading

*2026-09-14. Status: **measured record, not adjudicated.** Gate 0 is the
first action Amendment A3 orders (§4.1), and its kill criterion K0 is
John's to apply — the band criterion is a number he sets, not one this
document sets. Everything here ran locally on the Mac at **$0**; no pod
was created, nothing was trained, no checkpoint was promoted [C1/C2].
Scripts: `src/null_calibration.py` (committed at `3d08807`, **before it
read any checkpoint**), `src/null_escalation.py` (`a27dcb8`),
`src/summarize_null.py` (`9e67788`). Per-checkpoint records in
`null-calibration/`; every table below is generated from those files by
`summarize_null.py`, not typed by hand.*

## What was registered, and what this is

The pre-registration refused to let thresholds come from a pilot, because
on the same architecture and curriculum a pilot's drop *is* the registered
quantity. What it registered instead: **θ and δ are pre-committed
quantiles of the chance-corrected drop under ablations that carry no
information about any structure** — "matched-strength random-subspace and
matched-norm ablations, computed by a script committed before it runs."
That script did not exist until now. This is it, and this is its first
run.

The chance-corrected drop is the registered metric:
`d(B) = (B_base − B_abl) / (B_base − chance_B)`. A drop of d = 1.0 means
the ablation took the battery all the way from its baseline to chance.

**What was ablated.** Residual-stream operators at blocks 3, 4, 5, 7 and 8
of 12 — Experiment 1's registered layer list rescaled to this model's
depth. Two operators, paired so that each draw's noise carries the same
strength as its mean-ablation twin: a random rank-k subspace pinned to its
reference mean, and isotropic noise matched to the norm that pinning
removes. Ranks 4, 8 and 16 (16 is A3's rank cap), twenty seeds each: 120
draws per checkpoint. On the three register-bearing checkpoints, twenty
further draws replace the register's content with matched-norm noise —
the original design's own target, reported separately because A3 trains no
register.

**The whole eval runs under each ablation**, enactment forward passes and
acting-channel injections included, on the registered held-out eval at 400
episodes. The intact baselines reproduce the committed endpoint and item-
sweep rows, which is what validates the harness.

### Baselines reproduced at n=400 (the eval the endpoint rows report)

| checkpoint | arch | bound? | T_sr | T_si | T_state | T_syntax | T_sr_rev |
|---|---|---|---|---|---|---|---|
| pilot seed-0 full | full | yes | 0.993 | 0.960 | 0.993 | 1.000 | 0.842 |
| seed-1 twin | twin | yes | 1.000 | 0.968 | 1.000 | 1.000 | 1.000 |
| seed-1 full | full | no | 0.953 | 0.340 | 0.995 | 1.000 | 0.000 |
| seed-0 twin | twin | no | 0.953 | 0.355 | 0.998 | 1.000 | 0.000 |
| seed-2 full | full | no | 0.953 | 0.338 | 0.988 | 1.000 | 0.000 |

### θ — the null band, 95th percentile of |d| over 120 content-blind residual ablations

| checkpoint | T_sr | T_si | T_state | T_syntax | T_sr_rev |
|---|---|---|---|---|---|
| pilot seed-0 full | 0.0058 | 0.0060 | 0.0022 | 0.0000 | 0.1464 |
| seed-1 twin | 0.0000 | 0.0095 | 0.0000 | 0.0000 | 0.0000 |
| seed-1 full | 0.0000 | 0.1628 | 0.0033 | 0.0000 | floor (Δacc +0.000) |
| seed-0 twin | 0.0181 | 0.3790 | 0.0033 | 0.0000 | floor (Δacc +0.003) |
| seed-2 full | 0.0000 | 0.1315 | 0.0364 | 0.0000 | floor (Δacc +0.000) |

### δ — the differential band, 95th percentile of |d(B1) − d(B2)|

| checkpoint | T_sr-T_state | T_si-T_state | T_sr_rev-T_state | T_sr_rev-T_si |
|---|---|---|---|---|
| pilot seed-0 full | 0.0058 | 0.0061 | 0.1464 | 0.1465 |
| seed-1 twin | 0.0000 | 0.0096 | 0.0000 | 0.0095 |
| seed-1 full | 0.0034 | 0.1540 | floor | floor |
| seed-0 twin | 0.0215 | 0.3790 | floor | floor |
| seed-2 full | 0.0364 | 0.1221 | floor | floor |

### Register-state noise (full checkpoints only, 20 draws; the original design's own target)

| checkpoint | T_sr | T_si | T_state | T_syntax | T_sr_rev |
|---|---|---|---|---|---|
| pilot seed-0 full | 0.0058 | 0.0036 | 0.0000 | 0.0000 | 0.1464 |
| seed-1 full | 0.0000 | 0.0791 | 0.0002 | 0.0000 | floor |
| seed-2 full | 0.0000 | 0.1127 | 0.0000 | 0.0000 | floor |

### K0 — does the band swallow the binder/non-binder split?

| checkpoint | battery | baseline | null band θ | d if the battery fell to the non-binder level (0.35) | band ≥ 0.25? |
|---|---|---|---|---|---|
| pilot seed-0 full | T_si | 0.960 | 0.0060 | 0.731 | no |
| pilot seed-0 full | T_sr_rev | 0.842 | 0.1464 | 0.686 | no |
| seed-1 twin | T_si | 0.968 | 0.0095 | 0.733 | no |
| seed-1 twin | T_sr_rev | 1.000 | 0.0000 | 0.743 | no |
| seed-1 full | T_si | 0.340 | 0.1628 | -0.047 | no |
| seed-1 full | T_sr_rev | 0.000 | at floor, d undefined | — | no |
| seed-0 twin | T_si | 0.355 | 0.3790 | 0.022 | YES — K0 FIRES |
| seed-0 twin | T_sr_rev | 0.000 | at floor, d undefined | — | no |
| seed-2 full | T_si | 0.338 | 0.1315 | -0.056 | no |
| seed-2 full | T_sr_rev | 0.000 | at floor, d undefined | — | no |

### T_si repeated-item rescoring (the A3 decision-14 fix, $0 side table)

| checkpoint | unique items (n) | acc vs recorded answer | repeated items (n) | acc vs recorded | acc vs latest value |
|---|---|---|---|---|---|
| pilot seed-0 full | 375 | 0.997 | 25 | 0.400 | 0.720 |
| seed-1 twin | 375 | 1.000 | 25 | 0.480 | 0.240 |
| seed-1 full | 375 | 0.341 | 25 | 0.320 | 0.320 |
| seed-0 twin | 375 | 0.355 | 25 | 0.360 | 0.440 |
| seed-2 full | 375 | 0.344 | 25 | 0.240 | 0.360 |

### Which convention does each run apply to a repeated item?

Read off the thread-3 item rows (`lesion-results/items_*.jsonl`) with the episodes regenerated deterministically — T_si asks about other agents, whose values the enactment never touches, so no model pass is needed.

| checkpoint | repeated-item cells | picks the earlier value | picks the later value | picks neither |
|---|---|---|---|---|
| pilot seed-0 full | 25 | 0.28 | 0.72 | 0.00 |
| seed-1 twin | 25 | 0.76 | 0.24 | 0.00 |
| seed-1 full | 25 | 0.40 | 0.32 | 0.28 |
| seed-0 twin | 25 | 0.32 | 0.44 | 0.24 |
| seed-2 full | 25 | 0.36 | 0.36 | 0.28 |

### Instrument validity — where the operator does bite (escalation past the rank cap, not part of the band)


**pilot seed-0 full** (d_model 448, registered cap k≤16; residual RMS norm at layer 3 = 4234, mean-centred 747)

| operator | strength | share of residual norm | T_sr | T_si | T_state | T_syntax | T_sr_rev |
|---|---|---|---|---|---|---|---|
| rand-mean | rank 16 | 3.3% of raw, 19% of centred | 1.000 | 0.960 | 1.000 | 1.000 | 1.000 |
| rand-mean | rank 32 | 4.8% of raw, 27% of centred | 0.997 | 0.960 | 1.000 | 1.000 | 0.967 |
| rand-mean | rank 64 | 6.7% of raw, 38% of centred | 0.968 | 0.958 | 0.962 | 1.000 | 0.967 |
| rand-mean | rank 128 | 9.2% of raw, 52% of centred | 0.630 | 0.618 | 0.345 | 0.590 | 0.600 |
| rand-mean | rank 256 | 13.4% of raw, 76% of centred | 0.238 | 0.198 | 0.052 | 0.000 | 0.200 |
| rand-mean | rank 448 | 17.6% of raw, 100% of centred | 0.110 | 0.120 | 0.050 | 0.000 | 0.000 |
| rand-noise | noise ×1 | 3.3% of raw, 19% of centred | 0.997 | 0.960 | 1.000 | 1.000 | 0.933 |
| rand-noise | noise ×4 | 13.3% of raw, 75% of centred | 0.983 | 0.968 | 0.998 | 1.000 | 0.900 |
| rand-noise | noise ×16 | 53.1% of raw, 301% of centred | 0.665 | 0.637 | 0.857 | 0.997 | 0.633 |
| rand-noise | noise ×64 | 212.3% of raw, 1203% of centred | 0.245 | 0.245 | 0.230 | 0.548 | 0.300 |

**seed-1 twin** (d_model 448, registered cap k≤16; residual RMS norm at layer 3 = 2427, mean-centred 642)

| operator | strength | share of residual norm | T_sr | T_si | T_state | T_syntax | T_sr_rev |
|---|---|---|---|---|---|---|---|
| rand-mean | rank 16 | 5.0% of raw, 19% of centred | 1.000 | 0.958 | 1.000 | 1.000 | 1.000 |
| rand-mean | rank 32 | 6.6% of raw, 25% of centred | 1.000 | 0.957 | 0.987 | 1.000 | 1.000 |
| rand-mean | rank 64 | 9.7% of raw, 37% of centred | 1.000 | 0.958 | 0.877 | 1.000 | 1.000 |
| rand-mean | rank 128 | 13.7% of raw, 52% of centred | 0.948 | 0.893 | 0.288 | 1.000 | 0.967 |
| rand-mean | rank 256 | 19.9% of raw, 75% of centred | 0.128 | 0.115 | 0.023 | 0.000 | 0.100 |
| rand-mean | rank 448 | 26.4% of raw, 100% of centred | 0.105 | 0.100 | 0.020 | 0.000 | 0.100 |
| rand-noise | noise ×1 | 5.1% of raw, 19% of centred | 1.000 | 0.967 | 1.000 | 1.000 | 1.000 |
| rand-noise | noise ×4 | 20.3% of raw, 77% of centred | 0.998 | 0.968 | 0.990 | 1.000 | 1.000 |
| rand-noise | noise ×16 | 81.1% of raw, 307% of centred | 0.607 | 0.540 | 0.610 | 1.000 | 0.633 |
| rand-noise | noise ×64 | 324.6% of raw, 1228% of centred | 0.223 | 0.217 | 0.173 | 0.813 | 0.133 |

## The reading

**1. On the binders the band is narrow, and K0's stated condition is not
met — but the proposed number is tripped on one non-binder, and that needs
a decision.**

On the two binders, the only checkpoints where a lesion verdict could ever
be read, content-blind ablation moves `T_si` by a 95th-percentile
chance-corrected drop of 0.006 and 0.0095. The split K0 asks about — `T_si`
at 0.96 to 1.00 against 0.34 to 0.36 — is a drop of about 0.73 in the same
units. The band is roughly a hundred times too narrow to swallow it.

K0 is written two ways, and the two ways disagree on this data. Its
condition is that "the band is wide enough that the existing
binder/non-binder split sits inside it," and its proposed operational
number is a band of 0.25 on the verdict batteries. **The stated condition
is met nowhere. The proposed number is exceeded on one checkpoint of five:
the seed-0 twin, at 0.379.**

That checkpoint is a non-binder whose `T_si` sits at 0.355 against a chance
floor of 0.125. Two things make its band wide, and only one of them is
noise. The metric divides by distance above chance, and that distance is
0.23 here against 0.84 on a binder. And the ablations genuinely degrade it:
across the 120 draws its raw `T_si` falls from 0.355 to as low as 0.250,
with the signed drop never going negative. Whatever fragile above-chance
heuristic this run has, random damage knocks it down. In raw terms the band
is 0.087 accuracy, 35 items of 400.

**The decision this leaves John** is which checkpoints the band is read on.
The amendment does not say. If the band is read on the runs where a verdict
is read, it is about 0.01 and K0 plainly does not fire. If it is pooled
across all five including runs sitting near chance, the proposed 0.25 is
exceeded by one run and K0's number would fire on a technicality.

My reading, offered and not ruled: **a wide band near chance cannot
manufacture a false positive.** It can only make a marginal learner
unreadable, and "unreadable because it barely learned" is already its own
registered bin. So the near-chance band is not evidence that the verdict
logic is underpowered where the verdict is read. **Third recommendation for
red-team pass 3: state in K0 that the band is read on checkpoints whose
verdict battery clears the floor margin**, so the criterion cannot turn on
a run that never learned the task.

**2. A real power limit the band exposes, and it is not on `T_si`.** The
one battery with a wide band is `T_sr_rev`, and the reason is arithmetic,
not noise: at 400 episodes the revised-own split contains **19 items**, so
one item flipping is a drop of 0.073 and two is 0.147. Its band is two
items. The proposed 0.25 criterion is 3.4 items on that cell.

This matters for A3 more than anything else here. Decision 12 sets
"verdict cells at n=400," but in this harness 400 is a count of
*episodes*, and the revision-conditioned battery harvests one cell from
about one episode in twenty. A3's primary metric `T_act` is scored at the
model's own revision positions. If its generator inherits the current
revision frequency, **`T_act` would be a 20-item verdict cell at n=400
episodes, not a 400-item one**, and its null band would be dominated by
single-item granularity in exactly the way K0 exists to catch.

The amendment never states a revision frequency. Candidate A's design
arguably implies one — the supervised position *is* the own revision turn,
so every episode should carry exactly one — but implying it is not
registering it. **Recommendation for red-team pass 3, before the
registration commit: state in A3 §2.2 that every episode contains exactly
one own revision, so that 400 episodes yield 400 `T_act` cells.** This
costs nothing and is the difference between a verdict cell of 400 and one
of 20.

**3. The metric widens sharply as a battery approaches chance, and that is
where A3's unlearnable boundary sits.** The chance-corrected drop divides by
how far the baseline stands above chance, so the same wobble in items reads
very differently depending on where the battery sits. Measured on `T_si`:

| checkpoint | `T_si` baseline | distance above chance | null band | the same band in items |
|---|---|---|---|---|
| seed-1 twin | 0.968 | 0.843 | 0.0095 | 3 of 400 |
| pilot seed-0 full | 0.960 | 0.835 | 0.0060 | 2 of 400 |
| seed-1 full | 0.340 | 0.215 | 0.1628 | 14 of 400 |

Both effects compound on the non-binder. It is genuinely noisier in raw
items, because a model near chance is guessing and small perturbations flip
many answers, and its divisor is four times smaller. The band is not an
artifact; it is what the registered metric does in that regime, and it is
worth knowing before a verdict is read there.

**A3 reads its unlearnable verdict in exactly this regime.** Criterion K2
retires the pilot if `T_act` at budget exhaustion is "≤ lookup ceiling
(0.25) plus the null band." If `T_act` lands just above the lookup ceiling,
say 0.30, the divisor is 0.175 and a 14-item wobble of the kind the
non-binder shows would read as a drop of 0.20 — the same order as the
proposed 0.25 criterion.

There is also a units problem in K2 as written, and it should be fixed
before registration rather than argued about after a pilot. **The lookup
ceiling of 0.25 is a raw accuracy; the null band is in chance-corrected
units. As written, K2 adds one to the other.** They are not the same
quantity and the sum has no meaning. **Second recommendation for red-team
pass 3: state K2's comparison in raw accuracy, converting the band
explicitly** — unlearnable if `T_act` ≤ 0.25 + θ × (baseline − chance),
which on the numbers above is about 0.285 rather than 0.45. The two
readings differ by enough to change the verdict.

**4. The register is inert here too, and now with a band under it.**
Replacing the registers' content with matched-norm noise moves the
batteries no further than a random residual subspace does. Thread 4 reached
this conclusion from lesions; Gate 0 converts it into the registered-
instrument form the options memo asked for — a drop, a band, and the
verdict "indistinguishable from null" — without asking a reader to trust an
unregistered harness.

**5. The operator has teeth, so the narrow band is robustness and not a
dead instrument.** At the registered rank cap the random operator removes
only 3 to 5 percent of the residual stream's raw norm, so "nothing moved"
could have meant the network is robust or could have meant the operator
does nothing. Thread 4 made the same move before trusting its null,
verifying the register pathway was live rather than dead. The escalation
table settles it. Read against the mean-centred residual, which is the part
that carries information and is about a sixth of the raw norm, the cap
already removes 19 percent of it and the batteries do not move. Push
further and they break in an orderly way: at 52 percent of the centred
residual both binders fall apart, and by 75 percent everything is at chance.
Matched-norm noise behaves the same, untouched at four times the cap's
strength and collapsing at sixteen.

So there is a wide margin between the strength the registered band uses and
the strength that damages these models, and the band sits well inside it.
Every ablation here is random, so it touches no designated structure and
falls inside the dry-run A3 §4.1 permits before the lock.

**6. A correction to the thread-3 reading of the `T_si` repeated-item
defect.** The defect is real: when an item was revised, the recorded answer
is a coin flip between the stale and the current value, so a consistent
model is marked wrong about half the time. But thread 3 explained it by
saying the binders have "consistent latest-value semantics." They do not
agree with each other. On repeated items the seed-1 twin picks the
*earlier* value 76% of the time; the pilot seed-0 full picks the *later*
value 72% of the time. Both are consistent; they learned opposite
conventions.

So the retroactive half of A3's decision 14 cannot be done by re-keying old
scores to the latest value — that would score one binder at 0.24 and the
other at 0.72 and call the first one broken. The *structural* half of the
fix is sound and unaffected: Candidate A's deterministic revision rule
gives every revised item one well-defined answer, so the ambiguity stops
existing rather than being scored around. The rescoring table below is
published as a side table for the record, with both conventions shown, and
no verdict is read from it. This also adds a third leg to thread 3's
finding that the binders are doing generic associative retrieval: the
tie-break they apply to a genuinely ambiguous item is arbitrary and
seed-dependent.

## The seed-0 asterisk, stated where it cannot be missed

Thread 4 read register-ablation battery scores on the pilot seed-0
checkpoint on 2026-08-19, before any threshold lock existed. RT-10's clause
is that a pilot ablation result read before threshold lock voids the lock,
and by the run-identity note that checkpoint *is* the registered seed-0
full run. **The band computed here for seed 0 is therefore for the record,
not a clean registered lock on seed 0.** It is usable as the noise floor
against which thread 4's numbers are read, and it is not usable as a
threshold that seed 0's own result is then judged against.

Two things keep this from being worse than it is. The contamination runs
one way and against the design's own prediction: knowing the drop is about
zero cannot manufacture a positive, only foreclose one. And A3 inherits
none of it, because A3's θ and δ are calibrated on a new pilot checkpoint
by this same script, with the lock ordered ahead of any L1 read by the gate
order rather than by intention.

## What Gate 0 does not claim

It does not certify that any A3 result will be readable; it certifies that
the existing instrument's noise floor is narrow on the batteries where the
question can be posed, and it names one battery where the floor is coarse
and why. It reads no verdict on any hypothesis. It scores the five existing
checkpoints on nothing new except the `T_si` rescoring side table, which is
exploratory by A3 §3.6. And it sets no threshold: θ and δ for A3 are locked
on A3's own pilot, in a commit that is John's.

## Cost

**$0.** Five checkpoints × 120 or 140 ablated evaluations, plus the
escalation check, all local on the M4. The ledger row is recorded as $0
against the Gate 0 line of A3 §4.1, which budgeted $0 to $5. Cumulative
A3 spend: **$0 of the $100 hard stop.**

## What comes next, and what needs John

Gate 0 is complete and its result is reported. Nothing further in A3 runs
until John's go: the next action in the ratified sequence is red-team pass
3, then the registration commit, then Gate 1, and only then the pilot at
about $12 on his C2 authorization.

Three items are John's alone:

1. **K0's number.** The proposed criterion is a 95th-percentile band of
   0.25 on the verdict batteries. Measured: about 0.01 on `T_si` for both
   binders, and 0.147 on the 19-item `T_sr_rev` cell of the pilot. On the
   proposed number K0 does not fire.
2. **The `T_act` cell-size recommendation** above, which belongs in red-team
   pass 3 and changes A3's text before registration.
3. **The K2 units fix** above, likewise for red-team pass 3: the criterion
   currently adds a raw accuracy to a chance-corrected band.
4. **Whether the retroactive `T_si` rescoring is dropped** from decision 14,
   keeping only the structural fix, given that the two binders use opposite
   conventions.
