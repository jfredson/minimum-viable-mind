# Attention schema theory: per-prediction search screen (2026-11-21)

First reading, one reader (Claude). Draft files only; nothing in the repository was changed.
Method as fixed in `data/tracker/searches-2026-11-21.toml` before any search ran: screen each
prediction's results in order, up to 40, by title and abstract only; a result qualifies if it
reports new data and measures what the prediction's own test wording names; then take the five
most recent qualifying studies across the theory's seven predictions, by earliest public
appearance, at most one per prediction.

## What came out

| Prediction (plain) | Hits | Screened | Qualified | Taken |
|---|---|---|---|---|
| Awareness comes in degrees, as attention does (`ast-graded`) | 122 | 40 | 2 | Kumar and Srinivasan 2026 (`kumar-2026`), opened |
| Awareness and attention usually go together (`ast-covary`) | 14 | 14 | 11 | Lo 2018 (`lo-2018`), NOT opened |
| A system with a model of its attention will claim inner awareness (`ast-claims`) | 4 | 4 | 0 | none |
| Without awareness, control of attention suffers (`ast-control`) | 77 | 40 | 8 | Wang and colleagues 2022 (`wang-2022`), opened |
| A model of attention improves control of attention (`ast-schema-control`) | 231 | 40 | 0 | none |
| The right temporoparietal junction builds the model (`ast-tpj`) | 29 | 29 | 3 | Wilterson and colleagues 2021, brain scanning (`wilterson-2021-tpj`), already in the records |
| Awareness reaches as far as attention does (`ast-domain`) | 37 | 37 | 1 | Bong and colleagues 2025 (`bong-2025`), NOT opened |

24 different studies qualified (25 qualifying lines; one study, `wilterson-2021-tpj`, qualified
for two predictions). Five places were filled, because two predictions had no qualifying study.

## The choice, and how the one-per-prediction cap was applied

Every qualifying study across the seven lists, newest first by earliest public appearance:
`kumar-2026` (2026-08-24, graded), `bong-2025` (2025-11-22, domain), `wang-2022` (2022-11-17,
control), Karabay and colleagues (2021-11-22, graded: skipped, graded already filled),
`wilterson-2021-tpj` (2021-06-14, qualifies for control and junction), Güldener and colleagues
(2021-01-29, control: skipped), and so on down to `lo-2018` (2017-12-26, covary), the newest
study on a list whose place was still open.

The one study that qualified for two predictions is the Graziano lab's brain-scanning study
(`wilterson-2021-tpj`). When its turn came, the control place had already gone to the newer
`wang-2022`, so it took the junction place. Following the method ("taken once and judged for
both") it is judged for both, and both of its commitment judgements already exist and are
settled "unclear" by the own-lab dating ruling, so nothing new is written for it. Under any
other reading of the cap (for example, that a study qualifying for two predictions uses up both
places) the five would be the same, because the control place was already filled by a newer study.

The search for the junction prediction found the lab's study again although it was already in
the records from the earlier name search; it is reused by its id, as the method says.

## Judgements written (4)

| Judgement | Verdict | Unsure |
|---|---|---|
| Kumar 2026 on the graded prediction, dates (`com-kumar-2026-ast-graded`) | before | yes |
| Kumar 2026 on the graded prediction, result (`out-kumar-2026-ast-graded`) | for | yes |
| Wang 2022 on the control prediction, dates (`com-wang-2022-ast-control`) | before | yes |
| Wang 2022 on the control prediction, result (`out-wang-2022-ast-control`) | mixed | yes |

Every one is marked unsure. Why, in short:

- **Kumar, dates and commitment:** the 2015 statement says awareness "should also be graded"
  because attention is, and names the rating scale used; it does not say that less attention
  makes ratings more in-between, the specific pattern measured. A stricter reader would say
  "unclear".
- **Kumar, result ("for"):** attention was varied in two steps only; in the second experiment
  the average rating did not move with attention (only the spread did); and the authors write
  that smooth rating curves do not settle graded against all-or-none. Could be read "mixed".
- **Wang, dates and commitment:** what the 2015 paper means by control is correcting attention
  after something has drawn it (withdrawing it, taking it into account). Wang measures whether
  a goal set in advance decides which unseen cues draw attention at all. Whether the theory was
  committed to that is a judgement; could be read "unclear".
- **Wang, result ("mixed"):** unseen cues pulled attention in line with what people were
  searching for, about as in the group's earlier visible-cue study. That leans against the
  prediction if a goal held in advance counts as deliberate control, but the control the
  prediction names (holding, pushing away or moving attention with respect to the unseen cue)
  was never asked of people. The visible-cue comparison is across two papers and two sets of
  people, and the earlier one was not opened.

Weights, if both count: each study is outside the theory's camp and nothing else, so weight 2
(1 plus one for outside camp). They come from two different groups (Indian Institute of
Technology Kanpur; Jilin University and partners).

## Not opened (2 of the 5; no judgement made)

- **Bong and colleagues 2025 (NeuroImage), for the domain prediction.** Open access (CC BY-NC),
  but ScienceDirect refused an automated fetch (403) and Elsevier's article service gave no text
  without a key. John needs no sign-in: open https://doi.org/10.1016/j.neuroimage.2025.121606 in
  the browser pane. Verify entry `v-bong-2025`.
- **Lo 2018 (Attention, Perception, & Psychophysics), for the covary prediction.** OpenAlex lists
  a free copy at Springer, but the address answered with a robot check, not bypassed. John would
  open https://doi.org/10.3758/s13414-017-1474-7 in a normal browser (free if OpenAlex is right;
  otherwise a library sign-in to Springer). Verify entry `v-lo-2018`.
- Also on the verify list: the same group's earlier visible-cue study that the Wang result is
  compared with (`v-wang-2021-visible-cues`).

## Rule results John may not have intended (listed, not patched)

1. **The control place turned on one screening call.** The newest study on the control list,
   Qiu and colleagues 2023 (fearful faces, Frontiers in Neuroscience, PMID 37034154), was screened
   out because, by its own abstract, the masked faces drew no measurable attention, so the
   condition the test needs (unseen but still pulling attention) was absent and its result
   cannot count either way. A reader who screens it in would put it in the control place instead
   of Wang 2022; how it would read was not looked at beyond the abstract.
