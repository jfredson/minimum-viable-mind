# Method: writing version 5 of the successor proposal, the registration text with every ruled change written in

*Written 2026-10-07 (Pacific) by a fresh Claude Code session in its own
worktree, on branch `worktree-agent-a43545d6649460124`, cut from the main line
at `597a3f5` (the merge of pull request 123, the outside-perspective poll).
**Committed before any line of version 5 is drafted.** Nothing is trained,
rented or called: $0. No existing file is edited; this session writes three new
files and nothing else.*

*Written under the workspace plain-language rule (`~/Code/CLAUDE.md`, ruled
2026-08-30): the plain word before the term of art, every identifier carrying a
phrase saying what it is, no em-dashes.*

## 1. What this session is doing, in one paragraph

Version 4 of the successor experiment proposal
(`docs/successor-experiment-proposal-2026-10-03-v4.md`) is the text meant for
registration. Since it was filed, John has ruled a long list of changes to it,
and several sessions have done the work those rulings asked for, much of it on
branches that have not reached the main line. The registration commit, which
is John's and has a kill date of 2026-10-18, needs one text with everything
ruled written in. This session writes that text as version 5
(`docs/successor-experiment-proposal-2026-10-07-v5.md`), a handoff note saying
what it could and could not settle
(`docs/successor-registration-handoff-2026-10-07.md`), and this method note
first. Version 5 is owed a check by a session that wrote none of it, under the
pairing rule of `docs/outside-review-protocol.md`.

## 2. What will be read, in this order

Governing texts first, then the target, then the rulings newest first, then
the reviews, then the work on branches.

1. `~/Code/CLAUDE.md` and the repository's `CLAUDE.md` (the plain-language rule
   and the project's standing rules).
2. `docs/outside-review-protocol.md` (Gate A, the pairing rule, the closure
   rule, MEASURED against ARGUED) and `docs/known-failure-modes.md` (the six
   entries and the drafted seventh, each with its test).
3. Version 4, all 4,219 lines, with its section 19 (the seven questions) and
   section 20 (the change log) read for anything said to be ruled and not
   written.
4. The rulings, newest first: `docs/rulings/2026-10-07-two-sided-question-rulings.md`
   (decision 3 as first ruled, its stop-condition addition, and decisions 3
   and 4 as revised); the ruling packet on the two flat built models,
   `docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`, read from branch
   `ruling-packet-cm-flat` at commit `7583326`; the twelve-page ruling on the
   registration review, `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`
   with its same-day follow-ups, from branch `rulings-2026-10-06-gate-a-v4`
   at `525a625`, together with the two question packets and the two
   dispositions files it adopts; `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`;
   `docs/rulings/2026-10-03-version-4-check-questions-rulings.md`;
   `docs/rulings/2026-10-03-version-4-questions-rulings.md` (the record that
   stands on the four disputed points).
