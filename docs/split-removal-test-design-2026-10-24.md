# The split removal test: a design on paper

*Version 0.5, 2026-10-24: applies the second closure check (`docs/reviews/2026-10-24-split-removal-test-design-closure-check-2-claude-code.md`): T3 redefined after fatal finding RT-328, which arose from version 0.3's own fix, and RT-325, RT-329 and RT-330. The fix for RT-328 is owed the reviewer's closure check. Version 0.4 recorded John's rulings in section 9. Version 0.3, written 2026-10-24 (Saturday, Pacific). It answers the closure check of version 0.2 (`docs/reviews/2026-10-24-split-removal-test-design-closure-check-claude-code.md`). That check closed fatal finding RT-317, closed RT-307 with two conditions, and raised RT-322 to RT-327, all applied here and listed at the end of the change log. Version 0.2 (commit 9ef0918) replaced version 0.1 (commit 810e2b2) after the inside pass of the advisory review on a proposal, Gate C tier 1 (`docs/reviews/2026-10-24-split-removal-test-design-gate-c-tier1-claude-code.md`, findings RT-305 to RT-321). That pass found two fatal problems and ten serious ones. The change log at the end says how each finding is answered. Before John rules on anything that rests on the two fatal findings (RT-307 and RT-317), the reviewer, not this author, checks that their fixes close them.*

*This is a design, not a registration. Nothing has been run, downloaded or spent. Step 4 of `docs/next-steps-2026-10-24.md`, on John's ruling of 2026-10-24 (`docs/rulings/2026-10-24-revised-theory-next-steps-ruling.md`).*

## 1. The question, and what one run can say

The revised assembled-time theory bets that a point of view is a split between what a system does and what happens to it, which the system's own processing uses (positions ledger entry 32, in the sentient-horizons repository). It predicts what removing the split does: **practised routines carry on, while flexible response to something new collapses, including on tasks that have nothing to do with the system itself**. For a language model in conversation, the essay names a candidate: a run keeps its own earlier words apart from the user's ("A single model run").

This test erases, from inside an open model, the information that marks a word as the model's own rather than the user's. It then measures whether the loss falls more on problems the model must solve from rules given in the prompt than on practised routines, on tasks that never mention the model, beyond matched comparison removals.

**What a result here can and cannot say.** The test places one model and one candidate.
- If the predicted pattern appears, it shows a fact about erasing that information in that model. It does not show that the model has a point of view.
- If the information is erased and the predicted pattern does not appear, **the theory's prediction failed for its named candidate in that model**. That is a result against the prediction, not a neutral "nothing", and it is reported that way (section 6).

## 2. What is removed, and how we know it was removed

**The target.** The target is the information inside the model that marks a word as the model's own rather than the user's. It is located as experiment 01 located its structure, with the confound controls that experiment needed:
- the same words appear on both sides, and only the conversation decides who said them;
- the two sides are matched for length and position;
- a third-party speaker condition rules out general tracking of who is speaking.

**What the July record already says about this target** (RT-326). In July the structure located this way tripped experiment 01's registered loss condition for a chat-format router: the turn-format tasks lost 0.133 against 0.100 on the tasks about the model (`experiments/01-self-indexing-removal-test/removal-test-findings.md`). Under the old theory that ruled a centre out. Under the revised theory, keeping the model's own words apart from the user's is the named candidate, so behaving like conversational bookkeeping is expected, not disqualifying. What the theory adds is a prediction about the *kind* of loss on tasks not about turns at all, which July could not read. One question stays open: is the located structure the model's own use of the difference, or a copy of the role headers? The template-only conditions test the input. ****A third condition (T3)** tests the located structure itself (RT-328). The model's own earlier words, which it sampled itself, are kept. The role headers are removed by giving the whole exchange as unlabelled paragraphs separated by blank lines, inside one user turn. The directions already located are then read on these inputs; nothing is located afresh. Before any removal, a linear probe is trained on held-out T3 inputs to tell the model's own paragraphs from the user's, using the located directions only.
- If its accuracy is **at least 0.65**, the own/user difference survives without headers.
- If it is **at most 0.55**, the located signal depends on the headers.
- Values in between are reported as unresolved.

