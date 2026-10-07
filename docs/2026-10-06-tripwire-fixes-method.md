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
