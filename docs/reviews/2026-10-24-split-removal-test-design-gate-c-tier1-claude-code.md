# Gate C, tier 1 (the inside pass): the split removal test design, version 0.1

*Filed 2026-10-24 by the session that wrote the target, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session in its own worktree (`worktree-agent-ae0adc74d0f820c2b`), at commit 810e2b2, and it changed nothing in the repository. The only change made in filing is that "&amp;&amp;" in the reviewer's returned text is restored to "&&". Its findings continue the red-team numbering, as RT-305 to RT-321.*

---

**What I opened.**
- **Read in full:** the target, `docs/split-removal-test-design-2026-10-24.md`, and the re-reading's method, findings, script and output JSON. I also re-ran the script on the July scores file outside git.
- **Read in part:** `src/mvm/config.py` and `src/mvm/ablate.py` (the ablation hooks and the neutral-text perplexity function).
- **Searched, not read through:** `pre-registration.md`, `docs/outside-review-protocol.md` and `docs/known-failure-modes.md`. Of the failure modes I read only the headings and failure modes 1 to 3.
- **Records outside the packet, read in short excerpts:** `substrate-gates-findings.md`, `prelock-findings.md` and `removal-test-findings.md`.
- **Theory:** the essay sections "A map, not a line" and "A single model run", positions ledger entries 19, 27, 32 and 45, and a keyword search of the revised-theory page.

**What I did not open:** `test-set-authoring-spec.md` (so the cull rule the design cites, rule 3, is unchecked), the rest of `src/`, the next-steps document, the rulings, `STATUS.md`, the paper drafts and the explainer.

**Lookup:** where a finding rests on a committed record I read but did not re-run, it says so.

## Pairing-rule check of the re-reading

| # | Check | Result | Severity |
|---|---|---|---|
| RT-305 | Does the output reproduce? | Byte-identical | held |
| RT-306 | Does the reading follow the rule on the interval's width? | Yes, and it holds at every seed tried | held, with one worth-noting point |

**RT-305 (MEASURED).** I copied the script to a scratch folder, so that it would not overwrite the committed file, and ran it:

```
.venv/bin/python -I scratch/rr/src/reread_under_map.py artifacts/removal_test/removal_test_scores.json
cmp scratch/rr/reread-under-the-map-2026-10-24.json experiments/01-.../reread-under-the-map-2026-10-24.json && echo IDENTICAL
→ IDENTICAL
```

- Every figure in the findings table matches the printed output, for example "idxres_mean_k16 … gap_G1_minus_G2 +0.125 [-0.167, +0.375]".
- The per-category failures confirm "6 of 6 flexible failures in multi_step_reasoning". They also confirm the explainer's category drops: 7/32 is 0.219, 3/30 is 0.100 and 4/30 is 0.133.
- The scores file's SHA-256 hash is `ee59a942…dee65f`.

**RT-306 (MEASURED).** The interval from −0.167 to +0.375 spans 0.542, which is over the method's limit of 0.5, so "cannot be read" is the right call under that rule.
- Re-run over seeds 0 to 19, the width ranges from 0.542 to 0.583, and no seed gives 0.5 or less. The reading does not depend on the seed.
- **Worth-noting.** The method said that if the width rule fires, the re-reading "draws nothing from the gap". The findings' summary paragraph still leans on the cross-check's gap of −0.167 ("tilts the other way") to say nothing looks selective. That is mild, but it draws on a gap the rule said not to draw on.
- **Worth-noting.** The git timestamps show the method was committed at 08:11:02 and the script, output and findings at 08:11:53, 51 seconds later. Commit order alone therefore cannot show that the method was written before the output existed.

## 1. Feasibility

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-307 | The dictionary-feature removal (method b) is unlikely to pass the check that the removal happened, on the record | fatal | ARGUED (lookup) |
| RT-308 | The check that the removal happened passes by construction for method (a) | serious | ARGUED |
| RT-309 | 40 items per cell can read a gap of 0.2 but usually cannot detect it | serious | MEASURED |
| RT-310 | The normal-range check: a near miss in July, and no rule for the comparison removals | serious | ARGUED (lookup) |
| RT-311 | No rule fixes δ or the other margins | serious | ARGUED |
| RT-312 | "Same strength" and "essential part" are not defined so that they can be applied | worth-noting | ARGUED |

