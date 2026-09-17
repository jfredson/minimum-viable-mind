# Blind-localization arm — result

*2026-09-16. Local, $0, no compute rented. Read strictly against the
criteria committed in `401a54d` and `da0427f` **before the run produced
any output**. No bin was added after the fact.*

## Verdict

**NOT FLAGGED**, and within that, the sub-bin **instrument failure to
locate**.

The stack did not find own-agent identity at all. Criterion (a) — the
best probe clearing its label-permutation null by three standard
deviations — failed at every layer, and failed by a wide margin. The best
layer reached **1.3 standard deviations**, less than half the bar.

Because (a) failed, criterion (b) is moot: the subspace that was ablated
is one the probe never validly located, so the small drops below are
ablations of a direction that decodes at chance. They are reported for
completeness, not as evidence.

## The numbers

Four agents, so chance is 0.25. Every probe sits on it.

| layer | probe accuracy | null mean | null sd | margin |
|---|---|---|---|---|
| 3 | 0.2575 | 0.2473 | 0.0249 | 0.41 sd |
| 4 | 0.2675 | 0.2482 | 0.0243 | 0.80 sd |
| 5 | 0.2625 | 0.2435 | 0.0224 | 0.85 sd |
| **7** | **0.2750** | 0.2441 | 0.0237 | **1.30 sd** |
| 8 | 0.2450 | 0.2417 | 0.0227 | 0.15 sd |

Ablating the best-layer subspace at the inherited rank moved nothing. The
largest chance-corrected drop was **0.0739**, against the ruled Gate 0
band of 0.25, and it was **negative** — the battery it touched went *up*,
from 0.842 to 0.895, which is what noise looks like.

| battery | baseline | lesioned | drop |
|---|---|---|---|
| T_sr | 0.993 | 0.985 | 0.0092 |
| T_si | 0.960 | 0.955 | 0.0060 |
| T_state | 0.993 | 0.990 | 0.0033 |
| T_syntax | 1.000 | 1.000 | 0.0000 |
| T_sr_rev | 0.842 | 0.895 | −0.0739 |

## What this does and does not support

**It supports specificity only, never sensitivity.** That sentence was
written into the criteria before the number was seen, on John's ruling,
precisely so this result could not be read as a vindication of the
instruments. It is not one.

What the run shows is that on a checkpoint where a designated self-
structure exists by construction and was measured inert, the localization
stack did not manufacture a false positive. It did not cry wolf.

What it cannot show is whether the stack could find a structure that
*does* matter, because this checkpoint contains none to find. The honest
reading stops there.

**The sub-bin is the more consequential one.** The criteria split "not
flagged" in two, and this landed on the worse half. "Recovers and
correctly dismisses" would have meant the stack located a decodable
direction and correctly declined to call it load-bearing — a working
instrument showing restraint. What happened instead is that the stack
could not decode own-agent identity **at all**, at any probed layer, in a
model built with a designated slot for exactly that. Chance is 0.25 and
the best probe returned 0.275.

That is upstream-reportable, and it is reported: it weakens any reading
of Experiment 1's null that assumes the instruments would have found a
self-index had one been there. RT-12 named this as the single finding
that might outweigh the headline. It does not settle that question, but
it moves in that direction rather than away from it.

## The checkpoint, and why it is the strongest available case

The arm read the seed-0 full-architecture checkpoint. "Full" is the
register-bearing architecture; the twins are register-less. Its baseline
matches the registered lesion table exactly (T_sr 0.99, T_si 0.96,
T_sr_rev 0.84), which confirms identity without the arm ever having been
told where the register lives.

This is also the checkpoint that *binds* — one of only two in the five
that do. So the negative result is not an artifact of probing a model
with nothing going on. It is the most favourable case the register-
bearing set offers, and the stack still found nothing.

## Firewall, as registered

- Headline verdict committed 2026-08-19, before this arm existed.
- The pipeline never names any register internal; a self-check scans its
  own source against eleven forbidden names and refuses to run on a hit.
- Thresholds inherited, not chosen after seeing output.
- Both outcomes and the specificity-only limit committed before the run
  produced anything (`da0427f`, while the process was in flight).
- The three-standard-deviation bar is a **stated convention**, not a
  threshold inherited from Experiment 1, and was labelled as such in
  advance. The 0.25 is John's ruled Gate 0 band.

Worth stating plainly: a laxer bar would not have rescued this. The best
margin was 1.3 standard deviations, so the verdict is unchanged at two
standard deviations and unchanged at one and a half.

## What is still open

Sensitivity is untested and cannot be tested here. The companion positive
control on the A3 pilot checkpoint, where zeroing the acting channel is
measured load-bearing at 0.506 to 0.182, is written up at
`blind-arm-positive-control-proposal.md`. It is **unregistered, not run,
and awaiting John's separate ruling**. This result raises what is at
stake in that ruling: an instrument that finds nothing where nothing
matters is uninformative until it is also shown to find something where
something does.
