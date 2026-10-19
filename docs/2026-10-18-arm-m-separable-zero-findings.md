# Findings: why arm M's separable half reads zero route use at 10 million parameters (2026-10-18)

*Written 2026-10-18 (Pacific) by the Claude Code session that wrote the method
file (`docs/2026-10-18-arm-m-separable-zero-method.md`, committed on its own as
`cb3b9ee` before any diagnostic ran). Under the pairing rule of
`docs/outside-review-protocol.md`, a session that did not write this checks it.
Written under the workspace plain-language rule. $0: forward passes of saved
checkpoints on the laptop's processor; nothing trained, rented or called by API.
No frozen code, registered text, figure, ruling, `STATUS.md` or
`data/project.toml` is edited. Nothing here changes how experiment C ended.*

## The answer in plain words

Arm M's separable half at 10 million parameters does not use its built-in
ownership answer at all. **It gets the answer from the "this turn is yours"
signal in the shared trunk instead** (D5, a planned diagnostic). The trunk
makes the model's own row of the lookup table about 3.8 times larger than the
other agents' rows (a side figure of D3, planned, and D7, added). The part of the model that chooses a row has gone flat: it
puts about one quarter on each agent whatever the built-in answer says (D2,
planned). An even mix of all four rows then comes out as the model's own answer
(D7, a diagnostic added after the planned ones had printed). So swapping the
built-in answer changes nothing, and the check reads 0.000.

The row choice is flat because **the word embeddings of the agents' marker
words, which both the built-in answer and the row keys are made from, shrank to
about 3 per cent of their starting size** (D8, added after the planned
diagnostics had printed). Weight decay alone would have taken
them only to about 34 per cent, so training pushed them down. It was not decay
alone, and it was not the row-choice weights themselves, which grew.

On the toy models, and in arm T at 10 million, none of this happened. The
built-in answer chooses the row sharply there, and taking the "this turn is
yours" signal out of the trunk changes almost nothing (arm T 0.986 to 0.978;
the toy arm M 1.000 to 1.000).

**Which hypothesis the outputs support:** the first, in part. H1's result has
three parts:

- its first claim, that the trunk's "this turn is yours" signal and not the
  built-in answer carries the separable answers, is **supported by D5**, which
  was planned;
