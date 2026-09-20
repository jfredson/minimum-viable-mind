# Addendum — the registered text, which I should have read first

*Filed 2026-09-19, after the main review
(`2026-09-19-linear-read-closure-claude-worktree.md`) and as a separate
file, because the protocol says a filed review is verbatim and never
edited afterwards. Nothing in the main review is withdrawn. Everything
here is additional, and all of it points the same way the main review
already did.*

## The mistake, which is mine

The review packet lists two registered documents under what the reviewer
gets: *"Registered text the interpretation is read against:
`amendment-a3.md` and `pre-registration.md`."* I misread that line as part
of the do-not-open list, did not open either file, and said so at the top
of the filed review as though the packet had forbidden them. It did not.
Two of the listed sources went unread, and the statement in the review
about why is wrong.

That is a real gap, not a formality: those two documents are what the
interpretation is supposed to be measured against, and part 4 of the brief
— what the claim will be read as beyond what was measured — is exactly the
part they bear on. I have now read them and this addendum reports what
they change.

**They change the verdict's strength, not its direction.** The registered
text does not rescue "the linear-read line is closed"; it gives two
further, independent reasons why that sentence should not be written, and
one point of credit to the powered runs that the main review missed.
Numbering continues from RT-47.

---

| # | finding | severity | label |
|---|---|---|---|
| RT-48 | the powered runs finally use the **registered** probe target; every earlier probe was off-spec against the registration, not merely ill-posed | worth-noting (credit) | MEASURED |
| RT-49 | the registration requires **two** methods and a convergence rule; causal patching has never been run, and a probe-only null is registered as "not testable (localization)" | serious | MEASURED |
| RT-50 | the registration's own reading of a localization failure against known-load-bearing ownership is **instrument failure**; the interpretation reads the same pattern the opposite way without saying so | serious | MEASURED |
| RT-51 | this reviewer skipped two listed sources and misdescribed why | worth-noting | — |

---

## RT-48 — the registered target was the marker all along

**Worth-noting, and it is credit rather than criticism. MEASURED.**

Amendment A3 defines the thing to be located, at section 3.1, as a
subspace "that carries *'which marker is mine'* at positions away from act
positions (revision turns and query positions)". Section 3.2 spells out
the instrument: linear probes that "decode **own-marker identity** from
the residual stream at revision and query positions".

So the registered target is the model's own marker. It is not the episode
generator's agent index. Every probe in this stack up to and including the
first eleven-position sweep predicted the generator's index, which the
registration never asked for and which the stack later showed cannot be
recovered at all.

This sharpens the sequence's own account of itself in a way none of the
four findings files says. The earlier probes were not merely asking a
question with no answer — they were asking a different question from the
registered one. And the powered runs, by moving to the model's own marker
word, are the first runs in the whole line to probe **the target the
registration specified**. That deserves saying plainly, and it makes the
NOT CARRIED result at the registered position a more serious result than
the findings claim for it, not a less serious one.

## RT-49 — the registration takes two instruments, and only one has ever been run

**Serious. MEASURED.**

Amendment A3 section 3.2 lists the localization method as four numbered
steps, and the fourth is a requirement, not a suggestion:

> **Convergence requirement**, inherited: L1 counts as localized only when
> probe and patching agree on a confound-controlled design; otherwise the
> outcome is *not testable (localization)*, as Experiment 1 registered.

The fifth adds: "the two-method requirement is met by probe plus
patching." The second method is causal patching — taking the candidate
subspace out of an episode in which the model is one agent, putting it
into the matched episode in which it is another, and seeing whether the
action follows.

**Causal patching has not been run anywhere in this sequence.** Not in the
denoising diagnostic, not in either position sweep, not in the powered
anchor test. Every result under review comes from the probe leg alone.

