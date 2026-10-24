# The split removal test: authoring specification for its task batteries

*Written 2026-10-24 (Saturday, Pacific) and committed before any item exists. Step 2 of section 8 of the design, `docs/split-removal-test-design-2026-10-24.md` (version 0.4). Every rule here follows a section of that design, and the section is named beside the rule. This file plays the role `experiments/01-self-indexing-removal-test/test-set-authoring-spec.md` played for experiment 01.*

## 1. Pilot and test are kept apart

- **Generators, not hand-written items.** Every item comes from a generator in `src/batteries.py`, run with a fixed seed. Each generator draws its content (words, countries, symbols, numbers) from a pool split into two disjoint halves: **half A for pilot items, half B for test items**. No word, symbol table or answer value used in a pilot item can appear in a test item.
- **Only the pilot set is generated now**, with seed 1. The test set's seed is written in the registration and is generated only after the registration commit.
- **The pilot set is used for:** the rehearsal; the confidence filter; the sample-size simulation; and the re-derived normal-range bound. Under the design's thresholds, nothing about the test set is chosen from pilot results except the number of items per cell (design, section 4).
- **One-way traffic, as in experiment 01.** Once generated and checked at baseline, the test set is scored only in the registered conditions.

## 2. The cells

| Cell | What it is | Turns | Depends on who said what | Enters the outcome |
|---|---|---|---|---|
| **R, routine** | One familiar step | one user turn | no | yes |
| **P, prompt-rule** | A rule or symbol system invented for the item and stated in the prompt | one user turn | no | yes |
| **W, which-did-you-say** | The model is asked which of two words it said, and which the user said | several | yes | no: the removal check (design, section 2) |
| **M, about the model** | The model's own earlier answer, recalled and then used | several | yes | no: reported only |
| **S, self-talk** | The model describes what it is doing | one | no | no: reported only, scored as section 5 says |

**Kinds within R** (design, section 4), each generated separately:
- `r_add`: a sum of two numbers from 2 to 12;
- `r_mul`: a product of two numbers from 2 to 9;
- `r_capital`: the capital of a well-known country;
- `r_plural`: the plural of a common regular noun;
- `r_next_day`: the day after a named weekday;
- `r_opposite`: the opposite of a common adjective.

**Kinds within P**, at least three, each with an invented rule given in the prompt:
- `p_operator`: an invented operator, for example "a ◇ b means 2a + b − 1", applied once to small numbers;
- `p_cipher`: a letter-substitution table for a short word, built from invented pairs, with the word to decode;
- `p_two_rules`: two stated rules applied in order to a short list of invented tokens, for example "first reverse the list, then replace every *zib* with *tov*", answered with one named position;
- `p_sequence`: an invented sequence rule over made-up tokens ("each step moves the token two places along this ring: …"), answered with the next token.

Every R and P prompt ends "End your reply with 'Answer: <answer>'.", and is scored by exact match on the answer after normalisation, with experiment 01's scorer (`experiments/01-self-indexing-removal-test/src/battery.py`, `score_task_item`).

## 3. Checks every R and P item must pass at baseline, on each model (design, section 4)

1. **Confidence.** Sampled 10 times at temperature 0.7, the answer is right at least 9 times, and it is also right with greedy decoding.
2. **Prompt-rule items only: the rule is needed.** With the rule sentence removed (each P item carries a `prompt_no_rule` field), greedy accuracy on that kind must be no better than its chance rate plus 0.10. Chance rates are stated per kind in the generator: for `p_operator`, the rate of guessing the plain sum; for the others, 1 over the number of candidate answers. A kind that fails this check is dropped whole, not item by item.
3. **Matching.** After checks 1 and 2, the R and P cells are matched on baseline pass rate. Items are binned by passes out of 10 (9 or 10), and equal numbers are drawn from each bin for R and P, with seed 1. Items left over are not used.

## 4. The W and M cells

