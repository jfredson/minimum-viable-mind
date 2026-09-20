
## Open items

1. **Causal patching has still never run.** Under the registration it is
   required before anything counts as localized or absent. This is the
   binding item, and it is already on the 2026-10-04 control-battery
   decision.
2. **`other_revision_value` rises on all three checkpoints** (+2.33,
   +2.39, +3.34) and reaches MARGINAL on seed 2. If any position deserves
   a targeted rerun with far more draws, it is this one — though it is the
   other agent's turn, not the model's own.
3. **The marker-word target at these eleven positions** remains unrun, and
   is the obvious remaining cheap-ish read if about 70 processor-hours can
   be found.
4. **The pilot-versus-seeds legibility gap** on the difference-of-averages
   control is still unexplained.
5. **Seed 2's fits are mostly capped** (73.6%). Whether raising the cap
   changes anything there is unknown and untested; it would be a different
   instrument and would need its own anchor.

## Cost and where the output is

Local, inference only, no training, no network, $0 [C1/C2]. 10.8 hours of
wall-clock time, about eleven processor-hours, on three existing
checkpoints. Outputs, none overwritten [C6]:

- `a3-gates/fitted_position_sweep_a3_a3_30m_seed0.json`
- `a3-gates/fitted_position_sweep_a3_a3_30m_seed1.json`
- `a3-gates/fitted_position_sweep_a3_a3_30m_seed2.json`
- `a3-gates/fitted_position_sweep_a3_summary.json`

These findings go through a Gate B review before any of this enters
STATUS.md.


===== FILE: experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings-CORRECTION-2026-09-20.md =====

# Correction note — the sensitivity figure in `fitted-position-sweep-findings.md`

*2026-09-20 (Pacific). The findings file is committed method-then-output
text and is not edited. This note sits beside it and is cited wherever the
figure is used. Ruled by John 2026-09-20 on Gate B review finding RT-74
(ledger numbering; RT-56 in the review file), "agreed on all".*

The findings state that the run would have detected the register index if
it were legible in about one episode in twenty-seven. That figure assumes a
perfectly legible episode scores 1.0. This read never does: the only ceiling
the run measures is 0.539 to 0.567, at the position where the answer is the
input token. Recalibrated against that ceiling, the run's reach is a signal
legible in about **one episode in eleven**. The same correction applies to
the "essentially identical power" comparison between the two reads
(review RT-73 / ledger RT-91): the conclusion drawn there stands, the
reasoning given for it does not.

Anywhere the one-in-twenty-seven figure has been quoted (STATUS.md, the
step 4 proposal, the paper draft), it reads one in eleven and cites this
note.


===== FILE: experiments/06-mvm-0a-constructed-self-index/separation-clause-requirements.md =====

# What a separation clause must satisfy before it can be registered

*2026-09-19. Design requirements, not clause text and not registered
text. Written after John withdrew Amendment A4 on the findings in
`red-team-a4.md` (the second red-team pass on the A4 clause, findings F1
to F22 and nine remedies) and while a $10 unregistered pilot runs to see
whether the control battery learns when given its own loss term. Every
requirement below is traced to the finding it comes from. The numbers in
Part 2 are stated now, before the pilot reports, so that reading the
pilot against them is not fitting.*

*Status of the pilot, for the record. The registered loss (Amendment A3,
registration revision 9) is one pooled cross-entropy over every appended
query plus the action cross-entropy at the model's own revision turn,
summed at equal weight, the weight passed explicitly at every launch
(`train_a3.loss_a3`). A separate weighted term for the control query is
a change to that registered loss. So whatever the pilot shows, a clause
built on it belongs to a redesign with its own registration, and the
pilot checkpoint is a seen seed of that redesign: no verdict is ever
read from it, and it is not a calibration substrate for any threshold
with content.*

*House rule: the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30). The batteries are named in words; their short names
appear once each in the glossary of `red-team-a4.md` and are not
repeated here.*

---

## The one-paragraph version

