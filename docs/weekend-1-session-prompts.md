# Weekend 1 session prompts (2026-09-26 to 27)

*Written 2026-09-24 (Pacific) by the Cowork planning session, for John to paste
into Claude Code, started from `~/Code`. Companion to
`docs/weekend-roadmap-2026-09-24.md` section 7. Each session is paired: the
writer prompt, then a separate checker prompt run in a fresh session that has
not seen the writer's chat. Nothing in any prompt authorises a launch or spend;
the one paid item (the rented slice) runs only after John's spoken go, and the
prompt for it says so.*

*Order matters. Run (a) tonight, 2026-09-24, so the packet is waiting Saturday
morning. Run (b) and (e) tonight or Friday. Run (c) and (d) Saturday, after the
queue is ruled, because both depend on the rulings. Run (f) and (g) Sunday.*

*Every prompt starts with the same header so the sessions share the rules.*

---

## The header, pasted at the top of every prompt

```
You are working in ~/Code/minimum-viable-mind. Read CLAUDE.md, the top entry of
STATUS.md, docs/outside-review-protocol.md (the pairing rule, the isolation
section, the failure-mode pass, and Filing), and docs/known-failure-modes.md
before anything else. Work in your own git worktree under .claude/worktrees/,
branched from main, and open a pull request at the end; never commit to main
directly. Write in plain language: every code name, metric shorthand and
acronym explained on first use. Every number you write cites the committed file
it came from by path; a number with no file is not written. Label every finding
MEASURED (a command was run and its output is reported) or ARGUED. Do not launch
any machine, rent anything, or spend money; if a step would, stop and say so.
Do not edit any registered text, ruling file or protocol text; annotate beside
it or draft a proposal. Dates are Pacific and absolute (YYYY-MM-DD). When you
finish, append one worklog entry to TimeAssembler (project Minimum Viable Mind)
saying what you did and who decided what, and put your PR number and a
three-line summary at the end of your last message.
```

---

## (a) The ruling packet for John — run tonight

**Writer prompt**

```
[header]

Task: build John's ruling packet for Saturday 2026-09-26, so he can rule every
registration-blocking decision in one sitting of about an hour. Output: one
file, docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md (a proposal for him,
not a ruling), plus a one-page index at the top.

Sources: docs/2026-09-21-successor-measure-rehearsal.md (sections 3, 5, 7, 8,
11 and 12), docs/successor-experiment-proposal-2026-09-21.md (sections 6, 7, 8,
9), the Gate C review experiments/06-mvm-0a-constructed-self-index/reviews/
2026-09-21-successor-proposal-claude-worktree.md, docs/rulings/2026-09-23-
nomination-label.md, docs/rulings/2026-09-23-range-and-direction-only.md,
docs/preauthorised-spending-proposal-2026-09-21.md (including its two
afterwards notes), docs/rulings/2026-09-21-review-verification-and-staged-
spending.md, the TimeAssembler note "Wittgenstein criteria for the Stage 2
metric", and the compute ledger experiments/06-mvm-0a-constructed-self-index/
compute-ledger.md, which is the only source for money.

One page per decision, in this order, each with: the question in one sentence;
the measurement behind it, quoted with its file path; the options; a
recommendation with a confidence level and the strongest argument against it;
and what the ruling changes in which document.

1. The eight numbers from rehearsal section 11: separation bar, learn-both
   threshold per condition, whole-state transplant floor (relative to the
   arm's own accuracy), rank cap, candidate site family, seed count per arm
   (with the discount the rehearsal says toy repeatability deserves, given the
   2026-09-23 range-and-direction ruling), paired-uncertainty method,
   ownership-lesion collapse threshold.
2. Which form of the measure is registered: the proposal's form or the
   chance-corrected form. Quote the rehearsal's table where the two read
   identical systems apart.
3. The nomination procedure being three instruments rather than one across
   arms (ruling file section 3): what would make it one, and whether that is a
   text change or a code change.
4. The named-other condition not learning at toy scale (rehearsal section 8):
   redesign options with what each costs, versus accepting the risk on the
   record.
5. The middle of the scale (rehearsal section 12 item 4): a fourth,
   partially separable arm versus an admission in the registration text. Say
   what the fourth arm would cost in runs and dollars at 30 million parameters,
   from the ledger's per-run figure.
6. Spend: the successor cap ($130 in force, the plan comes to about $142) and
   the programme envelope ($400; about $172.40 left per the ledger; the two
   releases come to about $175). Present the numbers from the ledger rows, not
   from any document that quotes them. Per the standing rule (docs/rulings/
   2026-09-20-december-result-roadmap.md) propose the increase with the
   number; the weekend roadmap's proposal is cap $142 and envelope $450.
   Include the anomaly tripwire from the preauthorised-spending proposal.
7. The Wittgenstein criteria: into the proposal now, or resumption.
8. The two record corrections on the roadmap queue: the unreproducible key
   count in the independent A4 review (correct or leave annotated), and the
   measured value in registered text whose cited record does not contain it
   (how it is corrected without rewriting registered text).
9. The rented slice go: what John says, verbatim shape, and the hard cap
   ($2.00), from docs/successor-rented-slice-staging-2026-09-21.md and the
   launcher-guard ruling of 2026-09-22.

Also at the top: the exact file to open for the A3 closure tier 2 sessions
(experiments/06-mvm-0a-constructed-self-index/reviews/packets/2026-09-21-a3-
closure-tier2-INDEX-how-to-run-these-sessions.md), and where the two responses
are filed when he is done.

Do not decide anything. Do not change any registered text. If a source
disagrees with another, say so in the packet rather than choosing.
```

