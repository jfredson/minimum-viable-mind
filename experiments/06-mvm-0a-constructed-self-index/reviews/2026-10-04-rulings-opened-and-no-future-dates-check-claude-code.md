# Check of two rulings of 2026-10-04 (the registration review opened; no more future dates) and the roadmap edits that follow them

*Filed here under the filing fallback of the pairing rule (`docs/outside-review-protocol.md`, "The pairing rule"): the two ruling files belong to no experiment, and the experiment they most affect is the successor experiment, whose review records are filed in this folder.*

*Checked 2026-10-04 (Pacific) by a Claude Code session in its own worktree, on branch `check-rulings-2026-10-04-opened-and-dates`, from the tip `655b371` of the registration-review branch (`gate-a-registration-review-successor-v4`). This session wrote none of the material it checks, has not seen the chat of the session that wrote it, and edited none of it. Nothing was spent; laptop only. Written under the workspace plain-language rule. Each finding is labelled **MEASURED** (a command was run and its output is below) or **ARGUED** (reasoning a reader can dispute).*

## Verdict

The core of both rulings holds. Every quotation attributed to John matches the source text the recording session supplied, and every claim either file makes about another file in the repository checks out: the quotation of 2026-09-21 in the protocol's Amendments section, version 4 calling the opening "John's step", pull requests 85 to 91 on the main line, what each kill date binds, the wrap-up and hibernation dates, version 4's section 11 title, and the rule that passing a kill date takes a fresh ruling. The roadmap data file passes its check, exactly one weekend's status changed, no goal was copied, and the notes on the six changed goals are true against the record. That covers the work done 2026-10-03 on the controls re-run (W2.7) and the inside review and outside-review packet (W2.1). What does not hold is narrower. The registration-review file says John answered "in his own choice of words" when he picked one of two answers the session wrote. By the workspace rule and this repository's own earlier records, that answer makes the authorship mixed. The no-future-dates file puts the session's own reading under John's name: most clearly, that the Sunday-night handoff is retired, which John's words do not say and which the repository's `CLAUDE.md` still requires. The roadmap marks five goals "carried" under a rule that says a carried goal names the weekend it moved to. Several other files still describe the weekly re-plan as live. Two defects are must-fix and the rest can wait.

## What this check opened, and what it did not

**Opened:** `~/Code/CLAUDE.md` (the plain-language section and the `decidedBy` rule under "Session logging"); the repository `CLAUDE.md`; `docs/outside-review-protocol.md` ("The pairing rule", "Filing", "Amendments"); both ruling files; `git show 655b371` (all four files it changed); `git show f96c9eb`; `data/roadmap.toml` in full at `655b371` and its parent; the top of `docs/weekend-roadmap-2026-09-24.md` and its re-plan and handoff passages; the top of `STATUS.md` and its 2026-10-04 entry; `data/project.toml` (the "where" paragraphs, next steps N15 and N16); version 4 of the proposal (`docs/successor-experiment-proposal-2026-10-03-v4.md`), its opening list and section 11; the review-verification and staged-spending ruling of 2026-09-21 (item 23); the December-result roadmap ruling of 2026-09-20 (items 7 and the closing note); the December-result roadmap (row 14 of its chain); the inside-review findings file (`2026-10-04-successor-v4-gate-a-claude-code.md`, its summary and findings table); the commit messages of the code freeze (`db49cd2`) and of John's go on the development runs (`c9791c9`); four other ruling files of 2026-10-03 and 2026-10-04, for how authorship has been recorded; `scripts/export_site.py`; `site/README.md`; `site/src/pages/roadmap.astro` and `site/src/lib/project.ts`; `gh pr view 94`.

