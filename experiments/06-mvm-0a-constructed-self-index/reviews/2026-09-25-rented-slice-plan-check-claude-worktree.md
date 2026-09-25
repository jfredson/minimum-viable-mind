# Check of the regenerated rented-slice plan, at commit `60d1496`

*2026-09-25 (Pacific). A check under the pairing rule of
`docs/outside-review-protocol.md` (whatever one session writes, a different
session checks). Filed here because the plan's launcher, its ledger and its
money belong to this experiment, and because
`docs/rulings/2026-09-22-launcher-argument-guard.md`, section 4, makes this
check the thing a fresh go for the rented slice waits on: "the amended plan,
checked by a session other than the one that amended it".*

*This session did not write, amend or regenerate the plan, the staging script
or the staging document, and has not read the chat of any session that did.
Nothing was launched, rented or spent. No registered text, ruling or protocol
text was edited.*

**The target.** `experiments/rehearsal-successor-measure/out/rented-slice-plan.txt`
as committed in `60d1496` ("Regenerate the plan file on main, with step 0
withdrawn", 2026-09-21 21:34 Pacific). That file has not changed between
`60d1496` and the main line's head at the time of checking, `c89a3ef` (the
command is in check 5). This check covers **that file**, the "plan file" below.
The "staging document" is `docs/successor-rented-slice-staging-2026-09-21.md`
and the "staging script" is
`experiments/rehearsal-successor-measure/src/stage_rented_slice.sh`, which
writes the plan file.

**Labels.** MEASURED: a command was run and its output is printed here.
ARGUED: reasoning a reader can dispute.

## Verdict, point by point

| # | What was asked | Result | Label |
|---|---|---|---|
| 1 | Every path in the plan file resolves on this checkout | **PASS** | MEASURED |
| 2 | Every command matches the staging document, sections 1 to 6, with step 0 withdrawn | **PASS on the commands; FAIL on one outcome.** The commands pass. But section 6 of the staging document says the plan file tells the operator about a fourth outcome, and the plan file never mentions it (finding A) | MEASURED |
| 3 | The launcher named is `launch_a3_fetch_first.sh`, not the registered `launch_a3.sh` | **PASS** | MEASURED |
| 4 | Hard cap $2.00; estimate $0.75 to $1.00 | **PASS** | MEASURED |
| 5 | Regenerating the plan from the staging script reproduces the committed file byte for byte | **PASS**, when run from the main checkout. Run from a worktree, only the path prefix differs, on three lines | MEASURED |
| 6 | The launcher's dry run, only if it creates nothing and spends nothing | **Run, and it created nothing.** Exit status 0; no call reached the rental service's tool or `ssh`; no watchdog or keep-awake process started. It reports that a real launch would be **refused today**: there is no ledger row for `slice_handshake` yet | MEASURED |

**Overall.** The commands in the plan file are right. The file reproduces from
its script. The one thing that runs without money is safe to run. **One
sentence is missing:** the plan file does not tell the operator to look for the
shutdown watcher failing to start. The staging document says it does, and the
plan's step 3 tells the operator to watch "nothing else". Beyond what was
asked, this check found two further problems for John to weigh before a go
(findings B and C). Neither one changes a command.

## What was opened, and what was not

Opened and read in full: the plan file at `60d1496`; the staging document;
the staging script; section 4 of the 2026-09-22 ruling; the launcher
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`
from its argument guard to the end of its dry-run branch (lines 100 to 277);
the argument-guard check `…/src/check_launcher_argument_guard.sh`; the
dry-run branch of `…/src/launch_gate.sh`; the timing script
`experiments/rehearsal-successor-measure/src/bench_arms.py`, lines 1 to 25 and
39 to 130; the final-copy function of `…/src/watch_run_a3.sh`; and the pairing,
isolation, failure-mode-pass and Filing sections of
`docs/outside-review-protocol.md`, with `docs/known-failure-modes.md`.

Also read: the part of `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`
about this slice (lines 1160 to 1290). It is where the brief's description of
the plan comes from. It found no filed check of this plan, and this file is
that check.

Not opened: the shutdown-fix method note beyond one search of it; the
successor proposal beyond four searches; the machine-side watcher
`reap_agent.sh`, apart from a search for one log line. Two untracked files that
appeared in the main checkout while this check ran (see check 6) were not
opened.

## The checks, with commands and outputs

`$SP` below is this session's scratch folder. `$M` is the main checkout,
`/Users/john/Code/minimum-viable-mind`. `$W` is this worktree,
`$M/.claude/worktrees/rented-slice-plan-check`, branched from `c89a3ef`.

**Safety net used for every run below.** Before running anything, stand-ins
for `runpodctl` (the rental service's command-line tool), `ssh` and `scp` were
put first on the command path. Each stand-in writes its name to
`$SP/decoy-calls.log` and exits with status 99, so a script that tried to
reach the rental service or a machine would leave a line in that log and fail.
After every run the log was read. It was empty every time.

### Check 1 — every path resolves. PASS. MEASURED

```
$ grep -o '/Users/[^ ]*' $SP/plan-60d1496.txt | sort -u | while read p; do [ -e "$p" ] && echo "  exists: $p" || echo "  MISSING: $p"; done
  exists: /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
  exists: /Users/john/Code/minimum-viable-mind/experiments/rehearsal-successor-measure
