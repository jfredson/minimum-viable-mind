# Re-check: the spending-alarm fixes, second round (pull request 116)

*2026-10-06 (Pacific). Same checker as the first round (pull request 117),
which wrote none of pull request 116. Method committed first:
`docs/2026-10-06-tripwire-fixes-recheck-method.md`. Cost: $0. Nothing rented;
no call to the vendor's service. Outputs:
`experiments/08-successor-degree/tests/check-of-116/round2/` and the
`recheck_*` files beside it.*

## Verdict

**Not ready to merge yet. Safe for the approved $1.14 reruns, under the
operator rules.**

The substance is fixed. The three false "not found" answers no longer disarm
the deadline timer, both lost writes now survive, and the three rulings are
carried out as ruled. Two things stand in the way of merging:

- pull request 116's own check fails in 6 of 8 runs here, on timing;
- an honest short machine can now be halted as "cannot be checked yet",
  because the watchdog's deletion time reaches the alarm only after the
  stricter confirmation (problem 2 below).

Neither can spend money. Both are small fixes.

## Each first-round finding

| First-round problem | Now | How it was checked |
|---|---|---|
| 1. Any "not found" disarmed the timer | **Fixed.** The first check's script, unchanged, now leaves the timer armed for the 404 page, "command not found" and the configuration message. A second script with a stand-in machine list shows the timer stands down only on the vendor's phrase "pod not found" plus "(status 404)" **and** a good list without the machine, at two checks in a row. It stays armed if the list fails, shows the machine, or is not a list | `not_found_wording.sh` (unchanged), `recheck_timer_genuine.sh` |
| 2. The watchdog's record followed a failed read | **Fixed** for the record file: it now needs two good machine lists without the machine, 5 minutes apart. Their cases W1 to W7 pass, and reading the code agrees | code reading; their W cases |
| 4. Simultaneous writes lost | **Fixed.** Both of the first check's race cases now survive. Every load-change-save is under one file lock, vendor reads stay outside it, and no locked block is nested inside another | `shared_records_race.py` (unchanged) |
| 7. Flaky timing test | **Not fixed.** See problem 1 below | 8 full runs |
| 8. Wrong description | **Fixed.** Pull request 116's description is now its own | read |

## The three rulings

- **Bills below 0.90 of life are "cannot be checked yet":** carried out
  (`BILL_COMPLETE_MIN`, a halt naming the machine). Exactly 0.90 passes;
  0.899 trips; 3.5 times still trips as overbilling.
- **The 3-hour rule, written only:** carried out. It is in the launcher's
  header notes and the alarm's notes, with "never reuse a wave name" and "do
  not top up". The launcher's example no longer names `dev-10m`. It is
  written, not printed at launch, which is what was ruled.
- **A top-up restarts the in-flight comparison, logged, not a trip:**
  carried out (`segment`, `note_rise`, "restarts" in the records). The
  comparison restarts at the *last* rise and predicts from 15 minutes
  before it.

## Order of the work

Each round's method commit came first and touched only the method note:

- first round: `e54ecf6` (method), then `a3fc51f` (code);
- corrections: `de5f0c2` at 21:07:38 (method), then `46f561e` at 21:14:07
  (code);
- rulings: `00b468f` at 21:15:58 (method), then `63ed527` at 21:17:39 (code).

The rulings' code (about 160 changed lines with tests) came **1 minute 41
seconds** after its method. So git shows the order, but it cannot show that
the expected figures were fixed before the code was drafted. The method
says they came from a separate scratch calculation, which is consistent.
That code commit also *added* to the method (sections 12.5 and 12.6) without
changing any expectation.

Section 12.5 reports a first-run failure (B3, a bill of exactly 0.90
tripping on rounding). Unlike the first round, that failing output was not
kept: only the final run is committed (`001b786`). This is minor, but it
breaks the first round's own practice.

## Problems, most serious first

### 1. Pull request 116's own check fails in most runs (blocks merge; test only)

