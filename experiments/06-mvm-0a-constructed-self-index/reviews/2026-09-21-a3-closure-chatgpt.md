Model: ChatGPT 6 Astra Medium
Date: 2026-09-25
Mode: documents shown, lookup allowed

All 22 files arrived and were read in full. No supplied part appeared truncated.

**Review date:** 2026-09-25, Pacific. **Reviewer:** Codex; exact model version and app mode were not exposed in the supplied context. No external lookup or model execution was used. **MEASURED** below means a quotation, number, or arithmetic relationship checked against the supplied documents; it does not mean that I reproduced an experiment.

**My conclusion:** A3 has a sound basis for closing as *not testable*. Version 4 repairs the six principal problems identified in version 2, but several serious defects remain. I found no new fatal defect in the decision to close. I would revise the text before registration, and the required reviewer-owned closure checks remain a separate condition of registration.

For citations below, `E/` abbreviates the repository directory `experiments/06-mvm-0a-constructed-self-index/`.

## Part 1 — Feasibility

| Finding | Severity | Basis |
|---|---|---|
| A1 — The principal measurements and the registered outcome wording are supported | Worth-noting | MEASURED |
| A2 — The powered sweep’s two targets are incorrectly described as two arms reading the marker word | Serious | MEASURED |
| A3 — The money paragraph preserves figures superseded by its own supplied correction | Serious | MEASURED |
| A4 — The successor’s October 11 target is no longer operative in the cited ruling | Serious | MEASURED |
| A5 — Some verification records were not supplied; the packet cannot establish their contents or completion | Worth-noting; packet limitation | MEASURED |

### A1 — The central numerical record holds

The following checks pass:

| Closure claim | Check against the supplied record |
|---|---|
| Three training seeds; intact primary scores 0.5683, 0.5633, 0.5738; lesioned scores 0.1988, 0.2015, 0.1447 | All six appear in `E/seeds-endpoint-findings.md`. |
| Six evaluation seeds, with intact and lesioned readings paired | Explicitly stated in that file’s method notes. |
| State drop 0.0769 on seed 2, below 0.1172; syntax unchanged | Both numbers and zero syntax drops appear in that file. The state figure is a corrected drop, not raw accuracy points. |
| Control ceiling 1.0 | `E/ceiling-measurement-findings.md` reports two ownership-blind solvers scoring 1.0000 over 4,000 episodes. |
| The registered control drop cannot be computed for any model | The cited floor rule requires `baseline − ceiling ≥ 0.10`. With ceiling 1.0, this requires accuracy 1.10. This arithmetic holds. |
| Diagnostic pilot 0.3125 against a pre-stated 0.60 boundary | Both appear in `E/control-learnability-pilot-findings.md`; the compute-ledger pilot row also records the pre-stated boundary. |
| Eleven positions and five layers for the fitted own-index sweep | Supported by `E/fitted-position-sweep-findings.md`. |
| Third checkpoint, other agent’s revision value, layer 3 | Supported by `E/standardised-refit-findings.md`. |
| Margin equivalent to 1.94 episodes in 4,000 | `E/red_team_ledger.md`, RT-128, gives 0.000484 accuracy; multiplying by 4,000 gives 1.936. This is an equivalent accuracy margin, not a count of identifiable episodes. |
| Rough reach of one episode in eleven | Explicitly supplied by `E/fitted-position-sweep-findings-CORRECTION-2026-09-20.md`. Its application needs the qualification in A14 below. |
| Marker-word fitted read deferred at approximately seventy processor-hours | Supported by `E/red_team_ledger.md`, RT-89 and the surrounding ruling. This is an estimate, not the measured duration of a completed run. |
| Patching and re-indexing never run; no A3 patching implementation | Supported as recorded findings by `E/red_team_ledger.md`, RT-96 and RT-114. |
| Validity gates unimplemented and unapplied | Supported by the supplied F17 in `E/red-team-a4.md`. |
| Other-agent control’s lesion half unavailable | Explicitly stated in `E/red_team_ledger.md`, RT-142. |

The pilot’s “quadrupled weight” is supported if it means **per-row gradient weight**. The supplied findings describe a separate loss term at double weight, combined with changed sampling. Using the more precise phrase would prevent confusion about the actual setting.

The requested registration quotation is:

> No non-self cross-turn control can be built that is state-requiring at ceiling — then the differential discriminator is dead here and the honest report is “not testable” [RT-05].

That is the final loss condition in `E/pre-registration.md`. The closure quotes it accurately. The supplied ledger also records John’s application of it to A3. The distinction between that ruling and what the ceiling calculation itself proves matters, however; see A6.

### A2 — The 270 tests did not all read the marker word

The closure says the model’s marker word was read by a method:

> “which found it nowhere on either of its two arms across 270 tests”

But `E/powered-position-sweep-findings.md` names the arms separately:

- Arm 1 reads the model’s **marker word**.
- Arm 2 reads the **register index**.

Each has nine discovery positions × five layers × three checkpoints = **135 discovery tests**. The 270 total combines two different targets. Moreover, the positive-control positions did produce detections, so “nowhere” needs its discovery-position restriction.

This is a defect in the text, not missing evidence: the supplied record explicitly distinguishes the targets.

**Replacement:**

> The difference-of-averages sweep found no discovery-position clearance for either target: 135 tests read the registered marker-word target and 135 read the register index. Positive-control detections occurred where the answer was supplied by the input token (`powered-position-sweep-findings.md`).

### A3 — The correction must enter the block that will be registered

The money paragraph gives approximately $44.3 for A3 and $225.7 for the programme. The supplied `E/compute-ledger.md` subsequently records a measured account reduction of:

`$79.7159 − $77.8119 = $1.9040`.

Its corrected totals are approximately **$46.2** and **$227.6**. The later rehearsal row retains those totals at the ledger’s reporting precision.

The note beside the closure acknowledges this. That is useful disclosure during review, but it expressly says it is **not part of the closure text**. It therefore does not repair the block that will become permanent.

The approximately $44.3 figure may describe spend at the earlier decision to close. That does not justify leaving the accounting date implicit, particularly when the block also reports work completed afterward.

**Replacement:**

> As of the compute ledger’s 2026-09-21 rehearsal entry, approximately $46.2 was counted against A3’s $100 stop and approximately $227.6 against the programme’s $400 ceiling, including $1.904 spent on the refused rented-machine attempts (`compute-ledger.md`).

The supplied excerpt supports those reported totals and the incremental arithmetic. It does not permit independent reconciliation from the beginning of the programme.

### A4 — The cited ruling withdraws the October 11 pacing target

The closure states:

> “registration commit target 2026-10-11”

The complete supplied `docs/rulings/2026-09-20-december-result-roadmap.md` includes a later annotation saying:

> “the registration commit target of 2026-10-11 in item 1 was pacing, so it goes with the calendar”

The kill dates remain unchanged. The closure cites an earlier paragraph while missing a qualification later in the same file. The record was supplied and contradicts the current presentation.

**Replacement:**

> The successor proceeds through Gate A with both tiers as soon as its prerequisites are complete. The operative deadlines remain registration by 2026-10-18 and launch of the registered runs by 2026-11-01; missing either is recorded as a schedule failure (`docs/rulings/2026-09-20-december-result-roadmap.md`, including its 2026-09-21 annotation).

### A5 — What this packet does not independently establish

The following distinctions should remain explicit:

- The supplied `docs/outside-review-protocol.md` excerpt contains the **closure rule**, but not the measurement-rehearsal section the closure cites. The rehearsal requirement is corroborated by item 6 of the supplied December-result ruling; its detailed protocol wording was not shown.
- The original 2026-09-16 blind-run findings were not supplied. The supplied reconciliation establishes **John’s disposition of the arm**, not an independent check of the run’s execution.
- The control pilot’s original pre-statement, `E/control-learnability-pilot.md`, was not supplied. Its timing and boundary are corroborated by the findings, ledger and prior reviewer’s account.
- The required final reviewer-owned closure verification was not supplied. The ledger says that check is owed.
- The full compute ledger and Git history were not supplied, so I cannot independently verify complete expenditure or commit availability.

These are packet limits, not evidence that the underlying claims are false. The excerpts expose significant adverse evidence, including the unimplemented gates and corrected spending. I found no demonstrated selective omission that reverses a conclusion, although the missing protocol section limits the claimed completeness of the packet.

## Part 2 — Satisfied by the wrong thing