== the same paths relative to this worktree:
  exists: experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
  exists: experiments/rehearsal-successor-measure
== executable?
-rwxr-xr-x
== files named by name only:
  exists: experiments/rehearsal-successor-measure/src/bench_arms.py
  exists: experiments/rehearsal-successor-measure/src/stage_rented_slice.sh
  exists: experiments/06-mvm-0a-constructed-self-index/src/launch_a3.sh
== remote paths (on the rented machine; cannot resolve here):
/root/rehearsal
/root/rehearsal/src
/workspace/mvm-out/bench_arms.json
```

The two absolute paths point into the main checkout, not into any worktree.
That is deliberate: commit `60d1496` says it was generated "from the main
checkout so the absolute paths it prints are ones that will still exist". The
three remote paths exist only on a rented machine and cannot be checked here.
`/workspace/mvm-out` matches the launcher's run directory when a network
volume is attached (launcher lines 187 to 190; the dry run in check 6 prints
`run dir: /workspace/mvm-out`).

The plan's step 2 also depends on things that are not paths. All of them exist:

```
$ grep -n 'add_argument' experiments/rehearsal-successor-measure/src/bench_arms.py
89:    ap.add_argument("--device", default="auto")
90:    ap.add_argument("--steps", type=int, default=20)
91:    ap.add_argument("--batch", type=int, default=32)
92:    ap.add_argument("--out", default="")
$ for s in "ssh up:" "receipt written on the machine" "receipt found" "grace ran out"; do …grep -ln "$s" *.sh *.py; done   # in experiments/06-…/src
"ssh up:"                        launch_a3_fetch_first.sh launch_ctl_pilot.sh launch_a3.sh launch_pilot_a1.sh
"receipt written on the machine" watch_run_a3.sh
"receipt found"                  reap_agent.sh
"grace ran out"                  reap_handshake_selftest.sh reap_agent.sh
```

So the timing script accepts every flag step 2 passes it. The launcher prints
the `ssh up:` handle the plan tells the operator to use. Each of the three
handshake log lines the plan quotes is printed by the code it names.

### Check 2 — the commands match the staging document; step 0 withdrawn. PASS on the commands, FAIL on one outcome. MEASURED

**What sections 1 to 6 contain.** They do not contain the command lines.
Section 3 (lines 74 to 78) says "the exact commands, the settings and the plan
are produced by" the staging script. So the check was of two kinds. First, the
commands were checked against what sections 3 and 4 describe. Second, the
specific values were located:

```
$ S=docs/successor-rented-slice-staging-2026-09-21.md; for t in DRYRUN 'dry run' 'Step 0' 'step 0' 10M 2000000 2,000,000 slice_handshake GRACE 600 fifty 50 launch_a3_fetch_first launch_a3.sh '\$2.00' '\$0.75' bench_arms batch; do printf '%-22s ' "$t"; grep -n -- "$t" $S | cut -d: -f1 | tr '\n' ' '; echo; done
DRYRUN
dry run
Step 0
step 0
10M
2000000
2,000,000
slice_handshake
GRACE
600
fifty                  167
50                     176
launch_a3_fetch_first  86
launch_a3.sh           82
\$2.00                 175
\$0.75                 174
bench_arms
batch
```

Sections 1 to 6 run from line 12 to line 164. None of the run settings
(`SCALE=10M`, `MAXTOK=2000000`, `OUT=slice_handshake`, `GRACE_S=600`) appears
anywhere in the staging document. It never mentions a dry run or a step 0.
"Fifty" appears only in section 7, at line 167. The settings come from the
staging script's defaults, lines 60 to 64
(`SLICE_TOKENS=2000000`, `SLICE_SCALE=10M`, `SLICE_OUT=slice_handshake`,
`SLICE_GRACE_S=600`, `BENCH_STEPS=50`). They agree with the brief and with
the proposal's description (`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`,
lines 1167 to 1170).

**The staging document has not changed since it was written:**

```
$ git log --oneline -- docs/successor-rented-slice-staging-2026-09-21.md
8bc5fbe Stage the one short slice of rented time, for two answers and one rent, and do not run it
```

On 2026-09-22 John's words were that the document "is about to change". It did
not. The withdrawal of step 0 was made in the staging script and the plan
file only. ARGUED: this does not make the plan wrong, but it means "the
amended plan" can only mean the plan file, and a go should name the plan file
by commit. The proposal already recommends that
(`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`, item 3, at
line 1227).

**Against what sections 3 and 4 describe, the commands match:**

- Section 3: "a toy run through the derived launcher". Plan step 1
  (plan lines 26 to 30): yes.
- Section 3: while it trains, the three architectures are timed "on the same
  machine … written into the run directory on the network volume so that the
  laptop's final copy brings it home". Plan step 2 (lines 32 to 40) writes to
  `/workspace/mvm-out/bench_arms.json`: yes.
- Section 4: the derived launcher, not the registered one: yes (check 3).

**Step 0 is the dry run alone, and it is the launch command with only
`DRYRUN=1` added:**

```
$ diff <(sed -n 22,24p $SP/plan-60d1496.txt | sed 's/DRYRUN=1 //') <(sed -n 28,30p $SP/plan-60d1496.txt) && echo "step 0 == step 1 apart from DRYRUN=1"
step 0 == step 1 apart from DRYRUN=1
$ grep -n -- '--help' $SP/plan-60d1496.txt
16:  open with `launch_a3_fetch_first.sh --help`, which was withdrawn by John on
17:  2026-09-22 [RT-198]: the launcher had no --help and no argument handling at
```

`--help` survives only in the sentence saying it was withdrawn. No command
passes the launcher an argument.

**Finding A — FAIL: the fourth outcome is in the staging document and missing
from the plan file.** MEASURED. Section 6 of the staging document (lines 159
to 163) names "the quiet one". In that outcome the machine's own shutdown
watcher never starts, and the launcher falls back to the trainer deleting its
own machine. "Everything looks normal while nothing has been tested". The
section ends: "The launcher says so loudly when it happens, and **the plan
file tells the operator to read that line** before believing the run tested
anything." The plan file does not:

```
$ grep -n -i 'watcher\|unarmed\|never start\|ON_UNARMED\|not armed' $SP/plan-60d1496.txt
88:    watcher is not armed and only the laptop-only path is tested, which is
$ grep -n -i 'not armed\|UNARMED\|never start\|did not start' experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh | grep -v '^[0-9]*: *#'
172:ON_UNARMED="${ON_UNARMED:-self-terminate}"
271:  otherwise the fallback is ON_UNARMED=$ON_UNARMED
441:    echo "  SHUTDOWN WATCHER DID NOT START — check $RUN_DIR/reaper.log on the"
442:    echo "  machine. Falling back per ON_UNARMED below."
448:  echo "REAP: pod-side reaping NOT armed — $REAP_REFUSAL"
464:  case "$ON_UNARMED" in
467:      echo "SHUTDOWN ORDER: LAPTOP ONLY (ON_UNARMED=laptop-only)."
473:      echo "  (ON_UNARMED=self-terminate, the money-safe fallback)."
```

Plan line 88 covers a different case: no dedicated deletion key, decided
before launch. It does not cover a watcher that has a key but fails to start
on the machine. The lines the launcher prints in that case (441, 442, 448 and
473) are never named in the plan file. Plan step 3 (line 42) makes it worse:
"watch for the three signals, in this order, **and nothing else**". An
operator following the plan literally is told to ignore the one line that
would show the run tested nothing. The same gap is in the staging script, at
lines 198 and 213 to 227, so regenerating the file will not fix it; the
script text has to change first.

The lapsed go of 2026-09-21 asked for this very report: "which shutdown path
the launcher actually armed, said plainly, including the case where the
machine's own watcher never started and the run only looked normal". It is
quoted in the ledger row of that date,
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, line 74.

**Suggested repair, a draft only; nothing was edited.** In the staging
script's plan text, change step 3 to "watch for the three handshake signals,
in this order — and first, read which shutdown path the launcher armed: a
line reading `SHUTDOWN WATCHER DID NOT START` or `REAP: pod-side reaping NOT
armed` means the handshake was not tested, whatever follows". Add a fourth
handshake outcome under the plan's handshake heading to match section 6.
Then regenerate the plan from the main checkout, and have a different session
check it. Because the plan would change again, this check would no longer
describe it. ARGUED.

### Check 3 — the launcher is the derived one. PASS. MEASURED

```
$ grep -n 'launch_a3' $SP/plan-60d1496.txt
16:  open with `launch_a3_fetch_first.sh --help`, which was withdrawn by John on
24:      /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
27:  launcher launch_a3.sh is not used and not edited):
30:      /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
```

Both commands that run a launcher (lines 24 and 30) name
`launch_a3_fetch_first.sh`. `launch_a3.sh` appears once, at line 27, in the
sentence saying it is not used. The staging script's pre-flight also re-runs
the argument-guard check, which confirms the registered launcher is read and
never run (check 7).

### Check 4 — cap and estimate. PASS. MEASURED

Plan file lines 78 and 79: `estimate   about $0.75 to $1.00` and
`hard cap   $2.00`. The staging document, section 7, lines 174 and 175,
says the same. In the staging script, the cap is a setting (`HARD_CAP`,
default `2.00`, line 66). The estimate is fixed text (line 234), so a changed
rate would not move it. ARGUED, minor: "well under an hour … at $0.99 an
hour" (plan line 77) puts the rented time below $0.99, so the top of the
estimate, $1.00, sits a cent above that reasoning. The hard cap covers the
difference. Finding B names a cost the estimate does not count.

Each figure the plan cites was traced to its record (failure 4 below).

### Check 5 — regenerating the plan reproduces it byte for byte. PASS. MEASURED

The staging script writes its own absolute location into the plan (lines 53
to 57 and 178 to 191). So a run from a worktree cannot reproduce a file
generated in the main checkout. It was run twice.

**From this worktree**, with the prefix difference shown and then removed:

```
$ PATH=$SP/decoy:$PATH sh experiments/rehearsal-successor-measure/src/stage_rented_slice.sh > $SP/stage-stdout.txt 2>&1; echo "exit=$?"
exit=0
$ diff $SP/plan-60d1496.txt $SP/plan-regen-worktree.txt
24c24
<       /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
---
>       /Users/john/Code/minimum-viable-mind/.claude/worktrees/rented-slice-plan-check/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
30c30
<       /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
---
>       /Users/john/Code/minimum-viable-mind/.claude/worktrees/rented-slice-plan-check/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
35c35
<     tar czf - -C /Users/john/Code/minimum-viable-mind/experiments/rehearsal-successor-measure src | \
---
>     tar czf - -C /Users/john/Code/minimum-viable-mind/.claude/worktrees/rented-slice-plan-check/experiments/rehearsal-successor-measure src | \
diff exit=1
$ sed "s#$W#$M#g" $SP/plan-regen-worktree.txt > $SP/plan-regen-normalised.txt
$ cmp $SP/plan-60d1496.txt $SP/plan-regen-normalised.txt && echo "cmp: identical"
cmp: identical
```

The worktree's copy was then restored with `git checkout`, so this branch
does not change the plan file.

**From the main checkout, with no substitution.** The main checkout's working
tree was clean beforehand, and its copy of the plan file equals `60d1496`'s.
So the only file the script writes would come out unchanged if and only if it
reproduces:

```
$ echo "main before: $(git -C $M status --short | wc -l | tr -d ' ') changed paths; HEAD $(git -C $M rev-parse --short HEAD)"
main before: 0 changed paths; HEAD c89a3ef
$ git -C $M diff --quiet 60d1496 HEAD -- experiments/rehearsal-successor-measure/out/rented-slice-plan.txt && echo "plan file unchanged between 60d1496 and main HEAD"
plan file unchanged between 60d1496 and main HEAD
$ PATH=$SP/decoy:$PATH sh $M/experiments/rehearsal-successor-measure/src/stage_rented_slice.sh > $SP/stage-stdout-main.txt 2>&1; echo "stage exit=$?"
stage exit=0
$ diff $SP/plan-60d1496.txt $M/experiments/rehearsal-successor-measure/out/rented-slice-plan.txt && echo "diff: no differences (exit 0)"
diff: no differences (exit 0)
$ cmp … && echo "cmp: identical"
cmp: identical
$ shasum -a 256 $M/experiments/rehearsal-successor-measure/out/rented-slice-plan.txt
a62416bf0d96b467578e414c8c3e4801dee4fb5406c9003997c62f18a3dfc039  /Users/john/Code/minimum-viable-mind/experiments/rehearsal-successor-measure/out/rented-slice-plan.txt
main after: 0 changed paths
(no decoy calls)
```

The pre-flight checks the staging script printed on the worktree run, quoted
from `$SP/stage-stdout.txt`:

```
local preconditions
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
  [ ok ] runpodctl is on the path: …/scratchpad/decoy/runpodctl
