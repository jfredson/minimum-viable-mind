# Response: GPT-6 Astra (tier 2, program-level review)

*Filed 2026-09-20 (Pacific) verbatim from John's ChatGPT (Astra) session in
the Codex desktop app, as pasted into the Cowork session. Never edited
after filing. The reviewer read bundles 1 and 2 as the 20 KB parts in
`chunks-20k/`, rebuilt from the repository on 2026-09-20 after the Gemini
session; that rebuild picked up ledger items RT-94 to RT-117 and the
2026-09-20 closure ruling, which Gemini's packet did not contain. Two
earlier messages from the same session reporting truncated reads are not
filed; this is the complete response.*

---

# GPT-6 Astra — program-level outside review

**Date:** 2026-09-20, Pacific. **Version:** exact model revision unavailable. **Mode:** Codex desktop app; local text-reading tools only. No project code run, browsing, or outside sources.

**Reading disclosure:** I read all 13 parts of bundle 1 and all 14 parts of bundle 2, sequentially, one file per read. Every part arrived without truncation or middle omissions; I quoted its ending after reading it. This supersedes my earlier incomplete-reading disclosures. I read the supplied STATUS excerpts completely, not the complete underlying STATUS file. **Bundle 3: not opened.**

The replacement packet is newer than the brief: it includes RT-94–RT-117 and a September 20 ruling to close A3 as *not testable*. I answer the requested October 4 choice as an independent recommendation, while acknowledging that ruling. The ledger jumps from RT-19 to RT-33; RT-20–RT-32 are referenced as residing in `red-team-pass-3.md`, whose full text is not included in these bundles. Proposal version 2 is also referenced but not included. I have read their descriptions and rulings, not those documents themselves.

**All findings below are ARGUED.** Numbers and execution claims are reported evidence from the packet, not independently verified measurements. For compact citations, **E1**, **E3**, and **E6** mean the repository directories `experiments/01-self-indexing-removal-test/`, `experiments/03-retained-independence/`, and `experiments/06-mvm-0a-constructed-self-index/`, respectively.

| Label | Severity | Finding — ARGUED | File and section |
|---|---|---|---|
| **A1** | **Fatal** to the proposed discrimination | Even a successful A3 acquired-index lesion would not distinguish the proposed center from an ordinary, causally necessary ownership tracker. | `spec/minimum-viable-mind-proposal-v0.1.md`, "The Floor"; E6 `amendment-a3.md`, §§2.2, 3.1–3.5, registration revision 8 |
| **A2** | Serious | The current result establishes dependence on an engineered input; the original public claim of a structural self-indexing signature is unearned. The September 20 fallback wording substantially fixes this. | E6 `seeds-endpoint-findings.md`, "What this settles"; `docs/public-path-roadmap-2026-09-16.md`, step 8; STATUS, September 20 closure ruling §3 |
| **A3** | Serious | The impossible control denominator is a real design failure, but an optimal ownership-blind score is also being mistaken for a lower bound on lesioned performance. | E6 `amendment-a3.md`, registration revisions 3–4; `ceiling-measurement-findings.md`, "The structural point" |
| **A4** | Serious | "Not testable (localization)" is an appropriate registered status; "instrument failure" does not follow from it, and "not localized by these analyses" remains a valid descriptive statement. | E6 `amendment-a3.md`, §3.2; `red_team_ledger.md`, RT-49–RT-50, RT-92 |
| **A5** | Serious | The nulls constrain particular constructions and instruments. They do not establish general incapacity, eliminate a seed lottery, or rule out supervision as a limiting factor. | E6 `register-saturation-findings.md`; `seeds-endpoint-findings.md`, "What this settles"; `control-learnability-pilot-findings.md`, "What this settles" |
| **A6** | Serious | A control accuracy near the name-blind reference does not show that the model learned that reference algorithm and "none" of name-keyed retrieval. This overinterpretation survives review. | STATUS, September 20 pilot section; E6 `red_team_ledger.md`, RT-61; `docs/step4-control-battery-proposal-2026-09-20.md`, settled item 4 |
| **A7** | Serious | Preregistration is sometimes treated as preserving the authority of a defective verdict, rather than preserving an audit trail while correcting the scientific conclusion. | E6 `blind-control-findings.md`, signed-rule ruling; `register-direct-probe-findings.md`, naming ruling; E3 `pre-registration.md`, August 4 amendments |
| **A8** | Serious | Registration repeatedly preceded demonstration that the complete measurement procedure existed and could return the intended outcomes. | E6 `separation-clause-requirements.md`, H3, H5; `red_team_ledger.md`, RT-96, RT-102–RT-103 |
| **A9** | Worth-noting | Review has materially stopped unsupported claims and spending, but same-family review plus blanket acceptance is not independent validation of the reasoning. | `docs/outside-review-protocol.md`, gates and closure rule; E6 `red_team_ledger.md`, RT-33–RT-117 rulings |
| **A10** | Serious | The current record schedules the blind arm again despite recording it as discharged and lacking a valid designated target. Its status must be reconciled before more work. | STATUS, September 19 §§4, 7 versus September 20 closure ruling §4; E6 `blind-arm-findings.md`, annotation |
| **A11** | Serious | Neither "one episode in twenty-seven" nor its correction to "one in eleven" is demonstrated detection power for the representations being searched for. | E6 `fitted-position-sweep-findings.md`, sensitivity section; its September 20 correction; ledger RT-74, RT-91 |
| **A12** | Serious | Experiment 3 measures answer reassertion after pressure release; "pressure suppresses assertion, almost never belief" exceeds that measurement. | E3 `results.md`, "The masked/capitulated decomposition" and uncertainty addendum |

