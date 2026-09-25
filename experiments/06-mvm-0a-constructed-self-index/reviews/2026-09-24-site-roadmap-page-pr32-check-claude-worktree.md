# Check: pull request 32, the site's new roadmap page

*Written 2026-09-24 (Pacific), from about 17:50 to 18:10, by a checking session that
wrote none of the work being checked and had not seen the session that wrote it.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30). Every finding is marked **MEASURED** (a command was run and its
output is pasted here) or **ARGUED** (a reading or a judgment, not a measurement).*

**What was checked.** Pull request 32, "Add the /roadmap/ page: the weekend plan and
progress against it", branch `roadmap-page` at commit `1e3e544` (the same commit
locally and on GitHub). It branched from `main` at `b5cfc23` ("Add the weekend
roadmap, its structured twin for the site, and the weekend 1 session prompts").
`main` has since moved one commit, to `45875ee` ("Roadmap data: a carried goal is
never copied", 17:49 Pacific).

**How.** The branch was already checked out in another session's worktree, so it was
not touched. Its files were exported with `git archive origin/roadmap-page` into this
job's scratch folder and every check ran there; the site's installed packages were
linked from the main checkout (the pull request does not change `package.json` or
`package-lock.json`, MEASURED by `diff`, both identical). Python 3.14.5 on this Mac.
Nothing was deployed, launched, rented or spent. No registered text, ruling file or
protocol text was edited; the pull request was not edited.

**Verdict: not ready to merge; two things must change first**, both small. Everything
else in the brief passes.

| # | Check | Result |
|---|---|---|
| 1 | `npm run check` and `npm run build` | **Pass** (MEASURED) |
| 2 | All weekend, milestone and extension ids on the page | **Fail for 17 of 22** (MEASURED): extension ids E0–E4 are there; weekend ids W1–W13 and milestone ids K1, K2, W, H are not. The weekends and milestones themselves are all there, by number and title. |
| 3 | Progress strip numbers | **Pass** (MEASURED), with a clock caveat for the automatic deploy |
| 4 | Three broken copies of `data/roadmap.toml` rejected plainly | **Pass** (MEASURED), plus a fourth break and a passing control |
| 5 | 2026-02-30 gives a plain error, not a traceback | **Pass** (MEASURED), in both data files |
| 6 | Files touched | **Pass** (MEASURED), but the merge **conflicts** with `main` in `data/roadmap.toml` and, resolved the lazy way, would delete a 2026-09-24 ruling |
| 7 | Weekend 1 card against the plan's section 7 | **Pass** on the data (MEASURED); two small gaps between the prose and the data (ARGUED). Read as page text from the preview server, not by eye: the browser could not be opened from this session. |

---

## What must change before merging

1. **Rebase onto `main` and keep the ruling in the data file's header.** (MEASURED:
   `git merge-tree --write-tree --name-only main origin/roadmap-page` prints
   `CONFLICT (content): Merge conflict in data/roadmap.toml`.) After the branch was
   cut, `main` gained `45875ee`, which adds to the header of `data/roadmap.toml`:
   a carried goal is never copied into the later weekend; it stays where it was with
   status "carried" and the note, the page counts it as not yet done, and it is set to
   "done" there when it lands, "(ruled 2026-09-24, so no goal is ever counted
   twice)". The pull request rewrote the same lines, so the comparison of the two tips
   (check 6) shows the pull request deleting that paragraph. The resolution is: keep
   `main`'s paragraph word for word and add the pull request's two new vocabulary
   lines (milestone kinds, extension statuses) above it. The pull request's own sentence
   "the check refuses a carried goal without a `note` saying which" can sit alongside.
   The pull request description's call "Carried goals may be counted twice" is settled
   by that ruling and should be struck from the description.

2. **Show the weekend and milestone ids on the page, or have John drop that
   requirement.** The brief asks that the built page contain W1–W13 and K1, K2, W, H.
   It contains none of them as ids (MEASURED, check 2). Each weekend card is headed
   "Weekend 1" with an anchor `weekend-1`, and each milestone is shown by title
   ("Kill date 1: the registration committed") and date. All 41 goal ids (W1.1 and on)
   and the five extension ids are shown. Suggested change (ARGUED): print the weekend
   id in the card's header line beside the number (for example a small `W1` in the same
   monospace style as the goal ids) and the milestone id before each milestone title in
   the list under the timeline. That is what makes a handoff that says "W3.2 carried to
   W5" or "past K1" checkable against the page.

## Worth fixing, not blocking

