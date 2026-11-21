# Damasio's feeling-based theory: screening the per-prediction searches, 2026-11-21

Seven searches, one per prediction, were run on 2026-11-21 against Europe PMC by the method
fixed in `data/tracker/searches-2026-11-21.toml` before any of them ran. This file records what
each search returned, what happened to every result, which studies were chosen, and where a rule
gave a result John may not have intended. Nothing in the repository was touched; the records are
the four TOML files beside this one.

Everything here was screened on the title and the abstract only, as the method says. Full texts
were opened afterwards, and only for the chosen studies.

## What "qualifies" meant, applied the same way seven times

The method says a result qualifies when its title or abstract shows that it (a) reports new data,
or a reanalysis, from people, animals, tissue, a physical system or an artificial agent, and
(b) measures what the prediction's own test wording names, so that its result could count for or
against it. The second half did most of the work here, so it is worth saying how it was read:
**the thing the study measures has to be the thing the prediction's test names, not a neighbour of
it.** Measuring brain activity in a body-sensing region is not measuring a feeling. Describing a
newborn animal's reflexes is not measuring whether it feels hunger in a graded, flexible way.
Where a result sat near the line it is marked below as a borderline row, with the call and the
reason, so a second reader can disagree in one place.

Reason codes used in the tables:

- **A** — no new data: a review, a commentary, a theory paper, a modelling paper, a protocol, a
  guideline, a historical piece, or a case report that describes a condition without measuring
  what the prediction's test names.
- **B** — new data, but what it measures is not what this prediction's test names (each row says
  what it measured instead).
- **C** — the search words matched a different subject entirely (chest surgery, dentistry,
  agriculture, veterinary pathology, materials science), so nothing about the prediction.
- **T** — taken.

## 1. `dam-feeling-required` (without feelings of the body's state there is no consciousness)

Hits: 66. Screened: the first 40, in order.

| # | id | date | call | why |
|---|---|---|---|---|
| 1 | 43052692 | 2026-11-18 | B | New data: one patient with locked-in syndrome given zolpidem, with heartbeat-evoked brain responses and heart-rate variability. It measures brain-to-heart signalling and outward responsiveness, not whether the man had feelings of his body's state. **Borderline:** its finding of responsiveness returning while heart-brain communication collapsed is the closest thing in this list to the prediction's own counter-case, and a reader who accepts heartbeat-evoked responses as a measure of bodily feeling would take it and read the outcome as against the prediction. Not taken because the prediction's test asks for validated measures of felt hunger, thirst or pain, which an unresponsive patient cannot give. |
| 2 | 42664575 | 2026-08-23 | A | A proposed framework for cranial osteopathy; no data of its own. |
| 3 | 42901374 | 2026-10-20 | **T** | Thirteen adults whose sensing of carbon dioxide in the blood is abolished or nearly abolished, asked with a validated questionnaire whether their breathing feels unpleasant. A measured bodily feeling in conscious people missing a body-sensing channel. |
| 4 | 41823406 | 2026-10-01 | A | Review of predictive-coding accounts of functional neurological disorder. |
| 5 | 42361935 | 2026-06-26 | A | Systematic review of touch-based rehabilitation. |
| 6 | 42249914 | 2026-06-06 | B | New data in Parkinson's disease, measuring questionnaire scores for body awareness and mental body representation, not whether feelings are present or absent. |
| 7 | 42542835 | 2026-07-02 | A | Narrative review of a therapy technique. |
| 8 | 42525758 | 2026-07-29 | B | New intracranial recordings during breathing challenges; measures which cortical areas predict noticing a breathing disruption, not the presence of bodily feeling where body-sensing is abolished. |
| 9 | 41851618 | 2026-03-18 | B | Brain imaging in migraine; measures brain responses during an interoceptive task. |
| 10 | 41432193 | 2025-12-20 | A | Review of timing and self-disturbance in psychosis. |
| 11 | 42935715 | 2026-10-12 | B | New recordings offered in support of another theory of consciousness (Default Space Theory); measures synchrony between body and brain rhythms, not feelings abolished. |
| 12 | 42433211 | 2026-06-26 | A | A described psychotherapy model with a case illustration. |
| 13 | 42422542 | 2026-06-24 | A | A short perspective piece on breathlessness in rehabilitation. |
| 14 | 42246050 | 2026-05-20 | A | Protocol for a future diagnostic study. |
| 15 | 41464339 | 2025-12-12 | A | Systematic review of questionnaires. |
| 16 | 41422313 | 2025-12-21 | B | New data on body-signal processing in eating and weight disorders; measures accuracy and sensitivity, not abolished feelings with consciousness intact. |
| 17 | 41373279 | 2025-11-26 | A | Protocol for a rehabilitation trial. |
| 18 | 40460524 | 2025-06-02 | B | Brain imaging of self-disturbance in schizophrenia; no measure of bodily feeling being absent. |
| 19 | 39160454 | 2024-08-19 | B | Questionnaire study in insomnia; measures reported body sensitivity and reported quality of consciousness in people whose body-sensing is intact. |
| 20 | 40895030 | 2025-08-06 | A | Review of neurosurgical practice. |
| 21 | 39958752 | 2025-01-31 | B | Virtual-reality embodiment study; measures a sense of owning an avatar. |
| 22 | 39677366 | 2024-11-25 | B | Heartbeat-evoked responses during attention tasks in healthy people; a brain measure, nobody's feelings abolished. |
| 23 | 39665237 | 2024-12-12 | A | A framework paper on neuroethics. |
| 24 | 38788262 | 2024-05-17 | B | Survey in cardiovascular disease; measures reported body-listening and self-care behaviour. |
| 25 | 39120213 | 2024-07-30 | A | Narrative review for palliative care. |
| 26 | 38114633 | 2023-12-19 | A | Review proposing a three-dimensional model. |
| 27 | 39220208 | 2024-08-16 | A | A proposed prescribing approach with a review of evidence. |
| 28 | 39006064 | 2024-07-02 | B | Before-and-after study of breast surgery; measures questionnaire body awareness. |
| 29 | 37109233 | 2023-04-16 | B | Cohort study; measures whether low body awareness predicts later pain. |
| 30 | 37621971 | 2023-08-09 | A | A conceptual piece on intentionality. |
| 31 | 36360614 | 2022-10-22 | A | Systematic review and meta-analysis of a movement method. |
| 32 | 36099315 | 2022-09-13 | A | A formal model of cardiac inference; simulations, no new data about the world. |
| 33 | 35751711 | 2022-06-25 | B | Heartbeat-perception task in motor neurone disease; measures how accurately patients count heartbeats, not whether feelings are abolished. |
| 34 | 34668170 | 2021-10-19 | A | Review proposing a model of fatigue. |
| 35 | 35077847 | 2022-01-22 | B | Experiment showing body-signal feedback reduces pain; measures pain ratings in healthy people. |
| 36 | 36091366 | 2022-08-26 | B | Rehabilitation trial in fibromyalgia; measures clinical outcomes. |
| 37 | 33686522 | 2021-03-08 | A | Review of mapping the sense of self in surgery. |
| 38 | 34566738 | 2021-09-08 | A | Review of a mindfulness approach. |
| 39 | 34335449 | 2021-07-15 | B | Pilot study of vagus-nerve stimulation in disorders of consciousness; measures blood flow in the brain, and stimulates rather than abolishes body-sensing. |
| 40 | 32631425 | 2020-07-06 | B | Volume study of the insula in dementia with Lewy bodies; measures grey-matter volume. |

