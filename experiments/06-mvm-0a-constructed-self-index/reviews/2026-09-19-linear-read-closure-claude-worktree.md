# Outside review — the linear-read closure (Gate B, tier 1)

*Filed 2026-09-19 under the outside-review protocol, against the review
packet `2026-09-19-linear-read-closure-packet.md`. Verbatim on filing and
not edited afterwards. Nothing here is a ruling; rulings are John's and go
in the red-team ledger (`red_team_ledger.md`).*

## What was opened

Read at the commit that merged pull request 4 (`eaff1d5`), in a fresh
worktree checked out at that commit. Exactly the packet's list and nothing
else:

- The four method files: the denoised-direction method
  (`denoised-direction-method.md`), the position-sweep method
  (`position-sweep-method.md`), the powered-target-test method
  (`powered-target-test-method.md`), the powered-position-sweep method
  (`powered-position-sweep-method.md`).
- The four findings files with the matching names ending
  `-findings.md`.
- The six code files named in the packet, under `src/`:
  `denoised_direction_a3.py`, `position_sweep_a3.py`,
  `powered_target_test_a3.py`, `powered_position_sweep_a3.py`,
  `probe_target_diagnostic_a3.py`, `marker_legibility_a3.py`.
- The fifteen records under `a3-gates/` whose names begin `powered_`,
  `probe_target_diagnostic_` or `denoised_direction_`.
- Git metadata only — commit dates, messages and the list of files each
  commit touched — used to check the "committed before the run" claim.

**Not opened**, as instructed: the status file (`STATUS.md`), the compute
ledger (`compute-ledger.md`), the `docs/` folder including the research
note the denoising idea came from, the registered texts
(`amendment-a3.md` and `pre-registration.md`), the red-team ledger
(`red_team_ledger.md`), any chat transcript, any uncommitted file, and the
model checkpoint files themselves.

Two consequences of that, stated so they are not mistaken for omissions.
**First**, the packet says the interpretation is read against the
registered texts, and those are on the do-not-open list, so I cannot check
the interpretation against them. Nothing below turns on registered text.
**Second**, I could not read the red-team ledger to see the last number
used, so I have numbered findings from **RT-33**, reading "continue from
RT-32" as meaning RT-32 is taken. If that is off by one, the numbers
renumber trivially.

No outside lookup was used. Every number below either comes from a
committed record or from a check I ran myself, and each is labelled.

**Verdict in one line.** The CARRIED NOWHERE result is sound, correctly
computed and honestly reported — I reproduced every published number from
the records. The sentence built on top of it is not. The stack's own
committed records contain a measurement showing that the read used
throughout the sweep is roughly half as accurate as an ordinary fitted
linear read on the same states, and that measurement appears in none of
the four findings files.

---

# 1. Feasibility

*For every quantity the method files pre-state or threshold: can it be
measured at all, can the control actually reach the threshold, and is
there a committed record behind it?*

| # | pre-stated quantity | can it be measured? | record behind it | severity |
|---|---|---|---|---|
| F1 | the family bar of 3.56 standard deviations | yes | recorded in all three sweep files; arithmetic reproduces | none |
| F2 | the per-test bar of 3.0 standard deviations, reported for continuity | yes | recorded per test | none |
| F3 | the 1,000-draw null | yes | every one of the 330 tests records 1,000 draws and a count | none |
| F4 | the positive control reaching the bar | yes, by a wide margin | +159, +21, +29 standard deviations, no draw beating it | none |
| F5 | the negative control | yes | 30 tests, −2.19 to +0.76, none clears | none |
| F6 | reproducing the earlier anchor result | yes | all 60 shared tests bit-identical | none |
| F7 | the scorer agreeing with the original | yes | differences of exactly 0.0, recorded in every file | none |
| F8 | checkpoints verified by checksum | yes | the three checksums in the records match the ones the method files fixed in advance | none |
| F9 | method committed before output | yes | commit history and recorded runtimes agree | none |
| F10 → RT-37 | **the smallest signal the sweep could detect** | yes | **no record anywhere** | worth-noting |
| F11 → RT-38 | **the degeneracy preconditions** | yes | **fired twice; not reported in the findings** | worth-noting |
| F12 → RT-39 | **the independence the family bar assumes** | yes | **five fold splits shared across all 270 tests** | worth-noting |
| F13 → RT-40 | **the geometry of the states at the ten non-anchor positions** | not from the record | **none exists** | worth-noting |

