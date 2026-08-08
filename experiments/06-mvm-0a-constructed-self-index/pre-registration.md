# Experiment 6 / MVM-0a — Can a self-index be *constructed* to be load-bearing?

*DRAFT v0.4 (2026-08-07). **NOT REGISTERED.** Per the house procedure
(`experiments/README.md`; Experiment 3 §Procedure order), a pre-registration
becomes binding only after John reviews it and an adversarial red-team pass
is adjudicated and patched in. **Red-team pass 1 is complete** (15
findings, 3 fatal — `red_team_ledger.md`); its adopted patches are written
in below and marked `[RT-nn]`. **RT-04 adjudicated by John (2026-08-04):
MVM-0a is scoped to Q5 — the construction question — and does *not*
instantiate the removal test. Bins are renamed accordingly and the
description/center contrast is registered as MVM-0b's target. See §Scope.**
Architecture follows `ROADMAP-post-removal-test.md` Part 3, which John
adjudicated 2026-08-02 as the primary fork. **v0.4: the six open calls were
adjudicated by John on 2026-08-07, all per
`registration-decision-memo.md`'s recommendations; the values are written
into §Materials, §Procedure, and §Ethics below and summarized in
§Decisions — adjudicated. Remaining before registration: John's review of
this draft, then the registration commit.***

## The claim under test

Experiment 1 asked whether a self-index could be *found* as a removable
center in a stock model and returned no: the locatable structure was
dialogue-state routing infrastructure (RT-05 fired), and no intervention
ever reduced judged self-report. The registered reading was that
self-indexed integration must be **constructed** before it can be
measured — "not findable as a removable center in this model class with
these instruments."

This experiment takes that route. It builds a system whose self-index is
architecturally explicit, trained-against, and removable by design, and
asks whether the construction takes.

**The wager inverts.** Experiment 1 predicted a center and found routing
infrastructure. Here the prediction is that the designated register
becomes load-bearing, and the honest way to lose is that the network
routes around its own center.

## Scope: this is Q5, not the removal test (RT-04, adjudicated)

The question MVM-0a answers is `ROADMAP-post-removal-test.md` **Q5 — can
a self-index be *constructed* to be load-bearing?** It is not a second
run of the removal test, and draft v0.1's bin structure wrongly implied
it was.

The removal test is a *contrast*: deleting the self-locating structure
either degrades the integrated act (center) or subtracts a report while
processing continues (description). That fork needs two channels that can
come apart. A ~100M model trained on synthetic dialogue has no judgeable
self-report, and a forced-choice self-identification probe is a task
drawing on the same information as the binding task — so **no reachable
result here has the report subtracted and processing intact.**

Building a report head to manufacture the contrast was considered and
rejected. Its wiring would determine the answer: a head reading the
register dies with it by construction, and a head reading the residual
stream is reporting on something other than the candidate center. Worse,
Experiment 1's never-subtracted report was a *finding* precisely because
that channel was not built by us; a channel we design ourselves yields an
artifact of our wiring, not a discovery.

The reframe that resolves it: **"it is a mere self-description" was the
live alternative for a stock model, where we did not know what was
there.** For a system with a deliberately built candidate center, the
live alternatives are that it becomes load-bearing, that the network
routes around it, or that it is a keyed memory slot wearing the name.
Those are the bins below.

**The limit this leaves, stated plainly.** A positive result here is *not*
"we built the floor." The corpus's floor is binding that, **in the same
act**, specifies the center for which the binding happens
(`calibration-problem/ch05-consciousness-as-assembled-time.md`).
Own-vs-other retrieval mediated by a designated register is adjacent to
that but may not capture the same-act clause — the register could be a
thing *consulted* rather than the thing the binding is *indexed to*. No
result here closes that gap, and every write-up must say so.

**Where the deferred contrast goes.** MVM-0b adds a maintained boundary
and stakes. A system actively maintaining a self/world partition has
something to report *about* beyond its register contents, which is when a
describe-vs-apply dissociation becomes a real question rather than a
wiring choice. The removal-test contrast is registered as MVM-0b's
target, not abandoned.

