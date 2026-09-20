open, with the stack unvalidated at this scale.

## For the 2026-10-04 decision

The control-battery question now has its evidence. The choice is between a
registered Amendment A4 that makes the control learn, and closing A3 with
partial discriminators and saying so plainly. Whichever way it goes, the
proposal should carry three facts from this wave: the primary replicates
tightly across seeds, the control fails on all three rather than some, and
the ceiling adjudication permits exactly one amendment to the compute cap,
so an A4 needing new runs must make that argument explicitly.

> **CORRECTION, 2026-09-17. The last clause is withdrawn as misleading.**
> The single-amendment rule bars a **raise** above the $400 ceiling. An
> Amendment A4 that fits inside the existing ceiling is not a raise and
> needs no cap amendment at all. Three retrained seeds cost $27 to $39
> against $184.3 of remaining headroom and $65.69 left on the A3 stop, so
> money is not the binding constraint on this decision and I should not
> have implied it was.

## Method notes, recorded honestly

- Every figure is a mean across six evaluation seeds with its spread, not
  a single draw. Intact and lesioned are paired within each seed, so the
  drop is not exposed to between-seed noise even though the levels are.
- The pilot's published 0.506 and its 1.515 drop both came from the single
  default evaluation seed. Its typical values are 0.5683 and 1.337, so
  that seed flatters twice. The conclusion is unaffected; the headline
  number was simply lucky.
- The six seeds used here are the first six of the twelve in yesterday's
  noise measurement, so the spreads quoted understate the fuller estimate
  at this sample size. The wider one is the better figure.
- The control battery is reported and never read for a verdict, which is
  what the lock enforces by carrying no threshold for it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/register-lesion-findings.md =====

# Register-lesion + item-level diagnostics (anomaly threads 3 & 4)

*2026-08-19. Status: **diagnostic record, not adjudicated** — these are
the cheap threads the twin-binding anomaly note queued; nothing here is
a registered result and nothing here emits a verdict on H_load-bearing.
That read, and the wave-3 disposition, are John's. All runs local and
$0 [C1/C2]; per-run outputs in `lesion-results/`, no committed record
overwritten [C6]. Code: `src/lesion_register.py`, `src/item_analysis.py`,
`src/pick_analysis.py`.*

## Thread 4 — the register lesion: binding survives everything

Pre-stated in `twin-binding-anomaly.md`: "If the pilot's binding
survives the lesion, then even the one clean success was never
register-dependent and the construct problem is total rather than
partial." **It survives. All of it.**

Harness: the registered held-out eval (`train.eval_heldout`, n=100),
run twice per condition — the registered seed 987654321 (the eval the
endpoint rows report) and a disjoint replicate (20260819). The intact
baseline reproduces the committed endpoint row bit-for-bit (T_si 0.93 /
T_sr_rev 1.00), validating the harness. The lesioned model performs
the ENTIRE eval — enactment forwards and acting-channel injections
included. Four lesions on the bound pilot (`fd1eb80c…`), each an
instance-level patch with the canonical `forward` untouched:

| lesion | what it removes | T_si (reg. seed / repl.) | T_sr_rev |
|---|---|---|---|
| none (baseline) | — | 0.93 / 1.00 | 1.00 / 1.00 |
| frozen-writes | all accumulated content (shared init only) | 0.93 / 1.00 | 1.00 / 1.00 |
| keys-only | all content read (marker keys survive) | 0.93 / 0.99 | 1.00 / 1.00 |
| **no-xattn** | **the register injection entirely** | **0.94 / 0.99** | **1.00 / 1.00** |
| shuffle-binding | correct key→content binding (deranged read) | 0.93 / 1.00 | 1.00 / 1.00 |

T_sr / T_state / T_syntax: ≥0.99 everywhere. Full record:
`lesion-results/register_lesion_pilot_a1_30m_seed0.json`.

**This is not a dead pathway.** Verified before trusting a null this
clean: removing the injection shifts logits substantially (mean |Δ|
0.22, max 5.2 over 32 episodes), and the xattn residual stream is
LARGE (per-block mean norms 18–275 vs 3–14 for the ln1 trunk read) —
the trained model routes real activation mass through the registers.
But **shuffle-binding barely moves the logits at all (mean |Δ| 0.014)**:
whatever the registers hold is nearly identical across the four agent
rows. The register is numerically active and informationally inert —
a learned bias channel, not an agent-indexed store.