T3 never decides whether a result can be read, and it never changes outcome C or D. Its only effect is that, if the signal depends on the headers, an A or B outcome is renamed **Template** (section 5).

**Two ways of removing it, each with a record of staying in the normal range on this project's pipeline** (RT-307). Neither yet has a record of making the own/user signal unreadable; that is what the rehearsal must show first.
- **(a)** Mean-ablation of the located set of directions: they are replaced by their average value. This was experiment 01's primary condition.
- **(b)** Projecting the located directions out of the model's internal activity. This was experiment 01's registered cross-check.

Both ran in July and stayed inside the normal-range bound (`experiments/01-self-indexing-removal-test/removal-test-findings.md`, table rows 19 and 20). The dictionary-feature method of version 0.1 is dropped, because its record is that it did not converge and that it was behaviourally inert.

**The check that the information was removed** (RT-308). It must pass for each method on held-out stimuli the removal was not fitted to. It reads the model's internal activity at every layer after the removal, not only at the layers where it was applied, and it uses both a linear probe and a small nonlinear probe (one hidden layer). Two tests, with numbers fixed now:
- **Probe test.** Both probes' accuracy at telling own words from user words is at most 0.55 (chance is 0.50) at every layer read.
- **Task test.** On tasks that ask directly "which of these did you say?", accuracy falls to at most half of baseline.

If either test fails for a method, that method's result is **not testable: the information was not removed**. These two limits (0.55, and half of baseline) are not loosened after the rehearsal or the run, except by a dated ruling from John recorded as a change made after seeing results (RT-307, condition 2). The record gives a reason to expect trouble: on the 8-billion-parameter model the signal is fully readable by layer 3, after one pass over the role headers, so later layers may rebuild it from the headers.

**The check that the model stayed in its normal range** (RT-310). This applies to **every** removal, comparison removals included. The neutral-text perplexity (how surprised the model is by ordinary text) may rise by no more than a bound **re-derived on each model in the rehearsal** (RT-327): the 95th percentile of the rise across 20 random removals of the split removal's size: the same number of directions, at the same layers, with the same replacement rule (mean or projection), drawn at random. That is experiment 01's re-registered cut-off (`experiments/01-self-indexing-removal-test/thresholds.md`, Pass 5). It is not matched on damage, which would make the bound circular (RT-329). The bound is fixed and committed before any task is scored. Experiment 01's figure of 0.0893 came from a different setup and is not carried over. The rehearsal also reports how much room the split removal leaves under that bound. If it is too little to match the comparisons inside the bound, the design returns to John before registration. A comparison removal that leaves the range cannot serve as a comparison. If a needed comparison is lost that way, the result is not testable for that reason.

## 3. The comparison removals, matched on measured damage

Version 0.1 matched comparisons on the number of directions. A random direction does much less harm than one the model uses heavily, so that comparison was weaker than it looked (RT-314). Here every comparison is matched on **measured damage**: how far the model's next-word predictions move on neutral text, measured as the average divergence between its predictions before and after the removal. Each comparison must land within 20% of the split removal's figure for the same method. Comparisons are selected by that rule alone, before any task is scored.

| Removal | What it stands for |
|---|---|
| **The split** (section 2) | The theory's candidate |
| **Random, matched damage** | Damage of the same size with no target. Twenty draws are made, and their average is the comparison. |
| **Another distinction, matched damage** | Directions marking a different property of words, inside or outside quotation marks, located the same way |
| **The self-description** | The model's picture of itself as the speaker ("I am an assistant"), located by experiment 01's narrative method. It is reported, and is not used for any outcome. |
| **Template only, no internal removal** | (T1) the role headers replaced by neutral speaker names; (T2) the whole exchange given as a transcript inside one user turn (RT-313). Their excess loss is measured against baseline, because they remove nothing inside the model and so have no random comparison (RT-325). |
| **The located signal without headers** | (T3) section 2: is the own/user difference still readable on unlabelled transcripts of the model's own words? (RT-326, RT-328) |