**Not opened, and cannot be:** the chat in which John gave either ruling, the planning session of 2026-10-04, and the multiple-choice exchange the registration-review file reports. The source text for both rulings (in `...-check-scripts/source.txt`) was supplied to this session by the recording session. **It cannot be verified independently from here.** Every finding below that says a ruling "matches its source" means it matches that supplied text, nothing more. Also not opened: the TimeAssembler roadmap step quoted as "opened by John once version 4 is checked…", and the TimeAssembler task for the re-plan that the no-future-dates file says "had already been closed". Neither is in the repository.

## The checks, as commands and their outputs

Scripts and full outputs are in `2026-10-04-rulings-opened-and-no-future-dates-check-scripts/`. All are run from the repository root.

### Check 1: every quotation in both ruling files, looked up in the supplied source and in the repo files it names (MEASURED)

Chosen so that a misquoted or invented quotation would print `NOWHERE`.

```
$ python3 experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/quotes_vs_sources.py
== docs/rulings/2026-10-04-no-future-dates.md
  NOWHERE 'file the timing ruling' -> -
  FOUND  'John ruled 2026-10-04: stop scheduling Minimum Viable Mind work on fut' -> source.txt
  FOUND  'The goal is to run everything as soon as possible based on what pre-re' -> source.txt
  FOUND  'everything is approved' -> source.txt
  FOUND  'Order of work, and where it stops' -> docs/successor-experiment-proposal-2026-10-03-v4.md
  FOUND  'We are not working on a delayed calendar. We are working on a finish e' -> docs/outside-review-protocol.md, docs/rulings/2026-09-21-review-verification-and-staged-spending.md
== docs/rulings/2026-10-04-registration-review-opened.md
  FOUND  "John's step" -> docs/successor-experiment-proposal-2026-10-03-v4.md
  FOUND  'opened by John once version 4 is checked and its seven questions are a' -> source.txt
  FOUND  'The goal is to run everything as soon as possible based on what pre-re' -> source.txt
  FOUND  'everything is approved' -> source.txt
  NOWHERE 'opened by John once version 4 is checked and its seven questions are a' -> -
  FOUND  'run everything as soon as possible' -> source.txt
  NOWHERE 'everything is approved.' -> -
  NOWHERE "Yes, it's opened" -> -
  NOWHERE 'No, wait' -> -
  NOWHERE "Yes, it's opened" -> -
```

Reading the `NOWHERE` lines one by one. The second "opened by John…" and "everything is approved." are the same quotations inside the question put to John, where the sentence's full stop falls inside the quotation marks. The words match; only the full stop differs. "Yes, it's opened" and "No, wait" are the reported exchange, which this session cannot see (see above). "file the timing ruling" is given as John's instruction to file ruling 1. It is not in the supplied source, so it cannot be checked from here. None of these is a misquotation the record contradicts.

### Check 2: what commit `655b371` did to the roadmap data file (MEASURED)

Chosen so that a second weekend changing status, a copied goal, or a carried note without a weekend would each show.

```
$ python3 experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/roadmap_diff.py
weekend status changes:
  W2: active -> partial
  total weekends changed: 1 of 13
goal status changes:
  W2.1: planned -> carried
  W2.2: planned -> carried
  W2.3: planned -> carried
  W2.4: planned -> carried
  W2.5: planned -> carried
  W2.7: planned -> done
  goals before: 44, after: 44
goal ids in more than one place: none
goal texts in more than one place: none
carried goals: does the note name a weekend?
  W1.5: names 'weekend 2'
  W2.1: NAMES NO WEEKEND
  W2.2: NAMES NO WEEKEND
  W2.3: NAMES NO WEEKEND
  W2.4: NAMES NO WEEKEND
  W2.5: NAMES NO WEEKEND
```

### Check 3: claims about other records (MEASURED)

