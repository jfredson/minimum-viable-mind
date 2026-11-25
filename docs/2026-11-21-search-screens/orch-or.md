# Orchestrated Objective Reduction: per-prediction study screen, 2026-11-21

First reading by Claude (claude-opus-5-5). Theory id `orch-or`; eight predictions. The searches
had already run (raw results in `data/tracker/search-runs-2026-11-21/orch-*.json`); this file
screens them by the method fixed in `data/tracker/searches-2026-11-21.toml` before any search ran.
Screening used title and abstract only. Files beside this one: `studies.toml`, `sources.toml`,
`judgements.toml`, `verify.toml` (new records only; all four parse with `tomllib`; no id clashes
with the records; every quoted passage was checked by script against the copy opened).

## The rule used to screen, per prediction

A result qualifies when its title or abstract shows new data (or a reanalysis) that measures what
the prediction's test wording names. Where the wording needed reading, this is how it was read:

- **orch-mt-coherence, orch-mt-entangle, orch-coherence-time**: a measurement on microtubules of a
  quantum effect (a shared quantum state, quantum correlations, or how long one lasts).
  "Coherent" and "entangled" in their everyday or mechanical senses (coordinated growth, tangled
  polymers) do not count.
- **orch-synaptic-cyto**: a measured change in synaptic strength or its lasting change
  (for example long-term potentiation recorded electrically), together with a measured or
  blocked change in the cytoskeleton. Spine counts, synaptic protein levels or staining for a
  microtubule protein were not taken as measures of synaptic strength. *This is the screen's
  strictest call; see "Rule results" below.*
- **orch-mt-vibration**: vibrational states of microtubules measured in living neurons.
  "Resonance" in the sense of magnetic resonance imaging does not count.
- **orch-dp-collapse**: a test of collapse of a quantum superposition, or of its side effects
  (such as spontaneous radiation), that the abstract says bears on the Diósi-Penrose rule. A
  search that the abstract ties only to a different collapse model (CSL) does not qualify.
- **orch-mass-time**: a measure of how much brain tissue takes part, set against time to
  perception or response.
- **orch-anaesthetic-mt**: in animals or people, a drug acting on microtubules, with the dose or
  time needed for anaesthetic unconsciousness measured.

## The choice, and how the cap was applied

Six results qualified, in four of the eight lists:

| Prediction | Qualifying (earliest public appearance) | Taken |
|---|---|---|
| orch-anaesthetic-mt | huang-2026 (2026-01-08), li-2025 (2025-02-28), khan-2024 (2024-08-15) | huang-2026 |
| orch-synaptic-cyto | jia-2026 (2026-03-11) | jia-2026 |
| orch-dp-collapse | xenonnt-2026 (2025-06-05, arXiv preprint; journal 2026-03) | xenonnt-2026 |
| orch-mt-coherence | babcock-2024 (2023-02-03, arXiv preprint; journal 2024-04-19) | babcock-2024 |
| the other four | none | none |

The method takes the five most recent across all lists, at most one per prediction. Only four
predictions have any qualifying study, so **four studies are chosen and the fifth place is
empty**. The cap is what keeps li-2025 and khan-2024 out: without it, the fifth place would go to
li-2025 (2025-02-28), already in the records with its commitment settled "unclear".
No study qualified for two predictions, so the "taken once, judged for both" case did not arise.
Earliest public appearance was checked for each chosen study: arXiv preprints for xenonnt-2026
and babcock-2024 (both preprints already carried the result used here); Europe PMC preprint
searches found none for huang-2026 or jia-2026.

## What was opened, and what was not

- **babcock-2024**: opened (Europe PMC full text, CC BY 4.0). Judged.
- **xenonnt-2026**: opened (arXiv v2, the post-acceptance text, as HTML). Judged. The publisher's
  open PDF was downloaded but its text layer was only partly readable (verify entry
  `v-orch-xenonnt-aps`).
- **huang-2026**: **not opened.** Already in the records as not opened (verify entry
  `v-orch-huang-2026`, unchanged); no new record written. Not open access, no preprint.
  John would need a sign-in to *Neuropharmacology* on Elsevier's ScienceDirect.
- **jia-2026**: **not opened.** New record with `opened = false` and verify entry
  `v-orch-jia-2026`. Not open access, no preprint. The same sign-in (*Neuropharmacology*,
  ScienceDirect) would open it.
- The proponents' 1998 and 2014 texts were opened again from the same third-party copies the
  earlier drafting used; the new quotations from them are on the verify list
  (`v-orch-copies-new-judgements`).

So two of the four chosen studies carry judgements, and both of the most recent two are behind
the same publisher's paywall.

## Judgements (first reading)

| Judgement | Verdict | Unsure |
|---|---|---|
| com-babcock-orch-mt-coherence | before | no |
| out-babcock-orch-mt-coherence | mixed | yes |
| com-xenonnt-orch-dp-collapse | before | yes |
| out-xenonnt-orch-dp-collapse | against | yes |

Weights: babcock-2024 is 2 (outside the theory's camp only); xenonnt-2026 is 3 (outside the camp,
and replicated, a judgement explained below).

## Every unsure judgement

- **com-xenonnt-orch-dp-collapse (before).** The dates are clear (1998 and 2013 statements; data
  collected 2021, first published 2022; this analysis 2025). The doubt is commitment. The detector
  tests the faint X-ray glow that the Markovian (white-noise) form of the Diósi-Penrose model
  predicts. The proponents committed to the collapse rule and its timing, and in 2013 named the
  Diósi-Penrose scheme, but never to that form or to any glow. A reader who wants the exact test
  fixed in advance reads "unclear", and then the study does not count. Against that, the
  prediction's settled test wording names this glow as a way the prediction fails.
- **out-xenonnt-orch-dp-collapse (against).** The paper sets the model's smearing length above
  about half a nanometre (4.9 × 10^-10 m) and does not mention Orch OR. The proponents' 2014
  calculation puts the mass at the scale of carbon nuclei (2.5 × 10^-15 m), about a hundred
  thousand times smaller, where the glow would be far stronger than seen. Linking the two numbers
  is this reader's step, not the paper's. The 2014 review also calls the scale "a large
  uncertainty", so a larger scale escapes. A reader weighing that reads "mixed".
- **out-babcock-orch-mt-coherence (mixed).** A reader who takes the authors' conclusion
  (measurements "confirmed" their superradiance predictions) reads "for". The authors themselves
  say lifetime measurements are needed, so the result fits a shared quantum state but cannot yet
  tell it apart from less energy lost as heat. The coherence is also a brief light-driven state in
  a test tube, which may not be the kind the theory needs in neurons; that doubt did not move the
  verdict, because the prediction's wording does not say which kind.

**The shakiest reading** is `out-xenonnt-orch-dp-collapse`: "against" rests on matching the
paper's smearing length to the proponents' 2.5-femtometre figure, a step the paper does not take.

## Rule results John may not have intended

1. **The cap leaves a place empty.** Only four of eight predictions have any qualifying study,
   so the "five most recent, at most one per prediction" rule chooses four. The busy topic it was
   meant to stop (anaesthesia: three qualifying studies) is exactly the one that would have
   filled the fifth place.
