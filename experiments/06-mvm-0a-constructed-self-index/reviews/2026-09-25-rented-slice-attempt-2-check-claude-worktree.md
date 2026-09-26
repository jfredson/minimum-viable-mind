# Check of the rented slice's second attempt, at commit `7da1946`

*2026-09-25 (Pacific). A check under the pairing rule of
`docs/outside-review-protocol.md` (whatever one session writes, a different
session checks). Its target is branch `worktree-mvm-w1f-rented-slice-attempt-2`
at commit `7da1946`, open as draft pull request 51: the second attempt at the
rented slice, which this session did not write or run. The branch carries:*

- *the account of the run, `docs/2026-09-25-rented-slice-attempt-2-findings.md`
  ("the findings");*
- *its row in `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`
  ("the ledger row"), written in commit `3658a8f` before anything was created
  and completed with the actual cost in `7da1946`;*
- *the run's receipts in
  `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/`
  ("the slice receipts"), including the timing file `bench_arms.json` fetched
  from the machine;*
- *the dated note beside the spending proposal,
  `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
  ("the arithmetic note"), with the script it cites,
  `second_release_arithmetic.py`, in the slice receipts.*

*Nothing was launched, rented or spent by this session. No registered text,
ruling or protocol text was edited. The vendor was contacted only with
commands that list or read (below).*

**Labels.** MEASURED: a command was run and its output is filed. ARGUED:
reasoning a reader can dispute. Every output cited below is filed in
`experiments/rehearsal-successor-measure/out/rented-slice-attempt-2-check-2026-09-25/`,
called "this check's receipts" from here on:

- `check_attempt_2.sh` and its output `check-output.txt`: every local check,
  reading the checked commits straight out of git, contacting no vendor.
  Sections of that output are cited as "check output §1" and so on.
- `vendor_readings.sh` and its outputs `vendor-reading-1.txt` (02:13:45Z),
  `vendor-reading-2.txt` (02:19:40Z) and `vendor-reading-3.txt` (03:49:18Z,
  after the machine deadline fired; section 9 below). All read-only: account balance,
  machine list, per-machine billing, network-volume billing. The account id
  and email are removed from the copies. Reading 1 was taken before the
  network-volume query was added to the script; that query was run by hand
  at the same minute and gave the same rows reading 2 carries.
- `machine-deadline-after.log`: the machine deadline's log after it fired.

**Plain terms.** *The slice*: one short rented session on a graphics card, to
answer two questions — how long one training step takes for each of the
successor experiment's three model designs, and whether the shutdown
handshake works against the real vendor. *Arms T, C and F*: the three
designs — T keeps the ownership answer separable by construction, C
entangles it by construction, F is trained freely. *The launcher*:
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`,
the unregistered script that rents the machine and runs things on it. *The
watcher*: `src/reap_agent.sh`, started on the rented machine so it can delete
itself once the laptop confirms it has the files. *The watchdog*:
`src/watch_run_a3.sh`, on the laptop, which copies the files home, checks
them, writes a receipt file on the machine and deletes the machine. *The
handshake*: laptop writes the receipt, watcher sees it, watcher deletes. *The
machine deadline*: `src/machine_deadline.sh`, a laptop program that deletes
the machine once the hard cap divided by the hourly rate has passed. *The
second release*: the second of two stages in which the successor
experiment's money is released, to be priced from the measured seconds per
step. *Item R-11*: the rehearsal item in the successor proposal that
specifies that timing.

**What this session opened.** The four documents the brief names first
(`CLAUDE.md`, the top entry of `STATUS.md`, the pairing, isolation,
failure-mode and filing sections of the outside-review protocol, and
`docs/known-failure-modes.md`); every file the checked branch adds or
changes; the launcher, watchdog, watcher and machine-deadline code at the
checked commit; the run plan at `a96f873`
(`experiments/rehearsal-successor-measure/out/rented-slice-plan.txt`);
sections 10, 12.3 and 12.4 of `docs/successor-experiment-proposal-2026-09-21.md`
and section 3.4 of the spending proposal. **What it did not open:** the
running session's chat. A transcript of it is on this Mac; the protocol's
isolation section says the checking session gets the packet and nothing
else, so it was left closed, and that limits point 1 below.

## Verdict, point by point

