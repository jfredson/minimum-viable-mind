# STATUS — where we are, how to resume

*Living handoff doc. Update it at the end of a working session so the next one (you, or Claude in a fresh session) can pick up without re-deriving context. Most recent state at top.*

*Older entries (2026-10-08 late night and everything before it, back to the start of the project) moved to `STATUS-archive.md` on 2026-10-12, so a resumed session reads only the latest three. Line numbers cited into STATUS.md before 2026-10-12 now point into the archive, offset by 240 lines (old line N is archive line N − 240).*

**How the two roadmaps of 2026-09-20 fit together** (written 2026-09-24 at John's
instruction, as change 6 of the 2026-09-22 workflow audit asked — TimeAssembler
worklog entry `d6c7060e`, "Workflow audit: the record is honest and the science is
real…"): the programme roadmap (`docs/program-roadmap-2026-09-20.md`) is the
open-ended plan, whose lines of work are neither ordered nor dated, and the
December-result roadmap (`docs/december-result-roadmap-2026-09-20.md`), which says
of itself that it refines that plan rather than replacing it, is the one dated line
inside it — the successor experiment, with its two kill dates and its wrap-up start
of 2026-12-21 — while the weekend roadmap (`docs/weekend-roadmap-2026-09-24.md`) is
only a schedule laid over that dated line and gives way to it wherever the two
disagree.

## WHERE THINGS STAND 2026-10-18 (evening) — the paper's choices made and checked; John holds the outside reader for a readiness checklist; the battery rehearsal is part-run and resumes a day at a time; the spend figure corrected, and every new spend now needs its own go

*Written 2026-10-18 (Sunday evening, Pacific) by the session that worked the
programme over the weekend, on John's answers relayed by the fifth master
session for the tracker sites. The entry below it, from earlier the same
day, stands.*

**The paper.** John answered its four open choices, each as recommended
(authorship mixed; `docs/rulings/2026-10-18-paper-reserved-places-ruling.md`):

- the title is now "Instruments that can lose: a registered removal test, a
  constructed self-index and a successor stopped by its own rule, in the
  measurement of self-indexed integration";
- the paragraph that argued the damage pattern "supports the router reading
  twice over" now says the data do not separate the two readings;
- the Discussion's two changes are made, with a Limitations sentence that
  the constructed line's locating instruments are unvalidated at 30 million
  parameters;
- the spelling is British, with quotations left as their sources spell them.

A check then found the cost sentence untrue. On John's "Yes to both" and "Ok,
go ahead", it now gives the removal test's own cost, and "the two
constructed-line experiments that followed for about $230.94 of rented
compute". Three sentences that said "programme" for the removal test now say
"in this experiment". Pull requests 190 and 193, each checked (192 and 194),
are merged. Pull request 180, the checked explanation of arm M's zero
(re-checked as pull request 189), is merged on his "Go ahead".

**The outside reader is held, on John's own ruling** (authorship john): "I'm
not sure I have the confidence in it yet for that". He approved a five-step
readiness checklist, `docs/paper-readiness-checklist-2026-10-18.md`:

1. his own read of a clean copy, listing every sentence he would not defend;
2. three mock referee reports, then an outside model;
3. a reproduction of every number from a clean clone;
4. a friendly expert before a senior one;
5. a modest first venue.

He said to start steps 2 and 3 now. The three referee sessions are proposed
as session cards, and the reproduction is sent to the master session to
start.

**The battery rehearsal is part-run.** It started on John's "Go up to $50",
with ceilings of $27 for entry 1 and $23 for entry 2 and the worklog row
written before the first call. It stopped partway through entry 1 on Google's
daily limit of 250 requests to Gemini 3.1 Pro, having used 253.

- **Kept:** 437 calls held in records (arm S2 and arm B complete, arm B2 67
  of 107).
- **Spent by estimate:** about $2.88 to $7.13.
- **No reading yet.**
- **Left to finish:** 1,351 Gemini calls in all, so about 1,098 remain.

John ruled to finish it a day at a time under the same go and ceilings. A
loop on this Mac (`artifacts/stage3/battery_rehearsal_daily_resume.sh`,
beside the outputs) restarts the committed runner after each midnight
Pacific reset. Before each start it estimates the Google account's prepaid
balance. That was $20.00 on John's reading after the first start, and the
loop stops cleanly for a top-up if a day's calls could exhaust it. At the
high-end thinking allowance the remaining Gemini calls come to about $23, so
a top-up of about $10 is likely to be needed around the third or fourth
day.

**The spend figure, corrected.** This file, the site data and the explainer
have said "the programme stands at about $230.94 of $450". That figure is
the compute ledger only: rented machines from 2026-08-07, when the ledger
opened, to the stop of experiment C. The ledger itself says the removal
test's spend "predates this cap", and API calls are recorded in the worklog,
not the ledger. On 2026-08-30 John put true spend to date across every
vendor at about $281 to $300, when the ledger read about $181. From the
record as it stands, the programme's spend across every vendor is roughly
$335 to $360:

| Part | Figure |
|---|---|
| The ledger | $230.94 |
| Outside the ledger by 2026-08-30, by John's figure | about $100 to $119 |
| API calls logged since, at least | about $4 to $8 (the Gate A tier 2 pass of 2026-10-09 and the first start of the rehearsal) |

The poll of 2026-10-07 and any other unlogged API calls are still to be
added. *(Corrected the same evening: this paragraph first said John had
ruled that every vendor counts against the $450 ceiling. He had not; the
fifth master session corrected its relay.)* **John's ruling, in his words:**
"I'm not so worried about the $450 ceiling, I just want to make sure we are
keeping track of any new spending. Any new spending needs to get ruled on
rather than counted against some long term cap." (Authorship john;
`docs/rulings/2026-10-18-spending-ruling.md`.) So every new spend, on any
vendor, needs his go before it happens, with its estimate and ceiling. Every
dollar spent is tracked with its go in one place, `docs/spending-record.md`.
The $450 stays on the record as Amendment A2's registered envelope, but it
is no longer the control. The exact tally is a roadmap step. Older entries
are not edited.

