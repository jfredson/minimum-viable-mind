# Method: four ruled fixes to the spending alarm and its helpers

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree
(`~/Code/mvm-tripwire`, branch `tripwire-fixes`), **before any code was
changed**. It states what will be changed, the numbers the new rules use and
why, and the outcome every test is expected to give, so the results can be
held to what was written here first. Cost: $0. Nothing is rented, no paid
call is made, and every test talks to a stand-in for the vendor's command-line
tool, never the vendor.*

## 1. What John ruled, and where it comes from

The source is page 2 of the ruling packet on the two built models that lost
their ownership route (`docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`,
branch `ruling-packet-cm-flat`, pull request 109), which rests on the
independent check of the four 10-million-parameter development runs (pull
request 106, branch `check-dev-10m`). John ruled on 2026-10-06:

1. **Read during each wave.** The spending alarm ("tripwire") reads the vendor
   balance every few minutes while machines run, with a rule that can act on
   less than an hour of readings, plus a comparison at each machine's
   deletion. This **amends version 4 of the successor proposal, section 12.5**,
   which registers "hourly". The amendment is noted here for version 5
   (section 7 below); version 5 is not written by this work.
2. **The step that deletes a machine writes the deletion time into the
   alarm's records.** In the development run the alarm learned of the four
   deletions only at its next hourly reading, charged all four machines as if
   they had run until 01:11, and reported spending at 0.40 of the posted rate
   where the true figure was 0.99.
3. **Empty, not-yet-posted bills count as "cannot be checked yet", which is a
   trip** (version 4, section 12.7: a check that cannot run is a trip).
4. **Each laptop deadline timer stops itself only on a confirmed deletion:**
   the watchdog's own "machine gone" record, or the vendor saying the machine
   does not exist. Never on a failed or empty reading. The timer
   (`machine_deadline.sh`) deletes a machine when it reaches its spending cap
   and is the last line of defence on cost.

## 2. Terms used below

- **The alarm**: `experiments/08-successor-degree/src/tripwire.py`. It keeps a
  record folder per wave (`artifacts/tripwire/<wave>/state.json`) holding
  each machine (created, rate, deleted) and each balance reading.
- **The balance comparison** (version 4 calls it ratio B): money drawn from
  the account since the wave's first reading, divided by what the posted
  hourly rate predicts for the machines that ran over the same time, plus the
  storage volume's $0.01 an hour. 1.0 means billed as posted.