| # | What was asked | Result | Label |
|---|---|---|---|
| 1 | The ledger row quotes John's go verbatim | **PASS IN PART.** The go is in the row, in quotation marks, signed and dated; its 1,450 characters are identical before and after the actual was filled in; every setting it names is in the plan's step 1 command. **Not compared with John's own message**: no committed file other than the row holds it, the brief did not carry it, and the running session's chat was not opened | MEASURED (what was compared); the word-for-word claim itself is unchecked |
| 2 | The row carries an estimate committed before the machine's creation time in the launch log | **PASS.** Committed 01:44:04Z with "$0.75–1.00, hard cap $2.00" and an empty actual; pushed 01:44:12Z; dry run 01:44:24Z; machine rented 01:46:33Z | MEASURED |
| 3 | $0.0525 equals the two balance readings' difference; has it moved? | **PASS**: 75.917054611 − 75.864512286 = 0.052542325. **Not moved.** The balance's later falls are hourly network-volume charges ($0.0097222222 each), and by 03:49:18Z the vendor's own billing row for this machine had posted at $0.052542325, 191,063 ms. One sentence of the row's explanation is not supported (finding A) | MEASURED |
| 4 | The machine is absent from the vendor's machine list now | **PASS.** `[]` at 02:13:45Z, 02:19:40Z and 03:49:18Z | MEASURED |
| 5 | `bench_arms.json` complete; T 13.08, C 13.52, F 12.53 ms match the launcher's log line for line; ratios 1.044 and 1.080 recomputed | **PASS.** `"complete": true`; each arm's line, printed from the file at the log's one-decimal precision, is character-for-character the launcher's line; ratios recompute to 1.044 and 1.080 | MEASURED |
| 6 | $129.90 against the provisional $143, both releases $161.90, reproduce from the script and from the ledger's $10.04 | **PASS.** The script's re-run is byte-identical to its committed output; an independent recomputation gives the same figures; every provisional figure is where the note says it is | MEASURED (arithmetic); the method is ARGUED in the note and flagged there |
| 7 | Receipt, checksum and delete evidenced in the logs, in the order the plan's PASS line requires of the laptop | **PASS.** Copy 01:49:38Z, checksum `b4e56e1c69cc` verified 01:49:41Z, receipt 01:49:43Z, delete 01:49:43Z answered `"deleted": true`, gone 01:49:55Z; the home model file's checksum is still `b4e56e1c69cc…` | MEASURED |
| 8 | The claim that the machine's watcher cannot see the receipt before deletion on a normal run is true of the code | **PASS, with one correction of wording.** The claim sits in the findings' section 4 (repeated in section 9), not section 8. As the findings word it — "close to unreachable", "whether the container was still alive at :46 … is not known" — it is true of the code. The stronger form, "cannot see", is not: there is a window of up to one 15-second poll. What is strictly true is that **nothing brings the watcher's line home** on that run | MEASURED (the code lines); ARGUED (the vendor's shutdown delay, which no file records) |
| 9 | The machine deadline's log for process 7745, after its 03:47:44Z attempt | **Fired at 03:47:44Z.** The vendor tool answered all three deletes with exit 1, "pod not found to terminate", status 404: it does not report success on a machine already gone. The program then logged "FAILED … may still be billing" and a ledger-style line claiming about 2.04 hours and about $2.02, which is wrong (finding B) | MEASURED |

## 1. The go, quoted word for word (point 1)

**MEASURED** (check output §1). The row is ledger line 95; commit `3658a8f`
added exactly one line to the ledger. In both `3658a8f` and `7da1946` the row
contains the go opening "“Go, second attempt." and ending "John Fredrickson,
2026-09-25.”"; the text between is 1,450 characters in both and identical.
Of the row's eight cells, cells 0 to 3 and 5 (date, what ran, machine, the
estimated time, the estimate) are unchanged; 4, 6 and 7 (the actual time,
the actual cost, the running totals) changed, which is what filling in an
actual should change. Each of the ten settings the go names (`SCALE=10M`,
`MAXTOK=2000000`, `OUT=slice_handshake`, `GRACE_S=600`,
`RUN_SUBDIR=slice_handshake`, `CLEAR_RUN_SUBDIR=1`, `HARD_CAP_USD=2.00`,
`RATE_PER_HOUR_USD=0.99`, `PRE_TRAIN_DIR`, `PRE_TRAIN_CMD`) appears once in
the go and twice in the plan (step 0 and step 1).

