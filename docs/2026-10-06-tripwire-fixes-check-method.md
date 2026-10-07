# Method: independent check of the spending-alarm fixes (pull request 116)

*Written 2026-10-06 (Pacific) by a Claude Code session that wrote none of pull
request 116, in its own worktree (`~/Code/mvm-tripwire-check`, branch
`check-tripwire-fixes`, cut from `tripwire-fixes`). Committed before any
check script is written. Cost: $0. Nothing is rented; no paid call and no
call to the vendor's service is made. Reading the vendor's public source code
on GitHub and the text inside the vendor tool already installed on this
laptop is allowed; running that tool is not.*

Before this note was written the checker had already done three read-only
things, stated here so nothing is hidden: read the pull request, its method
note and its code changes; re-run the pull request's own check once and the
alarm's own self-test once; and searched the repository and the vendor tool's
public source for the vendor's "not found" wording. Everything below is still
to be done.

## What is checked

The four rulings of 2026-10-06 (page 2 of
`docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`, pull request 109),
as carried out in pull request 116:

1. the spending alarm reads every 5 minutes during a wave, with an in-flight
   rule ("rule S") and a rule at each deletion ("rule D");
2. every step that deletes a machine writes the deletion time into the
   alarm's records;
3. an empty or zero bill at the end-of-wave comparison is "cannot be checked
   yet", which is a trip;
4. the laptop deadline timer stops itself only on a confirmed deletion.

## Steps

1. **Commit order.** Confirm from the branch history that the method note
   was committed before any code change.
2. **Re-run every test** the pull request names (its own check, the alarm's
   self-test, the deadline timer's self-test, the watchdog handshake test,
   the launch gate and sleep guard self-tests, the successor launcher check,
   the successor self-test suite) at least three times where timing is
   involved, and compare with the committed output.
3. **"Not found" as proof of deletion.** Collect every recorded vendor answer
   in the repository, and the wording in the vendor tool's public source
   (version 2.6.1, the one installed), and list every way an answer that does
   *not* mean "this machine does not exist" can still contain the words
   "not found" or "404". For each, say whether it can reach the timer, the
   watchdog, the launcher or the alarm, and what follows.
4. **The watchdog's "gone" record.** Trace by reading the code whether a
   failed reading after an accepted delete can produce the record and so
   stand the deadline timer down.
5. **The thresholds.** Write a scratch script, separate from the alarm's
   code, that applies rule S and rule D to every recorded billing figure in
   the repository that can be turned into "money drawn against money
   predicted": the 2026-10-04 development run, the 2026-09-25 rented slices
   (both attempts), and the 2026-08-08 run that billed about 3.5 times the
   machine's life, plus the waves recorded in the compute ledger where both
   a balance change and machine hours exist. For each, report whether the
   rules would trip, and whether an honest one would falsely trip. Where a
   recorded figure is a whole-run total rather than a series of readings,
   say so and model the readings explicitly, stating the assumption.
   **Expected before looking:** a 3.5-times overcharge trips rule S within
   about 25 minutes of a machine starting, once the prediction passes $0.25,
   *if* the overcharge shows in the balance while the machine runs; if the
   2026-08-08 overcharge only appeared on the bill afterwards (the bill
   "grew overnight"), the in-flight rules cannot see it and only the
   end-of-wave comparison can. Honest waves are expected not to trip.
6. **The end-of-wave comparison.** Find where it is run and whether anything
   stops it being run before the bills post; and whether a bill that has
   posted only in part can pass.
7. **Experiment 06's launchers.** Read which of them use the changed watchdog
   and deadline timer, and whether their behaviour changes.
8. **The two unannounced fixes** (a machine listed again; the 20-second limit
   on the timer's vendor read): read and test.
9. **Shared records.** Check whether several programs writing the alarm's
   records at once can lose a write.
10. **A mid-wave top-up** of the account: whether money added during a wave
    would hide spending from the balance comparison, whether that is
    plausible on this account (from the ledger), and whether it needs a
    ruling.

## Output

Findings note `docs/2026-10-06-tripwire-fixes-check-findings.md`, scratch
scripts under `experiments/08-successor-degree/tests/check-of-116/` with
their outputs, and a pull request titled "Check of the spending-alarm fixes
(pull request 116): <verdict>", not merged. Severity is ranked by what a
fault would cost on the approved $1.14 reruns and later waves.