A separation clause compares how much a lesion hurts the self-directed
condition against how much it hurts an ownership-free comparator. It is
registerable only when (1) the comparator can fall about as far as the
self-directed battery can, so the boring outcome is reachable; (2) both
conditions are read at positions that stand in the same relation to the
lesion, so a position-local disruption cannot pass as ownership-specific;
and (3) the threshold is a measured quantity in score units, on a named
checkpoint, from a named draw set, with a non-degeneracy check, rather
than a score divided by its own null. The pilot decides (1) and nothing
else. (2) needs a grammar change to where the other-directed score is
read. (3) is a matter of writing the clause properly. And even with all
three met, the clause under an input-channel lesion answers only whether
the ownership input is load-bearing; the question the programme is
actually asking, whether the network built a structure, still needs a
localized lesion and the discriminators that go with it.

---

## Part 1 — Hard requirements

Each is necessary. A clause that fails any one is not registerable,
whatever the pilot shows.

### H1 — The comparator must have room to fall comparable to the primary's (from F1, F4, F8)

**The defect.** Under the input-channel lesion the self-directed battery
falls by about 0.37 to 0.43 raw. The control on the seen seeds sits at
0.29 to 0.32, so its largest possible fall is about 0.19 even if it were
destroyed to chance. A difference-of-drops statistic then cannot come
out near zero, so the cell that reads "generic binding" cannot fire, and
the clause cannot lose.

**The requirement.** Let a battery's *room* be its intact score minus
its chance floor. The comparator's room must be within the null band of
the primary's room, so that a lesion which removes the same fraction of
each battery's learned margin produces a difference the null cannot
distinguish from zero. Part 2 turns this into numbers.

**Corollaries.**

- The clause must state, before the fresh seeds exist, the *reachable
  range* of its statistic on a checkpoint of the design: the value if
  the comparator collapsed to chance and the primary collapsed to its
  ownership-blind ceiling. If the boring cell lies outside that range,
  the clause is not registerable (F1, F12, remedy 8).
- The clause must state its *expected* value from whatever seen record
  exists, and what result would surprise. A prediction from data in
  hand is fine when labelled; a claim of ignorance is not (F5, remedy 8).
- A second comparator counts only if it is matched on a dimension the
  first is not (content, position, chance, room). Two comparators that
  pass or fail for the same structural reason are one check (F4).
- An engagement floor must be set relative to the level a solver that
  ignores the name reaches, not relative to chance. "Above chance" on
  this control certifies nothing about name-keyed binding (F8).

### H2 — Both conditions must be read at comparable positions relative to where the lesion strikes (from F2, F18, F22)

**The defect.** The self-directed score is read at the model's own
revision turn inside the episode, which is exactly an acting-channel
injection site. The other-directed score is read at a question appended
after the episode, downstream of every injection. The input-channel
lesion alters the residual stream precisely at the tokens where one
score is read and not the other. A disruption that is local to the
altered positions and carries nothing about ownership therefore
satisfies the clause, and the registered random baseline, which damages
every position evenly, cannot catch it.

**The requirement.** The two conditions must be read at positions that
stand in the same relation to the lesion: both at injection sites or
neither; both at action positions or neither; the same distance in turns
from the last altered token. Three ways to meet it, in order of
preference:

1. **An other-directed action at an own enacted turn.** Add to the
   grammar a turn on which the model acts on *another agent's*
   commitment: for instance, on its own turn it must assign an item to
   the value the rule dictates for a named other agent's earlier value.
   That is an action, read at an injection site, requiring name-keyed
   binding and no ownership. It gives a comparator matched in position,
   in read type and in rule, with only whose commitment differs. This is
   the design change the brief anticipated, and it is a grammar change:
   the cue gates, the attack sweep and the frozen batteries all run
   again on it, and the ownership-blind ceiling of the new turn is
   measured on the new grammar by an attack that reads the name.
2. **Restrict the clause to lesions that strike positions symmetrically.**
   A localized subspace removed at every position affects the appended
   question and the revision turn alike. Under this option the clause is
   not read on the input-channel lesion at all; the input-channel lesion
   stays what A3 made it, a validity check and an upper bound. See Part 3.
