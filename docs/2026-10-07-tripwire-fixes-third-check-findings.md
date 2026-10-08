# Third check: the spending-alarm fixes (pull request 116)

*2026-10-07 (Pacific). Same checker as pull request 117's first two rounds,
which wrote none of pull request 116. Method committed first:
`docs/2026-10-07-tripwire-fixes-third-check-method.md`. Cost: $0. Nothing
rented; no call to the vendor's service. Outputs:
`experiments/08-successor-degree/tests/check-of-116/round3/` and the
`third_check_*` files beside it.*

## Verdict

**Ready to merge. Both blockers from the re-check are fixed.**

One small inaccuracy is left: problem 1 below, a one-line fix, worth under
a cent. Fixing it before the merge is better, but it need not hold the merge.

The work is safe for the approved $1.14 reruns under the operator rules: a
new wave name; no top-up during the wave; the end-of-wave comparison no
earlier than 3 hours after the last deletion.

## The two blockers

**1. Pull request 116's own check failing on timing: fixed.** Eight runs of
my own, load between about 2 and 5, are summarised in `round3/summary.txt`
(**8 of 8 passed, 82 checks each, 0 failed**; the one pre-stated replay range still reported as missed, as declared).

- The fix skips the timer's vendor check when the deadline is under two
  caps plus 2 seconds away. Tests time the delete from the stand-in's own
  log and allow 10 seconds after the deadline.
- The hollow passes are fixed. Every named timer case that tests a vendor
  answer must now make at least one vendor read (N7 exactly one), and R3
  must make none.
- The first-round scripts and the round-two timer script, re-run
  unchanged, give the expected results with one exception. The genuine
  "pod not found (status 404)" case had an 8-second deadline, which now
  sits inside the skip window. With a 20-second deadline the timer stands
  down without deleting, as before.

**2. An honest short machine halted at the 0.90 line: fixed.** The fix has
two parts:

- the watchdog now writes the alarm's deletion time straight after an
  accepted delete;
- for an inferred deletion, the 0.90 line uses the last reading that still
  listed the machine.

`third_check_inferred_bill.py` drives the alarm's own commands. Every
honest bill passes:

- 20-minute, 29-minute and 44-minute machines with inferred deletions;
- a 3-minute machine, whether its deletion was inferred or recorded.

A half-posted bill still halts as "cannot be checked yet".

**`pod list --all`** is now in both list checks: the timer's and the
watchdog's.

## Problems left

### 1. The timer can still delete up to about 28 seconds late with the real settings (minor; one line)

After a vendor check, the timer sleeps for the shorter of its poll (30
seconds) and the time left. But "time left" is worked out from the clock
reading taken *before* the check. A check that starts just outside the skip
window can take up to two caps (40 seconds). The sleep that follows can then
run past the deadline by up to about 28 seconds.

With a stand-in whose reads hang (`third_check_skip_window.sh`), the delete
was issued:

- 4 seconds late at a 3-second cap and 10-second poll;
- 5 seconds late at a 5-second cap and 20-second poll.

The tests miss this because they poll every second. The cost is under a
cent at $0.99 an hour. But section 13.1 and the code comment say vendor reads
"never delay" the deadline, which is not true.

**Fix:** read the clock again after the check, before working out the
sleep. For example, recompute the time left from a fresh `date +%s` just
before `sleep`.

### 2. Minor notes, no action needed

- The 1.25 overbilling line still uses the inferred deletion time. An
  inferred time is late, so a 20-minute machine billed 1.3 times its life
  read 1.24 and did not trip. This is as ruled, and stated in 13.2. It
  leans toward missing a mild overcharge, not toward a false halt. It only
  matters when no deleting step recorded a time, which is now rare because
  the watchdog writes it at once.
- Commit `a164eaf`'s message says "Timer code unchanged", but the commit
  carries the code fixes. Section 13.7 states this plainly.
- The order holds:
  - method `32fdbc4` at 22:23:55;
  - the first run, kept as it came out, at 22:31:02;
  - code `a164eaf` at 22:31:32.

  The kept first run tested code that was in the working copy but not yet
  committed (said in 13.7). Every failing attempt was kept this round.

## Tests re-run

- Pull request 116's own check: 8 runs (**8 of 8 passed, 82 checks each, 0 failed**; the one pre-stated replay range still reported as missed, as declared).
- First-round and second-round scripts: as above.
- New scripts:
  - `third_check_inferred_bill.py`;
  - `third_check_skip_window.sh`.
