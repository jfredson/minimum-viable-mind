# Outside-review protocol for Minimum Viable Mind

*Drafted 2026-09-19 (Pacific) in a Cowork session from the mobile-session
proposal of the same day ("a standing outside-review gate for MVM").
Status: IN FORCE. John ruled on the seven decisions at the end on
2026-09-19 (Pacific), all accepted as proposed, in his words: "agreed on
all". No compute or spend is implied.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

*Amended 2026-09-21 with the three changes John adopted on 2026-09-20 (item 6
of `docs/rulings/2026-09-20-december-result-roadmap.md`, in his words "Agreed
on all"): a complete measurement rehearsal before any Gate A, reviewer-owned
verification of a fatal finding's closure, and the word "unlikely" struck from
the fixed brief. They are listed at the end under "Amendments". The ruling
authorises the three changes; the wording is this session's and is John's to
overturn.*

---

## What already exists, so this is continuity and not a new practice

MVM has run adversarial review five times, all recorded in
`experiments/06-mvm-0a-constructed-self-index/`:

- Pass 1, 2026-08-04, on the pre-registration draft: 15 findings, 3 fatal
  (`red_team_ledger.md`, RT-01 to RT-15).
- Pass 2, 2026-08-09, on the gate-(iii) fix (same ledger, RT-16 to RT-19).
- Pass 3, 2026-09-15, on Amendment A3 before its registration commit: 13
  findings, 2 fatal (`red-team-pass-3.md`, RT-20 to RT-32).
- A4 pass 1, 2026-09-19, Claude on its own A4 proposal: 15 items
  (`a4-red-team-pass-1.md`).
- Independent A4 pass, 2026-09-19, a separate Claude Code session in its own
  worktree (`worktree-red-team-a4`), which by its own discipline did not open
  the amendment draft, the first pass, or the scoring script: 22 findings,
  labelled F1 to F22 (`red-team-a4.md`). This is the pass that stopped the
  three-seed wave.

So the proposal's premise that review "has run once" is wrong on the record.
What is true is that review has been ad hoc (fired when someone thought of
it), same-model (every pass was Claude), and has no closure rule. The third
of those is the one that has cost the most.

## What actually went wrong, read from the repo

The proposal lists two failures caught late: the registered comparison clause
was unsatisfiable from the day it was registered, and the localization probes
targeted a generator index that cannot be recovered in principle.

The first was not a detection failure. Pass 3 (2026-09-15, four days before
the registration commit) said it in so many words in RT-21: "under the unfixed
grammar the ownership-blind ceiling is 1.000, so the corrected metric has a
zero denominator, which is the arithmetic saying, correctly, that the metric
has nothing to measure." RT-21 was marked fatal and its metric fix was marked
adopted. But the fix depended on the control battery's ceiling having been
measured and attacked, and it never was: the registered text of A3 §4 said
both ceilings were "verified by the attack sweep" when only the primary's had
been (`ceiling-defect-2026-09-17.md`). The 2026-09-17 defect registration and
the 2026-09-19 "never computable" finding are the same fact landing twice.

So the missing piece is not more review before registration. It is a rule
that a fatal finding is not closed by a sentence saying it is fixed; it is
closed by a committed record that a second reader can check, and any
"verified" or "measured" claim in registered text has to point at one.

The second failure (the unrecoverable probe target) is the feasibility
question no pass was asked to ask: can the quantity the pre-statement names
be recovered at all with the stated instrument. That question goes into the
brief.

## The gates

Review fires, with a written record in the repo, at three points.

**Gate A — registration.** Every registration, amendment, threshold lock, or
pre-statement that will be read as binding, before the registration commit.
Both tiers below run. The registration commit waits on the closure rule and on
the filed failure-mode pass. No Gate A pass opens until the measurement
rehearsal for that target is committed, and reading the rehearsal is the first
thing the tier 1 reviewer does.

**Gate B — interpretation.** An interpretation of a result before it enters
STATUS.md's current-state section or the paper draft, when it either changes
program direction or is a claim the paper will carry. Routine null entries and
ledger rows are not gated. Tier 1 runs; tier 2 runs only when the
interpretation is paper-bound.

**Gate C — rulings.** A ruling on program direction is John's call by design,
and a review of the ruling after the fact would make the reviewer a veto over
him. So the review attaches to the proposal before it reaches him: any
proposal that asks for a John-level ruling carries a tier 1 pass, filed and
linked, so he rules on text that has already been attacked. Tier 2 only if he
asks. First application: public path step 4, the 2026-10-04 control-battery
decision (repair the clause under a new amendment, or close A3 with partial
discriminators).

## The pairing rule: whatever one session writes, a different session checks

The three gates above fire at three points. The pairing that has actually caught
things in this programme is finer-grained than a gate: one session writes or
fixes, a different session checks, every time — not only when a gate happens to
fall there. That is a standing rule and not an occasion.

**Binding text** is anything a later session will read as settled and build on
without deriving it again: registered text and its amendments, pre-statements
and threshold locks, closure texts, the text of this protocol and of the
known-failure list beside it (`docs/known-failure-modes.md`), and recorded
rulings. A proposal on its way to John counts, because Gate C attaches a pass to
it. A working draft does not, until it is committed as one of those.

**What the checking session produces** is a filed record with three things in
it: what it opened and what it did not; at least one check it ran, given as the
command and the output the command returned, chosen so that the output would
come out wrong if the writing were wrong; and, for each claim it checked, a
plain sentence saying whether that output matches what the text claims. Every
finding is labelled MEASURED or ARGUED, the convention the passes already use.
Reading the text and finding it convincing is not a check, and a summary of what
the text says is not a check either. Where there is genuinely nothing to run —
text carrying no number — the checking session says so and instead names the
records it opened and the sentences it read against them, one by one.

**Where it is filed.** Under the experiment's reviews directory when the target
belongs to an experiment, on the path in "Filing" below. Otherwise the check
goes in the message of the commit that lands the checked text, commands and
outputs included, which is where the packet rebuilds and the roadmap conversion
of 2026-09-21 already put theirs.

**The checking session is not the writing session.** It has not read that
session's chat, and it gets the packet and nothing else, on the same terms tier
1 works under below. One session may write one thing and check a different thing
in the same sitting. No session ever checks its own work.

**Why this is a rule and not a habit.** This protocol opens by saying that
review before it existed was ad hoc — fired when someone thought of it. Firing
review only where a gate falls is the same failure at a smaller scale: the gate
catches the document and misses the eleven edits that got it there. The pass
that stopped the three-seed wave, the independent Amendment A4 pass of
2026-09-19, was not at a gate, because no gates existed. It was a second session
reading what a first session had written.

## Isolation is not traded for speed

The separation between the session that writes something and the session that
checks it is never collapsed. Not when the fix is one line. Not when the writing
session is sure. Not when John is waiting, not when an outside reviewer's hour is
already booked, and not when collapsing it would save the only day standing
between the programme and a result.

The reason is written here, and not only the rule, because a session reading
this under pressure needs the reason: this is the cheapest step in the protocol
to skip and the one that has caught the most. Skipping it costs nothing visible
on the day. The text still reads well — to the person it reads well to, who is
the person who wrote it. What it costs shows up later, in a registered sentence
nobody can satisfy, and by then the cost is weeks. This document's own
opening is the evidence: a fatal finding was closed by a sentence saying it was
fixed, and a registered clause said two ceilings were "verified by the attack
sweep" — both written, read back and believed inside one session.

**What these rules cost.** The pairing rule, the failure-mode pass, this section
and the rebuild rule below all buy the same thing with the same currency: they
slow the programme down per unit of finished work. A document that used to be
written is now written and then waited on. A registration that used to need a
rehearsal now needs a rehearsal and a filed pass running the old failures against
the new design. A document that used to be tidied when it looked untidy is now
rebuilt whenever new binding text starts to lean on it. That is real, and none of
it is free. It is still the right trade, on one observation: the rate at which
this programme produces defects has not fallen, while the rate at which it
catches them has risen. The zero-denominator failure on the Amendment A3 control
battery (the unequal-ceilings finding, `RT-21`, 2026-09-15) and the moving-ceiling
failure in the successor proposal (the per-arm-ceiling finding, `RT-172`,
2026-09-21; both are set out with their records in `docs/known-failure-modes.md`)
are the same failure six days apart, and the design that produced the second was
written by a session that had the first in front of it. What has improved is the
finding, not
the writing. Until that changes, checking is the part of this work that is
producing the reliability, and it cannot be traded for speed without trading the
reliability with it.

## The measurement rehearsal, required before any Gate A

Twice a registration has gone in before anyone had run the measurement it
registers: the corrected metric whose denominator turned out to be zero, and
probes aimed at a quantity that cannot be recovered in principle. Both would
have shown themselves in an afternoon of running the procedure on a throwaway
system. So before any Gate A pass, the whole measurement runs once, end to
end, on a small stand-in, and that run is committed.

The rehearsal is meant to be small and cheap: tiny models, a handful of
episodes, a day or two of work, somewhere between nothing and about ten
dollars of compute. It is not a pilot and it is not evidence about the
question. It is a demonstration that the instrument exists and gives back
numbers.

"Complete" means all six of these, each with the command that was run and the
output it produced in the committed record:

1. **The target can be found.** The quantity the pre-statement names is
   recovered in the stand-in system by the stated instrument, with a number to
   show for it. If it cannot be recovered even there, the rehearsal says so
   and the pre-statement changes before it is registered.
2. **The comparison has room to move.** Every control, baseline or comparison
   condition is scored and its ceiling is measured rather than assumed, so the
   record shows the stated threshold is reachable and the comparison is not
   already saturated.
3. **The arithmetic is finite.** The metric is computed on those scores and
   returns a number: no zero denominator, and no formula that only survives on
   the values its author had in mind.
4. **The interventions run end to end.** Every lesion, patch, swap or other
   intervention the design leans on runs to completion on a saved checkpoint
   and moves the output it is supposed to move.
5. **All three outcomes are reachable.** Made-up cases are built that drive
   the procedure to a positive verdict, to a negative one, and to no verdict
   at all, and each is shown to land where it was meant to.
6. **An ordinary competing solver is built and scored.** A system with none of
   the structure the target claims to detect is constructed and put through
   the same measurement, so the brief's "satisfied by the wrong thing"
   question has a number behind it instead of an argument.

The rehearsal also reports throughput: how long one run takes at rehearsal
scale, and what the registered scale is therefore estimated to cost, so the
spend figure in the proposal has a measurement behind it.

It is filed the way findings are filed, under
`experiments/<experiment>/reviews/YYYY-MM-DD-<target>-rehearsal.md`, or under
`docs/` when the experiment's directory does not exist yet. A pre-stated
quantity with no rehearsal line covering it is a fatal finding on its own, on
the same reasoning as a "verified" claim with no record behind it. The numbers
the rehearsal produces are committed records, so the sentences the closure
rule asks to be cited have something to point at.

First application: the rehearsal for the successor experiment
(`docs/december-result-roadmap-2026-09-20.md`, section 4, step 2 of the chain).
It runs as soon as the successor proposal's first draft exists, alongside the
Gate C tier 1 pass on that draft, rather than in a week set aside for it. It
must show that the three arms are constructible, that the pointer in the
built-to-be-separable arm can be patched, that the joint patch in the
built-to-be-entangled arm works, that the metric returns positive, negative
and invalid values on toy cases, and what the new task grammar costs per run.

## The failure-mode pass: the known failures are run against the design, not cited

Every registration text goes through a pass in which each failure named in
`docs/known-failure-modes.md` — the list, kept beside this protocol, of what has
gone wrong here before — is tested against this design. Tested, not mentioned.

The reason is one afternoon's evidence. A proposal reviewed on 2026-09-21 named
the zero-denominator failure of the Amendment A3 control battery, by its plain
description, in the section where it discussed the weaknesses of its own
measure — and the measure two sections earlier reproduced it, with the zero
replaced by a ceiling that moves from arm to arm. The design had the failure mode
in hand, referred to it by name, and reproduced it anyway. Citing a failure is
something a text does; the text is not thereby free of it.

How the pass runs:

- **Every failure on the list gets a disposition, and every disposition shows
  its work**: the command that was run and the output it returned, in the filed
  record.
- **"Considered and does not apply" is not a disposition.** If a failure does not
  apply, the pass shows that: the denominator that is not zero, the pre-stated
  cell that has trials in it, the positive control that cleared the bar, the
  record that exists and contains the number the sentence cites.
- **A failure that genuinely cannot be tested on this design gets the reason on
  the record and stays open**, exactly as a closure check that cannot be run
  does. It is not closed by the difficulty of checking it.
- **The pass belongs to the Gate A tier 1 reviewer**, who owns and files it, for
  the same reason the closure check is the reviewer's: the design's author is the
  one whose blind spot produced it, and the design that reproduced the
  zero-denominator failure was written by an author who had just named that
  failure. The author may run the list first and fix what it
  finds — that keeps a scarce outside hour off a defect already known, which is
  what John ruled on 2026-09-21 about the closure text's citation defects — but
  an author's run never stands in for the reviewer's.
- **A fatal finding of a kind not on the list is added to the list** by the pass
  that found it, with its own test written the same way. That addition is binding
  text, so it is checked under the pairing rule like any other.

Filed with the Gate A findings, as a section headed by the list's entries in
order, so that a reader can see at a glance which failures were run and what each
one returned. A registration text with no filed failure-mode pass does not reach
its registration commit, on the same standing as a pre-stated quantity with no
rehearsal line covering it.

## Two tiers, because outside models cannot run the code

**Tier 1, the inside pass.** A fresh Claude Code session in its own worktree.
Context isolation is the non-negotiable part, and is what made the
independent A4 pass useful despite being the same model: the session gets the
packet (the target text, the registered text it must be read against, the
committed code and records) and nothing else. No chat history, no uncommitted
files from the shared checkout, no ruling annotations, and it says at the top
what it did and did not open. Every finding is labelled MEASURED (a check was
run and the output is reported) or ARGUED (reasoning a reader can dispute),
the convention the existing passes already use. This tier can run code and
compute bounds; it is the only one that can produce MEASURED findings. At
Gate A it also owns the verification the closure rule requires below: the
decisive check on a fatal finding's fix is the reviewer's to run, not the fix
author's to assert.

**Tier 2, the outside pass.** At least two models from labs other than
Anthropic, run by John through their apps, exactly as the Belt Equation's
step-27 protocol does it (`belt-equation/docs/reviews/protocol.md`). Same
packet as tier 1 plus the tier 1 findings, so the outside reader can go
looking elsewhere. All findings are ARGUED, since these models see documents
and not a running checkout. Model, version, date and mode recorded at the top
of every filed response; responses filed verbatim and never edited.

The tier 1 pass runs first. The tier 2 packet includes its findings. Neither
tier's author writes the fix for its own finding's closure check (below).

## The brief, fixed, sent unchanged with every packet

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether or
not the reviewer thinks the target should ship.

1. **Feasibility.** For every quantity the target pre-states or thresholds:
   can it be measured at all with the stated instrument, and can the control
   or comparison condition actually reach the stated threshold? Cite the
   committed record that shows so, or say that none exists. A "verified" or
   "measured" claim in the text with no record behind it is a fatal finding
   on its own.
2. **Satisfied by the wrong thing.** Every way the clause, its baselines, or
   its threshold calibration could be satisfied by a model with none of the
   structure it claims to detect, or fitted to data the text says is excluded.
3. **No verdict.** Every way the target could fail to return any verdict on
   the runs it is written for.
4. **Over-reading.** What the result will be read as claiming beyond what it
   measures, in the paper, in STATUS.md, and in public.

Plain language throughout. Lookup allowed and flagged. Do not soften findings
to be polite, and do not manufacture severity to look thorough. A pass that
finds nothing fatal is a valid result, reported as what was checked and what
held.

## The closure rule, which is the new part

Before a registration commit at Gate A:

- Every fatal finding from either tier has a closure line in the ledger, in
  the form: finding, the commit that lands the fix, and a MEASURED check by a
  session other than the one that wrote the fix, showing the fix does what
  the closure says. "Adopted" is a disposition, not a closure.
- **That check belongs to the reviewer, not to the author.** The tier 1
  reviewer of the Gate A pass owns it and runs it: reproduce the denominator,
  build the competing solver, re-run the intervention, recompute the number —
  whichever single measurement would come out wrong if the fix were wrong.
  Reading the fix and finding it convincing is not the check. What the
  reviewer produces is a MEASURED finding in the filed review: the command
  run, the output it gave, and a plain sentence saying whether that output
  matches what the closure claims. If the reviewer cannot run the check, the
  reason goes on the record and the finding stays open.
- **The ledger says which of the two happened.** A fatal item's ruling line
  states either that the argument was accepted or that the claim was checked,
  and, when it was checked, names the reviewer and the check. Agreement and
  verification are not the same thing, and the record should not let them read
  as if they were.
- Every sentence in the registered text that says verified, measured,
  calibrated, or attacked cites the committed record by file name, and the
  closure check confirms the record contains what the sentence says it does.
- Serious findings are closed the same way or carried as an open item named
  in the registered text, with John's ruling and reason.
- A declined finding keeps its reason on the record so the next pass can see
  it was considered.

Had this rule been in force on 2026-09-15, RT-21's closure check would have
gone looking for the control battery's attack record and found none.

## Rebuild a document when new binding text starts to depend on it

The closure rule above makes a sentence point at a record. This rule keeps the
record from drifting out from under the sentence.

A document is not tidied when it looks untidy. It is re-read at the moment new
binding text starts to depend on it — cites it, quotes it, takes a number from
it, or inherits an obligation from it — and the way it is re-read is by
**rebuilding** it: regenerating it from its source, converting it into a
different order, or deriving its list again from the thing it claims to
summarise. Reading a document you already believe is a weak instrument. Rebuilding
it makes the document answer, line by line, whether it still says what it is
being cited for.

The evidence is that three of the findings of 2026-09-21 came from exactly this,
and none of them came from anybody reading the document again:

- **Converting the December-result roadmap's plan into dependency order** — what
  waits on what, in place of which week — showed that the plan described one
  launch step where the ruling of the same day described two: one free-arm run
  first, its result read, and only then the remaining eight.
- **Rebuilding the outside-reviewer packet from the closure text's own
  citations** showed that the reviewer was being handed five records against the
  twenty that text cites, so most of a reviewer's hour would have gone on
  reporting the packet's gaps rather than the text's.
- **Committing the December-result ruling** showed that the closure text was
  citing a ruling file that existed at no commit in this repository (the
  uncommitted-citation finding, `RT-145`), which a registration commit is the one
  commit that may not do.

What the rebuild produces is the list of differences it found, filed with the
work that prompted it. Where the rebuild changes the document, that change is
binding text and is checked under the pairing rule like any other. Where a
rebuild is genuinely too expensive to run, the document is named, what was not
rebuilt is stated, and it stands as an open item rather than as a silence.

## Filing

- Findings: `experiments/<experiment>/reviews/YYYY-MM-DD-<target>-<reviewer>.md`,
  verbatim, never edited after filing. Tier 1 findings continue the ledger's
  RT numbering; tier 2 findings are labelled by reviewer (for example G1 to
  Gn for Gemini) and take RT numbers only when John's ruling adopts them, so
  the two passes cannot collide.
- Rulings: one line per item in `red_team_ledger.md`, in the form used since
  2026-08-04: item, reviewer(s), John's ruling (accept, accept with change,
  decline, carry open), reason, and for fatal items the closure line.
