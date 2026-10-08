# Check of the four 10-million development runs (arms M, T, C, F, seed 0)

*Written 2026-10-04 (Pacific; the work ran 2026-10-05 from 00:50Z) by a
Claude Code checking session, and finished 2026-10-06 (15:29Z to 17:20Z) by
a second checking session that also wrote none of the code, launched none of
the runs and wrote none of the ledger rows, on branch `check-dev-10m`, cut
from the main line at `53ae82c`. Method committed and pushed first, at
`b55dcd3` (`docs/2026-10-04-development-runs-check-method.md`). Laptop,
processor only. Nothing rented, nothing created, nothing trained, nothing
spent: $0. Vendor contact was read-only (machine list, balance, billing
rows).*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (this session ran something, or read it off a file, and says
which) or **ARGUED** (a judgement, with its reasons). The runs were a
pipeline and speed check, not a verdict on learning (version 4, section 11,
step 4). Nothing below is a result about the scientific question. Some of it
is about whether the arms are still what they were built to be, which the
registered runs depend on.*

**The pairing rule.** This session did not write the successor code (pull
request 97), did not launch the runs, and did not write the ledger rows (pull
request 98). It did not open the transcript of any session that did.

**Why it was finished by a second session.** The first session ran the
laptop procedure on arm T alone (1,749 seconds, row written), then started
arms M, C and F together at about 01:25Z. Their printed output stops at
01:37Z after the gate line and some hundreds of solver warnings, with no
error and no row file: the session was cut off, the procedure did not fail.
The second session reran M, C and F from the start, one at a time, with the
command the method names (C 2,159 s, M 1,607 s, F 2,608 s), then ran
`summarise`. Arm T's completed row was kept, not rerun. Everything else
below was written by the first session and checked by the second against the
new rows; where the second changed it, it says so (sections 6 and 7).

## In short

| Purpose (go packet, section 1) | Verdict |
|---|---|
| 1. The frozen trainer runs end to end on a rented machine, every arm, arm M for the first time | **Holds** |
| 2. The shutdown order (copy, check, receipt, delete) works | **Holds** |
| 3. The spending tripwire meets real billing | **Does not hold** |
| 4. The time per step is measured on the card | **Holds** |

Two findings matter more than the four verdicts:

- **The built-in ownership answer went flat in arms C and M** (MEASURED,
  section 6). In both, the learned sharpness that turns the acting channel
  into "which agent am I" fell from 4.0 to about zero (C −0.089, M −0.008),
  so the answer puts a quarter of its weight on each agent and says nothing.
  On the toy it stayed alive (C 0.70 to 1.73, M 2.42 to 2.84). Arm C's
  entanglement and arm M's separable route are both built on that answer, so
  at 10 million neither arm is the thing it was built to be. This is version
  4's weakness W3 ("an arm C whose construction did not hold") seen for the
  first time, at the development size.
- **Arm T's dip is a lookup that confuses particular agent names, and its
  reading still holds** (MEASURED, section 5). Every one of arm T's
  own-directed errors is a wrong row chosen from its table, and they fall on
  six specific pairs of name words: whenever, say, the model is the agent
  called `m5` and an agent called `m4` is also in the episode, arm T picks
  `m4`, every time. Its ownership answer itself is right on every episode.
  Its registered reading is still 0.0000, valid, with its controls holding.
- **The laptop procedure runs end to end on all four real checkpoints**
  (section 7). Arm T is read (0.0000); arms C, M and F return no verdict
  because the procedure cannot find ownership in their running state, which
  for C and M is the flat answer above seen a second, independent way.

## What this session opened

- Every file the runs brought home, read in place in the main checkout:
  `experiments/08-successor-degree/artifacts/succ_{m,t,c,f}_10m_seed0/`
  (checkpoint, training log, trajectory log, finished-marker, watchdog log,
  the machine's reaper log, machine-deadline log, run settings) and
  `artifacts/tripwire/dev-10m/` (state, watcher log, process id).
- The go packet, `docs/rulings/2026-10-04-development-runs-go-PROPOSAL.md`.
- Pull request 98's description and its ledger diff (branch
  `dev-10m-actuals`).
