# Week-37 spend review (verification only), run 2026-09-16 Pacific

*Scheduled for 2026-09-13, run three days late by a Cowork session. Governed by Amendment A2's
addendum in `experiments/06-mvm-0a-constructed-self-index/pre-registration.md`: reconcile spend,
check the amendment's wager, record the repeated-sampling outcome. No revision is permitted here
and none is proposed. Sources: `compute-ledger.md` on branch gate0-null-calibration at 5dedc18,
and the TimeAssembler decision of 2026-08-30 (the $400 ceiling covers all MVM compute across
every vendor; true spend then about $281 to $300).*

## 1. Did the $400 ceiling hold? YES.

| line | amount |
|---|---|
| All-vendor true spend at the 2026-08-30 ruling | $281 to $300 |
| of which RunPod per the ledger reconciliation that day | about $191.3 |
| of which Stage 3 Gemini arm | $49.77 |
| A3 learnability pilot (2026-09-15/16) | $13.92 |
| A3 self-terminate ops test (2026-09-16) | $0.29 |
| RunPod volume drip 2026-08-30 to 2026-09-16, about $0.59/day (balance $142.64 on 2026-08-18 to $126.05 on 2026-09-15) | about $10 |
| **All-vendor spend today, before the seeds wave** | **about $305 to $324** |
| A3 seeds 1 and 2, in flight, ledger estimate | $18 to $26 |
| **Projected after the wave** | **about $323 to $350** |
| **Headroom under $400 after the wave** | **about $50 to $77** |

A3 cumulative against its own $100 hard stop: $14.21, projected $32 to $40 after the wave.

## 2. The A2 wager: LOST, already on the record.

A2 projected $355 to $375 for five seeds of full plus twin, finishing under $400. The 5-seed run
was halted at 4 of 9 launches (ruled 2026-08-30) and closed under A3; the 2026-08-31 worklog
finding is that the halted remainder would have breached $400 under any reading. Nothing to add.

## 3. Repeated-sampling outcome: DOES NOT FIT, goes unrun under this cap.

It was fundable only from GPU-side underspend. The Stage 3 Gemini arm cost $49.77 for 31 of 360
subjects, roughly $580 at that rate for the full grid, against headroom of $50 to $77. A3's $100
stop also outranks its claim (ratified A3 ruling). Per the pre-committed consequence clause, the
publication states what was not run and why; the alternative route is a new pre-registration
with its own cap.

## 4. Consequence for the 2026-09-20 extra-seeds decision

STATUS prices seven total seeds at $77 to $105. After seeds 1 and 2 the all-vendor headroom is
$50 to $77, so the full seven do not fit under $400 even though they fit under A3's $100 stop.
At about $11 per register-less run plus drip, roughly three to five extra seeds fit. The $400
binds before the $100 does.

## 5. Open for John (the one part an agent cannot do)

Rule 4 console reconcile: RunPod console, Billing, confirm lifetime spend agrees with the ledger
within a dollar, after the seeds wave reports. Rows since 2026-08-15 are balance-implied, not
console-read. The non-RunPod share of the $281 to $300 figure is not itemized in the repo; if an
itemization exists only in the 2026-08-30 worklog entry, copy it into the ledger.

## 6. Console reconciliation (added 2026-09-16 Pacific, from John's RunPod billing exports)

*Source: four CSV exports John pulled from RunPod console, Billing, covering 2026-06-01 to
2026-09-16 UTC (summary monthly, summary daily, GPU daily, CPU daily). First billed day is
2026-07-12. The 2026-09-16 UTC row does not include the seeds 1 and 2 wave, which launched at
03:11Z on 2026-09-17. This section supersedes the estimates in section 1.*

**Rule 4 (console agrees with the ledger within a dollar): PASSES.**

| check | console | ledger | gap |
|---|---|---|---|
| Rows through 2026-08-11 (GPU) | $105.623 | $105.62 | $0.00 |
| 2026-08-15 to 2026-08-18, re-run plus waves 1 and 2 (GPU + storage) | $76.88 | $76.30 balance drop ($98.94 + $120 top-up to $142.64) | $0.58, whole-day storage at the window edges |
| same window, pod hours | 75.55 h | 75.91 h | 0.36 h |
| 2026-09-16, A3 pilot plus ops test (GPU) | $13.61, 13.75 h at $0.99 | $14.21 balance-implied, includes about $0.6 storage | $0.00 |
| Through 2026-08-30, the day of the all-vendor ruling | $191.77 | "about $191.3" (worklog 2026-08-30) | $0.47 |

**One structural finding: the ledger's running total is not RunPod's true spend.** The ledger
reads about $195.6; the console reads **$215.33** since 2026-08-07 (GPU $194.03 + storage
$21.31). The $19.7 difference is network-volume storage billed on days with no pod, which has
no ledger row. Nothing is unaccounted, but the running-total column should not be read as the
number that counts against $400.

**Exact figures, replacing section 1:**

| line | amount |
|---|---|
| RunPod all-time, 2026-07-12 to 2026-09-16 UTC | $258.18 |
| of which before the ledger opened (2026-07-12 to 2026-08-06) | $42.85 |
| of which ledger era | $215.33 |
| Stage 3 Gemini arm | $49.77 |
| **Known all-vendor spend** | **$307.95** |
| Other API spend (judge calls), not itemized anywhere; the 2026-08-30 range allows up to about $18 | $0 to $18 |
| **All-vendor spend before the seeds wave** | **$308 to $326** |
| Seeds 1 and 2, ledger estimate | $18 to $26 |
| **Projected after the wave** | **$326 to $352** |
| **Headroom under $400** | **$48 to $74** |

Reconstruction note: $42.85 + $191.77 + $49.77 = $284.4 on 2026-08-30, inside the ruling's $281
to $300. The itemization is this review's reconstruction; the ruling gave only the range.

**Storage is now the largest standing draw on the headroom.** Two network volumes bill $0.583
per day, about $17.50 per month, with or without a pod. From 2026-09-17 to the 2026-11-22
public release that is about $39, which is most of the low-end headroom and would leave room
for roughly one to three extra seeds, not three to five. Decision for John, after the wave
reports and every checkpoint is confirmed local with its md5: whether `mvm-models` (150 GB,
EUR-IS-1, about $0.35 per day, unused since the venue moved to EU-RO-1 on 2026-08-16) can be
deleted. Not recommended before that confirmation.
