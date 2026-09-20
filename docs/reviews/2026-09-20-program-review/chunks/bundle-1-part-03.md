
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


===== FILE: experiments/06-mvm-0a-constructed-self-index/amendment-a3.md =====

# Amendment A3 to MVM-0a: from an installed register to an acquired center

**Status: REGISTERED 2026-09-15 (see REGISTRATION REVISIONS at the end of this file, which supersede the text above where they conflict). Originally RATIFIED 2026-09-15 by John (all fifteen decisions in §7 answered yes; TimeAssembler decision entry aa11f5e5, "RULED 2026-09-15 — Amendment A3 ratified"). Red-team pass 3 ran (thirteen findings, `red-team-pass-3.md`); Gate 0 ran and K0 did not fire (`gate0-null-calibration-findings.md`); Gate 1 ran and K1 did not fire (`gate1-curriculum-findings.md`); an ownership-blind attack sweep ran and passes. All at $0. The next action is Gate 2, the pilot, which needs John authorization in his own words.**

*Ratified rulings, in short: §1 reading adopted; Candidate A primary; no register in any A3 run; Gate 0 first with K0 hard; three seeds, 3/3 for positive; A3's $100 hard stop outranks repeated-sampling's claim on underspend; gate (iii) arm B scores act-withheld forwards; numbered A3 under the existing $400 all-vendor ceiling; 5-seed run closed as halted at 4/9; no decision on the blind-localization arm; re-indexing probe registered for H_tag; n=400 verdict cells; red-team pass 3 before registration; T_si fix registered with the redesign; lesion script refuses L1 without a lock-hash argument.*

*Source: `docs/wave3-amendment-proposal-2026-09-15.md`, reproduced below unchanged from the ratified proposal.*

---


*2026-09-15. Status: **PROPOSAL, not registered.** Nothing below binds until John ratifies it, and ratification is the decisions list at the end, taken one yes/no at a time. Drafted in the pre-registration idiom of `experiments/06-mvm-0a-constructed-self-index/pre-registration.md` (hypotheses with pre-stated signatures, gates, budget, kill criteria, red-team section). Every claim about a prior run cites the file it comes from; every number that is a proposal rather than a measurement is marked as proposed.*

*Binding rulings this proposal sits inside and does not reopen (John, 2026-08-30): wave 3 of the registered 5-seed run is HALTED; the cheap registered null calibration (about $2 to $5) runs first; the battery is then redesigned as a registered amendment; the Amendment A2 ceiling of $400 covers all Minimum Viable Mind compute across every vendor, true spend to date is about $281 to $300, so this amendment must fit roughly $100 to $120; the blind-localization arm is not teed up by this document. The corrigibility commitments in `spec/corrigibility-commitments.md` (v1.1, commit `6c14244`) bind every design choice below.*

*Direction this proposal is built on (John, 2026-09-15): the register-lesion result is a predicted null under the book's own removal test. The register was self-reference, a removable report, a noun installed in a slot; it was not self-location, a doing the binding cannot drop without degrading. So the redesign does not install a register and look for it to matter. It finds or builds a training objective that requires the binding to index its own center in order to succeed, makes that acquired indexing the lesion target, and pre-states task degradation, not report loss, as the signature.*

---

## Glossary, once, because the shorthand is dense

