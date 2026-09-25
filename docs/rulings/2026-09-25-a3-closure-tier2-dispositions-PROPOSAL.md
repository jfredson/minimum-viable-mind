# PROPOSAL — draft dispositions for the two outside reviews of the A3 closure text

*Drafted 2026-09-25 (Pacific) by a Claude Code session in its own worktree
(`worktree-a3-tier2-dispositions`), at John's request: "Draft dispositions …
one line per item in the ledger form, with a recommendation and confidence on
each; do not rule." **Nothing here is ruled.** Every line is a recommendation
for John. When he rules, the lines he accepts are copied into the experiment's
red team ledger (`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`)
by the session that lands the ruling. This session did not edit the ledger, the
closure text, any ruling file or any protocol text.*

*This is a proposal on its way to John, so under the pairing rule
(`docs/outside-review-protocol.md`, "The pairing rule") it counts as binding
text and is owed a check by a different session. That check has not been run.*

## What is being disposed of

**The target.** Version 4 of the closure text for Amendment A3 (A3 is the
experiment's third registered design change; its "closure text" is the dated
block that will close it out, appended to `amendment-a3.md` once ruled). The
draft is `docs/a3-closure-text-draft-2026-09-21-v4.md`. This is Gate A, the
review a text gets before it becomes registered, and this is its tier 2: outside
models from other labs, run by John through their apps.