**Qualifying: 1 (row 3). Taken: row 3.**

## 2. `dam-subcortical` (basic feelings start in the brainstem and survive loss of the cortex)

Hits: 471. Screened: the first 40, in order. The search word "decortication" also means stripping
a membrane off a lung and stripping husks off grain, which is where most of this list comes from.

| # | id | date | call | why |
|---|---|---|---|---|
| 1 | 42118806 | 2026-05-14 | A | Three case descriptions of a gene mutation causing brain malformations; no measure of feeling. |
| 2 | 42846620 | 2026-09-07 | C | A case of a vein infection after influenza. |
| 3 | 41738435 | 2026-02-25 | B | New data: brain pathology in stillborn and newborn piglets, some with the cerebral mantle missing. It measures tissue damage in animals that were dead or died at birth, so there is no behaviour and no feeling to measure. |
| 4 | 41535039 | 2026-01-15 | A | A case of brainstem encephalitis; clinical description. |
| 5 | 42647317 | 2026-08-14 | C | A kidney case report. |
| 6 | 42402382 | 2026-07-03 | A | A case using blood-flow imaging in brainstem encephalitis. |
| 7 | 42429482 | 2026-07-01 | B | New data on blood-vessel development in the retina in a mouse model; nothing about feeling. |
| 8 | 42223893 | 2026-06-01 | C | Lung surgery for mesothelioma ("decortication" in the surgical sense). |
| 9 | 42191535 | 2026-05-26 | C | A lung transplant complication. |
| 10 | 42180437 | 2026-05-14 | C | Neck surgery and nerve ablation. |
| 11 | 41956352 | 2026-04-09 | B | New data: six newborn calves with the cerebral cortex largely lost after a virus, with the clinical signs described ("disorientation, absent reflexes, and poor suckling") and one examined after death. **Borderline:** it is the most recent report of living animals without a cortex. Not taken because the prediction's test asks for graded, flexible feeling-driven behaviour, such as a learned preference driven by the body's state, and a clinical note of poor suckling is not that; the calves were also euthanised, and the damage was not confined to the cortex. |
| 12 | 41827150 | 2026-02-25 | C | A lung infection case. |
| 13 | 40670102 | 2025-07-17 | C | Chest surgery series. |
| 14 | 42682943 | 2026-08-31 | C | A lung disease case in pregnancy. |
| 15 | 42116901 | 2026-04-24 | A | Two skull-surgery cases after combat injury. |
| 16 | 41399600 | 2025-11-12 | C | Review of a heart disease. |
| 17 | 40653787 | 2025-07-13 | A | Review of foetal brain injuries on ultrasound. |
| 18 | 41328078 | 2025-10-31 | C | A chest case report. |
| 19 | 41281040 | 2025-10-21 | C | Blood markers after lung surgery. |
| 20 | 41157629 | 2025-10-10 | B | New data: cattle abortions and malformations after a virus; pathology, no behaviour or feeling. |
| 21 | 40816661 | 2025-08-13 | A | Review of what suffices for consciousness, arguing for the cerebellum; no data of its own. |
| 22 | 41164037 | 2025-09-28 | C | An anaesthesia case report. |
| 23 | 40867688 | 2025-08-11 | B | New data: thirteen calves with cortical loss, examined clinically and by scan before being put down. **Borderline, same reason as row 11:** the examinations record signs of forebrain disease, not graded feeling-driven behaviour. |
| 24 | 40556403 | 2025-08-01 | C | Chest surgery imaging. |
| 25 | 40481842 | 2025-06-07 | C | Spine surgery experiments on cadaver bone. |
| 26 | 40707102 | 2024-08-29 | C | A chest surgery case. |
| 27 | 40242810 | 2025-03-14 | C | Spine surgery technique. |
| 28 | 40142754 | 2025-03-13 | C | Dentistry meta-analysis. |
| 29 | 40077482 | 2025-02-25 | C | Food science (grain husking). |
| 30 | 40969787 | 2025-09-03 | A | Three poisoning cases. |
| 31 | 40756302 | 2025-02-07 | C | Three thoracic surgery cases. |
| 32 | 39822587 | 2025-01-16 | B | New data on seizure networks in animals; measures connectivity, not feeling. |
| 33 | 39414989 | 2024-10-16 | A | A genetic case report of a prenatal syndrome. |
| 34 | 39306721 | 2024-09-19 | B | New data on a gene variant causing a developmental disorder; no measure of feeling. |
| 35 | 39791062 | 2024-12-10 | A | A newborn case report with literature review; describes the malformation, measures no feeling. |
| 36 | 39749076 | 2024-12-03 | C | A chest case report. |
| 37 | 39314658 | 2024-09-14 | C | A heart case report. |
| 38 | 39448711 | 2024-10-24 | C | Banana fibre materials science. |
| 39 | 39106006 | 2024-08-06 | B | New data: seventy-seven calves born with the cerebral mantle missing, their neurological signs sorted into common and uncommon ones (including unawareness of surroundings and failure to suckle). **Borderline, same reason as rows 11 and 23:** signs described by a clinician, not feeling measured. |
| 40 | 39398846 | 2024-09-11 | C | A kidney case report. |

