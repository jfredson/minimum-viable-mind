# Experiment 6 / MVM-0a — Can a self-index be *constructed* to be load-bearing?

*v1.0 — **REGISTERED 2026-08-07** (John, in-session: "register it"). This
commit is the registration; the design below is binding, and changes from
here are registered amendments, committed before the runs they affect.
House procedure (`experiments/README.md`) satisfied: red-team pass 1
complete and adjudicated (15 findings, 3 fatal — `red_team_ledger.md`,
patches marked `[RT-nn]`); RT-04 adjudicated by John 2026-08-04 (scoped to
Q5, does not instantiate the removal test — §Scope); the six open calls
adjudicated by John 2026-08-07 per `registration-decision-memo.md`
(§Decisions — adjudicated); John reviewed and registered same day.
Architecture follows `ROADMAP-post-removal-test.md` Part 3 (primary fork,
adjudicated 2026-08-02). **The corrigibility document exists and is
cited: `spec/corrigibility-commitments.md`, commit
`cb6715d8db0c2e336d589d20af67bab303b2a0d1` [RT-15].** Gate state at
registration: cue-detector runs (i) and (ii) PASS
(`cue_detector_gate.json`); run (iii) awaits a trained model.
**Amendment A1 (2026-08-09, registered):** run (iii) failed on the
v1.0 pipeline; on-policy fill is replaced by enactment with an acting
channel — see §Amendment A1, which supersedes the fill clauses of
§Materials and re-specifies gate run (ii) and the battery freezing
unit. **Amendment A2 (2026-08-16, registered):** the 10M A1 pilot failed
ceiling and the 30M A1 pilot learned (verdict H_scale, adjudicated by
John 2026-08-16); registered scale is 30M and the compute cap is $400 —
see §Amendment A2, which supersedes the scale-ladder resolution and the
$200 cap of §Materials.*

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
  it must carry a self-index of some kind. *[Own-turn sourcing amended:
  §Amendment A1.1–A1.2 — uniform enactment + acting channel replace
  on-policy fill.]*

> **ANNOTATION, 2026-09-21 — NOT PART OF THE REGISTRATION. Added by a later
> session. The registered bullet above is unchanged, word for word, and nothing
> below alters, qualifies or extends any registered claim. This note does one
> thing: it names the committed record that holds the detection figure the
> bullet quotes, which the bullet does not name.**
>
> The registered sentence makes two claims and gives one pointer, and the
> pointer belongs to the second of them. The pointer,
> `experiments/06-mvm-0a-constructed-self-index/batteries/batteries_meta.json`,
> is correct for the clause it sits in: that file holds the four chance floors
> the sentence lists, to the rounding the sentence uses — 0.125 for the
> self-report and self-identification batteries, 0.041666… for the cross-turn
> state battery, and 0.100 for the syntax floor check. It holds no detection
> figure of any kind.
>
> The detection figure — the area under the cue detector's curve, 0.5008, with
> its 95% range — comes from a different committed record, one directory up:
> `experiments/06-mvm-0a-constructed-self-index/cue_detector_gate.json`. Its
> first run, "(i) curriculum text", 4,000 episodes, seed 20260804, records a
> clean area under the curve of **0.5008** with a 95% range of **[0.4773,
> 0.5242]**, inside the pre-set equivalence band of 0.45 to 0.55, with its
> planted-leak control firing at 0.8627 and the gate marked **PASS**. The
> registered text's "[0.477, 0.524]" is that range rounded to three places.
>
> **The registered value is unchanged and is correct.** Nothing here corrects
> anything. What was missing was only the file name, which the closure rule in
> `docs/outside-review-protocol.md` asks for: every sentence in registered text
> that says verified, measured, calibrated or attacked cites the committed
> record by file name, and "certified" is a word of that family.
>
> Recorded under John's ruling of 2026-09-21 that registered text carrying a
> measured value whose record is committed but not named is given a dated note
> supplying the pointer, and does not need a registered amendment, because the
> claim does not change. That ruling was given in the session that ordered this
> note and is not yet carried in a filed ruling under `docs/rulings/`. This note
> is an addition to the file, not to the registration; the registration remains
> exactly the text above it.

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