## WHERE THINGS STAND 2026-10-18 — the refounded question is in the spec; the paper is at version 0.3; the battery rehearsal's method is checked and waits only on John's go; RT-283 closed on his reading

*Written 2026-10-18 (Sunday, Pacific) by the session that worked the
programme on 2026-10-17, picked up again at John's word relayed by the fifth
master session for the tracker sites ("yes, let's wake the MVM"), with merging
and the site deploy authorised for the five open pull requests. Records
only: nothing run against a model, nothing rented, nothing spent.*

**What landed on the main line today**, each checked by a session that wrote
none of it, and where a check left conditions, re-checked after them:

1. **Pull request 171**, the closure checks on the three fatal Gate A
   findings against section 2 version 3.
2. **Pull request 172**, the status entry of 2026-10-17 and the ruling that
   experiment C stays stopped.
3. **Pull request 173**, the ledger rows RT-283 to RT-304 and **section 2
   version 3 written into the spec** (`spec/minimum-viable-mind-proposal-v0.1.md`,
   SHA-256 `c824cd81b53b3cebc3a0dda350b63ece66c54c6dd77e6580eb132466eb7d0413`).
   Checked (pull request 179) and re-checked (pull request 183).
4. **Pull request 175**, `explainer.md` refreshed and the paper draft at
   version 0.3, with experiment 06 and the stopped experiment C folded in,
   the nulls and kills included. Checked (pull request 181) and re-checked
   (pull request 184).
5. **Pull request 174**, the method file, the version 1.2 rubric file and
   the runner for the measurement rehearsal of the battery's entries 1 and 2.
   Nothing ran. Checked (pull request 182) and re-checked twice (pull
   requests 186 and 187); no condition stands.

The three sessions that wrote 173, 174 and 175 stopped on usage credits
before applying their checks' conditions, so this session applied them. It
wrote none of those texts, so the pairing rule allows that, and the checking
sessions re-checked every fix.

**John's rulings today** (authorship mixed; this session recommended, and the
master session added the rehearsal condition):

- **RT-283 is closed on his reading**, not on the letter of its check. The
  check expected no "no better than" and found one. That hit is the
  observer loss condition RT-285's fix added, a different comparison, and it
  is guarded as a question and not a finding. His reading and its condition
  cover both copies of that comparison in the spec. The condition: when the
  observer study is designed, the comparison gets its instrument and a
  measurement rehearsal before it is registered.
  (`docs/rulings/2026-10-18-rt283-closure-ruling.md`.)