**Consequence (the pre-stated branch): the construct problem is
total.** The one checkpoint whose self-battery pass the design counted
as clean computes those answers entirely in the trunk. Combined with
wave 1–2 (a register-less twin binding, two registered fulls not
binding), no observed binding anywhere in the 30M data is
register-dependent.

## Thread 3 — item-level analysis: what the batteries actually measure

Per-item scoring of all five local 30M checkpoints on the registered
held-out eval at n=400 (`lesion-results/items_*.jsonl|summary.json`).
The split is stark and identical in kind across architectures:

| checkpoint | arch | bound? | T_sr | T_sr_rev | T_si | T_si unique-item | T_si repeated-item |
|---|---|---|---|---|---|---|---|
| pilot seed-0 full | full | yes | 0.99 | 0.84 | 0.96 | **1.00** | 0.40 |
| seed-1 twin | twin | yes | 1.00 | 1.00 | 0.97 | **1.00** | 0.48 |
| seed-1 full | full | no | 0.95 | **0.00** | 0.34 | 0.34 | 0.32 |
| seed-0 twin | twin | no | 0.95 | **0.00** | 0.36 | 0.36 | 0.36 |
| seed-2 full | full | no | 0.95 | **0.00** | 0.34 | 0.34 | 0.24 |

Two phenotypes, and neither is "a self-index binding":

- **The "binder" phenotype is general associative retrieval.** Both
  binders are at ceiling on every unique-item query — T_si asks about
  OTHER agents' turns, keyed by per-episode markers, so this is
  marker×item→value retrieval with no self component. Their only
  losses are on repeated items, where they answer ~0.4–0.48: the
  battery draws the queried turn at random, so when an item was
  revised the recorded "correct" answer is a coin flip between the
  stale and current value — **a T_si item-construction defect**: a
  model with consistent latest-value semantics is marked wrong
  whenever the draw landed on the earlier occurrence.
- **The "non-binder" phenotype still tracks its own acts.** All three
  non-binders hold T_sr at 0.95 with a perfectly clean internal split:
  1.00 when the queried own turn is the FIRST own assignment (turn
  idx 0–3), exactly 0.00 when it is a revised later turn (idx 4–7).
  They maintain first-binding-wins memory of their own commitments
  while being unable to do general marker-keyed retrieval (T_si 0.34,
  flat across positions — no recency gradient; error picks scatter
  over the episode's values with only a mild tilt toward the queried
  agent, `pick_analysis.py`).
- **T_sr is not a self battery for unique items.** Episode items
  repeat only under revision, so a non-revised "where did you assign
  X" is answerable by pure item lookup — which is why every run,
  bound or not, sits ≥0.95 on it. The batteries' load-bearing cells
  were T_sr_rev and T_si all along, and thread 4 shows neither is
  computed from the register.

## The acting channel (no-act lesion, run on three checkpoints)

If non-binders cannot do marker-keyed lookup, their T_sr 0.95 must
come from the acting channel (own-turn values are generator-drawn and
style-canonicalized — the motor copy is the only authorship signal in
the input [A1/RT-17]). Zeroing `act_proj` at eval tests this. Intact
values are the committed endpoint rows (n=100, registered seed);
no-act shows registered seed / replicate
(`lesion-results/register_lesion_*_noact.json`):

| checkpoint | T_sr intact → no-act | T_si intact → no-act | T_sr_rev intact → no-act |
|---|---|---|---|
| seed-1 full (non-binder) | 0.96 → **0.16 / 0.17** | 0.33 → 0.31 / 0.28 | 0.00 → 0.25 / 0.50 |
| seed-1 twin (binder) | 1.00 → 0.98 / 0.98 | 0.96 → 0.96 / 0.97 | 1.00 → 0.50 / 0.50 |
| pilot seed-0 full (binder) | 1.00 → 0.79 / 0.72 | 0.93 → 0.94 / 0.99 | 1.00 → 0.25 / 0.25 |

Three reads, in decreasing confidence:

- **The non-binder's self-recall is acting-channel-borne.** T_sr
  collapses from 0.96 to ~0.16 (8-way chance = 0.125) the moment the
  motor copy is removed. This is the one place in the whole 30M record
  where an authorship mechanism is demonstrably load-bearing — and it
  is the trunk-input channel the twin also has, not the register.
- **The binding twin barely needs authorship at all.** Its T_sr holds
  at 0.98 without the acting channel because non-revised "you" items
  are unique-item lookups. Its battery ceiling is authorship-free
  almost everywhere.
