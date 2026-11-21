# Kickoff proposal: Minimum Viable Mind becomes a tracker of the theories of consciousness

*Written 2026-11-20 by a working session, from John's proposal of the same day. The direction is
John's. Everything below it (the design, the scores, the formulas, the order of work) is the
session's, for his rulings in section 9; five rules for the scores and six for the ranking
were ruled by John the same day (section 4), and seven rulings are still open, go or no go first. Nothing is built. If John rules yes, this supersedes
section 4 of `docs/2026-11-20-three-hypotheses-and-refocus-proposal.md`.*

## 1. John's proposal, in his words

> What I would like to propose is that the minimum viable mind project turns into a new tracker
> site that tracks the progress made on all of the open questions related to consciousness and
> whether or not new evidence is tracking the predictions we have made with our working positions.
> Our MVM coding project can be one aspect of the site where we try to test these things ourself,
> but the bigger picture for the site should be, what are the active theories surrounding
> consciousness and how far along is the science in proving any individual theory, and then
> theories should be ranked based on how well the science backs them up, how well they are defined
> such that they can be tested, and how much is still left to test for each theory. This should be
> a completely quantifiable question for every working theory including our own.

## 2. The session's view of it, in short

It is a good fit for the family, and the strongest thing about it is "including our own": a site
that ranks the account published on Sentient Horizons by the same rules as every rival, and shows
it losing where it loses, is worth more to a reader than one more essay arguing for it. It also
gives Minimum Viable Mind a public face that does not depend on its own experiments producing a
result, which so far they mostly have not.

Two honest limits, stated now so the design answers them:

- **"Completely quantifiable" can mean that every number is computed by a fixed rule from a dated,
  sourced record. It cannot mean that no judgement goes in.** Someone has to decide what a theory
  predicts and whether a study's result supports it. The design makes every such judgement a
  separate, sourced, revisable record, read by a second reader on a model from another lab, so the
  numbers follow mechanically from judgements anyone can inspect and dispute one at a time.
- **The site ranks John's own account, so it has a conflict of interest built in.** The answer is
  the same rules for every theory, fixed before any theory is scored; the outside reader making
  the first judgement on every Sentient Horizons row; and the site saying so on the first screen.

## 3. The shape, in the tracker pattern's terms

**The trunk.** The question: *How far has the science of consciousness got in testing its
theories?* The thing held at a glance: the ranking, one row per theory, with three bars each
(section 4). The headline number, worked out from the leaves (tracker pattern rule 1.1): **the
share of the theories' sharp predictions that have been tested at all**, across every theory on
the site. It answers John's "how far along is the science" in one figure, and it should start low. *(ruled, John: "A, tested at all"; recorded 2026-11-21.)* Exactly: the
share of the distinguishing predictions tied to core claims that at least one counted study has
tested, as `scripts/tracker_scores.py` computes it (8 of 12 at the end of stage 2). Weakest steps,
stated to John when he ruled: it measures how widely the theories have been tested, not how firmly, so the card must say "tested
at all", and the support bars carry the strength; and it can fall when the field adds predictions, and
the page explains that the first time it happens.

**The branches.** One per theory, a fixed set of four to nine changed only at the yearly review
(rule 2.1). A first list for John, to be settled from sources (section 7), not from memory:
global workspace theory; integrated information theory; higher-order theories; recurrent
processing theory; predictive processing, with Anil Seth's living-body view; the attention schema
theory; and the Sentient Horizons account. Two candidates need a ruling: illusionism, which
denies there is a further fact to explain and still makes predictions about reports; and the
biological views that tie experience to living tissue. Seven to nine fits the rule.

**The leaves: predictions.** Each leaf is one prediction a theory makes, with a page of its own:

1. its plain statement;
2. **whose it is**: stated by the theory's own proponents (with the source), or inferred by the
   site (labelled, and counted at half weight until a proponent states it);
3. **the test**: what result would count for it and what against, written so two readers agree;
4. **whether it discriminates**: which rival theories predict something different. A prediction
   every theory shares is recorded but scores nothing;
5. **who settles it**: a published study with a measured result, never a press release or a talk;
6. **its state, with a date**: untested, supported, contradicted, or mixed, with each study that
   set it, and the study's quality (section 4);
7. its dated record, the last readings, and a way to disagree with this one thing.

One prediction can belong to several theories, for or against each.

