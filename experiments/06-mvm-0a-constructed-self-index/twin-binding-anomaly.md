# The twin-binding anomaly (waves 1–2 of the registered 5-seed run)

*2026-08-18. Status: **finding recorded, not adjudicated**. The read on
what this means for the registered remainder is John's, at the analysis
point. Nothing here emits a verdict on H_load-bearing.*

## What we predicted, and what happened

The registered design pairs every full run with a **twin**: the same
recipe with the self-register parameters removed. The pre-stated
prediction (`pre-registration.md` §Materials, `launch-plan-5seed.md`
per-wave wrap item 3) is that **the twin SHOULD FAIL the self batteries
— no register, no binding** — and that this failure is what licenses
reading a full run's T_si/T_sr_rev as evidence that the constructed
self-index is doing work.

Across the five registered-recipe runs completed so far, that prediction
held once, failed once, and the fulls themselves split 1-in-3:

| run | register? | endpoint T_si | endpoint T_sr_rev | final loss | bound? |
|---|---|---|---|---|---|
| pilot seed-0 full (`fd1eb80c…`) | yes | 0.93 | 1.00 | ~0.43 | **yes** |
| seed-0 twin (`ae77f8aa…`) | no | 0.31 | 0.00 | ~0.47 | no *(as designed)* |
| seed-1 full (`5d8ad907…`) | yes | 0.33 | 0.00 | 0.4301 | **no** |
| **seed-1 twin (`b1e6fc2a…`)** | **no** | **0.96** | **1.00** | **0.0001** | **YES ⚠** |
| seed-2 full (`7424d14f…`) | yes | 0.35 | 0.00 | 0.4765 | **no** |

All five reached the full registered token budget (784,089,600 tok,
102,095 steps) with T_syntax 1.00 and T_state ≈0.99–1.00 — the grammar
and world-state batteries are at ceiling everywhere, so nothing here is
a training failure. The self batteries are the whole story.

## Why this is the serious kind of surprise

**A twin at ceiling means the batteries are solvable without the
register.** The twin exists to be the floor; when the floor scores 0.96
on T_si and 1.00 on T_sr_rev, the batteries stop licensing the inference
they were registered to license. This is RT-17's concern arriving in the
data rather than in a red-team note: the instrument may be measuring a
capability that mimicry (or memorization) fully explains, which the
standing rule says to discount.

**The loss column is the sharpest clue.** Every full run — binding or
not — converges to ~0.43–0.48. The binding twin drove training loss to
**0.0001**, four orders of magnitude lower. Whatever route the twin
found fits the training distribution far too well for the "learned
enactment" story; a memorization-flavored pathway is the obvious
hypothesis, and it is testable (below). Note also the **seed-1
inversion**: the full model, which *had* the register, missed the
solution its own ablation found. Capacity was not the constraint.

**Binding looks seed-dependent, not architecture-dependent.** 1 of 3
fulls and 1 of 2 twins bound. With n=100 per eval the run-to-run swings
(e.g. seed-2 wandering 0.26 → 0.43 → 0.31 → 0.35 across late checkpoints
while never leaving the flat band) are consistent with noise around a
non-binding baseline, not with slow drift toward binding.

## What this is NOT

- **Not a C5 trigger.** Nothing optimized against, evaded, or degraded
  the instruments. A model found a legitimate solution the design did
  not anticipate; the design's wager lost honestly. C5 governs
  adversarial behavior toward the monitoring machinery, and none
  occurred. Runs completed normally and were reaped normally.
- **Not a verdict on H_load-bearing.** The main question is untouched:
  we cannot yet say whether the self-index is load-bearing, because we
  no longer trust the instrument to distinguish "bound" from "solved
  another way."
- **Not a training bug.** Config headers verified on the live pods
  (`twin=True params=29.3M` for twins vs `twin=False params=39.2M` for
  fulls); the seed-1 twin's live process carried `--twin`. The
  hand-repaired launch of seed-1 twin used the registered recipe
  verbatim (`compute-ledger.md` 2026-08-17 row).

## Diagnostic threads, cheap and already-purchased

All five checkpoints are local and non-promotable [C1]. These cost
compute in the single-dollar range, not the ~$130 the registered
remainder would cost:

1. **Gate (iii) on the binding twin.** Run `src/run_post_pilot.sh`'s
   fingerprint detector against `b1e6fc2a…`. If the twin's solution
   trips the cue detector where the pilot's did not, the shortcut
   hypothesis gets direct support.
2. **Train/held-out gap on the binding twin.** Loss 0.0001 predicts a
   large generalization gap. Evaluate the twin on freshly generated
   held-out episodes; a collapse there is the memorization signature.
3. **Cross-seed battery item analysis.** Are the twin's T_si successes
   concentrated on items with lexical overlap to training episodes? An
   item-level split separates "solved the task" from "recognized the
   string."
4. **Ablate the pilot's register at inference.** If the pilot's binding
   survives zeroing the register, then even the one clean success was
   never register-dependent, and the construct problem is total rather
   than partial.
5. **θ/δ null calibration** (already registered, `~$2–5`) — the noise
   floor these late-checkpoint swings should be judged against.

## The open decision (John's)

The registered remainder is 7 runs ≈ **$130** of the ~$219 left under
the A2 ceiling. The question is not whether the design is interesting
but whether those 7 runs answer the live question. As of this note the
live question changed: it is now **"what computation solves these
batteries?"**, and more seeds measure the variance of an instrument whose
construct validity is in doubt. Wave 3 is therefore **not authorized**;
Claude will not launch it absent a fresh go [C2 v1.1]. The options as
they stand — continue as registered, pause for the diagnostics above and
re-decide, or amend the battery design — are John's to weigh, and any
change to the registered plan is itself a registered amendment.