- Packets: hand-assembled for now, with the file list at the top of the
  findings file. A packet script like the Belt Equation's
  `scripts/review_packets.py` is worth writing once the third packet exists.

## What changes from the Belt Equation's step-27 protocol

Kept as is: reviewers see everything; lookup allowed and flagged; a fixed
brief sent unchanged; John runs the outside sessions and Claude prepares and
files; verbatim filing; John rules on every item and a ruling to keep the
text over an objection is a valid outcome with its reason on record.

Changed for an empirical program:

- The unit of review is a document (a registration, an amendment, a
  pre-statement, an interpretation), not a factor packet of nodes.
- The brief asks about feasibility, wrong-thing satisfaction, no-verdict, and
  over-reading, in place of missing nodes, criteria, and numbers.
- No 0.15 threshold for what counts as a disagreement; severity (fatal,
  serious, worth-noting) does that job, as the ledger already does.
- Two tiers instead of one, because the review needs code access to produce
  MEASURED findings and outside models cannot have it.
- The closure rule, which the Belt Equation does not need because a
  probability change lands in one data file and a re-run.

## Retroactivity

The proposal asked whether Gate A applies to the control-learnability pilot.
It is moot: the pilot launched 2026-09-19 at about 20:14Z on John's verbatim
go (compute ledger row of that date), and it is unregistered by design. Its
pre-statement (`control-learnability-pilot.md`) is the kind of document Gate A
would cover in future, and its pre-stated cells were committed before the
code existed, which is the discipline the gate is meant to enforce.