```

(The last line names the stand-in, not the real tool. That line goes to the
screen, not into the plan file.)

### Check 6 — the dry run. Run; it created nothing. MEASURED

**Why it was judged safe before it was run.** The judgement came from reading
the launcher, not from its header's promise:

- the argument guard (launcher lines 128 to 134) exits before anything else,
  and the plan passes no argument;
- everything between the guard and the dry-run exit reads settings, reads
  power settings and the ledger (the launch gate), runs local self-tests and
  prints text;
- the dry-run branch (lines 252 to 276) ends in `exit 0` before the first
  executed `runpodctl` (line 278). The `runpodctl` at line 255 is text inside
  the printed message;
- in `launch_gate.sh`, `caffeinate` (the keep-awake command) is only looked
  up, never started, and nothing is written.

It was then run exactly as plan lines 22 to 24 print it, behind the
stand-ins:

```
$ pgrep -fl 'watch_run|caffeinate' > $SP/procs-before.txt
$ PATH=$SP/decoy:$PATH DRYRUN=1 SCALE=10M MAXTOK=2000000 OUT=slice_handshake \
    GRACE_S=600 \
    /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh > $SP/dryrun-out.txt 2>&1; echo "exit=$?"
exit=0
local pre-flight: can this Mac fall asleep?
  ok: never-sleep override ON, running on wall power
  (idle sleep timers 15 min plugged in / 15 min on battery;
   not relied on — the override covers the lid; the keep-awake command
   (caffeinate) holds idle sleep off only once the watchdog is running,
   so the launch itself is not covered.)
