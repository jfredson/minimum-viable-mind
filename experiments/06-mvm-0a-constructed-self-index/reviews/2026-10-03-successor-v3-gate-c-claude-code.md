# Gate C tier 1 review of the successor proposal, version 3 — RT-230 to RT-236

*Written 2026-10-03 (Pacific) by a Claude Code session on branch
`gate-c-review-proposal-v3`, cut from the main line at `c2acb0d`. Filed under
this experiment's reviews directory because the successor experiment has no
directory of its own yet, and this is the experiment its text most affects
(`docs/outside-review-protocol.md`, "The pairing rule", the filing fallback).*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run, and the command and its output are below) or
**ARGUED** (reasoning a reader can dispute), and carries a severity: **fatal**,
**serious** or **minor** (the protocol's "worth-noting"). Findings continue the
red-team ledger's numbering from its last entry, RT-229
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`). No ledger
row is written here: rows are written when John rules.*

**Nothing was rented, created or spent: $0.** No registered text, ruling file,
protocol text or proposal text was edited. The three scripts this review ran
load committed toy models and fit small classifiers on the laptop; they train
no model and write no file.

**Verdict in one paragraph.** Nothing fatal. One serious finding in the
design (RT-230: the four-fifths floor is scored on the whole read, but the
piece that is actually transplanted can be as small as one direction, and on
two of three entangled-model seeds that piece does not hold the label at the
floor; the readings themselves survive, at every rank). One serious finding
about what is still owed before Gate A (RT-233). Five minor ones. One check
the proposal lists as owed was run here and holds (RT-231). The ruled numbers,
the site-set counts, the bar and the money all recompute.

---

## What this review is, and what it opened

**The target.** `docs/successor-experiment-proposal-2026-09-26-v3.md` at commit
`37269ad` on branch `worktree-w1d-proposal-v3` (pull request 71, open when this
was written): version 3 of the proposal for the successor experiment, which
builds systems whose "degree" (how far the act can be pulled apart from the
answer to "which agent am I") is fixed by construction, asks whether a
transplant-based measure tells them apart, and then reads a freely trained
system. Gate C is the review attached to a proposal before John rules on it;
tier 1 is the inside pass by a session that can run code.

**How isolated this session was, said plainly.** The protocol asks for a fresh
session with the packet and nothing else. This session is not that. Earlier
the same day it wrote the 2026-10-03 catch-up entry in `STATUS.md` (pull
request 73), and to do so it read: the top entries of `STATUS.md`; the Weekend
1 handoff; the Gate C rulings file on version 2 in full
(`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`); pages 4, 5, 7, 8
and 9 of the Weekend 1 queue ruling; the descriptions of pull requests 71 and
72; and the opening and findings table of the Gate C review of version 2. It
did not write version 3, has not read any chat of the session that did, and
formed no view of version 3's design before reading it for this review. John
chose to run the review in this session after being told it was not fresh.
A reader who wants the protocol's full isolation should treat this as a
paired check by a second session and commission a fresh one at Gate A.

**Opened for this review, in this order.** `docs/outside-review-protocol.md`
(the gates, the pairing rule, the isolation section, the rehearsal
requirement, the tiers, the brief, the closure rule, filing);
the headings of `docs/known-failure-modes.md`; the proposal at `37269ad`,
sections 0 to 15 in full (lines 1 to 2545). Then, as records and code the
proposal cites, on the main line: `experiments/rehearsal-successor-measure/src/repairs.py`
(the read, the floor and the nomination rule), `src/rerun_v3.py` (the family,
the pick, the fit and its verdict), `src/rehearse.py` (`basis_for`,
`_labels`), `src/transplant.py` (`position_mask`), `src/training.py`
(`pick_device`); `out-v3-rules/pass2_summary.json`, `pass2_table.md` and the
twelve `nominate_*` files; `out-repairs/measure_base_M.json`; the thirty
committed models' folder (the twelve base-recipe models for arms T, C, F and M
were loaded); the compute ledger's two 2026-09-25 rows.

**Not opened.** Sections 16, 17 and 18 of the proposal (where the pieces are,
the author's own failure-mode pass, the change log): none of the author's
dispositions was read. The body of `docs/known-failure-modes.md` beyond its
headings. The toy re-run findings, its check, the label search and its check,
as documents (their output files were read directly). Any vendor. The
project's citation checker was not run; the author reports its output in
section 17, which this review did not read.

**What this review is not.** It is not the failure-mode pass, which the
protocol gives to the Gate A tier 1 reviewer, and it is not the reviewer-owned
verification Gate A owes.

The scripts are committed beside this file, in
`reviews/2026-10-03-successor-v3-gate-c-scripts/`. Each is run from
`experiments/rehearsal-successor-measure/src` with the project's own Python
environment (`.venv`, torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0), on the
processor (not the laptop's graphics chip; RT-232 says why that matters).

---

## Findings at a glance

| Number | Severity | Label | Brief part | The finding in one line |
|---|---|---|---|---|
| RT-230 | **serious** | MEASURED | 1, 2 | The fit floor is scored on the whole read; the transplanted piece is its leading 1, 2, 4 or 8 directions, and on arm C seeds 1 and 2 that piece holds the label at 0.544 and 0.306, under the floor. Section 5.2's sentence that the transplanted subspace "holds the label and clears the fit floor on every seed" is false on two seeds of three. The readings survive at every rank |
| RT-231 | minor | MEASURED | 1 | The check section 5.3 lists as owed (arm M's blind reading within 0.10 of its true-slot reading at the registered site sets) was run here and holds: 0.0049, 0.0099 and 0.0529 |
| RT-232 | minor | MEASURED, ARGUED | 1 | The free arm's fits move by one held-out episode between the laptop's processor and its graphics chip (0.178 against 0.172; 0.100 against 0.106); the other ten fits are identical. The registration does not say which is the registered arithmetic |
| RT-233 | **serious** | ARGUED | 1 | Four controls (1, 2, 4 and 6) have no figure under the registered rules on arms C, F and M, and the null transplant was not run at seven changed site sets. The proposal says so itself. Under item 5 of the 2026-09-21 ruling each is fatal at Gate A if still missing |
| RT-234 | minor | MEASURED | 3 | The whole-state floor is written as applying "on the same fresh episodes", but the nomination applies it on development episodes and the reading applies it again on fresh ones. The text does not say what happens when the two disagree. On the toy they agree on all twelve; the free arm's narrowest margin is 9 episodes of 600 |
| RT-235 | minor | ARGUED | 3 | The stop after the first full-size free-model run reports "the nomination fit", which is the fit at whichever layer the nomination picks. On a model where no transplant moves anything that pick is made among sampling noise, so the stop could fire, or not, on an arbitrary layer |
| RT-236 | minor | MEASURED | 4 | The toy model is called "a five-layer model" against a "twelve-layer" registered one. It has four blocks and five running states; the registered model has twelve blocks and thirteen states. The label search and its check are now on the main line and are still cited by branch |

---

## RT-230 (serious, MEASURED). The floor certifies the read, not the piece that is transplanted

**What the proposal says.** Section 6.4, item 2, and section 7.2, items 1 and
3: one straight-line read is fitted per layer at the action position; its
held-out accuracy must be four fifths or better; the directions transplanted
are "that read's leading directions", at rank cap 1, 2, 4 or 8, and the
nomination picks the rank along with the site (item 5: highest
development-set ownership-only accuracy, ties to the lower rank). Section 5.2
then says of arm C: "Its reads fit at 1.000, 0.961 and 0.978 at the nominated
layers (…ranks 8, 2 and 1), so the subspace it transplants holds the label and
clears the fit floor on every seed". Section 3's rewritten admission rests on
the same step: "a subspace nominated by a read at 0.96 or better … held the
label and still moved nothing, which is what 'entangled at these sites'
means."

**What was measured.** The label has twelve classes on the development
episodes. A read restricted to one or two directions cannot be assumed to
carry a twelve-way label, so the review fitted a fresh read given only the
state's coordinates inside the subspace the transplant would move, on the same
600 development episodes and the same 420/180 split as the registered fit.

```
$ ../../../.venv/bin/python ../../06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-scripts/subspace_fit.py
development episodes 600, held out 180, distinct marker words 12, most common class share 0.102
arm/seed | nominated site set | full fit | restricted fit at the action position, rank 1 / 2 / 4 / 8 | at nominated rank | dev ownership-only share at that site, rank 1/2/4/8 (whole; untouched)
T/0 | layers (0,) at action, rank 8 | 1.000 | 0.539 / 1.000 / 1.000 / 1.000 | 1.000 | 0.1517 / 0.3350 / 0.7783 / 1.0000 (1.0000; 0.0000)
T/1 | layers (0,) at action, rank 8 | 1.000 | 0.656 / 0.928 / 1.000 / 1.000 | 1.000 | 0.1417 / 0.3950 / 0.8467 / 1.0000 (1.0000; 0.0000)
T/2 | layers (0,) at action, rank 8 | 1.000 | 0.772 / 1.000 / 1.000 / 1.000 | 1.000 | 0.1667 / 0.3350 / 0.8717 / 1.0000 (1.0000; 0.0000)
C/0 | layers (2,) at action, rank 8 | 1.000 | 0.356 / 0.667 / 0.989 / 1.000 | 1.000 | 0.0517 / 0.0500 / 0.0517 / 0.0550 (0.5667; 0.0517)
C/1 | layers (4,) at action, rank 2 | 0.961 | 0.300 / 0.544 / 0.700 / 0.900 | 0.544 | 0.0517 / 0.0533 / 0.0533 / 0.0517 (0.5783; 0.0517)
C/2 | layers (1,) at post-identity, rank 1 | 0.978 | 0.306 / 0.550 / 0.833 / 0.989 | 0.306 | 0.0533 / 0.0517 / 0.0533 / 0.0517 (0.5817; 0.0517)
      at the other positions of post-identity: full-state fit at first own turn 1.000, span mean 1.000; restricted to the nominated rank-1 subspace: first own turn 0.161, span mean 0.194
F/0 | layers (1,) at post-identity, rank 1 | 0.178 | 0.122 / 0.172 / 0.189 / 0.178 | 0.122 | 0.0633 / 0.0567 / 0.0533 / 0.0500 (0.5033; 0.0600)
      at the other positions of post-identity: full-state fit at first own turn 1.000, span mean 0.511; restricted to the nominated rank-1 subspace: first own turn 0.117, span mean 0.128
F/1 | layers (1,) at action+3, rank 4 | 0.067 | 0.072 / 0.072 / 0.094 / 0.044 | 0.094 | 0.0483 / 0.0483 / 0.0500 / 0.0500 (0.5533; 0.0483)
      at the other positions of action+3: full-state fit at first own turn 1.000, span mean 0.106; restricted to the nominated rank-4 subspace: first own turn 0.394, span mean 0.083
F/2 | layers (1,) at post-identity, rank 8 | 0.100 | 0.133 / 0.111 / 0.089 / 0.100 | 0.100 | 0.0700 / 0.0683 / 0.0683 / 0.0733 (0.5583; 0.0683)
      at the other positions of post-identity: full-state fit at first own turn 1.000, span mean 0.400; restricted to the nominated rank-8 subspace: first own turn 0.806, span mean 0.122
M/0 | layers (1,) at post-identity, rank 8 | 1.000 | 0.461 / 0.778 / 0.989 / 1.000 | 1.000 | 0.0317 / 0.0700 / 0.1833 / 0.3867 (0.7717; 0.0150)
      at the other positions of post-identity: full-state fit at first own turn 1.000, span mean 1.000; restricted to the nominated rank-8 subspace: first own turn 0.839, span mean 0.883
M/1 | layers (1,) at post-identity, rank 8 | 1.000 | 0.633 / 0.911 / 1.000 / 1.000 | 1.000 | 0.0450 / 0.0867 / 0.1817 / 0.3950 (0.7667; 0.0167)
      at the other positions of post-identity: full-state fit at first own turn 1.000, span mean 1.000; restricted to the nominated rank-8 subspace: first own turn 0.839, span mean 0.983
M/2 | layers (1,) at post-identity, rank 8 | 1.000 | 0.500 / 0.817 / 1.000 / 1.000 | 1.000 | 0.0450 / 0.0817 / 0.2467 / 0.3683 (0.7783; 0.0117)
      at the other positions of post-identity: full-state fit at first own turn 1.000, span mean 1.000; restricted to the nominated rank-8 subspace: first own turn 0.967, span mean 0.972
```

**Does the output match what the text claims?** For the full read, yes: the
"full fit" column reproduces the proposal's 1.000, 0.961 and 0.978 on arm C
and 1.000 on arms T and M exactly. For the sentence in section 5.2, no, on two
seeds of three. On arm C seed 1 the transplanted rank-2 subspace holds the
label at **0.544**, and on seed 2 the transplanted rank-1 subspace holds it at
**0.306** at the action position and at 0.161 to 0.194 at the other positions
of the span it is transplanted at. Both are under four fifths. Only seed 0,
nominated at rank 8, has a transplanted subspace that holds the label (1.000).

**Why it happens.** On an arm where no rank moves the action, the nomination's
"highest ownership-only accuracy" is a choice among numbers that differ by one
or two episodes of 600 (arm C: 0.0500 to 0.0550 at every rank, against 0.0517
untouched), and ties go to the lower rank. So at the entangled end, which is
where the free model's reading matters most, the rule drifts toward the
smallest subspaces, and the floor says nothing about them because it is scored
on the whole read.

**Why this is serious and not fatal: the readings survive.** If the low rank
were producing the reading of 1, this would be the fatal finding of version 2
(an empty instrument reading "entangled") come back at the level of rank. It
is not, on the toy. The rank-8 subspace does hold the label on every arm C
seed (1.000, 0.900, 0.989), and it moves nothing either:

```
$ ../../../.venv/bin/python ../../06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-scripts/rank_and_floor.py
blocks in the toy model: 4 | running states: 5
1. arm C, fresh episodes, reading by rank at the nominated layer and position set
C/0 layers (2,) at action (nominated rank 8); whole 0.5400, untouched 0.0512 | rank 1: ownership-only 0.0512, reading 1.0000 | rank 2: ownership-only 0.0512, reading 1.0000 | rank 4: ownership-only 0.0512, reading 1.0000 | rank 8: ownership-only 0.0488, reading 1.0051
C/1 layers (4,) at action (nominated rank 2); whole 0.5575, untouched 0.0488 | rank 1: ownership-only 0.0475, reading 1.0025 | rank 2: ownership-only 0.0475, reading 1.0025 | rank 4: ownership-only 0.0500, reading 0.9975 | rank 8: ownership-only 0.0500, reading 0.9975
C/2 layers (1,) at post-identity (nominated rank 1); whole 0.5463, untouched 0.0600 | rank 1: ownership-only 0.0600, reading 1.0000 | rank 2: ownership-only 0.0625, reading 0.9949 | rank 4: ownership-only 0.0612, reading 0.9974 | rank 8: ownership-only 0.0650, reading 0.9897
```

Arm C reads between 0.9897 and 1.0051 at every rank on every seed, on the
fresh episodes. The committed readings at the nominated ranks (1.0051, 1.0025,
1.0000) are reproduced to four decimals. So the toy anchor stands, and so does
the separation.

**What is wrong, then, and what it would cost at registered size.** Three
things. (1) Section 5.2 and section 3 state as measured something the record
does not show and this measurement contradicts on two seeds. That sentence
would go into registration text. (2) The reporting table of section 7.5 prints
"fit floor passes" beside a rank-1 or rank-2 subspace, and control 3 beside
it compares that subspace with random subspaces of the same small rank; a
reader takes both as statements about what was transplanted. (3) For the free
model at registered size, a full read at or above four fifths with nothing
moving at any rank would be reported at whatever rank the noise picked. The
entangled reading would very likely be right, as it is on arm C, but the
record would not show it, and the one line of defence against an empty
instrument would be certifying something other than the instrument.

**Repairs that cost nothing, for John to choose between; none is this
review's to adopt.** (a) Print the restricted fit of the nominated subspace
beside the full fit in the reporting table, and apply the floor to it. As the
rule stands that would return no verdict on arm C seeds 1 and 2, so it needs
(b) with it. (b) Let only ranks whose restricted fit clears the floor be
candidates; on the toy that leaves arm C rank 4 or 8 on seed 0, rank 8 on
seed 1 (0.900), rank 4 or 8 on seed 2, with readings of 0.99 to 1.005, and
leaves arms T and M at rank 8 as now. (c) Report the rank-8 row for every arm
and seed beside the nominated one, 8 being the registered cap. Whichever is
chosen, the sentence in section 5.2 and the admission in section 3 need
rewording to say what was measured: the read holds the label; the largest
subspace transplanted holds it; no rank moves the action.

**A side observation from the same output, not a finding.** On the free arm
the label is fully readable from the state at the model's first own turn
(1.000 on every seed) and nearly unreadable at the action position (0.07 to
0.18). That is the route sentence of section 7.2 seen directly: the marker
word is the input token at own turns, and the free toy model does not carry
it forward to where it acts.

---

## RT-231 (minor, MEASURED). The check section 5.3 lists as owed, run: it holds

Section 5.3 says the "within 0.10 of the true-slot reading" half of arm M's
prediction has no figure at the site sets the registered rule nominates, and
is owed before Gate A. Section 7.4 freezes that prediction, so by item 5 of
the 2026-09-21 ruling it must have been exercised. It was run here, at layer
1, the post-identity position set, rank 8, on the same 800 fresh episodes,
with the true-slot reading computed both ways the repairs code computes it.

```
$ ../../../.venv/bin/python ../../06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-scripts/arm_m_true_slot.py
seed | site set | blind reading (committed) | blind reading (this run) | oracle true-slot reading | route formula | blind minus oracle | blind minus formula | within 0.10
0 | layers (1,) at post-identity, rank 8 | 0.4886 | 0.4886 | 0.4837 | 0.4837 | +0.0049 | +0.0049 | True
      separable route: whole 1.0000, untouched 0.0000; entangled route: whole 0.6356, untouched 0.0207; entangled share 0.60375
1 | layers (1,) at post-identity, rank 8 | 0.4860 | 0.4860 | 0.4760 | 0.4760 | +0.0099 | +0.0099 | True
      separable route: whole 1.0000, untouched 0.0000; entangled route: whole 0.6253, untouched 0.0290; entangled share 0.60375
2 | layers (1,) at post-identity, rank 8 | 0.5449 | 0.5449 | 0.4920 | 0.4920 | +0.0529 | +0.0529 | True
      separable route: whole 1.0000, untouched 0.0000; entangled route: whole 0.6584, untouched 0.0228; entangled share 0.60375
```

**Does the output match what the text claims?** Yes. The blind readings
reproduce the committed 0.4886, 0.4860 and 0.5449; the oracle reading and the
route formula agree to four decimals, as the version 2 ruling on RT-223 says
they must; and the blind reading is within 0.10 of them on every seed. Seed 2
uses a little over half the allowance (0.0529). This figure is no longer owed
for arm M; version 4 can cite this file for it.

---

## RT-232 (minor, MEASURED and ARGUED). Near-chance fits move by one episode between the processor and the graphics chip

MEASURED: in the first output above, run on the processor, the free arm's
full fits are 0.178, 0.067 and 0.100. The committed figures the proposal
quotes are 0.172, 0.067 and 0.106. Each difference is exactly one held-out
episode of 180 (0.0056). The other ten fits, on arms T, C and M and arm F
seed 1, are identical to the committed ones. ARGUED: the cause is the device.
The committed run's driver picks the laptop's graphics chip when one is
present (`training.pick_device`), this review ran on the processor, and a read
near chance has many near-tied episodes that small arithmetic differences can
tip.

It changes no toy verdict: every free-arm fit is far under the floor either
way. It matters for the registration because the floor is a hard line, per arm
and seed, and a fit within an episode or two of four fifths could pass on one
device and fail on the other. Suggested for version 4: state the fit as a
count of held-out episodes, name the device and number format the registered
fit is computed on, and say that the figure on that device is the registered
one.

---

## RT-233 (serious, ARGUED). What is still unexercised under the registered rules blocks Gate A, not this proposal

The proposal is candid about this in sections 7.3 and 10: the re-run under
the registered rules re-ran control 3 and control 7 only. For arms C, F and M,
controls 1, 2, 4 and 6 have no figure at the site sets the rule now nominates,
and version 2's figures for them are withdrawn. The null transplant (control
7, one of the two that hold) was not run at the seven site sets that changed
on the second pass. Section 7.4 freezes all seven controls with their
pre-stated cells and expectations.

The protocol's rehearsal requirement and item 5 of the 2026-09-21 ruling make
a pre-stated quantity the rehearsal never exercised a fatal finding on its
own at Gate A. This review did not run those controls; the arm M true-slot
check (RT-231) was the one owed item cheap enough to run here. The finding is
that this is not optional tidying: the registration review cannot open on
version 4 until the re-run of rehearsal items R-1 to R-6 that section 10
promises is committed and checked. It is laptop work at $0. It sits on the
path to the 2026-10-18 kill date and should be scheduled as such.

---

## RT-234 (minor, MEASURED). The whole-state floor is applied twice, on different episodes, and the text names one

Section 6.4, item 1, and the table in section 9 say a site set is usable only
if the whole-state transplant clears four fifths of the arm's accuracy "on the
same fresh episodes". Section 7.1 says everything that is chosen is chosen on
development episodes, and the code does that: `repairs.nominate` applies the
floor on the development episodes to decide which site sets are candidates,
and the reading applies it again on the fresh ones. Both are right; the text
describes only the second, and does not say what the outcome is when a site
set clears on development episodes and misses on fresh ones (the code returns
no verdict; the text should say so, since the nomination is frozen by then and
cannot be redone).

The second part of the output under RT-230:

```
2. whole-state floor, development (nomination) and fresh (reading)
T/0 development: clears True (room 1.0000, needed 0.8000) | fresh: clears True (room 1.0000, needed 0.8000)
T/1 development: clears True (room 1.0000, needed 0.8000) | fresh: clears True (room 1.0000, needed 0.8000)
T/2 development: clears True (room 1.0000, needed 0.8000) | fresh: clears True (room 1.0000, needed 0.8000)
C/0 development: clears True (room 0.5150, needed 0.4120) | fresh: clears True (room 0.4888, needed 0.3980)
C/1 development: clears True (room 0.5267, needed 0.4133) | fresh: clears True (room 0.5088, needed 0.4260)
C/2 development: clears True (room 0.5300, needed 0.4200) | fresh: clears True (room 0.4863, needed 0.3940)
F/0 development: clears True (room 0.4433, needed 0.4280) | fresh: clears True (room 0.4263, needed 0.4000)
F/1 development: clears True (room 0.5050, needed 0.4160) | fresh: clears True (room 0.5112, needed 0.4080)
F/2 development: clears True (room 0.4900, needed 0.4027) | fresh: clears True (room 0.4613, needed 0.3900)
M/0 development: clears True (room 0.7567, needed 0.6747) | fresh: clears True (room 0.7675, needed 0.6870)
M/1 development: clears True (room 0.7500, needed 0.6840) | fresh: clears True (room 0.7563, needed 0.6900)
M/2 development: clears True (room 0.7667, needed 0.7000) | fresh: clears True (room 0.7800, needed 0.6860)
```

On the toy the two agree on all twelve. The narrowest margin is the free arm
seed 0 on development episodes: 0.4433 against 0.4280 needed, which is 9
episodes of 600. So a disagreement between the two sets is a live route to a
no verdict on the arm being read, and the registration should name it.

---

## RT-235 (minor, ARGUED). The stop after the first full-size free-model run reads its fit at a layer the noise may pick

Section 11, step 5a, and stop condition S4a: the single free-model run reports
"the nomination fit of that run's ownership read", and a miss of the floor is
a stop before the second release. The nomination is blind to the fit (section
7.2, item 5), by design. It picks among up to four candidates, one per
position set, each at that position set's smallest layer set that clears the
whole-state floor, by highest ownership-only accuracy. On a model where the
ownership-only transplant moves nothing, that is the same choice among
sampling noise that RT-230 describes for rank, and the layer it lands on can
differ between candidates. On the toy this did not bite, because arm C's read
fits at 0.96 or better at every layer past the first. At twelve blocks, on the
free model, the fit may well clear the floor at some layers and not others.

The stop is John's call with the figure in hand, so nothing here blocks. The
suggestion is that the report for step 5a prints the fit at every layer, the
restricted fit at the nominated rank (RT-230), and the candidates the
nomination chose among, all of which the procedure has already computed, so
the call is not made on one number from an arbitrary pick.

---

## RT-236 (minor, MEASURED). "Five-layer" against "twelve-layer", and two citations by branch

The first line of the second output above: the toy model has 4 blocks and 5
running states. Section 7.2, item 1, repeating the ruling's recorded reason,
calls the toy "a five-layer model" and the registered one "the twelve-layer
model". The registered model has twelve blocks and thirteen states (section
7.2, item 2, counts them that way). The like-for-like statement is four
blocks against twelve, or five states against thirteen. It bears, slightly,
on the argument John's ruling leans on, that a deeper model may clear a floor
the toy missed at 0.789: the gap in depth is a factor of three, not of two
and a half. The ruling stands as recorded; version 4 should state the depths
the same way in both places.

The label search and its check, cited in the proposal by branch
(`26b737f`, `75b7cf9`), are on the main line as `a97c12b` (pull request 66)
and `ecd2b6c` (pull request 70). The proposal says its citations change form
when they merge; they have.

---

## What was checked and held

- **The site-set counts** of section 7.2, by arithmetic on the rule: 60, 45,
  55 and 40 on the toy's five states; 364, 325, 351 and 312 on the registered
  model's thirteen. `python -c` output: `5 states: all 60 | layer0 kept at
  action only 45 | narrower 55 | stricter 40` and `13 states: all 364 | layer0
  kept at action only 325 | narrower 351 | stricter 312`. They match.
- **The learn-both bar.** The exact one-sided binomial tail at 790 of 3,000
  against one in four is 0.04851; at 789 it is 0.05286. So 790 is the first
  count that clears the 0.05 level, and 4.85% is the rate at which a fully
  collapsed seed reads "not collapsed", as sections 8.1 and 8.2 say.
- **The money.** $228.15 + $161.90 + $32 = $422.05; + $44 = $434.05; on the
  ruled split, $450 − ($228.15 + $44 + $119.06 + $44) = $14.79. They match
  section 12.4 and 12.8. The $228.15 and $46.75 are the running totals of the
  compute ledger's last row.
- **The toy readings.** Arm C's and arm M's committed readings were recomputed
  from the committed models on fresh episodes, on a different device from the
  committed run, and reproduce to four decimals (RT-230, RT-231).
- **The fits.** Ten of twelve reproduce exactly; the two that do not are
  RT-232.
- **The one-instrument claim.** `repairs.nominate` and `rerun_v3.pick` take no
  argument naming an arm; read, not run.
- **The repairs of version 2's findings, as far as this review reached.** The
  fit floor returns no verdict on the free arm and a reading on the other
  three (RT-212); the registered family is what the code runs (RT-215); no
  layer-0 site set survives away from the action position in any nomination
  (RT-216); control 3 is reported as twenty draws on all twelve rows (RT-214).

---

## The four parts of the brief

**1. Feasibility.** Every threshold in section 9 has a toy figure behind it
under the registered rules, except those RT-233 lists. The fit floor can be
measured and reached (arms T, C and M reach it); what it certifies is narrower
than the text says (RT-230). Arm M's "within 0.10" is now exercised (RT-231).
The fit's arithmetic is device-dependent at the edge (RT-232). No "measured"
claim was found with no record behind it except the sentence of RT-230.

**2. Satisfied by the wrong thing.** The floor can be passed by a read whose
transplanted piece does not hold the label (RT-230). What the proposal already
admits and this review agrees is unremovable: a read that clears the floor
shows the label is present, not that the act uses those directions (weakness
W12); the built models differ in more than degree (W1); arm M is a mixture by
item, not partial separation within a trial (W10).

**3. No verdict.** The routes by which the arm being read returns nothing:
it fails to learn the other-agent condition (the toy does, on two seeds of
three, after four repair attempts); its read misses the floor (the toy does,
on every seed); no site set clears the whole-state floor; a site set clears
on development episodes and misses on fresh ones (RT-234); the floor is read
at a layer the noise picked (RT-235). The first two are registered
possibilities with a stop that bounds their cost at the first release.
Decision 14, what a no verdict maps to, is still open and should be ruled
before Gate A; its recommended fifth term, "metric validated, degree not
read", is the honest one.

**4. Over-reading.** If arm C's readings are reported with the sentence of
section 5.2 as it stands, a reader takes "the transplanted subspace held the
label and did nothing" as shown on every seed; it is shown on one, and on the
other two what is shown is that no rank does anything and the largest holds
the label. If the experiment ends at "metric validated, degree not read", the
likely public misreading is that the free model was found entangled or found
empty; neither would have been measured. The depth comparison of RT-236 is a
small instance of the same thing.

---

## The kill case, in one paragraph

The strongest case against registering this design is that its most likely
ending, on its own toy record, is a ruler validated on three built models and
no reading of the one model the question is about. The free toy model's read
of the ruled label sits at chance (0.07 to 0.18 against 0.8), the best of
three alternative labels reached 0.789 and only by starting its span on the
answer, and the other-agent condition has failed every repair. Everything
that says the full-size model will do better is argued from depth, and
nothing at full size has been run. Against that: the design now fails
honestly rather than silently, which version 2 did not; the stop after the
first full-size run means the argument from depth is tested for about $44
before about $150 to $160 more is committed; and a validated measure with
three anchors is the Stage 2 deliverable in the roadmap's own words, "the
metric, not a verdict", whether or not the free model can be read with it.
This review's judgement is that the kill case is real and already priced into
the design by John's ruling of 2026-09-26, and that nothing found here adds to
it.

---

## What John is asked to rule

1. **RT-230:** which repair, (a) with (b), (b) alone, or (c), and the
   rewording of sections 3 and 5.2.
2. **RT-233:** that the re-run of rehearsal items R-1 to R-6 under the
   registered rules is a precondition of Gate A on version 4, and is scheduled
   before the registration text is reviewed.
3. **RT-232, RT-234, RT-235, RT-236:** accept the wording fixes as stated, or
   not.
4. The open decisions of the proposal's section 15 that no ruling has yet
   settled: 2, 3, 4, 8, 9, 10 (its standing), 13, 14, 15, 16, 17, 18 and 19.
   This review found no reason to recommend against any of the proposal's own
   recommendations on them.
