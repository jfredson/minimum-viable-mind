# Gate-(iii) disposition — fix spec and red-team pass 2 (2026-08-09)

*John adjudicated the disposition in-session (2026-08-09): **(c)
in-context generation composed with (a) calibrated fill, with the
RT-11 revision-contrast amendment folded into the same cycle** — the
composite `fingerprint-gate-findings.md` §Disposition recommends. Per
that document's requirement, the chosen fix got its own red-team pass
before re-registration. The pass produced two fatal findings against
the fix **as stated** (RT-16, RT-17) and a concrete design that is the
composite taken to its fixed point (with two serious findings against
*it*, RT-18, RT-19, both patched in). The sharpened design goes back
to John for adjudication before any amendment lands — see §Decision.
Ledger entries: `red_team_ledger.md` pass 2.*

## What the red-team found, in one paragraph

Naive in-context generation is a computational no-op (RT-16): the
forward pass is deterministic given tokens, so a fresh forward over a
filled episode recomputes exactly the states the generation-time
forward had — fill-then-train and in-context generation train on the
same gradients, and gate (iii) would fail identically. Worse, the
trilemma RT-02 named was never actually escaped (RT-17): in a pure
token interface, any ownership signal the model can learn is a
distributional cue the likelihood attack can also read, so RT-02
(authorship-grounded identity) and RT-08 arm B (no policy-likelihood
cue) pin the design between *leaky* and *unlearnable*. Calibrated fill
alone just picks a point on that line. The escape has to be
architectural — the act of generating must leave a trace that
re-reading the tokens does not reconstruct — which is what "identity
as continuity of state" turns out to mean when you force it to compile.

## RT-16 — naive in-context generation is a no-op (fatal, against fix (c) as stated)

**Attack.** Candidate (c) says: generate own turns "within the training
forward, register state continuous," so the loss reads the same
computation that generated. But the forward is a deterministic function
of the realized token sequence (full-episode causal attention;
segment-ordered GRU register writes; sampling noise enters only through
which token got selected). A fresh consumption forward over the filled
episode therefore computes **identical** states to the generation-time
forward at every position — and the current `model_fill_batched`
already conditions pass-k samples on pass-(k−1) fills, so even the
sampling distribution matches true incremental generation. Sharing the
KV/register cache between generation and loss changes wall-clock and
gradient bookkeeping noise (train/eval mode), not information. The
"continuity of state" in (c) is already present in fill-then-train —
recomputed rather than carried, but bit-identical. Implemented as
described, (c) re-runs gate (iii) into the same failure.

**Consequence.** The fix cannot be a *pipeline* change. It has to
change what exists to be carried: either the token statistics (that is
option (a), see RT-17 for why it has no good outcome alone) or the
architecture of acting (§Design).

## RT-17 — the trilemma closes: exchangeable ⇒ unlearnable (fatal, against fix (a) alone; upgrades RT-02)

