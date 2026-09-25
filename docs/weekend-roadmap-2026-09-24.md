# MVM weekend roadmap to 2026-12-21 (written 2026-09-24, Pacific)

*Drafted in the Cowork session of 2026-09-24 at John's request: review the
state of the project and lay out the route to the strongest research
conclusion reachable by 2026-12-21, as a weekend-by-weekend plan that gets
re-planned every week. Nothing here is a ruling. It is a schedule laid over
the December-result roadmap (`docs/december-result-roadmap-2026-09-20.md`),
which stays the document of record for what the work is, what counts as a
result, the two kill dates and the money. Where this document and that one
disagree, that one wins. Written under the workspace plain-language rule.*

*Mirrored as the TimeAssembler project document of the same name. The
TimeAssembler roadmap carries one step per weekend, due on the Sunday, so the
"Up next" view matches this table. Re-plan every Thursday or Friday evening
from the current top of `STATUS.md`; edit this file and the TimeAssembler
steps together.*

---

## 1. Where the project stands on 2026-09-24

The measurement line that runs to December is the successor experiment: train
one small model three ways on the same matched-role task (arm T, built so its
"which agent am I" answer sits in a slot of its own; arm C, built so that
answer is stirred through everything; arm F, trained freely), and test whether
a decomposability measure (how much accuracy is lost when only the ownership
answer is transplanted, against transplanting the whole state) can tell T
from C. If it can, arm F gets the programme's first degree reading. The
registered outcomes are R1 (measure validated, degree read), R2 (measure does
not separate T from C), R3 (an arm fails the learn-both gate), and R4 (nothing
trains; a schedule failure, not a scientific one).

What is finished:

- Amendment A3 (the earlier constructed self-index experiment) has its
  closure text at version 4, passed the first review tier with all six fatal
  findings ruled, and the second-tier packets are built and merged for the two
  outside reviewers. What remains on A3 is John's two reviewer sessions, the
  drafted rulings, and the closure commit.
