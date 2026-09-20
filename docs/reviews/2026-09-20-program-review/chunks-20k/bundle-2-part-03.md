---

## What needed John, and what still does

All three items that stood open on 2026-09-16 morning are **ruled**, above:
the bin (recorded as described, not binned), the undefined control drop
(strict reading, seed 0 not-testable on the differential clause), and the
seeds (one wave, on a fresh verbatim go).

**What still needs John**, in the order the registered procedure takes it:

1. **The threshold lock commit.** Reserved to him by §3.3. The thresholds
   are measured and waiting (`null-calibration/a3_pilot_seed0.json`):
   0.1777 on the primary battery, 0.2368 on the one computable
   differential. `lock_guard.py` refuses any localized-subspace run until
   that commit exists.
2. **A fresh verbatim go for the seeds 1 and 2 wave.** Neither ruling is
   one, and the go is quoted in the ledger row before spend.
3. **After seeds 1 and 2 report**, whether optional extra seeds run. The
   revision entry reopened this: seven seeds total roughly $77–105
   including the $13.92 spent, borderline rather than clearly past the
   $100 hard stop, so a checkpoint whose control learned stays a live
   route.


===== FILE: experiments/06-mvm-0a-constructed-self-index/seeds-endpoint-findings.md =====

# A3 seeds 1 and 2 — registered L0 endpoint

*2026-09-17. Local, $0, inference only. Run through `endpoint_a3.py`,
which was validated against the pilot first and reproduces its published
endpoint to the digit. Gated on John's threshold lock, which supplies
θ = 0.1777 on the primary battery and carries no threshold at all for the
control battery. Checkpoints verified by checksum.*

## What the wave was for, and what it answered

The ledger row staked the wave on two questions: whether the primary
battery's learnability **replicates**, and whether the control battery's
failure is a **seed lottery**. Both now have answers.

**Learnability replicates.** **The control is not a lottery; it fails on
every seed.**

## The primary battery

Across six independent evaluation seeds at n=800, reported as a spread
rather than a single draw:

| checkpoint | intact | under L0 | ceiling-corrected drop | vs θ |
|---|---|---|---|---|
| pilot (seed 0) | 0.5683 (sd 0.0076) | 0.1988 (sd 0.0173) | 1.337 (sd 0.057) | 7.5× |
| seed 1 | 0.5633 (sd 0.0316) | 0.2015 (sd 0.0215) | 1.342 (sd 0.103) | 7.6× |
| seed 2 | 0.5738 (sd 0.0284) | 0.1447 (sd 0.0127) | 1.528 (sd 0.068) | 8.6× |

Three checkpoints trained from different seeds land within 0.011 of each
other on the intact score. Zeroing the acting channel collapses all three.
Every drop clears the locked threshold by between seven and nine times,
and a drop above 1.0 means the lesion took the battery **below** what an
ownership-blind solver reaches.

This is as clean a replication as the design can produce. The objective is
learnable and the learning genuinely depends on ownership.

## The ownership-free controls

| checkpoint | state battery drop | syntax battery drop |
|---|---|---|
| pilot (seed 0) | +0.0018 | 0.0000 |
| seed 1 | +0.0002 | 0.0000 |
| seed 2 | **+0.0769** | 0.0000 |

The syntax battery does not move at all on any checkpoint. The state
battery is untouched on two and moves 0.0769 on seed 2, which is forty
times the others.

**That does not fire** — the locked threshold for the state battery is
0.1172 and 0.0769 is well inside it — but it is reported rather than
rounded away, because it is the only asymmetry in the table and a
write-up that shows the other two without it would be flattering.

## The control battery, which is the finding

| checkpoint | intact | its ownership-blind ceiling | learned? |
|---|---|---|---|
| pilot (seed 0) | 0.2877 (sd 0.0302) | 0.3227 | no |
| seed 1 | 0.3057 (sd 0.0281) | 0.3227 | no |
| seed 2 | 0.3195 (sd 0.0150) | 0.3227 | no |

**On all three checkpoints the control battery sits below its own
ownership-blind ceiling.** A battery scoring under the level a solver
reaches without knowing which agent it is has not learned the task. Seed
2 comes closest, 0.3195 against 0.3227, and still does not clear it.

The consequence is mechanical. The registered floor rule leaves a
battery's drop **undefined** when its baseline is below its ceiling, so
the control's drop is undefined on every checkpoint, and the registered
differential clause — the primary's drop minus the control's — **cannot
be evaluated on any of the three.**

> **CORRECTION, 2026-09-17.** The sentence above understates the bar and
> is corrected here rather than rewritten. The floor rule is not
> "baseline below ceiling"; it is **baseline minus ceiling below 0.10**.
> So the control needs **0.4227**, not 0.3227, for its drop to be
> defined, and the three checkpoints miss by 0.135, 0.117 and 0.103
> rather than by the 0.035, 0.017 and 0.003 the table implies.
>
> No conclusion changes — the clause is uncomputable either way — but the
> gap is four to forty times wider than the table suggests, and an
> Amendment A4 that merely cleared the ceiling would still leave the drop
> undefined. See `control-battery-proposal.md`.

John ruled seed 0 not testable on the differential clause on 2026-09-16.
That ruling now extends to the whole wave, not by a further ruling but by
the same arithmetic applied to two more checkpoints.

## What this settles, and what it does not

**Settled: the control battery does not learn under this design.** Three
seeds, one outcome. It was the modal case the ledger recorded against the
wave before the go was given, and it came true. A recorded case-against
that comes true is worth more than a prediction that does not, and this
one removes the remaining hope that the control was a lottery.

**Therefore A3 as registered cannot return a positive on any checkpoint
it has.** Not because the primary failed — it succeeded on all three, by a
wide margin — but because the clause that compares it to a control cannot
be computed when the control never learned.

> **ANNOTATION, 2026-09-17. The conclusion stands; the reason given here
> is wrong and is corrected.** The clause cannot be computed **whether or
> not the control learned**. Its ownership-blind ceiling is 1.0, so a
> defined drop would need a baseline of 1.10 and no model can reach it.
> The clause was unsatisfiable from registration, months before any
> checkpoint existed, and the control's failure to learn is beside the
> point. Measured at `ceiling-measurement-findings.md`.

**Not settled, and not touched here: where ownership lives.** L0 removes
an input channel. It shows the action depends on ownership; it does not
show the network built an internal structure carrying it. That is the
question the localization work was for, and yesterday's runs leave it
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
