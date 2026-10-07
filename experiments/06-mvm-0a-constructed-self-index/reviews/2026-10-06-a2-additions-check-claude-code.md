# Check of the floor cases and outcome wording added to pull request 105

*Method, committed before any check below runs. Written 2026-10-06 (Pacific)
by a Claude Code session that wrote none of the additions, none of the
decision code and none of the earlier check. Laptop only, nothing trained,
loaded or rented: $0.*

## What is checked

Pull request 105 (branch `a2-decision-procedure`) holds the successor
experiment's decision code: the code that decides, from the training runs'
records, which registered outcome the experiment reports. Two commits were
added after the first independent check (pull request 107):

- the method addendum and three new made-up cases with their expected
  outcomes (commit `400c265`, "method addendum: three floor cases"):
  case 23, arm C misses the minimum share of fresh episodes; case 24, arm T
  misses the minimum share of development episodes; case 25, arm F misses
  the minimum share of fresh episodes;
- the code changes and their outputs (commit `d776c70`, "25 of 25 cases
  match"): the "substrate not a testbed" outcome (R3) now names the gate
  condition and seeds that failed; "metric does not separate" (R2) carries
  the scope phrase; the self-test that no fresh or relaxed episode appears in
  training gains a stricter comparison of each episode's table of marker,
  item and value.

Rulings checked against: `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`
on branch `rulings-2026-10-06-gate-a-v4`, including follow-up item 7 (the two
refinements, "yes, stricter, go with the recommendation") and item 8 (training
to leave those pairings out outright; built separately on branch
`training-exclusion-pairing`, so not checked here).

## The five checks, and what passes

1. **Order and untouched originals.** Pass if the cases-and-expectations
   commit is an ancestor of the code-and-outputs commit, the code commit does
   not touch the case file or the method note, and the cases commit only
   appends (no deleted or changed line in the 22 original cases, their
   expectations or the original method text).
2. **Each rule turned off in turn, now with 25 cases.** Three ways:
   (a) the earlier check's own script (pull request 107, `recompute.py`),
   copied unchanged, run once per rule switch; (b) my own recompute, with
   finer switches than the earlier script (nomination and description-only
   separately, the step 5a rule, the "no step record" reading, the two-seed
   count, the separation bar); (c) the decision code itself, in a scratch
   copy, with the fresh-episode floor and then the development-episode floor
   switched off, rerun through the case runner. Pass if switching off the
   fresh floor changes case 23 or 25 and switching off the development floor
   changes case 24, in all three. Any rule whose removal changes no case is
   reported as a gap.
3. **Cases 23 to 25 recomputed from the ruling text** with my own code that
   imports neither `measure.py` nor `procedure.py` (only the case file, for
   the edits to the toy records). Pass if my outcome equals the written
   expectation and the code's committed outcome.
4. **The R3 sentences of cases 1, 3, 21 and 22.** For each, compute from the
   case's records (the gate counts against the bar) which condition fails on
   which seeds, and compare with the condition and seeds the sentence names.
   Pass if they match exactly (no seed missing, none extra).
5. **R2's scope phrase and the stricter self-test.** R2: pass if the sentence
   carries "on these constructed systems, for this intervention procedure"
   in the same sentence, as item 7 says. Self-test: rerun it; confirm by a
   planted example that it catches a training episode with the same table
   and a different turn order (which the whole-content check misses); and
   measure whether it could catch anything by chance at this sample size
   (rerun with the training exclusion switched off). It is not expected to
   be a guarantee, since item 8 replaces it with an outright exclusion; the
   check is only that it does what its text says.

Also: rerun the case runner from this clean worktree and compare with the
committed outputs byte for byte; rerun all self-tests.

Scripts and outputs go in `2026-10-06-a2-additions-check-scripts/` beside
this file. Findings are added below this method in a later commit.