2. **Wang 2022 qualified on a broad reading of "control".** It measures whether a goal set in
   advance shapes the pull of unseen cues, not deliberate correction of attention afterwards.
   The screening criterion (does it measure what the test wording names) let it in because the
   test names deliberate control and the paper is about goal-driven ("top-down") control of
   unseen cues. Read narrowly, the next control study down would be the lab's own (already in
   the records), then Güldener 2021.
3. **The domain search mostly found studies about dissociative disorders**, because the query
   word "dissociat*" also matches the psychiatric term. Only one study measured both attention to
   and awareness of an inner kind of content (the heartbeat). The query was applied as fixed.
4. **The schema-control search was swamped by "model of attention-deficit hyperactivity
   disorder"** and by machine-learning "attention mechanism" papers (231 hits, none in the first
   40 qualifying). The lab's own agent study (`wilterson-2021-agent`) is not in the first 40. The
   query was applied as fixed.
5. **The claims prediction has no study at all** (4 hits, none with data on what a system says
   about itself), which fits the prediction being about artificial systems that do not yet exist
   in the needed form.
6. **The five-most-recent rule reaches back to 2017 for the covary place.** The covary search's
   newest qualifying study is from 2017; that is the method working as written, because the
   search has only 14 hits and they are older.
7. **The own-lab ruling did not bite on the new studies.** None of the four new studies is from
   the theory's own lab; the ruling had already settled the reused lab study as "unclear" on both
   its predictions. Whether the two judged results move any score also depends on the settled
   testability of the graded and control predictions, which this task did not touch.

## Every screened result

Format: rank, date as Europe PMC gives it (the screen's order; earliest public appearance is
checked only for the studies chosen), title, PubMed id: verdict. "Off topic" means not about
awareness and attention in the sense the test names.

### ast-graded

Query run 2026-11-21 09:48 PST; 122 hits; 40 screened.

1. 2026-10-30, Robust Engagement Estimation in Mixed Reality Under Cognitive Attack. (PMID 42961794): does not qualify: off topic (not about awareness and attention in the sense the test names)
2. 2026-08-03, Radiation Safety Knowledge, Perceptions, and Self-Reported Practices Among Healthcare Workers in Radiology and Nuclear Medicine: A Cross-Sectional Survey. (PMID 42588337): does not qualify: off topic (not about awareness and attention in the sense the test names)
3. 2026-07-21, Diagnostic Discrimination of BOKE STARS, a Bimodal Continuous Performance Test, for Attention-Deficit/Hyperactivity Disorder Assessment in Chinese Children: Single-Center Case-Control Study. (PMID 42480509): does not qualify: off topic (not about awareness and attention in the sense the test names)
4. 2026-03-26, Gastric acid secretion therapy: long-term effects on gastric mucosa and polyp formation. (PMID 41882503): does not qualify: review, theory or comment, no new data
5. 2026-04-21, Factors Influencing the Use of Mobile Apps and Wearables: Pre- and Post-Surgery Quality of Life Assessment Study. (PMID 42013368): does not qualify: off topic (not about awareness and attention in the sense the test names)
6. 2026-08-24, Gradedness of gist perception with scenes depends on concurrent task load: awareness under high load is more graded due to noise suppression. (PMID 42828214): TAKEN (kumar-2026): attention varied by a second task, clarity ratings on a four-step scale
7. 2024-11-25, Campus Sexual Assault: A Qualitative Review and Meta-Synthesis of Students' Experiences of Campus Prevention Initiatives. (PMID 39584525): does not qualify: review, theory or comment, no new data
8. 2025-11-01, Health History, Health Condition, Health Behaviours and Health-Seeking Behaviours of Middle-Aged Women Living in a Modern Rural Community: A Survey Research. (PMID 41255219): does not qualify: off topic (not about awareness and attention in the sense the test names)
9. 2025-11-01, Work-Related Musculoskeletal Disorders Among Podiatric Physicians in Singapore. (PMID 40009467): does not qualify: off topic (not about awareness and attention in the sense the test names)
10. 2025-10-09, Qualitative study of stakeholder perspectives on dementia policy implementation in Macao: progress, challenges and future directions. (PMID 41067772): does not qualify: off topic (not about awareness and attention in the sense the test names)
11. 2025-07-16, Sabbaticals for Academic Surgeons: A Forgotten Enterprise in Faculty Development? (PMID 39831694): does not qualify: review, theory or comment, no new data
12. 2025-07-01, Intelligent Assessment Systems in Medical Education: A Systematic Review. (PMID 40642143): does not qualify: review, theory or comment, no new data
13. 2025-07-05, How to quantify between-study heterogeneity in single-arm evidence synthesis?-It depends! (PMID 40618136): does not qualify: off topic (not about awareness and attention in the sense the test names)
14. 2025-06-19, From Perception to Action: Air Pollution Awareness and Behavioral Adjustments in Pregnant Women in Serbia. (PMID 40565502): does not qualify: off topic (not about awareness and attention in the sense the test names)
15. 2025-05-13, Ongoing epidemic of scarlet fever in Shanghai and the emergence of M1UK lineage group A Streptococcus: a 14-year surveillance study across the COVID-19 pandemic period. (PMID 40487265): does not qualify: off topic (not about awareness and attention in the sense the test names)
16. 2025-05-20, A nationwide comparative analysis of the prevalance and determinants of non-communicable diseases risk factors between Jordanian and displaced Syrian populations. (PMID 40394471): does not qualify: off topic (not about awareness and attention in the sense the test names)
17. 2025-09-28, Prevalence and Severity of Pruritus in Patients on Hemodialysis: A Cross-Sectional Study. (PMID 41030529): does not qualify: off topic (not about awareness and attention in the sense the test names)
18. 2025-01-28, Barriers to and facilitators of healthcare professionals in ADR reporting in a tertiary care hospital in India. (PMID 39875957): does not qualify: off topic (not about awareness and attention in the sense the test names)
19. 2024-11-05, The effect of covert visual attention on pupil size during perceptual fading. (PMID 39532655): does not qualify: measures pupil size during fading; no clarity ratings at varied amounts of attention
20. 2024-10-18, First case of fungal peritonitis caused by Neosartorya hiratsukae in China. (PMID 39502836): does not qualify: off topic (not about awareness and attention in the sense the test names)
21. 2024-11-05, Influence of Distraction Factors on Performance in Laparoscopic Surgery in Immersive Virtual Reality: Study Protocol of a Cross-Over Trial in Medical Students and Residents-DisLapVR. (PMID 39500487): does not qualify: a study protocol, no data yet
22. 2024-09-11, Social and humanitarian issues in nephrology and hypertension. (PMID 39258991): does not qualify: review, theory or comment, no new data
23. 2024-09-21, An ISM-MICMAC-based study for identification and classification of preventable safety risk mitigation factors in mass housing projects following a BIM approach. (PMID 39386802): does not qualify: off topic (not about awareness and attention in the sense the test names)
24. 2024-10-01, [Utilizing ChatGPT in Systematic Reviews and Meta-Analyses]. (PMID 39350706): does not qualify: off topic (not about awareness and attention in the sense the test names)
25. 2024-07-01, Study on Awareness of Suicide and Suicide Prevention Among Community Youth. (PMID 38966193): does not qualify: off topic (not about awareness and attention in the sense the test names)
26. 2024-01-18, Effects of task type on spontaneous alternations of attentional states. (PMID 38238501): does not qualify: mind-wandering reports; attention not varied with a stimulus held the same
27. 2023-09-14, The relationship between sensory impairment and home care client's received care time-A cross-sectional study. (PMID 37710399): does not qualify: off topic (not about awareness and attention in the sense the test names)
28. 2024-02-01, Exploring patient delay in people with chronic kidney disease: A cross-sectional study. (PMID 38363926): does not qualify: off topic (not about awareness and attention in the sense the test names)
29. 2024-10-21, Medication adherence among Japanese patients with developmental disabilities: a survey study. (PMID 39497900): does not qualify: off topic (not about awareness and attention in the sense the test names)
30. 2024-04-18, Improving access to cancer clinical research in Brazil: recent advances and new opportunities. Expert opinions from the 4th CURA meeting, São Paulo, 2023. (PMID 38774565): does not qualify: off topic (not about awareness and attention in the sense the test names)
31. 2023-06-12, Exploring intrusions without awareness: A preliminary study of the characteristics and influences of meta-awareness failures. (PMID 37327656): does not qualify: intrusive memories noticed or not; no clarity ratings at varied attention
32. 2023-05-22, Patient's perception of hygiene in the dental practice after COVID-19. (PMID 37213091): does not qualify: off topic (not about awareness and attention in the sense the test names)
33. 2023-05-01, Expansion of hantavirus infection during the SARS-CoV-2 pandemic in Bosnia and Herzegovina, 2021. (PMID 37255412): does not qualify: off topic (not about awareness and attention in the sense the test names)
34. 2023-04-24, How do healthcare providers use national audit data for improvement? (PMID 37095495): does not qualify: off topic (not about awareness and attention in the sense the test names)
35. 2023-01-12, Self-caught methodologies for measuring mind wandering with meta-awareness: A systematic review. (PMID 36640586): does not qualify: review, theory or comment, no new data
36. 2023-07-06, Vitiligo-like lesions induced by cyclin-dependent kinase 4/6 inhibitor Palbociclib: a case report and literature review. (PMID 37483648): does not qualify: review, theory or comment, no new data
37. 2023-02-02, Level of Patient Safety Culture Awareness Among Healthcare Workers. (PMID 36756087): does not qualify: off topic (not about awareness and attention in the sense the test names)
38. 2022-11-07, Consumer-Led Screening for Atrial Fibrillation: Frontier Review of the AF-SCREEN International Collaboration. (PMID 36343103): does not qualify: review, theory or comment, no new data
39. 2021-11-22, Two faces of perceptual awareness during the attentional blink: Gradual and discrete. (PMID 34807708): qualifies, not taken: attention varied (attentional blink) with continuous reports of what was seen; older than kumar-2026, and the one-per-prediction cap keeps one place for ast-graded
40. 2021-08-10, Effects of mobile mindfulness on emergency department work stress: A randomised controlled trial. (PMID 34378320): does not qualify: off topic (not about awareness and attention in the sense the test names)

