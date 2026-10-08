# Method: the red-team ledger's missing rows, from entry 230 on

*Written 2026-10-08 (Pacific, the evening before the file's date) by a Claude
Code session in its own worktree, on branch `ledger-rows-rt230-on`, cut from
the main line at `760deef` (the merge of pull request 138, the check of the
write-in of John's answers to version 5's open items). Committed before any
row is written. $0: nothing was run but searches of committed files.*

*Written under the workspace plain-language rule. This session wrote none of
the reviews, rulings, checks or registration text the rows summarise.*

## Why the rows are owed

Item 12 of `docs/rulings/2026-10-08-v5-open-items-rulings.md` (John's answers
to version 5's open items, "Agreed on all", authorship mixed) rules that the
red-team ledger's rows be written before the registration commit, from entry
230 on, "each closed with 'the claim was checked' or 'the argument was
accepted'", and checked by a session that did not write them.

## Which ledger, and the confirmation that the rows are missing

The rows go in `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`,
the red-team ledger every review since 2026-08-04 numbers its findings
against and every ruling since 2026-09-20 names as the rows' home (for
example the 2026-10-06 rulings' table "Outside findings adopted, with their
ledger numbers"). The compute ledger beside it records money only and carries
no finding rows.

Before writing anything, on this branch:

```
$ grep -c "RT-2[3-9][0-9]" experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md:0
experiments/06-mvm-0a-constructed-self-index/compute-ledger.md:0
$ grep -o "RT-2[0-9][0-9]" experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md | sort -u | tail -1
RT-211
```

This agrees with version 5 of the registration text
(`docs/successor-experiment-proposal-2026-10-07-v5.md`), section 17, failure
4 ("ledger rows for RT-237 to RT-246: 0 of 10", "RT-247 to RT-256: 0 of 10")
and section 21, item 12 ("the ledger on the main line carries no row for
RT-230 onward").

## Where the rows come from

A search of every Markdown and TOML file for numbers RT-230 to RT-399 finds
the numbers RT-230 to RT-273, and RT-274 and RT-299 only inside one sentence
saying no file uses them (`docs/reviews/2026-10-07-filtered-battery-check.md`,
line 23). Nothing later than RT-273 has been assigned. The numbers come from
four sources, each read in full where it defines a finding:

1. **RT-230 to RT-236**: the review of version 3 of the successor proposal,
   `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`
   (its findings table, lines 96 to 102). Ruled in
   `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, pages 1 to 3.
2. **RT-237 to RT-246**: the inside registration review (Gate A, tier 1) of
   version 4, `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`
   (its findings table, lines 127 to 136). Ruled in
   `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`, pages 1 to 6.
3. **RT-247 to RT-256**: outside findings from the ChatGPT review of version
   4 (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-chatgpt.md`),
   adopted and numbered by the same 2026-10-06 rulings file (its table of
   adopted outside findings and its same-day follow-up). Severities are the
   outside dispositions' (`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`,
   lines 141 to 149).
4. **RT-256 to RT-273**: the inside pass (Gate C, tier 1) on the proposal to
   refound the project on the two-sided question,
   `docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md` (section 3).
   Ruled in `docs/rulings/2026-10-07-two-sided-question-rulings.md`, "Rulings
   later the same day" and rulings 9 to 11. **RT-256 is used twice**, once
   in source 3 and once here; see the findings note.

For each finding the row gives: the finding in one plain sentence; its
source file; its severity as the source grades it; how it was disposed (what
was ruled, by whom, and the rulings file); and its closure status.

## The closure rule, and the rule for each closure word

The closure rule is in `docs/outside-review-protocol.md`, "The closure rule,
which is the new part". Its bullet "The ledger says which of the two
happened" asks that a fatal item's ruling line say "either that the argument
was accepted or that the claim was checked, and, when it was checked, names
the reviewer and the check", because "agreement and verification are not the
same thing". Its first bullets ask that every fatal finding have the commit
that lands the fix and a measured check by a session other than the one that
wrote the fix; serious findings are closed the same way or carried as an
open item named in the registered text with John's ruling and reason. The
ledger's own last rows show the form: RT-204 is closed by a measured check
by the reviewer, "who did not write the fix"; RT-205 to RT-210 are closed as
wording "confirmed by the Re-check".

Each row gets exactly one of three closure statuses:

- **Closed: the claim was checked.** Only when a committed check file,
  written by a session that did not write the fix, ran a command whose output
  confirms the fix (or confirms the run the ruling asked for). The row names
  the check file. A reading of the text, however careful, does not qualify.
  Where a fix has a part that changes what is run or computed and a part that
  is wording, the computed part decides, and the row says which part was
  only read.
- **Closed: the argument was accepted.** When a cited ruling accepted the
  finding and its fix, the fix is in a committed file, and no committed
  measured check of the fix exists. Wording fixes land here even when a
  later session read the text and found the wording carried; the row names
  that reading where there is one.
- **Open.** When no ruling accepted the finding; when the ruling's own owed
  work is not done; when a committed check found the fix incomplete and the
  repair has not been checked; or when the item is fatal and has no measured
  check. The row says what closes it.

When unsure between "checked" and "accepted", the row says "accepted"; when
unsure whether a ruling accepted the finding, the row says "open". No row is
marked "checked" on this session's own judgement; this session ran no check.

## What this does not do

It does not renumber any finding, edit any review, ruling, check or the
registration text, or close any item by its own measurement. The rows are
owed a check by a session that did not write them (item 12).
