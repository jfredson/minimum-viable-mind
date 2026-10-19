**Verdict: PASS WITH CONDITIONS.** The explanation holds and every figure checks out; four changes are owed before merge, all in how the findings and the pull request's description report what the planned tests said.

# Check of pull request 180: why arm M's separable half reads zero route use at 10 million parameters (2026-10-18)

*Filed under the pairing rule of `docs/outside-review-protocol.md` (the section
"The pairing rule: whatever one session writes, a different session checks") by
a Claude Code session that did not write the pull request and has not read the
writing session's chat. Worked in its own worktree
(`.claude/worktrees/check-180`, branch `check-arm-m-separable-zero`, cut from
the pull request's branch `arm-m-separable-zero-explanation` at `8fa464d`).
Filed under `docs/reviews/` beside the pull request's own documents, which also
sit in `docs/` and not under an experiment folder. $0: forward passes of saved
checkpoints on the laptop's processor. Nothing trained, rented or called by API.
Nothing under check was edited. Written under the workspace plain-language rule.*

## The changes owed before merge

1. **Report D3 the way its planned reading says, and say the same in the
   summaries.** The method (`cb3b9ee`) said, for D3 (forcing the row choice onto
   each agent in turn): "H1 rejected if in arm M forcing a wrong row gives that
   agent's answer, as in arm T." That is exactly what came out (3,570 of 3,570).
   The findings' F3 calls this a rejection of "one form of H1". It also says the
   method's words "or the own row dominates" already covered the mechanism
   found later. They did not. D3 forces a single row (`sel_named` is a one-hot
   choice in `_separable_logits`), so a large own row could never have produced
   the own answer in D3. The form D3 rejects is the one the method itself gave:
   "the answer comes out right whichever row the slot selects." So:
   - In F3, drop "one form of", and drop the claim that the method's wording
     anticipated the large-own-row account.
   - In "The answer in plain words", in "Which hypothesis the outputs support",
     and in the pull request's **Hypotheses** line, state H1's result in three
     parts:
     - its first claim (the trunk's "this turn is yours" signal, not the
       built-in answer, carries the separable answers) is **supported by D5**,
       which was planned;
     - the mechanism the method gave for it is **rejected by D3**, which was
       planned;
     - the mechanism that replaces it (a flat row choice over a large own row)
       comes from **D7, added after the planned diagnostics had printed**.
2. **Say that D6 matched neither planned pattern for H4.** The method's
   "supported" pattern needed the row-choice weights at or below 0.335 of their
   start. Its "rejected" pattern needed arm M's weights as large as arm T's
   *and* its row choice as sharp. The weights grew, but the row choice is flat
   (weight on the top row 0.2616), so neither pattern fired. "Rejected as
   stated" is a fair reading, because the weights H4 named grew. But it is the
   writing session's reading, not the planned one, and the findings should say
   so in one sentence.
3. **Label the added diagnostics' results where they appear unlabelled, and
   correct "nothing in the reading below rests on them alone".** Two results
   come only from added diagnostics:
   - "an even mix of the four rows gives the own answer" (D7);
   - "the marker-word embeddings shrank to 3.4 per cent of their start" (D8).
   These appear with no word saying they were added in four places: the
   findings' sections "The answer in plain words", "What the outputs do not
   settle" (item 1) and "For the write-up, in one sentence", and the pull
   request's "What was found, in plain words". The write-up sentence is the one
   most likely to travel. The H1 verdict itself rests on D5, as the pull
   request says. But the account of *why* the row choice is flat rests on D8
   alone, and the claim that an even mix is enough rests on D7 alone, so the
   sentence "nothing in the reading below rests on them alone" is not true as
   written. (E5 below now backs D8's comparison with decay. The findings may
   cite it if they wish.)
4. **Three small wording fixes.**
   - F2 says arm M's slot "moves a hundred times less than arm T's". The output
     gives 20.4098 ÷ 0.2218, which is 92, so "about ninety times".
   - F6 cites F3 for "about 3.8 times". F3 prints 3.7 (11.642 ÷ 3.105, a ratio
     of mean sizes); 3.8 is D7's mean of per-action ratios (3.775). Cite D7, or
     use one figure in both places.
   - The plain-words section says that for arm T, taking the signal out of the
     trunk "changes nothing". It changes 0.986 to 0.978. Say "almost nothing",
     as F5 does.

None of these changes the explanation or any figure.

## What this session opened, and what it did not

**Opened:**
- `~/Code/CLAUDE.md` and this repository's `CLAUDE.md`.
- `docs/outside-review-protocol.md`: the pairing rule and the gate sections.
- Pull request 180's title, description and commit list (`gh pr view 180`).
  The description is saved here as `…-scripts/pr180_body_2026-10-18.md`.
- The method file and the findings file, in full.
- Every script and output file in `docs/2026-10-18-arm-m-separable-zero-scripts/`.
- In the frozen code at `6c47c56`:
  - `models.py`, lines 127 to 365: `_own_vec`, `_separable_logits`, both arm
    classes' `_embed` and `forward`, and `entangled_route`;
  - `procedure.swap_answer`;
  - `train_successor.run`, lines 112 to 135: the seed, `build`, AdamW and the
    one-cycle schedule;
  - `grammar.TrainingStream`.
- The toy retrain script `experiments/08-successor-degree/tests/retrain_toy_fixed.py`
  and the rehearsal's `training.train_arm` (decay 0.01, one-cycle, first tenth
  warming up).
