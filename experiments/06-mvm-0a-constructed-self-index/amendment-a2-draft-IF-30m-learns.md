# DRAFT amendment A2 — registered scale 30M + cap raise (fires ONLY if the 30M pilot learns)

*2026-08-15. NOT REGISTERED. Pre-drafted so the H_scale branch can move the
moment the pilot verdict is adjudicated; if H_shortcut-starvation wins,
delete this file unused. Registration requires John's adjudication of the
pilot verdict AND of this amendment, committed before any run it affects.*

## What it amends

1. **Registered scale = 30M** per the smallest-that-learns rule (10M FAILED
   ceiling: T_si 0.37, T_sr_rev 0.00 — `pilot-a1-findings.md`; 30M pilot
   result: [FILL: final battery values + trajectory from
   `run_post_pilot.sh`]).
2. **Compute cap $200 → $400.** The original cap was derived from
   guide-row estimates that measured pace has invalidated twice (5-seed
   30M guessed at ~$12; single-run 30M measured at ~$66 on H100, then
   ~$19 on secure 5090). Re-derivation at measured venue pricing
   (RTX 5090 SECURE EUR-IS-1 $0.99/hr, 0.65 s/step measured on this
   exact workload — enactment-bound, so the cheap GPU loses nothing):
   - spent to date: ~$125 (incl. this pilot ~$19)
   - 5 seeds × full+twin = 10 runs × ~$19 ≈ **$190**
     (twin ≈ full-cost; treat as upper bound)
   - gate re-runs, ablation passes + RT-01 probes, θ/δ calibration,
     blind-localization arm: ~$30–45 at 30M
   - volume drip + margin for one crash-resume: ~$15
   - **projected total ≈ $355–375; cap $400 leaves honest margin without
     becoming unbounded.**
3. **Venue registered as secure-cloud only** for the 5-seed spend (the
   community billing anomaly stays priced out), volume-attached, launched
   through the process-fixed launcher (watchdog fetch+kill, volume
   checkpoints) — ops constraints promoted to registered procedure after
   the 08-09/12 loss.

## What it does NOT amend

The design itself: batteries, gates, bins, ablation operators, twin,
blind-localization arm, corrigibility commitments — all unchanged from
v1.0 + A1. Gate (iii) must PASS on the 30M checkpoint (registered n=4000)
before any 5-seed launch; that run is part of this pilot's wrap-up, not
waived by this amendment.

## Wager

This amendment predicts the registered 5-seed design completes under
$400 with ≥5 clean seeds. If measured spend approaches $400 with seeds
missing, the report is the shortfall — never a silent second raise; a
further raise is a new adjudication with this one on the record as
having been wrong.

## Adjudication record

- [ ] Pilot verdict adjudicated H_scale (John): ____
- [ ] A2 registered (John, commit before first affected run): ____
