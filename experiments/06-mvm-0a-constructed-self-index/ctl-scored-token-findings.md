# Exactly one scored token per row — HOLDS, on every row the pilot trained

*2026-09-20. Step 4 housekeeping, ruled by John 2026-09-20 (STATUS.md,
"Before the closure text is drafted", item 5). Unregistered and labelled
so. Local, $0, no training, no registered text touched. Method committed
before output at `e54748f`; run with `src/ctl_split_check.py
--scored-token`. Record: `a3-gates/ctl_scored_token_selftest.json`.*

## Verdict

**HOLDS**, on all four claims, with no exceptions found.

| quantity | value |
|---|---|
| steps replayed | 55,116 — every step the pilot trained |
| rows checked | 7,054,848 |
| most scored tokens seen on any single row | 1 |
| rows with zero scored tokens | 0 |
| rows with two or more | 0 |

## What was in doubt

The pilot's loss function walks along each row adding up a
per-position penalty — how surprised the model was by the token that
actually came next, which is the quantity training drives down — and
calls the total that row's penalty for getting the answer wrong. That
step is only sound if every row has exactly one **scored** position: one
token the penalty is actually collected at, with the rest of the row
ignored. The code said so in a comment and nothing tested it.

It matters because of what the pilot's change actually did. The control
battery's rows were given a loss term of their own, at four times the
weight. Each row's contribution to that term is the sum over its
positions. A row that carried **two** scored tokens would have its loss
counted twice, and so would carry twice its intended weight — silently,
with nothing anywhere to notice. A row that carried **none** would drop
out of its half of the split entirely. Either would mean the delivered
supervision was not the supervision the pilot reported delivering, which
is the one thing the run was built to measure.

The review filed this as worth-noting rather than serious, on the
reasoning that the assumption is probably true. It is, and now it is
checked rather than assumed.

## The four claims, and why it takes four

A single assertion would not have covered it. Each of these can fail
while the others hold.

**B1 — the loss mask has exactly one 1 per row.** The direct reading of
the comment. Checked on every row of every batch: 7,054,848 rows, maximum
1, minimum 1.

**B2 — it survives the shift the loss function applies.** This is the one
that actually guards the code. `loss_a3` does not sum over the mask; it
sums over `loss_mask[:, 1:]`, the mask with its first column dropped,
because the model predicts each position from the one before it. B1 does
not imply B2. A mask whose single 1 sat at index 0 would satisfy B1 and
then vanish under the shift, leaving that row scored on nothing and
quietly dropped from its side of the split — and the divisor in the split
term counts rows, not scored tokens, so the loss would be diluted rather
than erroring. Checked separately on all 7,054,848 rows: holds.

**B3 — the scored token is the query's own answer.** One scored token per
row is not enough; it has to be the right token. If the mask pointed at
the end-of-sequence marker or at the last word of the question, every row
would still have exactly one and the per-row number would be a
cross-entropy on the wrong thing. Checked by decoding the token at the
scored position and comparing it against the query's answer, on every
row: holds.

**B4 — the identity the comment is really claiming.** The comment's
purpose is to license treating the per-row sum as the row's answer loss.
That licence is testable directly: when every row has exactly one scored
token, the registered pooled query term must equal the mean of the
per-row terms. Rather than restate the arithmetic, this runs the **real
loss function** both ways on the same batch — once by the registered path
with the flag off, once by the split path with every row marked as a
control row at weight 1, which reduces to that mean.

| path | query term |
|---|---|
| registered pooled term (flag off) | 48.558334 |
| mean of the per-row terms (split path) | 48.558342 |

The two agree to six significant figures, a relative difference of about
1.6 parts in ten million. That is ordinary single-precision rounding in a
sum over 83 positions, not a discrepancy: the sums are taken in a
different order, so they round differently in the last place.

## How this was run at $0

No model and no checkpoint are needed for B1 to B3, and that is not a
shortcut — it is a fact about the code. The trainer builds each batch by
generating episodes from a seed, enacting the model's own turns, choosing
each row's query, and encoding. Only the acting-channel injection needs a
model, and it changes neither the episodes, nor the queries, nor the loss
mask. So replaying the pilot's two seeds reproduces every batch's mask bit
for bit on a laptop. B4 does need a model and uses an untrained
smoke-scale one on the processor; the loss path under test does not care
what the weights are.

This is why the check covers all 55,116 steps rather than a sample. A
sample would have left the honest statement at "no counterexample in the
steps we looked at". The statement available instead is that there is no
counterexample in the run.

## Scope, stated plainly

This checks the pilot's batches as the pilot built them: seed 0, batch
128, control weight 2.0, control fraction 0.5. It says nothing about
other settings, and it is not a proof about the grammar — a future change
to the tokenizer or to how queries are attached could break any of the
four, and this check would have to be re-run to notice. It is a
measurement over a finite, complete set of batches, which is what the
closure asked for.

It also changes no result. The pilot's verdict stands exactly as ruled;
this removes a way it could have been wrong, and finds that it was not.

## Ledger closure

**RT-59 — "exactly one scored token per row" is asserted in a comment and
never tested. CLOSED 2026-09-20, HOLDS.** Tested on all 7,054,848 rows of
all 55,116 steps the pilot trained, on four claims: exactly one masked
token per row; it survives the shift the loss function applies; it is the
query's answer token; and the pooled query term equals the mean of the
per-row terms when run through the real loss function both ways. No
exceptions. The assumption the split term rests on is sound, and the
weight the control battery received is the weight the pilot reported.
Check at `src/ctl_split_check.py`, record at
`a3-gates/ctl_scored_token_selftest.json`.
