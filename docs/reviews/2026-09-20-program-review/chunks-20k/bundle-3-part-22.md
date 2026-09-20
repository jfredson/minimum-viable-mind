| 2026-09-19 | control-learnability pilot (UNREGISTERED) | **LAUNCHED 2026-09-19. John's go, quoted verbatim per C2(b): "Go. Launch the control-learnability pilot as staged: one 30M register-less run, seed 0, --ctl-weight 2.0 --ctl-frac 0.5, through launch_ctl_pilot.sh, ~$10.2. Weight and batch-split stay as you set them. Confirm zero pods and EU-RO-1 stock right before creation, and keep the flag out of launch_a3.sh."** Given in direct reply to Claude staging the run, naming it, stating the estimate, and stating that nothing was launched pending a fresh verbatim line. **Both final checks done immediately before creation and recorded here: zero pods (`runpodctl pod list` returned an empty list), and RTX 5090 SECURE stock present in the registered venue at $0.99/hr — the registered rate, not an elevated one.** The flag was kept out of `launch_a3.sh`, which is untouched registered text. **Pod `kdvdsomkf3u6va` created 2026-09-19 ~20:14Z at $0.99/hr (confirmed from the pod record, not assumed); LAUNCH CLEAN END TO END** — remote pre-flight passed all three self-tests **on the pod** before a training step (`curriculum_a3`, `encoding_a3`, `train_a3`, the last exercising the new flag's code path on the rented machine), training confirmed by the `[t]rain_a3.py` aliveness check rather than by the launcher's exit status, watchdog spawned under `caffeinate` (pid 54548) and already fetching. **FIRST PRODUCTION ARMING OF THE POD-SIDE REAPER, and it VERIFIED:** the dedicated reaper key reached pod management as the pod itself, and a laptop-independent +24h deadline reaper is running on the machine. That backstop was built after the third idle-billing occurrence and had never actually run in production; the laptop watchdog remains the primary reap and **the lid must still be open**, because `caffeinate` blocks idle sleep and not lid-close. One 30M **register-less** run, **seed 0**, with the unregistered control-learnability flag: the control battery gets a loss term of its own (`--ctl-weight 2.0 --ctl-frac 0.5`) instead of about a third of a shared one. **Seed 0 on purpose**, so the comparison against the existing A3 pilot is matched on initialization and data order and the loss is the only thing that differs. **The question:** does the control learn when properly supervised, or is supervision not the binding constraint? Three seeds have now failed it identically (0.2877, 0.3057, 0.3195, all under the 0.3227 reached by a solver that cannot read the name the question supplies), and the under-supervision reading has never been separated from the design-defeats-it reading. **Outcome cells pre-stated by John BEFORE the code existed** (`control-learnability-pilot.md`, committed `7eee3c5` ahead of the implementation): control intact **≥ 0.60 LEARNED**; **0.3227 to 0.60 PARTIAL**; **≤ 0.3227 DID NOT LEARN**, and option D or closing A3 is what is left. Secondary cells, reported with it and never instead of it: the primary battery must still learn (intact ≥ 0.50) and must still collapse under its own lesion, or the run is reported as a failed intervention and says nothing about the control. **Recipe identical to the 2026-09-15 A3 pilot** and unchanged by the flag: 585,544,960 tokens, 55,116 steps, batch 128, act-weight 1.0, eval every 500 at n=100 for trajectory only. **No grammar change** — the grammar, tokenizer, frozen batteries, rendering, ceilings and attack sweep are untouched; only the apportioning of the loss across queries the episode already carries moves. **Nothing registered.** No registered verdict is read from this run and John's threshold lock is not touched. The loss change (`ee7fc91`) defaults to OFF and the self-test proves the off path is bit-identical to the pre-flag pooled term rather than asserting it. **Launcher: `src/launch_ctl_pilot.sh`, a separate unregistered file.** `launch_a3.sh` is registered text and has no hook for an extra training argument, so it was NOT edited — the repo's own precedent (launch_a3.sh was split from launch_pilot_a1.sh for exactly this reason). Derived verbatim; the diff is the two flags, a distinct output name that cannot overwrite the existing pilot, and a refusal to launch at ctl-weight zero. **Dry run clean**; all three module self-tests pass locally and the remote pre-flight runs them on the pod and deletes it rather than billing a run on a truncated push. **PRE-LAUNCH CHECKS — two done, two outstanding.** DONE: **zero pods confirmed** at staging time; and the **Mac's sleep override is already back ON** (`SleepDisabled 1`, measured at staging), so the reversion recorded in the annotation below has since been undone by somebody — but the laptop watchdog is still the only reap that has ever worked in production, idle billing has cost about $10.30 across four occurrences, and **the lid must be open** regardless of the setting, because `caffeinate` blocks idle sleep and not lid-close. OUTSTANDING: (ii) confirm the balance covers the estimate plus $10 (about $23) by a route other than the stored key, which returned HTTP 403 during the last wave; (iii) confirm 5090 secure stock in EU-RO-1 at launch time. **Re-confirm zero pods immediately before creating one**, since the staging check ages. **Volume `x9f8pkn58t` (`mvm-models-ro`, EU-RO-1) is the right one and is untouched** — the volume deleted on 2026-09-19 was the old `mvm-models` (`8xeftvclmv`), see the annotation below. | RTX 5090 SECURE EU-RO-1 $0.99/hr, volume `x9f8pkn58t` | **est 9.87h training / ~10.2h pod**, computed from the pilot's **measured 0.645 s/step** × 55,116 steps; step count and token budget are unchanged because the grammar is unchanged. The one thing that could move the pace is that control questions render at a slightly different length from state and syntax ones, so padded batches may differ by a few percent — **MEASURED PACE, step 500: 325.4s (0.6508 s/step); step 1000: 651.5s (0.6515 s/step).** Against the A3 pilot on the same seed and the same recipe, 324.9s and 646.7s — **within about 0.7%**, so the padding effect I flagged is real and negligible. **Estimate CONFIRMED, not revised: 9.97h training, ~10.3–10.5h pod, $10.17–10.37**, inside the $9–13 band. | **$10.2, band $9–13** | — (nothing spent; not launched) | **⚠ READING NOTE, so the two trajectories are not misread side by side: THE LOSS NUMBERS ARE NOT COMPARABLE ACROSS THE TWO RUNS, BY CONSTRUCTION.** The pilot's query loss is one pooled mean; this run's is `other-term + 2 × control-term`, each normalised over its own subset of rows, so it sits on a different scale arithmetically and not because training is going worse. At step 500 the pilot reads q_loss 1.075 and this run 3.433, which is about what `1.1 + 2 × 1.15` gives. Anyone comparing the raw loss curves without this will conclude the run is diverging when it is not. **Trajectory accuracies at steps 500/1000 (n=100, TRAJECTORY ONLY — not the registered endpoint evaluation, and NOT the number the pre-stated cells are read on):** this run T_act 0.48/0.48, T_other 0.28/0.27, T_state 0.58/0.57, T_syntax 1.00/1.00; the pilot at the same steps T_act 0.54/0.52, T_other 0.24/0.18, T_state 0.66/0.64, T_syntax 1.00/1.00. **Nothing is read from this.** It is 1.8% of training at a sample size whose noise is large, the pilot's own trajectory wandered (T_act 0.54 → 0.52 → 0.50 → 0.64 over the first 2,000 steps), and **the pre-stated cells are read on the control's intact score at the n=800 endpoint evaluation, not here.** Recorded now only because it was measured now, and because a number that is written down before the end cannot be quietly reinterpreted after it. The one thing genuinely worth watching is the state battery, which is the coupling the pre-statement flagged: it drops from about a third of the rows to about a quarter, and it currently sits below the pilot at the same step. **OUTCOME 2026-09-20. THE RUN COMPLETED ITS FULL BUDGET, AND THE FINAL CHECKPOINT WAS NOT FETCHED. Both halves matter.** Pod `kdvdsomkf3u6va` ran 20:14Z → ~06:15Z, about **10.0h ≈ $9.9**, inside the $9–13 estimate, with **ZERO idle billing — the first run in the programme's history with none.** **What we hold locally is step 51,500 of 55,116 (93.4% of budget)**, the last incremental pull, archive-fetched and checksum-VERIFIED at 05:40Z. The trajectory record is complete to step 54,500 (109 evaluations). **The final full-budget checkpoint is on the network volume `x9f8pkn58t`, and it is there by proof rather than by hope:** `train_a3.self_terminate` REFUSES to delete the pod unless the output path is on `/workspace/` and the file exists — a hard gate added after the 2026-08-12 loss — and it runs only after the checkpoint and the DONE sentinel are written. The pod did delete itself, so both conditions were true at that moment. **ROOT CAUSE, and it is new: the trainer's self-terminate RACED the watchdog's fetch interval.** The watchdog polls about every ten minutes and is the thing that performs the final fetch-and-delete on the DONE sentinel; the trainer finished between poll 57 (06:11:12Z) and the next poll, wrote its checkpoint, and deleted its own pod before the watchdog could come back for it. The watchdog's log simply stops at poll 57, with no DONE, no final fetch and no delete — because there was no longer a pod to reach. **Two reaping mechanisms, built a month apart for the same problem, now defeat each other.** Self-termination was added after idle billing cost about $9.50 across three occurrences, and it worked perfectly here — that is exactly why there was no idle charge. The watchdog's final fetch was built for the same reason and now never gets to run on a completing run. **This will recur on every future run that finishes normally**, and it is a process defect, not bad luck. **NOT a balance problem:** the account holds **$79.89** and was never near exhaustion, so this is not a repeat of 2026-08-12. **RECOVERY, not yet done and not yet authorised:** mount `x9f8pkn58t` on the cheapest available pod, copy the file, delete the pod. Minutes, well under a dollar, and it needs John's go like any billable action. Until then the full-budget endpoint reading does not exist. **RECOVERED 2026-09-20 and the row is closed.** The DONE sentinel reads `{"step": 55116, "tokens": 585552384}` — the full registered budget, identical to the pilot and seeds 1 and 2 — and the checkpoint came back intact, md5 `a0c1c73af9c9bd5c60fb0e4e146180eb` verified against the volume before the recovery pod was deleted. **The root cause is confirmed in the trainer's own log rather than reconstructed**: `TRAINING COMPLETE` followed on the very next line by `self-terminate: runpodctl remove pod kdvdsomkf3u6va -> rc=0 pod removed`. **Endpoint on the full checkpoint: the control battery reads 0.3125 (sd 0.0240) — DID NOT LEARN**, with both secondary cells passing. Full reading in `control-learnability-pilot-findings.md`. The partial step-51,500 checkpoint and its reading are kept alongside so the earlier number stays reproducible. **ACTUAL ~$9.9 → A3 cumulative ~$44.2 / $100**, leaving ~$55.8 (was: would become ~$44.5), leaving ~$55.5. Also ~$215.7 / $400 on the wider envelope, and under the $80 account limit. *(Counting an unregistered diagnostic against the A3 hard stop is the conservative reading and is Claude's call; K6 speaks of cumulative actual spend, and a diagnostic run inside experiment 06 is most honestly counted there.)* |
| 2026-09-20 | checkpoint recovery (UNREGISTERED) | **RECOVERY OF THE CONTROL-LEARNABILITY PILOT'S FINAL CHECKPOINT.** John's go, quoted verbatim per C2(b): **"Go, recover the checkpoint, and kill the watchdog."** The 2026-09-19 pilot completed its full 55,116-step budget but the trainer self-terminated its pod between watchdog polls, so the watchdog never performed its final fetch and the local copy stopped at step 51,500 (93.4%). The full-budget checkpoint is on network volume `x9f8pkn58t` — by proof, not hope: `self_terminate` refuses to delete a pod unless the output is on `/workspace/` and the file exists, and it runs only after the checkpoint and DONE sentinel are written. **What runs:** cheapest available secure pod in EU-RO-1 with that volume mounted (network volumes are secure-cloud only), copy the checkpoint and the DONE sentinel and the final training log, **verify by md5 against the volume before deleting**, delete the pod, confirm zero pods. No training, no GPU work — this is a file copy. **Why it matters beyond tidiness:** the partial checkpoint reads the control battery at 0.3158 (sd 0.0204), which straddles the 0.3227 cell boundary at 0.34 sd below it, so the partial checkpoint cannot score John's pre-stated cell. The full-budget checkpoint is the one the cells are read on. **The watchdog was also killed** on the same instruction — it had been spinning against a deleted pod for over ten hours and holding `caffeinate`, keeping the Mac awake for no reason. | cheapest secure EU-RO-1 (A40 $0.49/hr or RTX 3090 $0.50/hr), volume `x9f8pkn58t` | **~5 min**, A40 secure EU-RO-1 | **<$0.15** | **$0.067** (balance $79.8897 → $79.8228, measured not inferred) | A3 cumulative ~$44.2 / $100 before this; a recovery of this size does not move the figure materially and the row is closed with the actual once measured. |

**ANNOTATION 2026-09-19 — storage volume deleted, and the sleep setting
reverted. Nothing in the table above is edited; this records two ops
actions taken after the rows were written.**

- **Network volume `mvm-models` (the 150 GB EUR-IS-1 volume,
  `8xeftvclmv`) was DELETED by John on 2026-09-19**, and only after both
  seed checkpoints had been verified against the checksums this ledger
  records: seed 1 `eeed93b80a7c8d81ba56d1ec6254af41` and seed 2
  `f1f131cb78f27c57194bedd127fd4031`, both 351,526,119 bytes, both
  re-checked locally after the pods were gone. The order matters and is
  the point: **nothing was deleted until the artifacts it might have
  held were proven to exist elsewhere, by checksum rather than by file
  size or by eye.** The volume was a leftover from the 2026-08 A1 30M
  era, had held nothing needed since, and had been dripping about
  $0.014/hr (roughly $10.50/mo) against the account since 2026-08-12 —
  the open item this ledger recorded then ("top up or delete
  `mvm-models`") is now closed by deletion. **The A3 volume
  `mvm-models-ro` (`x9f8pkn58t`, EU-RO-1) is untouched and still in
  use**; do not confuse the two.
- **The Mac's sleep setting was REVERTED the same day**, back to normal
  with `sudo pmset -a disablesleep 0`. Lid sleep had been disabled
  (`SleepDisabled 1`) while the seeds wave was in flight, because the
  laptop watchdog is the only thing that reaps a finished pod and a
  sleeping laptop bills a finished run at about $1/hr. With no pods
  rented and nothing in flight, the setting has no job to do and leaving
  it on would quietly cost battery for a reason nobody would remember.
  **If a future wave launches, it must be set again** — the standing
  warning in the 2026-09-17 row still holds, and idle billing has now
  cost roughly $10.30 across four occurrences.

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


===== FILE: research/removal-test-vs-the-field-research-note.md =====

# The Removal Test Against the Field

*Research note — June 23, 2026. Bridges `research/minimum-viable-consciousness-literature-vs-our-writing.md` (where the field puts the floor) to `experiments/01-self-indexing-removal-test/pre-registration.md` (the test we actually run). The question it answers: given that our floor sits in an unusual place on the field's spectrum, what does Experiment 1 adjudicate — for us, and for everyone else?*

---

## 1. Why this note exists

