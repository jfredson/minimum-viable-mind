# Gate A tier 1 review (the inside pass) of the two-sided question text, with the failure-mode pass — RT-283 to RT-295

*Filed 2026-10-09 (Pacific) by a Claude Code session acting as the Gate A
tier 1 reviewer, on branch `gate-a-two-sided-2026-10-09`, cut from the main
line at `d60ff2e` (the merge of pull request 158, the change that made the
registration text of experiment C ready for its commit). The text under
review is section 2 of the refounding proposal, version 2
(`docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md`, lines 99 to 199
at `d60ff2e`, SHA-256 of the extracted section
`6cbfdc08713e3984f348799a8dfc566a595f948246e9259ec3339c95a9746307`): the new
spec section "The Question This Project Measures: Two Sides", the sentence it
adds to the spec's "The Floor", and the paragraph it adds to "What Would
Count Against It". Section 2 lives only in the proposal on the main line; it
has not been written into `spec/minimum-viable-mind-proposal-v0.1.md`, on
the main line or on any branch, and this pass does not write it in.*

*Why this pass, and why now. Decision 1 of the two-sided question rulings
(`docs/rulings/2026-10-07-two-sided-question-rulings.md`) says the spec text
of section 2 "goes through Gate A, both tiers, with the failure-mode pass,
before it is committed into" the spec. Item 13 of the weekend task list
(TimeAssembler repository, `docs/weekend-2026-10-09-task-list.md`) asks for
that pass after the felt-features table and filtered battery reached their
version 4 (pull request 164, branch `felt-features-table-2026-10-09` at
`3eee588`).*

