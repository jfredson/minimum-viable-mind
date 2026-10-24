# The split removal test: the measurement rehearsal, method

*Written 2026-10-24 (Saturday, Pacific) and committed before the rehearsal runs. Step 3 of section 8 of the design (`docs/split-removal-test-design-2026-10-24.md`, version 0.6). The rehearsal uses pilot items only (half A, seed 1), runs on this Mac on `google/gemma-2-2b-it`, and costs $0. Nothing here is a registration. Every number below that the design does not already fix is a choice made by this session (authorship: agent), and it is listed in section 6 so the Gate A pass can check it.*

## 1. Why the rehearsal comes in two phases

The design says that if either removal method fails the removal check, the design goes back to John before any registration (section 8, step 3). Most of the rehearsal's cost is in scoring tasks under many removals, and that work is wasted if the removal check fails. So:

- **Phase 1** runs everything that the removal check needs, plus the measurements that do not depend on it: the baseline checks on the pilot items, locating the target, both removal methods, the removal check, the normal-range bound, and the damage the split removal does.
- **Phase 2** runs only if **both** methods pass the removal check. It covers the damage-matched comparisons, the other-distinction removal, T3 with its two controls, scoring the matched routine and prompt-rule items under every condition, and the committed sample-size simulation.

If either method fails in phase 1, the rehearsal stops there and the result goes to John through the master session.

## 2. Phase 1, step by step

**Step 1. Baseline checks** (battery specification, section 3). Every routine and prompt-rule item is run greedily once and sampled 10 times at temperature 0.7, with at most 96 new words (tokens), so that a short worked answer is not cut off before its "Answer:" line. An item is kept if greedy is right and at least 9 of the 10 samples are right. Each prompt-rule item is also run greedily with its rule removed. A prompt-rule kind is dropped whole if its accuracy without the rule is above its chance rate plus 0.10. The chance rates are:

| Kind | Chance rate | Why |
|---|---|---|
| `p_operator` | 0.0 | The answer is a number; the specification's "plain sum" rule is reported beside it as the share of no-rule replies that give the plain sum |
| `p_cipher` | 0.0 | The answer is an invented word that cannot be guessed |
| `p_two_rules` | 1 over the list length | One named position of a list |
| `p_sequence` | 1 over the ring length | The next token on a ring |

**Scoring.** Every routine, prompt-rule and which-did-you-say reply is scored only on the text after its last "Answer:", and a reply with no "Answer:" counts as wrong. Experiment 01's scorer, which the battery specification names, also accepts the answer anywhere in the reply. In the list and ring items the reply usually repeats the list, so that fallback would count most wrong answers as right.

Then the two cells are matched on pass rate (9 or 10 of 10), with seed 1. The rehearsal reports how many matched items each cell keeps. Under 40 makes the cell unusable on this model (specification, section 8).

**Step 2. Locating the target.** The stimuli follow experiment 01's version 2 context set (`experiments/01-self-indexing-removal-test/src/gen_context_stimuli.py`), with new first-person sentences:
- A fixed pool of 60 sentences is written in `src/locate_stimuli.py`, with no word that names who is speaking. Half A is the first 30 and half B the last 30.
- From half A, 18 sentences are used for fitting and 12 are held out. The held-out sentences are never used to fit any removal.
- Each sentence is placed four ways, one for each of four neutral user openings. In every case it is either the model's own turn or the user's turn. The two cases are balanced for length the way experiment 01's version 2 was. That gives 144 items to fit and 96 to hold out.
- The same sentences also appear inside a third-party transcript (the generic speaker condition) and, for phase 2, inside or outside quotation marks in one user turn (the other distinction).

The removal is fitted the way experiment 01's primary condition was fitted (`experiments/01-self-indexing-removal-test/src/run_removal_test.py`):
- a rank-16 basis per layer, found by logistic fitting with deflation, at layers 8, 11, 14, 18 and 22;
- the basis is then made independent of the third-party speaker direction at each layer, which removes generic tracking of who is speaking.

The readout is the last token of the identical sentence. A layer-0 check confirms that sentence's last token alone cannot tell the two cases apart.