local pre-flight: are the fetch and the delete scheduled inside the run window?
  ok: watchdog watch_run_a3.sh present and parses; runs under caffeinate
  ok: laptop fetch-and-delete by +24h, machine's own deadline +24h
local pre-flight: is there a ledger row with an estimate for 'slice_handshake'?
  problem: no row in the ledger table names this run's output name 'slice_handshake'
  WOULD REFUSE a real launch (this is a dry run, so it carries on and
  creates nothing):
    - no row in the ledger table names this run's output name 'slice_handshake'
      fix: write it before the machine exists: a row in the '## Ledger' table of /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/compute-ledger.md, dated today (Pacific), naming 'slice_handshake', with a dollar figure in the $ est column and the actual left as —
local pre-flight: module self-tests
  interpreter: /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/../../.venv/bin/python
  ok: curriculum_a3
  ok: encoding_a3
  ok: train_a3
  ok: frozen batteries present
creating SECURE pod (NVIDIA GeForce RTX 5090) for 10M/2000000 tok (out: slice_handshake)
  register-less by construction [A3 §2.4]; act-weight 1.0
  run dir: /workspace/mvm-out (network volume — survives pod death)
  advisory terminate-after: 2026-09-26T22:10:07Z; watchdog kill deadline: +24h
  artifacts -> /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake
DRYRUN — nothing created, nothing spawned. Would run:
  runpodctl pod create --name "mvm-slice_handshake" \
    --template-id runpod-torch-v280 --gpu-id "NVIDIA GeForce RTX 5090" \
    --cloud-type "SECURE"  --network-volume-id x9f8pkn58t --terminate-after "2026-09-26T22:10:07Z"
  push: src + batteries-a3  ->  /root/mvm
  remote pre-flight: python curriculum_a3.py --self-test
                     python encoding_a3.py  --self-test
                     python train_a3.py     --self-test
  train: python train_a3.py --scale 10M --seed 0 --twin --batch 128 --steps 200000 --max-tokens 2000000 --act-weight 1.0 --eval-every 500 --eval-n 100 --device cuda \
    --out /workspace/mvm-out/slice_handshake.pt
  aliveness: pgrep -f '[t]rain_a3.py'
  watchdog env dest: /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake
  shutdown watcher: sh reap_agent.sh /root/mvm/reap.env
                    (holds the machine open for the laptop's receipt, up to
                     600s, then deletes if the files are on the volume;
                     hard deadline +24h)
  trainer gets --no-self-terminate ONLY if that watcher is confirmed running;
  otherwise the fallback is ON_UNARMED=self-terminate
  NOTE: the register is never trained in an A3 run; this script has no
        flag that could enable it.
