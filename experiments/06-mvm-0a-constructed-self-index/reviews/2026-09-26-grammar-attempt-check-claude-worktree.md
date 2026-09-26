# Check of the grammar attempt — re-run from the committed code, and the ruling read against it

*Written 2026-09-26 (Pacific) by the Claude Code session "MVM W1c grammar
attempt check", on branch `worktree-w1c-grammar-check`, cut from main at
`c17dbdc` (after pull requests 52, 58 and 56 had merged;
`docs/2026-09-26-rehearsal-repairs.md` is on main at that commit).*

*This session did not write what it checks. The target is branch
`worktree-w1c-grammar-attempt` at commit `ba42732` (pull request 57), the
attempt at redesign (c) — a grammar change meant to let the free arm learn the
named-other condition — written by the session "MVM W1c grammar attempt". Its
method note is `docs/grammar-attempt-method-2026-09-25.md`, its findings
`docs/2026-09-26-grammar-attempt.md`, and its outputs
`experiments/rehearsal-successor-measure/out-grammar-c/`, all on that branch and
none on main. Every path below that starts `out-grammar-c/` means that folder at
`ba42732` unless it says "re-run". Nothing on branch
`worktree-w1c-grammar-attempt` was modified.*

*The pass line the attempt was run under is item 1 of
`docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` on pull request 53
(branch `rulings-2026-09-25-repairs`). The findings cite it at `e03288c`; the
branch now ends at `744f978`. The only change to that file between the two is
annotations appended after its check; item 1's wording is the same at both
(MEASURED, `git diff e03288c origin/rulings-2026-09-25-repairs -- docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`,
which adds lines only after line 93).*

*Every finding is labelled **MEASURED** (a command was run and its output is
printed here or in the appendix, with the file it rests on) or **ARGUED**
(reasoning a reader can dispute). Filed under this experiment's reviews
directory, beside the repairs check it copies the shape of. Nothing was rented,
no vendor was contacted, no network was used by the run, nothing was spent:
$0. Written under the workspace plain-language rule.*

## Verdict

- **The verdict reproduces: the pass line is not cleared, and fallback (d)
  registers.** MEASURED, section 3. On the re-run the free arm's named-other
  condition got **750, 809 and 739** correct of 3,000 on seeds 0, 1 and 2,
  against the findings' 774, 730 and 759. The line needs 790 or more on at
  least two seeds.
- **The count of seeds clearing does not reproduce: 1 of 3 on the re-run, not
  0 of 3.** MEASURED, section 3.3. Seed 1 reached 809. Under the 2026-09-23
  range-and-direction ruling the per-seed counts were never expected to repeat.
  But the findings' "0 of 3" and "this one on none" are facts about one
  training run. What the two runs together support: **at most one seed of three
  clears on either run**. That is the same one-in-three both earlier runs of
  the old grammar gave.
- **Own-directed not degraded: reproduces.** Mean 0.5652 on the re-run against
  0.5654 committed, both above the method's 0.5513. MEASURED, section 3.3.
- **Everything that does not depend on training the free or entangled arm
  reproduces exactly.** Every self-test check, the R-5 invariance file
  byte-for-byte, the name-only solver (0.238 and 1.000), and every arm T figure
  including the negative case at −0.1870. MEASURED, sections 3.2 and 3.3.
- **Commit order holds, and the code commit does what the method states.** The
  code adds nothing that changes a verdict. Two small gaps:
  the method's claim that its negative-case pool matches 2026-09-21 is wrong on
  the pool size (800 pairs here, 400 then), and two thresholds the method
  pre-states are defined in the driver but never used by it. MEASURED, section 1.
- **The carried-in driver is identical to main.** `repairs.py` and `training.py`
  (and `arm_middle.py`, `diagnose_named_other.py`) have the same content at
  `e0626b2`, on the branch, and on origin/main. MEASURED, section 2.
- **The diagnosis is ARGUED, resting on a MEASURED pattern.** The committed
  outputs measure *what* the free arm answers at the named-other turn. They do
  not measure *which step* fails. Section 4.
- **Three statements in the findings do not survive the re-run or the committed
  files.** MEASURED, section 5: "0 of 3" (1 of 3 on the re-run); arm C clearing
  named-other on 1 of 3 (0 of 3 on the re-run); "no nomination used an
  all-positions site set" (arm C seed 0 did on the re-run). One statement is
  wrong against the committed files themselves: the smallest "room" is 0.4300,
  not 0.4438. None of them changes a verdict.

---

## 0. Words used here, once

- **Arm**: one of the small trained models. **Arm T** is built so the answer to
  "whose value do I act on?" sits in a separate slot (built to be separable).
  **Arm C** is built so that answer is mixed into everything (built to be
  entangled). **Arm F**, the free arm, is trained with no such construction. The
  pass line is read on arm F.
- **Own-directed** and **named-other**: the two kinds of action turn. On one the
  model revises its own assigned value; on the other it revises the value of an
  agent named by a marker word.
- **Acting channel**: the extra input wire that tells the model "this turn is
  yours". The grammar change turns it off on the named-other action turn.
- **The bar**: 790 or more correct of 3,000 held-out episodes, i.e. above one
  in four at the 0.05 level (page 1b of `docs/rulings/2026-09-26-weekend-1-queue.md`).