**Beside the trunk, never moving it** (rule 1.2):

- **The open questions.** Which features experience needs; whether a machine could have it;
  which animals do; whether it can fade to nothing; whether a group can share one present. Each
  question links to the predictions that bear on it, so a reader sees which tests would move it.
  The questions held open on the Working Positions page are among them.
- **Our working positions against the evidence.** The Sentient Horizons account is scored as one
  branch like any other. Its predictions are taken from the "What would change my mind" sections
  of the public positions, which already state them. This page shows, for each position, whether
  new evidence has gone its way, against it, or neither.
- **Our own tests.** What Minimum Viable Mind does now: registered removal tests, run by the
  project, with their own rules (registration, spend under John's go, every result recorded as
  measured or argued). Its questions Q10 to Q12 become predictions on the Sentient Horizons branch.
  A result here counts in the scores only by the same rules as anyone's study, at the quality
  its method earns.

## 4. The three scores, and the ranking

**Ruled by John on 2026-11-20: "Yes to all five".** The five rules marked *(ruled)* below were
put to him that day as the session's recommendations, and he accepted all five. The wording of
each rule is the session's. Everything else in this section is still a proposal.

Each score is a number from 0 to 100. It is worked out from the leaves by a rule written down
before any theory is scored, and shown with its count, so that a reader can see how much it rests on.

**Testability: how well the theory is defined, so that it can be tested.**

- *(ruled)* **The core claims.** Each theory's core claims, between three and seven, are taken from
  one named publication by its own proponents and quoted. They are fixed before any theory is
  scored, and change only at the yearly review. Proponents and readers may dispute the choice on
  the disagree page. Counting claims, not predictions, stops a theory from scoring higher just by
  saying more. The weak point is that choosing the claims is a judgement where a theory has no
  single canonical statement (global workspace theory, for example); quoting the source and fixing
  the choice in advance is the answer.
- **The score.** A core claim scores 1 if a proponent states at least one prediction for it that
  could fail and that separates the theory from a rival; 0.5 if only the site has inferred one; 0 if
  none. Testability is the average across core claims, times 100.

**Support: how well the science backs it.** Across the theory's tested predictions that separate
it from a rival, each study's outcome counts +1 for, −1 against and 0 for mixed, multiplied by the
study's weight.

- *(ruled)* **A study's weight counts its protections against bias.** It starts at 1 and gains 1
  for each of these, up to 5:
  - its predictions were registered before the data came in;
  - it was run by people outside the theory's own camp;
  - a rival camp agreed in advance what result would count against each side;
  - another group has replicated it.

  This replaces the fixed table of weights first proposed (4, 3, 2 and 1), which were numbers
  without a stated reason. Each step up now has a reason a reader can check.
- *(ruled)* **Predictions tied to core claims count double.** A failure on a core claim is worse
  than one on a side claim. This rests on the core claims being chosen well, which is the
  testability score's weak point, so the two rules are reviewed together at the yearly review.
- *(ruled)* **A failure stands once recorded.** A prediction's state is fixed by what the theory
  said before the study. A later rescue (a new reading of the theory that softens the loss) is
  recorded and becomes a new prediction, which needs its own test. It does not undo the failure.
- *(ruled)* **No support score until studies from at least two separate research groups exist.**
  Until then the theory is shown as "too little tested to score", however many predictions one
  group has tested. This replaces the first proposal's minimum of three tested predictions, which
  one lab could meet alone.
