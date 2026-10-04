# Check of the controls re-run of 2026-10-03

*Written 2026-10-03 (Pacific) by a Claude Code checking session, on branch
`w2a-job1-controls-rerun-check`, cut from the main line at `7c403b0`. Laptop
only, on the processor. Nothing rented, nothing trained, nothing spent: $0.
Written under the workspace plain-language rule. This file edits no ruling,
proposal, registered text or protocol text, and none of the files it checks.*

**What this session opened.** Committed files only: the findings
`docs/2026-10-03-controls-rerun.md`; the method
`docs/controls-rerun-method-2026-10-03.md`; the code
`experiments/rehearsal-successor-measure/src/rerun_controls.py` and the
rehearsal code it calls (`transplant.py`, `repairs.py`, `rehearse.py`,
`rerun_v3.py`, `training.py`, `grammar.py`, `arms.py`); the after-the-fact
diagnostic `src/posthoc_control4.py`; the outputs in
`experiments/rehearsal-successor-measure/out-controls-rerun/`; the rulings
`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (pages 1 and 2) and
`docs/rulings/2026-10-03-controls-rerun-rulings.md` with its packet; sections
7.3 and 10 of proposal version 3; the git history and pull request 76's list
of commits. **What it did not open:** any chat or transcript of the session
that wrote and ran the re-run.

**Labels.** **MEASURED** means the command and its output are in this file or
in the folder beside it,
`2026-10-03-controls-rerun-check-scripts/`. **ARGUED** means reasoning a
reader can dispute.

## 1. The short version

- **The re-run reproduces exactly.** Run again from the committed code, it
  wrote the same 26 files. Every value in every output file is equal to the
  committed one, and the results table is identical byte for byte. The only
  difference is the script's own stopwatch.
- **The commit order is as claimed.** The method and code were committed with
  no output; the outputs came in a later commit; the script has not changed
  since.
- **The after-the-fact diagnostic of the too-early-position control is right,
  and its explanation is supported.** This session's own separately written
  test gets the same answers and adds two measurements that the diagnostic
  did not make, both of which back its account. **So John's ruling on that
  control stands and does not need to return to him.** Section 5.
- **One thing about that control John should have in plain view** (the packet
  told him, and it is now measured): before both twins' first own turns the
  twins' internal states are identical, so the redefined control puts back
  what was already there. It can fail only if the pairing or the code is
  broken. A pass says nothing about any model.
- **Five small things in the findings' wording and four places where the
  code, the method and the ruling do not say quite the same thing.** None
  changes a figure or a verdict. Sections 3 and 4.

## 2. The commit order, and whether the script changed

**MEASURED.**

```
$ git branch -a --contains f2d836b
(nothing: the commit is not on the main line, because pull request 76 was squashed)

$ gh pr view 76 --json commits,mergeCommit,headRefName
{"commits":[{"date":"2026-10-03T23:56:27Z","msg":"Controls re-run under the registered rules: method and code, committe…","oid":"f2d836b"},
            {"date":"2026-10-04T00:15:23Z","msg":"Controls re-run under the registered rules: findings and outputs","oid":"92d64a8"}],
 "head":"controls-rerun-2026-10-03","merge":"821f15427757a00cf9be29719d776dc1ec1bc770"}

$ git show --stat --format='%h %s' f2d836b
f2d836b Controls re-run under the registered rules: method and code, committed before any output
 docs/controls-rerun-method-2026-10-03.md           | 164 +++++++++
 .../src/rerun_controls.py                          | 393 +++++++++++++++++++++
 2 files changed, 557 insertions(+)

$ git diff --stat f2d836b 7c403b0 -- experiments/rehearsal-successor-measure/src/ docs/controls-rerun-method-2026-10-03.md
 .../src/posthoc_control4.py                        | 39 ++++++++++++++++++++++
 1 file changed, 39 insertions(+)