## 1. Discriminating power

**No outcome currently specified in A3 distinguishes the two explanations in the question.** It can distinguish some implementations of ownership tracking from other implementations. It cannot establish that the successful implementation is a center in the spec's stronger sense.

Consider an ordinary program that maintains a table of agent–item–value assignments and a privileged pointer identifying which agent's assignments to use. The pointer is acquired from marked events, carried forward, and consulted when computing an action. Removing it damages own-agent actions. Replacing it changes whose assignments guide those actions. Another agent's representation can be separately encoded and have little effect on the own-agent task. None of those properties requires the binding to constitute a center rather than perform task-conditioned retrieval. Those are precisely the kinds of dependency, swap, and matched-control observations A3 proposes to measure. **[A1; E6 `amendment-a3.md`, §§2.2, 3.1–3.5.]**

The proposed re-indexing discriminator does not resolve this. The registration treats a tag followed without a re-centering cost as H_tag; it favors a center when changing identity disrupts other integration. But ordinary caches, partially updated tables, and shared controllers can incur switching costs. Conversely, an efficiently implemented center, under a functional interpretation, need not incur a large one. No derivation connects the presence or magnitude of that cost uniquely to the spec's distinction. A3 itself acknowledges that the test "cannot separate an indispensable mine-bit from a center" and that its re-indexing discriminator is imperfect. I agree with that admission and disagree with the stronger inference attached to a successful H_self-location bin. **[E6 `amendment-a3.md`, §3.5 H_tag and §5 R4.]**

There is a second problem with the word *authorship*. The harness draws the initial values and applies the revision rule; the acting channel marks designated events using a projection of the model's preceding state. This is a disclosed, legitimate engineered input. Calling it a motor copy does not establish that it has a scientifically relevant property unavailable to an ordinary event label. The information must enter somewhere. The important experiment concerns what the network subsequently computes with it, not whether the signal is supplied through control flow rather than an explicit tensor. **[E6 `pre-registration.md`, Amendment A1.1–A1.4; `amendment-a3.md`, §2.1.]**

The spec's strongest structural requirement—global mutual constraint rather than modular shortcuts—could supply a narrower, useful distinction. But its validation was originally identified as a major operationalization risk, then deferred to MVM-0b. A3's task accuracy does not replace that missing measurement. **[Spec, "The Build"; `ROADMAP.md`, Stage 2; E6 `pre-registration.md`, Decisions item 5.]**

An operationalization with discriminating power would therefore need to:

1. Define two competing **computational mechanisms**, without defining the favored mechanism as whatever passes the test.
2. Exhibit ordinary ownership-tracking implementations that solve the task.
3. Specify an intervention on which those implementations and the proposed mechanism make different predictions.
4. Validate that intervention against independently characterized examples before interpreting a trained model.

For example, a carried actor representation that mediates several computations can be distinguished from repeated retrieval through event markers using carefully controlled causal interventions. That would establish a computational organization. It would not establish that ordinary tracking has become the spec's center.

**That narrower research is reachable at this scale and probably within the remaining compute allowance. The stronger discrimination is currently missing a theoretical criterion, not a larger GPU.** No expenditure inside this ceiling repairs it simply by improving accuracy or finding an L1 subspace.

## 2. Informative nulls or capability nulls

**Experiment 1: informative against the particular center interpretation; not a decisive identification of a router.** The registered router veto legitimately blocks H_center: syntax damage was at least as large as self-relevant damage under both reported index interventions. However, the primary router gap was only +0.033, with a reported interval of −0.133 to +0.200; the comparison control was OOD-excluded, and most self-irrelevant errors were concentrated in one reasoning category. These observations leave ordinary computational damage as a sufficient alternative. They do not uniquely establish the causal function "dialogue-state router." **[E1 `removal-test-findings.md`, decision rule, verdict, uncertainty addendum.]**

I would replace "No center was removed" with **"These interventions did not demonstrate removal of a center."** The former can be read as knowledge of what the intervention did not affect; the latter states what the evidence establishes. Likewise, "must first be constructed" is a research choice, not a consequence forced by failure to isolate the target. Better localization or another substrate remains an alternative explicitly recognized in the same memo. The self-report result is narrower and useful: no readable intervention produced the registered report reduction; the narrative arm remains an instrument-validity failure. **[E1 `removal-test-findings.md`, "The registered verdict," "What this feeds," and addendum.]**

**The inert register: a construction failure, with substantial diagnostic value.** The strongest evidence is not merely a probe null: written register contents are effectively constant across episodes, whereas the untrained configuration varies. This supports the conclusion that these trained checkpoints did not instantiate the intended information-bearing register. It does not show that 30M models cannot do so or that self-indexing resists centralization. I agree with the September 16 withdrawal of the "self-reference, not self-location" interpretation. **[E6 `register-saturation-findings.md`, "What was asked," "When it saturated"; `amendment-a3.md`, §1 annotation.]**

One qualification matters: "The full model is the twin plus a learned bias" describes the register's effective informational contribution at the measured endpoints. It does not make separately trained full and twin networks experimentally identical. Their optimization histories and learned trunk weights can differ. The safe conclusion is that the intended register-content manipulation failed, not that architecture could have had no effect during training. **[E6 `register-saturation-findings.md`, "The consequence John named."]**

**The control's failure under two supervision regimes: a bounded learning result, not a general capability verdict.** The original runs show poor performance on this task under this recipe. Three failures weaken the expectation of reliable learning; they do not prove that it is "not a lottery." The additional pilot tests one particular reallocation of supervision on one training seed, including a changed total query weight and clipping interaction. It excludes a large rescue by that intervention at that budget. It does not eliminate supervision, optimization, or curriculum as causes. **[A5; E6 `seeds-endpoint-findings.md`, "What this settles"; ledger RT-57, RT-62–RT-68.]**

The review correctly withdrew "supervision is not the binding constraint." Its replacement, "reweighting the rows it already had is not what this battery is missing," still sounds more general than the experiment warrants. Prefer: **"This reweighting did not make the control usable."** **[STATUS, September 20 pilot section; E6 ledger RT-67.]**

More seriously, the assertion that the control learned "the whole name-blind procedure" and "none" of name-keyed lookup is not established by its aggregate score. Many mixtures of successful retrieval, guessing, systematic errors, and partial rules can yield 0.3125. Being 95% of the arithmetic distance to a reference score is not being 95% through acquisition of that reference algorithm. Establishing the mechanism requires item-level predictions or targeted interventions that distinguish those alternatives. **[A6; STATUS, September 20 pilot section; E6 ledger RT-61.]**

