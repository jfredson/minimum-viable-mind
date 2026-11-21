# Stage 2 pilot: three theories scored end to end, one reader so far

*Written 2026-11-20 by the stage 2 working session, for the master session to put to John. A copy
is in the master's notes folder. Nothing was spent, nothing was published, deployed, merged or
pushed, and the second reader (Google's Gemini) has not been called.*

## In short

- **The records and the scoring script are built and committed** on the branch
  `claude/stage2-pilot-2026-11-20-7c94d9`, in `data/tracker/` (layout in `data/tracker/README.md`)
  and `scripts/tracker_scores.py`. Every number below comes out of the script, from the records alone.
- **My reading of every judgement is done** (43 judgements), and **43 blind packets are ready** for
  the second reader in `data/tracker/packets/`. A check in `scripts/tracker_packets.py` confirms no
  packet contains any part of my readings.
- **The second reader needs money.** The strongest Gemini model, Gemini 4 Carbon, is not on the free
  tier. Reading all 43 packets would cost about **$1.40 to $3.50** at today's price, which **doubles
  on 2026-12-01** (to about $2.75 to $7). A ceiling of **$10** covers every case. Details in section 5.
- **Two rules gave results John may not have intended, and I applied both as written** (section 2).
  The bigger one: the rule on when a prediction was made leaves most of the Cogitate study out of the
  scores, including every one of its tests of integrated information theory.
- **One reader's scores** (section 4): global workspace theory 44 on support, integrated information
  theory 75, sharing first place because one study could swap them; the Sentient Horizons account
  untested, with half its core claims sharp enough to test. These are not results yet. They rest on
  eight counted outcomes from four studies, all read by one reader on one model.

## 1. What was built, with counts

| | global workspace | integrated information | Sentient Horizons | all |
|---|---|---|---|---|
| core claims (quoted, fixed before scoring) | 5 | 5 | 4 | **14** |
| predictions | 8 | 8 | 5 | **21** |
| outcome judgements that count | 6 | 2 | 0 | **8** |

**Where the core claims come from.** Global workspace theory: Mashour, Roelfsema, Changeux and
Dehaene, *Neuron*, 2020. Integrated information theory: Albantakis, Tononi and colleagues,
"IIT 4.0", *PLOS Computational Biology*, 2023. The Sentient Horizons account: the live Working
Positions page (latest revision 2026-10-24), its predictions taken from the "What would change my
mind" sections, as the kickoff proposal says.

**Studies: nine records.**
- Counted toward at least one prediction (4): the Cogitate Consortium's adversarial test
  (*Nature*, 2025); Bellet and colleagues' monkey prefrontal decoding study (2022); Bandara, Rowe and
  Garrido's computer modelling of an inattentional-blindness dataset (2025); Dellert and colleagues'
  study of hearing without report (2025).
- Not counted (5): Coppola and colleagues' network study (2021), because it tests no prediction
  either theory's proponents stated, though ConTraSt lists it as designed to test both; the
  no-report study by Hatamimajoumerd, Ratan Murty, Pitts and Cohen (2022), because I could not open
  it (the publisher showed a robot check, which I did not get past); and three studies the Working
  Positions page cites (on cutting copies of eye-movement commands in monkeys, 2002; a man who lost
  body-position sense, 1992; Henry Molaison's memory loss, 1957), because each appeared long before the
  prediction it bears on.
- How the sample was chosen, so it can be checked and redone: the Cogitate study (named in the
  brief), then the five most recent ConTraSt rows marked as designed around both theories, then the
  studies the Working Positions page cites. ConTraSt served only as a reading list; every record was
  built from the paper itself, and ConTraSt is credited.

**Judgements: 43**, each its own record with its passages: 8 outcome judgements (did the study come
out for, against or mixed?), 14 commitment judgements (was the prediction on record before the
study appeared?) and 21 testability judgements (could the prediction fail, and does it separate the
theory from a rival?). The brief asked for two readers on the outcomes; rule 2.3 asks for two on the
commitments; I added the testability judgements too, because they set the testability score and,
for John's own account, that is where the conflict of interest bites hardest. If the master would
rather send only the outcomes and commitments, that is 22 packets, not 43.

**Verify list: 8 open entries** (`data/tracker/verify.toml`), each a statement resting on a source I
did not open or opened only in part. Nothing can be promoted while any stays open.

## 2. Two rules that gave results John may not have intended

I applied both as written and did not patch either. Both are for John.

**A. The rule on when a prediction was made leaves most of the Cogitate study out.** The rule (the
after-the-fact rules of 2026-11-20, kickoff section 12, rule 2.1) says a study counts only if the
prediction was on record, in a dated publication by the proponents, *before the study first
appeared*, and rule 2.3 says a study first appears at its registration if that comes first. The
Cogitate study's registration (on the Open Science Framework, 2019-01-16) is where the two theories'
proponents first wrote down most of its predictions. So under the rule as written, the study tests
nothing for those predictions: they were "first written in the same paper", which is exactly the case
the rule excludes. I searched for earlier statements:

- Three global workspace predictions were on record earlier, in a paper by Dehaene and colleagues
  (*Current Opinion in Neurobiology*, published online 2013-12-29): that seen content is represented in prefrontal
  cortex, that consciousness comes with a late, sudden rise of prefrontal and parietal activity, and
  that it comes with long-distance synchrony. Those count.
- Two global workspace predictions were not: the second "ignition" when a stimulus disappears, and
  the quiet holding of a lasting percept in between. The study's own papers derive them from other
  authors' work on prediction in the brain. The first of these is the failure the consortium calls the
  biggest challenge to the theory. It does not count.
- None of the three integrated information predictions could be dated before the registration from
  sources I could open. A 2017 paper by the same authors argues for a posterior "hot zone" but never
  names the theory. Two 2016 papers in *Nature Reviews Neuroscience* might state them, but are behind
  a sign-in. So the hot-zone prediction, the prediction of sustained activity, and the synchrony
  prediction that the consortium calls the theory's most direct failure all go uncounted.

The effect on the scores is large. With the rule as written, integrated information theory's
support rests on two small studies without registration, and reads 75. If the registration's
predictions counted (reading "on record before" as "on record before the data came in"), the
Cogitate study would add the consortium's own verdicts at its full weight. Using those verdicts as
a rough guide, not as readings: integrated information theory would fall to about 69 and global
workspace theory to about 36, and they would still share a rank. The rule's purpose, as the
proposal states it, is to stop a theory gaining support it did not earn after the fact. A
registration made before any data were collected, and agreed with the rival camp, is the opposite
of after the fact. So the rule's wording and its purpose pull apart on the one study the pilot was
built around. **For John: should a prediction first written in a study's own registration, by the
theory's proponents, before data collection, count for that study?** Two smaller points ride on
the same answer. A study in the pilot (Bandara and colleagues, 2025) reanalyses data published in
2015, before the prediction it tests was stated; the rules date the study, not the data, so it
counts. And the registration's public date is unknown: the Open Science Framework shows only when it
was created. So whether Bellet and colleagues (2022) count for integrated information theory is
"unclear", and that study is not counted.

**B. The ranking bar does not say whether the prediction must also separate the theory from a
rival.** Ranking rule 2 says a theory is ranked when "more than half its core claims come with a
prediction that could fail". The testability score, by contrast, also requires the prediction to
separate the theory from a rival. Read literally, the bar does not. The difference decides which
group John's own account falls in:

- Literal reading (used for the main result): three of the account's four core claims have a
  prediction that could fail, so it is past the bar. It goes in "testable, too little tested to rank".
- Stricter reading (computed beside it): only two of four have one that also separates the account
  from a rival. Two of four is not more than half, so it goes in "not yet defined sharply enough to
  rank".

Nothing else moves between the two readings: both other theories are past the bar either way.
**For John: does the bar need a prediction that separates, or only one that could fail?**

Three smaller gaps, which I handled as stated and which John may want to rule on later:
- **No "does not bear on it" outcome.** The ruled outcomes are for, against and mixed. Bellet and
  colleagues showed prefrontal neurons carrying detailed picture information, but could not say whether
  the monkeys saw the pictures, so the result neither supports nor contradicts a prediction about what
  is seen. I scored it "mixed", which pulls the score toward the middle. A fourth outcome that counts
  for nothing would be cleaner.
- **"No study has touched".** The left-to-test score counts a prediction as touched only if a
  *counted* study tested it. A study that tested it but was not counted (the Cogitate offset test)
  leaves it untouched. The other reading is possible.
- **Silence is not a contrary prediction.** I judged that a prediction separates a theory from a rival
  only when the rival predicts something different, not when it is silent. I applied this unevenly on
  the account's two predictions about the split (see section 6), which is the clearest place for the
  second reader to test me.

## 3. The Sentient Horizons account

Its core claims (from the Working Positions page): experience is the binding of the just-past into the
moment now, seen from the inside (the central bet); a point of view comes from the split between what
a system does and what happens to it; a boundary, mattering, self-awareness and kept memory enrich
experience without switching it on; and no experience is at zero on any of the three axes.

- **Testability 50.** The split prediction and the enriching-features prediction could fail and
  separate the account from a rival. The central bet names a losing condition but no study that could
  show it, so it could not fail. The no-bare-awareness prediction could fail, but integrated
  information theory also says every experience has structure, so it does not separate them.
- **Support: too little tested to score.** No study counts. Every study the page cites appeared before
  the predictions (2026-10-24), and the distinguishing part of the split prediction, that response to
  new, unrelated events degrades, has never been tested, as the page itself says.
- **Left to test 100.**
- **Group:** testable, too little tested to rank (literal bar), or not yet defined sharply enough to rank
  (stricter bar). Section 2B.

That matches the proposal's first guess, except that testability came out lower than "high", because
two of the four core claims carry no prediction that is both able to fail and separating.

**Where the unruled proposal would change this.** The proposal waiting for John on the positions
(the account stated in one sentence) has a choice about the workspace, its Choice C. Under its lean
(C1, keep the workspace as a job brains do by broadcasting), the core claims do not change. Under C2
(experience needs broadcast in the brain's sense), the account would gain a core claim whose
predictions are global workspace theory's own. Those would separate the account from integrated
information theory but not from global workspace theory, and testability would rise. Its one-sentence
statement (P2) would also fold "one space that the whole system can use" into the central bet. No
record depends on the proposal.

**The second reader goes first here.** On all five of the account's testability judgements, Gemini's
reading will be the first of record (ruling 7b). My readings on those rows are marked as second, and the
validator refuses the file if they are not.

## 4. The scores my reading alone gives (one reader, Claude Opus 5.5; not results)

| theory | testability | support | left to test | group |
|---|---|---|---|---|
| Global workspace theory | 60 | **44** (6 outcomes, 4 studies, 4 groups, total weight 34) | 50 | ranked, the evidence so far leans against it |
| Integrated information theory | 60 | **75** (2 outcomes, 2 studies, 2 groups, total weight 8) | 86 | ranked |
| The Sentient Horizons account | 50 | too little tested to score | 100 | testable, too little tested to rank |

**Ranking:** integrated information theory and global workspace theory **share first place**. Reversing
the outcome of the Dellert study alone would swap them, so by ranking rule 5 they are shown as tied.
That is the cost the rule accepted when it was ruled: early on most theories come out tied.

**The headline**, computed provisionally because ruling 3 is still open: 5 of the 13 distinguishing
predictions across the three theories have been tested by a counted study (38%).

How to read the support numbers: 50 means the evidence is even. Global workspace theory's 44 comes
from the Cogitate study at weight 4: prefrontal content mixed, onset ignition for, prefrontal synchrony
against. Then Bellet's study, mixed at weight 1; the modelling study, mixed at weight 2; and the
hearing study, against at weight 2. Integrated information theory's 75 is one study for (hearing) and
one mixed (modelling), both at weight 2, and it would read very differently if the Cogitate tests
counted (section 2A).

## 5. The second reader: calls, cost, and the free tier

- **Calls: 43**, one per packet: 8 outcome, 14 commitment, 21 testability. Of these, 5 are the
  account's rows, which Gemini reads first. Only 22 if testability is left out.
- **Model:** Gemini 4 Carbon, which Google's pricing page calls "our most capable reasoning model"
  (ruling 7a: the strongest version on offer). Source: Google, Gemini Developer API pricing,
  https://ai.google.dev/gemini-api/docs/pricing, read 2026-11-20 (the address now redirects to
  aistudio.google.com/docs/pricing).
- **Free tier: no.** The page says Gemini 4 Carbon "is not available on the Free tier" (and the same
  for Gemini 4 Argon and Neon). The free tier covers smaller models only (Gemini 4 Hydrogen, Gemini 3.8
  Flash and below), and on the free tier Google uses the content to improve its products. A free run
  would mean a weaker model than ruling 7a names, so it would need John's ruling too.
- **Price:** $2 per million input tokens and $10 per million output tokens, thinking included, through
  2026-11-30; **$4 and $20 from 2026-12-01**. The batch route costs half.
- **Estimate:** the 43 packets are about 43,000 input tokens in all. Output is the uncertain part,
  because thinking tokens are billed: at 3,000 per call the run costs about **$1.38** now ($2.75 from
  December); at 8,000 per call, **$3.53** now ($7.05 from December). The batch route halves each figure.
  A **ceiling of $10** covers every case. Running before 2026-12-01 halves the cost.
- **Who pays:** this is Google billing, not the Anthropic credits, so under the workspace rules it is
  out of pocket and needs John's go first. The key exists in the project's `.env` file (checked by name
  only, value not read); whether its Google project has billing switched on was not checked.
- **Nothing private goes to Google:** the packets hold public papers' passages, the public positions
  page, and the records' own wording.

## 6. Every place a judgement felt unsure (26 of the 43)

Each has its reason written in its record (`unsure_why` in `data/tracker/judgements.toml`). In plain terms:

**Outcomes (6 of 8).**
- *Cogitate, seen content in prefrontal cortex: mixed.* The category of what was seen could be decoded
  there, but its orientation was found by only one of three methods, and weakly. Whether that one
  method meets the registered criterion decides between "mixed" and "for".
- *Cogitate, the rise of activity at onset: for.* Every stimulus was seen, so the study cannot show a
  rise that unseen stimuli lack. And I split the onset response (on record since 2013) from the offset
  response (first written in the registration). Someone who will not split them would read "against".
- *Cogitate, prefrontal synchrony: against.* The measure agreed in advance found none. A measure
  chosen afterwards found some, and I gave it less weight.
- *Bellet, prefrontal content: mixed.* It cannot tell seen from unseen (section 2).
- *Dellert, fronto-parietal rise when sounds are heard: against.* Brain scanning is slow, and the
  comparison is between groups of people, so a brief rise could be missed. The proponents' own
  wording ("regardless of the stimulus modality or paradigm") does not exempt it.
- *Dellert, posterior hot zone: for.* The study found no prefrontal activation, which is weaker than
  showing that prefrontal cortex adds nothing. And the hot zone was described for vision, not hearing.

**Commitments (9 of 14).**
- *Did the 2013 paper commit the global workspace theory to content in prefrontal cortex even when the
  stimulus is irrelevant to the task?* The same paper hedges on exactly that.
- *Did it commit the theory to synchrony between prefrontal cortex and the areas holding the content?*
  It names long-distance synchrony, but not which two places.
- *The offset ignition and sustained activity:* not counted because no earlier statement was found;
  an unopened paper (the 2016 one, or Dehaene's 2014 book) might hold one.
- *The posterior hot zone, for the Cogitate and Bellet studies:* unclear. Settled by opening the 2016
  papers, or by finding when the registration went public.
- *The hot zone as an "auxiliary" prediction, for the two later studies:* I read it as committing the
  theory, because its proponents signed it.
- *The reanalysis of 2015 data:* counted, because the rules date the study, not the data.

**Testability (11 of 21).**
- *Top-down signals in the workspace theory:* named as a main idea but never given a test by its
  proponents. The test wording is mine.
- *The late start of consciousness:* I found no rival that says it starts earlier. Recurrent
  processing theory is often read that way, but I found no statement by its proponents in what I opened.
- *Quiet holding between ignitions:* its rival's sustained activity is in a different part of the
  brain, so the two are not strictly opposite.
- *The hot zone:* whether an "auxiliary" prediction is tied to a core claim. If it is not, it counts
  half as much.
- *High integrated information when awake and dreaming:* the workspace theory also predicts
  disruption in sleep and anaesthesia, so I said it does not separate them. Dreaming might.
- *Quiet but working neurons, and connection strength (two integrated information predictions):* the
  separation from the workspace theory is my inference from two papers that never discuss each other.
- *The account's central bet:* someone could take its losing condition as enough to make it able to fail.
- *The account's split prediction:* I said it separates from the workspace theory, because that theory
  ties responding to new things to the workspace, not to the split. That is reading a prediction into
  the theory's silence, which I refused to do for the workspace theory's own late-start prediction. By
  the stricter standard it would not separate, and the account's testability would fall to 25.
- *The account's no-split prediction:* I read this one strictly (does not separate), which is
  inconsistent with the previous one. The second reader should test both.
- *The account's enriching features:* separating it from Damasio's theory rests on a secondary
  quotation, and "mattering" and Damasio's "feeling" may not be the same thing.

## 7. What was not opened

- The two 2016 *Nature Reviews Neuroscience* papers by Tononi, Koch and colleagues. John can sign in to
  Nature himself in the browser pane, and his password is never typed for him. They could bring the
  Cogitate study's integrated information tests into the scores (verify entry `v-tononi-koch-2016`).
- The 2022 no-report study by Hatamimajoumerd and colleagues (robot check).
- The Cogitate study's Extended Data Table 1 and Fig. 7, which are images; the criteria come from the
  main text.
- The journal version of the Dellert study; I read the preprint.
- The papers the Working Positions page cites; they move no score.

## 8. Next, for the master to put to John

1. **The spend:** up to $10 on Gemini 4 Carbon for the 43 readings, ideally before 2026-12-01, when the
   price doubles. Or 22 readings without the testability judgements. Or a free run on a weaker model,
   which departs from ruling 7a.
2. **Rule A:** does a registration written by the proponents before data collection put a prediction
   "on record before" the study? (Section 2A.)
3. **Rule B:** does the ranking bar need a separating prediction? (Section 2B.)
4. Optionally, the 2016 Nature papers, opened by John's own sign-in.

The stage 2 stop condition, the readers disagreeing on more than a third of the judgements, can only be
checked once the second reading is in. If rule A is changed, a few of the Cogitate rows get outcome
judgements of their own first (about five more packets).
