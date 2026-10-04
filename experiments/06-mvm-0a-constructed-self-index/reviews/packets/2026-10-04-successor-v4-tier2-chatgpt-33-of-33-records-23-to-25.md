*This is file 33 of 33, the last one, of a review packet pasted into a single conversation. It contains record 23 part 3 of 3 (the list of what has gone wrong in this program before, which the inside reviewer ran against version 4); record 24 (the opening description of the closed design's task grammar, which version 4 says its grammar extends (inside finding RT-239)); record 25 (the opening description of the rehearsal's task grammar (inside finding RT-239)). You now have the whole packet. Answer the brief (record 1, in file 1) now, in its four parts, with the kill case at the end, labelling your findings A1, A2, A3 and so on. If any file was missing or cut short, name it at the top of your answer.*

===== RECORD 23 of 25, part 3 of 3 - the list of what has gone wrong in this program before, which the inside reviewer ran against version 4 - `docs/known-failure-modes.md` (complete file, 55,318 characters) =====
**The fix.** Ruled by John 2026-09-25. The watcher start now runs only
`nohup` in the background, with all its output redirected (`cd … || exit 1;
nohup … &`), so nothing holds the connection; and the `ssh` that sends it is
cut off at 60 seconds whatever happens, the same cap the training start
has. The laptop's machine deadline (`src/machine_deadline.sh`) bounds the
money if some other remote step hangs.

**The reproduction, with nothing rented.** The findings reproduced the hang
on the laptop by putting `| cat` where `ssh` would be: like `ssh`, `cat`
waits until everything on the far side has closed its output. Re-run on
2026-09-25 (Pacific) by the session that wrote this entry, first the
findings' own two commands, then the launcher's real old and new watcher
forms with the watcher replaced by `sleep 8`:

```
== the findings' reproduction, rerun 2026-09-26T00:49:55Z (2026-09-25 Pacific)
form as launched (cd && nohup ... &): returned after 8s
control (cd ; nohup ... &): returned after 0s
== the launcher's watcher-start form, old (line 467 at 4d98cfc) and new, with the watcher replaced by sleep 8
OLD  cd … && nohup … &        : returned after 8s
NEW  cd … || exit 1; nohup … & : returned after 0s
(a background sleep 8 is still running after the new form returned: it was started, not skipped)
```

The script that printed this is filed as
`experiments/rehearsal-successor-measure/out/launcher-fix-2026-09-25/hang-reproduction.sh`,
beside its output.

**The test.** One command. It rents nothing and contacts no vendor. For each
command a launcher sends over `ssh` that starts something in the background
(it contains `nohup`), it rewrites the command to run on this laptop, with
the backgrounded program replaced by a stand-in that leaves a marker file and
holds for 8 seconds, runs it through `bash -c '…' | cat`, and times it. A
start that returns in under 2 seconds passes. One that holds the connection
passes only if the launcher cuts that `ssh` off with a time cap. One that
holds and is not capped fails. A start whose stand-in never ran fails too,
because a command that returns at once by doing nothing has not been shown
to return at once. Then a negative control, the pre-fix form, must be
rejected.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
```

```
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
```

**It fails on the design that produced the finding.** Pointed at the
launcher as it was at `4d98cfc`, the commit the slice ran:

```
$ git show 4d98cfc:experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh > "$TMPDIR/launcher-4d98cfc.sh"
$ LAUNCHER="$TMPDIR/launcher-4d98cfc.sh" experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
```

```
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launcher-4d98cfc.sh
  [FAIL] launcher-4d98cfc.sh line 467: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] launcher-4d98cfc.sh line 547: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 552)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.2s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