```

- *The method and the code were committed with no output before the outputs.*
  **Matches:** commit `f2d836b` holds two files, the method and the script,
  and nothing else; the outputs and findings are commit `92d64a8`, nineteen
  minutes later.
- *`rerun_controls.py` is unchanged since that commit.* **Matches:** between
  `f2d836b` and the main line the only difference under `src/` is the added
  diagnostic script; the method file is unchanged too.
- **One limit, ARGUED.** The commit times show the order in which things were
  committed. They cannot show that the script was not run before `f2d836b`.
  The script takes about sixteen minutes and the gap is nineteen, which is
  consistent with the claim and does not prove it. Commit `f2d836b` is
  reachable only through the pull request's branch, not from the main line;
  if that branch is ever deleted the evidence of the order goes with it.

## 3. The re-run, run again, and every figure compared

**MEASURED.** The committed outputs were copied aside, then:

```
$ cd experiments/rehearsal-successor-measure/src
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python rerun_controls.py
...
done in 873s
```

(torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor; the same
versions the findings name. The project's Python lives in the main checkout,
so the full path was used from this worktree. The run's printed log is
`rerun_controls_stdout.txt` in the scripts folder.)

```
$ python compare_and_verify.py <the committed copy> <this run's folder>
== 1. committed outputs against this session's re-run
files in the committed copy: 26; in this run's folder: 26; same names: True
table.md: byte-identical True
json values compared (approximate count): 26723
differences other than the run's own wall-clock time: 0
  (wall-clock) summary.json/seconds: committed 967s | this run 873s
