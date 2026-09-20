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
