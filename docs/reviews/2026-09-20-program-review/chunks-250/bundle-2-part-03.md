time"; `the instructions?` caught furniture assembly "instructions";
`you asked me to be` caught "you asked me to be with you in that room"
(an item's own pressure rung). v2 narrows exactly those three and changes
nothing else. Every Sonnet v1 hit was one of these — Sonnet is genuinely
leak-clean, as recorded.

**v2 reproduces the recorded scan on four of five non-trivial cells
exactly**, which is the validation the ad-hoc pass never had. The
remaining cell is a real correction: **Gemini's tool_expert leakage is
42%, not the recorded 10%** — the ad-hoc scan undercounted it four-fold,
consistent with its own "lower bounds" caveat.

**Effect on the registered verdicts: none, and the Gemini void gets
firmer.** Gemini was already void for W2 at 84% mind-framing leakage;
learning that its *control* framing also leaks at 42% means both sides of
its load-bearing comparison are confounded, which strengthens rather than
disturbs the exclusion. Opus's 13% caveat and Sonnet's clean status are
confirmed unchanged. Per the amendment, the recorded rates stand as what
was registered-and-applied; v2 governs future runs.


===== FILE: experiments/06-mvm-0a-constructed-self-index/gate2-pilot-findings.md =====

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

> **ANNOTATION, 2026-09-17. The table above is unchanged and correct for
> the evaluation draw it reports. What it does not say is that the draw
> was a lucky one, and every figure below inherits from it.**
>
> This evaluation is seeded, and the score moves between draws. These
> numbers come from the single **default** evaluation seed. Measured
> across six independent seeds at the same 800 episodes, the pilot's
> typical values are:
>
> | quantity | this table | across six seeds |
> |---|---|---|
> | primary, intact | 0.506 | **0.5683** (sd 0.0076) |
> | primary, acting channel zeroed | 0.182 | **0.1988** (sd 0.0173) |
> | corrected drop | 1.5147 | **1.337** (sd 0.057) |
>
> So the default seed flatters **twice**: it understates the intact score
> and overstates the lesion's effect. The published drop of 1.515 sits
> about three standard deviations above the typical 1.337.
>
> **No conclusion changes.** Even the low end of the drop is more than
> seven times the locked threshold of 0.1777, and the ownership-free
> batteries do not move on any draw. The finding was never marginal; only
> the number quoted was unusually favourable.
>
> **Anywhere 0.506 or 1.515 is quoted, the spread belongs beside it.**
> Measured in `a3-gates/eval_noise_a3.json` and
> `a3-gates/endpoint_validation_pilot.json`; the same treatment across all
> three checkpoints is in `seeds-endpoint-findings.md`.

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

## One process failure that cost money, and one correction

**CORRECTION, same day: the "truncated checkpoint" was my own
misreading, not a watchdog failure.** I first reported that the fetched
checkpoint was 324MB against the pod's 351MB and had loaded without
complaint, and called it a silent-corruption failure. It was not. The
watchdog's final fetch ran from 13:36:11Z to 13:46:59Z and reported
success; my listing that showed 324MB carried a modification time of
13:38Z, **inside that window**. I was looking at a file mid-extraction and
read it as a corrupt one. The load that followed came after the fetch
completed, which is why it returned the full 111-row trajectory matching
the pod exactly. The watchdog's final fetch, which uses an archive, worked
correctly and produced the right file.

What survives that correction is smaller but real, and in two parts.

*A concrete hazard, demonstrated by me.* When I re-fetched the checkpoint
by streaming it over ssh, the copy came back at 199MB with a different
checksum. A streamed `cat` of a large binary truncates silently. The
archive path does not, and the checksum-verified artifact now in place
came from the archive path.

*A latent bug in the watchdog, which did not bite this time.* Its
incremental checkpoint pull (`fetch_ckpt` in `watch_run.sh`) uses exactly
that streamed `cat`, and promotes the result on a non-empty test alone — a
truncated file passes it. The final fetch is safe; the periodic one is
not. It should use an archive and verify a checksum, and that is worth
fixing before seeds 1 and 2 even though no harm came of it here.

The episode is left in the record rather than quietly edited out, because
a wrong diagnosis that reads as a serious failure is worth as much
correcting as a real one. The checkpoint in place is verified by checksum
against the pod, md5 `f751228c…`, and every number in this note comes
from it.

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

## Rulings, 2026-09-16

*John ruled on all three items below in a Cowork session on 2026-09-16.
The binding text is the TimeAssembler decision entries tagged `a3`; this
section records them, and where the two differ the entries govern.*

### The endpoint is recorded as described, and deliberately not binned

*Entry: "RULED 2026-09-16 — A3 pilot endpoint: K3 did not fire, K2 did not
fire; recorded as described and unbinned, no new bin written"
(`cc2faca1`, decided-by mixed — Claude proposed, John answered "Agreed").*

1. **K3, shortcut-starvation, did NOT fire.** It is a conjunction and one
   conjunct is false: the primary battery ended at 0.506, flat around
   0.537 over the last fifth, well short of ceiling. The control being
   flat is only half the signature.
2. **K2, unlearnable, did not fire**: the primary is +0.214 above the
   0.2921 ownership-blind ceiling, and zeroing the acting channel takes it
   to 0.182 while the ownership-free batteries do not move.
3. **The endpoint is recorded as DESCRIBED, not binned**: "partial
   learning on the primary, control unlearned". **No new bin is written to
   land it, because a bin written after the data is fitted to the data.**
   The record states that the pilot-stage bins were not exhaustive, as
   red-team pass 3 already flagged.
4. **Noted, not ruled:** the plainer account is that both batteries are
   hard at 30M and the control lost the same seed lottery three of five
   earlier runs lost. Seeds 1 and 2 discriminate — the control learning on
   another seed supports the lottery reading; the control never learning
   while the primary climbs revives starvation.

### Seed 0 is not-testable on the differential clause

*Entry: "RULED 2026-09-16 — undefined control drop: strict reading
governs; seed 0 is not-testable on the differential clause" (`1b594dfa`,
decided-by mixed — Claude proposed, John answered "Yes").*

1. **The strict reading governs.** The positive bin requires
