# Check of the sharpness-fix branch: the fixed sharpness, the in-use check and the toy retrain (2026-10-08)

*Written 2026-10-08 (Pacific) by a Claude Code session that wrote none of the
work it checks, under the repository's pairing rule. Checked: branch
`fix-sharpness-inuse-check` at its head commit `644238e` (the toy retrain and
findings commit; pull request 118), five commits, diffed against the merge
base with the main line, commit `bd0de26` (the last main-line commit the branch
contains), never against the main line directly. This report sits on branch
`check-sharpness-fix-2026-10-08`, cut from the sharpness branch. Laptop only,
nothing rented, no model called: $0. Written under the workspace plain-language
rule. Counts marked MEASURED carry the command that produced them; judgements
are marked ARGUED.*

## In short

- **The code and every figure reproduce.** The 237 self-tests pass, the twelve
  committed toy models load bit for bit, the 14 made-up cases on real models
  give the committed output byte for byte, the 28 decision-code cases rewrite
  their committed folder with not one byte changed, and the in-use check on
  the twelve committed and nine retrained toy models gives every number in the
  findings' tables, including arm C's route use 0.269, 0.233, 0.221 before and
  0.285, 0.273, 0.244 after the fix, arm M's stirred-in route 0.071, 0.090,
  0.109 before and 0.090, 0.106, 0.100 after, arm T at 1.000, and arm C's
  weight on the true agent 0.914, 0.573, 0.681 before and 0.999 after.
- **One must-fix, a wording range, not a figure in the code or the outputs.**
  The findings' summary says swapping arm C's answer "loses only 24% to 29%"
  before the fix and after it; the before-fix figures in the same sentence
  are 0.221 and 0.233, that is 22 and 23 per cent. Section 5.6 of version 5
  of the registration text copies the "24 to 29" range beside the same
  figures. The range should read 22 to 29 (or be limited to the after-fix
  figures). The direction of the claim, all six figures well under the 0.5
  bar, is unchanged.
- **Four should-fix items, all wording in the findings**: the sentence "all 14
  landed as written" overstates two cases (case 6's stirred-in route and case
  13's "could not be evaluated" branch, which no real-model case reached); one
  bare commit identifier; the outcome code "R1" used without its plain
  meaning; and the nine retrained model files are not in the repository (the
  `*.pt` ignore rule) although the findings point at their folder.
- **Verdict: the branch may be merged as it stands.** The registration may
  cite it once the one range is corrected in the findings and in section 5.6.
  Nothing in the code, the bars, the cases or the reasons differs from what
  section 5.6 and the 2026-10-08 ruling say they are.

## 1. What I read

- The workspace and repository working guides.
- The method note (`docs/2026-10-06-sharpness-fix-inuse-check-method.md`)
  and the findings (`docs/2026-10-06-sharpness-fix-inuse-check-findings.md`).
- The five commits' diffs against the merge base: the method note (commit
  `042dc17`), the sharpness fix (commit `6d17de0`, `models.py` only), the
  in-use check and made-up cases (commit `ffcaa51`), the case outputs,
  reference run, reruns and README note (commit `9638ca8`), and the toy
  retrain with the findings (commit `644238e`).
- The experiment's README, the code freeze method
  (`docs/successor-code-freeze-method-2026-10-04.md`, main line), section 5.6
  of version 5 of the registration text
  (`docs/successor-experiment-proposal-2026-10-07-v5.md`, main line) and the
  verification-bar ruling (`docs/rulings/2026-10-08-verification-bar-ruling.md`,
  main line).
- The model code's ownership answer (`_own_vec`), the trunk's use of the
  acting signal, arm M's route split, `measure.route_check`, `measure.withhold`,
  `measure.outcome`, `procedure.gate`, `procedure.swap_answer` and
  `procedure.route_in_use`.