- The arm M rerun's training log header (the recipe line).
- `out-reruns-10m/row_M_seed0.json`: the gate block and route-use figures.
- `out-sharpness-fix/retrained_inuse.txt`.
- From `docs/2026-10-09-reruns-10m-run-record.md`: the measurement and version
  lines, the arm M row, and item 3.
- From the 2026-10-17 ruling that experiment C stays stopped
  (`docs/rulings/2026-10-17-experiment-c-stays-stopped-ruling.md`): the
  precondition lines 63 to 70.
- The creation and change times of the writer's files in its worktree
  (`.claude/worktrees/arm-m-zero`), read with `stat` only.
- One sibling note in this session family's shared notes folder: the check of
  pull request 175, read for the filing convention only.

**Not opened:**
- The writing session's chat.
- Pull request 112's `decay_alone.py`. D6 reruns its arithmetic, and E5 below
  measures the same factor on the model directly.
- The registered experiment C text, beyond what the method quotes.
- Any arm C model.

## The checks run

All scripts are in `docs/reviews/2026-10-18-arm-m-separable-zero-check-claude-code-scripts/`,
each with its full printed output beside it as `<name>_output.txt`. To re-run
everything (about eight minutes), from the worktree root:

    sh docs/reviews/2026-10-18-arm-m-separable-zero-check-claude-code-scripts/run_all.sh

They import the pull request's `common.py` (read-only) and the frozen code, and
change no file in either. Library versions as in the pull request: torch 2.12.1,
scikit-learn 1.9.0, numpy 2.5.0, Python 3.12.13, processor.

### Item 1: the method came before any output, and its predictions are read as written

**The order of commits and files. MEASURED.** `git reflog` on the pull
request's branch gives these times on 2026-10-18 (Pacific):
- branch created 16:53:27;
- method commit `cb3b9ee` at 16:58:18;
- findings commit `8fa464d` at 17:06:19.

The creation times of the writer's files in its worktree
(`rerun_compare_output.txt`, last block):
- the method file: 16:58:14;
- the first script (`common.py`, `d0_reproduce.py`): 16:59:06;
- the first output: created 16:59:06, finished 16:59:29;
- the last D0 to D6 output finished: 17:02:42;
- `d7_flat_choice.py`: 17:02:57;
- `d8_answer_vector.py`: 17:03:30;
- `d9_stirred_in_items.py`: 17:04:41;
- the findings: 17:06:11.

Every output file in that folder was created after the method was committed.
This cannot rule out an earlier run whose files were written somewhere else
and deleted (ARGUED). Nothing points to one: the ten scripts take 226 seconds
in all on this laptop (the re-run times below), which fits the 16:59 to 17:05
window.

**Each planned prediction against its outcome. MEASURED for the figures,
ARGUED for the reading.**

