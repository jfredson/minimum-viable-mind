# The rented slice of 2026-09-25: run, stopped, neither measurement taken

*Written 2026-09-25 (Pacific) by the session that ran the slice (a Claude Code
session in its own worktree, branch `worktree-mvm-w1f-rented-slice`). Under the
pairing rule of `docs/outside-review-protocol.md`, a different session checks this
document. That check has not happened yet.*

*Labels. **MEASURED**: a command was run and its output is filed. **ARGUED**:
reasoning a reader can dispute. Every receipt named below is in
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25/`, called
"the receipts folder" from here on. The account id and SSH public keys are
removed from those copies and nothing else is changed.*

**Plain terms used below.** *The slice*: one short rented session on a graphics
card, meant to answer two questions. *The launcher*:
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`, the
unregistered script that rents the machine and runs things on it. *The machine's
own shutdown watcher*: `src/reap_agent.sh`, a small program started on the rented
machine so that it can delete itself once the laptop confirms it has the files.
*The handshake*: that confirmation. The laptop writes a receipt file, the watcher
sees it, and the watcher deletes the machine. *The laptop watchdog*:
`src/watch_run_a3.sh`, which copies the files home and writes that receipt.
*Seconds per step*: how long one training step takes. The money for the rest of
the successor experiment (its "second release") is to be priced from it.

## 1. What happened, in one paragraph

John's go of 2026-09-25 (quoted verbatim in the ledger row) authorised one run
of the plan at commit `4d98cfc`. The ledger row was written and committed first
(`8af960a`). The dry run (step 0) printed what the plan requires. Step 1 rented
an RTX 5090 at $0.99 an hour, pushed the code, passed the self-tests on the
machine, installed the dedicated reaper key and verified it. It then **hung** on
the command that starts the machine's own shutdown watcher. The watcher did
start, but the command never returned, so the launcher never reached the timing
step, the training, or the laptop watchdog. After about 30 minutes of silence
this session treated that as a difference from the plan and stopped. It ended
the launcher, deleted the machine, and confirmed zero machines. **Cost: $0.4974 by
the vendor balance. Neither deliverable was obtained.**

## 2. The deliverables, one by one

