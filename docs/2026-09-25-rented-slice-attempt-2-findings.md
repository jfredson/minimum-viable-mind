# The rented slice, second attempt, 2026-09-25: seconds per step measured; the handshake's laptop half worked and its machine half was never given the chance

*Written 2026-09-25 (Pacific) by the session that ran the second attempt (a
Claude Code session in its own worktree, branch
`worktree-mvm-w1f-rented-slice-attempt-2`). Under the pairing rule of
`docs/outside-review-protocol.md`, a different session checks this document.
That check has not happened yet.*

*Labels. **MEASURED**: a command was run and its output is filed. **ARGUED**:
reasoning a reader can dispute. Every receipt named below is in
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/`,
called "the receipts folder" from here on. The account id and the SSH public
keys are removed from those copies and nothing else is changed. UTC times are
the vendor's and the logs'; the whole run fell on the evening of 2026-09-25
Pacific (18:43 to 18:53).*

**Plain terms used below.** *The slice*: one short rented session on a
graphics card, to answer two questions. *The launcher*:
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`,
the unregistered script that rents the machine and runs things on it; the
registered launcher `launch_a3.sh` was not used and not edited. *The machine's
own shutdown watcher*: `src/reap_agent.sh`, started on the rented machine so it
can delete itself once the laptop confirms it has the files. *The handshake*:
that confirmation — the laptop writes a receipt file on the machine, the
watcher sees it, and the watcher deletes the machine. *The laptop watchdog*:
`src/watch_run_a3.sh`, which copies the files home, checks them, writes the
receipt, and deletes the machine itself if nothing on the machine does. *The
machine deadline*: `src/machine_deadline.sh`, the laptop program that deletes
the machine once the hard cap is spent. *Seconds per step*: how long one
training step takes; the money for the rest of the successor experiment (its
"second release") is to be priced from it. *Arms T, C and F*: the successor
experiment's three architectures — T keeps the ownership answer separable by
construction, C entangles it by construction, F is trained freely.

## 1. What happened, in one paragraph

John's go of 2026-09-25 for a second attempt (quoted word for word in the
ledger row) authorised one run of the plan at commit `a96f873`. The ledger row
was written and committed first (`3658a8f`, pushed before anything was
created). Step 0, the dry run, printed every line the go and the plan require.
Step 1 rented an RTX 5090 at $0.99 an hour at 01:46:33Z, armed the laptop's
machine deadline straight after the machine id, emptied the slice's folder,
started the machine's own shutdown watcher **without hanging** — the place the
first attempt stopped — timed the three architectures, trained the toy run to
its token budget, and handed over to the laptop watchdog. The watchdog copied
the files home, checked the model file by checksum, wrote the receipt on the
machine and **deleted the machine itself in the same second**, at 01:49:43Z.
The machine lived about 3 minutes 10 seconds. The vendor's machine list was
confirmed empty by hand. **Seconds per step: measured for all three arms.
Handshake: the laptop's half passed against the real vendor; the machine's
half was not exercised, because the laptop deletes the moment it writes the
receipt.**

## 2. The deliverables, one by one

| Deliverable | Result | Label |
|---|---|---|
| Seconds per step for the three architectures, `bench_arms.json` with `"complete": true`, fetched home | **Measured.** T 13.08 ms, C 13.52 ms, F 12.53 ms per step (means over 50 timed steps; section 3) | MEASURED (`bench_arms.json`) |
| Which shutdown path the launcher armed | **"shutdown watcher RUNNING on the machine"**, then "SHUTDOWN ORDER: copy, check, receipt, delete" | MEASURED (`step1-launch.txt`) |
| The handshake outcome under the plan's pre-stated lines | **None of the six lines fits.** Not PASS: the machine's "receipt found" was never observed, and the deletion was the laptop's. The honest statement is section 4's | ARGUED, from the measured facts in section 4 |
| The receipt | Written: "receipt written on the machine — it may delete itself now" at 01:49:43Z, after "final checkpoint VERIFIED (md5 b4e56e1c69cc)" | MEASURED (`watchdog.log`) |
| The ledger row's actual-after figure | **$0.0525** by the vendor balance, $75.917054611 before and $75.864512286 after (section 6) | MEASURED |
| The second release's arithmetic, rewritten from the measured seconds per step | **$129.90**, against the provisional $143; both releases **$161.90** against $175 (section 7 and the dated note beside the spending proposal) | MEASURED arithmetic on ARGUED method |

