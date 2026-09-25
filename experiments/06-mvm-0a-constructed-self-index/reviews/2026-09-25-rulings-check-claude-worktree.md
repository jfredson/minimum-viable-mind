# Check of the two rulings of 2026-09-25 against the proposals they rule on

*Filed 2026-09-25 (Pacific) by a Claude Code session in its own worktree
(branch `worktree-rulings-check-2026-09-25`, started from
`origin/rulings-2026-09-25` at `52e9bc1`). This session wrote neither ruling
file and neither proposal. **It does not rule, and it did not edit either
ruling file**, the proposals, the ledger or any registered text. This is the
check the pairing rule in `docs/outside-review-protocol.md` asks for before
sessions (c) and (d) rely on these rulings.*

**What was checked.**

- `docs/rulings/2026-09-26-weekend-1-queue.md` (the Weekend 1 ruling, nine
  pages), against `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md` (the
  proposal packet, as merged with its check, pull request 35).
- `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md` (the ruling on the
  two outside reviews of the A3 closure text, 22 items), against
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md` on pull
  request 37. I read it at `06a5636`. The branch then moved to `bbf69a2`, and I
  diffed that too: its only change rewords where the two reviewer files were
  committed (on main, in `c89a3ef`). **No recommendation changed.**

For each ruling I asked three things. Does it match the recommendation? If not,
is it one of the five departures the brief names (the page 3 rider; K5 "not
reached"; item 12 narrowed; item 16's headline; 19(e) held)? And does every
path, commit hash and number it cites actually resolve?

---

## The answer in five lines

1. **Every ruling matches the recommendation or is one of the five named
   departures.** None of the 9 pages and none of the 22 items quietly departs
   from its proposal on substance.
2. **Every commit hash resolves and is on this branch.** Every repository path
   resolves except one, the tier 2 proposal file, which is only on pull
   request 37 (still open). Every number I traced is in the file it comes from.
3. **One statement of fact is untrue today.** Page 8b says "The TimeAssembler
   task is closed". The task is still `todo`, and so are the two tasks the
   Weekend 1 ruling says "close" (details in W5 below).
4. **One condition cannot be met as written.** Item 19(e) is to be adopted only
   if someone shows it "from `standardised-refit-findings.md`". The merged
   check of pull request 37 found that this file does *not* show it; the code
   and the run's output files do (T4 below).
5. **The rest are small wording points** (W1–W4, T1–T3). None changes a ruling.

---

## Part 1: the Weekend 1 ruling, page by page

| Page | Recommendation in the packet | What was ruled | Verdict |
|---|---|---|---|
| 1a | Separation bar 0.5, on the scale page 2 chooses | 0.5, on the chance-corrected scale | matches |
| 1b | The rehearsal's own pre-stated test for each condition; the two competing solvers reported as reference points only | same, including 0.2630 on 3,000 episodes | matches (0.2630: rehearsal line 630) |
| 1c | Floor at four fifths of the arm's own accuracy; smallest layer set that clears it; the all-layers set excluded by name | same | matches |
| 1d | Rank cap 8 on every arm; also report caps 1, 2, 4 and 8 | same | matches |
| 1e | Register the rule that generates the site list, with the toy's count printed beside it | same; 176 comparisons; one label, which marker word | matches. 176 is the packet's own arithmetic (44 site sets × 4 caps × 1 label), not a quote from a file |
| 1f | Three seeds per arm; say the toy arithmetic was not carried across | same | matches |
| 1g | Spread across seeds as the main measure, bootstrap beside it; say neither measures drift between runs | same | matches |
| 1h | Collapse means falling below the 1b bar; the named-other clause is reported, not used as a gate; applies to arm F only | same | matches |
| 2 | The chance-corrected form | same; the "no normalisation" sentence replaced; room left for a miss of up to 0.0175 | matches (0.0175: rehearsal line 506) |
| 3 | Option (i) | option (i) **plus the rider** (report every arm's reading at arm T's sites and rank too) | **named departure.** The rider is the fix the packet itself offers under "Strongest argument against" |
| 4 | Try redesign (b), with (a) alongside it; fall back to (d) by Sunday | same; Sunday is 2026-09-27 (checked: it is a Sunday) | matches, but see T1 on stop condition S1 |
| 5 | Option (iii); fold the fourth arm in only if it reads 0.3 to 0.7 on all three seeds | same; $32 to $44 | matches, plus one addition (W3) |
| 6 | Record the $130 cap as superseded; envelope to $450; trip wire at 1.25 on both ratios | same; the pre-authorisation scheme is expressly not adopted | matches, but see W2 |
| 7 | Option (ii) | option (ii) | matches |
| 8a | Option (i): a dated note beside F17, the original left alone | same; counts 15, 15 and 7 | matches |
| 8b | Option (i): ratify in John's own words, and nothing wider | same | matches, but see W1 and W5 |
| 9 | Option (i): the go in the page 9 shape, after the plan check is filed and the no-sleep setting is on | same; no go issued | matches, but see T3 |

### Points on the Weekend 1 ruling

**W1. Page 8b says "Ratified in John's own words".** The ruling's own list of
what John said gives page 8 as "yes" (to option (i) on both items). The packet
set a bar here: option (i) is John saying "in his own words" what the rule is,
because its strongest counter-argument was that "a ruling about touching
registered text is the one kind that should not rest on a click". A spoken
"yes" to a sentence someone else drafted is more than a click. But it is not
the rule in John's own words, and the ruling's preamble says "none of the
wording is his drafting". Whether "yes" meets the bar is John's call. As
written, the ruling claims more than its own record shows.

**W2. Page 6 leaves out one clause of the trip wire.** The packet's summary
of the spending proposal includes: "a machine already in flight is left to
finish if its projected total is inside estimate times the measured ratio and
the balance covers it". The ruling says "halt, not trim" and nothing about
machines already running. Read literally, it halts those too. That may be what
John meant. But neither the packet nor the ruling says the clause was dropped,
and the "halt, not trim" rule it refers back to (item 13 of the 2026-09-21
ruling) was ruled before this clause existed.

**W3. Page 5 adds "its predicted reading stated before it runs".** The packet
asked for a pass line stated in advance (0.3 to 0.7). The ruling also asks for
a predicted reading stated in advance. That is a small addition, with the
packet's intent and not against it, but it is not in the recommendation.

**W4. Line 29 is hard to read.** "page 9, "Agree" was not spoken as a go;
the go itself is separate, see page 9." It is not clear whether John said
"Agree" to page 9's shape. Page 9's heading says the shape and order were
ruled, so presumably he did. Worth one plain sentence.

**W5. Status claims about TimeAssembler tasks** (checked with `list_tasks`,
2026-09-25). Page 8b says "The TimeAssembler task is closed." The task "DECIDE
(John): how to correct a measured value in REGISTERED text…" (`6aea06f0`) is
still **todo**. The section on two tasks ruled earlier says "Both close". That
task (`6aea06f0`) and "DECIDE (John): the entangled and free arms' numbers are
one sample…" (`588ac12c`) are both still **todo**. So are the tasks for the
questions this ruling answers: the A4 key count (`77dfc3b0`), the Wittgenstein
criteria (`9cc76c1b`), the named-other condition (`6291803f`), the middle of
the scale (`62c54720`) and spend (`3e5b2f7a`). If "is closed" means "is to be
closed", the text should say so. Either way the tasks still need closing. I did
not close them.

---

## Part 2: the A3 tier 2 ruling, item by item

| Item | Recommendation | What was ruled | Verdict |
|---|---|---|---|
| 1 | Name K5; say it was **not reached**; annotate beside RT-164 | same; stated as John's reading of registered text | **named departure (K5 not reached).** On substance it is the recommendation. What departs is that it is now stated firmly and in John's name, where the proposal had only medium confidence |
| 2 | Gemini's wording | same | matches |
| 3 | Credit in part, not for the money | same, "(see 8)" | matches. The proposal said "see item 12"; the ruling's "see 8" is the correct cross-reference |
| 4 | Accept as credit, read with 13 | same | matches |
| 5 | "the input-channel lesion, the only lesion A3 ran" | same | matches |
| 6 | Credit; "per-row gradient weight quadrupled" | same | matches |
| 7 | ChatGPT's sentence; 135 each; "at the discovery positions" | same | matches |
| 8 | The ledger's figures with an "as of" date | about $46.2 of $100; about $227.6 of $400; as the ledger read on 2026-09-21 | matches; see T2 |
| 9 | Drop 2026-10-11; keep 2026-10-18 and 2026-11-01 | same | matches |
| 10 | Record of the packet's limits; no text change | same | matches |
| 11 | Main point accepted; sub-point declined | same | matches |
| 12 | Narrower than ChatGPT's version: keep the ruled phrase and bound it | same wording | **named departure (item 12 narrowed)**, and it is the recommendation |
| 13 | Credit; "see item 15" | credit; "see 22" | matches. "22" is the correct cross-reference |
| 14 | ChatGPT's replacement | same | matches |
| 15 | Add ChatGPT's paragraph citing both rulings | same | matches |
| 16 | ChatGPT's headline | quoted in full | **named departure (item 16's headline)**, and it is the recommendation. The quote matches `reviews/2026-09-21-a3-closure-chatgpt.md` line 256 word for word |
| 17 | Add the same-act limit | same | matches |
| 18 | ChatGPT's replacement; keep the correction citation | same | matches |
| 19 | Accept (a), (c), (d), (f); change (b); hold (e) until the version 5 writer shows it | same, but (e) can also be shown by "the dispositions check" | **named departure (19(e) held)**, and see T4 |
| 20 | Annotate beside the file which model and mode ran | the annotation's content is supplied (Codex app; "ChatGPT 6 Astra Medium"; 22 parts; no lookup verified) | matches. The content is new information from John, not from the proposal. "22 parts" agrees with the file ("All 22 files arrived") |
| 21 | Number from RT-204; reconcile RT-172 to RT-203 later | same | matches |
| 22 | Version 5 writer ≠ drafter; tier 1 check; then the registration commit; no second tier 2 round | same, item list identical (1, 2, 5–9, 11, 12, 14–19) | matches |

The preamble's counts check out: 4 serious findings from Gemini and 11 from
ChatGPT make 15 (counted from the severity columns), and neither file has a
fatal finding.

### Points on the tier 2 ruling

**T1 (Weekend 1, page 4). The ruling on stop condition S1 goes beyond the
packet, which made no recommendation on it.** The packet says of S1: "This
packet does not choose; disagreement 5 in the index". The ruling states "S1
did not fire … This is John's ruling, adopting the rehearsal's adjudication."
So this is not a departure from a recommendation, because there was none, and
the brief does not list it. It is a ruling on a question the packet left open,
and the reasoning given is the rehearsal's. I note it because the brief asked
me to account for everything that is not the recommendation.

**T2. Item 8 and page 6 were ruled on the same evening, and they now pull
against each other.** Item 8 has version 5 quote "about $227.6 of the $400
programme ceiling as the ledger read on 2026-09-21", and re-read the ledger
the day version 5 lands. Page 6 of the other ruling raises the envelope to
$450 and has the ledger's header updated. If the ledger is updated before
version 5 lands, a re-read will show $450. Item 8's "as of" wording keeps $400
historically correct. But the version 5 writer should be told that the
ceiling itself moved on 2026-09-25, so the money paragraph does not look stale
the day it is registered. A note for the version 5 brief, not a defect in
either ruling.

**T3 (Weekend 1, page 9). The plan check now exists but has not been merged,
and it reports a gap.** The ruling says the check "was commissioned as
session 'MVM W1f plan check'", which was true when written. Pull request 38
(branch `worktree-rented-slice-plan-check`, open) is titled "Check the
regenerated rented-slice plan (60d1496): commands right, one outcome missing".
Condition (1) of page 9 asks for a *filed* check. Whether an open pull request
with a reported gap counts is for whoever puts the go to John. I did not read
pull request 38's contents.

**T4. Item 19(e) cannot be met the way it is written.** The ruling adopts
19(e) only if "the dispositions check or the version 5 writer shows it from
`standardised-refit-findings.md`". The dispositions check has since been filed
(pull request 40, squash-merged to main as `640638d`, file
`reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`; not on this
branch). It found:

- the findings file does **not** show the claim, and read alone it points the
  other way ("by the scaling and by nothing else", lines 62–65, true only of
  the anchor check);
- the committed code and the run's three output files **do** show it: the
  per-test seed hashes the target name, the two runs use different names, and
  each output file's `seeding` field says no test shares a split.

So ChatGPT's 19(e) is right, but not "from `standardised-refit-findings.md`".
Read literally, the condition is not met, and (e) stays out of version 5. Read
by intent ("shown from the record"), it is met. **This needs John**, or at
least a sentence in the version 5 brief, before the version 5 writer meets it
cold. The check also notes that the findings file's own sentence overstates.
That is a separate wording problem, not ruled.

**T5. Wording on the two proposals' cross-references.** In items 3 and 13 the
ruling quietly corrects the proposal's wrong cross-references ("item 12" to 8,
"item 15" to 22). Both corrections are right. I mention them only so nobody
reads them as departures.

---

## Part 3: citations resolved

### Commit hashes (all resolve, all on this branch)

| Hash | Cited for | What it is |
|---|---|---|
| `285903e` | the 8b note | 2026-09-21 "Pre-registration: dated note naming the record that holds the cue-detector figure" |
| `eeedb2f` | the 8b note | 2026-09-21 "Pre-registration note: give the battery keys…" |
| `57eb09d` | the 8b note | 2026-09-21 "Pre-registration note: give the question John was shown…" |
| `60d1496` | the page 9 plan | 2026-09-21 "Regenerate the plan file on main, with step 0 withdrawn". This is the last commit to touch `experiments/rehearsal-successor-measure/out/rented-slice-plan.txt` |

These three are the only commits to `pre-registration.md` since 2026-08-16.

### Paths

All resolve on this branch, except:

- `docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md`: only on
  pull request 37, which is **open**. The ruling points at a file that main
  does not have until that pull request merges. The merge order matters here:
  merging 37 first would make this pointer land.
- `~/Documents/Code/CLAUDE.md`: outside the repository. It exists, and
  `~/Documents/Code` is a link to `~/Code`.
- `launch_a3_fetch_first.sh`, named bare: resolves to
  `experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`.
- `pre-registration.md`, named bare at lines 170 and 200: four files share the
  name. The surrounding text means experiment 06's, which is the only one
  with the cue-detector note.

### Numbers and quotations, traced to their source

| Claim | Source | Found |
|---|---|---|
| $130 cap, item 4 | `docs/rulings/2026-09-20-december-result-roadmap.md` line 30 | yes |
| items 10, 11, 12, 19, 20; correction of 2026-09-22; about $44 and about $131 | `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` lines 60, 65, 69, 191, 204, 362, 401 | yes |
| 15, 15 and 7 keys; "110" | same file, lines 208–213; `red-team-a4.md` line 640 (still has no note beside it) | yes |
| the form of the existing note | `red-team-a4.md` line 82, "Added 2026-09-21 by a later session…" | yes |
| trip wire 1.25; sections 5.3 and 5.4 | `docs/preauthorised-spending-proposal-2026-09-21.md` lines 577, 594, 626 | yes |
| stale "$200" header | `compute-ledger.md` line 3 | yes |
| the envelope figure | `data/project.toml` line 625 ("MVM-0a registered design envelope") | yes |
| 0.2630; 0.0175; 12 layers | `docs/2026-09-21-successor-measure-rehearsal.md` lines 630, 506, 788 | yes |
| the "Friday evening" clause that moves the queue earlier | `docs/weekend-roadmap-2026-09-24.md` section 7, line 467 | yes |
| session (c) is the rehearsal repairs | same section, lines 421–426 | yes |
| $227.63, $402.63, $3 to $15, $32 to $44 | the packet's own sums of ledger rows (page 6 and page 5 tables); arithmetic checked: 450 − 402.63 − 44 = 3.37, and 450 − 402.63 − 32 = 15.37 | yes |
| K5 wording | `amendment-a3.md` line 265 | yes |
| §3.2's convergence requirement | `amendment-a3.md` §3.2 step 4 | yes |
| RT-96, RT-125, RT-164 ("Done in version 3."), last row RT-171 | `red_team_ledger.md` lines 531, 652, 756, 763 | yes |
| RT-204 not yet used | the highest finding number used elsewhere is RT-203; RT-204 appears only in this ruling | yes |
| patching not built for A3 | `docs/rulings/2026-09-20-december-result-roadmap.md` item 2, lines 18–23 | yes |
| kill dates 2026-10-18, 2026-11-01; 2026-10-11 withdrawn | same file lines 17, 44–45, 95 | yes |
| "every write-up must say so" | `pre-registration.md` line 84 | yes |
| about $46.2 of $100; about $227.6 of $400 | `compute-ledger.md` line 293 (the correction of 2026-09-21) | yes |
| review headers: "ChatGPT 6 Astra Medium", "Gemini 3.1 Pro", both dated 2026-09-25 | `reviews/2026-09-21-a3-closure-{chatgpt,gemini}.md` lines 1–2 | yes |
| item 16's headline | `reviews/2026-09-21-a3-closure-chatgpt.md` line 256 | yes, word for word |
| `standardised-refit-findings.md` exists | experiment folder | yes (but see T4) |
| pull request 35 checked the packet | pull request 35, merged | yes |

---

## Part 4: `scripts/check_citations.py` on both files

Run from the repository root at `52e9bc1`:
`python3 scripts/check_citations.py --only docs/rulings/2026-09-26-weekend-1-queue.md --only docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`.
It exits with status 1.

```
==============================================================================
check_citations.py - do the pointers land, and are the cited numbers there?
==============================================================================
Documents read: 2   scope: live