- **Transplant, reading, site set, nomination, floor**: as in the repairs check
  (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-rehearsal-repairs-check-claude-worktree.md`,
  section 0). The reading is 0 when the "whose value" answer sits entirely in
  its own directions and 1 when it is spread through everything.
- **"Room"**: how much the whole-state transplant moves the action above the
  untouched rate. It is the reading's denominator.

---

## 1. The method precedes the output, and what the code commit changed

**Order, MEASURED** (`git log --format='%h %ad %s' --date=iso origin/main..origin/worktree-w1c-grammar-attempt`, oldest last):

```
ba42732 2026-09-25 23:01:12 -0700 Grammar attempt: the findings — the pass line was not cleared
53eac6d 2026-09-25 22:59:25 -0700 Grammar attempt: the outputs
94da045 2026-09-25 20:19:19 -0700 Grammar attempt: the setting in grammar.py and the driver (code only, no output)
aa85b5e 2026-09-25 20:16:52 -0700 Carry in the rehearsal-repairs driver from e0626b2 (PR 52), unchanged
271d57c 2026-09-25 20:16:45 -0700 Grammar attempt (redesign (c)): the method, before any code or output
```

What each commit touches (`git show --stat` on each), MEASURED:

| commit | files | any output? |
|---|---|---|
| `271d57c` method | `docs/grammar-attempt-method-2026-09-25.md` only | no |
| `aa85b5e` carried-in driver | `arm_middle.py`, `diagnose_named_other.py`, `repairs.py`, `training.py` | no |
| `94da045` code | `grammar.py`, `grammar_attempt.py` | no |
| `53eac6d` outputs | the 31 files of `out-grammar-c/` other than the two below | yes, first |
| `ba42732` findings | the findings, `failure-mode-run.sh`, `failure-mode-run.txt` | yes (the author's failure-list run) |

**The pass line and the setting are in the method, before any output.**
MEASURED, `docs/grammar-attempt-method-2026-09-25.md` at `271d57c`:

- the setting is section 2.2: the acting channel set to 0 on all seven tokens
  of the named-other action turn, nothing else changed, implemented as
  `NAMED_OTHER_ACTING` with default 1 and set to 0 by the new driver;
- the pass line is section 5: (a) 790 or more of 3,000 on at least two of the
  three free-arm seeds, on the repairs gate's 1,500 pairs (pool `dev`, seed 99);
  (b) the three-seed mean own-directed accuracy at or above 0.5513.

**Caveat, ARGUED.** The method says it was committed "before any code is
written". Git records commit order, not writing order. The 336 lines of code in
`94da045` were committed 2 minutes 34 seconds after the method. That points to
the code having been drafted before the method was committed. The protocol
requirement the task names, that the method precede any *output*, is met with
room to spare: the first output commit is 2 hours 40 minutes later. The
findings also say one import check of the driver ran before `94da045` and wrote
nothing (findings, section 1).

**Did the code commit change anything the method did not state?** MEASURED,
`git show 94da045`, read against the method:

| in the code | in the method? | effect |
|---|---|---|
| `grammar.py` line 232: `acting.extend([1 if cond == OWN else NAMED_OTHER_ACTING] * 7)` | yes, section 2.2 | the change itself, exactly as stated |
| `grammar.py` self-test additions: tokens unchanged, acting differs only on the seven positions `action_pos-5 … action_pos+1`, acting at scored positions 1 and 0 | yes, section 4, last paragraph | as stated |
| `grammar.py` `--named-other-acting` command-line flag for the self-test | no | runs the self-test under either setting; touches no data the run uses. Harmless. |
| driver sets `G.NAMED_OTHER_ACTING = 0` before importing `repairs`, `training`, `transplant`, `diagnose_named_other`, and asserts it in `main` | yes, section 2.2 | all of them `import grammar as G`, so they share the one setting |
| pass line: `other_correct >= R.GATE_MIN_CORRECT` (790) on ≥ 2 seeds, mean own ≥ `OWN_LEVEL = 0.5513`; read from `gate_base.json`, which `repairs.stage_gate` builds from `make_data(1500, seed=99, pool="dev")` (`repairs.py` line 122) | yes, section 5 | as stated |
| R-4 no-verdict case on `make_data(800, seed=777, pool="fresh")` | pool **not stated** | it is the pool the 2026-09-21 rehearsal used for the same case (`rehearse.py` lines 463 and 500), so it matches the method's "as the 2026-09-21 rehearsal used" |
| R-4 negative case on `make_data(800, seed=780, pool="unseen-vocabulary")` | yes, "800 pairs, seed 780 … as `negative_case.py` did on 2026-09-21" | the code follows the method's number, but **the method's precedent is wrong on size**: `negative_case.py` line 36 and `rehearse.py` line 325 both take **400** pairs from that pool. The method changed the pool size without saying so. No verdict rests on it: arm T's negative reading is found either way (section 3.3). |
| `R2_TOLERANCE = 0.1`, `HIGH_LINE = 0.5` (method section 6, R-2 and R-3) | yes | **defined and never used**; `git grep` finds each name only on its definition line. The R-2 and R-3 verdicts were applied by the author reading `measure_base_F_T_C.json`, not by code. The numbers clear both lines by a wide margin (0.0000 against 0.1; 0.99 or more against 0.5), so nothing turns on it. |
| R-6 check: scans `measure.py`, `repairs.reading`, `repairs.floor_check` for attributes accessed on the name `G` | yes, section 6 R-6 ("a command shows …") | the check is shallow: it sees only uses of the name `G`. It holds anyway. `measure.py` imports only `argparse` and `math` (lines 38–41), and `reading` calls only `dict` and `floor_check`, which calls only `bool` and `dict` (MEASURED, an `ast` walk of their calls, run in this session). |

So the code commit adds no step, threshold or data choice that could move the
verdict beyond what the method states. It adds one pool the method leaves
implicit, and it relies on a precedent the method misquotes.

---

## 2. The carried-in driver, against origin/main now that pull request 52 is merged

MEASURED:

```
$ git diff --stat origin/main origin/worktree-w1c-grammar-attempt -- experiments/rehearsal-successor-measure/src/
 .../rehearsal-successor-measure/src/grammar.py     |  47 +++-
 .../src/grammar_attempt.py                         | 290 +++++++++++++++++++++
 2 files changed, 336 insertions(+), 1 deletion(-)

$ git diff origin/main origin/worktree-w1c-grammar-attempt -- .../src/repairs.py .../src/training.py .../src/arm_middle.py .../src/diagnose_named_other.py
(no output)

$ git diff --stat e0626b2 aa85b5e -- (the same four files)
(no output)
```

The content identifiers on both sides: `repairs.py` `f6a41a8…` and `training.py`
`516ffb6…`, the same at `e0626b2`, on the branch, and on origin/main.
**No difference.** "From e0626b2 unchanged" is true, and it is also unchanged
from main as merged.

---

## 3. The re-run from clean

### 3.1 How it was run

`git archive ba42732` was unpacked into this session's scratch folder, outside
the repository. The committed `out-grammar-c/` was moved aside to
`out-grammar-c-committed/`, and every stage ran into an empty `out-grammar-c/`
from the committed code. No checkpoint was reused, since none is committed. The
order was the writer's, read from its committed `train-log.txt` and
`run-log.txt`: three training streams side by side (arm T, arm F, arm C, seeds
0 to 2 each), then gate, nominate, measure, summary, diagnose, outcomes,
passline, invariance, then the four module self-tests. The driver script is
appendix A. Same laptop, same Python environment
(`~/Code/minimum-viable-mind/.venv`, torch 2.12.1 on the Mac's graphics chip).
It started on battery at 80% and was on wall power by the end of training.

MEASURED, from the driver's log: started 2026-09-26 06:51:33, training done
07:59:36, everything done 08:20:42. Arms T and F finished all three seeds in
3,683 and 3,626 seconds per stream (`rerun-logs/train_T.log`, `train_F.log`),
against the writer's 6,970 for arm T. No stage printed an error or failed; the only
warning is a straight-line fit's "failed to converge" notice from scikit-learn
(`rerun-logs/run.log`). $0.

### 3.2 Per-file

MEASURED, `cmp` on each file present in both folders: **one output file is
byte-identical, `invariance.json`**. That is the file that depends only on
generated data, never on training. Every other file holds either elapsed
seconds or figures from arms whose training drifts.

The self-test record matches check for check: 73 passing lines in each, and
"all checks passed" four times in each. It includes the largest distance-bin
difference of 0.0098 and the mean distances of 5.010 and 4.928, and 14,000
acting positions differing over 2,000 episodes (`rerun-logs/self-tests.txt`
against `out-grammar-c/self-tests.txt`). The only differences are how the
command lines are printed and one PyTorch warning that leaked past the filter.

Arm T's frozen straight-line reads differ from the committed ones by up to
0.05, 0.18 and 0.12 in some coefficient on seeds 0, 1 and 2 (largest over the
arrays in each `reads_T_base_seed*.npz`). Arm T's weights drift like every
arm's, and its outputs still come back exactly (section 3.3). This is the same
pattern, for the same reason, that the 2026-09-22 and 2026-09-25 re-runs
found.

### 3.3 The figures the brief names, and which must reproduce exactly

**What the 2026-09-23 ruling requires.** `docs/rulings/2026-09-23-range-and-direction-only.md`
rules that from the entangled and free arms (C and F) only a range and a
direction may be quoted, and no decimal as a property of the code. Arm T is
"unaffected" and reproduced exactly. So, ARGUED from that ruling:

- **must reproduce exactly**: anything computed without training arm C or F.
  That is the self-tests; the R-5 invariance (generated data); the name-only
  solver (computed from the episode's values); every arm T figure (by the
  ruling's own section 5 and two re-run precedents); and the R-6 code check.
- **need only reproduce in direction**: every figure from arms F and C. That
  includes the pass line's counts 774, 730, 759 and the own-directed mean,
  whose direction is "at or above 0.5513". It also includes arm C's gate counts,
  the diagnostic shares, and every nomination and reading on arms C and F.
  **The direction of the pass line is its verdict**: fewer than two seeds
  clearing, own-directed not degraded, so not cleared.

**The pass line** (`gate_base.json`, `passline.json`; bar 790 of 3,000). MEASURED:

| free arm | committed: named-other correct | re-run: named-other correct | committed: own-directed | re-run: own-directed |
|---|---|---|---|---|
| seed 0 | 774 | 750 | 0.5733 | 0.5687 |
| seed 1 | 730 | **809** (clears) | 0.5553 | 0.5550 |
| seed 2 | 759 | 739 | 0.5677 | 0.5720 |
| seeds clearing | **0 of 3** | **1 of 3** | mean 0.5654 | mean 0.5652 |
| (a) ≥ 2 of 3 | not met | not met | — | — |
| (b) mean ≥ 0.5513 | — | — | met | met |
| **cleared?** | **no** | **no** | | |

| figure the brief names | must be | verdict |
|---|---|---|
| 774, 730, 759 of 3,000 | direction | **not exactly**, as expected; the re-run is 739 to 809 |
| against the 790 bar | — | the bar is a constant in the code (`repairs.py` line 51); same |
| 0 of 3 clearing | direction | **does not reproduce as a count**: 1 of 3. Its direction does: fewer than two, so (a) is not met on either run |
| own-directed not degraded | direction | **reproduces**: 0.5652 against 0.5654, both above 0.5513 |
| not cleared | direction | **reproduces** |

**Everything else the findings rest on**, MEASURED (the full extraction for both
folders is appendices C and D):

| figure | committed | re-run | must be | verdict |
|---|---|---|---|---|
| arm T gate, both conditions, 3 seeds | 1.0000 | 1.0000 | exact | **exactly** |
| arm T lesion own-directed | 0.2467 / 0.2510 / 0.2733 | the same | exact | **exactly** |
| arm F lesion own-directed | 0.2120 / 0.2063 / 0.2110 | 0.2113 / 0.2113 / 0.2020 | direction | reproduces (0.20 to 0.21) |
| arm C own-directed, seed 0 | 0.7993 | **0.9997** | direction | seed 0 is again the high one; higher still |
| arm C named-other, seeds clearing | 1 of 3 (794 on seed 0) | **0 of 3** (778 / 730 / 725) | direction | count moves; "at most one" holds |
| R-2: arm T nomination and reading | layer 0, action, rank 8; 0.0000 all seeds | the same | exact | **exactly** |
| R-3: arm C reading at its nomination | 0.9863 to 1.0028 | 0.9975 to 1.0085 | direction | reproduces: clears the floor, ≥ 0.5 on every seed |
| R-3: arm C nomination uses an all-positions site set | none | **seed 0: layer 0, all positions, rank 2** | direction | **does not reproduce** (section 5). The reading without it is 1.0000 (layer 4, action, rank 1), so R-3 still holds |
| R-4 no verdict: arm T, first layer before identity, rank 2 | whole 0.0000, no verdict | the same | exact | **exactly** |
| R-4 negative: arm T seed 0 on unseen vocabulary | whole 0.7588, ownership-only 0.8850, −0.1870 | the same | exact | **exactly** |
| R-5: zeroed batches identical, old vs new grammar | yes on all four sets; 210,000 and 21,000 acting positions differ before zeroing | the same; file byte-identical | exact | **exactly** |
| R-5: name-only solver | 0.238 / 1.000 | 0.238 / 1.000 | exact | **exactly** |
| R-6: grammar attributes used by the arithmetic | none | none | exact | **exactly** |
| separation C − T, per seed | 0.99 to 1.00, all clear 0.5 | 0.9975 / 1.0000 / 1.0085, all clear 0.5 | direction | reproduces |
| control 2 full procedure | no verdict on 8 of 9, pass on arm C seed 1 | the same | direction | reproduces |
| control 6 cells | 81 and 719 trials | 81 and 719 | exact (generated data) | **exactly** |
| diagnostic: own value at the named-other turn | 0.054 / 0.049 / 0.064 | 0.063 / 0.051 / 0.074 | direction | reproduces (about one in twenty) |
| diagnostic: named as a share of the three non-own values | 0.340 / 0.314 / 0.334 | 0.333 / 0.337 / 0.326 | direction | reproduces (about one in three) |

**Does the re-run bear on the findings' comparison with the old grammar?**
ARGUED. The findings say the two earlier old-grammar runs "cleared the bar on
one seed; this one on none. The change did not move the condition up." On the
re-run the new grammar also clears on one seed. Across the four runs now on
record, old grammar 1 and 1 and new grammar 0 and 1, **the change did not move
the condition up**. That conclusion survives. "This one on none" does not.

---

## 4. The diagnosis: MEASURED or ARGUED?

The findings' diagnosis: the model tells the two turns apart but fails to match
the named marker word to that agent's value (findings, sections 0 and 3). The
findings themselves label it "MEASURED for the numbers; ARGUED for the
reading". This check agrees, and splits the two halves.

**What the committed outputs measure.** MEASURED,
`out-grammar-c/diagnose_named_other.json`, confirmed in direction by the re-run.
At the named-other position the free arm answers:

- the named agent's value: 0.24 to 0.26;
- its **own** value: 0.05 to 0.06 (re-run 0.05 to 0.07);
- one of the item's two remaining agents' values: 0.50 to 0.53;
- a value not in the item: 0.18 to 0.19 (re-run 0.15 to 0.19).

Arithmetic on the same file, MEASURED (appendix C): among the three agents'
values that are not its own, the named agent's gets **0.31 to 0.34** of the
answers (re-run 0.33 to 0.34). That is one in three, which is **chance among
those three**.

**"It tells the two turns apart": ARGUED, one short step from a MEASURED
pattern.** A model that treated the named-other turn like the own-directed one
would give its own value there at about its own-directed accuracy, 0.56 to 0.57
(`gate_base.json`). It gives its own value about one time in twenty. So its
answer does depend on which kind of turn it is. The method frames this against
"one in four", the rate for picking uniformly among the item's four values. The
comparison with its own-directed rate is the stronger one, and points the same
way. Neither comparison says *how* it tells them apart; in both grammars the
`<who>` word differs between the turns, so the turns differ in their tokens
anyway (method, section 2.1).

**"It fails to match the named marker to that agent's value": ARGUED.** What is
measured is the outcome: chance among the three candidates. Nothing committed
separates the steps that could produce that outcome. The model might not read
the named marker word at all. It might read it but fail to find that agent's
assignment turn. Or it might find the turn and fail to copy the value. All
three give chance among the three. No committed output isolates any one of
them. The nearest committed output, control 2's named-agent nomination
(`nominate_base_F_T_C.json`, "no verdict" on every free-arm seed), is
consistent with the diagnosis but is not a test of it: it returns no verdict
precisely because the arm has not learned the condition.

**"Taking away the shared signal removed something the model was not using at
that turn": ARGUED** (findings, section 3). It rests on a comparison across runs
of a drifting arm. The re-run is consistent with it (section 3.3) but does not
test it.

---

## 5. The consequence: fallback (d) registers

**It follows from the ruling's item 1 wording.** The ruling, item 1, at both
`e03288c` and `744f978`: "the named-other condition above the page 1b bar on at
least two seeds of three on the free toy arm, with the own-directed condition
not degraded below its current level. If it clears, version 2 is amended before
its Gate A with the grammar change … if it does not, (d) is what registers."

- Both halves are joined by "with", so clearing needs both. Part (a) fails on
  the committed run (0 of 3) and on the re-run (1 of 3). MEASURED, section 3.3.
- The result does not depend on how "above the page 1b bar" is read. Page 1b
  gives the bar as 0.2630 of 3,000, which is 789 correct. The method and the
  code use 790, from the binomial test. The committed run's best seed is 774,
  under either reading. The re-run's 809 clears under either, and is still one
  seed. MEASURED, `docs/rulings/2026-09-26-weekend-1-queue.md` lines 37–39 and
  `repairs.py` line 51.
- The own-directed half's exact form (a three-seed mean against the lowest
  earlier seed, 0.5513) is the method's own choice, which the method labels
  ARGUED. Since (a) fails, no reading of (b) changes the verdict. ARGUED.
- **So "fallback (d) registers" is what the ruling says follows.** It is also
  what the ruling's first sentence already records as standing for version 2.
  The attempt was the one route by which version 2 would have been amended
  instead. ARGUED from the ruling's wording.

One point of process, ARGUED: the ruling is on pull request 53, not yet merged.
The consequence follows from its words as recorded. Nothing here depends on
the merge, but the findings' citation of it by commit `e03288c` is now one
commit behind the branch.

---

## 6. Other things found against the committed files

1. **The findings' smallest "room" is wrong.** Findings, section 5, failure 1:
   "every one of the nine arm-and-seed pairs has room between 0.4438 and
   1.0000". The writer's own `out-grammar-c/failure-mode-run.txt`, line 5,
   prints **F/base/0: room 0.4300**; 0.4438 is the smallest on arm C only.
   MEASURED. Every pair still clears its floor, so nothing turns on it. On the
   re-run the smallest room is 0.3975 (free arm, seeds 1 and 2, against required
   0.391 and 0.394), which is a narrow margin and still clears. MEASURED,
   appendix D.
2. **"No nomination used an all-positions site set" is a property of one run.**
   Findings, section 4, R-3. On the re-run arm C seed 0 was nominated at layer
   0, all positions, rank 2, exactly the kind of set the 2026-09-25 ruling's
   item 3 excludes. MEASURED, appendix D. The repairs check found the same
   pattern on its re-run, with the pick moving to a different arm and seed
   (that file, section 5.1). The exclusion is already ruled, and the reading
   without it (1.0000) keeps R-3 at HOLDS. ARGUED.
3. **R-1's "arm C named-other 1 of 3" is a property of one run.** The re-run
   gives 0 of 3. R-1 is FAILS either way. MEASURED, section 3.3.
4. **The method's negative-case pool size and its unused thresholds.** Section 1.
   MEASURED.

The findings' figures quoted from the earlier records all match those files as
merged on main: the free arm's own-directed 0.5633 / 0.5563 / 0.5890
(`out/gate.json`) and 0.5597 / 0.5513 / 0.5547 (`out-repairs/gate_base.json`),
its named-other ranges 0.24 to 0.27 and 0.25 to 0.33, and every cell of the
old-grammar diagnostic row (`out-repairs/diagnose_named_other.json`). MEASURED,
appendix E.

---

## 7. What was opened, what was not

**Opened:** on branch `worktree-w1c-grammar-attempt` at `ba42732`, the method
note, the findings, `grammar.py` (the diff), `grammar_attempt.py`,
`diagnose_named_other.py`, the relevant parts of `repairs.py` and `training.py`,
and every file in `out-grammar-c/` through the extraction script. Also the
ruling on branch `rulings-2026-09-25-repairs` (item 1, and the diff between
`e03288c` and `744f978`), `docs/rulings/2026-09-23-range-and-direction-only.md`,
page 1b and page 4 of `docs/rulings/2026-09-26-weekend-1-queue.md`, and, on
main, `out/gate.json`, `out-repairs/gate_base.json`,
`out-repairs/diagnose_named_other.json`, `rehearse.py` and `negative_case.py`
(the pool lines only). **Not opened:** the writer's working folder and
checkpoints; the successor proposal; `docs/known-failure-modes.md` beyond what
the findings quote. No failure-mode pass is run here beyond what sections 1, 3
and 6 cover. The findings' own run of the list was checked only on failure 1
(section 6).

**The repository's own checks on this file.** MEASURED,
`scripts/check_citations.py --scope nocopies --only <this file>`: 19 references
to files not on main. Every one is a file on pull request 57's branch (the
method, the findings, `grammar_attempt.py`, `out-grammar-c/`,
`failure-mode-run.sh`), the ruling on pull request 53's branch, or this
session's scratch scripts and folders (`run_all.sh`, `extract.py`,
`out-grammar-c-committed/`), whose text is in the appendix. 0 exact figures
absent from the file their sentence cites. 10 approximate matches to look at,
all four-decimal or two-decimal roundings of figures the JSON files hold to
more places. `scripts/check_single_source.py --scope nocopies --only <this file>`:
0 confident findings; 1 money figure without a ledger source, the session's own
$0.

---

## Appendix

### A. The driver that ran the re-run (`run_all.sh`)

```sh
#!/bin/sh
# From-clean re-run of the grammar attempt at ba42732, in a scratch copy made by
# `git archive ba42732`. Local, laptop, no network, $0. The committed outputs
# were moved aside to out-grammar-c-committed/ before this ran; every stage
# writes into an empty out-grammar-c/. Order is the writer's, read from its
# committed train-log.txt and run-log.txt: three training streams side by side
# (arm T, arm F, arm C), then gate, nominate, measure, summary, diagnose,
# outcomes, passline, invariance, then the self-tests.
set -u
cd "$(dirname "$0")/experiments/rehearsal-successor-measure/src" || exit 1
PY=/Users/john/Code/minimum-viable-mind/.venv/bin/python
L=../rerun-logs
mkdir -p "$L"
echo "started $(date '+%F %T')"
for a in T F C; do
  $PY grammar_attempt.py --stage train --arms $a > "$L/train_$a.log" 2>&1 &
done
wait
echo "training done $(date '+%F %T')"
for s in gate nominate measure summary diagnose outcomes passline invariance; do
  $PY grammar_attempt.py --stage $s >> "$L/run.log" 2>&1 || echo "STAGE $s FAILED"
done
{
  echo '$ grammar.py --self-test --named-other-acting 0'; $PY grammar.py --self-test --named-other-acting 0
  echo '$ grammar.py --self-test'; $PY grammar.py --self-test
  echo '$ arms.py --self-test'; $PY arms.py --self-test
  echo '$ measure.py --self-test'; $PY measure.py --self-test
} > "$L/self-tests.txt" 2>&1
echo "everything done $(date '+%F %T')"
```

Run as `caffeinate -i run_all.sh`. Its log:

```
started 2026-09-26 06:51:33
training done 2026-09-26 07:59:36
everything done 2026-09-26 08:20:42
```

The re-run's pass-line stage printed:

```
    named-other correct [750, 809, 739] -> 1 of 3 seeds at 790 or more: (a) False
    own-directed mean 0.5652 vs 0.5513: (b) True
    PASS LINE CLEARED: False
```

### B. The extraction script (`extract.py`)

```python
# Prints every figure the check covers, from one out-grammar-c folder. Reads files only.
import json, os, sys

d = sys.argv[1]
J = lambda f: json.load(open(os.path.join(d, f)))

print("== gate_base.json (bar", J("gate_base.json")["bar"], ")")
for k, r in J("gate_base.json")["runs"].items():
    print(f"  {k}: own {r['own']:.4f} ({r['own_correct']})  named-other {r['other']:.4f} "
          f"({r['other_correct']})  clears own {r['own_clears']} other {r['other_clears']}  "
          f"lesion own {r.get('lesion', {}).get('own', float('nan')):.4f}")

p = J("passline.json")
print("== passline.json")
print("  named-other correct", p["named_other_correct"], "seeds clearing",
      p["named_other_seeds_clearing"], "(a)", p["a_named_other_clears"])
print(f"  own-directed {p['own_directed']} mean {p['own_directed_mean']:.4f} vs "
      f"{p['own_level']} (b) {p['b_own_directed_not_below']}  CLEARED {p['cleared']}")

print("== diagnose_named_other.json")
for k, v in J("diagnose_named_other.json").items():
    three = v["named"] + v["other_in_item"]
    print(f"  {k}: " + "  ".join(f"{a} {b:.4f}" for a, b in v.items())
          + f"   named as share of the three non-own values {v['named'] / three:.4f}")

print("== nominate_base_F_T_C.json (nominations)")
n = J("nominate_base_F_T_C.json")["arms"]
for k, v in n.items():
    s_ = v["ownership"]["nomination"]
    print(f"  {k}: {None if s_ is None else (s_['layers'], s_['positions'], s_['rank'])}"
          f"  control 2 {v['control2_named_agent'].get('status', '') if isinstance(v['control2_named_agent'], dict) else v['control2_named_agent']}")

print("== measure_base_F_T_C.json (readings at the nomination)")
m = J("measure_base_F_T_C.json")["arms"]
for k, v in m.items():
    r = v["reading"]; ss = v["site_set"]; sw = v["sensitivity_without_all_positions"]
    deg = "None" if r["degree"] is None else f"{r['degree']:.4f}"
    print(f"  {k}: site ({ss['layers']}, {ss['positions']}, rank {ss['rank']}) untouched "
          f"{r['accuracy_untouched']:.4f} whole {r['accuracy_whole']:.4f} ownership-only "
          f"{r['accuracy_ownership_only']:.4f} -> {r['status']} {deg}; floor {r['floor']}; "
          f"same site set without all-positions: {sw['site_set'] == ss}")
    c = v["controls"]
    print(f"      control 6 cells: same-value {c['6a same-value cell: trials']}, "
          f"different-value {c['6b different-value cell: trials']}; control 2 "
          f"{ {kk: (vv.get('status') if isinstance(vv, dict) else vv) for kk, vv in v['control2'].items()} }")

o = J("outcomes.json")
print("== outcomes.json")
for k, v in o["no_verdict"].items():
    print(f"  no verdict {k}: whole {v['reading']['accuracy_whole']:.4f} -> "
          f"{v['reading']['status']}")
for k, v in o["negative_at_nomination"].items():
    r = v.get("reading")
    print(f"  unseen vocabulary {k}: " + (v.get("status", "") if r is None else
          f"whole {r['accuracy_whole']:.4f} ownership-only {r['accuracy_ownership_only']:.4f}"
          f" -> {r['status']} degree {r['degree']}"))
print("  negative search", o["negative_search"])

s = J("summary_base.json")
print("== summary_base.json separation", json.dumps(s.get("separation_C_minus_T", s.get("separation")),
                                                   default=str)[:400])

inv = J("invariance.json")
print("== invariance.json")
for k, v in inv["R-5"]["blind_solver_inputs"].items():
    print(f"  R-5 {k}: identical {v['zeroed_batches_identical']}, acting differs "
          f"{v['acting_positions_differing_before_zeroing']}")
print("  R-5 name-only", inv["R-5"]["name_only_solver_recomputed"])
print("  R-6", inv["R-6"])
```

### C. `extract.py` on the committed folder (`out-grammar-c/` at `ba42732`)

```
== gate_base.json (bar {'as_a_share': 0.2633333333333333, 'episodes': 3000, 'min_correct': 790} )
  C/base/0: own 0.7993 (2398)  named-other 0.2647 (794)  clears own True other True  lesion own nan
  C/base/1: own 0.5703 (1711)  named-other 0.2440 (732)  clears own True other False  lesion own nan
  C/base/2: own 0.5583 (1675)  named-other 0.2350 (705)  clears own True other False  lesion own nan
  F/base/0: own 0.5733 (1720)  named-other 0.2580 (774)  clears own True other False  lesion own nan
  F/base/1: own 0.5553 (1666)  named-other 0.2433 (730)  clears own True other False  lesion own nan
  F/base/2: own 0.5677 (1703)  named-other 0.2530 (759)  clears own True other False  lesion own nan
  T/base/0: own 1.0000 (3000)  named-other 1.0000 (3000)  clears own True other True  lesion own nan
  T/base/1: own 1.0000 (3000)  named-other 1.0000 (3000)  clears own True other True  lesion own nan
  T/base/2: own 1.0000 (3000)  named-other 1.0000 (3000)  clears own True other True  lesion own nan
== passline.json
  named-other correct [774, 730, 759] seeds clearing 0 (a) False
  own-directed [0.5733333333333334, 0.5553333333333333, 0.5676666666666667] mean 0.5654 vs 0.5513 (b) True  CLEARED False
== diagnose_named_other.json
  F/base/0: named 0.2580  not_in_item 0.1857  other_in_item 0.5020  own 0.0543   named as share of the three non-own values 0.3395
  F/base/1: named 0.2433  not_in_item 0.1763  other_in_item 0.5310  own 0.0493   named as share of the three non-own values 0.3142
  F/base/2: named 0.2530  not_in_item 0.1797  other_in_item 0.5037  own 0.0637   named as share of the three non-own values 0.3344
== nominate_base_F_T_C.json (nominations)
  C/base/0: ([3], 'action', 4)  control 2 no verdict
  C/base/1: ([0], 'post-identity', 8)  control 2 nominated
  C/base/2: ([3], 'action', 1)  control 2 no verdict
  F/base/0: ([3], 'action', 1)  control 2 no verdict
  F/base/1: ([3], 'action', 8)  control 2 no verdict
  F/base/2: ([0], 'post-identity', 1)  control 2 no verdict
  T/base/0: ([0], 'action', 8)  control 2 no verdict
  T/base/1: ([0], 'action', 8)  control 2 no verdict
  T/base/2: ([0], 'action', 8)  control 2 no verdict
== measure_base_F_T_C.json (readings at the nomination)
  C/base/0: site ([3], action, rank 4) untouched 0.0300 whole 0.7300 ownership-only 0.0288 -> valid 1.0018; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.615, 'room': 0.7}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  C/base/1: site ([0], post-identity, rank 8) untouched 0.0475 whole 0.5038 ownership-only 0.0537 -> valid 0.9863; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.43100000000000005, 'room': 0.45625000000000004}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'pass'}
  C/base/2: site ([3], action, rank 1) untouched 0.0650 whole 0.5088 ownership-only 0.0638 -> valid 1.0028; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.386, 'room': 0.44375000000000003}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  F/base/0: site ([3], action, rank 1) untouched 0.0575 whole 0.4875 ownership-only 0.0575 -> valid 1.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.399, 'room': 0.43}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  F/base/1: site ([3], action, rank 8) untouched 0.0638 whole 0.5663 ownership-only 0.0638 -> valid 1.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.41700000000000004, 'room': 0.5025000000000001}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  F/base/2: site ([0], post-identity, rank 1) untouched 0.0663 whole 0.5138 ownership-only 0.0663 -> valid 1.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.40599999999999997, 'room': 0.4475}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  T/base/0: site ([0], action, rank 8) untouched 0.0000 whole 1.0000 ownership-only 1.0000 -> valid 0.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.8, 'room': 1.0}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  T/base/1: site ([0], action, rank 8) untouched 0.0000 whole 1.0000 ownership-only 1.0000 -> valid 0.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.8, 'room': 1.0}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  T/base/2: site ([0], action, rank 8) untouched 0.0000 whole 1.0000 ownership-only 1.0000 -> valid 0.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.8, 'room': 1.0}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
