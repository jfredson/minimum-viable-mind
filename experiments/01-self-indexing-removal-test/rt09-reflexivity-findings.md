# RT-09 first pass — reflexivity control results + a length confound (2026-07-12)

*Empirical companion to `pre-registration.md` §RT-09. Run on the pilot sandbox
(`google/gemma-2-2b-it`), per the registered materials committed 2026-07-01
(`7bb4355`) before any stimuli were run. Artifacts (gitignored):
`artifacts/stage1/{context_localize,separate_generic,patch_context}.json`.
Instruments: `gen_context_stimuli.py`, `localize_context.py`,
`separate_self.py` (extended this pass), `patch_context.py` (extended this
pass), `check_length_confound.py` (new, born from this pass).*

**Two findings, in tension, both stated as wagers below: (1) the pre-registered
generic verdict does NOT fire — C_self-index survives the generic-speaker
deflation on this pass; (2) a total length confound was found in three of the
four stimulus mechanisms, which keeps RT-09 open pending a length-matched
re-run and adds a new deflation candidate for the ledger (proposed RT-10).
Nothing here is adjudicated; the ledger merge and any amendment to registered
materials are John's.**

## 1. What ran

The full registered RT-09 pass, end to end, all on the 2b-it sandbox:

1. `gen_context_stimuli.py` — 192 stimuli, four mechanisms × 24/24 balanced,
   including the new `observed_speaker` set (third-party transcript inside a
   single user turn; responder vs asker slot set by turn structure).
2. `localize_context.py` — all four mechanisms pass the embedding-floor gate
   (margin +0.000) and show a computed signal: turn_role peak L24 (+0.56),
   attribution L15 (+0.57), narrative L22 (+0.57), **observed_speaker L10
   (+0.51)**. So the model does track speaker slots in dialogues it merely
   observes — C_speaker-generic is localizable and the reflexivity question is
   live.
3. `separate_self.py` (extended) — the RT-04 battery run on the
   (C_speaker-generic, C_self-index) pair; results in `separate_generic.json`.
4. `patch_context.py` (extended) — the cross-patch: d_generic (fitted on
   observed_speaker residuals) injected into the turn_role other-runs with the
   same set-the-coordinate semantics as C_self-index's own patch.

## 2. The pre-registered rule, conjunct by conjunct

The registered rule: C_self-index is *generic* iff cross-decode ≥ 0.9 AUC ∧
|cos| ≥ 0.5 ∧ cross-patch restoration ratio ≥ 0.5. Aggregation (committed in
code before results, since the pre-reg did not pin a layer): medians over the
band where both structures localize (own AUC ≥ 0.75); cross-patch ratio read at
C_self-index's peak causal layer.

| Conjunct | Threshold | Measured | Fires? |
|---|---|---|---|
| cross-decode gen→idx | ≥ 0.90 | **1.000** | yes — but length-inflated (§3) |
| direction \|cos\| | ≥ 0.50 | **0.224** | no |
| cross-patch ratio | ≥ 0.50 | **0.006** | no — decisively |

**The generic verdict does not fire.** The causal half is the striking one:
C_self-index restores 0.348 of the referent-dependent logit gap at L22 (random
control 0.003), while d_generic restores 0.002–0.038 at *every* layer — the
generic direction does not substitute causally at all. Geometrically the
reflexive residual survives: after projecting d_generic out of the turn_role
residuals, the index contrast still decodes at 1.0 across the band.

## 3. The length confound (found reconciling this pass; the reason RT-09 stays open)

Reconciling an instrument discrepancy (§5) exposed a confound the
embedding-floor gate cannot catch: the depth-matching filler exchange makes the
other/asker condition systematically **longer**, so label is predictable from
token count alone — perfectly, with non-overlapping ranges — in three of four
mechanisms (`check_length_confound.py`):