Over eight full runs of `tests/check_tripwire_fixes.py`, six failed. In
four of them only the builder's own "five runs in a row" check failed (17,
18 or 19 of 20 timing cases passed). In the other two, individual timer
cases also failed: N4 and N8 in one, N6 in the other (that run ended 18
seconds after the deadline). Five runs were alongside other test suites; the
three run afterwards all failed too.

The cause is the timing allowance. Each vendor check now makes two capped
calls (`pod get`, then `pod list`) plus a Python start. So the timer can
pass its deadline by up to **twice the cap plus one poll**, not "the cap plus
3 seconds" as the tests assume. With the real settings (20-second cap,
30-second poll) the deadline can slip by up to about 70 seconds, about 2
cents at $0.99 an hour. The money is trivial. But the code comment "a hung
read cannot hold the deadline back by more than the cap" is no longer true.

**Fix:** allow two caps plus a poll in the tests, and correct the comment;
or skip the vendor check when the deadline is less than two caps away.

### 2. An honest short machine can be halted as "cannot be checked yet" (should fix; safe direction)

The 0.90 line divides billed time by the life in the alarm's records. That
life ends at the recorded deletion time, or, if none was recorded, at the
first reading that no longer listed the machine (an "inferred" deletion,
up to one 5-minute reading late).

The vendor bills from creation, start-up included: the first 2026-09-25
machine billed 1,871.9 s against 1,873 s by the laptop's clock. So billing
from start-up rather than creation is *not* the risk. The laptop records
creation slightly late, which pushes the comparison up, the safe way. The
risk is a late deletion time (`recheck_topup_and_bills.py`, part b):

