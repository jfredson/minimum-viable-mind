# Check of the proposed dispositions for the inside review of successor proposal version 4 (pull request 95), and of the two measurements behind them

*Written 2026-10-04 (Pacific) by a Claude Code checking session, in its own git
worktree, on branch `check-gate-a-v4-dispositions`, cut from
`origin/gate-a-v4-dispositions` at `4fec1a5` (pull request 95, "PROPOSED
dispositions for the inside review of proposal version 4 (RT-237 to
RT-246)"). This is a paired check under "The pairing rule" of
`docs/outside-review-protocol.md`. It wrote none of version 4, the inside
review (pull request 94), the two measurements or the two PROPOSAL documents,
and has no chat history. Laptop only, on the processor. Nothing was trained,
rented or spent: $0. Version 4, the review, the rulings, the ledger and the
author's files were not edited.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run; the script and its output are in the folder
beside this file) or **ARGUED** (reasoning a reader can dispute).*

## What this session opened

**Read in full:** the method and the output of the two measurements
(`docs/2026-10-04-gate-a-v4-dispositions-measurements-method.md`,
`docs/2026-10-04-gate-a-v4-dispositions-measurements.md`); both PROPOSAL
documents (`docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`,
the detail; `docs/rulings/2026-10-04-successor-v4-gate-a-questions-PROPOSAL.md`,
the six-page packet for John); both of the author's scripts
(`lesion_content_check.py`, `width_fit_pool_standin.py`: read, never
imported); the review's `width_vs_count.py`.

**Read in part:** version 4 (every passage a proposed change replaces, and
sections 4.1, 5.4, 6.4 and 8.2 around them); the review's RT-237, RT-242 and
RT-243 and its committed outputs (`rule_from_text`, `floor_forms`,
`solver_sentence`, `older_figures`, `registered_shape_timing`); the
rehearsal's `grammar.py` (header, rendering, self-test), `training.py`,
`repairs.build_for` and `floor_check`; ruling 2 and ruling 7 of
`docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`; page 1h of
`docs/rulings/2026-09-26-weekend-1-queue.md` (by search); the label-search
findings table (`docs/2026-09-26-free-arm-label-search.md`, section 4); earlier
check files for their form.

**Not opened:** the outside review packet, `STATUS.md`, the site, any chat.

**Scripts and outputs** are in
`reviews/2026-10-04-successor-v4-gate-a-dispositions-check-scripts/`. None
imports either of the author's scripts, nor the review's `width_vs_count.py`,
nor `rehearse.py` or `rerun_v3.py`. They use only the rehearsal's shared
generator (`grammar.py`) and model builder (`repairs.build_for`), which the
pull request did not change, and the committed model files.

---

## The answer in five lines

1. **The battery-clause repair (RT-237): the figures hold exactly; the
   search for "batter" does not.** The line comes out at 1,546 from exact
   integer arithmetic, and every count on all 18 models matches the author's
   file (216 of 216 values). But on the proposed registration text a search
   for "batter" finds six lines, not one: the proposal's own new section 4.1
   adds one, and four are already in version 4. The closure check the
   proposal writes would fail on the text the proposal writes.
2. **The width stand-in (RT-240): holds exactly.** 74 → 120 → 156 at 420 / 900
   / 1,800 fitting episodes, 78 and 85 with the stronger penalties, and every
   other figure: 113 of 113 lists equal to the committed file.
3. **Numbers and text changes: every number traces to a committed file, with
   one false sentence and three smaller wording faults.** The proposed new
   weakness under RT-240 says the read "held the label on every toy model"
   at 420 episodes. The free model's did not (its best piece is 34 of 180).
4. **Method before output: holds.** `f13f28d` (method and both scripts, no
   output) is the parent of `b1c0a16` (output). Neither script changed
   afterwards.
5. **The two checker scripts: clean.** 0 confident findings. The only items
   to look at are the same ones the author's commit message lists.

**Verdict.** Fit to go to John after four small text fixes (defects 1 to 4
below). None changes a recommendation. Defect 1 matters most: as written,
the closure check for the fatal finding would report the finding still open
on the corrected text. There is also one point for John's own judgement on
page 1 (section 6): the replacement check is weaker than the proposal says.

---

## 1. Check 1, the battery-clause repair (RT-237)

### 1.1 The line, and the counts, from independent code (MEASURED)