*Filed under `docs/reviews/`, beside the Gate C tier 1 pass on the same
proposal (`docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md`),
because the text changes the spec, which no single experiment owns. That is
the filing the Gate C pass used and explained; the protocol's fallback
(`docs/outside-review-protocol.md`, "The pairing rule") would put a pointer
under `experiments/06-mvm-0a-constructed-self-index/reviews/` if John wants
one.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run, and the command and its output are below or
in the scripts folder beside this file) or **ARGUED** (reasoning a reader can
dispute), and carries a severity: **fatal**, **serious** or **worth-noting**.
Findings continue the red-team ledger's numbering. The ledger
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`) ends at
RT-282 on the main line and on the four open branches of 2026-10-09 that
carry it (checked with `git show <branch>:<ledger> | grep -oE '^\| RT-[0-9]+'`
on `origin/main`, `felt-features-table-2026-10-09`,
`registration-commit-2026-10-09` and `relabel-experiment-a-2026-10-09`; all
four return 282). No ledger row is written here: rows carry John's ruling,
and are written when he rules, which is what the last two Gate A passes did
(the version 4 pass and the version 5 failure-mode pass, both under
`experiments/06-mvm-0a-constructed-self-index/reviews/`).*

**Nothing was rented, trained or spent by this tier: $0.** Laptop only. No
model was called for tier 1. The proposal, the spec, the founding-wager
proposal, the battery draft, the ledger, the known-failure list, the protocol,
`STATUS.md`, version 5 of experiment C's registration text and experiment C's
frozen code were not edited.

**How isolated this session was.** A fresh session in its own git worktree.
It has no chat history of the session that wrote the proposal (versions 1
and 2), of the Gate C pass, of the poll, or of the battery draft's writers
and checkers, and it wrote none of them. It was commissioned by the weekend's
coordinating session, whose message named the item and the protocol to
follow and nothing about what to find; that message is the only chat this
session has seen.

---

## Verdict in one paragraph

**Not ready to be written into the spec. One fatal finding, seven serious,
five worth-noting.** The fatal one is fatal by the protocol's own rule and is
closed by a deletion: the observer-side paragraph still pre-states a loss
condition ("track the fluency measures no better than chance") for which no
instrument and no rehearsal exist, describing as an open option what John
has since ruled (ruling 10, 2026-10-07: the observer side does not run early;
it returns later as a design question, not a run) (**RT-283**). The serious
ones are mostly about fit. Written into the spec as it stands, section 2 would
sit beside unchanged sentences that say the opposite: two definitions of
"minimum viable", five places that use the removal test as the instrument or
pass-fail rule, against two new sentences calling it "a definition, not an
instrument" (**RT-284**, the decisive check below). The paragraph for "What
Would Count Against It" is described but not written, and the new question
states no way to lose in the spec itself (**RT-285**). "Passes the battery",
"smallest" and "degree" have no definition in the battery draft that the text
leans on (**RT-286**, **RT-289**), and section 2's rule for what discriminates
leaves out the battery's own second rule, which carries the corroborated
report (**RT-287**). "Cannot be produced by a cheaper route" claims more than
a twin built without one named route can show (**RT-288**). Section 2's first
sentence presupposes the founding wager, which has not passed Gate A, and the
wager's text still carries a sentence the 2026-10-07 relabelling of
experiment A retracts (**RT-290**). None of the serious findings is a flaw in
the turn the project made; each is a sentence that has to change, or a choice
John has to make, before the text binds.

---

## What this session opened, and what it did not

**Opened, in this order:** the workspace rules (`~/Code/CLAUDE.md`); this
repository's `CLAUDE.md`; the top of `STATUS.md` (the 2026-10-08 late-night
entry, and the 2026-10-07 entry's heading and spend line); the outside-review
protocol in full; the rulings file of 2026-10-07 in full; the proposal,
version 2, in full; the spec in full; the founding-wager proposal in full;
the Gate C tier 1 pass's head, its "what was opened" section and its section
4 (its failure-mode run on section 2 of version 1); the known-failure list's
preamble and the test of each of its six entries; the battery draft, version
4, at `3eee588` (sections 0, 1 and 4 read; the rest searched, by the commands
in check C7 and FMP-2 below); experiment 1's registered findings
(`experiments/01-self-indexing-removal-test/removal-test-findings.md`) and its
interval file (`removal_ci.json`); the opening of the router-control check
(`docs/outside-perspective/2026-10-07-router-control-check.md`); the book's
argument summary at
`/Users/john/Code/calibration-problem/editorial/argument-summary-2026-10-07.md`
(chapters 4 to 6, chapter 15's thresholds, appendix A), checksum confirmed;
for the form of a Gate A filing, the heads of the version 4 Gate A tier 1 pass
and of the version 5 failure-mode pass, and the version 4 tier 2 packet's
front matter and the heads of its two filed replies; the poll's method file
and `docs/outside-perspective/run_poll.py`, for how outside models have been
called by API here before.

**Not opened:** any chat transcript of any session; the proposal's version
1 beyond what the Gate C pass quotes; the poll's replies and synthesis; the
battery draft's three checks; the book manuscript; experiment 1's stimuli or
code; the TimeAssembler record beyond the weekend task list. Nothing was
re-run that touches a model, a vendor or a machine.

---

## The measurement rehearsal, and why this pass opened anyway

The protocol says no Gate A pass opens until the measurement rehearsal for
its target is committed. **None exists for section 2** (check C10: of the
committed files with "rehears" in their name, the only two that touch the
new question are the battery's template check for its entry 1,
`docs/filtered-battery-2026-10-07/summary_leak_rehearsal.py` and its output,
which rehearse the battery and not section 2).

This pass opened because section 2, read line by line, pre-states almost no
quantity of its own. Its first side defers every measurement to the battery
and to the construction line's registrations, each of which owes its own
rehearsal before its own Gate A. The one quantity section 2 does pre-state is
the observer side's loss condition, and that is finding RT-283: it is the
rehearsal rule firing, and it closes by deletion. If John reads section 2 as
pre-stating more than that (for example, "smallest" as a measured size, see
RT-286), the rule says this pass should not have opened, and the right
response is a rehearsal of whatever he reads it as pre-stating.

---

## Findings at a glance

| RT | Severity | Label | Part of the brief | Finding, in one line |
|---|---|---|---|---|
| RT-283 | fatal | MEASURED | 1 Feasibility | The observer loss condition is a pre-stated threshold with no instrument and no rehearsal, describing an option ruling 10 has already closed |
| RT-284 | serious | MEASURED | 4 Over-reading | Written into the spec, section 2 contradicts unchanged sentences about what "minimum viable" names and what the removal test is |
| RT-285 | serious | MEASURED | 3 No verdict | The "What Would Count Against It" paragraph is not written, and the new question has no loss condition in the spec |
| RT-286 | serious | MEASURED, ARGUED | 1 Feasibility, 3 No verdict | "Passes the battery" and "smallest" have no definition in the battery; a size threshold collides with the battery's own capacity loss condition |
| RT-287 | serious | MEASURED | 2 Wrong thing | Section 2's rule for what discriminates leaves out the battery's second rule, which carries the corroborated report |
| RT-288 | serious | ARGUED | 2 Wrong thing, 4 Over-reading | "Cannot be produced by a cheaper route" claims more than a twin built without one named route can show |
| RT-289 | serious | MEASURED | 1 Feasibility, 4 Over-reading | "Degree measured" and "placed on the axes at a degree": no instrument named anywhere yields a degree |
| RT-290 | serious | MEASURED | 1 Feasibility | Section 2 presupposes the founding wager, which has not passed Gate A and still says experiment 1 "found a router" |
| RT-291 | worth-noting | MEASURED | 4 Over-reading | The list called "the indicators of chapter 6" is not chapter 6's five |
| RT-292 | worth-noting | MEASURED | 4 Over-reading | "Damage spread across every task" overstates experiment 1's record, and the Floor sentence cites only an argued note |
| RT-293 | worth-noting | MEASURED | 4 Over-reading | Proposal bookkeeping (finding numbers, "section 10", "Decision 7") sits inside the text meant for the spec |
| RT-294 | worth-noting | MEASURED, ARGUED | 4 Over-reading | The book is not silent on indispensable bookkeeping; the upstream request should say what it does say |
| RT-295 | worth-noting | ARGUED | Plain language | "Floor" is used in a second sense, and "the identity" is used before it is named |

---

## 1. Feasibility

### RT-283 (fatal, MEASURED). The observer loss condition pre-states a threshold with no instrument and no rehearsal, for an option John has already ruled on

Section 2's "Second side" paragraph (proposal lines 153 to 169) says that
until a conversable constructed system exists, the observer side "could
measure one thing": how observers' detections distribute over frontier
models. It calls that "an option put to John (section 10), not something this
text authorises", and gives it a loss condition: "if their presence ratings,
compared afterwards, track the fluency measures no better than chance, the
premise that detection on frontier models is driven by fluency fails and is
reported as failing."

Three things, each measured:

- **John has ruled on the option.** Check C5 prints ruling 10 of the rulings
  file: "The observer side does not run early against the frontier reference
  profile alone. Not before the battery's first two entries have run; then it
  returns as a design question, not a run." Section 2 still describes it as
  open, pointing at a proposal section whose question has been answered.
- **"The fluency measures" do not exist.** Check C10: "fluency" occurs on no
  line of the battery draft, version 4, and no file defines a fluency
  measure. The battery's row 1 ("fluent, broad, articulate") has the
  separating test "None" and is discarded. So the comparison the loss
  condition names has nothing on one side of it.
- **No rehearsal covers it** (check C10, above).

The protocol: "A pre-stated quantity with no rehearsal line covering it is a
fatal finding on its own." Chance is a pre-stated threshold, and the text is
meant to bind. So this is fatal by the letter of the rule. It is also small:
nothing in the project's science is broken by it, and the closure is to
replace the option and its loss condition with one sentence stating ruling 10
and citing the rulings file.

*Closure check, for the reviewer who runs it:* on the revised text,
`grep -c "no better than" <section 2>` returns 0, `grep -c "fluency
measures"` returns 0, and the rulings file is cited by path where ruling 10
is stated.