- **The pilot's partial T_sr drop (→ ~0.75) reads as a mixed strategy
  plus distribution shift** — its T_state also slips to 0.92 under
  no-act (the twin's does not), so some of the drop is the trunk
  being off-distribution rather than authorship loss specifically.
  T_sr_rev cells are ~4–8 items at n=100; don't over-read them.

## What changed, in one paragraph

The live question after wave 2 was "what computation solves these
batteries?" It now has an answer with three legs: (1) the register
contributes nothing to any battery answer in the only checkpoint that
passed them — large activations, no information, no effect on a single
item; (2) the batteries decompose into unique-item lookup (solved by
everyone), general marker-keyed retrieval (a seed-lottery: 2 of 5 runs
found it, register irrelevant), and revised-item recency (found by
exactly the retrieval-finders, plus an item-construction defect in
T_si's repeated-item cells); (3) where authorship tracking is demonstrably load-bearing — the
non-binders' first-commitment memory, which collapses to chance
without the motor copy — it is carried by the acting channel, which
the twin also has; the binders' ceilings barely use authorship at
all. The instrument was registered to license "the constructed
self-index is doing work"; every leg of that license is now measured
to be false at 30M.

## Wave-3 bearing (John's call; options, not a verdict)

The registered remainder (7 runs ≈ $130) would measure the seed-rate
of the general-retrieval lottery on an instrument whose self-reading
is invalidated above. No outcome of those runs — any split of binders
and non-binders, any twin behavior — bears on H_load-bearing, because
thread 4 severs battery success from the register on the only
positive exemplar and wave 2 already produced a register-less binder.
The options as this note sees them: **(a)** halt the 5-seed remainder
and treat the ~$219 A2 headroom as available for a redesigned battery
(one where ownership is the ONLY disambiguator — e.g. every queried
item assigned by multiple agents, so lookup without binding cannot
answer; plus the T_si repeated-item fix); **(b)** run the already-
registered θ/δ null calibration (~$2–5) for the record before any
redesign; **(c)** continue wave 3 as registered anyway — defensible
only as a pre-committed-procedure completion, not as evidence-buying.
Any change to the registered plan is itself a registered amendment.


===== FILE: experiments/06-mvm-0a-constructed-self-index/register-saturation-findings.md =====

# The register is constant in every trained checkpoint

*2026-09-16. Local, $0, inference only. Ruled by John. Descriptive
survey, no bin and no threshold a verdict turns on. Raw per-turn numbers
in `a3-gates/register_saturation_survey.json`.*

## What was asked and what was found

John ruled: *"Check whether the register is constant in the other
register-bearing checkpoints (pilot seed 0 full, s1 full, s2 full), and at
any saved intermediate steps, to see when it saturated. Report per
checkpoint."*

**It is constant in all of them.** Every trained register-bearing
checkpoint collapses at the same turn, and the writer emits the same
vector whatever it is given, from its very first write.

| checkpoint | step | collapse turn | written-row spread across episodes |
|---|---|---|---|
| pilot seed-0 full | 102095 | 3 | 7.6 × 10⁻⁸ |
| pilot seed-1 full | 102095 | 3 | 2.8 × 10⁻⁸ |
| pilot seed-2 full | 102095 | 3 | 5.9 × 10⁻⁸ |
| 10M pilot | 22369 | 3 | at floor |
| **untrained, same config** | **0** | **never** | **3.3 × 10⁻¹** |

The two twins are register-less by construction and have no register to
measure. They are listed and skipped rather than silently absent. One
older 10M checkpoint predates the current module and will not load
strictly; it was skipped rather than loaded loosely, because loading it
loosely would have measured randomly initialized weights and reported them
as that checkpoint's.

## A correction to what I wrote earlier today

The direct probe findings say the register "carried episode-specific
content early and that content was about something else". **That is
wrong and is withdrawn here.** The original sentence stays in place in
that note with an annotation pointing to this one.

The mistake was reading the flattened register. It mixes two things: what
was written, and which of the four agent rows it went into. Which row is
written varies by episode, because agents speak in different orders. So
the apparent variation at turns 0 to 2 was variation in **which rows had
been filled yet**, not in their contents.

Isolating the written row shows the truth. Across-episode spread of the
row just written sits at the floating-point floor from **turn 0**, in all
three 30M checkpoints. By turn 3 all four rows have been filled in every
episode, so even the fill-pattern difference disappears and the flattened
register goes constant too.

**The register never carried episode-specific information at any point.**
Not degraded, not lost after a few turns. Constant from the first write.

## When it saturated

No intermediate-step weights were saved by any of these runs, so the
training-time onset cannot be read off disk. That is a real limit and no
amount of care recovers it from what exists.

It can be bounded from the other end, and that bound is informative. An
untrained model at the same configuration does **not** collapse: its
written values vary across episodes with a spread of 0.33 rising to 0.54,
and all 200 episodes give distinct register states at every turn from turn
2 on. So the constancy is **trained in, not architectural**. The
architecture can carry episode-specific state. Training drove it to stop.

What is measured precisely is the within-episode onset: turn 3 in every
trained checkpoint, which is simply the turn by which all four rows have
been overwritten with the constant.

## What it looks like mechanically

The register moves away from its initialization in equal steps and then
freezes exactly. On seed 0 the mean distance from initialization goes
0.0817, 0.1633, 0.2450, 0.3267 and then stays at 0.3267 for every
remaining turn. Those are one, two, three and four quarters of the same
number, which is what you see when each turn overwrites one of four rows
with the same target vector and nothing changes after the fourth.

The writer's input varies enormously the whole time, with per-feature
spreads around 30 to 40 and maxima from 145 to 355. Episode-specific
content reaches the writer at every turn and does not come out. The
mechanism is consistent with gate saturation in the recurrent update at
those input magnitudes. **That remains an inference from the magnitudes,
not a measurement.** What is measured is that the input varies and the
output does not.

## The consequence John named

If the register contributes a constant, the trunk reads a constant through
cross-attention, and a constant input is a bias term. **The full model is
the twin plus a learned bias.** The manipulation the A2 design turned on,
having a per-agent register versus not having one, was never applied in
any effective sense.

The binding results line up with that exactly. Two of five checkpoints
bind, and they are one full and one twin:

| checkpoint | architecture | bound? |
|---|---|---|
| pilot seed-0 full | full | **yes** |
| seed-1 twin | twin | **yes** |
| seed-1 full | full | no |
| seed-0 twin | twin | no |
| seed-2 full | full | no |

Binding does not track architecture. It tracks seed. That is what a
lottery in a single architecture looks like, and it is what the wave-2
"prediction inverted" result was reading.

**So the wave-2 result should not be read as a prediction inverting.** A
prediction about register-bearing versus register-less models cannot
invert, or hold, on a comparison where both arms are the same model up to
a bias term. The honest description is two of five seeds binding in one
architecture.

This is recorded as an annotation on the wave-2 ledger row and findings
note. Per John's standing instruction those are **annotated, never
edited**: the original text and the original reading stay exactly as
written, with a dated note beside them.

## What this does not say

It does not say the A2 runs were wasted or that the binding measurements
were wrong. The batteries measured what they measured, and two checkpoints
really do bind. What is withdrawn is only the architectural
**interpretation** laid on top of that comparison.

It also says nothing about A3. A3 is register-less by construction and its
authorship signal is the acting channel, which is measured load-bearing on
the pilot at 0.506 against 0.182. Nothing here touches that.


===== FILE: experiments/06-mvm-0a-constructed-self-index/register-direct-probe-findings.md =====

# Unblinded direct register probe — result

*2026-09-16. Local, $0, inference only. Ruled by John after the blind
arm's verdict was committed. Criteria committed before the run at
`8884b31`. Unregistered and labelled so. This is a follow-up diagnostic,
not a registered arm.*

## The headline

**The register never encoded own-agent identity, at any turn.** Not at
the end, where it is a constant vector identical across every episode,
and not in the early turns, where it does vary across episodes but
carries nothing about which agent the model is.

So the blind arm's sub-bin name is wrong. **"Instrument failure to locate"
presumed there was something to locate. There was not.**

> **ANNOTATION, 2026-09-16 (John's ruling).** The name is **not retired**;
> the sentence above is left as written. What is wrong is the
> interpretation the name invites, not the bin the result fell into under
> the criteria in force. The committed verdict carries a dated annotation
> beside it reading *superseded in interpretation by the unblinded
> register probe: no valid target.* Reasoning at the end of this note.

## First, a defect in my own pre-stated rule

The pre-stated rule was `accuracy >= null_mean + 3 * null_sd`. Applied to
the primary probe it returns **reading 1, sensitivity failure**. That is
an artifact and I am reporting it rather than quietly repairing it.

| quantity | value |
|---|---|
| probe accuracy | 0.2700 |
| null mean | 0.2700 |
| null standard deviation | 0.0000 |
| margin | undefined |
| majority-class rate | 0.2700 |

The inequality reads `0.27 >= 0.27 + 0`, which is true. The separation is
**zero** standard deviations, not three. Three independent signs say the
input was degenerate:

1. The permutation null has zero spread. Every permutation scored
   identically, so the rule compared a number to itself.
2. The margin in standard deviations is undefined, a division by zero.
3. The accuracy equals the majority-class rate **exactly**. That is the
   score of a classifier that ignores its input and predicts one constant
   class, which is all it can do when every episode hands it the same
   vector.

I did not change the rule's output. A degeneracy guard was added to the
module afterwards, reporting the literal result unchanged alongside the
three signs, and it assigns no bin. The guard is a validity check on the
rule's **input**, in the same category as the Gate 0 escalation check. It
is not a new bin, and the self-test now covers the degenerate case.

**Formally this result fits none of the pre-stated readings as written**,
because reading 1's inequality is satisfied but void. John rules on how
to record it. My reading of the evidence is below, and it is reading 2.

Stated plainly because it cuts against me: the pre-stated criteria were
written by me and this is a hole in them. A rule of this shape needs a
non-degenerate null as a precondition, and mine did not say so.

## The evidence, which is not ambiguous

**The register is constant across episodes at the point the primary probe
read it.** Across-episode standard deviation averages 1.68 × 10⁻⁷, with a
maximum of 8.34 × 10⁻⁷. That is float32 rounding. The 107 nominally
distinct rows out of 400 differ only at that level.

It is not untouched, though. It moves from its initialization by 0.327 on
average and 1.29 at most. **The register is saturated, not idle.** It
holds a fixed vector that is the same whoever the model is and whatever
happened in the episode.

**The one probe with a valid null also sits at chance.** The
trunk-visible projection, which the model actually reads through
cross-attention, does vary across episodes because the marker keys differ.
Its null is healthy.

| probe | accuracy | null mean | null sd | margin |
|---|---|---|---|---|
| trunk-visible projection | 0.2375 | 0.2369 | 0.0234 | 0.03 sd |

Against a bar of three standard deviations, that is 0.03.

## Was identity there earlier and destroyed?

This mattered enough to check, because "empty" is ambiguous between a
register that never held identity and one that held it and lost it. The
two have different consequences for the design.

The register is not constant at every turn. Within a forward pass it
varies across episodes for the first three writes and collapses
thereafter. Probing every turn of the graded pass, same imported probe and
null:

| turn | across-episode sd | accuracy | margin |
|---|---|---|---|
| 0 | 1.41 × 10⁻¹ | 0.3050 | 1.82 sd |
| 1 | 1.63 × 10⁻¹ | 0.2600 | 0.17 sd |
| 2 | 1.41 × 10⁻¹ | 0.2500 | −0.11 sd |
| 3 to 7 | ~1.68 × 10⁻⁷ | degenerate, constant across episodes | — |

The pre-collapse turns have real variation and healthy nulls, and their
margins are 1.82, 0.17 and −0.11 standard deviations. All are under the
bar. **The register never encoded own-agent identity.** It carried
episode-specific content early and that content was about something else.

> **ANNOTATION, 2026-09-16, later the same day. The last sentence above
> is WRONG and is withdrawn.** It stays in place rather than being
> deleted, so the correction is visible.
>
> The register carried no episode-specific content early either. I had
> read the *flattened* register, which mixes what was written with which
> of the four agent rows it went into, and which row is written varies by
> episode because agents speak in different orders. The apparent variation
> at turns 0 to 2 was variation in **which rows had been filled yet**, not
> in their contents.
>
> Isolating the row just written shows across-episode spread at the
> floating-point floor from **turn 0** in all three 30M full checkpoints.
> The writer emits one constant vector whatever it is given, from its
> first write. So the conclusion in bold above is not merely right, it is
> stronger than the evidence I gave for it: the register was never
> carrying episode-specific information of any kind, rather than carrying
> something that turned out not to be identity.
>
> Measured in `register-saturation-findings.md`.

This diagnostic was added after seeing the primary result and carries no
pre-stated bin. It is reported as description.

The 1.82 at turn 0 is the largest margin anywhere in this work and still
falls short. It should not be read as a near-miss: it is one of three
valid tests here, and more were run across the blind arm's five layers, so
the multiple-comparison correction pushes it further down. Nothing turns
on it.

## Where the collapse happens

Inside the writer. The writer's input, the attention-pooled top-layer
states, varies enormously across episodes at **every** turn, with
per-feature standard deviations around 30 to 40 and maxima from 145 to
355. So episode-specific content reaches the writer and does not come out.

The mechanism is consistent with gate saturation in the recurrent update
given inputs of that magnitude, which would drive the hidden state to a
fixed point regardless of input. **That is an inference from the
magnitudes, not a measurement**, and it is labelled as one. What is
measured is that the input varies and the output does not.

## What this does to the blind arm's record

**The blind arm result says nothing about the localization stack's
sensitivity, in either direction.** Not because the evidence is weak, but
because the arm had no target. A search for a structure that is not there
cannot demonstrate either that the instrument finds things or that it
misses them.

This sharpens both of John's corrections rather than softening them:

- On specificity, the corrected record already said no false positive was
  produced by an instrument that produced no positive of any kind. That
  now reads as generous. The instrument was pointed at a checkpoint whose
  designated self-structure was constant.
- On Experiment 1, the record already said this result is not evidence
  that Experiment 1's null was instrument blindness. That stands, and the
  ground under it is firmer: nothing here is evidence about instrument
  blindness at all.

The sub-bin name **"instrument failure to locate" should be retired** for
this arm, and the honest description is **no valid target**. That is a
change to how the blind result is described and John should rule on it,
since the sub-bin was part of the pre-stated criteria.

> **RULED 2026-09-16: NOT RETIRED.** The recommendation above is left
> standing rather than deleted, so the record shows both what was proposed
> and what was decided. John: "The committed verdict and its pre-stated
> name stand as written. Add a dated annotation beside it ... Annotate,
> never rewrite."
>
> His ruling is the better discipline and the reason is worth stating. A
> pre-stated name records which bin a result fell into under the criteria
> in force when it ran. Renaming it afterwards, even for a good reason,
> makes those criteria unfalsifiable in retrospect, because a later reader
> cannot tell which names were committed and which were fitted to the
> result. Annotation keeps both the commitment and the correction visible.
>
> The superseding interpretation is recorded as a dated annotation beside
> the verdict in `blind-arm-findings.md` and in `STATUS.md`: *superseded
> in interpretation by the unblinded register probe: no valid target.*

## What it says about the A2 architecture

This is a finding about the build, not only about the instruments. The
register was constructed to hold per-agent state. In the trained 30M
checkpoint it holds a constant after three turns and never encoded agent
identity at any point.

It also explains the earlier register lesion result rather than merely
agreeing with it. Removing the register injection entirely changed
nothing, and deranging which register is read moved logits by a mean
absolute 0.014. Of course it did. A constant injection is a bias term, and
permuting which constant you read changes nothing because they have
converged to the same place.

## What this changes downstream

The companion positive control, which John ruled yes on, is now **the only
remaining route to any sensitivity reading** on the localization stack.
Before this probe it was the better of two routes. It is now the only one.

The control-battery proposal due 2026-10-04 should carry this: whatever
else Amendment A4 decides, a register that saturates to a constant after
three turns is a design defect, and any future architecture claiming to
carry a self-index needs a check that the carrier still varies at the
point where it is read.


===== FILE: experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md =====

# The control battery's ceiling is 1.0, and the clause was never computable

*2026-09-17. Method committed before running at
`ceiling-measurement-method.md` (`2fba2ea`). No checkpoint loaded, no
inference, no spend. 4,000 episodes.*

## Verdict: A — STRUCTURALLY UNSATISFIABLE

**The registered differential clause could never have been computed. Not
by these models, not by any model, at any training budget, on any
architecture. It has been dead since registration.**

## The harness proved itself first

Both known-answer checks reproduced their registered values **exactly**,
to four decimal places, before any new number was reported:

| check | measured | registered |
|---|---|---|
| control, name-blind reference | 0.3227 | 0.3227 |
| primary battery reference | 0.2921 | 0.2921 |

So the harness reproduces the registration's own arithmetic. What follows
is not a different calculation quietly substituted.

## The measurement

| solver | score |
|---|---|
| name-keyed lookup | **1.0000** |
| registered name-blind reference | 0.3227 |
| learned attack | **1.0000** |
| **best of family** | **1.0000** |

Two independent solvers reach a perfect score. The hand-written one reads
