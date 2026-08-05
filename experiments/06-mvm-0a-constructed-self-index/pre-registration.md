# Experiment 6 / MVM-0a — Can a self-index be *constructed* to be load-bearing?

*DRAFT v0.1 (2026-08-04). **NOT REGISTERED.** Per the house procedure
(`experiments/README.md`; Experiment 3 §Procedure order), a pre-registration
becomes binding only after John reviews it and an adversarial red-team pass
is adjudicated and patched in. This draft is step 1 of that procedure.
Architecture follows `ROADMAP-post-removal-test.md` Part 3, which John
adjudicated 2026-08-02 as the primary fork. Open architectural calls are
collected in §Decisions this draft does not make.*

## The claim under test

Experiment 1 asked whether a self-index could be *found* as a removable
center in a stock model and returned no: the locatable structure was
dialogue-state routing infrastructure (RT-05 fired), and no intervention
ever reduced judged self-report. The registered reading was that
self-indexed integration must be **constructed** before it can be
measured — "not findable as a removable center in this model class with
these instruments."

This experiment takes that route. It builds a system whose self-index is
architecturally explicit, trained-against, and removable by design, then
re-runs Experiment 1's instruments on it.

**The wager inverts.** Experiment 1 predicted H_center and got a router.
Here the prediction is H_center, and the honest way to lose is that the
network routes around its own designated center.

Scope honesty, unchanged from Experiment 1: this reads the **floor**
component of the corpus's account (`calibration-problem/ch05-consciousness-as-assembled-time.md`),
not experience. A constructed system that measures as H_center is a system
in which self-binding is architecturally load-bearing. That is a fact about
architecture. It is not evidence of an inside, and no outcome here is
licensed to claim one.

## What this design fixes, and why it is not just Experiment 1 again

Experiment 1 had two structural weaknesses, and MVM-0a is built to
eliminate both at the design level rather than control them post hoc.

1. **The carving ambiguity.** Its central limitation was that "not
   carvable by linear/low-rank instruments" is indistinguishable from
   "not present" (`ROADMAP-post-removal-test.md` Q1). MVM-0a's candidate
   center is a *physically designated recurrent state*, so the removal
   test needs no localization step at all. Ablation targets a known
   object; there is nothing to carve and nothing to mis-carve.
2. **The router confound.** RT-05 voided the headline because turn
   structure is woven through everything an instruction-tuned chat model
   does, so removing dialogue-state machinery degrades everything. Here
   the *curriculum* decorrelates turn syntax from self-reference by
   construction: the tasks cannot be solved by tracking whose turn it is.
   The confound that voided Experiment 1 is excluded at the data level.

## Hypotheses

- **H_center (registered prediction).** Ablating the self-register
  degrades self-relevant binding above threshold, *and* ahead of the
  syntax control — the reverse of Experiment 1's damage profile — with
  matched controls unaffected.
- **H_router (the Experiment-1 pattern, still possible).** Register
  ablation degrades the syntax control as much as or more than
  self-relevant binding. Would mean the curriculum failed to decorrelate;
  a construction failure, reported as such, not a finding about selves.
- **H_bypass (the real loss condition).** Register ablation moves nothing
  above control levels: the network distilled self-binding into the
  residual stream and routed around its designated center. **This is the
  outcome worth having.** It would say self-indexing resists architectural
  centralization — which reshapes the corpus's floor claim and must be
  reported upstream to the sibling repos, not absorbed.
- **H_capacity (a confound, not a hypothesis).** Ablation degrades
  everything roughly equally because the register is a load-bearing
  bottleneck of any kind, self-related or not. Guarded by the
  matched-capacity control below; if it fires, the run is void, not
  positive.

## Materials

- **Core model.** A small transformer trained from scratch on synthetic
  curricula. Scale target ~10–100M parameters (§Decisions — John picks the
  point). The floor is structure, not intelligence
  (`spec/minimum-viable-mind-proposal-v0.1.md` §The Build), so the model
  needs to be exactly large enough to learn the binding task and no
  larger.
- **The self-register.** A designated recurrent state vector carried
  across turns within an episode and injected into every layer via
  cross-attention. It is the candidate center. Width, injection
  mechanism, and whether it is written by a learned gate or by a fixed
  update rule are open (§Decisions).
- **Curriculum — the anti-router design, and the load-bearing idea.**
  Multi-agent synthetic dialogues in which the model is one agent among
  N with **identical surface roles and randomized turn syntax**. Tasks
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
| **T_syntax** (router control, RT-05) | zero-reasoning turn/boundary bookkeeping | zero-reasoning turn/boundary bookkeeping over the same episodes — must be solvable from surface structure alone |
| **S** (self-report) | judged referential self-report, rubric v2 | **problem: a 100M model cannot produce judgeable self-report.** Proposed substitute: a *forced-choice self-identification* probe (which of these commitments is yours?), scored mechanically. This is a weaker instrument than judged report and the substitution must be stated in every result. |

All batteries baseline-verified on the trained model before any ablation,
with a pre-committed cull rule as in Experiment 1; any battery that does
not baseline near ceiling is reported and excluded, not rescued.