3. **Day counts use the machine's clock, which is UTC on the automatic deploy.**
   (MEASURED, check 3.) `scripts/export_site.py` computes "today" with
   `date.today()`. On this Mac that is the Pacific date and the numbers are right. Run
   under a UTC clock at 17:51 Pacific it gave 2026-09-25 and 23 / 37 / 87 / 101 days,
   one short. `site/README.md` says `.github/workflows/deploy-site.yml` deploys on push
   to `main`, and that workflow runs on `ubuntu-latest`, which uses UTC. So a push made
   after 17:00 Pacific (16:00 in winter) would publish counts one day short. This is
   not new: `main`'s export script already does the same for the home page (line 183),
   and the new page copies it. The fix for both is one line, taking today's date in
   `America/Los_Angeles`.

4. **Section 7 lists an agent session that has no goal of its own** (ARGUED, check 7):
   session (b), "the queue packet for John, one page per decision with the measurement
   behind it and a recommendation with its confidence". The data folds it into John's
   ruling goal W1.2 and his second item. If the packet is not ready by Saturday, the
   page has no line that goes red. This is a data-file question for the Thursday re-plan
   rather than a defect in the page.

5. **Weekend 1's outcome line leaves out one of the four things section 7 says to
   report Sunday night**: the rented slice's seconds per step written into the release
   arithmetic. The goal W1.5 covers it, so nothing is lost from the checklist; only the
   outcome sentence is short (ARGUED).

6. **The date-error wording depends on the Python version** (ARGUED, not measured on
   3.12). Python 3.14 on this Mac says "day 30 must be in range 1..28 for month 2 in
   year 2026"; older versions say only "day is out of range for month". Both are plain;
   no change needed.

---

## Evidence

### Check 1: check and build (MEASURED)

```
$ TZ=America/Los_Angeles date
Thu Sep 24 17:50:56 PDT 2026
$ cd site && npm run check && npm run build

> minimum-viable-mind-site@0.1.0 check
> python3 ../scripts/export_site.py --check

export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas, 15 findings, 12 next steps, 29 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 41 goals, 4 milestones, 5 extensions)
> minimum-viable-mind-site@0.1.0 prebuild
> python3 ../scripts/export_site.py
export_site: wrote site/src/data/project.json
export_site: wrote site/src/data/roadmap.json
> minimum-viable-mind-site@0.1.0 build
> astro build
17:50:57 [vite] Re-optimizing dependencies because vite config has changed
17:50:58 [content] Syncing content
17:50:58 [content] Synced content
17:50:58 [types] Generated 402ms
17:50:58 [build] output: "static"
17:50:58 [build] mode: "static"
17:50:58 [build] directory: /Users/john/.claude/jobs/a4ac3365/tmp/pr32/site/dist/
17:50:58 [build] Collecting build info...
17:50:58 [build] ✓ Completed in 410ms.
17:50:58 [build] Building static entrypoints...
17:50:58 [vite] ✓ built in 316ms
17:50:58 [build] ✓ Completed in 332ms.
 generating static routes
17:50:58 ▶ src/pages/404.astro
17:50:58   └─ /404.html (+4ms)
17:50:58 ▶ src/pages/eli5.astro
17:50:58   └─ /eli5/index.html (+1ms)
17:50:58 ▶ src/pages/index.astro
17:50:58   └─ /index.html (+2ms)
17:50:58 ▶ src/pages/ladder.astro
17:50:58   └─ /ladder/index.html (+1ms)
17:50:58 ▶ src/pages/learned.astro
17:50:58   └─ /learned/index.html (+1ms)
17:50:58 ▶ src/pages/questions.astro
17:50:58   └─ /questions/index.html (+1ms)
17:50:58 ▶ src/pages/roadmap.astro
17:50:58   └─ /roadmap/index.html (+5ms)
17:50:58 ▶ src/pages/spend.astro
17:50:58   └─ /spend/index.html (+1ms)
17:50:58 ▶ src/pages/story.astro
17:50:58   └─ /story/index.html (+2ms)
17:50:58 ✓ Completed in 25ms.
17:50:58 [build] 9 page(s) built in 770ms
17:50:58 [build] Complete!
```

(Colour codes removed; blank lines removed; nothing else changed.)

### Check 2: ids in `dist/roadmap/index.html` (MEASURED)

Counted as whole tokens, so `W1` inside `W1.1` or `W10` does not count, and a bare
`W` or `H` inside ordinary words does not count.

```
$ standalone-token count of each id in dist/roadmap/index.html (not part of a longer id like W1.1 or W10)
W1   0
W2   0
W3   0
W4   0
W5   0
W6   0
W7   0
W8   0
W9   0
W10  0
W11  0
W12  0
W13  0
K1   0
K2   0
W    0
H    0
E0   1
E1   14
E2   6
E3   2
E4   1

$ grep -o 'id="weekend-[0-9]*"' dist/roadmap/index.html | wc -l    (one anchor per weekend card)
      13
$ grep -oE 'W[0-9]+\.[0-9]+' dist/roadmap/index.html | sort -u | wc -l    (distinct goal ids)
      41
$ milestone titles, occurrences each
Kill date 1: the registration committed:        1
Kill date 2: the remaining eight:        1
Wrap-up starts:        2
Hibernation condition complete:        1
```