**Checker prompt** (fresh session)

```
[header]

You are the checking session for docs/rulings/2026-09-26-weekend-1-queue-
PROPOSAL.md on branch <writer's branch>. You have not seen the session that
wrote it. For every number in it, open the file it cites and confirm the number
is there; run at least one command per decision page whose output would come
out wrong if the page were wrong (grep the cited figure in the cited file, and
for money, read the ledger rows and add them). File your check at
experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-weekend-1-
queue-check-claude-worktree.md with what you opened, what you did not, the
commands and their outputs, and MEASURED/ARGUED on each finding. Do not edit
the packet; list what must change. Then run scripts/check_citations.py and
scripts/check_single_source.py against it and paste the output.
```

---

## (b) Handoff, STATUS entry, project.toml, worktree prune — run tonight or Friday

**Writer prompt**

```
[header]

Task: bring the record current. (1) Find the drafted-and-verified handoff for
2026-09-22/23 that the 2026-09-24 worklog entry says could not be committed
(search the agent worktrees under .claude/worktrees/ and any branch for a
STATUS.md whose top entry is dated 2026-09-22 or 2026-09-23); land it as the
new top "WHERE THINGS STAND" entry, then add a 2026-09-24 entry above it
covering: the two 2026-09-23 rulings on main (PR 28), the weekend roadmap
docs/weekend-roadmap-2026-09-24.md and its TimeAssembler mirror, and the two
TimeAssembler steps closed as already done. (2) Update data/project.toml in the
same commit per CLAUDE.md, and run
`.venv/bin/python scripts/export_site.py --check`. (3) List every worktree
`git worktree list` marks prunable, confirm each one's branch is merged into
main (`git branch --merged main`), and prune only those; list the unmerged ones
by name in your PR description and do not touch them. (4) Write the one
sentence the 2026-09-22 workflow audit asked for, reconciling the programme
roadmap and the December-result roadmap, into the top of STATUS.md.
```

**Checker prompt**

```
[header]

Check branch <writer's branch>: confirm the 2026-09-22/23 entry matches the
source it was recovered from (diff them, paste the output), that every
worktree pruned had a branch merged into main (paste `git branch --merged
main` before and the prune list), that `scripts/export_site.py --check` passes
(paste), and that no registered text, ruling or protocol file changed
(`git diff --stat main..HEAD`, paste). File at experiments/06-mvm-0a-
constructed-self-index/reviews/2026-09-26-handoff-check-claude-worktree.md.
```

---

## (e) The launcher sleep check — run tonight or Friday

**Writer prompt**

```
[header]

Task: the open roadmap step "make the launcher refuse to rent a machine when
the laptop can sleep; every launcher warns, none checks". Read the launchers
and the watchdog (start from src/ and scripts/, and docs/rulings/2026-09-22-
launcher-argument-guard.md, and the reap-race fix on main). Add a precondition
to every launcher that creates a machine: it checks that the Mac cannot sleep
for the run window (for example `pmset -g` shows sleep disabled or a
`caffeinate` holding the assertion), and refuses with a plain message if not.
Also make the launch checklist a gate the launcher checks, per the weekend
roadmap: scheduled fetch and kill inside the run window, and a compute-ledger
row with an estimate written before the machine exists. Unit-test the refusal
paths without creating any machine. Method note first, then code, then a
findings note under experiments/06-mvm-0a-constructed-self-index/ named
launcher-sleep-gate-findings.md.
```