== outcomes.json
  no verdict T/base/0: whole 0.0000 -> no verdict
  no verdict T/base/1: whole 0.0000 -> no verdict
  no verdict T/base/2: whole 0.0000 -> no verdict
  unseen vocabulary C/base/0: whole 0.5625 ownership-only 0.0625 -> valid degree 1.0
  unseen vocabulary F/base/0: whole 0.4612 ownership-only 0.0688 -> no verdict degree None
  unseen vocabulary T/base/0: whole 0.7588 ownership-only 0.8850 -> negative degree -0.18703703703703697
  negative search {'found_at_nomination': ['T/base/0'], 'widened': False}
== summary_base.json separation {"0": {"C_minus_T": 1.0017857142857143, "clears_0_5": true}, "1": {"C_minus_T": 0.9863013698630136, "clears_0_5": true}, "2": {"C_minus_T": 1.0028169014084507, "clears_0_5": true}}
== invariance.json
  R-5 dev seed 99 (1500 pairs): identical True, acting differs 21000
  R-5 train seed 1000 (15000 pairs): identical True, acting differs 210000
  R-5 train seed 1001 (15000 pairs): identical True, acting differs 210000
  R-5 train seed 1002 (15000 pairs): identical True, acting differs 210000
  R-5 name-only {'n': 3000, 'other': 1.0, 'own': 0.238}
  R-6 {'grammar_attributes_used': {'floor_check': [], 'measure': [], 'reading': []}, 'reaches_rendering': False}