E1 appears 14 times because other weekends' text refers to that extension; each
extension id appears once as its own table cell (MEASURED: `>E0<` through `>E4<` one
each).

### Check 3: progress strip (MEASURED)

Computed independently from the Pacific date:

```
Pacific now: 2026-09-24T17:51:50-07:00  UTC date: 2026-09-25
2026-10-18 24 days
2026-11-01 38 days
2026-12-21 88 days
2027-01-04 102 days
goal statuses Counter({'planned': 41}) counted (not not_needed): 41 done: 0
weekend statuses Counter({'planned': 9, 'slack': 2, 'active': 1, 'blackout': 1})
```

Thirteen weekends less the one blackout weekend is 12 working weekends, none done.

The page's strip, as built (tags removed):

```
Progress against the plan as of Sep 24, 2026
0 / 41 goals done  0% of the goals that count. 0 carried to a later weekend, 0 dropped.
0 / 12 working weekends done  The blackout weekend is not counted.
24 days to kill date 1, Oct 18, 2026
38 days to kill date 2, Nov 1, 2026
88 days to wrap-up, Dec 21, 2026
102 days to hibernation, Jan 4, 2027
```

All match. The same export under a UTC clock, a minute later:

```
TZ=UTC exported_on 2026-09-25 [('K1', 23), ('K2', 37), ('W', 87), ('H', 101)]
Mac local exported_on 2026-09-24 [('K1', 24), ('K2', 38), ('W', 88), ('H', 102)]
```

### Checks 4 and 5: broken copies (MEASURED)

Each break was written over the scratch copy's data file, checked, and the original
text written back. Script: this job's `tmp/check4.py`.

```
--- baseline, unbroken files
$ python3 scripts/export_site.py --check
export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas, 15 findings, 12 next steps, 29 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 41 goals, 4 milestones, 5 extensions)
[exit code 0; traceback: no]

--- (a) goal W1.1 status set to "finished" (not in the vocabulary)
$ python3 scripts/export_site.py --check
export_site: data/roadmap.toml: goal W1.1: status 'finished' not in ['carried', 'done', 'dropped', 'not_needed', 'planned']
[exit code 1; traceback: no]

--- (b) weekend blocks W2 and W3 swapped in the file (out of order)
$ python3 scripts/export_site.py --check
export_site: data/roadmap.toml: weekend W3: number 3 does not follow 1
[exit code 1; traceback: no]

--- (c) goal W1.2 status set to "carried" with no note
$ python3 scripts/export_site.py --check
export_site: data/roadmap.toml: goal W1.2: a carried goal needs a note saying which weekend it moved to
[exit code 1; traceback: no]

--- (control) goal W1.2 carried WITH a note (should pass)
$ python3 scripts/export_site.py --check
export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas, 15 findings, 12 next steps, 29 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 41 goals, 4 milestones, 5 extensions)
[exit code 0; traceback: no]

--- (check 5) project.updated_on set to 2026-02-30 (impossible date)
$ python3 scripts/export_site.py --check
export_site: data/project.toml: [project].updated_on: '2026-02-30' is not a real date (day 30 must be in range 1..28 for month 2 in year 2026)
[exit code 1; traceback: no]

--- (check 5b) roadmap weekend W1 start set to 2026-02-30
$ python3 scripts/export_site.py --check
export_site: data/roadmap.toml: weekend W1.start: '2026-02-30' is not a real date (day 30 must be in range 1..28 for month 2 in year 2026)
[exit code 1; traceback: no]

restored: data/roadmap.toml and data/project.toml byte-identical to the pull request's versions
--- after restore
$ python3 scripts/export_site.py --check
export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas, 15 findings, 12 next steps, 29 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 41 goals, 4 milestones, 5 extensions)
[exit code 0; traceback: no]
```

Swapping the blocks trips the numbering check before the date check, so the date check
was tested on its own: numbers left in order, weekend 3 moved to dates before weekend 2
(`tmp/check4b.py`):

```
--- (b2) weekend W3 dates 2026-10-10/2026-10-12 changed to 2026-09-19/2026-09-20 (before W2), numbers unchanged
$ python3 scripts/export_site.py --check
export_site: data/roadmap.toml: weekend W3: starts 2026-09-19, not after weekend W2 ends 2026-10-04; weekends must be in order
[exit code 1; traceback: no]
restored: data/roadmap.toml byte-identical
```

### Check 6: files touched (MEASURED)

Comparing the two tips, as the brief asked (`main` is now `45875ee`):

