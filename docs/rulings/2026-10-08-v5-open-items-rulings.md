# Rulings 2026-10-08: the open items of version 5 of the registration text

*Written 2026-10-08 (Thursday evening, Pacific) by a Claude Code session.
Authorship: **mixed** throughout. The recommendations were version 5's own
(section 21 of `docs/successor-experiment-proposal-2026-10-07-v5.md`), put to
John by this session as one packet in plain language, with two updated
against the main line as it stood that evening (items 10 and 12 below); John
accepted every one.*

## John's words

To the packet: **"Agreed on all."** To the follow-up on how to word the
confirmation of 2026-10-06 (item 2): **"1"**, choosing the first of three
drafted sentences (recorded in `docs/rulings/2026-10-08-flat-models-ruling-confirmed.md`).

The packet numbered its items 1 to 11 for reading. Below they carry version
5's own numbers (section 21, items 2 to 12), with the packet's number beside
each so the conversation can be matched to this file. Item 1 of section 21,
the bar for "the repaired route holds", was ruled earlier the same day
(`docs/rulings/2026-10-08-verification-bar-ruling.md`).

## The rulings

| Version 5 item | Packet item | What was asked | Ruled |
|---|---|---|---|
| 2 | 1 | The 2026-10-06 decisions on the two built models that lost their ownership route had no rulings file | **A dated file confirms them**, in the wording John chose: `docs/rulings/2026-10-08-flat-models-ruling-confirmed.md` |
| 3 | 2 | The exact words of the renamed outcome terms | **Adopted as drafted in section 3, with one change:** the eighth term becomes **"instrument returned no reading on the separable mechanism"**, replacing "instrument not validated", because "validated" is the word the 2026-10-07 refounding retired. R1, R2 and the fifth, sixth and seventh terms stand as drafted |
| 4 | 3 | Whether the scope phrases travel with the renamed terms | **Yes, kept.** "On these constructed systems, for this intervention procedure" follows every renamed term as before, including the eighth under its new words; "as a ratio of two transplants at the sites this procedure chose" follows "degree read" |
| 5 | 4 | The training recipe | **Confirmed as written** in section 5.5 (the frozen trainer's defaults, which the development runs used). The known cost, arm T's lookup damage after the learning-rate peak, stays named |
| 6 | 5 | Arm T's rerun failing | **A failure of arm T's rerun (its in-use check or its gate) also stops experiment C** at stop S4b, the same as arm C or arm M |
| 7 | 7 | The fitting step's iteration limit at 1,800 episodes | **Raise the limit to 10,000** in the frozen code, with the change to fitting on 1,800 of 1,980 episodes; re-run the page 4 measurement pass under it; have it checked by a session that did not run it; quote those figures. Before the registration commit |
| 8 | 8 | A ruled test of a differently coded decoy (weakness W18) | **Run it before the registration commit**: laptop only, $0, method written first, checked. If it cannot be done by 2026-10-18, register with W18 named and run it before step 5b |
| 9 | 9 | Three reporting changes | **Yes** to reporting arm T's row-choice split beside its gate. **Yes** to the summary saying "gate not decidable on one seed" rather than "failed its gate" when fewer than three seeds are in. **No, for now,** to storing arm M's per-step copy once on the model: it changes frozen code, and is taken up only if John asks for arm M's three runs to be cheaper |
| 10 | 11 | The registered commit of the frozen code, and the merges | **Yes, in this order.** The fifteen cited branches are already on the main line (pull request 136, 2026-10-08). The code changes ruled in items 7 and 9 land next; then section 7.4 names the main-line commit of `experiments/08-successor-degree/` as the registered code. That naming is the last step before John's registration commit |
| 11 | 6 | The launcher | **Confirmed:** the derived launcher `launch_successor.sh`, which the development runs ran, stands in the place of the parent launcher the ruling named |
| 12 | 10 | The red-team ledger's rows | **Write them before the registration commit**, from entry 230 on (the ledger on the main line carries no row for them; version 5, section 17, failure 4), each closed with "the claim was checked" or "the argument was accepted"; checked by a session that did not write them |

## What is now owed before the registration commit

Work these rulings ask for, none of it done by this file: the code changes of
items 7 and 9 (and, at the same time, the renamed outcome words of item 3,
which the code does not yet print; it still prints version 4's names); the
re-run of the page 4 pass under the new limit; the decoy test of item 8; the
ledger rows of item 12; a check of each by a session that did not do it; then
the naming of the registered commit (item 10). The closure check of RT-237,
the free model's gate, is owed separately, as before.

## What this does not do

It issues no go, releases no money and launches nothing. It does not register
anything: the registration is John's commit.
