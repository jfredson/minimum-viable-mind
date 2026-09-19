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

> **ANNOTATION, 2026-09-16 (John's ruling).** *Superseded in
> interpretation by the unblinded register probe: no valid target.*
>
> The verdict above and its pre-stated sub-bin name stand exactly as
> committed. John ruled the name is **not retired**: "The committed
> verdict and its pre-stated name stand as written. Add a dated
> annotation beside it ... Annotate, never rewrite."
>
> What the annotation records is that the *interpretation* has been
> superseded, not the verdict. The unblinded probe of the register at its
> known location found no own-agent identity at any turn, so there was
> nothing at this location for the blind stack to locate. "Failure to
> locate" remains the correct name of the bin the result fell into under
> the criteria as committed. It is no longer the correct description of
> what happened. See `register-direct-probe-findings.md`.

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

*Amended 2026-09-16 on John's ruling. The original wording of this
section claimed more than the numbers carry, in two places. Both are
corrected here rather than quietly rewritten, and what was originally
written is stated so the correction is checkable.*

**The specificity reading is weak, and weaker than first written.** The
criteria committed before the run said this result would support
specificity only and never sensitivity. That still holds and is still the
ceiling. But John ruled that even the specificity half is thin:

  "'not flagged' from probes at chance on every layer is weak evidence of
  specificity, since an instrument that locates nothing cannot cry wolf."

That is right, and the original draft of this section said the stack "did
not manufacture a false positive. It did not cry wolf." **That sentence is
withdrawn.** Crying wolf requires having found something to raise an alarm
about. An instrument returning chance at every layer never reached the
point where it could have flagged wrongly, so declining to flag is not
restraint and is barely evidence of anything. The honest statement is
narrower: **no false positive was produced, by an instrument that produced
no positive of any kind.**

What the result cannot show is whether the stack could find a structure
that *does* matter, because this checkpoint contains none to find. That
limit was committed before the number was seen and is unchanged.

**The sub-bin name stands.** The criteria split "not flagged" in two
before the run, and this landed on the worse half: **instrument failure to
locate**. "Recovers and correctly dismisses" would have meant the stack
located a decodable direction and correctly declined to call it
load-bearing. What happened instead is that the stack could not decode
own-agent identity **at all**, at any probed layer, in a model built with
a designated slot for exactly that. Chance is 0.25 and the best probe
returned 0.275.

## What this says about Experiment 1, correctly scoped

*Also amended 2026-09-16 on John's ruling.* The original draft said this
result "weakens any reading of Experiment 1's null that assumes the
instruments would have found a self-index had one been there", and that it
"moves in that direction rather than away from it". **That inference was
too broad and is withdrawn.** John's ruling:

  "that stack located a real structure (the router) on 2B and 8B models.
  This result says the stack is unvalidated at 30M; it does not by itself
  show Experiment 1's null was instrument blindness."

The record supports him. Experiment 1 did not come back empty-handed. Its
pipeline **found** a load-bearing structure and characterised it: the
registered reading is that the locatable residual is dialogue-state
routing infrastructure rather than the floor's self-binding. The router
control fired on its own pre-registered terms, and the ablations moved the
batteries by 0.219, 0.100 and 0.133. An instrument that locates a real
structure and correctly declines to call it a center is working, not
blind.

The scales are also nowhere near each other. Experiment 1 ran on a 2
billion parameter pilot substrate and a registered 8 billion parameter
run. This arm ran at 30 million, roughly two orders of magnitude smaller
and a different architecture besides.

So the correct scope is narrow: **the localization stack is unvalidated at
30M.** That is a real and reportable limitation of the A2 and A3 work,
which is where it applies. It is not evidence that Experiment 1's null was
an artifact of blind instruments, and this record should not be cited for
that claim. RT-12 named instrument blindness as the single finding that
might outweigh the headline; this result does not deliver it, and saying
otherwise would be reading a null at one scale as a verdict on a positive
result at another.

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

## What is still open, and what John ruled on 2026-09-16

Sensitivity is untested and cannot be tested on this checkpoint. Two
follow-ups were ruled, both local and free, both after this verdict was
committed:

1. **An unblinded probe of the register at its known location**, on this
   same checkpoint, for the same four-agent target with the same null and
   the same 3 sd bar. This separates two readings the blind arm cannot
   separate: a register that *holds* decodable own-agent identity the
   blind stack walked past, versus a register that is simply **empty**, in
   which case the arm had no valid target and "failure to locate" is the
   wrong description of what happened. Criteria pre-stated and committed
   before output, as with the blind arm. See
   `register-direct-probe-findings.md`.
2. **The companion positive control**, ruled **YES**: the same blind
   pipeline on the A3 pilot checkpoint, where zeroing the acting channel
   is measured load-bearing at 0.506 to 0.182. It stays **unregistered**
   and labelled so, under the same firewall, with criteria committed
   before output. See `blind-arm-positive-control-proposal.md` and its
   findings.

The order matters and was John's: the unblinded probe runs first, because
if the register turns out to be empty then this arm's "failure to locate"
was never a failure of the instrument at all.