Environment (MEASURED): the README names `requirements-measure.txt`; the
project's environment at `~/Code/minimum-viable-mind/.venv` has Python
3.12.13, torch 2.12.1, numpy 2.5.0, scikit-learn 1.9.0, scipy 1.18.0, matching
the pinned versions (`python -m pip freeze | grep -iE 'torch|numpy|scipy|scikit'`).
Nothing was installed.

## 2. What I ran, and what came back

Every command below ran from
`experiments/08-successor-degree/` in my worktree with the project's
`.venv/bin/python`, on the laptop's processor, $0.

| What | Command | Result (MEASURED) |
|---|---|---|
| Commit order | `git log --format='%h %ad %s' --date=iso bd0de26..HEAD` | method note `042dc17` at 19:17:21; first code change `6d17de0` at 19:18:14; the note has one commit in its history (`git log -- docs/2026-10-06-sharpness-fix-inuse-check-method.md`) and that commit holds only the note (`git show --stat 042dc17`: 1 file) |
| Every self-test | `src/run_self_tests.sh` | exit 0, `ALL SELF-TESTS PASS`; 237 `[PASS]`, 0 `[FAIL]` (`grep -c`); 26 seconds |
| Test T2, the twelve committed toy models load into the changed code | `python tests/load_toy_models.py` | exit 0, `T2 PASSES`, 12 of 12 "no missing or extra weights; outputs and all 5 running states bit-identical on 400 episodes" |
| The 14 made-up cases on real models | `python tests/inuse_cases.py --out SCRATCH` | "14 checks; differ from expectation: []"; `diff` of the printed table against the committed `out-sharpness-fix/inuse-cases/stdout.txt`: identical; 44 seconds |
| The in-use check on the twelve committed toy models | the committed `committed_toy_reference.py`, copied with its output path moved to the scratchpad | `diff` against the committed `.txt` and `.json`: both identical |
| The 28 decision-code cases | `python tests/a2_run_cases.py` (it deletes and rewrites the tracked `out-a2-cases/`) | "28 cases; 0 differ from expectation or leak: []"; afterwards `git status --short` listed 0 changed files, so the rewritten folder is byte-identical to the commit |
| The nine retrained toy models against the committed hash list | `shasum -a 256 -c SHA256SUMS` in the sibling worktree's `out-sharpness-fix/models/` | 9 of 9 OK; the list there is identical to the committed one (`diff`) |
| The in-use check on the nine retrained models beside the committed ones | `python tests/retrained_toy_inuse.py --models <sibling worktree>/out-sharpness-fix/models --out SCRATCH/retrained_inuse.json` | `diff` against the committed `retrained_inuse.txt` and `.json`: both identical; 44 seconds |
| Is the sharpness a buffer; how do old models load | my probe script (`sharpness_probe.py`, in the scratchpad) | see section 3, item 2 |
| Learned-number counts before and after | my probe script (`param_count.py`) against the merge-base `models.py` | arm T 950,879 to 950,878; arm C 1,301,191 to 1,301,190; arm M 987,781 to 987,780; arm F 1,265,191 unchanged |
| Case 13's untrained model | my one-off probe, same construction as the test script (`torch.manual_seed(0)`, `M.build("C", "toy")`) | right with the true answer 3 of 3,000; still right with the answer swapped 3; route use 0.000; state `failed` |
| Dashes in the two notes | `grep -o $'\xe2\x80\x94' FILE \| wc -l` and the same for `\xe2\x80\x93` | method note: 0 em-dashes, 0 en-dashes; findings: 0 and 0. Both contain the minus sign (U+2212) in negative numbers and the findings use arrows in a table; neither is a dash |

What I did not run: the toy retrain itself (section 5, item 4 explains), the
eleven remaining full re-reads, test T3 and test T6.

## 3. Findings

Severity: must-fix (the registration should not cite it as written),
should-fix (wording that would mislead a reader of the record), note (for the
record, no change needed).

### 3.1 Order of commits, and whether the code does what the method note says (check 1)

**Order (MEASURED, table above):** the method note is committed 53 seconds
before the first code change and has never been edited since.