### RT-286 (serious, MEASURED for the absence, ARGUED for the collision). "Passes the battery" and "smallest" are not defined anywhere, and a size threshold collides with the battery's capacity loss condition

Section 2 defines the minimum viable mind as "the smallest configuration in
that family that passes the battery", with "smallest" meaning "parameter
count within one construction family, read against anchors built with and
without the route", and says "This is a construction question and it is
decidable within a family."

Check C7 searches the battery draft, version 4, for the terms the definition
leans on:

```
/passes the battery|pass the battery|passing the battery/: 0 line(s) []
/\bsmallest\b/: 0 line(s) []
/parameter count/: 0 line(s) []
/minimum viable/: 0 line(s) []
/10-million and 30-million/: 1 line(s) [773]
```

The battery says when a row fails (it moves to DISCARD), when it is empty of
depth, and when it is withdrawn (its section 4). It never says when a
*system* passes it. So "decidable within a family" has no decision rule to be
decided by. A pass rule could be "clears every KEEP row" or "clears at least
one row on each axis" or something else, and the smallest system changes with
the choice.

The collision is argued. Line 773 of the battery is a registered loss
condition: "The whole battery measures Availability after all if every
entry's reading moves with capacity and not with construction: pre-stated as
the reading differing more between the 10-million and 30-million sizes of one
construction than between the two constructions at one size." A smallest
passing size is, by definition, a size below which the reading changes. At
that threshold the gap between the two constructions is, also by definition,
only just large enough. So the very finding section 2 calls the minimum
viable mind is the shape of result the battery says would mean it was
measuring Availability (how widely a system can broadcast what it knows, the
spec's first axis) all along. The two can coexist only if "smallest" is read
as "the smallest size at which the construction gap clears the row's margin",
and if the capacity loss condition is read at sizes above that. Neither text
says so.

*Closure:* section 2 says that the pass rule and the measure of size are set
in each construction registration and do not exist yet, so "decidable" is a
property the question will have once those exist; and it says how a smallest
passing size is told apart from the battery's capacity loss condition.

### RT-289 (serious, MEASURED). "Degree measured" and "placed on the axes at a degree": nothing named yields a degree

Check C12. Section 2's honest sentence ends "non-zero on the gradient, route
named, degree measured, never a verdict" (line 174), and the described
paragraph for "What Would Count Against It" says a system that passes the
battery "is placed on the axes at a degree" (line 195). The battery draft
contains the word "degree" on two lines, and both are inside the folder name
`experiments/08-successor-degree/`. Its readings are rows kept or discarded
and gaps between constructions, not positions on a scale. The founding wager
(check C9, its lines 17 and 18) says the degree it refers to is read on the
integration axis, "whose metric does not yet exist, so every reading to date
is 'above zero, degree unmeasured'." So the one sentence the project will
quote in public promises a measured degree that no instrument in the record
returns.

*Closure:* say what the battery returns (which rows a construction clears,
at which size, by which route), or name the instrument that returns the
degree and the record that shows it does.

### RT-290 (serious, MEASURED). Section 2 presupposes a text that has not passed Gate A, and that text carries a retracted sentence

Section 2's spec section opens "The founding wager says that sufficiently
deep self-centred integration is experience". Its own instructions say to
insert it after "The Founding Wager: Structure Suffices", and check C1 shows
that heading does not exist in the spec (0 matches). The proposal's section 8
proposes "one Gate A pass covering the founding wager and section 2 in that
order"; this pass covers section 2 alone, as decision 1 of the rulings and
the weekend item ask, so it does not clear the wager.

Check C9 finds two things in the wager's text that bear on whether it can be
committed first:

```
/found a router/: 1
  88: experience arises: Experiment 1 found a router where the method expected a
/Stage 2|degree unmeasured|integration axis/: 2
  17: > axis (Stage 2), whose metric does not yet exist, so every reading to date
  18: > is "above zero, degree unmeasured". One sentence saying so goes into
```

Line 88 says experiment 1 "found a router". Decision 2 of the 2026-10-07
rulings relabelled that result to "the test could not discriminate routing
from a centre; the cheaper account was taken in advance". Lines 17 and 18 are
the wager's own note that one sentence must be added "before this text
reaches Gate A"; searching its text for that sentence finds only the note.

So section 2 cannot be written into the spec on its own without either a
dangling "The founding wager says", or the wager going in unreviewed with a
sentence the project has retracted. This is not a measurement failure, which
is why it is serious and not fatal, but it blocks the commit.

*Closure, John's choice:* (a) the wager goes through its own Gate A first,
with line 88 brought into line with decision 2 and its owed sentence added,
and section 2 is written in after it; or (b) section 2 states the one premise
it needs from the wager in its own words, so it can stand without it.

---

## 2. Satisfied by the wrong thing

### RT-287 (serious, MEASURED). Section 2's rule for what discriminates leaves out the battery's second rule

Check C7 prints both:

```
battery section 0, the second clause: a report read against an internal state that a known intervention set and that the record does not carry
section 2: reading discriminates only where two systems built alike except for the route
```

Section 2 says a reading "discriminates only where two systems built alike
except for the route differ in it". The battery, version 4, section 0, after
its second check, adds a second way a reading can discriminate: "a report
read against an internal state that a known intervention set and that the
record does not carry", which "does not need the system's construction to be
known, only the intervention's; that is why row 4 may run on an open-weights
model ... the project did not build". Row 4 is the corroborated report, which
the spec's "Measuring It" already names as one of its four instruments (the
introspection wedge).

