# Check of pull request 31: the 2026-09-24 (evening) record update

*Filed 2026-09-24 (Pacific) by a checking session under the pairing rule of
`docs/outside-review-protocol.md`. This session did not write pull request 31 and
has not read the chat of the session that did. It is filed here, under the reviews
directory of the first constructed self-index experiment, because STATUS.md and
`data/project.toml` belong to no single experiment and this is the experiment their
top entries are mostly about. This check fixes nothing. It lists what must change.*

**Target:** pull request 31, "Bring the record current for 2026-09-24, and say how
the two roadmaps fit together", branch `worktree-record-current-2026-09-24`, one
commit `5d8529a` on top of main at `97ee3c9`.

**Verdict in one line:** the entry is not a duplicate, every pointer in it resolves,
and the site check passes. One thing must change before merge: `data/project.toml`
still says in two unchanged places what a missed kill date used to mean, and now
contradicts the new sentence the pull request adds a few lines above it. Two smaller
wording fixes are recommended.

---

## What was opened, and what was not

Opened: `CLAUDE.md`; the top entry of `STATUS.md` on main and on the pull request;
`docs/outside-review-protocol.md` (the pairing rule, the isolation section, Filing,
and the amendments); `docs/known-failure-modes.md` (the introduction and failures 4
and 5); the full diff of `5d8529a`; `STATUS.md` as commit `6d98e1e` landed it;
item 23 and the section list of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`; the head (lines
1–60) and section 5 wording (by search) of `docs/december-result-roadmap-2026-09-20.md`;
lines 1–130 of `docs/program-roadmap-2026-09-20.md`; the section list and "Bookkeeping
owed" paragraph of `docs/weekend-roadmap-2026-09-24.md`; the sleep-guard comment
(lines 196–262) of `experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`;
`data/project.toml` lines 95–103 and 560–566; in TimeAssembler, the Minimum Viable Mind
project's finished tasks, its document list, and the workflow-audit document
("Workflow audit — goals, roadmap, progress, and a seven-dimension scorecard", `4838a94f`).

Not opened: the rest of the December-result roadmap, the weekend roadmap's body,
`sleep_guard_selftest.sh`'s contents, and the two draft files outside the repository
(I listed them only). I **did not run** the sleep-guard self-test. It is written to
create nothing. But the brief for this session says launch nothing, and the entry
under review doesn't claim the test was run ("This session did not run that test").
So the check had nothing to compare it against.

A note on the setup, because it changes how check 4 reads: **local `main` on this Mac
is one commit ahead of `origin/main`.** The extra commit is `b5cfc23` ("Add the weekend
roadmap, its structured twin for the site, and the weekend 1 session prompts"). It is
not pushed and is not part of this pull request's base.

---

## Check 1 — does the new entry repeat the entry commit 6d98e1e landed?

**MEASURED.** Both entries were cut out of their files: from the first
`## WHERE THINGS STAND` heading to the next one. Then they were compared.

```
$ git show 6d98e1e:STATUS.md > STATUS_6d98e1e.md
$ awk '/^## WHERE THINGS STAND/{n++} n==1' STATUS_6d98e1e.md > entry_6d98e1e.md
$ awk '/^## WHERE THINGS STAND/{n++} n==1' STATUS.md > entry_new.md     # at 5d8529a
$ wc -l entry_*.md
      86 entry_6d98e1e.md
      60 entry_new.md
$ grep -nFxf entry_6d98e1e.md entry_new.md | grep -v ':$'     # non-blank lines both share
3:*This section is the current state. Everything below it is the older
4:record, newest first, and is left exactly as written.*
```

The full `diff entry_6d98e1e.md entry_new.md` (141 lines, exit 1) is pasted below.
The only lines the two entries share are the two lines of the italic banner, which
the pull request moved from the older entry up to the new one. Every paragraph of the
new entry is different text.