------------------------------------------------------------------------------
PART (a): does every file a document names exist?
------------------------------------------------------------------------------

[CONFIDENT] 1 reference(s) name a file that is not in the repository
  docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md:3
      names: docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md
      in:    Mixed authorship: the draft dispositions were proposed by the Claude Code session "MVM W1 A3 dispositions" in `docs/rulings/2026-09-25-a3-closure-tier2-disposit

[LOOK AT IT] 2 bare name(s) match more than one file
  docs/rulings/2026-09-26-weekend-1-queue.md:170  pre-registration.md
      could be: experiments/01-self-indexing-removal-test/pre-registration.md
      could be: experiments/03-retained-independence/pre-registration.md
      could be: experiments/06-mvm-0a-constructed-self-index/pre-registration.md
      could be: experiments/07-embodiment-amplifier-test/pre-registration.md
  docs/rulings/2026-09-26-weekend-1-queue.md:200  pre-registration.md
      could be: experiments/01-self-indexing-removal-test/pre-registration.md
      could be: experiments/03-retained-independence/pre-registration.md
      could be: experiments/06-mvm-0a-constructed-self-index/pre-registration.md
      could be: experiments/07-embodiment-amplifier-test/pre-registration.md

[LOOK AT IT] 0 name(s) of run-output files that are not in the repository
             (this repo does not commit `artifacts/`, so most of these point at
              uncommitted output rather than at a broken citation)

[LOOK AT IT] 0 reference(s) written with a gap or a wildcard that matched nothing

[NOT CHECKED] 2 reference(s) to files outside this repository
     2x  ~/Documents/Code/CLAUDE.md

[NOT CHECKED] 0 reference(s) to paths .gitignore keeps out of the repository (run outputs and caches, deliberately not committed)

------------------------------------------------------------------------------
PART (b): is a figure given with a citation actually in the file cited?
------------------------------------------------------------------------------

[CONFIDENT] 2 exact figure(s) absent from the one file their sentence cites
  docs/rulings/2026-09-26-weekend-1-queue.md:148
      figure: 12.2    cited: data/project.toml
      in:     *Changes:* the annotation on the 2026-09-20 ruling; proposal version 2, sections 12.2 and 12.4; the compute ledger's header (the stale "$200" line and a new envelope line); `data/project.toml`; the tr
  docs/rulings/2026-09-26-weekend-1-queue.md:148
      figure: 12.4    cited: data/project.toml
      in:     *Changes:* the annotation on the 2026-09-20 ruling; proposal version 2, sections 12.2 and 12.4; the compute ledger's header (the stale "$200" line and a new envelope line); `data/project.toml`; the tr

[LOOK AT IT] 0 figure(s) worth a human eye

==============================================================================
Confident findings: 3. Things for a human to look at: 2.
A confident finding is not a verdict. Read the sentence before acting on it,
and read the 'what this cannot check' note at the top of this file before
reading a clean run as reassurance.
==============================================================================
```