**The code against the note (ARGUED from reading the diffs, with the measured
cases):** every mechanism the note states is in the code: the buffer under the
old name (`_fix_sharpness` in `models.py`), arm F untouched, no change to the
training code, the record written by `procedure.gate` into `gate.route_in_use`,
part A as the mean weight on the agent with the most "this turn is yours"
firings (`tally.argmax`), part B as the swap of every agent label by one
(`swap_answer`, which changes only `assign_agent_at`, and `assign_agent_at` is
read in exactly one place in `models.py`, the ownership answer at line 174),
the route masks (arm T every own-directed action under "slot", arm C under
"entangled", arm M split by `entangled_route` into items it1 to it3 and it0
and it4), the ratio (right with the true answer minus still right with the
swapped answer, over right with the true answer), the bars 0.9 and 0.5, the
case runner's injected passing record for the 25 old cases (stated in the
note's section 3), and the retrain through the rehearsal's `training.train_arm`
with the exact recipe (`retrain_toy_fixed.py` asserts the recipe line is
present in `repairs.py`).

Differences, none of which changes behaviour:

1. **Note.** The route record carries fields the note does not list:
   `sharpness_learned`, `weight_bar`, `use_bar`, and its own `state` and
   `reasons` (computed in `procedure.route_in_use` by calling
   `measure.route_check`). `measure.withhold` re-judges from the raw fields and
   ignores the stored `state`. Harmless now; if the bar ever changes, a row's
   stored state goes stale while `withhold`'s judgement follows the constant.
2. **Note.** The record is computed and stored for arm F too. The note says arm
   F's figures are "recorded as a reference", so this is as stated;
   `route_check` returns "not applicable" for arm F and `withhold` never adds
   the check to arm F's list (self-test "case 17", passed).
3. **Note.** A README section was added; the note does not mention it. It
   describes the change accurately.
4. The two cases whose sub-expectations did not land as written are finding
   3.3.2 below.

### 3.2 The sharpness fix (check 2)

All MEASURED by the probe script unless marked.

1. **A buffer the optimiser never sees, 4.0 in arms T, C and M, untouched in
   arm F.** Freshly built at the toy size: arm T `in parameters=False
   in buffers=True value=4.0`; arm C and arm M the same; arm F `in
   parameters=True in buffers=False value=4.0`. Each built arm has exactly one
   learned number fewer than at the merge base; arm F has the same count
   (table above).
2. **The self-tests test what the note says.** In `self-tests.txt` lines 82 to
   88: for each of arms T, C and M, "the sharpness is fixed at 4.0, not
   learned; still exactly 4.0 after optimiser steps with weight decay; saved
   under its old name" and "a model saved with a learned sharpness loads
   strictly, with its value"; for arm F, "the sharpness is still a learned
   number (unchanged)". The test takes three AdamW steps at learning rate 0.1
   and weight decay 0.5 on a real loss and checks `float(m.own_sharpness) ==
   4.0` exactly (read from `models.py` lines 519 to 527).
3. **Every older saved model loads with the value it learned.** The twelve
   committed toy models, loaded strictly: arm T 3.8837, 3.8835, 3.8825; arm C
   1.7310, 0.6970, 0.9281; arm M 2.8421, 2.6914, 2.4174; arm F 4.0000 three
   times (each equal to the value in its saved file). The four 10-million
   development checkpoints, loaded by `procedure.load_model`: arm T 1.9469,
   arm C minus 0.0886, arm M minus 0.0083, arm F 4.0000. The nine retrained
   models: 4.0 exactly, nine of nine, and their learned-number counts match
   the changed code's.

### 3.3 The in-use check (check 3)