```
1c1
< ## WHERE THINGS STAND 2026-09-24 — the successor's reading has a label and a limit on what may be quoted from it, both rulings are on the main line, and nothing has been spent since 2026-09-21
---
> ## WHERE THINGS STAND 2026-09-24 (evening) — the record is current: the 2026-09-22/23 handoff is the entry below, the weekend roadmap is mirrored in TimeAssembler, the launcher refuses to rent while the laptop can sleep; nothing spent
6,10c6,13
< **Money.** About **$227.6 of $400**, leaving about **$172.4**; Amendment A3, the
< first constructed self-index experiment, at about **$46.2 of its $100 stop**,
< leaving about **$53.8** — the running totals in
< `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`. Last spend:
< about two cents on 2026-09-21, on a machine nobody meant to create.
---
> **Read the entry below first; it is still right.** It is the handoff for
> 2026-09-22 and 2026-09-23. It was drafted by a session that ran from the wrong
> folder (`~/Code`, which is not a git repository), left there as
> `~/Code/MVM-handoff-2026-09-24-STATUS-entry.md` with a matching data-file patch, and
> then landed by John on 2026-09-24 as commit `6d98e1e`, merged as pull request 29
> (`7244b5b`). That commit corrected the draft before landing it and its message says
> what it changed. The draft files outside the repository are now redundant. This
> entry adds only what happened after it.
12,20c15,20
< **Amendment A3 waits on John's hands, not on any work.** Version 4 of the closure
< text was checked by a session that did not write it: *"Yes. Nothing in the text is
< outstanding"* (`reviews/2026-09-21-a3-closure-v4-fix-verification-claude-worktree.md`
< — not the earlier `…-v4-closure-check-…` of the same day, whose verdict those fixes
< answer). The reviewer packets verify clean, re-checked today. What is left: John
< runs the two outside sessions by hand — **Gemini takes one document, ChatGPT
< twenty-two files in one conversation** — and files both answers verbatim; he rules
< on the findings; fatal ones get a closure line checked by someone who did not write
< the fix; then the closure block is appended to `amendment-a3.md`.
---
> **The two rulings of 2026-09-23 are on the main line**, merged as pull request 28
> (`f9fe138`): the nomination label is which marker word is the model's own
> (`docs/rulings/2026-09-23-nomination-label.md`), and the two arms whose training
> does not reproduce may be quoted as a range and a direction only
> (`docs/rulings/2026-09-23-range-and-direction-only.md`). Both were ruled with
> authorship mixed: proposed by a session, approved by John.
22,35c22,31
< **The successor's reading has a label and a limit, both ruled 2026-09-23 with
< authorship mixed, both on the main line today as pull request 28.** The review
< attached to the proposal (`reviews/2026-09-21-successor-proposal-claude-worktree.md`)
< found two fatal flaws; the measurement rehearsal
< (`docs/2026-09-21-successor-measure-rehearsal.md`) confirmed both by measurement and
< found worse — the step that fits the reading had no label at all, and two of its
< three possible meanings score an arm built to read **0.0000** at **0.982 to 1.000**.
< Ruled: the label is **which marker word is the model's own**; and from the two arms
< whose training does not reproduce the registration may quote **a range and a
< direction only** — about 0.83 to 0.89, at the entangled end, one seed of three
< clearing the bar — never a decimal (both files in `docs/rulings/`). Neither ruling
< makes the procedure one instrument; section 7 of the rehearsal holds the open
< problems, led by the free arm reading at the entangled anchor rather than between
< the anchors.
---
> **The weekend roadmap exists and is mirrored.** `docs/weekend-roadmap-2026-09-24.md`
> lays a weekend-by-weekend schedule to 2026-12-21 over the December-result roadmap,
> and says in its own preamble that it is not a ruling and gives way to that roadmap.
> It is mirrored as the TimeAssembler project document of the same name ("MVM weekend
> roadmap to 2026-12-21 (2026-09-24)"), and the TimeAssembler roadmap carries one
> step per weekend plus a standing step to re-plan every Thursday or Friday evening
> from the top of this file. One paragraph of it is already stale: the "Bookkeeping
> owed" paragraph in its section 1 says the top of this file still reads 2026-09-21,
> which stopped being true when pull request 29 merged. Fix that at the first weekly
> re-plan; this session did not edit it.
37,43c33,39
< **Owed before the registration text goes to its gate**
< (`reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`): of three
< things, one is discharged by today's merge. The attenuation check's forward-pass
< evidence reverses — the record has it failing its pre-stated line on **one** arm and
< seed, the re-run finds **five**, though the finding survives on model-free evidence
< identical between runs — and the committed self-test record reports **63** passes
< where the code now gives **64**.
---
> **Two TimeAssembler steps were closed as already done** by the weekend-planning
> session on 2026-09-24, and both closures check out against the repository: "Land
> the two 2026-09-23 rulings … onto the main line" (task `b1ccd8dd`), done by pull
> request 28; and "does the second kill date bind the whole staggered launch, or only
> the first run?" (task `f2c3bcf8`), already ruled on 2026-09-21 by item 23 of
> `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`: it binds the
> launch of the remaining eight runs, not the single free-arm run before them.
45,53c41,51
< **The process the next session works under** (`docs/outside-review-protocol.md`;
< items 3 and 22 of the 2026-09-21 ruling): whatever one session writes, a different
< session checks, filing a command and its output rather than a reading; the five
< failure modes in `docs/known-failure-modes.md` are exercised against each design,
< not cited; a document is rebuilt, not skimmed, when new binding text depends on it;
< the reviewer's own measured check runs at every registration gate whether or not
< anything fatal was found, and that gate runs both review tiers, the outside one at
< least two models from other labs. Use `scripts/check_citations.py` and
< `scripts/check_single_source.py` rather than re-deriving them.
---
> **The launcher now refuses to rent a machine while this Mac can fall asleep**,
> merged as pull request 30 (`a0723bc`), with its follow-up check merged after it
> (`97ee3c9`). The precondition is in
> `experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`, and its
> test, `…/src/sleep_guard_selftest.sh`, is written to prove it both refuses and
> passes without renting anything. A warning a person could skim is now a refusal.
> That narrows the warning in the entry below about the rented slice: the launcher
> now enforces the never-sleep override, which is the one setting that keeps this Mac
> awake with the lid shut, and wall power. Its own comment names one gap it does not
> close: while the machine is being created and started, before the keep-awake
> command begins, nothing holds off the idle timer. This session did not run that test.
55,63c53,56
< **Working mode: task time, not calendar time.** A step starts when its
< prerequisites are done. The two kill dates are backstops — registration committed
< by **2026-10-18**, the remaining eight registered runs launched by **2026-11-01**
< — and since item 23 of the 2026-09-21 ruling, passing one takes a fresh ruling
< naming what comes off the back end, rather than dropping the roadmap to outcome
< R4 as the entry below this one still says. That entry stands as written; the
< current rule is here, and the same item settles that the second date binds those
< eight runs and not the free-arm run before them. The weekend-by-weekend schedule
< over the December-result roadmap is `docs/weekend-roadmap-2026-09-24.md`.
---
> **Old agent folders.** Git marks none of this repository's agent worktrees (the
> separate working folders agent sessions use) as prunable, because every one of their
> folders is still on disk, so none was removed. Clearing them out stays on the
> Weekend 1 step in TimeAssembler.
65,74c58,59
< **The next rented machine is staged and not run**
< (`docs/successor-rented-slice-staging-2026-09-21.md`): one short slice, about
< **$0.75 to $1.00**, hard cap **$2.00**, buying seconds per step on all three
< architectures — which the second release of money may not be asked for without —
< and the first exercise of the shutdown handshake against the real vendor. **It needs
< John's verbatim go naming the run**; the earlier one lapsed because it named a
< staging document about to change, and what is owed first is the amended plan,
< checked by a session other than the one that amended it. Keep the lid open:
< `caffeinate` blocks idle sleep and not lid-close, and idle billing has cost about
< $10.30 across four occurrences.
---
> **Money is unchanged** from the entry below; nothing has been spent since 2026-09-21
> (`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`).
76,86d60
< **What waits on John** — seven live items tagged `awaiting-john` on the Minimum
< Viable Mind project in TimeAssembler: (1) the entangled and free arms' numbers are
< one sample, not a measurement; (2) the free arm reads at the entangled anchor — is
< the measure detecting rather than scaling? (3) the named-other condition does not
< learn — redesign it, or accept the risk; (4) the verbatim go for the rented slice;
< (5) how to correct a measured value in registered text that its cited record does
< not contain; (6) correct the unreproducible key count in the independent A4 review,
< or leave it annotated; (7) Amendment A3 closure, the outside tier of its
< registration gate. Three are closed: the nomination label, the scope of the second
< kill date, and the registered repeated-sampling run.
<
```

