# RT-06 ladder — findings (started 2026-07-16)

*Results against `rt06-ladder-spec.md` (registered `4611c66` before any rung
ran). SFT-rung numbers are computed from existing committed artifacts; DPO /
RLVR / Instruct rungs fill in as the bench sessions complete.*

## SFT anchor (from prelock artifacts, marker list as registered)

Deflection rate = fraction of S-v2 responses matching the spec's marker list:

| condition | deflection rate | judged S (v2) |
|---|---|---|
| baseline | **16/30 = 0.533** | 0.6375 |
| idxres mean k=4 | **6/30 = 0.200** | 0.7250 |
| idxres mean k=16 | 9/30 = 0.300 | 0.7208 |
| expert mean k=4 (control) | 14/30 = 0.467 | 0.6667 |

The pattern the unmasking read predicts is already visible within the SFT
rung: the index-residual ablation cuts deflection by more than half
(0.533 → 0.200) while the matched control barely moves it (0.467), and the
judged-S increase tracks the deflection drop. P1/P2 now ask whether the
*baseline* rate and the *ablation effect* grow up the ladder.

## Ladder table (Tulu family; Instruct = off-family reference)

| | SFT | DPO | RLVR |
|---|---|---|---|
| deflection rate, baseline | **0.533** | 0.333 | **0.267** |
| deflection rate, k=4 ablation | 0.200 | 0.400 | 0.300 |
| S (v2, judged), baseline | 0.6375 | 0.6458 | **0.6875** |
| S, k=4 ablation | 0.7250 | 0.6167 | 0.6958 |
| d_self (k=4) | **−0.137** | +0.045 | −0.012 |
| RT-06 cross-patch ratio (expert→index) | (sandbox 0.18) | 0.059 | 0.026 |
| RT-06 third-person verdict | ✅ | ✅ | ✅ |
| embedding floors (5 mechanisms) | +0.000 ✅ | +0.000 ✅ | +0.000 ✅ |
| T baseline (si / sr / syn) | 1.00/1.00/1.00 | 0.97/0.87/0.93 | 0.97/0.93/0.93 |

(T batteries were culled against SFT baselines, so the DPO/RLVR baseline
misses are expected substrate variation, reported not culled. k=4 Δnll ≈
+0.10 at both new rungs — same marginal-breach band as SFT; the OOD caveat
carries and the cross-rung comparison is unaffected.)

## P1–P4 verdicts (against `rt06-ladder-spec.md`, registered `4611c66`)

- **P1 — LOSES, reversed.** Baseline deflection *falls* monotonically with
  alignment depth (0.533 → 0.333 → 0.267). Deflection boilerplate in this
  family is an SFT-stage artifact that preference/RLVR training largely
  removes — not alignment-deepened self-presentation.
- **P2 — LOSES.** The ablation-raises-S effect vanishes up the ladder
  (d_self −0.137 → +0.045 → −0.012); the within-rung deflection suppression
  also reverses (SFT 0.533→0.200 under ablation; DPO 0.333→0.400; RLVR
  0.267→0.300). **The deflection-unmasking read is retracted as a general
  account, per the spec's own loss clause.** What survives is the narrower,
  rung-specific fact: *at SFT*, the index-residual subspace is entangled
  with the deflection reflex. By RLVR that entanglement is gone.
- **P3 — HOLDS at every rung: RT-06 is RESOLVED.** The expert persona stays
  functionally third-person all the way up (cross-patch ratios 0.059/0.026
  on index — *cleaner* with more alignment, not worse). The red team's
  "structurally unavoidable in heavily-RLHF'd models" prediction is defeated
  in this family; a capability-gating C_ctrl is available at every rung and
  the load-bearing differential is alive. RT-01 frequency and centrality
  checks also pass at both new rungs.
- **P4 — HOLDS.** Floors +0.000 and clean for all five mechanisms at every
  rung; computed signals +0.45–0.60. The context-set design is
  substrate-robust within the family.

## Consequences

1. **The last pre-lock gate is resolved in the design's favour** — RT-06 no
   longer blocks θ/δ lock; the C_ctrl-expert arm is validated on the
   registered substrate class.
2. **For the lock rationale:** at the registered SFT rung, S movements under
   ablation can be deflection-mediated *upward* (the retracted read's
   surviving kernel). The decision rule fires only on drops, so the test
   stays valid; small S increases at SFT must not be over-interpreted.
3. **Ladder deliverable:** self-structure geometry is essentially stable
   across alignment stages (floors, signals, separability), while
   surface self-presentation (deflection, S fidelity) changes markedly —
   alignment training in this family edits the *policy*, not the *geometry*
   we localize. Publishable as part of the methods/ladder paper.

## Instruct reference (off-family; no predictions attach)

`meta-llama/Llama-3.1-8B-Instruct`, run with the identical battery (one
instrument fix en route: eos-as-pad for Meta's pad-less tokenizer,
`03dc513`). Consistent with — and extending — the family trend:
deflection **0.100** baseline (lowest of any rung; 0.167 under k=4), S
0.7375 baseline / 0.7208 under k=4 (d_self +0.023, ~noise), RT-06
third-person with the cleanest ratio yet (0.020 / 0.343), floors +0.000
clean ×5, T 0.94/0.97/1.00 unmoved by ablation, and — notably — the k=4
ablation is fully on-manifold here (Δnll +0.012 vs ~+0.10 on the Tulu
rungs). Across two independent post-training pipelines, deeper alignment
coincides with less deflection, cleaner expert/self separation, and a less
load-bearing index subspace — the opposite of the RT-06 fear in every
column.