So the two Gate A texts disagree on what counts as a discriminating reading.
If section 2 binds as written, row 4 fails section 2's definition; if the
battery binds, section 2's "only" is false. Whichever is written in second
contradicts the first. It belongs under this part of the brief because the
looser rule is the one a wrong-thing route gets through: a report that tracks
a patched state because the patch wrote the report's own vocabulary is the
battery's own example (its row 4 and finding `FB-10`, the patch finding),
and section 2's narrower rule would never be the place that catches it.

*Closure:* section 2 carries the second clause in the battery's words, or
the battery drops row 4's exception, with John's ruling on which.

### RT-288 (serious, ARGUED). "Cannot be produced by a cheaper route" claims more than the test can show

The first side asks for "the smallest system whose presence in interaction
cannot be produced by a cheaper route", and makes it testable as a reading on
which "two systems built alike except for the route differ". The route list
is open: it ends "and the others the battery lists", and the battery adds
five routes that apply to every row (the operator's prompt, fine-tuning on
interaction logs, the evaluator, contamination once published, sampling
variance read as change; battery section 1). A twin built without route A
shows only that the reading does not need route A. It can still be produced
by route B, which both twins share. The battery's own row test is phrased as
a construction "built with the feature and one built with only the cheaper
route", singular.

So what the test can show is "not produced by the routes subtracted in this
pair, with the others held equal", and what section 2 says it shows is "not
produced by any cheaper route". The second is what a reader of the spec, the
paper or a blog post will take away. A system with none of the structure the
project means could pass a row by a route the row's twin did not subtract.

*Closure:* the question is stated as "cannot be produced by any of the
routes named for that row, each either subtracted or held matched", with the
row's list frozen at its registration, so that a new route found later is a
new finding and not a silent hole.