`candidate_counts_independent.py` regenerates the 3,000 gate episodes (1,500
development pairs, generator seed 99). It reads each action turn's item off
the **token sequence** and builds the four candidate answers from the four
assignment turns for that item word. The author built them from the
episode's `values` field. The line is computed with exact fractions
(`math.comb`), not scipy. The script recomputes each model's fingerprint, and
it seeds the untrained models the same way as the method (1000 + seed).

```
line: candidate count >= 1546  (P(X>=1546) = 0.04831; P(X>=1545) = 0.05208)
...
          F/0 off: own {'correct': 528, 'legal': 3000, 'candidate': 2100} ... holds(own) True
          F/1 off: own {'correct': 555, 'legal': 3000, 'candidate': 2238} ... holds(own) True
          F/2 off: own {'correct': 582, 'legal': 3000, 'candidate': 2324} ... holds(own) True
untrained-F/0 off: own {'correct': 0, 'legal': 0, 'candidate': 0} ... holds(own) False
untrained-F/1 off: own {'correct': 157, 'legal': 1262, 'candidate': 620} ... holds(own) False
untrained-F/2 off: own {'correct': 181, 'legal': 1536, 'candidate': 726} ... holds(own) False
author's line 1546, this line 1546
values compared: 216; differing: 0
```

The 216 values are 18 models × channel on and channel zeroed × own-directed
and named-other × correct, legal and candidate counts. **Both ends hold.**
All 15 trained models (arms T, C, M and F, and the competing solver) clear
1,546 with the channel zeroed, on every seed. The lowest is arm F seed 0 at
2,100, 554 above the line. All three untrained models fail. Every figure the
two PROPOSAL documents quote for this measurement matches, including "2,132
to 3,000" for the other trained models and "by 554 episodes or more".

`gate_file_compare.py` also checks the author's claim that the correct counts
equal the committed gate file `out-repairs/gate_base.json` (computed on the
graphics chip). Own-directed and named-other, with the channel on and
zeroed, on all 15 trained models: **0 differ.**

### 1.2 The search for "batter" in the proposed registration text (MEASURED): does not hold

No version 5 exists yet, so `batter_search.py` builds the part of it that
matters here. It applies to version 4 the three proposed changes that add or
remove the word: RT-237 text change 1 (the section 8.2 bullet), RT-237 text
change 3 (the section 9 row) and RT-239's new first paragraph of section 4.1.
The replacement text is lifted from the PROPOSAL file, not retyped. Then it
searches sections 0 to 16, as the proposal's closure check (RT-237, item 1)
says to:

```
proposed text: sections 0 to 16 are lines 93 to 3487; hits for 'batter': 6
  263: primary-battery accuracy on all three trained seeds.* Three things the
  436: query battery, landing at 0.2877, 0.3057 and 0.3195 against 0.3227 for a
  438: battery's own loss term reached 0.3125 and changed nothing
  503: end-of-episode question sets the closed design called batteries; none of
  1793: the reading on exactly the arm the control battery exists to validate, and
  2249: syntax batteries must hold", which was written for the closed design's
```

Line 2249 is the sentence recording the replacement, as intended. Line 503 is
added by the proposal's own RT-239 text. Lines 263, 436 and 438 describe the
closed design's record. Line 1793 is this design's "control battery" (its set
of controls). **None of the six sets a condition**, so the clause itself is
gone. But the closure check as worded ("returns only the sentence recording
the replacement") fails on the proposed text. A reviewer applying it
literally would report the fatal finding still open. Defect 1 below gives the
fix.

The proposal's own table entry C1 says it excluded "the three hits about the
closed design's batteries". There are four such lines in version 4, and the
one at 1769 (1793 after the edits) is not about the closed design. This is a
small inaccuracy and changes nothing.

---

## 2. Check 2, the fitting-episodes repair (RT-240) (MEASURED): holds

`width_standin_independent.py` re-implements the stand-in from its
description. The read's label (the model's own marker word) comes off the
tokens and the acting channel, and the script checks that the action
position it finds agrees with the batch's. It rebuilds the 8-direction piece
with its own singular value decomposition and QR. It loads models with its
own strict load. The noise follows the same recipe as the review's
(generator seed 20261004, scale = median per-coordinate spread), because
otherwise nothing would be comparable.

