# Check of the rented slice's findings and the launcher fix, at commit `8aaf6e4`

*2026-09-25 (Pacific). A check under the pairing rule of
`docs/outside-review-protocol.md` (whatever one session writes, a different
session checks). Its target is branch `worktree-w1f-launcher-fix` at commit
`8aaf6e4`, open as draft pull request 48, which carries two pieces of work
checked together here:*

- *(A) the account of the first rented-slice attempt,
  `docs/2026-09-25-rented-slice-findings.md` ("the findings"), with its row in
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md` ("the
  ledger row"). They arrive as commits `8af960a` and `45157f6`, the head of
  draft pull request 46; `8aaf6e4` sits directly on top of `45157f6`, so the
  branch carries them unchanged rather than through a merge commit.*
- *(B) the launcher fix, `docs/2026-09-25-launcher-fix.md` ("the fix
  document"), commit `8aaf6e4`, acting on John's ruling of 2026-09-25
  ("agreed on all") on three things: cap and re-form the command that starts
  the machine's shutdown watcher (line 467 of the launcher at `4d98cfc`); a
  deadline on the laptop that deletes the machine when the hard cap is spent;
  and failure 6 added to `docs/known-failure-modes.md`.*

*This session wrote neither. Nothing was launched, rented or spent. No
registered text, ruling or protocol text was edited.*

**Labels.** MEASURED: a command was run and its output is filed. ARGUED:
reasoning a reader can dispute. Every output cited below is filed in
`experiments/rehearsal-successor-measure/out/launcher-fix-check-2026-09-25/`,
called "this check's receipts" from here on, beside the script that produced
it. The first attempt's own receipts are in
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25/` on the
checked branch, called "the slice receipts".

**Plain terms.** *The launcher*: the unregistered script that rents a machine
and runs things on it, `experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`.
*The registered launcher*: `launch_a3.sh` beside it, which is registered text
and must not change. *The watcher*: `src/reap_agent.sh`, started on the rented
machine so it can delete itself once the laptop confirms it has the files.
*The machine deadline*: `src/machine_deadline.sh`, new in `8aaf6e4`, a small
program on the laptop that deletes the machine once the hard cap divided by
the hourly rate has passed. *Stand-in*: a fake version of a tool used in a
test so nothing real is rented. *Process group*: the set of processes a
terminal or tool signals together when it stops a job.

## Verdict, point by point

| # | What was asked | Result | Label |
|---|---|---|---|
| A1 | The ledger row quotes John's go verbatim | **PASS**, against the go as relayed to the slice session (all 858 characters identical). This session has not seen a message John typed himself; see A1 | MEASURED |
| A2 | The row carries an estimate dated before the machine's creation time in the log | **PASS.** Committed 23:47:19Z with the estimate and an empty actual; the launch gate read it at run time; the machine was rented at 23:48:33Z | MEASURED |
| A3 | $0.4974 matches the balance readings the findings quote | **PASS** as arithmetic (0.4973529112). **But the actual is not settled**: the vendor's per-machine billing has since posted at $0.3215, and the balance has fallen a further $0.0382 | MEASURED |
| A4 | The laptop hang reproduction reproduces from clean | **PASS.** 8 s and 0 s, twice, from an emptied environment | MEASURED |
| A5 | The machine's deletion is evidenced | **PASS.** Delete command answered `"deleted": true`; machine list empty then and now; billing for that machine stops in the hour it was deleted | MEASURED |
| A6 | "NO VERDICT" is the right handshake line, not "NOT TESTED" | **PASS** | ARGUED from the plan's own lines |
| B1 | The remote-forms check fails on the launcher at `4d98cfc` at line 467, and passes on the fix | **PASS**, both | MEASURED |
| B2 | The machine-deadline tests pass with a stand-in rental tool and a shortened clock | **PASS**, 20 passed and 0 failed | MEASURED |
| B3 | Paths where the deadline can fail to delete | **Four gaps found, none fatal to a watched second attempt.** A terminate signal to the launcher's process group kills the deadline; a hung rental tool stalls it forever; three failed tries end it for good; a "success" exit is trusted without reading the answer. Clock steps and sleep are argued below | MEASURED (four), ARGUED (clock, sleep) |
| B4 | `launch_a3.sh` is byte-identical to main | **PASS** | MEASURED |
| B5 | The four launcher self-tests pass | **PASS**: argument guard 21 checks, launch gate 369 and 0, sleep guard 67 and 0, shutdown handshake 26 and 0 | MEASURED |
| B6 | The folder-clear step refuses to run without `RUN_SUBDIR` | **PASS**, exit 2, with and without a dry run | MEASURED |
| B7 | Failure 6 is in the list's existing form, and its test reproduces | **PASS** on both | MEASURED |
| B8 | Regenerating the plan (main-checkout paths) reproduces the committed plan and `plan.diff` | **PASS**: plan identical byte for byte; diff content 111 of 111 lines identical | MEASURED |
| B9 | Step 0's dry run prints "machine deadline: ON … 7272s after creation", and step 1 requires "MACHINE DEADLINE ARMED" | **PASS**, both | MEASURED |
| B10 | The fix session's own calls, and whether each changes what the go must name | Nine calls listed; **three change what the go must name** (the new settings, the clear, and running only once merged) | ARGUED |

