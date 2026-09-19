# Amendment A3 — revision proposal, before the registration commit

*2026-09-15. Status: **PROPOSAL. Nothing here is registered and nothing
here is decided.** Amendment A3 was ratified on 2026-09-15 (all fifteen
decisions yes) and the registration commit has not yet happened. Gates 0
and 1 have run, red-team pass 3 has run, and a shortcut sweep has run.
Between them they found things that change the amendment's text, and one
that changes its design. This document lists them as numbered yes/no
decisions, in the same idiom as the original's §7, so they can be taken
one at a time. Everything below cost **$0**; A3 cumulative spend is
**$0.00 of the $100 hard stop**, and no pod has ever been launched for
this amendment.*

---

## The headline, in plain terms

The design's central bet survives. What does not survive is the claim
that the objective, as built, forces the network to work out which agent
it is. Three drafts of the grammar have now been built and measured, and
**each one traded one flaw for another**. That is not three mistakes in a
row; it is a structural tension in the design that nobody had named, and
naming it is the main thing this document has to offer.

The tension is between three things the objective needs at once:

1. **A scoring cell in every episode.** Gate 0 measured what happens
   otherwise: the registered grammar's revision-conditioned battery
   harvests 19 items from 400 episodes, and its noise band is two items
   flipping.
2. **Revising must not mark the model out.** If the model revises in
   every episode while others do not, then how much an agent speaks
   predicts which agent the model is, and the cue gate fails.
3. **Agents that have already acted must not be eliminable.** If every
   agent revises exactly once, then anyone who has already revised is
   not the one revising now — so a solver that knows nothing about
   ownership can cross them off.

**Any two can be had. Not all three.** Here is what each of the three
drafts measured, all at $0:

| draft | who revises | cell density | ownership-blind ceiling | cue gates |
|---|---|---|---|---|
| 1 | the model, always, plus one other | every episode | 0.29 | **FAIL** — turn count predicts ownership perfectly |
| 2 | every agent, once | every episode | **0.52** — a solver crosses off whoever has revised | PASS |
| 3 (current code) | two agents drawn uniformly | half of episodes | 0.29, confirmed by sweep | **FAIL** — turn count, at 0.53 |

Draft 2 is the one Gate 1 certified this morning. It passed both cue
gates and its shortcut ceiling was reported as 0.29. The sweep found that
the true figure for a solver that knows nothing about ownership is
**0.52**, because when the model revises last — a quarter of episodes —
its own assignment is the only one left, and identifying it needs no
self-knowledge at all.

Draft 3 fixes that and the sweep now passes at 0.29. But agents who
revise take three turns and agents who do not take two, and the cue
detector samples one own turn against one other turn per episode. "Own"
is one agent; "other" pools three. So even though turn count is exactly
balanced across all turns (0.596 against 0.601), under that sampling it
is not (**0.499 against 0.591**), and both gates fail at 0.53 and 0.54.

**This is decision 1 below, and it is the one that matters.** I have not
drafted a fourth grammar, deliberately. Each of the three took a sensible
fix and paid for it somewhere else, the kill criterion K1 allows two
regenerations and one is now spent, and the next choice should be made
with the trade-off in front of you rather than by me guessing again.

---

## What was already found, and is not re-argued here

Gate 0 (`gate0-null-calibration-findings.md`) and Gate 1
(`gate1-curriculum-findings.md`) between them found five specification
problems; red-team pass 3 (`red-team-pass-3.md`) found thirteen more,
numbered RT-20 to RT-32, two of them fatal. The decisions below fold all
of that in. The pass also recorded what it found sound, which is worth
repeating: the no-stakes commitment and the floor-only, episodic claim
both survive attack; the exchangeability construction is correct; and
keeping the registered grammar and tokenizer byte-identical was right.

---

## Decisions

### 1. The grammar's structural trade-off — the one real design choice

Pick where to sit on the tension above. The options, with measured costs:

- **(a) Two revisers drawn uniformly (draft 3, current code).** Ceiling
  0.29, half the episodes yield a cell, and the cue gates fail at about
  0.53 on a turn-count asymmetry that exists only under the detector's
  one-per-group sampling. Fixing the detector rather than the grammar is
  arguable — the asymmetry is in how the gate samples, not in what the
  model can see — but that is a change to a registered instrument and
  should be argued explicitly, not assumed.
- **(b) Give the non-revisers a filler turn** so every agent takes three.
  Removes the turn-count asymmetry; reintroduces the elimination, because
  an agent that has taken its third turn is not the one acting now.
  Ceiling returns toward 0.52. **Not recommended.**
- **(c) Vary how many turns each agent takes, independently of whether it
  revises.** Then turn count carries no information about revising, and
  an agent that has already acted cannot be cleanly crossed off because
  the attacker does not know how many turns it will take. This is the
  option I would explore first, and it is untested — I did not want to
  spend a regeneration on an untested idea without your say.