```
$ git diff --stat main..origin/roadmap-page
 CLAUDE.md                     |  10 +++
 data/roadmap.toml             |   9 +-
 scripts/export_site.py        | 185 ++++++++++++++++++++++++++++++++++++---
 site/.gitignore               |   1 +
 site/README.md                |   8 +-
 site/src/components/Nav.astro |   1 +
 site/src/layouts/Base.astro   |   1 +
 site/src/lib/project.ts       |   7 ++
 site/src/lib/roadmap.ts       |  60 +++++++++++++
 site/src/pages/roadmap.astro  | 195 ++++++++++++++++++++++++++++++++++++++++++
 site/src/styles/global.css    |  89 +++++++++++++++++++
 11 files changed, 549 insertions(+), 17 deletions(-)
```

The pull request's own changes, measured from where it branched:

```
$ git diff --stat main...origin/roadmap-page
 CLAUDE.md                     |  10 +++
 data/roadmap.toml             |   5 +-
 scripts/export_site.py        | 185 ++++++++++++++++++++++++++++++++++++---
 site/.gitignore               |   1 +
 site/README.md                |   8 +-
 site/src/components/Nav.astro |   1 +
 site/src/layouts/Base.astro   |   1 +
 site/src/lib/project.ts       |   7 ++
 site/src/lib/roadmap.ts       |  60 +++++++++++++
 site/src/pages/roadmap.astro  | 195 ++++++++++++++++++++++++++++++++++++++++++
 site/src/styles/global.css    |  89 +++++++++++++++++++
 11 files changed, 549 insertions(+), 13 deletions(-)
```

Every file is under `site/` or is `scripts/export_site.py`, `CLAUDE.md` or
`data/roadmap.toml`: inside the allowed set. The four extra deleted lines in the first
listing are `main`'s ruling paragraph (must-change 1). The merge test:

```
$ git merge-tree --write-tree --name-only main origin/roadmap-page
2d55601dcd476c0e476f6f151abd2fc6bf254a7b
data/roadmap.toml

Auto-merging data/roadmap.toml
CONFLICT (content): Merge conflict in data/roadmap.toml
```

The `CLAUDE.md` addition (ten lines telling the Thursday re-plan and the Sunday
handoff to edit `data/roadmap.toml` and run `npm run check`) matches `site/README.md`
and adds no rule beyond it (ARGUED).

### Check 7: the Weekend 1 card (MEASURED for the data, ARGUED for the prose)

**What was read, and how.** The preview ran with `npm run dev -- --port 4391` from the
scratch copy. The Chrome extension was not connected in this session, and the session's
safety guard refused to start Chrome headless, so the card was **not looked at by
eye**. It was read as text from the page the preview server served
(`http://localhost:4391/roadmap/`, 255,113 bytes), the `<article>` holding
`id="weekend-1"`, with tags removed:

```
Weekend 1 · Sep 26–27, 2026 · 2 days Clear the queue, close A3, repair the proposal This weekend
Outcome Amendment A3 (the earlier constructed self-index experiment) closed under Gate A; every registration-blocking decision ruled; successor proposal version 2 through its Gate C first-tier review.
Goals
○ A3 closure through Gate A, both tiers, and the closure commit landed W1.1 Planned John and agents
○ Every registration-blocking decision ruled and recorded in docs/rulings/2026-09-26-weekend-1-queue.md W1.2 Planned John
○ The 2026-09-22/23 handoff landed at the top of STATUS.md with a 2026-09-24 entry; data/project.toml current; merged worktrees pruned W1.3 Planned Agents
○ The launcher refuses to rent a machine when the laptop can sleep, and the launch checklist is a gate it checks W1.4 Planned Agents
○ The rented slice run: seconds per step per arm measured on the rented machine and written into the second release's arithmetic; the shutdown path exercised end to end W1.5 Planned John and agents
○ Rehearsal repairs at toy scale: the named-other condition redesigned (or the risk accepted on record), the nomination procedure shown to be one instrument across arms, control 2 built as stated, the fourth arm attempted if ruled W1.6 Planned Agents
○ Successor proposal version 2 written with the ruled numbers, label and form, the failure-modes checklist exercised against it with commands and output, both checking scripts clean W1.7 Planned Agents
○ Gate C first-tier review of version 2 filed; if clean, the registration text drafted and its Gate A first tier launched overnight W1.8 Planned Agents
John's items
Run the two A3 closure second-tier reviewer sessions from the committed packets and file both responses verbatim; rule the drafted dispositions the same day
Rule the pre-assembled queue in one sitting: the eight numbers, the form of the measure, the named-other condition, the middle of the scale, the Wittgenstein criteria, the two record corrections, the spend ruling (successor cap $142; programme envelope $400 to $450)
Give the spoken go for the rented slice (about $1, hard cap $2)
Optional, ten minutes: the two Cloudflare secrets and the repository visibility flip, so the site deploys
John's hours about 3
Beside it: Book text lock 2026-09-30 is off the table (done or moved).
```