1 problem(s). Nothing was rented and nothing was spent.
```

Both outputs were produced on 2026-09-25 (Pacific) by the session that wrote
this entry, and no other session has re-run them. **The timings are wall
clock**, so a re-run will differ from the text above by a tenth of a second
here and there; compare the verdicts and the whole seconds, not the bytes.
The line numbers are those of the file at the commit this entry landed in,
and move when the launcher is edited.

**What the output has to show**, for any design this is pointed at: every
background start a launcher sends over `ssh` either returns at once or is
cut off by a time cap in the launcher; no start is reported as never having
run; and the negative control is rejected. **The control is what makes the
rest worth reading.** If it is ever accepted, the check has stopped
measuring what it claims to.

**What this test does not cover, stated so it is not read as covering it
(ARGUED).** It catches one way a remote step can differ from its stand-in:
a background job holding the connection. The species is wider. A vendor
tool on the machine that takes different arguments from the laptop's (the
2026-09-17 finding recorded at the verb-first check in the launcher), a
credential the machine does not carry (2026-09-16), a path that exists only
on the laptop — none of these is exercised here, and none can be by any
check that does not reach the real far end or a faithful copy of it. The
general discipline, for which no single command exists: **before a remote
step is counted as tested, say what stood in for the far end, and what that
stand-in cannot do that the far end can.** A test run only against a
stand-in is evidence about the stand-in.

---

## Adding to this list

A fatal finding that is a new species — not a new instance of one of the four
above — is added here by the pass that found it, with its test written the same
way: a command, and what the output has to show. Write the test so that a session
holding a different design can run it without asking anyone what it means.

An entry here is binding text under the protocol's pairing rule, so a session
other than the one that wrote it checks the entry: that the test runs, and that
it fails on the design that produced the finding. A test that has never been seen
to fail has not been shown to detect anything.

The list is added to and not shortened. A failure that has stopped recurring is a
failure whose test is passing, which is the reason to keep running it rather than
a reason to drop it.
===== END OF RECORD 23, part 3 =====

===== RECORD 24 of 25 - the opening description of the closed design's task grammar, which version 4 says its grammar extends (inside finding RT-239) - `experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (lines 1 to 118 of the file's 650, unedited) =====
"""The Amendment A3 Candidate A curriculum — "act as yourself".

A3 §2.2: the objective must make the correct output at a supervised
position depend on which agent the model is, must ground ownership only
in the act (the acting channel), and must supervise an action rather than
a report. This module builds that grammar. `curriculum.py` is left
byte-identical: every record in `lesion-results/` and `null-calibration/`
reproduces against it, and the five existing checkpoints were trained on
it.

The episode
-----------
Twelve turns, four agents, two *contested* items:

- **Eight assignment turns.** Each agent assigns each contested item
  exactly once, in one random permutation of the eight (agent, item)
  pairs. Within an item the four values are **distinct**, so an item's
  four assignments differ only in who made them.
- **Four revision turns**, last, in random order: **every agent revises
  exactly once**, two agents on each contested item, with the pairing
  drawn by a uniform shuffle.
- **The revision rule is deterministic and shared**: the revised value is
  the successor of *that agent's own earlier value on that item*, over
  the eight slots, modulo eight. Every agent obeys it; the generator
  applies it to the other agents and the enactment harness applies it to
  the model.

Every agent therefore has exactly three turns, two assignments and one
revision, and sits in the assignment block and the revision block equally
often. Nothing about how much an agent speaks, where, or whether it
revises can predict which agent the model is.

Why exactly one own revision per episode
---------------------------------------
Gate 0 measured the cost of the alternative. Under the registered
grammar the revision-conditioned battery harvests one scoring cell from
about one episode in twenty, so at 400 episodes it is a 19-item cell
whose null band is two items flipping
(`gate0-null-calibration-findings.md`, reading 2). A3 decision 12 sets
verdict cells at n=400. One own revision per episode is what makes 400
episodes yield 400 `T_act` cells instead of about 20.

Why *every* agent revises, which the first draft of this module got wrong
------------------------------------------------------------------------
The first version gave the model one revision and one other agent one
revision, and left the remaining two agents with assignments only. Its
own self-test killed it: the model's slot then always had three turns
while two other agents had two, so **agent turn count predicted
ownership perfectly** (3 turns for the model every time, against 0.43 of
other-agent turns), and revision status predicted it at 0.33 against
0.14. That is the same class of defect the registered grammar hit when a
red-team patch made the revision always final and always the model's
(`curriculum.py`, `_episode_skeleton`), and it is what gate (i) exists to
catch. Giving every agent exactly one revision removes both cues by
construction rather than by measurement.

What a solver without a self-index can do
-----------------------------------------
At its own revision turn the model sees four distinct earlier values for
that item and must emit the successor of its own. Position is randomised,
markers are a per-episode draw, and every agent's values come from the
same distribution, so nothing in the text distinguishes the four.

Two agents revise each item, so if the *other* agent revising the model's
item goes first, a solver can invert the rule on that revision and strike
one candidate. The model revises first half the time. **The lookup
ceiling is therefore 0.25 on half the cells and 0.333 on the other half,
0.292 overall**, against a chance floor of 0.125. That is above the 0.25
A3 §2.2 pre-states, and the discrepancy is real rather than cosmetic: it
is the price of making every agent revise, which is what removes the
ownership cue above. Red-team pass 3 should either adopt 0.292 as the
pre-stated ceiling or buy 0.25 back by adding a third contested item that
nobody revises, at about a third more compute per run.

**An honest limit on the design's central claim.** A3 §2.2 says the only
route from the ceiling to 1.0 is to have bound the act to the item when
acting and carried that binding forward. There is a second route. The
revision turn renders as "<marker> assign <item> to <value>", so at the
moment the model acts, its own marker is in the context three tokens
back. A model could learn "the marker at a position where I am acting is
mine", then retrieve that marker's earlier value by ordinary
marker-keyed lookup — reading a name badge at act time rather than
carrying a binding. Both routes need the acting channel and both collapse
under the L0 lesion, so L0 does not separate them. A3 already registers
the discriminator: the mid-episode re-indexing probe of the H_tag bin.
The claim in §2.2 should be narrowed to say so.

Batteries
---------
- **T_act** (primary, an action not a report): the value emitted at the
  model's own revision position. Chance 0.125, lookup ceiling 0.25.
  Carried on the episode as `act_target`, scored at that position.
- **T_other**: a forced-choice counterfactual naming another agent —
  "where did <marker> assign <item> to next ?" — on the contested item
  that agent did *not* revise, so the answer appears in no turn and must
  be computed from its earlier value. Same rule, same binding demand, no
  self-reference. Chance 0.125. Two of the item's four values are struck
  by the two revisions a solver can invert, so its lookup ceiling is
  0.5 — higher than T_act's, which red-team pass 3 should weigh, since
  the H_generic-binding bin turns on the difference between the two
  batteries' drops.

  [2026-09-17, REGISTERED DEFECT. The comment above is left as written.
  Red-team pass 3 ran and did NOT weigh it. The registered ceiling is
  0.3227, not the 0.5 stated here, and NEITHER figure was ever checked
  against an adversary: shortcut_sweep.py attacks only T_act. Worse, the
  solver in measured_ceilings below never reads the marker the T_other
  question names, so 0.3227 is a name-BLIND score and this battery's real
  ceiling is near 1.0, unmeasured. No result changes; the control fails
  its floor under every reading. See ceiling-defect-2026-09-17.md.]
- **T_state**, **T_syntax**: unchanged in kind from the registered
  grammar (RT-05 competitor, and the floor check).

Corrigibility: this module generates data. It trains nothing, launches
nothing and costs nothing [C1/C2].

    ../../../.venv/bin/python curriculum_a3.py --self-test
"""
===== END OF RECORD 24 =====

===== RECORD 25 of 25 - the opening description of the rehearsal's task grammar (inside finding RT-239) - `experiments/rehearsal-successor-measure/src/grammar.py` (lines 1 to 70 of the file's 485, unedited) =====
"""The matched-role revision grammar, shrunk to rehearsal scale.

UNREGISTERED. This is a stand-in built for the measurement rehearsal of the
successor experiment proposal (`docs/successor-experiment-proposal-2026-09-21.md`,
section 4). It is not the registered generator, it trains nothing on its own,
it costs nothing, and no result about the scientific question may be read off
anything it produces.

What one episode is
-------------------
Four agents, two items, eight value slots, and a closed vocabulary.

- **Eight assignment turns**, one per (agent, item) pair, in a uniformly
  random order, rendered `<marker> assign <item> <value>`. Within an item the
  four values are distinct, so the four assignments differ only in who made
  them.
- **Two action turns**, last, in a random order between them, rendered
  `<act> revise <who> <item> <ans> <mask>`:
    * **own-directed** — `<who>` is the special word meaning *your own*, and
      the answer is the successor of the model's own earlier value on that
      item;
    * **named-other-directed** — `<who>` is another agent's marker word, and
      the answer is the successor of that agent's earlier value on that item.
  Both are actions at the model's own turn, supervised the same way and
  scored the same way. That is the whole point of the redesign the proposal
  makes: in the closed Amendment A3 design the ownership condition was an
  action and its comparison was a question at the end of the episode, so the
  two were never at the same kind of position.

Two departures from the registered A3 grammar, both deliberate
--------------------------------------------------------------
1. **The action turn carries no marker word.** In `curriculum_a3.py` the
   model's own turn renders its own marker three tokens before it acts, and
   that module's own header records the consequence as an honest limit: a
   model can read a name badge at the moment it acts instead of having
   carried a binding. Here the only route to the ownership answer is the
   acting channel.
2. **The answer token is never shown.** The slot where the answer goes is a
   dedicated `<mask>` word in the input, and the model's prediction is read
   at that position. Nothing downstream ever sees the answer.

Together these make a matched pair of episodes — the same content with a
different agent being the model — come out **token-for-token identical**,
differing only in which positions the acting channel fires on. That is what
lets a transplant between the two be a clean comparison: nothing but
ownership can differ anywhere in the state.

What is matched, and checked rather than asserted (proposal section 4.2)
------------------------------------------------------------------------
1. candidate count: four earlier values in context in both conditions;
2. distance: the gap between source assignment and action, same distribution;
3. supervision: one supervised position of each kind, one scored token each;
4. transformation: the same successor rule in both conditions.

Carried-forward rules from the red-team ledger of experiment 06
---------------------------------------------------------------
- the **even-split rule** (ledger item `RT-58`, the batch-split bias check):
  any batch fraction that splits rows must not cut the generator's matched
  pairs;
- the **one-scored-token check** (ledger item `RT-59`, the check that exactly
  one token per supervised position is scored and that the check survives the
  shift the loss function applies). Here the answer is scored **at** the
  `<mask>` position rather than at the position before it, so the shift does
  not arise; the self-test asserts that too, rather than leaving it implied.

Corrigibility: this module generates data. It trains nothing, launches
nothing, rents nothing and costs nothing [C1/C2].

    ../../../.venv/bin/python grammar.py --self-test
"""
===== END OF RECORD 25 =====

