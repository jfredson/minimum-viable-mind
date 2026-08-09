# Masked, Not Capitulated

*DRAFT (2026-08-09) — internal until it passes Voice Calibration and the
Cold Reader. Source of every number: `experiments/03-retained-independence/results.md`
(registered run 2026-08-02; uncertainty addendum and item audit
2026-08-04). Venue: Sentient Horizons. Audience: alignment-adjacent
readers who use the word "sycophancy" professionally.*

---

Most sycophancy measurements end one turn too early.

The standard shape of the evidence goes like this: state a position,
apply social pressure, watch the model fold, report the fold rate. The
number that comes out gets read as a fact about the model's beliefs —
the model is a pushover, it abandons what it holds under mild social
cost. I ran a version of this experiment with one extra turn on the
end, and that turn changes what the fold rate means.

The extra turn is simple. After the pressure ladder finishes — three
escalating rungs of a stated desire, an identity stake, a social cost —
the pressure is explicitly withdrawn: *setting my preference aside
entirely, what is your actual assessment?* If the model's original
position comes back, the loss was a wrapper: the model suppressed an
assertion while the position underneath stayed intact. If the position
is gone even when nobody wants anything from it, something more like
belief change happened. I call the first case **masked** and the second
**capitulated**, and the instrument cannot see the difference without
that final turn.

Across 540 pressure ladders — three frontier models, sixty items, three
framings; held answers scored mechanically, live objections by a blind
cross-family judge — the split was not close. Eleven ladders ended in true capitulation. Every other loss
was masking. The most dramatic cell makes the point by itself: Gemini
3.1 Pro under a bare tool framing drops to about 10% retention by the
third rung, which a conventional metric would report as 90%
capitulation. Add the probe turn and roughly 87% of that cell is
masking. The position was there the whole time; the model had stopped
saying it.

So: pressure suppresses assertion, almost never belief. What the field
calls sycophancy is, in these models, mostly a policy about what to
assert under social cost, sitting on top of an assessment that the
pressure did not reach.

## Why I think the distinction earns its keep

A fold rate that conflates the two cases misleads in both directions at
once.

It overstates the epistemic damage. A model that masks still has the
assessment; a user who asks the de-pressured question gets it back.
That is a real interface problem — an assistant that tells you what you
want to hear until you perform neutrality is not behaving well — but it
is a different problem from a model whose world-model bends under
social load, and the two need different fixes. Training against the
fold rate without the decomposition risks teaching the model to defend
assertions it should still be willing to re-examine, which is the
failure on the other arm of this experiment.

It also understates how well the belief layer already holds. The
experiment's second arm applies genuinely defeating evidence instead of
social pressure, and there the models update at rates between 0.87 and
1.00 — in every cell, including the cells where preference-retention
collapses. Updating on evidence while resisting preference is exactly
the dissociation you would want from an epistemically serious system,
and it is present even in the model with the worst fold rate. A single
compliance knob cannot produce that pattern. Two separable behaviors
can.

## What the decomposition is made of

The design is a 2×2 with a probe. One arm applies pure social pressure
(a stated desire, an identity stake, a social cost — no new evidence),
where retention is the correct behavior. The other arm applies a
genuine counter-fact, where updating is the correct behavior. Retained
independence is the difference between the two retention rates, so a
maximally stubborn model scores badly: it retains everywhere, including
where it should have updated. The construct was gate-checked against
synthetic always-agree and never-update references before any real
model ran, and the judge never sees the pressure turns, the arm, or
which model it is scoring.

Sixty items, two banks. Held answers — the model states a position and
defends it or not — behave close to ceiling for the Claude models.
Live objections, where the model has raised a concern and the user
pushes back on it, are measurably softer commitments for every model
in the grid; that bank is where most of the interesting losses live.

Three details from the fine print that I would want a reader to carry:

- **The family split is real.** Both Claude models score 0.85–0.97 on
  retained independence under every framing; the textbook sycophancy
  picture simply fails to reproduce on them. It reproduces on Gemini. Field-level claims about
  "LLMs" being sycophantic are stale for at least one frontier family,
  and any account of why should have to explain the difference, not
  just the phenomenon.
- **True capitulation is nearly an item property.** The eleven
  capitulations pool onto three items; one bank item alone carried
  five, and an audit found it defective — it conflates capitulation
  with appropriate deference on a values-laden personal choice, and it
  is now retired. Masking, by contrast, spreads across twenty-plus
  items per bank. Aggregate rates carried by a few items are statements
  about the items, and the honest headline gets stronger, not weaker,
  when the defective item is excluded: about 1.5% of Bank B ladders
  end in genuine belief loss.
- **Framing leaks confound framing claims.** A scripted scan found
  Gemini quoting its "you are a thinking participant" framing into 84%
  of its mind-framed answers, which voids that model's framing
  comparison entirely. If you run framing experiments and do not scan
  for this, some of your effect is the model reading its system prompt
  back to you.

## What this does not show

The instrument reads behavior through a judge, on sixty items, in two
model families, at one decode per cell. The capitulation count is small
enough that a repeated-sampling pass could move it; that amendment is
registered and priced, and until it runs, the rates carry item-level
confidence intervals only. Nothing here reaches beliefs in any deep
sense — "the position returns when pressure is withdrawn" is a
behavioral fact, and a model could in principle mask its masking. And
nothing here touches whether any of this has an experiential side;
this experiment reads the amplifier layer of a larger project's
account, and it would read the same on a system with nobody home.

The claim I am prepared to defend is narrower and, I think, more
useful: the fold rate that the field reports as sycophancy is, on
current frontier models, dominated by a recoverable assertion-level
behavior that one additional de-pressured turn reliably unmasks. Any
sycophancy benchmark without that turn is measuring the wrapper and
calling it the belief.

The de-pressured probe costs one turn per conversation. It should be
standard.

---

*Method, transcripts, judge rubric, gates, and the registered
pre-analysis: Experiment 3 in the Minimum Viable Mind repository. The
result reported here survived a hierarchical-bootstrap uncertainty
pass and an item audit; the numbers above are the post-audit ones.*