```
$ sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/record_claims.sh
== v4 opening list, item 3
26:3. **Opening the registration review is John's step.**
== v4 section 11 title
2465:## 11. Order of work, and where it stops
== protocol Amendments, the 2026-09-21 task-time quote
595:measured in task time, not calendar time. In his words, "We are not working on a
== pull requests 76, 79, 85 to 91 on origin/main (subject line, date)
d19f914 2026-10-03 Merge pull request #91 from jfredson/rulings-2026-10-04-solver-and-control-2
ecf3820 2026-10-03 Merge pull request #90 from jfredson/w2d-check-competing-solver-and-control-2
3fea27e 2026-10-03 Merge pull request #89 from jfredson/w2b-job2-control-2-twenty-draws
2b3fbee 2026-10-03 Merge pull request #88 from jfredson/w2b-job1-competing-solver-run
7a55fe0 2026-10-03 Merge pull request #87 from jfredson/rulings-2026-10-03-v4-check-questions
d425543 2026-10-03 Merge pull request #86 from jfredson/w2c-proposal-v4-check
41b0bd3 2026-10-03 Version 4 of the proposal, both records of the seven-question ruling, and John's ruling on which stands (supersedes 83 and 84) (#85)
e184a6e 2026-10-03 Check of the controls re-run of 2026-10-03: it reproduces exactly, and the too-early-position diagnostic holds (#79)
821f154 2026-10-03 Controls re-run under the registered rules: the ruled change holds; controls 2 and 4 go to John (#76)
== pull request 97 (the code freeze): on origin/main? in 655b371?
53ae82c 2026-10-04 17:08:06 -0700 Merge pull request #97 from jfredson/freeze-successor-code-2026-10-04
655b371 committed 2026-10-04 17:49:34 -0700
freeze merge is NOT in 655b371
== kill dates and what they bind
42-date = "2026-10-18"
43-title = "Kill date 1: the registration committed"
44-kind = "kill_date"
49-date = "2026-11-01"
50-title = "Kill date 2: the remaining eight registered runs launched"
51-kind = "kill_date"
277:    possible, but only on a fresh ruling that names what comes off the back end
292:    wants to spend. **The same ruling settles which step the second kill date
293:    binds**: the launch of the remaining eight runs (step 5b of the chain in
44:7. **The two kill dates are accepted**: registration committed by 2026-10-18;
== wrap-up and hibernation
34:wrap_up_start = "2026-12-21"
35:hibernation_by = "2027-01-04"
177:| 14. Wrap-up | Everything above, or a kill date having fired. **Starts 2026-12-21** (ruled); nothing new is launched after that date. | **Wrap-up** (ruled): hibernation condition per the program roadmap, **complete by 2027-01-04**. | — | Final ruling that the hibernation condition is met. |
== tier 1 counts quoted in W2.1
37:**One fatal finding, four serious, five worth-noting.** The fatal one is small
== John's go on the development runs (W2.4 note)
c9791c9 2026-10-04 Quote John's go for the four 10M development runs in their ledger rows, with its provenance
```

### Check 4: the site data check (MEASURED)

```
$ python3 scripts/export_site.py --check
export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas, 20 findings, 25 next steps, 43 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 44 goals, 4 milestones, 5 extensions)
exit=0
```

The output matches the one quoted in the message of `655b371`. Note that the check only requires a carried goal to have *some* note (`scripts/export_site.py` line 315). It does not test that the note names a weekend, which is why it passes despite Check 2.

### Check 5: places that still describe the weekly re-plan or a dated target as live (MEASURED)

