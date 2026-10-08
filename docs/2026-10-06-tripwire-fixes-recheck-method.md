# Method: re-check of the spending-alarm fixes (pull request 116, second round)

*Written 2026-10-06 (Pacific), before any re-check script, by the same
session that wrote the first check (pull request 117) and none of pull
request 116. Cost: $0. Nothing rented, no call to the vendor's service.*

What has been done before this note: fetched the branch, listed the five new
commits (`de5f0c2` to `001b786`) and which files each touched, and read
sections 11 and 12 of `docs/2026-10-06-tripwire-fixes-method.md`.

## Steps

1. **Order.** Each round's method commit came before its code commit and
   touched only the method note; later edits to the note only add.
2. **Each finding of the first check, re-tested with the first check's own
   scripts, unchanged**, against the new code:
   - `tests/check-of-116/not_found_wording.sh`: the three false "not found"
     answers must now leave the timer armed. (Its stand-in gives no machine
     list, so the genuine wording should now *also* stay armed; a version
     with a good, empty machine list is added for that one case.)
   - `tests/check-of-116/shared_records_race.py`: both lost writes must now
     survive.
   - The watchdog's record must not follow a failed read (problem 2), read
     in the code and run through a stand-in.
   - The flaky timer test (problem 7): five full runs.
   - Pull request 116's description (problem 8).
3. **John's three rulings as ruled:** bills below 0.90 of life are "cannot
   be checked yet"; the 3-hour operator rule is written where an operator
   reads it; a rise in the balance restarts the in-flight comparison, is
   logged, and does not trip.
4. **Look hardest at:**
   (a) the 15-minute look-back after a top-up: compute what overcharge it
       misses and for how long, with the lag actually recorded;
   (b) the 0.90 line against the two honest bills, and whether billing
       from the machine's start-up rather than its creation, or a laptop
       creation time taken late, could make an honest bill read below 0.90
       or above it;
   (c) the timer now standing down no sooner than 5 minutes after the first
       good check: what that costs, and whether a deleted machine can ever
       still be deleted twice;
   (d) every path by which the timer can stand down while a machine still
       bills.
5. Re-run every test: pull request 116's own check (five runs), the alarm's
   self-test, experiment 06's self-tests, the successor launcher check and
   self-test suite.

**Expected before looking:** findings 1, 2, 4, 7, 8 fixed; (a) misses
overcharges up to roughly 1.4 times for a short remaining wave, as the
builder states; (b) unknown; (c) acceptable, since a confirmed deletion was
real; (d) no path left except the vendor itself lying in both the read and
the list.