1. **The bars and routes are the ruling's (MEASURED from the code and the
   self-tests).** `ROUTE_WEIGHT_MIN = 0.9`, `ROUTE_USE_MIN = 0.5`; a seed fails
   when the weight is below 0.9 or any route's use is below 0.5, so exactly at
   a bar passes (self-test "exactly at the bars passes (0.9 weight, 0.5 use)",
   passed). Arm T is judged on its slot, arm C on its stirred-in route, arm M
   on both of its routes (self-test "arm M: one route of two flat", which
   fails naming "the separable route (items it0 and it4)", passed). A route
   with no right answer to lose returns "could not be evaluated" and
   withholds (self-test "a route with nothing right to lose", passed); a built
   arm's row with no `route_in_use` field returns "not run" and withholds
   (self-tests "case 16" for arms T and M, passed). A failing seed's reason
   begins "the built ownership route has gone flat (construction did not
   hold):" and names the route and the figure (the 28-case table, case 27:
   "... the stirred-in route is not in use: route use 0.005, bar 0.5").
2. **Should-fix (findings, section 2, "All 14 landed as written in the
   method").** Two cases landed on the overall state the script checks but
   not on what the method wrote for them. Case 6 (arm M, separable reader
   zeroed): the method wrote "fails, naming the separable route; the
   stirred-in route passes"; measured, the stirred-in route fails too at
   0.076. The findings disclose this two paragraphs later as something the
   cases "did not aim at". Case 13 (untrained arm C, "nothing right to lose"):
   the method wrote "part B could not be evaluated: fails"; measured, the
   untrained model got 3 of 3,000 own-directed actions right, so part B was
   evaluated, at 0.000, and the state is "failed", not "could not be
   evaluated". The test script accepts either outcome. So the "could not be
   evaluated" branch has been exercised only on a made-up record in
   `measure.py`'s self-test, never on a real model. Ask: say both in the
   findings' sentence, and, if a real-model case is wanted, zero the output
   head so that nothing is right.
3. **Not a learning condition; never "substrate not a testbed" by itself
   (MEASURED).** `withhold` returns `learning_passes` from `seed_gate`, which
   reads only the gate on learning; the route check is added to `checks`
   after that and cannot touch it (self-test "the in-use failure is not a
   learning failure (never R3 by itself)", passed). `measure.outcome` gives
   "substrate not a testbed" only from `gates[arm]` or the step 5a record,
   both built from `learning_passes`. End to end: arm T flat on two seeds
   gives "metric not validated" (case 27), arm C flat gives "metric checked
   against the separable model only, degree read" (case 26), arm M flat
   leaves "metric validated, degree read" with arm M without a verdict (case
   28).
4. **Reruns (MEASURED, table above):** 28 of 28 decision-code cases, with the
   tracked outputs byte-identical after the rewrite; 14 of 14 made-up cases on
   real models, printed table identical to the committed one.
5. **Note.** When a seed's only trouble is a route that "could not be
   evaluated", the reason reads "the built-route check could not be
   evaluated: ..." and does not contain the words "construction did not
   hold"; only a flat route (or a flat answer) carries them. Both withhold.
   The ruling names the three states separately ("could not be evaluated",
   "not run", both counting against; a failing seed "construction did not
   hold"), so this matches the ruling. If John wants every in-use withholding
   to carry "construction did not hold", it is one line in `route_check`.
6. **Note.** The made-up arm T row in case 27 is labelled "the stirred-in
   route" because the injected record uses one route name for every arm; real
   arm T rows say "the slot route". Disclosed in the findings; confirmed in
   `out-a2-cases/inuse-T-flat/summary.json`.

### 3.4 The toy figures (check 4)

1. **The twelve committed toy models (MEASURED):** the rerun of the reference
   script gives the committed text and JSON exactly. Arm T passed, route use
   1.000 on all three seeds; arm C failed, 0.269, 0.233, 0.221, with weight on
   the true agent 0.914, 0.573, 0.681; arm M failed, stirred-in route 0.071,
   0.090, 0.109, separable 1.000; arm F 0.000, not judged. Every number the
   findings' tables give for the committed models is in that output.
2. **The nine retrained models are not committed; the figures reproduce
   from the files on disk (MEASURED).** `git ls-files | grep '\.pt$'` lists no
   file under `out-sharpness-fix/`; the repository ignores `*.pt`. The nine
   files sit in the branch's own worktree
   (`~/Code/mvm-sharpness-fix/experiments/08-successor-degree/out-sharpness-fix/models/`)
   and match the committed `SHA256SUMS` nine of nine. Run on them, the
   committed script gives `retrained_inuse.txt` and `.json` exactly: arm C
   0.285, 0.273, 0.244; arm M stirred-in 0.090, 0.106, 0.100, separable 1.000;
   arm T 1.000; weight 0.999 on every built seed; sharpness 4.00 on all nine.
   **Should-fix (findings, section 4 heading and section 1):** say that the
   nine model files are not in the repository and where they are, since the
   section heading points at `out-sharpness-fix/models/` as if they were
   there. The nine training records there are committed and say
   `sharpness_at_end 4.0`, the recipe 2,500 steps, batch 256, learning rate
   0.003, 15,000 pairs, device `mps`, and 1,660 to 2,200 seconds each.
3. **The retrain was not reproduced, and why (ARGUED).** The findings say each
   model took 1,660 to 2,200 seconds (28 to 37 minutes) on the laptop's
   graphics processor, three at a time, 1 hour 44 minutes in all. That is
   not "minutes", and a second copy of nine models would carry nothing the
   hash-checked files do not. What the retrain claims (sharpness 4.0 at the
   end, the gate counts, the route-use figures) is reproduced from the files
   as above. Training on a graphics processor is not bit-reproducible in any
   case, so a retrain would have checked the recipe, not the figures.
4. **The arm T seed 0 re-read (MEASURED from `reread/row_T_seed0.json`):**
   nominated; site set layers `[0]`, positions "action", rank 8, piece 180 of
   180, whole read 180 of 180; degree 0.0; controls 1, 4 and 7 `True`, 3 and 6
   not run; development floor clears; the route record in the row says
   sharpness 4.0, not learned, weight 0.99899, slot route use 1.0, state
   passed; the checkpoint hash in the row equals the committed `SHA256SUMS`
   entry for arm T seed 0. This is what the findings and section 5.6 say.
   **Note:** this one re-read took 3,639 seconds on the shared processor; the
   re-read script runs up to four at once, so the findings' "about an hour on
   a quiet laptop" for the other eleven is an estimate, not a measurement.

### 3.5 The findings' claims against the outputs (check 5)

1. **"No seed lost more than 36 of 3,000 own-directed answers" (MEASURED):**
   from the reproduced `retrained_inuse.txt`, the drops are arm C seed 1 from
   1,703 to 1,671 (32), arm C seed 2 from 1,727 to 1,691 (36), arm M seed 0
   from 2,592 to 2,590 (2), arm M seed 1 from 2,584 to 2,563 (21); every other
   seed rose or held. Largest 36. Supported.
2. **"Arm C's weight on the true agent rose to 0.999 on every seed"
   (MEASURED):** 0.914, 0.573, 0.681 to 0.999, 0.999, 0.999 in the same
   output. Supported.
3. **The sentence that weight decay alone cannot drive the sharpness past
   zero (ARGUED; the sentence is in section 5.6 of version 5, not in the
   findings).** Both trainers use AdamW (`rehearsal-successor-measure/src/training.py`
   line 77, weight decay 0.01; `src/train_successor.py` line 120). AdamW's
   weight decay multiplies each number by one minus the learning rate times
   the decay at every step: it shrinks a number toward zero and cannot change
   its sign. A sharpness of minus 0.0886 (arm C, measured above) therefore
   came from the gradient. The sentence is sound for the optimiser the code
   uses.
4. **The four options (ARGUED against the figures):** (a) keep 0.5 is what the
   code does (`ROUTE_USE_MIN = 0.5`); (b)'s "toy arm C passes; toy arm M's
   stirred-in half sits at the edge" is right at a 0.1 bar (arm C 0.244 and
   up; arm M 0.090, 0.106, 0.100, one below, two at or above); (c) and (d) are
   design statements the figures do not contradict. The ruling took (a).
5. **Must-fix (findings, "In short", third bullet; and section 5.6 of
   version 5, the paragraph "What the toy says about that verification").**
   "Swapping arm C's built answer to another agent loses only 24% to 29% of
   its right own-directed answers" is said of the toy "before the fix and
   after it", but the before-fix figures are 0.269, 0.233, 0.221: the range
   over all six is 22 to 29 per cent. The findings' "arm M's stirred-in half
   loses 9% to 11%" has the same shape (before the fix includes 0.071, 7 per
   cent); section 5.6 already says "7 to 11 per cent" for arm M but keeps
   "24 to 29" for arm C beside the listed 0.221. Both are two-character
   fixes; the direction of the claim is unchanged. I did not edit either file.

### 3.6 The branch against section 5.6 and the ruling (check 6)

Read side by side (ARGUED, with each figure MEASURED above): the bars (0.9,
0.5, "at least"), the routes (arm T's slot, arm C's stirred-in route, both of
arm M's), the three states and that both "could not be evaluated" and "not
run" count against, the reason "construction did not hold", the same 3,000
gate episodes, `procedure.gate` writing `route_in_use` and `measure.withhold`
judging it, "a seed counts only when both parts pass and the seed passes its
learning gate", the 10-million figures (arm C 0.018, arm M 0.000 on both
routes, arm T 0.924; weights 0.218, 0.247, 0.942; sharpness minus 0.089,
minus 0.008, 1.947), the toy figures before and after, the retrain's 4.0 and
36, and the arm T seed 0 re-read all agree with the code and the outputs.
The one difference is the range in finding 3.5.5, which section 5.6 inherits
from the findings. Nothing else in a figure, a bar, a case or a reason
differs.

### 3.7 Plain language (check 7)

1. **Dashes (MEASURED):** 0 em-dashes and 0 en-dashes in each of the two
   notes.
2. **Should-fix (findings, section 1, "Merging"):** "`git merge-tree` at
   `0064ef3`" is a bare commit identifier with no phrase saying what it is (a
   commit of which branch, holding what). The workspace rule asks for a plain
   label on every identifier.
