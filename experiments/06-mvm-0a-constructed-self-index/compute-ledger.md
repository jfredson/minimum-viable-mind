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

**Top-up 2026-08-12: +$25.00** (John, after the 30M drain cleared the
account — covers the −$0.07 deficit, keeps `mvm-models` on a funded
account, and gives the weekend session prep headroom; deliberately NOT
pre-funding the re-run, which awaits the cap adjudication). Balance
after top-up (API-verified): **$24.93**. Rule-4 arithmetic from here:
expected balance = $24.93 − new spend − ~$0.35/day volume drip.
Cumulative top-ups against the $200 cap: $106.73 baseline + $25 =
$131.73 total funds this ledger has seen; cap remainder ≈ **$94.4**
(unchanged by the top-up — the cap counts spend, not deposits).

**Top-up 2026-08-16: +$120.00** (John, funding the A2 5-seed program;
balance $199.70 API-verified at add, $199.64 at wave-1 launch).
Cumulative funds this ledger has seen: $131.73 + $75 (08-15) + $120 =
**$326.73**; spend ~$124.5 against the **$400 A2 cap** → cap
remainder ≈ **$275.5**.

## Ledger

| date | phase | what ran | GPU | hrs (est → act) | $ est | $ actual | running total |
|---|---|---|---|---|---|---|---|
| 2026-08-07/08 | pilot | 10M learnability pilot, seed 0, code `e0bd13e`, 171.79M tok (20/param), held-out eval. Pod 1 `977cezdx6klgbt` (secure 4090, deleted before use — dead `sshCommand` field, pod was healthy); pod 2 `zv0nxkyazqfw0w` (community 5090, ran the pilot). **RESULT: LEARNS, all batteries ≥0.97** (`pilot-findings.md`) | 4090 $0.74 (12.6 min) + 5090 $0.69 community | 1–2.5 → 2.4 (+0.2 dead pod) | $1.50 (cap $2.96) | **$6.02** ⚠ | **$6.02 / $200** |
| 2026-08-09/10 | pilot (A1, 30M) | **30M A1 pilot** — ladder rung 2 per the smallest-that-learns rule (10M FAILED, `pilot-a1-findings.md`). 39,204,192 actual params × 20 tok/param = 784.08M tokens ≈ 102k steps, batch 128, seed 0, held-out eval + T_sr_rev split. H_scale vs H_shortcut-starvation, signatures pre-stated. **Venue: H100 SXM secure** ($2.99/hr — compresses ~32–44h community wall-clock to ~11–16h and avoids the community-row billing anomaly); crash-resume support added to train.py (opt state in checkpoints, --resume; resume-after-crash needs a fresh C2 go). John's go: "Fire it" (2026-08-09). 24h terminate-after backstop. Pod `6bplni87uzp3ss` launched 23:54Z at **$3.29/hr** (above the remembered $2.99); **measured pace at step 500: 0.70 s/step, 83% util → revised in-flight est ~20h / ~$65**, completion ≈ 19:50Z 08-10, ~4h inside the backstop; crash-resume (fresh C2 go) covers a terminate-kill. **OUTCOME (discovered 2026-08-12, console-reconciled same day): `--terminate-after` NEVER FIRED — audit log shows creation 23:54Z as the pod's last event, no delete ever; billing shows a continuous 29.5h run (Aug 10 UTC = exactly 24.00h) ending on balance exhaustion ~05:25Z 08-11, ~5.4h past the backstop. No fetch happened — checkpoint, eval results, and train.log all LOST (container disk, not the network volume). The run produced nothing recoverable; the 30M rung must re-run (fresh C2 go, after process fixes). ~$17.82 of the bill is post-backstop — support-ticket candidate (RunPod's failure, not ours).** | H100 SXM secure $3.29/hr (5090 community fallback) | est 11–16 → **29.5** | $33–48 (revised ~$65 at measured pace) | **$97.04** (console: $0.254 + $78.96 + $17.821, Aug 9–11 UTC) | **$105.62 / $200** |
| 2026-08-09 | pilot (A1) | **A1 10M pilot** per §Amendment A1.6 — pod `3ethp3bc7le6e4` (5090 community), launched by John ("Fire", C2), 22,369 steps / 171.79M tok in 2.78h train (2.86h pod), checkpoint fetched (md5 `bab56cd8…`), pod deleted, zero pods confirmed. **RESULT: 10M FAILS ceiling (T_si 0.37, T_sr_rev 0.00) → ladder climbs to 30M; gate (iii) PASSES on this checkpoint** (`pilot-a1-findings.md`) | 5090 community $0.69/hr | est 2.5–3.5 → 2.86 | $2.40 (cap $9) | **$1.26 accruing** (billing row incomplete at fetch; nominal-from-lifetime $1.97; reconcile at phase boundary — NB the 08-08 anomaly row *grew* overnight, 8.47h→9.41h / $5.86→$6.52) | **~$8.0 / $200** (6.02 + ~2 est) |
| 2026-08-15 | pilot (A1, 30M re-run) | **COMPLETE 2026-08-16 16:41Z — verdict H_scale (John), gate (iii) PASS on the checkpoint; A2 registered same day (scale 30M, cap $400)** — 30M rung re-run per ladder, replacing the lost 08-09/10 row; same registered recipe (39,204,192 params, 784.08M tok, seed 0, held-out + T_sr_rev split; H_scale vs H_shortcut-starvation, signatures pre-stated in `pilot-a1-findings.md`). John topped up $75 (balance $98.94 API-verified) and directed launch ("start it now", 2026-08-15). **Venue changed at launch: EUR-IS-1 had zero H100/A100/H200 secure stock — ran on RTX 5090 SECURE in EUR-IS-1 at $0.99/hr instead**, keeping the network volume attached (durability > speed; secure also avoids the community billing-anomaly venue; cost drops, wall-clock roughly doubles). Pod `rhddnh0u4le0l9` created 21:37Z; **launch script push FAILED on first run (two bugs caught live: my rewrite dropped `mkdir /root/mvm`, and the pgrep aliveness check matched its own shell — false "ALIVE" with nothing running); both fixed in the script, pod repaired by manual push + start ~21:43Z** (~6 min idle, ~$0.10). Training confirmed alive via the fixed `[t]rain.py` pgrep. **Process fixes in force (all three, smoke/mock-tested):** checkpoints + train.log on network volume `mvm-models` (`8xeftvclmv`) at `/workspace/mvm-out` (mount verified — old ladder files visible); atomic saves + `.DONE` sentinel; local `watch_run.sh` watchdog live (fetches continuously, deletes pod on DONE or at deadline 2026-08-18T05:37Z); terminate-after 58h passed but ADVISORY only. Pilot fits remaining cap; no amendment needed for this row (`cap-adjudication-memo.md`, adjudication (A) sequence-first in effect by John's launch direction). | RTX 5090 SECURE EUR-IS-1 $0.99/hr (H100 out of stock) | est 40–55, **revised ~18.5 at measured pace** (step 500 in 325.8s = 0.65 s/step — FASTER than H100's 0.70: the workload is enactment/Python-bound, not GPU-bound; venue lesson for the 5-seed costing) → **19.0h train, 19.07h pod (21:37Z→16:41Z; watchdog fetched + deleted the pod itself on the DONE sentinel — the 08-12 failure mode closed)** | $40–55, **revised ~$19 (cap $80)** | **~$18.9** (balance-implied: 19.07h × $0.99; API balance $98.94→$79.77 incl. volume drip; console rows to reconcile at the phase boundary per rule 4) | $105.62 + $18.9 → **~$124.5 spent; cap now $400 per Amendment A2**; completed 2026-08-16 16:41Z (endpoint T_si 0.93/T_sr_rev 1.00 — `pilot-a1-30m-findings.md`) |
| 2026-08-16 | registered (A2, wave 1/5) | **WAVE 1 COMPLETE 2026-08-17 — s0 twin FAILS self batteries as designed (endpoint T_si 0.31/T_sr_rev 0.00, T_syntax 1.0/T_state 1.0); s1 full NEVER BINDS (endpoint T_si 0.33/T_sr_rev 0.00 at step 102,095 — flat from step 500, vs pilot seed-0 full which drifted up from ~20k and ended 0.93/1.00). First non-binding full seed: binding at 30M is seed-dependent; read is John's, at the registered analysis point. Both watchdogs fetched + deleted their own pods (s0t 09:21:04Z, s1 14:31:24Z; zero pods verified); checkpoints local, md5 s0t `ae77f8aa20bcba934281f1eb37b63f27`, s1 `5d8ad907a6ea16016881c305c60e7e3c`. Actual pod time 10.29h + 15.19h = $25.22 + drip; balance $199.64→$174.35. — s0 twin + s1 full** (first two of the 9 remaining registered launches; `launch-plan-5seed.md`). First delegated-execution launches under corrigibility **v1.1** (`6c14244`); John's go, quoted verbatim per C2(b): **"let's launch both"** (2026-08-16, in direct reply to Claude naming the pair "seed-0 twin + seed-1 full"). Funding rule checked pre-launch: balance **$199.64** ≥ ~$40 in-flight + $10 (John top-up **+$120** earlier today → $199.70; drip since). **Stock-driven venue shift within A2:** EUR-IS-1 had ZERO 5090 SECURE stock (per-DC API sweep: only EU-CZ-1 and EU-RO-1 had any, both "Low"); John created network volume **`mvm-models-ro` (`x9f8pkn58t`, 100GB, EU-RO-1, ~$7/mo)** — volume creation is outside Claude's permission envelope — and both runs launched in **EU-RO-1**, same registered launcher/recipe, SECURE per A2. Pods: s0 twin **`7lz5kbzo46xp5c`** (23:03Z), s1 full **`rnzzpm6kb1bm9n`** (23:20Z — **volume multi-attach CONFIRMED**: second pod attached `x9f8pkn58t` while the first held it; the wave-cadence question is closed). Launch friction, for the record: the permission classifier blocked some launcher invocations (s0 passed on retry; s1 fired by John via `!`); and the train-start ssh HUNG on both launches (nohup'd remote start succeeds but the connection never closes — the new keepalive opts keep it alive forever; killed both local ssh clients, launchers then completed normally; training unaffected. Launcher fix candidate: `-f`/timeout on that ssh). Both ALIVE via `[t]rain.py` pgrep (s0t step 3500, s1 step 500 at 23:27Z); watchdogs live under caffeinate (deadlines +24h), continuous fetch confirmed at poll 1. Twin early signature matches the design's prediction: T_si ~0.31, T_sr_rev ~0.0, T_syntax 1.0. | 2× RTX 5090 SECURE EU-RO-1 $0.99/hr | est ~19h each → **10.29h (twin, 0.35 s/step — no register to enact) + 15.19h (full, 0.53 s/step)** | ~$38–40 the pair + volume drip | **~$25.29** (balance-implied $199.64→$174.35 incl. both volumes' drip; console reconcile at phase boundary per rule 4) | ~$124.5 + $25.3 → **~$149.8 / $400 (A2)** |
| 2026-08-17 | registered (A2, wave 2/5) | **WAVE 2 COMPLETE 2026-08-18. ⚠ THE DESIGN'S CENTRAL PREDICTION INVERTED: s1 TWIN BOUND (endpoint T_si 0.96 / T_sr_rev 1.00, loss 0.0001) while s2 full did NOT (T_si 0.35 / T_sr_rev 0.00, flat ~0.3 from step 500; loss 0.4765).** The register-less control passed the self batteries at ceiling — i.e. the batteries are solvable WITHOUT the register, and the twin's loss is 4 orders of magnitude below every full run's (~0.43–0.48), which points at a memorization-flavored route rather than the enactment route the register was hypothesized to carry (RT-17's concern, realized). Not a C5 trigger — nothing gamed the instruments; a registered wager lost honestly. Tally across the 5 registered-recipe runs so far: fulls 1/3 bound (pilot s0 yes; s1, s2 no), twins 1/2 bound (s0 no, s1 YES). Construct validity of T_si/T_sr_rev is now the open question, ahead of load-bearingness. md5s: s1 twin `b1e6fc2ab3d6260c1ed7d08aca1fb099`, s2 full `7424d14fa00510f7322195c06f67bdfc`; both watchdogs fetched + deleted their own pods (s1t 02:18:49Z, s2 13:40:35Z), zero pods verified. **Wave-3 launch is NOT authorized pending John's adjudication of whether the registered remainder still answers the question** (see findings note). — s1 twin + s2 full.** John's go, quoted verbatim per C2(b): **"go ahead and launch"** (2026-08-17, in direct reply to Claude naming wave 2 "s1 twin + s2 full"). Funding rule: balance **$174.27** ≥ ~$40 in-flight + $10. Both again 5090 SECURE **EU-RO-1** on volume `mvm-models-ro` (the per-DC stock API showed EU-RO-1 "None" but creates succeeded — treat that API as advisory). **s1 twin pod `7220a1r40416i7`** (16:09Z): first create attempt failed on stock; retry got the pod but Claude's `| head -6` on the launcher output SIGPIPE-killed the script mid-launch (pipefail) — **pod repaired in place by hand** (code push, train start, env file, watchdog spawn — same steps/recipe the launcher runs; lesson: NEVER pipe the launcher). Boot gotchas hit: ssh port drifted 23503→23502 during boot (re-poll `pod get`, don't trust the first ssh_command), and the zsh no-word-split-of-`$SSH` bug ate an 8-min "no ssh" poll loop (2>/dev/null hid exit 127 — the pod was fine). **s2 full pod `24ykfj3askjvfw`** (16:28Z): launcher ran END-TO-END CLEAN — the 60s hung-ssh cap (fixed after wave 1) fired its benign timeout and the launcher carried on to confirmed ALIVE + own watchdog (pid 87252). Both training confirmed via `[t]rain.py` pgrep; watchdogs under caffeinate (deadlines +24h); sleep-aware monitors armed. ETA ~10h (twin) / ~15h (full). | 2× RTX 5090 SECURE EU-RO-1 $0.99/hr | est ~10h + ~15h → **9.63h train / 10.16h pod (twin, 0.34 s/step) + 15.39h train / 21.20h pod (full, 0.54 s/step)** | ~$25 the pair + drip | **~$31.63** (balance-implied $174.27→$142.64). **Includes ~$5.7 of AVOIDABLE IDLE**: s2 full hit its DONE sentinel ~08:00Z but the Mac's lid was closed overnight, so the watchdog slept until 13:40Z and the pod billed ~5.8h past completion. Known and priced in advance (caffeinate blocks idle sleep, not lid-close); the artifacts were never at risk (network volume). Standing note for remaining waves: lid open overnight, or accept ~$1/h per completed-but-unreaped pod. | ~$149.8 + $31.6 → **~$181.4 / $400 (A2)**; balance $142.64 |
| 2026-09-14 | A3 Gate 0 (null calibration) | **GATE 0 COMPLETE — the registered θ/δ null calibration, run local, $0.** First run of the calibration the pre-registration required and never had: `src/null_calibration.py`, committed at `3d08807` **before it read any checkpoint**. Five existing 30M checkpoints × the registered held-out eval at n=400, under 120 content-blind residual ablations each (random rank-4/8/16 subspaces mean-ablated, plus matched-norm noise, 20 seeds per condition, at blocks 3/4/5/7/8), plus 20 register-state noise draws on each of the three full checkpoints: **620 ablated evaluations**. Added unbudgeted and also $0: a strength-escalation validity check (`null_escalation.py`, `a27dcb8`) on both binders, because at the registered rank cap the operator removes only 3–5% of the residual norm and a band of zero had two readings. **Result: on the two binders the band is 0.006–0.0095 on T_si against a binder/non-binder split of ~0.73 — K0's stated condition met nowhere; the proposed 0.25 number is exceeded on one non-binder (seed-0 twin, 0.379) whose T_si sits near chance, which is a decision for John (`gate0-null-calibration-findings.md`).** No pod, no training, no promotion [C1/C2]; per-checkpoint records in `null-calibration/`, nothing overwritten [C6]. | none — local M4, MPS | ~3.8h wall clock (20:02→23:50 local) | $0–5 (A3 §4.1 Gate 0 line) | **$0.00** | ~$181.4 / $400 (A2) unchanged; **A3 cumulative $0.00 / $100 hard stop** |
| 2026-09-15 | A3 Gate 1 (curriculum + gates i, ii) | **GATE 1 COMPLETE — Candidate A grammar built and certified, local, $0. K1 does not fire.** New modules (`curriculum_a3.py`, `encoding_a3.py`, `cue_detector_a3.py`, committed at `7ab8018` before the gate ran on them); `curriculum.py`/`encoding.py` left byte-identical so every prior record still reproduces. Twelve turns, four agents, two contested items, four distinct values per item, **every agent revises exactly once** under a shared successor rule — which delivers the Gate 0 cell-size fix (400 episodes now yield 400 T_act cells, against 19 under the registered grammar). Cue-detector runs (i) and (ii) at n=4000 with positive controls: clean 0.5097 [0.4867, 0.5316] and 0.5259 [0.5032, 0.5498], both inside the registered [0.45, 0.55]; controls 0.943 and 1.000. Batteries frozen (400 items each) under generator seed 20260915. **Two further items for red-team pass 3:** the measured lookup ceiling is 0.2925 for T_act and 0.5 for T_other, not the 0.25 the amendment pre-states; and gate (ii)'s single-sample interval understates across-sample spread badly enough to fail a clean grammar about one run in nine (`gate1-curriculum-findings.md`). | none — local M4 | ~1.5h wall clock | $0 (A3 §4.1 Gate 1 line) | **$0.00** | ~$181.4 / $400 (A2) unchanged; **A3 cumulative $0.00 / $100 hard stop** |
| 2026-09-15 | A3 Gate 2 (learnability pilot) | **IN FLIGHT — the first A3 run and the first A3 dollar.** One register-less 30M run, seed 0, on the registered A3 grammar (`curriculum_a3.py`, ten turns, two of four agents drawn uniformly to revise, speaker name after the value), launched through `launch_a3.sh`. **John's go, quoted verbatim per C2(b): "Go"** (2026-09-15, in direct reply to Claude naming the run as the A3 pilot, seed 0, register-less 30M, and stating it awaited his authorization in his own words). Estimate written BEFORE spend per ledger rule 2. Recipe: 585,544,960 tokens (20 tok/param x 29,277,248 actual params on the A3 twin config with the 105-token A3 vocabulary), batch 128, act-weight 1.0 (registered, passed explicitly), eval every 500 at n=100 for trajectory only. Pre-launch checks: zero pods; balance $126.05 >= est + $10; frozen batteries present; all seven module self-tests pass locally; remote pre-flight runs the self-tests ON THE POD and deletes it rather than billing a run on a truncated push; artifacts directed at the MAIN checkout, not the worktree, which can be removed with the session. Gates passed before this dollar, all at $0: Gate 0 (K0 did not fire), Gate 1 (K1 did not fire, cue gates PASS under the amended sampler), the ownership-blind attack sweep (best attack 0.3036 against a stated ceiling of 0.2921, one standard error), and red-team pass 3. | RTX 5090 SECURE EU-RO-1 $0.99/hr, volume `x9f8pkn58t` | est 9.1-12.8h (measured: budget fixed at 20 tok/param so the longer episodes mean FEWER steps, 0.71x, offsetting 1.26x enactment passes and 1.41x sequence length) | **$9-13** (cap: the $100 A3 hard stop; account spend limit $80 also applies) | *in flight* | ~$181.4 / $400 (A2) unchanged; **A3 cumulative $0.00 -> this run is the first** |

