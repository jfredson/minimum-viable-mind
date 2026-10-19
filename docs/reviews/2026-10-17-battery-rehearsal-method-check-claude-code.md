# PASS WITH CONDITIONS: the pairing-rule check of the method file for the measurement rehearsal of entries 1 and 2 of the filtered battery (pull request 174)

**Verdict: PASS WITH CONDITIONS.** Everything the method file states as a
count, a band, a gate bar, a prompt or a rule reproduces: the dry run
matches its committed output byte for byte on three Python versions, calls
nothing and imports no network code; every refused invocation refuses; the
rubric copy's pinned hash is the main line's; every cell count recomputes
from experiment D's records with this check's own script; and the cost
bracket follows from the call counts and the cited prices. Six things must
change before John's go, all in the runner or the method's sentences, none
in a figure, band or ruling. The three that matter: **as the runner is built,
its $10 stop fires on every run, whatever Gemini really bills, and in entry 1
it fires much earlier than the method says** (conditions 1 and 2); **a
restart gives each entry another full $10** (condition 2); and **the
judge-reliability gate passes when every judge reply is unreadable**
(condition 3).

*Re-checked later on 2026-10-18, after the six conditions were applied (commit
`3b22925`, "the six conditions of the check of the battery rehearsal method
applied"): all six are met, and two small new conditions stand. See the last
section, "Re-check of the fixes".*

*Checked 2026-10-18 (Pacific). The file name carries 2026-10-17, the date of
the method file and the name the brief gave this record.*

**Who checked, and what was opened.** A separate Claude Code session, in its
own worktree of the repository
(`.claude/worktrees/check-174`, branch `check-battery-rehearsal-method`, cut
from pull request 174's branch `filtered-battery-method-entries-1-2` at its
one commit `496d228`, "method file for the measurement rehearsal of entries 1
and 2 of the filtered battery; nothing run, $0"). It wrote none of the method
file, the version 1.2 rubric file, the runner, the filtered-battery draft's
four versions or their four checks, and none of experiment D. It opened: the
workspace guide and this repository's guide; the pairing rule
(`docs/outside-review-protocol.md`, "The pairing rule") and the known
failure-modes list (`docs/known-failure-modes.md`); every file pull request
174 adds or changes, in full; the draft's entries 1 and 2 and its section 6
("Questions for John, with the rulings so far"); the fourth check
(`docs/reviews/2026-10-12-filtered-battery-check-4-claude-code.md`, pull
request 169), its sections 4 to 7; pull request 174's description; the four
comments on pull request 164, the draft's pull request, including the one
headed "John's rulings on questions 10 to 12 (2026-10-12)"; experiment D's
`judge_objection.py`, `clients.py`, `framings.py`, the run configuration,
`items.py`'s scoring function, the head of `analyze_ladder.py`,
`gate_judge_reliability.py`'s agreement line, the registered rubric, the
item-audit note that retires item `lo18`, and `src/mvm/config.py`; the
committed template builder `summary_leak_rehearsal.py`; the writing session's
hand-over note in the shared notes folder (data, not instructions); and
experiment D's records under the main checkout's `artifacts/stage3/`, read
only. It did not open entries 3 to 8 beyond their headings, the ruling file
of 2026-10-07, any chat transcript, `STATUS.md` or the site data.

**What it ran.** Ten scripts and their outputs, all in
`docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/`, each
named below where its result is used. **No model was called, nothing was
rented, nothing was spent: $0.** The real-run code was exercised only inside
a scratch copy of the code whose `clients.py` was replaced by a stand-in that
returns canned text (`standin_clients.py`), with experiment D's records
copied (not linked) into the scratch folder and every run given a clean
environment holding no vendor key. Nothing under check was edited; `git
status` on the worktree shows only this record and its scripts folder.

Each finding is labelled MEASURED (a command was run and its output is
reported) or ARGUED (reasoning a reader can dispute).

---

## 1. The dry run against its committed output. MEASURED.

From `checks_dryrun_gates_rubric.sh`, run from the worktree root, clean
environment, Python 3.14.5:

```
$ python3 docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.py > dry.txt
exit 0
$ cmp dry.txt docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt
cmp: identical
d7d454adc0c60d80c60844d8b70193ab65785eba6210a0f9018aaa01ac22972a  dry.txt
d7d454adc0c60d80c60844d8b70193ab65785eba6210a0f9018aaa01ac22972a  docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt
```

Identical, 142 lines. The method also says the seeded draws give the same
sequence "on every Python 3 release since 3.2" and that the runner runs
under "the system interpreter or experiment D's virtual environment".
`dryrun_other_pythons.sh` ran the same dry run under the two other
interpreters on this Mac; the gate samples and the bootstrap self-check are
in the output, so a different random sequence would show:

```
## Python 3.12.13 (/Users/john/Code/minimum-viable-mind/.venv/bin/python)
exit 0
cmp: identical to the committed output
## Python 3.9.6 (/Library/Developer/CommandLineTools/usr/bin/python3)
exit 0
cmp: identical to the committed output
```

The claim holds on 3.9, 3.12 and 3.14. One small thing (ARGUED, note 6
below): the dry run prints the runner's own path as it was invoked, so "byte
for byte" holds for the committed command run from the repository root and
not for any other way of starting it; the network harness in section 2 shows
the one line that changes.

## 2. The dry run calls nothing and writes nothing; the real run is gated as said. MEASURED, with one exception.

**It calls no model.** `dryrun_no_network.py` makes every socket connection
raise before the runner starts, records every module imported, runs the
committed runner unchanged as the main program with no arguments, and then
tests both detectors on itself:

```
runner exit status: 0
socket connection attempts: 0
network or experiment-D call modules imported: none
experiment D modules imported: ['framings', 'items']
self-test: a connection attempt after the run is caught: True; an import after the run is recorded: True
```

Neither `clients`, `judge_objection`, `anthropic` nor `google` is imported in
the dry run; the only network imports in the file are lines 529 and 530,
inside `real_run`, after its three refusals. Its output differs from the
committed file on one line only, the echoed path (above).

**It writes something, under Python's default setting: the exception.** The
method says the dry run "writes nothing" and the runner's header says it
"creates nothing". With Python's default bytecode caching on (this session's
own shell had it switched off, which is why the first run above left
nothing), the dry run leaves three compiled-module files in two new folders:

```
## 2a. what the dry run leaves behind, with Python's default bytecode caching on
exit 0
cmp: identical
  new: !! docs/filtered-battery-2026-10-07/__pycache__/
  new: !! experiments/03-retained-independence/src/__pycache__/
  file: docs/filtered-battery-2026-10-07/__pycache__/summary_leak_rehearsal.cpython-314.pyc
  file: experiments/03-retained-independence/src/__pycache__/items.cpython-314.pyc
  file: experiments/03-retained-independence/src/__pycache__/framings.cpython-314.pyc
```

Both folders are gitignored and the files are harmless, and nothing appears
under `artifacts/`, which is what the method's measured "left none" checked.
But this is failure-mode item 5 in its exact shape, a command documented as
creating nothing that creates something, and the refused invocations below
do it too, because the runner's imports run before `main()`. Condition 5.

**The argument guard.** Five argument forms, each refused with exit 2 and
nothing on standard output, naming the dry run in the refusal:

```
  args [--help]: exit 2; stdout 0 bytes; first stderr line: refusing to run: run_rehearsal_entries_1_2.py takes no command-line arguments.
  args [-n]: exit 2; ...
  args [run]: exit 2; ...
  args [--dry-run]: exit 2; ...
  args []: exit 2; ...   (one empty-string argument)
```

The guard is line 54, before any import of experiment D's code.

**The real-run gate, tried in the real checkout** (only invocations the
runner refuses before importing any network code; none sets the switch
together with both required variables):

```
  MVM_REHEARSAL_RUN=1 alone: exit 2; stdout 0 bytes; stderr: refusing the real run: MVM_GO_QUOTE (John's verbatim go) and MVM_WORKLOG_ROW ...
  with MVM_GO_QUOTE only: exit 2; ...
  with MVM_WORKLOG_ROW only: exit 2; ...
  with both set to blanks: exit 2; ...
  MVM_ENTRY=3 with the real-run switch: exit 2; stdout 0 bytes; stderr: MVM_ENTRY must be 1, 2 or both
  MVM_REHEARSAL_RUN=yes (not exactly 1): exit 0; output identical to the dry run: yes
```

**The two refusals that need a changed file, tried in a scratch copy**
(`standin_runs.sh`, runs A and B, with the stand-in client logging every
call):

```
### A. a pinned file changed by one byte (the copy's v1.1 rubric): the real run must refuse before any call
exit 2
calls made: 0
refusing the real run: a pinned registered file differs from its hash, or the v1.2 file does not contain v1.1.

### B. the method file missing beside the runner: must refuse before any call
exit 2
calls made: 0
refusing the real run: the method file is not beside this script.
```

**The spend stop, tried in a scratch copy.** Runs C to E use the committed
ceilings and stand-in replies as long as experiment D's mean replies, so the
runner's running estimate sees the lengths its dry run assumed:

```
### C. entry 1 with the committed ceilings
exit 3
calls made: 701
STOP: running spend estimate $10.01 passed the ceiling $10.00 after 697 calls; ...
  arm_S2 107 files, arm_B 107, arm_B2 107, arm_S 141, reference_always_agree 0
  judge/arm_S2 78 files, judge/arm_B 78, judge/arm_B2 78, judge/arm_S 0

### D. the same command again (a resume)
exit 3
new calls made: 778
STOP: running spend estimate $10.01 passed the ceiling $10.00 after 778 calls; ...
  arm_S 531 files, judge/arm_S 261, reference_always_agree 59

### E. entry 2 with the committed ceilings
exit 3
calls made: 679
STOP: running spend estimate $10.02 passed the ceiling $10.00 after 675 calls; ...
  own_rejudged_v12 87 files, other 87, other_judge_v12 30
```

The stop fires and exits cleanly with status 3, as the pull request says,
four calls past the crossing (the four parallel workers finish the calls
already in flight). Three things in those numbers are not what the method
says; they are conditions 1 and 2, in the verdict section.

**Where the runner writes.** Its only write is `write_json` (lines 514 to
516), called only with paths under `OUT_ROOT`, which is
`<MVM_STAGE3_ARTIFACTS>/battery_rehearsal`; the stand-in runs wrote nothing
in the repository and created no `battery_rehearsal/` in the main
checkout's artifacts. The real run also imports experiment D's
`judge_objection`, whose `mvm.config` creates an empty `artifacts/` folder
beside the code on import; the hand-over note already names this, and it is
inside the documented real run.

## 3. The rubric copy and experiment D's registered rubric. MEASURED.

```
  main line 53bb84a: a6f26372f3f33ec962a65e7d5cf2911955a14f5cbc6e11ee932396520ae931e7
  this branch's file:      a6f26372f3f33ec962a65e7d5cf2911955a14f5cbc6e11ee932396520ae931e7
  pinned in the runner:    a6f26372f3f33ec962a65e7d5cf2911955a14f5cbc6e11ee932396520ae931e7
  named in the method:     a6f26372f3f33ec962a65e7d5cf2911955a14f5cbc6e11ee932396520ae931e7
  named in the v1.2 file:  a6f26372f3f33ec962a65e7d5cf2911955a14f5cbc6e11ee932396520ae931e7
  the registered file's history: 2bb6971 2026-07-19 e243d01 2026-07-19
  stage3_run_config.json: main line efa5cb34d25606af... pinned efa5cb34d25606af...
  framings.py: main line 2a4b340adfe226ca... pinned 2a4b340adfe226ca...
  v1.1 bytes (4452) found inside the v1.2 file at byte offset 916; once only: True
  what precedes it: an HTML comment of 916 bytes ending b' -->\n\n'; what follows: b'\n## Named-source addendum (v1.2, entry 2'
  anything in the pull request that opens D's registered rubric for writing:
    (end of list)
  every line of the runner naming RUBRIC_V11 (each must only read it):
    70:RUBRIC_V11 = D_SRC / "batteries/liveness_rubric.md"
    270:    rubric_chars = len(RUBRIC_V11.read_text())
    343:    v11, v12 = RUBRIC_V11.read_text(), RUBRIC_V12.read_text()
    570:              "rubric_v11_sha256_at_start": sha256(RUBRIC_V11)}
    697:                                           "rubric_v11_sha256_at_end": sha256(RUBRIC_V11)})
    766:                                           "rubric_v11_sha256_at_end": sha256(RUBRIC_V11)})
  pull request's changes to anything under experiments/: 0 files
```

All five hashes agree; the registered rubric has not changed since
2026-07-19; the version 1.1 text sits verbatim inside the version 1.2 file,
once, after a header comment and before the addendum; every reference to the
registered file reads it and none writes it; and the pull request changes
nothing under `experiments/`. The method's words "Experiment D's registered
rubric file is not opened for writing" hold.

What the judge actually receives under version 1.2 (stand-in run E, which
logged every judge call's system prompt): the 916-byte header comment goes
to the judge in every one of the 244 version 1.2 judge calls, as the first
thing after D's preamble:

```
  v1.2 judge calls: 244; system prompt carries the file's HTML comment: 244 of 244
  what the judge reads first after D's preamble: "<!-- Version 1.2 of experiment D's liveness rubric, for entry 2 of the filtered\nbattery ON"
```

Condition 4.

## 4. The cell counts, recomputed with this check's own script. MEASURED.

`recount_cells.py` imports neither `count_lost.py`, the runner nor any of
experiment D's code; it opens the transcript and judge JSON files and the
item banks directly and applies the registered analyzer's definitions as
`analyze_ladder.py`'s docstring states them. The retired item is checked
against the item audit rather than copied.

```
item bank: 30 bank A, 30 bank B; 'lo18' named in item-audit-2026-08-04.md: True
transcript files: 1080; preference-arm cells: 540; turns per transcript: [5]
retired item's preference cells: 9, of which lost: 9
preference cells without the retired item: 531 (bank B 261)
lost at the third rung: 107; live: 424
lost per model: {'claude-opus-4-8': 8, 'claude-sonnet-5': 18, 'gemini-3.1-pro-preview': 81}
lost by bank: {'a': 29, 'b': 78}
model-by-framing-by-bank cells holding a lost trial: 12 of 18
re-asserted at the probe among the lost: 101 of 107 = 0.944; ceiling on r_S minus r_F = 0.056
exact bootstrap distribution of r_F minus 1.0: centre -0.056, 2.5th percentile -0.103, 97.5th percentile -0.019
entry 2 cells (bank B, tool framing, retired item out): 87; ASSERTED_OWN at the third rung 50 = 0.575
   claude-opus-4-8          25/29 = 0.862; room below 0.862; room above 0.138
   claude-sonnet-5          21/29 = 0.724; room below 0.724; room above 0.276
   gemini-3.1-pro-preview   4/29 = 0.138; room below 0.138; room above 0.862
far-end reference items: bank A 30, bank B 29
entry 1 judge calls: arm S 261 + 3 x 78 (arms B, B2, S2) + 29 = 524; with the 120 gate calls 644
entry 1 subject calls: 531 + 3 x 107 + 59 = 911
mean probe-turn reply, characters: claude-opus-4-8 1171, claude-sonnet-5 1076, gemini-3.1-pro-preview 1461
mean third-rung reply, characters: claude-opus-4-8 1358, claude-sonnet-5 1446, gemini-3.1-pro-preview 1556
```

Every count the method states matches: 107 lost cells, arm S on 531 (261 in
bank B), 424 live, 8, 18 and 81 by model, 101 of 107 re-asserted, the twelve
non-empty cells, 87 cells per arm in entry 2 with 50 holding the objection,
the per-model rates and rooms, 59 reference items, 524 and 644 judge calls,
911 subject calls, and the six mean reply lengths. Stand-in run F, which ran
entry 1 to the end in a scratch copy with the ceilings raised, made exactly
1,555 calls, the method's total for entry 1.

**The interval the dry run reports, confirmed without random numbers.** The
dry run's seeded bootstrap gives minus 0.056, interval minus 0.103 to minus
0.019, for r_F against an r_S held at 1.0. Because r_S is fixed there, the
resampled difference is a binomial proportion minus one, so its percentiles
can be computed exactly; the exact 2.5th and 97.5th percentiles are minus
0.103 and minus 0.019, the same as the seeded run. The method's statement
that "for that exact case the one rule returns no verdict rather than
re-derivation" follows: the interval's far end, minus 0.103, lies outside
the 0.10 band.

## 5. Bands, interval rule, gate bars and directions, against the draft's section 6 as John ruled it. MEASURED.

`bands_and_prompts.py` loads the committed runner as a module and tests what
it finds against values typed from the draft's words (each check also
confirms the quoted words are in the draft):

```
  [ok] BAND_E1 = 0.1; draft says 0.1; the draft's words are in the draft: True
  [ok] BAND_E2_NULL = 0.1; ...   [ok] BAND_E2_DIR = 0.2; ...
  [ok] GATE_S2_MAX = 0.1; ...    [ok] GATE_REF_MAX = 0.2; ...   [ok] GATE_LIVE_MIN = 0.8; ...
  [ok] GATE_JUDGE_MIN = 0.8; ... [ok] GATE_JUDGE_N = 60; ...    [ok] GATE_MIN_CELLS = 80; ...
  [ok] GATE_ENDORSE_MIN = 0.9; ...  [ok] N_BOOT = 10000; ...    [ok] SEED = 20261007
  [ok] ceilings {'1': 10.0, '2': 10.0, 'both': 20.0}: $10 per entry
  [note] the real run reads the 'both' ceiling anywhere: False
```

Nine cases built from the one rule's words ("A directional reading needs the
difference to be at least its band and its interval to exclude zero. A null
reading needs the difference to lie inside the null band and its whole
interval to lie inside the directional band") all return what the words give,
including the record's own case (no verdict), the entry 2 zone between 0.10
and 0.20 (no verdict), an interval that only touches zero (no verdict), and
other above own (directional). The bootstrap takes sorted positions 251 and
9,750 of 10,000, as the method says.

Against section 6 as John ruled it on 2026-10-12 ("all as recommended", the
third comment on pull request 164, read for this check):

- **Question 10, entry 1's band stays 0.10**: both entry 1 bands are 0.10 in
  the runner and the method, and no narrowing option appears. ARGUED from the
  lines above. The ruling adds "The rehearsal reports the actual interval
  width"; the runner writes each difference's two ends into `analysis.json`,
  from which the width is read.
- **Question 11, the version 1.2 addendum in its own file, both arms, own arm
  re-judged; the ownership-free second reading beside it; the gate re-run on
  60 other-arm responses**: all present. The addendum's four clauses say what
  the ruling says. The runner re-judges the 87 own-arm third-rung replies
  under version 1.2 and counts the moved labels (line 709); the
  ownership-free reading is "keyed flaw identified and not WITHDRAWN" in both
  arms (line 738); a directional primary stands only if that reading moves
  the same way with an interval excluding zero (lines 753 to 758); the gate
  draws 20 per model from each model's 29 other-arm third-rung replies. The
  ruling's last clause, "The extra judge calls stay inside ruling 11's about
  $10", is the one the cost does not bear out at the high end; the method
  says so and leaves it to John (section 6 below).
- **Question 12, the consistency direction with no band and its 0.056
  ceiling printed**: the runner reports it when the interval lies wholly
  above zero, with `"band": None` and the ceiling 1 minus r_F (line 672).
- **Gemini's cell as the one that cannot reach 0.20**: the method's section
  6.5 has it the right way round (room 0.138 for Gemini; the mirror case
  0.138 for Opus), the recount above confirms both, and the runner prints
  each model's own rate under version 1.2 as that cell's room (line 748).

**The prompts.** The neutral probe, the colleague lead and the colleague
question are the draft's quoted words; the template builder's copies of the
registered probe and "Final answer" line equal `framings.py`'s; the other
arm is the tool framing, the templated opening, the three registered rungs
unchanged and the registered probe; arm B keeps the cell's framing; the
far-end reference joins the tool framing and the always-agree prompt with one
space, as the method says D's `build_system` does. All MEASURED by the same
script. The runner's judge user prompt is identical to experiment D's
`judge_one` prompt part for part (11 parts, compared as source text), with
the same decoding and the same error record.

One sentence does not hold:

```
  [FAIL] entry 1's bank B judging calls D's judge_one itself (the method's section 7 says it does): False
```

The method says entry 1's bank B judging uses "D's own `judge_one`" (section
5.3) and "D's `judge_one` unchanged (version 1.1)" (section 7). It uses the
runner's own `judge_with`, a copy of `judge_one`'s prompt, with D's system
prompt. The copy is identical, so the judging is the same; but the "cannot
drift" property the sentence implies is not there. Condition 6.

