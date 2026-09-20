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
