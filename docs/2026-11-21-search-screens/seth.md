# Anil Seth's living-body view: screening the per-prediction searches, 2026-11-21

First reading by one Claude session (claude-opus-5-5). Draft only; nothing here has been merged or
read by a second reader. The method is the one fixed in `data/tracker/searches-2026-11-21.toml`
before the searches ran; it was followed as written. Titles and abstracts only were used for the
screen.

## Hit counts

| prediction | hits | screened | qualifying | taken |
|---|---|---|---|---|
| seth-living-only | 22 | 22 | 0 | none |
| seth-ai-not-by-computation | 114 | 40 | 0 | none |
| seth-expectation-speeds-access | 348 | 40 | 0 | none |
| seth-presence-match | 36 | 36 | 0 | none |
| seth-interoceptive-ownership | 31 | 31 | 3 | vabba-2025 |
| seth-low-interoception-more-illusion | 14 | 14 | 10 | raoul-2025 |
| seth-interoceptive-suppression | 52 | 40 | 2 | harrison-2021 |
| seth-feeling-from-prediction | 37 | 37 | 13 (2 more unclear from title alone) | hill-2024 |

260 results screened. Counting each study once, **26 qualify** (Moffatt 2024 and Suzuki 2013
qualify on two lists). Only four of the eight predictions have any qualifying study.

## The choice, and how the cap was applied

The method takes the five most recent qualifying studies across all eight lists, by earliest public
appearance, with at most one per prediction. Because only four lists hold a qualifying study, the cap
fixes the answer: the most recent qualifying study on each of those four lists is taken, and **the
fifth place stays empty**. No list's second study can fill it, because that would be a second study
for one prediction.

| taken | prediction | earliest public appearance | opened | camp |
|---|---|---|---|---|
| raoul-2025 | seth-low-interoception-more-illusion | 2025-09-10 (publication) | **no** | outside |
| vabba-2025 | seth-interoceptive-ownership | 2024-08-29 (preprint) | yes | **Seth's own lab** |
| hill-2024 | seth-feeling-from-prediction | 2024-04-23 (publication) | yes | outside |
| harrison-2021 | seth-interoceptive-suppression | 2021-03-26 (preprint) | yes | outside |

**Studies on two lists.** Two studies appear on two lists and qualify on both. Moffatt, Finotti and
Tsakiris 2024 qualifies for ownership (borderline) and for the low-interoception prediction.
Suzuki 2013 also qualifies for both. Neither is the most recent on either list, so the rule "taken
once and judged for both" never comes into play. No study taken here qualifies on a second list. Vabba
2025 also reports, as a side analysis, no link between heartbeat sensing and the illusion, which
bears on the low-interoception prediction. It does not appear on that prediction's list, though,
so it is not judged for it (the method screens per list).

## Judgements (first reading)

- Commitment: 3. `before` 2 (hill, harrison), `unclear` 1 (vabba, on the own-lab rule).
- Outcome: 2. `for` 1 (harrison), `mixed` 1 (hill, leaning for).
- raoul-2025: none, not opened.

### Every unsure judgement

1. `com-vabba-seth-interoceptive-ownership` (unclear). The 2012 sentence is vague, and the same lab
   published the heartbeat-timing result in 2013, so the own-lab rule bars the study whatever is
   read into the 2012 sentence. If it were counted, the result would be mixed: heartbeat-timed
   flashing moved felt hand position, but did not change the ownership questionnaire.
2. `out-hill-seth-feeling-from-prediction` (mixed, leaning for). A falsely fast heartbeat raised
   fear while the real heart rate stayed the same across groups. A falsely slow one did not lower
   fear. Most of the fast group did not believe the feedback.
3. `out-harrison-seth-interoceptive-suppression` (for). Insula activity rose with prediction error
   when the breath arrived. The "less when well predicted" half rests on that same error scaling,
   because the certainty effect was measured at the cue, before the breath.

## Not opened

- **raoul-2025.** ScienceDirect returned no article text, and HAL (hal-05284068) returned a robot
  check; neither was got past. John would need only a normal browser: the HAL copy is free, and
  ScienceDirect lists it as open access. Verify entry `v-seth-raoul-not-opened`.
- The preprints of vabba-2025 (Authorea) and harrison-2021 (bioRxiv): their dates come from the
  Europe PMC records only. Verify entries `v-seth-vabba-preprint-date` and
  `v-seth-harrison-preprint-date`.
- The Coventry University copy of hill-2024 returned a robot check. The Imperial College copy was
  read instead.

## Rule results John may not have intended

