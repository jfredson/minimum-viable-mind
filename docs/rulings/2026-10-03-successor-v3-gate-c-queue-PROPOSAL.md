# Proposal for John, 2026-10-03: the rulings on the review of proposal version 3, one page each

*Written 2026-10-03 (Pacific) by a Claude Code session, at John's request.
**This is a proposal, not a ruling. Nothing in it is decided, nothing in it is
registered, and no registered text, ruling file, protocol text or proposal
text is changed by it.** Nothing was rented or spent to write it.*

*Written under the workspace plain-language rule. Findings are labelled
**MEASURED** (a command was run and its output is in the file cited) or
**ARGUED** (reasoning a reader can dispute). Two documents are cited
throughout and named here once:*

- *"the proposal" is `docs/successor-experiment-proposal-2026-09-26-v3.md`,
  version 3 of the successor experiment proposal, on the main line at
  `6d4ec3a` (pull request 71);*
- *"the review" is its first independent review,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`,
  on the main line at `4cb7f8e` (pull request 74). Its findings are numbered
  RT-230 to RT-236 in the red team ledger's sequence.*

**Two things a reader should know before relying on this packet.**

1. **The session that wrote it also wrote the review.** So pages 1 to 3
   recommend rulings on this session's own findings. The measurements behind
   them are in the review with their commands; the recommendations are
   opinions and are John's to overturn.
2. **It is owed a check.** Under the pairing rule in
   `docs/outside-review-protocol.md`, a packet on its way to John is checked
   by a session that did not write it before he relies on a number in it. No
   such check has been run. Every number here is copied from the review or
   the proposal, with the place named, so the check is a matter of comparing
   them.

---

## The one-page index

**How to rule.** "Agreed on all", or a list of exceptions by page number, is
enough. A session then writes the rulings up as
`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, with authorship
recorded as mixed, and a different session checks it.

**The order that matters.** Page 1 first: it changes which piece of the model
gets transplanted, and the $0 re-run of page 2 should use whatever page 1
rules. Everything after page 3 is independent of everything else.

