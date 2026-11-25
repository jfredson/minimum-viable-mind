# The sensorimotor theory: screening the per-prediction searches, 2026-11-21

First reading, one reader (Claude, claude-opus-5-5). Draft only: nothing here is in the
repository. Every fact comes from a source opened in this task on 2026-11-21: the seven results
files in `data/tracker/search-runs-2026-11-21/`, the Europe PMC and OpenAlex records named
below, the two open full texts, and O'Regan and Noë 2001 (the copy on kevin-oregan.net), whose
quoted passages were checked again against the text pulled from that PDF.

The method is the one fixed in `data/tracker/searches-2026-11-21.toml` before any search ran:
screen each prediction's results in rank order, up to 40, on title and abstract only; a result
qualifies if it reports new data (or a reanalysis) and measures what that prediction's own test
wording names; take the five most recent qualifying studies across the theory's lists, at most
one per prediction.

## In short

- **Screened:** 230 results over seven searches (40 each, except 23 and 7 where the search
  found fewer). **42 different studies qualified** (43 qualifying lines; one study qualifies in
  two lists).
- **Taken (5):** Thomas and Didierjean 2026 (change blindness), Hense and colleagues 2026
  (missed unexpected objects), Liu and colleagues 2026 (no single brain state), Maimon and
  colleagues 2022 (sensory substitution), Sekiyama and colleagues 2012 (reversing spectacles).
- **Opened (2):** Hense 2026 and Maimon 2022. **Not opened (3):** Thomas 2026, Liu 2026 and
  Sekiyama 2012, all behind subscriptions; they keep their places with no judgement.
- **Judgements (3):** two commitment readings (Hense: "before"; Maimon: "unclear") and one
  outcome reading (Hense: "for"). None of them can move a score; see "Rule results".

## The choice, and how the cap was applied

The most recent qualifying result in each list, by earliest public appearance:

| prediction | most recent qualifying study | first public | place |
|---|---|---|---|
| change blindness (`sm-change-blindness`) | Thomas and Didierjean, `thomas-2026` | 2026-11-13 (publication; a public data-only project on the Open Science Framework from 2026-09-09) | 1st, taken |
| missed unexpected objects (`sm-inattentional`) | Hense and colleagues, `hense-2026` | 2026-10-15 | 2nd, taken |
| no single brain state (`sm-no-ncc`) | Liu and colleagues, `liu-2026` | 2026-05-01 | 3rd, taken |
| sensory substitution (`sm-substitution`) | Maimon and colleagues, `maimon-2022` | 2022-06-22 | 4th, taken |
| reversing goggles (`sm-inversion`) | Sekiyama and colleagues, `sekiyama-2012` | 2012-06-26 | 5th, taken |
| moving the camera yourself (`sm-active-control`) | Auvray, Hanneton, Lenay and O'Regan (PMID 16385644) | 2005-12-01 | 6th, not taken |
| the colour experiment (`sm-colour-contingent`) | none in the 40 screened | | |

**How the cap worked.** Going through all qualifying results newest first, a study is taken if
its prediction's place is still free. Several studies newer than Liu and colleagues (2026-05-01)
qualified for change blindness and for missed objects (for example Simons and Ding, 2026-08-20),
but those two places were already filled by newer studies (Thomas, then Hense), so the cap passed
over them. In all, the cap set aside 17 further qualifying change-blindness studies and 14 further
missed-object studies (plus Liu, whose case is below).

**The one study that qualified for two predictions.** Liu and colleagues 2026 appears in two
lists: first in the no-single-brain-state search, and seventh in the missed-objects search, where
it also qualifies. When it was reached, the missed-objects place was already Hense's, and the
no-single-brain-state place was free. It was therefore taken **for `sm-no-ncc`**, and, as the
method says ("taken once and judged for both"), it would be judged for **both** `sm-no-ncc` and
`sm-inattentional`. That reading gives the missed-objects prediction two judged studies (Hense,
and Liu by the judged-for-both clause). The other possible reading, that the cap forbids a second
judged study for a prediction, would judge Liu only for `sm-no-ncc`. The difference is moot for
now, because Liu's paper was not opened and has no judgements.

**Pivotal screening calls.** The five taken depend on three calls that a second reader could make
differently:
- Stiles, Zheng and Shimojo 2015 (active-control list, rank 13) was ruled out: learning tracked
  the users' own head movements, but no group received the same input without controlling it, so
  the result is a correlation that cannot count for or against the test as worded. Had it
  qualified, it (2015) would have taken the fifth place from Sekiyama (2012).
- Liu 2026 qualifies for `sm-no-ncc` because it asks whether a brain response tracks seeing once
  report is removed, which is the test wording's "across reports". If a reader says a single
  no-report design does not compare across reports, the place goes to Wagener and Nieder 2024
  (crow neurons; 2024-03-01), and the five are otherwise unchanged.
- Slow-change studies (change-blindness list, ranks 3, 21, 28) were ruled out because the change
  is gradual rather than hidden by a flash or cut; this does not change the choice.

**What the list-by-list screening left out.** Each result was judged only against the
prediction whose search found it, as the method's step 2 reads. Two studies fit another
prediction's wording better than their own list's: Siegle and Warren 2010 (perceived distance
with a light-to-vibration device; active-control list) fits the substitution prediction, and
Hense 2026 (taken for missed objects) is also a search for the brain activity that goes with
seeing under minimal report, which the no-single-brain-state prediction names. Neither was
counted for the other prediction.

## What the cap did to the two predictions that cannot move a score

Change blindness and missed unexpected objects do not separate the theory from its rivals (ruling
C2 as read by John: global workspace and recurrent processing theory predict the same missed
reports). Their studies can be judged but can never count. The method still treats them as
predictions, and they are the two busiest topics (329 and 324 hits; 18 and 16 qualifying lines
in the 40 screened). Without the cap they would have filled all five places with studies that
cannot count. With the cap they take one place each, two of the five, and the other three places
go to predictions that do separate (`sm-no-ncc`, `sm-substitution`, `sm-inversion`). So the cap
did what it was set up to do; but two of five places still went to predictions that cannot move
a score, and the theory's only prediction that separates it from rivals on a rival's contrary
words (`sm-no-ncc`) got its study only because Liu happened to appear in that list as well.

## Every unsure judgement

- **`com-maimon-2022-sm-substitution`, read "unclear".** The 2001 statement covers stimulation
  that changes as the user moves; the paper describes pictures turned into sound on a website or
  app and played back, and never says he moved the camera himself while listening. One remark
  suggests he did aim a camera at times, and nine months is long practice, so a reader could read
  "before". This reader would then put the outcome as mixed: he calls it seeing, but also sees
  colours when colour words are spoken, with no device, and the authors leave open whether it is
  perception or imagery. The same 2001 publication says sound reaching the auditory nerve without
  movement is heard as sound, which cuts against counting a played-back device. Verify entry
  `v-sm2-maimon-active-use`.
- **`out-hense-2026-sm-inattentional`, read "for".** 38 of 47 uninformed people missed the
  background lines (worked out from the exclusion counts; the authors give "more than 80%" for
  all groups together). The lines were lighter grey among black lines and tuned in pilots so
  uninformed people would miss them, so whether they were "clearly visible" is arguable; people
  told about them did see them.
- `com-hense-2026-sm-inattentional`, read "before", is not marked unsure.

## Not opened

| study | why | sign-in John would need |
|---|---|---|
| Thomas and Didierjean 2026 (Cognition) | subscription; no open copy; the Open Science Framework project holds only a data spreadsheet | ScienceDirect (Elsevier) |
| Liu and colleagues 2026 (Journal of Experimental Psychology: General) | subscription; no open copy or preprint found | APA PsycNet |
| Sekiyama, Hashimoto and Sugita 2012 (Acta Psychologica) | subscription; no open copy | ScienceDirect (Elsevier) |

No paywall or robot check was tried. Of the three, Liu matters most: it is the only chosen
study on the theory's one prediction that separates it from rivals on their own contrary words.
Also not opened: the three supplementary videos of Maimon 2022, Buchs and colleagues 2021 (the
training description it cites), and the SSRN version of Hense 2026 (`v-sm2-hense-preprint-date`).

## Rule results John may not have intended (applied as written)

1. **The searches found plenty, but none of it counts yet.** 42 studies qualified, against one
   under the earlier search by the theory's name. Of the five taken, three are not opened (Thomas,
   Liu and Sekiyama), Maimon is read "unclear", and Hense, read "before" and "for", sits on a
   prediction that does not separate. The theory still has no counted study, so still no support
   score.