```

### D. `extract.py` on the re-run folder

```
== gate_base.json (bar {'as_a_share': 0.2633333333333333, 'episodes': 3000, 'min_correct': 790} )
  C/base/0: own 0.9997 (2999)  named-other 0.2593 (778)  clears own True other False  lesion own nan
  C/base/1: own 0.5583 (1675)  named-other 0.2433 (730)  clears own True other False  lesion own nan
  C/base/2: own 0.5710 (1713)  named-other 0.2417 (725)  clears own True other False  lesion own nan
  F/base/0: own 0.5687 (1706)  named-other 0.2500 (750)  clears own True other False  lesion own nan
  F/base/1: own 0.5550 (1665)  named-other 0.2697 (809)  clears own True other True  lesion own nan
  F/base/2: own 0.5720 (1716)  named-other 0.2463 (739)  clears own True other False  lesion own nan
  T/base/0: own 1.0000 (3000)  named-other 1.0000 (3000)  clears own True other True  lesion own nan
  T/base/1: own 1.0000 (3000)  named-other 1.0000 (3000)  clears own True other True  lesion own nan
  T/base/2: own 1.0000 (3000)  named-other 1.0000 (3000)  clears own True other True  lesion own nan
== passline.json
  named-other correct [750, 809, 739] seeds clearing 1 (a) False
  own-directed [0.5686666666666667, 0.555, 0.572] mean 0.5652 vs 0.5513 (b) True  CLEARED False
