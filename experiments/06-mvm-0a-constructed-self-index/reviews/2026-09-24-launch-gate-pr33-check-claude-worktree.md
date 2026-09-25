# Check: pull request 33, the shared launch gate on every unregistered launcher

*Written 2026-09-24 (Pacific) by a checking session that wrote none of the work
being checked, under the pairing rule in `docs/outside-review-protocol.md`. This
session did not see the writing session's chat. It read the two documents the
pull request adds, the code, and the records those documents point at, and ran
the commands below.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30). Every finding is labelled MEASURED — a command was run and
its output is reported here — or ARGUED — reasoning a reader can dispute.*

**What was checked.** Pull request 33, "Make the launch checklist a gate every
unregistered launcher checks", branch `worktree-launcher-sleep-gate` at commit
`182f407` ("Findings for the launch gate, and the mutation run that backs them"),
sitting on `b98c4e2` (the code) and `1801d7b` (the method, committed first), all
three on top of `97ee3c9`. The main line has since moved by one commit
(`45875ee`, a roadmap data fix touching only `data/roadmap.toml`), so this
session merged the pull request's three commits onto current main in its own
worktree (`worktree-pr33-launch-gate-check`) and checked the result. The merge
was clean. Every command below ran from that worktree unless it says otherwise.

**Nothing was rented, the rental company was not contacted, nothing was spent,
no machine was created, and this Mac's real power settings were read and never
changed.** Every run of a launcher in real mode had a stand-in rental command
first on the command path, which logs and fails, and an empty home folder, so
even the real tool would have had no account key. The stand-in was never called
except where a case says it must be (the controls). The registered launcher
`launch_a3.sh` was never run, with or without arguments.

**Verdict: yes, with two small things to change first, neither of which is a
hole in the gate.** The gate refuses where it should, lets a prepared launch
through, is called before the first rental command in all three unregistered
launchers, and the registered launcher is byte-for-byte untouched. Both
harnesses and the mutation run reproduce the writer's counts exactly, and this
session's own deliberate break is caught. The two things to change are in the
ledger check: a sentence in the method claims the real ledger's 2026-08-17 row
is handled, and a test with that row's shape shows it is not (the gate refuses a
good row with the wrong reason — safe direction, wrong message); and a hyphen
counts as a word boundary, so a row naming a hyphenated cousin of the run
satisfies the check. Both are set out under "What must change". One thing for
John rather than for the pull request: this Mac's never-sleep setting now reads
**on**, where the writer's finding 5 and both earlier sleep-guard checks read it
**off** earlier the same day; nobody in this session touched it.

---

## What was opened, and what was not

Opened: `CLAUDE.md`; the top entry of `STATUS.md`; the pairing rule, the
isolation section and "Filing" in `docs/outside-review-protocol.md`; all of
`docs/known-failure-modes.md`; the pull request's two documents,
`launcher-sleep-gate-findings.md` and `launcher-sleep-gate-method.md`; the new
`src/launch_gate.sh`, `src/launch_gate_selftest.sh` and
`src/launch_gate_mutation_run.py` in full; the diffs of the three unregistered
launchers and of `src/sleep_guard_selftest.sh` against `97ee3c9`; lines 55–71,
136–145 and the watchdog line of the registered `src/launch_a3.sh`; the
`## Ledger` table of `compute-ledger.md` (header, cell counts of every row, rows
64 and 74 in full); the launch-checklist lines of
`docs/weekend-roadmap-2026-09-24.md`; section 9 of `argument-guard-method.md`
(the corrected step 0 of the staged slice); line 86 of
`docs/successor-rented-slice-staging-2026-09-21.md`; the header of
`reviews/2026-09-24-sleep-guard-fixes-check-claude-worktree.md`.

Not opened: the writing session's chat; the pull request's conversation on
GitHub beyond its title, branch and base; the two earlier sleep-guard checks in
full (only the header of the second); the watchdog scripts `watch_run.sh` and
`watch_run_a3.sh`; `reap-shutdown-order-method.md`; the fetch-first launcher's
own sleep-guard record beyond what its diff shows.

Not re-run: the writer's statement that the sleep harness reported 59 passes on
main's code before this change. Running the old harness needs the old launcher
beside it and the repository's Python environment at the old path; the number
matches the harness's own written record, and nothing here depends on it.

---

## 1. Both harnesses pass with the writer's counts — MEASURED

```
$ experiments/06-mvm-0a-constructed-self-index/src/launch_gate_selftest.sh | tail -3
checks passed: 264   failed: 0
launch gate self-test OK — nothing was rented, no vendor was contacted,
and this Mac's real power settings were never read or changed.
$ echo "exit $?"
exit 0

$ experiments/06-mvm-0a-constructed-self-index/src/sleep_guard_selftest.sh | tail -3
checks passed: 67   failed: 0
sleep guard self-test OK — nothing was rented, no vendor was contacted,
and this Mac's real power settings were never read or changed.
$ echo "exit $?"
exit 0
```

