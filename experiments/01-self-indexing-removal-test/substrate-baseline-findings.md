# Substrate-migration baselines — Tülu-3-8B-SFT (2026-07-13)

*Step 1 of the migration to the registered substrate (see
`registered-run-model-comparison.md`, Addendum 2026-07-13). Generated on the
cloud bench (RTX 4090, CUDA bf16, deterministic decoding), model selected via
the `MVM_MODEL` env override — the config pin is untouched. Raw outputs in
`artifacts/substrate-migration/tulu-sft/` (gitignored). These are REFERENCE
numbers for gate re-verification and eventual θ/δ lock; nothing here is a
finding about the removal hypothesis.*

## Numbers

| Battery | Tülu-3-8B-SFT | 2B sandbox (pilot) |
|---|---|---|
| T (task), 20 items | **0.900** | 0.750 |
| — multi_step_reasoning | 1.000 (5/5) | — |
| — coreference_binding | 1.000 (5/5) | — |
| — needle_synthesis | 1.000 (5/5) | — |
| — instruction_following | 0.600 (3/5) | (weak category on sandbox too) |
| T_self_relevant (RT-02), 12 items | **0.750** | — |
| T_syntax (RT-05), 12 items | **0.917** | — |
| S fidelity, rubric v2, 18 items (held-out judge: Claude) | **0.639** | 0.615 (v1 rubric — not comparable) |
| — first_person_activity | 0.500 | |
| — self_monitoring | 0.594 | |
| — self_vs_other | 0.625 | |
| — forced_third_person (RT-03) | 0.771 | |

## Reads and caveats

- **Headroom is good.** T at 0.900 leaves real room to observe an ablation
  *drop* (the pre-registration's d_task is a relative drop; a saturated or
  floored battery can't move). Three categories are at ceiling (5/5) though —
  at 5 items/category, one flipped item is a 0.2 swing; the rehearsal
  finding that batteries must grow to ≥30 items/subset before θ/δ lock stands.
- **instruction_following (0.600) is again the weak T category** — same
  pattern as the sandbox precedent noted in `run_t_controls.py`'s floor check.
  Revise or expand this category during battery growth, or it contributes
  noise, not signal.
- **own_commitment items went 2/4** (sr05, sr06 missed) inside T_self_relevant
  — worth eyeballing the transcripts before treating T_sr = 0.750 as solid.
- **S = 0.639 is a v2-rubric number on a new substrate** — not comparable to
  the sandbox's 0.615 (v1). It becomes S_base only after the pre-registered
  human spot-check on a sample of judge scores (John, pending).
- Judge noise floor for θ_self calibration should be re-measured against these
  responses (rehearsal rule: θ_self ≥ ~4× judge noise).

## Next (per pre-registration order)

1. Human spot-check of judge scores (John).
2. Re-run localization (probes + causal patching) and gates RT-01/02/04/05/07/09/10
   on Tülu-SFT.
3. Grow batteries to ≥30 items/subset; fix instruction_following.
4. Stronger-ablation pilot (top-k subspace, SAE features) under RT-07.
5. θ/δ lock (separate commit) — then, and only then, the registered run.