```

- *Every figure in `table.md`.* **Matches:** the file this run wrote is
  identical byte for byte.
- *Every figure in the 25 output files.* **Matches:** no value differs, in
  about 26,700 compared, other than the stopwatch.

**The findings' prose figures**, recomputed from the output files by the same
script (its full output is `compare_and_verify.out`). One line each:

| The findings say | Recomputed | Verdict |
|---|---|---|
| Section 1: the separable model reads 0.0000 on every seed; the entangled 1.0051, 0.9926, 0.9974; the mixed 0.4886, 0.4860, 0.5449 | 0.0, 0.0, 0.0; 1.00512, 0.99259, 0.99743; 0.48860, 0.48595, 0.54487 | Matches |
| Section 1: the separation clears 0.5 on every seed | 1.0051, 0.9926, 0.9974; all true | Matches |
| Section 1: the free model's best piece is right on 34 of 180 | 34 (seed 0), 20, 29 | Matches |
| Section 3: the entangled model's seed 1 chose layer 1, the action position and the three before it, 8 directions, piece 172 of 180; 0.0533 there against 0.0517 at layer 4 | The candidates list shows exactly that | Matches |
| Section 3: the free model's whole read is right on 32, 12 and 18 of 180 at the layers shown; the graphics-chip figures were 31, 12 and 19 | 32, 12, 18 at layer 1; the earlier figures are 0.172, 0.067, 0.106 in `docs/2026-09-26-toy-rerun-v3-rules.md` | Matches |
| Section 4: the null transplant is bit-identical "on all twelve primary site sets, on the nine stricter-row site sets, and on arm F's three described ones" | 12 of 12 primary; 9 of 9 stricter | Matches, **with a wording slip**: the free model's three described sites are three of the twelve, not three more; and six of the nine stricter rows are the same site as the primary. The number of different places tested is fifteen |
| Section 4: the no-transplant rule holds on all twelve; largest miss 0.0132, the entangled model's seed 0 | 12 of 12; 0.01321, C/0 | Matches |
| Section 4: control 1 figures | Equal to four decimals on all twelve | Matches |
| Section 4: control 3, which models sit above, among or below the twenty random pieces | As stated | Matches |
| Section 4: control 6, 81 and 719 trials; ranges 0.51 to 0.63, 0.22 to 0.32, 0.63 to 0.73 | As stated | Matches |
| Section 4: the mixed model's reading is within 0.0049, **0.0100** and 0.0529 of its built-in reference | 0.0049, **0.0099**, 0.0529 | **Differs in the fourth decimal.** The unrounded difference is 0.00995. The findings subtracted two rounded figures. The method file and the first packet say 0.0099 |
| Section 4: the rider, and the stricter row changing only the separable model, to layer 1, still 0.0000 | As stated | Matches |
| Section 4: the whole-state floor on fresh episodes clears on all twelve | 12 of 12 | Matches |
| Section 5: the other-agent control's block for the free model's seed 0 | Every figure equal | Matches. Note that the best figure in that block is a piece, 139 of 180 (layer 2, 8 directions), two above the whole read's best of 137. Both are under 144 |
| Section 5: the other eleven (760, 751, 708, 781, 746 against 790) | As stated | Matches |
| Section 6: above the no-transplant rate by 0.065 to 0.10 on six, 0.005 or less on the rest | 0.0650 to 0.1013; 0.0050 or less | Matches |
| Section 6: the diagnostic's printed block | This session ran `posthoc_control4.py` again: every line equal (`posthoc_control4_rerun.out`) | Matches |

## 4. The code against the method, and the method against the ruling

Read rule by rule. **ARGUED** throughout, from the files named; nothing here
changes a figure.

**Where the code does what the method says** (rules 1, 2, 4 to 12, and the
controls of section 4): the fingerprint check before loading; the seeds
4242, 777, 778, 781 and 4243; the family of 45 site sets, asserted; the
whole-state floor; fewest layers per position set, ties to the earliest; the
piece's accuracy as a fresh read on the piece's coordinates, worst layer,
144 of 180; the choice by highest development share, then smaller size, then
earlier position set; the two kinds of no verdict; the stricter row; the
floor applied again on fresh episodes; the free model's controls run at the
site the rule would choose with the piece requirement off and labelled as
description.

**Where the code does something the method does not state, or states
differently:**

1. **"The committed figure" is not printed** (method, rule 3). The method
   says each read's accuracy is "recomputed on the processor and printed as a
   count of 180 beside the committed figure". The table prints the recomputed
   count only. The findings give the earlier figures for the free model in a
   sentence and for no other model.
2. **The whole read's accuracy is a refit, not the committed read scored**
   (method, rule 3; code, `correct_count`). The method says the committed
   reads "are not refitted". That is true of the directions that are
   transplanted, which come from the committed coefficients. But the count
   printed as "whole read" is from a fresh read fitted on the processor on
   the same split, not from the committed coefficients applied to held-out
   episodes. On the built models nothing turns on it (180 of 180 or close).
   A reader should know the printed whole-read count and the transplanted
   directions come from two fits of the same read.
3. **The controls that "hold" are computed and printed, and nothing in the
   code withholds a reading on them.** The method says a failure of the null
   transplant, of control 1 on the separable model, or of the no-transplant
   rule "withholds the reading for that arm and seed", and stop K2 says no
   reading is reported if the null transplant fails. The code records each as
   a true-or-false field and prints the reading regardless. All of them
   passed, so no reading was printed that should not have been. For the
   registered version the withholding should be in the code, not left to the
   reader of the table.
4. **Control 2's random piece is a single draw with its own seed** (code,
   line 251: `100 + seed`). The method names no seed and says "a random
   piece". Control 3 uses twenty draws. The pass line that used this draw has
   since been withdrawn, so this matters only as a note for how the reported
   description is computed.
5. **Control 4 uses the site's layers and not its positions** (code, lines
   195 to 196). The method does not say either way. This is what makes
   section 6's sentence about "the ones whose site set is ... `post-identity`"
   a pattern and not a cause; see section 5 below.

**Where the method states something the ruling does not:**

6. **The piece's accuracy is taken at the action position only**, and the
   requirement is applied after the layers are chosen. The method marks both
   as its own reading for John to overturn, and John has since ruled on the
   first (reported at the other positions, not gated). The second has not
   been put to him in terms: under it the requirement can never change which
   layers are used, only which sizes.
7. **Control 3, the rider and the stricter row** are run though page 2 of the
   ruling does not list them. Additions, harmless.
8. **The ruling's first sentence is wider than what was run.** Page 2 rules
   "the re-run of rehearsal items R-1 to R-6 under the registered rules" and
   then says what it covers: controls 1, 2, 4 and 6 on three kinds of model
   and control 7. The method follows the second sentence. Items R-1 and R-5
   as the proposal lists them (that the task is learnable; that the ordinary
   competing solver, the one with no "this turn is yours" signal, is built
   and measured) were not run again: the gate is read from the committed
   file, as the method's section 7 says, and the competing solver's three
   models are not loaded. **The competing solver has therefore not been
   measured under the rule that only pieces carrying the label may be
   chosen.** If version 4 quotes a figure for it, the figure is from before
   that rule. Small, and for John to know rather than to rule.

**Where the method's own predictions were wrong, as the findings say.** The
entangled model's seed 1 (predicted layer 4, reading 0.9975; got layer 1,
0.9926): flagged in the findings, section 3. The other-agent control was
expected to run on the free model's seed 0 and did not: flagged, section 5.
Both are reported straight.

## 5. The after-the-fact diagnostic of the too-early-position control

John's ruling 2 of `docs/rulings/2026-10-03-controls-rerun-rulings.md` rests
on this, and says in terms that it returns to him if this check finds the
diagnostic wrong. **It does not find it wrong.**

**The diagnostic's central claim:** in about half the matched pairs the donor
twin's first own turn comes before the recipient's, and with positions taken
before both twins' first own turns the transplant changes nothing.

**This session's own test** is
`2026-10-03-controls-rerun-check-scripts/independent_control4.py`. It does not
use the diagnostic script, the project's position-mask function, its
transplant function or its scoring function. It finds each twin's first own
turn by scanning the raw episode, builds its own masks, swaps states with its
own hook and scores with its own code. It reuses only the episode generator
(same seed), the model loader and the model's forward pass.

**MEASURED** (full output in `independent_control4.out`):

```
== claim 1: whose first own turn comes first
pairs: 800
donor's first own turn before the recipient's: 407 of 800 = 0.5088
recipient's before the donor's:                393 of 800 = 0.4913
the same position:                             0 of 800