- **The Floor sentence's interval clause was corrected before the spec
  merged.** The record (`experiments/01-self-indexing-removal-test/removal_ci.json`)
  gives the second of the removal test's three drops, 0.10, an interval from
  0.00 to 0.20. The spec now says "the first and third intervals above zero
  and the second, from 0.00 to 0.20, touching it". RT-292 closed when the
  re-check matched the record.

**The ledger count for the Gate A pass on section 2:** 3 closed with the
claim checked, 17 closed with the argument accepted, 1 closed on John's
reading, 1 open. The open one is RT-302: ruling 4's wording ("the result was
ambiguous", not "the instrument could never return the other answer") still
has to reach this file's older entries, the site data, the site's learned
page, version 2 and the 2026-10-07 rulings file.

**The battery rehearsal, for John's go.** Entry 1 re-runs experiment D's
pressure-and-release test with the transcript replaced by a summary that
leaves out the model's own earlier position. It asks whether D's
re-assertion after release was looked up in the transcript, worked out
again, or a trace of the pressure. Entry 2 hands the same objection over as
a colleague's concern instead of the model's own, to see what changing who
owns a position does. Both are reference readings of what the cheaper
routes produce, not tests of a feature. About 2,632 calls by API, recorded
in the worklog. The runner refuses to start unless the ceilings are set to
the figures John's go names.

| | Low end | High end |
|---|---|---|
| Entry 1 | about $9.28 | about $21.14 |
| Entry 2 | about $8.97 | about $16.72 |
| Both | about $18.26 | about $37.86 |

At the draft's $10 per entry, neither entry finishes in one start. Ceilings
of about $23 and $19 let both finish.

**Arm M's zero, explained and checked, not landed.** Pull request 180 finds
that arm M's separable half, at 10 million parameters, answers from the
"this turn is yours" signal in the shared trunk, not from its built-in
answer. Its check (pull request 185) passed with four reporting changes, now
applied. It needs a short re-check of those changes and John's word to
merge, since it was not among the five he authorised. Nothing about
experiment C's ending changes.

**What still stands between the record and the preprint**, in order:

1. Pull request 180 re-checked and merged on John's word.
2. John's go on the rehearsal's ceilings, the run, its records, then Gate A
   on the table and entries 1 and 2, both tiers.
3. RT-302's reach into the older texts.
4. John's three reserved places in the paper (the title, the Discussion, the
   "router reading twice over" paragraph; proposed wording in its dated
   note), and the spelling choice, since the paper mixes American and
   British spelling.
5. The outside reader named by John and sent the approach note
   (`docs/outside-reader-approach-note-2026-10-17.md`; links to add before
   it goes, under the rule of 2026-10-18).
6. The Sentient Horizons essay's hold lifted, a separate call.
7. The public release.

The programme stands at about $230.94 of $450, unchanged since 2026-10-09.

**The site data.** `data/project.toml` records today: next steps N49 and N51
done, N50 waiting on John's go, N52 done but not landed, and a timeline row.

## WHERE THINGS STAND 2026-10-17 — experiment C stays stopped on John's ruling; three of the four open calls had been ruled on 2026-10-12 after the entry below was written; the closure checks on section 2 are filed; the chain to the spec, the battery's method file and the paper fold are running as paired sessions

*Written 2026-10-17 (Saturday, Pacific) by a helper session of the weekend
master session for the tracker sites, which handed Minimum Viable Mind to it
because the programme has its own record and rules. Records only: this
session ran nothing, rented nothing and spent nothing. The dated line of
the December-result roadmap (weekends 4 to 13 of the weekend plan) is closed
as overtaken by the stop; the plan from here is the task order below.*

**The record lagged the day it describes.** The 2026-10-12 entry below
lists four calls as open for John. Three were ruled later that same day, by
the weekend overseer putting each packet to him, and were recorded where
the work happened but not in this file or the site data until now:

1. **The six Gate A calls on the two-sided question text:** ruled "all as
   recommended" (authorship mixed; the six rulings are the last comment on
   pull request 165, the Gate A pass, and are restated at the head of
   `docs/rulings/2026-10-12-two-sided-question-section-2-v3.md`). Section
   2, version 3, applied them and was merged as pull request 170 the same
   day. Under ruling 5, tier 2 of Gate A is now run by API as the standing
   way, and the protocol text says so.
