
### RT-A4-04 — The threshold calibration buys much less than section 5.5 implied

**Severity: medium. No fix; an honest restatement, plus a relocation of
where the protection actually comes from.**

The separation score is standardized **against its own null**. So under
that null it has a mean near zero and a spread near one *by
construction*, and the 95th percentile of its absolute value therefore
lands near **2 on any substrate whatever** — trained twin, untrained
model, or anything else. The elaborate three-substrate calibration in
section 5.5 will, in all likelihood, return a number close to 2 no matter
what it is run on.

**What follows, and it matters.** The calibration is not worthless — it
confirms the machinery behaves and it produces a number locked before the
data exists, which is a real discipline — but **I oversold it**. It is
close to a formality, and the proposal presented it as the main guarantee.

**Where the protection actually lives**, which the amendment now says
plainly instead:

1. the magnitude condition of RT-A4-02, tied to the already-locked 0.1777;
2. the sign-flip paired test of RT-A4-03, computed on the very checkpoint
   being read, after the lock, and therefore unavailable to fitting;
3. the second, learned comparator;
4. the existing matched-other-agent and random-subspace controls.

**One consequence must be stated explicitly in the registered text.** The
per-checkpoint null spread is **measured on the checkpoint being read**,
not inherited from the calibration substrates. My draft could be read as
locking that spread from the twins, which would be wrong — it would
import a noise estimate from models that learned a different task. What
is locked in advance is the **threshold on the standardized score**; what
is measured per checkpoint is the **spread it is standardized by**.
Measuring a content-blind noise null on a fresh checkpoint before its
verdict is read is not fitting, and is exactly what Gate 0 did per
checkpoint.

---

## Items that tighten the pre-statement

### RT-A4-05 — Matched cells halve the sample, and the noise ruling deserves better

The self-directed query exists only in episodes where the model revises,
which is half of them. So 800 episodes yield about **400 matched cells**,
not 800, and the 2026-09-19 ruling's requirement of at least 800 paired
readings is met in episodes but not in the cells the statistic is
actually computed over. The ruling's own reasoning was about noise: the
bite threshold is about 0.038 raw battery points, against evaluation
spread of 0.0284 at 400 and 0.0169 at 800.

**Fix, folded in, cost $0:** evaluate at **1,600 episodes**, giving about
800 matched cells. It is local inference on checkpoints already fetched —
more wall-clock, no dollars, no pods.

### RT-A4-06 — What happens if one of the three fresh seeds is not testable

Not pre-stated anywhere, and a gap like this is how a result gets
rescued after the fact. With three fresh seeds and an engagement
precondition that can fail per seed, the across-seed outcome needs a rule
written now.

**Folded in, conservatively, and flagged as my call rather than John's:**
the across-seed outcome requires **all three fresh seeds to be testable
and all three to hold**. If any one is not testable, the across-seed
outcome is **NOT TESTABLE** and is reported as such, naming the seed and
the condition it failed. No partial credit, no "two of the three
testable" fallback. John can overturn it; what he cannot do is leave it
unwritten until the data arrives.

### RT-A4-07 — The prior John ordered stated carries a reading rule with it

John's first addition: state now, before the seeds exist, that under
input-channel removal the predicted cell is H_self-location, and that the
informative application of the clause is a localized-subspace lesion.

**The consequence has to be stated with it, or the prior is decoration.**
Zeroing the channel that tells the model which agent it is obviously
destroys a task that requires knowing which agent it is — the existing
result already shows the collapse, by seven to nine times the threshold.
So a positive in that cell is **near-certain in advance and is evidence
that the instrument works, not evidence for the hypothesis.** The
amendment now says that in terms, as the reading rule attached to that
cell, so no write-up can quote it as a confirmation.

### RT-A4-08 — The informative application may be unrunnable, and that outcome needs a home now

The localized-subspace lesion is where the clause earns its keep, and the
localization stack **has so far found nothing anywhere**: probes below
their own permutation baselines on a checkpoint where ownership is
measured to be load-bearing, the blind arm not flagged and on the worse
half of that outcome, and one damage test improving the battery it was
meant to hurt. There is a live chance there is nothing to lesion.

**Folded in:** if the localization procedure's probe fails its own
permutation baseline on a fresh checkpoint, the clause is **NOT TESTABLE**
under the localized lesion on that checkpoint, reported as such, and the
input-channel reading stands alone carrying the weak-evidence label from
RT-A4-07. Written down now so it is a pre-stated cell rather than an
improvisation at 3 a.m.

### RT-A4-09 — Choosing the best layer is a selection, and the defence needs to be on the record

The localization pipeline picks its layer by `best = max(PROBE_LAYERS,
key=probe accuracy)` — a selection over five layers. Selection inflates
false positives.

**The defence, which happens to hold:** the selection is made on *probe
accuracy*, using own-agent labels, and is **blind to the clause's
outcome**. It never sees a battery score. That is the thing that defuses
the multiplicity worry, and it is worth having on the record rather than
discovered by a reviewer. **Folded in:** the amendment states that the
layer and rank are fixed by the localization procedure's own
outcome-blind rule before the clause is read, and that if the clause is
ever read at more than one site, a multiplicity correction is pre-stated
at that time.

### RT-A4-10 — John's second addition needs a precise definition or it will be reported loosely

John's second addition: report the measured spread of the ownership-free
comparator's change alongside the verdict, so a comparator that did not
fall is a number rather than a sentence.

**Folded in as an exact reporting requirement**, because "report the
spread" can be discharged badly. Every verdict carries, for **both**
conditions and for the paired difference: the intact score, the damaged
score, the mean change, the standard deviation across matched cells, and
the standard error of the paired mean, at the stated cell count. So the
sentence "the ownership-free comparator did not fall" always appears as
a mean with its spread attached, and a reader can see for themselves
whether it could have fallen.

