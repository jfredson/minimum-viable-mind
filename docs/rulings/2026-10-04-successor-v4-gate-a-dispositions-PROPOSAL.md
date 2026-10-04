# PROPOSAL — draft dispositions for the inside review of successor proposal version 4 (findings RT-237 to RT-246)

*Drafted 2026-10-04 (Pacific) by a Claude Code session in its own worktree,
on branch `gate-a-v4-dispositions`, cut from the review branch
`gate-a-registration-review-successor-v4` at `0fcc25c` (pull request 94).
Asked for by the coordination session, so that John can rule on every
finding in one sitting. **Nothing here is ruled.** Every disposition below is
a recommendation for John, marked PROPOSED. When he rules, the session that
records the ruling copies the accepted lines into the experiment's red team
ledger (`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`).
This session did not edit the ledger, version 4, the review, any ruling
file, the protocol or the known-failure list. Nothing was rented or spent:
$0.*

*Written under the workspace plain-language rule. Findings and checks are
labelled **MEASURED** (a command was run and its output is given or filed)
or **ARGUED** (reasoning a reader can dispute). Two documents are cited
throughout and named once here:*

- *"version 4" is `docs/successor-experiment-proposal-2026-10-03-v4.md`, the
  successor experiment proposal, version 4, as on the review branch;*