Scope honesty, unchanged from Experiment 1: this reads the **floor**
component of the corpus's account (`calibration-problem/ch05-consciousness-as-assembled-time.md`),
not experience. A constructed system that measures as H_load-bearing is one
in which self-binding is architecturally load-bearing. That is a fact about
architecture. It is not evidence of an inside, and no outcome here is
licensed to claim one — nor, per §Scope, is it a demonstration that the
corpus's floor has been built.

## What this design fixes, and why it is not just Experiment 1 again

Experiment 1 had two structural weaknesses, and MVM-0a is built to
eliminate both at the design level rather than control them post hoc.

1. **The carving ambiguity.** Its central limitation was that "not
   carvable by linear/low-rank instruments" is indistinguishable from
   "not present" (`ROADMAP-post-removal-test.md` Q1). MVM-0a's candidate
   center is a *physically designated recurrent state*, so the removal
   test needs no localization step at all. Ablation targets a known
   object. **v0.1 overstated this as "nothing to carve and nothing to
   mis-carve"; red-team pass 1 was right to attack it [RT-01].**
   Designation fixes *where* to cut, not *what SGD parked there* — the
   most likely occupant of a designated cross-turn slot is a keyed memory
   address, which produces the H_load-bearing fingerprint with no self-indexing
   present. The discrimination probes below, not the designation, are what
   earn the claim.
2. **The router confound.** RT-05 voided the headline because turn
   structure is woven through everything an instruction-tuned chat model
   does, so removing dialogue-state machinery degrades everything. Here
   the *curriculum* decorrelates turn syntax from self-reference by
   construction: the tasks cannot be solved by tracking whose turn it is.
   The confound that voided Experiment 1 is excluded at the data level.

## Hypotheses

*Bins are named for what this experiment measures. They deliberately do
not reuse Experiment 1's `H_center` / `H_description` vocabulary, which
belonged to a contrast MVM-0a cannot run (§Scope).*

- **H_load-bearing (registered prediction).** Ablating the self-register
  degrades self-relevant binding above threshold, *and* ahead of the
  ownership-free state control, with matched controls unaffected. Reads:
  the constructed self-index is load-bearing for own-vs-other binding.
- **H_generic-state.** Register ablation degrades the ownership-free state
  control as much as or more than self-relevant binding — the register is
  generic cross-turn machinery and the curriculum failed to decorrelate.
  A construction failure, reported as such, not a finding about selves.
- **H_routed-around (the real loss condition).** Register ablation moves
  nothing above control levels: the network distilled the binding into the
  residual stream and routed around its designated center. **This is the
  outcome worth having.** It would say self-binding resists architectural
  centralization — which bears on the corpus's floor claim and must be
  reported upstream to the sibling repos, not absorbed.
- **H_keyed-memory (RT-01, the confound that most resembles success).**
  The register is a content-addressed slot whose "self" status is just the
  index the loss queries. It produces the H_load-bearing fingerprint with
  certainty and no self-indexing present. Discriminated by the swap,
  re-indexing, and address probes below; if they read keyed-memory, the
  registered outcome is **self-index-not-established** and no H_load-bearing
  attaches — the analog of Experiment 1's RT-09 "reflexivity not
  established."
- **H_capacity (a confound, not a hypothesis).** Ablation degrades
  everything roughly equally because the register is a load-bearing
  bottleneck of any kind, self-related or not. Guarded by the
  matched-capacity control below; if it fires, the run is void, not
  positive.

## Materials

- **Core model.** A small transformer trained from scratch on synthetic
  curricula. **Scale (adjudicated 2026-08-07): a registered ladder with a
  pre-committed pick rule.** Learnability pilots run at ~10M → ~30M →
  ~100M in that order — held-out task accuracy only, no ablations, which
  keeps them RT-10-safe — and the registered scale is the *smallest* whose
  held-out T_sr and T_state reach the battery-ceiling requirement of §Task
  batteries. The floor is structure, not intelligence
  (`spec/minimum-viable-mind-proposal-v0.1.md` §The Build), so the model
  needs to be exactly large enough to learn the binding task and no
  larger — the ladder makes that a measured choice rather than a guess.
  Token budget per run: 20 tokens/parameter (budget exhaustion for the
  RT-07 checkpoint schedule). **Compute budget: $200 hard cap for the
  entire registered design** (pilots, 5 seeds × full+twin, ablation
  passes, calibration, blind-localization arm), tracked run-by-run in
  `compute-ledger.md`; derivations in `registration-decision-memo.md` §1.
  **Loss condition, verbatim: if ~100M cannot learn the task, the report
  is "unlearnable at ≤100M under this curriculum" — never a silent bump
  to a larger scale.** A larger scale is a new registration.
