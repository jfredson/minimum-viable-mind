# Do the template conditions already test "take the speaker cue out of the input"?

*Written 2026-10-24 (Saturday, Pacific). A read-only check on John's ruling of the same day, relayed by the fifth weekend master session: "Record that the split can't be removed from inside this model, and have the session check whether the existing template tests already cover the take-it-out-of-the-input version before designing anything new." Nothing was run and nothing was spent. Sources:*
- *the design (`docs/split-removal-test-design-2026-10-24.md`, version 0.6, sections 2, 3 and 5);*
- *the battery specification (`experiments/09-split-removal-test/battery-authoring-spec.md`, section 6);*
- *the generator's three template functions (`experiments/09-split-removal-test/src/batteries.py`, `render_t1`, `render_t2`, `render_t3`);*
- *the review finding that introduced them (RT-313, in `docs/reviews/2026-10-24-split-removal-test-design-gate-c-tier1-claude-code.md`).*

## The short answer

**No.** The template conditions do not answer whether the split goes away when the speaker cue is taken out of the input. There are four reasons:
- they were built for a different job;
- on the tasks that decide the outcome, they take away no cue at all;
- where they do change the cue, they relabel it rather than remove it;
- none of them has been run.

## What the template conditions are, and what they were for

The inside pass of the design's review raised the problem in finding RT-313. In a chat model, the conversation template writes "this is the model speaking" into the input, as role headers. Erasing the signal inside the model might therefore amount to deleting the headers. The fix was to add conditions that leave the model's inside alone and change only the input:

- **T1** prefixes each turn with a neutral name, "Speaker Ash:" or "Speaker Birch:", with the model's turns as Birch. Note that the generator keeps the turns inside the model's normal turn markers (`render_t1`, and battery specification section 6). So T1 *adds* names and leaves the role headers in place. The design's own table says T1 "replaced" the headers, so the design text and the code do not agree. T1 as built removes nothing.
- **T2** gives the whole exchange as a labelled transcript ("Ash: …", "Birch: …") inside one user turn, followed by the question.
- **T3** gives the model's own sampled words and the user's words as unlabelled paragraphs inside one user turn. It is not a task condition. It reads whether the located signal is still there without headers.

Their job, in section 5 of the design, is a **check on a positive result**. If removing the split from inside the model gave the predicted pattern, and T1 or T2 alone gave the same pattern, then the result would be renamed "Template": a fact about the chat format, not about the split. They are a guard against one misreading. They are not a test of their own, and they never decide an outcome on their own.

## What they cover, and what they leave out

**What they cover.** They would show whether the model's performance on the routine and prompt-rule tasks changes when the chat format changes. That is real information, but it is about sensitivity to the format.

**What they leave out:**

1. **On the cells that decide the outcome, there is no cue to take away.** Every routine and prompt-rule item is a single user turn (design, section 4, finding RT-316). The model's only "own words" in those items are the reply it is writing now, and under T1 and T2 it still writes that reply in its own marked turn. So on the outcome cells, T1 and T2 change only the wrapping of the question. The cue that marks the model's words as its own is untouched.
2. **Where the cue does change, it is relabelled, not removed.** On the multi-turn items (which-did-you-say, and the model's own earlier answer), T2 drops the model's turn markers but presents its earlier words as a third party's ("Birch"). That replaces "I said this" with "someone named Birch said this". It is a swap of labels, not an absence of one. And those cells are excluded from the outcome by design.
3. **Only T3 actually takes the cue out, and T3 reads, it does not test.** T3 is the one condition where the model's own words appear with no speaker cue at all. But it only asks whether the located signal can still be read. It scores no task, so it cannot show a loss.
4. **Nothing has been run.** The template conditions belong to phase 2 of the rehearsal, which never ran because the removal check failed. There is no data either way.

## If a new design is wanted: what it would need (not designed here)

A test of "does the split go away when the cue is taken out of the input" would need at least these parts:

- **Tasks where the model's own earlier words do part of the work.** For example, multi-step problems where the model's own earlier steps must be built on. They would be split into routine and prompt-rule kinds, and not be about the model. The current single-turn cells cannot carry this.
- **A condition with no speaker cue at all.** The model's own sampled earlier words would be shown unmarked, as in T3, with the task scored. One way is plain text continued without the chat format.
- **Two controls, so that losing the cue is not confused with changing the format.** One changes the format but keeps the cue. The other keeps the cue but makes it wrong, with the model's words labelled as the user's.
- **A check that the cue is really gone.** A model may recognise its own writing by its style or by where it sits in the exchange. T3's probe, with its controls for order and style, is the start of that check.
- **The split test's own rules, carried over.** Thresholds fixed in advance, paired intervals, matching on confidence, and the rule that "no excess loss" counts against the prediction. The way to lose is stated before anything runs, and it goes through the project's review.
- **Two known limits to settle first.**
  - Taking the cue out of the input tests whether the model *depends on the cue*. That is not the same as removing its own use of the difference, which the theory names, and the design would have to say which one it can claim.
  - On the bench model, only one kind of prompt-rule problem is answered reliably (phase 1 findings, step 1). So the task cell needs easier kinds, or a larger model, which would mean RunPod under John's standing rule.
