# Attention schema theory: notes on the stage 3 draft (2026-11-21)

Theory id `ast`. Every quote in the TOML files was checked by a script against the text
this session downloaded (all matched, whitespace and curly quotes aside). Downloads are in
the scratch folder `ast-dl/`.

## How the core claims were chosen

Source: Graziano and Webb 2015, Frontiers in Psychology (`graziano-webb-2015`), ruled by John
2026-11-21 ("Yes, keep 2015").

Method, so it can be redone: split the full text into sentences and keep every sentence in
which the authors say what the theory itself holds, found by the phrases "the theory
proposes", "the heart of the attention schema theory", "the core claim of the theory", "the
theory holds", "in the theory" / "in this theory" / "in the attention schema theory",
"according to the theory", and "if the theory is correct", in the body text (the abstract
left out). That gave about twenty sentences. Then:

1. Drop sentences that are about side questions, not about what makes a system aware
   (social cognition and religion; whether awareness without attention is possible; the
   no-mystery remark).
2. Where two sentences say the same thing, keep one: the sentence the paper itself labels
   "the core claim" wins over its restatements ("in a nutshell ... internal model of the
   process of attention", "holds that subjective awareness is the brain's simplified model");
   otherwise the earliest in the paper.
3. "The heart of the attention schema theory" (awareness has an adaptive value because it
   serves as a model of attention) was folded into claims 1 and 3, which state its two parts.

Result, six claims:

- claim 1, the model and reports (`ast-c1`, Conclusion);
- claim 2, the model leaves out the mechanism, so it depicts something impossible (`ast-c2`, Figure 1 caption);
- claim 3, awareness is part of the control machinery for attention (`ast-c3`, Figure 3 caption);
- claim 4, awareness of an item needs a brain-spanning joining of self, attention and item (`ast-c4`);
- claim 5, joining information up is not enough without the model (`ast-c5`);
- claim 6, awareness reaches wherever attention does (`ast-c6`).

Claims 4 and 5 have no prediction: no proponents' publication opened here states a test for
either. Both stay, because the method picked them; they pull the testability score down.

## Predictions

Seven, all stated by the proponents (none inferred by the site). The earliest opened
statement is the 2015 paper for five, Graziano 2018 for the temporoparietal junction one.
Other proponents' papers opened: Graziano 2022 (PNAS), Graziano 2024 (eNeuro, searched; it adds
no new testable prediction), and the two 2021 study papers. Graziano 2026 (PNAS) was read in
summary only, as instructed; its abstract states no dated, testable attention prediction beyond
the earlier ones, so nothing enters from it.

## Study search and screen

Query exactly `(TITLE_ABS:"attention schema") AND SRC:MED`, Europe PMC REST, `sort=P_PDATE_D
desc`, run 2026-11-21, 20 hits. Listed in the order returned (Europe PMC sorted item 9 by
its print year, so it sits after June 2021 items although it appeared online 2022-01-11).

| # | Record (first publication date) | Taken? | Why |
|---|---|---|---|
| 1 | Graziano, society of self-schemas, PNAS (2026-10-09) | no | theory, no new data |
| 2 | O'Reilly-Shah, State Space Theory (2026-04-01) | no | theory, a different theory |
| 3 | Graziano, conceptual framework, PNAS (2022-04-29) | no | theory and review |
| 4 | Long and colleagues, video classification (2022-03-04) | no | machine-learning "attention", not this theory |
| 5 | Schurger and Graziano, explained or described? (2022-01-21) | no | argument, no data |
| 6 | Wilterson and Graziano, neural network agent, PNAS (2021-08-01) | **yes** | artificial-agent experiment testing a stated prediction |
| 7 | Steel, topological perspective (2021-04-20) | no | theory |
| 8 | Wilterson and colleagues, right temporoparietal junction, PNAS (2021-06-01) | **yes** | human brain-scanning experiment testing the theory's predictions |
| 9 | Luczak and Kubo, predictive neuronal adaptation (2022-01-11) | no | theory, a different theory |
| 10 | Yi and colleagues, relation extraction (2021-11-01) | no | machine-learning "attention"; retracted |
| 11 | Graziano, certainty we're conscious (2020-11-11) | no | comment |
| 12 | Wilterson and colleagues, attention control, Prog Neurobiol (2020-06-01) | **yes** | six behavioural experiments testing the theory's predictions |
| 13 | Graziano, why it has to be right (2020-05-20) | no | reply to comments |
| 14 | Brown and LeDoux, higher-order memory schema (2020-02-25) | no | comment |
| 15 | Romo and Rossi-Pool (2020-02-18) | no | comment |
| 16 | Gennaro, some questions (2020-02-14) | no | comment |
| 17 | Graziano and colleagues, toward a standard model (2019-09-26) | no | theory |
| 18 | Webb, Kean and Graziano, effects of awareness, J Cogn Neurosci (2016-02-02) | **yes** | behavioural experiment testing the theory's predictions |
| 19 | Graziano and Webb 2015 | no | review, no new data (the core-claim source) |
| 20 | Graziano, speculations on evolution (2014-03-26) | no | theory |

