# Higher-order theories: notes on the stage 3 draft (2026-11-21)

First reader: Claude (claude-opus-5-5). Every quotation in the TOML files was checked by a
script against the texts downloaded in this task (68 passages, all found, ignoring line
breaks and spacing). Downloads are in the scratchpad folder `hot-dl/`.

## 1. The core-claim source and which copy was used

- **Ruled source:** Brown, Lau and LeDoux, "Understanding the higher-order approach to
  consciousness", *Trends in Cognitive Sciences* 23(9):754-768, 2019.
- **Copy used:** the authors' PsyArXiv preprint, "The Misunderstood Higher-Order Approach to
  Consciousness" (OSF file `BrownLauLedoux_Jan 3 2019.text.boxes.figs.pdf`, posted
  2019-01-07, one version only). Read in full.
- **Journal text not opened.** OpenAlex lists a free copy at cell.com; that address, and the
  PhilArchive copy (which OpenAlex marks as the submitted version), both answered with a
  "Just a moment..." robot check. Not bypassed. No copy on Brown's or Lau's own sites was found
  by search. Verify entry `v-hot-journal-text` says the quotations need checking against the
  journal text, which John would sign in for.
- **Differences seen:** the title changed; the journal abstract (read in Europe PMC) is
  reworded and adds two sentences, one saying higher-order states are "cognitively assembled"
  with requirements "considerably less than often presumed", one saying most proponents "do
  not stipulate consciousness as equivalent to metacognition or confidence". The second matches
  the preprint's Misconception 3, so the body probably kept it.

## 2. How the core claims were chosen (repeatable)

1. Read the preprint's "What Is HOT?" section and the corrective statement that ends each
   "Misconception" section.
2. Keep each sentence that states, as the theory's own position, what makes a state conscious
   or what consciousness requires. Markers: "a fundamental tenet of HOT", "the claim that",
   "according to HOT", "the hypothesis is", "HOT ... posits".
3. Drop sentences about what HOT does *not* claim (it is not a single theory; it does not need
   sophisticated thought; consciousness is not metacognition; agnosticism about animals), and
   about applications (emotion, the clinic).
4. Merge sentences that say the same thing; keep the most general wording.

