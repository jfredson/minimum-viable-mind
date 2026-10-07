# PROPOSAL for John: the two built models that lost their ownership route, and four fixes to the spending alarm

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree, on
branch `ruling-packet-cm-flat`. **This is a proposal, not a ruling.
Everything in it, including the recommendation, is PROPOSED and yours to
overturn.** Nothing was rented, trained or spent: $0. Its source is the
independent check of the four 10-million-step development runs (pull request
106, not yet merged; its sections 6 to 8), read with proposal version 4
(sections 5, 11, 12 and its weakness W3) and the record of your 2026-10-06
rulings (pull request 103). This session ran nothing; every figure is that
check's.*

---

## Page 1 — the decision: arms C and M lost their built-in ownership route

**What was found.** Each built model works out "which agent am I" by counting
how often the "this turn is yours" signal fired on each agent's turns and
turning the counts into weights over the four agents. One learned number, the
*sharpness*, sets how decisive those weights are; it starts at 4.0, nearly all
weight on the right agent. In the 10-million-step runs, training drove it to
about zero in arm C (built with ownership stirred into everything, the high
end of the scale: 4.0 to −0.09) and arm M (built half separable, half stirred
in, the middle: to −0.01). At zero the answer puts a quarter on each agent and
says nothing. The registered measuring procedure confirms it independently:
it cannot find "which agent am I" in either model (best 41 and 45 right of
180; the floor is 144). Arm T (ownership kept in one swappable slot, the low
end) still works. In the small laptop models the number stayed alive in every
arm. Because it went *past* zero, training drove it there; weight decay (the
setting that slowly shrinks every learned number) cannot do that alone.

**Why it matters.** The claim rests on the measure telling apart models whose
answer is known from how they were built: T low, C high, M between. If
training can switch the built route off, arm C is just a second freely trained
model and "the measure separates the built ends" stops testing what it says.
Version 4 named this as weakness W3 (arm C's construction might not hold at
full size) and expected to see it only after both money releases were spent.
It has now been seen before anything is registered.

| Option | Cost | What it changes | What it risks |
|---|---|---|---|
| **1. Fix the sharpness at 4.0** in the built models | $0 code; toy models retrained on the laptop, $0; a short rerun of arms C and M, about $0.81 at this wave's bills, from the $8.53 left on the development line (needs your go) | Frozen model code; version 4's description of the three built arms | The network may still route round it by shrinking the layers that apply the answer; the toy evidence was gathered with the number learned |
| **2. Exempt it from weight decay** | as option 1 | Frozen training code | Probably does nothing: weight decay was not the cause |
| **3. Add an in-use check** that fails a built model whose route has gone flat | $0 code and its check | Frozen measuring code and version 4's gates; joins the open decision-procedure work (pull request 105) | Detects, does not prevent: a failure is still found after the money is spent, but recorded as "construction did not hold" |
| **4. Accept as is**, relying on your 2026-09-20 ruling that a fallback to arm T and the free model alone is accepted in advance | nothing now | nothing | The fallback becomes the likely end: it can show the measure *detects* something, not that it *scales*, after about $194 to $206 |

**Recommendation: options 1 and 3 together.** Fixing the number removes the
cause found; the check catches the network routing round it some other way.
Option 2 does not touch the cause; option 4 accepts a risk that is no longer a
forecast. Order: code change, toy retrain and re-read, its check, then the two
short reruns on your go, all before the registration deadline, 2026-10-18.

**How this bears on page 12 (continue or stop).** The recommendation on record
is "continue if the decoy test is not fooled", and the decoy test (pull
request 108, not yet checked) reports not fooled. But that assumed a working
high end. Proposed: **continue only if the built route is shown to hold at 10
million steps before registration; if it cannot be made to hold, stop or
redesign.** Choosing option 4 strengthens the case for stopping.

---

## Page 2 — four fixes to the spending alarm and its helpers

The spending alarm ("tripwire") is the automatic check that halts launches if
the vendor bills more than its posted rate. In the 10-million wave, billing
was normal (the balance fell $1.46 against $1.47 expected), but the alarm
could not have caught it if it had not been.

**1. It never read during the wave.** It reads the balance once an hour, and
the whole wave lasted 29 minutes, so it never compared spending with the rate
while machines ran. *Fix:* read every few minutes during a wave, with a rule
that can act on less than an hour of readings, or compare at each machine's
deletion. **Needs a ruling:** version 4 (section 12.5) registers "hourly".

**2. It did not know when machines were deleted.** At its next hourly reading
it marked all four machines as gone *then*, charged them as if they had run
until 01:11, and worked out a ratio of 0.40 where the true figure was 0.99.
The same error would hide overbilling, which is what it exists to catch.
*Fix:* the step that deletes a machine writes the deletion time into the
alarm's records. **A correction:** it makes the code do what the rule already
means; it needs only your go to touch frozen code.

**3. Empty bills were read as a pass.** The end-of-wave comparison of billed
hours against machine life read the vendor's not-yet-posted (empty) bills as
"zero hours billed" and passed. *Fix:* treat empty bills as "cannot be checked
yet", which counts as a trip. **A correction:** your standing rule (version 4,
section 12.7) already says a check that cannot run is a trip; the code
disagrees with it.

**4. The deadline timers outlive their machines.** Each machine has a timer on
the laptop that records when it hits its spending cap. These do not notice
the machine is gone; they were stopped by hand, or they would have written
false "deadline reached, $2.50" lines. *Fix:* each timer stops itself when its
machine is gone. **A correction**, housekeeping only.