```
1. review's stand-in, 600 episodes
  C/1 L1 | 177, 172 | [91, 94, 89, 90, 92]; [80, 88, 79, 76, 85]      (= width_vs_count.out.txt)
2-3. pool of 1,980, last 180 held out
  C/1 L1 fit 420 C 1.0:  ... piece [74, 87, 82, 82, 77];      min piece 74
  C/1 L1 fit 900 C 1.0:  ... piece [128, 120, 124, 131, 123]; min piece 120
  C/1 L1 fit 1800 C 1.0: ... piece [156, 162, 162, 160, 160]; min piece 156
  C/1 L1 fit 420 C 0.1:  ... min piece 78
  C/1 L1 fit 420 C 0.01: ... min piece 85
4. width 160, best piece over layers 1-4, fit 420/900/1800
  F/0: best piece [28, 37, 41]   F/1: [18, 20, 19]   F/2: [23, 26, 37]
lists compared with the committed JSON: 113; differing: 0
```

**Every figure the author reports reproduces**: the reproduction of the
review (5 of 5 cases), the sweep, and the toy-width table. This includes the
figures quoted in prose: arm C seed 2 at 129 / 168 / 177 and 140 / 141; the
whole read on arm C seed 1 at 87 to 97, 121 to 134 and 165 to 170; and the
free model's best piece of 41 at most. scikit-learn printed the same 20
warnings that a fit stopped at its iteration limit, as the author recorded.

---

## 3. Check 3, numbers and text changes

### 3.1 Every number traces to a committed file (MEASURED, with one wording fault)

Traced, beyond sections 1 and 2:

- **RT-238:** `need > 0` at `repairs.py` line 276. Version 4 has 0
  occurrences. "Four of its six runs", "0 of 45 site sets" and "two of the
  solver's three seeds at or below zero" all match `rule_from_text.out.txt`,
  section 4.
- **RT-242:** 0.733 / 0.383 / 0.478, and 0.417 and 0.633, recomputed from
  the committed `out-label-search/fit_*_F_seed*.json` over the 45
  action-anchored site sets (`label_search_fixed_extent.py`).
- **RT-243:** 576, 892 and 1,080 (`floor_forms.out.txt`). But see defect 3.
- **RT-244:** 119; 0.1091 to 0.1393; 0.0911 to 0.1213 (`solver_sentence.out.txt`).
- **RT-245:** 4.59 s, about 124.6 minutes, about 24.9 hours and 56 tokens
  (`registered_shape_timing.out.txt`). "One episode in 600, arm C seed 1"
  is in the review, RT-245.
- **The rest:** the C6 re-run of the review's three scripts gives 0 lines
  different in each (`review_scripts_rerun.out.txt`). C7's line numbers (A3
  lines 13, 79, 82; version 4 line 500) and C10's (lines 462 and 2732) are
  right. C8 (`grammar.py --self-test`) prints both quoted PASS lines and "all
  checks passed". The quoted old text for every replacement is in version 4
  at the cited lines. The roadmap's "resting on T alone" is at its line 141,
  in section 3.

**Wording fault (defect 2).** RT-240 text change 2 says the piece "fell to as
low as 74 and 129 of 180 on two seeds". It cites the review's
`width_vs_count.out.txt` and part B. Those two figures come from part B's
pool of 1,980 episodes. The review's own file has 76 and 126.

### 3.2 Each text change against its finding

Each change answers its finding, and the changes to rulings John made are
all flagged as needing his words. **Not found:** a silent change to any
number, bar or gate. Four defects:

**Defect 1, must fix before John relies on RT-237's closure (MEASURED,
section 1.2).** The closure check's "batter" search cannot pass on the
proposed text. *Suggested wording for item 1:* "and `grep -n -i "batter"` over
sections 0 to 16 finds no sentence that sets a condition: the expected hits
are the sentence recording the replacement (section 8.2), the sentence saying
the closed design's batteries are not carried (section 4.1), the two
passages describing the closed design's record (sections 1 and 3) and the
phrase 'the control battery' (section 7.3)". The alternative is to reword
those passages so that the word appears only once.

**Defect 2, must fix: a false sentence in proposed registration text
(ARGUED from the committed record).** RT-240 text change 2, the new section
13 weakness, says: "Fitted on 420 episodes, the read held the label on every
toy model". The free model's read did not: it "failed its floor" on every
seed (best piece 34 of 180 on the committed record; 28 / 18 / 23 on part B's
pool). *Fix:* "on every constructed toy model (arms T, C and M)". Also give
74 and 129 as part B's figures, with the review's 76 and 126 beside them
(section 3.1).

