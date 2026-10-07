# Check of the ruling packet on arms C and M (pull request 109)

*Written 2026-10-06 (Pacific) by a Claude Code session that did not write the
packet, on branch `check-cm-packet`, following the method committed first
(`docs/2026-10-06-cm-packet-check-method.md`, commit `a1094e2`). $0: nothing
rented, trained or spent; no project code changed. The packet checked is
`docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md` at commit `79bd26d`.*

## In short

**The figures hold; one description is wrong; the options table needs four
changes before John rules from it. The recommendation (fix the sharpness and
add the in-use check) still stands, once its scope and its schedule cost are
stated.**

- Every number the packet uses matches its source or recomputes from it
  (table in section 1).
- **One factual error, in three places and the pull request text:** the runs
  are called "10-million-*step*" runs. They are 10-million-*parameter* runs
  of 108,919 steps each. The recommended rerun is "at 10 million steps" in
  the pull request text; it should be at the 10-million-parameter size.
- **The weight-decay reasoning reaches the right conclusion by a weak
  route.** "It went past zero, so decay cannot have done it" is not sound
  near zero. The sound argument is the size: over these runs decay alone
  would have taken the sharpness from 4.0 to about +1.34, not to zero, and
  arm T, under the same decay, ended above that (+1.95). So training did
  push it down in arms C and M, and option 2 would not by itself stop it.
- **The options are not quite even-handed:** option 2 is a weaker version of
  what the source offered; option 1 does not say whether arm T (also a built
  model, whose sharpness also fell) is included; the recommendation's time
  cost before the 2026-10-18 deadline is not stated while option 4's
  downside is; and option 4 is not described as what version 4 already
  chose ("the two-arm fallback rather than a repair").
- **Page 12 is fairly framed and nothing is presented as ruled**, but it
  should say that it changes a condition John already said to "go with", and
  that the decoy test's "not fooled" comes with a limit its own authors
  stated.
- **Page 2:** the fourth fix understates what the deadline timer is: it
  deletes the machine at its cap; it is the cost backstop, not just a
  recorder.

## 1. The figures: all supported

| Packet says | Source | Holds? |
|---|---|---|
| Sharpness starts at 4.0 | `models.py` (pull request 106 branch): `nn.Parameter(torch.tensor(4.0))` | yes |
| Arm C 4.0 to −0.09; arm M to −0.01 | Pull request 106, section 6 table: C −0.089, M −0.008 (script output −0.0886, −0.0083) | yes, to rounding |
| A flat answer puts a quarter on each agent | Pull request 106, section 6: weights on the true agent 0.218 (C), 0.247 (M) | yes |
| The procedure finds "which agent am I" at best 41 and 45 of 180; pass mark 144 | Pull request 106, section 7 table (C 41 at layer 4, M 45 at layer 8; floor 144) | yes |
| Arm T still works | Section 7: arm T read 180 of 180, reading 0.0000, valid | yes (but see finding 6) |
| Toy models: the number stayed alive in every arm | Section 6 table | yes as worded (but see finding 6) |
| Version 4 expected to see this only after both money releases | Version 4, section 11 step 5b and weakness W3 ("seen only after both releases are drawn") | yes |
| Rerun of arms C and M about $0.81 | Ledger rows (pull request 98, commit `d7581d9`): arm C $0.3341 + arm M $0.4744 = $0.8085, by machine life at $0.99 an hour | yes |
| $8.53 left on the development line | Same ledger rows: "development line about $8.53 of $10 left" | yes |
| John's 2026-09-20 ruling: fallback to arm T and the free model accepted in advance | Version 4, section 5.2: "the two-arm fallback is accepted in advance" (ruled 2026-09-20) | yes |
| The fallback shows the measure detects, not that it scales | Version 4, section 5.2, "Why the fallback is weaker" | yes |
| About $194 to $206 | Version 4, section 11 step 5b: "costs the whole successor, about $194 to $206" | yes |
| Registration deadline 2026-10-18 | `data/project.toml`, `data/roadmap.toml`: kill date 1 | yes |
| Billing normal: $1.46 against $1.47 expected | Pull request 106, section 3: drawn $1.4565 against $1.4713 | yes |
| Wave lasted 29 minutes | Section 3: "the 29 minutes that money was being spent" | yes |
| Ratio 0.40 where the true figure was 0.99; machines charged as if run until 01:11 | Section 3: ratio B 0.401 against 0.990; all marked gone at 01:11:20Z | yes |
| Section 12.5 registers "hourly" | Version 4, section 12.5: "It runs in flight, hourly, on ratio B" | yes |
| Section 12.7: a check that cannot run is a trip | Version 4, section 12.7 | yes |
| Empty bills read as zero hours, passed | Section 3: "billed 0.000 h ... ratio A 0.0 ... exited 0, no trip" | yes |
| Deadline timers stopped by hand; would have written false "$2.50" lines | Section 2 (lines 133 to 136) and the ledger note | yes |
| Page 12: recommendation on record "continue if the decoy test is not fooled" | Rulings record (pull request 103), page 12: "if it is not, continue" | yes (but see finding 7) |
| Decoy test (pull request 108) reports not fooled, unchecked | Pull request 108: "not fooled, both ways round"; open, owed a check | yes (but see finding 7) |