- the mechanism the method gave for it ("the answer comes out right whichever
  row the slot selects") is **rejected by D3**, which was planned: forcing a
  wrong row gives that agent's answer, 3,570 of 3,570;
- the mechanism that replaces it, a flat row choice over a large own row, comes
  from **D7, added after the planned diagnostics had printed**.

The second hypothesis (the check is wired differently) and the third (a
bookkeeping error) are rejected by their planned diagnostics. For the fourth
(weight decay drove the row-choice weights to zero), **D6 matched neither of
its planned patterns**: the row-choice weights grew, which is not the
"supported" pattern, but the row choice is flat, which is not the "rejected"
pattern. Calling it rejected as stated is this session's reading, because the
weights it named grew; it is not the planned reading. What did shrink is the
marker words' embeddings, about ten times further than decay alone could take
them, and that comes from D8, added later.

**What stays unexplained:** why training pushed the marker words' embeddings
down in arm M at 10 million and not in arm T or on the toy. Also unexplained is
the order of events: whether the trunk took over first and the built-in answer
then faded, or the reverse. Only the final checkpoints exist, so neither can be
measured from what is on the laptop.

## Words used below

- **The acting channel**, or "this turn is yours" signal: a learned vector
  added to the trunk's input on every token of the model's own assignment
  turns (`act_vec` in `models.py`). It is the only honest source of who the
  model is.
- **The built-in ownership answer**: the hand-built tally of which agent's
  turns the acting channel fired on, turned into a 24-wide vector made from
  that agent's marker word (`_own_vec`). It sits in the **slot**, the last 24
  dimensions of the running state, which no block touches.
- **The row choice**: the separable head compares the slot with each agent's
  marker key and chooses a row of the lookup table (a softmax over the four
  agents). **The table** holds, for each agent and item, a vector made by the
  trunk from that agent's value word. **The rule** turns the chosen row into
  the answer.
- **Route use** (part B of the in-use check): of the own-directed actions right
  with the built-in answer, the share no longer right once that answer is
  swapped to point at the next agent round (`procedure.route_in_use`, bar 0.5).
- **Separable actions**: own-directed actions about items it0 and it4 in arm M
  (all own-directed actions in arm T).

## Models examined

| Name below | File | Checksum |
|---|---|---|
| M 10M rerun | `~/Code/minimum-viable-mind/experiments/08-successor-degree/artifacts/succ_m_10m_seed0_rerun/succ_m_10m_seed0_rerun.pt` | md5 `c4701f70e7967e008954640c88e89112`, as the run record gives |
| T 10M rerun | `.../succ_t_10m_seed0_rerun/succ_t_10m_seed0_rerun.pt` | md5 `c9f2684070a67920577b26f2f1662ffd`, as the run record gives |
| M toy, seeds 0 to 2; T toy, seed 0 | `experiments/08-successor-degree/out-sharpness-fix/models/ckpt_{M,T}_fixed_seed*.pt` (sharpness fixed at 4.0) | sha256 checked against that folder's `SHA256SUMS`: all OK |

All on the 3,000 gate episodes exactly as the frozen procedure builds them
(`procedure.EvalData().gate`).

## Where the commands and outputs are

Every script is in `docs/2026-10-18-arm-m-separable-zero-scripts/`, run from
that folder as `~/Code/minimum-viable-mind/.venv/bin/python <script>.py`, with
its full printed output beside it as `<script>_output.txt`. Library versions in
every output: torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, Python 3.12.13,
processor. The scripts import the frozen code from
`experiments/08-successor-degree/src/` and change no file in it. D5, D7 and D9
replace one method (`_own_vec`) on the loaded model object in memory, inside
the script, and put it back.

- `checks_output.txt`: `git diff --stat 6c47c56 -- experiments/08-successor-degree/src/`
  printed nothing (the frozen folder is unchanged); the checksums above.
- D0 to D6 are the diagnostics the method named, in its order. **D7, D8 and D9
  were added after D0 to D6 had printed**, because those outputs raised
  questions the method did not foresee. They are labelled as added wherever
  they are used. The H1 verdict on where the answer comes from rests on D5,
  which was planned. But two parts of the account rest on added diagnostics
  alone: that an even mix of the rows is enough to give the own answer (D7),
  and that the row choice is flat because the marker-word embeddings shrank
  (D8).

## Findings

### F0. The figure reproduces. MEASURED

`python d0_reproduce.py` (the frozen `procedure.route_in_use`), from
`d0_reproduce_output.txt`:

```
M-10M-rerun ... "separable": {"actions": 1190, "right": 1190, "still_right_after_swap": 1190, "route_use": 0.0}
               "entangled_items": {"actions": 1810, "right": 1387, "still_right_after_swap": 1354, "route_use": 0.0238}
T-10M-rerun ... "slot": {"actions": 3000, "right": 2959, "still_right_after_swap": 41, "route_use": 0.9861}
M-toy-seed0 ... "separable": {"actions": 1190, "right": 1190, "still_right_after_swap": 0, "route_use": 1.0}
M-toy-seed1 and seed2: separable route use 1.0, 1,190 right, 0 still right after swap
T-toy-seed0 ... "slot": route_use 1.0
```

The run record's figures (0.000, 0.024, 0.986) and the toy figure (1.000) are
reproduced exactly. In every model the built-in answer itself is right: weight
on the true agent 0.9990.

### F1. No bookkeeping error (H3 rejected). MEASURED

`python d1_bookkeeping.py`, on arm M 10M rerun:

```
(a) ... item word two before the mask differs from the item word of the assignment turn for the action's item: 0
    mask disagreements with 'item word is it1, it2 or it3': 0
    separable actions by item word: it0 616, it1 0, it2 0, it3 0, it4 574
(b) actions (both conditions) where the returned logits are not exactly the separable route's on the separable mask: 0; not exactly the stirred-in route's on the other: 0
(c) separable own-directed actions: 1190 of 3000, share 0.3967 (expected about 0.4 ...)
```

The 1,190 actions the check counts as separable are exactly the it0 and it4
actions, and on each of them the model returns exactly the separable head's
answer, bit for bit.

### F2. The swap reaches the slot; the row choice does not follow it, because it is flat (H2 rejected). MEASURED

`python d2_swap_reach.py`:

| Model | Slot moves under the swap | Mean size of the move | Weight on the true agent, true answer | Weight on the next agent, swapped answer |
|---|---|---|---|---|
| M 10M rerun | 1,190 of 1,190 | 0.22 | 0.2545 | 0.2540 |
| T 10M rerun | 3,000 of 3,000 | 20.41 | 0.9780 | 0.9790 |
| M toy seed 0 | 1,190 of 1,190 | 6.29 | 0.9989 | 0.9988 |
| T toy seed 0 | 3,000 of 3,000 | 7.46 | 0.9974 | 0.9974 |

The swap moves arm M's slot on every action, as it does arm T's, so the check
is not missing the route. **ARGUED, from the code:** the swap reaches arm M's
separable head by the same path as arm T's (`swap_answer` changes only
`assign_agent_at`, which only `_own_vec` reads, and both arms use the same
`_own_vec` and `_separable_logits`). What differs is that arm M's row choice
puts about a quarter on every agent under both answers, and its slot moves a
ninety times less than arm T's (20.41 against 0.22). By the method's own rule, a flat row choice is
read under H4 and is not H2.