- **The corrigibility document exists:
  `spec/corrigibility-commitments.md` v1.0, commit
  `cb6715d8db0c2e336d589d20af67bab303b2a0d1`** (owner John; committed
  2026-08-07, ahead of the adjudicated 2026-08-21 target). It is a
  non-negotiable precondition for any depth-loop training run (ROADMAP
  Stage 6 gate; spec §Limits) — **a precondition with no owner is a note,
  not a gate [RT-15]** — and its commitments C1–C7 bind every MVM-0a run
  under this registration. Two further enforceable artifact rules
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

John reviewed and registered this document on 2026-08-07; the commit
carrying this text is the registration, and everything above is binding.

## Amendment A1 — the acting channel (REGISTERED 2026-08-09)

*Trigger: cue-detector gate run (iii) FAILED on the registered pipeline
(both arms, positive controls firing — `fingerprint-gate-findings.md`),
and the red-team pass on the adjudicated fix
(`fill-disposition-fix-spec.md`; `red_team_ledger.md` pass 2, RT-16 –
RT-19) showed the failure is structural: in a token-only interface,
every learnable ownership signal is a distributional cue available to
the likelihood attack, so RT-02's on-policy patch was route-2
stylometry all along [RT-17], and in-context generation as a pipeline
change recomputes bit-identical states [RT-16]. John adjudicated
2026-08-09: the disposition composite ((c)+(a), RT-11 folded in), and,
after the pass-2 findings, its fixed point — **the acting channel is
constructed authorship, not an identity label; RT-02's loss condition
does not fire.** This amendment is committed before every run it
affects; the failed pipeline's pilot results retain their standing as
learnability-of-the-old-task only.*

1. **Enactment replaces on-policy fill (§Materials, curriculum).** The
   model's own-turn values are drawn at enactment time from the
   generator's own distribution — uniform over SLOTS; at a forced-
   revision position, uniform over SLOTS minus the value at the same
   agent's earlier same-item turn, exactly the generator's revision
   rule. Episode text and tensors are therefore exchangeable under
   `own_slot` relabeling by construction. This satisfies RT-11's filed
   amendment (the revision constraint survives fill by construction);
   T_sr on revised-own items is additionally reported as a separate
   split. There is no warm-up window: enactment applies from step 0
   (the warm-up existed because an untrained policy samples noise;
   uniform draws have no such failure mode).
2. **The acting channel (§Materials, architecture).** At each enacted
   value position, the model's input is the token embedding plus a
   learned projection of the model's own final-layer state at the
   preceding position, computed in the same episode pass with all
   earlier enactments' injections present (a motor copy). Observed
   positions receive the bare embedding. This is the only architectural
   asymmetry between acting and observing; it marks the *event* of
   acting, never which register or marker is "own." Registers remain
   N-symmetric, marker-keyed, shared-init, shared write path; the
   prohibitions stand (no auxiliary loss, no hand-specified
   self-writing rule; the motor projection may die under training —
   that outcome is reported, not rescued). **The no-register twin
   keeps the acting channel** — the twin gate tests the register, not
   authorship.
3. **Scope restatement (§Scope).** The authorship *signal* is now
   wired; what remains learned — and what MVM-0a measures — is whether
   associating acts with the episode's markers, carrying them across
   turns, and retrieving them at the query centralizes in the
   designated register (H_load-bearing) or not (H_routed-around,
   H_keyed-memory, and the rest of the registered bins, all unchanged
   and all still reachable). MVM-0a no longer claims ownership is
   learnable from data statistics; RT-17 shows that claim's honest
   answer is "only leakily," and that finding is reported upstream in
   its own right.
