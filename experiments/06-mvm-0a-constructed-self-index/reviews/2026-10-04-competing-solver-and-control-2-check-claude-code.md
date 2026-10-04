# Check of the competing-solver run (pull request 88) and of the other-agent control against twenty random pieces (pull request 89)

*Written 2026-10-03 (Pacific), late evening, by a Claude Code checking
session ("MVM W2d check of the competing-solver run and the twenty-piece
control"), on branch `w2d-check-competing-solver-and-control-2`, cut from the
main line at `7a55fe0`. The file carries the date 2026-10-04 because the
brief named it so. Laptop, processor only. Nothing rented, nothing trained
beyond the small straight-line reads the checked code itself fits, nothing
launched, nothing spent: $0.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (this session ran something, or read it off a committed file or
off GitHub's own record, and says which) or **ARGUED** (a judgement, with its
reasons). This is a check of two rehearsal records on toy models. It is not a
result about the scientific question.*

**The pairing rule.** This session wrote neither pull request. Both were
written and run by one other session. This check is the one ruling 7
(`docs/rulings/2026-10-03-version-4-questions-rulings.md`) requires before
the registration review, and the one the control's findings say is owed.

## What this session opened

- **Pull request 88**, branch `w2b-job1-competing-solver-run` (commits
  `744a8b3`, `3fee39f`, `3d55865`): its method
  (`docs/2026-10-03-competing-solver-run-method.md`), findings
  (`docs/2026-10-03-competing-solver-run.md`), code
  (`experiments/rehearsal-successor-measure/src/competing_solver_run.py`),
  every output under `out-competing-solver-run/`, and its description on
  GitHub.
- **Pull request 89**, branch `w2b-job2-control-2-twenty-draws` (commits
  `174081e`, `c148bf1`): its method
  (`docs/2026-10-03-control-2-twenty-draws-method.md`), findings
  (`docs/2026-10-03-control-2-twenty-draws.md`), code
  (`src/control2_twenty_draws.py`), every output under
  `out-control-2-twenty-draws/`, and its description on GitHub.
- The rulings the two cite: the seven-question ruling, record B
  (`docs/rulings/2026-10-03-version-4-questions-rulings.md`, rulings 4, 5 and
  7), the ruling that record B stands
  (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`), and the
  ruling on the two questions from the check of version 4
  (`docs/rulings/2026-10-03-version-4-check-questions-rulings.md`, ruling 1).
- The committed code both runs import (`rerun_controls.py`, `rerun_v3.py`,
  `repairs.py`, `training.py`, `arms.py`), the committed gate file
  `out-repairs/gate_base.json`, the earlier code test's output
  `out-short-prestated-run/part_c_NOT_A_RESULT.json`, the model fingerprint
  list `out-repairs/models/SHA256SUMS`, and the environment lock
  `.venv-lock-2026-08-28.txt`.
- Version 4 of the proposal (`docs/successor-experiment-proposal-2026-10-03-v4.md`
  at `7a55fe0`): every passage that mentions the competing solver, the
  other-agent control, the whole-state floor's job, the no-transplant
  formula, or the sampling band, found by search and read in full with the
  surrounding section. Not read through end to end.
- GitHub's own record of when each branch was created and pushed.

**Not opened:** the transcript of any other session; the first record of
the seven-question ruling, beyond the line that version 4 cites it; any
ruling packet. Nothing was put to John in chat.

This session's scripts and their outputs are beside this file, in
`2026-10-04-competing-solver-and-control-2-check-scripts/`.

**A note on citations.** The files of pull requests 88 and 89 are cited
here by the paths they will have once those pull requests are merged. Until
then they exist only on those two branches, and the repository's citation
checker (`scripts/check_citations.py`), run on this file, lists the 14 such
references as missing for that reason. It finds no other missing file and no
figure absent from the file its sentence cites.

---

## 1. The result on one page

**Both pull requests hold. Every figure the brief named checks out. The
re-runs reproduce the committed outputs exactly. Neither needs a new run.**
What this check adds is a handful of wording fixes, one fault in how the
solver's findings explain *why* the solver gets no verdict, and two points
for the registration text that the runs' own findings did not reach.

- **Method before output, both pull requests (MEASURED, from git and
  GitHub).** Each method commit carries no output, comes before its output
  commit in the branch's history, and was pushed before it. The code file is
  byte-identical between each method commit and the branch tip.
- **Re-run from a clean checkout (MEASURED).** The control's three output
  files came back byte-identical; its printed output differs only in the
  running time (52 seconds against 50). Of the solver's 21 output files, 20
  came back byte-identical, including all six fitted reads, whose arrays are
  equal too; the twenty-first, `summary.json`, differs in one field only, the
  running time (930 seconds against 839). Its printed output is identical
  apart from the running time.
- **The figures (MEASURED, by an independent recount from the raw fields;
  all 69 checks pass).** No verdict on every seed under both readings of
  the solver. Best piece of the marker-word read 20 to 25 of 180 against 144.
  The gate on the processor at 702, 715 and 702 of 3,000 on the own-directed
  condition, equal field for field to the committed graphics-chip figures.
  The null transplant bit-identical at all 45 site sets everywhere. Seed 2
  with the channel left on clears the whole-state floor at 33 of 45 site
  sets on fresh episodes and none on development episodes. For the control:
  0.0012, 0.0063 and 0.0962 equal the earlier code test's to the last bit;
  the twenty pieces have a middle value of 0.0037, a 95th percentile of
  0.0052, and 0 below, 1 equal and 19 above.
- **Against the rulings (MEASURED from the code, then ARGUED).** The control
  does what ruling 5 says and nothing else. The solver run does what ruling 7
  asks. It does not do one thing version 4 requires of the registered code
  (withholding a reading in code when the no-transplant rule fails); here
  that changes nothing, because nothing was nominated.
- **One explanation in the solver's findings needs correcting (ARGUED, from
  version 4's text).** Its section 4, its question 2 and the pull-request
  description say the gate on learning is the first thing that "holds the
  solver back", because "in the registered experiment a model that fails the
  gate is not read at all". Version 4 gates the four arms, not the competing
  solvers: their accuracy is printed beside the gate as a reference (section
  8.1, and the gate row of section 9). The solver *would* fail the gate if it
  were gated as the free model is, but that is not what stopped it. What
  stopped it under the rules as written is the floor at nomination, and
  behind that the piece rule and the no-transplant rule.
- **Two points for the registration that neither run's findings reached
  (ARGUED).** (a) Version 4's rehearsal item R-6 credits the whole-state floor
  alone with keeping the formula's divisor away from zero. On this solver
  the floor was cleared on fresh episodes with a divisor of one or two
  episodes in 800. What keeps the divisor large on a real arm is the floor
  *together with* the gate and the no-transplant rule. (b) This solver fails
  the task. So the run shows the measure returns nothing on a model that has
  not learned the task; it does not show what the measure does on a model
  that solves the task by a route other than tracking whose turn it is.
- **Version 4 sentences.** The solver's findings name the right passages and
  miss five more; the control's findings name the right passages and miss
  the one that a later ruling made wrong (section 7.3, item 2, lines 1830 to
  1837). Section 6 lists them all, by line.
- **Questions for John.** Of the five, four suggestions follow from the
  evidence as written; one (the solver's question 2) needs rewording for the
  gate. This check adds two, each with a suggestion (section 9).

---

## 2. Job 1: method before output

**MEASURED, from git** (`git show --stat`, `git diff --name-status`,
`git rev-parse <commit>:<path>`) **and from GitHub's activity record for each
branch** (`gh api repos/jfredson/minimum-viable-mind/activity?ref=...`).

| | Pull request 88, the solver | Pull request 89, the control |
|---|---|---|
| Branch cut from | `41b0bd3` (the main line before pull requests 86 and 87) | `41b0bd3` |
| Method commit and what it carries | `744a8b3`: the method file and `competing_solver_run.py`. **No output file.** No file under `out-competing-solver-run/` exists in its tree | `174081e`: the method file and `control2_twenty_draws.py`. **No output file.** No file under `out-control-2-twenty-draws/` exists in its tree |
| Output commit, and its parent | `3fee39f`, parent `744a8b3`; then `3d55865`, parent `3fee39f` | `c148bf1`, parent `174081e` |
| What the output commits change | Only added files (the findings and 22 output files); `3d55865` changes two lines of the findings. Nothing already committed is modified | Only added files (the findings and 3 output files) |
| The code, method commit against branch tip | byte-identical (both blobs `af7cc95`) | byte-identical (both blobs `517aa17`) |
| Pushed to GitHub (Pacific) | method at 19:36:03 (the branch's creation); outputs at 19:52:02; wording fix at 19:52:35 | method at 19:52:49 (the branch's creation); outputs at 19:54:22 |

The solver's run took 839 seconds by its own printout, which fits in the 16
minutes between the two pushes. The control's took 50 seconds, which fits in
its 93. GitHub's record shows the method's push before the output's push in
both cases, which is what the pairing rule needs; it cannot show when on the
laptop each run started, and this check does not claim it does.

**One thing worth knowing, not a fault.** Both branches were cut before the
main line took in the check of version 4 (pull request 86) and John's ruling
on its two questions (pull request 87). So neither run could cite
`docs/rulings/2026-10-03-version-4-check-questions-rulings.md`. The control
satisfies its ruling 1 anyway (section 4 below). That ruling also says "The
competing-solver session ... already has this change in its plan. Its check
confirms the change was made": **confirmed** — the change is in pull request
89, not 88, and was made by the same session.

---

## 3. Job 2: the re-run from a clean checkout

**MEASURED.** Each branch tip was checked out in its own detached worktree
(`git worktree add --detach`), with nothing else in it, and the committed
code was run exactly as each findings file gives the command, with the
project's Python (`.venv/bin/python`; torch 2.12.1, scikit-learn 1.9.0,
numpy 2.5.0, the versions `.venv-lock-2026-08-28.txt` pins). The three
competing-solver model files matched `SHA256SUMS` before the run (`shasum -a
256 -c`). Then every output file was compared with the committed one by
`compare_rerun.py`: byte for byte for the JSON, the tables and the text, and
array by array for the `.npz` files (a zip archive can change its bytes while
its arrays stay the same).

**Pull request 89, the control.** 3 files compared, **0 differ**:
`code_test_NOT_A_RESULT.json`, `table.md`, and `stdout.txt` (which the run
does not write; it is unchanged). The printed output equals the committed
`stdout.txt` line for line except the last, "done in 52s" against "done in
50s". Running time: 52 seconds.

**Pull request 88, the solver.** 21 files compared, **1 differs, and only
in its running time**. All six `measure_*.json`, all six `nominate_*.json`
and `table.md` are byte-identical. All six `reads_*.npz` are array-equal
(largest difference 0.0) and byte-identical as well. `summary.json` differs
in one line of 394, the field `"seconds"`: 929.91 against 839.05. That is
how long the run took, not a result. The printed output equals the committed
`stdout.txt` line for line apart from the last line, "done in 930s" against
"done in 839s". Running time: 930 seconds. The committed models matched their
fingerprints before loading, and the run's own fingerprint check (stop B1)
passed.

Outputs, in the scripts folder: `rerun_compare_output.txt` (the comparison),
`rerun_solver_stdout.txt` and `rerun_control_stdout.txt` (what each re-run
printed). Neither run writes its own `stdout.txt`, so the comparison file's
`stdout.txt` lines compare the committed file with itself; the printed output
is compared separately, at the end of each section of that file.

---

## 4. Job 3: every figure, against the outputs

**MEASURED**, by `independent_check.py`, which reads the committed outputs
straight from git at the two branch tips and recounts each figure from the
raw fields rather than from the checked code's summaries: it recounts the
site sets that clear the floor from the whole-state accuracies and the
floor's formula; recomputes the sampling band from the textbook formula; and
recomputes the middle value and 95th percentile of the twenty by hand. Its
output is `independent_check_output.txt`. **Every check passes.**

### 4.1 The figures the brief named

| Figure | Claimed | Found |
|---|---|---|
| No verdict on every seed, both readings | yes | **yes**: all six runs "no verdict: no site set clears the whole-state floor", the stricter row the same; the summary's three stop lists empty |
| The marker-word read, best piece | 20 to 25 of 180 against 144 | **20 to 25** (best per seed 24, 23, 23 with the channel removed; 25, 20, 21 left on); 144 needed |
| The gate | 702, 715 and 702 of 3,000 | **702, 715, 702** own-directed and 712, 726, 650 named-other with the channel removed, **equal field for field to `out-repairs/gate_base.json`**; with the channel left on 707, 716, 698 and 710, 722, 653 |
| The null transplant | bit-identical | **bit-identical at all 45 site sets**, on all six runs |
| Seed 2, channel left on | clears the whole-state floor at 33 of 45 site sets on fresh episodes | **33**, and **0** on development episodes. The fresh floor asks for +0.0010, which is 0.8 of one episode in 800; the largest raise is +0.0025, two episodes |
| The control's unchanged figures | 0.0012, 0.0063, 0.0962, matching the earlier test | **equal to the earlier test's to the last bit** (0.0012499999720603228, 0.0062500000931322575, 0.09624999761581421), same site set |
| The twenty | middle 0.0037, 95th percentile 0.0052; 0 below, 1 equal, 19 above | **the same**, recomputed by hand. In episodes of 800, the twenty are 1, 2, 2, 3 (eight times), 4 (eight times) and 7; the real figure is 1 |

### 4.2 Every other figure in the two findings and the two descriptions

All hold. The ones worth a line:

- **The solver's tables 3.1** (the read at every layer and size, both
  readings): equal to the output files **cell for cell**.
- **The whole read 11 to 21; any count 9 to 25**: correct.
- **The sampling bands** in table 3.2 (for example 24 → 16 to 34): the
  Wilson interval at 95 percent, rounded; recomputed independently.
- **"Fails by 64 to 140 of 3,000"**: correct as the range over all twelve
  gate counts (726 is 64 short, 650 is 140 short). On the own-directed
  condition alone it is 74 to 92.
- **Section 4.1, "the floor asks for less than nothing" on seeds 0 and 1**:
  correct under both readings (with the channel removed, seed 0's accuracy
  0.2333 against an untouched rate of 0.2400; seed 1's 0.2100 against
  0.2300).
- **Section 4.2, development requirement +0.0053 and largest raise
  +0.0017** on seed 2 with the channel left on: correct.
- **Table 3.3, the no-transplant rates** (0.2487, 0.2300, 0.2200, 0.2500,
  0.2313, 0.2225 against 0.1107, 0.1116, 0.1109): correct; misses 0.109 to
  0.139, so "0.11 to 0.14" holds. **The wording fix at `3d55865` is right**:
  the earlier text said the rate was *outside its allowance* by 0.11 to
  0.14, when that is the miss against the formula; outside the allowance it
  is 0.09 to 0.12.
- **Table 5, the description-only arithmetic**: the counts of undefined and
  defined comparisons (180/0 three times; 32/148, 20/160, 20/160) and the
  smallest, middle and largest values: correct.
- **The twins' own-directed actions differ on 3 to 12 trials** with the
  channel left on: correct (6, 10, 3, 3, 10, 12).
- **The control's "the one old draw sits above 19 of the 20 and above their
  95th percentile"**: correct.

### 4.3 Two things this check measured that the findings assume

- **The solver's acting-channel vector really is untrained (MEASURED).**
  Rebuilding each model's starting weights from its training seed and
  comparing: the stored vector points in exactly the starting direction
  (cosine 1.0000 on all three seeds) and is 0.9631 times its starting length
  on all three. That shrinkage is the optimiser's weight decay, which acts on
  every weight whether or not it receives a training signal
  (`act_vec_check.py`, output `act_vec_check_output.txt`). So the method's
  "the vector ... was never used: no training step ever passed a signal
  through it" is exactly right, and "reading B" feeds the solver a fixed
  random nudge at its own turns, about 0.25 long.
- **The environment is the pinned one (MEASURED):** the versions both runs
  print equal those in `.venv-lock-2026-08-28.txt`.

### 4.4 Two places where the prose does not match the file it quotes

- **The control's findings, section 2, "What it printed".** The block is
  presented as the program's output but is a reformatted version of it. The
  program prints the site set as a Python dictionary on one line; the block
  writes it out in words and adds "(the floor would have asked for 144)",
  which the program does not print. The figures are the same. *Fix:* label
  the block "what it printed, laid out for reading", or paste
  `stdout.txt` verbatim.
- **The solver's findings, section 2**, shows the command and "..." then
  "done in 839s"; that matches `stdout.txt`. No fix needed.

---

## 5. Job 4: the method against the rulings it cites

### 5.1 Pull request 89 against ruling 5, and the check-questions ruling 1

Ruling 5 asks for: twenty random pieces of the same size at the same sites;
their middle value, 95th percentile, and where the real figure sits among
them; no pass line; the code test run once more on the changed code,
labelled a test of the code and not a result. The check-questions ruling 1
adds: done before the registration review. The brief adds: drawn as control 3
draws them.

**MEASURED, by reading the code and diffing it against the function it
replaces.**

- **Twenty, drawn as control 3 draws them.** `compare` calls
  `rerun_v3.random_bases(rank, layers, seed, ...)`, the same function, with
  the same arguments, that control 3 calls in `rerun_controls.measure_at`.
  The function seeds each draw from (20260926, model seed, draw number) and
  does not depend on the positions. So for a given model, size and layers
  these are control 3's twenty pieces. `assert V.N_RANDOM == 20` guards the
  count.
- **Same size, same sites.** Same rank as the nominated piece, at the same
  layers, applied with the same position mask and the same donor states.
- **Middle value, 95th percentile, below / equal / above.** `np.median`,
  `np.percentile(..., 95)` and three counts, exactly as control 3 computes
  them. The comparison is with the real figure (the named agent's piece),
  which is what ruling 5 asks.
- **No pass line.** The pass-or-fail field and the 0.05 tolerance
  (`C2_TOL`) are gone; the status is "reported; no pass line".
- **Nothing else changed.** The early exits (not applicable on arms T and M;
  no verdict below 790 on the named-other condition; the nomination by the
  identical procedure) are **copied line for line** from
  `rerun_controls.control2`: a diff shows only the docstring and one line's
  indentation differ. (The method says these are "imported"; the helper
  functions are imported, the twelve lines of early exits are copied. The
  behaviour is the same. Not worth a fix.) The one old draw is kept beside
  the twenty, for comparison only, as the method says.
- **Labelled NOT A RESULT**, in the output file's name and first field, the
  table's heading and the findings. **Run before the registration review.**

**Verdict: the code does what ruling 5 says, and nothing else.** One
reading in the method is the running session's and is reasonable: "where the
real figure sits" is reported as the three counts, not as a rank of its own.

### 5.2 Pull request 88 against ruling 7

Ruling 7 asks for: the three committed ownership-blind toy models through the
nomination and the reading as registered; laptop, $0; method before output;
checked by another session before the registration review; the method to
state, as the running session's reading, what "the model's own turn" and its
twin pairing mean for a solver with no acting channel; no verdict expected,
and a reading on any seed to go to John first.

**MEASURED from the code, then ARGUED.**

- **The three models, fingerprint-checked first:** yes (`C.check_sha`, then
  a strict load).
- **The nomination and the reading as registered.** The rule that chooses
  (`rerun_controls.pick`), the 45 site sets, the stricter row, the piece
  rule at 144 applied after the layers are chosen, the whole read printed
  beside it, the floor on development episodes at nomination and again on
  fresh episodes at the reading: all imported from the controls re-run, not
  copied. What is new is only the split between the batch the model is fed
  and the batch the positions and labels come from. Rulings 1 and 2 are
  followed exactly. Ruling 3 (the processor, versions pinned): followed.
  Ruling 4 (the toy's counts; the band printed): the counts are the toy's;
  **the band is printed for each seed's best piece only**, not beside every
  count taken against the floor. Since every count is 119 or more short of
  144, nothing turns on it, but the registered table must print it beside
  every such count, as ruling 4 says.
- **The read is fitted here, because no committed read exists for this
  solver.** The fit is the repairs' own call (logistic regression, at most
  3,000 iterations, C = 1.0, first 420 of 600 for fitting). It is saved and
  then applied unchanged to fresh episodes. Fair, and the method says so.
- **"The model's own turn" and the twin pairing are stated** as the
  session's reading, with a second reading run beside it. Reading A (channel
  removed, as trained) makes the twins one input, so the no verdict follows
  by construction; reading B (channel left on) is the one that tests the
  solver. Both the method and the findings say this plainly. **This is the
  most useful thing the run did**, and it goes past what the ruling asked.
- **What the code does not do (ARGUED).** Version 4 requires the registered
  code to *withhold* a reading itself when a no-transplant miss is outside
  its allowance, or a control that holds fails (section 6.4, item 5, lines
  1205 to 1213). This code records the no-transplant miss and prints it, but
  its "a reading was returned" field depends only on the floor at the
  reading; and it runs none of the controls. Had a site set been nominated,
  stop B2 would have fired on a figure the registered code would have
  withheld. Nothing was nominated, so no figure is affected. The method
  states that it runs no controls (section 4, "Not run"); it does not state
  that the no-transplant rule is printed and not applied. **The findings'
  sentence "It would withhold a reading on its own" (section 1) is true of
  the rule as version 4 registers it, not of this code**, and should say so.
- **Stops.** B1 to B4 are coded as the method states them and none fired.

**Verdict: the run does what ruling 7 asks.** The gap above is a gap
against version 4's later requirement on the registered code, which no
toy-scale code yet meets (version 4 lists it as owed at line 3866), not
against ruling 7.

### 5.3 The solver's explanation of why it gets no verdict

**ARGUED, from version 4's text.** The findings' section 4 (last paragraph),
their question 2, and the pull-request description say what "holds the
solver back with room to spare is, in order: the gate on learning (... in the
registered experiment a model that fails the gate is not read at all); the
piece rule; and the no-transplant rule."

Version 4 does not put the competing solvers through the gate. Section 8.1
gates arms T, C and M on the own-directed condition and arm F on both
(lines 2150 to 2159); the competing solvers' accuracy is listed under
"Reference points reported alongside, and they are references and not
thresholds" (lines 2178 to 2187); the gate row of section 9 says the same
(line 2257). Failing the gate gives outcome R3 *for an arm* (line 2188). So
for the solver the gate is a counterfactual: it *would* fail the gate, on
both conditions and every seed, if it were gated as arm F is. Under the
rules as written, what returned no verdict was the floor at nomination, and
what would have returned no verdict after it, with room to spare, is the
piece rule and the no-transplant rule.

This matters because the registration will likely quote this run as its
answer to "can the measure be satisfied by the wrong thing?". An answer that
leans on the gate invites the reply that the gate is not applied to
competitors. *Fix:* in section 4 and question 2 of the findings and in the
pull-request description, say "would fail the gate if it were gated as arm F
is" and put the piece rule first.

### 5.4 The whole-state floor's job, as the run shows it

**ARGUED, from the measured figures in 4.1 and 4.2.** The findings are right
that on this solver the floor is "a coin": its requirement is four fifths of
(accuracy − untouched rate), and for a solver that cannot tell whose value it
needs those two are within a few episodes of each other. On seed 2 with the
channel left on the fresh floor asked for less than one episode in 800 and
33 site sets cleared it by one or two episodes. Had any of them been
nominated and reached the reading, the formula's divisor would have been one
or two episodes in 800, and the reading would have been decided by single
episodes (the description-only arithmetic on that seed runs from 0.0000 to
1.0000, middle 1.0000).

So the floor alone does not keep the divisor away from zero. On a real arm
it is kept large by three rules together: the gate puts accuracy at 0.2633
or more; the no-transplant rule keeps the untouched rate within 0.018 of
(1 − accuracy) ÷ 7, which is at most about 0.123 at the bar; so the room
between them is at least about 0.14, and four fifths of that is at least
about 0.11. This touches version 4's item R-6 (section 6 below).

---

## 6. Job 5: which sentences of version 4 each finding bears on

Version 4 read at `7a55fe0`. Not edited.

### 6.1 The solver's findings, section 7

| Claim | Right? |
|---|---|
| **Section 7.3, the last paragraph** (lines 1996 to 2017): the run it says is owed exists; "no verdict" came back; its reason ("no read of its own marker word that reaches four fifths") holds but is not the rule that stopped the run first; "This version quotes no figure for it" and "until then this text does not go to the registration review" can be replaced once the run is checked | **Right.** The best piece is 20 to 25 of 180, so the stated reason holds; the floor at nomination stopped it first. Add: the paragraph should also say that with the channel removed the no verdict follows from the pairing alone (section 5.2 above) |
| **Section 8.1, the reference points** (lines 2178 to 2187): 0.2340 to 0.2383 reproduced exactly on the processor; the clause "to be put through the nomination under it before the registration review" is answered | **Right.** 702/3,000 = 0.2340 and 715/3,000 = 0.2383; equal field for field |
| **Section 10, item R-5** (lines 2391 to 2396) **and "What happens next"** (lines 2455 to 2458): the run is done, method first; the check is owed | **Right.** This check is that check |
| **The header's item 2** (lines 21 to 25) | **Right** |
| **Any sentence saying the whole-state floor protects against a solver like this**: "not found by search" | **There is one, and it is a near miss: item R-6** (lines 2397 to 2399), "The chance-corrected form's denominator is kept off zero by the whole-state floor". See section 5.4 above. Also, less directly, line 1860, "Its job of catching a leaky site set is done by the whole-state floor and the no-transplant rule", which is about a different failure and still holds |

**Passages the solver's findings did not name, which also need updating
(MEASURED, by search):**

- **Section 10, item R-4** (lines 2386 to 2389): the list of no-verdict
  cases ("arm F on every seed ...; control 2 on every toy model it applies
  to") can now add the ordinary competing solver, on every seed.
- **Section 11, step 1** (lines 2475 to 2478): "Owed before step 2: the
  competing solver's run under the piece rule, and its check".
- **Section 15, item 29** (lines 3318 to 3324) and its closing sentence
  ("follows the checks owed on this version, the competing solver's run").
- **Section 17** (lines 3735 to 3737, "The competing solvers' figures were
  taken before the piece rule") and the closing paragraph (lines 3864 to
  3869, "What this pass leaves open").
- **Section 19, item 7** (lines 4035 to 4053) and **"What this version does
  not do"** (lines 4215 to 4217).
- **Section 6.4, item 3**, the reason given for the no-transplant formula
  (lines 1178 to 1183: "because an untransplanted model lands on the donor's
  answer only by erring onto exactly that one of the seven other slots"),
  which the solver's question 3 is about.

### 6.2 The control's findings, section 6

| Claim | Right? |
|---|---|
| **Section 7.3, item 2, "What is reported"** (lines 1781 to 1786): the code now does it | **Right**, and section 5.1 above confirms it |
| **The same item's bullet "The part of its code after the floor has run once, and that run is NOT A RESULT"** (lines 1810 to 1829): should name this run as well as the earlier one | **Right** |

**The passage the control's findings did not name, and the one that matters
most (MEASURED, by search; the session could not have known, because the
ruling that makes it wrong came after its branch was cut):**

- **Section 7.3, item 2, the bullet "Twenty random pieces, not one"**
  (lines 1830 to 1837): "That is a change to the control's code, owed with
  the registered measurement, so the code path that ran once on 2026-10-03,
  with a single random piece, is not quite the one registered." John's
  ruling on the check's questions (ruling 1) says the change is made
  *before* the registration review, and names these lines. After this pull
  request the sentence is wrong twice: the change is made, and the code path
  that ran is the one with twenty pieces.

**Also not named:** section 10's paragraph on the seven controls (lines
2445 to 2453, "the part of its code after the floor has run once, in a run
labelled NOT A RESULT"), which needs the same update as lines 1810 to 1829;
section 17's closing paragraph (lines 3864 to 3869), which lists "control
2's twenty random pieces" as code still owed; the section 9 row for control 2
(line 2265), whose citation for the twenty is record A only; and section 19,
item 5 (lines 4009 to 4018), which can say the change has been made and the
code test re-run.

---

## 7. What needs changing in version 4 for the registration text

By section and line, at `7a55fe0`. For whoever writes the registration text;
this check edits nothing.

| Where | Lines | What changes | Why |
|---|---|---|---|
| Header, item 2 | 21 to 25 | The run is done and checked; say what came back in one sentence, or remove the item | Pull request 88 and this check |
| Section 6.4, item 3 | 1178 to 1183 | After "because an untransplanted model lands on the donor's answer only by erring onto exactly that one of the seven other slots", add that this assumes wrong answers spread evenly; a model that confuses owners lands on the donor's value more often (on the toy's competing solver about twice the formula), and the rule then withholds the reading, which is the intended outcome | The solver's question 3; table 3.3 of its findings |
| Section 7.3, item 2, "has run once" bullet | 1810 to 1829 | Name the second code test (pull request 89, `out-control-2-twenty-draws/`, NOT A RESULT) beside the first, with its figures: real figure 0.0012; twenty pieces middle 0.0037, 95th percentile 0.0052; 0 below, 1 equal, 19 above. Keep "not a pass or a fail of anything" | Ruling 5; pull request 89 |
| Section 7.3, item 2, "Twenty random pieces, not one" | 1830 to 1837 | Replace "owed with the registered measurement, so the code path that ran once ... is not quite the one registered" with: the change is made, in `src/control2_twenty_draws.py`, and its code test was run before the registration review. Cite the check-questions ruling 1 | That ruling names these lines |
| Section 7.3, the last paragraph | 1996 to 2017 | Replace "has not yet been measured ... This version quotes no figure for it ... until then this text does not go to the registration review" with the result: no verdict on every seed, under both readings of the solver; the reason (no site set cleared the floor at nomination); the read's best piece 20 to 25 of 180; the no-transplant rule failed on every seed; and that with the channel removed this follows from the pairing alone, so the reading with the channel left on is the informative one. Cite the findings and this check | Pull request 88 |
| Section 7.5, item 4, and the matching lines in 7.4 and section 9 | 2105 to 2108; 2072 to 2076; 2276 | Name how the band is computed: the Wilson interval at 95 percent, as the competing-solver run computes it. Ruling 4 says "the band that sampling alone would put around it" and names no method | Section 4.2 above |
| Section 8.1, reference points | 2178 to 2187 | Replace "to be put through the nomination under it before the registration review" with the result, and keep the solvers as references: **say that the gate does not apply to them** | Section 5.3 above |
| Section 9, control 2 row | 2265 | Cite record B, ruling 5, and the check-questions ruling 1 beside record A | Both records stand; the second ruling set the timing |
| Section 10, R-4 | 2386 to 2389 | Add the competing solver to the no-verdict cases | Pull request 88 |
| Section 10, R-5 | 2391 to 2396 | "Exercised under the piece rule, 2026-10-03, and checked" with a pointer | Pull request 88 and this check |
| Section 10, R-6 | 2397 to 2399 | "kept off zero by the whole-state floor" becomes "kept off zero by the whole-state floor together with the gate and the no-transplant rule", with one sentence: on the toy's competing solver, which fails the gate, the floor was cleared on fresh episodes with a divisor of one or two episodes in 800 | Section 5.4 above |
| Section 10, the paragraph on the seven controls | 2445 to 2453 | As for lines 1810 to 1829 | Pull request 89 |
| Section 10, "What happens next"; section 11, step 1 | 2455 to 2458; 2475 to 2478 | Move the competing solver's run and its check from "owed" to done | Pull request 88 and this check |
| Section 13, weaknesses | (new) | One weakness, if John agrees (question 7 in section 9 below): the toy's ordinary competing solver fails the task, so its no verdict shows the measure returns nothing on a model that has not learned the task, not on one that solves it by a different route | Section 9, question 7 |
| Section 15, item 29; section 17; section 19, items 5 and 7; section 20; closing | 3318 to 3324; 3735 to 3737; 3864 to 3869; 4009 to 4018; 4035 to 4053; 4161 to 4162; 4190 to 4193; 4215 to 4217 | Each says the run, the control's code change, or both are owed; each becomes done, with a pointer | Pull requests 88 and 89 |

**Not to change:** nothing in either pull request touches a registered
number. No floor, bar, count or site list moves.

---

## 8. What this session did not do

- It did not edit pull request 88 or 89, version 4, any ruling file,
  `STATUS.md` or `data/project.toml`.
- It did not read version 4 through end to end; the passages in section 6
  were found by search and read with their sections.
- It did not run either piece of code on any model the runs did not use, did
  not run the `--smoke` paths, and did not re-run the earlier code test (it
  compared against that test's committed output).
- It did not compute, at the 33 site sets that cleared the floor on fresh
  episodes, what the reading would have been at each one; the run does not
  save the fresh-episode grid, and section 5.4 relies on the summary the run
  does save.
- It did not check the controls re-run, the short pre-stated run or the
  repairs, beyond reading the functions these two runs import.
- It put no question to John in chat and read no transcript of another
  session.

---

## 9. The questions for John

Not asked in chat; for the coordination session that routes rulings, one
session at a time.

### 9.1 The five the two findings put

**The solver's question 1: which reading of the solver the registration
cites.** *Their suggestion:* the channel removed as the primary, because
that is how the solver was trained and scored; the channel left on stated
beside it, because with the channel removed the no verdict follows from the
pairing alone. **Follows from the evidence.** With the channel removed the
twins' states were identical to the last bit on every seed (section 4.1), so
every transplant is a null transplant and that reading cannot return
anything but no verdict. *Addition:* the registration should say in so many
words that the primary reading's no verdict is a property of the pairing,
not evidence about the measure, and that the channel-left-on reading is the
one that tests the measure.

**The solver's question 2: whether the registration says what actually
stops this solver.** *Their suggestion:* one sentence, that the solver's no
verdict comes from the gate on learning, the piece rule and the
no-transplant rule, each with room to spare, and that the floor is close to
zero for a model near chance. **Follows in part; the gate needs rewording.**
The piece rule (best 20 to 25 of 180 against 144) and the no-transplant rule
(missed by 0.11 to 0.14 against 0.018) are right. The gate is not applied to
competing solvers in version 4 (section 5.3). *Suggested sentence instead:*
"On the toy, the ordinary competing solver returned no verdict because no
site set cleared the floor at nomination; behind that, its best piece missed
the piece rule by 119 or more of 180 and its untouched rate missed the
no-transplant rule by 0.11 or more, and it would have failed the gate on
learning had it been gated as the free model is. For a model near chance the
floor itself is close to zero and is decided by one or two episodes."

**The solver's question 3: the no-transplant formula on a solver that cannot
tell owners apart.** *Their suggestion:* report only; the rule withholds a
reading here, which is the right outcome, but the registration should not
describe the formula as a property of every model. **Follows.** The untouched
rate (0.22 to 0.25) sits close to the solver's own accuracy (0.22 to 0.24),
which is what a solver choosing among the four agents' values would show;
the donor's value is one of those four. The wording change is in section 7
above, at lines 1178 to 1183.

**The control's question 1: which file is the registered control 2.**
*Their suggestion:* the registration names `control2_twenty_draws.control2`
as control 2's code and says `rerun_controls.control2` is the earlier
version, kept as the record of what the re-run did. **Follows.** The new
function is the old one with only the ruled change (section 5.1), and the old
one still carries the pass line John withdrew. *Addition:* the registered
code for the full-size run is still to be written (section 11, step 3 of
version 4); it should take control 2 from the new function, so that there is
one control 2 at registration and not two.

**The control's question 2: whether the 95th percentile of twenty is the
right summary.** *Their suggestion:* leave it as ruled, and print the twenty
as well. **Follows.** With twenty draws the 95th percentile is a mix of the
two largest (here 0.0052, between 4 and 7 episodes of 800, which no single
draw can equal); control 3 has the same property and was ruled that way.
Printing the twenty, as the code does, lets a reader see the spread.

### 9.2 Two that this check raises

**6. The solver run's explanation, before it is quoted.** Section 4 of the
solver's findings, its question 2 and pull request 88's description say the
gate on learning is the first thing holding the solver back, on the ground
that "a model that fails the gate is not read at all". Version 4 does not
gate the competing solvers (section 5.3). *Suggestion:* the running session,
or the session that writes the registration text, corrects those three
places to "would fail the gate if it were gated as the free model is" before
any of it is quoted; no re-run, and no change to any rule. This is a wording
question, and it goes to John only because pull request 88 is his to merge.

**7. What the competing-solver run can and cannot show.** The toy's ordinary
competing solver fails the task: it is right about one time in four, the
rate of a solver that cannot tell whose value it needs. So its no verdict
shows that the measure returns nothing on a model that has not learned the
task. It does not show what the measure does on a model that *does* the task
by a route other than tracking whose turn it is, which is the harder test of
"satisfied by the wrong thing". The toy has no such model: the name-only
solver is computed from the episodes and has no states to transplant
(`training.name_only_solver`). *Suggestion:* no new run before the
registration review. Add one weakness to section 13 of the registration text
saying this in two sentences, so a reviewer finds it stated rather than
finding it. *Strongest alternative:* build a competing solver that learns
the task from another cue (for example, a model fed the name token at every
turn) and put it through the measure before the review; that is a training
run, not $0 work on committed files, and would move the timeline.
