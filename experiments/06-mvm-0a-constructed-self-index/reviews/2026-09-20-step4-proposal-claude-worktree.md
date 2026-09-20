# Outside review — the step 4 proposal (Gate C, tier 1)

*Filed 2026-09-20 under the outside-review protocol, against the review
packet `2026-09-20-step4-proposal-packet.md`. Verbatim on filing and not
edited afterwards. Nothing here is a ruling; rulings are John's and go in
the red-team ledger (`red_team_ledger.md`). Written under the workspace
plain-language rule.*

## What was opened

Read in a fresh worktree off `main` at commit `1f9d2af`, which is also
what the shared repository's `main` points at, so nothing below rests on
an unpushed change. The packet's list, and then four things beyond it,
each disclosed here rather than left to be found.

**The packet's list, read as listed:**

- The proposal under review
  (`docs/step4-control-battery-proposal-2026-09-20.md`), in full.
- `separation-clause-requirements.md`, in full.
- `control-battery-proposal.md` (the 2026-09-17 options and the
  annotation that moots them), in full.
- `ceiling-measurement-findings.md` and `ceiling-defect-2026-09-17.md`,
  both in full.
- `control-learnability-pilot.md` and
  `control-learnability-pilot-findings.md`, both in full;
  `reviews/2026-09-20-control-learnability-claude-worktree.md` in the
  sections that bear on the proposal (the matched-seed finding, the
  step 4 recommendation, the ceiling precondition, the proposed
  status-file sentence and the kill case), plus its headings throughout.
- Part 4 of `reviews/2026-09-20-fitted-read-claude-worktree.md`, and its
  opening statement of what that reviewer opened and how it numbered.
- The ledger blocks: the control-learnability rulings (rows `RT-52` to
  `RT-69`) and the fitted-read rulings (rows `RT-70` to `RT-93`),
  including the preamble that records what John settled, plus row
  `RT-49`, which the proposal cites.
- Section 3.2 of `amendment-a3.md`, and `pre-registration.md` at the
  two-method requirement and the instrument-failure reading.
- `red-team-a4.md`: its opening, its glossary and its full summary table
  of the twenty-two findings. Not all 781 lines.
- `docs/public-path-roadmap-2026-09-16.md` in full, and the running
  totals in `compute-ledger.md`.

**Four departures, disclosed:**

1. **Sections 3.1 and 3.3 to 3.5 of `amendment-a3.md`.** Section 3.2
   says how a thing is located; section 3.1 says what the thing is, and
   section 3.5 names the outcome bins a localization result would land
   in. The proposal's central recommendation is about what patching
   would buy, which is unreadable without all three. The previous
   reviewer made the same call on section 3.1 and disclosed it.
2. **The loss conditions and the bin list in `pre-registration.md`.**
   The packet names two clauses of that file. The loss conditions sit
   two headings away and one of them is about this exact situation. It
   is quoted in finding `RT-107`.
3. **The kill case and the ordered next steps at the end of the
   fitted-read review.** The packet names part 4. The ordered next steps
   are that reviewer's answer to "what should run, in what order", which
   is the question the proposal's recommendation turns on.
4. **File and directory names only — no file contents.** I listed
   `src/`, listed `a3-gates/`, ran one repository-wide search for files
   whose names contain "patch" or "lesion", and ran one listing of what
   git tracks. This was to answer a question the packet's brief asks
   directly and that no document in the review set can answer: whether
   the code causal patching needs exists. No source file was opened.

**Not opened, as instructed:** the current-state file (`STATUS.md`), any
chat transcript, any uncommitted file. Also not opened, and it leaves a
gap: the outside-review protocol itself (`docs/outside-review-protocol.md`),
which is what defines Gate A, Gate B and Gate C. The proposal asks John
to send its closure text through Gate A. I cannot check what that
involves or how long it takes, and I say so again in part 3.

**Two gaps the list creates.** The proposal's arithmetic about the pilot
rests on records under `a3-gates/` that the packet does not list, so
where I check a number I check it against the findings files that quote
it, not against the machine record. And the reference solvers behind the
ceiling of 1.0 are code I did not read; I take the 2026-09-17
measurement as the record states it.

No outside lookup was used. Every number below comes from a committed
document in this repository or from arithmetic I did on those documents.
Each finding is labelled **MEASURED** or **ARGUED**.

## Ledger numbering

The packet says to continue from `RT-93`. The ledger's last row is
`RT-93`. I number from **RT-94**.

## Verdict in one line

**The proposal reads the record accurately and reaches the right
destination by a route that does not exist.** Every number in it
reproduces, it carries the rulings it was told to carry, and its case for
closing Amendment A3 rather than redesigning the grammar is sound. But
the thing it asks John to authorise — causal patching, run now, free, on
the checkpoints in hand — has no code, no target, and cannot produce
either of the two outcomes the proposal promises it will produce. And the
sentence it offers the paper, "a structural signature of
ownership-specific learning", is the one claim the registered text says
this experiment's surviving result cannot support.

---

# 1. Feasibility

*Every claim the proposal makes about the record: is the tier reading
right, is the ceiling carried correctly, is causal patching really free
and local with code that exists, do the dates hold. The brief says a
claim with no record behind it is fatal.*

| # | finding | severity | label |
|---|---|---|---|
| RT-94 | the tier reading is correct, uses the rule that was pre-stated before the pilot reported, and survives every other way of taking the spread | worth-noting (credit) | MEASURED |
| RT-95 | the ceiling of 1.0 and the arithmetic that makes the registered comparison undefined are both carried correctly | worth-noting (credit) | MEASURED |
| RT-96 | causal patching is not "free and local with existing code": no patching code exists for this design, and the warrant the proposal offers is for a different operation | **fatal** | MEASURED |
| RT-97 | the money is right — the remaining headroom reproduces from the ledger to the cent | worth-noting (credit) | MEASURED |
| RT-98 | every date holds against the approved roadmap; one of them is described in words no reader outside this workspace could decode | worth-noting | MEASURED |
| RT-99 | the proposal omits a registered, unconditional, free step that the approved roadmap puts a week before the decision it is written for | serious | MEASURED |
| RT-100 | "the two open free closures (three numbers)" miscounts, and one of the three had a deadline that has already passed unmet | serious | MEASURED |
| RT-101 | "two follow-up runs authorised" is exactly right, and the free paired check the last review asked for before this proposal cited the pilot was not done | worth-noting | MEASURED |