| Deliverable | Result | Label |
|---|---|---|
| Seconds per step for the three architectures (`bench_arms.json` with `"complete": true`, fetched home) | **Not measured.** The timing step never started. No `bench_arms.json` exists, on the volume or at home | MEASURED (the remote listing at the stop shows only `reaper.log` in the slice's folder: `remote-state-at-stop.txt`) |
| Which shutdown path the launcher armed | **The launcher never said.** It printed none of the three lines step 3 of the plan says to read first. On the machine, the watcher **was** running and logged "deletion is armed" at 23:49:28Z | MEASURED (`step1-launch.txt` ends at "VERIFIED"; `remote-state-at-stop.txt`) |
| The handshake outcome under the plan's pre-stated lines | **NO VERDICT** (section 3) | ARGUED, from the measured facts above |
| The ledger row's actual-after figure | **$0.4974**, from the vendor balance before and after (section 5) | MEASURED |
| The second release's arithmetic, rewritten from the measured seconds per step | **Cannot be done: there is no measured figure.** A dated note beside the spending proposal says so and gives the consequence (`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25.md`) | ARGUED |

## 3. The outcome under the plan's own lines, written before it ran

The plan (`experiments/rehearsal-successor-measure/out/rented-slice-plan.txt`)
states its outcome lines in advance. Here is how each applies.

**Throughput.** PASS needs three figures in a complete file, and there are none.
FAIL means an architecture would not run at the registered shape, and none was
tried. NO VERDICT is written for "the machine is unavailable, or it bills at the
anomalous rate". Neither of those happened either: the machine was available and
billed normally (section 5). **None of the three lines fits.** The honest
statement is **not measured, because the slice was stopped before the timing
step.** That is recorded here in place of forcing a label the plan did not write
for this case.

**The handshake.** PASS needs "receipt written on the machine", then "receipt
found", then a deletion. None occurred. Both FAIL lines need a finished run, and
there was none. NOT TESTED is defined as the machine's own watcher **never
starting**. **It did start**, so reading this as NOT TESTED would misreport the
watcher. NO VERDICT is written for "the slice does not run". **This is the one
that fits: the slice did not run past arming.** So the result is **NO VERDICT**.
Nothing about the handshake was exercised against the real vendor. The one new
fact is that the watcher starts and reports "deletion is armed" on a real
machine with the dedicated key (MEASURED, `remote-state-at-stop.txt`).

## 4. Why the launcher hung

**MEASURED.** The stuck process was the `ssh` at launcher line 467:

```
ssh … -o ConnectTimeout=20 -o ServerAliveInterval=30 -o ServerAliveCountMax=4 -o BatchMode=yes
    cd /root/mvm/src && nohup sh reap_agent.sh /root/mvm/reap.env >> /workspace/mvm-out/slice_handshake/reaper.log 2>&1 < /dev/null &
```

(`hung-ssh.txt`: running for 29 min 36 s at the time of reading.) On the machine
there were two processes (`remote-state-at-stop.txt`): process 283, a `bash -c`
still holding the whole `cd … && nohup … &` line, and process 284, the watcher.

**The mechanism, reproduced on the laptop with nothing rented (MEASURED,
`hang-reproduction.txt`).** With `| cat` standing in for `ssh`:

```
form as launched (cd && nohup ... &): returned after 8s
control (cd ; nohup ... &): returned after 0s
```

In `cd … && nohup … &`, the `&` sends the whole `cd && nohup` chain to the
background as a subshell. The redirections apply to `nohup` only, not to that
subshell, which keeps the connection's output open until its child exits.
`ssh` waits for that output to close. The watcher runs until its +24h deadline,
so the `ssh` would have waited up to a day. (The mechanism is ARGUED from shell
behaviour; the eight-second and zero-second timings are MEASURED.)

**This is a known hang in this same file.** The training start at line 547 has
the same `cd … && … nohup … &` form, and a comment at line 543, dated
2026-08-17, says: "this ssh can HANG after the remote nohup succeeds". That call
is capped at 60 seconds (line 552). The watcher start at line 467 came in with
commit `40d165d` on 2026-09-21 and has no cap. MEASURED (`grep` and `git log -S`
on the launcher).

**Why no check caught it (ARGUED).** Every test of this launcher replaces `ssh`
with a stand-in: `reap_handshake_selftest.sh` line 131 sets
`SSH="$BIN/fakessh"`, and both plan checks ran behind stand-ins that exit
immediately. A stand-in returns at once whatever the remote command does, so
this hang cannot appear in any of them. The only earlier live use of this
launcher, on 2026-09-21, died before any remote step (ledger, 2026-09-21 row).
**So 2026-09-25 was the first time line 467 met a real `ssh`.**

## 5. Money

All MEASURED; the receipts are `pre-user.txt`, `stop.txt` and the ledger row.

| | |
|---|---|
| Balance before creation, 2026-09-25T23:45:19Z | $76.4526535694 |
| Balance after deletion, 2026-09-26T00:19:56Z and 00:22:10Z | $75.9553006582 |
| **Fall** | **$0.4974** |
| Machine life: rented 23:48:33Z (creation record), deleted 00:19:46Z | 31 min 13 s, $0.515 at $0.99 an hour |
| Rate read from the creation record (`costPerHr`) | $0.99, at the line this session stated in advance |

The fall is below the lifetime arithmetic, so the anomalous-rate stop (S9) did
not fire. The vendor's per-machine billing rows had not posted by 00:22Z
(`billing-this-pod.txt` is empty), so the figure may still move by that lag.

**What unattended would have cost (ARGUED).** Nothing on the laptop would have
deleted the machine: the watchdog is spawned after training starts, and the
launcher never got there. The watcher on the machine deletes only after a
finished-marker, which needs training, or at its +24h hard deadline. So the
machine would have billed for up to 24 hours, **about $24 against a hard cap of
$2.00**. No part of the tooling enforces that cap. It held because the session
was watching the log. That is the lesson of failure 5 in
`docs/known-failure-modes.md`, in John's words there: "a mitigation that depends
on the operator noticing is not a mitigation."

**One side reading (MEASURED, `billing-pods.txt`).** The vendor's billing history
now shows the accidental machine of 2026-09-21 at **$0.0077, 28 seconds billed**
(dated 2026-09-22 UTC). The ledger's 2026-09-21 row estimated "about $0.02" and
is not edited here.

## 6. What this session did and did not do

- **Did:** ran step 0 and step 1 from the main checkout exactly as printed; took
  two read-only readings when the launcher went silent; ended the launcher and
  its `ssh`; deleted the machine; confirmed zero machines twice; recorded the
  balance.
- **Did not:** kill the stuck `ssh` on its own to let the launcher carry on,
  although that would probably have completed the slice. The line 543 comment
  records that the 2026-08-17 launches "needed their local ssh killed by hand".
  That would have been a step the plan does not contain, and the go said to stop
  on a difference. Also did not relaunch, change any file other than the ledger,
  or edit the registered launcher `launch_a3.sh`.
- **Left behind:** the slice's folder `/workspace/mvm-out/slice_handshake` on the
  network volume holds one file, `reaper.log` (469 bytes, MEASURED). It holds no
  finished-marker and no receipt, so the stale-marker risk the re-check raised
  for a second attempt does not arise.
- **The main checkout** was given the committed ledger row in its working copy
  for the launch gate to read (the gate reads the ledger beside the launcher,
  `launch_gate.sh` line 272). After the stop it was put back to `4d98cfc` exactly
  (checked with `cmp`), so no uncommitted change remains there.

## 7. For John: decisions owed (ARGUED; nothing here is ruled)

1. **Whether today's go covers a second attempt.** This session reads it as not
   covering one. It named "one toy run", and that run happened and was stopped.
   A fresh go would name the fixed launcher.
2. **The fix, drafted and not applied.** Two options for line 467, either of which
   the laptop reproduction above shows would return at once:
   - (a) give the watcher start the same 60-second cap as the training start
     (lines 549 to 553), and let the existing `pgrep` check that follows decide
     whether the watcher is up. This matches how the file already handles the
     same hang.
   - (b) change the remote command so the background job does not hold the
     connection, for example `cd /root/mvm/src; nohup sh reap_agent.sh … &`,
     or run it under `setsid` with its output redirected.

   **Confidence that (a) stops the hang: high.** It is the file's own remedy, in
   use since 2026-08-17. **Standard practice** for starting remote background jobs
   over `ssh` is (b). **The strongest alternative** is to do both. Whichever is
   chosen, it needs a test that fails today, and a stand-in `ssh` cannot provide
   one. The laptop form above (`bash -c '…' | cat`) can, because it reproduces
   the hang without renting anything.
3. **A candidate for the known-failure list** (binding text, so drafted here and
   not added): *a remote step whose only tests run against a stand-in for the
   remote end.* Such a test passes whatever the remote end does. Its test would
   be to run each remote command form against a local shell through `| cat`, with
   a time limit.
4. **A hard cap no code enforces.** Nothing in the launcher stops billing at the
   ledger's hard cap. Option (a) removes this particular route to a day of
   billing. It does not add a cap.

## 8. What is owed

- A check of this document by a different session, under the pairing rule.
- John's rulings on section 7.
- The seconds-per-step measurement. The second release still may not be asked
  for without it (ruling item 11,
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`).
