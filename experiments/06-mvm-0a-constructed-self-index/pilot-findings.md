# Learnability pilot findings — 10M, seed 0 (2026-08-08)

*First rung of the registered scale ladder (pre-registration v1.0
§Materials). Learnability only: held-out episode accuracy, **no
ablations** [RT-10]. Artifacts: `artifacts/pilot-10m-seed0/` (checkpoint
`pilot_10m_seed0.pt` md5 `d63a85a91ffd9efd3d54dc9911da2a9c`, eval trace
`.jsonl`, full log). Code `e0bd13e`; pod `zv0nxkyazqfw0w` (RTX 5090
community, then deleted); run config in the checkpoint's `args`.*

## Headline: 10M LEARNS — the ladder stops at its first rung

8,589,024 params, 171,786,240 tokens (the registered 20 tok/param
budget), 22,368 steps, batch 128, on-policy fill from step 2000, ~100 min
wall-clock. Held-out accuracy at budget exhaustion (chance floors in
parentheses):

| battery | final | floor |
|---|---|---|
| T_sr (own-commitment binding) | **0.99** | 0.125 |
| T_si (other-agent binding) | **0.97** | 0.125 |
| T_state (ownership-free cross-turn state) | **0.995** | 0.042 |
| T_syntax (surface floor check) | **1.00** | 0.100 |

Under the pre-committed smallest-that-learns rule, **the registered scale
is 10M**. No 30M or 100M pilot runs; the rule decided, not a preference.

## Shape of the run (from the eval trace)

- **T_syntax → 1.0 within 500 steps; T_state → 0.94 by step 2000.**
  Generic cross-turn state is easy here, exactly as the design intends —
  it is the competitor hypothesis, and it needs to be at ceiling for the
  H_generic-state bin to be live.
- **On-policy inflection.** T_sr sat at 0.325 when fill engaged at step
  2000 and jumped to 0.615 within 500 steps — before any binding
  breakthrough on T_si (0.235 at the same point). Consistent with
  causal-authorship grounding doing real work [RT-02], but see the
  caveat below before reading it as vindication.
- **A sharp transition between steps ~8.5k and ~13.5k** took every
  battery to ceiling (T_sr 0.565→0.99, T_si 0.225→0.96). Loss fell to
  ~0.02–0.07. Ceiling then held stable for the final ~9k steps — no
  regression across the last three eval points, which matters for RT-07's
  stopping-rule concerns in the registered run.

## Caveats, stated before anyone gets excited

1. **This says nothing about H_load-bearing.** Learnability was the
   question; whether the register *carries* the binding (versus the
   residual stream) is the registered experiment — twin gate, utilization
   gate, RT-01 probes, ablations — none of which ran here.
2. **Policy-reconstruction shortcut.** After on-policy fill, T_sr's answer
   is the model's own earlier sample. A model can score well by
   *re-deriving* what it would have said rather than *recalling* what it
   did say. The mid-run T_sr > T_si asymmetry is consistent with exactly
   that shortcut. The forced-revision items [RT-11] are the guard, but
   `fill_own_turns` overwrites own-turn values with fresh samples, which
   weakens the revision contrast on own turns (the revised value is no
   longer forced to differ). **Before the registered run: make the
   revision constraint survive on-policy fill for own turns (resample
   until different, or apply the revision after fill), and report T_sr on
   revised-own items separately.** Filed as a pre-registration amendment
   candidate — it changes the fill procedure, so it must land as a
   registered amendment before the 5-seed runs, not as a quiet code edit.
3. **One seed.** Seed 0 only; the registered design's k=5 exists because
   this number is a draw [RT-06]. The pilot answers "learnable at all,"
   not "reliably learnable."
4. **No twin data.** The no-register twin gate [RT-03] runs in the
   registered phase; nothing here shows the residual path can carry the
   task, only that the full architecture can.

## What this unlocks

- **Gate run (iii)** — the post-training fingerprint detector, RT-02's
  most-likely-surviving cue — is now buildable against this checkpoint
  and should run before the 5-seed spend.
- The registered 5-seed × full+twin run at 10M: ~10 × 100 min ≈ ~17 GPU-h
  ≈ **$6–12** at community rates (see ledger for the billing anomaly that
  must be resolved first).

## Ops notes

- Secure-cloud 4090 never exposed SSH in 12 min (billed $0.16 — it was
  live; deleted before the instrument was tested — the top-level
  `sshCommand` field is dead, use `.ssh.ssh_command`). Community 5090
  booted in ~2 min and ran the whole pilot.
- The Monitor tool's shell cannot make outbound SSH connections (two
  monitors failed 100% while every direct call succeeded); chained
  background sleep-checks are the working watch pattern.
- **Billing anomaly (unresolved, John):** the 5090 row bills
  30,476,200 ms ≈ 8.47 h against ~2.42 h of pod existence — ~3.5× —
  $5.86 charged where ~$1.67 was expected. `nvidia-smi` showed a single
  GPU, so it is not a multi-GPU allocation on the OS side. Balance math
  is internally consistent with the billing rows ($106.73 − $6.02 pods −
  ~$0.78 volume drip ≈ $99.93), so the anomaly is inside the row, not a
  hidden charge. Worth a RunPod support ticket before the 5-seed runs —
  at 3.5×, the registered run's budget estimate inflates accordingly.
