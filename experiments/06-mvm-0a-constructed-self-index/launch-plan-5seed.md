# 5-seed × full+twin launch plan (registered run, Amendment A2)

*2026-08-16. Adjudicated: pairs sequencing; pilot seed-0 checkpoint counts
as registered seed-0 full (see pre-registration §Run-identity note); start
on current balance, top up on trigger. All launches are HUMAN-RUN [C2] —
John fires them; `DRYRUN=1` first, every time.*

## The balance rule (hard, from the 08-11 loss)

**Never launch a wave unless balance ≥ projected cost of everything then
in flight + $10.** A pair ≈ $38–40 incl. volume drip. Check:
`runpodctl` GraphQL `myself { clientBalance }` (or the console) before
each wave. **Top-up trigger: ~$120 before wave 2** (balance after wave 1
≈ $40 — covers a pair with only ~$2 margin, too thin).

## Waves (each ≈19h; watchdog per run; Mac powered, lid open, ~5 days)

| wave | runs | commands (from `experiments/06-mvm-0a-constructed-self-index/`) |
|---|---|---|
| 1 | s0 twin + s1 full | `SEED=0 TWIN=1 ./src/launch_pilot_a1.sh` · `SEED=1 ./src/launch_pilot_a1.sh` |
| 2 | s1 twin + s2 full | `SEED=1 TWIN=1 ./src/launch_pilot_a1.sh` · `SEED=2 ./src/launch_pilot_a1.sh` |
| 3 | s2 twin + s3 full | `SEED=2 TWIN=1 ./src/launch_pilot_a1.sh` · `SEED=3 ./src/launch_pilot_a1.sh` |
| 4 | s3 twin + s4 full | `SEED=3 TWIN=1 ./src/launch_pilot_a1.sh` · `SEED=4 ./src/launch_pilot_a1.sh` |
| 5 | s4 twin (solo) | `SEED=4 TWIN=1 ./src/launch_pilot_a1.sh` |

Wave 1's second launch is the cheap test of network-volume multi-attach.
If the second pod's create fails on the volume: relaunch it with
`NETVOL=none` (container disk + watchdog hourly pulls) or go serial —
minutes lost either way. Do NOT move any registered run to COMMUNITY.

## Money map (against the $400 single-amendment ceiling)

- Spent through the pilot: ~$124.5
- 9 remaining runs ≈ $171 + drip ≈ $175
- Projected after 5-seed: ~$300 → ~$100 headroom for gate re-runs,
  ablation passes, θ/δ calibration, blind-localization, margin
- Repeated-sampling: funded ONLY by underspend (R1 adjudication)

## Per-wave wrap (the relieving-session checklist)

1. Both DONE sentinels fetched, pods deleted by their watchdogs
   (`runpodctl pod list` empty), md5s recorded.
2. Ledger row actual-after; balance check vs the rule before next wave.
3. Eval endpoint sanity (twin should FAIL the self batteries — that is
   the design's prediction, not a bug: no register, no binding).
4. Next wave launched (C2) or top-up requested.
