# Recurrent processing theory (Victor Lamme): drafting notes, 2026-11-21

Draft for the stage 3 theories tracker. Nothing here is merged; the session that
started this draft reviews it. Files: `sources.toml`, `theory.toml`, `predictions.toml`,
`studies.toml`, `judgements.toml`, `verify.toml`. All six parse with `tomllib`. Every
quotation was checked by a script against the text this session extracted from the
opened copy; four did not match character for character only because of page breaks,
line numbers or a font code in the extracted text, and were checked by eye.

## The core-claim source, and which copy was read

The ruled source is Lamme 2010, "How neuroscience will change our view on
consciousness" (Cognitive Neuroscience 1(3):204-220), the target article.

- **Author's own copies, looked for first.** The University of Amsterdam repository
  (UvA-DARE) has a record for it with the abstract and no file. Lamme's university
  profile page answered "not found", and the university's Pure search refused the
  request. No author page or author copy was found. ResearchGate was not tried.
- **Copy used.** The publisher's own PDF of the whole discussion issue (target article,
  commentaries, reply), posted openly with no sign-in on the Université libre de
  Bruxelles repository (it was filed there under one commentary's title). Its pages are
  stamped as downloaded by a subscriber on 2010-09-04. Because it is the journal's
  typeset file, no difference from the journal text is expected, and none was seen; it
  was not compared with the journal's own page, which needs a sign-in (verify list,
  `v-rpt-lamme-2010-copy`). It is not an author's copy, so John may prefer to have it
  checked before the claims are fixed.
- The 2006 paper (Trends in Cognitive Sciences) was read from the publisher's PDF on a
  University of California San Diego course page, also not an author's copy; it is used
  only for the earliest statement of predictions.

## Core claims: how they were chosen (repeatable)