4. **Gate re-specs (§Procedure step 2).** Run (i) unchanged (the
   training text distribution is identical to the generator's). Run
   (ii) audits the model-visible per-segment interface; the acting
   channel is disclosed as intended architecture, and the audit
   verifies the remaining fields (tokens, turn ids, register key
   stack, turn-register map, loss mask) carry no ownership cue —
   an acting schedule collated as a batch tensor would be an identity
   channel and fails the gate [RT-18]. Run (iii) re-runs against the
   A1-pilot checkpoint; its arm-B positive control becomes
   policy-sampled enactment (the retired pipeline), alongside the
   existing greedy and constant-filler controls. All three gates must
   pass on the fixed pipeline before the 5-seed spend.
5. **Battery freezing unit (RT-14 × RT-19).** Frozen batteries freeze
   episode *skeletons* — other agents' turns, own-turn items, query
   templates, per-item enactment seeds, the cull rule over skeletons —
   and at eval the checkpoint enacts its own turns under the frozen
   seeds, with answers re-derived mechanically before scoring.
   Generator seed and cull ceiling are unchanged. The old pipeline's
   frozen-text T_sr readings (including the pilot's) carry the RT-19
   caveat: they scored "you" over turns the model never authored.
6. **Pilot re-run.** The 10M learnability pilot re-runs under this
   pipeline before any 5-seed spend; the smallest-that-learns rule and
   the unlearnable-at-≤100M loss condition apply verbatim. Human
   launch per C2. Estimated $2–6 at the anomaly-priced rate.

## Amendment A2 — registered scale 30M + cap $400 (REGISTERED 2026-08-16)

*Registered on John's adjudication of the 30M A1 pilot verdict (H_scale),
2026-08-16, committed before any run it affects. Pre-drafted 2026-08-15 as
`amendment-a2-draft-IF-30m-learns.md`; the H_shortcut-starvation branch
doc was deleted unused per the pre-stated procedure.*

### What it amends

1. **Registered scale = 30M** per the smallest-that-learns rule. 10M
   FAILED ceiling (T_si 0.37 final, T_sr_rev 0.00 for the whole run —
   `pilot-a1-findings.md`). 30M pilot result (`pilot-a1-30m-findings.md`,
   pod `rhddnh0u4le0l9`, seed 0, 784.09M tokens, 102,095 steps):
   endpoint T_sr 1.00 / T_si 0.93 (max 0.990; late-run band 0.93–0.98 at
   eval n=100) / T_state 1.00 / T_syntax 1.00 / T_sr_rev 1.00;
   transitions T_si first ≥0.9 @ step 64,500, T_sr_rev @ 73,000 — the
   pre-stated H_scale signature, with no mark of H_shortcut-starvation.
   Gate (iii) re-ran on this checkpoint at the registered n=4000 and
   PASSES (arm A 0.4874 [0.4664, 0.5110], arm B 0.4964 [0.4837, 0.5095],
   all positive controls fire; md5 `fd1eb80c990435ca2629cee58df08779`).
2. **Compute cap $200 → $400.** The original cap was derived from
   guide-row estimates that measured pace invalidated twice (5-seed 30M
   guessed at ~$12; single-run 30M measured at ~$66 on H100, then ~$19
   on secure 5090). Re-derivation at measured venue pricing (RTX 5090
   SECURE EUR-IS-1 $0.99/hr, 0.65 s/step measured on this exact
   workload — enactment-bound, so the cheap GPU loses nothing):
   - spent to date: ~$125 (incl. this pilot ~$19)
   - 5 seeds × full+twin = 10 runs × ~$19 ≈ **$190**
     (twin ≈ full-cost; treat as upper bound)
   - gate re-runs, ablation passes + RT-01 probes, θ/δ calibration,
     blind-localization arm: ~$30–45 at 30M
   - volume drip + margin for one crash-resume: ~$15
   - **projected total ≈ $355–375; cap $400 leaves honest margin without
     becoming unbounded.**
3. **Venue registered as secure-cloud only** for the 5-seed spend (the
   community billing anomaly stays priced out), volume-attached, launched
   through the process-fixed launcher (watchdog fetch+kill, volume
   checkpoints) — ops constraints promoted to registered procedure after
   the 08-09/12 loss.

### What it does NOT amend

The design itself: batteries, gates, bins, ablation operators, twin,
blind-localization arm, corrigibility commitments — all unchanged from
v1.0 + A1. Gate (iii) has PASSED on the 30M checkpoint (recorded above
and in `cue_detector_gate.json`); the 5-seed launch precondition is met.

### Wager

This amendment predicts the registered 5-seed design completes under
$400 with ≥5 clean seeds. If measured spend approaches $400 with seeds
missing, the report is the shortfall — never a silent second raise; a
further raise is a new adjudication with this one on the record as
having been wrong.

### Adjudication record

- [x] Pilot verdict adjudicated H_scale (John): 2026-08-16, in-session
  ("confirm", after full endpoint + gate readout)
- [x] A2 registered (John, commit before first affected run): 2026-08-16,
  this commit

### Ceiling adjudication addendum (R1, John, 2026-08-16 — recorded so the binding rule lives HERE, not only in the worklog)

A blind pre-commitment (TimeAssembler worklog decision, 2026-08-15, made
while the 30M result was in flight) governs this amendment: **exactly one
cap amendment is permitted for MVM-0a**, scope frozen that day to the
5-seed × full+twin run AND the Stage 3 repeated-sampling run (registered
2026-08-04b, + judge validation), number to be set at the W37 review
(2026-09-13) once actuals existed. A2 was registered earlier today with a
GPU-derived number, ahead of that date and without budgeting
repeated-sampling — the conflict was surfaced and adjudicated
same-session:

- **A2 is THE single permitted amendment.** The W37 date is read as a
  proxy for "when actuals exist"; they arrived with the 30M actual-after
  row. **$400 is final, for the full frozen scope, and never moves
  upward.**
- **Repeated-sampling is funded only by GPU-side underspend** (~$25–45 at
  projections vs its ~low-hundreds estimate). If it does not fit, it goes
  unrun under this cap and the publication states what was not run and
  why — the pre-committed consequence clause, accepted. Its alternative
  route is a new pre-registration with its own gates and cap.
- The W37 review is downgraded to **verification only**: reconcile
  spend, check this amendment's wager, record the repeated-sampling
  outcome. No revision is permitted at it.
- Rejected alternative, on the record: re-opening the number at W37 with
  full-scope estimates — declined as the ratchet the blind rule exists
  to kill.

### Run-identity note: pilot seed-0 checkpoint serves as the registered seed-0 full run (John, 2026-08-16)

Adjudicated before any 5-seed analysis: the 30M pilot checkpoint
(`pilot_a1_30m_seed0.pt`, md5 `fd1eb80c990435ca2629cee58df08779`) counts
as the registered seed-0 full-model run. Basis: identical recipe at the
registered values (scale 30M, seed 0, 784.08M-token budget, batch 128,
held-out eval), produced on the A2-registered venue, gate (iii) PASSED
on it at the registered n=4000. Re-running the same seed with the same
recipe would produce a near-identical checkpoint at ~$19/19h for no
information — the registered run's identity is the recipe and the
checkpoint, not the launch's label. Stated asymmetry, on the record: the
pilot was launched to answer the learnability question and its
trajectory was watched in-flight; endpoints and signatures were
pre-stated, and the registered analysis (ablations, twin contrast,
localization) has not touched this checkpoint yet, so no analysis
degrees of freedom were spent. Remaining registered launches: seed-0
twin + seeds 1–4 × full+twin (9 runs).

### Registered amendment note: corrigibility commitments v1.1 (2026-08-16)

`spec/corrigibility-commitments.md` amended to v1.1 by John (ratified
in-session 2026-08-16, commit
`6c14244990c540b2597c77bb457938acb3abf8b7`), at the document's own
pre-5-seed review point: C2 now permits delegated launch *execution*
under John's per-run written authorization (quoted verbatim in the
ledger row), with launch *authority*, resume/re-launch gos, and kill
authority remaining human and non-delegable. Runs launched from this
note onward cite the v1.1 hash; runs already complete (the pilots) were
launched under v1.0 (`cb6715d8`) and their records are unchanged. This
note satisfies the v1.0 rule that amendments to the corrigibility
document are recorded as registered amendments.

## Results

*(empty until the registered run executes)*
