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