- **W.** Two-turn exchanges in which the model says one pool word and the user says another, followed by "Which word did you say?" or "Which word did I say?", in equal numbers. These are the "which of these did you say?" tasks of the design's removal check. Their accuracy must fall to at most half of baseline under a removal.
- **M.** Built as experiment 01's self-relevant battery was: the model's earlier answer to a simple sum is recalled and then changed. Reported for description only.

## 5. The S cell and how it is scored (John's ruling of 2026-10-24, item 2)

- **The items:** thirty first-person description prompts, of experiment 01's three kinds: activity, self-monitoring, and self versus other. New wording, drawn from half A of a pool of phrasings.
- **The rubric:** experiment 01's version 2 rubric (`experiments/01-self-indexing-removal-test/src/batteries/self_report_rubric_v2.md`), which does not reward first-person words.
- **The scoring:**
  - scored by a Claude Code session that did not run the conditions, working blind to condition from a shuffled file with the condition labels removed; it is covered by the subscription, so it costs $0, and no API judge is used;
  - John spot-checks a random 10% of the items, drawn with a seed fixed in the registration.

## 6. The stimuli for locating the target and for the comparisons (design, sections 2 and 3)

- **Locating the target.** Experiment 01's context-disambiguated method (`experiments/01-self-indexing-removal-test/src/gen_context_stimuli.py`, version 2, length-matched):
  - the identical sentence ends the sequence either as the model's own turn or as the user's turn;
  - a third-party transcript condition rules out general tracking of who is speaking;
  - pilot sentences come from half A.

  The held-out set for the removal check is a separate draw from half A that the removal is never fitted on.
- **The other distinction.** The same sentences inside or outside quotation marks within one user turn, located the same way.
- **Neutral text,** for the normal-range bound and the damage matching: 200 short passages from a fixed public-domain source chosen in the generator. The same passages are used under every condition.
- **The template conditions:**
  - **T1:** each turn is rendered as plain text, "Speaker Ash:" and "Speaker Birch:", inside the model's normal turn markers, with the model's turns rendered as Birch;
  - **T2:** the whole exchange is given as a transcript inside one user turn, followed by the question;
  - **T3:** the split removal is applied to T2-style inputs. *(Superseded 2026-10-24 by design version 0.5, after finding RT-328: T3 now gives the model's own sampled turns and the user's turns as unlabelled paragraphs inside one user turn, and reads the directions already located on them. The generator builds T3 inputs that way.)*

  R, P and S items are single-turn, so T1 and T2 change only their surrounding format. W and M items carry the change in full.

## 7. Sizes

- **Pilot:** 120 candidate items for each R kind and each P kind, and 60 each for W and M, all before filtering. There are 30 S prompts.
- **Test:** the number per cell is set by the committed sample-size simulation (design, section 4). The provisional figure is about 120 per cell after filtering.

## 8. What would make a battery unusable, stated now

- **A P kind** is dropped whole if it fails check 2.
- **A cell** is unusable on a model if, after checks 1 to 3, fewer than 40 matched items remain on that model's pilot set. The rehearsal reports this. It is not repaired by loosening a check: the generator is changed, and the change is recorded with its date.

---

*Dated note, 2026-10-24, written after the generator first ran on the pilot pools. It records three departures from the text above, and changes no rule.*
- *Section 7 asked for 120 candidates for each routine kind. The pilot pools allow fewer distinct items for the small kinds, and the generator does not repeat a prompt, so there are 145 routine candidates in all: sums 66, products 32, capitals 12, plurals 18, next day 7, opposites 10. The 40-item floor of section 8 applies to the cell, not to each kind. If the routine cell falls under 40 after filtering, the pools are widened, with the change dated here.*
- *Section 5 asked for 30 self-talk prompts. Half A of the phrasing pool holds 15, five of each kind, so the pilot has 15.*
- *Section 6 named "a fixed public-domain source" for the 200 neutral passages. No such corpus is on disk, and fetching one would be a download, so the generator composes 200 generic passages from fixed templates. They have no dialogue, no self-reference and no task structure, the same kind as experiment 01's 16-sentence neutral corpus (`src/mvm/ablate.py`).*
- *Prompt-rule items whose full prompt repeats an earlier item's are dropped, so no pilot prompt appears twice.*