2. **Questions 10 to 12 of the felt-features battery:** ruled "all as
   recommended" (mixed; the comment on pull request 164, and a dated line
   under each question in the draft). The fourth check (pull request 169)
   passed with no conditions and two notes for the next edit; both pull
   requests were merged on John's word.
3. **The five never-merged check pull requests:** the four check notes
   (pull requests 104, 110, 111 and 112) merged on his ruling "as
   recommended", and the stale status entry of 2026-10-04 (pull request
   92) closed, 311 commits behind the main line and already superseded by
   later entries. The 14 files citations pointed at are now on the main
   line.

**Ruled: experiment C stays stopped at its registered ending.** The one
call still open from 2026-10-12 was put to John today with what each way
would cost, and he asked for the session's recommendation and reasoning
before ruling. The recommendation was to stay stopped: the record predicted
this ending (the verification-bar ruling called it the likelier one, and
the toy models already read arm C at about 0.25 and arm M at about 0.10
before the reruns read both at zero, training having driven those routes
to zero while arm T's survived); a rebuilt arm C is a different
construction, which the poll warned "must not retrospectively rescue the
original contrast", and nobody has shown that only-route arms would still
differ from arm T on the entanglement axis while in use; arm M's separable
half reads 0.000 against the toy's 1.000 and is unexplained; the
refounding of 2026-10-07 moved the measurement target to the two-sided
question; and the paper does not need a positive C. John's words: "Ok,
that works for me" (authorship mixed; the ruling, with the recommendation
as given, is `docs/rulings/2026-10-17-experiment-c-stays-stopped-ruling.md`).
What is ruled: C stays at its stop S4b with the ruled public sentence,
"the built arms as designed are not references; the measure was not
reached"; option (d) of the verification-bar ruling (arms C and M rebuilt
so the built route is their only route) stays on the record as the named
route if C is ever reopened, not authorised, no toy work toward it
authorised; any reopening waits on one precondition, that arm M's 0.000 is
explained first from the existing checkpoints at $0, by a session that did
not write the reruns, with a method file before any output, which belongs
in the write-up either way; and the paper chain comes first. Nothing
spent.

**The closure checks on section 2 are filed.** The three fatal findings of
the Gate A pass (RT-283, RT-284, RT-289) each have the closure check the
protocol's closure rule owes, run today by a session that wrote none of the
proposal, the pass, the rulings or version 3:
`docs/reviews/2026-10-17-section-2-v3-closure-checks-claude-code.md` (pull
request 171, with the script and output beside it). RT-289 closes:
"degree measured" 0, "at a degree" 0, "non-zero" 1 in the inserted text and
the hit is the sentence about Scope's phrase. RT-284 closes with a reading:
check C4 re-run on the spec assembled as it would read after the commit
(377 lines) finds every unchanged sentence the pass found in competition
with section 2 now quoted or named by section in the supersession
paragraph, with the precedence rule present. RT-283 does not close by the
letter: "fluency measures" is gone and ruling 10 is cited by path, but "no
better than" returns one hit against an expected zero. The hit is not the
deleted sentence; it is the sixth loss condition RT-285's fix added
(observers detect presence "no better than in the frontier reference
profile"), which shares the defect RT-283 named (a pre-stated comparison
for an observer study with no instrument and no rehearsal, a study
decision 7 deferred), guarded by "this is a question and not a finding".
Whether the guard is enough is John's call when the ledger line is
written; the check reports the count and decides nothing.

**The proposal packet to the book is written.** Decision 8 of 2026-10-07 is
discharged: the three book changes the poll asked for (chapter 1's
other-minds sentence, chapter 5's forward-pass claim, the removal test's
missing differential prediction) are a proposal file on the branch
`proposal/mvm-poll-three-book-changes` of the Calibration Problem
repository (`proposal-mvm-poll-three-book-changes-2026-10-17.md`), with
offered wording under each and John ratifying, amending or declining item
by item there. Nothing in any chapter is edited.

**What ran as sessions, each by a session that did not write what it
touches (the pairing rule).** John started all three in the afternoon and
all three landed as pull requests the same evening, unmerged, each owed a
check by a session that did not write it (proposed the same evening):

