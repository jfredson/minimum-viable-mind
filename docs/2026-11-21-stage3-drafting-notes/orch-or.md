# Orch OR drafts: notes (2026-11-21, first reader Claude)

Theory id `orch-or`, prefix `orch-`. Files: `sources.toml`, `theory.toml`, `predictions.toml`,
`studies.toml`, `judgements.toml`, `verify.toml`. All six parse with `tomllib`. Every quotation
in the claims, predictions and judgements was checked by script against the text that was
opened (one OCR line break rejoined by hand, in the 1998 prediction (1)).

## The core-claim source, and how it was opened

Hameroff and Penrose, "Consciousness in the universe: a review of the 'Orch OR' theory",
*Physics of Life Reviews* 11:39-78 (online 2013-08-20; issue March 2014). The publisher's copy is
open access (CC BY-NC-ND 4.0 per Crossref and Unpaywall), but ScienceDirect answered every
automated request with 403, in the built-in browser too, and the Open Philanthropy copy did the
same. Nothing was bypassed. The full typeset PDF was read from a third-party upload
(coroflot.com) found by web search. Because that copy is not the publisher's, every quotation is
on the verify list (v-orch-2014-copy): John can check them on the publisher's page in a normal
browser.

## How the core claims were chosen (repeatable)

The abstract states the theory in one sentence that begins "We proposed in the mid 1990's
that ...", followed by one sentence saying what the process produces. Claims 1 to 4 are that
sentence's clauses, split where it splits, plus the next sentence:
1. experience depends on organised quantum processes in microtubules in neurons;
2. those processes track and steer neurons' synaptic and membrane activity;
3. each ends by the Diósi-Penrose objective reduction;
4. each such event is a moment of awareness or choice.

Claims 5 and 6 are the two further things the paper itself says are part of the theory: the
isolation requirement, "essential for Orch OR" (section 4.5), and the anaesthetic mechanism, listed
in the Conclusion among developments "we have now incorporated into the theory". Other items in
that list (dipoles rather than shape changes, magnetic rather than electric dipoles, the
"Bandyopadhyay coherence" evidence, beat frequencies as the source of EEG) were left out. They
are about mechanism or evidence, not about what makes a system conscious. Six claims in all.

## Predictions

Eight, all stated by the proponents, one or two per claim. Seven come from Hameroff's 1998 list
of twenty (*Phil Trans R Soc A* 356:1869-1896, Appendix B), which the 2014 review repeats with
status comments; the 1998 statement is the earliest opened for each. The anaesthesia prediction
dates from the 2014 review (online 2013-08-20): the 1998 paper puts anaesthetic action in
"hydrophobic pockets of neural proteins", not in microtubules.

Oddities found on the way:
- The 2014 review says the twenty predictions were "published [15]" in 1998, but its reference
  [15] is Hameroff 2007. The 1998 list is in its reference [14]. This does not change any date.
- The 2014 review sets aside three 1998 predictions about a shielding gel of actin (11 to 13) as
  "perhaps a moot point, now". They were not recorded as separate predictions. That is a
  withdrawal, not a recorded failure, and is noted on `orch-coherence-time`.
- The proponents rate their own prediction 17 (more brain tissue, faster perception) as "not
  very clear", and give no way to measure the tissue involved.
- Not recorded: the 1998 predictions about Alzheimer's drugs, psychoactive drugs in general, A-lattice
  microtubules, coherent photons, gap junctions, the retina and Cambrian fossils. Each is either
  not about what makes a system conscious or is covered by a recorded one. Claim-tied coverage was
  the aim, not the full list.

## Rival separation (ruling C): no prediction separates

Rival texts searched for "quantum", "microtubul" and "anesthe"/"anaesthe":
- IIT: Albantakis 2023 (`albantakis-2023`; "quantum" only in the reference list) and Tononi and Koch 2015 (`tononi-koch-2015`, full text).
- GWT: Baars and Edelman 2012 (abstract only).
- Damasio: Singer and Damasio 2025 (`singer-damasio-2025`; no hits).
- Mashour 2020 and Lamme 2018: their Europe PMC full-text calls returned an error this time, so
  they were not re-searched. The pilot read both in full.

The nearest passages are these. Tononi and Koch: "IIT is compatible with quantum mechanics ...
at the quantum level Φ values may be very small". Baars and Edelman: quantum proposals have not
yet met the burden of proof. Neither predicts a different result on any recorded test. The
Khan study's authors sum up the workspace and integrated information theories as "do not at
present predict specific molecular targets of anesthetics", which is silence. **So every
testability judgement reads `separates = false`.** Under the ruled scoring, Orch OR's
testability score is 0, no core claim counts toward the bar, and the theory lands in "not yet
defined sharply enough to rank".