## 2. Findings, in order of weight

### Finding 1. Error: "10-million-step" should be "10-million-parameter"

The packet says "the four 10-million-step development runs" (line 7), "In
the 10-million-step runs" (line 21), and on page 12 "shown to hold at 10
million steps" (lines 56 to 57). The pull request text says "rerun arms C and
M at 10 million steps".

**Correct:** the runs are of the 10-million-*parameter* models (`models.py`,
size "10M": 256 wide, 8 layers), each trained for **108,919 steps** on
585,548,544 tokens, the registered token budget (ledger rows, pull request
98; `out-dev-10m-check/row_*_seed0.json`, `tokens_seen`). A rerun "at 10
million steps" would be about 92 times longer and would not cost $0.81. The
$0.81 figure is right for the runs as they were actually done; only the
description is wrong.

Related omission: the packet never says that the registered size is 30
million parameters. Pull request 106 (section 6) cautions that "10 million
is not 30 million". Page 12's proposed condition, "shown to hold at 10
million ... before registration", should say the registered runs are larger,
so a pass at 10 million is evidence, not proof. (With the sharpness fixed,
it cannot drift at any size; what remains open at 30 million is the risk
option 1 already names, the network routing round it.)

### Finding 2. The weight-decay reasoning: right conclusion, weak argument

The packet says: "Because it went *past* zero, training drove it there;
weight decay ... cannot do that alone", and option 2 "probably does
nothing: weight decay was not the cause".

The sign argument is true of the decay term on its own (the trainer uses
AdamW, whose decay multiplies each number by slightly less than one every
step, so it shrinks toward zero and never crosses it). But it is weak
evidence here: once the number is near zero, the optimiser's own steps,
which are roughly the learning rate in size whatever the gradient's size,
can carry it a little past zero by noise alone. Arm M's −0.008 is well within
that. The sign does not by itself show a push.

**The sound argument is the size,** and it supports the packet's
conclusion more strongly than the sign does. Using the recorded recipe and
PyTorch's own scheduler (script `2026-10-06-cm-packet-check-scripts/decay_alone.py`,
output beside it): over the 108,919 steps, decay alone multiplies a number
by **0.335**, so the sharpness would end at about **+1.34**, not near zero.
Arm T, under the same decay, ended at **+1.95**, above that, so its training
held the number up against decay; in arms C and M training pushed it from
there to zero. (Arm F's stayed at exactly 4.000 because it gets no gradient,
and AdamW skips a number with no gradient, decay included, so arm F says
nothing about decay.)

**So:** "training drove it there" holds; "option 2 probably does nothing" is
fair if read as "would not by itself stop it". "Weight decay was not the
cause" goes slightly too far: decay would have taken it about two-thirds of
the way down on its own, so it may have helped; what it cannot explain is
the last stretch to zero. Suggested wording for the packet: "Weight decay
alone would have left it at about 1.3 over this run, and arm T, under the
same decay, kept 1.9; so training pushed it to zero in arms C and M.
Exempting it from decay would not stop that."