| Finding | Severity | Basis |
|---|---|---|
| A6 — Failure of the registered metric is presented as proof that the control itself cannot be built | Serious | ARGUED from checked text and arithmetic |
| A7 — The accepted question about hard kill K5 remains unanswered | Serious | MEASURED |
| A8 — “Excluded the exclusion confound” still exceeds the supported scope | Serious | ARGUED from checked records |
| A9 — The principal repairs to version 2 are present, but acceptance is not verification | Worth-noting | MEASURED |

### A6 — Separate an impossible comparison from an impossible task

The ceiling calculation decisively establishes that the **registered comparison is unusable**.

It does not establish, by itself, that no ownership-free, state-requiring control can be built. Indeed, a task that requires looking back through named agents’ assignments can require cross-turn information and still be perfectly solvable without ownership. A ceiling of 1.0 is compatible with that task requirement.

The supplied `E/ceiling-measurement-findings.md` supports the structural argument under an explicit restriction:

> “Any control that is fully determined by the visible episode and does not require ownership…”

Within that setting, a correct ownership-blind solver can attain 1.0, leaving no positive margin for this metric. The defect is the pairing of the control with the denominator and floor rule.

The closure should not turn that into an unrestricted impossibility claim about ownership-free controls, or imply that changing the grammar alone repairs it. There is also an unresolved consistency issue in the cited findings: they call the state battery ownership-free while assigning it a ceiling of 0.0676. The meaning of “ceiling” cannot silently shift between an optimal ownership-blind solver and a more restricted reference solver.

John’s ruled outcome can stand without overstating the mathematical proof.

**Replacement:**

> John applied the registered loss condition and ruled the outcome “not testable.” The demonstrated obstruction is that this control’s ownership-blind ceiling is 1.0, making its drop inadmissible under the registered metric for every possible model. The same obstruction applies to any deterministic ownership-free control fully answerable from the visible episode under that definition of ceiling.

For the successor, add:

> A successor must demonstrate both its control ceiling and a usable comparison metric; measuring the ceiling alone does not resolve this defect.

### A7 — K5 is still neither triggered nor explicitly left untested

The inside review’s RT-164 asked for an explicit disposition of:

> **K5.** Probe-patching convergence fails on all three seeds: *not testable (localization)*, reported as such; no further seeds.

The ledger says this was addressed in version 3. Version 4 still does not name K5 or say whether it fired.

“Because the two instruments never converged” does not resolve the ambiguity. One instrument was never run. Failure to establish convergence is not automatically a measured failure of convergence.

Section 3.2 supplies a sufficient basis for saying localization was **not established**. K5 additionally names an event across all three seeds and imposes a consequence. The closure must distinguish them.

A defensible replacement, subject to John’s explicit ruling, is:

> Localization was not established under §3.2 because causal patching was never implemented or run. K5’s three-seed convergence test was therefore not completed; this closure does not report a measured K5 failure. A3 closes under the separately ruled loss condition, with no further A3 seeds scheduled.

If John instead rules that non-execution satisfies K5, record that interpretation expressly. Do not let the sentence imply that both instruments ran.

### A8 — Narrow the confound conclusion to what was tested

Version 4 improves the earlier wording by retaining the relational-encoding alternative. Nevertheless, it first says that the probe half:

> “excluded the exclusion confound”

The supplied `E/other-index-position-sweep-findings.md` reports that a particular fitted classifier did not decode agent B’s four-way rank at the relevant position. The ledger’s RT-125 expressly carries a relational route that could produce the own-index pattern and the other-index null together.

The positive controls and RT-126’s effect-size argument strengthen the result against the specified account. They do not establish that every representation capable of supporting exclusion would be recoverable by this classifier at this position.

**Replacement:**

> The probe half did not support the proposed explanation based on a linearly decodable four-way representation of the other agent’s rank. It did not exclude relational, nonlinear or distributed representations that this probe would miss; the relational route remains open.

This preserves the useful comparison without allowing a null on one target to become a mechanism-level exclusion.

### A9 — The earlier fatal defects have mostly been repaired in the text

The six principal version-2 findings now have visible textual responses:

- The endpoint paragraph names its source.
- The patching claim cites RT-96.
- The successor ruling is supplied, although its later schedule annotation creates A4.
- The two senses of “center” are distinguished.
- Only the **probe half** of the other-agent control is described as run.
- The standing interpretation is explicitly **instrument failure, not absence**.

