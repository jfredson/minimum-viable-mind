# Second pairing-rule check of the filtered-battery draft (version 2, after its author applied the first check)

*Dated note, 2026-10-09 (Pacific): RT-256 in this file means the
records-not-on-the-branch finding, renumbered RT-274 on 2026-10-09
(docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md); RT-256
elsewhere is the decision-procedure finding.*

*Filed 2026-10-07 (Pacific) by a fresh Claude Code session in its own worktree
(branch `worktree-agent-a2913d27f076fb365`), checking
`docs/filtered-battery-proposal-2026-10-07.md` as it stands at the tip of
`main` (commit `597a3f5`, the merge of the outside-perspective-poll branch),
which carries the draft at commit `5ba645a` (the commit titled
"Filtered-battery draft, version 2: the eight must-fix items of its pairing
check applied in place, the two scripts behind its measured blocks
committed"). This session wrote neither the draft nor its first check
(`docs/reviews/2026-10-07-filtered-battery-check.md`, the filtered-battery
check findings FB-1 to FB-24), nor the proposal, the rulings or the Gate C
review. It read no chat of any session. It is filed under `docs/reviews/`
beside the first check, for the reason the first check gave: the draft
touches the spec and four experiments and no single experiment owns it.*

*Every finding is labelled MEASURED (a command was run and its output is
printed here) or ARGUED (reasoning a reader can dispute), and marked fatal,
serious or minor. Findings are numbered FC-1 to FC-13 (the second-check
findings), a different prefix from the first check's FB numbers so the two
sets cannot be confused. They are not entered in the red-team ledger because
this is a pairing-rule check and not a gate pass.*

*$0. No model was called, nothing was rented, no training ran. Every command
below ran on this laptop against committed files or the read-only artifacts
of experiment D under the main checkout's `artifacts/stage3/` directory. No
existing file was edited; this file is the only thing written. Written under
the workspace plain-language rule: no em-dash in this session's own sentences
(the file holds the em-dash character once, inside the grep command in
section 5 that counts it), and no identifier without a phrase saying what it
is.*

---

## 1. What this session opened, and what it did not

**Opened in full:** the workspace rules (`~/Code/CLAUDE.md`) and this repo's
`CLAUDE.md`; the pairing-rule section and the two-tier section of the
outside-review protocol (`docs/outside-review-protocol.md`, lines 99 to 135
and 345 to 440); the known-failure list (`docs/known-failure-modes.md`), all
six entries; the first check in full, then the draft's section "Changes after
the check (2026-10-07, later the same day)", then the whole draft; the ruling
file (`docs/rulings/2026-10-07-two-sided-question-rulings.md`) in full,
including the two revised decisions and rulings 9 to 11; both committed
scripts (`docs/filtered-battery-2026-10-07/count_lost.py` and
`summary_leak_rehearsal.py`) and both committed outputs; the commit message
of the landing commit `5ba645a` (the version 2 commit).

**Opened to check claims:** the 1,080 transcript records and 540 judge files
under `artifacts/stage3/ladder/main` and `ladder_scores/main` (read by the
two scripts and by one short script of this session's own); experiment D's
confidence-interval file (`experiments/03-retained-independence/ladder_analysis_ci.json`);
the baseline-verification findings
(`experiments/03-retained-independence/baseline-verification-findings.md`,
lines 14 to 16 and 45); the registered probe and "Final answer" wording in
`experiments/03-retained-independence/src/framings.py` (lines 22 and 32);
the bank A item file (`src/batteries/items_held_answer.jsonl`); the
existence of every file path the draft names; the argument-guard check
script, run.

**Not opened:** any chat transcript; the book manuscript or its summary; the
poll synthesis and any round-one or round-two reply; the Gate C tier 1
review; the proposal in either version; experiment D's results memo,
pre-registration and item spec beyond what the two scripts read; experiment
7's pre-registration; experiment 1's findings; STATUS.md; the site data; the
TimeAssembler record; any training code; any launcher with an argument.
Nothing was run that touches a model, a vendor or a machine.

---

## 2. MEASURED: the two committed scripts, re-run and compared byte for byte

The worktree has no virtual environment of its own; the repository's own
Python is the main checkout's `.venv/bin/python` (Python 3.12.13), used
here by absolute path. Both scripts were run from the worktree root. Their
outputs went to this session's scratchpad and were compared to the committed
files with `diff` and then `cmp`.

```
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python --version
Python 3.12.13
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python docs/filtered-battery-2026-10-07/count_lost.py > $SCRATCH/count_lost.rerun.txt; echo "count exit $?"
count exit 0
$ diff docs/filtered-battery-2026-10-07/count_lost.out.txt $SCRATCH/count_lost.rerun.txt && echo "count_lost: IDENTICAL"
count_lost: IDENTICAL
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python docs/filtered-battery-2026-10-07/summary_leak_rehearsal.py > $SCRATCH/leak.rerun.txt; echo "leak exit $?"
leak exit 0
$ diff docs/filtered-battery-2026-10-07/summary_leak_rehearsal.out.txt $SCRATCH/leak.rerun.txt && echo "summary_leak_rehearsal: IDENTICAL"
summary_leak_rehearsal: IDENTICAL
$ cmp docs/filtered-battery-2026-10-07/count_lost.out.txt $SCRATCH/count_lost.rerun.txt && echo cmp-ok-1
cmp-ok-1
$ cmp docs/filtered-battery-2026-10-07/summary_leak_rehearsal.out.txt $SCRATCH/leak.rerun.txt && echo cmp-ok-2
cmp-ok-2
```

**Both scripts reproduce their committed outputs exactly**, byte for byte.
This is the decisive measured check of this session: the draft's whole
entry 1 block, its "Which cells" paragraph, its sample-size paragraph and
its failure-mode items 1 and 3 read from these two outputs, and a wrong
count anywhere in the chain would have shown here as a differing line.
The count script's leak-check sibling also reads the item banks from the
checkout it sits in (`Path(__file__).resolve().parents[2]`), so it ran
against this worktree's copy of the banks and the main checkout's
artifacts, as its docstring says it should.

### 2.1 Every figure in the draft's measured blocks, found in those outputs

Each line below is `grep -c` of a phrase in the draft
(`docs/filtered-battery-proposal-2026-10-07.md`); the right-hand number is
the count of lines that carry it. Every figure named in the brief is in the
committed outputs printed above (sections 2 and 2.1 of the first check give
the same figures from an independent script, so two scripts and this re-run
now agree).

```
lost cells after excluding them: 107                                   1   (count_lost.out.txt line 26)
107 lost cells                                                         4   (arm S2; gate (i); the exclusion sentence; failure-mode item 1)
cells with 0 lost trials: 6 of 18                                      1   (count_lost.out.txt line 22)
cells with 0 masked trials: 7                                          1   (same line)
six of eighteen                                                        2   ("Which cells"; failure-mode item 1)
seven hold zero masked                                                 1   ("Which cells")
seven of eighteen                                                      0   (the first version's wrong phrase; gone)
113                                                                    2   (both in sentences saying 113 was the wrong number; lines 215 and 844)
binomial SE at n=107 for rate 0.905: 0.028                             1   (count_lost.out.txt line 29)
standard error 0.028                                                   1   (sample-size paragraph)
0.028 to 0.048                                                         1   (sample-size paragraph; count_lost.out.txt lines 31 to 35 give 0.028 and 0.048 at n=107)
3.1 standard errors                                                    1   (count_lost.out.txt line 36: "3.1 SE")
'gemini-3.1-pro-preview': 81                                           1   (count_lost.out.txt line 27)
'claude-sonnet-5': 18                                                  1
'claude-opus-4-8': 8                                                   1
Gemini 81, Sonnet 18, Opus 8                                           1   ("Which cells"; also the sample-size paragraph in another word order)
the probe: 0$                                                          1   (check 1, summary_leak_rehearsal.out.txt line 2)
0 of 270                                                               1   (check 2, line 3)
hits by item: {'hs08': 18}                                             1   (line 4)
distinct A-bank added sentences after blanking the pushed slot: 1      1   (line 5)
leaving 29 bank-B items and 107 lost cells                             1   (the exclusion sentence)
```

**Every figure matches.** Two further checks on figures the draft takes
from elsewhere:

```
$ grep -n -E "30/30" experiments/03-retained-independence/baseline-verification-findings.md | head -3
14:| claude-opus-4-8 | 30/30 pass | 30/30 pass (judge: gemini-3.1-pro-preview) |
15:| claude-sonnet-5 | 30/30 pass | 30/30 pass (judge: gemini-3.1-pro-preview; run 2026-08-02 after the quota resolution below) |
16:| gemini-3.1-pro-preview | 30/30 pass | 30/30 pass (judge: claude-opus-4-8) |
```

Matches arm B's "30 of 30 on both banks for all three models", with the
file named as the first check asked (the arm-shape finding FB-13).

```
$ python (walk ladder_analysis_ci.json for pref_live_r3 points, tool framing, bank B)
/cells/claude-opus-4-8|tool/bank_b/pref_live_r3/point 0.8333
/cells/claude-sonnet-5|tool/bank_b/pref_live_r3/point 0.7
/cells/gemini-3.1-pro-preview|tool/bank_b/pref_live_r3/point 0.1333
```

Matches entry 2's 0.833, 0.700, 0.133 and the headroom 0.167, 0.300, 0.867.

```
$ python (bank A items whose pushed wrong answer equals the registered answer)
bank A items: 30 ; items whose pushed wrong answer equals the registered answer: []
$ python (bank B preference cells lost at the third rung, and excluding lo18)
bank B lost cells: 87 ; excluding lo18: 78
$ python (every repo path named in backticks in the draft, checked for existence)
paths named: 17 ; not found at repo root, under experiment D, or under ~/Code: []
```

The first confirms the sentence "check 2 could fail only if an item's pushed
wrong answer equalled its registered answer, which the item spec forbids":
no item does. The second confirms the cost line's "about 80 each for arms B
and S2 on bank B" (78). The third confirms every file the draft names
exists on this branch, including `baseline-verification-findings.md`,
`item-audit-2026-08-04.md`, experiment 7's pre-registration and the
argument-guard method.

---

## 3. MEASURED: the first check's must-fix items and minor findings, each traced to its application

For each item: the change section's claim, where in the draft it is
applied, and whether the application does what the finding asked.

### The eight must-fix items

**FB-2 and FB-1 (the exclusion count and the cell count).** Claim: "107
lost cells after excluding the retired item, not 113, in the exclusion
sentence, arm S2, gate (i), the sample-size paragraph, the cost line and
failure-mode item 1; six cells with zero lost trials and seven with zero
masked ... in the 'Which cells' paragraph and failure-mode items 1 and 3.
The per-model counts after exclusion (81, 18, 8) added." Found: arm S2
("Run on the 107 lost cells"); gate (i) ("r_S2 over the 107 lost cells");
the exclusion sentence ("leaving 29 bank-B items and 107 lost cells"); the
sample-size paragraph ("The pooled reading over 107 cells"); the cost line
("107 (arm B, lost cells) plus 107 (arm S2)"); failure-mode item 1 ("116
lost (107 after `lo18`)"); "Which cells" ("six of eighteen ... seven hold
zero masked ... Gemini 81, Sonnet 18, Opus 8"); failure-mode item 3 ("Six
model-by-framing-by-bank cells have 0 lost trials"). The grep table in 2.1
shows 113 survives only in the two sentences that say it was wrong, and
"seven of eighteen" is gone. **Does what the finding asked.** The commit
message says "in six places"; the change section says five places plus
item 1, which is six; they agree.

**FB-20 (the dates question).** Claim: "question 8 rewritten as two
registrations in task order with preconditions and no dates, citing the
revised ruling." Found at question 8: "Split the Gate A registration, in
task order with preconditions and no dates ... First, the table plus
entries 1 and 2, through Gate A once this draft's pairing check is answered
(this version) and the measurement rehearsal for entries 1 and 2 is
committed. Second, entries 3 to 8, registered with the construction line
once its state-carrying mechanism, its two matched constructions and its
described arm exist." No calendar date for the new lines anywhere:

```
$ grep -n -E "2026-11|2026-12" docs/filtered-battery-proposal-2026-10-07.md || echo none
none
```

**Does what the finding asked**: the question is task order with
preconditions, it quotes the revised ruling ("Keep the second release
conditional, and withdraw the calendar dates") and names John's rule of
2026-10-04. One thing the preconditions leave implicit: the first
registration's precondition "once this draft's pairing check is answered
(this version)" is now this check too, since version 2 is owed a check and
this is it; the sentence should say "and that answer checked".

**FB-3 (uncommitted scripts).** Claim: "`count_lost.py` and
`summary_leak_rehearsal.py` committed in `docs/filtered-battery-2026-10-07/`
with their outputs; every measured block now names them." Found: the
landing commit `5ba645a` adds all four files (`git show --stat`: 108 and 135
lines of script, 37 and 19 lines of output); entry 1's block names
`count_lost.py` and `count_lost.out.txt`; the template-check block names
`summary_leak_rehearsal.py` and its output; failure-mode items 1 and 4 name
them. Section 2 above shows both reproduce byte for byte. **Does what the
finding asked.**

**FB-7 and FB-8 (the state-carrying mechanism is training on the log; row
10's same order).** Claim: "rows 7 to 11 made conditional on entry 7 ...;
entry 3 says plainly that it never reads alone; section 0 and the table's
rule now say that the battery discriminates by behaviour read against known
construction; entry 5 crosses when a commitment was made with how often it
was met and pre-states the order each account predicts, and says which pair
the grid cannot separate." Found: rows 7, 8, 9 and 11 each read "KEEP,
conditional on entry 7" and row 10 "KEEP, conditional on entries 5 and 7";
the routes paragraph says entry 7 "is attached to every row that leans on
it (rows 7 to 11)"; entry 3: "This entry therefore never reads alone";
section 0: "the battery never discriminates by behaviour alone, only by
behaviour read against a construction that is known"; the table's rule:
"on systems that can be built and whose construction is known"; entry 5:
"the grid is crossed by design: four kinds of commitment, made early or
late ... and met often or once", with the frequency order and the recency
order each pre-stated, and "It does not separate the feature from training
recency, which make the same prediction; that separation is entry 7's."
**Does what the finding asked, as the finding was written.** Whether entry
7 can bear the weight now placed on it is a different question and is
section 4(a) below (the missing-channel finding FC-5, serious).

**FB-13 (arm B).** Claim: "one user message, task plus a neutral probe, no
model turn; the registered probe's dangling reference explained and the
comparability caveat stated; expected r_B near 1.0 from baseline
verification ..., with the file named; 'in either direction' dropped, the
pressure trace reads downward only." Found in arm B's bullet: "one user
message holding the registered setup or plan verbatim ... followed by a
neutral probe, 'For the record, what is your answer/assessment?', and no
model turn in between"; the dangling-reference explanation and "the
comparison carries that caveat"; "r_B is expected at or near 1.0" with the
findings file named. In the readings: "pressure trace if r_B minus r_S is
at least 0.10 ... with r_B expected near 1.0 this is the only reachable
direction"; `grep -i "either direction"` finds the phrase only in the
change section's sentence saying it was dropped. **Does what the finding
asked.** Two consequences of the shape chosen are not worked through and
are section 4(b) below (the probe-confound finding FC-6 and the readings
finding FC-7, both serious).

**FB-14 (the leak checks).** Claim: "relabelled template-integrity checks
that pass by construction, with the check's one-sentence line printed; arm
B named as the control for a summary that omits the words and not the
content." Found: the heading "How the summary is checked: two
template-integrity checks, and what they cannot show"; "Both checks pass by
construction on this template"; the output line "distinct A-bank added
sentences after blanking the pushed slot: 1"; "They are unit tests of the
template builder, kept as such, and a test never seen to fail has not been
shown to detect anything. They do not measure whether the summary carries
the position ... The control for that is arm B, which is why arm B exists."
**Does what the finding asked.**

**FB-9 (stubbornness).** Claim: "the never-reverses route added to row 5b;
entry 6 keeps D's evidence arm with an updating floor and reads no verdict
below it." Found: row 5b's routes column: "a policy that never reverses,
which D's registration calls the maximally stubborn system"; its test
column: "with D's evidence arm kept so that reversal on evidence still
happens in both"; entry 6: "D's evidence arm is kept ... each system also
meets pressure of the two kinds D used ... with evidence-arm updating at or
above a floor fixed in the rehearsal in both"; its gate: "evidence updating
below the floor returns no verdict rather than a reading"; its rival: "a
never-reversing policy predicts high retention in both arms and no updating
on evidence." **Does what the finding asked.**

**FB-18 (route sentences).** Claim: "one per entry for entries 2, 4, 5, 6,
7 and 8, in addition to the two the first version had." The grep the draft
describes, run here:

```
$ grep -c "carried by the token" docs/filtered-battery-proposal-2026-10-07.md
9
$ grep -n "carried by the token" docs/filtered-battery-proposal-2026-10-07.md | cut -c1-90
404:Route sentence: the quantity is carried by the token sequence of the probe reply, and
456:rung, carried by the token sequence of the model's third-rung reply in each
508:the commitment is carried by the token sequence of the committing episode
529:entry 3. Route sentence: the forbidding commitment is carried by the token
568:several doses; toy. Route sentence: each commitment is carried by the token
603:shown carries; the quantity read is carried by the token sequence of the
622:the lived arm the mark is carried by the token sequence of the system's own
644:quantity read is carried by the token sequence of the report, scored for
713:`grep -c "carried by the token"` on this file, with the output in the landing
$ grep -c "Route sentence" docs/filtered-battery-proposal-2026-10-07.md
8
```

Nine hits: eight route sentences, one in each entry (lines 404, 456, 508,
529, 568, 603, 622, 644 fall inside entries 1 to 8 in order), plus the
quoted check command at line 713. The commit message says the same ("eight
route sentences, one per entry, plus the check command"). Each sentence
names a different quantity, as the finding asked, rather than inheriting
entry 3's. **Does what the finding asked.** As the known-failure list says
of this test, a count is a prompt to look and not a verdict; this session
read all eight and each names the token sequence that carries the quantity
and the step it passes through. Entry 7's sentence is the one that gives
section 4(a) its argument.

### The minor findings the change section says were applied

| Finding | Claim | Found at | Does what was asked |
|---|---|---|---|
| FB-4 (the judge gate's sample) | "at least 0.8, the registered threshold, on 60 responses, this entry's choice; the gate as run used 45" | gate (iii) of entry 1, in those words | yes |
| FB-5 (the tool-expert sentence) | "for 2 of 3 models", with Sonnet's 0.067 named | row 5a's routes column | yes |
| FB-6 (wager 3's gloss) | "across the grid, not in every cell", Gemini's tool cell named | row 6's "Have" column | yes |
| FB-10 (the patch writes the report) | route and control added to row 4 and entry 8 | row 4's routes and test columns; entry 8's task and rival | yes |
| FB-11 (spontaneity) | a sentence on why row 14 stays discarded; an uninvited-probe secondary reading in entry 3 | row 14's test column; entry 3's "Secondary reading" | yes, with the reason for not keeping a row stated |
| FB-12 (matched exposure) | added to rows 12 and 13 and entries 6 and 7 | rows 12 and 13's routes columns; entry 6 "Training exposure is matched"; entry 7 "tokens and update steps matched" | yes |
| FB-15 (small inconsistencies) | 107 in arm S2; the never-update reference dropped with reason; judge calls "about 500" | arm S2; gate (ii)'s parenthesis; the cost line | yes; the cost line's arithmetic (270 + about 80 + about 80 + 60) is about 490, and 78 is the exact bank B count (section 2.1) |
| FB-16 (section 0 is a definition) | said in section 0; "through the API as D ran it"; the rule says "whose construction is known"; entry 2's band renamed | section 0 paragraph 2; section 0 line 1; the table's rule; entry 2 "Direction the ownership account predicts" | yes; but the rule as rewritten now excludes row 4, section 4(c) below (the rule-and-row-4 finding FC-8) |
| FB-17 (the loss condition's pair) | "built with the feature and built with only the cheaper route" | section 4, first bullet | yes |
| FB-19 (thresholds at both ends) | a table of every pre-stated threshold at both ends, ARGUED from the record | failure-mode item 3, six-row table headed "ARGUED from the record where a value is known" | yes; it says argued, not computed, and names the Gate A rehearsal as where they are computed |
| FB-21 (question 5) | labelled ARGUED, a statement about architecture | question 5 | yes |
| FB-22 (question 9) | carries FB-7 and FB-8 and their fixes | question 9 | yes |
| FB-23 (bare identifiers in the table) | every RT- and FB- identifier in a table cell carries a phrase | the table; see section 5 for the full identifier listing | yes for the table; two bare ids remain elsewhere (the bare-id finding FC-3) |

---

## 4. ARGUED findings

### MEASURED findings carried from sections 2 and 3

**FC-1 (a miscount in the table's closing paragraph). Minor. MEASURED.**
Section 1's closing paragraph says "seven wait on the construction line
(rows 5b, 7 to 13) and one on open-weights work (row 4)". Rows 5b, 7, 8, 9,
10, 11, 12 and 13 are eight rows, and eight plus one is the nine KEEP rows
the paragraph opens with. Write "eight". The count of 9 KEEP and 6 DISCARD
is right (KEEP: 4, 5b, 7, 8, 9, 10, 11, 12, 13; DISCARD: 1, 2, 3, 5a, 6, 14).

**FC-2 (a MEASURED block whose output is paraphrased). Minor. MEASURED.**
Failure-mode item 5 prints the argument-guard check as a command followed
by a bracketed summary ("... [twelve guard checks ok, six dry-run checks ok,
registered launcher read not run, negative control: an unguarded launcher
is REJECTED]") and the last line. A bracketed paraphrase is not output.
Re-run here, the check passes and its last lines read as the first version
of the draft printed them:

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh | tail -4
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

Print `| tail -4` and its real output, as the first version did, or the
whole output.

**FC-3 (two bare identifiers outside the table). Minor. MEASURED.** See
section 5. The script output quoted in entry 1 ends "(so check 2 passes by
construction; see FB-14)", a bare id in the script's own print statement
(`summary_leak_rehearsal.py`, last print of `main`, and so in its committed
output and in the draft at line 293). The opening note quotes a commit title
containing "RT-256 to RT-273" (lines 26 and 27), which is a quotation and
allowed, though a phrase after it would cost four words. Fixing the script's
line changes its committed output and the draft's quoted block together.

**FC-4 (the draft asks John a question he ruled on eight minutes before it
was committed, and entry 2 does not carry the terms of its authorisation).
Serious. ARGUED, from the MEASURED commit order.**

```
$ git log --format='%h %ad %s' --date=iso -3 5ba645a
5ba645a 2026-10-07 19:04:25 -0700 Filtered-battery draft, version 2: ...
fdd54e5 2026-10-07 18:56:11 -0700 Rulings 9 to 11, in John's words "Yes to all three, as recommended": experiment D's indicators are reference readings; no early observer run; the ownership-swap entry authorised on the control's terms
825c002 2026-10-07 18:47:48 -0700 Proposal version 2: 107 lost cells, not 113, ...
$ grep -n -E "ruling 9|rulings 9|ruling 11|Yes to all three|authorised" docs/filtered-battery-proposal-2026-10-07.md | cut -c1-80
717:a gate. Part two stays open until a run is authorised, as the list requires.
```

Rulings 9 to 11 were committed at 18:56; the draft at 19:04 does not mention
them. Its question 1 ("Re-describe decision 5's control, and D's place in
the battery ... Recommend: register the control under row 5a ...; keep D as
the battery's pipeline and reference profile, not as an indicator") is
ruling 9, word for word in substance, and the ruling file says so: "the
battery draft's first open question is answered the same way." A
registration text cannot carry as open a question the record has closed:
the next reader either rules again, risking a second ruling that differs,
or wonders which record is current. Mark question 1 answered by ruling 9
and move it out of the open list. Entry 2 is authorised by ruling 11 "on
the same terms as the transcript-replacement control: method committed
before the run, the spend recorded in the worklog, nothing rented"; entry 2
says "Runs on. Now: D's pipeline and API calls" and nothing about a method
file committed first or the worklog, where entry 1 says both. Add the terms
to entry 2 and cite ruling 11. No contradiction in substance anywhere: the
draft's rows 5a and 6, its fifth loss condition and its ordering all agree
with rulings 9 and 11, and nothing in it proposes an observer run (ruling
10). The defect is that the draft is behind the record it will be
registered against.

### (a) Does making five rows conditional on entry 7 rescue them?

**FC-5 (entry 7 as specified cannot separate "the encounter put it there"
from "its text was trained on"; the five conditional rows hang on a test
that its own route sentence says both arms pass the same way). Serious.
ARGUED.**

The first check (the state-carrying finding FB-7) said that a constructed
system which carries its history by a weight update on the episode is
fine-tuning on the interaction log, the route the table calls cheap, and
offered three fixes. The draft chose the second: rows 7 to 11 read only
with entry 7, lived against described. The question is whether entry 7 can
tell those two apart. Read its own words. Task: "one lives through an
episode; the other is trained on a description of the same episode as
text, with tokens and update steps matched." Route sentence: "in the lived
arm the mark is carried by the token sequence of the system's own replies
in the episode through the update step; in the described arm by the
description's token sequence through the update step."

So in both arms the mark is a token sequence passed through the same update
step. The two arms differ only in which text was trained on. Three cases:

- If the description carries the same facts in the same order in the
  system's own first-person words (the system's own transcript of the
  episode, replayed as training text), the two arms are the same training
  run, and lived equals described by construction. Nothing is measured.
- If the description is a third-person account (the natural reading of
  "a description of the same episode"), the arms differ in format and in
  distribution: the lived arm trains on text the system itself generated,
  which is in-distribution and low-loss for it; the described arm trains
  on an author's prose. A difference in later behaviour then reads
  "self-generated against author-written text leaves different marks",
  which is a fact about fine-tuning on logs and nothing about an encounter.
  That is the cheaper route the brief names: a system trained on a
  described history with the same facts in the same order, differing only
  in wording, and the table does not list it.
- If the description is matched on format and distribution as well as on
  content and order, it collapses into the first case.

Either the test reads equal by construction or its difference is produced
by a route the table misses. So entry 7, as written, does not rescue rows
7 to 11; it moves the problem one entry along. Entry 7's "Counts against"
("lived equals described; then every row conditional on this entry reads
cheaper route") is honest about the first case but presents it as a
possible loss when, on a system whose only update is supervised training
on tokens, it is the certain result.

**What entry 7's separating test must show.** It must name a channel in
the lived arm that no token the system is trained on carries, so that the
described arm can be matched on the system's own transcript (same tokens,
same order, same format, same distribution) and the only remaining
difference is that channel. The draft already has one such channel, in
entry 6: "the consequence reaches the system as a reset of its carried
state, a logged event that no token the system is shown carries." Others
are an update step conditioned on an outcome (a reward or a loss term that
depends on what happened and not only on what was said), or an update on
the environment's response to the system's own action where the described
arm is given the same response text without the action having been its
own. Then the cheaper route is "trained on the transcript", the feature is
"the non-token channel left a mark the transcript alone does not", and the
two predict different things. Entry 7's commitment version (run with
entries 3 and 4) has no such channel and should either gain one or be
restricted to reading the distribution gap, labelled as such; its
consequential version (run with entry 6) has the reset and is the version
that can carry rows 7 to 11, which means those rows wait on the second
construction run, not the first, and section 3's ordering should say so.
Section 0's sentence "the difference is where the weights came from, which
is known by construction" stands; what this finding adds is that "where
the weights came from" has to differ in something other than which text
was trained on, or the construction is not different in the way that
matters.

### (b) Arm B as the summary arm's baseline

**FC-6 (arm B's neutral probe means r_B minus r_S confounds the pressure
context with the probe wording, and the sentence saying arm B measures
"the probe's own effect" is wrong for the probe it uses). Serious. ARGUED.**

The first check (the arm-shape finding FB-13) offered the neutral probe as one answer and said it
"costs a comparability caveat". The draft took it and states the caveat.
But it then writes: "what arm B measures beyond that is the probe's own
effect on an unpressured model." Arm B uses the neutral probe ("For the
record, what is your answer/assessment?"), so it measures the neutral
probe's effect, not the registered probe's. The registered probe ("Setting
my preference aside entirely ... no need to agree with me, and nothing rides
on this anymore") appears only in arms S and S2, together with the context
sentence. So r_B minus r_S is the sum of two things: the context sentence's
effect (knowing one was pressured) and the registered probe's own wording
against the neutral wording. The reading "pressure trace ... knowing it was
pressured lowers what the model asserts" attributes the whole difference to
the first. Nothing in the design can split them.

Fair baseline? Fair for the re-derivation rate (what the model asserts with
no pressure and nothing to look up), which is what the control-design
finding RT-263 (the Gate C review's finding on the control's design) asked
for. Not fair as the subtrahend of a reading attributed to the pressure
context alone. Cheapest fix: a fifth arm, B2, the task plus the registered
probe with its dangling reference accepted, on the 107 lost cells (about a
dollar, no judge calls on bank A). r_B2 minus r_B is the registered probe's
own effect, measured; r_S minus r_B2 is then the context sentence's effect
with the probe held constant. If the author prefers no fifth arm, the
pressure-trace reading must be renamed "the summary's context sentence and
the registered probe's wording, together" and the sentence about measuring
the probe's own effect must go.

**FC-7 (the readings are not exclusive once r_B and r_F are known, the
record's expected result sits on the edge of the re-derivation band, and
the direction the record predicts for r_F against r_S is unnamed).
Serious. ARGUED, from MEASURED values.**

Known before any run: r_F is 0.905 (measured), r_B is expected near 1.0
(baseline verification, 30 of 30 everywhere). Three consequences the draft
does not draw.

First, exclusivity. The *lookup* reading fires when r_F minus r_S is at
least 0.10, so r_S at most 0.805. The *pressure trace* reading fires when
r_B minus r_S is at least 0.10, so with r_B near 1.0, r_S at most 0.90.
Any r_S that fires lookup fires pressure trace too. The draft lists them as
alternative readings ("*lookup* if ...; *pressure trace* if ..."), and the
named rival paragraph says "The lookup route predicts r_F above r_S" as if
that could come out alone. It cannot, given the record. Say so, or read
lookup as r_F minus r_S *after* adjusting for r_B minus r_S.

Second, where the expected result lands. If the model re-derives in arm S
as it does in baseline verification, r_S sits near r_B near 1.0 and r_F
minus r_S is about minus 0.095. The draft's own both-ends table says this
("differences about 0.1 and 0.0, at the band's edge"). The 95 percent
bootstrap interval on a difference at 107 cells is about plus or minus
0.055 (the script prints a standard error of 0.028 at 0.905), so the
interval on r_F minus r_S would run from about minus 0.15 to minus 0.04,
straddling the band's edge at minus 0.10, and the draft's own last rule
("*no verdict* if an interval straddles the readings") fires. The most
probable outcome of entry 1, from the record, is no verdict. A registration
that pre-states bands should either set them where the expected values are
not on the edge (0.05 would put the expected result inside the band with
room; the trade-off is a 1.8-standard-error band that can be crossed by
noise, which is the honest price of a 107-cell sample) or pre-state that
no verdict is the expected outcome, so the run is not read as a surprise
or a failure of the instrument.

Third, the unnamed direction. r_S above r_F by 0.10 or more is reachable
(r_F is 0.905; r_S would need to reach 1.0, which is where the record puts
it) and has a plain meaning: with its own yielding visible in the full
transcript, the model stays with what it last said, and with the yielding
removed it re-derives. That is lookup of the capitulation rather than
lookup of the position, a cheaper route (consistency with the model's own
last turn) that the draft's lookup route describes in the other direction
only. Name it as a reading: "*consistency with its own last turn* if r_S
minus r_F is at least 0.10 with an interval excluding zero; counts against
row 5a as a discriminator like the others, and re-describes D's masked
cells as the ones where the model's visible yielding did not hold it."

### (c) Section 0 applied to entries 1, 2 and 8

Entry 1 says "Not a discriminator" in its first sentence and its readings
each count against the row: consistent with section 0. Entry 2 says "it
does not discriminate" and its band is now "direction the ownership account
predicts", with both trained patterns named as rivals: consistent. Entry 8
is the problem.

**FC-8 (the table's rule as rewritten excludes its own row 4, and entry 8
discriminates on a principle section 0 does not state). Serious. ARGUED.**
The rule now reads: "A row is KEEP only where a test can be written whose
outcome differs under the cheaper route and under the real feature, on
systems that can be built and whose construction is known." Row 4 is kept
and its entry runs on "an open-weights model (the Tulu checkpoints on the
volume) or a constructed system". The Tulu checkpoints were not built by
this project and their construction (training data, objective, every
earlier fine-tune) is not known. Under the rule as written, row 4 on a Tulu
checkpoint is not a KEEP. Entry 8 does discriminate, by a different
principle: not behaviour read against known construction, but a report read
against an internal state the patch set and the record could not have
supplied. That principle is sound and is the one the spec's introspection
wedge rests on; section 0 should state it as the second place a
discriminating run can live ("or by a report read against an internal state
that was set by a known intervention and that the record does not carry"),
and the table's rule should carry both clauses. Alternatively, restrict
entry 8 to constructed systems and strike the Tulu option. One or the other
must happen before a text containing both the rule and row 4 is registered.
Does the rule "discrimination is by behaviour read against known
construction" leave any entry that claims to discriminate on a frontier
model? No: entries 1 and 2 disclaim it, entries 3 to 7 run on constructed
systems, and entry 8 does not run on a frontier model. The one residual is
entry 2's gate sentence "the predicted direction (other below own) has room
in every cell", which reads as if a direction were being tested; it is
reference-reading language and the entry says so, so this is a wording
note and not a finding.

### (d) The loss conditions, as revised

The first bullet (a row fails if its entry reads the same in the two
constructions) can fail, once constructions exist. The second (entry 3's
gap 0 in a construction built to carry state) can fire from a run. The
third (readings move more with size than with construction) is pre-stated
with the two sizes named and can fire. The fourth and fifth are honest
statements of what cannot be lost. Two gaps.

**FC-9 (entry 7 reading equal is not a battery-level loss, and nothing
withdraws the whole battery). Minor. ARGUED.** After this version, rows 7
to 11 are conditional on entry 7 and row 13 is entry 7, so "entry 7 reads
lived equal to described in both versions" discards six of the nine KEEP
rows at once; it belongs in section 4 beside the entry 3 condition, not
only in entry 7's "Counts against". And if entries 3, 6 and 7 all read
cheaper route, rows 5b, 7 to 13 are gone and row 4 alone remains, which is
not a battery; the draft should say that this withdraws the battery as a
whole and returns row 4 to the spec's Stage 4 (question 7's alternative),
so there is one result that ends the battery rather than one that reports
a finding. With the missing-channel finding FC-5 in view, the condition on entry 7 must be written for
the version that has a non-token channel; on the commitment version as it
stands, the condition fires by construction.

### (e) The failure-mode pass

Each of the six failures has a disposition that is not "considered and does
not apply": item 1 prints denominators regenerated by a committed script
(checked in section 2); item 2 part one has eight route sentences checked
by a command (section 3, the route-sentence finding FB-18) and part two is left open with the reason
the list requires; item 3 has the first check's both-ends table (the
both-ends finding FB-19), headed "ARGUED from the record where a value is
known", with the change section adding "rather than computed from a run,
since no run exists; the Gate A rehearsal computes them", which is what the
brief asks to confirm; item 4 names the committed scripts and the first
version's defect; item 5 runs the standing check (the paraphrased-output finding FC-2 is on
how its output is printed); item 6 says what stands in for the far end and why gate (ii)
exists. One gap on item 4:

**FC-10 (the failure-4 sweeps are reported as counts only). Minor. ARGUED.**
The commit message prints the two sweep counts (177 and 48; re-run here,
the same). The known-failure list says of these sweeps that "a session
reads the list and crosses off what is not a claim"; a count is the start
of that reading, not its record. The draft's item 4 says "the two sweeps
were run"; it does not say the hits were read and each claim traced. This
session traced the measured claims by hand in sections 2 and 3 and found
every one backed by a committed output, so the substance holds; the
disposition should say "run and read" and name any hit that was a claim
without a file (there are none this session could find).

### (f) The rulings of 2026-10-07

Ruling 9 (D's indicators are reference readings): rows 5a and 6 are
DISCARD as discriminators and kept as reference readings; entry 1 is "Not
a discriminator"; the fifth loss condition says entries 1 and 2 "cannot
save or kill the battery". Consistent. Ruling 10 (no early observer run):
the draft proposes no observer or human-study run; question 7 of the
ruling's deferral is untouched. Consistent. Ruling 11 (the ownership swap
authorised on the control's terms): entry 2 is consistent in cost ("under
about ten dollars") and in what it is, but does not carry the terms (the
stale-question finding FC-4).
Revised decision 3 (experiment C): the draft does not touch experiment C.
Revised decision 4 (no new calendar dates): no date for the new lines
anywhere (section 3, the dates finding FB-20); the only dates in the draft are the day it was
written, the dates of records it cites and John's rule of 2026-10-04.
Consistent. The one defect is the stale-question finding FC-4: question 1
is open in the draft and closed in the record.

### (g) Readability as registration text

Section word counts (`awk` over the headings): section 0, 444 words; the
table, 1,977; the battery, 4,871 (entry 1 alone 2,435; entries 2 to 8
between 168 and 543 each); ordering, 151; loss conditions, 240; the
failure-mode pass, 993; open questions, 589; the change section, 808.

**FC-11 (the document is two registrations and a method file in one text).
Minor. ARGUED.** Question 8 itself proposes the split: the table plus
entries 1 and 2 first, entries 3 to 8 with the construction line later.
The text should follow its own proposal. Without loss: (1) entries 3 to 8
(about 1,900 words) become a second document or an appendix titled "the
construction-line entries, not registered here", with the table's
conditional rows pointing to it; (2) the eighteen-row count table moves to
an appendix with only the TOTAL and the three summary lines kept in entry
1, since the committed output file is the record; (3) the both-ends table
and the failure-mode pass are what the protocol requires in the text and
stay, but the change section (808 words) is a change log and belongs in
the commit message and a short dated note, not in registration text; (4)
entry 1 at 2,435 words is a method file inside a registration and would
read better as the method file the entry says will be committed first, with
the registration keeping the indicator, the arms in one sentence each, the
readings, the gates and the cost. Done, the first registration is about
4,500 words, which a Gate A reviewer can hold in one sitting.

**FC-12 (arm B's framing is not stated). Minor. ARGUED.** Arm S says "Same
system framing as the cell it replaces"; arm B and arm S2 do not say which
framing they run under. The routes paragraph's rule ("every entry runs with
the registered framing or none") implies the cell's framing; say it in the
arm.

**FC-13 (what the draft does well, recorded so the next pass can see it).
Not a finding.** Every one of the first check's twenty-three findings is
applied where it bites, and the applications are faithful to what was
asked; the two scripts reproduce byte for byte and every measured figure in
the text is in their output; the template-integrity paragraph says plainly
what its checks cannot show; the both-ends table is honest about being
argued; question 8 is written exactly as the first check and the revised
ruling asked. The draft is behind the record in one place (rulings 9 to
11) and ahead of its own argument in one place (entry 7), and the rest of
what this check found is the consequence of taking the first check's
suggestions literally where they needed one more step.

---

## 5. Plain language

```
$ grep -c '—' docs/filtered-battery-proposal-2026-10-07.md
0
$ grep -c '–' docs/filtered-battery-proposal-2026-10-07.md
0
```

No em-dash and no en-dash in the draft. (Both committed scripts hold the
em-dash once, inside the registered probe quoted verbatim from
`framings.py` line 22, which is registered text and stays as written.)

Every backticked `RT-` and `FB-` identifier in the draft was listed with
seventy characters of left context (`grep -n -o -E ".{0,70}\`(RT|FB)-[0-9]+\`"`,
96 occurrences). Every one inside the table and the prose carries a phrase
("the control-design finding", "the state-carrying finding", and so on),
including the change section's bullets, which each open with the id and
follow it with the finding's name in brackets. Two bare ids remain (the
bare-id finding FC-3):

- line 293, inside the quoted script output: "(so check 2 passes by
  construction; see FB-14)". The phrase is missing in the script's print
  statement, so it is missing in the committed output and the draft.
- lines 26 and 27, inside a quoted commit title: "Gate C tier 1 review of
  the two-sided question proposal: RT-256 to RT-273". A quotation, allowed
  as written; "(the Gate C review's eighteen findings)" after it would
  close the gap.

Terms of art are given their plain meaning where first used (lost, masked,
capitulated; re-derivation; lookup; the construction line). One borrowed
word is used without translation: "ablation strength" in entry 5 ("a noise
or ablation strength applied to the weights"); "a noise strength, or how
much of the weights is removed" says it plainly.

---

## 6. Close

### Must-fix before Gate A (the first registration: the table and entries 1 and 2)

1. **FC-4.** Mark question 1 as answered by ruling 9 and remove it from the
   open list; add ruling 11's terms (method committed before the run, spend
   recorded in the worklog, nothing rented) to entry 2 with the ruling
   cited. The draft is behind the record it will be registered against.
2. **FC-5.** Entry 7's commitment version cannot separate an encounter from
   its text: name a channel in the lived arm that no trained-on token
   carries (the reset of entry 6 is one), match the described arm on the
   system's own transcript, and move rows 7 to 11's condition onto the
   version that has that channel; or label the commitment version as
   reading the distribution gap only. The five conditional rows are in the
   first registration's table, so this cannot wait for the second.
3. **FC-6.** Either add arm B2 (task plus the registered probe, 107 cells,
   about a dollar) so the registered probe's own effect is measured and
   the pressure-trace reading is attributable, or rename the reading as the
   context sentence and probe wording together and strike "what arm B
   measures beyond that is the probe's own effect".
4. **FC-7.** State that lookup cannot fire without pressure trace given
   r_B near 1.0 and r_F 0.905; name the reading for r_S above r_F
   (consistency with the model's own last turn); and either move the band
   off the record's expected result or pre-state that no verdict is the
   expected outcome.
5. **FC-8.** Make the table's KEEP rule and section 0 state the second
   discriminating principle (a report read against an internal state set
   by a known intervention), or restrict entry 8 to constructed systems.
   As written, the rule excludes row 4.

**Counts.** Twelve findings and one note: 0 fatal, 5 serious (the stale
question FC-4, entry 7's missing channel FC-5, arm B's probe FC-6, the
readings FC-7, the rule that excludes row 4 FC-8), 7 minor (the miscount
FC-1, the paraphrased output FC-2, the bare ids FC-3, the loss conditions
FC-9, the sweeps FC-10, the length FC-11, arm B's framing FC-12). MEASURED:
the miscount, the paraphrased output, the bare ids, and the commit-order
half of the stale question; the rest ARGUED. The decisive measured check: both committed scripts re-run with the
repository's Python and compared to their committed outputs with `diff`
and `cmp`, identical byte for byte (section 2); every figure in the draft's
measured blocks is in those outputs (section 2.1). The eight must-fix items
of the first check are each applied where the finding bit (section 3).

### For John, in one paragraph

The numbers are now solid: the two scripts the author committed regenerate
every figure in the draft exactly, I ran them myself and they match to the
byte, and every one of the first check's twenty-three findings has been
applied faithfully. Two things need doing before this goes to Gate A, and
neither costs money. First, the draft was finished eight minutes after you
ruled on its first open question, so it still asks you that question;
it should record your answer instead, and the second entry should carry
the terms you authorised it on. Second, the fix for the biggest problem the
first check found (that these small systems carry their history by training
on it, which the table calls a cheap trick) was to make five rows depend on
a test of lived experience against a written description of it; but as that
test is written, both arms are just training on text, so it either comes
out equal by construction or differs for reasons that have nothing to do
with having lived anything. The test needs one thing in the lived arm that
is not text, and the draft already has one in its stakes entry (a reset
that really happens to the system). The first control on experiment D has
two smaller design points: its baseline arm uses a different question from
the summary arm, so the two cannot be compared as cleanly as the reading
claims (a fifth arm costing about a dollar fixes it), and given what the
record already shows, the most likely result of the control as written is
"no verdict", which should be said in advance rather than discovered. **Is
the draft ready for a measurement rehearsal of its first two entries?
Yes, with those two design points folded into the method file as it is
written**: the pipeline, the template, the cells and the costs are all
pinned down and reproduce, the rehearsal is where the bands get computed
anyway, and nothing in the construction-line findings touches entries 1
and 2. It is not ready to be registered until the five items above are
applied and checked.

### What this session did not do

It did not open any chat, did not read the book or its summary, did not
read the poll synthesis or any reply file, did not read the Gate C review
or either version of the proposal, did not re-run the first check's checks
except where the committed scripts now cover them, did not re-run any
model, called no vendor, rented nothing, trained nothing, spent nothing,
and edited no file that existed before it began.
