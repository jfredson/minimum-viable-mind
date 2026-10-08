# Method: the red-team ledger's rows for entries 212 to 229, and the renumbering of the records-not-on-the-branch finding

*Written 2026-10-08 (Pacific, by this session's clock; the ruling it carries
out is dated 2026-10-09) by a Claude Code session in its own worktree, on
branch `ledger-rows-rt212-229`, cut from the main line at `dafdaf2` (the merge
of pull request 143, the check of the rows from entry 230 on). Committed
before any row is written or any number changed. $0: nothing was run but
searches of committed files.*

*Written under the workspace plain-language rule. This session wrote none of
the reviews, rulings, checks or registration text the rows summarise, and
none of the rows from entry 230 on.*

## Why this is owed

John's rulings of 2026-10-09
(`docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md`, on branch
`rulings-ledger-packet-2026-10-09`, pull request 144; "As recommended",
authorship mixed) ask for three things this session does:

- **Ruling 2:** the ledger rows for entries 212 to 229 (the review of version
  2 of the successor proposal) are written before the registration commit,
  "by the method of the rows from 230 on", and checked by a session that did
  not write them.
- **Ruling 1:** of the two findings both numbered RT-256, the
  decision-procedure finding keeps the number, and the missing-records
  finding of the Gate C pass on the refounding proposal becomes **RT-274**,
  with a note in the ledger and in the refounding records that it was once
  also called RT-256.
- **Ruling 5:** the refounding's fatal finding RT-262 (narrowing experiment C
  to its first release leaves it no outcome it can reach) stays closed as
  accepted, with a note that a measured check is owed if that proposal's text
  goes toward the spec.

## Which ledger, and the confirmation that the rows are missing

The rows go in `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`,
as the rows from entry 230 on did. Before writing anything, on this branch:

```
$ grep -cE "RT-2(1[2-9]|2[0-9])\b" experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
0
```

The check of those rows (`docs/reviews/2026-10-09-ledger-rows-and-v5-wording-check-claude-code.md`,
section A.5) found the same gap.

## Where the rows come from

1. **The findings:** the Gate C tier 1 review of version 2,
   `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
   (main line `c17dbdc`, pull request 56), its findings table (lines 84 to
   101) and each finding's own section. Its severity words are kept (fatal,
   serious, minor).
2. **The rulings:** `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`
   (`3af189d`, pull request 60), John answering "Agreed" to each, mixed
   authorship; its refinements after the toy re-run (pull request 63), the
   annotation of refinement 2 (pull request 68), "RT-212 item 3 resolved"
   (pull request 69), and decisions 20 and 21. Later amendments are named in
   the row they touch (the dated notes beside RT-220 and RT-222 in that file;
   the rulings of 2026-10-03 and 2026-10-06).
3. **The checks of the fixes,** found by searching every Markdown file for
   the numbers and reading each check where it treats them:
   - the check of the toy re-run under the version 3 rules,
     `reviews/2026-09-26-toy-rerun-v3-rules-check-claude-worktree.md`
     (`70be9fb`, pull request 65), which recomputed every figure from the
     committed outputs with its own code;
   - the check of the free-arm label search,
     `reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`
     (`ecd2b6c`, pull request 70);
   - the review of version 3, `reviews/2026-10-03-successor-v3-gate-c-claude-code.md`,
     "What was checked and held", which refitted reads from the committed
     models;
   - the two checks of the decision code (pull requests 107 and 113), for
     the rules as later amended;
   - the check of the four development runs,
     `reviews/2026-10-04-development-runs-check-claude-code.md` (`51ec07d`,
     merged by `de8ed2c`, pull request 106).
4. **Version 5's uses:** every line of
   `docs/successor-experiment-proposal-2026-10-07-v5.md` carrying one of the
   eighteen numbers is read against the row, and any mismatch goes in the
   findings note.

## The closure rule

Exactly the one in `docs/2026-10-09-ledger-rows-method.md`, "The closure
rule, and the rule for each closure word", unchanged:

- **Closed: the claim was checked** only when a committed check by a session
  that did not write the fix ran a command whose output confirms it, and the
  row names the check. Where a fix has a computed part and a wording part,
  the computed part decides, and the row says which part was only read.
- **Closed: the argument was accepted** when a ruling accepted the finding
  and its fix, the fix is in a committed file, and no measured check of it
  exists. Wording and citation fixes land here even when a later check read
  them as carried, or measured the figures they quote.
- **Open** when no ruling accepted the finding, when the ruling's own owed
  work is not done, when a check found the fix incomplete and the repair is
  unchecked, or when a fatal item has no measured check. The row says what
  closes it.

When unsure between "checked" and "accepted", "accepted"; when unsure whether
a ruling accepted the finding, "open". No row is marked checked on this
session's judgement; this session ran no check.

## Where the rows go

As their own clearly labelled section, placed where the numbering puts them:
after the last rows numbered below 212 and the numbering notes that follow
them, and before the section of rows from entry 230 on. No existing row is
edited by this step.

## The renumbering

- **In the ledger:** the records-not-on-the-branch row's number changes from
  RT-256 to RT-274, saying it was filed as RT-256; the section note and the
  row count note say so with a date. RT-262's row gains the note ruling 5
  asks for. Nothing else in the ledger changes.
- **In the refounding records:** every file found by
  `grep -rl "RT-256"` whose uses mean the records-not-on-the-branch finding
  (or the Gate C pass's range "RT-256 to RT-273") gets one dated note near
  its top, in the ruling's words: "RT-256 in this file means the
  records-not-on-the-branch finding, renumbered RT-274 on 2026-10-09
  (docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md); RT-256
  elsewhere is the decision-procedure finding." No use in the body is
  rewritten. Files whose RT-256 means the decision-procedure finding (version
  5, the 2026-10-06 rulings, the registration handoff, the version 5 check)
  are not touched. Files that discuss both meanings on purpose (the earlier
  method and findings notes and their check) and the running records
  (`STATUS.md`, `data/roadmap.toml`) are left alone and named in the
  findings note.

## What this does not do

It rules on nothing, edits no review, ruling, check or registration text
beyond the dated notes above, and closes nothing by its own measurement. The
rows are owed a check by a session that did not write them (ruling 2).
