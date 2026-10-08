# PROPOSAL for John: the two built models that lost their ownership route, and four fixes to the spending alarm

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree, on
branch `ruling-packet-cm-flat`. **This is a proposal, not a ruling.
Everything in it, including the recommendation, is PROPOSED and yours to
overturn.** Nothing was rented, trained or spent: $0. Its source is the
independent check of the four development runs of the small,
10-million-parameter models, each trained for 108,919 steps (pull request
106, not yet merged; its sections 6 to 8), read with proposal version 4
(sections 5, 11, 12 and its weakness W3) and the record of your 2026-10-06
rulings (pull request 103). The registered runs use larger, 30-million-parameter
models. This session ran nothing; every figure is that check's, or the check
of this packet's.*

*Revised the same day after the independent check of this packet (pull
request 112), applying all eight of its points; see the change note at the
end.*

---

## Page 1 — the decision: arms C and M lost their built-in ownership route

**What was found.** Each built model works out "which agent am I" from how
often the "this turn is yours" signal fired on each agent's turns. One learned
number, the *sharpness*, sets how decisive that answer is; it starts at 4.0,
nearly all weight on the right agent. In the 10-million-parameter development runs it
fell to about zero in arm C (built with ownership stirred into everything, the
high end of the scale: 4.0 to −0.09) and arm M (built half separable, half
stirred in, the middle: to −0.01). At zero the answer puts a quarter on each
of the four agents and says nothing; the measuring procedure, independently,
cannot find "which agent am I" in either model (best 41 and
45 right of 180, where the pass mark is 144, four fifths). Arm T (ownership
kept in one swappable slot, the low end) still works, though its sharpness
also fell, to 1.95. The fall was already visible in the small laptop models:
arm C's sharpness there ended at 1.73, 0.70 and 0.93 on its three seeds. Each
development run is one seed, but both arms C and M went flat. **Why:** the
setting that slowly shrinks every learned number (weight decay) alone would
have left it at about 1.34, and arm T, under the same setting, kept 1.95;
training pushed arms C and M the rest of the way.

**Why it matters.** The claim rests on the measure telling apart models whose
answer is known from how they were built: T low, C high, M between. With the
route off, arm C is just a second freely trained model, and "the measure
separates the built ends" stops testing what it says. Version 4
named this as weakness W3 and expected to see it only after both blocks of
spending you approved in advance had been spent. It has been seen first.

| Option | Cost | What it changes | What it risks |
|---|---|---|---|
| **1. Fix the sharpness at 4.0.** (a) arms C and M only; (b) all three built arms, T too | (a) rerun C and M, about $0.81; (b) about $1.14, plus re-reading arm T on the laptop. Both from the $8.53 left of the $10 you approved for development runs; both need your go | The model code fixed and tested on 2026-10-04 to be registered as is ("frozen"); version 4's arm descriptions | The network may route round it by shrinking the layers that apply the answer; the toy evidence had the number learned |
| **2. Exempt it from weight decay, and check it stays above a minimum** | about $0.81 to $1.14 as above | Frozen training code; a new check | Decay is only part of the cause, so the check would likely fire: a failure found, not prevented |
| **3. Keep it learned, but never below a minimum** | as above | Frozen model code | Same route-round risk as 1; one more setting to choose |
| **4. Add an in-use check** that fails a built model whose route has gone flat | $0 code and its check | Frozen measuring code and version 4's gates; joins the open decision-code work (pull requests 105 and 107) | Detects, does not prevent: a failure is found after spending, but recorded as "construction did not hold" |
| **5. Keep version 4's plan.** Its weakness W3 already says a failed arm C fires the fallback to arm T and the free model "rather than a repair" (accepted in advance, 2026-09-20); a failed arm M is dropped | nothing now | nothing | The fallback becomes the likely end: it shows the measure *detects* something, not that it *scales*, after about $194 to $206 |

Options 1 to 4 are repairs, so each departs from that stated plan.

**Recommendation: option 1(b) with option 4.** Fixing the number in all three
built arms removes the cause found and keeps the built arms alike (arm T is
drifting too); the check catches the network routing round it. **Time cost:**
a change to frozen code, retraining and re-reading the laptop models, the new
check, three reruns on your go, and an independent check of each; by this
session's estimate several working days of the twelve calendar days left before the
registration deadline (2026-10-18), beside other work owed in the same code.

**Page 12 (continue or stop).** Your words were "decide after the decoy test,
go with the recommendation", whose condition was "continue if not fooled".
The decoy test (whether the read can be fooled by an unused copy of the
owner's marker; pull request 108, not yet checked) reports not fooled, but it
ruled out an exact copy only, not one coded differently. This proposal
**changes the condition you endorsed**: continue only if the built route is
shown to hold in the 10-million-parameter reruns before registration (evidence
for the 30-million size, not proof); if it cannot be made to hold, stop or
redesign. Option 5 strengthens the case for stopping.

---

## Page 2 — four fixes to the spending alarm and its helpers

The spending alarm ("tripwire") is the automatic check that halts launches if
the vendor bills more than its posted rate. In the four machines launched
together on 2026-10-04, billing was normal (the balance fell $1.46 against
$1.47 expected), but the alarm could not have caught it if it had not been.

**1. It never read while the machines ran.** It reads the balance once an
hour, and the whole launch lasted 29 minutes; the check before each launch
read too briefly to compute anything. *Fix:* read every few minutes while
machines run, with a rule that can act on less than an hour of readings, or
compare at each machine's deletion. **Needs a ruling:** version 4 (section
12.5) registers "hourly".

**2. It did not know when machines were deleted.** At its next hourly reading
it marked all four as gone *then* and charged them as if they had run until
01:11. Its figure, spending divided by what the posted rate predicts (1.0
means billed as posted), came out 0.40 where the true figure was 0.99. The
same error would hide overbilling, which is what it exists to catch. *Fix:*
the step that deletes a machine writes the deletion time into the alarm's
records. **A correction:** it makes the code do what the rule already means;
it needs only your go to touch frozen code.

**3. Empty bills were read as a pass.** The end-of-launch comparison of billed
hours against machine life read the vendor's not-yet-posted (empty) bills as
"zero hours billed" and passed. *Fix:* treat empty bills as "cannot be checked
yet", which counts as a trip. **A correction:** your standing rule (version 4,
section 12.7) already says a check that cannot run is a trip.

**4. The deadline timers outlive their machines.** Each machine has a timer on
the laptop that deletes it if it reaches its spending cap: the last line of
defence on cost. The timers do not notice when the machine is already gone;
they were stopped by hand, or they would have written false "deadline
reached, $2.50" lines. *Fix:* a timer stops itself only on a confirmed
deletion (the watchdog's own "machine gone" record, or the vendor saying the
machine does not exist), never on a failed or empty reading. **A correction
with that condition;** without it, it would be a change to a safety control.

---

## Change note

*2026-10-06, after the check of this packet (pull request 112,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-06-cm-packet-check-claude-code.md`
on branch `check-cm-packet`). All eight points applied: the runs described as
10-million-parameter models of 108,919 steps, and the registered size given
(point 1); the weight-decay argument replaced by the size argument (2);
option 2 restored as its source had it, and the minimum option added (3);
option 1 split by whether arm T is included, with costs, and one variant
recommended (4); the recommendation's time cost stated, and the last option
described as version 4's existing plan, which drops arm M (5); the toy trend
and the one-seed limit added (6); page 12 states your words and the decoy
test's limit (7); fix 4 states the timer is the cost backstop and stops only
on a confirmed deletion (8). Terms the check flagged are explained in place.*