264 and 67 are the figures in the findings' section 2. The two other checks the
findings' section 6 names also pass:

```
$ src/check_launcher_argument_guard.sh | tail -1
all checks pass. nothing was created and nothing was spent.
$ src/reap_handshake_selftest.sh | tail -2
checks passed: 26   failed: 0
reap handshake self-test OK — no machine was rented and no vendor contacted
```

## 2. The writer's mutation run reproduces exactly, and the gate is restored — MEASURED

Run once, on the merged tree. The output is identical to the block in the
findings' section 3, line for line, including the "REACHED THE RENTAL COMMAND"
lines, which name the stand-in and not the rental company:

```
$ shasum -a 256 src/launch_gate.sh
50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c  src/launch_gate.sh
$ python3 src/launch_gate_mutation_run.py
original launch_gate.sh sha256 50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c

# M1 warning only: the refusal prints and carries on
  launch_gate_selftest.sh: exit 1; checks passed: 204   failed: 60
      45 x FAIL: it went on past the gate to the next step
      15 x FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run …
  sleep_guard_selftest.sh: exit 1; checks passed: 60   failed: 7
      7 x FAIL: it ran on past the sleep check to the next precondition

# M2 the ledger check accepts anything
  launch_gate_selftest.sh: exit 1; checks passed: 175   failed: 89
      (thirteen kinds of failure, as in the findings)
      8 x FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run …
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0

# M3 the deadline-order check removed
  launch_gate_selftest.sh: exit 1; checks passed: 254   failed: 10
      1 x FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run …
  sleep_guard_selftest.sh: exit 0; checks passed: 67   failed: 0

# M4 the discharging-charger check removed
  launch_gate_selftest.sh: exit 0; checks passed: 264   failed: 0
  sleep_guard_selftest.sh: exit 1; checks passed: 63   failed: 4

restored; sha256 50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c matches original: True
$ shasum -a 256 src/launch_gate.sh
50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c  src/launch_gate.sh
$ git status --short src/
(nothing)
```

Every count matches the findings. The three lines abbreviated with "…" above
are the same stand-in command line the findings print in full.

## 3. This session's own deliberate break is caught — MEASURED

Done in a scratch copy of the whole experiment folder, not in the checkout, so
the file under review was never edited. The gate's one `exit 1` (line 407) was
replaced by a warning, and the scratch copy's own harness was run against it.

```
$ cp -R experiments/06-mvm-0a-constructed-self-index /Users/john/.claude/jobs/aa4e9c14/tmp/scratch/exp
$ cd /Users/john/.claude/jobs/aa4e9c14/tmp/scratch/exp
$ shasum -a 256 src/launch_gate.sh
50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c  src/launch_gate.sh
$ sed -i.orig 's/^  exit 1$/  echo "  (warning only — carrying on)" >\&2/' src/launch_gate.sh
$ shasum -a 256 src/launch_gate.sh
d0ad5a9272801bb0ea43e08a27e8953a4e9cd6bfad51830566a4ef9a2cbc0b5b  src/launch_gate.sh
$ diff src/launch_gate.sh.orig src/launch_gate.sh
407c407
<   exit 1
---
>   echo "  (warning only — carrying on)" >&2
$ src/launch_gate_selftest.sh | tail -2; echo "exit $?"
checks passed: 204   failed: 60
exit 1
$ grep FAIL scratch_selftest.out | sort | uniq -c
  45     FAIL: it went on past the gate to the next step
  15     FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run …
```

Same 204 and 60 as the writer's M1, and fifteen refusal cases reach the stand-in
rental command — which is what the harness exists to see. The checkout was
untouched throughout:

```
$ shasum -a 256 experiments/06-mvm-0a-constructed-self-index/src/launch_gate.sh
50b5257e238ab3b32109ed42bae3a4dc68d53f5021894258dbed6c8fa8892e7c  …/src/launch_gate.sh
$ git status --short
(nothing)
```

## 4. The gate is called before the first rental command in every launcher that has one; the registered launcher is untouched — MEASURED

Every code reference to the gate (documents excluded; comment lines trimmed to
the ones that matter):

```
$ git grep -n launch_gate -- ':!*.md'
…/src/launch_a3_fetch_first.sh:204:. "$SRC_DIR/launch_gate.sh"
…/src/launch_a3_fetch_first.sh:205:launch_gate
…/src/launch_ctl_pilot.sh:169:. "$SRC_DIR/launch_gate.sh"
…/src/launch_ctl_pilot.sh:170:launch_gate
…/src/launch_pilot_a1.sh:108:. "$SRC_DIR/launch_gate.sh"
…/src/launch_pilot_a1.sh:109:launch_gate
…/src/launch_gate.sh:337:launch_gate() {
(plus comment lines in those three launchers, launch_gate.sh, launch_gate_selftest.sh,
 launch_gate_mutation_run.py and sleep_guard_selftest.sh; none in launch_a3.sh)
```

