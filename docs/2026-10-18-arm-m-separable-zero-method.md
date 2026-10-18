# Method: why arm M's separable half reads zero route use at 10 million parameters (2026-10-18)

*Written 2026-10-18 (Pacific) by a Claude Code session started from the
programme's master session, before any diagnostic output exists. This file is
committed on its own, before the scripts are run, under the pairing rule of
`docs/outside-review-protocol.md` (the section "The pairing rule: whatever one
session writes, a different session checks"). Written under the workspace
plain-language rule. $0: everything on the laptop's processor, nothing rented,
no model called by API. The frozen code, every registered text, figure and
ruling, `STATUS.md` and `data/project.toml` are not edited.*

## The question, and why it is owed

Experiment C, the degree experiment (registered text
`docs/successor-experiment-proposal-2026-10-07-v5.md`, frozen code at commit
`6c47c56` under `experiments/08-successor-degree/src/`), stopped on 2026-10-12
at its registered stop S4b, after the three 10-million-parameter reruns of its
hand-built reference models failed the in-use check
(`docs/2026-10-09-reruns-10m-run-record.md`;
`docs/rulings/2026-10-12-experiment-c-stop-ruling.md`). John ruled on
2026-10-17 that C stays stopped (`docs/rulings/2026-10-17-experiment-c-stays-stopped-ruling.md`),
and that the write-up owes, either way, an explanation of one puzzle named in
item 3 of the run record:

- **Arm M** is the half-and-half model: actions about items it1, it2 and it3
  go through a "stirred-in" (entangled) route, actions about items it0 and it4
  through a "separable" route built the same way as arm T's.
- **The in-use check, part B** ("route use", `procedure.route_in_use`, judged
  by `measure.route_check` against `ROUTE_USE_MIN` = 0.5) asks: of the
  own-directed actions the model gets right with its built-in ownership answer,
  what share does it get wrong once that answer is swapped to point at the next
  agent round?
- At 10 million parameters arm M's separable half reads **0.000** (1,190 right,
  all 1,190 still right after the swap; `out-reruns-10m/row_M_seed0.json`).
  Arm T's slot, built the same way, reads **0.986** in the same reruns. On the
  toy models (`out-sharpness-fix/retrained_inuse.txt`, three seeds, sharpness
  fixed at 4.0) arm M's separable half reads **1.000** on every seed.

Nothing about C's ending changes whatever the explanation turns out to be.

## What arm M's separable route is, read from the frozen code

From `models.py` (`MiddleArm.forward` and `_Shared._separable_logits`), stated
here so the hypotheses can be checked against it:

1. The **ownership answer** (`_own_vec`) is a running tally of which agent's
   assignment turns the "this turn is yours" signal (the acting channel) fired
   on, turned into weights over the four agents at a fixed sharpness of 4.0,
   and then into a 24-wide vector (the agent's marker word through
   `own_marker`). It reads `assign_agent_at`, which the swap changes.
2. That vector is carried, untouched by any block, in the last 24 dimensions of
   the running state: the **slot**.
3. The separable head reads the slot at the action (`read_own`), compares it
   with each agent's marker key (`own_key`), and turns the comparison into a
   choice of row (a softmax over the four agents). It then takes, from a table
   built by `to_val` out of the trunk's state at each agent's assignment value
   word, the chosen agent's row for the action's item, and applies the rule
   (`rule`) to give the answer.
4. The table is built from the **trunk**, and the trunk is not blind to
   ownership: the acting channel's vector (`act_vec`) is added to the embedding
   on every token of the model's own assignment turns, including the value
   word, and in arm M the stirred-in route also enters every block (a
   scale-and-shift from the ownership vector) and every value word (`bind`).
   In arm T the acting channel is added to the trunk too; there is no
   scale-and-shift and no `bind`.

## The hypotheses, stated before any output

**H1. The trunk carries the acting signal for the separable items too, so
their built-in answer is not consulted.** The table rows (or the rule applied
to them) already say which agent is the model's own, read off the acting
channel in the trunk, so the answer comes out right whichever row the slot
selects. The swap moves the slot and the selection but not the answer.

**H2. The counterfactual is applied to a route the half-and-half construction
wires differently from arm T's.** The swap (`procedure.swap_answer`, which
moves every agent label in `assign_agent_at` on by one) does not reach arm M's
separable selection the way it reaches arm T's: for example the slot at the
action is unchanged by it, or the selection does not move to the next agent.