| mechanism | label-from-length CV acc | len(label=1) | len(label=0) | length-dir decodes contrast |
|---|---|---|---|---|
| turn_role | **1.000** | 23–28 | 33–38 | 1.00 (all layers) |
| narrative | **1.000** | 23–28 | 29–34 | 1.00 |
| observed_speaker | **1.000** | 37–42 | 45–51 | 1.00 |
| attribution | 0.396 (~chance) | 11–15 | 11–15 | ~0.51 |

A pure length direction cross-decodes turn_role at ~1.0 from layer 4 on, and
projecting length out of d_generic drops the saturated cross-decode from 1.00
to 0.64–0.91 depending on layer. Per the corpus rule — discount anything a
shallow mechanism fully explains — a length/position representation is exactly
the kind of nobody-home signal that must be screened before any of these
decodes count as referent structure.

**What the confound does and does not touch:**

- It **inflates** the cross-decode and (via the shared component) |cos| — i.e.
  it biased the geometry *toward* the generic verdict, which still did not
  fire. The "not generic" outcome is therefore conservative in the right
  direction.
- It **compromises the control's validity**: C_speaker-generic as localized may
  be substantially a length tracker rather than a slot tracker, in which case
  this pass did not really test slot-generality. RT-09 cannot be closed on this
  pass; it needs the length-matched re-run.
- It **re-opens a caveat on C_self-index itself** (and C_self-narrative): their
  own-contrast decodes ride the same confound. The causal patch is the
  evidence that survives: d_generic carries the same saturated length
  confound, and it restores ~0 while C_self-index restores 0.348 — so the
  causal effect is not borne by length alone. (Caveat: d_generic's length
  component was fitted on the 37–51-token range and applied on 23–38-token
  stimuli; a length representation need not transfer linearly across ranges.)
- **attribution is untouched** — the one length-clean mechanism, and it keeps a
  clean-floor computed signal (peak L15, margin +0.57). Its own caveat stands
  (the speaker noun appears upstream, so attention-copying is possible), but on
  the length axis it is now the strongest confound-free evidence that a
  context-set referent is computed at all.

## 4. Proposals for adjudication (nothing patched into registered docs)

1. **Proposed RT-10 (ledger entry): the length/depth deflation.** C_self-index
   as localized may be partially a context-length/position tracker. Controls:
   (a) **length-matched stimuli v2** — give the self/responder condition a
   filler exchange too, and/or vary filler length so the label↔length
   correlation is broken and the length distributions overlap across labels, in
   all turns-based mechanisms; (b) a **length-direction control in
   `patch_context.py`** alongside the random-direction control (patch the
   least-squares length direction with its own scale; C_self must beat it).
2. **RT-09 disposition for this pass:** report "generic verdict does not fire
   (provisional)" and hold the gate open until the rule is re-applied on
   length-matched stimuli. The decision rule itself needs no amendment — only
   the materials (stimulus generator).
3. **RT-04 note:** the narrative mechanism's length gap (29–34 vs 23–28) is the
   quantified version of the already-flagged instruction-length nuisance; the
   same v2 redesign covers it.

## 5. Instrument notes (recorded so the numbers are reproducible)

- **k-consistency fix in `separate_self.py`:** its held-out `cv_auc` sized the
  PCA from the training fold (k=9 at n=48) while `localize_context.py` sizes
  from the full n (k=12). The observed_speaker signal sits in components
  ~10–12, so the first pass showed gen_own ≈ 0.17–0.65 on activations that
  localize at 0.98 — two instruments contradicting each other on the same data.
  Fixed to the localize convention (k = `_probe(len(y))`). This is a
  consistency fix, not post-hoc tuning: k=12 was the pre-existing convention of
  the validated instrument. RT-04 numbers shift slightly under k=12 (median
  |cos| 0.28 → 0.23); the partially-separable verdict is unchanged.