== A: are the twins' inputs identical before both first own turns
token sequences identical in every pair, at every position: True
'this turn is yours' signal identical before both first own turns, every pair: True
and different at the earlier of the two first own turns, every pair: True

arm/seed | layers | no transplant | as run | as run, donor-first pairs | as run, recipient-first pairs | before both | outputs bit-identical before both | states identical before both, every layer
T/0 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (no transplant 0.0000) | 0.0000 (no transplant 0.0000; bit-identical True) | 0.0000 | True | True
T/1 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (no transplant 0.0000) | 0.0000 (no transplant 0.0000; bit-identical True) | 0.0000 | True | True
T/2 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (no transplant 0.0000) | 0.0000 (no transplant 0.0000; bit-identical True) | 0.0000 | True | True
C/0 | (2,) | 0.0512 | 0.0538 (+0.0025) | 0.0565 (no transplant 0.0516) | 0.0509 (no transplant 0.0509; bit-identical True) | 0.0512 | True | True
C/1 | (1,) | 0.0487 | 0.0500 (+0.0013) | 0.0590 (no transplant 0.0565) | 0.0407 (no transplant 0.0407; bit-identical True) | 0.0487 | True | True
C/2 | (1,) | 0.0600 | 0.1312 (+0.0712) | 0.1990 (no transplant 0.0590) | 0.0611 (no transplant 0.0611; bit-identical True) | 0.0600 | True | True
F/0 | (1,) | 0.0587 | 0.1375 (+0.0788) | 0.2064 (no transplant 0.0516) | 0.0662 (no transplant 0.0662; bit-identical True) | 0.0587 | True | True
F/1 | (1,) | 0.0562 | 0.0613 (+0.0050) | 0.0688 (no transplant 0.0590) | 0.0534 (no transplant 0.0534; bit-identical True) | 0.0562 | True | True
F/2 | (1,) | 0.0688 | 0.1338 (+0.0650) | 0.2039 (no transplant 0.0762) | 0.0611 (no transplant 0.0611; bit-identical True) | 0.0688 | True | True
M/0 | (1,) | 0.0125 | 0.1138 (+0.1013) | 0.2187 (no transplant 0.0197) | 0.0051 (no transplant 0.0051; bit-identical True) | 0.0125 | True | True
M/1 | (1,) | 0.0175 | 0.0975 (+0.0800) | 0.1843 (no transplant 0.0270) | 0.0076 (no transplant 0.0076; bit-identical True) | 0.0175 | True | True
M/2 | (1,) | 0.0137 | 0.0988 (+0.0850) | 0.1867 (no transplant 0.0197) | 0.0076 (no transplant 0.0076; bit-identical True) | 0.0137 | True | True
```

(The output's last column, the share of transplanted places where the
donor's state differs from the recipient's under the control as run, is 0.5309
on every model and is left out of the block above; it is in the output file.
Where a figure differs from the diagnostic's in the fourth decimal, 0.0538
against 0.0537 or 0.0487 against 0.0488, it is the same count of trials, 43
or 39 of 800, rounded from a slightly different stored number.)

- *In about half the pairs the donor's first own turn comes first: 0.5088.*
  **Matches:** 407 of 800.
- *With positions before both first own turns, the transplant changes
  nothing.* **Matches, and more strongly than the diagnostic showed.** The
  diagnostic showed the share landing on the donor's value was unchanged.
  This test shows the model's outputs are bit-identical on all twelve.
- *The control as run, at each model's layers.* **Matches** the re-run's
  figures on all twelve.

**Two measurements the diagnostic did not make, both supporting its account.**

- **A. The twins' states are identical before both first own turns**, at
  every layer of every model, and so are their inputs. The second packet,
  page 2, said this "was not measured". It now is. *Why it follows* (ARGUED):
  the twins are the same text; they differ only in which turns carry the
  "this turn is yours" signal; the models read left to right; so until one
  twin's signal first comes on, both have had exactly the same input.
- **B. All of the control's excess is in the pairs where the donor's first
  own turn comes first.** In the other 393 pairs the transplant as run is
  bit-identical to no transplant, on every model. In the 407 donor-first
  pairs, on the six models with a large excess, the share landing on the
  donor's value rises from about 0.02 to 0.08 with no transplant to 0.18 to
  0.22. That is the diagnostic's explanation shown directly: the effect lives
  exactly where the donor already knows who it is.

**One sentence of the findings that the test does not support as written**
(section 6: "Those six are exactly the ones whose site set is layer 1 at the
`post-identity` position set, which reaches back to the model's first own
turn"; the second packet repeats it). The control never uses the site's
position set, only its layers. **MEASURED**, the control as run, one layer at
a time, excess over no transplant at running state 0, 1, 2, 3, 4:

```
T/0 | nominated: layers (0,) at action | +0.0000 +0.0000 +0.0000 +0.0000 +0.0000
T/1 | nominated: layers (0,) at action | +0.0000 +0.0000 +0.0000 +0.0000 +0.0000
T/2 | nominated: layers (0,) at action | +0.0000 +0.0000 +0.0000 +0.0000 +0.0000
C/0 | nominated: layers (2,) at action | +0.1050 +0.0325 +0.0025 +0.0000 +0.0000
C/1 | nominated: layers (1,) at action+3 | +0.0950 +0.0013 +0.0000 +0.0000 +0.0000
C/2 | nominated: layers (1,) at post-identity | +0.0962 +0.0712 -0.0025 +0.0000 +0.0000
F/0 | nominated: layers (1,) at post-identity | +0.0887 +0.0787 +0.0425 +0.0000 +0.0000
F/1 | nominated: layers (1,) at action+3 | +0.0938 +0.0050 -0.0012 +0.0000 +0.0000
F/2 | nominated: layers (1,) at post-identity | +0.0750 +0.0650 +0.0200 +0.0025 +0.0000
M/0 | nominated: layers (1,) at post-identity | +0.1112 +0.1013 +0.0338 +0.0063 +0.0000
M/1 | nominated: layers (1,) at post-identity | +0.0787 +0.0800 +0.0238 +0.0100 +0.0000
M/2 | nominated: layers (1,) at post-identity | +0.1075 +0.0850 +0.0250 +0.0062 +0.0000
```

At the first running state the control as run is above nothing by 0.075 to
0.11 on every model except the separable one. What separates "the six" from
the rest is how much of that survives at the layer the rule happened to
choose: the entangled model's seed 1 and the free model's seed 1 also have a
layer-1 site and show almost nothing there. So the six-of-six match with
`post-identity` sites is a real pattern in these models, and it is not the
mechanism. The mechanism is the one the diagnostic names. This does not touch
the ruling.

**What the redefined control is, said plainly for the registration** (ARGUED
from A). Before both first own turns the donor's state and the recipient's
are the same numbers. Transplanting one into the other changes nothing by
construction, on any model. So the redefined control is a second known-answer
test, of the pairing and of the code's left-to-right property, alongside the
null transplant. It is right that a failure should withhold a reading,
because a failure means something is broken. **It should not be described
anywhere as showing that a model does not know its identity early.** The
packet's page 2 put this to John ("it can only fail if the pairing is
broken or if something in the text gives identity away early"), so the
ruling was made knowing it. One correction to that sentence: in this task the
twins' text is identical by construction, so the second way to fail cannot
arise here either.

## 6. What this check does not cover

It did not retrain anything, so it says nothing about whether other trained
copies of these models would give the same figures. It took the committed
models, the committed reads and the committed gate counts as given, checking
only that the model files match their fingerprint list (the script does that
on every run, and passed). It did not check the earlier rehearsal code the
script calls beyond reading the functions used. The agreement between the two
runs shows the script is repeatable on this laptop; it was not run on another
machine.

## 7. What should happen next

1. **Nothing returns to John from this check as a ruling.** Ruling 2 stands.
2. **For John to know, not to rule:** items 4.3 (the controls that hold are
   not enforced by the code), 4.8 (the ordinary competing solver was not
   measured under the new rule) and the plain description of the redefined
   control at the end of section 5.
3. **For whoever writes version 4:** quote 0.0099, not 0.0100, for the mixed
   model's seed 1; count the null transplant's places as fifteen; do not
   carry the sentence tying the six models to `post-identity` sites as a
   cause.
4. The short pre-stated run John ruled (the redefined control, the new
   reported figure, the other-agent control's code path) goes ahead, on its
   own branch, method first.

## 8. Files beside this one

`2026-10-03-controls-rerun-check-scripts/`: `independent_control4.py` and its
output `independent_control4.out` and `independent_control4.json`;
`compare_and_verify.py` and its output `compare_and_verify.out`;
`rerun_controls_stdout.txt`, what the re-run printed in this session;
`posthoc_control4_rerun.out`, the committed diagnostic run again.