**What this does not show (ARGUED).** That the quoted text is what John typed.
The check of the first attempt could compare its row against the go as it was
relayed in that check's brief (all 858 characters identical;
`reviews/2026-09-25-launcher-fix-check-claude-worktree.md`, row A1). This
brief did not relay the second go, and the only other copy is the running
session's chat, which the isolation rule keeps closed to this session. So the
word-for-word claim rests on the row alone. **If John wants it closed, the
cheapest route is for him to paste the go into the handoff session's brief**,
where a `cmp` against the row settles it in one command.

## 2. The estimate came first (point 2)

**MEASURED** (check output §1).

| When (UTC, 2026-09-26) | What | Record |
|---|---|---|
| 01:43:02 to 01:43:03 | Pre-creation readings: no machines, balance $75.917054611 | `pre-pod-list.txt`, `pre-user.txt` (slice receipts) |
| 01:44:04 | Commit `3658a8f`, the row with its estimate and an empty actual | `git log` |
| 01:44:12 | That commit pushed to the remote branch | this Mac's record of the remote branch (`git reflog`), printed in check output §1 |
| 01:44:24 | Dry run (step 0) started | `step0-dryrun.txt` line 1 |
| 01:46:33 | Machine `alpua1c0w6jonx` rented | the creation record, `step1-launch.txt` line 34 |

The launch gate read the row at run time: "ledger row at line 95 names
'slice_handshake', dated within 2 days, estimate written, no actual cost yet"
(`step1-launch.txt` line 11). The push time comes from this Mac's own record
of the remote branch, not from GitHub: GitHub's public event feed, queried
during this check, carried no event for this branch at all.

## 3. The money (points 3 and 4)

**The figure (MEASURED, check output §2).** 75.917054611 − 75.864512286 =
0.052542325, which is the row's **$0.0525**. The readings are
`pre-user.txt` (01:43:03Z) and `post-user-settled.txt` (01:54:04Z) in the
slice receipts.

**Has it moved (MEASURED, vendor readings 1 and 2).**

| Reading | Balance | Machine list | Billing rows for `alpua1c0w6jonx` |
|---|---|---|---|
| 01:54:04Z (the row's) | $75.864512286 | `[]` | none (`billing-this-pod.txt`) |
| 02:13:45Z (reading 1) | $75.8547900638 | `[]` | none |
| 02:19:40Z (reading 2) | $75.8547900638 | `[]` | none |
| 03:49:18Z (reading 3) | $75.8450678416 | `[]` | **one row: $0.05254232510924339, 191,063 ms billed, hour 01:00** |

The fall between the row's reading and reading 1 is $0.0097222222. The
network volume's billing rows (reading 2) are hourly charges of
$0.009722222574 each, for 100 GB — about $7.00 a month. The two differ by
less than a billionth of a dollar, so the fall is one hourly storage charge
and nothing else. The fall between readings 2 and 3 is again
$0.0097222222, one more such charge, and reading 3's volume rows carry one
more. **Then, by 03:49:18Z, the machine's own billing row had posted:
$0.05254232510924339 for 191,063 milliseconds** (vendor reading 3). To nine
places that is the balance difference, $0.052542325, and it is also 191.063
seconds at $0.99 an hour. **So the $0.0525 has not moved, and it is now
settled by the vendor's own row, not only by the balance.**

**Finding A — one sentence of the row's explanation has no record behind it
(MEASURED arithmetic; the reading of it is ARGUED; minor).** The row says:
"190 s at $0.99 an hour is $0.052; the rest of the fall is about two minutes
of the $0.01-an-hour storage charge." The remainder is $0.000292 (check
output §2). The storage is not billed by the minute: the volume's rows are
whole-hour charges, and the one that fell after 01:54:04Z is exactly one of
them. The remainder is instead what 1.06 seconds more of machine time at
$0.99 an hour costs, and the vendor's row now says exactly that: 191,063
milliseconds billed against the 190 seconds the logs measure from creation
to deletion, and not a cent of storage in the machine's row. The figure is
right; its explanation is not what the records show. The findings' own money section (section 6) does not repeat
it. Suggested wording for an annotation beside the row (not made
here): "settled by the vendor's billing row, $0.0525 for 191.063 s; the
remainder over 190 s is about one second more of billed machine time, not
storage, which is billed in whole hours."