== diagnose_named_other.json
  F/base/0: named 0.2500  not_in_item 0.1860  other_in_item 0.5013  own 0.0627   named as share of the three non-own values 0.3327
  F/base/1: named 0.2697  not_in_item 0.1490  other_in_item 0.5307  own 0.0507   named as share of the three non-own values 0.3369
  F/base/2: named 0.2463  not_in_item 0.1713  other_in_item 0.5087  own 0.0737   named as share of the three non-own values 0.3263
== nominate_base_F_T_C.json (nominations)
  C/base/0: ([0], 'all', 2)  control 2 no verdict
  C/base/1: ([3], 'action', 1)  control 2 nominated
  C/base/2: ([0], 'post-identity', 1)  control 2 no verdict
  F/base/0: ([3], 'action', 1)  control 2 no verdict
  F/base/1: ([2], 'action', 1)  control 2 no verdict
  F/base/2: ([3], 'action', 1)  control 2 no verdict
  T/base/0: ([0], 'action', 8)  control 2 no verdict
  T/base/1: ([0], 'action', 8)  control 2 no verdict
  T/base/2: ([0], 'action', 8)  control 2 no verdict
== measure_base_F_T_C.json (readings at the nomination)
  C/base/0: site ([0], all, rank 2) untouched 0.0000 whole 1.0000 ownership-only 0.0025 -> valid 0.9975; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.8, 'room': 1.0}; same site set without all-positions: False
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  C/base/1: site ([3], action, rank 1) untouched 0.0575 whole 0.5600 ownership-only 0.0575 -> valid 1.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.391, 'room': 0.5025000000000001}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'pass'}
  C/base/2: site ([0], post-identity, rank 1) untouched 0.0612 whole 0.5050 ownership-only 0.0575 -> valid 1.0085; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.40199999999999997, 'room': 0.44375}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  F/base/0: site ([3], action, rank 1) untouched 0.0612 whole 0.5637 ownership-only 0.0612 -> valid 1.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.391, 'room': 0.5025}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  F/base/1: site ([2], action, rank 1) untouched 0.0712 whole 0.4688 ownership-only 0.0712 -> valid 1.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.39100000000000007, 'room': 0.3975}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  F/base/2: site ([3], action, rank 1) untouched 0.0688 whole 0.4662 ownership-only 0.0688 -> valid 1.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.3940000000000001, 'room': 0.39749999999999996}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  T/base/0: site ([0], action, rank 8) untouched 0.0000 whole 1.0000 ownership-only 1.0000 -> valid 0.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.8, 'room': 1.0}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  T/base/1: site ([0], action, rank 8) untouched 0.0000 whole 1.0000 ownership-only 1.0000 -> valid 0.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.8, 'room': 1.0}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
  T/base/2: site ([0], action, rank 8) untouched 0.0000 whole 1.0000 ownership-only 1.0000 -> valid 0.0000; floor {'clears': True, 'clears_plain_form': True, 'required_room': 0.8, 'room': 1.0}; same site set without all-positions: True
      control 6 cells: same-value 81, different-value 719; control 2 {'fixed-site variant': 'pass', 'full procedure': 'no verdict'}