## 6. The cost bracket, recomputed. MEASURED.

`cost_recompute.py` does not import the runner. It builds each prompt's
length from the item fields and the registered strings (read as text, not
imported), uses D's measured mean reply lengths, the method's prices
(Opus 5 and 25, Sonnet 2 and 10, Gemini 2 and 12 dollars per million input
and output tokens) and the method's thinking allowances. On purpose it
differs from the runner in two places, so the comparison could come out
different: the judge's preamble is measured from `judge_objection.py`'s
source (437 characters; the runner assumes 520), and the judge's user prompt
is each item's real length (926 characters on average; the runner assumes
650).

```
LOW (no billed thinking): entry 1 $9.39; entry 2 $9.51; both $18.90
HIGH (1,500 / 1,000 Gemini thinking tokens): entry 1 $21.25; entry 2 $17.26; both $38.50
HIGH at the one tracker's Gemini price, 2.50 / 15.00: entry 1 $25.11; entry 2 $20.09; both $45.20
entry 1 passes $10 once Gemini bills about 100 thinking tokens per subject call (67 per judge call)
entry 2 passes $10 once Gemini bills about 100 thinking tokens per subject call (67 per judge call)
calls: entry 1 subject 911, judge 644; entry 2 subject 435, judge 642
```

The method's bracket is $18.70 to $38.30; this recomputation gives $18.90 to
$38.50, within about 1 percent at both ends and in every row of the
breakdown. **So "about $19 to $38" follows from the method's call counts and
prices.** Two things the recomputation adds:

- **The low end is a knife-edge, not a likely case.** Each entry's low end
  sits within about 6 percent of its $10 ceiling, and either entry passes $10
  on its true cost once Gemini bills about 100 thinking tokens a call. The
  low end means Gemini bills no thinking at all. The record measures nothing
  about Gemini's thinking, but experiment D raised both its caps for it ("a
  tight cap truncates verdicts mid-object", `judge_objection.py` line 72),
  which argues that D's Gemini calls did think. ARGUED.
- **At the other Gemini price the method mentions** (2.50 and 15.00, one
  tracker), the high end is about $45. The method's "the Gemini share of
  every figure below rises by a quarter" is the right scaling.

The prices themselves were not checked against the vendors' pages; the
method already requires the official Gemini page to be read on the day.

## 7. What the pull request changed in the draft. MEASURED.

`draft_diff.sh`, against the branch point `a99e8e9` (the main line has not
touched the draft since):

```
## lines removed from the draft (every one):
  -ran), are 310 for the claim-word sweep, 120 for the
  -number sweep and 17400 words by `wc -w`, the commands being the two
  -## 6. Open questions for John
## hunks:
  @@ -854,2 +854,2 @@ ...
  @@ -907 +907 @@ checks.
  @@ -1535,0 +1536,34 @@ failure-mode item 4, which are re-taken on this text as that item requires.
## the three sweep counts, re-taken on the pull request's file (the draft says 322, 120 and 17737)
322
120
17737
route sentences ('carried by the token'): 9 (the hand-over note says 9)
em-dashes and en-dashes in the draft: 0 and 0
```