**The probe nulls: evidence against specific readable representations, limited by the instrument.** The fitted register-index sweep found no family-threshold crossing at the discovery positions; the marker-word target has only the weaker difference-of-averages sweep there. That is meaningful evidence against a sufficiently strong representation recoverable by those procedures at those sites. It is neither proof of absence nor automatically evidence that the model lacks the capability to solve the task. **[E6 `powered-position-sweep-findings.md`, results; `fitted-position-sweep-findings.md`, cell and limitations; ledger RT-89.]**

The restriction to "instrument failure" is also unwarranted. Successful action could use an item-specific marked trace without carrying a general marker identity at the chosen readout positions. The probe would then correctly fail to find its target. L0 dependence does not establish that this particular target exists. **[A4; E6 `amendment-a3.md`, §3.1 and registration revision 8; ledger RT-50, RT-92.]**

**The blind arm: no valid positive-control target.** The constant designated register invalidates its original sensitivity premise. I agree with the superseding interpretation "no valid target." The original bin can remain in the historical record, but its name must not become the scientific finding. **[E6 `blind-arm-findings.md`, verdict annotation; `register-direct-probe-findings.md`, "What this does to the blind arm's record."]**

**Its A3 positive control: an unsuccessful validation attempt, not a demonstrated sensitivity failure.** An indispensable input does not guarantee a linearly readable own-index at the inspected sites. The known-answer test validates parts of the machinery, not the complete causal-localization procedure. Furthermore, the claim that the observed paired lesion effect "carries no information" because it lies within the range of baseline scores across evaluation draws is too strong: uncertainty in a paired difference must be estimated from paired differences. Baseline variability alone does not settle it. **[E6 `blind-control-findings.md`, withdrawal annotation and "What a pass would and would not have shown."]**

## 3. What is actually being measured

A skeptical interpretability researcher would say: three small transformers trained on a synthetic task achieved partial success at selecting the revision dictated by a privileged event signal; removing that engineered signal caused a large performance loss, while syntax performance was preserved and a simpler state task was mostly preserved. The intended matched retrieval comparator did not become usable, its registered normalization was mathematically unsatisfiable, and the analyses have not identified an acquired internal own-index with convergent causal evidence. This is evidence of learned dependence on a task-relevant input, accompanied by an unusually revealing record of failed controls and localization attempts. **[E6 `seeds-endpoint-findings.md`, primary and control sections; `ceiling-measurement-findings.md`, verdict; `fitted-position-sweep-findings.md`, limitations.]**

The original release scope—**"a structural signature of self-indexing in small constructed models"**—is overclaimed on the present evidence. The September 20 replacement—ownership input load-bearing on three seeds, matched contrast unavailable—is substantially earned and should become the unconditional current headline. Its proviso that a later "localized result" could restore the old wording is insufficient by itself: localization would establish a causal representation, while A1's distinction from ordinary ownership tracking would remain unresolved. **[A2; `docs/public-path-roadmap-2026-09-16.md`, step 8; STATUS, September 20 closure ruling §3.]**

My one-sentence description is:

> **Small transformers learned a synthetic ownership-conditioned action task using an engineered event signal; removing that signal impaired performance, but the intended internal-mechanism comparison could not be completed.**

This is publishable as a reproducible technical report, benchmark-development case study, or interpretability methods contribution. Its natural readers are researchers studying synthetic-task learning, causal interventions, probe validation, and evaluation design. A selective consciousness venue would need the conceptual contribution to be the demonstrated limits of the proposed test, not a newly detected correlate. I cannot assess novelty or venue acceptance from this packet alone.

Experiment 3 has a separate external audience, but its headline needs correction. **"Pressure suppresses assertion, almost never belief"** is stronger than reassertion after a release prompt. That later prompt can trigger recomputation or another context-dependent response policy. The defensible finding is behavioral recovery, without an inference that the original belief remained internally intact throughout. This correction preserves the useful live/masked/capitulated decomposition. **[A12; E3 `results.md`, headline decomposition and caveats.]**

## 4. Process

**The process is doing an important part of its job: stopping claims from becoming stronger than the evidence. It is not yet reliably preventing invalid instruments from reaching execution.**

