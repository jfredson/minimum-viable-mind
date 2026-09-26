# Note beside the spending proposal, 2026-09-25: the second release's arithmetic still cannot be rewritten

*A dated note beside `docs/preauthorised-spending-proposal-2026-09-21.md`, added
2026-09-25 (Pacific) by the Claude Code session that ran the rented slice. It is
not John's ruling and not part of the proposal. The proposal is not edited. The
same practice as the proposal's own two notes applies: a superseded figure gets a
dated note, never a rewrite.*

**What was asked of this note.** To rewrite the second release's arithmetic (the
second of the two stages in which the successor experiment's money is released)
from the seconds per step measured on the rented machine.

**Why it cannot be done.** The slice ran on 2026-09-25 and was stopped before its
timing step, so **no seconds per step were measured** on the rented card. The
full account is `docs/2026-09-25-rented-slice-findings.md`. The launcher hung
while starting the machine's own shutdown watcher, and the session stopped the
run, as the go instructed, on the first difference from the plan. Two documents
bind the release to that measurement:

- item 11 of `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`:
  "The second release is requested only after the week-40 rehearsal has measured
  seconds-per-step for all three arms";
- section 12.4 of `docs/successor-experiment-proposal-2026-09-21.md`: "If item
  R-11 does not produce them, the second release is not asked for at all."

So no second-release figure is written here. Any figure would rest on the
inference both of those documents refuse.

**The figures that did move**, all drawn from
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, the 2026-09-25
`slice_handshake` row:

| Measure | Before the slice | After it |
|---|---|---|
| Programme spent (envelope $400) | about $227.6 | **about $228.1** |
| Programme headroom | about $172.4 | **about $171.9** |
| Amendment A3 spent (stop $100) | about $46.2 | **about $46.7** |
| Rehearsal line of the first release (up to $10) remaining | about $9.98 | **about $9.48** |
| Vendor prepaid balance | $76.4527 (2026-09-25T23:45:19Z) | **$75.9553** (2026-09-26T00:22:10Z) |

**The knock-on figures, worked out here:**

- **The two releases against the headroom.** The proposal's second note had the
  first release (about $32) plus the provisional second (about $143) come to
  about $175. That was about $2.60 past a headroom of $172.40. Against about
  $171.9 it is now about **$3.10** past. It is still the proposal's open
  question, and it still waits on the measurement.
- **The rented slice's own budget inside the rehearsal line.** Section 12.3 of the
  successor proposal budgets **$3** for rehearsal item R-11 (the rented slice).
  About $0.02 on 2026-09-21 and about $0.50 today leave about **$2.48** of it. A
  second attempt at the plan's estimate ($0.75 to $1.00, hard cap $2.00) fits
  inside that, even at its cap. That second attempt needs John's fresh go, and a
  fixed launcher (findings, section 7).

Every figure above comes from the compute ledger named above. No money was spent
and no machine was rented to write this note.