- *"the review" is the inside (tier 1) review of it,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`,
  with its scripts in the folder beside it.*

*The short ruling packet that puts the questions to John is
`docs/rulings/2026-10-04-successor-v4-gate-a-questions-PROPOSAL.md`. This
file is the detail behind it: the exact text each disposition would put into
the registration text, and why.*

**Three things to know before relying on this.**

1. **Who wrote it.** A fresh session with no chat history. It wrote none of
   version 4, the review, the rulings or the runs they cite. It did write the
   two $0 measurements this file cites
   (`docs/2026-10-04-gate-a-v4-dispositions-measurements.md`, method committed
   first at `f13f28d`, output at `b1c0a16`), so where a recommendation rests on
   them, a reader is relying on this session's own work.
2. **It is owed a check.** A proposal on its way to John is binding text
   under the pairing rule (`docs/outside-review-protocol.md`, "The pairing
   rule"), so a session that did not write it checks it, and checks the two
   measurements, before John relies on a number in it. **Done:** an independent check was
   filed as pull request 96 (branch `check-gate-a-v4-dispositions`, filed in
   the experiment's reviews folder on that branch, not yet on this one; called "the check of these dispositions"
   below). Both measurements reproduced exactly. It found four text defects
   and two smaller points, all fixed in this revision, and a caveat on the
   battery-clause repair, now stated under RT-237 and on page 1 of the
   packet.
3. **The outside review is not in it.** The outside (tier 2) packet is with
   John; no outside response is filed. The outside reviewers' findings will
   need their own dispositions. These ten can be ruled now or together with
   those; nothing here depends on them.

---

## Headline

**One fatal finding, closable without new spending; four serious, all
recommended for acceptance; five worth-noting, all recommended for
acceptance as wording. No finding is recommended for rejection.**

- **The fatal one** (RT-237, the free model's gate requires "batteries" the
  task does not have): replace the clause with a check the task can evaluate
  — with the acting channel zeroed, the model's answer is still one of the
  four values the ownership-free part of the act allows — with a line set
  from chance, 1,546 of 3,000. Measured at $0 on every committed toy model
  today: every trained model holds it with a wide margin (the free model at
  2,100 to 2,324), and untrained weights fail it (0 to 726). It amends John's
  ruling of 2026-09-26 (page 1h), which wrote the batteries in.
- **The serious one that adds work** (RT-240, the ruled episode counts were
  rehearsed only at the toy's width): fit every read on 1,800 development
  episodes, not 420. On the review's own stand-in this is the only one of
  the repairs tried that holds; 900 episodes and stronger regularisation do
  not. It amends John's ruling of 2026-10-03 on the episode counts, and it
  needs a $0 toy re-run of the nomination and reading, with its check,
  before registration.
- **The serious one that most needs John's own words** (RT-241, holes in the
  outcome map): one outcome table, with three new registered terms, for
  states the registered runs can reach and nothing now names.
- The other two serious ones (RT-238, the floor as printed lets a model at
  chance through; RT-239, the grammar that keeps the model's own name out of
  the act is not written in the registration) are text changes that make
  the registration say what the code already does.

---

## The checks this session ran

All from the root of this worktree on 2026-10-04, with the project's Python
(`~/Code/minimum-viable-mind/.venv/bin/python`). "V4" is version 4.

| # | Command (abridged to what it tests) | Output | What it shows |
|---|---|---|---|
| C1 | `grep -n -i "batter" V4` (excluding the four other hits: three about the closed design's batteries and one, line 1769, about this design's "control battery") | line 2223: "the ownership-free state and syntax batteries **must hold**."; line 2270: "...the ownership-free batteries must hold; gates arm F only" | The battery clause is in section 8.2 and the section 9 row, as the review says |
| C2 | `grep -n "batteries" docs/rulings/2026-09-26-weekend-1-queue.md` | line 66: "...named-other clause is reported and not gated; the ownership-free batteries" | John's ruling of 2026-09-26, page 1h, carries the clause; removing it amends that ruling |
| C3 | `lesion_content_check.py` (part A of this session's measurements) | line 1,546 of 3,000; with the channel zeroed the free model's candidate counts are 2,100 / 2,238 / 2,324, arms T, C, M and the competing solver hold on 3 of 3 seeds, untrained weights 0 / 620 / 726 hold on 0 of 3 | The proposed replacement clause can be evaluated, refuses a model that answers with noise and passes every trained one (it would also pass a model that lost which item is named: see RT-237) (MEASURED, NOT A RESULT about the question) |
| C4 | compare part A's correct counts with `out-repairs/gate_base.json` | 15 of 15 trained models equal, with the channel on and zeroed | The new script measures on the same episodes and models as the committed gate |
| C5 | `sed -n 276p experiments/rehearsal-successor-measure/src/repairs.py` and `grep -c "need > 0" V4` | `clears=bool(whole - untouched >= need and need > 0)`; `0` | The code refuses a requirement at or below zero; the text does not say so (RT-238) |
| C6 | re-run of the review's `solver_sentence.py`, `floor_forms.py` and `older_figures.py`, diffed against their committed outputs | 0 lines differ in all three | The figures behind RT-242, RT-243 and RT-244 reproduce; the replacement sentences below quote them |
| C7 | `grep -n "Twelve turns\|name badge\|three tokens" .../src/curriculum_a3.py` and `grep -n "ten turns" V4` | A3 line 13 "Twelve turns, four agents, two *contested* items"; line 79 "...its own marker is in the context three tokens"; line 82 "reading a name badge at act time"; V4 line 500 "ten turns" | Version 4 credits the closed design's grammar with the successor's ten turns, and points at the generator that has the name cue (RT-239) |
| C8 | `grammar.py --self-test` (the rehearsal generator) | "[PASS] matched pairs are token-for-token identical"; "[PASS] no name badge — the own-directed turn shows only the self word"; "all checks passed" | The two properties RT-239 asks the registration to state are already asserted by a self-test that can be named |
| C9 | `width_fit_pool_standin.py` (part B) | the review's stand-in reproduces 5 of 5 cases exactly; smallest piece on the entangled model's seed 1: 74 at 420 fitting episodes, 120 at 900, **156 at 1,800**; 78 and 85 with stronger regularisation; at the toy's width the free model's best piece is 41 at most | Of the repairs tried on the stand-in, only 1,800 fitting episodes holds; no toy verdict changes at width 160 (MEASURED on a stand-in, NOT A RESULT) |
| C10 | `grep -n "fires the two-arm fallback\|without its re-run line" V4` | line 462 (the fallback); line 2732 "release without its re-run line: $84.06 + $12 + $23" | The second release as ruled holds no re-run money (RT-241, hole 5) |

---

## Draft dispositions, one line per finding (ledger form)

Order: the fatal finding, the serious ones, then the worth-noting ones.
Every line is **PROPOSED**. "Confidence" is this session's confidence that
the recommendation is the right ruling.

| Finding | Reviewer | The finding, in plain words | Severity as filed | Proposed ruling | Confidence | What closes it |
|---|---|---|---|---|---|---|
| RT-237 | tier 1 (the review) | The free model's channel-removal gate requires "the ownership-free state and syntax batteries" to hold; the task has no such batteries, so the gate cannot be evaluated and, by stop condition S8, counts as failed: the free model could never be read | fatal | **PROPOSED: ACCEPT WITH CHANGE.** Replace the clause with the ownership-free part of the act, with a chance line of 1,546 of 3,000, two seeds of three. Amends page 1h of the 2026-09-26 ruling | high that the clause must go; moderate on the replacement over striking it (the check of these dispositions showed it would pass a model that lost which item is named) | The registration text without the battery clause, and the reviewer-owned measured check listed under RT-237 below |
| RT-238 | tier 1 | The whole-state floor as printed admits every site set, with a divisor of zero or below, on a model at chance; only an unwritten clause of the code refuses it | serious | **PROPOSED: ACCEPT.** Write the code's clause (the requirement must be above zero) into section 6.4 item 1 and the section 9 row | high | The text change, and the review's floor-from-text check re-run with the clause, giving 0 of 45 site sets on the competing solver, as the code does |
| RT-239 | tier 1 | The registration describes the grammar as an extension of the closed design's, which shows the model its own name three tokens before it acts; the two departures that remove that cue are written nowhere in it | serious | **PROPOSED: ACCEPT WITH CHANGE.** Register the episode format in full (the rehearsal's grammar at its sizes), with both departures and the self-tests that assert them; say the closed design's batteries and twelve turns are not carried | high | The text change; a search showing the departures and self-tests named; step 3's self-test run on the built generator |
| RT-240 | tier 1 | The ruled counts (a read fitted on 420 episodes) were rehearsed only at width 160; on a stand-in at the registered width 448 the entangled model's read falls below the floor on two seeds of three | serious | **PROPOSED: ACCEPT WITH CHANGE.** Fit every read on 1,800 development episodes with 180 held out; the transplant passes stay on 600 pairs. Toy re-run under it before registration. New weakness stating the stand-in's limits. Amends ruling 4 of 2026-10-03, late evening | moderate | The toy re-run and its check; the text change |
| RT-241 | tier 1 | The outcome map has holes: no verdict on the separable model maps to nothing; the two-model fallback has no term; "R3 for that arm"; a failed channel-removal check; who gets the one re-run | serious | **PROPOSED: ACCEPT WITH CHANGE.** One outcome table in section 3, frozen in section 7.4, with three new registered terms, arm M's gate failure dropping arm M, and a stated rule for the one re-run | moderate; low on the exact words of the new terms, which are John's | The table in the text, and a check that every arm-level state the review lists maps to exactly one term |
| RT-242 | tier 1 | "The three candidates reach 0.733, 0.383 and 0.478" quotes one candidate's three seeds | worth-noting | **PROPOSED: ACCEPT** as the review words the fix | high | The text change (figures reproduce, C6) |
| RT-243 | tier 1 | "On the toy [the two forms of the floor] never did [disagree]" holds for the own-directed grids only; they disagree on 576, 892 and 1,080 rows elsewhere, always with the plain form passing where the registered form refuses, almost always on a model near chance | worth-noting | **PROPOSED: ACCEPT.** Narrow the sentence and cite the disagreements as the reason the corrected form is registered | high | The text change (figures reproduce, C6) |
| RT-244 | tier 1 | The sentence John ruled in on 2026-10-04 says the solver's untouched rate "missed the no-transplant rule by 0.11 or more"; it missed the formula by 0.109 or more and the allowance by 0.091 or more | worth-noting | **PROPOSED: ACCEPT WITH CHANGE.** Correct the figure; its first clause becomes true once RT-238 is accepted. Amends the wording of ruling 2 of 2026-10-04 | high | The text change (figures reproduce, C6) |
| RT-245 | tier 1 | Running the registered nomination on the laptop is argued, not measured; the device ruling covers the read's fit, not the transplant passes that choose the site set | worth-noting | **PROPOSED: ACCEPT WITH CHANGE.** Cite the review's timing (about two hours per model, about 25 hours for twelve, $0) in place of the argument; name the processor and number format for the whole nomination and reading | high | The text change |
| RT-246 | tier 1 | The weakness ruled on 2026-10-04 says the toy has no model doing the task "by another route"; the free model is one, and the measure returns no verdict on it | worth-noting | **PROPOSED: ACCEPT WITH CHANGE.** Write the weakness with both halves: the route the toy has seen, and the one it has not | high | The text change |

---

## Each finding: the proposed text and the reason

Quoted replacements are what the writer of the registration text (version 5)
would put in. Square brackets mark what that writer fills in (a commit, the
date of John's ruling). Section and line numbers are version 4's.

### RT-237 (fatal): the battery clause in the free model's gate

**PROPOSED: ACCEPT WITH CHANGE.**

**Text change 1, section 8.2, the last bullet (line 2223).** Replace

> - the ownership-free state and syntax batteries **must hold**.

with

> - **the part of the act that needs no ownership must hold** (replacing,
>   by John's ruling of [date], the clause "the ownership-free state and
>   syntax batteries must hold", which was written for the closed design's
>   end-of-episode question sets; the successor's task has none: the inside
>   review of version 4, RT-237). With the acting channel zeroed, the model's
>   own-directed answer must still be the successor of one of the four
>   agents' earlier values on the item named — the four answers that remain
>   open once "which agent am I" is taken away — on **1,546 or more of the
>   3,000 held-out gate episodes**, on at least two seeds of three, the third
>   reported. 1,546 is the smallest count above one half at the 0.05 level,
>   one-sided, by the exact binomial tail; one half is what a model guessing
>   among the eight value words reaches. The count is written to the gate's
>   output file beside the lesioned accuracy, as the field the clause is
>   evaluated on. The same count on the named-other condition is reported
>   and not gated.

**Text change 2, section 8.2, the paragraph "On the toy, described
honestly", added at its end:**

> With the channel zeroed, arm F's own-directed answer is one of the four
> candidate values on 2,100, 2,238 and 2,324 of 3,000, against 1,546; arms
> T, C and M and the ordinary competing solver clear the line on every seed;
> three models of arm F's architecture with untrained weights reach 0, 620
> and 726 and do not (MEASURED, a rehearsal record and not a result:
> `docs/2026-10-04-gate-a-v4-dispositions-measurements.md` at [commit],
> part A, from `out-lesion-content-check/lesion_content_check.json`; checked
> at [commit of the check]). So the check refuses a model that answers with
> noise and passes every trained toy model by 554 episodes or more. It shows
> that the model still answers with the successor of a value it was shown;
> it does **not** show that the model still uses the right item: a model
> that had lost which item the action names, and answered the successor of
> any of the eight values shown, would score about 2,257 of 3,000 and pass
> (the check of these dispositions, pull request 96, section 6).

**Text change 3, the section 9 row "Ownership-lesion collapse threshold"
(line 2270).** Replace "the ownership-free batteries must hold" with "with
the channel zeroed, the own-directed answer is one of the four candidate
values on **1,546 or more of 3,000** gate episodes, on two seeds of three";
add to its "Ruled in" column "John's ruling of [date] on RT-237, amending
page 1h".

**Text change 4, section 7.4 (line 2064).** Replace "and the
ownership-lesion rule with its two-of-three clause" with "and the
channel-removal rule: its collapse line and its ownership-free line (1,546 of
3,000), each with its two-of-three clause".

**Text change 5, section 8.2, after the bullets, and the gate code named in
section 11, step 3** (placed where a builder of the gate looks, not under
section 6.4's reading controls), one sentence added: "The gate's code writes, for every arm and seed, the
lesioned own-directed count and the lesioned candidate count, so that every
clause of every gate is evaluated on a named field."

**Reason.** The review is right and the finding is fatal as filed: the
clause names something the successor's task does not contain, sets no line,
and was never exercised, and the design's own stop condition S8 turns a gate
that cannot be evaluated into a failed one, so "metric validated, degree
read" could not be reached by any result. Striking the clause would close
the finding, but it would drop what John's page 1h ruling asked for: that
the channel removal be shown to take away the ownership answer and not the
model's whole grip on the episode, which is what makes a collapse to one in
four mean something. The successor's task has an exact counterpart. A model
that has lost only "which agent am I" still picks among the four agents'
values on the right item, and the one-in-four collapse level the gate
already uses assumes exactly that. Measured today at $0 on every committed
toy model, the counterpart can be evaluated on a field every gate run can
record, its line comes from chance and not from any toy figure, it refuses a
model that answers with noise (untrained weights reach at most 726 against
1,546) and it passes every trained model, the free one by 554 episodes or
more. So it adds no realistic new way for the free model to go unread, and it is rehearsed,
which is the reason a second collapse line was not taken on 2026-09-26 (the
Gate C rulings, RT-220). **What it does not do, found by the check of these
dispositions (section 6):** it cannot tell whether the lesion broke the step
"find the item the action names". A model that lost the item and answered the
successor of any value shown would score about 2,257, above the line and above
the free model's lowest seed (2,100), and the line cannot be raised to catch
it without failing arm F on two seeds and arm C on all three. So the check is
weaker than "the model kept its grip on the episode": it shows only that the
model still answers the successor of a value it was shown, and the
registered sentence should say exactly that. **Strongest alternative,
closer than it first looked for that reason:** strike the clause, with its
reason on the record. That is simpler and is a valid ruling; its cost is
that a channel removal that left the model answering at random would count
as a collapse.
**A second alternative:** keep the new count as a reported figure with no
line. Weaker than either, because page 1h made the clause a condition.

**The measured check another session must run on the repair** (the closure
rule makes it the tier 1 reviewer's, not the author's: `docs/outside-review-protocol.md`,
"The closure rule"). On the registration text once written:

1. **Every clause of the channel-removal gate has a field.** For each clause
   of section 8.2 (the collapse line, its two-of-three clause, the
   named-other report, the ownership-free line and its two-of-three clause),
   name the field of a committed rehearsal output file that evaluates it and
   print the field's values for arm F's three seeds. A clause with no field
   leaves the finding open. **The test is for a condition, not a word:** no
   sentence in sections 0 to 16 sets a condition on any battery, question set
   or other quantity the successor's task does not produce. A word search is
   only a way to find candidates: on the proposed text `grep -n -i "batter"`
   over sections 0 to 16 finds six lines (the check of these dispositions,
   section 1.2), namely the sentence recording the replacement (section 8.2),
   the sentence saying the closed design's batteries are not carried
   (section 4.1), three passages describing the closed design's record
   (sections 1 and 3) and the phrase "the control battery" (section 7.3), and
   none of them sets a condition. Each hit is read and classified; a hit that
   sets a condition leaves the finding open. (This is the test the review
   proposed for the known-failure list, run on this gate.)
2. **The figures recompute from independent code.** Without importing
   `lesion_content_check.py`, compute the candidate count with the channel
   zeroed on the fifteen committed trained models (arms T, C, M, F and the
   competing solver, `out-repairs/models/`, checked against `SHA256SUMS`) and
   on three untrained models, on the 3,000 gate episodes (1,500 development
   pairs, generator seed 99). Every count must equal part A's
   (`out-lesion-content-check/lesion_content_check.json`), and the line must
   come out at 1,546 from the exact binomial tail. This would come out wrong
   if the clause were mis-stated, the episodes differed, or the line were
   typed rather than computed.
3. **Both ends.** Every trained model passes and the untrained ones fail, on
   the recomputed figures.
4. **Owed later, and named so it is not lost:** when the registered gate code
   is written (section 11, step 3), its output file carries the two fields
   of text change 5.

### RT-238 (serious): the whole-state floor as printed lets a model at chance through

**PROPOSED: ACCEPT.**

**Text change, section 6.4, item 1 (lines 1113 to 1132).** After the
formula, insert:

> **and the requirement on the right must be above zero.** Where the arm's
> own-directed accuracy is not above its no-transplant rate on the same
> episodes, the floor is not defined, no site set is usable, and the arm
> returns "no verdict: no site set clears the whole-state floor". This is the
> code's clause (`need > 0` in `repairs.floor_check`, which every toy run
> used), and the registered code carries it (the inside review of version 4,
> RT-238).

and replace "The floor keeps the denominator away from zero by construction:
on an arm that has learned the task, `own_directed_accuracy −
accuracy_untouched` is large, and the denominator is at least four fifths of
it." with

> The floor keeps the denominator away from zero by construction only with
> that clause. Without it, a model at chance meets the inequality at every
> site set with a divisor of zero or below: the ordinary competing solver
> does so on four of its six runs (MEASURED: the inside review, RT-238,
> `rule_from_text.out.txt`, section 4). With it, the denominator is at least
> four fifths of a requirement that is above zero; on an arm that has learned
> the task that requirement is large.

**And the section 9 row "Whole-state floor"**: after "four fifths of the
arm's own own-directed accuracy, on the chance-corrected scale", add "**with
the requirement above zero; where it is not, no site set is usable**".

**Reason.** The registered code is written from the registration text, and
the text's own claim that the floor keeps the divisor off zero "by
construction" is false without a clause that today lives only in code. The
first known failure on this programme's list is exactly a registered
comparison whose divisor was zero. The fix is one sentence, changes no toy
verdict (on all twelve arm models the requirement is well above zero; on the
competing solver both forms already return no verdict), and makes the
sentence John ruled in on 2026-10-04 ("no site set cleared the floor at
nomination") true of the text as well as the code. No alternative is worth
taking.

### RT-239 (serious): the grammar that keeps the model's own name out of the act is not registered

**PROPOSED: ACCEPT WITH CHANGE.**

**Text change, section 4.1, its first paragraph (lines 498 to 504).**
Replace "The grammar extends the registered Amendment A3 grammar ... The
rehearsal's shrunken version of it is
`experiments/rehearsal-successor-measure/src/grammar.py`." with

> **The episode format, registered in full (the inside review of version 4,
> RT-239).** The registered generator is the rehearsal's grammar,
> `experiments/rehearsal-successor-measure/src/grammar.py`, at its sizes. It
> is **not** an extension of the closed design's generator
> (`curriculum_a3.py`), which has twelve turns, four revision turns and the
> end-of-episode question sets the closed design called batteries; none of
> those is carried. One episode has four agents, two items, eight value
> slots and a closed vocabulary (twelve marker words and five items in the
> training, development and fresh pools; 56 tokens). **Eight assignment
> turns**, one per agent and item, in random order, rendered
> `<marker> assign <item> <value>`; within an item the four values are
> distinct, except in the collision set for control 6, where two agents
> share a value on one item (section 4.2). **Two action turns**, last, in random order, rendered
> `<act> revise <who> <item> <ans> <mask>`: on the own-directed action
> `<who>` is the special word meaning "your own", and on the named-other
> action it is the named agent's marker word. The correct answer is the
> successor of the relevant earlier value, counted round the eight slots.
>
> **Two departures from the closed design's grammar, both deliberate.**
> (1) **The action turn carries no marker word of the model's own.** The
> closed design renders the acting turn with the actor's own marker three
> tokens before the action, and its own header names the consequence: a
> model can read "a name badge at act time rather than" carry a binding.
> Here the only route to the ownership answer is the acting channel
> (section 1). (2) **The answer is never shown**: its slot is the `<mask>`
> word, and the prediction is read there. Together these make the two
> episodes of a matched pair **token-for-token identical**, differing only
> in which positions the acting channel fires on (section 6.1). **The
> registered generator's self-test asserts both**, as the rehearsal's does
> ("matched pairs are token-for-token identical"; "no name badge — the
> own-directed turn shows only the self word"; `grammar.py --self-test`),
> and that self-test runs on the built generator at section 11, step 3.

**Reason.** Read as written, version 4 tells whoever builds the registered
generator to extend the closed design's generator, which shows the model its
own name just before it acts. A free model built from that could clear the
fit floor by copying a name rather than carrying an answer, the twins would
stop being the same text, and the ownership cue the whole design exists to
keep out (ledger item RT-17, the finding that any learnable ownership cue in
the tokens is a fingerprint) would be back, on the one model the experiment
exists to read. The rehearsal grammar already has the right format, says so
in its header, and has self-tests for both properties (C8), so the fix is to
write down what was rehearsed. Stating the sizes matters for the same reason:
no text now fixes the episode length (the review, RT-245). It also settles
the review's doubt under RT-237: the batteries are not carried. **The
choice inside it that is John's:** registering the rehearsal's sizes, which
are the only ones any toy figure was measured at. The alternative, larger
sizes at registered scale, would need its own rehearsal.

### RT-240 (serious): the ruled episode counts were rehearsed only at the toy's width

**PROPOSED: ACCEPT WITH CHANGE.**

**Text change 1, section 7.4, the counts bullet, and the section 9 row "The
numbers of episodes at the registered size".** Replace "600 development
episodes with the last 180 held out for every fit, so the floor is 144 of
180" with

> for every read, **1,980 development episodes: the first 1,800 fitted and
> the last 180 held out, so the floor is still 144 of 180**; the
> nomination's transplant passes on 600 development pairs, as rehearsed

and add to the "Ruled in" column "John's ruling of [date] on RT-240,
amending ruling 4 of 2026-10-03, late evening, for the read's fitting count
only".

**Text change 2, a new weakness in section 13:**

> **The read's fitting count was chosen on a stand-in.** The toy's state is
> 160 wide and the registered model's 448. Fitted on 420 episodes, the read
> held the label on every constructed toy model (arms T, C and M; the free
> model's read failed its floor on every seed, as section 5.4 records); on a
> stand-in at width 448 (the toy states with 288 coordinates of independent
> noise appended) the entangled model's 8-direction piece fell to as low as
> 76 and 126 of 180 on two seeds against 144 (the review's 600 episodes), and
> 74 and 129 on a larger pool with a fixed held-out set (part B). Fitting on 1,800 episodes brought every seed back above the
> floor on every noise draw (smallest 156); 900 episodes and stronger
> regularisation did not (MEASURED on a stand-in, NOT A RESULT: the inside
> review of version 4, RT-240, `width_vs_count.out.txt`;
> `docs/2026-10-04-gate-a-v4-dispositions-measurements.md` at [commit],
> part B). A wider model's extra coordinates carry structured content, not
> noise, so this is not a forecast, and 1,800 is the smallest of three sizes
> tried that held, not a size derived from anything. The read at the
> registered width is first seen on arm F at step 5a and on arm C at step 5b.

**Work owed before registration:** the nomination and reading of the twelve
toy models and the competing solver, re-run with every read fitted on 1,800
episodes, method committed before output, at $0, by a session other than
this one, and checked. It is needed because the piece's directions come from
the read, so a refit can move which site set and size are chosen, not only
the counts.

**Reason.** The review's stand-in reproduces exactly (C9), and on it the
problem is plainly too few fitting episodes for the number of coordinates:
the entangled model's piece goes from 74 at 420 to 120 at 900 to 156 at
1,800 on the seed that fails worst, while making the read's penalty ten or a
hundred times stronger leaves it at 78 and 85. At the toy's width, fitting
on more episodes changes no verdict (the free model's best piece is 41 at
most against 144), so the change does not quietly help the model the floor
exists for. The cost at registered scale is small: capturing states for
1,980 episodes is a few more seconds of forward passes than 600, and the
transplant passes, which are the expensive part (the review, RT-245), are
unchanged. The arm at risk is the high anchor, whose failure is first seen
after both releases of money are drawn, which is the expensive place to
learn it. **What this does not settle:** what a trained 448-wide model does.
**Strongest alternative:** keep the ruled counts and carry the risk as a
named weakness; no re-run, but the stand-in says the high anchor could miss
its floor, which fires the two-model fallback. **Another:** train a stand-in
at width 448 on the laptop and rehearse the read on it before registration.
That is the measurement that would actually settle the question; it is $0
but has not been timed, and it would be a new training run needing its own
go. It can be added to, not substituted for, the recommendation.

### RT-241 (serious): the outcome map has holes

**PROPOSED: ACCEPT WITH CHANGE.** One table, replacing the three-item list
"What a no verdict maps to" in section 3 (lines 456 to 467), frozen by name
in section 7.4 (line 2061), and repeated in the section 9 row "What a no
verdict maps to".

**Text change 1, section 3, the new table and its two rules:**

> **Every state the registered runs can reach, and its registered term
> (ruled 2026-10-03, page 11, closing the no-verdict finding RT-182 of the
> review of version 1, for arms C, M and F; completed for every arm by the
> inside review of version 4, RT-241, ruled [date]).** An arm *reads*
> if two or more of its seeds read; it returns *no verdict* if two or more
> seeds do. Rules are applied in this order.
>
> 1. **The gate on learning comes first.** If arm T, C or F fails its gate
>    (section 8.1), after the experiment's one permitted re-run where it is
>    still available (rule 3 below), the outcome is **R3, "substrate not a
>    testbed"**, naming the arm and the condition, whatever else happened.
>    **Arm M is the exception:** if it fails its gate it is dropped and
>    carried as an extension, exactly as a no verdict on it is.
> 2. **Otherwise, the readings decide:**
>
> | Arm T | Arm C | Arms T and C separate (section 9)? | Arm F | Registered term | Satisfactory |
> |---|---|---|---|---|---|
> | reads | reads | yes | reads | **R1, "metric validated, degree read"** | Yes |
> | reads | reads | yes | no verdict, or fails the channel-removal check of section 8.2 | **"metric validated, degree not read"**, with the reason after a colon | Yes, stated as weaker than R1 |
> | reads | reads | no | (not read) | **R2, "metric does not separate"** | Yes |
> | reads | no verdict (the two-model fallback) | (cannot be asked) | reads | **"metric checked against the separable model only, degree read"** (new) | Yes, stated as weaker than R1 |
> | reads | no verdict (the two-model fallback) | (cannot be asked) | no verdict, or fails the channel-removal check | **"metric checked against the separable model only, degree not read"** (new), with the reason after a colon | Yes, stated as weaker than the line above |
> | no verdict | any | (cannot be asked) | (not read) | **"metric not validated"** (new), with the reason after a colon | No: the measure did not return a reading on the model built to be easiest to read |
>
> Arm M never changes the term. It is reported against its band if it
> reads; if it returns no verdict or fails its gate it is dropped, said by
> name, and carried as an extension. R4 is unchanged.

**Text change 2, section 8.1 (line 2188).** Replace "An arm that fails,
after the one permitted re-run, gives outcome R3 for that arm, and the
registration says which arm and on which condition." with

> An arm that fails, after the experiment's one permitted re-run where it is
> still available, gives outcome R3 for the experiment (arm M excepted: it is
> dropped), and the report says which arm and on which condition (section 3,
> rule 1).

**Text change 3, rule 3 of the same section 3 block, the one re-run:**

> 3. **The experiment has one permitted re-run** (item 19 of the 2026-09-21
>    ruling), held in the first release. It goes to the first registered run
>    that fails its gate on learning: to arm F at step 5a if it fails there;
>    if step 5a does not use it, it is held for step 5b and goes to the first
>    run of arms T, C or M that fails, on John's go naming it. Once used, a
>    later gate failure gives its outcome under rule 1 with no re-run.

**Text change 4, section 5.2 (lines 820 to 827).** Replace "The registration
text, if the fallback fires, says that in those words, and the R1 sentence is
correspondingly weaker." with "If the fallback fires, the outcome is one of
the two terms section 3 registers for it, 'metric checked against the
separable model only', and arm F's figure has no upper reference."

**Reason.** Each hole is a state the registered runs can reach, and line 305
forbids reporting an outcome in words that are not registered, so a hole
there is a result with no name. The ruling that created the fifth term
closed the same kind of hole for three arms and not the fourth; this closes
the rest in one table. The calls inside it, each John's:

- **No verdict on the separable model** is not R2 (nothing was compared) or
  R3 (no gate failed). Arm T reads exactly zero by construction on every toy
  seed, so a no verdict there means a control that holds failed, the pairing
  broke, or its floor was missed: a failure of the measure on its easiest
  case. "Metric not validated", with its reason, says that and claims
  nothing about the substrate.
- **The two-model fallback** was accepted in advance on 2026-09-20 "with the
  metric's validation resting on T alone, which is weaker and is said to be
  weaker" (the December-result roadmap, section 3). The two new terms say
  what was done in plain words, and keep the fifth term's pattern for an
  unread arm F.
- **A failed channel-removal check on arm F** maps to the same place as a no
  verdict on arm F, not to R3: it says the free model is not fit to be read,
  not that the recipe failed to learn, which is what R3 means (section 3).
- **Arm M's gate failure drops arm M** rather than making the whole
  experiment R3, because its no verdict already only drops it; it would be
  odd for one of arm M's failures to sink the experiment and the other not.
  This narrows R3's "one or more arms" to arms T, C and F, which is a change
  to a registered term and needs John's words.
- **The one re-run** is singular in the ruling that funded it, and the
  second release as ruled holds no re-run money (C10). Saying which run gets
  it, and that a built arm at step 5b can have it only if step 5a did not
  use it, is the only reading the money supports.

**Strongest alternative:** register only the two lines the review calls
reachable on the existing path (the fallback's terms and no verdict on arm
T) and leave the rest as reporting practice. Fewer new terms, but the
remaining holes stay holes.

### RT-242 (worth-noting): one candidate's three seeds quoted as three candidates

**PROPOSED: ACCEPT.** Section 7.2, item 1 (lines 1387 to 1388): replace
"anchored at the action position the three candidates reach 0.733, 0.383 and
0.478" with "anchored at the action position, candidate 1 reaches 0.733,
0.383 and 0.478 on seeds 0, 1 and 2, and candidates 2 and 3 at most 0.417 and
0.633".

**Reason.** The review's reading of the findings table is right, and its
script reproduces (C6). Nothing ruled rests on the sentence, and every figure
stays under 0.80 either way; a figure quoted as something it is not should
still be fixed before it is registered.

### RT-243 (worth-noting): the two forms of the floor do disagree on the toy

**PROPOSED: ACCEPT.** Section 6.4, item 1 (lines 1121 to 1125): replace "so
a reader can see whether the two readings of the ruled sentence ever
disagree; on the toy they never did (MEASURED: 0 disagreements across all
site sets, arms and seeds, the repairs findings at `882f252`, section 3; ...)"
with

> so a reader can see where the two readings of the ruled sentence
> disagree. On the own-directed grids of the twelve toy models they never do
> (MEASURED: the repairs findings at `882f252`, section 3; the re-run records
> both forms on every row,
> `experiments/rehearsal-successor-measure/out-v3-rules/measure_*_seed*.json`,
> `reading.floor`). Elsewhere on the toy they do, always in the same
> direction, the plain form passing where the registered form refuses: on
> 576 rows of the repairs run's other-agent grids, 892 rows of the grammar
> attempt's grids and all 1,080 rows of the competing solver's (MEASURED: the
> inside review of version 4, RT-243, `floor_forms.out.txt`). Almost all are
> on models near chance; five are on the grammar attempt's free model with
> its own-directed condition learned, missed by 0.011 or less (the check of
> these dispositions, section 3.2, defect 3). That is the
> reason the chance-corrected form is the one registered.

**Reason.** The counts reproduce (C6). The narrowed sentence is true, and the
disagreements it now reports are the best evidence for the choice the design
already made.

### RT-244 (worth-noting): a figure in the sentence John ruled in on 2026-10-04

**PROPOSED: ACCEPT WITH CHANGE.** The sentence of ruling 2 of
`docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md` is written
into the registration text as:

> On the toy, the ordinary competing solver returned no verdict because no
> site set cleared the floor at nomination; behind that, its best piece
> missed the piece rule by 119 or more of 180, its untouched rate was 0.109
> or more above the no-transplant formula and 0.091 or more outside the
> rule's allowance, and it would have failed the gate on learning had it been
> gated as the free model is. For a model near chance the floor's
> requirement is close to zero or below it and is decided by one or two
> episodes; where it is not above zero, no site set is usable (section 6.4,
> item 1).

**Reason.** The figures reproduce (C6): misses of 0.1091 to 0.1393 against
the formula and 0.0911 to 0.1213 beyond the allowance, so "0.11 or more" is
true on neither reading. The last sentence is changed only so that it agrees
with RT-238's clause: on two of the solver's three seeds the requirement is
at or below zero. Because this changes the words of a sentence John adopted,
his ruling should say so.

### RT-245 (worth-noting): the registered nomination on the laptop, timed; the device for the whole nomination

**PROPOSED: ACCEPT WITH CHANGE.**

**Text change 1, section 11, step 5a (lines 2520 to 2524).** Replace "(ARGUED:
a 30-million-parameter model's activations on development episodes fit on the
laptop; if that turns out not to be so, the cost goes into the first
release's rehearsal line and is said)" with

> (MEASURED at the registered shape on the laptop's processor: one
> transplant pass over the 600 development pairs takes 4.59 seconds, so one
> model's nomination takes about two hours and the twelve registered models'
> about 25 hours, at $0; the inside review of version 4, RT-245,
> `registered_shape_timing.out.txt`, timed on 56-token episodes. If it proves
> impractical at full size, that is a fresh question for John, not a switch
> of device: record B of 2026-10-03, ruling 3.)

**Text change 2, section 7.2, item 1, the device paragraph (line 1333) and the
section 9 device row.** Replace "the registered fit is computed on the
laptop's **processor**" with "**the whole nomination and reading — every
forward pass, every transplant pass that chooses the site set, and every
fit — is computed on the laptop's processor**", and add one sentence: "The
choice of site set can turn on one episode in 600 (arm C, seed 1, on the
toy), and a transplant pass can move by an episode between devices as a fit
can."

**Reason.** The timing makes an argument into a measurement and shows it
holds. The device point is the review's and is sound: the ruling named the
device for the number that decides the floor and not for the passes that
decide the site set, and on the toy the site set was once decided by a
single episode. The cost is nothing; every toy figure already came from the
processor.

### RT-246 (worth-noting): the competing-solver weakness, stated exactly

**PROPOSED: ACCEPT WITH CHANGE.** The weakness ruled on 2026-10-04 (ruling 7)
is written into section 13 as:

> **The toy's competing solvers do not test the measure on a model that
> solves the task another way and still looks readable.** The ordinary
> competing solver fails the task, so its "no verdict" shows only that the
> measure returns nothing on a model that has not learned the task. The toy
> does have one model that does the task by a route other than carrying the
> registered label: the free model, which solves the own-directed condition
> from the value tokens on the turns its channel marked, without carrying its
> marker word to where it acts (section 5.4). On it the measure returns "no
> verdict, read failed its floor" and says why. What the toy has no case of
> is a model that does the task by another route and still leaves the label
> readable where it acts. The obvious such route, reading its own name off
> the text near the action, is closed by the grammar (section 4.1), not
> tested by a control.

**Reason.** The ruled weakness is true and incomplete: a reader would
conclude the toy has no other-route model at all, when the free model is
one. The two-part version says which other route has been seen and which
has not, and ties the unseen one to RT-239.

---

## What closes each finding, and who checks it

Under the closure rule (`docs/outside-review-protocol.md`, "The closure
rule"), "adopted" is a disposition, not a closure.

- **RT-237, fatal.** Closed by: the registration text with the replacement
  clause, at a named commit, and the four-part measured check above, run by
  a session other than the one that writes the text and other than this one;
  the protocol gives it to the tier 1 reviewer of this Gate A. The ledger
  line then says the claim was checked, names the reviewer and the check.
- **RT-238 to RT-241, serious.** Closed the same way, or carried as open
  items named in the registration text with John's ruling and reason. Each
  has a check named in the one-line table. RT-240 also needs the toy re-run
  and its check before registration.
- **RT-242 to RT-246, worth-noting.** Closed by the text change; the checking
  session confirms each replacement sentence against the record it cites.
- **This file and the two measurements** are checked first, under the
  pairing rule, by a session that did not write them.

## Tally

Ten findings: one fatal, four serious, five worth-noting. Proposed: **accept**
3 (RT-238, RT-242, RT-243); **accept with change** 7 (RT-237, RT-239,
RT-240, RT-241, RT-244, RT-245, RT-246); **reject** 0. Six of the seven
"with change" lines change something John ruled or adopted (RT-237 page 1h of
2026-09-26; RT-240 the episode counts of 2026-10-03; RT-241 the registered
outcome terms; RT-244 the wording of ruling 2 of 2026-10-04; RT-245 the
device ruling's reach; RT-246 the wording of ruling 7 of 2026-10-04), so each
needs his words, not only his agreement.

## What this session did not do

It did not rule, edit version 4, the review, the ledger, any ruling file,
the protocol or the known-failure list, or write version 5. It did not run
the toy re-run RT-240 asks for, or train a model at width 448. It did not
open the outside reviewers' packet, and no outside response exists yet. It did not check its own work; that is owed.