**A rule result John may not have intended.** Orch OR is perhaps the most openly falsifiable
theory on the list. Its proponents published twenty predictions in 1998. It scores zero here
because rival theories never mention microtubules or quantum collapse. Ruling C was made to stop
a reader inventing rivals' predictions. Here its effect is that a theory testing a level its
rivals ignore can never separate, however sharply it is put. The rule has been applied as written.
A possible fix, for John only: a separation could also be sourced to a mainstream statement that
a classical, neuron-level account predicts no effect. That would need a ruling.

The second question for John is whether Bernard Baars counts as a global workspace proponent. He
first proposed the theory but is not on the pilot's list. His 2012 abstract would not change
any judgement here (v-orch-baars-2012).

## Study search, screen list and counts

Query, exactly as briefed, run 2026-11-21 against the Europe PMC REST search, `sort=P_PDATE_D
desc`, `resultType=core`: 125 hits. Screened in the order returned (Europe PMC's newest-first
order is not strictly by first publication date; item 7 is dated 2026-10-09). **Only four of the
first 80 qualify, fewer than five, so the screen stopped at 80 as the method says.**

A quirk worth knowing: `TITLE_ABS:"Orch OR"` also matches "orchiectomy", "orchidectomized",
"orchardgrass", "Orchidaceae" and the like. Roughly a third of the hits are animal-hormone or
plant papers.