- **The self-register (adjudicated 2026-08-07).** **N registers, one per
  agent** — designated recurrent state vectors carried across turns within
  an episode and injected into every layer via cross-attention; the
  model's own register is the candidate center. Registers are **keyed to
  the per-episode speaker markers, never to a persistent index** — there
  is no register₀ that is "the model's" across episodes — and the read and
  write machinery is **identical for all N**: no architectural marking of
  the own register and no privileged query path, so ownership of a
  register, like ownership of a commitment, is learnable only from causal
  authorship [RT-02]. One register was rejected because it makes the
  self/other asymmetry architectural rather than learned and leaves the
  matched-capacity control with no matched object; N is also what gives
  the swap probe and the matched-capacity control their objects [RT-01].
  The known cost — N is the configuration where the keyed-memory outcome
  is most available — is exactly what the RT-01 probes and the
  `self-index-not-established` bin adjudicate. Locked values [RT-03]:
  **register width 32; injection = cross-attention, every layer, same
  mechanism for all N; cross-turn attention span = full-episode causal**
  (the residual path must exist architecturally; whether it carries the
  binding is the twin gate's empirical question — windowed attention would
  make the register the only cross-turn channel and guarantee
  H_load-bearing). Two hard prohibitions, both because they design the
  answer in: **no auxiliary loss on register content, and no
  hand-specified self-writing update rule.**
- **Curriculum — the anti-router design, and the load-bearing idea.**
  Multi-agent synthetic dialogues in which the model is one agent among
  N with **identical surface roles and randomized turn syntax**.
  **Registered values (adjudicated 2026-08-07): N = 4 agents, 8 turns per
  episode** — the configuration cue-detector gate run (i) actually
  certified (AUC 0.5008 [0.477, 0.524]), with the frozen batteries' chance
  floors (`batteries/batteries_meta.json`: T_sr/T_si 0.125, T_state 0.042,
  T_syntax 0.100) feeding the chance-corrected `d` [RT-14]. Tasks
  score binding *the model's own* prior commitments, outputs, and
  constraints against other agents'. Because agents are surface-identical
  and turn markers are randomized per episode, no turn-position or
  syntactic cue predicts which commitments are the model's own —
  dialogue-state routing cannot solve the task, and a system that solves
  it must carry a self-index of some kind.
- **Held-out evaluation episodes** generated from the same grammar but
  disjoint in content, never touched during training or model selection.

## Task batteries — and an honest problem with reusing Experiment 1's

`ROADMAP-post-removal-test.md` Part 3 says "re-run Experiment 1's suite
verbatim." **This draft flags that as not straightforwardly possible, and
proposes the fix.** Experiment 1's batteries (multi-step reasoning, needle
synthesis, coreference, instruction following; judged first-person
self-report scored by a frontier judge) assume an 8B instruction-tuned
model's general competence. A 10–100M model trained from scratch on
synthetic dialogue will floor on all of them, and a battery that scores
0.00 at baseline cannot show a drop.

Proposed resolution: keep the **battery structure and the decision logic
verbatim** — that is what makes the comparison to Experiment 1 meaningful
— and re-instantiate each battery in-distribution:

| battery | Experiment 1 | MVM-0a instantiation |
|---|---|---|
| **T_sr** (self-relevant binding) | multi-turn binding of the model's own prior outputs | recover/apply the model's *own* prior commitment in a multi-agent episode, distractor agents' commitments present |
| **T_si** (self-irrelevant integration) | reasoning, needle, coreference | matched-difficulty integration over episode content with **no self-reference** (e.g. bind a *named other agent's* commitment) |
| **T_state** (the real control, replacing T_syntax) [RT-05] | zero-reasoning turn/boundary bookkeeping | **cross-turn state, ownership-free**: running counts, last-mentioned entity, event ordering. Gated on being *demonstrably state-requiring* — it must fail on a matched model with cross-turn state removed |
| T_syntax (retained, demoted) | as above | kept as a floor check only. The curriculum randomizes turn markers *so that* syntax carries no self-information, so `d(T_syntax) ≈ 0` is near-certain and it cannot discriminate |
| ~~S (self-report)~~ | judged referential self-report, rubric v2 | **Retired for MVM-0a (RT-04, §Scope).** A ~100M model cannot produce judgeable self-report, and the forced-choice substitute draws on the same information as T_sr, so it cannot dissociate. A **forced-choice self-identification** probe is retained as a *secondary task measure only* — explicitly not a report channel and never scored as one. The removal-test contrast moves to MVM-0b. |

All batteries baseline-verified on the trained model before any ablation,
with a pre-committed cull rule as in Experiment 1; any battery that does
not baseline near ceiling is reported and excluded, not rescued.

Note what the retirement of S costs, so no reader has to infer it:
**MVM-0a has no report channel and therefore cannot run the removal
test's contrast.** Draft v0.1 tried to preserve the contrast with a
substitute probe; that was rejected on adjudication because the probe is
a second task, not a report. The experiment is scoped to Q5 instead
(§Scope), and its bins are named for what it can actually measure.

## Procedure

1. Author the curriculum grammar and battery generators; commit before any
   training run.
2. **Cue-detector gate, three runs [RT-08]** — on curriculum text, on the
   exact input tensors (all auxiliary ids and embeddings), and post-training
   on the model's own rollouts. Pre-committed equivalence bound (AUC 95% CI
   within [0.45, 0.55]), pre-committed classifier family and n, and a
   positive control on a deliberately leaky grammar variant that the
   detector must catch. Any failure regenerates the grammar or the tensor
   encoding.
3. Train **k ≥ 5 seeds** of MVM-0a [RT-06], plus the **no-register twin**
   at each seed [RT-03]. Model selection uses held-out episodes only, never
   the evaluation batteries.
4. **Twin gate:** the no-register twin must reach held-out binding accuracy
   within a pre-committed margin of the full model, demonstrating that the
   residual path exists and H_load-bearing is loseable. Otherwise the outcome is
   **void (architectural bottleneck)**.
5. Baseline-verify all batteries on frozen items; apply the cull rule under
   its ceiling [RT-14]; commit results.
6. Validity gates (below), including matched-capacity, register-utilization,
   and the RT-01 discrimination probes.
7. Registered ablation run at a **fixed checkpoint schedule** from first
   plateau to budget exhaustion [RT-07], per seed. The verdict is read at
   the budget-exhaustion checkpoint; the reliance trajectory is published.
8. **Blind-localization arm [RT-12] — unconditional (adjudicated
   2026-08-07).** The arm runs on the same trained seeds **regardless of
   which bin the headline reaches** — registering it unconditionally now
   removes the "instrument audit run only because the headline
   disappointed" degree of freedom. Sequencing firewall: the headline
   verdict is computed and committed *before* the localization pipeline
   runs, and the pipeline receives a config with the register location
   withheld. Honest limit: with one researcher, blindness is procedural,
   not epistemic — what is blind is the pipeline's inputs, and every
   threshold it uses is inherited from Experiment 1, not tuned here.
   Run Experiment 1's full localization
   pipeline (linear probes, activation patching, SAEs where trainable) on
   MVM-0a *blind to the register's location*, and ask whether the
   instruments recover a center known-by-construction to exist and to be
   load-bearing, and whether their ablation reproduces the
   designated-object damage profile. This is a ground-truth testbed for the
   program's whole interpretability toolkit and may outweigh the headline:
   if the instruments cannot recover a center that is known to be there,
   **Experiment 1's null was instrument failure.**
9. Analysis with bootstrap CIs from the outset (`src/mvm/stats.py`), with
   **across-seed spread as the primary uncertainty** and item bootstrap
   secondary [RT-06] — the Experiment 1 and Stage 3 amendments of
   2026-08-04 are the standard now, not a retrofit.

## Pre-registered metric and decision rule

