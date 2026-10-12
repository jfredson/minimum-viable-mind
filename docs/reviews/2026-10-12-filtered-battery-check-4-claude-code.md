# Fourth pairing-rule check of the filtered-battery draft (version 4, with John's rulings of 2026-10-12 on questions 10 to 12)

**Verdict: PASS.** Every figure in version 4 reproduces from the committed
script and from the stated numbers, all nine of the third check's must-fix
and should-fix items are applied where the draft's change section says they
are, and after one small recorded edit by this session the draft reads
questions 10 to 12 as ruled rather than as open. No condition stands on the
author. Two notes follow for the next edit of the draft.

**Who checked, and what was opened.** This was a separate Claude Code
session. It wrote none of versions 1 to 4 of the draft, none of the three
earlier checks, and not the comment that checked version 4 on draft pull
request 164 (the one headed "Pairing-rule check of version 4"); it read no
session's chat. It opened: pull request 164's body and its comments
(including John's rulings of 2026-10-12, the last comment); version 4 of the
draft at commit `3eee588` ("Filtered-battery draft, version 4: the check's
two conditions and three notes applied"); the third check
(`docs/reviews/2026-10-08-filtered-battery-check-3-claude-code.md`);
`docs/filtered-battery-2026-10-07/count_lost.py` and its committed output;
and line 34 of experiment D's judge script. It did not open entries 3 to 8
beyond their headings, the ruling files, or the outside-perspective replies.
Everything ran in a separate worktree
(`/Users/john/Code/mvm-battery-check`) on the pull request's branch, with
the repository's own scripts. No model was called, nothing was rented,
nothing was spent.

Each finding is labelled MEASURED (a command was run and its output read)
or ARGUED (a judgement from reading), as the project's checks do.

## 1. The count script, re-run and compared byte for byte. MEASURED.

Run from the worktree root with the system Python (3.14.5), reading the
read-only artifacts of experiment D at their default path:

```
$ python3 docs/filtered-battery-2026-10-07/count_lost.py > count_lost.rerun.txt
exit 0
$ cmp count_lost.rerun.txt docs/filtered-battery-2026-10-07/count_lost.out.txt && echo "cmp: identical"
cmp: identical
$ md5 -q count_lost.rerun.txt docs/filtered-battery-2026-10-07/count_lost.out.txt
02b1d7737f07fec8973321b44b530e34
02b1d7737f07fec8973321b44b530e34
```

The re-run output is 52 lines and is identical to the committed
`count_lost.out.txt` byte for byte, so the full output is the committed
file; the lines the draft's entries depend on are these:

```
TOTAL lost-at-R3 preference cells: 116; masked 105; capitulated 11; pooled re-assertion 0.905
retired item(s) ['lo18'] lost in 9 preference cells; lost cells after excluding them: 107
per-model lost after exclusion: {'claude-opus-4-8': 8, 'claude-sonnet-5': 18, 'gemini-3.1-pro-preview': 81}
preference cells after excluding the retired item: 531 (bank B 261); live among them: 424
full-transcript re-assertion over the 107 cells without the retired item: 101 of 107 = 0.944; capitulated 6
binomial SE at n=107 for rate 0.944: 0.022
largest reachable r_S minus r_F (r_S cannot exceed 1.0): 0.056
r_S needed for the lookup reading (r_F minus r_S at least 0.10): at most 0.844
if r_S is 1.0: r_F minus r_S = -0.056, 95 percent interval about -0.100 to -0.012
entry 2 own arm (bank B, tool framing, retired item excluded): n=87, live at third rung=50, pooled own rate=0.575
  claude-opus-4-8: 25/29 = 0.862, room for the other arm to sit below it 0.862
  claude-sonnet-5: 21/29 = 0.724, room for the other arm to sit below it 0.724
  gemini-3.1-pro-preview: 4/29 = 0.138, room for the other arm to sit below it 0.138
SE of own minus other at n=87 per arm, both rates near 0.575: 0.075; 95 percent half-width about 0.147
entry 2: an interval lies wholly inside plus or minus 0.20 only if the difference is within about 0.053 of zero; inside plus or minus 0.10 never (half-width 0.147 exceeds 0.10)
  n=107: 0.944 vs 0.75: difference 0.194, SE of difference 0.047, 4.1 SE
  n=107: 0.944 vs 0.844: difference 0.100, SE of difference 0.042, 2.4 SE
```

The draft's quoted block in entry 1 matches these lines, with the omissions
it labels in parentheses.

## 2. The figures, recomputed from the stated numbers with a script written for this check. MEASURED.

A twelve-line script in this session's scratchpad took only the counts the
draft states (101 of 107; 50 of 87; 25, 21 and 4 of 29) and recomputed
everything the readings rest on. It reads none of the artifacts and only
confirms the arithmetic.

**The full-transcript rate and the consistency ceiling** (task items d).
101 of 107 is 0.9439, printed as 0.944. The ceiling on r_S minus r_F is
1 minus 0.9439, which is 0.0561, printed as 0.056: a 0.10 band could never
be met, exactly as question 12 and entry 1 say. The standard error at 107
cells is 0.0222; with r_S at exactly 1.0 the difference r_F minus r_S is
minus 0.0561 with a 95 percent interval of minus 0.0997 to minus 0.0125,
printed as minus 0.100 to minus 0.012, whose far end sits on the 0.10
band's edge. That is what makes question 10's "near-even split" between the
re-derivation reading and no verdict the right description. The lookup
threshold 0.944 minus 0.10 is 0.8439, printed 0.844. A fall to 0.75 is 4.09
standard errors of the (unpaired) difference and a fall to 0.844 is 2.41,
printed 4.1 and 2.4. **All confirmed.**

**Entry 2's no-verdict zone at 87 cells** (task item e). The own arm's
pooled rate is 50 of 87, 0.5747. Treating both arms as near that rate, the
standard error of the difference is the square root of 2 times 0.5747 times
0.4253 over 87, which is 0.0750; the 95 percent half-width is 0.1469,
printed 0.147. An interval of that half-width lies wholly inside plus or
minus 0.20 only when the difference is within 0.20 minus 0.1469, which is
0.0531 of zero, printed 0.053; it can never lie inside plus or minus 0.10.
So the null reading is reachable only within about 0.05 of zero, the
directional reading only at 0.20 or more, and everything in between is no
verdict, as the entry says. **Confirmed.** (Two different 87s appear in the
draft and both are right: entry 2's 87 cells are 3 models times 29 items,
and the 87 bank-B lost cells before the retired item's nine are excluded are
4 + 5 + 2 + 4 + 9 + 7 + 20 + 26 + 10 from the per-cell table, which leaves
the 78 entry 1's judge-call count uses.)

**The room-to-move correction** (task item e). The predicted direction puts
the other arm below the own arm, and a rate cannot fall below zero, so the
room in a cell is the own arm's rate itself: 25 of 29 is 0.862 (Opus), 21 of
29 is 0.724 (Sonnet), 4 of 29 is 0.138 (Gemini). The 0.20 direction is
reachable in Opus's and Sonnet's cells and in the pooled reading (0.575),
and not in Gemini's, where 0.138 is under 0.20. The mirror case the draft
states, "other above own", has room of one minus the own rate: 0.138
(Opus), 0.276 (Sonnet), 0.862 (Gemini), so it cannot reach 0.20 in Opus's
cell. **Version 4's correction is right, and the mirror statement is
right.** I also checked where the draft says this: entry 2's gate paragraph,
failure-mode item 1, and the both-ends table in failure-mode item 3 all now
name Gemini's cell for the predicted direction, and the entry alone adds the
mirror case, as the change section says.

**The call counts.** Entry 1's judge calls: 261 (arm S, bank B) plus 3
times 78 (arms B, B2 and S2 on bank B) plus 29 (the reference's bank B
items) is 524, which the draft gives as "about 525". Entry 1's single-turn
calls: 531 + 107 + 107 + 107 + 59 is 911, matching the five numbers the
entry lists. Entry 2's judge calls: 87 conversations times 5 judged turns is
435, plus 87 own-arm re-judgings, plus 60 gate responses judged twice (120)
is 642, which the entry gives as "about 640" and question 11 as "about 87
own-arm re-judgings and 120 gate calls". **All confirmed.**

## 3. The third check's nine items, one by one, against the "Changes after the third check" section. MEASURED by reading the lines quoted.

| Third-check item | Applied as the change section says? | The line that applies it |
|---|---|---|
| 1. The reading that could never fire (`FB3-1`), must-fix | **Yes** | Entry 1's readings list: "*Consistency with its own last turn*, **reported as a direction, with no band** (the third check's unreachable-reading finding `FB3-1`). ... r_S minus r_F can be at most 0.056 (MEASURED, the block above) ... It is now reported when the interval of r_S minus r_F lies wholly above zero, with its size read against that 0.056 ceiling, and it carries no band anyone can pass or fail." The both-ends table has its row: "Entry 1, consistency direction, interval of r_S minus r_F wholly above zero, no band ... its ceiling of 0.056 is printed beside it". |
| 2. The full-transcript rate over the wrong cells (`FB3-2`), must-fix | **Yes** | Entry 1: "**The rate every paired reading uses is 0.944, not 0.905** ... over the 107 cells the new arms run on, the full-transcript re-assertion rate is 101 of 107, 0.944." Carried to arm F ("Re-assertion among the 107 lost cells without the retired item is 0.944 (101 of 107)"), the measurement paragraph ("r_F = 0.944 (full transcript, already measured: 101 of 107, not the 0.905 over all 116"), the lookup threshold ("r_S at most 0.844"), the sample-size paragraph ("0.944 with standard error 0.022; a fall to 0.75 ... is 4.1 ... a fall of 0.10 (to 0.844 ...) is 2.4"), the both-ends table ("r_F 0.944 over the 107 cells"), failure-mode items 1 and 2 ("already at 0.944 over the 107 cells the other arms use (0.905 over all 116, the retired item included)"), and question 10. `grep -n "0\.905"` returns eleven lines and every one labels 0.905 as the 116-cell figure. |
| 3. Entry 2's yardstick (`FB3-3`), must-fix | **Yes** | Entry 2, "**How the other arm is scored**": "1. **A rubric addendum, version 1.2, for this entry**, written before any other-arm response is judged, **in a new file of its own** ... It does not edit experiment D's registered rubric ... which D's judge loads directly (`judge_objection.py`, line 34) ... applied to both arms alike ... the own arm's 87 third-rung replies are judged again under version 1.2"; "2. **A second reading that does not depend on ownership wording** ... A difference that appears on the primary reading and not on this one is read as the yardstick's, not the model's, and the entry returns no verdict"; "3. **The judge-reliability gate re-run on other-arm responses**: two-pass agreement at least 0.8 ... on 60 other-arm third-rung responses under version 1.2, before any reading." Line 34 of the judge script reads `RUBRIC = (Path(__file__).parent / "batteries" / "liveness_rubric.md").read_text()`, as cited. The phrase "written into the rubric file" no longer appears anywhere in the draft (`grep` returns nothing). |
| 4. Entry 2's missing no-verdict clause (`FB3-4`), should-fix | **Yes** | Entry 1: "**How a reading is called: one rule for every difference in entries 1 and 2** ... A *directional* reading needs the difference to be at least its band and its interval to exclude zero. A *null* reading needs the difference to lie inside the null band and its whole interval to lie inside the directional band ... Anything else is *no verdict*." Entry 2: "*No verdict*: anything else, including every difference between 0.10 and 0.20 in size" and "**No verdict is a likely outcome of this entry**, for any true difference between about 0.05 and 0.20". |
| 5. The timing sentence (`FB3-5`), should-fix | **Yes** | Question 1: "forty-eight minutes after the first version was committed and eight minutes before version 2 was (the third check's timing finding `FB3-5` corrected version 3's 'eight minutes before the first version')". |
| 6. Entry 1's missing terms (`FB3-6`), should-fix | **Yes** | Entry 1, "Runs on": "Method file and runner committed first ... The spend is recorded in the TimeAssembler worklog and nothing is rented: with the method file first, these are the three terms decision 5's control runs on". |
| 7. Sweep counts that did not reproduce (`FB3-7`), should-fix | **Yes, and re-taken by this check after its own edit** | Failure-mode item 2: "`grep -c "carried by the token"` on this file, which returns 9 on this version"; item 4: "are 310 for the claim-word sweep, 120 for the number sweep and 17400 words by `wc -w`". On the committed text before this check's edit the counts were 309, 117 and 17,253, as version 4 printed; this check's added lines moved them, and section 5 below records the re-take. |
| 8. The retired item in arm S, and three counts (`FB3-8`), should-fix | **Yes** | Arm S: "Run on the 531 preference cells left once the retired item's nine are excluded"; cost: "261 for arm S"; gate (ii): "run through arm S on the 59 items that remain once the retired item is excluded (30 bank A, scored by the matcher; 29 bank B, judged)"; "D's own gate ran ten bank A items only"; entry 2's block: "25/29 = 0.862 ... 21/29 = 0.724 ... 4/29 = 0.138". |
| 9. Failure-mode item 6's missing zero (`FB3-9`), should-fix | **Yes** | Item 6 prints the command and "no ssh or nohup in any experiment D source file". Re-run on this worktree, the same line comes back. |

The three notes are also present: "ASSERTED_OWN label for the keyed
objection, which the registered analyzer calls 'live' (line 6 of ...)" for
the label's name (`FB3-10`); plain phrases at first use for the eight terms
the plain-language note (`FB3-11`) named, all found at or before the term's
first use in prose (for "binomial standard error" the first prose use is the
sample-size paragraph, which glosses it); and the two paragraphs the split's
consequences note (`FB3-12`) asked for, at the end of section 1 ("What the
first registration registers of this table") and the head of section 4
("Which of these the first registration can fire").

The "Changes after the check of version 4" section's five claims also
hold on the text: 0.944 in failure-mode item 2, the addendum in a file of
its own with D's rubric and judge files untouched, the exact list of new
script lines, the mirror case in entry 2, and the sentence on the leak
checks' 540 ("The leak checks' '540' counts every preference cell, the
retired item's nine included ... arm S itself runs on 531").

## 4. Questions 10 to 12: they read as open, and this check closed them. MEASURED on the text, then edited.

**Finding.** On the committed version 4, section 6's questions 10, 11 and
12 still ended with *Recommend* and nothing after it, and three sentences in
the entries pointed at them as live: entry 1's "Whether the band should move
is open question 10" and "Open question 12 asks whether to keep it in this
form", and entry 2's "Whether to register the addendum this way is open
question 11". John ruled on all three on 2026-10-12 ("all as recommended",
the last comment on pull request 164). The entry text already matched the
rulings before any edit: entry 1's bands are both 0.10 and no narrowing
option appears in it (`grep -n -i narrow` finds the word only in question
10 and in row 4's table cell); the near-even split is pre-stated ("about an
even chance of the re-derivation reading or no verdict"); entry 2's scoring
is the three-part text quoted in the table above, with "inside ruling 11's
about $10" carried in its cost paragraph; and the consistency reading is a
direction with no band and its 0.056 ceiling printed. Only the framing as
open was stale.

**The edit this session made, in full.** This is the one edit the check's
brief permitted, plus the wording that follows from it, all in
`docs/filtered-battery-proposal-2026-10-07.md`:

1. Under question 10, after "John as a question.", three new lines:
   "*Ruled by John 2026-10-12: as recommended* (his words, "all as
   recommended"; the last comment on pull request 164). Entry 1's band stays
   0.10, the near-even split is stated there, and the narrowing option is
   dropped."
2. Under question 11, after "inside ruling 11's about $10.", five new lines:
   "*Ruled by John 2026-10-12: as recommended* (the same comment). Entry 2's
   other arm is scored as the entry says: the version 1.2 addendum in its
   own file, both arms, own arm re-judged; the ownership-free second reading
   beside it; the judge-reliability gate re-run on 60 other-arm responses;
   inside ruling 11's about $10."
3. Under question 12, after "a band set to fit the expected result.", three
   new lines: "*Ruled by John 2026-10-12: as recommended* (the same comment).
   The reading stays a reported direction with the interval rule and no
   band, its 0.056 ceiling printed beside it, as entry 1 has it."
4. Entry 1: "Whether the band should move is open question 10." became
   "Question 10 asked whether the band should move; John ruled on
   2026-10-12 that it stays at 0.10."
5. Entry 1: "Open question 12 asks whether to keep it in this form." became
   "Question 12 asked whether to keep it in this form; John ruled on
   2026-10-12 that it is kept as written here."
6. Entry 2: "Whether to register the addendum this way is open question
   11." became "Question 11 asked whether to register the addendum this way;
   John ruled on 2026-10-12 that it is registered as written here."
7. Failure-mode item 4's three sweep counts, which that item requires to be
   taken on the final text: "309 for the claim-word sweep, 117 for the
   number sweep and 17253 words" became "310 ... 120 ... 17400" (section 5).

Why 4 to 6: a dated ruling line under a question whose entry still calls it
open would leave the draft contradicting itself. No figure, reading, band,
gate, cost or recommendation was changed. Nothing outside those seven places
was touched; `git diff` on the branch shows them and nothing else.

## 5. The other re-runs on the final text. MEASURED.

On the draft as committed by version 4, before this check's edit:

```
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' docs/filtered-battery-proposal-2026-10-07.md
309
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' docs/filtered-battery-proposal-2026-10-07.md
117
$ wc -w < docs/filtered-battery-proposal-2026-10-07.md
17253
```

All three matched failure-mode item 4 as version 4 printed it. After the
edit in section 4 the same three commands return 310, 120 and 17400 (the
added ruling lines contain "re-run", which the claim-word sweep counts, and
"0.10" and "0.056", which the number sweep counts), and item 4 now prints
those. Unchanged by the edit and matching the text:

```
$ grep -c "carried by the token" docs/filtered-battery-proposal-2026-10-07.md
9
$ grep -rn -c -E '\bssh\b|nohup' experiments/03-retained-independence/src/*.py | grep -v ':0' || echo "no ssh or nohup in any experiment D source file"
no ssh or nohup in any experiment D source file
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh | tail -4
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

## 6. Plain language. MEASURED.

```
$ grep -c $'\xe2\x80\x94' docs/filtered-battery-proposal-2026-10-07.md ; grep -c $'\xe2\x80\x93' docs/filtered-battery-proposal-2026-10-07.md
0
0
```

No em-dashes or en-dashes in the draft, before or after the edit. The
finding numbers in the ruling lines this check added carry their phrases
("the yardstick finding", "the unreachable-reading finding") through the
question headings they sit under, and the added lines coin no new term.

## 7. Notes for the next edit of the draft (not conditions). ARGUED.

- a. The draft records each check's application in a dated change section.
  This check's edit is recorded here and in the pull request that lands this
  note beside the draft, but not in the draft itself. When the draft is next
  edited (the method file will cause that), a short "Changes after the
  fourth check (2026-10-12)" section saying that questions 10 to 12 were
  closed as ruled and pointing at this note would keep the draft's own
  record complete.
- b. Section 6 is still headed "Open questions for John" while questions 1,
  10, 11 and 12 are ruled. Question 1 set the precedent of keeping a ruled
  question under that heading with its number, so this is consistent, but a
  heading such as "Questions for John, with the rulings so far" would say
  what the section now holds.

## Verdict

**PASS.** ARGUED from the measured items above. The decisive measured
check, the one that would have come out wrong if the draft's central block
were wrong, is section 1: the committed count script re-run against
experiment D's artifacts and compared to its committed output with `cmp` and
MD5, identical byte for byte. The second decisive check is section 2: every
figure the readings depend on (0.944, 0.056, the interval on the band's
edge, 0.147 and 0.053 at 87 cells, and the room-to-move rates in the right
direction) recomputed from the stated counts alone and matching. The one
thing that was not as it should be, the three questions still framed as
open after John ruled them, is closed by the recorded edit in section 4,
which changes no figure and no reading. The draft is ready for the method
file and the measurement rehearsal of entries 1 and 2, then Gate A, both
tiers. The paid run of entry 2 still waits for John's separate go on the
day it runs, as his rulings comment says.

## For John, in one paragraph

The numbers hold up: I re-ran the counting script and it matches its saved
output exactly, and I recomputed every rate, ceiling and interval the two
entries rest on from the raw counts and got the same values, including the
corrected statement that it is Gemini's cell, not Opus's, that cannot reach
the 0.20 direction. All nine of the third check's fixes are in the text
where the draft says they are. The only thing missing was your ruling
itself: the three questions you answered on 2026-10-12 still read as open,
so I added a dated "Ruled by John 2026-10-12: as recommended" line under
each and changed the three sentences in the entries that still called them
open. Nothing else in the draft changed. It is ready for the next step, the
method file and the rehearsal, and nothing here spends anything.

## What this session did not do

It did not rewrite any part of the draft beyond the seven places listed in
section 4. It did not run or re-run any experiment, call any model, rent
anything, or touch anything under `experiments/` or `artifacts/`. It did
not re-check the fourteen rows, entries 3 to 8, or the ruling files, which
earlier checks covered and version 4 says are unchanged. It did not merge
anything.