**Step 3. The two removal methods.** (a) Mean-ablation: each basis coordinate is pinned to its average over the fitting items. (b) Projection: each coordinate is set to zero. Both apply at every position and on every generated word, through `src/mvm/ablate.py`.

**Step 4. The removal check** (design, section 2), on each method separately:
- **Probe test.** The held-out items are run under the removal. At every layer from 8 (the first removal layer) to 25 (the last), a linear probe and a nonlinear probe each try to tell the model's own sentence from the user's. Each probe gets 5-fold cross-validation, split by sentence so that no sentence is in both training and scoring.
  - The linear probe is logistic regression on standardised activity.
  - The nonlinear probe has one hidden layer of 64 units.
  - The test passes only if **both probes are at most 0.55 at every layer**.
  - The same probes are also run at baseline, and the probes' accuracy on shuffled labels is reported beside every number. The threshold applies to the raw accuracy, as the design says.
- **Task test.** The 60 which-did-you-say items are run greedily (at most 32 new words), at baseline and under the removal. The test passes if accuracy under the removal is at most half of baseline. The scorer reads only the text after "Answer:", and counts an answer right only if it names the expected word and not the other one. Experiment 01's scorer falls back to the whole reply, which in these items always contains both words.

**Step 5. The normal-range bound** (design, section 2). There are 20 random removals of the split's size: rank-16 orthonormal bases at the same five layers, seeds 0 to 19.
- Each random removal is run with mean-ablation and with projection.
- For mean-ablation, a random basis's average is taken over the same fitting items.
- The rise in neutral-text surprise (mean negative log-likelihood per token on the 200 neutral passages) is measured for each one.
- The bound for each method is the 95th percentile of its 20 rises, computed with numpy's default (linear) percentile.
- It is written into the results file before any task is scored under a removal.

**Step 6. The split removal's damage and its room under the bound.** Two figures are measured for each method on the 200 neutral passages:
- the rise in surprise, against the bound;
- the damage: the mean, over every word position, of the divergence (KL, in nats) of the removed model's next-word predictions from the unremoved model's.

The room left under the bound is reported. If the split removal is itself above the bound, that is a normal-range failure for that method, and it is reported as one.

## 3. Phase 2, in outline

Phase 2 is fixed in detail only if phase 1 passes. These are its parts, so that a pass does not leave room to choose after seeing results:
- **Random comparisons matched on damage.** Random bases at the same layers, with the rank raised in steps (16, 32, 64, 128, 256) until a draw's damage lands within 20% of the split's. The 20 draws are made at the first rank where the median draw does.
- **The other distinction.** Located on the quotation-mark stimuli at the same rank, then matched the same way.
- **T3.** With its order and style controls.
- **Scoring.** The matched routine and prompt-rule items are scored under every condition.
- **The simulation.** It is written and committed before it is run.

## 4. What phase 1 can say

Phase 1 decides one thing: whether this design can be run on this model as written. If the removal check fails, the finding is that this target, removed this way, does not erase the information it was meant to erase on this model. That says nothing yet about the theory's prediction. It is a statement about the instrument, and it goes to John as one.

## 5. Outputs

- `rehearsal/phase1-2026-10-24.json` holds every number above.
- `rehearsal/phase1-findings-2026-10-24.md` gives the plain account.
- Per-item outputs go under `artifacts/` (not committed; gitignored).

## 6. Choices made here that the design did not fix (authorship: agent)

1. Experiment 01's layers (8, 11, 14, 18, 22), rank (16), fitting method and generic-speaker residual are kept as they were.
2. The removal check reads layers 8 to 25, which are the layers at and after the first removal.
3. Probe settings: 5-fold cross-validation split by sentence; 64 hidden units in the nonlinear probe.
4. The chance rates per prompt-rule kind (table above).
5. The strict scorer, for every cell, in place of experiment 01's.
6. A maximum of 96 new words per reply on the baseline checks, and 32 on the which-did-you-say items.
7. The rank steps for damage matching in phase 2.
8. The two phases, and stopping after phase 1 on a failed removal check.
9. The order of running: steps 2, 3, 5 and 6 first, then step 4, then step 1. The normal-range bound is therefore written to disk before any task, the which-did-you-say items included, is scored under a removal.
