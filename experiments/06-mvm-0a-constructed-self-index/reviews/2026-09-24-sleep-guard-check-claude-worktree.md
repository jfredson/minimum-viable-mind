# Check: the launch precondition that refuses to start when this Mac could fall asleep

*Written 2026-09-24 (Pacific) by a checking session that did not write the thing
being checked, under the pairing rule in `docs/outside-review-protocol.md`.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

**What was checked.** Branch `worktree-agent-a0aa22f6fe502b9ac`, the single commit
`aa7b739` titled "Refuse to launch when this Mac could fall asleep". Two files: the
new precondition inside the derived launcher
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`, and the
new test beside it, `src/sleep_guard_selftest.sh`.

**Nothing was rented, no vendor was contacted, nothing was spent, and this Mac's
real power settings were never changed.** Every reading of the real settings was a
read. They were the same at the end of this check as at the start: the never-sleep
override off, the idle sleep timer fifteen minutes on both power sources, drawing
from wall power. Both files were restored to the committed version after the
deliberate-breakage run below, and the restoration is proved by a hash and by an
empty comparison against the commit.

**Verdict: yes, merge.** One item below is marked must-fix, and it is a comment,
not behaviour.

---

## 1. Exercising the guard with cases its author did not write

The guard reads this Mac's power settings through a command named in a variable, so
a test can point it at a stand-in. That is the same trick the shutdown-handshake
test plays on the rental tool, and it is what made this check possible without
touching anything real. This session wrote its own stand-ins rather than re-running
the author's, and its own launch harness rather than the author's.

Every case below refused or stopped long before the first command that could create
a rented machine, and every one was confirmed to have done so.

| Case this session devised | What happened |
|---|---|
| **A.** The never-sleep setting is present but its value is a word, not a number (`SleepDisabled enabled`) | Refused. But it refused saying "the never-sleep override is OFF", which is not what it read. See the follow-up list. |
| **B.** The setting's line is present with no value after it | Refused, correctly, saying it could not read the setting |
| **C.** The value is `1` followed by a parenthetical note, the way the real tool annotates some of its other lines | Passed the guard. Correct: the value really is on. |
| **D.** The power-reading command does not exist at all | Refused, correctly, saying it could not read the setting |
| **E.** The command prints nothing and reports success | Refused, correctly |
| **F.** The command prints a good reading but reports failure | Passed the guard. The guard ignores the command's success-or-failure report and trusts the printed reading. |
| **G.** The command prints a good reading to the error channel only | Refused, correctly |
| **H.** The never-sleep override is on and the Mac says it is drawing from wall power, but the battery is at 2% and discharging — the signature of a charger that has stopped delivering | **Passed the guard.** The same command that answers the power-source question also prints the charge level and the word "discharging", and the guard throws both away. |
| **I.** Drawing from an uninterruptible power supply, a real answer the tool can give | Refused. Conservative, and defensible. |
| **J.** The power-source line mentions wall power while the Mac is on battery | Refused, correctly, but the refusal message came out garbled — the pattern that pulls the power source out of the line grabs too much when the line holds a second quoted phrase |
| **K.** The idle-timer reading fails while both gating readings succeed | Passed the guard and reported the timers as "unread". Correct by design: the timers never decide anything. |
| **L.** The idle timers are set to never, but the never-sleep override is off | Refused. Confirms the guard does not treat a generous idle timer as a substitute for the override. |
| **M.** The override is off *and* the Mac is on battery | Refused on the override only. The fix it prints does not mention plugging in, so an operator in both states gets sent round twice. |
| **N.** `ALLOW_LAPTOP_SLEEP=0` | **The guard switched off.** It printed "OVERRIDDEN by ALLOW_LAPTOP_SLEEP=0 — carrying on anyway", which contradicts itself. |
| **O.** `ALLOW_LAPTOP_SLEEP=false` | The guard switched off, same as above |
| **P.** A command-line argument passed while the Mac is sleepy | Refused with status 2 by the argument guard, before the sleep check ran at all. Correct order. |
| **Q.** The override spelled as an argument instead of an environment setting | Refused with status 2 by the argument guard. The override cannot be smuggled past it. |
| **R.** The power-reading command hangs | **The launcher hung with it — there is no time limit on the read.** Still running after 25 seconds, having printed only its first line. It creates nothing while hung, so this fails in the safe direction. |

Cases **N**, **O**, **H** and **R** are the ones that found something. They are
carried into the lists at the end.

---

## 2. The deliberate-breakage run: does the test actually catch a launcher that only warns?

**Yes. Confirmed independently, and the author's reported numbers reproduce exactly.**

This session broke the launcher itself rather than replaying the author's account of
having broken it. The refusal block was replaced with the shape every other launcher
in this repository has — print the warning, print the fix, carry on and launch — and
the test was run against it unchanged. It reported:

```
checks passed: 29   failed: 9
```

with the nine failures falling in exactly the places the author recorded: the two
readings that have actually cost money, the two unreadable-reading cases, and, in
the first of them, the missing mention of the override. The safe-machine control and
the two escape-hatch cases passed throughout, which is right — a launcher that only
warns still lets a safe Mac through and still previews cleanly, so those cases are
not what detects this.

**The author's account of why the first version of the test was blind is also
correct, and this session saw it directly.** Under the broken launcher, the
assertion "it exited 1" *passed*, because the launcher exited 1 a few lines later at
an unrelated precondition. So did the assertion that nothing was created. Of the
eight assertions in the first refusal case, only two — that the refusal said so in
its own words, and that the script stopped there rather than running on — can see
the breakage at all. Those two are the whole detector. An exit status shared by two
different refusals says nothing about which one fired, and that is not a theoretical
worry here: this session watched it not fire.

**A second, harder breakage the author did not try.** The refusal's words were left
in place and only the stopping was removed, so the launcher announced that it was
refusing and then launched anyway. The word-based assertion cannot see this. The
test still caught it:

```
checks passed: 34   failed: 4
```

four failures, all of them the positional assertion, and the test exited 1. So the
two assertions are not redundant: one catches a quiet downgrade, the other catches a
loud but toothless one. That is a stronger result than the commit claims for itself.

**Restoration proved.** After both breakages the launcher was restored and checked
two ways: its hash matches the version taken from the commit
(`ab9e72d9dcf0159758f1aeaf0385b0c9bfe34c7633e2f2cbe1c2e65430a0ca39`), and comparing
the working file against the commit prints nothing.

Against the standard in `docs/known-failure-modes.md` — that a test never seen to
fail has not been shown to detect anything — this test now clears the bar twice over:
seen failing by its author, and seen failing again, on a breakage of a different
shape, by a session that did not write it.

---

## 3. What it declines to gate on, and whether that is right

The guard reads the two per-power-source idle timers and never decides on them. The
reasoning given is that the display timer only darkens the screen, that the idle
timer is already held off by the wakefulness command the launcher spawns its watchdog
under, and that neither survives the lid coming down. A control case pins this in
place: a machine with fifteen-minute timers on both power sources — a machine that
would idle-sleep — must not be refused.

**The reasoning is right, and the control is right to exist.** The display timer
genuinely is a screen-brightness setting with no bearing on whether the machine stays
awake. The wakefulness command really is spawned with the flag that holds off idle
sleep, so for as long as the watchdog lives the idle timer cannot fire. And neither
mechanism does anything about a shut lid, which is the failure that has cost money.
Gating on the idle timer would refuse machines that are in fact safe, which is how a
guard gets switched off and stops protecting anything. Passing this Mac, with its
fifteen-minute timers, is correct rather than a hole.

**But the coverage claim is overstated in time, and that is the must-fix below.** The
wakefulness command is spawned at the very end of the launcher, on line 597. The
rented machine comes into existence on line 360. Between those two points the
launcher creates the machine, pushes the code, runs the remote checks and starts the
training — and during all of it nothing is holding off the idle timer. On this Mac
that timer is fifteen minutes, which is not obviously longer than a slow launch. If
it fires in that window the result is the exact shape the guard exists to prevent: a
rented machine exists, the Mac is asleep, and nothing awake is left to delete it.

This gap is not introduced by this commit — it is a property the launcher already
had, and the commit leaves the situation strictly better than it found it. What the
commit adds is a sentence saying the idle timer is already covered, with no
qualification about when the cover starts. A later session reading that sentence to
decide whether the window needs anything would be told, wrongly, that it does not.
The sentence is the stated reason for the control case, so it is load-bearing, and
correcting it costs nothing and changes no behaviour.

---

## 4. The override

**The constraint is real.** The launcher refuses any command-line argument with exit
status 2, under a guard ruled by John on 2026-09-22 after an argument that was
silently ignored led to a rented machine being created by a command whose stated
purpose was to create nothing. So a switch spelled as a flag could not work, and an
environment setting is the only shape available. Confirmed directly: case **P** above
shows the argument guard firing before the sleep check on a sleepy Mac, and case
**Q** shows the override rejected when spelled as an argument. The override does not
weaken the argument guard in any way this session could find.

**Overridable is the right call.** The shutdown fix of 2026-09-21 bounds what a
sleeping laptop costs at roughly fifty cents, and nothing at this point in the script
can know whether the machine's own watcher will arm. A guard that cannot be overridden
at a bounded cost of that size is a guard someone eventually comments out, and a
commented-out guard protects nothing. Refusing by default and taking an explicit,
loudly announced setting to proceed is the proportionate shape.

**The shape of the test is wrong, though, and the commit message misdescribes its own
precedent.** The override fires on the setting being non-empty, not on it being `1`.
So `ALLOW_LAPTOP_SLEEP=0` and `ALLOW_LAPTOP_SLEEP=false` both switch the guard off —
cases **N** and **O**. The commit message justifies the shape as "the same shape as
`ON_UNARMED`", and it is not: the shutdown-policy setting compares its value against
names and sends everything it does not recognise to the money-safe branch, whereas
this one sends everything it does not recognise to the money-losing branch. There is
house precedent for the non-empty test — the preview setting in the same file works
that way — but that one fails safe and this one fails open.

This is a follow-up rather than a blocker, on one ground: the failure announces
itself. Someone who types `ALLOW_LAPTOP_SLEEP=0` sees a banner saying the guard has
been overridden and quoting what it can cost. The billing failures this guard exists
to stop were silent. A loud wrong answer is a different and much smaller problem than
a silent one.

---

## 5. Regressions

All re-run by this session, all green.

| What was re-run | Result |
|---|---|
| The launcher argument-guard check, `src/check_launcher_argument_guard.sh` | 21 checks, all pass, exit 0 — including its negative control, which still rejects an unguarded stand-in |
| The shutdown-handshake test, `src/reap_handshake_selftest.sh` | 26 checks passed, 0 failed, exit 0 |
| A preview run of the derived launcher on this real Mac | Exit 0, reported creating nothing |
| The three module self-tests — the curriculum, the encoding and the trainer | All three report OK |
| The new sleep-guard test itself, unbroken | 38 checks passed, 0 failed, exit 0 |

One of these is worth more than its line in the table. The argument-guard check runs
a preview of this launcher on this Mac, and this Mac is one the sleep guard *would*
refuse. The preview still exited 0 and still reported creating nothing. So the
carve-out that lets a preview report the problem and carry on is not merely asserted
by the new test against a stand-in — it is exercised against the real settings by a
test that predates it.

---

## 6. The claim about the derivation script — verified, and true

The commit says that `src/derive_fetch_first_launcher.py` has not reproduced the
derived launcher since 2026-09-22, because the argument guard was applied by hand and
never added to the derivation script. This session checked that independently, by
running the derivation itself.

The script takes the file to read and the file to write as arguments and never writes
the registered launcher, so it was run to a scratch file. It succeeded, and all nine
of its replacements still matched exactly once — the script is not broken, only out
of date.

Against the launcher **as this commit leaves it**: 619 lines against 492, differing at
129 lines. Against the launcher **as it stood immediately before this commit**: 509
lines against 492, differing at exactly 17 — and those seventeen are the argument
guard and its comment, nothing else. So the claim is right, and right to the line:
reproduction broke on 2026-09-22, with the hand-applied argument guard, and this
commit widens a gap that already existed rather than opening it.

**The defect that follows is in a document.** `reap-shutdown-order-method.md` says:

> That makes "derived verbatim" a checkable claim rather than a promise: re-run it
> and compare. It never writes to the registered file.

Re-running it and comparing is exactly what this session did, and the comparison
fails. The invitation was true when it was written on 2026-09-21 and has been false
since the next day. Under the standard in `docs/known-failure-modes.md` this is the
familiar species: a check offered as runnable that no longer runs clean, left standing
because nobody ran it. It is not a defect in this commit — indeed this commit is where
the problem is first disclosed, in the launcher's own header, which now says plainly
that re-running the derivation no longer reproduces the file. What is left over is that
the method note still invites the comparison without saying it will fail.

Two honest ways to close it, neither of them this commit's job: teach the derivation
script the two hand-applied blocks so the invitation becomes true again, or amend the
method note to say the derivation records the file's origin and no longer reproduces
it. The first is better if the derived launcher is going to keep changing.

---

## Findings

### Must fix before merge

1. **The sentence giving the reason not to gate on the idle timer overstates the
   cover, and it is the load-bearing sentence.** The launcher's comment says the idle
   timer "is already covered by the `caffeinate` the launcher spawns its watchdog
   under". That cover starts on line 597. The rented machine exists from line 360. The
   window between them — machine creation, code push, remote checks, training start —
   has no cover at all, and this Mac's idle timer is fifteen minutes. The sentence
   needs the words that say when the cover begins, and a line saying the launch window
   itself is uncovered. Text only; no behaviour changes; the control case stays exactly
   as it is. *(If John would rather this land today, this is the one item to carry into
   the next commit and nothing else on this page is.)*

### Can follow

2. **Every non-empty value of the override switches the guard off**, including `0` and
   `false`, and the banner then reads "OVERRIDDEN by ALLOW_LAPTOP_SLEEP=0", which
   contradicts itself. One line to change, and one case to add to the test, which
   currently exercises only `1` and empty. The commit message's claim that this matches
   the shutdown-policy setting's shape is wrong in the direction that loses money, and
   should be corrected wherever it is repeated.

3. **A reading that is present but unintelligible is reported as "the override is
   OFF".** Feeding it `SleepDisabled enabled` produces a refusal that names a state the
   guard never established. It refuses either way, so no money is at risk; the
   diagnostic sends the operator to the wrong fix.

4. **When the override is off and the Mac is on battery, only the first is reported,
   and the fix printed does not mention plugging in.** The operator corrects the
   override, re-runs, and is refused again. Naming both at once costs a few lines.

5. **A charger that has stopped delivering is not caught.** With the override on and
   the Mac reporting wall power while the battery sits at 2% and discharging, the guard
   passes. The same command it already runs prints the charge level and the word
   "discharging" on the very next line. The guard's own stated reason for requiring wall
   power — that the override cannot outlast a flat battery over a run this long —
   applies to this case word for word, and it is the one route to a flat battery the
   guard does not close.

6. **The power-reading command's success-or-failure report is ignored.** A command that
   fails but still prints a reading is believed. Narrow, since a reading has to exist
   for this to matter at all.

7. **There is no time limit on the reading.** A hung command hangs the launcher with no
   further output; it was still going after 25 seconds. It creates nothing while hung,
   so this is a nuisance rather than a risk, but a hung launcher with no explanation is
   worth one line of timeout.

8. **The pattern that extracts the power source grabs too much** when the line holds a
   second quoted phrase, garbling the refusal message. It still refuses. Cosmetic.

### Not in this commit

9. **`reap-shutdown-order-method.md` offers a comparison that no longer holds.** Its
   invitation to re-run the derivation and compare has been false since 2026-09-22, and
   this session confirmed it by running the comparison: 17 differing lines then, 129
   now. A real defect in a document, and a cheap one to close either way.

---

## Plain-language check

The new text in both files was read against the workspace plain-language rule. It
holds up: the refusals speak in ordinary words ("shut the lid and this Mac sleeps,
taking the watchdog with it"), the phrase "idle billing" is given its plain meaning
the first time it appears in each file, and the settings named in the messages are
named because an operator has to type them, which is the exception the rule allows.
No new shorthand is coined. This page is written to the same rule.

---

## What this check does not establish

It exercised the guard against stand-ins, never against a Mac in any of the states it
refuses. Nobody put this Mac on battery, and nobody turned the never-sleep override on
or off. So what has been shown is that the guard reads what the tool prints and decides
correctly on it — not that the tool prints what this session assumed in every real
state. The stand-in's layout was checked against the real tool's output on this Mac for
all three readings and matches it. The one real state exercised end to end is the one
this Mac is in: override off, on wall power, which the guard refuses and which the
preview run reports and carries past.

It also did not run the staged slice, create anything, or contact any vendor, and it
has not checked anything in the commit beyond the two files named at the top.
