# Dress-rehearsal removal test — findings (2026-07-12, pilot sandbox)

*Full pre-registered pipeline exercised end to end on `gemma-2-2b-it`:
localize → ablate (mean primary + directional cross-check, band [8,11,14,18,22])
→ re-score T_si / T_sr / T_syntax / S-v2 → RT-07 OOD gate → decision rule with
clearly-labeled REHEARSAL-ONLY thresholds (θ_task 0.15, θ_self 0.30, δ 0.10).
NOT the registered run; no claim attaches to bin names. Artifacts in
`artifacts/stage1/rehearsal/`; instruments registered at `5d9e4cf` before
running.*

## Verdicts (rehearsal thresholds, non-binding)

| condition | d_task^si | d_task^sr | d_task^syn | d_self | Δnll | bin |
|---|---|---|---|---|---|---|
| C_self-index residual, mean | +0.000 | +0.000 | +0.000 | +0.034 | **+0.265** | **OOD-inconclusive (RT-07 fired)** |
| C_self-index residual, directional | +0.067 | +0.000 | +0.000 | −0.011 | +0.033 | (cross-check; null pattern) |
| C_self-narrative, mean | +0.067 | +0.000 | +0.000 | −0.045 | +0.038 | inconclusive (null) |
| C_ctrl-generic, mean | +0.067 | +0.000 | +0.000 | −0.022 | +0.012 | — |
| C_ctrl-expert, mean | +0.000 | +0.000 | +0.000 | −0.079 | +0.011 | — |

Baseline: T_si 0.750, T_sr 0.750, T_syntax 0.917, S(v2) 0.618, nll 3.6763.
OOD bound (rehearsal): Δnll ≤ max(2 × worst C_ctrl, 0.05) = 0.05.

## What the rehearsal established

1. **The pipeline works.** Every component ran end to end and every gate did
   its job — most notably RT-07, which fired *exactly* on the failure mode it
   was registered for: mean-ablating the index residual (a direction with a
   large reference-mean coordinate) inflates neutral-corpus NLL +0.265
   nats/token — an off-manifold intervention that, without the gate, could
   have been misread as degraded integration. The directional variant of the
   same ablation stays on-manifold (+0.033) — the registered
   mean-primary/directional-cross-check pairing is not redundant; it is the
   difference between a confound and a measurement.

2. **The substantive lesson: rank-1 ablation is too weak to move behaviour on
   this model.** Under the OOD-clean directional ablation of the very
   direction that restores 0.34 of referent-dependent logit behaviour, nothing
   moves: d_task ≈ 0 on all three batteries, d_self ≈ 0. Two non-exclusive
   readings, both instrument lessons for the registered run:
   - the self-structures are **distributed/redundant** beyond a per-layer
     linear direction — causal-for-logits ≠ load-bearing-for-behaviour at
     rank 1; the registered run needs a stronger, still-gated intervention
     (subspace ablation of the top-k directions, SAE-feature sets, or wider
     layer bands, escalated *until* the OOD gate binds);
   - battery resolution is coarse (12–20 items ⇒ one item = 5–8% steps), and
     S-judge noise across conditions is σ ≈ 0.05 (controls score d_self
     −0.02…−0.08) — battery n must grow and θ_self must sit well above that
     noise floor when it locks.

3. **The null is a null, not H_description.** d_self never approaches
   θ_self-scale movement (max +0.034 under the OOD-breached condition), so
   nothing here supports "the report is subtracted"; the honest reading is
   "this intervention did not remove enough of anything." Recorded to
   pre-empt the tempting misreading.

4. **Differential machinery behaves.** Controls' Δnll (+0.011/+0.012) gives
   the RT-07 relative bound teeth, and control d_task wobbles (±one item)
   bound the noise the δ threshold must clear.

## Consequences for the registered run (mini-day checklist additions)

- Pilot ablation-strength escalation (rank-1 → top-k subspace → SAE features)
  under the OOD gate *before* locking θ/δ; θ must be reachable by an
  on-manifold intervention or the test is unrunnable as specified.
- Grow T batteries (≥30 items/subset) and S battery for resolution; lock
  θ_self ≥ ~4× the measured judge noise.
- Keep the mean/directional pairing; report both, as registered.

## Rehearsal caveats

Sandbox model; rehearsal thresholds; S judged without the human spot-check
(pending, John); single seed; ablation band chosen from the causal-patching
profile rather than swept.