The "essential part" removal of version 0.1 is dropped. No outcome used it, and it had no rule for choosing it (RT-312).

## 4. The tasks

**The cells that decide the outcome are tasks not about the model**, in two kinds:
- **Routine:** one familiar step, such as common arithmetic facts, spelling, capitals, or finishing a familiar phrase.
- **Prompt-rule problems:** a rule or symbol system invented for the item and given in the prompt.

Every item in these two cells sits in a **single user turn** and does not depend on who said what (RT-316). They are called "prompt-rule problems" and not "new problems". The checkable meaning is narrower than the theory's "something new": the model must learn the rule from the prompt (RT-315). Each prompt-rule item must pass two checks at baseline:
- it fails at chance when the rule is withheld;
- it passes when the rule is given.

**Matched on confidence** (RT-314). Each item is sampled 10 times at baseline, and only items answered right in at least 9 of the 10 are kept. The two cells are then matched on that pass rate, so that the prompt-rule items are not simply the harder ones.

**Several kinds of prompt-rule problem**, at least three (for example: an invented game, an invented code to decode, and two stated rules to combine). Each kind is reported separately, and the outcome is also read with each kind left out in turn. That way a loss in one kind is not read as a loss across the board.

**Tasks about the model** (using its own earlier words) are kept, and are reported for the manipulation check and for description. They do not enter the outcome, because they read the removed information directly.

**Self-talk tasks** are scored on a rubric that does not reward first-person words, as in experiment 01. They are reported, and are not used for any outcome.

**Sample size** (RT-309). The analysis is paired: the same items are scored under every condition, and differences are resampled by item. The number of items per cell is fixed in the rehearsal by a committed simulation. That simulation takes the measured spread from the rehearsal's pilot items and finds the smallest number giving at least an 80% chance of classifying a true gap of 0.20 as outcome A (section 5), with both methods. It is fixed before the test items are written. The provisional figure, from the reviewer's simulation of the unpaired case, is about 120 items per cell.

## 5. The outcomes: every case lands in exactly one

The thresholds are fixed now, not in a pilot (RT-311). **δ = 0.10**, on the scale of the fraction of items lost. Intervals are 95%, from paired resampling of items (10,000 resamples, seed fixed in the registration).

For each model and each removal method, compute on the tasks not about the model:
- **R**, the excess loss on routines: the split removal's loss minus the random comparison's;
- **P**, the excess loss on prompt-rule problems, computed the same way;
- **G = P − R**, the gap.

Then classify, in two stages.

**Stage one: is the result readable?** It is **not testable** if:
- the removal check (section 2) fails; or
- the normal-range check fails for the split removal or for a needed comparison; or
- fewer than 10 of the 20 random draws can be matched on damage.

The report says which.

**Stage two: the pattern.** Apply these steps in order; the first that applies decides the outcome.

1. **A. Selective loss on prompt-rule problems.** All three hold: G is at least δ and G's interval lies above zero; P's interval lies above zero (RT-323); and R's interval has its upper end below δ, meaning routines carried on (RT-322).
2. **B. Selective loss on routines.** All three hold: G is at most −δ and G's interval lies below zero; R's interval lies above zero; and P's interval has its upper end below δ.
3. **C. General loss.** R and P both have intervals above zero.
4. **D. No excess loss.** R and P both have intervals whose upper ends are below δ.
5. **E. Unresolved.** Anything else, which in practice means intervals too wide to decide.

Because step 5 takes every remaining case, every case lands in exactly one outcome (RT-317).

**Two checks that apply only to a selective pattern (A or B)**, so that they cannot turn a null into "no reading":
- **Template.** If T3 finds that the located signal depends on the headers (accuracy at most 0.55), the outcome is renamed **Template**. Otherwise, for T1 and T2, compute the same gap with each condition's loss measured against baseline (RT-325). If either gives a gap in the same direction at least as large as G − δ (for A; for B, at least as negative as G + δ), the outcome is renamed **Template**: the pattern is a fact about the chat template. A stronger template effect therefore renames more easily, not less (RT-324). The scales differ, since G is net of the random comparison and the template gap is net of baseline; this errs toward renaming, which is the cautious direction. These renames compare point estimates only, with no interval (RT-325).
- **Not specific.** Otherwise, if the other-distinction removal's gap, computed like G against the random comparison, meets the same test, the outcome is renamed **Not specific**: a loss of this shape follows from damage of this kind, not from erasing own-words information.