### RT-A4-11 — The lock file and its guard do not yet know about the new number

Concrete build item, easy to miss until it fails at the wrong moment. The
existing lock holds the bite threshold and the differential threshold;
the guard checks a lock covers the batteries about to be read. Neither
knows about the separation threshold. **A lock with no separation
threshold in it would pass the guard**, which would put the clause back
in the position of being governed by intention rather than mechanism —
the exact thing the guard was built to end.

**Folded in:** the lock gains the separation threshold, the evaluation
size, the substrates used, and a field recording the exclusion of seeds
0, 1 and 2; the guard is extended to refuse a lock that lacks the
separation threshold when a separation reading is what is being asked
for.

### RT-A4-12 — "Reported, not binding" needs a definition, or it will drift

John ruled the partial-damage ladder reported rather than binding on this
wave. **Folded in as a definition:** the five rungs and their numbers
appear in the findings; **no outcome cell turns on any of them**; no
sentence in any write-up may present the ladder as support for a verdict;
and whether it becomes binding is a later ruling that carries its own
fresh-seed requirement. A criterion's first run should not also be its
first verdict.

### RT-A4-13 — Three concurrent pods is one more than has ever been run

Two pods on one network volume is confirmed working. **Three is not.**
The multi-attach question was answered for two and assumed for more.
Three also triples the idle-billing exposure — which has cost money on
four separate occasions — and triples the exposure to a stock shortage
in the one region the registered venue permits.

**Folded in as pre-launch checks**, not as clause text: confirm the
volume accepts a third attachment before the third pod is created; if it
does not, stage the third run rather than dropping the volume, because
the volume is what makes a pod's death survivable; confirm secure-cloud
stock for three machines in the permitted region; and keep the Mac
powered with the lid open, since the laptop watchdog is still the only
reap that has ever actually worked in production.

### RT-A4-14 — The across-seed bin must name which seeds counted

Small but it is exactly the kind of thing that becomes a correction
later. The fresh-seed rule excludes seeds 0, 1 and 2 from the outcome.
**Folded in:** the outcome is recorded as "3 of 3 **fresh** seeds" with
the seeds named, and any write-up that states the across-seed result must
say which seeds it counted and which it excluded, and why.

### RT-A4-15 — The engagement precondition, once more, with its known weakness

Carried forward from section 6.1 of the proposal and not repaired here,
because I do not think it can be repaired inside this design: **the
content-matched comparator never learned**, and no comparator available
in this design is both content-matched and lively. RT-A4-10's reporting
requirement turns that from a hidden assumption into a visible number,
and the second learned comparator covers part of it, but the gap is real
and the amendment states it rather than managing it.

---

## What this pass did not look at

The training design, the grammar, the tokenizer, the frozen batteries and
the attack sweep — all unchanged by A4 and all previously red-teamed. The
localization stack's own validity, which is a live problem and is the
subject of RT-A4-08, but is not something an amendment to a scoring
clause can fix. The cost arithmetic, which is checked separately against
the ledger rather than red-teamed.

**Standing caution for the independent pass:** this pass was run by the
same author as the proposal, which is the weakest possible arrangement
for finding a motivated error. The three high-severity items above are
the ones I found by checking my own arithmetic and definitions. The class
of error I am least able to find in my own work is a *choice that was
made because it makes a positive reachable*, and RT-A4-04 and RT-A4-15
are the two places I would look first.


===== FILE: experiments/06-mvm-0a-constructed-self-index/red-team-a4.md =====

# Red-team pass on the Amendment A4 clause — §5 of the control-clause proposal, read as registerable text

*2026-09-19. Target: §5 of `docs/control-clause-proposal-2026-09-19.md`
(the 2026-09-19 control-clause proposal, at commit `df039ca`), which is
the text the proposal says can be lifted into `amendment-a4.md` and
registered. Read against Amendment A3 as registered
(`amendment-a3.md`), the ceiling measurement of 2026-09-17
(`ceiling-measurement-findings.md`), the code the clause would run on
(`src/curriculum_a3.py`, `src/train_a3.py`, `src/endpoint_a3.py`,
`src/null_calibration.py`, `src/null_calibration_a3.py`,
`src/lock_guard.py`, `src/encoding.py`, `src/encoding_a3.py`,
`src/model.py`) and the committed records those scripts produced.*

*Brief this pass was fired under: John has ruled for Candidate B with
three fresh seeds (3, 4 and 5), the partial-damage ladder reported but
not binding, the registration commit before launch and the threshold
lock before any endpoint is read. This pass takes those rulings as fixed
and does not argue A against B. It was asked to find every way the
clause, its baselines and its threshold calibration could (a) be
satisfied by a model with no ownership-specific structure, (b) be fitted
to seeds 0 to 2 despite the exclusion, (c) produce a verdict that later
gets over-read, or (d) fail to produce any verdict on seeds 3 to 5, and
to give a short kill case whether or not it would ship.*

*Independence. When this pass read the proposal, the copy on disk
already carried John's ruling annotation, which mentions an amendment
draft (`amendment-a4.md`), a first red-team pass on it
(`a4-red-team-pass-1.md`, fifteen items) and a scoring script
(`src/separation_a4.py`), all uncommitted in the shared checkout.
**None of those three files was opened.** Every finding below was
reached from §5 as written, the registered A3 text, the code and the
committed records. Where the annotation itself disclosed one of the
other pass's conclusions (the within-run baseline being wrong, the
threshold landing near 2, a denominator that can degenerate), this pass