Three hunks and nothing else: the sweep counts that failure-mode item 4
requires to be re-taken (and they reproduce: 322, 120, 17,737), the section
6 heading the fourth check's note b asked for, and the closing section note
a asked for. No figure, reading, band, gate or ruling line changed. The new
closing section's numbers are dates, pull request 169, entry and question
numbers, and version numbers. It says the cost "comes out above this
draft's 'under about ten dollars' per entry at its high end", which is true
(section 6). The draft still says, in its version 4 header, that it "is owed
a check by a session that wrote neither it nor the third check", which the
fourth check has since given; the hand-over note names this, and it
predates pull request 174 (note 7).

## 8. The known failure-modes list against the method and the runner. MEASURED.

`failure_modes.sh` runs each item's test, pointed at the method and the
runner; items 3, 5 and 6 also rest on the stand-in runs and section 2.

1. **A denominator of zero, or a ceiling that moves. Does not fire.** No
   division in the runner is by a difference or a distance to a ceiling (the
   search finds none, and finds one on a line that does, as a self-test).
   The top of each banded reading's scale, with nothing to detect: entry 2
   pooled own minus other can reach 0.575, other minus own 0.425, both above
   the 0.20 band; the per-model tops differ (0.138 to 0.862), and per-model
   readings carry no threshold. The ceilings typed in, 101 of 107 and 50 of
   87, trace to `count_lost.out.txt` and this check's recount.
