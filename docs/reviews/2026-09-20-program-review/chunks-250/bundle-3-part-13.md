  stack has found no ownership structure on any seed and the blind
  positive control returned NOT TESTABLE (`blind-control-findings.md`).
  If no other-index subspace can be localized, (e) cannot be evaluated,
  and the text does not say whether that is NOT TESTABLE or (e) waived.
  Under the input-channel lesion there is no defined other-agent
  analogue at all (the channel injects only at own positions; the
  re-indexing probe is the nearest thing and is not named).

### F15 — The two twin calibration substrates cannot run as written

**Severity: fatal against §5.5 as written. MEASURED.**

§5.5's substrates 1 and 2 are the register-less twin checkpoints from
the earlier wave, `artifacts/pilot_a1_30m_seed0_twin/…` and
`…seed1_twin/…`, to be run on the A3 batteries at 800 episodes. Static
checks:

- The twins were trained under `encoding.py`; the A3 harness encodes
  with `encoding_a3.py`. Comparing the two vocabularies: **103 tokens
  against 105, and 72 of the 105 A3 tokens carry a different id** in
  the old vocabulary or none at all. The A3 tokenizer inserts "by"
  before the item names, so every item name, every one of the eight
  answer slots and every query word is shifted. Under the A3 encoding
  the twin reads `parcel_1` as its `parcel_2`, `bay_A` as its `bay_B`,
  `bay_H` as its `where`, and ids 103 and 104 fall outside its table.
- "by" appears in every A3 turn (`assign <item> to <value> by
  <marker>`, registration revision 2). The old vocabulary has no id for
  it.
