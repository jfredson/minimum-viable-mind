*This is file 16 of 33 of one review packet, pasted into a single conversation. It contains record 5 part 4 of 4 (the inside reviewer's findings on version 4 (Gate A, tier 1)). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 5 of 25, part 4 of 4 - the inside reviewer's findings on version 4 (Gate A, tier 1) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md` (complete file, 80,950 characters) =====
```
  gate bar 790 of 3,000; a model at one in four clears it with probability 0.0485
  no-transplant rule at own-directed 1.0: formula 0.0000; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.8712: formula 0.0184; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.56: formula 0.0629; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.2633: formula 0.1052; a broken pairing (0.125) flagged: True
  piece floor at 144 of 180: the competing solver's best piece 20 to 25, arm F's 34, the built arms' chosen pieces 150 to 180
  whole-state floor, printed formula, at the broken end (solver seeds 0 and 1): admits every site set (above)
```

**Disposition.** Control 6's two cells have trials on every arm and seed (the
empty-cell repair, ledger item RT-173, holds). Control 4 transplants at one
position or more in every pair. Control 2's cell is empty on the toy and the
text says so; it carries no line, by ruling. The two-of-three rule has never
been exercised and the text says so. **The channel-removal gate's battery
clause has no cell at all, in any record: RT-237.** At both ends: the gate,
the no-transplant rule and the piece floor pass the working end and refuse
the broken end; **the whole-state floor as printed passes the broken end
(RT-238).** Control 4's pass line has no working end to test, which version 4
already says.

### Failure 4. A claim of measurement with no record, or a record that does not reproduce — **fires twice, on two worth-noting sentences (RT-242, RT-243)**

*Part one, the two sweeps* (on sections 0 to 16 at `d19f914`, cut at
section 17's heading):

```
$ git show d19f914:docs/successor-experiment-proposal-2026-10-03-v4.md | awk '/^## 17\. /{exit} {print}' > v4-through16.md
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' v4-through16.md
761
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' v4-through16.md
235
$ wc -l < v4-through16.md
3449
```

(Section 17 prints 759, 233 and 3,406, from before the late-evening rulings
were written in; the check of version 4 found the same 761 and 235. The
hits were read through the closure rule's own narrower question, next.)

and the closure rule's own check, every paragraph using verified, measured,
calibrated or attacked, and whether it names a record (`closure_sentences.py`):

```
paragraphs in sections 0 to 16: 274; using one of the four words: 99; of those, naming no file, commit, ledger item, section, page, ruling or item: 13
```

The thirteen were read one by one (`closure_sentences.out.txt` prints them in
full). Four are headings. Five use "measure" as the name of the instrument, or
sit in the opening summary, the quoted question or a sentence about what a
check is for, and claim nothing the body does not cite. Two are tables whose
source is named in the sentence above them (section 12.4). One is the
statement that the tripwire's ratios are measured against the posted rate,
which is a rule, not a claim. One says the transplanting code "proves the
restriction as a tensor identity in its self-test (rehearsal item R-8)", which
names the rehearsal record's item; that record (section 2a, R-8) says "The
restriction property is proved as a tensor identity at full rank". **No claim
of measurement lacks a record.**

*Part two, the records hold what the sentences say.* The check of version 4
compared 89 figures of 2026-10-03 against their files and did not re-derive
the older ones (its section 5). This review did the older ones
(`older_figures.py`, full output in `older_figures.out.txt`):

```
strong transplant, version 1 form / chance-corrected form      v4: 0.4323 / 0.5018     file: 0.4323 / 0.5018
weak transplant, version 1 form / chance-corrected form        v4: 0.3222 / 0.5013     file: 0.3222 / 0.5013
largest |measured - formula|, and where                        v4: 0.017536, free arm  file: 0.017536 at F/2
same-value trials, distinct grammar                            v4: 0 of 4,000          file: 0 of 4000
blind solver, strict set to relaxed set                        v4: 0.2467 to 0.3095    file: 0.24675 to 0.3095
arm T own-directed on unseen marker words, seeds 0/1/2         v4: 0.7612, 0.6512, 0.6512   file: 0.76125, 0.65125, 0.65125
negative readings on that pool (rehearsal R-4)                 v4: -0.1706 and -0.2755 file: -0.1706 and -0.2755 (version 1 form)
arm T seed 0 on the grammar attempt's unseen pool              v4: -0.1870             file: -0.1870
curriculum: named-other seeds clearing, counts                 v4: 0 of 3              file: 0 of 3, [232, 580, 429]
reweight: named-other seeds clearing, counts                   v4: 0 of 3              file: 0 of 3, [695, 619, 713]
grammar attempt: named-other counts; own-directed mean; level  v4: 774, 730, 759; 0.5654; 0.5513   file: [774, 730, 759]; 0.5654; 0.5513
the grammar check's own re-run                                 v4: 750, 809, 739       file: 750, 809 and 739 found
fourth_arm.entangled_share, seeds 0/1/2                        v4: 0.60375 (483 of 800) file: 0.60375, 0.60375, 0.60375
ms per step T / C / F                                          v4: 13.08 / 13.52 / 12.53   file: 13.08 / 13.52 / 12.53
arm C slowest step over its median                             v4: 2.9%                file: 2.8%
out-v3-rules/models_sha256_check.json all_agree                v4: true                file: True
```

Every figure matches its file. Two small notes: the negative readings
−0.1706 and −0.2755 are in the version 1 form of the reading (the
chance-corrected form gives −0.1917 and −0.3303 on the same rows), which
version 4 quotes only as "negative" except in this one place (line 2387 quotes
−0.1870, which is the chance-corrected form, from a different run); and arm
C's slowest step is 2.85 percent over its median from the unrounded fields
(2.9 from the rounded milliseconds), inside the "within 3%" the text claims.
Neither is a finding. **Where the entry fires:** the label-search sentence,
whose record says something else (RT-242), and the floor-forms sentence,
whose cited record is right and whose "on the toy" is wider than any record
(RT-243).

The repository's two checkers were not run again here: the check of version 4
ran both on this same file (its section 2.5) and this review changed nothing
they look at.

### Failure 5. A command that creates something while documented as creating nothing — **does not fire**

Version 4 runs nothing against a vendor. The list's own test, run by this
session after reading the launchers' dry-run paths (each stops before its first
vendor command):

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
...
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

(exit status 0; full output in `failure5_launcher_guard.out.txt`, every line
`[ ok ]`, with the standing prohibition on the registered launcher printed as
expected). The launcher version 4 names (`launch_a3_fetch_first.sh`) carries
the guard. The gap version 4 itself states stays open: the training entry
point for the built models on the rented machine does not exist.

### Failure 6. A remote step tested only against stand-ins — **does not fire on the launcher; four steps of the design are untested at the far end, and the text says so for each**

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)
negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.0s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang
all checks pass. Nothing was rented and nothing was spent.
```

**What stood in for the far end, step by step.** The shutdown handshake's
machine half: local stand-ins only (stated, weakness W9). The mixed model's
code on the rented machine: never run (W9; step 4 is the first time). The
tripwire: no code (section 12.5). The registered measurement code itself, run
on a full-size model on the laptop's processor: never run; the toy code at
the toy shape stood in for it, and this review's timing is the first
measurement at the registered shape (RT-245). Each is said in the text; none
is counted as tested.

### The drafted seventh entry (not yet on the list)

Version 4 ran it; this review notes only where it fires on the text that
results once the ruled changes are written in: on the battery clause (RT-237:
a gate line the design cannot produce on any path) and on the fallback's
outcome (RT-241: an outcome the design can reach and cannot name).

---

## The decisive measured checks

The protocol asks for at least one check on the text being registered that
would come out wrong if the text were wrong. Two were run.

### Check 1. The rule as the text states it, run on the committed development grids

`rule_from_text.py` implements, from version 4's sentences alone and without
importing any of the checked code, the site-set family and its two exclusions
(section 7.2, item 2), the whole-state floor as printed (section 6.4, item 1),
the smallest clearing layer set per position set with ties to the earliest
(item 4), the piece rule at 144 of 180 applied after the layers (item 3), and
the choice by the highest development ownership-only share with ties to the
smaller size and then the earlier position set (item 5). It runs that rule on
the committed development grids of the twelve toy models and compares its
choice with the committed code's, for the primary and the stricter row; then
computes the reading, the no-transplant rule, the three controls that hold,
the two-of-three rule, the separation and the outcome term, all as the text
states them.

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/rule_from_text.py
=== 1. Nomination: the text's rule against the committed code's choice, twelve toy models
primary  T/0: text -> nominated, ((0,), 'action', 8); code -> nominated, ((0,), 'action', 8); same: True
...
primary  C/1: text -> nominated, ((1,), 'action+3', 8); code -> nominated, ((1,), 'action+3', 8); same: True
primary  C/2: text -> nominated, ((1,), 'post-identity', 4); code -> nominated, ((1,), 'post-identity', 4); same: True
primary  F/0: text -> read failed its floor: no size's piece reaches four fifths, None; code -> read failed its floor: ...; same: True
...
stricter T/0: text -> nominated, ((1,), 'action', 8); code -> nominated, ((1,), 'action', 8); same: True
...
agree on 24 of 24 (twelve primary, twelve stricter)

=== 2. The reading on fresh episodes, from the text, against the committed degree
T/0: text degree 0.0000; committed 0.0000; no-transplant miss +0.0000; controls 7/1/4 True/True/True; gate True -> reads
C/0: text degree 1.0051; committed 1.0051; no-transplant miss -0.0132; controls 7/1/4 True/True/True; gate True -> reads
C/1: text degree 0.9926; committed 0.9926; no-transplant miss -0.0111; controls 7/1/4 True/True/True; gate True -> reads
C/2: text degree 0.9974; committed 0.9974; no-transplant miss -0.0039; controls 7/1/4 True/True/True; gate True -> reads
F/0: text degree 1.0000; committed 1.0000; ... gate False -> no verdict: read failed its floor (described only), fails its gate
M/0: text degree 0.4886; committed 0.4886; no-transplant miss -0.0059; controls 7/1/4 True/True/True; gate True -> reads
...
=== 3. Two seeds of three, the separation, and the outcome term (section 3)
arm T: reads on 3 of 3 seeds: [0.0, 0.0, 0.0]
arm C: reads on 3 of 3 seeds: [1.0051, 0.9926, 0.9974]
arm F: reads on 0 of 3 seeds: []
arm M: reads on 3 of 3 seeds: [0.4886, 0.486, 0.5449]
separation, lowest of arm C minus highest of arm T: 0.9926; clears 0.5: True
outcome by the text's rules: the fifth term, metric validated, degree not read
```

(full output, every row, in `rule_from_text.out.txt`).

**Does it match what the text claims?** Yes. The rule the text states picks
the same site set, the same size and the same verdict as the code that ran, on
all twenty-four rows, including the entangled model's seed 1, where the choice
was decided by one episode in 600, and the free model's three "read failed its
floor". Every reading equals the committed one to four places; the separation
under the reconciled rule is 0.9926; and the text's own outcome rules put the
toy where version 4 says it is, on the fifth term. Had the text described a
different order of rules, a different tie-break or a different floor from the
one that ran, this would have come out different on at least the entangled
model's seeds 1 and 2. The one place the text and the code differ (the floor's
clause for a requirement at or below zero) does not bite on these twelve
models, and section 4 of the same output shows where it does (RT-238).

### Check 2. The committed code, run again from clean, against its committed outputs

`rerun_controls.py`, unchanged, run from a copy of `src/` whose output folder
points into this session's scratch space (the committed models, reads and gate
file linked in read-only, the models first checked against `SHA256SUMS` by the
script itself), then compared value by value with `compare_rerun.py`:

```
$ cd <scratch copy>/src && .venv/bin/python rerun_controls.py        # the committed code, unchanged; "done in 1485s"
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/compare_rerun.py <scratch copy>/out-controls-rerun
measure_C_seed0.json     values compared    110; differ 0
measure_C_seed1.json     values compared    110; differ 0
measure_C_seed2.json     values compared    110; differ 0
...
nominate_T_seed2.json    values compared   1980; differ 0
summary.json             values compared   1497; differ 0
table.md identical: True
TOTAL: 25 JSON files, 26722 values, 0 differ
fresh run: separation field {'0': 1.0051, '1': 0.9926, '2': 0.9974} | device cpu | torch 2.12.1 | seconds 1485
```

(every file's line in `compare_rerun.out.txt`).

**Does it match?** Yes. Every value the committed code wrote on 2026-10-03,
26,722 of them in 25 files, came back identical on this laptop today, and the
table is byte-identical; only the running time differs (1,485 seconds against
the committed 967, because this session ran other scripts alongside it). The
per-seed separation field is 1.0051, 0.9926 and 0.9974, whose lowest minus
arm T's highest is the 0.9926 of check 1. This repeats what the check of the
controls re-run (at `e184a6e`) found; it is repeated because the registration
leans on these files and the protocol makes their verification the tier 1
reviewer's.

### What these two checks do not cover

They cover the procedure on the toy. They do not cover the registered width
(RT-240), the registered generator (RT-239), the battery clause (RT-237) or the
outcome states the toy never reached (RT-241); those are the findings.

---

## The kill case

The case for not registering this text, as strongly as it can be put. The
registration's purpose is to fix in advance what would count as a result; as
written it fixes one thing that would make its best outcome impossible and
leaves several reachable outcomes without a name. The free model's gate
carries a clause about batteries that the task does not contain and that no
run has ever evaluated, and the design's own rule turns an unevaluable gate
into a failure, so "degree read" cannot be reached as written. The episode
counts it freezes were chosen because they were the only ones rehearsed, but
they were rehearsed at a third of the registered width, and a stand-in at the
registered width puts the high anchor under its own floor on two seeds of
three; if that happens the experiment falls into a two-model fallback that has
no registered outcome term, after both releases of money are drawn. The grammar
it registers is described by reference to a generator that shows the model its
own name as it acts, which is the one cue the whole design exists to keep out,
and the two lines that keep it out are not in the text. And the floor that is
meant to keep the divisor off zero "by construction" does so only through a
clause in code the text does not carry. None of this is expensive to fix: one
ruling on a clause, one sentence on the floor, one page on the episode format,
one table of outcomes, and either more fitting episodes or a rehearsal at
width 448 on the laptop. But every one of them is the kind of thing this
programme has already paid for once in a registered sentence nobody could
satisfy, and the registration commit is the one commit that cannot be taken
back.

---

## For the outside reviewers

Not a ruling; for the session that builds the tier 2 packet.

**(a) The files an outside reader who cannot run code most needs.**

1. `docs/successor-experiment-proposal-2026-10-03-v4.md`, with the list of
   ruled changes in this review's section "The registration text as
   reviewed".
2. `docs/rulings/2026-10-03-version-4-questions-rulings.md` (record B), the
   reconciliation `docs/rulings/2026-10-03-seven-questions-reconciliation.md`,
   `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` and
   `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`.
3. `docs/2026-09-21-successor-measure-rehearsal.md` (sections 0, 3, 5, 6, 7,
   8): what the instrument does on built models and where it first failed.
4. `docs/2026-10-03-controls-rerun.md` and `docs/2026-10-03-competing-solver-run.md`:
   the toy figures under the rules as registered, and the ordinary competing
   solver.
5. `docs/known-failure-modes.md` and `docs/outside-review-protocol.md` (the
   brief and the closure rule).
6. This review, and the two checks it builds on:
   `reviews/2026-10-03-proposal-v4-check-claude-code.md` and
   `reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`.
7. The two grammar headers, which say in prose what RT-239 is about:
   `experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (lines
   1 to 115) and `experiments/rehearsal-successor-measure/src/grammar.py`
   (lines 1 to 65).

**(b) Questions this review could not settle, for a reader from another lab.**

1. **Does a reading near 1 on the entangled model say anything the
   construction did not already guarantee?** Any piece that holds the label at
   the action position and moves nothing reads near 1. Is there a design
   change that would let the high anchor fail in an informative way, rather
   than only by its whole-state transplant missing the floor?
2. **What fit floor and fitting-sample size would you register for a
   twelve-way straight-line read on a 448-wide state?** RT-240 shows the
   ruled 420 fitting episodes are fragile under a crude stand-in; what would a
   lab that does this routinely use, and would it fix the regularisation in
   advance?
3. **Is the separation rule's asymmetry right?** It sets aside a seed that
   returns no verdict and counts a seed that returns an odd reading
   (the check-questions ruling, ruling 2). For a claim of "metric validated",
   is that the conservative direction, or does it make the result hostage to
   which failures happen to trip a floor?
4. **Is a mixture by item a fair middle anchor for a measure meant to read
   partial separation within each act?** The design says it is not, and keeps
   the mixed model anyway (W10). What middle anchor would you build at this
   size?
5. **Should the name cue at the moment of acting be closed by the grammar, or
   tested for by a control?** RT-239 asks the text to register the grammar
   that removes it. An outside reader may know a cleaner discriminator than
   removing it, one that would let a free model's reading be checked for
   reliance on a name.

---

## Scripts and outputs beside this file

In `reviews/2026-10-04-successor-v4-gate-a-scripts/`, each run from the root
of the checkout with the project's own Python (torch 2.12.1, scikit-learn
1.9.0, numpy 2.5.0, scipy 1.18.0), on the processor:

| Script | What it does | Output |
|---|---|---|
| `rule_from_text.py` | the decisive check: the rule from the text, on the committed grids; the reading, the controls that hold, the seeds rule, the separation and the outcome; the floor on the competing solver | `rule_from_text.out.txt` |
| `compare_rerun.py` | compares a fresh run of `rerun_controls.py` with its committed outputs | `compare_rerun.out.txt` |
| `failure_mode_pass.py` | the known-failure list's tests 1 to 3 on the committed outputs | `failure_mode_pass.out.txt` |
| `older_figures.py` | figures version 4 quotes from records older than 2026-10-03, against their files | `older_figures.out.txt` |
| `closure_sentences.py` | every paragraph using verified, measured, calibrated or attacked, and whether it names a record | `closure_sentences.out.txt` |
| `floor_forms.py` | where the two forms of the whole-state floor disagree, across every committed grid | `floor_forms.out.txt` |
| `solver_sentence.py` | the ruled sentence about the competing solver, against its outputs | `solver_sentence.out.txt` |
| `width_vs_count.py` | the width stand-in (NOT A RESULT) | `width_vs_count.out.txt` |
| `registered_shape_timing.py` | forward-pass timing at the toy and registered shapes on the processor | `registered_shape_timing.out.txt` |
| (the repository's) `check_launcher_argument_guard.sh`, `check_remote_forms.py` | failures 5 and 6 | `failure5_launcher_guard.out.txt`, `failure6_remote_forms.out.txt` |
===== END OF RECORD 5, part 4 =====

