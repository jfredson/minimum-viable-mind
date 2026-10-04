# Check of the two ruling packets of 2026-10-03 and the records of John's two rulings

*Written 2026-10-03 (Pacific) by a Claude Code checking session, on branch
`w2a-job3-rulings-check`, cut from the main line at `7c403b0`. Written under
the workspace plain-language rule. Nothing was rented, trained or spent: $0.
This file edits no ruling, packet, proposal, registered text or protocol text.*

**What this session opened.** Committed files only: the two packets and two
rulings files named below; the review of proposal version 3 and its scripts
folder; proposal version 3; the controls re-run's findings, method and
outputs; the December-result roadmap; the ruling of 2026-09-21 on review
verification and staged spending; the ruling of 2026-09-26 on the review of
version 2; the Weekend 1 handoff; the compute ledger; the committed gate
counts. **What it did not open:** any chat or transcript of the session that
wrote the packets and the records. So two things the packets say about
themselves cannot be checked here: that one session wrote the review, both
packets and both records, and that a TimeAssembler step for the re-run
"already exists".

**How it was done.** The first packet has sixteen pages. A helper agent
working for this session, with no view of this session's conclusions, compared
every number, date, commit, quotation and factual claim in it with the place
it cites, 161 rows in all, and reported each with the source's line and exact
words. This session then opened the source itself for every row that was not
a clean match. The second packet (three pages) this session compared itself.
Findings are labelled **MEASURED** (the source line is named and was opened)
or **ARGUED**.

The four targets:

- the first packet, `docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md`,
  and its record, `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`;
- the second packet, `docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md`,
  and its record, `docs/rulings/2026-10-03-controls-rerun-rulings.md`.

