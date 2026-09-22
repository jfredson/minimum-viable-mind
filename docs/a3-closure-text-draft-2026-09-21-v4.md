# Amendment A3 closure text, version 4 (DRAFT for Gate A, tier 2)

*2026-09-21 (Pacific). Version 4 is version 3 with its three
non-wording preconditions met and the text they held open filled in:
the December-result ruling is committed (`acd8305`), the compute ledger
carries the programme running total on its two most recent rows
(`38c006b`), and the blind-arm reconciliation is a committed ruling file
(`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`). As first
written, the diff against version 3 was confined to the successor's
registration date, the blind-arm sentences, and the money paragraph; the
correction recorded in the next paragraph added to it. Versions 1 to 3 stay on
disk unedited. John ruled on 2026-09-21 that all twenty-nine tier 1
findings (ledger RT-143 to RT-171) are accepted as drafted and that
version 3 replaces version 2 as the text; version 4 is the text the tier
2 pass reads.*

*Corrected 2026-09-21 (Pacific), after version 4 was first written, by a
session acting on an independent closure check of it. Nothing below changes
what the block concludes; every change is a citation that pointed at the
wrong place, or a claim that carried no record. The successor's schedule now
cites item 1 of the December-result ruling, which is where the registration
date, the kill date, both review tiers and the amendment to the
center-as-degree ruling actually are; it cited item 7, which carries only the
two kill dates. That is the same class of error as the finding that stopped
version 2 (the red team ledger's `RT-145`): a citation pointing at something
that does not say what the sentence says. The sentence that read "the
validity gates were clean and no instrument breached them" is replaced,
because no record of any outcome on those gates exists, and the record that
does exist says they were never applied to anything; the replacement says
that and no more. The figure of 1.94 episodes in four thousand now points at
the ledger row that computed it, instead of at a findings file that does not
contain it. Two further claims that an instrument was never run — the
mid-episode re-indexing probe and the deferred marker-word read — now carry
their records, as the patching claim already did, and the marker-word read
now carries the reason it was deferred. "Registration revision 8" now names
the file it is a revision of. The date in the heading is still a placeholder,
because the commit that fills it does not exist yet, and the placeholder now
says so. The session that made these changes did not verify them; the closure
rule gives that to another session (`docs/outside-review-protocol.md`, "The
closure rule").*

*This is registered text once it lands in
`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` as a dated
closure block. It has not landed. Nothing is appended until both tiers
have filed, John has ruled, and the closure rule is satisfied.*

---

## Closure of Amendment A3, [date of the Gate A pass]

*The date above is a placeholder and is filled with the date of the commit
that appends this block to `amendment-a3.md`. It cannot be written before
that commit exists, so it is still open here.*

**Outcome: not testable — the registered comparison could never be
computed, and what the experiment could measure without it was measured on
three seeds.** This is the loss condition's sense of the phrase, not the
validity-gate bin of the same name — the bin for an ablation that damages the
model so broadly that no reading of it can be trusted. That bin did not fire,
and it was also never tested: those gates have no code written for this design
and were never applied to any lesion on any seed (the independent review of
2026-09-19 searched the source and the three endpoint records and found
neither — `red-team-a4.md`, its seventeenth finding, labelled there F17), and
the subspace ablation
they were written to guard never ran, because no subspace was ever
localized.

The pre-registered loss condition fired: *no non-self cross-turn control
can be built that is state-requiring at ceiling — then the differential
discriminator is dead here and the honest report is "not testable"*
(`pre-registration.md`, under "Loss conditions"). The control battery's
ownership-blind ceiling was measured at 1.0
(`ceiling-measurement-findings.md`, 2026-09-17), so the registered
differential clause had no computable value for any model from the day it
was registered; the same measurement shows why this is structural rather
than a defect of this control, in that the ceiling-corrected metric and the
idea of an ownership-free control are incompatible by construction. The
number the registration recorded as that ceiling was itself never attacked,
which is registered separately as a defect in the instrument
(`ceiling-defect-2026-09-17.md`). An unregistered pilot giving the control
its own loss term at quadrupled weight did not make it usable — 0.3125
against a bar of 0.60 that was pre-stated before the code existed
(`control-learnability-pilot-findings.md`). The clause is not repaired; a
successor grammar is a new registration.

**What A3 measured.** On three seeds trained from scratch, the primary
battery learned (intact 0.5683, 0.5633, 0.5738) and collapsed when the
ownership input channel was zeroed (0.1988, 0.2015, 0.1447), while the
syntax battery was unchanged and the state battery moved on one seed
(0.0769 on seed 2, below its locked threshold of 0.1172). All six scores
are means across six evaluation seeds, paired within seed, and every figure
in this paragraph is recorded at `seeds-endpoint-findings.md`. The
ownership input is load-bearing **for the primary battery**. The matched
contrast against a non-self control could not be run.

**What A3 did not measure.** Whether the network built an internal
structure around the ownership input — a center in the sense of something
the network acquired — is not testable with these instruments. The section
of the amendment that defines what is ablated (§3.1) says why: the
input-channel lesion removes a sense organ, not a structure the network
built. The registration concedes a second limit alongside it: attending
back to marked positions is a re-readable pointer rather than a carried
binding, both routes need the channel, and so the wire lesion cannot
separate them (`amendment-a3.md`, the file this block lands in, registration
revision 8 of 2026-09-15, "The central claim is narrowed").
The instrument the registration names as the discriminator for that
question, the mid-episode re-indexing probe, has never run (the red team
ledger's finding `RT-114`, which lists it among the registered discriminators
that have never fired).

Four localization runs bear on where ownership sits, and none of them
localizes it. A fitted linear classifier at eleven positions and five
layers found the register index — the four-way rank of the marker, not the
registered target itself — nowhere except where its marker is the input
(`fitted-position-sweep-findings.md`, with its sensitivity corrected at
`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`). A standardised
refit, a different estimator on the same states, found the same thing
everywhere but one cell (`standardised-refit-findings.md`): at the third
checkpoint, at the **other** agent's revision value, at layer 3, it crossed
the family bar by 1.94 episodes in four thousand — a margin computed in the
review of that run and not stated in its findings file (the red team ledger's
finding `RT-128`, which ruled that the number and its fragility travel
together or neither travels) — and is recorded as a sub-bar pattern measured
twice, not a clearance. The registered matched
control (§L2(a), the other-agent index) had its **probe half** run for the
first time, with rank matched by design and accuracy matched as observed;
it excluded the exclusion confound that had been proposed for that pattern,
while a purely relational encoding remains open as a route that would
produce both the pattern and this null (`other-index-position-sweep-findings.md`).
The control's **lesion half** — a localized other-agent subspace whose
ablation leaves the self-directed condition intact — remains unavailable,
because no such subspace was found and there is nothing to ablate; running
the probe half does not discharge the registered requirement. All the
rulings in this paragraph are the Gate B rulings of 2026-09-21 on the two
follow-up runs (ledger RT-120 to RT-142).

The registered probe target, the model's own marker word, has been read at
these positions only by the weaker difference-of-averages method, which
found it nowhere on either of its two arms across 270 tests
(`powered-position-sweep-findings.md`). Reading the registered target with
a sensitive instrument is one unrun job of about seventy processor-hours at
no money cost (both the price and the fact that the job was dropped before
that run rather than after it are recorded in the red team ledger's finding
`RT-89`), and until it runs, only the narrower sentence above is
available. Causal patching, which the section on how the ablation is
localized (§3.2) requires alongside the probe before anything counts as
localized or as absent, was never run and has no code for this design (the
ruling of 2026-09-20 that patching is new code rather than existing
machinery, ledger RT-96). Because the two instruments never converged on
any seed, no L1 subspace was ever localized, and so the registered
uncarvable signature H_diffuse was never reachable either: it requires a
subspace that beats the matched controls, and none was carved to compare.

**The registered term for the line is therefore *not testable
(localization)*, and the registered reading of this null is instrument
failure, not absence.** The registration reads "ownership is known to be
load-bearing and the instruments cannot find it" as a failure of the
instruments until causal patching has run, and that reading stands. What
can be said descriptively, and separately from it: these probes did not
localize this target at these positions, at a heuristic reach of roughly
one legible episode in eleven. What may not be said is that the structure
is absent, or that these nulls make it less likely, because every number in
these runs is conditional on this stack being able to recover a center that
is known to be there, and that has never been established on this design.
The registered blind-localization arm is the measurement that would
establish it. Its status is ruled: the 2026-09-16 blind run discharged the
registered arm and no re-run is scheduled
(`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, reconciling the
December-result ruling's item 3 with the step 4 ruling); the requirement it
serves is carried into the successor's rehearsal, and a re-run is a $0 side
item if a later session finds the 2026-09-16 run did not meet the arm's
registered target.

**Where this sits on the project's gradient.** Under the ruling of
2026-09-20 that a load-bearing self-index is a center
(`docs/rulings/2026-09-20-center-as-degree.md`), "center" has a second and
weaker sense than the one used above: a pointer that is causally
load-bearing for the act is a center at the bottom of the gradient, with no
requirement that the network built a structure to hold it. In that weaker
sense — and only in it — what the lesion measured puts these checkpoints
above zero. Their degree on the integration axis, how much of the act is
organized around the ownership signal rather than consulting it, is
unmeasured, because the metric for that axis (Stage 2) does not yet exist.
The sentence this experiment supports in public is: the ownership input is
load-bearing for the primary battery on three seeds; whether an internal
center formed around it is not testable here; its degree is unmeasured. No
result of A3 is described as "a structural signature of self-indexing" or
"a structural signature of ownership-specific learning".

**Successor.** A matched-role causal-interchange experiment with a
learn-both eligibility gate, whose purpose is to develop and validate the
Stage 2 degree metric on contrast cases known by construction
(`docs/competing-mechanisms-2026-09-20.md`). It registers in 2026 through
Gate A with both tiers, registration commit target 2026-10-11 and kill date
2026-10-18 (`docs/rulings/2026-09-20-december-result-roadmap.md`, item 1,
which carries all four of those facts and is what amends item 5 of
`docs/rulings/2026-09-20-center-as-degree.md`; item 7 of the same ruling
restates the 2026-10-18 date and adds a second one, that the registered runs
launch by 2026-11-01, with either date missed recorded as a schedule
failure). Three
things the successor inherits and must carry: measuring the control's
ceiling properly is a precondition of any successor amendment (John,
2026-09-17, `ceiling-defect-2026-09-17.md`); nothing counts as localized or
as absent until both instruments, probe and causal patching, agree; and the
successor's whole purpose is a measurement that does not yet exist, so the
rehearsal requirement — that a full measurement procedure be demonstrated
before it is registered — applies to it even though it does not apply to
this closure.

**Open items carried on this closure.** The instrument-sensitivity
requirement the blind arm served, carried into the successor's rehearsal
(the arm itself is discharged, above). The registered
probe target, the marker word, unread by a sensitive instrument at these
positions — deferred because reading it was priced at about seventy
processor-hours against about eleven for the register-index read done in its
place, and dropped before that run rather than because of anything the run
found (the red team ledger's finding `RT-89`); whether it runs before the
paper draft is one of the questions the ruling of 2026-09-20 on centers as a
matter of degree expressly leaves undecided
(`docs/rulings/2026-09-20-center-as-degree.md`, "What this ruling does not
decide"). Causal patching, unwritten and unrun. The mid-episode re-indexing
probe, the registered discriminator for pointer against carried binding,
unrun. The lesion half of the registered other-agent control, unavailable.
The relational-encoding route at the other agent's revision value, untested.

**Money.** Amendment A3 closed at ~$44.3 of its $100 hard stop, and the
programme at ~$225.7 of its $400 ceiling (`compute-ledger.md`, the running
totals on the rows dated 2026-09-19 and 2026-09-20).