**Defect 3, should fix: RT-243's replacement says more than the record
(MEASURED, `floor_forms_direction.py`).** The proposed sentence says the two
forms disagree "always the same way: the plain form passes a model near
chance and the registered form refuses it". The direction is right in all
2,549 disagreements: the plain form passes and the registered form refuses.
"A model near chance" is wrong for five of them, which are on the grammar
attempt's free model with the own-directed condition learned. Four are rows
of its own-directed site-set grid (`out-grammar-c/nominate_base_F_T_C.json`,
arm F seed 1), with room 0.3967 against a required 0.4027. One is a reading in
`out-grammar-c/outcomes.json`, which the sentence does not count, with room
0.3925 against 0.403. The review's RT-243 text has the same overstatement.
*Fix:* "always the same way, the plain form passing where the registered
form refuses: on models near chance in the other-agent grids and on the
competing solver, and on five rows of the grammar attempt's free model, by
0.011 or less".

**Defect 4, should fix: one sentence of RT-239's new section 4.1 conflicts
with section 4.2 (ARGUED).** "Within an item the four values are distinct"
is not true of the collision set for control 6. In that set, two agents
share a value on one item (`grammar.py`'s `collide` option, kept in version
4's section 4.2, line 568; the self-test checks it). *Fix:* add "(except in
the collision set for control 6, section 4.2)".

**Smaller points (ARGUED), for whoever writes version 5:**

- **RT-237 text change 5** puts the requirement that the gate's code record
  the lesioned candidate count under section 6.4 item 5. That item is about
  the reading's controls. Section 8.2, or step 3 of section 11, would be where
  a builder looks for it.
- **RT-241 text change 1** replaces the block "What a no verdict maps to"
  together with its heading. That heading carried the provenance: "ruled
  2026-10-03, page 11; it closes ... RT-182". The new table cites only RT-241.
  The old citation should be kept beside the new one.
- Nothing else changes silently. RT-245's change to the section 9 device row
  and RT-244's rewrite of the last sentence of ruling 2 are both disclosed.

---

## 4. Check 4, method before output (MEASURED): holds

```
f13f28d 2026-10-04T13:05:09-07:00  Method and code ... committed before any output
b1c0a16 2026-10-04T13:11:03-07:00  Output of the two $0 measurements committed at f13f28d ...
4fec1a5 2026-10-04T13:16:34-07:00  PROPOSED dispositions ...
```

`f13f28d` adds only the method file and the two scripts. No output file is in
it. `git diff f13f28d HEAD` over the scripts and the method file is empty, so
neither changed after it was committed. The only change to the output document
after `b1c0a16` is one abridged command line in `4fec1a5`. Git cannot show
when `f13f28d` was pushed. The commit order and the exact reproduction above
are what can be checked.

Against its own advance statements, the output document reports the two
expectations that turned out wrong in size or direction. Candidate counts on
arms C and F were not "near 3,000", and 900 episodes did not "bring most of
them back". It reports both openly.

## 5. Check 5, the two checker scripts (MEASURED): clean

Each of the four new documents was run through `scripts/check_citations.py --only <document>`
(`check_citations.out.txt`). Each has 0 confident findings. One item to
look at, in the dispositions PROPOSAL: "$0" beside
`registered_shape_timing.out.txt`, a statement that nothing was spent, not a
figure from that file. `scripts/check_single_source.py` with all four
documents (`check_single_source.out.txt`) has 0 confident findings. Three
items to look at, each a line saying nothing was spent, "$0". Both results
are exactly what the author's commit message reports.

---

## 6. For John

**Page 1: the replacement check is weaker than the packet says (MEASURED and
ARGUED).** The packet says the new check "refuses a model whose lesion broke
the act". It refuses a model that answers with noise. It cannot tell whether
the lesion broke the step "find the item the action names".
`item_blind_null.py` computes, on the same 3,000 gate episodes, the expected
count for a model that has lost the item and answers the successor of any of
the eight values shown in the episode: **about 2,257 of 3,000**. That is well
above the line (1,546), and above the free model's lowest seed (2,100). On
this task, then, the check shows that the model still answers "the successor
of a value it was shown". It does not show that the model still uses the
right item.

The line could not simply be raised to catch this. A line above 2,257 would
fail arm F on two seeds of three (2,100 and 2,238) and arm C on all three, on
the toy as it stands. Even with the
channel on, arms C and F stay at 2,197 to 2,328. That is already about the
level of an item-blind model, so the toy free model's wrong answers are
themselves nearly item-blind.