```
$ sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/stale_timing.sh
CLAUDE.md:54:Friday re-plan edits `data/roadmap.toml`** (the coming weekend's goals, which
CLAUDE.md:56:the Sunday-night handoff sets each goal's status there** (a carried goal gets a
site/README.md:20:| `/roadmap/` | The weekend roadmap to 2026-12-21 from `data/roadmap.toml`: the question and the two rules (what weekdays carry, the weekly re-plan); ...
site/README.md:30:`data/roadmap.toml` is the structured twin of the weekend roadmap (...). The Thursday or Friday evening re-plan edits it (...), and the Sunday-night handoff sets each goal's status there (a carried goal gets a `note` naming the weekend it moved to) ...
6:# way, and the weekend log in prose). The Thursday/Friday re-plan edits both,
7:# and the Sunday-night handoff sets each goal's status here.
56:      <p><span class="kicker-inline">The weekly re-plan</span> {r.replan_rule}</p>
66:        <Meter value={goalsPct} caption={`${Math.round(goalsPct)}% of the goals that count. ${carried} carried to a later weekend, ...`} />
316:                raise Bad(f"{gw}: a carried goal needs a note saying which weekend it moved to")
681:when = "after the competing solver's run and the check of version 4; realistic commit date 2026-10-10/11; kill date 2026-10-18"
14:only a schedule laid over that dated line and gives way to it wherever the two
```

(The two `site/README.md` lines are shortened here; the full output is in `stale_timing.out.txt`. Lines 6, 7 are `data/roadmap.toml`; 56, 66 `site/src/pages/roadmap.astro`; 316 `scripts/export_site.py`; 681 `data/project.toml`; 14 `STATUS.md`.)

### Check 6: whether this branch still merges cleanly with the main line (MEASURED)

```
$ git merge-tree --write-tree --name-only HEAD origin/main
f12481bc8fc3c744af55e76b50894035c8a1dfe6
STATUS.md
data/project.toml

Auto-merging STATUS.md
CONFLICT (content): Merge conflict in STATUS.md
Auto-merging data/project.toml
CONFLICT (content): Merge conflict in data/project.toml
```

## Claim by claim

### Ruling 1: `docs/rulings/2026-10-04-no-future-dates.md`

- **The ruling as quoted ("stop scheduling … outer limits only").** Holds: word for word the supplied source (Check 1). MEASURED.
- **"The goal is to run everything as soon as possible…" and "everything is approved", about the registered training.** Hold against the source (Check 1). MEASURED.
- **"He gave the ruling in a planning session on 2026-10-04."** Not supported by the source as supplied. The source places the two *other* quotations in "the planning session", but the timing ruling's own sentence says only "John ruled 2026-10-04". This is probably true, but it is the session's inference. ARGUED. Defect 7.
- **"As John's message put it."** The quoted wording is in the third person ("John ruled 2026-10-04: …"), and the same message tells the session to "Confirm with John". That reads as a message drafted for the session and relayed, not John's own phrasing. The task brief says John typed it, and this session cannot see otherwise. Either way the ruling is John's, so **authorship john holds for the quoted ruling itself.** ARGUED. Defect 8.
- **"at John's instruction ('file the timing ruling')".** Cannot be checked: not in the supplied source (Check 1).
- **The 2026-09-21 quotation in the protocol's Amendments section.** Holds, word for word (Checks 1 and 3). MEASURED.
- **Version 4 has a section 11 titled "Order of work, and where it stops", and it orders work by what each step waits on.** Holds. The title is at line 2465 (Check 3), and the section is a chain of prerequisites whose step 2 says "No target date". MEASURED for the title; ARGUED for the description.
- **The first kill date, 2026-10-18, binds the registration commit; the second, 2026-11-01, binds the launch of the remaining eight registered runs.** Holds against `data/roadmap.toml` (milestones `K1` and `K2`), item 7 of the 2026-09-20 ruling and item 23 of the 2026-09-21 review-verification ruling (Check 3). MEASURED.
- **Wrap-up starts 2026-12-21; hibernation deadline 2027-01-04; both unchanged.** Holds: the same dates in `data/roadmap.toml` and row 14 of the December-result roadmap (Check 3). That John's ruling leaves them unchanged is the session's reading, though nothing in his words touches them. MEASURED / ARGUED.
- **"Passing a kill date still takes a fresh ruling naming what comes off the back end (ruled 2026-09-21)."** Holds. Item 23 of the review-verification ruling states it of launching past a date, and the first kill date's note in `data/roadmap.toml` and version 4 section 11, step 2, apply the same item to committing the registration. MEASURED (the texts).
- **"There is no weekly re-plan; the standing Thursday or Friday re-plan … retired."** The session's reading, though a close one: the re-plan existed to decide the coming weekend's goals and which weekend absorbs a slip, which is timing, and John said the weekend roadmap no longer sets timing. It should be marked as the session's reading. ARGUED. Defect 2.
- **"… and the Sunday-night handoff they describe are retired."** Does not follow from John's words. The handoff is not only timing. It writes the handoff entry at the top of `STATUS.md` and sets each goal's status in `data/roadmap.toml`, and the repository's `CLAUDE.md` still requires it. Recorded under "Authorship: john", this sentence retires a standing instruction John is not recorded retiring. ARGUED. Defect 2 (must-fix).
- **"The TimeAssembler task for that re-plan had already been closed."** Not checked (outside the repository).
- **"It continues an earlier ruling … This ruling takes the schedule off again."** The session's description of how the two rulings relate. The quotation it rests on holds, but the framing is the session's. ARGUED. Defect 2.
- **"No gate, check, review tier or spending rule changes. A step that waits on John … still waits on him."** The session's reading. It is sound and conservative, since nothing in John's words touches any of these, but it is not his ruling. ARGUED. Defect 2.