## 3. Seconds per step

**MEASURED**, `bench_arms.json` (fetched home by the watchdog's final copy,
`"complete": true`, `"device": "cuda"`, accelerator "NVIDIA GeForce RTX 5090",
torch 2.8.0+cu128), printed by `second_release_arithmetic.py` into
`second-release-arithmetic.txt`:

| Arm | Mean ms per step | Median | Fastest | Slowest | Parameters | Ratio to arm F |
|---|---|---|---|---|---|---|
| T | 13.08 | 13.08 | 13.05 | 13.13 | 26,065,471 | **1.044** |
| C | 13.52 | 13.51 | 13.47 | 13.90 | 29,329,735 | **1.080** |
| F | 12.53 | 12.52 | 12.50 | 12.58 | 29,049,735 | 1.000 |

All three at the registered shape the timing script names (width 448, 12
layers, 8 heads), batch 32, sequence length 56, fifty timed steps after five
warm-up steps, with the card to itself before training started. Against the
plan's pre-stated lines this is **Throughput: PASS** — three figures, one per
architecture, with the spread, in a file with `"complete": true`, fetched home
to `experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/bench_arms.json`
(a copy is in the receipts folder).

**What the figures replace (MEASURED against the proposal's text).** Every
dollar in the second release carried a premium of **1.55** for a constructed
arm, inferred from Amendment A2's full-versus-twin step times on a different
architecture (`docs/successor-experiment-proposal-2026-09-21.md` section 12.4;
`docs/preauthorised-spending-proposal-2026-09-21.md` section 3.2). The rented
card measures **1.044 for T and 1.080 for C**. The spending proposal's own
"case against" (section 3.2) guessed that T "may cost almost nothing" and C
"might be under 10%"; both guesses hold on this reading.

**Three limits, stated so the figures are not read as more (ARGUED).**

1. **Fifty steps, not the five hundred item R-11 specifies.** The successor
   proposal's item R-11 asks for "five hundred steps per arm", with the window
   starting after the first fifty (section 10). The plan John authorised runs
   `--steps 50` after five warm-up steps. The spread is tight (the slowest step
   is within 3% of the median on every arm), so a longer window is unlikely to
   move the ratios much, but the measurement is the plan's and not the
   proposal's. A reviewer may hold that R-11 is not yet met as written.
2. **The seconds cannot be turned straight into hours for a run.** A timed step
   here holds 1,792 tokens; a registered A3 step held about 10,624 (ledger
   line 86: 55,116 steps over 585,552,384 tokens at 0.645 s/step). At the timed
   pace the whole A3 token budget would take arm F about 1.14 hours, $1.13 —
   but the registered A3 run took about 8.7 times the timed pace per token
   (`second-release-arithmetic.txt`, last block). The timing measures the
   model's own forward and backward pass on a batch already on the card; a real
   run also generates its data, evaluates every 500 steps and saves
   checkpoints. So the absolute seconds price the model, not the run, and
   section 7 uses the ratios on a measured run cost instead.
3. **The ratios are not a property of the architectures alone.** The same
   script on the laptop gave T 0.981 and C 1.049
   (`experiments/rehearsal-successor-measure/out/throughput.json`), so the
   ratio depends on the hardware; and at batch 32 the card is lightly loaded,
   so fixed per-step costs may flatten the differences. If a real run's time is
   mostly the data and evaluation work all three arms share, a real run's
   premium would be smaller still. That direction is argued, not measured.

## 4. The handshake

**What was measured, in order (`step1-launch.txt`, `watchdog.log`,
`reaper.log`):**

| UTC | Where | Line |
|---|---|---|
| 01:47:46 | machine's watcher | "reap-agent: up …", "machine id present; deletion is armed" |
| between 01:47:46 and 01:49:01 (the launcher log carries no clock) | launcher | "shutdown watcher RUNNING on the machine (waits 600s for the laptop's receipt; hard deadline +24h, laptop-independent)", "SHUTDOWN ORDER: copy, check, receipt, delete — in that order." |
| 01:49:01 | machine's watcher | "training finished. Holding this machine open so the laptop can take the last copy and check it. Waiting up to 600s for the receipt." |
| 01:49:25 | watchdog | "finished-marker found — training complete" |
| 01:49:38 | watchdog | "final fetch OK" |
| 01:49:41 | watchdog | "final checkpoint VERIFIED (md5 b4e56e1c69cc)" |
| 01:49:43 | watchdog | "receipt written on the machine — it may delete itself now" |
| 01:49:43 | watchdog | "deleting pod alpua1c0w6jonx" → `"deleted": true` |
| 01:49:55 | watchdog | "pod gone; billing stopped" |
| 01:50:00 | this session, by hand | `runpodctl pod list` → `[]` (`post-pod-list.txt`) |

The model file at home has md5 `b4e56e1c69cc10f4033cece45bab4da8`
(`model-md5.txt`), whose first twelve characters are the ones the watchdog
checked against the machine. **MEASURED.**

**Against the plan's six pre-stated lines:**

- **PASS** needs "receipt written on the machine" in the laptop's log (**yes**),
  then "receipt found" in the machine's log (**not observed**), then a deletion
  within seconds (**yes, but by the laptop**), and a checksum match (**yes**).
  Not a pass.
- **FAIL (bounded-wait path)** needs "grace ran out" in the machine's log. It
  did not; the machine was deleted 42 seconds into its 600-second wait.
- **FAIL (credential path)** needs the machine unable to delete itself after
  the bounded wait. The wait never ended, so this was not tested either way.
  (The launcher's "VERIFIED: the pod can reach the API as itself" shows the
  credential worked for reading, not for deleting.)
- **NOT TESTED** is defined as the watcher never starting. It started.
- **NO VERDICT** is "the slice does not run". It ran.
- **CUT OFF BY THE CAP** needs "DEADLINE REACHED" in `machine-deadline.log`. It
  holds only the two "armed" lines (`machine-deadline.log`).

**So none fits, and this document does not force one.** The honest statement:
**the laptop half of the handshake passed against the real vendor — copy,
checksum, receipt written on the machine, delete, confirmed gone — and the
machine half was not exercised.** That is the same thing the first attempt did
with its throughput result, for the same reason.

**Why the machine half could not be exercised (ARGUED from the code, which was
read, not changed).** The watchdog's finishing path, `on_finished` in
`src/watch_run_a3.sh`, calls `write_receipt` and then `kill_pod` on
consecutive lines (241 and 242): it writes the receipt and immediately deletes
the machine, with no wait for the machine's watcher. The watcher looks for the
receipt once every 15 seconds (`AGENT_POLL_S`, `src/reap_agent.sh` line 97).
It logged "training finished" at 01:49:01, so its polls fell roughly at
:16, :31 and :46; the receipt went at :43 and the delete at :43. Whether the
container was still alive at :46 to poll once more is not known. And **even if
the watcher had found the receipt, its "receipt found" line would have gone to
`reaper.log` on the network volume after the final copy had already taken that
file home** — the home copy ends at 01:49:01 (`reaper.log` in the receipts
folder). The volume can only be read from a rented machine, which this go does
not cover. **So, on the normal passing path, the plan's PASS line is close to
unreachable by construction.** The two halves race, the laptop is almost
always first, and the one line that would show the machine's half is written
where nothing will fetch it.

**Is this a new failure or an old one? (ARGUED; a candidate, not an entry.)**
It has the shape of failure 3 in `docs/known-failure-modes.md`, "a cell that is
empty by construction": an outcome line pre-stated in a plan that the design
it tests cannot produce. Adding it is binding text, so it is drafted in
section 9 for John and not added here.

## 5. Every signal the go named, in order

| Signal | Seen | Where |
|---|---|---|
| "run dir: /workspace/mvm-out/slice_handshake" | yes, in step 0 and step 1 | `step0-dryrun.txt`, `step1-launch.txt` |
| "machine deadline: ON … 7272s" | yes: "machine deadline: ON -- hard cap $2.00 at $0.99 an hour: this laptop deletes the machine 7272s after creation" | `step0-dryrun.txt` |
| "MACHINE DEADLINE ARMED" right after the machine id | yes: "pod: alpua1c0w6jonx", next line "MACHINE DEADLINE ARMED (pid 7745): this laptop deletes alpua1c0w6jonx at 2026-09-26T03:47:44Z, 7272s after creation" | `step1-launch.txt` |
| The folder-clear line | yes: "clearing the run folder before anything on the machine starts: /workspace/mvm-out/slice_handshake"; found before clearing one file, `reaper.log`, 469 bytes, dated 23:49 — the first attempt's watcher log, the same size its last reading gave (`rented-slice-2026-09-25/remote-state-at-stop.txt`); no "LEFTOVER:" line; "files left after clearing: 0" | `step1-launch.txt` |
| Which shutdown path was armed | "shutdown watcher RUNNING on the machine" | `step1-launch.txt` |
| "wrote … bench_arms.json (3 of 3 architectures)" | yes | `step1-launch.txt` |
| "before-training step finished (exit 0)" | yes | `step1-launch.txt` |
| The three handshake signals | first yes, second not observed, third by the laptop (section 4) | `watchdog.log`, `reaper.log` |
| Silence of more than a couple of minutes after "VERIFIED" | **none**: the shutdown path was reported within seconds | `step1-launch.txt`; the session's monitor raised no silence alarm |

**Two lines that looked like trouble and were not (MEASURED against the
code).** (1) The shell printed "Terminated: 15 ( sleep "$cap"; kill "$pid" … )"
at launcher line 637, just after "VERIFIED". That is `ssh_capped` stopping its
own 60-second timer because the `ssh` returned first (`kill "$killer"` in the
helper). It is the fix of 2026-09-25 working on a real connection: **the
watcher start returned at once, where the first attempt hung for 30 minutes.**
The same message at line 701 is the timing step's own timer being stopped the
same way. (2) The launcher's liveness check printed "NOT RUNNING — check
…/train_slice_handshake.log". Training had already finished: the toy run's
189 steps took 52.2 seconds (`train_slice_handshake.log`: "token budget reached
(2,007,936)", "TRAINING COMPLETE"), inside the training start's 60-second
connection cap, and the watchdog found the finished-marker three seconds after
it started. On a toy run this line is expected, and a later reader should not
take it for a crash.

## 6. Money

MEASURED; the receipts are `pre-user.txt`, `post-user.txt`, `post-user-2.txt`,
`post-user-settled.txt`, `billing-this-pod.txt` and the ledger row.

| | |
|---|---|
| Balance before creation, 2026-09-26T01:43:03Z | $75.917054611 |
| Balance after deletion, 01:50:01Z and 01:52:46Z | $75.917054611 — unchanged; the vendor had not yet debited |
| Balance after the vendor debited, 01:54:04Z | **$75.864512286**, a fall of **$0.0525** (`post-user-settled.txt`); the per-machine billing rows had not posted by 01:54:05Z (`billing-this-pod.txt`) |
| Machine life | rented 01:46:33Z (creation record) to deleted 01:49:43Z (the delete's return in `watchdog.log`): 3 min 10 s, **$0.052** at $0.99 an hour |
| Rate from the creation record (`costPerHr`) | $0.99, at the line stated in advance |

**The laptop's machine deadline is still running** (process 7745) and will ask
the vendor to delete the already-deleted machine at 03:47:44Z. Nothing in the
plan stops it and this session did not. What it logs then is the first real
answer to one of the check's four gaps — whether the vendor's tool reports
success on a delete that did nothing (gap (c)) — and is left for a later
session to read from
`experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/machine-deadline.log`.

## 7. The second release, from the measured figures

The dated note beside the spending proposal carries this in full
(`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`).
In brief, **MEASURED arithmetic on an ARGUED method**, from
`second-release-arithmetic.txt`: the measured registered-size run of
2026-09-17 ($10.04, ledger line 88) times each arm's measured ratio gives
**F $10.04, T $10.48, C $10.84** a run. Section 12.4's eight remaining runs
(two F, three T, three C) come to **$84.06** (provisional $96), the permitted
re-run at the dearest arm **$10.84** (provisional $12), and with the two lines
that do not depend on throughput unchanged ($12 and $23) the second release is
**$129.90** (provisional $143). With the first release's $32, **$161.90**
(provisional $175). Against the $400 ceiling that leaves about **$10.0**;
against the $450 ceiling ruled on 2026-09-25, about **$60.0**. The proposal's
wager (section 12.8) — that the per-run cost comes in at or below the $12
planning figure — survives on this reading: the dearest arm is $10.84.

## 8. What this session did and did not do

- **Did:** read the listed documents; took the pre-creation readings; wrote,
  committed and pushed the ledger row before creation; ran step 0 and step 1
  from the main checkout exactly as printed; watched every signal; confirmed
  the machine list empty by hand, twice (01:50:00Z, 01:52:46Z); read the
  balance; filed the receipts; wrote this document and the note beside the
  spending proposal.
- **One choice of its own in how step 1 was started (ARGUED).** The command was
  put, character for character as the plan prints it, into a small script and
  started in a session of its own (`os.setsid`), with its output appended to
  `step1-launch.txt`. The reason is the check's gap (d): a terminate signal to
  the launcher's process group kills the machine deadline, and the tool this
  session runs commands through may signal its own group when it stops a
  background job. In its own session the launcher, and the deadline it
  spawns, were out of that group's reach. The launcher's process number was
  7617; it was never signalled, and it exited 0 on its own at 01:49:26Z.
- **The main checkout** was given the committed ledger (`3658a8f`) in its
  working copy for the launch gate to read (the gate reads the ledger beside
  the launcher, `launch_gate.sh` line 272), as the first attempt did. After the
  run it was put back to `a96f873` exactly, checked with `cmp`. The fetched
  files sit in `experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/`
  in the main checkout, which git ignores (`.gitignore` line 15).
- **A read-only `ssh` to the machine failed** host-key verification at
  01:49:37Z and changed nothing; the machine was then left to the watchdog.
- **Did not:** empty anything outside `/workspace/mvm-out/slice_handshake`;
  relaunch; stop the machine deadline; edit any registered text, ruling or
  protocol text; edit the spending proposal or the successor proposal.
- **Left behind:** the slice's folder on the network volume now holds this
  run's files, including the toy model (77,450,933 bytes at home), the
  finished-marker and the receipt. The plan's "What is left behind" says the
  registered launcher's final copy would carry this folder home on a later
  registered run unless it is removed first.

## 9. For John: decisions owed (ARGUED; nothing here is ruled)

1. **The handshake's machine half is still untested against the real vendor.**
   Two ways to test it. (a) Make the watchdog wait, after writing the receipt,
   for up to twice the watcher's poll interval (30 s) and delete only if the
   machine is still there, and have the watcher append its "receipt found"
   line somewhere the laptop reads after the fact (for example, the vendor's
   deletion record already says who deleted; or the watcher can write a second
   file the watchdog fetches before deleting). (b) Leave the design as it is
   and accept that on the normal path the laptop is the reap, with the watcher
   as the backstop for a laptop that never answers. **Confidence that (a) would
   let PASS be observed: moderate** — the 30-second wait is cheap, but the
   log-placement half needs care. **Standard practice** for a two-party
   shutdown is (a)'s shape: the side that asks waits for the other side to
   acknowledge. **The strongest alternative** is (b), which is what the
   registration can honestly say today, and which costs nothing more to rent.
2. **A candidate for the known-failure list** (binding text, drafted, not
   added): *an outcome line a plan states in advance that the design it tests
   cannot produce on the path it expects.* Its test would be, for each
   pre-stated line, to name the code path that prints each signal it needs and
   show that path can run in the order the line requires. This may be an
   instance of failure 3 rather than a new species; that is a ruling.
3. **Whether fifty steps meets item R-11**, which specifies five hundred
   (section 3, limit 1). The second release is priced here on the fifty-step
   figures; if John holds R-11 to its letter, the release waits on a longer
   timing, which could ride on the first registered-size run rather than a new
   rental.
4. **Settle the actual.** Read the balance and the machine's billing rows again
   after a day, and annotate the row with the settled figure if it moves, as
   the check of the first attempt recommended for that row.
5. **The slice folder on the volume** holds a 77 MB toy model. Whether to
   empty it before the next registered run is John's; this go allowed emptying
   it only as part of the launcher's pre-flight clear.

## 10. What is owed

- A check of this document, the ledger row and the note beside the spending
  proposal, by a different session, under the pairing rule.
- John's rulings on section 9.
- The machine deadline's log after 03:47:44Z (section 6).