- The frozen code in `experiments/08-successor-degree/src/` where a finding
  needed it (`models.py`, `train_successor.py`, `tripwire.py`, `procedure.py`,
  `grammar.py`).
- Version 4, sections 5.1, 5.2, 8.1, 11 and weakness W3, found by search and
  read with their surrounding text; not read end to end.
- The rehearsal's committed toy models and gate file,
  `experiments/rehearsal-successor-measure/out-repairs/models/` and
  `out-repairs/gate_base.json`.

This session's scripts and their outputs are beside this file, in
`2026-10-04-development-runs-check-scripts/`. The laptop procedure's outputs
are in `experiments/08-successor-degree/out-dev-10m-check/`.

---

## 1. Purpose 1: the trainer ran end to end on every arm. Holds.

**MEASURED** (`checkpoints_end_to_end_output.txt`; the four training logs).
For every arm: the recipe line names 108,919 steps of batch 96, learning
rate 0.002, the token budget; there is an evaluation line every 2,000 steps
to step 108,919; the data stream skipped no batch; the log ends with the
finished-marker (`{"step": 108919, "tokens": 585548544}`) and `TRAINING
COMPLETE`. Each checkpoint loads strictly into the frozen model code on the
laptop and records step 108,919 of 108,919 with 55 evaluations logged. Arm
M's code, never before run on a rented machine (weakness W9), ran to the end
like the others.

That the trainer ran is all this purpose asks. Whether what it trained is
what the arms were built to be is section 6, and the answer there is no for
two arms.

## 2. Purpose 2: the shutdown order worked for every run. Holds.

**MEASURED** (the four `watchdog.log` files; `checkpoints_end_to_end_output.txt`;
`vendor_reads_output.txt`). Each watchdog log shows, in order and with
nothing failing between: "final fetch OK", "final checkpoint VERIFIED (md5
...)", "receipt written on the machine", "deleting pod", "pod gone; billing
stopped". The md5 of each checkpoint now on the laptop matches the one the
watchdog verified (first 12 characters, all four). The vendor's machine list,
read at 00:56Z, was empty.