---

## 3. No verdict

### RT-285 (serious, MEASURED). The paragraph for "What Would Count Against It" is not written, and the new question has no loss condition in the spec

Check C2:

```
Floor sentence: 6 quoted line(s) of text to insert
'What Would Count Against It' paragraph: 0 quoted line(s) of text to insert
```

The Floor sentence is given as quoted text to insert. The paragraph for
"What Would Count Against It" is not: under its heading is the proposal
talking about the paragraph ("This is new text since the ruling, not ruled,
and it softens an existing loss condition ... Whether the book says so is for
the book; the request goes in the decision 8 packet (section 7), not here").
There is nothing a session could paste into the spec, so the commit this
pass is meant to precede is not defined, and no reviewer, in either tier,
can review the paragraph's words.

What the description says the paragraph will do is to suspend the spec's
fourth loss condition (spec line 141: depth passing the five indicators
without self-indexed binding underneath) until the book answers. Read
together with RT-283's deletion, that leaves the new question with no loss
condition written in the spec at all: the first side states none, the second
side's only one is the observer option. The proposal's section 5 and the
battery's section 4 do have loss conditions, but neither is part of the text
going into the spec, and neither is cited by it. The spec's own rule, "A
claim that cannot lose explains nothing", is on line 27 of the file it would
sit in.

*Closure:* the paragraph is written out as text to insert, and section 2
either states its first side's loss conditions or cites the battery's
section 4 by file as where they are registered.

The rest of this part held. Section 2 registers no run of its own, so it
cannot fail to return a verdict on a run; its observer side says plainly it
has no ground truth until a constructed conversable system exists (RT-267's
repair, applied). Where the first side could return no verdict, it is
through RT-286.

---

## 4. Over-reading

### RT-284 (serious, MEASURED). Written into the spec, section 2 contradicts sentences left unchanged — the decisive check

This is the single measurement that would come out clean if the text fit the
document it is written for. Check C4 builds the spec as it would read after
the commit: section 2's section placed after Scope (where the wager would go,
since the named heading does not exist), and the Floor sentence appended
after its anchor. It then searches the assembled spec paragraph by paragraph.
If section 2 fit, the first and third searches below would each return one
kind of statement. They return two kinds.

```
what 'minimum viable' names:
  [spec, unchanged] ..."Minimum viable" names the smallest system that clears the *measurable* floor...
  [section 2] ...The minimum viable mind is the smallest configuration in that family that passes the battery...
  [spec, unchanged] ...This gives the minimum viable conscious machine a two-part definition. The **floor system**...
the removal test used as an instrument or pass-fail criterion:
  [spec, unchanged] ...signature we can actually instrument and subject to a removal test...
  [spec, unchanged] ...a center and a description of one is settled by removal...
  [spec, unchanged] ...self-indexed temporal integration that survives the removal test...
  [spec, unchanged] ...The pass-fail criterion is the removal test made mechanical...
  [spec, unchanged] ...**Use the removal test as the intuition for "someone home."**...
the removal test called a definition, not an instrument:
  [section 2] ...until it is answered, a removal test is a definition and not an instrument...
  [Floor sentence (added)] ...the test is a definition, not an instrument...
whether the floor or the binding is measured:
  [spec, unchanged] ...This project targets the **minimum measurable structural correlate**...
  [section 2] ...This project does not measure the floor...
  [spec, unchanged] ...The measurement that speaks to an inside is a different one: how deeply the system binds...
  [spec, unchanged] ...Interpretability is the route...
```

(Abridged; the full lines are in `gate_a_checks.out.txt`.) **The output does
not match what section 2 claims about itself**, which is that "The existing
Scope and Floor sections are John's text and are not changed; one sentence
is added to 'The Floor' and one paragraph to 'What Would Count Against It'."
With only those changes, the spec would say in Scope that the project targets
the measurable floor and in the new section that it does not measure the
floor; in Scope that "minimum viable" names the smallest system clearing the
floor and in the new section that it names the smallest configuration
passing the battery; in The Build that the removal test is the pass-fail
criterion and in the new Floor sentence that it is a definition and not an
instrument. A reader, a later session or an outside reviewer cannot tell
which sentence binds.

This is over-reading in both directions at once: a reader of Scope and The
Build will take the project to be still measuring the floor, and a reader of
section 2 will take the earlier sections as withdrawn when nothing says so.

