# Check of the rehearsal repairs — re-run from the committed code, and the rulings read against it

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1c repairs
check", on branch `worktree-w1c-repairs-check`, cut from main at `a96f873`. The
file keeps the name the session prompts give it (`docs/weekend-1-session-prompts.md`
on branch `worktree-w1c-rehearsal-repairs`, section (c), checker prompt): the
date in the name is the Saturday it was planned for; the work ran on the Friday
evening.*

*This session did not write what it checks. The target is branch
`worktree-w1c-rehearsal-repairs` at commit `e0626b2` (pull request 52), the
Weekend 1 rehearsal repairs, written by the session "MVM W1c rehearsal
repairs". Its findings are `docs/2026-09-26-rehearsal-repairs.md`, its method
note `docs/rehearsal-repairs-method-2026-09-25.md`, and its outputs
`experiments/rehearsal-successor-measure/out-repairs/`, all on that branch and
none of them on main yet. Every path below that starts `out-repairs/` means that
folder at `e0626b2` unless it says "re-run".*

*Every finding is labelled **MEASURED** (a command was run and its output is
printed here) or **ARGUED** (reasoning a reader can dispute). Filed under this
experiment's reviews directory because the successor measure is the next thing
this experiment registers. Nothing was rented, no vendor was contacted, nothing
was spent: $0. Written under the workspace plain-language rule.*

*An interim version of this file, without section 3 or section 5.1, was
committed first at `09c91cb`, before the re-run finished, so that the checks
already done could not be lost. This version completes it.*

*The brief asked for this session's table to be pasted "beside the findings'
tables in `docs/2026-09-26-rehearsal-repairs.md`". That file is another
session's filed findings, on another open pull request, and the protocol's Filing
rule says findings are "never edited after filing". So the side-by-side tables
are here, in section 3.3, with the findings' figure and the re-run's in adjacent
columns. The findings file is untouched.*

## Verdict

- **Every verdict the findings draw reproduces from the committed code.**
  MEASURED, section 3. Neither training redesign clears the named-other bar (0
  of 3 seeds each), the unchanged recipe clears on 1 of 3, and arm M passes
  page 5's line (0.52 to 0.53, inside the findings' 0.48 to 0.53). Arm T reads
  0.0000 exactly, arms C and F read at the entangled end, the free arm fails the
  learn-both gate, and control 2 gives no verdict on arms T, C and M. Every
  figure on arm T comes back to the last decimal.
- **The decimals on arms C, F and M do not reproduce, as the 2026-09-23 ruling
  expects.** Three statements the findings make about the procedure are
  properties of one training run. MEASURED, section 3.3: the degenerate
  all-positions site set lands on arm F seed 0 here, not arm C seeds 0 and 1;
  the two readings of "smallest" disagree on 6 of 12, not 7; and control 2
  passes on 2 free-arm seeds, not 3. Arm C reads up to 1.0078 and the free arm
  up to 1.0057, outside the ranges printed.
- **Commit order confirmed.** MEASURED, sections 1 and 2: the method note
  precedes all output, and both additions not pre-stated were committed as
  code before their output was produced (by about nine seconds in one case).
- **Three errors against the committed files themselves.** MEASURED, section 4:
  "7 of 12" is 8 of 12; arm M's rider "no verdict" is a floor miss with about
  0.41 moved, not "nothing moves"; and two seeds are transposed in one table.
