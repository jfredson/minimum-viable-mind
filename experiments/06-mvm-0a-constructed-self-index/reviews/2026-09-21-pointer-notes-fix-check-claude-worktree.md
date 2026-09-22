# Check of the six pointer-and-money fixes — 2026-09-21

*A checking pass by a Claude Code session in its own worktree. This session did
not write any of the six fixes and did not fix anything here. It exists because
of the first of the four rules John authorised on 2026-09-21 — item 22 of the
ruling on review verification and staged spending
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`): a session
that writes binding text is always paired with a different session that checks
it.*

*What was opened: the two fix branches, the triage they were built from, the
files they annotate, the two data records the registered-text note rests on, and
the repository's commit history. Every number and every commit named below was
re-derived in this worktree; nothing was taken from the writing sessions'
accounts or from the triage.*

*Every finding is marked **MEASURED** (a command was run and its output is
reported) or **ARGUED** (reasoning from the documents, which a reader can
dispute).*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## What was checked

Two branches, six fixes.

**The annotation branch** (`worktree-agent-a2cba20f89cc11b74`), four commits on
top of the main line as it stood at commit `73aa7e3`:

- `2086036` — deletes three `src/` prefixes in the reserve bank's authoring
  notes (`experiments/03-retained-independence/reserve-bank/authoring-notes.md`).
- `0c2d481` — a dated note on red-team pass 3
  (`experiments/06-mvm-0a-constructed-self-index/red-team-pass-3.md`) about a
  chance floor that moved.
- `9cb9575` — dated notes in the control-clause proposal
  (`docs/control-clause-proposal-2026-09-19.md`) and the independent Amendment A4
  review (`experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`) about
  two withdrawn files.
- `285903e` — a dated note on the pre-registration
  (`experiments/06-mvm-0a-constructed-self-index/pre-registration.md`), which is
  registered text.

**The trim branch** (`worktree-agent-ad4721f18c398ff46`), commit `e37566f` on top
of `fcc2a14`: notes on the two live proposals, written long and then cut to about
five lines with the detail moved to an appendix.

The triage both branches were built from is `0116bc7` on
`worktree-agent-a3928053ab2f57b6d`.

---

## Verdict in one paragraph

Five of the six fixes hold. The history work behind them is unusually good: every
commit identifier, title, timestamp and file state they assert was re-derived
here and matched, and in three places the writing sessions corrected the triage
and were right to. **Two findings stand.** One is fatal and sits in the
registered-text note: it translates two registered battery labels into plain
English and gets both wrong, in a way that collides with two other things the
same registered document names. One is serious and sits in the reserve-bank fix:
it edits a dated record rather than annotating it, on the one item where the
triage's own evidence shows the record was accurate when written. Two further
items are worth noting. The trim is clean and loses nothing.

---

## Findings

| # | Item | Where | Severity | Kind |
|---|---|---|---|---|
| 1 | The registered-text note misdescribes two registered battery labels | pre-registration note, `285903e` | **fatal** | MEASURED |
| 2 | The reserve-bank fix edits a record that was correct when written | authoring notes, `2086036` | **serious** | MEASURED |
| 3 | "Rebuilt hours later" was nine and a half minutes | pass-3 note, `0c2d481` | worth-noting | MEASURED |
| 4 | The only authority for annotating registered text is an unquoted, unfiled ruling | pre-registration note, `285903e` | worth-noting | ARGUED |
| 5 | The note splits a registered list in two | pre-registration note, `285903e` | worth-noting | ARGUED |

---

### Finding 1 — the registered-text note misdescribes two registered battery labels. **FATAL. MEASURED.**

This is the one the permission does not cover.

The note's second paragraph says the record of frozen batteries holds the four
chance floors the registered sentence lists, and names them in plain words:

> 0.125 for the **self-report** and **self-identification** batteries, 0.041666…
> for the cross-turn state battery, and 0.100 for the syntax floor check.

The two floors of 0.125 belong, in the record, to the keys `T_sr` and `T_si`. The
pre-registration defines both — in its own battery table, thirty-four lines below
the bullet the note is attached to:

    | **T_sr** (self-relevant binding) | ... |
    | **T_si** (self-irrelevant integration) | ... matched-difficulty
      integration over episode content with **no self-reference** ... |

So `T_sr` is self-*relevant* binding, not self-report, and `T_si` is
self-*irrelevant* integration, not self-identification. The note's gloss of `T_si`
inverts it: `T_si` is the battery defined by having **no** self-reference, and
"self-identification" says the opposite.

It is worse than a loose paraphrase, because both substituted names are already
taken, by two different things in the same registered document:

    | ~~S (self-report)~~ | ... | **Retired for MVM-0a (RT-04, §Scope).** ...
      A **forced-choice self-identification** probe is retained as a
      *secondary task measure only* — explicitly not a report channel and
      never scored as one. |

"Self-report" is the name of a battery the registration **retired**.
"Self-identification" is the name of a secondary probe the registration says is
"explicitly not a report channel and never scored as one". A reader who takes the
annotation at its word comes away believing the registration's two 0.125-floor
batteries are a self-report battery and a self-identification battery. The
registration says one is self-relevant binding, the other is the no-self-reference
control, and that self-report was dropped.

Commands run:

    git show main:experiments/06-mvm-0a-constructed-self-index/pre-registration.md | sed -n '236,244p'
    git grep -n 'T_sr.*self-report\|self-report.*T_sr' main -- '*.md'

The second command returns seven hits and every one of them is the retired-battery
row, which distinguishes retired self-report (`S`) from `T_sr` rather than
equating them. Nowhere in this repository is `T_sr` glossed as "self-report".

**Why this is fatal rather than serious.** The note's own opening sentence sets
the standard it must meet: "nothing below alters, qualifies or extends any
registered claim. This note does one thing: it names the committed record". The
permission it was written under — that registered text may carry a dated note
where the claim does not change — covers naming a record. Translating registered
labels is not naming a record, and translating them wrongly puts a false
description of registered content inside the registered file, under a banner
saying nothing registered has been touched. That banner is what makes it fatal:
a reader is told, in bold, that they can trust the note not to change the
registration's meaning.

**The narrow fix**, for whoever writes it: give the keys and let the
registration's own table do the defining — "0.125 for the two task batteries
`T_sr` and `T_si`, 0.041666… for the cross-turn state control `T_state`, and
0.100 for the syntax floor check `T_syntax`" — or use the registration's own
words, self-relevant binding and self-irrelevant integration. The plain-language
rule asks for the plain word over the term of art, but it does not license
renaming a registered quantity, and where a label is registered the plain move is
to quote the registration's gloss rather than invent one.

**Everything else in that note checks out**, and it is worth saying so plainly,
because the rest of it is careful. MEASURED:

    git show main:experiments/06-mvm-0a-constructed-self-index/batteries/batteries_meta.json

returns exactly four chance floors — `T_sr` 0.125, `T_si` 0.125, `T_state`
0.041666666666666664, `T_syntax` 0.1 — and **no detection figure of any kind**.
The note's claim that the pointer is correct for the clause it sits in, and that
the file holds no area-under-the-curve number, both hold.

    git show main:experiments/06-mvm-0a-constructed-self-index/cue_detector_gate.json

returns, for the first run, `"run": "(i) curriculum text"`, `n_episodes` 4000,
`seed` 20260804, clean `auc` **0.5008**, `ci95` **[0.4773, 0.5242]**,
`equivalence_bound` [0.45, 0.55], positive control `auc` **0.8627**, `GATE`
**"PASS"**. Every figure the note quotes is exact. The rounding claim holds too:
`round(0.4773, 3)` is 0.477 and `round(0.5242, 3)` is 0.524, and 1/24 is
0.041666666666666664, which the registered text renders 0.042.

**The registered sentence is byte-identical.** MEASURED:

    git diff --numstat 73aa7e3 worktree-agent-a2cba20f89cc11b74

reports 39 insertions and 0 deletions on `pre-registration.md`. A diff with no
deletion lines means every original line survives unchanged and in order; no
registered word moved. Stripping the quoted note back out leaves a file differing
from the original only by the two blank lines that set the note off.

---

### Finding 2 — the reserve-bank fix edits a record that was correct when it was written. **SERIOUS. MEASURED.**

Commit `2086036` deletes three `src/` prefixes from the reserve bank's authoring
notes, at five references. The new paths are right for the repository as it stands
today. MEASURED:

    git ls-tree -r --name-only main -- experiments/03-retained-independence/reserve-bank/

returns `scripts_shared.py`, `validate_items.py` and `verify_a_answers.py` sitting
directly in the reserve-bank folder, beside the notes that name them. There is no
`src/` folder there.

But the prefix was not an error. MEASURED:

    git ls-tree -r --name-only cc76ad8 | grep '03-retained'

At commit `cc76ad8` — "Stage 3 item bank authored + audited (pre-baseline): 60
items, rubric, validator", 2026-07-19 at 09:08 Pacific, the commit that wrote
these notes — the tree holds:

    experiments/03-retained-independence/authoring-notes.md
    experiments/03-retained-independence/src/scripts_shared.py
    experiments/03-retained-independence/src/validate_items.py
    experiments/03-retained-independence/src/verify_a_answers.py

The notes file sat at the experiment root and the three programmes sat in `src/`
beneath it. **`src/scripts_shared.py` was a correct relative path from the file
that wrote it.** Eighteen minutes later, the commit "Stage 3 bank fork
reconciled: batteries/ primary (machine-verified + audited), second bank to
reserve pool" (`2bb6971`, 09:26 Pacific) moved the notes *and* the three
programmes into `reserve-bank/`, which left three of the notes' pointers stale
and the rest of them correct.

So this is the same shape as the chance-floor item: a dated record that was
accurate when filed and went stale when the world moved under it. On that item the
same branch wrote a dated note and left the digit alone. Here it edited, with no
note, no date and no trace in the file that anything was touched on 2026-09-21.
It is the only one of the six fixes that changes an existing sentence, and the
only one a reader of the file cannot tell happened.

The triage knew this. Its own words at item B1: "Checking every commit in this
repository's history shows the three have only ever lived at two addresses …
The notes kept the old address." It then sorted the item into the pile marked
"real, fixable with no judgment" and prescribed a silent edit, while sorting three
structurally identical items into the pile marked "add a dated note, change no
existing sentence". The writing session followed the prescription. What neither
noticed is the sharper fact that the notes file moved too, which is what makes the
old address a *former truth* rather than a *mistake*, and which is the fact that
decides which pile the item belongs in.

**ARGUED, and I want to be fair about the scope.** The protocol's "never edited
after filing" rule is written for findings filed under
`experiments/<experiment>/reviews/`. These authoring notes are not a filed review,
not registered text, and not covered by that rule on its face. A reasonable person
could say a stale relative path in a working notes file is housekeeping. That is
why this is serious and not fatal. But the file opens by calling itself "the
original authoring record", it carries a dated audit trail, and the branch it sits
on is otherwise scrupulously annotate-only. Editing it silently is the one place
the six fixes are not consistent with each other.

**What would settle it**, and it is cheap: add one dated line to the notes saying
the three programmes moved to this folder in `2bb6971` on 2026-07-19 and that the
`src/` prefixes, correct when written, were updated on 2026-09-21. That keeps the
corrected paths and stops the record claiming it was always so.

---

### Finding 3 — "the battery record was rebuilt hours later" was nine and a half minutes. **WORTH-NOTING. MEASURED.**

The chance-floor note opens, in bold, with:

> The figure quoted above was right when this pass was filed. The battery record
> was rebuilt hours later and now reads 0.0909.

MEASURED:

    git log --all --diff-filter=A --format='%H %ad %s' --date=format-local:'%Y-%m-%d %H:%M %Z' \
      -- experiments/06-mvm-0a-constructed-self-index/red-team-pass-3.md

returns one commit and only one: `30cab76`, 2026-09-15 at **15:51:16** Pacific,
"Red-team pass 3 kills the certified grammar; the fix is free". The rebuild,
`e76d0d4`, is at **16:00:48** Pacific. Author and commit timestamps agree on both.
That is nine minutes and thirty-two seconds after filing, not hours.

The note's own body gets it right — "The battery was rebuilt the same afternoon" —
so the headline and the body disagree, and the headline is the part a reader meets
first. The error came in from the triage, which wrote "the record was regenerated
hours later" in its prescription for this fix; the writing session carried it
across without re-deriving it. It is worth-noting rather than serious because
nothing in the note's substance depends on the interval. It is worth noting at all
because this is a note whose entire purpose is to stop a reader trusting a stale
number, and the claim a reader is most likely to test is the one in bold.

There is a reading on which "hours later" counts from the record's first commit
(`7995382`, 09:58 Pacific, six hours earlier), but the sentence immediately before
it sets "when this pass was filed" as the clock, so that reading is strained.

**Everything else in that note holds.** MEASURED:

    git show 7995382:experiments/06-mvm-0a-constructed-self-index/batteries-a3/batteries_meta.json
    git show e76d0d4:experiments/06-mvm-0a-constructed-self-index/batteries-a3/batteries_meta.json
    git show main:experiments/06-mvm-0a-constructed-self-index/batteries-a3/batteries_meta.json

- `7995382`, "Gate 1 complete: the grammar passes both cue gates at $0; K1 does
  not fire", 2026-09-15 09:58 Pacific: `n_turns` 12, `T_state` chance floor
  **0.07692307692307693**. That is exactly 1/13, as the note says.
- `e76d0d4`, "Shortcut sweep finds a second fatal leak; three drafts map the real
  trade-off; revision proposal drafted", 2026-09-15 16:00 Pacific: `n_turns` 10,
  `T_state` **0.09090909090909091**. The turns did drop from twelve to ten.
- Today: **0.09090909090909091**, and the record still carries one floor per
  battery, which is what the note needs for its claim that the finding's substance
  survives the rebuild. It does.

The pass's own sentence quotes 0.0769 and cites that file, as the note says.

**And the note's quotations from the control-clause proposal are right where the
triage's were wrong.** MEASURED: the phrase "Nothing in this memo is rewritten"
is at line 19 and "It is left unedited" at line 92, both inside the later of the
two stacked annotations, speaking of the earlier one — which is exactly how the
note describes them. The triage had attributed "Nothing below is rewritten" (line
96, the *earlier* annotation) to the later one. The writing session caught the
mix-up and quoted correctly. Credit where it is due.

---

### Finding 4 — the only authority for annotating registered text is a ruling that is neither quoted nor filed. **WORTH-NOTING. ARGUED.**

The registered-text note closes:

> Recorded under John's ruling of 2026-09-21 that registered text carrying a
> measured value whose record is committed but not named is given a dated note
> supplying the pointer, and does not need a registered amendment, because the
> claim does not change. That ruling was given in the session that ordered this
> note and is not yet carried in a filed ruling under `docs/rulings/`.

The disclosure is honest, and I checked that the ruling is indeed unfiled.
MEASURED:

    git grep -ni 'dated note\|annotat' main -- docs/rulings/

returns eight hits, every one about annotating a *ruling*, none about annotating
registered text. Nothing in `docs/rulings/` settles the question.

What is missing is not the disclosure but the form. This programme has a house way
of recording a real ruling whose text has not landed yet, and it is two items
below in the same file the note cites elsewhere. Item 22 of the ruling on review
verification and staged spending records what John was asked, quotes him verbatim
— "Ok, can we implement all of these?" — states exactly what the ruling authorises,
and then says in bold what it does **not** authorise: "It does **not** accept any
particular wording". The note uses none of that. It gives no words of John's, and
it states the rule in a general form — any registered measured value, any
committed-but-unnamed record — which is broader than the single case in front of
it and is phrased throughout in the session's own language while carrying his
name.

That matters here more than it usually would, for two reasons. The workspace rule
is explicit that an agent must "never upgrade your own call to John's, however
sound the reasoning was". And the triage that raised this question named this
precise risk as the strongest case against annotating at all: "'registered text
may be annotated when the annotation does not change a claim' is a judgement each
writer would then make about their own text, which is the shape of every drift
this programme has recorded." Finding 1 above is that drift, arriving on the first
use.

**What would settle it**, and it costs a sentence: say what John was asked and
what he said, in his words if they are on hand; and add the disclaimer the
protocol already models — the ruling authorises the note, the wording is the
session's and is John's to overturn.

---

### Finding 5 — the note splits a registered list in two. **WORTH-NOTING. ARGUED.**

The note is placed between two items of the registered list of design elements —
after the curriculum bullet, before "**Held-out evaluation episodes**". A
blockquote between two list items ends the first list and starts a second, so a
registered list now renders as two lists with a note wedged between them. No
registered word changes and the diff is pure insertion, so this is presentation,
not content. But the note's whole claim is that the registration is left exactly
as it was, and the structure of a registered list is part of what it was. Placing
the note after the list, or at the end of the section, would carry the same
pointer without rearranging registered furniture.

---

## The trim — clean, and nothing lost. MEASURED.

All four claims reproduce.

**Claim: against the base, the whole branch is 140 insertions and zero
deletions.**

    git diff --numstat 2ad356a worktree-agent-ad4721f18c398ff46
    71  0   docs/preauthorised-spending-proposal-2026-09-21.md
    69  0   docs/successor-experiment-proposal-2026-09-21.md

140 insertions, 0 deletions. Confirmed. This is also the strongest available proof
of the third claim: a diff with no deletion lines means every original line of both
proposals survives byte-identical and in order. Counting deletion lines directly:

    git diff 2ad356a worktree-agent-ad4721f18c398ff46 | grep -c '^-[^-]'
    0

**Claim: against the long-note version, 109 deleted lines, all beginning with
`>`.**

    git diff --shortstat fcc2a14 e37566f
     2 files changed, 134 insertions(+), 109 deletions(-)

109 deletions, as claimed. And of those 109, the number that do not begin with
`>` is:

    git diff fcc2a14 e37566f | grep '^-' | grep -v '^---' | grep -vc '^->'
    0

Every deleted line was part of the long blockquote note. Nothing else was removed.

**Claim: each file with note and appendix stripped is byte-identical to the
commit before any note existed.** Established by the zero-deletion diff above. I
also tried the strip directly and record the result so nobody repeats the mistake:
a crude `grep -v '^>'` also eats blockquotes that were already in the proposals
(the framed research question in the successor proposal, the proposed cap and
envelope lines in the spending proposal) and produces a misleading difference. The
pure-insertion diff is the right test and it passes.

**Claim: exactly one word changed in the moved text, "below" to "above".**
Extracting the long note from `fcc2a14`, stripping its quote prefix, and diffing
against the appendix in `e37566f`, for both files:

    3c3
    < the proposal. Nothing in the proposal below is rewritten; it is left
    ---
    > the proposal. Nothing in the proposal above is rewritten; it is left

That is the only difference in the body, in both files, plus one trailing blank
line. The change is correct: the note moved from above the proposal to below it.

One thing the claim does not cover and a reader should know: the long note's
heading was **replaced**, not moved. In each file a first-level heading — "NOTE
ADDED AFTERWARDS — one of the things this proposal asks John to rule on is already
done", and "NOTE ADDED AFTERWARDS — the spend file this document calls stale has
since been corrected" — became "Note added afterwards: the detail" plus a new
italic line pointing back to the short note. That is new scaffolding rather than
moved text, so it does not contradict the claim, but "exactly one word changed"
is true of the body and not of the heading.

**Nothing was lost.** The dropped headlines' substance is carried by the short
notes, in both cases more sharply than before: "one of the things this proposal
asks John to rule on is already done" becomes "item 7 needs no ruling: it is
already satisfied", and "the spend file this document calls stale has since been
corrected" becomes "That correction has since landed, and no number here changes".

---

## Are the short notes adequate? Yes. ARGUED.

They were cut because sixty lines at the head of a document John is about to read
costs him attention before he reaches the proposal. Five lines still do the job in
both.

**The spending proposal's note is the one that had to work hardest, and it does.**
It names section 1.3 and, in bold, **item 7 of section 7**; says the file has been
corrected; and states the conclusion outright in bold — **"item 7 needs no ruling:
it is already satisfied"** — then protects the rest of the list with "Items 1 to 6
are untouched." A reader who reads only those five lines knows to skip item 7 and
to rule on the other six. That is the whole point of the note and it is
unmissable. Verified that it is true: item 7 asks for `data/project.toml` to be
corrected from $215.70 and $44.20; the file now reads `spent = 225.7` and
`spent = 44.3`.

**The successor proposal's note** names section 12.1 and the source list in
section 16, says the correction landed, and says in bold that **no number here
changes**, with the reason in one clause: section 12 was written against the
compute ledger rather than that file. It omits the December-roadmap correction,
which the appendix carries. That is the right omission — it is a secondary fact
about a different document and would cost a sixth line to no purpose.

Both notes end by naming the appendix, so the detail is one jump away.

---

## Every claim of fact in the notes, re-derived

All MEASURED. Commit titles are quoted from `git log`; times are Pacific, and
author and commit timestamps agree on every commit below.

| Claim in a note | Command | Result |
|---|---|---|
| `a6576d3`, "WITHDRAWN: Amendment A4 draft and its scoring script, parked, never registered", 2026-09-19 13:05 Pacific | `git log -1 a6576d3` | exact, to the title and the minute |
| It is the only commit on `withdrawn/amendment-a4-2026-09-19` | `git log --oneline main..withdrawn/amendment-a4-2026-09-19` | one commit |
| It exists in exactly one commit anywhere in the repository | `git branch -a --contains a6576d3` | that branch and its remote only |
| It holds the amendment draft and the scoring programme, at the paths given | `git show --name-only a6576d3` | `.../amendment-a4.md`, `.../src/separation_a4.py` |
| It branches from the main line at the merge commit `770c142`, two minutes earlier | `git log -1 --format='%P' a6576d3`; `git log -1 770c142` | parent is `770c142`, a merge commit, 13:03 Pacific — two minutes |
| `770c142` is the commit the ruling cites | `git show main:docs/control-clause-proposal-2026-09-19.md \| grep 770c142` | line 22, inside the refusal annotation |
| The commit message says no second version was to be written | `git log -1 --format='%B' a6576d3` | "John's instruction was explicit: no version two tonight" |
| John ruled against A4 on the strength of F1, F2, F6, F14 and F15 | control-clause proposal, line 22 | "fatal on F1, F2, F6, F14 and F15" |
| The earlier pass `a4-red-team-pass-1.md` is on the main line, landed by `416b289`, "Ruling of 2026-09-19 recorded, and red-team pass 1 on Amendment A4" | `git log -1 416b289`; `git show --name-only 416b289` | exact; the commit adds that file; 2026-09-19 12:35 Pacific |
| The A4 review's preamble names the draft as the text §5 "can be lifted into", names the scoring programme, and records both as uncommitted | `git show main:.../red-team-a4.md \| sed -n '1,60p'` | all three, verbatim |
| `4b4ec99`, "data: match the site's spend figures to the corrected compute ledger", 19:56:05 Pacific 2026-09-21 | `git log -1 4b4ec99` | exact, to the second |
| `176efad`, "Proposal: pre-authorised spending for the successor experiment", 19:51:27 Pacific | `git log -1 176efad` | exact, to the second |
| The correction landed about five minutes after the proposal | subtraction | 4 minutes 38 seconds — a fair rounding |
| `data/project.toml` now reads `spent = 225.7` and `spent = 44.3`, with both explanations rewritten to the compute ledger | `git show main:data/project.toml` | both figures, both notes rewritten |
| `5ad79a0`, "Land the ruled spend correction in the December roadmap", 20:16:39 Pacific | `git log -1 5ad79a0` | exact, to the second |
| The roadmap now reads about $225.70 spent and about $174.30 left | `git show main:docs/december-result-roadmap-2026-09-20.md` | "About **$225.70 is spent and about $174.30 is left**" |
| Item 16 of the ruling orders the stale spend figures brought into line with the ledger, and names this file | ruling file, lines 84–88 | exact, and it names both `data/project.toml` and the roadmap |
| Item 20 leaves the review's sentence standing and carries the correction as a separate task | ruling file, lines 204–221 | "carried as a small task to correct the record rather than chased tonight" |
| `STATUS.md` carries a dated block marked "ANNOTATION 2026-09-16" above a paragraph it leaves standing | `git grep -n ANNOTATION main -- STATUS.md` | line 673 |
| Section 12.1 and section 16 of the successor proposal say what the note quotes | `grep` against the base version | both, verbatim |
| Section 1.3 twice, and item 7 of section 7, say what the note quotes | `grep` against the base version | lines 119–129 and line 778, verbatim |

**One near-miss worth recording, because it could have gone wrong.** Two commits
on the main line share the title "Proposal: pre-authorised spending for the
successor experiment": `176efad` at 19:51:27 and `be99527` at 20:34:37. The note
cites the earlier one, and its whole timing argument depends on that being the
right one — if the annotated proposal were the 20:34 commit, the correction at
19:56 would have come *before* the proposal, not five minutes after, and the note
would be backwards. MEASURED:

    git log --format='%h %ad %s' 2ad356a -- docs/preauthorised-spending-proposal-2026-09-21.md

returns `176efad` and nothing else, and the file is byte-identical across
`176efad`, `be99527` and the branch base. The citation is correct and the timing
argument holds.

---

## Attribution — clean, and better than the triage it came from. MEASURED.

No note claims John ruled "annotate, never edit".

    git grep -n 'annotate, never edit' worktree-agent-a2cba20f89cc11b74
    git grep -n 'annotate, never edit' worktree-agent-ad4721f18c398ff46

Two hits, both on the trim branch, and both are explicit **denials**:

> No ruling of John's puts that practice into words. The nearest is item 20 of the
> ruling file named above … and it does not say "annotate, never edit". The
> practice here rests on precedent, not on any wording of his.

That is a direct correction of the triage, which had written that "John ruled on
2026-09-21 — item 20 … — that a filed review carrying a wrong measured claim is
**annotated with a dated note, not edited**". I read item 20 and it says no such
thing; it defers the correction to a later task. The writing session was right to
refuse it, and the annotation branch refused it too, describing the same practice
as "this repository's practice" rather than a ruling. Both sessions held the line.

The three remaining mentions of John on the annotation branch: two state that he
ruled against Amendment A4 on 2026-09-19 and that no second version was to be
written, both verified above against the ruling annotation and the withdrawal
commit message. The third is the unfiled ruling of finding 4.

---

## Plain language and whether the notes read as later additions

**Plain language: holds, with the exception that is finding 1.** The notes do real
work here — "the area under the cue detector's curve" for AUC, "95% range" for the
confidence interval, "the commit titled X (`abc1234`)" rather than a bare hash
anywhere. I checked every identifier in all six notes against the workspace rule
that no bare identifier may stand alone: every commit hash, ruling item and
finding label carries a phrase saying what it is. Finding 1 is the place where the
plain-language effort overreached — the rule asks for the plain word over the term
of art, but a registered label is not a term of art to be replaced, it is a name,
and the plain move is to quote the registration's own gloss.

**They read as later additions: yes, five of six, unmistakably.** Each of the five
notes is a blockquote, opens with a bold dated banner, says in its first two lines
that it was added afterwards by a later session and not by whoever wrote or ruled
on the document, and closes by saying what it did and did not change. Nobody could
mistake one for original text. The sixth is the reserve-bank edit, which carries
no marker at all, which is finding 2.

---

## Are the six fixes fit to merge?

**Five of six: yes.** Both branches merge into the main line without conflict —
`git merge-tree --write-tree main <branch>` returns a tree for each with no
conflict report, despite the annotation branch being based four weeks of commits
back. The trim is clean by every test its author claimed for it. The history work
across all six notes is accurate to the minute and, in three places, corrects the
triage.

**The registered-text note is not fit to merge as written.** Finding 1 puts a
false description of registered content into the registered file under a banner
promising the opposite. The fix is small — give the keys, or quote the
registration's own glosses — but it has to happen before this lands, because the
one permission the note was written under is that it changes nothing registered,
and as written it misdescribes something registered. Finding 4 should be fixed in
the same pass, since it is one sentence and it is the note's only authority.

**The reserve-bank edit should be turned into an edit plus a dated line** before
it lands, per finding 2, or sorted back into the annotate pile. Either is fine;
leaving it as a silent edit is the thing to avoid.

**Finding 3 is a one-word fix** — "hours later" to "nine minutes later", or simply
"the same afternoon", which is what the note's own body already says.

**Finding 5 is optional.** A different session fixes all of these; this one did
not touch them.