**The machine is gone (point 4, MEASURED).** `runpodctl pod list` returned
`[]` at 01:50:00Z (`post-pod-list.txt`), 01:52:46Z and 01:54:04Z
(`post-user-2.txt`, `post-user-settled.txt`), and in this session at
02:13:45Z, 02:19:40Z and 03:49:18Z (vendor readings 1 to 3).

**Observation beside the check, for ruling (4) below.** The first attempt's
machine, `c14x21x0u3ju7r`, now has two billing rows, $0.1562 and $0.3600,
together **$0.5162** (vendor readings 2 and 3, unchanged between them), against that row's $0.4974. The
check of the first attempt saw them at $0.3215. They have kept posting. This
session did not annotate that row; John's ruling (4) says both rows are
annotated after a day, which this is not yet.

## 4. The timing file (point 5)

**MEASURED** (check output §3). `bench_arms.json` says `"complete": true`,
`"device": "cuda"`, accelerator "NVIDIA GeForce RTX 5090". Printed from the
file at the one-decimal precision the launcher's log uses, each arm's line
is character-for-character the log's (`step1-launch.txt` lines 82, 84, 86):

| Arm | File, mean (ms) | File, median | Launcher log line | Identical |
|---|---|---|---|---|
| T | 13.08 | 13.08 | "arm T: 13.1 ms/step (median 13.1), 26,065,471 parameters" | yes |
| C | 13.52 | 13.51 | "arm C: 13.5 ms/step (median 13.5), 29,329,735 parameters" | yes |
| F | 12.53 | 12.52 | "arm F: 12.5 ms/step (median 12.5), 29,049,735 parameters" | yes |

Ratios recomputed from the means: **T 1.044, C 1.080**; the same in the
file's own `ratio_to_arm_F` and in the log's line 88. The fetched home copy
of the file is byte-identical to the one in the slice receipts (check
output §9; the home copy is git-ignored, in the main checkout's
`experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/`).

The findings say each arm's slowest step is "within 3% of the median". It
is: 0.4% for T, 2.8% for C, 0.5% for F (check output §3).

## 5. The second-release arithmetic (point 6)

**MEASURED** (check output §4). Run from the repository root at `7da1946`,
as its opening lines say (run from its own folder it cannot find its input
and stops), `second_release_arithmetic.py` exits 0 and its output is
byte-identical to the committed `second-release-arithmetic.txt`. The
sentence it anchors on, "20.28 pod-hours at $0.99 = $20.08", is on ledger
line 88, the 2026-09-17 row; half of it is the $10.04 a run.

Recomputed separately, from the means in `bench_arms.json` and not from the
script's code: per run F $10.04, T $10.48, C $10.84; eight remaining runs
(two F, three T, three C) $84.06; the re-run at the dearest arm $10.84;
with the two unchanged lines ($12 and $23) the second release is
**$129.90**; with the first release's $32, **$161.90**. From the rounded
ratios 1.044 and 1.080 the answer is the same to the cent. Against $228.1
already spent, both releases leave about $10.0 under $400 and $60.0 under
$450.

The script types in the unchanged lines and the provisional figures rather
than reading them, so they were checked against the successor proposal at
`7da1946`: $96 (line 1051), $143 (line 1055), the first release's $32 (line
954), and "$32 plus $143 is $175" (line 1067). Item R-11's "Five hundred
steps per arm" is on line 695, as both the findings and the note say.

The method — the measured run cost times each arm's measured ratio, rather
than the measured seconds turned into hours — is ARGUED in the note, and the
note says why (a real run does much more per step than the timed pass: 8.7
times the timed pace per token, from its own output). That is a reasonable
choice and the note flags its limits; this check did not re-argue it.

## 6. Receipt, checksum, delete (point 7)

**MEASURED** (check output §5). From `watchdog.log` in the slice receipts:

| UTC | Line |
|---|---|
| 01:49:38 | "final fetch OK" |
| 01:49:41 | "final checkpoint VERIFIED (md5 b4e56e1c69cc)" |
| 01:49:43 | "receipt written on the machine — it may delete itself now" |
| 01:49:43 | "deleting pod alpua1c0w6jonx", then `"deleted": true` |
| 01:49:55 | "pod gone; billing stopped" |

That is the laptop's part of the plan's PASS line in the order it requires:
the copy is checked against the machine's own checksum before the receipt
(the watchdog computes `md5sum` on the machine and compares, lines 163 to
169 of `watch_run_a3.sh`), the receipt is written, and the deletion follows
within seconds. `model-md5.txt` holds `b4e56e1c69cc10f4033cece45bab4da8`,
and the home model file (77,450,933 bytes) still has that checksum today.
The machine's part of that line, "receipt found" in the watcher's log, does
not appear: the log fetched home has zero such lines and ends at 01:49:01Z.

## 7. Can the watcher see the receipt on a normal run? (point 8)

**Where the claim is.** The brief calls it the section 8 claim. It is in the
findings' section 4, under "Why the machine half could not be exercised",
and section 9 item 1 builds on it. Section 8 is the list of what the running
session did.

**The code (MEASURED, check output §6; the branch changes no code — zero
files differ under either `src` folder between `a96f873` and `7da1946`).**

- `watch_run_a3.sh` lines 240 to 244: `if fetch_final; then write_receipt;
  kill_pod; say …; exit 0`. The receipt and the delete are consecutive lines
  with no wait between them. `write_receipt` (lines 180 to 186) is one `ssh`
  that writes the file and returns.
- `reap_agent.sh` line 97: `AGENT_POLL_S="${AGENT_POLL_S:-15}"`. The loop
  checks for the receipt (lines 234 to 236) and then sleeps that long (line
  258). The launcher passes its own default of 15 to the machine (lines 166
  and 606), and the plan's step 1 command does not set it.
- The only call to `fetch_final` on the finishing path is line 240, before
  the receipt. The other, line 290, is on the +24-hour deadline path. So on
  a normal run **nothing the laptop does after the receipt copies anything
  home**, including the watcher's log.

**The timing, against the logs (MEASURED times; the conclusion ARGUED).**
The watcher saw the finished-marker at 01:49:01Z (`reaper.log`), so its
later checks fall at about 01:49:16, :31 and :46. The receipt went at :43
and the delete at :43; the delete had returned by about :45 (the "pod gone"
line at :55 follows a 10-second pause, `KILL_SETTLE_S`, line 91). The
watcher's :46 check would find the receipt only if the vendor had not yet
stopped the machine one to three seconds after accepting the delete. How
long the vendor takes to stop a machine after a delete is in no file here.

**So:**

- *"The machine half could not be observed on this run"* — **true of the
  code.** Even had the watcher found the receipt, its line went to
  `reaper.log` on the network volume after the only copy home.
- *"The watcher cannot see the receipt before deletion"* — **not strictly
  true.** It has a window of up to one poll interval after the receipt, and
  whether that window closes before the machine stops depends on the vendor.
  The findings' own words ("close to unreachable", "almost always first",
  "not known") are the accurate ones, and nothing in the findings overstates
  it.
- *"Written where nothing will fetch it"* — **true for this go, not for
  ever (ARGUED).** `reaper.log` is on the network volume, which outlives the
  machine, and John's ruling (5) keeps the slice's folder there until the
  first registered run's pre-flight clear. That clear step lists every file
  with its size before emptying the folder (launcher line 510, `ls -la`;
  it printed exactly such a listing on this run, `step1-launch.txt` lines 62
  to 66). **The copy of `reaper.log` fetched home is 873 bytes** (check
  output §9). If that listing shows it larger, the
  watcher wrote something after 01:49:01Z — most likely "receipt found" and
  its delete attempt — and the machine half did run. This costs nothing
  beyond a rental that is happening anyway, and the handoff session may want
  to write it into the first registered run's plan as a line to read.

## 8. What else was run: the known failures against this branch

The outside-review protocol's failure-mode pass is owed by Gate A texts
(registrations, amendments, threshold locks, pre-statements). Nothing on
this branch is one, so no formal pass is owed. The six failures were run
against it anyway, briefly, because the branch makes claims about
measurements and money.

