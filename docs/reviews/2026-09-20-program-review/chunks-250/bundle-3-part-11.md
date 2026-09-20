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