== outcomes.json
  no verdict T/base/0: whole 0.0000 -> no verdict
  no verdict T/base/1: whole 0.0000 -> no verdict
  no verdict T/base/2: whole 0.0000 -> no verdict
  unseen vocabulary C/base/0: whole 0.5600 ownership-only 0.0737 -> valid degree 1.0025773195876289
  unseen vocabulary F/base/0: whole 0.5463 ownership-only 0.0762 -> valid degree 1.0
  unseen vocabulary T/base/0: whole 0.7588 ownership-only 0.8850 -> negative degree -0.18703703703703697
  negative search {'found_at_nomination': ['T/base/0'], 'widened': False}
== summary_base.json separation {"0": {"C_minus_T": 0.9975, "clears_0_5": true}, "1": {"C_minus_T": 1.0, "clears_0_5": true}, "2": {"C_minus_T": 1.008450704225352, "clears_0_5": true}}
== invariance.json
  R-5 dev seed 99 (1500 pairs): identical True, acting differs 21000
  R-5 train seed 1000 (15000 pairs): identical True, acting differs 210000
  R-5 train seed 1001 (15000 pairs): identical True, acting differs 210000
  R-5 train seed 1002 (15000 pairs): identical True, acting differs 210000
  R-5 name-only {'n': 3000, 'other': 1.0, 'own': 0.238}
  R-6 {'grammar_attributes_used': {'floor_check': [], 'measure': [], 'reading': []}, 'reaches_rendering': False}