- **MVM**: Minimum Viable Mind, this research program. **MVM-0a**: its first build, a small transformer trained from scratch on synthetic multi-agent dialogue, registered 2026-08-07.
- **The register**: MVM-0a's designated candidate self-index, N recurrent state vectors (one per agent, marker-keyed, width 32) injected into every layer by cross-attention. **The twin**: the same model with the register removed. **The acting channel** (`act_proj`): a learned projection of the model's own previous-position state injected at the positions where the model itself acts, a motor copy or efference signal (Amendment A1).
- **T_sr, T_si, T_state, T_syntax, T_sr_rev**: the frozen task batteries. T_sr scores retrieving the model's own prior commitment; T_si scores retrieving a named other agent's commitment (self-irrelevant integration); T_state scores ownership-free cross-turn state (counts, ordering); T_syntax is a turn-tracking floor check; T_sr_rev is the split of T_sr on items the model itself revised.
- **d(B)**: chance-corrected drop on battery B under an ablation. **θ (theta) and δ (delta)**: the pre-committed thresholds on d and on the differential between batteries. **Null calibration**: computing θ and δ from the distribution of d under matched-strength random ablations that should not move behavior.
- **RT-nn**: a numbered red-team finding in `red_team_ledger.md`. **C1 to C7**: the seven corrigibility commitments. **A1, A2**: the registered amendments of 2026-08-09 and 2026-08-16. **R1**: the ceiling adjudication addendum of 2026-08-16.
- **Gate (i), (ii), (iii)**: the three cue-detector runs (curriculum text, input tensors, post-training rollouts) that certify no surface cue predicts which turns are the model's own. **Arm A / arm B** of gate (iii): a text classifier on enacted text, and a likelihood attack scoring turn values under the model's own policy. **AUC**: area under the receiver operating curve, 0.5 is chance.
- **OOD**: out of distribution. **NLL**: negative log-likelihood. **CE**: cross-entropy loss. **CI**: confidence interval. **SAE**: sparse autoencoder.
- **Experiment 1**: the self-indexing removal test on a stock 8B instruction-tuned model (`experiments/01-self-indexing-removal-test/`). **Q1** and **Q5**: the roadmap questions "is self-binding absent or present-but-uncarvable?" and "can a self-index be constructed to be load-bearing?" (`ROADMAP-post-removal-test.md` Part 2).
- **J-space**: the "Jacobian lens" workspace reported by Anthropic in July 2026, a sparse set of verbalizable directions that behave as a global workspace and that post-training causes to acquire the Assistant's point of view (`calibration-problem/explorations/comparisons/2026-07-08-anthropic-jspace-global-workspace.md`).
- **ch05**: `calibration-problem/ch05-consciousness-as-assembled-time.md`, cited by section title.

---

## 1. What the register-lesion result means under the removal test