2. **The cap kept the busy, non-separating topics to two places, but not to zero.** The method
   counts every prediction, whether it can move a score or not. A rule that skipped
   non-separating predictions when choosing would have taken four studies (Liu, Maimon, Sekiyama
   and the active-camera study, Auvray 2005, which is co-authored by O'Regan, so own-lab dating
   would apply) and left the fifth place empty, since the colour experiment has no qualifying
   result.
3. **"At most one per prediction" against "judged for both".** The method's two sentences pull
   apart for a study that qualifies for two predictions, one of them already filled. Applied as
   above: the study takes the free place and is judged for both. Moot here (Liu is not opened),
   but it will recur for other theories.
4. **List-by-list screening misses fits across lists** (Siegle and Warren 2010; Hense 2026 for the
   brain-state prediction). The method's wording ("measures what the prediction's own test wording
   names") was read as the prediction whose search found the result.
5. **The colour experiment's search finds nothing it was meant to find.** All 40 results are
   about eye movements or colour separately; none trains people with a colour tied to gaze. The
   prediction's own record says the proponents were testing it themselves in 2001 (O'Regan and
   colleagues 2001, not opened), which a hand search might find, but the method allows none.
6. **Earliest public appearance and a public data project.** Thomas 2026's data spreadsheet was
   public on the Open Science Framework from 2026-09-09, two months before the paper. The method
   names a preprint or publication; a data-only project is neither. It changes nothing here.

## Every screened line

Each line: rank, first author, Europe PMC first-publication date, PMID, title, verdict, reason.
"The cap" means the method's rule of at most one study per prediction.

### `sm-colour-contingent`: the colour experiment (a patch that changes colour with where the eyes point)

Hits: 71. Screened: 40 (ranks 1 to 40). Query run 2026-11-21 09:51 PST.

1. Dimigen and Stein, 2026-05-11, PMID 42115564, "Advantages and artifacts of high-speed OLED monitors for vision, eye-tracking, and EEG research.": does not qualify. a methods paper on monitor timing; no colour-linked-to-gaze training.
2. Polgári and Schütz, 2026-04-27, PMID 42045734, "Visual working memory-related corrective saccade biases are amplified by task demands, without updating working memory content.": does not qualify. working memory and corrective eye movements; no colour-linked-to-gaze training or colour judgements.
3. Chiu and Golomb, 2026-04-15, PMID 41984303, "Top-down motivation both decreases and increases feature interference following a saccade.": does not qualify. feature mixing errors after an eye movement; no training in which a colour changes with where the eyes point.
4. Nir and Deouell, 2026-04-10, PMID 41963708, "Systematic classification differences across eye movement detection algorithms.": does not qualify. a comparison of eye-movement detection algorithms; off topic: does not measure what the test wording names.
5. Xia et al., 2026-03-10, PMID 41812398, "Stage-specific priming of pop-out effects in the target-feature memory encoding and retrieval.": does not qualify. priming in visual search; off topic: does not measure what the test wording names.
6. Cajar and Laubrock, 2026-03-06, PMID 41790310, "Color needs luminance for visual selection during scene search.": does not qualify. colour and brightness in scene search; no colour-linked-to-gaze training.
7. Liu et al., 2025-11-28, PMID 41375496, "Associations Between REM Sleep-like Posture Expression and Cognitive Flexibility in 2-Month-Old Japanese Black Calves.": does not qualify. calves' sleep posture; off topic: does not measure what the test wording names.
8. Ling and Hiraki, 2025-10-14, PMID 41087485, "Infants organize their learning process based on the same or different informants.": does not qualify. infant learning; off topic: does not measure what the test wording names.
9. Luo et al., 2025-07-02, PMID 40723683, "Transferable Modulation of Cognitive Control: The Cross-Task Role of Conflict Adaptation in Thematic Roles Assignment in Chinese.": does not qualify. language and cognitive control; off topic: does not measure what the test wording names.
10. Martel and Madelain, 2025-06-04, PMID 40465421, "Ineffective cues for contextual saccade adaptation.": does not qualify. saccade adaptation with colour as a cue; measures eye-movement size, not how colours look.
11. Simpson et al., 2025-05-26, PMID 40415698, "Feedback-Driven Learning Through Eye Movements in Autism Spectrum Disorder.": does not qualify. eye-movement learning in autism; off topic: does not measure what the test wording names.
12. Chen and Lee, 2024-06-05, PMID 38839714, "Peripheral vision contributes to implicit attentional learning: Findings from the "mouse-eye" paradigm.": does not qualify. peripheral vision and attention learning; no colour-linked-to-gaze training.
13. Garner et al., 2024-04-28, PMID 38679809, "Assessing the influence of dopamine and mindfulness on the formation of routines in visual search.": does not qualify. routines in visual search; off topic: does not measure what the test wording names.
14. Gutzeit et al., 2024-01-09, PMID 38199168, "Eye did this! Sense of agency in eye movements.": does not qualify. sense of agency for eye movements (a colour change follows a saccade); measures felt timing, not whether the colours come to look alike.
15. Kunkel Genannt Bode et al., 2022-11-16, PMID 36384816, "Gaze-contingent display technology can help to reduce the ipsilesional attention bias in hemispatial neglect following stroke.": does not qualify. gaze-linked display as a treatment for neglect; no colour judgements.
16. Lammers et al., 2022-04-01, PMID 35363793, "Mid-range visual deficits after stroke: Prevalence and co-occurrence.": does not qualify. visual deficits after stroke; off topic: does not measure what the test wording names.
17. Conway et al., 2021-09-01, PMID 34415269, "Telemedicine Evaluations in Neuro-Ophthalmology During the COVID-19 Pandemic: Patient and Physician Surveys.": does not qualify. telemedicine survey; off topic: does not measure what the test wording names.
18. Hamblin-Frohman and Becker, 2021-04-13, PMID 33862440, "The attentional template in high and low similarity search: Optimal tuning or tuning to relations?": does not qualify. attentional templates in search; off topic: does not measure what the test wording names.
19. Braun et al., 2021-06-01, PMID 34144606, "Age effects on saccadic suppression of luminance and color.": does not qualify. how seeing of colour is dampened during eye movements, by age; no training.
20. Van der Stigchel et al., 2020-09-01, PMID 32915955, "Transsaccadic perception is affected by saccade landing point deviations after saccadic adaptation.": does not qualify. combining what is seen across an eye movement after saccade adaptation; no colour training.
21. Cajar et al., 2020-07-01, PMID 38755794, "How spatial frequencies and color drive object search in real-world scenes: A new eye-movement corpus.": does not qualify. an eye-movement data set for object search; no colour-linked-to-gaze training.
22. Westerberg et al., 2020-03-01, PMID 32229500, "Priming of Attentional Selection in Macaque Visual Cortex: Feature-Based Facilitation and Location-Based Inhibition of Return.": does not qualify. priming of attention in monkey cortex; off topic: does not measure what the test wording names.
23. Lixenberg et al., 2020-01-15, PMID 31940216, "Encoding of eye movements explains reward-related activity in cerebellar simple spikes.": does not qualify. cerebellar activity and eye movements; off topic: does not measure what the test wording names.
24. Kayhan et al., 2019-02-16, PMID 30780046, "Infants differentially update their internal models of a dynamic environment.": does not qualify. infant internal models; off topic: does not measure what the test wording names.
25. Li et al., 2018-10-29, PMID 30384128, "Model of Multiple Identity Tracking (MOMIT) 2.0: Resolving the serial vs. parallel controversy in tracking.": does not qualify. a model of tracking several objects; no new data on colour.
26. Ort et al., 2018-11-01, PMID 30088257, "Lack of free choice reveals the cost of multiple-target search within and across feature dimensions.": does not qualify. cost of searching for several targets; off topic: does not measure what the test wording names.
27. Zhou et al., 2018-07-01, PMID 29435825, "Word segmentation by alternating colors facilitates eye guidance in Chinese reading.": does not qualify. colour-alternated word boundaries in reading; off topic: does not measure what the test wording names.
28. Beck and Hollingworth, 2017-02-01, PMID 28134550, "Competition in saccade target selection reveals attentional guidance by simultaneously active working memory representations.": does not qualify. working memory and saccade target choice; off topic: does not measure what the test wording names.
29. Falciati and Maioli, 2017-12-18, PMID 29326576, "Dynamic Changes in Upper-Limb Corticospinal Excitability during a 'Pro-/Anti-saccade' Double-Choice Task.": does not qualify. spinal excitability in a saccade task; off topic: does not measure what the test wording names.
30. Olmos-Solis et al., 2017-08-14, PMID 29157407, "Oculomotor measures reveal the temporal dynamics of preparing for search.": does not qualify. preparing for search; off topic: does not measure what the test wording names.
31. Armstrong, 2017-05-31, PMID 28805589, "Visual Dysfunction in Parkinson's Disease.": does not qualify. visual problems in Parkinson's disease; a review or survey, no new data.
32. Zimmermann et al., 2016-05-01, PMID 27139583, "Adaptation to size affects saccades with long but not short latencies.": does not qualify. size adaptation and saccades; no colour.
33. Bachy and Zaidi, 2016-03-01, PMID 26974918, "Properties of lateral interaction in color and brightness induction.": does not qualify. colour and brightness induction; no eye-linked training.
34. Nuthmann and Malcolm, 2016-01-01, PMID 26824640, "Eye guidance during real-world scene search: The role color plays in central and peripheral vision.": does not qualify. colour in central and peripheral vision during search; no training in which a colour changes with gaze.
35. Armstrong and Kergoat, 2015-07-01, PMID 26094831, "Oculo-visual changes and clinical considerations affecting older patients with dementia.": does not qualify. older patients with dementia; a review or survey, no new data.
36. Cecala et al., 2015-05-20, PMID 25995353, "Context cue-dependent saccadic adaptation in rhesus macaques cannot be elicited using color.": does not qualify. colour as a cue for saccade adaptation in monkeys; measures eye-movement size.
37. Heimler et al., 2015-03-29, PMID 25829265, "Finding the balance between capture and control: Oculomotor selection in early deaf adults.": does not qualify. eye-movement capture in deaf adults; off topic: does not measure what the test wording names.
38. Wright et al., 2014-11-10, PMID 25384235, "Functional fixedness: The functional significance of delayed disengagement based on attention set.": does not qualify. delayed disengagement of attention; off topic: does not measure what the test wording names.
39. Armstrong, 2015-01-01, PMID 26599301, "Oculo-Visual Dysfunction in Parkinson's Disease.": does not qualify. visual problems in Parkinson's disease; a review or survey, no new data.
40. Marino et al., 2015-09-30, PMID 26550008, "Can we resist another person's gaze?": does not qualify. resisting another person's gaze; off topic: does not measure what the test wording names.