- The pre-reg did not pin the layer aggregation for the RT-09 rule; medians
  over the both-localized band (mirroring the RT-04 ledger convention) were
  committed in code before results existed. If a different aggregation is
  preferred, re-reading the saved artifacts is enough — no re-run needed.

## 6. Wagers

- **Wager (RT-09, provisional):** under length-matched v2 stimuli,
  C_speaker-generic still localizes with a clean floor, and the rule still does
  not fire (|cos| stays < 0.5 and the cross-patch ratio stays < 0.5).
  **Loss:** if the re-run fires the rule, C_self-index is generic slot-tracking
  and no H_center claim attaches to it — "reflexivity not established," per the
  registered loss condition.
- **Wager (proposed RT-10):** under length-matched v2 stimuli, turn_role keeps
  a clean-floor computed signal and C_self-index keeps restoring well above
  both the random and the length-direction controls. **Loss:** if the turn_role
  signal collapses when length is matched, C_self-index as localized was a
  length tracker; the localization must be redone and the causal claim
  retracted to that extent.

## 7. v2 re-run (2026-07-12, same day, after adjudication) — both wagers won

Both proposals were adopted as-is (ledger Pass 4); the amendment was committed
(`b6eaf39`) before any v2 stimulus ran; the full chain then re-ran on the v2
materials. Artifacts overwritten in place (`artifacts/stage1/`).

**Length gate (the precondition):** passed. Label-from-token-count fell from
1.000 to ~chance in every turns-based mechanism (turn_role 0.522, narrative
0.520, observed_speaker 0.438); the pure length direction decodes turn_role and
observed_speaker at 0.50 everywhere. One residue, recorded: narrative retains a
mild length signal (length-direction AUC 0.56–0.57) — the short/long lead
crossing narrowed but did not perfectly null it. It is far below decision-rule
relevance, but narrative claims should carry the caveat.

**RT-10 — deflation defeated on both counts.**

- The turn_role signal survives length matching: embedding floor +0.000, peak
  L15, margin +0.55. (The v1 peak at L24 was partly length; the referent signal
  proper peaks mid-stack.)
- C_self-index's causal restoration is essentially unchanged (0.348 → 0.340 at
  L22) and beats the length-direction control 0.340 vs 0.012 (gap +0.328,
  convention ≥ 0.10). The causal effect was never length-mediated.

**RT-09 — the rule does not fire, now on a valid control.** C_speaker-generic
localizes length-clean (peak L19, margin +0.36 — more modest than the
length-inflated v1 number, as expected; own-AUC 0.75–0.86 in the band). The
conjuncts: cross-decode gen→idx **1.000** ✓ — and this time it is real shared
structure, not length; |cos| **0.148** ✗; cross-patch ratio **−0.005** ✗
(restore(generic) ≤ 0.014 at every layer). So: the turn_role contrast is
linearly separable along a generic-speaker direction (a shared decodable
component exists), but the two structures are nearly orthogonal and the generic
direction is **causally inert** on referent-dependent behaviour. C_self-index
is not generic speaker-slot tracking.

**Consequence (pre-registered partial-separation path):** because the shared
component is real (cross-decode fires) while the structures separate
geometrically and causally, the removal test targets the **residual** —
C_self-index with C_speaker-generic projected out — as primary. The residual is
well-defined and strong: turn_role still decodes at 1.0 after the projection
(idx⊥gen column).

**Side observation for RT-04:** on length-matched stimuli, index vs narrative
reaches *clean* separability at L6 (|cos| 0.017, both survive removing the
other, cross-decodes under threshold). Single layer, n≈24/side — supporting
evidence, not an upgraded verdict; the causal cross-patch (next action) stays
the decisive test.

**Scope:** all of this is the pilot sandbox (`gemma-2-2b-it`). RT-09 and RT-10
re-verify on the registered substrate (Llama-3.1-8B + Tülu ladder) before
`δ`/`θ` lock, like every other pilot gate.