With `--small-integers` added, part (b) reports two more, both on line 165:
the figure 15 (twice) is not in `red-team-a4.md`.

**Reading the checker's findings.**

- The missing proposal file is real and expected: it is on pull request 37,
  which is still open (see Part 3).
- 12.2 and 12.4 are false alarms. They are section numbers of the successor
  proposal, and the checker paired them with `data/project.toml` because both
  sit in the same sentence.
- The 15s are expected. The key counts come from the endpoint records, by way
  of item 20 of the 2026-09-21 ruling, and the note that will put them into
  `red-team-a4.md` has not been written yet.
- The two `pre-registration.md` matches mean experiment 06's file, from the
  surrounding text.

The checker cannot see whether a figure means what the sentence says, so the
tracing in Part 3 was done by reading.

---

## What this session did not do

It did not rule, edit either ruling file or either proposal, close any
TimeAssembler task, read pull request 38's plan check, launch anything, or
spend anything.

---

## Re-check of commit `cdc5869` (2026-09-25)

*Added by the same session that filed the check above, at John's request:
"Re-check that commit's diff against your review." The commit ("apply the
rulings check's findings…") changes only the two ruling files. It adds 26
lines and removes 10. I read the whole diff. This session still does not rule
and did not edit either ruling file.*

### Each point, against the diff

| Point in the check above | What `cdc5869` does | Verdict |
|---|---|---|
| W1: 8b "in John's own words" | Now reads "Ratified by John ("yes" to option (i), on the wording below put to him)" | **fixed.** The record and the claim now agree |
| W2: trip wire leaves out the clause for machines already running | Adds: "A machine already in flight is left to finish only if its projected total is inside estimate times the measured ratio and the balance covers it (the spending proposal's own clause, section 5.4)" | **fixed.** The clause is in `docs/preauthorised-spending-proposal-2026-09-21.md` §5.4, item 2 ("A pod already in flight is left to finish if…"), with the same meaning. Cosmetic: the added line is not wrapped like the rest of the file |
| W4: line 29 unclear | Now: page 9, "Agree" (to the shape and the order only; it was not spoken as a go, and this file issues none) | **fixed** |
| W5: "The TimeAssembler task is closed" | 8b: "The TimeAssembler task (`6aea06f0`) is to be closed by the Sunday handoff session". The closing section names `588ac12c` and `6aea06f0` "along with every other TimeAssembler task these rulings answer" | **fixed.** Both ids are the right tasks (checked against `list_tasks` earlier today). The text no longer claims anything that is untrue |
| T2: the ceiling moved to $450 the same evening | Item 8 adds that the ceiling was raised to $450 (Weekend 1 ruling, page 6) and that "version 5 states the ceiling as $450 with that ruling cited" | **applied**, with a small wording point, R2 below |
| T4: the 19(e) condition cannot be met as written | (e) changes from "held" to "**adopted**". It cites the dispositions check (pull request 40) and the output files' wording ("no test shares a split with the unscaled run's"). It says the findings file does not show it and that its "by nothing else" overstates. Version 5 cites the check, not the findings file | **resolved on substance**, and the description of the check is accurate. See R1 on who made the call, and R3 on where the pointer lands |
| W3, T1, T3, T5 | not touched | these were notes, not defects. T3 (the plan check on pull request 38) is still open and is still for whoever puts the go to John |

### New points from the re-check

**R1. The 19(e) change is a change of ruling, and the text does not say whose
it is.** As ruled first, (e) was held on a condition. The condition, read
literally, was not met, and the new text adopts (e) on different evidence.
That is a reasonable reading of intent, and my check said it needed John. The
commit's author is John, but the preamble's record of his words ("Agreed on
all") comes from before this change, and item 19 does not say that John
adopted (e), or when. A few words such as "(John, 2026-09-25)" would make the
authorship something a reader can check, as the file does for everything else.
It also means the brief's list of departures ("19(e) held") is out of date for
this file.

**R2. Item 8 now reads as two instructions on the ceiling.** Its first
sentence still has version 5 give "about $227.6 of the $400 programme ceiling
as the ledger read on 2026-09-21". The added sentence says version 5 "states
the ceiling as $450". A careful writer will read this as: the spend is as of
2026-09-21, and the ceiling is now $450. But the first sentence, taken alone,
still tells them to print $400. Something like "about $227.6 spent as of
2026-09-21, against a ceiling since raised to $450" would leave one
instruction. This is wording only.

**R3. The new pointer resolves on main, not on this branch.**
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`
came in with pull request 40, which was squash-merged to main after this
branch started. The pointer lands once pull request 39 reaches main (checked:
the file is on `origin/main`). The tier 2 proposal pointer still waits on pull
request 37, as before.

### `scripts/check_citations.py` on both files at `cdc5869`

Same command as in Part 4. Exit status 1. Part (a):

```
[CONFIDENT] 2 reference(s) name a file that is not in the repository
  docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md:3
      names: docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md
  docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md:82
      names: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-dispositions-check-claude-worktree.md

[LOOK AT IT] 2 bare name(s) match more than one file
  docs/rulings/2026-09-26-weekend-1-queue.md:173  pre-registration.md
  docs/rulings/2026-09-26-weekend-1-queue.md:207  pre-registration.md

[NOT CHECKED] 2 reference(s) to files outside this repository
     2x  ~/Documents/Code/CLAUDE.md
```

Part (b):

```
[CONFIDENT] 2 exact figure(s) absent from the one file their sentence cites
  docs/rulings/2026-09-26-weekend-1-queue.md:151   figure: 12.2   cited: data/project.toml
  docs/rulings/2026-09-26-weekend-1-queue.md:151   figure: 12.4   cited: data/project.toml

Confident findings: 4. Things for a human to look at: 2.
```

This is the same as the first run, plus one new finding: the pointer at line
82, which is R3 and not a broken citation. Only line numbers have moved.

### Result

Every finding the commit set out to apply is applied correctly, and nothing in
the diff contradicts the proposals or the record. Three small points remain,
none of which changes a ruling: R1, whose name 19(e)'s adoption goes under;
R2, the wording of the item 8 ceiling; and R3, the merge order for the new
pointer.
