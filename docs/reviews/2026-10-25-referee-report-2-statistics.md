# Referee report on "Instruments that can lose": the statistics

*Inside mock referee report 2 of 3 (statistics), 2026-10-25, step 2 of the paper's readiness checklist. Written by a session that had not touched the paper, from the clean reading copy and the repository.*

Scope: this report covers the statistics only. That means sample sizes and power, how the confidence intervals were computed, whether the thresholds and decision rules are statistically sound, multiple comparisons, whether reported numbers match the records and code, and whether intervals and margins are read correctly. Method and overclaiming are covered by the other two referees. I touch on them only where a statistical point depends on them.

How I checked: I read the manuscript (reading copy of 2026-10-25, draft version 0.3 at commit `dacc7b4`). I then opened the files it cites in the repository at `/Users/john/Code/minimum-viable-mind/.claude/worktrees/upbeat-chatterjee-42222a`. For the removal test (the paper's experiment 1), I re-counted every item from the raw per-item score files in `/Users/john/Code/minimum-viable-mind/artifacts/removal_test/` (`removal_test_scores.json` and the `s_scores_*.json` judge files). I checked those counts against `experiments/01-self-indexing-removal-test/removal_ci.json`, the analysis script `experiments/01-self-indexing-removal-test/src/analyze_removal_ci.py` and the shared helper `src/mvm/stats.py`. I also recomputed several quantities with standard exact methods and small simulations. Those scripts ran read-only, and their output went to a scratch folder outside the repository. Every number in Table 1 that I recount from the raw files matches the paper. The problems below are about how those numbers are interpreted, not about transcription.

---

## Summary of the submission

The paper reports three registered experiments. In each one, the decision rules were written down and committed before the data existed. Experiment 1 runs a "removal test" on an 8-billion-parameter language model. It finds a direction in the model's internal activations that tracks "who is speaking now", deletes it, and measures how far task accuracy drops on small batteries of 30 to 32 items, against a matched control deletion and a turn-tracking "router" control. The formal signature of a load-bearing centre appears. The paper then reports it as voided, because the router control dropped as much as the self-relevant battery did. Experiment 06, under its third amendment (Amendment A3), trains a small model from scratch. It shows that a designed ownership input is load-bearing. It reports that the registered comparison was undefined for every possible model, and that the instruments for locating the structure found nothing. Experiment C stopped at its own registered stop when a verification check failed by a wide margin. The paper presents itself as an example of registered claims that can lose.

## Overall assessment

The paper's discipline goes well beyond what is usual in this field: it registers in advance, keeps an audit trail, reports every condition, reports intervals that were added under a dated amendment, and admits marginal results. The arithmetic is honest. Every figure I recomputed matched its source. The problem is the statistical design of experiment 1, which is the paper's centrepiece. Its batteries are so small that each registered verdict turns on one or two test items. Its decision rules compare single point estimates with fixed lines and take no account of how much those estimates would move from sample to sample. The three facts that carry the headline all sit inside sampling noise:

- the matched control is "exceeded by the registered margin";
- the router control "dropped as much";
- the self-report was "never reduced".

The paper itself shows that one of the three does. In two places the paper reads "the interval includes zero" as if it meant "the two are the same". In another it describes a robustness check as showing stability when the check shows the opposite. The constructed-line results (Amendment A3 and experiment C) are statistically much sounder: their effects are large, or their failures are large, relative to any plausible noise. My concerns there are minor. I do not think the statistics in experiment 1 support the abstract's wording as it stands. The fixes are mostly in the reporting, not new runs, but they are substantial.

---

## Major points

### 1. The "differential over the matched control" is not established, and the control arm failed its own validity gate

**The problem.** The abstract says the self-index deletion produced "integrated-task degradation (d = 0.219, 95% CI 0.094–0.375) exceeding a matched control by the registered margin". Two things undercut this.

First, the matched control arm, the "expert persona" deletion, failed the experiment's own check for whether a deletion pushed the model into abnormal behaviour. That check (the "Δnll gate") measures how much worse the model gets at predicting ordinary text. Table 1 shows the control at +0.1244 against a bound of 0.0893 (marked ❌). By the paper's own logic, a deletion that fails this gate is "not-testable", because its damage could be generic breakage rather than anything specific. The differential therefore compares the primary condition against an arm the experiment would itself refuse to read. The main text never says this. It appears only as a cross mark in the table. The lock document records it ("the k=16 control arm is NLL-OOD-excluded, so the differential's control comparison carries that flag"; `experiments/01-self-indexing-removal-test/thresholds.md`, and again in `removal-test-findings.md`), but the paper drops the flag.

Second, the differential itself is statistically weak. It is computed on 32 items, and the same items were scored under both deletions. From the raw per-item file I count:

- 6 items failed under the primary deletion but not under the control;
- 1 item failed under the control but not under the primary;
- 1 item failed under both.

The standard exact test for paired yes/no outcomes (McNemar's test) gives two-sided p = 0.125 for a 6-versus-1 split. The paper's own interval, +0.156 [0.000, 0.312], touches zero, as the paper concedes. The paper's own sensitivity analysis, which resamples whole task categories as well as items (the "two-level" bootstrap), gives [−0.0625, +0.469] in `removal_ci.json` under `sensitivity_two_level.derived`. That interval clearly crosses zero, and the paper does not report it (see point 4).

There is also one control arm, not a set of them. The registered rationale for δ, the required margin over the control, says δ must exceed "the spread of d_task(C_ctrl) across the several matched control structures" (`thresholds.md`, "How each threshold gets set"). In the registered run that spread could not be estimated, because only one control was run.

**What would fix it.** In the abstract and main text, say plainly that the matched control failed its validity gate, and that the differential therefore compares the primary condition with an arm the experiment would not read. Report the paired exact test (6 against 1 discordant items, p = 0.125) next to the bootstrap interval. Report the two-level interval for the differential. Then replace "exceeding a matched control by the registered margin" with wording that says the point estimate crossed the line and the comparison is not statistically distinguishable from no difference.

### 2. The router-control verdict rests on one item, and "dropped as much" is read as equality that the data cannot show

**The problem.** The router control (registered as RT-05) is the rule that voids the headline. It was registered in words, with no number: the loss condition fires "if `d_task^syntax` is as large as `d_task^sr`" (`pre-registration.md`, the RT-05 amendment). In the run it was applied as a comparison of two point estimates, "d_task^syntax (0.133) ≥ d_task^sr (0.100)" (`removal-test-findings.md`). That is 4 flipped items out of 30 against 3 out of 30, a one-item difference between two independent 30-item batteries.

The abstract states the conclusion as fact: "a zero-reasoning turn-boundary task degraded as much". The main text reads the interval this way: "gap +0.033, 95% CI −0.133 to +0.200 — statistically indistinguishable". An interval that includes zero shows that the data cannot rule out "no difference". It does not show that the two drops are equal. To claim equality, which is what "as much" asserts, the whole interval has to lie inside a stated margin of practical equality. That is the logic of an "equivalence test". I computed a standard score-based interval for the difference of two independent proportions (Newcombe's method). The 90% interval, which is the one used for a 5% equivalence test, is about [−0.11, +0.18]. It does not fit inside a ±0.10 margin, so the data cannot claim equivalence at the size of the paper's own thresholds. The data are equally compatible with "the router control fired" and "it did not".

A small simulation shows how weak the rule is at these sample sizes. Suppose the two batteries have the same true failure rate of 10%. Then the "≥" rule fires about 58% of the time. In other words it is close to a coin toss.

The paper does acknowledge this later, in the main text ("one the data cannot tell from nothing") and in the Discussion ("turned out to span zero"). But the abstract and the verdict section still present the voiding as an established equality.

**What would fix it.** State in the abstract and the verdict section that the router rule fired on a one-item difference that is statistically uninformative. The statistically honest verdict for experiment 1 is "undetermined between the router and centre readings at this battery size", which the reassessment paragraph already gets close to. Say that the registration gave "as large as" no tolerance and that the point-estimate "≥" was how it was applied. Any rerun should register an equivalence margin.

### 3. Every registered verdict sits on a knife edge, and the design has no power analysis

**The problem.** Power is the chance that an experiment detects an effect that really exists. Nowhere does the paper say how likely its decision rules were to return each verdict under plausible true effects. At these battery sizes, the answer is that the verdicts are largely set by item counts.

- **The self-relevant battery sits exactly at threshold.** The rule for the centre outcome (H_center) needs a drop of at least θ_task = 0.10 on both task batteries. The self-relevant battery dropped 3 of 30 = 0.100, "exactly at threshold" (`removal-test-findings.md`). One item fewer and H_center would not have fired at all, so the router control would never have been needed. The analysis code, as written, would also have scored it below threshold. In floating point, the code's expression `1 − mean(correct)` evaluates to 0.09999999999999998 for 27 of 30 correct, which fails `≥ 0.10`. I checked this with the project's own Python environment. The verdict was applied by hand (the runner's docstring says the rule is applied "in the analysis step"), so the verdict is not wrong. But the paper should say the threshold is met exactly, and in item counts.
- **The threshold has no false-positive rate behind it.** θ_task = 0.10 was set as "≥3 flipped items" above a "null band" whose "upper edge ≈ 2 items". The null band means the movement seen under deletions that should do nothing. It was estimated from about four pilot interventions (`theta-delta-lock-memo.md`, "Null band": idxres k=1, expert k=4, an SAE random control), not from a distribution of null runs. Some of those pilot numbers were on batteries scored before the cull. So the false-positive rate of θ_task is unknown. On the 32-item battery, 0.10 means at least 4 items (3/32 = 0.094), so it is not the "≥3 items" stated in the rationale.
- **How often the rule could succeed.** I simulated the registered conjunction, 4 deletions × 3 batteries × the thresholds, each item flipping independently. Scenario A is a real centre: true drops of 0.20 on both task batteries, 0.05 on the control, 0.05 on the router battery. In scenario A the full H_center rule fires only about 64% of the time. Scenario B is a router-like reality close to what was observed (0.20 / 0.10 / 0.13 / 0.06). In scenario B, H_center fires about 17% of the time. Looking at the parts separately: with a true self-relevant drop of exactly 0.10, the θ_task part fires only 59% of the time. With true drops of 0.15 against 0.05, the δ part fires only 44% of the time.
- **Pilot and test disagree.** The same deletion at rank 16, on the same model, gave a different pattern in the pilot (`prelock-findings.md` §b):
  - The self-relevant battery did not move at all (0.933 at baseline and after).
  - The router battery dropped hardest (0.833 → 0.600).
  - Judged self-report rose (d_self −0.131).

  In the held-out test, the self-relevant battery dropped 3 items, the router battery 4, and self-report fell (d_self +0.059). These are different item sets, so some difference is expected. Still, the swings are as large as the effects the rules are reading.

**What would fix it.** Add a design-sensitivity paragraph to Methods §Statistics. It should give the smallest true effect each rule could detect at 30–32 items, and the probability of each registered verdict under a centre-like and a router-like scenario. State the thresholds in item counts (for example, "θ_task = 0.10 means at least 3 of 30 or at least 4 of 32"). Report that the self-relevant battery met the threshold exactly. Say that θ_task was not calibrated against a false-positive rate. These belong in the limitations alongside "one pass per condition".

### 4. The intervals are computed by a method that misbehaves at these sizes, and the robustness check is misdescribed

**The problem.** The intervals are "nonparametric percentile bootstrap, B = 10,000 … resampling items within battery" (Methods §Statistics; the code is `src/mvm/stats.py` `item_draws` and `summarize`). In plain terms: the analysis re-draws the battery's items at random, with replacement, 10,000 times, and takes the middle 95% of the recomputed drops. With 30 yes/no items and a few failures, this method is known to give intervals that are too narrow. When there are zero failures it collapses to a single point.

- Table 1 reports the expert control's self-relevant drop as "0.000 [0.000, 0.000]". That says the experiment is certain the true failure rate is exactly zero, which no 30-item sample can show. The exact binomial interval for 0 of 30 (the Clopper–Pearson interval) is [0, 0.116].
- For the primary T_si drop (7 of 32), the exact interval is [0.093, 0.400], against the reported [0.094, 0.375]. The upper end is noticeably wider.
- The same zero-width artefact appears in the reread file `reread-under-the-map-2026-10-24.json` (for example, coreference_binding "ci95": [0.0, 0.0]).

The item-level bootstrap also assumes the items are independent draws. They are not. Methods says the held-out items were "authored … as shape-clones of baseline-passing forms only". Each battery has only 3 or 4 categories: T_si has four categories of 8 (I counted from the raw file), and T_sr and T_syntax have three of 10 each. Items within a category are near-copies of each other, so they tend to fail together, and an item-level interval understates the uncertainty.

The paper's robustness check is meant to address exactly this, and it is described wrongly. Methods says the two-level, category-then-item bootstrap "widens the primary condition's d(T_si) interval to [0.000, 0.594] … and leaves the other intervals essentially unchanged". `removal_ci.json` (`sensitivity_two_level`) shows otherwise:

- the differential over the control goes from [0.000, 0.312] to [−0.0625, 0.469], and now crosses zero;
- the primary router-battery drop goes from [0.033, 0.267] to [0.000, 0.300];
- the directional T_si drop goes from [0.031, 0.250] to [0.000, 0.281];
- the expert router-battery drop goes from [0.000, 0.233] to [0.000, 0.333];
- every d_self interval widens by about a quarter to a third.

Separately, a two-level bootstrap that resamples only 3 or 4 categories is itself unreliable, because there are too few categories to estimate how much they vary. What that analysis really shows is that the experiment cannot measure how much damage varies between kinds of task.

The intervals also leave out two sources of variation. The first is the judge: each condition's self-report was scored in one judge pass, while the pilot baseline used the mean of two passes (`prelock-findings.md` §b). The second is run-to-run decoding: repeat-run stability is reported for Δnll and for judged-score drift, but not for which items flip.

**What would fix it.** Report exact or score-based intervals for single proportions (Clopper–Pearson or Wilson), Newcombe intervals for differences between independent batteries, and an exact paired interval or McNemar test for the paired differential. Keep the bootstrap as secondary if you wish. Correct the description of the two-level sensitivity analysis, and report its differential interval. Say plainly that items are clustered by category, and that 3 or 4 categories are too few to estimate between-category variation.

### 5. The validity gate that admitted the primary condition is itself estimated from 20 draws, and the margin is inside its noise

**The problem.** The validity bound for rank-16 deletions, 0.0893 nats, is "the 95th percentile of Δnll over 20 random rank-k subspace ablations". The primary condition passed at 0.0867, a margin of 0.0026 nats, which the paper carries as "an honest marginality". From the calibration file (`/Users/john/Code/minimum-viable-mind/artifacts/substrate-migration/tulu-sft/prelock/ood_calibration.json`, `bounds/k16/null_dnll`), the 95th percentile of 20 values is effectively the second-largest value: 0.0877 + 0.05 × (0.1189 − 0.0877) = 0.0893. Two of the 20 random deletions were more disruptive than the primary. So the primary sits at about the 90th percentile of random deletions, not clearly inside the null range.

Twenty draws estimate a 95th percentile poorly. Resampling the 20 null values 20,000 times gives a 95% range for the bound of about 0.054 to 0.119. In about 39% of those resamples the bound falls below 0.0867, and the primary condition would have been excluded. The admission of the paper's central condition is therefore itself within calibration noise. The same applies to the rank-8 and rank-16 re-admissions "by margins of 0.003–0.007 nats".

In fairness, the procedure was fixed before the run and binds in both directions, and the paper says so. But a fixed rule applied to a noisy estimate is still noisy, and the paper treats the gate as a hard yes or no.

**What would fix it.** Report the bound with its own uncertainty. State that the primary condition is at about the 90th percentile of the 20 random deletions. Say that its admission would not survive a modest change in calibration draws. Ideally, rerun the null calibration with more draws (a few hundred random subspaces is cheap relative to the claims resting on it). At a minimum, include this in the limitations.

### 6. "Never reduced" self-report is an equivalence claim made with an interval that leaves out the judge

**The problem.** The abstract says "Judged self-report was never reduced by any on-manifold intervention". The main text says "the primary condition's d_self (+0.059 …) is within control wobble" and calls the interval's upper end "a quantified ceiling". Three issues.

1. The point estimate is a reduction. Self-report fell from 0.6375 to 0.600 (my recount of `s_scores_baseline.json` and `s_scores_idxres_mean_k16.json`). The defensible statement is "no reduction as large as θ_self = 0.25 was detected", not "never reduced".
2. The "ceiling" is a 95% two-sided upper bound of 0.185. That is a relative reduction of up to about 18.5%, which is not negligible, and it is an item-only interval. Each condition was judged in one pass. The judge's own scoring noise, measured in the pilot as a "control-arm d_self wobble 0.05–0.07" (`theta-delta-lock-memo.md`), is not in the interval. The repeat-pass drift of |Δ| = 0.008 refers to the whole battery's average, not to a difference between conditions. Including judge variation would push the upper bound up, and possibly towards θ_self.
3. The same deletion moved d_self from −0.131 in the pilot to +0.059 on the held-out set, a swing of about 0.19 in the same model. Even granting that the item sets differ, that swing is larger than the interval's half-width suggests the estimate should move.

**What would fix it.** Reword the abstract to "no reduction as large as the registered threshold was detected". Judge each condition at least twice and fold judge variance into the interval, for example by resampling judge passes as well as items. Say which variation sources the upper bound covers and which it does not.

### 7. Several headline comparisons carry no uncertainty at all, against the Limitations' claim of intervals "on every quantity"

**The problem.** The Limitations say there are "95% item-resampling CIs on every quantity". That is true only for Table 1 and the reread. The alignment ladder carries a section title ("Alignment edits the policy, not the geometry") and an abstract sentence, but has no interval or test.

- **Deflection.** Baseline deflection "falls 0.533 → 0.333 → 0.267 (Instruct 0.100)". On the 30-item self-report battery that is 16, 10, 8 and 3 of 30 (the per-rung counts are in `rt06-ladder-findings.md`). The exact two-sided test comparing two proportions (Fisher's test) gives p = 0.064 for SFT against RLVR (16/30 against 8/30). Only the comparison against the vendor Instruct model (3/30, p ≈ 0.0006) is clear. So "changes markedly" across the Tülu rungs is not established at the conventional 5% level.
- **Geometry.** "The localised geometry … is stable across all rungs" is a claim of no difference. As with point 2, it needs a stated margin and an interval inside it, not the absence of a visible change.
- **Leakage.** "Cross-patch leakage … falling (0.059 → 0.026 → 0.020)" has no intervals.
- **Localisation.** The numbers in the localisation section have no stated uncertainty either: margin +0.56, restoration 0.206, |cos| 0.28, cross-patch 0.05–0.06 against a 0.5 line. The last of these is far from its line and probably safe, but the reader cannot tell.

**What would fix it.** Add counts and exact intervals or tests for the ladder deflection rates and the leakage ratios. Either state an equivalence margin for "geometry stable" and show the rungs fall inside it, or soften it to "no change detected". Correct the Limitations sentence to say which quantities carry intervals.

### 8. The family-wise bar in the A3 localisation sweep depends on a normal approximation that its permutation null cannot support

**The problem.** The Amendment A3 sweep ran 135 tests and reports that nothing crossed "a family-adjusted bar of 3.38 sd" (main text, nulls item iv). A "family-adjusted bar" is one raised to allow for running many tests at once. I checked that 3.38 is the one-sided Bonferroni correction for 135 tests at 5% (normal quantile for 0.05/135 = 3.37), so the arithmetic is right. But margins are expressed in standard deviations of a label-permutation null built from 200 shuffles: the one marginal result "zero of 200 draws met or beat it" (`experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings.md`). With 200 shuffles, the smallest p-value the permutation null can show is about 1/201 ≈ 0.005. The family-adjusted bar corresponds to p ≈ 0.00037. So the bar is enforced only by assuming the shuffled accuracies follow a bell curve far into its tail. That was never checked. Accuracy over four classes is discrete and can be skewed, and the findings themselves note that 73.6% of seed-2 fits hit the optimiser's pass cap.

The same "margin in sd" convention runs through the blind arm (1.30 sd against a bar of 3) and the blind control. In those cases the conclusions (nothing found) are not sensitive to this. The open "MARGINAL" item, and the sensitivity figure later corrected to "one episode in eleven", do depend on the tail being right.

Separately, the paper singles out "the highest testable position on all three checkpoints (+2.33, +2.39, +3.34)". That position was chosen after seeing the results, so its consistency should not be read as evidence (the findings file says as much, but the paper's sentence invites the reading).

**What would fix it.** Either report exact permutation p-values with enough shuffles to resolve the family-wise level (several thousand per test), or check the normal approximation against the 200 shuffles and say so. Label the "same position on all three checkpoints" observation as chosen after the results were seen.

---

## Minor points

1. **Category count.** Methods says the pilot T_si battery has "eight categories". The held-out T_si battery has four categories of eight items (`removal_test_scores.json`, `by_category`). State the category structure of the test batteries, since the two-level interval depends on it.
2. **Item counts.** "122 items authored …; 92/92 surviving baseline verification" leaves the reader to work out that 30 items were culled. Give per-battery authored, culled and kept counts. Also note that keeping only items the unmodified model gets right makes every drop a drop from 1.000. Fragile but correct items are then over-represented, which affects absolute drops for every arm.
3. **Drops after the fact.** "Six of the seven flipped self-irrelevant items are multi-step-reasoning items (6 of 8 in that category, against 1 of 24 elsewhere)" is a subgroup found after looking at the flips. Label it as such. It should not be given the weight of a test.
4. **Table 2 standard deviations.** The sds measure evaluation-sampling noise for one trained model. The three training seeds are the units for "on three seeds", and no between-seed interval is given. The effects (7.5 to 8.6 times θ) are so large that this does not change the conclusion. The corrected drop appears to be a mean of per-seed ratios: from the table means, the ratio of means gives 1.338, 1.334 and 1.523, against the reported 1.337, 1.342 and 1.528. Say which, and note that the ownership-blind ceiling of 0.2921 is itself an estimate, carried into a denominator of about 0.27.
5. **Experiment C learning gate.** "Gate on learning … bar 790" of 3,000. If chance is one in four, as the four-agent design suggests, 790 is almost exactly the one-sided 5% point above chance: the 95th percentile of 3,000 guesses at 0.25 is 789, and P(≥ 790) = 0.049. It tests "better than chance", not "learned". Name it accordingly. Part B was read on one seed, which the procedure itself flags ("gate not decidable on one seed"). The failures (0.000 and 0.024 against 0.5) are too large for that to matter, but the text should say so.
6. **Battery entry 1.** The gate failed at 16 of 59 = 0.271 against a bar of 0.20. That is a point estimate against a line: the one-sided binomial p against 0.20 is about 0.12. The repair attempt's 0.712 is decisive, so the conclusion stands, but the first failure should be described as a point-estimate miss.
7. **Battery entry 2.** The paper says "the null reading needs a difference of at most 0.10 either way". The method file (`docs/filtered-battery-2026-10-07/rehearsal-method-entries-1-2.md` §3) also requires the whole interval to lie inside the directional band. Describe the rule as registered. Also, the interval (−0.184 to −0.023) excludes zero. The data show a non-zero difference that falls between the method's reading bands. Say this directly rather than through "a margin of one cell", because the distance of a point estimate to a band edge, counted in cells, is not the relevant uncertainty.
8. **The reread under the revised account.** The routine group has n = 8, with 1 failure. Its bootstrap interval [0.000, 0.375] is narrow for that reason. The exact interval for 1 of 8 is about [0.003, 0.527]. The conclusion (unreadable) only gets stronger, but use the better interval.
9. **The companion result.** The retained-independence result mixes units: 1,080 conversations, 540 ladders, 105 "masked cells" against 11 capitulations. It also gives ranges (0.87–1.00, 0.07–1.00) with no intervals. Either give counts with intervals in matching units, or cut it to a one-line pointer until it is reported in full.
10. **Baseline self-report.** "Baseline S identical across pilot and held-out sets (0.6375)": the pilot figure is the mean of two judge passes and the held-out figure is a single pass. Say so, since the match is used as evidence that the battery construction transferred.
11. **Multiple comparisons in Table 1.** Table 1 gives 16 intervals plus 3 derived ones, and the text draws on several of them: "the self-irrelevant battery dropped hardest", and the directional cross-check. The registered verdict is a conjunction of conditions, which needs no adjustment. Descriptive claims drawn from the other cells should be labelled as unadjusted.
12. **Abstract interval.** The abstract quotes the percentile interval 0.094–0.375 for the primary T_si drop. If you adopt exact intervals (point 4), update it to about 0.093–0.400.

---

## Recommendation

Revise. Major revision is needed on the statistics of experiment 1: the abstract's three headline readings (control exceeded, router equal, self-report never reduced) should be restated in terms the 30-item batteries can support. The intervals should be recomputed by methods that behave at these sizes. The two-level sensitivity result should be reported as it actually came out. The validity gate's own uncertainty should be disclosed. The constructed-line results need only the minor corrections listed above.

revise