The rental command lines (comments excluded), which is where the gate has to
come first:

```
$ grep -n 'runpodctl' src/launch_a3.sh src/launch_a3_fetch_first.sh src/launch_ctl_pilot.sh src/launch_pilot_a1.sh | grep -v ':[0-9]*:#'
launch_pilot_a1.sh:117:  runpodctl pod create --name "mvm-$OUT" \\       ← inside the dry-run text
launch_pilot_a1.sh:127:CREATE_OUT=$(runpodctl pod create --name "mvm-$OUT" \     ← the real one
launch_a3.sh:144:  runpodctl pod create --name "mvm-$OUT" \\               ← inside the dry-run text
launch_a3.sh:161:CREATE_OUT=$(runpodctl pod create --name "mvm-$OUT" \    ← the real one; NO gate above it
launch_ctl_pilot.sh:219:  runpodctl pod create --name "mvm-$OUT" \\       ← inside the dry-run text
launch_ctl_pilot.sh:236:CREATE_OUT=$(runpodctl pod create --name "mvm-$OUT" \     ← the real one
launch_a3_fetch_first.sh:255:  runpodctl pod create --name "mvm-$OUT" \\  ← inside the dry-run text
launch_a3_fetch_first.sh:278:CREATE_OUT=$(runpodctl pod create --name "mvm-$OUT" \  ← the real one
(the remaining hits are `pod get`, `pod delete`, and the on-machine `runpodctl config`
 and `remove pod` lines, all after the machine exists)
```

So: fetch-first, gate at 204–205, real rental at 278; control pilot, gate at
169–170, rental at 236; A1 pilot, gate at 108–109, rental at 127. Between the
gate call and the rental in each file there is only the local module self-test
loop and the check that the frozen battery files exist (verified by reading
lines 206–277, 171–235 and 110–126 with comments stripped: no `ssh`, `scp`,
`rsync`, `git` or `curl`).

The registered launcher's untouched state, on record three ways:

```
$ git diff --stat 97ee3c9 HEAD -- experiments/06-mvm-0a-constructed-self-index/src/launch_a3.sh
(nothing)
$ git diff --stat main...HEAD -- experiments/06-mvm-0a-constructed-self-index/src/launch_a3.sh
(nothing)
$ git rev-parse 97ee3c9:experiments/06-mvm-0a-constructed-self-index/src/launch_a3.sh HEAD:experiments/06-mvm-0a-constructed-self-index/src/launch_a3.sh
9b24d70ffc9c2d83abaf93aa5375b6fbe50d3fe9
9b24d70ffc9c2d83abaf93aa5375b6fbe50d3fe9
```

The dry-run flag is tested the same way by the gate and by all four launchers
(a non-empty test, so `DRYRUN=0` is a dry run everywhere, and there is no value
that the launcher reads as real while the gate reads as a rehearsal):

```
$ grep -n 'DRYRUN' src/launch_a3_fetch_first.sh src/launch_ctl_pilot.sh src/launch_pilot_a1.sh src/launch_a3.sh | grep -v ':[0-9]*:#' | grep 'if \['
launch_a3_fetch_first.sh:252:if [ -n "$DRYRUN" ]; then
launch_pilot_a1.sh:114:if [ -n "$DRYRUN" ]; then
launch_ctl_pilot.sh:216:if [ -n "$DRYRUN" ]; then
launch_a3.sh:141:if [ -n "$DRYRUN" ]; then
```

and `launch_gate.sh` line 374: `if [ -n "${DRYRUN:-}" ]; then`.

## 5. The charger case refuses, and its controls pass — MEASURED

The power reader was a stand-in reporting never-sleep **on**, drawing from
`AC Power`, battery line `87%; discharging; 3:12 remaining`; a good stand-in
ledger row; real mode (no dry-run flag); stand-in rental command first on the
path. All three launchers:

```
### 4a discharging, real launch → must refuse — launch_a3_fetch_first.sh
    exit status: 1
    2:  problem: this Mac is on wall power but its battery is discharging — the charger is not keeping up, and a flat battery ends the watchdog over a 24h run just as unplugging does
    7:  ok: ledger row at line 5 names 'gate_env_test', dated within 2 days, estimate written, no actual cost yet
    8:  REFUSING TO LAUNCH — the launch checklist is not met:
    10:      fix: use a stronger power adapter, or lighten the load until '…/pmset -g batt' reads charging or charged, then re-run
    stand-in rental command: never called
### 4a … — launch_ctl_pilot.sh        exit status: 1 … stand-in rental command: never called
### 4a … — launch_pilot_a1.sh         exit status: 1 … stand-in rental command: never called
```

