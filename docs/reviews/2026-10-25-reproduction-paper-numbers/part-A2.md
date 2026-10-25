# A2 — paper lines 185–318, 842–900 (less 883–886), 971–1057, 1205–1225

Checker A2, 2026-10-25. Clean clone at `dacc7b4`. $0 spent; no model downloaded, no API called, nothing rented.
Script written: `work-A2/router_gap_ci.py` (in the clone's parent folder, `scratchpad/repro/work-A2/`).

## Summary

58 rows: **Reproduced 35 · Differs 5 · Not reproducible 18.** A sixth discrepancy, the Fig. 3 legend contradicting L290, has no row of its own because it is not a number. It is listed as Differs item 6 below.

**What could be recomputed.** None of the per-layer margins, patching restorations, cross-patch ratios, null-calibration draws, judge scores or ladder generations are committed. Everything under `artifacts/` is gitignored, and this includes the `stage1/`, `substrate-migration/`, `prelock/` and `removal_test/` outputs. What *is* committed and was checked directly:
- stimulus and battery files (item counts, categories, mechanisms);
- the code constants (layers, seeds, quantile, prompts, tokens, PCA cap, judge model);
- git history (every cited hash);
- `removal_ci.json`. Its primary-condition cells and the router-control margin interval (+0.033, −0.133 to +0.200, which spans zero) were rebuilt exactly from the committed flip list, the item order and the committed seed and bootstrap code (`work-A2/router_gap_ci.py`).

**Commit hashes, all Reproduced.** Every hash exists, touches the file the paper says it does, and comes in the order claimed:
1. `1181a40` (thresholds re-registered), 2026-07-17 18:23.
2. `2fdf2cc` (calibration runner), 2026-07-17 18:30.
3. Calibration results `e14ed4c`, 2026-07-18 14:38.
4. Lock `8b1fcbe`, 15:35. It changes `thresholds.md` only, and that file is not touched again afterwards.
5. Spec `3df532d`, 15:37.
6. 122 items authored `cf06b49`, 15:48.
7. Runner `a4efcf0` (plus cull pass 1), 16:35. The runner is not modified afterwards.
8. Final test set `a11e769`, 16:48.
9. Registered result `692510c`, 18:03.

RT-09's registration `7bb4355` (07-01) and RT-10's `b6eaf39` (07-12) both come before their runs and before the lock.

**Differs (6):**
1. **L1042 "T_si eight categories".** The committed T_si battery (pilot and test) has **4 categories × 8 items**: multi-step reasoning, coreference binding, needle synthesis and instruction following. The test-set spec says the same. The paper has probably turned "eight per category" into "eight categories".
2. **L230 / L1019–1027: ten controls described as the product of the adversarial review loop.** The red-team ledger records **RT-10** as Pass 4, an "empirical self-audit … (not from the Gemini loop)". RT-09 is filed as "external review". So 9 of the 10 came from review and 1 from self-audit. Also, RT-08 was "accepted risk, folded into RT-07" and is not a separate control.
3. **L312–313: "the only S drop ever observed in this experiment".** The registered run itself shows small positive d_self, meaning S fell: primary +0.059, narrative +0.039, control +0.020 (`removal-test-findings.md`, `removal_ci.json`). `prelock-findings.md` calls the SAE zero-mode +0.177 "the program's *first* S drop". The defensible wording is "the only S drop beyond noise" or "the largest".
4. **L996: "RTX 4090/5090 class".** The baselines ran on an RTX 4090 and the gates on an RTX 5090. But the prelock dose-response, the SAE pilot and the null calibration that produced the 2.2× and 0.003–0.007 figures ran on an **RTX PRO 4500 Blackwell** (`prelock-findings.md` header and §e). This is minor, but as written it is not accurate.
5. **L290: alignment-ladder leakage "0.059 → 0.026 → 0.020".** The numbers exist, but they belong to **DPO → RLVR → Instruct**. The paper's parallel chain for deflection (0.533 → 0.333 → 0.267) is SFT → DPO → RLVR, so readers will take the leakage chain as SFT → DPO → RLVR. No registered-substrate SFT expert cross-patch ratio is in the record; the ladder table gives only "(sandbox 0.18)". So "the objection loses at every rung" has no committed SFT number on Tülu behind it.
6. **L1222–1225: Fig. 3 says control cross-patch ratios are "stable"**, while the main text (L290) says they are "*falling*". The paper contradicts itself. The findings say "cleaner with more alignment", which means falling.

**Not reproducible (21).** All are GPU or model outputs whose raw records are gitignored. Each matches its findings file unless noted. The ones that need flagging, because they match only a *superseded or pilot* pass while the text reads as the registered substrate:
- **L242 "17 of 26 layers" at ceiling.** This comes from `STATUS-archive.md` (role-declarative v2, chat mode, Gemma 2B). The same archive entry block records two problems: the padding-side readout bug, after which "every earlier probe/SAE number this session … is not trustworthy in detail"; and a later correction that the earlier "leak" was partly from labelling `resid_post[0]` as the embedding. So "at the token-embedding layer, before any computation" may rest on that mislabel. It has not been re-derived with the fixed code.
- **L259–260 "+0.56", "rising through the stack".** This is the v1 Gemma pilot, length-confounded, with its peak at L24. The length-matched v2 pilot gives +0.55 at L15. On the registered Tülu substrate the signal is "perfect linear decode by L3" (`substrate-gates-findings.md`), so "rising through the stack" is pilot-only, as is the Fig. 2a legend.
- **L271 "median |cos| 0.28".** This is the Gemma pilot v1 under the old PCA convention. It was corrected to 0.23 at k=12, and the **registered substrate gives 0.18**.
- **L277–278 "cross-patch ratio 0.006 vs 0.348".** This is the **v1 Gemma pilot pass that RT-10 found length-confounded**. The length-matched v2 pilot gives **−0.005 vs 0.340**. The **registered substrate gives 0.114** (own restoration 0.200). The paper also sets a ratio (0.006) against a restoration (0.348), which are different quantities.
- **L274 "0.27 in the sandbox pilot".** The findings give 0.282 and 0.273, so "0.27–0.28" would be accurate.
- **L262 "restoration 0.206".** 0.206 is the margin over the random control (0.200 vs −0.007). The raw restoration is 0.200.

**Estimated cost to regenerate the GPU-borne numbers in this section** (8B models; rented RTX 5090 at $0.99–$1.19/h; the only timing in the repo is the null calibration, 47 min, about $0.60 on an RTX PRO 4500):
- Stage-1 chain re-verification on Tülu-SFT (0.206, L27, 0.05–0.06, RT-09 ratio, floors): about 1 GPU-h, $1–1.20.
- RT-06 ladder, 3 further rungs (DPO, RLVR, Instruct; each a localisation chain plus baseline and k=4 generations): about 2–3 GPU-h, $2–3.60.
- Prelock dose-response (7 conditions) plus null calibration plus SAE pilot: about 1.5–2 GPU-h, $1.50–2.40.
- **Total about 5–6 GPU-hours, about $5–7**, plus about 570 judge calls (30 items × 19 S conditions across prelock, ladder and SAE) for the S and d_self numbers. The deflection rates need only generations and a regex, no judge.
- The Gemma-2B pilot numbers (17/26, +0.56, 0.28, 0.27, 0.006/0.348) would run on the laptop at $0, roughly 1–2 h. But `google/gemma-2-2b-it` is a gated download that needs the licence accepted on Hugging Face, which was not done here.

## Table

| # | paper line | number as stated | what it is (plain words) | source in repo | how checked (command or script) | result | note |
|---|---|---|---|---|---|---|---|
| 1 | 230 | RT-01 through RT-10 (ten controls) "resulting" from the adversarial review | count of red-team controls patched in before the lock | `red_team_ledger.md` | `grep -oE 'RT-[0-9]+' red_team_ledger.md \| sort -u`; read the Pass 4 header | Differs | Ten IDs exist and all predate the lock (`b6eaf39` is 07-12, `8b1fcbe` is 07-18). But RT-10 is recorded as "empirical self-audit … (not from the Gemini loop)" |
| 2 | 242 | 17 of 26 layers at ceiling, at the token-embedding layer | role-declarative probe reaching 1.000 accuracy from layer 0 (Gemma 2B pilot) | `STATUS-archive.md` L3430; stimuli `matched_self_speaker_stimuli_v2.jsonl` (224 rows, committed) | grep; stimuli counted (224 = 112/112) | Not reproducible | Matches the archive. Activations not committed; needs gated Gemma-2B (laptop, $0, about 1 h). Archive caveat: computed before the padding fix, and "layer 0" may have been `resid_post[0]` mislabelled as the embedding |
| 3 | 256 | +0.00 | required embedding-floor margin | `stage1-localization-findings.md`, `substrate-gates-findings.md` | read | Not reproducible | Matches: +0.000 × 5 mechanisms on Tülu, +0.00 on the pilot. Activations gitignored |
| 4 | 259 | +0.00 | turn-role margin at the embedding | same | read | Not reproducible | Matches the findings |
| 5 | 260 | +0.56 | peak turn-role decoding margin | `stage1-localization-findings.md` F1, `rt09-reflexivity-findings.md` §1 | read | Not reproducible | Matches the **v1 Gemma pilot** (peak L24, length-confounded). v2 pilot gives +0.55 at L15. Tülu gives +0.34…+0.57 and is perfect by L3, so "rising through the stack" is pilot-only |
| 6 | 262 | 0.206 | causal restoration by C_self-index on the registered substrate | `substrate-gates-findings.md` gate table | read; 0.200 − (−0.007) = 0.207 | Not reproducible | Matches, but 0.206 is the *margin over random*. Raw restoration is 0.200. Patching outputs gitignored (about 1 GPU-h, about $1) |
| 7 | 263 | layer 27 of 32 | causal peak layer | `substrate-gates-findings.md` | read | Not reproducible | Matches the findings |
| 8 | 264 | ≈ 0.00 at every layer | random-direction control | same | read | Not reproducible | Matches (−0.007 at L27) |
| 9 | 271 | median \|cos\| 0.28 | angle between index and narrative directions | `stage1-localization-findings.md` F3 | read | Not reproducible | Matches the **Gemma pilot only**. Revised to 0.23 under the k=12 fix (`rt09…` §5). The **registered substrate gives 0.18** (`substrate-gates-findings.md`) |
| 10 | 273 | 0.05–0.06 | cross-patch substitution ratios on the registered substrate | `substrate-gates-findings.md` (0.063 / 0.054 @ L27) | read; rounding | Not reproducible | Matches the findings (0.054 → 0.05, 0.063 → 0.06) |
| 11 | 274 | 0.27 | sandbox cross-patch ratio | `stage1-localization-findings.md` addendum (0.282 / 0.273) | read | Not reproducible | Only half matches: 0.282 rounds to 0.28. "0.27–0.28" is accurate |
| 12 | 275 | 0.5 | pre-committed separability line | `substrate-gates-findings.md` criterion "both cross-patch ratios < 0.50"; `pre-registration.md` | read | Reproduced | The line is in the committed criteria |
| 13 | 277 | 0.006 | generic-speaker cross-patch ratio (RT-09) | `rt09-reflexivity-findings.md` §2 | read | Not reproducible | Matches the **v1 pilot pass, superseded as length-confounded**. v2 pilot gives −0.005. **The registered substrate gives 0.114** |
| 14 | 278 | 0.348 | C_self-index restoration given in the same comparison | `rt09-reflexivity-findings.md` §2 | read | Not reproducible | Matches v1 pilot. v2 gives 0.340; Tülu gives 0.200. This is a restoration, not a ratio, so "0.006 vs 0.348" compares different quantities |
| 15 | 287 | SFT, DPO, RLVR + Instruct (4 rungs) | ladder composition | `rt06-ladder-findings.md`, `rt06-ladder-spec.md` (`4611c66`) | read; git | Reproduced | Spec registered 2026-07-15 17:01, before the ladder results `213489e` at 18:13 |
| 16 | 290 | 0.059 → 0.026 → 0.020 | expert-persona cross-patch leakage up the ladder | `rt06-ladder-findings.md` table + Instruct section | read | Differs | The values match but belong to **DPO → RLVR → Instruct**, while the parallel deflection chain is SFT → DPO → RLVR. The SFT/Tülu value is not in the record (only "sandbox 0.18") |
| 17 | 292 | 0.533 → 0.333 → 0.267 | baseline deflection rate, SFT → DPO → RLVR | `rt06-ladder-findings.md` | read; 16/30, 10/30, 8/30 | Not reproducible | Matches the findings, and the arithmetic of the counts agrees with the spot-check note (10/12, 8/9, 3/5). Generations not committed (about 2–3 GPU-h for the rungs, about $2–3.60) |
| 18 | 292 | Instruct 0.100 | Instruct baseline deflection | same | read; 3/30 | Not reproducible | Matches the findings |
| 19 | 305 | 95th percentile | quantile defining the null bound | `src/run_ood_calibration.py` L62 `QUANTILE = 0.95`; `thresholds.md` Pass 5 (`1181a40`) | grep | Reproduced | Committed before the run |
| 20 | 305 | 20 | random rank-k null ablations per k | `run_ood_calibration.py` L61 `N_SEEDS = 20` | grep | Reproduced | — |
| 21 | 308 | 2.2× | rank-4 Δnll relative to its null bound | `prelock-findings.md` §e (+0.065 / +0.0302) | arithmetic: 0.065/0.0302 = 2.15 | Reproduced (arithmetic) | Inputs not reproducible (calibration json gitignored, 47 min, about $0.60) |
| 22 | 309 | 0.003–0.007 nats | re-admission margins for rank-16 and rank-8 | `prelock-findings.md` §e; `removal-test-findings.md` (+0.0867 vs 0.0893) | 0.0630 − 0.056 = 0.007; 0.0893 − 0.0867 = 0.0026 | Reproduced (arithmetic) | With the 3-decimal prelock +0.087, k=16 gives 0.0023. The 0.003 needs the 4-decimal registered-run value |
| 23 | 312–313 | "the only S drop ever observed" | count of self-report drops | `prelock-findings.md` §d (+0.177 "first S drop"); `removal_ci.json` d_self | read json | Differs | Registered-run d_self is positive (a drop) for the primary (+0.059), narrative (+0.039) and control (+0.020) arms. It is the only drop *beyond noise* |
| 24 | 314 | Δrep-4 | long-generation repetition probe added to the gate | `thresholds.md` Pass 5; `run_ood_calibration.py` | grep | Reproduced | Exists and was registered at `1181a40`/`2fdf2cc` |
| 25 | 858 | 8B | substrate size | `substrate-*-findings.md`; model id | read | Reproduced | Llama-3.1-Tulu-3-8B-SFT |
| 26 | 880 (in range, outside the cost sentence) | "re-read two months later … span zero" | router-control margin interval | `removal_ci.json` `derived.router_gap_idxres_mean_k16`; rulings 2026-10-07 | `work-A2/router_gap_ci.py` rebuilds +0.0333 [−0.1333, +0.2000] exactly | Reproduced | The interval rebuilds exactly from the committed flips, item order and seed. Dates: run 2026-07-18; interval computed 2026-08-04 (`10481e2`); re-read 2026-10-07 (about 2.6 months). It was already on file 17 days after the run |
| 27 | 888 | one pass per registered condition | — | `removal_ci.json` config note | read | Reproduced | "single registered pass per condition" |
| 28 | 889 | 95% item-resampling CIs | interval method | `removal_ci.json` config (alpha 0.05, item-level bootstrap, B = 10,000, seed 20260804) | read; script reproduces T cells | Reproduced | Primary cells for T_si, T_sr and T_syntax rebuilt exactly |
| 29 | 897–898 | 30 million parameters | scale of the constructed line | `experiments/06-…/blind-arm-findings.md` L109 | grep | Reproduced | "unvalidated at 30M" |
| 30 | 899 | 2026-09-16 | date of John's ruling | `blind-arm-findings.md` L3, L22 | grep | Reproduced | — |
| 31 | 978 | `2fdf2cc` | Pass-5 calibration runner | git | `git show --stat 2fdf2cc` | Reproduced | Adds `src/run_ood_calibration.py`, 2026-07-17 18:30, before the results `e14ed4c` (07-18 14:38) and the lock |
| 32 | 978 | `1181a40` | Pass-5 OOD re-registration | git | `git show --stat 1181a40` | Reproduced | Touches `thresholds.md` and `pre-registration.md`, 2026-07-17 18:23 |
| 33 | 979 | θ_task = 0.10, θ_self = 0.25, δ = 0.10 | locked thresholds | `thresholds.md` | `git show 8b1fcbe` | Reproduced | Values are in the diff |
| 34 | 979 | `8b1fcbe` | threshold lock commit | git | `git log -- thresholds.md` | Reproduced | Touches only `thresholds.md`; 07-18 15:35, before any test item; no later edit to `thresholds.md` |
| 35 | 980 | `3df532d` | test-set authoring spec | git | `git show --stat`; `git log -- test_*.jsonl` | Reproduced | 15:37, before the first item commit `cf06b49` (15:48) |
| 36 | 980–981 | `a11e769` | test-set finalisation | git | `git show --stat` | Reproduced | Cull pass 2, "92/92 … FINAL", 16:48, before the result `692510c` (18:03) |
| 37 | 981 | `a4efcf0` | registered runner | git | `git show --stat`; `git log -- run_removal_test.py` | Reproduced | Adds `run_removal_test.py`, 16:35; never modified afterwards. It predates the final cull by 13 min, which is consistent with the paper |
| 38 | 982 | 92-item pilot batteries | pilot T item count | `src/batteries/task_battery*.jsonl` | line counts: 32 + 30 + 30 | Reproduced | — |
| 39 | 984 | 2026-10-07, decision 2 | ruling requiring the disclosure | `docs/rulings/2026-10-07-two-sided-question-rulings.md` | read | Reproduced | Decision 2 requires the wager-date disclosure |
| 40 | 988 | 2026-09-20 | date the founding wager was adopted | same ruling; `docs/founding-wager-proposal-2026-09-20.md` | read | Reproduced | Ruling: "2026-09-20, after A, B and D ran" |
| 41 | 996 | RTX 4090/5090 class | GPUs used | `substrate-baseline-findings.md` (4090); `substrate-gates-findings.md` (5090); `prelock-findings.md` (RTX PRO 4500 Blackwell) | read | Differs | Prelock, SAE pilot and null calibration ran on an RTX PRO 4500 Blackwell |
| 42 | 998 | 16 GB laptop | pilot hardware | `STATUS-archive.md` L3289, L3483 | grep | Reproduced | — |
| 43 | 1001 | 48 per mechanism | stimuli per mechanism | `src/probes/context_self_speaker_stimuli.jsonl` | Python Counter: 5 mechanisms × 48 (24/24) | Reproduced | Includes expert_persona as a fifth mechanism |
| 44 | 1008 | PCA(≤15) | probe dimensionality cap | `src/localize_context.py` L59 `k = min(15, max(2, n // 4))` | grep | Reproduced | — |
| 45 | 1011 | +0.00 | lexical-floor requirement | `localize_context.py` / findings (gate "≤ 0.10" in `substrate-gates-findings.md`) | read | Reproduced | The paper is stricter than the gate criterion (≤ 0.10); observed values were +0.000 |
| 46 | 1015 | 0.5 | substitution-ratio line | as row 12 | read | Reproduced | — |
| 47 | 1021 | ten findings | red-team findings count | ledger | as row 1 | Reproduced | Count of IDs = 10. Origin attribution: see row 1 |
| 48 | 1031 | k = 16 | selected rank | `prelock-findings.md` §e item 3 | read | Not reproducible | Matches the findings ("Candidate strength = k=16"). The selection data are gitignored |
| 49 | 1032 | layers {10, 14, 17, 22, 27} | ablation layers | `run_removal_test.py` L59 `scale_layers([8,11,14,18,22])`, `config.NUM_LAYERS = 26` | computed rescale for 32 layers → [10, 14, 17, 22, 27] | Reproduced | — |
| 50 | 1035–1036 | 95th pct of 20 …; seeds 0–19 | null calibration | `run_ood_calibration.py` L61–62, `range(n_seeds)` | grep | Reproduced | — |
| 51 | 1037 | 16 neutral prompts × 256 greedy tokens | degeneracy probe | `src/mvm/ablate.py` `NEUTRAL_CORPUS` (16 sentences); `GEN_TOKENS = 256`; `do_sample=False` | grep | Reproduced | — |
| 52 | 1038–1039 | four decimal places | control-arm Δnll reproduced across runs (+0.1244) | `removal-test-findings.md` instrument note 1 | read | Not reproducible | Matches the findings. The calibration's 4-decimal value is only in the gitignored `ood_calibration.json` (prelock shows +0.124) |
| 53 | 1040 | \|Δ\| = 0.008 | repeat-run judge drift | `prelock-findings.md` §c (0.6417 / 0.6333) | 0.6417 − 0.6333 = 0.0084 | Reproduced (arithmetic) | The judge outputs themselves are not committed |
| 54 | 1042 | ≥30 items per subset; S 30 items | pilot battery sizes | `src/batteries/*.jsonl` | counts 32/30/30/30 | Reproduced | — |
| 55 | 1042 | T_si "eight categories" | number of T_si categories | `task_battery.jsonl`, `test_task_battery.jsonl`, `test-set-authoring-spec.md` | Python Counter by category | Differs | 4 categories × 8 items |
| 56 | 1046 | 122 items | held-out items authored | `cf06b49` battery files | `git show cf06b49:…` line counts: 32 + 30 + 30 + 30 | Reproduced | The commit message also says 122 |
| 57 | 1048–1049 | 92/92 final; baseline 1.000 | held-out T items passing baseline | final `test_*` files (32 + 30 + 30 = 92); `removal-test-findings.md` | counts; read | Not reproducible | The item count reproduces. The baseline accuracy needs an 8B generation run (part of about 0.5 GPU-h) |
| 58 | 1055 | 0.6375 (pilot and held-out) | baseline judged self-report | `prelock-findings.md` (mean of two passes), `removal-test-findings.md` | (0.6417 + 0.6333)/2 = 0.6375 | Not reproducible | Pilot value reproduced as arithmetic from the two committed passes. The held-out 0.6375 only matches the findings; judge scores are not committed |

Items in range with no number to check: Fig. 1(c) "four registered outcome bins" was checked against `pre-registration.md` (floor-consistent, floor-consistent restricted, description-only, inconclusive), so it is Reproduced but not counted in the table. Fig. 2a repeats rows 4–5; Fig. 3 "falls monotonically" is consistent with 0.533 > 0.333 > 0.267 > 0.100, but its "stable" ratios contradict L290 (Differs 6 in the summary, not repeated as a row). Judge model `claude-opus-4-8` (L1051) matches `judge.py` L41 `JUDGE_MODEL`.