**Beyond the points asked** (section "Findings beyond the points asked"):
the new settings are **silently ignored** by main's launcher, so the plan run
before this branch merges would launch with no machine deadline, caught only
by a person reading step 0 (MEASURED); and two filed scripts hard-code another
session's temporary folder (MEASURED by reading).

## What was opened, and what was not

Opened: this repository's `CLAUDE.md`, the top entry of `STATUS.md`,
`docs/outside-review-protocol.md` (the pairing rule, the isolation section,
the failure-mode pass, Filing), `docs/known-failure-modes.md` at `4d98cfc` and
at `8aaf6e4`; at `8aaf6e4`: the findings, the fix document, the ledger row, the
diff of the launcher, `machine_deadline.sh`, `machine_deadline_selftest.sh`,
`check_remote_forms.py`, the diff of `stage_rented_slice.sh`, the regenerated
plan, and every file in both receipt folders I cite; at `4d98cfc`: the plan
file's outcome section and the launcher.

**One departure from the isolation section, stated so a reader can weigh
it.** To check that the go is verbatim I opened the transcript files of the
slice session and of the fix session, and read **only the first message of
each**: the brief each was given, which is the instructions sent to that
session, not anything that session wrote. The slice session's brief is the
only place in reach where John's go appears outside the ledger row. I did not
read either session's replies, reasoning or tool output.

Not opened: the staging document, `reap_agent.sh`, `watch_run_a3.sh`,
`launch_gate.sh`, the spending-proposal note of 2026-09-25, or pull request
descriptions.

## How it was run

Both commits were unpacked with `git archive` into this session's scratch
folder: `8aaf6e4` ("the fix copy") and `4d98cfc` ("the main copy"). Nothing
was run in the fix session's own folder or in the main checkout. Every
launcher run and self-test ran with a **blocking stand-in `runpodctl`** first
on the command path, which records and refuses any call that gets past the
test's own stand-ins; it recorded **zero calls** in every run
(`four-selftests.txt`, `folder-clear-refusals.txt`, `plan-regeneration.txt`
and the step 0 files). The vendor was contacted only for read-only listings:
the machine list, the balance, and the billing history (`vendor-readings.txt`).

This check's own scripts reference its scratch folder by absolute path, the
same portability defect noted of the fix session's scripts below; they record
what was run, and need that path changed to be run elsewhere.

## Part A — the findings and the ledger row

### A1. The go is quoted verbatim. PASS. MEASURED

`go-comparison.txt`: the go in the slice session's opening brief, which
introduces it as "John's go, verbatim", with line breaks folded to spaces, is
858 characters, and the quotation in the ledger row is the same 858
characters at both `8af960a` and `8aaf6e4`: `identical: True` twice. The
quotation did not change between the commit written before creation and the
commit that added the actuals.

