# Findings: the launch gate on every unregistered launcher

*Written 2026-09-24 (Pacific) by the session that wrote the code, on branch
`worktree-launcher-sleep-gate`. The method was committed first, as
`launcher-sleep-gate-method.md` (commit `1801d7b`), and the code after it
(commit `b98c4e2`). Nothing was rented, the rental company (RunPod) was not
contacted, no money was spent, and this Mac's power settings were read and
never changed.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30). Every finding is labelled MEASURED — a command was run and
its output is reported here — or ARGUED — reasoning a reader can dispute.*

**This is the writing session's account, not a check.** Under the pairing
rule in `docs/outside-review-protocol.md` a different session checks it
before it is relied on. What that check is owed is at the end.

---

## Headline

Every launcher in this repository that can rent a machine and is not
registered text — three of the four — now **refuses** a real launch unless
(1) this Mac cannot fall asleep, (2) the laptop's fetch-and-delete is set up
to run inside the time the machine is allowed to live, and (3) a ledger row
with an estimate for this run already exists. Before today one of the three
refused on (1) and none checked (2) or (3). The fourth launcher,
`src/launch_a3.sh`, is registered and was not touched; the amendment that
would give it the same gate is drafted in the method's §7.

**On this Mac, as it stands today, every real launch through those three
launchers would be refused,** because the never-sleep setting is off (finding
5). That is the gate doing its job, and turning the setting on is John's call.

---

## 1. The premise was partly out of date — MEASURED

The task said "every launcher warns, none checks". That was true until
earlier today. Pull request 28 (commit `aa7b739`) and its repairs
(`32472d1`, `5913bfa`) gave `src/launch_a3_fetch_first.sh` a real refusal,
which two checking sessions passed
(`reviews/2026-09-24-sleep-guard-check-claude-worktree.md`,
`reviews/2026-09-24-sleep-guard-fixes-check-claude-worktree.md`). Of the four
files that contain the rental command, `runpodctl pod create`, that was the
only one that checked. The table is in the method's §1. So this work
**extended and consolidated** an existing, reviewed check rather than writing
one from nothing: the check moved unchanged into a shared file,
`src/launch_gate.sh`, and the two launchers that only warned —
`src/launch_ctl_pilot.sh` and `src/launch_pilot_a1.sh` — now call it too.

## 2. Both test harnesses pass on the finished code — MEASURED

```
$ experiments/06-mvm-0a-constructed-self-index/src/launch_gate_selftest.sh | tail -3
checks passed: 264   failed: 0
launch gate self-test OK — nothing was rented, no vendor was contacted,
and this Mac's real power settings were never read or changed.

$ experiments/06-mvm-0a-constructed-self-index/src/sleep_guard_selftest.sh | tail -3
checks passed: 67   failed: 0
sleep guard self-test OK — nothing was rented, no vendor was contacted,
and this Mac's real power settings were never read or changed.
```

`launch_gate_selftest.sh` (new) runs **each of the three launchers** through
fifteen refusal cases and two cases that must pass. The refusals: the
never-sleep setting off; no ledger row naming the run; a row naming a longer
name that merely starts with this one; a row five days old; a row dated in the
future; a row with no dollar estimate; a row that already records an actual
cost; no ledger file; the watchdog missing; the watchdog not parsing; the
keep-awake command missing; the laptop's deadline after the machine's; a
deadline of zero hours; two problems at once (both must be reported); and the
sleep override given while a ledger problem stands (the override must not
cover it). The two that must pass are the **negative control** — a safe Mac, a
good row, a sound watchdog, run as a *real* launch, which must get past the
gate and reach the stand-in rental command — and equal deadlines. It also
checks that a dry run reports every problem, exits 0 and creates nothing.

It rents nothing by three independent stops, set out in its header: stand-in
power readings and ledger; a stand-in `runpodctl` first on the command path,
which logs every call and fails (the harness confirms the path resolves to it
before any launcher runs); and an empty home folder, so the real tool would
have no account key even if reached.

