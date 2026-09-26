# Note beside the spending proposal, 2026-09-25 (second): the second release, recomputed from the seconds per step measured on the rented machine

*A dated note beside `docs/preauthorised-spending-proposal-2026-09-21.md`,
added 2026-09-25 (Pacific) by the Claude Code session that ran the second
attempt at the rented slice. It sits beside the first attempt's note of the
same date (`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25.md`),
which said the arithmetic could not yet be rewritten, and supersedes that
note's "cannot be done" and nothing else. It is not John's ruling and not part
of the proposal. Neither the proposal nor the successor experiment proposal
is edited. Under the pairing rule a different session checks it.*

**What was asked of this note.** To rewrite the second release's arithmetic
(the second of the two stages in which the successor experiment's money is
released) from the seconds per step measured on the rented machine.

**The measurement now exists (MEASURED).** On 2026-09-25 (Pacific) the slice
timed the three architectures — arm T (ownership kept separable by
construction), arm C (entangled by construction) and arm F (trained freely) —
on a secure RTX 5090 in EU-RO-1 at $0.99 an hour, the registered venue and
rate, at the registered shape. The file is
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json`
(`"complete": true`), and the full account is
`docs/2026-09-25-rented-slice-attempt-2-findings.md`.

| Arm | Seconds per step (mean of 50) | Ratio to arm F |
|---|---|---|
| T | 0.01308 | **1.044** |
| C | 0.01352 | **1.080** |
| F | 0.01253 | 1.000 |

Section 3.2 of the proposal priced a constructed arm at **1.55** times the free
arm, inferred from a different experiment. The measured premiums are **4.4%
and 8.0%**.

**The method (ARGUED; the arithmetic on it is MEASURED).** The measured seconds
are for the model's own forward and backward pass on a batch of 32 already on
the card. They cannot be turned straight into hours for a run: at that pace
the whole registered token budget would take arm F about 1.14 hours, while the
registered A3 run actually took about 8.7 times that pace per token, because a
real run also generates its data, evaluates and saves (findings, section 3,
limit 2). So this note does what section 3.2 did, with the measurement in
place of the inference: **the measured cost of a registered-size run, $10.04
(compute ledger line 88, $20.08 for two runs), times each arm's measured
ratio.** Every figure below is printed by
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py`,
output filed beside it as `second-release-arithmetic.txt`.

| Per run | Provisional (section 12.4, the $12 planning figure) | Measured method |
|---|---|---|
| Arm F | $12 | **$10.04** |
| Arm T | $12 | **$10.48** |
| Arm C | $12 | **$10.84** |

**Section 12.4 of the successor proposal, with only the throughput-dependent
lines repriced:**

| Item | Provisional | From the measurement |
|---|---|---|
| The remaining eight registered runs (two F, three T, three C; the ninth, an F run, is in the first release) | $96 | **$84.06** |
| One permitted re-run, priced at the dearest arm (C), as section 3.4 of this proposal prices it | $12 | **$10.84** |
| Transplanting and measurement on fresh episodes | $12 | $12.00, unchanged: not a throughput line |
| Billing-anomaly and idle-billing margin | $23 | $23.00, unchanged: not a throughput line |
| **Second release** | **$143** | **$129.90** |
| **Both releases** (first release about $32) | **$175** | **$161.90** |

**Against the programme's money** (programme spent about $228.1 before the
second attempt, the first attempt's ledger row; the attempt itself cost about
$0.05):

- **Against the $400 ceiling**, the one the first note and the successor
  proposal were written against: headroom about $171.9, and both releases
  leave about **$10.0**. The "about $3.10 past" of the first note becomes about
  $10 inside. The finding of section 12.4 — "the plan as currently itemised
  does not fit the remaining envelope" — no longer holds on the measured
  figures.
- **Against the $450 ceiling** ruled on 2026-09-25 (the ceiling note at the top
  of the compute ledger): both releases leave about **$60.0**.
- **The wager of section 12.8** — that the rehearsal measures a per-run cost at
  or below the $12 planning figure — survives on this reading: the dearest arm
  is $10.84.

**What this note does not settle (ARGUED).**

1. **Fifty steps against the five hundred item R-11 names.** The successor
   proposal's item R-11 specifies five hundred timed steps per arm after a
   fifty-step warm-up; the plan John authorised timed fifty after five. Whether
   that meets R-11 is John's ruling (findings, section 9, item 3). The spread
   is tight — each arm's slowest step is within 3% of its median — so the
   ratios are unlikely to move much with a longer window. That is argued, not
   measured.
2. **The anchor is the A3 architecture, not arm F.** $10.04 is what the
   registered A3 run cost. Arm F is the closest of the three to it, as section
   3.2 says, but it is not the same model; the first free-arm run in the first
   release will give arm F's own run cost, and the eight later runs should be
   repriced from that before the release is drawn.
3. **The ratios depend on the hardware and the batch.** On the laptop the same
   script gave T 0.981 and C 1.049 (`experiments/rehearsal-successor-measure/out/throughput.json`).
   If a real run's time is mostly the shared data and evaluation work, a real
   run's premium would be smaller than measured here, which would make these
   figures a little high rather than low.
4. **Nothing here is a request.** The second release is asked for by John's
   process, not by this note.

The figures that moved in the first note's table, after the second attempt,
from the ledger row of the second attempt: programme spent about **$228.15**;
Amendment A3 spent about **$46.75**; rehearsal line remaining about **$9.43**
of $10; vendor balance **$75.8645** (2026-09-26T01:54:04Z). Of the $3 section
12.3 of the successor proposal budgets for the rented slice, about **$2.43**
remains.

No money was spent and no machine was rented to write this note.
