# Damasio's feeling-based theory: draft notes, 2026-11-21

Theory id `damasio`, prefix `dam-`. Every file here was drafted on 2026-11-21 by one Claude
session. Nothing in the repository was touched.

## 1. The core-claims source was only partly opened

The ruled source is Damasio A and Damasio H, "Feelings are the source of consciousness",
*Neural Computation* 35(3):277-286, 2023 (doi 10.1162/neco_a_01521). It is free at the
publisher: Unpaywall and Semantic Scholar both list it as open access. But the free PDF
and the article page both answered with a Cloudflare "Performing security verification"
robot check, to a plain fetch and in the browser pane, and it was not bypassed. There is
no copy in PubMed Central, and no other open copy turned up.

What was opened is the paper's **published abstract**, read word for word in Europe PMC.
The abstract is part of the ruled publication, not another source. So I drafted the core
claims from it, and I did not substitute any other paper. **This needs John's ruling:**
may core claims be fixed from the abstract alone? Or are they held until the full text is
read? If they are held, the theory has no fixed claims yet, and every record below is
provisional. The verify entry `v-damasio-2023-fulltext` says what clears it. Because the
paper is free, John should need no sign-in: he only has to open it in his own browser (or
in the browser pane, where the check may let a person through), and a session then checks
the claims against the full text.

The paper went public before its "2023" date. PubMed first listed it on 2022-07-27
(received 2022-01-04, accepted 2022-04-13), and Semantic Scholar gives 2022-07-19. The
print issue is dated 2023-02-17.

## 2. How the core claims were chosen (repeatable)

In the abstract, every sentence that gives the authors' own hypothesis or their definition
of consciousness is a candidate, one claim per sentence. These are the sentences that open
with "Consciousness occurs when", "We hypothesize", "We also hypothesize" and "we outline a
mechanism". I kept the ones that say what makes a system conscious, or what produces the
feelings that do. That gave four claims:

- `dam-c1`: a thing is conscious when the mind's contents are marked as belonging to one organism.
- `dam-c2`: a continuous flow of feelings of the body's own state does the marking.
- `dam-c3`: those feelings were the first form of consciousness to evolve.
- `dam-c4`: the feelings come from a two-way exchange between the nerves that sense the body's
  interior and the body's organs and chemistry.

I left out the framing sentence, the sentence about the self, the description of what the
feelings are like, the sentence about "overt" guidance (which follows from claim 3), the two
sentences calling feelings "hybrid", and the closing remark on the mind-body problem.

## 3. Does Singer and Damasio 2025 restate the theory? (the coordinator's added check)

**It states the same theory, but its main job is narrower: the physiology of how the
nerves that sense the body's interior work. It is not a full restatement.** The paper says
its own aim in plain terms:

> "The goal of this article is to describe the distinct mechanisms through which
> homoeostatic feelings are generated." (Introduction, fifth paragraph)

Its abstract places it as building on the earlier theory, not replacing it: "This idea
builds on our prior work, which grounds consciousness in core biology rather than
high-level cognition." Its first reference is the 2023 paper.

What it restates: homeostatic feelings are the basis of subjectivity and the ground of
consciousness (sections 5(a) and 8). It also sets the theory against global workspace
theory, integrated information theory and higher-order theories (section 6).

What it adds, beyond the 2023 abstract:

- a split between a "feeling mind" and a "modern mind";
- "consciousness proper" as subjectivity combined with the modern mind;
- a brainstem-centred view;
- signalling that is graded and continuous ("analogue") and passes outside synapses;
- a claim about AI.

What it does not restate in 2023's terms: the definition in `dam-c1` (the nearest it comes
is "Interoceptive feelings underpin the sense of direct ownership of the organism’s body"),
and the claim in `dam-c3` that these feelings came first in evolution.

Damasio and Damasio 2024 (*Phil Trans R Soc B*, "Sensing, feeling and consciousness") is
closer to a full restatement, though a short one. It covers the claims in `dam-c2`, `dam-c3`
and `dam-c4`. So if the rule question is "latest statement of the same theory", the 2025
paper is a narrower piece, and the 2024 paper is the latest short statement of the whole
theory that I opened.

## 4. Predictions

There are seven, all stated by the proponents (`stated_by = "proponent"`). Each one's
`first_stated` is the earliest Damasio publication opened here that states it.