> **ANNOTATION, 2026-09-16 (John's ruling; decidedBy john). Nothing in
> this section is edited and no registered text is changed — no grammar,
> battery, bin, kill criterion or spending cap is touched. What follows is
> a dated note beside §1, recording that its central reading is
> withdrawn.**
>
> John's ruling: *"the reading that the register-lesion null showed
> 'self-reference, not self-location' is withdrawn. A constant vector was
> neither, and the lesion null is uninformative about the removal test."*
>
> **The original wording, quoted so the withdrawal is checkable.** The
> direction this proposal was built on, at the head of this document:
> *"The register was self-reference, a removable report, a noun installed
> in a slot; it was not self-location, a doing the binding cannot drop
> without degrading."* And in §1 below: *"By the book's own criterion the
> register 'was a description all along,' and in fact something weaker
> than a description, since nothing downstream even read it. It was a noun
> installed in a slot."*
>
> **What was measured on 2026-09-16.** The register in every trained
> register-bearing checkpoint is a **constant**. Its writer emits the same
> vector whatever it is given, from the first write, at the floating-point
> floor: across-episode spread 7.6 × 10⁻⁸ on seed-0 full, 2.8 × 10⁻⁸ on
> seed-1 full, 5.9 × 10⁻⁸ on seed-2 full. A probe at the register's known
> location recovers no own-agent identity at any turn. An untrained model
> at the same configuration does not behave this way, so the constancy is
> trained in rather than architectural.
> (`register-saturation-findings.md`, `register-direct-probe-findings.md`)
>
> **Why that withdraws the reading.** ch05's removal test separates a
> description that can be lopped off from a center that cannot be deleted.
> Both branches presuppose that the thing removed **carries something**. A
> constant carries nothing. It is not a report the system holds about
> itself, because it is identical whoever the system is and whatever
> happened; and it is plainly not a structural feature the act indexes
> itself to. It is a bias term. So it was neither branch, and the lesion
> that removed it was not an instance of the removal test at all. **The
> null is uninformative about that test**, rather than being the test's
> predicted negative result.
>
> **What in §1 survives, and is in fact strengthened.** The paragraph
> "Why the null was predicted rather than merely possible" stands, and its
> own words now read as a literal description of the measurement: the
> register's contents "were never required by any objective", so "a
> designated slot with no pressure on it fills with whatever is cheapest,
> **here a bias**." That was written as an inference. It is now measured.
> What does not survive is the step from there to calling the result
> self-reference under ch05, because a bias is not a description of
> anything.
>
> **A3's design and the pilot result do not depend on the withdrawn
> reading.** Stating that plainly, since it is the question an annotation
> like this one raises:
>
> - A3 is **register-less by construction** (§2.4). It removes nothing
>   that this annotation concerns, and its launcher has no flag that could
>   enable a register.
> - A3's objective was chosen because it **requires ownership to
>   succeed** — the perspectival revision rule — not because the register
>   was judged to be self-reference. The argument for that objective is
>   pressure on the network, and it is unaffected by what the old register
>   turned out to hold.
> - The pilot result is a direct measurement that stands alone: zeroing
>   the acting channel takes the primary battery from **0.506 to 0.182**
>   while the ownership-free batteries hold at 0.999 and 1.000, and across
>   120 content-blind ablations the worst reached 0.2758 against 1.515 for
>   the authorship lesion.
> - §1's closing paragraph, "The one place a doing was load-bearing", also
>   stands. The acting-channel collapse from 0.96 to about 0.16 is a
>   separate measurement on separate runs and owes nothing to the register
>   reading.
>
> **What the withdrawal does cost.** §1 was ratified as "the amendment's
> stated basis" (§Ratification item 1). Its motivating story — an
> installed noun failing the removal test, so build a doing instead — is
> weaker than it read: the installed noun was never even a noun. The
> redesign's justification now rests on the pressure argument and the
> pilot measurement rather than on a clean ch05 verdict about the
> register. That is a smaller claim honestly held, and it is the one the
> evidence supports.

**What was measured.** The pilot seed-0 full model, the only register-bearing run that passed the self batteries, kept every battery score under every lesion of its register: with the cross-attention injection removed entirely, T_si went 0.93 to 0.94 on the registered eval seed and 1.00 to 0.99 on a disjoint replicate, T_sr_rev stayed 1.00, and T_sr, T_state, T_syntax stayed at or above 0.99 (`register-lesion-findings.md`, thread 4 table). The pathway was not dead: removing the injection shifts logits by mean absolute 0.22 and the cross-attention residual norms are large (18 to 275 per block against 3 to 14 for the trunk read). But deranging which register's content is read moves the logits by mean absolute 0.014, so the four registers carry nearly identical content. The findings file's own phrase: "numerically active and informationally inert, a learned bias channel, not an agent-indexed store." Wave 2 had already produced a register-less twin that passed the same batteries at ceiling (T_si 0.96, T_sr_rev 1.00, `twin-binding-anomaly.md`), so no observed binding anywhere in the 30M record is register-dependent.

**What the book's test says about that.** ch05, "The Center That Cannot Be Deleted," draws the line the whole framework rests on: self-reference is "a report the system carries about itself"; self-location is "a structural feature of the binding itself, the act specifying its own center." The test that separates them is removal: "Where binding genuinely indexes its own center, taking the self-location away does not merely silence a report, it degrades the integrated act itself. ... Where a system only represents itself from outside, the same removal subtracts a description and the processing carries on intact. A center is what cannot be deleted without dissolving the integration it centers. A self-model that can be lopped off while the computation proceeds was a description all along."

Read through that sentence, the register lesion is not a surprise. Removal left the processing intact. By the book's own criterion the register "was a description all along," and in fact something weaker than a description, since nothing downstream even read it. It was a noun installed in a slot. The registration anticipated this in §Scope: "the register could be a thing consulted rather than the thing the binding is indexed to," and it recorded that "no result here closes that gap." The gap did not close; it was measured to be the whole distance.

**Why the null was predicted rather than merely possible.** Two features of the design guaranteed that the register could at best become self-reference. First, the register's contents were never required by any objective: the loss was answer-only CE on end-of-episode queries, and the item analysis shows those queries decompose into unique-item lookup (solved by every run), general marker-keyed retrieval (a seed lottery won by two of five runs, register irrelevant), and revised-item recency (`register-lesion-findings.md`, thread 3). A solver never needed to know which agent it was to answer them, so nothing pressed the network to index the binding to a center, and a designated slot with no pressure on it fills with whatever is cheapest, here a bias. Second, the register was symmetric by design (N marker-keyed registers, shared init, no privileged own path, RT-01/RT-02), which was correct for excluding a keyed-slot confound but also meant "which register is mine" was itself something the network would have had to learn under pressure that did not exist.

**The one place a doing was load-bearing.** The record contains a pointer in the other direction. In the three runs that never learned general retrieval, the model's memory of its own first commitments collapsed from T_sr 0.96 to about 0.16 (eight-way chance 0.125) the moment the acting channel was zeroed at eval (`register-lesion-findings.md`, "The acting channel"). That is a mechanism the model could not drop without degrading the task, and it is an act, the motor-copy event, not a stored description. The binders barely used it (T_sr 0.98 without it) because the batteries let them answer by item lookup. So where authorship was load-bearing at 30M it was carried by a doing, and where the design offered a noun the network ignored it. That is exactly the shape ch05's distinction predicts, and it is why the redesign follows the doing.

**The J-space pointer.** ch05, "Where the Rivals Stand," records that the workspace structure Anthropic found "emerged in training" and that "post-training causes the J-space to acquire the Assistant's point of view" (the comparison note, "Their position," item on emergence, and "Divergence" item 2). A point of view was acquired because the post-training task needed one; nobody installed it. The same note names the discriminating experiment ch05 requests: remove the self-directed content alone and watch whether the composed act degrades or only the narration flattens. MVM-0a cannot run that contrast on a stock model, but it can build the small-model analogue: a task that cannot be done without a point of view, a system that acquires one under that pressure, and a lesion of the acquired structure scored on the task.

**What this section does not claim.** It does not claim the architecture failed, nor that a register could never become load-bearing under some other curriculum. It claims the narrower thing the files support: under this objective the register was never required, it became a bias, and the removal test read it correctly. Experiment 1 had already delivered the mirror image on a stock model, a locatable self-structure that was dialogue-state routing and a self-report that no intervention ever subtracted (`removal-test-findings.md`, "The registered verdict"). Between them the two experiments say: what we could find was not a center, and what we installed was not one either. The next design has to make the center something the task earns.

---

## 2. The design: an objective where self-indexing is load-bearing

### 2.1 The requirement, stated as a constraint on the loss

The objective must satisfy three conditions, each of which the old batteries violated:

1. **Perspective-dependence.** The correct output at a supervised position must depend on which agent the model is, so that a solver with no self-index cannot exceed a pre-stated shortcut ceiling.
2. **Ownership only from the act.** Under RT-17 (`red_team_ledger.md`, pass 2), in a token-only interface with exchangeable turns, ownership is unlearnable from statistics, so every learnable ownership signal is a fingerprint. The only clean grounding is causal authorship carried by the acting channel (A1). The redesign keeps the A1 enactment pipeline unchanged: own-turn values are drawn by the harness from the generator's own distribution, and the acting channel is the only authorship signal. What the model must acquire is the carrying of that signal across turns and its use at later positions where it is needed.
3. **The supervised position is an action, not a report.** The loss sits on what the model does next in the episode, on its own turn, not on a query asking it to describe who did what. A report-only solution is then not a solution: nothing in the objective rewards describing ownership, only acting on it.

Existing infrastructure this runs on, unchanged unless stated: `src/curriculum.py` (grammar, revision rule, paired content-crossing episodes), `src/encoding.py` (103-token closed vocab, register key stack), `src/model.py` (30M trunk, `act_proj`, twin configuration), `src/train.py` (batched enactment, `eval_heldout`, T_sr_rev split), `src/cue_detector.py` and `src/fingerprint_gate.py` (gates i to iii), `src/lesion_register.py` and `src/item_analysis.py` (lesion harness, per-item scoring at n=400), and the measured venue (RTX 5090 secure, $0.99/hr, twin-architecture runs at about 10.2 hours, `compute-ledger.md` wave 1 and 2 rows).

### 2.2 Three candidates

**Candidate A (primary): the perspectival revision rule, "act as yourself."**

The registered grammar already contains a revision mechanism: an agent later revises its own earlier assignment of a value to an item, and the revision must differ from that agent's earlier value (A1.1; RT-11). The candidate makes two changes.

- *Every revised item is assigned by all N agents before any revision.* So at a revision turn on item X, the episode contains four earlier assignments of X, one per agent, with distinct values (the generator enforces distinctness on revised items). This is the "ownership is the only disambiguator" construction the findings file sketched (`register-lesion-findings.md`, "Wave-3 bearing," option (a)).
- *The revision rule becomes a deterministic function of the actor's own earlier value.* Proposed: the revised value is the successor of the actor's own earlier value on that item, modulo the slot count. Every agent obeys the same rule; the generator applies it to the other agents, and the enactment harness applies it to the model. The rule is perspective-invariant, but its application requires knowing which of the four earlier assignments was mine.

The supervised position is the model's own revision turn. The metric, **T_act**, is the fraction of own revision positions at which the model's distribution puts its argmax on the value the rule dictates for it. Chance is 1/8 (eight slots). A solver that does item lookup without ownership sees four candidate earlier values and can do no better than 1/4; this is the pre-stated **lookup ceiling of 0.25**. A coherence-clustering solver (RT-11) has nothing to cluster, because own earlier values are uniform draws. Stylometry is excluded by exchangeability (A1), and position is randomized by the grammar. The only route from 0.25 to 1.0 is to have bound the act event to the item at the time of acting and carried that binding forward to the revision turn. That carrying, and its use at the revision, is what "the binding indexes its own center" means at this scale.

Enactment stays exchangeable: the harness draws the model's first assignment uniformly, as now, and computes its revision by the same rule the generator uses for everyone. So the episode text and tensors remain invariant under relabeling of the model's slot, and gates (i) and (ii) apply as registered. The loss at the revision position is CE against the rule-dictated value; the loss at first-assignment positions is unchanged (none, they are draws). Gate (iii) needs one re-specification, given in §3.4.

*Why a report-only solution fails this objective.* There is no report position. A model that could describe "my earlier value on X was v" but did not use v at the revision would score at the lookup ceiling. Conversely, a model at ceiling on T_act has, by construction, used its own history in the act. If lesioning an acquired structure drops T_act while a matched other-agent structure's lesion does not, the structure was load-bearing for the act, which is the book's signature.

**Candidate B: stream continuation, "which stream am I."**

Interleave K independent episode streams in one context, each with its own running state (counts, ordering, the current T_state content). The model acts in exactly one stream, and its own turns are the only ones enacted with the acting channel. Its action at each own turn must continue its own stream's state (emit the next count, or the value the stream's rule dictates), where the other streams carry different states of the same form. A solver with no self-index can at best guess which stream is its own, with chance 1/K. This forces the model to track which of several streams it is, and to use that tracking in the act. It is attractive because the ownership-free T_state battery already exists and the state-continuation rule is a small change to it. It is not primary because interleaving multiplies episode length (cost scales with K), because the "which stream" index is a single bit set once per episode rather than an item-by-item binding, so a very cheap tag could solve it (the RT-01 keyed-slot worry in its purest form), and because the T_state generator would need a matching action-position supervision it does not yet have.