| Run | Machine created | Training finished (machine's reaper) | Pod gone (watchdog) | Machine life |
|---|---|---|---|---|
| arm M | 00:11:18Z | 00:38:47Z | 00:40:02Z | 28.7 min |
| arm T | 00:14:40Z | 00:34:10Z | 00:34:56Z | 20.3 min |
| arm C | 00:17:47Z | 00:37:30Z | 00:38:01Z | 20.2 min |
| arm F | 00:20:51Z | 00:39:07Z | 00:40:22Z | 19.5 min |

Two things around the order, neither a failure of it:

- The machine's own reaper logs end at "waiting for the receipt": the laptop
  deleted each machine within about 15 seconds of writing the receipt, before
  the reaper acted. The reaper's own deletion was therefore never exercised.
  That is the order working as designed (the laptop deletes first; the reaper
  is the backstop).
- The four laptop deadline processes were stopped by hand at 00:51:15Z (a
  note is appended to each `machine-deadline.log`). They do not notice that
  their machine is gone, so left running they would have written false
  "DEADLINE REACHED ... $2.50" lines at 02:42Z to 02:52Z (pull request 98
  says the same). See section 8, change 3.

## 3. Purpose 3: the spending tripwire did not meet real billing. Does not hold.

**MEASURED** (the state as it stood at 00:52Z, copied before it changed, in
`tripwire-state-snapshot-0052Z/`; the state and log after the watcher's last
reading, in `tripwire-state-after-0111Z/`; `tripwire_after_the_fact_output.txt`;
`vendor_reads_output.txt`).

The test written in the method was: while machines were running, did the
tripwire compute a billing ratio over a span long enough for its own rules to
act on it (0.9 hours for the watcher, 0.5 for preflight)? It did not.

- **Ratio B (balance drawdown against the posted rate) during the wave.** The
  watcher reads once an hour. It read once at 00:11:19Z ("ratio B 0.000", one
  reading, no span), then slept until 01:11:20Z, by which time every machine
  had been gone for 31 to 36 minutes. Preflight read the balance before each
  of the four machines, over at most 9 minutes, below its half-hour rule, so
  it never computed a ratio either. During the 29 minutes that money was
  being spent, the tripwire could not have tripped on anything but a failed
  read.
- **Its one real ratio was wrong by more than half.** At 01:11:20Z the watcher
  read the balance ($72.3080), marked all four machines gone *at that
  moment*, computed **ratio B 0.401** and exited ("done"). It had never
  recorded the deletion times, so it charged every machine as if it had run
  until 01:11. With the deletion times from the watchdog logs, the same
  arithmetic (the frozen `ratio_b`) gives **0.990** over the wave: drawn
  $1.4565 against $1.4713 expected. Billing was normal; the tripwire would
  have said so, but by luck of direction: the same error understates any
  overbilling by the same factor, which is the case it exists for.
- **Ratio A (the vendor's billed hours against machine life) cannot be read
  yet, and the frozen code reads that as a pass.** At 00:56Z the vendor's
  billing rows for all four machines were empty (`[]`). `tripwire.py
  reconcile`, run on a scratch copy of the state with the true deletion times,
  printed "billed 0.000 h ... ratio A 0.0" for each machine and exited 0, no
  trip. Billed hours of zero for a machine that existed is not a reading; it
  is a check that cannot yet run, which version 4 section 12.7 says counts as
  a trip, not a pass. Run on the real state folder, it would also have used
  the wrong lifetimes: before 01:11Z arm M's "last seen" one second after
  creation (a false trip), after 01:11Z the late deletion times (about half
  the true ratio). This session did not run it on the real folder.

What the wave did show about money, MEASURED: the balance fell from $73.7742
(before arm M) to $72.3178 (00:56Z), $1.4565, which matches machine life
times $0.99 an hour ($1.4655) less the storage drip within a cent. Nothing
came near its $2.50 cap. Pull request 98's figures agree with this.

## 4. Purpose 4: the time per step was measured on the card. Holds.

**MEASURED** (the training logs' `sec_per_step`, steady from step 2,000 to
the end in every run):

| Arm | Seconds per step on the card | Training time | Against the packet's estimate (about 0.017) |
|---|---|---|---|
| T | 0.0099 | 18.0 min | 0.58 times |
| C | 0.0100 | 18.2 min | 0.59 times |
| F | 0.0093 | 16.9 min | 0.55 times |
| M | 0.0145 | 26.3 min | 0.85 times |

Every run finished well inside the low end of its estimate (0.6 hours of
machine life) and far inside its cap.

**Arm M's slower step.** The method expected that arm M might simply do more,
smaller operations per step. **MEASURED** (`op_count_output.txt`): it does
not do enough more to explain it. Counted on the processor, one training step
of arm M runs 1.11 times as many operator calls as arm C (13,199 against
11,933), while its step on the card took 1.44 times as long. Arm F runs 0.69
times arm C's calls and took 0.93 times as long. So the operation count does
not track the card's times, and the simple explanation fails.

**ARGUED, from reading the code, not tested on a card:** arm M is the only arm
whose forward pass builds a tensor from a Python list on every step,
`torch.as_tensor(ENTANGLED_ITEM_IDS, device=...)` in
`MiddleArm.entangled_route` (`models.py`). On a graphics card that is a copy
from the processor's memory, which makes the processor wait for the card to
finish its queued work before it can carry on. The other arms never wait, so
the processor keeps queueing work ahead of the card. At this small size the
card spends much of its time waiting for work, so losing that overlap could
plausibly cost about half again. The alternative is that arm M's machine was
simply slower (each run had its own machine, at a different address). This
session cannot tell the two apart without a card. The fix, if it is the cause,
computes nothing differently (the five item ids stored once on the model), but
the code is frozen, so it is John's call (section 8, change 5).

What this reprices: the 10-million times are not the registered-size times.
Version 4's step 5a takes the registered-size timing from the first arm F run
at 30 million; these figures say only that at 10 million the card is faster
than the packet assumed and that arm M costs about half again per step.

---

## 5. Arm T: what happened, and whether it threatens the registered runs

### 5.1 What the logs show

**MEASURED** (`train_succ_t_10m_seed0.log`). Own-directed and named-other
accuracy on the 400-episode watch set were both 1.0 from step 2,000 to
14,000, with training loss printed as 0.0. The learning rate peaks at step
10,892 (the first tenth of 108,919). Own-directed fell to 0.77 at 16,000 and
0.585 at 20,000, recovered unevenly to about 0.89 by 48,000, and ended at
0.8925. Named-other stayed at 1.0 to about step 50,000, then drifted to
0.9625.

### 5.2 Where the own-directed errors come from

**MEASURED** (`arm_t_errors.py`, output `arm_t_errors_output.txt`), on the
registered 3,000 gate episodes:

- Arm T gets 2,750 own-directed and 2,913 named-other actions right (0.917,
  0.971).
- **Its ownership answer is right on every episode.** The answer it computes
  from the acting channel puts its highest weight on the agent the model
  actually is in 3,000 of 3,000 episodes. The learned sharpness of that answer
  has halved (1.95, against 4.0 at the start and 3.88 on the toy), so the
  answer is less peaked (0.94 average top weight, against 0.999 on the toy),
  but it is never wrong.
- **What goes wrong is the next step: choosing the table row with it.** The
  row chosen is the right agent's in 2,586 of 3,000 episodes. Where it is
  right, the action is right every time (no errors). Where it is wrong (414
  episodes), the action is right in 40% of them, by coincidence of values; all
  250 own-directed errors are there. The choice is confident, not spread: the
  chosen row gets essentially all the weight.
- **Forcing the right row fixes it.** With the row forced onto the right agent
  and nothing else changed, 2,999 of 3,000 own-directed actions are right. The
  table and the rule are sound.
- **The wrong choices are confined to six pairs of agent name words, and are
  certain within them.** The agents in an episode are labelled with name
  words `m0` to `m11`. When the model is the agent named `m5` and an agent
  named `m4` is also present, arm T chooses `m4`'s row in 76 of 76 such
  episodes. The same holds, every time, for `m1` with `m0` (62 of 62), `m1`
  with `m3` (75 of 75), `m3` with `m0` (73 of 73), `m10` with `m0` (63 of 63)
  and `m11` with `m8` (79 of 79). Six of the twelve name words are never
  confused. The error does not depend on which agent number the model is
  (0.86 to 0.87 right for each).
- **The toy arm T (seed 0) has none of this**: right row in 3,000 of 3,000, no
  confused pairs.

**ARGUED: what this is.** The row is chosen by comparing a query made from
the ownership answer with a key made from each agent's name word, and both
are built from the name word's embedding, which the rest of the network also
trains. Some of those embeddings have moved so that, for these six pairs, the
wrong name's key matches better. The 1.0 to 0.585 fall right after the
learning-rate peak is when that happened; training repaired most pairs and not
these six. The method named weight decay softening the choice as one possible
cause; the data does not fit that (the choice is sharp, not soft, and the
errors are pair-specific), so that idea is dropped.

### 5.3 Its reading

**MEASURED** (`out-dev-10m-check/row_T_seed0.json`). The registered procedure
nominated layer 0 at the action position with a piece of 8 directions, the
whole read and the piece each right on 180 of 180 held-out episodes: the same
site set the toy chose. On fresh episodes the reading is **0.0000, valid**:
the ownership-only transplant and the whole-state transplant both change the
action in 0.8325 of trials, against 0.0225 with no transplant (inside its
allowance). Controls 1, 4 and 7 hold; control 3's twenty random pieces all
fall below the ownership piece (0.0225 to 0.0325 against 0.8325); control 2
is not applicable to arm T (ruled). The gate clears easily (2,750 and 2,913
against a bar of 790). The true-slot reference also reads 0.0000.

One figure differs from the toy: **under the stricter variant** (no layer 0)
the site moves to layer 1 at the action position, as on the toy, but reads
**0.0802** there (ownership-only 0.7675 against whole 0.8325), where the toy
read 0.0000 (version 4, section 5.1). The stricter variant is a reported
sensitivity, not the registered figure.

### 5.4 Does it threaten the registered runs?

**ARGUED.** Not as an anchor, yet. Arm T's construction held: its ownership
answer is in its own slot and is right, the action has no other route, and the
registered reading is 0.0000. What the 10-million run shows is that the
recipe can damage the lookup arm T's action depends on, and that the damage
lowers the ceiling the reading is computed under (0.8325 rather than near
1.0) and nudges the stricter variant off zero. At the registered size the same
recipe (learning rate 0.002 with a one-cycle schedule, the same long run)
could do the same or worse, and nothing in the procedure would flag it except
the accuracies. The cheap protection is to report, for arm T, the row-choice
split this check computed, beside its gate (section 8, change 6). Whether to
change the recipe for arm T is not this check's to say: the arms are meant to
differ only in architecture.

---

## 6. Arms C and M: the built-in ownership answer went flat

This was not in the method. It was found while checking arm M's route with
the arm T script, and then measured on every checkpoint
(`ownership_answer_sharpness.py`, output `ownership_answer_sharpness_output.txt`;
`arm_m_selection_output.txt`).

**What the answer is.** Every arm computes a built-in ownership answer from
the acting channel: a running count of how often the "this turn is yours"
signal fired on each agent's turns, turned into weights over the four agents
by a softmax with a learned sharpness that starts at 4.0. Arm T uses it to
choose its table row; arm C feeds it into every block as a scale-and-shift on
the whole running state and multiplies it into the values at binding (version
4, section 5.2); arm M does both, by item. Arm F computes it and does not use
it.

**MEASURED, the learned sharpness and the weight the answer puts on the agent
the model actually is, on the 3,000 gate episodes:**

| Model | Sharpness | Weight on the true agent |
|---|---|---|
| arm T, 10M | +1.947 | 0.942 |
| **arm C, 10M** | **−0.089** | **0.218** |
| **arm M, 10M** | **−0.008** | **0.247** |
| arm F, 10M (unused, never trained) | +4.000 | 0.999 |
| toy arm T, seeds 0 to 2 | +3.88 | 0.999 |
| toy arm C, seeds 0 to 2 | +1.73, +0.70, +0.93 | 0.914, 0.573, 0.681 |
| toy arm M, seeds 0 to 2 | +2.84, +2.69, +2.42 | 0.990, 0.986, 0.977 |

A quarter (0.25) is what a flat answer puts on each agent. At 10 million, arms
C and M carry no ownership through the built-in answer at all; the sharpness
was driven through zero, which weight decay alone cannot do (it shrinks
toward zero, never past it), so training pushed it there (ARGUED from the
sign).

**What that does to arm M** (MEASURED, `arm_m_selection_output.txt`). Its
separable route, which answers actions about items it0 and it4 (40% of
own-directed actions), chooses the right agent's row in only a quarter of
episodes, as a flat answer must, yet gets **every** own-directed action on
that route right (1.000), and forcing the right row changes nothing (1.000).
So on arm M's separable route the action no longer depends on the ownership
slot at all. (The first session added that the network carries
who-the-model-is in its running state and writes it into the table; section
7 corrects that: the procedure's read does not find it there.) The
"separable by construction" half of arm M is not separable at 10 million. The
toy arm M, by contrast, chose the right row on every episode.

**What that does to arm C** (ARGUED, from the code and the figures). With the
answer flat, the scale-and-shift every block applies carries no identity, so
nothing in arm C's construction entangles ownership any more. Whatever
ownership it uses comes in through the acting channel and the attention
layers, the same free route arm F has. Its accuracy says the same: arm C ends
at 0.595 own-directed on the watch set, arm F at 0.5975.

**Whether this threatens the registered runs. ARGUED: yes, and it is the
largest threat this check found.** The validation step reads the measure on
arms T and C and asks whether they separate. If arm C's construction does not
hold at the registered size, arm C is a second free model, its reading is
whatever such a model gives, and the validation is not testing what it says
it tests. Version 4 names exactly this risk as W3 and says that under the
launch order it is seen only after both releases are drawn (section 11, step
5b). At 10 million it has now been seen, for nothing extra, before the
registered runs. Two cautions: 10 million is not 30 million, and the
development size was registered in advance as telling nothing about
learnability; but this is not a learnability finding, it is a finding that a
trained parameter switched a built-in route off, and nothing about the larger
size makes that less likely.

The laptop procedure's readings on arms C and M are in section 7.

## 7. The laptop procedure on all four checkpoints

**MEASURED** (`out-dev-10m-check/row_{T,C,M,F}_seed0.json`, `table.md`,
`summary.json`; registered counts, episode scale 1.0, 200 null shuffles).
The procedure ran end to end on all four real 10-million checkpoints, on the
processor, in 27 to 44 minutes each, without error. Nothing here is read as
a result about learning or the question.

| Arm | Gate: own / named-other right of 3,000 (bar 790) | Ownership read, best layer, held-out right of 180 (floor 144) | Site set nominated? | Reading |
|---|---|---|---|---|
| T | 2,750 / 2,913 | 180 (layer 0) | yes: layer 0, action, 8 directions | **0.0000, valid**, controls 1, 4, 7 hold |
| C | 1,700 / 1,701 | 41 (layer 4) | no: no piece reaches four fifths | no verdict (arithmetic 0.99, described only) |
| M | 2,592 / 1,755 | 45 (layer 8) | no: same reason | no verdict (arithmetic 1.00, described only) |
| F | 1,689 / 924 | 22 (layer 1) | no: same reason | no verdict (arithmetic 0.99, described only) |

The read's labels are the twelve name words, so a read that knows nothing
gets about 15 of 180. Every arm's own gate passes and every arm's ownership
lesion collapses its own-directed accuracy (lesioned: T 758, C 526, M 579,
F 435).

What this adds:

- **Arm T** is as section 5.3 says (that section was written from the same
  row).
- **Arms C and M: the procedure cannot find "which agent am I" in their
  running state at all**, at any of the nine states, at the action position
  where the read is fitted (C 13 to 41 of 180, M 26 to 45, against a floor of
  144). On the toy the same read found it at 180 of 180 for both arms (the
  pull request 97 freeze tests, `out-freeze-tests/t3a-committed-reads/`). This
  is the procedure's own registered route reaching section 6's finding
  independently: with the built-in answer flat, the constructed arms carry no
  readable ownership where the procedure looks, so they return no verdict.
  Arm C's named-other read, by contrast, is 180 of 180 at layers 1 to 6: the
  network reads names fine; it is the self that is missing.
- **Arm F** reads at about chance (10 to 22 of 180); its named-other gate
  (924) clears the bar narrowly.
- **`summarise` says every arm "failed its gate", and the outcome "substrate
  not a testbed".** That is an artefact of one seed per arm, not a finding:
  the registered rule passes an arm's gate on two seeds of three, and one seed
  can never make two. Each row's own gate passes. The development runs were
  registered as telling nothing about the outcome, and this line is not one.
- **Correction to section 6, arm M.** The first session wrote that arm M
  "carries who-the-model-is somewhere in its running state ... and writes it
  into the table". The procedure's read finds no such thing at the action
  position (best 45 of 180). Where arm M's separable route gets its answer
  from is therefore not located by this check; that it does not come through
  the ownership slot (section 6) stands. A side observation, ARGUED: the toy
  arm M and the 10-million arm M get exactly the same own-directed count
  (2,592) and the same entangled-route accuracy (0.7746) on the gate
  episodes, which suggests that figure is a ceiling set by the episodes rather
  than by either model; not checked here.

## 8. What should change before the registered runs

Each is a change to frozen code or to the plan, so each is John's ruling.

1. **The tripwire must read during the wave, not hourly.** Ratio B over a
   wave this short needs readings every few minutes and a rule that can act on
   less than 0.9 hours, or a ratio computed at each machine's deletion. At the
   registered size a run is longer, but the first arm F run (step 5a) is the
   one whose billing is meant to be checked before anything else launches, and
   the tripwire should be shown working on real billing before then; this wave
   did not show it.
2. **Deletion times must be recorded when the machine is deleted**, by the
   watchdog's "pod gone" step writing them into the tripwire state, not
   guessed at the watcher's next reading. Without that, both ratios use the
   wrong lifetimes: here ratio B read 0.401 instead of 0.990, and ratio A would
   have tripped falsely or read about half.
3. **`reconcile` must treat empty billing rows as a check that cannot yet run**
   (a trip, or at least "not read"), not as ratio A of zero. As written it
   passes a machine the vendor has not yet billed.
4. **The laptop deadline process should stop itself when its machine is
   gone**, so it cannot write a false "DEADLINE REACHED ... $2.50" line.
5. **Arm M's per-step copy (ARGUED cause of its 1.44 times slower step):**
   store the item ids once on the model. It changes nothing the model
   computes. Worth doing only if John wants arm M's three registered runs
   cheaper; worth confirming on the first card it runs on.
6. **Report arm T's row-choice split** (right row, accuracy where right and
   wrong, confused name pairs) beside its gate, so a damaged lookup is seen as
   such.
7. **Before the registration text: a ruling on arms C and M's flat ownership
   answer** (sections 6 and 7; the procedure's own read now confirms it). Options this check can see, without recommending
   among them: (a) hold the learned sharpness fixed at its starting value in
   the constructed arms, so the construction cannot be switched off (a change
   to what the arms are, needing its own check on the toy); (b) exclude it
   from weight decay and add a check that it stays above some value; (c) add
   to the procedure a test that the constructed route is in use (as this check
   did with the flat answer and the forced row), and treat a construction that
   did not hold as a no-verdict for that arm; (d) accept the risk as W3
   already does. The first two would want a short rerun at 10 million to show
   the construction now holds, which is a spend and needs a go.

8. **`summarise` on fewer than three seeds** should say "gate not decidable
   on one seed" rather than "failed its gate", so a development folder cannot
   print a false outcome line. Small, reporting only.

## 9. What this does not do

It does not read the figures as anything about learning or about the
question. It did not run anything on a card, so the cause of arm M's slower
step is argued, not shown. It did not test why arm T's lookup confused those
six name pairs (that would need training). It did not check the frozen code
as a whole: the TimeAssembler step's title also names that, and the code
freeze's own findings (`docs/2026-10-04-successor-code-freeze.md`, section
4.1, the toy landing on "substrate not a testbed" under the rules as written)
were not re-examined here. It did not change any file in the main checkout's
artifact folders, and it ran `reconcile` only on a scratch copy.