--- decoy log:
(no decoy calls)
--- watchdog/keep-awake processes, before vs after:
(no change)
--- … artifacts/slice_handshake exists? no
```

The time in `advisory terminate-after` is UTC (the letter Z). It is the moment
of the dry run plus 24 hours, not a planned date.

**What the dry run tells John before a go.** MEASURED:

- The never-sleep override was **ON** and the Mac was on wall power at the
  time of this run. The weekend-queue proposal
  (`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`, around line 1218)
  says the check of 2026-09-24 read it as off. That item has since changed.
  It can change back before the go.
- A real launch **would be refused today**, because there is no ledger row
  naming `slice_handshake`. That is the ledger's rule 2 working as intended
  (`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, line
  16). The row is owed at the go, and the plan's closing section already
  names it.
- The train command asks for `--steps 200000` but `--max-tokens 2000000`
  stops it first. The staging script's comment at line 60 puts that at "about
  200 steps at batch 128". ARGUED: that figure is not checked here.

**A side note on the main checkout.** After the dry run,
`git -C $M status --short` showed two untracked files that were not there
before the staging run: `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`
(modified 15:10:10 Pacific) and `docs/rulings/2026-09-26-weekend-1-queue.md`
(15:09:38). They were not written by anything this check ran:

```
$ grep -c 'rulings' launch_a3_fetch_first.sh launch_gate.sh check_launcher_argument_guard.sh ../../rehearsal-successor-measure/src/stage_rented_slice.sh
../../rehearsal-successor-measure/src/stage_rented_slice.sh:0
check_launcher_argument_guard.sh:0
launch_a3_fetch_first.sh:0
launch_gate.sh:0
```

They appear to belong to other sessions working in the main checkout at the
same time. They were left alone and not opened. If
`docs/rulings/2026-09-26-weekend-1-queue.md` rules on this slice, this check
has not read it.

### Check 7 — the argument-guard test, run directly. PASS. MEASURED

```
$ PATH=$SP/decoy:$PATH experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh; echo "exit=$?"
RT-198 — launchers must refuse arguments rather than launch

unregistered launchers: an argument is refused
  [ ok ] launch_a3_fetch_first.sh refuses an argument (exit 2)
  [ ok ] launch_a3_fetch_first.sh says why it refused
  [ ok ] launch_a3_fetch_first.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_a3_fetch_first.sh guard (line 119) precedes any vendor command (line 255)
  [ ok ] launch_ctl_pilot.sh refuses an argument (exit 2)
  [ ok ] launch_ctl_pilot.sh says why it refused
  [ ok ] launch_ctl_pilot.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_ctl_pilot.sh guard (line 93) precedes any vendor command (line 219)
  [ ok ] launch_pilot_a1.sh refuses an argument (exit 2)
  [ ok ] launch_pilot_a1.sh says why it refused
  [ ok ] launch_pilot_a1.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_pilot_a1.sh guard (line 48) precedes any vendor command (line 117)

unregistered launchers: the guard did not break the real path
  [ ok ] launch_a3_fetch_first.sh dry run still exits 0
  [ ok ] launch_a3_fetch_first.sh dry run still creates nothing
  [ ok ] launch_ctl_pilot.sh dry run still exits 0
  [ ok ] launch_ctl_pilot.sh dry run still creates nothing
  [ ok ] launch_pilot_a1.sh dry run still exits 0
  [ ok ] launch_pilot_a1.sh dry run still creates nothing

registered launcher: read, never run
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A
  [… the standing-prohibition block, unchanged …]

negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
exit=0
(no decoy calls)
```