- **The billed-hours comparison** (version 4's ratio A): hours on the
  vendor's bill for a machine, divided by the hours the machine existed.
- **The watchdog**: `experiments/06-.../src/watch_run_a3.sh`, the laptop
  program that copies a run's files home and then deletes its machine.
- **The deadline timer**: `experiments/06-.../src/machine_deadline.sh`.
- **A trip**: the alarm writes the ledger figures, then a halt file; nothing
  launches until John clears it. Unchanged by this work.

## 3. Fix 1: reading during the wave, and the two rules

**Reading cadence.** While any machine of the wave runs, the alarm's watcher
reads the balance and the machine list every **5 minutes** (it was every 60).
After the last machine is deleted it keeps reading for **30 minutes** more, so
the comparison at deletion has a settled balance to work on, then stops.
Reads are free (no paid call) and run on the laptop.

**Why a short-window rule needs care.** The development run's own readings
show the balance is *lagged and lumpy*: machine M was created at 00:11:18, and
the balance read the same $73.7742 at 00:11:19, 00:14:40 and 00:17:47 (six
and a half minutes of a running machine with no visible charge), then
dropped $0.16 by 00:20:50. Sixteen minutes after the last deletion it still
had about half a cent to settle. So any rule over a few minutes of readings
will see (a) spending that has not posted yet, which makes the comparison
read *low*, and (b) a charge that posts in one lump, which can make it read
*high* for a moment when little has been spent. The comparison stays
cumulative from the wave's first reading (as now), so a late lump is spread
over the whole wave instead of read as a spike.

**Rule S, in flight (fast, rough).** At a reading while machines run, the
comparison counts as over the line when both hold:

- predicted spending so far is **at least $0.25** (about 15 machine-minutes
  at $0.99 an hour). Below that, a single lump of a few cents dominates the
  ratio: at one minute in, ten minutes charged in advance would read 9.9.
- money drawn is **at least 1.25 times the prediction plus $0.05**. The 1.25
  is version 4's trip line, unchanged. The $0.05 absorbs one lump of about
  three machine-minutes posted early.

The alarm trips only when **the latest two readings both** meet that (about 5
minutes apart). A real overcharge persists from one reading to the next; a
lump posted early is overtaken by the prediction at the next reading. The
cost of waiting one reading is about 5 machine-minutes, $0.08 a machine at
the posted rate. Because lag only ever makes this rule read low, it can miss
a mild overcharge on a short machine; that is what rule D is for.

**Rule D, at each deletion (steady, preferred).** Once a machine's deletion
time is recorded, its spending is final. At every reading taken **at least 15
minutes after a recorded deletion**, the comparison over the whole wave so
far counts as over the line when the prediction is **at least $0.10** and
money drawn is **at least 1.25 times the prediction plus $0.02**. One reading
is enough: the deleted machine's charges have had time to post, so the lump
problem is gone for it, and only rounding is allowed for. The 15 minutes come
from the lag seen in the development run (at least 6.5 minutes before the
first charge showed; nearly all settled by 16 minutes after the last
deletion). A machine still running alongside can only be under-posted, which
makes rule D read low, never high, so it cannot cause a false trip.

Rule D is the one to trust: it compares a finished machine's whole cost with
its whole life. Rule S exists to catch a gross overcharge (the 2026-08-08
shape, 3.5 times the rate) before the machines finish.

**Before the next machine of a wave.** The check the launcher runs before it
creates a machine applies the same two rules to its own reading and the one
before it. The old requirement of half an hour of readings is removed.

**A machine that disappears with no deletion record** (deleted by its own
on-machine watcher, or by the trainer) is marked deleted at the first reading
that does not list it, and the record says it was inferred. That is at most
one reading (5 minutes) late, and late only makes the comparison read low. A
recorded deletion time always replaces an inferred one.

## 4. Fix 2: every deleting step writes the deletion time

A new alarm command, `tripwire.py gone --state DIR --pod ID --at EPOCH --by
WHO`, records a deletion. The earliest recorded time wins over a later one;
any recorded time replaces an inferred one. It is called by:

- the watchdog, after its delete (normal finish, and its 24-hour backstop);
- the deadline timer, after its delete;
- the alarm itself, after an in-flight delete;
- the launcher, after its two emergency deletes (no connection to the machine
  after 8 minutes; the remote self-tests failed).

The time written is the moment the delete command came back. A step records
a deletion only when the vendor accepted the delete (exit 0) or answered that
the machine does not exist, and (for the watchdog) the machine is not listed
afterwards. The watchdog and deadline timer learn where the alarm's records
are from their settings files (`TRIP_PY`, `TRIP_SCRIPT`, `TRIP_DIR`), which
only the successor launcher writes, so experiment 06's own launchers behave
as before.

## 5. Fix 3: empty bills are "cannot be checked yet"

In the billed-hours comparison (run at the end of a wave), a machine whose
billing reading is an empty list, has no row for that machine, or sums to
zero billed time is "cannot be checked yet", and that is a trip, as section
12.7 already requires. The comparison also uses the recorded deletion time
for "hours the machine existed". **Consequence for whoever runs it:** run it
only once the vendor has posted the bills; run early, it halts launches until
John clears the halt. That is the rule as ruled, not a side effect.

## 6. Fix 4: the deadline timer stops only on a confirmed deletion

Each time the timer reads the clock (every 30 seconds) it looks for the
watchdog's "machine gone" record, a file `machine_gone_<machine id>` the
watchdog now writes beside the run's files, naming the machine. Every 5
minutes it also asks the vendor about the machine (`runpodctl pod get`, a
read). It stops itself, without deleting and without its "deadline reached"
lines, only when:

- the record file exists **and names this machine**; or
- the vendor's answer says the machine is **not found** (the words "not
  found", or status 404, which is how the vendor answered a delete of a
  machine already gone on 2026-09-26, measured in the attempt-2 check).

