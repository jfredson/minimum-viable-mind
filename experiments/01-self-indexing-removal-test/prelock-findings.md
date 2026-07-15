# Pre-lock bench bundle — findings (2026-07-15)

*Results of the three registered pre-lock checks run per `ablation-pilot-spec.md`
(committed `164e132` before the run) on Tulu-3-8B-SFT, RunPod cloud bench
(RTX PRO 4500 Blackwell, CUDA bf16). Raw artifacts:
`artifacts/substrate-migration/tulu-sft/prelock/` (gitignored). Grown batteries
from `a73da73`; cull + replacements below. Nothing here locks θ/δ — that
remains John's separate commit.*

## (a) Grown-battery baselines + cull — DONE, batteries at candidate-lock state

Baseline on the grown batteries (pilot `baseline` condition):
**T_si 0.938 (30/32), T_sr 0.933 (28/30), T_syntax 0.833 (25/30)**.
The instruction_following fix landed: **8/8** (was 3/5 = 0.600). The RT-02
coherence expectation holds at baseline (T_si ≈ T_sr).

**Cull (rule as pre-committed in `battery-growth-notes.md`):** nine
baseline-failing items dropped, none a format artifact:

- t21 (skipped step mid-chain), t24 (sign error) — genuine reasoning misses.
- **sr04 — the pre-named at-risk item, failed again** (arithmetic across two
  own outputs); dropped as committed, noted as binding-flavored.
- **sr32 — a genuine role-binding failure** ("You are the editor" →
  "I am the author. Answer: author."). The only true binding miss at baseline;
  dropped per rule but carried as a datapoint: Tulu-SFT role binding is not
  perfect at baseline.