**Qualifying: 0. Taken: none.** Three rows (11, 23, 39) are the near misses, and all three fail
on the same point: nobody measured whether an animal without a cortex feels hunger, thirst, pain
or pleasure in a graded, flexible way. This is the clearest gap the search found: the prediction
is testable in principle, and this search found no study that tests it.

## 3. `dam-insula` (feelings survive loss of both insulae)

Hits: 287. Screened: the first 40, in order.

| # | id | date | call | why |
|---|---|---|---|---|
| 1 | 42700908 | 2026-09-06 | A | A perspective piece on empathy and memory. |
| 2 | 42939345 | 2026-10-10 | A | Review of smell loss after stroke. |
| 3 | 42767166 | 2026-09-01 | B | New lesion mapping of impaired emotional speech tone; measures how people speak, not how they feel. |
| 4 | 42762287 | 2026-09-19 | A | Review and hypothesis on multiple sclerosis. |
| 5 | 42621758 | 2026-08-20 | B | New data on recognising emotions in faces in multiple sclerosis; recognising others' emotions is not feeling one's own, and the lesions are not loss of both insulae. |
| 6 | 42525758 | 2026-07-29 | B | New intracranial recordings of breathing awareness; measures the timing of signals through an intact insula, not life after losing both. |
| 7 | 42393674 | 2026-07-02 | B | New lesion-network mapping of bodily symptoms; measures which networks the lesions touch, in people with varied single lesions. |
| 8 | 42087845 | 2026-05-01 | A | Review of the insula in heart disease. |
| 9 | 41610599 | 2026-01-17 | B | New data in mice: an insula-to-habenula circuit in itch and low mood, manipulated chemically. It measures itch-scratching and anxiety-like behaviour with the insula interfered with on both sides, which is close, but the manipulation is a reversible circuit silencing aimed at one pathway, not loss of both insulae, and the measure is anxiety-like behaviour rather than the range of feelings. |
| 10 | 41549955 | 2026-04-01 | B | Brain imaging and questionnaires in leprosy; no insular loss. |
| 11 | 41547471 | 2026-01-15 | A | Scoping review of body sensing after stroke. |
| 12 | 42780841 | 2026-09-09 | A | Narrative review of dizziness. |
| 13 | 42376131 | 2026-06-15 | A | Review of stress and functional neurological disorder. |
| 14 | 42079832 | 2026-04-17 | B | New recordings in people with insular tumours; measures brain network indices and anxiety and depression scores. A tumour in one insula is not loss of both. |
| 15 | 42051540 | 2026-04-13 | A | Systematic review of post-exertional malaise. |
| 16 | 41630843 | 2026-01-29 | A | Review of sensory loss and mood after stroke. |
| 17 | 41527564 | 2026-01-08 | A | Systematic review of emotional intelligence. |
| 18 | 41313951 | 2025-11-20 | A | A case of music and sound intolerance after removing part of one side; one side only, and the measures are musical perception. |
| 19 | 41072268 | 2025-10-01 | A | Systematic review of imaging in skin-picking disorder. |
| 20 | 41187327 | 2025-11-04 | A | Protocol for a neurofeedback trial. |
| 21 | 40930338 | 2025-09-08 | A | Scoping review of the insula in a heart condition. |
| 22 | 41117366 | 2025-10-21 | B | New data on brain volume after a depression treatment; no insular loss. |
| 23 | 41009323 | 2025-09-22 | B | New data on emotion regulation and memory in healthy people. |
| 24 | 40373909 | 2025-05-13 | B | New data in epileptic rats on a receptor in the insula; measures synaptic changes, not feelings. |
| 25 | 40275827 | 2025-04-25 | A | Systematic review of body sensing after frontal injury. |
| 26 | 40585817 | 2025-06-04 | B | New data on feeling a body part is not one's own after stroke; measures ownership of a limb, not the range of feelings, and no bilateral insular loss. |
| 27 | 40318503 | 2025-04-27 | B | New imaging in functional neurological disorder; measures white matter. |
| 28 | 39316247 | 2024-09-24 | A | Review of the insula and heart control. |
| 29 | 39516519 | 2024-11-08 | B | New data linking right-hemisphere stroke to social connectedness; measures social outcomes. |
| 30 | 39005040 | 2024-07-15 | B | New data: people with focal brain damage, including right insula, doing a breathing-regulation task with feelings rated by questionnaire. **Borderline:** it does measure feelings (anxiety and bodily states) in people with insular damage, and it is in the same journal issue as a Damasio statement. Not taken because the damage is to one side and to several different regions, where the prediction names complete loss of both insulae. |
| 31 | 38838083 | 2024-06-04 | **T** | New data: rats with both insulae destroyed, tested on whether they learn to avoid the taste and the place that alcohol made them feel bad in. Both insulae gone, and the measure stands in for how bad the body felt. |
| 32 | 38705507 | 2024-05-04 | B | New brain-structure data in skin-picking disorder. |
| 33 | 38552812 | 2024-03-27 | A | Review of emotional processing after insular stroke; gathers other studies' results. |
| 34 | 38770492 | 2024-04-18 | A | Integrative review of the insula in chronic pain. |
| 35 | 40800324 | 2024-05-09 | B | New data on connectivity and giving up smoking in older people. |
| 36 | 39018294 | 2024-07-17 | B | New imaging in people with insular damage looking at emotional faces; measures brain responses to others' faces, and the damage is one-sided. |
| 37 | 38428325 | 2024-02-27 | B | New data on facial emotion processing after stroke with depression. |
| 38 | 38422831 | 2024-02-28 | B | New resting-state imaging in functional neurological disorder. |
| 39 | 37619765 | 2023-08-22 | B | New data: electrical stimulation of one insula in rats with nerve pain; measures pain behaviour under stimulation, not loss of both insulae. |
| 40 | 37930733 | 2023-12-04 | B | New imaging in moyamoya disease. |