Counts: 0 taken, 0 qualify but not taken, 40 do not qualify.

### `sm-inversion`: inverting or reversing goggles

Hits: 84. Screened: 40 (ranks 1 to 40). Query run 2026-11-21 09:51 PST.

1. Wang et al., 2025-09-27, PMID 41016216, "Proprioception and vision relationship in aimed movement with restricted and reversed vision.": does not qualify. aiming movements under reversed vision; measures movement speed, not how the scene looks.
2. Fang et al., 2024-07-15, PMID 39007414, "TET3 Contributes to Exercise-Induced Functional Axon Regeneration and Visual Restoration.": does not qualify. axon regrowth in animals; off topic: does not measure what the test wording names.
3. Guo et al., 2025-02-03, PMID 39900579, "Sensorimotor environment but not task rule reconfigures population dynamics in rhesus monkey posterior parietal cortex.": does not qualify. monkey parietal cortex during mirror-reversed reaching; no report of how the world looks.
4. Zhao et al., 2023-08-16, PMID 37631167, "Simultaneous Quantification and Visualization of Photosynthetic Pigments in Lycopersicon esculentum Mill. under Different Levels of Nitrogen Application with Visible-Near Infrared Hyperspectral Imaging Technology.": does not qualify. plant pigments; off topic: does not measure what the test wording names.
5. Mathieu et al., 2023-04-28, PMID 37121267, "Seeing our hand or a tool during visually-guided actions: Different effects on the somatosensory and visual cortices.": does not qualify. mirror-reversed tracing with hand or tool; measures performance and brain responses, not how the scene looks.
6. He et al., 2023-08-17, PMID 37663341, "Perception of rigidity in three- and four-dimensional spaces.": does not qualify. telling rigid from non-rigid motion of 4-D shapes; no inverting goggles.
7. Zou et al., 2023-02-17, PMID 36874454, "Case report: Robot-assisted laparoscopic partial nephrectomy for renal cell carcinoma in a patient with situs inversus totalis and abdominal cocoon.": does not qualify. a surgical case report; off topic: does not measure what the test wording names.
8. Goldenkoff et al., 2020-11-18, PMID 33220339, "Reversal of Visual Feedback Modulates Somatosensory Plasticity.": does not qualify. short training with reversing spectacles; measures touch-cortex excitability and motor skill, not how the scene looks.
9. Temple et al., 2018-03-29, PMID 29651250, "Efficacy of Stochastic Vestibular Stimulation to Improve Locomotor Performance During Adaptation to Visuomotor and Somatosensory Distortion.": does not qualify. vestibular stimulation during distorted-vision walking; motor measures only.
10. Keane et al., 2018-03-12, PMID 29593580, "Self-Reported Visual Perceptual Abnormalities Are Strongly Associated with Core Clinical Features in Psychotic Disorders.": does not qualify. self-reported visual abnormalities in psychosis; no goggles.
11. Maxime et al., 2016-09-10, PMID 28149394, "Reduced plantar sole sensitivity facilitates early adaptation to a visual rotation pointing task when standing upright.": does not qualify. foot-sole sensitivity and visual-rotation pointing; motor measures only.
12. Lebar et al., 2015-07-17, PMID 26191651, "Neural correlates for task-relevant facilitation of visual inputs during visually-guided hand movements.": does not qualify. brain responses during visually guided hand movements; no inversion experience measured.
13. Kuang and Gail, 2014-09-16, PMID 25218421, "When adaptive control fails: Slow recovery of reduced rapid online control during reaching under reversed vision.": does not qualify. fast arm corrections under reversed vision; motor measures only.
14. Barton et al., 2014-08-07, PMID 25104829, "Paradoxical visuomotor adaptation to reversed visual input is predicted by BDNF Val66Met polymorphism.": does not qualify. a gene variant and adaptation to reversed input; motor measures only.
15. Lemieux et al., 2013-11-22, PMID 24258770, "Balance control interferes with the tracing performance of a pattern with mirror-reversed vision in older persons.": does not qualify. mirror tracing and balance in older people; motor measures only.
16. Sato et al., 2014-10-24, PMID 25358393, "Prism adaptation and perceptual skill learning deficits in early-stage Parkinson's disease.": does not qualify. prism adaptation in Parkinson's disease; motor and skill measures, not how the scene looks.
17. Lillicrap et al., 2013-05-23, PMID 23700129, "Adapting to inversion of the visual field: a new twist on an old problem.": does not qualify. why adapting to inversion is slow (computational account with reaching experiments); motor measures, not how the scene looks.
18. Sekiyama et al., 2012-06-26, PMID 22742662, "Visuo-somatosensory reorganization in perceptual adaptation to reversed vision.": **taken**. long-term wearing (32 to 37 days) of left-right reversing spectacles, with left-right judgements tested over the wear and after removal; measures perceptual adaptation, which the test wording names. Most recent qualifying result for this prediction.
19. Deniz et al., 2011-09-25, PMID 21948084, "Acute "upside-down" visual inversion in a patient with multiple sclerosis.": does not qualify. a case report of upside-down vision from multiple sclerosis; no goggles or relearning.
20. Sadun et al., 2012-03-01, PMID 22410442, "Effect of EPI-743 on the clinical course of the mitochondrial disease Leber hereditary optic neuropathy.": does not qualify. a drug trial for an optic nerve disease; off topic: does not measure what the test wording names.
21. Werner, 2011-07-20, PMID 21764164, "Adaptation to mirror-reversed vision is based on directionally tuned modules.": does not qualify. mirror-reversed pointing; motor measures only.
22. Yang et al., 2012-01-01, PMID 23366702, "Training complexity is not decisive factor for improving adaptation to visual sensory conflict.": does not qualify. training for space motion sickness; motor measures only.
23. Anzai et al., 2010-07-30, PMID 20674618, "Effects of reversible pharmacological shutdown of cerebellar flocculus on the memory of long-term horizontal vestibulo-ocular reflex adaptation in monkeys.": does not qualify. eye-reflex adaptation in monkeys; off topic: does not measure what the test wording names.
24. Werner and Bock, 2010-03-20, PMID 20304517, "Mechanisms for visuomotor adaptation to left-right reversed vision.": does not qualify. left-right reversed pointing; motor measures only.
25. Ito et al., 2010-01-01, PMID 21180357, "Rapid learning by walking observers wearing a reversing or inverting prism.": does not qualify. first minutes of walking with reversing or inverting prisms; learning curve only, not how the scene looks.
26. Serrien, 2009-07-22, PMID 19631236, "Bimanual information processing and the impact of conflict during mirror drawing.": does not qualify. mirror drawing and brain activity; motor measures only.
27. Serrien and Spapé, 2009-11-01, PMID 19730838, "The role of hand dominance and sensorimotor congruence   in voluntary movement.": does not qualify. hand dominance and mirror drawing; motor and brain measures only.
28. Bernier et al., 2009-01-06, PMID 19126799, "Direct evidence for cortical suppression of somatosensory afferents during visuomotor adaptation.": does not qualify. suppression of touch signals during visuomotor adaptation; no report of how the scene looks.
29. Okuyucu et al., 2007-10-17, PMID 17942518, "Acute 'upside-down' visual inversion due to multiple sclerosis.": does not qualify. a case report of upside-down vision from multiple sclerosis; no goggles.
30. Richter et al., 2007-07-04, PMID 17609882, "The effects of inverting prisms on the horizontal-vertical illusion: a systematic effect of downward gaze.": does not qualify. inverting prisms and a line-length illusion; measures an illusion's size, not whether the world comes to look upright.
31. Fernandez-Ruiz et al., 2007-01-10, PMID 17215478, "Human parietal "reach region" primarily encodes intrinsic visual direction, not extrinsic movement direction, in a visual motor dissociation task.": does not qualify. parietal reach region with reversed vision; brain coding, not how the scene looks.
32. Tanaka et al., 2007-03-26, PMID 17383707, "Mirror symmetrical transfer of perceptual learning by prism adaptation.": does not qualify. transfer of perceptual learning after prism adaptation; tests a learning transfer, not whether the scene looks right.
33. Grigorova and Bock, 2006-01-18, PMID 16418852, "The role of eye movements in visuo-manual adaptation.": does not qualify. eye movements in adaptation to reversed vision; motor measures only.
34. Reschke et al., 2006-01-01, PMID 16422446, "Stroboscopic vision as a treatment for motion sickness: strobe lighting vs. shutter glasses.": does not qualify. stroboscopic vision for motion sickness; off topic: does not measure what the test wording names.
35. Harvey et al., 2005-12-01, PMID 15811221, "Evolutionary robotics: a new scientific tool for studying cognition.": does not qualify. evolutionary robotics; a review or survey, no new data.
36. Marotta et al., 2004-09-22, PMID 15385588, "Task-specific sensorimotor adaptation to reversing prisms.": does not qualify. reaching and grasping with a reversing prism; finds adaptation is task-specific but measures action, not how the scene looks.
37. Berndt et al., 2005-01-01, PMID 15312693, "Effects of rearranged vision on event-related lateralizations of the EEG during pointing.": does not qualify. brain signals during pointing with rearranged vision; no report of how the scene looks.
38. Miyauchi et al., 2004-01-01, PMID 15477033, "Adaptation to left-right reversed vision rapidly activates ipsilateral visual cortex in humans.": qualifies, not taken. wearing left-right reversing goggles for 35 to 39 days, with behavioural tests of the inner sense of nearby space alongside brain scans; qualifies, not taken (older than the taken study, and the cap allows one per prediction).
39. Kilgour et al., 2004-01-01, PMID 15037050, "Haptic face recognition and prosopagnosia.": does not qualify. face recognition by touch; off topic: does not measure what the test wording names.
40. Ichikawa et al., 2003-01-01, PMID 12696661, "Modification of depth and distance perception caused by long-term wearing of left-right reversing spectacles.": qualifies, not taken. wearing left-right reversing spectacles for 35 to 39 days, with reports of perceived depth order; qualifies, not taken (older than the taken study; cap).