1. **A comparison whose denominator was zero.** The only ratios are to arm
   F's mean, 12.53 ms (check output §3). Not zero. MEASURED.
2. **A probe target that cannot be recovered in principle.** The findings
   and the arithmetic note contain the word "probe" zero times
   (check output §9); nothing on the branch fits or reads a
   probe. Stays inapplicable to a timing-and-billing record. MEASURED.
3. **A cell that is empty by construction.** Yes: the plan's handshake PASS
   line, as the findings say. Section 7 above confirms from the code that on
   a normal run its middle signal cannot come home. John has ruled this in
   as failure 7 (ruling (2) below); this session did not write the entry.
   MEASURED (code), ARGUED (that it is the same shape).
4. **A claim of measurement with no record, or a record that does not
   reproduce.** Every number checked above has its record, and each
   reproduced. Two exceptions: finding A (the storage explanation of the
   remainder), and the claim that the row was pushed before creation, which
   had no committed record and now has one in this check's output. MEASURED.
5. **A command that creates something while documented as creating
   nothing.** The branch changes no launcher (zero files under `src`,
   check output §6); this session ran no launcher, not even a dry run. The
   one command that could have acted on the vendor afterwards, the machine
   deadline's delete, did nothing and said so (section 9); its record line
   is the one place a claim came out wrong (finding B). MEASURED.
6. **A remote step tested only against stand-ins.** The watcher-start fix
   passes its test on the launcher that ran (line 616 returns in 0.0 s; the
   pre-fix form is rejected; check output §7). **But the handshake's machine
   half — the watcher finding the receipt and deleting — has still only been
   exercised against local stand-ins**, which is exactly this failure's
   species, and it stays open until a run shows "receipt found" from a real
   machine. The findings say so in their own words; ruling (1) settles what
   the registration text says in the meantime. MEASURED (the test), ARGUED
   (the remaining gap).

## 9. The machine deadline's attempt on the deleted machine

**MEASURED** (`machine-deadline-after.log` in this check's receipts, a copy
of the git-ignored log in the main checkout's
`experiments/06-mvm-0a-constructed-self-index/artifacts/slice_handshake/`,
taken at 03:49Z; the process was watched until it exited).

The program fired on time and did what its code says (lines 57 to 78 of
`src/machine_deadline.sh`):

