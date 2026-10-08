# Check of the five rulings on the ledger packet (pull request 144) and the ledger rows for entries 212 to 229 with the RT-274 renumbering (pull request 145)

*Written 2026-10-08 (Pacific, by this machine's clock; the file name follows
the date the two pull requests use) by a Claude Code session that wrote
neither pull request, nor any review, ruling, check or registration text they
cite. Branch `check-ledger-packet-and-rows-212-229`, cut from the main line at
`dafdaf2` (the merge of pull request 143). $0, laptop only: nothing was run
but searches of committed files and the project's citation checker. Nothing
was fixed. Written under the workspace plain-language rule.*

*Targets:*
- *Pull request 144, branch `rulings-ledger-packet-2026-10-09`, one commit
  `e71a5ca`, base main: `docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md`.*
- *Pull request 145, branch `ledger-rows-rt212-229`, four commits (`dd314fc`
  method, `612c11c` rows, `42da518` renumbering, `53e40a8` findings), base
  main, cut from `dafdaf2`.*

*Short names used below: "the source review" is the Gate C review of
successor proposal version 2,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`;
"the version 2 rulings" is `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`;
"the re-run check" is the check of the toy re-run under the version 3 rules,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-toy-rerun-v3-rules-check-claude-worktree.md`;
"version 5" is the registration text `docs/successor-experiment-proposal-2026-10-07-v5.md`;
"the ledger" is `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`.
RT-256 has two meanings on the main line: "the decision-procedure finding"
(outside finding A2, fatal) and "the records-not-on-the-branch finding" (from
the Gate C pass on the refounding proposal); pull request 145 renumbers the
second to RT-274.*

## Verdicts

- **Pull request 144 (the five rulings): ready to merge after one must-fix**,
  the date. Every fact the five questions state is true against the record,
  and authorship is recorded as mixed. The file says it was written
  2026-10-09, but its only commit is dated 2026-10-08 15:22 Pacific.
- **Pull request 145 (the eighteen rows and the renumbering): ready to
  merge**, after or together with pull request 144, with should-fix items
  only. Every row's finding matches the source review and every disposition
  matches the version 2 rulings. The six "checked" rows meet the closure
  rule. The one open row (RT-219, the two entangled shares) is rightly open.
  The renumbering touched only uses of RT-256 that mean the
  records-not-on-the-branch finding. Only the allowed ledger text changed,
  plus one section heading the findings note does not mention. The claim
  about version 5's section 13 is true.

## Must-fix

1. **Pull request 144: the ruling's date.** The file is headed "Rulings
   2026-10-09" and "Written 2026-10-09 (Friday, Pacific)". Its commit is
   `e71a5ca 2026-10-08 15:22:09 -0700`, so it was committed the day before the
   date it gives. A ruling's date is part of what makes it checkable, and
   later records here are ordered by it. Either put the true date in the
   file, or add a dated line saying which clock the 2026-10-09 date comes from
   and that the commit is dated 2026-10-08 Pacific. The second option keeps
   the file name, which pull request 145 cites in about a dozen places, so
   neither pull request has to be re-cut. (Command A.6.)

## Should-fix

Pull request 145:

1. **Say in the findings note that one section heading of the ledger was
   edited.** The heading of the refounding pass's section changed from
   "(RT-256 to RT-273)" to "(RT-257 to RT-274; filed by the pass as RT-256 to
   RT-273)". The change is correct and follows ruling 1. But the findings
   note's "What was written" lists only the renamed row, the count note and
   RT-262's note, and the method says only "the section note". (Command B.5.)