### ast-covary

Query run 2026-11-21 09:48 PST; 14 hits; 14 screened.

1. 2017-07-22, Neural processes underlying the orienting of attention without awareness. (PMID 28826603): qualifies, not taken: cueing with and without awareness of the cue (masking), attention measured both ways; older than lo-2018 (2017-07-22 against 2017-12-26)
2. 2018-04-01, Attention without awareness: Attentional modulation of perceptual grouping without awareness. (PMID 29280049): TAKEN (lo-2018): attention acting on a pattern people report not seeing; NOT OPENED
3. 2016-05-03, Reward-associated features capture attention in the absence of awareness: Evidence from object-substitution masking. (PMID 27153978): qualifies, not taken: attention drawn by targets people were unaware of (masking); older
4. 2015-04-25, Exogenous attention to unseen objects? (PMID 25922174): qualifies, not taken: attention to objects that stay unseen; older
5. 2013-04-09, Object-based attention without awareness. (PMID 23572282): qualifies, not taken: attention to objects that stay unseen; older
6. 2012-07-12, The attentional requirements of consciousness. (PMID 22795561): does not qualify: an opinion piece proposing tests, no new data (by its abstract)
7. 2011-08-12, Natural-scene perception requires attention. (PMID 21841149): qualifies, not taken: tests awareness without attention for natural scenes; older
8. 2007-12-17, Attended but unseen: visual attention is not sufficient for visual awareness. (PMID 18237752): qualifies, not taken: attention changes priming by colours people do not see; older
9. 2008-02-29, Distinct and independent correlates of attention and awareness in a hemianopic patient. (PMID 18396301): qualifies, not taken: attention and reported awareness measured apart in a patient with blindsight; older
10. 2004-08-01, Perceptual grouping and attention: not all groupings are equal. (PMID 15581119): does not qualify: grouping under inattention; no report of awareness named in the abstract
11. 2003-01-01, Orienting of attention without awareness is affected by measurement-induced attentional control settings. (PMID 12678623): qualifies, not taken: attention drawn by masked cues, with and without asking for reports; older
12. 2001-10-01, Perceptual learning without perception. (PMID 11677607): does not qualify: learning from a stimulus that was neither attended nor seen; attention to it not measured
13. 1999-09-01, Attention without awareness in blindsight. (PMID 10518327): qualifies, not taken: attention without awareness in blindsight; older
14. 1997-02-01, Orienting attention without awareness. (PMID 9157183): qualifies, not taken: attention drawn by cues below the threshold of awareness; older

