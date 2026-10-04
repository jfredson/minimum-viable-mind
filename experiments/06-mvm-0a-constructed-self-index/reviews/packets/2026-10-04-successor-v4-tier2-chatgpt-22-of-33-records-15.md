*This is file 22 of 33 of one review packet, pasted into a single conversation. It contains record 15 part 2 of 3 (the check of the competing-solver run and the twenty-piece control). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 15 of 25, part 2 of 3 - the check of the competing-solver run and the twenty-piece control - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md` (complete file, 42,479 characters) =====
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

===== END OF RECORD 15, part 2 =====

