# 30M A1 pilot — raw findings note (SCAFFOLD — endpoint numbers pending)

*Fast, unpolished, per roadmap item "30M result: raw findings note" — NOT
through Voice Calibration. Drafted 2026-08-16 ~15:00Z while the run finishes;
sections marked ⟨PENDING⟩ fill in from the endpoint + gate (iii). The verdict
is John's adjudication against the pre-stated signatures in
`pilot-a1-findings.md`; nothing here auto-emits it.*

## Run record

- Pod `rhddnh0u4le0l9` (`mvm-a1-pilot-30M`), RTX 5090 SECURE, EUR-IS-1,
  $0.99/hr, network volume `mvm-models` at `/workspace` (checkpoints + log
  survive pod death — the 08-12 process fixes working as designed).
- Recipe: `train.py --scale 30M --seed 0 --batch 128 --steps 200000
  --max-tokens 784083840 --eval-every 500 --eval-n 100 --eval-mode heldout`.
- Started 2026-08-15 21:43Z; measured pace 0.647–0.665 s/step (FASTER than
  the H100's 0.70 — workload is enactment/Python-bound, not GPU-bound).
- Token-budget stop at 784.08M tokens ≈ step 102,094; completion ⟨PENDING —
  actual finish time⟩; cost est ~$19 (ledger actual-after ⟨PENDING⟩).
- This is the re-run of the row lost 08-09/12 (pod outran its backstop;
  post-mortem in STATUS.md). Watchdog fetch-and-kill + session-independent
  monitoring ran throughout; one false stall alarm traced to lid-close sleep,
  none to the run.

## Trajectory (from synced held-out evals, n=100 per battery)

| step | T_sr | T_si | T_state | T_syntax | T_sr_rev | note |
|---|---|---|---|---|---|---|
| 500 | 0.62 | 0.10 | — | 1.00 | 0.00 | pre-scale shape; pace trued up here |
| 27,500 | 0.97 | 0.46 | 0.96 | 1.00 | 0.25 | 10M signature already breaking |
| 46,000 | 0.97 | 0.53 | 0.98 | 1.00 | 0.50 | both diagnostics climbing |
| 60,500 | 0.98 | 0.80 | 1.00 | 1.00 | 0.50 | mid-transition |
| 89,000 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | everything at ceiling |
| ⟨PENDING endpoint⟩ | | | | | | verdict reads HERE |

Sharp everything-to-ceiling transition in roughly the 46k–89k window
(⟨PENDING: exact first-above-threshold steps from run_post_pilot.sh
readout⟩) — same qualitative shape as the v1.0 10M pilot's 8.5k–13.5k
transition, arriving later at the harder A1 task.

## Signature comparison vs the pre-stated fork

Pre-stated in `pilot-a1-findings.md` (verdict at ENDPOINTS):

- **H_scale**: T_si (and plausibly T_sr_rev) reach ceiling → 30M learns;
  ladder registers 30M.
- **H_shortcut-starvation**: 10M signature repeats (instant T_sr, flat T_si,
  floor T_sr_rev) → ladder STOPS; upstream packet.

| metric | 10M endpoint | 30M endpoint | floor |
|---|---|---|---|
| T_si | 0.37 (never transitions) | ⟨PENDING⟩ (0.98 @ 89k) | 0.125 |
| T_sr_rev | 0.00 (entire run) | ⟨PENDING⟩ (1.00 @ 89k) | — |
| T_sr | 0.96 | ⟨PENDING⟩ | 0.125 |
| T_state | 1.00 | ⟨PENDING⟩ | 0.042 |
| T_syntax | 1.00 | ⟨PENDING⟩ | 0.100 |

In-flight lean was H_scale from ~step 27.5k onward; endpoint row decides.

## Gate (iii) at the registered n=4000 — ⟨PENDING⟩

`fingerprint_gate.py --run --ckpt <30M checkpoint>` (replaces the run-(iii)
entry in `cue_detector_gate.json` by design; 10M record in git history).

- Arm A (committed detector on enacted text): ⟨PENDING⟩ vs [0.45, 0.55]
- Arm B (likelihood attack): ⟨PENDING⟩ vs [0.45, 0.55]
- Positive controls (incl. retired v1.0 policy pipeline): ⟨PENDING⟩
- Checkpoint md5: ⟨PENDING⟩

## Verdict — ⟨PENDING: John adjudicates⟩

Branch docs pre-drafted; fire the winner, delete the loser:
- H_scale → `amendment-a2-draft-IF-30m-learns.md` (registered scale 30M;
  cap $200→$400; 5-seed × full+twin ≈ $190 at measured 5090-secure pricing)
- H_shortcut-starvation → `upstream-draft-IF-shortcut-starvation.md`

## Cost/pricing note (already actionable)

Measured 5090-secure pace reprices the ladder: ~$19/30M run vs the ~$66
H100 estimate and the ~$650–770 the original cap memo priced for the full
5-seed design — the A2 cap ask ($400) covers the whole remaining program
with headroom. Ledger row actual-after ⟨PENDING: console rows at phase
boundary⟩; running total before this run $105.62/$200.
