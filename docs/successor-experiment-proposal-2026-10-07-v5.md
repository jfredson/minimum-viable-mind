# Successor experiment, proposal version 5: reading how much of the act is organised around who is acting

*Written 2026-10-07 (Pacific) by a fresh Claude Code session in its own
worktree (branch `worktree-agent-a43545d6649460124`, cut from the main line
at `597a3f5`, the merge of pull request 123, the outside-perspective poll).
**Status: the registration text, DRAFT, not yet checked, not yet committed as
registered. Nothing here binds until John makes the registration commit.** It
is version 4 (`docs/successor-experiment-proposal-2026-10-03-v4.md`, main
line at `41b0bd3`, pull request 85, left unedited) with every change John has
ruled since written in, each marked in a phrase with the ruling or finding it
comes from, and with the work those rulings asked for cited by file, branch
and commit. Its method, committed before any of it was drafted, is
`docs/successor-registration-method-2026-10-07.md`. No money is spent and no
machine is rented by this document.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30): the plain word before the term of art, and no bare
identifier anywhere. Every finding quoted from a record is labelled
**MEASURED** (a command was run and its output is filed in the record cited)
or **ARGUED** (reasoning a reader can dispute). Every number carries the
committed file it was read from. Figures from the arms whose training does not
reproduce are quoted with the caution
`docs/rulings/2026-09-23-range-and-direction-only.md` requires: they describe
the particular trained models on the record, not a property of the code.*

**What stands in front of the registration commit, in order.** (1) This
version is owed a check by a session that did not write it, under the pairing
rule of `docs/outside-review-protocol.md`. (2) The open items of section 21
are John's; each has a recommendation and the text says what it does
meanwhile. (3) The closure check of the fatal finding RT-237 (the free model's
gate named question sets this task does not have) runs on this text, by the
tier 1 reviewer, as the closure rule requires. (4) Every record this version
cites from an unmerged branch must be on the main line at the registration
commit: a registration may not rest on a record its reader cannot open at a
main-line commit (the citation defect RT-145 in the red-team ledger, the
finding that a registration commit rested on an uncommitted ruling file;
failure 4 of `docs/known-failure-modes.md`). Section 16 lists them. (5) The
registration commit is John's. **Kill date: 2026-10-18** (section 11).

**Three things a reader of version 4 should know first.** The outcome terms
are renamed to what they measure (section 3; John's ruling of 2026-10-07,
decision 3). The three built arms are now hand-set references: the number that
sets how decisive their built-in ownership answer is, the sharpness, is fixed
at 4.0 and not learned, after the four development runs at 10 million
parameters showed it driven to about zero in two of them; the amendment is
section 5.6, and whether the repaired route "holds" at 10 million is verified
before the free-arm run, with a stop if it does not. And the second release
of money is kept and conditional: asked for only after the first release ends
with the repaired route holding and the free model clearing its gate and its
floor, a pass being necessary and not sufficient (section 11; the same
ruling, decision 3 as revised). Since 2026-10-08 two more things: the bar
for "the repaired route holds" is ruled at 0.9 and 0.5 (section 5.6), and
an early stop at that verification is a registered ending of experiment C
with its own ruled sentence (stop S4b).

**Marking.** A passage marked *(ruled: ...)* comes from a rulings file that
records John's answer. A passage marked **[OPEN ITEM n for John: ...]** is
one no ruling settles; section 21 lists them all with a recommendation. A
passage marked *(carried from version 4)* is unchanged.

## What this version rests on

The first fourteen rows are new since version 4. **Ten of them sit on
fifteen branches that have not reached the main line**, and are cited by branch and
commit; each is marked "unmerged" and listed again in section 16. The
registration commit cannot be made until they are on the main line (the
header's point 4). Version 4's rows follow, unchanged except where a row's
standing has moved.

| Source | Main-line commit | Standing |
|---|---|---|
| **John's rulings on the two-sided question, 2026-10-07: decision 3 (experiment C's first release, the $1.14 repair as an amendment, the stop condition, the renamed outcomes), its revision later the same day (the second release kept and conditional) and decision 4 as revised (no new dates; the two kill dates stand)** | main line at `597a3f5` (pull request 123): `docs/rulings/2026-10-07-two-sided-question-rulings.md`; authorship mixed; owed a check | **Binding on this version.** The latest ruling on the shape of this experiment; where it and an earlier ruling disagree, it governs |
| **John's twelve-page ruling on the registration review of version 4, 2026-10-06, with its same-day follow-ups** (pages 1 to 12; the four wording fixes A7, A8, A11, A12; the scope phrases; the decision procedure A2; the generator self-test; the training exclusion) | **unmerged:** branch `rulings-2026-10-06-gate-a-v4` at `525a625`: `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`, with the two question packets and the two dispositions files it adopts (`docs/rulings/2026-10-04-successor-v4-gate-a-questions-PROPOSAL.md`, `...-dispositions-PROPOSAL.md`, `...-tier2-questions-PROPOSAL.md`, `...-tier2-dispositions-PROPOSAL.md`) | **Binding on this version.** Every page ruled in John's words, page by page; checked in pull request 104. Its ledger numbers RT-247 to RT-256 for the adopted outside findings are used here; the ledger rows themselves are owed |
| **The inside (tier 1) Gate A review of version 4, findings RT-237 to RT-246** | **unmerged:** branch `gate-a-tier1-successor-v4` at `135c1f7`: `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`, scripts in `reviews/2026-10-04-successor-v4-gate-a-scripts/` | One fatal (RT-237), four serious (RT-238 to RT-241), five worth-noting (RT-242 to RT-246); all ruled 2026-10-06. Its two decisive checks held: the rule written from version 4's text alone reproduces the code's choice on 24 of 24 toy rows, and the committed code re-run from clean reproduces 26,722 values with none different |
| **The two outside (tier 2) reviews of version 4**: ChatGPT (GPT-6 Astra), findings A1 to A13; Gemini 3.1 Pro, findings G1 to G9 | **unmerged:** branch `tier2-chatgpt-v4` at `6136407`: `reviews/2026-10-04-successor-v4-chatgpt.md`; branch `tier2-gemini-v4` at `8da74c4`: `reviews/2026-10-04-successor-v4-gemini.md` | Filed word for word. Gemini's nine repeat inside findings and, asked again, it found nothing new. ChatGPT's A2 (fatal), A6, A7, A9, A10, A13 (serious), A8, A11, A12 (worth-noting) are adopted as RT-256, RT-247, RT-251, RT-248, RT-249, RT-250, RT-252, RT-253, RT-254 |
| **The ruling packet on the two built models that lost their ownership route, and four fixes to the spending alarm** | **unmerged:** branch `ruling-packet-cm-flat` at `7583326`: `docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`; checked in pull request 112 | A PROPOSAL. Its option 1(b) plus option 4 (fix the sharpness at 4.0 in all three built arms; add an in-use check) and its page 2 (the alarm fixes) are reported as ruled on 2026-10-06 by the two method notes that did the work; **no rulings file records those words** (section 21, open item 2). The repair itself is ruled by decision 3 of 2026-10-07, which names it |
| **The check of the four development runs at 10 million parameters** (the flat ownership route in arms C and M; arm T's lookup confusion; the spending alarm that read 0.40 where the true figure was 0.99) | **unmerged:** branch `check-dev-10m` at `51ec07d`: `reviews/2026-10-04-development-runs-check-claude-code.md`, scripts beside it; the laptop procedure's rows in `experiments/08-successor-degree/out-dev-10m-check/` | MEASURED on the four real checkpoints. The source of every 10-million figure in sections 5, 11 and 12 |
| **The sharpness fixed at 4.0, the in-use check, and the toy retrain** | **unmerged:** branch `fix-sharpness-inuse-check` at `644238e`: `docs/2026-10-06-sharpness-fix-inuse-check-method.md` (committed first), `docs/2026-10-06-sharpness-fix-inuse-check-findings.md`, code in `experiments/08-successor-degree/src/`, outputs in `out-sharpness-fix/`; **owed its check** | The amendment of section 5.6 rests on it. Its concern 2 fired: the in-use check's second part fails every toy arm C and arm M seed before and after the fix (section 5.6; the bar ruled 2026-10-08, `docs/rulings/2026-10-08-verification-bar-ruling.md`) |
| **The page 4 toy re-run with every read fitted on 1,800 development episodes, and its check** | **unmerged:** branch `page4-toy-rerun-1800` at `e948899` (pull request 121): `docs/2026-10-06-page4-toy-rerun-1800.md`, outputs in `experiments/rehearsal-successor-measure/out-page4-rerun-1800/`; check on branch `check-page4-rerun` at `1e168f3` (pull request 122): `docs/2026-10-07-page4-rerun-check.md` | **Every toy read figure in this version is taken from this re-run**, as John's page 4 ruling requires and its findings direct. Checked: 40,855 values recomputed, none different; no toy decision moves |
| **The decoy test (page 10, finding A6) and its check** | **unmerged:** branch `decoy-test-a6` at `6794155` (pull request 108): `docs/2026-10-06-decoy-test.md`, `docs/decoy-test-method-2026-10-06.md`; check on branch `check-decoy-test-a6` at `ba5d64f`: `docs/2026-10-06-check-decoy-test.md` | Not fooled by an exact unused copy of the owner's marker, both ways round, reading 0.0000 on all six runs; reproduced exactly. The check adds that the test could not have failed, and that a differently coded decoy partly fools the read (0.23 to 0.29): weakness W18 |
| **The decision procedure brought to the 2026-10-06 rulings and run end to end on the toy and 25 made-up cases (outside finding A2, RT-256), with its two checks** | main line at `bd0de26` (pull request 105): `docs/2026-10-06-successor-a2-decision-procedure-method.md`, `docs/2026-10-06-successor-a2-decision-procedure-findings.md`, code `experiments/08-successor-degree/src/measure.py` and `procedure.py`, outputs `out-a2-cases/`; checks at `e6dd8fa` (pull request 107) and `f609c9d` (pull request 113) | 25 of 25 cases land on the term written for them in advance; every registered term reached; no withheld figure in any output. Rehearsal item R-13 |
| **The training stream leaves fresh and relaxed pairings out outright, and its check** | **unmerged:** branch `training-exclusion-pairing` at `9acc566` (pull request 115): `docs/2026-10-06-successor-training-exclusion-pairing-findings.md`, method first; check on branch `check-training-exclusion` at `7278309` | Ruled 2026-10-06 (follow-up item 8). 227 self-tests pass; the whole-pipeline test passes at both sizes; a replay of the development runs' stream finds 0 such pairings in 5,228,112 contents |
| **The four fixes to the spending alarm and its helpers, and their three checks** | **unmerged:** branch `tripwire-fixes` at `5e2faf9` (pull request 116): `docs/2026-10-06-tripwire-fixes-method.md`; checks on branch `check-tripwire-fixes` at `b01e564`: `docs/2026-10-07-tripwire-fixes-third-check-findings.md` | The amendment to section 12.5 rests on it. Third check: "ready to merge", eight runs of 82 checks all passing; one minor timing point left |
| **The code freeze of 2026-10-04** (`experiments/08-successor-degree/`, step 3 of section 11) and the four development runs' ledger rows | main line at `53ae82c` (pull request 97): `docs/2026-10-04-successor-code-freeze.md`, method `docs/successor-code-freeze-method-2026-10-04.md`; ledger rows at `865f108` (pull request 98) | The frozen code every registered run uses, as changed since by pull request 105 and the three branches above. Its section 4.1 (the toy is R3 under the rules as written) and 4.2 (no ruling set the training recipe) are both answered here (sections 3 and 5.5) |
| **The ruling of 2026-10-04 on the competing-solver run and the twenty-piece control (seven rulings), and the ruling of 2026-10-03 (night) on the check of version 4's two questions, with that check's thirty wording fixes** | main line: `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`; `docs/rulings/2026-10-03-version-4-check-questions-rulings.md`; `reviews/2026-10-03-proposal-v4-check-claude-code.md`, section 4; `reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`, section 7 | **Binding on this version.** Version 4 was filed before them; the inside review's table "The registration text as reviewed" lists each as ruled and not yet written. All are written in here |
| **John's ruling of 2026-10-08 on the bar for "the repaired route holds"** | main line (pull request 126): `docs/rulings/2026-10-08-verification-bar-ruling.md` | **Binding on this version.** The in-use check's bars 0.9 and 0.5 are ruled; open item 1 closed |
| **John's rulings of 2026-10-08 on the December-result restatement** | main line (pull request 128): `docs/rulings/2026-10-08-december-result-restatement-rulings.md`; the restatement itself, `docs/rulings/2026-10-08-december-result-restatement-PROPOSAL.md`, now a dated note at the head of `docs/december-result-roadmap-2026-09-20.md` | **Binding on this version.** The early stop of S4b is a registered ending with its ruled sentence; terms, kill dates and caps unchanged |
| Version 3 of this proposal | `6d4ec3a` (pull request 71): `docs/successor-experiment-proposal-2026-09-26-v3.md` | The text this version starts from. Left unedited |
| The first independent review of version 3, findings RT-230 to RT-236 | `4cb7f8e` (pull request 74): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`, with its scripts in `reviews/2026-10-03-successor-v3-gate-c-scripts/` | Reviewed version 3 at `37269ad`. Nothing fatal; two serious findings (RT-230, the floor certified the read and not the piece transplanted; RT-233, four controls had no figure under the registered rules); five minor |
| **John's rulings of 2026-10-03 on that review and on version 3's open decisions (sixteen pages)** | `56a5a86` (pull request 75), with a dated note added under its decisions table at `fe5df65` (pull request 77): `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` | **Binding on this version.** Its "What this changes, and where" is the first checklist this version was written to. Two rows of its decisions table (decisions 15 and 16) were changed later the same day by the ruling two rows below; the dated note says so |
| **The controls re-run under the registered rules, and its check** | re-run: `821f154` (pull request 76): `docs/2026-10-03-controls-rerun.md`, method `docs/controls-rerun-method-2026-10-03.md`, outputs `experiments/rehearsal-successor-measure/out-controls-rerun/`; check: `e184a6e` (pull request 79): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md` | **Every toy nomination, reading and control figure in this version is taken from this re-run**, under the rule that only a piece which itself carries the label at four fifths may be chosen. Checked by a session that did not run it: run again from the committed code, all 26 output files are equal value for value |
| **John's three rulings of 2026-10-03 after the controls re-run** | `fe5df65` (pull request 77): `docs/rulings/2026-10-03-controls-rerun-rulings.md` | **Binding on this version.** Control 2 kept as a reported description with no pass line; control 4 redefined and made a control that holds; the piece's accuracy at the other positions of its site reported, not gated |
| **The short pre-stated run** | method and code with no output: `9e978d9`; findings and outputs: `853988f` (pull request 80): `docs/2026-10-03-short-prestated-run-method.md`, `docs/2026-10-03-short-prestated-run.md`, outputs `experiments/rehearsal-successor-measure/out-short-prestated-run/` | The redefined control 4 as a pre-stated quantity, the new reported column for all twelve toy models, and one end-to-end run of control 2's code. **Checked by a second session (next row): run again from the committed code, its output files are identical byte for byte, and every figure in its findings matches them** |
| **The check of the short pre-stated run and of the evening ruling's record** | `53c8100` (pull request 82): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`, with its scripts in `reviews/2026-10-03-short-prestated-run-check-scripts/` | Both hold. Four notes for this version, all followed: say the too-early-position control compares the outputs at the two action positions; set out how the new column's two figures are computed and deal with the figure on the average moving by an episode; say that what the short run added for the other-agent control is the part of its code after the floor; say the piece's four fifths is established at the action position only. |
| **John's late-evening ruling of 2026-10-03 on this version's seven questions** | **filed with this version, pull request 83**: `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` | **Binding on this version.** The floor on the piece only; the piece rule after the layers are chosen; the laptop's processor; the toy's episode counts at full size; twenty random pieces for the other-agent control; two seeds of three when an arm's seeds disagree; the competing solver run before the registration review. Recorded by the session that wrote this version, and owed a check. **Read with the second record of the same evening, `docs/rulings/2026-10-03-version-4-questions-rulings.md`, which by John's ruling stands on the four points where the two differ (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`)** |
| The check of the two ruling packets of 2026-10-03 and their records | `f32ba0c` (pull request 81): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md` | No number in either packet is wrong; six places where a page says a little more or less than its source. Its section 7 lists what this version should and should not carry, and this version follows it |
| **John's evening ruling of 2026-10-03** | `f32ba0c` (pull request 81): `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` | **Binding on this version.** The fifth registered outcome is satisfactory and stated as weaker than R1; the new reported figure is printed both ways. The record is checked (the row above): it says what John's words say. On the one part that rested on implication, how the two figures are computed, John confirmed that evening in the words "Yes, section 4 of the method is what I meant"; the dated note recording that is beside item 3 of the ruling record |
| The Gate C tier 1 review of version 2, findings RT-212 to RT-229 | `c17dbdc` (pull request 56): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md` | Reviewed version 2 at `e88c3c0`; one fatal finding (RT-212, the empty read on the free arm), four serious, thirteen minor |
| John's rulings on that review | `3af189d` (pull request 60), refined at `4bb5727` (pull request 63), annotated at `da41c20` (pull request 68), and extended at `a11f1d3` (pull request 69, "RT-212 item 3 resolved"): `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` | **Binding on this version.** Its "What this changes, and where" is the checklist this version was written to; its three refinements after the toy re-run, the annotation of refinement 2's arm C clause, and the resolution of RT-212 item 3 after the label search are carried too |
| The five rehearsal-repairs rulings of 2026-09-25, with their annotations after the check | `62c3824` (pull request 53): `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` | Binding; read with the annotations |
| The rehearsal repairs, session (c), and their check | findings `882f252` (pull request 52): `docs/2026-09-26-rehearsal-repairs.md`; check `d216dbc` (pull request 58) | Checked: every verdict reproduces from the committed code; the decimals on arms C, F and M do not, as the 2026-09-23 ruling expects |
| John's rulings on version 3's decisions 20 and 21 | `9ed9f8c` (pull request 72): recorded in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` | Binding. Version 3 carried these from John's revision instruction because no ruling file held them yet; one now does |
| The toy re-run under the version 3 rules, and its check | findings `9d9d31a` (pull request 62): `docs/2026-09-26-toy-rerun-v3-rules.md`, Part 1; check `70be9fb` (pull request 65): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-toy-rerun-v3-rules-check-claude-worktree.md` | **Superseded on 2026-10-03 for every nomination, reading and control on arms C, F and M** by the controls re-run above, because the piece rule changes which sizes may be chosen. Still the source for three things: the label-permutation null beside the fit, the history of how the layer-0 and control 3 rules were clarified, and the fits as the laptop's graphics chip computed them (0.172, 0.067 and 0.106 on arm F). Arm T's figures reproduce exactly and are the same in every record |
| The thirty trained toy models | `8038275` (pull request 64) for the fifteen behind the repairs and the re-run, and `7ed2b0e` (pull request 67) for the other fifteen: `experiments/rehearsal-successor-measure/out-repairs/models/` (twenty-one) and `out-grammar-c/models/` (nine), with one `SHA256SUMS` covering all thirty | Committed, with each file's fingerprint; every toy result of 2026-09-25 and 2026-09-26 rests on them (section 10) |
| The grammar attempt (redesign (c)) and its check | attempt `ff778ea` (pull request 57): `docs/2026-09-26-grammar-attempt.md`; check `f1ea004` (pull request 61) | The pass line was not cleared; fallback (d) registers for the named-other condition (section 4.4) |
| The rented slice, second attempt, and its check | `9f802db` (pull request 51): `docs/2026-09-25-rented-slice-attempt-2-findings.md` and the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`; check `afb5183` (pull request 55) | Checked: every point passes, point 1 in part (the go was not compared with John's own message, which no committed file holds) |
| Version 2's failure-mode pass | `a3013be` (pull request 54): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md` | The author's run on version 2; this version's own run is section 17 |
| The Weekend 1 queue ruling (nine pages, 2026-09-25) | main line: `docs/rulings/2026-09-26-weekend-1-queue.md`; its check, `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-rulings-check-claude-worktree.md`, main line at `7c403b0` (pull request 78) | Ruled. Version 3 said the check of this ruling was still owed. The check had been written on 2026-09-25 and merged into a branch that never reached the main line; it landed on 2026-10-03 |
| The route (b) label search on the free arm, and its check | search: `a97c12b` (pull request 66): `docs/2026-09-26-free-arm-label-search.md`; check: `ecd2b6c` (pull request 70): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md` | Reported and checked: none of its three candidate reads clears the four-fifths floor on arm F, every figure recomputes, and John ruled on 2026-09-26 that the registration carries the fit floor alone (section 7.2, item 1). Version 3 cited both by branch; both are on the main line and are cited by their main-line commits throughout (the review of version 3, finding RT-236) |

---

## 0. The whole thing in eight sentences

The project's open question is one of degree: a small transformer that has
learned a causally load-bearing answer to "which agent am I" counts as a
centre at the bottom of the gradient, and what would separate it from a
centre in the fuller sense is how much of its act is organised around that
answer. Nobody has a measure of that. So the successor experiment builds
systems whose degree is fixed by how they are built, one where "which agent
am I" sits in a slot that can be swapped on its own, one where it is stirred
into everything, and one that is a mixture of the two by item, and one
ordinary freely trained system, and asks whether a candidate measure can tell
the built systems apart and place the mixture between them. The measure is:
transplant the part of the internal state that says who is acting from one
run into a matched run and see whether the action follows the transplanted
identity; compare that with transplanting the whole internal state at the
same places; the gap between the two, as a share of the room the whole-state
transplant had to move, is the reading. If the measure separates the two
built anchors at the ruled bar, the freely trained system gets a reading and
the project's current sentence "degree unmeasured" is replaced by a number.
If it does not separate them, that is a result too, and the measure is not
used. The reading is made only where the piece of the internal state that is
actually transplanted has been shown to hold its label, at a pre-stated
floor, so that an empty instrument returns *no verdict* rather than a number
at the entangled end; on the toy that is exactly what the freely trained
system returns, on every seed. And the admission that remains is narrower
than before: the toy can now tell an empty instrument from a ceiling, from a
number the procedure already computes, and what it still cannot tell is a
system that is entangled from one whose ownership answer lives somewhere the
read did not look. **Since version 4, two more things are true.** The built
systems are hand-set references: the number that makes their built-in
ownership answer decisive is fixed, not learned, because the first runs at 10
million parameters drove it to zero in two of the three and left them with no
built-in route to measure (section 5.6); whether the repaired route holds is
verified for about $1.14 before anything larger is spent, and if it does not,
the experiment stops there. And the outcome words say what the experiment
can show: an instrument that discriminates specified constructed mechanisms,
not a validated metric of degree (section 3).

---

## 1. Words used here, once

- **The programme.** Minimum Viable Mind, this repository. **MVM-0a** is its
  small-transformer build, registered 2026-08-07, whose Amendment A3 closed on
  2026-09-25 with the registered word *not testable*
  (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`, the closure
  block dated 2026-09-25).
- **Ownership.** Which of the several agents in a synthetic dialogue the model
  itself is. Nothing psychological is meant by the word; it names a fact about
  the episode that the model has to get right.
- **The acting channel.** The wire through which the model is told, at the
  moment it acts, that this turn is its own: a vector added to the model's
  input state at its own turns. Registered as Amendment A1 on 2026-08-09. It is
  the only honest source of ownership in this design, because in a dialogue
  where the turns are interchangeable, nothing in the text itself can carry it
  (the red-team finding that made this necessary is ledger item RT-17, the
  finding that any learnable ownership cue in the tokens is a fingerprint).
- **The injection, or layer 0.** The place the acting channel is added: the
  running state straight after the input embedding, before the first block.
  The transplant code counts it as layer 0. Section 7.2 removes layer-0 site
  sets from the candidate family wherever they span the turns the channel
  fires on.
- **The ownership answer.** A stored answer to "which of the agents am I" that
  later computation looks up.
- **The marker word.** The made-up name that stands for an agent in an episode.
  Marker words are drawn afresh every episode, so no name is permanently
  attached to any agent. **Which marker word is the model's own** is the label
  the ownership read is fitted against (ruled 2026-09-23,
  `docs/rulings/2026-09-23-nomination-label.md`).
- **The running state.** The vector a transformer carries forward from layer to
  layer at each token position, which everything downstream reads and writes.
  The technical name is the residual stream; it is used once more, in section
  6, and not again.
- **Transplanting (patching).** Taking the running state, or a part of it, out
  of one forward pass and putting it into another at the same place, then
  reading what the second pass does. The programme built this for the first
  time in the measurement rehearsal of 2026-09-21
  (`experiments/rehearsal-successor-measure/src/transplant.py`); nothing at
  the registered size has run it.
- **A fitted straight-line read (a linear probe).** A classifier fitted to the
  running state to predict a label, used here only to propose candidate places
  to transplant, never to conclude anything on its own.
- **The fit, and the fit floor.** How often a straight-line read names the
  model's own marker word correctly on held-out development episodes, stated
  as a count of those episodes (on the toy, of 180). Ruled 2026-09-26 (the
  rulings on the review of version 2, RT-212) and moved on 2026-10-03 from
  the whole read to the piece that is transplanted (next entry): a piece
  whose own count is below **four fifths** cannot be chosen, an arm and seed
  with no piece that reaches it returns *no verdict*, and both counts are
  printed in the reporting table.
- **The piece.** What the ownership-only transplant actually moves: the
  leading 1, 2, 4 or 8 directions of the read at each layer of the site set.
  The number of directions is the piece's **size**; version 3 called it the
  rank, and both words appear below for the same thing. **The piece's own
  accuracy** is the held-out count of a fresh read given only the state's
  coordinates inside the piece (section 7.2, item 3).
- **The label-permutation null.** The fit the same read reaches when the labels
  are shuffled, from two hundred shuffles at toy scale, reported beside the
  fit as its 95th and 99th percentiles. It is reported, not used as the bar.
- **The no-transplant rate.** The share of trials in which the model, with
  nothing transplanted, already gives the value the donor's identity would
  dictate. It is the quantity the chance-corrected form subtracts (section
  6.3).
- **The chance-corrected form.** The reading with the no-transplant rate
  subtracted from both the top and the bottom of the fraction, ruled as the
  registered form on 2026-09-25 (`docs/rulings/2026-09-26-weekend-1-queue.md`,
  page 2).
- **Arms.** The four trained systems being compared: the one built to keep the
  ownership answer separable (arm T, for tracker), the one built to entangle it
  (arm C, for the fuller centre end of the axis), the one built as a mixture of
  the two by item (arm M, for middle; section 5.3), and the ordinary freely
  trained one (arm F, for free).
- **The twenty-draw null (control 3).** Twenty random subspaces of the same
  rank at the same sites, each transplanted in place of the nominated one, so
  the reader can see whether the nominated directions do more than random
  directions of that size would. Reported, not gated (section 7.3).
- **Twins, and a twin's first own turn.** The two episodes of a matched pair
  (section 6.1). A twin's first own turn is the first position at which its
  acting channel is on. Control 4 is defined on the positions before both
  twins' first own turns (section 7.3, item 4).
- **The rider.** John's addition of 2026-09-25 to the reporting table: every
  arm is also read at arm T's nominated site set and rank, beside the reading
  at its own (the queue ruling, page 3).
- **The tripwire.** The billing check of section 12.5: two ratios, either at
  or above 1.25 halts the wave (the queue ruling, page 6, part 3). Since the
  development runs it reads every five minutes while a machine runs, not
  hourly, and every step that deletes a machine records the time (section
  12.5, as amended 2026-10-06).
- **The registered outcomes: R1 to R4, a fifth term, and three terms for the
  fallback and the unread separable model.** R1 to R4 were set by section 2
  of the December-result roadmap. The fifth was ruled on 2026-10-03. Three
  more were ruled on 2026-10-06 (the registration review, page 5), and on
  2026-10-07 John ruled that the words change to what they measure
  (`docs/rulings/2026-10-07-two-sided-question-rulings.md`, decision 3):
  "metric validated" becomes **"instrument discriminates specified constructed
  mechanisms"**, and the fifth term follows. All of them, old names beside
  new, are in section 3.
- **The sharpness, and the in-use check.** Every arm computes a built-in
  ownership answer from the acting channel: a running count of how often the
  "this turn is yours" signal fired on each agent's turns, turned into
  weights over the four agents by one learned number, the *sharpness*, which
  starts at 4.0. At 4.0 the answer puts nearly all its weight on the right
  agent; at zero it puts a quarter on each and says nothing. **In the three
  built arms it is now fixed at 4.0 and not learned** (section 5.6). The
  *in-use check* is the check that fails a built model whose route has gone
  flat anyway, in two parts: the answer is decisive, and the network uses it
  (section 5.6).
- **A hand-set reference.** What the three built arms are once the sharpness
  is fixed: systems whose ownership route is set by hand rather than left to
  training. The ruling of 2026-10-07 asks the amendment to say so in those
  words.
- **The first release and the second release.** The two blocks of money of
  the 2026-09-21 ruling, about $44 and about $150 to $172 (section 12). The
  second is kept and conditional on the first (section 11).
- **Gates A, B and C.** The three review points of
  `docs/outside-review-protocol.md`: registration, interpretation, and
  proposals that ask John for a ruling. Versions 1 to 3 of this document
  were Gate C material; this version is written as Gate A material.
- **Two phrases left from version 3, and what they mean here.** "The Gate C
  review" and "the Gate C rulings", wherever version 3's text is carried
  unchanged, mean the review of version 2 and John's rulings of 2026-09-26 on
  it. The review of version 3 and the rulings of 2026-10-03 are always called
  that. Likewise "the re-run findings at `9d9d31a`" is the earlier toy re-run
  of 2026-09-26, and "the controls re-run" is the one of 2026-10-03 that
  supersedes its figures for arms C, F and M.
- **Ledger items, written RT-nn.** Numbered red-team findings in
  `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`. Each one
  cited below carries a phrase saying what it found.

---

## 2. The question, and what this experiment is for

The question, from section 1 of the December-result roadmap, unchanged:

> Can a measure of how far an act can be pulled apart, validated on systems
> whose degree is known by how they were built, read the degree of a freely
> trained 30-million-parameter transformer that acquired a load-bearing
> ownership answer under task pressure? If so, what does it read?

Two things the question is not. It is not "is anyone home"; the founding wager
carries that step and no experiment here settles it. And it is not "tracker or
centre" as two kinds of thing; that was ruled one axis of degree on 2026-09-20
(`docs/rulings/2026-09-20-center-as-degree.md`).

What this experiment is for, stated so it can lose: **to deliver a measure, not
a verdict.** That is Stage 2 of `ROADMAP.md`, whose win condition is written in
the roadmap's own words as "deliver the metric, not a verdict", validated on
contrast cases where the answer is known by construction, with a loss condition
for "the metric cannot distinguish the known cases". This proposal supplies the
contrast cases and writes that loss condition down as outcome R2. **Whatever
it returns, experiment C is written up as instrument research** (ruled
2026-10-07, decision 3): what a specified intervention procedure does on
specified constructed systems, and not a measure of degree validated in
general.

The design is the one the outside reviewer named as the single experiment most
likely to change his view of the programme, the matched-role swap experiment
in section 5 of `docs/reviews/2026-09-20-program-review/response-chatgpt-astra.md`,
extended from two arms to four so the measure has a known case at both ends
of the axis and one in the middle.

**What Amendment A3 hands this experiment, in the words its closure block
registers** (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
the closure block dated 2026-09-25, and
`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`). Its outcome:
*not testable: the registered comparison was undefined for every possible
model; separately, removing the ownership-input channel reduced
primary-battery accuracy on all three trained seeds.* Three things the
successor inherits and must carry, from the block's "Successor" paragraph:
measuring the control's ceiling properly is a precondition of any successor
amendment; nothing counts as localized or as absent until both instruments,
probe and causal patching, agree; and the rehearsal requirement applies to
the successor in full. The block also says what may not be said: that the
ownership structure is absent, or that Amendment A3's nulls make it less
likely. Nothing in this proposal reads Amendment A3's checkpoints, and
nothing here reopens its closure.

**Non-binding motivation, from the Wittgenstein note (ruled 2026-09-25, the
queue ruling, page 7).** The TimeAssembler note "Wittgenstein criteria for the
Stage 2 metric" (document id `d08c23ae-7dca-4e55-9ac3-bb785ebed652` on the
Minimum Viable Mind project; a discussion note of 2026-09-22 that says of
itself "Nothing here is ruled or registered") proposes three tests. Its first
is the rationale this design already runs on, and John ruled that it goes
here, as motivation and not as a requirement: *an internal variable belongs
to the game only if intervening on it changes what the model does.* That is
why the measure is built on transplants rather than on how well a straight
line reads: a representation that a read recovers beautifully but that does
nothing when moved is, on this rationale, not part of the act. The fit floor
of this version is the other half of the same thought: a subspace nominated
by a read that never found its label is not a representation at all, and
transplanting it measures nothing. The note's own caution stands with it:
these criteria license claims about degree of participation, not a verdict on
inside experience. The note's second and third tests wait for resumption
after May 2027; the second is named on the weekend roadmap's extension list
so it is not lost. **Nothing in this paragraph is registered text, and no gate
reads it.**

---

## 3. What counts as a result

Reproduced from section 2 of the December-result roadmap, which John accepted
as the basis of this proposal (its dated head note of 2026-10-08 says what the
result means now that the measurement target has moved, and changes none of
the terms, kill dates or caps), with R4 restated to the ruling of 2026-09-21
(item 23 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`), with
the fifth term John ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11), with the
three terms John ruled on 2026-10-06 for states the registered runs can reach
and nothing named (the registration review, pages 5 and 9, closing the
inside review's finding RT-241, the outcome-map finding, and the outside
review's A10, adopted as RT-249), **and with every term renamed to what it
measures, as John ruled on 2026-10-07** (`docs/rulings/2026-10-07-two-sided-question-rulings.md`,
decision 3: "metric validated" becomes "instrument discriminates specified
constructed mechanisms", and the fifth term accordingly). The registered
wording is the wording in the "Registered term" column; the name version 4
used is beside it so a reader of the earlier record is not lost; nothing in
this document may report an outcome in other words.

**[OPEN ITEM 3 for John: the ruling renames "metric validated" and says "the
fifth term accordingly". The exact words of the renamed fifth term, of R2 and
of the three terms of page 5 below are this session's drafting and are yours
to set.]**

| Outcome | Registered term | Version 4's name | What it means | Satisfactory |
|---|---|---|---|---|
| **R1** | **instrument discriminates specified constructed mechanisms, degree read** | metric validated, degree read | The measure separates arms T and C at the pre-stated bar (section 9: 0.5 on the chance-corrected form), and arm F gets a reading with its spread across seeds. The closure sentence "degree unmeasured" is replaced by a number, stated as where arm F sits against the three anchors on this measure (weakness W1). | Yes |
| **R2** | **instrument does not discriminate the specified constructed mechanisms** | metric does not separate | Arms T and C pass their gates and do not separate at the bar; arm F is not read, whether or not it passed its gate at step 5b. The result is that this candidate does not read degree on this substrate, and the registered design says what to try next. | Yes |
| **R3** | **substrate not a testbed** | (unchanged) | Arm T or arm C fails its gate after the one permitted re-run, or arm F fails it at step 5a after its re-run. Reading: this recipe and this size are not yet a place to study mechanism. Resumption starts from a size or recipe change. The sentence names the arm, the condition and the seeds that failed. | Yes, if the gate was reached |
| **R4** | (none) | (unchanged) | The programme hibernates with a registered design and a rehearsal only. **Since 2026-09-21 a missed kill date does not put the roadmap here by itself**: registration after 2026-10-18, or launch of the remaining registered runs after 2026-11-01, is still possible on a fresh ruling that names what comes off the back end to make room, and R4 is where the roadmap lands only if that ruling says it is not worth it (item 23 of the 2026-09-21 ruling; section 5 of `docs/december-result-roadmap-2026-09-20.md`). | No. Recorded as a schedule failure, not a scientific one |
| **The fifth term** | **instrument discriminates specified constructed mechanisms, degree not read** | metric validated, degree not read | Arms T and C separate at the pre-stated bar, and arm F returns no verdict, fails its channel-removal check (section 8.2), or, having passed its gate at step 5a, fails it at step 5b. Reported in those words with the reason after a colon. The instrument is delivered and shown to discriminate on the built systems; the freely trained system is not read with it. | **Yes, and stated as weaker than R1** (ruled 2026-10-03 in John's words, "Yes, satisfactory and weaker than R1") |
| **The sixth term** (new, page 5) | **instrument checked against the separable mechanism only, degree read** | metric checked against the separable model only, degree read | Arm C returns no verdict (the two-model fallback accepted in advance on 2026-09-20); arm T reads; arm F reads. Arm F's figure has no upper reference. | Yes, stated as weaker than R1 |
| **The seventh term** (new, page 5) | **instrument checked against the separable mechanism only, degree not read** | metric checked against the separable model only, degree not read | As the sixth, with arm F returning no verdict or failing its channel-removal check; the reason after a colon. | Yes, stated as weaker than the sixth |
| **The eighth term** (new, page 5) | **instrument not validated** | metric not validated | Arm T, the model built to be easiest to read, returns no verdict; the reason after a colon (a control that holds failed, a floor missed, the built route not in use). The measure did not return a reading on its easiest case. | No |

**Scope, fixed with the terms (ruled 2026-10-06, page 11 and follow-up items
2 and 7, closing the outside review's A13, adopted as RT-250).** Wherever a
term containing "instrument discriminates", "instrument checked" or "instrument
not validated" appears,
in this text, `STATUS.md`, the paper or in public, it is followed in the same
sentence by **"on these constructed systems, for this intervention
procedure"**; so is R2. "Degree read" is followed by **"as a ratio of two
transplants at the sites this procedure chose"**. No result here establishes
a scale of integration, consciousness, selfhood or general agency. The table
of tempting summaries against what can be said is in section 13.
**[OPEN ITEM 4 for John: the scope phrases were ruled for the old names;
whether they still travel with the renamed terms, or the renaming makes them
unnecessary, is yours. This text keeps them.]**

**Every state the registered runs can reach, and its registered term (ruled
2026-10-06, pages 5 and 9 together, in John's words "accept all, go with the
recommendations"; closing RT-241 and A10).** A seed counts only if it passes
every condition of its arm's gate and every check that withholds a reading,
and returns a reading; an arm passes its gate if two or more seeds each pass
every gate condition, and is read if two or more seeds count; it returns no
verdict, as an arm, if two or more seeds do (page 7, below). Rules are
applied in this order.

1. **The gate on learning comes first.** If arm T or arm C fails its gate
   (section 8.1), after the experiment's one permitted re-run where it is
   still available (rule 3), or arm F fails its gate at step 5a after its
   re-run (section 11, stop S4), the outcome is **R3**, naming the arm, the
   condition and the seeds. **Arm M is the exception:** if it fails its gate
   it is dropped and carried as an extension, exactly as a no verdict on it
   is. **Arm F is the exception after step 5a:** if it passed at step 5a and
   its arm fails the gate at step 5b, with arms T and C learned, that is a no
   verdict on arm F with the reason "failed its gate on learning", and the
   readings decide (page 9).
2. **Otherwise, the readings decide:**

| Arm T | Arm C | Arms T and C separate (section 9)? | Arm F | Registered term | Satisfactory |
|---|---|---|---|---|---|
| reads | reads | yes | reads | **R1** | Yes |
| reads | reads | yes | no verdict; or fails the channel-removal check of section 8.2; or, having passed at step 5a, fails its gate at step 5b | **the fifth term**, with the reason after a colon | Yes, weaker than R1 |
| reads | reads | no | (not read) | **R2** | Yes |
| reads | no verdict (the fallback) | (cannot be asked) | reads | **the sixth term** | Yes, weaker than R1 |
| reads | no verdict (the fallback) | (cannot be asked) | no verdict, or fails the channel-removal check | **the seventh term**, with the reason after a colon | Yes, weaker than the sixth |
| no verdict | any | (cannot be asked) | (not read) | **the eighth term**, with the reason after a colon | No |

Arm M never changes the term. It is reported against its band if it reads;
if it returns no verdict or fails its gate it is dropped, said by name, and
carried as an extension. **If arm M reads and misses its prediction (section
9), the report says so in the sentence that carries the term, with the
figures, and arm F's figure is placed against arms T and C only** (page 9,
part 2). R4 is unchanged.

3. **The experiment has one permitted re-run** (item 19 of the 2026-09-21
   ruling), held in the first release. It goes to the first registered run
   that fails its gate on learning: to arm F at step 5a if it fails there; if
   step 5a does not use it, it is held for step 5b and goes to the first run
   of arms T, C or M that fails, on John's go naming it. Once used, a later
   gate failure gives its outcome under rule 1 with no re-run.

**The decision procedure that applies these rules has run end to end before
registration** (rehearsal item R-13, section 10): on the toy's committed
records and on 25 made-up cases, each landing on the term written for it in
advance, with every term above reached and no withheld figure in any output
(MEASURED: `docs/2026-10-06-successor-a2-decision-procedure-findings.md` at
`bd0de26`, from `experiments/08-successor-degree/out-a2-cases/results.md`;
checked at `e6dd8fa` and `f609c9d`).

**What a no verdict does not mean (ruled 2026-10-06, follow-up item 1,
closing the outside review's A11, adopted as RT-253).** It means this
registered procedure did not return a reading, for the stated reason. It
does not show that the arm has no ownership representation, that its
representation cannot be separated, or that another instrument could not
read it. The registered search has limits that can produce it on a model
with a recoverable representation: the nomination order, the rank cap of 8,
the fitting sample, the fresh-episode floor, the gates and the seed rule.

**Arm F may return no verdict, and the registration says so in advance (ruled,
the rulings on the review of version 2, RT-212, items 1 and 3; the floor
moved to the transplanted piece by the rulings of 2026-10-03, page 1).** A
reading is made on an arm only where some size of the piece that would be
transplanted clears the fit floor of section 7.2 on held-out development
episodes. On the toy the free arm never did: its best piece, at any layer and
any size on any seed, is right on 34 of 180 held-out episodes against 144
needed, and its whole read is right on 32, 12 and 18 of 180 at the layers the
rule would otherwise choose (MEASURED: `docs/2026-10-03-controls-rerun.md` at
`821f154`, sections 1 and 3, from
`experiments/rehearsal-successor-measure/out-controls-rerun/nominate_F_seed*.json`,
computed on the laptop's processor). The earlier run, on its graphics chip,
gave 31, 12 and 19, which is the 0.172, 0.067 and 0.106 that version 3 quoted
(`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section 1.3;
section 7.2, item 1, says which device's figure is registered). So the toy
record for arm F is **"no verdict, read failed its
floor"** on every seed, and version 2's toy reading for arm F at the
entangled end is withdrawn from the record under failure 2's own rule (the
pre-stated target changed before registration, so the null already collected
is withdrawn rather than reported). **At registered scale the same can
happen, and the first release is the test of it** (John's ruling of
2026-09-26 on the route (b) result, the rulings file at `a11f1d3`, "RT-212
item 3 resolved", item 5; section 7.2, item 1): the single arm F run of step
5a has its nomination reported against the floor before the second release
is asked for, and a miss is a stop there, beside the learn-both stop (section
11). **If arms T and C separate and arm F returns no verdict, the outcome is
the fifth term, "instrument discriminates specified constructed mechanisms,
degree not read", with its reason after a
colon; it is not reported under R1** (ruled 2026-10-03, page 11, item 3). The
route (b) investigation, which looked for a label the own-directed loss does
force on a free system, found none that clears the floor at toy scale
(section 7.2, item 1), so this version registers with the fit floor alone and
with the ruled label as its one registered read. **The stop after the first
full-size free-model run is unchanged by the fifth term: a miss of the floor
there still goes to John before the second release** (page 11, item 6), and
whether the remaining runs are worth that release is his call with the
registered-size figures in hand.

**The admission (rewritten in version 3 from the ruling on RT-212; reworded
here to say what was measured, as the rulings of 2026-10-03, page 1, item 2,
direct).** Version 2 admitted that a free-arm reading at the entangled anchor
could not be told from the instrument's ceiling, because the chance-corrected
form reads 1 both when the act is entangled and when the nominated subspace
carried nothing. **The toy can tell those two apart, from a number the
procedure already computes**: the accuracy of the piece that is transplanted.
A piece right on 34 of 180 carried nothing, and the fit floor says so before
any transplant is looked at. On arm C, **the read holds the label; the
largest piece transplanted holds it; and no size of piece moves the action.**
In figures: the whole read is right on 180, 177 and 176 of 180 at the chosen
layers on seeds 0, 1 and 2; the chosen pieces, of 8, 8 and 4 directions, are
right on 180, 172 and 150 of 180 at the action position; and the
ownership-only transplant of those pieces lands at 0.0488, 0.0525 and 0.0612
against a no-transplant rate of 0.0512, 0.0488 and 0.0600 (MEASURED: the
controls re-run at `821f154`, section 2, from
`out-controls-rerun/measure_C_seed*.json`; "no size moves the action" is the
review of version 3, RT-230, which read arm C between 0.9897 and 1.0051 at
every size on every seed, at version 3's site sets). That is what "entangled
at these sites" means. **That is a statement about this instrument at these
sites, not an independent certificate of arm C's degree** (ruled 2026-10-06,
page 10, closing the outside review's A6, adopted as RT-247): arm C's high
status rests on its construction and on the instrument finding no piece that
moves the action. A model with a readable but unused copy of its marker and a
separate ownership variable the action uses would read the same way
(weakness W12; the decoy test of section 10, R-12, and weakness W18). **And
at 10 million parameters arm C's construction did not hold**: its built-in
ownership answer went flat and the procedure found no readable ownership in
its running state at all (section 5.6), so what "entangled by construction"
means now rests on the repaired, hand-set arm. Version 3's sentence here, that a subspace nominated
by a read at 0.96 or better "held the label and still moved nothing", claimed
more than was measured: on two seeds of three the piece it transplanted held
the label at 0.544 and 0.306 (the review, RT-230), and it is replaced by the
sentence in bold above.

**The piece's four fifths is established at the action position only.** Where
a site covers several positions, the same directions are transplanted at
every one of them, and away from the action position the piece often falls
below four fifths. On arm C seed 1 it is right on 139, 139 and 33 of 180 at
the three positions before the action; on arm C seed 2 it is below 144 at all
ten positions reported, from 30 to 139, and 123 on the average over the other
positions; on arm M it clears on the average on every seed (163, 174 and 175)
and misses at six, six and three of the ten positions reported. The whole
state at those positions holds the label throughout (149 to 180 of 180 on the
built systems), so the label is there and is not held in the chosen
directions (MEASURED, **checked: the check of the short run at `53c8100`**:
`docs/2026-10-03-short-prestated-run.md` at `853988f`, section 4, from
`out-short-prestated-run/part_b.json`). So "the piece held the label and the
transplant of it did nothing" is true at the action position and is not shown
across the whole site. John ruled that this is reported in the registered
table both ways and gated in neither
(`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3;
`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling
2); it is weakness W13.

What the admission that remains says (ARGUED): a piece that clears the floor
shows the label is present in those directions at the action position; it
does not show that the directions it found are the ones the act uses. A free
arm whose piece clears the floor and whose reading is near 1 is therefore "as
entangled as the built anchor at the sites this procedure nominates", and no
more; that the ownership answer lives in some other part of the state the
read did not find is not excluded. Arm M (section 5.3) is a known case in the
middle of the scale, so that a free-arm reading can be placed against three
anchors rather than two. It does not remove that residual admission, because
arm M's known degree is a mixture by item, and a free arm's partial
separation, if it has any, would be within each trial (section 5.3).

**The toy outcome, on the anchors' terms (ruled, the rulings on the review of
version 2, RT-213, item 1; corrected here by the code freeze's finding and the
ruling of 2026-10-06, page 9).** Version 4 said the toy reaches the fifth
term. Applied as the code applies them, the rules put the toy on **R3,
"substrate not a testbed"**, because the free model fails its learning gate
(the named-other condition clears on one seed of three), and R3 covers an arm
that fails its gate (`docs/2026-10-04-successor-code-freeze.md`, section 4.1,
MEASURED on the frozen code; the outside review's A10 found the same
conflict). Under the rule John ruled on 2026-10-06 (page 9), **the toy's
outcome depends on which seed is taken as the step 5a run**: the fifth term
if seed 0 (which passes both learning conditions) is taken as the run trained
alone at step 5a, and R3 if seed 1 or seed 2 is. The decision procedure
lands exactly there on the toy's committed records (cases 1 to 3 of R-13:
R3 as the toy actually is, the fifth term with seed 0 as the step 5a run, R3
with seed 1; MEASURED: `docs/2026-10-06-successor-a2-decision-procedure-findings.md`
at `bd0de26`). So the toy sentence is: **the anchors separate, the middle
model reads in its band, the free model is not read, and the registered
outcome is the fifth term or R3 according to which free-model seed stands
for the step 5a run.** The anchors' figures, with every read fitted on 1,800
development episodes (ruled 2026-10-06, page 4): arm T reads 0.0000 and arm C
**1.0026, 1.0000 and 1.0000**, so the separation, the lowest of arm C minus
the highest of arm T, is 1.0000 and clears 0.5; arm M reads 0.5252, 0.4793
and 0.5208, inside its band on every seed; and arm F returns no verdict on
every seed, twice over, because it fails its gate and no piece of its read
reaches the floor (best piece 40, 19 and 36 of 180 against 144; MEASURED:
the page 4 re-run at `e948899`, section 2, from
`out-page4-rerun-1800/models-1800/summary.json` and `comparison.md`; checked
at `1e168f3`, 40,855 values recomputed, none different). At the earlier
fitting count of 420, arm C read 1.0051, 0.9926 and 0.9974 and arm M 0.4886,
0.4860 and 0.5449 (the controls re-run at `821f154`); the chosen site set or
size moved on five models of fifteen when the fitting count changed, as the
page 4 method said it might (section 7.2, item 3). **The toy record is
development evidence, not an untouched test of the frozen procedure**
(section 10; the outside review's A8, adopted as RT-252). Arm C's named-other
condition fails on every toy seed, at 760, 751 and 708 correct of 3,000
against a bar of 790 (MEASURED: `out-repairs/gate_base.json` at `882f252`;
the review of version 2, RT-213); under version 2's rules that made the toy
an R3, and under this version's it does not, because the constructed arms
are gated on the own-directed condition only (section 8.1) and their reading
uses only the own-directed action. **Version 2 left that failure out, and
this version states it wherever arm C's toy record is quoted** (sections 5.2,
10 and 11). **One more caution on the toy record, new in this version:** the
twelve committed toy models were trained with the sharpness learned; the
registered built arms have it fixed (section 5.6). Nine toy models retrained
with it fixed learn the task as well (no seed lost more than 36 of 3,000
own-directed answers), but only arm T seed 0 of them has been re-read, at
0.0000 as before; the other eleven re-reads are owed (section 5.6).

**The honest prior, stated before the work rather than after it.** On the
existing record the most likely outcome at registered scale is that **arm F
returns no verdict, or fails its gate**, and the most likely reason for either
is the named-other half of the task and the read that cannot find its label.
Three seeds of the closed Amendment A3 design failed to learn a named-other
query battery, landing at 0.2877, 0.3057 and 0.3195 against 0.3227 for a
solver that cannot read the name the question supplies; a fourth run with the
battery's own loss term reached 0.3125 and changed nothing
(`control-learnability-pilot-findings.md`, the pilot findings file; ledger
items RT-52 to RT-69). This experiment moves the named-other condition from a
query at the end of the episode to an action at the model's own turn. **At toy
scale that has not been enough, and every repair tried has now been tried and
failed** (section 4.4): the named-other condition failed its bar on two of
three toy arms; doubling the training budget did not fix it; a curriculum and
loss re-weighting did not fix it; and the grammar change, redesign (c), did
not fix it either, at 774, 730 and 759 correct of 3,000 on the free arm
against 790 needed on two seeds (MEASURED: `docs/2026-09-26-grammar-attempt.md`
at `ff778ea`, section 3; its check at `f1ea004` re-ran it and got 750, 809 and
739, so at most one seed of three clears on either run). Fallback (d)
registers. Section 11 places a stop before the expensive wave so that a
gate failure on arm F costs the first release (about $44, section 12.3)
rather than the whole plan; **a failure on arm C, the high anchor, is first
seen in step 5b, after the second release is drawn, and section 11 states
that cost.**

**What a no verdict maps to** is the table at the head of this section
(ruled 2026-10-03, page 11, for arms C, M and F, closing the no-verdict
finding RT-182 of the review of version 1; completed for every arm on
2026-10-06, pages 5 and 9). An arm's *no verdict* is reported in those two
words with its reason after a colon, as the re-run's table does ("no verdict:
read failed its floor"). In short: no verdict on arm C fires the fallback
(the sixth or seventh term); no verdict on arm M drops arm M; no verdict on
arm F after arms T and C have separated is the fifth term; no verdict on arm
T is the eighth term. **New since version 4:** a built arm whose ownership
route has gone flat returns no verdict for that seed with the reason
"construction did not hold" (the in-use check, section 5.6), and that no
verdict maps as any other does.

**When an arm's three seeds disagree: a seed counts only if it passes
everything (ruled 2026-10-06, page 7, closing the outside review's A10,
adopted as RT-249; amending ruling 6 of 2026-10-03, late evening, in both its
records).** The floors and the controls that hold apply per arm and seed
(section 7.2, item 1), so an arm can read on two seeds and return no verdict
on the third. A seed counts only if it passes every condition of its arm's
gate and every check that withholds a reading, and returns a reading; an arm
passes its gate if two or more seeds each pass every gate condition, and is
read if two or more seeds count; separate two-of-three counts per condition
are not used. Every seed is printed, whichever way it went. The reason
recorded: under separate counts an arm could pass with no single seed passing
everything; the frozen code of 2026-10-04 had 18 patterns of 512 in which
only one seed passed everything and the arm still passed (MEASURED by the
check of the outside dispositions, pull request 102; closed by the decision
procedure of pull request 105, whose cases 10 to 12 land those patterns on
the fifth term, not R1). **The separation is not compared seed by seed**
(ruled 2026-10-03, night, record B ruling 6; the reconciliation): it is the
lowest reading among arm C's seeds that read, minus the highest among arm
T's seeds that read, and it must be at least 0.5; seeds are not paired by
number. The rule forgives a seed that returns no verdict and does not forgive
a seed that returns an odd reading (the check-questions ruling of 2026-10-03,
ruling 2). "Instrument discriminates specified constructed mechanisms" means
arms T and C each read on at least two seeds and that separation clears;
"degree read" means arm F reads on at least two seeds; if arm F reads on one
seed only, the outcome is the fifth term and that seed's figure is printed as
a description. **On the toy, with every read fitted on 1,800 development
episodes (section 7.2, item 1), that separation is 1.0000** (arm C reads
1.0026, 1.0000 and 1.0000; arm T 0.0000 on every seed; MEASURED: the page 4
re-run, `docs/2026-10-06-page4-toy-rerun-1800.md` at `e948899`, section 2,
from `out-page4-rerun-1800/models-1800/summary.json`; checked at `1e168f3`).
At the earlier fitting count of 420 it was 0.9926 (the controls re-run at
`821f154`). On the toy every arm behaves alike on all three seeds, so the
seed rule has been exercised only on made-up cases (R-13), not on a real
split.

---

## 4. The task: matched-role revisions

### 4.1 What the model does

**The episode format, registered in full (ruled 2026-10-06, page 3, closing
the inside review's RT-239, the unstated-grammar finding; the outside
review's A5 and G3 repeat it).** The registered generator is the rehearsal's
grammar, `experiments/rehearsal-successor-measure/src/grammar.py`, at its
sizes, as carried into the frozen code
(`experiments/08-successor-degree/src/grammar.py`). It is **not** an
extension of the closed design's generator
(`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py`), which
has twelve turns, four revision turns and the end-of-episode question sets
the closed design called batteries; none of those is carried. One episode has
four agents, two items, eight value slots and a closed vocabulary (twelve
marker words and five items in the training, development and fresh pools; 56
tokens). **Eight assignment turns**, one per agent and item, in random order,
rendered as the marker word, the word "assign", the item and the value;
within an item the four values are distinct, except in the collision set for
control 6, where two agents share a value on one item (section 4.2). **Two
action turns**, last, in random order, rendered as the act word, the word
"revise", the who-word, the item, the answer cue and the mask word: on the
own-directed action the who-word is the special word meaning "your own", and
on the named-other action it is the named agent's marker word. The correct
answer is the successor of the relevant earlier value, counted round the
eight slots.

**Two departures from the closed design's grammar, both deliberate.** (1)
**The action turn carries no marker word of the model's own.** The closed
design renders the acting turn with the actor's own marker three tokens
before the action, and its own header names the consequence: a model can
read a name badge at act time rather than carry a binding. Here the only
route to the ownership answer is the acting channel (section 1). (2) **The
answer is never shown**: its slot is the mask word, and the prediction is
read there. Together these make the two episodes of a matched pair
**token-for-token identical**, differing only in which positions the acting
channel fires on (section 6.1). **The registered generator's self-test
asserts both** (the checks named "matched pairs are token-for-token
identical" and "no name badge", the second saying that the own-directed turn
shows only the self word; `grammar.py --self-test`), and that self-test runs
on the built generator at section 11, step 3 (MEASURED: it passes in the
freeze's 195 checks and the training-exclusion branch's 227;
`docs/2026-10-04-successor-code-freeze.md`, section 3, test T1;
`docs/2026-10-06-successor-training-exclusion-pairing-findings.md` at
`9acc566`, section 3). **Three more lines of that self-test are registered:**
no fresh or relaxed episode's pairing (its table of which marker holds which
value on which item) occurs in the training stream, in the stricter reading
that checks the pairing and not only the whole episode (ruled 2026-10-06,
follow-up items 4 and 7, RT-255); the training stream refuses any such
pairing outright, whatever its turn order (ruled 2026-10-06, follow-up item
8; section 7.1); and on every matched pair the donor's dictated answer is
computed from the donor's own identity and value on the named item and
differs from the recipient's except in the relaxed set's same-value trials
(ruled 2026-10-06, page 8; section 6.4, item 3).

The change is that the model now acts in **two matched roles at the same kind
of position**:

- **Own-directed revision.** The model's turn arrives; the correct output is
  the successor of **the model's own** earlier value on that item.
- **Named-other-directed revision.** The model's turn arrives carrying a
  marker word; the correct output is the successor of **the named agent's**
  earlier value on the same item.

Both are actions on the model's own turn, supervised the same way, scored the
same way. This is the whole point of the redesign: in the closed Amendment A3
design the ownership condition was an action and its comparison condition was a
question asked at the end, so the two were never at the same kind of position,
which is the defect the outside review called out and the internal requirements
document had already ranked first for repair.

**The grammar is as version 2 had it, now written out above.** The grammar
change attempted on 2026-09-25 (redesign (c), section 4.4) did not clear its
pass line, so nothing in the format changes; in particular the acting channel
fires on both action turns, as before.

### 4.2 What "matched difficulty" means, concretely

Four things are matched, by construction in the generator and checked at the
rehearsal (MEASURED on the toy grammar: the four matched properties hold,
`docs/2026-09-21-successor-measure-rehearsal.md`, check P-1 and rehearsal item
R-1; re-checked on 3,000 matched pairs under the grammar attempt's setting
too, `docs/2026-09-26-grammar-attempt.md` at `ff778ea`, section 2):

1. **Candidate count.** In both conditions the item has been assigned by all
   four agents, so four earlier values are in the context. A solver that cannot
   tell which agent the answer belongs to can do no better than one in four.
   Random guessing over the eight slots is one in eight. Both numbers are the
   same in both conditions.
2. **Distance.** The number of turns between the source assignment and the
   action, and the number of intervening turns by other agents, are drawn from
   the same distribution in both conditions.
3. **Supervision.** Equal numbers of supervised action positions of each kind
   per episode, equal loss weight per position, one scored token per position.
4. **Transformation.** The same successor rule in both conditions, so nothing
   about the arithmetic differs.

**The asymmetry that cannot be matched, stated rather than hidden.** In the
named-other condition the identity of the source agent is a token in the input;
in the own-directed condition it is not, and cannot be, because a dialogue with
interchangeable turns carries no honest ownership signal in its text (ledger
item RT-17). So one condition reads its answer's owner and the other has to
have carried it. That asymmetry *is* the experiment; removing it would mean
putting the model's own name in the text, which would reintroduce the very
leak the acting channel was built to avoid. It is recorded here, will be
recorded in the registration text, and bounds what a difference between the two
conditions may be read as. **Ruled 2026-10-03 (decision 9): it is recorded as
a known limitation and not engineered away.**

**Distinctness, and the one place it is relaxed.** Within an item the four
agents' values are distinct, drawn without replacement (MEASURED on the
rehearsal grammar: `experiments/rehearsal-successor-measure/src/grammar.py`,
the function `_content`, draws the four values with `replace=False`, and the
matched-property check counts four distinct candidate values on every item).
Sections 4.2, 6.1 and 8.1 lean on that. Control 6 in section 7.3 needs its
negation for one of its two cells, so control 6 runs on a **separately
generated relaxed set** in which one item per episode has two agents sharing
a value (the same file's `collide` option), labelled as such wherever it
appears. The relaxed set is never used for the reading, the gates or any
other control. Section 7.3 gives the trial counts that set produces.

### 4.3 Carried-forward rules that apply to the new generator

- **The even-split rule.** Any batch fraction that splits rows by condition must
  give an even number of rows, or the split cuts the generator's matched content
  pairs. Measured and recorded 2026-09-20 as ledger item RT-58 (the batch-split
  bias check). The rehearsal grammar carries it (`grammar.py`, the function
  `_check_even_split`).
- **The one-scored-token self-test.** The check that exactly one token per
  supervised position is scored, and that the check survives the shift the loss
  function applies: ledger item RT-59, which turned out to need more than the
  one line it was first written as. It runs on every generator build.
- **The pairing exclusion in training (ruled 2026-10-06, follow-up item 8,
  "(a), go with the recommendation").** The training stream refuses any
  episode whose pairing, the table of which marker holds which value on
  which item, is that of a fresh or relaxed episode, whatever its turn order,
  named agent, action order or listing order; the whole-content rule stays
  for every evaluation set. Done in the frozen code's `grammar.py`
  (`TrainingStream.admits`) and `train_successor.py`, with seven new
  self-test checks; 227 of 227 self-tests pass; a replay of the development
  runs' own stream (seed 0, 108,919 steps of 48 pairs, 5,228,112 contents)
  finds none such, so those runs most likely saw none (MEASURED:
  `docs/2026-10-06-successor-training-exclusion-pairing-findings.md`, branch
  `training-exclusion-pairing` at `9acc566`; checked, pass, with the
  whole-pipeline test passing at both sizes: `reviews/2026-10-06-training-exclusion-pairing-check-claude-code.md`,
  branch `check-training-exclusion` at `7278309`). The reason recorded: a
  sampled self-test of 200 steps cannot promise the registered claim that no
  such pairing "occurs in the training stream"; the options not taken were
  to check every step in full, or to reword the claim.
- **The cue-detector gates.** Gates (i) and (ii) of the registered design (no
  surface cue in the curriculum text or the input tensors predicts which turns
  are the model's own) run unchanged on the new grammar. Gate (iii), the
  likelihood attack, runs in its act-withheld form as re-specified in Amendment
  A3 §3.4, because the policy at a revision position is perspectival and
  scoring another agent's turn under it with the acting channel present would
  read the model's ownership knowledge as a leak.

### 4.4 The named-other condition: fallback (d) registers

**What registers (ruled 2026-09-25: the queue ruling, page 4, fallback (d);
the repairs rulings, item 1, whose "if it does not, (d) is what registers" is
now the case).** The registration text records, in these words:

- that the named-other condition **failed its bar on two of three toy arms**
  (on the committed models: arm F clears it on 1 seed of 3, at 994, 781 and
  746 correct of 3,000 against 790; arm C on 0 seeds of 3, at 760, 751 and
  708; arms T and M on 3 of 3; MEASURED: `out-repairs/gate_base.json` at
  `882f252`, reproduced field for field by the re-run's `out-v3-rules/gate.json`
  at `9d9d31a`);
- that **doubling the training budget did not fix it**
  (`docs/2026-09-21-successor-measure-rehearsal.md`, section 8);
- that **both training changes did not fix it**: a curriculum (the named-other
  condition alone for the first 1,000 of 2,500 steps) and loss re-weighting
  (the named-other loss four times the own-directed) cleared on 0 of 3 seeds
  each, against 1 of 3 on the unchanged recipe, and both made it worse
  (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at `882f252`, section 2,
  from `out-repairs/gate_curriculum.json` and `out-repairs/gate_reweight.json`;
  the check at `d216dbc` re-ran both from clean and got 0 of 3 each again);
- that **the grammar change did not fix it**: redesign (c), which turns the
  acting channel off on the seven tokens of the named-other action turn so
  that the two action turns no longer receive the same "this turn is yours"
  signal, ran on 2026-09-25 with its pass line committed before the run (790
  or more of 3,000 on at least two free-arm seeds of three, with the
  own-directed condition not degraded below 0.5513). It got **774, 730 and
  759**, 0 seeds of 3; the own-directed half held at a mean of 0.5654
  (MEASURED: `docs/2026-09-26-grammar-attempt.md` at `ff778ea`, section 3,
  from `out-grammar-c/passline.json`). Its check re-ran the attempt from the
  committed code and got **750, 809 and 739**, 1 seed of 3, and the same
  verdict (MEASURED: `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`
  at `f1ea004`, "Verdict"). **The check's note is carried into the record:
  a count of seeds clearing is a property of one training run, not of the
  code**, so the record says "at most one seed of three clears on either
  run", which is also what both earlier runs of the unchanged grammar gave;
- and that **the staggered first run bounds the money** (section 11, step 5a):
  the learn-both result of one free-arm run is read before the remaining
  runs are committed.

**Stop condition S1 did not fire.** It asks whether the grammar is learnable at
tiny scale even in principle, and the separable arm learned both conditions to
1.0000 (MEASURED: `out-repairs/gate_base.json` at `882f252`, arm T on every
seed). This is John's ruling, adopting the rehearsal's adjudication (the queue
ruling, page 4).

**The diagnosis, ARGUED and not ruled.** In this grammar the acting channel
fires on both action turns, so the two turns differ only in one word, and a
model that learns the own-directed route applies it at the named-other turn
too (the repairs findings, section 2, the paragraph headed "The reading").
The grammar attempt tested exactly that diagnosis by removing the shared
signal, and found the free arm still gives its own value at the named-other
turn only about one time in twenty and splits the rest across the other
agents' values, the same pattern as before the change (the grammar attempt at
`ff778ea`, section 3, from `out-grammar-c/diagnose_named_other.json`). Its
own reading, marked ARGUED there and here: the model already tells the two
turns apart and fails at a different step, matching the named marker word to
that agent's assignment. The check agrees the pattern is measured and the
step is not (the grammar check at `f1ea004`, section 4). Nothing in this
version acts on that reading.

**What the grammar attempt's failure does not show.** It does not show that no
grammar change could work, only that the smallest one, which removes the
shared acting signal, did not; and the toy arms may be too small to learn a
condition the registered size will learn, which is page 4's standing argument
against every toy redesign (the grammar attempt, section 7; ARGUED).

---

## 5. The four arms

All four train on the same grammar, at the same size (the registered 30M
configuration), on the same token budget and the same recipe (section 5.5),
with the same launcher, watchdog and network volume. **The launcher, named
(ruled, the Gate C rulings, RT-228):** version 4 named
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`,
the unregistered launcher that carries the argument guard of ledger item
RT-198 and the hang fix of 2026-09-25. The code freeze of 2026-10-04 derived
the successor's own launcher from it,
`experiments/08-successor-degree/src/launch_successor.sh`, carrying everything
that keeps money safe; it creates nothing on a dry run, calls no vendor,
refuses without its settings and refuses the toy size (MEASURED: the freeze,
test T7, `out-freeze-tests/t7-check-launcher.txt`), and it is the launcher
the four development runs ran (the compute ledger's four 2026-10-04 rows).
**[OPEN ITEM 11 for John: the ruling named the parent launcher; the registered
runs use the derived one. Confirm that the derived launcher stands in the
ruling's place.]** The registered launcher `launch_a3.sh` is registered text
under a standing prohibition (it has no argument handling) and is not used.
**Part of the registered recipe (ruled 2026-10-03, decision 13): the launcher
waits for the laptop's receipt, and the trainer does not delete its own
machine.** What the registration says about the shutdown is section 13,
weakness W9. **The two things version 4 said were owed as code exist**: the
training entry point for every arm on the rented machine
(`experiments/08-successor-degree/src/train_successor.py`) and the tripwire
(`src/tripwire.py`), both frozen on 2026-10-04 (`docs/2026-10-04-successor-code-freeze.md`),
the tripwire since amended on branch `tripwire-fixes` (section 12.5). Arm M's
code has now run on the rented machine, in the development runs (section
5.6). What differs between the arms is the architecture, and only in the way
the ownership answer is allowed to exist. **And since 2026-10-06 one more
thing is the same in the three built arms: the sharpness of their built-in
ownership answer is fixed at 4.0 (section 5.6).**

### 5.1 Arm T: the ownership answer kept separable, by construction

The registered trunk plus two additions:

- **An explicit table** of assignments: for each agent and each item, the value
  that agent most recently assigned. It is written at assignment turns and read
  at action positions.
- **A separate slot holding the ownership answer**, a single vector position
  that carries "which agent am I" and nothing else, produced from the acting
  channel and read by the action head as the row selector into the table.

The action is computed as: read the ownership slot, read the table row it
selects for the current item, apply the successor rule. The factoring into
(table, ownership answer, lookup) is the architecture, not something the
network may or may not discover, and the ownership slot is a single place that
can be transplanted on its own. **Its degree is zero by construction**, and
that is the point of the arm.

What the toy measured, under the rules this version registers: it reads
**0.0000 on every seed**, nominated at layer 0 at the action position with a
piece of 8 directions, the whole read and the piece each right on 180 of 180
held-out episodes on every seed; its ownership-only transplant moves the
action in every trial, above all twenty random draws of control 3 (MEASURED:
the controls re-run at `821f154`, section 2). Under the stricter layer-0
variant of section 7.2 its site moves to layer 1 at the action position and
it still reads 0.0000 (the same record, section 4). Its gate and lesion
figures reproduce the 2026-09-21 record exactly, and its toy training
reproduces from code and seed
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`).

**Ruled 2026-10-03 (decision 2): the ownership path is forced by the
architecture, not merely encouraged by a penalty term.** The forced version
is what makes the degree known; a soft version would be more comparable with
arm F but would forfeit the one thing the arm exists to supply.

**What the development run at 10 million parameters showed for this arm
(MEASURED: the check of the development runs,
`reviews/2026-10-04-development-runs-check-claude-code.md`, branch
`check-dev-10m` at `51ec07d`, sections 5 and 7; one seed, a pipeline check
and not a result).** Its construction held: its ownership answer was right on
3,000 of 3,000 gate episodes, the registered procedure nominated layer 0 at
the action position with a piece of 8 directions, right on 180 of 180, and
its reading was **0.0000, valid**, with controls 1, 4 and 7 holding and the
true-slot reference also 0.0000. Two things to carry: its learned sharpness
had halved (1.95 against 4.0), which is part of why it is now fixed (section
5.6); and its own-directed accuracy ended at 0.917 because the step that
chooses the table row with the ownership answer confused six specific pairs
of agent name words, every time (for example, when the model was the agent
named `m5` and an agent named `m4` was present, it chose `m4`'s row in 76 of
76 episodes), while forcing the right row gave 2,999 of 3,000 right. Under the
stricter layer-0 variant its reading there was 0.0802, where the toy read
0.0000 (the stricter variant is a reported sensitivity, not the registered
figure). The check asked that arm T's row-choice split (right row chosen,
accuracy where right and wrong, confused name pairs) be reported beside its
gate at the registered size, so a damaged lookup is seen as such.
**[OPEN ITEM 9 for John: that report is this session's recommendation and
the check's; no ruling adds it. The reporting table carries it meanwhile
(section 7.5, item 15).]**

### 5.2 Arm C: the ownership answer entangled, by construction

The registered trunk with the ownership signal mixed into the content
representation at every layer, and no slot of its own anywhere:

- The acting channel produces, per layer, a scale-and-shift applied to the
  whole running state of that block, so the ownership signal multiplies content
  rather than sitting beside it.
- The item and value representations are combined with the ownership signal
  multiplicatively at the point of binding, so that "which item, whose value"
  is one quantity rather than two.
- No dedicated ownership position exists and no part of the architecture reads
  ownership alone.

The prediction, if the construction works: transplanting any single nominated
part of the state fails to reproduce the counterfactual action, while
transplanting the whole state at the same places succeeds. **Its reading should
be high.**

**What the toy measured, under the rules this version registers (MEASURED:
the controls re-run at `821f154`, sections 2 to 4, from
`out-controls-rerun/nominate_C_seed*.json`, `measure_C_seed*.json` and
`summary.json`; reproduced value for value by the check at `e184a6e`, section
3).** It reads **1.0051, 0.9926 and 0.9974** on seeds 0, 1 and 2, at the
entangled end on every seed, quoted per seed for these particular models and
not as a property of the code. The rule chose:

| Seed | Site set | Size of piece | Whole read, right of 180 | Piece, right of 180, at the action position | Whole-state, ownership-only and no-transplant shares | Reading |
|---|---|---|---|---|---|---|
| 0 | layer 2 at the action position | 8 directions | 180 | 180 | 0.5400, 0.0488, 0.0512 | 1.0051 |
| 1 | layer 1 at the action position and the three before it | 8 directions | 177 | 172 | 0.5550, 0.0525, 0.0488 | 0.9926 |
| 2 | layer 1 from the model's first own turn to the action | 4 directions | 176 | 150 | 0.5463, 0.0612, 0.0600 | 0.9974 |

**What that shows, in the words the ruling of 2026-10-03 directs (page 1,
item 2): the read holds the label; the largest piece transplanted holds it;
no size moves the action.** Every chosen piece clears four fifths (144 of
180) at the action position, and its ownership-only transplant lands within
0.004 of the no-transplant rate while the whole-state transplant moves the
action in more than half of trials. That no size moves the action is the
review of version 3, RT-230, at version 3's site sets: arm C read between
0.9897 and 1.0051 at 1, 2, 4 and 8 directions on every seed. **Version 3's
sentence here, that the subspace arm C transplants "holds the label and
clears the fit floor on every seed", was false on two seeds of three** (the
pieces it chose there, of two directions and of one, held the label at 0.544
and 0.306; the review, RT-230), and its readings for those seeds (1.0025 and
1.0000, at layers 4 and 1) are replaced by the table above. Version 2's
figures for this arm (0.99 to 1.00, and the separation figures 0.9977 and
0.9927) were replaced in version 3 and stay replaced.

**Away from the action position the piece often does not hold the label at
four fifths.** On seed 1 the piece is right on 139, 139 and 33 of 180 at the
one, two and three positions before the action, and 113 on the average over
those three. On seed 2 it is below 144 at all ten positions reported, from 30
to 139, and 123 on the average over the other positions of its site. Seed 0's
site is a single position (MEASURED, **checked: the check of the short run at `53c8100`**:
the short pre-stated run at `853988f`, section 4). The whole state holds the
label at every one of those positions. This is reported and not gated
(section 7.2, item 3; weakness W13).

**The choice among candidates is made among sampling noise on this arm, and
the record says so.** On seed 1 the rule chose layer 1 over layer 4 because
the development ownership-only share was 0.0533 against 0.0517, one episode
of 600; the session that ran the re-run had predicted layer 4, and said so in
its findings. What the piece rule fixes is that whichever candidate wins, its
piece carries the label. The reading at the chosen site is 0.9926; at layer 4
with 8 directions it was 0.9975 (the controls re-run, section 3; the review,
RT-230). **This version does not use the sizes and readings on page 1 of the
ruling packet of 2026-10-03 (8, 8 and 4 directions at layers 2, 4 and 1;
1.0051, 0.9975 and 0.9974): they were that session's forecast, the ruling
itself says they are not committed results, and the forecast was wrong on
seed 1.**

Control 3's twenty random draws all sit above the ownership-only transplant
on seed 0, and around it on seeds 1 and 2 (6 below, 1 equal and 13 above; 6
below, 5 equal and 9 above), which is what an entangled arm should show: its
ownership piece does no more than a random piece of its size (the controls
re-run, sections 2 and 4; the reading of it is ARGUED).

**Arm C fails the named-other condition on every toy seed, and this version
says so wherever its toy record is quoted (ruled, the Gate C rulings, RT-213,
item 2).** Its named-other accuracy is 760, 751 and 708 correct of 3,000
against a bar of 790, so it clears on 0 seeds of 3, while its own-directed
condition clears on 3 of 3 (MEASURED: `out-repairs/gate_base.json` at
`882f252`, fields `runs.C/base/*.other_correct`; the Gate C review, RT-213).
Under version 2's learn-both gate that would have made the toy an R3 by way
of the high anchor. Under this version arm C is gated on the own-directed
condition only (section 8.1), with the reason recorded there, so its toy
record is a pass on the gate and a reading on every seed. **What that failure
costs under the launch order** is in section 11: a constructed arm that fails
its gate at registered scale is first seen in step 5b, after the second
release is drawn, and John ruled against an extra arm C run in step 5a on the
envelope's arithmetic (the Gate C rulings, RT-213, item 3).

**This arm is conditional and the condition is already accepted.** John ruled
on 2026-09-20 that arm C depends on the rehearsal showing that its degree is
genuinely known by construction rather than merely intended, and that the
two-arm fallback is accepted in advance. This proposal keeps that exactly as
ruled; rehearsal items R-3 and R-6 in section 10 are the test, and at toy
scale both pass under the registered rules. **At 10 million parameters the
condition failed, and the arm is repaired (section 5.6).** In the development
run the learned sharpness of arm C's built-in ownership answer fell from 4.0
to −0.089, so the answer put 0.218 of its weight on the agent the model
actually was (a quarter is flat), the scale-and-shift every block applies
carried no identity, and the registered procedure could not find "which
agent am I" anywhere in its running state at the action position (best piece
41 of 180 against 144 needed; on the toy, 180); it returned no verdict with
the arithmetic 0.99 described only. Its own-directed accuracy ended at 0.595,
beside the free model's 0.5975 (MEASURED: the check of the development runs,
branch `check-dev-10m` at `51ec07d`, sections 6 and 7). With the sharpness
fixed at 4.0 the nine retrained toy models of arms T, C and M keep it at
exactly 4.0 and arm C's weight on the true agent is 0.999 on every seed
(MEASURED: `docs/2026-10-06-sharpness-fix-inuse-check-findings.md`, branch
`fix-sharpness-inuse-check` at `644238e`, section 4). **What the repair does
not settle is in section 5.6:** on the toy, before and after the fix, arm
C's network gets most of its right answers through the acting signal in its
trunk and not through the built route, so the in-use check's second part
fails it (route use 0.244 to 0.285 against a bar of 0.5). **Also ruled, 2026-10-03
(decision 3): arm C entangles by its architecture, and is not trained with a
penalty against transplantable ownership directions**, which would train the
system against the very instrument that will measure it.

**Why the fallback is weaker, said plainly.** With arms T and F only, the
measure is anchored at one end. A reading on arm F above arm T's would show the
measure responds to something, and that arm F is less separable than a system
built to be separable, but there would be no known-high case, so nothing would
establish that the measure *scales* rather than merely *detects*, and the
number given to arm F would have no upper reference. **If the fallback fires,
the outcome is one of the two terms section 3 registers for it, "instrument
checked against the separable mechanism only", with "degree read" or "degree
not read", and arm F's figure has no upper reference** (ruled 2026-10-06, page
5, closing RT-241's hole 2).

**The toy figures for this arm with every read fitted on 1,800 development
episodes (ruled 2026-10-06, page 4; MEASURED: the page 4 re-run at
`e948899`, section 2, from `out-page4-rerun-1800/comparison.md`; checked at
`1e168f3`):** seed 0, state 2 at the action position, now a piece of 4
directions right on 178 of 180, reading 1.0026; seed 1, now state 4 at the
action position, 8 directions, piece 178, reading 1.0000; seed 2, state 1
from the first own turn to the action, 4 directions, as before, piece **165**
(it was 150), reading 1.0000. The two pieces nearest the floor moved away
from it, which is what page 4 was about. The table above, at 420 fitting
episodes, stands as the earlier record.

### 5.3 Arm M: a mixture of the two, by item

**Why it exists.** Section 3's admission, in its version 2 form: with anchors
only at the two ends, a free-arm reading at the entangled end cannot be told
from a ceiling. John ruled on 2026-09-25 that a fourth, partly separable arm
would be attempted at toy scale at $0, with its predicted reading stated
before it ran, and folded into the main registration only on a pre-stated
pass: a chance-corrected reading between 0.3 and 0.7 on all three seeds (the
queue ruling, page 5, option (iii)). It passed on the repairs run, and it was
folded in (the repairs rulings, item 2).

**Version 2's arm M pass was read without control 3 applied (ruled, the Gate C
rulings, RT-214, item 3).** Under version 2's own rules, which made control 3
a control that holds with a fixed 0.0175 room, arm M seed 1 got no reading
(its random subspace moved 0.0563 of trials against a limit of 0.0350; the
Gate C review, RT-214), so the "on all three seeds" pass John folded arm M in
on was not met by the design as then written. Control 3 is now a reported
twenty-draw null (section 7.3), and under it arm M reads on every seed; the
re-run was the check the RT-214 ruling asked for before this version was
filed, and its result is below.

**The construction** (`experiments/rehearsal-successor-measure/src/arm_middle.py`,
method in `docs/rehearsal-repairs-method-2026-09-25.md`, section 5, both at
`882f252`): arm T's slot and head, and arm C's entangling and ordinary output
layer, in one network. Actions about some items go wholly through the
separable route and actions about the others go wholly through the entangled
route, so that about three fifths of actions are entangled: 0.60375 of the 800
fresh measurement trials, 483 of 800 (MEASURED: `out-repairs/measure_base_M.json`
at `882f252`, the field `fourth_arm.entangled_share`). The repairs findings
print 0.6033, which is the same share on the held-out gate episodes, 1,810 of
3,000 (MEASURED: `out-repairs/gate_base.json` at `882f252`, the field
`own_by_route.entangled_share`); both are right, on different episodes (the
Gate C review, RT-219). **The registration
describes it as what it is: a mixture by item, each action going wholly
through the separable or the entangled route, about three fifths entangled,
not partial separation within a trial** (the repairs rulings, item 2, in those
words).

**The prediction, and what it is (ruled, the Gate C rulings, RT-223).** Write
*p* for the entangled share, and for each route write its whole-state and
no-transplant accuracies. The reading the measure should return, if the blind
nomination catches the separable route's slot and nothing of the entangled
route, is the entangled route's share of the total room the whole-state
transplant moves:

    p × (whole_C − untouched_C) / [ (1 − p) × (whole_T − untouched_T) + p × (whole_C − untouched_C) ]

**That formula is the true-slot reading of section 7.2, item 6, written in
route accuracies: one check, not two.** By algebra, a transplant that carries
the separable route fully and the entangled route not at all gives exactly
this number in the chance-corrected form, and on the repairs run the formula
and the true-slot reading agree to four decimals on every seed (0.4895,
0.4572 and 0.4904; MEASURED: the Gate C review, RT-223, from
`out-repairs/measure_base_M.json` at `882f252`). So what the comparison
shows is that the blind nomination finds about what the true slot gives on
the same episodes, a check of the nomination against the construction, and
not a prediction made in advance of the run. The registered prediction for
arm M at the registered size is: **between 0.3 and 0.7 on every seed, and
within 0.10 of the true-slot reading on the same fresh episodes.** The
true-slot reading is computed and written down before the blind reading is
looked at.

**What the toy measured, under the rules this version registers (MEASURED:
the controls re-run at `821f154`, sections 2 and 4, from
`out-controls-rerun/measure_M_seed*.json`; reproduced by the check at
`e184a6e`, section 3).** The blind reading is **0.4886, 0.4860 and 0.5449**
on seeds 0, 1 and 2, inside 0.3 to 0.7 on every seed, so the fold-in pass
stands with control 3 reported beside it. Every seed is nominated at layer 1
from the model's first own turn to the action, with a piece of 8 directions;
the whole read and the piece are each right on 180 of 180 at the action
position; the whole-state transplant moves 0.7800, 0.7738 and 0.7937 of
trials and the ownership-only transplant 0.4050, 0.4062 and 0.3688, above all
twenty random draws of control 3 by a wide margin (random medians 0.015 to
0.019). **The "within 0.10" half of the prediction now has its figure at the
registered site sets, which version 3 listed as owed:** the true-slot reading
is 0.4837, 0.4760 and 0.4920, the route formula agrees with it to four
decimals, and the blind reading is within **0.0049, 0.0099 and 0.0529** of it
(MEASURED: the review of version 3, RT-231, from its script
`arm_m_true_slot.py`; found again by the controls re-run, section 4, whose
prose printed the middle figure as 0.0100 from two rounded numbers; the
unrounded difference is 0.00995, and the check at `e184a6e`, section 3,
gives 0.0099). Seed 2 uses a little over half the allowance. Arm M passes its
gate on the own-directed condition on all three seeds (0.8613 to 0.8667), and
clears the named-other condition too (0.5517 to 0.5663), although that is no
longer gated for it (MEASURED: `out-repairs/gate_base.json` at `882f252`).
Its self-test passes all seven checks, including that perturbing the slot
never moves an entangled-route action (`out-repairs/self-tests.txt` at
`882f252`).

**Away from the action position arm M's piece is not what this session, or
the one that ran it, expected.** On the average over the other positions of
its site the piece is right on 163, 174 and 175 of 180, above four fifths on
every seed. Position by position it reaches 144 at only four, four and seven
of the ten positions reported, and at the fourth token of the model's first
own turn (the value word) it is right on 34, 71 and 33 (MEASURED, **checked: the check of the short run at `53c8100`**: the short pre-stated run at `853988f`, section
4, whose author records that it expected better and was wrong). The two ways
of computing the figure give different pictures of this arm, which is why
John ruled that the registered table prints both (section 7.5).

**With every read fitted on 1,800 development episodes (ruled 2026-10-06,
page 4; MEASURED: the page 4 re-run at `e948899`, section 2; checked at
`1e168f3`):** the blind reading is **0.5252, 0.4793 and 0.5208**, inside 0.3
to 0.7 on every seed, and the true-slot reading on the same fresh episodes is
0.5000, 0.4760 and 0.4920, so the blind reading is within 0.0252, 0.0033 and
0.0288 of it, inside the 0.10 allowance on every seed (from
`out-page4-rerun-1800/models-1800/summary.json`, the arm M block). Seed 0's
site moved to state 3 at the action position, 8 directions; seeds 1 and 2
keep their site. The earlier figures above, at 420, stand as the earlier
record.

**At 10 million parameters arm M's construction did not hold either, and it
is repaired with arm C (section 5.6).** In the development run its sharpness
fell to −0.008, its separable route chose the right agent's row in only a
quarter of episodes yet got every own-directed action on that route right,
and forcing the right row changed nothing: that route no longer depended on
the ownership slot at all. The registered procedure found no readable
ownership in its running state (best piece 45 of 180) and returned no
verdict (MEASURED: the check of the development runs, branch `check-dev-10m`
at `51ec07d`, sections 6 and 7). On the toy, before and after the fix, arm
M's separable route depends wholly on the built answer (route use 1.000) and
its stirred-in route hardly at all (0.090 to 0.106 after the fix), so the
in-use check's second part fails it (section 5.6).

**What this buys, and what it does not (ARGUED, from the findings' own
words).** It shows the measure, pointed blind at a system with a known
mixture, returns a number in the middle and near the mixture's share. It does
not show that the measure scales on a system whose partial separation is
*within* each trial, which is what a freely trained system would have. Page
5's strongest argument against applies in full and is carried as weakness
W10: its degree is a design intention, and it differs from both anchors in
more than degree.

**What it costs.** Three registered runs, priced at **$32 to $44** from the
compute ledger's per-run rows (the queue ruling, pages 5 and 6; the
derivation, from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and
2026-08-12 rows, is on page 5 of
`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`), from the $450
envelope (section 12). Of that, the $1.94 development run at the 10-million
size is now paid from the first release's development line and launched in
step 4 with the other three arms (ruled, the Gate C rulings, RT-229; section
12.3), and section 12.4 carries only the three registered runs. **Arm M's
seconds per step were not measured on the rented machine before version 4**:
the slice of 2026-09-25 timed arms T, C and F only
(`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section
3). **They were measured in the development run at 10 million parameters:
0.0145 seconds a step against 0.0099, 0.0100 and 0.0093 for arms T, C and
F, about 1.44 times arm C's, where its operation count is only 1.11 times**
(MEASURED: the check of the development runs, branch `check-dev-10m` at
`51ec07d`, section 4). The check's argued cause is a per-step copy from the
processor's memory in arm M's forward pass; it was not tested on a card.
Section 12.4 carries the consequence for arm M's three registered runs.

### 5.4 Arm F: the freely trained system

The registered register-less configuration with the acting channel present,
the same architecture as the closed Amendment A3 runs, trained on the same
matched-role grammar with no constraint on where the ownership answer may live.
This is the system being read. It is read only after it passes the learn-both
gate, the channel-removal check in section 8.2 (its collapse line and its
ownership-free line), and the fit floor of section 7.2. Its sharpness is left
learned: it computes the built-in answer and never uses it, so the number
receives no training signal and stayed at exactly 4.000 in the development
run (section 5.6).

**What the toy record states for it: "no verdict, read failed its floor", on
every seed (ruled, the rulings on the review of version 2, RT-212, item 2;
the floor moved to the piece on 2026-10-03).** No piece of its read of "which
marker word is the model's own" reaches four fifths at any layer, at any
size, on any seed: the best is right on 34 of 180 held-out episodes against
144 needed. Its whole read is right on **32, 12 and 18 of 180** on seeds 0, 1
and 2 at the layers shown in the re-run's table (MEASURED: the controls
re-run at `821f154`, sections 2 and 3, from
`out-controls-rerun/nominate_F_seed*.json`, `fits`, on the laptop's
processor). On the laptop's graphics chip the same reads were right on 31, 12
and 19, which are the 0.172, 0.067 and 0.106 quoted in version 3 and in every
earlier record; each difference is one held-out episode, and section 7.2,
item 1, says which device's figure is the registered one (the review of
version 3, RT-232). The no-information level of this read is 0.072, about 13
of 180 (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section
1.3). It also fails the learn-both gate: the named-other condition clears on
1 seed of 3 (section 4.4). So it fails twice over. **The number the
arithmetic would have returned (1.0000, 1.0000 and 1.0108) is withdrawn from
the record** under failure 2's rule and is not a reading; it appears in the
re-run's table in parentheses, labelled "reported for description; no
reading", only so that a reader can see what an empty instrument returns,
which is the entangled end. Every control figure for this arm in section 7.3
is taken at the site the rule would choose with the piece requirement
switched off, and carries the same label.

**What the free arm does instead of representing the label (ARGUED, the Gate
C review, RT-212, from `grammar.py` and the gate file).** It scores 0.5513 to
0.5597 on the own-directed condition against 0.2340 to 0.2383 for the
ownership-blind solver, and it collapses when the acting channel is removed
(0.1760 to 0.1940), so its ownership answer is load-bearing; but an
own-directed action can be solved by attending to the value tokens on the
turns the acting channel marked, with no need to know which marker word those
turns carry. That is why the route (b) investigation of section 7.2 looked for
a label the own-directed loss does force on a free system. The review of
version 3 saw the same thing directly: on the free arm the label is fully
readable from the whole state at the first token of the model's first own
turn and nearly unreadable at the action position (its RT-230, the side
observation), so the free toy model does not carry the marker word forward to
where it acts.

### 5.5 Seeds, and the training recipe, now fixed

**Three seeds per arm** (ruled 2026-09-25, the queue ruling, page 1f), giving
**twelve** registered runs across four arms. The registration says in terms
that the toy arithmetic implying one seed, the rehearsal's half-width
calculation, which the 2026-09-21 findings cautioned against carrying across
because the toy arms are far more repeatable than registered-size runs will
be (`docs/2026-09-21-successor-measure-rehearsal.md`, section 11), was not
carried across.

**The training recipe, fixed in this text (the code freeze's finding,
`docs/2026-10-04-successor-code-freeze.md`, section 4.2: version 4's "the
rehearsal's unchanged recipe" and "the same token budget" fix no recipe at 30
million parameters, and the trainer's defaults were a session's call).** The
registered recipe is the frozen trainer's defaults
(`experiments/08-successor-degree/src/train_successor.py`, the argument
defaults and the recipe line it writes into every run), which the four
development runs ran (the check of the development runs, section 1): the
AdamW optimiser at a peak learning rate of 0.002 with weight decay 0.01; a
one-cycle schedule with the first tenth of the steps as warm-up; gradients
clipped at 1.0; a batch of 96 episodes a step, which is 48 matched pairs (the
even-split rule, section 4.3); the closed design's token budget of
**585,544,960 tokens**, which at 56 tokens an episode is **108,919 steps**;
training episodes generated fresh at every step and never matching an
evaluation set by whole content, nor a fresh or relaxed episode by pairing
(section 4.3); an evaluation line every 2,000 steps on the 400-episode
trajectory set; seeds 0, 1 and 2; the same recipe for every arm, so that the
arms differ in architecture only. **[OPEN ITEM 5 for John: no ruling set this
recipe; it is the freeze session's call, now written as registered text
because the registration must fix it. Confirm it, or change it before the
reruns of section 5.6.]** One thing the development runs showed about it
(ARGUED by their check, section 5.4): with this learning rate and schedule arm
T's own-directed accuracy fell from 1.0 to 0.585 just after the learning-rate
peak and recovered to 0.89, and at the registered size the same recipe could
do the same or worse; nothing in the procedure flags it except the
accuracies, which are reported.

### 5.6 Amendment, written in before registration: the built arms are hand-set references, and the repaired route is verified before the free-arm run

*Ruled 2026-10-07 (`docs/rulings/2026-10-07-two-sided-question-rulings.md`,
decision 3 as first ruled, its addition in John's words "Yes, add the stop
condition to decision 3", and decision 3 as revised; authorship mixed), on
the ruling packet about the two built models that lost their ownership
route (`docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`, branch
`ruling-packet-cm-flat` at `7583326`, option 1(b) with option 4). The
ruling asks that the repair be written in as an amendment that says it turns
the built arms into hand-set references, before the registration is
committed (the Gate C pass's finding RT-271: there is no dated amendment to a
registration that does not yet exist). This is that text.*

**What was found (MEASURED: the check of the four development runs, branch
`check-dev-10m` at `51ec07d`, sections 6 and 7).** Each built model works out
"which agent am I" from how often the "this turn is yours" signal fired on
each agent's turns. One learned number, the sharpness, sets how decisive that
answer is; it starts at 4.0, nearly all weight on the right agent. In the
10-million-parameter development runs (108,919 steps each) it fell to −0.089
in arm C and −0.008 in arm M, so their answers put 0.218 and 0.247 of their
weight on the agent the model actually was, where a flat answer puts 0.25;
arm T's fell to 1.947 and still worked (0.942). The registered procedure,
independently, could not find "which agent am I" in arm C's or arm M's
running state (best pieces 41 and 45 of 180 against a floor of 144) and
returned no verdict on both. The fall was already visible in the toy models:
arm C's sharpness ended at 1.73, 0.70 and 0.93 on its three seeds, arm M's at
2.84, 2.69 and 2.42. Weight decay alone shrinks a number toward zero and
never past it, so training drove it there (ARGUED from the sign). This is
weakness W3 (an arm C whose construction did not hold), which version 4
expected to see only after both releases of money were spent, seen first at
the development size for nothing extra.

**The repair, as ruled: the built arms become hand-set references.** In arms
T, C and M the sharpness is a fixed stored value of 4.0 that training cannot
move (a buffer, never seen by the optimiser, so neither training nor weight
decay touches it); arm F is left as it is. The arms' ownership route is
therefore set by hand rather than left to training, and the arms are no
longer "known by construction" in the sense version 4 meant, where the
construction was trained and held: they are **references whose built-in
answer is fixed by hand**, and that is what the registration calls them. The
code change is on branch `fix-sharpness-inuse-check` at `644238e`
(`experiments/08-successor-degree/src/models.py`; method committed first,
`docs/2026-10-06-sharpness-fix-inuse-check-method.md`), with self-tests that
the number is not learned, is 4.0, and is still exactly 4.0 after an
optimiser step with heavy weight decay; every saved model still loads under
the same name, an older model with the value it learned. The change costs
nothing to the toy's learning: nine toy models retrained with the recipe
unchanged and the sharpness fixed all ended at exactly 4.0, arm C's weight
on the true agent rose from 0.914, 0.573 and 0.681 to 0.999 on every seed,
and no seed lost more than 36 of 3,000 own-directed answers (MEASURED:
`docs/2026-10-06-sharpness-fix-inuse-check-findings.md`, section 4, from
`out-sharpness-fix/retrained_inuse.txt`). **This work is owed its independent
check before the reruns.**

**The in-use check, as ruled (option 4), and what "holds" means in figures.**
A built model whose ownership route has gone flat anyway returns no verdict
for that seed with the reason "construction did not hold". The check is
computed on the same 3,000 gate episodes as the learning gate and judged by
the decision code (`procedure.gate` writes `route_in_use`; `measure.withhold`
judges it). It has two parts, both of which must pass on a seed for that
seed to count:

- **Part A, the answer is decisive:** the mean, over the gate episodes, of
  the weight the built-in answer puts on the agent the model actually is, at
  the own-directed action, is **at least 0.9**. With the sharpness at 4.0
  every episode gives 0.999; a flat answer gives 0.25; the mean falls below
  0.9 only if the sharpness falls below about 1.65. With the number fixed
  this part can fail only if the fix is undone or an old model is read (the
  bars and this arithmetic are the method note's,
  `docs/2026-10-06-sharpness-fix-inuse-check-method.md`, section 2, on branch
  `fix-sharpness-inuse-check` at `644238e`).
- **Part B, the network uses the answer:** each gate episode is run again
  with the built-in answer pointed at a different agent (every agent label
  in the tally moved on by one; the text and the acting signal unchanged);
  on the own-directed actions that go through the built route and that the
  model got right with the true answer, the share it no longer gets right is
  the *route use*. It must be **at least 0.5 on every built route** (arm T's
  slot; arm C's stirred-in route; both of arm M's). A route with nothing
  right to lose "could not be evaluated"; a missing field is "not run"; both
  count against.

The bars 0.9 and 0.5 are the method note's, stated before any figure was
seen, and **are ruled: on 2026-10-08, in John's words "Rule the verification
bar now, keep it at 0.5" (`docs/rulings/2026-10-08-verification-bar-ruling.md`, authorship mixed), they are fixed here as
written.** **The verification John ruled (decision 3 and its
addition) is: the three built arms are retrained once more at 10 million
parameters, seed 0, with the sharpness fixed (about $1.14 from the first
release's development line, of which $8.53 remains: the compute ledger's
2026-10-04 rows), and each is run through the registered procedure with the
in-use check; the repaired route "holds" when arm C and arm M each pass the
in-use check, both parts, and pass their gate on learning.**

**The stop condition (ruled 2026-10-07, in John's words "Yes, add the stop
condition to decision 3").** If that verification fails, that is, if the
rerun built models at 10 million parameters do not hold their built-in
ownership route (the stirred-in model and the half-and-half model) or do not
do the task, **experiment C stops there, before the free-arm run at
registered size, and the rest of the first release is not spent.** That
ending is reported in the words ruled on 2026-10-08, "the built arms as
designed are not references; the measure was not reached", and is a
registered ending of experiment C, not a failure of the year (`docs/rulings/2026-10-08-december-result-restatement-rulings.md`). A
verification that passes is evidence for the 30-million size, not proof of
it. **A failure of arm T's rerun is not named by the ruling; this text
treats it the same way and says so.** **[OPEN ITEM 6 for John: confirm that
arm T's rerun failing its in-use check or gate also stops experiment C.]**

**What the toy says about that verification, and the question it leaves
(MEASURED: the sharpness findings, section 2 and section 4).** On the twelve
committed toy models and on the nine retrained with the sharpness fixed, part
A passes everywhere the number is 4.0. **Part B fails every arm C and arm M
seed, before the fix and after it.** Swapping arm C's built answer to another
agent loses only 24 to 29 per cent of its right own-directed answers (route
use 0.269, 0.233, 0.221 before; 0.285, 0.273, 0.244 after); arm M's
stirred-in route loses 7 to 11 per cent (0.071, 0.090, 0.109 before; 0.090,
0.106, 0.100 after); arm T and arm M's separable route lose 100 per cent
(1.000). On the real 10-million checkpoints: arm C 0.018, arm M 0.000 on both
routes, arm T 0.924. So on the toy the stirred-in route was never the main
carrier of "which agent am I": the network gets it mostly through the acting
signal in its trunk and its attention layers, the same free route arm F
uses, and the fix does not change that. **With the bar at 0.5 as coded, the
reruns would very likely fail the verification and experiment C would stop at
about $1.14.** The findings offer four options, none chosen there: (a) keep
0.5; (b) set part B's bar against the free model's 0.000, for example 0.1,
which toy arm C passes and arm M's stirred-in half sits at the edge of, and
which detects a route switched off (as at 10 million) but not a minority
carrier; (c) part A only, the literal reading of "gone flat"; (d) change arm
C and arm M's stirred-in half so the built route is the only route (for
example, no acting signal in their trunk), which is a change to what the arms
are and needs its own toy retrain and check. *(Ruled 2026-10-08: option (a)
taken; (b), (c) and (d) declined, (d) staying the named route to a real
reference if the stop fires, with its own toy work and ruling; `docs/rulings/2026-10-08-verification-bar-ruling.md`. Open
item 1 of section 21 is closed by that ruling.)* The bar is ruled at 0.5 and
fixed here before the reruns launch, as the 2026-10-07 ruling requires, and
the route-use figure is recorded for every built arm and seed.

**What the toy record quoted in this text rests on, after the repair.** Every
toy reading in sections 3, 5, 7 and 9 was measured on the twelve committed
toy models, whose sharpness was learned. Of the nine retrained with it fixed,
only arm T seed 0 has been run through the full procedure: nominated at state
0, the action position, 8 directions, 180 of 180; reading 0.0000; controls 1,
4 and 7 hold; identical to the committed figure (MEASURED: the sharpness
findings, section 4, from `out-sharpness-fix/reread/row_T_seed0.json`). The
other eleven re-reads (about an hour on a quiet laptop) are owed, and the toy
outcome under the repaired construction has not been summarised. **The
registration therefore says: the toy anchors' readings are those of the
learned-sharpness models; the hand-set models have been shown to learn the
task and to keep the number at 4.0, and have been read on one of nine.**

**What this amendment changes elsewhere.** The frozen model code
(`models.py`); the decision code (`procedure.py`, `measure.py`); version 4's
description of arms T, C and M as "by construction" (sections 5.1 to 5.3);
the order of work (section 11, step 4b and stop S4b); the money (section
12.3); weaknesses W3 and W17 (section 13). It does not change the grammar,
the measure, the floors, the controls or the free model.

---

## 6. The measure

### 6.1 The pairing

Episodes are generated in matched pairs that share a content seed and rotate
which agent the model is, machinery the registered generator already has. In
a pair, the **recipient** episode is the one the model runs; the **donor**
episode is its twin in which the model is a different agent. Because all four
agents assigned the item, **the value the donor's identity dictates is already
present in the recipient's own context.** So the donor's answer is not new to
the recipient. **That does not show a successful transplant moved who is
acting rather than carrying the donor's chosen value: a transplant at the
action position can carry either, and nothing in this design separates the
two** (ruled 2026-10-06, follow-up item 1, closing the outside review's A7,
adopted as RT-251; version 4's sentence that this construction lets the
experiment tell the two apart is withdrawn).

### 6.2 The two transplants

A **site set** is fixed before anything is read: a list of token positions and
a list of layers. At those sites:

- **Whole-state transplant.** Replace the entire running-state vector at each
  site with the donor's.
- **Ownership-only transplant.** At the same sites, replace only the part of
  that vector lying in the nominated ownership subspace, leaving the rest of
  the vector as the recipient had it.

The second is a restriction of the first to a subspace, not a smaller or
different intervention. That is deliberate: it means the measure reads *how
much of the identity-driven difference at these places lives outside the
nominated subspace*, and not *how many places you had to touch*. The
rehearsal's transplanting code proves the restriction as a tensor identity in
its self-test (rehearsal item R-8).

**Two kinds of site set are not an intervention on what the network built.**
Copying the running state at every position of a layer makes everything
downstream of that layer the donor's own computation, wherever ownership lives
only in the running state; copying every layer at every position is the
donor's forward pass outright. And copying layer 0, the state the acting
channel is added to, at positions spanning the turns the channel fires on, is
a transplant of the acting channel's own input rather than of anything the
network computed from it (the Gate C review, RT-216). Section 7.2 removes both
kinds from the candidate family by rule.

### 6.3 The number

For each arm, on fresh episodes:

- `accuracy_whole`: the share of transplant trials where the action is the
  value the donor's identity dictates, under the whole-state transplant.
- `accuracy_ownership_only`: the same share under the ownership-only
  transplant.
- `accuracy_untouched`: the same share with no transplant at all: the
  no-transplant rate. Section 6.4 says what it must be near.

**The reading is the chance-corrected form** (ruled 2026-09-25, the queue
ruling, page 2):

    degree = (accuracy_whole − accuracy_ownership_only) / (accuracy_whole − accuracy_untouched)

**with the raw difference and both accuracies always reported beside it**, and
the no-transplant rate with them. Zero means fully separable: transplanting
the ownership answer alone does everything transplanting the whole state
does. One means the ownership-only transplant did nothing at all: the act
resists being pulled apart at these sites. The separation bar (section 9, 1a)
and the floor (1c) are written on this scale.

**Why this form and not version 1's.** Version 1 divided by `accuracy_whole`
alone. A no-transplant rate that sits under both terms does not cancel in
that ratio, so the largest value version 1's reading could return was
different for every arm: the ceiling failure of Amendment A3 with the zero
replaced by a moving number (the Gate C review of version 1, finding RT-172,
the per-arm-ceiling finding, in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`;
failure 1 of `docs/known-failure-modes.md`). The rehearsal confirmed it and
demonstrated the repair: on two made-up systems with the same true share
outside the subspace, 0.5, and different transplant strengths, version 1's
form read 0.4323 and 0.3222, and the chance-corrected form read 0.5018 and
0.5013 (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`, section
5, from `out/denominator_simulated.json`). The top of the chance-corrected
scale is 1 on every arm; section 17, failure 1, prints it for all twelve
toy arm-and-seed pairs under this version's rules.

**Readings outside 0 to 1 are reported as observed and never clipped** (the
repairs rulings, the paragraph after item 5). A negative reading means the
ownership-only transplant moved the action more than the whole-state one; a
reading above 1 means the ownership-only transplant landed below the
no-transplant rate. Both are sampling noise around "the subspace does
nothing" when small (arm C reads 1.0051 at one toy seed; the controls re-run
at `821f154`, section 2) and a warning about the instrument when large. The
rehearsal showed a negative value is reachable (rehearsal item R-4).

### 6.4 When the measure returns no verdict

The closed Amendment A3 design registered a comparison whose denominator was
zero from the day it was registered, and nobody noticed for four days after a
red-team pass had said so in plain words (ledger item RT-21, the unequal
ceilings finding). This measure has a denominator, so it gets explicit
no-verdict rules, written before it runs:

1. **The whole-state floor (ruled, the queue ruling, page 1c; refined by the
   repairs rulings, item 4).** A site set is usable only if the whole-state
   transplant clears **four fifths of the arm's own own-directed accuracy on
   the same fresh episodes**, written on the chance-corrected scale:

       accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy − accuracy_untouched)

   **and the requirement on the right must be above zero** (ruled 2026-10-06,
   page 2, closing the inside review's RT-238, the zero-divisor finding; the
   outside review's A3 and G4 repeat it). Where the arm's own-directed
   accuracy is not above its no-transplant rate on the same episodes, the
   floor is not defined, no site set is usable, and the arm returns "no
   verdict: no site set clears the whole-state floor". This is the code's
   clause (`need > 0` in `repairs.floor_check`, which every toy run used), and
   the registered code carries it. The plain form,
   `accuracy_whole ≥ 0.8 × own_directed_accuracy`, is printed beside it
   everywhere, so a reader can see where the two readings of the ruled
   sentence disagree. **On the own-directed grids of the twelve toy models
   they never do** (MEASURED: the repairs findings at `882f252`, section 3;
   the re-run records both forms on every row,
   `out-v3-rules/measure_*_seed*.json`, `reading.floor`). **Elsewhere on the
   toy they do, always in the same direction, the plain form passing where
   the registered form refuses**: on 576 rows of the repairs run's
   other-agent grids, 892 rows of the grammar attempt's grids and all 1,080
   rows of the competing solver's (MEASURED: the inside review of version 4,
   RT-243, the floor-forms finding, `floor_forms.out.txt`, on branch
   `gate-a-tier1-successor-v4` at `135c1f7`; ruled 2026-10-06, page 6).
   Almost all are on models near chance; five are on the grammar attempt's
   free model with its own-directed condition learned, missed by 0.011 or
   less (the check of the inside dispositions, pull request 96, section 3.2).
   That is the reason the chance-corrected form is the one registered;
   version 4's "on the toy they never did" was true of the own-directed grids
   only. *Turning the ruled sentence into the first form is this design's
   choice and is marked ARGUED in the repairs method note.* If no site set
   clears the floor for an arm, that arm returns **no verdict** at
   nomination, and that is recorded rather than repaired. **The floor keeps
   the denominator away from zero by construction only with that clause.**
   Without it, a model at chance meets the inequality at every site set with
   a divisor of zero or below: the ordinary competing solver does so on four
   of its six runs, with divisors between −0.0017 and +0.0033 (MEASURED: the
   inside review, RT-238, `rule_from_text.out.txt`, section 4). With it, the
   denominator is at least four fifths of a requirement that is above zero;
   on an arm that has learned the task that requirement is large.

   **The floor is applied twice, on different episodes (the review of
   version 3, RT-234, accepted 2026-10-03, page 3).** At nomination it is
   applied on development episodes, to decide which site sets are candidates.
   At the reading it is applied again, on the fresh episodes. **A site set
   that clears on development episodes and misses on fresh ones returns "no
   verdict: floor missed on fresh episodes"**; the nomination is frozen by
   then and is not redone. On the toy the two agree on all twelve arm-and-seed
   pairs, and the narrowest margin is arm F seed 0 on development episodes,
   0.4433 against 0.4280 needed, which is 9 episodes of 600 (MEASURED: the
   review, RT-234; the controls re-run at `821f154`, section 4, "the
   whole-state floor on fresh episodes clears on all twelve").
2. **The fit floor, on the piece that is transplanted (ruled, the rulings on
   the review of version 2, RT-212, item 1; applied per arm and seed, ruled
   2026-09-26 on decision 21; moved from the whole read to the piece by the
   rulings of 2026-10-03, page 1).** Only a size of piece whose own held-out
   accuracy reaches **four fifths** on development episodes may be chosen
   (section 7.2, item 3, gives the rule in full). An arm and seed with no
   size that reaches it returns **"no verdict, read failed its floor"**, and
   the transplant arithmetic is not reported as a reading. The piece's count
   and the whole read's count are both printed in the reporting table, with
   the label-permutation null beside them as a reference and not as the bar.
   **The floor is on the piece only (ruled 2026-10-03, late evening, ruling
   1).** The ruling of 2026-09-26 put the floor on the whole read, at the
   worst layer of the nominated site set. The morning ruling of 2026-10-03
   moved it to the piece and did not say whether the whole read must still
   clear four fifths in its own right. John ruled that it need not: the
   whole read's count is printed beside the piece's and is not a second
   condition. That is how the controls re-run ran
   (`experiments/rehearsal-successor-measure/src/rerun_controls.py`,
   `PIECE_MIN`; its method, rule 9). On the toy the two readings give the
   same twelve verdicts: every chosen piece's whole read is right on 176 or
   more of 180, and arm F misses both. They can differ in principle, because
   a piece can score above its whole read by an episode or two (on arm F seed
   1, 17 against 12; on the named agent's read of section 7.3, item 2, 139
   against 137). The alternative that was put and not taken: require both.
3. **The no-transplant sanity rule, with the review's formula and the
   allowance as re-worded (ruled, the Gate C rulings, RT-222).** Version 1
   said the no-transplant rate "should be near the one-in-eight guessing
   rate; if it is not, the pairing is broken and nothing is read". With
   distinct values that rule is pointed the wrong way round: a model that has
   learned nothing lands near one in eight and a model that has learned the
   task lands far below it (the Gate C review of version 1, finding RT-173;
   failure 3 of `docs/known-failure-modes.md`). The registered rule is the
   review's formula: with *p* the arm's own-directed accuracy on the same fresh
   episodes, the no-transplant rate should be near

       (1 − p) / 7

   because an untransplanted model lands on the donor's answer only by erring
   onto exactly that one of the seven other slots. **That assumes the model's
   wrong answers spread evenly over the seven other values, which is not true
   of every model** (ruled 2026-10-04, ruling 3, closing the solver run's
   question 3): a model that confuses owners lands on the donor's value more
   often, as the toy's competing solver did at about twice the formula.
   Version 2 set the room at the largest measured miss, 0.017536 on the free
   arm at one seed, rounded up to 0.018 (MEASURED:
   `docs/2026-09-21-successor-measure-rehearsal.md`, section 5, from
   `out/denominator_floor.json`; the Gate C review, RT-222). On the repairs'
   fresh episodes every miss was inside 0.0132 (the repairs findings at
   `882f252`, section 6.4).

   **The no-transplant rate is reported against the formula, not used to
   withhold a reading (ruled 2026-10-06, page 8, closing the outside review's
   A9, adopted as RT-248; amending the Gate C ruling RT-222 and ruling 3 of
   2026-10-04, which treated the formula as withholding).** The formula is
   right only if the model's errors spread evenly over the seven wrong
   values. A correctly paired model whose errors go to the other three
   agents' values lands at `(1 − p) / 3`, outside the allowance at any
   accuracy below about 0.9: at an accuracy of 0.8 that is 0.0667 against the
   formula's 0.0286, a gap of 0.0381; on 800 pairs a rule of 0.018 would
   withhold such a model 0.99 of the time, and would catch a fully broken
   pairing at the learn-both bar only 0.56 of the time (MEASURED:
   `docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements.md`, part B, on
   branch `rulings-2026-10-06-gate-a-v4` at `525a625`). On the toy every
   model erred roughly evenly (0.097 to 0.155 of its errors on the donor's
   answer), which is why it passed. **The pairing is checked directly
   instead:** the registered generator's self-test asserts, on every matched
   pair, that the donor's dictated answer is computed from the donor's own
   identity and value on the named item, and differs from the recipient's
   except in the relaxed set's same-value trials; and **control 4**, which
   already withholds a reading, transplants the donor's states from before
   either twin's own turn and requires the output to be bit-identical, which
   a mismatched pair would break (ruled 2026-10-06, follow-up item 3: control
   4 is the pairing check that withholds; the self-test is kept as a second
   check). Control 7, the null transplant, checks the transplant code, not
   the pairing. **Version 4's detection-margin sentence is replaced, not
   dropped silently:** "the detection margin at the bar is printed in the
   reporting table ... 0.0198, a margin of only 0.0018 over the allowance; at
   0.56 ... 0.0441" becomes: the chance the formula would flag a broken
   pairing on 800 pairs is printed beside the rate, **0.56 at the learn-both
   bar** (the outside review, A9: the 0.0018 margin was not a demonstration
   of detection). The rate, the formula's value, their difference and the
   share of errors landing on the donor's answer are printed in the reporting
   table. The decision code of pull request 105 reports the rate and does
   not withhold on it (its case 19: arm T's rate 0.05 off the formula, R1).
4. **A reading outside 0 to 1** is reported as observed (section 6.3), not
   clipped and not suppressed.
5. **If a control that holds fails** (section 7.3: the null transplant,
   control 7; the content transplant, control 1, on arm T only; and the
   too-early-position control, control 4, as redefined), **or, on a built
   arm, the in-use check fails** (section 5.6), the reading is not made for
   that arm and seed. **The registered code withholds the reading itself; the
   procedure that does so was rehearsed end to end before registration
   (section 10, R-13; ruled 2026-10-06, follow-up item 6, closing the outside
   review's fatal finding A2, adopted as RT-256).** The toy re-run's code
   computed each of these as a true-or-false field and printed the reading
   regardless; every one passed, so no reading was printed that should not
   have been, but the withholding was left to the reader of the table (the
   check at `e184a6e`, section 4, item 3). In the registered code a failed
   control that holds, a floor missed on development or fresh episodes, a
   failed gate, a failed channel-removal check on arm F, or a failed in-use
   check on a built arm replaces the reading with "no verdict" and **every**
   reason that applies, in the output file and in the table; a check that
   could not be evaluated counts as failed; and the figure the arithmetic
   would have given appears nowhere in the output (the field that carried it,
   `arithmetic_withheld`, was removed on John's word "yes, remove"). The
   no-transplant rate no longer withholds (item 3). Exercised on 25 made-up
   cases (MEASURED: `docs/2026-10-06-successor-a2-decision-procedure-findings.md`
   at `bd0de26`; the checks at `e6dd8fa` and `f609c9d`: no withheld figure in
   any output; each rule, switched off in turn, changes at least one case's
   outcome).

**The only subtraction anywhere in this design is of the measured
no-transplant rate, in the chance-corrected form of section 6.3, and nothing
wider.** No ownership-blind ceiling is estimated, subtracted or divided by
anywhere. (This sentence replaces version 1's "No normalisation by an
ownership-blind ceiling anywhere", as the queue ruling's page 2 directs: the
outside review's one-line warning still stands, and the programme has already
paid for the lesson once; what has changed is that the no-transplant rate is
a measured quantity of the pairing, not a ceiling, and subtracting it is what
gives every arm the same top of scale.)

---

## 7. The measurement procedure

### 7.1 Data split, and what "fresh" means

Three disjoint sets, generated from separate seeds and committed before use:

- **Training episodes**: what the arms are trained on.
- **Development episodes**: the only data on which anything is chosen: the
  site set, the nominated subspace, its rank, and any tuning at all. **The
  straight-line reads are fitted on development episodes, written to disk and
  reloaded**; they are never refitted on the episodes the reading is taken
  from (the rehearsal caught itself doing that and fixed it before any result
  was read: `docs/2026-09-21-successor-measure-rehearsal.md`, section 9, item 3).
  The fit of section 7.2, item 1, is scored on a held-out part of the
  development episodes (on the toy, the last 180 of 600), never on the fresh
  episodes.
- **Fresh episodes and confirmation seeds**: evaluated once, after the freeze.
  **No fresh or relaxed episode's pairing (which marker holds which value on
  which item) can occur in training**: the training stream refuses it
  outright (section 4.3; ruled 2026-10-06, follow-up item 8), and the
  generator's self-test asserts it in the stricter reading (follow-up items 4
  and 7, RT-255). Different random seeds alone were not taken as proof that
  the sets are disjoint (the outside review's unlettered remark on control
  5).

**"Fresh" is disambiguated, as the rehearsal required** (its section 7, item
4). Version 1 asked for "marker and content combinations that appear in
neither of the other two sets", and that phrase has two readings. **The
registered reading is the weak one: unseen *combinations* of marker words,
items and values that the arm has each seen in training**, the rehearsal
grammar's pool named `fresh`, which draws from the training vocabulary with
its own seed (`experiments/rehearsal-successor-measure/src/grammar.py`, the
`POOLS` table). The strong reading, marker words the arm has never seen, is
**kept as a named diagnostic and is never the evaluation set**: under it the
separable arm's own accuracy fell to 0.7612, 0.6512 and 0.6512, the
whole-state transplant was capped there, and the reading went negative on two
seeds of three (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`,
section 7, item 4; the pool named `unseen-vocabulary` in the same grammar
file). The registration says which reading it means in these words.

### 7.2 Choosing the candidate ownership representation: one instrument

On development episodes only, for each arm, **identically**: one function,
which takes no argument that names an arm, called the same way for every arm
(the repairs' `experiments/rehearsal-successor-measure/src/repairs.py` and the
re-run's `src/rerun_v3.py`, both at `9d9d31a`, and the controls re-run's
`src/rerun_controls.py` at `821f154`, do this, and their nomination tables
show one rule applied throughout). **The registration says in one
sentence that the rule's outputs differ per arm, and differ by seed within
arms C, F and M** (ruled, the queue ruling, page 3; MEASURED on the toy: arm C
is nominated at layer 2 at the action position, layer 1 at the action
position and the three before it, and layer 1 from the first own turn to the
action, on its three seeds; the controls re-run at `821f154`, section 3).

1. **The label, its route to the states, and the fit floor.** The
   straight-line read is fitted against **which marker word is the model's
   own**. *The route by which that quantity reaches the model's states, in one
   sentence:* the marker word is the input token at every turn the model's own
   assignments are spoken on, so it is carried by the token into the running
   state; and on an arm whose slot is built from it (arms T and M) or which
   multiplies it into content (arm C), the read recovers it at 0.96 or better
   from the first block onward. **What version 2's route sentence went on to
   claim, that which marker word is the model's own is forced by the loss at
   the own-directed action, is false for a freely trained system and is
   struck** (the Gate C review, RT-212): an own-directed action can be solved
   by attending to the value tokens on the turns the acting channel marked,
   without knowing which marker word those turns carry, and the toy free arm
   does exactly that (section 5.4). Ruled 2026-09-23
   (`docs/rulings/2026-09-23-nomination-label.md`; fixed in code as well as in
   text: the repairs code's `READ_LABEL = "marker-word"`, and the successor's
   measurement code when written, per the queue ruling, page 3). The label
   was ruled on the separable arm alone, which is the one arm whose slot is
   made of the label by construction (that ruling's section 4), and it is the
   only one of the three readings of "which agent is acting" that recovers a
   degree known independently of the instrument; the other two, the agent's
   slot and the marker's rank, put an arm whose degree is zero by construction
   at the entangled end of the scale.

   **The fit floor (ruled, the rulings on the review of version 2, RT-212,
   item 1; moved to the piece by the rulings of 2026-10-03, page 1, item
   1).** In the ruling's words: "only sizes whose own held-out accuracy
   clears four fifths may be chosen, and that accuracy is printed in the
   reporting table", beside the whole read's. "The accuracy of a piece is the
   held-out accuracy of a read given only the state's coordinates inside that
   piece, on the same development episodes and split as the whole read. An
   arm and seed with no size that clears returns 'no verdict, read failed its
   floor'." The floor is absolute, the same convention as the whole-state
   floor. The label-permutation null, the fit the whole read reaches when the
   labels are shuffled (two hundred shuffles at toy scale; its 95th and 99th
   percentiles), is reported beside it and is not the bar. The reason
   recorded in the ruling of 2026-09-26: a permutation null alone would
   likely certify a read at 0.172, which recovers the label on about one
   episode in six, and that is not an instrument worth transplanting. **The
   floor applies per arm and seed** (ruled 2026-09-26 on decision 21,
   recorded in the rulings file at `9ed9f8c`): an arm's three seeds are
   reported one by one, each a reading or a no verdict, and the across-seed
   spread of section 9 is taken over the seeds that read. The whole read's
   count is printed and is not a second floor (section 6.4, item 2).

   **How the accuracy is stated, on how many episodes, and on what it is
   computed (the review of version 3, RT-232; accepted 2026-10-03, page 3, as
   the review states the fix; the fitting count ruled 2026-10-06, page 4).**
   Every fit in the registration and in the reporting table is **stated as a
   count of held-out episodes** (of 180; the floor is 144). **Every read is
   fitted on 1,800 development episodes, with the last 180 of 1,980 held
   out** (ruled 2026-10-06, page 4, "(a), go with the recommendation",
   closing the inside review's RT-240, the width finding, and the outside
   review's A4 and G1; amending ruling 4 of 2026-10-03, late evening, in both
   its records, for the read's fitting count only). The reason: the toy's
   running state is 160 numbers wide and the registered model's 448, so at
   the ruled 420 fitting episodes there would be more coordinates than
   episodes; on a stand-in at width 448 (the toy states with 288 coordinates
   of independent noise appended) the entangled model's read fell below the
   floor on two seeds of three at 420 and 900 fitting episodes and under
   stronger regularisation, and held on every seed and draw at 1,800
   (smallest 156; MEASURED on a stand-in, NOT A RESULT: the inside review,
   RT-240, `width_vs_count.out.txt`; `docs/2026-10-04-gate-a-v4-dispositions-measurements.md`,
   part B, branch `rulings-2026-10-06-gate-a-v4` at `525a625`). The toy
   re-run under it is done and checked (section 10, R-3; the page 4 re-run
   at `e948899`, checked at `1e168f3`): no toy decision moves; the chosen
   site set or size moved on five models of fifteen; the two pieces nearest
   the floor moved away from it; one status changed, control 2 on the free
   model's seed 0 (section 7.3, item 2). The transplant passes that choose
   the site set stay on 600 development pairs. **Two cautions the re-run
   recorded:** 1,800 is the smallest of three sizes tried that held on the
   stand-in, not a size derived from anything (weakness W15); and at 1,800
   the straight-line fit stopped at its iteration limit of 3,000 far more
   often on arm M (471 warnings against 27 at 420), so arm M's reads there
   are partly a product of where the fitter stopped, and a wider model may
   hit the limit more often still. **[OPEN ITEM 7 for John: whether 3,000
   iterations is enough at the registered width, or the limit is raised
   before registration; the frozen code still fits on 420 of 600 and the
   change to 1,980 is owed in it.]** **The registration names the device and the number format
   the registered fit is computed on, and the figure on that device is the
   registered one.** The reason: the floor is a hard line, per arm and seed,
   and on the toy two of twelve reads moved by exactly one held-out episode
   between the laptop's processor and its graphics chip (arm F, 32 against 31
   and 18 against 19; the other ten were identical; MEASURED: the review,
   RT-232; the controls re-run at `821f154`, section 3), so a fit within an
   episode or two of four fifths could pass on one device and fail on the
   other. **Ruled 2026-10-03, late evening (ruling 3), widened 2026-10-06 (page 6,
   RT-245):** **the whole nomination and reading, every forward pass, every
   transplant pass that chooses the site set, and every fit, is computed on
   the laptop's processor**, never its graphics chip; the model's states are
   computed in the model's own 32-bit floating-point format; the read is
   scikit-learn's logistic regression, which fits in 64-bit. The choice of
   site set can turn on one episode in 600 (arm C, seed 1, on the toy at 420
   fitting episodes), and a transplant pass can move by an episode between
   devices as a fit can, which is why the device is named for the whole
   nomination and not only the fit. **The registered code writes every
   pinned version to its output file** (the controls re-run recorded torch
   only; its findings give torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0;
   the check of version 4, finding 8), **and the versions are pinned in a
   committed file named here:
   `experiments/08-successor-degree/requirements-measure.txt`** (frozen
   2026-10-04, on the main line at `53ae82c`; torch, scikit-learn, numpy and
   scipy), so that a line read to one episode does not move because a
   library was upgraded between the registration and the reading
   (`docs/rulings/2026-10-03-version-4-questions-rulings.md`, ruling 3; the
   reconciliation; the check of version 4, finding 9: the lock file version 4
   gave as the model is not committed, and `.gitignore` keeps any file so
   named out, so the pin file has this name and place). **If the processor
   proves impractical at full size, that is a fresh question for John, not a
   switch of device** (record B, ruling 3). The processor is the device the
   controls re-run, the short pre-stated run and the page 4 re-run, which
   supply every toy figure in this version, ran on. The alternative that was
   put and not taken: the graphics chip. **In the registered run the
   read is fitted once, on that device, written to disk and reloaded
   (section 7.1); the printed whole-read count and the transplanted
   directions come from that one fit.** On the toy re-run they came from two
   fits of the same read: the directions from the coefficients committed
   earlier on the graphics chip, and the printed count from a fresh fit on
   the processor (the check at `e184a6e`, section 4, item 2); on the built
   arms nothing turns on it.

   **The toy demonstration (MEASURED: the controls re-run at `821f154`,
   sections 2 and 3; reproduced by the check at `e184a6e`, section 3).** The
   floor returns no verdict on arm F and a reading on arms T, C and M. Right
   of 180 held-out episodes at the action position, whole read then chosen
   piece: arm T 180 and 180 on every seed; arm C 180 and 180, 177 and 172,
   176 and 150; arm M 180 and 180 on every seed; arm F 32, 12 and 18 for the
   whole read, with no piece above 34 at any layer or size. The lowest piece
   among those that clear is 150 of 180. The permutation null's 95th
   percentile sat at 0.111 to 0.128 (about 20 to 23 of 180) across all twelve
   pairs on the earlier re-run (`docs/2026-09-26-toy-rerun-v3-rules.md` at
   `9d9d31a`, Part 1, section 1.3; the check at `70be9fb`, section 3.2; that
   null is for the whole read, on the graphics chip, and was not recomputed
   on 2026-10-03). **One clause of the rulings file's refinement item 2 was
   wrong on this point and carries an annotation** (the rulings file at
   `da41c20`, pull request 68): it said that under the layer-0 removal "arms
   C and F still fall to the fit floor"; arm C does not, and only arm F falls
   to the floor. Nothing ruled depends on the clause.

   **The route (b) investigation, and what it found (the Gate C rulings,
   RT-212, item 3; the result ruled 2026-09-26).** Route (b) asked for a label
   the own-directed loss does force on a free system, which a straight-line
   read can recover on arm F at four fifths. The free-arm label search
   (`docs/2026-09-26-free-arm-label-search.md`, main line at `a97c12b`, pull
   request 66; laptop only, $0,
   nothing retrained, on the committed arm F models) tried three candidates
   under the registered site-set rule at toy scale, with a floor of 0.80 on
   held-out fit and a 200-shuffle label-permutation null at each site.
   **None clears the four-fifths floor on arm F, at any site set, on any
   seed.** The best is 0.789, from candidate 1 (which earlier turns are the
   model's own), and that from position spans that start at one of the
   model's own turns, so that where the span starts gives part of the answer
   away; anchored at the action position, candidate 1 reaches 0.733, 0.383
   and 0.478 on seeds 0, 1 and 2, and candidates 2 and 3 at most 0.417 and
   0.633 (ruled 2026-10-06, page 6, closing the inside review's RT-242:
   version 4 quoted one candidate's three seeds as three candidates). All three sit well above their shuffle null, so they are
   carried by the free arm, just not at the floor (MEASURED: the search's
   findings at `a97c12b`, sections 1 and 2; its check,
   `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`,
   main line at `ecd2b6c`, pull request 70,
   recomputed every best fit, shuffle summary and verdict from the committed
   files with no disagreement, and confirmed the twelve models against the
   committed fingerprint list; its section 6 narrows the search's closing
   sentence to "none of three candidates chosen in advance", which is how it
   is stated here). **John's ruling of 2026-09-26 (the rulings file at
   `a11f1d3`, "RT-212 item 3 resolved", items 1 to 5): this version registers
   with the fit floor alone; the ruled label, which marker word is the model's
   own, stays the one registered read; the three candidates enter the toy
   record as exploratory fits, not as registered reads; the experiment
   proceeds; and the first release's single arm F run reports its nomination
   fit against the floor, a miss being a stop before the second release
   draws** (section 11, step 5a). The reason recorded there: the fits rising to
   0.79 above a 0.10 shuffle baseline on the small toy model is the argument
   that the deeper registered model may clear the floor, and $44 is the price
   of finding out before $130 is spent. **The depths, stated the same way in
   both places (the review of version 3, RT-236; accepted 2026-10-03, page
   3): the toy has four blocks and five running states; the registered model
   has twelve blocks and thirteen running states.** The ruling as recorded
   calls the toy "a five-layer model" and the registered one "twelve-layer",
   which counts states for one and blocks for the other; the rulings file
   carries a dated note beside the phrase and stands as recorded. Like for
   like, the registered model is three times as deep, not two and a half. **The search also printed a
   fit for the ruled label on arm F of 0.556, 0.483 and 0.433 over its 60 site
   sets, which is not the 0.172 the Gate C review and the re-run report. The
   check reconciled the two: they are different reads of the same models,
   episodes, split and fitter.** The registered rule fits one read per layer
   at the action position only and reports the worst layer of the nominated
   set; the search fitted one read per site set, with the layers and
   positions of the set laid end to end and the post-identity span averaged,
   and all three of its higher figures come from that averaged span at layers
   0 to 1 or 0, which starts at the model's own marker word and which the
   layer-0 removal of item 2 excludes. On the search's own cell for the
   registered read (layer 1, the action position) it prints 0.172, 0.067 and
   0.106 to the digit (MEASURED: the check at `ecd2b6c`, "Verdict" and section
   2). Item 3 registers which read is meant, so the two cannot be confused
   again; the 0.172 is the registered read's figure as the graphics chip
   computed it, and on the processor the same read is right on 32 of 180.

2. **Candidate sites: the rule, the printed list, and what is removed from the
   family.** The site list is registered as the rule that generates it
   (ruled, the queue ruling, page 1e), and the registration prints the list
   the rule produces for the registered 12-layer architecture beside the rule,
   with the count of comparisons it implies, so the family correction is
   pre-stated. **The rule has now been run at toy scale exactly as registered
   (ruled, the Gate C rulings, RT-215; MEASURED: the re-run findings at
   `9d9d31a`, Part 1), so every toy nomination, reading and control figure in
   this version comes from the family the rule generates**, which meets the
   review's objection that version 2's figures came from a hand-listed
   44-set family the rule never produced (the Gate C review, RT-215). The
   rule:
   - **Positions**, grouped into the position sets the rehearsal used and
     registered here by name (`experiments/rehearsal-successor-measure/src/rehearse.py`,
     `CANDIDATE_POSITIONS`; positions in `src/transplant.py`): the action
     position alone (`action`); **the action position and the answer-marker
     token just before it** (`action+ans`; version 2 described this set
     backwards, the Gate C review, RT-224); the action position and the three
     positions before it (`action+3`); every position from the model's first
     own turn to the action (`post-identity`). (The rehearsal's fifth set,
     every position, is excluded by the rule below.) **Ruled 2026-10-03 (decision 19): the
     position sets are the rehearsal's four, by name.**
   - **Layers**: every contiguous set of the model's running states, counting
     the state after the input embedding as one (layer 0) and each of the
     twelve blocks' outputs as one more: 13 states, 91 contiguous sets.
   - **The all-positions exclusion** (ruled, the repairs rulings, item 3):
     **any site set whose positions are all positions is excluded**, at any
     layer. The reason is section 6.2's: copying all positions at a layer
     hands the donor's whole forward pass downstream. On the four named
     position sets no site set spans every position in any episode (MEASURED:
     the re-run's `out-v3-rules/nominate_*_seed*.json`, field
     `family.share_of_episodes_where_position_set_spans_every_position`; the
     check at `70be9fb`, section 4.3), so on this family the exclusion removes
     nothing further.
   - **The layer-0 exclusion, as removal from the family (ruled, the Gate C
     rulings, RT-216, item 1, as clarified by refinement item 2).** Layer 0 is
     the state the acting channel is added to. **Every site set whose layers
     include layer 0 is removed from the candidate family before nomination
     at every position set other than `action`**, and the rule chooses again
     from what remains, in the way the all-positions exclusion works. Layer 0
     stays a candidate at the action position set only, where the constructed
     anchors' slot sits by construction. The reason: at position sets
     spanning the turns the channel fires on, the twins differ at layer 0 only
     by the channel's own input, so a whole-state transplant there is a
     transplant of the acting channel and not of anything the network built,
     and the subspace compared against it was, on arms C and F, a read fitted
     at 0.072 (the Gate C review, RT-216). **This reading of the ruling, that
     "excluded" means removed from the family and chosen again, was clarified
     after the re-run of 2026-09-26, with the re-run's figures in hand, and is
     not called pre-stated here**: the re-run's first pass read "excluded" as
     "reported as no verdict", recorded the removal reading as its own column
     before it ran, and put the choice to John, who ruled the removal reading
     on the same day (the re-run findings, Part 2; the check at `70be9fb`,
     sections 1.3 and 4.6). Under it, six of the nine toy nominations on arms
     C, F and M that the first pass had left at the injection move off layer
     0, every one to a single later layer (the re-run findings, Part 1,
     section 1.5). *Two readings of which position sets "span the acting
     turns" exist, and they give the same twelve toy nominations:* the ruling's
     first sentence keeps layer 0 at `action` only, which the re-run applied;
     its parenthesis names `post-identity` and any set including the marked
     turns, which on this grammar is `post-identity` alone (MEASURED: the check
     at `70be9fb`, section 4.4, by a script printed in its appendix C and not
     committed as a file). **This version registers the reading as run, layer
     0 kept at `action` only, 45 site sets on the toy and 325 on the
     registered model (ruled 2026-09-26 on decision 20)**; the narrower
     reading is recorded beside it as the alternative that was put and not
     taken. On the separable arms layer 0 inside
     the action turn does move the action (arm T's whole-state share there is
     1.000 against 0.000 untouched; arm M's about 0.40, short of its floor),
     so it is the rule's position-set order, `action` first, that decides the
     tie on arm T and not any property of the states (the check at `70be9fb`,
     section 5). Version 2's argument that those states are identical in the
     twins was wrong for arms T and M and is not repeated.
   - **The count.** With every contiguous layer set at the four position sets,
     the family is 60 site sets on the toy and 364 on the registered model;
     with the layer-0 sets removed at the three position sets other than
     `action`, **45 site sets and 180 comparisons on the toy, and 325 site
     sets and 1,300 comparisons on the registered model** at four rank caps.
     The narrower reading of decision 20 gives 55 and 220 on the toy, 351 and
     1,404 on the registered model; the stricter variant below gives 40 and
     160, and 312 and 1,248 (MEASURED: the review of version 3, "What was
     checked and held", recomputed all eight site-set counts by arithmetic
     on the rule; section 18 prints the registered list with its command). The ruled figures before the
     all-positions widening, 296 and 1,816, and version 2's 60 and 364, are
     superseded by these; the repairs rulings' annotation 4 records the first
     supersession. The list and the rule have to agree, and the registration
     prints both: **the list for the registered model is printed in section
     18**, generated by the rule and not typed by hand, with the command that
     generated it.
   - **The stricter variant, as a sensitivity row (ruled, the Gate C rulings,
     RT-216, item 3).** Every layer-0 site set removed at every position set,
     `action` included, then choose again. Reported beside the primary
     reading for every arm and seed, so John can switch to it with figures in
     hand before Gate A. On the toy it differs from the primary row only on
     arm T, whose site moves from layer 0 to layer 1 at the action position,
     rank 8, with fit 1.000 and reading 0.0000 on every seed; on arms C, F
     and M the primary nominations contain no layer 0, so the row is the same
     pick with the same numbers (MEASURED: the re-run findings, Part 1,
     section 1.3; the check at `70be9fb`, section 3.7). The reason recorded
     for not ruling it blind: it may move arm T's anchor read off the layer
     its slot was built at, which on the toy is exactly what it does.
3. **Candidate directions, and the read that supplies them, registered.**
   **The read the rule uses is one fitted straight-line read per layer, on
   the running state at the mask token of the own-directed action (the
   `action` position), labelled with the model's own marker word, fitted on
   the development episodes and scored on the held-out part of them** (in the
   rehearsal code, `repairs.fit_reads`: one logistic regression per layer, the
   same read whatever site set is later nominated). At each site set the
   directions transplanted are that read's leading directions at each layer
   in the set, at each of the rank caps **1, 2, 4 and 8**; **the registered
   cap is 8** and the search family reports all four (ruled, the queue ruling,
   page 1d).

   **The piece rule (ruled 2026-10-03, page 1; the review of version 3,
   RT-230, option (b)).** For each candidate site set and each size, the
   piece's own accuracy is computed: a fresh straight-line read given only
   the state's coordinates inside the piece, **at the action position**, on
   the same development episodes and the same split as the whole read; for a
   site set with more than one layer, the worst layer's. **A size is a
   candidate only if its piece is right on at least four fifths of the
   held-out episodes** (on the toy, 144 of 180). An arm and seed with site
   sets that clear the whole-state floor and no size that reaches four fifths
   returns "no verdict, read failed its floor". The alternative that was put
   to John and not taken: fixing the size at 8 directions with the smaller
   sizes as extra rows. **The requirement is applied after the layer set is
   chosen (item 4), so it decides which sizes may be chosen and never changes
   which layers are used (ruled 2026-10-03, late evening, ruling 2).** The
   re-run's method had marked that as its own reading, for John to overturn
   (`docs/controls-rerun-method-2026-10-03.md`, rule 7; the check at
   `e184a6e`, section 4, item 6); he confirmed it. The alternative that was
   put and not taken: letting the piece's accuracy also decide between layer
   sets, which has not been run. **Reconciled 2026-10-03 (night): what this
   order can miss, stated as the ruling requires.** The earliest layers at
   which the whole-state transplant works need not be layers at which the
   label can be read where the model acts. A model whose label is readable
   only at later layers returns "no verdict, read failed its floor" although
   a later layer might have passed. The report for the first full-size
   free-model run prints the accuracy at every layer and the candidates the
   rule chose among (section 11), so such a miss is visible when John rules
   at that stop (`docs/rulings/2026-10-03-version-4-questions-rulings.md`,
   ruling 2; `docs/rulings/2026-10-03-seven-questions-reconciliation.md`).

   **The piece's accuracy at the other positions of its site: reported both
   ways, gated in neither (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3, and
   `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`,
   ruling 2).** Where the chosen site set covers more than the action
   position, the same directions are transplanted at every position of it,
   and the four fifths above was established at one of them. So the
   reporting table prints, beside the piece's count at the action position,
   **(i) its count at each other position of the site, and (ii) its count on
   the average over those positions.** Neither has a pass line; the rule is
   unchanged. Each is computed as the short pre-stated run's method states
   (`docs/2026-10-03-short-prestated-run-method.md` at `9e978d9`, section 4):
   - **A count at a position** is computed exactly as at the action position,
     with only the position changed: the model's state at that position on
     the development episodes, its coordinates inside the piece, **a fresh
     read fitted at that position** on the same split, and the number of
     held-out episodes it gets right. It is not the action-position read
     carried over. The same count for the whole state at that position is
     printed beside it, so that a low piece figure can be told apart from a
     position where the label is not in the state at all.
   - **Which positions are reported one by one.** For the action position and
     the token before it: that one position. For the action position and the
     three before it: each of the three. For a site that runs from the
     model's first own turn to the action, whose length differs from episode
     to episode: **the five tokens of the model's first own turn, and the
     five tokens before the action**; the positions between them do not line
     up from one episode to the next and **are covered by the average only**.
     A site at the action position alone is printed as "single position".
   - **The count on the average** is the same count taken on the state
     averaged over every position of the site except the action position.
     **In the registered code that average is taken in 64-bit arithmetic.**
     The reason is the check of the short run, finding 11: on the toy, the
     same average of the same numbers added up in a different order moved the
     count by one episode of 180 on three of the eight figures (arm F seed
     0's whole state, 90 against 91; arm F seed 2's, 74 against 73; arm M
     seed 0's piece, 164 against 163), and in 64-bit arm F seed 0 gives 92
     and 24. The check offered two ways to deal with it, saying the figure is
     good to an episode or two, or fixing the arithmetic; this draft does
     both, and the choice of 64-bit is this draft's. **The toy figures on the
     average quoted in this version are therefore good to an episode or
     two.** The per-position counts did not move.
   - For a site set with more than one layer, the worst layer's figure.
   - **How much of a span the ten named positions cover:** a span from the
     first own turn to the action runs 16 to 53 positions on the toy, 39.2 on
     average, so the ten positions reported one by one are about a quarter of
     it, and the rest is seen only through the average (the check of the
     short run, finding 14).

   **This computation rests on John's own words.** The evening ruling
   recorded it as ruled from "print both figures", which accepts it by
   implication only; the check of that record said so (its finding 19), John
   was asked, and he answered "Yes, section 4 of the method is what I meant"
   (a dated note beside item 3 of the ruling record, main line at `53c8100`).

   *What the toy shows (MEASURED, **checked: the check of the short run at `53c8100`**:
   `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 4, from
   `out-short-prestated-run/part_b.json`; each cell is whole state then
   piece, right of 180).* Arm T on every seed and arm C seed 0: single
   position. Arm C seed 1: 180 and 139, 179 and 139, 179 and 33 at one, two
   and three positions before the action; 179 and 113 on the average. Arm C
   seed 2: the piece between 30 and 139 at the ten positions, the whole state
   between 149 and 180; 180 and 123 on the average. Arm M: the piece at 144
   or more at four, four and seven of the ten positions on seeds 0, 1 and 2,
   and as low as 34, 71 and 33 at the fourth token of the first own turn;
   180 and 163, 180 and 174, 180 and 175 on the average. Arm F, described
   only: the piece between 11 and 36 everywhere except the first token of
   the first own turn on seed 2 (145), which is the model's own marker word
   itself. The action-position counts recomputed by that run equal the
   controls re-run's on all twelve. **A limit of these figures, from the
   run's own findings:** each is a fresh read fitted on 420 episodes with
   twelve possible answers, in a piece of 4 or 8 directions; a figure like
   139 against 144 is a few episodes and should not be read finely. (In the
   registered run, and in the page 4 re-run, every such read is fitted on
   1,800 episodes, item 1.) **A nominated site set's fit, for the floor of item 1, is the
   fit of the worst layer in the set**, as the re-run's verdict code reports
   it; on the toy no nomination has more than one layer, so this has not yet
   bitten. **What is not the registered read:** a read fitted per site set,
   with the states of every layer and every position in the set laid end to
   end and a multi-position span averaged over its positions, which is what
   the route (b) label search fitted (its `site_features`). That is a
   different quantity, it can score far higher on the same models (0.556
   against 0.172 on arm F seed 0, item 1), and nothing in this design uses it
   (the label-search check at `ecd2b6c`, section 2, which traced both reads
   through the code).
4. **The layer set for the whole-state transplant: "the smallest that clears
   the floor", in one reading** (ruled, the repairs rulings, item 4). For each
   position set, the layer set with the fewest layers that clears the
   four-fifths floor of section 6.4, ties going to the earliest layers; a
   position set with no clearing layer set drops out. The other reading, the
   highest ownership-only share over every clearing site set, is computed and
   printed beside it as a sensitivity row, **and that repairs-style row is the
   sensitivity row this version means** (the check at `70be9fb`, section 4.3,
   asked for the row to be named). On the repairs run's 44-set family the two
   readings picked different site sets on **8 of 12 arm-and-seed pairs, and
   the ownership-only shares they reached differed on 7 of 12**, by 0.02 or
   less (MEASURED: the Gate C review, RT-218, which resolved version 2's two
   counts; the repairs rulings' annotation 3, which adds that the check's
   re-run gave 6 of 12, so about half the pairs, by about 0.02, is what both
   runs support). On the re-run's 60-set family, no primary nomination is a
   multi-layer set, and the sensitivity reading picks a multi-layer set on five
   of twelve pairs (MEASURED: the re-run findings at `9d9d31a`, Part 2, first
   pass, section 5). The ruling's condition, that a nomination moving to a
   multi-layer set the hand list never tried be reported, did not fire.
5. **Nominate by causal effect, not by how well the read fits.** Over the
   surviving (position set, its smallest clearing layer set) pairs and the
   sizes whose piece clears the floor (item 3), the nominated configuration
   is the one with the highest *development-set ownership-only transplant
   accuracy*; ties go to the smaller size, then the earlier position set.
   This is the main lesson of the closed design: a representation that a
   straight-line read recovers beautifully can do nothing when you intervene
   on it. **What changed on 2026-10-03:** version 3 applied the fit floor to
   the nominated configuration afterwards; under the piece rule the floor is
   applied before the choice, as a limit on which sizes may be chosen. Among
   the sizes that pass, the choice is still blind to how well any read fits.
   **On an arm where nothing moves the action, that choice is made among
   sampling noise, and the registration says so** (the review of version 3,
   RT-230 and RT-235): on arm C the development shares at different sizes and
   sites differ by one or two episodes of 600, and on seed 1 one episode
   decided the site (section 5.2). What the piece rule secures is that
   whichever candidate wins, its piece holds the label at the action
   position. It does not make the pick stable.
6. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
   procedure and not just the arithmetic at the end. The reading obtained by
   handing the procedure arm T's true slot, and arm M's, is computed and
   reported separately as a reference; on arm M that reference is the formula
   of section 5.3 written in route accuracies, one check and not two (the Gate
   C rulings, RT-223). On the toy the true-slot reading is 0.0000 on arm T
   and 0.4837, 0.4760 and 0.4920 on arm M (the controls re-run at `821f154`,
   section 4). Ruled 2026-09-25 (decision 1).
7. **The rider, in the reporting table** (ruled: John's addition, the queue
   ruling, page 3; kept in the table by the repairs rulings). For every arm
   and seed, the reading is also taken at **arm T's** nominated site set and
   rank for the same seed, using that arm's own read fitted at those sites,
   and reported beside the reading at the arm's own nomination, so a reader
   can see whether what differs between arms is their degree or where the
   procedure looked. **Where the whole-state transplant at arm T's site set
   misses the floor, the rider returns "no verdict", and the report says
   which of two things that means.** On the toy it returned no verdict for
   arms C, F and M on every seed, for two different reasons (ruled, the Gate C
   rulings, RT-225): on arms C and F, at layer 0 at the action position,
   nothing about ownership has yet reached those arms' running states, and
   the whole-state transplant lands on the no-transplant rate (0.0512 to
   0.0600 on arm C, 0.0563 to 0.0688 on arm F); on arm M, which carries arm
   T's slot, the whole-state transplant there moves the action in about 0.41
   of trials against about 0.01 untouched, and the no verdict is **a miss of
   the four-fifths floor**, not nothing reaching the state (MEASURED: the
   repairs findings at `882f252`, section 3, "The rider"; the Gate C review,
   RT-225; the repairs rulings' annotation 5). Arm T's site set is layer 0 at
   the action position on every seed under the registered rule, the same site
   the repairs run nominated, so these rider figures stand under the rule,
   and the controls re-run found them again: the whole-state share at arm T's
   site is 0.0512, 0.0488 and 0.0600 on arm C, 0.0587, 0.0563 and 0.0688 on
   arm F, each the no-transplant rate, and 0.4088, 0.4138 and 0.4100 on arm M
   (the controls re-run at `821f154`, section 2, the last column).

### 7.3 Controls

Every one of these is run on every arm. **Three of them hold**, and a failure
means the reading is not made for that arm and seed: control 7 (the null
transplant), control 1 on arm T only, and control 4 (the too-early-position
control, as redefined on 2026-10-03). **The rest are reported** beside the
reading and cannot veto it. Version 2 made control 3 hold as well, and
version 3 made control 4 reported; this version does neither, for the reasons
under items 3 and 4. **The registered code withholds a reading when a control
that holds fails; it does not only print true or false** (section 6.4, item
5).

**All of them now have figures under the registered rules.** Version 3 had
none for controls 1, 2, 4 and 6 on arms C, F and M at the site sets the rule
nominates, and the review of version 3 made that a precondition of the
registration review (RT-233; ruled 2026-10-03, page 2). The controls re-run
of 2026-10-03 ran controls 1, 3, 4, 6 and 7, the true-slot reference, the
rider and the stricter row on all twelve toy models, with its method and code
committed before its output (`docs/2026-10-03-controls-rerun.md` at
`821f154`); a session that did not run it ran it again from the committed
code and found every one of about 26,700 values equal (the check at
`e184a6e`, section 3). Control 2 has no figure and cannot have one at toy
scale (item 2). Arm F's figures are taken at the site the rule would choose
with the piece requirement switched off and are labelled "reported for
description; no reading" (the re-run's method, rule 12).

1. **Content transplant, re-worded so it cannot veto the entangled arm.**
   Transplant the complement of the nominated subspace at the same sites.
   *On arm T it holds*: the action must not follow the donor's identity above
   the no-transplant rate plus the 0.018 room of section 6.4 (on the toy:
   0.0000 on every seed). *On arms C, M and F it is reported and cannot
   veto.* On an entangled arm the complement carries the ownership signal by
   construction, since in a system where ownership multiplies content at
   every layer there is no ownership-free complement to transplant, so on
   such an arm the complement is expected to reproduce the counterfactual
   almost as well as the whole state does. On the toy it does: arm C's
   complement moves 0.5450, 0.5625 and 0.5312 of trials against whole-state
   shares of 0.5400, 0.5550 and 0.5463; arm M's moves 0.3875, 0.3762 and
   0.4288 against about 0.78, about half, which is what a mixture would give
   (ARGUED); arm F's, for description only, 0.4838, 0.5637 and 0.5400 against
   0.4850, 0.5675 and 0.5300 (MEASURED: the controls re-run at `821f154`,
   sections 2 and 4). As version 1 wrote it, this control would have vetoed
   the reading on exactly the arm the control battery exists to validate, and
   on arm F it would have vetoed whatever the free arm turned out to be,
   which is the thing being measured. Its value on arms C, M and F is a
   description of how much of the identity-driven difference lives outside
   the nominated subspace, which is the reading itself seen from the other
   side.
2. **Another agent's representation: a reported description with no pass
   line; not applicable on arms T and M (ruled, the repairs rulings, item 5;
   and `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1).**
   Nominate, by the identical procedure with the named agent's marker word as
   the label and the named-other action as the anchor, a representation of
   the named agent who is not acting, and transplant it from a twin that
   differs only in which agent is named. **What is reported: how often the
   own-directed action moves under the named agent's piece, beside how often
   it moves under twenty random pieces of the same size at the same sites,
   reported as control 3 reports its twenty (median, 95th percentile, and
   the counts below, equal and above).**
   - **It has no pass line.** Version 3 proposed a tolerance of 0.05 over the
     random piece (its decision 15); John agreed to it on the morning of
     2026-10-03 and withdrew it the same day after the controls re-run. No
     number is registered for this control, so nothing about it is a
     pre-stated quantity the rehearsal failed to exercise, in the sense of
     item 5 of the 2026-09-21 ruling.
   - **The registration says in terms: this control never ran at toy scale.**
     It runs only on an arm that has learned the named-other condition
     (passes the section 8.1 bar on it), and only where a piece of the named
     agent's read reaches four fifths. Arms T and M are not applicable by
     ruling: they hold the named agent outside the running state by
     construction, so no transplant into the state can move that action. Of
     the other six toy models, five have not learned the named-other
     condition (arm C at 760, 751 and 708 of 3,000 and arm F seeds 1 and 2 at
     781 and 746, against 790). The one that has, arm F seed 0 (994), has a
     read of the named agent's marker that misses the floor: the whole read
     is right on at most 137 of 180 held-out episodes and the best piece on
     139, against 144 needed (MEASURED: the controls re-run at `821f154`,
     section 5, from `out-controls-rerun/measure_F_seed0.json`, `control2`;
     the check at `e184a6e`, section 3). That would have been a no verdict
     under version 3's rule too. Four attempts to repair the named-other
     condition have not produced a toy model that learns it (section 4.4).
   - **A no verdict is the expected result at registered scale too**, and is
     reported as "no verdict" with which of the two reasons applies.
   - **The part of its code after the floor has run once, and that run is NOT
     A RESULT.** The function has three early exits, and the controls re-run
     took all three: "not applicable" on the six separable and mixed models,
     "has not learned" on five, and the floor on arm F seed 0. What had never
     run was everything after the floor (the check of the short run, finding
     15). So that the registered run is not the first time that code
     executes, the
     re-run's own function for the control was called once on arm F seed 0
     with the piece's accuracy floor switched off for that one call, at $0.
     It ran without error and returned its figures: a site at layer 1, the
     action position and the three before it, 8 directions, a piece right on
     92 of 180 (the floor would have asked for 144); the own-directed action
     moved in 0.0012 of trials, under a random piece in 0.0063, and the
     named-other action in 0.0962. **Those figures are evidence that the code
     ran. They are not a pass or a fail of anything**, because the piece
     transplanted is not known to carry the named agent at all (**NOT A
     RESULT**, and **checked: the check of the short run at `53c8100`**:
     `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 5, from
     `out-short-prestated-run/part_c_NOT_A_RESULT.json`). What is still true
     after it: the control has never been exercised on a model whose read of
     the named agent clears its floor.
   - **Twenty random pieces, not one (ruled 2026-10-03, late evening, ruling
     5; the code changed and its test re-run before the registration review,
     by the check-questions ruling of 2026-10-03, ruling 1).** The re-run's
     code compared against a single random piece, drawn with its own seed
     (the check at `e184a6e`, section 4, item 4). **The change is made:** the
     registered control 2 is `control2_twenty_draws.control2`
     (`experiments/rehearsal-successor-measure/src/control2_twenty_draws.py`),
     and `rerun_controls.control2` is named as the earlier version, kept as
     the record of the re-run (ruled 2026-10-04, ruling 4). Its code test ran
     once on the free model's seed 0 with the floor switched off, **NOT A
     RESULT**, and came back identical to the first code test on everything
     the change was not meant to touch: the same site set (layer 1, the
     action position and the three before it, 8 directions), the own-directed
     action moved in 0.0012 of trials under the named agent's piece, under
     twenty random pieces a middle value of 0.0037 and a 95th percentile of
     0.0052, with 0 below, 1 equal to and 19 above the real figure; the
     named-other action moved in 0.0962 (MEASURED:
     `docs/2026-10-03-control-2-twenty-draws.md`, main line, from
     `out-control-2-twenty-draws/code_test_NOT_A_RESULT.json`; checked in
     pull request 90). **The 95th percentile of the twenty is the summary,
     and all twenty are printed beside it** (ruled 2026-10-04, ruling 5).
     The alternative that was put and not taken: leave it at one draw.
   - **One toy status moved when the fitting count rose to 1,800 (section
     7.2, item 1):** on the free model's seed 0 this control went from "no
     verdict" to "reported; no pass line", because the read of the named
     other agent rose from a best piece of 140 to 176 of 180 and now clears
     the floor there (chosen: state 3 at the action, 8 directions, a piece of
     171; the own-directed action moved in 0.0000 of trials against a random
     median of 0.0025). The free model's *ownership* read stays far below the
     floor (best 40 of 180). Control 2 has no pass line and the free model
     fails its gate anyway, so no toy decision moves (MEASURED: the page 4
     re-run at `e948899`; its check at `1e168f3`, problem 1). So "this control
     never ran at toy scale" now reads: it has returned a figure on one toy
     model of six, at 1,800 fitting episodes.

   The alternative that was put to John and not taken: exercising the control
   on a made-up case built for the purpose. This is the successor's own
   obligation, not the closed design's control run on 2026-09-21 (the review
   of version 1, finding RT-181).
3. **Matched random subspaces: the twenty-draw null. Reported, not gated
   (ruled, the rulings on the review of version 2, RT-214, items 1 and 2, as
   refined on 2026-09-26 by refinement item 1).** Twenty random subspaces of
   the same rank and the same norm at the same sites are each transplanted in
   place of the nominated subspace, on every arm and seed. The reporting
   table prints the median and 95th percentile of the twenty random donor
   shares, the ownership-only transplant's own donor share, and how many of
   the twenty draws fall below, equal and above it. The fixed 0.0175 room of
   version 2 is dropped from this control. **The reason it is reported and
   not gated, as recorded in the refinement: a gate on this control cannot
   pass a separable arm and an entangled arm in the same direction.** An
   entangled arm's ownership-only transplant is meant to move nothing, so it
   can never beat random subspaces; on the earlier re-run's first pass, which
   gated on it, arm C seed 0's read fit at 1.000 and was blocked only by this
   control (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 2,
   first pass, sections 6.2 and 7). Its job of catching a leaky site set is
   done by the whole-state floor and the no-transplant rule. **This reporting
   rule was clarified after the re-run of 2026-09-26, with the first pass's
   figures in hand, and is not called pre-stated here** (the check at
   `70be9fb`, section 1.3). *What the toy shows (MEASURED: the controls
   re-run at `821f154`, sections 2 and 4):* on arms T and M the
   ownership-only transplant sits above all twenty draws on every seed (arm M
   0.37 to 0.41 against random medians of 0.015 to 0.019); on arm C it sits
   below all twenty on seed 0 and among them on seeds 1 and 2; on arm F it
   sits among the draws on every seed, which is consistent with a piece that
   holds nothing, though arm F's verdict comes from its floor and not from
   this control.
4. **Positions before both twins' first own turns. Holds (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 2, which
   reverses that morning's ruling on version 3's decision 16).**
   - **What is run.** At the layers of the arm's nominated site set, the
     donor twin's whole state is transplanted into the recipient at every
     position before the earlier of the two twins' first own turns. A twin's
     first own turn is the first position at which its acting channel is on.
     The control takes the site set's layers and not its positions.
   - **The pass line: the transplant changes nothing.** The model's outputs
     at its two action positions (its scores over the vocabulary there, which
     is what the null transplant has always compared) with the transplant are
     compared with the same outputs without it, on every pair, and must be
     bit-identical. "Outputs" here and wherever this control is described
     means those, and not the outputs at every position (the check of the
     short run, finding 7). Reported
     beside it: the share of trials landing on the donor's value with the
     transplant, the no-transplant share, and the number of trials whose
     action changed. **A failure withholds the reading for that arm and
     seed.**
   - **What this control is, said plainly: a known-answer test of the pairing
     and of the code, like the null transplant.** The twins are the same
     text. They differ only in which turns carry the acting channel. The
     models read left to right. So until one twin's channel first comes on,
     both have had exactly the same input, their internal states are the same
     numbers, and transplanting one into the other puts back what was already
     there. **It cannot fail on a correctly built model with correctly built
     pairs, and a pass says nothing about any model.** It is right that a
     failure withholds a reading, because a failure means the pairing, the
     left-to-right property or the transplant code is broken. It is not
     evidence that a model does not yet know its identity at those positions,
     and no report of this experiment describes it that way.
   - **What is withdrawn.** Version 3 defined this control on the positions
     before the *recipient's* first own turn, found it above the
     no-transplant rate on arms C and F, and explained that by saying those
     arms "receive the ownership signal by other routes at those sites".
     **That sentence is withdrawn** (ruling 2, item 3). The control as then
     defined was transplanting at positions where identity was already known,
     in the donor: in 407 of 800 matched pairs (0.5088) the donor twin's
     first own turn comes before the recipient's. Under that definition the
     re-run found the control above the no-transplant rate by 0.065 to 0.10
     on six of the twelve toy models and by 0.005 or less on the other six
     (MEASURED: the controls re-run at `821f154`, section 6).
   - **The evidence the redefinition rests on.** The diagnostic that
     suggested it was written after the re-run's output was seen and was not
     pre-stated (`src/posthoc_control4.py`). The ruling said that if the
     check of the re-run found the diagnostic wrong, the ruling returned to
     John. The check did not find it wrong. With separately written code that
     shares only the episode generator, the model loader and the model's
     forward pass, it found on all twelve models: the twins' inputs and
     states are identical before both first own turns, at every layer; the
     outputs with the redefined transplant are bit-identical to the outputs
     without it; and all of the old definition's excess is in the pairs where
     the donor's first own turn comes first (MEASURED: the check at
     `e184a6e`, section 5, from its script `independent_control4.py`).
   - **The pre-stated run the ruling required** (method and code committed
     before output, by a session that did not write the diagnostic): the
     redefined control **holds on all twelve toy models**. The outputs are
     bit-identical; the donor-value share equals the no-transplant share on
     every line; no trial's action changes; a null transplant at the same
     positions is bit-identical; and across the 800 pairs the control
     transplants at between 1 and 21 positions per pair, about 5 on average,
     never none, so it is never an empty test (MEASURED, **checked: the check of the short run at `53c8100`**: `docs/2026-10-03-short-prestated-run.md` at
     `853988f`, section 3, from `out-short-prestated-run/part_a.json`). The
     method said in advance that this was not a blind prediction: the session
     had already observed it with different code while checking the re-run.
     **The check of that run** ran it again from the committed code and got
     byte-identical output files, found the same thing with separately
     written code at all five running states of every model, and showed the
     test is not empty: with random noise added to the donor's state at the
     same positions the outputs change on all twelve models, so the
     transplant does write there, and it changes nothing in the real control
     because what it writes is what was already there (findings 4, 8 and 9).
     **One limit the check records on the word "pre-stated"** (finding 3):
     the record shows that the method and code were committed and pushed
     before the output, 2 minutes 39 seconds apart; no committed file can
     show that the script was never run before the method was committed.
     Little turns on it, because this control cannot fail on correctly built
     pairs whenever it is run.

   The alternative that was put to John and not taken: redefining the
   positions and keeping the control reported only.
5. **Fresh marker and content combinations**, per section 7.1. By construction.
6. **Same-value and different-value cells. Reported, on the relaxed set.
   A description, not a discriminator (ruled 2026-10-06, follow-up item 1,
   closing the outside review's A7, adopted as RT-251).** Trials are split
   into pairs whose donor identity dictates *the same* value as the
   recipient's and pairs where it dictates a *different* value. Copying who
   is acting and copying the donor's prepared answer predict the same
   pattern: nothing moves in the same-value cell, everything in the
   different-value cell. A moved same-value cell shows the whole-state
   transplant changes the action where neither would, which can be other
   content carried across or an imperfect model erring differently for the
   two owners; it does not say which. Version 4 called this "the
   discriminating control" and said a transplant that smuggled a value across
   changes both cells; both sentences are withdrawn. **The first cell is
   empty by construction on the distinctness-preserving grammar** (0 of
   4,000 trials: MEASURED, `docs/2026-09-21-successor-measure-rehearsal.md`,
   section 5, from `out/denominator_control6.json`; the Gate C review of
   version 1, finding RT-173; failure 3 of `docs/known-failure-modes.md`), so
   control 6 runs on the **separately generated relaxed set** of section 4.2,
   in which one item per episode has two agents sharing a value. On that set
   both cells have trials: 81 same-value and 719 different-value trials of 800
   per arm and seed on the toy, on all four arms (MEASURED: the `controls`
   fields of `out-repairs/measure_base_*.json` at `882f252`; section 17,
   failure 3, prints them). Both cells are pre-stated and both are reported,
   with the one-in-four reference for a solver that cannot tell which agent it
   is restated for the relaxed set, where it rises (on the toy, from 0.2467 to
   0.3095 on exactly the trials the relaxation adds; the 2026-09-21 rehearsal,
   section 5). Pre-stated expectation: the separable arm moves nothing in the
   same-value cell and everything in the different-value cell; an entangled
   arm is expected to move the same-value cell too, and that is reported as
   the caveat it is (weakness W11): on those arms the whole-state transplant
   moves the action where neither copying who is acting nor copying the
   answer would, which may be other content carried across or the model
   erring differently by owner; the cell does not say which. *What the toy shows under the
   registered rules (MEASURED: the controls re-run at `821f154`, sections 2
   and 4):* arm T moves 0.0000 of the same-value cell and 1.0000 of the
   different-value cell on every seed; the same-value cell moves on arm C
   (0.5062, 0.6296 and 0.5679), on arm M (0.2222, 0.2716 and 0.3210) and, for
   description, on arm F (0.7284, 0.6790 and 0.6296); the different-value
   cell moves in 0.82 to 0.95 of trials on those three arms.
7. **Null transplant. Holds.** Transplant the recipient's own state into
   itself. Every logit must be bit-identical. This is the known-answer test
   for the transplanting code and it runs before any result is read. **On the
   toy it holds at every place it was run, fifteen different places:** the
   twelve primary site sets (arm F's three being the described ones) and the
   three stricter-row site sets that differ from their primary, which are arm
   T's (MEASURED: the controls re-run at `821f154`, section 4; the check at
   `e184a6e`, section 3, which corrects the re-run's own count: its "twelve,
   nine and three" names fifteen different places, not twenty-four). That
   closes the citation gap version 3 recorded, that the null transplant had
   not been run at the site sets that changed. It is run again at the
   registered site sets before any registered reading.

**The ordinary competing solver was measured under the piece rule before the
registration review opened, as ruled (2026-10-03, late evening, ruling 7),
and the result is written here (ruled 2026-10-04, rulings 1, 2 and 6; the
sentence corrected 2026-10-06, page 2, RT-244).** The three committed
ownership-blind toy models were put through the nomination and reading as
registered, on the laptop at $0, method committed before output, by a
session other than the one that drafted version 4, and checked
(`docs/2026-10-03-competing-solver-run.md`, main line, from
`experiments/rehearsal-successor-measure/out-competing-solver-run/`; the
check, `reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`).
**The main reading has the acting channel removed, as the solver was trained
and scored; the reading with the channel left on is stated beside it** (ruling
1). With the channel removed the twins' states are identical, so every
transplant is a null transplant and that reading's "no verdict" follows from
the pairing alone and is not evidence about the measure; the reading with the
channel left on is the one that tests the measure. Both returned **no verdict
on every seed**. In the words ruled on 2026-10-04 and corrected on
2026-10-06: *on the toy, the ordinary competing solver returned no verdict
because no site set cleared the floor at nomination; behind that, its best
piece missed the piece rule by 119 or more of 180 (best 20 to 25 against
144), its untouched rate was 0.109 or more above the no-transplant formula
and 0.091 or more outside the rule's allowance (0.1091 to 0.1393, and 0.0911
to 0.1213), and it would have failed the gate on learning had it been gated
as the free model is (702, 715 and 702 of 3,000 own-directed, 712, 726 and
650 named-other, against 790; the gate does not apply to competing solvers).
For a model near chance the floor's requirement is close to zero or below it
and is decided by one or two episodes; where it is not above zero, no site
set is usable (section 6.4, item 1).* The ruled sentence's "0.11 or more" was
true on neither reading of the figures (MEASURED: the inside review, RT-244,
`solver_sentence.py`), and its first clause is true of the text only with the
clause of section 6.4, item 1 (RT-238). With the channel left on, on seed 2,
33 of 45 site sets cleared the whole-state floor on fresh episodes by one or
two episodes of 800 while none cleared on development episodes, which is
where the nomination is made; had one been nominated, the piece rule would
have refused every size. **At 1,800 fitting episodes the solver's best piece
moved from 20 to 25 down to 17 to 20, and it still returns no reading**
(MEASURED: the page 4 re-run at `e948899`, section 2). What this shows and
what it does not is weakness W16: the solver fails the task, so its no verdict
shows the measure returns nothing on a model that has not learned the task,
not what the measure does on a model that does the task by another route.
The alternative that was put and not taken on 2026-10-04 (ruling 7): training
a solver that learns from another cue before the review. In the registered
experiment both solvers are scored on both conditions on the registered
episodes, as section 8.1 says.

### 7.4 What is frozen, and when

Committed to git, with the commit hash recorded in the registration file,
**before a single fresh episode is evaluated**:

- the label (which marker word), in code and in text, as the one registered
  read; the three route (b) candidates recorded as exploratory fits and not
  frozen as reads;
- **the fit floor: four fifths of held-out development episodes, on the piece
  that is transplanted and on the piece only, at the action position, stated
  as a count; the device the whole nomination and reading are computed on,
  the laptop's processor, and its number format; the pinned-versions file
  (section 7.2, item 1); and the permutation null beside it**;
- **the order of the piece rule: applied after the layer set is chosen, so
  it decides which sizes may be chosen and never which layers, with the
  sentence on what that order can miss** (reconciled 2026-10-03, night,
  record B ruling 2; section 7.2, item 3);
- **the piece's accuracy at the other positions of its site, both ways (each
  position, and the average over them), as reported figures with no pass
  line, and the method by which each is computed** (section 7.2, item 3);
- the site-set rule of section 7.2, the printed list it produces for the
  registered architecture (section 18), its two exclusions (all positions;
  layer 0 away from the action position set, as removal from the family), and
  the count of comparisons;
- the stricter layer-0 variant, as the sensitivity row;
- the rank caps (1, 2, 4, 8) and the registered cap (8);
- the nominated subspace and its size, per arm and seed;
- the whole-state layer set, per arm and seed, under the one registered
  reading of "the smallest that clears it", with the repairs-style sensitivity
  row named;
- the transplanting operation, as code, with its self-tests;
- all seven controls, and which hold: **control 7; control 1 on arm T;
  control 4 as redefined, on the positions before both twins' first own
  turns, with its pass line that the outputs are bit-identical, which is the
  registered check of the pairing**; the twenty-draw null of control 3 and
  its reported statistics; **control 2 as a reported description with no
  pass line, against twenty random pieces, from
  `control2_twenty_draws.control2`, with the statement that it has returned a
  figure on one toy model of six**; **control 6 as a description that cannot
  tell copying who is acting from copying the answer**; the pre-stated cells,
  the relaxed set for control 6 and its generating seed;
- **the in-use check on the built arms, both parts, with its bars as
  section 5.6 fixes them** (ruled 2026-10-08, `docs/rulings/2026-10-08-verification-bar-ruling.md`; the
  bar);
- **that the code withholds a reading when a control that holds, a floor, a
  gate, the channel-removal check or the in-use check fails, lists every
  reason, and keeps no withheld figure in its output** (section 6.4, item 5;
  rehearsal item R-13);
- the whole-state floor rule (four fifths, on the chance-corrected scale,
  with the requirement above zero, applied on development episodes at
  nomination and again on fresh episodes at the reading) and the no-verdict
  rules of section 6.4; **the no-transplant formula and its 0.018 room as a
  reported figure, not a veto, with the 0.56 detection chance printed beside
  it**;
- the separation bar between R1 and R2 (0.5), taken as the lowest of arm C's
  readings minus the highest of arm T's;
- **the eight registered outcome terms of section 3, their scope phrases,
  and the table of every state the registered runs can reach**;
- the gates of section 8: the own-directed bar on arms T, C and M, the
  learn-both bar on arm F, and the channel-removal rule: its collapse line
  and its ownership-free line (1,546 of 3,000), each counted on the same
  seeds as every other condition;
- **the seed rule: a seed counts only if it passes everything; two seeds of
  three** (section 3);
- **the training recipe of section 5.5, and the sharpness fixed at 4.0 in
  arms T, C and M** (section 5.6);
- the uncertainty method (section 9, 1g) and the seed count (three);
- **the numbers of episodes at the registered size (ruled 2026-10-03, late
  evening, ruling 4; the read's fitting count amended 2026-10-06, page 4):
  for every read, 1,980 development episodes, the first 1,800 fitted and the
  last 180 held out, so the floor is 144 of 180; the nomination's transplant
  passes on 600 development pairs, as rehearsed; 800 fresh matched pairs; 800
  pairs on the relaxed set; 3,000 held-out episodes for the gates, so the bar
  is 790 and the ownership-free line 1,546; 200 shuffles for the permutation
  null**;
- **(reconciled 2026-10-03, night) the band that sampling alone puts around
  every count taken against the four-fifths floor, printed beside it, as a
  95 per cent Wilson interval (the check of pull requests 88 and 89, section
  7, adopted 2026-10-04); the committed file that pins the library versions;
  and the separation as the lowest of arm C's readings minus the highest of
  arm T's** (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`);
- the reporting table's columns (section 7.5), including the rider;
- the predictions: arm T near zero; arm C high; arm M between 0.3 and 0.7 and
  within 0.10 of its true-slot reading on the same fresh episodes; arm F
  unknown and not predicted, and possibly no verdict.

Nothing on that list may be changed afterwards. If something on it turns out
to be wrong, the registered output is reported as it stands and the correction
is a separate, dated note beside it, the programme's existing practice, and
the process correction the outside review asked for: an immutable registration
is not an immutable scientific conclusion, but the two are kept visibly apart.

### 7.5 The reporting table

One row per arm and seed, with these columns, in this order, so that every
number a no-verdict rule or a caveat depends on is beside the reading it
bears on:

1. the nominated site set (layers, position set, size of piece);
2. **the whole read's held-out count at the nominated layer, and the chosen
   piece's own held-out count at the action position, each as a count of
   held-out episodes on the registered device, with the permutation null's
   95th and 99th percentiles beside them** (RT-212, RT-230, RT-232);
3. **the chosen piece's count at each other position of its site, and its
   count on the average over those positions, each with the whole state's
   count beside it; reported, with no pass line on either** (ruled
   2026-10-03; section 7.2, item 3);
4. whether the fit floor passes, **with the band that sampling alone would
   put around the count printed beside it, computed as a 95 per cent Wilson
   interval** (reconciled 2026-10-03, night: at 180 held-out episodes one
   episode is 0.0056, and a piece whose true accuracy is exactly four fifths
   passes about half the time; the method named by the check of pull
   requests 88 and 89, section 7, as the competing-solver run computed it,
   adopted 2026-10-04);
5. the whole-state, ownership-only and no-transplant accuracies on fresh
   episodes, the raw difference, and whether the whole-state floor clears in
   both forms, **on development episodes and again on fresh ones** (RT-234);
6. the no-transplant rate beside the formula of section 6.4, their
   difference, the share of errors landing on the donor's answer, **and the
   chance the formula would flag a broken pairing on 800 pairs (0.56 at the
   learn-both bar)**; reported, not a veto (RT-222 as amended by RT-248);
7. **control 3's twenty-draw null: median and 95th percentile of the random
   donor shares, the ownership-only share, and the counts below, equal and
   above** (RT-214);
8. the reading on the chance-corrected form, or the no verdict with its
   reason;
9. **the stricter layer-0 row**: the same columns with every layer-0 site set
   removed (RT-216);
10. the repairs-style sensitivity row for the whole-state layer set;
11. the rider: the reading at arm T's site set, or its no verdict with which
    of the two reasons applies;
12. the true-slot reference on arms T and M;
13. **the controls that hold, each with its pass or fail: control 7; control
    1 on arm T; control 4 as redefined, with the donor-value share, the
    no-transplant share and the number of trials whose action changed**;
14. **the controls that are reported: control 1 on arms C, M and F; control 2
    as a description (the own-directed action's share moved under the named
    agent's piece, beside twenty random pieces), or its no verdict with the
    reason; control 6's two cells**, each with its pre-stated expectation
    where it has one;
15. the channel-removal result on arm F (the collapse line and the
    ownership-free count, section 8.2), and, described, on the built arms;
    **on arm T, the row-choice split beside its gate** (section 5.1; open
    item 9);
16. **on the built arms, the in-use check: the sharpness as read from the
    model, the weight on the true agent, and the route use per built route,
    with pass or fail** (section 5.6);
17. and, across the three seeds of each arm, the across-seed spread of the raw
    difference with the within-seed bootstrap beside it (section 9, 1g),
    **labelled as the uncertainty of the raw difference only** (section 9).

**The report for the first full-size free-model run (step 5a of section 11)
prints more than its row (the review of version 3, RT-235; accepted
2026-10-03, page 3):** the read's held-out count at every layer, the chosen
piece's own count, and the candidates the nomination chose among. The reason:
on a model where no transplant moves anything, the layer the nomination lands
on is picked among sampling noise, so the stop of step 5a must not be decided
on one number from an arbitrary pick. The procedure has already computed all
three.

---

## 8. The gates every arm passes before it is read

### 8.1 The gate on learning: own-directed only on the constructed arms, both conditions on arm F

**The constructed arms T, C and M are gated on the own-directed condition
only; arm F keeps the learn-both gate (ruled, the Gate C rulings, RT-213,
item 1, refining the queue ruling's page 1b as it applies to arms T, C and M;
the bar itself is unchanged).** The reason recorded: the anchors' ownership
slot is built in by construction, their reading uses only the own-directed
action, and the named-other gate tests whether a free system learned to
represent ownership, which the anchors are not asked to prove. Arm F is not
read mechanistically until it has learned **both** conditions.

- Measured on held-out episodes, at the end of the token budget, on every seed
  carried.
- Reported as raw accuracy on each condition separately, on every arm, with
  its spread across seeds. Not combined into one number, not normalised by
  anything. The named-other condition is reported on arms T, C and M although
  it does not gate them.
- **The threshold, per condition (ruled, the queue ruling, page 1b):** the
  condition's accuracy is above the one-in-four level at the 0.05 level under
  a one-sided binomial test, **on at least two seeds of three, the same seeds
  passing every condition** (ruled 2026-10-06, page 7: a seed counts only if
  it passes everything; section 3). The ruling
  writes the bar as "above 0.2630"; on 3,000 held-out episodes that is 790 or
  more correct, a share of 0.2633 (MEASURED: the bar's derivation is printed
  in `docs/rehearsal-repairs-method-2026-09-25.md` at `882f252`, and
  `out-repairs/gate_base.json` carries it as the field `bar`; this session
  re-derived it by an exact binomial tail, section 17, failure 3); the
  registered measurement uses the same 3,000, so the bar is 790 there too
  (ruled 2026-10-03, late evening, ruling 4).
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and the **measured** accuracy of two competing
  solvers built at the rehearsal, one that cannot use ownership at all, one
  that uses only the name token (rehearsal item R-5; on the toy the
  ownership-blind solver scored 0.2340 to 0.2383 on the own-directed
  condition and the name-only solver 1.0000 on the named-other condition and
  0.2380 on the own-directed, `out-repairs/gate_base.json` at `882f252`;
  these were taken before the piece rule of 2026-10-03; the ownership-blind
  solver was put through the nomination under it on 2026-10-03 and returned
  no verdict on every seed, section 7.3, the last paragraph). **The gate does
  not apply to the competing solvers**; they are references (ruled
  2026-10-04, ruling 6: "would fail the gate if it were gated as the free
  model is", not "the gate stopped it").
- An arm that fails, after the experiment's one permitted re-run where it is
  still available, gives outcome **R3 for the experiment** (arm M excepted:
  it is dropped; arm F excepted after step 5a: section 3, rule 1), and the
  report says which arm, on which condition and on which seeds (ruled
  2026-10-06, pages 5 and 9, closing RT-241's hole 3).
- **What is already on the record about this gate (MEASURED: the earlier
  re-run's findings at `9d9d31a`, Part 1, section 1.2, whose gate counts
  equal `out-repairs/gate_base.json` field for field; the controls re-run of
  2026-10-03 read the gate from that committed file and did not run it
  again):** arm T clears both
  conditions on 3 seeds of 3; arm C clears the own-directed condition on 3 of 3
  and the named-other on 0 of 3 (760, 751 and 708 of 3,000), and passes its
  gate; arm M clears both on 3 of 3 and passes; arm F clears the own-directed
  on 3 of 3 and the named-other on 1 of 3 (994, 781 and 746), and **fails**.
  No training change fixed the free arm's failure (section 4.4).

### 8.2 The channel-removal check, for arm F only

Before arm F is read, the acting channel is zeroed at evaluation, the lesion
the existing code already performs. **The pre-stated shape (ruled, the queue
ruling, page 1h; refined by the Gate C rulings, RT-220; its last clause
replaced 2026-10-06, page 1, in John's words "(a), go with the
recommendation", closing the inside review's fatal finding RT-237; its seed
counting amended 2026-10-06, page 7):**

- **own-directed accuracy falls below the section 8.1 bar**: that is the
  collapse, and it gates;
- **arm F is read if at least two of three seeds collapse, the same seeds
  that pass every other condition, with the third reported** (the RT-220
  ruling, as amended by page 7: the collapse is no longer counted across
  seeds separately). A separate collapse bar below the learn-both bar was
  considered and not taken, because it adds a second pre-stated number nobody
  has rehearsed. What the two-of-three clause is for: because the collapse
  line *is* the learn-both bar, it sits just above the level a fully
  collapsed arm is expected to reach, and an arm whose lesion drops it to
  exactly one in four is read as "not collapsed" 4.85% of the time per seed
  (MEASURED: section 17, failure 3, the exact binomial tail at 790 of
  3,000). One seed of three misreading that way must not stop arm F being
  read;
- named-other-directed accuracy is **reported and not gated**; the pre-stated
  expectation that it holds is a description, because the rehearsal found
  that shape is architecture-specific (`docs/2026-09-21-successor-measure-rehearsal.md`,
  section 8);
- **the part of the act that needs no ownership must hold** (replacing, by
  John's ruling of 2026-10-06, the clause "the ownership-free state and
  syntax batteries must hold", which was written for the closed design's
  end-of-episode question sets; the successor's task has none, the clause set
  no line, no record exercised it, and by stop condition S8 an unevaluable
  gate counts as failed, so as written the free model could never have been
  read: the inside review of version 4, RT-237, fatal; the outside review's
  A1 and G5 repeat it). With the acting channel zeroed, the model's
  own-directed answer must still be the successor of one of the four agents'
  earlier values on the item named, the four answers that remain open once
  "which agent am I" is taken away, on **1,546 or more of the 3,000 held-out
  gate episodes**, on at least two seeds of three, the same seeds, the third
  reported. 1,546 is the smallest count above one half at the 0.05 level,
  one-sided, by the exact binomial tail; one half is what a model guessing
  among the eight value words reaches. The count is written to the gate's
  output file beside the lesioned accuracy, as the field the clause is
  evaluated on (the decision code of pull request 105 carries the field; its
  case 17, "ownership-free line never ran on arm F", gives the fifth term
  with the reason "not run"). The same count on the named-other condition is
  reported and not gated. **The gate's code writes, for every arm and seed,
  the lesioned own-directed count and the lesioned candidate count, so that
  every clause of every gate is evaluated on a named field.** This amends
  page 1h of the ruling of 2026-09-26 and sits beside, not in place of, the
  collapse rule of RT-220.

**What the replacement shows and does not show (MEASURED, a rehearsal record
and not a result: `docs/2026-10-04-gate-a-v4-dispositions-measurements.md`,
part A, from `out-lesion-content-check/lesion_content_check.json`, on branch
`rulings-2026-10-06-gate-a-v4` at `525a625`; checked in pull request 96).**
With the channel zeroed, arm F's own-directed answer is one of the four
candidate values on 2,100, 2,238 and 2,324 of 3,000, against 1,546; arms T, C
and M and the ordinary competing solver clear the line on every seed; three
models of arm F's architecture with untrained weights reach 0, 620 and 726
and do not. So the check refuses a model that answers with noise and passes
every trained toy model by 554 episodes or more. It shows that the model
still answers with the successor of a value it was shown; it does **not**
show that the model still uses the right item: a model that had lost which
item the action names, and answered the successor of any of the eight values
shown, would score about 2,257 of 3,000 and pass, and the line cannot be
raised to catch that without failing arm F on two seeds and arm C on all
three (the check of the inside dispositions, pull request 96, section 6). The
registered sentence claims exactly what the check shows and no more. The
alternative that was put and not taken: strike the clause with its reason on
the record.

**What this check does and does not establish, in the closed design's own
registered words: it removes a sense organ, not a structure the network
built.** It is a precondition for reading arm F, since it shows the ownership
answer is load-bearing for the act, which is what makes arm F worth
measuring; it is not evidence of a centre and is never reported as such
(ruled 2026-10-03, decision 10).

Arms T, C and M do not take this check as a gate: their dependence on
ownership is architectural, and since 2026-10-06 hand-set (section 5.6),
with the in-use check in its place. Their lesion results are computed and
reported as a description of the constructed systems. **On the toy, described honestly
(ruled, the Gate C rulings, RT-220):** arm T collapses on two of three seeds,
at 0.2467 and 0.2510, and its seed 2 reads 0.2733 against the bar of 0.2633,
so under the rule it did not collapse there; arms C and M collapse on all
three (0.1703 to 0.1830 and 0.2190 to 0.2230); arm F, the arm this gate is
for, collapses on all three, at 0.1760 to 0.1940 (MEASURED:
`out-repairs/gate_base.json` at `882f252`, fields `lesioned_own` and
`lesion_collapses_own`; section 17, failure 3, prints them). Version 2's "all
three collapse" was wrong for arm T seed 2 and is replaced.

---

## 9. The numbers, now set

Every number version 1 deliberately left blank is filled from John's rulings
of 2026-09-25, 2026-09-26 and 2026-10-03, each citing the ruling that set it.
**None was invented here.** The registration text freezes them in this form.
The device row and the last row, the numbers of episodes, were open when this
version was first filed and were ruled the same night.

| Number | Set to | Ruled in |
|---|---|---|
| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap between arm C's reading and arm T's, on the chance-corrected form, **taken as the lowest reading among arm C's seeds that read minus the highest among arm T's, not paired by seed number**; the rule forgives a seed that returns no verdict and not one that returns an odd reading | `docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a, which does not say how the gap is taken across seeds; `docs/rulings/2026-10-03-version-4-questions-rulings.md` (record B), ruling 6, which stands by the reconciliation; the check-questions ruling of 2026-10-03, ruling 2. On the toy, with every read fitted on 1,800 development episodes, the separation is **1.0000** (arm C's three readings 1.0026, 1.0000 and 1.0000; MEASURED: the page 4 re-run at `e948899`, from `out-page4-rerun-1800/models-1800/summary.json`); at 420 it was 0.9926 (the controls re-run at `821f154`). Version 3's 1.0051, 1.0025 and 1.0000 were read on two seeds through pieces that do not hold the label and are superseded (the review of version 3, RT-230) |
| Gate on learning (R3) | above one in four at the 0.05 level, one-sided binomial, **on at least two seeds of three, the same seeds passing every condition**: **0.2633 on 3,000 held-out episodes** (790 or more correct); **on the own-directed condition only for arms T, C and M, on both conditions for arm F**; the ownership-blind and name-only solvers reported beside it as references, not gated | the queue ruling, page 1b; the Gate C rulings, RT-213, item 1; the seed rule, the 2026-10-06 ruling, page 7 (RT-249) |
| Fit floor | **four fifths of held-out development episodes, on the piece that is transplanted, at the action position**, per arm and seed, stated as a count (144 of 180), **every read fitted on 1,800 development episodes with the last 180 of 1,980 held out**; only sizes whose piece reaches it may be chosen; the whole read's count printed beside it and not a second floor; the permutation null reported beside it and not used as the bar; the order of the piece rule stated with what it can miss | the rulings on the review of version 2, RT-212, item 1; per arm and seed, and the read itself, ruled 2026-09-26 (decisions 21 and 23); moved to the piece by `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 1; on the piece only, and applied after the layers are chosen, by record B, rulings 1 and 2 (`docs/rulings/2026-10-03-version-4-questions-rulings.md`), which says the registration states what the order can miss; the fitting count by the 2026-10-06 ruling, page 4 (RT-240) |
| The piece's accuracy at the other positions of its site | **reported both ways, with no pass line on either**: a count at each other position, and a count on the average over them, computed as section 7.2, item 3, states | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 2 |
| The device and number format of the whole nomination and reading | **the laptop's processor, for every forward pass, every transplant pass that chooses the site set, and every fit; the figure computed there is the registered one.** States in 32-bit, the read fitted in 64-bit by scikit-learn, every library version written to the output file, **and pinned in `experiments/08-successor-degree/requirements-measure.txt`**; if the processor proves impractical at full size, a fresh question for John, not a switch | the review of version 3, RT-232, accepted as the review states it by the rulings of 2026-10-03, page 3; the device by record B, ruling 3 (`docs/rulings/2026-10-03-version-4-questions-rulings.md`); widened to the whole nomination by the 2026-10-06 ruling, page 6 (RT-245) |
| Whole-state floor (whether a site set is usable) | **four fifths of the arm's own own-directed accuracy**, on the chance-corrected scale, **with the requirement above zero; where it is not, no site set is usable**; **applied on development episodes at nomination and again on the fresh episodes at the reading; a site set that clears the first and misses the second returns no verdict**; the whole-state layer set is **the smallest that clears it, per position set, then the highest ownership-only share among those**; every all-positions site set excluded; every layer-0 site set removed at position sets other than `action` | the queue ruling, page 1c; the repairs rulings, items 3 and 4; the rulings on the review of version 2, RT-216, item 1, as clarified by refinement item 2; the review of version 3, RT-234, accepted 2026-10-03, page 3; the requirement above zero by the 2026-10-06 ruling, page 2 (RT-238) |
| Rank cap on the nominated subspace | **8**, with the family reporting caps 1, 2, 4 and 8 | the queue ruling, page 1d |
| Candidate site list and its family correction | the rule of section 7.2, printed for the registered 12-layer model: **325 site sets and 1,300 comparisons** with layer 0 kept at the action position set only (45 and 180 on the toy); the count is the rule's output, not hand arithmetic | the queue ruling, page 1e; the repairs rulings, item 3; the Gate C rulings, RT-215 and RT-216; the reading of the layer-0 exclusion ruled 2026-09-26 (decision 20) |
| Control 3 | **a twenty-draw null, reported and not gated**: median, 95th percentile, and the ownership-only share's place among the draws | the rulings on the review of version 2, RT-214, items 1 and 2, as refined on 2026-09-26, refinement item 1 |
| Control 2, the other-agent control | **no pass line.** A reported description, beside twenty random pieces from `control2_twenty_draws.control2`, the 95th percentile as the summary and all twenty printed; the 0.05 tolerance of version 3's decision 15 is withdrawn and not registered; the registration says the control has returned a figure on one toy model of six, at 1,800 fitting episodes | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1; the twenty by record B, ruling 5, and the check-questions ruling of 2026-10-03, ruling 1; the function and the summary by the 2026-10-04 ruling, rulings 4 and 5 |
| Control 4, the too-early-position control | **holds; its pass line is that the outputs with the transplant are bit-identical to the outputs without it**, on the positions before both twins' first own turns, at the nominated layers; a failure withholds the reading for that arm and seed; **it is the registered check of the pairing** | the same file, ruling 2, reversing that morning's ruling on version 3's decision 16; the pairing role by the 2026-10-06 ruling, page 8 and follow-up item 3 (RT-248) |
| What a no verdict maps to | the table of section 3: arm C: the fallback, the sixth or seventh term; arm M: arm M is dropped and carried as an extension; arm F after arms T and C separate: **the fifth term, satisfactory and stated as weaker than R1**; arm T: the eighth term, not satisfactory; a built arm whose route is not in use: no verdict for that seed, "construction did not hold" | `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 1; the 2026-10-06 ruling, pages 5 and 9 (RT-241, RT-249); the renaming by the 2026-10-07 ruling, decision 3 |
| Seed count per arm | **three**; the toy arithmetic implying one seed was not carried across | the queue ruling, page 1f |
| Uncertainty across seeds | **the across-seed spread of the raw difference** is the registered uncertainty; the within-seed bootstrap over matched pairs is reported beside it; neither measures drift between runs of one seed, and the registration says so. **This is the spread of the raw difference, not of the reading, whose denominator moves too, and not of the separation between arms T and C, which is a decision rule on point figures. Neither the reading nor the separation has a registered uncertainty; both are reported as descriptions. The sampling band printed beside a piece's count does not account for that piece having been chosen on the same held-out episodes** | the queue ruling, page 1g; on the repairs run the two disagreed by more than two to one on arms C and F (the repairs findings at `882f252`, section 6.2; figures at pre-rule site sets, not carried); the labelling by the 2026-10-06 ruling, follow-up item 1, closing the outside review's A12 (RT-254) |
| Channel-removal check (whether arm F is read) | own-directed accuracy **below the learn-both bar** with the acting channel zeroed, **on at least two seeds of three, the same seeds passing every other condition, the third reported**; the named-other clause reported and not gated; **with the channel zeroed, the own-directed answer is one of the four candidate values on 1,546 or more of 3,000 gate episodes, on two seeds of three**; gates arm F only | the queue ruling, page 1h; the Gate C rulings, RT-220; the ownership-free line by the 2026-10-06 ruling, page 1 (RT-237), amending page 1h; the same seeds by page 7 (RT-249) |
| The in-use check (whether a built arm's seed counts) | **part A: the built-in answer's weight on the true agent at least 0.9; part B: route use at least 0.5 on every built route; ruled 2026-10-08 at these figures (`docs/rulings/2026-10-08-verification-bar-ruling.md`)**; a failure gives no verdict for that seed, "construction did not hold" | the 2026-10-07 ruling, decision 3, and the flat-models packet's option 4; the bars from `docs/2026-10-06-sharpness-fix-inuse-check-method.md`, branch `fix-sharpness-inuse-check` at `644238e`, not ruled |
| The no-transplant allowance | **at most the largest measured miss, rounded up to 0.018; reported, not a veto**: the rate beside `(1 − p) / 7`, their difference, the share of errors on the donor's answer, and the chance of flagging a broken pairing on 800 pairs (0.56 at the bar); the pairing checked by control 4 and the generator's self-test | the queue ruling, page 2; the Gate C rulings, RT-222, as amended by the 2026-10-06 ruling, page 8 (RT-248) |
| The form of the reading | **the chance-corrected form** of section 6.3 | the queue ruling, page 2 |
| The label | **which marker word is the model's own**, the one registered read; the route (b) candidates recorded as exploratory fits only | `docs/rulings/2026-09-23-nomination-label.md`; the queue ruling, page 3; the Gate C rulings, RT-212, item 3; John's ruling of 2026-09-26 on the route (b) result (section 7.2, item 1) |
| Seconds per step, per arm, on the rented machine | **Measured 2026-09-25 for arms T, C and F**: 13.08, 13.52 and 12.53 milliseconds per step, ratios to arm F of 1.044, 1.080 and 1.000, on a secure RTX 5090 at $0.99 an hour, at the registered shape, fifty timed steps after five warm-up steps | `docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 3, from `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json`; checked at `afb5183`, point 5. **Arm M was not timed.** **Fifty timed steps are accepted for the second release's arithmetic; the five-hundred-step figure is taken from the first full-size run, and the later runs are repriced from it before the second release is asked for** (ruled 2026-10-03, decision 17) |
| Arm M's predicted reading | between **0.3 and 0.7** on every seed, and within **0.10** of its true-slot reading on the same fresh episodes (the formula of section 5.3, which is that reading written in route accuracies). On the toy under the registered rules: 0.4886, 0.4860 and 0.5449, within 0.0049, 0.0099 and 0.0529 of the true-slot reading | the queue ruling, page 5 (the band); the repairs method note at `882f252`, section 5 (the formula and the 0.10); the rulings on the review of version 2, RT-223; the toy figures from the review of version 3, RT-231, and the controls re-run at `821f154` |
| The numbers of episodes at the registered size | **for every read, 1,980 development episodes, the first 1,800 fitted and the last 180 held out (the floor is 144 of 180); the nomination's transplant passes on 600 development pairs, as rehearsed; 800 fresh matched pairs; 800 pairs on the relaxed set; 3,000 held-out episodes for the gates (the bar is 790; the ownership-free line 1,546); 200 shuffles for the permutation null.** The caution carried with it: at 180, one episode is 0.0056 of the scale. **The band that sampling alone puts around each count against the floor is printed beside it, as a 95 per cent Wilson interval** | record B, ruling 4 (`docs/rulings/2026-10-03-version-4-questions-rulings.md`) and the reconciliation; the read's fitting count amended by the 2026-10-06 ruling, page 4 (RT-240), for the read only; the band's method adopted 2026-10-04 from the check of pull requests 88 and 89 |
| An arm whose three seeds disagree | **a seed counts only if it passes every gate condition and every check that withholds a reading, and returns a reading; two seeds of three decide, the third reported**; separate counts per condition are not used. **The separation is the lowest of arm C's readings minus the highest of arm T's, among the seeds that read, and is not compared seed by seed** | record B, ruling 6, as amended by the 2026-10-06 ruling, page 7 (RT-249) |
| The training recipe | **the frozen trainer's defaults** (section 5.5): AdamW, peak learning rate 0.002, weight decay 0.01, one-cycle schedule with a tenth of the steps as warm-up, gradients clipped at 1.0, 96 episodes a step, 585,544,960 tokens in 108,919 steps, fresh training episodes excluded from every evaluation set and from fresh and relaxed pairings | `experiments/08-successor-degree/src/train_successor.py` at `53ae82c`; **not ruled** (open item 5) |
| The spending alarm's cadence | **every 5 minutes while a machine runs, and for 30 minutes after the last deletion; rule S in flight and rule D at each deletion** (section 12.5) | the flat-models packet, page 2, reported ruled 2026-10-06 in `docs/2026-10-06-tripwire-fixes-method.md`, section 1 (branch `tripwire-fixes` at `5e2faf9`); no rulings file (open item 2) |

---

## 10. The rehearsal: what it was, and where each item stands

A complete measurement rehearsal before any Gate A is protocol
(`docs/outside-review-protocol.md`, "The measurement rehearsal, required
before any Gate A"). **The toy runs are development and rehearsal evidence**
(ruled 2026-10-06, follow-up item 1, closing the outside review's A8, adopted
as RT-252). Controls, gates and site exclusions were changed after toy
outputs were seen, and some fresh episodes were reused to assess changed
rules; committing a method before re-running already-inspected models does
not make them untouched. No toy figure is an independent test of the frozen
procedure; the registered runs, on unused episodes, are the first. The
rehearsal ran in five parts, and then in six more since version 4 (R-12 to
R-15 and the page 4 re-run, below), all at toy scale on the laptop
except one item: the rehearsal of 2026-09-21
(`docs/2026-09-21-successor-measure-rehearsal.md`, code in
`experiments/rehearsal-successor-measure/`, re-run from code on 2026-09-22
with the separable arm reproducing exactly and the other two not); the
repairs of 2026-09-25 (`docs/2026-09-26-rehearsal-repairs.md` at `882f252`,
code and outputs under the same directory's `src/repairs.py` and
`out-repairs/`, checked at `d216dbc`); and the re-run of 2026-09-26 under this
version's rules (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, code
`src/rerun_v3.py`, outputs `out-v3-rules/`, checked at `70be9fb`); **the
controls re-run of 2026-10-03 under the piece rule**
(`docs/2026-10-03-controls-rerun.md` at `821f154`, method
`docs/controls-rerun-method-2026-10-03.md`, code `src/rerun_controls.py`,
outputs `out-controls-rerun/`, checked at `e184a6e`), which the rulings of
2026-10-03, page 2, made a precondition of the registration review; **and the
short pre-stated run of the same day** (`docs/2026-10-03-short-prestated-run.md`
at `853988f`, method at `9e978d9`, code `src/short_prestated_run.py`, outputs
`out-short-prestated-run/`; checked by a second session, main line at
`53c8100`). The
last two loaded the twelve committed base-recipe models, checked each file's
fingerprint against the committed list before loading it, trained nothing and
spent nothing. The one part that spent money is item R-11. Total spent on the rehearsal so far:
about $0.57, the sum of the compute ledger's three slice rows, of the
rehearsal line's $10 (item 10 of the 2026-09-21 ruling; section 12.3).

**The models every toy result rests on: thirty, all committed.** The fifteen
trained toy models behind the repairs and the re-run (arms T, C, F and M and
the ownership-blind solver, three seeds each) are committed at
`experiments/rehearsal-successor-measure/out-repairs/models/` (main line at
`8038275`, pull request 64), because they cannot be rebuilt from code and
seed (the repairs check at `d216dbc` retrained from clean and got different
nominations) and an uncommitted record the reader cannot open is the form of
ledger item RT-145. The other fifteen are committed too (main line at
`7ed2b0e`, pull request 67): the six free-arm models behind the two training
redesigns that failed (`ckpt_F_curriculum_seed*.pt` and
`ckpt_F_reweight_seed*.pt`, in the same folder) and the nine behind the
grammar attempt (arms T, C and F, three seeds each, at
`experiments/rehearsal-successor-measure/out-grammar-c/models/`). One
fingerprint list, `out-repairs/models/SHA256SUMS`, covers all thirty, with a
`README.md` beside it saying where each file came from. The re-run's
fingerprint check compared three recorded hashes per file with the list for
the first fifteen and found all agree, its check hashed the stored files
themselves and found the same, and the label-search check found all thirty
files on the main line check against the list (MEASURED:
`out-v3-rules/models_sha256_check.json`, `all_agree: true`; the check at
`70be9fb`, section 2.1; the label-search check at `ecd2b6c`, section 4).
**What rests on them: every toy result of 2026-09-25 and 2026-09-26 that
this version quotes.** On the first fifteen: every base-recipe result of the
repairs (`gate_base.json`, `nominate_base_*.json`, `measure_base_*.json`,
`summary_base.json`, the training records `train_*_base_seed*.json` and the
`F/base/*` rows of `diagnose_named_other.json`), the whole of
`out-v3-rules/`, the label search's fits, the whole of
`out-controls-rerun/` and `out-short-prestated-run/` (which use the twelve
models of arms T, C, F and M and not the solver's three), and every toy
figure in sections 3, 5, 7, 8 and 9 of this version. On the six redesign models: the curriculum and
loss re-weighting results of section 4.4 (0 of 3 seeds each). On the nine
grammar-attempt models: the grammar attempt's figures of section 4.4 (774,
730 and 759, and everything in `out-grammar-c/`). Two kinds of figure quoted
in this version are not toy results and rest on no committed model, and are
said to be what they are where they appear: the rented slice's seconds per
step (section 9), a timing of a model that exists on the record as a
checksum only; and the two checks' own re-run figures (the grammar check's
750, 809 and 739; the repairs check's 6 of 12), which are the checks'
verification of a verdict, quoted as such, from retrainings those checks
recorded but did not keep. Decision 22, which asked whether the further
fifteen should be committed, is done.

**A pre-stated quantity the rehearsal never exercised is a fatal finding on
its own** (item 5 of the 2026-09-21 ruling). Each item below therefore says
what exercised it.

- **R-1. The grammar works and both conditions are learnable at tiny scale.**
  The four matched properties hold (P-1). The own-directed condition learns on
  every arm. **The named-other condition does not clear the bar on the free
  arm on a majority of seeds, under any of three training recipes or under
  the grammar change, and does not clear it on arm C on any seed** (760, 751
  and 708 of 3,000; section 4.4 and section 5.2). Stop condition S1 is ruled
  not to have fired; fallback (d) registers; the constructed arms are gated on
  the own-directed condition only. *Exercised; the finding is the honest
  prior, measured.*
- **R-2. Arm T is constructible and its ownership slot is transplantable on
  its own, and so is arm M's separable route.** The blind nomination finds
  arm T's slot without being told where it is, on every seed, and reads
  0.0000 under the registered rule and under the stricter variant; on arm M
  the blind subspace's ownership-only transplant moves 0.37 to 0.41 of trials
  against random medians of 0.015 to 0.019 (the controls re-run at `821f154`,
  sections 2 and 4). *Exercised.*
- **R-3. Arm C is constructible and its degree is genuinely known by
  construction, and arm M's mixture reads between the anchors in its
  pre-stated band.** On arm C the read holds the label, the piece
  transplanted holds it at the action position (180, 172 and 150 of 180), and
  the ownership-only transplant lands within 0.004 of the no-transplant rate
  while the whole state moves the action, so it reads 1.0051, 0.9926 and
  0.9974; arm M reads 0.4886, 0.4860 and 0.5449 against a band of 0.3 to 0.7,
  and within 0.0049, 0.0099 and 0.0529 of its true-slot reading at the
  registered site sets (sections 5.2 and 5.3). **With every read fitted on
  1,800 development episodes, as now registered: arm C reads 1.0026, 1.0000
  and 1.0000 and arm M 0.5252, 0.4793 and 0.5208, each within its tolerance
  of its true-slot reading; the two arm C pieces nearest the floor rose from
  172 and 150 to 178 and 165 of 180** (MEASURED: the page 4 re-run at
  `e948899`, section 2; checked at `1e168f3`, 40,855 values recomputed, none
  different). **Arm C fails the named-other condition on every seed and
  passes its gate on the own-directed condition** (section 5.2). *Exercised
  under the registered rules on the learned-sharpness toy models; the
  two-arm fallback does not fire there.* **At 10 million parameters the
  condition this item tests failed in arms C and M, and the repaired,
  hand-set arms have been shown to learn the task and to keep the sharpness
  at 4.0 but have been read on one model of nine** (section 5.6); the three
  reruns of section 11, step 4b, are where this item is exercised on the
  repaired arms. The check of arm M's reading against its true-slot reading,
  which version 3 listed as owed, is done.
- **R-4. All the measure's outcomes are reachable.** Near zero (arm T), high
  (arm C), the middle (arm M), negative (the unseen-vocabulary diagnostic,
  section 7.1; and arm T seed 0 on the grammar attempt's unseen pool, at
  −0.1870), above one (arm C at 1.0051), and no verdict (arm F on every seed,
  by the gate and by the fit floor; control 2 on five toy models of six at
  1,800 fitting episodes; the ordinary competing solver on every seed under
  both readings; arms C, M and F at 10 million parameters). *Exercised.*
- **R-5. Ordinary competing solvers are built and measured.** The
  ownership-blind solver and the name-only solver, both scored on both
  conditions (section 8.1). *Exercised under the piece rule on 2026-10-03,
  and checked: no verdict on every seed under both readings of the solver,
  best piece 20 to 25 of 180, the whole-state floor cleared at nomination
  nowhere* (section 7.3, the last paragraph; `docs/2026-10-03-competing-solver-run.md`,
  main line; the check in pull request 90).
- **R-6. The arithmetic is finite.** The chance-corrected form's denominator is
  kept off zero by the whole-state floor **together with the gate and the
  requirement that the floor's right-hand side be above zero** (section 6.4,
  item 1; the check of pull requests 88 and 89, section 5.4, and the inside
  review's RT-238): on the toy's competing solver, which fails the gate, the
  printed floor alone was cleared on fresh episodes with a divisor of one or
  two episodes in 800, and the clause refuses it. The smallest toy
  denominator under the registered rule is 0.4863, arm C seed 2, among the
  pairs that read, and 0.4263 on arm F seed 0, which is described and not
  read (section 17, failure 1); the no-transplant formula was checked
  against nine arm-and-seed pairs on 2026-09-21 and twelve on 2026-09-25;
  two made-up systems of equal true share and unequal transplant strength
  read the same under the registered form (section 6.3). *Exercised.*
- **R-7. Throughput, per arm, projected to dollars.** Done from item R-11's
  measured ratios on the lifetime-priced cost of a registered-size run
  (section 12.4). *Exercised for arms T, C and F; arm M's runs are priced from
  ledger rows.*
- **R-8. The transplanting code passes its known-answer tests.** The null
  transplant leaves every logit bit-identical on every arm and seed; the
  ownership-only transplant is proved a restriction of the whole-state one;
  a transplant on arm T moves the action to the donor's value. *Exercised*
  at fifteen different places on the toy (section 7.3, item 7), which closes
  the citation gap version 3 recorded.
- **R-9. The uncertainty method is chosen.** Ruled (section 9, 1g) from both
  methods computed on the same data. *Exercised.*
- **R-10. The separation bar is set.** Ruled at 0.5 from a toy separation of
  0.873 to 0.885 on 2026-09-21; a separation of 0.9926 under the registered
  rules on 2026-10-03 (the lowest of arm C's readings minus the highest of
  arm T's), and 1.0000 with every read fitted on 1,800 development episodes
  (the page 4 re-run at `e948899`). *Exercised.*
- **R-11. Seconds per step on the rented machine, all three arms, and the
  shutdown path against the real vendor.** Measured on 2026-09-25 on the
  second attempt at the rented slice, after a first attempt that hung and was
  stopped with neither measurement taken (`docs/2026-09-25-rented-slice-findings.md`,
  main line). Throughput: **PASS**, three figures with their spread, fetched
  home (section 9), checked character for character against the launcher's
  log (the check at `afb5183`, point 5). The shutdown handshake: **the laptop
  half passed against the real vendor, copy, checksum, receipt written,
  delete, confirmed gone, and the machine half was not exercised**, because
  the laptop deletes the machine in the same second it writes the receipt, so
  the machine's own "receipt found" can never be observed on the normal path
  (MEASURED and ARGUED: `docs/2026-09-25-rented-slice-attempt-2-findings.md`
  at `9f802db`, section 4; the check at `afb5183`, points 7 and 8). None of
  the slice's six pre-stated handshake lines fits, and the findings do not
  force one. **Both things this left open were ruled on 2026-10-03**: fifty timed
  steps are accepted for the second release's arithmetic, with the
  five-hundred-step figure taken from the first full-size run (decision 17);
  and the registration says what is true of the handshake today, that on the
  normal path the laptop deletes the machine and the machine's own watcher is
  a backstop (decision 18; weakness W9). Cost:
  about $0.57 across three rows against the item's $3 (section 12.3).

- **R-12. The decoy test (ruled 2026-10-06, page 10, "yes, run it, go with
  the recommendation", closing the outside review's A6, adopted as RT-247).**
  Arm T's committed toy models with 24 extra numbers bolted onto the running
  state carrying an exact, causally unused copy of the owner's marker, at
  four times the ownership block's scale and at a quarter of it (and, beside
  the verdict, at sixteen times and a sixteenth), run through the registered
  nomination and reading unchanged; method committed before the run. **Not
  fooled, both ways round, on every seed: reading 0.0000 on all six runs**
  (and on the four supplementary ones), the same site chosen as on the
  unaltered model, although at scale 4 the transplanted piece lay about 94
  per cent in the unused copy (0.9370, 0.9341, 0.9382 by squared size)
  (MEASURED: `docs/2026-10-06-decoy-test.md`, branch `decoy-test-a6` at
  `6794155`, from `out-decoy-test/table.md`; reproduced exactly by its check,
  `docs/2026-10-06-check-decoy-test.md`, branch `check-decoy-test-a6` at
  `ba5d64f`). **What the check adds, and this text carries as weakness W18:**
  an exact copy could not have fooled the read (the fitted directions carry
  the block along in step with the copy, as the test's own method predicted),
  so "not fooled" is a correct result and not evidence that the read resists
  a decoy; and in the check's probe, not a ruled test and skipping the
  registered nomination, an unused one-of-twelve code of the owner's marker
  at four times the block's size gave readings of **0.28, 0.23 and 0.29** at
  the site the test always chose with 8 directions, and 0.52 to 0.96 with
  fewer, which under the test's own bands is "inconclusive", not "not
  fooled". *Exercised in its ruled form; the differently coded decoy is
  untested as a ruled test (open item 8).*
- **R-13. The final decision procedure, run end to end before registration
  (ruled 2026-10-06, follow-up item 6, closing the outside review's fatal
  finding A2, adopted as RT-256).** The module that turns per-seed records
  into one registered term (`experiments/08-successor-degree/src/measure.py`
  and `procedure.py`, `summarise`, on the main line at `bd0de26`) was brought
  to the rulings of 2026-10-06 (the outcome table, the seed rule, the
  ownership-free line, the no-transplant rate reported and not withheld,
  every reason listed, the withheld figure removed) and run on the toy's
  committed records, giving R3 as the toy actually is, and on 25 made-up
  cases, each landing on the term written beside it before it ran, among
  them R1, R2, R3, the fifth term, both fallback terms and "metric not
  validated" (now the eighth term); no withheld reading appears in its
  output file or its table (MEASURED: `docs/2026-10-06-successor-a2-decision-procedure-findings.md`
  at `bd0de26`, from `out-a2-cases/results.md`; checked at `e6dd8fa`, 22 of
  22 recomputed from the ruling text with independent code, and at `f609c9d`,
  25 of 25, with each floor switched off changing a case). The in-use check
  of section 5.6 was then added to the same module with three more cases, 28
  of 28 landing as written (branch `fix-sharpness-inuse-check` at `644238e`;
  owed its check). The registered runs use this code unchanged. *Exercised.*
- **R-14. The four development runs at 10 million parameters (step 4 of
  section 11; John's go in the ledger rows, "ok it's plugged in, launch it"
  and "all four is right, keep them running").** The frozen trainer ran end
  to end on a rented machine for every arm, arm M for the first time; the
  shutdown order worked for every run; the time per step was measured on the
  card (arm M 1.44 times arm C's); the four cost $0.47, $0.34, $0.33 and
  $0.33, $1.47 in all, against estimates of $0.60 to $1.25 each; the spending
  alarm did not meet real billing (it read once an hour, never during the
  29-minute wave, and its one real figure was 0.401 where the true figure was
  0.990) (MEASURED: the check of the development runs, branch `check-dev-10m`
  at `51ec07d`; the compute ledger's four 2026-10-04 rows). **And the built
  arms' ownership answer went flat in arms C and M** (section 5.6). *A
  pipeline and throughput check, as registered; exercised. What it found
  about the arms is the amendment of section 5.6; what it found about the
  alarm is section 12.5.*
- **R-15. The toy retrain with the sharpness fixed (section 5.6).** Nine
  models, the committed recipe, the number fixed at 4.0: every seed clears
  the learning bar, none loses more than 36 of 3,000 own-directed answers;
  arm T seed 0 re-read at 0.0000 as before; the in-use check's second part
  fails every arm C and arm M seed before and after the fix (MEASURED:
  `docs/2026-10-06-sharpness-fix-inuse-check-findings.md`, branch
  `fix-sharpness-inuse-check` at `644238e`, section 4). *Exercised for
  learning and for the fix; eleven of twelve re-reads owed; owed its check.*

**The page 4 re-run (ruled 2026-10-06, page 4).** The twelve toy models and
the competing solver, with every read fitted on 1,800 development episodes:
first the reproduction of the committed 420-fitted record from the committed
code (29,154 and 11,712 values, none different), then the 1,800 pass. No toy
decision moves; none of its seven pre-stated concerns happened; its figures
are quoted in sections 3, 5 and 9 (MEASURED: `docs/2026-10-06-page4-toy-rerun-1800.md`,
branch `page4-toy-rerun-1800` at `e948899`; checked at `1e168f3`). Two of
its records are carried: its outcome line was made under the rules frozen
before pull request 105 and must be summarised again with the current
decision code before it is quoted as an outcome (this text quotes its
per-model figures only); and the two-hour time limit its method set was
reset to three hours by the coordinating session, an agent's call and not
John's, after the laptop's load fell.

**The seven controls, and what exercised each under the registered rules.**
Controls 1, 3, 6 and 7, the true-slot reference, the rider and the stricter
row: the controls re-run, on all twelve toy models, checked (section 7.3), and
again with every read fitted on 1,800 development episodes in the page 4
re-run, checked (above). Control 4 as redefined: the short pre-stated run, on
all twelve, **checked: the check of the short run at `53c8100`**; the same fact
was measured independently, with separately written code, by the check of the
controls re-run (section 7.3, item 4). Control 5 holds by construction, and
since 2026-10-06 by the training stream's refusal of every fresh and relaxed
pairing (section 4.3). **Control 2 has returned a figure on one toy model of
six, at 1,800 fitting episodes, and the registration says so in terms**
(section 7.3, item 2). It carries no pre-stated number, so by John's ruling
nothing about it is an unexercised quantity in the sense of item 5 of the
2026-09-21 ruling; the part of its code after the floor had run once before
that, in a run labelled NOT A RESULT.

**What happens next.** This text is checked under the pairing rule by a
session that did not write it; the open items of section 21 go to John; the
closure check of RT-237 runs on this text; the branches of section 16 reach
the main line; John commits the registration. There is no target date; the
only date is the kill date of 2026-10-18 (section 11). Then the three reruns
of section 11, step 4b.

---

## 11. Order of work, and where it stops

Binding if registered, in this order, on the chain of section 4 of
`docs/december-result-roadmap-2026-09-20.md` as amended 2026-09-21:

1. **Done.** The first independent review of version 3 (RT-230 to RT-236);
   John's rulings of 2026-10-03 on it and on version 3's open decisions; the
   controls re-run under the registered rules, and its check; John's three
   rulings after it; the short pre-stated run; John's evening ruling; the
   check of the short pre-stated run and of the evening ruling's record;
   John's late-evening ruling on version 4's seven questions, in two records
   reconciled; the check of version 4 and the ruling on its two questions;
   **the competing solver's run under the piece rule, the twenty-piece
   control's code test, and their check (pull requests 88 to 90), ruled
   2026-10-04.**
2. **Done: Gate A, both tiers, on version 4.** The inside review (RT-237 to
   RT-246); the two outside reviews (A1 to A13, G1 to G9); the two
   dispositions packets and their checks; **John's ruling on all twelve
   pages and the follow-ups, 2026-10-06**; the work those rulings asked for
   (the decision procedure, the page 4 re-run, the decoy test, the training
   exclusion, each with its check); the ruling of 2026-10-07 on the shape of
   the experiment. **This text, version 5, written with everything ruled
   written in** → its check by a session that did not write it → the open
   items ruled → the closure check of RT-237 on this text → the branches of
   section 16 merged → **the registration commit, John's. No target date.
   Kill date 2026-10-18**, past which committing it takes a fresh ruling
   naming what comes off the back end (item 23 of the 2026-09-21 ruling;
   confirmed to stand exactly as written on 2026-10-07, decision 4 as
   revised).
3. **Done, with four changes since: the implementation frozen and tested**
   (`experiments/08-successor-degree/`, 2026-10-04, pull request 97: 195
   self-tests; the twelve toy models load bit for bit; the frozen procedure
   reproduces all 502 figures of the toy record; the site-set rule gives 325
   site sets; the whole pipeline runs at 10 and 30 million parameters; the
   launcher creates nothing on a dry run). The even-split rule and the
   one-scored-token self-test run on the built generator (test T1). The
   training entry point and the tripwire exist. **Changed since the freeze,
   each by ruling and each checked or owed its check:** the decision code
   (pull request 105, merged); the training exclusion by pairing (branch
   `training-exclusion-pairing`, checked); the sharpness fixed and the
   in-use check (branch `fix-sharpness-inuse-check`, owed its check); the
   spending alarm's four fixes (branch `tripwire-fixes`, three checks). **Two
   changes still owed in the code:** the read fitted on 1,800 of 1,980
   development episodes (the frozen procedure still fits on 420 of 600; the
   page 4 re-run made the change at run time only), and the renamed outcome
   words (open item 7 for the episode count; the bar of the in-use check is
   ruled at 0.9 and 0.5, which the frozen code already carries). The registration names the
   commit of the frozen code it registers; **that commit does not exist until
   the branches are merged (open item 10).**
4. **Done: the development runs at the 10-million size, four arms, one seed
   each, including arm M** (2026-10-04, from the first release's development
   line; $1.47; rehearsal item R-14). **This was a pipeline and throughput
   check, not a learnability verdict**, registered as such in advance, and
   its learning figures are read as nothing about the registered size. What
   it did show that the registration acts on: the built arms' ownership
   answer went flat in arms C and M (section 5.6), and the spending alarm
   could not have caught a billing fault (section 12.5).
   - **4b. The verification of the repair, new (ruled 2026-10-07, decision
     3 and its addition).** The three built arms, T, C and M, are retrained
     once at 10 million parameters, seed 0, with the sharpness fixed at 4.0
     (section 5.6), on John's go naming them, **about $1.14 from the first
     release's development line** (the four development runs cost $0.34,
     $0.33 and $0.47 for arms T, C and M; $8.53 of the $10 line remains: the
     compute ledger's 2026-10-04 rows), **after the sharpness work has its
     independent check and the spending alarm's fixes are merged** (the third
     check of the alarm: "safe for the approved $1.14 reruns" under a new
     wave name, no top-up during the wave, the end-of-wave comparison no
     earlier than three hours after the last deletion). Each rerun's
     checkpoint is run through the registered procedure on the laptop with
     the in-use check. **What comes back: whether arm C and arm M each pass
     the in-use check, both parts, at the bar section 5.6 fixes, and pass
     their gate on learning.** If they do, the repaired route holds at 10
     million, which is evidence for the 30-million size and not proof of it,
     and step 5a follows. **If they do not, experiment C stops here (stop
     S4b), before the free-arm run, and the rest of the first release is not
     spent.** Arm T's rerun is read and reported the same way (open item 6).
     The rows go in the compute ledger before anything is created, with
     John's words.
5. **The staggered launch, in two steps, as ruled 2026-09-21** (item 12 of
   that ruling; steps 5a and 5b of the roadmap chain).
   - **5a. One arm F run at the registered size launches first**, on John's go
     naming it, inside the first release (section 12.3). Three things come
     back before anything else launches: whether it passes the learn-both
     gate; what the machine actually bills (the tripwire, section 12.5); and,
     **new (John's ruling of 2026-09-26 on the route (b) result, section 7.2,
     item 1), the nomination of that run's ownership read on development
     episodes, reported against the four-fifths floor: whether any size of
     piece reaches it, with the read's held-out count at every layer, the
     chosen piece's own count, and the candidates the nomination chose among
     (the review of version 3, RT-235; section 7.5)**. A fourth thing comes
     back with them: **the five-hundred-step timing that rehearsal item R-11
     asked for is taken from this run, and the eleven later runs are repriced
     from it before the second release is asked for** (ruled 2026-10-03,
     decision 17). If it fails the
     gate, the one permitted re-run happens, also inside the first release
     (item 19 of the 2026-09-21 ruling); if that fails too, the outcome is R3
     and nothing else launches. **If no size of piece reaches the fit floor,
     that is a stop before the second release draws, beside the learn-both
     stop** (unchanged by the fifth outcome term: the rulings of 2026-10-03,
     page 11, item 6; confirmed 2026-10-07, decision 3: "a floor or gate miss
     there stops C"): it goes to John as a registered-size "no verdict, read
     failed its floor" on one seed, **with the count's sampling band beside
     it** (record B, ruling 4), and whether the remaining runs are worth the
     second release is his call with that figure in hand (section 3). The
     nomination and the fit are computed on the laptop's processor from the
     fetched checkpoint, as the toy nominations were, and draw no rented time
     (MEASURED at the registered shape on the laptop's processor: one
     transplant pass over the 600 development pairs takes 4.59 seconds, so
     one model's nomination takes about two hours and the twelve registered
     models' about 25 hours, at $0; the inside review of version 4, RT-245,
     `registered_shape_timing.out.txt`, timed on 56-token episodes; ruled
     2026-10-06, page 6. If it proves impractical at full size, that is a
     fresh question for John, not a switch of device: record B, ruling 3).
   - **5b. The remaining eleven registered runs**, two more of arm F, three
     each of arms T, C and M, launch only after 5a's learn-both result is
     read and its billing found normal, the second release is asked for and
     ruled, and John gives the go. **The second release is kept and
     conditional (ruled 2026-10-07, in John's words "Keep the second release
     conditional"; decision 3 as revised): it is asked for only after the
     first release has ended with the repaired route holding (step 4b) and
     the free model clearing its gate and its floor (step 5a), and a pass is
     necessary for that request and not sufficient for it; John gives the go
     on the figures, about $150 to $172 by section 12.4 including arm M.**
     The ruling of the same morning that struck the second release is
     withdrawn (the Gate C pass on that proposal, RT-262: struck, the design
     had no registered outcome it could reach, because the built anchors
     train at registered size only here). **Kill date 2026-11-01 binds this
     step, not 5a** (item 23 of the 2026-09-21 ruling; confirmed 2026-10-07,
     decision 4 as revised): past it, launching takes a fresh ruling naming
     what comes off the back end.
   - **What a constructed arm's failure costs under this order, stated (ruled,
     the Gate C rulings, RT-213, items 2 and 3).** Step 5a tests arm F only.
     Arm C, the high anchor, is first trained at the registered size in step
     5b, after the second release, about $119 on the ruled split plus arm M's
     runs (section 12.4), has been drawn. On the toy, arm C is the arm that
     fails the named-other condition on every seed; under this version's gate
     that failure would not fire an R3 (section 8.1), but a failure of arm C's
     *own-directed* condition at registered scale, or an arm C whose
     construction did not hold (weakness W3), is seen only after both releases
     are drawn, and an R3 or a two-arm fallback caused that way costs the
     whole successor, about $194 to $206, not the first release's $44. John
     ruled against an extra arm C run inside step 5a: at $422 to $434 of $450
     the envelope has no room, and if he later wants the anchor's construction
     proven at registered scale before the second release, that run needs the
     ceiling revisited.
6. Nomination on development episodes as arm F checkpoints arrive, with the
   fit floor applied and printed; frozen and committed; transplants on fresh
   episodes, all arms. The measure computed on arms T, C and M: that is the
   validation result.
7. **Gate B** on the validation. John rules: read arm F, or close on R2 or R3.
   A no verdict on arm C fires the two-arm fallback, and a no verdict on arm
   M drops arm M (section 3).
8. If arms T and C separate: arm F read on the frozen procedure, confirmation
   seeds. If arm F reads, the outcome is R1; if it returns no verdict, the
   outcome is the fifth term, "instrument discriminates specified constructed
   mechanisms, degree not read", with its
   reason. Findings; Gate B; closure text through Gate A. Wrap-up starts 2026-12-21 whatever
   state the chain is in.

**Stop conditions, each of which halts spend and goes to John.**

- **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
  scale even in principle) or item R-8 (the transplanting code does not pass
  its known-answer tests). **Ruled on 2026-09-25 not to have fired** (the
  queue ruling, page 4): the separable arm learned both conditions to 1.0000
  and the transplanting code passes. The named-other failure on the free arm,
  and now on arm C too, is fallback (d), on the record in section 4.4, not S1.
- **S2.** The rehearsal fails item R-3. The two-arm fallback fires; this is not
  a stop, but it is a change John has pre-approved and it is recorded. At toy
  scale R-3 passed under the registered rules.
- **S3.** The rehearsal fails item R-4 or R-6. The measure is not registered.
  At toy scale both passed.
- **S4.** The staggered first registered run fails the learn-both gate, and the
  one permitted re-run fails it too. Outcome R3. **About $44 spent**: the
  whole first release, which since item 19 of the 2026-09-21 ruling includes
  the re-run (section 12.3). (Version 1 stated this outcome's cost two ways;
  the Gate C review of version 1, finding RT-178, caught it, and item 19
  removed the gap.)
- **S4a (new, John's ruling of 2026-09-26).** The staggered first registered
  run passes the learn-both gate but no size of piece of its ownership read
  reaches the fit floor on development episodes. Not an outcome on its own: a
  stop before the second release draws, with the registered-size fit reported
  to John against the floor, its permutation null **and its sampling band**
  (record B, ruling 4), and nothing else launches until he rules. About $44
  spent at most, as for S4.
- **S4b (new, John's ruling of 2026-10-07, "Yes, add the stop condition to
  decision 3").** The verification of the repair fails: the rerun built
  models at 10 million parameters do not hold their built-in ownership route
  (the stirred-in model or the half-and-half model fails the in-use check at
  the bar section 5.6 fixes) or do not do the task (fail their gate on
  learning). **Experiment C stops, before the free-arm run at registered
  size; the rest of the first release is not spent.** About $1.14 spent on
  the reruns, plus the $1.47 of the development runs. Not one of the eight
  outcome terms, which are unchanged, but **a registered ending of experiment
  C, reached by its own stop rule**, reported in the words ruled on 2026-10-08:
  **"the built arms as designed are not references; the measure was not
  reached"** (`docs/rulings/2026-10-08-december-result-restatement-rulings.md`, decision 2; `docs/rulings/2026-10-08-verification-bar-ruling.md`), with the figures, and goes to John;
  the redesign of the arms so the built route is the only route is the named
  route to a real reference and needs its own ruling.
- **S10 (new, with the in-use check, section 5.6).** At the registered size,
  a built arm whose seed fails the in-use check returns no verdict for that
  seed, "construction did not hold"; the arm's outcome follows section 3's
  table. Not a stop on its own; listed here because a failure on arm C at
  step 5b is the fallback and a failure on arm T is the eighth term.
- **S5.** Cumulative actual spend reaches the release John has authorised,
  about $44 for the first release (section 12.3), until and unless he rules on
  the second. Work stops regardless of state; what is unrun is reported as
  unrun, and nothing launches against a release that has not been ruled.
- **S6.** A kill date passes: registration not committed by 2026-10-18, or
  the remaining runs of step 5b not launched by 2026-11-01. **Launching or
  registering past the date needs a fresh ruling that names what comes off the
  back end to make room** (item 23 of the 2026-09-21 ruling); nothing is
  written off automatically and nothing slips past unremarked. R4 is where
  the roadmap lands only if that ruling says it is not worth it. There is no
  2026-10-11 target: version 1 carried one, and item 23 leaves the schedule
  with the two kill dates and nothing else.
- **S7.** Any corrigibility event under commitment C5 of
  `spec/corrigibility-commitments.md` (the model observed exploiting or
  degrading the evaluation machinery) halts the run before further compute.
- **S8.** A rehearsal item, a gate or a stop condition **cannot be evaluated**:
  missing data, code that will not run on the artifact, a measurement never
  taken. It counts as failed and its consequence fires; it is never recorded as
  not applicable and stepped over (item 15 of the 2026-09-21 ruling; section
  12.7). Control 2's *not applicable* on arms T and M is not an instance of
  this: it is a ruled disposition with the reason on the record (section 7.3).
  Nor is control 2's *no verdict* on an arm that has not learned the
  named-other condition or whose read of the named agent misses its floor:
  the registration says in advance that it is the expected result. Nor is a
  *no verdict* under the fit floor: that is a registered outcome of the
  procedure with its reason printed.
- **S9.** **The tripwire trips**: either billing ratio of section 12.5 at or
  above 1.25 on any machine of a wave, under rule S in flight or rule D at a
  deletion, or a check that cannot run, including a vendor bill not yet
  posted. **The wave halts, not trims** (section 12.5), and it goes to John
  with the ledger row beside the estimate.

---

## 12. Spend: rebuilt from the compute ledger, and the two releases as ruled

*Every dollar figure in this section is read from
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md` (the
programme's system of record for money), from the dated note beside the
spending proposal that recomputed the second release, or from a ruling that
quotes the ledger; the row or note is named beside each figure. Nothing here
is a request, and nothing here releases money: John's process does that, run
by run, with his own words quoted in the ledger row before anything is
created.*

### 12.1 Where the money stands

| | | Source |
|---|---|---|
| Programme ceiling | **$450**, raised from $400 on 2026-09-25 | the compute ledger's ceiling note of 2026-09-25 at the top of the file, recording the queue ruling's page 6 ("The envelope") |
| Spent across the programme, as of the last row on the main line | **about $229.62** | the ledger's fourth 2026-10-04 row (line 99), arm F's development run, "After this run"; on the main line since `865f108` (pull request 98) |
| Amendment A3 against its $100 stop | **about $46.75** | the second 2026-09-25 row (line 95) |
| The rehearsal line of the first release, spent | about $0.02 (2026-09-21), about $0.50 (first attempt), about $0.05 (second attempt); **about $9.43 of $10 remains** | the same row; the check at `afb5183`, point 3, confirms the $0.0525 against the two balance readings and the vendor's posted billing row |
| **The development line of the first release, spent** | **$1.47: $0.47, $0.34, $0.33 and $0.33 for arms M, T, C and F at 10 million parameters, 2026-10-04; about $8.53 of $10 remains; the three reruns of step 4b, about $1.14, come from it, leaving about $7.39** | the four 2026-10-04 rows (lines 96 to 99); the reruns' estimate from those actuals and the flat-models packet, page 1 |
| The vendor balance | **$73.7742 before the wave, $72.3178 after it** (00:11Z and 00:56Z on 2026-10-05), a fall of $1.4565 against $1.4713 expected at the posted rate | the 2026-10-04 rows; the check of the development runs, section 3 |
| Headroom before the successor's two releases | **about $220.38** | $450 minus about $229.62, arithmetic on the rows above; not a figure the ledger states |

Version 4 carried $228.15 spent (the ledger's second 2026-09-25 row, line
95) and $221.85 of headroom (arithmetic, $450 minus that). The four
development runs since then (lines 96 to 99) are the only rows written;
nothing in the work since 2026-10-05 rented or spent anything.

### 12.2 What is ruled, and what this section is built to

- **The flat $130 cap of 2026-09-20 is superseded** by the two releases of
  the 2026-09-21 ruling (items 10, 11 and 19 of
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, with
  its correction note of 2026-09-22: about $44 and about $131). That sentence
  is the closure of the Gate C review of version 1's finding RT-176 (the
  $175-against-$130 finding), and a dated annotation goes beside item 4 of the
  2026-09-20 ruling (the queue ruling, page 6, part 1).
- **The envelope is $450** (the queue ruling, page 6, part 2, recorded in the
  compute ledger's ceiling note of 2026-09-25). What it was ruled to buy, on
  the ledger rows the packet cited: the base plan of about $175 on top of
  about $227.63 spent, plus one extension of $32 to $44 (arm M) or about $36,
  with $3 to $15 left. It does not hold two extensions. The measured figures
  below leave more room than that arithmetic did.
- **The first release's development line covers four arms, not three (ruled,
  the Gate C rulings, RT-229).** This widens item 10 of the 2026-09-21 ruling,
  which covered three; the reason recorded is that arm M's code has never run
  on the rented machine, so its development run belongs in step 4 with the
  others, before the second release. Version 2 had costed that run twice, once
  in each release (the Gate C review, RT-229); this version costs it once, here.
- **The second release is asked for only after seconds per step were
  measured on the rented machine** (item 11 of the 2026-09-21 ruling). They
  were, on 2026-09-25 (section 9). The ruling changed the ceiling, not that
  gate.
- **The staggered launch** (item 12), **halt not trim** (item 13), **funding
  per wave** (item 14) and **a check that cannot run is a trip** (item 15) all
  stand; sections 11, 12.5, 12.6 and 12.7.
- **The pre-authorisation scheme** of `docs/preauthorised-spending-proposal-2026-09-21.md`
  **is not adopted** (the queue ruling, page 6, part 3). Only its tripwire is.
- **The successor gets a new experiment directory with its own registration
  (`experiments/08-…`), and the compute ledger stays where it is**, in
  experiment 06's folder, as the programme's one record of money (ruled
  2026-10-03, decision 8).

### 12.3 The first release: about $44, ruled 2026-09-21, with a four-arm development line

| Item | What it buys | Basis | Amount |
|---|---|---|---|
| The rehearsal | Tiny models, the transplanting code, rehearsal items R-1 to R-11, including the rented slice | item 10 of the 2026-09-21 ruling: up to $10. Spent so far: about $0.57, the sum of the ledger's three slice rows (about $0.02 on the 2026-09-21 row, about $0.50 and about $0.05 on the two 2026-09-25 rows), leaving about $9.43 by the last row's own running line | up to **$10** |
| Development runs, **and the three reruns of the repaired built arms** | **Four arms, one seed each**, at the 10-million size: pipeline, self-tests, throughput, and arm M's first run on the rented machine (**done, $1.47**); **then arms T, C and M once more with the sharpness fixed, about $1.14** (section 11, step 4b) | item 10: up to $10 for three arms, **widened to four by the RT-229 ruling**; the reruns by the 2026-10-07 ruling, decision 3. The four runs cost far less than the ledger's 2026-08-12 figure of $1.943 each had suggested (the card ran 0.0093 to 0.0145 seconds a step: the check of the development runs, section 4), so $2.61 of the $10 line is spent or committed and about $7.39 remains | up to **$10** |
| One free-arm run at the registered size | Step 5a of section 11 | item 10: about $12. The lifetime-priced cost of a registered-size run is $10.04 (the ledger's 2026-09-17 row, line 88: 20.28 pod-hours at $0.99 for two runs, computed from measured pod lifetimes and not balance-confirmed, as the row itself says; the Gate C rulings, RT-226) | about **$12** |
| The one permitted re-run | If step 5a fails the learn-both gate | **item 19: folded into the first release**, at the same planning figure | about **$12** |
| **First release, total** | | | **about $44** |

This is the release John has authorised; nothing beyond it is launchable
without the second. Stop conditions S4 and S5 in section 11 are stated
against it.

### 12.4 The second release: from the measured seconds per step, then arm M's three runs

**What the second release is bound to, and now has.** Item 11 bound it to
rehearsal item R-11's measured seconds per step for arms T, C and F on the
registered venue. Those were measured on 2026-09-25 (section 9), and the
dated note beside the spending proposal recomputed the release from them
(`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
at `9f802db`; checked at `afb5183`, point 6, where the script's re-run is
byte-identical to its committed output). The method, in the note's own words,
is MEASURED arithmetic on an ARGUED method: the measured seconds cannot be
turned straight into hours for a run (a timed step holds 1,792 tokens where a
registered step held about 10,624, and a real run also generates its data,
evaluates and saves), so the note does what version 1's spending arithmetic
did, with the measurement in place of the inference: **the lifetime-priced
cost of a registered-size run, $10.04 (the ledger's 2026-09-17 row), times
each arm's measured ratio.** Every figure below is the note's, printed by
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py`
into `second-release-arithmetic.txt` beside it.

| Per run | Version 1's planning figure | From the measurement |
|---|---|---|
| Arm F | $12 | **$10.04** |
| Arm T | $12 | **$10.48** (ratio 1.044) |
| Arm C | $12 | **$10.84** (ratio 1.080) |
| Arm M | (none: arm M is new in version 2) | **not measured**; priced from ledger rows below |

| Item | Version 1 (provisional) | From the measurement (the note's table) |
|---|---|---|
| The remaining eight registered runs of arms T, C and F (two F, three T, three C) | $96 | **$84.06** |
| One permitted re-run, priced at the dearest arm (C) | $12 | **$10.84** |
| Transplanting and measurement on fresh episodes | $12 | $12.00, unchanged: not a throughput line |
| Billing-anomaly and idle-billing margin | $23 | $23.00, unchanged: not a throughput line |
| **Second release, before arm M** | **$143** | **$129.90** |
| **Both releases, before arm M** (the note's first release of about $32) | $175 | **$161.90** |

**How this reads against the ruled split.** The note's table keeps the
permitted re-run inside the second release and pairs it with a first release
of about $32, which was the split on 2026-09-21 when the note's method was
written. Item 19 later moved the re-run into the first release (section
12.3), so the same money as ruled is **about $44 plus $119.06** (the second
release without its re-run line: $84.06 + $12 + $23), about $163.06. The
$1.16 between the two totals is the re-run at the $12 planning figure in the
ruled first release against $10.84 on the measured method; it is a matter of
which release the re-run sits in and at which price, not of how much money
there is. **$161.90 is the figure this section carries for both releases
before arm M**, as the note computed it.

**Then arm M's three registered runs.** Arm M's ruled allocation is **$32 to
$44** (the queue ruling, page 5, and page 6's envelope; the repairs rulings,
item 2), from the ledger's per-run rows rather than from item R-11, because
arm M was not timed on the rented machine. That range is: three runs at what
the last three clean runs billed (about $29.70 to $30.12), or $36 at the
planning figure, or up to about $41.76 if each billed as the 2026-09-15 pilot
did with its idle time, **plus about $1.94 for one development run at the
10-million size** (page 5 of `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`,
from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and 2026-08-12 rows).
**The $1.94 comes out of this section (ruled, the Gate C rulings, RT-229):**
it is paid from the first release's four-arm development line and launched in
step 4, so this section carries the three registered runs only, **about $30
to $42**. The ruled $32 to $44 stands as the allocation John ruled; moving its
development run between releases changes which release pays and when, not
how much money there is. Arm M's runs are in the second release (the repairs
rulings, "What this changes": section 12.4).

**The whole successor, and the programme after it.** Arithmetic on the
figures above; no ledger row states these totals.

| | |
|---|---|
| Both releases before arm M | about $161.90 |
| Arm M's three runs | about $30 to $42 (the ruled $32 to $44 less its $1.94 development run, now in the first release) |
| **The successor, all in** | **about $192 to $204** on the note's split; about $193 to $205 on the ruled split |
| Spent before it | about $228.15 |
| **Programme after the successor** | **about $422 to $434 of $450**, stated as a range: the repairs rulings' annotation 2 gives it in these words on the note's split with arm M at $32 to $44 (MEASURED: section 17, candidate 7, prints $422.05 and $434.05); on the ruled split with the $1.94 moved into the first release it is about $421 to $433 |
| **Left** | **about $16 to $28** on the note's split; about $17 to $29 on the ruled split with the $1.94 moved; **$14.79 at the least**, on the ruled split with arm M at its ruled top of $44 (the Gate C review, RT-217) |

**The second release, as ruled on 2026-10-07 (decision 3 as revised), is
about $150 to $172 on this section's figures: $129.90 before arm M, plus arm
M's three runs at $30 to $42 (the note's split; on the ruled split without
the re-run line, $119.06 plus arm M, about $149 to $161).** It is kept and
conditional: asked for only after the repaired route holds at 10 million
(step 4b) and the free model clears its gate and floor at step 5a, a pass
necessary and not sufficient, John's go on the figures. **The second release
is asked for on these figures or not at all**, and the request carries the
measured figures beside the provisional ones so the movement is visible.
**One figure has moved since version 4 and is carried as a caution (ARGUED
from the development runs' check, section 4):** at 10 million parameters arm
M's step took 1.44 times arm C's (0.0145 against 0.0100 seconds), where its
operation count is only 1.11 times; if the same ratio holds at the registered
size, arm M's three runs at arm F's $10.04 times 1.44 are about $43.37,
inside the ruled $32 to $44 but at its top. The check's argued cause, a
per-step copy from the processor's memory in arm M's forward pass, would
change nothing the model computes; whether to fix it in frozen code is John's
(open item 9). Two things that could still move it, stated so they
cannot arrive quietly: the first free-arm run of step 5a gives arm F's own
run cost and the five-hundred-step timing, and the later runs are repriced
from it before the second release is asked for (the note's "what this does
not settle", item 2; ruled 2026-10-03, decision 17); and arm M's per-run cost is a ledger inference until a run
of it exists. Arm M is priced at arm F's per-run figures although it carries
both arm T's slot and arm C's entangling, whose measured ratios are 1.044 and
1.080; at arm C's ratio the lower end of its three runs would be about $32.52,
which the range still covers (the Gate C review, "The arithmetic of both
releases"; ARGUED there).

### 12.5 The tripwire: 1.25, halt not trim, with the in-flight clause

**Adopted on 2026-09-25** (the queue ruling, page 6, part 3), from sections
5.3 and 5.4 of `docs/preauthorised-spending-proposal-2026-09-21.md`, whose
pre-authorisation scheme is not adopted. Two ratios are measured, because the
authoritative one is slow and the fast one is rough:

- **Ratio A, authoritative: billed hours divided by machine-existence hours**,
  per machine, from the vendor's own billing rows: the quantity rule 4 of the
  compute ledger already reconciles at phase boundaries, and the one the
  2026-08-08 anomaly was recorded in (8.47 billed against 2.42 existed; the
  figures are at the ledger's 2026-09-21 row, line 93, and its note at line
  423, both describing the 2026-08-07/08 row, which itself carries neither
  number; the Gate C rulings, RT-226).
- **Ratio B, fast: account-balance drawdown per elapsed hour, divided by the
  posted hourly rate times the number of machines running**, from the balance
  query the ledger already uses, available within minutes of launch.

Both are measured against the posted rate read from the machine's creation
record, not remembered. **Either ratio at or above 1.25 is a trip.** When it
trips:

1. **Halt, not trim.** No further machine is created. The wave stops; nothing
   else launches (item 13 of the 2026-09-21 ruling replaced the roadmap's seed
   fallback with this, on the arithmetic that a trimmed plan at the anomalous
   rate still spends about $326, more than the programme has).
2. **A machine already in flight is left to finish only if** its projected
   total is inside its estimate times the measured ratio and the funded balance
   covers it, the spending proposal's own clause (its section 5.4, item 2):
   killing a running machine forfeits its checkpoint, but if the projected
   drawdown would exhaust the funded balance before the checkpoint and its
   finished-marker are written, the machine is deleted and the run written
   off. That is arithmetic, not taste.
3. **The ledger row is written first**, with the measured ratio, both hours and
   the balance reading, before anything else happens.
4. **John is told the number**, and every later launch needs his own words.
5. **A check that cannot run is a trip** (item 15 of the 2026-09-21 ruling;
   section 12.7).

The tripwire is written into the launch preconditions beside the sleep guard
and the argument guard (the queue ruling, page 6, "Changes"). **It exists as
code** (`experiments/08-successor-degree/src/tripwire.py`, frozen 2026-10-04),
**and it met real billing once, in the four development runs, and did not
hold** (MEASURED: the check of the development runs, branch `check-dev-10m`
at `51ec07d`, section 3): reading once an hour, it read once as the first
machine was created and next at 01:11Z, 31 to 36 minutes after every machine
was gone; it never recorded the deletion times, so its one real figure was
ratio B 0.401 where the same arithmetic with the true lifetimes gives 0.990
(drawn $1.4565 against $1.4713 expected); the end-of-wave comparison read the
vendor's not-yet-posted, empty bills as zero hours billed and passed; and the
laptop deadline timers did not notice their machines were gone and had to be
stopped by hand. Billing was normal; the alarm could not have said so.

**Amended 2026-10-06 (the flat-models packet, page 2; reported ruled by John
that day in `docs/2026-10-06-tripwire-fixes-method.md`, section 1; no rulings
file records the words, open item 2).** Version 4's "it runs in flight,
hourly, on ratio B from the first hour of the first machine" becomes:

1. **It reads every 5 minutes while any machine of the wave runs, and for 30
   minutes after the last deletion.** Reads are free.
2. **Rule S, in flight:** the comparison counts as over the line when the
   predicted spending so far is at least $0.25 and the money drawn is at
   least 1.25 times the prediction plus $0.05, **on the latest two readings
   both**, about 5 minutes apart. The 1.25 is the trip line unchanged; the
   $0.05 absorbs one lump of about three machine-minutes posted early; the
   $0.25 floor keeps a single early lump from dominating. Lag only ever makes
   this rule read low.
3. **Rule D, at each deletion:** at every reading at least 15 minutes after
   a recorded deletion, the comparison over the whole wave counts as over
   the line when the prediction is at least $0.10 and the money drawn is at
   least 1.25 times the prediction plus $0.02; one reading is enough. Rule D
   is the one to trust; rule S catches a gross overcharge before the machines
   finish.
4. **Every step that deletes a machine records the deletion time in the
   alarm's records** (the watchdog, the deadline timer, the alarm itself, the
   launcher's emergency deletes), at the moment the delete came back
   accepted; an inferred time is replaced by a recorded one.
5. **Empty or not-yet-posted bills are "cannot be checked yet", which is a
   trip** (section 12.7). So the end-of-wave comparison runs only once the
   vendor has posted the bills; run early, it halts launches until John
   clears the halt.
6. **Each laptop deadline timer stops itself only on a confirmed deletion**
   (the watchdog's "machine gone" record naming its machine, or the vendor
   answering "not found"), never on a failed or empty reading.

The code is on branch `tripwire-fixes` at `5e2faf9` (pull request 116;
`tripwire.py`, `launch_successor.sh`, `watch_run_a3.sh`,
`machine_deadline.sh`), tested against a stand-in vendor on five made-up
waves whose expected outcomes were written first; checked three times
(branch `check-tripwire-fixes` at `b01e564`), the third check "ready to
merge": eight runs of 82 checks all passing; one minor point left (the timer
can delete up to about 28 seconds late with the real settings, under a cent
at the posted rate). **By failure 6's standard the alarm has now met the
vendor once and failed; the fixed alarm has met only the stand-in. The three
reruns of step 4b are where it meets real billing again, and the launcher's
guard against a halt file is what stops the free-arm run until it has.**

### 12.6 The account is funded per wave, not per release

Unchanged from version 1 and from item 14 of the 2026-09-21 ruling: the rented
account is prepaid with automatic reload off, and **topped up to the estimate
for the wave about to launch plus $20, and no further**, so that no anomaly of
any size can cost more than that, because there is nothing else in the account
to spend. This is the only control in the programme's history that held when
everything else failed (2026-08-12). The vendor balance stood at $75.8645 on
2026-09-26T01:54Z (the ledger's second 2026-09-25 row, line 95; the check at
`afb5183` read $75.864512286 at 01:54:04Z), which is above what step 5a's
estimate plus $20 would call for; the rule caps what is topped up, not what
is already there.

### 12.7 A check that cannot be run counts as a trip, not a skip

Item 15 of the 2026-09-21 ruling, and it is a spend rule as much as a method
rule. If a rehearsal item, a gate, a stop condition or a tripwire check cannot
be evaluated (the data is missing, the code will not run on the artifact, the
measurement was never taken, the balance query returns an error), **the check
counts as failed and its consequence fires.** It is never recorded as not
applicable and stepped over, and it is never deferred past the launch it was
supposed to gate. Written into section 11 as stop condition S8 and into the
tripwire as its fifth line.

### 12.8 The wager on this estimate

Stated so it can lose, in the shape the earlier amendment used. **Version 1's
wager, that the rehearsal measures a per-run cost at or below the $12
planning figure, survives on the 2026-09-25 measurement: the dearest timed
arm is $10.84** (the note at `9f802db`). **The wager this version makes, on
the ruled split and against the full range (ruled, the Gate C rulings,
RT-217):** the twelve registered runs, with arm M's three priced from ledger
rows at the top of their ruled range, complete inside the $450 envelope with
three seeds on every arm carried and **at least $10 left**. On the ruled
split, $44 plus $119.06, with arm M at its ruled top of $44, the plan leaves
$14.79, and with arm M's three runs at $41.76 and the $1.94 moved into the
first release it leaves $17.03; both meet the floor (MEASURED: section 17,
candidate 7). **The development runs and the reruns of step 4b do not move
these totals**: they are paid from the first release's $10 development line,
of which $2.61 is spent or committed, and the ledger's $229.62 spent equals
version 4's $228.15 plus that line's $1.47 (section 17, candidate 7, this
version's run). Version 2's $16 floor was already lost at the top of the range
on the ruled split (the Gate C review, RT-217), which is why the floor is
now $10. If measured spend approaches the second release's ruled figure with
runs missing, **the report is the shortfall, never a second raise.**

---

## 13. What this cannot claim, and its weakest points

The Gate C brief asks what a result will be read as claiming beyond what it
measures. Answering it before the reviewer does.

**W1. The constructed arms differ in more than their degree.** They differ in
architecture, in parameter count within the size band, in how they route
information. Anything that separates them is confounded with degree. What the
arms establish is that the measure moves in the right direction between a
system built to be separable, one built as a mixture and one built to be
entangled; they do **not** establish that the measure responds to integration
and to nothing else. Consequently arm F's reading is "where arm F sits against
three constructed anchors on this measure", and never "arm F's integration is
*d*". The public sentence in section 8 of the December-result roadmap already
carries this hedge, and the recommendation is that the hedge is not loosened
at any later point. This is the deepest weakness in the design and it is not
removable by anything affordable.

**W2. The reading is relative to the site set, and the arms cannot be read
at the same site set.** A different frozen site set could give a different
number. Mitigated by one pre-stated rule applied identically to every arm, and
by saying in the registered text that the reading is the degree *at the sites
this procedure nominates*. The rider makes the second half of this weakness
visible rather than hidden: at arm T's site set, arms C, F and M return no
verdict on the toy, for two different reasons (section 7.2, item 7), so what
differs between arms is first of all where the procedure has to look.

**W3. Arm C's degree was an intention; at 10 million parameters the
construction did not hold, and the arm is now a hand-set reference.** At toy
scale no nominated piece carries the counterfactual on arm C, although the
pieces transplanted hold the label at the action position (section 5.2). At
10 million parameters training drove the sharpness of arm C's built-in
ownership answer to zero, so nothing in its construction entangled ownership
any more and the procedure found no readable ownership in its running state
(section 5.6): the failure version 4 expected to see only after both releases
were drawn was seen first at the development size. The repair fixes the
number by hand (section 5.6), and the three reruns of step 4b verify it
before the free-arm run, with a stop if it does not hold. **What the repair
cannot do** is make the built route the main carrier of "which agent am I"
if the network learns another: on the toy it did, before and after the fix
(W17). A network built with ownership multiplied into every layer could
still, at 30 million parameters, concentrate it in a low-rank direction, in
which case arm C's anchor collapses into a second copy of arm T; the
registered-size nomination and the in-use check are the test, and a failure
at step 5b fires the fallback (the sixth or seventh term), after the second
release is drawn.

**W4. The whole-state transplant may fail for arm C at the registered size.**
If ownership in arm C is spread across layers the site-set rule does not
cover, no site set clears the floor and arm C returns no verdict: honest, but
it leaves the experiment with no high anchor by another route. The rule of
section 7.2 covers every contiguous layer set precisely to give it the best
chance without letting the rule differ between arms.

**W5. The most likely outcome is that arm F fails its gate or returns no
verdict, and both are now measured at toy scale, not predicted.** Sections
3, 4.4 and 5.4. The staggered launch makes a gate failure on arm F cost the
first release, about $44, instead of the whole wave, and since John's ruling
of 2026-09-26 on the route (b) result the same is true of a read that misses
the fit floor: the first release's single arm F run is the test of both, and
either miss is a stop before the second release draws (section 11, step 5a).
The route (b) search found no label the free system carries at the floor at
toy scale (section 7.2, item 1), so the registered read is the ruled one and
the honest expectation is that this stop may fire. John's present view is that
a registered "no verdict on the free arm" is worth the second release (the
Gate C rulings, RT-212, item 3); the stop lets him make that call with the
registered-size fit in hand. **The toy figures that make this the honest
prior are development evidence** (section 10; RT-252): the rules were changed
after toy outputs were seen, and the registered runs are the first untouched
test of them.

**W6. The named-other condition reads its owner from a token and the
own-directed condition does not.** Section 4.2; unremovable; recorded in the
registration text, as ruled 2026-10-03 (decision 9).

**W7. The nomination could find the acting channel's own trace rather than
anything the network built.** The objection the closed design registered
against itself, and it carries over. **On the toy, before this version's
rule, six of the nine nominations on arms C, F and M sat at the injection:
layer 0 at the post-identity position set, which spans exactly the turns the
channel fires on** (MEASURED: the Gate C review, RT-216; the re-run findings
at `9d9d31a`, Part 2, first pass, section 6.2). Version 2's claim that the
other arms' nominated sites were downstream of the injection was false and is
struck (ruled, the Gate C rulings, RT-216, item 2). What now mitigates the
weakness: layer-0 site sets are removed from the candidate family at every
position set spanning the acting turns (section 7.2), and the rule chooses
again; under that rule every toy nomination on arms C, F and M sits at layer
1 or later; the stricter variant, layer 0 removed everywhere, is reported as
a sensitivity row so that the one remaining layer-0 nomination, arm T's at
the action position, can be compared with its layer-1 alternative (0.0000 on
both). The rider and the honest gap between the lesion result and the
transplant result do the rest. Control 2, which was meant to help here, has
never run on any toy model and is expected to return no verdict at
registered scale too (section 7.3, item 2), so it is not counted on. What the
rule does not do: it does not show that a layer-1 nomination is anything
other than the channel's trace one block on; that is what the fit floor and
control 3's distribution are reported for.

**W8. The per-run cost is measured for three arms and inferred for the
fourth, and the measurement is fifty steps, not five hundred.** Section 12.4
prices arms T, C and F from the 2026-09-25 measurement and arm M from ledger
rows. Item R-11 as written asks for five hundred timed steps per arm; the plan
John authorised timed fifty, and the spread was tight (each arm's slowest
step within 3% of its median; the check at `afb5183` recomputed arm C's at
2.9%), so the ratios are unlikely to move much with a longer window; that is
argued, not measured (the slice findings at `9f802db`, section 3). **Ruled
2026-10-03 (decision 17): fifty steps are accepted for the second release's
arithmetic, and the five-hundred-step figure comes from the first full-size
run, with the later runs repriced from it.**

**W9. The shutdown handshake's machine half has not been exercised against
the real vendor, and arm M's code has never run on the rented machine.** The
laptop half has (section 10, R-11). **What the registration says, as ruled on
2026-10-03 (decision 18, option (b)): on the normal path the laptop deletes
the machine, and the machine's own watcher is a backstop for a laptop that
never answers.** That is what is true today: the laptop deletes the machine
the moment it writes the receipt, so the machine's own "receipt found" is
close to unobservable by construction. Option (a), making the laptop wait for
the machine's acknowledgement, is the repair if a later run shows the laptop
failing to answer, and it comes off the Weekend 2 launcher items. **The
caution John ruled with is carried: twelve full-size runs rest on a backstop
that has not fired against the real vendor.** **Beside it (ruled, the rulings
on the review of version 2, RT-228): arm M's code,
`experiments/rehearsal-successor-measure/src/arm_middle.py`, has run only on
this laptop; the rented slice timed arms T, C and F only, and no training
entry point for arms T, C or M exists on the rented machine yet.** By failure
6's discipline both are untested until they have met the far end; step 4 of
section 11 is where arm M first does.

**W10. Arm M's degree is a design intention, and it is a mixture by item.**
Its construction fixes which actions go through which route; a freely trained
system's partial separation, if it has any, would be within each trial, and
the measure has not been shown to scale on that. Arm M shows the measure
returns a number in the middle for a known mixture and near the mixture's
share, and no more (section 5.3). It differs from both anchors in more than
degree.

**W11. On the entangled arms, the same-value cell of control 6 moves, and
control 6 cannot say why** (retitled and rewritten 2026-10-06, follow-up item
1, closing the outside review's A7, adopted as RT-251). On the relaxed set
the same-value cell moved on arm C in 0.51 to 0.63 of trials and on arm M in
0.22 to 0.32 (section 7.3, item 6; the controls re-run at `821f154`, section
4). Neither copying who is acting nor copying the donor's answer would move
it, so the whole-state transplant changes something else on those arms, or
the models err differently by owner. Control 6 cannot separate copying who
is acting from copying the answer, so no reading here is claimed as purely a
statement about where the ownership answer lives.

**W12. The fit floor tells an empty instrument from a ceiling; it does not
tell an entangled act from an ownership answer the read did not find.**
Section 3's residual admission. A piece that clears the floor shows the label
is in those directions at the action position; a reading near 1 with such a
piece shows the directions the read found do nothing on their own; that the
act's ownership answer is carried by directions the read did not find, at
sites the rule did not nominate, is not excluded by anything in this design.
The rider, the sensitivity rows and control 3's distribution make that
visible; they do not remove it. **The same limit applies to the high anchor**
(ruled 2026-10-06, page 10, closing the outside review's A6, RT-247): arm C's
reading near 1 is what this instrument returns on it, and no measurement
independent of the instrument shows arm C's ownership answer cannot be
separated. The decoy test (section 10, R-12) did not read a separable model
with an exact idle copy of its marker as entangled, reading 0.0000 on all six
runs; what it did not test is weakness W18.

**W13. The piece is shown to hold the label at the action position only.**
The floor is applied there, where the registered read is fitted. Where the
chosen site covers several positions the same directions are transplanted at
all of them, and on the toy the piece often falls below four fifths away from
the action position: on arm C seeds 1 and 2, and, position by position, on
arm M (sections 3, 5.2 and 5.3; **checked: the check of the short run at `53c8100`**). So
a sentence of the form "the piece held the label and transplanting it did
nothing", or "did half", is true at the action position and is not shown
across the whole site. The readings do not depend on it: they come from what
the transplants do to the action. John ruled that the figure is reported both
ways and gated in neither; the alternative put to him and not taken was to
require four fifths at every position of the site.

**W14. Two of the seven controls say less than their names suggest.** Control
4 as redefined is a known-answer test of the pairing and the code: it cannot
fail on a correctly built model, so its pass is not evidence about what any
model knows early. Control 2 has returned a figure on one toy model of six,
has no pass line, and is expected to return no verdict at the registered
size. Neither is a weakness of the reading itself, but a reader counting
controls should know that two of the three that hold (controls 4 and 7) test
the pairing and the code and not a model, that control 6 is a description
that cannot tell copying who is acting from copying the answer (W11), and
that the controls which say something about a model are 1, 3 and 6.

**W15. The read's fitting count was chosen on a stand-in** (ruled 2026-10-06,
page 4, RT-240). The toy's state is 160 wide and the registered model's 448.
Fitted on 420 episodes, the read held the label on every constructed toy
model (the free model's read failed its floor on every seed, as section 5.4
records); on a stand-in at width 448 (the toy states with 288 coordinates of
independent noise appended) the entangled model's 8-direction piece fell to
as low as 76 and 126 of 180 on two seeds against 144 (the review's 600
episodes), and 74 and 129 on a larger pool with a fixed held-out set.
Fitting on 1,800 episodes brought every seed back above the floor on every
noise draw (smallest 156); 900 episodes and stronger regularisation did not
(MEASURED on a stand-in, NOT A RESULT: the inside review of version 4,
RT-240, `width_vs_count.out.txt`; `docs/2026-10-04-gate-a-v4-dispositions-measurements.md`,
part B, branch `rulings-2026-10-06-gate-a-v4` at `525a625`). A wider model's
extra coordinates carry structured content, not noise, so this is not a
forecast, and 1,800 is the smallest of three sizes tried that held, not a
size derived from anything. At 1,800 the fitter stopped at its iteration
limit far more often on arm M (section 7.2, item 1). The read at the
registered width is first seen on arm F at step 5a and on arm C at step 5b.

**W16. The toy's competing solvers do not test the measure on a model that
solves the task another way and still looks readable** (ruled 2026-10-04,
ruling 7, as worded by the 2026-10-06 ruling, page 6, RT-246). The ordinary
competing solver fails the task, so its "no verdict" shows only that the
measure returns nothing on a model that has not learned the task. The toy
does have one model that does the task by a route other than carrying the
registered label: the free model, which solves the own-directed condition
from the value tokens on the turns its channel marked, without carrying its
marker word to where it acts (section 5.4). On it the measure returns "no
verdict, read failed its floor" and says why. What the toy has no case of is
a model that does the task by another route and still leaves the label
readable where it acts. The obvious such route, reading its own name off the
text near the action, is closed by the grammar (section 4.1), not tested by
a control.

**W17. The built route is a minority carrier on the toy's arms C and M, and
the hand-set reference is a reference only as far as the in-use check
certifies it** (section 5.6; new in this version, from the sharpness
findings). On the twelve committed toy models and the nine retrained with the
sharpness fixed, swapping arm C's built-in answer to another agent loses only
24 to 29 per cent of its right own-directed answers, and arm M's stirred-in
route 7 to 11 per cent; arm T and arm M's separable route lose all of them.
So on the toy, arm C's network gets most of "which agent am I" through the
acting signal in its trunk, the free route arm F uses, and is "entangled by
construction" only in part. Fixing the sharpness repairs the number that
went flat; it does not make the built route the carrier. Whether the
reruns at 10 million show the built route in use at the bar section 5.6 fixes
is the verification of step 4b, and the bar is ruled at 0.5 (2026-10-08). The toy
readings quoted in this text were taken on the learned-sharpness models; the
hand-set models have been read on one of nine.

**W18. An unused representation coded differently from the one the action
uses can partly fool the read** (from the check of the decoy test, section
10, R-12; new in this version). The ruled decoy test used an exact copy of
the ownership block, which cannot pull the read away from the block, so its
"not fooled" is correct and carries little weight. The check's probe, not a
ruled test and skipping the registered nomination, used an unused
one-of-twelve code of the owner's marker word at four times the block's size
and got readings of 0.28, 0.23 and 0.29 at 8 directions, and 0.52 to 0.96 at
fewer, on a model whose true reading is 0. So a separable model carrying such
a decoy could read part way to entangled, and a high reading on arm C could
in principle be of that kind. Nothing in the design excludes it. A ruled test
of the differently coded decoy, about an hour on the laptop at $0, is open
item 8.

**How results may be summarised (ruled 2026-10-06, page 11, closing the
outside review's A13, RT-250; the reviewer's table, registered as written,
with control 6 added to the last row).** The scope phrases of section 3
travel with every term; this table says what the tempting summaries would
claim beyond what the experiment measures.

| Tempting summary | Defensible scope |
|---|---|
| "The metric measures degree of integration." | It compares whole-state and selected-subspace interventions at sites chosen by a specified rule, on these constructed systems, for this intervention procedure. |
| "The entangled anchor's degree is known." | Its architecture encourages the intended mixing, its built-in answer is now set by hand, and the tested subspaces have little effect; independent causal inseparability remains unestablished (W12, W17). |
| "F is as entangled as C." | F has a similar intervention ratio under the registered searches, subject to the unused-label and alternative-site explanations (W12, W18). |
| "M validates intermediate degrees." | M demonstrates an intermediate reading for a mixture of routes across items. Its formula and true-slot reference are not independent checks (W10). |
| "No verdict means the model has no ownership representation." | This instrument did not admit a reading, for the stated reason (section 3). |
| "The lesion establishes a centre." | Removing an input channel impairs performance. The registration already prohibits the stronger claim (section 8.2). |
| "Seven controls validated the mechanism." | The controls have different roles; some test implementation (4, 7), some are descriptive (1 on arms C, M and F; 2; 3; 6), and control 2 has returned a figure on one toy model. |

---

## 14. What this does not change

- **The programme ceiling of $450**, ruled 2026-09-25 and recorded in the
  compute ledger's ceiling note of that date. This document asks for no
  change to it and proposes none.
- **The corrigibility commitments** (`spec/corrigibility-commitments.md`,
  version 1.1): John authorises every run and his go is quoted word for word in
  the ledger row; every run is killable; no stakes term; checkpoints are not
  promotable; optimisation against the instruments halts the run. All four
  arms are episodic and floor-only: no state kept across episodes, no
  maintained boundary, no stakes. Nothing here pre-authorises a larger build.
- **The claim rule.** Nothing produced by this experiment is reported as a
  conscious machine, and every positive is bounded at "non-zero on the
  gradient", per the standing limits in `ROADMAP.md`.
- **The closure of Amendment A3.** It closed as *not testable* on 2026-09-25
  and this experiment does not reopen it. The closed design's checkpoints are
  not transplanted: their grammar has no matched comparison condition and
  their target was never localised.
- **The outside-review protocol's gates, its closure rule, the pairing rule
  and the failure-mode pass.** This document passes through them; it does not
  amend them. Its failure-mode pass is section 17.
- **The grammar of section 4.** The grammar attempt did not clear, so the
  grammar, the training recipe and rehearsal items R-1 to R-6 stand as
  version 2 had them.
- **The dates.** Registration by 2026-10-18 and the remaining runs of step 5b
  launched by 2026-11-01, each a kill date in the sense of item 23 of the
  2026-09-21 ruling (a fresh ruling to go past, never a quiet drift);
  **confirmed to stand exactly as written on 2026-10-07 (decision 4 as
  revised, in John's words "withdraw the calendar dates": the three new dates
  of that morning's ruling are withdrawn, item 23 is read as its words say,
  and no step is scheduled on a future date, as ruled 2026-10-04)**; wrap-up
  starting 2026-12-21; the hibernation condition complete by 2027-01-04. No
  2026-10-11 target.
- **The question of section 2.** Renaming the outcomes to what they measure
  changes what the experiment is called, not what it asks or how it is read.

---

## 15. Decisions, each now ruled

**Every decision below is now ruled or done.** Each keeps its number from
version 3, with the ruling that settled it and the alternative that was put
and not taken, so that the reader can see what was chosen against what.
Decisions 2, 3, 4, 8, 9, 10, 13, 14, 17, 18 and 19 were ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, "Agreed on all" to sixteen pages put to John with a
recommendation each; the record says he ruled from the index and three pages
his attention was drawn to). Decisions 15 and 16 were ruled that morning and
changed later the same day. Five new entries, 24 to 28, record the other
rulings of 2026-10-03, and entry 29 the seven questions this version raised,
ruled the same night.

1. **Nomination runs blind on every arm, including arms T and M.** The
   procedure is one instrument (section 7.2). *Ruled 2026-09-25 (the queue
   ruling, page 3, option (i), with the rider).* The true-slot readings are
   reported as references; on arm M the true-slot reading and the formula of
   section 5.3 are one check (the Gate C rulings, RT-223).

2. **Arm T's ownership path is architecturally forced, not encouraged.**
   *Ruled 2026-10-03 (page 4).* **The alternative not taken:** a soft
   table-and-pointer with a penalty term, which is more comparable with arm F
   but gives up the one property the arm exists for: a degree that is known
   rather than hoped.

3. **Arm C entangles by architecture** (per-layer scale-and-shift from the
   acting channel, multiplicative binding of ownership into content).
   *Ruled 2026-10-03 (page 5): by architecture, with no penalty against
   transplantable ownership directions.* **The alternative not taken:** train
   arm C with a penalty that punishes any linearly transplantable ownership
   direction, which trains the system against the very instrument that will
   measure it.

4. **The two transplants are a subspace and its containing space at identical
   sites.** *Ruled 2026-10-03 (page 6).* **The alternative not taken:** transplant
   the whole forward state at every
   layer as the denominator, which always succeeds and turns the measure into a
   report on how the sites were chosen.

5. **The registered reading is the chance-corrected form, with the raw
   difference and both accuracies reported alongside, always, plus the floors
   and the no-verdict rules.** *Ruled 2026-09-25 (the queue ruling, page 2);
   the fit floor added 2026-09-26 (the Gate C rulings, RT-212).*

6. **Three seeds per arm.** *Ruled 2026-09-25 (page 1f).*

7. **The money goes in two releases.** *Ruled 2026-09-21 (items 10, 11 and 19)
   and 2026-09-25 (the queue ruling, page 6); the development line widened to
   four arms 2026-09-26 (the Gate C rulings, RT-229); section 12 is built to
   them.* The one number John should see before it can surprise him: the
   programme after the successor is about $422 to $434 of $450, and on the
   ruled split with arm M at its ruled top the plan leaves $14.79, against the
   wager's $10 floor (section 12.8).

8. **A new experiment directory with its own registration**
   (`experiments/08-…`), not another amendment to MVM-0a. *Ruled 2026-10-03
   (page 7), with one thing settled alongside: the compute ledger stays in
   experiment 06's folder as the programme's one record of money.* **The
   alternative not taken:** number it as a further amendment, which keeps one
   budget instrument and one ledger but attaches new work to a closed
   registration.

9. **The own-versus-named asymmetry is recorded as a known limitation rather
   than engineered away.** *Ruled 2026-10-03 (page 8).* **The alternative not
   taken:** add a condition in which the model's own name appears as a token,
   which would match the conditions exactly and would put an ownership cue
   into the text.

10. **The ownership-lesion check is a precondition for reading arm F, and is
    never reported as evidence of a centre.** *Its shape was ruled on
    2026-09-25 (the queue ruling, page 1h) and its two-of-three clause on
    2026-09-26 (RT-220); its standing as a precondition and not a finding was
    ruled 2026-10-03 (page 9).*

11. **The registered wave launches staggered**: step 5a, then 5b. *Ruled
    2026-09-21 (item 12), with item 23 settling which step the second kill
    date binds; the fit-floor stop added to step 5a by John's ruling of
    2026-09-26 on the route (b) result.*

12. **The proposal went to an independent review before John ruled on its
    open items**, per the protocol. *Done: the review of version 3, RT-230 to
    RT-236, main line at `4cb7f8e`.*

13. **The successor's registration names a launcher that waits for the
    receipt, and makes "the trainer does not delete its own machine" part of
    the registered recipe.** *Ruled 2026-10-03 (page 10).* The launcher
    file is named (section 5; RT-228); the laptop half of the handshake works
    against the real vendor and the machine half was never given the chance
    (section 10, R-11). **The alternative not taken:** leave the shutdown
    policy in unregistered operations scripts, where a later edit can quietly
    remove it. *The ruling packet's page for this decision gave as a reason a
    sentence about the programme's largest single loss; the check of the
    packets found that sentence is not what the ledger shows, and it is not
    carried here. The decision stands without it.* (Version 1's account of what one failure cost merged two events;
    the Gate C review of version 1, finding RT-186, corrected it, and the
    sentence is not repeated here.)

14. **What a no verdict maps to.** *Ruled 2026-10-03 (page 11), closing the
    no-verdict finding RT-182 of the review of version 1:* a no verdict on arm
    C fires the two-arm fallback already ruled in advance; a no verdict on
    arm M drops arm M and carries it as an extension on the weekend roadmap;
    a no verdict on arm F after arms T and C have separated is a fifth
    registered term, *metric validated, degree not read*, with the reason
    after a colon. The stop after the first full-size free-model run is
    unchanged. **The alternative not taken:** keep four terms and report an
    arm F no verdict under R1 with a sentence, which is the over-reading the
    finding warns against. Whether the fifth term counts as satisfactory is
    entry 28.

15. **Control 2's tolerance.** *Ruled twice on 2026-10-03.* In the morning
    John agreed to version 3's recommendation, 0.05 over the random subspace
    (page 12). After the controls re-run showed the control has no figure on
    any toy model, he **withdrew it**: control 2 is kept as a reported
    description with no pre-stated pass line
    (`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1; the
    morning's rulings file carries a dated note under its decisions table).
    Section 7.3, item 2. **Alternatives not taken:** the 0.018 room of the
    no-transplant rule; and exercising the control on a made-up case built
    for the purpose.

16. **Control 4's standing.** *Ruled twice on 2026-10-03.* In the morning
    John agreed to version 3's recommendation that it be reported and not a
    control that holds (page 13), on the account that arms C and F "receive
    the ownership signal by other routes". After the controls re-run and its
    diagnostic he **reversed it**: the control is redefined on the positions
    before both twins' first own turns, and it holds (the same file, ruling
    2; the same dated note). The account is withdrawn. Section 7.3, item 4.
    **The alternative not taken:** redefining the positions and keeping the
    control reported only.

17. **Whether fifty timed steps meets item R-11's five hundred.** The plan
    John authorised ran fifty after five warm-up steps; the item says five
    hundred after fifty. Recommendation: accept fifty for the second release's
    arithmetic, and take the five-hundred-step window from the first
    registered-size run of step 5a rather than from a new rental, repricing
    the later runs from it before the second release is asked for. *Ruled
    2026-10-03 (page 14), as recommended.* **The alternative not taken:**
    hold R-11 to its
    letter and rent a longer timing before asking for the second release,
    about another dollar and another go.

18. **The handshake's machine half.** Two ways to test it, from the slice
    findings' section 9 (at `9f802db`): (a) make the laptop wait, after
    writing the receipt, up to twice the watcher's polling interval before
    deleting, and have the watcher write its "receipt found" somewhere the
    laptop fetches, standard practice for a two-party shutdown, moderate
    confidence that it lets a pass be observed; (b) leave the design as it is
    and register that on the normal path the laptop is the reap and the
    watcher is the backstop, which is what can honestly be said today and
    costs nothing more to rent. *Ruled 2026-10-03 (page 15): option (b), with
    (a) as the repair if a later run shows the laptop failing to answer, and
    (a) taken off the Weekend 2 launcher items. The caution put with it is
    carried in weakness W9: twelve full-size runs rest on a backstop that has
    not fired against the real vendor.*

19. **The position sets of section 7.2 are the rehearsal's four, by name**,
    with the second described as the action position and the answer-marker
    token just before it. The ruled position clause does not say how
    positions are grouped (the repairs findings, section 3); registering the
    rehearsal's grouping is the only one that has been exercised, now under
    the registered rule. *Ruled 2026-10-03 (page 16): the rehearsal's four, by
    name.* **The alternative not taken:** register the ruled clause literally, the action position and each position
    between the source assignment and the action, one set each, which has not
    been run and would change the count.

20. **Which reading of the layer-0 exclusion is registered.** The RT-216
    ruling's first sentence keeps layer 0 at the action position set only;
    its parenthesis names the position sets spanning the acting turns, which
    on this grammar is `post-identity` alone. The two readings differ on
    `action+ans` and `action+3`, and on the toy they give the same twelve
    nominations (the check at `70be9fb`, section 4.4). *Ruled 2026-09-26: the
    reading as run, layer 0 kept at `action` only, 45 site sets on the toy and
    325 on the registered model.* Registered in section 7.2, item 2. The
    alternative that was put and not taken: the narrower reading, layer 0
    removed at `post-identity` only (55 and 351), which follows the ruling's
    parenthesis and keeps two more site sets that on the separable arms do
    move the action.

21. **The fit floor is applied per arm and seed, not per arm.** The RT-212
    ruling says a read that misses the floor "returns no verdict on that
    arm"; the re-run applied it per seed, and the check calls that an
    interpretation, moot on the toy because every arm passes or fails on all
    three seeds alike (the check at `70be9fb`, section 4.1). *Ruled
    2026-09-26: per arm and seed.* Written into sections 6.4 and 7.2. The
    alternative that was put and not taken: per arm, with the arm returning
    no verdict if fewer than two seeds of three clear.

22. **Whether the fifteen further toy models get the same treatment as the
    fifteen committed.** *Done: pull request 67 (main line at `7ed2b0e`)
    committed the six redesign models under `out-repairs/models/` and the
    nine grammar-attempt models under `out-grammar-c/models/`, with the one
    `SHA256SUMS` covering all thirty.* Section 10 now says that every toy
    result of 2026-09-25 and 2026-09-26 rests on committed models.

23. **The registered read is one read per layer at the action position, with
    a site set's fit being its worst layer (new, and ruled with the
    revision).** Put here so the choice is on the record beside the others:
    the rule's read is `repairs.fit_reads`, one logistic regression per layer
    at the mask token, scored on held-out development episodes; the label
    search's pooled per-site-set read is a different quantity and is not
    registered (section 7.2, item 3). *Ruled 2026-09-26, in John's revision
    instruction for this version.* The alternative that exists and was not
    taken: register the pooled read, which scores higher on arm F (0.556
    against 0.172 on seed 0) because it strings positions together and
    averages a span that starts at the model's own marker word, and which the
    layer-0 removal would then cut into.

24. **The fit floor applies to the piece that is transplanted** (the review
    of version 3, RT-230, serious). *Ruled 2026-10-03 (page 1), option (b):
    only sizes whose own held-out accuracy clears four fifths may be chosen,
    and that accuracy is printed beside the whole read's.* Sections 6.4 and
    7.2. **The alternative not taken:** fixing the size at 8 directions with
    the smaller sizes as extra rows.

25. **The controls re-run comes before the registration review** (the review
    of version 3, RT-233, serious). *Ruled 2026-10-03 (page 2); done and
    checked the same day* (sections 7.3 and 10).

26. **The review's four minor findings, RT-232, RT-234, RT-235 and RT-236,
    are accepted as the review states each fix.** *Ruled 2026-10-03 (page
    3).* The fit as a count on a named device and number format (section
    7.2, item 1); the whole-state floor applied twice (section 6.4, item 1);
    the fuller report for the first full-size free-model run (section 7.5);
    the depths stated the same way (section 7.2, item 1). For RT-232 this
    version follows the review's own wording and not the packet's shortening
    of it, as the check of the packets advises.

27. **The chosen piece's accuracy at the other positions of its site is
    reported, not gated, and printed both ways.** *Ruled 2026-10-03
    (`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3, and
    `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`,
    ruling 2).* Section 7.2, item 3; section 7.5. **The alternative not
    taken:** requiring four fifths at every position of the site.

28. **The fifth registered outcome is satisfactory, and is stated as weaker
    than R1.** *Ruled 2026-10-03 in John's own words, "Yes, satisfactory and
    weaker than R1" (the evening ruling, ruling 1).* That morning's record
    had counted his "Agreed on all" as settling it; the check of the packets
    found that recording honest but thin and asked him to confirm or overturn
    it, and he confirmed it. Section 3.

29. **The seven questions this version put to John.** *Ruled 2026-10-03, late
    evening, "Agreed on all" (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`).* The
    floor on the piece only; the piece rule applied after the layers are
    chosen; the registered fit on the laptop's processor; the toy's episode
    counts at full size; twenty random pieces for control 2; two seeds of
    three when an arm's seeds disagree; the competing solver run under the
    piece rule before the registration review. Section 19 gives each with the
    alternative not taken.

30. **The twelve pages of the registration review, and their follow-ups.**
    *Ruled 2026-10-06, page by page, in John's words quoted in
    `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md` (branch
    `rulings-2026-10-06-gate-a-v4` at `525a625`).* Page 1, RT-237: "(a), go
    with the recommendation" (the ownership-free line replaces the battery
    clause; section 8.2). Page 2, RT-238 and RT-244: "yes, accept". Page 3,
    RT-239: "yes, accept". Page 4, RT-240: "(a), go with the recommendation"
    (1,800 fitting episodes; option (c), a 448-wide stand-in trained on the
    laptop, not taken). Pages 5 and 9, RT-241 and A10: "accept all, go with
    the recommendations" (the outcome table; arm F's gate failure at step 5b
    is the fifth term). Page 6, the four wording fixes: "yes, accept all
    four and fold it in". Page 7, A10: "accept, go with the recommendation"
    (the joint seed rule). Page 8, A9: "accept, go with the recommendation"
    (the no-transplant rate reported, not a veto). Page 10, A6: "yes, run
    it, go with the recommendation" (the decoy test). Page 11, A13: "(a), go
    with the recommendation" (the scope phrases). Page 12, the kill case:
    "decide after the decoy test, go with the recommendation" (answered by
    decision 3 of 2026-10-07: continue through the first release on the
    packet's condition). Follow-ups: "accept all four, yes, yes" (A7, A8,
    A11, A12; both scope phrases; control 4 as the pairing check); "yes to
    the self-test, go with the recommendation" (RT-255); "yes, remove" (A2,
    the withheld figure removed); "yes, stricter, go with the recommendation"
    (R2's scope phrase; the self-test on pairings); "(a), go with the
    recommendation" (training leaves the pairings out outright). **The
    alternatives not taken** are in the two dispositions files, under each
    finding.

31. **The repair of the built arms, and the verification before the free-arm
    run.** *Ruled 2026-10-07, decision 3, "Yes this all looks good. Let's
    move forward with this", then "Rule now, don't wait for the pass"; the
    stop condition added the same day, "Yes, add the stop condition to
    decision 3".* Section 5.6; section 11, step 4b and stop S4b. **The
    alternatives not taken** (the flat-models packet, page 1): exempting the
    sharpness from weight decay with a minimum check; keeping it learned but
    never below a minimum; the in-use check alone without the fix; version
    4's plan, the fallback, unchanged.

32. **The second release kept and conditional; the outcomes renamed; the
    kill dates unchanged.** *Ruled 2026-10-07, "Keep the second release
    conditional, and withdraw the calendar dates" (decisions 3 and 4 as
    revised).* Sections 3, 11 and 14. **The alternatives not taken:**
    striking the second release (ruled that morning and withdrawn after the
    Gate C pass's RT-262); new calendar dates for the new lines (withdrawn
    after RT-258 and RT-268); renaming the terms was itself the alternative
    to the scope phrase on 2026-10-06, and became the ruling on 2026-10-07.

33. **The spending alarm's four fixes.** *Reported ruled 2026-10-06 (the
    flat-models packet, page 2; `docs/2026-10-06-tripwire-fixes-method.md`,
    section 1); no rulings file (open item 2).* Section 12.5.

34. **The training recipe** is fixed in this text from the frozen trainer's
    defaults and is **not ruled** (open item 5). Section 5.5.

35. **The bar for "the repaired route holds".** *Ruled 2026-10-08, "Rule the
    verification bar now, keep it at 0.5" (`docs/rulings/2026-10-08-verification-bar-ruling.md`; authorship mixed: the
    drafting session recommended option (a), John chose it).* Section 5.6;
    section 9; stop S4b. **The alternatives not taken:** a small bar against
    the free model's 0.000 such as 0.1; part A alone; redesigning arm C and
    arm M's stirred-in half so the built route is the only route, which
    stays the named route to a real reference if the stop fires.

36. **The December result restated under the refounding.** *Ruled
    2026-10-08, "Merge it and approve all the decisions from the doc"
    (`docs/rulings/2026-10-08-december-result-restatement-rulings.md`; authorship mixed).* The early stop of S4b is a registered ending
    of experiment C with the public sentence "the built arms as designed are
    not references; the measure was not reached"; the eight outcome terms,
    the kill dates and the caps are unchanged; the restatement is a dated
    note at the head of the December-result roadmap. Section 3 and stop S4b.

*Nothing above is registered. The registration commit, if it comes, follows
the check owed on this version, John's answers to the open items of section
21, the closure check of RT-237, and the merge of the branches of section
16; every run it affects is launched after it.*

---

## 16. Where the pieces are

- This text: `docs/successor-experiment-proposal-2026-10-07-v5.md`, with its
  method `docs/successor-registration-method-2026-10-07.md` and its handoff
  `docs/successor-registration-handoff-2026-10-07.md`.
- Version 4, unedited: `docs/successor-experiment-proposal-2026-10-03-v4.md`
  (main line at `41b0bd3`, pull request 85).
- **The records this text cites that are not on the main line, each of which
  must be merged before the registration commit (open item 10):** the
  twelve-page ruling and the four packets it adopts, with the two
  measurement files (`rulings-2026-10-06-gate-a-v4` at `525a625`); the
  inside Gate A review and its scripts (`gate-a-tier1-successor-v4` at
  `135c1f7`); the two outside reviews (`tier2-chatgpt-v4` at `6136407`;
  `tier2-gemini-v4` at `8da74c4`); the flat-models packet
  (`ruling-packet-cm-flat` at `7583326`); the check of the development runs
  and the laptop procedure's rows (`check-dev-10m` at `51ec07d`); the
  sharpness fix, the in-use check and the toy retrain
  (`fix-sharpness-inuse-check` at `644238e`); the page 4 re-run and its
  check (`page4-toy-rerun-1800` at `e948899`; `check-page4-rerun` at
  `1e168f3`); the decoy test and its check (`decoy-test-a6` at `6794155`;
  `check-decoy-test-a6` at `ba5d64f`); the training exclusion and its check
  (`training-exclusion-pairing` at `9acc566`; `check-training-exclusion` at
  `7278309`); the spending alarm's fixes and their checks (`tripwire-fixes`
  at `5e2faf9`; `check-tripwire-fixes` at `b01e564`).
- The frozen code: `experiments/08-successor-degree/` (main line at
  `53ae82c`, pull request 97; the decision code at `bd0de26`, pull request
  105), with `docs/2026-10-04-successor-code-freeze.md` and its method; the
  pinned versions, `experiments/08-successor-degree/requirements-measure.txt`.
- The rulings since version 4, on the main line:
  `docs/rulings/2026-10-07-two-sided-question-rulings.md`;
  `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`;
  `docs/rulings/2026-10-03-version-4-check-questions-rulings.md`;
  `docs/rulings/2026-10-03-version-4-questions-rulings.md` (record B);
  `docs/rulings/2026-10-03-seven-questions-reconciliation.md`.
- The runs since version 4, on the main line: the competing solver
  (`docs/2026-10-03-competing-solver-run.md`, outputs
  `experiments/rehearsal-successor-measure/out-competing-solver-run/`); the
  twenty-piece control's code test (`docs/2026-10-03-control-2-twenty-draws.md`,
  `out-control-2-twenty-draws/`); their check,
  `reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`;
  the decision procedure (`docs/2026-10-06-successor-a2-decision-procedure-findings.md`,
  `experiments/08-successor-degree/out-a2-cases/`) and its checks
  (`reviews/2026-10-06-a2-decision-procedure-check-claude-code.md`,
  `reviews/2026-10-06-a2-additions-check-claude-code.md`); the four
  development runs' files (`experiments/08-successor-degree/artifacts/`) and
  their ledger rows.
- Version 3, unedited: `docs/successor-experiment-proposal-2026-09-26-v3.md`
  (main line at `6d4ec3a`, pull request 71). Version 2, unedited:
  `docs/successor-experiment-proposal-2026-09-26-v2.md` (main line at
  `a3013be`, pull request 54). Version 1, unedited:
  `docs/successor-experiment-proposal-2026-09-21.md`.
- The first independent review of version 3, whose two serious findings and
  five minor ones this version repairs:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`
  (RT-230 to RT-236; main line at `4cb7f8e`, pull request 74), with its
  scripts in `reviews/2026-10-03-successor-v3-gate-c-scripts/`.
- The three rulings of 2026-10-03 this version is built to:
  `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (sixteen pages;
  main line at `56a5a86`, pull request 75; its dated note at `fe5df65`), with
  its packet `docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md`;
  `docs/rulings/2026-10-03-controls-rerun-rulings.md` (three rulings; main
  line at `fe5df65`, pull request 77), with its packet
  `docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md`; and
  `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` (the
  evening ruling; main line at `f32ba0c`, pull request 81). **This version
  quotes the rulings files and the toy records, not the packets.**
- The check of the two packets and their records:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md`
  (main line at `f32ba0c`, pull request 81).
- The controls re-run: `docs/2026-10-03-controls-rerun.md`, its method
  `docs/controls-rerun-method-2026-10-03.md`, code
  `experiments/rehearsal-successor-measure/src/rerun_controls.py` and the
  after-the-fact diagnostic `src/posthoc_control4.py`, outputs
  `experiments/rehearsal-successor-measure/out-controls-rerun/` (main line at
  `821f154`, pull request 76); its check,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md`,
  with scripts in `reviews/2026-10-03-controls-rerun-check-scripts/` (main
  line at `e184a6e`, pull request 79).
- The short pre-stated run: `docs/2026-10-03-short-prestated-run-method.md`
  (main line at `9e978d9`) and `docs/2026-10-03-short-prestated-run.md` (main
  line at `853988f`; pull request 80), code `src/short_prestated_run.py`,
  outputs `experiments/rehearsal-successor-measure/out-short-prestated-run/`,
  of which `part_c_NOT_A_RESULT.json` is named for what it is. Its check,
  which also checks the record of the evening ruling:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`,
  with scripts in `reviews/2026-10-03-short-prestated-run-check-scripts/`.
  (main line at `53c8100`, pull request 82).
- John's late-evening ruling on this version's seven questions:
  `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
  filed with this version on pull request 83.
- The Gate C tier 1 review of version 2, whose one fatal finding and four
  serious findings this version repairs:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
  (RT-212 to RT-229; main line at `c17dbdc`, pull request 56), with its
  scripts in `reviews/2026-09-27-successor-v2-gate-c-scripts/`.
- The earlier rulings, all still binding:
  `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` (main line at
  `3af189d`, pull request 60; its refinements at `4bb5727`, pull request 63;
  the annotation of refinement 2's arm C clause at `da41c20`, pull request
  68; the resolution of RT-212 item 3 after the label search at `a11f1d3`,
  pull request 69);
  `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` (five decisions and
  five annotations; main line at `62c3824`, pull request 53);
  `docs/rulings/2026-09-26-weekend-1-queue.md` (nine pages, 2026-09-25);
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (the
  releases, the staggered launch, halt not trim, item 23 on the dates);
  `docs/rulings/2026-09-23-nomination-label.md` and
  `docs/rulings/2026-09-23-range-and-direction-only.md`;
  `docs/rulings/2026-09-20-center-as-degree.md` and
  `docs/rulings/2026-09-20-december-result-roadmap.md`. John's rulings of
  2026-09-26 on decisions 20 and 21 are recorded in the first of those files
  (main line at `9ed9f8c`, pull request 72); his ruling on decision 23 is
  carried from his revision instruction for version 3 and has no ruling file
  of its own.
- The three earlier rehearsals: `docs/2026-09-21-successor-measure-rehearsal.md`
  (main line); `docs/2026-09-26-rehearsal-repairs.md` (main line at
  `882f252`, pull request 52; checked at `d216dbc`, pull request 58); and
  `docs/2026-09-26-toy-rerun-v3-rules.md` (main line at `9d9d31a`, pull
  request 62; checked at `70be9fb`, pull request 65), with their method notes
  `docs/successor-measure-rehearsal-method-2026-09-21.md`, its denominator
  addendum, `docs/rehearsal-repairs-method-2026-09-25.md` and
  `docs/toy-rerun-v3-rules-method-2026-09-26.md`; code and outputs under
  `experiments/rehearsal-successor-measure/` (`out/`, `out-repairs/`,
  `out-v3-rules/`).
- The thirty trained toy models:
  `experiments/rehearsal-successor-measure/out-repairs/models/` (twenty-one)
  and `experiments/rehearsal-successor-measure/out-grammar-c/models/` (nine),
  with the one `SHA256SUMS` and the `README.md` in the first folder (main line
  at `8038275`, pull request 64, and `7ed2b0e`, pull request 67).
- The grammar attempt: `docs/2026-09-26-grammar-attempt.md` (main line at
  `ff778ea`, pull request 57; its method note
  `docs/grammar-attempt-method-2026-09-25.md`; outputs `out-grammar-c/`),
  checked at `f1ea004` (pull request 61):
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`.
- The route (b) label search: `docs/2026-09-26-free-arm-label-search.md`
  (main line at `a97c12b`, pull request 66), and its check,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`
  (main line at `ecd2b6c`, pull request 70).
- The rented slice: `docs/2026-09-25-rented-slice-findings.md` (first attempt,
  main line) and `docs/2026-09-25-rented-slice-attempt-2-findings.md` with
  the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
  (main line at `9f802db`, pull request 51; checked at `afb5183`, pull request
  55).
- Amendment A3's closure, registered: `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
  the closure block of 2026-09-25, and
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`.
- The roadmap it implements: `docs/december-result-roadmap-2026-09-20.md`,
  sections 2, 4 and 5 as amended 2026-09-21, with the two dated notes of
  2026-10-03 under its outcome table; the weekend schedule laid over it,
  `docs/weekend-roadmap-2026-09-24.md`.
- The spend record every figure in section 12 is drawn from:
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, with its
  ceiling note of 2026-09-25 and its rows of 2026-09-21 and 2026-09-25 (lines
  93 to 95).
- The review it will be attacked under: `docs/outside-review-protocol.md`,
  Gate A, both tiers, with the list it is run against,
  `docs/known-failure-modes.md`; this version's own run of that list is
  section 17.
- The Wittgenstein note cited in section 2 as non-binding motivation: the
  TimeAssembler document `d08c23ae-7dca-4e55-9ac3-bb785ebed652` on the
  Minimum Viable Mind project; not a file in this repository.

---

## 17. This version's failure-mode pass, entry by entry

The outside-review protocol's failure-mode pass belongs to the Gate A tier 1
reviewer, and "an author's run never stands in for the reviewer's"
(`docs/outside-review-protocol.md`, "The failure-mode pass"). This is the
author's run on version 5, made so that the reviewer's hour is not spent on a
defect already known, and kept in this document so that a reader sees it
without opening a second file. The list (`docs/known-failure-modes.md`) has
six numbered entries on the main line and a seventh candidate, drafted in
`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 9,
item 2, which John has not ruled onto the list (the 2026-10-06 ruling, page
6: the inside review's test for gate clauses is folded into that entry when
it is ruled). All seven were run here, on 2026-10-07, with this session's own
commands, on the committed outputs of the page 4 re-run (the rows of
`experiments/rehearsal-successor-measure/out-page4-rerun-1800/models-1800/`,
branch `page4-toy-rerun-1800` at `e948899`, extracted with `git archive` into
a scratch folder), of the competing-solver run (`out-competing-solver-run/`
on the main line), of the short pre-stated run and of the decision procedure
(`experiments/08-successor-degree/out-a2-cases/`), and on this text.
`.venv/bin/python` stands for the project's own Python (torch 2.12.1,
scikit-learn 1.9.0, numpy 2.5.0), run by its full path from this worktree.
Nothing was rented, created, trained or spent, and no registered, ruling or
protocol text was edited. The script that printed the blocks below is this
session's `failure_pass_v5.py`, kept in its scratch folder and described
here command by command; the inside review's own pass on version 4 (branch
`gate-a-tier1-successor-v4`, `failure_mode_pass.py`) was read after this one
was run, and nothing below is copied from it. **Version 4's section 17 ran
the same tests on the 420-fitted outputs; every block below is this
session's own run.**

**1. A comparison whose denominator was zero. Does not fire on any model that
reads; the case it fired on in version 4 (the printed floor admitting a model
at chance, RT-238) is now refused by the text. MEASURED.** Part one asks
whether the ceilings typed in trace to committed measurements: every
no-transplant rate is read from a named field of a committed row, none typed
(the script prints each with its file and field; for example `C/0:
accuracy_untouched 0.0512 <- out-page4-rerun-1800/models-1800/row_C_seed0.json,
primary.reading.accuracy_untouched`). Part two, the denominator and the top
of the scale at the site set the rule chose, with every read fitted on 1,800:

```
$ .venv/bin/python failure_pass_v5.py        # the failure 1 blocks
arm/seed  untouched  whole   own-acc | denominator  floor-needs | top of scale | status
T/0       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
T/1       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
T/2       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
C/0       0.0512    0.5400  0.5487 |  0.4888       0.3980    |  1.0000 | reads
C/1       0.0488    0.5575  0.5813 |  0.5088       0.4260    |  1.0000 | reads
C/2       0.0600    0.5463  0.5525 |  0.4863       0.3940    |  1.0000 | reads
F/0       0.0587    0.4850  0.5587 |  0.4263       0.4000    |  1.0000 | described only, no reading
F/1       0.0563    0.5713  0.5663 |  0.5150       0.4080    |  1.0000 | described only, no reading
F/2       0.0688    0.5138  0.5563 |  0.4450       0.3900    |  1.0000 | described only, no reading
M/0       0.0125    0.8050  0.8712 |  0.7925       0.6870    |  1.0000 | reads
M/1       0.0175    0.7738  0.8800 |  0.7563       0.6900    |  1.0000 | reads
M/2       0.0138    0.7937  0.8712 |  0.7800       0.6860    |  1.0000 | reads
smallest denominator among those that read: 0.4863 (C/2); the requirement above zero (section 6.4 item 1) holds on every row above: True
```

```
the competing solver's development grids (out-competing-solver-run/nominate_blind_seed*_*.json, dev_accuracy and dev_untouched):
  seed 0 channel_removed: own-directed 0.2333, untouched 0.2400, floor asks for -0.0053 -> requirement above zero: False
  seed 0 channel_left_on: own-directed 0.2383, untouched 0.2417, floor asks for -0.0027 -> requirement above zero: False
  seed 1 channel_removed: own-directed 0.2100, untouched 0.2300, floor asks for -0.0160 -> requirement above zero: False
  seed 1 channel_left_on: own-directed 0.2100, untouched 0.2300, floor asks for -0.0160 -> requirement above zero: False
  seed 2 channel_removed: own-directed 0.2333, untouched 0.2300, floor asks for +0.0027 -> requirement above zero: True
  seed 2 channel_left_on: own-directed 0.2367, untouched 0.2300, floor asks for +0.0053 -> requirement above zero: True
```

Among the nine pairs that read, the smallest denominator is 0.4863 (arm C
seed 2); the top of the scale is 1.0000 on every arm. The per-arm-ceiling
repair (RT-172) holds at 1,800 fitting episodes as it held at 420. The case
the inside review found (RT-238: the floor as version 4 printed it admitted
every site set on four of the solver's six runs with a divisor at or below
zero) is the four rows above where the requirement is not above zero; section
6.4, item 1, now refuses them in words, as the code did. One thing to watch,
ARGUED: on arm F the denominator clears what the floor needs by 0.026 to
0.107.

**2. A probe target that cannot be recovered in principle. Fires on the free
arm, and is caught by a registered rule. MEASURED.** Part one, the
route-sentence search, with this design's own wording in the pattern, run on
sections 0 to 16 of this file:

```
$ awk '/^## 17\. /{exit} {print}' docs/successor-experiment-proposal-2026-10-07-v5.md > "$T/v5-through16.md"
$ grep -n -iE 'route by which|carried by the token|forced by the loss|is the input token' "$T/v5-through16.md"
1870:   own**. *The route by which that quantity reaches the model's states, in one
1871:   sentence:* the marker word is the input token at every turn the model's own
1872:   assignments are spoken on, so it is carried by the token into the running
1876:   claim, that which marker word is the model's own is forced by the loss at
```

A route sentence exists (section 7.2, item 1), and the fourth match is the
sentence striking version 2's loss clause, not a route. Part two, the two
runs on the same instrument with the same bar: the committed counts per
running state (whole read | best piece of 1, 2, 4 or 8 directions), the built
arms as the positive control and the free arm as the target run:

```
  T/0 180|180 180|180 180|180 180|180 180|180 -> nominated
  T/1 180|180 180|180 180|180 180|180 180|180 -> nominated
  T/2 180|180 180|180 180|180 180|180 180|180 -> nominated
  C/0  17| 17 180|180 180|180 180|180 180|180 -> nominated
  C/1  17| 17 180|180 180|178 180|178 180|178 -> nominated
  C/2  17| 17 180|180 180|180 180|180 180|179 -> nominated
  F/0  17| 17  34| 30  30| 30  36| 40  34| 33 -> read failed its floor: no size's piece reaches four fifths
  F/1  17| 17  15| 18  17| 17  20| 19  14| 19 -> read failed its floor: no size's piece reaches four fifths
  F/2  17| 17  25| 24  39| 36  30| 27  27| 28 -> read failed its floor: no size's piece reaches four fifths
  M/0 180|180 180|180 180|180 180|180 180|180 -> nominated
  M/1 180|180 180|180 180|180 180|180 180|180 -> nominated
  M/2 180|180 180|180 180|180 180|180 180|179 -> nominated
  separation (lowest C minus highest T): 1.0000; clears 0.5: True
  arm M readings: [0.5252, 0.4793, 0.5208]; prediction met: True
```

The middle limb, "the second run clears the bar and the first does not", is
the free arm's state at 1,800 as it was at 420: on arms T, C and M a piece
reaches 144 of 180 at every running state past the injection, and on arm F
none does at any (at most 40). **This is the fatal finding of the review of
version 2, RT-212, and it still fires on the free arm.** The design catches it
rather than repairing it: the floor on the piece turns it into a registered
no verdict on arm F on every seed, and the withdrawn number is not reported
as a reading. **A second place the same failure fires, new at 10 million
parameters:** on the real development checkpoints the procedure's read found
no readable ownership in arms C and M either (best pieces 41 and 45 of 180
against 144; the check of the development runs, section 7; not recomputed
here), which is the independent face of the flat ownership answer of section
5.6; the registered rule returned no verdict on both. **A third, carried
from version 4 and now narrower:** the named agent's read that control 2
needs reached the floor on one toy model of six at 1,800 (section 7.3, item
2); that control carries no pre-stated number, by ruling.

**3. A cell that is empty by construction. Does not fire on any reported
cell; one gate clause has no field in the toy's records, and the text says
so. MEASURED.** Part one, the cells:

```
  control 6, T/0: same-value trials 81, different-value trials 719 (C/0, F/0, M/0 the same; seeds 1 and 2 the same: the relaxed set has a fixed seed)
  control 4, T/0: twins' states identical at the sites True, trials whose action changed 0, largest output difference 0.0
  control 4 as redefined, positions transplanted per pair (the short pre-stated run, part_a.json): {'max': 21, 'mean': 5.2125, 'min': 1}
  control 2: toy models on which it returned a figure at 1,800 fitting episodes: 1 of 6 it applies to (arm F seed 0)
  the two-of-three seed rule: arms whose three seeds disagree on the toy: 0 of 4
  the channel-removal clauses, fields in the gate record: ['bar', 'episodes', 'lesion_collapses_own', 'lesioned_other_correct', 'lesioned_own_correct', 'other', 'other_clears', 'other_correct', 'own', 'own_clears', 'own_correct', 'seed_passes']
```

Both of control 6's cells have trials on every arm and seed (the RT-173
repair holds). Control 4 as redefined transplants at one position or more in
every pair. Control 2 returned a figure on one toy model of six at 1,800
(none at 420), so its cell is no longer empty by construction on the toy; the
text says what it shows (section 7.3, item 2). The seed rule has never been
exercised on a real split; it has on made-up cases (R-13). **The ownership-free
line of section 8.2 (1,546 of 3,000) has no field in the toy's committed
rows, which predate it**: its field lives in `procedure.gate` on the main
line at `bd0de26`, and the decision procedure's case 17 shows what the code
does when the field is missing ("not run", the fifth term). So on the toy
record this clause is evaluated from the dispositions' separate measurement
(2,100, 2,238 and 2,324 of 3,000), not from the registered rows; the first
registered rows to carry the field are the reruns of step 4b. This is the
inside review's RT-237 test for gate clauses ("a clause with no field is the
finding"), and it is stated rather than stepped over. Part two, the generator
property that empties a cell, is section 4.2's distinctness, read and named
there, and the training stream's refusal of fresh and relaxed pairings
(section 4.3) adds a second property read and named. Part three, thresholds
at both ends, for every threshold this version attaches to a count:

```
  learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05: 790, share 0.2633, tail 0.0485
  ownership-free line: smallest k with P(X>=k | n=3000, p=1/2) <= 0.05: 1546, tail 0.0483; the ruled line is 1,546: True
  a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability 0.0485 per seed
  ownership-free line at both ends: trained free model 2,100 / 2,238 / 2,324 pass; untrained 0 / 620 / 726 fail; a model that lost the item about 2,257 passes
  no-transplant formula at own-directed 1.0: 0.0000; 0.8712: 0.0184; 0.56: 0.0629; 0.2633: 0.1052; a broken pairing (0.125) flagged by the 0.018 room in every case: True; reported, not a veto
  a correctly paired model whose errors go to the other three agents, p = 0.8: rate 0.0667 against formula 0.0286, gap 0.0381 > 0.018: True (why it is no longer a veto)
  piece floor at 144 of 180: the free model's best piece anywhere 40; the built arms' chosen pieces [165, 178, 178, 180, 180, 180, 180, 180, 180]
  the in-use check at both ends: arm T 1.000 passes; the 10-million arms C 0.018 and M 0.000 fail; the toy arms C 0.22 to 0.29 and M 0.07 to 0.11 fail at 0.5 (the bar ruled 2026-10-08)
```

The bar reproduces at 790 of 3,000 and the ownership-free line at 1,546 of
3,000, both from the exact binomial tail. The ownership-free line passes
every trained toy model and fails untrained weights, and the text says what
it cannot tell (a model that lost the item). The no-transplant formula flags
a broken pairing at every accuracy and would also flag a correctly paired
model that confuses owners, which is why it reports and no longer withholds
(section 6.4, item 3). The piece floor has room on both ends on the toy (40
against 165 to 180). **The in-use check fails on the working end of the toy
(arms C and M, trained and reading correctly) and on the broken end (the
10-million arms, flat), so as a threshold it does not yet separate the two
ends on the toy; that is weakness W17 (the bar ruled 2026-10-08), stated rather than
stepped over.** Control 4's pass line, bit-identical outputs, has no working
end to test; it cannot fail on a correctly built model, which section 7.3,
item 4, says.

**4. A claim of measurement with no record, or a record that does not
reproduce. Fires on three classes of figure, each said so in the text.
MEASURED.** Part one, the two sweeps, run on sections 0 to 16 of this file
(cut at this section's heading, because this section's own output blocks
match the patterns and would count themselves):

```
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' "$T/v5-through16.md"
1136
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' "$T/v5-through16.md"
399
$ grep -c MEASURED "$T/v5-through16.md"; grep -c ARGUED "$T/v5-through16.md"; wc -l < "$T/v5-through16.md"
105
16
4691
```

(Version 4's section 17 printed 759, 233, 68, 14 and 3,406 on its sections 0
to 16; the inside review found 761 and 235 after the late-evening rulings
were written in.) Part two was run three ways. **(a) Every paragraph with a
figure names a record**: of the paragraphs in sections 0 to 16 that carry a
figure, the script lists those naming no file, record, ruling, section,
page, review, check or item; after the two repairs made on its first run (the
in-use check's part A bullet and the 12.1 paragraph), the ones left are table
rows and a heading whose source is the sentence above them. **(b) The
repository's two checkers, run on the whole document as it stands:**

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-10-07-v5.md
[CONFIDENT] 50 reference(s) name a file that is not in the repository
  (every one is a file on one of the fifteen unmerged branches of section 16, cited by branch and commit, or a script in the inside review's folder on its branch, or the handoff note written beside this text; none is a file that exists at no commit)
[LOOK AT IT] 11 bare name(s) match more than one file; 12 name(s) of run-output files that are not in the repository; 14 reference(s) written with a gap or a wildcard
[CONFIDENT] 1 exact figure(s) absent from the one file their sentence cites
  (the count of arm M's entangled gate episodes, 1,810, in a sentence of section 5.3 carried unchanged from versions 3 and 4: the file cited holds the share and not the count, which is that share of the gate's episodes; version 4's checker run found the same)
$ .venv/bin/python scripts/check_single_source.py --only docs/successor-experiment-proposal-2026-10-07-v5.md
[CONFIDENT] Group 1: a dollar figure the ledger does not contain: 2 found
  ($221.85, version 4's headroom, and $7.39, what is left of the development line: both arithmetic on ledger rows, and each sentence now says so)
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source: 2 found
  (both in one sentence of section 12.2, carried from version 4, cited to the 2026-09-21 ruling that set the two releases, which is the figures' source; version 4's run found the same two)
```

**(c) The red-team ledger's rows for the findings this text cites:**

```
  ledger rows for RT-237 to RT-246: 0 of 10 (rows are owed: the 2026-10-06 ruling)
  ledger rows for RT-247 to RT-256: 0 of 10 (rows are owed: the 2026-10-06 ruling)
```

**Where the entry fires, and what the text does about it.** First, **fifty
of the records this version cites exist at no main-line commit**: they are on
the fifteen branches of section 16, and a registration commit may not rest on
a record its reader cannot open at a main-line commit (RT-145's form, the
uncommitted-citation finding). The header says so, section 16 lists them, and
open item 10 asks for the merges before the commit; until then this text is
a draft and not a registration. Second, **the ledger carries no row for any
finding from RT-237 on**, although the 2026-10-06 ruling assigns RT-247 to
RT-256 and says the rows are owed; this text uses the numbers the ruling
assigns, and open item 12 asks for the rows. Third, **one class of toy figure
does not rest on a committed model of the registered kind**: every toy
reading quoted was measured on models whose sharpness was learned, while the
registered built arms have it fixed; the hand-set models have been read on
one of nine (section 5.6, W17). Fourth, carried from version 4: the figure on
the average over a site does not reproduce to the episode under a different
order of addition (section 7.2, item 3); the 1,810 count is a share times a
count; the controls re-run's 0.0100 is quoted as 0.0099. **Every MEASURED
figure this version adds was read against the file named beside it** (the
page 4 re-run's rows and summary, the sharpness findings' tables, the
development-runs check's tables, the decoy test's table, the dispositions'
measurements, the decision-procedure results), and the two checkers see only
what they are built to see.

**5. A command that creates something while documented as creating nothing.
Does not fire on anything this document runs; the launcher the registered
runs use is the derived one. MEASURED.** The proposal runs nothing that
touches a vendor. The list's own test, run by this session (the last lines of
its output; every line above them is `[ ok ]`, with the standing prohibition
on the registered `launch_a3.sh` printed as expected):

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
  ...
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

(exit status 0.) The successor's launcher, `launch_successor.sh`, is not
among the three this check exercises; the code freeze's test T7 ran the same
kind of checks on it (refuses an argument and says why, names `DRYRUN=1`, a
dry run exits 0 and creates nothing, refuses without its settings, refuses
the toy size, reports a halt file), and the training-exclusion branch re-ran
T7 with the same 21 checks passing. The four development runs created four
machines on John's go, each named in a ledger row written after the run with
his words quoted; that is a launch, documented as one.

**6. A remote step tested only against stand-ins. The launcher's check
passes; the spending alarm has now met the far end once and failed, and its
fix has met only the stand-in. MEASURED.**

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.0s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
```

On the design, what stood in for the far end, step by step. The shutdown
handshake's machine half: in the development runs the laptop deleted each
machine within about 15 seconds of writing the receipt, before the machine's
own watcher acted, so the machine half was again not exercised (W9; the
check of the development runs, section 2). Arm M's code on the rented
machine: now run once, in the development runs (R-14). **The spending alarm:
met real billing once and could not have caught a fault (section 12.5); its
four fixes were tested against a stand-in vendor on five made-up waves and
checked three times, and have not met the vendor.** The registered
measurement code on a full-size model on the laptop's processor: the
30-million shape has been timed (RT-245) and the pipeline run end to end on
untrained 30-million models (the freeze, test T6), not on a trained one. The
in-use check: run on the real 10-million checkpoints and on the toy, not yet
on a repaired checkpoint. Each is said in the text; none is counted as
tested.

**Candidate 7. An outcome line a plan states in advance that the design
cannot produce on the path it expects. Fires on one line, which the text
states as open; does not fire on the others. MEASURED.** The drafted test:
for each pre-stated line, name the code path that prints each signal it
needs, and show that path can run in the order the line requires.

```
  terms reached by the decision procedure's made-up cases (out-a2-cases/results.json): ['R1', 'R2', 'R3', 'fallback_not_read', 'fallback_read', 'fifth', 'not_validated']
  the toy's own outcome at 1,800 (pre-A2 rules, to be re-summarised): R3, 'substrate not a testbed', reason 'arm(s) F failed the gate'
```

- **The eight outcome terms of section 3:** each reached by at least one of
  the 25 made-up cases, and no output carries a term that is not registered
  (R-13). **The renamed words are not yet in the code**, which prints version
  4's names (open item 3): a line the design can produce under a name the
  text no longer uses, until the code follows the ruling.
- **The toy's own outcome line:** R3 as the toy actually is; the fifth term
  if seed 0 is taken as the step 5a run (section 3); produced by the
  decision procedure's cases 1 to 3. The page 4 re-run's outcome line was
  made under the pre-A2 rules and is to be summarised again (section 10).
- **Arm M's pass line** ("between 0.3 and 0.7 on every seed, and within 0.10
  of its true-slot reading"): produced, both halves, at 1,800 (failure 2's
  output above: prediction met).
- **The separation line** (0.5): produced, 1.0000.
- **Control 4's pass line**: produced on all twelve, by code committed before
  its output, reproduced byte for byte by its check (main line at `53c8100`).
- **Control 2's reported description**: produced on one toy model of six at
  1,800; the text says so and attaches no line to it.
- **The ownership-free line** (1,546 of 3,000): its field is in
  `procedure.gate` on the main line and not in the toy's rows (failure 3
  above); produced on the toy by the dispositions' separate measurement; the
  code path that prints it in a registered row first runs at step 4b. Stated.
- **The in-use check's two lines** (0.9; 0.5): produced on 14 made-up cases
  on real models and on 28 decision-code cases; **on the toy's real arms C and
  M the line is not met**, before and after the fix, so the verification of
  step 4b at the bar as coded is a line the design has not produced on any
  built-to-be-entangled model. **This is the one place the candidate fires
  on this version.** The bar is ruled at 0.5 (2026-10-08), and the firing
  stands as the record's own prediction that the stop of S4b will most
  likely fire, which the ruling says in its own words.
- **The money lines of section 12:**

```
  spent to the ledger's last row: 229.62; version 4's 228.15 plus the development line's 1.47 = 229.62: True
  development line: spent 1.47 (0.47 + 0.34 + 0.33 + 0.33), reruns about 1.14 (T, C, M actuals), committed 2.61 of 10, left 7.39
  ruled split: first release 44.00 + second release without its re-run line 119.06 = 163.06
  arm M as ruled at 32: programme after 423.21, left 26.79, meets the 10 floor: True
  arm M as ruled at 44: programme after 435.21, left 14.79, meets the 10 floor: True
  second release including arm M, note's split: 159.90 to 171.90; ruled split: 149.06 to 161.06
  arm M at 1.44 times arm F's 10.04 per run, three runs: 43.37; inside the ruled 32 to 44: True
```

  The wager meets its floor on every split and at both ends of the range;
  the development runs sit inside the first release's $44, so the base is
  unchanged; the ruling's "about $150 to $172" for the second release is the
  note's split with arm M at $30 to $42.

Whether the candidate is a new species or an instance of failure 3 is John's
ruling, still open; on this version it catches the in-use check's bar, which
failure 3's part three catches too.

**What this pass leaves open, in one place.** The twelve open items of
section 21; the check of this version by a session that did not write it;
the closure check of RT-237 on this text; the merges of section 16; the
ledger's rows; the eleven re-reads of the hand-set toy models; the
re-summary of the page 4 re-run under the current decision code; the
reviewer's own pass, which is still owed, as the protocol says.

**The two scans the method note promised, run on the finished file.**
Em-dashes and en-dashes: `grep -c` for each character returns 0 and 0
(version 4: 0 and 0). Bare identifiers: the script `scan_ids.py` lists every
RT number, commit identifier, pull request number, branch name and outside
finding label and flags any with fewer than three descriptive words within
ninety characters; it found 845 identifiers on 533 lines and flagged none, and this session read every line of the new text for the same thing by eye, which is the weaker of the two instruments and the one the heuristic cannot replace.

---

## 18. The printed site list for the registered model

The site list is registered as the rule that generates it (section 7.2, item
2), and the registration prints the list beside the rule. This is the list,
printed by the rule and not typed by hand. A layer set is written as its
first and last running state: "3-5" is states 3, 4 and 5 together. State 0 is
the running state straight after the input embedding, where the acting
channel is added; states 1 to 12 are the outputs of the twelve blocks. Each
row lists every layer set that begins at that state, and the position sets
each of them is a candidate at. Every site set whose layers include state 0
is a candidate at the action position set only; every other layer set is a
candidate at all four position sets (`action`, the action position alone;
`action+ans`, the action position and the answer-marker token just before it;
`action+3`, the action position and the three positions before it;
`post-identity`, every position from the model's first own turn to the
action). No site set spans every position. The toy's list is printed after
it, for comparison with the 45 the controls re-run's code asserts.

```
$ .venv/bin/python -c "
def contiguous(n): return [(a,b) for a in range(n) for b in range(a,n)]
P4=['action','action+ans','action+3','post-identity']
def name(a,b): return str(a) if a==b else f'{a}-{b}'
for label,n in (('registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)',13),('toy model: 5 running states',5)):
    L=contiguous(n); total=0
    print(label)
    for a in range(n):
        sets=[name(x,y) for x,y in L if x==a]
        ps=['action'] if a==0 else P4
        total+=len(sets)*len(ps)
        print(f'  first state {a:>2} | at {", ".join(ps)} | layer sets: {", ".join(sets)} | {len(sets)} x {len(ps)} = {len(sets)*len(ps)} site sets')
    print(f'  total: {total} site sets, {4*total} comparisons at sizes 1, 2, 4 and 8')"
registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4, 0-5, 0-6, 0-7, 0-8, 0-9, 0-10, 0-11, 0-12 | 13 x 1 = 13 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4, 1-5, 1-6, 1-7, 1-8, 1-9, 1-10, 1-11, 1-12 | 12 x 4 = 48 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4, 2-5, 2-6, 2-7, 2-8, 2-9, 2-10, 2-11, 2-12 | 11 x 4 = 44 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4, 3-5, 3-6, 3-7, 3-8, 3-9, 3-10, 3-11, 3-12 | 10 x 4 = 40 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4, 4-5, 4-6, 4-7, 4-8, 4-9, 4-10, 4-11, 4-12 | 9 x 4 = 36 site sets
  first state  5 | at action, action+ans, action+3, post-identity | layer sets: 5, 5-6, 5-7, 5-8, 5-9, 5-10, 5-11, 5-12 | 8 x 4 = 32 site sets
  first state  6 | at action, action+ans, action+3, post-identity | layer sets: 6, 6-7, 6-8, 6-9, 6-10, 6-11, 6-12 | 7 x 4 = 28 site sets
  first state  7 | at action, action+ans, action+3, post-identity | layer sets: 7, 7-8, 7-9, 7-10, 7-11, 7-12 | 6 x 4 = 24 site sets
  first state  8 | at action, action+ans, action+3, post-identity | layer sets: 8, 8-9, 8-10, 8-11, 8-12 | 5 x 4 = 20 site sets
  first state  9 | at action, action+ans, action+3, post-identity | layer sets: 9, 9-10, 9-11, 9-12 | 4 x 4 = 16 site sets
  first state 10 | at action, action+ans, action+3, post-identity | layer sets: 10, 10-11, 10-12 | 3 x 4 = 12 site sets
  first state 11 | at action, action+ans, action+3, post-identity | layer sets: 11, 11-12 | 2 x 4 = 8 site sets
  first state 12 | at action, action+ans, action+3, post-identity | layer sets: 12 | 1 x 4 = 4 site sets
  total: 325 site sets, 1300 comparisons at sizes 1, 2, 4 and 8
toy model: 5 running states
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4 | 5 x 1 = 5 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4 | 4 x 4 = 16 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4 | 3 x 4 = 12 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4 | 2 x 4 = 8 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4 | 1 x 4 = 4 site sets
  total: 45 site sets, 180 comparisons at sizes 1, 2, 4 and 8
```

**The count this implies, frozen with the list:** 325 site sets, each at four
sizes of piece, so 1,300 comparisons in the nomination family for each arm
and seed. Under the stricter variant (the sensitivity row) the first row
drops out: 312 site sets and 1,248 comparisons. Both agree with section 7.2,
item 2, and with the review of version 3, which recomputed them ("What was
checked and held"). The registered measurement code asserts the count before
it runs, as the toy code does.

---

## 19. The seven questions version 4 put to John, each ruled, four of them not as suggested

Seven places where the session that wrote version 4 did not think the answer
was its to give. **John ruled on all seven on 2026-10-03, late evening, in
the words "Agreed on all", twice over: once to the packet of the session that
wrote version 4 (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
record A) and once to a second session's packet
(`docs/rulings/2026-10-03-version-4-questions-rulings.md`, record B), and the
two records differ on rulings 2, 3, 4 and 6; John ruled that record B stands
on all four** (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`).
So "each now ruled as suggested", version 4's heading, is not true of four:
the body of this text follows record B and the reconciliation where the
suggestion and the final ruling differ (the check of version 4, finding 3;
its fix 28). The check also found six places where record B says more than
record A without conflict; under the reconciliation both records stand, and
this text carries record B's fuller points (the check-questions ruling of
2026-10-03, "For John to know"). **Two of the seven have since been amended
by the ruling of 2026-10-06:** ruling 4, for the read's fitting count only
(now 1,800 of 1,980: page 4), and ruling 6, part 1, for how a seed counts
(now: only if it passes everything: page 7). The questions are left below as
they were put, so that a reader can see what was chosen against what;
"written as run" and "this version says" in them describe version 4's first
filing. None of them changes a toy figure.

1. **Does the whole read still have to reach four fifths, now that the piece
   does?** The ruling of 2026-09-26 (RT-212) put the fit floor on the whole
   read, at the worst layer of the nominated site set. The ruling of
   2026-10-03 (page 1) says only sizes whose own accuracy clears may be
   chosen, printed "beside the whole read's", and does not say whether the
   earlier floor remains a second condition. The controls re-run applied the
   floor to the piece only. On the toy both readings give the same twelve
   verdicts, but a piece can score an episode or two above its whole read.
   *Written as run: the floor is on the piece (sections 6.4, item 2, and
   7.2, item 1).* **Suggestion: the piece only, with the whole read's count
   printed.** Confidence moderate. It is the piece that is transplanted, and
   a second floor is a second way to return no verdict on the arm being read,
   for no gain the first does not give. Strongest alternative: require both,
   which costs nothing on the toy and keeps the 2026-09-26 ruling to its
   letter.

2. **The piece rule is applied after the layers are chosen.** So it decides
   which sizes may be chosen and never changes which layers are used. That
   was the re-run method's own reading, marked as John's to overturn; the
   check noted it has not been put to him in terms. *Written as run (section
   7.2, item 3).* **Suggestion: confirm it.** Confidence moderate. The
   alternative, letting the piece's accuracy also decide between layer sets,
   has not been run, and would need the toy re-run again before the
   registration review.

3. **Which device, and which number format, is the registered fit computed
   on?** The ruling (page 3, RT-232) says the registration names them and
   that the figure on the named device is the registered one. It does not
   say which. *This draft writes in the laptop's processor, the model's
   states in 32-bit, the read fitted by scikit-learn in 64-bit, the library
   versions recorded (section 7.2, item 1).* **Suggestion: confirm that.**
   Confidence high on the processor, because every toy figure in this version
   was computed on it and it is the one device every later reader will also
   have; moderate on whether the registration should also pin the library
   versions exactly or only record them. Strongest alternative: the graphics
   chip, which is faster on a 30-million-parameter model and is what the
   earlier committed fits used.

4. **The numbers of episodes at the registered size.** The brief for this
   version asks for every frozen number to be stated. Every bar is stated,
   but each is a share or a rule, and no ruling sets how many development,
   held-out and fresh episodes the registered measurement uses, how many are
   on the relaxed set, how many held-out episodes the gates are scored on, or
   how many shuffles the permutation null uses. *The registration must print
   them; this version lists them as not set (section 9, the last row).*
   **Suggestion: the toy's counts, unchanged: 600 development episodes with
   the last 180 held out, 800 fresh matched pairs, 800 on the relaxed set,
   3,000 for the gates, 200 shuffles.** Confidence moderate. They are the
   only counts the procedure has been rehearsed at, the floor is then 144 of
   180 as on the toy, and section 11 already argues the registered model's
   states fit on the laptop at that scale. Strongest alternative: more
   held-out episodes, so that the floor is not decided by a handful: at 180,
   one episode is 0.0056, and the toy has already shown fits moving by one
   episode between devices.

5. **Control 2's comparison: one random piece or twenty?** The ruling keeps
   control 2 as a description: how often the own-directed action moves under
   the named agent's piece, beside how often it moves under "a random piece".
   The code draws one, with its own seed; control 3 draws twenty. *Written
   as the code runs, one draw (section 7.3, item 2).* **Suggestion: twenty,
   reported as control 3 reports them.** Confidence moderate. With no pass
   line a single draw is a weak thing to print beside a figure. It is a small
   code change, and it would mean the code path that ran once on 2026-10-03
   is not quite the one registered. Strongest alternative: leave it at one,
   since the control is expected to return no verdict anyway.

6. **What is an arm's outcome when its seeds disagree?** The floors and the
   controls that hold apply per arm and seed, so an arm can read on two seeds
   and return no verdict on the third. The ruling on what a no verdict maps
   to (page 11) speaks of "no verdict on arm C", "on arm M" and "on arm F"
   and does not say how many seeds make that so. The separation bar is
   written "per seed" in the same way, without saying what follows if it is
   cleared on two seeds of three. On the toy every arm behaves alike on all
   three seeds, so this has never bitten. *Not written into the body beyond
   section 3 saying the case is open.* **Suggestion: the rule the design
   already uses for its gates, at least two seeds of three, with the third
   reported.** Confidence low to moderate; this is a new pre-stated rule and
   deserves his attention more than the others. Strongest alternative: all
   three seeds, which is stricter and makes the fifth outcome and the
   two-arm fallback more likely.

7. **The ordinary competing solver under the piece rule.** The protocol's
   rehearsal asks that a system with none of the structure the measure
   claims to detect be put through the same measurement. The ownership-blind
   solver and the name-only solver were scored on both conditions before the
   piece rule existed, and the controls re-run did not load them. *This
   version says so in three places and quotes no figure for them as if it
   were under the new rule (sections 7.3, 8.1 and 10).* **Suggestion: run
   the ownership-blind solver's three committed toy models through the
   nomination and reading as now registered, on the laptop at $0, method
   committed before output, before the registration review opens.**
   Confidence moderate to high. The expected result is a no verdict (a
   solver with no acting channel should have no read of its own marker that
   reaches four fifths), it is an afternoon, and without it the registration
   review's first question on "satisfied by the wrong thing" has an argument
   behind it and not a number. Strongest alternative: state in the
   registration that it was not measured under the rule, and let the
   reviewer decide whether that is a finding.

**Two things that are not questions, said so they are not found later.**
John's ruling on decision 23 (which read is the registered one) still has no
ruling file of its own; it is carried from his revision instruction for
version 3. And the five rulings of 2026-10-03 (the morning rulings, the
re-run rulings, the evening ruling, the two records of the late-evening
ruling with the reconciliation in John's own words, and the night ruling on
the check's two questions) were each given as agreement to a packet or a
suggestion, with the wording the recording session's; the records say so
themselves, and this version quotes the records.

---

## 20. Change log from version 4, keyed to the ruling or finding behind each change

Version 4's own change log from version 3 is its section 20 and is not
repeated. "The 2026-10-06 ruling" is
`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md` (branch
`rulings-2026-10-06-gate-a-v4` at `525a625`), with its pages and follow-up
items. "The 2026-10-07 ruling" is
`docs/rulings/2026-10-07-two-sided-question-rulings.md`. "The inside review"
is the Gate A review of version 4, RT-237 to RT-246. Every change below is in
the `diff` between the two files; nothing in that diff is outside this list.

- **The 2026-10-07 ruling, decision 3 and its stop-condition addition: the
  repair as an amendment; the verification; the stop.** New subsection 5.6;
  section 11, step 4b and stop S4b; sections 0, 1, 5 (intro, 5.1 to 5.4),
  6.4 item 5, 7.4, 7.5 item 16, 9 (new row), 10 (R-3, R-14, R-15), 12.1,
  12.3, 12.8, 13 (W3, W17), 15 (entry 31).
- **The 2026-10-07 ruling, decision 3: the outcomes renamed; experiment C as
  instrument research.** Sections 0, 1, 2, 3 (the table, old names beside
  new), 5.2, 9, 15 (entry 32). The exact renamed words are open item 3.
- **The 2026-10-07 ruling, decision 3 as revised: the second release kept and
  conditional, about $150 to $172.** Sections 1, 11 (step 5b), 12.4, 15
  (entry 32).
- **The 2026-10-07 ruling, decision 4 as revised: the kill dates stand.**
  Sections 11 (steps 2 and 5b; S6 unchanged) and 14.
- **The 2026-10-06 ruling, page 1 (RT-237, fatal; A1, G5).** The battery
  clause replaced by the ownership-free line, 1,546 of 3,000: sections 5.4,
  7.4, 8.2 (retitled "the channel-removal check"), 9.
- **Page 2 (RT-238; A3, G4).** The requirement above zero: sections 6.4
  item 1, 9, 10 R-6. **(RT-244; G8.)** The solver sentence's figures
  corrected: section 7.3, last paragraph.
- **Page 3 (RT-239; A5, G3).** The episode format in full, the two
  departures, the self-tests: section 4.1.
- **Page 4 (RT-240; A4, G1).** 1,800 fitting episodes; the toy re-run's
  figures quoted: sections 3, 5.2, 5.3, 7.2 items 1 and 3, 7.3 item 2, 7.4,
  9, 10 (R-3, R-4, R-10, the re-run), 13 (W15). Version 4's toy readings at
  420 (arm C 1.0051, 0.9926, 0.9974; arm M 0.4886, 0.4860, 0.5449;
  separation 0.9926) stay where they are quoted as the earlier record and are
  superseded as the registered toy figures by 1.0026, 1.0000, 1.0000;
  0.5252, 0.4793, 0.5208; separation 1.0000.
- **Pages 5 and 9 (RT-241; A10 as RT-249; G6).** The outcome table with
  three new terms; the one re-run; arm F's gate failure at step 5b as the
  fifth term; arm M's miss reported; the toy sentence corrected (the code
  freeze's finding, section 4.1): sections 3, 5.2, 7.4, 8.1, 9.
- **Page 6 (RT-242, RT-243, RT-245, RT-246; G2, G7, G9).** Sections 7.2
  item 1 (the candidates' figures; the device for the whole nomination; the
  timing), 6.4 item 1 (where the two floor forms disagree), 11 step 5a, 13
  (W16).
- **Page 7 (A10 as RT-249).** The joint seed rule: sections 3, 7.4, 8.1,
  8.2, 9.
- **Page 8 (A9 as RT-248).** The no-transplant rate reported, not a veto;
  control 4 the pairing check; the 0.56 sentence: sections 6.4 items 3 and
  5, 7.4, 7.5 item 6, 9.
- **Page 10 (A6 as RT-247).** The sentence after "entangled at these sites";
  W12's last sentences; the decoy test as R-12; its check's probe as W18:
  sections 3, 10, 13.
- **Page 11 and follow-up items 2 and 7 (A13 as RT-250).** The scope
  phrases; the table of summaries: sections 3 and 13.
- **Page 12.** Answered by the 2026-10-07 ruling: section 15, entry 30.
- **Follow-up item 1 (A7 as RT-251; A8 as RT-252; A11 as RT-253; A12 as
  RT-254).** Sections 6.1, 7.3 item 6, 13 (W11 retitled), 3 (what a no
  verdict does not mean), 10 (the toy as development evidence), 13 (W5), 9
  (the uncertainty row), 7.5 item 17.
- **Follow-up items 4, 7 and 8 (RT-255; the training exclusion).** Sections
  4.1, 4.3, 7.1.
- **Follow-up item 6 (A2 as RT-256).** Rehearsal item R-13; the withholding
  requirement rewritten; the field `arithmetic_withheld` gone: sections 3,
  6.4 item 5, 7.4, 10.
- **The 2026-10-04 ruling, rulings 1 to 7, and section 7 of the check of
  pull requests 88 and 89.** The solver's result written in; the twenty-piece
  control's code and its test; the band as a Wilson interval; the gate does
  not apply to solvers; R-4, R-5, R-6: sections 7.3 item 2 and last
  paragraph, 7.4, 7.5 item 4, 8.1, 9, 10, 13 (W16).
- **The 2026-10-03 night ruling on the check's two questions, and the thirty
  wording fixes of section 4 of the check of version 4.** Written in where
  they bear: the separation sentences (fixes 4, 13, 16, 26); record B and
  the reconciliation cited beside record A (fixes 3, 5, 14, 15, 23, 24, 29);
  the sampling band (6, 18, 20); the pinned versions written to the output
  file and the pin file named in a place the ignore list does not catch (7,
  8); the processor-impractical clause (9, 19); control 2's code test (10,
  17, 27); record B's two clauses on the solver and the result written in
  (11); the order of the piece rule in the frozen list (12); one range for
  the successor (21: section 12.4 now gives both splits beside each other);
  section 19's heading (28); the source table's "ten" rows (30: the sentence
  is rewritten). Fix 22 (a sentence in W12) is optional and not taken; fix
  25 (the sweeps re-run) is section 17.
- **The code freeze's two findings (`docs/2026-10-04-successor-code-freeze.md`,
  sections 4.1 and 4.2).** The toy's outcome sentence (section 3); the
  training recipe fixed (section 5.5; open item 5).
- **The check of the development runs (branch `check-dev-10m`).** The
  figures of sections 5.1 to 5.3, 5.6, 11 step 4, 12.1, 12.4 and 12.5; arm
  T's row-choice split in the reporting table (open item 9).
- **The spending alarm's four fixes.** Section 12.5 amended; S9; section 1.
- **The header, the source table, sections 15 (entries 30 to 34), 16, 17,
  19 (heading and intro), 20 and 21.** Rewritten or new for this version.
- **Left alone.** Sections 4.2, 4.4, 6.2, 6.3, 7.1 (but for one bullet), 7.2
  items 2 and 4 to 7, 7.3 items 1, 3, 4, 5 and 7, 12.2, 12.6, 12.7, 18, and
  the bodies of the seven questions of section 19 carry version 4's text.
  Every passage not named above is version 4's, unchanged.

---

## 21. Open items for John

Each is marked in the body where it bears. For each: the source, what the
text does meanwhile, and this session's recommendation with its confidence.
None is this session's to decide, and the registration commit should not be
made until each has John's answer or his word that it may stand open.

1. **The bar for "the repaired route holds" (section 5.6; the largest). CLOSED,
   ruled 2026-10-08 in John's words "Rule the verification bar now, keep it at
   0.5" (`docs/rulings/2026-10-08-verification-bar-ruling.md`, authorship mixed): option (a), the recommendation
   below, taken; the number is kept so that the body's cross-references still
   land. The text below is as it stood before the ruling.**
   *Source:* the 2026-10-07 ruling's addition says what "holds" means in
   figures is fixed in the amendment text before the reruns launch; the
   in-use check as coded (part A at 0.9; part B, route use, at 0.5) fails
   every toy arm C and arm M seed, before and after the fix (route use 0.22
   to 0.29 on arm C, 0.07 to 0.11 on arm M's stirred-in route), so with the
   coded bar the reruns would very likely fail and experiment C would stop at
   about $1.14 (`docs/2026-10-06-sharpness-fix-inuse-check-findings.md`,
   branch `fix-sharpness-inuse-check` at `644238e`, sections 4 and 5).
   *Meanwhile:* the text carries the coded bars and says they are not ruled.
   *Options* (the findings' own): (a) keep 0.5; (b) a bar against the free
   model's 0.000, such as 0.1; (c) part A only; (d) redesign arm C and arm
   M's stirred-in half so the built route is the only route. *Recommendation:
   (a), keep 0.5, and let the stop condition do what it was ruled for.* The
   anchors exist to be systems whose ownership route is known; a route that
   carries a quarter of the right answers is not that, and reading it as
   "entangled by construction" would be the inflation the project's standing
   rules forbid. If the reruns fail at 0.5, the honest result is that the
   built arms as designed are not references, which is a finding about the
   design and costs $1.14; (d) is then the route to a real reference and
   needs its own toy work and ruling. Confidence moderate; (b) is the closest
   alternative and detects only a route switched off.
2. **The 2026-10-06 ruling on the flat-models packet has no rulings file.**
   *Source:* the sharpness and tripwire method notes state the ruling
   (option 1(b) plus option 4; page 2's four fixes); no `docs/rulings` file
   on any branch records John's words; the repair is named in decision 3 of
   2026-10-07, which is ruled. *Meanwhile:* the text treats the repair as
   ruled through decision 3 and the alarm fixes as reported ruled.
   *Recommendation:* record the 2026-10-06 ruling in a dated rulings file
   with John's words, authorship mixed, before the registration commit, so
   that section 5.6 and section 12.5 cite a ruling and not a method note.
   Confidence high.
3. **The exact words of the renamed outcome terms (section 3).** *Source:*
   decision 3 renames "metric validated" and says "the fifth term
   accordingly"; it says nothing of R2, the three terms of page 5 or the
   words for them. *Meanwhile:* this session's drafting, with version 4's
   names beside each. *Recommendation:* adopt the table as drafted, or give
   the words; "instrument not validated" for the eighth term is the weakest
   of the drafted ones because "validated" is the word being retired, and
   "instrument returned no reading on the separable mechanism" is the
   alternative. Confidence moderate on the drafting, high that the words are
   John's to set.
4. **Whether the scope phrases travel with the renamed terms (section 3).**
   *Source:* page 11 and follow-up items 2 and 7 ruled the phrases for the
   old names; decision 3 renamed the terms the next day without mentioning
   them. *Meanwhile:* kept. *Recommendation:* keep them; the renamed term
   still invites the reading the phrase guards against ("on these
   constructed systems, for this intervention procedure" is still true and
   still needed). Confidence moderate.
5. **The training recipe (section 5.5).** *Source:* the code freeze, section
   4.2: no ruling sets it; the trainer's defaults are a session's call.
   *Meanwhile:* written as registered text from the frozen trainer's
   defaults, which the development runs ran. *Recommendation:* confirm it as
   written; the development runs show it runs end to end on every arm, and
   changing it now would make the reruns of step 4b test a recipe no run has
   used. The one thing to weigh: arm T's lookup damage after the
   learning-rate peak (section 5.1), which the recipe may cause at the
   registered size too. Confidence high on confirming; low on whether the
   recipe is the best one.
6. **Arm T's rerun failing (section 5.6).** *Source:* the stop condition
   names the stirred-in and half-and-half models. *Meanwhile:* the text
   treats arm T the same way and says so. *Recommendation:* confirm; an arm T
   whose hand-set route is not in use at 10 million is as much a failed
   reference as the others. Confidence high.
7. **The fitter's iteration limit at 1,800 episodes, and the frozen code's
   fitting count (section 7.2, item 1).** *Source:* the page 4 re-run and its
   check: 471 iteration-limit warnings on arm M at 1,800 against 27 at 420;
   the frozen procedure still fits on 420 of 600. *Meanwhile:* the text
   registers 1,800 of 1,980 and says the code change is owed.
   *Recommendation:* raise the limit (for example to 10,000) in the frozen
   code with the 1,980 change, re-run the page 4 pass under it, and quote
   those figures; a read that stopped short of its optimum is a weaker
   nomination. Confidence moderate; the alternative is to register 3,000 and
   carry the warning count in the reporting table.
8. **A ruled test of a differently coded decoy (W18).** *Source:* the check
   of the decoy test, probe 3: readings 0.23 to 0.29 at 8 directions on a
   model whose true reading is 0, outside the registered nomination.
   *Meanwhile:* carried as W18. *Recommendation:* run it as a ruled test
   before the registration commit (about an hour on the laptop, $0, method
   first, checked), since it is the sharpest cheap test of what a high
   reading on arm C can mean; if that is not possible before 2026-10-18,
   register with W18 named and run it before step 5b. Confidence moderate.
9. **Three reporting changes from the development runs' check, none ruled
   (sections 5.1, 7.5, 12.4).** Arm T's row-choice split reported beside its
   gate; arm M's per-step copy stored once on the model (a change to frozen
   code that computes nothing differently); `summarise` on fewer than three
   seeds saying "gate not decidable on one seed" rather than "failed its
   gate". *Meanwhile:* the first is in the reporting table; the other two are
   not done. *Recommendation:* yes to the first and third (reporting only);
   the second only if John wants arm M's three registered runs cheaper, and
   then confirmed on the first card it runs on. Confidence high.
10. **The registered commit of the frozen code, and the merges.** *Source:*
    the frozen code is changed on three unmerged branches (the training
    exclusion; the sharpness fix and in-use check; the alarm fixes), and
    every ruling and review this text cites from a branch (section 16) is
    off the main line. *Meanwhile:* cited by branch and commit.
    *Recommendation:* merge the checked branches (the training exclusion,
    the alarm fixes, the page 4 re-run and its check, the decoy test and its
    check, the development-runs check, the rulings and reviews) before the
    registration commit; have the sharpness branch checked, then merged;
    then name the resulting main-line commit of `experiments/08-successor-degree/`
    in section 7.4 as the registered code. Confidence high.
11. **The launcher (section 5).** *Source:* RT-228 named the parent
    launcher; the derived `launch_successor.sh` is what ran. *Meanwhile:*
    the derived launcher is named with the parent. *Recommendation:*
    confirm. Confidence high.
12. **The red-team ledger's rows.** *Source:* the rulings of 2026-10-06
    assign RT-247 to RT-256 and say the rows for RT-237 onward are owed; the
    ledger on the main line carries no row for RT-230 onward (section 17,
    failure 4). *Meanwhile:* this text uses the numbers as the ruling assigns
    them. *Recommendation:* write the rows before the registration commit,
    each with "the claim was checked" or "the argument was accepted" as the
    closure rule asks. Confidence high.

---

## What this version does not do

It edits nothing: not version 4, not any ruling, registered text or protocol
text, not the known-failure list, the ledger or the frozen code, and not the
findings of any run. It issues no go, releases no money, launches nothing,
trains nothing and rents nothing. It merges no branch. It does not rule any
of the twelve open items of section 21: each is John's. It is not the
registration: that is John's commit, after this text is checked by a session
that did not write it, after the closure check of RT-237 runs on it, and
after every record it cites is on the main line. **It is the text meant for
that commit, with everything ruled by 2026-10-07 written in.**

---

## Changes after the check (2026-10-08)

The check by a session that wrote none of this text
(`docs/reviews/2026-10-08-successor-v5-check-claude-code.md`, pull request
130) found every ruling of 2026-10-06 and 2026-10-07 carried in substance and
every figure matching its file, and five must-fix items. All five are applied
above, in place, by a session that wrote neither the text nor the check, at
John's word "Merge both and apply the version 5 fixes":

1. Version 4's closing section, left at the end of the file after this
   version's own and joined to it without a line break, is removed (the
   check's finding 1).
2. The scope rule of section 3 now names "instrument not validated" too, so
   the eighth term keeps the scope phrase the 2026-10-06 ruling's follow-up
   item 2 gave it (finding 3).
3. The two registered sentences that still named the fifth term by its old
   words (section 3; section 11, step 8) now use its renamed words
   (finding 8). Section 15's record of the 2026-10-03 ruling keeps the old
   words as history.
4. The verification-bar ruling of 2026-10-08 is written in: section 5.6's
   "are not ruled" is replaced by the ruling and its citation, the options
   marked as taken or declined, open item 1 closed in section 21, and the
   pointers in sections 7.4, 9, 11 (step 3), 13 (W17) and 17 changed to
   match; section 15 gains entry 35 and the source table a row (finding 12).
5. The December-result restatement rulings of 2026-10-08 are written in:
   stop S4b and section 5.6 report an early stop in the ruled sentence, "the
   built arms as designed are not references; the measure was not reached",
   as a registered ending of experiment C; section 15 gains entry 36 and the
   source table a row (finding 13). Section 3's opening cites the roadmap's
   dated head note (the check's should-fix B.2).

No figure, bar, term meaning or stop changed. The other should-fix items
(the check's findings 4 to 7) and open items 2 to 12 stand for the next
edit and for John. This edit is owed a short re-check that the five landed
and nothing else moved.