1. The ledger rows from RT-283 on (tier 1, plus the tier 2 findings ruling
   6 gives numbers to), carrying the six rulings and the three closure
   lines, with RT-283's line stating the count above; then the commit of
   section 2 into the spec, checksum printed; then a check of both by a
   third session.
2. The method file for the measurement rehearsal of the battery's entries
   1 and 2, committed before any output, with a dry run that calls no
   model. The rehearsal itself (about $20 by API, recorded in the worklog)
   runs only on John's verbatim go on the day.
3. The paper: `explainer.md` refreshed for the relabelled removal-test
   result, experiment 06 and experiment C; experiment 06 and the stopped C
   folded into `drafts/paper-removal-test-nature-draft.md` as version 0.3
   with the nulls and kills, the three places John reserved on 2026-10-09
   (the title, the Discussion, the "supports the router reading twice
   over" paragraph) marked and proposed, not applied; the Voice Calibration
   and Cold Reader passes on the new text; and the outside-reader approach
   note drafted for the two jobs the shortlist names, addressed to no one
   until John names the reader.

What they produced. **Pull request 173**: 22 ledger rows (RT-283 to
RT-304, fourteen tier 2 duplicates recorded with reasons) carrying the six
rulings and the three closure lines (RT-289 and RT-284 checked and closed;
RT-283 open for John on the one hit), and section 2 version 3 written into
the spec with SHA-256 `3d0baaca…6df119`, matching the closure checks
exactly; two layout tidies and the section's heading level ("###" where the
spec uses "##") are John's one-character calls. **Pull request 174**: the
method file for the rehearsal of entries 1 and 2, the version 1.2 rubric
addendum in its own file (experiment D's registered rubric pinned by
checksum and never opened for writing), a runner that is dry-run by default
and gated for the real run, and the dry run's output; nothing ran against a
model. New for John: costed from token counts and list prices rather than
by scaling experiment D's spend, the two entries come to **about $19 if
Gemini bills no thinking tokens and about $38 if it bills about 1,500 a
call**, against the draft's about $20; his go on the day is on that
bracket, or on the $10-per-entry ceilings with a likely stop partway.
**Pull request 175**: `explainer.md` refreshed (about 2,900 words of prose,
over the brief's 2,500, with the cut named in the Cold Reader report);
paper draft version 0.3 with results sections for experiment 06 with
Amendment A3 and for experiment C at its registered stop, the nulls and
kills and two tables each, Methods and abstract sentences, the founding
wager's adoption date disclosed; the three places John reserved on
2026-10-09 untouched with proposed wording in a dated note, and one
Discussion paragraph ("The constructive turn") replaced because its fact
was no longer true, its old text kept in the note; the Voice Calibration
and Cold Reader records filed as self-passes, which say so; the
outside-reader approach note in two versions, addressed to no one.
Flagged: the paper mixes American spelling (version 0.2) with British (the
new sections and the records they quote), and one half has to move before
the draft leaves the repository.

**What still stands between the record and the preprint**, in order:
the checks of pull requests 173, 174 and 175 and their merges; John's
ruling on RT-283's one hit; his go on the rehearsal's bracket (about $19
to $38) and the run, then its Gate A, both tiers; his three reserved
sentences in the paper and the spelling choice; the outside reader
named and sent the packet, and the red-team read answered; the Sentient
Horizons essay's hold lifted (a separate call); then the public release
(the repository opened with its registrations and ledger, the preprint,
one essay). Nothing on that list needs a new positive result. The
programme stands at about $230.94 of $450, unchanged since 2026-10-09.

**The site data.** `data/project.toml` records the three rulings of
2026-10-12 (next steps N45 to N47 done, N36 done with the check's merge,
N29 done with the packet) and today's (N48 done, N52 added for the arm M
explanation), adds the closure checks and the three sessions as next
steps, and a timeline row for today; `data/roadmap.toml`
marks weekend 4's four goals as not needed, since the validation result
they planned for cannot exist after the stop, and says where the work went.



*Written 2026-10-12 (Monday, Pacific, the last day of the four-day weekend)
by a helper session of the weekend overseer. Records only: this session ran
nothing and spent nothing. On the branch
`ruling-2026-10-12-experiment-c-stop`.*