(Line breaks added between items for reading; the words are as served.)

Each item in the data for weekend 1, looked for on that card (`tmp/check7.py`):

```
goal W1.1 (both, planned): YES
goal W1.2 (john, planned): YES
goal W1.3 (agents, planned): YES
goal W1.4 (agents, planned): YES
goal W1.5 (both, planned): YES
goal W1.6 (agents, planned): YES
goal W1.7 (agents, planned): YES
goal W1.8 (agents, planned): YES
John item 1: YES
John item 2: YES
John item 3: YES
John item 4: YES
title: YES
outcome: YES
beside: YES
john_hours: YES
```

Owners show as "John", "Agents" and "John and agents", matching `john`, `agents` and
`both` (MEASURED, above).

**Against section 7 of `docs/weekend-roadmap-2026-09-24.md`** (the committed text;
ARGUED, a reading):

| Section 7 says | On the card |
|---|---|
| John: the two A3 second-tier sessions (about two hours) | John item 1 |
| John: the queue of rulings (about one hour) | John item 2; goal W1.2 |
| John: the spoken go for the rented slice | John item 3; goal W1.5 |
| John, optional: site secrets and visibility flip | John item 4 |
| Hours: two plus one | "about 3" |
| Agents (a): handoff, STATUS entry, worktree prune | W1.3 |
| Agents (b): the queue packet for John | **no goal of its own** (follow-up 4) |
| Agents (c): rehearsal repairs | W1.6 |
| Agents (d): proposal version 2 | W1.7 |
| Agents (e): launcher sleep check | W1.4 |
| Agents Sunday (f), (g): Gate C first tier on version 2; if clean, Gate A first tier on the registration text | W1.8 |
| Report Sunday: A3 closed; decisions ruled; version 2 through first tier; the rented slice's seconds per step in the release arithmetic | Outcome line has the first three; the fourth is goal W1.5 only (follow-up 5) |

Section 7's note that each agent session is paired with a checker in a separate
worktree is not on the card; that is how the work is done rather than a goal, and
leaving it off is reasonable (ARGUED).

**Aside, not about this pull request.** The main checkout has an uncommitted edit to
`docs/weekend-roadmap-2026-09-24.md` (section 1 only; section 7 unchanged, MEASURED by
`diff` against the committed file). It says the STATUS.md handoff has landed (pull
requests 29 and 31) and that the worktree folders need a `git worktree remove` pass
rather than a prune. If that is committed, goal W1.3's wording ("merged worktrees
pruned") and possibly its status want updating at the Thursday re-plan. Not touched
here.

---

*Scratch copy, scripts and outputs: `/Users/john/.claude/jobs/a4ac3365/tmp/` (removed
when the job is deleted). The preview server was stopped at the end.*

---

## Re-check, 2026-09-24 (Pacific, about 18:05)

*Asked for: re-check the new commits on pull request 32 that answer the two
must-change findings and the clock finding above.*

**Result: there are no new commits to re-check. Nothing above is resolved yet.**
The four requested checks were not run against new work, because none has been
pushed or committed. What was found instead is below.

**No new commits (MEASURED).** After `git fetch`, the branch is where it was:

```
$ git rev-parse roadmap-page origin/roadmap-page
1e3e544799e04f6f6696925be1930fa5e8beee30
1e3e544799e04f6f6696925be1930fa5e8beee30
$ gh pr view 32 --json headRefOid,updatedAt,commits
headRefOid 1e3e544799e04f6f6696925be1930fa5e8beee30, updatedAt 2026-09-25T00:43:33Z (17:43 Pacific)
commits: b5cfc23 "Add the weekend roadmap, ...", 1e3e544 "Add the /roadmap/ page: ..."
```

Main on GitHub has moved since the first check, to `814b782` (the merge of pull
request 31, 17:58 Pacific).

**Re-check 1, merge against main: still conflicts (MEASURED)**, now against `814b782`:

```
$ git merge-tree --write-tree --name-only origin/main origin/roadmap-page
89e06e8dd4291d98d8fccce0ffeb7518a5d317e7
data/roadmap.toml

Auto-merging data/roadmap.toml
CONFLICT (content): Merge conflict in data/roadmap.toml
[exit 1]
```

**Work in progress, not yet committed (MEASURED, read-only).** The writing session's
worktree (`.claude/worktrees/roadmap-page`) has one changed file, `data/roadmap.toml`,
saved 18:01 Pacific and not committed. Its `site/` folder and `scripts/export_site.py`
are identical to commit `1e3e544` (`diff -rq`, no differences). The uncommitted edit:

- restores main's carried-goal paragraph. Diffing the first 30 lines of main's file
  against the uncommitted file shows only the two added lines of allowed values (the
  other two lines in the output are the 30-line window shifting by two):

  ```
  15a16,17
  > #   milestone.kind: "kill_date" | "wrap_up" | "hibernation"
  > #   extension.status: "proposed" | "authorised" | "running" | "done" | "deferred" | "declined"
  29,30d30
  < source = "docs/weekend-roadmap-2026-09-24.md"
  < one_line = "Twelve working weekends between ..."
  ```

  So the paragraph is word for word, **in the uncommitted file**;
- adds "the rented slice's seconds per step in the release arithmetic" to the
  Weekend 1 outcome (follow-up 5);
- adds goal `W1.9`, "The Saturday ruling packet built and checked (PR 34)", owner
  agents (follow-up 4).

**Re-checks 2, 3 and 4 were not run (ARGUED).** The page code and the export script
are unchanged, so the build would still print no weekend or milestone ids (must-change
2), and the day counts would still follow the machine's clock (the UTC finding). Check
and build already passed on `1e3e544` (evidence above). Building someone else's
uncommitted state would not test the pull request.

**Still to do before merging:** commit and push the data-file edit above, rebased onto
`814b782` so the merge test is clean; print the W1–W13 and K1, K2, W, H ids on the page;
take today's date in Pacific time in `scripts/export_site.py`. Then ask for this
re-check again.


---

## Re-check 2, 2026-09-24 (Pacific, about 18:10)

*Asked for: re-check the rebased branch pushed to pull request 32 (expected tip
`1b76ce7` on top of `3a19488`).*

**Result: all four checks pass. Both must-change findings and the clock finding are
fixed; nothing blocks merging.** Follow-ups 4 and 5 (the ruling-packet goal and the
outcome line) are also answered. Checked on a fresh `git archive` of `1b76ce7`, with
the site's packages linked from the main checkout (the pull request does not change
`package.json` or `package-lock.json`: `git diff --stat origin/main 1b76ce7 --` those
two files prints nothing).

**The branch (MEASURED).**

```
$ git fetch origin roadmap-page
$ git rev-parse origin/roadmap-page origin/main
1b76ce7b81c62198ee3b4f9958dd9fd70b54c98e
814b782404b69f020fa418533de7a45b10c3238a
$ git log --format='%h %p %ad %s' origin/main..origin/roadmap-page
1b76ce7 3a19488 2026-09-24 18:03 Fix the five items the check of pull request 32 raised
3a19488 814b782 2026-09-24 17:43 Add the /roadmap/ page: the weekend plan and progress against it
$ git diff --stat 3a19488 1b76ce7
 data/roadmap.toml            |  3 ++-
 scripts/export_site.py       | 16 +++++++++++++---
 site/src/pages/roadmap.astro | 14 +++++++-------
 site/src/styles/global.css   |  3 +++
 4 files changed, 25 insertions(+), 11 deletions(-)
```

The page now sits directly on the current main (`814b782`).

### Re-check 1: merge and header, pass (MEASURED)

```
$ git merge-tree --write-tree --name-only origin/main origin/roadmap-page
79329655d616916097ae1a2af40f73166501337a
[exit 0]
```

No conflicted files are listed. The data file against main:

```
$ git diff origin/main origin/roadmap-page -- data/roadmap.toml
diff --git a/data/roadmap.toml b/data/roadmap.toml
index 605c10c..b2bcbf3 100644
--- a/data/roadmap.toml
+++ b/data/roadmap.toml
@@ -13,6 +13,8 @@
 #   weekend.status: "planned" | "active" | "done" | "partial" | "blackout" | "slack"
 #   goal.status:    "planned" | "done" | "carried" | "dropped" | "not_needed"
 #   goal.owner:     "john" | "agents" | "both"
+#   milestone.kind: "kill_date" | "wrap_up" | "hibernation"
+#   extension.status: "proposed" | "authorised" | "running" | "done" | "deferred" | "declined"
 #
 # "carried" means the goal moved to a later weekend (say which in `note`). A
 # carried goal is NEVER copied into the later weekend: it stays here with its
@@ -74,7 +76,7 @@ end = "2026-09-27"
 days = 2
 status = "active"
 title = "Clear the queue, close A3, repair the proposal"
-outcome = "Amendment A3 (the earlier constructed self-index experiment) closed under Gate A; every registration-blocking decision ruled; successor proposal version 2 through its Gate C first-tier review."
+outcome = "Amendment A3 (the earlier constructed self-index experiment) closed under Gate A; every registration-blocking decision ruled; the rented slice's seconds per step in the release arithmetic; successor proposal version 2 through its Gate C first-tier review."
 beside = "Book text lock 2026-09-30 is off the table (done or moved)."
 john_hours = "about 3"
 john_items = [
@@ -92,6 +94,7 @@ goals = [
   { id = "W1.6", text = "Rehearsal repairs at toy scale: the named-other condition redesigned (or the risk accepted on record), the nomination procedure shown to be one instrument across arms, control 2 built as stated, the fourth arm attempted if ruled", owner = "agents", status = "planned" },
   { id = "W1.7", text = "Successor proposal version 2 written with the ruled numbers, label and form, the failure-modes checklist exercised against it with commands and output, both checking scripts clean", owner = "agents", status = "planned" },
   { id = "W1.8", text = "Gate C first-tier review of version 2 filed; if clean, the registration text drafted and its Gate A first tier launched overnight", owner = "agents", status = "planned" },
+  { id = "W1.9", text = "The Saturday ruling packet built and checked (PR 34)", owner = "agents", status = "planned" },
 ]
 
 [[weekends]]
```