### F3. Forcing a row gives that row's agent's answer, and arm M's own row is much the largest. MEASURED

`python d3_forced_row.py`:

```
M-10M-rerun: row forced onto a wrong agent: 3570 cases, still the model's own answer 0, that agent's answer 3570
             table row size (mean norm): true agent's row 11.642, other agents' rows 3.105
T-10M-rerun: row forced onto a wrong agent: 9000 cases, still the model's own answer 25, that agent's answer 8960
             table row size (mean norm): true agent's row 12.657, other agents' rows 12.928
M-toy-seed0: ... that agent's answer 3570; rows 12.192 and 11.485
T-toy-seed0: ... that agent's answer 9000; rows 16.370 and 16.386
```

**By the method's pre-stated reading for D3, this rejects H1 as the method
worded it** ("H1 rejected if in arm M forcing a wrong row gives that agent's
answer, as in arm T"). The table rows do not all say "own": each row still
holds its own agent's value, in arm M as in arm T. The method's parenthetical
"or the own row dominates" did not anticipate what follows, because D3 forces a
single row, so a large own row could never have produced the own answer here.
What the same output does show, as a side figure, is that in arm M at 10
million only the model's own row is far larger than the others (mean size 11.6
against 3.1). In every other model the rows are the same size. F5, and F6 from
an added diagnostic, show what that does.

### F4. Named-other actions by route. MEASURED

`python d4_named_by_route.py`:

```
M-10M-rerun  own separable 1190/1190 1.000; own stirred-in 1387/1810 0.766
             named-other separable 1178/1178 1.000; named-other stirred-in 555/1822 0.305
M-toy-seed0  own separable 1.000; own stirred-in 0.773; named-other separable 1.000; named-other stirred-in 0.287
T-10M-rerun  own 0.986; named-other 0.993
```

Arm M's separable named-other actions are all right, at 10 million and on the
toy. **ARGUED:** this fits F3. The named-other action's row is chosen by
`action_who` directly, not through the slot (`_separable_logits`, `sel_named`),
and the rows still hold each agent's value. So a large own row does not spoil
naming another agent once that agent's row is chosen exactly. Arm M's poor
named-other score in the run record (1,733 of 3,000) comes entirely from the
stirred-in items.

### F5. Take the acting channel out of the trunk only, and arm M's separable answers fall to chance (H1 supported). MEASURED

`python d5_trunk_lesion.py`. The trunk sees the episode with the acting channel
set to zero, while the built-in answer is still computed from the real episode:

| Model | Separable own-directed right, frozen | Right with the trunk lesioned | Route use, trunk lesioned | Right with acting zeroed everywhere |
|---|---|---|---|---|
| M 10M rerun | 1,190 of 1,190 (1.000) | 327 (0.275) | 0.177 | 296 (0.249) |
| T 10M rerun | 2,959 of 3,000 (0.986) | 2,934 (0.978) | 0.990 | 767 (0.256) |
| M toy seed 0 | 1,190 (1.000) | 1,190 (1.000) | 1.000 | 299 (0.251) |
| T toy seed 0 | 3,000 (1.000) | 3,000 (1.000) | 1.000 | 740 (0.247) |

