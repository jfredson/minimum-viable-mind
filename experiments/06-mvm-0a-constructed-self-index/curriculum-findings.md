# Curriculum build + cue-detector gate — findings (2026-08-04)

*Pre-training work for MVM-0a draft v0.3. Built before the
pre-registration is final, deliberately: the RT-08 cue-detector gate can
fail the whole design before a scale is chosen or a training run is
funded, so it is the cheapest thing to learn first. **No model was
trained and nothing here is a registered result.***

## Headline: the anti-router curriculum is buildable — run (i) passes

The design's central structural claim over Experiment 1 is that *no
surface cue predicts which commitments are the model's own*, so
dialogue-state routing cannot solve the binding task and the confound
that voided Experiment 1 is excluded at the data level. That claim is now
measured rather than asserted, on curriculum text:

| | AUC | 95% CI | verdict |
|---|---|---|---|
| clean curriculum | 0.5008 | [0.4773, 0.5242] | inside the [0.45, 0.55] equivalence bound ✅ |
| planted-leak control | 0.8627 | [0.8482, 0.8768] | ≥ 0.70 floor, detector has power ✅ |

**GATE: PASS** (`cue_detector_gate.json`). Detector: char n-gram TF-IDF
(1–3) plus explicit positional features — turn index, relative position,
length, speaks-first, speaks-last, per-agent turn count, marker identity —
logistic, capacity and n pre-committed, 8,000 balanced examples,
2,000-draw bootstrap CI.

Two runs remain and are stubbed with explicit `NotImplementedError`
rather than silently skipped: **(ii)** the same detector over the exact
input tensors (turn-type embeddings, segment ids, loss-mask-correlated
padding), which needs the tokenizer/collator, and **(iii)** the
post-training self-vs-generated fingerprint detector over the model's own
rollouts, which needs a trained model. A pass on (i) alone is not the
gate passing.

## The gate earned its keep immediately: it caught a real leak

The first full run **failed at AUC 0.722**. Diagnosis produced two
distinct problems, and separating them mattered.

**A sampler artifact (mine, not the data's).** An earlier
`build_examples` took the *first* own turn and the *first* other turn per
episode. With N agents the episode's first turn belongs to another agent
with probability 1−1/N, so the construction manufactured a position
asymmetry: mean turn index 1.53 for own versus 0.24 for other. Fixed by
drawing both turns uniformly. This is recorded in the code because it is
the standing hazard of this gate — *it tests whatever you hand it*, and a
FAIL is a hypothesis about the data, not a verdict on it.

**A genuine curriculum leak, from two red-team patches interacting.**
After the sampler fix the gate still failed. The cause: the forced-
revision mechanism added for **RT-11** (a commitment the agent later
contradicts, so a coherence-clustering solver fails where an ownership
tracker succeeds) appended the revision as the **final turn** and
**always by the model's own slot**. That plants exactly the positional
ownership cue **RT-02** forbids — "speaks last" went from 0.132/0.121
(own/other, no revisions) to 0.183/0.088 with revisions at 25%.

Two individually-correct patches combined into a confound. Fixed by
making revision agent- and position-neutral: the revising agent is drawn
uniformly over *all* agents, and the revision occupies that agent's own
later turn in the existing order, so no position and no revision-presence
is self-specific. The self-test now asserts that both self-revision and
other-revision occur.

This is the argument for building the gate before the model, made
concrete. Neither leak would have been visible in a trained system's
results; both would have produced a clean-looking H_load-bearing.

## What was built

- **`src/curriculum.py`** — episode grammar and battery generators.
  Multi-agent dialogues, surface-identical roles, per-episode marker pool
  drawn without replacement, speaking order re-shuffled each round, model
  slot redrawn per episode, one fixed rendering template (the
  canonicalizer), ownership crossed with content via paired episodes that
  share a content seed and rotate the owner. `fill_own_turns` is the
  on-policy hook: at training time the model's own turns are filled by its
  own sampled outputs and canonicalized, so ownership is grounded in
  causal authorship rather than a label, a fingerprint, or a fixed index
  [RT-02].
- **`src/cue_detector.py`** — the gate above, with equivalence bound,
  positive control, and pre-committed capacity.
- **`batteries/`** — frozen items [RT-14]: 200 each for T_sr, T_si,
  T_state, T_syntax from seed 20260804, with chance floors recorded
  (0.125 / 0.125 / 0.042 / 0.100) for the chance-corrected `d` metric.

## What this does *not* establish

The curriculum is *generatable* without a surface ownership cue. Whether
a model of any affordable scale can **learn** the binding task from it is
untested and is a separate registered loss condition — if it cannot, the
honest report is that the task is unlearnable at this scale, not that
self-indexing is absent. Likewise, run (i) passing says nothing about the
tensor-level and fingerprint-level cues that runs (ii) and (iii) exist to
catch; the fingerprint one in particular cannot be checked until a model
exists, and it is the route RT-02 flags as most likely to survive.

## Open decisions this work touches

The generator currently defaults to N = 4 agents and 8 turns. N sets the
chance floor in the corrected `d` metric and is one of John's open calls;
changing it re-freezes the batteries and re-runs the gate, both cheap.

*(Resolved 2026-08-07: John adjudicated N = 4 / 8 turns as the registered
values — pre-registration v0.4 §Materials.)*

## Addendum (2026-08-07): gate run (ii) — input tensors — PASSES

With the architecture values adjudicated (N marker-keyed registers, no
persistent index), the tensor layout became definable, so run (ii) was
built and run the same day. `src/encoding.py` is the data interface the
training step will consume: closed word-level vocab (103 tokens), per-token
turn ids, answer-only loss mask, right-padding, and the **register key
stack ordered by marker vocab id** — markers are a uniform per-episode
draw, so the model's own register lands at a uniformly random stack index
(measured: 0.263/0.246/0.249/0.242 over 4,000 episodes; self-test asserts
±0.03 of uniform).

**Result (pre-committed params: n = 4000 episodes, seed 20260804, same
equivalence bound and classifier family as run (i)):** clean tensors AUC
**0.5133 [0.4898, 0.5366]** — inside [0.45, 0.55], PASS. Positive control
**1.0000**: the planted leak is the *canonical-reindex bug* — stacking the
model's own register at index 0, the convenient implementation choice that
would smuggle an identity channel in as a tensor layout [RT-01/RT-02].
Perfect separability is expected there (`reg == 0` identifies own turns by
construction); the point of planting it is that the detector demonstrably
sees the register stack, so its clean verdict on the honest layout has
standing.

Features the detector saw, per RT-08's named channels: register-stack row
and key id, token spans and relative position, turn ids, loss-mask
overlap, distance-to-padding, and raw token ids. Run (i) re-run unchanged
(0.5008 [0.477, 0.524], PASS); combined gate record in
`cue_detector_gate.json` now carries both runs. **Run (iii) —
post-training fingerprint on the model's own rollouts — remains stubbed
`NotImplementedError` and is the cue RT-02 flags as most likely to
survive; it cannot exist until a model does.**