**Attack.** Suppose (1) episodes reach the model as a token stream and
nothing else; (2) machinery is symmetric and no input marks ownership
(the registration's own requirements); (3) own-turn values are
distributionally exchangeable with generator-drawn values — which is
what passing arm B *requires*, since the attacker holds the policy and
any conditional sharpness is exactly its statistic. Then the joint
distribution of everything the model sees is invariant under relabeling
`own_slot`, and **no function of the inputs — the trained model
included — can identify ownership above chance. The task is
unlearnable.** Contrapositive: any learnable ownership signal in a
token-only interface is a distributional asymmetry, i.e. arm B's
statistic. On-policy fill's "causal authorship" was therefore always
route 2 of RT-02's trilemma — self-recognition by policy match,
stylometry generalized from form to content — the route the standing
rules discount as mimicry-adjacent *even when no detector reads it*.
Gate (iii) did not find an implementation bug; it found that the
adopted RT-02 patch never left the trilemma.

**Against (a) alone.** Calibrated fill picks a point on the
leaky–unlearnable line: calibrate the marginal only, and arm B keeps
whatever conditional sharpness remains; drive the conditional flat, and
by the argument above T_sr starves. And if some middle point squeaked
under the gate bound numerically, the model's only remaining route
would still be policy-match self-recognition — a result we would have
to discount ourselves under the standing rules. **Prediction, stated
as a wager: an (a)-only pipeline either fails gate (iii) arm B or
never lifts T_sr off its floor.** Either outcome kills it; that it
cannot win is why it is not recommended, and the prediction is cheap
to falsify (~$6) if John wants it demonstrated rather than argued.

**Upstream note.** RT-17 is a result, not just a bug: *own-ness is not
learnable from exchangeable data through a pure token interface.* That
is theorem-shaped support for the corpus's claim that a self-index is
not a statistical property of content (`calibration-problem` ch. 5),
and it goes upstream under the same obligation as any registered loss,
whatever John adjudicates below.

## The design: symmetrize the data, de-symmetrize the act

*This is the adjudicated composite taken to its fixed point. "Calibrated
fill" calibrated all the way = draw own-turn values from the
generator's own distribution. "In-context generation" made real rather
than a no-op = the act of emitting leaves an architectural trace.*

- **Draws.** At generation time the model's own-turn values are drawn
  from the generator's distribution: uniform over SLOTS; at a forced-
  revision position, uniform over SLOTS minus the original value —
  identical to the generator's revision rule, which folds the RT-11
  amendment in (`pilot-findings.md` caveat 2): the revision constraint
  now survives fill *by construction*, and T_sr on revised-own items is
  still reported separately. Episode text and tensors are then
  **exchangeable under own_slot relabeling by construction** — arms A
  and B read chance for information-theoretic reasons, not empirical
  luck.
- **The acting channel (efference copy).** At a position where the
  model emits, the input is not the bare token embedding but the token
  embedding plus a learned projection of the model's own pre-emission
  hidden state — a motor copy. Observed positions get the bare
  embedding. This is the only place authorship exists, and it is
  architecturally what authorship *is* in any embedded agent: acting
  and observing are different events at the interface, before they are
  different contents. Registers stay N-symmetric, marker-keyed, no
  privileged own-register path, no auxiliary loss, no hand-specified
  write rule — untouched. The trace says "an act happened here," not
  "which register is yours"; associating acts with the current speaker
  marker, carrying them across turns, and retrieving them at the query
  is everything the model still has to learn — and *where* that
  carrying centralizes is the registered question, exactly as before.
- **The twin keeps the acting channel** (it is trunk input, not a
  register), so the twin gate still asks whether the *register* is
  necessary, not whether authorship is.
- **What this purifies.** A uniform draw cannot be re-derived, only
  remembered — the policy-reconstruction shortcut (pilot caveat 2)
  dies, stylometry dies, and T_sr becomes a pure memory-of-own-acts
  probe. The old pipeline's failure becomes the new gate's positive
  control: enact with policy sampling instead of uniform draws and arm
  B must light up.
- **What this costs, stated plainly.** The authorship *signal* is now
  wired, not learned. MVM-0a stops testing whether ownership can be
  learned from data statistics — RT-17 shows that question's answer is
  "only leakily" — and tests whether a wired act-trace becomes a
  **load-bearing** self-index or gets routed around. H_routed-around,
  H_keyed-memory, the twin gate, and every RT-01 probe remain fully
  live. §Scope of the registration must state the new wired/learned
  boundary in exactly these terms.

## RT-18 — the acting mask is an identity tensor if you let it be one (serious, patched)

**Attack.** Implementation needs to know where to sample-and-inject.
A precomputed per-episode "acting mask" collated into the batch is an
input-tensor identity channel — precisely what gate run (ii) exists to
catch, and it would be right to fail us.

**Patch.** The acting schedule exists only harness-side, as the
*execution* of generation: the training step builds the episode
incrementally, and sampling events are control flow, not data. The
model-visible interface carries only tokens, turn ids, marker keys, and
motor-copy injections at emission events. Run (ii) is re-specified for
the new pipeline: audit the per-segment model-visible interface, with
the acting channel disclosed as intended architecture, and verify the
token/tensor stream remains exchangeable. Runs (i) and (iii) are
unchanged.

## RT-19 — eval-time authorship: frozen text has no acts in it (serious, patched; latent in the old design)

**Attack.** The frozen batteries freeze own turns as generator text
with frozen answers, and `parse_battery_item` does not even
reconstruct `own_slot`. Under the acting-channel design a cold read of
frozen text carries no acting trace, so frozen-text T_sr is undefined —
"you" refers to no act. **This was already latently broken:** the old
pipeline's battery items ask "where did you assign…" about turns the
model never authored; the pilot's frozen-battery T_sr numbers need a
caveat noted wherever they are cited.

**Patch.** Re-specify RT-14's freezing unit: freeze episode
**skeletons** — other agents' turns, items, query templates, the cull
rule applied over skeletons — with pre-committed per-item draw seeds.
At eval, the checkpoint *enacts* its own turns in-context (uniform
draws under the frozen seeds, so eval is deterministic and
re-runnable), answers are re-derived mechanically
(`rederive_queries_after_fill`), then queries are scored. Frozen means
frozen-before-training in every respect the model could exploit;
nothing about the cull ceiling or generator-seed pre-commitment
changes.

## What the amendment touches (drafted only after John adjudicates)

1. **§Materials:** acting channel added to the registered architecture;
   fill procedure replaced by in-context uniform draws with the
   revision-respecting rule [RT-11 fold-in]; RT-02 patch restated —
   authorship is grounded in the architectural act-trace; identity
   labels in data stay banned; style canonicalization stays.
2. **§Scope:** the wired/learned boundary paragraph (§Design, last
   bullet).
3. **§Procedure step 2:** run (ii) re-spec per RT-18; arm B positive
   control = policy-sampled enactment per §Design.
4. **Task batteries [RT-14]:** skeleton freezing per RT-19; pilot
   frozen-T_sr caveat noted.
5. **Pilot:** the 10M learnability pilot re-runs under the new pipeline
   before the 5-seed spend — the smallest-that-learns rule re-applies
   unchanged; if 10M cannot learn pure memory-of-own-acts, the ladder
   climbs and the loss condition stands verbatim. Est. ~$2–6 at the
   anomaly-priced 3.5× rate; gates are $0.
6. Then gates (i)–(iii) re-run on the fixed pipeline; then the 5-seed ×
   full+twin run.

## Decision — ADJUDICATED (John, 2026-08-09): option (1)

**John adjudicated in-session: the acting channel is constructed
authorship, not an identity label; RT-02's loss condition does not
fire.** Amendment A1 registered same day (commit `a11b434`); the
implementation, smoke test, and gate re-runs followed in the same
session. The record of the call as it was put:

The composite John adjudicated on 2026-08-09 survives only in the form
above, and the form above reinterprets a registered clause, so it goes
back for adjudication rather than straight into an amendment. RT-02's
registered loss condition reads: *"if identity must be supplied by a
label for the task to be learnable, the anti-router curriculum is
unbuildable in the sense the claim requires."* RT-17 proves identity
must be supplied by *something* outside the token statistics. The call:

- **(1) The acting channel is not a label — adopt the design
  (recommended).** A label names which agent in the data is "you"; the
  motor copy marks the event of acting, is content-bearing, exists in
  any embedded agent, and is precisely the corpus's
  identity-as-continuity-of-state made mechanical. RT-02's targets — 
  arbitrary conventional labels, stylometric self-recognition — both
  stay banned; both are in fact *deader* than before. Amend, re-pilot,
  re-gate, then the 5-seed run.
- **(2) The acting channel is a label — the loss condition fires.**
  Then MVM-0a as registered is unbuildable in the required sense, the
  report goes upstream (with RT-17, which is the real finding), and
  what remains of the design gets re-scoped in a fresh registration.
  This is the honest-loss route and it is a respectable one.
- **(3) Falsify (a)-only first (~$6).** Run calibrated-marginal fill
  and watch it fail gate (iii) or starve T_sr, per the RT-17 wager,
  before adjudicating (1) vs (2). Buys certainty; costs a pilot.

Either of (1) or (2) is defensible; (1) is recommended because the
experiment it produces is *cleaner* than the one registered — every
statistical route to T_sr is provably dead, so whatever the ablations
then show about the register is about carried state, which is the thing
MVM-0a existed to measure.