Anything else keeps it running to its deadline: a failed reading (an error
without "not found"), an empty answer, an answer that is not readable, or a
record naming another machine. The watchdog writes the record only when its
delete was accepted or answered "not found" and the machine is not listed
afterwards. When the watchdog finds the machine already gone over three
checks, it writes the record only if one more reading says "not found"; three
silent readings alone do not count.

**Not changed here:** what the timer writes when its own delete meets a
machine that is already gone (the attempt-2 check's finding B, its own
ruling).

## 7. The amendment, noted for version 5 (not written here)

Version 4, section 12.5, last paragraph: "It runs in flight, hourly, on ratio
B from the first hour of the first machine" becomes, by John's ruling of
2026-10-06: it reads every 5 minutes while machines run and for 30 minutes
after the last deletion; ratio B trips in flight under rule S (two readings
in a row at or above 1.25 times the prediction plus $0.05, once the
prediction is at least $0.25) and at each deletion under rule D (15 minutes
after a recorded deletion, 1.25 times plus $0.02, prediction at least $0.10);
every step that deletes a machine records the time; empty bills are a trip.

## 8. Tests, and the outcome each must give (stated before running)

All tests use a stand-in vendor program. Readings in the made-up waves are
taken at the first machine's creation and then at 1, 6, 11, ... minutes,
as the watcher would. Each machine costs $0.99 an hour and the volume $0.01.
The stand-in posts charges `L` minutes late, in steps of `P` minutes, at `m`
times the posted rate. The expected figures below were worked out by a
separate scratch calculation, not by the alarm's code.

| # | Case | Expected outcome |
|---|---|---|
| T1 | Honest wave, lagged and lumpy: two machines, 0 to 30 and 3 to 33 min; m 1.0, L 8, P 5 | No trip at any reading. The watcher ends at the first reading 30 min after the last deletion (minute 66). Final comparison 0.99 to 1.01 (scratch: 0.998) |
| T2 | Overbilled wave: same machines, m 3.5 | Rule S trips at minute 26 (two in a row: 21 and 26), while both machines still run; halt file and ledger figures written; the check before a next machine then refuses |
| T3 | Mild overcharge hidden by lag: one machine 0 to 20 min, m 1.4, L 8, P 5 | Rule S never trips; rule D trips at minute 36, the first reading 15 min after the deletion, ratio about 1.39 |
| T4 | Lumpy, honest: one machine 0 to 30, ten minutes charged in advance at each ten-minute mark | No trip (rule S holds at minute 21 only, not at 16 or 26); final comparison 1.00 |
| T5 | Lagged balance, honest: one machine 0 to 20, L 14 | No trip; final comparison 0.98 to 1.00 (scratch: 0.992) |
| T6 | Failed vendor reading in flight (balance read errors at minute 11) | Trip, "a check that cannot run" |
| T7 | Empty bill at the end of a wave (`[]`); a bill with zero hours; a bill with no row for this machine | Each a trip, "cannot be checked yet", exit 3, halt written. A real row (191,063 ms against 191.063 s of life) passes at 1.0. The old code passed the empty bill (shown) |
| T8 | Deletion records | The `gone` command records the time and who; an earlier recorded time is kept over a later one; a recorded time replaces an inferred one; the watcher's inferred time is the first reading without the machine |
| T9 | The watchdog's delete, stand-in vendor | Accepted delete: record file naming the machine written, and the alarm's record shows the deletion time. Delete answered "not found": the same. Delete failed with another error and the machine still listed: no record file, no alarm record |
| T10 | Deadline timer, machine already deleted, watchdog record present | Stops before its deadline; no delete call; no "DEADLINE REACHED" line |
| T11 | Deadline timer, vendor says "pod not found" (404) | Stops; no delete call |
| T12 | Deadline timer, failed vendor reading (error, no "not found") | Keeps running; deletes at the deadline |
| T13 | Deadline timer, empty vendor answer | Keeps running; deletes at the deadline |
| T14 | Deadline timer, record file naming a different machine | Ignored; deletes at the deadline |
| T15 | Deadline timer deletes at its deadline with the alarm configured | The alarm's record shows the timer's deletion time, by "machine deadline" |
| T16 | All earlier self-tests: the alarm's own, the launcher check, the deadline timer's six cases, the watchdog handshake test | Still pass |

