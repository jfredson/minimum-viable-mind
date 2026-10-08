# Handoff: version 5 of the successor proposal, the registration text, as drafted on 2026-10-07

*Written 2026-10-07 (Pacific) by the Claude Code session that wrote
`docs/successor-experiment-proposal-2026-10-07-v5.md` and its method
`docs/successor-registration-method-2026-10-07.md`, on branch
`worktree-agent-a43545d6649460124`, cut from the main line at `597a3f5`.
Nothing trained, rented or called: $0. No existing file edited. **Version 5
is owed a check by a session that wrote none of these three files**, under
the pairing rule of `docs/outside-review-protocol.md`; this note says what
that session should look at first.*

*Written under the workspace plain-language rule.*

## 1. What was done, in one paragraph

Version 5 is version 4 with every change John has ruled since written in, in
place, so that `diff` between the two files shows every change (5,550 lines
against 4,219; the plain `diff` output is 3,558 lines long). It carries the ruling of
2026-10-07 on the shape of the experiment (the repair of the built arms as a
new subsection 5.6, the verification before the free-arm run with its stop
condition, the second release kept and conditional, the outcomes renamed, the
kill dates unchanged); the twelve pages of the 2026-10-06 ruling on the
registration review and their follow-ups (every inside finding RT-237 to
RT-246 and every adopted outside finding RT-247 to RT-256 written in as the
dispositions drafted them, with the measured figures from the work those
rulings asked for: the page 4 re-run, the decoy test, the decision procedure,
the training exclusion); the seven rulings of 2026-10-04 and the two of
2026-10-03 (night) with the thirty wording fixes behind them; the code
freeze's two findings; the development runs' check; and the spending alarm's
amendment. It has its own failure-mode pass (section 17), a change log keyed
to each ruling (section 20) and twelve open items for John (section 21).

## 2. How many ruled changes were written in

Counting by the ruling or finding behind each change, as section 20 keys them:

- the 2026-10-07 ruling: 4 (decision 3 as first ruled; its stop-condition
  addition; decision 3 as revised; decision 4 as revised);
- the 2026-10-06 ruling: 12 pages and 6 follow-up items, carrying 20 numbered
  findings (RT-237 to RT-256), every one written in;
- the 2026-10-04 ruling: 7 rulings, all written in, with the 15 text changes
  section 7 of the check of pull requests 88 and 89 listed;
- the 2026-10-03 night ruling: 2 rulings, and 28 of the check's 30 wording
  fixes (fix 22 was optional and not taken; fix 25 is the re-run sweep,
  section 17);
- the code freeze's 2 findings for the registration text;
- the spending alarm's 4 fixes, as one amendment to section 12.5.

**In all: 39 ruled changes, plus 28 wording fixes and 4 alarm fixes carried
as ruled, written into 78 edits of version 4's text.** Nothing ruled that this
session found was left out; where a ruling left words open, the words are
this session's and are marked as an open item.

## 3. What is open for John: twelve items, the two biggest first

The full list with sources and recommendations is version 5, section 21.

