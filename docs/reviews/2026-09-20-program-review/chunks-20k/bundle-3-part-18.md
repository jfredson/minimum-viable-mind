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