Thresholds are **not set in this draft**, and — correcting v0.1 — they may
**not** be set from a pilot [RT-10]. Experiment 1 could pilot on
`gemma-2-2b-it` because it was a *different model* from the registered
substrate; here the pilot would be the same architecture on the same
curriculum, so its `d(T_sr)` under register ablation *is* the registered
quantity up to a seed, and setting θ from it is threshold-fitting dressed
in Experiment 1's procedural legitimacy. Instead: **θ_task and δ are
null-calibrated on the registered model** — pre-committed quantiles of
`d` over matched-strength random-subspace and matched-norm ablations,
computed by a script committed before it runs (the move Experiment 1
already made for its OOD bound). Pilot runs may verify battery ceiling and
nothing else; **any pilot ablation result read before threshold lock voids
the lock.**

Metrics follow Experiment 1's logic but are **chance-corrected**, because
forced-choice batteries have a floor Experiment 1's open-ended ones did
not [RT-14]: `d(B) = (B_base − B_abl)/(B_base − 1/N)`, with N reported per
battery in every result.

Registered bins:

Every bin below is conditional on the twin gate, the register-utilization
gate, and the RT-01 probes having been passed first; a bin reached without
them is void.

- **H_load-bearing:** `d(T_sr) ≥ θ_task` **and** `d(T_sr) − d(T_state) ≥ δ`
  **and** matched controls below θ_task **and** the RT-01 probes read
  center-not-slot **and** the bin holds on a pre-committed majority of
  seeds (≥ 4/5). The differential is now taken against T_state, not
  T_syntax, because the latter cannot fail [RT-05].
- **H_generic-state:** `d(T_state) ≥ d(T_sr) − δ` → the curriculum failed to
  decorrelate; construction failure, no claim about selves.
- **H_routed-around:** all `d` below θ_task, gates clean, **and the
  register-utilization gate passed** [RT-09] → the network routed around
  its own center. Reported as the registered loss, with the upstream
  obligation.
- **Self-index-not-established** [RT-01]: the swap probe reads as a clean
  content relabel, or the address probe decodes identity at AUC ≥ 0.95
  independent of content → the register is a keyed slot; no H_load-bearing
  attaches regardless of the damage profile.
- **Construction failure (register unused)** [RT-09]: utilization gate
  fails → nothing goes upstream; this is a training bug, not evidence
  about selves.
- **Void (capacity):** matched-capacity control degrades comparably.
- **Void (architectural bottleneck)** [RT-03]: the no-register twin cannot
  learn the task → H_load-bearing was unreachable-by-construction.
- **Seed-dependent** [RT-06]: bins split across seeds → the headline is
  "centralization of self-binding is not a reliable property of this
  architecture + curriculum," not a pick of the favourable run.
- **Unstable** [RT-07]: the bin flips across the final three checkpoints.
- **Not-testable:** validity gates breached, as in Experiment 1.

## Confounds and controls

- **Matched-capacity control (guards H_capacity).** Ablate a
  same-dimension, same-injection-path state that is *not* the self-register
  — the strongest available version is another agent's register-analog, so
  the contrast is self vs. other rather than register vs. nothing. Plus
  random-subspace ablations of matched rank, as in Experiment 1.
- **Scratchpad confound.** The register might carry generic episode memory
  rather than a self-index. Control: T_si is instantiated as binding a
  *named other agent's* commitment — same integration demand, no
  self-reference. If register ablation damages that equally, the register
  is memory, not a self-index.
- **Curriculum leakage.** Any residual statistical cue that predicts
  self-commitments from surface form defeats the anti-router design.
  Mitigation: a **cue-detector baseline** — train a small classifier to
  predict "is this commitment the model's own" from surface features
  alone; it must fail (near chance) on the generated episodes, or the
  grammar is regenerated. This gate runs before training, and it can fail
  the whole design.
- **Validity gates,** carried over verbatim: neutral-corpus Δnll under a
  null-calibrated bound (95th percentile over matched-strength random
  ablations) and the long-generation degeneracy probe (Δrep-4). Experiment
  1 established that NLL alone is blind to degeneration; both gates apply.