Nothing in this part is fatal. The packet's fatal trigger — a "verified"
or "measured" claim with no record behind it — is not tripped. I went
looking for it and did not find it. The record is in unusually good shape.

**Everything the two headline sentences claim, reproduces.** MEASURED. I
recomputed the published numbers from the fifteen records rather than
reading them off the tables:

| claim in the findings | recomputed | agrees |
|---|---|---|
| 270 testable tests | 270 (330 total, minus 5 layers × 2 arms × 3 checkpoints for each of the two control positions) | yes |
| largest margin +2.73 | +2.73 (seed 1, marker word, the other agent's revision value, layer 8) | yes |
| smallest margin −2.59 | −2.59 (seed 1, register index, the appended question's answer, layer 3) | yes |
| mean across the 270 is −0.085 | −0.0846 | yes |
| nothing reaches 3.0, let alone 3.56 | confirmed, both | yes |
| zero marginal and zero robust clearances among the testable tests | confirmed | yes |
| positive control +159.08 / +20.66 / +29.45 | exact | yes |
| every one of the 22 rows in the two position tables | all 66 numbers exact | yes |
| the anchor "reproduces the previous run exactly" | all 60 shared tests identical to the last decimal place, including the counts of shuffled draws | yes |
| the powered-anchor ranges (−1.85 to +0.49; 308 to 980 draws; 502 to 980 on arm 1) | exact | yes |

**The pre-commitment is real and independently checkable.** MEASURED. The
method file and the code for the eleven-position sweep went in as one
commit at 17:13 Pacific on 2026-09-19, touching no output. The records and
the findings went in as a separate commit at 18:08, 55 minutes later. Each
checkpoint's recorded runtime is about 53 minutes, and the method file says
the three were run as parallel processes — so the timing fits a run started
immediately after the method was fixed, with no room for a run beforehand.
The only change that commit made to existing code was to pass the family
bar in as a parameter and record which value was used; the statistics were
untouched, which is why the 60 shared tests come back bit-identical. This
is the strongest part of the whole package and it deserves saying so.

**The family-bar arithmetic is right.** MEASURED. Recomputing from
scratch: at a 3.0-standard-deviation bar one test in 741 clears by luck;
across 270 tests the chance of at least one false clearance is 30.6 per
cent; the bar that brings that back to 5 per cent is 3.55, quoted as 3.56.
The earlier runs' figures check out too (15 tests → 2.0 per cent, bar 2.71;
30 tests → 4.0 per cent, bar 2.93; 45 tests → bar 3.05, quoted 3.06; 165
tests → 20.0 per cent, bar 3.42, quoted 3.43). The honesty note about 1,000
draws resolving only to about 3.09 standard deviations is also correct.

### RT-37 — the smallest detectable signal is nowhere on the record

**Worth-noting. MEASURED.** No method file and no findings file states how
big a signal the sweep would have found. I computed it from the recorded
spread of each null. To reach the 3.56 bar, the model's own marker word
would have to be read at 5.23 per cent accuracy against a chance rate of 4
per cent, and the register index at 27.93 per cent against 25 per cent.
Put in plain terms, the sweep would detect an identity that is perfectly
legible in as few as **1.3 per cent of episodes** for the marker word, or
**3.9 per cent** for the register index. That is genuinely good power, and
it is a point in the result's favour.

It should be in the findings. A null result whose stated strength is "270
tests found nothing" is much weaker than one that says "270 tests would
have found a signal present in one episode in eighty, and found nothing."
The second sentence is true and is not written down anywhere.

Two things this number does **not** cover, and they are the subject of
part 2: it assumes the identity sits in the directions this read can see,
and it says nothing about a reader other than a difference of averages.

### RT-38 — two pre-stated preconditions fired and the findings do not say so

**Worth-noting. MEASURED.** The method pre-states that a test whose
accuracy exactly equals the majority-class rate is degenerate and gets no
cell. Two testable tests on the pilot did exactly that — the register
index read before the model's own revision turn at layer 7, and at the
appended question's answer token at layer 8, both landing on 0.2582
against a majority-class rate of 0.2582. Both are flagged in the record
and neither is mentioned in the findings, which report all 270 as tests
that answered.

This changes nothing material: both sat around one standard deviation,
nowhere near any bar, and the cell is a null either way. Strictly the
discovery family was 268, which would move the bar from 3.56 to about
3.55. It is worth a line because the whole point of writing preconditions
down in advance is to report them when they fire, and because the
denoised-direction findings set the right precedent by saying explicitly
that nothing was reported degenerate. The eleven-position sweep dropped
that sentence in the run where it would have been untrue.

### RT-39 — the 270 tests share five fold splits and five sets of shuffles

**Worth-noting. MEASURED.** In the code, each test's fold split and its
1,000 shuffled label draws are seeded by the layer number alone
(`measure(..., seed=Lr)`). So every test at layer 3 — both arms, all
eleven positions, all three checkpoints — uses one identical fold split
and one identical sequence of 1,000 shuffles. There are five distinct
splits across the whole sweep, not 270.

This cuts both ways and neither way is large. The nulls at a given layer
move together, so a lucky or unlucky set of shuffles is shared rather than
averaged out. And the family bar treats 270 tests as independent when five
layers reading the same states and two arms sharing a target are strongly
related, so the true bar is lower than 3.56 and the sweep is stricter than
it needed to be. Both are moot in the event, because the largest margin
anywhere was 2.73 and nothing came near even the unadjusted bar. I record
it because the method file's arithmetic is presented as if the tests were
independent and they are not.

### RT-40 — the geometry is known at one position out of eleven

**Worth-noting. MEASURED for what exists, ARGUED for the gap.** The only
measurement of the shape of the state space anywhere in this package is in
the denoised-direction findings: about ten directions out of 448 carry
around 99 per cent of the variation, with the largest single direction at
18 to 34 per cent. That measurement was taken **at the revision position
only** — the anchor — on 400 episodes, at five layers. The
eleven-position sweep reads ten further positions and there is no record
of the geometry at any of them.

This matters because of part 2 below: how much a difference-of-averages
read can see depends on that geometry, and outside the anchor it is
unknown.

---

# 2. Satisfied by the wrong thing

*Every way "carried nowhere" could be returned by a model that does carry
own-agent identity linearly at these positions.*

| # | mechanism | does it survive checking? | severity |
|---|---|---|---|
| RT-33 | the read is far less sensitive than an ordinary fitted linear read, **measured on these very checkpoints** | **yes — and the measurement is already in the record** | **fatal** |
| RT-34 | the read cannot see a linear signal in a quiet direction, at this stack's own measured geometry | yes | serious |
| RT-35 | the register-index arm has no positive control of its own | yes | serious |
| RT-36 | on two of three checkpoints the control recovers the answer on only one episode in eight, and the unexplained gap was quietly upgraded from a caveat to "holds without qualification" | yes | serious |
| — | the target is still ill-posed | no — both targets decode at the marker position, and the generator-index problem is genuinely fixed | — |
| — | the null is too wide | no — the nulls are tight and the detectable signal is small (RT-37) | — |
| — | the positions that matter were excluded | partly — see RT-42 and the note on position 1 | worth-noting |

### RT-33 — the stack's own record shows this read is about half as good as a fitted one, and no findings file reports it

**Fatal to the interpretation under review. MEASURED — the numbers are
read directly out of `probe_target_diagnostic_a3_*.json`, one of the
records the packet lists.**

The target diagnosis ran two instruments side by side on the same states,
same folds, same 400 episodes: the difference-of-averages read used
throughout this line of work, and an ordinary fitted linear classifier
(logistic regression). For targets with more than eight possible answers
the classifier was skipped as too slow, so the marker word was not run
through it — but the **register index has four answers, and it was**.

At the marker position, where the answer is available, on the register
index, chance being 0.25 and the majority-class rate 0.273:

| checkpoint | difference of averages (accuracy, margin) | how many of 5 layers clear | fitted classifier (accuracy, margin) | how many of 5 layers clear |
|---|---|---|---|---|
| pilot | 0.295–0.330, +1.87 to +2.93 | **0 of 5** | 0.5025–0.5250, +9.09 to +10.95 | **5 of 5** |
| seed 1 | 0.250–0.2675, **+0.03** to +0.63 | **0 of 5** | 0.4800–0.5350, +9.41 to +11.96 | **5 of 5** |
| seed 2 | 0.2975–0.3175, +1.88 to +2.24 | **0 of 5** | 0.4475–0.4950, +8.00 to +10.33 | **5 of 5** |

Read seed 1's first row. At a position where own-agent identity is so
strongly and so linearly present that a fitted classifier reads it at 48
per cent against a chance rate of 25 per cent, **the read this whole sweep
depends on returns 0.2500 — exactly chance — at a margin of +0.03 standard
deviations.** That is not a subtle sensitivity difference. It is the
sweep's read returning a flat null on a signal that is unmistakably there.

That is precisely the failure mode part 2 asks about, it is not
hypothetical, and it is measured on these three checkpoints.

Three things follow.

**First, "the read works" is doing more work than it can bear.** The
positive control shows the read can recover the marker word when the
marker word is the token sitting there. It does not show the read is a
good linear reader in general, and the table above shows it is not.

**Second, the justification written into the code for skipping the
classifier is false.** Where the classifier is skipped for having more
than eight answers, the code gives as its reason that a fitted classifier
"adds nothing the read above does not say". The four-answer results in the
very same run say the opposite, by a factor of about two in accuracy and
by the difference between clearing nothing and clearing everything.

**Third, and this is the finding: no fitted linear read has ever been run
against a well-posed target at any of the nine testable positions.** I
traced this through all six code files. The 2026-09-16 probes used a
fitted classifier but asked for the generator's agent index, which the
stack itself has established cannot be recovered. Arm 2 of the first
position sweep compared the two instruments, also on the generator index —
and its own findings say it "would have to be rerun against a well-posed
target to mean what it was designed to mean", listing that as open item 5.
It was never rerun. The two powered runs, which are the ones with
well-posed targets and real power, use the difference-of-averages read and
nothing else.

So the line "the linear-read line of attack on these checkpoints is
closed" describes work that was not done. What is closed is the
difference-of-averages read.

**One qualification, in the result's favour, which I want to state as
plainly as the criticism.** At the anchor, the fitted classifier *also*
finds nothing: on the register index its margins run from −1.90 to +1.61
across the fifteen layer-and-checkpoint tests, clearing nowhere. So the
anchor null — the NOT CARRIED result of the earlier run — is corroborated
by a second instrument, and RT-33 does not touch it. The gap is exactly
over the nine testable positions the eleven-position sweep added, where
only one instrument was ever used. That is the part of the claim that
fails, and it is the part the sweep exists to support.

### RT-34 — why the read misses it, and how quiet a direction has to be

**Serious. MEASURED, by simulation at this stack's own measured numbers.**

Both scorers assign a held-out episode to whichever class average is
nearest in plain straight-line distance, treating all 448 directions of
the state as equally important (`dist = sum((x − mu)²)` in the original,
the same arithmetic as matrix products in the vectorised rewrite). A
fitted classifier does something different: it effectively rescales each
direction by how much the states vary along it, so that a quiet direction
counts for as much as a loud one. When the states vary enormously more in
some directions than others — which is exactly what the denoised-direction
findings measured here — the two come apart badly.

I built states with the spectrum that findings file reports for the pilot
at layer 3 (largest direction 23.3 per cent of the variation, largest
three 50.4 per cent, largest ten 98.8 per cent, 448 directions in total),
at the sweep's own settings: 4,000 episodes, 25 classes, four folds. Into
those states I planted a perfectly linear identity code occupying eight
directions, and scored it with the sweep's scorer copied verbatim, against
its own permutation null of 100 draws. Alongside it I ran an ordinary
fitted linear read (shrinkage discriminant analysis) on the same folds.

| where the identity code sits | sweep's read: accuracy | its margin | clears 3.56? | fitted read: accuracy |
|---|---|---|---|---|
| in one of the ten loud directions | 0.7790 | +210.80 | yes | 0.6590 |
| a direction holding 1 per cent of the variation | 0.5507 | +152.20 | yes | 0.6590 |
| 0.1 per cent | 0.0927 | +13.71 | yes | 0.6590 |
| 0.03 per cent | 0.0542 | +3.60 | yes | 0.6590 |
| 0.01 per cent | 0.0462 | +1.58 | **no** | 0.6590 |
| **a typical direction at the measured anchor (0.0027 per cent)** | **0.0418** | **+0.44** | **no** | **0.6590** |
| no identity code at all (sanity check) | 0.0400 | +0.01 | no | 0.0447 |

Chance is 0.0400. The fitted read gets 0.6590 in every row because
rescaling makes it blind to where the code sits; the sweep's read falls
off a cliff. At the variance share that 438 of the 448 directions actually
have at the anchor, **a cleanly linear identity that a standard fitted
read recovers on two episodes in three produces +0.44 standard deviations
under the sweep's read** — indistinguishable from the 270 numbers the
sweep actually returned. With a weaker code (fitted read 0.22, still five
times chance) the crossover moves up by another factor of ten.

So the answer to part 2's question is yes, concretely and quantitatively:
a model that carries own-agent identity in a perfectly linear form returns
CARRIED NOWHERE on all 270 tests if that identity lives below roughly ten
to a hundred times the typical direction's share of the variation.

**The counter-argument, and why it does not hold.** The
denoised-direction findings argue there is "no room in this geometry" for
a quiet signal under a loud one, because ten directions carry 99 per cent
of everything. That argument confuses how much the states *vary* along a
direction with how much they can *carry*. The remaining one per cent is
spread over 438 directions, and the simulation above puts a fully
recoverable 25-way identity code exactly there. The fitted read finds it
at 0.659. There is room.

I could not test this on the real states, because doing so needs the
checkpoint files and the packet does not list them. It is the obvious next
measurement and it is cheap: the register index, four answers, fitted
classifier, all eleven positions, 4,000 episodes. The machinery already
exists in `probe_target_diagnostic_a3.py`.

### RT-35 — the register-index arm has no positive control of its own

**Serious. MEASURED.**

The method is careful and correct here: it says the control is the
marker-word arm at position 6 and that it governs both arms. The
**findings** go further than that, and the extra step does not hold.

The powered-target-test findings say the register index "is a quantity the
model demonstrably carries *somewhere*" because it reads at four to seven
standard deviations at the marker position, and conclude that its absence
at the anchor "is not a target problem and not an instrument problem".

But the register index is, by construction in the code, the rank of the
model's own marker among the episode's four markers in vocabulary order.
At the marker position the model's own marker is the token sitting there.
Knowing your own marker word already tells you a great deal about its
rank. I worked out how much: with four markers drawn from a pool of 25,
the best possible accuracy at guessing the rank **from the own marker word
alone** is **0.5815**.

The observed readings at the marker position are 0.3093 on the pilot,
0.2605–0.2720 on seed 1, and 0.2865–0.2943 on seed 2 — all well *below*
that ceiling. Every one of them is consistent with a partial read of the
marker token and nothing else. On the same checkpoint at the same position,
the marker word itself reads at 0.5877.

So the register-index clearance at the marker position is not evidence
that the model computes or stores a rank. It is a shadow of the marker
token. The arm has one demonstrated working condition, and in that
condition its target is a function of the current input token — which is
the same thing the method file says makes a position uninteresting.

The consequence for the result under review is bounded but real: arm 2's
nulls at the other ten positions rest entirely on the marker-word control,
and on an untested assumption that a read with power for a 25-way
token-identity target has comparable power for a 4-way derived rank. RT-33
shows that assumption is wrong in the direction that matters.

### RT-36 — the legibility gap was downgraded from a caveat to nothing, without a measurement

**Serious. MEASURED for the numbers, ARGUED for the drift.**

The same input token, at the same position, at the same layers, on three
checkpoints that differ only by training seed, is read at 0.5877 on the
pilot and at 0.1022–0.1398 on seeds 1 and 2. That is the positive control.
On seeds 1 and 2 the read recovers the answer on roughly one episode in
eight **when the answer is the token it is looking at**.

Follow how that fact is handled across the four findings files:

| document | what it says about the gap |
|---|---|
| position-sweep findings | "unexplained… it means the positive control is strong evidence on the pilot and weaker evidence on seed 1"; and as next step 3, "Until that is understood, any read of those two checkpoints rests on a positive control that barely holds, and a null on them means correspondingly less" |
| powered-target-test findings | runs the bounded measurement meant to explain it; reports that neither embedding length nor attention explains it, and that attention runs the wrong way; still lists it as open |
| powered-position-sweep findings | "the control that governs both arms is the marker word, and **it holds without qualification**" |

Nothing measured the gap away. The one measurement aimed at it came back
empty, by its own account. Between the second document and the third, a
stated reason to discount the nulls on two of three checkpoints was
dropped, and the sentence that replaced it says the opposite.

This matters directly for the cell. The CARRIED SOMEWHERE cell needs a
clearance on the pilot *and* on at least one other seed. If the read is
much less sensitive on seeds 1 and 2 — and an eightfold difference in
recovering the input token is strong evidence that it is — then the cell
is harder to reach than it appears, and CARRIED NOWHERE is correspondingly
easier to land in. The sweep has no calibration of the read's sensitivity
on those two checkpoints at all.

To be fair to the run: the pilot's control is excellent, and the pilot
alone shows nothing at any testable position. So the result does not
collapse. But "holds without qualification" is not a sentence the record
supports, and the earlier document had it right.

---

# 3. No verdict

*Every way the sweep could have failed to return a verdict and been read
as one anyway.*

| # | route to a non-verdict | did it happen? | severity |
|---|---|---|---|
| RT-38 | a pre-stated degeneracy precondition fires and is not reported | **yes, twice** | worth-noting |
| RT-41 | the two cells are exhaustive by construction, so a partial pattern lands in CARRIED NOWHERE | no — nothing cleared anywhere, and the method names the risk and reports the sub-pattern | none |
| RT-42 | the negative control is read as licensing more than it can | yes | worth-noting |
| RT-43 | a date on the pre-committed files that disagrees with the commit | yes | worth-noting |
| — | the positive control fails and the arm is read anyway | no — it clears at +159/+21/+29 with no draw beating it, and the code enforces it | none |
| — | the cell is assigned by hand rather than by the pre-stated rule | no — the rule is in code, unit-tested, and the summary record agrees with the findings | none |
| — | the bar is chosen after seeing the numbers | no — committed 55 minutes before the outputs, in a separate commit, with runtimes that fit the gap | none |

On the whole this part comes back clean, and more thoroughly clean than I
expected. The cell-assignment rule is implemented in code, the self-test
checks it against constructed cases including the awkward ones ("cleared
on the pilot only" must land in CARRIED NOWHERE *and* must report the
sub-pattern), and the summary record matches the findings text exactly. The
negative control's premise — that the model's own marker really has not
appeared anywhere before its first own value token — is verified against
real episodes in the self-test rather than asserted. That is the right way
round and it is rare.

Two things to record.

### RT-41 — the exhaustive pair of cells, and why it is not a problem here

**No finding. Recorded for completeness. MEASURED.** Making CARRIED
NOWHERE mean "the other cell did not fire" means it absorbs outcomes that
are not nothing. The method names this cost in advance and requires the
clearing positions to be reported per checkpoint whatever the cell says.
In the event, zero of the 270 testable tests cleared anything on any
checkpoint, the summary record says "nothing cleared on any checkpoint",
and there is no sub-pattern being hidden. The design risk is real and did
not bite.

### RT-42 — the negative control is weaker than the sentence built on it

**Worth-noting. ARGUED, from measured placement.** The findings say the
clean negative control is "the reason the other 270 numbers can be taken
at face value". That is more than it can carry, in two ways.

A leak at position 1 would have cast doubt on everything; no leak at
position 1 does not validate the other positions. The inference only runs
one way.

And position 1 is the weakest place in the episode to look for a leak from
the acting channel. The channel is described as a projection of the
model's own preceding state, added at the value token of each of its own
turns. At the model's *first* own turn there is barely any preceding own
state to leak. The positions where the channel would have the most to
carry are the model's second assignment and its revision value — and those
are inside the testable set, where they read +1.16/+0.42/+0.64 and
+0.55/+1.36/+1.78. So the leak question is in fact answered, and answered
reassuringly, but by the testable positions rather than by the negative
control. The negative control on its own establishes less than the
sentence claims.

This does not weaken the null. If anything it strengthens the reading that
nothing is leaking. It is the phrasing that overreaches.

### RT-43 — a date on the pre-committed files that does not match the commit

**Worth-noting. MEASURED.** The eleven-position sweep's method file and
findings file are both headed *2026-09-20*. Both were committed on
**2026-09-19** Pacific (17:13 and 18:08), as was everything else in the
sequence, and the packet itself is dated 2026-09-19. Almost certainly a
clock written in a different time zone. It is cosmetic and it is worth one
line only because these are the files whose entire value is *when* they
were written relative to the run, and a reader checking that chain will
hit a date that disagrees with the commit. The commit order is what
matters and it is correct.

---

# 4. Over-reading

*What "the linear-read line is closed" will be read as claiming, beyond
what was measured.*

| # | the sentence | what a reader will take it to mean | what was measured | severity |
|---|---|---|---|---|
| RT-44 | "closing the linear-read line" | no linear read finds own-agent identity at these positions | one linear read — a difference of averages — finds nothing; the fitted read was never tried at nine of the eleven positions | **fatal** |
| RT-45 | "the instrument demonstrably works" | the read has the sensitivity of a competent linear probe | the read recovers a token that is present; on a well-posed target at a position where both were tried, it scores about half what a fitted read scores | serious |
| RT-46 | "the rest of the episode is empty too" | the episode carries no own-agent identity | eleven positions of a seventy-one-token episode, by one read, carry none that this read can see | serious |
| RT-47 | "this was the last run in this line" | the question has been settled and the line can be retired | the cheapest and most obvious follow-up — a fitted classifier on the four-answer target at all eleven positions — has not been run | serious |

### RT-44 — the headline claim is not supported, and the record contradicts it

**Fatal. ARGUED, resting on the measurements in RT-33 and RT-34.**

"The linear-read line of attack on these checkpoints is closed" will be
read in the status file, in a paper and in public as: *we looked for a
linear self-index with linear methods and there is none to find.* The
measurement supports something much narrower: *nearest-class-average
distance in the raw state space finds none.* Those are different claims,
and the gap between them is not academic — it is the difference between
0.2500 and 0.4800 on seed 1 at the marker position, which is in the
committed record.

A paper that says "we closed the linear read" and is then asked "did you
try logistic regression?" has no good answer, because the honest one is
"we tried it only on a target we had already shown was unrecoverable, and
in the one place we tried it on a good target it beat our method by
roughly two to one, and we did not report that."

### RT-45 — "the instrument demonstrably works"

**Serious. MEASURED, via RT-33.** The sentence is true of the one thing
the positive control tests: the read can recover a token that is present
at the position being read. It is not true in the sense a reader will take
it — that the read is a competent linear probe whose null is worth
something. The record shows it scoring about half what an ordinary fitted
classifier scores on a well-posed target at the one position where both
were run. "The instrument works" should be replaced with "the instrument
recovers the input token", which is all that was shown.

### RT-46 — eleven positions of seventy-one

**Serious. ARGUED.** The session's own narrower statement already makes
this point, and makes it well. I add only that the eleven positions were
chosen because they are the structurally interesting ones, which is the
right way to choose them, and that it still leaves about sixty tokens
unread — every token of the other agents' turns apart from the one
reviser's two, and almost all of the first eight turns. I could not verify
the figure of seventy-one tokens from the listed records; it is consistent
with the template the code uses (a one-token prefix and ten turns of seven
tokens each), but no record states the episode length.

### RT-47 — "this was the last run in this line"

**Serious. ARGUED.** Retiring the line is a decision, not a measurement,
and it is being taken one obvious experiment too early. The first sweep's
own findings list rerunning the two-instrument comparison against a
well-posed target as open item 5. It remains open. Until it is closed the
line has not run out of cheap questions, and stopping here means the
strongest claim the sequence makes is the one claim it did not test.

### Is the session's narrower statement the right wording for the status file?

**Nearly, and not quite.** The session wrote:

> The honest statement is narrower and duller: a linear difference of
> averages, at the positions and layers we chose, does not find one.

That sentence is **true, and it is the right instinct**. It names the
instrument instead of the class of instruments, which is exactly the
correction RT-44 asks for. Two things stop it being sufficient on its own.

It appears in a paragraph whose heading and surrounding text say the
linear-read line is closed, so a reader takes the narrow sentence as a
modest restatement of the broad one rather than as a replacement for it.
The broad sentence is the one that will be quoted.

And it omits the fact that makes the distinction bite. "A difference of
averages does not find one" reads as a technicality unless the reader also
knows that a fitted linear read, on these states, at the one position
where both were tried, found a great deal more. Without that, nobody will
understand why the narrower wording was chosen, and the broader wording
will creep back.

**The sentence I would put in the status file**, in place of any claim
that the linear-read line is closed:

> Across eleven positions and five layers on all three 30-million-parameter
> checkpoints, a difference-of-averages read finds no own-agent identity —
> neither the model's own marker word nor its register index — anywhere
> except at the token where the marker is the current input. The controls
> held: the read recovers that input token at up to 159 standard
> deviations, and the negative control shows no leak. What this closes is
> the difference-of-averages read, not the linear read: a fitted linear
> classifier was never run at any of these positions against a well-posed
> target, and in the one place both were tried it read the register index
> at about twice the accuracy. The registered probe position is a stronger
> result than the rest, because both instruments find nothing there.

If that is too long, the part that must survive is the third sentence.

---

# The kill case

*Required whether or not the interpretation should stand.*

The kill case is that this sequence mistook the exhaustion of one
instrument for the exhaustion of a class of instruments, and wrote the
stronger sentence. Every number in the eleven-position sweep is correct,
every control behaved, the pre-commitment is real and I verified it three
ways — but the sweep measures straight-line distance to a class average in
a state space the stack itself has measured to be wildly lopsided, where
ten directions out of 448 hold 99 per cent of the variation. In such a
space that measurement is blind to any signal living in a quiet direction,
and I have shown both by simulation at the stack's own measured geometry
and, more damningly, from the stack's own committed records on its own
checkpoints, that the gap between this read and an ordinary fitted linear
read is about a factor of two in accuracy and the difference between
clearing zero of fifteen tests and fifteen of fifteen. On seed 1 at the
marker position the sweep's read returns exactly chance on a signal a
logistic regression reads at 48 per cent. That comparison sat in
`probe_target_diagnostic_a3_*.json` while four successive findings files
were written, and none of them reports it; the first sweep's own findings
even listed rerunning that comparison against a well-posed target as open
item 5, and it was never done. So the line "the linear-read line is
closed" describes an experiment nobody ran, one that would cost an
afternoon with machinery that already exists in this repository. The
narrow, dull, correct claim — a difference of averages at eleven chosen
positions finds nothing, and the registered probe position is empty under
two instruments rather than one — is a real result and worth recording.
The broad one should not enter the status file, and if this line of work
is to be retired, it should be retired after the four-answer target has
been put through a fitted classifier at all eleven positions, not before.

---

## What I would do next, in order

1. **Run the fitted classifier on the register index at all eleven
   positions**, 4,000 episodes, 1,000 draws, three checkpoints. Four
   answers, so it is affordable; the code exists in
   `probe_target_diagnostic_a3.py`. This is the measurement that decides
   whether "linear-read line closed" is true or false. It needs its own
   committed method file and its own cells.
2. **State the smallest detectable signal** in any future findings file of
   this kind. The numbers are in this review (RT-37) and they help the
   result.
3. **Do not let the legibility gap between checkpoints disappear.** Either
   explain it or restore the qualification the first sweep's findings put
   on nulls from seeds 1 and 2 (RT-36).
4. **Drop the claim that the register index is demonstrably carried**
   (RT-35). Everything observed at the marker position is below what the
   marker token alone determines.
5. Report the two degenerate tests (RT-38), and correct the file dates
   (RT-43).

## How the checks in this review were run

Everything is reproducible from the listed records alone. The
recomputations of the published numbers, the family-bar arithmetic, the
smallest-detectable-signal figures, the per-position aggregates, the
degeneracy scan and the rank ceiling are plain arithmetic over the fifteen
records and need nothing else. The geometry simulation in RT-34 copies the
sweep's scorer and its fold construction verbatim from
`powered_target_test_a3.py` and `denoised_direction_a3.py`, uses the
spectrum reported in `denoised-direction-findings.md`, and compares against
shrinkage discriminant analysis from scikit-learn at the sweep's own
episode count, class count and fold count. It uses 100 permutation draws
rather than 1,000, which is ample for estimating the spread of a null and
is the only place any setting differs from the sweep's own.

No checkpoint file was opened and no model was run.
