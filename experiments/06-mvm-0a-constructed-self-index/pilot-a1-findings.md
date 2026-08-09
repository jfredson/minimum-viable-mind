# A1 pilot findings — 10M FAILS the ceiling requirement: the acting channel solves T_sr instantly and T_si never transitions (2026-08-09)

*First compute of the A1 pipeline (§Amendment A1), run per the
registered recipe: 10M (8.7M params), seed 0, 171.79M tokens (20
tok/param), batch 128, 22,369 steps, held-out eval every 500 steps
with the T_sr_rev split [A1.1]. Launched by John ("Fire", C2), pod
`3ethp3bc7le6e4` (RTX 5090 community), 2.78h train wall-clock,
checkpoint md5 `bab56cd8…` in `artifacts/pilot-a1-10m-seed0/`. Ledger
row in `compute-ledger.md`.*

## Headline

**10M does not learn the A1 task to ceiling.** By the pre-committed
smallest-that-learns rule the ladder climbs: **the 30M pilot is the
next registered step** (John launches; est below). Final numbers at
budget exhaustion against chance floors 0.125/0.125/0.042/0.100:

| battery | final | max | first ≥0.95 | v1.0 pilot (same budget) |
|---|---|---|---|---|
| T_sr (all) | 0.96 | 0.96 | step 1,000 | 0.99 |
| **T_sr_rev (revised-own split)** | **0.00** | 0.25 | never | *(not measured — RT-11 gap)* |
| **T_si** | **0.37** | 0.47 | never | 0.97 |
| T_state | 1.00 | 1.00 | step 5,000 | 0.995 |
| T_syntax | 1.00 | 1.00 | step 500 | 1.00 |

The pick rule's letter names T_sr and T_state, but T_sr at 0.96 is not
ceiling once its composition is read honestly: revised-own items are
~6% of T_sr evals (0.25 revision rate × 1/4 own reviser) and the model
scores **0.00** on them across the entire run — ~120 cumulative items,
all answered with the *first* own act for the item rather than the
revision. Non-revised T_sr is ~1.00. And T_si failing its §Task
batteries baseline requirement would gut the registered design
regardless (it is the scratchpad control; an excluded T_si leaves the
self-relevant/self-irrelevant differential without its comparison), so
reading 0.96/1.00 as a pass and proceeding to the 5-seed spend would
be threshold-gaming our own registration.

## The shape, and what it says about the acting channel

Three facts, one picture:

1. **T_sr ≥0.95 from step 1,000.** In v1.0, T_sr left the floor only
   when on-policy fill engaged and reached ceiling at the ~8.5k–13.5k
   transition. Under A1 the acting channel makes own-binding almost
   immediate — the motor-copy trace is a far stronger signal than the
   statistical route it replaced. RT-02's route analysis is confirmed
   from the other side: given a non-statistical channel, the model
   prefers it instantly.
2. **T_si never transitions.** Same battery, same budget, same scale
   as v1.0's 0.97 — the only change is the pipeline. The v1.0
   transition lifted T_sr and T_si *together*, which suggests they
   shared circuitry: solving own-binding statistically forced a
   general marker→commitment binding that T_si rode on. Under A1 the
   acting channel gives T_sr a private shortcut, and the shared
   machinery never gets built. T_si's own supervision (one query per
   ~4) sustained only a late drift (0.26 → 0.47 over the final 6k
   steps, inconclusive).
3. **T_sr_rev stays at 0.00.** The register write path is a per-marker
   GRU — recency should be architecturally easy — yet the model
   retrieves the first act. Consistent with the shortcut reading: an
   act-trace lookup keyed by item, not a maintained per-agent state
   that later acts update.

Two hypotheses go to the 30M pilot armed with a prediction each:

- **H_scale:** 10M lacks capacity to hold the acting-channel solution
  *and* general marker binding; 30M learns T_si (and plausibly
  T_sr_rev) to ceiling. The ladder exists for exactly this.
- **H_shortcut-starvation:** the acting channel removed the gradient
  pressure that built shared binding machinery in v1.0; no scale fixes
  it, 30M shows the same signature (instant T_sr, flat T_si, floor
  T_sr_rev). If this is the outcome, the fix is curricular and lands
  as a registered amendment — e.g. rebalancing query supervision — and
  the deeper lesson is uncomfortable and interesting: **giving a
  system a wired self-channel can *prevent* it from learning the
  general other-modeling the task was designed to force.** That
  finding would go upstream on its own.

The A1 design change is not impugned by this result: the v1.0
alternative was a leaking gate, and gate (iii) below shows the A1
pipeline is clean. The task got harder for the right reason — T_sr can
no longer be bought with statistics that also leak.

## Gate run (iii) against this checkpoint

**PASS at the registered n=4000** (`cue_detector_gate.json`, checkpoint
md5 `bab56cd8…`) — the run that FAILED on the v1.0 pipeline:

| arm | clean AUC [95% CI] | bound | positive controls | verdict |
|---|---|---|---|---|
| A — committed family on enacted text | **0.4874** [0.4664, 0.5110] | [0.45, 0.55] | constant filler 0.9361 ✓ | **PASS** |
| B — likelihood attack | **0.4933** [0.4808, 0.5062] | [0.45, 0.55] | greedy 0.8796 ✓; **retired v1.0 policy pipeline 0.8514 ✓** | **PASS** |

Both clean CIs sit inside the equivalence bound; both arms still catch
the v1.0 pipeline (the failure this gate was built on) at ~0.85 — the
instruments have teeth and the enacted data carries nothing for them
to bite. RT-17's by-construction prediction is now also an empirical
record. All three gate runs PASS on the A1 pipeline. (n=300 shakeout
agreed: clean arms at chance with power-limited CIs.)

Note for the record: whichever scale the ladder settles on, run (iii)
re-runs against a checkpoint at the *registered* scale before the
5-seed spend — the fingerprint that matters is the registered policy's.

## Next steps

1. **30M pilot** (John launches per C2): same recipe, `--scale 30M`,
   600M tokens (20 tok/param at ~29M params), batch 128. Est: ~3.5×
   tokens × ~2.5× step cost ≈ 6–9 GPU-h ≈ **$4–7 nominal / up to ~$25
   at the anomaly rate** on a community 5090. `launch_pilot_a1.sh`
   generalizes with env overrides (or copy with the three values
   changed).
2. If 30M reproduces the 10M signature (instant T_sr, flat T_si,
   T_sr_rev floor): stop the ladder — the loss is structural, not
   scale — and open the amendment cycle on H_shortcut-starvation
   rather than spending the 100M rung reflexively. The ladder rule
   licenses the climb; it does not command a mechanical march through
   an outcome the middle rung has already explained.
3. Ledger: reconcile the 2026-08-09 5090 row (accruing at fetch time)
   and note the 08-08 anomaly row *grew* overnight (8.47h → 9.41h
   billed, $5.86 → $6.52) — consistent with delayed/spread billing
   rather than a one-time error; the waived-ticket note in the ledger
   stands.

## Ops notes

- The launch script's final ssh reset (exit 255) AFTER starting the
  run — benign, now tolerated in-script with an explicit `pgrep`
  aliveness check.
- The session harness killed every long-lived background watcher
  (loop, single-sleep, and remote-blocking ssh variants, 13–50 min
  lifetimes); redundant staggered single-shot checks worked. Memory
  updated.
- Train wall-clock 10,021s for 171.79M tokens on the 5090 — ~1.7× the
  v1.0 pilot's 5,985s, close to the 3-graphed-passes estimate (~1.5×).