- The checkpoints' stored configuration: twin `vocab: 103`, A3 seed 0
  `vocab: 105` (read from the `.pt` files' `cfg`). The twin's token
  embedding and output head are 103 wide.
- No bridge exists: a search of `src/` for any remapping between the two
  vocabularies finds none; `encoding_a3.py`'s own self-test only asserts
  that the registered vocabulary was not edited.

So the twins cannot be fed A3 episodes without new code that maps ids,
and whatever mapping is written after registration decides what the
twin "sees" and hence what its null looks like. Even with a mapping,
a model reading a scrambled or shifted vocabulary is not "a trained
model out of distribution" as §5.5 describes it; it is a random reader
whose answers are noise of an unknown shape. The precedent §5.5 cites,
Gate 0 calibrating on the existing checkpoints, ran those checkpoints
on **their own** grammar and tokenizer. Only the untrained substrate
survives, and see F16.

### F16 — The untrained substrate risks a zero-spread null, and the maximum rule turns that into no threshold or an unreachable one

**Severity: serious. ARGUED, with this week's precedent.**

An untrained network at this configuration produces, at the revision
position and at the answer position, whatever its random head favours
among eight slot tokens; that choice can be nearly constant across
episodes or flip on small perturbations, and which of the two is not
known until it is run. Rank-4 to rank-16 random residual damage at five
layers is small relative to the residual norms (the A3 pilot record
shows removed norms of 10 to 18 per layer against reference means of 66
to 205). If few or no per-cell scores flip, the per-cell difference is
zero almost everywhere, the spread across draws is near zero, and S is
either 0/0 or a handful of flips divided by almost nothing. §5.5 then
takes the maximum 95th percentile across substrates, so a degenerate
untrained null gives either no σ or a σ far above anything a learned
model's shaped null reaches. The control diagnostic of 2026-09-17
failed on exactly a zero-spread null by construction
(`control-diagnostic-findings.md`), and that document's own lesson was
to write a non-degeneracy precondition into every null. §5.5 has none.

### F17 — Condition (f)'s validity gates have never been applied to this lesion and have no A3 implementation

**Severity: serious. MEASURED.**

(f) carries over "verbatim from Amendment A3 §3.3" the neutral-episode
likelihood bound, the long-generation degeneracy probe and the
out-of-distribution-inconclusive branch. A search of `src/` finds no
neutral-episode likelihood bound and no degeneracy probe implemented
for the A3 grammar (the only "degenerate" checks are the zero-spread
guards in the control diagnostic and the blind control). The endpoint
records for seeds 0 to 2 carry no such field among their 110 keys. So
the input-channel lesion has never been tested against these gates on
any seed. Zeroing an input the model was trained with moves every
battery (F2, F5), so it is plausible it also moves the neutral-episode
likelihood past a 95th-percentile random-damage bound. If (f) is built
and applied on the fresh seeds, all three may return NOT TESTABLE on
the first application of a gate that was never run on the seen seeds;
if it is not built, (f) is a sentence. Either the gates are implemented
and run on the seen seeds before registration, with the result
reported, or (f) should say what it actually binds.

### F18 — The random baseline is not matched to the input-channel lesion in any stated sense

**Severity: serious. ARGUED from the code.**

§5.4(a) describes the baseline as "random removals of the same rank and
the same norm, at the same layers" as the damage operation. For a
localized subspace lesion that is meaningful. For zeroing `act_proj`,
a 448-by-448 projection that injects at the model's own enacted
positions only, it has no rank in the residual stream, no layer among
3, 4, 5, 7 and 8, and a norm concentrated at three positions rather
than spread over all of them. The Gate 0 machinery applies random
damage to all positions at fixed layers with strengths set by a
reference pass. A3's endpoint used that sweep as the input-channel
lesion's null anyway, which is a defensible precedent as long as the
text says "the registered residual sweep, unmatched to this lesion";
§5's text promises a matched baseline the machinery cannot produce, and
a reader will take "matched-strength" at its word.

### F19 — Per-cell scoring is a new instrument, and its first run would be the verdict

**Severity: serious. MEASURED.**

The A3 evaluation function returns per-battery accuracies rounded to
three places and nothing per episode (`train_a3.eval_heldout`); the
endpoint script stores per-evaluation-seed means. The clause needs a
per-cell record of intact and damaged correctness for two or three
batteries on the same 800 episodes, the pairing of the self-directed
read (inside the episode) with the appended reads (after it), the
within-run baseline, and the ladder. That is a new scoring path. The
known-answer rule of 2026-09-16 (`lock_guard.require_known_answer_pass`
and its ruling) exists because a new pipeline returned five probes
below their nulls and nothing separated an insensitive stack from a
bug. §5 registers no known-answer test for the separation script. A
cheap one is available and should be registered: the new script's
per-cell records for seed 0 must reproduce the seed-0 endpoint means
for every battery, intact and lesioned, to the rounding, before any
fresh seed is scored. (That reproduces published aggregates; it does
not compute the separation statistic on a seen seed.)

### F20 — The lock guard cannot hold this lock, and the evaluation seeds are outside it

**Severity: worth noting. MEASURED.**

`lock_guard.require_lock` (version 1) refuses a lock that lacks `theta`
and `delta` fields, requires a threshold entry for every battery about
to be read, and validates against exactly one calibration record by
hash. A σ lock carrying three calibration records and an exclusion
field is a new lock version and new guard code, written after
registration. §5.5 step 3's "through the existing lock-guard machinery"
is not literally available. Separately, the endpoint reads use six
evaluation seeds and report a spread; §5 does not say which seeds
define the 800 episodes the verdict is read on for seeds 3 to 5, and a
seed chosen after seeing the default-seed reading is a fit route. The
lock should carry the evaluation seeds.

### F21 — Two seeds in the text, three in the ruling

**Severity: worth noting; must be fixed before registration. ARGUED.**

Condition (h) reads "seeds 3 and 4, and must hold on both". John ruled
three fresh seeds. The registered text needs to say three of three (the
A3 rule), what a NOT TESTABLE seed does to the across-seed condition,
and where two of three lands (F13).

### F22 — The comparator is read on a subpopulation its precondition was not written on

**Severity: worth noting. ARGUED from the code.**

The other-directed and state queries are appended to every episode, and
their battery scores are over all 800. Matched cells exist only in the
roughly 400 episodes where the model's slot was drawn as a reviser. In
those episodes the model's own revision is visible and the named other
agent is one of the non-revisers or the co-reviser, so the
other-directed query's difficulty differs from the full battery's, and
its intact level on that subpopulation has not been measured. Condition
(d)'s 0.10 margin is written on the whole battery. The text should say
which population (d) is evaluated on and which the comparator's
"measured spread of change" (the ruling annotation's second addition)
is reported on.

---

## Two notes on time and money, because §5.5 depends on them

- **Calibration time.** The one A3 random sweep on the record took
  6,047 seconds for 120 draws at 800 episodes on the Mac. Three
  substrates is about five hours if the twins could run (F15), and a
  within-run spread on each fresh seed (F6, reading 1) is another 1.7
  hours per seed after arrival, before any verdict. That fits inside
  "lock before read" as ruled, but the lock cannot be cut before launch
  if the substrates need new code first, and the registration should
  say so rather than leaving §6.4's permission to cover it.
- **Nothing in this pass changes the cost estimate.** Every finding is
  fixable at $0 or is a reason not to spend.

---

## Kill case, in one paragraph

Under the only damage operation the programme can currently read, the
clause cannot fail on any checkpoint resembling the three in hand: the
comparator has a fifth of the self-directed battery's room to fall, so
the cell the repair exists to make reachable is arithmetically
unreachable, and the positive cell will fire with a many-sigma number
under the registered positive bin's name. The calibration that is meant
to set the bar sets a number near 2 on any substrate, and two of its
three substrates cannot be run because their tokenizer is not the A3
tokenizer. The application that would make the clause informative, a
localized lesion, is gated behind a stack that has found nothing on any
seed. So the $30 buys three more instances of C1's already replicated
result, relabelled. Close A3 on the record as it stands, state the
matched self/other contrast as the design's unmet requirement, and
register a separation clause only when there is a localized lesion to
read it on and a comparator that can fall as far as the battery it is
compared against.

## If it ships anyway: what §5 needs before it is registerable

Listed as remedies, not as amendment text; every one is $0.

1. Rename the positive cell for what it measures under the input-
   channel lesion; reserve H_self-location for the registered localized
   result (F9). Restore the ruled meaning of "located, wrong structure"
   and give the other-directed-falls-more event its own name (F10).
2. Make the outcome table exhaustive: cells for (a) holding while (c),
   (e) or (h) fails; for an improvement inside the band; for two of
   three; carry A3's seed-dependent and unstable bins (F13, F21).
3. Define the spread: on which checkpoint, over which draws, pooled or
   per cell, across draws not cells (F6). Say plainly that σ will land
   near 2 and why that is acceptable, or replace the self-normalized
   calibration with one that has content.
4. Replace the twin substrates or register the tokenizer bridge and its
   consequences before the lock (F15). Add a non-degeneracy precondition
   on every null and say what happens when it fails (F16).
5. Quantify condition (e) and say what happens when the other-index
   subspace cannot be localized (F14). Describe the baseline as the
   registered residual sweep, unmatched to the input-channel lesion, or
   design a matched one and register it (F18).
6. Either implement (f)'s gates for A3, run them on the seen seeds'
   input-channel lesion before registration and report the result, or
   strike (f) (F17).
7. Register a known-answer test for the separation script against the
   seed-0 endpoint means, to pass before any fresh seed is scored (F19).
   Extend the lock guard to a σ lock that also carries the evaluation
   seeds (F20).
8. Pre-state, in the registered text, the expected S on the fresh seeds
   computed from the seen endpoint records, and the minimum S reachable
   if the control collapsed to chance; report seen seeds under their
   own heading, never alongside fresh ones; state which cells were
   reachable on the checkpoint read (F1, F5, F11, F12).
9. State which population the engagement precondition and the
   comparator's reported spread are read on (F22), and carry the memo's
   admissions about data-informed choices into the registered text (F8).

---

*Authorship: this pass is Claude's. Nothing in it is a ruling. It does
not edit the proposal, does not write the amendment, and did not open
the amendment draft, the first red-team pass or the scoring script that
were on disk when it ran.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/control-battery-proposal.md =====