**Qualifying: 1 (row 31). Taken: row 31.**

## 4. `dam-nonneural` (consciousness comes from nerves and body together, not nerves alone)

Hits: 666. Screened: the first 40, in order.

| # | id | date | call | why |
|---|---|---|---|---|
| 1 | 42685938 | 2026-09-02 | B | New data: a plant compound, bile acids and anxious behaviour in mice. It touches the blood-brain barrier but blocks nothing at a barrier-free body-sensing site and measures anxious behaviour. |
| 2 | 43011228 | 2026-11-10 | A | Review of appetite drugs. |
| 3 | 42929410 | 2027-01-01 | C | Plant pharmacology in isolated gut tissue. |
| 4 | 42828728 | 2026-10-03 | A | Review of gut bacteria and cognition. |
| 5 | 42790664 | 2026-09-25 | B | New data on blood-derived particles and behaviour in addicted mice; no blocking of the body-to-nerve exchange. |
| 6 | 41715909 | 2026-02-19 | B | New data on the barrier forming in unborn mice after maternal stress; measures barrier development and later behaviour, not feelings of the body's state. |
| 7 | 43002616 | 2026-11-09 | A | A case of nausea and vomiting from an autoimmune disease. |
| 8 | 42969617 | 2026-11-02 | A | Review of exercise for chronic pain. |
| 9 | 42742987 | 2026-09-15 (preprint 2025-01-24) | **T** | New data in mice: the receptor for a circulating drug taken away from, or restored in, two neighbouring body-sensing brainstem patches, one standing in a gap in the blood-brain barrier and one behind it, with the sickly avoidance state measured. This is the prediction's test in all but name. |
| 10 | 42668022 | 2026-08-29 | A | Review of a hormone system in brain disease. |
| 11 | 42665122 | 2026-09-01 | A | Review of immune cells in depression after stroke. |
| 12 | 42265941 | 2026-06-09 | A | A case of a brainstem syndrome in a genetic disease. |
| 13 | 42875549 | 2026-10-15 | A | Review of drug carriers in psychiatry. |
| 14 | 42481362 | 2026-07-21 | A | Clinical guidelines. |
| 15 | 42435826 | 2026-07-11 | A | Review of dopamine given through the nose. |
| 16 | 42883907 | 2026-09-28 | A | Review of a brainstem syndrome across three diseases. |
| 17 | 42728876 | 2026-09-01 | A | Review of a schizophrenia medicine. |
| 18 | 42442453 | 2026-07-13 | A | Review of nanomedicine in Huntington's disease. |
| 19 | 41495612 | 2025-12-31 | A | Review of the nose-to-brain route. |
| 20 | 42648453 | 2026-08-26 | B | New data on gut bacteria, inflammation and mood in mice and people; measures mood-related behaviour, blocks no body-to-nerve exchange. |
| 21 | 42603218 | 2026-08-15 | A | Review of hiccups as a brainstem sign. |
| 22 | 42532542 | 2026-08-01 | A | Review of oral disease and mental health. |
| 23 | 41895669 | 2026-03-25 | B | New data on a signalling molecule, the barrier and thinking in mice with skin disease; measures memory and barrier leakage. |
| 24 | 42871863 | 2026-07-01 | A | Review of side effects of appetite drugs. |
| 25 | 42533037 | 2026-07-30 | B | New data on a protein in the hippocampus and mood in mice after ovary removal. |
| 26 | 42527715 | 2026-07-30 | A | A case report. |
| 27 | 42517391 | 2026-07-24 | A | Review of ultrasound stimulation. |
| 28 | 42450248 | 2026-07-03 | A | Review of fat signalling in depression. |
| 29 | 42434537 | 2026-07-10 | A | A case report of a brainstem syndrome. |
| 30 | 42411221 | 2026-07-06 | A | Review of plant nanomedicine in Alzheimer's disease. |
| 31 | 42184678 | 2026-05-25 | A | Review of gene regulation after stroke. |
| 32 | 42352912 | 2026-06-08 | A | A proposed model of autism. |
| 33 | 42321914 | 2026-06-19 | A | Review of lung injury and brain development. |
| 34 | 42025017 | 2026-04-20 | B | New data in mice: nausea-like behaviour after a chemotherapy drug, with activity marked in the barrier-free brainstem patch. **Borderline:** it measures a bodily feeling by its behavioural stand-in, and it involves the right place. Not taken because it manipulates a receptor for a signal passed between nerve cells and never blocks the exchange between body-sensing nerves and the blood or tissue around them, which is what the prediction's test names. |
| 35 | 42214740 | 2026-05-28 | A | Review of focused ultrasound in addiction. |
| 36 | 42199116 | 2026-05-14 | A | Review of bone-to-brain signalling. |
| 37 | 42152094 | 2026-05-18 | B | New data in mice: airway inflammation reaching a barrier-free body-sensing brain organ, and a circuit from it silenced. Measures learning to stop being afraid, not a feeling of the body's state, so it misses the test's wording. |
| 38 | 41690434 | 2026-02-12 | A | Review of oxytocin in dogs. |
| 39 | 42111451 | 2026-04-23 | A | Review of mild head injury. |
| 40 | 42076023 | 2026-04-19 | A | Systematic review of cell-junction proteins. |