| Diagnostic | What the method said | What came out | Does the findings' reading follow the planned rule? |
|---|---|---|---|
| D0 | Arm M separable 0.000 (1,190 of 1,190 still right), stirred-in 0.024; arm T 0.986; toy arm M 1.000 on each seed | Exactly that | Yes |
| D1 (H3) | Rejected if (a) and (b) are 0 and (c) is near 0.4 | 0, 0, 0.3967 | Yes |
| D2 (H2) | Rejected if the slot moves in both arms and, where the row choice is sharp, it follows the swap; a flat row choice "is read under H4" | Slot moves on 1,190 of 1,190 (arm M) and 3,000 of 3,000 (arm T); arm M's row choice is flat | Yes |
| D3 (H1) | "H1 rejected if in arm M forcing a wrong row gives that agent's answer, as in arm T" | 3,570 of 3,570 give that agent's answer | **Partly.** F3 reports the rejection but calls it "one form", and leans on a parenthetical that D3 could not have tested. Change 1 |
| D4 | Context only, read beside D3 | Separable named-other answers 1,178 of 1,178 | Yes |
| D5 (H1) | Supported if arm M's separable accuracy falls well below 1.0 while arm T's stays near its unlesioned figure | 0.275 against 0.978 | Yes |
| D6 (H4) | Supported if `read_own` and `own_key` end at or below about 0.335 and arm M's row choice is flat; rejected if arm M's weights are as large as arm T's and its row choice as sharp | Weights grew (1.92, 1.37); row choice flat | Neither pattern fired. Change 2 |

### Item 2: D7, D8 and D9 labelled as added, and the H1 verdict resting on D5

**MEASURED** (`e3_figures_and_labels_output.txt`, second half). Where they are
used, the three added diagnostics are labelled:
- each script's docstring says "ADDED AFTER THE FIRST OUTPUTS";
- the findings' section on where the commands are says so;
- F6's and F8's headings say so;
- F7's paragraph introducing D8 says so.

The check splits the findings and the description into sections and looks for
the added diagnostics' key phrases (for example "even mix", "flat mixture",
"3.775", "3.4 per cent", "0.503" and "marker-word embeddings"). It finds them
in sections that never say they were added: the findings' "The answer in plain
words", "What the outputs do not settle" and "For the write-up, in one
sentence", and the description's "What was found, in plain words". Change 3.

**ARGUED.** The verdict on H1's first claim rests on D5, which was planned, and
D5 came out the way the method said H1 would. That part of the description's
item 2 holds. D7 does more than "join the pieces": it is the only measurement
showing that an even mix of the rows gives the own answer.

### Item 3: every script re-run, outputs compared, frozen folder unchanged

**MEASURED** (`rerun_compare_output.txt`):

```
$ git diff 6c47c56 -- experiments/08-successor-degree/src/ | wc -c
       0
d0_reproduce: differs; 23.93 s
d1_bookkeeping: identical; 5.74 s
d2_swap_reach: identical; 19.31 s
d3_forced_row: identical; 46.23 s
d4_named_by_route: identical; 11.35 s
d5_trunk_lesion: identical; 47.71 s
d6_weights: identical; 13.44 s
d7_flat_choice: identical; 40.38 s
d8_answer_vector: identical; 1.90 s
d9_stirred_in_items: identical; 15.70 s
$ diff d0_reproduce_output.txt (committed) against the re-run
18c18
<   (1.9 s)
---
>   (1.8 s)
23c23
<   (1.9 s)
---
>   (1.8 s)
```

D0's only difference is two printed wall-clock times. Every figure in every
output is reproduced byte for byte. The pull request also touches no file
outside its own three paths (`git diff --name-only 53bb84a 8fa464d`, filtered
to paths not starting `docs/2026-10-18-arm-m-separable-zero`: 0 files). The
checkpoint checksums are checked by `common.load` on every run, against the
values the run record gives. The run record's figures match too:
`row_M_seed0.json` gives named-other 1,733, separable 1,190 right with 1,190
still right, and stirred-in 1,387 with 1,354.

### Item 4: the in-memory lesion in D5, D7 and D9

**ARGUED, from the code.** The frozen models read the acting channel in exactly
two places:
- `_own_vec`, the built-in answer, which reads `b["acting"]` at the assignment
  turns;
- `_embed`, which adds `act_vec` to the trunk's input wherever `b["acting"]`
  is 1.

The scripts hand the model a batch with `acting` set to zero and override
`_own_vec` on the instance with a function that calls the original method on
the real chunk. So the trunk's input loses the acting channel, and the
built-in answer reads the real one. `del m._own_vec` in a `finally` block
brings the class method back. One thing a reader should know: in arm M, the
built-in answer also enters the trunk through every block's scale-and-shift
and through the value-word binding, and under the lesion that answer is the
real one. So the lesion removes the acting channel from the trunk, not every
trace of ownership. That the own row still falls to the others' size under the
lesion (D7: 1.017) shows those two routes do not make it large. This
strengthens the reading rather than weakening it.

