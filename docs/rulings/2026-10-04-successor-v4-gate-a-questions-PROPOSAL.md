# Proposal for John, 2026-10-04: six questions from the inside review of proposal version 4, one page each

*Written 2026-10-04 (Pacific) by a Claude Code session in its own worktree,
on branch `gate-a-v4-dispositions`. **This is a proposal, not a ruling.
Everything in it is PROPOSED. Nothing is decided or registered, and no
registered text, ruling file, protocol text or proposal text is changed by
it.** Nothing was rented or spent: $0.*

*Written under the workspace plain-language rule. MEASURED means a command
was run and its output is in a committed file named beside it; ARGUED means
reasoning a reader can dispute.*

**What it covers.** The inside (tier 1) review of the successor
experiment's registration text, version 4
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`,
on pull request 94), found ten things, numbered RT-237 to RT-246: one fatal,
four serious, five worth-noting. Each has a drafted disposition, with the
exact text it would put into the registration and a reason, in
`docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`. This
packet asks only the questions that are John's, six of them.

**Three things to know before relying on it.**

1. **This session wrote none of what the review looked at**, and did not
   write the review. It did run two small measurements at $0 that pages 1
   and 4 rest on (`docs/2026-10-04-gate-a-v4-dispositions-measurements.md`,
   with the method committed before the output).
2. **It has been checked** by a session that did not write it (pull
   request 96): both measurements reproduced exactly; four wording defects
   it found are fixed here, and its caveat is on page 1.
3. **The outside reviewers have not answered yet.** Their findings will come
   in their own packet. These six can be ruled now; nothing here waits on
   them.

---

## The one-page index

"Agreed on all", or exceptions by page number, is enough. A session then
records the ruling in a rulings file dated the day it is made, with authorship marked mixed, and a different
session checks it.

| Page | Question | Recommendation (John's to overturn) | Confidence |
|---|---|---|---|
| 1 | **The fatal one.** The free model's gate requires "batteries" this task does not have, so as written the free model could never be read (RT-237). Strike the clause, or replace it? | **Replace** it with a check the task can evaluate: with the acting channel removed, the model still answers with one of the four values the rest of the act allows, 1,546 or more of 3,000, on two seeds of three. Amends your ruling of 2026-09-26, page 1h. Weaker than it looks: see page 1's caveat | moderate; striking the clause is a close second |
| 2 | The floor as printed would let a model at chance through, and a sentence you adopted on 2026-10-04 has a wrong figure (RT-238, RT-244) | Write the code's own safeguard into the text, and correct the figure | high |
| 3 | The text never writes down the episode format that keeps the model's own name out of the moment it acts (RT-239) | Register the format in full: the rehearsal's grammar at its sizes, its two deliberate differences from the closed design, and the self-tests that check them | high |
| 4 | The episode counts you ruled on 2026-10-03 were tried only at a third of the registered width (RT-240) | Fit every read on 1,800 development episodes, not 420; one $0 toy re-run, checked, before registration | moderate |
| 5 | **Some results the registered runs can reach have no registered name** (RT-241) | One outcome table, with three new names. The words of the new names are yours | moderate; low on the exact words |
| 6 | Four wording fixes (RT-242, RT-243, RT-245, RT-246) | Accept all four as drafted | high |

**What a "yes on all" adds to the work before registration:** one toy
re-run at $0 and its check (page 4), and the check of page 1's repair owed
under the closure rule. Everything else is wording in version 5.

---

## Page 1 — the free model's gate names "batteries" this task does not have (RT-237, fatal)

**The question.** Before the free model is read, its acting channel (the
input that tells it "this turn is yours") is switched off to check that its
ownership answer collapses. Your ruling of 2026-09-26 (page 1h) added: "the
ownership-free batteries must hold". Those batteries were question sets at
the end of each episode in the closed design. The successor's task has none.
What should the clause become?

**Why it is fatal.** The design's own stop rule S8 says a gate that cannot be
evaluated counts as failed. So, as written, the free model could never be
read, and the best registered outcome could never be reached.

**What the clause was for.** To show that switching the channel off removed
the ownership answer, and not the model's whole grip on the episode.

**What this task has instead (MEASURED today, $0, on every committed toy
model).** With the channel off, a model that has lost only "which agent am
I" still answers with the successor of one of the four agents' values on the
right item, and so is right about one time in four, which is the collapse
level the gate already uses. Counting how often its answer is one of those
four:

| Model | With the channel off, of 3,000 | Line: 1,546 (above one half, the chance level among the eight values) |
|---|---|---|
| Free model, seeds 0 / 1 / 2 | 2,100 / 2,238 / 2,324 | holds on all three |
| The three built models and the competing solver | 2,132 to 3,000 | hold on every seed |
| Untrained weights (to show the check can fail) | 0 / 620 / 726 | fails on all three |

**The options.**

- **(a) Replace the clause with that count**, line 1,546 of 3,000, on two
  seeds of three.
- **(b) Strike the clause**, with its reason on the record. Simpler; a
  channel removal that left the model answering at random would then count
  as a collapse.
- **(c) Report the count with no line.** Weaker than either.

**The caveat, found by the independent check of this packet (pull request
96, section 6).** The check refuses a model that answers with noise. It
cannot tell whether switching the channel off broke the step "find the item
the action names": a model that had lost the item and answered the successor
of any of the eight values shown would score about **2,257** of 3,000, above
the line and above the free model's lowest seed (2,100). The line cannot be
raised to catch that without failing the toy's free model on two seeds and
its entangled model on all three. So what (a) shows is only "the model still
answers with the successor of a value it was shown", and if it is ruled, the
registered sentence says exactly that.

**Recommendation: (a), narrowly.** It keeps part of what page 1h asked for,
it has been measured on every toy model, its line comes from chance rather
than from any toy figure, and it passes the free model by more than 550
episodes. But for the reason above it is closer to (b) than it first looked.
*Confidence: moderate.* **Strongest alternative, and a close one: (b).**

**Either way**, the closure rule requires a measured check by a session other
than the one that writes the fix. The dispositions file lists it: every
clause of the gate named against a field of a committed output file, and the
counts above recomputed by independent code.

*Changes:* version 5, sections 6.4, 7.4, 8.2 and 9; a dated note beside page
1h of `docs/rulings/2026-09-26-weekend-1-queue.md`.

---

## Page 2 — a safeguard that is only in the code, and a wrong figure in an adopted sentence (RT-238, RT-244)

**The question.** Should the registration say what the code already does?

**The facts (MEASURED by the review, reproduced here).** The floor that
decides whether a place in the model is usable is written as an inequality.
For a model at chance the right-hand side is zero or below, and the
inequality is met everywhere, with a divisor of zero or below. The code
refuses that case by one extra condition that the text does not carry. On
the ordinary competing solver, the text's rule admits every place on four
runs of six; the code admits none. No toy verdict changes either way.

Separately, the sentence you adopted on 2026-10-04 (ruling 2) says the
solver's no-transplant rate "missed the no-transplant rule by 0.11 or
more". It missed the formula by 0.109 or more, and the allowance by 0.091 or
more.

**Recommendation: write the code's condition into the text, and correct the
figure** (exact wording in the dispositions file). *Confidence: high.* The
registered code is written from the text, and the first known failure on
this programme's list is a divisor that was zero. With the condition
written in, the first clause of your adopted sentence ("no site set cleared
the floor at nomination") is true of the text too. **Alternative:** none
worth taking.

*Changes:* version 5, sections 6.4 and 9, and the sentence of ruling 2
wherever it is quoted.

---

## Page 3 — the episode format that keeps the model's own name out of the act (RT-239)

**The question.** Should the registration write down the exact episode
format, rather than describe it as an extension of the closed design's?

**Why it matters.** Version 4 says the grammar "extends" the closed design's
generator. That generator shows the model its own name three tokens before
it acts, and its own header calls that a way to read "a name badge" instead
of carrying the answer. The rehearsal's grammar removes the name from the
act and never shows the answer, so the two episodes of a matched pair are
the same text; but those two choices are written nowhere in the
registration. Someone building the registered generator from the text could
put the name back, and the free model could then pass by copying it.

**Recommendation: register the format in full**: the rehearsal grammar at
its sizes (four agents, two items, eight values, 56 tokens), its two
deliberate differences, and its existing self-tests ("matched pairs are
token-for-token identical", "no name badge", both passing today), and say
the closed design's twelve turns and batteries are not carried.
*Confidence: high.* **The one choice inside it:** the rehearsal's sizes are
the only ones any toy figure was measured at; larger sizes would need their
own rehearsal.

*Changes:* version 5, section 4.1.

---

## Page 4 — the episode counts at the registered width (RT-240)

**The question.** On 2026-10-03 you ruled that the registered measurement
uses the toy's counts, so every read is fitted on 420 episodes. The toy's
model is 160 wide; the registered one is 448. Keep the counts, or change them?

**The facts (MEASURED on a stand-in, NOT A RESULT).** The review widened the
toy's states to 448 with random noise. The entangled model's read then
fell below the floor (144 of 180) on two seeds of three. This session
repeated that exactly and tried the review's two cheap repairs, on the seed
that fails worst:

| Read fitted on | Smallest piece count, of 180 (floor 144) |
|---|---|
| 420 episodes (as ruled) | 74 |
| 900 | 120 |
| 1,800 | **156** (and every other seed and draw above 144) |
| 420, with a ten or a hundred times stronger penalty | 78, 85 |

At the toy's real width, fitting on more episodes changes no toy verdict;
the free model still misses the floor by a wide margin (41 at most).

**The options.**

- **(a) Fit every read on 1,800 episodes**, keeping the 180 held out and the
  600 pairs the transplants run on. Needs one $0 toy re-run of the
  nomination and reading, with method first, and its check, before
  registration, because the read's directions decide what gets
  transplanted.
- **(b) Keep the ruled counts** and carry the risk as a named weakness. No
  re-run; but if the high anchor misses its floor at full size, the
  two-model fallback fires, after both releases of money are drawn.
- **(c) Also train a 448-wide stand-in on the laptop** and try the read on
  it before registration. The only thing that would really settle it; $0,
  not yet timed, and a new training run needing your go. It can be added to
  (a).

**Recommendation: (a).** *Confidence: moderate.* The stand-in is noise, not a
trained model, and 1,800 is the smallest size tried that held, not a size
derived from anything; the registration says both. **Strongest alternative:
(b).**

*Changes:* version 5, sections 7.4, 9 and 13; a dated note beside ruling 4
of `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` and its
twin record.

---

## Page 5 — results the registered runs can reach that have no registered name (RT-241)

**The question.** The registration forbids reporting an outcome in words
that are not registered. Several reachable results have no words. Should
one table name them all?

**The holes.** No verdict on the separable model maps to nothing. The
two-model fallback (accepted by you in advance on 2026-09-20) has no term.
"R3 for that arm" mixes an arm's result with the experiment's. A failed
channel-removal check on the free model maps to nothing. And who gets the
one permitted re-run at step 5b is not said, when the second release as
ruled holds no money for it.

**Recommendation: one table** (in full in the dispositions file). In short:

1. A gate failure on arm T, C or F, after the one re-run if it is still
   available, is **R3** for the experiment. **Arm M failing its gate drops
   arm M**, as its no verdict already does.
2. Arms T and C read and separate: arm F reads → **R1**; arm F no verdict
   or fails the channel-removal check → **"metric validated, degree not
   read"**, as already ruled.
3. Arms T and C read and do not separate → **R2**.
4. Arm C no verdict (the fallback): **"metric checked against the separable
   model only, degree read"** or **"…, degree not read"** (both new).
5. Arm T no verdict → **"metric not validated"** (new), with its reason;
   suggested as not satisfactory.
6. The one re-run goes to the first registered run that fails its gate: arm
   F at step 5a if it fails there, otherwise held for the first failing
   built-arm run at step 5b, on your go.

*Confidence: moderate that the table is needed; low on the exact words of
the three new terms,* which are yours. **The part most worth your thought:**
whether arm M's gate failure should drop it rather than make the whole
experiment R3, since that narrows a registered term. **Strongest
alternative:** name only the fallback and the arm-T case, and leave the
rest as reporting practice.

*Changes:* version 5, sections 3, 5.2, 7.4, 8.1 and 9. A dated note goes beside
the outcome list in `docs/december-result-roadmap-2026-09-20.md`.

---

## Page 6 — four wording fixes (RT-242, RT-243, RT-245, RT-246)

Each makes a sentence say what its record says. None changes a verdict.

- **RT-242.** "The three candidates reach 0.733, 0.383 and 0.478" are one
  candidate's three seeds. *Fix:* say so, and give the other two candidates'
  best, 0.417 and 0.633.
- **RT-243.** "On the toy [the two forms of the floor] never [disagree]" is
  true only for the own-directed grids; elsewhere they disagree on 576, 892
  and 1,080 rows, always with the plain form passing a model near chance.
  *Fix:* narrow the sentence and give that as the reason the registered form
  was chosen.
- **RT-245.** That the registered measurement fits on the laptop was argued,
  not timed; the review timed it at about two hours per model, about 25
  hours for all twelve, $0. *Fix:* cite the timing, and name the processor
  for the whole nomination, not only the read's fit, because the choice of
  place in the model once turned on one episode in 600.
- **RT-246.** The weakness you ruled on 2026-10-04 (ruling 7) says the toy
  has no model that does the task another way. The free model is one, and
  the measure returns no verdict on it. *Fix:* say which other route the toy
  has seen and which it has not (the name cue of page 3, closed by the
  grammar rather than tested).

**Recommendation: accept all four as drafted.** *Confidence: high.* RT-245
and RT-246 touch wording you ruled, so the ruling should say so.

*Changes:* version 5, sections 6.4, 7.2, 9, 11 and 13.

---

## One small item, for when it comes up

The review proposes a test for the known-failure list, for whoever next
edits it: *for every clause of every gate, name the field of a committed
rehearsal output file that evaluates it, and print that field; a clause with
no field is the finding.* It belongs with the drafted seventh entry ("an
outcome line a plan states in advance that the design cannot produce"),
which you have not yet ruled onto the list. **Suggestion:** fold the test
into that entry when it is ruled. Not needed for this registration; page 1's
check runs it on the one gate where it fired.
