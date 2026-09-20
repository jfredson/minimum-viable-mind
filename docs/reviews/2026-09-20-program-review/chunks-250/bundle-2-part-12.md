
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