`sleep_guard_selftest.sh` was changed in three ways. It now supplies a
stand-in ledger, since otherwise its override case is refused by the new
ledger check before reaching the step it tests. Its case 6 checks the
**order** the comment states — the keep-awake cover starts after the machine
exists — in all three launchers, instead of two hand-written line numbers that
the move made meaningless; that also closes the second sleep-guard check's
follow-up 2. And its new case 7 covers a charger that is not keeping up, with
a control (a Mac holding its charge on purpose must still pass). Before any
of this, on main's code, it reported `checks passed: 59   failed: 0` (run in
this session, matching the figure its own record gives).

## 3. Both harnesses were seen failing against a broken gate — MEASURED

`src/launch_gate_mutation_run.py` breaks the gate four ways, runs both
harnesses against each broken copy, and restores the original, proving the
restore by its fingerprint (sha256). Its output, verbatim:

```
$ python3 experiments/06-mvm-0a-constructed-self-index/src/launch_gate_mutation_run.py
original launch_gate.sh sha256 50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c

# M1 warning only: the refusal prints and carries on
  launch_gate_selftest.sh: exit 1; checks passed: 204   failed: 60
      45 x FAIL: it went on past the gate to the next step
      15 x FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run --template-id runpod-torch-v280 --gpu-id NVIDIA GeForce RTX 5090 --cloud-type SECURE --network-volume-id 8xeftvclmv --terminate-after <time>
  sleep_guard_selftest.sh: exit 1; checks passed: 60   failed: 7
      7 x FAIL: it ran on past the sleep check to the next precondition

# M2 the ledger check accepts anything
  launch_gate_selftest.sh: exit 1; checks passed: 175   failed: 89
      3 x FAIL: it did not report the row it matched
      24 x FAIL: never said it was refusing
      3 x FAIL: did not name the problem 'no row in the ledger table names this run's output name 'gate_test_run''
      24 x FAIL: it went on past the gate to the next step
      6 x FAIL: did not name the problem 'no row in the ledger table names'
      3 x FAIL: did not name the problem '5 days ago (must be within 2)'
      3 x FAIL: did not name the problem 'in the future'
      3 x FAIL: did not name the problem 'no dollar figure in its estimate column'
      3 x FAIL: did not name the problem 'already records an actual cost'
      3 x FAIL: did not name the problem 'the compute ledger is not where it should be'
      3 x FAIL: only the first problem was reported
      3 x FAIL: the ledger problem was not in the dry run
      8 x FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run --template-id runpod-torch-v280 --gpu-id NVIDIA GeForce RTX 5090 --cloud-type SECURE --network-volume-id 8xeftvclmv --terminate-after <time>
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0

# M3 the deadline-order check removed
  launch_gate_selftest.sh: exit 1; checks passed: 254   failed: 10
      3 x FAIL: never said it was refusing
      3 x FAIL: did not name the problem 'after the machine's own deadline'
      3 x FAIL: it went on past the gate to the next step
      1 x FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run --template-id runpod-torch-v280 --gpu-id NVIDIA GeForce RTX 5090 --cloud-type SECURE --network-volume-id 8xeftvclmv --terminate-after <time>
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0

# M4 the discharging-charger check removed
  launch_gate_selftest.sh: exit 0; checks passed: 264   failed: 0
  sleep_guard_selftest.sh: exit 1; checks passed: 63   failed: 4
      1 x FAIL: it never said it was refusing
      1 x FAIL: it ran on past the sleep check to the next precondition
      1 x FAIL: it did not say the battery is discharging
      1 x FAIL: it did not print the fix

restored; sha256 50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c matches original: True
```

Each break is caught by at least one harness. The two harnesses cover
different things, which the pattern shows: the sleep harness does not notice
the ledger or deadline checks being broken (M2, M3), and the gate harness
does not notice the charger check being removed (M4), because the charger
case lives only in the sleep harness.

**Every "REACHED THE RENTAL COMMAND" line above is the stand-in, not the rental
company.** It is the proof those breakages would have rented a machine, and it
is why the stand-in exists.

## 4. The first mutation run found a hole in the new harness, now closed — MEASURED

