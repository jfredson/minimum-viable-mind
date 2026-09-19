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