**Qualifying: 1 (row 9). Taken: row 9**, dated by its earliest public appearance, the preprint of
2025-01-24, not by the journal version of 2026-09-15.

## 5. `dam-nss` (body-sensing nerve fibres also signal outside synapses)

Hits: 72. Screened: the first 40, in order. This list runs back to 1995, because the search terms
are narrow.

| # | id | date | call | why |
|---|---|---|---|---|
| 1 | 43052716 | 2026-08-25 | A | Systematic review of mathematical models. |
| 2 | 42846523 | 2026-09-23 | A | A hypothesis piece about a cough reflex; acoustic reasoning, no new data. |
| 3 | 41594782 | 2025-12-31 | A | A review of a brainstem nucleus which ends by suggesting non-synaptic signalling; no new data. |
| 4 | 41229287 | 2025-11-13 | A | The proponents' own statement of the theory (Singer and Damasio), already a source in these records; a review, not a study. |
| 5 | 39623218 | 2024-12-02 | B | New data on the shape and function of thin brain axons; the axons are not body-sensing fibres and the measure is membrane mechanics. |
| 6 | 35892199 | 2022-07-27 | A | Review of neuropeptides in fly behaviour. |
| 7 | 35131465 | 2022-02-04 | B | New data on mitochondria spacing in axons. |
| 8 | 33722070 | 2021-03-15 | A | Review of glial function and myelin. |
| 9 | 32173398 | 2020-03-12 | B | New data on inhibition of body-sensing C-fibre inputs in the spinal cord; the mechanism measured is synaptic (a transmitter at a synapse), which is the opposite of what the prediction names. |
| 10 | 32269519 | 2020-03-25 | A | A simulation method paper. |
| 11 | 31689490 | 2019-11-02 (preprint 2019-07-14) | **T** | New data in rats: signalling between neighbouring body-sensing nerve cell bodies outside synapses, in the ganglion beside the spinal cord and in the vagus nerve's own ganglion, with one receptor blocked to change it. Antonio Damasio is an author. |
| 12 | 29472865 | 2018-02-08 | B | New data on skull pressure and nerve activity; asks whether a brainstem response is non-synaptic, but measures sympathetic nerve traffic, not signalling between body-sensing fibres. |
| 13 | 29201256 | 2017-03-15 | A | Review of signalling in a face-sensing ganglion. |
| 14 | 25871969 | 2015-06-01 | B | New data in guinea pigs on recovery from facial paralysis; measures facial movement. |
| 15 | 25194917 | 2014-09-07 | B | New anatomy of wake-promoting axons; counts synaptic contacts in a reward area. |
| 16 | 21036204 | 2010-10-29 | B | New anatomy of the same system in the frontal cortex. |
| 17 | 20937358 | 2010-10-16 | B | New data in living animals: non-synaptic activation of body-sensing nerve cell bodies beside the spinal cord. **Borderline:** it is the same kind of result as the taken study, in the same place, but it measures calcium rising when a chemical is dropped on the cells, not signalling passing from one fibre to its neighbour, and nothing is blocked to show the signal's route. Older than the taken study in any case. |
| 18 | 20923934 | 2010-10-05 | B | New data on non-synaptic release of a chemical from axons; the axons are in the optic nerve, not body-sensing. |
| 19 | 18842957 | 2008-10-08 | B | New data in smell-sensing neurons; smell is an outward sense. |
| 20 | 14528450 | 2003-11-01 | B | New data on interactions between smell-nerve axons, including field effects; again an outward sense. |
| 21 | 12834879 | 2003-07-01 | B | New anatomy of opioid terminals in a face-sensing region. |
| 22 | 11994125 | 2002-04-01 | B | New anatomy: evidence of non-synaptic supply to spinal cord cells by body-sensing fibres, measured as where receptors and terminals sit. Anatomy, not signalling measured passing between fibres. |
| 23 | 11588203 | 2001-10-01 | B | The first demonstration of field coupling between axons, in the smell system; an outward sense. |
| 24 | 11298363 | 2001-05-01 | B | New anatomy of serotonin receptors in a reward area. |
| 25 | 11898511 | 2001-03-01 | A | Review of electrical fields against seizures. |
| 26 | 11084206 | 2000-11-01 | A | A calculation of the energy cost of nerve signals. |
| 27 | 10660896 | 2000-02-01 | B | New anatomy of serotonin receptors in the brain. |
| 28 | 10550500 | 1999-11-01 | A | Review of spinal inhibition. |
| 29 | 10400892 | 1999-08-01 | B | New anatomy of opioid receptors in a brainstem body-sensing nucleus; receptor locations, not signalling between fibres. |
| 30 | 10188938 | 1999-04-01 | B | New anatomy of a glutamate receptor in a movement area. |
| 31 | 10819088 | 1999-01-01 | A | Review of nerve pain mechanisms. |
| 32 | 10336064 | 1999-01-01 | B | New anatomy of receptors on vagal body-sensing fibres and their targets; locations, not non-synaptic signalling measured. |
| 33 | 9845242 | 1998-12-01 | B | New anatomy of a receptor in the vagal brainstem complex. |
| 34 | 9622618 | 1998-06-01 | B | New anatomy of receptors in a brainstem arousal nucleus. |
| 35 | 9456175 | 1998-01-01 | B | New anatomy of dopamine fibres in human brain tissue after death. |
| 36 | 9406957 | 1997-10-01 | B | New anatomy of a receptor in the spinal cord. |
| 37 | 9018705 | 1997-01-01 | A | Review of a surgical treatment for face pain. |
| 38 | 8896842 | 1996-09-01 | B | New anatomy of a receptor in the vagal brainstem complex. |
| 39 | 7751438 | 1995-03-01 | B | New anatomy of synaptic input to vagal motor neurons; synaptic, and motor rather than body-sensing. |
| 40 | 7715786 | 1995-02-01 | B | New anatomy of body-sensing fibres at the carotid body, read as chemical transmission through the space around them. **Borderline:** it is non-synaptic signalling at a body-sensing nerve ending, inferred from electron microscopy rather than measured as a signal, and it is the oldest result in the list. |