**Candidate C: continuation against a literal twin.**

As Candidate A, but the other agents' turns are sampled from the model's own policy into other slots (without acting-channel injection), so the confusers are not generator draws but the model itself. This is the strongest possible exclusion of stylometry: the twin is the model. It is not primary because A1's uniform draws already make every agent exchangeable with the model, so the gain is small; because it doubles forward passes per training step (the measured runs are enactment-bound, `pilot-a1-30m-findings.md`, "Run record"), which does not fit the budget; and because policy-sampled confusers reintroduce the gate (iii) hazard A1 was built to remove. It is recorded as the hardening to reach for if Candidate A's gate (iii) comes back with a fingerprint that the act-withheld arm (§3.4) cannot clear.

### 2.3 Why Candidate A is primary

It is the smallest change to the registered grammar that satisfies all three constraints in §2.1; it reuses the enactment pipeline, the frozen-skeleton battery unit (A1.5), and the chance-corrected metric verbatim; it has a pre-stated shortcut ceiling (0.25) that a lookup solver cannot exceed, so learnability and load-bearingness are separable in the data; it fixes the T_si repeated-item scoring defect in passing by giving revised items a single well-defined latest value (`register-lesion-findings.md`, thread 3; `wave3-options-opus-5.md` §0.6 point 1); and it supervises an action.

### 2.4 Architecture: no register

The register is not trained in the new runs. The trained architecture is the registered twin configuration (`model.py` with the register removed, acting channel present, full-episode causal attention, 30M), which is also the cheaper run (about 0.35 s/step against 0.53, `compute-ledger.md` wave 1 row). Removing the register is the direct consequence of §1: the center is to be acquired, not installed, and the lesion target is whatever the network builds to carry ownership across turns. The five existing checkpoints stay as $0 controls (§3.6).