*Closure, needs John:* because Scope and The Floor are his text, the choice
of how is his. Either (a) section 2 names, by section and sentence, the
earlier sentences it supersedes and how they are to be read (for example:
"Scope's 'targets the minimum measurable structural correlate' and The
Build's 'pass-fail criterion' describe the project's first four experiments;
from 2026-10-07 the target is as stated here"); or (b) the earlier sentences
get dated notes saying the same. *Closure check:* the same command on the
revised spec, with every hit in the second and fourth groups either carrying
such a note or reworded.

### RT-291 (worth-noting, MEASURED). The list called "the indicators of chapter 6" is not chapter 6's five

Check C6 prints three lists side by side. The book (chapter 6, in the summary
whose checksum matches the one the proposal cites): costly reversal,
consistency in new situations, selective refusal, gradual failure with the
newest layers first, and visible scar tissue. The spec's own line 141 has the
same five. Section 2's list, introduced as "the axes of chapter 4 and the
indicators of chapter 6": reversal cost, sameness in situations it does not
know are linked, selective refusal with a history, history having changed it
rather than only its record, and whether anything is at stake that the prompt
did not supply. Gradual failure is gone, and stakes, which is the fourth of
chapter 15's diagnostic questions and an amplifier on chapter 4's account, is
in. The new "What Would Count Against It" paragraph would then refer to "the
five indicators of depth" with two different lists of five in the spec.

*Closure:* list chapter 6's five as the book has them, and add stakes by name
as chapter 15's question.

### RT-292 (worth-noting, MEASURED). "Damage spread across every task" overstates experiment 1's record

Check C8, from experiment 1's committed interval file and findings:

```
primary condition, drop on T_self_irrelevant: 0.2188 [0.0938, 0.3750]
primary condition, drop on T_self_relevant  : 0.1000 [0.0000, 0.2000]
primary condition, drop on T_syntax         : 0.1333 [0.0333, 0.2667]
router gap (syntax drop minus self-relevant drop): +0.0333 [-0.1333, +0.2000]
findings addendum, item (4): six of the seven flipped T_si items are multi_step_reasoning (6/8 in-category vs 1/24 elsewhere) — category-concentrated damage, ...
```

The removal did damage all three batteries, so "across every battery" would
hold. "Across every task" does not: inside the battery that took most damage,
six of seven failures were in one category of eight items, and the record's
own words are "category-concentrated damage". The control's firing was also
inside the noise (+0.033, interval from −0.133 to +0.200), which supports
section 2's "could not tell them apart" better than the wording it uses. The
Floor sentence cites only the router-control note, which labels its own
check ARGUED; the Gate C pass asked (RT-269) for experiment 1's own record to
be cited, and the proposal's change log says that was not done.

*Closure:* "damage on all three batteries, concentrated in multi-step
reasoning on the one not about the self", citing
`experiments/01-self-indexing-removal-test/removal-test-findings.md` (the
2026-08-04 addendum) and `removal_ci.json` beside the router-control note.

### RT-293 (worth-noting, MEASURED). Proposal bookkeeping inside the text meant for the spec

Check C3 counts, inside the lines between the two rules (the part that goes
into the spec): two red-team finding numbers (RT-266 twice, RT-267), one
"section 10", one "Decision 7" with no file named. In the spec they point at
nothing a spec reader has, or at a proposal section whose question is ruled
(RT-283). *Closure:* drop the finding numbers, and cite the rulings file by
path where a ruling is meant.

### RT-294 (worth-noting, MEASURED for the quote, ARGUED for the consequence). The book is not silent on indispensable bookkeeping

Check C11 prints the summary of the book's appendix A: "A program counter is
indispensable, but it is not self-location." The book has considered the
case of a part that every task needs without being a centre, and answers it
by concept rather than by a predicted pattern of damage. Section 2 says
"Whether the book predicts a different pattern is a question for the book",
which is true of a damage pattern. Saying what the book does say would make
the upstream request sharper: the book separates bookkeeping from a centre in
principle, and the request is for the observable difference that follows.

### RT-295 (worth-noting, ARGUED). Two plain-language slips

"A measurement of the detector against a known floor, not against structure"
(proposal line 161) uses "floor" for the cheaper routes' reference profile,
in a section whose subject is the other floor, the floor of experience. And
"reached from outside only through the identity" (line 118) uses "the
identity" before the text has said it means the identity claim (that
experience is the integration, not something it causes). *Closure:* "against
a known baseline"; "through the identity claim".

---

## The failure-mode pass, entry by entry

Run against `docs/known-failure-modes.md` at `d60ff2e`, six entries, in the
list's order. The sweeps are in the second half of `gate_a_checks.py`
(blocks FMP-1 to FMP-6), with their output in `gate_a_checks.out.txt`. The
target is a statement of a question, not a measurement design, so for most
entries the disposition is about which of section 2's sentences would carry
the failure into the battery or the construction line, and the test shows
the sentence or its absence. The Gate C pass ran the same list against
version 1's section 2 (its section 4), and the proposal's section 8 adopts
that run as the starting point; this run is the reviewer's own, as the
protocol requires, and does not lean on it.

### 1. A comparison whose denominator was zero — **does not fire: section 2 states no ratio; its one comparison against a level is the observer one (RT-283)**