Counts: 1 taken, 2 qualify but not taken, 37 do not qualify.

### `sm-active-control`: a camera-to-touch device works only when the user moves the camera

Hits: 23. Screened: 23 (ranks 1 to 23). Query run 2026-11-21 09:51 PST.

1. Hu et al., 2026-10-26, PMID 43005310, "Audio-motor and related audio-spatial interventions for spatial function in people with visual impairment: a systematic review.": does not qualify. systematic review; a review or survey, no new data.
2. Guyoton et al., 2025-05-26, PMID 40419471, "Cortical circuits for cross-modal generalization.": does not qualify. mice generalising task rules between touch and vision, with light-triggered stimulation of the brain; no comparison of controlling a device's camera against receiving the same input without control.
3. Devecioğlu, 2022-05-17, PMID 35581510, "Psychophysical Evaluation of Proprioceptive Feedback Through a Probe Sliding on the Forearm Skin of Healthy Humans.": does not qualify. feedback through a probe on the forearm; accuracy compared across feedback types, not self-controlled against passive.
4. Ahmad et al., 2020-07-01, PMID 33018856, "Audio-Visual Thumble (AVT): A low-vision rehabilitation device using multisensory feedbacks.": does not qualify. a description of a ring-shaped rehabilitation device; no active against passive comparison.
5. Nataletti et al., 2020-06-19, PMID 32656190, "Temporal Asynchrony but Not Total Energy Nor Duration Improves the Judgment of Numerosity in Electrotactile Stimulation.": does not qualify. counting electrical touch pulses; no device camera, no active against passive comparison.
6. Hanneton et al., 2019-01-01, PMID 32092705, "Ears on the Hand: Reaching Three-Dimensional Targets With an Audio-Motor Device.": does not qualify. reaching to sounds with a sound-feedback device linked to the hand or the head; both conditions are self-controlled, so no passive comparison.
7. Tivadar et al., 2019-03-14, PMID 30930756, "Mental Rotation of Digitally-Rendered Haptic Objects.": does not qualify. mental rotation of shapes felt through a touch device; no active against passive comparison of locating objects out in space.
8. Lassagne et al., 2017-09-22, PMID 28952949, "Performance Evaluation of Passive Haptic Feedback for Tactile HMI Design in CAVEs.": does not qualify. touch feedback for virtual control panels; off topic: does not measure what the test wording names.
9. Schumann and O'Regan, 2017-02-14, PMID 28195187, "Sensory augmentation: integration of an auditory compass signal into human perception of space.": does not qualify. a sound-based compass felt as part of turning the head; by the theory's own proponent (O'Regan); tests integration into felt self-rotation, not self-controlled against passive use of a camera device.
10. Kristjánsson et al., 2016-09-01, PMID 27567755, "Designing sensory-substitution devices: Principles, pitfalls and potential1.": does not qualify. design principles for substitution devices; a review or survey, no new data.
11. Kolarik et al., 2016-08-05, PMID 27494318, "Echoic Sensory Substitution Information in a Single Obstacle Circumvention Task.": does not qualify. walking around an obstacle with an echo-based device; movement measures, no passive comparison.
12. Dieterich and Brandt, 2015-01-07, PMID 25581203, "The bilateral central vestibular system: its pathways, functions, and disorders.": does not qualify. the balance organs and their pathways; a review or survey, no new data.
13. Stiles et al., 2015-06-17, PMID 26136719, "Length and orientation constancy learning in 2-dimensions with auditory sensory substitution: the importance of self-initiated movement.": does not qualify. learning size and orientation constancy with a sound-based device, where learning tracked the number of the users' own head tilts; no group received the same input without controlling it, so the result is a correlation and cannot count for or against the test as worded (nearest miss; see the note on this call).
14. Kolarik et al., 2013-12-27, PMID 24370580, "Sensory substitution information informs locomotor adjustments when walking through apertures.": does not qualify. walking through gaps with an echo-based device; movement measures, no passive comparison.
15. Hartcher-O'Brien and Auvray, 2014-01-01, PMID 25693304, "The process of distal attribution illuminated through studies of sensory substitution.": does not qualify. distal attribution in sensory substitution; a review or survey, no new data.
16. Rosati et al., 2012-10-10, PMID 23046683, "Effect of task-related continuous auditory feedback during learning of tracking motion exercises.": does not qualify. sound feedback in motor training; off topic: does not measure what the test wording names.
17. Siegle and Warren, 2010-01-01, PMID 20402243, "Distal attribution and distance perception in sensory substitution.": does not qualify. perceived distance with a finger-mounted light sensor driving vibration on the back; compares attention instructions, not self-controlled against passive input (it would fit the substitution prediction's wording, but it is not in that prediction's list).
18. Robineau et al., 2007-04-01, PMID 17405378, "Guiding the surgical gesture using an electro-tactile stimulus array on the tongue: a feasibility study.": does not qualify. guiding a surgical gesture with a tongue display; off topic: does not measure what the test wording names.
19. Auvray et al., 2007-01-01, PMID 18283925, "The perception of space and form recognition in a simulated environment: the case of minimalist sensory-substitution devices.": does not qualify. learning new movement-to-stimulation laws in a minimal substitution interface; co-authored by O'Regan; varies the link between action and stimulation but the abstract names no passive group receiving the same stimulation.
20. Auvray et al., 2005-12-01, PMID 16385644, "There is something out there: distal attribution in sensory substitution, twenty years later.": qualifies, not taken. head-mounted camera turned into sound, with and without a link between the wearer's movements and the stimulation, and ratings of whether sensations were attributed to an object out in space; co-authored by O'Regan. Qualifies, not taken: it is the most recent qualifying result for this prediction, but it ranks sixth by date among the predictions' best candidates, and only five are taken.
21. Segond et al., 2005-01-01, PMID 16309117, "Human spatial navigation via a visuo-tactile sensory substitution system.": does not qualify. navigating a maze by remotely steering a robot carrying the camera; all users steer it, so no passive comparison.
22. Rauschecker, 1995-01-01, PMID 7535489, "Compensatory plasticity and sensory substitution in the cerebral cortex.": does not qualify. brain plasticity and sensory substitution; a review or survey, no new data.
23. Easton, 1992-01-01, PMID 1741108, "Inherent problems of attempts to apply sonar and vibrotactile sensory aid technology to the perceptual needs of the blind.": does not qualify. problems with sonar and vibration aids for the blind; a review or survey, no new data.

Counts: 0 taken, 1 qualify but not taken, 22 do not qualify.

### `sm-substitution`: with practice, a substitution device gives experience of objects out in space, not of touch or sound

Hits: 140. Screened: 40 (ranks 1 to 40). Query run 2026-11-21 09:52 PST.

1. Cirdan et al., 2026-10-31, PMID 42965879, "Platformed Atmospheres: How Digital Platforms Reshape the Felt Experience of Family Life.": does not qualify. digital platforms and family life; off topic: does not measure what the test wording names.
2. Spence and Di Stefano, 2026-09-01, PMID 43047830, "Aligning sensations: Do trumpets sound scarlet?": does not qualify. an opinion piece on matching colours and sounds; a theory, opinion or commentary piece, no new data.
3. Gözaçık Karakoç, 2026-09-02, PMID 42684556, "Prior minimally invasive experience and the robotic mitral valve learning curve: a focused narrative review and the tactile-visual decoupling hypothesis.": does not qualify. robotic surgery learning curves; a review or survey, no new data.
4. Chebat et al., 2026-09-01, PMID 42549635, "Hippocampal Subfield Volumetry and Navigation in Congenital Blindness.": does not qualify. hippocampus size and navigation with a touch device in congenital blindness; measures brain volume and obstacle performance, not whether objects are experienced out in space.
5. Akar et al., 2026-08-18, PMID 42613492, "Sensory substitution under passive guidance: Effects on proprioceptive acuity and motor performance.": does not qualify. shape recognition under passive guidance through a device; measures recognition and position sense, not whether the stimulation is experienced as out in space or as touch.
6. Gwiaździński et al., 2026-07-27, PMID 42507482, "Usability of sensory substitution systems: test and comparison of the BrainPort and colorophone devices.": does not qualify. usability of two devices (BrainPort, Colorophone); measures usability and task completion, not the kind of experience.
7. Moon et al., 2026-08-26, PMID 42718785, "Early acquisition efficiency in visual-to-auditory sensory substitution: the role of structured learning.": does not qualify. speed of learning a sound-coded image scheme; recognition only.
8. Cesari et al., 2026-01-01, PMID 41588926, "Sensory Substitution and Embodiment Shape Performance and Immersion in Teleoperated Settings.": does not qualify. force shown visually in remote manipulation; presence and performance, not where objects are experienced.
9. Martín Muñoz et al., 2026-01-07, PMID 41501868, "Artificial vibrotactile feedback elicits neural correlates of sense of agency.": does not qualify. sense of agency with vibration feedback; off topic: does not measure what the test wording names.
10. Ortiz-Teran et al., 2025-12-15, PMID 41407217, "Long-term visual-to-tactile stimulation induces functional reorganization of thalamic pathways to achieve visual perception.": does not qualify. long-term passive touch stimulation and thalamic connectivity in blind children; brain connectivity and identification scores, not reports of the experience.
11. Karimi et al., 2025-09-18, PMID 41007234, "Haptic Feedback Systems for Lower-Limb Prosthetic Applications: A Review of System Design, User Experience, and Clinical Insights.": does not qualify. touch feedback for leg prostheses; a review or survey, no new data.
12. Mielke et al., 2025-04-25, PMID 40085451, "SensARy Substitution: Augmented Reality Techniques to Enhance Force Perception in Touchless Robot Control.": does not qualify. augmented reality cues for force in robot control; off topic: does not measure what the test wording names.
13. Micera and Shokur, 2024-07-12, PMID 38994666, "Our research path toward the restoration of natural sensations in hand prostheses.": does not qualify. restoring touch in hand prostheses; a review or survey, no new data.
14. Kim et al., 2024-05-24, PMID 38797383, "Visual Mental Imagery and Neural Dynamics of Sensory Substitution in the Blindfolded Subjects.": does not qualify. whether a sound-coded letter is perceived as visual-like, judged by fitting brain models (dynamic causal modelling); the measure is a brain model, not users' reports or reactions, which is what the test wording names (borderline; see the note).
15. Jin et al., 2024-06-01, PMID 38990235, "Functional performance of a vibrotactile sensory substitution device in people with profound vision loss.": does not qualify. a vibration device for people with profound vision loss; performance with exit interviews on usability, not reports of objects out in space.
16. Goral et al., 2024-06-27, PMID 38937475, "Enhancing interoceptive sensibility through exteroceptive-interoceptive sensory substitution.": does not qualify. breathing signals shown as sights and sounds; off topic: does not measure what the test wording names.
17. Blau et al., 2024-06-12, PMID 38865475, "Conductive block copolymer elastomers and psychophysical thresholding for accurate haptic effects.": does not qualify. materials for touch displays; off topic: does not measure what the test wording names.
18. Li and Shi, 2024-03-01, PMID 38433698, "[Research advances in the mechanism of vestibular compensation and treatment].": does not qualify. vestibular compensation; a review or survey, no new data.
19. Jiang et al., 2024-03-26, PMID 38530828, "Towards sensory substitution and augmentation: Mapping visual distance to audio and tactile frequency.": does not qualify. matching distance to sound and vibration frequency; no practice with a device, no report of the experience.
20. Cesari et al., 2023-11-01, PMID 38027699, "Sensory substitution increases robotic surgical performance and sets the ground for a mediating role of the sense of embodiment: a systematic review.": does not qualify. sensory substitution in robotic surgery; a review or survey, no new data.
21. Arbel et al., 2023-09-21, PMID 37741551, "Rapid plasticity in the ventral visual stream elicited by a newly learnt auditory script in congenitally blind adults.": does not qualify. ventral visual stream activity when blind adults learn a sound-based script; brain activity, not reports of the experience.
22. de Paz and Travieso, 2023-07-04, PMID 37402032, "A direct comparison of sound and vibration as sources of stimulation for a sensory substitution glove.": does not qualify. sound against vibration for a substitution glove; grasping performance only.
23. Aggius-Vella et al., 2023-03-01, PMID 36863342, "Activation of human visual area V6 during egocentric navigation with and without visual experience.": does not qualify. visual area V6 during navigation with a sound device; brain activity, not reports.
24. Plaza et al., 2023-11-22, PMID 37992062, "Sound-encoded faces activate the left fusiform face area in the early blind.": does not qualify. face area activity for sound-coded faces in early blind people; brain activity, not reports.
25. Pamir et al., 2020-09-30, PMID 32997554, "Preparing participants for the use of the tongue visual sensory substitution device.": does not qualify. training blind adults to use a tongue display (BrainPort); training progress and strategies, not whether objects are experienced out in space.
26. Maimon et al., 2022-06-22, PMID 35752268, "A case study in phenomenology of visual experience with retinal prosthesis versus visual-to-auditory sensory substitution.": **taken**. a late-blinded man's first-hand reports after about nine months' training with a camera-to-sound device (EyeMusic), compared with a retinal implant; reports of whether the experience is visual, which the test wording's 'against' case names. Most recent qualifying result for this prediction.
27. Arbel et al., 2022-03-14, PMID 35288597, "Congenitally blind adults can learn to identify face-shapes via auditory sensory substitution and successfully generalize some of the learned features.": does not qualify. congenitally blind adults learning face shapes through sound; recognition only.
28. Kilian et al., 2022-02-26, PMID 35271009, "The Unfolding Space Glove: A Wearable Spatio-Visual to Haptic Sensory Substitution Device for Blind People.": does not qualify. design and evaluation of a vibration glove; performance and usability.
29. Cieśla et al., 2022-02-25, PMID 35217676, "Effects of training and using an audio-tactile sensory substitution device on speech-in-noise understanding.": does not qualify. speech in noise with fingertip vibration; off topic: does not measure what the test wording names.
30. Maimon et al., 2023-01-26, PMID 36776219, "The Topo-Speech sensory substitution system as a method of conveying spatial information to the blind and vision impaired.": does not qualify. a speech-based spatial substitution system; performance only.
31. Eagleman and Perrotta, 2023-01-13, PMID 36712151, "The future of sensory substitution, addition, and expansion via haptic devices.": does not qualify. future of haptic devices; a review or survey, no new data.
32. Arbel et al., 2022-10-03, PMID 36263367, "Face shape processing via visual-to-auditory sensory substitution activates regions within the face processing networks in the absence of visual experience.": does not qualify. face-area activity for sound-coded faces; brain activity, not reports.
33. Hamilton-Fletcher and Chan, 2021-11-01, PMID 34892454, "Auditory Scene Analysis Principles Improve Image Reconstruction Abilities of Novice Vision-to-Audio Sensory Substitution Users.": does not qualify. image reconstruction by novice users of a sound device; recognition only.
34. Remache-Vinueza et al., 2021-09-30, PMID 34640895, "Audio-Tactile Rendering: A Review on Technology and Methods to Convey Musical Information through the Sense of Touch.": does not qualify. conveying music through touch; a review or survey, no new data.
35. Lynch and Monaghan, 2021-09-17, PMID 34604558, "Effects of sensory substituted functional training on balance, gait, and functional performance in neurological patient populations: A systematic review and meta-analysis.": does not qualify. balance training with substitution; a review or survey, no new data.
36. Pesnot Lerousseau et al., 2021-07-20, PMID 34285265, "Training-induced plasticity enables visualizing sounds with a visual-to-auditory conversion device.": qualifies, not taken. a crossmodal interference test before and after training with a picture-to-sound device, with the users' phenomenology measured; bears on whether the experience becomes visual. Qualifies, not taken (older than the taken study; cap).
37. Hofstetter et al., 2021-04-06, PMID 33836269, "Topographic maps and neural tuning for sensory substitution dimensions learned in adulthood in a congenital blind subject.": does not qualify. a single blind user's brain maps for a learned sound space; brain activity, not reports.
38. Bahrami Moqadam et al., 2021-11-29, PMID 34868280, "Conceptual Method of Temperature Sensation in Bionic Hand by Extraordinary Perceptual Phenomenon.": does not qualify. a temperature sensation method for a bionic hand; off topic: does not measure what the test wording names.
39. Ptito et al., 2021-02-09, PMID 33633557, "Brain-Machine Interfaces to Assist the Blind.": does not qualify. brain-machine interfaces for the blind; a review or survey, no new data.
40. Zilbershtain-Kra et al., 2020-12-11, PMID 33392481, "Active sensory substitution allows fast learning via effective motor-sensory strategies.": does not qualify. fast learning with an active-sensing substitution device; accuracy and speed only, not the kind of experience.

Counts: 1 taken, 1 qualify but not taken, 38 do not qualify.

### `sm-change-blindness`: change blindness (large changes missed when the moment of change is hidden)

Hits: 329. Screened: 40 (ranks 1 to 40). Query run 2026-11-21 09:53 PST.

1. Thomas and Didierjean, 2026-11-13, PMID 43025128, "You process it, yet miss the change: a magic-based demonstration of a novel form of change blindness.": **taken**. people miss a large change (water vanishing from upturned cups in a magic trick) across an interruption, and most report no surprise; measures failure to notice a large change whose moment of change is hidden. Most recent qualifying result for this prediction and for the theory.
2. Qi et al., 2026-10-21, PMID 42902897, "Task load and phase relevance modulate primary flight display change blindness: evidence from flight simulator, eye-tracking, and fNIRS.": qualifies, not taken. pilots' detection of changes on a flight display under load, with eye tracking; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
3. Frey and Whitney, 2026-08-03, PMID 42972330, "Slow change blindness from serial dependence: slowly changing objects are perceived as biased toward the past.": does not qualify. slow change blindness: the change is gradual, with no flash, cut or blink hiding it, so the local signal is absent rather than masked as the test wording requires (borderline).
4. Herbranson, 2026-06-01, PMID 42272387, "Selective attention as a contributor to negative frequency dependent selection in predator-prey interactions.": does not qualify. selective attention in predators; a theory, opinion or commentary piece, no new data.
5. Norman et al., 2026-06-08, PMID 42258119, "Subdomains of executive function correlate with accuracy on a change detection task.": qualifies, not taken. a flicker change-detection task in 260 people with a cognitive battery; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
6. Berger and Hochhauser, 2026-05-18, PMID 42144622, "The role of stimulus characteristics in visual attention: an eye-tracking study.": qualifies, not taken. change detection in real-world scene pairs with eye tracking; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
7. Kawachi and Kawachi, 2026-08-03, PMID 42609239, "Dyadic interaction enhances sensitivity and shifts decision criterion in a change detection task.": qualifies, not taken. flicker change detection by pairs against individuals; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
8. Oliva et al., 2026-04-02, PMID 41926447, "Where extended reality and AI may take us: Ethical issues of impersonation and AI fakes in social virtual reality.": does not qualify. a panel in social virtual reality in which two panellists swapped avatars; about 40 of 100 who answered did not notice. A change of identity during a live event, not a large change whose local signal is masked (borderline).
9. Hwang et al., 2025-09-24, PMID 41338770, "Development and validation of implicit behavioral tests assessing perceptual sensitivity to construction hazards.": does not qualify. validation of hazard-sensitivity tests for construction workers; the change task is a tool for measuring hazard sensitivity.
10. Grosprêtre et al., 2025-12-01, PMID 41261364, "Effect of Two Types of Open-Skill Training on Cognitive Functions: The Case of Parkour.": does not qualify. parkour against team sports and cognitive tests; the abstract names no change-detection measure.
11. Hertzmann, 2025-11-26, PMID 41292451, "Lossy processing principles in 2D and 3D vision.": does not qualify. a commentary on lossy vision; a theory, opinion or commentary piece, no new data.
12. Miller et al., 2025-11-24, PMID 41289916, "A cross-cultural comparison of change detection in driving and non-driving scenes.": qualifies, not taken. change blindness in driving scenes across cultures; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
13. Jurkat et al., 2024-05-09, PMID 38722583, "The socialization of visual attention: Training effects of verbal attention guidance in urban German children.": does not qualify. verbal attention training in children; the abstract names no masked change measure.
14. Horde et al., 2025-10-01, PMID 40779372, "A Survey on Tactile Change Blindness.": does not qualify. tactile change blindness; a review or survey, no new data.
15. Becker et al., 2025-05-06, PMID 40334441, "Change blindness, subset segmentation, and the perceptual underestimation of subset numerosity.": does not qualify. colour-change detection used to study the counting of dot subsets; the change is not a large change in a scene.
16. Sugiyama and Mori, 2025-05-14, PMID 40369392, "Sex differences in the relationship between autistic traits and face-change discrimination sensitivity in the general population: a psychophysical investigation.": does not qualify. face-change discrimination and autistic traits; a fine discrimination threshold, not large masked changes.
17. Martin et al., 2025-05-02, PMID 40316646, "Viewers perceive shape in pictures according to per-fixation perspective.": does not qualify. perceived shape in pictures by fixation; off topic: does not measure what the test wording names.
18. Zhu et al., 2025-04-25, PMID 40063472, "Evaluating 3D Visual Comparison Techniques for Change Detection in Virtual Reality.": does not qualify. comparison techniques for change detection in virtual reality; a display design study.
19. Chen et al., 2025-02-21, PMID 39986207, "Individual differences in prioritization for consciousness and the conscious detection of changes.": qualifies, not taken. individual differences in noticing changes in a change blindness paradigm; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
20. Lee et al., 2024-09-01, PMID 39418450, "Learning traps and change blindness in dynamic environments.": does not qualify. learning traps: not noticing a change in a decision rule; not a visual scene change.
21. Frey et al., 2024-09-01, PMID 39254964, "Memory representations during slow change blindness.": does not qualify. memory during slow change blindness; gradual change, not masked (borderline, as rank 3).
22. Ünal et al., 2024-07-02, PMID 38959638, "Asymmetries in encoding event roles: Evidence from language and cognition.": does not qualify. event roles in language and cognition; off topic: does not measure what the test wording names.
23. Cohen et al., 2024-07-01, PMID 38527082, "Familiarity Alters the Bandwidth of Perceptual Awareness.": qualifies, not taken. noticing peripheral alterations in familiar against unfamiliar scenes; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
24. Saeed et al., 2024-01-25, PMID 38271026, "Looks can be deceiving: Investigating change blindness in an online setting.": qualifies, not taken. change blindness online; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
25. Fudali-Czyż et al., 2022-05-14, PMID 35574598, "An Attentive Blank Stare Under Simulator-induced Spatial Disorientation Events.": does not qualify. pilots' visual change detection during spatial disorientation; the abstract centres on a 'blank stare' under disorientation, a dual-task design (borderline).
26. Wright et al., 2024-11-26, PMID 42339458, "Detecting multiple simultaneous and sequential feature changes.": qualifies, not taken. flicker task with several simultaneous and sequential changes; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
27. Favieri et al., 2024-11-22, PMID 39649660, "Effects of bottom-up and top-down attentional processes on change blindness for COVID-related stimuli: influence of heart rate variability.": qualifies, not taken. flicker task with emotional and COVID-related pictures; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
28. Frey et al., 2024-02-09, PMID 38348333, "A novel, semi-automatic procedure for generating slow change blindness stimuli.": does not qualify. a procedure for making slow change blindness stimuli; a methods paper on gradual change.
29. Kallinen and Ojanen, 2023-12-01, PMID 37331012, "Cognitive Performance changes during a 20-day Winter Military Training Course and the Following 10-day Recovery Period.": does not qualify. cognition during military winter training; the abstract names no change measure.
30. Senel et al., 2023-09-15, PMID 37876610, "Imperceptible body transformation in virtual reality: Saliency of self representation.": qualifies, not taken. virtual reality: 73% and 85% did not notice changes to their own and an instructor's virtual face; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
31. Barzy et al., 2023-03-26, PMID 36847458, "Are social interactions preferentially attended in real-world scenes? Evidence from change blindness.": qualifies, not taken. change detection for social interactions in real-world scenes; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
32. Kondyli et al., 2023-08-09, PMID 37556047, "How do drivers mitigate the effects of naturalistic visual complexity? : On attentional strategies and their implications under a change blindness protocol.": qualifies, not taken. change detection in naturalistic driving scenes; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
33. Lee et al., 2023-06-29, PMID 37384518, "When searching helps you see: Bridging the gap between incidental and intentional change detection.": qualifies, not taken. incidental and intentional detection of changes across video cuts; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
34. Kalkstein et al., 2022-11-17, PMID 36395038, "Social norms govern what behaviors come to mind-And what do not.": does not qualify. social norms and what behaviours come to mind; off topic: does not measure what the test wording names.
35. Martin et al., 2023-05-01, PMID 37027712, "A Study of Change Blindness in Immersive Environments.": qualifies, not taken. change blindness in immersive virtual reality; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
36. Grosprêtre et al., 2023-04-01, PMID 37029516, "How Exergaming with Virtual Reality Enhances Specific Cognitive and Visuo-Motor Abilities: An Explorative Study.": does not qualify. virtual reality exergaming and cognitive tests; change blindness is one test in a training study, not reported as such in the abstract.
37. Sawant et al., 2022-09-19, PMID 36123120, "A Midbrain Inspired Recurrent Neural Network Model for Robust Change Detection.": does not qualify. a neural network model of change detection; a model with no new data from people.
38. Witzel and Dewis, 2022-07-14, PMID 35843086, "Why bananas look yellow: The dominant hue of object colours.": does not qualify. object colours; off topic: does not measure what the test wording names.
39. Barnas and Ward, 2022-07-02, PMID 35792349, "Metacognitive judgements of change detection predict change blindness.": qualifies, not taken. metacognitive judgements and alternating-scene change blindness; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
40. Hermens and Zdravković, 2022-08-15, PMID 35971314, "Visual attention in change blindness for objects and shadows.": qualifies, not taken. change detection for objects and shadows with eye tracking; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.

Counts: 1 taken, 17 qualify but not taken, 22 do not qualify.

### `sm-inattentional`: missing an unexpected object while busy with a task

Hits: 324. Screened: 40 (ranks 1 to 40). Query run 2026-11-21 09:53 PST.

1. Hense et al., 2026-10-15, PMID 42920898, "Distinct electrophysiological correlates of low- and high-level visual consciousness with minimized post-perceptual processing.": **taken**. an inattentional blindness design: uninformed people doing a demanding task at fixation, with lines forming a face appearing repeatedly in the background; awareness assessed afterwards. Most recent qualifying result for this prediction.
2. Simons and Ding, 2026-08-20, PMID 42622799, "The effects of cognitive and perceptual load on inattentional blindness.": qualifies, not taken. five inattentional blindness studies varying perceptual and cognitive load, about 100 per condition; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
3. Chau et al., 2026-10-03, PMID 42828852, "Stopping too soon: Search termination and subsequent search misses in diagnostic radiography.": does not qualify. search termination in radiography; a review or survey, no new data.
4. Cohen, 2026-09-01, PMID 42744753, "Conscious Awareness Across the Visual Field.": does not qualify. conscious awareness across the visual field; a review or survey, no new data.
5. Yeung et al., 2026-08-04, PMID 43058132, "A Comprehensive Full Body Kinematics Dataset with and without Head-Mounted AR/VR Display.": does not qualify. a body movement data set with and without headsets; no unexpected-object test reported.
6. Salehi et al., 2026-05-05, PMID 42086575, "Modeling attention and binding in the brain through bidirectional recurrent gating.": does not qualify. a computer model of attention and binding; no new data from people.
7. Liu et al., 2026-05-01, PMID 42060400, "A late-stage neural signature of visual awareness in the no-report inattentional blindness paradigm.": qualifies, not taken. a no-report inattentional blindness design across three EEG experiments; qualifies for this prediction too, but taken for the no-single-brain-state prediction (sm-no-ncc) under the cap, see 'The choice'. Judged for both if opened.
8. Nguyen et al., 2026-03-23, PMID 41872686, "Assessing the role of magician patter on deception in the Three-Card Monte.": qualifies, not taken. how many viewers notice a visible mark on a card during the Three-Card Monte; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
9. Zhang et al., 2025-07-09, PMID 40629927, "The role of executive functions in young children's static and sustained inattentional blindness.": qualifies, not taken. static and sustained inattentional blindness in 154 children; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
10. Qiu et al., 2025-12-26, PMID 41455171, "The effects of concurrent perceptual load and physical exertion on inattentional blindness in children.": qualifies, not taken. perceptual load, physical exertion and inattentional blindness in children; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
11. Cullen et al., 2025-05-18, PMID 42211421, "Can expert testimony and demonstrations influence juror perceptions of witness inattentional blindness?": does not qualify. jurors' views of witnesses' inattentional blindness; measures jurors' opinions, not noticing.
12. Peters et al., 2026-04-15, PMID 41993059, "Stimulus duration modulates awareness-dependent brain activation in the fusiform gyrus independently of task-relevance.": qualifies, not taken. an inattentional blindness fMRI design (Straube group) in which uninformed people stay unaware of a face; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
13. Martinez et al., 2025-05-26, PMID 40415512, "Inattentional Blindness: Failure to Notice Something Unexpected in Plain Sight Among Surgical and Medical Trainees.": qualifies, not taken. prevalence of inattentional blindness among surgical and medical trainees; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
14. Gutiérrez-García et al., 2025-05-16, PMID 40377478, "Misperception of non-Happy Facial Features: Overshadowing and Priming by a Smiling Mouth.": does not qualify. facial expression judgements; off topic: does not measure what the test wording names.
15. Soffar et al., 2025-12-16, PMID 41416020, "Virtual Reality Simulation for Orthopedic Surgical Training: A Narrative Review of Current Evidence and Educational Impact.": does not qualify. virtual reality in orthopaedic training; a review or survey, no new data.
16. Nakhapaksirat et al., 2025-06-21, PMID 40542678, "Identification and evaluation of radiographic interpretation errors among undergraduate dental students.": does not qualify. radiographic interpretation errors among dental students; error types, not an unexpected-object test.
17. Most, 2025-11-26, PMID 41292469, "Seeing attention in inattentional blindness.": does not qualify. a commentary on attention; a theory, opinion or commentary piece, no new data.
18. Migliorini et al., 2025-04-23, PMID 40273546, "Optimizing multimodal alarms to mitigate inattentional blindness in air traffic control.": qualifies, not taken. alarms to reduce inattentional blindness in air traffic control; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
19. Finger et al., 2025-09-24, PMID 40932017, "Spatial priors affect sensory weighting in navigation and landing in Egyptian fruit bats.": does not qualify. bats' navigation and spatial priors; off topic: does not measure what the test wording names.
20. Strayer and McDonnell, 2025-04-11, PMID 40216457, "SPIDER 2.0: Driver Distraction and Visual Attention.": does not qualify. driver distraction; a review or survey, no new data.
21. Cho et al., 2025-08-15, PMID 40815451, "Effect of multi-refresh-rate method on user experience: sustained attention and inattentional blindness.": does not qualify. noticing reduced refresh rates in peripheral view; a reduction in display quality, not an unexpected object (borderline).
22. Cleary et al., 2025-01-07, PMID 39775501, "Does familiarity-detection flip attention inward? The familiarity-flip-of-attention account of the primacy effect in memory for repetitions.": does not qualify. a memory account of attention flips; a theory, opinion or commentary piece, no new data.
23. Gandolfo and Peelen, 2025-03-10, PMID 40068579, "A body detection inversion effect revealed by a large-scale inattentional blindness experiment.": qualifies, not taken. a large single-trial inattentional blindness experiment (13,539 people) with an unexpected silhouette next to fixation; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
24. Özkartal et al., 2025-04-09, PMID 40409847, "A Transvenous Pacing Lead's Journey Leading to Perforation and Hematothorax.": does not qualify. a pacing lead case report; off topic: does not measure what the test wording names.
25. Nartker et al., 2025-05-19, PMID 40388213, "Sensitivity to visual features in inattentional blindness.": qualifies, not taken. sensitivity to features of stimuli people say they did not notice; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
26. Asken et al., 2025-04-01, PMID 40153860, "Inattentional Blindness as an Underappreciated Emphasis in Patient Safety Education: Need for Greater Recognition in Medical and Surgical Training.": does not qualify. inattentional blindness in patient safety education; a theory, opinion or commentary piece, no new data.
27. Cooper and Strayer, 2024-08-23, PMID 39178389, "Multitasking Induced Contextual Blindness.": does not qualify. multitasking and learning of context cues; not an unexpected-object test.
28. Wang, 2025-10-16, PMID 41181668, "The dual system model of distraction: explaining the cognitive mechanism of distraction.": does not qualify. a conceptual model of distraction; a theory, opinion or commentary piece, no new data.
29. Bandara et al., 2025-09-23, PMID 40995066, "Computational modelling shows evidence in support of both sensory and frontal theories of consciousness.": does not qualify. computer modelling of an existing inattentional blindness EEG data set (already in the records as bandara-2025); a reanalysis of awareness-related brain activity, not a measure of noticing.
30. Morris, 2025-04-22, PMID 40469940, "Invisible Gorillas in the Mind: Internal Inattentional Blindness and the Prospect of Introspection Training.": does not qualify. 'internal' inattentional blindness and introspection; a theory, opinion or commentary piece, no new data.
31. Zhang et al., 2024-11-20, PMID 39563598, "Re-examining our evolutionary propensities toward snakes: Insights from children's inattentional blindness.": qualifies, not taken. children's detection of an unexpected snake or lizard, with eye tracking; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
32. Chong and Beck, 2024-10-23, PMID 39447236, "Real-world Statistical Regularity Impacts Inattentional Blindness.": qualifies, not taken. noticing rates for probable and improbable unexpected scenes; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
33. Hutchinson et al., 2024-08-23, PMID 39182710, "No electrophysiological evidence for semantic processing during inattentional blindness.": qualifies, not taken. a three-phase inattentional blindness EEG design; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
34. Mizubuti et al., 2024-06-25, PMID 38918271, "Identifying intraoperative events in a simulated laparotomy video: a multinational study of inattentional blindness among anesthesiologists.": qualifies, not taken. anaesthesiologists noticing unexpected events in a surgical video; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
35. Chu and Aimola Davies, 2024-07-13, PMID 39002298, "When the WRENCH turns a few heads: Expectation and semantic relatedness in inattentional blindness.": qualifies, not taken. noticing an unexpected word at fixation; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
36. Simons et al., 2024-01-05, PMID 38182856, "Individual differences in inattentional blindness.": does not qualify. individual differences in inattentional blindness; a meta-analysis and review.
37. Cohen et al., 2024-07-01, PMID 38527082, "Familiarity Alters the Bandwidth of Perceptual Awareness.": does not qualify. noticing peripheral alterations in familiar scenes; alterations to a scene, not an unexpected object during a demanding task (also in the change blindness list, where it qualifies).
38. Mitani et al., 2024-01-08, PMID 38186286, "Effectiveness of novel oral hygiene instruction avoiding inattentional blindness using an application for unique plaque control record calculation: A randomized clinical trial.": does not qualify. an oral hygiene trial; off topic: does not measure what the test wording names.
39. Canton et al., 2024-04-12, PMID 38607522, "Feasibility and Usability of Augmented Reality Technology in the Orthopaedic Operating Room.": does not qualify. augmented reality in the operating room; a review or survey, no new data.
40. Eddine et al., 2024-04-10, PMID 38598036, "On investigating drivers' attention allocation during partially-automated driving.": does not qualify. drivers' attention during partly automated driving; gaze allocation, not noticing of an unexpected object.

Counts: 1 taken, 15 qualify but not taken, 24 do not qualify.

### `sm-no-ncc`: no single brain state goes with a given visual experience in every situation

Hits: 7. Screened: 7 (ranks 1 to 7). Query run 2026-11-21 09:53 PST.

1. Liu et al., 2026-05-01, PMID 42060400, "A late-stage neural signature of visual awareness in the no-report inattentional blindness paradigm.": **taken**. searches for the brain activity that goes with seeing an object when the object is irrelevant to the task and not reported (a no-report design), asking whether a late brain response tracks awareness or report; measures the brain activity accompanying an experience across report conditions, which the test wording names. Most recent qualifying result for this prediction.
2. Wagener and Nieder, 2024-03-01, PMID 38165732, "Conscious Experience of Stimulus Presence and Absence Is Actively Encoded by Neurons in the Crow Brain.": qualifies, not taken. crow neurons coding 'seen' and 'not seen', with the motor response separated from the percept by the task design; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
3. Hesse and Tsao, 2020-11-11, PMID 33174836, "A new no-report paradigm reveals that face cells encode both consciously perceived and suppressed stimuli.": qualifies, not taken. monkey face cells tracking the seen image without any report; the cap allows one study per prediction, and a more recent qualifying study already holds this prediction's place.
4. Colás et al., 2019-03-07, PMID 30853537, "Conscious perception in patients with prefrontal damage.": does not qualify. near-threshold seeing in patients with prefrontal damage; one task, so it does not test whether brain activity tracks an experience across tasks or reports.
5. Schlicht, 2018-11-15, PMID 30447435, "A methodological dilemma for investigating consciousness empirically.": does not qualify. a methodological argument about searching for brain correlates; a theory, opinion or commentary piece, no new data.
6. Lau and Passingham, 2006-11-21, PMID 17124173, "Relative blindsight in normal observers and the neural correlate of visual consciousness.": does not qualify. prefrontal activity with matched performance under masking; one task and one report condition, so it does not test whether the activity changes across tasks or reports.
7. Sewards and Sewards, 2001-12-01, PMID 11790038, "On the correlation between synchronized oscillatory activities and consciousness.": does not qualify. an argument about brain oscillations and consciousness; a theory, opinion or commentary piece, no new data.

Counts: 1 taken, 2 qualify but not taken, 4 do not qualify.