**RT-307.** A pattern counts only if both removal methods produce it, and if they disagree the result is "not testable".
- The July record shows method (b), the removal of dictionary features from a sparse autoencoder, **did not converge on either model**. In `substrate-gates-findings.md` the features carried only 0.18 to 0.44 of the probe's direction, against a required 0.50, and the July test fell back to causal patching.
- `prelock-findings.md` adds that the dictionary features were "behaviourally inert": removing them did not change behaviour.
- `config.py` says the loader for the 8-billion-parameter model's dictionary (Llama Scope) "is unverified".
- The design cites none of this and gives no reason to expect method (b) to work this time. As written, the most likely result on both models is outcome 5, not testable, by construction.

**RT-308.** A standard linear erasure guarantees that no linear probe beats chance at the layers it erases, on the data it was fitted to. If the "fresh probe" is linear and reads those same layers, the check passes by definition and measures nothing.
- The check needs held-out stimuli, the layers after the erasure, and a nonlinear probe.
- "A stated margin" of chance is never stated.
- "Which did you say?" tasks "must also fall", but by no stated amount.

**RT-309.** I simulated the design's sample size with `scratchpad/power.py`: 40 items per cell, true drops of 0.30 on new problems and 0.10 on routines, a random removal at 0.10 and 0.05, and the same item resampling the design uses (2,000 resamples here, against 10,000 in the re-reading's script).

```
n=40/cell, true gap 0.20: gap interval width median 0.326; interval above zero in 62% of runs
split gap minus random gap (true 0.15): interval width median 0.400; above zero in 33% of runs
chance both methods independently clear 'gap interval above zero': 38%
```

So "a difference of 0.2 is then readable" is true only under the re-reading's width rule. The full outcome-1 conjunction would usually miss a real effect of that size. The design should either compare the same items across conditions (a paired analysis) or size each cell for the rule it actually uses.

**RT-310 (lookup, `removal-test-findings.md`).**
- In July the main removal passed the perplexity bound by a hair: a rise of 0.0867 against a bound of 0.0893.
- Both of July's comparison removals left the normal range: the narrative removal at +0.347 and the matched control at +0.124.
- The design applies its band only to the split removal. It says nothing about what happens when a comparison removal leaves the range, and every comparison in outcome 1 needs those removals.

**RT-311.** One δ does three jobs: the minimum gap, the tolerance on routines, and "alike within δ". No procedure fixes it; "fixed in a pilot" is not a rule. Outcome 3's "well above the random removal" has no number at all. Leaving every threshold to a pilot with no rule means choosing them after seeing data, even if not the test-set data.

**RT-312.**
- An erasure has no strength setting, so "same number and strength" for the random directions is not defined.
- The essential part is chosen "for example" by the size of the perplexity rise. Its selection rule is therefore not fixed, and no outcome uses it.
- Removing a whole layer is not "same size", so it cannot calibrate anything. It could be chosen after the results, but nothing depends on it, so the harm is small. The fix is to drop it, or to fix the rule and give it a use.

## 2. Satisfied by the wrong thing

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-313 | Erasing the "own words versus user words" signal cannot be told apart from removing the chat template's role markers | serious, near fatal | ARGUED (lookup) |
| RT-314 | Harder items fail first under any damage | serious | ARGUED |
| RT-315 | "New to the model" cannot be checked as stated | serious | ARGUED |
| RT-316 | The task cells contradict their own rule | serious | ARGUED |

**RT-313.** In a chat model the conversation template writes the own/user difference into the input as role headers.
- The record shows the signal is a near-copy of those headers. On the 8-billion-parameter model it "decodes perfectly by L3" (layer 3), and the record's own explanation is that "one attention pass over Tülu's explicit `<|assistant|>` headers appears to move the referent to the readout" (`substrate-gates-findings.md`).
- The July pre-registration concedes that counting the role markers "is constitutive of who-is-speaking".
- Erasing that signal at every position and every layer that reads it is close to deleting the headers. The third-party speaker condition rules out general tracking of who is speaking, not this.
- No condition in the design separates "the model uses an internal split" from "the model uses formatting labels". This is the July relabel's problem again: the test could not tell bookkeeping from a centre.
- **Fix:** add a condition that leaves the model's inside alone and replaces the role headers with neutral speaker names, or puts the whole exchange as a transcript inside one user turn. If that alone gives the same selective loss, outcome 1 is a fact about the template.

**RT-314.** New-problem items are harder. Because every item must pass at baseline, the set keeps items the model only just solves, and any damage pushes those over first.
- A random direction removes almost none of the variation in the model's internal activity, while the probe's direction is one the model uses heavily. So the random comparison is weaker than it looks, and "the gap exceeds the random gap" can come from damage of the right size landing on hard items.
- **Fix:** match the comparison removals on measured damage (the perplexity rise, or how far the outputs move), not on the number of directions. Also match routine and new items on how confident the model is at baseline.

