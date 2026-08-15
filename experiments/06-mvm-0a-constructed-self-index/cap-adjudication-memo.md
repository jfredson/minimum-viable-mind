# Cap adjudication memo — can the registered design finish under $200?

*2026-08-15. Decision-memo pattern (constraint set → candidates → derivations →
one recommendation). Advisory only; John adjudicates. Prompted by the ledger's
2026-08-12 flag: the phase-budget guide priced the 5-seed 30M run at ~$12, but
the measured 30M pilot pace says a single 30M run costs ~$66 — the registered
design does not fit the remaining cap, and the registration (v1.0 §Materials)
makes the $200 cap binding. STATUS open item #4.*

## Constraint set

1. **The $200 cap is registered.** Exceeding it requires a registered
   amendment committed before the runs it affects — never a silent overrun.
2. **Ledger state (console-reconciled 2026-08-12):** spent **$105.62**,
   remaining under cap **$94.38**. Account balance $23.94 (2026-08-15) —
   balance is a funding question, not a cap question; the cap counts spend.
3. **Measured prices.** H100 SXM secure $3.29/hr; 30M pace 0.70 s/step at
   83% util → ~20h to the 784.08M-token budget ≈ **$66/run**. (The lost
   pilot billed 29.5h = $97, but ~9.5h of that was post-completion idle +
   overrun — eliminated by the new watchdog fetch-and-kill.) Community 5090
   $0.69/hr → 32–44h ≈ $22–30/run nominal, with the documented unexplained
   ~3.5× billing anomaly (2026-08-08, ticket waived) as priced risk →
   $77–105/run worst case, and 32–44h of unattended exposure per run.
4. **The ladder is not settled.** The 30M pilot re-run decides
   H_scale vs H_shortcut-starvation. If shortcut-starvation wins, the
   ladder stops by registered rule and **the 5-seed spend never happens**.
5. **Registered design remainder if 30M learns:** gate (iii) re-run at 30M
   (~$1–3), 5 seeds × full+twin = 10 runs, then ablation/RT-01 probes +
   θ/δ null calibration + blind-localization arm (guide $9–15 at 10M;
   scale to ~$15–40 at 30M).

## Derived costs of "everything" at 30M

| venue | pilot re-run | 5-seed (10 runs) | gates+ablation+calib+blind | total remaining | total project spend |
|---|---|---|---|---|---|
| H100 secure | ~$66 | ~$600–660 | ~$20–45 | **~$690–770** | ~$795–875 |
| 5090 community (nominal) | ~$25 | ~$220–300 | ~$20–45 | ~$265–370 | ~$370–475 |
| 5090 community (3.5× anomaly) | ~$88 | ~$770–1050 | — | ~$860–1140 | ~$965–1245 |

No candidate fits $94.38. The pilot re-run alone **does** fit (~$66,
leaving ~$28) with no amendment needed.

## Candidates

- **(A) Sequence-first: spend only the pilot now; adjudicate the 5-seed
  cap after its result.** No amendment today. If H_shortcut-starvation
  wins, the cap question dissolves — the ladder stops, the ~$28 remainder
  funds the wrap-up analysis, and the finding goes upstream. If H_scale
  wins, open the cap amendment with a measured, checkpoint-in-hand number.
  Cost of waiting: zero (nothing else is runnable first anyway).
- **(B) Cap-raise amendment now** (e.g. $200 → $900 for H100 5-seed, or
  → $500 for community-nominal / 3-seed-H100). Pre-commits the money
  before knowing whether the 5-seed runs at all; buys nothing the pilot
  result wouldn't buy better-informed.
- **(C) Venue amendment: 5-seed on community 5090.** Nominal ~$250–300 but
  carries the unexplained 3.5× anomaly as open risk and 13–18 days of
  serial wall-clock (or parallel pods × anomaly exposure). The watchdog
  mitigates the unattended-pod failure mode, not the billing one.
- **(D) Seed-reduction amendment: 5 → 3 seeds** (6 runs, ~$400 H100 total
  remaining). Weakens the registered across-seed CI story the design was
  written around; only worth pricing if (B)'s number is refused.

## Recommendation

**(A) sequence-first**, with the amendment decision explicitly deferred to
the pilot verdict. Wager form: if the 30M pilot reproduces the 10M
signature (T_si stuck at floor, T_sr_rev 0), the 5-seed money was never
needed and pre-committing it (B) would have been pure downside; if 30M
learns, the amendment gets written against a measured cost, not a guide
row that has already been wrong by 8×.

**Funding consequence (John's action, not a cap action): top up $75 now**
→ balance ~$99, covering the ~$66 pilot + volume drip + gate (iii) +
margin for one crash-resume day, all inside the existing cap. Do **not**
pre-fund the 5-seed; that money moves only if H_scale wins and the cap
amendment is registered (then: ~$650–750 more for H100 5-seed, or
~$250–350 community, John's venue call at that point).

## Adjudication record

- [ ] John adjudicates: A / B / C / D / other — date, notes.