1. **Whole-body illusions, and which ownership study is taken.** The ownership prediction's test
   wording names "a seen hand". I read it to that scope, so studies that flash a whole virtual body
   in time with the heartbeat do not qualify: Knobel 2024, Heydrich 2018, Ronchi 2015 and Todd 2025
   (Todd also has no out-of-time comparison). Seth and Friston 2016 do mention the full-body version.
   If John counts whole bodies, **Knobel 2024 replaces Vabba 2025**: published 2024-12-11, with no
   preprint found in Europe PMC (received by the journal 2023-08-31), so it is later than Vabba's
   2024-08-29. Knobel is outside the camp, and its abstract reports no ownership difference between
   in-time and out-of-time feedback. It would most likely read "against".
2. **Pain is not emotion.** Parrotta 2026 (rank 2 on the feeling list) gave false heartbeat sounds
   and changed how painful identical shocks felt. I did not count pain as the "emotion" the test
   wording names. Also, the participants' real heart rate changed, so the body was not held still.
   If John counts it, **Parrotta 2026 replaces Hill 2024**.
3. **The search for seth-expectation-speeds-access found nothing usable.** Its query word
   "breakthrough" (meant for breaking through into awareness) matched breakthrough pain,
   breakthrough infections and the like. All 40 screened results are off topic, out of 348 hits.
   The query was fixed in advance and is not changed here. The prediction simply has no study.
4. **The two machine predictions cannot get a study.** seth-living-only and
   seth-ai-not-by-computation need "an agreed test for consciousness" applied to machines. No such
   test exists, so no result can qualify. This matches the ruling that they cannot fail with today's
   methods.
5. **The own-lab rule removes the only study testing the ownership prediction's exact form.** The
   heartbeat-timing prediction was first written by the lab that tested it. So under the own-lab
   rule no study from that lab can ever count for it, and an outside study (Moffatt 2024, Knobel
   2024) would also need a commitment earlier than 2013 that the 2012 sentence may not give.
6. **README wording.** As the earlier drafting notes said, `data/tracker/README.md` still says
   `data_collected` is what a prediction's date is compared with (2026-11-20). Ruling D compares it
   with the study's earliest public appearance. The `dates` tables here use `study_first_appeared`,
   as the brief says, and every opened study's collection date is also recorded. Neither rule
   changes a verdict here.

## The screen, line by line

"Qualifies" means the title or abstract shows new data (or a reanalysis) measuring what the test
wording names. "Cap" means not taken because a more recent study on the same list was taken.

### `seth-living-only`

Query run 2026-11-21 09:44 PST; **22 hits**; 22 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 42750552 | Shevlin H, 2026-09-17 | no: commentary or letter, no new data |
| 2 | 42750543 | Solms M, 2026-09-17 | no: commentary or letter, no new data |
| 3 | 42750514 | Baltieri M, 2026-09-17 | no: commentary or letter, no new data |
| 4 | 38163972 | Häyry M, 2026-07-01 | no: does not measure what the test names (antinatalism essay) |
| 5 | 41419099 | Milinkovic B, 2025-12-17 | no: review, no new data |
| 6 | 42876598 | Schilling A, 2026-09-30 | no: theory, essay or position paper, no new data |
| 7 | 42775162 | Koch F, 2026-09-22 | no: commentary or letter, no new data |
| 8 | 42338642 | Tanaka S, 2026-06-22 | no: theory, essay or position paper, no new data |
| 9 | 42206281 | Singh R, 2026-05-12 | no: review, no new data |
| 10 | 41858498 | Harris AR, 2026-03-04 | no: theory, essay or position paper, no new data |
| 11 | 41110526 | Escolà-Gascón Á, 2025-10-18 | no: simulation or model only, no new data; its index is not an agreed test for consciousness |
| 12 | 40754292 | Trukovich JJ, 2025-08-05 | no: theory, essay or position paper, no new data |
| 13 | 40862889 | Vallverdú J, 2025-08-07 | no: theory, essay or position paper, no new data |
| 14 | 40257177 | Seth AK, 2025-04-21 | no: theory, essay or position paper, no new data (the core-claim source itself, seth-2025) |
| 15 | 41736970 | Tleuberdinova A, 2026-02-09 | no: theory, essay or position paper, no new data |
| 16 | 41602303 | Niazi SK, 2026-01-12 | no: review, no new data; mentions pilot studies but applies no agreed test for consciousness |
| 17 | 37863713 | Aru J, 2023-10-18 | no: review, no new data |
| 18 | 33969001 | Geraci A, 2021-04-23 | no: theory, essay or position paper, no new data |
| 19 | 31379521 | Pennartz CMA, 2019-07-16 | no: review, no new data |
| 20 | 33500908 | Linson A, 2018-03-08 | no: theory, essay or position paper, no new data |
| 21 | 25575609 | Tannier C, 2015-01-06 | no: does not measure what the test names (medical ethics of stopping artificial nutrition) |
| 22 | 18922687 | Clowes RW, 2008-10-14 | no: theory, essay or position paper, no new data |

### `seth-ai-not-by-computation`

