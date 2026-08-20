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
