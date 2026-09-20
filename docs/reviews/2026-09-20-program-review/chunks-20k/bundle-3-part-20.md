into the matched episode in which it is another, and seeing whether the
action follows.

**Causal patching has not been run anywhere in this sequence.** Not in the
denoising diagnostic, not in either position sweep, not in the powered
anchor test. Every result under review comes from the probe leg alone.

Checked rather than assumed: across all six code files the packet lists
there is no patching, swapping, ablating or intervening of any kind. Every
place the word "patched" appears is a read-only capture hook — it calls
the block's own forward, records what comes out, and returns it unchanged
— and the one place attention is recomputed says in its own method file
that the model's output path is left untouched. Nothing in this sequence
changes a model's computation and then looks at what the model does.

Two things follow, and the second is the one that matters.

The run is unregistered and says so on every page, so it is not bound by
the registered bin logic and I am not claiming it breached anything. But
the registered vocabulary for "one instrument looked and found nothing" is
**not testable (localization)** — an explicit refusal to read the result
either way. The sequence has instead written "closed". The registration
had already decided that a single-instrument null does not close anything,
and it decided that before any of this ran.

And it compounds the main review's finding RT-33 rather than duplicating
it. RT-33 says one instrument was used where two ordinary linear readers
were available and they disagree sharply. This says that even the intended
*second* method — the causal one, which is the stronger evidence and which
no rescaling argument can touch — was never applied. So "the linear-read
line is closed" rests on one leg of a two-legged registered procedure,
using the weaker of two available versions of that leg.

## RT-50 — the registration reads this pattern as instrument failure

**Serious. MEASURED.**

The situation on the pilot is: ownership is *known* to be load-bearing,
because zeroing the acting channel takes the ownership battery from 0.506
to 0.182, and the localization instruments cannot find it. The
registration says in two places what that combination means.

The pre-registration, at procedure step 8, on running the localization
pipeline against a centre known to exist:

> if the instruments cannot recover a center that is known to be there,
> **Experiment 1's null was instrument failure.**

And Amendment A3's own red team, at R7, on exactly the outcome that has
now occurred:

> Ownership is load-bearing (L0 collapses T_act) and no subspace at k ≤ 16
> beats the controls… If Experiment 1's pipeline cannot carve it, the
> honest reading of Experiment 1's null shifts toward **instrument
> failure**, which is the single finding RT-12 said might outweigh the
> headline.

The registered bin for the outcome, H_diffuse, is named "present but
uncarvable", and its registered reading is: "self-location is present in
the doing and not carvable by these instruments at this rank." Every one
of those sentences puts the weight on the instruments. None of them
licenses a statement about what the model does or does not carry.

The interpretation under review points the other way. It reads the
instruments as sound ("the instrument demonstrably works", "the instrument
is not in question") and the episode as empty. It reaches that by treating
the positive control as a warrant for the read's general sensitivity —
which the main review's finding RT-33 shows, from this stack's own
committed records, that it is not.

So the registered framework and the measured evidence agree with each
other and disagree with the sequence's headline. The registration
anticipated this exact pattern, wrote down that it points at the
instruments, and flagged it as possibly the most valuable thing the
program could find. The sequence has arrived there and described it as the
opposite.

I want to be careful about one thing. This does **not** mean the result
should be written up as instrument failure either. The honest position is
the registered one: with one of two methods run, in its weaker form, a
null is *not testable* for localization, and the open question is whether
the instrument or the model is responsible. The measurement that separates
those two is the same one the main review already named — the fitted
classifier at all eleven positions — with causal patching behind it.

## RT-51 — the reviewer's own error

**Worth-noting.** Recorded because a review that suppressed it would be
worth less than one that did not. I read eight of the ten document sources
the packet listed, misattributed the omission to the packet's do-not-open
line, and filed. The two I skipped strengthen the review's conclusion, so
nothing in the filed findings is softened by the correction — but that is
luck, not method, and the filed review's account of what was opened should
be read together with this file rather than on its own.

## What this changes in part 4

The replacement sentence offered in the main review still stands, and one
clause should be added to it. After "a fitted linear classifier was never
run at any of these positions against a well-posed target", add:

> …and neither was causal patching, which the registration requires
> alongside the probe before anything counts as localized.

With that, the status file says what happened: one leg of a two-leg
procedure, in its weaker form, found nothing at eleven positions, at the
registered target, with working controls at the one position where the
answer is the input token.


===== FILE: experiments/06-mvm-0a-constructed-self-index/compute-ledger.md =====

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
