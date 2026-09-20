
**C7 — Money is not the binding constraint, but the caps are real.**
Spent against the A3 hard stop: **$34.31 of $100** (kill criterion K6,
which halts everything). Spent against the wider envelope: **$215.7 of
$400**, leaving about $184. The RunPod account spend limit is $80 and the
funding rule requires the balance to cover the estimate plus $10 before a
launch. A two-seed wave at about $20 fits all three with room.

**C8 — Two gates hold absolutely.** No registered text changes without
John's ruling. Nothing launches without John's go in his own words,
quoted in the ledger row before the spend.

---

## 2. What changed since the 2026-09-17 draft

Six things, in the order they matter.

**1. The ceiling measurement mooted the previous candidates.** The
2026-09-17 proposal offered four routes, two of which (extra supervision,
a scaffolded intermediate question) aimed at making the control battery
learn, at $27 to $39. A perfectly learning control would have changed
nothing whatever, because the clause fails at a score of 1.0 just as it
fails at 0.32. That proposal is withdrawn, and the annotation on it says
so.

**2. The question itself changed shape.** It is no longer "how do we make
the control learn". It is "can the comparison be repaired at all, and is
the repair a change of measurement rather than a change of training".

**3. The extra-seeds date is answered, not deferred.** John ruled on
2026-09-17 (worklog decision `36413c8d`) that the 20 September
extra-seeds question is closed: it asked for more seeds routed to a
checkpoint whose control had learned, and no such checkpoint exists or
can exist. Any further seeds are now seeds of an amended design, which
makes them this decision's business rather than a separate one.

**4. The bite rule is ruled, and it left one thing open.** C5 above. The
ruling explicitly routed one question here: whether to replace a single
crossing of a threshold with a graded ladder of partial damage requiring
the degradation to grow as more is removed. That is answered in §5.4.

**5. There is now a published precedent for the shape of the repair.**
The Pain Axis paper (Tagliabue, Dung & Berg, arXiv 2609.16247, September
2026; read and summarised in `docs/research-note-pain-axis-2026-09-19.md`)
builds its strongest result as a **matched comparison between identical
content directed at the self and at another**, scored by how cleanly the
two sets of numbers can be told apart, with **no ceiling anywhere in the
denominator**. That is the shape our control comparison was meant to have
and never had. The precedent matters for C4: it means the comparison is
built that way because that is how this kind of comparison is built, not
because it is the shape that makes our numbers work.

> *Verification note, per the standing rule on facts stated from memory:
> the Pain Axis figures were read through a summarising fetch of the
> paper's web version and have **not** been checked against the PDF.
> Nothing in this proposal depends on any number from that paper. It is
> cited only as precedent for the shape of a comparison.*

**6. The date moved.** The decision was scheduled for 4 October. John
intends to rule today and, if the ruling is for an amendment, to launch
tonight. That is why this memo carries the registerable text, the
threshold plan and the cost estimate rather than deferring them.

---

## 3. The candidates

### Candidate A — Close A3 with partial discriminators

Report the primary result, the instrument audit, and the comparison that
was never available, and say all three plainly. **Cost: $0.**

**What it yields.** A replicated, well-measured finding that an objective
requiring a model to act as itself is learnable at 30M parameters, and
that removing the one signal telling it which agent it is collapses that
ability. Plus an unusually candid instrument audit: a registered
denominator that was never checked, a verification attached to the wrong
battery, and a design comment that warned about it and was not acted on.

**What it costs in strength, stated honestly.** The discriminators that
survive without the control are the matched other-agent damage test, the
random matched-subspace tests, and the swap probe. **All three run
through a localization stack that has so far found nothing anywhere.**
Its probes fell below their own permutation baselines on a checkpoint
where ownership is measured to be load-bearing; the blind arm was not
flagged and landed on the worse half of that outcome; and one damage test
*improved* the battery it was meant to hurt. So the partial
discriminators are partial in a stronger sense than the phrase suggests:
they are the ones whose instrument is currently unvalidated.