**MEASURED — the older entry survives intact underneath.**

```
$ awk '/^## WHERE THINGS STAND/{n++} n==2' STATUS.md > entry_old_in_pr.md     # at 5d8529a
$ diff entry_6d98e1e.md entry_old_in_pr.md
3,5d2
< *This section is the current state. Everything below it is the older
< record, newest first, and is left exactly as written.*
<
exit 1
```

The only change to the older entry is that banner moving up. That's right: the banner
belongs to whichever entry is current.

**Finding 1a (MEASURED): no duplicate.** The new entry does not repeat the text of
`6d98e1e`'s entry.

**Finding 1b (ARGUED): two paragraphs repeat facts the older entry already records,
which contradicts the new entry's own framing.** The new entry says "This entry adds
only what happened after it." But its second paragraph, the pull request 28 rulings,
restates the older entry's third paragraph ("both on the main line today as pull
request 28"). The tail of its fourth paragraph restates item 23 ("the same item settles
that the second date binds those eight runs"), which is also in the older entry. The
merge times show pull request 28 came *before* the older entry, not after:

```
$ gh pr list --state merged --limit 6 --json number,mergedAt
[{"mergedAt":"2026-09-25T00:02:35Z","number":30},{"mergedAt":"2026-09-24T23:27:12Z","number":29},{"mergedAt":"2026-09-24T17:30:32Z","number":28},...]
```

