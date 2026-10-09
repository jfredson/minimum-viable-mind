# Findings: the ledger rows for entries 212 to 229, and the renumbering to RT-274

*Written 2026-10-08 (Pacific, by this session's clock; the rulings it carries
out are dated 2026-10-09) by the Claude Code session that wrote the rows, on
branch `ledger-rows-rt212-229`. The method is
`docs/2026-10-09-ledger-rows-rt212-229-method.md`; the rows are the section
"Rows for entries 212 to 229" of
`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`. $0.
Written under the workspace plain-language rule. Nothing here rules on
anything; each point that needs a decision is John's.*

## What was written

Eighteen rows on eighteen numbers, from the Gate C review of version 2 of the
successor proposal (`c17dbdc`, pull request 56) and John's rulings on it:

- **Closed with the claim checked: 6.** RT-212 (the empty-read finding, the
  one fatal finding), RT-213 (the anchor's failed gate), RT-214 (control 3 on
  arm M), RT-215 (the site-set rule never run), RT-216 (nominations at the
  acting channel's injection), RT-220 (the lesion's honest description). Each
  rests on a check that ran its own code: the check of the toy re-run
  (`70be9fb`, pull request 65), the check of the free-arm label search
  (`ecd2b6c`, pull request 70) for RT-212, and the two decision-code checks
  (pull requests 107 and 113) for RT-220's rule as amended.
- **Closed with the argument accepted: 11.** RT-217, RT-218 and RT-221 to
  RT-229: wording, citation and costing fixes, each carried in version 5.
- **Open: 1.** RT-219 (the two entangled shares): see point 1 below.

Version 5's uses of the sixteen numbers it cites were read line by line
against the rows. They match, with the one exception in point 3. Its source
table's count ("one fatal finding ..., four serious, thirteen minor") matches
the review. RT-221 (separation figures from excluded site sets) and RT-227
(citations of unmerged files) are the two it does not cite; both fixes are in
it anyway.

The renumbering: the records-not-on-the-branch finding is now RT-274 in the
ledger, the count note reads forty-five rows on forty-five numbers (old
wording quoted in a dated note), and RT-262's row carries ruling 5's note.
Seven files got the dated note under their title:

1. `docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md`
2. `docs/rulings/2026-10-07-two-sided-question-rulings.md`
3. `docs/reviews/2026-10-07-proposal-v2-check.md`
4. `docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md`
5. `docs/filtered-battery-proposal-2026-10-07.md`
6. `docs/reviews/2026-10-07-filtered-battery-check-2.md`
7. `docs/reviews/2026-10-08-filtered-battery-check-3-claude-code.md`

The last three use RT-256 only inside the quoted title of the Gate C pass's
commit ("RT-256 to RT-273"); the note is true of them too.

*Dated note, 2026-10-08 (evening, Pacific), added after this note's check
(`docs/reviews/2026-10-09-ledger-packet-and-rows-212-229-check-claude-code.md`,
should-fix 1): one more ledger edit was made and not listed above. The
heading of the refounding pass's section changed from "(RT-256 to RT-273)" to
"(RT-257 to RT-274; filed by the pass as RT-256 to RT-273)", as ruling 1
requires.*

## What could not be traced, or does not match

1. **RT-219's owed correction was never made.** The ruling says "the
   findings' sentence is corrected at its check". The sentence, in
   `docs/2026-09-26-rehearsal-repairs.md`, section 5 ("about three fifths
   entangled (0.6033 of the fresh episodes, `measure_base_M.json`)"), still
   cites the gate-episode figure to the fresh-trial file. It has no dated
   note, and the check of the repairs (`d216dbc`, pull request 58) prints
   the share in its output but does not correct the sentence. Version 5,
   section 5.3, states both figures correctly, so nothing registered is
   wrong. The row is open by the method's rule (owed work not done). What
   closes it: a dated note beside that sentence, or John's ruling that
   version 5's statement is enough.
2. **RT-214's annotation sits in a different file from the one named.** Item
   2 says the fold-in ruling (item 2 of
   `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`) "stands and is
   annotated with the checked figures". That file has no such annotation.
   The substance is in refinement 2 of
   `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` (arm M reads on
   all three seeds, the fold-in stands), and the checked figures are in the
   check of the toy re-run. The row is closed as checked on the computed
   part and says where the annotation is.
3. **Version 5's section 13 is out of date on arm M (RT-228).** It says arm
   M's code "has run only on this laptop; the rented slice timed arms T, C
   and F only, and no training entry point for arms T, C or M exists on the
   rented machine yet". All four arms ran end to end on the rented machine on
   2026-10-04 (the compute ledger's four rows of that date; version 5's own
   section 12.3, "arm M's first run on the rented machine (done, $1.47)"),
   and the check of those runs (`51ec07d`, merged by `de8ed2c`, pull request
   106) finds that purpose holds. The sentence needs rewording before the
   registration commit; that is the text's author's to fix and John's to
   approve, and this session did not edit version 5.
4. **The 2026-10-09 rulings file is not on the main line yet.** The new rows,
   the ledger's dated notes and the seven files' notes cite
   `docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md`, which is
   on branch `rulings-ledger-packet-2026-10-09` (pull request 144). The
   project's citation checker flags those citations until that pull request
   merges.
5. **Line numbers into the seven files shift by five.** Each note adds five
   lines under the title. Citations pinned to a commit are unaffected; any
   unpinned "line N" citation into those files is now five short. A search
   of every Markdown and TOML file found no unpinned line citation into
   them; the checks' own line citations (for example the version 2 check's
   "RT-256 at lines 77 and 91") are of the commit each check read.
6. **Files left alone, on purpose.** `STATUS.md` (line 259 cites the Gate C
   pass as "RT-256 to RT-273"; it is the running record, not a refounding
   record, and a note at its top would sit oddly there); `data/roadmap.toml`
   (its RT-256 is the decision-procedure finding); the earlier method and
   findings notes of the rows from entry 230 on and their check, which name
   both meanings deliberately while describing the collision; version 5, the
   2026-10-06 rulings, the registration handoff and the check of version 5,
   which all mean the decision-procedure finding. If John wants `STATUS.md`
   noted too, one line beside line 259 would do it.
7. **RT-212's closure leans on later rows.** The floor was checked in the
   form ruled on 2026-09-26 and, on the transplanted piece, under RT-230.
   Its final form (every read fitted on 1,800 development episodes, with the
   fitting step's limit raised to 10,000) is not yet measured; that is
   RT-240's open item, not a gap in RT-212's row.
8. **A reservation the numbering overran.** The ledger's numbering note of
   2026-09-25 said the adopted outside findings on the A3 closure text
   (Gemini G1 to G6, ChatGPT A1 to A15) would "take numbers after RT-211"
   when they get rows. The review of version 2 then used RT-212 to RT-229,
   and later passes ran on to RT-274, so those findings, which still have no
   numbers or rows, would now start at RT-275.

## What was not done

No review, ruling, check or registration text was edited beyond the seven
dated notes; no finding other than the records-not-on-the-branch one was
renumbered; no check was run. The rows are owed a check by a session that did
not write them (ruling 2 of 2026-10-09). One fix to this session's own new row
went in with this note: RT-213's row now gives the gate file's full path
(`experiments/rehearsal-successor-measure/out-v3-rules/gate.json`), which the
citation checker could not resolve from its bare name.
