# The launcher fix after the hung rented slice, 2026-09-25

*Written 2026-09-25 (Pacific) by a Claude Code session in its own worktree
(branch `worktree-w1f-launcher-fix`), acting on John's ruling of 2026-09-25,
"agreed on all", on the three items of section 7 of
`docs/2026-09-25-rented-slice-findings.md` (the account of the first attempt,
which hung and cost $0.4974 — the 2026-09-25 row of
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`). Under the
pairing rule of `docs/outside-review-protocol.md`, a different session checks
this work. That check has not happened. Nothing was rented, no machine was
created and nothing was spent.*

*Labels. **MEASURED**: a command was run and its output is filed. **ARGUED**:
reasoning a reader can dispute. Every output named below is in
`experiments/rehearsal-successor-measure/out/launcher-fix-2026-09-25/`, called
"the receipts folder" from here on.*

**Plain terms.** *The launcher*: the unregistered script that rents a machine
and runs things on it, `experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`.
The registered launcher, `launch_a3.sh`, is not edited. *The watcher*: the
small program started on the rented machine so it can delete itself once the
laptop confirms it has the files (`src/reap_agent.sh`). *Stand-in*: a fake
version of a tool, used in tests so that nothing real is rented.

## What was done

**1. The hang, fixed both ways.** The watcher start (line 467 at commit
`4d98cfc`) now sends `cd /root/mvm/src || exit 1; nohup sh reap_agent.sh … &`,
in which only `nohup` runs in the background and all its output is
redirected, so nothing holds the connection; and the `ssh` that sends it is
cut off after 60 seconds by a small helper, `ssh_capped`, the same cap the
training start has carried since 2026-08-17. The only other background start
over `ssh` in the launcher is the training start, which was already capped
and is left as it was (see "Left as it was" below). MEASURED:

- the findings' own laptop reproduction, re-run: 8 s as launched, 0 s for the
  control; the launcher's real old form 8 s, the new form 0 s, with the
  background program still running after the new form returned
  (`hang-reproduction.txt`, produced by `hang-reproduction.sh`);
- a new check, `src/check_remote_forms.py`, that runs every background start
  the launcher sends over `ssh` against a real local shell: on the launcher
  at `4d98cfc` it fails at line 467 (held 8.1 s, nothing cuts it off)
  (`check-remote-forms-at-4d98cfc.txt`); on the fixed launcher it passes
  (`check-remote-forms-fixed.txt`); its negative control, the pre-fix form,
  is rejected in both runs. Run read-only on the registered launcher's text,
  it passes: that file's own background start has no `cd` in front of it and
  returns at once (`check-remote-forms-registered-launcher-read-only.txt`).

**2. A deadline on this laptop, from the hard cap.** When `HARD_CAP_USD` and
`RATE_PER_HOUR_USD` are both given, the launcher starts
`src/machine_deadline.sh` the moment the machine exists, detached and under
the keep-awake command. It deletes the machine once cap ÷ rate hours have
passed since creation, whatever the run is doing, and writes the reason and a
line in the ledger's column order to `machine-deadline.log` beside the run's
files. Off unless the cap is given. The slice's plan passes $2.00 and $0.99 an
hour, so 7,272 seconds, about 2 h 01 min (`rented-slice-plan.txt`, "What it
costs"). MEASURED, `selftest-machine-deadline.txt`, 20 passed and 0 failed,
behind a stand-in rental tool that logs every call and a clock shortened by
caps of a fraction of a cent: the program deletes at its deadline and not
before (a negative control with the deadline 60 s away deletes nothing in
4 s); **with the whole launcher stuck on its first `ssh`, the way it was stuck
on 2026-09-25, the machine was deleted 4 s after creation for a 4 s
deadline**; a higher rate on the vendor's creation record shortens the
deadline; with no cap nothing is armed; a cap with no rate is refused.

**3. The known-failure list.** Entry 6, "A remote step tested only against
stand-ins", is added to `docs/known-failure-modes.md` in the list's existing
form, with `check_remote_forms.py` as its test and both outputs printed (the
pass on the fixed launcher and the failure on the launcher the slice ran).
John ruled the addition on 2026-09-25. It is binding text and is owed a check
by a different session. The list's opening section, which counts five
failures, is left as written; the new entry says so.

**4. The leftover files on the network volume.** The volume can only be read
from a rented machine. MEASURED on this laptop: the vendor tool's only
read of a volume, `runpodctl network-volume get x9f8pkn58t`, returns four
fields (`dataCenterId`, `id`, `name`, `size`) and no file listing, and no
other tool here reaches the volume's files (none of the S3-style clients
`aws`, `s5cmd` or `rclone` is installed, and there is no `~/.aws` folder). The
last reading of the slice's folder is the one the first attempt took on the
machine at 2026-09-26T00:19:13Z, 33 seconds before deleting it: one file,
`reaper.log`, 469 bytes, and no finished-marker, receipt or output file
(`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25/remote-state-at-stop.txt`).
That the folder is unchanged since is ARGUED: nothing that could write to it
ran after the machine was deleted. So a pre-flight step is added: with
`CLEAR_RUN_SUBDIR=1`, which the plan passes, the launcher lists the slice's
own folder, names any leftover finished-marker, receipt, model or timing file,
and empties the folder **before the watcher starts** (a leftover marker and
receipt would let the watcher delete a fresh machine before it trains). It
refuses to run without `RUN_SUBDIR`, so the shared folder is never emptied.
This step has run only in the dry run; nothing has exercised it on a machine.

**5. The plan, regenerated.** `stage_rented_slice.sh` now passes the cap, the
rate and the clear to the launcher in steps 0 and 1, adds step 1a (the
clear), tells the operator what the dry run and the launch must now print,
adds an outcome line for a run cut off by the cap, and checks, before
staging, that the deadline program exists and that `check_remote_forms.py`
passes. The diff is `plan.diff` in the receipts folder. MEASURED: the stager's
preconditions all pass (exit 0). Step 0's dry run, run with the plan's
settings against this branch's launcher behind stand-ins, exits 0, makes no
call to the rental tool or to `ssh`, and prints every line the plan now
requires (`step0-dryrun-behind-standins.txt`, by
`step0-dryrun-behind-standins.sh`). The four launcher self-tests pass:
argument guard all checks, launch gate 369 and 0, sleep guard 67 and 0,
shutdown handshake 26 and 0 (`selftest-*.txt`).

## Who decided what

- **John** ruled the three items on 2026-09-25: the fix both ways, the laptop
  deadline, and the known-failure entry.
- **This session** decided, on its own authority, while building: the exact
  command form (`cd … || exit 1; nohup … &`) and the `ssh_capped` helper; the
  names `HARD_CAP_USD`, `RATE_PER_HOUR_USD`, `CLEAR_RUN_SUBDIR`; counting the
  deadline from just before the create call; using the vendor's stated rate
  when it is higher than the one given; that the deadline program deletes
  without checking whether the machine is already gone, and retries three
  times; clearing the whole slice folder rather than only the marker files;
  adding the remote-forms check to the stager's preconditions; the new
  outcome line "CUT OFF BY THE CAP"; and printing main-checkout paths in the
  plan when it is regenerated from a worktree.

## Left as it was, and what is owed (ARGUED)

- **The training start** (the other background start over `ssh`) keeps its
  old form and its 60-second cap, as the ruling's scope ("any other uncapped
  background start") says. It still holds its connection for the full minute
  on every launch (`check-remote-forms-fixed.txt`). Giving it the new form is
  a one-line change for a later go.
- **The deadline runs on this laptop's clock.** If the laptop is off the
  network or powered down at the deadline, it cannot delete. The launch gate
  already refuses a launch while this Mac can sleep. The machine's own
  +24-hour deadline remains behind it. Billing between the deadline and the
  vendor acting on the delete is not covered, and is seconds.
- `src/derive_fetch_first_launcher.py` was already out of step with the
  launcher before this change and is not updated.
- A check of all of this by a different session; then a fresh go from John
  naming the regenerated plan, before any second attempt.