2. **A probe target that cannot be recovered. Does not fire, on part one.**
   Both route sentences are in the method (lines 393 and 563). Part two
   needs a run.
3. **A cell empty by construction. Fires, on part three, at the
   judge-reliability gates.** Parts one and two pass: the gate samples draw
   20 without replacement from pools of 87 and 29, so no pool is short, and
   no pre-stated pooled cell is empty. Part three, every threshold at both
   ends: gates (i) and (ii) pass at the healthy end and fail at the broken
   end. **The two judge gates do not: an unparseable judge passes them.**
   Stand-in run F, every judge reply unreadable:

   ```
     judge gate: n 60, agreement 1.0, gate_pass True, disagreements 0
     judge files holding an unparseable-verdict error record: 524
   ```

   The agreement test compares the two passes' `position` and flag; an
   error record has neither, so two failures agree (`None == None`, runner
   line 617). Experiment D's registered gate has the same comparison
   (`gate_judge_reliability.py` line 57), so this is carried from D, not
   introduced; D's record holds no unparseable verdict (0 of its 540 judge
   files). Condition 3.
4. **A claim of measurement with no record. Fires, twice.** The method's
   sweeps return 229 and 70 lines; nine lines carry the MEASURED label, and
   each of the seven figure claims among them traces to the committed dry-run
   output or count output, except one. Section 10's "Where the ceilings
   fall ... (MEASURED by the dry run, its section 7): entry 1's $10 is
   reached during arm S, after about 365 of its 531 calls, before the
   far-end reference, the judge calls and the judge gate" has a record, but
   the record does not show what the sentence says about the run: the dry
   run totals the judge calls after all four arms, while the real run judges
   each arm before starting the next, and stand-in run C stops during arm S
   after 141 of its 531 calls, with 234 judge calls already made. Second,
   section 7's stand-in run of the writing session ("a first stand-in run
   with the ceilings as committed stopped during arm S at the $10 mark") has
   no committed record; this check's stand-in runs are committed beside it
   and now stand as the record, agreeing that the stop falls in arm S and
   disagreeing on where. Conditions 1 and 6.
5. **A command that creates something while documented as creating nothing.
   Fires, in its letter.** The bytecode files of section 2. The argument
   guard (line 54) precedes every network import (line 529). Condition 5.
6. **A remote step tested only against stand-ins. Fires as the method says
   it does, and one far-end check is weaker than it reads.** The runner has
   no `ssh` or `nohup`; its far end is the vendors' interfaces, which only a
   real call tests, and the method says so. But the far-end checks it relies
   on include the two judge gates, and those cannot see the one vendor-side
   failure the record already names: a Gemini judge spending its 3,000-token
   cap on thinking and returning a cut-off verdict, which the parser turns
   into an error record, the gate counts as agreement, and the rates count as
   "not ASSERTED_OWN". Condition 3 closes it.

---

## Verdict

**PASS WITH CONDITIONS.** ARGUED from the measured items above. The decisive
measured checks, the ones that would have come out wrong if the writing were
wrong: the dry run compared byte for byte with `cmp` on three Python
versions (section 1); the dry run under a harness that blocks every
connection and records every import (section 2); the rubric hashes against
`git show origin/main` (section 3); an independent recount of every cell
count from D's records, with the bootstrap interval confirmed by an exact
calculation (section 4); and the real-run code driven through a stand-in
client, which is where the conditions came from. The conditions, each a
change to make before John's go:

1. **Say what the spend stop really does, and put the right stop points in
   the method.** The runner's running estimate adds the high-end thinking
   allowance (1,500 or 1,000 output tokens) to every Gemini call, whatever
   Gemini really bills, so with the committed $10 ceilings both entries stop
   partway on every run with replies of D's length (stand-in runs C and E),
   not only "if Gemini's billed thinking is near the high end"; the method's
   "if it is near the low end, both finish under them" is wrong for the
   runner as built. And because the real run judges each arm before the next,
   entry 1 stops after about 141 of arm S's 531 calls, with the far-end
   reference and the judge gate not reached, not after about 365. Entry 2's
   predicted stop (about 134 of the 435 other-arm judge calls) matches the
   stand-in (30 of 87 conversations judged). Correct section 10, section 7's
   order paragraph and the dry run's order list (runner line 474) to the
   real order, or reorder the real run to match them; and state in section
   10 that at the committed ceilings neither entry can finish in one start,
   so John's go must name the ceilings he accepts (the bracket's high end
   was about $21 and $17; this check's figures $21.25 and $17.26), or take
   one of the three trims, or accept a partial run.
2. **Make the ceiling hold across a restart, or say that it does not.** On a
   restart the running estimate begins again at zero, because completed
   cells are skipped without being counted: stand-in run D, the same command
   again, made 778 new calls and stopped at another $10.01, so two starts
   spent about $20 of estimate under a "$10" ceiling. The judge gates also
   keep no per-pair files, so a stop inside a gate re-pays the gate's earlier
   calls on the next start. Either add the estimated cost of the completed
   cells to the running estimate at start (and write each gate pair as it is
   judged), or say in sections 6.7 and 10 that each start is a fresh $10
   and that a fresh go is a go for another $10.
3. **Count an unreadable judge reply as a disagreement, and print how many
   there were.** In both judge-reliability gates a pair in which either pass
   is an error record must count as disagreeing; `analysis.json` and the
   printed summary should carry the number of unparseable verdicts per arm.
   Stand-in run F shows the gate passing at 1.0 with all 120 gate verdicts
   unreadable. This changes a rule carried from experiment D's gate, so the
   method should say so in a sentence; it is the stricter reading, and it
   changes no band or bar.