- **(d) One reviser drawn uniformly.** Ceiling exactly 0.25, the cleanest
  number, but only a quarter of episodes yield a cell, so a 400-cell
  verdict needs 1,600 episodes at evaluation (free) and the action
  supervision during training is four times sparser (not free — it may
  need more tokens to learn, which is the pilot's whole question).

**Proposed: (c), with (d) as the fallback if (c) does not measure clean.**
Either way the sweep and both cue gates re-run before anything is
registered, at $0.

### 2. Adopt the measured ceilings, whatever the grammar turns out to be

The amendment pre-states a shortcut ceiling of 0.25 (§2.2). No draft has
had that. The ceiling must be **measured on the grammar that is actually
registered**, by the sweep, and written into the amendment as a measured
number with its method cited — not asserted. The current code reports
0.2921 for the primary battery and 0.3227 for the control, both in the
frozen battery record.

### 3. Correct the drop against the ceiling, not against chance (RT-21)

The registered metric divides each drop by the distance from baseline to
chance. The two verdict batteries have different shortcut ceilings, so
the largest drop each can show differs, and a lesion of a purely generic
who-did-what binder produces a spurious differential. On draft 2 that was
0.237 against a band of about 0.01 — the headline positive bin fires on
the boring explanation. On draft 3 it falls to 0.035, still above the
band. **Divide by the distance from baseline to the measured ceiling.**
$0, and it changes registered text.

### 4. State the revision frequency in the amendment (Gate 0)

Whatever decision 1 settles, §2.2 must say how often the model revises,
because that number is what sets the verdict cell count. The amendment is
currently silent and the registered grammar's silence is what produced a
19-item verdict cell.

### 5. Fix kill criterion K2's units (Gate 0)

K2 compares the primary battery "≤ lookup ceiling (0.25) plus the null
band". The ceiling is a raw accuracy; the band is chance-corrected. The
sum has no meaning. Restate in raw accuracy, converting the band
explicitly.

### 6. Say which checkpoints K0's band is read on (Gate 0)

K0 is met nowhere on its stated condition and exceeded on one checkpoint
of five on its proposed number — a run that never learned the battery,
where the metric's divisor is tiny. State that the band is read on
checkpoints whose verdict battery clears the floor margin.

### 7. Take the tensor cue gate's verdict over several samples (Gate 1)

Its interval resamples one draw's test split and is silent on spread
between draws. Six samples gave a spread of 0.0224 against a band
half-width of 0.05, so a clean grammar fails about one run in nine. Take
the verdict over several samples, or raise the episode count to about
14,000. **This also bears on decision 1**: draft 3's failure is at 0.53
and 0.54, which is outside that noise, so it is a real signal rather than
an unlucky draw — but the rule should be fixed before it is applied.

### 8. Register the shortcut sweep as a gate in its own right

RT-20's attack — read the model's own name, sitting three tokens from the
graded position, and match it — scored **1.000** on a grammar that had
just passed both cue gates. The cue gates could not have caught it: they
ask which turns are the model's own, which is a different question. A
sweep of ownership-blind attacks (`src/shortcut_sweep.py`) is now built
and should be a registered gate that any A3 grammar must pass before a
dollar is spent, with its own kill criterion. It is free and it has
already paid for itself twice.

### 9. Narrow the amendment's central claim (RT-20, RT-23)

§2.2 says the only route from the ceiling to full accuracy is to bind the
act to the item when acting and carry that binding forward. That is too
strong, and was simply false of two of the three drafts. The acting
channel marks positions, and attending back to marked positions is a
re-readable pointer rather than a carried binding. Both routes need the
channel, so the wire lesion cannot separate them; the re-indexing probe
already registered for the tag bin is what does. Say so.

### 10. Register the loss mixture (RT-27)

The trainer supervises the action and the query answers together, summed
with equal weight. The amendment does not state this, and the weight by
itself decides whether the starvation bin can fire. The reading
implemented is that no query anywhere asks about the model's own
commitments — which is satisfied, because the self-report battery is
gone — while the ownership-free and other-agent queries stay supervised.
Confirm or correct that reading, and register the weight.

### 11. Re-cost the ladder (RT-26)

The budget is costed on the registered 8-turn grammar. Measured on the
new one: more turns, more own turns per episode, and these runs are bound
by enactment rather than the GPU. The red team measured about 1.3 to 1.4
times per run, or roughly $14 against the cited $10 to $11. Three seeds
still fit the $100 stop; the optional extra seeds do not. **Re-cost from
a measurement on the grammar decision 1 settles, and state whether the
optional seeds are dropped.**

### 12. The remaining serious findings (RT-22, RT-24, RT-25)

Fold in, or rule against, the three the red team raised that are not
covered above: the outcome bins are neither exhaustive nor mutually
exclusive and have no bin for the validity check failing; the thresholds
are written as single numbers when Gate 0 measured them per battery
across a twenty-five-fold range, and no readability floor is registered
before the two paid seeds; and declaring the new likelihood attack
uncertifiable is a live outcome the procedure routes nowhere.

### 13. Record the three drafts in the amendment, not just in the notes

The registration commit should carry a short subsection saying that the
grammar took three drafts, what each traded away, and that the ceiling
reported by the second was wrong by a factor of nearly two until a sweep
was built to check it. A design that took three tries should say so where
the design is registered, not only in a findings note.

---

## What is not proposed

The ceiling, the $100 hard stop and the corrigibility commitments are
unchanged and not reopened. No new experiment is proposed. Nothing here
asks for more money; if anything, decision 11 may reduce what the ladder
can afford. The blind-localization arm remains untouched, as A3 left it.

## What happens after this

The order is unchanged: settle these, then the registration commit, then
Gate 2 — the pilot, on your authorization in your own words. Everything
from here to the registration commit is free. The first dollar is spent
on the pilot and not before.