**MEASURED** (`e2_lesion_audit.py`). This runs the three scripts unchanged and
watches every forward pass. In this process only, it wraps `_own_vec` and both
`_embed` methods so that each forward pass records:
- how many acting flags the built-in answer saw;
- how many the trunk's input saw;
- whether the override was in place.

The wrappers return the original results unchanged. Output:

```
d5_trunk_lesion: forward passes 120: {'normal': 48, 'trunk-only lesion': 48, 'acting zeroed everywhere': 24}
  passes that break the rule above: 0; models still carrying the override after the run: 0 of 4
  printed output identical to the committed d5_trunk_lesion_output.txt: True
d7_flat_choice: forward passes 72: {'normal': 48, 'trunk-only lesion': 24, 'acting zeroed everywhere': 0}
  passes that break the rule above: 0; models still carrying the override after the run: 0 of 4
  printed output identical to the committed d7_flat_choice_output.txt: True
d9_stirred_in_items: forward passes 36: {'normal': 24, 'trunk-only lesion': 12, 'acting zeroed everywhere': 0}
  passes that break the rule above: 0; models still carrying the override after the run: 0 of 2
  printed output identical to the committed d9_stirred_in_items_output.txt: True
```

"The rule above" is checked on every pass:
- in every pass where the trunk saw no acting flags but the built-in answer
  did, the override was in place and the built-in answer read all 24 flags per
  episode;
- in every other pass, no override was in place.

The pass counts are what the scripts' loops should make (D5: 4 models × 6
chunks × 5 passes = 120). So the lesion does what the findings say, and it is
put back after each chunk.

### Item 5: the rebuilt starting weights in D6 and D8

The findings argue (ARGUED in F7) that the ratios stand even if the rebuilt
start is not the trainer's draw, because starting sizes vary little between
draws. Two checks:

**E4, the spread over twenty draws. MEASURED** (`e4_start_spread_output.txt`).
The start was rebuilt with seeds 0 to 19:
- no starting size moves by more than 20 per cent from seed 0 (`act_vec`
  moves by up to 16 per cent; the differing part of the answer vector by up to
  20 per cent);
- no end-over-start ratio crosses 0.335 or 1;
- arm M's marker-word embeddings come out between 0.0325 and 0.0338 of their
  start;
- arm T's come out between 0.369 and 0.383.

The argument holds.

**E5, decay alone measured on the model itself. MEASURED**
(`e5_unused_markers_output.txt`). The vocabulary has twenty marker words, and
only m0 to m11 appear in the episodes. In 200 training batches drawn as the
trainer draws them (seed 0, steps 0 to 199), m0 to m11 each appear about
14,000 to 15,000 times, and m12 to m19 appear 0 times. An embedding row that
never appears gets no gradient, so AdamW changes it by decay alone:

```
M-10M-rerun: end over start, per marker word
  m0-m11:  0.038 0.032 0.033 0.036 0.034 0.038 0.034 0.033 0.035 0.032 0.035 0.025
  m12-m19: 0.335 0.335 0.335 0.335 0.335 0.335 0.335 0.335
  start rebuilt with seed 0: words never used, end over start from 0.33501 to 0.33502
  start rebuilt with seed 1: words never used, end over start from 0.31557 to 0.36202
T-10M-rerun: m0-m11 mean 0.3819; m12-m19 0.335 each; seed 0 0.33501 to 0.33502
```

This settles two things.
- **The decay factor.** Pull request 112's decay-alone factor (0.3350) is what
  the unused rows of these very models show. The words arm M did use ended ten
  times smaller than the words it never saw. So F7's "pushed down by training,
  not merely left to decay" is now measured, not only argued.
- **The starting draw.** The rebuilt seed-0 start is the trainer's exact draw:
  eight rows agree to five decimals, while a seed-1 rebuild scatters them from
  0.316 to 0.362.

The findings' ARGUED paragraph on the starting weights could cite this instead.
That is optional, not a condition.

### Item 6: every MEASURED figure against its output, every ARGUED step

**MEASURED** (`e3_figures_and_labels_output.txt`, first half). 67 figures from
F0 to F8 were looked up as text in the output file each comes from:

```
figures checked: 67; not found in their output file: 0
derived: 11.642 / 3.105 = 3.749 (F3 says 3.7; F6, the plain words and the body say 3.8 or about four)
derived: 0.503 / 14.940 = 0.0337 (findings: 3.4 per cent)
derived: 5.697 / 14.940 = 0.381 (findings: 38 per cent)
derived: 1178 + 555 = 1733 (findings: the run record's 1,733)
derived: 20.4098 / 0.2218 = 92.0 (findings: 'a hundred times less')
```