3. **A position-matched random baseline.** If the clause is to be read
   on the input-channel lesion anyway, the null family must include
   random damage concentrated at the model's own enacted positions with
   norm matched to the injection it removes, so that "damage at own
   positions with no ownership content" is something the null can
   produce. This is a weaker fix than 1 or 2 because it corrects the
   baseline rather than the measurement, and it should not be the only
   one taken.

Moving the self-directed read to an appended question is not an option:
Amendment A3 §2.1 requires the supervised position to be an action, not
a report, and that requirement is the reason the design exists.

**Corollaries.**

- The baseline must be described as what the machinery produces. If
  the registered residual sweep is used as the null for a lesion it is
  not matched to, the clause says "unmatched" (F18).
- The population each condition is read on must be stated: matched
  cells only, or the whole battery, and the engagement floor must be
  evaluated on the same population the statistic is (F22).

### H3 — The calibration must have content (from F6, F7, F14, F15, F16, F19, F20)

**The defect.** A score divided by the standard deviation of its own
null has a 95th percentile near 2 on any substrate; the calibration
decided nothing, and the quantity that decided the verdict, the spread
used on the fresh seeds, was undefined. Two of the three calibration
substrates could not be run because their tokenizer was not the design's
tokenizer. No non-degeneracy check existed. The random draws that
defined the threshold were also required not to exceed it.

**The requirement.** Every quantity the verdict divides by or compares
against must be:

1. **In score units, on a named checkpoint.** The spread or band is
   measured in raw battery points on a stated checkpoint, and the clause
   says which: the checkpoint being read (a within-run null after the
   lock), or a substrate, never "the baseline" unqualified. If a
   substrate, it runs the design's own grammar and tokenizer; a
   checkpoint that needs a vocabulary bridge is not a substrate. **A
   substrate is named in a clause only after a dry run has shown it
   loads and scores on the design's batteries** (F15; this is now a
   standing rule in memory: verify substrates before proposing them).
2. **From a named draw set with named pooling.** Layers, ranks,
   operators, seeds, and whether the spread is pooled over all draws or
   taken per layer-rank-operator cell; across draws, not across cells.
3. **Guarded by a non-degeneracy precondition.** A null whose spread is
   below a stated floor, or in which fewer than a stated fraction of
   cells ever flip, assigns no threshold and stops the read. The floor
   is written before the sweep runs. The 2026-09-17 control diagnostic
   is the precedent for why (F16).
4. **Not self-referential.** A threshold set as the 95th percentile of a
   population cannot also require every member of that population to
   sit below it. Any control condition on random draws carries a
   quantifier: the 95th percentile of a fresh sweep, or the median
   (F14).
5. **Separated from the shape statistic.** If a standardized score is
   kept for reporting, the verdict turns on the raw quantity and its
   measured band, and the standardized number is reported beside it,
   labelled as a shape statistic that lands near 2 by construction.
6. **Locked with what it depends on.** The lock carries the calibration
   record hash, the checkpoint, the draw set, the pooling rule, the
   non-degeneracy result, and the evaluation seeds that define the
   episodes the verdict is read on. The lock guard is extended to hold
   that lock before the clause is written, not after (F20).
7. **Read by a validated instrument.** Per-cell paired scoring is a new
   path; it passes a known-answer test before any fresh seed is scored.
   The cheap one: its per-cell records for a seen checkpoint must
   reproduce that checkpoint's endpoint means, intact and lesioned, for
   every battery, to the rounding (F19).

### H4 — The outcome table must partition the outcomes and keep ruled names (from F9, F10, F13, F21)

- Every combination of the clause's conditions lands in a named cell,
  including: the separation condition holding while a comparator or
  control condition fails; an improvement of the primary inside the
  band; two seeds of three; a seed returning not-testable while the
  others pass. The A3 bins "seed-dependent" and "unstable" are carried
  (F13, F21).
- Cell names are not reused from the registered A3 bins unless the cell
  carries the same discriminators. A positive under an input-channel
  lesion is named for what it measures, on the order of "the ownership
  input is specifically load-bearing for the self-directed condition";
  H_self-location stays reserved for the localized result (F9).
- A cell John has ruled keeps its ruled meaning. The 2026-09-19 "located,
  wrong structure" cell means the ablation improves the primary battery
  beyond noise; a comparator-falls-more outcome gets its own name (F10).