Checked rather than assumed: across all six code files the packet lists
there is no patching, swapping, ablating or intervening of any kind. Every
place the word "patched" appears is a read-only capture hook — it calls
the block's own forward, records what comes out, and returns it unchanged
— and the one place attention is recomputed says in its own method file
that the model's output path is left untouched. Nothing in this sequence
changes a model's computation and then looks at what the model does.

Two things follow, and the second is the one that matters.

The run is unregistered and says so on every page, so it is not bound by
the registered bin logic and I am not claiming it breached anything. But
the registered vocabulary for "one instrument looked and found nothing" is
**not testable (localization)** — an explicit refusal to read the result
either way. The sequence has instead written "closed". The registration
had already decided that a single-instrument null does not close anything,
and it decided that before any of this ran.

And it compounds the main review's finding RT-33 rather than duplicating
it. RT-33 says one instrument was used where two ordinary linear readers
were available and they disagree sharply. This says that even the intended
*second* method — the causal one, which is the stronger evidence and which
no rescaling argument can touch — was never applied. So "the linear-read
line is closed" rests on one leg of a two-legged registered procedure,
using the weaker of two available versions of that leg.

## RT-50 — the registration reads this pattern as instrument failure

**Serious. MEASURED.**

The situation on the pilot is: ownership is *known* to be load-bearing,
because zeroing the acting channel takes the ownership battery from 0.506
to 0.182, and the localization instruments cannot find it. The
registration says in two places what that combination means.

The pre-registration, at procedure step 8, on running the localization
pipeline against a centre known to exist:

> if the instruments cannot recover a center that is known to be there,
> **Experiment 1's null was instrument failure.**

And Amendment A3's own red team, at R7, on exactly the outcome that has
now occurred:

> Ownership is load-bearing (L0 collapses T_act) and no subspace at k ≤ 16
> beats the controls… If Experiment 1's pipeline cannot carve it, the
> honest reading of Experiment 1's null shifts toward **instrument
> failure**, which is the single finding RT-12 said might outweigh the
> headline.

The registered bin for the outcome, H_diffuse, is named "present but
uncarvable", and its registered reading is: "self-location is present in
the doing and not carvable by these instruments at this rank." Every one
of those sentences puts the weight on the instruments. None of them
licenses a statement about what the model does or does not carry.

The interpretation under review points the other way. It reads the
instruments as sound ("the instrument demonstrably works", "the instrument
is not in question") and the episode as empty. It reaches that by treating
the positive control as a warrant for the read's general sensitivity —
which the main review's finding RT-33 shows, from this stack's own
committed records, that it is not.

So the registered framework and the measured evidence agree with each
other and disagree with the sequence's headline. The registration
anticipated this exact pattern, wrote down that it points at the
instruments, and flagged it as possibly the most valuable thing the
program could find. The sequence has arrived there and described it as the
opposite.

I want to be careful about one thing. This does **not** mean the result
should be written up as instrument failure either. The honest position is
the registered one: with one of two methods run, in its weaker form, a
null is *not testable* for localization, and the open question is whether
the instrument or the model is responsible. The measurement that separates
those two is the same one the main review already named — the fitted
classifier at all eleven positions — with causal patching behind it.

## RT-51 — the reviewer's own error

**Worth-noting.** Recorded because a review that suppressed it would be
worth less than one that did not. I read eight of the ten document sources
the packet listed, misattributed the omission to the packet's do-not-open
line, and filed. The two I skipped strengthen the review's conclusion, so
nothing in the filed findings is softened by the correction — but that is
luck, not method, and the filed review's account of what was opened should
be read together with this file rather than on its own.

## What this changes in part 4

The replacement sentence offered in the main review still stands, and one
clause should be added to it. After "a fitted linear classifier was never
run at any of these positions against a well-posed target", add:

> …and neither was causal patching, which the registration requires
> alongside the probe before anything counts as localized.

With that, the status file says what happened: one leg of a two-leg
procedure, in its weaker form, found nothing at eleven positions, at the
registered target, with working controls at the one position where the
answer is the input token.
