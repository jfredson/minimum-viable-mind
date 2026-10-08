# Check of version 5 of the successor registration text (2026-10-08)

*Written 2026-10-08 (Pacific) by a Claude Code session that wrote none of
the three files under check, on branch `check-successor-v5-2026-10-08`, cut
from the drafting branch `successor-v5-registration-draft` at its tip
`641a29e` (the balance correction to STATUS and the site data). Laptop only;
nothing rented, created, trained or spent: $0. No file under check, no
ruling, `STATUS.md` and `data/project.toml` were edited. Nothing was merged.*

*Written under the workspace plain-language rule (`~/Code/CLAUDE.md`, ruled
2026-08-30). Every count below is labelled **MEASURED** with the command that
produced it; every judgement is labelled **ARGUED**. Every finding number,
pull request number, commit and branch carries a phrase saying what it is.*

**The three files under check**, all on the drafting branch:

- version 5, `docs/successor-experiment-proposal-2026-10-07-v5.md` (5,550
  lines), "version 5" below;
- its method, `docs/successor-registration-method-2026-10-07.md`;
- its handoff, `docs/successor-registration-handoff-2026-10-07.md`.

**The verdict in one sentence (ARGUED).** Version 5 carries every ruling of
2026-10-07 and 2026-10-06 in substance and every figure it quotes matches the
file it names, and it may be committed as the registration once the fifteen
branches it cites are on the main line and the five must-fix items below are
applied; three of those are slips in the text (a stale closing section left
over from version 4, two places that still name the fifth term by its old
words, and a scope rule that drops the eighth term), and two are the edits
owed to the two rulings John gave today.

---

## 1. What was read, and what was run

**Read in full:** the method and the handoff; version 5's header and source
table, sections 0, 3, 5.6, 8, 11, 12, 16, 17, 20 and 21 and its closing
section; the whole plain `diff` between version 4
(`docs/successor-experiment-proposal-2026-10-03-v4.md`) and version 5 (3,558
lines), which covers every other section where version 5 differs from
version 4; the ruling of 2026-10-07 on the two-sided question
(`docs/rulings/2026-10-07-two-sided-question-rulings.md`, main line); the
twelve-page ruling of 2026-10-06 on the registration review with its
same-day follow-ups (`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`,
branch `rulings-2026-10-06-gate-a-v4` at `525a625`) and the two dispositions
files it adopts (the inside dispositions,
`docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`, and
the outside dispositions,
`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`,
same branch); the ruling of 2026-10-04 on the competing-solver run
(`docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`, main
line); the two rulings of today on the main line: the verification-bar
ruling (`docs/rulings/2026-10-08-verification-bar-ruling.md`, landed by pull
request 126, the ruling that keeps the bar at 0.5) and the December-result
restatement rulings (`docs/rulings/2026-10-08-december-result-restatement-rulings.md`,
landed by pull request 128) with the one-page restatement they adopt
(`docs/rulings/2026-10-08-december-result-restatement-PROPOSAL.md`).