### Finding 3. Option 2 is stated more weakly than its source

Pull request 106's option (b) was "exclude it from weight decay **and add a
check that it stays above some value**". The packet's option 2 keeps only the
first half, then rates it as "probably does nothing". The second half partly
overlaps option 3, but not entirely: a check on the number itself is
narrower and simpler than a check that the whole route is in use.

There is also a middle option the sources point to and the packet does not
list: **keep the sharpness learned but hold it above a minimum** (a floor,
for example by clamping it or by learning it through a form that cannot
fall below a set value). That keeps some of the toy evidence's conditions (the
number was learned on the toy) while stopping it reaching zero. It carries
the same "route round it" risk as option 1. Whether it is better than fixing
at 4.0 is John's call; the point is that it should be on the page.

### Finding 4. Option 1 does not say whether arm T is included

Option 1 is "Fix the sharpness at 4.0 **in the built models**". Arm T is a
built model too (separable by construction), and its sharpness also fell, to
+1.95 (still working: weight 0.942 on the true agent). The packet's cost
covers reruns of arms C and M only.

- If arm T is included, its 10-million run and its 0.0000 reading must be
  redone as well: about **$0.33 more, about $1.14 in all** (ledger: arm T
  $0.3347), still inside the $8.53 left.
- If arm T is left learned, the built arms differ in whether this number
  learns, and the registration should say so and why.

Either is defensible; the packet should say which it proposes. (The source,
pull request 106 option (a), says "in the constructed arms", which includes
arm T, and is equally unclear.)

### Finding 5. The recommendation's costs are not stated as fully as option 4's

The table gives option 4's downside in full ("the fallback becomes the
likely end ... after about $194 to $206") but not the recommendation's
**time** cost: a change to frozen code (the model code was fixed and tested
on 2026-10-04 and is meant to be registered as is), a toy retrain and
re-read, the new in-use check written and tested, two reruns on John's go,
and an independent check of each, all before 2026-10-18, alongside other
owed work in the same code (the training change John ruled on 2026-10-06,
item 8 of the follow-ups in pull request 103; the decision-code work in pull
requests 105 and 107). Twelve days is likely enough, but it is a real cost
and it bears directly on the deadline.

The table also leaves out what is **for** option 4: it is the plan already
on record. Version 4's weakness W3 says that a failure of arm C's
construction "fires the two-arm fallback **rather than a repair**". Options 1
to 3 are repairs, so they depart from a stated design choice. The departure
is reasonable (the failure has been seen before registration, which version
4 did not expect), but John should see that he is changing it, not only
choosing among new options. Option 4's entry should also say that under
version 4 a no-verdict on arm M **drops arm M** (it is carried as an
extension), not only that arm C falls back (version 4, section 9 table,
"What a no verdict maps to").

### Finding 6. "Stayed alive on the toy" is true but leaves out a trend

The toy arm C's sharpness had already fallen from 4.0 to +1.73, +0.70 and
+0.93 on its three seeds (weight on the true agent 0.914, 0.573, 0.681), and
the 10-million arm T fell to +1.95. The drift downward was visible on the
toy, weakest in arm C. This matters for two things the packet says: option
1's risk ("the toy evidence was gathered with the number learned": on the
toy, arm C's built route was already partly weakened), and finding 4 (arm T
is drifting too). One more limit worth a line: each arm at 10 million is one
seed. Both arms C and M went flat, so this is not a fluke, but it is not
three seeds either.

A smaller point of description: version 4's weakness W3, as written,
imagined arm C collapsing into "a second copy of arm T" (ownership
concentrated in one narrow direction). What happened is the opposite end:
arm C became a second freely trained model like arm F (pull request 106,
section 6: arm C 0.595 own-directed, arm F 0.5975). Both are "an arm C whose
construction did not hold", the phrase in version 4 section 11, so calling
it W3 is fair; the packet's paraphrase is fine.

### Finding 7. Page 12: fair, nothing presented as ruled, two things to add