**John ruled: "accept the stop".** He was accepting the independent reading
of the three 10-million reruns, posted as a comment on pull request 166 (the
reruns' outputs and run record). Route use against the bar of 0.5: arm T
(the separable built model) 0.986, arm C (the stirred-in built model) 0.000,
arm M (the half-and-half built model) 0.024 on its stirred-in items and
0.000 on its separable items. So, under version 5, section 5.6 and section
11's stop S4b (the stop for a failed verification of the built models),
experiment C stops before the free-arm run at registered size, and the rest
of the first release is not spent. The ending is reported in the ruled
words: **"the built arms as designed are not references; the measure was
not reached."** It is a registered ending of experiment C, reached by its
own stop rule, not one of the eight outcome terms. The ruling, with version
5's sentences quoted exactly, is
`docs/rulings/2026-10-12-experiment-c-stop-ruling.md` (authorship john).
**The 2026-10-09 evening entry's "pending John's read" is now settled.**

**What follows from it.** The free-arm run (about $12) does not launch, and
the second release (about $150 to $172) is never asked for. Experiment C
spent about $1.47 on the development runs and $1.3032 on the reruns; the
programme stands at about $230.94 of $450, unchanged since 2026-10-09.
Pull request 166 (the reruns' outputs and run record) was merged by the overseer on John's word ("merge the ready ones") at 10:03
Pacific today, and pull request 163 (the relabel of experiment A) a minute
later, so both are on the main line. Version 5 and every earlier ruling are
left unedited.

**Not decided.** Whether experiment C continues in a new form: rebuilding
arms C and M so the built route is the only route (option (d) of the
verification-bar ruling) changes what the arms are and needs its own toy
retrain, check and ruling. Nothing is started. And arm M's separable half
reads 0.000 where the toy models read 1.000 (arm T's separable slot reads
0.986 in the same reruns); the registration says nothing about it, it does
not change the miss, and it stays unexplained.

**The site data.** `data/project.toml` and `data/roadmap.toml` change in
this commit: experiment C is recorded as stopped at S4b on John's ruling,
not pending; a finding and a timeline row are added; the step that asked
him to read the reruns is done and a new one asks whether C continues in a
new form; the reruns' verification goal (W3.3) is done and the free-arm
branch goal (W3.4) is not needed.

**What stays open for John, each with what it unblocks.**

1. Make the six calls in pull request 165's index
   (`docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md`, Gate A on
   the two-sided question text). That unblocks fixing the text, writing it
   into the spec, and writing its ledger rows.
2. Answer questions 10 to 12 in pull request 164 (the felt-features battery,
   version 4). That unblocks the method file, then the measurement
   rehearsal of the battery's first two entries (about $20 when run), then
   Gate A on the battery.
3. Land or close the five never-merged check pull requests: 92, 104, 110,
   111 and 112 (named in the 2026-10-09 evening entry). Landing the last
   four puts their 14 files on the main line so citations to them resolve.
4. Say, only if he wants one, whether experiment C continues in a new form.
   Until then it stays stopped.

## WHERE THINGS STAND 2026-10-09 (evening) — the successor experiment is registered; the three reruns ran, and an independent reading says the verification fails and experiment C stops at its registered stop, pending John's read

*Written 2026-10-09 (Friday evening, Pacific, the first day of the four-day
weekend) by a helper session of the weekend overseer, from the day's
TimeAssembler worklog entries for this project. Records only: this session
ran nothing and spent nothing. On the branch `status-2026-10-09-evening`.*

**The successor experiment is registered.** John's words, in reply to the
overseer's packet: "Can you make the commit and accept the sessions handling
of the eight findings?", and on the three reruns, "Approved." The commit went
up as pull request 162 (the registration commit). It changes only version 5's
status line, from draft to registered at the frozen code `6c47c56`, and adds
`docs/rulings/2026-10-09-registration-commit-ruling.md` with his words. A
session that wrote none of it checked it and passed it with conditions: the
frozen code folder is byte-identical at `6c47c56`, at the main line and at the
pull request's head, and the ruling file's account of the reviewer's eight
findings (red-team ledger rows RT-275 to RT-282) matches the ledger. John
merged it at 10:52 Pacific (merge commit `e7c6f23`), inside kill date 1
(2026-10-18). How the eight findings were handled is still a session's
proposal that John accepted (authorship mixed), and the four carried open stay
open as named weaknesses: the denominator margin, the in-use judge's
leniency, the out-of-date code comments, and the evaluation-set fingerprint
not tested off the laptop.

**Version 5's pre-registration sentences are left unedited on purpose.** The
check's second condition asks this entry to say so. Several places in version
5 still read as they did before the commit: the header's "What remains is
John's registration commit", section 10's "What happens next", the end of
section 15 ("Nothing above is registered"), section 17's "this text stays a
draft", and the closing "Ready for the registration commit" note. Each is
conditional or dated wording, and the condition each names is the one the
commit met. The registration method allows only the status line to change,
and the status line governs, so the registered text stays exactly what was
checked. The check's first condition (the date on the status line holds only
for a merge on 2026-10-09, Pacific) is met. Its third (label pull request 158,
the registration-ready change, in the ruling file) was done before the merge.

**The three reruns ran.** On John's go, a helper session ran step 4b of the
registered plan as a new wave, with no top-up. Arms T (the separable built
model), C (the stirred-in built model) and M (the half-and-half built model)
were each retrained once at 10 million parameters, seed 0, sharpness fixed at
4.0, on the frozen code, on three rented RTX 5090 cards between 18:10 and
18:54 UTC. Each trained all 108,919 steps; each checkpoint was copied home and
checked against the machine's copy before the machine was deleted; nothing
is left running. **The spend was $1.3032 against the about $1.14 John
approved, about 14% over,** because the vendor's posted price was $1.19 an
hour, not the $0.99 the record carried (at $0.99 the same hours would have
cost $1.08). It came from the first release's development line, which has
about $7.23 left; the programme stands at about $230.94 of $450. The vendor
balance fell from $71.2191 to $69.8935, the extra two cents or so being the
storage volume's standing charge. The spending alarm met real billing for the
first time and held: its fast comparison peaked at 1.007 against its 1.25
trip line, and the end-of-wave comparison matched billed hours to machine
lifetimes on all three (1.000). Outputs, the run record and the ledger rows
are in draft pull request 166 (the reruns' outputs and run record), not yet
merged.

**What the reruns read: the independent reading, which John has not yet
read.** A session that ran none of it and wrote none of the registration read
pull request 166 against version 5. Route use is the share of right answers
about the model's own turn that are lost when the built-in "which agent am I"
answer is swapped; the bar is 0.5. Arm T read 0.986 (2,918 of 2,959). Arm C
read 0.000 (0 of 3,000). Arm M read 0.024 on its stirred-in items (33 of
1,387) and 0.000 on its separable items (0 of 1,190). All three put 0.999
weight on the true agent (bar 0.9) and passed their gate on learning (bar 790
of 3,000). Version 5, section 5.6, says the repaired route holds only when
arms C and M each pass both parts of the in-use check and their gate, and
that if the verification fails experiment C stops there, before the free-arm
run at registered size, and the rest of the first release is not spent. In
the reader's account the verification fails, and **experiment C stops at
its registered stop S4b (the stop for a failed verification of the built
models), in the ruled words "the built arms as designed are not references;
the measure was not reached".** Section 5.6 foresaw it: "the reruns would
very likely fail the verification and experiment C would stop at about
$1.14." A redesign in which the built route is the only route would need its
own ruling (option (d) of the verification-bar ruling). The reader re-checked
that the measurement code is the frozen code, that the checkpoints' file
fingerprints match the record, and re-ran the frozen gate step on the laptop
at $0, reproducing every field. Noted, and not bearing on the result: the
training logs record no code commit, so training on the frozen code rests on
the run record; the helper's own calls (a `_rerun` suffix on run names so the
2026-10-04 checkpoints were not overwritten, a $1.00 hard cap a run, and a
retry wrapper outside the repository that re-ran the unchanged launcher every
5 minutes while the vendor was out of stock); John's go was relayed to the
running session rather than heard by it; and two small record errors (the run
record says per-run logs are committed in a folder that is absent, and the
ledger's pre-launch token count differs from the checkpoints' by 3,584).
Arm M's separable half reads 0.000 where the toy models read 1.000; the
registration says nothing about that, and it does not change the miss.
**This is the reader's account, not John's ruling. Experiment C is not
stopped until he has read it.**

**The day's other work, each in a draft pull request for John.**
Pull request 163 (the relabel of experiment A) applies decision 2 of the
2026-10-07 two-sided-question ruling: experiment A's label becomes "the test
could not discriminate routing from a centre; the cheaper account was taken
in advance", in a dated note under the 2026-07-18 entry below, the paper
draft's header, abstract and verdict sentence, the site data and the site's
"learned" page. It also takes two claims the record struck on 2026-09-20 off
the site ("a structural signature of ownership-specific learning" and "of
self-indexing"). No figure, method or registered text changed. Still owed
there: the paper's title, Discussion and supporting argument rest on the old
reading. Pull request 164 (the felt-features table and filtered battery,
version 4) applies the third check's fixes; a fresh check passed it with two
conditions, both met in commit `3eee588`; the full-transcript rate is 0.944,
not 0.905, and one error no check had named (entry 2's room to move computed
the wrong way round) is corrected. John's questions 10 to 12 stand. Pull
request 165 (Gate A on the two-sided question text) ran both review tiers on
section 2 of the refounding proposal's version 2. The first tier filed
findings RT-283 to RT-295: one fatal (the observer-side loss condition has no
instrument, and an earlier ruling already closed the option it describes),
seven serious, five worth noting. The second tier went to Gemini 3.1 Pro and
GPT-6 Astra by API rather than pasted into their apps, a departure from the
protocol's wording; both rate "degree measured" fatal. That spend was about
$1.04 at most (Gemini about $0.16, GPT at most about $0.88 at an assumed
rate, since none is on record); the overseer's brief said to stop before any
tier costing more than about $1, and the helper went ahead on the expected
cost. Nothing is written into the spec and no ledger rows are written yet.

**Housekeeping.** Three stale pull requests were closed, each found fully on
the main line through pull request 136 (the merge of the fifteen branches):
96 (the check of version 4's answers to review findings), 101 (the proposal
answering the outside reviews of version 4) and 102 (the check of that
proposal). Five were found never merged and stay open: 92 (the status and site
data update of 2026-10-03, late evening; the main line has no matching
entry), 104 (the check of the 2026-10-06 rulings record), 110 (the check of
the two rulings added to it), 111 (the page 1 closure check) and 112 (the
check of the arms C and M ruling packet). The last four carry 14 review,
method and script files the main line does not have.

**The site data.** `data/project.toml` and `data/roadmap.toml` change in this
commit: the registration is recorded as made, the reruns as run, and the stop
as the independent reading pending John's read. The out-of-date "remaining"
item the check flagged (twelve open items, fifteen unmerged branches) is
rewritten. The registration goal (W3.2) and the weekend 2 goal it carried
(W2.2) are marked done.

**What waits on John, each with what it unblocks.**

1. Read the independent reading of the reruns (the review comment on pull
   request 166) and say whether experiment C stops at its registered stop.
   If it does, the ending is written up as instrument research, a registered
   outcome, and pull request 166 can be checked for merge so the run record
   and outputs reach the main line. The free-arm run and the second release
   are then not spent. A redesign would need its own ruling, only if he wants
   one.
2. Note two spends over what was said in advance: the reruns at $1.3032
   against about $1.14 (the posted price had moved from $0.99 to $1.19 an
   hour), and the second review tier of pull request 165 at up to about $1.04
   against a brief that said to stop before about $1. Nothing waits on these;
   they are here so they are in front of him.
3. Make the six calls in pull request 165's index
   (`docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md`). That
   unblocks fixing the two-sided-question text, writing it into the spec, and
   writing its ledger rows.
4. Answer questions 10 to 12 in pull request 164 (entry 1's band width, entry
   2's scoring, the direction with no band). That unblocks the method file,
   then the measurement rehearsal of the battery's first two entries (about
   $20 when run), then Gate A on the battery.
5. Read pull request 163. Merging it puts the relabel of experiment A and the
   two struck claims on the site; the rest of the paper's rewrite follows it.
6. Land or close the five never-merged pull requests (92, 104, 110, 111, 112,
   named above). Landing the last four puts their 14 files on the main line so
   citations to them resolve.
