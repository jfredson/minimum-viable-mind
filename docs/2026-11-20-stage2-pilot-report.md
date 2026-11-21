# Stage 2 pilot: three theories scored end to end, one reader so far

*Written 2026-11-20 by the stage 2 working session, for the master session to put to John. Revised
the same evening after John ruled on the two rules the first version raised ("Yes, count it" and
"Yes, must separate"). A copy is in the master's notes folder. Nothing was spent, nothing was
published, deployed, merged or pushed, and the second reader (Google's Gemini) has not been called.*

## In short

- **The records and the scoring script are built and committed** on the branch
  `claude/stage2-pilot-2026-11-20-7c94d9`, in `data/tracker/` (layout in `data/tracker/README.md`)
  and `scripts/tracker_scores.py`. Every number below comes out of the script, from the records alone.
- **John's two rulings are applied and recorded** in the kickoff proposal (section 12, rule 2.1;
  section 4, ranking rule 2), each marked *(ruled)* with his words, in the master's wording.
- **My reading of every judgement is done** (48 judgements, five of them added for the Cogitate
  outcomes the first ruling brings in), and **48 blind packets are ready** for the second reader in
  `data/tracker/packets/`. A check in `scripts/tracker_packets.py` confirms no packet contains any
  part of my readings.
- **The second reader still needs money.** Gemini 4 Carbon, the strongest model, is not on the free
  tier. All 48 readings would cost about **$1.50 to $3.90** at the current price, and the price
  **doubles on 2026-12-01** (to about $3.10 to $7.90). The 27 outcome and commitment readings alone
  would cost about $0.90 to $2.20 now. A ceiling of **$10** covers every case. Details in section 5.
- **One reader's scores** (section 4): global workspace theory 46 on support and integrated
  information theory 57. They share first place, because one study could swap them. The Sentient
  Horizons account is "not yet defined sharply enough to rank": only two of its four core claims carry
  a prediction that could fail and that a rival predicts differently. None of these is a result yet.
  They rest on 12 counted outcomes from four studies, all read by one reader on one model.

## 1. What was built, with counts

| | global workspace | integrated information | Sentient Horizons | all |
|---|---|---|---|---|
| core claims (quoted, fixed before scoring) | 5 | 5 | 4 | **14** |
| predictions | 8 | 8 | 5 | **21** |
| outcome judgements that count | 8 | 4 | 0 | **12** |

**Where the core claims come from.** Global workspace theory: Mashour, Roelfsema, Changeux and
Dehaene, *Neuron*, 2020. Integrated information theory: Albantakis, Tononi and colleagues,
"IIT 4.0", *PLOS Computational Biology*, 2023. The Sentient Horizons account: the live Working
Positions page (latest revision 2026-10-24), its predictions taken from the "What would change my
mind" sections, as the kickoff proposal says.

**Studies: nine records.**
- **Counted toward at least one prediction (4):**
  - the Cogitate Consortium's adversarial test (*Nature*, 2025), now for all eight of its predictions;
  - Bellet and colleagues' monkey prefrontal decoding study (2022);
  - Bandara, Rowe and Garrido's computer modelling of an inattentional-blindness dataset (2025);
  - Dellert and colleagues' study of hearing without report (2025).
- **Not counted (5):**
  - Coppola and colleagues' network study (2021). It tests no prediction that either theory's
    proponents stated, though ConTraSt lists it as designed to test both.
  - The no-report study by Hatamimajoumerd, Ratan Murty, Pitts and Cohen (2022). It was not opened,
    because the publisher showed a robot check, which I did not get past.
  - Three studies the Working Positions page cites: one on cutting copies of eye-movement commands in
    monkeys (2002), one on a man who lost body-position sense (1992), and the study of Henry
    Molaison's memory loss (1957). Each was done long before the prediction it bears on.
- **Study-and-prediction pairs not counted (2):**
  - Bellet for integrated information theory's posterior "hot zone". The paper does not say when its
    recordings were made, and the record that fixed the hot-zone prediction (2019) is only three years
    older than the paper's submission, so the order is unclear.
  - Bandara for the same prediction. Its data come from a 2015 study, so they were collected before
    the 2019 record.
- **How the sample was chosen**, so it can be checked and redone: the Cogitate study first, because
  the brief names it; then the five most recent ConTraSt rows marked as designed around both theories;
  then the studies the Working Positions page cites. ConTraSt was only a reading list. Every record was
  built from the paper itself, and ConTraSt is credited.