In Pacific time, pull request 28 merged at 10:30 on 2026-09-24 and pull request 29 at
16:27. What is genuinely new is how the older entry got landed; the TimeAssembler
mirror and the two closed steps; the stale paragraph in the weekend roadmap; pull
request 30; the agent folders; and the reconciling sentence. This is a small wording
issue, not a factual error.

---

## Check 2 — does every claim point at something that exists?

**MEASURED — the two 2026-09-23 rulings are on main, carried by pull request 28.**

```
$ git log --oneline main | grep -E '^(0d0c290|049c175)'
049c175 Record John's ruling on the unrepeatable arms: range and direction only
0d0c290 Record John's ruling on the nomination label: which marker word
$ git merge-base --is-ancestor 0d0c290 origin/main; echo $?
0
$ git merge-base --is-ancestor 049c175 origin/main; echo $?
0
$ gh pr view 28 --json commits --jq '.commits[].oid[0:7]'
0d0c290
049c175
$ gh pr view 28 --json title,state,mergeCommit
{"mergeCommit":{"oid":"f9fe13823261e3807cb39cb7347718467fdcf8c1"},"state":"MERGED","title":"Two rulings of 2026-09-23: the nomination label, and what the unrepeatable arms may be quoted as"}
$ ls docs/rulings/
... 2026-09-23-nomination-label.md  2026-09-23-range-and-direction-only.md
```

The entry's `f9fe138` for pull request 28 matches the merge commit. Both ruling files
exist.

**MEASURED — pull request 30 carries the launcher sleep check.**

```
$ gh pr view 30 --json title,state
{"state":"MERGED","title":"Refuse to rent a machine when this Mac could fall asleep"}
$ gh pr view 30 --json mergeCommit,commits --jq '.mergeCommit.oid[0:7], (.commits[].oid[0:7])'
a0723bc
aa7b739
d4f10fa
32472d1
4d152ab
5913bfa
$ git show --stat --format='%h %P %s' 97ee3c9 | head -3
97ee3c9 a0723bccbf87e6b68ef75031a4ce7c0e07e0553b 5cc4b0198cffb8d0d1faca5af8102573307f2929 Merge branch 'worktree-agent-abe72a067c1968fba'
 ...9-24-sleep-guard-fixes-check-claude-worktree.md | 364 +++++++++++++++++++++
```