## Decisions (ruled 2026-09-19, all accepted as proposed; each with confidence, whether it is standard practice, and the alternative)

1. **Adopt the three gates as scoped here** (A: every registration, both
   tiers; B: direction-changing or paper-bound interpretations only; C: review
   attached to proposals, advisory, not a gate on rulings). Confidence high on
   A, moderate on the scoping of B and C. Standard practice for A (a
   registration is a pre-print of the method). Alternative: the proposal's
   original wording, every interpretation and every ruling; costs a pass on
   routine null entries and puts a reviewer between John and his own calls.
2. **Context isolation is mandatory for tier 1; other-lab models are
   mandatory for tier 2.** Confidence high. The independent A4 pass shows
   isolation is what does the work; other labs add a different set of blind
   spots. Alternative: tier 1 only. Cheaper; every pass so far has been
   Claude, and a same-model reviewer shares the proposer's priors about what
   is measurable.
3. **The closure rule.** Confidence high; this is the finding of this draft.
   Standard in engineering review (a fix is closed by a test, not by a note).
   Alternative: keep "adopted" as the terminal state. That is the state RT-21
   was in when the unsatisfiable clause was registered.
4. **The four-part brief.** Confidence moderate on the exact wording, high on
   feasibility being part 1. Alternative: reuse the A4 brief (a to d) as
   written; it lacks the feasibility question, which is the one both late
   failures needed.