**What the write-up then claims.** That removing the ownership input
breaks the ownership task, while two ownership-free batteries hold. The
weakness a reader will find immediately: those two batteries (cross-turn
state, turn counting) are **much easier tasks**, scoring 0.999 and 1.000
intact. "The damage broke the hard thing and not the easy things" is not
the same claim as "the damage was specific to ownership", and Candidate A
cannot separate them.

### Candidate B — Register Amendment A4: replace the differential clause with a separation-scored comparison

Keep both batteries exactly as they are. Keep the grammar, the frozen
batteries, the gates and the attack sweep untouched. Replace the one
registered clause that compares the two batteries' damage figures with a
comparison that scores **how cleanly the damage to the ownership-dependent
condition separates from the damage to the ownership-free condition, on
matched content, under the same damage operation**, with no ceiling in
any denominator. Lock its threshold on checkpoints nobody reads a verdict
from, then read it on two **fresh** checkpoints, seeds 3 and 4, launched
as one wave. **Cost: about $20.**

**The fact that makes this cheap.** Every episode in the frozen batteries
already carries **both** queries — the self-directed one, scored at the
model's own revision position, and the other-directed one, asking the
same rule's verdict for a named other agent. Same turns, same items, same
rule, same episode; **only the agent whose commitment is queried
differs.** The matched self/other contrast the Pain Axis paper had to
build on purpose is already inside our registered grammar by
construction. So Candidate B needs **no grammar change, no re-freezing of
batteries, no change to training, and no new attack sweep.** It needs a
new scoring script and two fresh checkpoints.

**What it repairs, and what it does not.** It repairs the comparison. It
does **not** repair the localization question — where in the network
ownership lives — which remains open and whose instrument remains
unvalidated. §5.7 states this as a registered limitation so that a
positive result cannot be read as more than it is.

---

## 4. Recommendation

> **Register Amendment A4 (Candidate B), under three conditions, and
> launch seeds 3 and 4 as one wave tonight if John's go is given.**

**Why B over A.** Candidate A closes a registered comparison as
permanently uncomputable at the exact moment a computable version of the
same comparison is available, costs about $20, requires no change to the
design being tested, and can be locked before the data it reads exists.
The scientific content at stake is not decoration: the matched self/other
contrast is the only thing in the design that can separate "the damage
was specific to ownership" from "the damage broke binding in general",
and that separation is the difference between a finding about
self-indexing and a finding about binding. Candidate A cannot make it.
Candidate B can, on data that does not yet exist, under a threshold
committed in advance.

**Why this is not the forbidden move.** C4 forbids changing a measure
after seeing which way it cuts. Three things keep B on the right side of
that line, and John should test each of them rather than take them:

1. The reason for the change was **measured before the change was
   proposed**, and the measurement was one John required as a
   precondition. The ceiling-corrected measure is incompatible with an
   ownership-free control *by construction* (C3) — a fact about the
   design, not about our results.
2. The replacement has a **published precedent** for why a comparison of
   this kind is built without a ceiling in the denominator.
3. The verdict is read **only on fresh checkpoints**, with the threshold
   locked and committed before those checkpoints exist, and with an
   explicit written commitment that the new statistic is not computed on
   seeds 0, 1 or 2 before the lock (§5.5).

**The three conditions.**

- **(i)** The clause is read on fresh seeds only. Seeds 3 and 4 must both
  satisfy it. Seeds 0, 1 and 2 may be scored under it *after* the verdict
  is read, reported as a consistency check, labelled as such, and never
  counted toward the outcome.
- **(ii)** The threshold is calibrated only on the register-less twin
  checkpoints and an untrained model, by the plan in §5.5, and **John
  commits the lock file**, as he committed the existing one.
- **(iii)** The registration states in terms that A4 repairs the
  comparison and not the localization, so that a positive result under
  the input-channel removal is reported as *the ownership input being
  specifically load-bearing*, never as *an acquired internal structure
  having been found*.

