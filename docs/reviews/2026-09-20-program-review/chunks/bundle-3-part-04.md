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
says so at the finding. Reconciling the two passes is a separate job,
and this file does not take ledger numbers (the running RT-nn series in
`red_team_ledger.md`) so that the reconciliation can assign them without
collision; findings here are labelled F1 to F22.*

*What this pass did and did not do. Every finding is marked **MEASURED**
(a static check was run and its output is reported: a tokenizer
comparison, a checkpoint configuration read, a record inspection, a
search of the source) or **ARGUED** (reasoning from the documents and
the code, which a reader can dispute). **No model was run. The
separation statistic was not computed on any checkpoint**, including
seeds 0, 1 and 2, in keeping with the discipline commitment in §5.5;
where a number below concerns those seeds it is quoted from a record
already committed, or is a bound derived from such quotes. Nothing was
spent.*

*House rule this document is written under: the workspace plain-language
rule (`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30). Short labels are
kept where they make a claim checkable and every one carries a phrase
saying what it is.*

---

## Glossary, once

- **The self-directed query, or the primary battery (T_act).** The
  model's own revision turn inside an episode. Scored by whether the
  model's most likely next token, among the eight slot names, is the
  value the shared rule dictates for its own earlier value. Chance
  0.125.
- **The other-directed query, or the control battery (T_other).** A
  question appended after the episode: "where did <named agent> assign
  <item> to next?", about an item that agent did not revise, so the
  answer is one visible turn plus the rule. Chance 0.125.
- **The state battery (T_state).** An ownership-free question appended
  after the episode ("which parcel was mentioned last?" or "how many
  parcels went to <slot>?"). Scores 0.998 intact on the seen seeds.
- **The input-channel lesion, called L0.** Zeroing the acting channel,
  the projection that injects the model's own previous state at the
  positions where it acts. It is the only authorship signal in the
  design.
- **A localized-subspace lesion, called L1.** Removing a low-rank
  direction in the residual stream found by probes and patching. The
  localization stack has so far found nothing on any A3 checkpoint.
- **The separation score, S.** §5.1's statistic: the mean over matched
  cells of (self-directed drop minus other-directed drop), divided by
  the spread of that same mean under random damage.
- **σ (sigma).** The threshold S must reach, to be set by §5.5.
- **The seen seeds.** Checkpoints 0, 1 and 2, whose lesion results are
  already on the record. **The fresh seeds.** 3, 4 and 5, to be trained.

---

## Summary

| ID | Finding | Brief question | Severity |
|---|---|---|---|
| F1 | Under the input-channel lesion the boring cell is arithmetically unreachable on any checkpoint resembling the three in hand, because the comparator has about a fifth of the self-directed battery's room to fall; the clause cannot lose there | (a), (c) | **fatal** against the claim that the generic-binding cell "can fire" |
| F2 | "Matched content" is not a matched condition: the self-directed score is read at the very positions the lesion strikes, the other-directed score is read at an appended question far from them; a position-local disruption with no ownership content satisfies the clause, and the random baseline damages all positions alike so cannot catch it | (a) | **fatal** against the reading "specific to ownership" |
| F3 | Under a localized lesion the clause drops every discriminator the registered positive bin carried (swap probe, matched other-index control, re-indexing probe, probe-patching convergence); an act-marker echo or a mine-bit tag satisfies (a) to (h) | (a) | serious |
| F4 | The second comparator does not repair F1 or F2: the state battery is unmatched in content, chance, question form and position, sits at ceiling, and fell about 0.07 raw under the same lesion on seed 2; two comparators that fail the same way are one check | (a) | serious |
| F5 | Every ingredient of the numerator on the seen seeds is already in committed records, including the control's score under the lesion on all three; the "not computed" commitment protects a pairing detail, not the sign or size of the result | (b) | serious |
| F6 | σ is self-normalizing and lands near 2 on any substrate, so the calibration decides nothing; the quantity that decides the verdict is the spread as used on the fresh seeds, and §5 does not say on which checkpoint, over which draws, or pooled how — each a post-lock choice on data in hand | (b), (d) | **fatal** against §5.5 as a calibration |
| F7 | The random-damage raw draws for seed 0, which are what the spread is by definition, already exist in the record the A3 lock was cut from; the sizes and shape of the clause were chosen with that band visible | (b) | worth noting |
| F8 | The engagement precondition certifies nothing: a checkpoint passes "engaged" at 0.225 while scoring below the solver that cannot read the name (0.3227); and the text admits the margin and the second comparator were chosen knowing the data | (b) | worth noting |
| F9 | The positive cell is named H_self-location, the registered A3 positive bin's name, which carried discriminators this clause drops; §5.7's disclaimer will not survive a summary table | (c) | serious |
| F10 | The "located, wrong structure" cell is redefined: as ruled on 2026-09-19 it means the ablation improves the primary battery; §5.2 maps it to the other-directed condition falling more, and an improvement of the primary now lands nowhere | (c), (d) | serious |
| F11 | Magnitudes of S around 10 to 25 are expected under the input-channel lesion by arithmetic, and a monotone dose ladder on an input scaling is near-automatic; both will be read as many-sigma evidence of a structure | (c) | serious |
| F12 | Reporting the seen seeds "as a consistency check" yields "five of five" from three results whose sign and size are already known, and a non-firing generic-binding cell will be read as generic binding ruled out when F1 says it could not fire | (c) | serious |
| F13 | The outcome table does not partition the outcomes: (a) holding while (c), (e) or (h) fails lands nowhere; an improvement inside the band lands nowhere; two seeds of three lands nowhere; the A3 seed-dependent bin is not carried | (d) | serious |
| F14 | Condition (e) fails by construction: the random matched-subspace draws define σ as their own 95th percentile, so one draw in twenty exceeds it; the condition needs a quantifier, and the matched other-agent damage test needs a localized other-index subspace the stack cannot supply | (d) | **fatal** as written |
| F15 | The two twin calibration substrates cannot run: they were trained under a tokenizer whose ids differ from the A3 tokenizer on 72 of 105 tokens (every item, every answer slot, every query word), a token in every A3 turn has no id in their vocabulary, their embedding tables are 103 wide against 105, and no bridge exists in the source | (d), (b) | **fatal** against §5.5 as written |
| F16 | The untrained substrate risks a zero-spread null (no answers flip under small random damage), which under "maximum across substrates" yields either no σ or one no learned model can reach; the control diagnostic failed on exactly this on 2026-09-17 and §5.5 has no degeneracy precondition | (d) | serious |
| F17 | Condition (f)'s validity gates have no A3 implementation and were never applied to the input-channel lesion on any seed; applied for the first time on the fresh seeds they may void every verdict, and not applied they are decorative | (d) | serious |
| F18 | The random baseline is not matched to the input-channel lesion in rank, norm, layer or position; "the same rank and the same norm, at the same layers" has no meaning for zeroing a projection that injects at three positions | (d), (a) | serious |
| F19 | The evaluation harness returns battery means only; per-cell pairing, the within-run baseline and the ladder are a new instrument whose first run would be the verdict, against the known-answer rule of 2026-09-16 | (d), (c) | serious |
| F20 | The lock guard as built cannot hold a σ lock (it requires θ and δ per battery against one calibration record); the evaluation seeds that define the 800 episodes on the fresh seeds are not part of the lock | (d), (b) | worth noting |
| F21 | The clause reads "seeds 3 and 4, both"; the ruling is three seeds, and the text does not say three of three or what a not-testable seed does to the across-seed condition | (d) | worth noting, must be fixed before registration |
| F22 | The matched-cell restriction reads the other-directed query on a subpopulation (episodes where the model revises) on which its intact level is unmeasured, while the engagement precondition is written on the whole battery | (d) | worth noting |

**The single most serious finding is F1 together with F6.** Under the
only damage operation the programme can currently read, the clause is
satisfied by arithmetic on any checkpoint like the three in hand, and
the calibration that is supposed to set its bar sets nothing. The
amendment's informative application, a localized lesion, is gated
behind a stack that has found nothing anywhere. So the half of A4 that
can be read cannot lose, and the half that could lose may never be read.

---

## (a) Ways a model with no ownership-specific structure satisfies the clause

### F1 — Under the input-channel lesion, the boring cell is unreachable

**Severity: fatal against the claim in §5.2 and §6.5 that "for the
first time the generic-binding cell can fire". ARGUED, from committed
numbers.**

The generic-binding cell requires S below σ with the self-directed drop
positive: the two conditions fall alike. Consider what "alike" can mean.

The other-directed drop per cell is at most the intact score minus
chance. On the seen seeds the control's intact scores are 0.2877,
0.3057 and 0.3195 (the endpoint findings, `seeds-endpoint-findings.md`),
so even a lesion that destroyed the control all the way to chance gives
a mean other-directed drop of at most about **0.19**. The self-directed
drop under the input-channel lesion is 0.37 to 0.43 on the same seeds
(intact 0.5683, 0.5633, 0.5738; lesioned 0.1988, 0.2015, 0.1447; the
proposal's own C1). C1 also says the three intact scores land within
0.011 of one another, and the seeds are byte-identical recipes, so the
fresh seeds are expected to look the same.

So the mean of the per-cell difference is at least about **0.17 raw in
the worst case for the hypothesis**, the case where the control is
annihilated, and about 0.30 in the case the record actually shows
(control falls about 0.06 to 0.07, see F5). The denominator is the
spread of that mean under random residual damage. The only band on the
record for this design is the A3 lock's 95th-percentile absolute
corrected drop on the primary battery, 0.1777, which is about 0.049
raw; a standard deviation is smaller than a 95th percentile, so the
spread is of order a few hundredths. S is therefore at least 3 to 5
even if the control collapses to chance, and around 10 in the case the
record shows, against a σ near 2 (F6).

**The generic-binding cell cannot fire under the input-channel lesion
on any checkpoint whose control sits where all three seen ones sit.**
Not "will probably not": cannot, because the comparator has about a
fifth of the self-directed battery's room to fall. This is the same
shape as the finding that killed the ratified A3 differential in
red-team pass 3 (RT-21, the two batteries' unequal ceilings biasing the
differential so a generic binder read as self-location): there the bias
came from unequal ceilings, here from unequal rooms to fall. The
registered metric's ceiling correction was adopted to remove exactly
this bias; §5 removes the ceiling and the bias returns in a softer form.

Put as the workspace's own wager rule asks: what result on seeds 3 to 5
would count against H_self-location under the input-channel lesion?
Only the self-directed battery not collapsing, which is C1's settled
result not replicating. A clause that can only lose by an already
replicated result failing to replicate a fourth time is not a wager on
the question it is named for.

### F2 — "Matched content" is not a matched condition; the lesion strikes where one score is read and not the other

**Severity: fatal against the reading "the damage is specific to the
ownership-dependent condition". ARGUED from the code.**

§3's case for Candidate B is that both queries live in the same episode:
"same turns, same items, same rule, same episode; only the agent whose
commitment is queried differs." That is true of the episode text. It is
not true of the two measurements.

- The self-directed score is read **at the model's own revision turn,
  inside the episode**, as the most likely of eight slot tokens at that
  position (`train_a3.eval_heldout`, the T_act block). That position is
  an enacted position: it is exactly where the acting channel injects.
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