- **The ruling of 2026-09-25 is not only the findings' numbers.** MEASURED,
  section 5. $161.90 cites a file that is not on main (pull request 51), "about
  $434" is the top of $422 to $434, "7 of 12" and "within 0.04" are wrong, and
  its item 3 prints site counts (296, 1,816) that its own widened exclusion
  changes (to 240 and 1,456 with the toy's position sets).
- **No ruled choice is undermined by the re-run; four sentences of the ruling
  should be annotated.** ARGUED, section 5.1.
- **Carried forward, not new:** the free arm's ownership read is near chance
  on both runs, so its "entangled end" reading cannot be told apart from a read
  that found nothing. ARGUED from MEASURED fits, section 4.4.

---

## 0. Words used here, once

- **Arm**: one of the four small trained models the rehearsal compares. **Arm
  T** is built so the answer to "whose value do I act on?" sits in one separate
  slot (built to be separable, and so it should read 0 on the measure). **Arm C**
  is built so that answer is mixed into everything (built to be entangled; it
  should read near 1). **Arm F**, the free arm, is trained with no such
  construction. **Arm M**, the fourth arm new in the repairs, sends some actions
  through arm T's route and some through arm C's, so it should read in the
  middle.
- **Own-directed** and **named-other**: the two kinds of action turn. On one the
  model acts on its own assigned value; on the other it acts on the value of an
  agent named by a marker word.
- **Learn-both gate**: the ruled check that an arm answers both kinds of turn
  better than one in four, here 790 or more correct of 3,000 held-out episodes.
- **Transplant**: copying part of the model's running internal state from a
  "donor" episode into a "recipient" episode and seeing whether the action
  follows the donor. **Whole-state** copies everything at the chosen places;
  **ownership-only** copies only the directions a straight-line read picked out
  as carrying "which agent is me".
- **The reading** (the ruled "chance-corrected" form): how much of the whole-state
  transplant's effect is *not* carried by the ownership-only transplant, on a
  scale where 0 means "all of it is in the ownership directions" (separable) and
  1 means "none of it is" (entangled).
- **Site set**: a choice of layers and token positions at which to transplant.
  **Nomination**: the one ruled rule that picks a site set and a rank (how many
  directions) for each arm and seed from development episodes.
- **The rider**: John's addition, reading every arm at arm T's site set as well
  as at its own.
- **Control 2**: the check that transplanting a *named* agent's representation
  leaves the *own-directed* action alone.

---

## 1. The method note precedes the first output commit — confirmed

MEASURED:

```
$ git log --reverse --format='%h %ad %s' --date=iso main..e0626b2
426b6e8 2026-09-25 16:38:35 -0700 Rehearsal repairs: the method, committed before any code or output
16d75f6 2026-09-25 16:40:26 -0700 Rehearsal repairs: training options, the fourth arm, and the driver's train and gate stages
9e341e6 2026-09-25 17:24:23 -0700 Rehearsal repairs: nomination, measure and summary stages (code only, no output)
81dc84d 2026-09-25 18:52:46 -0700 Rehearsal repairs: two additions not pre-stated, both labelled so in the code
004d134 2026-09-25 19:50:04 -0700 Rehearsal repairs: the outputs
e0626b2 2026-09-25 19:53:16 -0700 Rehearsal repairs: the findings
```

and, counting what each commit touches:

```
$ git show --name-only --format='== %h' 426b6e8 16d75f6 9e341e6 81dc84d 004d134 e0626b2 | awk '/^==/{if(h)print h, n" files,", o" in out-repairs/"; h=$2; n=0; o=0; next} NF{n++; if(/out-repairs\//)o++} END{print h, n" files,", o" in out-repairs/"}'
426b6e8 1 files, 0 in out-repairs/
16d75f6 4 files, 0 in out-repairs/
9e341e6 1 files, 0 in out-repairs/
81dc84d 2 files, 0 in out-repairs/
004d134 45 files, 45 in out-repairs/
e0626b2 2 files, 0 in out-repairs/
```

The method note (`426b6e8`) is the first commit on the branch, and the only
commit that adds any output is `004d134`, four commits later. The findings'
section 1 table matches this exactly.

---

## 2. The two additions not pre-stated were committed as code before their output — confirmed, with one caveat

**In git, MEASURED.** Both additions arrive in `81dc84d`, neither is in the
commit before it, and both are labelled in the code:

```
$ git show --stat --format='%h %ad %s' --date=iso 81dc84d
81dc84d 2026-09-25 18:52:46 -0700 Rehearsal repairs: two additions not pre-stated, both labelled so in the code

 .../src/diagnose_named_other.py                    | 79 ++++++++++++++++++++++
 .../rehearsal-successor-measure/src/repairs.py     | 38 +++++++++++
 2 files changed, 117 insertions(+)

$ git grep -c 'pick_without_all_positions\|sensitivity_without_all_positions' 9e341e6 -- experiments/rehearsal-successor-measure/src/ ; echo "exit $?"
exit 1
$ git grep -c 'pick_without_all_positions\|sensitivity_without_all_positions' 81dc84d -- experiments/rehearsal-successor-measure/src/
81dc84d:experiments/rehearsal-successor-measure/src/repairs.py:3
$ git ls-tree --name-only 9e341e6 experiments/rehearsal-successor-measure/src/ | grep -c diagnose
0
$ git grep -n -i 'not pre-stated' 81dc84d -- experiments/rehearsal-successor-measure/src/
81dc84d:experiments/rehearsal-successor-measure/src/diagnose_named_other.py:3:UNREGISTERED, and **not pre-stated**: written after the curriculum runs came
81dc84d:experiments/rehearsal-successor-measure/src/repairs.py:329:    """NOT PRE-STATED. Added 2026-09-25 after the arm C nominations came back
81dc84d:experiments/rehearsal-successor-measure/src/repairs.py:582:            # ------------- sensitivity, NOT pre-stated: no "all" position sets
```

**Caveat, ARGUED.** Git can only show that the code was committed before the
outputs were *committed*. All 45 output files went in together at 19:50. Whether
each addition's code was committed before its output was *produced* is a
question about when the runs happened, which git does not record. The writer's
working folder is still on disk (`.claude/worktrees/w1c-rehearsal-repairs/`, not
committed), so this session read its file times and its run logs, without
touching them. MEASURED, from `ls -la -T` on that folder's `out-repairs/` and
`out-repairs/logs/`:

| output carrying an addition | file written | how long the run took (its log's last line) | so it started about |
|---|---|---|---|
| `diagnose_named_other.json` (the diagnostic) | 19:13:49 | — (a single pass over 3,000 episodes) | well after 18:52:46 |
| `measure_base_T_C.json` (first file with the `sensitivity_without_all_positions` field) | 18:54:20 | 84.6 s (`logs/measure_base_T_C.log`) | 18:52:55 |

So the first run that wrote the sensitivity field started about nine seconds
after `81dc84d` was committed. That is consistent with the findings' claim. It
cannot prove the process loaded the committed version and not an uncommitted
edit made in those seconds. The margin is narrow, but it points the right way.
The same times also bear out the order the findings give for *why* each
addition was written: the curriculum gate (`gate_curriculum.json`, 18:22:07) came
before the diagnostic, and the arm C nominations (`nominate_base_T_C.json`,
18:45:32) came before the sensitivity code.

---

## 3. The re-run from clean

### 3.1 How it was run

`git archive e0626b2` was unpacked into this session's scratch folder, outside
the repository. The committed `out-repairs/` was moved aside to
`out-repairs-committed/`, and every stage ran into an empty `out-repairs/`, from
the committed code, with no checkpoint reused. The writer's checkpoints are
still in its working folder; they were not opened. The order was the writer's
own, read from its logs: two training streams in parallel (stream A the free arm
under all three recipes; stream B arms T, C, M and the ownership-blind solver),
then the three gates, the diagnostic, nomination and measurement for T and C,
then F, then M, then the summary and the five module self-tests. The driver
script is in the appendix. Same laptop, same Python environment
(`~/Code/minimum-viable-mind/.venv`, torch 2.12.1 on the Mac's graphics chip),
on wall power with sleep disabled.

MEASURED, from the driver's log: started 2026-09-25 20:12:39, training done
2026-09-26 00:18:39, everything done 00:58:37. The two training streams took
13,186 and 14,756 seconds of wall time, against the writer's 9,161 and 11,307
(its logs, uncommitted). No stage logged an error. $0.

### 3.2 Per-file

MEASURED: **no output file is byte-identical**. That is expected rather than
telling: every training record holds elapsed seconds, and every gate, nominate
and measure file mixes arms whose training drifts. The self-test record passes
71 checks and fails none, the same count as the committed one. It differs only in
two lines where a warning's source text leaked past the output filter. Arm T's
frozen straight-line reads differ from the committed ones by up to 0.24 in some
coefficient (largest over the 15 arrays in each `reads_T_base_seed*.npz`). Its
weights drift like every arm's, and its outputs still come back exactly,
because it answers 1.0000 and a drifted weight cannot move a saturated answer.
That is the explanation the 2026-09-22 re-run gave, and it holds again.

### 3.3 The figures the brief names, side by side

"Committed" is `out-repairs/` at `e0626b2`, and is also what the findings print
unless section 4 says otherwise. "Re-run" is this session's run. The verdict
column says whether the figure reproduces **exactly**, **as a range** (the
re-run's values fall inside the range the findings quote, or the count or
verdict comes back though the decimals move), or **not at all**. The full
extraction for both folders is in the appendix.

**The named-other condition** (`gate_base.json`, `gate_curriculum.json`,
`gate_reweight.json`; bar 790 correct of 3,000):

| free arm, recipe | committed: named-other, seeds 0 / 1 / 2 | seeds clearing | re-run: named-other, seeds 0 / 1 / 2 | seeds clearing | verdict |
|---|---|---|---|---|---|
| unchanged | 0.3313 / 0.2603 / 0.2487 | **1 of 3** | 0.4080 / 0.2477 / 0.2537 (1,224 / 743 / 761 correct) | **1 of 3** | count **exactly**; decimals not at all; range 0.25 to 0.33 widens to 0.25 to 0.41 |
| curriculum | 0.0773 / 0.1933 / 0.1430 | **0 of 3** | 0.2287 / 0.0773 / 0.0677 | **0 of 3** | count **exactly**; direction (down from unchanged) reproduces |
| re-weighting | 0.2317 / 0.2063 / 0.2377 | **0 of 3** | 0.2407 / 0.2453 / 0.2203 | **0 of 3** | count **exactly**; direction reproduces |
| re-weighting, own-directed | 0.1723 / 0.1700 / 0.1760 | — | 0.1757 / 0.1550 / 0.1717 | — | **as a range** (the collapse to about 0.17 reproduces) |

The diagnostic (`diagnose_named_other.json`) reproduces its pattern but not its
seeds. The unchanged model still most often gives another agent's value in the
right item (0.34 to 0.50). After the curriculum, "gives its own value" is again
more than half on one seed, but on seeds 1 and 2 (0.56, 0.55), not seed 0 (0.06
here). "On seed 0, more than half the time" does not reproduce. "The curriculum
teaches the model to answer with its own value, on some seeds" does.

**Arm M's readings** (`measure_base_M.json`):

| seed | committed: blind reading | formula | miss | re-run: blind reading | formula | miss |
|---|---|---|---|---|---|---|
| 0 | 0.5105 | 0.4895 | 0.0209 | 0.5275 | 0.4871 | 0.0405 |
| 1 | 0.4846 | 0.4572 | 0.0274 | 0.5237 | 0.4829 | 0.0408 |
| 2 | 0.5322 | 0.4904 | 0.0418 | 0.5281 | 0.4752 | 0.0530 |

Verdict: **"0.48 to 0.53" reproduces as a range.** The re-run's 0.5237 to
0.5281 lies inside it. Page 5's pass (0.3 to 0.7), the method note's band (0.30
to 0.60) and its "within 0.10 of the formula" all pass again. **"Within 0.02 to
0.04 of what its construction predicts" does not reproduce**: the re-run misses
by 0.0405 to 0.0530. The blind reading sits above the formula on every seed
again, so the direction reproduces. Arm M passes the learn-both gate again
(own-directed 0.8560 to 0.8650, named-other 0.5573 to 0.5640). The across-seed
spread of its raw difference falls from 0.0309 to 0.0045 (`summary_base.json`).

**The site counts.** 176 is asserted in the code on import and recorded as
`family_size` in every re-run `nominate_base_*.json`: **exactly**. 296 and
1,816 are arithmetic on the rule, not outputs of a run: **exactly** (section 5).

**The two readings of "the smallest layer set that clears it"**
(`nominate_base_*.json`):

| | committed | re-run | verdict |
|---|---|---|---|
| pairs where the two readings pick different site sets | 8 of 12 (the findings say 7; section 4.1) | **6 of 12** | **not at all**. It is a property of each training run, not of the code |
| largest gap in ownership-only share between the two picks | 0.0200 | **0.0233** | "0.0200 apart or less" does **not** reproduce; "about 0.02" does |
| the two forms of the floor disagree | 0 | 0 | **exactly** |
| sets whose positions are all positions, nominated | arm C seeds 0 and 1 | **arm F seed 0** only | the event reproduces; **where it happens does not** |

Re-run nominations, for the record (committed ones in section 4.1):

```
C/base/0   clear 38  nom post-identity L[0] r8        0.5083/0.0550  other post-identity L[1, 2, 3, 4] r2 gap 0.0017  c2 no verdict (0)
C/base/1   clear 35  nom action+3 L[1] r4             0.5583/0.0667  other post-identity L[1, 2, 3, 4] r4 gap 0.0050  c2 no verdict (0)
C/base/2   clear 35  nom action L[3] r4               0.5400/0.0683  other same                         gap 0.0000  c2 no verdict (0)
T/base/0   clear 44  nom action L[0] r8               1.0000/1.0000  other same                         gap 0.0000  c2 no verdict (0)
T/base/1   clear 44  nom action L[0] r8               1.0000/1.0000  other same                         gap 0.0000  c2 no verdict (0)
T/base/2   clear 44  nom action L[0] r8               1.0000/1.0000  other same                         gap 0.0000  c2 no verdict (0)
F/base/0   clear 35  nom all L[0] r4                  0.5850/0.0683  other same                         gap 0.0000  c2 nominated (38)
F/base/1   clear 39  nom post-identity L[0] r8        0.5267/0.0700  other post-identity L[0, 1, 2, 3, 4] r8 gap 0.0033  c2 nominated (40)
F/base/2   clear 32  nom post-identity L[0] r4        0.5150/0.0783  other same                         gap 0.0000  c2 no verdict (0)
M/base/0   clear 35  nom post-identity L[0] r8        0.7633/0.3683  other action L[0, 1, 2, 3, 4] r8   gap 0.0200  c2 no verdict (0)
M/base/1   clear 35  nom post-identity L[0] r8        0.7700/0.3750  other action L[0, 1, 2, 3, 4] r8   gap 0.0150  c2 no verdict (0)
M/base/2   clear 35  nom post-identity L[0] r8        0.7617/0.3650  other all L[1, 2, 3, 4] r8         gap 0.0233  c2 no verdict (0)
readings disagree on 6 of 12; largest ownership-only gap 0.0233; floor-form disagreements 0
family_size 176 label marker-word
```

Arm T's nomination (action position, first layer, rank 8, on every seed)
reproduces **exactly**. So does "one rule, and it no longer picks arbitrarily on
arm T".

**Control 2 as the proposal states it** (`control2` fields):

| arm | committed | re-run | verdict |
|---|---|---|---|
| T | no verdict ×3; fixed-site variant passes | no verdict ×3; fixed-site passes | **exactly** |
| C | no verdict ×3 | no verdict ×3 | **exactly** |
| F | pass ×3 (own-directed moved 0.0075 / 0.0000 / 0.0012) | **pass, pass, no verdict** (0.0025 / 0.0000 / —; seed 2: 0 clearing site sets) | **not at all** as "pass on all three seeds"; "weak where it runs" reproduces (the named-other action itself moved 0.095 and 0.000) |
| M | no verdict ×3 | no verdict ×3 | **exactly** |
| old control 2 on arm T | 0.2512 / 0.2350 / 0.2562 | same | **exactly** (arm T) |

**The measure under the ruled form and numbers** (`measure_base_*.json`,
`summary_base.json`, `gate_base.json`):

| figure | committed | re-run | verdict |
|---|---|---|---|
| arm T reading, every seed | 0.0000 (untouched 0.0000, whole 1.0000, ownership-only 1.0000) | the same | **exactly** |
| arm C reading | 0.9927 / 0.9977 / 1.0000 ("0.99 to 1.00") | 1.0000 / 0.9952 / **1.0078** | **as a range and a direction** (entangled end) but **not** as "0.99 to 1.00": one seed reads above 1 |
| arm F reading | 1.0029 / 1.0000 / 1.0000 ("1.00 to 1.003") | 1.0000 / 1.0028 / **1.0057** | **as a direction** (entangled end); the upper bound 1.003 does not hold |
| every reading valid under the floor | yes | yes | **exactly** |
| separation, arm C minus arm T, above 0.5 on every seed | 0.9977 / 0.9927 / 1.0000 | 1.0000 / 0.9952 / 1.0078 | the verdict **exactly** |
| arm T learn-both gate, including lesioned own-directed 0.2467 / 0.2510 / 0.2733 | passes | same figures | **exactly** |
| name-only solver | 0.2380 own, 1.0000 named-other | same | **exactly** |
| free arm fails learn-both | fails (named-other 1 of 3) | fails (1 of 3) | **exactly**, as a verdict |
| free arm lesion collapses on all three seeds | yes | yes (0.1627 / 0.1860 / 0.1823) | **exactly**, as a verdict |
| arm C learn-both | fails, named-other 0 of 3 | fails, 0 of 3 (0.2487 / 0.2440 / 0.2547) | **exactly**, as a verdict |
| across-seed spread of raw difference, C / F / M | 0.0466 / 0.0499 / 0.0309 | 0.0369 / 0.0571 / 0.0045 | **not at all**, as decimals |
| rank cap 8 binds on T and M on every seed | yes | yes | **exactly** |
| rider: C and F no verdict with whole-state equal to untouched | yes | yes | **exactly**, as a verdict |
| rider: arm M no verdict, whole-state about 0.41 against about 0.01 | 0.41 / 0.0125–0.0175 | 0.4075–0.4138 / 0.0112–0.0175 | **as a range**; section 4.2's point reproduces |
| control 1 on C / F / M | 0.50–0.57 / 0.49–0.56 / 0.36–0.42 | 0.51–0.58 / 0.51–0.60 / 0.40–0.42 | **as a range**, slightly wider |
| control 4 on C (the "worth a second look") | 0.14 to 0.16 | 0.1537 / **0.0563 / 0.0688** on seeds 0 / 1 / 2, against untouched rates of 0.0625 / 0.0587 / 0.0650 | **not at all** on two seeds of three. It tracks where the rule looks, as the findings guessed |
| control 6a (same-value cell moved) C / F / M | 0.59–0.72 / 0.64–0.74 / 0.17–0.32 | 0.47–0.67 / 0.62–0.74 / 0.21–0.27 | **as a range** for F and M; C's lower end moves to 0.47 |
| control 7 (null transplant bit-identical) | yes on every arm | yes | **exactly** |

**In one line, ARGUED on the tables above.** Every verdict the findings draw
reproduces: no redesign passes, arm M passes, arm T reads 0.0000, the free arm
fails its gate. So does every figure on arm T and every count on arm T or on
the gates' pass lines. What does not reproduce is the particular decimal or
seed on the three arms whose training drifts. That includes three numbers the
findings state as facts about the procedure: which arm and seed got a
degenerate site set, "7 of 12", and control 2 passing "on all three seeds" on
the free arm. The 2026-09-23 range-and-direction ruling already covers arms C
and F. It should cover arm M, and every count taken over the nominations, too.

---

## 4. The findings against their own committed files

Before comparing against a fresh run, every figure under check was read out of
the committed files at `e0626b2` by one script, which prints them from any
`out-repairs` folder. The script and its full output are in the appendix. Every
figure the brief lists matches the committed files except where this section says
otherwise.

**4.1 "The two readings disagree on 7 of the 12 arm-and-seed pairs" — the files
say 8. MEASURED.** The findings' own table in section 3 lists a different pick
in its last column on arm C seeds 1 and 2, arm F seeds 0, 1 and 2, and arm M
seeds 0, 1 and 2. That is eight rows, and the committed files agree:

```
$ .venv/bin/python $JOB/check_nominate.py $JOB/rerun/experiments/rehearsal-successor-measure/out-repairs-committed
  # $JOB is this session's scratch folder; out-repairs-committed is out-repairs/ at e0626b2, moved aside
  # before the re-run (section 3). Script in the appendix.
C/base/0   clear 38  nom all L[0] r2                  0.5867/0.0550  other same                         gap 0.0000  c2 no verdict (0)
C/base/1   clear 35  nom all L[0] r4                  0.6033/0.0567  other post-identity L[0, 1, 2, 3, 4] r8 gap 0.0067  c2 no verdict (0)
C/base/2   clear 38  nom post-identity L[0] r2        0.5300/0.0550  other post-identity L[0, 1, 2, 3, 4] r2 gap 0.0050  c2 no verdict (0)
T/base/0   clear 44  nom action L[0] r8               1.0000/1.0000  other same                         gap 0.0000  c2 no verdict (0)
T/base/1   clear 44  nom action L[0] r8               1.0000/1.0000  other same                         gap 0.0000  c2 no verdict (0)
T/base/2   clear 44  nom action L[0] r8               1.0000/1.0000  other same                         gap 0.0000  c2 no verdict (0)
F/base/0   clear 35  nom post-identity L[0] r2        0.4883/0.0633  other post-identity L[1] r1        gap 0.0000  c2 nominated (38)
F/base/1   clear 35  nom action+3 L[1] r4             0.5533/0.0500  other all L[1, 2, 3, 4] r8         gap 0.0033  c2 nominated (38)
F/base/2   clear 35  nom post-identity L[0] r1        0.4933/0.0700  other post-identity L[1] r8        gap 0.0033  c2 nominated (40)
M/base/0   clear 35  nom post-identity L[0] r8        0.7900/0.3683  other post-identity L[2] r8        gap 0.0200  c2 no verdict (0)
M/base/1   clear 35  nom action L[3] r8               0.7250/0.3783  other post-identity L[1] r8        gap 0.0167  c2 no verdict (0)
M/base/2   clear 35  nom post-identity L[0] r8        0.7717/0.3700  other post-identity L[0, 1, 2, 3, 4] r8 gap 0.0100  c2 no verdict (0)
readings disagree on 8 of 12; largest ownership-only gap 0.0200; floor-form disagreements 0
family_size 176 label marker-word
```

("Other" is the file's `sensitivity` field, the other reading of "the smallest
layer set that clears it". "Gap" is the difference in ownership-only share
between the two picks.) One possible source of the 7: on arm F seed 0 the two
picks differ in site set but reach the same ownership-only share, a gap of 0.0000.
Counting only the pairs whose shares differ also gives 7, but that is not what
the sentence says. The findings' other two claims in that bullet hold on the
committed files: the largest gap is 0.0200, and the two forms of the floor never
disagree (0). The ruling repeats the 7 (section 5 below). On the re-run the
count is 6 of 12 and the largest gap 0.0233 (section 3.3), so no exact count
here is a property of the code.

**4.2 Arm M at arm T's site set: something does move there. MEASURED, then
ARGUED.** The findings' rider paragraph says "at the first layer, at the action
position, nothing about ownership has yet reached the running state of arms C,
F or M … so copying the donor's state there changes nothing." For arms C and F
the files bear this out: the whole-state transplant equals the untouched rate on
every seed. For arm M they do not, from `measure_base_M.json`, field
`rider_at_arm_T_site_set`:

```
[5] rider at arm T's site set: status, whole/untouched
  C no verdict 0.0512/0.0512  no verdict 0.0488/0.0488  no verdict 0.0600/0.0600
  F no verdict 0.0587/0.0587  no verdict 0.0563/0.0563  no verdict 0.0688/0.0688
  M no verdict 0.4088/0.0125  no verdict 0.4138/0.0175  no verdict 0.4100/0.0138
```

On arm M the whole-state transplant at arm T's site set moves the action in
about 0.41 of trials against about 0.01 untouched. Arm M returns "no verdict"
because 0.41 falls short of the four-fifths floor, not because nothing moves.
ARGUED: that is what arm M's construction predicts. About two fifths of its
actions go through arm T's slot, which the action position at the first layer
does carry. The rider's "no verdict" therefore means two different things on
the three arms, and the ruling's sentence on the rider (section 5) describes only
one of them.

**4.3 Two transcription slips, MEASURED.**

- Section 2's table gives the re-weighted free arm's own-directed accuracy as
  0.1700 / 0.1723 / 0.1760 for seeds 0 / 1 / 2. `gate_reweight.json` has
  0.1723 / 0.1700 / 0.1760, so seeds 0 and 1 are swapped. It moves no
  conclusion.
- Section 0 says arm M reads "within 0.02 to 0.04 of what its construction
  predicts". Section 5 gives the misses as 0.021, 0.027 and 0.042, which the
  file bears out (0.0209, 0.0274, 0.0418; `measure_base_M.json`,
  `reading.degree` against `fourth_arm.predicted_from_route_accuracies`). So
  the largest miss is just over 0.04. The pre-stated pass was "within 0.10",
  which holds either way.

**4.4 The free arm's ownership read found almost nothing, as on 2026-09-21. ARGUED
from MEASURED fits.** The findings don't say so. The straight-line read for
"which marker word is the model's own" is fitted on held-out development
episodes, where chance is one in twelve (about 0.083; twelve marker words in
the development pool, `src/grammar.py`, `POOLS`). Its held-out fit accuracy, per
layer 0 to 4, from the `fit_accuracy.own` fields of the committed
`nominate_base_*.json`:

```
  C/base/0 {'0': 0.072, '1': 0.994, '2': 1.0, '3': 1.0, '4': 1.0}
  C/base/1 {'0': 0.072, '1': 0.983, '2': 0.967, '3': 0.983, '4': 0.961}
  C/base/2 {'0': 0.072, '1': 0.978, '2': 0.983, '3': 1.0, '4': 1.0}
  F/base/0 {'0': 0.072, '1': 0.172, '2': 0.144, '3': 0.106, '4': 0.067}
  F/base/1 {'0': 0.072, '1': 0.067, '2': 0.117, '3': 0.144, '4': 0.117}
  F/base/2 {'0': 0.072, '1': 0.106, '2': 0.139, '3': 0.111, '4': 0.111}
  M/base/0 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 0.989, '4': 0.989}
  T/base/0 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
```

(Arm M seeds 1 and 2 and arm T seeds 1 and 2 are 1.0 or 0.989 at every layer.)
The re-run gives the same picture (its `nominate_base_*.json`): the free arm
fits at 0.072 to 0.161 at every layer on every seed, and arm C at 0.961 to 1.0
from layer 1 on.
On arm C the read recovers the label almost perfectly, and the ownership-only
transplant still moves nothing: that is entanglement actually shown. On the free
arm the read is near chance at every layer. Its ownership-only transplant then
does what a random subspace does: 0.056 to 0.069, against control 3's 0.059 to
0.071, from the findings' own section 6 tables. So the free arm's reading "at
the entangled end (1.00 to 1.003)" cannot be told apart from "the read found
no ownership directions to transplant". The 2026-09-21 review raised exactly
this, as its "third reading" of the free arm
(`reviews/2026-09-21-successor-measure-rehearsal-claude-worktree.md`, section 6,
can-follow item 7), from the same fits in the old record (`out/nominate.json`:
0.072 to 0.144 on the free arm). The repairs neither address it nor mention it.
It bears on no ruling of 2026-09-25, because the free arm fails the learn-both
gate and would not be read. It will bear on the registered free arm, which is
the one arm whose answer is not known in advance.

---

## 5. John's rulings on the findings, read against them

The file is `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` on branch
`rulings-2026-09-25-repairs` (commit `e03288c`, pull request 53, open). It says of
itself: "Every number below is the findings file's". This section checks that
sentence number by number. It does not edit the ruling; anything to change is
listed for an annotation beside it.

MEASURED, each row checked against the findings file at `e0626b2` and the
committed output it cites (section 4 and the appendix):

| the ruling says | is it the findings'? | does the committed output bear it out? |
|---|---|---|
| curriculum 0 of 3, re-weighting 0 of 3, unchanged recipe 1 of 3 | yes, section 2 | yes (`gate_curriculum.json`, `gate_reweight.json`, `gate_base.json`: 0, 0 and 1 seeds with 790 or more correct) |
| arm M 0.48 to 0.53 on all three seeds | yes, sections 0 and 5 | yes (0.4846, 0.5105, 0.5322) |
| "within 0.04 of its construction's prediction" | nearly: section 0 says "0.02 to 0.04" | **no, by a hair**: the largest miss is 0.0418 (section 4.3) |
| $450 envelope | from the Weekend 1 queue ruling, page 6 (`docs/rulings/2026-09-26-weekend-1-queue.md`), which the findings quote | not a findings figure |
| three runs at "$32 to $44" | yes, section 5, quoting page 6 of the queue ruling | not a findings figure; its source is the queue ruling, line 119 |
| $161.90 for the two releases | **no**. Cited to `docs/2026-09-25-rented-slice-attempt-2-findings.md`, which is **not on main**: it exists only on branch `worktree-mvm-w1f-rented-slice-attempt-2` (commit `7da1946`, pull request 51, open) | that file's section 7 does give $161.90 |
| "about $434 of $450" | **no**. Computed in the ruling itself | only at the top of the range. From that file's "about $60.0" left of $450 after both releases, adding arm M gives $422 at $32 or $434 at $44 (command below) |
| arm C seeds 0 and 1 picked an all-positions set | yes, section 3 | yes (section 4.1 table) |
| 296 on the toy, 1,816 on the 12-layer model | yes, section 3 | yes, as arithmetic (command below). **But see the argued point after this table** |
| "the packet's 176 was hand arithmetic" | the findings say the 176 "comes from the rehearsal's nine hand-listed layer sets" | the 176 is the size of the family that was actually run, asserted in code (`repairs.py`: `assert len(SITE_SETS) == 44 and FAMILY_SIZE == 176`) and recorded in every `nominate_base_*.json`. "Hand-listed", not "hand arithmetic" |
| "differed on 7 of 12 arm-and-seed pairs by 0.02 or less" | yes, section 3 | **no: 8 of 12** (section 4.1). "0.02 or less" holds |
| control 2 cannot run on arms T and M; no verdict where the named-other condition is unlearned | yes, section 4 | yes: no site set clears on T, C or M for any seed; F nominates |
| a reading above 1.0 is reported as observed | yes, section 6.2 | yes (arm F seed 0 1.0029; arm C sensitivity seed 0 1.0051) |
| the rider returns "no verdict" "where the whole-state transplant moves nothing at arm T's site set" | the findings' wording | **not for arm M**: there the whole-state transplant moves about 0.41 and fails the floor (section 4.2) |

The money arithmetic, MEASURED:

```
$ python3 -c "
committed = 450 - 60.0   # attempt-2 findings section 7: both releases leave about \$60.0 of \$450
print('spent plus both releases:', committed)
for m in (32, 44): print(f'plus arm M at \${m}: {committed + m:.1f} of 450')
"
spent plus both releases: 390.0
plus arm M at $32: 422.0 of 450
plus arm M at $44: 434.0 of 450
```

The site counts, MEASURED, including what the ruling's own widened exclusion
gives:

```
$ python3 -c "
def contiguous(n): return [tuple(range(a,b+1)) for a in range(n) for b in range(a,n)]
for name,n in (('toy, 5 states',5),('registered, 13 states',13)):
    c=len(contiguous(n))
    print(f'{name}: contiguous layer sets {c}; as ruled on page 1e (less every-layer-at-every-position) {(c*5-1)*4}; widened exclusion (no set spanning every position) {(c*4)*4}')
"
toy, 5 states: contiguous layer sets 15; as ruled on page 1e (less every-layer-at-every-position) 296; widened exclusion (no set spanning every position) 240
registered, 13 states: contiguous layer sets 91; as ruled on page 1e (less every-layer-at-every-position) 1816; widened exclusion (no set spanning every position) 1456
```

**Item 3 of the ruling is inconsistent with itself. ARGUED, on the arithmetic
above.** The item widens the exclusion to "any site set that spans every
position at any layer". In the next sentence it gives the site count as "296 on
the toy, 1,816 on the registered 12-layer model". Those are the counts under the
*old*, narrow exclusion. The findings warned of exactly this ("if every
all-positions set is excluded, as argued above, the counts change again"). With
the toy's five position sets and the widened exclusion, the counts are 240 and
1,456 — if the toy's five position sets are kept and only the "every position"
set counts as spanning every position. Neither assumption is settled: the
findings pointed out that the ruled position clause does not say how positions
are grouped into sets, and that two of the toy's five ("after identity" and
"every position") reach outside it. So the true count depends on the position
list the registration prints.
The ruling's own principle, "the site count is the rule's output", is sound. The
two numbers printed beside it are the wrong outputs.

### 5.1 Does anything the re-run moved bear on a ruling?

ARGUED, on the section 3 tables. No ruled *choice* is undermined. Four sentences
of the ruling state as fact something the re-run shows is a property of one
training run. The ruling says of itself that "if that check moves a number
above, the ruling is re-read against the checked figure and this file is
annotated, not rewritten". These are the four places to re-read.

| ruling item | what the re-run moved | bears on the choice? | bears on the wording? |
|---|---|---|---|
| 1, the named-other condition | nothing that matters: 1, 0 and 0 seeds of 3 clear again | no | no |
| 2, arm M folded in | readings 0.5237 to 0.5281, inside 0.48 to 0.53; the pass reproduces | no | **yes**: "within 0.04 of its construction's prediction" fails on the re-run (misses 0.0405, 0.0408, 0.0530), and on the committed run by a hair (0.0418). "Within about 0.02 to 0.05, inside the pre-stated 0.10" is what both runs support |
| 3, widened exclusion | the degenerate all-positions pick lands on arm F seed 0, not arm C seeds 0 and 1 | no. It **strengthens** the reason: the rule picks such a set on a second arm in a second run | **yes**: "the rule nominated such a set on arm C, seeds 0 and 1" is true of one run only. And, independent of the re-run, the counts 296 and 1,816 do not survive the item's own widening (section 5 above) |
| 4, which reading of "smallest" | the two readings disagree on 6 of 12, largest gap 0.0233 | no. The choice rests on the ruled words, not on the count | **yes**: "7 of 12 … by 0.02 or less" is 8 of 12 on the committed run and 6 of 12 by up to 0.0233 on this one. "About half the pairs, by about 0.02" survives both |
| 5, control 2 | on the free arm, pass on 2 seeds and no verdict on 1 (was pass on 3) | no. The ruling already carries arms C and F as a reported check, run only once they have learned the named-other condition | no. The ruling's sentences on arms T and M reproduce exactly |
| also ruled: a reading above 1 reported as observed | three readings above 1 now (1.0078, 1.0028, 1.0057) | no. It makes the ruling matter more | no |
| also ruled: the rider stays in the table | arm M's 0.41 moved at arm T's site set reproduces | no | **yes**, as section 4.2 says: "no verdict where the whole-state transplant moves nothing" misdescribes arm M on both runs |

---

## 6. The failure-mode pass

The pass is owed to registration text at Gate A. Neither the findings nor the
ruling is registration text yet, but both are about to be built into version 2
of the successor proposal, so each failure on the list is run here where it can
be run cheaply.

1. **A comparison whose denominator was zero. MEASURED, does not fire.** The
   reading's denominator is the floor's required room, four fifths of (the arm's
   accuracy minus the untouched rate). Smallest per arm across the three seeds,
   from the committed `measure_base_*.json`, field `reading.floor.required_room`:
   T 0.8, C 0.394, F 0.39, M 0.686. None is zero. The top of the scale does move
   between arms (that is what the floor is relative to), which is the ruled
   design, not a defect found here.
2. **A probe target that cannot be recovered in principle. MEASURED, fires on one
   arm.** On the free arm the marker-word read fits near chance at every layer
   (section 4.4). The target is recoverable on arms T, C and M, so the instrument
   works where the answer is known. On the free arm, the one arm where the
   answer is not known, the read recovers nothing, and the reading built on it
   is uninformative. This is failure 2's own limb: a working instrument that
   returns nothing on the target. Open; carried from 2026-09-21.
3. **A cell that is empty by construction. MEASURED, fires, and the findings
   caught it.** Control 2's full procedure has zero clearing site sets on arms T
   and M on every seed (section 4.1, "c2 no verdict (0)"). That cell is empty by
   construction, because those arms hold the named agent outside the running
   state. The ruling's item 5 records it as not applicable, which is the right
   disposition. Control 6's two cells are not empty: 81 and 719 trials on every
   arm and seed (`controls` fields).
4. **A claim of measurement with no record, or with a record that does not
   reproduce. MEASURED, fires twice.** "7 of 12" does not match its record
   (section 4.1), and the ruling carries it forward. The ruling's "$161.90"
   cites a file that exists at no commit on main (section 5). This is the form
   `RT-145` in the red team ledger names: a citation to a file the reader of main
   cannot open. It is harmless while the ruling sits on its own branch. It bites
   if pull request 53 merges before pull request 51. On reproducing from code
   (section 3): every figure on arm T, every gate verdict and every ruled pass
   reproduces. Three figures the findings state about the procedure do not
   reproduce: which arm and seed got the degenerate site set, the disagreement
   count, and control 2 passing on all three free-arm seeds. Neither do the
   decimals on arms C, F and M, as the 2026-09-23 ruling expects for C and F.
5. **A command that creates something while documented as creating nothing.
   MEASURED, does not apply.** The new code contacts nothing outside the laptop:

   ```
   $ grep -n -i -E 'runpod|ssh|curl|requests|subprocess|urllib|socket' experiments/rehearsal-successor-measure/src/repairs.py experiments/rehearsal-successor-measure/src/arm_middle.py experiments/rehearsal-successor-measure/src/diagnose_named_other.py experiments/rehearsal-successor-measure/src/training.py; echo "exit $?"
   experiments/rehearsal-successor-measure/src/training.py:33:    and is the slowest thing in the rehearsal, so identical requests are
   exit 0
   ```

   The one hit is the word "requests" in a comment about caching episode
   generation. Nothing in the four files reaches outside the laptop.
6. **A remote step tested only against stand-ins. Does not apply**, on the same
   command: there is no remote step in the repairs.

---

## 7. What was opened, what was not, and the repository's own checks on this file

**Opened:** on branch `worktree-w1c-rehearsal-repairs` at `e0626b2`, the findings,
the method note (its outline and section 7), `repairs.py`,
`diagnose_named_other.py`, `grammar.py` (the marker pools), `training.py` (the
data cache), every file in `out-repairs/`, and the session prompts, section
(c). Also the ruling on branch `rulings-2026-09-25-repairs`, the attempt-2
rented-slice findings at `7da1946` (section 7 only), the 2026-09-21 record
`out/nominate.json`, the 2026-09-21 review's section 6, and the 2026-09-22 re-run
precedent. **Read only, not used for any output:** the writer's working folder
(file times and logs). **Not opened:** the writer's checkpoints; `arm_middle.py`
beyond running its self-test; the proposal; the queue ruling beyond the lines
cited.

MEASURED, `scripts/check_citations.py --scope nocopies --only <this file>`:
19 references to files not on main, every one of them a file on pull request
52's branch (the findings, the method note, `out-repairs/`), as the header says.
0 figures absent from the file their sentence cites. 1 approximate match to look
at (the 0.072 fit, which is in `out/nominate.json` to more places).
`scripts/check_single_source.py` on this file: 0 confident findings; 2
figures without a ledger source, the session's own $0 and the $450 envelope,
which is cited to its ruling.

## Appendix

Every script here only reads files, except the driver, which trains and measures on the laptop. All ran from this session's scratch folder (`$JOB`, `~/.claude/jobs/e0de12ac/tmp/`), which is not kept.

### A. The driver that ran the re-run (`run_all.sh`)

```
#!/bin/sh
# From-clean re-run of the rehearsal repairs at e0626b2, in a scratch copy. Local, $0.
set -u
PY=/Users/john/Code/minimum-viable-mind/.venv/bin/python
cd /Users/john/.claude/jobs/e0de12ac/tmp/rerun/experiments/rehearsal-successor-measure/src
L=../out-repairs/logs
date "+start %Y-%m-%d %H:%M:%S"
$PY repairs.py --stage train --arms F --recipes base,curriculum,reweight > $L/train_streamA.log 2>&1 &
A=$!
$PY repairs.py --stage train --arms T,C,M,blind --recipes base > $L/train_streamB.log 2>&1 &
B=$!
wait $A; wait $B
date "+trained %H:%M:%S"
$PY repairs.py --stage gate --arms F --recipes curriculum > $L/gate_curriculum.log 2>&1
$PY repairs.py --stage gate --arms F --recipes reweight > $L/gate_reweight.log 2>&1
$PY repairs.py --stage gate --arms T,C,F,M,blind --recipes base > $L/gate_base.log 2>&1
$PY diagnose_named_other.py --recipes base,curriculum,reweight > $L/diagnose.log 2>&1
for a in T,C F M; do
  t=$(echo $a | tr , _)
  $PY repairs.py --stage nominate --arms $a --recipes base > $L/nominate_base_$t.log 2>&1
  $PY repairs.py --stage measure --arms $a --recipes base > $L/measure_base_$t.log 2>&1
done
$PY repairs.py --stage summary --arms T,C,F,M --recipes base > $L/summary.log 2>&1
: > ../out-repairs/self-tests.txt
for m in grammar arms transplant measure arm_middle; do
  $PY $m.py --self-test 2>&1 | grep -v -i "userwarning\|consider using\|^  log(f" >> ../out-repairs/self-tests.txt
done
date "+done %H:%M:%S"
```

Its log:

```
start 2026-09-25 20:12:39
trained 00:18:39
done 00:58:37
```

### B. The extraction script (`extract.py`)

```
# Prints every figure the check covers, from one out-repairs folder. Reads files only.
import json, os, sys
d = sys.argv[1]
J = lambda f: json.load(open(os.path.join(d, f)))
f4 = lambda x: "  --  " if x is None else f"{x:.4f}"
S = (0, 1, 2)
print("[1] named-other gate, free arm (bar 790 of 3000)")
for rec in ("base", "curriculum", "reweight"):
    g = J(f"gate_{rec}.json")
    rs = [g["runs"][f"F/{rec}/{s}"] for s in S]
    print(f"  {rec:10s} named-other {' / '.join(f4(r['other']) for r in rs)}  correct {[r['other_correct'] for r in rs]}"
          f"  clearing {sum(r['other_clears'] for r in rs)} of 3   own {' / '.join(f4(r['own']) for r in rs)}")
g = J("gate_base.json")
print("[2] learn-both gate, base recipe")
for a in ("T", "C", "F", "M", "blind"):
    rs = [g["runs"][f"{a}/base/{s}"] for s in S]
    v = g["verdicts"].get(f"{a}/base", {})
    print(f"  {a:5s} own {' / '.join(f4(r['own']) for r in rs)}  other {' / '.join(f4(r['other']) for r in rs)}"
          f"  lesioned own {' / '.join(f4(r['lesioned_own']) for r in rs)}  learn-both {v.get('learn_both')}"
          f"  collapses {[r['lesion_collapses_own'] for r in rs]}")
print("  name-only solver", g["name_only_solver"])
dg = J("diagnose_named_other.json")
print("[3] diagnostic (named / own / other in item / not in item)")
for rec in ("base", "curriculum", "reweight"):
    print(f"  {rec:10s}", "  ".join("/".join(f"{dg[f'F/{rec}/{s}'][k]:.2f}" for k in ("named", "own", "other_in_item", "not_in_item")) for s in S))
M = {}
for f in ("measure_base_T_C.json", "measure_base_F.json", "measure_base_M.json"):
    M.update(J(f)["arms"])
print("[4] reading (chance-corrected), per seed: untouched whole own-only degree | site set")
for a in ("T", "C", "F", "M"):
    for s in S:
        r = M[f"{a}/base/{s}"]; rd = r["reading"]; ss = r["site_set"]
        print(f"  {a}{s} {f4(rd['accuracy_untouched'])} {f4(rd['accuracy_whole'])} {f4(rd['accuracy_ownership_only'])} "
              f"deg {f4(rd['degree'])} {rd['status']:9s} | {ss['positions']} L{ss['layers']} r{ss['rank']}")
print("[5] rider at arm T's site set: status, whole/untouched")
for a in ("C", "F", "M"):
    print(f"  {a}", "  ".join(f"{r['status']} {f4(r['accuracy_whole'])}/{f4(r['accuracy_untouched'])}"
                              for r in (M[f'{a}/base/{s}']['rider_at_arm_T_site_set']['reading'] for s in S)))
print("[6] control 2 (full procedure | fixed-site variant)")
for a in ("T", "C", "F", "M"):
    c = [M[f"{a}/base/{s}"]["control2"] for s in S]
    full = [x["full procedure"] for x in c]
    r4 = lambda x, k: round(x[k], 4) if k in x else None
    print(f"  {a} full {[x['status'] for x in full]}"
          f" own-moved {[r4(x, 'own_directed_moved') for x in full]}"
          f" random {[r4(x, 'own_directed_moved_random_subspace') for x in full]}"
          f" named-moved {[r4(x, 'named_other_moved') for x in full]}"
          f" | fixed {[x['fixed-site variant']['status'] for x in c]}")
print("[7] arm M: blind, formula, true slot, miss, entangled share")
for s in S:
    r = M[f"M/base/{s}"]; fa = r["fourth_arm"]
    print(f"  M{s} blind {f4(r['reading']['degree'])} formula {f4(fa['predicted_from_route_accuracies'])} "
          f"true-slot {f4(r['oracle_reading']['degree'])} miss {abs(r['reading']['degree'] - fa['predicted_from_route_accuracies']):.4f} "
          f"share {fa['entangled_share']:.4f} entangled whole/untouched {f4(fa['entangled_route_whole'])}/{f4(fa['entangled_route_untouched'])}")
print("[8] sensitivity without all-position sets (arm C)")
for s in S:
    x = M[f"C/base/{s}"]["sensitivity_without_all_positions"]
    print(f"  C{s} {x['site_set']['positions']} L{x['site_set']['layers']} r{x['site_set']['rank']} deg {f4(x['reading']['degree'])}")
sm = J("summary_base.json")
print("[9] summary: separation C-T, across-seed sd of raw difference")
print("  separation", {k: round(v["C_minus_T"], 4) for k, v in sm["separation"].items()})
for a in ("C", "F", "M"):
    print(f"  {a} sd {sm['arms'][a]['across_seed_sd_of_raw_difference']:.4f} range {[round(x, 4) for x in sm['arms'][a]['degree_range']]}")
print("[10] controls 1 / 3 / 4 / 6a / 6b / 7, per seed")
for a in ("T", "C", "F", "M"):
    for s in S:
        c = M[f"{a}/base/{s}"]["controls"]
        pick = lambda p: next(v for kk, v in c.items() if kk.startswith(p))
        print(f"  {a}{s} {pick('1 '):.4f} {pick('3 '):.4f} {pick('4 '):.4f} {pick('6a same-value cell: share'):.4f} "
              f"{pick('6b different-value cell: share'):.4f} {pick('7 ')}")
```

### C. The nomination script (`check_nominate.py`)

```
# Prints the nomination table from one out-repairs folder: sets clearing, the
# nomination, the other reading ("sensitivity" in the file), whether they agree,
# their ownership-only gap, and floor-form disagreements. Reads files only.
import json, sys, os
d = sys.argv[1]
rows, dis, gaps, floor_dis = [], 0, [], 0
for f in ("nominate_base_T_C.json", "nominate_base_F.json", "nominate_base_M.json"):
    j = json.load(open(os.path.join(d, f)))
    for k, r in j["arms"].items():
        o = r["ownership"]
        for g in o["grid"]:
            floor_dis += g["floor"]["clears"] != g["floor"]["clears_plain_form"]
        n, s = o["nomination"], o["sensitivity"]
        fmt = lambda g: f'{g["positions"]} L{g["layers"]} r{g["rank"]}'
        same = (n["positions"], n["layers"], n["rank"]) == (s["positions"], s["layers"], s["rank"])
        gap = abs(n["accuracy_ownership_only"] - s["accuracy_ownership_only"])
        dis += not same; gaps.append(gap)
        print(f'{k:10s} clear {o["site_sets_clearing"]:2d}  nom {fmt(n):28s} {n["accuracy_whole"]:.4f}/{n["accuracy_ownership_only"]:.4f}  '
              f'other {"same" if same else fmt(s):28s} gap {gap:.4f}  c2 {r["control2_named_agent"]["status"]} ({r["control2_named_agent"]["site_sets_clearing"]})')
print(f'readings disagree on {dis} of {len(gaps)}; largest ownership-only gap {max(gaps):.4f}; floor-form disagreements {floor_dis}')
print('family_size', j["family_size"], 'label', j["label"])
```

### D. `extract.py` on the committed folder (`out-repairs/` at `e0626b2`)

```
$ .venv/bin/python $JOB/extract.py $JOB/rerun/experiments/rehearsal-successor-measure/out-repairs-committed
[1] named-other gate, free arm (bar 790 of 3000)
  base       named-other 0.3313 / 0.2603 / 0.2487  correct [994, 781, 746]  clearing 1 of 3   own 0.5597 / 0.5513 / 0.5547
  curriculum named-other 0.0773 / 0.1933 / 0.1430  correct [232, 580, 429]  clearing 0 of 3   own 0.5507 / 0.5643 / 0.5637
  reweight   named-other 0.2317 / 0.2063 / 0.2377  correct [695, 619, 713]  clearing 0 of 3   own 0.1723 / 0.1700 / 0.1760
[2] learn-both gate, base recipe
  T     own 1.0000 / 1.0000 / 1.0000  other 1.0000 / 1.0000 / 1.0000  lesioned own 0.2467 / 0.2510 / 0.2733  learn-both True  collapses [True, True, False]
  C     own 0.5703 / 0.5677 / 0.5757  other 0.2533 / 0.2503 / 0.2360  lesioned own 0.1780 / 0.1830 / 0.1703  learn-both False  collapses [True, True, True]
  F     own 0.5597 / 0.5513 / 0.5547  other 0.3313 / 0.2603 / 0.2487  lesioned own 0.1760 / 0.1850 / 0.1940  learn-both False  collapses [True, True, True]
  M     own 0.8640 / 0.8613 / 0.8667  other 0.5543 / 0.5663 / 0.5517  lesioned own 0.2230 / 0.2190 / 0.2203  learn-both True  collapses [True, True, True]
  blind own 0.2340 / 0.2383 / 0.2340  other 0.2373 / 0.2420 / 0.2167  lesioned own 0.2340 / 0.2383 / 0.2340  learn-both False  collapses [True, True, True]
  name-only solver {'n': 3000, 'other': 1.0, 'own': 0.238}
[3] diagnostic (named / own / other in item / not in item)
  base       0.33/0.06/0.39/0.22  0.26/0.07/0.48/0.18  0.25/0.05/0.51/0.19
  curriculum 0.08/0.55/0.17/0.20  0.19/0.14/0.38/0.30  0.14/0.28/0.30/0.28
  reweight   0.23/0.17/0.47/0.13  0.21/0.18/0.49/0.13  0.24/0.18/0.45/0.13
[4] reading (chance-corrected), per seed: untouched whole own-only degree | site set
  T0 0.0000 1.0000 1.0000 deg 0.0000 valid     | action L[0] r8
  T1 0.0000 1.0000 1.0000 deg 0.0000 valid     | action L[0] r8
  T2 0.0000 1.0000 1.0000 deg 0.0000 valid     | action L[0] r8
  C0 0.0512 0.5850 0.0525 deg 0.9977 valid     | all L[0] r2
  C1 0.0488 0.5613 0.0525 deg 0.9927 valid     | all L[0] r4
  C2 0.0600 0.5025 0.0600 deg 1.0000 valid     | post-identity L[0] r2
  F0 0.0587 0.4850 0.0575 deg 1.0029 valid     | post-identity L[0] r2
  F1 0.0563 0.5675 0.0563 deg 1.0000 valid     | action+3 L[1] r4
  F2 0.0688 0.4913 0.0688 deg 1.0000 valid     | post-identity L[0] r1
  M0 0.0125 0.7887 0.3925 deg 0.5105 valid     | post-identity L[0] r8
  M1 0.0175 0.7475 0.3937 deg 0.4846 valid     | action L[3] r8
  M2 0.0138 0.7913 0.3775 deg 0.5322 valid     | post-identity L[0] r8
[5] rider at arm T's site set: status, whole/untouched
  C no verdict 0.0512/0.0512  no verdict 0.0488/0.0488  no verdict 0.0600/0.0600
  F no verdict 0.0587/0.0587  no verdict 0.0563/0.0563  no verdict 0.0688/0.0688
  M no verdict 0.4088/0.0125  no verdict 0.4138/0.0175  no verdict 0.4100/0.0138
[6] control 2 (full procedure | fixed-site variant)
  T full ['no verdict', 'no verdict', 'no verdict'] own-moved [None, None, None] random [None, None, None] named-moved [None, None, None] | fixed ['pass', 'pass', 'pass']
  C full ['no verdict', 'no verdict', 'no verdict'] own-moved [None, None, None] random [None, None, None] named-moved [None, None, None] | fixed ['pass', 'pass', 'pass']
  F full ['pass', 'pass', 'pass'] own-moved [0.0075, 0.0, 0.0012] random [0.0125, 0.0, 0.0] named-moved [0.115, 0.0012, 0.035] | fixed ['pass', 'pass', 'pass']
  M full ['no verdict', 'no verdict', 'no verdict'] own-moved [None, None, None] random [None, None, None] named-moved [None, None, None] | fixed ['pass', 'pass', 'pass']
[7] arm M: blind, formula, true slot, miss, entangled share
  M0 blind 0.5105 formula 0.4895 true-slot 0.4895 miss 0.0209 share 0.6038 entangled whole/untouched 0.6501/0.0207
  M1 blind 0.4846 formula 0.4572 true-slot 0.4572 miss 0.0274 share 0.6038 entangled whole/untouched 0.5818/0.0290
  M2 blind 0.5322 formula 0.4904 true-slot 0.4904 miss 0.0418 share 0.6038 entangled whole/untouched 0.6542/0.0228
[8] sensitivity without all-position sets (arm C)
  C0 action L[2] r8 deg 1.0051
  C1 post-identity L[0] r8 deg 0.9863
  C2 post-identity L[0] r2 deg 1.0000
[9] summary: separation C-T, across-seed sd of raw difference
  separation {'0': 0.9977, '1': 0.9927, '2': 1.0}
  C sd 0.0466 range [0.9927, 1.0]
  F sd 0.0499 range [1.0, 1.0029]
  M sd 0.0309 range [0.4846, 0.5322]
[10] controls 1 / 3 / 4 / 6a / 6b / 7, per seed
  T0 0.0000 0.0000 0.0000 0.0000 1.0000 True
  T1 0.0000 0.0000 0.0000 0.0000 1.0000 True
  T2 0.0000 0.0000 0.0000 0.0000 1.0000 True
  C0 0.5637 0.0500 0.1562 0.7160 0.8985 True
  C1 0.5675 0.0488 0.1437 0.7160 0.8971 True
  C2 0.5038 0.0625 0.1562 0.5926 0.9054 True
  F0 0.4938 0.0587 0.1475 0.7407 0.8957 True
  F1 0.5637 0.0600 0.0612 0.6790 0.8790 True
  F2 0.4888 0.0712 0.1437 0.6420 0.8818 True
  M0 0.4125 0.0125 0.1237 0.2346 0.9458 True
  M1 0.3638 0.0563 0.0275 0.1728 0.8456 True
  M2 0.4238 0.0125 0.1212 0.3210 0.9527 True
```

### E. `extract.py` on the re-run folder

```
$ .venv/bin/python $JOB/extract.py $JOB/rerun/experiments/rehearsal-successor-measure/out-repairs
[1] named-other gate, free arm (bar 790 of 3000)
  base       named-other 0.4080 / 0.2477 / 0.2537  correct [1224, 743, 761]  clearing 1 of 3   own 0.5667 / 0.5667 / 0.5560
  curriculum named-other 0.2287 / 0.0773 / 0.0677  correct [686, 232, 203]  clearing 0 of 3   own 0.5583 / 0.5683 / 0.5553
  reweight   named-other 0.2407 / 0.2453 / 0.2203  correct [722, 736, 661]  clearing 0 of 3   own 0.1757 / 0.1550 / 0.1717
[2] learn-both gate, base recipe
  T     own 1.0000 / 1.0000 / 1.0000  other 1.0000 / 1.0000 / 1.0000  lesioned own 0.2467 / 0.2510 / 0.2733  learn-both True  collapses [True, True, False]
  C     own 0.5717 / 0.5710 / 0.5780  other 0.2487 / 0.2440 / 0.2547  lesioned own 0.1750 / 0.1787 / 0.1897  learn-both False  collapses [True, True, True]
  F     own 0.5667 / 0.5667 / 0.5560  other 0.4080 / 0.2477 / 0.2537  lesioned own 0.1627 / 0.1860 / 0.1823  learn-both False  collapses [True, True, True]
  M     own 0.8560 / 0.8577 / 0.8650  other 0.5607 / 0.5640 / 0.5573  lesioned own 0.2293 / 0.2180 / 0.2193  learn-both True  collapses [True, True, True]
  blind own 0.2360 / 0.2477 / 0.2413  other 0.2300 / 0.2320 / 0.2287  lesioned own 0.2360 / 0.2477 / 0.2413  learn-both False  collapses [True, True, True]
  name-only solver {'n': 3000, 'other': 1.0, 'own': 0.238}
[3] diagnostic (named / own / other in item / not in item)
  base       0.41/0.05/0.34/0.20  0.25/0.06/0.48/0.21  0.25/0.04/0.50/0.21
  curriculum 0.23/0.06/0.46/0.25  0.08/0.56/0.16/0.21  0.07/0.55/0.16/0.22
  reweight   0.24/0.17/0.46/0.13  0.25/0.16/0.46/0.13  0.22/0.18/0.46/0.14
[4] reading (chance-corrected), per seed: untouched whole own-only degree | site set
  T0 0.0000 1.0000 1.0000 deg 0.0000 valid     | action L[0] r8
  T1 0.0000 1.0000 1.0000 deg 0.0000 valid     | action L[0] r8
  T2 0.0000 1.0000 1.0000 deg 0.0000 valid     | action L[0] r8
  C0 0.0625 0.5125 0.0625 deg 1.0000 valid     | post-identity L[0] r8
  C1 0.0587 0.5850 0.0612 deg 0.9952 valid     | action+3 L[1] r4
  C2 0.0650 0.5487 0.0612 deg 1.0078 valid     | action L[3] r4
  F0 0.0650 0.6088 0.0650 deg 1.0000 valid     | all L[0] r4
  F1 0.0625 0.5138 0.0612 deg 1.0028 valid     | post-identity L[0] r8
  F2 0.0712 0.5075 0.0688 deg 1.0057 valid     | post-identity L[0] r4
  M0 0.0150 0.7875 0.3800 deg 0.5275 valid     | post-identity L[0] r8
  M1 0.0112 0.7775 0.3762 deg 0.5237 valid     | post-identity L[0] r8
  M2 0.0175 0.7725 0.3738 deg 0.5281 valid     | post-identity L[0] r8
[5] rider at arm T's site set: status, whole/untouched
  C no verdict 0.0625/0.0625  no verdict 0.0587/0.0587  no verdict 0.0650/0.0650
  F no verdict 0.0650/0.0650  no verdict 0.0625/0.0625  no verdict 0.0712/0.0712
  M no verdict 0.4113/0.0150  no verdict 0.4075/0.0112  no verdict 0.4138/0.0175
[6] control 2 (full procedure | fixed-site variant)
  T full ['no verdict', 'no verdict', 'no verdict'] own-moved [None, None, None] random [None, None, None] named-moved [None, None, None] | fixed ['pass', 'pass', 'pass']
  C full ['no verdict', 'no verdict', 'no verdict'] own-moved [None, None, None] random [None, None, None] named-moved [None, None, None] | fixed ['pass', 'pass', 'pass']
  F full ['pass', 'pass', 'no verdict'] own-moved [0.0025, 0.0, None] random [0.0012, 0.0, None] named-moved [0.095, 0.0, None] | fixed ['pass', 'pass', 'pass']
  M full ['no verdict', 'no verdict', 'no verdict'] own-moved [None, None, None] random [None, None, None] named-moved [None, None, None] | fixed ['pass', 'pass', 'pass']
[7] arm M: blind, formula, true slot, miss, entangled share
  M0 blind 0.5275 formula 0.4871 true-slot 0.4871 miss 0.0405 share 0.6038 entangled whole/untouched 0.6480/0.0248
  M1 blind 0.5237 formula 0.4829 true-slot 0.4829 miss 0.0408 share 0.6038 entangled whole/untouched 0.6315/0.0186
  M2 blind 0.5281 formula 0.4752 true-slot 0.4752 miss 0.0530 share 0.6038 entangled whole/untouched 0.6232/0.0290
[8] sensitivity without all-position sets (arm C)
  C0 post-identity L[0] r8 deg 1.0000
  C1 action+3 L[1] r4 deg 0.9952
  C2 action L[3] r4 deg 1.0078
[9] summary: separation C-T, across-seed sd of raw difference
  separation {'0': 1.0, '1': 0.9952, '2': 1.0078}
  C sd 0.0369 range [0.9952, 1.0078]
  F sd 0.0571 range [1.0, 1.0057]
  M sd 0.0045 range [0.5237, 0.5281]
[10] controls 1 / 3 / 4 / 6a / 6b / 7, per seed
  T0 0.0000 0.0000 0.0000 0.0000 1.0000 True
  T1 0.0000 0.0000 0.0000 0.0000 1.0000 True
  T2 0.0000 0.0000 0.0000 0.0000 1.0000 True
  C0 0.5112 0.0600 0.1537 0.6667 0.8943 True
  C1 0.5813 0.0612 0.0563 0.5185 0.8679 True
  C2 0.5487 0.0700 0.0688 0.4691 0.8387 True
  F0 0.6038 0.0650 0.1525 0.6543 0.8915 True
  F1 0.5112 0.0625 0.1600 0.7407 0.8832 True
  F2 0.5125 0.0700 0.1650 0.6173 0.8915 True
  M0 0.4213 0.0138 0.0912 0.2099 0.9332 True
  M1 0.3987 0.0138 0.1138 0.2099 0.9485 True
  M2 0.4012 0.0175 0.1250 0.2716 0.9332 True
```