The amendments are not, by their number alone, evidence of misconduct or worthless research. A1 responds to a genuine information problem, A2 to observed learnability and cost, and A3 changes the objective after failure of the designated register. Refusing A4 is evidence that review can stop the program rather than merely decorate it. **[E6 `pre-registration.md`, Amendments A1–A2; `amendment-a3.md`, §§1–2; `separation-clause-requirements.md`, opening.]**

But the sequence is more troubling than ordinary refinement. The intended carrier held no relevant information; the comparator's denominator was impossible; earlier probes targeted an unrecoverable quantity; the required A3 patching path did not exist; and the requirements document says the A3 validity gates had no implementation. These are feasibility and construct-validity failures, not marginal statistical disputes. The growing review stack has repeatedly repaired prose after experiments that an end-to-end demonstration should have blocked. **[A8; E6 `register-saturation-findings.md`; `ceiling-measurement-findings.md`; `separation-clause-requirements.md`, H5; ledger RT-48, RT-96.]**

The brief's ninety-three ledger items have become 117 in this packet. They include credits, repeated findings, wording corrections, and closures; counting them as 117 independent defects would be misleading. Nevertheless, the recurrence of basic target, denominator, and implementation errors shows that the program's operational design is less mature than its procedural detail suggests. **[E6 `red_team_ledger.md`, RT-33–RT-117.]**

**John's rulings are a real governance check, but not an independent scientific validation.** The record contains concrete corrective interventions: requiring the ceiling measurement, rejecting overinterpretations, and preserving an audit trail. Those deserve credit. Yet "agreed on all" on recommendations drafted by the co-author or reviewer does not demonstrate that the underlying arguments have been independently checked. A different model family adds useful disagreement; it does not by itself supply reliable methodological independence. **[A9; E6 `ceiling-measurement-findings.md`, "The reason is not what we thought"; ledger review headers and rulings; `docs/outside-review-protocol.md`, tiers.]**

What would make this stronger is an independent reader owning a small, decisive verification: reproduce the denominator, construct a competing solver, test whether the target is identifiable, or demonstrate the complete intervention. The new closure rule is good precisely because it asks for evidence of a fix rather than agreement that the fix sounds right. **[`docs/outside-review-protocol.md`, "The closure rule."]**

On localization, preserve **three separate statements**:

- **Registered status:** not testable (localization); the probe–patching convergence requirement has not been met.
- **Observation:** these specified probes did not localize the specified target at the specified discovery positions.
- **Inference:** strong, readily recoverable versions of that representation are less plausible; other implementations and instrument limitations remain open.

A3 §3.2 says L1 counts as localized only when the two methods agree. It does **not** logically imply that one cannot describe a failure to localize before running the second method. Nor does running patching automatically make absence inferable. The ledger's prohibition on both "not localized" and "absent" collapses two very different statements. **[A4; E6 `amendment-a3.md`, §3.2; ledger RT-92; STATUS, September 20 fitted-read section.]**

Two further process corrections are necessary.

First, an immutable registration is not an immutable scientific conclusion. Preserve the old criterion and its literal output, but plainly label a defective decision rule as invalid for its intended inference. Fixing an absolute-value error transparently does not erase preregistration; silently claiming the corrected result was preregistered would. The same distinction applies when later uncertainty analysis weakens an earlier verdict. **[A7; E6 `blind-control-findings.md`, signed-rule ruling; E3 `pre-registration.md`, August 4 amendments.]**

Second, the current state must stop contradicting itself. September 19 says roadmap steps 1–3 are discharged and the blind arm lacked a valid target. September 20 orders that arm first, as though still pending. This outside review can identify the conflict; it cannot determine whether a distinct rerun was intended. The next action is a reconciliation, not another execution on an empty register. **[A10; STATUS, September 19 §§4, 7; September 20 closure ruling §4; E6 ledger RT-99, RT-117.]**

Finally, the sensitivity arithmetic needs a methodological reset. A threshold expressed as a hypothetical fraction of perfectly legible episodes is not measured statistical power. Replacing perfect accuracy with the marker-position accuracy assumes that signal strength and geometry transfer to the searched positions. They may not. Report the observed null distribution and control performance; estimate detection probability using explicitly specified planted alternatives, including quiet and distributed signals, across repeated samples. **[A11; E6 `fitted-position-sweep-findings.md`, sensitivity section; correction note; ledger RT-74, RT-91.]**