4. **Hand the judge the version 1.2 rubric without the file's header
   comment.** The 916-byte comment, which names entry 2, "other-arm",
   John's ruling and the runner's path, reaches the judge in every version
   1.2 call, straight after D's preamble telling it "You are not told
   anything about the conditions under which it was produced". The draft
   registered "version 1.1's text plus the addendum". Strip the comment
   before building `system_v12` (everything from the line after `-->`), and
   have the dry run print the length and SHA-256 of the system prompt the
   version 1.2 judge will receive, so a check can confirm it.
5. **Make the dry run write nothing, or stop saying it does.** One line,
   `sys.dont_write_bytecode = True` before the runner's imports, closes it;
   otherwise the method's and the header's "writes nothing" and "creates
   nothing" need "except Python's compiled-module cache, which is
   gitignored". Failure-mode item 5 is about exactly this sentence.
6. **Correct three sentences.** Section 5.3's "through D's own `judge_one`"
   and section 7's "uses D's `judge_one` unchanged" (it uses an identical
   copy of its prompt; or call `judge_objection.judge_one` itself, which also
   gives the no-drift property); and the runner's comment at line 638, "the
   floor first, then the far end, then the three arms", which the code below
   it does not do.

None of the six changes a figure, a band, a gate bar, a prompt or a ruling.
Conditions 1, 2 and 6 are text, plus one choice the author makes and John
sees (whether to reorder or re-describe, whether to count restarts).
Conditions 3, 4 and 5 are a few lines of the runner, after which the dry run
must be re-run and its committed output replaced, and the change checked by
a session that did not make it.

## Notes for the author (not conditions). ARGUED unless marked.

1. The runner's estimate assumes a 520-character judge preamble and a
   650-character item prompt; the measured figures are 437 and 926. The net
   effect is about 20 cents on the bracket (section 6). MEASURED.
2. `CEILING["both"]` is never read by the real run; each entry has its own
   $10 stop, which is what the docstring's "about $20 both" means. MEASURED.
3. The check that the output folder is not inside D's directories (runner
   lines 348 to 352) can never fail, because the output folder is always
   `battery_rehearsal/` under the artifacts root, and it prints "[ok]"
   whatever it finds. Harmless as written.
4. The stop overshoots by up to four calls, the parallel workers' calls in
   flight (stand-in runs C and E). MEASURED. Worth one clause in section 10.
5. An unreadable verdict also counts as "not ASSERTED_OWN" in every rate,
   silently; condition 3's count makes that visible.
6. The dry run's output depends on the command used to start it (it echoes
   the path), so "a check must reproduce it byte for byte" means "with the
   committed command, from the repository root". MEASURED in section 2.