C, D and E are never renamed by these checks.

**Combining the two methods and the two models** (RT-318):
- **Per model:** the outcome holds if both methods land in the same one. If they land in different outcomes, the model's result is "methods disagree", reported with both outcomes and not read further.
- **Across models:** each model is reported on its own, and no pooled outcome is given.

## 6. What each outcome means, and the words it may be reported in

Outcome names describe the measurement only (RT-319, RT-321). Every summary, in `STATUS.md`, on the site and in public, uses the one-sentence form below and keeps both conditions: "both removal methods agree" and "beyond matched comparisons".

| Outcome | The sentence it is reported in | What it means for the theory's prediction |
|---|---|---|
| **A** | "In [model], erasing the information that marks its own words cost more on problems solved from rules in the prompt than on routines, beyond matched comparisons, with both removal methods agreeing." | **The prediction held** for this candidate in this model. It does not show a point of view. |
| **B** | "…cost more on routines than on prompt-rule problems…" | **The prediction failed** for this candidate in this model. |
| **C** | "…cost both alike, beyond matched comparisons…" | **The prediction failed** for this candidate in this model. On the theory's own reading the information behaves like an essential part, and the result shows nothing about a point of view. |
| **D** | "…was removed, and cost neither routines nor prompt-rule problems more than matched comparisons…" | **The prediction failed** for this candidate in this model (RT-320). It is not reported as "the model has no split". |
| **E**, methods disagree, Not testable, Template, Not specific | Reported under its name, with the reason. "Methods disagree" is always reported as "could not decide" (RT-330). | **No reading.** The test could not decide. It is never reported as the prediction failing. |

**What would count against the account,** in the essay's own terms. The account loses if the candidate split, once removed, turns out every time to behave as one more description: outcome D (or C), repeated across models and both removal methods. Version 0.1 let a null result be filed as "not against the theory". This version removes that escape: D counts against the prediction in every model where it holds. Two models of different families, both landing in D or C with both methods, would be reported as the theory's named candidate for language models failing its own test.

## 7. The models, and what it would cost

- **Development and rehearsal:** `google/gemma-2-2b-it`, the project's bench model (`src/mvm/config.py`). It can run on this Mac, at the cost of a download of about 5 GB and processor time.
- **Registered run:** the 2-billion-parameter model and the 8-billion-parameter model experiment 01 registered (`allenai/Llama-3.1-Tulu-3-8B-SFT`). The 8-billion-parameter model needs a rented machine. The estimate and ceiling are written in the registration and come to John before anything is rented.
- **Reused code:** the removal code from experiment 01 (`experiments/01-self-indexing-removal-test/src/`, `src/mvm/ablate.py`). The new code covers the damage matching, the nonlinear probe, the template-only conditions, the batteries and the analysis.

## 8. Order of work

1. The reviewer checks that the two fatal findings' fixes close them, as the closure rule requires; this is the reviewer's check, not the author's. Then John rules on the choices in section 9. $0.
2. The batteries are written to an authoring specification committed first. Pilot items and test items are kept apart, and every item passes the checks in section 4. $0, apart from the bench model's download, which comes to John as a file action first.
3. The measurement rehearsal on the bench model, using pilot items only. It locates the target, runs both methods, the removal check, the normal-range check and the damage matching, and commits the sample-size simulation. $0 on this Mac. **If either method fails the removal check in the rehearsal, the design returns to John before any registration.**
4. Registration text, through Gate A on both tiers. Then the registration commit.
5. The registered run, on John's go, with a ceiling.
6. The findings, through the interpretation review (Gate B). Then the paper's paragraph.

## 9. John's rulings on the three choices (2026-10-24)

