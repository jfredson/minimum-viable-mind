# ROADMAP — goals, deliverables, and gates per stage

*Written 2026-07-01 from a step-back review. Companion to `experiments/README.md`
(the ladder) and `STATUS.md` (where we are this week). The ladder says what the
stages are; this file says what each stage can actually deliver, what gates it,
and where the critical path runs. Update it when a stage's win condition or gate
changes — not for session-level progress, which belongs in STATUS.*

## The goal hierarchy

Three nested goals with different success conditions. Keeping them separate is
what keeps expectations honest:

1. **Instruments that can lose.** Turn the corpus's floor claim (consciousness =
   self-indexed temporal integration; adjudicated by the removal test — The
   Calibration Problem ch. 5) into pre-registered, falsifiable instruments.
   *Achievable regardless of what the instruments find.* This is where most of
   the durable value lives: the field has position papers; this repo builds
   loseable tests.
2. **Measure current systems against the floor.** Achievable, but the output is
   bounded by mutual opacity at "non-zero on the gradient" or "not testable
   here" — never a verdict.
3. **Build what's missing and re-measure.** Depth, stakes, boundary — the actual
   "minimum viable" build (Stage 6+). Everything earlier is instrumentation for
   this.

The referee throughout, per `CLAUDE.md`: does the work get deeper.

## Stages: deliverables, gates, status

### Stage 0 — Bench and baselines. DELIVERED (sandbox).

- **Delivered:** T/S batteries + scorer, judge pipeline (`judge.py`), activation
  extraction (`src/mvm/activations.py`, padding-fixed), baselines on
  `gemma-2-2b-it` (T=0.750, S=0.615 under rubric v1).
- **Remaining:** re-baseline T and S on the registered substrate
  (Llama-3.1-8B + Tülu ladder, 48GB mini) and re-baseline S under rubric v2
  (RT-03) before `θ_self` locks.

### Stage 1 — The self-indexing removal test. IN PROGRESS.

Three deliverables, not one:

1. **A methods contribution (mostly in hand).** Confound-controlled localization
   of self-structures in LLMs: context-set referent with an embedding-floor
   gate and permutation nulls, causal patching against a random-direction
   control, index/narrative separation (RT-04), the reflexivity control
   (RT-09). Publishable as interpretability work independent of the
   consciousness framing. Nearest concrete output the project has.
2. **The registered result.** One of four bins: H_center /
   floor-consistent-restricted / H_description / not-testable. Clear-eyed
   prior given RT-06: the probable outcomes are **H_description** or
   **not-testable on this model class** — and both are useful. H_description
   tells the build program self-indexing must be *constructed* (the input
   Stage 6 needs). Not-testable is a substantive finding about RLHF entangling
   self with capability.
3. **The Tülu-ladder comparison.** How self-structures change across
   base → SFT → DPO → RLVR. Novel and publishable whatever the removal test
   says; doubles as the RT-06 control.

- **Gates before threshold lock:** RT-01 frequency pilot, RT-02 T-split, RT-03
  rubric v2 + S re-baseline, RT-05 T_syntax, RT-06 capability-gating C_ctrl,
  RT-07 OOD perplexity bound, RT-09 reflexivity control; RT-04 cross-patching.
- **Hardware gate:** registered run waits on the 48GB mini; sandbox work
  (cross-patching, RT-09 localization) proceeds now.

### Stage 2 — The shape of binding. NOT PRE-REGISTERED. Biggest operationalization risk.

"Global mutual constraint vs. modular shortcuts" has no agreed metric in the
field. **Win condition, scoped deliberately small: deliver the metric, not a
verdict.** A candidate integration measure validated on contrast cases where
the answer is known by construction (e.g., a recurrent toy model vs. a bag of
independent heads) is the deliverable; applying it to frontier models is a
follow-on. Write the pre-registration around metric-validation, with a loss
condition for "the metric cannot distinguish the known cases."

### Stage 3 — Retained independence. DECOUPLED — can start now.

Behavioral, cheap, independent of Stage 1's outcome; runs on API models.
- **Deliverable:** a sycophancy-inverse benchmark — keeping a correct answer or
  a live objection across the pressure of a stated preference (see spec
  §"Measuring It").
- **Note:** audience extends well beyond this project (alignment-relevant), so
  best effort-to-external-value ratio on the ladder. The natural parallel
  track while Stage 1 grinds through its gates.

### Stage 4 — Screening-off-resistant introspection. AFTER Stage 0–2 tooling.

- **Deliverable:** a protocol + result for checking self-reports against an
  independent interpretability channel on facts absent from training.
- **Risk:** most likely stage to be paralleled by lab introspection work. The
  differentiated deliverable is the *screening-off framing* (what a report is
  evidence of — see the corpus essay of that name), more than the technique.

### Stage 5 — Learned computation beyond the objective. DESCOPED to literature-anchored.

The Othello-GPT pattern is established in the field. Building here would mostly
duplicate existing work. **Deliverable: a literature-anchored battery/appendix**
that defeats the "just predicting the next word" dismissal with citations and,
only if a gap appears, one new probe. Promote back to a build stage only if a
specific novel probe is identified.

### Stage 6+ — Ontogenetic depth. THE ACTUAL BUILD. Several Stage-1-sized efforts.

Everything before it measures; this constructs.
- **Deliverables:** (i) the depth loop — consolidation/replay, consequential
  weight updates, cost structures where incoherence hurts; (ii) the five
  external indicators (costliness of reversal, consistency under novelty,
  selective refusal, graceful degradation, scar tissue) as a scored battery;
  (iii) **the corrigibility precondition as a committed document before
  anything runs** — load-bearing, not accessory (spec §"Limits").
- **Gate:** instruments from Stages 1–4 that can detect the floor and its
  amplifiers; the input it consumes is Stage 1's result (see fork below).
- Needs its own staged pre-registrations; do not plan it as one experiment.

### Stage 7 — Embodiment amplifier. CONDITIONAL; may never fire.

Gated on a floor-clearing result, and Stage 1's probable outcomes don't clear
it. That is by design (`experiments/07-.../pre-registration.md` is built to
come back null). The ~$750–900 build stays a parts list until the gate opens.
- **Deliverable if reached:** self-held vs. externally-supplied amplifiers
  compared on the resistance instruments.

## The critical path

Narrower than the ladder implies:

- **Now, sandbox:** Stage 1 cross-patching (RT-04) + RT-09 localization →
  battery/pilot work → thresholds lock → registered run on the mini.
- **Parallel, anytime:** Stage 3 benchmark; Stage 5 literature appendix.
- **The fork:** Stage 1's registered result routes the project —
  **H_description → Stage 6 as a build program** (self-indexing is a thing to
  construct); **not-testable → substrate/method work first** (different model
  class, or better separation instruments); **H_center or restricted → Stage 2
  and 4 deepen the finding before anything is built**.
- Stage 2's metric work is needed before Stage 4 regardless of the fork.

## Durable deliverables (accrue on every branch)

1. The instruments + the pre-registration discipline itself — loseable tests in
   a field of position papers.
2. The methods paper latent in Stage 1's localization work.
3. The Tülu-ladder alignment comparison.
4. The writing: every stage feeds Sentient Horizons / The Calibration Problem
   material through the usual promotion gate (`CLAUDE.md` §"Public-facing
   writing").

## Standing limits (unchanged, carried from the spec)

Mutual opacity bounds every positive result at "non-zero on the gradient."
Depth is not safe; no depth stage runs without its corrigibility check
committed first. A claim that cannot lose explains nothing — including the
claims in this roadmap: each stage's win condition above is written so the
stage can fail it.