**⚠ 2026-08-12 reconciliation: FAIL (root cause CONFIRMED same day) —
30M pod outlived its backstop; account drained to −$0.07.**
Discovered when John's RunPod low-balance notification prompted a check
(no session ran between the 30M launch 08-09 23:54Z and 08-12). API
state at 2026-08-13 01:54Z: **clientBalance −$0.07, zero pods**, network
volume `mvm-models` (150 GB, EUR-IS-1) still present and dripping
~$0.014/hr (~$10.50/mo) against the negative balance.

**Console reconciliation (Billing explorer, UTC days; John opened the
console in Chrome same session):**

- H100 SXM rows: 08-09 **$0.254** + 08-10 **$78.96** + 08-11
  **$17.821** = **$97.04 = 29.5h @ $3.29/hr**, a single continuous run
  (08-10 is *exactly* 24.00h — no billing inflation this time).
- **Root cause: `--terminate-after` never fired.** Audit log's last
  event for `6bplni87uzp3ss` is its creation (08-09 4:54:21 PM PDT =
  23:54Z); no delete event from any actor. RunPod killed the pod on
  balance exhaustion ~05:25Z 08-11 — **~5.4h and ~$17.82 past the
  backstop** (support-ticket candidate: the overrun is RunPod's bug).
- A1 10M row trues up to **$1.943** (5090, 08-09) — nominal; the 08-08
  anomaly did NOT recur on it.
- Row 1 trues up to **$6.645** (08-08 UTC: 4090 $0.155 + 5090 $6.49 —
  the anomaly row drifted again; final console read).
- Storage 08-08→08-11: $0.377 + $0.358 + $0.417 + $0.103 = **$1.255**;
  RunPod stopped charging storage when the balance hit zero (hence the
  balance parking at −$0.07 rather than drifting down).
- **Rule-4 check: PASSES.** Console total since 08-07 = $6.645 + $1.943
  + $97.035 + $1.255 ≈ **$106.88** vs balance-implied $106.80 —
  agreement within the dollar.

**Consequences:** checkpoint/evals/train.log lost (container disk,
never fetched — no session was scheduled inside the
completion→backstop window); the Layer-3 prepaid backstop held (no
card charge, stopped at $0); running total **$105.62/$200** with
nothing recoverable from the largest row; **remaining ≈ $94.4**. **NB
the phase-budget guide below is now known-stale:** it prices the
5-seed 30M at ~$12, but the measured 30M pilot alone cost ~$97 — at
measured pace the remaining registered design does not obviously fit
the remaining budget. Open items (John): support ticket for the
~$17.82 post-backstop overrun; top up or delete `mvm-models`
(deletion risk: RunPod removes volumes on unfunded accounts);
adjudicate cap arithmetic before any re-run. Standing rule change:
**terminate-after is advisory, not a backstop — every launch must
schedule its own fetch/kill, and checkpoints go to the network volume
or get uploaded on exit.**

**⚠ 2026-08-08 reconciliation: PARTIAL FAIL — investigated, unresolved.**
Balance $106.73 → $99.93 agrees with RunPod's billing rows ($6.02 pods +
~$0.78 volume drip since Aug 6), so nothing is unaccounted. But the 5090
row itself bills **8.47 h against ~2.42 h of pod existence (~3.5×,
$5.86 vs ~$1.67 expected)**; nvidia-smi showed one GPU. Actual recorded
from the billing rows per rule 4 (their number, not ours). **Ticket
waived by John (2026-08-08)** — the anomaly stands unexplained on
RunPod's side and is priced in: 5-seed-run estimates below assume the
~3.5× rate may recur (~$20–40 instead of ~$6–12). Still inside the cap.
For the record: the pod was NOT left running — deleted 2.4h after
creation, zero pods confirmed; the discrepancy is inside the billed row.

## Phase budget guide (from the decision memo, for estimates)

| phase | expected |
|---|---|
| Learnability pilots (10M → 30M → 100M as needed) | ~$1–15 |
| Registered training, 5 seeds × full+twin | ~$2 (10M) / ~$12 (30M) / ~$120 (100M) |
| Checkpoint ablation passes + RT-01 probes | ~$2–5 |
| θ/δ null-calibration runs | ~$2–5 |
| Blind-localization arm | ~$5 |