| prediction | core claim | first stated | could fail | separates from |
|---|---|---|---|---|
| `dam-feeling-required`: no feelings of the body's state, no consciousness | c2 | 2024-07-15 | yes | sh |
| `dam-subcortical`: basic feelings start in the brainstem and survive loss of cortex | c4 | 2012-04-03 | yes | gwt, iit |
| `dam-insula`: feelings survive loss of both insulae | c4 | 2012-04-03 | yes | none on the list |
| `dam-nonneural`: consciousness comes from nerves and body together, not nerves alone | c4 | 2024-07-15 | yes (unsure) | none |
| `dam-nss`: body-sensing nerve fibres also signal outside synapses | c4 | 2025-11-13 | yes | none |
| `dam-no-nervous-system`: bacteria and plants are not conscious | c3 | 2024-07-15 | no | none |
| `dam-ai`: present-day AI lacks what grounds feelings | c4 | 2025-11-13 | no | none |

`dam-c1` has no prediction. No opened text names an observation that would show a mind's
contents present but not marked as one's own.

**Where this leaves testability, read provisionally:** c1 scores 0, c2 scores 1, c3 scores
0 and c4 scores 1, so testability is 50. The ranking bar asks for *more than half* of the
core claims to have a prediction that could fail and that separates the theory from a
rival. Two of four is exactly half, so the theory falls below the bar: "Not yet defined
sharply enough to rank". A fifth claim, or a different choice of claims, would change this
(see section 7).

Some Damasio papers that may state these predictions earlier were not opened. Europe PMC
lists no open copy for any of them:

- Damasio and Carvalho 2013 (*Nature Reviews Neuroscience*)
- Parvizi and Damasio 2001
- Carvalho and Damasio 2021 (*BioEssays*)
- Damasio and Damasio 2022 (*Brain*)
- Damasio and Damasio 2024 (*Journal of Cognitive Neuroscience*)

The verify entry `v-damasio-earlier-statements` covers them. Reading them would change no
study's count in this sample.

## 5. Study search and screen

The search was a Europe PMC REST search, run 2026-11-21, sorted newest first
(`sort=P_PDATE_D desc`, `pageSize=60`). The query was exactly:

    (TITLE_ABS:"Damasio" OR TITLE_ABS:"homeostatic feeling*" OR TITLE_ABS:"primordial feeling*" OR TITLE_ABS:"feelings are the source") AND TITLE_ABS:conscious* AND SRC:MED

It found **18 hits in all**, so the limit of 60 never came into play. I screened them in
order. A hit was taken only if its title or abstract reports new data (or a reanalysis)
**and** says it tests Damasio's theory or a result or prediction he stated, or says that
his framework predicts its result.

| # | PubMed id | year | first author | taken? | why |
|---|---|---|---|---|---|
| 1 | 40910115 | 2025 | Immertreu | **taken** | new data (an AI agent); abstract says it probes core consciousness "as proposed by Antonio Damasio's theory" |
| 2 | 39217421 | 2024 | Rybakowski | skipped | review, no new data |
| 3 | 37918346 | 2023 | Damasio H | skipped | interview |
| 4 | 35896152 | 2023 | Damasio A | skipped | the core-claims paper itself; theory, no new data |
| 5 | 34735235 | 2021 | Gomez-Marin | skipped | book review |
| 6 | 27439487 | 2016 | Tirapu-Ustarroz | skipped | review |
| 7 | 27721801 | 2016 | Shafir | skipped | perspective on movement therapy; no new data in the abstract |
| 8 | 23678246 | 2013 | Almada | skipped | theoretical synthesis, no new data |
| 9 | 21694965 | 2011 | Vaillant | skipped | essay or review |
| 10 | 18824046 | 2008 | Denburg | skipped (unsure) | new data (a single patient), but the abstract presents Tranel and Damasio 1985 as earlier evidence its case "complements". It does not say it tests a Damasio theory or prediction |
| 11 | 18824045 | 2008 | Vianna | **taken** | new data; abstract says Damasio's framework "predicts such a dissociation" |
| 12 | 18609007 | 2008 | Wilson | skipped (unsure) | reconsiders an earlier case report and weighs Damasio's "extended consciousness" as one of three explanations. It is a reinterpretation, not a test, and the abstract reports no new data |
| 13 | 17689980 | 2007 | Bosse | skipped | a formal simulation of the theory; no data about the world |
| 14 | 16513144 | 2006 | Gutbrod | **taken** | new data; tests a claim by Bechara, Damasio and colleagues (1997) |
| 15 | 16179816 | 2005 | Farina | skipped | history |
| 16 | 15949516 | 2005 | Naccache | **taken** (unsure) | new data; abstract says it replicates "the findings reported by these authors" (Damasio, Bechara and colleagues) |
| 17 | 15501919 | 2004 | Maia | **taken** | new data; re-examines the evidence for Damasio's somatic marker hypothesis |
| 18 | 12445903 | 2002 | Robertson | not reached | five already taken |

