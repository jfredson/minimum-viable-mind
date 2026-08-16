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
| **102,095 (END)** | **1.00** | **0.93** | **1.00** | **1.00** | **1.00** | verdict reads HERE |

Endpoint recorded 2026-08-16 16:41Z: loss 0.0259, tokens 784,089,600
(budget stop), wall 68,228.8s = 18.95h train. DONE sentinel
`{"step": 102095, "tokens": 784089600}`; watchdog final fetch OK
16:41:27Z, pod deleted by watchdog (pod list empty). T_si endpoint 0.93
sits in its late-run noise band (0.93–0.98 over the final evals; n=100).

Measured transition points (first eval ≥0.9, from run_post_pilot.sh):
T_syntax @500, T_sr @1,000, T_state @1,500 — the surface-solvable floor,
immediate as designed — then **T_si @64,500 and T_sr_rev @73,000**: the
two diagnostics transition late and separately, the same
qualitative everything-to-ceiling shape as the v1.0 10M pilot's
8.5k–13.5k window, arriving much later at the harder A1 task. T_si max
0.990; endpoint 0.93 is late-run eval noise (n=100), not a shelf.

## Signature comparison vs the pre-stated fork

Pre-stated in `pilot-a1-findings.md` (verdict at ENDPOINTS):

- **H_scale**: T_si (and plausibly T_sr_rev) reach ceiling → 30M learns;
  ladder registers 30M.
- **H_shortcut-starvation**: 10M signature repeats (instant T_sr, flat T_si,
  floor T_sr_rev) → ladder STOPS; upstream packet.

| metric | 10M endpoint | 30M endpoint | floor |
|---|---|---|---|
| T_si | 0.37 (never transitions) | **0.93** (0.93–0.98 band late-run) | 0.125 |
| T_sr_rev | 0.00 (entire run) | **1.00** | — |
| T_sr | 0.96 | **1.00** | 0.125 |
| T_state | 1.00 | **1.00** | 0.042 |
| T_syntax | 1.00 | **1.00** | 0.100 |

In-flight lean was H_scale from ~step 27.5k onward; the endpoint row reads
as the H_scale signature (both diagnostics at/near ceiling; neither
pre-stated failure mark present). Adjudication is John's.

## Gate (iii) at the registered n=4000 — **PASS** (2026-08-16 ~17:0xZ)

`fingerprint_gate.py --run --ckpt pilot_a1_30m_seed0.pt` (replaced the
run-(iii) entry in `cue_detector_gate.json` by design; 10M record in git
history). Ran locally on MPS, $0.

- Arm A (committed detector on enacted text): **0.4874 [0.4664, 0.5110]**
  — inside [0.45, 0.55], PASS; positive control (constant) 0.9361 fires.
- Arm B (likelihood attack, model-scored values): **0.4964
  [0.4837, 0.5095]** — inside [0.45, 0.55], PASS; positive controls fire:
  greedy 0.9312, retired v1.0 policy pipeline 0.8248 (RT-17's
  by-construction prediction holding at 30M).
- Checkpoint md5: `fd1eb80c990435ca2629cee58df08779`.
- **GATE: PASS** — with standing proven by all positive controls. The
  30M rollouts carry no detectable ownership fingerprint; the 5-seed
  spend precondition is met.

## Verdict — **H_scale** (adjudicated by John, 2026-08-16)

Adjudicated in-session after the full endpoint + gate readout; Amendment
A2 registered the same day (`pre-registration.md` §Amendment A2: scale
30M, cap $200→$400). The starvation branch doc deleted unused, per the
pre-stated procedure.

Caveats on the record (none weaken the call):

1. **Single seed.** H_scale is established for seed 0; the registered
   5-seed run is what turns "a 30M can learn this" into "30M learns
   this."
2. **Learnability ≠ load-bearing.** This pilot says the A1 task is
   learnable at 30M; it says nothing about whether the *register* is
   what carries it. That is H_load-bearing — the registered main
   experiment, still entirely open. Do not over-read upstream.
3. **Endpoint literalism.** The endpoint row reads T_si 0.93; "ceiling"
   here means the late-run band 0.93–0.98 (max 0.990) at eval n=100 —
   stated explicitly rather than quietly citing the max.
4. **RT-17 strengthened, not touched.** The acting channel is present in
   this pipeline, and the retired v1.0 policy pipeline still lights the
   detector at 0.82 while the clean arms sit at chance — own-ness is
   carried by the act, not the statistics, at 30M as at 10M.

## Cost/pricing note (already actionable)

Measured 5090-secure pace reprices the ladder: ~$19/30M run vs the ~$66
H100 estimate and the ~$650–770 the original cap memo priced for the full
5-seed design — the A2 cap ask ($400) covers the whole remaining program
with headroom. Ledger row actual-after ⟨PENDING: console rows at phase
boundary⟩; running total before this run $105.62/$200.
