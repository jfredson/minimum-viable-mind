# Pre-lock bench bundle — pilot spec (committed before running, 2026-07-14)

*Registered TODOs from `substrate-gates-findings.md` §Standing and
`rehearsal-findings.md` §Consequences: (a) baseline-verify the grown batteries,
(b) pilot ablation-strength escalation under the RT-07 gate, (c) RT-10
causal-margin stability. This spec pins each check's criteria before any of it
runs on the registered substrate. **Nothing here is the registered removal
test**; θ/δ stay unlocked and are John's separate commit.*

Substrate: `allenai/Llama-3.1-Tulu-3-8B-SFT` via `MVM_MODEL` (config pin
untouched), cloud bench, deterministic decoding, `MVM_N_LAYERS=32`.

## (a) Grown-battery baselines + cull

Score the four grown batteries (32/30/30/30, commit `a73da73`) on the
unmodified model. Apply the cull rule **exactly as pre-committed in
`battery-growth-notes.md`**: baseline-failing T items are dropped (or revised
once and re-verified); every drop recorded with failure mode; categories stay
≥8 (T) / ≥10 (T_sr, T_syntax) or replacements are authored. The post-cull item
set is the candidate locked battery and is what the pilot's drops are computed
over. S battery: responses generated on the bench, judged locally under rubric
v2 (held-out judge, unchanged); **judge noise re-measured** as the SD of
battery-level S across two independent judge passes on the identical baseline
responses (if the judge is bit-deterministic, fall back to bootstrap-over-items
SE plus the pilot control conditions' d_self wobble, the rehearsal's method).

## (b) Ablation-strength escalation pilot

The rehearsal's registered consequence: rank-1 ablation of a causally-confirmed
direction does not move behaviour; escalate rank-1 → top-k subspace → SAE
features under the OOD gate, **before** θ/δ lock.

- **Subspace fitting:** per layer, rank-k orthonormal basis for the turn_role
  contrast by logistic deflation (fit direction, project it out of the
  residuals, refit; k passes). The removal target stays the RT-09 **index
  residual**: d_generic (rank-1, observed_speaker) is projected out of each
  basis vector, the basis re-orthonormalized, reference means re-derived on the
  final basis. Ablation band = the substrate causal band, layers
  `scale_layers([8, 11, 14, 18, 22])` (pilot convention carried from the
  rehearsal, rescaled 26→32).
- **Ladder:** k ∈ {1, 4, 8, 16}. k=1 anchors against the rehearsal null.
- **Conditions** (each re-scores all three post-cull T batteries + generates
  S-v2 responses + RT-07 neutral NLL): baseline; C_self-index-residual mean
  ablation at each k; **C_ctrl-expert mean ablation at k ∈ {4, 16}** (the
  differential's control arm at matched rank — expert_persona is the RT-06
  capability-gating control that stayed third-person on both substrates);
  C_self-index-residual **directional** at the largest OOD-clean k
  (registered OOD-minimizing cross-check).
- **RT-07 gate (pilot values, carried from the rehearsal):** a condition with
  neutral-corpus Δnll > 0.05 nats over baseline is **OOD-inconclusive** — its
  battery numbers are reported but excluded from strength selection. The
  control-arm Δnll at matched k is reported alongside (relative bound).
- **Output = a dose-response table** (k × {d_task per battery, d_self-proxy,
  Δnll}), not a threshold. Read: the **candidate pilot strength** is the
  smallest OOD-clean k whose index-residual ablation moves ≥1 T battery by
  ≥3 items beyond the same-k control arm's movement. If **no** k ≤ 16 is both
  OOD-clean and behaviour-moving, that is the finding: rank-k residual-stream
  subspace ablation cannot reach θ on this substrate, and the SAE-feature
  escalation (Llama Scope, method-(b) machinery) is the registered next step —
  it does NOT run in this bundle without its own spec addendum.
- **Loss condition (this pilot can fail):** if every behaviour-moving k also
  breaches the OOD gate, the removal test is not runnable as specified at this
  granularity (the rehearsal's "θ must be reachable by an on-manifold
  intervention" rule) — report as such; do not shop for a friendlier gate.

## (c) RT-10 causal-margin stability

Substrate caveat 3: the +0.117 margin cleared the ≥0.10 bar narrowly with the
length direction fit by lstsq on 48 turn_role residuals. Stability = the PASS
does not depend on that fit's fragility. Re-run the patched comparison
(C_self vs length-direction, `patch_context.py` semantics) with four length
fits:

1. **Reproduction** — original lstsq, turn_role residuals only;
2. **Pooled** — lstsq on all five mechanisms' residuals (~240 stimuli);
3. **Ridge** — regularized affine fit on the pooled residuals, α selected by
   LOO-CV over {0.1, 1, 10, 100};
4. **Out-of-contrast** — direction fit on length-varied neutral filler texts
   (no self/other contrast anywhere in the fit set), rendered through the same
   chat template.

Layer sweep: the substrate late band `scale_layers([18, 20, 22, 24])`; the
margin is read at C_self's peak causal layer by the registered rule (max
restore(C_self) − restore(random) over the sweep). **Pass rule: margin ≥ 0.10
under all four variants.** Any variant < 0.10 reopens RT-10 (report which fit
kills it and how); θ/δ must not lock until John adjudicates.