**Qualifying: 1 (row 11). Taken: row 11**, dated by its preprint of 2019-07-14. It could not be
opened (see `verify.toml`), so it carries no judgement; the note on its record says that the
dating rules would read it as "not before" in any case, because the prediction was first stated in
November 2025 and this is the proponents' own lab.

## 6. `dam-no-nervous-system` (bacteria and plants are not conscious)

Hits: 216. Screened: the first 40, in order. The prediction's own test wording is "None stated":
the proponents name no observation that would show a bacterium or a plant has or lacks experience.
Under the method, no study can measure what the test names, so nothing here can qualify. The
search was run and screened anyway, as the method says, so that the record shows it.

| # | id | date | call | why |
|---|---|---|---|---|
| 1 | 41660784 | 2026-02-09 | B | New data: wheat seedlings exposed to a proposed "consciousness field"; measures germination, growth and plant chemistry, which no stated test of this prediction names. |
| 2 | 43051078 | 2026-11-17 | C | Herbicides and soil microbes. |
| 3 | 43030898 | 2026-11-09 | A | Review of pressure inside the kidney. |
| 4 | 42537960 | 2026-07-31 | A | Review of treatments for a stomach bacterium. |
| 5 | 42430044 | 2026-07-10 | B | New data: cattle poisoned by a shrub; brain pathology. |
| 6 | 42342995 | 2026-06-24 | A | Historical and philosophical remarks on plant cognition. |
| 7 | 42169462 | 2026-05-01 | C | Wastewater engineering. |
| 8 | 42115900 | 2026-05-11 | C | Chemistry of a metal complex. |
| 9 | 42064443 | 2026-03-31 | C | Bacteria used to grow lettuce. |
| 10 | 41892767 | 2026-03-11 | C | Comparing disinfectants. |
| 11 | 41865106 | 2026-03-21 | C | Machine learning for machine maintenance. |
| 12 | 41745536 | 2026-02-02 | A | Review of desert plant compounds for skin printing. |
| 13 | 42996437 | 2026-10-23 | C | Software for spotting tomato leaf disease. |
| 14 | 41484359 | 2026-01-03 | C | Oil recovery chemistry. |
| 15 | 41211987 | 2025-11-10 | C | Bacterial genetics method. |
| 16 | 41283473 | 2025-11-04 | B | New data: infection and inflammation in injured pigs; the word "conscious" is about the animals being awake. |
| 17 | 40908257 | 2025-09-04 | B | New data on human standing balance. |
| 18 | 40741096 | 2025-07-30 | C | Composting and maize seedlings. |
| 19 | 39841540 | 2025-05-12 | C | An underwater robot. |
| 20 | 40647901 | 2025-06-20 | C | Plant oils against nematodes. |
| 21 | 40552339 | 2025-06-23 | C | Yoghurt making. |
| 22 | 40534723 | 2025-04-11 | C | Consumer survey about potatoes. |
| 23 | 40360734 | 2025-05-13 | C | Farm sensing software. |
| 24 | 40308652 | 2025-04-14 | C | Printing buildings from soil and seeds. |
| 25 | 39837417 | 2025-01-19 | C | Canteen food choices. |
| 26 | 39276228 | 2024-09-14 | A | Historical criticism of plant-intelligence claims. |
| 27 | 40051517 | 2025-02-11 | C | Survey about phage therapy. |
| 28 | 39118391 | 2024-08-08 | C | Pesticide dealers' views. |
| 29 | 39082745 | 2024-11-01 | A | Review of chia seeds. |
| 30 | 38969119 | 2024-07-03 | C | Antibiotic resistance genes in soil. |
| 31 | 39063353 | 2024-07-18 | C | Food labelling and consumer choice. |
| 32 | 38984341 | 2024-06-19 | B | New data: a herbal medicine in epilepsy; "consciousness" here means seizures. |
| 33 | 38611412 | 2024-04-04 | C | Winemaking. |
| 34 | 38481545 | 2023-10-31 | C | Plant extract pharmacology. |
| 35 | 38062788 | 2023-12-08 | C | Covers for plaster casts. |
| 36 | 38317894 | 2024-01-16 | C | Drug measurement chemistry. |
| 37 | 39575104 | 2024-11-07 | C | Diet survey. |
| 38 | 39109343 | 2024-07-23 | C | Dog gum disease markers. |
| 39 | 38510423 | 2024-03-15 | C | Badger welfare during blood sampling. |
| 40 | 38162248 | 2023-09-01 | C | Contamination of anaesthetic vials. |