**Judgements: 48** in all, each its own record with its passages:
- **13 outcome judgements:** did the study come out for, against or mixed?
- **14 commitment judgements:** was the prediction fixed before the study's data were collected?
- **21 testability judgements:** could the prediction fail, and does a rival predict differently?

The brief asked for two readers on the outcomes, and rule 2.3 asks for two on the commitments. I added
the testability judgements too, because they set the testability score and, since John ruled the bar
must separate, the ranking group as well. For John's own account, that is where the conflict of
interest bites hardest.

**Verify list: 9 open entries, 1 closed** (`data/tracker/verify.toml`). Each open entry is a statement
resting on a source I did not open, or opened only in part. The closed entry, when the Cogitate
registration became public, no longer matters under the ruling. Nothing can be promoted while any
entry stays open.

## 2. The two rulings, and what they changed

**Rule A, "Yes, count it".** A study now counts toward a prediction if the theory's proponents fixed
that prediction in a dated record before the study's data were collected. The record can be a
publication or a registration.
- **Cogitate.** Its registration was created on the Open Science Framework on 2019-01-16, and the
  protocol says it was frozen before data acquisition began. All eight Cogitate predictions now count.
  That brings in two workspace predictions: the offset ignition, which failed, and the quiet holding of
  the percept between ignitions, whose observable part held. It also brings in all three integrated
  information predictions: the posterior hot zone (held), sustained activity (mixed) and posterior
  synchrony (failed).
- **Bellet 2022, rechecked for integrated information theory.** Unclear, so not counted. The record
  that fixed the hot-zone prediction dates from 2019-01-16, but the paper does not say when its monkey
  recordings were made. It was submitted on 2021-01-19, and the recordings could fall on either side
  of the record.
- **An effect I had not expected.** The ruling compares the prediction with when the data were
  collected, not with when the study appeared. The Bandara study reanalyses data published in 2015,
  so it no longer counts for the hot-zone prediction, fixed in 2019. It still counts for global
  workspace theory's top-down prediction, because the proponents quote their own 1998 paper as already
  giving the workspace "descending connections". That 1998 paper was not opened; it is on the verify
  list.
- **A convention I had to adopt.** Bellet and Dellert do not date their data, and Bandara dates its
  data only as "before 2015". I read a record fixed five or more years before a study first appeared
  as fixed before its data were collected, and a shorter gap as unclear. It is a reading, not a rule,
  and is written into the header of the commitment judgements so the second reader and John can test
  it. If no undated study counted, only the Cogitate study would remain. Both theories would then rest
  on one group and fall to "testable, too little tested to rank".
- **Wording left for the master.** Rule 2.3 still says that a study dates from its earliest public
  appearance. Under ruled rule 1, that sentence no longer decides whether a study counts. I added a
  note in the proposal saying so, and left the wording to the master.

**Rule B, "Yes, must separate".** The ranking bar now uses the same test as the testability score. A
core claim counts toward the bar only if it has a prediction that could fail and that a rival predicts
differently. Only two of the Sentient Horizons account's four core claims pass that test: the split,
and the enriching features. So the account moves from "testable, too little tested to rank" to "not
yet defined sharply enough to rank". To get past the bar it needs one more core claim with such a
prediction. The open candidates are the central bet and the claim that no experience is at zero on any
axis. The other two theories pass the bar with three of five claims each.

**Three smaller gaps, still unruled, handled as stated:**
- **No "does not bear on it" outcome.** Bellet's study could not tell whether the monkeys saw the
  pictures, so I scored it "mixed", which pulls the score toward the middle.
- **What "touched" means.** The left-to-test score counts a prediction as touched only if a counted
  study tested it.
- **Silence.** A prediction separates a theory from a rival only when the rival predicts something
  different, not when the rival is silent. I applied this unevenly to the account's two predictions
  about the split (section 6).

## 3. The Sentient Horizons account

**Its core claims**, from the Working Positions page:
- Experience is the binding of the just-past into the moment now, seen from the inside (the central bet).
- A point of view comes from the split between what a system does and what happens to it.
- A boundary, mattering, self-awareness and kept memory enrich experience without switching it on.
- No experience is at zero on any of the three axes.

**How it scores:**
- **Testability 50.** The split prediction and the enriching-features prediction could fail, and a
  rival predicts differently. The central bet names a losing condition but no study that could show it,
  so it cannot fail. The no-bare-awareness prediction could fail, but integrated information theory also
  says every experience has structure, so it does not separate the two.