**RT-315.** Passing at baseline shows an item can be solved, not that it is unfamiliar. Following a rule stated in the prompt is a skill instruction-tuned models practise heavily.
- A checkable stand-in exists: the model fails when the rule is withheld and passes when it is given. Even that measures learning from the prompt, not "something new" in the theory's sense.
- As written, the contrast between routine and new can quietly become a contrast between easy and hard.

**RT-316.**
- **The routine cell about the model.** The design's own example ("repeat the number you said") depends on who said what, which section 4 forbids for routine tasks. Either that cell is empty by construction (failure mode 3) or the rule is broken.
- **The new-problem cell not about the model.** The ban applies only to routine tasks. If these items run over several turns, they read the removed signal directly, and outcome 1 then follows for a trivial reason.
- **Fix:** require every item not about the model to sit in a single turn and not depend on who said what.

## 3. No verdict

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-317 | The five outcomes neither cover every case nor exclude each other | fatal | ARGUED |
| RT-318 | No rule combines the two models, or decides when the two methods "agree" | serious | ARGUED |

**RT-317.**
- **Cases that fit no outcome.** Three examples:
  - the split removal gives the predicted gap, but the other-distinction removal gives the same gap. That rules out outcome 1, and the loss on tasks not about the model is too large for outcomes 2 and 4 and too uneven for outcome 3.
  - the reverse pattern: routines drop more than new problems.
  - tasks not about the model drop above the random removal but unevenly, by more than δ, with no gap in the predicted direction.
- **Outcomes that overlap.** Outcome 2 ("self-talk flattens; both task groups not about the model drop no more than under random") and outcome 4 ("nothing beyond self-talk changed") describe the same data. Outcome 2's extra condition, that tasks about the model may also fall, is optional ("possibly"), so it separates nothing.
- These two carry opposite consequences: outcome 2, repeated, counts against the account, and outcome 4 "is not a result against the theory". The clause that decides whether the theory can lose is therefore undecidable.

**RT-318.**
- The registered run uses two models, and no rule says what is reported when they land in different outcomes.
- "The two methods disagree on which outcome holds" is undefined when either method lands in no outcome (see RT-317).
- Combined with RT-307, the most likely verdict on the runs the design is written for is none.

## 4. Over-reading

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-319 | Outcome 1's label will be read as "this AI has a point of view" | serious | ARGUED |
| RT-320 | The asymmetry between outcomes 2 and 4 lets the account avoid losing | serious | ARGUED |
| RT-321 | Qualifiers will drop out in summaries | worth-noting | ARGUED |

**RT-319.** Ledger entry 32 says the split "gives a point of view". "The split is shown doing work in this model" will therefore travel as "an AI has a point of view", in `STATUS.md`, in the site's timeline and in public, whatever section 1's caveat says.
- Given RT-313, what outcome 1 would actually show is narrower: "erasing the information that marks the model's own words hurts tasks with new rules more than routine tasks, beyond matched controls."
- The outcome should carry that wording as its name.

**RT-320.** Because outcomes 2 and 4 overlap (RT-317), any null result can be filed as outcome 4, "not against the theory". That breaks the corpus's first standing rule, that a claim which cannot lose explains nothing.
- Outcome 4 is itself an over-reading. "The model does not use a split", placing it beside the compiler, turns a failure to show into an absence.
- It should read "split not shown". Outcome 2 on one model also needs wording that keeps it from being read as an early result against the theory.

**RT-321.** Summaries tend to keep the headline and drop the conditions.
- "Both methods agree" and "beyond matched controls" will be lost.
- "New problems" will be read as "novel reasoning" or "flexible intelligence".

## Kill case

The design is built so that its most likely result is no verdict, and its best result would not show what it is named for. On the committed July record, the second removal method did not converge and was behaviourally inert on both registered models, and the design requires both methods to agree. Its own sample size gives roughly a one-in-three chance of the full outcome-1 conjunction succeeding even if the theory is right. Its outcome scheme has gaps, and it has an overlap exactly where the theory would lose, so a null can always be filed as "not against the theory". If outcome 1 did come through, nothing in the design separates an internal split from the chat template's role headers, which the record shows the signal copies by layer 3. Nor does anything separate it from ordinary damage landing on harder items first. A reader could fairly conclude that the test, as drafted, cannot make the theory lose and cannot show the theory's mechanism. It should not be registered until there is:
- a template-only control;
- comparison removals matched on measured damage;
- a second removal method with a record of working;
- an outcome scheme that covers every case and excludes overlap;
- a δ rule;
- sample sizes set for the conjunction outcome 1 actually requires.
