# Handoff — 30M A1 pilot re-run in flight (written 2026-08-16 02:50Z for the relieving session)

*Everything durable is in STATUS.md (top two entries), compute-ledger.md
(2026-08-15 row), and pilot-a1-findings.md (pre-stated signatures). This
note is the operational layer: what is running on which processes, and
what the relieving session must re-arm vs must NOT duplicate.*

## 1. The run

MVM-0a Amendment-A1 **30M learnability pilot** (ladder rung 2; re-run of
the row lost 08-09/12). Registered question: smallest-that-learns.
Diagnostic fork: **H_scale** (T_si and plausibly T_sr_rev reach ceiling)
vs **H_shortcut-starvation** (10M signature repeats: instant T_sr, flat
T_si, floor T_sr_rev) — signatures pre-stated in `pilot-a1-findings.md`;
verdict read at ENDPOINTS, adjudicated by John, never auto-emitted.

- Pod `rhddnh0u4le0l9` (`mvm-a1-pilot-30M`), RTX 5090 SECURE EUR-IS-1,
  $0.99/hr, network volume `mvm-models` (`8xeftvclmv`) at `/workspace`.
- Recipe: `train.py --scale 30M --seed 0 --batch 128 --steps 200000
  --max-tokens 784083840 --eval-every 500 --eval-n 100 --eval-mode
  heldout --out /workspace/mvm-out/pilot_a1_30m_seed0.pt` (log
  `/workspace/mvm-out/train_pilot_a1_30m_seed0.log`).
- Started 2026-08-15 21:43Z; measured 0.647 s/step; ~102,094 steps
  (token-budget stop) → **ETA ≈ 2026-08-16 16:05Z**; est ~$19.
- As of 02:47Z: step 27,500 (27%), loss 0.50, T_sr 0.97 / T_state 0.96 /
  T_syntax 1.00 / **T_si 0.46 and climbing** (10M ended 0.37) /
  **T_sr_rev 0.25, off the floor** (10M: 0.00 for the whole run).
  In-flight read: the 10M failure signature is breaking → leaning
  H_scale, but a shelf at 0.4–0.5 would still fail ceiling and land in a
  murky-middle adjudication. Endpoints decide.

## 2. Monitoring — what is already running (do NOT duplicate)

**The watchdog is an OS process on John's Mac, independent of any Claude
session — it survives session close.** PIDs 4103/4104 (`watch_run.sh`
under `caffeinate -i`, spawned via nohup), env file
`artifacts/pilot_a1_30m_seed0/run_rhddnh0u4le0l9.env`, log
`artifacts/pilot_a1_30m_seed0/watchdog.log`. Every 10 min it syncs
`pilot_a1_30m_seed0.jsonl` + log tail; hourly it pulls the full 471MB
checkpoint. **On the DONE sentinel — or the hard deadline
2026-08-18T05:37:17Z — it does a full fetch and DELETES the pod itself.**
Do not run a second fetch/kill loop; monitor the watchdog, don't replace
it.

What DIED with the old session and the relieving session should re-arm:
- **Completion watch:** local `artifacts/pilot_a1_30m_seed0/pilot_a1_30m_seed0.DONE`
  appears → run the post-run pipeline (§3).
- **Stall detector:** local jsonl mtime >35 min with no DONE → training
  likely crashed while the pod lives; ssh in and check
  (`tail /workspace/mvm-out/train_pilot_a1_30m_seed0.log`). Resume =
  fresh C2 go from John: `RESUME=/workspace/mvm-out/pilot_a1_30m_seed0.pt
  ./launch_pilot_a1.sh` (checkpoint + opt state are on the volume).
- **Watchdog-death check:** `pgrep -f watch_run.sh` empty → respawn:
  `nohup caffeinate -i bash src/watch_run.sh <abs path to env file> >>
  <artifacts dir>/watchdog.log 2>&1 < /dev/null &` (idempotent; safe).

SSH (also in the env file, keepalive opts matter — a hung ssh froze
nothing only because we added them):
`ssh -o ConnectTimeout=20 -o ServerAliveInterval=30 -o ServerAliveCountMax=4 -o BatchMode=yes -i /Users/john/.runpod/ssh/runpodctl-ssh-key root@157.157.221.30 -p 55783 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null`

## 3. When it finishes

The watchdog fetches everything and kills the pod on its own (verify:
watchdog.log ends "run complete"; `runpodctl pod list` empty). Then:

1. `src/run_post_pilot.sh` — completion check + md5, trajectory readout
   vs the pre-stated signatures, **gate (iii) at registered n=4000**
   against the 30M checkpoint (`fingerprint_gate.py --run --ckpt …`,
   runs locally, $0, maybe an hour on MPS). NB: it REPLACES the run-(iii)
   entry in `cue_detector_gate.json` (by design; the 10M record lives in
   git history + pilot-a1-findings.md).
2. **John adjudicates the verdict.** Branch docs are pre-drafted, fire
   the winner, DELETE the loser:
   - H_scale → `amendment-a2-draft-IF-30m-learns.md` (scale 30M, cap
     $200→$400; 5-seed ≈ $190 at this venue) — registration before any
     affected run.
   - H_shortcut-starvation → `upstream-draft-IF-shortcut-starvation.md`
     (ladder STOPS; packet upstream; curricular amendment cycle).
3. Ledger: actual-after from console rows at the phase boundary
   (est $19); STATUS entry; commit/push (re-check `git log` first —
   parallel-session rule).

## 4. Gotchas not fully written down elsewhere

- **C2:** no new pods/runs/resumes without John's explicit go, ever.
- `pgrep -f 'train.py'` matches its own remote shell — always use the
  `[t]rain.py` form (this false-ALIVE burned us once already).
- The Bash tool shell here is zsh: it does NOT word-split `$SSH` — inline
  the ssh command or use bash scripts.
- Lid-close suspends the watchdog (caffeinate -i ≠ lid); it resumes on
  wake and catches up. Post-completion lid-closed = pod idles $0.99/hr
  until wake. John knows; deadline + terminate-after (2026-08-18) are
  the backstops.
- Balance ~$95, cap spend $105.62 + this run. Report money in the
  ledger's terms (spend vs cap; balance is funding, not cap).
- Report times as dates/UTC (a weekday slip already happened once).
- Still pending on John, no rush: RunPod ticket
  (`runpod-ticket-overrun.md`), cap memo sign-off
  (`cap-adjudication-memo.md`).
