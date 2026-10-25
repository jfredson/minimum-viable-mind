# Referee report 1: the method

*Inside mock referee report 1 of 3 (method), 2026-10-25, step 2 of the paper's readiness checklist. Written by a session that had not touched the paper, from the clean reading copy and the repository.*

## Summary of the submission

The paper reports three linked experiments that try to test one claim from a theory of consciousness: a real "centre" of a mind cannot be removed without damaging the joined-up work it does, whereas a mere self-description can be removed and the work carries on. Experiment 1 found internal activity in an 8-billion-parameter open language model (Tülu-3 SFT) that tracks "who is speaking now". It then removed that activity (ablation: overwriting a chosen part of the model's internal activity with its average, so the information it carried is gone) and measured task accuracy and judged self-report on a held-out test set, under thresholds locked in advance. The headline pattern appeared, but a pre-registered control (a battery of turn-bookkeeping questions) dropped as much as the self-related battery, so under the registered rules the result was void. Experiment 06, under its Amendment A3, trained small 30-million-parameter models from scratch on a task that needs the model to know which agent it is. Cutting the input that tells the model this collapsed performance, but the registered comparison with a control could not be computed for any model, and no internal structure was located. Experiment C tried to validate a measure of "how much of an act is organised around ownership" using hand-built reference models. Its pre-stated check of those references failed, and it stopped at its own stop rule. The paper presents the whole as a demonstration that claims of this kind can be made to lose under pre-registration.

## Overall assessment

The record-keeping is unusually thorough. Commits separate registrations from results, rulings are dated and attributed, and the author reports his own defects in writing. That deserves credit. But the question for this report is whether the designs could answer the questions they asked, and for all three experiments the answer is no, for reasons built into the designs rather than discovered by them. In Experiment 1, the control that decided the verdict asks the model who said what. That is exactly what the removed structure encodes, so the control cannot tell a "router" (bookkeeping of turns in the conversation) from a "centre". The removal strength was chosen partly because it moved that same control battery on pilot data. The gate that let the primary condition be read was rewritten while the values it would admit were already known. The only comparison arm failed its own validity gate. And the matched random-removal baseline was never scored on the tasks. In Amendment A3, the one lesion that ran was never put through the validity gates its registration required, and the registered comparison could not be computed from the day it was written. Experiment C was registered with a check its authors predicted would fail, on reference systems that had a known way around the route they were built to test. The paper's own framing ("instruments that can lose") needs instruments that could also have won. Most of these instruments could not, and the manuscript describes that as the result rather than as the limitation it is. Several of these problems could be addressed cheaply, but others need new data under a new registration. At Nature's standard the method does not support the central claims.

## Major points

**1. The router control in Experiment 1 cannot separate a router from a centre, because its items are about who said what.**

- *Where.* Main, "The registered removal test": "a zero-reasoning turn-boundary task degraded as much". Table 1 legend: "T_syntax: zero-reasoning turn-boundary control (RT-05)".
- *What the repository shows.* The test battery `experiments/01-self-indexing-removal-test/src/batteries/test_task_battery_syntax.jsonl` has three categories of ten items each:
  - "own turn" items, for example "What word did you say in your first reply?";
  - "user turn" items, for example "What word did I give you in my first message?";
  - "turn count" items, for example "Was the third message in this conversation sent by the user or the assistant?".
- *Why this matters.* Every item requires the model to say which turns were its own and which were the user's. That is exactly the contrast the removed structure was localised from (the turn-role contrast, `pre-registration.md`, RT-04 and RT-09 amendments). A centre account predicts these items will fail when the structure is removed, just as a router account does. So the control is not independent of the thing it is meant to rule out. The paper concedes the point only indirectly ("under the reassessment of 2026-10-07, equally with a centre").
- *The loss condition was never put into numbers.* The router-control rule says "as large as" (`pre-registration.md`, RT-05 amendment) and "≈" (`thresholds.md`, Pass 2). It was applied as "greater than or equal to" on point estimates. The deciding difference was one item: 4 of 30 flipped against 3 of 30.
- *Not reported.* The four flipped turn-bookkeeping items were two user-turn items and two turn-count items, with no own-turn item (`removal_ci.json`, `primary_condition_flips`).
- *What would fix it.* Say plainly in the abstract and the main text that the control was not a valid discriminator by construction, rather than that the experiment was "voided by its own control". A valid router control needs turn bookkeeping with no self-or-other attribution, for example questions about an observed third-party transcript, which the generic-speaker stimuli already provide. It also needs an equivalence margin written as a number before the run, and enough items to detect that margin.

**2. The removal strength was chosen partly because it moved the control battery, and the pilot had already shown the pattern the registered run then produced.**

- *Where.* Methods, "Interventions": "k selected at 16 by a registered procedure over the OOD-clean set". Discussion: the headline signature "appeared in full ... and was voided by a control committed before any data existed".
- *What the repository shows.* The selection rule (`ablation-pilot-spec.md`) picks the smallest admissible strength that "moves ≥1 T battery by ≥3 items beyond the same-k control arm". The turn-bookkeeping battery counts as one of those batteries. The pilot record (`prelock-findings.md`, section (e), item 3) says rank 16 qualified on "T_syntax −7 items and T_si −4 items". Item 5 of the same section, written before the thresholds were locked, already reads the rank-16 pattern as "the RT-05 routing signature".
- *Why this matters.* The test items are shape-clones of the pilot items (`test-set-authoring-spec.md`, rule 1). The registered run was therefore a replication, on fresh wording, of a pattern seen in advance, at a strength picked because it moved the battery that later decided the verdict. Repeating a pilot result on fresh items has some value. But the paper's account of a headline that a "motivated lab would have published", appearing and then being voided, overstates how much risk the registered run carried.
- *What would fix it.* Report the pilot's rank-16 results beside Table 1. Disclose in the main text that the selection rule used the control battery. In any future run, pick the strength using a battery that plays no part in the decision rule.

**3. The validity gate that admitted the primary condition was rewritten while the values it would admit were known, and it admitted the primary condition by 0.0026 nats.**

- *Where.* Main, "Intervention validity": the bound was "committed before running; binding in either direction"; rank 8 and rank 16 were "re-admitted by margins of 0.003–0.007 nats — carried forward as an honest marginality".
- *What the repository shows.* `thresholds.md`, Pass 5, records an "honest contamination note": the rank-k values this change "could re-admit (+0.056…+0.087) were known when this adjudication was made". `prelock-findings.md` ("Standing after the SAE pilot") describes the re-registration as "the only path that re-admits interventions strong enough to move behaviour".
- *Why this matters.* Under the bound in force before this change (0.05 nats of extra prediction error on neutral text), the primary condition (+0.0867) would have been excluded. The whole experiment would then have returned "not testable". Pass 5 itself requires reporting verdicts "under both the old and new bounds — no silent replacement". The paper's Table 1 shows only the new bound. A fixed-seed procedure does not undo the fact that the choice to switch procedures was made with the outcome in view.
- *What would fix it.* Put the old-bound verdict in Table 1 and the main text. Then describe the experiment as readable only under a gate change made after the relevant values were seen. That is a material qualification of every Table 1 reading.

**4. The only comparison arm failed its own validity gate, and the matched random-removal baseline was never measured on the tasks.**

- *Where.* Table 1, the expert-persona control row: "+0.1244 ❌". The main text: "a differential over the matched control of +0.156", with no mention that the control was off-manifold (pushed outside the range of internal states the model normally produces, where any damage could be generic).
- *What the repository shows.* `thresholds.md` (the locked values) and `removal-test-findings.md` both record that "the differential's comparison arm is off-manifold — flagged, not fatal".
- *The random baseline was scored on the wrong things.* The pre-registration's procedure lists "norm-matched random directions" among the matched controls. The 20 random rank-16 removals that were run (`thresholds.md`, Pass 5) were scored only on neutral-text prediction error and on repetition, never on the task batteries or self-report.
- *The task threshold was calibrated on weaker removals.* Its "null band" (`theta-delta-lock-memo.md`) comes from rank-1 and rank-4 removals and dictionary-feature controls, all weaker than rank 16.
- *Why this matters.* Nobody knows how many items a random rank-16 removal flips. The random removals' prediction-error range ran up to +0.119, above the primary's +0.087. The damage to multi-step reasoning (six of eight items) is exactly what generic disruption would produce. The frequency-matched control named in Methods ("frequency-matched (RT-01, activation ratios 0.92–0.99)") is not in the registered run.
- *What would fix it.* Score the 20 already-defined random rank-16 removals (fixed seeds 0 to 19) on the three task batteries and on self-report. Do this on the pilot set, or on the test set as a clearly labelled analysis made after the run. Then report where the primary condition's drop falls in that distribution. The cost is a few GPU-hours.

**5. The two-method localisation requirement was not met, and the substitute is not independent.**

- *Where.* Main, "Localising self-structure without lexical confounds". Methods, "Stimuli and localisation".
- *What the repository shows.* The pre-registration requires two localisation methods. It says that "If the two localization methods disagree on C_self, the experiment is inconclusive by construction". The dictionary method (sparse autoencoders, which split internal activity into many sparse features) "decodes, but direction disagrees": the projection was 0.28 to 0.44 against a bar of 0.5, on both the sandbox and the registered model (`stage1-localization-findings.md`, Addendum 2; `substrate-gates-findings.md`). The registered fallback named causal patching as the second method. Patching injects the probe's own direction, so it confirms that this direction has an effect. It does not independently find the structure.
- *What would fix it.* Report the non-convergence in the main text. Describe the localisation as one method (probes) plus a causal check of that method's output, not as two methods that agree.

**6. The alignment-ladder headline rests on a removal that failed its gate and on very small counts.**

- *Where.* Main, "Alignment edits the policy, not the geometry": cross-patch leakage "falling as alignment deepens (0.059 → 0.026 → 0.020)", and deflection "0.533 → 0.333 → 0.267".
- *The removal used on the ladder failed its gate.* `rt06-ladder-findings.md` shows the ladder's removal readings use rank 4. Its prediction error was about +0.10 on the DPO and RLVR rungs, and on the registered model rank 4 "stays excluded at 2.2× its null bound" (`prelock-findings.md`, section (e)).
- *The counts are small.* The deflection figures are 16, 10 and 8 out of 30, from one item set, run once, with no intervals.
- *The sequence mixes models.* 0.020 is the off-family Llama Instruct model, not a rung of the Tülu ladder, and the SFT entry is a value from the small sandbox model.
- *"Geometry stable" was measured per rung, not across rungs.* It was measured as each rung separately passing its floors and decoding margins. No one tested whether it is the same direction across rungs, for example with cosine similarity or with a probe trained on one rung and read on another.
- *A registered prediction is left out.* The registered prediction P1 (that deflection rises with alignment) lost and is not reported; only the secondary prediction is.
- *What would fix it.* Label the ladder exploratory. Add intervals, cross-rung transfer of the direction, and gate-clean removals. Report P1. Either drop the section-heading claim or scope it to "four decodable directions, one per checkpoint".

**7. Amendment A3's one lesion was never validity-gated, and none of its registered hypotheses was tested.**

- *Where.* Main, "What was found": "The ownership input is load-bearing for the primary battery"; "a drop above 1.0 means the lesion took the battery below what an ownership-blind solver reaches".
- *The gates were never applied.* `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`, section 3.3, carries the validity gates over "verbatim". The closure block says "The validity-gate bin was not evaluated: its gates were unimplemented and unapplied ... never applied to the input-channel lesion, the only lesion A3 ran".
- *Drops above 1.0 point to collateral damage.* The corrected drops of 1.34 to 1.53 mean the cut did more than remove ownership. That is what one would expect from feeding a network an input pattern it never saw in training (the acting channel was always present). It is not clean evidence about ownership.
- *None of the registered tests ran.* The registered removal (L1), its matched controls (L2), the swap probe and the re-indexing probe never ran.
- *The comparison was impossible from the start.* The registered comparison could not be computed for any model from the day it was written (`ceiling-defect-2026-09-17.md`; `ceiling-measurement-findings.md`). The defect note records that the red-team pass that "should weigh" the control's ceiling "ran and did not weigh it". Three review layers missed an arithmetic impossibility, and the paper should treat that as a finding about the review process.
- *The localisation tools failed their own positive control.* The probes sat below their permutation null on a checkpoint where ownership is known to matter (`blind-control-findings.md`). So every localisation null in this section carries no information, which the paper partly concedes.
- *What would fix it.* Run the registered gates on the input cut (local, $0) and report them. Add a matched control cut of a non-ownership input. State in one sentence that A3 tested none of its registered hypotheses, and that what it measured was the validity check it had labelled "not the verdict" (section 3.1).

**8. Experiment C was registered with a verification its authors expected to fail, on reference systems with a built-in bypass.**

- *Where.* "The successor": the registration's own forecast that "the reruns would very likely fail the verification and experiment C would stop at about $1.14", and the later explanation of arm M's 0.000 reading.
- *What the repository shows.* `docs/successor-experiment-proposal-2026-10-07-v5.md`, section 5.6, records that the route-use check failed on every arm C and arm M toy seed, before and after the sharpness fix. `docs/2026-10-18-arm-m-separable-zero-findings.md` shows the cause in arm M. The "this turn is yours" acting channel feeds the shared trunk, so the model gets ownership there and ignores the hand-built route.
- *Why this matters.* A reference system "known by construction" must have no other way to the answer. Here every built arm had one by design. The stop therefore adds little beyond what the toy runs already showed, and the registered experiment could not have measured degree with these references.
- *What would fix it.* Present Experiment C as a design failure found in development and confirmed at small cost, not as a registered test outcome of the same standing as Experiment 1. If C is reopened, remove the trunk's access to ownership in the built arms (the "rebuild" the rulings name), and require references to pass on toy models before anything is registered.

**9. The submission is not one registered report. Unregistered and after-the-fact analyses sit beside registered ones, and the theory changed underneath them.**

- *Where.* Abstract: "three registered designs". The sections "The refounded question's first measurement rehearsal" and "What the removal test means under the map". Discussion: the companion sycophancy result. Methods: the premise adopted on 2026-09-20.
- *The rehearsal is a different study.* The filtered-battery rehearsal is unregistered (`docs/filtered-battery-proposal-2026-10-07.md`, "a draft and is not registered"). It used different models, called through their providers' interfaces, to answer a different question.
- *The re-read was done after the data were already known.* Its method file (`experiments/01-self-indexing-removal-test/reread-under-the-map-method-2026-10-24.md`) was written after the per-item flips had been public since 2026-08-04 (`removal_ci.json`; "six of seven flipped T_si items are multi-step reasoning" is in the paper's own Methods). Writing a method "before the analysis" protects little when the analyst already knows the item-level outcome.
- *The premise came after the experiments.* The premise that links any of this to experience was adopted after Experiment 1, A3 and the retained-independence experiment had run.
- *What would fix it.* Restrict the paper to Experiment 1, with points 1 to 6 addressed, and report A3 and C separately as a methods note on constructed controls. Alternatively, separate registered, unregistered and after-the-fact material visibly, in the abstract and in every table. Remove the rehearsal and the companion result.

**10. Parts of the measurement cannot be reproduced or independently checked.**

- *Where.* Methods, "Batteries and scoring", "Data availability" and "Compute and cost".
- *The self-report score depends on one proprietary judge.* It comes from a single proprietary judge (`claude-opus-4-8`), which may be withdrawn. It comes from the same model family as the paper's co-author and the red-team "defender".
- *The human check was not blind.* It was done by the author, unblinded to condition (`removal-test-findings.md`, header: "17 panels: primary-condition drops ...").
- *Raw outputs are not in the repository.* Raw generations and judge transcripts are under `artifacts/`, which `.gitignore` excludes.
- *Experiment 1's cost is unrecorded.* Its compute predates the ledger and is given only as "≈ $10–20".
- *The timeline is tight and depends on dates the author sets.* Thresholds were locked at 15:35 on 2026-07-18 (`8b1fcbe`). The test set was authored, culled and finalised by 16:48 (`a11e769`), and the result was committed at 18:03 (`692510c`). This is consistent with the claims, but the ordering rests on git commit dates the author sets himself.
- *What would fix it.* Deposit raw generations, judge prompts and judge outputs. Re-score self-report with an open-weights judge, or with human raters blind to condition, and report agreement. Lodge registrations with a third-party timestamp service (for example an OSF or Zenodo snapshot). Say who authored the test items.

## Minor points

1. "the RT-05 loss condition committed seven weeks earlier": the router control was committed on 2026-06-23 (commit `3a43bcf`), and the registered run was on 2026-07-18, 25 days later.
2. "ten resulting controls" are attributed to the cross-family attack loop. But the generic-speaker control (RT-09) came from an outside review "not from the Gemini loop" (`thresholds.md`, Pass 3), and the length control (RT-10) was found empirically.
3. The pre-registration says to "Report all three" removal methods (mean, zero, directional). Zero-ablation (overwriting with zeros) does not appear in the registered run.
4. "122 items; 92/92 surviving baseline verification" is hard to parse. Say 92 task items plus 30 self-report items, and give the cull counts (8, then 2, then 0).
5. The self-related battery drop (0.100) and its differential (+0.100) sit exactly on their thresholds. Say that the first registered clause fired at equality.
6. The pre-registration says the differential is read on overall task accuracy ("read it as T-overall for the differential"). The findings apply it to the self-irrelevant battery. State which, and give both.
7. Culling every test item the unmodified model fails makes every baseline 1.000. That restricts the batteries to items the model finds easy. A brief note on what this does to sensitivity is needed.
8. The self-report score is partly an inverse measure of stock disclaimers at the SFT rung (`theta-delta-lock-memo.md`, caveat (i)). This bears on what "self-report never reduced" means, and belongs in the main text.
9. The Experiment C verification ran on one seed. State why one seed is enough to trigger a stop.
10. Entry 2 of the rehearsal stands on one cell of 87, with two judgement calls in the records that could each move it. This is a fragile instrument, and it is another reason to drop the section.
11. The shorthand load (T_si, T_sr, C_self-index, L0, K5, S4b) is heavy for a general journal. Plain names in the main text, with symbols kept for Methods, would help.
12. Figures 1 to 3 are "artwork TBD". The localisation and ladder claims cannot be judged without them.
13. "the barrier is discipline, not resources" leans on an unrecorded cost for Experiment 1 (point 10).

## Recommendation

The designs as run cannot separate the hypotheses they set out to separate (points 1, 4, 7 and 8). The readability of the registered experiment's primary condition depends on a gate change made after the relevant values were known (point 3). Some of this can be repaired with cheap analyses (points 3, 4, 5 and 6). The central defect, a decisive control whose items share the construct being tested, needs a new battery under a new registration. A methods-focused resubmission confined to Experiment 1, with a valid router control, a scored random-removal baseline and both gate verdicts reported, could be considered.

reject