Read the whole target article. Mark every sentence in which the author, in his own
voice, says what makes a state conscious or unconscious, or where the line between
them lies (not sentences reporting others' views or single experiments). Merge
sentences that say the same thing, keeping the more general one, and keep the rest in
the order the paper's argument reaches them. That gave six, all inside the 3-to-7 range,
so none was dropped:

1. `rpt-c1` the fast forward pass is unconscious wherever it reaches (p. 216);
2. `rpt-c2` recurrent processing is necessary for seeing (p. 216);
3. `rpt-c3` recurrence among visual areas is what makes seeing conscious; prefrontal and
   motor areas add report (p. 219);
4. `rpt-c4` recurrence confined to visual areas, without attention, is just as conscious
   (pp. 219-220);
5. `rpt-c5` the general rule, beyond vision: a sensation is conscious if and only if the
   areas involved engage in recurrent interactions (p. 219);
6. `rpt-c6` attention and consciousness are independent (p. 218).

Left out as not claims about what makes something conscious: the paper's arguments
about method (introspection, "neural arguments"), the Φ and learning arguments (offered
as support), and the line "Recurrent interactions that produce consciousness therefore
should not be too strong" (p. 217), which is an inference from another theory; a
reader could argue it in as a seventh.

## Predictions

Seven: six stated by the proponent, one inferred by the site.

| prediction | core claim | first stated | separates (reading) |
|---|---|---|---|
| `rpt-ff-unseen` forward-only processing is unseen even when it reaches prefrontal cortex | c1 | lamme-2006 | no |
| `rpt-feedback-needed` cutting feedback into early visual cortex removes seeing | c2 | lamme-2006 | no |
| `rpt-van` seeing shows first as an early posterior EEG wave (~200 ms) | c2 | lamme-2018 | yes, from global workspace (unsure) |
| `rpt-no-report-sensory` without report, seeing shows in sensory cortex, not fronto-parietal or late waves | c3 | lamme-2010 | yes, from global workspace |
| `rpt-unattended-local` unattended, unreported stimuli still drive recurrence within visual cortex | c4 | lamme-2006 | no |
| `rpt-attention-independent` attention does not decide seeing | c6 | lamme-2006 | no |
| `rpt-other-senses` (site) hearing works the same way | c5 | site, from lamme-2010 | yes, from global workspace |

Rivals: only global workspace theory has an opened rival-proponent passage here
(`mashour-2020`). No higher-order theory paper by its proponents could be opened (Brown,
Lau and LeDoux 2019 and Lau and Rosenthal 2011 are not open in Europe PMC), and
integrated information theory's proponents predict the same as this theory on every
point checked (posterior, recurrent), so no separation from it is claimed.

## Study search (repeatable)

- **Reading list:** ConTraSt live CSV export, downloaded 2026-11-21 (494 rows),
  `scratchpad/contrast/export.csv`.
- **Query, as run:** rows with `Is_the_experiment_theory_driven == "driven"` and
  `"FOT"` in `Driven_by_theories` (71 rows); one row per DOI (64 papers); sorted by
  `Year`, newest first; take the first five. Ties within a year kept in the export's order.
- **Screen list (every candidate, in order):**
  1. Bandara, Rowe and Garrido 2025 (10.1093/nc/niaf033): taken; existing record
     `bandara-2025`, reused.
  2. Dellert … Straube 2025, Current Biology (10.1016/j.cub.2025.10.026): taken; the
     journal version of existing record `dellert-2025`, reused (journal version not
     opened: robot check).
  3. Filimonov, Krabbe, Revonsuo and Koivisto 2024 (10.1093/nc/niae031): taken, new
     record `filimonov-2024`.
  4. Eiserbeck, Enge, Rabovsky and Abdel Rahman 2022 (10.1093/cercor/bhab289): taken,
     new record `eiserbeck-2022` (preprint read; journal version blocked).
  5. Filimonov, Railo, Revonsuo and Koivisto 2022 (10.1016/j.neuropsychologia.2022.108154):
     taken, new record `filimonov-2022`.
  (Next in line, not taken: Dellert … Straube 2022, NeuroImage, 10.1016/j.neuroimage.2022.119679.)
- **Counts:** 5 screened, 5 taken, 0 skipped. Every study recorded tests at least one
  recorded prediction, so none has `bears_on = []`. Research groups: Garrido, Straube,
  Koivisto (two studies), Abdel Rahman.
- None was registered; none was run by the theory's proponent; none had a rival camp's
  agreement or a replication. Every study's weight is 2.

## What counts, under the rules as written

- **Counted:** one study-prediction pair, `filimonov-2022` on `rpt-van`, read "for".
- **Before, but scores nothing** (prediction does not separate): `bandara-2025` and
  `eiserbeck-2022` on `rpt-unattended-local` (mixed, against).
- **Unclear, not counted:** both auditory studies on the proponent's predictions
  (`dellert-2025`, `filimonov-2024`), `eiserbeck-2022` on `rpt-van`, `bandara-2025` on
  `rpt-no-report-sensory`.
- **Not-before:** three pairs on the site-inferred `rpt-other-senses`.
- My arithmetic, not the script's: testability (0 + 1 + 1 + 0 + 0.5 + 0) / 6 ≈ 42; two of
  six core claims (three if a site-inferred prediction counts for the bar) have a
  separating prediction, which is not more than half, so the theory sits in "not yet
  defined sharply enough to rank"; one counted study from one group, so no support score.

## Judgements: counts and every unsure one

21 judgements: 3 outcome, 11 commitment, 7 testability. Unsure (13):

- `out-filimonov2022-rpt-van` (for): the early wave leads the late one by only ~30 ms, in
  a design with report.
- `out-bandara-rpt-unattended-local` (mixed): the authors read it against "sensory
  theories"; this reading follows Lamme's own account of inattentional blindness.
- `out-eiserbeck-rpt-unattended-local` (against): Lamme 2010 says blinked targets are
  masked, which would make the result irrelevant ("mixed").
- `com-eiserbeck-rpt-van` (unclear): Lamme 2018 expects early signals intact in the
  attentional blink, against the general awareness-negativity statement.
- `com-eiserbeck-rpt-unattended-local` (before): same tension, read the other way.
- `com-bandara-rpt-unattended-local` (before): the 2006 passage reports one experiment.
- `com-bandara-rpt-no-report-sensory` (unclear): for this theory the study's "unaware"
  group may have seen the face.
- `com-dellert-rpt-no-report-sensory`, `com-filimonov2024-rpt-no-report-sensory`,
  `com-filimonov2024-rpt-attention-independent` (unclear): vision-only statements
  applied to hearing.
- `tst-rpt-van` (separates, unsure): global workspace theory's review grants the early
  wave and relabels it.
- `tst-rpt-unattended-local`, `tst-rpt-attention-independent` (do not separate, unsure):
  same observations, different labels.

## Not opened, or opened only through a copy

- Lamme 2010 journal page (sign-in); read from the publisher's PDF on another
  university's repository (verify).
- Lamme 2018: PubMed Central and the Royal Society both answered with robot checks for
  this session; read from a copy of the PubMed Central page saved earlier today in this
  session's scratchpad (`scratchpad/lamme.html`) by the session that started this draft
  (verify). The pilot opened it directly on 2026-11-20.
- Eiserbeck 2022 journal version (Oxford Academic, 403): preprint read (verify).
- Dellert 2025 Current Biology version (robot check): preprint read (verify, as in the pilot).
- Lamme 2003 (Trends in Cognitive Sciences), 2004 (Neural Networks) and Lamme and
  Roelfsema 2000 (Trends in Neurosciences), which may state some predictions earlier,
  were not looked for in open copies beyond UvA-DARE's listing, which showed no files.
  None of the dating verdicts depends on them except `rpt-van` (stated 2018 here).
- Higher-order theory papers (no open copy found), so no separation from that rival.
- For John to sign in to: Taylor and Francis (Lamme 2010), Oxford Academic (Eiserbeck
  2022), Cell Press (Dellert 2025).

## Reused records: anything wrong for this theory

- `bandara-2025`: nothing wrong in the record. For this theory, its "awareness" factor
  compares people who could not report the face (phase 1, inattentionally blind) with the
  same people once alerted (phase 2), and Lamme holds that inattentionally blind people
  may have seen what they cannot report; the readings say so. `camps = []` holds.
- `dellert-2025`: nothing wrong. `camps = []` holds for this theory. ConTraSt lists the
  journal version's authors without Dellert first; the journal and preprint put him first.

## Where a rule gave a result John may not have intended (applied anyway)

1. **Hearing is shut out.** Two of the five studies chosen through ConTraSt's family for
   this theory are about hearing, and both find what the study authors call this theory's
   prediction (sensory, not fronto-parietal). Because every opened statement by Lamme is
   about seeing, the commitment is "unclear" and they count for nothing. Their authors,
   and ConTraSt, read the theory as covering every sense; Lamme's own general claim
   (`rpt-c5`) arguably does too. If John reads `rpt-c5` as committing the theory for
   hearing, both pairs become "before", and the theory would have counted studies from
   three groups.
2. **The theory's central claim cannot score.** Its main disagreement with global
   workspace theory, that unattended, unreported but unmasked stimuli are seen
   (`rpt-c4`), predicts the same measurements as workspace theory, which calls them
   "preconscious". Under ruling C (a rival must predict something different) that claim
   never separates, so the theory's testability is held down by the very claim that
   defines it. Probably intended (a disagreement only over labels is not a test), but
   worth seeing stated.
3. **One proponent paper pulls against itself.** Lamme 2018 states both that the early
   awareness wave marks seeing and that the attentional blink leaves early signals
   intact; and Lamme 2010 says blinked targets are masked. The rules have no way to
   choose among a proponent's own statements, so the Eiserbeck pairs come out "unclear"
   on one prediction and "before" on the other.
4. **ConTraSt's family is broader than the theory.** The family "FOT" now includes
   predictive processing; none of the five studies was framed around predictive
   processing, so nothing was excluded on that ground.