### Ruling 2: `docs/rulings/2026-10-04-registration-review-opened.md`

- **Version 4 says opening the review is "John's step" (opening list, item 3).** Holds, line 26 (Check 3). MEASURED.
- **The roadmap step says the review is "opened by John once version 4 is checked and its seven questions are answered".** Matches the supplied source (Check 1). The step itself is not in the repository, so this cannot be checked further.
- **The check of version 4 and the ruling on its questions are on the main line (pull requests 85 to 87); so are the competing-solver run, the twenty-piece control, their check and John's ruling on them (pull requests 88 to 91).** Holds: all seven are on `origin/main`, and their subject lines match those descriptions (Check 3). Pull request 85 is version 4 together with the seven-question records; 86 is the check of version 4; 87 is John's ruling on the questions that check raised. MEASURED.
- **The planning-session quotations, and that they were "not said about this review in particular".** The quotations hold (Check 1). The second half matches the source, which itself asks for confirmation before relying on them. MEASURED / ARGUED.
- **The question as put, the two answers offered, and that John chose "Yes, it's opened".** The file reports this the same way in each place, as do the commit message (`f96c9eb`) and the 2026-10-04 entry in `STATUS.md`. This session cannot see the exchange.
- **"He answered a direct question in his own choice of words; the session proposed nothing beyond the question."** Does not hold against the file's own account. He chose one of two answers the session wrote. The question also carried the session's framing of what was being opened ("both tiers … so I can run the inside review now and build the outside reviewers' packet"). ARGUED from the file's own text. Defect 1 (must-fix).
- **"What this opens": Gate A on version 4, both tiers; no registration commit, no launch, no spend.** Consistent with the question as put, and it claims nothing beyond it. ARGUED.

### Is "authorship: john" right?

The workspace rule (`~/Code/CLAUDE.md`, "Session logging") says: "`john` only when John stated the ruling himself, `mixed` when you proposed it and he approved."

- **Ruling 1:** right for the ruling itself, which is John's statement as relayed. **Not right for the sections "What it means in practice" and "What this does not change"**, which are the recording session's reading presented under his name. Those sections should be labelled as the session's own reading (authorship agent), or the contested part, the retired handoff, confirmed with John. ARGUED.
- **Ruling 2: should be mixed, or the file should argue explicitly why not.** The session wrote the question and both answers, including the framing of what opens. John chose one. That is "you proposed it and he approved". This repository has recorded the same shape as mixed before: the ruling on the fifth outcome and both figures (`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`) records a yes to a checking session's question as "Mixed authorship: the question was the checking session's, the choice is his". There is a case for john: opening the review is a step reserved to him, and the question only asked whether he had already taken it. But the file does not make that case. Instead it says he chose his own words, which he did not. ARGUED.