Query run 2026-11-21 09:45 PST; **114 hits**; 40 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 43044230 | Kim P, 2026-11-16 | no: does not measure what the test names (veterinary dental AI) |
| 2 | 42978091 | Wu CF, 2026-11-03 | no: review, no new data |
| 3 | 42283141 | Harris-Watson AM, 2026-06-12 | no: does not measure what the test names (how people perceive minds in AI, not a test of consciousness in AI) |
| 4 | 42658654 | Monti A, 2026-08-27 | no: review, no new data |
| 5 | 42721556 | Wang P, 2026-09-08 | no: review, no new data |
| 6 | 42406739 | D'Alessandro A, 2026-09-01 | no: review, no new data |
| 7 | 43009939 | Karabulut M, 2026-08-14 | no: does not measure what the test names (survey of students' AI literacy) |
| 8 | 42309439 | Bisenbaev AK, 2026-06-17 | no: does not measure what the test names (ant colonies) |
| 9 | 42443865 | Liu CL, 2026-07-13 | no: does not measure what the test names (health chatbot adoption) |
| 10 | 41850148 | Oullier O, 2026-03-14 | no: review, no new data |
| 11 | 41820112 | Pennartz CMA, 2026-03-11 | no: commentary or letter, no new data |
| 12 | 41757900 | Ohmachi Y, 2026-07-01 | no: does not measure what the test names (medical image AI) |
| 13 | 41692418 | Datta SS, 2026-02-15 | no: review, no new data |
| 14 | 41219038 | Butlin P, 2025-11-10 | no: review, no new data (indicator framework; applies no agreed test) |
| 15 | 42169462 | Aras E, 2026-05-01 | no: review, no new data |
| 16 | 42077384 | Lee HS, 2026-04-05 | no: does not measure what the test names (smartwatch fainting prediction) |
| 17 | 42121994 | Vlasiu AR, 2026-04-25 | no: does not measure what the test names (autism screening AI) |
| 18 | 41939423 | Cicerone GC, 2026-04-01 | no: theory, essay or position paper, no new data |
| 19 | 41876853 | Toker D, 2026-03-24 | no: does not measure what the test names (AI used to model disorders of consciousness in brains, not to test AI) |
| 20 | 41911026 | Rudan I, 2026-03-30 | no: commentary or letter, no new data |
| 21 | 41763873 | Fathollahi Y, 2026-02-12 | no: review, no new data |
| 22 | 41751462 | Gunel A, 2026-02-11 | no: review, no new data |
| 23 | 41735504 | Gao Y, 2026-02-24 | no: does not measure what the test names (data privacy system) |
| 24 | 41627361 | Saunanen V, 2026-02-02 | no: theory, essay or position paper, no new data |
| 25 | 42948529 | Chen CC, 2026-10-14 | no: does not measure what the test names (clinical case report) |
| 26 | 42909349 | Gao L, 2026-10-07 | no: review, no new data |
| 27 | 42687985 | Chella A, 2026-08-19 | no: theory, essay or position paper, no new data (proposes a research programme) |
| 28 | 42592127 | Wei Y, 2026-07-29 | no: review, no new data |
| 29 | 42440630 | Krumsvik RJ, 2026-06-22 | no: theory, essay or position paper, no new data |
| 30 | 42006865 | Cao W, 2026-04-02 | no: does not measure what the test names (clinical prediction model) |
| 31 | 41858844 | Alqurni J, 2026-03-04 | no: does not measure what the test names (education survey) |
| 32 | 41835076 | Tarnutzer AA, 2026-02-26 | no: review, no new data |
| 33 | 41696045 | Liang Z, 2026-01-29 | no: does not measure what the test names (a language model's self-talk compared with children's, not a test of consciousness) |
| 34 | 41594836 | Pinna B, 2026-01-21 | no: does not measure what the test names (brain tractography) |
| 35 | 41354552 | Riva G, 2025-12-18 | no: review, no new data |
| 36 | 41469818 | Lori N, 2025-12-30 | no: does not measure what the test names (education model) |
| 37 | 41168276 | He X, 2025-10-30 | no: does not measure what the test names (chatbot first-aid advice) |
| 38 | 40876193 | Birkun AA, 2025-08-27 | no: does not measure what the test names (chatbot first-aid advice) |
| 39 | 40754292 | Trukovich JJ, 2025-08-05 | no: theory, essay or position paper, no new data |
| 40 | 40984999 | Johnston SL, 2025-06-26 | no: commentary or letter, no new data |

### `seth-expectation-speeds-access`

Query run 2026-11-21 09:45 PST; **348 hits**; 40 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 42888378 | Chiusaroli L, 2026-10-16 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 2 | 42786360 | Szanto T, 2026-09-25 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 3 | 42702880 | Taemaitree F, 2026-09-06 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 4 | 42628806 | Shaw JR, 2026-08-21 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 5 | 42456415 | Al-Faraj A, 2026-07-15 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 6 | 42190589 | Sobhani ME, 2026-05-15 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 7 | 42083728 | Gaskin PS, 2026-05-05 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 8 | 42894459 | Costa E, 2026-10-19 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 9 | 42802487 | Kozyra P, 2026-09-27 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 10 | 42790364 | Seid Shazileh SAH, 2026-09-23 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 11 | 42767273 | Phongkhun K, 2026-09-21 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 12 | 41940742 | Furlow LT, 2026-04-07 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 13 | 42902655 | Goenka M, 2026-08-01 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 14 | 42617115 | Plo I, 2026-08-01 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 15 | 42470089 | Lanas-Gimeno A, 2026-07-21 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 16 | 42360175 | Baccelli F, 2026-06-26 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 17 | 42322916 | Chan NC, 2026-06-17 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 18 | 42373752 | Shao C, 2026-06-29 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 19 | 41954861 | Nakajima Y, 2026-04-09 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 20 | 42175904 | Berghmans M, 2026-05-23 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 21 | 42174456 | Iroz CB, 2026-05-22 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 22 | 41310961 | Lee Y, 2025-11-27 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 23 | 41998958 | Liu J, 2026-03-01 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 24 | 41938838 | Budini B, 2026-03-04 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 25 | 41886751 | Wong MYH, 2026-03-26 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 26 | 41443357 | Lv F, 2025-12-22 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 27 | 41916711 | Sa Y, 2026-02-01 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 28 | 41379283 | Guastella V, 2025-12-11 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 29 | 42870899 | Chen Y, 2026-09-29 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 30 | 41481453 | Jackson Z, 2026-01-02 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 31 | 41047692 | Abbass J, 2026-01-01 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 32 | 41262422 | Fraser AG, 2025-09-15 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 33 | 40852775 | Mercadante S, 2025-10-01 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 34 | 39304568 | Panday H, 2024-09-20 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 35 | 41096797 | Papaliagkas V, 2025-09-29 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 36 | 41095961 | Luca SA, 2025-09-28 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 37 | 40696829 | Li YH, 2025-07-22 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 38 | 40441485 | D'Andria Ursoleo J, 2025-05-27 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 39 | 40135752 | Bai Y, 2025-03-26 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |
| 40 | 40578946 | Crispo A, 2025-07-01 | no: off topic (the query word 'breakthrough' or 'predictab*' matched medicine, chemistry or ecology); not about perception or awareness |

### `seth-presence-match`

Query run 2026-11-21 09:45 PST; **36 hits**; 36 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 42334568 | Bufalari I, 2026-06-23 | no: does not measure what the test names (online survey; no manipulation of expected bodily response) |
| 2 | 42591433 | King A, 2026-07-29 | no: theory, essay or position paper, no new data |
| 3 | 42491124 | Ricci V, 2026-07-03 | no: review, no new data |
| 4 | 40694885 | Maister L, 2025-07-21 | no: does not measure what the test names (self-face memory in depersonalisation; no manipulation of expectation) |
| 5 | 41253885 | Gonzalez-Herrero B, 2025-11-18 | no: does not measure what the test names (autism assessment in a neurology clinic) |
| 6 | 41149816 | Scaramuzzino C, 2025-09-29 | no: does not measure what the test names (neurofeedback after surgery) |
| 7 | 40091080 | Bianco F, 2025-03-17 | no: review, no new data |
| 8 | 38613397 | Ballerini M, 2024-04-13 | no: does not measure what the test names (questionnaire study in eating disorders) |
| 9 | 38480797 | Gwyther MPD, 2024-03-13 | no: does not measure what the test names (online survey of waking and dreaming) |
| 10 | 38114633 | Martino M, 2023-12-19 | no: review, no new data |
| 11 | 38142536 | Jamieson G, 2023-12-23 | no: does not measure what the test names (single unplanned episode during EEG; nothing manipulated) |
| 12 | 39173608 | Sarasso P, 2024-08-22 | no: does not measure what the test names (two clinical case studies) |
| 13 | 37230745 | Elkommos S, 2023-05-25 | no: does not measure what the test names (heartbeat-evoked brain response before seizures; expectation not manipulated) |
| 14 | 37018935 | Millman LSM, 2023-03-30 | no: does not measure what the test names (dance therapy trial) |
| 15 | 36543824 | Saini F, 2022-12-21 | no: simulation or model only, no new data |
| 16 | 35410413 | Meneguzzo P, 2022-04-12 | no: does not measure what the test names (time estimation in eating disorders) |
| 17 | 35321264 | Gatus A, 2022-03-07 | no: theory, essay or position paper, no new data |
| 18 | 32757140 | Demartini B, 2020-08-05 | no: does not measure what the test names (mirror-gazing in anorexia; expectation not manipulated) |
| 19 | 32846163 | Salami A, 2020-08-23 | no: review, no new data |
| 20 | 33192765 | Gerrans P, 2020-10-29 | no: theory, essay or position paper, no new data |
| 21 | 32446241 | Nicholson AA, 2020-04-22 | no: does not measure what the test names (brain networks in PTSD) |
| 22 | 31630646 | Bowling NC, 2019-10-21 | no: does not measure what the test names (body-ownership traits in vicarious pain) |
| 23 | 28911803 | Harricharan S, 2017-09-11 | no: does not measure what the test names (vestibular connectivity in PTSD) |
| 24 | 27538601 | Demartini B, 2016-06-23 | no: does not measure what the test names (questionnaire comparison of patient groups) |
| 25 | 27042977 | Nicholson AA, 2016-04-01 | no: does not measure what the test names (insula connectivity in PTSD) |
| 26 | 32755926 | Cathey AJ, 2016-01-01 | no: does not measure what the test names (induces depersonalisation with visual tasks; expected bodily response not set against felt) |
| 27 | 27313548 | Medford N, 2016-06-02 | no: does not measure what the test names (emotional processing in depersonalisation disorder; expectation not manipulated) |
| 28 | 26376409 | Müller LE, 2015-11-01 | no: does not measure what the test names (body signals in borderline personality disorder) |
| 29 | 26106345 | Farb N, 2015-06-09 | no: review, no new data |
| 30 | 24967634 | Sedeño L, 2014-06-26 | no: does not measure what the test names (heartbeat detection in one patient; expectation not manipulated) |
| 31 | 24587061 | Michal M, 2014-02-27 | no: does not measure what the test names (heartbeat accuracy in depersonalisation disorder; expectation not manipulated) |
| 32 | 23932225 | Lemche E, 2013-08-07 | no: does not measure what the test names (emotional faces in depersonalisation disorder) |
| 33 | 23118274 | Weiner E, 2012-11-01 | no: does not measure what the test names (exposure therapy trial) |
| 34 | 24095116 | Critchley HD, 2013-01-01 | no: review, no new data (book chapter) |
| 35 | 22291673 | Seth AK, 2012-01-10 | no: theory, essay or position paper, no new data (the model itself, seth-2012) |
| 36 | 7150514 | Taylor FK, 1982-12-01 | no: theory, essay or position paper, no new data |

### `seth-interoceptive-ownership`

Query run 2026-11-21 09:46 PST; **31 hits**; 31 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 42125933 | Savickaite S, 2026-05-13 | no: does not measure what the test names (movement synchrony, not heartbeat-timed feedback) |
| 2 | 41675468 | Todd J, 2025-12-27 | no: does not measure what the test names (heartbeat-timed feedback only, no out-of-time comparison; full body; pain outcome) |
| 3 | 40997355 | Raoul L, 2025-09-10 | no: does not measure what the test names (touch or movement asynchrony, not heartbeat timing) |
| 4 | 41084361 | Gong W, 2025-10-01 | no: does not measure what the test names (painful shocks timed to the heart cycle; no heartbeat-timed versus out-of-time visual feedback) |
| 5 | 40097357 | Vabba A, 2025-03-01 | TAKEN |
| 6 | 39661868 | Knobel SEJ, 2024-12-11 | no: heartbeat-timed versus out-of-time flashing on a whole virtual body, not a hand (JUDGEMENT CALL, see below) |
| 7 | 38518888 | Yoris AE, 2024-03-20 | no: does not measure what the test names (exercise and heartbeat sensing) |
| 8 | 38135190 | Radziun D, 2023-12-20 | no: does not measure what the test names (touch-only illusion in blind people) |
| 9 | 38280444 | Moffatt J, 2024-01-25 | qualifies (borderline: seen-and-felt taps fall in or out of time with the heartbeat, rather than the hand's appearance pulsing); not taken: the cap allows one study for this prediction and vabba-2025 appeared later |
| 10 | 39723393 | Kaneno Y, 2024-12-11 | no: does not measure what the test names (interoception measures, no heartbeat-timed feedback) |
| 11 | 37816882 | Yamagata T, 2023-10-10 | no: does not measure what the test names (reanalysis of interoceptive accuracy and the illusion, no heartbeat-timed feedback) |
| 12 | 35948567 | Koreki A, 2022-08-10 | no: does not measure what the test names (sense of agency) |
| 13 | 35620242 | Dobrushina OR, 2022-05-11 | no: data descriptor, reports no result on the relation |
| 14 | 34673435 | Dobrushina OR, 2021-09-28 | no: does not measure what the test names (no heartbeat-timed feedback) |
| 15 | 33942318 | Botan V, 2021-05-04 | no: does not measure what the test names (vicarious pain) |
| 16 | 34788333 | Butler AA, 2021-11-17 | no: does not measure what the test names (grasp illusion; no heartbeat-timed feedback) |
| 17 | 33031978 | Horváth Á, 2020-09-16 | no: does not measure what the test names (no heartbeat-timed feedback) |
| 18 | 32932793 | Stern Y, 2020-09-11 | no: does not measure what the test names (agency in virtual reality) |
| 19 | 32162704 | Betka S, 2020-03-12 | no: does not measure what the test names (breathing-timed feedback on a whole body) |
| 20 | 31800367 | Monti A, 2019-12-04 | no: does not measure what the test names (breathing-timed feedback on a whole body) |
| 21 | 30878983 | Crucianelli L, 2019-03-15 | no: protocol, no results |
| 22 | 28532579 | Crucianelli L, 2017-05-01 | no: does not measure what the test names (affective touch; no heartbeat-timed feedback) |
| 23 | 29915337 | Heydrich L, 2018-06-18 | no: heartbeat-timed versus out-of-time flashing on a whole body, not a hand (same call as rank 6) |
| 24 | 28334126 | Sel A, 2017-11-01 | no: heartbeat-timed flashing on a face (self-face recognition), not a hand |
| 25 | 27880880 | Filippetti ML, 2016-11-20 | no: does not measure what the test names (measures the illusion's effect on heartbeat sensing, the reverse direction) |
| 26 | 28955213 | Fischer D, 2017-09-12 | no: does not measure what the test names (body-scan training) |
| 27 | 27511016 | Park HD, 2016-08-01 | no: does not measure what the test names (brain responses to heartbeats during a touch-induced full-body illusion) |
| 28 | 25676677 | Ronchi R, 2015-02-10 | no: heartbeat-timed feedback on a whole body, single patient (same call as rank 6) |
| 29 | 25498876 | Schauder KB, 2014-12-10 | no: does not measure what the test names (no heartbeat-timed feedback) |
| 30 | 23993906 | Suzuki K, 2013-08-28 | qualifies; not taken: the cap allows one study for this prediction and it is older (already in the records as suzuki-2013) |
| 31 | 21208964 | Tsakiris M, 2011-01-05 | no: does not measure what the test names (heartbeat sensing and the illusion; no heartbeat-timed feedback) |

### `seth-low-interoception-more-illusion`

Query run 2026-11-21 09:47 PST; **14 hits**; 14 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 40997355 | Raoul L, 2025-09-10 | TAKEN |
| 2 | 38518888 | Yoris AE, 2024-03-20 | qualifies (heartbeat counting and the rubber hand illusion both measured; the abstract reports group comparisons); not taken: cap, older |
| 3 | 38135190 | Radziun D, 2023-12-20 | no: does not measure what the test names (touch-only illusion in blind people, no seen stroking) |
| 4 | 38280444 | Moffatt J, 2024-01-25 | qualifies (exploratory analysis of heartbeat counting with the illusion); not taken: cap, older |
| 5 | 39723393 | Kaneno Y, 2024-12-11 | qualifies (classical illusion and heartbeat counting); not taken: cap, older |
| 6 | 37816882 | Yamagata T, 2023-10-10 | qualifies (reanalysis of two datasets); not taken: cap, older |
| 7 | 35620242 | Dobrushina OR, 2022-05-11 | no: data descriptor, reports no result on the relation |
| 8 | 34673435 | Dobrushina OR, 2021-09-28 | qualifies (heartbeat detection and illusion drift in the same people); not taken: cap, older |
| 9 | 33942318 | Botan V, 2021-05-04 | no: does not measure what the test names (vicarious pain profiles) |
| 10 | 28532579 | Crucianelli L, 2017-05-01 | qualifies (heartbeat counting and the illusion); not taken: cap, older |
| 11 | 27880880 | Filippetti ML, 2016-11-20 | no: does not measure what the test names (measures the illusion's effect on heartbeat sensing, the reverse direction) |
| 12 | 25498876 | Schauder KB, 2014-12-10 | qualifies; not taken: cap, older |
| 13 | 23993906 | Suzuki K, 2013-08-28 | qualifies; not taken: cap, older (already in the records as suzuki-2013) |
| 14 | 21208964 | Tsakiris M, 2011-01-05 | qualifies; not taken: cap, older (it is the earlier finding the 2012 passage reads) |

### `seth-interoceptive-suppression`

Query run 2026-11-21 09:47 PST; **52 hits**; 40 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 41690396 | Strigo IA, 2026-02-12 | no: does not measure what the test names (brain activity while anticipating pain, not the response to a predicted versus unpredicted body signal) |
| 2 | 43022233 | Li X, 2026-10-29 | no: review, no new data |
| 3 | 42903131 | Gomez Uncu YM, 2026-10-06 | no: theory, essay or position paper, no new data |
| 4 | 42780841 | Yang S, 2026-09-09 | no: review, no new data |
| 5 | 42079303 | Luan P, 2026-04-17 | no: protocol, no results |
| 6 | 40181049 | Patchitt J, 2025-04-03 | no: false heartbeat-like pulses on the skin; the insula contrast is faster versus slower feedback, not predicted versus prediction-breaking body signals (closest call in this list) |
| 7 | 39909338 | Skałbania J, 2025-02-03 | no: does not measure what the test names (cognitive load and taste choices) |
| 8 | 41211594 | Flockton JR, 2025-10-24 | no: survey and theory; no brain measure |
| 9 | 40979198 | Rushani S, 2025-09-05 | no: theory, essay or position paper, no new data (perspective) |
| 10 | 40740255 | Park H, 2025-07-16 | no: does not measure what the test names (prediction errors about money rewards, not body signals) |
| 11 | 39587011 | Paulus MP, 2025-01-01 | no: review, no new data |
| 12 | 39558709 | Sojka P, 2024-11-19 | no: does not measure what the test names (attention to heartbeat in a patient group; predictability not manipulated) |
| 13 | 38946148 | Kipping M, 2024-06-30 | no: does not measure what the test names (brain stimulation of the insula) |
| 14 | 38918578 | Kaldewaij R, 2024-06-25 | no: does not measure what the test names (ketamine and touch) |
| 15 | 39273056 | Iezzi D, 2024-09-04 | no: does not measure what the test names (mouse insula after prenatal exposure) |
| 16 | 38849067 | Strigo IA, 2024-06-06 | no: review, no new data |
| 17 | 39403362 | Soleymani MB, 2024-05-01 | no: does not measure what the test names (brain response to drug pictures) |
| 18 | 37432752 | Picard F, 2023-09-01 | no: theory, essay or position paper, no new data |
| 19 | 37302437 | Benson S, 2023-06-10 | no: does not measure what the test names (visceral pain with cues, inflammation and mood; predictability not compared) |
| 20 | 35907498 | Hübner AM, 2022-07-27 | no: does not measure what the test names (predictability of seen facial emotions, not body signals) |
| 21 | 36162077 | McIntosh RC, 2022-09-06 | no: does not measure what the test names (insula during heartbeat detection and depression) |
| 22 | 34998254 | Le TM, 2022-01-03 | no: does not measure what the test names (resting connectivity and alcohol expectancy) |
| 23 | 34672986 | Harrison OK, 2021-10-20 | TAKEN |
| 24 | 33875493 | Finnegan SL, 2021-11-18 | no: does not measure what the test names (breathlessness clusters) |
| 25 | 33976383 | Koenen LR, 2021-05-11 | no: does not measure what the test names (conditioning across senses) |
| 26 | 33615622 | Sojka P, 2020-12-07 | no: does not measure what the test names (white matter and heartbeat accuracy) |
| 27 | 32661840 | McMorris T, 2020-10-01 | no: review, no new data |
| 28 | 32061891 | Stefanova E, 2020-02-13 | no: review, no new data |
| 29 | 39015778 | Gerrans P, 2020-12-30 | no: review, no new data |
| 30 | 30229711 | Eckstrand KL, 2018-09-19 | no: does not measure what the test names (reward prediction errors) |
| 31 | 31061515 | Kirk U, 2019-05-06 | no: does not measure what the test names (reward prediction errors) |
| 32 | 29608992 | McMorris T, 2018-03-30 | no: review, no new data |
| 33 | 28210930 | Schienle A, 2018-02-01 | no: does not measure what the test names (nocebo smell suggestion) |
| 34 | 30390838 | Lutz K, 2018-09-10 | no: review, no new data |
| 35 | 30297988 | Edwards DJ, 2018-09-21 | no: does not measure what the test names (touch therapy trial) |
| 36 | 28714434 | Berner LA, 2017-07-17 | no: does not measure what the test names (breathing load in anorexia; predictability not manipulated) |
| 37 | 28424393 | Ohira H, 2017-04-01 | no: review, no new data |
| 38 | 26854560 | Labrenz F, 2016-02-12 | qualifies (predictable versus unpredictable visceral pain, brain responses measured); not taken: cap, older |
| 39 | 27867351 | Goodyear K, 2016-11-04 | no: does not measure what the test names (advice-taking) |
| 40 | 25971601 | Becker CA, 2015-05-13 | no: does not measure what the test names (thirst and pictures of drinks) |

### `seth-feeling-from-prediction`

Query run 2026-11-21 09:48 PST; **37 hits**; 37 screened.

| rank | Europe PMC id | first author, date | verdict |
|---|---|---|---|
| 1 | 42963537 | Patchitt J, 2026-11-01 | no: does not measure what the test names (resting brain networks that predict who is swayed by false feedback; does not report whether false feedback changed emotion) |
| 2 | 42294597 | Parrotta E, 2026-06-15 | no: false heartbeat feedback changed reported PAIN, not emotion, and actual heart rate changed too (JUDGEMENT CALL, see below) |
| 3 | 38663458 | Hill MW, 2024-04-23 | TAKEN |
| 4 | 39845548 | Ikarashi H, 2025-01-08 | no: does not measure what the test names (outcome is actual heart-rate variability, not reported emotion) |
| 5 | 35143921 | Bečev O, 2022-02-08 | no: does not measure what the test names (brain responses to sounds; no emotion report) |
| 6 | 31235576 | Iodice P, 2019-06-24 | no: does not measure what the test names (perceived effort, not emotion) |
| 7 | 30923745 | Costa J, 2017-06-01 | qualifies (false slow heart-rate feedback and anxiety); not taken: cap, older |
| 8 | 26676918 | Judah MR, 2016-06-01 | no: does not measure what the test names (attention biases; false feedback used only to induce self-focus) |
| 9 | 26956658 | Judah MR, 2015-12-29 | no: does not measure what the test names (error monitoring; false feedback used only to induce self-focus) |
| 10 | 26167147 | Forster M, 2015-06-26 | no: does not measure what the test names (liking of drawings after false skin-conductance feedback, not felt emotion) |
| 11 | 23312431 | Makkar SR, 2012-08-02 | qualifies (false heart-rate increase or decrease and negative feelings); not taken: cap, older |
| 12 | 22309028 | Ma-Kellams C, 2012-02-06 | qualifies (Study 1: false heart-rate feedback and reported feelings); not taken: cap, older |
| 13 | 21432638 | Weibel D, 2011-05-24 | qualifies (false heart-rate feedback and enjoyment); not taken: cap, older |
| 14 | 18561016 | Stone JM, 2008-06-17 | no: does not measure what the test names (sexual arousal and erection, by false tumescence feedback) |
| 15 | 19125336 | Karsdorp PA, 2009-01-06 | no: does not measure what the test names (perceived heart symptoms, not emotion) |
| 16 | 18692167 | Story TJ, 2008-06-27 | qualifies (false feedback and anxiety); not taken: cap, older |
| 17 | 17579718 | Gray MA, 2007-06-20 | qualifies (false heart-rate feedback and judged emotional intensity of faces, with brain imaging); not taken: cap, older |
| 18 | 17477208 | Barefoot JC, 2005-07-01 | no: does not measure what the test names (rated attractiveness of photographs) |
| 19 | 11195911 | Crucian GP, 2000-12-01 | no: does not measure what the test names (rated attractiveness of pictures) |
| 20 | 10432800 | Phillips GC, 1999-07-01 | no: does not measure what the test names (heartbeat-counting performance) |
| 21 | 7673538 | Palace EM, 1995-08-01 | no: does not measure what the test names (genital arousal, by false feedback) |
| 22 | 1784650 | Shahidi S, 1991-12-01 | qualifies (false heart-rate feedback and embarrassment); not taken: cap, older |
| 23 | 3341996 | Ehlers A, 1988-01-01 | qualifies on its title (anxiety after false heart-rate feedback; no abstract); not taken: cap, older |
| 24 | 486338 | Linton JC, 1979-03-01 | qualifies on its title and abstract (emotional response to false feedback); not taken: cap, older |
| 25 | 887709 | Liebhart EH, 1977-06-01 | unclear from the title alone (no abstract); not needed: cap, older |
| 26 | 993982 | McCanne TR, 1976-11-01 | no: does not measure what the test names (conditioning and a perception test) |
| 27 | 974449 | Thornton EW, 1976-08-01 | qualifies (reported affect after false feedback); not taken: cap, older |
| 28 | 21287016 | Hendrick C, 1976-03-01 | no: does not measure what the test names (attitude change) |
| 29 | 1195088 | Hendrick C, 1975-06-01 | no: does not measure what the test names (attitude change) |
| 30 | 4429534 | Decaria MD, 1974-09-01 | qualifies on its title (anxiety reports; no abstract); not taken: cap, older |
| 31 | 4418693 | Botto RW, 1974-08-01 | no: does not measure what the test names (attitudes to sexual stimuli) |
| 32 | 4825211 | Borkovec TD, 1974-04-01 | qualifies on its title (speech anxiety; no abstract); not taken: cap, older |
| 33 | 4735700 | Borkovec TD, 1973-05-01 | no: does not measure what the test names (avoidance behaviour) |
| 34 | 5019746 | Stern RM, 1972-01-01 | unclear from the title alone (no abstract); not needed: cap, older |
| 35 | 5100717 | Barefoot JC, 1971-02-01 | no: does not measure what the test names (rated attractiveness) |
| 36 | 5483868 | Reisman S, 1970-12-01 | no: does not measure what the test names (attitude consistency) |
| 37 | 5969996 | Valins S, 1966-10-01 | no: does not measure what the test names (rated attractiveness) |