**The replay (R).** The development run's recorded alarm state at 00:52 UTC
(copied from pull request 106 into this branch as a test fixture, with where
it came from), with the deletion times the watchdogs logged (the "pod gone"
lines, which is when the new watchdog would write them, give or take its
10-second settle), fed through the new alarm with the two later recorded
readings: $72.3178 at about 00:56:28 (the check's own reading) and $72.3080
at 01:11:20 (the old watcher's). Expected:

- with the 00:56:28 reading: **0.9899** (the check's figure, 0.99), no trip;
- with the 01:11:20 reading: about **0.995**, no trip;
- using the "deleting pod" times instead (the earlier edge of each delete):
  still 0.98 to 1.00;
- the old code's arithmetic on the same readings, with deletions inferred at
  01:11: **0.401**, as the old watcher logged.

## 9. Files touched, and files not touched

Touched: `experiments/08-successor-degree/src/tripwire.py`,
`experiments/08-successor-degree/src/launch_successor.sh`, a new test file
under `experiments/08-successor-degree/tests/`, recorded fixtures under it,
`experiments/06-.../src/machine_deadline.sh`, `.../watch_run_a3.sh`, and their
self-tests. Not touched: model, training, grammar or measuring code (another
session is changing those on other branches), the proposal, the ledger.
The alarm and the successor launcher are frozen code (2026-10-04 freeze);
John's 2026-10-06 rulings are the authority for these changes, and each
changed file says so.

## 10. After running (added after the first run, which is committed as it came out)

Every pre-stated outcome held except one range. **The replay using the
earlier edge of each delete (the "deleting pod" log lines) read 0.9988 with
the 00:56 reading and 1.0038 with the 01:11:20 reading; section 8 stated 0.98
to 1.00, so the second is outside it.** The range was written as a guess, not
worked out, and it was wrong: taking each deletion about 12 seconds earlier
shortens the predicted spend by about $0.013, and the balance kept falling
slightly after 00:56 ($0.0098 in 15 minutes, more than the volume's $0.0025),
so the later reading against the shorter lives comes out just over 1. Nothing
trips either way (the line is 1.25). The first run's output is kept as it
came out (`tests/check_tripwire_fixes_output.txt` in the commit that added
it). From the next run the check reports this as a missed prediction, by
name, and does not count it as a fault in the code; the range is not quietly
widened.

**Which figure the new code would actually have given.** The new watchdog
writes the moment its delete command came back, before its 10-second settle,
so in the development run it would have written times close to the earlier
edge: the replay figure is therefore about **1.00** (0.999 at 00:56, 1.004 at
01:11), and **0.99** (0.9899, 0.9948) with the "pod gone" times the
development-run check used. Either way it is about 1, against the old
alarm's 0.40.

## 11. Corrections after the independent check (pull request 117), stated before the code

The check (branch `check-tripwire-fixes`,
`docs/2026-10-06-tripwire-fixes-check-findings.md`) passed this work with
fixes needed. The coordinator asked for its problems 1, 2, 4, 7 and 8 to be
fixed, plus an operator note. **Its problems 3, 5 and 10 (a bill posted only
in part, a built-in "too early" refusal for the end-of-wave comparison, and
a top-up during a wave) are left unchanged here: John is ruling on them.**
Everything below was written before the code changed. Cost: $0.

### 11.1 Proof that a machine is deleted (check problems 1 and 2)

The old test, any answer containing "not found" or `"status":404`, is
replaced everywhere. The check showed three answers that wrongly passed it:
a 404 from something other than the machine ("404 page not found (status
404)"), the shell saying the tool is missing ("runpodctl: command not
found"), and a configuration message ("Config File … Not Found in …").

**The vendor's word** now means: the answer contains the vendor's own phrase
"pod not found" **and** "(status 404)", as in the one recorded answer
(2026-09-26, to a delete):
`{"error":"api error: {\"error\":\"pod not found to terminate\",\"status\":404} (status 404)"}`.
Anything else is a failed reading.

**A confirmed deletion** (what lets the deadline timer stand down, and what
lets the watchdog write its "machine gone" record) now needs, in addition,
**a machine list that succeeds** (the tool exits 0 and prints a list) **and
does not show the machine, twice, 5 minutes apart.**

- The deadline timer already asks the vendor every 5 minutes. It now counts
  checks in a row at which both hold (the vendor's word, and a good list
  without the machine). At two it stands down. Any check that fails either
  part sets the count back to zero. So the earliest stand-down is 5 minutes
  after the first good check.
- The watchdog writes its record when its delete was accepted (exit 0) or
  answered with the vendor's word, **and** a good list without the machine,
  read twice 5 minutes apart (`GONE_CONFIRM_GAP_S`, default 300). If either
  list read fails or shows the machine, no record. Its "found gone" path
  (three silent checks) needs the vendor's word to `pod get`, and then the
  same two list reads. A failed read never writes the record.
- The time written into the alarm's records is still the moment the delete
  came back. It is written once the deletion is confirmed.
- The launcher's two emergency deletes and the alarm's own in-flight delete
  only write into the alarm's records, never the timer's. They now use the
  stricter wording, without the list reads. A wrong record there makes the
  alarm read high (it trips; it never hides spending).

### 11.2 A lock on the alarm's records (check problem 4)

Every load-change-save of `state.json` in `tripwire.py` is done under a file
lock (`state.lock` in the wave's folder). Vendor reads happen **outside** the
lock: the watcher and the check before a launch read the vendor first, then
lock, load, apply, save and unlock. So a `gone` or `register` from another
program during the read is never overwritten.

### 11.3 The flaky timing test (check problem 7)

The timer tests measured time from the unrounded clock, but the deadline was
written rounded down to a whole second. They now check that the delete came
at or after the written deadline, and no more than the cap plus 3 seconds
after it. The timer itself is unchanged.

### 11.4 Operator note (asked by the coordinator)

In the launcher's usage notes and the alarm's notes: **run the end-of-wave
comparison (`tripwire.py reconcile`) no earlier than 3 hours after the last
deletion**, since bills post late and an empty bill is a trip; and **never
reuse an old wave name** (for example `dev-10m`, which still holds the
2026-10-04 records). The usage example stops naming `dev-10m`.

### 11.5 Expected outcomes, stated before running

| # | Case | Expected |
|---|---|---|
| N1 | Deadline timer; `pod get` answers "Error: api error: 404 page not found (status 404)"; list good and empty | Stays armed; deletes at its deadline |
| N2 | Deadline timer; the vendor tool missing from its command path | Stays armed; tries its delete at the deadline (which fails: no tool) and does not stand down |
| N3 | Deadline timer; `pod get` answers `Config File "config" Not Found in "[/Users/x/.runpod]"` | Stays armed; deletes at its deadline |
| N4 | Deadline timer; the recorded "pod not found … (status 404)" wording, and a good list without the machine, at two checks | Stands down; no delete; no deadline line |
| N5 | The same wording, but the machine list fails | Stays armed; deletes |
| N6 | The same wording, but the list shows the machine | Stays armed; deletes |
| N7 | The same wording and a good list, but only one check fits before the deadline | Stays armed; deletes |
| N8 | The old T11 answer, `{"error":"pod not found","status":404}` (no "(status 404)") | Now stays armed and deletes (T11 is changed to N4's wording) |
| W1 | Watchdog; delete accepted; list good without the machine at both reads | Record written; the alarm gets the delete time |
| W2 | Watchdog; delete accepted; first list read fails | No record; no alarm time |
| W3 | Watchdog; delete accepted; first list good, second shows the machine | No record |
| W4 | Watchdog; delete answered with the recorded wording; lists good | Record written |
| W5 | Watchdog; delete fails "HTTP 503"; lists good and empty | No record (the delete was neither accepted nor answered with the vendor's word) |
| W6 | Watchdog "found gone"; `pod get` gives the vendor's word; lists good | Record written |
| W7 | Watchdog "found gone"; `pod get` gives the 404-page wording | No record |
| L1 | The check's race, case 1: the watchdog's `gone` lands while the watcher reads the vendor | The watchdog's time survives |
| L2 | The check's race, case 2: a `register` lands while the watcher reads the vendor | The second machine survives |
| L3 | Another process holds the lock for 2 seconds | `gone` waits for it, then records |
| F1 | The deadline-timer cases, five full runs in a row | Pass every time |
| — | Everything earlier: the alarm's self-test, the launcher check, the deadline timer's and the watchdog's self-tests, all successor self-tests, the replay figures (0.9899, 0.9948, 0.9988, 1.0038, 0.401) | Unchanged; pass |

## 12. John's three rulings on the check's open items (2026-10-06), stated before the code

John ruled on the check's problems 3, 5 and 10, each on the check's
recommendation. All three are **amendments for version 5** (section 12.5 and
12.7 of version 4), noted here; version 5 is not written by this work.
Cost: $0.

### 12.1 A bill posted only in part is "cannot be checked yet" (check problem 3)

**Ruling:** at the end-of-wave comparison, billed time well below the
machine's life counts as "cannot be checked yet", which is a trip (an
extension of section 12.7).

**Threshold: below 0.90 of the machine's life.** From the recorded bills:

- The two honest complete bills on record read **0.9994** (2026-09-25, first
  machine: two hourly rows, 566,260 ms and 1,305,615 ms, against 1,873 s of
  life) and **1.00** (the second machine, 191,063 ms).
- The one recorded partial bill, the same first machine with only its first
  hourly row posted, reads **0.30**.
- Honest bills sit within about 0.1% of life; a missing hourly row of a
  short run removes far more than 10%. A line at 0.90 leaves a tenth of the
  life for disagreement between the laptop's clock of the machine's life and
  the vendor's billed time (two minutes of a 20-minute run), and still catches
  any missing row worth more than a tenth of the life. **What it cannot
  catch:** on a long run, a missing last row worth less than a tenth of the
  life (for example the final 40 minutes of a 10-hour run). Only two honest
  bills are on record, so the 0.90 rests on thin evidence; if an honest bill
  ever reads below it, the halt says "cannot be checked yet" and John decides.
- Overbilling (at or above 1.25) is still a trip as before.

### 12.2 When to run the end-of-wave comparison: a written rule only (check problem 5)

**Ruling:** no built-in "too early" refusal. The operator rule, in the
launcher's notes and the alarm's notes: run the end-of-wave comparison no
sooner than 3 hours after the last deletion; if it halts with "cannot be
checked yet", tell John, and run it again after he clears the halt.

### 12.3 A top-up during a wave (check problem 10)

**Ruling:** when the balance rises between readings, restart the in-flight
comparison from the next reading, record the event in the alarm's log, and do
not trip. Operator rule: do not top up during a wave.

**How, and one design choice that needs flagging.** A rise in the balance
never comes from honest spending, so at a reading higher than the one before,
the alarm records the event (in its records, under "restarts", and as a line
in the watcher's log saying the balance rose, by how much, and that the
comparison restarts here; not a trip), and from then on both rules work only
on readings from that reading onward. The risen reading is the new starting
point.

A plain restart would false-trip an honest wave, because the balance runs
late: charges for machine time *before* the restart post *after* it, and get
counted as spending in the new comparison, which starts its prediction at the
restart. Worked out in a scratch calculation (one honest 40-minute machine,
charges 8 minutes late in 5-minute steps, a $75 top-up at minute 13): the
plain restart reads 1.45 and trips at minute 56. So **the restarted
comparison's prediction starts 15 minutes before the restart reading** (the
same 15-minute allowance for late posting as the comparison at deletion).
The cost: after a top-up the comparison reads low by up to 15 machine-minutes,
so it still catches a gross overcharge (3.5 times) but can miss a mild one
(1.4 times) on what is left of the wave. That is the price of not tripping,
and the reason for the operator rule.

### 12.4 Expected outcomes, stated before running

| # | Case | Expected |
|---|---|---|
| B1 | End-of-wave comparison, the recorded partial bill (566,260 ms against 1,873 s of life, 0.30) | Trip, "cannot be checked yet", exit 3 |
| B2 | The recorded complete bill (1,871,875 ms against 1,873 s, 0.9994) | Passes, exit 0 |
| B3 | Billed exactly 0.90 of life; billed 0.899 | 0.90 passes; 0.899 is a trip, "cannot be checked yet" |
| B4 | Billed 3.5 times life | Still a trip, as over the line (unchanged) |
| U1 | Honest wave, one machine 0 to 40 min, charges 8 min late in 5-min steps, $75 top-up at minute 13 | No trip. A restart recorded at minute 16 and a line in the watcher's output. Final comparison about 0.895 (0.85 to 0.95) |
| U2 | Overbilled 3.5 times, machines 0 to 60 and 3 to 63 min, same lag, $75 top-up at minute 13 | Restart at 16; trips by the in-flight rule at minute 31 |
| U3 | Overbilled 1.4 times, one machine 0 to 40, same lag, $75 top-up at minute 13 | **Not caught** (final about 1.25, just under the line with its allowance): the stated cost |
| U4 | Honest, no lag, one machine 0 to 40, $75 top-up at minute 13 | No trip; reads low, about 0.62 |
| U5 | U1 with the 15-minute allowance set to zero (the plain restart) | Trips at minute 56: shows why the allowance is there |
| — | Everything earlier (section 8 and 11.5 cases, self-tests, replay) | Unchanged |

### 12.5 After running

All of 12.4 held except B3 on its first run: a bill of exactly 0.90 of life
tripped, because 0.25 hours over 0.2778 hours comes out a hair under 0.90 in
the computer's arithmetic. "Below 0.90" was meant, so the code now ignores
differences under one part in a billion; B3 then passes as stated. Nothing
else changed.

### 12.6 For version 5 (amendments to version 4, not written here)

In addition to section 7: (a) section 12.7 is extended: at the end-of-wave
comparison, a machine billed for less than 0.90 of its life "cannot be
checked yet", which is a trip; (b) operator rule: run that comparison no
sooner than 3 hours after the last deletion, and if it halts with "cannot be
checked yet", tell John and run it again after he clears it (no built-in
refusal); (c) section 12.5: a rise in the balance between readings is not a
trip; it is logged and the in-flight comparison restarts from that reading,
predicting from 15 minutes before it; operator rule: do not top up during a
wave; (d) proof that a machine is deleted is the vendor's "pod not found"
with "(status 404)" and two good machine lists without it, 5 minutes apart
(the check's corrections, section 11).

## 13. Corrections after the re-check, stated before the code

The re-check (`docs/2026-10-06-tripwire-fixes-recheck-findings.md` on branch
`check-tripwire-fixes`) found two blockers and one minor point; no ruling is
needed. It also noted that the failing first run of section 12 (B3) was not
kept; **this round keeps its first run's output, as it comes out, in its own
commit before anything is fixed after it.** Cost: $0.

### 13.1 The deadline timer's vendor check can delay the deadline (re-check problem 1)

Each check now makes two capped calls (`pod get`, then the machine list), so
the deadline could slip by about two caps plus a poll (about 70 seconds with
the real settings), and the comment saying "no more than the cap" was wrong.
**Fix in the code:** the timer skips its vendor check whenever the deadline
is less than two caps plus 2 seconds away. Two capped calls started earlier
than that end before the deadline, so the vendor check can no longer delay
the deadline at all; the only remaining lateness is the poll's own rounding
and the time to start the delete. The comment is corrected to say this.
**Fix in the tests:** the allowance becomes 10 seconds after the written
deadline (this laptop runs other heavy work, and the earlier runs showed
start-up delays of several seconds), and the stand-down cases get deadlines
long enough for two checks outside the skip window.

### 13.2 An inferred deletion time can halt an honest short machine (re-check problem 2)

- **The alarm's deletion time is written straight after the watchdog's delete
  is accepted** (exit 0) or answered with the vendor's words, as in the first
  round, whether or not the two machine lists then succeed. A wrong time
  there only makes the alarm read high, the safe way. The two good machine
  lists, 5 minutes apart, stay the condition for the **record file** the
  deadline timer reads.
- **The 0.90 line, for a deletion the alarm only inferred,** is judged
  against the machine's life up to the last reading that still listed it. The
  1.25 line keeps using the inferred time. A recorded deletion time is used
  for both, as now.

### 13.3 "Not listed" must mean "does not exist" (re-check problem 3)

Both list checks (the timer's and the watchdog's) use `pod list --all`,
since plain `pod list` shows running machines only.

### 13.4 Expected outcomes, stated before running

| # | Case | Expected |
|---|---|---|
| R1 | The whole check, eight runs in a row | All eight pass (the one pre-stated range still reported as missed) |
| R2 | Timer; every vendor read hangs; cap 2 s, deadline 12 s, checks every 1 s | Deletes no earlier than the written deadline and within 10 s after it |
| R3 | Timer; cap 20 s, deadline 10 s, checks every 1 s | Makes no vendor read at all (the deadline is inside the skip window); deletes at its deadline |
| R4 | Watchdog; delete accepted; first list read fails (old W2) | No record file; **the alarm gets the deletion time**, by "the watchdog" |
| R5 | Watchdog; delete accepted; second list shows the machine (old W3) | No record file; the alarm gets the deletion time |
| R6 | Watchdog; delete fails "HTTP 503" (W5) | Neither (unchanged) |
| R7 | End-of-wave comparison; machine listed for 20 minutes, deletion inferred 5 minutes after the last listing, billed 20 minutes | Passes (judged against the last listing, 1.00; against the inferred time it would read 0.80 and trip) |
| R8 | The same with only 10 minutes billed | Trip, "cannot be checked yet" |
| R9 | The same machine billed 1.3 times its life to the inferred deletion (that is, 32.5 minutes) | Trip as overbilling, at or above 1.25 |
| R10 | The list checks | Every `pod list` call the timer and the watchdog make carries `--all` |
| — | Everything else in sections 8, 11.5 and 12.4, and every other suite | Unchanged; pass |

### 13.5 After the first run (kept as it came out, in its own commit)

The first run failed four timing checks: T13 and T14 deleted 20 and 15
seconds after the written deadline, R2 10.5 seconds, and the five-run check
passed 18 of 20. **T13 and T14 made no vendor read at all**, so the lateness
was not the vendor check. The laptop was under very heavy load from other
work (load average about 450 earlier in the evening, 230 when measured just
after); a timer run by hand straight afterwards issued its delete at the
written deadline to the second. The tests had measured "late" as the moment
the whole timer program finished, including its log and ledger lines, each
of which starts several small programs. **Changed after seeing this, and
said so:** the tests now take the moment the delete was issued from the
stand-in tool's own timestamped log, keep the 10-second allowance, and print
the laptop's load at the start. The timer code is not changed by this.

### 13.6 Two more test-script faults found while running the eight runs (kept)

- **Attempt 1 crashed** in every run at the first timer case: the new "delete
  issued" figure was printed as a whole number when no delete had been issued.
  Output kept (`..._eight_runs_attempt1_crashed.txt`); format fixed.
- **Attempt 2 was stopped after its first run, which passed, because that pass
  was hollow.** With the new skip window (two caps plus 2 seconds, 6 seconds
  in the tests) the cases with 5-second deadlines (N1, N3, N5 to N8, T12, T13
  and the hung-read case) made **no vendor read at all**, so they passed
  without testing the answer they name. Output kept
  (`..._eight_runs_attempt2_stopped.txt`). **Fix:** those cases now run with
  14-second deadlines and must make at least one vendor read (N7: exactly
  one, with checks every 5 seconds); the five-run timing cases use 10-second
  deadlines and must read too. Expected outcomes are unchanged from 13.4.
