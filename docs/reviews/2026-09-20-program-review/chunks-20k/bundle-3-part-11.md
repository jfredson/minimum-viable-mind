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
| A3 hard stop | $34.31 | **$65.69** |

Three retrained seeds cost **$27 to $39** at measured rates. That fits
inside both, comfortably. Money is not the binding constraint on this
decision, and I should not have implied it was.

## Candidates

**A. Close A3 with partial discriminators.** Report the primary result,
the instrument audit, and the undefined comparison. *Cost $0.* Honest, and
weaker than it sounds: the discriminators that do not need the control are
the matched other-agent lesion, the random matched subspaces and the swap
probe — all of which run through a localization stack that has so far
found nothing, with probes below their own nulls and an ablation that
improved the battery it was meant to damage.

**B. Eval-side A4: divide by chance instead of the ceiling.** *Cost $0.*
At chance all three checkpoints would clear the floor and the comparison
would become computable. **Reject.** The ceiling denominator was itself a
registered revision made because dividing by chance manufactured a
spurious differential. Changing it back after seeing that it blocks the
result is fitting the rule to the data, which is the thing this programme
exists to not do. It would be the third time in two days that a rule of
mine was found wanting by the data, and the first two were reported rather
than repaired for exactly this reason.

**C. Retrain with the control properly supervised.** *Cost $27–39, three
seeds.* One change: give the control its own loss term or oversample it,
instead of a third of a shared one. No grammar change, so the frozen
batteries, the cue gates and the attack sweep are all unaffected.

**D. Retrain with a scaffolded intermediate query.** *Cost $27–39 plus
re-freezing batteries.* Teach plain name-keyed retrieval before layering
the rule on top.

**E. Train longer or bigger.** **Fenced by the registration**, which says
the finding is "unlearnable at this scale under this curriculum" and never
a silent scale bump.

## Recommendation

> **ANNOTATION, 2026-09-17, later the same day. The candidates below are
> MOOTED and the recommendation is superseded, though its one operative
> instruction was right.**
>
> The ceiling measurement John made a precondition has now run. The
> control battery's ownership-blind ceiling is **1.0**, reached by two
> independent solvers, with both known-answer checks reproducing their
> registered values exactly first.
>
> A defined drop needs a baseline of 1.10, so **the control's drop is
> undefined for every possible model** and the registered differential
> clause was never computable, at any budget, on any architecture. It has
> been unsatisfiable since registration.
>
> **So options C and D below are moot.** Both aimed at making the control
> learn, and a perfectly learning control would change nothing. I was
> proposing to spend $27 to $39 repairing the wrong component. What caught
> it was John's instruction to measure the ceiling before opening an