- Three fresh seeds, three of three for a positive, as A3 registered.

### H5 — The validity gates must exist and have been run (from F17)

The neutral-episode likelihood bound and the long-generation degeneracy
probe have no A3 implementation and have never been applied to the
input-channel lesion on any seed. Before a clause names them, they are
implemented for the design's grammar and run on the seen seeds under
every lesion the clause will read, and the result is reported. A gate
whose first application is on the verdict seeds is either a surprise
kill or a sentence.

### H6 — Reporting rules registered with the clause (from F11, F12)

- Seen seeds are reported under their own heading, labelled seen and
  verdict-free, never in the same table as fresh seeds.
- The write-up states which cells were reachable on the checkpoint read,
  not only which fired.
- Any dose ladder on an input scaling is reported as an input-scaling
  curve, with the statement that a smooth reduction of one signal is
  monotone by construction.

---

## Part 2 — What the pilot must show for H1 to be satisfiable

The pilot is one unregistered seed. What it can decide is whether the
control battery, given its own loss term, reaches a level at which a
comparison has room to move. The numbers below are stated before the
pilot reports and are read against the pilot's intact scores measured
the way the endpoint reads are: at least 800 episodes, at least six
independent evaluation seeds, mean and spread reported. Where a
threshold is compared against a mean, use the mean minus one spread, so
that a lucky draw does not clear a bar.

### The fixed points these numbers rest on

| quantity | value | source |
|---|---|---|
| primary battery intact, seen seeds | 0.5683, 0.5633, 0.5738 | the endpoint findings, `seeds-endpoint-findings.md` |
| primary under the input-channel lesion | 0.1988, 0.2015, 0.1447 | same |
| primary's chance floor / ownership-blind ceiling | 0.125 / 0.2921 | `batteries-a3/batteries_meta.json` |
| control intact, seen seeds | 0.2877, 0.3057, 0.3195 | the endpoint findings |
| control under the input-channel lesion, seen seeds | 0.2283, 0.2342, 0.2617 | the endpoint records, `a3-gates/endpoint_*.json` |
| control's chance floor / name-blind reference / true ownership-blind ceiling | 0.125 / 0.3227 / 1.0 | `ceiling-measurement-findings.md` |
| evaluation noise at 800 episodes, primary / control | sd 0.0169 / 0.0233 | `a3-gates/eval_noise_a3.json` |
| random-damage band on the primary, 95th percentile | 0.1777 corrected, about 0.049 raw | John's lock, `null-calibration/theta_delta.lock.json` |

From these: the primary's room (intact minus chance) is about **0.44**;
its fall under the input-channel lesion is about **0.37 to 0.43**; a
random-damage spread of the mean drop is of order **0.02 to 0.025 raw**
(a standard deviation runs about half the 95th percentile), so a
difference of two drops is inside the null when it is below about
**0.05 raw**.

### Tier A — a raw-difference clause is registerable

The statistic compares raw drops. For the boring cell to be reachable,
a lesion removing the same fraction of each battery's room must give a
difference inside the null even at full removal, so the two rooms must
differ by no more than the band:

> **control intact ≥ primary intact − 0.05**, with both measured on the
> pilot checkpoint. At a primary of 0.57 that is **control ≥ 0.52**.

Under Tier A the statistic needs no denominator that can shrink, the
design's original intent (matched contrast, no ceiling anywhere) is
met, and H1 is satisfied outright.

### Tier B — a relative-drop clause is registerable, with a floor

The statistic compares each battery's drop as a fraction of its own
room. This restores reachability at lower control scores but puts a
room back in a denominator, the shape of the defect that killed the A3
clause, so the room must be large enough that the fraction is not
noise:

> **control room ≥ 0.25**, that is **control intact ≥ 0.375**; and
> **control intact ≥ name-blind reference + 2 sd = 0.3227 + 0.047 ≈ 0.37**,
> so that "learned" means "beats a solver that cannot read the name",
> not "landed near it".

