# Gate 2 — the A3 learnability pilot

*2026-09-16. Status: **measured record, not adjudicated.** The verdict is
John's at the registered analysis point. The run completed its full
registered budget: 55,116 steps, 585,552,384 tokens, one register-less 30M
model at seed 0 on the registered A3 grammar. Launched on John's go,
quoted verbatim in the ledger as "Go". Actual cost **$13.92** against a
$9 to $13 estimate; A3 cumulative **$13.92 of the $100 hard stop**.
Checkpoint `a3_30m_seed0.pt`, md5 `f751228c…`, verified against the pod
before it was reaped. Endpoint record: `a3-gates/pilot_endpoint.json`.*

## The headline: the objective is learnable, and it is genuinely about ownership

Verdict evaluation at 800 episodes, which yields 400 scoring cells on the
primary battery. The in-training evaluations used 100 episodes and are
trajectory only.

| battery | intact | acting channel zeroed | its shortcut ceiling |
|---|---|---|---|
| **T_act** (primary, the action) | **0.506** | **0.182** | 0.2921 |
| T_other (control) | 0.299 | 0.234 | 0.3227 |
| T_state (ownership-free) | 1.000 | 0.999 | — |
| T_syntax (floor check) | 1.000 | 1.000 | — |

**The primary battery is 0.214 above the best score any ownership-blind
solver can reach.** The shortcut sweep put that ceiling at 0.2921 and
confirmed it empirically at 0.3036 over 12,000 episodes. So the model is
doing something no amount of reading the transcript can produce. Kill
criterion K2, unlearnable, does not fire.

**The L0 validity check passes decisively, and selectively.** Zeroing the
acting channel — the only authorship signal in the design — takes the
primary battery from 0.506 to 0.182, while the ownership-free batteries
do not move at all (1.000 to 0.999, and 1.000 to 1.000). The damage is
specific to the battery that needs to know which agent the model is. This
is the check that would have exposed the whole objective as hollow, and it
is the one that a smoke-scale control gave a false pass on earlier in this
programme. At full scale it is unambiguous.

**Under the registered metric the drop reads 1.515**, and that number is
worth pausing on. It exceeds 1.0, meaning the lesion took the battery
*below* what an ownership-blind solver achieves. That is expected — a
model deprived of an input it has trained on for 585 million tokens is off
its distribution and is not a rational fallback solver — and it is exactly
the case John's decision 3 ruled must be reported rather than clipped. A
clamp would have turned the most informative number in this table into a
quiet 1.000.

**The supplementary read is cleaner still.** Evaluated at one reviser,
where the ownership-blind ceiling is exactly 0.25 rather than 0.2921, the
primary battery scores 0.531, a margin of +0.281. This carries a
distribution shift from the training grammar and is supplementary, never
the headline, per the ruling that introduced it.

## The control battery never learned, and that has a consequence

`T_other` finished at **0.299, which is below its own shortcut ceiling of
0.3227**. It never acquired marker-keyed retrieval at all. Nothing it did
requires anything beyond the eliminations an ownership-blind solver is
entitled to.

This repeats the registered programme's own history: the comparable
retrieval ability was a seed lottery that only two of five earlier runs
ever won, and the three that lost sat flat at 0.34 against a chance floor
of 0.125.

**The consequence is structural and John should see it before the lesion
phase.** Because the control's baseline sits below its ceiling, the
registered floor rule makes its drop **undefined** — the denominator is
negative. Any bin that compares the two batteries' drops therefore cannot
be evaluated on this checkpoint, in either direction. The
H_generic-binding bin, which exists to catch "the lesion hit generic
who-did-what machinery rather than a self-index", has no signal on the
side it needs.

There is a reading on which that is benign: if generic binding was never
learned, a positive on the primary battery cannot *be* generic binding,
because there is no generic binder to confuse it with. There is a reading
on which it is not: the control was the registered discriminator, and a
discriminator that cannot fire is not doing its job, whatever the
alternative argument says. Which reading governs is an adjudication, not a
measurement, and it belongs to John.

## What bin this lands in is not obvious, and that is worth saying plainly

The starvation criterion, K3, is written as "T_act reaches ceiling early
while T_other stays flat at the end of the token budget". **Half of that
fired and half did not.** The control battery is flat, exactly as the
criterion describes. But the primary battery is at 0.506, not at ceiling:
it is well above its shortcut floor and nowhere near 1.0, and its
trajectory over the last fifth of training is flat around 0.537 rather
than saturated.

So the honest description is **partial learning on the primary battery and
none on the control**, which is neither the clean positive the design
hoped for nor the clean starvation the criterion describes. The bins were
written before the grammar existed, which is the same gap red-team pass 3
flagged when it found them neither exhaustive nor mutually exclusive.

## Two process failures, one of which cost money

**A truncated checkpoint loaded without complaint.** The watchdog's
fetched copy was 324MB against the pod's 351MB, and it opened cleanly,
reported the right step count and a plausible trajectory. Had it been
trusted, every number above would have come from a corrupt file. It was
caught by comparing sizes against the pod before reaping it, and the
checkpoint was re-fetched by tar and verified by checksum. **A streamed
`cat` over ssh truncates binary silently; the tar path does not.** The
watchdog should verify a checksum after every checkpoint pull, and that
should be fixed before seeds 1 and 2.

**The idle-billing failure recurred.** Training finished at 09:54Z and the
watchdog only woke to reap the pod at 13:47Z, so the pod billed 3.9 idle
hours, about $3.8 of the $13.92. The Mac slept: `caffeinate -i` blocks
idle sleep but not lid-close. This is the third time — wave 2 lost about
$5.70 the same way and the ledger already carries a standing note about
it. Three occurrences is a design problem, not a habit problem. The
watchdog deadline should be driven by something that does not sleep, or
the pod should carry a self-kill that does not depend on a laptop being
awake.

A third, smaller item: the watchdog's incremental log fetch stopped when
the Mac slept, so the local evaluation log had 68 of 111 rows. The full
trajectory was recoverable because the trainer stores it inside the
checkpoint, which is a piece of redundancy worth keeping deliberately.

## What Gate 2 does not claim

It does not claim a self-index was found. It claims the objective is
learnable at 30M and that what was learned depends on the authorship
signal. Whether the structure carrying that dependence is a center, a
re-readable tag, or something diffuse is the lesion phase, which needs
the threshold lock first, and the lock needs John's commit.

It is one seed. The registered bin rule requires the positive on all
three, and binding at 30M was seed-dependent throughout the earlier
programme.

## What needs John

1. **Adjudicate the bin.** Partial learning on the primary, none on the
   control, K3 half-fired. The bins do not cleanly cover this.
2. **Rule on the undefined control drop** before the lesion phase, since
   one registered bin cannot fire on this checkpoint.
3. **Whether seeds 1 and 2 launch**, at about $11 each on a fresh go, and
   whether the two process fixes above land first.
