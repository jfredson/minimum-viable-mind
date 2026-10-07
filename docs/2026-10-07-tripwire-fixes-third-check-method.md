# Method: third check of the spending-alarm fixes (pull request 116)

*Written 2026-10-07 (Pacific), before any script, by the checker of pull
requests 117's first two rounds, which wrote none of pull request 116.
$0: nothing rented, no call to the vendor's service. Done before this note:
listed the eight new commits and the files each touched.*

Steps:
1. Order: the method commit (`32fdbc4`) comes before the code (`a164eaf`).
2. Blocker 1 (timing): read the timer's new skip rule and show, with a
   stand-in vendor, that it never delays the delete past the deadline by
   more than the allowance, including with a hanging vendor and with the
   deadline at the edge of the skip window. Check that every timer test
   case that claims to test a vendor answer actually made a vendor read.
3. Blocker 2 (honest short machines halted): re-run the first rounds'
   scripts, and a new case: a 20-minute machine whose deletion was only
   inferred, reconciled against an honest bill, must not halt; a genuine
   partial bill must still halt.
4. `pod list --all` in both list checks.
5. Run pull request 116's own check 8 times, noting the machine's load.

Expected: both blockers fixed; no new route to a late or skipped delete.