3. **Should-fix (findings, section 3; method note, cases 18 and 20):** the
   outcome code "R1" is used without its plain meaning ("metric validated,
   degree read"). The method note labels "R3" once ("substrate not a
   testbed"); "R1" is never labelled in either note.
4. **Note:** "checkpoints" (both notes) is borrowed software vocabulary where
   "saved models" would do; "AdamW" and "one-cycle schedule" are the recipe's
   own names and are explained by their settings. The term "buffer" is
   explained at first use in both notes. The notes are otherwise plain.

## 4. Verdict

**The branch may be merged as it stands (ARGUED from the measurements
above).** The code is a buffer fixed at 4.0 in the three built arms and
untouched in arm F; every older model loads with its learned value; the
in-use check is the ruling's, bar for bar, route for route and reason for
reason; it is not a learning condition; and every figure the findings and the
registration quote from this branch reproduces exactly from the committed
files and the hash-checked retrained models. **The registration may cite it
once the one range ("24 to 29 per cent" for arm C's loss) is corrected, in
the findings and in section 5.6, to 22 to 29 per cent or limited to the
after-fix figures.** The should-fix items are wording in the findings and do
not touch code, outputs or bars.

## 5. What I did not check

- The toy retrain itself (section 3.4, item 3): reproduced from the
  hash-checked files, not by training again.
- The eleven remaining full re-reads and the toy outcome under the repaired
  construction: not run on the branch either; the findings say so.
- Tests T3 and T6 of the code freeze: not run on the branch either.
- The findings' claim that this branch merges with branch
  `training-exclusion-pairing` without conflict: not re-run.
- The 10-million development checkpoints' provenance: I took the files on the
  laptop as given and recorded their hashes in my probe output; the made-up
  case script records them too.
- Whether the three 10-million reruns should launch: not this check's
  question.