| UTC, 2026-09-26 | Line (the vendor's answer cut at 200 characters by the program) |
|---|---|
| 03:47:44 | "DEADLINE REACHED. Deleting alpua1c0w6jonx. Reason: hard cap reached: $2.00 at $0.99 an hour allows 7272s of machine life; run state was not consulted" |
| 03:47:45 | "delete attempt 1: exit 1: {"error":"api error: {\"error\":\"pod not found to terminate\",\"status\":404}…" followed by the tool's usage text |
| 03:48:08 | attempt 2: the same, exit 1 |
| 03:48:29 | attempt 3: the same, exit 1 |
| 03:48:49 | "delete command FAILED 3 times (exit 1) -- the machine may already be gone, or may still be billing: check the vendor's machine list NOW" |
| 03:48:49 | a "LEDGER-STYLE LINE" (quoted in finding B) |

Process 7745 then exited. The machine list read `[]` at 03:49:18Z (vendor
reading 3).

**The answer to gap (c) of the first attempt's check** — does the vendor's
tool report success on a delete that did nothing? **No, not for a machine
that no longer exists.** `runpodctl` 2.6.1 exits 1 and says "pod not found
to terminate" with status 404. So on this path the deadline cannot mistake
an already-gone machine for one it deleted. What this run does not show:
what the tool says for a machine that exists but will not stop, which is
the case gap (c) is really about. MEASURED for the gone machine; the other
case is untested.

**Finding B — the deadline's record line is wrong in a way a session could
copy into the ledger (MEASURED; minor today, it matters on a real run).**
The line it printed for a session "to copy into ../compute-ledger.md" reads,
in part: "machine `alpua1c0w6jonx` delete command FAILED 3 times … act: about
2.04 h of machine life by the laptop clock | cap $2.00 | by arithmetic at
most about $2.02". The machine lived 190 seconds (0.053 hours) and billed
$0.0525 (section 3). The program measures "machine life" as time since
creation (line 74, `LIFE=$(( $(date +%s) - CREATED_AT_EPOCH ))`), which is
right only when it is the thing that ends the machine. It also reports the
same "FAILED … may still be billing" for a 404 as for any other failure,
though the vendor's answer already says which. Two ways to repair it, for
John or the handoff session (ARGUED; nothing changed here): have the program
read the machine list once before deleting and, if the machine is absent,
log "already gone; nothing to delete" and no ledger line; or treat a 404
answer as "already gone". The first is the more robust. It is code on an
unregistered launcher's companion, so a fix goes through the pairing rule
like the last one. Until then, **nobody should copy this program's ledger
line without checking the machine list and the billing row first** — which
is what its own "check the vendor's machine list NOW" asks, and which
this check did.

**Worth recording beside it (ARGUED).** The deadline outlived its machine by
almost two hours and still fired, as designed ("whether the machine was
already deleted" is on its list of things it deliberately does not look
at, lines 22 to 27). On a run where the machine ends normally, it will always end
this way: three failed deletes and a false-looking ledger line two hours
later. That is harmless while someone reads it and misleading if someone
reads it in a hurry.

## 10. Smaller observations

- **The account email is in the slice receipts** (`pre-user.txt`,
  `post-user*.txt`), in a public repository. The findings say only the
  account id and SSH keys were removed. Four files here carry it (check output §9). This adds
  nothing new — on the main line the first attempt's `pre-user.txt` carries
  it in the same form (check output §9), and
  `experiments/06-mvm-0a-constructed-self-index/runpod-ticket-overrun.md`
  in plain text (a `git grep` at `a96f873` during this check) — but if John wants it out, it is a redaction for all
  three sets of receipts together, not this branch alone. Not changed here.
- **Running the arithmetic script from the wrong folder** fails at once with
  a missing file, and says nothing wrong about the numbers. Its opening
  lines say to run it from the repository root. No change needed.
- **The "Terminated: 15" lines** in `step1-launch.txt` (lines 71 and 92)
  are as the findings explain: the first is `ssh_capped`'s own 60-second
  timer being stopped when the connection returned first (launcher lines 473
  to 482, `kill "$killer"`); the log carries no "cut off at 60s" line, so the
  watcher start returned before the cap. The second is the timing step's
  timer (line 681). MEASURED by reading the code against the log.

## 11. John's rulings on the findings' section 9, recorded as his

*Given 2026-09-25 (Pacific), "agreed on all", relayed to this session in its
brief and recorded here in the brief's words. This session has not acted on
any of them; they are for the handoff session.*

1. The registration text says the laptop is the reap and the machine's
   watcher the backstop; option (a) (make the watchdog wait for the watcher
   and bring its line home) is a Weekend 2 item.
2. The candidate — an outcome line a plan states in advance that the design
   it tests cannot produce on the path it expects — is added to
   `docs/known-failure-modes.md` as failure 7.
3. Fifty steps prices the second release; R-11's five hundred rides on the
   first registered-size run.
4. Both attempts' ledger rows are annotated after a day (with the settled
   figures).
5. The 77 MB toy model stays in the slice's folder on the network volume
   until the first registered run's pre-flight clear.

**What this check hands to them (ARGUED).** For (2): section 7 above is the
code evidence the entry can cite, and the entry is binding text, so a
different session checks it. For (4): the first attempt's rows now sum to
$0.5162 against its row's $0.4974; the second's has posted at $0.0525,
exactly its row's figure (section 3). Finding A's wording can go in the
second row's annotation. If the annotation mentions the machine deadline,
it should say the deadline's ledger-style line is not to be copied
(finding B). For (5): the 873-byte size of
`reaper.log` is the thing to read in that pre-flight listing (section 7).
For (1): nothing further.

## 12. What is owed

- The handoff session: act on rulings (1) to (5); add failure 7 and have it
  checked; annotate both slice rows after a day.
- A decision on finding B (the machine deadline's record line after a
  normal finish): fix it, or note it beside the program. Not ruled.
- If John wants point 1 closed: the text of his go, pasted into a brief, to
  compare with the row.
- This check is itself a filed record under the pairing rule; it changes no
  binding text, so it is not owed a check of its own unless the handoff
  session builds binding text on it.