The guard-check test uses the launchers' own `runpodctl` line as the
"first vendor command" (line 255). That is the printed text in the dry-run
branch, not the first line that runs (278). The comparison still holds,
because the guard comes before both.

## Two further findings, beyond the six points asked

**Finding B — the slice's final copy brings home the whole shared run
directory, not just the slice's files.** MEASURED on the code and on past
copies. The size for this run is ARGUED. The laptop's final copy is
`$SSH "tar czf - -C $RUN_DIR ." | tar xzf - -C "$DEST"`
(`…/src/watch_run_a3.sh`, `fetch_final`, line 160). `$RUN_DIR` is
`/workspace/mvm-out`, the directory on the network volume that every run
shares. Past final copies show what this does. The two most recent A3 run
folders each hold every run's model files:

```
$ for d in a3_30m_seed1 a3_30m_seed2; do …ls -S $M/experiments/06-mvm-0a-constructed-self-index/artifacts/$d | head -12 …; done
== a3_30m_seed1: 31 entries
    449M  pilot_a1_30m_seed1.pt
    449M  pilot_a1_30m_seed2.pt
    335M  pilot_a1_30m_seed0_twin.pt
    335M  pilot_a1_30m_seed1_twin.pt
    335M  a3_30m_seed0.pt
    335M  a3_30m_seed1.pt
    335M  a3_30m_seed2.pt
    …
== a3_30m_seed2: 31 entries
    [the same seven model files at the same sizes]
$ du -sh …/artifacts/a3_30m_seed1 …/artifacts/a3_30m_seed2
2.5G	…/artifacts/a3_30m_seed1
2.5G	…/artifacts/a3_30m_seed2
```