Why 0.25: the standard error of a mean of 400 paired 0/1 differences is
about 0.023 raw; over a room of 0.25 that is a relative error of about
0.09, against about 0.05 for the primary. Below a room of 0.25 the
comparator's relative drop is noisier than the effect it is meant to
detect. The two conditions coincide near **0.375**, which is also
within rounding of the level the corrected A3 floor rule already
required (0.4227) for the old drop to be defined at all; a control that
cannot clear the old floor does not clear the new one either.

Under Tier B the clause must additionally register the room floor as a
not-testable condition on every fresh seed, because a fresh seed whose
control lands below it has no defined comparator.

### Tier C — no separation clause

> **control intact < 0.375** on the pilot.

The control does not learn enough for any comparison to move. The
result is reported as the matched contrast remaining unmet, and the
next design question is the grammar, not the clause.

### Conditions on the primary, which the extra loss term can move

Adding a control loss changes the mixture the primary was learned
under. Whatever tier the control reaches, the primary must still be a
battery a lesion can be read on:

> **primary intact ≥ 0.49** (its ownership-blind ceiling of 0.2921 plus
> 0.20, four times the random-damage band), and its fall under the
> input-channel lesion must still clear the locked band. If the control
> loss starves the primary toward its ceiling, that is the
> shortcut-starvation outcome A3 pre-stated, and no clause is built on
> it.

### What the pilot does not decide

- One seed reaching a tier licenses a design, not a registration. The
  tier is confirmed or not on the redesign's fresh seeds, and a fresh
  seed landing in a lower tier is not-testable under that clause.
- The pilot says nothing about H2. A control that learns the appended
  question to 0.55 is still read at the appended question.
- The pilot's control score under the input-channel lesion will be in
  its endpoint record, as the seen seeds' are. It may be quoted to
  pre-state the expected value of a future statistic (H1, corollary 2).
  It is not evidence for a cell.

---

## Part 3 — What still needs a localized lesion

Everything above makes a comparison clause honest. None of it makes the
comparison answer the programme's question. Two distinct claims are in
play and the requirements for each differ.

### Claim 1 — the ownership input is specifically load-bearing

This is what a separation clause under the input-channel lesion can
say, once H1 and H2 hold. It is a stronger statement than the seen
result, because it controls content and rule on a comparator that can
move. It is still a statement about an input, and the registered text
already concedes that the wire lesion cannot separate a carried binding
from a re-readable pointer (Amendment A3, registration revision 8). No
comparator fixes that, because the two accounts predict the same
behaviour under input removal.

### Claim 2 — the network built a structure that indexes its binding to its own center

This is the registered H_self-location and it needs, in addition to a
comparison that can move:

1. **A localized lesion target**, a low-rank subspace at positions away
   from the model's own act positions, found by probe and patching that
   agree (Amendment A3 §3.2). The stack has found nothing on any seed,
   and the known-answer test validates the plumbing but not the
   ablation path. Before any clause is read on a localized lesion:
   - a positive control the stack recovers, on this design, not a
     synthetic one;
   - the denoised difference-of-means direction from the Pain Axis note
     (item 2 of `docs/research-note-pain-axis-2026-09-19.md`) run
     against the same permutation null, so that "insensitive stack" and
     "no signal" are separated before money is spent.
2. **The discriminators the comparison does not carry** (F3): the swap
   probe moving the action with the patched identity; the other-index
   control, a subspace localized for a named non-self agent, matched in
   rank and probe accuracy, that does not hurt the self-directed
   condition; and the mid-episode re-indexing probe for the tag bin.
   Without these, an act-marker echo or a mine-bit tag passes any
   separation clause.
3. **A random baseline matched to the lesion** in rank, norm and layer,
   which the Gate 0 machinery does produce for a subspace lesion (H2,
   option 2 is met by construction here).
4. **The full bin set**: H_tag, H_self-reference-only, H_diffuse and the
   validity-check-failed bin, as A3 registered them, with the separation
   statistic replacing only the differential conjunct inside them.

### The order this implies

1. Read the pilot against Part 2. If Tier C, stop here and say so.
2. If Tier A or B, redesign the grammar for H2 (an other-directed action
   at an own enacted turn), re-run the gates and the attack sweep with a
   name-reading attacker, measure the new ceilings, and re-freeze.