These repairs deserve credit. I would not reissue the six findings merely because the previous reviewer called them fatal.

However, `E/red_team_ledger.md` explicitly says that reviewer-owned verification is owed. The supplied closure rule requires a fix commit and a reviewer’s measured check, not just agreement with the wording. This outside document review cannot certify that procedural condition as complete.

## Part 3 — No verdict

| Finding | Severity | Basis |
|---|---|---|
| A10 — Administrative discharge of the blind arm must not imply successful sensitivity validation | Serious | MEASURED and ARGUED |
| A11 — The open-item list omits operative decisions that explain why work remains undone | Serious | MEASURED |
| A12 — The headline incorrectly suggests that everything measurable without the comparison was measured | Serious | ARGUED from checked text |

### A10 — “Discharged” and “validated” must remain separate

The closure correctly says the localization stack has not been shown able to recover the relevant structure on this design. It then calls the blind arm:

> “the measurement that would establish it”

and says that arm was discharged.

Read quickly, this sounds like a completed validation immediately following a claim that validation never happened.

The supplied `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md` is clearer: the arm is administratively discharged, while the sensitivity requirement remains unmet and moves to the successor’s rehearsal.

Also, merely running a blind arm would not establish sensitivity. It would need an appropriate known-present target and a successful recovery.

**Replacement:**

> John ruled the 2026-09-16 blind arm discharged, so it does not block this closure. That disposition does not establish successful recovery of an acquired ownership representation on the A3 design. The unmet sensitivity requirement carries into the successor’s rehearsal.

The successor must validate its own instruments and substrate. Success there would not automatically validate the historical A3 probes or retrospectively convert their nulls into findings of absence.

### A11 — Carry the decisions, not just the unfinished jobs

The open-item paragraph names important unfinished work, but it does not consistently say whether each item is deferred, unavailable, prohibited pending a new ruling, or assigned to the successor.

Two supplied rulings should be carried explicitly:

1. `docs/rulings/2026-09-20-december-result-roadmap.md`, item 2, says **patching is not built for A3**; it is built for the successor, and A3 closure does not wait for it.
2. `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, item 3, says **no further work on the other agent’s revision-value position is authorised**.

Simply listing “causal patching, unwritten and unrun” and “relational-encoding route … untested” does not convey those decisions. A future session could reasonably treat them as active A3 tasks rather than recorded limitations.

**Add:**

> Patching is not scheduled for A3; the December-result ruling assigns its construction to the successor. No further investigation of the other-agent revision-value position is authorised under the follow-up ruling. The marker-word fitted read remains deferred, and whether it runs before the paper remains undecided. These limitations do not imply that the missing measurements have been satisfied.

K5 should receive its own explicit disposition as requested in A7.

### A12 — The headline claims too much completion

The headline says:

> “what the experiment could measure without it was measured on three seeds”

The body then identifies several measurements that were not made: sensitive marker-word probing, patching, re-indexing and validity gates. Some required new implementation; others were feasible but deferred. None is accurately covered by an assertion that everything measurable without the comparison was measured.

The three-seed evidence is valuable without claiming exhaustion.

**Replacement headline:**

> **Outcome: not testable — the registered comparison was undefined for every possible model. Separately, removing the ownership-input channel reduced primary-battery accuracy on all three trained seeds.**

This states the outcome and the result while leaving the unfinished work visible.

## Part 4 — Over-reading

| Finding | Severity | Basis |
|---|---|---|
| A13 — The gradient paragraph needs the inherited limits on experience and the same-act claim | Serious | MEASURED and ARGUED |
| A14 — “These probes,” “this target,” and one-in-eleven combine results with different targets and sensitivities | Serious | MEASURED and ARGUED |
| A15 — Several remaining phrases invite stronger readings than the records support | Worth-noting | MEASURED and ARGUED |

### A13 — “Above zero” is a theoretical classification, not a measured degree

Version 4 now identifies the weaker definition of “center” and dates the ruling. That repairs the direct ambiguity identified by the inside reviewer.

But a public reader can still read “these checkpoints [are] above zero” as evidence of a minimal mind or experience. The supplied center-as-degree ruling makes that association particularly salient by using “thin inside.”

The original registration explicitly withholds both experience claims and a demonstration of its same-act requirement. It says every write-up must state the latter limit. “Degree unmeasured” does not state either restriction: it can sound like a positive amount has been established and only its size remains unknown.

**Add to the gradient paragraph:**

> “Above zero” is the project’s classification under its 2026-09-20 definition of a load-bearing input, not a measured integration score. A3 does not establish that binding specifies its center in the same act, and it provides no licensed verdict about consciousness or experience.

The public sentence would be stronger as:

> Removing the ownership-input channel reduced primary-battery accuracy on three trained seeds. The matched comparison was unavailable; whether an acquired internal ownership structure exists was not established, and integration degree was not measured.

The theoretical classification can follow, expressly attributed to the ruling.

### A14 — The heuristic reach belongs to particular probes and targets

The localization summary says:

> “these probes did not localize this target … at a heuristic reach of roughly one legible episode in eleven”

By that point, the text has discussed:

- Fitted decoding of the own register index.
- Fitted decoding of the other-agent index.
- Difference-of-averages decoding of the marker word.
- Difference-of-averages decoding of the register index.

Those are not one target under one sensitivity estimate. The cited correction concerns the fitted **register-index** read. It cannot supply measured or heuristic sensitivity for a fitted marker-word read that never happened.

Even for the fitted read, one-in-eleven depends on transporting performance at an easy positive-control position to other positions. Calling it heuristic is correct; calling it the reach of “these probes” obscures its restricted basis.

**Replacement:**

> The fitted register-index read had a heuristic reach of approximately one episode in eleven, calculated using its positive-control accuracy. This is not measured detection power at the discovery positions and does not establish the sensitivity of the unrun fitted marker-word read (`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`).

### A15 — Small wording changes would prevent recurrent over-reading

These are not independent reasons to reject the outcome, but they matter in a permanent account.

| Passage | Likely reading | Suggested wording |
|---|---|---|
| “That bin did not fire, and it was also never tested” | The lesion avoided invalidity | “The validity-gate bin was not evaluated: its gates were unimplemented and unapplied.” |
| The control ceiling “was itself never attacked” | No control attack ever happened | “The registered 0.3227 control figure had not been independently attacked before registration; the 2026-09-17 attack later invalidated it.” |
| State battery “moved on one seed” | Exactly zero movement on the other two | “The state drop was 0.0769 on seed 2, versus 0.0018 and 0.0002 on the other seeds; all were below the locked 0.1172 threshold.” |
| “1.94 episodes in four thousand” | Two actual episodes explain the result | “An accuracy margin of 0.000484, equivalent to 1.94 of 4,000 episodes.” |
| Standardised refit “found the same thing everywhere but one cell” | A controlled comparison isolated the effect of scaling | “The second estimator produced one nominal crossing; its folds and permutation draws also differed, so the change cannot be attributed to scaling alone.” |
| “A center … known to be there” | An acquired internal center was established | “Ownership-channel dependence was established; recovery of an acquired internal representation by this stack was not.” |

The refit paragraph should also briefly explain why a nominal crossing is reported as sub-bar. The supplied ledger gives two direct reasons: the crossing is within uncertainty in the estimated null spread, and the relevant multiple-testing correction remains unresolved. Stating those reasons is clearer than making the reader infer that a ruling changed the numerical result.

The existing refusals of “a structural signature of self-indexing” and “a structural signature of ownership-specific learning” should remain. They are unusually effective because they prevent a later writer from mistaking deliberate restraint for an omitted claim.

**The strongest case against registering version 4 as written is that it is more complete in appearance than in accounting.** Its main outcome and endpoint measurements hold, but it still leaves K5 undisposed, describes a metric obstruction as a broader control impossibility, combines two probe targets into one 270-test claim, and carries an obsolete schedule and superseded expenditure into text intended to be permanent. Its headline implies measurement exhaustion while its own body lists deferred instruments, and its gradient claim can travel without the registration’s explicit limits on experience and the same-act requirement. None of these objections requires reopening A3 or running another experiment before closure. They require a more exact account of what failed, what was measured, what was never tested, and what John has decided will remain undone—followed by the reviewer-owned closure checks the supplied ledger still says are owed.