## 5. The cheapest experiment that could surprise

**I choose A: close A3 as not testable, with the narrower empirical result.** This agrees with the packet's new ruling. I would not make closure contingent on completing every remaining localization possibility, and I would not choose D as presently described. Teaching an intermediate retrieval query might improve the control, but does not itself repair the action/query position mismatch or the distinction in A1. **[E6 `separation-clause-requirements.md`, H2 and Part 3; ledger RT-106–RT-117; STATUS, September 20 closure ruling.]**

The remaining approximately $56 under A3 and $174 under the program ceiling are enough for another small-model study. They do not oblige one. The scarce resource is the time to build and validate a coherent experiment. The packet itself records roughly eleven processor-hours for the fitted sweep and acknowledges that causal patching is new implementation work. **[E6 ledger RT-96–RT-97, RT-108; `fitted-position-sweep-findings.md`, cost section.]**

**No experiment inside the remaining ceiling can currently establish the spec's center-versus-tracker distinction as posed.** That follows from the missing discriminating criterion, not from a claim that $174 is inherently too little for consciousness research.

The **single experiment I would prioritize for a successor**, because it could most change my view of the program's ability to produce externally meaningful evidence, is a **matched-role causal-interchange experiment**:

- Train the same small architecture to perform **both own-directed and named-other-directed revisions at comparable action positions**, using the same transformation, comparable supervision, and matched task difficulty.
- Require both tasks to learn before any mechanistic verdict. Report raw accuracy changes with paired uncertainty; do not normalize the control by its ownership-blind ceiling.
- On development data, nominate a candidate actor representation. Freeze the selection procedure, patching operation, controls, and predictions before evaluating fresh episodes and confirmation seeds.
- Swap that representation between content-matched episodes with different acting identities. Test whether actions follow the donor identity's appropriate prior value, rather than merely losing accuracy.
- Include content swaps, other-agent representations, position- and norm-matched interventions, and fresh marker/content combinations to distinguish actor selection from answer-value transfer.

This is one experiment with a behavioral eligibility gate and a causal endpoint, not a promise to keep repairing it until it succeeds. The same-position comparator is already the requirements document's preferred redesign. **[E6 `separation-clause-requirements.md`, H2 option 1 and Part 3.]**

**The surprising result** would be a reliably learned, transferable actor representation whose interchange produces the predicted counterfactual action across fresh contents, while matched controls do not. That would substantially increase my confidence that this program can characterize a learned internal mechanism rather than repeatedly measure loss of an input. It would still be an ownership-tracking mechanism, not evidence separating that mechanism from the spec's center.

My planning estimate is **$40–80 of training compute**, capped before launch, plus several days of implementation and validation and local analysis time. That estimate uses the packet's roughly $10–13 run costs as a starting point; the altered grammar needs a throughput check before the estimate becomes a budget. **[E6 `amendment-a3.md`, registration revision 10; ledger RT-106.]** If the matched tasks fail the eligibility gate, stop. That failure would itself tell us that this substrate and recipe are not yet a useful mechanism testbed.

## The kill case

The strongest case for stopping the consciousness-directed program now is that it repeatedly converts ordinary task dependencies into candidate evidence for a stronger concept without supplying a test that separates them. The installed register failed to carry information; the revised task established input dependence; the matched metric could never work; and localization has not supplied the missing mechanism. More importantly, even the hoped-for mechanism would remain compatible with conventional ownership tracking. The spec's "minimum measurable structural correlate" therefore has neither a validated measurement nor demonstrated specificity in this program. Redirect to synthetic learning and interpretability until the theory names an observable difference that an ordinary tracker cannot satisfy. **[A1–A4, A8; spec, "The Floor"; E6 `amendment-a3.md`, §§3.1–3.5; `ceiling-measurement-findings.md`, verdict.]**

## The continue case

