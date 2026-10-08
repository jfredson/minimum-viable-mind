*This is file 31 of 33 of one review packet, pasted into a single conversation. It contains record 22 part 2 of 2 (the other-agent control against twenty random pieces (NOT A RESULT: a code test)); record 23 part 1 of 3 (the list of what has gone wrong in this program before, which the inside reviewer ran against version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 22 of 25, part 2 of 2 - the other-agent control against twenty random pieces (NOT A RESULT: a code test) - `docs/2026-10-03-control-2-twenty-draws.md` (complete file, 7,572 characters) =====
**Still true, and unchanged by this:** the control has never been exercised
on a model whose read of the named agent clears its floor. No toy model has
one.

## 6. Which sentences of version 4 this bears on

Version 4 is `docs/successor-experiment-proposal-2026-10-03-v4.md`. This file
does not edit it; another session is working on it.

- **Section 7.3, item 2**, the sentence "What is reported: how often the
  own-directed action moves under the named agent's piece, beside how often
  it moves under twenty random pieces of the same size at the same sites,
  reported as control 3 reports its twenty (median, 95th percentile, and the
  counts below, equal and above)". The code now does this:
  `control2_twenty_draws.control2`.
- **The same item's bullet "The part of its code after the floor has run
  once, and that run is NOT A RESULT"**, which describes the run of the
  single-draw code. The code that would be registered has now also run once,
  NOT A RESULT, and the text should name this run and this file rather than
  only the earlier one. Version 4's own section 19, item 5 foresaw this ("the
  code path that ran once on 2026-10-03 is not quite the one registered").

## 7. Questions for John, each with a suggestion

Not asked in chat; for the session that routes rulings.

1. **Which file is the registered control 2.** The ruled change lives in a
   new file, because the brief said not to edit the committed scripts;
   `rerun_controls.control2` still has the one random piece and the pass
   line. *Suggestion:* the registration names
   `control2_twenty_draws.control2` as control 2's code and says that
   `rerun_controls.control2` is the earlier version, kept as the record of
   what the re-run did.
2. **Whether the 95th percentile of twenty is the right summary.** With
   twenty draws it is an interpolation between the two largest. That is the
   same as control 3 does, which is what was ruled. *Suggestion:* leave it as
   ruled and print the twenty as well, as this code does, so a reader sees
   the spread.

## 8. Files

`experiments/rehearsal-successor-measure/out-control-2-twenty-draws/`:
`code_test_NOT_A_RESULT.json`, `table.md`, `stdout.txt`. Code:
`src/control2_twenty_draws.py`, unchanged since `174081e`.
===== END OF RECORD 22, part 2 =====

===== RECORD 23 of 25, part 1 of 3 - the list of what has gone wrong in this program before, which the inside reviewer ran against version 4 - `docs/known-failure-modes.md` (complete file, 55,318 characters) =====
# Known failure modes, and the test that catches each one

*Written 2026-09-21 (Pacific) as the companion to the outside-review protocol
(`docs/outside-review-protocol.md`). That protocol was amended the same day to
require every registration text to be run against this list rather than to cite
it. This file is the list.*

*Approved by John as one of six recommendations put to him with its cost, in his
words "Ok, can we implement all of these?". The session proposed and he
approved; the wording here is the session's and is his to overturn.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## What this list is for

Five things have gone wrong in this programme badly enough to cost weeks of work,
to put an unsatisfiable sentence into text that had already been registered, or to
create a rented machine with a command documented as creating nothing.
Each is easy to recognise once it has been named — and, as it turns out, just as
easy to reproduce while naming it. A proposal reviewed on 2026-09-21 quoted the
first failure below by name, in the section discussing the weaknesses of its own
measure, and the measure two sections earlier reproduced it.

So this is not a reading list. Every entry ends with a test: a command a session
can run against a new design, and what the output has to show. The protocol's
failure-mode pass requires that test to be run and its output filed, for every
failure here, on every registration text. **"Considered and does not apply" is
not a disposition.** The count that is not zero, the cell that has trials in it,
the record that exists and contains what the sentence says it contains — those
are dispositions.

Every output printed below was produced by running the command printed above it,
in this repository, on 2026-09-21.

**What this list has been shown to be, and what it has not.** As a description of
what has gone wrong here, it is accurate.

**Which blocks below have been run, and which have not.** Fifteen blocks are
printed below. Twelve carry a command and the output that running it produced.
A thirteenth, the first block under failure 5, is different in kind and is
flagged again where it appears: it is the **recorded** output of the command
that created a rented machine on 2026-09-21, and it must never be re-run,
because re-running it is the failure. The block beneath it is failure 5's
actual test, which was run, and which creates nothing.
Ten of those eleven have been re-run by a session other than the one that wrote
them and compared against the printed text with `cmp`, which names the first byte
at which two files differ; nothing differed. The eight the list carried before
the repair described below had already been checked the same way once, with
`diff`. The eleventh is newer than that check: it is the block under failure 2
that prints the two rows illustrating that failure's middle limb, and the session
that added it ran it, but no other session has yet re-run it. The remaining two
blocks carry placeholders in angle brackets and no output. One of them is failure
4's first part, written as a template because it is pointed at whatever document
is under review; the word lists inside it are exercised on six worked claims in
the block below it, and that block was run and its output printed. **The other is
failure 2's second part, and it has never been run at all.** Running it means
running a whole probe pipeline twice against model checkpoints, which costs
compute that nobody has authorised. Its middle limb — the second run clears the
bar and the first does not — is now illustrated, by a printed block under failure
2 showing the two rows in the position sweep's findings file where exactly that
pattern appears. Illustrated is not executed: those rows come from the history
this entry was written from, so the limb still has not been seen to fire on
anything it had not already been fitted to.

As a set of tests a new design can be run against, this list is not yet
established. The first check found that three of the four tests fell short of the
standard this document sets on its own last page — that a test never seen to fail
has not been shown to detect anything. One passed on the very design that
produced the failure it describes, one did not execute at all, and one looked
only for words that the newest form of its own failure does not use. Those three
were repaired on 2026-09-21 by a third session. Failure 3's empty cell and
failure 4's widened word list are each printed below with the command and the
output showing the test failing on the design it was written from. Failure 2 is
printed that way for its first part only, and that part is a proxy rather than a
detector, for the reasons set out under it.

**Where that leaves the list.** The repairs have been checked once, by the
session that wrote
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-protocol-repair-claude-worktree.md`
at commit `fbfecb5`, the commit titled "Check the repair: the ten outputs hold,
two tests still owe a sentence". That check found the two gaps the paragraphs
above and the paragraph under failure 2's first part now fill. Those two
corrections were written by a fourth session and have not themselves been checked
by anyone. Under the pairing rule in the protocol beside this file, they are owed
a check by a session that did not make them. Until that check exists, treat this
list as a reliable account of the past and an unproven instrument for the future:
run it on a registration text and file what it returns, but do not read a clean
pass from it as evidence that a design is clean.

---

## 1. A comparison whose denominator was zero

**What it was.** Amendment A3 registered a corrected measure that subtracts, from
each score, the best a solver could do while ignoring ownership — the
ownership-blind ceiling — and then divides by the distance left between that
ceiling and a perfect score. For the control battery (the comparison battery of
questions, built so that answering it does not require knowing whose value is
whose), that ceiling turned out to be 1.0. The distance left was zero. The
measure had nothing to measure, and had had nothing to measure from the day it
was registered.

**How it showed up.** The third adversarial pass said it four days before the
registration commit, in its twenty-first finding — the unequal-ceilings finding
(`RT-21` in the red-team ledger), marked fatal, whose metric fix was marked
adopted. The fix depended on a ceiling nobody had measured. The measurement, when
it was finally made, is
`experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md`,
whose title is the finding: "The control battery's ceiling is 1.0, and the clause
was never computable." A battery built so that its questions do not require
ownership has an ownership-blind ceiling of 1.0 by construction; dividing by the
distance to 1.0 divides by zero.

**Its newest form, found 2026-09-21.** The successor experiment proposal
registers its reading as the difference between two accuracies divided by the
larger of them, with no floor subtracted from either. A floor that sits under
both terms does not cancel in a ratio, so the largest value the reading can
return is different for every arm — every version of the system being compared —
because the accuracy it divides by is different for every arm, and the design
expects it to be. Two systems separable to exactly the same degree then read
differently for no reason but their overall accuracy. This is the ceiling failure
with the zero replaced by a moving number, which is harder to see and no more
measurable. It is filed as the first finding of the Gate C pass on that proposal
(`RT-172`, the per-arm-ceiling finding), in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`
at commit `3bbfece`, the commit titled "Gate C tier 1 review of the successor
experiment proposal: RT-172 to RT-188". The commit is named and not only the
branch it was written on, because a session branch is deleted once it is merged
and a citation anchored to one loses its signpost without anyone editing the
sentence. The design being criticised is the successor experiment proposal
(`docs/successor-experiment-proposal-2026-09-21.md`) at commit `d8ceba9`, the
commit titled "Successor proposal: the rehearsal buys a rented slice, and the
second release is bound to what it measures", which was written on a different
branch again. Both commits have since reached the main line in the working
checkout, though neither had been pushed to the shared copy of the main line when
this was written.

**The test.** Two parts, both cheap.

*Part one: print the denominator at the ceiling, for every condition the reading
will be applied to, using ceilings measured in the rehearsal rather than
assumed.*

```
$ python3 -c "
ceilings = {'primary battery': 0.2921, 'control battery': 1.0000}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery: denominator 1 - ceiling = 0.7079
control battery: denominator 1 - ceiling = 0.0000
```

**Part one is a display and not a detector; part two below is what does the
detecting.** The arithmetic only shows what it is handed. Hand it the ceilings as
they were actually registered on 2026-09-15 — 0.2921 for the primary battery and
0.3227 for the control (`amendment-a3.md` line 415) — and it prints two healthy
denominators, with nothing to see:

```
$ python3 -c "
ceilings = {'primary battery': 0.2921, 'control battery': 0.3227}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery: denominator 1 - ceiling = 0.7079
control battery: denominator 1 - ceiling = 0.6773
```

That is the failure passing its own test. The zero only appears once somebody has
measured the ceiling, and measuring it is the rehearsal's job, not this test's. So
part one's failure criterion is about where its numbers came from rather than
about the arithmetic: **it fails if any ceiling typed into it cannot be traced to
a committed measurement record**, named by file. Type in an assumed ceiling and
this command reproduces the original failure while producing a filed output that
looks like a disposition — which is what 0.3227 was.

*Part two: print the largest value the reading can return, per condition, when
the thing it is meant to detect is entirely absent.*

```
$ python3 -c "
def reading(whole, ownership_only): return (whole - ownership_only) / whole
floor = 0.125
for whole in (0.90, 0.60, 0.35):
    print(f'best score {whole}: top of scale = {reading(whole, floor):.3f}')
"
best score 0.9: top of scale = 0.861
best score 0.6: top of scale = 0.792
best score 0.35: top of scale = 0.643
```

**It fails if** any denominator is zero, or small enough that ordinary noise in
the measured ceiling moves the reading a lot; or if the top of the scale differs
between the conditions a single pre-stated threshold is compared across. A
threshold in units whose top of scale moves between where it was set and where it
is applied is not a threshold. Both halves need numbers from the rehearsal: a
ceiling that was assumed rather than measured is what produced this failure in
the first place.

---

## 2. A probe target that cannot be recovered in principle

**What it was.** The localization line spent weeks predicting `own_slot` — the
episode generator's index for whichever agent the model is playing — from the
model's internal states. That quantity has no consistent surface realisation: the
generator knows it, and nothing the model was shown or trained on requires the
model to compute it. It cannot be recovered from these states at any position,
with any instrument. Every null the line produced was therefore a null about an
unanswerable question, which is not evidence of the absence of anything.

**How it showed up.** In the position sweep of 2026-09-19
(`experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md`),
whose first arm came back "SWEEP INVALID on all three checkpoints" because its
positive control failed: zero of 165 tests cleared the bar. The finding names
what that cost — the blind-arm probes of 2026-09-16, the denoise-before-probing
diagnostic and the sweep itself "were all asking a question with no answer". The
contrast is the powered target test of the same day
(`powered-target-test-findings.md`): with the target re-posed as a quantity that
demonstrably reaches the states — the marker word, read at the position where it
*is* the input token — the same kind of read returns 0.5877 against a
no-information value of 0.04, about 159 standard deviations of its own null. The
instrument was never the problem. No review pass had been asked whether the named
quantity was recoverable at all.

**The test.** Two parts. **Part two is the one that catches this failure; part
one is a prompt to look.** Part one asks for a written sentence and checks that
it exists, which forces the question to be faced but settles nothing on its own.
Part two runs the probe twice and compares the two results, and its middle limb —
the second run clears the bar and the first does not — is what actually
distinguishes an unrecoverable target from a working one. Part two has never been
run; see the paragraph under it.

*Part one, before anything is registered:* the method document states, in one
sentence and in a fixed form of words, the route by which the quantity reaches
the model's states — which token carries it, or which part of the loss forces the
model to compute it. "The episode generator knows it" is not a route. Writing the
sentence is paper and pencil; **checking that it is there is a command**, so that
this part produces a disposition with its work shown like every other:

```
$ python3 -c "
import re
pattern = r'route to the states|carried by the token|forced by the loss|is the input token'
base = 'experiments/06-mvm-0a-constructed-self-index/'
for f in ('position-sweep-method.md', 'powered-target-test-method.md'):
    lines = [l.strip() for l in open(base + f) if re.search(pattern, l, re.I)]
    print(f'{f}: {len(lines)} route sentence(s)')
    for l in lines:
        print('   ' + l)
"
position-sweep-method.md: 0 route sentence(s)
powered-target-test-method.md: 1 route sentence(s)
   the marker position**, where it is the input token. It must clear three
```

That is this failure caught, on the design that produced it, with a command and
an output. The method committed before the sweep that spent weeks on `own_slot`
contains no sentence naming a route, because none could be written. The method
for the target that turned out to be recoverable contains one, and it names the
token. Run this on a new design's method document with that design's own wording
in the pattern; a count of zero is the finding.

**What this search cannot see, plainly.** It counts sentences that match a fixed
set of words, so it cannot see a route named in any other words. Run exactly as
printed above across all nine method documents in this experiment, seven come
back at zero, and one of the seven is the method for the powered eleven-position
sweep
(`experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-method.md`),
which does what this part asks for and does it at length: it names in advance the
token that carries the target at one position, and says that nothing carries it
at another. It scores zero because it writes "as an input token" where the
pattern says "is the input token". That run is printed in the check of this
repair
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-protocol-repair-claude-worktree.md`
at commit `fbfecb5`, the commit titled "Check the repair: the ten outputs hold,
two tests still owe a sentence"). The other direction is no better: a count above
zero says only that some sentence matched the words typed into the pattern, and
the instruction to run it with the new design's own wording means a session that
writes the pattern out of the document it has just read will match by
construction. What this command records is whether the checking session found a
sentence it was willing to call a route — worth recording, because it forces one
specific sentence to exist and be quoted into the filed output where it can be
argued with by name, but not a measurement of whether a route exists.

**So part one is a prompt to look and not a verdict**, and the sentence above
calling a count of zero the finding should be read that way: a zero is a reason
to go and read the method document and settle in writing whether a route is named
there, and a sentence that matched is not on its own a pass.

*Part two, run in the rehearsal:* run the whole probe pipeline twice — once on
the pre-stated target, once on a quantity the design guarantees is present, read
at a position where it must be present — with the same bar and the same null.

```
$ python3 src/<probe_script>.py --target <the pre-stated quantity> --report margins
$ python3 src/<probe_script>.py --target <a quantity the input guarantees> --report margins
```

**It fails if** any of three things is true, and they are read together:

- **Part one returned no route sentence.** Fatal on its own, whatever the two
  runs do. A target whose route nobody can name is the target that has cost this
  programme weeks.
- **The second run clears the bar and the first does not.** *This is the failure
  this entry exists for.* A working instrument that returns nothing on the
  pre-stated target is evidence that the target is not there to be recovered —
  not evidence about the system being probed. The pre-stated target changes
  before registration, and the null already collected is withdrawn rather than
  reported.
- **The second run does not clear the bar.** Then the pipeline is broken and
  nothing has been measured at all; the first run says nothing either way,
  whether it cleared or not.

File both runs. A pre-stated probe target whose positive control was never run is
a fatal finding on its own, on the same reasoning as a pre-stated quantity the
rehearsal never exercised.

**Why the criterion is written this way.** Until 2026-09-21 this entry said only
"it fails if the second run does not clear the bar", and on the history the entry
is written from that test passes. The second run is the one on the quantity the
input guarantees, and in the position sweep of 2026-09-19 it cleared by an
enormous margin — 0.5877 against a no-information value of 0.04, about 159
standard deviations — which is the same evidence the entry itself cites for "the
instrument was never the problem". A criterion that looks only at the pipeline
detects a broken pipeline. It cannot detect an unrecoverable target, which is
what this entry is about, and the pattern that reveals one — the first run empty
while the second clears — was not named as a failure anywhere in the entry. It is
now the second bullet above.

**What that middle limb looks like in the record, with the test itself still
unrun.** The two runs part two asks for were never made. But a diagnostic filed
with the position sweep of 2026-09-19 read both quantities at the same position,
through the same instrument, each against its own fifty-draw permutation null,
and the sweep's bar throughout is three standard deviations of that null. Those
two rows are in its findings file, and this is them:

```
$ grep -nE "own_slot.*what the stack asks for|marker_token.*the input token itself" experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md
120:| `own_slot` — what the stack asks for | 0.293 (+1.60) | 0.273 (+0.88) | 0.243 (−0.24) | 0.283 (+1.33) | 0.275 (+0.91) |
122:| `marker_token` — the input token itself | **0.550 (+51.6)** | 0.513 (+43.1) | 0.510 (+41.3) | 0.498 (+41.9) | 0.490 (+40.8) |
```

First number column is the third layer, and each cell is the accuracy with its
margin in standard deviations of that cell's own null. The pre-stated quantity
tops out at 0.293, about 1.60 standard deviations, and clears three nowhere. The
quantity the input guarantees reaches 0.550, about 51.6. Second run clears, first
does not: that is the middle limb, in numbers that already exist.

**This illustrates the limb; it does not execute the test.** These are two rows
lifted from a record, not the two runs part two asks for. They come from the very
history this entry was written from, so the limb has still never been seen to
fire on a design nobody had already diagnosed. And the findings file labels the
diagnostic these rows sit in as **not pre-stated** — it was written after the
sweep had already failed, which the file says makes it worth less than a
measurement designed in advance. Part two stays unrun, because running it means
running a whole probe pipeline twice against model checkpoints and nobody has
authorised that compute. The paragraph near the top of this file that says so
still stands.

---

## 3. A cell that is empty by construction

**What it was.** Found 2026-09-21, in the successor experiment proposal. One of
the seven pre-stated controls — the one that separates "the transplant moved who
is acting" from "the transplant smuggled a value across", and so the one the
whole reading leans on — splits trials into pairs where the donor's identity
dictates the *same* answer as the recipient's and pairs where it dictates a
*different* one. Both cells are pre-stated and both are to be reported. The
grammar the design extends draws four *distinct* values for each contested item,
one per agent, without replacement, and asserts that the property survives
rendering. Two agents therefore never dictate the same answer, the first cell can
never hold a trial, and three other passages of the same proposal require the
distinctness that empties it. Filed as the second finding of the Gate C pass on
that proposal (`RT-173`, the empty-cell finding), in the same review file and at
the same commit named under failure 1 above (`3bbfece`), against the same
proposal commit (`d8ceba9`).

**The same defect one step further.** That control carries a pre-stated check: an
untouched condition "should be near the one-in-eight guessing rate; if it is not,
the pairing is broken and nothing is read." With distinct values, a model that has
learned the task lands on the donor's answer only by erring onto exactly that
slot. The rule as written passes a model that has learned nothing and fails one
that has learned the task. It is pointed the wrong way round, and it sits inside
the list of things the design proposes to freeze.

**The test.** Two parts, and a third for any threshold attached to a cell.

===== END OF RECORD 23, part 1 =====