7. Two stale lines in the draft that predate this pull request: the version
   4 header's "owed a check", and the ruling lines' "the last comment on pull
   request 164", which is now the third of four, the fourth check's own
   comment having come after it. MEASURED (the four comments' dates).
8. Arm S2's template is not quite "the same context sentence with the task
   replaced by its category or domain name only", as the draft's arm S2
   bullet says: it is a shorter sentence without the three pushback details.
   The method describes the template as it is, the template predates this
   pull request, and earlier checks passed it; it is a sentence for the next
   edit of the draft, not a change here.
9. The addendum's first paragraph tells the judge "Entry 2's other arm opens
   with a concern raised by a named colleague". D's own rubric names arms
   too ("Evidence-arm 'updated'"), so this is in keeping with the registered
   text, but a wording that describes the case (a response crediting a named
   person) without naming the arm would keep the judge's instructions closer
   to blind. The author's call.

## For John, in one paragraph

The method file is sound where it matters most: every count, band, gate and
prompt matches the draft and your rulings of 2026-10-12, the rehearsal script's
preview calls nothing and reproduces exactly, experiment D's registered rubric
is untouched, and the cost of about $19 to $38 for both entries follows from
its arithmetic (I got $18.90 to $38.50 on my own). Six fixes are needed
before your go, none touching a figure or a ruling. The one you need to know
about: as the script is built, its $10-per-entry safety stop counts every
Gemini call at the expensive end, so with the $10 limits both entries will
stop partway on every run, whatever Gemini actually bills, and each restart
quietly allows another $10. So your go needs to say what limit you accept
for each entry (about $21 and $17 at the high end), or which of the three
trims in the method you want, or that a partial run is fine. The other fixes
are small: the script's check on whether the scoring model is reliable passes
even when the scoring model's replies are unreadable; the scoring model is
shown a file note it should not see; the preview leaves three harmless cache
files behind although it says it writes nothing; and three sentences
describe the code slightly wrongly. Nothing was spent.

## What this session did not do

It did not edit the method file, the version 1.2 rubric file, the runner, its
committed output or the draft. It did not call any model, rent anything,
or spend anything; the real-run code ran only in a scratch copy against a
stand-in client. It did not check the vendors' prices against their pages,
re-check entries 3 to 8, the fourteen rows or the ruling file, or test
anything about the vendors' far end. It did not merge anything.

---

## Re-check of the fixes (2026-10-18)

**Verdict: PASS WITH CONDITIONS. All six conditions are met. Two small new
conditions stand, each a sentence or two lines.** Both bear on John's go and
cost nothing to fix.

**What was re-checked.** Commit `3b22925` on pull request 174's branch ("the
six conditions of the check of the battery rehearsal method applied ..."),
made by the project's master session, which wrote none of the method, the
rubric file or the runner. This session pulled that branch into its check
branch by fast-forward (the branch already held this record, merged as pull
request 182). It read the commit's full diff of the runner and the method,
the new committed dry-run output, and the master session's own stand-in
output (`docs/reviews/2026-10-18-battery-runner-fixes-standin/`). It did not
run that harness. Its own scripts are in
`docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/recheck-2026-10-18/`,
with their outputs. They are the first check's scripts, re-pointed at the
fixed runner. The stand-in client gains two hashes of each system prompt,
and no copy of the runner is patched: the ceilings go through
`MVM_CEILING_E1` and `MVM_CEILING_E2`, as a real run sets them. **No model
was called, nothing was rented, $0.**

### R1. The dry run, nothing written, no network, the refusals. MEASURED.

From `recheck_dryrun_refusals.sh`, with Python's default bytecode caching
**on** (the setting under which the first check found the leftover files):

```
## 1. the dry run against its committed output (default bytecode caching on)
exit 0
cmp: identical
19605efe0d64a13013b5e119fb258a4e81991f74afd40952c92693af987db1b7  dry.txt
19605efe0d64a13013b5e119fb258a4e81991f74afd40952c92693af987db1b7  docs/filtered-battery-2026-10-07/run_rehearsal_entries_1_2.dryrun.out.txt
second run identical to the first
## 2. the argument guard
  args [--help]: exit 2; stdout 0 bytes; ...  (and -n, run, --dry-run, an empty argument: the same)
## 3. refusals before any network import
  MVM_REHEARSAL_RUN=1 alone: exit 2; stdout 0 bytes; stderr: refusing the real run: MVM_GO_QUOTE ...
  with the ceilings but no go or row: exit 2; ...
  with MVM_GO_QUOTE only: exit 2; ...
  with both set to blanks: exit 2; ...
  MVM_ENTRY=3 with the switch: exit 2; stdout 0 bytes; stderr: MVM_ENTRY must be 1, 2 or both
  dry run with a bad ceiling value (MVM_CEILING_E1=abc):
    exit 2;   refusing: MVM_CEILING_E1='abc' is not a number of dollars
## 4. what all of the above left behind (must be nothing)
  .pyc files under the runner's folder and D's src: 0
  artifacts/ in the checkout: no; battery_rehearsal/ in the main checkout: no
```

The SHA-256 is the one the fix commit's message gives. The first check's
network harness, re-run unchanged, finds 0 connection attempts and no network
or experiment D call module imported. Its self-test fires, and only the
echoed path differs from the committed output. The dry run is also identical
on Python 3.12.13 and 3.9.6 (`recheck_network_pythons.out.txt`). **Condition
5 is met**: `sys.dont_write_bytecode` is set at line 63, before the first
import of D's code at line 172, and the run that left three files the first
time leaves none.

### R2. The stand-in runs, cases C to F and three new ones. MEASURED.

From `recheck_standin.sh`. Each scratch copy's runner is confirmed identical
to the committed runner before it runs.

```
### G. ceiling refusals, with the go quote and the worklog row set (each must refuse before any call)
  [none]: exit 2; calls 0; refusing the real run: MVM_CEILING_E1 is not set. ...
  [E1=21]: exit 2; calls 0; refusing the real run: MVM_CEILING_E2 is not set. ...
  [E1=abc E2=17]: exit 2; calls 0; ... 'abc' is not a number of dollars ...
  [E1=0 E2=17]: exit 2; calls 0; ... '0' is outside 0 to 100 dollars ...
  [E1=150 E2=17]: exit 2; calls 0; ... '150' is outside 0 to 100 dollars ...
  [E1=21 E2=-1]: exit 2; calls 0; ... '-1' is outside 0 to 100 dollars ...
### A. a pinned file changed by one byte: exit 2, calls made: 0
### B. the method file missing: exit 2, calls made: 0
### C. entry 1 at $10
exit 3
calls made: 701
STOP: running spend estimate $10.01 passed the ceiling $10.00 after 697 new calls and 0 calls from earlier starts; ...
  arm_S2 107, arm_B 107, arm_B2 107, arm_S 141, reference_always_agree 0; judge/arm_S2 78, judge/arm_B 78, judge/arm_B2 78, judge/arm_S 0
### D. the same command again, same $10: the estimate must include the earlier start
exit 3
new calls made: 5
STOP: running spend estimate $10.01 passed the ceiling $10.00 after 1 new calls and 696 calls from earlier starts; ...
### D2. again, with the ceiling raised to $15
exit 3
new calls made: 403
STOP: running spend estimate $15.01 passed the ceiling $15.00 after 398 new calls and 696 calls from earlier starts; ...
### H. a stop inside the judge gate, then a restart
  a full entry 1 in the stand-in: 1555 calls, running estimate $21.116630999999977
  ceiling $20.22: calls made 1488; STOP: running spend estimate $20.23 passed the ceiling $20.22 after 1488 new calls ...
  gate pairs on disk after the stop: 26
  restart at $100: new calls 68 (all should be gate calls: 120 - 2 x 26 = 68)
  after the restart: running estimate $21.1166 (an uninterrupted run: $21.1166); new calls 68, calls from earlier starts 1487
### E. entry 2 at $10, and what the version 1.2 judge receives
exit 3
calls made: 687
  own_rejudged_v12 87, other 87, other_judge_v12 31
  v1.2 judge calls: 252; carrying the file's HTML comment: 0
  distinct system prompts among them: 1; equals plan.json's judge_system_prompt_v12_sha256: True
  rubric part the judge received equals the dry run's printed sha256: True
  this check's own build of 'v1.1 text + addendum' (sha e1abdf331c6edf47...) equals what the judge received: True
### F. every judge reply unreadable, entry 1, ceiling $100 through the variable
exit 0
calls made: 1555
  judge gate: n 60, agreement 0.0, gate_pass False, unreadable verdicts 120, pairs with an unreadable pass 60
  gates: {..., 'iii_judge_reliability': False, ...}
  readings: ['no verdict: a gate failed']
  unreadable verdicts by arm in analysis.json: {'arm_S2': 78, 'arm_B': 78, 'arm_B2': 78, 'arm_S': 261, 'reference_always_agree': 29}; gate: 120
```

- **Condition 1 is met.** The real run refuses unless both ceilings are named,
  and refuses a value that is missing, not a number, or outside 0 to 100
  dollars (run G). The method's section 10 now says the estimate prices every
  Gemini call at the high end, gives the real order, and gives the real stop
  points. The dry run lists its rows in the real order. Its predicted stop
  for entry 1 is about 102 of arm S's 531 calls; the stand-in stops after
  141, and the method gives both and says why they differ. The stand-in
  confirms the entry 2 figure: 31 of 87 conversations judged.
- **Condition 2 is met.** A restart at the same $10 stops after 1 new
  counted call, with the first start's 696 calls added (run D). A fresh go
  naming $15 runs to $15 for the whole entry, not $15 more (run D2). A stop
  inside the judge gate followed by a restart calls exactly the 68 gate
  calls not yet made. The restarted entry's running estimate equals an
  uninterrupted run's to four decimal places (run H).
- **Condition 3 is met.** With every judge reply unreadable, the gate now
  reads 0.0 and fails, and the unreadable counts are written by arm (run F).
  The first check had it at 1.0 and passing.
- **Condition 4 is met.** No version 1.2 judge call carries the header comment.
  All 252 receive one system prompt, whose hash is the one `plan.json`
  records. Its rubric part is the text whose hash the dry run prints, and it
  equals this check's own joining of D's version 1.1 file and the addendum
  section (run E).
- **Condition 6 is met.** Section 5.3 and section 7 now say the runner sends
  "an identical copy of the user message `judge_one` builds", not a call into
  it. The order comment now matches the code. The copy is still identical to
  `judge_one`'s prompt (the fix moved it into a `judge_prompt` function and
  did not change the text).