`a0723bc` is pull request 30's merge commit, as the entry says. `97ee3c9` merges the
follow-up check (`5cc4b01`, "Check the two sleep-guard repairs: nothing blocking,
merge"), as the entry says. It was a direct branch merge, not a pull request, and the
entry doesn't call it one.

**MEASURED — the launcher facts the entry repeats are in the launcher's own comment.**
`sleep_guard_selftest.sh` exists (26,813 bytes, executable). The launcher's comment
(lines 197–233) says three things. The never-sleep setting (`SleepDisabled`) is "the
ONLY one of these settings that keeps this Mac awake with the LID SHUT". The power
source is "refused on the same footing". And "THE LAUNCH WINDOW ITSELF IS NOT COVERED:
creating the machine, pushing the code, running the remote checks and starting the
training all happen with nothing holding the idle timer off". Each matches the entry
and the new `teaches` line in `data/project.toml`. **ARGUED:** "A warning a person
could skim is now a refusal" holds, but the refusal can be switched off.
`ALLOW_LAPTOP_SLEEP=1` overrides it on purpose (launcher lines 235–260). The entry
would be more exact if it said "a refusal that has to be switched off out loud". That
is optional.

**MEASURED — item 23 of the 2026-09-21 ruling, pasted in full**
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, lines 271–299):

```
23. **Past a kill date, launching takes a fresh ruling rather than dropping the
    roadmap.** Put to John with its strongest alternative, approved in his words
    "Ok that's fine. Let's go with your recommendation". The two kill dates of
    `docs/december-result-roadmap-2026-09-20.md` used to drop the roadmap to its
    fourth outcome (R4: hibernate with a registered design and a rehearsal, on
    the record as a schedule failure). Past a date, launching is now still
    possible, but only on a fresh ruling that names what comes off the back end
    to make room — a thinner closure, one outside reviewer at the closure gate
    instead of two, no refresh of the explainer, or whatever the real trade turns
    out to be. The dates themselves do not move, and neither does the reason for
    having them: nobody drifts past one quietly, and nobody decides in the moment
    without saying so out loud. The reasoning accepted, recorded so it can be
    attacked later: the kill dates were never really about schedule, but about
    stopping money going on a result that can no longer be finished before
    wrap-up starts on 2026-12-21; as written they would have abandoned a working
    design over a two-day slip, which is a rule nobody would follow, and a rule
    that gets broken is worse than none; the staggered launch of item 12 above
    now bounds the money better than a date can, because the large spend happens
    only after the first run reads out; and what a date still does, which no
    judgment about feasibility made at the moment of spending can do, is decide
    in advance — a judgment made when you want to spend is made by someone who
    wants to spend. **The same ruling settles which step the second kill date
    binds**: the launch of the remaining eight runs (step 5b of the chain in
    section 4 of the roadmap), not the single free-arm run before it (step 5a).
    The December result rests on the arms built to be separable and to be
    entangled, and those are in the second wave; the first run is a precondition
    for launching them, not the milestone. Outcome R4 stays in the roadmap as an
    outcome — it still describes hibernating with a design and no runs — but a
    missed date no longer puts the roadmap there by itself.
```

The pull request's new `where_we_are_going` text says three things: "the remaining
eight registered runs launched by 2026-11-01 (the second binds those eight, not the
single free-arm run before them)"; "passing either one no longer records a schedule
failure on its own"; and "launching past it takes a fresh ruling that names what comes
off the back end to make room". All three are in the item. The STATUS entry says "it
binds the launch of the remaining eight runs, not the single free-arm run before them",
and that is in the item too. **These match.**

**MEASURED — but two unchanged lines of `data/project.toml` still state the rule
item 23 replaced.**

