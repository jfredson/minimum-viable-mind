# Findings: independent check of the spending-alarm fixes (pull request 116)

*2026-10-06 (Pacific). Checker: a Claude Code session that wrote none of pull
request 116, in its own worktree (`~/Code/mvm-tripwire-check`, branch
`check-tripwire-fixes`). Method committed first:
`docs/2026-10-06-tripwire-fixes-check-method.md`. Cost: $0. Nothing rented; no
call to the vendor's service. The vendor tool's public source (GitHub,
`runpod/runpodctl`, tag v2.6.1, the version installed here) and the text
inside the installed tool were read; the tool was not run.*

## Verdict

**Passes with fixes needed before relying on it beyond the approved $1.14
reruns.** The four rulings are carried out, the arithmetic is right (my own
arithmetic and the alarm's agree on every recorded bill), the commit order is
right, and nothing recorded would falsely trip it. But proof of deletion
rests on any answer containing the words "not found", which the vendor tool
and the shell produce in several ways that do not mean "this machine does
not exist", and each of them stands the deadline timer down. The timer
is the last line of defence on cost, and the ruling said "never on a failed
reading". For the $1.14 reruns, with an operator watching and a fresh wave
name, the risk is small. Fix it before any unattended or registered wave.

## Problems, most serious first

### 1. "Not found" is too loose a proof of deletion (serious; fix before unattended waves)

The deadline timer, the watchdog, the launcher's emergency deletes and the
alarm all accept any answer containing "not found" (spaces removed, any
case) or `"status":404` as the vendor saying the machine is gone. Tested
against the real timer with a stand-in vendor tool
(`experiments/08-successor-degree/tests/check-of-116/not_found_wording.sh`,
output beside it), **three answers that do not mean the machine is gone each
disarm the timer**, which then logs "confirmed deleted":

- **Any 404 at all.** In the vendor tool 2.6.1 (`internal/api/client.go`),
  every answer outside the 200s becomes `api error: <body> (status N)`. A
  wrong address, an API version the vendor retires, or a gateway in front of
  the service answers "404 page not found", which matches.
- **The tool missing from the timer's command path.** The shell prints
  "runpodctl: command not found", which matches. Before this change the
  timer would have tried its delete, failed three times and printed "check
  the vendor's machine list NOW". Now it stands down quietly.
- **Configuration messages.** The installed tool contains a "Config File …
  Not Found in …" message. On 2026-09-16 the tool printed "Runpod config
  file not found" on a rented machine (compute ledger, self-terminate test).

What the vendor actually says to `pod get` for a deleted machine **is still
unrecorded**. The only recorded wording is the answer to a *delete* of a
machine already gone (2026-09-26): exit 1,
`{"error":"api error: {\"error\":\"pod not found to terminate\",\"status\":404} (status 404)"}`.
The second pattern, `"status":404`, never matches that recorded text, because
the vendor escapes the inner quotes. So it adds nothing real, and it would
match some other 404 body.

Where it can bite: the timer's 5-minute read; the watchdog's "found gone"
path (one `pod get` after three silent checks); the watchdog's delete; the
launcher's two emergency deletes; and the alarm's in-flight delete. In most
of these worlds the timer's own delete would fail too. So the main harm is
turning a loud failure into a quiet false "confirmed deleted". The exception
is a fault on the read path only, where a timer that would have worked gets
disarmed.

**Suggested fix:** stand down on the vendor's word only when (a) the answer
contains "pod not found" (the vendor's phrase) and "(status 404)", and (b) a
machine list that *succeeds* (valid list, exit 0) does not contain the
machine. Ideally require (b) twice, 5 minutes apart. Treat "command not
found" as a failed reading. Record what `pod get` really says for a deleted
machine the next time one is deleted on a paid run. That is a free read
after a deletion that happens anyway.

### 2. The watchdog's "gone" record does not check that the machine is unlisted (moderate)

The method says the record needs an accepted delete (or "not found") **and**
the machine not listed afterwards. In the code, "not listed" is
`pod_exists`, which reads `pod get` and greps for `"id"`. A failed or empty
reading counts as "not listed". So after an accepted delete (the vendor
answered with a 200-range status), one failed read writes the record and
disarms the timer. The record then rests on the delete's answer alone.
Whether the vendor can accept a delete and leave the machine billing is
untested: the attempt-2 check called this gap (c). The same read is reused
for the "found gone" path. **Fix:** check absence with a machine list that
succeeds, as in 1(b).

### 3. A bill posted only in part passes the end-of-wave comparison (moderate)

Fix 3 catches an empty bill, a missing row and a zero bill. It does not
catch a bill posted in part. The first 2026-09-25 machine billed in two
hourly rows (566,260 ms and 1,305,615 ms against 1,873 s of life). If only
the first row has posted, billed against life reads **0.30, which passes**.
The record shows bills arrive late and grow: on 2026-09-25 the second
machine's bill was still empty 4, 24 and 30 minutes after its deletion and
present 2 hours after, and the 2026-08-08 bill grew from 8.47 to 9.41 hours
overnight. The end-of-wave comparison is the only rule that sees an
overcharge posted after the watcher stops (problem 5). **Fix:** treat billed
hours below about 0.9 of machine life as "cannot be checked yet" too. That
needs John's word, as an extension of ruling 3.

### 4. Two programs writing the alarm's records at once can lose a write (moderate, partly older than this change)

The watcher loads the records, reads the vendor (seconds; up to 60 s a
call), then saves. A `gone` from the watchdog or timer, or a `register` from
the launcher, landing in that gap is overwritten. Shown deterministically in
`tests/check-of-116/shared_records_race.py` (output beside it):

- The watchdog's deletion time is lost. The watcher then infers the
  deletion up to 5 minutes late, which reads low. This partly undoes fix 2.
- A second machine's registration is lost. Its spending is then not
  predicted, which reads high: a false trip, and later its `gone` is refused
  ("not a machine of this wave").

The risk was always there for `register`. Reading every 5 minutes and adding
four new writers gives twelve times as many chances (roughly 1 in 100 per
write at a few seconds of reading per 5 minutes). **Fix:** a file lock around
every load-change-save in `tripwire.py`, held only around the load and the
save. Re-read the records after the vendor reads and apply the changes then.

### 5. The end-of-wave comparison: when to run it is left to the operator (moderate, procedural)

Nothing runs `reconcile` (the end-of-wave comparison); no launcher calls it.
Run within about 2 hours of the last deletion, the record says the bill will
likely still be empty. That is a trip, and launches halt until John clears
it. The code says only "once the bills have posted". **For the operator:**
run it no earlier than 3 hours after the last deletion. If it trips "cannot
be checked yet", that halt is real under the rule: tell John, and run it
again after he clears it. **Suggested fix:** make the comparison refuse to
start (no halt written) less than 3 hours after the last recorded deletion,
saying when to come back. Because 12.7 says a check that cannot run is a
trip, John should say whether "too early to start" is allowed.

### 6. The 2026-08-08 overcharge is caught only if it shows while the machine runs (expected; state it in version 5)

From `tests/check-of-116/thresholds_against_records.py`, at the successor's
$0.99 rate:

- **3.5 times, reaching the balance in flight**, with the 6.5-minute lag seen
  on 2026-10-04: rule S trips at **minute 20** after creation, and rule D
  would too.
- **The extra posting in one lump within the watcher's last 30 minutes:**
  rule D trips.
- **The extra posting more than 30 minutes after the last deletion:**
  nothing in flight sees it. Only the end-of-wave comparison can, and it
  has problems 3 and 5. The record cannot say which shape 2026-08-08 had.
  The balance agreed with the bill the same day, and the bill grew
  overnight after the machine was gone, so at least part of it posted late.

### 7. The new test of the 20-second cap fails about half the time (minor; the test, not the timer)

On re-running, "(added) a vendor read that hangs" failed in 2 of 4 full runs
(4.4 s against a 4.5 s floor). The test writes the deadline as
`int(time.time()) + 5` but times from the unrounded clock, so the run can be
up to a second shorter than it expects. T12 to T15 share the margin and passed
narrowly (3.6 s against 3.5 s). The timer is fine: it deleted at its
deadline in every run. **Fix:** time from the written deadline, or allow a
second.

### 8. Pull request 116's description is pull request 115's (minor; fix before merge)

The description of 116 is word for word the description of pull request 115
(the training-exclusion pairing work). Its commit list, results and "look
hardest at" items describe other code. It should be replaced with this
work's own summary.

### 9. Rule S would falsely trip if the vendor ever charged 15 minutes or more in advance (minor; not seen)

An honest machine charged in advance in blocks of 15 or 20 minutes trips
rule S for lives of 30 minutes and up. Blocks of 10 minutes or less do not
trip it (the pull request's own test T4 is the 10-minute case). Nothing
recorded shows early charging. Every recorded charge posts late: 6.5 minutes
on 2026-10-04, about 4 minutes after deletion on 2026-09-25, and the volume
in hourly lumps. A false trip halts launches; it does not spend. No change
suggested. If one ever happens, this is the likely cause.

### 10. A top-up during a wave hides spending (worth a short ruling)

The balance comparison treats any rise in the balance as negative spending.
A top-up of $X during a wave lowers "money drawn" by $X. Any top-up of the
size seen in the ledger (+$75 on 2026-08-15, +$120 on 2026-08-16) would hide
a whole wave's overcharge, and the drawn figure would go below zero. It is
plausible on this account: John tops up by hand, has done it on the day of a
launch, and registered waves run for hours. A rise in the balance never
comes from honest spending. **Suggested ruling:** any rise between two
readings either (a) is a trip ("cannot be checked"), or (b) starts the
comparison afresh from the reading after the rise and logs it. (b) is
gentler and loses only the comparison so far. Either is a few lines of code.
For the $1.14 reruns: do not top up while they run. The balance (about $72)
covers them many times over.

## The other points asked about

- **Commit order: right.** The method note (`e54ecf6`, 19:25 Pacific) came
  before the code (`a3fc51f`, 19:35). Section 10 of the note was added after
  the first run. It reports the one missed range as missed, and the first
  run's failing output was committed as it came out (checked in `a3fc51f`).
  The two unannounced fixes came after, in their own commits.
- **The thresholds against all recorded billing:** the 2026-10-04
  development run (all its readings plus the two later ones), both
  2026-09-25 rented machines (every recorded balance reading), and the
  2026-08-08 shape modelled three ways. No honest record trips. The second
  2026-09-25 machine (191 seconds) is below both floors, so the in-flight
  rules cannot judge a machine that short. My arithmetic and the alarm's
  functions agree on every case.
- **Experiment 06's launchers.** `launch_a3_fetch_first.sh` uses both the
  watchdog and the timer; `launch_a3.sh` and `launch_ctl_pilot.sh` use the
  watchdog. None of them sets the alarm settings, so the alarm is never
  called. They get the stand-down and the record file, as the ruling meant
  for "each laptop deadline timer". The timer's settings file and the
  watchdog's destination are the same folder in every launcher, so the
  record is found. Their self-tests pass: deadline timer 20 of 20,
  watchdog handshake 26 of 26, launch gate 369 of 369, sleep guard 67 of 67.
  No regression found beyond problems 1 and 2, which they share.
- **The unannounced fix for a machine listed again:** right. It clears only
  an *inferred* deletion. A recorded deletion of a machine still listed is
  kept, which makes the comparison read high, the safe way.
- **The unannounced 20-second limit on the timer's vendor read:** right. The
  read runs in the background and is killed at the limit, so a hung read
  delays the deadline by at most 20 seconds. Its test is flaky (problem 7).
  The timer's *delete* still has no time limit; that is an older finding,
  not in scope.
- **For the $1.14 reruns, use a fresh wave name.** The launcher's own
  example says `WAVE=dev-10m`, and that folder still holds the 2026-10-04
  records: a starting balance from two days ago, four old machines and a
  stale watcher process number. Reused, the comparison would include two
  days of storage charges and old machines and read about 0.5, which hides
  an overcharge. A stale process number that the system has since given to
  another program would also stop a new watcher being started.

## Tests re-run

- `tests/check_tripwire_fixes.py` (the pull request's own): 4 full runs. All
  checks pass in 2. In the other 2 the 20-second-cap test fails on timing
  (problem 7). The pre-stated replay range is reported as missed, as
  declared.
- `tripwire.py --self-test`: all checks passed.
- Experiment 06 self-tests: as above, all pass.
- Successor launcher check (`tests/check_launcher.sh`, including its dry
  run, which runs the local self-tests): all checks pass, exit 0.
- Successor self-test suite (`src/run_self_tests.sh`): 200 passed, 0 failed,
  "ALL SELF-TESTS PASS".
- Outputs: `experiments/08-successor-degree/tests/check-of-116/rerun_*`.