**Qualifying: 0. Taken: none.**

## 7. `dam-ai` (present-day artificial intelligence lacks what grounds feelings)

Hits: 28, so all 28 were screened. Like the prediction above, its test wording is "None stated",
so nothing can qualify under the method.

| # | id | date | call | why |
|---|---|---|---|---|
| 1 | 43027110 | 2026-10-26 | A | Structured review of evidence for animal suffering. |
| 2 | 42658654 | 2026-08-27 | A | Review of the body's role in human thought. |
| 3 | 42750541 | 2026-09-17 | A | A commentary arguing against Seth; no data. |
| 4 | 41500378 | 2026-01-05 | A | A theory piece ("life is a collection of programs"). |
| 5 | 42876598 | 2026-09-30 | A | A proposed framework for machine consciousness; no data. |
| 6 | 41516001 | 2025-12-22 | A | Review of modelling and regeneration. |
| 7 | 40150717 | 2025-03-03 | B | New data: a learning aid for deafblind children; nothing about feelings in machines. |
| 8 | 40910115 | 2025-08-20 (preprint 2024-11-25) | B | New data on an artificial agent, explicitly framed around Damasio's theory. Already in the records as `immertreu-2025` with `bears_on = []`: it probes whether a classifier can read the agent's own position from its activity, which no stated test of `dam-ai` names, and the agent has no body-sensing or feelings. |
| 9 | 39220208 | 2024-08-16 | A | A proposed prescribing approach. |
| 10 | 38618488 | 2024-04-13 | B | New data: what ordinary people believe about language models having feelings. It measures beliefs about machines, not the machines. |
| 11 | 37524933 | 2023-07-31 | A | Review of machine learning datasets. |
| 12 | 37799520 | 2023-09-20 | B | New data on detecting emotion in text by machine; detecting human emotion, not having feelings. |
| 13 | 35150452 | 2022-02-12 | B | New data on breathing and voice recognition in people, using a robot; about people, not machines. |
| 14 | 34672015 | 2021-10-20 | A | A discussion of care robots in nursing homes. |
| 15 | 34202965 | 2021-06-20 | A | A theory piece on embodied self-models. |
| 16 | 33458614 | 2020-12-16 | B | New data: thoughts feeling foreign in healthy people under robot-induced sensorimotor conflict; about people. |
| 17 | 33148398 | 2020-10-23 | A | Review of artificial intelligence in medicine. |
| 18 | 29892405 | 2018-05-09 | B | New data on owning a robotic arm; about people. |
| 19 | 33500893 | 2018-02-07 | B | New data: a robot architecture built on Damasio's account of emotions. It reports the system working, with no measure of feelings present or absent, and the prediction names no observation. |
| 20 | 30618706 | 2018-12-11 | A | A requirements paper on touch in assistive robots. |
| 21 | 28360849 | 2017-03-16 | A | A position piece on embodied medicine. |
| 22 | 25965942 | 2015-05-16 | B | New data on the feeling of control over one's own action; about people. |
| 23 | 24924875 | 2014-06-09 | B | New data on a method for inducing body ownership; about people. |
| 24 | 24878453 | 2014-02-13 | B | New data on body image after thyroid surgery; a robot performed the surgery. |
| 25 | 23423672 | 2013-02-18 | B | New data on out-of-body experiences after brain damage; about people. |
| 26 | 21521620 | 2011-04-01 | B | New data on where people feel themselves to be; about people. |
| 27 | 18930641 | 2008-10-18 | A | A commentary on feeling and the Turing test. |
| 28 | 18592055 | 2008-03-01 | A | An essay on a film. |

**Qualifying: 0. Taken: none.**