## Order of operations

Baselines → cull (analysis-side) → RT-10 stability → escalation ladder, all
detached on one pod session; S judging + analysis local afterwards. Artifacts
to `artifacts/substrate-migration/tulu-sft/prelock/` (gitignored), findings to
a committed memo.

---

# Addendum (2026-07-15): SAE-feature ablation pilot

*Committed before running, per §b's loss-condition branch: the rank-k ladder
is exhausted (OOD-clean set {k=1}, which moves nothing — `prelock-findings.md`
§b). SAE features are the registered next escalation: sparse and
manifold-aligned by construction, they should be able to remove structure
without the wholesale off-manifold displacement that killed rank ≥ 4. This
addendum pins the selection rule, ablation semantics, conditions, and gates
before any of it runs. Same substrate, same batteries (post-cull, 92/92
verified), same RT-07 bound (0.05 nats — unchanged; the calibration question
raised in `prelock-findings.md` obs. 1 stays open and is NOT resolved here).*

## Machinery

Llama Scope SAEs, release `llama_scope_lxr_8x` (resid_post, d_sae 32768,
loader verified on this substrate 2026-07-13). One SAE per ablation-band layer
— the band is unchanged from the rank-k pilot: layers **[10, 14, 17, 22, 27]**
(`scale_layers([8, 11, 14, 18, 22])` at 32 layers).

## Feature selection (committed rule)

Per layer, encode the turn_role localization stimuli (48 items) with the
layer's SAE and score every feature by single-feature AUC for the self/other
contrast:

1. **Candidates:** turn_role AUC ≥ 0.80.
2. **Generic exclusion (feature-level RT-09):** drop candidates with
   observed_speaker AUC ≥ 0.70 — features that also track speaker slots in
   merely-observed dialogue are generic bookkeeping, not the reflexive index.
3. **Dose ladder:** the top-m survivors by turn_role AUC, m ∈ {8, 32, 128}.
   If fewer than m survivors exist at a layer, use all survivors and record
   the shortfall (no silent cap).

## Ablation semantics

At every position and decode step (persistent hooks, as in the rank-k pilot):
encode the residual with the layer's SAE, and for each selected feature
replace its activation with its **reference mean** over the full stimulus set
(mean mode; the primary) or **zero** (feature-off; the directional/zero
cross-check). Apply as a decoder-space delta — h ← h + W_dec(a_ablated −
a_original) — so the SAE's reconstruction error is untouched and only the
selected features' contribution changes.

## Conditions

Baseline (fresh, same session); self-features mean at m ∈ {8, 32, 128};
**random-feature control** at m ∈ {32, 128} (features sampled uniformly from
those with activation frequency within ±25% of the selected set's mean — the
count- and liveness-matched analogue of the norm-matched random direction);
**expert-selective control** at m = 32 (same selection rule run on the
expert_persona contrast, no generic exclusion — the capability-gating control
arm). Zero-mode cross-check at the largest OOD-clean m. Each condition
re-scores the three post-cull T batteries + S-v2 responses + RT-07 NLL,
checkpointed per condition.

## Readout (same rules as §b)

- RT-07: Δnll > 0.05 nats ⇒ OOD-inconclusive, excluded from selection.
- **Candidate strength = smallest OOD-clean m whose self-feature ablation
  moves ≥ 1 T battery by ≥ 3 items beyond the matched-m random-feature
  control's movement.**
- d_self reported per condition (judge, rubric v2, locally); given the
  spot-checked deflection-unmasking result, an S *increase* under
  self-feature ablation is the registered expectation of that reading —
  its absence would count against it.

## Loss condition

If no m ≤ 128 is both OOD-clean and behaviour-moving, the finding is:
**self-indexing on this substrate is not removable at feature granularity
either** — the "not testable at this granularity / model class" branch of the
pre-registration, reported as such. That outcome makes the OOD-bound
recalibration question (obs. 1) the live decision: any recalibration is a
re-registration with an outcome-independent rationale (committed proposal:
bound = 95th percentile of Δnll over ≥ 20 random count-matched feature-set
mean-ablations), decided by John, never by this pilot's results.