The description's figures were checked by eye against the same outputs, and
all match: 0.26, 1.9 and 1.4 times, 3.4 and 33.5 per cent, 0.275, 0.978 and
1.000. The toy recipe in F7 matches the code: 2,500 steps, peak 0.003, decay
0.01, one-cycle, first tenth warming up (`retrain_toy_fixed.py` and
`training.train_arm`). The 10-million recipe in D6 matches the rerun's own
recipe line: seed 0, 108,919 steps, learning rate 0.002, decay 0.01, warm-up
0.1, one-cycle. The only mismatches are the wording in change 4.

**The ARGUED steps, one by one:**
- **F2, the swap reaches arm M's head by the same path as arm T's.** Holds.
  `swap_answer` changes only `assign_agent_at`, which only `_own_vec` reads.
  Both arms share `_own_vec` and `_separable_logits` through `_Shared`.
- **F4, a large own row does not spoil naming another agent.** Holds. For
  named-other actions, `sel_named` picks the named row exactly, and D3 shows
  each row holds its own agent's value.
- **F7, "only the part of those vectors that differs from one marker word to
  the next lets the row choice tell agents apart".** Holds exactly for the row
  keys: a part common to all four keys adds the same amount to every score,
  and the row choice ignores that. For the slot's query, its whole size
  matters, not only its differing part. The findings report that size too
  (0.561 against arm T's 20.479), so the account stands.
- **F7, the size argument (below 0.335 means training pushed it down).**
  Holds, and E5 now measures it.
- **F8 and "What the outputs do not settle", item 4.** Labelled as unproven,
  and fairly so.

## This session's own check: move the signal instead of removing it (E1)

**Why.** D5 shows that arm M's separable answers need the trunk's acting
channel. It does not show what that channel tells the model. A trunk deprived
of an input it was trained on might fail for reasons unrelated to ownership.
So E1 moves the acting channel in the trunk onto the next agent round's two
assignment turns, leaving the action turns as they were, while the built-in
answer still reads the real episode. This is the mirror image of the frozen
check, which moves the built-in answer and leaves the trunk alone. It uses the
same in-memory override as D5.

**The prediction came first.** It was committed on its own in
`…-scripts/PREDICTION.md` (commit `7b76310`, 17:24:37) before
`e1_trunk_redirect.py` was run. If H1 holds:
- arm M's separable actions give the next agent's answer on at least 80 per
  cent, and the own answer on at most 10 per cent;
- the next agent's row becomes at least 2.5 times the others;
- arm T and toy arm M keep the own answer on at least 95 per cent of the
  actions they get right unmoved.

H1 would be contradicted if fewer than half of arm M's separable actions gave
the next agent's answer.

**MEASURED** (`e1_trunk_redirect_output.txt`):

```
M-10M-rerun
  separable  actions  1190; right unmoved  1190
             moved: own answer     0 (0.000); next agent's answer  1190 (1.000)
  stirred-in actions  1810; right unmoved  1387
             of those right unmoved: own answer    27 (0.019); next agent's answer  1169 (0.843)
  separable table rows, moved: next agent's row over the others' mean 3.765; own row over the others' mean 0.530
T-10M-rerun
  separable  actions  3000; right unmoved  2959
             of those right unmoved: own answer  2919 (0.986); next agent's answer    20 (0.007)
  separable table rows, moved: next agent's row over the others' mean 0.993; own row over the others' mean 1.009
M-toy-seed0
  separable  actions  1190; right unmoved  1190
             moved: own answer  1190 (1.000); next agent's answer     0 (0.000)
  stirred-in: of those right unmoved, next agent's answer 1152 (0.823)
```

Every prediction holds, and by a wide margin. In arm M at 10 million, moving
the acting channel in the trunk alone moves every separable answer, 1,190 of
1,190, to the next agent's. The large row moves with it (3.765, against 3.775
for the own row unmoved), even though the built-in answer still names the true
agent with weight 0.999. In arm T and toy arm M the answer stays with the
built-in answer. So the trunk's acting channel does not merely prop up arm M's
separable answers: it decides whose answer they are. This is the strongest
direct evidence for H1's first claim. As a by-product, it also confirms F8: in
both arm M models, the stirred-in items follow the trunk too (0.843 and 0.823).

## Outside this pull request

Nothing found.