- *(ruled)* **A split between "mixed" and one side is recorded as "mixed".** *(ruled, 2026-11-20,
  John: "Yes, as you lean"; wording the master session's.)* When the two readers of an outcome split
  between "mixed" and "for" or "against", the outcome is recorded as "mixed". Weakest step, stated
  when it was ruled: it always pulls toward the middle, so it is to be reviewed when stage 3 shows how
  often it fires. (Raised by the stage 2 pilot, where it fired on two of fourteen outcomes.)
- **The number.** Support is the weighted sum divided by the total weight, which runs from −1 to 1,
  put on a 0 to 100 scale: 50 means the evidence is even, above 50 it leans for, below 50 against.
  It is an average, not a total, so a theory tested more often does not score higher for that
  alone. More tests make the score steadier, and the page shows how much it rests on beside it.

**Left to test: the share of the theory's distinguishing predictions that no study has touched.**
Only predictions tied to the fixed core claims count, and every core claim must have at least one,
so a theory cannot look nearly finished by having said little. When new predictions are added the
number can rise, and that is honest: the field found more to test. The page shows the score's
history so that a reader can see why it moved. A high number is not a fault; it says where the
work is.

**A worked example, with invented numbers.** A theory with five core claims. Proponents state a
prediction that could fail for three claims, the site infers one for a fourth, and the fifth has
none: testability is (3 + 0.5 + 0) ÷ 5 = 70. Two studies from different groups: one registered
and run outside the camp (weight 3) came out for; one with no protections (weight 1) came out
against. Support is (3 − 1) ÷ 4 = 0.5, which is 75 on the scale. Two of eight distinguishing
predictions are tested, so 75 is left to test. The page would read: well defined, leaning
supported on thin evidence, most of it still untested.

**The ranking. Ruled by John on 2026-11-20: "Yes to all six".** The six rules below were the
session's recommendations; the wording is the session's.

1. *(ruled)* **Three groups, shown in this order:**
   - **Ranked:** past the testability bar, with a support score.
   - **Testable, too little tested to rank:** past the bar, but without studies from two separate
     groups yet, so with no support score.
   - **Not yet defined sharply enough to rank:** below the bar, each shown with what it would
     need, meaning which core claims lack a prediction that could fail.
2. *(ruled)* **The bar is a criterion, not a bare number:** a theory is ranked only when more than
   half its core claims come with a prediction that could fail. *(ruled, 2026-11-20, John: "Yes,
   must separate".)* The bar counts a core claim only if it has a prediction that could fail and
   that a rival predicts differently, the same test as the testability score. *(ruled, 2026-11-20,
   John: "Yes, sourced only"; wording the master session's.)* A prediction separates a theory from a
   rival only when a publication by the rival's own proponents, opened and cited, predicts something
   different. A reader's own knowledge does not count, and a rival's silence does not count. This
   governs both the bar and the testability score. (Raised by the stage 2
   pilot, which found the first wording did not say; wording the master session's.) A support score speaks only for the
   claims that were testable; where fewer than half were, it describes a minority of the theory,
   and ranking the whole theory on it would mislead. This replaces the bare figure of 50 first
   proposed.
3. *(ruled)* **The order is support, highest first.** Testability gets a theory into the ranking
   and what is left to test is shown beside each row, but neither sets the order; if they did,
   vagueness or little testing would count in a theory's favour. The three scores are not combined
   into one number, for the same reason.
4. *(ruled)* **Ties go to the theory resting on more evidence**, measured by the total weight of
   its studies, not by how many tests it has had, so that a few well-protected studies outweigh many
   unprotected ones.
5. *(ruled)* **Two theories share a rank unless their order would survive reversing the outcome of
   any single study.** If one study going the other way could swap them, they are shown as tied,
   and the page says so. A reader can check it by hand. Known cost, stated when it was ruled: early
   on most theories may come out tied, so the first screen may look undecided for a while. That is
   the honest result, and it matches the headline, which says how little of the field has been
   tested.
6. *(ruled)* **A theory the evidence goes against stays in the ranking**, in its place by score,
   with the note "the evidence so far leans against it". Removing it would hide what the site
   exists to show.

Within the second and third groups, theories are listed by testability, highest first (the
session's choice, following from rule 3; not separately ruled). The three bars stay visible
beside every row, so a reader can weigh them differently.

A first guess at where this leaves the Sentient Horizons account, to be replaced by the real
scoring: high on testability, because every position states what would change its mind; too
little tested to score on support; nearly everything left to test. The page should say that
plainly.

## 5. How a judgement gets made, and checked

- **Every judgement is its own record.** "This study supports this prediction" is a row with the
  study, the passage, the reason, who judged it and when.
- **Two readers.** The first reading of every outcome is made by one reader and checked by a
  second on a model from another lab, the family's independence rule. Where they disagree the row
  is flagged for John, and the score does not move until it is settled.
- **The Sentient Horizons branch is judged first by the outside reader.**
- **The weekly reading** (as on the other trackers) searches new papers and preprints against every
  open prediction, appends rows and flags, and never changes a score on its own.
- **Facts are sourced before promotion** (rule 3.3): nothing sends readers to the site while any
  record carries an open check.

## 6. What happens to Minimum Viable Mind

Its name, site address and repository carry on, at John's choice (section 9). Its experiments,
registrations, spending record and ledger stay as they are and become the "our own tests"
section. Its programme log stays the record of record for those tests. The change is what the
site leads with: the theories and the evidence, not the project's own runs. The hibernation from
2027-01-04 still stands for the project's own runs. Whether the weekly reading runs through the
hibernation is a ruling (it can run as a scheduled job, with flags waiting for John).

## 7. Where the first records would come from (all to be opened and checked before use)

Named from general knowledge in this proposal, none yet opened for it:

- The Cogitate Consortium's adversarial test of global workspace and integrated information
  theory (*Nature*, 2025), already cited with a link on the Working Positions page.
- A public database of consciousness experiments sorted by the theory each bears on (the
  "ConTraSt" database, from Liad Mudrik's group, published around 2022). If it exists as
  remembered, it is most of the support record's first draft.
- A 2023 report by Patrick Butlin, Robert Long and colleagues listing properties drawn from these
  theories that would indicate consciousness in an AI system.
- Reviews comparing the theories (for example Anil Seth and Tim Bayne, *Nature Reviews
  Neuroscience*, 2022), and proposed criteria for judging them.
- The second book's own comparison table of the theories (`sentient-horizons`,
  `editorial/second-book/08-theories-comparison-table-2026-11-09.md`) and the draft map of the
  theories waiting on John.

## 8. Cost and effort

Building the site: sessions on the subscription, as for the other trackers; the Minimum Viable
Mind site already exists with its own design, so this is a rebuild of its pages, not a new site
from nothing. The weekly reading: a scheduled job, about the size of the AGI Zeitgeist's, which
runs on API credits. Minimum Viable Mind has no API workspace or key yet, so a new one is proposed
to John, with an estimate before any spend. The first scoring pass (perhaps a few hundred
predictions and judgements, each read twice) is the largest piece of work and would come to John
with an estimate first.

## 9. Rulings for John

1. ~~Go or no go~~ **Ruled 2026-11-20: "Go, in stages, as above."** The four stages and their stop
   conditions are in section 10.
2. **The name: ruled 2026-11-20, "Keep Minimum Viable Mind, mark the rename reopened".** John first
   chose "Consciousness on Trial" the same day ("Go with Consciousness on Trial"), then withdrew it
   after discussing why a rename might or might not be right. The tracker keeps the name Minimum
   Viable Mind. The rename stays open to be raised again, for example by the cold-reader test in
   section 11. **The address is still open.** See section 11.
3. **The headline number: ruled, "A, tested at all".** *(ruled, John; recorded 2026-11-21; wording the
   master session's.)* The share of distinguishing predictions tied to core claims that at least one
   counted study has tested (section 3). Weakest steps, stated to John: it measures how widely the theories have been tested, not how firmly, so the card must say "tested
   at all", and the support bars carry the strength; and it can fall when the field adds predictions, and
   the page explains that the first time it happens.
   The trunk's question (section 3) was not part of this ruling.
4. **The first set of theories: the test ruled 2026-11-20, "Yes, as you lean"; the list itself still
   to be ruled.** The session's recommendations, in its wording. (a) A theory gets a branch if it says
   what makes a system conscious (not only what goes with it), its proponents still publish it, it is
   stated in a publication by its proponents that can be quoted, and it appears in at least two of
   the comparison sources opened at stage 1 (Doerig, Schurger and Herzog 2021; the ConTraSt
   database; Butlin, Long and colleagues 2023; Seth and Bayne 2022). The Sentient Horizons account
   is in by stated exception, said on the first screen. (b) A read-only session applies the test from
   opened sources and brings back the list, each entry sourced, for John to rule; the seven proposed
   branches are expected to pass but are not assumed to. (c) Predictive processing alone says how the
   brain works, not what makes a system conscious, so the branch is Anil Seth's living-body view by
   name, with predictive processing as its workings, core claims from his own publication, and its
   life claim scored as a core claim. (d) Orchestrated Objective Reduction is a branch if it passes.
   (e) Illusionism and panpsychism are not branches; each gets a note saying why (neither says which
   systems are conscious and which are not), the illusionism note naming attention schema theory as
   its nearest branch. Weakest step, stated when it was ruled: the two-sources part takes what the
   field's reviewers chose to cover, so it favours established theories over new ones; the yearly
   review is where that is corrected.

   **The list: ruled 2026-11-20, "Yes, ten".** A read-only research session applied the test from
   opened sources (report: the master session's notes, `2026-11-20-theory-list-test.md`), with
   Seth and Bayne's full text read after John signed in to Nature himself. Read strictly (a source
   counts when it gives the theory a table row, a section of its own, or names it in its summary),
   nine theories pass: global workspace theory; integrated information theory; higher-order
   theories, as one entry; recurrent processing theory; Anil Seth's living-body view; attention
   schema theory; the sensorimotor theory (O'Regan and Noë), not on the expected list;
   Orchestrated Objective Reduction; and Damasio's feeling-based theory ("Self comes to mind").
   With the Sentient Horizons account that is ten entries, one over the tracker pattern's limit of
   four to nine (rule 2.1). John raised the limit to ten for this tracker, the session's and the
   master's lean, so every theory that passes the ruled test stays in and a weak one shows as weak
   in its scores. Weakest step, stated when it was ruled: the limit was raised to fit the list, a
   precedent for the other trackers. Out: unlimited associative learning (its proponents call it a
   marker of when consciousness evolved, not an account of what makes a system conscious, so it
   fails part 1), the midbrain theory (one source only, read strictly), and the other rows of Seth
   and Bayne's table. Still open, needed before those theories are scored at stage 3: which
   publication supplies the core claims where there are two (attention schema theory, 2015 or the
   wider 2026 version; Seth's view, his 2025 paper or *Being You*; Damasio, the 2023 paper or the
   2010 book).

   **Core-claim sources: ruled 2026-11-21, "Yes, latest same theory".** *(ruled; wording the master
   session's.)* A theory's core claims come from its proponents' most recent full statement of the
   same theory. A later work that widens or renames it into something new is a different theory and
   does not replace it. Applied:
   - Seth's view: Seth 2025, "Conscious artificial intelligence and biological naturalism",
     *Behavioral and Brain Sciences*.
   - Damasio: Damasio and Damasio 2023, "Feelings are the source of consciousness", *Neural
     Computation*.
   - Attention schema theory: Graziano and Webb 2015, *Frontiers in Psychology*. Graziano 2026
     (*PNAS*) widens it into "a more general schema theory". Testable attention claims from 2026 can
     enter as dated predictions.

   Weakest step, stated to John: "widened or updated" is a judgement, and the 2026 paper has been seen
   only in summary. The core claims themselves are not fixed yet; that is stage 3 work.
5. ~~The three scores and their formulas~~ **Ruled 2026-11-20 ("Yes to all five"):** core claims
   fixed from one named source; study weights by counted protections; no support score before two
   separate groups; core-claim predictions count double; a failure stands. See section 4.
6. ~~The ranking rule~~ **Ruled 2026-11-20 ("Yes to all six"):** three groups; the bar is more
   than half the core claims testable; ordered by support; ties to the greater weight of evidence;
   a shared rank unless the order survives reversing any one study; theories the evidence goes
   against stay in. See section 4.
7. **The second reader: ruled 2026-11-20, "Yes, as you lean".** The session's recommendations, in
   its wording. (a) The second reader is Google's Gemini, its strongest version on offer at the time
   of reading. (b) It reads blind: it gets the prediction, the study and the wording of what counts
   for and against, never the first reader's answer, so the stage 2 stop condition (disagreement on
   more than a third of judgements) measures something, and the outside reader's judgement on every
   Sentient Horizons row is a true first reading. (c) The exact model version is recorded on every
   judgement, and a change of version is logged. (d) Stage 2 stays without spend if Gemini's free
   tier covers the model (the material is public papers, so nothing private goes to Google); if it
   does not, an estimate with a ceiling comes to John before any call. Weakest step, stated when it
   was ruled: the two models learned from much of the same writing and can share a mistake, so
   agreement shows the rules apply the same way twice, not that a judgement is right. The partial
   answer, to be settled once the pilot shows how many judgements there are, is John reading a
   random sample of agreed judgements as well as every disagreement, by a stated rule for drawing it.
   *(ruled, 2026-11-20, John: "Yes, that sample"; wording the master session's.)* **The sample:**
   every judgement both readers agreed on that sits on a Sentient Horizons row, plus half of the
   other agreed judgements (rounded up), drawn at random, with the seed and the drawing method written
   into the record and committed before the draw, so anyone can repeat it. The reason for half: if one
   agreed judgement in ten were wrong, reading half gives about an 80% chance of seeing at least one.
   Weakest step: his time. (Method and seed: `scripts/tracker_spot_check.py`, seed 20261120.)
8. **Whether the weekly reading runs through the hibernation** from 2027-01-04.
9. **The API workspace and key** for the weekly reading, with a cost estimate before any spend.

## 10. The stages (go ruled by John on 2026-11-20: "Go, in stages, as above.")

The stages were the session's recommendation, put to John with three alternatives (all at once;
not yet; no). He chose this one. Each stage has a condition that stops it and brings it back to him.

1. **Feasibility check, no cost.** Open the sources section 7 leans on (the database of experiments
   sorted by theory, the 2023 report on signs of consciousness in AI systems, the reviews comparing
   the theories) and confirm the evidence base exists and can be used. *Stops if* it does not, and
   comes back to John with what building the evidence record by hand would take.
2. **A pilot on three theories, no API spend.** Score global workspace theory and integrated
   information theory end to end (the Cogitate test gives both real data), and the Sentient Horizons
   account, under the rules of section 4. *Stops if* the two readers disagree on more than a third
   of the outcome judgements: the rules could not then be applied the same way twice as written, and
   they come back to John. Before it starts: the first list of theories (ruling 4) and the second
   reader (ruling 7).
3. **The remaining theories and the site**, built and not announced. Before it starts: the
   headline (ruling 3) and the name and address (ruling 2).
4. **The weekly reading**, once John has ruled on the API workspace with a cost estimate (ruling 9)
   and on whether it runs through the hibernation (ruling 8).

Stages 1 and 2 can realistically finish before the hibernation of 2027-01-04. Stage 3 may run past
it, in which case it waits. Nothing is announced while any fact waits to be checked (tracker
pattern rule 3.3).

## 11. The name and the address (name kept, rename reopened, address open: John, 2026-11-20)

Raised by John on 2026-11-20: the site is now at a subdomain of sentient-horizons.com. He looked
up the name on his Cloudflare account the same day: the .com, .org and .net addresses for
"minimumviablemind" are taken; .app and .dev are offered at $8.20 for the first year (renewing at
$14.20 and $12.20); .io at $32; .ai at $160 for a two-year minimum.

The session's view: the address follows the name, so the name comes first, and nothing is bought
before it. Every other tracker in the family has a .com in its own name. A tracker of the theories
of consciousness arguably needs a name that says its subject (title rule 2, "name the subject"),
which "Minimum Viable Mind" does not. Its own tests can keep the name at the present subdomain.
Candidate names, with their .com addresses unregistered in the public registry on 2026-11-20 (a
lookup of the registry; whether Cloudflare offers each at the standard price is not checked):
Consciousness on Trial (consciousnessontrial.com), The Consciousness Scorecard
(consciousnessscorecard.com), The Inside Test (theinsidetest.com), What Is It Like to Be
(whatisitliketobe.com). Two were set aside: thehardquestion.com is taken, and the name would argue
with the second book, which calls the hard problem the wrong question; "ledger" is a word the
positions page keeps out of public text. A domain is a new spend, which John makes himself.

**What was ruled, in order.**

1. John chose Consciousness on Trial, the session's lean, on 2026-11-20 ("Go with Consciousness on
   Trial"). *Withdrawn the same evening.*
2. He then said he was not sold on the rename and still thought Minimum Viable Mind was the right
   name, and asked for the case for renaming to be argued. The session's case, both ways: for
   keeping, every theory of consciousness is an answer to the question the name asks (what is the
   least a system needs to have a mind), so the name can be the question at the top of the site;
   the site, the record, the paper and the links from the positions page already carry it; and it
   is distinctive. For renaming, the word "consciousness" is not in it, so a stranger cannot tell
   the subject or find it by searching; it echoes "minimum viable product", startup vocabulary the
   plain-language rule asks to translate; and a name about building a mind may read as taking a
   side. The session changed its lean to keeping the name, with the subject said in the line above
   the title on the first screen (for example: "What is the least a mind needs? Every theory of
   consciousness gives an answer. Here is how each is holding up."), and page titles and link
   previews carrying the words people search for.
3. John ruled: "Keep Minimum Viable Mind, mark the rename reopened." The name stays. The rename is
   not closed: it can be raised again on evidence.

**A test that could reopen it.** Show the first screen, with the line above the title, to two
readers who know nothing of the project, one on a Claude model and one on a Gemini model, as in
the cold-reader audit of all eight sites on 2026-11-20, and ask each what the site is about. If
they read it as a site about the theories of consciousness, the name holds; if they read it as an
AI product or a build log, that is the case for renaming, on evidence. Not yet run; it belongs in
stage 3, once the first screen exists.

**The address.** Open. minimumviablemind.com, .org and .net are taken (John's Cloudflare lookup of
2026-11-20); the site stays at its present subdomain of sentient-horizons.com until John decides.

## 12. Stage 1 result, 2026-11-20: the evidence base exists, with gaps

Read the same evening by a research session, from pages it opened (sources below). Stage 1's stop
condition was that no usable evidence base exists. One does, so stage 1 passes; what it lacks
shapes stage 2.

**What exists.**
- **The ConTraSt database** of experiments sorted by theory (Yaron, Melloni, Pitts and Mudrik,
  *Nature Human Behaviour* 6, 593–604, 2022, https://doi.org/10.1038/s41562-021-01284-5; free
  preprint https://www.biorxiv.org/content/10.1101/2021.06.10.447863v1; site
  https://contrastdb.tau.ac.il). A 2021 snapshot (412 experiments, https://osf.io/avz8b/) and a live
  CSV export (481 experiments from 432 papers) can both be downloaded. Each experiment is marked as
  supporting or challenging each of four families (global workspace, integrated information,
  higher-order, and first-order with predictive processing), and as designed to test a theory,
  only mentioning one, or interpreted afterwards (175, 121 and 185 of the 481). The site states
  the data licence as CC-BY-SA-4.0.
- **Doerig, Schurger and Herzog, "Hard criteria for empirical theories of consciousness"**
  (*Cognitive Neuroscience* 12, 41–62, 2021, https://infoscience.epfl.ch/record/278952, open
  access): four criteria, and a table rating 13 theories against them, which the authors call their
  interpretation. A ready starting point for the testability score.
- **The Cogitate Consortium's adversarial test** (*Nature* 642, 133–142, 2025,
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12137136, CC BY 4.0): predictions registered in advance
  with pass or fail criteria (https://osf.io/92tbg/). It is the best material for the stage 2 pilot.
- **Butlin, Long and colleagues' indicators of consciousness in AI systems** (arXiv 2308.08708,
  2023; published in *Trends in Cognitive Sciences*, 2025): fourteen indicator properties drawn from
  five theories, a starting point for predictions about machines.
- **Five more adversarial collaborations funded by the Templeton World Charity Foundation**, none
  with published results found (first-order against higher-order; integrated information against
  predictive processing; rival higher-order theories; global workspace against integrated
  information in animals).
- **No existing site or living review ranks the theories themselves** that the search found.

**What it lacks, and what that means for stage 2.**
1. **No record of advance registration, and no prediction records.** Each ConTraSt verdict is the
   original authors' own reading. Under the scoring rules, most of its rows would carry weight 1.
2. **Most studies interpret their results afterwards.** ConTraSt's own paper says so, and its
   tallies lean heavily one way (for example, by the research session's count from the live export,
   integrated information 82 for against 7 challenging, global workspace 166 against 46).
   **Ruled by John on 2026-11-20: "Yes to all four".** The four rules were the session's
   recommendations; the wording is the session's. What matters is when the prediction was made,
   not how the study was framed:
   1. *(ruled)* **A prediction counts for a study if the theory's proponents fixed it before they
      could have known the study's result:** before the registration, for a study registered before
      its data were collected; before its earliest public appearance (preprint or publication), for
      any other study; before that data first appeared, for a study reanalysing earlier published
      data. The ban on stating and testing in the same paper stays. *(ruled, 2026-11-20, John: "Yes,
      that test"; wording the master session's.)* **This replaces the wording recorded just below for
      his earlier ruling "Yes, count it"** ("before the study's data were collected"), which is kept
      struck through for the record; what that ruling settled (a registration's predictions count for
      the study that registered them) stands. Whether an earlier passage commits the theory to the
      exact test is a separate judgement, read by both readers and settled by John.
      ~~A study counts toward a prediction if that prediction was fixed, by the theory's
      proponents, in a dated record made before the study's data were collected, whether a
      publication or a registration.~~ *(ruled, 2026-11-20, John: "Yes, count it"; wording the
      master session's; replaced the same day as above.)* What decides is when the record was fixed, not when it became public. The
      ban on a paper that states a prediction and tests it in the same paper stays. So the Cogitate
      registration's predictions count for the Cogitate study. Weakest step, stated to John: a
      prediction becomes the theory's once its proponents sign it into a registration, even if it was
      derived for that study (the offset ignition), and under "a failure stands" it counts. (Raised by
      the stage 2 pilot, which found that the first wording, below, left most of the Cogitate study
      out.) A study that counts counts at its ordinary weight under the protections rule of section 4.
      *Replaced wording, kept for the record:* ~~A study counts toward a prediction only if that
      prediction was on record, in a dated publication by the theory's proponents, before the study
      first appeared. The study's own framing does not decide it: a study that explained its result
      afterwards still tests a prediction the theory had already made, and a study that says it set
      out to test a theory tests nothing if the prediction was first written in the same paper.~~
   2. *(ruled)* **A study that fails this is listed beside the prediction**, marked "explained
      afterwards, not counted", and moves no score.
   3. *(ruled)* **When the dates or the commitment are unclear, the study is not counted.**
      *(Applied by John, 2026-11-20, "Yes, as you lean": when the two readers split on whether an
      earlier passage committed the theory to the test, the commitment is unclear, so the study is not
      counted for that prediction. Wording the master session's.)* Not
      counting is the safe direction, because the failure this guards against is a theory gaining
      support it did not earn. Known cost, stated when it was ruled: some genuine tests of
      loosely stated older theories will be left out. Whether an earlier statement committed the
      theory to a result is a judgement, made as its own record and read by both readers.
      A prediction dates from the first publication by the theory's proponents that states it; a
      study dates from its earliest public appearance (its registration, its preprint or its
      publication, whichever came first). *(Note from the stage 2 pilot, 2026-11-20, not a ruling: under the
      ruled rule 1 above, what the prediction is compared with is when the study's data were
      collected, so this sentence's dating of a study by its earliest public appearance no longer
      decides whether it counts. The wording is left for the master session to bring into line.)*
   4. *(ruled)* **ConTraSt's "designed to test, mentioned, or interpreted afterwards" field is a
      pointer** for which studies to check first, not the rule.
3. **The licence is share-alike.** ConTraSt's data is under CC BY-SA 4.0, so anything built from
   its data must be shared under the same terms; Minimum Viable Mind's data, like the AGI
   Zeitgeist's, is under CC BY 4.0 (`LICENSE-DATA`). The tracker needs only ConTraSt's list of
   studies: its verdicts are the authors' own readings, which the rules already set aside (every
   judgement is made independently by two readers, and whether a study counts turns on when the
   prediction was made, which ConTraSt does not record). **Ruled by John on 2026-11-20: "Yes to all
   three".** The rules were the session's recommendations; the wording is the session's.
   1. *(ruled)* **ConTraSt is used as a list of studies to read.** Every record is built from the
      paper itself (its citation, its dates, what it found, and the tracker's own judgement), so the
      tracker's tables stay under CC BY 4.0.
   2. *(ruled)* **ConTraSt is credited** on the method page and on every record found through it.
   3. *(ruled)* **At stage 3, a separate file shows ConTraSt's own verdicts beside the tracker's**,
      under ConTraSt's licence (CC BY-SA 4.0), credited, and moving no score, because the gap between
      what authors said of their own studies and what an independent reading finds is worth showing.
      (The session had suggested deciding this at stage 3; John said yes now.) Any of ConTraSt's own
      fields the tracker copies go in that file and nowhere else.

   Not legal advice, stated when it was ruled: whether taking a bare list of studies from a
   database counts as using it under its licence is not certain (some countries protect databases
   as such, and CC 4.0 licences are written to cover that). The tracker acts as if it does, which
   for a reading list asks only for the credit given anyway.
4. **Coverage.** Attention schema theory, Seth's living-body view and the Sentient Horizons account
   have no category; studies since 2022 are barely added (none from 2026); Cogitate is not in it.
   These are built by hand.
5. **Some sources were read only in part.** The Nature articles needed a sign-in, and Seth and
   Bayne's review was read only in its abstract. Before stage 2 relies on any of them, their full
   text is opened (John's Nature subscription may cover the Nature pieces, through a sign-in he makes
   himself).