```

### E. The earlier records the findings compare against (origin/main at `c17dbdc`)

```
== out-repairs/diagnose_named_other.json, base recipe
  F/base/0: named 0.3313  not_in_item 0.2173  other_in_item 0.3880  own 0.0633
  F/base/1: named 0.2603  not_in_item 0.1837  other_in_item 0.4847  own 0.0713
  F/base/2: named 0.2487  not_in_item 0.1920  other_in_item 0.5127  own 0.0467
== out-repairs/gate_base.json, free arm
  F/base/0: own 0.5597 named-other 0.3313 (994)
  F/base/1: own 0.5513 named-other 0.2603 (781)
  F/base/2: own 0.5547 named-other 0.2487 (746)
== out/gate.json
  top-level keys ['learn_both', 'lesion', 'reference_points', 'solvers']
{"learn_both": {"C/0": {"n": 3000, "other": 0.259, "own": 0.5816666666666667}, "C/1": {"n": 3000, "other": 0.237, "own": 0.566}, "C/2": {"n": 3000, "other": 0.26366666666666666, "own": 0.5766666666666667}, "F/0": {"n": 3000, "other": 0.25466666666666665, "own": 0.5633333333333334}, "F/1": {"n": 3000, "other": 0.268, "own": 0.5563333333333333}, "F/2": {"n": 3000, "other": 0.23933333333333334, "own": 0.589}, "T/0": {"n": 3000, "other": 1.0, "own": 1.0}, "T/1": {"n": 3000, "other": 1.0, "own": 1.0}, "T/2": {"n": 3000, "other": 1.0, "own": 1.0}}, "lesion": {"C/0": {"n": 3000, "other": 0.20466666666666666, "own": 0.17166666666666666}, "C/1": {"n": 3000, "other": 0.18466666666666667, "own": 0.18066666666666667}, "C/2": {"n": 3000, "other": 0.172, "own": 0.186}, "F/0": {"n": 3000, "other": 0.19133333333333333, "own": 0.18133333333333335}, "F/1": {"n": 3000, "other": 0.222, "own": 0.19466666666666665}, "F/2": {"n": 3000, "other": 0.17866666666666667, "own": 0.18566666666666667}, "T/0": {"n": 3000, "other": 1.0, "own": 0.24666666666666667}, "T/1": {"n": 3000, "other": 1.0, "own": 0.251}, "T/2": {"n": 3000, "other": 1.0, "own": 0.2733333333333333}}, "reference_points": {"a solver that cannot tell whose value it needs": 0.25, "guessing over the eight value slots": 0.125}, "solvers": {"name-only (computed)": {"n": 3000, "other": 1.0, "own": 0.238}, "ownership-blind (trained, acting channel removed)": {"n": 3000, "other": 0.22533333333333333, "own": 0.22366666666666668}}}
```