The method (§4) planned three breaks. On the first run of the "warning only"
break, the gate harness reported **15 failures, all from the A1-pilot
launcher**, and passed every refusal case for the other two. Those two
launchers run their module self-tests right after the gate, and the harness
gives refusal cases a self-test stand-in that always fails — a safety stop
that has nothing to do with the gate. With the gate reduced to a warning,
they were stopped there instead: never reached the rental command, still
printed "REFUSING TO LAUNCH" (the warning prints those words and carries on),
still exited 1. Three of the four refusal assertions passed on a broken gate.

This is the same trap the sleep harness's own record describes from its first
mutation run: an exit status two unrelated refusals share cannot say which one
fired. The fix was the same too — every refusal case now also asserts **where**
the launcher stopped (not past the gate). With it, the same break fails all 45
refusal cases (15 per launcher), as in M1 above. A fourth break, M4, was added
for the charger check, which the method did not plan to break.

## 5. On this Mac today, every real launch is refused — MEASURED

This Mac's settings, read with `pmset -g` and `pmset -g batt` and not changed:
never-sleep setting off (`SleepDisabled 0`), drawing from wall power, battery
`100%; charged`. A dry run (which creates nothing) of the A1-pilot launcher at
its defaults:

```
$ DRYRUN=1 experiments/06-mvm-0a-constructed-self-index/src/launch_pilot_a1.sh
local pre-flight: can this Mac fall asleep?
  problem: the never-sleep override is OFF (SleepDisabled 0) — shut the lid and this Mac sleeps, taking the watchdog with it
local pre-flight: are the fetch and the delete scheduled inside the run window?
  ok: watchdog watch_run.sh present and parses; runs under caffeinate
  ok: laptop fetch-and-delete by +24h, machine's own deadline +24h
local pre-flight: is there a ledger row with an estimate for 'pilot_a1_30m_seed0'?
  problem: no row in the ledger table names this run's output name 'pilot_a1_30m_seed0'
  WOULD REFUSE a real launch (this is a dry run, so it carries on and
  creates nothing):
  …
DRYRUN — nothing created. Would run:
  …
```

The staged rented slice (`docs/successor-rented-slice-staging-2026-09-21.md`)
launches through the fetch-first launcher under the output name
`slice_handshake`. Its dry run reports the same two problems, the second being
`no row in the ledger table names this run's output name 'slice_handshake'`.
`grep -c slice_handshake compute-ledger.md` returns `0`.

At its default output name the fetch-first launcher **does** find a real row —
the 2026-09-21 row for the machine created by accident — and correctly
declines it:

```
$ DRYRUN=1 PY_LOCAL=/usr/bin/true …/src/launch_a3_fetch_first.sh | grep -A1 'ledger row with an estimate'
local pre-flight: is there a ledger row with an estimate for 'a3_30m_seed0'?
  problem: rows in the ledger name 'a3_30m_seed0' but none will do: line 74 is dated 2026-09-21, 3 days ago (must be within 2)
```

That is the one real row the date limit was written for, and the only live
test of the ledger check against the real file.

## 6. Nothing else broke — MEASURED

`src/check_launcher_argument_guard.sh` — the test for failure 5 in
`docs/known-failure-modes.md`, a command that creates something while
documented as creating nothing — passes every check, including "dry run still
exits 0" and "dry run still creates nothing" for all three launchers, and its
negative control still rejects an unguarded stand-in; it ends
`all checks pass. nothing was created and nothing was spent.`
`src/reap_handshake_selftest.sh` reports `checks passed: 26   failed: 0`.

## 7. What this changes for the weekend — ARGUED

- **Before any launch, the never-sleep setting has to be switched on**
  (`sudo pmset -a disablesleep 1`, and back with `… 0` afterwards), and the Mac
  plugged in. The refusal prints both commands. That needs John's password, so
  it is his hands.
- **Every ledger row written from now on has to name the run's output name**
  (`OUT`), be dated within two days of the launch (Pacific), and leave its
  actual-cost column as `—` until after the machine is gone. Of the existing
  rows only the 2026-09-21 row names an output name at all, so this is a new
  habit; the refusal says exactly what to write.