### RT-94 — the tier reading is correct, and correct under every reading of the spread

**Worth-noting, and it is credit. MEASURED.**

The proposal says the pre-stated tiers make a separation clause
registerable only if the control battery's intact score, mean minus one
spread, reaches 0.375; that the pilot read 0.3125 with a spread of
0.0240; and that this puts 0.2885 against the bar. The subtraction is
right and every input is on the record.

More to the point, the rule it uses is the rule that was written down
first. The requirements document says, in the paragraph that sets the
tiers: "Where a threshold is compared against a mean, use the mean minus
one spread, so that a lucky draw does not clear a bar." The proposal
applies that sentence exactly, and applies it in the direction that is
harder on the programme's own hopes.

It is worth adding what the proposal does not say, because it makes the
reading stronger rather than weaker. John's ruling on the pilot review
(`RT-63`, the row about the wrong spread) held that a single draw's
spread is not the uncertainty of a scored mean. That objection would
apply here too — except that it changes nothing. The mean alone is
0.3125, which is 0.0625 below the bar; the tier holds whether you
subtract a spread, subtract the uncertainty of the mean, or subtract
nothing at all. The pre-stated rule and every alternative to it give the
same tier.

**A requirement met that nobody asked about.** The tiers also say they
are read against intact scores "measured the way the endpoint reads are:
at least 800 episodes, at least six independent evaluation seeds, mean
and spread reported." The pilot reported six evaluation seeds at 800
episodes with mean and spread. The measurement the tier rule demanded is
the measurement that was taken.

### RT-95 — the ceiling is carried correctly, and so is what it does to the registered comparison

**Worth-noting, and it is credit. MEASURED.**

The proposal's first settled point says the control battery's true
ownership-blind ceiling is 1.0, so under the registered floor rule its
drop is undefined at every possible score, and the registered comparison
has been unsatisfiable since registration. Each clause checks out against
the 2026-09-17 measurement: the floor rule needs baseline minus ceiling
of at least 0.10, a ceiling of 1.0 therefore needs a baseline of 1.10,
and accuracy cannot exceed 1.0.

Its fifth settled point adds that even under the old reference score of
0.3227 the control needed 0.4227 for its drop to be defined, so the whole
band a rerun could land in changes nothing. That is the argument John's
ruling on the pilot review (`RT-53`, the row about the superseded floor
rule) said the step 4 proposal should make, and it is made. The pilot's
six evaluation draws ranged 0.2850 to 0.3460, so the highest single draw
is still 0.077 below 0.4227 — the band claim is not just argued, it is
bounded by the measured range.

**One distinction the proposal keeps and should keep.** The 0.4227 bar
belongs to the registered comparison, which divides by a ceiling. The
0.375 bar belongs to a separation clause, which does not. They are
different bars for different instruments, and an argument from one is not
an argument about the other. The proposal states each in its own place
and never uses the dead clause's bar as an argument against the grammar
redesign. That is the right handling and it would have been easy to get
wrong.

### RT-96 — causal patching is not free, local and already built

**Fatal. MEASURED.**

This is the finding that matters, because the recommendation rests on it.
The proposal says:

> Running it on the existing checkpoints is local and $0 (the lesion
> machinery exists) and turns "not testable (localization)" into either a
> localized result or a registered null with both instruments.

Three things are wrong with the parenthesis and one of them is fatal on
the brief's own rule.

**First, a lesion is not a patch.** A lesion removes something and looks
at what breaks. Causal patching takes a piece of one run's internal state
out of an episode where the model is one agent, puts it into the matched
episode where it is a different agent, and reads what the model then
does. The registered text is explicit that these are separate methods and
that both are required: section 3.2 lists probes as step one, patching as
step two, and then says "the two-method requirement is met by probe plus
patching". Offering the existence of removal machinery as evidence that
transplant machinery exists is a change of subject.

**Second, the record in the review set says the opposite.** The
fitted-read review states, of the code it and its predecessor were given:
"The previous review checked all six code files it was given and found no
intervention of any kind; I have checked the one code file I was given
and it is the same... Nothing in this run changes a model's computation
and then looks at what the model does."

**Third, and this is the measurement.** I listed the file names in this
experiment's source folder. There are fifty files. None of them is
a patching script — the localization pipeline is there
(`localize_a3.py`), the removal lesion is there (`lesion_register.py`),
the null calibration, the sweeps, the probes and the diagnostics are all
there. A repository-wide search for file names containing "patch" returns
patching code in exactly one place: Experiment 1's source folder
(`experiments/01-self-indexing-removal-test/src/patch_context.py` and
`cross_patch_self.py`). That is the code section 3.2 points at, and it
points at it as a *pattern*: "Experiment 1's localization stack is reused
**where it transfers**."

Whether it transfers is the whole question, and it has never been asked.
Experiment 1 ran on a different model, a different vocabulary and a
different grammar; it was a register-bearing design, and this one has no
register by construction (section 2.4). Porting activation-transplant
code across that gap is the same shape of job as the two calibration
substrates that could not run, which the A4 red team found fatal (`F15`):
they failed on a tokenizer whose ids differed on 72 of 105 tokens. That
finding is why the requirements document carries a standing rule, in
bold: "A substrate is named in a clause only after a dry run has shown it
loads and scores on the design's batteries."

**So the answer to the brief's question is: it needs something that does
not exist.** Not something impossible — writing the patching path for
this design is ordinary work, and it is probably a day rather than a
week. But it is new code on a registered instrument, and the proposal
asks John to authorise it as a free item that is already built. The brief
says a claim with no record behind it is fatal, and this is the claim the
recommendation is carried by.