**The limit.** The brief is John's instruction to that session and presents
the go as verbatim. I cannot see a message John typed on his own. If the go
was given elsewhere (a chat, a phone), that record is the one to hold the
quotation against.

### A2. The estimate predates creation. PASS. MEASURED

`ledger-row-timing.txt`:

```
8af960a… author 2026-09-25T16:47:19-07:00 committer 2026-09-25T16:47:19-07:00
 **est well under 1h**: … | **$0.75–1.00, hard cap $2.00** | —
  ok: ledger row at line 75 names 'slice_handshake', dated within 2 days, estimate written, no actual cost yet
creating SECURE pod (NVIDIA GeForce RTX 5090) for 10M/2000000 tok (out: slice_handshake)
  "lastStatusChange": "Rented by User: Fri Sep 25 2026 23:48:33 GMT+0000 (Coordinated Universal Time)",
2026-09-25T23:48:27Z
```

The row was committed at 16:47:19 Pacific (23:47:19Z) with the estimate and
an empty actual ("—"); step 1 began at 23:48:27Z (`step1-start.txt`); the
vendor's creation record says rented at 23:48:33Z, 74 seconds after the
commit. A commit's time is written by the laptop that makes it, so it is not
independent evidence on its own. The independent part is the launch log: the
launcher's own gate found the row, with "no actual cost yet", **before** it
printed "creating SECURE pod".

### A3. $0.4974 matches the balance readings. PASS, with a new reading. MEASURED

`vendor-readings.txt`: the findings' two readings, $76.4526535694 before
creation (`pre-user.txt` in the slice receipts) and $75.9553006582 after
deletion (`stop.txt`), differ by **0.4973529112**, which rounds to $0.4974.
That is what the findings and the ledger row say.

**The actual is not settled.** Read-only readings taken at 2026-09-26T01:25:56Z,
same file:

- The vendor's billing rows for this machine, `c14x21x0u3ju7r`, have now
  posted, which they had not by 00:22Z (`billing-this-pod.txt`): **$0.1562 +
  $0.1654 = $0.3215**, for 1,165,878 ms, **19.43 minutes billed**, against 31
  min 13 s of life. At $0.99 an hour those milliseconds are $0.3206; the rest
  is disk.
- The balance now reads **$75.917054611**, a further **$0.0382** below the
  00:22:10Z reading. The $0.01-an-hour storage charge accounts for about
  **$0.0106** of that over the 63 minutes to this reading.

So the balance says about $0.54 has left the account since before creation
(**$0.5356**), and the per-machine billing says $0.32 was charged for the
machine. Those two do not agree, and this session cannot say why from
read-only listings (ARGUED: a balance that debits ahead of the billing rows
settling would produce it, but nothing here shows that). The ledger row
already says its figure "may still move by that lag", and it is inside the
estimate and the cap on either reading. **Recommendation, not a ruling:**
read the balance and the billing rows again after a day and write the settled
figure as an annotation beside the row, not by editing it.

### A4. The hang reproduces from clean. PASS. MEASURED

`hang-reproduction-rerun.txt`, from `hang-reproduction-clean.sh`, which runs
the findings' two commands under `env -i` (an emptied environment) so nothing
carried over from this session's shell can matter:

```
2026-09-26T01:25:57Z
form as launched (cd && nohup ... &): returned after 8s
control (cd ; nohup ... &): returned after 0s
2026-09-26T01:26:06Z
form as launched (cd && nohup ... &): returned after 8s
control (cd ; nohup ... &): returned after 0s
```

Then the fix session's `hang-reproduction.sh`, with only its
scratch folder changed, gives the same two lines plus the launcher's own old
and new forms, `OLD … returned after 8s` and `NEW … returned after 0s`, with
the background program confirmed still running after the new form returned.
Same verdicts and same whole seconds as the findings.

### A5. The deletion is evidenced. PASS. MEASURED

From the slice receipts, `stop.txt`:

```
2026-09-26T00:19:45Z  runpodctl pod delete c14x21x0u3ju7r
                      {
                        "deleted": true,
                        "id": "c14x21x0u3ju7r"
                      }
2026-09-26T00:19:56Z  runpodctl pod list   ->  []
```

And this session's own reading, `vendor-readings.txt`:

```
2026-09-26T01:25:56Z
[]
```

The vendor's hourly billing for that machine has two rows, the 23:00Z hour
(566,260 ms) and the 00:00Z hour (599,618 ms), and none after. Neither is more
than the machine's actual life in that hour (687 s and 1,186 s, same file), so
nothing was billed after 00:19:46Z.

### A6. NO VERDICT is the right line. PASS. ARGUED

The plan the slice ran (`rented-slice-plan.txt` at `4d98cfc`, "What passing
looks like") defines the two candidates:

```
    NOT TESTED  the quiet one (staging document, section 6). The machine's
          own watcher never started: the launcher printed "SHUTDOWN WATCHER
          DID NOT START" or "REAP: pod-side reaping NOT armed", then fell
          back to "SHUTDOWN ORDER: the trainer deletes the machine itself"
          (or "LAPTOP ONLY"). …
    NO VERDICT  the slice does not run. Then the handshake is exercised
          against local stand-ins only, …
```

NOT TESTED is defined by three things: the watcher never starting, the
launcher saying so, and a fallback shutdown path. None happened. The watcher
started and logged "deletion is armed" at 23:49:28Z (`remote-state-at-stop.txt`),
and the launcher printed neither refusal line nor any fallback
(`step1-launch.txt` ends at "VERIFIED" and then "launcher exit=143"). Calling
it NOT TESTED would record that the watcher failed, which is false. NO
VERDICT's condition, "the slice does not run", is the closest fit: the run
stopped before training, the receipt, or the fetch, so no handshake signal
could occur. The fit is not exact ("does not run" versus "ran partway"), and
the findings say so honestly for throughput, where they record "not measured"
rather than force a line. For the handshake, NO VERDICT is right.

## Part B — the launcher fix

### B1. The remote-forms check: fails at `4d98cfc`, passes on the fix. PASS. MEASURED

`check-remote-forms-at-4d98cfc.txt`:

```
  [FAIL] launcher-4d98cfc.sh line 467: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] launcher-4d98cfc.sh line 547: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 552)
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: …
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang
1 problem(s). Nothing was rented and nothing was spent.
exit=1
```

`check-remote-forms-at-8aaf6e4.txt`:

```
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)
  [rejected] stand-in line 1: returned after 8.0s -- …
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang
all checks pass. Nothing was rented and nothing was spent.
exit=0
```

**What this check does not see (ARGUED).** It finds remote starts only in the
two shapes `$SSH "…"` and `ssh_capped N "…"` whose text contains `nohup`
(`check_remote_forms.py` lines 74 to 103). A future background start written
another way, with single quotes, with `setsid` instead of `nohup`, or through a
helper with a new name, would not be checked and would not be reported as
unchecked. Its "found no background start at all" line catches only the case
where it finds none. And it takes `ssh_capped`'s cap on trust; the 60-second
cut-off in `ssh_capped` (launcher line 473) is not itself exercised by any
test here, because the new form returns at once.

### B2. The deadline tests. PASS, 20 and 0. MEASURED

`selftest-machine-deadline.txt`, the fix's `machine_deadline_selftest.sh` run
unchanged: `20 passed, 0 failed`. The case that matters most: with the whole
launcher stuck on its first `ssh`, as on 2026-09-25, `creation to delete: 4s,
for a 4s deadline`. The negative control (a deadline 60 s away) deleted
nothing in 4 s.

### B3. Where the deadline can fail to delete. Four gaps. MEASURED and ARGUED

`deadline-failure-paths.sh` runs the real `machine_deadline.sh` at `8aaf6e4`
behind a stand-in rental tool, output in `deadline-failure-paths.txt`.

**(a) The rental tool errors on every call** (no network, or a revoked key).
MEASURED, case A: three attempts 20 s apart, then

```
delete command FAILED 3 times (exit 1) -- the machine may already be gone, or may still be billing: check the vendor's machine list NOW
  exit=1 after 61s; delete calls: 3
```

After that the program exits and nothing on the laptop tries again. The
message goes to `machine-deadline.log`, which nobody is watching by design
(the program exists for the case where nobody is). What stands behind it is
the watcher's own +24-hour deadline on the machine (`reaper.log`, "hard
deadline epoch", in the slice receipts), which is the roughly $24 exposure the
findings describe. Case B shows the retries do work when the network comes
back within them: fail, fail, then `DELETED` 42 s after the deadline.

**(b) The rental tool hangs.** MEASURED, case C: with a `pod delete` that never
returns, the program was `still waiting on attempt 1 after 20s (no time limit
on the delete call)`. It would wait forever; attempts 2 and 3 never happen.

**(c) The rental tool exits 0 without deleting.** MEASURED, case D: a stand-in
that prints `{"error": "pod not found"}` and exits 0 is logged as `DELETED by
the laptop's machine deadline`. The program trusts the exit status and never
reads the answer or lists machines afterwards. Whether the real tool ever
exits 0 on a failed delete is not known here; finding out needs a write call
to the vendor, which this session did not make. The slice receipts show what
a real success looks like (`"deleted": true` in `stop.txt`), so a check for
that, or a machine listing after the delete, is available.

**(d) The launcher's process group is stopped.** MEASURED, case E, three runs
each giving the same result. The deadline was started exactly as the
launcher starts it (`nohup "$CAFFEINATE" -dimsu bash machine_deadline.sh … &`,
line 436), from a parent in its own process group, and the whole group was
signalled one second in, with the deadline four seconds away:

```
  SIGINT to the group: delete calls after the deadline: 1
  SIGTERM to the group: delete calls after the deadline: 0
  SIGHUP to the group: delete calls after the deadline: 1
```

Ctrl-C and a closed terminal do not stop it. **A terminate signal to the
group does**, because `nohup` only shields against the hang-up signal and the
program is not started in a session of its own. On 2026-09-25 the slice
session stopped the launcher by its process number (`stop.txt`: `kill 39959`),
which would have left the deadline alive. **ARGUED:** a tool that stops a
background job by terminating its whole group, which is a common way to stop
a job, would take the deadline with it, silently, at exactly the moment a
person has decided something is wrong. Nothing in the fix, its tests or the
plan says which way a session should stop the launcher.

**(e) The laptop clock steps. ARGUED.** Both ends of the deadline are read
from the laptop's clock (`CREATED_AT_EPOCH` at launcher line 383, the loop at
`machine_deadline.sh` lines 50 to 55), so a difference between the laptop's
clock and the vendor's does not matter. What matters is the laptop's clock
jumping while the deadline waits. A jump forward deletes early, which costs a
run but not money. A jump backward delays deletion by the size of the jump.
Ordinary network time corrections on a Mac are small; a large backward jump
would need someone setting the clock by hand.

