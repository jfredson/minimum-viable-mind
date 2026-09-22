# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 19 of 20: The A4 review finding, and the compute ledger

*This is file 19 of 20 of one review packet, pasted into a single
conversation. It contains the independent review of a later draft clause - the
finding the text cites; the compute ledger - its rules, its baseline and the
two rows the text cites. Reply with one short line saying you have it, and
wait for the rest: the brief you are answering is in file 1, and your review
comes only after file 20 arrives. If this file looks cut short, say so now.*

---

===== RECORD 21 of 23 - the independent review of a later draft clause - the finding the text cites - EXCERPT: experiments/06-mvm-0a-constructed-self-index/red-team-a4.md =====

*Source note: excerpted from `experiments/06-mvm-0a-constructed-self-
index/red-team-a4.md` (47,208 characters in full), twenty-two findings from a
separate isolated session on 2026-09-19 on a later draft clause. Reproduced
here: that review's front matter, its summary row for the one finding the text
under review cites (its seventeenth, labelled F17 there) and that finding in
full. The other twenty-one findings are left out.*

**This is an excerpt, not a whole file.** The source is
`experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`, about 47,000
characters: twenty-two findings from a separate Claude Code session in its own
worktree on 2026-09-19, reviewing a later draft clause. The text under review
cites one of them, its seventeenth, labelled F17 there — for the claim that the
validity gates have no code written for this design and were never applied to
any lesion on any seed. What follows is that review's front matter (so you can
see what the reviewer was and was not given), its summary-table row for that
finding, and the finding in full. Quoted unedited.

# Red-team pass on the Amendment A4 clause — §5 of the control-clause proposal, read as registerable text

*2026-09-19. Target: §5 of `docs/control-clause-proposal-2026-09-19.md`
(the 2026-09-19 control-clause proposal, at commit `df039ca`), which is
the text the proposal says can be lifted into `amendment-a4.md` and
registered. Read against Amendment A3 as registered
(`amendment-a3.md`), the ceiling measurement of 2026-09-17
(`ceiling-measurement-findings.md`), the code the clause would run on
(`src/curriculum_a3.py`, `src/train_a3.py`, `src/endpoint_a3.py`,
`src/null_calibration.py`, `src/null_calibration_a3.py`,
`src/lock_guard.py`, `src/encoding.py`, `src/encoding_a3.py`,
`src/model.py`) and the committed records those scripts produced.*

*Brief this pass was fired under: John has ruled for Candidate B with
three fresh seeds (3, 4 and 5), the partial-damage ladder reported but
not binding, the registration commit before launch and the threshold
lock before any endpoint is read. This pass takes those rulings as fixed
and does not argue A against B. It was asked to find every way the
clause, its baselines and its threshold calibration could (a) be
satisfied by a model with no ownership-specific structure, (b) be fitted
to seeds 0 to 2 despite the exclusion, (c) produce a verdict that later
gets over-read, or (d) fail to produce any verdict on seeds 3 to 5, and
to give a short kill case whether or not it would ship.*

*Independence. When this pass read the proposal, the copy on disk
already carried John's ruling annotation, which mentions an amendment
draft (`amendment-a4.md`), a first red-team pass on it
(`a4-red-team-pass-1.md`, fifteen items) and a scoring script
(`src/separation_a4.py`), all uncommitted in the shared checkout.
**None of those three files was opened.** Every finding below was
reached from §5 as written, the registered A3 text, the code and the
committed records. Where the annotation itself disclosed one of the
other pass's conclusions (the within-run baseline being wrong, the
threshold landing near 2, a denominator that can degenerate), this pass
says so at the finding. Reconciling the two passes is a separate job,
and this file does not take ledger numbers (the running RT-nn series in
`red_team_ledger.md`) so that the reconciliation can assign them without
collision; findings here are labelled F1 to F22.*

*What this pass did and did not do. Every finding is marked **MEASURED**
(a static check was run and its output is reported: a tokenizer
comparison, a checkpoint configuration read, a record inspection, a
search of the source) or **ARGUED** (reasoning from the documents and
the code, which a reader can dispute). **No model was run. The
separation statistic was not computed on any checkpoint**, including
seeds 0, 1 and 2, in keeping with the discipline commitment in §5.5;
where a number below concerns those seeds it is quoted from a record
already committed, or is a bound derived from such quotes. Nothing was
spent.*

