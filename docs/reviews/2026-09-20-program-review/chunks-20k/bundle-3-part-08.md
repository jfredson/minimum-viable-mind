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

*Authorship: this memo is Claude's proposal. Nothing in it is a ruling,
and no call inside it has been upgraded to John's. The rulings it rests
on are cited by date and by their worklog entries, each named in plain
words in the text.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/a4-red-team-pass-1.md =====

# Red-team pass 1 on Amendment A4

*2026-09-19. Free, local, before any registration commit — step 1 of the
proposal's order of operations. Run by Claude against Claude's own
proposal (`docs/control-clause-proposal-2026-09-19.md`), after John's
ruling of 2026-09-19 and **before** the independent pass John has running
in another session. Nothing here is registered and nothing is spent.*

**Fifteen items. Three of them change the clause materially, one is an
outright error in my draft, and one lowers my own claim about how much
the threshold calibration buys. All fifteen are folded into the amendment
draft; this file is the record of what was caught and why, so the
independent pass can see what has already been found and go looking
elsewhere.**

---

## The three that change the clause

### RT-A4-01 — The new denominator can degenerate, which is exactly how the old clause died

**Severity: high. The clause is not registerable without this fix.**

The separation score divides by `spread_null(L)`, the spread of the mean
paired difference across random-damage draws. Random damage at matched
strength is chosen precisely because it *should not move behaviour*. If
it moves behaviour hardly at all, that spread is small; in a degenerate
case it can approach zero, and the score approaches infinity.

**This is the same structural failure that killed the registered A3
clause** — a denominator that can go to zero — arriving by a different
road. Registering a replacement with the same class of defect, on the
same day the defect is documented, would be indefensible.

**Fix, folded in.** Put a floor under the denominator that cannot be
zero for non-degenerate data:

    spread(L) = max( spread_null(L) , standard error of the paired mean )

where the standard error is the ordinary one computed from the observed
per-cell spread of the paired difference at the evaluation size. The
record states which of the two governed on each reading. A denominator
that is the larger of a measured null spread and a sampling floor cannot
vanish, and taking the larger is conservative in the right direction: it
makes the clause harder to satisfy, never easier.

### RT-A4-02 — The magnitude of the damage is not in the clause at all

**Severity: high.**

Every condition in my draft is about *specificity* — whether the damage
falls more on the ownership-dependent side than the ownership-free side.
Nothing in it requires the damage to be **large**. A tiny but perfectly
specific effect would satisfy the clause.

**Fix, folded in, at no cost and with no new calibrated number.** Add a
magnitude condition tied to the threshold John has **already locked**:
the self-directed battery's damage, under the registered ceiling-corrected
measure, must reach the locked bite threshold of **0.1777**. That measure
is well defined for the primary battery — its baseline is about 0.57
against a ceiling of 0.2921, so the floor rule passes with room — and the
number is already committed in John's existing lock. The clause gets a
magnitude bar for free, out of the registered instrument, rather than out
of a new quantity somebody would have to calibrate and defend.

### RT-A4-03 — My within-run baseline was the wrong permutation, and would have been testing the wrong thing

**Severity: high. This is an error in the proposal, not a weakness.**

Section 5.4(b) of the proposal specified a baseline that **shuffles the
self/other labels across matched cells**. That is invalid here. The two
conditions are *not* exchangeable: intact, the self-directed query scores
about 0.57 and the other-directed query about 0.30. Shuffling their
labels tests whether those two levels are exchangeable — which they
plainly are not, and which nobody asked. It would have produced a
baseline the observed value clears for a reason that has nothing to do
with the damage.

**Fix, folded in.** Replace it with the correct paired test: **randomly
flip the sign of each cell's paired difference**, 1,000 draws, and take
the spread of the resulting means. This tests exactly the null the clause
needs — *the damage falls equally on both conditions, so the paired
difference is centred on zero* — and it makes no assumption whatever
about the two conditions having equal base rates. It is the standard
paired permutation test and it is the right one.

*The proposal's section 5.4(b) is wrong as written and is corrected here
rather than quietly rewritten.*

---

## The one that shrinks a claim I made

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

