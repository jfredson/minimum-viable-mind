# Substrate-migration gate re-verification — Tülu-3-8B-SFT (2026-07-13)

*Step 2 of the migration (baselines: `substrate-baseline-findings.md`). Full
Stage-1 localization chain + red-team gates re-run on the registered substrate
(cloud bench, RTX 5090, CUDA bf16). Code parametrization in commit `3fbc2de`
(renderer via the checkpoint's chat template, layer sweeps rescaled 26→32,
Llama Scope SAEs); Gemma sandbox behavior verified byte-identical. Raw
artifacts in `artifacts/substrate-migration/tulu-sft/stage1/` (gitignored).*

## Gate table (pass criteria from the pilot registrations)

| Gate | Criterion | Tülu-3-8B-SFT | Pilot (2B) | Verdict |
|---|---|---|---|---|
| RT-10 length gate | label-from-length ≈ chance; length-AUC ≈ 0.5 | acc 0.40–0.54; AUC ≈ 0.50 (turns mechanisms) | 0.44–0.52 | **PASS** |
| Embedding floor | margin ≤ 0.10, all mechanisms | **+0.000 × 5** | +0.00 | **PASS** |
| Computed signal | layer ≥ 2 with margin ≥ 0.15 | all 5, +0.34…+0.57 | +0.55 | **PASS** |
| Finding 1 (C_self-index causal) | restore(C_self) − restore(random) ≥ 0.10 | 0.200 vs −0.007 @ L27 → **+0.206** | +0.340 @ L22 | **PASS** |
| RT-10 causal | C_self − length-direction ≥ 0.10 | 0.200 vs 0.083 → **+0.117** | +0.328 | **PASS** (see caveat 3) |
| RT-09 reflexivity | generic verdict fires only if cross-decode ≥ .9 AND \|cos\| ≥ .5 AND ratio ≥ .5 | 1.000 ✓ / 0.324 ✗ / 0.114 ✗ | 1.000 / 0.148 / −0.005 | **does not fire — PASS** |
| RT-04 geometric | own AUC / cross-decode / \|cos\| | PARTIALLY SEPARABLE, median \|cos\| 0.18, residuals decode 1.00 | PARTIAL, \|cos\| 0.23–0.28 | same reading |
| RT-04 causal (decisive) | both cross-patch ratios < 0.50 | **0.063 / 0.054** @ L27 | 0.282 / 0.273 | **FUNCTIONALLY SEPARABLE — PASS** |
| Method (b) SAE convergence | decode margin ≥ 0.15 AND proj-fraction ≥ 0.50 | decodes (+0.55) but proj 0.18–0.32 < 0.50 | decodes but proj 0.28–0.44 | **not converged — registered fallback (causal patching) stands, same as pilot** |

## Substrate differences worth carrying forward

1. **turn_role signal is nearly immediate on Tülu** — perfect linear decode by
   L3 (embedding floor still clean at +0.000), vs a mid-stack rise (peak L15)
   on the 2B pilot. One attention pass over Tülu's explicit `<|assistant|>`
   headers appears to move the referent to the readout. The floor gate still
   discriminates lexical vs computed; but "middle-layers rise" is a
   sandbox-specific expectation, not a property of the design.
2. **The causal peak moved late**: L27 of 32 (~84% depth) for both structures,
   vs L22 of 26 (~85%) — same depth fraction, reassuringly.
3. **RT-10 causal margin narrowed**: +0.117 (vs pilot +0.328). It clears the
   ≥ 0.10 bar but a stronger length control could plausibly eat it. Before
   θ/δ lock, re-run with the length direction fit on more stimuli (or an
   affine length model) to confirm the margin is stable.
4. **Restoration magnitudes are lower overall** (own-restore 0.200–0.273 vs
   pilot 0.340) while cross-patch ratios are *much* cleaner (0.05–0.06 vs
   0.27–0.28). Rank-1 interventions move an 8B model relatively less — consistent
   with the rehearsal's "rank-1 too weak" finding and the planned escalation
   to top-k subspace / SAE-feature ablations.
5. **Xet/CDN operational note**: hf_hub forwards `HF_TOKEN` to the Xet CAS
   bridge, which 401s on public repos (fnlp/Llama-Scope). Rule: token only for
   gated weights; unset it for public SAE fetches (and `HF_HUB_DISABLE_XET=1`
   on low-RAM pods).

## Standing after this run

All pilot gates re-verify on the registered substrate. The C_self-index /
C_self-narrative picture (computed, causal, functionally separable, reflexive
residual survives) reproduces on a 4×-larger, lightly-RLHF'd model with the
pilot's decision rules unchanged. Remaining before θ/δ lock (unchanged):
battery growth (≥30 items/subset; fix instruction_following), stronger-ablation
pilot under RT-07, RT-10-causal margin stability check (caveat 3), and RT-06
ladder work (needs Tülu DPO/RLVR checkpoints + volume resize).