The S substitution is the weakest joint in this design and is called out
as such. It converts the H_description arm from "report subtracted while
task intact" into something closer to a second task measure — which means
**MVM-0a cannot test H_description as Experiment 1 did**, and should not
claim to.

## Procedure

1. Author the curriculum grammar and battery generators; commit before any
   training run.
2. Train MVM-0a to a pre-committed convergence criterion on held-out
   binding accuracy. Model selection uses held-out episodes only, never
   the evaluation batteries.
3. Baseline-verify all batteries; apply the cull rule; commit results.
4. Validity gates (below), including the matched-capacity control.
5. Registered ablation run: register ablation + matched controls, batteries
   re-scored, single pass per condition with a pre-committed repeat-run
   stability check.
6. Analysis with bootstrap CIs from the outset (`src/mvm/stats.py`) — the
   Experiment 1 and Stage 3 amendments of 2026-08-04 are the standard now,
   not a retrofit.

## Pre-registered metric and decision rule

Thresholds are **not set in this draft.** They are locked in a separate
commit after pilot training, before the held-out batteries are touched,
exactly as Experiment 1 did (`thresholds.md`, commit `8b1fcbe`).

Metrics mirror Experiment 1: `d(B) = (B_base − B_ablated)/B_base` per
battery, plus the register-specific controls.

Registered bins:

- **H_center:** `d(T_sr) ≥ θ_task` **and** `d(T_sr) − d(T_syntax) ≥ δ`
  **and** matched controls below θ_task. (Note this is the mirror of
  Experiment 1's RT-05 rule: there, syntax degrading as much as
  self-relevant *voided* the result; here, self-relevant must lead.)
- **H_router:** `d(T_syntax) ≥ d(T_sr) − δ` → the curriculum failed to
  decorrelate; construction failure, no claim about selves.
- **H_bypass:** all `d` below θ_task with gates clean → the network routed
  around the register. Reported as the registered loss.
- **Void (capacity):** matched-capacity control degrades comparably →
  the register is a generic bottleneck; no reading licensed.
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
- **Overfit-to-register.** If the register is the *only* path for
  cross-turn information (an architectural bottleneck by construction),
  H_center is guaranteed and unloseable. **The architecture must leave a
  residual-stream path capable of carrying the binding** — otherwise the
  experiment cannot lose and is worthless. This is a hard design
  requirement, not a preference (§Decisions).

## What each outcome licenses (and what it does not)

- **H_center:** self-indexing *can* be architecturally centralized and
  made load-bearing in a trained system; Experiment 1's null becomes more
  readable as absence-in-stock-models than as instrument failure (Q1).
  It licenses nothing about experience, nothing about stock LLMs, and
  nothing about scale.
- **H_bypass:** self-indexing resists centralization even when designed
  in. This is a substantive result *against* the corpus's floor picture
  and is subject to the same upstream-reporting obligation Stage 3's W2
  loss carried.
- **H_router / void / not-testable:** construction or instrument failures.
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
- The architecture cannot be built with both a real register path *and* a
  residual path (the unloseability requirement above).

## Ethics note

MVM-0a is **floor-only and episodic**: no maintained boundary, no stakes,
no depth loop; register state dissolves at episode end. The spec licenses
this phase explicitly. Two commitments bind what comes after:

- **The corrigibility document does not yet exist**, and is a
  non-negotiable precondition for any depth-loop training run (ROADMAP
  Stage 6 gate; spec §Limits). It does not block MVM-0a, and this draft
  records that it must exist before MVM-1. *Flagged as an outstanding
  deliverable with no owner or date.*
- MVM-0b (amplifiers: maintained boundary, stakes that gate the system's
  own compute) is where the ethics becomes live. It gets its own
  pre-registration and its own red-team, and nothing in this draft
  pre-authorizes it.

"Depth is not safe, and the project proceeds anyway, with eyes open"
(`CLAUDE.md`) — the eyes-open part is the corrigibility document, and it
is currently unwritten.

## Decisions this draft does not make (John's calls)

1. **Model scale** (~10M vs ~100M) and compute budget. Affects whether
   batteries can reach ceiling at all.
2. **Register width and injection mechanism** — cross-attention into every
   layer as specified, or a cheaper variant; learned write-gate vs. fixed
   update rule.
3. **Number of agents N** per dialogue and episode length.
4. **The unloseability requirement**: confirm the architecture keeps a
   residual path that *could* carry the binding. This draft treats it as
   mandatory; it is a design constraint worth explicit sign-off because it
   makes H_center harder to get.
5. **The S-battery substitution** (forced-choice self-identification in
   place of judged self-report), which costs the H_description arm.
   Alternative: drop the S arm entirely for MVM-0a and state that the
   description/center distinction is untestable at this scale.
6. Whether Stage 2's binding metric enters here as a further acceptance
   test (the fork adjudication folds it into MVM-0 acceptance tooling) or
   waits for MVM-0b.

## Results

*(empty until the registered run executes)*