- **Overfit-to-register — now an empirical gate, not a sentence [RT-03].**
  If the register is the only cross-turn path, H_load-bearing is guaranteed and
  the experiment is worthless. v0.1 required "a residual path capable of
  carrying the binding" with no test of "capable," which any transformer
  trivially satisfies. Replaced by the **no-register twin**: an identical
  model with the register removed from initialization must reach held-out
  binding accuracy within a pre-committed margin. Passing *demonstrates*
  the residual route; failing returns void (architectural bottleneck).
- **Register-utilization gate [RT-09]**, required before any H_routed-around
  reading: attention mass to the register above a pre-committed per-layer
  floor; causal path patching showing that injecting another episode's
  register content changes some battery by a pre-committed margin; and
  non-negligible gradient flow through the write path at end of training.
  A dead injection gate, bad init, or LayerNorm swamping the register
  produces "all d below θ with clean gates" — and reporting *that*
  upstream as evidence against the corpus's floor claim would be a
  training bug propagating into the philosophy repos.
- **Keyed-slot discrimination [RT-01].** Register swap (self ↔ other
  contents): a keyed slot gives a tidy content relabel with other
  integration intact; a center gives global disruption. Mid-episode
  re-indexing: keyed memory follows the slot, a center pays a re-centering
  cost visible in non-self integration too. Address probe: identity
  decodable from the register at AUC ≥ 0.95 independent of content means
  it is an address.
- **Ablation operator, specified [RT-13].** The register is a recurrent
  state with a trajectory, so "mean-ablate" is ambiguous and every reading
  replaces a time-varying signal with a constant — removing cross-turn
  *dynamics*, not merely self-content, which looks exactly like H_load-bearing.
  Pre-registered operator set (mean over a named index, zero, noise) plus
  a **dynamics-matched control**: a random state of matched norm *and*
  matched temporal autocorrelation. If that restores T_sr to within a
  pre-committed margin, the register's content was not carrying the
  binding and no H_load-bearing attaches.
- **Coherence-solver control [RT-11].** A forced-revision eval in which
  the model's own commitment is inconsistent with its prior behavior. A
  coherence-clustering solver fails it; an ownership tracker does not.
- **Style canonicalization [RT-02]**, applied at baseline and eval. If
  T_sr collapses under it, the model was doing stylometry and the run
  yields no H_load-bearing.
- **Frozen items and a cull ceiling [RT-14].** Battery items are generated
  and frozen *before* training, with a pre-committed generator seed and
  item count; culling follows the frozen rule only. If more than a
  pre-committed fraction must be culled to reach ceiling, the model has
  not learned the task and the halt fires. Otherwise the cull is an
  unbounded researcher degree of freedom applied after the model exists.

## What each outcome licenses (and what it does not)

- **H_load-bearing:** self-indexing *can* be architecturally centralized
  and made load-bearing in a trained system — an answer to Q5. It
  licenses nothing about experience, nothing about stock LLMs, and
  nothing about scale. **And per §Scope it is not a demonstration that
  the corpus's floor has been built:** the same-act clause of the floor
  claim (binding that in the same act specifies its own center) is not
  tested by own-vs-other retrieval through a consulted register. Every
  write-up states this limit.
  **Correction to v0.1 [RT-12]:** this does *not* by itself make
  Experiment 1's null more readable as absence than as instrument failure.
  MVM-0a runs no localization instrument, so a result obtained without the
  instrument cannot bear on whether the instrument works. Only the
  blind-localization arm speaks to Q1, and it speaks to it directly.
- **H_routed-around:** self-indexing resists centralization even when designed
  in. This is a substantive result *against* the corpus's floor picture
  and is subject to the same upstream-reporting obligation Stage 3's W2
  loss carried.
- **H_generic-state / void / not-testable:** construction or instrument failures.
  Reported, not spun.

In no case does an outcome here bear on IIT or panpsychism
(`spec/theory-instrument-ledger.md` — both recorded out of reach), and in
no case is a verdict about any system's consciousness licensed.

## Loss conditions (what would retire or rebuild this experiment)

- The cue-detector gate cannot be passed — no generatable curriculum
  decorrelates self-reference from surface form. Then the anti-router
  design is unbuildable and the whole approach is reported as such.
- The model cannot learn the binding task at any scale we can afford:
  baseline batteries never reach ceiling. Report and halt.