This is the method's pre-stated test for H1, and it comes out the way H1
predicts. In arm M at 10 million, with the built-in answer intact and correct,
the separable half answers at about chance (one in four) once the trunk loses
the acting channel. So the trunk's acting channel is what was carrying it. In
arm T at 10 million and in the toy arm M, the same lesion changes almost
nothing, because their built-in answer is carrying it.

### F6. Added after the first outputs: an even mix of the four rows is enough for arm M at 10 million. MEASURED

`python d7_flat_choice.py` (D7, not in the method):

```
M-10M-rerun: flat mixture of the four rows, own answer right: 1190 (1.000)
             flat mixture, acting channel out of the trunk:    296 (0.249)
             own row's size over the other rows' mean size: 3.775; with the acting channel out of the trunk: 1.017
T-10M-rerun: flat mixture 970 (0.323); own row's size ratio 0.991
M-toy-seed0: flat mixture 518 (0.435); ratio 1.064
T-toy-seed0: flat mixture 710 (0.237); ratio 0.999
(sanity, every model: the rule on the true row differs from the forced-row head in 0 actions)
```

This joins F2, F3 and F5 into one account. Arm M's row choice is flat (F2), so
the head gets roughly an even mix of the four rows. The trunk, through the
acting channel, makes the own row about 3.8 times the others (D7's per-action
ratio, 3.775; F3's mean sizes say the same), and that is
enough for the rule to give the own answer every time. Take the acting channel
out of the trunk and the own row is no bigger than the rest (ratio 1.017), and
the even mix falls to chance (0.249). Swapping the built-in answer changes a
choice that was already flat, so it changes nothing.

### F7. The row-choice weights grew; the marker words' embeddings shrank far below decay alone (D6 matched neither planned pattern for H4). MEASURED

`python d6_weights.py`. Weight decay alone, by `decay_alone.py`'s arithmetic
(pull request 112), multiplies a weight by **0.3350** over the 10-million run
and by **0.9631** over the toy run. Weight sizes at the end, against the
starting weights (rebuilt with the trainer's own seed and code):

| Weight | M 10M rerun, end over start | T 10M rerun, end over start |
|---|---|---|
| `read_own.weight` (the slot's query) | 1.92 | 1.13 |
| `own_key.weight` (the row keys) | 1.37 | 1.13 |
| `own_marker.weight` (marker word to 24-wide vector) | 0.88 | 3.27 |
| `to_val.weight` (the table) | 3.02 | 2.42 |
| `act_vec` (the acting channel) | 19.3 | 18.6 |

The row choice at the own-directed action (true answer, separable actions):

```
M-10M-rerun  score gap top minus second    0.035; weight on top row 0.2616 (flat would be 0.25); size of the slot's query 0.561
T-10M-rerun  score gap top minus second  278.988; weight on top row 1.0000; size of the slot's query 20.479
M-toy-seed0  score gap top minus second   10.213; weight on top row 0.9989
T-toy-seed0  score gap top minus second    8.914; weight on top row 0.9974
```

H4 as the method stated it predicted that `read_own` and `own_key` would end at
or below about 0.335 of their start. They ended at 1.92 and 1.37, larger than
arm T's, so the "supported" pattern did not fire. The "rejected" pattern needed
arm M's weights as large as arm T's *and* its row choice as sharp, and the row
choice is flat (weight on the top row 0.2616), so that pattern did not fire
either. **D6 matched neither planned pattern.** This session reads H4 as
rejected as stated, because the weights it named grew; that is this session's
reading, not the planned one.

`python d8_answer_vector.py` (D8, added after the first outputs) finds why.
Both the slot and the row keys are made from the agents' marker-word embeddings
through `own_marker`. Only the part of those vectors that differs from one
marker word to the next lets the row choice tell agents apart:

```
M-10M-rerun  end   vector 1.670  differing part  0.151  keys' differing part  0.132  embeddings  0.503
             start vector 2.541  differing part  2.422  keys' differing part  1.383  embeddings 14.940
             differing part, end over start 0.0625 (decay alone: 0.3350)
T-10M-rerun  end   vector 14.258 differing part 14.085  keys' differing part 21.526  embeddings  5.697
             differing part, end over start 5.8165
M-toy-seed0  end   differing part 4.269; embeddings 10.248
T-toy-seed0  end   differing part 5.067; embeddings 11.069
```

In arm M at 10 million, the marker words' embeddings ended at 0.503 against
14.94 at the start, which is 3.4 per cent. With them, the differing part of the
built-in answer's vector ended at 6 per cent of its start. **ARGUED, by pull
request 112's size argument:** decay alone can take a weight only to 33.5 per
cent over this run. A weight that ends at 3.4 per cent was pushed down by the
training signal, not merely left to decay. Arm T's marker embeddings also ended
smaller (38 per cent, about what decay alone gives), but its `own_marker` grew
3.3 times and made up for it: the differing part ended 5.8 times its start.

**ARGUED, on the starting weights:** they were rebuilt on the laptop with
`torch.manual_seed(0)` and `models.build(arm, "10M")`, the steps
`train_successor.run` takes before moving the model to the graphics card. They
were not compared with a saved starting checkpoint, because none exists. The
rebuilt arm T and arm M starts agree where they share shapes (marker
embeddings 14.94 in both; `own_marker` 2.787 in both). Starting sizes of
randomly drawn weights of these shapes vary little from one draw to another, so
the ratios would hardly move even if the draw were not the trainer's.

### F8. Added after the first outputs: arm M's stirred-in items lean on the trunk's acting channel on the toy too. MEASURED

`python d9_stirred_in_items.py` (D9, not in the method). Arm M's stirred-in
own-directed actions:

```
M-10M-rerun: frozen 1387 (0.766); swapped answer 1405 (0.776); trunk lesioned 267 (0.148)
M-toy-seed0: frozen 1400 (0.773); swapped answer 1398 (0.772); trunk lesioned 400 (0.221)
```

In both arm M models, the stirred-in items get their answer from the trunk's
acting channel, not from the built-in answer. That fits the low stirred-in
route use the record already gives (0.024 at 10 million, 0.09 on the toy).
**ARGUED:** so "the trunk learned to read the acting channel" is true of arm M
on the toy as well, where the separable half still used its slot (F5). What
sets arm M at 10 million apart is two further things, both measured above: the
table's own row grew large from the acting channel (F6), and the marker-word
embeddings the row choice depends on collapsed (F7). Arm T has no stirred-in
items, and at 10 million its table rows stayed equal (ratio 0.991).

## What the outputs do not settle

1. **Why training pushed arm M's marker-word embeddings down at 10 million.**
   The shrinking itself comes from D8, a diagnostic added after the planned ones
   had printed; the size argument then shows the training signal did it (F7). It does not show
   which part of the model the signal came from. In arm M the marker words feed
   the trunk as text, and through `own_marker` they feed the slot, the row
   keys, every block's scale-and-shift and the value-word binding. One possible
   account, not measured: once the trunk carries ownership, the built-in answer
   is only noise to the scale-and-shift and binding that enter every block, so
   training shrinks what it is made of. Settling that needs the gradient at
   points during training, or checkpoints saved along the way. Neither exists,
   and making them means training, which this task did not authorise.
2. **The order of events.** Whether the trunk took over first and the row
   choice then went flat, or the row choice went flat first and the trunk filled
   the gap, cannot be told from the final checkpoints alone.
3. **One seed.** The 10-million figures are one seed of each arm (seed 0), as
   the reruns were.
4. **Why the toy did not do it.** **ARGUED:** the toy run was 2,500 steps,
   against 108,919 at 10 million, and its decay factor is 0.963 against 0.335.
   That leaves much less room for any slow drift, whether from decay or from
   training. This fits the contrast but does not prove it is the cause.

## For the write-up, in one sentence

At 10 million parameters, arm M's separable half answered from the "this turn
is yours" signal in its shared trunk rather than from its built-in ownership
answer (a planned test), so swapping the built-in answer changed nothing. The
toy models and arm T kept using the built-in answer. Diagnostics added after
the planned ones suggest how: training made the model's own table row much
larger than the others, and shrank the marker words its row choice depends on
until that choice went flat.
