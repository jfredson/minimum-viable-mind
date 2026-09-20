
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
  `vocab: 105` (read from the `.pt` files' `cfg`). The twin's token
  embedding and output head are 103 wide.
- No bridge exists: a search of `src/` for any remapping between the two
  vocabularies finds none; `encoding_a3.py`'s own self-test only asserts
  that the registered vocabulary was not edited.

So the twins cannot be fed A3 episodes without new code that maps ids,
and whatever mapping is written after registration decides what the
twin "sees" and hence what its null looks like. Even with a mapping,
a model reading a scrambled or shifted vocabulary is not "a trained
model out of distribution" as §5.5 describes it; it is a random reader
whose answers are noise of an unknown shape. The precedent §5.5 cites,
Gate 0 calibrating on the existing checkpoints, ran those checkpoints
on **their own** grammar and tokenizer. Only the untrained substrate
survives, and see F16.

### F16 — The untrained substrate risks a zero-spread null, and the maximum rule turns that into no threshold or an unreachable one

**Severity: serious. ARGUED, with this week's precedent.**

An untrained network at this configuration produces, at the revision
position and at the answer position, whatever its random head favours
among eight slot tokens; that choice can be nearly constant across
episodes or flip on small perturbations, and which of the two is not
known until it is run. Rank-4 to rank-16 random residual damage at five
layers is small relative to the residual norms (the A3 pilot record
shows removed norms of 10 to 18 per layer against reference means of 66
to 205). If few or no per-cell scores flip, the per-cell difference is
zero almost everywhere, the spread across draws is near zero, and S is
either 0/0 or a handful of flips divided by almost nothing. §5.5 then
takes the maximum 95th percentile across substrates, so a degenerate
untrained null gives either no σ or a σ far above anything a learned
model's shaped null reaches. The control diagnostic of 2026-09-17
failed on exactly a zero-spread null by construction
(`control-diagnostic-findings.md`), and that document's own lesson was
to write a non-degeneracy precondition into every null. §5.5 has none.

### F17 — Condition (f)'s validity gates have never been applied to this lesion and have no A3 implementation

**Severity: serious. MEASURED.**

(f) carries over "verbatim from Amendment A3 §3.3" the neutral-episode
likelihood bound, the long-generation degeneracy probe and the
out-of-distribution-inconclusive branch. A search of `src/` finds no
neutral-episode likelihood bound and no degeneracy probe implemented
for the A3 grammar (the only "degenerate" checks are the zero-spread
guards in the control diagnostic and the blind control). The endpoint
records for seeds 0 to 2 carry no such field among their 110 keys. So
the input-channel lesion has never been tested against these gates on
any seed. Zeroing an input the model was trained with moves every
battery (F2, F5), so it is plausible it also moves the neutral-episode
likelihood past a 95th-percentile random-damage bound. If (f) is built
and applied on the fresh seeds, all three may return NOT TESTABLE on
the first application of a gate that was never run on the seen seeds;
if it is not built, (f) is a sentence. Either the gates are implemented
and run on the seen seeds before registration, with the result
reported, or (f) should say what it actually binds.

### F18 — The random baseline is not matched to the input-channel lesion in any stated sense

**Severity: serious. ARGUED from the code.**

§5.4(a) describes the baseline as "random removals of the same rank and
the same norm, at the same layers" as the damage operation. For a
localized subspace lesion that is meaningful. For zeroing `act_proj`,
a 448-by-448 projection that injects at the model's own enacted
positions only, it has no rank in the residual stream, no layer among
3, 4, 5, 7 and 8, and a norm concentrated at three positions rather
than spread over all of them. The Gate 0 machinery applies random
damage to all positions at fixed layers with strengths set by a
reference pass. A3's endpoint used that sweep as the input-channel
lesion's null anyway, which is a defensible precedent as long as the
text says "the registered residual sweep, unmatched to this lesion";
§5's text promises a matched baseline the machinery cannot produce, and
a reader will take "matched-strength" at its word.

### F19 — Per-cell scoring is a new instrument, and its first run would be the verdict

**Severity: serious. MEASURED.**

The A3 evaluation function returns per-battery accuracies rounded to
three places and nothing per episode (`train_a3.eval_heldout`); the
endpoint script stores per-evaluation-seed means. The clause needs a
per-cell record of intact and damaged correctness for two or three
batteries on the same 800 episodes, the pairing of the self-directed
read (inside the episode) with the appended reads (after it), the
within-run baseline, and the ladder. That is a new scoring path. The
known-answer rule of 2026-09-16 (`lock_guard.require_known_answer_pass`
and its ruling) exists because a new pipeline returned five probes
below their nulls and nothing separated an insensitive stack from a
bug. §5 registers no known-answer test for the separation script. A
cheap one is available and should be registered: the new script's
per-cell records for seed 0 must reproduce the seed-0 endpoint means
for every battery, intact and lesioned, to the rounding, before any
fresh seed is scored. (That reproduces published aggregates; it does
not compute the separation statistic on a seen seed.)

### F20 — The lock guard cannot hold this lock, and the evaluation seeds are outside it

**Severity: worth noting. MEASURED.**

`lock_guard.require_lock` (version 1) refuses a lock that lacks `theta`
and `delta` fields, requires a threshold entry for every battery about
to be read, and validates against exactly one calibration record by
hash. A σ lock carrying three calibration records and an exclusion
field is a new lock version and new guard code, written after
registration. §5.5 step 3's "through the existing lock-guard machinery"
is not literally available. Separately, the endpoint reads use six
evaluation seeds and report a spread; §5 does not say which seeds
define the 800 episodes the verdict is read on for seeds 3 to 5, and a
seed chosen after seeing the default-seed reading is a fit route. The
lock should carry the evaluation seeds.

### F21 — Two seeds in the text, three in the ruling

**Severity: worth noting; must be fixed before registration. ARGUED.**

Condition (h) reads "seeds 3 and 4, and must hold on both". John ruled
three fresh seeds. The registered text needs to say three of three (the
A3 rule), what a NOT TESTABLE seed does to the across-seed condition,
and where two of three lands (F13).

### F22 — The comparator is read on a subpopulation its precondition was not written on

**Severity: worth noting. ARGUED from the code.**

The other-directed and state queries are appended to every episode, and
their battery scores are over all 800. Matched cells exist only in the
roughly 400 episodes where the model's slot was drawn as a reviser. In
those episodes the model's own revision is visible and the named other
agent is one of the non-revisers or the co-reviser, so the
other-directed query's difficulty differs from the full battery's, and
its intact level on that subpopulation has not been measured. Condition
(d)'s 0.10 margin is written on the whole battery. The text should say
which population (d) is evaluated on and which the comparator's
"measured spread of change" (the ruling annotation's second addition)
is reported on.

---

## Two notes on time and money, because §5.5 depends on them

- **Calibration time.** The one A3 random sweep on the record took
  6,047 seconds for 120 draws at 800 episodes on the Mac. Three
  substrates is about five hours if the twins could run (F15), and a
  within-run spread on each fresh seed (F6, reading 1) is another 1.7
  hours per seed after arrival, before any verdict. That fits inside
  "lock before read" as ruled, but the lock cannot be cut before launch
  if the substrates need new code first, and the registration should
  say so rather than leaving §6.4's permission to cover it.
- **Nothing in this pass changes the cost estimate.** Every finding is
  fixable at $0 or is a reason not to spend.

---

## Kill case, in one paragraph

Under the only damage operation the programme can currently read, the
clause cannot fail on any checkpoint resembling the three in hand: the
comparator has a fifth of the self-directed battery's room to fall, so
the cell the repair exists to make reachable is arithmetically
unreachable, and the positive cell will fire with a many-sigma number
under the registered positive bin's name. The calibration that is meant
to set the bar sets a number near 2 on any substrate, and two of its
three substrates cannot be run because their tokenizer is not the A3
tokenizer. The application that would make the clause informative, a
localized lesion, is gated behind a stack that has found nothing on any
seed. So the $30 buys three more instances of C1's already replicated
result, relabelled. Close A3 on the record as it stands, state the
matched self/other contrast as the design's unmet requirement, and
register a separation clause only when there is a localized lesion to
read it on and a comparator that can fall as far as the battery it is
compared against.

## If it ships anyway: what §5 needs before it is registerable

Listed as remedies, not as amendment text; every one is $0.

1. Rename the positive cell for what it measures under the input-
   channel lesion; reserve H_self-location for the registered localized
   result (F9). Restore the ruled meaning of "located, wrong structure"
   and give the other-directed-falls-more event its own name (F10).
2. Make the outcome table exhaustive: cells for (a) holding while (c),
   (e) or (h) fails; for an improvement inside the band; for two of
   three; carry A3's seed-dependent and unstable bins (F13, F21).
3. Define the spread: on which checkpoint, over which draws, pooled or
   per cell, across draws not cells (F6). Say plainly that σ will land
   near 2 and why that is acceptable, or replace the self-normalized
   calibration with one that has content.
4. Replace the twin substrates or register the tokenizer bridge and its
   consequences before the lock (F15). Add a non-degeneracy precondition
   on every null and say what happens when it fails (F16).
5. Quantify condition (e) and say what happens when the other-index
   subspace cannot be localized (F14). Describe the baseline as the
   registered residual sweep, unmatched to the input-channel lesion, or
   design a matched one and register it (F18).
6. Either implement (f)'s gates for A3, run them on the seen seeds'
   input-channel lesion before registration and report the result, or
   strike (f) (F17).
7. Register a known-answer test for the separation script against the
   seed-0 endpoint means, to pass before any fresh seed is scored (F19).
   Extend the lock guard to a σ lock that also carries the evaluation
   seeds (F20).
8. Pre-state, in the registered text, the expected S on the fresh seeds
   computed from the seen endpoint records, and the minimum S reachable
   if the control collapsed to chance; report seen seeds under their
   own heading, never alongside fresh ones; state which cells were
   reachable on the checkpoint read (F1, F5, F11, F12).
9. State which population the engagement precondition and the
   comparator's reported spread are read on (F22), and carry the memo's
   admissions about data-informed choices into the registered text (F8).

---

*Authorship: this pass is Claude's. Nothing in it is a ruling. It does
not edit the proposal, does not write the amendment, and did not open
the amendment draft, the first red-team pass or the scoring script that
were on disk when it ran.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/control-battery-proposal.md =====

# The control-battery decision — proposal for John, due 2026-10-04

*2026-09-17. **Advisory only; John adjudicates.** Decision-memo pattern:
constraint set, then what the audit changed, then candidates, then one
recommendation. Nothing here authorises spend or changes registered text.
Written after the seeds reported, as the roadmap specified.*

## The question

Three trained checkpoints. The ownership objective learns on all three and
its removal lesion is enormous. The control battery never learned on any
of them, so the registered clause comparing the two cannot be evaluated
anywhere. Does the programme open a registered Amendment A4 that makes the
control learn, or close A3 with partial discriminators and say so plainly?

## What is settled

| | pilot | seed 1 | seed 2 |
|---|---|---|---|
| primary, intact | 0.5683 | 0.5633 | 0.5738 |
| primary, channel zeroed | 0.1988 | 0.2015 | 0.1447 |
| corrected drop | 1.337 | 1.342 | 1.528 |
| control, intact | 0.2877 | 0.3057 | 0.3195 |

The primary result is not in doubt and is not marginal. The control's
failure is systematic rather than a seed lottery, which is what the wave
was run to find out.

## Four things the audit changed, and they matter more than the numbers

**1. The bar is higher than I have been saying, and I was wrong about it.**
The floor rule is not "the baseline must clear the ceiling." It is
`baseline − ceiling ≥ 0.10`. So the control needs **0.4227**, not 0.3227.
All three miss by 0.103 to 0.135, so no conclusion moves, but an A4
argument that merely clears 0.3227 would still leave the drop undefined.
My findings note said "below its own ceiling" and is corrected.

**2. The control's ceiling was never attack-verified.** The registration
says the ceilings are verified by the attack sweep. **The attack sweep
contains no control-battery code at all** — zero occurrences. It attacks
the primary battery only. The 0.3227 rests entirely on one reference
solver in the curriculum module.

**3. That reference solver is blind to the thing the question hands it.**
The control question **names** the agent it asks about. The solver that
sets the ceiling never uses that name; it enumerates the four agents'
successors and guesses among those not already visible. A solver that can
do ordinary name-keyed lookup answers correctly every time.

So 0.3227 is not a ceiling on the battery. It is the score of a solver
that cannot read names, and the battery's real ceiling is near 1.0.
**This is the deeper problem, and it cuts both ways.** It means the
control at 0.32 is far worse than it looked, since it is barely above a
solver that ignores half the question. It also means the metric's
denominator for this battery was never a meaningful quantity.

**4. The design warned about this and the warning was never acted on.**
The curriculum module's own documentation says the control's lookup
ceiling is **0.5**, not 0.3227, and says in terms that *"red-team pass 3
should weigh"* it *"since the H_generic-binding bin turns on the
difference between the two batteries' drops."* Red-team pass 3 ran. It did
not weigh this. The registered number and the module's own comment have
disagreed since before the first dollar was spent.

## Why the control plausibly failed, from the code

It is **not** unsupervised. Each episode carries three queries and one is
chosen per training row, so roughly **one row in three** carries a control
target, one token each. Against that, the primary battery has a dedicated
full-weight loss term of its own on the roughly half of rows that carry an
action. The control gets perhaps a third of one shared term, with two easy
queries soaking up most of it.

Three further asymmetries, all in the code:

- **The primary battery has a private route the control does not.** The
  acting channel marks the model's own earlier value positions directly.
  The control must bind a name to a value across turns by ordinary
  attention, with no such help.
- **The rendering was reversed for the primary battery's benefit.** The
  speaker's name was moved after the value to kill a name-reading shortcut
  on the primary battery. The consequence for the control, which must now
  attend backwards from a name to a value two tokens earlier, was never
  revisited.
- **The answer appears in no turn.** It must be retrieved and then
  transformed by the revision rule. Retrieval and arithmetic both, from
  one supervised token.

## A correction on the money, in the programme's favour

I wrote in the seeds findings that an A4 needing new runs "must make that
argument explicitly" against the single-amendment ceiling rule. **That was
misleading and is withdrawn here.** The rule bars a *raise* above $400. An
A4 that fits inside the existing ceiling is not a raise and needs no cap
amendment at all.

| envelope | spent | remaining |
|---|---|---|
| A2 ceiling | $215.7 | **$184.3** |