Taken (T) or skipped, with the reason:
1. 42537979 Roeloffs, Tuszynski 2026, quantum effects at subneuronal scales: skip, a hypothesis paper built from published data
2. 42501780 Choi 2026, quantum circuit model: skip, model
3. 42450355 Neuronal microtubules and radiofrequency waves: skip, review
4. 41713567 Choi 2026, surface code feasibility: skip, model
5. **T** 41519196 Huang ... Wiest 2026, epothilone B and isoflurane in mice (`huang-2026`; not opened, abstract only)
6. 41637896 Phenomenal binding problem for neural networks: skip, review
7. 42920515 Echternach 2026, "dimensional convergence": skip, a synthesis of others' experiments
8. 42643630 Cheung 2026, XXZ spin chains: skip, toy model
9. 42585374 Sex hormones and pain in old rats: skip, off topic ("Orch" for orchiectomized)
10. 42253571 Theory of psychic quanta: skip, theory
11. 42137636 Roeloffs, Tuszynski 2026, self-referential processing: skip, theory
12. 41704543 ORCH multi-agent orchestrator: skip, off topic
13. 40999612 Unified model of consciousness: skip, editorial
14. 41630764 Orchiectomy in cats: skip, off topic
15. 40563901 Hormone therapy and bone in rats: skip, off topic
16. 39978568 An, Choi 2025, surface code: skip, model
17. **T** 40021968 Li ... Martyn 2025, microtubule drugs and isoflurane in mice (`li-2025`)
18. 41141302 Corrigendum: skip
19. 41036467 Conscious active inference I: skip, review
20. 41019231 Conscious active inference II: skip, review
21. 40977855 Quantum-classical complexity and Orch OR: skip, discussion piece (no abstract)
22. 40342554 Wiest 2025: skip, a review ("Recent experimental evidence, briefly reviewed here")
23. 39122150 Dairy cow digestibility: skip, off topic
24. **T** 39147581 Khan ... Wiest 2024, epothilone B and isoflurane in rats (`khan-2024`)
25. 37801932 Comment on underground radiation and Orch OR: skip, comment
26. 37190380 A quantum-classical model of brain dynamics: skip, model
27. 36791569 Comment: skip
28. 36764151 Comment: skip
29. 36359629 Non-separability as a foundation of consciousness: skip, theory
30. 33715591 Anaesthetics and tubulin by molecular modelling: skip, simulation
31. 35617922 Derakhshani and colleagues 2022, spontaneous radiation and Orch OR: skip, an analysis of earlier published experiments (a review), not new data. Bears on `orch-dp-collapse`; the underlying experiment is not in the screen.
32. 35414166 Zadeh-Haghighi, Simon 2022, radical pairs: skip, model
33. 34758403 Orchid flowering genes: skip, off topic
34. 34439603 Neural circuits, microtubules, EM field: skip, review
35. 33232193 Hameroff 2020: skip, comment (also a proponents' statement, not opened)
36. 33378843 Quantum chemistry to quantum biology: skip, review
37. to 43: skip, off topic (zinc and cardiac, DHEA and bone, horse feeds, germ-cell tumours, testosterone and kidney, horse hay, a bacterial enzyme)
44. 31807566 The finer scale of consciousness: skip, review
45. to 47, 49, 51, 53, 54: skip, off topic (soil, osteoporosis, testosterone, prostate, zinc and cardiac, spleen)
48. 30142359 Intracellular signalling: skip, theoretical study
50. 28852014 Craddock ... Hameroff 2017, anaesthetics and terahertz oscillations in tubulin: skip, simulation
52. **T** 29154287 Accorsi, Mondo, Cocchi 2017, dogs' platelet fatty acids "according to theory Orch-OR" (`accorsi-2017`; abstract only; tests no recorded prediction)
55. 26227538 Serotonin and quantum consciousness: skip, model
56. 26478778 Barlow 2015, plants and Orch OR: skip, theory
57. 25912536 Schizophrenia and quantum theory: skip, review
58. 26191092 Platelet dialysis "measurement problem": skip. It reports data, but on angiogenic activity of platelet extracts, and does not say it bears on Orch OR or on microtubules in consciousness or anaesthesia.
59. 25714379 Craddock ... Hameroff 2015, anaesthetics in quantum channels: skip, molecular modelling
60. 25012711 Quantum effects in consciousness: skip, review
61. to 66, 68: skip, comments on the 2014 review
67. 24070914 Hameroff and Penrose 2014: skip, the theory paper itself
69. 24454909 Tang, Dai 2014, biophotons in mouse brain slices: skip. New data, and the abstract mentions consciousness, an anaesthetic (procaine) and the microtubule-associated protein tau. It does not say it bears on Orch OR or on microtubules in consciousness or anaesthesia; it is about light emission in neural circuits. *Unsure:* a looser reader might take it.
70. 24259348 Hameroff 2014, quantum walks: skip, theory
71, 72, 75, 77, 78, 80: skip, off topic (gold nanoparticles, sex steroids, bladder, osteoporosis, atrial fibrillation)
73. 23673035 Hameroff 2013, quantum cognition: skip, comment
74. 22925839 Baars and Edelman 2012: skip, theory and review. Used instead as a rival passage.
76. 23091452 Hameroff 2012, free will: skip, review
79. 20020354 The consciousness circuit: skip, theory

Counts: 80 screened, 4 taken. Of the four, 2 were opened and judged (`khan-2024`, `li-2025`), 1
was not opened (`huang-2026`, abstract only), and 1 tests no recorded prediction
(`accorsi-2017`, abstract only). All four are about anaesthesia except Accorsi. No study in the
screen tests predictions 1 to 7; the experiments that would (microtubule coherence, collapse
tests) are published in physics journals and do not match the query's medical-database filter
(`SRC:MED`).

## Unsure judgements (8 of 12)

- `out-khan-orch-anaesthetic-mt` (for): the test counts a change in either direction because the
  proponents fixed none. Other doubts: eight rats, mechanism not shown, and the righting reflex
  standing in for unconsciousness.
- `out-li-orch-anaesthetic-mt` (mixed): the bare wording gives "for"; the opposite-direction
  stabiliser results and the large morphine effect make it unable to tell mechanisms apart.
- `com-khan-orch-anaesthetic-mt` and `com-li-orch-anaesthetic-mt` (before): the dates are clear,
  but the 2013 passage commits to microtubules as an anaesthetic site, not to this drug test.
  "Unclear" is defensible, and would remove both studies.
- `tst-orch-mt-coherence`, `tst-orch-mt-entangle`, `tst-orch-mass-time`: whether open-ended
  predictions with no deadline or measuring rule "could fail".
- `tst-orch-anaesthetic-mt`: whether a network-level account of anaesthesia (Mashour) counts as a
  contrary prediction. No opened passage says so.

None of these changes a score today, because no prediction separates, so no study counts.

## Not opened (all on the verify list)

- Hameroff 2020, *Cognitive Neuroscience*: 403.
- Hameroff 2006, *Anesthesiology*: not fetched.
- The Royal Society and ScienceDirect pages for 1998 and 2014: 403. Read from third-party copies instead.
- Huang 2026 and Accorsi 2017: abstracts only. Huang needs a sign-in to Elsevier's *Neuropharmacology*. Accorsi needs a sign-in to IOS Press's *Journal of Integrative Neuroscience*.
- Baars and Edelman 2012: abstract only.

## Note on the dating fields

The brief asks for `study_first_appeared` in the commitment `dates` table, following ruling D.
The pilot's records still use `data_collected`. Both studies' collection dates are recorded on the
study records anyway (before 2024-07-01 and before 2024-01-17). Either test gives "before".