| Page | Decision | Recommendation (John's to overturn) | Confidence |
|---|---|---|---|
| 1 | The accuracy floor is checked on the whole read, not on the piece that is transplanted (the review's finding RT-230) | Only pieces that themselves carry the label at four fifths may be chosen; print that figure in the results table | moderate to high |
| 2 | Four controls have no figure under the rules being registered (finding RT-233) | The $0 re-run is a precondition of the registration review, and runs under page 1's rule | high |
| 3 | Four small fixes (findings RT-232, RT-234, RT-235, RT-236) | Accept all four as the review states them | high |
| 4 | The separable model's ownership path is forced by its architecture (proposal decision 2) | Agree | high |
| 5 | The entangled model is entangled by its architecture (decision 3) | Agree | moderate to high |
| 6 | The two transplants are a piece and the whole, at the same places (decision 4) | Agree | high |
| 7 | A new experiment folder with its own registration (decision 8) | Agree: `experiments/08-…` | high |
| 8 | The mismatch between the two task conditions is recorded, not engineered away (decision 9) | Agree | high |
| 9 | The channel-removal check is a precondition for reading the free model, never evidence of a centre (decision 10) | Agree | high |
| 10 | The shutdown rule is part of the registered recipe (decision 13) | Agree | moderate |
| 11 | **What a "no verdict" counts as (decision 14)** | Agree, including a fifth registered term, "metric validated, degree not read" | moderate; this is the one that most deserves thought |
| 12 | The tolerance on the other-agent control: 0.05 (decision 15) | Agree | low on the number, and it matters little |
| 13 | The too-early-position control is reported, not a veto (decision 16) | Agree | moderate |
| 14 | Fifty timed steps instead of five hundred (decision 17) | Agree: accept fifty, take the longer timing from the first full-size run | moderate to high |
| 15 | The untested half of the shutdown test (decision 18) | Agree: option (b), register what can honestly be said | moderate |
| 16 | The four position sets, by name (decision 19) | Agree | moderate |

**What these rulings do not do.** They release no money and give no go. They
do not open the registration review: that waits on version 4 of the proposal
and on page 2's re-run.

---

## Page 1 — the accuracy floor is checked on the whole read, not on the piece that is transplanted

**The question in one sentence.** When the measure says "the ownership piece
does nothing on its own", how does the record show that the piece was carrying
the ownership label in the first place?

**What the design does now.** A straight-line read is fitted at each layer to
predict which marker word is the model's own. If it is right four times in
five on held-out episodes, the floor passes. What is then transplanted is not
the whole read but its leading 1, 2, 4 or 8 directions, and the rule picks how
many by whichever moves the action most, with ties going to the fewest
(proposal, section 7.2, items 3 and 5).

**What the review measured** (finding RT-230, MEASURED, its first two output
blocks). The label has twelve possible values. On the entangled model:

| Seed | Size of piece the rule chose | Whole read's accuracy | The chosen piece's own accuracy | The 8-direction piece's accuracy | Reading at the chosen size | Reading at 8 directions |
|---|---|---|---|---|---|---|
| 0 | 8 directions | 1.000 | 1.000 | 1.000 | 1.0051 | 1.0051 |
| 1 | 2 directions | 0.961 | **0.544** | 0.900 | 1.0025 | 0.9975 |
| 2 | 1 direction | 0.978 | **0.306** | 0.989 | 1.0000 | 0.9897 |

So on two seeds of three the transplanted piece misses the four-fifths floor,
although the floor "passed". The proposal's sentence that the transplanted
piece "holds the label and clears the fit floor on every seed" (section 5.2)
is false on those two. **The readings are not in doubt**: the entangled model
reads between 0.99 and 1.005 at every size, and the largest piece does carry
the label. What is wrong is the rule and the sentence, and at full size the
same rule would let a free-model reading be reported beside a piece the floor
never certified.

**Why the rule drifts to small pieces.** Where no piece moves the action, the
choice between sizes is a choice among figures that differ by one or two
episodes of 600, and ties go to the smallest.

**The options.**

- **(a) Apply the floor to the chosen piece.** Honest, but on its own it
  returns no verdict on entangled-model seeds 1 and 2, so the toy would no
  longer show a reading on the high anchor on every seed.
- **(b) Only sizes whose own accuracy clears four fifths may be chosen, and
  that accuracy is printed in the results table.** On the toy: the entangled
  model is read at 8, 8 and 4 directions (readings 1.0051, 0.9975 and 0.9974,
  from the review's second output block); the separable and mixed models stay
  at 8 directions with their readings unchanged; the free model has no size
  that clears, and returns no verdict as it does now.
- **(c) Leave the rule, and always print the 8-direction row beside the
  chosen one.** Smallest change. The floor still certifies something other
  than what was transplanted.
- **(d), not in the review: fix the size at 8 directions and report 1, 2 and
  4 as extra rows.** Simplest, and it cuts the number of comparisons by four.
  Its risk is at full size: nobody has checked that 8 directions can carry
  the label in the registered model.

**Recommendation: (b).** It makes the floor certify the thing that is
transplanted, it keeps every toy verdict, and it leaves the choice of size to
one rule applied to every model alike. *Confidence: moderate to high.* It is
a new rule, so it has not been run end to end; page 2's re-run is where it is
exercised, and the registration should not quote the three readings above as
committed results until then. **Strongest alternative: (d)**, if John prefers
fewer moving parts over a rule that adapts to the model.

**Whatever is chosen**, sections 3 and 5.2 of the proposal are reworded to
say what was measured: the read holds the label; the largest piece
transplanted holds it; no size moves the action.

*Changes:* proposal version 4, sections 3, 5.2, 6.4 (item 2), 7.2 (items 3
and 5), 7.4 and 7.5 (a new column).

---

## Page 2 — four controls have no figure under the rules being registered

**The question in one sentence.** Does the registration review wait for the
re-run the proposal promises?

**The facts** (finding RT-233, ARGUED; the proposal says the same in sections
7.3 and 10). The toy re-run under the registered rules re-ran two of the seven
controls. For the entangled, free and mixed models, controls 1, 2, 4 and 6
have no figure at the places the rule now chooses, and the earlier figures are
withdrawn. The known-answer test of the transplant code (control 7) was not
run at seven places that changed. All seven controls are frozen by the
registration.

**Why it is not optional.** Item 5 of the ruling of 2026-09-21
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`) makes a
pre-stated quantity the rehearsal never exercised a fatal finding on its own
at the registration review.

**One piece is already done.** The mixed model's reading against its built-in
reference at the new places was run by the review and holds: off by 0.0049,
0.0099 and 0.0529 against an allowance of 0.10 (finding RT-231, MEASURED).

**Recommendation.** Rule that the re-run of the rehearsal's first six items
under the registered rules, with page 1's rule in it, is a precondition of the
registration review; it is committed with method before output, and checked by
a session that did not run it. *Confidence: high.* Laptop only, $0. It sits on
the path to the 2026-10-18 kill date, so it starts as soon as page 1 is ruled.
**Alternative:** none that the protocol allows.

*Changes:* the weekend roadmap's Weekend 2 goals; the TimeAssembler step for
the re-run, which already exists.

---

## Page 3 — four small fixes

Each is a wording or reporting change for version 4. None changes a verdict.

- **Finding RT-232 (MEASURED).** The free model's read accuracies move by one
  held-out episode of 180 depending on whether the laptop's processor or its
  graphics chip does the arithmetic (0.178 against 0.172; 0.100 against
  0.106). *Fix:* state the accuracy as a count of episodes, name the device
  the registered figure is computed on.
- **Finding RT-234 (MEASURED).** The floor on the whole-state transplant is
  applied twice: on development episodes when the place is chosen, on fresh
  episodes when the reading is taken. The text names only the second. On the
  toy they agree on all twelve; the narrowest margin is 9 episodes of 600.
  *Fix:* say both, and say that a place which clears the first and misses the
  second returns no verdict.
- **Finding RT-235 (ARGUED).** The stop after the first full-size free-model
  run reports the read's accuracy at whichever layer the rule chose, and where
  nothing moves the action that choice is made among noise. *Fix:* the report
  for that run prints the accuracy at every layer, the chosen piece's own
  accuracy (page 1), and the candidates the rule chose among.
- **Finding RT-236 (MEASURED).** The toy is called "a five-layer model"
  against "the twelve-layer model". It has four blocks; the registered model
  has twelve. *Fix:* state the depths the same way in both places. The same
  phrase is in the reason recorded for John's ruling of 2026-09-26 on the
  label search; that file gets a dated note beside it, not an edit. The label
  search and its check are also now cited by their main-line commits
  (`a97c12b`, `ecd2b6c`).

**Recommendation: accept all four.** *Confidence: high.*

*Changes:* proposal version 4, sections 6.4, 7.2, 9 and 11; one dated note in
`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`.

---

## Page 4 — the separable model's ownership path is forced by its architecture (decision 2)

**The question.** Is the built-to-be-separable model made separable by its
wiring, or only encouraged to be by a penalty during training?

**The proposal's position** (section 5.1). Forced: an explicit table of who
assigned what, and one slot that holds "which agent am I" and nothing else.
Its degree is zero because of how it is built.

**What is on the record.** It reads 0.0000 on every toy seed, and its training
reproduces exactly from code and seed (proposal, section 5.1).

**Recommendation: agree.** *Confidence: high.* The whole point of this model
is a degree that is known and not hoped for. **Alternative:** a softer version
with a penalty, closer in kind to the free model but with a degree nobody
could state in advance.

*Changes:* none; version 4 marks it ruled.

---

## Page 5 — the entangled model is entangled by its architecture (decision 3)

**The question.** Is the built-to-be-entangled model made that way by its
wiring, or trained with a penalty against any separable ownership direction?

**The proposal's position** (section 5.2). By wiring: the ownership signal
multiplies into the content at every layer and has no slot of its own.

**What is on the record.** Its reads find the label at 0.96 or better and no
piece of any size moves the action (page 1's table). It fails the
other-agent condition on every toy seed (760, 751 and 708 of 3,000 against
790), which no longer gates it under the ruling of 2026-09-26.

**Recommendation: agree.** *Confidence: moderate to high.* **Alternative:** a
penalty that punishes any transplantable ownership direction, which would
train the model against the very instrument that measures it. Recommended
against. **The risk that stays** (the proposal's weakness W3): at full size
the model could still concentrate ownership in a few directions, and that
would be seen only after both releases of money are drawn.

*Changes:* none; version 4 marks it ruled.

---

## Page 6 — the two transplants are a piece and the whole, at the same places (decision 4)

**The question.** What is the ownership-only transplant compared against?

**The proposal's position** (section 6.2). Against the whole internal state
transplanted at exactly the same places. The reading is then how much of the
identity-driven difference at those places lives outside the piece.

**Recommendation: agree.** *Confidence: high; this is ordinary practice for
comparing interventions.* **Alternative:** compare against transplanting
everything everywhere, which always succeeds and turns the measure into a
report on how the places were chosen.

*Changes:* none; version 4 marks it ruled.

---

## Page 7 — a new experiment folder with its own registration (decision 8)

**The question.** Does the successor live in a new folder, or as one more
amendment to the earlier experiment (MVM-0a, `experiments/06-…`)?

**The facts.** The earlier experiment's last amendment closed on 2026-09-25.
`experiments/07-embodiment-amplifier-test` exists, so the next number is 08.

**Recommendation: agree, `experiments/08-…`.** *Confidence: high.*
**Alternative:** a further amendment to experiment 06, which keeps one ledger
but attaches new work to a closed registration. **One thing to settle with
it:** the compute ledger stays where it is, in experiment 06's folder, as the
programme's single record of money; the new folder points at it.

*Changes:* a new folder at the registration commit; the rehearsal code moves
or is referenced from it.

---

## Page 8 — the mismatch between the two task conditions is recorded, not engineered away (decision 9)

**The question.** In one condition the model is told by a word whose value to
use; in the other it has to have carried "which agent am I" itself. Should the
design remove that difference?

**The proposal's position** (section 4.2). No. Removing it means putting the
model's own name in the text, which brings back the leak the acting channel
was built to avoid. The mismatch is the experiment, and it limits what a
difference between the conditions may be read as.

**Recommendation: agree.** *Confidence: high.* **Alternative:** add a
condition where the model's own name appears as a word. Recommended against.

*Changes:* the registration text carries the paragraph as a known limitation.

---

## Page 9 — the channel-removal check is a precondition, never evidence of a centre (decision 10)

**The question.** Before the free model is read, its acting channel is zeroed
to see whether its accuracy collapses. What may that result be called?

**Already ruled:** the shape of the check and its two-seeds-of-three clause.
**Not yet ruled:** its standing.

**The proposal's position** (section 8.2). It shows the ownership answer is
needed for the act, which is what makes the model worth reading. In the earlier
design's own registered words it "removes a sense organ, not a structure the
network built". It is never reported as evidence of a centre.

**Recommendation: agree.** *Confidence: high.* **Alternative:** none worth
taking; reporting it as more would be the over-reading the project's rules
exist to prevent.

*Changes:* none; version 4 marks it ruled.

---

## Page 10 — the shutdown rule is part of the registered recipe (decision 13)

**The question.** Does the registration itself say that the launcher waits for
the receipt and that the trainer does not delete its own machine, or is that
left in scripts outside the registration?

**The facts.** The launcher is already named in the proposal (section 5). On
2026-09-25 the laptop's half of the shutdown worked against the real vendor;
the machine's half was not exercised (proposal, section 10, item R-11).

**Recommendation: agree, register it.** *Confidence: moderate.* The
programme's largest single loss, $97.04 on the run of 2026-08-09/10, was a
machine that kept running after its work was done. **Alternative:** leave it in
unregistered scripts, where a later edit can remove it without anyone ruling.

*Changes:* one paragraph in the registration text. Read with page 15.

---

## Page 11 — what a "no verdict" counts as (decision 14)

**The question in one sentence.** If one of the four models returns no
verdict, which of the registered outcomes is that?

**Why this is the page to think about.** On the toy record the free model
returns no verdict on every seed, and the proposal's own stated expectation is
that this is the most likely result at full size (its section 3, "The honest
prior"). So this page decides the words the December result is most likely to
be reported in.

**The registered outcomes now** (the December-result roadmap, ruled
2026-09-20): R1 "metric validated, degree read"; R2 "metric does not
separate"; R3 "substrate not a testbed"; R4, the schedule failure.

**The proposal's recommendation**, in three parts:

- no verdict on the **entangled** model: the two-model fallback, already ruled
  in advance on 2026-09-20;
- no verdict on the **mixed** model: it is dropped and carried as an extension
  on the weekend roadmap;
- no verdict on the **free** model after the built models have separated: a
  **fifth registered term, "metric validated, degree not read"**, with the
  reason after a colon.

**Recommendation: agree with all three.** *Confidence: moderate.* The fifth
term says exactly what would have happened. The review reached the same view
(its section on over-reading). **Strongest alternative:** keep four terms and
report it under R1 with a sentence. That would file "no reading" under a term
that says "degree read".

**Three things to be clear about before agreeing.**

1. Adding a term amends the outcome list John ruled on 2026-09-20. The ruling
   should say so in terms.
2. **Is the fifth outcome satisfactory?** The roadmap marks each outcome as
   satisfactory or not. The measure is the Stage 2 deliverable, "the metric,
   not a verdict", so a validated measure with no reading delivers it. The
   suggestion is: satisfactory, and stated as weaker than R1. This is John's
   call and nothing in the record settles it.
3. It does not replace the stop after the first full-size run. A miss there
   still goes to John before the second release of money.

*Changes:* proposal version 4, section 3 (the outcome table and the reporting
paragraph); a dated note beside the outcome list in
`docs/december-result-roadmap-2026-09-20.md`.

---

## Page 12 — the tolerance on the other-agent control: 0.05 (decision 15)

**The question.** One control transplants a representation of the *other*
agent and expects the model's own-marker action not to move. How much movement
is allowed?

**The facts.** 0.05 above a random piece of the same size was the rehearsal's
working figure, chosen before any result existed. The control is reported and
cannot veto a reading. It runs only on models that learned the other-agent
condition, which on the toy is one seed.

**Recommendation: agree, 0.05.** *Confidence: low on the number, high that a
pre-stated number is needed.* Because the control only reports, a poor choice
costs a line in a table, not a verdict. **Alternative:** 0.018, the allowance
used elsewhere in the design; tidier, and possibly too tight for a control
that moves an action.

*Changes:* proposal version 4, section 7.3, item 2.

---

## Page 13 — the too-early-position control is reported, not a veto (decision 16)

**The question.** One control transplants at a position before the model can
know which agent it is, and expects nothing to happen. If something does, is
the reading withheld?

**The facts.** On the earlier rehearsal run this control did not come back at
"nothing" on the entangled and free models, because those models receive the
ownership signal by other routes at those positions (proposal, section 7.3,
item 4). As first written it would have withheld the reading on exactly those
models.

**Recommendation: agree, reported.** *Confidence: moderate.* This is the
design's own call and not yet anyone's ruling. Page 2's re-run will give its
figures at the registered places. **Alternative:** keep it as a veto and
anchor it somewhere the chosen places cannot reach; the rule does not
guarantee such a position exists.

*Changes:* none beyond marking it ruled.

---

## Page 14 — fifty timed steps instead of five hundred (decision 17)

**The question.** The rehearsal item asks for five hundred timed training
steps per model on the rented machine. The run John authorised on 2026-09-25
timed fifty. Is that enough to price the second release?

**The facts** (proposal, section 9 and weakness W8). 13.08, 13.52 and 12.53
milliseconds per step; each model's slowest step within 3% of its median. The
mixed model was not timed.

**Recommendation: agree.** Accept fifty for the arithmetic, and take the
five-hundred-step figure from the first full-size run, repricing the later
runs from it before the second release is asked for. *Confidence: moderate to
high.* **Alternative:** rent a longer timing first, about another dollar and
another go.

*Changes:* proposal version 4, section 10 (item R-11) and section 12.4.

---

## Page 15 — the untested half of the shutdown test (decision 18)

**The question.** The machine's own "I have seen the receipt" has never been
observed, because the laptop deletes the machine in the same second it writes
the receipt. What does the registration say about it?

**The options.**

- **(a)** Make the laptop wait, and have the machine write its
  acknowledgement somewhere the laptop collects. This lets a pass be seen. It
  is code work and one more rented test.
- **(b)** Leave the design, and register what is true today: on the normal
  path the laptop does the deleting, and the machine's own watcher is a
  backstop for a laptop that never answers.

**Recommendation: (b) for the registration, with (a) as the repair if a later
run shows the laptop failing to answer.** *Confidence: moderate.* **A caution
that goes with it:** the Weekend 1 handoff listed (a) among the Weekend 2
items. Ruling (b) takes it off that list. Twelve full-size runs would then
rest on a backstop that has never fired against the real vendor; the
never-sleep refusal in the launcher is what stands in front of it.

*Changes:* proposal version 4, weakness W9; the Weekend 2 launcher items.

---

## Page 16 — the four position sets, by name (decision 19)

**The question.** The ruled site rule says which positions are candidates but
not how they are grouped. Which grouping is registered?

**The proposal's position** (section 7.2, item 2). The rehearsal's four: the
action position alone; the action position and the token just before it; the
action position and the three before it; everything from the model's first
own turn to the action.

**The facts.** This is the only grouping that has been run, now under the
registered rule, and it gives the 325 site sets on the registered model that
John ruled on 2026-09-26.

**Recommendation: agree.** *Confidence: moderate.* **Alternative:** one set
per position between the source and the action, which follows the ruled clause
literally, has never been run, and would change the count already ruled.

*Changes:* none beyond marking it ruled.

---

## Appendix — where each number on these pages comes from

- Page 1's table: the review, finding RT-230, the outputs of
  `subspace_fit.py` and `rank_and_floor.py` in
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-scripts/`.
  The choice of size under option (b) is this session's reading of those
  outputs: among sizes whose own accuracy is 0.8 or more, the highest
  development ownership-only share, ties to the smaller (seed 0: 8 directions
  at 0.0550 over 4 at 0.0517; seed 1: only 8 clears; seed 2: 4 directions at
  0.0533 over 8 at 0.0517). ARGUED until page 2's re-run produces it.
- Page 2: the review, findings RT-231 and RT-233; the proposal, sections 7.3
  and 10.
- Page 3: the review, findings RT-232 and RT-234 to RT-236.
- Pages 4 to 16: the proposal's section 15, by decision number, and the
  sections each page names.
- The $97.04 on page 10: the compute ledger,
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, the
  2026-08-09/10 row for the 30-million-parameter pilot (line 79) and its
  reconciliation (line 386: "$97.04 = 29.5h @ $3.29/hr").