**(f) The laptop sleeps. ARGUED.** The program sleeps at most 30 s at a time
and re-reads the wall clock, so time asleep counts, as its header says. But a
program on a sleeping laptop does not run: if the laptop is asleep at the
deadline, the delete happens on waking, and the machine bills for the whole
sleep. Idle sleep is held off by the keep-awake command it runs under, and
the lid by the never-sleep override, which the launch gate checks **once, at
launch**. A sleep the override does not prevent (a flat battery, choosing
Sleep from the menu, someone turning the override off) is not covered. Waking
also tends to come before the network does, which is case (a): three tries in
about 40 s, then nothing. The fix document names the laptop-off case already;
the wake-without-network case is new here.

**What this adds up to (ARGUED).** The deadline does what it was ruled to do
in the case that happened on 2026-09-25, and the tests show it. None of the
four measured gaps is fatal to a second attempt that a session watches, as
the first was. Each is a place where "enforced by code" quietly becomes
"enforced if nothing else goes wrong", which is the pattern failure 5's lesson
warns about. Two are cheap to close: start the program in a session of its
own, so a group signal cannot reach it (macOS has no `setsid` command; a
one-line Python wrapper does it), and put a time limit on each delete call.
Retrying until a machine listing confirms the machine is gone would close (a)
and (c) together. These are proposals for John, not changes made here.