5. **Tier 2 reviewers: the same pair as the Belt Equation** (GPT-6 Astra via
   the ChatGPT app, Gemini via its app), a third on disagreement. Confidence
   moderate. Alternative: one outside model; halves John's session time,
   loses the disagreement signal.
6. **Filing under `experiments/<experiment>/reviews/` with the ledger as the
   rulings file**, this protocol at `docs/outside-review-protocol.md`,
   mirrored as a TimeAssembler project document once ruled. Confidence high;
   it is where the five existing passes already live.
7. **First application is public path step 4**: a tier 1 pass on whatever
   proposal carries the 2026-10-04 control-battery decision, then Gate A in
   full on any amendment text that comes out of it. Confidence high.
   Alternative: start with the paper draft at step 7; later, and step 7's
   outside human reader is a different check (see
   `docs/outside-reader-shortlist-2026-09-19.md`), not a substitute.

## Amendments

**2026-09-21 — three changes, ruled by John on 2026-09-20** (item 6 of the
December-result roadmap ruling, `docs/rulings/2026-09-20-december-result-roadmap.md`,
"Agreed on all"). All three come from the two-lab program review of 2026-09-20
(`docs/reviews/2026-09-20-program-review/`), and the ruling makes this edit the
first thing the successor experiment's Gate A checks.