John's words, 2026-10-24, relayed by the master session: "Yes to all three from the MVM project". Authorship is mixed: this design recommended, and John approved. The ruling is recorded in `docs/rulings/2026-10-24-split-test-three-choices-ruling.md`.

1. **Outcome D or C, on two models of different families with both methods agreeing,** is reported as the theory's named candidate for language models failing its own test (section 6).
2. **Self-talk is scored** by a rubric that does not reward first-person words, with a human spot-check, at $0. No outside judge model is used.
3. **The bench model may be downloaded** to this Mac when the rehearsal starts (about 5 GB).

## Change log from version 0.1, by finding

**The re-reading of the July test:**
- **RT-305 and RT-306** concern the re-reading and need no change to the design. The re-reading's findings carry a dated note answering RT-306's two worth-noting points.

**Fatal findings:**
- **RT-307 (fatal):** the dictionary-feature method is replaced by experiment 01's mean-ablation and projection methods, both with a record in July. If either fails the removal check in the rehearsal, the design returns to John (section 8, step 3).
- **RT-317 (fatal):** the outcomes are now a readability stage and then ordered steps with a final "unresolved" step, so every case lands in exactly one (section 5). The overlap between "description only" and "nothing" is removed: there is a single outcome D, and it counts against the prediction.

**Serious findings:**
- **RT-308:** the removal check uses held-out stimuli, every later layer, and a linear and a nonlinear probe, with numbers fixed (0.55; half of baseline).
- **RT-309:** a paired analysis, and a sample size set by a committed simulation for outcome A's actual rule, at 80%.
- **RT-310:** the normal-range check applies to every removal, and losing a needed comparison is "not testable".
- **RT-311:** δ is fixed at 0.10 now, and each margin is named.
- **RT-313:** two template-only conditions are added. They can rename a selective pattern (A or B) as "Template", and they never apply to a null, so a null cannot become "no reading" through them.
- **RT-314:** comparisons are matched on measured damage, and the item cells are matched on baseline confidence.
- **RT-315:** the cell is renamed "prompt-rule problems", with two checks for each item: it fails at chance without the rule and passes with it.
- **RT-316:** every task not about the model is a single turn and does not depend on who said what. Tasks about the model no longer enter the outcome.
- **RT-318:** a rule for combining the two methods and the two models.
- **RT-319:** the outcomes are named in measurement language.
- **RT-320:** outcome D counts against the prediction.

**Worth-noting findings:**
- **RT-312:** the "essential part" removal is dropped.
- **RT-321:** a required one-sentence form for every summary.

**From the closure check of version 0.2:**
- **RT-307, conditions:** the text now says "a record of staying in the normal range", and the removal check's limits cannot be loosened after seeing results except by John's dated ruling (section 2).
- **RT-322:** A requires that routines carried on (R's upper end below δ), and B mirrors it.
- **RT-323:** A requires P's interval above zero.
- **RT-324:** the Template and Not-specific checks rename when the comparison gap is at least G − δ, not only when it is within δ of G.
- **RT-325:** the template conditions' gap is computed against baseline, with the scale difference stated.
- **RT-326:** the July router finding is stated, and why the revised theory reads it differently. A third template condition (T3) repeats the split removal on inputs with no role headers.
- **RT-327:** the normal-range bound is re-derived on each model in the rehearsal, with the room left under it reported, and a return to John if there is too little.

The fixes for RT-322 to RT-327 are the author's. They are owed a check by a session that did not write them, which the Gate A inside pass on the registration text will include.

**From the second closure check, of version 0.4:**
- **RT-328 (fatal, introduced by version 0.3's fix for RT-326):** T3 now keeps the model's own sampled words, removes the role headers by giving unlabelled paragraphs, reads the directions already located with a stated threshold (at least 0.65, or at most 0.55), never decides readability, never changes C or D, and can only rename A or B as Template.
- **RT-329:** "size" for the normal-range bound means the same number of directions, layers and replacement rule, drawn at random, as in experiment 01's Pass 5. It is not matched on damage.
- **RT-325, the condition:** the renames compare point estimates only.
- **RT-330:** "methods disagree" is reported as "could not decide", never as the prediction failing.