(These folders are ignored by git, `.gitignore` line 15. The record for these
figures is this file's command output.)

ARGUED consequences:

- **Cost and timing.** The slice's toy run is small. But unless the volume has
  been emptied, its final copy moves at least the same 2.5 GB over the
  network while the machine is still billing. The handshake's deletion waits
  for that copy. The plan's "well under an hour" and "a deletion within
  seconds" of the receipt do not account for this. At $0.99 an hour, a copy of
  a few minutes adds a few cents, well inside the $2.00 cap. The bigger risk
  is how the result gets read: a slow copy stretches the time between
  starting the machine and deleting it, so the handshake result could look
  like a delay in the handshake itself.
- **What lands on the volume stays there.** `bench_arms.json` and
  `slice_handshake.pt` are written to the shared directory. Every later
  registered run's final copy will carry them home too.

This does not change any command. It is a question for John, or for the
author of the shutdown fix: should the slice set a separate run directory, or
should the copy be narrowed first? Narrowing it touches the shutdown fix,
which is another session's work, so it is not proposed here.

**Finding C — the timing result can be lost to the handshake it rides on, and
it is timed while the card is busy with training.** ARGUED on code that was
read.

- `bench_arms.py` writes its output file only after all three architectures
  have been timed (lines 108 to 111 of that file). The toy run "finishes in a
  few minutes" (plan line 74). If it finishes first, the laptop's copy, the
  receipt and the machine's deletion can all happen before `bench_arms.json`
  exists. Section 3 of the staging document reads a missing file as "the
  fetch fails". Here it could equally mean the timing had not finished, so a
  missing file would not tell the two apart.
- The plan starts timing "while that run is training", on the same graphics
  card. The three seconds-per-step figures would then be taken while the card
  is shared with another training process. That can make them slower than a
  registered run on its own card. The ratios between the three architectures
  are less exposed, because all three share the card with the same load.

ARGUED remedy, not drafted: time the three architectures before the toy run
starts, on the same machine. Or say in the plan that the operator waits for
`wrote /workspace/mvm-out/bench_arms.json` before the toy run reaches its
finished-marker.

**Not checked.** Whether batch 32 in step 2 is "the registered shape" for
the successor experiment. The laptop measurement used batch 32
(`docs/2026-09-21-successor-measure-rehearsal.md`, line 789), and the timing
script records the batch in its output. But this check did not find the
successor proposal stating a registered batch size. It is left open.

## The failure-mode pass, run against the plan

The plan file is not Gate A text, so the protocol does not formally require
this pass. It was run anyway, because failure 5 on the list happened on an
earlier version of this very plan. Each disposition shows its evidence.

1. **A comparison whose denominator was zero.** The plan's only division is
   the ratio of each architecture's seconds per step to the free arm's
   (`bench_arms.py`, line 104, `ratio_to_arm_F`). The denominator is a
   measured time. On the laptop it was 0.2548 seconds per step
   (`docs/2026-09-21-successor-measure-rehearsal.md`, the table at lines 791
   to 795). Nothing in the plan divides by a count that could be zero.
   MEASURED on the laptop record; the rented figure is ARGUED to be positive
   by the same code.
2. **A probe target that cannot be recovered in principle.** The plan reads no
   probe and draws no scientific reading: `grep -c 'probe'` on the plan file
   returns `0`. Section 8 of the staging document says nothing about the
   design's science may be read off the run. MEASURED.
3. **A cell that is empty by construction.** The plan's pre-stated outcomes
   are the cells here. Throughput has pass, fail and no-verdict. The handshake
   has pass, two fails and no-verdict. The staging document's fourth
   handshake outcome, the watcher that never starts, is **absent from the
   plan file**. So an outcome that can happen has no line to be recorded
   against. That is **finding A**. MEASURED.
4. **A claim of measurement with no record.** Every figure the plan cites was
   found in its record:
   - the $0.29 test and its $0.50 cap: compute ledger, the 2026-09-16 row,
     line 68;
   - the $0.99 rate: the 2026-09-17 row, line 69, "20.28 pod-hours at $0.99 =
     $20.08";
   - the anomalous rate of "the 2026-08-08 row": the ledger has no row dated
     2026-08-08. The anomaly is in the row dated 2026-08-09 (line 61, the
     A1 10M pilot) and in the reconciliation note headed "2026-08-08
     reconciliation" (line 371). The figure of 8.47 hours billed against about
     2.42 appears at lines 61, 74 and 374. The record exists, but the plan's
     name for it ("the 2026-08-08 row", plan line 54) points at a row that
     does not exist under that date, so a reader searching the table by date
     finds nothing. This is minor, and it is inherited from staging document
     section 6, line 138;
   - the $10 rehearsal line: `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`,
     line 60, item 10;
   - commitment C2(b): `spec/corrigibility-commitments.md`, line 58;
   - ledger rule 2: `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, line 16;
   - stop condition S9: `docs/successor-experiment-proposal-2026-09-21.md`,
     line 845;
   - "pull request 15": commit `dd1b974`, "Merge pull request #15 from
     jfredson/worktree-reap-race-fix".

   MEASURED (the commands are the `grep` and `git log` searches run in this
   session; the line numbers above are their output). One claim is not in the
   plan file but sits beside it: section 7 of the staging document says
   nothing has been spent from the rehearsal line. That stopped being true on
   2026-09-21, when about $0.02 was spent (ledger line 74). The proposal
   already records this.
5. **A command that creates something while documented as creating nothing.**
   The plan's step 0 is documented as creating nothing. It was run behind
   stand-ins that would have recorded any call to the rental service, `ssh`
   or `scp`. None was called, no watchdog or keep-awake process started, and
   no artifacts folder was created (check 6). The guard test passes, and its
   negative control still rejects an unguarded launcher (check 7). MEASURED.

**A note for the list's keeper, not an edit.** `docs/known-failure-modes.md`,
under failure 5, prints the guard test's expected output with the guard at
line 104 and the vendor command at line 227 for `launch_a3_fetch_first.sh`.
It says a later reader should expect the output to differ "in exactly that
respect and in no other", meaning only in the standing-prohibition block.
Today the lines are 119 and 255 for that launcher, and they have moved for
the other two launchers as well (check 7). That is because the launch gate was
added later. The test still passes. But the list's sentence is no longer
exactly true, and a session diffing the printed output would see unexpected
differences. Whether to reword that sentence is for whoever next edits the
list, under the pairing rule.

## What this check does and does not license

It checks the plan file at `60d1496` against the six points asked, and it
finds one of them short. It is not a go, and it does not say the slice should
run. Two things follow for John, ARGUED:

- If the plan is regenerated to fix finding A, that regeneration needs its
  own check by a session that did not make it, as section 4 of the
  2026-09-22 ruling requires. A go should then name the new commit.
- If John prefers to speak a go against `60d1496` as it stands, the missing
  instruction can be covered by saying it in the go itself. The lapsed go of
  2026-09-21 did exactly that. That is John's call.