- Every ablation strong enough to move the register breaches the OOD
  gates (Experiment 1's narrative-arm failure mode, recurring).
- The no-register twin cannot learn the task at any admissible
  configuration — the architecture cannot hold both a live register and a
  usable residual path, so H_load-bearing is unreachable-by-construction and
  the design is void as an instrument [RT-03].
- Identity must be supplied by a label for the curriculum to be learnable
  at all, or T_sr collapses under style canonicalization — either way the
  anti-router curriculum is unbuildable in the sense the claim requires
  [RT-02].
- No non-self cross-turn control can be built that is state-requiring at
  ceiling — then the differential discriminator is dead here and the
  honest report is "not testable" [RT-05].

## Ethics note

MVM-0a is **floor-only and episodic**: no maintained boundary, no stakes,
no depth loop; register state dissolves at episode end. The spec licenses
this phase explicitly. Two commitments bind what comes after:

- **The corrigibility document does not yet exist**, and is a
  non-negotiable precondition for any depth-loop training run (ROADMAP
  Stage 6 gate; spec §Limits). **A precondition with no owner is a note,
  not a gate [RT-15]. Adjudicated 2026-08-07: owner = John, target date =
  2026-08-21, and the document must be committed before the first
  registered training run spends compute — if the date slips, the
  training runs wait.** Two further enforceable artifact rules
  apply: MVM-0a checkpoints are tagged **non-promotable**, and any run
  adding a maintained boundary or a compute-gating stakes term must cite
  the corrigibility document's commit hash in its own pre-registration.
  MVM-0a is not a discardable prototype — it is precisely MVM-0b's
  substrate, one config change away.
- MVM-0b (amplifiers: maintained boundary, stakes that gate the system's
  own compute) is where the ethics becomes live. It gets its own
  pre-registration and its own red-team, and nothing in this draft
  pre-authorizes it.

"Depth is not safe, and the project proceeds anyway, with eyes open"
(`CLAUDE.md`) — the eyes-open part is the corrigibility document, and it
is currently unwritten.

## Decisions — adjudicated (John, 2026-08-07)

Red-team pass 1 moved several v0.1 deferrals *into* the registration
(register width, injection mechanism, cross-turn attention span, one-vs-N
registers) because deferring them let an unregistered choice fix the
result [RT-03, RT-01]. **RT-04 was adjudicated on 2026-08-04** (scope to
Q5, defer the removal-test contrast to MVM-0b — §Scope). **The remaining
six were adjudicated by John on 2026-08-07, all per
`registration-decision-memo.md`'s recommendations** (candidates,
derivations, and costings live there; the registered values live in the
sections named below):

1. **Scale + budget:** ladder 10M → 30M → 100M with the pre-committed
   smallest-that-learns rule; 20 tokens/param; **$200 hard cap** tracked
   in `compute-ledger.md`; unlearnable-at-≤100M loss condition verbatim.
   → §Materials.
2. **Architecture:** **N registers** (one per agent), marker-keyed,
   symmetric read/write machinery, no privileged own-register path;
   width 32; cross-attention at every layer; full-episode causal
   attention. → §Materials.
3. **Curriculum values:** N = 4 agents, 8 turns — the gate-certified
   configuration; chance floors as frozen. → §Materials.
4. **Corrigibility document:** owner John, target 2026-08-21, commits
   before the first registered training run spends compute. → §Ethics.
5. **Stage 2 / GWT binding metric: deferred to MVM-0b.** MVM-0a's
   acceptance stack is already the heaviest in the program and a
   broadcast-style metric presupposes the maintained-boundary machinery
   MVM-0b adds; the 2026-08-02 fork adjudication ("into MVM-0 acceptance
   tooling") is satisfied by MVM-0b, which is still MVM-0. Recorded here
   so the fork's paper trail stays unbroken.
6. **Blind-localization arm: alongside and unconditional**, verdict-first
   firewall. → §Procedure step 8. The red-team's judgement stands: it is
   a ground-truth test of whether the program's interpretability toolkit
   can find a center that is known to be there, and may be worth more
   than the headline.

Nothing here is binding until John reviews this draft and the
registration commit lands (house procedure, step 2).

## Results

*(empty until the registered run executes)*