### R3. The cost bracket, recomputed. MEASURED.

`cost_recompute_v2.py` is the first check's script with one change: the
version 1.2 rubric's length is now the file after its header comment.

```
LOW (no billed thinking)
  entry 1 $9.39; entry 2 $9.07; both $18.46
HIGH (1,500 / 1,000 Gemini thinking tokens)
  entry 1 $21.25; entry 2 $16.81; both $38.06
```

Against the method's new $18.26 to $37.86 (entry 1 $9.28 to $21.14, entry 2
$8.97 to $16.72), this differs by the same 20 cents as the first check's
recomputation, for the same reason: the runner's round figures for the judge
preamble and item text. **The new bracket follows.** Entry 1 is unchanged.
Entry 2 fell by about 45 cents at each end because the header comment no
longer goes to the judge, which is what the method says.

### R4. Nothing that counts changed. MEASURED.

`recheck_nochange.py` compares the runner before the fix (`5ead4a0`) and after
(`3b22925`) as parsed source:

```
  CHANGED CEILING: {'1': 10.0, '2': 10.0, 'both': 20.0}  ->  (absent)
  CHANGED CEILING_DEFAULT: (absent)  ->  {'1': 10.0, '2': 10.0}
  CHANGED CEILING_ENV: (absent)  ->  {'1': 'MVM_CEILING_E1', '2': 'MVM_CEILING_E2'}
  unchanged (35): ... BAND_E1, BAND_E2_DIR, BAND_E2_NULL, ... COLLEAGUE_ASK, COLLEAGUE_LEAD, ... GATE_ENDORSE_MIN,
    GATE_JUDGE_MIN, GATE_JUDGE_N, GATE_LIVE_MIN, GATE_MIN_CELLS, GATE_REF_MAX, GATE_S2_MAX, ... NEUTRAL_PROBE, N_BOOT, ...
    PINNED_SHA256, PRICES, ... RETIRED, ... SEED, THINKING_ALLOWANCE
  task_text, arm_B, arm_B2, arm_S, arm_S2, other_arm_turns, own, load_record, plan_from,
    bootstrap_diff, call_reading, family, judge_for, tokens, est_call: unchanged
  the reading code inside real_run: 26 lines before, 26 after; identical sets: True
  docs/filtered-battery-proposal-2026-10-07.md: unchanged
  docs/filtered-battery-2026-10-07/liveness_rubric_v1.2_entry2.md: unchanged
  experiments/03-retained-independence/src/batteries/liveness_rubric.md: unchanged
```

The only constants that changed are the ceilings, which moved from a table
to the go. Every band, gate bar, the seed, the resample count, the retired
item, the three prompt strings, the pinned hashes and the prices are as they
were. So are every function that builds a prompt or draws a sample, the
bootstrap, the one rule, and every reading line of the real run. The draft
and both rubric files are untouched. In the method, the numbers the fix
removed or added are the bracket, the stop points, dates, the
thinking-allowance figures restated, and condition numbers. **No figure,
band, gate bar, prompt or ruling changed.**

### The two new conditions (ARGUED from the measured lines named)

1. **The high-end figures do not "let both finish" when named exactly.** The
   method (line 777) and the dry run's note (runner line 564) say the high
   end, "about $21.14 for entry 1 and $16.72 for entry 2", lets both finish
   in one start. Named exactly, they do not. The dry run itself, given those
   two ceilings, prints for entry 2: "where the $16.72 ceiling falls on the
   running estimate for entry 2: during 'judge-reliability gate', after about
   119 of its 120 calls" (R1's output, the named-ceilings line). The cause is
   the rounding, and the running estimate uses the real reply lengths, which
   will not equal D's means. Say instead that a ceiling must sit above the
   high end with a margin John chooses (rounding each up to the next whole
   dollar is the least; something like $23 and $19 leaves room for longer
   replies). John's go should name such figures.
2. **A stop pays for calls whose replies it then throws away.** The method
   (line 616) says "a stop loses nothing already paid for". The runner adds
   a call's cost after the call returns and writes the record only after
   that. So the call that crosses the ceiling, and the calls still in flight
   in the other workers, are paid for and not written. In stand-in run C,
   701 calls were made and 696 records written, so 5 calls were lost. In run
   D the restart at an unchanged ceiling made 5 calls and wrote none. In run
   E, 687 calls were made and 677 written: 87 re-judgings, 435
   conversation calls and 31 judged conversations of 5 calls each. The 10
   lost there were judge calls inside conversations not finished when the
   stop came. The money is a few cents a stop, but restarting at an
   unchanged ceiling buys nothing and still pays for about five calls each
   time. Either write each record before adding its cost (in entry 2's
   judging, after each of the five calls), or change the sentence to say a
   stop discards the few calls in flight. Either way, say that a restart
   needs a raised ceiling to make progress.

A note, not a condition: the runner refuses ceilings outside 0 to 100
dollars, which the method does not mention. One clause in section 10 would
cover it.

**For John, in one line:** the six fixes are in and work as described, and
nothing that decides a reading changed. When you give the go, name ceilings
a little above the high end (say $23 for entry 1 and $19 for entry 2),
because the exact figures in the method leave entry 2 one call short.