1. **The bar for "the repaired route holds" (open item 1).** The 2026-10-07
   ruling says what "holds" means in figures is fixed in the amendment text
   before the reruns launch. The in-use check as coded has two parts (the
   built-in answer's weight on the true agent at least 0.9; the route use,
   the share of right answers lost when the built-in answer is swapped, at
   least 0.5 on every built route). **Part B fails every toy arm C and arm M
   seed, before and after the sharpness fix** (route use 0.22 to 0.29 on arm
   C; 0.07 to 0.11 on arm M's stirred-in route), so with the bar as coded
   the three reruns would very likely fail the verification and experiment C
   would stop at about $1.14. The findings on branch
   `fix-sharpness-inuse-check` offer four options and choose none. This
   session recommends keeping 0.5 and letting the stop condition do what it
   was ruled for, with the alternative (redesign the arms so the built route
   is the only route) as the way to a real reference; confidence moderate.
   **This is the decision the registration turns on.**
2. **The registration cannot be committed from this branch as it stands
   (open item 10).** Fifty of the records version 5 cites are on fifteen
   unmerged branches (the rulings file of 2026-10-06, the inside and outside
   reviews, the flat-models packet, the development-runs check, the sharpness
   work, the page 4 re-run and its check, the decoy test and its check, the
   training exclusion and its check, the alarm fixes and their checks), and
   the frozen code is changed on three of them. A registration commit may not
   rest on a record its reader cannot open at a main-line commit (the
   citation defect RT-145; failure 4 of the known-failure list). Merging the
   checked branches, having the sharpness branch checked and merged, and then
   naming the main-line commit of `experiments/08-successor-degree/` in
   section 7.4 is the path; confidence high.

The other ten, briefly: (2) the 2026-10-06 ruling on the flat-models packet
(option 1(b) plus option 4; the alarm's four fixes) has no rulings file and
should get one; (3) the exact words of the renamed outcome terms; (4) whether
the scope phrases travel with the renamed terms; (5) the training recipe,
written from the frozen trainer's defaults and never ruled; (6) whether arm
T's rerun failing also stops C; (7) the fitter's iteration limit at 1,800
episodes and the frozen code's fitting count, still 420 of 600; (8) a ruled
test of a differently coded decoy; (9) three reporting changes from the
development runs' check; (11) the derived launcher standing in for the one
RT-228 named; (12) the red-team ledger's rows for RT-237 to RT-256, none of
which exist.

## 4. Contradictions and gaps found in the record

Each is stated in version 5 where it bears; this is the list.

1. **The repair's ruling has no ruling file.** Two method notes on branches
   (`docs/2026-10-06-sharpness-fix-inuse-check-method.md`,
   `docs/2026-10-06-tripwire-fixes-method.md`) state that John ruled option
   1(b) plus option 4 of the flat-models packet, and its page 2, on
   2026-10-06. No `docs/rulings` file on the main line or on any branch
   records those words (`grep -rn -i sharpness docs/rulings/` on the main
   line returns nothing). The repair is nonetheless ruled through decision 3
   of 2026-10-07, which names it; the alarm fixes have only the method note.
2. **The verification as coded contradicts the toy.** The in-use check's
   second part fails the toy's trained, correctly reading arms C and M, and
   the 10-million arms whose route is flat; as a threshold it does not
   separate the working end from the broken end on the toy (section 17,
   failure 3, part three). The stop condition John ruled therefore turns on
   a bar nobody has ruled (item 1 above).
3. **Two rulings a day apart disagree on the outcome words.** The 2026-10-06
   ruling (page 11) kept the terms and added a scope phrase; the 2026-10-07
   ruling (decision 3) renames them. The later governs and is written in;
   the phrase is kept pending John's word (open items 3 and 4).
4. **Version 4's section 3 said the toy reaches the fifth term; the code
   gives R3.** Found by the code freeze (section 4.1) and the outside review
   (A10). Resolved in version 5 by the 2026-10-06 ruling on page 9: the fifth
   term if the free model's seed 0 is taken as the step 5a run, R3 otherwise
   (the decision procedure's cases 1 to 3).
5. **The toy figures version 5 quotes were measured on models the registered
   arms no longer are.** Every toy reading comes from the twelve committed
   models with a learned sharpness; the registered built arms have it fixed.
   Nine models were retrained with it fixed, learn the task, and have been
   read on one of nine (arm T seed 0, 0.0000 as before). Eleven re-reads are
   owed, and the toy outcome under the repaired construction has not been
   summarised (W17).
6. **The red-team ledger carries no row for RT-230 onward**, although the
   2026-10-06 ruling assigns RT-247 to RT-256 and says the rows from RT-237
   are owed (section 17, failure 4, part two (c)).
7. **The page 4 re-run's outcome line was made under rules since changed.**
   Its per-model figures stand; its `summary.json` outcome ("substrate not a
   testbed") was computed before the decision procedure of pull request 105
   changed `procedure.py`, and the re-run's own findings say to re-summarise
   before quoting it. Version 5 quotes the per-model figures only.
8. **The decoy test's "not fooled" could not have come out otherwise**, by
   its own method and its check; the check's probe with a differently coded
   decoy gave readings of 0.23 to 0.29 on a model whose true reading is 0.
   John's page 12 answer ("decide after the decoy test") was given as
   decision 3 of 2026-10-07 (continue through the first release); the
   two-sided proposal's revised page 12 recorded that the test "ruled out an
   exact copy only". Version 5 carries the probe as weakness W18 and asks for
   a ruled test (open item 8).
9. **`STATUS.md`'s 2026-10-07 entry says the account balance is $73.77.**
   That was the balance before the development wave (00:11Z on 2026-10-05);
   after it the balance was $72.3178 (the check of the development runs,
   section 3). A small staleness, not in registered text.
10. **The frozen code still fits the read on 420 of 600 development
    episodes**; the ruled 1,800 of 1,980 was made at run time by the page 4
    re-run's drivers only. The code change is owed before registration
    (open item 7).
11. **The thirty wording fixes' ruling says "the thirty wording fixes"
    go into the registration text**, and the inside review's table says all
    thirty can be written in; fix 22 was marked optional by the check itself
    and is not taken, and fix 21 (one range for the whole successor) is met
    by giving both splits beside each other rather than by one range.
    Stated in section 20 so the checker does not count them as missed.

## 5. What another session must check, in order of what it would catch

1. **The diff.** `diff docs/successor-experiment-proposal-2026-10-03-v4.md
   docs/successor-experiment-proposal-2026-10-07-v5.md` against section 20's
   change log: every hunk should be named by a log entry, and every log
   entry should have a hunk. This session built version 5 by applying 78
   replacements to a copy of version 4 (the build script is in its scratch
   folder, not committed); a hunk no entry names is a slip.
2. **Every ruled change against its ruling, word by word.** The 2026-10-06
   ruling adopts drafted text at named line ranges of the two dispositions
   files; version 5 carries that text with small changes of tense and
   cross-reference, and with the renaming of 2026-10-07 applied on top. The
   checker should read each adopted passage against the dispositions file
   and confirm nothing of substance moved. The places this session changed
   the drafted wording on purpose: the outcome table's terms (renamed; open
   item 3), the fifth term's row (adds the step 5b case from page 9), rule 1
   (adds arm F's exception), section 8.1's R3 sentence (both exceptions),
   and the no-transplant item (the ruling 3 of 2026-10-04 sentence folded in
   before the A9 text).
3. **Every figure against its file.** Section 17's failure 4 lists the
   classes. The ones new in version 5: the page 4 re-run's figures (branch
   `page4-toy-rerun-1800` at `e948899`: `models-1800/summary.json`,
   `comparison.md`, the row files); the sharpness findings' tables (branch
   `fix-sharpness-inuse-check` at `644238e`); the development-runs check's
   tables (branch `check-dev-10m` at `51ec07d`, sections 3 to 7); the decoy
   test's table and its check's probe (branches `decoy-test-a6` at `6794155`
   and `check-decoy-test-a6` at `ba5d64f`); the dispositions' measurements
   (branch `rulings-2026-10-06-gate-a-v4` at `525a625`); the ledger's four
   2026-10-04 rows. This session read each figure off those files or the
   findings that quote them and recomputed the money lines (section 17,
   candidate 7); it did not re-run any model.
4. **The failure-mode pass of section 17.** Re-run `failure_pass_v5.py`'s
   blocks (the commands are given in section 17; the script reads the page 4
   rows from a `git archive` of the branch and the main line's committed
   outputs) and compare. The text sweeps should return 1,136 and 399 on
   sections 0 to 16 cut at the section 17 heading.
5. **What this session decided on its own, so it can be overturned.** The
   wording of the eight outcome terms; keeping the scope phrases; treating
   arm T's rerun like arms C and M in the stop condition; writing the trainer's
   defaults as the registered recipe; quoting the 1,800-fitted toy figures as
   the registered toy record and the 420-fitted ones as the earlier record;
   naming the derived launcher; folding the inside review's "report arm T's
   row-choice split" into the reporting table; calling the three new terms
   the sixth, seventh and eighth terms. Each is marked in the text as an open
   item or as this session's reading.
6. **The plain-language rule.** This session scanned for em-dashes (0) and
   bare identifiers (845 identifiers on 533 lines, none flagged by a weak
   heuristic, every new line read by eye). A checker reading for jargon will
   find more than a scan does; the handoff asks for that reading.

## 6. What this session did not do

It did not rule, launch, rent, spend or train. It did not edit version 4, any
ruling file, any review, the protocol, the known-failure list, the ledger,
`STATUS.md` or `data/project.toml`; the method note says why `STATUS.md` and
the site data are left to the session that merges this work (a "WHERE THINGS
STAND" entry and `data/project.toml` are updated in the same commit, per the
repository's `CLAUDE.md`, by the session that lands it on the main line). It
did not merge any branch. It did not run the eleven owed re-reads of the
hand-set toy models, re-summarise the page 4 re-run, or write the ledger
rows. It did not check its own work. The build script that turned version 4
into version 5 is in its scratch folder and is not committed; the diff is the
record.

## 7. Files

- `docs/successor-registration-method-2026-10-07.md` (committed first, at
  `6a38f08`).
- `docs/successor-experiment-proposal-2026-10-07-v5.md`.
- `docs/successor-registration-handoff-2026-10-07.md` (this note).