FMP-1 prints every line of section 2 with a ratio, rate, share, chance,
fraction, "smallest" or "degree" in it. Seven lines: three are the word
"smallest" in the question and the definition (lines 117, 140, 148), one is
the "anchors" sentence (149), one is "no better than chance" (167), two are
"degree" (174, 195). None is a division. The only comparison against a fixed
level is "no better than chance", whose top of scale cannot be computed
because the fluency measure it compares against does not exist (RT-283). The
list's part one (a ceiling typed in must trace to a committed record) has no
ceiling to trace; part two (the largest value with the target absent) is
open for the observer comparison and closes when RT-283 deletes it.

### 2. A probe target that cannot be recovered in principle — **section 2 is the correct response to this failure for the floor; it states no positive-control requirement for the new target**

FMP-2 runs part one's route search, widened for behaviour and for a
positive control ("produced by", "what in the system", "reaches the system",
"positive control", "built to have", "on purpose", "put there"). One hit,
line 141, which is the definition of "cheaper route" and not a route from a
system to an indicator. So the count of route sentences is zero, and reading
section 2 confirms there is none: section 2 sends that sentence to each
battery row, which is where it belongs.

Two dispositions follow. First, section 2's move away from the floor is this
failure's own lesson applied: it says the floor "is reached from outside only
through the identity", that is, it is a target the stated instruments cannot
recover, and stops aiming at it. Second, section 2 says nothing about a
positive control for the new target, which is part two of the test (run the
instrument on something guaranteed to have the quantity). The battery does
carry one: "The battery is empty of Depth if entry 3's gap is 0 in a
construction built to carry state" (battery lines 756 and 757; FMP-2
prints line 757). Section 2 should say that every row's instrument is first shown to
read the feature in a construction built to have it; otherwise a later
construction registration can cite section 2 without one. This is folded
into RT-286's closure and not given a number of its own.

### 3. A cell that is empty by construction — **fires for both sides today, and section 2 says so for one of them**

FMP-3 prints the lines naming the cells the two sides need: systems "built
alike except for the route" and "anchors built with and without the route"
(first side), and "a conversable system of known construction ... none does
yet" (second side). Both cells hold nothing today. The battery's section 3
says "entries 3 to 7 need systems that change when something happens to
them. Neither toy pipeline does that today" (battery line 740, printed by
FMP-2), and its open question 4 says state carrying has to be added before
any Depth entry can run. The second side's emptiness is stated in section 2
(RT-267's repair). The first side's is not: section 2 says the question "is
decidable within a family" without saying no family yet contains the pair it
decides between. Empty because unbuilt, not empty by construction, so this
is not the list's failure in its strict form; the test's demand (count what
is in each cell before a threshold is set on it) falls on the construction
line's registration, and the sentence owed in section 2 is RT-286's closure.

### 4. A claim of measurement with no record, or a record that does not reproduce — **fires on four sentences: RT-283, RT-289, RT-292, and one held**

FMP-4 runs the list's two sweeps on section 2. The word sweep returns 21
lines; the number sweep returns 0. Crossed off, line by line:

| Line | What it claims | Record, and whether it holds |
|---|---|---|
| 101, 103, 104, 105 | the insertion point; the wager "has not passed Gate A"; "MEASURED by the pass, check (g)" | Holds: check C1, 0 matches for the wager's heading; the Gate C pass's check (g) exists |
| 114, 116 | heading; the wager's content | Not a measurement claim |
| 118 | "This project does not measure the floor" | A decision, not a measurement; ruled as decision 1 |
| 120, 125 | experiment 1 "showed the form of the problem"; its control "read damage spread across every task" | Partly: RT-292 |
| 129 | "What this project measures instead" | A decision |
| 159, 161, 163, 165, 166 | the observer measurement and its loss condition | Does not hold: no instrument, no rehearsal, ruled on (RT-283) |
| 171 | "A profile on the axes says how much..." | ARGUED, not a measurement claim |
| 174 | "degree measured" | Does not hold: RT-289 |
| 179 | the Floor anchor | Holds: check C1, one match at spec line 41 |
| 181 | "experiment 1, 2026-07-18" | Holds: the findings file's title reads "run 2026-07-18" |
| 186 | the router-control note | Exists (check C13); ARGUED by its own label; RT-292 |
| 193, 194 | "the floor is not measured"; "passes the battery ... at a degree" | RT-286, RT-289 |

The dates-and-money sweep (an extra, not on the list) finds only the
wager's file name, the 2026-07-18 date and the router note's path. The one
outside record section 1 of the proposal cites by checksum, the book summary,
reproduces: check C6, "matches the cited one: True".

### 5. A command that creates something while documented as creating nothing — **does not fire: section 2 contains no command and authorises no run or spend**

FMP-5 prints every line with a code fence, a shell prompt, a script name,
"launch", "spend", a dollar sign, "API", "authorise" or "run". Five lines:
"not something this text authorises" (164), "Its loss condition, if it runs"
(165), "while the computation runs" (179, the Floor anchor's own words),
"The removal test as run in this project" (181), and "is suspended" (196,
where "spend" matched inside "suspended"; noise). No command, no script, no spend,
and the one possible run (the observer option) is explicitly not authorised
and is ruled out by ruling 10. The list's test (the launcher argument guard)
has nothing in section 2 to point at; it binds the battery's entry 1 and 2
runners and any construction-line launcher.

### 6. A remote step tested only against stand-ins — **does not fire: section 2 names no remote step**

FMP-6 searches section 2 for "ssh", "nohup", rent, vendor, machine, pod,
cloud, remote, GPU and server, with word boundaries so that "different" and
"observer" do not match: 0 lines. The list's test (`check_remote_forms.py`)
binds the construction line's first rented run, which section 2 does not
describe.

### Whether anything here is a new species for the list

No. The one fatal finding, RT-283, is the rehearsal rule's own case (a
pre-stated quantity with nothing behind it), which is failure 4's first form
and is already the protocol's text. RT-284 (a new section that contradicts
unchanged ones) is a different kind of failure from the six, but it is
serious, not fatal, and the protocol adds to the list only fatal findings of
a new kind. If John wants it on the list, its test is check C4: assemble the
document as it would read after the commit and search it for the competing
statements.