- sx23, sx30 — positional-tracking misses.
- **sx24/sx25/sx26 — SFT refusal boilerplate** ("as an AI, I don't have the
  capability to count messages") overriding visible context. Substrate quirk
  worth remembering: meta-conversational counting triggers refusals flakily
  (identical phrasing passed in other items). Replacement turn-count items use
  only shapes that passed.

Nine replacements authored (t35, t36, sr33, sr34, sx31–sx35), cloning
baseline-passing shapes only; category floors restored (T 8/cat, T_sr and
T_syntax 10/cat; 32/30/30 items). **Replacement verification (bench): all
three batteries score 1.000 at baseline — 92/92 items pass**
(`postcull_baseline.json`). The candidate locked battery is fully
baseline-verified; every item can register a drop, and one flipped item is
≈0.031–0.033 of battery accuracy (the resolution θ_task must respect).

## (b) Ablation-strength escalation — the OOD gate binds at k ≥ 4

Dose-response table (Δnll = neutral-corpus NLL over baseline; RT-07 bound
0.05 nats; batteries as scored pre-cull — post-cull deltas unchanged in kind):

| condition | Δnll | T_si | T_sr | T_syntax |
|---|---|---|---|---|
| baseline | — | 0.938 | 0.933 | 0.833 |
| idxres mean k=1 | +0.008 ✅ | 1.000 | 0.933 | 0.800 |
| idxres mean k=4 | +0.065 ❌ | 0.875 | 0.933 | 0.800 |
| idxres mean k=8 | +0.056 ❌ | 0.906 | 0.967 | 0.800 |
| idxres mean k=16 | +0.087 ❌ | 0.812 | 0.933 | **0.600** |
| expert mean k=4 | −0.015 ✅ | 0.938 | 0.967 | 0.833 |
| expert mean k=16 | +0.124 ❌ | 0.938 | 0.867 | 0.800 |
| idxres directional k=1 | −0.002 ✅ | 0.906 | 0.900 | 0.767 |

**Per the committed selection rule: no k ≤ 16 is both OOD-clean and
behaviour-moving.** The OOD-clean set is {k=1}, and k=1 moves nothing beyond
noise (±1–2 items). The spec's loss-condition branch therefore applies as
written: rank-k residual-stream subspace ablation cannot reach θ on-manifold
under the 0.05-nat bound at these ranks, and **SAE-feature ablation (Llama
Scope) is the registered next escalation**, requiring its own spec addendum
before running.

Observations for John's adjudication (reported, not acted on):

1. **The breaches are marginal** (+0.056…+0.087), nothing like the
   rehearsal's mean-ablation blowout (+0.265 on the 2B). The 0.05 bound was
   set on the sandbox; whether it is correctly calibrated for this substrate
   is an open question — but loosening it after seeing these results is
   exactly what the discipline forbids, so any recalibration needs a
   re-registration with rationale independent of these outcomes (e.g. bound
   as a quantile of benign perturbations at matched rank).
2. **The k=16 damage pattern is structure-specific and points at RT-05, not
   H_center.** At k=16 the index-residual ablation drops T_syntax hardest
   (−0.233) and T_si (−0.126) while **T_self_relevant does not move (0.933)**
   — the opposite of the floor claim's prediction. Meanwhile the expert
   control at k=16, with a *larger* Δnll (+0.124), moves batteries far less.
   So the damage is not generic off-manifold degradation; it looks like the
   higher-rank index subspace contains **dialogue-state routing** (exactly
   RT-05's worry), and the thing the removal test cares about — self-binding —
   is not what rank-k ablation is removing.
3. **OOD asymmetry at matched rank:** idxres k=4 breaches (+0.065) while
   expert k=4 is fully on-manifold (−0.015). The index-residual subspace is
   more load-bearing for plain language modelling than a matched control —
   consistent with turn/boundary structure being woven into everything.

**d_self (S battery under ablation) — no condition produces a self-report
drop; every condition produces a small INCREASE** (S under rubric v2,
held-out judge; baseline = mean of two judge passes, 0.6375):

| condition | S | d_self (relative drop) |
|---|---|---|
| idxres mean k=1 | 0.688 | −0.078 |
| idxres mean k=4 | 0.725 | −0.137 |
| idxres mean k=8 | 0.725 | −0.137 |
| idxres mean k=16 | 0.721 | −0.131 |
| expert mean k=4 | 0.667 | −0.046 |
| expert mean k=16 | 0.679 | −0.065 |
| idxres directional k=1 | 0.700 | −0.098 |

**Human spot-check (pre-registered judge control): PASSED AS-IS — John,
2026-07-15.** Sample reviewed side-by-side (baseline vs idxres_mean_k4): the
five largest fidelity increases (s28, s29, s21, s14, s06), the one real
decrease (s26), and a low-flat item (s08). Dimension-level breakdown shows the
battery increase is carried by **referential self-tracking itself**
(+0.27…+0.33 at k4/k8 vs +0.03 for the expert control) and non-confabulation,
not coherence; output length is flat (295 vs 318 chars), so it is not a
brevity artifact. The judge is consistent in both directions (it still docks
constraint violations and uncalibrated claims in the higher-scoring ablated
responses). **Interpretation adopted: deflection-unmasking** — baseline S is
depressed by trained disclaimer boilerplate ("As an AI language model, I
don't…"), which rubric v2 correctly scores down; the index-residual ablation
suppresses that reflex and plainer self-reference scores up. Consequences:
(i) the prelock d_self numbers are usable; (ii) S on this substrate is partly
an inverse measure of deflection boilerplate — the decision rule only fires on
drops, so the test stays valid, but the θ_self lock rationale must carry this
caveat; (iii) the unmasking read makes a falsifiable prediction for the RT-06
ladder (deflection and the ablation-raises-S effect should grow with
alignment depth), to be registered in the ladder spec before it runs.

Negative d_self means ablation *raised* judged fidelity. The index-residual
increases (+0.08…+0.14) exceed the control arm's (+0.05…+0.07), i.e. they are
~2× the control wobble and ~2–3× the bootstrap SE — probably not pure noise,
and in the *opposite* direction from the floor claim's prediction. Consistent
with observation 2: whatever rank-k ablation removes here, it is not the
machinery of referential self-tracking; if anything the outputs got slightly
more concrete under ablation (category means rose mostly in self_monitoring
and self_vs_other). These scores await the pre-registered human spot-check
before anything leans on them.

## (c) RT-10 causal-margin stability — STABLE; PASS is robust

Four length-direction fits, patched comparison per `rt10_stability.py`
(sweep L22–L30, peak by the registered rule at **L25**):

| length fit | restore(length) at peak | margin vs C_self (0.213) |
|---|---|---|
| repro (turn_role lstsq, the original) | 0.094 | **+0.119** |
| pooled (all 5 mechanisms) | 0.022 | **+0.190** |
| ridge (LOO-CV, pooled) | 0.024 | **+0.189** |
| out-of-contrast (neutral texts) | 0.002 | **+0.211** |

All four ≥ 0.10 ⇒ **PASS by the committed rule**, and the reading is stronger
than the rule required: the more independent the length fit, the *less* it
restores. The original narrow +0.117 margin was an artifact of the length
control being fit on the contrast stimuli themselves (partially contaminated
with C_self); a genuinely independent length direction restores ~nothing.
Substrate-gates caveat 3 is closed. (Sandbox replication same day: stable,
margins +0.33 across all four fits.)

**Judge noise re-measured (spec §a):** two independent judge passes on the
identical baseline responses give battery-level S of 0.6417 / 0.6333
(|Δ| = 0.008; 24/30 items scored identically, item-level pass–pass SD 0.085).
Bootstrap-over-items SE of the battery mean: 0.040. The binding number for
θ_self is the **control-arm d_self wobble, 0.05–0.07 relative** — consistent
with the rehearsal's σ ≈ 0.05. Under the registered rule (θ_self ≥ ~4× judge
noise) that puts θ_self at roughly ≥ 0.2 relative; the actual value is John's
lock decision.

## Standing after this bundle

- **Batteries: candidate-lock item set committed and fully baseline-verified
  (92/92).** RT-02 coherence holds; instruction_following fixed.
- **RT-10: closed, stable** — the strongest of the three results; the length
  deflation is dead on independent fits.
- **Ablation strength: the rank-k path is exhausted per the committed rule**
  (no OOD-clean k moves behaviour), and the breached-k pattern (T_syntax
  drops, T_sr and S do not) points at RT-05 dialogue-state routing rather
  than self-binding. **Next instrument step: SAE-feature ablation spec
  addendum (Llama Scope), pre-committed before running.**
- For John: (1) human spot-check of the prelock judge scores; (2) adjudicate
  the OOD-bound calibration question (observation 1) — recalibration, if any,
  needs an outcome-independent rationale; (3) θ/δ lock remains blocked on the
  SAE-feature pilot + RT-06 ladder.