```
$ grep -n -i "schedule failure\|kill date\|2026-10-18\|2026-11-01\|R4" data/project.toml | cut -c1-260     # at 5d8529a
21:where_we_are_going = "One result by 2026-12-21, or a named schedule failure. ...
101:remaining = ["No pre-registration yet; it is committed as soon as its outside-review gate is answered on both tiers and John rules, with 2026-10-18 as the kill date past which the line is a schedule failure. ...
564:teaches = "The text the whole December roadmap hangs on. The registration is committed as soon as both review tiers are answered and John rules, with no target date; the one date that binds is the kill date of 2026-10-18. ...
657:title = "December-result roadmap approved: ... one result or a named schedule failure by 2026-12-21"
```

**Finding 2a (MEASURED, must change): line 101 contradicts item 23 and the pull
request's own line 21.** The "remaining" list of stage 2 ("The shape of binding") says
2026-10-18 is "the kill date past which the line is a schedule failure". Item 23 says
"a missed date no longer puts the roadmap there by itself". Line 21 of the same file,
as this pull request rewrites it, says "passing either one no longer records a schedule
failure on its own". The pull request didn't touch line 101, so the site will now show
both rules. The project's working guide says "where the two disagree, fix the data
file", and this pull request is the one that rewrote the rule in the data file.

**Finding 2b (ARGUED, should change): line 564 is incomplete rather than wrong.** "The
one date that binds is the kill date of 2026-10-18" is true of the registration step.
But it leaves out that passing that date now needs a fresh ruling, not a stop. One
clause would bring it into line. Line 657 is a timeline row recording what was approved
on 2026-09-20, so it is history and should stay as written.

**MEASURED — the other pointers in the new entry.**

