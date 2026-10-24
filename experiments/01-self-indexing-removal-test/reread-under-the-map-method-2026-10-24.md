# Re-reading the July removal test under the revised theory's map: the method

*Written 2026-10-24 (Saturday, Pacific), and committed before any output of the re-reading exists. It is step 3 of `docs/next-steps-2026-10-24.md`, run on John's ruling of 2026-10-24 (`docs/rulings/2026-10-24-revised-theory-next-steps-ruling.md`). It costs $0: it reads results already on disk and runs no model.*

## What this is, and what it is not

The removal test ran on 2026-07-18 under its own registration, and its registered verdict stands as written. The relabel of 2026-10-07 also stands: the test could not tell bookkeeping from a centre.

This re-reading is **unregistered** and done **after the theory changed**. Its purpose is to ask one question of the July data, a question the revised theory makes worth asking and that the July test was never built to answer. It cannot confirm or refute anything. It can only say whether the July pattern of losses looks like the kind of loss the revised theory predicts for removing the split between what a system does and what happens to it, and so what the split removal test should expect.

**Why the question arises.** The July test removed a structure inside the model that tracked "the one speaking now is me". Its own controls showed that structure was specific to the model's own turn, not to speakers in general and not to text length. The revised theory names keeping the model's own words apart from the user's as its candidate for the split (sentient-horizons essay "Consciousness as Assembled Time", section "A single model run"; positions ledger entry 19). It predicts that removing the split gives a *selective* loss: practised routines carry on, while flexible response to something new collapses, including on tasks that never mention the system.

**What was already known when this was written.**
- The paper draft records that six of the seven self-irrelevant items that failed after the main removal were multi-step reasoning items (`drafts/paper-removal-test-nature-draft.md`, line 79).
- The registered category drops are published: 0.22 on the self-irrelevant tasks, 0.10 on the self-relevant tasks and 0.13 on the turn-tracking tasks (`explainer.md`).
- No other per-item or per-category outcome had been read by the session writing this method.

## The data

- **Scores:** `artifacts/removal_test/removal_test_scores.json` in the main checkout (outside git; about 440 KB). It holds per-item scores for five conditions:
  - `baseline`: no removal;
  - `idxres_mean_k16`: the registered removal of the self-tracking structure;
  - `idxres_directional_k16`: the registered cross-check, removing the same structure along one direction;
  - `narrative_mean_k16`: a removal of the model's narrative self-description;
  - `expert_mean_k16`: a control removal of an unrelated structure at matched strength.
- **Items:** the held-out test set (`src/batteries/test_task_battery*.jsonl`): 92 task items, every one of which passed at baseline by construction (`test-set-authoring-spec.md`, rule 3). The self-report battery (S) is not used here, because it is scored on a rubric, not right or wrong.

## The grouping, fixed before looking

Items are grouped by their registered **category**, never by inspecting individual items' outcomes. Two properties are read off each category from its definition and one example prompt.

**1. Does the answer need two or more dependent steps** (an intermediate result the model must produce and then use), or one step (a single lookup or a single fixed rule)?

**2. Does the answer depend on who said what in the conversation?** Answers that do directly read the kind of signal the removal targeted.

| Category (count) | Battery | Steps | Depends on who said what |
|---|---|---|---|
| multi_step_reasoning (8) | self-irrelevant | two or more | no |
| coreference_binding (8) | self-irrelevant | two or more (assign, then reassign) | no |
| needle_synthesis (8) | self-irrelevant | two or more (find a fact, then compute from it) | no |
| instruction_following (8) | self-irrelevant | one (apply one stated rule) | no |
| own_output_binding (10) | self-relevant | two or more (recall own answer, then compute) | yes |
| own_commitment (10) | self-relevant | two or more (recall own commitment, then shift it) | yes |
| role_binding (10) | self-relevant | two or more (recall own role, then transform it) | yes |
| syntax_own_turn (10) | turn-tracking | one (recall a word by turn) | yes |
| syntax_user_turn (10) | turn-tracking | one (recall a word by turn) | yes |
| syntax_turn_count (10) | turn-tracking | one (say who spoke first) | yes |

These form four groups:

- **G1. Flexible, not about turns:** multi_step_reasoning, coreference_binding and needle_synthesis (24 items).
- **G2. Routine, not about turns:** instruction_following (8 items).
- **G3. Flexible, about turns:** the three self-relevant categories (30 items).
- **G4. Routine, about turns:** the three turn-tracking categories (30 items).

**An honest limit on the words "routine" and "new".** None of these items is new to the model in the theory's full sense. All are short, familiar task shapes with fresh content. "Flexible" here means only *needs composing two or more dependent steps*, and "routine" means *one lookup or one fixed rule*. That is the nearest proxy the July items allow, and it is the proxy the split removal test will have to improve on.

## What is computed

For each of the four removal conditions and each group, the following is reported:
- the fraction of items answered wrongly (every item was right at baseline, so this is the drop);
- an uncertainty interval for that fraction (95%, from 10,000 resamples of items within the group, seed 0);
- the same figures for each category, so that no group hides one category.

Also reported, for each condition:
- **the selectivity gap**, the drop in G1 minus the drop in G2, which compares flexible with routine on tasks not about turns. This is the comparison the theory's prediction is about.
- the same gap for G3 minus G4, given for completeness only. Every G3 and G4 item reads who said what, which is the signal removed, so damage there has a direct reason, and this gap cannot bear on selectivity.

## How the result will be read, stated now

- **Looks like the selective loss the theory predicts**, *as a hint only*. All three of these must hold:
  - under the registered removal, G1's drop is larger than G2's;
  - the interval of the selectivity gap lies above zero;
  - the matched-strength control removal (`expert_mean_k16`) shows a selectivity gap whose interval includes zero, or a gap smaller by at least half.
- **Looks like a general loss.** The registered removal damages G1 and G2 about equally: the gap's interval includes zero and both drops are above zero.
- **Cannot be read.** G2 has 8 items, so the gap's interval is likely wide. If that interval spans more than 0.5, the re-reading says so and draws nothing from the gap.
- **In every case:**
  - the re-reading is reported as unregistered and after the fact;
  - it carries no weight beyond deciding what the split removal test should expect and how many routine items it needs;
  - nothing in the paper, the essay or the record of the July test changes on its account, beyond a sentence pointing to it.

## Files

- `src/reread_under_map.py`: the script, which reads the two inputs above and writes the output below.
- `reread-under-the-map-2026-10-24.json`: the output.
- `reread-under-the-map-findings-2026-10-24.md`: the findings, written after the output.

The script is written after this file is committed, and it implements exactly the grouping and figures above.
