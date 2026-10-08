# Findings: writing the red-team ledger's rows from entry 230 on

*Written 2026-10-08 (Pacific, the evening before the file's date) by the
Claude Code session that wrote the rows, on branch `ledger-rows-rt230-on`.
The method is `docs/2026-10-09-ledger-rows-method.md`; the rows are the last
section of `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`.
$0. Written under the workspace plain-language rule. Nothing here renumbers a
finding or rules on anything; each point below that needs a decision is
John's.*

## What was written

Forty-five rows on forty-four numbers, RT-230 to RT-273. Fifteen are closed
with the claim checked, twenty-two with the argument accepted, and eight are
open:

- **Bearing on the successor's registration commit:** RT-237 (the free
  model's gate; its closure check runs separately), RT-240 (the episode
  counts at the registered width; waits on item 7 of the 2026-10-08 rulings,
  the iteration-limit change, re-run and check), RT-247 (the decoy; waits on
  item 8, the differently coded decoy test, or W18 named in the registered
  text if not done by 2026-10-18), RT-250 (the outcome words; waits on item
  3's code change so the code prints the renamed terms, and its check).
- **Bearing on the refounding proposal, which registers nothing:** RT-263,
  RT-267 and RT-273 (each found partly applied by the check of version 2 of
  that proposal and repaired in place by its author at `32c3b78`, a commit no
  other session has checked), and RT-269 (the book's chapter 5 not yet
  quoted, waiting on the book's text).

Nothing has been assigned a number above RT-273: a search of every Markdown
and TOML file finds RT-274 and RT-299 only in one sentence of
`docs/reviews/2026-10-07-filtered-battery-check.md` saying no file uses them.
That check numbered its own findings FB-1 to FB-24 and said deliberately that
they are not ledger findings.

## 1. A number collision: RT-256 names two different findings

- **The decision-procedure finding.** The same-day follow-up of
  `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md` (item 6, added at
  commit `380612a` on 2026-10-06) gives RT-256 to the ChatGPT review's fatal
  finding A2: the decision procedure had never been run end to end on the
  ruled rules. Version 5 of the registration text uses RT-256 in this sense
  (lines 88, 1804, 3306, 5443), as do its handoff and its check.
- **The records-not-on-the-branch finding.** The Gate C pass on the
  refounding proposal (`docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md`)
  numbered its eighteen findings RT-256 to RT-273, saying "the highest number
  in use is RT-255". It reviewed the proposal at commit `9184ad9`, and
  `git merge-base --is-ancestor 380612a 9184ad9` exits 1: the addendum that
  assigned RT-256 was not in the history that pass searched. Version 2 of the
  proposal, the filtered battery draft and three checks use RT-256 in this
  sense.

**What the rows do:** both are recorded under RT-256, each with a phrase
naming which finding it is, in their own sections. **What needs John:** which
finding keeps the number. This is the same kind of collision as RT-198, which
the ledger's numbering note of 2026-09-25 records as also unsettled. One
option, not a recommendation this session can make on its own: the
decision-procedure finding keeps RT-256 (assigned first, and the one the
registration text cites), and the Gate C finding is cited everywhere as "the
records-not-on-the-branch finding, RT-256 of the Gate C pass", with no
renumbering of the other seventeen.

**A misdescription beside it.** The same Gate C pass calls RT-255 "the a2
decision-procedure finding, in `docs/2026-10-06-successor-a2-decision-procedure-findings.md`".
RT-255 is the unseen-combinations remark (training must not contain the
fresh or relaxed pairings); that findings file mentions RT-255 only in that
sense (its line 76, "Control 5 (RT-255)"). The pass's own text is left as
filed.

## 2. Gaps: numbers that still have no ledger row

Outside the range item 12 asked for, and not written here:

- **RT-212 to RT-229**, the Gate C review of successor proposal version 2
  (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`,
  ruled in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`). Version
  5 of the registration text cites sixteen of these eighteen numbers (RT-212,
  the empty-read finding, 25 times), so the registered text will lean on
  findings with no row. The ruling of 2026-10-03 on version 3's review listed
  them as owed alongside RT-230 onward.
- **RT-172 to RT-203**, from three filed reviews of 2026-09-21, listed in the
  ledger's numbering note of 2026-09-25 as having no rows.
- **RT-198's two meanings**, the protocol-repair finding and the launcher's
  silent-argument finding, still unsettled (the same note).
- **The adopted outside findings on the A3 closure text** (Gemini G1 to G6,
  ChatGPT A1 to A15), reserved numbers after RT-211 by that note and never
  given rows or numbers.

These are the reconciliation item 21 of the 2026-09-21 ruling assigned to a
later session. If the registration commit is to cite only findings with
rows, RT-212 to RT-229 are the ones that matter, because version 5 cites them.

## 3. Points the rows record but could not settle

1. **The decision-procedure finding (RT-256) was checked on code that will
   change again.** Its two checks (pull requests 107 and 113) checked the
   decision code as of 2026-10-06. Items 3, 7 and 9 of the 2026-10-08 rulings
   change the frozen code again (the renamed outcome words, the iteration
   limit with the 1,800-episode fitting, and the reporting changes), and only
   then is the registered code named (item 10). No ruling says whether the
   end-to-end run of version 5's rehearsal item R-13 is repeated on that final
   code. The row is closed as checked on the record as it stands; whether the
   closure carries to the final code is for John or the check of the code
   changes.
2. **The fatal Gate C finding (RT-262) is closed on argument, not
   measurement.** It is an argued finding whose fix is John's revised
   decision 3; the check of version 2 compared the text with the ruling by
   reading. The closure rule's measured check is written for fatal findings
   before a registration commit, and this proposal registers nothing; the
   row says so rather than marking it checked.
3. **Four refounding-proposal rows depend on one unchecked commit.** The
   author of version 2 of the proposal applied its check's six must-fix items
   in place at `32c3b78`; no file on the main line checks that commit
   (a search for the commit across the repository's Markdown finds none).
   RT-263, RT-267 and RT-273 stay open on it; RT-266's added spec paragraph,
   marked there as softening a loss condition, also rests on it.
4. **Severity scales differ by source.** The review of version 3 used "minor"
   for its lowest grade; the review of version 4 used "worth-noting"; the
   Gate C pass used "minor". The rows keep each source's word. RT-255 has no
   grade in any source, and the row says so.
5. **Two unlettered outside remarks took no number.** The outside
   dispositions (lines 112 to 132) list three unlettered remarks from the
   ChatGPT review's feasibility table; one became RT-255, and the other two
   (the pinned dependency file; the single-fit-and-reload procedure) were
   disposed as already covered. They have no number and no row, which matches
   how they were ruled.
6. **"The claim was checked" means the fix's check, not the finding's
   measurement.** Several findings were measured by the reviewer who raised
   them (RT-230, RT-240, RT-245 and others). That makes the finding solid;
   it is not a check of the fix, and no row is marked checked on that basis
   alone.

## What was not done

No finding was renumbered, no review, ruling, check or registration text was
edited, and no check was run by this session. The rows are owed a check by a
session that did not write them (item 12 of the 2026-10-08 rulings).
