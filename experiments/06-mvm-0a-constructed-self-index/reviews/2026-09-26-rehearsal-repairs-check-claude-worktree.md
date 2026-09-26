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

**INTERIM RECORD.** Sections 1, 2, 4, 5 and 6 are complete. Section 3, the
re-run, is filled in when the run finishes (about four hours of laptop time).
This version is committed first so that the checks already done cannot be lost.

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

*(Filled in when the run finishes.)*

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
the sentence says. The findings' other two claims in that bullet hold: the
largest gap is 0.0200, and the two forms of the floor never disagree (0). The
ruling repeats the 7 (section 5 below).

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
| $450 envelope | from the Weekend 1 queue ruling, page 6, which the findings quote | not a findings figure |
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
   if pull request 53 merges before pull request 51. Whether the figures
   reproduce from code is section 3.
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

## Appendix — the two scripts

*(Pasted in full with the final version.)*
