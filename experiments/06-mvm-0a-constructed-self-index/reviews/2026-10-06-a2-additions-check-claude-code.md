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

---

## Findings

*Added after the checks ran, in a second commit. Outputs in
`2026-10-06-a2-additions-check-scripts/`.*

### Verdict: pass

All five checks pass. The three new cases land where the ruling text says,
in my own recompute, in the earlier check's script and in the decision code.
Switching off the fresh-episode floor now changes cases 23 and 25, and
switching off the development-episode floor changes case 24, in all three.
The R3 sentences name exactly the conditions and seeds that fail in the
records. R2 carries the scope phrase as ruled. The stricter self-test does
what its text says. Nothing below blocks merging pull request 105. The one
medium point is about the self-test, which the training-exclusion ruling
(item 8) already replaces.

| # | Check | Result |
|---|---|---|
| 1 | Order, originals untouched | **Pass** |
| 2 | Each rule off in turn, 25 cases, three ways | **Pass** for both floors; no real gap (see problem 2) |
| 3 | Cases 23 to 25 recomputed independently | **Pass**, 3 of 3 (and 25 of 25 overall) |
| 4 | R3 sentences of cases 1, 3, 21, 22 | **Pass**, exact match |
| 5 | R2 scope phrase; stricter self-test | **Pass**; the self-test has almost no power to find anything (problem 1) |

### 1. Order and untouched originals (`history.txt`)

- The cases commit (`400c265`, 10:24:12) is the direct child of the earlier
  outputs commit and an ancestor of the code commit (`d776c70`, 10:25:25).
- The cases commit changes only the method note and the case file, and
  removes no line from either: the 22 original cases, their expectations
  and the original method text are unchanged. The code commit touches
  neither file. The case file is also unchanged from the first method commit
  (`590a630`) to the earlier outputs.
- The code commit's only change to the case runner adds a check of the new
  expectations on existing cases (`ADDENDUM_EXPECT`); it changes no original
  check.
- Rerunning the case runner and then the self-tests in this clean worktree
  reproduces every committed output byte for byte. All self-tests pass
  (`self-tests.txt`).
- Git can prove order, not timing: 73 seconds separate the two commits.

### 2. Each rule turned off in turn

**(a) The earlier check's script, unchanged** (`earlier_check_recompute.py`,
SHA-256 `526d4cbf…e6cae90d`, copied from pull request 107;
`earlier_check_sweep.txt`): 25 of 25 agree with the written expectations.
Fresh floor off: case 23 goes to R1 and case 25 goes to R1. Development
floor off: case 24 goes to R1. Every other switch changes the same cases as
in the earlier re-check.

**(b) My own recompute** (`my_recompute.py`, `my_recompute_sweep.txt`), with
finer switches:

| Rule turned off | Cases that change |
|---|---|
| control 7 | 6 and 7 |
| control 1 on arm T | 8 and 9 |
| control 4 | 18 |
| **fresh-episode floor** | **23 (to R1), 25 (to R1)** |
| **development-episode floor** | **24 (to R1)** |
| nomination alone | none |
| description-only alone | none |
| "no reading computed" alone | none |
| nomination and description-only together | 7 |
| learning gate, own-directed | 21 |
| learning gate, named-other | 1, 3, 12 |
| channel-removal collapse | 12, 20 |
| ownership-free line | 17 |
| seed rule (back to separate counts) | 12 |
| step 5a rule (stop S4) | 3 |
| "no step record means R3" reading | 1 |
| separation bar | 5 |

**(c) The decision code itself**, in a scratch copy (`code_mutation.txt`,
with the one-line edit shown): with the fresh-episode floor forced to pass,
the runner reports cases 23 and 25 wrong, and the withheld figures appear in
the outputs. With the development-episode floor forced to pass, it reports
case 24 wrong, and also case 13 ("overlap-one-seed"), whose listed reasons
lose "development episodes".

### 3. Cases 23 to 25 recomputed from the ruling text

`my_recompute.py` imports only the case file. Its rules: page 7 (a seed
counts only if it passes its own gate conditions and every withholding check;
an arm passes, or reads, on two such seeds); page 1 (named-other learning
and the channel-removal check on arm F only, line 1,546 of 3,000); page 8
(the no-transplant rate withholds nothing); pages 5 and 9 (the outcome table
and its order).

- **Case 23**, arm C seeds 0 and 1 fail the fresh floor. Arm C counts only
  seed 2, so it has no verdict. Arm T reads; arm F learns and reads on all
  three seeds. Result: **"metric checked against the separable model only,
  degree read"**. This matches the expectation and the code.
- **Case 24**, arm T seeds 0 and 1 fail the development floor. Every gate
  passes, and arm T counts only seed 2, so it has no verdict. Result:
  **"metric not validated"**. This matches.
- **Case 25**, arm F seeds 0 and 1 fail the fresh floor. Arm F passes its
  gate on all three seeds, so its step 5a seed (0) passed and no R3 follows.
  Arms T and C read and separate (C's lowest about 0.99, T's highest 0). Arm
  F counts only seed 2. Result: **the fifth term, "metric validated, degree
  not read"**. This matches.

### 4. The R3 sentences

From each case's records (the gate counts against the bar of 790 correct
out of 3,000):

