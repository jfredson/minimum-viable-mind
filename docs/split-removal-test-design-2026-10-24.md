# The split removal test: a design on paper

*Version 0.1, written 2026-10-24 (Saturday, Pacific). Step 4 of `docs/next-steps-2026-10-24.md`, on John's ruling of 2026-10-24 (`docs/rulings/2026-10-24-revised-theory-next-steps-ruling.md`). This is a design, not a registration.*
- *Nothing has been run, downloaded or spent.*
- *Before it can be registered it goes through the project's outside-review protocol (`docs/outside-review-protocol.md`): the advisory review on a proposal (Gate C), a measurement rehearsal, and the review of registration text (Gate A).*
- *Running it comes back to John first, with an estimate and a ceiling.*

## 1. The question

The revised assembled-time theory bets that a point of view is a split between what a system does and what happens to it, which the system's own processing uses (positions ledger entry 32, in the sentient-horizons repository). It names a test, the removal of the split, and predicts a particular kind of loss: **practised routines carry on, while flexible response to something new collapses, including on tasks that have nothing to do with the system itself**. Removing other things should give other kinds of loss:

- removing only a description of the self should flatten only the system's talk about itself;
- removing an essential part should break everything at once, which shows nothing;
- a random removal of the same size should change little.

For a language model in conversation, the essay names the candidate: a run keeps its own earlier words apart from the user's ("A single model run"). This test removes that difference from the inside of an open model, leaves everything else in place, and reads which kind of loss follows.

**What one run of this test can and cannot do.** It places one model on the map: either the split is shown doing work in this model, or it is not shown. It cannot by itself refute the theory's bet. The essay's own way for the account to lose is broader: if careful investigation found, every time, that the split was one more description. A run here is one such investigation, and its result is reported as that, never as a verdict on experience.

## 2. What is removed, and how we know it was removed

**The target.** The target is the information inside the model that marks a word as the model's own rather than the user's. It is located the way experiment 01 located its structure, with the confound controls that experiment needed:
- the same words appear on both sides, and only the conversation decides who said them;
- the two sides are matched for length and position;
- generic speaker tracking is ruled out by a third-party speaker condition.