*House rule this document is written under: the workspace plain-language
rule (`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30). Short labels are
kept where they make a claim checkable and every one carries a phrase
saying what it is.*

---


*The summary-table row for this finding, as that review's summary has it:*

| ID | Finding | Brief question | Severity |
|---|---|---|---|
| F17 | Condition (f)'s validity gates have no A3 implementation and were never applied to the input-channel lesion on any seed; applied for the first time on the fresh seeds they may void every verdict, and not applied they are decorative | (d) | serious |

*The finding in full:*

### F17 — Condition (f)'s validity gates have never been applied to this lesion and have no A3 implementation

**Severity: serious. MEASURED.**

(f) carries over "verbatim from Amendment A3 §3.3" the neutral-episode
likelihood bound, the long-generation degeneracy probe and the
out-of-distribution-inconclusive branch. A search of `src/` finds no
neutral-episode likelihood bound and no degeneracy probe implemented
for the A3 grammar (the only "degenerate" checks are the zero-spread
guards in the control diagnostic and the blind control). The endpoint
records for seeds 0 to 2 carry no such field among their 110 keys. So
the input-channel lesion has never been tested against these gates on
any seed. Zeroing an input the model was trained with moves every
battery (F2, F5), so it is plausible it also moves the neutral-episode
likelihood past a 95th-percentile random-damage bound. If (f) is built
and applied on the fresh seeds, all three may return NOT TESTABLE on
the first application of a gate that was never run on the seen seeds;
if it is not built, (f) is a sentence. Either the gates are implemented
and run on the seen seeds before registration, with the result
reported, or (f) should say what it actually binds.

===== END OF RECORD 21 =====

===== RECORD 22 of 23 - the compute ledger - its rules, its baseline and the two rows the text cites - EXCERPT: experiments/06-mvm-0a-constructed-self-index/compute-ledger.md =====

*Source note: excerpted from `experiments/06-mvm-0a-constructed-self-
index/compute-ledger.md` (48,352 characters in full), which carries a row for
every rented-machine session since 2026-08-07. Reproduced here: the ledger's
opening, its rules, its reconciliation baseline, its column headings and the
two rows dated 2026-09-19 and 2026-09-20 in full. The other rows are left out,
so the two cited rows can be checked but the running total cannot be re-added
from the beginning.*

**This is an excerpt, not a whole file.** The source is
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, about 49,000
characters: a row for every rented-machine session the programme has run since
2026-08-07. The text under review cites it once, for two money figures — that
Amendment A3 closed at about $44.3 of its $100 hard stop and the programme at
about $225.7 of its $400 ceiling — and names the rows those figures sit on. What
follows is the ledger's opening, its rules, its reconciliation baseline (which
is where the $200 figure in the opening paragraph becomes the $400 one the text
cites), its column headings, and the two rows dated 2026-09-19 and 2026-09-20 in
full. The other rows are not reproduced, so you can check that the two cited
rows say what the sentence says but cannot re-add the running total from the
beginning. Quoted unedited.

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
| … | … | *(the rows dated 2026-08-07 to 2026-09-18 are not reproduced in this excerpt)* | … | … | … | … | … |
| 2026-09-19 | control-learnability pilot (UNREGISTERED) | **LAUNCHED 2026-09-19. John's go, quoted verbatim per C2(b): "Go. Launch the control-learnability pilot as staged: one 30M register-less run, seed 0, --ctl-weight 2.0 --ctl-frac 0.5, through launch_ctl_pilot.sh, ~$10.2. Weight and batch-split stay as you set them. Confirm zero pods and EU-RO-1 stock right before creation, and keep the flag out of launch_a3.sh."** Given in direct reply to Claude staging the run, naming it, stating the estimate, and stating that nothing was launched pending a fresh verbatim line. **Both final checks done immediately before creation and recorded here: zero pods (`runpodctl pod list` returned an empty list), and RTX 5090 SECURE stock present in the registered venue at $0.99/hr — the registered rate, not an elevated one.** The flag was kept out of `launch_a3.sh`, which is untouched registered text. **Pod `kdvdsomkf3u6va` created 2026-09-19 ~20:14Z at $0.99/hr (confirmed from the pod record, not assumed); LAUNCH CLEAN END TO END** — remote pre-flight passed all three self-tests **on the pod** before a training step (`curriculum_a3`, `encoding_a3`, `train_a3`, the last exercising the new flag's code path on the rented machine), training confirmed by the `[t]rain_a3.py` aliveness check rather than by the launcher's exit status, watchdog spawned under `caffeinate` (pid 54548) and already fetching. **FIRST PRODUCTION ARMING OF THE POD-SIDE REAPER, and it VERIFIED:** the dedicated reaper key reached pod management as the pod itself, and a laptop-independent +24h deadline reaper is running on the machine. That backstop was built after the third idle-billing occurrence and had never actually run in production; the laptop watchdog remains the primary reap and **the lid must still be open**, because `caffeinate` blocks idle sleep and not lid-close. One 30M **register-less** run, **seed 0**, with the unregistered control-learnability flag: the control battery gets a loss term of its own (`--ctl-weight 2.0 --ctl-frac 0.5`) instead of about a third of a shared one. **Seed 0 on purpose**, so the comparison against the existing A3 pilot is matched on initialization and data order and the loss is the only thing that differs. **The question:** does the control learn when properly supervised, or is supervision not the binding constraint? Three seeds have now failed it identically (0.2877, 0.3057, 0.3195, all under the 0.3227 reached by a solver that cannot read the name the question supplies), and the under-supervision reading has never been separated from the design-defeats-it reading. **Outcome cells pre-stated by John BEFORE the code existed** (`control-learnability-pilot.md`, committed `7eee3c5` ahead of the implementation): control intact **≥ 0.60 LEARNED**; **0.3227 to 0.60 PARTIAL**; **≤ 0.3227 DID NOT LEARN**, and option D or closing A3 is what is left. Secondary cells, reported with it and never instead of it: the primary battery must still learn (intact ≥ 0.50) and must still collapse under its own lesion, or the run is reported as a failed intervention and says nothing about the control. **Recipe identical to the 2026-09-15 A3 pilot** and unchanged by the flag: 585,544,960 tokens, 55,116 steps, batch 128, act-weight 1.0, eval every 500 at n=100 for trajectory only. **No grammar change** — the grammar, tokenizer, frozen batteries, rendering, ceilings and attack sweep are untouched; only the apportioning of the loss across queries the episode already carries moves. **Nothing registered.** No registered verdict is read from this run and John's threshold lock is not touched. The loss change (`ee7fc91`) defaults to OFF and the self-test proves the off path is bit-identical to the pre-flag pooled term rather than asserting it. **Launcher: `src/launch_ctl_pilot.sh`, a separate unregistered file.** `launch_a3.sh` is registered text and has no hook for an extra training argument, so it was NOT edited — the repo's own precedent (launch_a3.sh was split from launch_pilot_a1.sh for exactly this reason). Derived verbatim; the diff is the two flags, a distinct output name that cannot overwrite the existing pilot, and a refusal to launch at ctl-weight zero. **Dry run clean**; all three module self-tests pass locally and the remote pre-flight runs them on the pod and deletes it rather than billing a run on a truncated push. **PRE-LAUNCH CHECKS — two done, two outstanding.** DONE: **zero pods confirmed** at staging time; and the **Mac's sleep override is already back ON** (`SleepDisabled 1`, measured at staging), so the reversion recorded in the annotation below has since been undone by somebody — but the laptop watchdog is still the only reap that has ever worked in production, idle billing has cost about $10.30 across four occurrences, and **the lid must be open** regardless of the setting, because `caffeinate` blocks idle sleep and not lid-close. OUTSTANDING: (ii) confirm the balance covers the estimate plus $10 (about $23) by a route other than the stored key, which returned HTTP 403 during the last wave; (iii) confirm 5090 secure stock in EU-RO-1 at launch time. **Re-confirm zero pods immediately before creating one**, since the staging check ages. **Volume `x9f8pkn58t` (`mvm-models-ro`, EU-RO-1) is the right one and is untouched** — the volume deleted on 2026-09-19 was the old `mvm-models` (`8xeftvclmv`), see the annotation below. | RTX 5090 SECURE EU-RO-1 $0.99/hr, volume `x9f8pkn58t` | **est 9.87h training / ~10.2h pod**, computed from the pilot's **measured 0.645 s/step** × 55,116 steps; step count and token budget are unchanged because the grammar is unchanged. The one thing that could move the pace is that control questions render at a slightly different length from state and syntax ones, so padded batches may differ by a few percent — **MEASURED PACE, step 500: 325.4s (0.6508 s/step); step 1000: 651.5s (0.6515 s/step).** Against the A3 pilot on the same seed and the same recipe, 324.9s and 646.7s — **within about 0.7%**, so the padding effect I flagged is real and negligible. **Estimate CONFIRMED, not revised: 9.97h training, ~10.3–10.5h pod, $10.17–10.37**, inside the $9–13 band. | **$10.2, band $9–13** | — (nothing spent; not launched) | **⚠ READING NOTE, so the two trajectories are not misread side by side: THE LOSS NUMBERS ARE NOT COMPARABLE ACROSS THE TWO RUNS, BY CONSTRUCTION.** The pilot's query loss is one pooled mean; this run's is `other-term + 2 × control-term`, each normalised over its own subset of rows, so it sits on a different scale arithmetically and not because training is going worse. At step 500 the pilot reads q_loss 1.075 and this run 3.433, which is about what `1.1 + 2 × 1.15` gives. Anyone comparing the raw loss curves without this will conclude the run is diverging when it is not. **Trajectory accuracies at steps 500/1000 (n=100, TRAJECTORY ONLY — not the registered endpoint evaluation, and NOT the number the pre-stated cells are read on):** this run T_act 0.48/0.48, T_other 0.28/0.27, T_state 0.58/0.57, T_syntax 1.00/1.00; the pilot at the same steps T_act 0.54/0.52, T_other 0.24/0.18, T_state 0.66/0.64, T_syntax 1.00/1.00. **Nothing is read from this.** It is 1.8% of training at a sample size whose noise is large, the pilot's own trajectory wandered (T_act 0.54 → 0.52 → 0.50 → 0.64 over the first 2,000 steps), and **the pre-stated cells are read on the control's intact score at the n=800 endpoint evaluation, not here.** Recorded now only because it was measured now, and because a number that is written down before the end cannot be quietly reinterpreted after it. The one thing genuinely worth watching is the state battery, which is the coupling the pre-statement flagged: it drops from about a third of the rows to about a quarter, and it currently sits below the pilot at the same step. **OUTCOME 2026-09-20. THE RUN COMPLETED ITS FULL BUDGET, AND THE FINAL CHECKPOINT WAS NOT FETCHED. Both halves matter.** Pod `kdvdsomkf3u6va` ran 20:14Z → ~06:15Z, about **10.0h ≈ $9.9**, inside the $9–13 estimate, with **ZERO idle billing — the first run in the programme's history with none.** **What we hold locally is step 51,500 of 55,116 (93.4% of budget)**, the last incremental pull, archive-fetched and checksum-VERIFIED at 05:40Z. The trajectory record is complete to step 54,500 (109 evaluations). **The final full-budget checkpoint is on the network volume `x9f8pkn58t`, and it is there by proof rather than by hope:** `train_a3.self_terminate` REFUSES to delete the pod unless the output path is on `/workspace/` and the file exists — a hard gate added after the 2026-08-12 loss — and it runs only after the checkpoint and the DONE sentinel are written. The pod did delete itself, so both conditions were true at that moment. **ROOT CAUSE, and it is new: the trainer's self-terminate RACED the watchdog's fetch interval.** The watchdog polls about every ten minutes and is the thing that performs the final fetch-and-delete on the DONE sentinel; the trainer finished between poll 57 (06:11:12Z) and the next poll, wrote its checkpoint, and deleted its own pod before the watchdog could come back for it. The watchdog's log simply stops at poll 57, with no DONE, no final fetch and no delete — because there was no longer a pod to reach. **Two reaping mechanisms, built a month apart for the same problem, now defeat each other.** Self-termination was added after idle billing cost about $9.50 across three occurrences, and it worked perfectly here — that is exactly why there was no idle charge. The watchdog's final fetch was built for the same reason and now never gets to run on a completing run. **This will recur on every future run that finishes normally**, and it is a process defect, not bad luck. **NOT a balance problem:** the account holds **$79.89** and was never near exhaustion, so this is not a repeat of 2026-08-12. **RECOVERY, not yet done and not yet authorised:** mount `x9f8pkn58t` on the cheapest available pod, copy the file, delete the pod. Minutes, well under a dollar, and it needs John's go like any billable action. Until then the full-budget endpoint reading does not exist. **RECOVERED 2026-09-20 and the row is closed.** The DONE sentinel reads `{"step": 55116, "tokens": 585552384}` — the full registered budget, identical to the pilot and seeds 1 and 2 — and the checkpoint came back intact, md5 `a0c1c73af9c9bd5c60fb0e4e146180eb` verified against the volume before the recovery pod was deleted. **The root cause is confirmed in the trainer's own log rather than reconstructed**: `TRAINING COMPLETE` followed on the very next line by `self-terminate: runpodctl remove pod kdvdsomkf3u6va -> rc=0 pod removed`. **Endpoint on the full checkpoint: the control battery reads 0.3125 (sd 0.0240) — DID NOT LEARN**, with both secondary cells passing. Full reading in `control-learnability-pilot-findings.md`. The partial step-51,500 checkpoint and its reading are kept alongside so the earlier number stays reproducible. **ACTUAL ~$9.9 → A3 cumulative ~$44.2 / $100**, leaving ~$55.8 (was: would become ~$44.5), leaving ~$55.5. **Programme running total: ~$215.7 + $9.9 = ~$225.6 / $400** on the wider envelope (corrected 2026-09-21 on the Gate A money-citation finding, `RT-147`, which found that the programme total the closure text cites was not in this ledger: this row had carried the pre-run figure. The row earlier read "RT-143's companion", which is the finding about the nine measured numbers, not the money one.), and under the $80 account limit. *(Counting an unregistered diagnostic against the A3 hard stop is the conservative reading and is Claude's call; K6 speaks of cumulative actual spend, and a diagnostic run inside experiment 06 is most honestly counted there.)* |
| 2026-09-20 | checkpoint recovery (UNREGISTERED) | **RECOVERY OF THE CONTROL-LEARNABILITY PILOT'S FINAL CHECKPOINT.** John's go, quoted verbatim per C2(b): **"Go, recover the checkpoint, and kill the watchdog."** The 2026-09-19 pilot completed its full 55,116-step budget but the trainer self-terminated its pod between watchdog polls, so the watchdog never performed its final fetch and the local copy stopped at step 51,500 (93.4%). The full-budget checkpoint is on network volume `x9f8pkn58t` — by proof, not hope: `self_terminate` refuses to delete a pod unless the output is on `/workspace/` and the file exists, and it runs only after the checkpoint and DONE sentinel are written. **What runs:** cheapest available secure pod in EU-RO-1 with that volume mounted (network volumes are secure-cloud only), copy the checkpoint and the DONE sentinel and the final training log, **verify by md5 against the volume before deleting**, delete the pod, confirm zero pods. No training, no GPU work — this is a file copy. **Why it matters beyond tidiness:** the partial checkpoint reads the control battery at 0.3158 (sd 0.0204), which straddles the 0.3227 cell boundary at 0.34 sd below it, so the partial checkpoint cannot score John's pre-stated cell. The full-budget checkpoint is the one the cells are read on. **The watchdog was also killed** on the same instruction — it had been spinning against a deleted pod for over ten hours and holding `caffeinate`, keeping the Mac awake for no reason. | cheapest secure EU-RO-1 (A40 $0.49/hr or RTX 3090 $0.50/hr), volume `x9f8pkn58t` | **~5 min**, A40 secure EU-RO-1 | **<$0.15** | **$0.067** (balance $79.8897 → $79.8228, measured not inferred) | A3 cumulative ~$44.2 / $100 before this → **~$44.3 / $100** with the $0.07 recovery; **programme running total ~$225.6 + $0.07 = ~$225.7 / $400** (added 2026-09-21 so the A3 closure text can cite a figure the ledger contains). |

===== END OF RECORD 22 =====