2. **RT-212's row (the empty-read finding, the one fatal finding) should name
   the commits that land the fix.** The protocol's closure rule
   (`docs/outside-review-protocol.md`, "The closure rule") asks that a fatal
   finding's closure line give "the commit that lands the fix" as well as
   the measured check. The row names the two checks (`70be9fb` and
   `ecd2b6c`) but not the fix. The fix is the toy re-run under the version 3
   rules (`9d9d31a`) and version 3 itself. The section's opening note names
   the re-run, but not in the row. The rows from entry 230 on leave this out
   too (the decision-procedure finding's row is the same), so this is
   practice, not a slip special to these rows.
3. **RT-215's row (the site-set rule never run) describes the 36 re-picked
   nominations as "primary, and both layer-0 variants".** The re-run check's
   section 3.3 table has three columns per pair: the first pass (no layer-0
   removal), the second pass (the primary), and the stricter row. "First
   pass, primary and stricter" is what was re-picked. The closure does not
   change.
4. **The version 5 section 13 sentence (RT-228's fix, now out of date) needs
   a named owner before the registration commit.** The findings note names
   it (its point 3) and leaves it to the text's author. Nothing in either
   pull request adds it to a list of work owed before the commit, so it could
   be missed. The same paragraph's last sentence ("step 4 of section 11 is
   where arm M first does") is also out of date, since step 4 has happened.

Pull request 144: none beyond the must-fix.

## A. Pull request 144: the five questions against the record

**A.1 Question 1, the two meanings of RT-256 and where each was assigned.**
True. The decision-procedure finding was assigned first, on 2026-10-06, by
the addendum to the 2026-10-06 rulings. The Gate C pass on the refounding
proposal numbered from RT-256 on 2026-10-07, from a copy that did not yet
hold that addendum:

```
$ git log --format='%h %ad %s' --date=iso -S "RT-256" origin/main -- docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md
c920637 2026-10-07 17:50:53 -0700 Gate C tier 1 review of the two-sided question proposal: RT-256 to RT-273
380612a 2026-10-06 10:09:51 -0700 Addendum: John accepts the decision-procedure finding (A2, RT-256), "yes, remove"; ...
$ git show -s --format='%h %ad %P' --date=iso c920637
c920637 2026-10-07 17:50:53 -0700 aef720d7405801721600e37b679eee499b83803f
$ git merge-base --is-ancestor 380612a aef720d && echo "parent HAS 10-06 assignment" || echo "parent LACKS 10-06 assignment"
parent LACKS 10-06 assignment
$ git show aef720d:docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md | grep -c "RT-256"
0
```

The 2026-10-06 rulings' table row reads "| RT-256 | A2 (fatal) | The final
decision procedure ... had not run end to end on the rules as ruled".

**A.2 RT-256 cited 9 times in version 5.** True, and all nine mean the
decision-procedure finding (the ranges "RT-247 to RT-256" of adopted outside
findings, and "A2, adopted as RT-256"):

```
$ git grep -o "RT-256" origin/main -- docs/successor-experiment-proposal-2026-10-07-v5.md | wc -l
       9
$ git grep -n "RT-256" origin/main -- docs/successor-experiment-proposal-2026-10-07-v5.md   (lines 84, 86, 92, 1808, 3310, 5014, 5026, 5447, 5610)
```

**A.3 RT-274 is the next free number.** True on the main line and on every
branch on the remote. On the main line the highest number used for a finding
is RT-273. RT-274, RT-299 and RT-399 appear only as the ends of searched
ranges ("RT-274 to RT-299", "RT-230 to RT-399"):

```
$ git grep -ohE "RT-[0-9]{3}" origin/main | sort -u | tail -4
RT-273
RT-274
RT-299
RT-399
$ git grep -nE "RT-(274|299|399)" origin/main
  docs/2026-10-09-ledger-rows-findings.md:31, docs/2026-10-09-ledger-rows-method.md:47-48,
  docs/reviews/2026-10-07-filtered-battery-check.md:23, docs/reviews/2026-10-09-ledger-rows-and-v5-wording-check-claude-code.md:175
  (each a searched range, none a finding)
```

A script (`docs/reviews/2026-10-09-ledger-packet-and-rows-212-229-check-scripts/scan.sh`,
then `scan2.sh` beside it, both committed with this review) ran
`git grep -lE "RT-27[4-9]"` over all 61 remote branches. The only branch with
RT-274 in a file the main line does not have is `ledger-rows-rt212-229` (pull
request 145), plus the rulings file itself. Seven other branches showed only
the four range lines above.

**A.4 Ledger rows RT-212 to RT-229 missing on main; version 5 cites 16 of the
18.** True:

```
$ git show origin/main:experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md | grep -cE "RT-2(1[2-9]|2[0-9])\b"
0
$ grep -ohE "RT-2(1[2-9]|2[0-9])" v5.md | sort -u | tr '\n' ' '
RT-212 RT-213 RT-214 RT-215 RT-216 RT-217 RT-218 RT-219 RT-220 RT-222 RT-223 RT-224 RT-225 RT-226 RT-228 RT-229
$ ... | wc -l
      16
```

The two it does not cite are RT-221 and RT-227.

**A.5 RT-238, RT-239 and RT-251 are serious and closed only as accepted, and
the eight open rows.** True. A small script
(`docs/reviews/2026-10-09-ledger-packet-and-rows-212-229-check-scripts/rows.py`,
which reads the ledger's table rows into fields; `ledger_main.md` and
`ledger_pr.md` are the ledger as `git show` prints it on the main line and on
pull request 145's branch) printed:

```
$ python3 rows.py ledger_main.md RT-238 RT-239 RT-251 OPEN
RT-238 | serious | **Closed: the argument was accepted.** A wording fix bringing the text to what the code al...
RT-239 | serious | **Closed: the argument was accepted.** In version 5, section 4.1; read as carried by the c...
RT-251 | serious | **Closed: the argument was accepted.** A wording fix in version 5 (sections 6.1 and 7.3 it...
open: ['RT-237', 'RT-240', 'RT-247', 'RT-250', 'RT-263', 'RT-267', 'RT-269', 'RT-273']
```

The findings match the packet's descriptions: RT-238 is the floor's missing
condition, RT-239 the episode format, and RT-251 control 6. The eight open
rows match ruling 5's names and its split: four bear on the registration
(the free model's gate, the episode counts, the decoy, the outcome words) and
four on the refounding proposal. RT-262 (the refounding's fatal finding) is
closed as accepted, as ruling 5 says. The protocol's sentence that question 4
paraphrases is real: "Serious findings are closed the same way or carried as
an open item named in the registered text, with John's ruling and reason"
(`docs/outside-review-protocol.md`, the closure rule). Question 5 cites
"item 12 of the 2026-10-08 rulings". That is version 5 item 12 (packet item
10) in `docs/rulings/2026-10-08-v5-open-items-rulings.md`, which asks for each
row to be "closed with 'the claim was checked' or 'the argument was
accepted'". Question 3's premise holds too: items 7 and 9 of those rulings
change the frozen code after the 2026-10-06 decision-code checks.

**A.6 Authorship and date.** The file's header says "Authorship: **mixed**
throughout", and the ruling is quoted as John's two words. Both as asked.
The date:

```
$ git log --format='%h %ad %s' --date=iso origin/main..origin/rulings-ledger-packet-2026-10-09
e71a5ca 2026-10-08 15:22:09 -0700 Record John's five rulings on the ledger and closure-check packet
$ date
Thu Oct  8 15:46:35 PDT 2026
```

This is must-fix 1.

## B. Pull request 145: the rows and the renumbering

**B.1 Commit order.** The method (`dd314fc`, 15:31) came before the rows
(`612c11c`, 15:33), then the renumbering (`42da518`, 15:35), then the
findings (`53e40a8`, 15:37), all on 2026-10-08 Pacific. That is the order the
method requires.

**B.2 Each row's finding against the source review, and its disposition
against the version 2 rulings.** I read all eighteen rows against the source
review's findings table (lines 84 to 101) and against the full sections for
RT-212 to RT-216 and RT-219 (lines 159 to 455). I read every disposition
against the version 2 rulings in full, including the refinements, "RT-212
item 3 resolved", decisions 20 and 21, and the dated notes beside RT-220 and
RT-222. Every row matches. Specific points I checked:

- RT-213 (the anchor's failed gate): 760, 751 and 708 of 3,000 against 790
  are in the review's section (its printout of the toy's gate file). The review's table
  wording "fails ... on 0 of 3" means it passes on none, which the row puts
  as "fails on every toy seed", the same as the section heading.
- RT-216 (nominations at the acting channel's injection): "six of the nine"
  is the review's section wording. The table's "most" is less precise.
- RT-214 (control 3 on arm M): the review gives 0.0563 against 0.0350. The
  row's statement that the repairs rulings
  (`docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`) carry no
  annotation with the checked figures beside item 2 is true. That file's
  annotations 1 and 2 on item 2 are about money, and the only "annotation"
  hit is the section heading at its line 97.
- RT-218 and RT-225 (the two counts of 12, and the rider's cause on arm M):
  the repairs rulings' annotations 3 and 5 are on item 4 and the rider, as
  the rows say.
- RT-220 (the lesion's honest description): the case names
  "F-channel-removal" and "split-one-seed-everything" are in the first
  decision-code check (pull request 107, lines 87, 95 and 133), and "cases
  12, 20" for the channel-removal collapse are in the second (pull request
  113, line 144).
- RT-229 (arm M's development run costed twice): the compute ledger's four
  2026-10-04 development rows each say "widened by RT-229".

**B.3 The closure words against the closure rule.**

*The six "checked" rows, in full.*

- **RT-212 (the empty-read finding, fatal).** The re-run check, section 3.2,
  recomputes fit and floor on all twelve arm-and-seed pairs. It finds arm F
  failing on every seed (best 0.172) and the lowest passing fit on arms T, C
  and M at 0.961, and says in its own words "RT-212 item 1's closing test ...
  is met in the second pass". The check of the free-arm label search
  (`ecd2b6c`, pull request 70) says "No candidate clears on any seed; the
  figures reproduce. MEASURED". Both are by sessions that wrote neither the
  fix nor its runs, and both ran commands with committed output. This meets
  the rule, apart from should-fix 2.
- **RT-213 (the anchor's failed gate).** Re-run check section 3.1 gives the
  gate per arm under the own-directed-only rule (T, C and M pass, F fails on
  named-other 1 of 3). Section 4.5 sets the rule against the ruling, word for
  word. The file `experiments/rehearsal-successor-measure/out-v3-rules/gate.json`
  exists. The wording part is marked as only read. This meets the rule.
- **RT-214 (control 3 on arm M).** Section 3.6 gives the median, 95th
  percentile and below / equal / above counts for all twelve pairs, with
  "Every cell equals the findings' table". Section 3.4 gives arm M at 0.4886,
  0.4860 and 0.5449. Section 4.2 sets the rule against the ruling and
  refinement 1. This meets the rule.
- **RT-215 (the site-set rule never run).** Section 3.3 covers the 300 grid
  entries per pair, the 60-set family, "All 36 picks equal the recorded
  ones", and the floor verdict equal "on all 3,600 grid entries". Section 4.3
  finds no multi-layer nomination. This meets the rule (see should-fix 3 on
  the wording).
- **RT-216 (nominations at the acting channel's injection).** Section 3.3
  re-picks with the removal. Section 3.7 shows the stricter row moving only
  arm T, to layer 1, reading 0.0000. Section 4.4 says "MEASURED, `alt.py`
  ... all twelve second-pass nominations are the same". The rewording of
  weakness W7 is marked as read; it is in version 5 at line 4042 ("six of the
  nine nominations on arms C, F and M sat at the injection"). This meets the
  rule.
- **RT-220 (the lesion's honest description).** The amended rule (page 7 of
  the 2026-10-06 rulings) was recomputed by both decision-code checks, and
  switching the rule off changes their cases (as in B.2). The arm T seed 2
  description is marked as wording. This meets the rule.

*The one open row, in full.*

- **RT-219 (the two entangled shares).** The ruling's owed work is "the
  findings' sentence is corrected at its check". The sentence is unchanged:

  ```
  $ sed -n 328,331p docs/2026-09-26-rehearsal-repairs.md
  through the separable one, about three fifths entangled (0.6033 of the fresh
  episodes, `measure_base_M.json`). ...
  $ git log --oneline -3 -- docs/2026-09-26-rehearsal-repairs.md
  882f252 Rehearsal repairs (Weekend 1 session c): ... (#52)
  ```

  The file has had one commit and no note. The repairs check (`d216dbc`,
  pull request 58) prints "share 0.6038" for arm M in its output (its lines
  826 to 829 and 895 to 898). That is the fresh-trial share, so "prints the
  share" is true, but the check does not correct the sentence. Version 5,
  section 5.3 (lines 1188 to 1191), states both figures correctly. "Open,
  owed work not done" is the method's rule applied correctly.

*The eleven "accepted" rows, sampled (seven of eleven read against version
5).*

- RT-217 (the $16 wager): section 12.8 gives $14.79 and the lowered floor, and
  says version 2's $16 floor "was already lost".
- RT-218 (the two counts of 12): section 7.2, lines 2326 to 2328, reads "8 of
  12 arm-and-seed pairs, and ... differed on 7 of 12".
- RT-221 (separation figures from excluded site sets): lines 1065 and 1066
  say the figures 0.9977 and 0.9927 "were replaced in version 3 and stay
  replaced".
- RT-222 (the 0.0175 allowance): section 6.4, line 1759, gives "rounded up to
  0.018", and the section 9 table, line 3081, gives "at most the largest
  measured miss, rounded up to 0.018; reported, not a veto".
- RT-224 (a position set described backwards): section 7.2, line 2107, reads
  "token just before it" (`action+ans`), and section 18 says the same.
- RT-228 (the launcher, and arm M on the rented machine): section 5, lines 930
  to 945, names both launchers. Section 13's sentence is in B.6.
- RT-229 (arm M's development run costed twice): section 12.4, line 3771,
  says "The $1.94 comes out of this section".

None of these has a measured check of the text, so "the argument was
accepted" is the right word for each. These are all minor findings, and the
closure rule asks a measured check of fatal and serious ones only.

**B.4 The renumbering touched only the records-not-on-the-branch sense.** I
read every RT-256 use in the seven noted files on the main line. Each one
means the Gate C pass's finding or its range "RT-256 to RT-273":

```
$ git grep -n "RT-256" origin/main -- <the seven files>
docs/filtered-battery-proposal-2026-10-07.md:26        quoted commit title "... RT-256 to [RT-273]"
docs/reviews/2026-10-07-filtered-battery-check-2.md:387, 749   the same quoted title
docs/reviews/2026-10-07-proposal-v2-check.md:10, 72, 490, 601  the range; "### RT-256, the records-not-on-the-branch finding"
docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md:24, 130, 343, 840, 886, 903, 920   the pass's own numbering
docs/reviews/2026-10-08-filtered-battery-check-3-claude-code.md:645   the quoted title
docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md:7, 17, 78, 92, 394   the range and the finding
docs/rulings/2026-10-07-two-sided-question-rulings.md:116   the range
```

None of them means the decision-procedure finding. The files that do mean
it were not touched: version 5, the 2026-10-06 rulings (lines 358 and 537),
the registration handoff (lines 24, 40, 95 and 133), the version 5 check
(line 432) and `data/roadmap.toml`. The diff to those seven files is one
five-line dated note in each, under the title, and nothing else:

```
$ git diff origin/main origin/ledger-rows-rt212-229 -- <the seven files> | grep -E "^[-+@]"
(seven hunks "@@ -1,5 +1,10 @@", each adding the same four-line note and a blank line; no "-" lines)
```

In the ledger after the change, RT-256 is used only for the
decision-procedure finding, or when describing the old number of the
renamed row:

```
$ grep -n "RT-256" ledger_pr.md
1017 (the range RT-247 to RT-256), 1041 (the decision-procedure row), 1043, 1047, 1049, 1052, 1058, 1098, 1109-1111 (notes saying what was renumbered)
```

`STATUS.md` line 259 still reads "RT-256 to RT-273" for the Gate C pass with
no note. The findings note (point 6) says this was left on purpose and
offers a one-line note for John to accept or decline. I agree it is John's
call.

**B.5 No other ledger row was edited.**

```
$ git diff -U0 origin/main origin/ledger-rows-rt212-229 -- .../red_team_ledger.md | grep "^@@"
@@ -868,0 +869,66 @@   the new section (rows 212 to 229)
@@ -977 +1043,11 @@     the refounding section's heading, plus the new dated note
@@ -1001 +1077 @@       the renamed row (RT-256 -> RT-274)
@@ -1007 +1083 @@       RT-262's row
@@ -1020,5 +1096,5 @@   the count note
@@ -1030,0 +1107,9 @@   the dated note on the count
```

A comparison in Python, using the same row parsing as `rows.py`, read both
ledgers. The only changed rows
are RT-256 (split into the decision-procedure row, unchanged, and RT-274)
and RT-262. RT-274's text after the ID cell is identical to the old row. In
RT-262's row the old text is kept, with a full stop and the note added at
the end. After the change the ledger has one row for each number from
RT-212 to RT-274, with no duplicates and no gaps (63 rows). The main line has
45 rows in that range, with RT-256 twice and RT-212 to RT-229 and RT-274
missing. The one edit outside the allowed set is the heading (should-fix 1).

**B.6 Version 5's section 13 on arm M.** The claim is true. Section 13, weakness
W9, lines 4086 to 4091:

> arm M's code, `experiments/rehearsal-successor-measure/src/arm_middle.py`, has run only on
> this laptop; the rented slice timed arms T, C and F only, and no training
> entry point for arms T, C or M exists on the rented machine yet.

Against the record:

```
$ grep -n "arm M for the first time" experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-claude-code.md
40:| 1. The frozen trainer runs end to end on a rented machine, every arm, arm M for the first time | **Holds** |
$ grep -n "2026-10-04" experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
96-99: four rows "successor development run, 10M ... RAN AND DELETED. ACTUAL AFTER." (arms C, F, M and T)
$ grep -n "arm M's first run" v5.md
3706: ... and arm M's first run on the rented machine (**done, $1.47**) ...
```

Arm M's code, and training entry points for arms T, C and M, ran end to end
on rented machines on 2026-10-04, which version 5's own section 12.3 records.
The sentence and the paragraph's last sentence are out of date (should-fix
4). The row is still rightly "accepted": the ruled fix was made, and later
events overtook it.

**B.7 Citation checker on the pull request's copy.** The pull request was
extracted with `git archive origin/ledger-rows-rt212-229` to a scratch
folder, and the checker was run from there:

```
$ python3 -I scripts/check_citations.py --only experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md --only docs/2026-10-09-ledger-rows-rt212-229-method.md --only docs/2026-10-09-ledger-rows-rt212-229-findings.md --part paths
Confident findings: 7. Things for a human to look at: 3.
$ ... | grep "names:" | sort | uniq -c
   7       names: docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md
```

All seven point to pull request 144's file, which is not on the main line
yet. The findings note discloses this (its point 4), and the warnings go away
once pull request 144 merges, so 144 should merge first or with 145. The
three "look at it" items are at ledger lines 346, 388 and 587, which were
there before this pull request. The number check (`--part numbers`) flags
two figures in the new rows: $1.94 beside the 2026-09-21 ruling's path, and
0.961 beside the label-search check's path. I read both sentences. Neither
claims the figure is in that file; the checker pairs a figure with the
nearest path in the sentence.

## What this does not do

It fixes nothing, merges nothing, and rules on nothing. The questions it
leaves for John are the ones already put in pull request 145's findings note:
whether RT-219 closes by a dated note or by his ruling, and whether
`STATUS.md` gets a note.