**The two responses**, filed verbatim by John on 2026-09-25 and committed
to main in commit `c89a3ef` ("File the two A3 closure tier 2 reviewer
responses…"), which this pull request's branch starts from; this pull request
does not change them:

- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-gemini.md`
  — Gemini 3.1 Pro, six findings, G1 to G6.
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-chatgpt.md`
  — ChatGPT, fifteen findings, A1 to A15.

**Headline.** Neither reviewer found anything fatal (a fatal finding would block
registration outright). Between them they raise fifteen findings marked serious (four from Gemini, eleven from ChatGPT, counted from the severity column of each file's tables), which
the closure rule says must be either fixed or carried as an open item that John
has ruled on (`docs/outside-review-protocol.md`, "The closure rule"). **The two
reviewers, who never saw each other's answer, independently found the same two
defects:** the text never says whether hard kill criterion K5 fired, and it
says the two localization instruments "never converged" when one of them was
never run. Those two are the strongest items here. My recommendation overall:
**accept almost everything as a wording change, write version 5, and send
version 5 to a tier 1 closure check. No new experiment and no new spending is
implied by any item.**

## How to read the labels

- **MEASURED** means *this session* ran a command against the committed files
  and the output is given. **ARGUED** means reasoning a reader can dispute.
  Under the protocol, every tier 2 finding is ARGUED as filed, because outside
  models see documents, not a checkout (`docs/outside-review-protocol.md`, "Two
  tiers"). Both reviewers labelled some of their own findings MEASURED; that
  label is theirs and is not relied on here. Where this session checked a
  reviewer's claim, the line says so and gives the check.
- **Confidence** is my confidence that the recommendation is the right ruling:
  high, medium, or low.
- **Ruling words** follow the ledger's form: accept, accept with change,
  decline, carry open, and accept as credit (a reviewer confirming something
  already right).

## The checks this session ran

All were run from the root of the repository, in this worktree, on 2026-09-25.
`E/` is short for `experiments/06-mvm-0a-constructed-self-index/`.

| # | Command (abridged to what it tests) | Output | What it shows |
|---|---|---|---|
| C1 | `grep -c "K5" docs/a3-closure-text-draft-2026-09-21-v4.md` and the same on `-v3.md` | `0` and `0` | Neither version 3 nor version 4 names K5. |
| C2 | `grep -n "RT-164" E/red_team_ledger.md` | line 756: "… ACCEPT (drafted) … Done in version 3." | The ledger records the K5 fix as done in version 3. C1 shows it was not. |
| C3 | `grep -n "K5" E/reviews/2026-09-21-a3-closure-v4-closure-check-claude-worktree.md E/reviews/2026-09-21-a3-closure-v4-fix-verification-claude-worktree.md` | nothing | Neither of the two independent checks of version 4 looked at K5. |
| C4 | `grep -n "\*\*K5" E/amendment-a3.md` | line 265: "**K5.** Probe-patching convergence fails on all three seeds: *not testable (localization)*, reported as such; no further seeds." | K5's registered wording. |
| C5 | `grep -n "converged" docs/a3-closure-text-draft-2026-09-21-v4.md` | line 150: "Because the two instruments never converged on" | The sentence both reviewers object to. |
| C6 | `grep -n "F17" E/red-team-a4.md` | line 137: "…were never applied to the input-channel lesion on any seed…" | The cited record says "the input-channel lesion", not "any lesion". |
| C7 | `grep -n "Arm 1\|Arm 2\|270" E/powered-position-sweep-findings.md` | line 13 "270 testable tests"; line 31 "Arm 1 — the model's own marker word"; line 47 "Arm 2 — the register index" | Only one of the two arms reads the marker word. |
| C8 | `grep -n "46\.2\|227\.6" E/compute-ledger.md` | line 293: "A3 cumulative is ~$44.3 -> ~$46.2 of $100 … programme running total is ~$227.6 / $400" | The ledger's corrected money figures; version 4's money paragraph (line 232) still reads ~$44.3 and ~$225.7. |
| C9 | `grep -n "2026-10-11" docs/rulings/2026-09-20-december-result-roadmap.md` | line 17 "Registration commit target 2026-10-11"; line 95 "registration commit target of 2026-10-11 in item 1 was pacing, so it goes with the calendar" | The ruling version 4 cites withdraws the date version 4 quotes. |
| C10 | `sed -n '84,92p;110,112p' E/ceiling-measurement-findings.md` | line 85 "Any control that is fully determined by the visible episode and does not require ownership has an ownership-blind ceiling of 1.0 by construction"; line 110 "The state battery's ceiling is 0.0676"; line 112 "…specific to a control designed to be ownership-free" | The impossibility claim carries a restriction version 4 drops; the state battery is contrasted with the ownership-free control, not called ownership-free. |
| C11 | `grep -n "^| RT-125" E/red_team_ledger.md` | line 652: a purely relational encoding "would produce the own-index pattern and this exact null together" … "ACCEPT, CARRIED OPEN" | The relational route is on the record as open. |
| C12 | `sed -n '28,48p' docs/rulings/2026-09-21-followup-runs-and-blind-arm.md` | "The arm was discharged on 2026-09-16 and is not re-run … The requirement the arm serves … is carried into the successor's rehearsal" | The arm was cleared administratively, and the sensitivity requirement is still unmet. |
| C13 | `grep -n -i "patching" docs/rulings/2026-09-20-december-result-roadmap.md` and `grep -n "authoris" docs/rulings/2026-09-21-followup-runs-and-blind-arm.md` | Dec. ruling lines 18–23: "patching is not built for the Amendment A3 design"; follow-up ruling line 19: "No further work on that position is authorised." | Both decisions exist; version 4's open-items list does not carry either. |
| C14 | `grep -n -i "every write-up\|same-act\|experience" E/pre-registration.md`, then `grep -c -i "same act\|same-act\|experience" docs/a3-closure-text-draft-2026-09-21-v4.md` | pre-registration line 84 "…result here closes that gap, and every write-up must say so"; line 529 "the same-act clause of the floor claim … is not"; version 4: `0` | The registration requires every write-up to state the same-act limit; version 4 never mentions it. |
| C15 | `grep -n "0\.0018\|0\.0002\|0\.0769" E/seeds-endpoint-findings.md` | lines 42–44: +0.0018, +0.0002, **+0.0769** | The state-battery drops on the three seeds. |
| C16 | `grep -n -i "quadrupl" E/control-learnability-pilot-findings.md` | line 13–14: "its per-row gradient weight quadrupled" | "Quadrupled" is per-row gradient weight, in the findings' own words. |
| C17 | `grep -n -i "attack" E/ceiling-defect-2026-09-17.md` | line 16: "The control battery's ceiling has never been attacked" | Version 4's "never attacked" is the defect file's own claim, true as of 2026-09-17. |
| C18 | `grep -l "The measurement rehearsal, required before any Gate A" E/reviews/packets/2026-09-21-a3-closure-tier2-*` | no files | The tier 2 packets did not carry the protocol's rehearsal section, as ChatGPT's A5 says. |
| C19 | `grep -rhoE "RT-[0-9]{3}" --include='*.md' . \| sort -t- -k2 -n -u \| tail -1` and `grep -o "^\| RT-[0-9]*" E/red_team_ledger.md \| tail -1` | `RT-203` and `\| RT-171` | Finding numbers above the ledger's last row are already used in review files. |

## Draft dispositions, one line per item

Order: the items both reviewers raised first, then Gemini's, then ChatGPT's,
then matters about the filing itself. Every "accept" below means: change the
wording in version 5. None means run anything.

| Item | Reviewer(s) | Finding, in plain words | Severity as filed | Recommended ruling | Confidence | Reason / what closes it |
|---|---|---|---|---|---|---|
| 1 | Gemini G5, ChatGPT A7 | The text uses hard kill K5's exact outcome, *not testable (localization)*, without ever saying whether K5 fired. (A hard kill is a registered stop condition that ends a line of work with a named consequence.) | serious (both) | **ACCEPT WITH CHANGE.** Version 5 names K5 and says it was **not reached**: its test is that probe and patching fail to agree on all three seeds, patching was never built, so the test was never run. The *not testable (localization)* term then rests on §3.2 (the amendment section saying nothing counts as localized until both instruments agree), and A3 closes under the loss condition, with no further A3 seeds. Also annotate, beside RT-164's line and without editing it, that "Done in version 3" was not so. | high that K5 must be named; **medium** on "not reached" | MEASURED by C1–C4. Both reviewers found this independently, and neither check of version 4 caught it (C3), so the ledger now carries a closure line the text contradicts. Judgment call, not standard practice. **Strongest alternative:** rule that K5 *fired*, reading "convergence fails" as covering an instrument that was never built. That gives the "no further seeds" consequence straight from the registered kill list. It also records as a failure something that was never measured, which is the over-reading the rest of this closure works to avoid. Either way, John states it in so many words, because it is an interpretation of registered text. |
| 2 | Gemini G4 and G6, ChatGPT A7 (second half) | "Because the two instruments never converged" reads as though both ran and disagreed. Causal patching (swapping internal activity between runs to test cause) never ran. | serious (both) | **ACCEPT WITH CHANGE.** Replace with Gemini's wording, near-verbatim: "Because causal patching was never run, agreement between probe and patching could not be tested and no L1 subspace was ever localized; so the registered uncarvable signature H_diffuse was never reachable either…" | high | MEASURED by C5, against the same paragraph's own sentence that patching "was never run and has no code for this design" (version 4, lines 147–150). Standard practice: don't describe an unrun test as a failed one. Alternative: keep "never converged" and add "because one instrument never ran". Weaker, because the first clause still reads as a result. |
| 3 | Gemini G1 | Every added citation and number reproduces against the records. | worth-noting (credit) | **ACCEPT AS CREDIT, IN PART.** Credit for the citations and the endpoint numbers. Not for the money: G1 credits "~$46.2/$227.6", which are in the *note beside* the text. The block itself still says ~$44.3 and ~$225.7 (see item 12). | high | MEASURED by C8. Filed as independent confirmation, no new number. |
| 4 | Gemini G2 | "Not testable" is the registered word, quoted correctly from the pre-registration's loss conditions. | worth-noting (credit) | **ACCEPT AS CREDIT**, read with item 13, which narrows what the loss condition is said to prove. | high | ChatGPT A1 confirms the same quotation. |
| 5 | Gemini G3 | The text says the validity gates (checks that a lesion did not simply break the model) were "never applied to any lesion on any seed". The cited record says "the input-channel lesion". | serious | **ACCEPT WITH CHANGE.** "…never applied to the input-channel lesion, the only lesion A3 ran, on any seed (`red-team-a4.md`, F17)." | high | MEASURED by C6. The claim is true in effect, since no other lesion was run, but the sentence must say what the record says. Severity as filed is high for a wording fix. I'd rule it worth-noting in substance, but it is accepted either way. |
| 6 | ChatGPT A1 | The central numbers hold. Side note: "quadrupled weight" should say *per-row gradient* weight. | worth-noting | **ACCEPT AS CREDIT; accept the side note as a wording change.** | high | MEASURED by C15 and C16. The findings file uses exactly "per-row gradient weight quadrupled" (C16). |
| 7 | ChatGPT A2 | "Found it nowhere on either of its two arms across 270 tests" merges two targets: 135 tests read the marker word, 135 read the register index. "Nowhere" also needs "at the discovery positions", because the positive-control positions did detect. | serious | **ACCEPT WITH CHANGE**, using ChatGPT's replacement sentence. | high | MEASURED by C7. The findings file names the two arms separately. |
| 8 | ChatGPT A3 | The money paragraph keeps figures its own note says are superseded. | serious | **ACCEPT.** Version 5 gives the ledger's figures with an "as of" date: about $46.2 of A3's $100 stop and about $227.6 of the programme's $400 ceiling (`E/compute-ledger.md`, line 293), including the $1.904 from the two refused follow-up machines. The note beside version 4 then has nothing left to correct. | high | MEASURED by C8. Registered text should not need a correction note on the day it lands. The rented-slice row of 2026-09-21 adds about $0.02 and says it moves neither figure (`E/compute-ledger.md`, line 74). Re-read the ledger on the day version 5 lands, in case anything has been spent since. |
| 9 | ChatGPT A4 | The successor's "registration commit target 2026-10-11" was withdrawn as pacing by the very ruling cited. | serious | **ACCEPT.** Drop the 2026-10-11 target. Keep the two kill dates (register by 2026-10-18; launch the registered runs by 2026-11-01) and cite the ruling's annotation. | high | MEASURED by C9. |
| 10 | ChatGPT A5 | Some records were not in the packet: the protocol's rehearsal section, the original blind-run findings, the pilot's pre-statement, and the reviewer-owned closure check (which does not exist yet). | worth-noting (packet limit) | **ACCEPT AS RECORD; no text change.** The rehearsal-section gap is real. Note it for the next packet: the brief should carry every protocol section the text cites. | high | MEASURED for the rehearsal section by C18. The reviewer states these are limits of the packet, not evidence against the text. The missing closure check is item 15. |
| 11 | ChatGPT A6 | The ceiling measurement proves the *registered comparison* can't be computed. It does not prove that no ownership-free, state-requiring control can ever be built, and version 4 drops the restriction the findings file attaches. Sub-point: the findings file is said to call the state battery ownership-free while giving it a ceiling of 0.0676. | serious | **ACCEPT WITH CHANGE** on the main point: restore the restriction, "any control fully determined by the visible episode and not requiring ownership", and adopt ChatGPT's successor sentence (a successor must show both its control ceiling and a comparison measure that can be computed). **DECLINE the sub-point.** | medium-high on the main point; high on declining the sub-point | Main point MEASURED by C10: line 85 carries the restriction, and version 4 lines 76–78 state the incompatibility without it. Sub-point MEASURED against the reviewer by C10: line 110–112 contrasts the state battery with "a control designed to be ownership-free" and does not call it ownership-free. **Strongest alternative on the main point:** leave it, since John's ruling applies the loss condition and the reader can follow the citation. I'd still recommend the change, because this sentence is the one most likely to be quoted upstream. |
| 12 | ChatGPT A8 | "Excluded the exclusion confound" claims more than one classifier's null at one position shows. A relational encoding the probe would miss remains open. | serious | **ACCEPT WITH CHANGE, narrower than proposed:** keep the ruled phrase and bound it, e.g. "excluded the exclusion confound in the form proposed, a four-way rank of the other agent that this probe could decode", then the existing relational-route sentence. | medium | The route is carried open (C11). But "the exclusion confound is excluded" is the wording of the Gate B ruling of 2026-09-21 (the heading of the STATUS.md entry of that date), and ChatGPT's replacement drops it. Qualifying the phrase narrows the ruling without contradicting it. **Strongest alternative:** ChatGPT's full replacement ("did not support the proposed explanation…"), which is cleaner, but in effect re-rules a Gate B ruling inside a closure text. If John wants that, it should be its own ruling line. |
| 13 | ChatGPT A9 | The six fatal version 2 defects are visibly repaired, but agreeing with a wording is not verifying it. The reviewer-owned check is still owed. | worth-noting | **ACCEPT AS CREDIT**, and see item 15. | high | Correct statement of the closure rule. |
| 14 | ChatGPT A10 | "The blind arm is the measurement that would establish it … discharged" reads as if sensitivity was shown. It wasn't. The arm was cleared administratively, and the requirement carries on. | serious | **ACCEPT WITH CHANGE**, using ChatGPT's replacement: discharged so it doesn't block closure; that doesn't establish recovery on this design; the requirement carries into the successor's rehearsal. | high | MEASURED by C12. The ruling says exactly this. The reviewer's further point, that running a blind arm alone wouldn't establish sensitivity without a known-present target, is ARGUED and sound. |
| 15 | ChatGPT A11 | The open-items list gives unfinished jobs, not the decisions about them. Patching is ruled *not* to be built for A3, and no further work on the other agent's revision-value position is authorised. | serious | **ACCEPT.** Add ChatGPT's paragraph, citing both rulings by item. | high | MEASURED by C13. Without it, a later session could read "causal patching, unwritten and unrun" as an A3 task. |
| 16 | ChatGPT A12 | The headline "what the experiment could measure without it was measured on three seeds" claims exhaustion, while the body lists four unrun instruments. | serious | **ACCEPT WITH CHANGE:** ChatGPT's headline, which states the outcome (not testable: the registered comparison was undefined for every possible model) and the result (removing the ownership input lowered primary-battery accuracy on all three seeds). | medium-high | ARGUED. Version 4 lines 59–61 against its own lines 97–154. **Strongest alternative:** keep the headline and add "some of" plus the unrun instruments by name. It's shorter to change, but still leads with a completeness claim. |
| 17 | ChatGPT A13 | "Above zero" on the gradient can be read as a measured degree, or as evidence about experience. The registration requires every write-up to state that the same-act clause (binding that specifies its own center in the same act) is not shown, and version 4 never does. | serious | **ACCEPT.** Add ChatGPT's two sentences to the gradient paragraph and use its public sentence. | **high**; of the ChatGPT items, this is the one that is a registered obligation rather than an improvement | MEASURED by C14: the pre-registration says "every write-up must say so" (line 84), and version 4 contains the phrase zero times. |
| 18 | ChatGPT A14 | "These probes did not localize this target … one episode in eleven" lumps four reads on two targets together. The one-in-eleven figure belongs only to the fitted register-index read and says nothing about the unrun fitted marker-word read. | serious | **ACCEPT WITH CHANGE**, using ChatGPT's replacement. Keep the required citation of the correction file. | high | ARGUED from version 4 lines 112–165, plus the scope of `E/fitted-position-sweep-findings-CORRECTION-2026-09-20.md`, which concerns the fitted register-index read (by its own name, and as version 4 introduces it at lines 113–117). This narrows the earlier ruling that the figure is heuristic (ledger, program review, Astra A11); it does not contradict it. |
| 19 | ChatGPT A15 | Six small wording changes to head off over-reading. | worth-noting | **ACCEPT four, ACCEPT ONE WITH CHANGE, HOLD ONE FOR A CHECK.** Accept: (a) validity-gate bin "not evaluated"; (c) give the state drops 0.0769 against +0.0018 and +0.0002; (d) "an accuracy margin of 0.000484, equivalent to 1.94 of 4,000 episodes"; (f) "ownership-channel dependence was established; recovery of an acquired internal representation was not". Accept with change: (b) "never attacked" becomes "had not been attacked before registration" (C17), with no claim about what the later measurement "invalidated". Hold: (e), the refit's folds and permutation draws "also differed", is not checked by this session. Adopt it only if the version 5 writer shows it from `E/standardised-refit-findings.md`. | medium overall; high on (c) and (d) | (c) MEASURED by C15. (d) is the ledger's RT-128 figure, which ChatGPT A1 recomputes. (e) is unverified. The refit findings' mention of folds (line 102–104) does not by itself show different folds. |
| 20 | Filing — ChatGPT header | The ChatGPT file's header says "ChatGPT 6 Astra Medium". Its body says "Reviewer: Codex; exact model version and app mode were not exposed". | — | **FOR JOHN: annotate beside the file (not in it)** which model and mode actually ran. | high that it needs annotating | MEASURED by reading lines 1 and 7 of the filed response. The protocol requires model, version and mode on record, and the file disagrees with itself. The file is not edited, per the filing rule. |
| 21 | Filing — numbering | If items are adopted, they need finding numbers. The ledger's last row is RT-171, but review files already use up to RT-203. | — | **FOR JOHN:** number adopted items from RT-204, and ask a later session to reconcile why RT-172 to RT-203 are used outside the ledger. | medium | MEASURED by C19. This session did not check what RT-172 to RT-203 refer to. The protocol text names RT-172 as a successor-proposal finding. |
| 22 | Process — what happens next | No fatal findings from either tier 2 reviewer. | — | **FOR JOHN:** version 5 is written by a session that has not drafted these dispositions, from items 1–2, 5–9, 11, 12 and 14–19 as ruled. Then a tier 1 reviewer, not the version 5 writer, runs the closure rule's reviewer-owned check on version 5 and files it. The registration commit follows only then. No second tier 2 round, because nothing fatal came back. | medium-high | The closure rule (`docs/outside-review-protocol.md`, "The closure rule") requires the reviewer-owned check at every Gate A, with or without a fatal finding. The weekend roadmap names a second tier 1 pass only for the fatal case (`docs/weekend-roadmap-2026-09-24.md`, line 234). **Strongest alternative:** send version 5 back to both outside models. Safer, costs John about two more hours (the roadmap's own estimate, line 223), and isn't required by any rule. |

## Tally

Of the twenty-one reviewer findings (G1 to G6, A1 to A15), counted one by one
even where two share a line: five are credit (G1 in part, G2, A1, A9, and A5
as a record); fifteen are accept or accept with change (G3 to G6, A2 to A4,
A7, A8, A10 to A15); one is split (A6: main point
accepted, sub-point declined); and one sub-item is held for a check (A15e).
Nothing is recommended for decline in whole. Three further lines (20–22) are
about the filing and the next step. They are not reviewer findings.

## What this session did not do

It did not rule, edit the closure text, the ledger, any ruling file or any
protocol text, launch anything, or spend anything. It did not run the tier 1
closure check owed on version 5, which belongs to a different session. It did
not verify ChatGPT's A15(e), or what RT-172 to RT-203 are.