Result: five claims. `hot-c1` (first-order states are not sufficient), `hot-c2` (the
transitivity principle), `hot-c3` (higher-order awareness, not broadcast, is essential),
`hot-c4` (prefrontal cortex's key role), `hot-c5` (the higher-order state decides, whatever
the first-order process). One further "posits" sentence (p. 6-7: all conscious experiences
involve regions "traditionally thought to be important for high level cognition and
attention") was folded into `hot-c4`.

## 3. Predictions, and the claim with none

Five predictions, all stated by proponents. Statements opened: brown-lau-ledoux-2019,
ledoux-brown-2017 (PNAS, open on PubMed Central), fleming-2020 (open). Michel and Lau's
PsyArXiv paper ("On the dangers of conflating strong and weak versions of a theory of
consciousness", 2019-06-24) was opened and searched; it is about integrated information
theory and states no higher-order prediction, so it is not used. Lau and Rosenthal 2011 was
not opened (paywalled; no author copy; a copy on a university course page was not used
because it is not the authors' own).

| claim | prediction | separates from (rival's own source) |
|---|---|---|
| hot-c1 | hot-first-order-insufficient | rpt (lamme-2018) |
| hot-c2 | **none** | |
| hot-c3 | hot-unconscious-global | gwt (mashour-2020) |
| hot-c4 | hot-pfc-involved | rpt (lamme-2018), iit (cogitate-protocol-2023) |
| hot-c4 | hot-pfc-disrupt | rpt, iit (same passages, read as implying it) |
| hot-c5 | hot-awareness-performance | none sourced |

**hot-c2 has no prediction.** The transitivity principle is stated as following from what
"phenomenally conscious" means, and no opened statement attaches an observation to it beyond
those already under c1 and c5. It adds a placeholder to "left to test" and scores 0 on
testability.

If the readings stand, testability is (1 + 0 + 1 + 1 + 0) ÷ 5 = 60, and three of five claims
pass the bar, so the family is past it.

## 4. Study search and screen

- Query, on the export downloaded 2026-11-21 (`contrast/export.csv`, 494 rows):
  `Is_the_experiment_theory_driven == "driven"` and `"HOT" in Driven_by_theories`; distinct
  DOIs; sorted by `Year` descending, ties in the export's own row order; take five. 13 rows,
  12 distinct papers.
- Screened list, in order:
  1. Mei and Soto 2025, 10.5334/joc.443: **taken** (`mei-soto-2025`).
  2. Bandara, Rowe and Garrido 2025, 10.1093/nc/niaf033: **taken** (existing `bandara-2025`).
  3. Dellert et al. 2025, 10.1016/j.cub.2025.10.026: **taken** (existing `dellert-2025`).
  4. Martin, Lane and Hsu 2023, 10.1016/j.cortex.2023.05.022: **taken** (`martin-2023`).
  5. Hobot, Skóra, Wierzchoń and Sandberg 2023, 10.1016/j.neuroimage.2023.119991: **taken** (`hobot-2023`).
  6. Hatamimajoumerd et al. 2022, 10.1016/j.cub.2022.07.068: not taken (beyond five; already
     an unopened pilot record).
  7. 2019, 10.1523/ENEURO.0268-18.2018: not taken (beyond five).
  8. 2019, 10.1016/j.neuropsychologia.2019.04.015: not taken (beyond five).
  9. 2017, 10.3389/fpsyg.2017.00210: not taken (beyond five).
  10. 2017, 10.1016/j.concog.2017.02.005: not taken (beyond five).
  11. 2013, 10.1016/j.neuroimage.2013.01.054: not taken (beyond five).
  12. 2011, 10.1016/j.neuroimage.2011.06.081 (Persaud et al., Lau among the authors): not
     taken (beyond five). This one is run inside the camp and predates every statement opened.
- Counts: 12 screened, 5 taken, 5 opened, 0 recorded with `bears_on = []` (each of the five
  tests at least one recorded prediction).
- Every taken study has weight 2 for this theory (outside the camp; none registered, agreed
  with a rival or replicated).
- Author order: ConTraSt lists the Martin study's authors alphabetically (Hsu first); the
  record uses the journal order (Martin, Lane, Hsu) and the id `martin-2023`. The brief
  called it "Hsu TY, Lane TJ, et al.".

## 5. Pairs judged

| study | prediction | commitment | outcome |
|---|---|---|---|
| mei-soto-2025 | hot-unconscious-global | before (unsure) | for (unsure) |
| dellert-2025 | hot-pfc-involved | before | mixed (unsure) |
| bandara-2025 | hot-pfc-involved | not-before (unsure) | none, not counted |
| martin-2023 | hot-pfc-disrupt | before | mixed (unsure) |
| hobot-2023 | hot-pfc-disrupt | before (unsure) | mixed (unsure) |
| martin-2023 | hot-awareness-performance | before | for (unsure) |
| hobot-2023 | hot-awareness-performance | before | for (unsure) |

Pairs considered and not judged: Mei and Soto against `hot-first-order-insufficient` (unseen
content was found in visual cortex, but the study does not measure feedback activity, which
the test wording asks for); Dellert against `hot-first-order-insufficient` (it found
awareness in auditory cortex but cannot show sensory activity without awareness);
Bandara against `hot-first-order-insufficient` (not-before in any case).

The two awareness-performance outcomes do not count, because that prediction does not
separate (see 7). Counted for support, if the readings stand: four pairs from four groups
(Soto, Straube, Hsu, Sandberg), one "for" and three "mixed".

## 6. Every unsure judgement

- `out-mei-hot-unconscious-global`: fMRI cannot show "stable"; seven people (four at the
  strictest cut).
- `out-dellert-hot-pfc-involved`: "mixed" leans on the proponents' own warning about null
  results; a reader could say "against".
- `out-martin-hot-pfc-disrupt`: the clean result is a null on visibility ratings; "against"
  is defensible.
- `out-hobot-hot-pfc-disrupt`: metacognition improved rather than worsened; "for" or "does
  not bear" both defensible.
- `out-martin-hot-awareness-performance`, `out-hobot-hot-awareness-performance`: weak
  evidence; metacognition may not be awareness.
- `com-mei-hot-unconscious-global`: the 2019 passage names no brain area.
- `com-bandara-hot-pfc-involved`: turns on the unopened Lau and Rosenthal 2011.
- `com-hobot-hot-pfc-disrupt`: the general statement against one prefrontal sub-region.
- All five testability readings are marked unsure; the reasons are in each record.

## 7. Places a rule may give a result John did not intend (applied anyway)

1. **Proponents' advance protection against nulls.** The 2019 statement says a null from a
   coarse method should not be generalised and that more prefrontal activity does not mean
   more consciousness; Fleming 2020 says null results from lesions should not surprise. The
   test wording follows the proponents (rule: write the test from what they said), which makes
   "against" hard to reach. The Dellert outcome is "mixed" because of this. A rule on how far a
   theory's own stated escape clauses may shape `test_against` would settle it.
2. **Ruling C and a rival described only by the theory.** The higher-order statement contrasts
   itself with global workspace theory on performance ("consciousness is associated with
   important functional advantages"), but that is the higher-order side describing its rival.
   No global workspace passage opened here says awareness cannot change while performance is
   matched, so `hot-awareness-performance` does not separate and `hot-c5` scores 0. This is the
   claim the family treats as its strongest empirical distinction from the workspace.
3. **Reading a location claim as a disruption claim.** For `hot-pfc-disrupt`, the rival
   passages say where the correlates of consciousness are, not what disrupting prefrontal
   cortex does. I counted them as separating (unsure). A strict reading of ruling C would not,
   which leaves `hot-c4` passing through `hot-pfc-involved` alone and changes no score.
4. **A family entry.** The family statement says its versions disagree on mechanism (HOROR
   puts the conscious state in prefrontal cortex itself; Lau's view has it "jointly determined"
   with sensory areas). Claims and predictions are written at the level all versions share,
   which keeps them loose; `hot-c5`'s "or even in the absence of a first order state in some
   views" belongs to some versions only.
5. **Who is a proponent.** Fleming 2020 states a higher-order model but Fleming is not an
   author of the family statement. The brief names his paper as a proponents' publication, so
   he is listed; it changes only `also_stated` passages and no date (every prediction's first
   statement is by Brown, Lau or LeDoux).
6. **Reanalyses and the 2011 gap.** Bandara's data appeared in 2015 and the earliest opened
   higher-order statement is from 2017, so it is "not-before". The likely earlier statement is
   paywalled. The rule's direction (unclear or unseen means not counted) is followed.
7. **Shared with global workspace theory.** `hot-pfc-involved` and `hot-pfc-disrupt` are
   predicted by the workspace too. They separate the family from recurrent processing and
   integrated information theory, which is enough under the ruled test, but a reader should know
   that support for them is also support for the workspace.

## 8. Not opened

- The Trends in Cognitive Sciences text (robot check at cell.com and PhilArchive):
  `v-hot-journal-text`.
- Lau and Rosenthal 2011 (paywalled): `v-lau-rosenthal-2011`.
- The Cortex version of the Martin study (no open copy; PhilArchive robot check):
  `v-martin-journal`.
- The Current Biology version of the Dellert study (cell.com): `v-hot-dellert-journal`.
- The Mei, Santana and Soto 2021 paper (dates from Europe PMC only): `v-mei-original-data`.
- ScienceDirect answered the Hobot page with a robot check; the published PDF was read from
  the Jagiellonian University repository instead (CC BY).
- The Cogitate preregistration file on OSF returned server errors (500) twice; the integrated
  information theory passage is taken from the Cogitate protocol (PLOS ONE, open), whose authors
  include the theory's proponents, instead.
- What John would need to sign in to: cell.com (Trends in Cognitive Sciences and Current
  Biology), Elsevier/ScienceDirect (Trends in Cognitive Sciences 2011, Cortex).

## 9. The reused pilot records, read for this theory

- **`bandara-2025`.** Nothing wrong for higher-order theories: `camps = []` holds (no author
  of brown-lau-ledoux-2019, ledoux-brown-2017 or fleming-2020 is an author), so
  `outside_camp = true` is right for `hot`. The paper's own framing is "frontal theories" against "sensory theories"; its introduction describes
  higher-order thought theories ("Higher-order thought theories propose
  that conscious ..."), citing Morales and Lau 2020 among others, so it is aimed at this family as well as the workspace. It bears on `hot-pfc-involved` only as a frontal theory.
- **`dellert-2025`.** `camps = []` and `outside_camp = true` are right for `hot`. Two things
  to note: (a) the record's source is the preprint, while ConTraSt and this brief point to the
  Current Biology version, already flagged by the pilot's `v-dellert-journal`; (b) the paper
  names higher-order theories directly and says its results "do not support a key role of the
  lateral PFC in conscious perception (Brown et al., 2019; ...)", so it is a test the authors
  aimed at this family too, not only at the workspace. The pilot's `expectation_note` (they
  expected sensory, not fronto-parietal, activity) applies here as well.
- The pilot's `contrast-export` source describes the 2026-11-20 export (515 rows); this draft
  used the 2026-11-21 export (494 rows) and adds `contrast-export-2026-11-21`. The row count
  differs; the five HOT rows were not compared against the earlier export.