**Confidence, and the strongest case against.** My confidence that B is
the right call is **moderate-to-high** on the reasoning and **moderate**
on the outcome — I think the clause is the right instrument and I do not
predict it will fire. The strongest argument against B, which I cannot
fully answer, is in §6.1: **the content-matched comparator never learned**,
so it may be unable to show damage, and a comparison in which one side
cannot move is a weaker comparison than it looks. §5.2 adds a second,
learned comparator to cover this, and §6.1 says plainly what remains
uncovered.

---

## 5. The amendment, in registerable form

Everything in §5 is drafted so it can be lifted into an `amendment-a4.md`
and committed. It is **not** registered until John rules and the
registration commit is made.

### 5.1 Definitions

**Matched cell.** An evaluation episode carrying both queries: the
self-directed query (the primary battery, scored at the model's own
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

## 6. Red team on my own recommendation

**6.1 The strongest objection, which I cannot fully answer.** The
content-matched comparator — the control battery — **never learned**. It
scores 0.288 to 0.320, which is roughly what a solver that ignores the
name in the question gets. A comparator answering at the level of blind
guessing may be unable to show damage, because a lesion to ownership
structure plausibly does not disturb blind guessing. If so, the
separation score would be driven almost entirely by the self-directed
side collapsing, and "the damage was specific to ownership" would be
partly confounded with "the other side had nothing to lose."

*What is true in mitigation:* the control sits about 0.17 above its
chance floor, so it does have room to fall, and a measured refusal to
fall across 800 paired episodes is evidence rather than an artifact.
*What condition (c) adds:* a second ownership-free comparator that did
learn, at 0.999 intact, with enormous room to fall. *What remains
uncovered:* the learned comparator is not content-matched and the
content-matched comparator is not learned. No comparator in this design
is both. A reader is entitled to say so, and the amendment should say it
first.

**6.2 "This is a metric change after a null."** It is a metric change,
and that should make John suspicious. §4 gives the three tests I think it
passes. The one I would press hardest on: the choice to add the state
battery as a second comparator in (c) **is informed by data I have seen** —
I know it learned and I know the control did not. The defence is that (c)
makes the clause *harder* to satisfy rather than easier, and a change
that raises the bar is not the failure mode C4 exists to catch. But it is
a choice made with knowledge of the data, and John should weigh it as
such.

**6.3 Two fresh seeds is weaker than the registered three.** The
registration required the outcome to hold on every trained seed, with
three seeds for a positive. A4 read on seeds 3 and 4 is two of two. A
third fresh seed costs about **$10 more** and would restore the
registered strength. I did not fold it into the recommendation because
the wave John named is two seeds, but it is cheap, it is inside every
cap, and it is a real sub-decision rather than a detail. **Flagged for
John's ruling.**

**6.4 The order of lock and launch.** The registered procedure puts the
threshold lock before the seeds. The principle behind it is that any
damage result read before the thresholds are locked voids the lock — and
**training reads nothing**. So the binding line is *lock before read*,
not *lock before launch*. The calibration in §5.5 is free but not
instant, and the checkpoints take about ten hours to arrive, which is a
natural window for it. **Recommendation: attempt the lock before launch;
if calibration has not finished, launch anyway and lock before any
endpoint is read, with the registration stating that order explicitly so
it is a choice rather than a slip.** *(My call, not a ruling; confidence
moderate-to-high on the principle, lower on whether the calibration
finishes tonight.)*

**6.5 What a null buys.** The honest prior is that this comes back
generic-binding or not-testable. That is worth the $20 anyway, because
for the first time the generic-binding cell **can** fire. A design in
which the boring explanation cannot be selected is not a test. This
amendment makes the boring explanation reachable, which is most of what
it is for.

---

## 7. Cost estimate — seeds 3 and 4 as one wave

Built from the pilot's **measured 0.645 seconds per training step**, not
from a projection.

| quantity | figure | source |
|---|---|---|
| steps per run | 55,116 | registered budget; identical on the pilot and both seeds |
| tokens per run | 585,552,384 | registered, 20 tokens per parameter |
| training time per run | 55,116 × 0.645 s = **9.87 h** | measured pilot rate |
| pod time above training | +0.3 to +0.5 h | measured on seeds 1 and 2 (10.16 h and 10.12 h pods) |
| pod lifetime per run | **10.2 to 10.4 h** | |
| two pods, run concurrently | 20.4 to 20.8 pod-hours | one wave, both launched together |
| rate | $0.99/hour, RTX 5090 secure, EU-RO-1 | the venue of every A3 run |
| **central estimate** | **$20.2** | |
| **estimate band** | **$18 – $26** | the same band the seeds 1 and 2 wave carried, which landed at $20.08 |
| storage volume drip | ~$0.10 for the run | about $7/month |
| idle-billing exposure | +$0.76 best case, +$4 to $6 per pod if a watchdog dies | four measured occurrences |
| **worst credible total** | **~$30** | both watchdogs lost, both pods billing past completion |

**Against the caps.**

| cap | before | after the wave | headroom left |
|---|---|---|---|
| A3 hard stop (kill criterion K6) | $34.31 / $100 | ~$54.5 / $100 | ~$45.5 |
| wider envelope | $215.7 / $400 | ~$235.9 / $400 | ~$164 |
| RunPod account spend limit | $80 | — | must be checked before launch |

**Adding a third fresh seed** (§6.3) costs about **$10.2** more: about
$30.4 for the wave, about $64.8 against the $100 stop.

**Wall clock.** About 10.2 hours. Launched tonight, the checkpoints
report tomorrow morning.

**Two standing warnings that cost real money.**

1. **Idle billing has happened four times**, most recently when an
   overnight operating-system update rebooted the Mac and killed both
   watchdogs. The pod-side reaper is now armed in the launcher but has
   **never run in production**. The laptop watchdog is still the backstop:
   **keep the Mac powered and the lid open overnight.**
2. **The balance query returned an HTTP 403 with the stored key** during
   the last wave, so the last wave's $20.08 is arithmetic on measured pod
   lifetimes rather than a confirmed balance. The balance must be checked
   by another route before launch, because the funding rule requires it
   to cover the estimate plus $10 — about $36 here.

---

## 8. If John rules for A4, the order of operations

Stated so the evening has no ambiguity in it. **Every gate below holds.**

1. **Red-team pass on this proposal** — free, local, before any commit.
2. **Registration commit** — `amendment-a4.md` written from §5, committed.
   *Requires John's ruling; no registered text moves without it.*
3. **Threshold calibration** on the two twins and the untrained model
   (§5.5) — free, local; produces the lock file.
4. **John commits the lock.** Claude writes the file; the commit is
   John's, as it was for the existing lock.
5. **Stage the wave** through the launcher, dry-run clean, with a ledger
   row carrying the estimate **before** any spend.
6. **Stop for John's go, in his own words, quoted in the ledger row.**
   *Nothing launches without it.*

If step 3 does not finish in time, step 6 may precede it under §6.4 —
launch, then lock before any endpoint is read — but only if the
registration says so explicitly.

---

## 9. What John is being asked to rule

1. **A or B?** Close A3 with partial discriminators, or register
   Amendment A4. *(Recommendation: B.)*
2. **If B: two fresh seeds or three?** Two is $20; three is $30 and
   restores the registered across-seed strength. *(§6.3; no
   recommendation — it is a judgment about how much the stronger claim is
   worth.)*
3. **If B: is the partial-damage ladder reported, or binding?**
   *(Recommendation: reported on this wave, §5.6.)*
4. **If B: lock before launch, or lock before read?** *(Recommendation:
   attempt before launch, permit before read, stated in the
   registration, §6.4.)*

---

