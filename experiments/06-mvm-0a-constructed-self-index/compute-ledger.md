# MVM-0a compute ledger

*The registered budget instrument. Cap: **$200 for the entire registered
design** (learnability pilots, 5 seeds × full+twin, ablation passes, θ/δ
null-calibration, blind-localization arm) — adjudicated 2026-08-07,
derivations in `registration-decision-memo.md` §1. Once the registration
lands, exceeding the cap is a protocol violation, not just an overspend:
work stops and any continuation is a registered amendment.*

## Rules

1. **Every pod session gets a row** — written in the same session the pod
   is deleted, with the estimate recorded *before* the run and the actual
   after. STATUS entries already carry per-session costs by habit; this
   table is the running total against the cap.
2. **Estimate before spend.** A run whose pre-run estimate would take the
   running total past $200 does not launch.
3. **Pods always launch with `--terminate-after`** (standing ops rule), so
   no single run can exceed its own estimate by more than the terminate
   window.
4. **Reconcile against RunPod's own billing** (console → Billing) at each
   phase boundary (pilot → training → ablation → localization); the
   ledger's total and RunPod's lifetime-spend-since-2026-08-07 should
   agree to within a dollar, and a disagreement is investigated, not
   averaged away.
5. The hard backstop is upstream of this file: **the RunPod account is
   funded by prepaid credits with auto-reload OFF**, topped up in
   increments John chooses, never past the cap's remainder. The account
   physically cannot overspend what the ledger permits.

## Reconciliation baseline

RunPod balance at adjudication (John, checked 2026-08-07): **$106.73**
(prior spend from $150 predates this cap — Experiment 1 / Stage 3 work;
this ledger starts at $0). Rule 4 reconciles against this number:
expected balance = $106.73 − ledger running total − storage drip since
this date. Auto-reload: **OFF** (John's setting; the Layer-3 backstop).

## Ledger

| date | phase | what ran | GPU | hrs (est → act) | $ est | $ actual | running total |
|---|---|---|---|---|---|---|---|
| 2026-08-07/08 | pilot | 10M learnability pilot, seed 0, code `e0bd13e`, 171.79M tok (20/param), held-out eval. Pod 1 `977cezdx6klgbt` (secure 4090, deleted before use — dead `sshCommand` field, pod was healthy); pod 2 `zv0nxkyazqfw0w` (community 5090, ran the pilot). **RESULT: LEARNS, all batteries ≥0.97** (`pilot-findings.md`) | 4090 $0.74 (12.6 min) + 5090 $0.69 community | 1–2.5 → 2.4 (+0.2 dead pod) | $1.50 (cap $2.96) | **$6.02** ⚠ | **$6.02 / $200** |

**⚠ 2026-08-08 reconciliation: PARTIAL FAIL — investigated, unresolved.**
Balance $106.73 → $99.93 agrees with RunPod's billing rows ($6.02 pods +
~$0.78 volume drip since Aug 6), so nothing is unaccounted. But the 5090
row itself bills **8.47 h against ~2.42 h of pod existence (~3.5×,
$5.86 vs ~$1.67 expected)**; nvidia-smi showed one GPU. Actual recorded
from the billing rows per rule 4 (their number, not ours). **Action
(John): RunPod support ticket before the 5-seed runs** — at 3.5× the
registered-run estimate inflates from ~$6–12 to ~$20–40. Still inside
the cap either way.

## Phase budget guide (from the decision memo, for estimates)

| phase | expected |
|---|---|
| Learnability pilots (10M → 30M → 100M as needed) | ~$1–15 |
| Registered training, 5 seeds × full+twin | ~$2 (10M) / ~$12 (30M) / ~$120 (100M) |
| Checkpoint ablation passes + RT-01 probes | ~$2–5 |
| θ/δ null-calibration runs | ~$2–5 |
| Blind-localization arm | ~$5 |