### B4. The registered launcher is untouched. PASS. MEASURED

```
$ git rev-parse 8aaf6e4:…/launch_a3.sh 4d98cfc:…/launch_a3.sh origin/main:…/launch_a3.sh
9b24d70ffc9c2d83abaf93aa5375b6fbe50d3fe9
9b24d70ffc9c2d83abaf93aa5375b6fbe50d3fe9
9b24d70ffc9c2d83abaf93aa5375b6fbe50d3fe9
```

The same content identifier at all three means the same bytes. No file under
`docs/rulings/`, the protocol, or any registration or amendment changed
between `4d98cfc` and `8aaf6e4` (checked with `git diff --name-only`).

### B5. The four launcher self-tests. PASS. MEASURED

`four-selftests.txt`, run on the fix copy with the blocking stand-in:

```
check_launcher_argument_guard.sh exit=0      all checks pass. (21 "[ ok ]" lines)
launch_gate_selftest.sh exit=0               checks passed: 369   failed: 0
sleep_guard_selftest.sh exit=0               checks passed: 67   failed: 0
reap_handshake_selftest.sh exit=0            checks passed: 26   failed: 0
calls that reached the blocking runpodctl:        0
```

(Condensed; the file has the full tails.) These are the counts the fix
document reports.

### B6. The folder clear refuses without `RUN_SUBDIR`. PASS. MEASURED

`folder-clear-refusals.txt`:

```
$ CLEAR_RUN_SUBDIR=1 DRYRUN=1 OUT=slice_handshake SCALE=10M MAXTOK=2000000 launch_a3_fetch_first.sh
refusing to run: CLEAR_RUN_SUBDIR=1 needs RUN_SUBDIR -- the shared run folder is never emptied
exit=2
$ CLEAR_RUN_SUBDIR=1 RUN_SUBDIR= DRYRUN= OUT=slice_handshake SCALE=10M MAXTOK=2000000 launch_a3_fetch_first.sh
refusing to run: CLEAR_RUN_SUBDIR=1 needs RUN_SUBDIR -- the shared run folder is never emptied
exit=2
```

The second is the non-dry path, run behind the blocking stand-in. The same
file shows `CLEAR_RUN_SUBDIR=yes` refused, and `RUN_SUBDIR` set to `.`, `..`
or `a/b` refused ("must be a plain folder name", line 187), so the shared
folder cannot be reached by spelling it differently. **ARGUED, minor:** the
clear command puts the folder inside single quotes (line 509), so a folder
name containing a single quote would break out of them. Only the operator
sets that name and the plan sets `slice_handshake`; not tested.

### B7. Failure 6: the list's form, and its test. PASS. MEASURED

Form: failure 6 carries the same five headings in the same order as failure
5, the list's newest entry before it: "What it was", "How it showed up", "The
fix", "The test", "What the output has to show" (read with `grep -n` on
`docs/known-failure-modes.md` at `8aaf6e4`, the entry starting at line 807). It prints its
test command and its output, prints the output on the design that produced
the finding (the `4d98cfc` launcher), explains its negative control, and says
what it does not cover. That is the standard the list's "Adding to this list"
section sets.

Reproduction: the entry's two commands, run as printed with `$TMPDIR` pointed
at this session's scratch folder, give the verdicts the entry prints and the
same whole seconds (B1 above; the entry itself warns the tenths will differ).
Its reproduction block also reproduces (A4).

Two things about the list, **neither this entry's fault and not edited
here**: its opening says "Five things have gone wrong" (the entry says so
itself), and "Adding to this list" still says "one of the four above", which
was already one behind before this entry. Both are binding text, so they are
for a proposal, not a quiet fix.