- **The staged slice's step 1 will be refused until its row exists.** Its go
  lapsed on 2026-09-22 and a fresh one is quoted in a new row anyway, so this
  adds no step — but whoever amends the staging plan should add "write the
  ledger row naming `slice_handshake`" before step 1, and the plan's checker
  should see this gate. The staging document is **not** changed here.

## 8. What the gate does not do — ARGUED

1. **The registered launcher `launch_a3.sh` is not covered.** It still only
   warns. Drafted amendment: the method's §7. Until Gate A clears it, the
   registered-run path depends on the operator, which is the thing John's
   2026-09-22 ruling says a mitigation must not do.
2. **It does not bound idle billing, only its order.** It requires the
   laptop's deadline to be no later than the machine's; it does not check that
   the deadline is close to the run's expected length, because the ledger's
   hours column is free prose. A `WATCH_H` of 24 on a 10-hour run is still
   allowed. The obvious next step, if wanted, is a machine-readable hours
   estimate in the row.
3. **It does not check John's go is quoted in the row** (commitment C2(b)).
   Whether a sentence is a go is not something a pattern can decide.
4. **The ledger is read from the same checkout as the launcher.** A launch
   from a git worktree reads that worktree's copy of the ledger, which may be
   behind or ahead of the main line. The fix message prints the full path, so
   the operator sees which file it means.
5. **A relaunch on the same day can reuse the first launch's row** if that row's
   actual-cost column has not been filled in yet. The date limit and the
   actual-cost rule narrow this and do not close it; an explicit key per row
   would (the alternative the method weighed and set aside).
6. **The keep-awake gap during the launch itself** (named in the carried-over
   comment) remains as written. With the never-sleep setting on — which the
   gate now requires — this Mac should not idle-sleep either, so the gap should
   matter only on the override path. That is ARGUED from what the setting is
   documented to do; nobody switched it on to watch.