Counts: 20 screened, 4 qualified (fewer than the 5 asked for, so all 4 taken), 2 opened and
judged, 2 not opened (below). All four have Michael Graziano as last author: every study is
inside the theory's own camp, none is registered, none rival-agreed, none replicated by
another group. Each weighs 1, and they all come from one research group, so under the ruled
two-groups rule this theory gets no support score however the outcomes read.

The query misses this lab's experiments that do not say "attention schema" in title or
abstract (for example Guterstam and colleagues 2020, PNAS, on other people's gaze seen as
implied motion, which turned up in a side search; and the Webb and colleagues 2016 brain-scanning
study that Graziano 2018 discusses). The method was applied as given.

## Judgements: 12 (2 outcome, 3 commitment, 7 testability)

Unsure readings (8 of 12 marked unsure):

- **Outcome, brain-scanning study on the control prediction** (`out-wilterson-tpj-ast-control`,
  read "for"): the "attention is still drawn to the masked cue" half was not measured in this
  study; it rests on the unopened 2020 paper. Aware and unaware groups were different people.
- **Outcome, agent study on the model-helps-control prediction** (`out-wilterson-agent-ast-schema-control`,
  "for"): one small network; the authors say a bigger one might not need the model.
- **Commitment, brain-scanning study on the temporoparietal junction prediction**
  (`com-wilterson-tpj-ast-tpj`, "unclear"): the 2018 sentence ties the junction to awareness,
  not to control; the specific test is first written in the study itself.
- **Commitment, agent study** (`com-wilterson-agent-ast-schema-control`, "before"): the 2015
  statement is about the brain; whether it commits the theory to an artificial agent's result
  is a judgement.
- **Testability, graded awareness** (`tst-ast-graded`, separates from global workspace theory):
  the only separating reading in the draft, and it leans on global workspace passages about
  "all-or-none" network states and "episodes", not about rated visibility.
- **Testability** of the covary, claims, control, junction and domain predictions: reasons in
  each record (mostly that only half the prediction can fail, or that rivals were not opened).

What the readings imply, by the ruled scoring as I understand it: only claim 1 has a separating
proponent prediction, so testability is 1 of 6 claims, about 17, and the theory is below the
bar (more than half its claims would need one): "not yet defined sharply enough to rank". No
outcome counts, because the two outcomes read "before" sit on predictions that do not separate.

## Not opened

- Wilterson and colleagues 2020 (Progress in Neurobiology): ScienceDirect gave no text to an
  automated fetch; Europe PMC lists it as open access, so John could open it in the browser pane.
- Webb, Kean and Graziano 2016 (Journal of Cognitive Neuroscience): subscription; MIT Press
  robot check. John would need to sign in at MIT Press (direct.mit.edu) or through a library.
- Graziano 2026 (PNAS) body: paywalled, no access; abstract only (verify entry `v-graziano-2026-body`).
- Graziano and Kastner 2011 and Graziano 2013 (the book), the earliest statements of the theory.
- Rival sources that might give separations: Koch and Tsuchiya 2007; Brown, Lau and LeDoux 2019;
  Lau and Rosenthal 2011; Rahnev and colleagues 2011 (all paywalled to an automated reader);
  Lamme 2018 (not available as open text this session). The Graziano lab's own site
  answered with a robot check and was not used.
- Re-opened for rival passages, already defined in the pilot: the global workspace review
  (`mashour-2020`), Dehaene and colleagues 2014 (`dehaene-2014`), integrated information
  theory 4.0 (`albantakis-2023`).

## Where a rule may give a result John did not intend (applied anyway)

1. **The dating test and the proponents' own lab.** For a study not registered in advance, a
   prediction counts if it was published before the study first appeared. Every study here comes
   from the lab that wrote the prediction. The brain-scanning study's behavioural result had
   already been published by the same lab a year earlier (2020), and the 2015 statement came
   out nine months before the lab's 2016 study (the 2015 paper was received in January 2015, when
   that study may already have been under way). The rule reads all of these as "before", though
   the lab could have known its results. The outside-camp protection only lowers the weight; it
   does not stop the count.
2. **Separation when a rival agrees.** The theory's central and most tested prediction (no
   awareness of an item means poor control of attention toward it) separates from no rival,
   because the one rival source opened that speaks to it, from global workspace theory, predicts
   the same direction. So the most-tested part of the theory can never move its support score.
   The theory itself (graziano-webb-2015, Introduction) says it is "consistent with" workspace and
   integration proposals "but also goes beyond them", so few separations may be the honest result.
3. **Claims with no stated test.** Claims 4 and 5 were picked by the method and have no
   prediction, which halves the theory's chance at the bar before any reading.