3. Write the clause to H3 to H6, with substrates dry-run before they are
   named and the scoring script's known-answer test passed on a seen
   checkpoint.
4. Register Claim 1's cell under its own name. Read it on fresh seeds.
5. Register Claim 2 only when Part 3's items 1 and 2 exist on the
   design. Until then, the localized-lesion application of the clause
   is a stated future amendment, not a registered one.

---

*Authorship: this document is Claude's, written to John's brief of
2026-09-19. Nothing in it is a ruling and nothing in it is clause text.
The tiers in Part 2 are pre-stated numbers; the choice of 0.05 for the
raw band and 0.25 for the relative-room floor are judgment calls from
the measured noise, stated so that they can be argued before the pilot
reports rather than after.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md =====

# MVM-0a red-team ledger (pass 1, 2026-08-04)

*Adversarial pass on `pre-registration.md` draft v0.1. Fifteen findings:
three fatal, eleven serious, one procedural. All patches are written into
**draft v0.3**. RT-04 was adjudicated by John on 2026-08-04 (option (b) —
scope to Q5); the other fourteen dispositions are the drafter's
recommendation and remain open to John's review, per the house procedure.

Findings below quote v0.1's bin names (`H_center`, `H_bypass`,
`H_router`) because that is the vocabulary they were written against.
v0.3 renames those bins to `H_load-bearing`, `H_routed-around`, and
`H_generic-state` — a consequence of the RT-04 adjudication, not a
separate change.*

The pass's summary judgement, which the draft should absorb rather than
resist: the design's one structural virtue — a physically designated
ablation target — was doing more rhetorical work than engineering work.
Designation fixes *where* to cut, not *what was cut*.

| ID | Finding | Severity | Disposition |
|---|---|---|---|
| RT-01 | Register may be a keyed memory array; bins can't tell | fatal | ADOPTED — swap/re-index/address probes + new bin |
| RT-02 | Self-identification bootstrap trilemma | fatal | ADOPTED — on-policy mandatory, no identity token, style canonicalization |
| RT-03 | "Residual path" unfalsifiable; decision deferred past registration | fatal | ADOPTED — no-register twin gate; architecture locked in registration |
| RT-04 | No report channel; H_description engineered out | serious→fatal for framing | **ADJUDICATED 2026-08-04 — option (b): scope to Q5, defer the contrast to MVM-0b** |
| RT-05 | T_syntax vacuous by construction; H_center collapses to one clause | serious | ADOPTED — cross-turn state control replaces it |
| RT-06 | Single training run; model is a draw, not a fixture | serious | ADOPTED — k ≥ 5 seeds, majority rule, seed-dependent bin |
| RT-07 | Register reliance is a trajectory; stopping point selects the verdict | serious | ADOPTED — checkpoint schedule, verdict read at budget exhaustion |
| RT-08 | Cue-detector gate: wrong time, wrong representation, no power | serious | ADOPTED — three runs, equivalence bound, positive control |
| RT-09 | H_bypass has no construction-failure guard | serious | ADOPTED — register-utilization gate before any bypass reading |
| RT-10 | Thresholds fitted to a same-model pilot | serious | ADOPTED — null-calibrated θ/δ on the registered model |
| RT-11 | Ownership not crossed with content; coherence solver passes | serious | ADOPTED — content-crossing as hard curriculum property + forced-revision eval |
| RT-12 | Q1 inference invalid; the instrument-testbed arm is missing | serious | ADOPTED — blind-localization arm added; Q1 claim deleted otherwise |
| RT-13 | Ablation operator for a recurrent state unspecified | serious | ADOPTED — operator set pre-registered + dynamics-matched control |
| RT-14 | `d` metric doesn't transfer: unbounded cull pool, chance floor | serious | ADOPTED — frozen items, cull ceiling, chance-corrected `d` |
| RT-15 | Ethics precondition is nominal (no owner/date) | worth-noting | ADOPTED — owner+date required in the registration; non-promotable tags |

## The three fatal findings, in full

### RT-01 — the register may be a keyed memory array