7. **The earlier sleep-guard checks' other follow-ups are still open**: an
   unreadable value reported as "off"; the power reader's success-or-failure
   report ignored; no time limit on the reading; the power-source pattern
   grabbing too much; and the out-of-date invitation in
   `reap-shutdown-order-method.md` to compare against the derivation script.
   Closed here: follow-up 1 of the second check (the preview now says a
   non-1 override value would not be taken — MEASURED by one dry run,
   `DRYRUN=1 ALLOW_LAPTOP_SLEEP=0 …/launch_pilot_a1.sh`, which printed
   "ALLOW_LAPTOP_SLEEP is set to '0', which is not 1, so a real launch would
   not take it as an override either."; no harness case covers it yet), 2 of
   the second (hand-kept line
   numbers), and 4 and 5 of the first (all problems named at once; the
   discharging charger).

## 9. Who decided what

- **John** set the task: it is the roadmap step he approved in
  `docs/weekend-roadmap-2026-09-24.md`, and the rule that a mitigation must
  not depend on the operator noticing is his, from
  `docs/rulings/2026-09-22-launcher-argument-guard.md`.
- **The earlier sessions** (pull request 28 and its repairs) decided what the
  sleep check reads and that it accepts only the value 1 as an override; that
  design was carried over unchanged.
- **This session decided, on its own authority**: one shared file rather than
  copies; not accepting a running `caffeinate` in place of the never-sleep
  setting; the charger check; the meaning of "the run window" and the
  `WATCH_H ≤ TERM_H` rule; the ledger rules (output name, two days, dollar
  figure, no actual cost yet); no override for the two new checks; and the
  drafted amendment's wording. Each has its confidence and strongest
  alternative in the method. None has been put to John.

## 10. Owed before this is relied on

A check by a session that did not write it. It should at least: run the two
harnesses and the mutation script and compare their counts with §§2–3; read
`launch_gate.sh` against the fetch-first launcher's sleep block at `97ee3c9`
and confirm the move changed nothing but what §8.7 says it closed; try the
ledger check with rows this session did not write (the real ledger's other
rows, a row with a `|` inside its prose); and say whether the two-day limit
and the `WATCH_H ≤ TERM_H` rule are right, since both are judgment calls.

---

## 11. The two repairs the check asked for, 2026-09-24 — MEASURED

The check of pull request 33 is filed at
`reviews/2026-09-24-launch-gate-pr33-check-claude-worktree.md` (draft pull
request 36). It found the gate holds, and asked for two fixes to the ledger
check before it is relied on. Sections 2 and 3 above are left as written: they
record the state at commits `b98c4e2` and `182f407`. This section records the
state after the repairs.

1. **Rows of the wrong shape.** A good row with an annotation added as an extra
   cell (the real 2026-08-17 row's shape) was refused with the wrong reason,
   "no dollar figure", because counting from the right read the actual-cost
   cell as the estimate. Now a row must have exactly eight cells, a `|` written
   `\|` is prose, and any other count is refused with "line N has C cells,
   expected 8". The method's §3c carries the corrected rule beside the struck
   sentence.
2. **Hyphenated cousins of the run name.** A row for `slice_handshake-v2`
   satisfied a launch of `slice_handshake`. A hyphen, or a full stop followed
   by more name, no longer ends a name. **One consequence the check did not
   foresee, and that this session met while testing:** the real 2026-09-21 row
   names the machine, `mvm-a3_30m_seed0`, and with a hyphen no longer a
   boundary that row stopped matching, which would have made finding 5 above
   false. `mvm-`, the name the launchers give the machine, is the one prefix
   now accepted. A dry run at the default name again reports
   `line 74 is dated 2026-09-21, 3 days ago (must be within 2)`.
3. **Found while fixing, not asked for.** The rows were passed to the shell
   with tab as the separator, and the shell merges runs of tabs, so an empty
   date or cell would have shifted every field after it. Each field now carries
   a leading marker, so an empty one keeps its place. No harness case isolates
   this.

New harness cases, for each of the three launchers: a hyphenated, a dotted and
a hyphen-prefixed cousin must be refused; the name ending a sentence and the
machine name `mvm-…` must pass; the 2026-08-17 shape (10 cells) and an appended
cell with a closing `|` (9 cells) must be refused as wrong shape and not for
the estimate; an escaped `\|` in prose must pass.

```
$ …/src/launch_gate_selftest.sh | tail -3
checks passed: 351   failed: 0
$ …/src/sleep_guard_selftest.sh | tail -3
checks passed: 67   failed: 0
$ …/src/check_launcher_argument_guard.sh | tail -1
all checks pass. nothing was created and nothing was spent.
$ python3 …/src/launch_gate_mutation_run.py      (summary lines)
# M1 warning only: the refusal prints and carries on
  launch_gate_selftest.sh: exit 1; checks passed: 271   failed: 80
  sleep_guard_selftest.sh: exit 1; checks passed: 60   failed: 7
# M2 the ledger check accepts anything
  launch_gate_selftest.sh: exit 1; checks passed: 212   failed: 139
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0
# M3 the deadline-order check removed
  launch_gate_selftest.sh: exit 1; checks passed: 341   failed: 10
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0
# M4 the discharging-charger check removed
  launch_gate_selftest.sh: exit 0; checks passed: 351   failed: 0
  sleep_guard_selftest.sh: exit 1; checks passed: 63   failed: 4
# M5 the name pattern treats '-' and '.' as word boundaries again
  launch_gate_selftest.sh: exit 1; checks passed: 321   failed: 30
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0
# M6 the eight-cell rule removed
  launch_gate_selftest.sh: exit 1; checks passed: 342   failed: 9
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0
restored; sha256 182b6555788bd7eebff9cacf85a46a49b4cc3f0950eb2463cfb374674006d64f matches original: True
```

M5 and M6 each put one of the two defects back, and each is caught. **These
repairs, and the `mvm-` prefix most of all, are owed a check by a session that
did not write them.** The `mvm-` rule is a judgment call this session made on
its own authority. `launch_a3.sh` was not touched.