2. **The screen's reading of "synaptic strength" decides the synaptic pick.** Read strictly
   (an electrical measure of synaptic strength), only jia-2026 qualifies. Read loosely (structural
   signs such as spine counts, or plasticity named without a method), four more recent results
   would qualify (results 7, 10, 18 and 28 in that list; result 33 too, but it is older), and the most recent, result 7
   (2026-09-30, an epilepsy drug study measuring spine density and a microtubule protein), would
   be taken instead. jia-2026 is not opened either way.
3. **The physics test counts through one form of the model.** xenonnt-2026 is the only chosen
   study that is opened, outside the camp and plainly dated, and its "against" depends on the
   Markovian glow, which the proponents never adopted. If the commitment is read "unclear", the
   one recorded failure of the theory's collapse claim disappears; if it is read "before", a
   physics experiment that never mentions consciousness counts against a theory of it. The
   prediction's own note already anticipates the proponents' reply and says it does not undo a
   recorded failure.
4. **"Replicated" for an earlier, weaker study.** xenonnt-2026 is marked replicated because the
   Majorana Demonstrator, a separate collaboration, had already found no such glow in 2022 and set
   the previous best limit. That search came first and was five times less sensitive. If
   "replicated" must mean a later repeat at the same sensitivity, mark it false and the weight
   drops from 3 to 2. The Majorana study was in the screen (orch-dp-collapse, result 12) but did not
   qualify, because its abstract ties it only to the CSL model.
5. **Physics journals are partly outside MEDLINE.** The collapse query was run without the MEDLINE
   filter, as written. Even so, most of its 52 hits are off topic (soil collapse, lung collapse,
   protein folding), because "collapse model" and "test" match widely.

## Screen, per prediction

Each line: rank, PubMed id, Europe PMC first publication date, title, decision.

### orch-mt-coherence

Hits: 133. Screened: 40. Qualifying: 1.

1. 42537979 (2026-07-31) On the functional significance of quantum effects at subneuronal scales. Does not qualify: theory or hypothesis paper, no new data (built from published measurements).
2. 42421320 (2026-07-08) Computational modeling of microtubule dynamic instability: From molecular mechanisms to emergent behavior. Does not qualify: review.
3. 42409159 (2026-07-06) Coherent photonic biofields: Revisiting Fritz-Albert Popp's hypothesis. Does not qualify: theory or hypothesis paper, no new data.
4. 42450355 (2026-07-07) Neuronal Microtubules and Radiofrequency Waves: The Quantum Core of Human Consciousness, Memory, and Pathway to Memory Enhancement/Recovery. Does not qualify: review.
5. 42432227 (2026-07-10) Endophytic Aspergillus glaucus as a novel epothilone B producer: Antiproliferative activity and in silico analysis. Does not qualify: off topic (a fungus that makes epothilone B).
6. 42055333 (2026-04-27) A coherent structural picture of the interaction of Tau with tubulin provides a link to its aggregation. Does not qualify: review.
7. 41713567 (2026-02-17) Feasibility analysis of the surface code model for the Orch-OR microtubule. Does not qualify: model or simulation, no new data.
8. 42041796 (2026-03-31) Quantum-Inspired and Non-Classical Approaches to Consciousness: Models, Evidence and Constraints. Does not qualify: review.
9. 41524425 (2026-03-04) Geometry-dependent transmission of externally imposed shear stress in confined microtubule-kinesin active fluids. Does not qualify: new data, but on the flow mechanics of microtubule-motor fluids; no quantum measurement.
10. 41751706 (2026-02-11) Quantum Information Flow in Microtubule Tryptophan Networks. Does not qualify: model or simulation, no new data.
11. 42920515 (2026-10-09) Dimensional convergence at the nanoscale: a novel synthesis of experimental evidence justifying direct measurement of quantum coherence in microtubules. Does not qualify: a synthesis of other groups' experiments, no new data.
12. 42643630 (2026-08-11) Transient entanglement in minimal open XXZ spin chains: a toy-model analogy for microtubule-inspired quantum biology. Does not qualify: model or simulation, no new data.
13. 42137636 (2026-04-29) Self-referential processing as the biological switch between classical and quantum functioning of the brain. Does not qualify: theory or hypothesis paper, no new data.
14. 41988526 (2026-03-31) Psychedelics and the quantum brain: a falsifiable hypothesis on Posner molecules and spin-dependent pharmacology. Does not qualify: theory or hypothesis paper, no new data.
15. 41266643 (2025-11-20) 4Pi-SIMFLUX: 4Pi single-molecule localization microscopy with structured illumination. Does not qualify: microscopy method.
16. 40999612 (2026-01-01) A Unified Model of Consciousness: Glycoprotein Patterns in Memory Processes and Quantum Entanglement. Does not qualify: editorial.
17. 41229347 (2025-12-03) Modeling active nematics &lt;i&gt;via&lt;/i&gt; the nematic locking principle. Does not qualify: model or simulation, no new data.
18. 41303511 (2025-11-14) TDP-43 Regulates Rab4 Levels to Support Synaptic Vesicle Recycling and Neuromuscular Connectivity in &lt;i&gt;Drosophila&lt;/i&gt; and Human ALS Models. Does not qualify: off topic.
19. 40522379 (2025-06-16) Consciousness, Microtubules, and the Axon Initial Segment. Does not qualify: theory or hypothesis paper, no new data.
20. 40062969 (2025-03-10) Vimentin filament transport and organization revealed by single-particle tracking and 3D FIB-SEM. Does not qualify: off topic (vimentin filaments).
21. 41281348 (2025-11-19) On the potential of microtubules for scalable quantum computation. Does not qualify: review.
22. 41132902 (2025-10-21) Consciousness and spintronic coherence in microtubules. Does not qualify: theory or hypothesis paper, no new data.
23. 39815535 (2025-01-01) Microtubular structured random lasers as microfluidic channels for multifunctional sensing. Does not qualify: about artificial "microtubular" laser tubes, not biological microtubules.
24. 38695186 (2024-05-02) Retrofitting the Heart: Explaining the Enigmatic Septal Thickening in Hypertrophic Cardiomyopathy. Does not qualify: review.
25. 38641327 (2024-04-19) Ultraviolet Superradiance from Mega-Networks of Tryptophan in Biological Architectures. **Taken** as `babcock-2024`.
26. 38553880 (2024-04-01) The Planar Cell Polarity Protein Fat1 in Sertoli Cell Function. Does not qualify: off topic.
27. 36752605 (2023-02-08) Motor processivity and speed determine structure and dynamics of microtubule-motor assemblies. Does not qualify: new data on motor-driven microtubule assemblies; classical mechanics, no quantum measurement.
28. 35398343 (2022-04-08) Cell chirality regulates coherent angular motion on small circular substrates. Does not qualify: off topic.
29. 35385739 (2022-04-01) Augmin-dependent microtubule self-organization drives kinetochore fiber maturation in mammals. Does not qualify: cell biology of spindles; no quantum measurement.
30. 34360980 (2021-07-30) Generation of Electromagnetic Field by Microtubules. Does not qualify: theory or hypothesis paper, no new data (classical dipole calculation).
31. 34340333 (2021-07-01) Fractal generation in a two-dimensional active-nematic fluid. Does not qualify: classical active-fluid physics.
32. 32324945 (2020-05-15) Nucleating microtubules in neurons: Challenges and solutions. Does not qualify: review.
33. 32844429 (2020-09-02) Second harmonic generation microscopy using pixel reassignment. Does not qualify: microscopy method.
34. 32961270 (2020-09-19) Fibrillation and molecular characteristics are coherent with clinical and pathological features of 4-repeat tauopathy caused by MAPT variant G273R. Does not qualify: off topic (tau fibrils).
35. 32579171 (2020-09-01) Structural view of the yeast Dam1 complex, a ring-shaped molecular coupler for the dynamic microtubule end. Does not qualify: review.
36. 32665556 (2020-07-14) In vivo microscopy reveals macrophage polarization locally promotes coherent microtubule dynamics in migrating cancer cells. Does not qualify: "coherent" here means coordinated growth of microtubules in migrating cells, not a quantum state.
37. 32289972 (2020-03-01) Gliding filament system giving both global orientational order and clusters in collective motion. Does not qualify: classical collective motion.
38. 32084125 (2020-02-21) Cytoskeleton polarity is essential in determining orientational order in basal bodies of multi-ciliated cells. Does not qualify: model or simulation, no new data.
39. 33285818 (2019-12-27) Non-Equilibrium Quantum Electrodynamics in Open Systems as a Realizable Representation of Quantum Field Theory of the Brain. Does not qualify: theory or hypothesis paper, no new data.
40. 31611385 (2019-10-14) Tunable corrugated patterns in an active nematic sheet. Does not qualify: classical active-fluid physics.