**To be fair to the proposal on one point.** Nothing about the
checkpoints being register-less blocks patching in principle. The
registered target is a low-rank direction in the residual stream, not a
register, and a residual direction can be transplanted in a model that
has no register at all. The brief asks whether register-lessness is a
reason patching cannot run and the honest answer is no. What blocks it is
the absence of the code and, separately, the absence of anything to patch
(`RT-103`).

### RT-97 — the money is right

**Worth-noting, and it is credit. MEASURED.**

The proposal puts the remaining room under the hundred-dollar stop at
$55.7. The ledger's last two rows give the pilot at about $9.9, taking
the running total to about $44.2, and the checkpoint recovery at $0.067.
A hundred minus $44.2 minus $0.067 is $55.73. The ledger's own row says
"leaving ~$55.8" and then, in the same sentence, "leaving ~$55.5" — two
different figures from a mid-sentence correction. The proposal's $55.7 is
the one that actually follows from the numbers, so it is not merely
copied across, it is right where the source is muddled.

The redesign's price, three seeds at $27 to $39, is also consistent with
what seeds have measured: the A3 pilot billed $13.92, and seeds 1 and 2
billed $20.1 the pair. Three more at the measured rate lands inside that
band. What the band leaves out is dealt with at `RT-106`.

### RT-98 — the dates hold, and one of them is written in private language

**Worth-noting. MEASURED.**

Every date in the recommendation checks against the approved roadmap: the
decision on 2026-10-04 (step 4), the paper draft on 2026-10-25 (step 6),
the outside reader on 2026-11-08 (step 7), public release on 2026-11-22
(step 8). None is misquoted and the ordering argument built on them is
fair.

The last one is not a date problem but a language problem, and the
workspace rule is explicit about it. The proposal writes: "The release
date is 2026-11-22 and **the pipeline resumes** 2027-01-04." The
roadmap's own line is "SERE pipeline starts 2027-01-04", under
constraints about what must be finished before then. A reader of this
document — including John in three months, and certainly the outside
reader at step 7 — will read "the pipeline" as something in this
programme: the training pipeline, the localization pipeline, the compute
pipeline. It is none of those. It is John going away to a military school
and the research stopping. The plain sentence is "John's military
training starts 2027-01-04 and the work stops until it ends", and the
argument is stronger for saying so, because a hard stop on the researcher
is a much better reason not to open a new registration than a vague
resumption.

### RT-99 — the registered arm the proposal does not mention

**Serious. MEASURED.**

The approved roadmap's step 3 reads:

> Blind-localization arm (registered, unconditional): run blind on one of
> the five A2 register-bearing 30M checkpoints, local, $0. The A3 L1
> pipeline does not discharge it — **2026-09-27**

It is registered. It is unconditional. It is free. It is local. It is
scheduled for one week before the decision this proposal is written for.
The proposal does not mention it anywhere — not in what has been settled,
not in the options, not in the reasons, not in what the proposal does not
decide.

That matters more than a missing cross-reference, for three reasons.

**It is the registered test of the thing the proposal is worried about.**
The pre-registration says of this arm: "ask whether the instruments
recover a center known-by-construction to exist and to be load-bearing...
if the instruments cannot recover a center that is known to be there,
Experiment 1's null was instrument failure." The whole difficulty with
the localization line right now is that nobody can tell an insensitive
stack from an absent signal. This arm is the registered instrument for
telling them apart, and the requirements document asks for exactly this
before money is spent on a localized lesion: "a positive control the
stack recovers".

**The registration ranks it above the headline.** The pre-registration's
decision list says the blind arm is "alongside and unconditional" and
"may be worth more than the headline". Its correction at `RT-12` says
"Only the blind-localization arm speaks to Q1, and it speaks to it
directly."

**It competes for the same hours.** It is free in dollars and it is not
free in the one resource the proposal's own argument is about, which is
calendar time before 2026-10-25. See `RT-108`.

**One qualification I owe.** A findings file for a blind arm and a
machine record for it both exist in this repository by name
(`blind-arm-findings.md`, `a3-gates/blind_arm_seed0_full.json`). I did
not open either, so I cannot say whether step 3 is already discharged, or
partly, or not at all. That is precisely the problem: the document that
tells John what stands between here and closure does not say either.

### RT-100 — three numbers for two items, and a deadline already missed

**Serious. MEASURED.**

The proposal's fourth ruling request reads: "Either way: the two open $0
closures from the pilot review (RT-56, RT-58, RT-59) land before the
closure text is drafted."

Two problems, and the second is the one that matters.

**It names three rows and calls them two.** In the ledger, the row about
the fixed positional split (`RT-58`) and the row about the untested
one-token assumption (`RT-59`) are both marked "ACCEPTED, CARRIED OPEN"
with a free closure attached. The row about the missing training log
(`RT-56`) is marked "ACCEPTED" and is not carried open. So there are two
open closures and they are `RT-58` and `RT-59`. Whether `RT-56` was meant
to be in the list or the count was meant to be three, one of the two is
wrong.

**John's deadline for the third one has already passed, unmet.** The
ruling on `RT-56` says, in bold: "**Closure:** commit both beside the
endpoint record **before the step 4 proposal is filed**." The step 4
proposal is filed — it is the document under review. I listed what git
tracks. The control pilot's two endpoint records are committed
(`a3-gates/endpoint_a3ctl_30m_seed0.json` and the partial one at step
51,500). There is no training log and no trajectory record for that run
anywhere in the repository; the only trajectory file in that folder,
`pilot_trajectory.jsonl`, belongs to the 2026-09-15 A3 pilot, which is a
different run.

