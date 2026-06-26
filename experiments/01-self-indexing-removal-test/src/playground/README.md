# Dial console — interactive playground (Stage 1)

A qualitative tool for getting a *feel* for how each version of the model behaves
as you turn the self-structure dials up and down. You chat with the model while
steering a localized direction; it is the hands-on companion to the registered
removal test, not part of it.

## Non-evidential — read this first

This playground is **outside the registered measurement path** and must stay there.

- Nothing here is imported by the scoring scripts (`run_baseline.py`, `judge.py`,
  `battery.py`). Its only outputs are cached dial vectors in
  `artifacts/playground/` — never the `artifacts/stage1/` results the pre-reg reads.
- Impressions from turning these dials **must not** influence where `θ_task`,
  `θ_self`, or `δ` get set. Letting a qualitative "feel" leak into thresholds is
  exactly the researcher-degrees-of-freedom problem the pre-registration closes.
- The corpus rule applies to you, too: *discount anything mimicry fully explains.*
  A fluent first-person reply at high `alpha` is the easiest thing in the world to
  over-read. Treat it as a prompt for a registered test, never as a result.

## What the dials are

| Dial | Structure | Default layer |
|---|---|---|
| `index` | C_self-index — the thin "who is the current speaker" indexical (turn_role). Causally confirmed in `patch_context.py`. | L22 |
| `narrative` | C_self-narrative — the persona/identity structure (narrative contrast, `separate_self.py`). | L23 |
| `random` | Norm-matched random direction at the index layer — the "is anybody home" control. | L22 |

`alpha` is in units of the measured self/other projection gap at the dial's layer:
`alpha = +1` injects ~one gap of the structure, `0` is baseline, `-1` removes ~one
gap (the removal direction), `+2` amplifies. Steering is applied at **all
positions each decode step** — a stronger intervention than the validated
last-token patch, chosen for "feel", so these magnitudes do not map 1:1 onto
`patch_context`'s ~0.35 restoration number.

## The perplexity gate (so you don't fool yourself)

Every reply is shown with the perplexity of a fixed neutral passage under the
current dial setting. Flat perplexity as you move `alpha` = the steering is staying
on-distribution (a real behavioural change). A spike (the console flags `x>=1.5`)
= you are pushing the model off-distribution and breaking it; any "personality"
you see at that point is an artifact, not a self-structure. This is the same
neutral-corpus gate RT-07 specifies, reused live.

The **`/sweep`** command re-runs one prompt at `alpha = -2,-1,0,1,2` so you compare
removed vs baseline vs amplified on identical input — the controlled way to feel a
difference, rather than chasing a single drifting conversation.

### Self-specificity probe (the `self-spec d=` number)

Perplexity is now reported on **two** passages: the self-free `NEUTRAL_TEXT` and a
`SELF_RELEVANT_TEXT` in the model's own assistant voice (about being the current
speaker, tracking its own turn and prior outputs — the content C_self-index should
carry). Each is shown against its own `alpha=0` baseline, plus a delta
`d = (self ratio) - (neutral ratio)`.

A **positive d under removal** (negative alpha) means the dial degrades
self-relevant prediction *more* than neutral prediction — a hint the structure is
self-relevant rather than a generic LM axis. This is the RT-02 T-split intuition in
miniature. It is **a hint, not evidence**: it cannot separate "self" from the
deflationary turn-state/router reading (RT-05), and when the `OFF-DIST` flag fires
the model is breaking, so the delta there is unreliable. The adjudicating test is
the registered `T_syntax` control, not this tool.

## Run it (on the Mac — needs MPS + the model; will not run in the Linux sandbox)

```bash
cd ~/Documents/Code/minimum-viable-mind
source .venv/bin/activate
python experiments/01-self-indexing-removal-test/src/playground/play.py --smoke   # quick check
python experiments/01-self-indexing-removal-test/src/playground/play.py            # interactive
```

First launch fits the dials (one forward pass over the context stimuli) and caches
them; later launches are instant. Use `--refit` after changing a layer.

## Layout

- `steer_engine.py` — UI-agnostic engine (model + dials + steering hooks +
  perplexity + sweep). A web UI would wrap this same class.
- `play.py` — the CLI REPL.

## Status / next

v1: Stage-1 self-dials on the `gemma-2-2b-it` sandbox, CLI only. The engine takes a
generic `Dial` (direction, layer, method), so future levels (boundary, valence,
stakes, ontogenetic depth) plug in by adding entries to the dial registry, and a
slider web UI can wrap `SteerEngine` unchanged once the mini is in hand.