**Counts.** 18 hits; 17 screened before five were taken. Five taken, eleven skipped and one
not reached. Two of the five (Gutbrod and Naccache) were read as abstracts only, because
their full texts are behind subscriptions. One more study, by the proponents themselves
(`damasio-tranel-2013`, patient B.), is recorded because a prediction rests on it. The
search did not find it.

**Result: no study counts.** None of the five tests a recorded prediction of the
feeling-based theory, so each has `bears_on = []`. The patient-B. study tests `dam-insula`,
but it states the prediction in the same paper, so it is "not-before". The theory would
show as "too little tested to score".

The two close calls, Denburg (skipped) and Naccache (taken), decide which five were taken.
Taking Denburg would push Maia out. Either way, no score changes.

## 6. Unsure judgements

All readings are Claude's, with `order = "first"`.

- `com-damasio-tranel-2013-dam-insula` (not-before): Damasio papers not opened here might
  state the prediction earlier. But the patient's data date from 1975 on, so the verdict
  would likely stand.
- `tst-dam-feeling-required` (could fail, separates from sh): it is doubtful the case could
  ever be observed, and "mattering" on the account may not be the same thing as Damasio's
  "homeostatic feeling". This row names the site's own account, so the outside reader
  should read it first (ruling 7b).
- `tst-dam-subcortical` (separates from gwt and iit): the rivals' registration speaks of
  "conscious experience" in general, and Damasio speaks of "basic feeling states". They
  conflict only if basic bodily feeling counts as conscious experience for the rivals.
- `tst-dam-nonneural` (could fail): the test wording is mine, and "not from the nervous
  system alone" is loose. A stricter reader would say it could not fail.
- `tst-dam-nss` (could fail): the paper calls the mechanism only "plausible".
- Screen calls 10, 12 and 16 (above).

## 7. Where a rule gave a result John may not have intended (applied anyway)

1. **Abstract-only core claims.** The ruled source is free but blocked by a robot check. Read
   strictly, the rules leave the theory with no claims. I drafted from the abstract and
   flagged it, rather than stopping.
2. **The search finds another Damasio theory.** The query matches "Damasio" in abstracts.
   Three of the five most recent qualifying studies (Gutbrod, Naccache, Maia) test his
   *somatic marker hypothesis*, which is about how bodily signals guide decisions, not his
   theory of consciousness. The "five most recent" rule takes them anyway, and none counts.
   The search also cannot find the proponents' own studies, because author names are not in
   the title or abstract fields.
3. **Ruling C and the site's own account.** Under ruling C, `dam-feeling-required` separates
   Damasio's theory only from the Sentient Horizons account, because that is the only
   rival's opened source that says something different. Damasio's own section 6 (2025) sets
   his theory against global workspace theory, integrated information theory and
   higher-order theories, but that is his description of them, so it does not count. One of
   the theory's two separating claims therefore rests on the site's own account.
4. **Exactly half misses the bar.** Two of four core claims pass, which is not "more than
   half". Taking a fifth sentence from the abstract as a claim (the "overt" guidance
   sentence, which has no separating prediction) would lower testability to 40 and keep the
   theory below the bar. Dropping c1 or c3 instead (three claims) would put two of three over
   the bar. So the claim-choice method alone decides which group the theory is shown in; I
   applied the method as written in section 2 and did not tune it.
5. **The insula prediction opposes a theory not on the list.** Damasio's clearest tested
   prediction (patient B.) is aimed at A. D. Craig's view that the insula alone produces
   feeling. Craig's theory is not one of the ten, so the prediction separates nothing.

## 8. What was not opened

- Damasio and Damasio 2023, full text: robot check (`v-damasio-2023-fulltext`).
- The earlier Damasio papers listed in section 4, behind subscriptions
  (`v-damasio-earlier-statements`).
- Gutbrod 2006 and Naccache 2005, full texts: subscriptions (`v-damasio-screen-abstract-only`).
- Damasio's 1999 and 2010 books.

Opened in full or in large part:

- Singer and Damasio 2025
- Damasio and Damasio 2024
- Damasio, Damasio and Tranel 2013 (online 2012)
- Immertreu 2025
- Vianna 2008
- Maia 2004
- the Cogitate registration v1, pp. 5-6
- the Working Positions page

Every quoted passage in the TOML files was checked by script against the text that was
opened: 26 passages, none missing.