So the proposal quietly moves a ruled deadline. John said "before the
step 4 proposal is filed". The proposal says "before the closure text is
drafted", which is later, and does not say that the earlier deadline went
by. This is small in substance — two files — and it is exactly the
category of drift the previous review was praised for finding none of
(`RT-93`, nineteen rulings and no drift). A proposal that carries a
ruling forward with its deadline relaxed and the relaxation unremarked is
how the count starts again.

### RT-101 — "two follow-up runs authorised" is right; the free paired check was not done

**Worth-noting. MEASURED.**

The proposal's closing section says the linear-read line is "parked, two
follow-up runs authorised 2026-09-20". That is exactly right, and it
would have been easy to get wrong: three cheap runs were put to John and
he authorised two of them — the other-agent index control and the
standardised refit — and deferred the third, the marker-word target under
the fitted read. The count, the date and the parking are all faithful to
the ledger.

Against that, one thing the pilot review asked for specifically, aimed at
this document, was not done. Its matched-seed finding (`RT-62`, the row
John ruled fatal) closes: "It costs nothing and should be done before the
step 4 proposal cites this run." The "it" is taking the difference
between the two checkpoints *within each evaluation draw* rather than
between two six-draw means, which removes the item-set variation from
both sides and would tighten the estimate of what the reweighting
actually bought. The proposal cites the run and quotes the between-means
figure — the move of about 1.6 standard errors, which I checked against
the ledger row and which reproduces exactly. It does not report the
within-draw comparison and does not say why not.

Nothing turns on it for the tier, because the distance to every bar that
matters is many times the difference between the two estimates. It is
recorded because a free check that a fatal-rated row asked for, timed
explicitly to this document, went unmentioned in it.

---

# 2. Satisfied by the wrong thing

*Every way the recommendation — close Amendment A3, run causal patching
first, defer the grammar redesign — could be the wrong call even if every
fact in it is right.*

| # | finding | severity | label |
|---|---|---|---|
| RT-102 | patching cannot produce either of the two outcomes the proposal says it produces; both need runs the proposal does not schedule | **fatal** | ARGUED |
| RT-103 | patching has nothing to patch: the registered method patches a subspace the probes have never found, and the proposal never says what would be transplanted | serious | ARGUED |
| RT-104 | the swap probe is counted as a separate prize when the registered text says it *is* the patching step | worth-noting | MEASURED |
| RT-105 | the order is inverted against the review John ruled on the same day, which put patching last of six | serious | MEASURED |
| RT-106 | the redesign is priced at three runs when this programme has never run a wave without a learnability run first, and the cheaper redesign in the review set is not the one costed | serious | ARGUED |
| RT-107 | the closure text cannot be honest without naming a registered bin, and there is a pre-registered loss condition about this exact situation that the proposal never cites | serious | MEASURED |

### RT-102 — neither promised outcome is reachable

**Fatal. ARGUED, from registered text and ruled ledger rows.**

The proposal's third reason says patching "turns 'not testable
(localization)' into either a localized result or a registered null with
both instruments." Take the two halves in turn.

**"A localized result" is not reachable.** Section 3.2's fourth step is a
requirement, not a preference: "L1 counts as localized only when probe
and patching agree on a confound-controlled design; otherwise the outcome
is *not testable (localization)*." Agreement needs both to find
something. The probe leg has found nothing. The fitted classifier read
the register index at eleven positions, five layers, three checkpoints,
and found it nowhere except the token where the model's own marker is the
input. The registered target — the model's own marker word — has never
been read at the nine positions by a fitted read at all, and the run that
would do it is the one John deferred. So patching cannot agree with a
probe finding, because there is no probe finding to agree with. Running
patching alone cannot move the line to "localized" no matter what it
returns.

**"A registered null with both instruments" is not reachable either.**
The registered bin for a two-instrument null is `H_diffuse`: "L0
collapses T_act (ownership is load-bearing) but **no L1 subspace at k ≤
16 beats the L2 controls**, and probe-patching convergence fails." The
clause in bold is the problem. The matched controls are named in section
3.1 as L2, and L2(a) is the other-index subspace — the one localized for
a named non-self agent, matched in rank and probe accuracy. It has never
been run. John authorised it on 2026-09-20 (`RT-82`) and it has not run
yet. Until it does, "no subspace beats the L2 controls" is not a
statement anyone can make, so `H_diffuse` is not a bin this result can
land in.

And underneath both, the pre-registration's reading stands and was ruled
on twice (`RT-50`, `RT-92`): a null from instruments applied to a centre
known to be load-bearing is read as instrument failure, not as absence.
Two instruments failing is still instruments failing. Converting that
into a registered null needs the positive control the requirements
document asks for — "a positive control the stack recovers, on this
design, not a synthetic one" — and that control does not exist either.

**So the recommendation's third reason, which is the reason it says
carries the most weight after the calendar, promises two destinations and
can reach neither.** What patching alone would actually buy is real but
much smaller: it discharges one of the two methods the registration
names, so that the sentence "not testable (localization)" is true for a
narrower reason than it is true for today. That is worth having. It is
not what the proposal tells John he is buying.

### RT-103 — there is nothing to patch

**Serious. ARGUED.**

Section 3.2's patching step is written against a specific object: "patch
**the L1 subspace** from an episode in which the model is agent A into
the matched episode in which it is agent B and read the revision action."
L1 is defined in section 3.1 as "a low-rank subspace of the residual
stream, localized as in §3.2". So the method patches the thing the probes
found.

The probes have found nothing. The requirements document states it
flatly: "The stack has found nothing on any seed, and the known-answer
test validates the plumbing but not the ablation path."

That leaves whoever writes the patching method a choice nobody has made:
patch the whole residual stream at a position, patch the one candidate
the last review surfaced (the other agent's revision value, positive in
fifteen tests of fifteen but short of the family bar), patch a direction
from the difference-of-means read, or patch a subspace defined some other
way. Each is a different experiment with a different null and a different
claim. The proposal asks John to authorise "the causal-patching design as
a $0 local item, method committed before output" without saying which of
these it is — and the choice is not a detail, because a patch target
chosen after the probes came back empty is a design decision made with
the data in hand, which is the move this programme's whole procedure
exists to prevent.