## The choice, and the one-per-prediction cap

Qualifying studies in all: four, across seven predictions. The method takes the five most recent
qualifying studies by earliest public appearance, at most one per prediction. Four qualified, so
four were taken, and the five-place limit never bit:

| study | prediction | earliest public appearance |
|---|---|---|
| `bret-2026` (carbon dioxide sensing abolished, breathing still felt unpleasant) | `dam-feeling-required` | 2026-10-20 |
| `yacawych-2026` (one receptor in two brainstem patches, one in a gap in the blood-brain barrier) | `dam-nonneural` | 2025-01-24 (preprint) |
| `mukherjee-2024` (both insulae destroyed in rats, alcohol avoidance learning) | `dam-insula` | 2024-06-04 |
| `carvalho-2019` (signalling between body-sensing nerve cell bodies outside synapses) | `dam-nss` | 2019-07-14 (preprint) |

**How the cap was applied: it never bound.** No study qualified for two of this theory's
predictions, and no prediction had two qualifying studies, so each taken study came from a
different prediction and the cap changed nothing. Had the three borderline rows in the
brainstem-and-cortex list (rows 11, 23 and 39 of search 2) been read as qualifying, the most
recent of them (2026-04-09) would have taken a fifth place, and nothing already taken would have
been displaced.

## Judgements made, and the unsure ones

Two of the four chosen studies could be opened, so two study-and-prediction pairs carry
judgements: four judgements in all (two about dating, two about the result). The two that could
not be opened carry none, as the brief directs.

| judgement | verdict | unsure? |
|---|---|---|
| `com-mukherjee-2024-dam-insula` (dating) | before | no |
| `out-mukherjee-2024-dam-insula` (result) | mixed, leaning against | yes |
| `com-yacawych-2026-dam-nonneural` (dating) | before | yes |
| `out-yacawych-2026-dam-nonneural` (result) | for | yes |

The three unsure readings, in short:

- **The insula result is the shakiest thing in this batch.** Rats with both insulae destroyed did
  not learn to avoid the taste and the place that alcohol had made them feel bad in, which points
  against the prediction that feelings survive. But learning is not a report of feeling, the same
  lesion also removed the rats' ordinary wariness of a new flavour, and the prediction is written
  about what a person says and what observers see. A reader could read "against", and a stricter
  reader could say rat learning cannot touch a prediction about human self-report at all.
- **The dating of the brainstem-patch study** rests on the proponents' 2022 wording ("not on an
  isolated nervous system"), which is two and a half years earlier than the study's preprint but
  looser. Their firmer 2024 wording is only six months earlier, and the study gives no date for
  its experiments, so the data were probably in hand before it. A reader who requires the firmer
  wording would say the dating is unclear, and then nothing counts.
- **The brainstem-patch result** is read as for the prediction, but the circulating molecule is a
  medicine rather than one of the body's own signals, the feeling is read from mice refusing a
  flavour, and the two patches differ in more than the barrier between them.

## Not opened

- `bret-2026`: Chest needs an Elsevier subscription; no open copy anywhere, and no preprint. Only
  the abstract was read. John would need an Elsevier (ScienceDirect) sign-in, or an author copy.
  Verify entry `v-dam-bret-2026-fulltext`.
- `carvalho-2019`: the journal version needs an Elsevier subscription, and the free bioRxiv copy
  answered a plain fetch with a robot block. No sign-in should be needed: the bioRxiv page is
  free, and John opening it himself (as he did for the 2023 core-claims paper) would clear it.
  Verify entry `v-dam-carvalho-2019-fulltext`.

## Where a rule gave a result John may not have intended (applied as written)

1. **Two predictions cannot be touched by any search, by construction.** `dam-no-nervous-system`
   and `dam-ai` have "None stated" as their test wording, because the proponents name no
   observation. The method requires a study to measure what the test names, so these two searches
   could only ever return nothing: 244 results screened, none able to qualify. The record now
   shows it, which was the point of searching them, but it is work that could not have gone
   otherwise.
2. **The theory's most testable prediction has no study at all.** Feelings surviving the loss of
   the cortex is the prediction most open to a test, and 40 screened results gave nothing: the
   cases of animals and newborns without a cortex are reported as pathology or as clinical signs,
   and nobody measures whether such an animal feels hunger or pain in a graded, flexible way. So
   the theory's best test is untested, not failed.
3. **A search built from a prediction's wording finds other fields' words.** "Decortication" is
   lung surgery and grain husking; the plants-and-bacteria search returned winemaking and
   wastewater treatment. Of the 268 results screened across those two searches, most were off the
   subject altogether. This is the cost of fixing queries before seeing results, and it is worth
   knowing that the cost is this high.
4. **The best-matching study is about a medicine, not about a body.** The brainstem-patch study
   fits the prediction's test wording closely, but it was done to find out whether appetite drugs
   can be made to work without making people feel sick. Counting it gives the theory a point from
   a study with no interest in the theory. That is what the method asks for, and the outcome
   judgement says plainly how loose the fit is.
5. **One taken study is the proponents' own, from six years before the prediction.** The
   non-synaptic signalling study has Antonio Damasio as an author and appeared in 2019; the
   prediction it bears on was first stated in November 2025. The own-lab dating rule puts it at
   "not before", so taking it adds a study to the record that cannot count. It is recorded anyway,
   with the reason on its record, because the method takes the most recent qualifying study per
   prediction and does not let the dating rule pre-empt the choice.
