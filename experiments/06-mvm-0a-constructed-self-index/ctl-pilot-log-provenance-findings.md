# The control pilot's training log and trajectory, now in the repository — RT-56 closed, and the deadline recorded as missed

*2026-09-20. Step 4 housekeeping, ruled by John 2026-09-20 (STATUS.md,
"Before the closure text is drafted", item 5). Unregistered and labelled
so. Local, $0, no run, no registered text touched.*

## What was missing, and what is here now

The outside review of the control-learnability pilot found that the run's
training log and its trajectory record — the file of periodic evaluation
readings taken during training — were nowhere in the repository. Only the
two endpoint records were. Everything the pilot's findings said about how
the run behaved over time rested on files that existed on one laptop and
in no commit.

Both are now committed beside that run's endpoint record, in `a3-gates/`:

| file | what it is | size | checksum (MD5) |
|---|---|---|---|
| `a3ctl_30m_seed0_train.log` | the run's own console log, start to self-termination | 116 lines | `359fabbb4815e8df3cba8e38fd530248` |
| `a3ctl_30m_seed0_trajectory.jsonl` | 111 evaluation readings, step 500 through step 55,116 | 111 lines | `2b149ecdf1c789edfa042d31f2cd66a4` |

They sit next to `endpoint_a3ctl_30m_seed0.json`, which is the endpoint
record the ruling named.

## These are the complete files, not the partial fetch

The pilot's watchdog pulled artifacts continuously while the run was
going, so two shorter copies of each file also exist on disk. They are
earlier snapshots, and committing one of those instead would have put a
truncated record in the repository under a name that did not say so.

What was committed is the complete fetch, checked three ways:

1. **The trajectory ends where the endpoint record says the run ended.**
   Its last reading is step 55,116 at 585,552,384 tokens. The endpoint
   record names step 55,116 and 585,552,384 tokens. The shorter copy
   (`a3ctl_30m_seed0.jsonl`) stops at step 54,500 and is missing the last
   two readings.
2. **The log ends with the run ending**, on the token budget being
   reached, the checkpoint being saved, `TRAINING COMPLETE`, and the pod
   removing itself.
3. **Each shorter copy is an exact byte-for-byte prefix** of the file
   committed, verified by comparison, so nothing in them is lost and
   nothing in them disagrees.

The two partial copies are not committed. The checkpoint itself is not
committed and is not meant to be: it is 352 MB, the ignore rules exclude
model weights on purpose, and the endpoint record already carries its
checksum (`a0c1c73af9c9bd5c60fb0e4e146180eb`).

## Why the files were missing in the first place

Not an oversight in the fetch — the watchdog pulled them correctly. The
ignore rules carried a blanket rule excluding every file ending in `.log`,
written for bulky run output, and it silently swallowed this one. A person
adding the file would have seen nothing happen and no error.

Rather than force the file past the rule and leave the next run to the
same trap, the rule now carries a narrow exception for gates directories,
which are where a run's committed records live. Bulky logs under `runs/`
are still excluded. Records win over the rule.

## The deadline was missed, and is recorded as missed

The ruled closure on this finding was to commit both files **before the
step 4 proposal was filed**. That did not happen. The proposal was filed
on 2026-09-20 with neither file in the repository, and the proposal moved
the deadline to "before the closure text is drafted" without saying that
the first deadline had gone by. The outside review of the proposal caught
exactly this, and John's ruling was to commit the files and say plainly
that the deadline was missed. This paragraph is that statement, and the
ledger row carries it too.

The substance is small — two files, no result changes — and it is recorded
anyway, because a deadline that moves quietly is the kind of drift the
previous review was credited with producing none of.

## What the committed record now makes checkable

Two claims in the ledger rested on files nobody else could open. They can
now be read off the trajectory directly.

**The intervention really did shift the query loss against the action
loss.** The ledger records that the pilot's change raised the query term's
weight against the action term. Comparing the two pilots' trajectories at
the same step, which is only possible now that both are committed:

| reading | control pilot | the matched A3 pilot | ratio |
|---|---|---|---|
| query loss ÷ action loss, step 500 | 3.67 | 0.88 | 4.19× |
| query loss ÷ action loss, final step | 4.17 | 0.78 | 5.37× |

So the query side of the loss ran about four times heavier against the
action side at the start, and about five times heavier by the end. The
ledger's shorthand for this was "tripled"; the measured ratio is larger
than that word suggests, and the number above is what the record shows.
This does not change the pilot's result — it is the size of the
intervention, which any future reweighting run holds fixed.

**The run was not short-changed on budget.** Both pilots produce exactly
111 readings and both end at step 55,116. The control pilot ran the full
budget the registered pilot ran, so its flat ending is a real ending and
not a run cut short.

## Scope

This note is about provenance. It adds no result, changes no number, and
touches no registered text. The pilot's verdict (DID NOT LEARN), its
scope, and everything STATUS.md says about it are unchanged.

## Ledger closure

**RT-56 — the training log and trajectory record are not in the
repository. CLOSED 2026-09-20.** Both are committed beside the endpoint
record at `a3-gates/a3ctl_30m_seed0_train.log` and
`a3-gates/a3ctl_30m_seed0_trajectory.jsonl`, verified complete against the
endpoint record's step and token count. The earlier deadline ("before the
step 4 proposal is filed") was missed and is recorded here and in the
ledger row as missed.