**The honest version of the request** is: authorise the design of a
patching method, which will have to state its target and its null before
it runs, and which cannot inherit a target from the probe stack because
the probe stack has none.

### RT-104 — the swap probe is the patching step, counted twice

**Worth-noting. MEASURED.**

Describing option A, the proposal says: "The discriminators that do not
need the control (the matched other-agent lesion, the random matched
subspaces, **the swap probe**) run through the localization stack, which
is parked... so A is honest and thin unless patching runs too."

The swap probe is not a discriminator that patching unlocks. It is
patching. Section 3.2, step two, after describing the transplant: "This
is also the **swap probe** of RT-01, re-aimed at an acquired structure."

So the list of what A lacks contains patching's own output as a separate
item alongside patching, which makes the case for running patching look
broader than it is. Two of the three named items are real and distinct —
the matched other-agent lesion (which is L2(a), and needs a localized
subspace it does not have, per the A4 red team's `F14`) and the random
matched subspaces (which are a null, not a discriminator, and which the
Gate 0 machinery already produces).

**One item in that sentence is not blocked at all.** Section 3.1 lists a
third matched control, L2(c): "on the five existing register-bearing
checkpoints only, the register lesions already run, as a $0 reference."
Those lesions have run; their records are in this repository. Saying the
discriminators "run through the localization stack, which is parked"
sweeps in one that does not and one that has already happened.

### RT-105 — the order is inverted against the review ruled the same day

**Serious. MEASURED.**

The fitted-read review, filed 2026-09-20 and ruled by John the same day
with "agreed on all", ends with an ordered list of what to do next. Its
order is: (1) the other-agent index at the eleven positions; (2) the
marker-word target under the fitted read; (3) the standardised refit; (4)
correct the sensitivity figure; (5) report consistency across layers in
future sweeps; (6) **causal patching** — "Already the binding open item
and already on the 2026-10-04 control-battery decision. Nothing above
substitutes for it."

The proposal takes item six and makes it the operative instruction, and
puts items one and three — the two John authorised — into the closing
paragraph of things this proposal does not decide, described as a parked
line.

That is backwards, and not only as a matter of deference. Items one and
three are the runs that could give patching a target. The other-agent
index is described by that reviewer as "the cheapest decisive measurement
available"; the standardised refit "separates 'not linearly present' from
'not reachable under this penalty'". If either turns up a candidate
subspace, patching has something to transplant and the convergence rule
can actually be applied. If neither does, patching is a method with no
target, which is `RT-103`.

"Nothing above substitutes for it" is true and the proposal is right to
carry it. It does not mean "do it first". It means "doing the others does
not let you skip it".

### RT-106 — the redesign is under-priced, and it is not the cheapest redesign on the record

**Serious. ARGUED.**

Two separate problems with how option D is costed, and the brief asks
about a cheaper version specifically.

**The price is three runs when this programme has never run three without
a fourth.** The figure of $27 to $39 is inherited unchanged from the
2026-09-17 proposal, where it meant three retrained seeds. But a grammar
redesign is a new design, and every wave in this programme's ledger ran a
learnability run before the seeds: Gate 2 was the A3 learnability pilot
at seed 0 ($13.92), and only after it reported did seeds 1 and 2 launch
as one wave ($20.1 the pair). The amendment's own procedure order works
the same way. So the realistic figure for option D is four runs, about
$40 at the measured rate, plus whatever the re-freeze costs — and the
re-freeze is named as a cost three times in the proposal and priced at
zero every time. On the record, re-freezing is local and free in dollars
(Gate 1 ran locally at $0) but it is not free in hours, which is the
currency the proposal's own argument is denominated in.

This does not overturn the recommendation. Forty dollars still fits
inside $55.7. It matters because the proposal offers the headroom figure
as the reassurance that money is not the constraint, and a reader who
later finds the real number is $40 plus an unpriced re-freeze against
$55.7 will trust the next estimate less.

**The cheaper redesign is the one that fixes both defects, and it is not
the one costed.** The proposal's option D teaches plain name-keyed
retrieval before layering the rule on top. That addresses one of the
three non-supervision explanations — the proposal says so honestly: "D
addresses only the first of them directly."

The requirements document contains a different grammar change, ranked
first of three ways to satisfy the second hard requirement: "**An
other-directed action at an own enacted turn.** Add to the grammar a turn
on which the model acts on *another agent's* commitment... That is an
action, read at an injection site, requiring name-keyed binding and no
ownership. It gives a comparator matched in position, in read type and in
rule, with only whose commitment differs."

That change costs the same three-or-four runs and the same re-freeze, and
it fixes the position mismatch that the A4 red team called fatal (`F2`) —
the defect that no amount of teaching retrieval touches. It also
plausibly fixes the learning problem for free, because it gives the
control battery the same private route through the acting channel that
the primary battery has, which is one of the three explanations the pilot
left standing.

So when the proposal says D "buys: a control battery that can reach Tier
A or B, and with it a separation clause meeting H1 to H6", that is
over-claimed for the D it describes. D as written could satisfy the first
hard requirement and would still fail the second, and a clause cannot be
registered that fails any one of them. The requirements document says so
in its own words: "A clause that fails any one is not registerable,
whatever the pilot shows." If John is to be offered a redesign at all, he
should be offered the one that could actually end with a registerable
clause.

### RT-107 — the registered words for this outcome exist, and the proposal uses different ones

**Serious. MEASURED.**

The proposal asks John to send the closure text through Gate A because it
is registered text. Registered text has to land in a registered bin, and
there is a clause in the pre-registration about this exact situation that
the proposal never cites. It sits under the heading "Loss conditions
(what would retire or rebuild this experiment)":

> No non-self cross-turn control can be built that is state-requiring at
> ceiling — then the differential discriminator is dead here and the
> honest report is "not testable" [RT-05].

Whether that condition has fired is John's call and I am not making it.
The case that it has is strong: the 2026-09-17 measurement did not find
that this particular control failed to learn, it found that an
ownership-free control and a ceiling-corrected metric "are incompatible
by construction, not by accident". That is a statement that no control of
this kind can be built for this metric, which is the loss condition in
its own terms. The case that it has not is that the control *was* built
and does carry a cross-turn binding demand; what failed is the model
learning it and the metric reading it.

Either way, the proposal should have put the clause in front of him. Two
consequences hang on it.

**The registered name for the outcome may be "not testable", not
"closed".** The requirements document's own Tier C wording is "the
matched contrast remaining unmet", which is a description rather than a
bin name. The pre-registration's bin list and the amendment's bin list
both carry "not-testable". If the loss condition has fired, the
registered report is a not-testable verdict on the differential
discriminator, and "close Amendment A3 with partial discriminators" is a
softer sentence for the same fact.

**A loss condition says "retire or rebuild", which is the A-versus-D
question.** The heading is not decorative. The clause that covers this
situation is one of the clauses that were written, before any money was
spent, to say when the experiment should be rebuilt rather than reported.
A proposal recommending report-and-close should say why that clause does
not point the other way.

---

# 3. No verdict

*Every way step 4 could be ruled on this proposal and still leave the
programme unable to return a verdict or close Amendment A3 cleanly by
2026-11-22.*

| # | finding | severity | label |
|---|---|---|---|
| RT-108 | "$0" hides a queue of local runs that the proposal's own calendar argument would rule out if it were applied to them | serious | MEASURED |
| RT-109 | the proposal asks for three gates on the patching work and schedules none of them | serious | ARGUED |
| RT-110 | the proposal never says what the closure text says if patching returns nothing, which is the likely case | serious | ARGUED |
| RT-111 | if John rules A but declines the patching item, nothing in the proposal says what closes Amendment A3 | worth-noting | ARGUED |
| RT-112 | the linear-read line cannot be honestly retired without the run John deferred, and closure needs a sentence about it either way | worth-noting | MEASURED |

### RT-108 — free in dollars, expensive in the currency the argument is about

**Serious. MEASURED for the hours, ARGUED for the queue.**

The proposal's first and heaviest reason against the grammar redesign is
the calendar: the redesign "does not fit without moving the release." Its
third reason recommends patching because it is "local and $0".

Those two reasons are denominated in different currencies, and the second
one is spent in the first one's coin. Local runs in this programme take
about half a day each. The fitted sweep's three elapsed times "sum to
10.76 hours against an estimate of six and a half" — that is in the
ledger row John ruled on (`RT-72`), and it is a measured overrun of two
thirds on a run of this exact shape. The other-agent index and the
standardised refit are each priced by that reviewer at "the same eleven
processor-hours". The marker-word read is priced at about seventy.

Set against 2026-10-25, when experiment 06 folds into the paper draft,
the queue that would have to clear is: the other-agent index (about
eleven hours, authorised), the standardised refit (about eleven hours,
authorised), the blind-localization arm (registered, unconditional, due
2026-09-27, unpriced in hours), the patching work (new code, then a run
of at least the same order), and — if the linear-read line is to be
honestly retired rather than parked — the marker-word read at about
seventy hours, which is the one John deferred.

None of that costs a dollar and all of it costs the thing the proposal
says the redesign cannot have. The proposal prices the redesign's
calendar in detail, over four clauses, and prices its own at nothing. A
reader applying the proposal's own standard to its own recommendation
would have to ask whether patching fits either.

### RT-109 — three gates requested, none scheduled

**Serious. ARGUED.**

The proposal's own ruling requests attach three procedural steps to the
work it recommends: the patching design is to be "method committed before
output, with its own Gate B", and "the A3 closure text goes through Gate
A (it is registered text)". A Gate B pass in this programme is a
context-isolated review session that produces a findings file, ledger
rows and John's rulings; the two that ran on 2026-09-20 produced
forty-two ledger rows between them and took a day each to rule.

So the sequence the proposal is actually requesting is: write the
patching method and commit it; run it; write findings; commission and run
a tier 1 review of those findings; rule the ledger rows; draft the
closure text; take the closure text through Gate A; then fold everything
into the paper draft on 2026-10-25. The decision itself is 2026-10-04.
That is three weeks for a code-writing job, a run, a full review cycle
and a registered-text gate.

I cannot check how long Gate A takes, because the protocol that defines
it is not in the review set (see "What was opened"). That is itself worth
saying to John: the proposal commits the closure text to a gate whose
cost neither the proposal nor this review has priced.

### RT-110 — what the closure text says if patching finds nothing

**Serious. ARGUED.**

On the record, the likely result of patching is nothing. The probes found
nothing at nine positions on the recoded target. The one pattern that
looks like anything sits at a position where the A4 red team's confound
(`RT-82`, the other agent's marker having just been named) has never been
excluded. And the requirements document says in terms that the stack's
sensitivity has never been established on this design.

The proposal does not say what the closure text says in that case. It
says patching "turns 'not testable (localization)' into either a
localized result or a registered null with both instruments", and
`RT-102` above shows it turns it into neither. So the realistic outcome
of ruling A-with-patching is: three weeks later, the line is still *not
testable (localization)*, for a slightly better reason, and the closure
text says what it would have said on 2026-10-04.

That is not an argument against running patching. It is an argument that
the proposal should have stated the likely outcome and shown that the
closure text is acceptable under it — which is the discipline the
requirements document imposes on clauses ("The clause must state its
*expected* value from whatever seen record exists, and what result would
surprise") and which a closure proposal should hold itself to as well.

### RT-111 — if the patching item is declined, nothing closes

**Worth-noting. ARGUED.**

The proposal's recommendation is "A, with causal patching run before
closure". Its own assessment of A without patching is "A is honest and
thin unless patching runs too". Its ruling request splits them: item 1 is
A or D; item 2 is the patching authorisation, conditional on A.

So John can rule A and decline item 2 — reasonably, for instance on
`RT-96`, because the code does not exist and the request was made as
though it did. The proposal does not say what happens then. There is no
fallback closure path, no statement of what the paper claims under a thin
A, and no alternative use of the three weeks. Given that item 2 is the
part of the recommendation this review finds unsupported, the missing
fallback is the branch most likely to be taken.

### RT-112 — the deferred run and the closure sentence

**Worth-noting. MEASURED.**

Closure text has to say something about the linear read, and the ruled
position is narrow. The registered target is the model's own marker word;
no fitted read has ever been run on it at the nine positions; the only
read that has been run there on that target is the difference-of-averages
read, which the fitted run measured as recovering five to nineteen times
less. That is `RT-89` in the ledger, rated fatal to the sentence it
killed, and John deferred the run that would fix it.

The consequence for step 4 is simple and the proposal does not draw it: a
closure written before that run cannot say the linear read found nothing,
only that a fitted classifier did not find a four-answer recoding of the
target. Whether that sentence is good enough for the paper is a John
question, and it belongs in a closure proposal.

---

# 4. Over-reading

*What "close A3 with partial discriminators" will be read as claiming;
whether the framing of the grammar redesign is right; and what the
recommendation should be.*

| # | finding | severity | label |
|---|---|---|---|
| RT-113 | "a structural signature of ownership-specific learning" is the one claim the registered text says the surviving result cannot support, and it is the claim the proposal hands the paper | **fatal** to that sentence | MEASURED |
| RT-114 | "partial discriminators" will be read as "some discriminators fired"; none has | serious | MEASURED |
| RT-115 | the framing of the grammar redesign as a different question rather than more supervision is right, and is exactly what the last review asked for | worth-noting (credit) | MEASURED |
| RT-116 | the proposal writes bare ledger numbers with no plain phrase, against the house rule, in the one section John has to act on | worth-noting | MEASURED |
| RT-117 | the recommendation I would put in front of John, which differs | — | ARGUED |

### RT-113 — "structural" is the word the registration reserves for the result that does not exist

**Fatal to that sentence. MEASURED.**

Describing what closing Amendment A3 lets the paper claim, the proposal
says: "a structural signature of ownership-specific learning in small
constructed models, with the matched contrast unmet." Both load-bearing
words are ones the registered text withholds from the result that would
survive.

**"Structural".** The only damage the programme can currently read is the
input-channel lesion, and the amendment says what it is worth, in its own
voice: "L0 is a *validity check and an upper bound*, not the verdict... It
is **not evidence of an acquired center, because it removes a sense
organ, not a structure the network built**." The registration's later
revision concedes the same limit again — "the wire lesion cannot separate
a carried binding from a re-readable pointer". The requirements document
restates it a third time under Claim 1: "It is still a statement about an
input... No comparator fixes that, because the two accounts predict the
same behaviour under input removal."

A structure the network built is `H_self-location`, and the requirements
document says the name is reserved: "H_self-location stays reserved for
the localized result." Under option A there is no localized result. So
"structural signature" is the reserved claim, arrived at by adjective.

**"Ownership-specific".** The A4 red team's second finding was rated
fatal against exactly this reading: the primary score is read at the
positions the lesion strikes and the control score is read at an appended
question far from them, so "a disruption that is local to the altered
positions and carries nothing about ownership therefore satisfies the
clause". That defect is a property of the design, not of any clause, and
closing the amendment does not repair it. The requirements document gives
the sentence that *is* available, and it is deliberately flatter: "the
ownership input is specifically load-bearing for the self-directed
condition."

**This is bigger than the proposal, and that is why it has to be said
here.** The approved roadmap's step 8 states the public claim scope as "a
structural signature of self-indexing in small constructed models", and
the proposal's closing section lists that scope as "unchanged". If option
A is ruled, the word "structural" in the approved scope stops being
supportable, and the one document whose job was to tell John what closure
costs him says the scope is unchanged. The honest claim after a
close-with-no-localization is something like: *in small constructed
models, an ownership signal can be made load-bearing for an
ownership-conditioned action, and our instruments could not find a
structure carrying it.* That is a good result and a publishable one. It is
not the one on the roadmap.

### RT-114 — no discriminator has fired

**Serious. MEASURED.**

"Close Amendment A3 with partial discriminators" invites the reading that
some of the discriminators worked and some did not. Going through the
registered list:

- **The matched other-agent lesion** (L2(a)). Never run. Needs a
  localized subspace that does not exist (the A4 red team's `F14`);
  authorised as a probe-side run on 2026-09-20 and not yet done.
- **The random matched subspaces** (L2(b)). These exist and run — but
  they are the null the other conditions are read against, not a
  discriminator that can fire.
- **The swap probe.** Never run; it is the patching step (`RT-104`).
- **The mid-episode re-indexing probe**, which the amendment registers as
  the discriminator for the tag bin. Never run.
- **The register lesions on the five register-bearing checkpoints**
  (L2(c)). Run, and registered as "a $0 reference", not as a
  discriminator for this result.

So the count of registered discriminators that have produced a result
bearing on the A3 claim is zero. "Partial" describes the coverage
correctly only if it is read as "a small part of none". What is actually
partial is the *result set*: a primary result that replicates on three
seeds, an instrument audit, and a comparison that was never computable.
The proposal describes all three accurately in the body of option A. It
is the label that over-claims, and the label is what survives into a
summary table — which is the A4 red team's finding `F9` about a different
name, arriving again.

### RT-115 — the grammar redesign is framed correctly

**Worth-noting, and it is credit. MEASURED.**

The pilot review warned that the findings file's reason for narrowing
step 4 argued against the option it pointed to: if supervision is not the
binding constraint, then a redesign that adds a training signal is an odd
thing to recommend. Its instruction was specific: "What the run actually
rules out is reweighting rows the battery already had. What option D
proposes is giving it a different and easier question first... Write it
that way, or the contradiction will be found by someone else."

The proposal writes it that way. Its fourth settled point says the run
"says nothing about a different and easier question taught first (option
D), which is a grammar change, not a reweighting", and the withdrawn
sentence — "supervision is not the binding constraint" — appears nowhere
in the document. The ruled correction was carried in full and without
being softened back.

The same is true of two other rulings aimed at this document: the
corrected floor of 0.4227 is stated as the reason (`RT-53`), and the
ceiling precondition is carried explicitly (`RT-69`). And the matched
comparison that `RT-62` was ruled fatal over is quoted, with the words
"bought nothing" absent. On the four things the ledger told this proposal
to do, it did four.

**One small staleness in the precondition.** The proposal's sixth settled
point says "any option that keeps this battery measures its ceiling
properly first". The ceiling *was* measured, on 2026-09-17, at 1.0, by
two independent solvers with both known-answer checks reproducing their
registered values first. What remains unmeasured is the ceiling of a
*new* grammar's control turn, which only the redesign needs — the
requirements document says so: "the ownership-blind ceiling of the new
turn is measured on the new grammar by an attack that reads the name".
Under option A there is nothing further to measure. Worth a clause,
because as written the precondition reads as outstanding work on both
paths when it is outstanding on one.

### RT-116 — bare numbers in the section John has to act on

**Worth-noting. MEASURED.**

The workspace rule is explicit: "Never write a bare identifier... every
one of them carries a plain phrase saying what it is... This applies
inside lists and source appendices too, which is exactly where bare ids
are most tempting and least useful."

The proposal is well written against that rule almost everywhere — the
tiers are explained, the batteries are named in words, the arithmetic is
spelled out. Two places break it, and they are the two places where John
has to do something:

- "patching has never run (ledger RT-49, RT-92)" — two numbers, no
  phrase. They are the row about the two-method requirement and the row
  that restates it against the fitted read.
- "the two open $0 closures from the pilot review (RT-56, RT-58, RT-59)
  land before the closure text is drafted" — three numbers, no phrase, in
  a ruling request. John is being asked to rule that three things happen
  and is not told what any of them is. They are the missing training log,
  the fixed positional split in the batch, and the untested
  one-scored-token assumption. Written out, it is also immediately
  visible that the first is not like the other two, which is `RT-100`.

The same document writes "$0" eight times where "free" or "no spend" is
the plain word, and "Tier C" as a bare label in a heading before the
paragraph that explains it. Small, but this is the document that gets
quoted into the closure text, and the closure text is what the outside
reader sees.

### RT-117 — the recommendation I would put in front of John

**The brief asks for it if it differs. It differs in the instruction, not
in the destination.**

> **Rule A: close Amendment A3.** The case for it is sound and this
> review did not dent it — the registered comparison has been dead since
> registration for a reason no training can fix, the control battery is
> flat at the level of a solver that cannot read the name, and a grammar
> redesign is a new experiment that does not fit before the release or
> before John's military training starts in January. But do not rule "A
> with causal patching run first", because that instruction does not
> survive contact with the record: there is no patching code for this
> design (only Experiment 1's, written for a different model and a
> different vocabulary), there is no subspace for it to transplant
> because the probes have found none, and with the probe leg empty and
> the matched other-agent control unrun it can reach neither of the two
> outcomes the proposal promises. Rule instead that the localization line
> runs the queue the last review set and you already authorised — the
> other-agent index control and the standardised refit — plus the
> registered, unconditional blind-localization arm that the approved
> roadmap puts on 2026-09-27 and that this proposal never mentions, since
> that arm is the registered test of whether these instruments can find a
> centre known to be there, and without it no null here can be read as
> anything but instrument failure. Let causal patching be designed after
> those report, with its target and its null written down before it runs,
> its own review, and an honest note that it is new code rather than a
> free reuse. Two things belong in the ruling either way: say whether the
> pre-registered loss condition about a non-self control that cannot be
> built at ceiling has fired, because if it has, the registered word for
> this outcome is *not testable* and the closure text has to use it; and
> strike "a structural signature of ownership-specific learning" from
> what the paper will claim, because the input-channel lesion removes a
> sense organ rather than showing a structure, and that is the
> registration's own sentence about its own instrument.

---

# The kill case

*One paragraph, required whether or not the proposal should stand.*

The kill case is that this proposal does the hard half of its job and
then recommends the one action it did not check. The hard half is real:
it reads the tiers exactly as they were pre-stated, carries the corrected
floor rule and the ceiling precondition John ruled, quotes the matched
comparison that a fatal ledger row demanded, keeps the withdrawn sentence
about supervision out, frames the grammar redesign as a different
question rather than more supervision exactly as it was told to, and
reaches a conclusion — close Amendment A3 — that survives everything in
this review. Then it tells John the thing that makes closure worth having
is free, local, and already built, and it is none of the three: there is
no patching code in this experiment's source folder, the only patching
code in the repository belongs to a different experiment on a different
substrate and section 3.2 says the stack transfers only "where it
transfers", the warrant offered is removal machinery for a transplant
operation, and even with the code written there is no localized subspace
to transplant because the probes have found nothing on any seed. From
there the two promised outcomes both fail: "localized" needs probe and
patching to agree and the probe leg is empty, and the registered
two-instrument null needs the matched other-agent control that John
authorised yesterday and that has not run. Around that hole sit three
smaller ones pointing the same way — a registered, unconditional, free
localization arm due a week before the decision that the document never
mentions; a ruled deadline for committing the pilot's training log that
has passed unmet and been quietly rewritten to a later one; and a paper
claim, "a structural signature", that the amendment's own text about the
input-channel lesion forbids. **None of that makes the recommendation
wrong.** Closing Amendment A3 is right, for the reasons given, and the
calendar argument against the redesign is the strongest thing in the
document. It makes the operative instruction wrong: the three weeks after
4 October should buy the two probe-side runs already authorised and the
registered blind arm already scheduled, and patching should be designed
once there is something for it to patch and once somebody has written
down that it is new code.