- The successor proposal version 1 exists, went through its Gate C review
  (two fatal findings: the measure's formula divides by an uncorrected
  accuracy, and one control's first cell is empty by construction), and the
  measurement rehearsal has since settled both by measurement rather than
  argument. The rehearsal also found the defect that was blocking
  registration, the nomination step never said what its straight-line read is
  fitted against, and John ruled it on 2026-09-23: which marker word.
- Two rulings of 2026-09-23 are on the main line (PR 28). The launcher now
  refuses arguments, the reaping race is fixed, seven protocol amendments are
  landed, and two checking scripts (`scripts/check_citations.py`,
  `scripts/check_single_source.py`) make the closure rule mechanical.

What is open, and blocks registration (all listed in section 11 and 12 of
`docs/2026-09-21-successor-measure-rehearsal.md`):

1. Eight numbers only John can set: the separation bar between T and C, the
   learn-both threshold per condition, the floor on whole-state transplant
   accuracy (stated relative to the arm's own accuracy), the rank cap on the
   nominated subspace, the candidate site family, the seed count per arm, the
   paired-uncertainty method, and the ownership-lesion collapse threshold. The
   rehearsal measured behind each one; none is a close call except the seed
   count, which should carry a discount because toy arms are more repeatable
   than 30-million-parameter runs (the entangled and free toy arms already do
   not reproduce; ruled 2026-09-23: quote them as a range and a direction
   only).
2. Which form of the measure's arithmetic is registered: the proposal's form,
   or the chance-corrected form the rehearsal showed recovers the true value.
3. The nomination procedure is not one instrument across arms (the winning
   label changed between arms before the label was fixed). The label is now
   fixed; the procedure still has to be shown to behave identically on every
   arm.
4. The named-other condition does not learn at toy scale, and doubling its
   budget moved it about a point. This is the cheapest thing the rehearsal
   found that could sink the registered experiment (outcome R3 on the first
   run). Redesign it, or accept the risk on the record.
5. The middle of the scale: the free toy arm reads at the entangled anchor,
   not between the two, so a free-arm reading there cannot be told from a
   ceiling. Either a fourth arm built to be partially separable, or an
   admission in the registration text.
6. Three text repairs to the proposal with a measurement behind each, and
   control 2 built as the proposal states it rather than as it was run.
7. The rented slice (about $1, one rent, two answers: seconds per step per
   arm on the rented machine, which is the whole of the second release's
   arithmetic). Its earlier go lapsed under the launcher-guard ruling; it
   needs a fresh spoken go naming it.
8. The spend ruling: the $130 successor cap is $12 short of its own plan, the
   two releases come to about $175 against about $172.40 of headroom (about
   $2.60 over), and pre-authorisation needs an anomaly tripwire
   (`docs/preauthorised-spending-proposal-2026-09-21.md`). Under the standing
   rule this is proposed with the number, not worked around.
9. Smaller items on the queue: do the Wittgenstein criteria enter the
   proposal or wait for resumption; correct or annotate the unreproducible key
   count in the independent A4 review; how to correct a measured value in
   registered text whose cited record does not contain it; make the launcher
   refuse to rent when the laptop can sleep.

Bookkeeping owed (updated 2026-09-24 evening: the 2026-09-22/23 handoff
landed as PR 29 and a 2026-09-24 evening entry as PR 31, so `STATUS.md` is
current): the 69 agent worktree folders are all merged but none is prunable
by git's definition, so clearing them is a `git worktree remove` pass, not a
prune; two redundant draft files sit outside the repo at
`~/Code/MVM-handoff-2026-09-24-STATUS-entry.md` and its project.toml patch,
John's to delete; the site's two Cloudflare secrets and the repository
visibility flip are John's; and the TimeAssembler mission line still carries
"working toward a publishable result", which the 2026-09-20 ruling struck.

Money: about $227.60 of the $400 envelope is spent, about $172.40 left (from
the ledger's rows, via the 2026-09-22 notes). No compute is in flight and none
is authorised.

> **Note added 2026-09-24 (evening), after the check of the ruling packet
> (draft pull request 35).** Every "about $12 per run" and the figures built on
> it in this document ($96 for eight runs, $36 for three) were carried from the
> December-result roadmap, whose source is the compute ledger's planning guide.
> That guide gives $12 for all registered training at an earlier size and the
> ledger itself calls it out of date. The figure survives only as an estimate
> resting on the measured actual-after rows for single 30-million-parameter
> runs in `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`
> (about $9.9 for the control-learnability pilot and about $13.92 for the A3
> pilot), and the rented slice's seconds-per-step measurement is what replaces
> it. Nothing else in this document is changed by the note.

## 2. The constraint this plan is built around

Weekdays carry rulings and spoken go's only, fifteen to thirty minutes on some
evenings, from a queue that a session has pre-assembled. Weekends carry the
sessions John runs by hand (two outside reviewer sessions per gate, about an
hour each) and the launches. Agents run unattended between weekends, and the
Mac can run local work (nomination, transplants, fitted reads) midweek as long
as nothing else needs it.

Working weekends between now and wrap-up, with what sits beside each:

| # | Weekend (Pacific) | Days | Beside it |
|---|---|---|---|
| 1 | 2026-09-26 to 27 | 2 | Book lock 2026-09-30 is off the table (done or moved) |
| 2 | 2026-10-03 to 04 | 2 | |
| 3 | 2026-10-10 to 12 | 3 (Columbus Day) | Field exercise 2026-10-13 to 14 follows (blackout, tentative) |
| 4 | 2026-10-17 to 18 | 2 | **Kill date 1, Sunday 2026-10-18: registration committed** |
| 5 | 2026-10-24 to 25 | 2 | |
| 6 | 2026-10-31 to 11-01 | 2 | **Kill date 2, Sunday 2026-11-01: the remaining eight runs launched** |
| 7 | 2026-11-07 to 08 | 2 | Field exercise 2026-11-10 to 11 follows |
| 8 | 2026-11-14 to 15 | 2 | Mini CSS 2026-11-18 to 19 and the mile retest 2026-11-20 follow |
| 9 | 2026-11-21 to 22 | 2 | |
| 10 | 2026-11-26 to 29 | 4 (Thanksgiving) | |
| 11 | 2026-12-05 to 06 | 0 | **Blackout: Mini CSS 2026-12-04 to 08** |
| 12 | 2026-12-12 to 13 | 2 | Inside the post-field recovery window; plan light |
| 13 | 2026-12-19 to 20 | 2 | Wrap-up starts Monday 2026-12-21; nothing new launches after it |
| — | 2026-12-21 to 2027-01-03 | exodus break (dates inferred) | Hibernation work only: records, write-up, resume file. Complete by 2027-01-04 |

That is twelve working weekends, twenty-seven days, and about 50 John-hours if
each weekend costs three to four. The December-result roadmap's own estimate
of John's load (ten reviewer sessions, six rulings, the launch approvals) fits
inside that with room, so the binding constraint is not his hours; it is the
number of gate round-trips, because each gate costs at least one weekend (the
reviewer sessions and the ruling) and a fatal finding costs a second one.

## 3. The route: critical path by weekend

The principle: front-load everything that needs John into the first three
weekends so that both kill dates pass with their work already done, and
leave the back half of the block for the failure branches and for the
extensions that make the conclusion stronger. Every weekend has one named
outcome; if the outcome lands early, the next weekend's work starts.

### Weekend 1, 2026-09-26 to 27: clear the queue, close A3, repair the proposal

Outcome: A3 closed under Gate A; every registration-blocking decision ruled;
proposal version 2 through its Gate C tier 1 review.

Saturday, John (about three hours):

- Run the two A3 closure tier 2 sessions from the committed packets and file
  both responses verbatim. Rule on the drafted dispositions the same day.
- Rule the pre-assembled queue in one sitting: the eight numbers, the form of
  the measure (recommendation: the chance-corrected form, since it recovered
  the true value and the registered form did not), the named-other condition
  (recommendation: redesign, because the rehearsal showed it is not a budget
  problem and it is the cheapest route to R3), the middle of the scale
  (recommendation: a fourth partially-separable arm if the rehearsal can build
  one inside this weekend at toy scale; otherwise the admission in the text),
  the Wittgenstein criteria (recommendation: wait for resumption unless they
  change the metric spec), the two record corrections, and the spend ruling
  (recommendation: set the successor cap at $142, the figure its own plan
  comes to, with the anomaly tripwire; and rule the programme envelope up
  from $400 to $450, because the base plan already runs about $2.60 past the
  headroom and every extension in section 4 costs about $36 more. Stated
  with the numbers per the standing rule; the alternative is the base plan
  with no extension, which fits only if the rented slice's measurement comes
  in under estimate).
- Give the spoken go for the rented slice (about $1).

Agents, both days, one session writing and a different one checking, always:

- Land the 2026-09-22/23 handoff and a 2026-09-24 entry at the top of
  `STATUS.md`; update `data/project.toml`; prune the worktrees.
- Run the rented slice once the go is given; write the seconds-per-step
  figures into the second release's arithmetic.
- Rehearsal repairs: the named-other redesign measured at toy scale; the
  nomination procedure made one instrument across arms and shown to be;
  control 2 as stated; the fourth arm attempted if ruled.
- Proposal version 2 with the three text repairs, the ruled numbers, the ruled
  label and the ruled form; the failure-modes checklist
  (`docs/known-failure-modes.md`) exercised against it with commands and
  output, not citations; both checking scripts run clean.
- Launcher sleep check (the open roadmap item) landed before any launch.

Sunday: Gate C tier 1 on version 2 in an isolated worktree. If clean, the
registration text (version 2 of the successor proposal, as registered text)
goes to Gate A tier 1 the same night, so it runs unattended midweek.

Optional, ten minutes of John's: the two Cloudflare secrets and the repository
visibility flip, so the site deploys.

Midweek 2026-09-28 to 10-02: Gate A tier 1 on the registration runs and its
packet for tier 2 is built and checked independently. Implementation
(generator, arms T and C, the transplant code) written against the rehearsal.
John rules tier 1 findings from the queue on one evening.

### Weekend 2, 2026-10-03 to 04: register

Outcome: registration committed, two weeks ahead of kill date 1.

Saturday, John: the two tier 2 sessions on the registration (about two hours),
then rule on the drafted dispositions. Agents: text fixes paired-checked,
checklist and citation scripts run on the final text, registration commit
once both tiers are answered and John rules.

Sunday: implementation frozen; unit tests; the even-split rule (RT-58) and the
one-scored-token self-test carried over; development runs at 10 million
parameters (about $10, inside the first release, needs John's go naming them),
launched Saturday night so they land by Sunday; ledger rows opened with
estimates before any machine exists.

If tier 2 returns a fatal finding: the repair and a second tier 1 pass run
midweek and the commit moves to weekend 3, still inside kill date 1.

Midweek 2026-10-05 to 09: development-run results checked by a session that
did not write the code; launch checklist made a gate the launcher checks
(sleep, scheduled fetch and kill, ledger row before the pod); the go packet
for the first registered run assembled.

### Weekend 3, 2026-10-10 to 12 (three days): the first registered run, then all nine

Outcome: every registered run landed, checkpoints local and checksummed, pods
reaped, ledger actual-after rows written. Three weeks ahead of kill date 2.

- Friday night or Saturday morning: John's go naming the single free-arm run
  (step 5a, about $12, about ten hours). It lands Saturday evening.
- Saturday night: the learn-both gate and the ownership-lesion check evaluated
  on the free-arm checkpoint by a paired session; the billing read against the
  ledger's rate.
- Sunday morning, the decision point: if the gate passes and billing is
  normal, John rules the second release and gives the go for the remaining
  eight, launched in parallel Sunday (eight machines, about ten hours each,
  about $96). They land Sunday night into Monday.
- Monday 2026-10-12: fetch, checksum, reap, ledger. Nomination on development
  episodes starts as checkpoints arrive.

If the free arm fails the gate: the one permitted re-run fires Saturday night
on John's go (its money is inside the first release). If it fails again, the
eight are never launched, the roadmap lands on R3, and from this point the
block is spent on the R3 conclusion (section 5).

If billing is anomalous: halt, not trim, per the ruling; restarting is a new
ruling on a later weekend.

Midweek 2026-10-13 to 16 (field exercise 13 to 14): the Mac runs nomination
on development episodes unattended; agents prepare the freeze.

### Weekend 4, 2026-10-17 to 18: the validation result

Outcome: nomination frozen and committed before output; transplants run on
fresh episodes on all arms; the measure computed on T and C; validation
findings drafted; Gate B tier 1 launched Sunday night. Kill date 1 passes with
the registration long committed.

John's load this weekend is light: one ruling if the nomination freeze needs
one, and the queue.

### Weekend 5, 2026-10-24 to 25: Gate B, and the reading if R1

Outcome: John's Gate B ruling on the validation result (R1: read F; R2 or R3:
closure path). If R1, arm F is read on the frozen procedure with confirmation
seeds, locally, starting Saturday night; findings drafted Sunday.

John: two tier 2 sessions on the validation packet, the ruling.

### Weekend 6, 2026-10-31 to 11-01: the reading's findings and its Gate B

Outcome: findings document for the reading (or the null); Gate B tier 1 run
midweek before; John's two tier 2 sessions and ruling. Kill date 2 passes with
the runs landed three weeks earlier.

### Weekend 7, 2026-11-07 to 08: closure text and Gate A

Outcome: the closure text (registered text) drafted the week before, Gate A
tier 1 run midweek, John's two tier 2 sessions and ruling on Saturday, closure
landed in the successor's registration file on Sunday.

At this point the December result exists, six weeks before wrap-up. Weekends
8, 9, 10, 12 and 13 are the room the plan holds for slipped gates (each costs
one weekend) and, if the gates hold, for the extensions in section 4.

### Weekends 8 to 13: contingency first, then extensions

Rule for these weekends, so the choice is made in advance rather than in the
moment: a slipped gate takes the weekend before any extension does; an
extension that needs money is proposed with its number the weekend before it
would run, so the ruling is on the queue midweek; nothing new launches after
2026-12-21.

- Weekend 8, 2026-11-14 to 15: slack, or extension E1.
- Weekend 9, 2026-11-21 to 22: slack, or extension E2.
- Weekend 10, 2026-11-26 to 29 (four days): the state-of-the-programme
  write-up (Cowork), the write-up to the outside human reader (the shortlist
  is in `docs/outside-reader-shortlist-2026-09-19.md`; John chooses and
  contacts), `explainer.md` refresh, site and `data/project.toml` current.
  This is the communication half of the work, which John has said is a
  required part of it, and the long weekend is the right place for it.
- Weekend 11: blackout.
- Weekend 12, 2026-12-12 to 13: light. Records closed with actual-after rows;
  `RESUME.md` drafted; any extension's Gate B ruling.
- Weekend 13, 2026-12-19 to 20: final state of the record before wrap-up;
  nothing launches.
- Exodus break: the hibernation condition per the programme roadmap, complete
  by 2027-01-04; John's final ruling that it is met.

## 4. What "maximum conclusion" adds beyond the registered result

The registered result is one of R1, R2 or R3, and reaching it by weekend 7 is
the plan's job. The extensions below are ranked by how much each strengthens
the conclusion per weekend and per dollar, and each is a separate
registration with its own Gate A. None is authorised by this document. Money
first: the base plan uses all of the $172.40 left in the $400 envelope, so
each extension that trains anything (E0, E1, E3, about $36 each) is an
envelope ruling, not a cap ruling. The $450 proposal in weekend 1 covers the
base plan and one of them; two would be about $490.

- **E0, folded into the main registration if the rehearsal can build it in
  weekend 1: the fourth arm, partially separable by construction.** Without a
  middle case, an F reading at the entangled end cannot be told from a
  ceiling, and the conclusion would be "F is not separable" rather than "F
  reads at degree d". This is the single change that most improves what R1
  can say. Cost: one more architecture, three more 30-million-parameter runs
  (about $36), which does not fit the $400 envelope and is why the envelope
  ruling is put to John in weekend 1 rather than discovered in weekend 3.
- **E1, if R1: tighter uncertainty on the free arm's degree.** Three more
  free-arm seeds (about $36) so the reading carries a paired uncertainty
  across six seeds rather than three. Proposed with its number after Gate B
  in weekend 5; runs in weekend 8; read midweek; findings and a short Gate B
  by weekend 9.
- **E2, if R1 or R2, $0: a second point on size.** The 10-million-parameter
  development checkpoints already exist; reading them on the frozen procedure
  gives the measure's behaviour at a second size at no cost. Runs on the Mac
  midweek; registered as a side reading, not a claim.
- **E3, if R3 (an arm fails the learn-both gate twice): one registered recipe
  change, not hibernation.** The rehearsal already says the named-other
  condition is the likely failure and that its budget is not the cause. A
  single registered follow-up (the redesigned condition at 30 million
  parameters, three free-arm seeds, about $36, through Gate A) turns R3 from
  "this recipe is not a testbed" into "this recipe is not, and this one is
  (or is not)". Proposed in weekend 3 if the branch fires, registered by
  weekend 5, run in weekend 6, closed by weekend 9.
- **E4, deferred, $0 but seventy processor-hours: the marker-word fitted
  read on the A3 checkpoints.** The registered A3 target that was never read
  at the nine positions. It runs unattended on the Mac and costs John nothing,
  but it competes with nomination and transplants for the Mac in October, so
  it runs in November midweeks only if the main line has finished with the
  machine. It does not bear on the December result and is on the list only
  because it is free.

Not on the list, because each is bigger than the block: option D (the
scaffolded name-keyed grammar), the frontier deliberative-gap pilot, Stage 3,
the construction project. They stay deferred to resumption after May 2027.

## 5. What ends the December result, and what the plan does about each

- **A second stop like 2026-08-31 to 09-14.** The plan puts every item that
  needs John on a queue a session assembles, so a weekday evening's fifteen
  minutes moves the chain; and the Thursday or Friday re-plan is the standing
  check that the coming weekend has a named outcome. If a weekend is lost,
  the next re-plan says which of weekends 8 to 13 absorbs it, out loud.
- **The named-other condition fails at 30 million parameters.** Attacked in
  weekend 1 at toy scale, before money; if it still fails in weekend 3, the
  branch is E3, decided in advance.
- **A gate returns a fatal finding.** Each costs one weekend; the plan holds
  five. Two fatal findings on the same gate is the point at which the re-plan
  names what comes off the back end, per the kill-date rule.
- **A rented machine bills anomalously or the laptop sleeps.** Halt, not
  trim; the launcher sleep check lands in weekend 1 before any launch; the
  fetch and kill are scheduled inside the run window; the ledger row exists
  before the pod does.
- **The measure turns out to detect rather than scale (the middle-of-scale
  finding).** E0 is the answer, and it is why the envelope ruling goes to John
  in weekend 1.

## 6. How the weekly iteration works

1. Thursday or Friday evening, Cowork: read the top of `STATUS.md` and the
   TimeAssembler queue; write the coming weekend's outcome, John's items with
   time estimates, the agent sessions to spawn (each with its checker), and
   the go's and rulings needed, as the next entry in this file's section 7.
   Update the weekend's TimeAssembler step and mirror this document.
2. Saturday morning, John: the queue first (rulings, go's, reviewer sessions),
   because everything else waits on it.
3. Sunday night, an agent: the handoff entry at the top of `STATUS.md`,
   `data/project.toml`, the ledger if money moved, and this file's section 7
   marked with what landed and what carried.
4. Kill dates and the wrap-up start never move. What moves is which weekend
   absorbs a slip, and the re-plan names it.

## 7. Weekend log

### Weekend 1, 2026-09-26 to 27 (planned 2026-09-24)

John's items, in order: the two A3 tier 2 sessions (about two hours); the
queue of rulings in section 1 (about one hour, pre-assembled by a session
before Saturday); the spoken go for the rented slice; optionally the site
secrets and the visibility flip.

Agent sessions to spawn Friday night or Saturday morning, each paired with a
checker in a separate worktree: (a) handoff and STATUS entry and worktree
prune; (b) the queue packet for John, one page per decision with the
measurement behind it and a recommendation with its confidence; (c) rehearsal
repairs: named-other redesign, one-instrument nomination, control 2, fourth
arm attempt; (d) proposal version 2; (e) launcher sleep check. Sunday: (f)
Gate C tier 1 on version 2; (g) if clean, Gate A tier 1 on the registration
text.

Outcome to report Sunday night: A3 closed or not; every blocking decision
ruled or which remain; version 2 through tier 1 or which findings block; the
rented slice's seconds per step in the release arithmetic.

### Weekend 1, progress as of 2026-09-24 evening

Landed on main tonight, all paired writer/checker: the record update (PR 29,
PR 31, check merged), the site's /roadmap/ page (PR 32, check merged), the
shared launch gate on all three unregistered launchers (PR 33, check landed
from PR 36, empty-date test 9c76a0f), and the Saturday ruling packet
(PR 34, check PR 35). Goals W1.3, W1.4 and W1.9 are done in
`data/roadmap.toml`. The Mac's never-sleep setting is on.

Working rules learned tonight, for whichever session runs the weekend:

- Every session prompt starts with a name in the form "MVM W1c rehearsal
  repairs" (weekend, letter, task) and is launched from `~/Code` with
  `claude -n "<that name>"`, so the agents overview rows are readable.
- A re-check prompt goes to the checker only after the writer has reported a
  commit hash that is on origin. Three re-checks tonight fired early and
  found nothing because the fix was still uncommitted.
- Merge order: the writer's PR, then the check's PR, except the ruling packet
  (check first, so the packet's pointers resolve). A check PR that carried the
  writer's commits merged in will conflict once main moves; land its review
  file directly and close the PR.
- The rented slice session (f) runs its checker first: a filed check of the
  regenerated plan file is owed before the go, and the gate now also needs a
  ledger row naming the run, dated within two days, with an estimate.
- The per-run figure is an estimate resting on measured ledger rows (see the
  note above section 2), never "$12 from the guide".

Saturday's queue, in order: the two A3 tier 2 reviewer sessions from the
INDEX file the packet names; the drafted dispositions and the A3 ruling; the
nine pages of `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`, ruled
into `docs/rulings/2026-09-26-weekend-1-queue.md`; items 10 to 12 from the
TimeAssembler Weekend 1 step (reviewer-count discrepancy, the launch gate's
unruled design choices, the registered-launcher amendment's timing); the
spoken go for the rented slice. If Friday evening has three hours, all of
this moves a day earlier and the agent sessions (c), (d), (f), (g) follow
the same night.