| life | deletion 12 s late (the watchdog's own time) | 300 s late (inferred) |
|---|---|---|
| 10 min | 0.980 | **0.667, trips** |
| 20 min | 0.990 | **0.800, trips** |
| 30 min | 0.993 | **0.857, trips** |
| 45 min | 0.996 | 0.900 (just passes; 330 s trips) |
| 60 min | 0.997 | 0.923 |

The change in this round makes an inferred time more likely. The watchdog
now writes the deletion time into the alarm's records only after its two
machine lists 5 minutes apart succeed. If either list read fails, the alarm
keeps only the inferred time. The "found gone" path never writes one.

The reruns and the development runs are 20-to-30-minute machines. Each such
miss means a halt, John's attention, and a clear. It never means spending.

**Fix:** write the alarm's deletion time straight after an accepted delete,
as in the first round. A wrong time there only makes the alarm read high, the
safe way. Keep the two-list confirmation for the timer's record file only.
Also, for an inferred deletion, judge the 0.90 line against the last
reading that still listed the machine, and keep the inferred time for the
1.25 line.

### 3. "Not listed" means "not running", not "does not exist" (minor)

The vendor tool 2.6.1 `pod list` shows **running machines only** unless
given `--all` (`cmd/pod/list.go`: "default: running only"). A stopped machine
still exists and still bills its disk.

The timer cannot stand down on that alone, because it also needs `pod get`
to say "pod not found (status 404)". The watchdog's record, however, rests on
an accepted delete plus two lists without the machine. A machine the vendor
stopped instead of deleting would pass. That costs storage only, cents an
hour, not the card.

**Fix:** use `pod list --all` in both list checks, so "omitted" means "does
not exist".

### 4. The top-up allowance: what it misses (as stated by the builder; acceptable)

I drove the alarm itself (part a): a reading every 5 minutes, charges posted
late in 5-minute steps, and a $75 top-up at minute 13.

- **Honest waves never trip.** I tested lags of 0, 6.5 (the lag recorded
  on 2026-10-04), 8, 12, 15 and 20 minutes, with one machine of 40 or 120
  minutes and with four machines.
- **What it misses after a top-up:**

  | overcharge | 40 min | 60 min | 120 min | 240 min | 480 min |
  |---|---|---|---|---|---|
  | 1.3 times | missed | missed | missed | trips at 256 | trips at 461 |
  | 1.4 times | **missed** | trips at 76 | trips at 131 | trips at 171 | trips at 171 |
  | 1.5 times | trips at 56 | trips at 76 | trips at 111 | trips at 111 | trips at 111 |
  | 2 times | trips at 51 | trips at 51 | trips at 51 | trips at 51 | trips at 51 |
  | 3.5 times | trips at 31 | trips at 31 | trips at 31 | trips at 31 | trips at 31 |

  Four 60-minute machines at 1.4 times trip at minute 76.
- **Without a top-up,** a 1.4-times overcharge on a 40-minute machine trips
  at minute 56. So the top-up's real cost is mild overcharges (about 1.4
  times or less) on waves under about an hour. The stated cost ("can miss a
  mild one on what is left of the wave") is accurate, and slightly
  pessimistic for longer waves.
- **The end-of-wave comparison of billed hours is unaffected by a top-up.**
  It still catches an overcharge in billed hours, the 2026-08-08 kind. It
  cannot see a higher price per hour, but it never could.

The look-back is 15 minutes against a recorded lag of about 6.5. So up to
8.5 machine-minutes already paid before the top-up are predicted again,
which reads a little low. That is the price of tolerating lags up to 15
minutes. With "do not top up during a wave" as the operator rule, no change
is suggested.

### 5. The timer's stand-down is now 5 to 10 minutes after deletion (acceptable)

- **By the vendor's word:** two checks 5 minutes apart, the first up to 5
  minutes after deletion.
- **By the watchdog's record:** written after its 5-minute second list,
  then seen by the timer within 30 seconds.

So the timer stands down 5 to 10 minutes after a deletion. If a machine is
deleted less than about 10 minutes before its deadline, the timer still
fires. It tries to delete a machine already gone, the vendor answers "pod
not found", and the timer prints its "FAILED … may still be billing" line.
That line is the older finding B, still open by ruling. It costs nothing.
With caps of $2.50 against machines of about 25 minutes this does not arise
in the reruns.

### 6. Can the timer stand down while a machine still bills? (d)

I read every path.

- **The vendor's word:** needs `pod get` to answer "pod not found" with
  "(status 404)", and two good lists without the machine. A machine that
  exists does not answer 404.
- **The watchdog's record:** needs an accepted delete or that same answer,
  then two good lists without the machine, 5 minutes apart. The record file
  is written only by the watchdog and names the machine. Machine ids are not
  reused.

The only gap left is problem 3: a machine stopped rather than deleted, which
bills disk only. **No path remains by which the timer stands down while the
card is billing**, short of the vendor both accepting a delete it did not
carry out and dropping a running machine from its running list.

Still unrecorded: what `pod get` really answers for a deleted machine. If it
is not "pod not found … (status 404)", the vendor's-word route never fires
and the timer relies on the watchdog's record. That is the safe direction.
Recording it at the next paid deletion is still worth doing (a free read).

## Tests re-run

- **Pull request 116's own check:** 8 runs; 2 pass, 6 fail on timing
  (problem 1).
- **The alarm's self-test:** passes.
- **Experiment 06 self-tests:** deadline timer 20 of 20, watchdog handshake
  26 of 26, launch gate 369 of 369, sleep guard 67 of 67.
- **The successor launcher check:** passes.
- **The successor self-test suite:** 200 of 200, "ALL SELF-TESTS PASS".
- **The first round's two scripts, unchanged:** all three false answers now
  stay armed; neither write is lost.

## For the $1.14 reruns

Safe to rely on, with:

- a new wave name;
- no top-up while they run;
- the end-of-wave comparison run no earlier than 3 hours after the last
  deletion;
- someone watching.

If that comparison halts with "cannot be checked yet" on a machine whose
deletion the alarm only inferred (its records say `gone_inferred`), that is
problem 2, not a partial bill. Tell John so; he decides.