### ast-claims

Query run 2026-11-21 09:49 PST; 4 hits; 4 screened.

1. 2025-08-20, Probing for consciousness in machines. (PMID 40910115): does not qualify: an artificial agent probed for an internal map of itself and the world; it is given no way to describe itself and makes no claims
2. 2022-01-11, Predictive Neuronal Adaptation as a Basis for Consciousness. (PMID 35087383): does not qualify: a simulation with no new data, about a different theory
3. 2019-10-25, A Naturalistic Approach to the Hard Problem of Consciousness. (PMID 31708755): does not qualify: review, theory or comment, no new data
4. 2018-11-23, The Embodied Self, the Pattern Theory of Self, and the Predictive Mind. (PMID 30532721): does not qualify: review, theory or comment, no new data

### ast-control

Query run 2026-11-21 09:49 PST; 77 hits; 40 screened.

1. 2026-07-01, Temporal dynamics of adapting to novel contexts during the generalization of learned spatial suppression. (PMID 42536381): does not qualify: learned suppression of a distractor location; awareness not manipulated (by the abstract)
2. 2025-04-25, Self-report and actigraphy measures of sleep and domain-specific cognitive performance in older adults. (PMID 40274698): does not qualify: off topic (not about awareness and attention in the sense the test names)
3. 2025-11-18, Apoe genotype knowledge and its impact on cognitive beliefs and performance. (PMID 41252556): does not qualify: off topic (not about awareness and attention in the sense the test names)
4. 2024-11-01, The potential mechanisms underlying the effect of acute alcohol use on duration perception. (PMID 39542435): does not qualify: off topic (not about awareness and attention in the sense the test names)
5. 2024-08-12, Neural Correlates of the Attentional Bias Towards Subliminal Pornographic Cues in Individuals with Tendencies Toward Problematic Pornography Use: An ERP Study Using a Dot-Probe Task. (PMID 39134733): does not qualify: automatic pull of attention by masked cues only; no deliberate control measured
6. 2023-03-30, Altered Gaze Control During Emotional Face Exploration in Patients With Amyotrophic Lateral Sclerosis. (PMID 36997323): does not qualify: off topic (not about awareness and attention in the sense the test names)
7. 2023-03-23, Attentional capture by fearful faces requires consciousness and is modulated by task-relevancy: A dot-probe EEG study. (PMID 37034154): does not qualify: masked faces drew no measurable attention, so the condition the test needs (unseen but still drawing attention) was absent and the result cannot count either way; the top-down effect was shown only for visible faces. A screening call; see the notes
8. 2022-03-15, Assessing anxiety-linked impairment in attentional control without eye-tracking: The masked-target antisaccade task. (PMID 35292933): does not qualify: a masked target in an anxiety test; awareness of a stimulus drawing attention not manipulated
9. 2022-11-17, Subliminal meaning-contingent attentional orienting: The role of attentional control setting based on displaywide features. (PMID 36533058): TAKEN (wang-2022): masked cues people could not see, and whether a goal set in advance decides which of them draw attention
10. 2022-11-21, Facial mask disturbs ocular exploration but not pupil reactivity. (PMID 36478875): does not qualify: off topic (not about awareness and attention in the sense the test names)
11. 2021-06-01, Attention, awareness, and the right temporoparietal junction. (PMID 34161276): qualifies, not taken for this prediction: masked versus visible cue used to steer attention; it is wilterson-2021-tpj, which took the ast-tpj place (see the cap note) and is judged for both
12. 2021-01-06, The effect of emotional valence and age of faces on adults and children's inattentional blindness. (PMID 33409905): does not qualify: noticing an unexpected face; awareness measured, control of attention to it not
13. 2021-02-10, How society modulates our behavior: Effects on error processing of masked emotional cues contextualized in social status. (PMID 33494660): does not qualify: masked cues and error monitoring; attention to the cue not measured
14. 2021-01-29, Feature-Based Attentional Weighting and Re-weighting in the Absence of Visual Awareness. (PMID 33584229): qualifies, not taken: whether unseen stimuli can re-weight what attention selects; older
15. 2020-08-16, Unseen food images capture the attention of hungry viewers: Evidence from event-related potentials. (PMID 32814119): does not qualify: automatic pull of attention by unseen images only; no deliberate control measured
16. 2020-07-20, To look or not to look: Subliminal abruptonset cues influence constrained free-choice saccades. (PMID 33828805): qualifies, not taken: whether attention control settings govern masked cues' pull on eye movements; older
17. 2019-10-03, Speech-in-speech perception, nonverbal selective attention, and musical training. (PMID 31580123): does not qualify: off topic (not about awareness and attention in the sense the test names)
18. 2020-11-30, Reward Influences Masked Free-Choice Priming. (PMID 33329223): does not qualify: reward and masked priming; attention to the prime not measured
19. 2019-08-29, Attentional capture alters feature perception. (PMID 31464467): does not qualify: capture by visible distractors; awareness not manipulated
20. 2018-05-15, The impact of temporal contingencies between cue and target onset on spatial attentional capture by subliminal onset cues. (PMID 29766295): qualifies, not taken: whether masked cues capture attention regardless of a top-down timing setting; older
21. 2019-08-01, The Nature of Unconscious Attention to Subliminal Cues. (PMID 31735839): does not qualify: review, theory or comment, no new data
22. 2019-08-01, Influence of Methylphenidate on Long-Term Neuropsychological and Everyday Executive Functioning After Traumatic Brain Injury in Children with Secondary Attention Problems. (PMID 31178001): does not qualify: off topic (not about awareness and attention in the sense the test names)
23. 2018-05-05, Attentional and Interpretational Biases Toward Pain-Related Stimuli in Children and Adolescents: ASystematic Review of the Evidence. (PMID 29733993): does not qualify: review, theory or comment, no new data
24. 2018-04-01, The power law of visual working memory characterizes attention engagement. (PMID 29733667): does not qualify: off topic (not about awareness and attention in the sense the test names)
25. 2018-02-07, EEG measures of brain activity reveal that smoking-related images capture the attention of smokers outside of awareness. (PMID 29427572): does not qualify: automatic pull of attention by unseen images only; no deliberate control measured
26. 2018-01-01, Correction to: Dissociating the capture of attention from saccade activation by subliminal abrupt onsets. (PMID 29255916): does not qualify: off topic (not about awareness and attention in the sense the test names)
27. 2017-07-28, Dissociating the capture of attention from saccade activation by subliminal abrupt onsets. (PMID 28755238): qualifies, not taken: masked onsets in a task that requires looking away from them (anti-saccades); older
28. 2017-07-21, The Neural Bases of Event Monitoring across Domains: a Simultaneous ERP-fMRI Study. (PMID 28785212): does not qualify: off topic (not about awareness and attention in the sense the test names)
29. 2016-05-03, Reward-associated features capture attention in the absence of awareness: Evidence from object-substitution masking. (PMID 27153978): does not qualify: automatic pull of attention by unseen targets only; no deliberate control measured
30. 2016-02-02, Effects of Awareness on the Control of Attention. (PMID 26836517): qualifies, not taken: webb-2016, already in the records (not opened); older
31. 2015-12-15, Subliminal trauma reminders impact neural processing of cognitive control in adults with developmental earthquake trauma: a preliminary report. (PMID 26670907): does not qualify: masked trauma reminders and cognitive control in general, not control of attention to the reminder
32. 2016-10-21, Decreased Pain Perception by Unconscious Emotional Pictures. (PMID 27818642): does not qualify: masked pictures and pain ratings; attention not measured
33. 2016-10-20, Contributions of Sensory Coding and Attentional Control to Individual Differences in Performance in Spatial Auditory Selective Attention Tasks. (PMID 27812330): does not qualify: off topic (not about awareness and attention in the sense the test names)
34. 2015-11-06, Involuntary attentional orienting in the absence of awareness speeds up early sensory processing. (PMID 26673944): does not qualify: automatic orienting to unseen cues only; no deliberate control measured
35. 2015-08-14, Evaluating automatic attentional capture by self-relevant information. (PMID 26208833): does not qualify: review, theory or comment, no new data
36. 2015-11-01, An inability to set independent attentional control settings by hemifield. (PMID 26220268): does not qualify: control settings with visible stimuli; awareness not manipulated
37. 2015-02-10, Boundary conditions for the influence of unfamiliar non-target primes in unconscious evaluative priming: The moderating role of attentional task sets. (PMID 25680827): does not qualify: masked primes and task set; attention to the prime not measured
38. 2015-02-09, S-ketamine influences strategic allocation of attention but not exogenous capture of attention. (PMID 25676122): does not qualify: off topic (not about awareness and attention in the sense the test names)
39. 2015-06-10, Action video game players' visual search advantage extends to biologically relevant stimuli. (PMID 26071923): does not qualify: off topic (not about awareness and attention in the sense the test names)
40. 2015-04-01, Stimulus-driven attentional capture by subliminal onset cues. (PMID 25520044): qualifies, not taken: masked cues capture attention even when they do not fit the top-down setting; older