**Attack.** The draft never fixes whether there is one register or N (one
per agent). With N symmetric registers and the model owning index 0,
"self" is a slot address fixed by which index the loss queries. Ablating
register₀ destroys T_sr; ablating register₁ spares it. That crossed
dissociation *is* the H_center fingerprint, and a content-addressed
memory array containing no self-indexing produces it with certainty. The
system would behave identically if slot 0 were named "agent Q." With one
register, the self/other asymmetry is architectural rather than learned
and the matched-capacity control has no matched object.

**Why it bites.** Every gate in v0.1 passes. The paper reports
"self-indexing can be architecturally centralized." The mechanism is a
labeled dict.

**Patch (adopted).** Three probes a keyed slot and a center answer
differently: (1) **register swap** — exchange self and other register
contents; a keyed slot gives a tidy content relabel with all other
integration intact, a center gives global disruption; (2) **mid-episode
re-indexing** — change which agent the model is at turn k; keyed memory
follows the slot, a center pays a re-centering cost visible in non-self
integration too; (3) **address probe** — if the register decodes agent
identity at AUC ≥ 0.95 independent of episode content, it is an address.
New registered bin **self-index-not-established**, the direct analog of
Experiment 1's RT-09 "reflexivity not established" — a gate v0.1 dropped
while inheriting the objection.

### RT-02 — the self-identification bootstrap trilemma

**Attack.** For the curriculum to be solvable the model must establish
which agent it is, and there are only three routes: **told** (an identity
token — identity supplied from outside, precisely the corpus's
"represents itself from outside"); **stylometry** (its own sampled text
is distributionally distinct from grammar-generated distractors —
self-recognition by fingerprint, fully explained by mimicry, which the
standing rules say to discount); or **teacher-forced** (its "own" turns
are designated turns in a static transcript it did not produce — third-
person tracking, not self-reference). All three yield H_center; none
supports the claim.

**Patch (adopted).** The only non-disqualifying grounding is *causal
authorship*. Therefore, registered rather than deferred: on-policy
training mandatory (commitments are the model's own sampled outputs); no
agent-identity token, header, or persistent positional convention;
style-canonicalization of all commitments at baseline and eval. **Loss
condition:** if T_sr collapses under canonicalization, the model was
doing stylometry and no H_center attaches; if identity must be supplied
by a label for the task to be learnable, the anti-router curriculum is
unbuildable in the required sense.

### RT-03 — the unloseability guard is a sentence, not a test

**Attack.** "The architecture must leave a residual path capable of
carrying the binding" has no test of "capable," and is trivially
satisfied by any transformer whose attention reaches prior turns. The
real determinant is whether *this* optimizer on *this* curriculum finds
the residual route — set by choices v0.1 defers to §Decisions, plus one
it never names: **whether attention spans the whole episode or is
windowed per turn.** Windowed ⇒ the register is the only cross-turn
channel ⇒ H_center guaranteed. So the registered prediction's truth value
is fixed by an unregistered decision made after registration.

**Patch (adopted).** A **no-register twin**: an identical model with the
register removed from initialization, same curriculum, budget, seeds. It
must reach held-out binding accuracy within a pre-committed margin — then
the residual path is *demonstrated* and H_center is loseable. If it does
not, the outcome is **void (architectural bottleneck)**, never H_center.
Cross-turn attention span, injection mechanism, and register width move
out of §Decisions and into the registration. No auxiliary loss on
register content and no hand-specified self-writing update rule — that
would be designing the answer in.

## The highest-value finding

### RT-12 — the missing arm is worth more than the headline

v0.1 claimed an H_center result would make Experiment 1's null "more
readable as absence than instrument failure (Q1)." That does not go
through: MVM-0a runs *no localization instrument at all* — that is its
advertised advantage — so a result obtained without running the
instrument cannot bear on whether the instrument works.

But the design is one step from answering Q1 properly. **Added as a
registered arm:** run Experiment 1's full localization pipeline (linear
probes, activation patching, SAEs where trainable) on MVM-0a **blind to
the register's location**, and ask whether the instruments recover a
center that is known-by-construction to exist and to be load-bearing,
and whether their ablation reproduces the designated-object damage