1. **A complete measurement rehearsal before any Gate A** — the new section
   above, plus one sentence added to Gate A. It closes the reviewer's finding
   that registration here has repeatedly run ahead of any demonstration that
   the full measurement procedure existed (item A8 of the ChatGPT/Astra
   response, and the same point as Gemini's first process change). The six
   checks are that reviewer's list; the throughput line and the filing rule
   are this session's addition.
2. **Reviewer-owned verification of a fatal finding's closure** — two bullets
   added to the closure rule, and one sentence added to tier 1. It closes the
   finding that same-family review followed by a ruling of "agreed on all" is
   governance rather than an independent check (item A9 of the same response).
   The existing rule already demanded a measured check by a session other than
   the fix's author; what is new is that the Gate A tier 1 reviewer owns it,
   runs it, and files the command and its output, and that the ledger line
   says whether an argument was accepted or a claim was checked.
3. **"Unlikely" struck from the fixed brief** — the sentence that a target
   with nothing fatal was "a possible finding, but an unlikely one" is gone,
   because it paid reviewers in severity (the seventh process change of the
   same response). The program review's own brief had already dropped the
   equivalent line before it went out. The replacement warns off both
   directions: do not soften, and do not manufacture.

The ruling authorises these three changes. The wording is the drafting
session's and is John's to overturn.

**2026-09-21 (later the same day) — one wording change, ruled by John**: work is
measured in task time, not calendar time. In his words, "We are not working on a
delayed calendar. We are working on a finish every task as quickly as possible
mode." The rehearsal section's first application named a week; it now names what
must exist before the rehearsal can run. Nothing else in this protocol changed:
no gate, tier, brief item, closure rule or filing path is affected. Two dates
elsewhere in this file are left alone because they are records of what was ruled
and when, not plans: the 2026-10-04 control-battery decision named as the first
application of Gate C and of the protocol as a whole (ruled early, on
2026-09-20), and every date in the history of past passes.

**2026-09-21 (later the same day again) — four changes, approved by John.** Six
recommendations came out of a working session, each put to him with its cost, and
he approved them in the words "Ok, can we implement all of these?". Four of the
six are protocol text and are the four below; the other two are not. Mixed
authorship, on the same footing as the items above: the session proposed them and
he approved them, and none of the wording is his drafting. No compute was launched
and no money was spent under them.

*A ruling file recording these four had not been written when this text was
committed.* The two ruling files of the same day —
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, the
review-verification and staged-spending ruling, and
`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, the follow-up-runs and
blind-arm ruling — do not contain them. One is owed, and this entry is the only
record of the approval until it exists. That is the gap the rebuild rule above is
about, so it is stated here rather than papered over with a citation to a file
that does not yet say it.

1. **The pairing rule** — the new section of that name, after the gates. It closes
   the finding that the pairing which has caught things is finer-grained than a
   gate: one session writes, a different session checks, every time. What the
   approval authorises is the rule. What is the session's judgment is the
   definition of binding text (which documents are in and which are not), the
   three things the checking session has to produce, and the filing fallback into
   the commit message for documents that belong to no experiment.
2. **The failure-mode pass, and the list it runs against** — the new section of
   that name, one clause added to Gate A, and the companion document
   `docs/known-failure-modes.md`. It closes the sharpest finding of the day: a
   proposal cited the zero-denominator failure by name, in the section discussing
   its own measure's weaknesses, and reproduced that failure in the measure. The
   approval authorises the pass and the list. The session's judgment is that the
   Gate A tier 1 reviewer owns the pass rather than the author (with the author
   free to run it first and fix what it finds), that a failure which cannot be
   tested stays open rather than closing on the difficulty of testing it, and that
   a new species of fatal finding is added to the list by the pass that found it.
   The four entries on the list are the four real failures; the test written under
   each is the session's, and every output printed in that document came from
   running the command printed above it.
3. **Isolation is not traded for speed** — the new section of that name. It states
   plainly that the separation between the session that writes a fix and the
   session that checks it is never collapsed, including under time pressure, and
   gives the reason in the same place: it is the cheapest step to skip and the one
   that has caught the most. The approval authorises the rule; the reason, its
   wording, and the statement of what all four changes cost are the session's.
   That cost statement is the session's own addition and nobody asked for it:
   these four rules slow the programme per unit of finished work, and the argument
   for paying is the observation that the rate of producing defects has not fallen
   while the rate of catching them has risen.
4. **Rebuild a document when new binding text starts to depend on it** — the new
   section of that name, after the closure rule. It closes the finding that
   documents here go stale underneath the citations that depend on them, and that
   rebuilding is what finds it: three findings of 2026-09-21 came from a
   conversion, a packet rebuild and a commit, and none from re-reading. The
   approval authorises the rule. The session's judgment is what triggers it (new
   binding text citing, quoting, taking a number from, or inheriting an obligation
   from the document), that the differences a rebuild finds are filed with the work
   that prompted it, and that a rebuild too expensive to run becomes a named open
   item rather than a silence.

The approval authorises these four changes. The wording is the drafting session's
and is John's to overturn. This text had not been checked by another session when
it was committed; under the pairing rule it is owed one, and the session that
writes that check is not this one.
