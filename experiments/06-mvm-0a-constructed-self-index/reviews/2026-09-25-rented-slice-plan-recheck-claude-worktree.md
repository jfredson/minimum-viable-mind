# Re-check of the rented-slice plan after its fix, at commit `425334f`

*2026-09-25 (Pacific). A check under the pairing rule of
`docs/outside-review-protocol.md` (whatever one session writes, a different
session checks). It re-runs the check of the plan at `60d1496`
(`reviews/2026-09-25-rented-slice-plan-check-claude-worktree.md`, merged as
pull request 38, "the first check" below) against the fix for that check's
findings: commit `425334f` on branch `worktree-rented-slice-staging-fixes`,
open as draft pull request 42 ("the fix" below).*

*This session did not write the fix, the plan, the staging script or the
staging document, and has not read the chat of any session that did. It read
the fix's commit message and pull request description. Nothing was launched,
rented or spent. No registered text, ruling or protocol text was edited.*

**The target.** `experiments/rehearsal-successor-measure/out/rented-slice-plan.txt`
as committed in `425334f` (the "plan file"), and the four files that commit
changes: the unregistered launcher `launch_a3_fetch_first.sh`, the timing
script `bench_arms.py`, the staging script `stage_rented_slice.sh`, and the
plan file itself. The "staging document" is
`docs/successor-rented-slice-staging-2026-09-21.md`. The fix is one commit on
top of `57636c0` (the first check's merge). Main has moved on twice since
then, with the A3 closure dispositions (pull request 37) and the Weekend 1
queue ruling (pull request 39). Neither touches any file the fix changes.

**Labels.** MEASURED: a command was run and its output is printed here.
ARGUED: reasoning a reader can dispute.

## Verdict, point by point

The first check's six points, then its two findings beyond them, then the four
extra confirmations asked for this time.

| # | What was asked | Result | Label |
|---|---|---|---|
| 1 | Every path in the plan file resolves | **PASS.** Every laptop path, machine path and quoted log line exists in the code that prints it. The main checkout still holds main's launcher and timing script until pull request 42 merges and the checkout is updated. The plan's new step-0 stop instruction catches an out-of-date launcher (check 1) | MEASURED |
| 2 | Every command matches the staging document, sections 1 to 6, with step 0 withdrawn | **PASS.** The fourth outcome (the machine's own shutdown watcher never starting) is now in the plan, and step 3 no longer says "and nothing else". First check's finding A: **fixed.** One departure is not stated in the plan (section 4, see check 2) | MEASURED; the departure ARGUED |
| 3 | The launcher named is `launch_a3_fetch_first.sh`, not the registered `launch_a3.sh` | **PASS** | MEASURED |
| 4 | Hard cap $2.00; estimate $0.75 to $1.00 | **PASS**, unchanged | MEASURED |
| 5 | Regenerating the plan from the staging script reproduces the committed file byte for byte | **PASS**, from a copy of `425334f`, once the copy's folder prefix is rewritten to the main checkout's (five lines carry it). A regeneration inside the main checkout cannot be done until the fix merges | MEASURED |
| 6 | The dry run, only if it creates nothing and spends nothing | **PASS.** Exit status 0; no call reached a stand-in; no watchdog, keep-awake or shutdown-watcher process started; no artifacts folder created. A real launch would still be **refused today**: no ledger row for `slice_handshake` | MEASURED |
| B | First check's finding B: the final copy brought home the whole shared run folder | **Fixed.** The slice's run folder is `/workspace/mvm-out/slice_handshake`, and every reader of the run folder uses it: the trainer's output, the machine's watcher, the laptop watchdog's final copy and its receipt | MEASURED |
| C | First check's finding C: the timing file could be lost, and was timed on a busy card | **Fixed.** The timing now runs before training starts, on an idle card, and the launcher waits for it. The file is rewritten after each architecture and marked complete only at the end. Two small leftover risks, neither a money risk (check C) | MEASURED; the leftovers ARGUED |
| E1 | The registered launcher `launch_a3.sh` is byte-identical to main | **PASS**: same content hash on main, on `425334f` and in the main checkout | MEASURED |
| E2 | The three new settings change nothing when unset | **PASS on everything that runs.** The dry-run printout gains **one blank line**, and nothing else differs. Set to empty strings, the result is the same as unset | MEASURED |
| E3 | The four launcher self-tests pass | **PASS**: all four exit 0, no stand-in called | MEASURED |
| E4 | The plan states its departure from staging document section 3 | **PASS**: plan lines 51 to 54 | MEASURED |

**Overall.** The fix does what its commit message says, and nothing beyond it.
Both of the first check's extra findings are resolved, and the one failed point
(the missing fourth outcome) now passes. No check failed. **Three things for
John before a go** (the last section): the go wording adopted on 2026-09-25
names the plan at `60d1496` and lists four of the plan's seven settings; the
main checkout has to be updated after the merge, because the plan's commands
point into it; and the ledger row is still owed.

## What was opened, and what was not

Opened and read in full: the first check; the fix's commit message and pull
request description; the fix's full diff to the launcher, the timing script
and the staging script; the plan file at `425334f`, and its diff against
`60d1496`; the launcher's launch path, from the push to the machine through to
the writing of the watchdog's settings (lines 330 to 575 at `425334f`); the
main loop of the machine's shutdown watcher `reap_agent.sh` (lines 200 to 258);
sections 3, 4, 6 and 7 of the staging document; page 9 of the Weekend 1 queue
ruling (`docs/rulings/2026-09-26-weekend-1-queue.md`), with its header; and the
go wording on page 9 of that ruling's proposal (lines 1227 to 1250).

Searched, not read in full: the laptop watchdog `watch_run_a3.sh` (every use of
the run folder); the trainer `train_a3.py` (where it writes its finished-marker).

Not opened: the rest of the Weekend 1 ruling and its proposal; the successor
proposal; the shutdown-fix method note.

## How it was run

`$SP` is this session's scratch folder. `$M` is the main checkout,
`/Users/john/Code/minimum-viable-mind`. Two copies were unpacked into `$SP`
with `git archive`: `$SP/fix` from `425334f` and `$SP/main` from main at
`09fedf5`. The launcher is the same file at `09fedf5` and at main's head
`d9f4729`. Both copies fall back to the main checkout's Python environment, and
both name the main checkout as the artifacts folder. So their dry runs differ
only in the folder prefix, which was rewritten to `TREE`, and in the
advisory deletion time, which was rewritten to `<TIME>`.

**Safety net, the same as the first check's.** Stand-ins for `runpodctl` (the
rental service's command-line tool), `ssh` and `scp` went first on the command
path. Each one writes its name and arguments to `$SP/decoy-calls.log` and exits
with status 99:

```
$ cat $SP/decoy/ssh
#!/bin/sh
echo "ssh $*" >> /Users/john/.claude/jobs/6193d352/tmp/decoy-calls.log
exit 99
```

The log was emptied before each batch and read after it. It was empty every
time.

## The checks

### Check 1 — every path resolves. PASS. MEASURED

```
== absolute laptop paths in the plan: in the main checkout today, and in 425334f's tree
  main checkout: MISSING | 425334f: MISSING | experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/bench_arms.json
  main checkout: exists | 425334f: exists | experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
  main checkout: exists | 425334f: exists | experiments/rehearsal-successor-measure/src
== machine-side paths in the plan
/workspace/mvm-out
/workspace/mvm-out/slice_handshake
/workspace/mvm-out/slice_handshake/bench_arms.json
== where the launcher sets them
221:  RUN_DIR="/workspace/mvm-out"
224:[ -n "$RUN_SUBDIR" ] && RUN_DIR="$RUN_DIR/$RUN_SUBDIR"
528:    $SSH "mkdir -p /root/pre-train && tar xzf - -C /root/pre-train --no-same-owner"
```

The one "missing" path is where the timing file lands on the laptop. The run
creates it. The run folder on the machine is created by the launcher's first
push (line 361, `mkdir -p $RUN_DIR`), before the timing step writes into it.

Every log line the plan tells the operator to look for is printed by the code
it names:

```
  "ssh up:"                                                  launch_a3_fetch_first.sh
  "run dir:"                                                 launch_a3_fetch_first.sh
  "before training (waits"                                   launch_a3_fetch_first.sh
  "shutdown watcher RUNNING on the machine"                  launch_a3_fetch_first.sh
  "SHUTDOWN WATCHER DID NOT START"                           launch_a3_fetch_first.sh
  "REAP: pod-side reaping NOT armed"                         launch_a3_fetch_first.sh
  "SHUTDOWN ORDER: the trainer deletes the machine itself"   launch_a3_fetch_first.sh
  "SHUTDOWN ORDER: LAPTOP ONLY"                              launch_a3_fetch_first.sh
  "before-training step finished (exit 0)"                   launch_a3_fetch_first.sh
  "receipt written on the machine"                           watch_run_a3.sh
  "receipt found"                                            reap_agent.sh
  "grace ran out"                                            reap_agent.sh
== the timing file line
119:            print(f"wrote {a.out} ({len(out['arms'])} of {len(A.ARMS)} "
  ARMS = ['T', 'C', 'F']
```

So "(3 of 3 architectures)" is what a full run prints. The timing script
still accepts every flag the plan passes it (`--device`, `--steps`, `--batch`,
`--out`, lines 99 to 102).

**The main checkout is not yet the fixed one.** The plan's commands name
files by their absolute paths in the main checkout:

```
  DIFFERS from 425334f (still main's): experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
  DIFFERS from 425334f (still main's): experiments/rehearsal-successor-measure/src/bench_arms.py
```

That is expected before the merge. The plan's step 0 guards against it. The
plan's own step-0 command was run against **main's** launcher, which does not
know the new settings and ignores them without a word:

```
main-plan: exit=0
24:  run dir: /workspace/mvm-out (network volume — survives pod death)
(no "before training" line)
```

Plan lines 27 to 30 say that if the dry run "prints the shared folder
/workspace/mvm-out instead, stop". So an operator who follows the plan after
merging but before updating the checkout is stopped at step 0. ARGUED: the
stop is only as good as the operator reading it. Updating the checkout right
after the merge removes the need (last section).

### Check 2 — the commands match the staging document; step 0 withdrawn. PASS. MEASURED

The staging document is unchanged by the fix (an empty `git diff --stat
origin/main 425334f` for it). The fix changes the plan in exactly the places
its commit message names; the full diff against `60d1496` was read. In summary:

- **Step 0 is still the dry run alone, and step 1 is still the same command
  without `DRYRUN=1`.** Both gain the same three settings. `--help` still
  appears only in the sentence saying it was withdrawn.
- **Step 2 is no longer typed on the machine.** It is done by the launcher
  inside step 1.
- **Step 3 now reads the shutdown path first** and names the three lines that
  tell the operator which path was armed.
- **A NOT TESTED outcome is added** under the handshake heading. It matches
  section 6's "quiet one" (staging document lines 159 to 163). **The first
  check's finding A is fixed.**
- **Two new sections: the final copy's scope, and what is left behind.**

**Section 3's "while it trains".** The plan now times before training, not
during it, and says so at lines 51 to 54 (confirmation E4). Section 3's other
promise still holds: the file is "written into the run directory on the
network volume so that the laptop's final copy brings it home" (the run
directory is now the slice's own folder).

**One departure the plan does not state.** ARGUED. Section 4 of the staging
document says "This staging does not change the shutdown fix and does not
duplicate it. It exercises it." The derived launcher "landed with the shutdown
fix", and the fix edits it. The edit is small, and off unless set. It does not
touch the shutdown code paths. The two watchers are unchanged (an empty diff
for `watch_run_a3.sh`, `reap_agent.sh` and `launch_gate.sh`). But when the
slice sets them, the new settings do change which folder those watchers work
in, and they put a new step between arming the shutdown path and starting
training. The pull request description says this openly ("a sixth" direct
edit of the derived launcher). The plan file does not. This does not change
a command. It matters only for reading "exercises the shutdown fix" as "the
shutdown fix exactly as it landed". The same section's claim that the derived
launcher is "derived verbatim" by nine named replacements was already out of
date after the five earlier direct edits, as the pull request also says.

### Check 3 — the launcher is the derived one. PASS. MEASURED

Both commands that run a launcher (plan lines 26 and 38) name
`launch_a3_fetch_first.sh`. `launch_a3.sh` appears once, at line 33, in the
sentence saying it is not used. The registered launcher is byte-identical to
main (confirmation E1).

### Check 4 — cap and estimate. PASS. MEASURED

Plan lines 113 and 114: `estimate   about $0.75 to $1.00`, `hard cap   $2.00`.
The staging script still has the cap as a setting (`HARD_CAP`, default `2.00`,
line 66) and the estimate as fixed text (line 276). The fix changed neither.
The cost paragraph gains one sentence about the narrower final copy. That
sentence removes the extra copy time the first check's finding B described.

### Check 5 — regeneration reproduces the plan byte for byte. PASS. MEASURED

The fixed staging script exists only on the fix branch, so it was run from
`$SP/fix`, behind the stand-ins:

```
stage exit=0
  [ ok ] interpreter: /Users/john/Code/minimum-viable-mind/.venv/bin/python
  [ ok ] grammar self-test passes
  [ ok ] arms self-test passes
  [ ok ] transplant self-test passes
  [ ok ] measure self-test passes
  [ ok ] the derived launcher is present (registered launcher untouched)
  [ ok ] the machine's own shutdown watcher is present
  [ ok ] the shutdown watcher parses
  [ ok ] a dedicated reaper key is present and is mode 600
  [ ok ] launchers refuse arguments (RT-198 check passes)
  [note] launch_a3.sh is registered and still unguarded: pass it NO
  [note] arguments until the Gate A amendment clears.
  [ ok ] runpodctl is on the path: /Users/john/.claude/jobs/6193d352/tmp/decoy/runpodctl
--- raw diff (committed vs regenerated): lines 24, 26, 36, 38, 74 differ, each only in
    /Users/john/Code/minimum-viable-mind  vs  /Users/john/.claude/jobs/6193d352/tmp/fix
$ sed "s#$SP/fix#/Users/john/Code/minimum-viable-mind#g" <regenerated> > plan-regen-normalised.txt
cmp after prefix rewrite: identical
a2cc52c1cb111b48159db1e08379e7c6e07d0b139e9906aecfb160e2d589f565  plan-425334f.txt
(no stand-in calls)
```

(The `runpodctl` line names the stand-in; it goes to the screen, not into the
plan.) Five lines now carry the folder prefix, up from three, because the
timing folder and the laptop landing path are now printed too. After the
merge, a regeneration in the main checkout should leave `git status` clean.
The fix's pull request gives that command. This check could not run it,
because the main checkout does not have the fixed script yet.

### Check 6 — the dry run. PASS; it created nothing. MEASURED

Run exactly as plan step 0 prints it, with the fixed launcher from `$SP/fix`:

```
fix-plan: exit=0
local pre-flight: can this Mac fall asleep?
  ok: never-sleep override ON, running on wall power
local pre-flight: is there a ledger row with an estimate for 'slice_handshake'?
  problem: no row in the ledger table names this run's output name 'slice_handshake'
  WOULD REFUSE a real launch (this is a dry run, so it carries on and
  creates nothing):
…
  run dir: /workspace/mvm-out/slice_handshake (network volume — survives pod death)
…
  before training (waits for it, at most 1800s):
    push: /Users/john/Code/minimum-viable-mind/experiments/rehearsal-successor-measure/src  ->  /root/pre-train
    run:  cd /root/pre-train && python bench_arms.py --device cuda --steps 50 --batch 32 --out /workspace/mvm-out/slice_handshake/bench_arms.json
  train: python train_a3.py --scale 10M … --device cuda \
    --out /workspace/mvm-out/slice_handshake/slice_handshake.pt
=== stand-in log:
(no stand-in calls)
=== processes before vs after:
(no change)
artifacts/slice_handshake before: absent
artifacts/slice_handshake after: absent
```

It prints both things step 0 says it must print. The never-sleep override was
on and the Mac was on wall power at the time of this run. That can change
before a go. The ledger row is still owed.

The new input checks refuse bad settings before anything else runs, as the
fix says:

```
fix-badsub: exit=2    refusing to run: RUN_SUBDIR must be a plain folder name, got '../x'
fix-halfpre: exit=2   refusing to run: set both PRE_TRAIN_DIR and PRE_TRAIN_CMD, or neither
```

### Finding B re-checked — only the slice's folder comes home. Fixed. MEASURED

The run folder is set once, at launcher line 224. Every piece that reads it
gets the same value:

- **the trainer's output**: `--out $RUN_DIR/$OUT.pt` (dry run above), and the
  trainer writes its finished-marker beside it
  (`train_a3.py` line 376, `Path(args.out).with_suffix(".DONE")`), so at
  `$RUN_DIR/$OUT.DONE`;
- **the machine's shutdown watcher**: `RUN_DIR` is written into its settings
  file (launcher line 463), and it looks for `$RUN_DIR/$OUT.DONE`,
  `$RUN_DIR/$OUT.FETCHED` and `$RUN_DIR/$OUT.pt` (`reap_agent.sh` lines 103 to
  105);
- **the laptop watchdog**: `RUN_DIR` is written into its settings file
  (launcher line 569). Its final copy is `tar czf - -C $RUN_DIR .`
  (`watch_run_a3.sh` line 160), and it writes its receipt to
  `$RUN_DIR/$OUT.FETCHED` (line 181).

So the final copy takes the slice's folder and nothing else. The plan's new
"What is left behind" section says the folder stays on the shared volume and
that later registered runs will carry it home. That answers the second half
of finding B. Its "roughly 120 MB" is marked as not measured, and was not
checked here.

### Finding C re-checked — the timing finishes first, on an idle card. Fixed. MEASURED, with two leftovers ARGUED

**Order.** The timing step (launcher lines 518 to 541) runs after the
shutdown path is settled and before the training start (line 547). The
launcher waits for it. Nothing on the machine can delete it before the
finished-marker except the 24-hour deadline. The shutdown watcher's loop
(`reap_agent.sh` lines 207 to 258) deletes on exactly four things: the hard
deadline, and, once the finished-marker exists, the laptop's receipt or the
grace wait running out. It has no rule that deletes a machine with no trainer
running. So it cannot cut the timing step short on a fresh folder. In the
fallback where the trainer deletes the machine itself, it can only do so after
training, which starts after the timing.

**The file.** A short local run of the fixed timing script, 2 steps at batch 2
on the laptop's processor, spending nothing:

```
arm T: 54.5 ms/step (median 54.8), 26,065,471 parameters
wrote …/bench-test.json (1 of 3 architectures)
arm C: 59.2 ms/step (median 59.7), 29,329,735 parameters
wrote …/bench-test.json (2 of 3 architectures)
arm F: 54.6 ms/step (median 54.9), 29,049,735 parameters
wrote …/bench-test.json (3 of 3 architectures)
ratios to the freely trained arm: T 0.997, C 1.083, F 1.000
wrote …/bench-test.json
complete= True arms= ['C', 'F', 'T']
(no .tmp file left behind)
```

These figures only show the file handling works. They say nothing about speed
on the rented card. What the launcher pushes for this step is the timing
script's folder, 220 KB of source.

**Leftover 1, a stale marker on a second attempt.** ARGUED from the code
above; not reproduced. The machine's shutdown watcher is started before the
timing step. The old finished-marker and receipt are only cleared when
training starts (launcher line 547, `rm -f $RUN_DIR/$OUT.DONE
$RUN_DIR/$OUT.FETCHED`). If a first attempt of the slice got as far as
finishing, both files stay in `/workspace/mvm-out/slice_handshake` on the
volume. A second attempt under the same name would then be deleted by the
watcher on its first look, before or during the timing. The race existed
before the fix, but it lasted only the few seconds between starting the
watcher and starting training. The timing step stretches it to minutes. The
first attempt is not exposed, because the folder is new. And the failure
deletes the machine rather than leaving it billing, so this is not a money
risk. It would cost a lost result and a confusing log. The simplest remedy,
not drafted: clear the two markers in the first push (line 361), or re-run
under a different `OUT`.

**Leftover 2, the laptop watchdog starts later.** ARGUED. The laptop watchdog
is started after training begins (launcher line 576, under the keep-awake command), so it is not yet
running during the timing step, which is capped at 1800 seconds. The launch
gate's own dry-run text says the keep-awake command "holds idle sleep off only
once the watchdog is running, so the launch itself is not covered". The part
of the launch it does not cover is now minutes long instead of seconds. The
never-sleep override covers it, and the go requires that override. If the
time cap cuts the step off, it stops the laptop's `ssh`, not necessarily the
timing process on the machine, so that process may run on beside training.
The plan's step 2 lines, and the `"complete"` flag, would show that happened.

### Confirmation E1 — the registered launcher is byte-identical to main. PASS. MEASURED

```
$ git diff --stat origin/main 425334f -- experiments/06-mvm-0a-constructed-self-index/src/launch_a3.sh
(empty) diff exit=0
$ git rev-parse origin/main:…/launch_a3.sh 425334f:…/launch_a3.sh
9b24d70ffc9c2d83abaf93aa5375b6fbe50d3fe9
9b24d70ffc9c2d83abaf93aa5375b6fbe50d3fe9
$ cmp main/…/launch_a3.sh fix/…/launch_a3.sh && echo "cmp: identical"
cmp: identical
$ shasum -a 256 (main copy, fix copy, main checkout)
f164451a90c85ca6fc73eaffef964be96cde806c73bb561212dd5dc82f47ad2b  (all three)
```

### Confirmation E2 — the new settings change nothing when unset. PASS on behaviour; one blank line in the printout. MEASURED

Four dry runs, all behind the stand-ins, all with the three settings and the
time cap removed from the environment first (`env -u`). All used the plan's
four original settings (`SCALE=10M MAXTOK=2000000 OUT=slice_handshake
GRACE_S=600`):

```
=== diff main-unset vs fix-unset (the new settings unset)
34a35
>
=== diff fix-unset vs fix-empty (set to empty strings)
IDENTICAL
=== diff fix-unset vs fix-plan (set as the plan sets them)
24c24
<   run dir: /workspace/mvm-out (network volume — survives pod death)
---
>   run dir: /workspace/mvm-out/slice_handshake (network volume — survives pod death)
35c35,37
<
---
>   before training (waits for it, at most 1800s):
>     push: …/experiments/rehearsal-successor-measure/src  ->  /root/pre-train
>     run:  cd /root/pre-train && python bench_arms.py --device cuda --steps 50 --batch 32 --out /workspace/mvm-out/slice_handshake/bench_arms.json
37c39
<     --out /workspace/mvm-out/slice_handshake.pt
---
>     --out /workspace/mvm-out/slice_handshake/slice_handshake.pt
(no stand-in calls; no process change; no artifacts folder)
```

With the settings unset, the only difference from main is **one empty line**
in the dry-run preview. It comes from the empty "before training" block,
between the remote self-test lines and the `train:` line:

```
                     python train_a3.py     --self-test$
$
  train: python train_a3.py --scale 10M …
```

It is text on the screen only. The dry run cannot show the real launch path,
so that was read instead: each of the three places the fix adds code does
nothing unless a setting is non-empty (line 224, `[ -n "$RUN_SUBDIR" ] && …`;
line 198, `if [ -n "$PRE_TRAIN_DIR$PRE_TRAIN_CMD" ]`; line 523,
`if [ -n "$PRE_TRAIN_CMD" ]`). The launcher runs without stop-on-error
(`set -uo pipefail`, line 117), so the `&&` line cannot end the script when
the setting is empty. ARGUED on that reading. So, strictly, "changes nothing"
is true of everything that runs and false by one blank line of preview. The
fix's own words, "a dry run prints the same shared run folder as before", are
exactly right.

### Confirmation E3 — the four launcher self-tests pass. PASS. MEASURED

Run from `$SP/fix/experiments/06-mvm-0a-constructed-self-index/src`, behind the
stand-ins:

```
check_launcher_argument_guard.sh   exit=0
    | all checks pass. nothing was created and nothing was spent.
launch_gate_selftest.sh            exit=0
    | launch gate self-test OK — nothing was rented, no vendor was contacted,
    | and this Mac's real power settings were never read or changed.
sleep_guard_selftest.sh            exit=0
    | sleep guard self-test OK — nothing was rented, no vendor was contacted,
    | and this Mac's real power settings were never read or changed.
reap_handshake_selftest.sh         exit=0
    | checks passed: 26   failed: 0
    | reap handshake self-test OK — no machine was rented and no vendor contacted
(no stand-in calls)
```

In the argument-guard check, the fixed launcher's guard is at line 119. The
first vendor command is at line 287, up from 255 because of the added lines.
The guard still comes first. The one line of that output containing "FAIL"
is the heading of its negative-control section ("the check must FAIL on an
unguarded launcher"), and that control passed.

### Confirmation E4 — the plan states its departure from section 3. PASS. MEASURED

Plan lines 51 to 54:

> (Section 3 of the staging document had the timing run WHILE the toy run
> trained. That is changed here: on a toy run that finishes in minutes, the
> machine could be deleted before the timing file existed, and the figures
> would be taken on a card busy with training.)

## For John, before a go

None of these is a failed point. Each changes what a go should say or what
has to happen first. ARGUED.

1. **The go wording names the old plan and four of its seven settings.** The
   Weekend 1 queue ruling (`docs/rulings/2026-09-26-weekend-1-queue.md`,
   page 9, merged as pull request 39 after the fix was written) names the plan
   "at commit `60d1496`". It adopts the proposal's verbatim go, which lists
   "`SCALE=10M MAXTOK=2000000 OUT=slice_handshake GRACE_S=600`" and "the
   fifty-step timing of the three architectures on the same machine". If pull
   request 42 merges, the plan to name is the merged commit, not `60d1496`.
   The flag list would then miss `RUN_SUBDIR` and the two timing-step
   settings. The go also says "stop and report if anything differs from the
   plan". A go that names the new commit and says "with the settings the plan
   prints", or lists all seven, avoids an operator stopping on the mismatch,
   or leaving the three out.
2. **Update the main checkout after merging.** The plan's commands run the
   launcher and push the timing script by their paths in the main checkout.
   Check 1 showed that a stale launcher ignores the new settings without a
   word. After merging with `gh`:
   ```
   git -C ~/Code/minimum-viable-mind pull
   sh ~/Code/minimum-viable-mind/experiments/rehearsal-successor-measure/src/stage_rented_slice.sh
   git -C ~/Code/minimum-viable-mind status --short     # expect no changed paths
   ```
   The last two lines are the byte-for-byte check this session could not run
   in the main checkout.
3. **Still owed, unchanged:** the ledger row for `slice_handshake`, written
   before anything is created (the dry run would refuse without it), and the
   never-sleep override on at the time of the go.

Two smaller notes, for whoever next touches the launcher or the plan: the
stale-marker leftover under finding C, and the unstated departure from
section 4. Neither blocks a go.

## What this check does and does not license

It checks the plan and the fix at `425334f` against the six points of the
first check, that check's two further findings, and the four confirmations
asked for. It finds none of them failing. Section 4 of the 2026-09-22 ruling
asks for "the amended plan, checked by a session other than the one that
amended it". This is that check for `425334f`. It is not a go, and it does not
say the slice should run. If the fix is changed again before merging, this
check no longer describes it.