The only header change is the two added lines of allowed values; no header line is
removed. Main's carried-goal paragraph, cut from both files and compared with line
numbers stripped:

```
$ diff <main's 7-line "carried" paragraph> <the pull request's>
carried-goal paragraph: identical (7 lines)
```

The header at `1b76ce7`, lines 12 to 26:

```
# Vocabularies (validated by scripts/export_site.py):
#   weekend.status: "planned" | "active" | "done" | "partial" | "blackout" | "slack"
#   goal.status:    "planned" | "done" | "carried" | "dropped" | "not_needed"
#   goal.owner:     "john" | "agents" | "both"
#   milestone.kind: "kill_date" | "wrap_up" | "hibernation"
#   extension.status: "proposed" | "authorised" | "running" | "done" | "deferred" | "declined"
#
# "carried" means the goal moved to a later weekend (say which in `note`). A
# carried goal is NEVER copied into the later weekend: it stays here with its
# id, status "carried" and the note, and the page counts it as not yet done.
# When it lands, set it to "done" here (ruled 2026-09-24, so no goal is ever
# counted twice).
# "not_needed" means a branch that did not fire (for example a re-run that was
# not required). Neither counts against progress; "dropped" does.
```

### Re-checks 2, 3 and 4 (MEASURED)

One script (this job's `tmp/recheck2.sh`) runs check and build on this Mac's clock,
counts the ids in the fresh build, then builds once under `TZ=UTC` and once under
`TZ=America/Los_Angeles`. Its output, colour codes removed:

```
=== CHECK 4: check and build (this Mac's clock)
$ date; TZ=UTC date
Thu Sep 24 18:09:58 PDT 2026
Fri Sep 25 01:09:58 UTC 2026
$ npm run check && npm run build

> minimum-viable-mind-site@0.1.0 check
> python3 ../scripts/export_site.py --check

export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas, 15 findings, 12 next steps, 30 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 42 goals, 4 milestones, 5 extensions)
> minimum-viable-mind-site@0.1.0 prebuild
> python3 ../scripts/export_site.py
export_site: wrote site/src/data/project.json
export_site: wrote site/src/data/roadmap.json
> minimum-viable-mind-site@0.1.0 build
> astro build
18:09:59 [vite] Re-optimizing dependencies because vite config has changed
18:09:59 [content] Syncing content
18:09:59 [content] Synced content
18:09:59 [types] Generated 76ms
18:09:59 [build] output: "static"
18:09:59 [build] mode: "static"
18:09:59 [build] directory: /Users/john/.claude/jobs/a4ac3365/tmp/pr32b/site/dist/
18:09:59 [build] Collecting build info...
18:09:59 [build] ✓ Completed in 85ms.
18:09:59 [build] Building static entrypoints...
18:10:00 [vite] ✓ built in 273ms
18:10:00 [build] ✓ Completed in 286ms.
 generating static routes 
18:10:00 ▶ src/pages/404.astro
18:10:00   └─ /404.html (+3ms) 
18:10:00 ▶ src/pages/eli5.astro
18:10:00   └─ /eli5/index.html (+1ms) 
18:10:00 ▶ src/pages/index.astro
18:10:00   └─ /index.html (+2ms) 
18:10:00 ▶ src/pages/ladder.astro
18:10:00   └─ /ladder/index.html (+1ms) 
18:10:00 ▶ src/pages/learned.astro
18:10:00   └─ /learned/index.html (+1ms) 
18:10:00 ▶ src/pages/questions.astro
18:10:00   └─ /questions/index.html (+1ms) 
18:10:00 ▶ src/pages/roadmap.astro
18:10:00   └─ /roadmap/index.html (+4ms) 
18:10:00 ▶ src/pages/spend.astro
18:10:00   └─ /spend/index.html (+1ms) 
18:10:00 ▶ src/pages/story.astro
18:10:00   └─ /story/index.html (+2ms) 
18:10:00 ✓ Completed in 23ms.
18:10:00 [build] 9 page(s) built in 397ms
18:10:00 [build] Complete!
[exit 0]

=== CHECK 2: ids in dist/roadmap/index.html (whole tokens: not inside W1.1, W10 or ordinary words)
W1    2
W2    2
W3    2
W4    2
W5    2
W6    2
W7    2
W8    2
W9    2
W10   2
W11   2
W12   2
W13   2
K1    3
K2    3
W     3
H     3
W1.9  1
ids inside the rm-id label tag:
H×3  K1×3  K2×3  W×3  W1×1  W1.1×1  W1.2×1  W1.3×1  W1.4×1  W1.5×1  W1.6×1  W1.7×1  W1.8×1  W1.9×1  W10×1  W10.1×1  W10.2×1  W10.3×1  W10.4×1  W11×1  W12×1  W12.1×1  W12.2×1  W13×1  W13.1×1  W13.2×1  W2×1  W2.1×1  W2.2×1  W2.3×1  W2.4×1  W2.5×1  W3×1  W3.1×1  W3.2×1  W3.3×1  W3.4×1  W3.5×1  W4×1  W4.1×1  W4.2×1  W4.3×1  W4.4×1  W5×1  W5.1×1  W5.2×1  W5.3×1  W6×1  W6.1×1  W6.2×1  W7×1  W7.1×1  W7.2×1  W8×1  W8.1×1  W8.2×1  W9×1  W9.1×1  W9.2×1  

=== CHECK 3: build under TZ=UTC
$ TZ=UTC date; TZ=UTC npm run build
Fri Sep 25 01:10:00 UTC 2026
[build exit 0]
roadmap.json exported_on 2026-09-24 days_to [('K1', 24), ('K2', 38), ('W', 88), ('H', 102)]
project.json exported_on 2026-09-24 days_to_wrap_up 88 days_to_hibernation 102
page strip: Progress against the plan as of Sep 24, 2026 0 / 42 goals done 0% of the goals that count. 0 carried to a later weekend, 0 dropped. 0 / 12 working weekends done The blackout weekend is not counted. 24 days to kill date 1 ( K1 ), Oct 18, 2026 38 days to kill date 2 ( K2 ), Nov 1, 2026 88 days to wrap-up ( W ), Dec 21, 2026 102 days to hibernation ( H ), Jan 4, 2027

=== CHECK 3: build under TZ=America/Los_Angeles
$ TZ=America/Los_Angeles date; TZ=America/Los_Angeles npm run build
Thu Sep 24 18:10:01 PDT 2026
[build exit 0]
roadmap.json exported_on 2026-09-24 days_to [('K1', 24), ('K2', 38), ('W', 88), ('H', 102)]
project.json exported_on 2026-09-24 days_to_wrap_up 88 days_to_hibernation 102
page strip: Progress against the plan as of Sep 24, 2026 0 / 42 goals done 0% of the goals that count. 0 carried to a later weekend, 0 dropped. 0 / 12 working weekends done The blackout weekend is not counted. 24 days to kill date 1 ( K1 ), Oct 18, 2026 38 days to kill date 2 ( K2 ), Nov 1, 2026 88 days to wrap-up ( W ), Dec 21, 2026 102 days to hibernation ( H ), Jan 4, 2027
```

**Reading it.**

- **Check 4, pass.** Check and build succeed, with 9 pages. The goal total is now 42
  rather than 41, because goal W1.9 was added.
- **Check 2, pass.** Each weekend id W1 to W13 appears twice: in the card's header and
  on its timeline segment. Each milestone id K1, K2, W, H appears three times: in the
  progress strip, on the timeline tick and in the milestone list. W1.9 appears once, on
  its goal. Each goal id now sits at the start of its goal text in the same small label
  style, not in the line of chips below it.
- **Check 3, pass.** It was 18:10 Pacific, so the UTC date was already 2026-09-25. Both
  builds give "today" as 2026-09-24 and the same counts, 24 / 38 / 88 / 102 days to K1,
  K2, W and H. The home page's data (`project.json`) agrees, 88 and 102, so the same fix
  covers it. Before the fix, a UTC build at this hour gave 23 / 37 / 87 / 101 (the first
  check, above).

**Not re-checked:** the broken-file rejections (checks 4 and 5 of the first round) and
the Weekend 1 card read. The fix commit changes only the lines shown above
(`scripts/export_site.py` gains the Pacific date and nothing else; its validation code
is untouched), and the page was not looked at by eye this time either (ARGUED).

**Verdict: merge.** Merging is John's step (`gh pr merge 32`); this session did not
merge.