(The other two launchers printed the same refusal text, differing only in the
watchdog's name.) The controls, through the A1 pilot:

```
### 4b discharging, with the sleep override ON → carried on out loud
    8:  OVERRIDDEN by ALLOW_LAPTOP_SLEEP=1 — carrying on anyway.
    9:  what was found: this Mac is on wall power but its battery is discharging — …
    15:launch gate: every check passed.
    STAND-IN RENTAL COMMAND WAS CALLED: pod create --name mvm-gate_env_test …
### 4c control: 'AC attached; not charging' (the battery-health hold) → must pass
    2:  ok: never-sleep override ON, running on wall power
    12:launch gate: every check passed.
    STAND-IN RENTAL COMMAND WAS CALLED: pod create --name mvm-gate_env_test …
### 4d control: 'charging' → must pass                      … every check passed … CALLED
### 4e 'finishing charge' (another word the Mac prints) → must pass … every check passed … CALLED
```

So the check refuses on the one word `discharging` and on nothing else the
battery line says, which is what the method's section 3a promises. In 4b the
override carries a discharging charger through, as designed: the override is a
spending choice said out loud, and the text says what was found.

## 6. The staged slice is refused against the real ledger, today, with the plain message — MEASURED

The staged slice launches through the fetch-first launcher with output name
`slice_handshake` (the corrected step 0 in `argument-guard-method.md` section
9). The real ledger has no row naming it:

```
$ grep -c slice_handshake experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
0
```

A dry run with the **real** power reader (read only) and the **real** ledger:

```
$ OUT=slice_handshake DRYRUN=1 src/launch_a3_fetch_first.sh      (stand-in rental command on PATH, empty HOME)
    exit status: 0
    2:  ok: never-sleep override ON, running on wall power
    11:  problem: no row in the ledger table names this run's output name 'slice_handshake'
    12:  WOULD REFUSE a real launch (this is a dry run, so it carries on and
    14:    - no row in the ledger table names this run's output name 'slice_handshake'
    15:      fix: write it before the machine exists: a row in the '## Ledger' table of …/compute-ledger.md, dated today (Pacific), naming 'slice_handshake', with a dollar figure in the $ est column and the actual left as —
    27:DRYRUN — nothing created, nothing spawned. Would run:
    stand-in rental command: never called
```

Real mode, real power reader, real ledger — today's actual state:

```
$ OUT=slice_handshake src/launch_a3_fetch_first.sh                (stand-in rental command on PATH, empty HOME)
    exit status: 1
    2:  ok: never-sleep override ON, running on wall power
    11:  problem: no row in the ledger table names this run's output name 'slice_handshake'
    12:  REFUSING TO LAUNCH — the launch checklist is not met:
    13:    - no row in the ledger table names this run's output name 'slice_handshake'
    14:      fix: write it before the machine exists: …
    stand-in rental command: never called
```

The same with a stand-in power reader reporting a safe Mac gave the same
refusal, so the ledger problem stands on its own. And at the launcher's default
output name the one real row that names it is found and declined by date, as
the findings' section 5 says:

```
$ src/launch_a3_fetch_first.sh        (default OUT=a3_30m_seed0, safe stand-in power reader, real ledger)
    11:  problem: rows in the ledger name 'a3_30m_seed0' but none will do: line 74 is dated 2026-09-21, 3 days ago (must be within 2)
    12:  REFUSING TO LAUNCH — the launch checklist is not met:
    stand-in rental command: never called
```

Note that the "3 days ago" reading exits at the date test, so **the real
ledger has never exercised the estimate and actual-cost columns of the check**.
That is why section 8 below builds rows to do it.

## 7. Nothing in the diff contacts a vendor — MEASURED

```
$ git diff main...HEAD > pr33.diff; wc -l pr33.diff
1924
$ grep -n -i 'runpod\|curl\|wrangler' pr33.diff
12:+(commit `b98c4e2`). Nothing was rented, the rental company (RunPod) was not
51:+files that contain the rental command, `runpodctl pod create`, that was the
87:+power readings and ledger; a stand-in `runpodctl` first on the command path,
116:+      15 x FAIL: REACHED THE RENTAL COMMAND: pod create --name mvm-gate_test_run --template-id runpod-torch-v280 …
134:+      8 x FAIL: REACHED THE RENTAL COMMAND: pod create … runpod-torch-v280 …
142:+      1 x FAIL: REACHED THE RENTAL COMMAND: pod create … runpod-torch-v280 …
335:+creates a machine, contacts the rental company (RunPod) or spends money.*
356:+`runpodctl pod create` (ruling `docs/rulings/2026-09-22-launcher-argument-guard.md`
550:+2. a stand-in `runpodctl` is first on the command path, records that it was
553:+3. `HOME` points at an empty temporary folder, so even the real `runpodctl`,
556:+Before each run the harness checks that the command path resolves `runpodctl`
692:-#     `runpodctl pod create` runs.
750:-# reap_handshake_selftest.sh plays on runpodctl.
1004:+# reap_handshake_selftest.sh plays on runpodctl.
1404:+#   2. a stand-in `runpodctl` sits first on the command path. It rents
1409:+#   3. HOME is an empty temporary folder, so even the real `runpodctl`, if
1452:+cat > "$T/bin/runpodctl" <<FAKE
1454:+echo "\$*" >> "$T/runpodctl.calls"
1457:+chmod +x "$T/bin/runpodctl"
1459:+if [ "$(PATH="$SAFE_PATH" command -v runpodctl)" != "$T/bin/runpodctl" ]; then
1460:+  red "the stand-in runpodctl is not first on the command path — stopping before any launcher runs"
1504:+  rm -f "$T/runpodctl.calls"
1521:+  rm -f "$T/runpodctl.calls"
1529:+called()   { [ -s "$T/runpodctl.calls" ]; }
1550:+  called && bad "REACHED THE RENTAL COMMAND: $(head -1 "$T/runpodctl.calls")" \
1565:+  if called && grep -q "pod create" "$T/runpodctl.calls"; then
1823:-  CREATE_LINE=$(grep -n '^CREATE_OUT=\$(runpodctl pod create' "$LAUNCHER" | head -1 | cut -d: -f1)
1842:+    CREATE_LINE=$(grep -n '^CREATE_OUT=\$(runpodctl pod create' "$SRC_DIR/$L" | head -1 | cut -d: -f1)
```

Every hit is one of: prose in the two documents (12, 51, 87, 116, 134, 142,
335, 356, 550–556); a comment (692, 750, 1004, 1404, 1409); the harness writing
its stand-in file (1452–1460), clearing or reading the stand-in's log
(1504–1565); or a search pattern the sleep harness uses to find a line number
(1823, 1842). No added line runs the rental tool. A second sweep for other ways
of reaching the network, on added lines with comments excluded:

```
$ grep -n '^+' pr33.diff | grep -i -E '\bssh\b|\bscp\b|https?://|\bwget\b|\bnc\b|api\.|apiKey' | grep -v '^[0-9]*:+#'
(nothing)
```

And the set of code files that contain the rental command is the four
launchers plus the two harnesses, whose occurrences are the stand-in and the
search pattern above:

```
$ git grep -l 'pod create' -- ':!*.md'
…/src/launch_a3.sh
…/src/launch_a3_fetch_first.sh
…/src/launch_ctl_pilot.sh
…/src/launch_gate_selftest.sh
…/src/launch_pilot_a1.sh
…/src/sleep_guard_selftest.sh
```

## 8. The ledger check against rows this session did not write, and rows shaped like the real ledger's — MEASURED

The method's section 3c says the columns are counted from the right-hand end
"because a `|` inside the prose of the 'what ran' column (the 2026-08-17 row has
one) shifts every column counted from the left." Counting the cells of every
row in the real table:

```
$ awk -F'|' '/^## Ledger[ \t]*$/{f=1;next} f && /^## /{exit} f && /^\| 20/{n=NF; if ($n ~ /^[ \t]*$/) n--; print NR": "(n-1)" cells; trailing pipe: "(($NF ~ /^[ \t]*$/)?"yes":"NO")}' compute-ledger.md
59: 8 cells; trailing pipe: yes
60: 8 cells; trailing pipe: yes
61: 8 cells; trailing pipe: yes
62: 8 cells; trailing pipe: yes
63: 8 cells; trailing pipe: yes
64: 10 cells; trailing pipe: NO
65: 8 cells; trailing pipe: yes
… (66–74: 8 cells, trailing pipe yes)
$ sed -n 64p compute-ledger.md | awk -F'|' '{for(i=2;i<=NF;i++) printf "  cell %d: %s\n", i-1, substr($i,1,70)}'
  cell 1:  2026-08-17
  cell 2:  registered (A2, wave 2/5)
  cell 3:  **WAVE 2 COMPLETE 2026-08-18. ⚠ THE DESIGN'S CENTRAL PREDICTION INV
  cell 4:  head -6` on the launcher output SIGPIPE-killed the script mid-launch      ← the pipe in the prose
  cell 5:  2× RTX 5090 SECURE EU-RO-1 $0.99/hr
  cell 6:  est ~10h + ~15h → **9.63h train / 10.16h pod (twin, 0.34 s/step) +
  cell 7:  ~$25 the pair + drip                                                     ← $ est
  cell 8:  **~$31.63** (balance-implied $174.27→$142.64). **Includes ~$5.7 of      ← $ actual
  cell 9:  ~$149.8 + $31.6 → **~$181.4 / $400 (A2)**; balance $142.64               ← running total
  cell 10:  **ANNOTATION 2026-09-16 (John's ruling; the row above is unchanged an   ← an annotation, appended as a cell
```

The 2026-08-17 row has the pipe in its prose **and** an annotation appended as
a tenth cell with no closing pipe. Counted from the right, the gate reads its
running total as the actual cost and its actual cost as the estimate. On that
row the date test fires first, so nothing is visible today. To see what the
shape does to a row that should pass, this session sourced the gate and ran its
ledger function directly against copies of the real ledger with one row
appended after line 74, dated today, naming `slice_handshake`:

```
$ . src/launch_gate.sh; LEDGER=<copy> OUT=slice_handshake _gate_ledger

B1 well-formed row, 8 cells, trailing pipe
     ok: ledger row at line 75 names 'slice_handshake', dated within 2 days, estimate written, no actual cost yet
B2 a pipe inside the prose, trailing pipe, no annotation (the shape the method describes)
     ok: ledger row at line 75 names 'slice_handshake', dated within 2 days, estimate written, no actual cost yet
B3 the 2026-08-17 row's actual shape: pipe in prose AND an annotation cell appended, no trailing pipe
     problem: rows in the ledger name 'slice_handshake' but none will do: line 75 has no dollar figure in its estimate column
B4 no pipe in prose, but an annotation cell appended WITH a trailing pipe
     problem: rows in the ledger name 'slice_handshake' but none will do: line 75 has no dollar figure in its estimate column
B5 actual cost already written ('**about $0.02** — a machine nobody meant to create')
     problem: … line 75 already records an actual cost ('about $0.02 — a machine nobody meant to create '), so it belongs to a launch that has happened
B6 estimate in words, no dollar sign ('about one dollar')
     problem: … line 75 has no dollar figure in its estimate column
B7 estimate '$ 1.00' with a space after the sign
     problem: … line 75 has no dollar figure in its estimate column
B8 row dated two days ago
     ok: ledger row at line 75 names 'slice_handshake', dated within 2 days, …
B9 row dated three days ago
     problem: … line 75 is dated 2026-09-21, 3 days ago (must be within 2)
B10 row names slice_handshake_v2 only
     problem: no row in the ledger table names this run's output name 'slice_handshake'
B11 row names slice_handshake-v2 only
     ok: ledger row at line 75 names 'slice_handshake', dated within 2 days, estimate written, no actual cost yet
B12 actual cell 'not launched yet'
     ok: ledger row at line 75 …
B13 actual cell 'nothing yet' (a phrase the list does not know)
     problem: … line 75 already records an actual cost ('nothing yet '), so it belongs to a launch that has happened
B14 row with only 7 cells (running total left off)
     problem: … line 75 has no dollar figure in its estimate column
```

Against the real ledger's own rows: `SIGPIPE-killed`, a word that appears only
in row 64, is found at line 64 and declined by date (38 days), so the matching
and the date reading work on that row; `ctl_pilot`, `a3_30m_seed0` and
`slice_handshake` behave as the findings say.

**What B3 and B4 show.** A good row with an annotation cell appended — the
shape the ledger already uses, at row 64, for a ruling that leaves the row
unchanged — is refused with the reason "no dollar figure in its estimate
column", because the gate read the row's actual-cost cell (`—`) as the estimate.
The direction is safe (a refusal), but the reason is wrong, and an operator who
follows the fix message will find a dollar figure already there. The method's
sentence about the 2026-08-17 row claims a record handles a case that the
record shows it does not: the shape of failure 4 in `docs/known-failure-modes.md`,
in an unregistered document.

**What B11 shows.** The whole-word pattern treats `-` as a boundary, and `-` is
a character the gate allows in output names (line 260). A row for
`slice_handshake-v2` satisfies a launch of `slice_handshake`. This is in the
money direction — a launch goes through on a row that belongs to a different
run — though the row still carries an estimate someone wrote, so it is a
misattribution and not an unpriced launch.

**What B7 and B13 show.** Formats the pattern does not know are refused with a
message that is wrong in a small way (`$ 1.00` has a dollar figure; `nothing yet`
is not an actual cost). Safe direction, and the fix message says what to write,
so these are noted and not listed as changes.

## 9. The move of the sleep check — ARGUED from the diff, MEASURED by the harnesses

Read side by side, the fetch-first launcher's sleep block at `97ee3c9` and
`_gate_sleep` plus the decision in `launch_gate.sh`: the reading of the
never-sleep setting, the power source and the idle timers is the same code; the
four refusal branches (setting unreadable, setting off, power source unreadable,
not wall power) are the same text; the override still takes the value `1` and
no other; the "ok" report is the same five lines. What changed, beyond what the
findings' section 8.7 says was closed (the `discharging` branch; the dry-run
preview saying a non-1 value would not be taken):

- the refusal heading is now `REFUSING TO LAUNCH — the launch checklist is not
  met:` followed by a list, instead of `REFUSING TO LAUNCH: <reason>`; and the
  closing line reads `To launch on a Mac that can sleep anyway, knowing what it
  costs:` instead of `To launch anyway, knowing what the paragraph above costs:`;
- the override's cost paragraph now has two forms, chosen by whether the
  launcher defines `GRACE_S` (the on-machine watcher's grace period); the two
  pilots have none and get a paragraph saying the machine keeps billing to its
  own deadline, which is what those launchers do;
- the override paragraph and the dry-run preview are printed once for the whole
  gate rather than inside the sleep block.

None of these change what is refused or allowed; the sleep harness's 67 passes
cover the behaviour. The fetch-first launcher's header sentence "moved …
unchanged" is true of the behaviour and the reasons and not quite of the
wording. No reference to the old block's variables survives in any launcher:

```
$ grep -n 'PMSET\|SLEEP_REFUSAL\|SLEEP_FIX\|POWER_SOURCE\|IDLE_AC\|IDLE_BATT\|SLEEP_OVERRIDE' src/launch_a3_fetch_first.sh src/launch_ctl_pilot.sh src/launch_pilot_a1.sh | grep -v ':[0-9]*:#'
(nothing)
```

The findings' section 8.7 claim about the preview, re-run:

```
$ DRYRUN=1 ALLOW_LAPTOP_SLEEP=0 src/launch_pilot_a1.sh     (stand-in power reader: never-sleep off; stand-in ledger; stand-in rental command)
    exit status: 0
    8:  WOULD REFUSE a real launch (this is a dry run, so it carries on and
    10:    - the never-sleep override is OFF (SleepDisabled 0) — shut the lid and this Mac sleeps, taking the watchdog with it
    12:      (ALLOW_LAPTOP_SLEEP is set to '0', which is not 1, so a real
    17:DRYRUN — nothing created. Would run:
    stand-in rental command: never called
```

## 10. The drafted amendment for the registered launcher — ARGUED, with the variables MEASURED

The method's section 7 proposes inserting four lines into `launch_a3.sh` after
its settings block and before its dry-run block, and changing its watchdog line
to spawn `"$CAFFEINATE"` and `"$WATCHDOG"` instead of the literal command and
path. Checked against the registered file:

```
$ grep -n 'WATCH_H=\|TERM_H=\|^OUT=\|GRACE_S\|SRC_DIR=\|EXP_DIR=\|^set \|nohup caffeinate' src/launch_a3.sh
55:set -uo pipefail
57:EXP_DIR="$(cd "$(dirname "$0")/.." && pwd)"
58:SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
64:OUT="${OUT:-a3_$(echo "$SCALE" | tr 'A-Z' 'a-z')_seed${SEED}}"
70:TERM_H="${TERM_H:-24}"
71:WATCH_H="${WATCH_H:-24}"
342:nohup caffeinate -dimsu bash "$SRC_DIR/watch_run_a3.sh" "$ENVF" \
```

Every variable the gate reads from the launcher (`DRYRUN`, `OUT`, `WATCH_H`,
`TERM_H`, `SRC_DIR`, `EXP_DIR`) exists in the registered file before line 141,
where its dry-run block starts; `GRACE_S` does not, and the gate reads it as
optional, so the override paragraph would take the "no watcher on the machine"
form — which describes `launch_a3.sh`, whose machine-side stop is a plain
sleep-then-remove (line 299). The watchdog line at 342 is the one the draft
names. So the draft is what it says it is: the gate call and the two variables
it needs, plus one line changed to read those variables.

Does it change anything beyond adding the gate call? Three things, one of which
the writer names:

1. **The registered launcher would read an unregistered file** — the writer's
   own point, and Gate A's to decide.
2. **`CAFFEINATE` becomes an environment input to registered text.** The gate
   checks only that the named command exists (`command -v`, line 205), not that
   it is the keep-awake command. `CAFFEINATE=/usr/bin/true` passes the gate and
   makes the watchdog spawn a no-op — a launch with no laptop watchdog. Setting
   it is a deliberate act, in the same class as `PMSET` and `LEDGER`, and
   nobody does it by accident; but the registration text has never had such an
   input, and the draft does not mention it. Not measured past the gate, since
   measuring it means reaching the spawn, which is after the rental command.
3. **A bare invocation on an unprepared Mac becomes a refusal** where today it
   launches — intended, and the reason for the amendment.

## 11. This Mac's never-sleep setting is now on — MEASURED, for John

The findings' section 5 read `SleepDisabled 0` and both earlier sleep-guard
checks the same day read the same. At the end of this session:

```
$ pmset -g | grep -i sleepdisabled
 SleepDisabled		1
$ pmset -g batt
Now drawing from 'AC Power'
 -InternalBattery-0 (id=23265379)	100%; charged; 0:00 remaining present: true
$ pmset -g log | grep -i 'disablesleep\|SleepDisabled' | tail -5
(nothing)
```

Nobody in this session changed it; the power log has no line for the change.
Two consequences. The findings' headline that "on this Mac, as it stands today,
every real launch through those three launchers would be refused" now holds
because of the ledger check alone (section 6 above, run 5c: the sleep check
passed, the ledger check refused). And the gate's own fix text says to put the
setting back afterwards; it is on now with no run in progress. Whether it stays
on is John's call, not a defect in the pull request.

## 12. The known-failure list's printed output has drifted — MEASURED

Failure 5 in `docs/known-failure-modes.md` prints the argument-guard check's
output with guard lines 104, 87 and 42 and vendor lines 227, 201 and 99, and
says a later reader should expect it to differ only in the prohibition block.
Today's output names other lines:

```
  [ ok ] launch_a3_fetch_first.sh guard (line 119) precedes any vendor command (line 255)
  [ ok ] launch_ctl_pilot.sh guard (line 93) precedes any vendor command (line 219)
  [ ok ] launch_pilot_a1.sh guard (line 48) precedes any vendor command (line 117)
```

Part of that drift predates this pull request: at `97ee3c9` the guard's `if`
line sits at 122, 96 and 51 in the three launchers and the real rental line at
404, 218 and 109 (`git show 97ee3c9:<file> | grep -n`), already away from the
printed figures. This pull request moves them again (now 128, 102, 57 and 278,
236, 127 by the same grep; the check anchors on the first line mentioning
`RT-198` in the guard's comment and on the first non-comment `runpodctl` line,
which is why it prints 119, 93, 48 and 255, 219, 117 — verified at
`check_launcher_argument_guard.sh` lines 68–69). The list is binding text and not touched here;
this is recorded so the session that next runs the failure-mode pass is not
surprised by a `cmp` that differs.

---

## What must change before this is relied on

1. **The method's claim about the 2026-08-17 row (section 3c, and the matching
   comment at `launch_gate.sh` lines 239–241).** The sentence says counting from
   the right handles that row's pipe-in-prose; the row also carries an appended
   annotation cell with no closing pipe, and on that shape the right-count reads
   the wrong columns (section 8, B3 and B4). Either state the rule the check
   actually enforces — a row of exactly eight cells ending in a pipe, with any
   annotation kept out of the row — in the method, the comment and the refusal's
   fix text, so the operator writes a row the gate can read; or make the check
   say so when a row has more or fewer than eight cells, instead of reporting a
   missing dollar figure that is not missing. The first is a wording change and
   is enough; the second is a few lines. Not a hole: every wrong reading refuses.

2. **The word-boundary class should exclude the characters an output name may
   contain.** Line 270 treats `-` and `.` as boundaries while line 260 allows
   them in `OUT`, so `slice_handshake-v2` satisfies `slice_handshake` (section
   8, B11). Change `[^A-Za-z0-9_]` to `[^A-Za-z0-9_.-]` on both sides of the
   name, and add the case to the harness beside 2b so it is seen to fail first.

## Open items, carried and not ruled on here

The writer's ARGUED limits (findings, section 8) are carried as open items and
not as findings; this session agrees with all seven as stated. Added to them:

- **The two-day limit (a judgment call the writer asked about).** ARGUED: right
  for the roadmap as written — rows are opened on the Saturday for launches
  that night or Sunday — and the boundary behaves as stated (B8 passes at two
  days, B9 refuses at three). A row written on a Thursday for a Sunday launch
  will be refused and the fix text says what to do. The explicit-key
  alternative the method set aside is the right answer if that refusal ever
  bites in practice, not a looser limit.
- **`WATCH_H ≤ TERM_H` (the other judgment call).** ARGUED: right as an order
  rule and not a bound, as the writer says. Equal deadlines pass the gate (case
  9b) and mean both stops fire in the same minute; whether the shutdown
  handshake handles that race is `reap-shutdown-order-method.md`'s question and
  not the gate's, and it was not opened here.
- **`CAFFEINATE` as an input** (section 10, item 2), for the Gate A amendment
  and, less urgently, for the three unregistered launchers.
- **The never-sleep setting is on** (section 11), for John.
- **The known-failure list's printed line numbers** (section 12), for the next
  failure-mode pass.
- **Wrong-reason refusals on formats the pattern does not know** (`$ 1.00`,
  `nothing yet`; section 8, B7 and B13). Safe direction; noted for the day the
  explicit-key alternative is weighed.
- **The 59-pass figure for the old harness** was not re-run here (see "What was
  opened").

## Files this session wrote

Only this file. Scratch material lives under
`/Users/john/.claude/jobs/aa4e9c14/tmp/` and is not part of the repository:
the three test scripts (`ledger_shapes.sh`, `gate_env_cases.sh`, `override0.sh`),
their outputs, the fourteen shaped ledger copies, the scratch copy of the
experiment folder with the broken gate, and the saved harness outputs.