### ast-schema-control

Query run 2026-11-21 09:50 PST; 231 hits; 40 screened.

1. 2026-10-31, The broiler chicken as a model for studying partial exocrine pancreatic insufficiency. (PMID 42987764): does not qualify: off topic (not about awareness and attention in the sense the test names)
2. 2026-10-09, Psychometric Validation and Nomological Network of the Amsterdam Executive Function Inventory (AEFI) in Ecuadorian Adolescents. (PMID 42938577): does not qualify: off topic (not about awareness and attention in the sense the test names)
3. 2026-10-09, Understanding consciousness (biological and artificial) as a society of self-schemas. (PMID 42853683): does not qualify: review, theory or comment, no new data (Graziano 2026, the theory's own)
4. 2026-07-22, Systematic evaluation of single-cell foundation model interpretability: attention-derived edge scores add no incremental value over gene-level features for perturbation-target prediction. (PMID 42482180): does not qualify: off topic (not about awareness and attention in the sense the test names)
5. 2026-06-29, Graph-based analysis of work-from-home layouts and affective responses in virtual reality. (PMID 42373868): does not qualify: off topic (not about awareness and attention in the sense the test names)
6. 2026-06-26, Health prediction of metro platform screen door system based on XGBoost-BiGRU-attention model. (PMID 42362812): does not qualify: off topic (not about awareness and attention in the sense the test names)
7. 2026-05-01, [Driver gene mutations predicted by pathology-foundation-model and their clinical associations in clear cell renal cell carcinoma]. (PMID 42103618): does not qualify: off topic (not about awareness and attention in the sense the test names)
8. 2026-05-05, Predicting driver adaptability: a computational rationality model for attention allocation in lateral vehicle control. (PMID 42084985): does not qualify: a computational model of drivers' attention; no controller with and without a model of its own attention
9. 2025-08-27, Impact of Hearing Loss and Cochlear Implantation on Attentional Selection in Older Adults. (PMID 40862498): does not qualify: hearing loss and attentional selection; no model of attention compared
10. 2026-10-13, Research on hybrid estimation algorithm for dynamic center-of-mass parameters of tracked agricultural transport platform. (PMID 42948087): does not qualify: off topic (not about awareness and attention in the sense the test names)
11. 2026-07-21, An adjustable wave model for attention restoration. (PMID 42553581): does not qualify: off topic (not about awareness and attention in the sense the test names)
12. 2026-05-05, Route selection impairment and microglia activation in a rodent model of attention-deficit hyperactivity disorder. (PMID 42164021): does not qualify: off topic (not about awareness and attention in the sense the test names)
13. 2025-12-25, Gestational physical exercise prevents early-life behavioral impairments in the offspring of a rat model of attention deficit hyperactivity disorder. (PMID 41449231): does not qualify: off topic (not about awareness and attention in the sense the test names)
14. 2025-05-08, A novel CNN-LSTM model with attention mechanism for online monitoring of moisture content in fluidized bed granulation process based on near-infrared spectroscopy. (PMID 40367754): does not qualify: off topic (not about awareness and attention in the sense the test names)
15. 2025-08-06, Decoding Covert Visual Attention in Space and Time from Neural Signals. (PMID 40769500): does not qualify: review, theory or comment, no new data
16. 2025-07-24, Expanding the framework of attention in posttraumatic stress disorder: Commentary on Clauss et al. (2025). (PMID 40704387): does not qualify: review, theory or comment, no new data
17. 2025-07-01, The analysis of acquisition system for electronic traffic signal in smart cities based on the internet of things. (PMID 40595191): does not qualify: off topic (not about awareness and attention in the sense the test names)
18. 2025-01-07, Visual attention matters during word recognition: A Bayesian modeling approach. (PMID 39777606): does not qualify: review, theory or comment, no new data
19. 2025-05-21, Advancing Traditional Dunhuang Regional Pattern Design with Diffusion Adapter Networks and Cross-Entropy. (PMID 40422500): does not qualify: off topic (not about awareness and attention in the sense the test names)
20. 2025-01-01, [Oral Ingestion of Umami during the Developmental Period Is Involved in Emotion Formation via the Vagus Nerve in Attention Deficit Hyperactivity Disorder Model Rats]. (PMID 40754410): does not qualify: off topic (not about awareness and attention in the sense the test names)
21. 2025-06-04, Genome-wide DNA methylation analysis of hippocampal tissue in a murine model of attention deficit-hyperactivity disorder. (PMID 40465750): does not qualify: off topic (not about awareness and attention in the sense the test names)
22. 2025-05-19, Neuromotor mechanisms of successful football penalty kicking: an EEG pilot study. (PMID 40458627): does not qualify: off topic (not about awareness and attention in the sense the test names)
23. 2024-12-30, Multi-environment and multi-parameter screening of stability and coating efficiency of gold nanoparticle bioconjugates in application media. (PMID 39738087): does not qualify: off topic (not about awareness and attention in the sense the test names)
24. 2024-11-01, Is hyperactivity in children with attention deficit/hyperactivity disorder (ADHD) a functional response to demands on specific executive functions or cognitive demands in general? (PMID 39480349): does not qualify: off topic (not about awareness and attention in the sense the test names)
25. 2024-07-30, Pollution loads in the middle-lower Yangtze river by coupling water quality models with machine learning. (PMID 39098157): does not qualify: off topic (not about awareness and attention in the sense the test names)
26. 2024-05-01, Alcohol withdrawal and amphetamine co-use in an animal model for attention deficit hyperactivity disorder. (PMID 38833614): does not qualify: off topic (not about awareness and attention in the sense the test names)
27. 2024-02-08, Factors affecting intent to perpetrate violence against nurses: Theory of Planned Behavior approach. (PMID 38330828): does not qualify: off topic (not about awareness and attention in the sense the test names)
28. 2024-02-01, No Effects of Decanoic Acid on Locomotor Activity and Antioxidant Defences in an Experimental Animal Model of Attention-Deficit/Hyperactivity Disorder. (PMID 38419446): does not qualify: off topic (not about awareness and attention in the sense the test names)
29. 2023-12-19, Impaired monoamine neural system in the mPFC of SHRSP/Ezo as an animal model of attention-deficit/hyperactivity disorder. (PMID 38246729): does not qualify: off topic (not about awareness and attention in the sense the test names)
30. 2024-03-11, A Novel CNN-BiLSTM Ensemble Model With Attention Mechanism for Sit-to-Stand Phase Identification Using Wearable Inertial Sensors. (PMID 38373135): does not qualify: off topic (not about awareness and attention in the sense the test names)
31. 2023-11-13, Emerging infectious disease surveillance using a hierarchical diagnosis model and the Knox algorithm. (PMID 37963966): does not qualify: off topic (not about awareness and attention in the sense the test names)
32. 2023-10-24, Validity of Diagnostic Support Model for Attention Deficit Hyperactivity Disorder: A Machine Learning Approach. (PMID 38003840): does not qualify: off topic (not about awareness and attention in the sense the test names)
33. 2023-09-14, The mesocortical dopaminergic system cannot explain hyperactivity in an animal model of attention deficit hyperactivity disorder (ADHD)- Spontaneously hypertensive rats (SHR). (PMID 37710339): does not qualify: off topic (not about awareness and attention in the sense the test names)
34. 2023-04-04, Rat model of attention-deficit hyperactivity disorder exhibits delayed recovery from acute incisional pain due to impaired descending noradrenergic inhibition. (PMID 37016045): does not qualify: off topic (not about awareness and attention in the sense the test names)
35. 2023-02-02, Sex-specific responses to juvenile stress on the dopaminergic system in an animal model of attention-deficit hyperactivity disorder. (PMID 36738506): does not qualify: off topic (not about awareness and attention in the sense the test names)
36. 2023-02-18, An explainable and interpretable model for attention deficit hyperactivity disorder in children using EEG signals. (PMID 36827785): does not qualify: off topic (not about awareness and attention in the sense the test names)
37. 2023-07-12, How attention factors into executive function in preschool children. (PMID 37502749): does not qualify: off topic (not about awareness and attention in the sense the test names)
38. 2023-05-15, The relative reinforcing efficacy of nicotine in an adolescent rat model of attention-deficit hyperactivity disorder. (PMID 37255676): does not qualify: off topic (not about awareness and attention in the sense the test names)
39. 2022-12-16, Semi-mechanistic reduced order model of pharmaceutical tablet dissolution for enabling Industry 4.0 manufacturing systems. (PMID 36529354): does not qualify: off topic (not about awareness and attention in the sense the test names)
40. 2022-12-04, Biomechanical and Sensory Feedback Regularize the Behavior of Different Locomotor Central Pattern Generators. (PMID 36546926): does not qualify: off topic (not about awareness and attention in the sense the test names)

### ast-tpj

Query run 2026-11-21 09:51 PST; 29 hits; 29 screened.

1. 2024-11-22, Resting-state functional connectivity in gelotophobes: A neuroscientific perspective on the fear of laughter. (PMID 39581269): does not qualify: off topic (not about awareness and attention in the sense the test names)
2. 2025-08-06, Human self and Neurosurgery: Advances and insights from Geneva. (PMID 40895030): does not qualify: review, theory or comment, no new data
3. 2021-12-20, Neural correlates of product attachment to cosmetics. (PMID 34930953): does not qualify: off topic (not about awareness and attention in the sense the test names)
4. 2021-06-15, The emergent relationship between temporoparietal junction and anosognosia in Alzheimer's disease. (PMID 34131953): does not qualify: review, theory or comment, no new data
5. 2021-06-04, Seeing things differently: Gaze shapes neural signal during mentalizing according to emotional awareness. (PMID 34098065): does not qualify: off topic (not about awareness and attention in the sense the test names)
6. 2021-06-01, Attention, awareness, and the right temporoparietal junction. (PMID 34161276): TAKEN (wilterson-2021-tpj, reused): right temporoparietal junction with visible versus masked cue, attention matched; also qualified for ast-control
7. 2021-05-21, Updating beliefs beyond the here-and-now: the counter-factual self in anosognosia for hemiplegia. (PMID 34151264): does not qualify: off topic (not about awareness and attention in the sense the test names)
8. 2020-09-08, To the self and beyond: Arousal and functional connectivity of the temporo-parietal junction contributes to spontaneous sensations perception. (PMID 32910970): does not qualify: junction connectivity and bodily sensations; attention not matched
9. 2020-04-01, The neuroanatomy of spatial awareness: a large-scale region-of-interest and voxel-based anatomical study. (PMID 31938986): does not qualify: stroke lesions and neglect tests (exploration, reading, line bisection), not reported awareness or control of attention apart
10. 2019-06-04, Toward a theory of consciousness: A review of the neural correlates of inattentional blindness. (PMID 31173773): does not qualify: review, theory or comment, no new data
11. 2018-06-22, Why could meditation practice help promote mental health and well-being in aging? (PMID 29933746): does not qualify: review, theory or comment, no new data
12. 2017-09-09, Semantic incongruity attracts attention at a pre-conscious level: Evidence from a TMS study. (PMID 28969900): qualifies, not taken: magnetic stimulation over the right temporoparietal junction and noticing a change (damage-style test); older
13. 2017-12-14, Brain structural alterations associated with dysfunctional cognitive control of pain in patients with low back pain. (PMID 29239055): does not qualify: off topic (not about awareness and attention in the sense the test names)
14. 2018-03-27, The temporoparietal junction and awareness. (PMID 30042858): does not qualify: review, theory or comment, no new data (Graziano 2018, the theory's own)
15. 2018-01-01, Unilateral spatial neglect after posterior parietal damage. (PMID 29519463): does not qualify: review, theory or comment, no new data
16. 2017-04-17, Game theoretical mapping of causal interactions underlying visuo-spatial attention in the human brain based on stroke lesions. (PMID 28419682): does not qualify: off topic (not about awareness and attention in the sense the test names)
17. 2016-12-23, Common and distinct brain regions processing multisensory bodily signals for peripersonal space and body ownership. (PMID 28017920): does not qualify: a meta-analysis of body-ownership studies, no new data
18. 2016-11-14, Cortical networks involved in visual awareness independent of visual attention. (PMID 27849616): qualifies, not taken: aware versus unaware with matched attention, brain scanning, from the Graziano lab (Webb and colleagues 2016); older
19. 2014-09-29, A Predominantly Visual Subdivision of The Right Temporo-Parietal Junction (vTPJ). (PMID 25267856): does not qualify: a visual region in the junction; attention varied, awareness not measured
20. 2014-02-04, Do you know what I mean? Brain oscillations and the understanding of communicative intentions. (PMID 24550813): does not qualify: off topic (not about awareness and attention in the sense the test names)
21. 2013-01-01, [Review of the effects of mindfulness meditation on mental and physical health and its mechanisms of action]. (PMID 24719001): does not qualify: review, theory or comment, no new data
22. 2011-11-12, Asymmetric loss of parietal activity causes spatial bias in prodromal and mild Alzheimer's disease. (PMID 22079258): does not qualify: off topic (not about awareness and attention in the sense the test names)
23. 2012-04-01, Dynamical properties of BOLD activity from the ventral posteromedial cortex associated with meditation and attentional skills. (PMID 22496570): does not qualify: off topic (not about awareness and attention in the sense the test names)
24. 2012-04-19, Hemispheric asymmetry in white matter connectivity of the temporoparietal junction with the insula and prefrontal cortex. (PMID 22536413): does not qualify: off topic (not about awareness and attention in the sense the test names)
25. 2011-11-01, How Does Mindfulness Meditation Work? Proposing Mechanisms of Action From a Conceptual and Neural Perspective. (PMID 26168376): does not qualify: review, theory or comment, no new data
26. 2007-12-12, What are you feeling? Using functional magnetic resonance imaging to assess the modulation of sensory and affective responses during empathy for pain. (PMID 18091986): does not qualify: off topic (not about awareness and attention in the sense the test names)
27. 2005-12-01, Visual short-term memory load suppresses temporo-parietal junction activity and induces inattentional blindness. (PMID 16313661): does not qualify: memory load lowers junction activity and noticing together, so attention and awareness are not separated
28. 2005-04-01, [Neural correlates of priming in vision: evidence from neuropsychology and neuroimaging]. (PMID 16155328): does not qualify: off topic (not about awareness and attention in the sense the test names)
29. 2000-03-01, A multimodal cortical network for the detection of changes in the sensory environment. (PMID 10700261): does not qualify: brain response to sensory change; attention and awareness not separated

### ast-domain

Query run 2026-11-21 09:51 PST; 37 hits; 37 screened.

1. 2026-09-25, Resting-state EEG dissociates heartbeat counting from heart-rate discrimination: Cortical signal entropy tracks counting accuracy, default-mode connectivity tracks exteroceptive discrimination. (PMID 42790611): does not qualify: resting brain waves and heartbeat counting; attention to the heartbeat not measured apart from awareness
2. 2026-08-05, Examining the Mediating Role of Emotion Regulation Difficulties and Mindfulness in the Relationship Between Sexual Abuse and Dissociative Experiences. (PMID 42552831): does not qualify: off topic (not about awareness and attention in the sense the test names)
3. 2026-06-12, Prisoners of the Body: The Link Between Interoception and Sleep Paralysis. (PMID 42283104): does not qualify: off topic (not about awareness and attention in the sense the test names)
4. 2026-09-24, Watchfulness (Nepsis) and Attentive Presence (Prosoche): A Patristic Framework for Clinical and Spiritual Healing. (PMID 42798700): does not qualify: off topic (not about awareness and attention in the sense the test names)
5. 2026-02-09, Subjective symptoms of functional/dissociative seizures and their diagnostic value: A systematic review. (PMID 41661078): does not qualify: review, theory or comment, no new data
6. 2026-03-01, Emotion Regulation and Neurocognitive Profiles in Adolescents With Selective Mutism. (PMID 41860376): does not qualify: off topic (not about awareness and attention in the sense the test names)
7. 2026-03-03, Cognitive Complaints in Schizophrenia: A Meta-Analysis of Studies Using the Subjective Scale to Investigate Cognition in Schizophrenia (SSTICS): Les plaintes cognitives dans la schizophrénie : Une méta-analyse des études utilisant la Subjective Scale To Investigate Cognition in Schizophrenia (SSTICS). (PMID 41773631): does not qualify: review, theory or comment, no new data
8. 2026-01-02, Toward dimensional body consciousness impairments in post-traumatic stress disorder and its dissociative subtype: A predictive processing approach. (PMID 41485717): does not qualify: review, theory or comment, no new data
9. 2026-10-02, Beyond heartbeats: re-thinking interoception in autism through virtual reality and computational modelling. (PMID 42890209): does not qualify: review, theory or comment, no new data
10. 2026-01-23, Unaware and unrestrained: binge-eating behavior in epileptic absence seizures. (PMID 41575613): does not qualify: off topic (not about awareness and attention in the sense the test names)
11. 2025-11-22, Conscious cardiac awareness and interoceptive attention differentially modulate heartbeat-evoked neural dynamics. (PMID 41285234): TAKEN (bong-2025): attention to one's heartbeat and reported awareness of it, measured apart; NOT OPENED
12. 2025-03-27, EEG oscillations reveal neuroplastic changes in pain processing associated with long-term meditation. (PMID 40148498): does not qualify: off topic (not about awareness and attention in the sense the test names)
13. 2024-02-01, Metaphorical language and psychopathological symptoms: a case study of trauma victims' metaphor use. (PMID 38303003): does not qualify: off topic (not about awareness and attention in the sense the test names)
14. 2023-07-01, [Validated care programs for patients with functional neurological disorders]. (PMID 37400332): does not qualify: review, theory or comment, no new data
15. 2022-05-08, The Molecular Genetics of Dissociative Symptomatology: A Transdiagnostic Literature Review. (PMID 35627228): does not qualify: review, theory or comment, no new data
16. 2021-07-07, Beyond internalizing and externalizing symptoms: The association between body disconnection and the symptoms of Internet gaming disorder. (PMID 34315095): does not qualify: off topic (not about awareness and attention in the sense the test names)
17. 2021-11-15, The effects of subliminal or supraliminal sadness induction on the sense of body ownership and the role of dissociative symptoms. (PMID 34782628): does not qualify: unseen sad pictures and body ownership; attention to the pictures not measured
18. 2020-02-01, Dissociation in How Core Autism Features Relate to Interoceptive Dimensions: Evidence from Cardiac Awareness in Children. (PMID 31705421): does not qualify: off topic (not about awareness and attention in the sense the test names)
19. 2020-10-22, Altered interoception in patients with borderline personality disorder: a study using heartbeat-evoked potentials. (PMID 33101689): does not qualify: off topic (not about awareness and attention in the sense the test names)
20. 2020-07-10, Motivated Cue-Integration and Emotion Regulation: Awareness of the Association Between Interoceptive and Exteroceptive Embodied Cues and Personal Need Creates an Emotion Goal. (PMID 32754097): does not qualify: off topic (not about awareness and attention in the sense the test names)
21. 2018-06-05, Dissociative absorption, mind-wandering, and attention-deficit symptoms: Associations with obsessive-compulsive symptoms. (PMID 29873088): does not qualify: off topic (not about awareness and attention in the sense the test names)
22. 2018-01-22, Deficits in Response Inhibition in Patients with Attention-Deficit/Hyperactivity Disorder: The Impaired Self-Protection System Hypothesis. (PMID 29403397): does not qualify: off topic (not about awareness and attention in the sense the test names)
23. 2017-02-21, Attentional Modulation of Change Detection ERP Components by Peripheral Retro-Cueing. (PMID 28270759): does not qualify: attention and awareness of a visual change; one ordinary outer kind of content, so it does not bear on how far awareness reaches across kinds
24. 2015-09-21, Intact error monitoring in combat Veterans with post-traumatic stress disorder. (PMID 26481979): does not qualify: off topic (not about awareness and attention in the sense the test names)
25. 2015-04-14, Dissociation between the cognitive and interoceptive components of mindfulness in the treatment of chronic worry. (PMID 25912677): does not qualify: off topic (not about awareness and attention in the sense the test names)
26. 2015-04-23, The attention schema theory: a mechanistic account of subjective awareness. (PMID 25954242): does not qualify: review, theory or comment, no new data (Graziano and Webb 2015, the theory's own)
27. 2013-11-07, The balanced mind: the variability of task-unrelated thoughts predicts error monitoring. (PMID 24223545): does not qualify: mind-wandering reports and error monitoring; attention selecting the thoughts not measured
28. 2012-08-15, Suppression of aversive memories associates with changes in early and late stages of neurocognitive processing. (PMID 22917568): does not qualify: off topic (not about awareness and attention in the sense the test names)
29. 2012-04-04, Use of hypnosis in the treatment of pain. (PMID 22514773): does not qualify: review, theory or comment, no new data
30. 2012-05-07, The role of consciousness in cognitive control and decision making. (PMID 22586386): does not qualify: review, theory or comment, no new data
31. 2011-01-26, Dissociating spatial attention and awareness in emotion-induced blindness. (PMID 21270446): does not qualify: emotional pictures and spatial attention in vision; same reason as the visual change study
32. 2007-10-01, Neural biases to covert and overt signals of fear: dissociation by trait anxiety and depression. (PMID 17854280): does not qualify: off topic (not about awareness and attention in the sense the test names)
33. 2006-02-07, Identity state-dependent attentional bias for facial threat in dissociative identity disorder. (PMID 16455142): does not qualify: off topic (not about awareness and attention in the sense the test names)
34. 2004-10-01, Adaptive and maladaptive self-focus in depression. (PMID 15465571): does not qualify: off topic (not about awareness and attention in the sense the test names)
35. 1997-05-01, Neurobiology of consciousness: an overview. (PMID 9105571): does not qualify: review, theory or comment, no new data
36. 1994-03-01, Implicit learning. (PMID 8165269): does not qualify: review, theory or comment, no new data
37. 1991-01-01, Integrating affect in treatment with adult survivors of physical and sexual abuse. (PMID 2006678): does not qualify: review, theory or comment, no new data