None of this overturns the recommendation (a). It is still better than
nothing, and it does fail a model that has collapsed outright. But it moves
the comparison with option (b), striking the clause, closer than "moderate to
high" suggests. If (a) is ruled, the registered sentence should say what the
check does show: "the model still answers with the successor of a value it
was shown". It should not say the check shows the item step survived. The
measurement document's own caveat, that "a lesion that halves a model's
content-tracking would still pass", points the same way.

**Nothing else needs John before the four fixes.** Defects 1 to 4 are wording
for the author or for whoever writes version 5. None changes a
recommendation, a tally or a number John would rule on.

## 7. What this session did not do

It did not rule, edit version 4, the review, the ledger, any ruling file or
either PROPOSAL document, or write version 5. It did not run the toy re-run
that RT-240 asks for, or train anything. It did not check the outside packet
or any outside response (none is filed). It did not merge anything. It did
not spend anything.

---

## Re-check of the fixes at `52f8d54` (2026-10-04, Pacific)

*The same checking session did this, in a new worktree detached at
`origin/gate-a-v4-dispositions` (`52f8d54`). It checked only the changes from
`4fec1a5` to `52f8d54`. Nothing was spent.*

**What changed.** `git diff --stat 4fec1a5 52f8d54` touches only the two
PROPOSAL documents. The measurement documents, scripts and outputs are
untouched. Every changed passage answers an item of this check, or says the
check was done. Nothing else in either document changed.

| Item | Asked for | At `52f8d54` | Verdict |
|---|---|---|---|
| Defect 1, the "batter" search in RT-237's closure check | Test for a condition, not the word; list the expected hits | The check is reworded to "no sentence sets a condition". It lists the six hits and says each is to be read and classified. `batter_search.py`, run again on the revised text, still finds exactly those six (lines 263, 436, 438, 503, 1794, 2250). C1 now counts four other hits. | **holds**, with one location slip noted below |
| Defect 2, the false RT-240 weakness | "every constructed toy model (arms T, C and M)"; the review's 76 and 126 beside part B's 74 and 129 | Both done. The free model's failed read is cited to section 5.4, which records it (best piece 34 of 180). | **holds** |
| Defect 3, RT-243's "near chance" | Keep the direction; say five rows are on the grammar attempt's free model, missed by 0.011 or less | Done, in the replacement text and in the summary table | **holds** (nit below) |
| Defect 4, RT-239's "values distinct" | Add the exception for control 6's collision set | Done, citing section 4.2 | **holds** |
| Smaller point, RT-237 text change 5 | Move it to section 8.2 and step 3 | Moved | **holds** |
| Smaller point, RT-241's provenance | Keep the page 11 / RT-182 citation | Kept in the table's heading, alongside RT-241 | **holds** |
| Page-1 caveat | Say what the check does and does not show; about 2,257; the line can't be raised | It is in RT-237's text change 2, its reason, the C3 and summary-table rows, and page 1 of the packet. Confidence is lowered to moderate, and (b) is named as a close second. The figures (2,257; 2,100; two seeds of arm F, all three of arm C) match section 6. | **holds** |
| Checker scripts on the two revised documents | Run them | `check_citations.py`: 0 confident findings in each document; one item to look at (the same "$0" as before). `check_single_source.py`: 0 confident findings; one item to look at ("$0"). | **holds** |

**Two slips, neither blocking (MEASURED by locating the lines in version 4):**

- **Wrong section, and the slip is mine.** The closure check's list puts the
  closed design's passages in "sections 1 and 3". Line 263 is in section 2,
  so it should read "sections 2 and 3". This came from the wording I
  suggested in defect 1, which made the same error.
- **"Three passages" should be "two".** The revised text says "three
  passages". Lines 436 and 438 are one sentence, so there are two passages
  (three lines).

**Nit on defect 3.** The sentence says "five are on the grammar attempt's free
model". Four of those five are among the 892 rows it counts. The fifth is in
`out-grammar-c/outcomes.json`, which it does not count. The text is accurate
enough, and the next edit could say so.

**Verdict.** All four defects, both smaller points and the page-1 caveat are
fixed as this check asked. Nothing else changed. The dispositions and the
packet are fit to go to John. The two slips can be corrected whenever version
5 is written.