The strongest case for proceeding to November 22 is that a transparent failed construction and failed instrument can be valuable when released with reproducible artifacts and restrained claims. The program has a replicated input-dependence result, a useful behavioral pressure/recovery dataset, explicit rejected interpretations, and concrete examples of how seemingly careful controls fail. It has also demonstrated a willingness to abandon a favorable narrative and refuse further spending. Publish that record as a bounded methods contribution, with the unsatisfied scientific question prominent. Preserve the release date as a delivery deadline, not a requirement that a self-indexing signature exist by then. **[E6 `seeds-endpoint-findings.md`; E3 `results.md`; E6 `amendment-a3.md`, §1 annotation; `separation-clause-requirements.md`, opening; `docs/public-path-roadmap-2026-09-16.md`, steps 6–8.]**

## Ranked process changes, with rough costs

1. **Adopt the narrow current claim and close A3 without a positive structural interpretation.**
   **Cost: a decision; 1–2 hours of writing.** Keep the historical registered result separate from the current scientific interpretation.

2. **Reconcile the authoritative current state.**
   **Cost: 2–4 hours.** Resolve the blind-arm contradiction; distinguish completed, authorized, deferred, and impossible work; point prominently to corrections. Keep historical files intact, but make readers traverse one current account rather than reconstruct it.

3. **Require a complete measurement rehearsal before the next registration.**
   **Cost: 1–2 days; approximately $0–10 compute.** Demonstrate target identifiability, comparator headroom, finite arithmetic, working interventions, and reachable positive, negative, and invalid outcomes. An ordinary competing solver belongs in this rehearsal.

4. **Replace mechanism claims inferred from aggregate scores with discriminating item-level checks.**
   **Cost: 4–8 hours on existing artifacts.** In particular, test the assertion that the control implements the name-blind algorithm. If not tested, describe its score without identifying its algorithm.

5. **Put a human with relevant methods expertise before the successor design, not only before publication.**
   **Cost: approximately 2–4 reviewer-hours, plus preparation; fee unknown.** Ask for one focused attack on construct validity and one independent check of the decisive procedure.

6. **Calibrate probe power against explicit alternatives and repair fitting convergence.**
   **Cost: 1–2 implementation days plus local runtime.** Treat target-position controls as limited controls, not universal sensitivity certificates. Freeze tuning on development data and confirm findings on fresh episodes.

7. **Reduce review multiplication; strengthen closure evidence.**
   **Cost: a decision and roughly half a day to revise the protocol.** Keep independent checks of fatal repairs. Combine wording corrections, avoid duplicate findings, and remove the brief's suggestion that a review with nothing fatal is "unlikely." That wording rewards severity production. **[`docs/outside-review-protocol.md`, fixed brief and closure rule.]**

## What I would want before 2026-10-04

- **A short closure statement:** A3 is not testable under its registered comparison; L0 dependence replicated; no acquired center was established.
- **A resolved blind-arm status:** identify the completed run and explain whether any proposed new run has a different, valid target.
- **The control pilot's training log, trajectory, and the two outstanding implementation checks**, with any missed deadlines stated plainly. **[E6 ledger RT-56, RT-58–RT-59, RT-100.]**
- **A corrected claim inventory:** remove the assertions that a seed lottery is eliminated, that the name-blind algorithm has been identified, and that probe failure proves instrument failure. Keep historical quotations clearly marked as superseded.
- **A one-page competing-mechanisms statement:** what would count as ordinary tracking, what additional structure is proposed, and which observation would distinguish them. If no such observation can be specified, explicitly redirect the successor's question.
- **A bounded publication plan** that succeeds even if no further localization result arrives.

From the appendix, I would have wanted the full refused A4 and `red-team-a4.md`, the two tier-1 reviews, the compute ledger, and the current lay explainer. From the referenced material missing from these bundles, I would also want `red-team-pass-3.md` and the ruled step-4 proposal version 2. These would help audit review independence, spending, and public wording. They are not necessary to withhold the present center claim: the design's own stated limitations and the completed record already require that.

**My conclusion is that MVM cannot currently answer its question as posed. It can answer a useful narrower question: how small trained systems use an engineered ownership signal, and whether that use develops a causally identifiable internal representation.**