**Two ways of removing it, which must agree.**
- **(a)** Erase the linear direction or directions that a probe uses to tell own words from user words, at every position and at the layers where the probe reads it. This is done with a standard method that removes exactly the linearly readable information and nothing else.
- **(b)** Ablate the dictionary features (from a sparse autoencoder, a published tool that splits a model's internal activity into readable parts) that separate own from user words.

The re-reading of the July test found that its two removal methods produced different patterns (`experiments/01-self-indexing-removal-test/reread-under-the-map-findings-2026-10-24.md`). So here a pattern is read only if both methods produce it.

**The check that the removal happened (manipulation check).** After the removal, a fresh probe trained on the removed model must fail to tell own words from user words: its accuracy must be at or within a stated margin of chance. Tasks that ask directly "which of these did you say?" must also fall. If this check fails, the result is **not testable: the split was not removed**, and nothing else is read.

**The check that the model was not simply broken (staying on the model's normal range).** Perplexity on neutral text, meaning how surprised the model is by ordinary text, must stay within a band fixed beforehand against random removals of the same size. This is the dual check experiment 01 used to avoid reading a broken model as a meaningful loss. If it fails, the result is **not testable: the removal left the model's normal range**.

## 3. The comparison removals

| Removal | What it stands for | Expected loss |
|---|---|---|
| **The split** (section 2) | The theory's candidate for a point of view | The theory's prediction: new problems collapse, routines carry on |
| **The self-description** | The model's picture of itself as the speaker ("I am an assistant"), located by the narrative method of experiment 01 | Only talk about itself flattens |
| **An essential part** | A component the model cannot run without, chosen in advance for calibration only (for example, the layer whose removal most raises perplexity in a pilot) | Everything fails at once |
| **Random, same size** | Directions of the same number and strength, drawn at random | Little changes |
| **Another distinction, same size** | A direction marking a different property of words that is not about who said them (for example, inside or outside quotation marks), located the same way | Little changes, or a small general loss |

The last two removals give the size of loss that means nothing. A loss from removing the split counts only where it beats both.

## 4. The tasks

There are four task groups, two by two, plus the manipulation-check tasks and the self-talk tasks.

| | Not about the model | About the model (uses its own earlier words) |
|---|---|---|
| **Practised routines** (one familiar step) | e.g. common arithmetic facts, spelling, capitals, finishing a familiar phrase, applying a common formatting rule | e.g. repeat the number you said, say the word you were asked to say |
| **New problems** (a rule or situation the model cannot have practised) | e.g. a made-up game whose rules are given in the prompt; an invented symbol system to decode; a puzzle combining two stated rules in a way no worked example shows | e.g. apply a newly given rule to your own earlier answer; continue a made-up game in which your earlier move constrains the next one |

**What the re-reading of the July test taught, built in:**
- **At least 40 items per cell.** A difference of 0.2 between routine and new is then readable; the July test had 8 routine items not about turns, which was never enough.
- **"New" means new to the model,** not a familiar shape with fresh content. Each new-problem item uses invented rules or symbols, and is checked against the model at baseline to confirm it is solvable from the prompt alone and not from memory.
- **Several categories of new problem, each read separately,** so that a loss concentrated in one task type is not read as a loss across flexible response. Six of the July test's six flexible failures sat in one category.
- **Routine tasks never depend on who said what.** That dependence is what the removal targets, so it would damage them for a reason that has nothing to do with selectivity.
- **Every item passes at baseline,** the cull rule of experiment 01 (`test-set-authoring-spec.md`, rule 3), so every failure after a removal is a drop.

**Self-talk tasks:** first-person descriptions of the model's own activity, scored on a rubric that does not reward first-person words, as experiment 01's self-report scoring was revised to do.

## 5. Outcomes, stated before any run

Every figure is an item-level drop with an interval of 95% from resampling items. The thresholds named δ are fixed in a pilot on separate items before the test set is touched.

1. **The selective loss the theory predicts** (the split is shown doing work in this model). All of these hold:
   - the manipulation check and the normal-range check pass;
   - both removal methods agree;
   - the drop on new problems not about the model exceeds the drop on routines not about the model by at least δ, with the interval above zero;
   - that gap exceeds the same gap under both the random and the other-distinction removals;
   - the routine drop not about the model is no larger than the random removal's plus δ.
2. **A description only** (on this model, the candidate split behaves as a description). The removal flattens self-talk, and possibly tasks about the model, while both task groups not about the model drop no more than under the random removal.
3. **A general loss** (the candidate is an essential part here, which shows nothing). Routines and new problems not about the model fall alike, within δ, and both fall well above the random removal.
4. **Nothing** (the information was removed, and nothing beyond self-talk changed). The model does not use a split for what these tasks need. On the map this places the model as having binding without the split being shown, as the essay places the compiler. It is not a result against the theory.
5. **Not testable.** The manipulation check fails, or the normal-range check fails, or the two removal methods disagree on which outcome holds.

**What would count against the account,** in the essay's own terms: outcome 2, repeated across models and removal methods. That would mean the candidate split, every time it is removed, turns out to be one more description. One model cannot show this. The registration names how many models the project would need before it reports outcome 2 as evidence against the bet, rather than as a placement of one model.

## 6. The models, and what it would cost

- **Development and pilot:** `google/gemma-2-2b-it`, the project's bench model (`src/mvm/config.py`), with its published dictionary of features (Gemma Scope). This can run on this Mac, at the cost of a download of about 5 GB and processor time. Experiment 01 found this model's heavy safety training tangles "self" with dialogue mechanics, which is why it was the sandbox there and not the registered model. That matters less here, because the split is about who said what rather than about the persona. Even so, the design does not rest on one model.
- **Registered run:** the 2-billion-parameter model, and the 8-billion-parameter model experiment 01 registered (`allenai/Llama-3.1-Tulu-3-8B-SFT`), which needs a rented machine. The estimate and ceiling are written in the registration and come to John before anything is rented. The removal code from experiment 01 (`experiments/01-self-indexing-removal-test/src/`, and `src/mvm/ablate.py`) is reused. The new code is the erasure method, the new task batteries and the analysis.

## 7. Order of work

1. **This design is checked** by a session that did not write it, then given the advisory review on a proposal (Gate C). Then John rules on the open choices in section 8. $0.
2. **The batteries are written to an authoring specification committed first:** pilot items and test items kept apart, every item checked at baseline. $0, apart from the bench model's download, which comes to John as a file action first.
3. **The measurement rehearsal on the bench model**, using pilot items only: locate the target, run both removal methods, the manipulation check and the normal-range check, and fix δ. $0 on this Mac.
4. **Registration text, through Gate A** on both review tiers. Then the registration commit.
5. **The registered run**, on John's go, with a ceiling.
6. **Findings, through the interpretation review (Gate B).** Then the paper's paragraph, and a sentence for the essay if John wants one.

## 8. Choices for John before registration

- **How many models before outcome 2 counts against the bet.** *Recommended: at least two models of different families and sizes,* with both removal methods agreeing on each.
- **Whether the self-talk scoring needs an outside judge model,** which would be an API cost, or can use the rubric with a human spot-check, as experiment 01 did. *Recommended: the experiment 01 route, at $0, unless the rehearsal shows the rubric cannot separate the outcomes.*
- **Whether the bench model may be downloaded to this Mac now, for the rehearsal** (about 5 GB). *Recommended: yes, when step 3 begins.*