"The review" is
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`.
"The proposal" is `docs/successor-experiment-proposal-2026-09-26-v3.md`.

## 1. The short version

- **No number in either packet is wrong.** Of 161 claims in the first packet,
  142 match their source exactly, 15 match in part, 1 does not match and 3
  could not be found in a committed file. Every figure in page 1's table, the
  appendix, and pages 2, 3, 5, 14 and 16 matches. The second packet's figures
  all match the re-run's outputs and the review.
- **Nothing found changes a recommendation.** No page recommends something
  its cited record contradicts.
- **Six places where a page says a little more, or a little less, than its
  source.** Section 2. The two worth John's eye: the first packet twice states
  a higher confidence than the proposal it is summarising without saying so
  (pages 5 and 14), and page 10 describes a $97.04 loss in words the ledger
  and the proposal do not support.
- **Both records say what the packets put, with small additions that are all
  drawn from the packet's own page.** Section 4.
- **One item should go back to John for a one-word confirmation:** whether the
  fifth outcome, "metric validated, degree not read", counts as satisfactory.
  The record is honest about how it got there, and the note it added to the
  December-result roadmap is not. Section 5.
- **The three dated notes are accurate**, with that one exception. Section 6.

## 2. The first packet against the places it cites

Every row not listed here was a clean match. Line numbers are in the file
named.

| # | Page | What the packet says | What the source says | Weight |
|---|---|---|---|---|
| 1 | 14, and the index | Confidence in accepting fifty timed steps: "moderate to high" | The proposal, decision 17, line 2470: "Confidence: moderate. Judgment call." | **MEASURED. Small, but it leans one way.** The page presents itself as agreeing with the proposal and gives a higher confidence than the proposal does, without saying it has raised it |
| 2 | 5, and the index | Confidence that the entangled model is entangled by its build: "moderate to high" | The proposal, decision 3, line 2367: "Confidence: moderate, raised by the toy result of section 5.2" | **MEASURED.** Same kind as row 1, and softer: "moderate, raised" can fairly be read as the packet's phrase |
| 3 | 10 | "The programme's largest single loss, $97.04 on the run of 2026-08-09/10, was a machine that kept running after its work was done." | The compute ledger, lines 384 to 391: $97.04 is the whole bill for a 29.5-hour run; the machine ran "~5.4h and ~$17.82 past the backstop". The proposal, decision 13, lines 2432 to 2434: an earlier account of what this failure cost "merged two events", was corrected by an earlier review's finding (RT-186, two failures merged into one), "and the sentence is not repeated here" | **MEASURED. The figure is right; the sentence is not what the record shows.** The overrun was about $17.82. The proposal left this sentence out on purpose and the packet brought a version of it back as the reason for its recommendation. The recommendation (register the shutdown rule) stands without it |
| 4 | 11 | The proposal's stated expectation is that the free model returning no verdict "is the most likely result at full size" | The proposal, lines 320 to 322: the most likely outcome is that the free model "returns no verdict, or fails its gate" | **MEASURED.** Half the sentence. Failing the gate is a different registered ending (outcome R3) from the one page 11 is about, so page 11's "the words the December result is most likely to be reported in" is a little stronger than its source |
| 5 | 11 | "The review reached the same view (its section on over-reading)" | The review, lines 429 to 431, in its "No verdict" part: the fifth term "is the honest one". Its over-reading part (lines 433 to 440) warns how that term may be misread | **MEASURED.** Right view, wrong section, and the review endorses the fifth term only, not the other two parts of the recommendation |
| 6 | 1, option (b) | The entangled model would be read at 8, 8 and 4 directions | The review, lines 206 to 209: "rank 4 or 8" on seeds 0 and 2 | **MEASURED.** The packet's appendix says this choice is its own reading and labels it ARGUED, and page 1 says the readings are not committed results. Fairly flagged. **The re-run then showed the reading was wrong on seed 1**, where the rule moved to a different layer and position set (8 directions, reading 0.9926, not 0.9975); the re-run's findings say so |
| 7 | 2 | Item 5 of the 2026-09-21 ruling makes an unexercised quantity a fatal finding "at the registration review" | That ruling, line 39: "A pre-stated quantity the rehearsal never exercised is a fatal finding on its own." No mention of which review | **MEASURED.** The added words are the review's reading of item 5, not item 5 |
| 8 | 4 | The separable model's "training reproduces exactly from code and seed (proposal, section 5.1)" | Section 5.1, lines 566 to 568, puts "exactly" on the gate figures. "Reproduces exactly" for the training is in sections 7.3 and 10 | **MEASURED.** True; cited to the wrong section |
| 9 | 3 | Finding RT-232 is labelled MEASURED; its fix is "state the accuracy as a count of episodes, name the device" | The review, line 253: "MEASURED and ARGUED"; lines 268 to 271: the fix also names the number format and says the figure on that device is the registered one | **MEASURED.** The page says "accept all four as the review states them", so the review's fuller wording is what was agreed. Version 4 should follow the review's text, not the page's shortening |
| 10 | 1 | The entangled model reads "between 0.99 and 1.005" | The review, line 184: 0.9897 to 1.0051 | **MEASURED.** Rounding. The rulings file gives the exact figures |
| 11 | 7 | "The compute ledger stays where it is" | Not in the proposal's decision 8 | **MEASURED.** An addition, and the page says so ("one thing to settle with it") |
| 12 | 15 | "The never-sleep refusal in the launcher is what stands in front of it"; option (a) "is code work and one more rented test" | Neither is in the proposal's decision 18 or its weakness W9. The refusal is real: the launcher script, line 280 | **MEASURED.** Additions, true as far as checked |

**Whether each page states its options fairly** (ARGUED). Pages 4 to 10, 12 to
14 and 16 give the proposal's own recommendation and its own alternative, each
checked against section 15 of the proposal; none drops an alternative the
proposal offers, and page 9 says "none worth taking" where the proposal offers
none. Page 1 gives the review's three options and adds a fourth of its own,
labelled as not in the review. Page 2 says there is no alternative the
protocol allows, which is what item 5 of the 2026-09-21 ruling says. Page 11
is the fullest page and puts the strongest alternative plainly. Page 15 puts
both options and a caution against its own recommendation. **No page stacks
its options.** The one page whose case is helped by something the record does
not show is page 10 (row 3).

**One proposal decision the packet does not cover:** decision 12 (the proposal
goes to an independent review before John rules). It is the step the review
itself carried out, so nothing is missing.

## 3. The second packet against the places it cites

Compared by this session with `docs/2026-10-03-controls-rerun.md`, the output
files under `experiments/rehearsal-successor-measure/out-controls-rerun/`, the
review and the proposal. The re-run's own figures were separately reproduced
by this session (the check of the controls re-run, filed beside this one).

| Page | Claim | Source | Result |
|---|---|---|---|
| 1 | The other-agent control does not apply to the separable and mixed models, by ruling | The proposal, section 7.3, item 2 | MATCH |
| 1 | Of the six remaining models one learned the other-agent condition: the free model's seed 0, 994 of 3,000 against 790 | `measure_F_seed0.json`, `control2.named_other_correct` 994; the others 760, 751, 708, 781, 746 | MATCH |
| 1 | The named agent's read is right on at most 137 of 180 against 144 | The same file: whole read 16, 95, 137, 127, 102 by layer | MATCH for the whole read. **One piece is higher than the whole read: 139 of 180 (layer 2, 8 directions).** Still under 144, so nothing turns on it, but "at most 137" is the whole read's best, not the best figure in the table |
| 1 | It "would have happened under the proposal's earlier rule too" | The earlier rule put the floor on the whole read: 137 is under 144 | MATCH |
| 1 | The quotation of item 5 of the 2026-09-21 ruling | That ruling, line 39 | MATCH, word for word |
| 1 | "Four repair attempts have not produced one that learns it" | The proposal, section 4.4: a doubled training budget, a curriculum, loss re-weighting, the grammar change | MATCH |
| 2 | Above the no-transplant rate by 0.065 to 0.10 on six of twelve: the mixed model on every seed, the entangled model's seed 2, the free model's seeds 0 and 2 | `summary.json`: 0.1013, 0.0800, 0.0850, 0.0713, 0.0788, 0.0650; the other six 0.0050 or less | MATCH |
| 2 | "Those six are exactly the ones whose transplant site reaches back to the model's first own turn" | True as a list. **But the control's positions do not depend on the site's position set at all**: the code takes only the site's layers (`rerun_controls.py`, lines 195 to 196). This session ran the control at every layer of every model: it is above nothing by 0.075 to 0.11 at the first layer on all nine models that are not the separable one, and what differs between models is how much survives at the second layer | **ARGUED from a MEASURED run** (the check of the controls re-run, section 5). The sentence describes a pattern, not the cause. It does not affect the diagnosis, which is right |
| 2 | In 0.5088 of pairs the donor's first own turn comes earlier; with positions before both, exactly the no-transplant rate on all twelve | Reproduced by this session with separately written code: 407 of 800; outputs bit-identical on all twelve | MATCH |
| 2 | "Their states should be identical", marked as not measured | Measured by this session: identical at every layer on all twelve | MATCH, and the caution was the right one to give |
| 2 | Version 1 made a failure withhold the reading; version 3 made it reported, giving "other routes" as the reason | The proposal, section 7.3, item 4, lines 1405 to 1414 | MATCH |
| 3 | A one-direction piece on the entangled model's seed 2: 0.306 at the action position, 0.161 to 0.194 elsewhere. The mixed model's 8-direction piece: 1.000, and 0.839 to 0.983 elsewhere | The review, lines 136 to 137 and 145 to 149 | MATCH |
| 3 | The re-run chose 4 directions at a span on seed 2 and 8 directions at a four-position set on seed 1; neither measured elsewhere | `summary.json`; the re-run's findings, section 3 | MATCH |
| 3 | The registered read is fitted at the action position (decision 23, ruled 2026-09-26) | The proposal, line 2525 | MATCH |
| 3 | "About two weeks before the registration deadline of 2026-10-18" | Fifteen days. The first packet and the review call the same date "the kill date" | MATCH |

**Whether each page states its options fairly** (ARGUED). Page 1 gives four
options, including the hardest one (build a case to exercise the control), and
names it as the strongest alternative. Page 2 gives three and says twice that
its recommendation rests on an unchecked, after-the-fact diagnostic. Page 3
gives three. **Page 2 is the one whose recommendation depended on something
not yet checked; that check is now done and the diagnostic holds.** One thing
page 2 says that a reader should hold on to: the redefined control "can only
fail if the pairing is broken". That is right, and it means a pass says
nothing about any model. The packet put this to John in plain words, so the
ruling was made with it in view.

## 4. Do the records say what the packets put, no more and no less?

John ruled each packet in the words "Agreed on all". So each record should be
the packet's recommendations and nothing else.

**The first record** (`2026-10-03-successor-v3-gate-c-rulings.md`), page by
page against the packet:

- **Pages 1 to 3:** as recommended. The record adds a sentence defining a
  piece's accuracy ("a read given only the state's coordinates inside that
  piece, on the same development episodes and split as the whole read"). The
  packet's page 1 does not define it; the definition is what the review's
  script computes. A fair filling-in, and the re-run's method then marked its
  own further choices (accuracy taken at the action position only) as its
  reading for John to overturn. For finding RT-232 the record repeats the
  packet's shortened fix; see row 9 above.
- **Pages 4 to 10, 12 to 14 and 16:** the table has eleven rows, one per page,
  each the proposal's recommendation. The compute-ledger sentence on decision
  8 is recorded as ruled; it was on the page.
- **Page 11:** items 1 to 4 and 6 are the page's. Item 5 is section 5 below.
- **Page 15:** option (b), with the page's caution carried.
- **It says about itself** that John ruled from the index and from the three
  pages the session pointed him to, and that the record does not show whether
  he read the rest. That is the right thing to have written down.

**The second record** (`2026-10-03-controls-rerun-rulings.md`):

- **Ruling 1** is page 1's option (b), plus the $0 run of the code path with
  the floor off, which the page offered as "worth making under (b)". Recorded
  as ruled; fair, since it was on the page and costs nothing.
- **Ruling 2** is page 2's option (a). **One small difference:** option (a)'s
  stated pass line is that the share landing on the donor's value equals the
  no-transplant share; the record's pass line is that "the transplant changes
  nothing", comparing the outputs themselves. That is stricter than option
  (a) as written, and it is what the page's own caution asked for. Nothing is
  lost by it. It also records its own condition: if the check finds the
  diagnostic wrong, the ruling returns to John. The check did not find it
  wrong.
- **Ruling 3** is page 3's option (c).

**Verdict (ARGUED):** neither record rules something its packet did not put,
and neither leaves out something its packet recommended. The additions are
the three named above, each taken from the same page.

## 5. Page 11: was "Agreed on all" fairly recorded as agreeing that the fifth outcome is satisfactory?

**What the packet did.** The index row for page 11 reads: "Agree, including a
fifth registered term". The page's recommendation is "agree with all three"
parts of the proposal's recommendation. Then, under "Three things to be clear
about before agreeing", it asks "Is the fifth outcome satisfactory?", gives a
suggestion (satisfactory, and stated as weaker than R1), and says: "This is
John's call and nothing in the record settles it."

**What the record did.** It lists "the fifth outcome is satisfactory, and is
stated as weaker than R1" among the things ruled, and says in the same item:
"The packet put this as a suggestion and said it was John's call; 'Agreed on
all' is recorded as agreeing to it."

**This session's view (ARGUED).**

- **The record is fair in the sense that matters most: it hides nothing.** A
  reader of the record learns exactly how thin the basis is. It also says
  that page 11 was one of the three pages the session drew John's attention
  to before he ruled.
- **But "Agreed on all" answers recommendations, and this was put as an open
  question.** The packet's own instruction was "'Agreed on all', or a list of
  exceptions by page number, is enough." A question the packet itself calls
  "John's call" is not obviously something a blanket agreement settles. The
  suggestion was not in the index row, and it was not one of the three parts
  of the recommendation.
- **The caveat did not travel.** The dated note added to
  `docs/december-result-roadmap-2026-09-20.md` says flatly: "John ruled on
  2026-10-03 that the successor's registration carries a fifth term ... It is
  satisfactory, and stated as weaker than R1." A reader of the roadmap does
  not see that this half was a suggestion swept in by a general agreement.
- **Why it is worth one more word from John.** The proposal's own stated
  expectation is that the free model returns no verdict or fails its gate.
  So whether the December result counts as satisfactory may well turn on this
  one line. It is cheap to confirm now and awkward to argue about in December.

**Recommendation:** John confirms or overturns it in a sentence. Until then
the record should be read as "suggested and not objected to", not as "ruled
on its merits". This session has not edited the record or the note.

## 6. The three dated notes

| Where | What the note says | Check |
|---|---|---|
| `docs/december-result-roadmap-2026-09-20.md`, lines 87 to 92, under the outcome table | A fifth term, "metric validated, degree not read", for the case where the built models separate and the free model returns no verdict; satisfactory, and weaker than R1 | The first half matches the record's page 11, items 3 and 4. The table above it is left as written, as the note says. **The "satisfactory" half carries the weakness of section 5 without its caveat** |
| `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, lines 338 to 343, beside "a five-layer model" | The phrase counts the toy's five running states; it has four blocks; the registered model has twelve blocks and thirteen states; "the ruling stands as recorded" | MATCH with the review's finding RT-236 (four blocks, five states; twelve and thirteen) and with the record's page 3. The sentence it sits beside is untouched |
| `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, lines 110 to 117, under the decisions table | Decision 15's 0.05 is withdrawn, the other-agent control kept as a reported description; decision 16 is reversed, the too-early-position control redefined on both twins and made a control that holds; page 1 gains a reported figure with the rule unchanged | MATCH with the second record's rulings 1, 2 and 3. The table is left as written |

## 7. What should happen next

1. **To John:** the one-sentence confirmation of section 5.
2. **For whoever writes version 4 of the proposal:** take finding RT-232's fix
   from the review's own wording (row 9); do not carry page 10's $97.04
   sentence (row 3); quote the re-run, not page 1's option (b), for the
   entangled model's sizes and readings (row 6).
3. Nothing here blocks version 4.