| Case | Fails in the records | Sentence names | Match |
|---|---|---|---|
| 1, the toy | arm F named-other on seeds 1 (781) and 2 (746) | arm F, named-other condition, seeds 1 and 2 | yes |
| 3, toy with seed 1 as step 5a | the step 5a seed, 1: named-other (781) | arm F, at step 5a, named-other condition, seed 1 | yes |
| 21, arm T fails its gate | arm T own-directed on seeds 0 and 1 | arm T, own-directed condition, seeds 0 and 1 | yes |
| 22, arm F fails at step 5a | seed 1: named-other (781) | arm F, at step 5a, named-other condition, seed 1 | yes |

In case 3, arm F's seed 2 also fails named-other, but the step 5a rule is
about the one step 5a run, so naming seed 1 alone is right.

### 5. R2's scope phrase and the stricter self-test

**R2.** The reported sentence reads "metric does not separate on these
constructed systems, for this intervention procedure", in one sentence, as
item 7 of the follow-up rulings says. The table's bare "outcome:" line keeps
the registered term without the phrase and the "as reported:" line carries
it, which is how every other term is laid out. The code's own self-test now
checks it.

**The stricter self-test** (`control5_probe.py`, `control5_probe.txt`).
It builds each fresh and relaxed episode's table of which marker holds which
value on which item, and asserts that none appears among 9,600 training
tables from 200 steps of run seed 0. That is exactly what its text says.
- It catches what the whole-content test misses. A planted copy of a fresh
  episode with the agents reordered, the turns reversed and a different
  named agent has the same table and different whole content.
- "Pairing" can only mean the whole table. All 480 possible single (marker,
  item, value) triples occur within the 200 sampled steps, so a
  single-triple reading would fail at once, and excluding by it would empty
  training.
- See problem 1 for what the test cannot show.

## Problems, ranked by severity

1. **Medium, already addressed by ruling item 8: the stricter self-test
   cannot fail by chance at this sample size, so its pass is no evidence
   about the registered claim.**
   - With the training exclusion switched off entirely, 200 steps still
     share no table with the fresh or relaxed sets, on run seeds 0, 1 and 2.
   - About 14 billion tables are possible, so the expected number of chance
     matches in the sample is 0.0005.
   - By contrast, one full run's stream (108,919 steps of 48 contents, the
     default token budget) is expected to hold 0.30 fresh tables: a 26%
     chance of at least one. Over the three seeds' streams it is 0.90, a 59%
     chance. Whole-content exclusion does not block these.
   - The 800 relaxed tables can never match, because each has two agents on
     one value and training never draws that, so half the comparison is
     empty by construction.
   - The test's wording ("in 200 sampled training steps", "sampled, not
     guaranteed") is honest. This is the brief's expectation, now with
     numbers. **For the training-exclusion-pairing branch:** the outright
     exclusion is needed, not just tidier. Its self-test should plant a
     same-table, different-content episode and show the stream skips it,
     rather than rely on a sample.
2. **Low: three withholding checks are never exercised alone.** Switching
   off nomination, description-only, or "no reading computed" changes no
   case on its own; nomination and description-only together change case 7.
   In the real pipeline these fire together: `procedure.py` marks a reading
   description-only exactly when nomination fails. A case that separates
   them would describe a record the pipeline cannot write. This is not a
   real gap, but a reader of the earlier check's single "piece floor" switch
   should know it covers two rules.
3. **Low: the runner's new expectations do not pin the seed numbers in R3
   sentences.** They check "arm F" and "named-other condition" but not
   "seeds 1 and 2". The seeds are right (check 4), but the runner alone
   would not catch a wrong seed.
4. **Low, not exercised: the R3 wording does not tell a missing measurement
   from a failure.** The new code groups every learning check that did not
   pass, including one never run, under the condition's name. A seed with
   no gate count would read "own-directed condition, on seed 0" without
   "not run". The seed's own reasons do say "not run", and no case has a
   missing gate count.
5. **Low: the floor outcomes do not name the arm or seeds.** Case 24 reads
   "metric not validated: floor on development episodes failed" and case 25
   "…degree not read: floor on fresh episodes failed". R3 now names arm,
   condition and seeds, and these do not. The ruling does not require it.
   Each seed's listed reasons carry it.
6. **Low, housekeeping:**
   - The code commit deletes the output folder's ignore file and commits
     291 per-case record files (about 21 MB) without mentioning it.
   - Running the case runner on its own deletes the committed
     `self-tests.txt`, because it wipes the output folder. "Byte for byte"
     holds only after the self-tests are rerun too.

For information: the earlier checker re-checked the same head on the pull
request 107 branch (commit `1f519cc`) and reached the same results. This
check was done separately, with its own recompute and the code-level switch
test, and agrees.

## Files

All in `2026-10-06-a2-additions-check-scripts/`:
- `history.txt`: check 1.
- `earlier_check_recompute.py` and `earlier_check_sweep.txt`: check 2(a).
- `my_recompute.py`, `my_recompute_sweep.txt` and `my_recompute_base.json`:
  checks 2(b), 3 and 4.
- `code_mutation.txt`: check 2(c).
- `control5_probe.py` and `control5_probe.txt`: check 5.
- `self-tests.txt`: the self-test rerun.