**H3. A bookkeeping error in which items count as separable.** The mask that
decides which actions count as separable in the check
(`MiddleArm.entangled_route`, the item word two tokens before the mask) does
not match the item the action is about, or does not match the route whose
logits the model actually returns, or the count of separable actions is not
the expected share (about two fifths: two of the five items in use).

**H4. Weight decay drove the separable half's selection weights to zero, as it
did the stirred-in routes.** The weights that turn the slot into a choice of
row (`read_own` and `own_key`) shrank until the choice no longer depends on the
slot, so swapping the answer cannot change the row chosen. The sign and size
argument is the one in the check of the arms C and M ruling packet (pull
request 112, `decay_alone.py`): with this recipe (AdamW, peak learning rate
0.002, weight decay 0.01, one-cycle, 108,919 steps) decoupled decay alone
multiplies any weight by about **0.335** over the run. So a weight whose norm
ended near 0.335 times its starting norm was left to decay (no gradient
defended it); one well below that was actively pushed down by training; one
above it was sustained or grown by training. The toy recipe (2,500 steps,
peak 0.003, the same decay) gives a factor near 1, which is why decay could
matter at 10 million and not on the toy.

**H1 and H4 are not exclusive.** If the trunk makes the selection redundant
(H1), nothing defends the selection weights and decay shrinks them (H4). The
outputs below are read to say which of the two holds, or both, and in which
order: H1 is about where the working signal comes from; H4 is about whether the
built route's weights are gone.

**H0. None of these.** If no output below matches a hypothesis's predicted
pattern, the findings say so.

## The models examined

All read-only, loaded with `procedure.load_model` (which is the frozen code):

- arm M, 10 million, the rerun: `~/Code/minimum-viable-mind/experiments/08-successor-degree/artifacts/succ_m_10m_seed0_rerun/succ_m_10m_seed0_rerun.pt`, md5 `c4701f70e7967e008954640c88e89112` (the run record's checksum);
- arm T, 10 million, the rerun (the comparison): `.../succ_t_10m_seed0_rerun/succ_t_10m_seed0_rerun.pt`, md5 `c9f2684070a67920577b26f2f1662ffd`;
- the toy models with the sharpness fixed at 4.0: `experiments/08-successor-degree/out-sharpness-fix/models/ckpt_M_fixed_seed{0,1,2}.pt` and `ckpt_T_fixed_seed0.pt`.

Arm C is not examined: it has no separable route. The starting weights of the
10-million models are rebuilt with the trainer's own steps
(`torch.manual_seed(0)` then `models.build(arm, "10M")`, as
`train_successor.run` does) for the weight-size comparison in H4.

## The commands, and what each outcome would look like

Every script sits in `docs/2026-10-18-arm-m-separable-zero-scripts/`, imports
the frozen code from `experiments/08-successor-degree/src/` and changes nothing
in it. Where a diagnostic needs a model to see something other than the frozen
forward pass would show it (D5 below), it does so by replacing a method on the
loaded object in memory, inside the script; no file of the frozen code is
touched. Each script's printed output is saved beside it as `<name>_output.txt`.
The checkpoints are checked against their recorded md5 first, and
`git diff 6c47c56 -- experiments/08-successor-degree/src/` is run to show the
frozen folder is unchanged.

**D0. Reproduce the figure.** `python d0_reproduce.py`: the frozen
`procedure.route_in_use` on `EvalData().gate` for each model above.
*Expected:* arm M rerun separable 0.000 (1,190 of 1,190 still right), stirred-in
items 0.024; arm T rerun slot 0.986; toy arm M separable 1.000 on each seed.
*If not reproduced:* stop and report that; no hypothesis is read.

**D1. Bookkeeping (H3).** `python d1_bookkeeping.py`, on the gate episodes:
(a) the item word at two tokens before the mask, against the item word of the
assignment turn for the action's item (`tokens[assign_value_pos[a, item] - 1]`),
counting disagreements; (b) the logits the model returns, against the two
routes' logits computed separately from the same final state (the stirred-in
head on the action position; `_separable_logits`), counting actions where the
returned logits are not exactly the separable route's on the separable mask, or
not exactly the stirred-in route's on the other; (c) the count and share of
separable own-directed actions.
*H3 supported if* any count in (a) or (b) is non-zero, or (c) is far from two
fifths. *H3 rejected if* (a) and (b) are zero and (c) is near 0.4.