### B8. The plan, regenerated. PASS. MEASURED

`plan-regeneration.txt`: the stager at `8aaf6e4`, run in the fix copy with
`RUN_FROM` left at its default (the main checkout's path), passed every
precondition and wrote a plan that is **identical** to the committed plan
(`cmp`). Rebuilding the diff from the `4d98cfc` plan to it
(`plan-regenerated.diff`) and comparing its content lines with the filed
`plan.diff`, leaving out only the four header lines that name file paths and
content identifiers: **111 lines against 111, `hunks identical`**. The
regenerated plan names neither a worktree nor a scratch folder (`grep -c` gives
0).

### B9. Step 0's dry run, and step 1's requirement. PASS. MEASURED

`step0-at-8aaf6e4.txt`, from the fix session's `step0-dryrun-behind-standins.sh`
with only its two folder paths changed:

```
  machine deadline: ON -- hard cap $2.00 at $0.99 an hour:
    this laptop deletes the machine 7272s after creation, whatever
    the run is doing (sooner if the vendor states a higher rate)
  …
  clear the run folder, before the shutdown watcher starts:
    list, then empty, /workspace/mvm-out/slice_handshake
…
exit=0
stand-in runpodctl calls: 0
stand-in ssh calls: 0
```

7272 is $2.00 ÷ $0.99 × 3600 = 7272.7 seconds, cut to whole seconds
(`vendor-readings.txt`, arithmetic). Step 1 of the regenerated plan
(`rented-slice-plan.txt` at `8aaf6e4`, lines 49 to 53):

```
  Straight after "pod:" it must print "MACHINE DEADLINE ARMED", with the
  time this laptop will delete the machine: 2 h 01 min (7272s)
  after creation, which is the hard cap of $2.00 at $0.99 an
  hour. If it does not, delete the machine at once
  (runpodctl pod delete <id>) and stop: the cap is not enforced.
```

### B10. The fix session's own calls, and the go. ARGUED

The fix document's "Who decided what" lists these as the session's own
decisions, made while building. For each, whether a go for a second attempt
has to name it. The first go named its settings one by one ("with the
settings the plan prints: … RUN_SUBDIR=slice_handshake …"), so a setting the
plan newly passes is something the go names.

| # | The session's call | Changes what the go must name? |
|---|---|---|
| 1 | The command form `cd … \|\| exit 1; nohup … &`, and the `ssh_capped` helper | **No.** It is how the ruled fix is carried out, inside the launcher; it sets nothing the operator types |
| 2 | The setting names `HARD_CAP_USD`, `RATE_PER_HOUR_USD`, `CLEAR_RUN_SUBDIR` | **Yes.** They are new settings in the step 0 and step 1 commands. A go that lists settings, as the first did, has to list these three with their values ($2.00, $0.99, 1) |
| 3 | Counting the deadline from just before the create call | **No.** It can only make the deadline earlier than the bill's start, which is the safe direction |
| 4 | Using the vendor's stated rate when it is higher than the one given | **No.** It can only bring the deadline sooner. Worth one clause if John wants the go to say what happens at a higher rate; the first attempt's ledger row had its own line for that (delete at once above $0.99) and the two now overlap |
| 5 | Deleting without checking whether the machine is already gone, and retrying three times | **No**, but see B3 (a) and (c): these are where the deadline can fail. John may want them fixed before the go rather than named in it |
| 6 | Clearing the whole slice folder rather than only the marker files | **Yes.** The brief asked for a step that "checks and clears that folder". Emptying the whole folder deletes files on the persistent network volume, which the first go did not cover. Today that is one 469-byte `reaper.log` whose content is already filed (`remote-state-at-stop.txt`). The go should say the clear is authorised |
| 7 | Adding the remote-forms check to the stager's preconditions | **No.** Staging refuses sooner; nothing about the run changes |
| 8 | The new outcome line "CUT OFF BY THE CAP" | **Named by naming the plan's commit.** It is a result line written by the session, not by John, before the run. A go that names the regenerated plan at its commit adopts it; John may want to read it first, since it decides how a capped run is reported (never as a handshake pass) |
| 9 | Printing main-checkout paths when the plan is regenerated from a worktree | **Yes**, see the next section: the plan only works once this branch is on main and the main checkout is updated. The go should name that commit, not `8aaf6e4` on a side branch |

## Findings beyond the points asked

### F1. Main's launcher silently ignores the new settings. MEASURED

`step0-new-settings-on-main-launcher.txt`: step 0 of the regenerated plan,
run with its new settings against the **main** copy's launcher (`4d98cfc`,
which is what the main checkout holds until this branch merges):

```
DRYRUN — nothing created, nothing spawned. Would run:
…
exit=0
stand-in runpodctl calls: 0
```

and `grep -c 'machine deadline'` on that output gives **0**. The new settings
are environment variables, not arguments, so the argument guard of failure 5
does not see them. The old launcher accepts them, ignores them, and would
launch with **no machine deadline and the uncapped watcher start**, the exact
configuration that hung on 2026-09-25. The only thing that catches it is the
plan's instruction to stop if step 0 does not print the two new lines, which
depends on a person reading the output. (The previous re-check,
`reviews/2026-09-25-rented-slice-plan-recheck-claude-worktree.md`, point 1,
noted the same dependence for the previous change.) **ARGUED:** the go should
name the merged commit on main, and the session running it should confirm the
main checkout is at that commit before step 0. A launcher that refuses
settings it does not recognise would close this for good, and would itself be
a change for John to rule on.

### F2. Two filed scripts hard-code another session's scratch folder. MEASURED by reading

`hang-reproduction.sh` writes into `/Users/john/.claude/jobs/3eb5118f/tmp`,
and `step0-dryrun-behind-standins.sh` reads the launcher from the fix
session's worktree folder, `.claude/worktrees/w1f-launcher-fix`. Both folders
belong to one session and will go when it is cleaned up; the first script
will then quietly recreate a folder in another job's space. This check ran
both with only those paths changed (`step0-at-8aaf6e4.sh` and
`hang-reproduction-rerun.txt` show how). Minor; it affects re-running, not
what the outputs show.

## The failure-mode pass

Not owed here: the protocol's failure-mode pass applies to texts going
through Gate A (registrations, amendments, threshold locks, pre-statements),
and none of these is one. The two entries whose tests are about launchers
were run: failure 5's test is inside B5 (the argument guard, 21 checks), and
failure 6's is B1 and B7. Failures 1 to 4 test measurement designs, and
neither document states a measure; they were not run.

## For John, before a go (ARGUED; nothing here is ruled)

1. **Settle the first attempt's actual.** Read the balance and the machine's
   billing rows after a day; annotate the row with the settled figure (A3).
2. **Decide whether to close the four deadline gaps first** (B3): a session of
   its own for the deadline program, a time limit on each delete, and retrying
   until a listing confirms the machine is gone. Confidence that the first two
   close (d) and (b): high, since each is exactly the missing piece. Standard
   practice for a watchdog that must outlive its parent is its own session.
   The strongest alternative is to change nothing and keep the second attempt
   watched, as the first was, which the cap then backs up.
3. **Say how a session stops the launcher**: by its process number, not its
   process group, while (d) stands.
4. **The go should name**: the merged commit on main (not `8aaf6e4`); the
   three new settings with their values; that the clear may empty
   `/workspace/mvm-out/slice_handshake`; and, by naming the plan's commit,
   the new "CUT OFF BY THE CAP" line.

## What this check does and does not license

It licenses reading the findings as an accurate account of the first attempt,
on every point asked, with the actual still to settle; and reading the fix as
doing what John ruled, tested as it says. It does not license launching:
that needs John's go, and this branch merged first (F1). It does not show that
the deadline holds against the four failures in B3, or that `ssh_capped`'s
60-second cut-off works on a real connection; nothing here reached a real
machine.