- `docs/weekend-roadmap-2026-09-24.md` exists (last commit `1582599`, "Add the weekend
  roadmap to 2026-12-21"). Its section 1 is "## 1. Where the project stands on
  2026-09-24" (line 20), and lines 96–98 read: "Bookkeeping owed: the 2026-09-22/23
  handoff was drafted and verified but never committed … so the top of `STATUS.md`
  still reads 2026-09-21". The entry says that paragraph is stale, and it is. The same
  paragraph also says "about sixty agent worktrees are prunable", which the entry's
  "Old agent folders" paragraph contradicts. On that point the entry is right:
  ```
  $ git worktree list --porcelain | grep -c '^prunable'
  0
  $ git worktree list | wc -l
        74
  ```
  So the weekend roadmap's paragraph is stale in a second place as well. The entry
  should say so, since it tells the next re-plan to fix that paragraph.
- The two draft files outside the repository exist:
  `~/Code/MVM-handoff-2026-09-24-STATUS-entry.md` (10,476 bytes) and
  `~/Code/MVM-handoff-2026-09-24-project-toml.patch` (17,303 bytes), both dated
  2026-09-24 10:27.
- Pull request 29 is merged with merge commit `7244b5b`, and `6d98e1e` is the commit
  it landed ("Where things stand 2026-09-24: …").
- TimeAssembler: the task "Land the two 2026-09-23 rulings … onto the main line"
  (`b1ccd8dd`) and the task "DECIDE (John): does the second kill date bind the whole
  staggered launch, or only the first run?" (`f2c3bcf8`) are both `done`. The project
  document "MVM weekend roadmap to 2026-12-21 (2026-09-24)" exists (`89c3a882`). The
  worklog entry cited in the reconciling sentence (`d6c7060e`, "Workflow audit: the
  record is honest and the science is real; the cadence and the app's task list are
  what need fixing") exists, dated 2026-09-22.
- I did not check the claim that the TimeAssembler roadmap carries "one step per
  weekend plus a standing step to re-plan every Thursday or Friday evening". I didn't
  pull the roadmap.

---

## Check 3 — does the site's data file pass its check?

**MEASURED.** Run at `5d8529a`. The worktree has no `.venv` of its own, so the main
checkout's interpreter ran the pull request's copy of the script. The script finds its
data from its own location (`ROOT = Path(__file__).resolve().parent.parent`), so it
read the pull request's `data/project.toml`.

```
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python scripts/export_site.py --check
export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas, 15 findings, 12 next steps, 30 timeline rows)
exit 0
$ git status --short
(no output)
```

**Passes, and wrote nothing.** **ARGUED:** this check only confirms the file's
structure (dates, required fields, counts). It can't see finding 2a, because a sentence
that contradicts another sentence is still valid structure. A pass here says nothing
about whether the content is consistent.

---

## Check 4 — does the diff touch only STATUS.md and data/project.toml?

**MEASURED.** The command as written, run with the pull request's head checked out:

```
$ git diff --stat main..HEAD
 STATUS.md                         |  71 ++++++-
 data/project.toml                 |  12 +-
 data/roadmap.toml                 | 376 ------------------------------------
 docs/site-roadmap-page-prompt.md  |  88 ---------
 docs/weekend-1-session-prompts.md | 397 --------------------------------------
 5 files changed, 79 insertions(+), 865 deletions(-)
$ git rev-parse main origin/main
b5cfc233de78ae78ff41a00bf4d5a1412953f4c9
97ee3c9a6d079db04f10ee37e80b20ac068f24dd
$ git show --stat --oneline b5cfc23
b5cfc23 Add the weekend roadmap, its structured twin for the site, and the weekend 1 session prompts
 data/roadmap.toml                 | 376 ++++++++++++++++++++++++++++++++++++
 docs/site-roadmap-page-prompt.md  |  88 +++++++++
 docs/weekend-1-session-prompts.md | 397 ++++++++++++++++++++++++++++++++++++++
 3 files changed, 861 insertions(+)
$ git diff --stat origin/main..HEAD
 STATUS.md         | 71 ++++++++++++++++++++++++++++++++++++++++++++++-
 data/project.toml | 12 +++++++---
 2 files changed, 79 insertions(+), 4 deletions(-)
$ git diff --stat main...HEAD
 STATUS.md         | 71 ++++++++++++++++++++++++++++++++++++++++++++++-
 data/project.toml | 12 +++++++---
 2 files changed, 79 insertions(+), 4 deletions(-)
```

**Finding 4 (MEASURED): the pull request touches only the two files.** The three extra
files in the literal command are exactly the three files of `b5cfc23`, which exists
only on this Mac's local `main`. They show up as deletions because the two-dot form
compares the two end states, not what the pull request changed. Measured against
GitHub's `main` (`origin/main`, the pull request's real base), or from the point where
the branches split (three dots), the diff is `STATUS.md` and `data/project.toml` only.
Nothing in the pull request needs to change for this. **Separately, for John:**
`b5cfc23` is a commit on local `main` that has not been pushed. It is not in this pull
request, and when the pull request merges on GitHub, local `main` will need a pull
before it can be pushed.

---

## Check 5 — is the reconciling sentence consistent with both roadmaps?

There is no number to run here. So, as the pairing rule asks, here are the sentences
the reconciling sentence was read against, one by one. **All ARGUED.**

| What the reconciling sentence says | What it was read against | Consistent? |
|---|---|---|
| The programme roadmap is "the open-ended plan" | `docs/program-roadmap-2026-09-20.md`, "What changed and why": John "would rather it be an ongoing research experiment that is documented and shared as it unfolds than something with a specific date and result in mind" | Yes |
| "whose lines of work are neither ordered nor dated" | Same file, heading "## Lines on the table (as of 2026-09-20, not ordered, not dated)"; and "What replaces them", item 1: "Lines of inquiry, each ending in a ruling … This is the program's cadence in place of dates" | Yes. Note: the same file also has an ordered "Near-term order of work" table and three dated commitments of its own (book lock 2026-09-30, wrap-up 2026-12-21, hibernation by 2027-01-04). The sentence says "lines of work", so it isn't wrong, but a reader shouldn't take it to mean the file contains no order and no dates. |
| The December-result roadmap "says of itself that it refines that plan rather than replacing it" | `docs/december-result-roadmap-2026-09-20.md`, status block: "Companion to `docs/program-roadmap-2026-09-20.md` (which it refines, not replaces)" | Yes, nearly word for word |
| It "is the one dated line inside it — the successor experiment" | December roadmap: "Section 4's week-by-week table is now an ordered chain …"; the amendment notes' "The dates that are commitments rather than pacing — the two kill dates, the book text lock, the wrap-up start and the hibernation condition"; and the workflow audit's change 6 (TimeAssembler document `4838a94f`): "the program is open-ended and undated, and the measurement line is the one dated line running inside it, with its own kill dates" | Yes. The sentence follows the audit's change 6, which it cites as its source. |
| "with its two kill dates" | December roadmap, third amendment note: "past a kill date, launching is still possible, but only on a fresh ruling …"; section heading "## 5. Kill dates and what they trigger" | Yes |
| "and its wrap-up start of 2026-12-21" | December roadmap, step 14 of section 4: "Wrap-up … **Starts 2026-12-21** (ruled)"; programme roadmap, item 5: "Wrap-up start: 2026-12-21 (ruled by John 2026-09-20)" | Yes, with a small imprecision. The wrap-up start is a programme-wide date that the programme roadmap rules and the December roadmap repeats. "Its wrap-up start" makes it sound like it belongs to the dated line only. "the programme's wrap-up start of 2026-12-21, which it runs up to" would be exact. Optional. |
| The weekend roadmap "is only a schedule laid over that dated line and gives way to it wherever the two disagree" | `docs/weekend-roadmap-2026-09-24.md`, lines 6–10: "Nothing here is a ruling. It is a schedule laid over the December-result roadmap … [where they] disagree, that one wins." | Yes |

**Finding 5 (ARGUED): the sentence is consistent with both roadmaps.** It says what the
workflow audit asked for. The one imprecision, "its" wrap-up start, is optional to fix.

---

## What must change before merge

1. **Must.** `data/project.toml` line 101 (the `remaining` list of stage 2, "The shape
   of binding"): replace "with 2026-10-18 as the kill date past which the line is a
   schedule failure" with wording that matches item 23. For example: "with 2026-10-18
   as its kill date; past it, launching takes a fresh ruling naming what comes off the
   back end". Then rerun `export_site.py --check`. (Finding 2a.)

## What should change (recommended, not blocking)

2. `data/project.toml` line 564: add that passing 2026-10-18 now takes a fresh ruling
   rather than ending the line. (Finding 2b.)
3. STATUS.md, first paragraph of the new entry: "This entry adds only what happened
   after it" is not accurate, because the pull request 28 paragraph and the
   item 23 clause repeat the older entry. Either cut those two, or change the claim to
   something like "This entry adds what happened after it, and confirms two closures
   against the repository." (Finding 1b.)
4. STATUS.md, weekend-roadmap paragraph: say that the stale "Bookkeeping owed"
   paragraph is wrong in a second place too. It says about sixty agent worktrees are
   prunable, and the count is 0. That way the Thursday re-plan fixes both. (Check 2.)

## Optional

5. The reconciling sentence: say "the programme's wrap-up start" rather than "its
   wrap-up start". (Check 5.)
6. The pull request 30 paragraph: say the refusal can be overridden deliberately
   (`ALLOW_LAPTOP_SLEEP=1`). (Check 2.)

## Outside this pull request, noted for John

- Local `main` holds an unpushed commit, `b5cfc23`. (Check 4.)
- The TimeAssembler worklog listing shows this pull request's entry (`9e7d5aa9`,
  "Record brought current for 2026-09-24 …") and the pull request 30 entry
  (`6d16a4e2`) under 2026-09-25. The commit is dated `2026-09-24 17:37:27 -0700`,
  which is 2026-09-24 in Pacific time. The date shown is most likely the app's
  creation time in Coordinated Universal Time (UTC), not something the sessions
  wrote. I didn't open the entries to confirm that, so it's worth knowing when you
  read the worklog by date, but it isn't a finding against this pull request.