**Checker prompt**

```
[header]

Check branch <writer's branch>: run the launcher in a dry mode or with the
sleep assertion absent and paste the refusal; run the unit tests and paste;
confirm with `git grep` that every script that creates a machine calls the new
check (paste the grep and the list). Confirm nothing was rented (no vendor
calls in the diff). File at experiments/06-mvm-0a-constructed-self-index/
reviews/2026-09-26-launcher-sleep-gate-check-claude-worktree.md.
```

---

## Saturday, John, before (c) and (d)

1. The two A3 closure tier 2 sessions, from the INDEX file named in the
   packet. File both responses verbatim where the index says. Then paste this
   into a fresh Claude Code session: *"[header] Draft dispositions for the two
   A3 closure tier 2 responses just filed, one line per item in the ledger
   form, with a recommendation and confidence on each; do not rule."* Rule.
   Then a second session appends the closure block and lands the Gate A
   commit, and a third checks it (same shape as (b)'s checker).
2. Rule the packet from (a). Write the rulings as a dated file
   docs/rulings/2026-09-26-weekend-1-queue.md (a session can draft it from
   your answers; say "Agreed on all" or list the exceptions).
3. Give the rented slice go, verbatim, in the shape the packet gives.

---

## (c) Rehearsal repairs — Saturday, after the rulings

**Writer prompt**

```
[header]

Read docs/rulings/2026-09-26-weekend-1-queue.md first; it governs this task.
Then docs/2026-09-21-successor-measure-rehearsal.md sections 3, 6, 7, 8, 12,
docs/successor-measure-rehearsal-method-2026-09-21.md and its denominator
addendum. Method note committed before any output, as always.

Do, at toy scale, on the laptop, $0:
1. The named-other condition: implement the ruled redesign (or, if John
   accepted the risk, skip this and say so) and measure whether it now clears
   the one-in-four level on a majority of seeds. Report as a range and a
   direction where the arms do not reproduce (ruling of 2026-09-23).
2. Make the nomination procedure one instrument: with the label fixed to
   which marker word, run the procedure identically on all three arms and
   show, with the table, that the same procedure selects the same way on each.
3. Build control 2 as the proposal states it, not as it was run, and report
   what it returns.
4. If John ruled for the fourth arm: build a partially separable arm by
   construction, state before running what its degree should read, and
   measure it. If it cannot be built so that its degree is known, say so
   plainly; that is the finding.
5. Re-run the measure with the ruled form and the ruled numbers on all arms.

Findings file: docs/2026-09-26-rehearsal-repairs.md, same shape as the
rehearsal findings, with the "what still needs John" table updated.
```

**Checker prompt**

```
[header]

Check branch <writer's branch>: re-run the repaired rehearsal from the
committed code from clean (the precedent is experiments/06-mvm-0a-
constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-
worktree.md), paste the table beside the findings' table, and say for each
figure whether it reproduces exactly, as a range, or not at all. Confirm the
method note commit precedes the first output commit (`git log`, paste). File
at experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-rehearsal-
repairs-check-claude-worktree.md.
```

---

## (d) Successor proposal version 2 — Saturday, after (c) has findings

**Writer prompt**

```
[header]

Read docs/rulings/2026-09-26-weekend-1-queue.md and docs/2026-09-26-rehearsal-
repairs.md first. Write docs/successor-experiment-proposal-2026-09-26-v2.md
from version 1 (docs/successor-experiment-proposal-2026-09-21.md) with: the
two fatal Gate C findings repaired the way the rehearsal demonstrated (the
chance-corrected form if ruled; control 1 re-worded so it cannot veto the
entangled arm; the no-transplant sanity rule replaced with the review's
formula; section 7.1's freshness requirement disambiguated); the nomination
label written in (which marker word) and the one-instrument requirement stated
as a registered condition; every number from section 9 now filled from the
ruling, each citing the ruling file; the named-other redesign or the accepted
risk on the record; the fourth arm if ruled, with its predicted reading; the
spend section rebuilt from the ledger and the spend ruling; the staggered
launch (5a/5b) and halt-not-trim as ruled 2026-09-21. Keep version 1 unedited.

Then run the failure-mode pass the protocol requires: for each of the five
failures in docs/known-failure-modes.md, test version 2 against it with a
command and its output, not a citation, and file the pass at experiments/06-
mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-
pass-claude-worktree.md. Run scripts/check_citations.py and
scripts/check_single_source.py on version 2 and paste the output into the PR.
```

**Checker prompt**

```
[header]

You are the Gate C tier 1 reviewer for docs/successor-experiment-proposal-
2026-09-26-v2.md on branch <writer's branch>, under docs/outside-review-
protocol.md (read the tier 1 description and the fixed brief). You have not
seen the writing session. Attack it: every number against its cited file,
every repaired finding against the rehearsal's measurement, the five failure
modes against the design with your own commands, and the arithmetic of both
releases against the ledger. Continue the RT numbering from the last entry in
experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md. File at
experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-
gate-c-claude-worktree.md with fatal/serious/minor and MEASURED/ARGUED on each.
Do not edit the proposal.
```

---

## (f) The rented slice — only after John's spoken go, and after (e) is merged

**Writer prompt**

```
[header]

John's go, verbatim, is: "<paste>". Quote it in the compute ledger row before
anything is created. Run the one rented slice exactly as staged in
docs/successor-rented-slice-staging-2026-09-21.md, under the launcher with the
new sleep gate (PR <number> from (e), merged), hard cap $2.00, and stop on the
first thing that differs from the staging document. Deliverables: seconds per
step for each of the three (or four) architectures on the rented machine; the
shutdown path exercised end to end (credential, watcher, finished marker,
receipt, deletion) with the receipt filed; the ledger row's actual-after
figure from the vendor balance before and after; and the second release's
arithmetic rewritten from the measured figure in a note beside the
preauthorised-spending proposal (annotate, never rewrite). Findings:
docs/2026-09-27-rented-slice-findings.md.
```

**Checker prompt**

```
[header]

Check branch <writer's branch>: confirm the ledger row carries John's go
verbatim and an estimate dated before the machine's creation time in the
receipt (paste both), that the vendor balance delta equals the ledger's
actual-after (paste), that the machine is deleted (paste the vendor listing or
the receipt), and that the seconds-per-step figures in the findings match the
raw log (grep, paste). File at experiments/06-mvm-0a-constructed-self-index/
reviews/2026-09-27-rented-slice-check-claude-worktree.md.
```

---

## (g) Sunday: Gate A tier 1 on the registration text, if (d)'s Gate C is clean

```
[header]

The Gate C tier 1 review of proposal version 2 is filed at <path> and John has
ruled its findings in <ruling file>. Produce the registration text: copy
version 2 to experiments/<successor experiment directory>/registration-v2-
DRAFT.md in the form the A3 registration used (experiments/06-mvm-0a-
constructed-self-index/amendment-a3.md is the precedent), carrying the ruled
dispositions. Then, in a fresh session that has not seen this one, run Gate A
tier 1 on it under the protocol's fixed brief, continuing the RT numbering, and
build the tier 2 packet for the two outside reviewers with
scripts/build_a3_closure_tier2_packets.py as the model (Gemini whole; ChatGPT
in parts under 20 KB) and an INDEX file saying how to run the sessions. Verify
the packet independently the way scripts/check_a3_packets_independently.py
does. Nothing is committed as registered; this is a draft until both tiers are
answered and John rules.
```

---

## Sunday night: the handoff

```
[header]

Write the Sunday 2026-09-27 "WHERE THINGS STAND" entry at the top of STATUS.md
and update data/project.toml (run the check). Then append to docs/weekend-
roadmap-2026-09-24.md section 7, under Weekend 1, what landed and what carried,
against the four outcomes it names (A3 closed; blocking decisions ruled;
version 2 through tier 1; the rented slice's figures in the release
arithmetic). Update the WEEKEND 1 and WEEKEND 2 steps in TimeAssembler to
match, and refresh the TimeAssembler document "MVM weekend roadmap to
2026-12-21 (2026-09-24)" from the repo file. Name the John items now on the
queue for the week of 2026-09-28.
```
