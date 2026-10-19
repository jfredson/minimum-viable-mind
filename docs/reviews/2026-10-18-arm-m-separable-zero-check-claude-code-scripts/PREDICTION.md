# The checking session's own check, stated before it ran (2026-10-18)

*Written by the session checking pull request 180 (why arm M's separable half
reads zero route use at 10 million parameters), and committed on its own before
`e1_trunk_redirect.py` was run. $0: forward passes of saved checkpoints on the
laptop's processor.*

## Why this check

The findings rest the verdict on the first hypothesis (H1: the shared trunk
carries the "this turn is yours" signal, so the built-in ownership answer is not
consulted) on D5: remove the acting channel from the trunk only, and arm M's
separable answers fall to about one in four. A fall to chance shows the answer
needs something the lesion removed. It does not show what that something says.
A trunk knocked off the inputs it was trained on could fail for reasons that
have nothing to do with ownership.

So this check moves the signal instead of removing it. The trunk sees the
acting channel on the next agent round's two assignment turns instead of the
model's own (the action turns are left as they are), while the built-in
ownership answer still reads the real episode. This is the mirror image of the
frozen check, which moves the built-in answer and leaves the trunk alone. It is
done the same way as D5: by wrapping `_own_vec` on the loaded object in memory.
No file of the frozen code changes.

## What H1 predicts, and what would count against it

On the gate episodes, own-directed actions:

1. **Arm M at 10 million, separable items (it0 and it4), 1,190 actions.** If H1
   holds, the answer follows the trunk: **at least 80 per cent** of these
   actions give the next agent round's answer, and **at most 10 per cent** the
   model's own answer. The next agent's table row becomes the large one: its
   size over the other rows' mean is **at least 2.5**.
2. **Arm T at 10 million (3,000 actions) and toy arm M seed 0 (1,190 separable
   actions).** Their built-in answer carries the choice, so the answer stays:
   the model's own answer on **at least 95 per cent** of the actions it gets
   right unmoved, and the next agent's answer on **at most 5 per cent**.

**H1 is contradicted if** arm M's separable actions give the next agent's
answer on fewer than half of them under the move. That would mean the trunk's
acting channel is needed (D5) but does not say whose answer to give, and the
findings' account (the trunk makes the model's own row large, and an even mix
of the rows then gives the own answer) would be wrong. Between half and 80 per
cent, H1 is weakened, and the record says so.

Reported without a prediction: the same move on arm M's stirred-in items (it1
to it3), for both arm M models.