- **Support: too little tested to score.** No study counts. Every study the page cites was done before
  the predictions (2026-10-24). The distinguishing part of the split prediction, that response to new,
  unrelated events degrades, has never been tested, as the page itself says.
- **Left to test: 100.**
- **Group: not yet defined sharply enough to rank** (ruling B).

**Where the unruled proposal would change this.** The proposal waiting for John on the positions has a
choice about the workspace, its Choice C.
- Under its lean, C1 (keep the workspace as a job brains do by broadcasting), the core claims do not change.
- Under C2 (experience needs broadcast in the brain's sense), the account would gain a core claim whose
  predictions are global workspace theory's own. Those would separate the account from integrated
  information theory but not from global workspace theory. That claim would also count toward the bar,
  which would lift the account past it (three of five).
- The proposal's one-sentence statement of the account (P2) would fold "one space that the whole system
  can use" into the central bet.

No record depends on the proposal.

**The second reader goes first here.** On all five of the account's testability judgements, Gemini's
reading will be the first of record (ruling 7b). My readings on those rows are marked as second, and the
validator refuses the file if they are not.

## 4. The scores my reading alone gives (one reader, Claude Opus 5.5; not results)

| theory | testability | support | left to test | group |
|---|---|---|---|---|
| Global workspace theory | 60 | **46** (8 outcomes, 4 studies, 4 groups, total weight 50) | 25 | ranked; the evidence so far leans against it |
| Integrated information theory | 60 | **57** (4 outcomes, 2 studies, 2 groups, total weight 28) | 57 | ranked |
| The Sentient Horizons account | 50 | too little tested to score | 100 | not yet defined sharply enough to rank |

**Ranking:** integrated information theory and global workspace theory **share first place**. Reversing
the outcome of the Dellert study alone would swap them, so by ranking rule 5 they are shown as tied.

**Headline**, provisional because ruling 3 is still open: 9 of the 13 distinguishing predictions across
the three theories have been tested by a counted study (69%). Before ruling A it was 5 of 13.

**What the support numbers rest on.** 50 means the evidence is even.
- **Global workspace theory (46).** The Cogitate study counts at weight 4 on each of five predictions,
  and its outcomes cancel out:
  - for: the onset rise, and quiet holding between ignitions;
  - against: prefrontal synchrony, and the offset ignition;
  - mixed: prefrontal content.

  The rest pulls the score down: Bellet is mixed (weight 1), the modelling study is mixed (weight 2),
  and the hearing study is against (weight 2).
- **Integrated information theory (57).** From the Cogitate study: the hot zone is for, sustained
  activity is mixed, and synchrony is against. The hearing study is for (weight 2).

The first version gave 44 and 75. The Cogitate tests of integrated information theory, now counted, are
what brought its score down.

**Under the stricter convention** (no undated study counts), only Cogitate would count. Both theories
would then fall to "testable, too little tested to rank".

## 5. The second reader: calls, cost, and the free tier

**Calls: 48**, one per packet:
- 13 outcome, 14 commitment and 21 testability;
- 5 of these are the account's rows, which Gemini reads first;
- 27 if the testability judgements are left out.

**The model.** Gemini 4 Carbon, which Google's pricing page calls "our most capable reasoning model"
(ruling 7a: the strongest version on offer). Source: Google, Gemini Developer API pricing,
https://ai.google.dev/gemini-api/docs/pricing, read 2026-11-20. The address now redirects to
aistudio.google.com/docs/pricing.

**Free tier: no.**
- The page says Gemini 4 Carbon "is not available on the Free tier".
- The free tier covers only smaller models, such as Gemini 4 Hydrogen and Gemini 3.8 Flash.
- On the free tier, Google uses the content to improve its products.

**Price:**
- $2 per million input tokens and $10 per million output tokens, thinking included, through 2026-11-30;
- $4 and $20 from 2026-12-01;
- the batch route costs half.

**Estimate.** The 48 packets come to about 52,000 input tokens in all. Output is the uncertain part,
because thinking tokens are billed.

| | at 3,000 output tokens per call | at 8,000 output tokens per call |
|---|---|---|
| all 48, through 2026-11-30 | $1.54 | $3.94 |
| all 48, from 2026-12-01 | $3.09 | $7.89 |
| outcomes and commitments only (27), through 2026-11-30 | $0.88 | $2.23 |
| outcomes and commitments only (27), from 2026-12-01 | $1.75 | $4.45 |

The batch route halves each figure. A ceiling of **$10** covers every case.

**Who pays.** This is Google billing, not the Anthropic credits, so it is out of pocket and needs John's
go first. I checked by name only that the key is in the project's `.env` file, and did not read its
value. I did not check whether its Google project has billing switched on.

**What goes to Google.** The packets hold passages from public papers, the public positions page, and
the records' own wording.

## 6. Every place a judgement felt unsure

Each has its reason written in its record (`unsure_why` in `data/tracker/judgements.toml`). In plain terms:

**Outcomes.**
- **Cogitate, seen content in prefrontal cortex: mixed.** The category of what was seen could be decoded
  there, but its orientation was found by only one of three methods, and weakly.
- **Cogitate, the rise of activity at onset: for.** Every stimulus was seen, so the study cannot show a
  rise that unseen stimuli lack.
- **Cogitate, prefrontal synchrony: against.** The measure agreed in advance found none. A measure chosen
  afterwards found some, and I gave it less weight.
- **Cogitate, quiet holding between ignitions: for.** The only observable part is absence of activity,
  which is also what no prefrontal role at all looks like.
- **Cogitate, hot zone: for.** Category could also be decoded from prefrontal cortex, and the consortium
  called this prediction non-critical.
- **Cogitate, sustained activity: mixed.** It held for category and failed for orientation. By the
  registered criterion, the consortium says it passed.
- **Cogitate, posterior synchrony: against.** Early visual cortex was thinly covered by the electrodes.
- **Bellet: mixed.** The study cannot tell seen pictures from unseen ones.
- **Dellert, fronto-parietal rise: against.** Brain scanning is slow, and the comparison is between groups
  of people, not between trials.
- **Dellert, hot zone: for.** The study found no prefrontal activation, which is weaker than showing that
  prefrontal cortex adds nothing. And the hot zone was described for vision, not hearing.

**Commitments.**
- **Bellet and Dellert for global workspace theory, and Dellert for the hot zone.** These rest on the
  five-year convention. Dellert's hot-zone reading is the closest call: 6.3 years.
- **Bellet for the hot zone:** unclear.
- **Bandara's top-down prediction.** It rests on the proponents' quotation of their own 1998 paper, which
  I did not open.
- **The hot zone as an "auxiliary" prediction.** I read it as committing the theory, because its
  proponents signed it.

**Testability.**
- **The workspace theory's top-down prediction.** Its proponents give no test for it; the test wording is mine.
- **The late start of consciousness.** I found no rival that says it starts earlier.
- **Quiet holding.** It is set against a rival's sustained activity in a different part of the brain.
- **The hot zone.** Whether an "auxiliary" prediction is tied to a core claim.
- **High integrated information when awake.** Global workspace theory also predicts that consciousness
  is disrupted in sleep and anaesthesia.
- **Two integrated information predictions: quiet neurons, and connection strength.** The separation
  from the workspace theory is my inference.
- **The account's central bet.** Its losing condition might be taken as enough to make it able to fail.
- **The account's split prediction.** I said it separates from the workspace theory by reading a
  prediction into that theory's silence, which I refused to do elsewhere. By the stricter standard it
  would not separate. The account's testability would then fall to 25, and only one of its claims would
  pass the bar.
- **The account's no-split prediction.** I read this one strictly, which is inconsistent with the split
  prediction. The second reader should test both.
- **The account's enriching features.** The separation from Damasio's theory rests on a secondary
  quotation.

## 7. What was not opened

- **The two 2016 papers in *Nature Reviews Neuroscience* by Tononi, Koch and colleagues.** Since ruling A
  they no longer decide anything in the pilot.
- **The 2022 no-report study by Hatamimajoumerd and colleagues**, which showed a robot check.
- **The 1998 workspace paper by Dehaene, Kerszberg and Changeux.** It is quoted by its proponents; its
  open copy was not read.
- **The Cogitate study's Extended Data Table 1 and Fig. 7**, which are images.
- **The journal version of the Dellert study.**
- **The papers the Working Positions page cites.**

## 8. Next, for the master to put to John

1. **The spend.** Up to $10 on Gemini 4 Carbon for the 48 readings, or the 27 outcome and commitment
   readings alone, ideally before 2026-12-01, when the price doubles.
2. **Optionally, the five-year convention** for studies that do not date their data (section 2). It is a
   reader's convention now, and it decides whether either theory has a support score.

The stage 2 stop condition is the readers disagreeing on more than a third of the judgements. It can only
be checked once the second reading is in.