### orch-mt-entangle

Hits: 76. Screened: 40. Qualifying: 0.

1. 42450355 (2026-07-07) Neuronal Microtubules and Radiofrequency Waves: The Quantum Core of Human Consciousness, Memory, and Pathway to Memory Enhancement/Recovery. Does not qualify: review.
2. 40468966 (2025-06-05) Nuclear Entanglement: New Insights Into the Role of Cytoskeleton and Nucleoskeleton in Plant Nuclear Function. Does not qualify: review.
3. 42041796 (2026-03-31) Quantum-Inspired and Non-Classical Approaches to Consciousness: Models, Evidence and Constraints. Does not qualify: review.
4. 42643630 (2026-08-11) Transient entanglement in minimal open XXZ spin chains: a toy-model analogy for microtubule-inspired quantum biology. Does not qualify: model or simulation, no new data.
5. 41988526 (2026-03-31) Psychedelics and the quantum brain: a falsifiable hypothesis on Posner molecules and spin-dependent pharmacology. Does not qualify: theory or hypothesis paper, no new data.
6. 40999612 (2026-01-01) A Unified Model of Consciousness: Glycoprotein Patterns in Memory Processes and Quantum Entanglement. Does not qualify: editorial.
7. 41053963 (2025-10-06) Rigidity Governs Entrainment of Bacteria Cells in Biopolymer Scaffolds. Does not qualify: "entrainment" of bacteria in gels; off topic.
8. 40788221 (2025-08-11) Multi-kinesin clusters impart mechanical stress that reveals mechanisms of microtubule breakage in cells. Does not qualify: microtubule breakage mechanics; no quantum measurement.
9. 40279414 (2025-04-25) Protecting centrosomes from fracturing enables efficient cell navigation. Does not qualify: off topic.
10. 40149167 (2025-02-26) Quantum Models of Consciousness from a Quantum Information Science Perspective. Does not qualify: perspective, no new data.
11. 41281348 (2025-11-19) On the potential of microtubules for scalable quantum computation. Does not qualify: review.
12. 41019231 (2025-09-13) Conscious active inference II: Quantum orchestrated objective reduction among intraneuronal microtubules naturally accounts for discrete perceptual cycles. Does not qualify: review.
13. 40342554 (2025-05-06) A quantum microtubule substrate of consciousness is experimentally supported and solves the binding and epiphenomenalism problems. Does not qualify: review.
14. 39214493 (2024-08-28) On the possibility of implementing a quantum entanglement distribution in a biosystem: Microtubules. Does not qualify: model or simulation, no new data.
15. 38402459 (2024-07-01) PLK1 phosphorylation of ZW10 guides accurate chromosome segregation in mitosis. Does not qualify: off topic.
16. 38072337 (2023-12-10) Modeling of the quantum entangled state transfer protocol in the cell microtubules. Does not qualify: model or simulation, no new data.
17. 37893156 (2023-10-13) In Silico Approaches to Developing Novel Glycogen Synthase Kinase 3β (GSK-3β). Does not qualify: in silico drug design.
18. 37400052 (2023-07-01) Modeling of the entangled states transfer processes in microtubule tryptophan system. Does not qualify: model or simulation, no new data.
19. 38075677 (2023-11-24) Hypothesis: The opposing pulling forces exerted by spindle microtubules can cause sliding of chromatin layers and facilitate sister chromatid resolution. Does not qualify: theory or hypothesis paper, no new data.
20. 38505277 (2022-08-26) Multiscale architecture: Mechanics of composite cytoskeletal networks. Does not qualify: review.
21. 36056012 (2022-09-02) Optical-Tweezers-integrating-Differential-Dynamic-Microscopy maps the spatiotemporal propagation of nonlinear strains in polymer blends and composites. Does not qualify: "entangled" means tangled polymers; mechanics.
22. 36094259 (2022-08-25) Reconstituting and Characterizing Actin-Microtubule Composites with Tunable Motor-Driven Dynamics and Mechanics. Does not qualify: methods video on composites.
23. 35086931 (2022-02-01) Extensile to contractile transition in active microtubule-actin composites generates layered asters with programmable lifetimes. Does not qualify: "entangled" polymer composites; mechanics.
24. 35549144 (2021-11-19) DNA Conformation Dictates Strength and Flocculation in DNA-Microtubule Composites. Does not qualify: polymer composites; mechanics.
25. 32312216 (2020-05-05) Size-dependent dynamic stability analysis of the cantilevered curved microtubule-associated proteins (MAPs). Does not qualify: model or simulation, no new data.
26. 33586756 (2021-03-01) Static adhesion hysteresis in elastic structures. Does not qualify: mechanics.
27. 33547082 (2021-02-05) Myosin-driven actin-microtubule networks exhibit self-organized contractile dynamics. Does not qualify: actin-microtubule network mechanics.
28. 33232193 (2020-11-24) 'Orch OR' is the most complete, and most easily falsifiable theory of consciousness. Does not qualify: comment (Hameroff 2020, a proponents' statement).
29. 33166678 (2020-11-07) The entangled relationship between cilia and actin. Does not qualify: review.
30. 32957179 (2020-06-01) Biological cells and coupled electro-mechanical effects: The role of organelles, microtubules, and nonlocal contributions. Does not qualify: model or simulation, no new data ("nonlocal" in the mechanics sense).
31. 32379884 (2020-06-01) Microtubules control cellular shape and coherence in amoeboid migrating cells. Does not qualify: cell shape; no quantum measurement.
32. 31853502 (2019-12-13) Topology-dependent anomalous dynamics of ring and linear DNA are sensitive to cytoskeleton crosslinking. Does not qualify: DNA in cytoskeleton networks; mechanics.
33. 31519880 (2019-09-13) Vimentin filaments interact with the actin cortex in mitosis allowing normal cell division. Does not qualify: off topic.
34. 30177441 (2018-08-16) Co-Entangled Actin-Microtubule Composites Exhibit Tunable Stiffness and Power-Law Stress Relaxation. Does not qualify: polymer composites; mechanics.
35. 28975423 (2017-10-03) Structure-property relation and relevance of beam theories for microtubules: a coupled molecular and continuum mechanics study. Does not qualify: model or simulation, no new data.
36. 29971233 (2018-06-19) Kinase and Phosphatase Cross-Talk at the Kinetochore. Does not qualify: review.
37. 28627043 (2017-06-19) Fabrication of Millimeter-Long Carbon Tubular Nanostructures Using the Self-Rolling Process Inherent in Elastic Protein Layers. Does not qualify: materials science.
38. 28427819 (2017-04-17) Size-dependent axial instability of microtubules surrounded by cytoplasm of a living cell based on nonlocal strain gradient elasticity theory. Does not qualify: model or simulation, no new data.
39. 27477947 (2016-07-28) Cellulose-Microtubule Uncoupling Proteins Prevent Lateral Displacement of Microtubules during Cellulose Synthesis in Arabidopsis. Does not qualify: plant cell walls.
40. 26233708 (2015-07-23) The effects of anti-DNA topoisomerase II drugs, etoposide and ellipticine, are modified in root meristem cells of Allium cepa by MG132, an inhibitor of 26S proteasomes. Does not qualify: plant root cells and drugs.

### orch-synaptic-cyto

Hits: 1392. Screened: 40. Qualifying: 1.

1. 42831136 (2026-09-10) Investigating the effects of missense mutations on the dual Ras/Rap activation mechanism of SYNGAP1 using molecular modelling. Does not qualify: model or simulation, no new data.
2. 42572407 (2026-08-09) Occupationally relevant vibrations and the brain: frequency-dependent proteomics signatures in a rat model. Does not qualify: proteomics after whole-body vibration; no measure of synaptic strength.
3. 43046860 (2026-11-01) Small Molecules Targeting TrkB/BDNF for Neurodegenerative Disease Therapeutic Discovery. Does not qualify: review.
4. 43033188 (2026-11-13) MM102 promotes axonal regeneration and synaptic remodeling through membrane lipid remodeling to restore motor function after spinal cord injury. Does not qualify: nerve regrowth after spinal cord injury; tubulin and synapse-formation markers, but no measure of a change in synaptic strength.
5. 43006739 (2026-11-10) Allosteric activation of CaMK4 by Calmodulin enables phosphorylation of WNK2 kinase. Does not qualify: protein biochemistry; no synapse measured.
6. 42992918 (2026-11-01) High-Resolution Spatial Proteomics Uncovers Molecular Diversity across Mouse Hippocampal Subregions. Does not qualify: protein atlas of the hippocampus; no change measured.
7. 42779151 (2026-09-30) Perampanel improves cognitive function in epilepsy by targeting AMPA receptor subunit GluR2-mediated endoplasmic reticulum stress and synaptic plasticity. Does not qualify: BORDERLINE: spine counts and MAP2 staining (a microtubule protein), which the authors call synaptic plasticity, but no measure of synaptic strength.
8. 42712177 (2026-09-30) Biophysical characterization of Arc protein-RNA interactions. Does not qualify: protein biophysics in a test tube.
9. 42674204 (2026-08-31) Cytoskeletal alterations underlying dendritic and synaptic plasticity in epilepsy. Does not qualify: review.
10. 42202912 (2026-05-26) Jiawei Sini San ameliorates cognitive deficits in CUMS depression rats by reshaping dendritic spines through regulating TRPC6-activated ROCK2-Cofilin signaling pathway. Does not qualify: BORDERLINE: dendritic spines and F-actin (cytoskeleton) measured, but no measure of synaptic strength.
11. 43043659 (2026-09-21) A non-canonical PDZ recognition mechanism underlies the synaptic CTNND2-MAGI2 complex assembly. Does not qualify: protein structure.
12. 42799673 (2026-09-26) KIF1A-Mediated Axonal Transport of Netrin-1 in iPSC-Derived Human Forebrain Neurons. Does not qualify: axonal transport of a guidance protein.
13. 42726843 (2026-09-11) CaMKIIα holoenzymes self-organize into chain-like mesoscale clusters. Does not qualify: protein imaging in a test tube; no synapse.
14. 42543904 (2026-09-01) Executive Function and Epigenetic Markers in Youth Exposed to Family and Community Violence in Childhood. Does not qualify: off topic.
15. 42523149 (2026-07-29) Novel blood lncRNA biomarkers associated with clinical severity and specific cognitive dimensions in Alzheimer's disease. Does not qualify: off topic (blood biomarkers).
16. 43021116 (2026-08-19) Neuregulin 2 and tubulin protein levels in children with autism spectrum disorder. Does not qualify: blood tubulin levels in autism; no synapse measured.
17. 42653320 (2026-08-16) Epigenetic Control of Stress-Induced Depression: Emerging Roles of HDAC3 and HDAC6. Does not qualify: review.
18. 42603820 (2026-08-15) Neurabin I haploinsufficiency disrupts ion channel regulation and synaptic maturation in human cortical neurons in neurodevelopmental disorders. Does not qualify: BORDERLINE: a cytoskeletal scaffold gene, with patch-clamp recordings, but of firing (intrinsic excitability), not synaptic strength.
19. 42210778 (2026-05-29) Fine-Tuned Regulation of mRNA Translation and Transport by STAU2 Condensate Facilitates Neuronal Development and Plasticity. Does not qualify: RNA granules carried along microtubules; no cytoskeletal change with synaptic change measured.
20. 43004397 (2026-07-28) Activity-dependent increase of Egr1 in the hippocampus improves contextual memory in mice. Does not qualify: a gene for memory and potentiation; no cytoskeleton measured.
21. 42652054 (2026-07-24) Limited Detectability of Network Functional Alterations in a Tauopathy Model Using Mouse Primary Cortical Cultures. Does not qualify: network activity in a tau disease model; no synaptic strength or cytoskeleton change measured.
22. 42511986 (2026-07-05) Targeting CRMP2 for Chronic Pain: From Molecular Mechanisms to Therapeutic Strategies. Does not qualify: review.
23. 42450246 (2026-07-03) Subcortical Dendritic Scaffolding in Autism Spectrum Disorder: A Testable ANK2-SCN2A-SHANK Framework. Does not qualify: review.
24. 42417179 (2026-07-08) Actin scaffolds as organizers of presynaptic function, assembly and plasticity across species. Does not qualify: review.
25. 42104730 (2026-05-09) A novel synaptic compartmentalization failure framework for neurodegeneration. Does not qualify: review.
26. 41945856 (2026-04-07) Nanoscale Spatial Organization of ARC High- and Low-Order Assemblies at Excitatory Synapses. Does not qualify: nanoscale imaging of the ARC protein (named "cytoskeleton-associated" but not part of the cytoskeleton); no synaptic strength measured.
27. 42334898 (2026-06-23) Combining post-mortem and neuroimaging measures of brain amyloidosis to accelerate genomic discovery. Does not qualify: off topic (genetics).
28. 42321890 (2026-06-19) Aerobic exercise enhances α-tubulin lactylation and neurological recovery after ischemic stroke. Does not qualify: BORDERLINE: tubulin modification and "synaptic plasticity" both reported after stroke, but the abstract does not say how plasticity was measured.
29. 42268489 (2026-06-10) Unravelıng non-canonıcal Wnt sıgnalıng ın neural development and dısorders: a revıew of Wnt/PCP and Wnt/ca&lt;sup&gt;²⁺&lt;/sup&gt; pathways. Does not qualify: review.
30. 42208149 (2026-05-28) An Adnp frameshift variant disrupts Wnt signalling inducing chromatocytoskeletal defects and autism-related behaviour in male mice. Does not qualify: cytoskeletal gene expression and behaviour; no synaptic strength measured.
31. 42002114 (2026-04-17) NOTCH3 R545C mutation drives vascular-neuronal dysfunction and cognitive impairment in CADASIL pathogenesis. Does not qualify: impaired synaptic plasticity, but no cytoskeleton measured.
32. 41825505 (2026-03-11) The MAP6-NTS axis in hippocampal CA1 regulates synaptic plasticity and memory. **Taken** as `jia-2026 (not opened)`.
33. 41713405 (2026-02-19) Role of microtubule affinity-regulating kinases in epilepsy: A novel therapeutic strategy. Does not qualify: BORDERLINE: kinases that regulate microtubules, with EEG and signalling proteins; no direct measure of synaptic strength or of the cytoskeleton.
34. 41687803 (2026-02-11) The serotonin receptor 7 as an emerging target to restore altered neuroplasticity in Angelman syndrome. Does not qualify: review.
35. 42204717 (2026-05-28) Environmental enrichment is associated with enhanced novel object recognition performance and an increased proportion of smooth endoplasmic reticulum-containing spines in the dentate gyrus of Septin3&lt;sup&gt;-/-&lt;/sup&gt; mice. Does not qualify: septin (a cytoskeletal protein) knockout, with spine contents and behaviour; synaptic strength not measured in this study.
36. 42138082 (2026-05-15) Wdr26 insufficiency causes Skraban-Deardorff syndrome-like neurodevelopmental deficits in mice. Does not qualify: MAP2 levels and behaviour; no synaptic strength measured.
37. 42128064 (2026-05-12) Disruption of hippocampal synaptic plasticity by chronic ethanol exposure: A narrative review of neurotoxic adverse outcome pathways. Does not qualify: review.
38. 42120067 (2026-05-12) CircMAP2 attenuates synaptic impairment in neurons subjected to cerebral ischaemia/reperfusion injury. Does not qualify: synapse structure and proteins; the "MAP2" in the name is an RNA, no cytoskeleton measured.
39. 42102067 (2026-05-08) A Proline-Rich-Domain-Binding Single Domain Antibody Selectively Inhibits RNA-Induced Phase Separation of Tau. Does not qualify: protein biochemistry.
40. 42086746 (2026-05-05) Structural basis for recognition of diverse localizing mRNAs by Egl-BicD. Does not qualify: protein structure.

### orch-mt-vibration

Hits: 181. Screened: 40. Qualifying: 0.

1. 43043498 (2026-11-17) Mild perinatal hypoxia uncouples excitatory-inhibitory circuit maturation and reprograms neocortical organization. Does not qualify: off topic.
2. 42654155 (2026-08-20) Targeting TTLL1 Alleviates Aβ-Induced Microtubule Disruption and TAU Pathology in Human iPSC-Derived Cortical Neurons. Does not qualify: tau and microtubule damage in cultured neurons; no vibration measured.
3. 42450355 (2026-07-07) Neuronal Microtubules and Radiofrequency Waves: The Quantum Core of Human Consciousness, Memory, and Pathway to Memory Enhancement/Recovery. Does not qualify: review.
4. 42852325 (2026-06-01) A Case of Early-Onset VCP-Related Frontotemporal Dementia: Insights from Neuroimaging and Genetic Analysis. Does not qualify: case report.
5. 42102067 (2026-05-08) A Proline-Rich-Domain-Binding Single Domain Antibody Selectively Inhibits RNA-Induced Phase Separation of Tau. Does not qualify: tau biochemistry.
6. 42074141 (2026-04-14) Synphilin-1 Is Essential for Cytoskeletal Integrity of Brain Ventricular Cilia and Mitochondrial Proteostasis. Does not qualify: off topic.
7. 41921971 (2026-04-01) Electric Double Layer Phenomena Near Surfaces Irreversibly Trigger Assembly of Tau Protein. Does not qualify: tau biochemistry.
8. 42577438 (2026-07-27) From clinical phenotypes to molecular precision: multimodal biomarkers for progressive supranuclear palsy. Does not qualify: review.
9. 41537864 (2025-12-01) Architecture-encoded mechanics and communication in microtubules: a multiscale computational study. Does not qualify: model or simulation, no new data.
10. 39688878 (2025-01-08) Detecting the Undetectable: Advances in Methods for Identifying Small Tau Aggregates in Neurodegenerative Diseases. Does not qualify: review.
11. 39681249 (2024-12-15) Fidgetin binds spastin to attenuate the microtubule-severing activity. Does not qualify: microtubule-cutting enzymes; no vibration measured.
12. 41019231 (2025-09-13) Conscious active inference II: Quantum orchestrated objective reduction among intraneuronal microtubules naturally accounts for discrete perceptual cycles. Does not qualify: review.
13. 39857391 (2025-01-06) GENI as an AMPK Activator Binds α and γ Subunits and Improves the Memory Dysfunction of Alzheimer's Disease Mouse Models via Autophagy and Neuroprotection. Does not qualify: off topic.
14. 39171951 (2024-09-10) BIN1 deficiency enhances ULK3-dependent autophagic flux and reduces dendritic size in mouse hippocampal neurons. Does not qualify: off topic.
15. 39171695 (2024-09-03) Mitochondrial bioenergetics stimulates autophagy for pathological MAPT/Tau clearance in tauopathy neurons. Does not qualify: off topic.
16. 38837385 (2024-06-05) Quantitative cellular pathology of the amygdala in temporal lobe epilepsy and correlation with magnetic resonance imaging volumetry, tissue microstructure, and sudden unexpected death in epilepsy risk factors. Does not qualify: "resonance" is magnetic resonance imaging.
17. 38826096 (2024-06-03) Pick's Disease Presenting as Tremulous Parkinsonism with Limited Levodopa Response-A Rare Cause of Corticobasal Syndrome. Does not qualify: case report.
18. 38292192 (2023-07-08) Cerebral furin deficiency causes hydrocephalus in mice. Does not qualify: off topic.
19. 38658850 (2024-04-24) Clinical and molecular outcomes from the 5-Year natural history study of SSADH Deficiency, a model metabolic neurodevelopmental disorder. Does not qualify: off topic.
20. 38512672 (2024-01-01) Phosphorylation of Tau Protein by CDK2/cyclin A and GSK3β Recombinant Kinases: Analysis of Phosphorylation Patterns by Nuclear Magnetic Resonance Spectroscopy. Does not qualify: "resonance" is nuclear magnetic resonance of tau.
21. 38463420 (2024-03-06) Histological Characterisation of a Sheep Model of Mild Traumatic Brain Injury: A Pilot Study. Does not qualify: pilot animal study of brain injury; no vibration measured.
22. 37788754 (2023-10-01) Resistance exercise alleviates the prefrontal lobe injury and dysfunction by activating SESN2/AMPK/PGC-1α signaling pathway and inhibiting oxidative stress and inflammation in mice with myocardial infarction. Does not qualify: off topic.
23. 37450599 (2023-07-14) Amyloid fibril structures of tau: Conformational plasticity of the second microtubule-binding repeat. Does not qualify: tau structure by nuclear magnetic resonance.
24. 36724228 (2023-02-01) Chaperoning of specific tau structure by immunophilin FKBP12 regulates the neuronal resilience to extracellular stress. Does not qualify: off topic.
25. 36756194 (2023-01-23) Pathogenic tau decreases nuclear tension in cultured neurons. Does not qualify: off topic.
26. 36310199 (2023-01-01) Analysis of Tau/Nucleoporin Interactions by Surface Plasmon Resonance Spectroscopy. Does not qualify: "resonance" is surface plasmon resonance.
27. 36945338 (2022-08-22) Probing the Interactions of Lamotrigine and Phenobarbital with Tau Protein: Experimental and Molecular Modeling Studies. Does not qualify: drug-tau binding.
28. 35597325 (2022-05-18) Manganese-enhanced magnetic resonance imaging method detects age-related impairments in axonal transport in mice and attenuation of the impairments by a microtubule-stabilizing compound. Does not qualify: axonal transport by magnetic resonance imaging; no vibration measured.
29. 35857846 (2022-07-20) Microtubule-binding core of the tau protein. Does not qualify: tau structure.
30. 35408855 (2022-03-23) Phosphorylation but Not Oligomerization Drives the Accumulation of Tau with Nucleoporin Nup98. Does not qualify: tau biochemistry.
31. 35373198 (2022-03-01) Global Structure of the Intrinsically Disordered Protein Tau Emerges from Its Local Structure. Does not qualify: tau structure.
32. 35782391 (2022-06-16) Consciousness, Cognition and the Neuronal Cytoskeleton - A New Paradigm Needed in Neuroscience. Does not qualify: theory paper (Hameroff 2022, a proponents' statement).
33. 35663380 (2022-04-28) Histologic lesion type correlates of magnetic resonance imaging biomarkers in four-repeat tauopathies. Does not qualify: imaging and pathology of tau diseases.
34. 35412274 (2022-01-01) Studying Axonal Transport in the Brain by Manganese-Enhanced Magnetic Resonance Imaging (MEMRI). Does not qualify: imaging method.
35. 33910450 (2021-12-01) Development of molecular tools for diagnosis of Alzheimer's disease that are based on detection of amyloidogenic proteins. Does not qualify: review.
36. 34320693 (2021-07-28) The hot cross bun sign in corticobasal degeneration. Does not qualify: case report.
37. 33956508 (2021-05-06) Effects of Low-Dose Gestational TCDD Exposure on Behavior and on Hippocampal Neuron Morphology and Gene Expression in Mice. Does not qualify: off topic.
38. 33932318 (2021-05-01) Neuroprotective response and efficacy of intravenous administration of mesenchymal stem cells in traumatic brain injury mice. Does not qualify: off topic.
39. 33621102 (2021-02-23) Super-resolution Imaging of Energy Transfer by Intensity-Based STED-FRET. Does not qualify: microscopy method.
40. 33583409 (2021-02-15) Serum neurofilament light and tau as prognostic markers for all-cause mortality in the elderly general population-an analysis from the MEMO study. Does not qualify: blood markers.

### orch-dp-collapse

Hits: 52. Screened: 40. Qualifying: 1.

1. 42086863 (2026-05-05) Bell-inequality violation for continuous, non-projective measurements. Does not qualify: theory or hypothesis paper, no new data (Bell tests on continuous data).
2. 41964993 (2026-03-01) Challenging Spontaneous Quantum Collapse with the XENONnT Dark Matter Detector. **Taken** as `xenonnt-2026`.
3. 40355473 (2025-05-12) Monitoring subsurface soil displacement in karst collapse by designing a MEMS-based spherical monitoring device. Does not qualify: off topic (soil).
4. 39517747 (2024-10-25) Model Test on Acoustic Emission Monitoring of Loess Slope Failure. Does not qualify: off topic (slopes).
5. 39054922 (2024-08-07) Gravitationally-induced wave function collapse time for molecules. Does not qualify: calculation of collapse times, no new data.
6. 39085627 (2024-07-31) Model experimental study on the mechanism of collapse induced by leakage of underground pipeline. Does not qualify: off topic (pipes).
7. 37998181 (2023-10-27) Experimental Predictions for Norm-Conserving Spontaneous Collapse. Does not qualify: theory or hypothesis paper, no new data.
8. 37190433 (2023-04-12) Collapse Models: A Theoretical, Experimental and Philosophical Review. Does not qualify: review.
9. 36832661 (2023-02-04) A Novel Approach to Parameter Determination of the Continuous Spontaneous Localization Collapse Model. Does not qualify: statistical method for a different collapse model (CSL); no new data in the abstract.
10. 36584389 (2023-02-13) Hoop compression driven instabilities in spontaneously formed multilayer graphene blisters over a polymeric substrate. Does not qualify: off topic.
11. 35617922 (2022-05-17) At the crossroad of the search for spontaneous radiation and the Orch OR consciousness theory. Does not qualify: review (Derakhshani and colleagues 2022).
12. 36053678 (2022-08-01) Search for Spontaneous Radiation from Wave Function Collapse in the Majorana Demonstrator. Does not qualify: new data on collapse radiation, but the abstract tests only a different collapse model (CSL), not the Diósi-Penrose rule.
13. 35956758 (2022-07-27) Interdiction in the Early Folding of the p53 DNA-Binding Domain Leads to Its Amyloid-Like Misfolding. Does not qualify: off topic.
14. 35879511 (2022-07-25) Spontaneous breathing promotes lung injury in an experimental model of alveolar collapse. Does not qualify: off topic.
15. 35409264 (2022-03-31) Protein Folding Interdiction Strategy for Therapeutic Drug Development in Viral Diseases: Ebola VP40 and Influenza A M1. Does not qualify: off topic.
16. 31905827 (2019-12-30) Effect of Porosity on Dynamic Mechanical Properties and Impact Response Characteristics of High Aluminum Content PTFE/Al Energetic Materials. Does not qualify: off topic.
17. 31491197 (2019-08-01) Neutron Star Heating Constraints on Wave-Function Collapse Models. Does not qualify: calculation from existing neutron-star observations for CSL-type models; no new data.
18. 30901220 (2019-04-03) Nature's Shortcut to Protein Folding. Does not qualify: off topic.
19. 30638968 (2019-01-11) Control of Acoustic Cavitation for Efficient Sonoporation with Phase-Shift Nanoemulsions. Does not qualify: off topic.
20. 30057369 (2018-07-30) The route to massive black hole formation via merger-driven direct collapse: a review. Does not qualify: review.
21. 30278287 (2018-09-29) Predicting the location of the non-local contacts in α-synuclein. Does not qualify: off topic.
22. 30206405 (2018-09-11) Accretionary prism collapse: a new hypothesis on the source of the 1771 giant tsunami in the Ryukyu Arc, SW Japan. Does not qualify: off topic.
23. 26243034 (2015-08-05) Dissipative Continuous Spontaneous Localization (CSL) model. Does not qualify: theory or hypothesis paper, no new data.
24. 26182086 (2015-07-02) Nonthermal Quantum Channels as a Thermodynamical Resource. Does not qualify: theory or hypothesis paper, no new data.
25. 25227991 (2014-09-17) Cerium; crystal structure and position in the periodic table. Does not qualify: off topic.
26. 23085151 (2012-10-19) Polypeptide chain collapse and protein folding. Does not qualify: review.
27. 22524589 (2012-04-23) Haemodynamic stability and pulmonary shunt during spontaneous breathing and mechanical ventilation in porcine lung collapse. Does not qualify: off topic.
28. 21488606 (2011-04-13) Effects of cake collapse caused by deposition of fractal aggregates on pressure drop during ceramic filtration. Does not qualify: off topic.
29. 21410235 (2011-04-06) Diverse pathways of oxidative folding of disulfide proteins: underlying causes and folding models. Does not qualify: review.
30. 18676658 (2008-08-01) Influence of liquid-layer thickness on pulmonary surfactant spreading and collapse. Does not qualify: off topic.
31. 18312272 (2008-02-26) Patterns of chromosomal fragmentation due to uracil-DNA incorporation reveal a novel mechanism of replication-dependent double-stranded breaks. Does not qualify: off topic.
32. 18216071 (2008-01-23) Observation of multiple folding pathways of beta-hairpin trpzip2 from independent continuous folding trajectories. Does not qualify: off topic.
33. 17552694 (2007-06-01) Effect of nuclei concentration on cavitation cluster dynamics. Does not qualify: off topic.
34. 17331539 (2007-02-07) Microsecond hydrophobic collapse in the folding of Escherichia coli dihydrofolate reductase, an alpha/beta-type protein. Does not qualify: off topic.
35. 16965059 (2006-08-01) A kinetic theory of tertiary contact formation coupled to the helix-coil transition in polypeptides. Does not qualify: theory or hypothesis paper, no new data.
36. 16241776 (2005-10-12) Testing gravity-driven collapse of the wave function via cosmogenic neutrinos. Does not qualify: proposal for a test, no data.
37. 15924487 (2005-06-01) Stability of microfabricated high aspect ratio structures in poly(dimethylsiloxane). Does not qualify: off topic.
38. 15698290 (2005-01-24) The alpha--> gamma transition in Ce: a theoretical view from optical spectroscopy. Does not qualify: theory or hypothesis paper, no new data.
39. 12956608 (2003-10-01) A first-order-like state transition for recombinant protein folding. Does not qualify: off topic.
40. 10756101 (2000-04-01) Hierarchical unfolding of the alpha-lactalbumin molten globule: presence of a compact intermediate without a unique tertiary fold. Does not qualify: off topic.

### orch-mass-time

Hits: 2. Screened: 2. Qualifying: 0.

1. 21209190 (2011-01-01) Role of prefrontal cortex in conscious visual perception. Does not qualify: new data (monkeys, response timing in a frontal area), but it does not measure how much brain tissue takes part.
2. 8528890 (1994-01-01) Blockade by interleukin-1-alpha of nitricoxidergic control of luteinizing hormone-releasing hormone release in vivo and in vitro. Does not qualify: off topic ("conscious" means awake rats).

### orch-coherence-time

Hits: 21. Screened: 21. Qualifying: 0.

1. 42988103 (2026-11-05) How many labels can a biological oscillator carry? A quality-factor screen for proposed information carriers. Does not qualify: a bound computed from two published quantities, no new data.
2. 42450355 (2026-07-07) Neuronal Microtubules and Radiofrequency Waves: The Quantum Core of Human Consciousness, Memory, and Pathway to Memory Enhancement/Recovery. Does not qualify: review.
3. 40826945 (2025-08-18) Old theory, new evidence: inhalational anesthetics disrupt a collective quantum state of intraneuronal microtubules to cause unconsciousness. Does not qualify: commentary.
4. 41713567 (2026-02-17) Feasibility analysis of the surface code model for the Orch-OR microtubule. Does not qualify: model or simulation, no new data.
5. 41539352 (2026-01-13) Relaxation effects in cell microtubule under the influence of an external electric field: The mean field approximation. Does not qualify: model or simulation, no new data (computes decoherence times theoretically).
6. 42920515 (2026-10-09) Dimensional convergence at the nanoscale: a novel synthesis of experimental evidence justifying direct measurement of quantum coherence in microtubules. Does not qualify: a synthesis of other groups' experiments.
7. 42643630 (2026-08-11) Transient entanglement in minimal open XXZ spin chains: a toy-model analogy for microtubule-inspired quantum biology. Does not qualify: model or simulation, no new data.
8. 42137636 (2026-04-29) Self-referential processing as the biological switch between classical and quantum functioning of the brain. Does not qualify: theory or hypothesis paper, no new data.
9. 41988526 (2026-03-31) Psychedelics and the quantum brain: a falsifiable hypothesis on Posner molecules and spin-dependent pharmacology. Does not qualify: theory or hypothesis paper, no new data.
10. 40999612 (2026-01-01) A Unified Model of Consciousness: Glycoprotein Patterns in Memory Processes and Quantum Entanglement. Does not qualify: editorial.
11. 41281348 (2025-11-19) On the potential of microtubules for scalable quantum computation. Does not qualify: review.
12. 40342554 (2025-05-06) A quantum microtubule substrate of consciousness is experimentally supported and solves the binding and epiphenomenalism problems. Does not qualify: review.
13. 39214493 (2024-08-28) On the possibility of implementing a quantum entanglement distribution in a biosystem: Microtubules. Does not qualify: model or simulation, no new data.
14. 24070914 (2013-08-20) Consciousness in the universe: a review of the 'Orch OR' theory. Does not qualify: the proponents' own theory paper (hameroff-penrose-2014).
15. 23091452 (2012-10-12) How quantum brain biology can rescue conscious free will. Does not qualify: review.
16. 19251667 (2009-02-26) Weak, strong, and coherent regimes of Fröhlich condensation and their applications to terahertz medicine and quantum consciousness. Does not qualify: theory or hypothesis paper, no new data.
17. 15555759 (2004-12-01) Does quantum mechanics play a non-trivial role in life?. Does not qualify: theory or hypothesis paper, no new data.
18. 12188753 (2002-06-10) Quantum computation in brain microtubules: decoherence and biological feasibility. Does not qualify: calculation (Hagan, Hameroff and Tuszynski 2002), no new data.
19. 11755497 (2002-01-01) Conduction pathways in microtubules, biological quantum computation, and consciousness. Does not qualify: theory or hypothesis paper, no new data.
20. 11684479 (2001-11-01) A quantum approach to visual consciousness. Does not qualify: theory or hypothesis paper, no new data.
21. 11088215 (2000-04-01) Importance of quantum decoherence in brain processes. Does not qualify: calculation (Tegmark 2000), no new data.

### orch-anaesthetic-mt

Hits: 267. Screened: 40. Qualifying: 3.

1. 42537979 (2026-07-31) On the functional significance of quantum effects at subneuronal scales. Does not qualify: theory or hypothesis paper, no new data (built from published measurements).
2. 42657234 (2026-03-19) Synchronized Chromatin Reorganization as a Key Biomarker in Anesthetic Effects on Plants. Does not qualify: plants; anaesthetic effects on cells, no unconsciousness.
3. 42958458 (2026-07-31) Esketamine induces ferroptosis and suppresses immune evasion in lung adenocarcinoma cells via the hsa_circ_0022392/miR-548b-3p/MAP7 axis. Does not qualify: off topic (cancer cells).
4. 42482521 (2026-07-21) Brain State Entropy as a Marker of Injury Severity and Sedation Effects Following Traumatic Brain Injury. Does not qualify: brain injury patients under sedation; no microtubule drug.
5. 42063249 (2026-07-01) Early Isoflurane Exposure Is Associated With Delayed Adolescent Neurobehavioral Deficits, Accompanied by Dysregulation of FOXG1 and EB3. Does not qualify: early isoflurane exposure and later behaviour; measures a microtubule protein, not unconsciousness.
6. 40826945 (2025-08-18) Old theory, new evidence: inhalational anesthetics disrupt a collective quantum state of intraneuronal microtubules to cause unconsciousness. Does not qualify: commentary, no abstract; no new data shown.
7. 41663006 (2026-02-07) Microtubule-stabilizer epothilone B counteracts anesthetic-induced slowed swimming in Tetrahymena pyriformis. Does not qualify: a single-celled organism's swimming speed; the test asks about unconsciousness in animals or people.
8. 41519196 (2026-01-08) Brain-penetrant microtubule-stabilizer epothilone B delays isoflurane-induced unconsciousness in mice. **Taken** as `huang-2026 (already in the records; still not opened)`.
9. 41687741 (2026-02-11) Single-cell transcriptomics reveals the mechanism of long-term neurodevelopmental toxicity following sevoflurane anesthesia. Does not qualify: later toxicity of sevoflurane.
10. 42920515 (2026-10-09) Dimensional convergence at the nanoscale: a novel synthesis of experimental evidence justifying direct measurement of quantum coherence in microtubules. Does not qualify: a synthesis of other groups' experiments.
11. 42770120 (2026-01-01) Hesperidin attenuates cisplatin-induced cardiotoxicity in rats through regulating autophagy. Does not qualify: off topic.
12. 42769438 (2026-09-14) Sevoflurane Inhibits Colon Cancer Progression by Inducing Cell Autophagy and Apoptosis through the ROS/Nrf2/P62 Pathway. Does not qualify: off topic.
13. 42643630 (2026-08-11) Transient entanglement in minimal open XXZ spin chains: a toy-model analogy for microtubule-inspired quantum biology. Does not qualify: model or simulation, no new data.
14. 42137636 (2026-04-29) Self-referential processing as the biological switch between classical and quantum functioning of the brain. Does not qualify: theory or hypothesis paper, no new data.
15. 40999612 (2026-01-01) A Unified Model of Consciousness: Glycoprotein Patterns in Memory Processes and Quantum Entanglement. Does not qualify: editorial.
16. 41406175 (2025-12-01) Sevoflurane Postconditioning Regulates Mitophagy Through the PINK1/Parkin Pathway to Alleviate Myocardial Microcirculatory Reperfusion Injury. Does not qualify: off topic (heart).
17. 41387721 (2025-12-12) Mitochondria are absent from microglial processes performing surveillance, chemotaxis, and phagocytic engulfment. Does not qualify: off topic.
18. 40576766 (2025-06-27) Hesperidin provides dose-dependent renal protection from cisplatin-induced injury, mediated by its regulation of Beclin-1 and LC3-II. Does not qualify: off topic (kidney).
19. 41057130 (2025-10-05) The study of beneficial effect and mechanism of propofol on TNF-α-induced p-Tau increase in HT22 hippocampal neurons. Does not qualify: propofol and tau in a cell line; no unconsciousness.
20. 40639436 (2025-07-08) KIF23 inhibition protects against perioperative neurocognitive disorders by hindering ROS/caspase-3/GSDME-mediated pyroptosis. Does not qualify: post-operative cognitive problems; not unconsciousness.
21. 40902546 (2025-09-02) Sevoflurane preconditioning improves Cx43 localization and electrical conduction by stabilizing myocardial microtubule structure during ischemia-reperfusion. Does not qualify: off topic (heart).
22. 40711457 (2025-08-01) Distinct Right Ventricular Performance in Response to Acute Colchicine Treatment in Healthy and Diseased States. Does not qualify: off topic (heart).
23. 40820533 (2025-06-01) [6-Shogaol alleviates cerebral injury after cardiac arrest-cardiopulmonary resuscitation in rats by inhibiting death-associated protein kinase 1-mediated autophagy]. Does not qualify: off topic.
24. 40455293 (2025-06-02) Synaptotoxic effects of extracellular tau are mediated by its microtubule-binding region. Does not qualify: tau and synapses.
25. 40287805 (2025-04-01) Investigating the Mechanisms of Esketamine in Treating Propofol-Induced Cognitive Impairment in Elderly Rats. Does not qualify: esketamine and propofol-related memory problems; not the dose or time to unconsciousness.
26. 40230274 (2025-04-01) The Role of the Sirt1/Foxo3a Pathway in Mitigating Myocardial Ischemia-Reperfusion Injury by Dexmedetomidine. Does not qualify: off topic (heart).
27. 40202105 (2025-04-01) Repeated Exposure to Sevoflurane in Neonatal Mice Induces Cognitive and Synaptic Impairments in a TTLL6-Mediated Tubulin Polyglutamylation Manner. Does not qualify: repeated neonatal sevoflurane and later cognition; not unconsciousness.
28. 39978568 (2025-02-18) Surface code model for Fibonacci helical pathways of the Orch OR microtubule. Does not qualify: model or simulation, no new data.
29. 40021968 (2025-02-28) Microtubule-modulating drugs alter sensitivity to isoflurane in mice. **Qualifies, not taken** (`li-2025`): a more recent study qualifies for this prediction and the method takes at most one per prediction.
30. 40017363 (2025-02-01) [Autophagy reduces bacterial translocation by regulating intestinal mucosal oxidative stress]. Does not qualify: off topic.
31. 41019231 (2025-09-13) Conscious active inference II: Quantum orchestrated objective reduction among intraneuronal microtubules naturally accounts for discrete perceptual cycles. Does not qualify: review.
32. 40342554 (2025-05-06) A quantum microtubule substrate of consciousness is experimentally supported and solves the binding and epiphenomenalism problems. Does not qualify: review ("Recent experimental evidence, briefly reviewed here").
33. 39322401 (2024-11-01) Propofol attenuates prostate cancer progression by upregulating TRHDE-AS1 expression, and METTL14 could mediate its m6A modification. Does not qualify: off topic.
34. 39344320 (2024-09-01) The Role of the SIRT1-mTOR Signaling Pathway in Regulating Autophagy in Sevoflurane-Induced Apoptosis of Fetal Rat Brain Neurons. Does not qualify: fetal neuron death.
35. 38849977 (2024-06-07) Inhalation of hydrogen gas mitigates sevoflurane-induced neuronal apoptosis in the neonatal cortex and is associated with changes in protein phosphorylation. Does not qualify: neonatal neuron death.
36. 39147581 (2024-08-29) Microtubule-Stabilizer Epothilone B Delays Anesthetic-Induced Unconsciousness in Rats. **Qualifies, not taken** (`khan-2024`): a more recent study qualifies for this prediction and the method takes at most one per prediction.
37. 39223886 (2024-07-01) [Anti-inflammatory mixture alleviates acute lung injury induced by sepsis in rats by modulating Beclin-1-mediated autophagy]. Does not qualify: off topic.
38. 38957242 (2024-06-02) Dexmedetomidine Inhibits Hippocampal Neuronal Damage Caused by Persistent Isoflurane-Induced Hypotension in Rat Model of Chronic Cerebral Hypoperfusion. Does not qualify: brain damage from low blood pressure.
39. 38701566 (2024-05-02) Sevoflurane postconditioning ameliorates cerebral hypoxia/reoxygenation injury in zebrafish involving the Akt/GSK-3β pathway activation and the microtubule-associated protein 2 promotion. Does not qualify: zebrafish brain injury.
40. 36414713 (2022-11-21) Ketamine impairs growth cone and synaptogenesis in human GABAergic projection neurons via GSK-3β and HDAC6 signaling. Does not qualify: ketamine and growth of neurons.