5. The reviews: the inside Gate A review of version 4
   (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`,
   findings RT-237 to RT-246, on branch `gate-a-tier1-successor-v4` at
   `135c1f7`), especially its table "The registration text as reviewed"; the
   ChatGPT outside review (findings A1 to A13, branch `tier2-chatgpt-v4` at
   `6136407`); the Gemini outside review (findings G1 to G9, branch
   `tier2-gemini-v4` at `8da74c4`); the check of version 4
   (`reviews/2026-10-03-proposal-v4-check-claude-code.md`, section 4, the
   thirty wording fixes); the check of the competing-solver run (its section
   7).
6. The code freeze (`docs/2026-10-04-successor-code-freeze.md`, sections 4.1
   and 4.2) and the trainer's defaults in
   `experiments/08-successor-degree/src/train_successor.py`.
7. The work on branches, each by `git log --oneline main..<branch>` and
   `git diff --name-only main...<branch>`, then its findings and its check:
   the training exclusion by pairing (`training-exclusion-pairing`, pull
   request 115; its check on `check-training-exclusion`); the spending-alarm
   fixes (`tripwire-fixes`, pull request 116; its three checks on
   `check-tripwire-fixes`); the sharpness fix and the in-use check
   (`fix-sharpness-inuse-check`); the page 4 toy re-run with 1,800 fitting
   episodes (`page4-toy-rerun-1800`, pull request 121; its check on
   `check-page4-rerun`); the decision procedure (merged, pull request 105,
   with its checks in pull requests 107 and 113); the decoy test
   (`decoy-test-a6`, pull request 108; its check on `check-decoy-test-a6`);
   the check of the four development runs (`check-dev-10m`, pull request
   106). Also the compute ledger's four development-run rows and the
   red-team ledger's last rows.

## 3. How "ruled" is told from "proposed"

A change is **ruled**, and is written into version 5 as registered text, only
when one of these holds:

- a rulings file (`docs/rulings/*-rulings.md`, or a dated ruling section in
  one) records John's answer in his own words, with authorship marked, to a
  named page or question; "Agreed on all" to a named packet counts when the
  packet is identified and the drafted text it adopts is identified;
- a dated addendum in such a file records a later answer the same way.

Everything else is **proposed**: a PROPOSAL file, a review finding, a check's
recommendation, a method note's own statement of what John said when no
rulings file carries it, a session's design call (for example the trainer's
defaults), and this session's own drafting where a ruling leaves the words
open. Proposed material goes into version 5 only in one of two ways: as the
recommended text, marked with an open item that names it as unruled; or not
at all.

Two edge cases, decided now so they are not decided under pressure:

- **The sharpness repair.** Two method notes on branches say John ruled option
  1(b) plus option 4 of the flat-models packet on 2026-10-06, but no rulings
  file on the main line or any branch records those words. The repair is
  nevertheless carried as ruled, because decision 3 of
  `docs/rulings/2026-10-07-two-sided-question-rulings.md` (ruled, authorship
  mixed) names "the $1.14 repair" as the first step of the first release. The
  handoff note records that the 2026-10-06 ruling has no ruling file.
- **Where a later ruling and an earlier one disagree**, the later governs and
  the earlier is cited as superseded. One known case: the 2026-10-06 ruling
  kept the outcome terms with a scope phrase (page 11); the 2026-10-07 ruling
  renames them. The renaming is written in; the scope phrase is kept; whether
  it should travel with the renamed terms is an open item.

## 4. How open items are marked

Every point this session cannot settle from a ruling is marked in the body of
version 5 as **[OPEN ITEM n for John: one sentence]**, in bold square brackets
at the place it bears, and listed in version 5's section 21, "Open items for
John", with the finding or source behind it, what the text does meanwhile, and
this session's recommendation with its confidence. The handoff note repeats
the list. A finding of a review that has no ruling is written in as the
finding's demand, bracketed the same way.

## 5. How version 5 is built, so a reader can diff it

Version 5 keeps version 4's section numbers and order. It is made by taking
version 4's text and applying each change in place, so that a plain `diff` of
the two files shows every change and nothing else moves. Each changed passage
carries, in a phrase, the ruling or finding it comes from. New material goes in
three places: a new subsection 5.6 (the amendment that turns the built arms
into hand-set references); a rewritten section 17 (this session's run of the
failure-mode list on version 5, each test with its command and its output); a
rewritten section 20 (the change log from version 4, one entry per ruling or
finding) and a new section 21 (open items). The header and the source table are
rewritten for version 5. Nothing from version 4 is deleted without the change
log saying so.

The toy figures quoted for the reads are the 1,800-fitted ones of the page 4
re-run where that re-run gives them, because John ruled the fitting count
changed and the re-run's findings say version 5 should quote them; the
420-fitted figures stay where the re-run does not supersede them, labelled.

## 6. The checks this session runs on its own text, and what each must show

Each is run on the finished version 5, with the command and its output filed in
version 5's section 17 or in the handoff note. None is a substitute for the
check another session owes.

1. **The failure-mode pass.** Every entry of `docs/known-failure-modes.md`,
   1 to 6, and the drafted seventh, run against version 5 with the list's own
   tests: the denominators and the top of the scale on the committed records
   (failure 1); the route-sentence search on sections 0 to 16 and the two
   runs from committed counts (failure 2); every pre-stated cell counted and
   every threshold at both ends (failure 3); the two sweeps and the two
   repository checkers, `scripts/check_citations.py` and
   `scripts/check_single_source.py`, on version 5 (failure 4); the launcher
   argument-guard check (failure 5); the remote-forms check (failure 6); each
   pre-stated outcome line against the code path that produces it (candidate
   7). "Considered and does not apply" is not a disposition. What each must
   show: a count, a record, or a zero, as the list's entries say.
2. **A scan for bare identifiers.** Every `RT-` number, pull request number,
   commit identifier and branch name in version 5 is listed by `grep`, and
   each line is read to confirm a phrase beside it says what the thing is.
   The count of lines read and the count of bare ones found (which must be
   zero after repair) are filed.
3. **A scan for em-dashes.** `grep -c` for the em-dash and the en-dash
   characters on version 5 must return 0. Version 4's own count is recorded
   beside it, because carried text can carry the character in.
4. **Every figure has its source named.** The number sweep of failure 4
   lists every line with a figure; for each, the paragraph it sits in must
   name the file, record, ruling or section the figure comes from. The
   count of figure lines and the count without a source (which must be zero
   after repair, or named in the handoff) are filed.
5. **Diff against version 4.** `diff` between the two files is produced and
   its length recorded, and the change log is read against it so that no
   change is in one and not the other.

## 7. What this session does not do

It does not rule, launch, rent, spend or train. It does not edit version 4,
any ruling file, any review, the protocol, the known-failure list, the ledger,
`STATUS.md` or `data/project.toml`. It does not merge any branch; it cites
branch work by branch and commit and says in the handoff that the registration
commit cannot rest on unmerged branches. It does not check its own work: that
is owed to a session that wrote none of these three files.
