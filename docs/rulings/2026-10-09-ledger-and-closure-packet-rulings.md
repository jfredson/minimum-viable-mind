# Rulings 2026-10-09: five decisions from the ledger rows and the closure checks

*Written 2026-10-08 (Thursday evening, Pacific) by a Claude Code session.
**A note on the date:** John's answer and this file are both of 2026-10-08,
Pacific time, the clock the commit carries. The "2026-10-09" in the file's
name and heading is the drafting session's error; the name is kept because
other records already cite it. Authorship:
**mixed** throughout. The session drafted each question and recommendation
from what the ledger-rows work (pull request 141), its check (pull request
143) and the closure check of the fatal flaw's repair (pull request 142)
turned up. John accepted every recommendation.*

## John's words

To the packet of five: **"As recommended"**.

## The rulings

| | What was asked | Ruled |
|---|---|---|
| 1 | Two findings carry red-team number 256: the decision-procedure finding (outside finding A2, fatal; numbered first, on 2026-10-06; cited 9 times in version 5 of the registration text) and the refounding check's missing-records finding (numbered 2026-10-07 from a copy that did not yet hold the first assignment) | **The decision-procedure finding keeps 256.** The missing-records finding becomes **RT-274**, the next free number, with a note in the ledger and in the refounding records that it was once also called RT-256 |
| 2 | Ledger rows 212 to 229 (the review of proposal version 2) are missing, though version 5 cites 16 of those 18 numbers | **Write them before the registration commit**, by the method of the rows from 230 on (`docs/2026-10-09-ledger-rows-method.md`), checked by a session that did not write them |
| 3 | The end-to-end test of the decision code (the made-up cases and the toy run that closed the decision-procedure finding) ran on the code of 2026-10-06, which the ruled changes of 2026-10-08 alter again | **Re-run it on the final registered code** once the code changes are checked, confirm every case lands on its term, have the run checked, and name it in the registration |
| 4 | Three serious findings are closed as "the argument was accepted" with no measured check, while the protocol (`docs/outside-review-protocol.md`, the closure rule) asks that a serious finding be checked or named as an open item in the registered text: the floor's missing condition (RT-238), the episode format (RT-239), control 6 (RT-251) | **One short check by a fresh session before the commit:** the floor's text against the code; the two self-tests against the registered episode description; control 6's withdrawn claim absent everywhere in version 5 |
| 5 | Eight ledger rows are open, though item 12 of the 2026-10-08 rulings asked that each be closed | **The four that bear on the registration** (the free model's gate, RT-237; the episode counts, RT-240; the decoy, RT-247; the outcome words, RT-250) **must close before the commit.** The four that belong to the refounding proposal (RT-263, RT-267, RT-269, RT-273) may stand open, named as open. The refounding's fatal finding RT-262 stays closed as accepted, with a note that a measured check is owed if that proposal's text goes toward the spec |

## What this does not do

It issues no go, spends nothing and registers nothing. The work it asks for
is done and checked by other sessions.