### The roadmap edits (commit `655b371`)

- **The site data check passes** (Check 4). MEASURED.
- **Exactly one weekend's status changed:** weekend 2, active → partial (Check 2). MEASURED.
- **No goal was copied into another weekend:** 44 goals before and after; no id or text appears twice (Check 2). MEASURED.
- **The W2.7 note (the controls re-run): "Done 2026-10-03 … (pull request 76), checked … (pull request 79); it reproduces exactly".** Holds: both are on the main line, dated 2026-10-03, and the subject of 79 says "it reproduces exactly" (Check 3). MEASURED.
- **The W2.1 note (the registration text through both review tiers): inside review ran 2026-10-04, one fatal and four serious findings (RT-237 to RT-246, pull request 94); outside packet built, checked and with John.** Holds. The findings file says "One fatal finding, four serious, five worth-noting" (Check 3). Pull request 94 exists and is open against `main`. The packet check and its re-check are filed in this folder. "With John" rests on `STATUS.md` only. MEASURED.
- **The W2.2 note (the registration commit).** Holds: kill date 1 is 2026-10-18 and the steps it waits on match version 4 section 11, step 2. MEASURED.
- **The W2.3 note (the code freeze): "Under way on its own step".** Stale at the moment it was committed. The code freeze merged to the main line as pull request 97 at 17:08 on 2026-10-04, 41 minutes before `655b371` (17:49), and is not in this branch (Check 3). The W2.4 note's "Waits on the code freeze (W2.3)" is stale the same way. Its "John approved the spend on 2026-10-04" holds against commit `c9791c9`. MEASURED. Defect 6.
- **The W2.5 note (the first run's go packet).** Holds as a statement of what it waits on. ARGUED.
- **Is "carried" without a weekend consistent with the file's own rule?** No. The header of `data/roadmap.toml` (lines 19 to 23) says "'carried' means the goal moved to a later weekend (say which in `note`)". The validator's message says the same, and the roadmap page's progress caption will now read "6 carried to a later weekend", which is false for five of the six (Check 2, Check 5). The honest representation is a status that says what is true: not done, and no longer assigned to any weekend. Suggested: add one goal status, for example `"open"` with the plain label "Open, no weekend", to the vocabularies in `scripts/export_site.py`, `site/src/lib/roadmap.ts` and the labels in `site/src/lib/project.ts`. Count it as not yet done, and define it in the file's header with the date and the ruling that created it. Set W2.1 to W2.5 to it. The smaller alternative is to keep "carried" but amend its definition in the header, the validator message and the page caption, with a dated note that from 2026-10-04 a carried goal may be taken off the weekend schedule rather than moved. ARGUED. Defect 3.
- **The dated note at the top of the weekend roadmap.** Accurate against the ruling file and `data/roadmap.toml`, except that it repeats the "Sunday-night handoff … retired" claim (Defect 2). It edits nothing else, as `git show 655b371` shows. MEASURED.
- **The changed paragraph in the 2026-10-04 `STATUS.md` entry.** Accurate about what was filed and changed. It repeats "authorship john" for the registration-review ruling (Defect 1). MEASURED.

## Defects

1. **Must-fix.** (Ruling 2, the registration review opened.) The sentence "He answered a direct question in his own choice of words; the session proposed nothing beyond the question" is false by the file's own account: John chose one of two answers the session wrote, to a question that carried the session's framing. Strike it. Record the authorship as mixed, matching the workspace rule and this repository's precedent (the fifth-outcome ruling of 2026-10-03), or argue in the file why john is right. Bring the 2026-10-04 `STATUS.md` entry and any worklog decision entry into line. ARGUED.
2. **Must-fix.** (Ruling 1, no future dates.) Under "Authorship: john", the file states that the Sunday-night handoff is retired. John's words, as supplied, retire the weekend roadmap's timing, not the handoff. The handoff also writes `STATUS.md` and sets goal statuses, and the repository's `CLAUDE.md` still requires it. Either confirm this with John or mark it as the session's reading. The rest of "What it means in practice" and "What this does not change" should also be labelled as the recording session's reading rather than John's ruling. That covers the retired re-plan, the continuation of the 2026-09-21 ruling, and that no gate, check, review tier or spending rule changes. Most of it is a sound reading and can stay; it should not be under his name. The same sentence about the handoff appears in the weekend roadmap's dated note. ARGUED.
3. **Can wait (fix before the site is next deployed).** `data/roadmap.toml` marks W2.1 to W2.5 "carried" with notes naming no weekend, against the file's own definition (header lines 19 to 23). The roadmap page will say "carried to a later weekend". The suggested fix is a new goal status meaning "not done, no longer assigned to a weekend", or a dated amendment to what "carried" means, as set out above. MEASURED (the mismatch), ARGUED (the fix).
4. **Can wait.** `data/roadmap.toml`'s header comment (lines 6 to 7) still says the Thursday/Friday re-plan edits the file and the Sunday-night handoff sets goal statuses. Weekends 3 to 13 keep their dates, "planned" statuses and dated items for John ("Friday night or Saturday morning: the go…"). The `one_line` field says the dates are no longer targets, but each weekend card on the page does not. MEASURED / ARGUED.
5. **Can wait (some need John).** Other places still describe the re-plan, the handoff or a dated target as live (Check 5). Each should be updated or given a dated note; none was edited here:
   - the repository `CLAUDE.md`, "Keeping the site current", the paragraph beginning "The Thursday or Friday re-plan edits `data/roadmap.toml`…" (John's instruction file, so his call);
   - `site/README.md`, lines 20 and 30;
   - `site/src/pages/roadmap.astro`, the "The weekly re-plan" label (line 56) and the "carried to a later weekend" caption (line 66);
   - `scripts/export_site.py` line 316, the validator message about which weekend a carried goal moved to;
   - `data/project.toml`, next step N15 (the registration text), whose `when` still reads "realistic commit date 2026-10-10/11", a future-date target the ruling retires;
   - the standing paragraph at the top of `STATUS.md` (lines 4 to 15), which still calls the weekend roadmap "a schedule laid over that dated line" in the present tense.
6. **Can wait.** The W2.3 note (the code freeze, "Under way on its own step") and the W2.4 note (the development runs, "Waits on the code freeze (W2.3)") were stale when committed. The freeze merged to the main line as pull request 97 at 17:08 on 2026-10-04, 41 minutes before `655b371`. Separately, this branch now conflicts with the main line in `STATUS.md` and `data/project.toml` (Check 6). Whoever merges the registration-review pull request (94) should resolve both and set W2.3 against the freeze's record. MEASURED.
7. **Can wait.** (Ruling 1.) "He gave the ruling in a planning session on 2026-10-04" goes beyond the source as supplied, which names the planning session only for the two other quotations. Soften it to "on 2026-10-04" or confirm it. The 2026-10-04 `STATUS.md` entry says "In the same planning session he ruled" and should follow. ARGUED.
8. **Can wait.** (Ruling 1.) "As John's message put it" introduces text written in the third person ("John ruled 2026-10-04: …") that also tells the session to "Confirm with John". It reads as a relayed statement of his ruling rather than his own phrasing. A plain note saying so would let a later reader weigh the wording correctly. This does not change the authorship of the ruling itself. ARGUED.

*Not a defect, noted for the next filing:* on the main line, the code freeze (pull request 97) created `experiments/08-successor-degree/`, which has no `reviews/` folder yet. Once it has one, later checks that most affect the successor may belong there rather than here.