**Read for the figures:** the sharpness-fix findings and the bars section of
its method (`docs/2026-10-06-sharpness-fix-inuse-check-findings.md` and
`...-method.md`, branch `fix-sharpness-inuse-check` at `644238e`); the page 4
re-run's findings and its comparison table
(`docs/2026-10-06-page4-toy-rerun-1800.md` and
`experiments/rehearsal-successor-measure/out-page4-rerun-1800/comparison.md`,
branch `page4-toy-rerun-1800` at `e948899`) and the opening of its check
(`docs/2026-10-07-page4-rerun-check.md`, branch `check-page4-rerun` at
`1e168f3`); the check of the four development runs
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-claude-code.md`,
branch `check-dev-10m` at `51ec07d`); the decoy test and its check
(`docs/2026-10-06-decoy-test.md`, branch `decoy-test-a6` at `6794155`;
`docs/2026-10-06-check-decoy-test.md`, branch `check-decoy-test-a6` at
`ba5d64f`); the compute ledger's rows of 2026-09-25 and 2026-10-04 (lines 95
to 99 of `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`);
and, by search only, the code freeze report, the training-exclusion
findings, the third check of the spending-alarm fixes, the inside Gate A
review, the Gate C pass of the two-sided proposal and the development runs'
go packet.

**Run** (every command from the root of this worktree unless said
otherwise; `.venv/bin/python` is the project's own Python at
`/Users/john/Code/minimum-viable-mind/.venv/bin/python`):

- `diff` and `diff -U0` between version 4 and version 5, and a script of
  this session's (`map_hunks.py`, scratch folder) that places every hunk in
  the version 5 section it lands in;
- the two text sweeps and the em-dash counts of section 17, on sections 0
  to 16 of version 5 cut at the section 17 heading;
- `scripts/check_citations.py --only` and `scripts/check_single_source.py
  --only` on version 5;
- `experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh`
  and `src/check_remote_forms.py`;
- `git archive e948899 experiments/rehearsal-successor-measure/out-page4-rerun-1800/models-1800`
  into the scratch folder, and a script of this session's
  (`recompute_rows.py`) that recomputes section 17's failure 1 and failure
  2 tables from the twelve row files and `summary.json`;
- a script of this session's (`arith.py`) that recomputes the two binomial
  lines, the no-transplant formula lines, the part A sharpness arithmetic
  and every money line of section 12 and section 17's candidate 7;
- `git cat-file --batch-check` over every path the citation checker could
  not find, against the fifteen cited commits, the main line and this
  branch;
- `git for-each-ref` and `git log --no-walk` over the fifteen branches and
  twenty-three commits version 5 cites, to confirm each exists and is what
  version 5 says it is.

The drafting session's own `failure_pass_v5.py` is not committed (section
17 says it is kept in that session's scratch folder), so it could not be
re-run as a script; every block of section 17 whose inputs are committed was
recomputed with this session's own commands instead.

---

## 2. Findings

Labels: **must-fix** (the registration should not be committed with it in),
**should-fix** (a defect that does not change what is registered), **note**
(for the record).

### 2.1 The diff against the change log (handoff section 5, item 1)

**MEASURED.** `diff docs/successor-experiment-proposal-2026-10-03-v4.md
docs/successor-experiment-proposal-2026-10-07-v5.md | wc -l` gives **3558**,
as the handoff says. `diff -U0 ... | grep -c '^@@'` gives **157 hunks**.
Placed by section (`map_hunks.py`): header 5; source table 2; section 0, 1;
1, 1; 2, 1; 3, 9; 4.1, 3; 4.3, 1; 5 intro, 2; 5.1, 1; 5.2, 3; 5.3, 3; 5.4,
1; 5.5 (including the whole of the new 5.6), 3; 6.1, 1; 6.4, 4; 7.1, 1; 7.2,
3; 7.3, 4; 7.4, 6; 7.5, 3; 8.1, 2; 8.2, 5; 9, 5; 10, 9; 11, 5; 12.1, 3;
12.3, 1; 12.4, 1; 12.5, 2; 12.8, 1; 13, 8; 14, 2; 15, 3; 16, 1; 17, 43; 19,
3; 20, 3; 21, 1; the closing section, 1. No hunk lands in sections 4.2, 4.4,
6.2, 6.3, 12.2, 12.6, 12.7 or 18, which the log lists as left alone; the one
hunk in 7.1 is the one bullet the log names.

**Every log entry has a hunk** (ARGUED from the placement above read against
section 20: every section each entry names has at least one hunk, and the
diff text at that place says what the entry says).

**Two hunks no entry names:**

1. **Must-fix (finding 1).** The last hunk, `@@ -4211,0 +5533,10 @@`, adds
   version 5's closing section *before* version 4's closing section instead
   of in place of it, and without a line break between them. Version 5's
   last eight lines (5543 to 5550) are version 4's text: "It edits nothing:
   not version 3 ... It does not open the registration review, and it is not
   ready for it: the competing solver's run under the piece rule is owed,
   and this version and the record of the late-evening ruling are owed a
   check". Every clause of that is false of version 5 and contradicts
   sections 7.3, 10 and 11, which say the solver's run was done, checked and
   ruled on 2026-10-04. MEASURED: `sed -n '5541,5543p'` prints
   `that commit, with everything ruled by 2026-10-07 written in.**## What
   this version does not do`, the two headings joined on one line. Section
   20 says "nothing in that diff is outside this list" and names the
   closing section nowhere. Fix: cut the stray heading off the end of line
   5541 and delete lines 5542 to 5550.
2. **Note (finding 2).** The hunk `@@ -4056,3 +5298,6 @@`, the last
   paragraph of section 19 ("the five rulings of 2026-10-03 ... were each
   given as agreement to a packet"), is a rewrite of version 4's "the three
   rulings of 2026-10-03"; the log's entry for section 19 names only its
   "heading and intro". The change is right (it counts the two late-evening
   records and the night ruling); the log should name it.

The handoff says version 5 was built by "78 replacements"; the build script
is not committed, so that count cannot be checked against the 157 hunks
(note).

### 2.2 The ruled changes against their rulings, word by word (handoff section 5, item 2)

Each adopted passage was read in version 5 against the dispositions file the
2026-10-06 ruling names, and against the 2026-10-07 and 2026-10-04 rulings.

- **The outcome table's terms (open item 3).** The six registered terms are
  the inside dispositions' RT-241 table (the outcome-map finding) and the
  outside dispositions' A10 changes, with "metric" replaced by
  "instrument" as decision 3 of 2026-10-07 directs; version 4's names stand
  beside each. Faithful (ARGUED), and rightly marked open item 3.
- **The fifth term's row** adds "or, having passed its gate at step 5a,
  fails it at step 5b", which is the outside dispositions' A10 text change 2
  as ruled on page 9. Faithful.
- **Rule 1** adds arm F's exception after step 5a: A10 text change 2 again.
  Faithful.
- **Section 8.1's R3 sentence** is the inside dispositions' RT-241 text
  change 2 with A10's "arm F excepted after step 5a" folded in, plus "and on
  which seeds", which the drafted text does not have but section 3's R3 row
  does ("names the arm, the condition and the seeds that failed", carried
  from version 4). Consistent with itself; note only.
- **The no-transplant item (section 6.4, item 3)** carries the outside
  dispositions' A9 text as ruled on page 8, with the control 4 reading of
  follow-up item 3, and ruling 3 of 2026-10-04 (the formula is reported, not
  generalised) folded in before it. One phrase is the drafting session's
  own and unsourced: "as the toy's competing solver did at about twice the
  formula" (note).
- **The twenty other adopted passages** (RT-237 text changes 1 to 5 in
  section 8.2; RT-238 in 6.4 item 1 and the section 9 row; RT-239 in 4.1;
  RT-240 in 7.2 item 1 and W15; RT-242, RT-243, RT-244, RT-245, RT-246; A7
  in 6.1, 7.3 item 6 and W11; A8 in section 10 and W5; A11 and A12; A6 in
  section 3, W12 and R-12; A2 as R-13 and 6.4 item 5; the joint seed rule
  of page 7 in sections 3, 8.1, 8.2 and 9; RT-255 and the training
  exclusion in 4.1, 4.3 and 7.1; the seven rulings of 2026-10-04 in 7.3's
  last paragraph, 7.4, 7.5 and 8.1) say what the drafted text says, with
  changes of tense, cross-reference and the plain-language rendering of the
  episode format (RT-239's angle-bracket tokens are described in words).
  Faithful (ARGUED, read passage by passage).

**One contradiction with the 2026-10-06 ruling, must-fix (finding 3).** The
scope rule of section 3 reads: "Wherever a term containing 'instrument
discriminates' or 'instrument checked' appears ... it is followed in the
same sentence by 'on these constructed systems, for this intervention
procedure'; so is R2." The eighth term, "instrument not validated" (version
4's "metric not validated"), contains neither phrase, so the rule as
written drops the scope phrase from it. The ruling's follow-up item 2, in
John's word "yes", says "the three new terms of page 5, which all contain
'metric', carry the first phrase too", and names "metric not validated"
among them. Open item 4 asks whether the phrases travel with the renamed
terms at all, and the text says it keeps them meanwhile; keeping them means
keeping them on all four new terms. Fix: "a term containing 'instrument
discriminates', 'instrument checked' or 'instrument not validated'".

### 2.3 Every figure new in version 5 against its file (handoff section 5, item 3)

**MEASURED, every figure below read in the cited file at the cited commit
and compared with version 5's sentence; none differs.**

- *The sharpness findings* (`644238e`, sections 2, 4 and 5): sharpness
  −0.089 and −0.008 at 10 million, weights 0.218 and 0.247, arm T 1.947 and
  0.942; toy sharpness 1.73, 0.70, 0.93 and 2.84, 2.69, 2.42; weights 0.914,
  0.573, 0.681 rising to 0.999; no seed losing more than 36 of 3,000; route
  use 0.269, 0.233, 0.221 before and 0.285, 0.273, 0.244 after on arm C;
  0.071, 0.090, 0.109 and 0.090, 0.106, 0.100 on arm M's stirred-in route;
  1.000 on arm T and arm M's separable route; 0.018, 0.000, 0.924 on the
  10-million checkpoints; arm T seed 0 re-read at 0.0000; 14 made-up cases,
  28 decision-code cases. The bars 0.9 and 0.5 are the method note's section
  2, and the frozen code on that branch carries them (`ROUTE_WEIGHT_MIN =
  0.9`, `ROUTE_USE_MIN = 0.5` in `experiments/08-successor-degree/src/measure.py`).
  The part A arithmetic reproduces: with the signal fired twice, a sharpness
  of 4.0 gives a weight of 0.9990 and 1.65 gives 0.9004 (`arith.py`).
- *The page 4 re-run* (`e948899`, section 2 and `comparison.md`): arm C
  1.0026, 1.0000, 1.0000; arm M 0.5252, 0.4793, 0.5208 with true-slot
  0.5000, 0.4760, 0.4920; arm F's best piece 40, 19, 36; arm C's pieces 178,
  178, 165 (from 180, 172, 150); site set or size moved on five models of
  fifteen; control 2 on arm F seed 0 from 140 to 176, piece 171; 471 against
  27 iteration-limit warnings on arm M; the reproduction check 29,154 and
  11,712 values. The check's "40,855 values, none different" is what the
  re-run's corrected findings state. Section 17's failure 1 and failure 2
  tables reproduce exactly from the twelve row files (`recompute_rows.py`:
  every untouched, whole and own-directed figure, every denominator, every
  whole-read and best-piece count per state, the smallest denominator 0.4863
  on arm C seed 2, lowest arm C minus highest arm T 1.0000, arm M's
  prediction met). The committed `summary.json` carries the outcome `R3`,
  "substrate not a testbed", reason "arm(s) F failed the gate", as section
  17 prints it; it has no `separation` field, so that line of section 17 is
  the script's arithmetic on the readings, which is right.
- *The development-runs check* (`51ec07d`, sections 3 to 7): step times
  0.0099, 0.0100, 0.0093, 0.0145; the ratio 1.44 against 1.11; ratio B 0.401
  against 0.990; $1.4565 drawn against $1.4713 expected; balance $73.7742
  to $72.3178; arm T's 2,750 and 2,913 of 3,000, six confused name pairs, 76
  of 76, 2,999 of 3,000 with the row forced, 0.0802 under the stricter
  variant; arms C and M's best pieces 41 and 45; arm C's 0.595 beside arm
  F's 0.5975. The $0.60 to $1.25 estimate per run is the go packet's
  (`docs/rulings/2026-10-04-development-runs-go-PROPOSAL.md`, line 53).
- *The decoy test and its check* (`6794155`, `ba5d64f`): 0.0000 on all six
  runs and the four supplementary ones; piece shares 0.9370, 0.9341, 0.9382
  and 0.0588; the probe's 0.28, 0.23, 0.29 at 8 directions and 0.52 to 0.96
  with fewer; reproduced byte for byte.
- *The dispositions' measurements* (`525a625`): 2,100, 2,238, 2,324 against
  1,546; untrained 0, 620, 726; 554; about 2,257; 18 patterns of 512; 0.0667
  against 0.0286, gap 0.0381; 0.99 and 0.56; the candidates 0.733, 0.383,
  0.478 and at most 0.417 and 0.633; 576, 892 and 1,080 rows; 0.109 and
  0.091; 4.59 seconds, about two hours, about 25 hours.
- *The ledger's four 2026-10-04 rows* (lines 96 to 99): $0.47, $0.34,
  $0.33, $0.33; "After this run" $228.62, $228.96, $229.29, $229.62;
  development line $1.47 spent; the wave balance $73.7742.
- *Other figures spot-checked by search:* the freeze's 195 checks, 502
  figures and 325 site sets; the training exclusion's 227 checks and
  5,228,112 contents; the alarm's third check "safe for the approved $1.14
  reruns", 82 checks, 28 seconds; the inside review's 24 of 24 and 26,722;
  the Gate C pass's RT-262 (the narrowing-leaves-no-outcome finding) and
  RT-271 (the dated-amendment finding); the ledger's RT-145 row (the
  uncommitted-citation finding).

**The money lines of section 12, recomputed (`arith.py`), all as version 5
states:** $228.15 + $1.47 = $229.62; $450 − $229.62 = $220.38; the
development line $1.47 spent, $1.14 for the reruns, $2.61 committed, $7.39
left, $8.53 left before the reruns; the rehearsal line $9.43; $44 + $119.06 =
$163.06; arm M at $32 leaves $26.79 and at $44 leaves $14.79, both over the
$10 floor; the note's split leaves $27.95 and $15.95; the second release
$159.90 to $171.90 on the note's split and $149.06 to $161.06 on the ruled
split; arm M at 1.44 times $10.04 over three runs $43.37; the four runs'
machine lives at $0.99 an hour give $1.4635 against the $1.4565 drawn.

### 2.4 The failure-mode pass of section 17, re-run (handoff section 5, item 4)

- **The text sweeps. MEASURED.** `awk '/^## 17\. /{exit} {print}'` on
  version 5, then the two `grep -c` lines of section 17, give **1144** and
  **401** on **4707** lines, with 105 MEASURED and 16 ARGUED. Section 17 and
  the handoff print 1,136, 399 and 4,691. The file has one commit
  (`c9b0259`, the version 5 draft), so the pass was run on the text before
  its last sixteen lines of sections 0 to 16 were added and not re-run.
  **Should-fix (finding 4):** re-run and reprint the three counts.
- **Em-dashes. MEASURED.** `grep -c` for the em-dash character and for
  the en-dash character return 0 and 0 on version 5, and 0 and 0 on the
  method and the handoff.
- **The citation checker. MEASURED.** `scripts/check_citations.py --only`
  on version 5 reports **54** references naming a file not in the
  repository (section 17 says 50), 11 bare names matching more than one
  file, 12 run-output names, 14 wildcards, and 1 exact figure absent from
  its cited file (the 1,810 count, as section 17 explains). The 54 are 33
  distinct names. Probed against the fifteen cited commits with `git
  cat-file --batch-check`: 28 exist on the branch version 5 cites for them;
  `comparison.md` is the bare name of a file that exists there; the two
  review scripts `failure_mode_pass.py` and `solver_sentence.py` exist in
  the inside review's scripts folder on branch `gate-a-tier1-successor-v4`
  at `135c1f7`; and **two names exist at no commit: `failure_pass_v5.py` and
  `scan_ids.py`**, the drafting session's own scratch scripts. Section 17's
  gloss, "none is a file that exists at no commit", is wrong for those two,
  which section 17 itself says are kept in a scratch folder.
  **Should-fix (finding 5):** reprint the count as 54 and say which two are
  uncommitted scripts, or commit the two scripts beside the handoff.
- **The single-source checker. MEASURED.** 2 and 2, the same two dollar
  figures and the same two sentences section 17 names.
- **The launcher argument-guard check. MEASURED.** "all checks pass.
  nothing was created and nothing was spent.", exit 0.
- **The remote-forms check. MEASURED.** "all checks pass. Nothing was rented
  and nothing was spent.", exit 0 (the stand-in returned after 8.1 seconds
  here against 8.0 printed; a timing difference and nothing else).
- **The binomial lines. MEASURED** (`arith.py`, exact tail): 790 of 3,000,
  share 0.2633, tail 0.0485; 1,546 of 3,000, tail 0.0483; the no-transplant
  formula 0.0000, 0.0184, 0.0629 and 0.1052 at the four accuracies, each
  more than 0.018 under 0.125.
- **The red-team ledger. MEASURED.** `grep -c 'RT-23[0-9]\|RT-24[0-9]\|RT-25[0-9]'`
  on `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`
  returns 0; its last row is RT-211. Section 17's "0 of 10" and "0 of 10"
  hold, and open item 12 stands.
- **Failure 1, 2 and candidate 7's tables.** Reproduced from the committed
  rows as section 2.3 says.

### 2.5 The decisions the drafting session made on its own (handoff section 5, item 5)

| Decision | How the text marks it | Overturn? (ARGUED) |
|---|---|---|
| The wording of the eight outcome terms | open item 3, in the body and section 21 | No. The session's own doubt about "instrument not validated" is right: "validated" is the word being retired. John sets the words; the alternative the session offers is the better one |
| Keeping the scope phrases | open item 4 | No. Keep them, on all four new terms (finding 3) |
| Treating arm T's rerun like arms C and M in the stop condition | open item 6, stated in 5.6 and 11 | No. The verification-bar ruling of today leaves this open by name; the text's reading is the safe one |
| The trainer's defaults as the registered recipe | open item 5, in 5.5 and the section 9 row | No. Section 5.5 says what it is and whose call it was |
| The 1,800-fitted toy figures as the registered toy record, the 420 ones as the earlier record | marked as ruled (page 4) with the re-run's findings directing it; not marked as the session's own | No. The page 4 ruling and the re-run's section 4 direct exactly this; the caution that the models were the learned-sharpness ones is carried (W17) |
| Naming the derived launcher | open item 11 | No |
| Folding "report arm T's row-choice split" into the reporting table | open item 9 | No |
| Calling the three new terms the sixth, seventh and eighth | not marked; open item 3 covers their words but not the ordinals | No; a note. The ordinals are a convenience the code does not use (it prints version 4's names, as section 17's candidate 7 says) |

### 2.6 The plain-language rule (handoff section 5, item 6)

- **Em-dashes: 0** (section 2.4).
- **Bare identifiers. MEASURED.** Version 5 has 289 RT mentions on 230
  lines, 98 pull-request mentions and 318 seven-character commit
  identifiers. `grep -c -E '\((RT-[0-9]+)(, RT-[0-9]+)*\)'`, a parenthesis
  holding nothing but RT numbers, returns **22** lines (version 4: 10). Read
  by eye, 18 of the 22 have the phrase just before the parenthesis (for
  example "the per-arm-ceiling repair (RT-172)"); **four are bare, all
  carried from version 4 unchanged, all in the reporting table of section
  7.5:** item 2 "(RT-212, RT-230, RT-232)", item 5 "(RT-234)", item 7
  "(RT-214)", item 9 "(RT-216)". **Should-fix (finding 6):** give each a
  phrase ("the empty-read finding RT-212", and so on). The drafting
  session's scan flagged none because its test was three descriptive words
  within ninety characters, which these pass on neighbouring text.
- **Jargon. MEASURED by search, ARGUED by reading.** Terms used without a
  plain meaning first: the training recipe of section 5.5 and the section 9
  row ("the AdamW optimiser at a peak learning rate of 0.002 with weight
  decay 0.01; a one-cycle schedule with the first tenth of the steps as
  warm-up; gradients clipped at 1.0"), where none of the five terms is
  glossed; "95th percentile" (11 uses, first at line 206, never glossed as
  "the value nineteen of twenty draws fall under"); "bootstrap" (2 uses,
  section 7.5 item 17 and the section 9 row, never glossed). Terms that do
  get their plain meaning first and are fine: the sharpness, the in-use
  check, a buffer ("a fixed stored value ... never seen by the optimiser"),
  the Wilson interval ("the band that sampling alone puts around each
  count"), the route use. **Should-fix (finding 7):** gloss the recipe's
  terms once in 5.5 and the percentile once at its first use. Borrowed
  vocabulary: "tripwire" is used alongside "the spending alarm" throughout
  (both names appear; the plain one is given first in section 1), and
  "halt not trim" is John's ruled phrase; neither needs changing.

### 2.7 What the 2026-10-07 rulings say, and whether version 5 says it

- **Decision 3 as revised.** The first release runs as decision 3 says (the
  $1.14 repair as an amendment, the repaired models verified, the stop, the
  single free-arm run, a floor or gate miss there stops C); the second
  release kept and conditional, asked for only after the repaired route
  holds and the free model clears its gate and floor, a pass necessary and
  not sufficient, John's go on the figures, about $150 to $172. Version 5
  says all of this in sections 0, 1, 5.6, 11 (steps 4b, 5a and 5b) and
  12.4, and withdraws the morning's striking of the second release by name.
  Agrees.
- **The stop condition.** The addition in John's words "Yes, add the stop
  condition to decision 3" is quoted in section 5.6 and stop S4b, with the
  ruling's own wording ("the stirred-in model and the half-and-half
  model", "do not do the task"). Agrees.
- **The kill dates unchanged.** 2026-10-18 for the registration and
  2026-11-01 for step 5b, S6 unchanged, the three withdrawn dates named as
  withdrawn in section 14. Agrees.
- **The outcomes renamed.** Section 3's table renames every term and keeps
  version 4's names beside them; section 0 and section 2 say experiment C is
  written up as instrument research. **But two sentences of registered text
  still state the fifth term by its old words as the outcome, must-fix
  (finding 8).** MEASURED: `grep -n 'metric validated' docs/successor-experiment-proposal-2026-10-07-v5.md`
  finds, besides the table and the places that quote the ruling, line 483
  (section 3: "If arms T and C separate and arm F returns no verdict, the
  outcome is the fifth term, 'metric validated, degree not read', with its
  reason after a colon") and line 3520 (section 11, step 8: "if it returns
  no verdict, the outcome is the fifth term, 'metric validated, degree not
  read', with its reason"). Section 3's own rule says "nothing in this
  document may report an outcome in other words". Line 4336, in section
  15's record of the 2026-10-03 ruling (decision 14), quotes the term as it
  was ruled then and may stand as history, with "now the fifth term under
  its renamed words" beside it.

### 2.8 What the 2026-10-06 ruling's twelve pages say, and whether version 5 says it

Page 1 (the ownership-free line, 1,546 of 3,000): section 8.2, 7.4, 9, 5.4.
Page 2 (the requirement above zero; the solver sentence's figures): 6.4 item
1, 9, 7.3's last paragraph, word for word. Page 3 (the episode format in
full): 4.1. Page 4 (1,800 fitting episodes; option (c) not taken): 7.2 item
1, 7.4, 9, W15, and the re-run's figures throughout. Pages 5 and 9 (the
outcome table, the one re-run, arm F's gate failure at step 5b as the fifth
term, arm M's miss reported, the toy sentence corrected): section 3, 5.2,
8.1, 9. Page 6 (the four wording fixes): 7.2 item 1, 6.4 item 1, 11 step
5a, W16. Page 7 (the joint seed rule): 3, 8.1, 8.2, 9. Page 8 (the
no-transplant rate reported; control 4 the pairing check; the 0.56
sentence): 6.4 items 3 and 5, 7.4, 7.5 item 6, 9. Page 10 (the decoy test,
both ways round; the two A6 sentences): 3, W12, R-12, W18. Page 11 (the
scope phrases; the table of summaries): 3 and 13, **with the eighth term
dropped from the rule (finding 3)**. Page 12 (the kill case): answered by
decision 3 of 2026-10-07 and recorded in section 15, entry 30. The
follow-ups: A7, A8, A11, A12 (RT-251 to RT-254); the two scope phrases and
R2's; control 4 as the withholding pairing check; the stricter generator
self-test (RT-255); A2 as R-13 with the withheld field removed (RT-256); the
training exclusion. All present. The page 11 wording "the ruled terms stay"
is superseded by the later ruling's renaming, and version 5 says so (the
later ruling governs; section 15, entry 32).

### 2.9 Other notes

- **Note (finding 9).** Section 17's candidate 7 says the decision code
  "prints version 4's names"; with the terms now renamed by ruling, the code
  change is owed with the other two (open item 7's 1,980 change; and, after
  today's ruling, no change to the bar). Worth a line in section 11, step 3.
- **Note (finding 10).** The header table's row for the sharpness work
  says it is "owed its check"; that is still true today. The verification
  of step 4b cannot launch before it, as step 4b says.
- **Note (finding 11).** The handoff's section 4, gap 9, says `STATUS.md`
  said $73.77; the drafting branch's last commit (`641a29e`) corrected that
  to $72.32 on the branch, and the main line's 2026-10-08 entry already
  carries $72.32. Nothing owed.

---

## 3. Edits version 5 owes to the two rulings of 2026-10-08

Version 5 was drafted on 2026-10-07 and cites neither. The author of
version 5 applies these; this check makes none of them.

**A. The verification-bar ruling** (`docs/rulings/2026-10-08-verification-bar-ruling.md`,
main line, pull request 126; John's words "Rule the verification bar now,
keep it at 0.5"; authorship mixed). **Must-fix (finding 12)** as a set,
because the text otherwise says a ruled bar is unruled:

1. Section 5.6: replace "The bars 0.9 and 0.5 are the method note's, stated
   before any figure was seen, and are not ruled" with a pointer to the
   ruling file, as the ruling itself asks; delete the bracket "[OPEN ITEM 1
   for John ...]"; rewrite "Whichever bar is ruled, the registration fixes
   it here" as "The bar is ruled at 0.5 and fixed here". The toy figures and
   the four options stay, the options now marked as declined by the ruling
   ((b), (c) and (d) declined; (d) named as the route to a real reference
   if the stop fires).
2. Section 21, item 1: mark **closed** by the ruling, with the date and the
   authorship, keeping its number so that the body's cross-references still
   land.
3. Section 9, the in-use row: "as coded, pending John's ruling on the bar
   (open item 1)" and "not ruled" become "ruled 2026-10-08".
4. Section 7.4, the frozen list: "(section 21, open item 1, until John sets
   the bar)" becomes the ruling's citation.
5. Section 11, step 3: "the bar of the in-use check once John sets it (open
   items 1 and 7)" becomes: the bar is ruled and the frozen code already
   carries it; the 1,980 change (open item 7) and the renamed outcome words
   (finding 9) are what remain owed in code.
6. Section 13, W17: "the bar is open item 1" becomes "the bar is ruled at
   0.5".
7. Section 17, failure 3 part three and candidate 7: "(open item 1)" and
   "it is open item 1" become a statement that the bar is ruled and that
   the candidate's firing stands as the record's own prediction that the
   stop of S4b will most likely fire, which the ruling says in its own
   words.
8. Section 15: a new entry recording the ruling, John's words, authorship
   mixed, and the three options declined.
9. The source table: a row for the ruling, on the main line.
10. The header's "Three things a reader of version 4 should know first": add
    that the bar is ruled.

**B. The December-result restatement rulings** (`docs/rulings/2026-10-08-december-result-restatement-rulings.md`,
main line, pull request 128; John's words "Merge it and approve all the
decisions from the doc"; authorship mixed; the restatement itself now a
dated note at the head of `docs/december-result-roadmap-2026-09-20.md`):

1. **Must-fix (finding 13).** Stop S4b and section 5.6 say an early stop is
   "Not an outcome term: it is reported as 'the repaired construction did
   not hold at 10 million parameters'". Decision 2 confirms the public
   sentence for that ending, "the built arms as designed are not
   references; the measure was not reached", and decision 1 adopts the
   restatement that calls that ending "a registered ending reached by its
   own stop rule" and "not a failure of the year". Version 5 should carry
   the ruled sentence as the registered wording of the S4b ending, say that
   it is a registered ending of experiment C under the restatement's first
   row while the eight outcome terms are unchanged, and cite the ruling.
   The verification-bar ruling uses the same sentence for the same case.
2. Should-fix: section 3's opening ("Reproduced from section 2 of the
   December-result roadmap") and section 14 should cite the roadmap's dated
   head note of 2026-10-08, which says what the result means now that the
   measurement target has moved and changes none of the terms, kill dates
   or caps; and R4's row can say that the restatement's own terms for a
   schedule failure are the same two kill dates.
3. Note: the restatement's cost table ($1.14 for the first ending, about
   $13 for the second, about $150 to $172 more for the third) agrees with
   version 5's sections 12.3 and 12.4; nothing owed there. Decision 3 (the
   state-of-the-programme write-up folds into the closing STATUS entry, the
   essay as its public face) touches section 11's step 8 only as a
   cross-reference, if at all.
4. Section 15 and the source table: an entry and a row for this ruling too.

---

## 4. Verdict

**ARGUED.** Version 5 may be committed as the registration once the fifteen
branches it cites are merged (the sharpness branch after its own check,
which is still owed) and the five must-fix items are applied: finding 1
(version 4's closing section left in the file), finding 3 (the scope rule
drops the eighth term), finding 8 (the fifth term's old words in two
registered sentences), finding 12 (the verification-bar ruling written in)
and finding 13 (the ruled sentence for an early stop written in). The
should-fix items (findings 4, 5, 6, 7 and B.2) are recommended before the
commit because each is a few lines. Nothing found changes a figure, a bar, a
term's meaning or a stop; the drafting is faithful to the rulings in
substance, and every figure checked matches its file.

The must-fix items, in one line each:

1. Cut the stray heading off the end of line 5541 and delete version 4's
   closing section (lines 5542 to 5550).
2. Add "instrument not validated" to the scope rule of section 3.
3. Replace "metric validated, degree not read" with the fifth term's renamed
   words at lines 483 and 3520.
4. Write the verification-bar ruling in (section 3, part A above).
5. Write the ruled early-stop sentence in at S4b and section 5.6 (section 3,
   part B.1 above).

Open items 2 to 12 of section 21 stand as John's; open item 1 is closed by
today's ruling; open item 6 is left open by that ruling in its own words.

---

## 5. What this check did not do

It did not re-run any model, any read or any transplant; the page 4 rows and
the other outputs were read as committed. It did not check the thirty
wording fixes of the check of version 4 one by one against that check's
section 4, nor the 2026-10-03 rulings against version 5 (the handoff says
these were carried as version 4 already carried them, and the diff shows
only the places the log names). It did not read the ChatGPT and Gemini
reviews in full, the inside review beyond search, the code freeze beyond
search, the tripwire code, or section 18 of version 5. It did not check the
2026-10-06 ruling record against the word-for-word note, which is owed to a
separate check. It did not run the drafting session's `failure_pass_v5.py`
or `scan_ids.py`, which are not committed; it recomputed what section 17
prints from the committed inputs with its own commands. It did not verify
the handoff's count of 39 ruled changes or 78 edits. It did not check the
sharpness branch, which remains owed its check before the reruns. It did
not edit, merge, rule, rent, spend or train anything.

## 6. Files

- This report: `docs/reviews/2026-10-08-successor-v5-check-claude-code.md`.
- This session's scripts (`map_hunks.py`, `recompute_rows.py`, `arith.py`,
  `missing_paths.py`, `probe_summary.py`) and their outputs are in its
  scratch folder and are not committed; every command they stand for is
  named above, and each is a few lines a reader can rewrite from its
  description.