**D2. Does the swap reach the route? (H2).** `python d2_swap_reach.py`: on the
separable own-directed actions of arm M and on all own-directed actions of arm
T, (a) how far the slot at the action moves under the swap (mean size of the
change, and the share of actions where it moves at all); (b) the mean weight
the row choice puts on the true agent with the true answer, and on the next
agent round (the one the swap points at) with the swapped answer.
*H2 supported if* in arm M the slot does not move, or the row choice does not
follow the swap to the next agent, while in arm T both happen. *H2 rejected
if* the slot moves in both arms and, where the row choice is sharp, it follows
the swap in both. (If arm M's row choice is flat under both answers, that is
not H2; it is read under H4.)

**D3. Does the answer depend on which row is chosen? (H1).** `python d3_forced_row.py`:
on the separable own-directed actions of arm M (and, for comparison, on arm T
and toy arm M), force the row choice onto each of the four agents in turn (by
setting the action's `action_who` to that agent, which makes the head select
that row exactly) and count how often the answer is still the model's own
right answer, how often it is that agent's answer (the successor of that
agent's value on the item), and the size of each agent's table row.
*H1 supported if* in arm M the own answer comes out whichever row is forced
(the table itself carries the own answer, or the own row dominates), while in
arm T and toy arm M forcing a wrong row gives that agent's answer. *H1 rejected
if* in arm M forcing a wrong row gives that agent's answer, as in arm T.

**D4. The named-other actions by route.** `python d4_named_by_route.py`: the
named-other accuracy on the gate, split by whether the named-other action's
item is a separable or a stirred-in item, for arm M rerun, toy arm M, and
(whole) arm T. This is context for H1: a table that answers "own" whatever row
is chosen should be bad at naming another agent's answer.
*Reading:* reported beside D3; it supports H1 only together with D3.

**D5. Take the acting channel out of the trunk only (H1).** `python d5_trunk_lesion.py`:
the model's ownership answer is computed from the true episode, but the trunk
sees the episode with the acting channel set to zero (done in the script by
wrapping `_own_vec` on the loaded object so it always reads the unlesioned
acting channel). On the separable own-directed actions of arm M (and on arm T
and toy arm M) report the own-directed accuracy with the true answer, and the
route use computed the frozen way (true answer against swapped answer, both
with the trunk lesioned).
*H1 supported if* arm M's separable accuracy falls well below 1.0 once the
trunk loses the acting channel (the trunk was carrying it), while arm T's stays
near its unlesioned figure. *H1 rejected if* arm M's separable accuracy stays
near 1.0 with the trunk lesioned and the swap still changes nothing: then the
answer is coming from neither the slot nor the trunk's acting channel, and the
findings say what is left.

**D6. The sizes of the selection weights, and how flat the row choice is
(H4).** `python d6_weights.py`: (a) `decay_alone.py`'s arithmetic rerun for the
10-million recipe and for the toy recipe (one-cycle, 2,500 steps, peak 0.003,
first tenth warming up, decay 0.01); (b) for arm M rerun and arm T rerun, the
norm of each weight of the separable head (`read_own`, `own_key`, `to_val`,
`rule`, `own_marker`) and of `act_vec`, at the end and at the start (rebuilt
as above), and the ratio; (c) the spread of the row-choice scores across the
four agents at the action (the gap between the highest and the next score, and
the weight on the chosen row) for arm M rerun, arm T rerun and toy arm M.
*H4 supported if* arm M's `read_own` and `own_key` ended at or below about
0.335 of their starting size while arm T's ended above it, and arm M's row
choice is near flat (weight near one quarter on each agent) where arm T's is
sharp. *H4 rejected if* arm M's selection weights are as large as arm T's and
its row choice is as sharp. Where H4 is supported, the ratio says whether the
weights merely decayed (near 0.335: no gradient defended them, which is what
H1 would cause) or were pushed down by training (well below 0.335).

## How the findings will be written

`docs/2026-10-18-arm-m-separable-zero-findings.md`: every command and its
output (or the output file beside it), each finding labelled **MEASURED** (a
command and its printed output) or **ARGUED** (reasoning from measured figures
or the code), and one plain sentence saying which hypothesis the outputs
support, or that none does. A session that did not write the findings checks
them; the pull request body says what that session must check.

## What this does not do

It does not reopen, redesign, retrain or re-register experiment C, and it does
not read any figure against a bar other than the frozen code's own. It edits no
frozen code, registered text, figure, ruling, `STATUS.md` or
`data/project.toml`. It trains nothing; the only model runs are forward passes
of saved checkpoints on the laptop.
