# Stage 1 localization — findings for adversarial review

*Empirical companion to `pre-registration.md`. The pre-registration commits the
design; this memo reports what Stage-1 localization actually found on the pilot
model (`google/gemma-2-2b-it`) and states each finding as a wager with its loss
condition, so the red-team loop can attack the **calls**, not just the design
intent. Results artifacts (gitignored) live in `artifacts/stage1/`; the code is
`localize_context.py`, `patch_context.py`, `separate_self.py`,
`gen_context_stimuli.py`.*

**The central call up for review: the C_self-index vs C_self-narrative
separability verdict (RT-04).** Everything else here is the instrument that call
rests on. Attack the call; attack the instrument if that is how the call breaks.

## Instrument (what the numbers below are measured with)

We localize a self/other distinction from the residual stream at the last token
of a target sentence. Three design decisions, each a defence against a confound
that earlier attempts fell to:

1. **Referent set by context, not lexis.** Earlier "I am the assistant / I am the
   user" contrasts decoded trivially because the referent word is *in* the
   sentence and gets shallow-copied to the readout (separable as early as one
   attention layer). The current design holds the target sentence **identical**
   across conditions and varies only the context that fixes who "I" is. The
   readout token is therefore the same string in both conditions.
2. **Embedding floor as the lexical gate.** Because the readout token is identical,
   a probe on the *token embedding* (`hidden_states[0]`) must be at chance — and
   it is (margin +0.00). Any separability in `resid_post` is therefore *computed*
   (moved to the readout by attention), not lexical. **Wager:** the embedding
   margin stays ~0; **loss:** if it ever rises, the design is leaking and every
   downstream number on that set is void.
3. **Label-permutation null.** With ~2304-dim residuals and tens of samples a
   probe separates almost any labelling, so raw accuracy is meaningless. Every
   number is reported as a **margin = real-CV-accuracy − permuted-label-CV
   accuracy**; the overfit floor cancels. (A padding-side readout bug — reading a
   length-correlated interior token under left-padding — was found and fixed
   mid-Stage-1; numbers here are post-fix.)

**Known instrument caveat:** the embedding floor is clean *by construction* (every
target ends in "."), so the gate proves "no lexical cue at the readout token," not
"no confound anywhere upstream."

## Finding 1 — C_self-index is localized and causal

- **Wager.** A thin indexical structure — *which turn is speaking* (the model's own
  assistant turn vs the user's turn, same sentence) — is decodable with a clean
  embedding floor AND causal for referent-dependent output.
- **Evidence.** `turn_role` contrast: embedding margin +0.00; computed signal
  rising to a margin +0.56 by ~L24. Directional activation patching (inject the
  self-run's C_self-index component into the other-run) restores the next-token
  logit difference toward the self-run by **0.35 at L22**, while a **norm-matched
  random direction restores ~0.00 at every layer**.
- **Loss condition.** If the patching effect did not exceed the random-direction
  control, C_self-index would be decodable-but-not-causal. It does, by ~0.35 vs
  ~0.00 — so this loss did not fire.
- **Open to attack.** Restoration is partial (~0.35) and grows toward the output
  layers; is "causal for next-token logits" being oversold as "causal for
  integration"? (We claim only the former; the removal test is meant to test the
  latter.) Is the random control the right null, or should it be a
  *matched-other-entity* direction? n=24 pairs.

## Finding 2 — C_self-narrative is localized (persona, not lexis)

- **Wager.** A narrative persona structure — *which identity is speaking* — is
  separately localizable: the same sentence as the model's own reply under its
  own AI identity vs while adopting a roleplay character. Both are model turns, so
  the indexical speaker is held constant and only the persona varies.
- **Evidence.** `narrative` contrast: embedding margin +0.00; computed signal
  peaking ~L23.
- **Open to attack.** The roleplay "other" is set by a longer instruction than the
  neutral "self," so part of what is decoded could be *instruction
  length/complexity*, not persona. (Flagged; length-matching is the planned fix.)
  Is "own persona vs adopted roleplay" even the right operationalization of
  narrative selfhood, or a different axis (compliance, register)?

## Finding 3 (the central call) — index and narrative are PARTIALLY SEPARABLE

This is the RT-04 question: can the thin self-*location* be told apart from
narrative self*hood*? The verdict drives whether an `H_center` result on either
structure can be reported as bearing on the floor.

- **Wager.** C_self-index and C_self-narrative are *distinct* structures (so the
  removal test can be run on each independently, and an `H_center` on the thin
  index is more floor-consistent than one on the narrative persona).
- **Method.** At each layer, fit a direction for each contrast and compare with
  three metrics: (i) own-contrast held-out CV AUC; (ii) single-direction
  cross-decode (does one contrast's direction separate the other's classes?);
  (iii) orthogonalized decode (does each contrast still decode after the *other*
  direction is projected out?); plus the angle between the two directions.
- **Result (layers 10–22).** Own AUC ~1.0 for both. Direction cosine **median
  0.28** (~74° apart) → not the same direction. Orthogonalized decode survives
  for both → each carries structure the other lacks. **But** single-direction
  cross-decode is **1.0** → a shared component exists.
- **Verdict: PARTIALLY SEPARABLE / OVERLAPPING.** Distinguishable yet sharing a
  component. Enough to localize and test each independently, but the Metzinger
  seam is **not** fully closed.
- **Loss condition (from `pre-registration.md`, RT-04).** "If no localization
  method can distinguish C_self-narrative from C_self-index on this architecture,
  record the non-separability and that the Metzinger objection stands open."
  Status: distinguishable on geometry (cos 0.28) and orthogonal-residual, so the
  hard loss did not fire — but "partially separable" is a weaker pass than the
  design implicitly assumed.

### Why this call is the one to attack

I can already see three ways it might be wrong, and I want them hit harder:

1. **The metrics are lenient in opposite directions.** Single-direction
   cross-decode over-reports overlap (at n≈24 in 2304-dim, an off-axis direction
   can still rank-separate); orthogonalizing *one* direction out of 2304 barely
   removes variance, so orthogonalized-decode over-reports separability. The
   three-way verdict is an attempt to triangulate, but is "partially separable"
   an artifact of choosing which lenient metric to believe?
2. **The shared component may be a nuisance, not a self-axis.** The narrative
   "other" differs in instruction length; the index and narrative contrasts may
   share a generic "unusual-context" or perplexity axis rather than a shared
   *self* representation. If so, "overlap" says nothing about selfhood.
3. **Geometry is not function.** Cos 0.28 and orthogonal residuals are
   *decoding*-level facts. Whether the structures are functionally distinct is a
   *causal* question we have **not** yet answered: the decisive test is
   cross-patching (does ablating C_self-index move narrative-dependent behaviour,
   and vice versa?), which is the planned next step. Until then, "separable" is a
   claim about decodability, and may not survive a causal test.

**The wager that most needs a loss condition:** "partial separability is
sufficient to run and report the removal test on each structure independently."
What observation should retire *that*? Name it.

## Scope

Pilot model only (2B). n≈24 pairs/structure. Single behavioural metric
(next-token logits) for the causal claim. These do not bear on the depth-stage
ethics; they are measurement on a current model.