Nothing in the packet is presented as already ruled. The header, the
recommendation and page 12 all say "proposed"; the one thing described as
ruled (the 2026-09-20 fallback) is ruled.

Two additions would make page 12 complete:

- **John's own words on page 12 were "decide after the decoy test, go with
  the recommendation"** (rulings record, pull request 103). The packet calls
  the condition "the recommendation on record", which is accurate, but the
  proposal changes a condition John said to go with. It should say so in
  those terms.
- **The decoy test's "not fooled" carries a limit its authors stated**
  (pull request 108): it shows the read is not fooled by an *exact* copy of
  the owner's marker, not by a copy coded differently, which pull request
  108 calls a new question for John. Page 12's continue condition rests
  partly on that result, so the limit belongs on the page.

### Finding 8. Page 2, fix 4: the deadline timer is the cost backstop

The packet describes each timer as recording "when it hits its spending
cap", and calls the fix "housekeeping only". The timer does more: at its
hard cap it **deletes the machine** (`machine_deadline.sh`, line 58:
"DEADLINE REACHED. Deleting ..."). It is the last line of defence on cost;
the programme lost $97 on 2026-08-12 when a backstop of this kind did not
fire. The fix (stop when the machine is gone) is still right, but it should
carry a condition: the timer stops only on a confirmed deletion (the
watchdog's own "pod gone" record, or the vendor saying the machine does not
exist), never on a failed or empty reading, or the fix could switch the
backstop off by mistake. With that condition it is a correction; without
it, it is a change to a safety control.

Fixes 1 to 3 are accurately stated. On fix 1, a small precision: the hourly
reader was not the only reading; the launch check also read the balance
before each machine, but over at most 9 minutes, below its own half-hour
rule, so it never computed a ratio either (pull request 106, section 3). The
packet's point stands.

Pull request 106's section 8 also lists three items the packet does not
carry (5: arm M's slower step; 6: reporting arm T's row choices; 8: the
summary printing "failed its gate" on one seed). They are outside this
packet's scope, but they remain unruled and should not be lost.

## 3. Plain language

Every pull request number carries a plain label, and weakness W3 is
explained. These terms are used without explanation and should be replaced
or glossed at first use:

| Term in the packet | Plain version |
|---|---|
| "10-million-step runs" | the runs of the 10-million-parameter models (and wrong as written: finding 1) |
| "the floor is 144" | the pass mark is 144 of 180 (four fifths) |
| "the decoy test" | the test of whether the read can be fooled by an unused copy of the owner's marker |
| "frozen model code", "frozen training code" | the code fixed and tested on 2026-10-04, meant to be registered as is |
| "this wave" | the four machines launched together on 2026-10-04 |
| "the development line" | the $10 John approved for development runs |
| "a ratio of 0.40 where the true figure was 0.99" | spending divided by what the posted rate predicts (1.0 means billed as posted) |
| "money releases" | the two blocks of spending John approved in advance for the registered runs |
| "the registered measuring procedure" | the measuring procedure fixed for registration (fine, if "registration" is explained once as committing the plan publicly before the main runs) |

## 4. Does the recommendation still stand?

**Yes.** Nothing found changes the facts the recommendation rests on: the
sharpness went to about zero in arms C and M, training (not decay) pushed it
there, and the measuring procedure independently cannot find ownership in
either. Fixing the number removes that route to failure; an in-use check
catches others. Finding 2 strengthens the case against option 2 alone.

What should change before John rules:

1. "10-million-step" becomes "10-million-parameter" (three places and the
   pull request text), and page 12 says the registered size is 30 million.
2. Option 1 says whether arm T is included, and the cost if it is (about
   $1.14 for three reruns).
3. Option 2 is restated as the source had it, or the floor option is added
   as its own row.
4. The table states the recommendation's time cost before 2026-10-18, says
   option 4 is the plan version 4 already chose ("rather than a repair"),
   and adds that option 4 drops arm M.
5. Page 12 says it changes a condition John said to go with, and gives the
   decoy test's stated limit.
6. Fix 4 on page 2 is stated as a change to the cost backstop, with the
   "confirmed deletion only" condition.
7. The weight-decay sentence uses the size argument (finding 2).