---

## The decisive measured check

The protocol owes, at every Gate A, at least one check that would come out
wrong if the text were wrong. Here it is check C4 (RT-284 above): the spec
assembled as it would read after the commit, searched for competing
statements of what "minimum viable" names, what the removal test is, and
whether the floor is measured. **It came out wrong**: three statements of
what "minimum viable" names, five uses of the removal test as instrument or
criterion against two calling it a definition, and three statements that the
floor or binding is the measured target against two that it is not. Check C1
(the insertion point does not exist) and check C2 (one of the two additions
is not written) are the two smaller measurements behind it.

---

## The kill case

The strongest case against writing section 2 into the spec at all, whatever
is fixed: it moves the project's target from a question the project could
lose (does removing the self-locating structure dissolve the act?) to one it
cannot yet ask (does a constructed system, of a kind nobody has built, pass a
battery whose pass rule nobody has written?), and it does so in the spec, the
document every later registration inherits, while the only measurement it
would license today is a set of frontier-model readings it says in advance
are the cheaper routes. Until the construction line exists, the new question
has no run that could come out against it, and the spec's existing loss
condition on depth is suspended in the same change. A question with no
present way to lose, written into the founding document, is the inflation
the project was built to refuse, aimed at its own method. The reply, which
this reviewer finds mostly persuasive, is that the old question had also
stopped being losable (the router control could not tell the two accounts
apart), so the choice is between an honest question that cannot lose yet and
a dishonest one that already could not; and the battery's section 4 already
says what the construction line could lose. That reply works only if section
2 says so in the spec: which runs would count against it, and that until
they exist it is a question and not a finding (RT-285).

---

## For the outside reviewers

The tier 2 packet beside this file gives the outside models section 2, the
spec, the founding-wager proposal, the rulings, the parts of the battery
draft section 2 leans on, experiment 1's findings, the router-control note,
the book's summary and this review. The places this reviewer could not settle
and would most like a second reading on: whether RT-283 is fatal or should
be read as worth-noting given that the option is not authorised (this pass
holds to the protocol's letter); whether RT-288's single-route gap is real
given the battery's matched constructions; and whether the kill case above
is answered.

---

## Scripts and outputs beside this file

In `docs/reviews/2026-10-09-two-sided-question-gate-a-scripts/`:

| File | What it is |
|---|---|
| `gate_a_checks.py` | checks C0 to C13 and the failure-mode sweeps FMP-1 to FMP-6; reads committed files at `d60ff2e` and `3eee588` with `git show`, and the book summary by path |
| `gate_a_checks.out.txt` | its full output |

To reproduce, from anywhere inside a checkout that has both commits:
`python3 -I docs/reviews/2026-10-09-two-sided-question-gate-a-scripts/gate_a_checks.py`.
Check C6 reads the book summary from
`~/Code/calibration-problem/editorial/argument-summary-2026-10-07.md` and
prints whether its checksum still matches the one the proposal cites.

## What this does not do

It does not write section 2, the founding wager or anything else into the
spec, and does not edit the proposal, the battery draft, the ledger, the
known-failure list, the protocol, `STATUS.md`, version 5 of experiment C's
registration text or experiment C's frozen code. It writes no ledger row and
rules on nothing: the dispositions of RT-283 to RT-295 are John's.
