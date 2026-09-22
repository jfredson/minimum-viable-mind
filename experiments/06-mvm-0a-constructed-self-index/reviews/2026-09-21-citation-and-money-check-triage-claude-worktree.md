# Triage of the two repository checkers — 2026-09-21

*A sorting pass by a Claude Code session in its own worktree, run against the
repository at the tip of the main line (the commit titled "Proposal:
pre-authorised spending for the successor experiment", `be99527`), with the two
checking programmes brought in from the branch their author left them on
(`worktree-agent-af64fa37d31cc1be5`, the commit `767fd0c`).*

*This session fixed nothing and edited nothing. It ran both programmes itself
rather than reading anyone's account of what they found, sorted every finding
into four piles, collapsed repeats, and established the facts behind the two
questions it is handing on for a ruling. A separate session writes the fixes; a
third checks those, which is this programme's pairing rule.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## What was run, and what came back

Both programmes were run from this worktree with the repository's own Python
interpreter, at the default scope (which skips mechanically assembled copies and
review packets — the right default, because a defect inside a copy is a defect in
the file it was copied from).

    .venv/bin/python scripts/check_citations.py
    .venv/bin/python scripts/check_single_source.py

**The pointer-and-figure checker** (`scripts/check_citations.py`, which asks
whether every file a document names exists and whether a figure given beside a
citation is really in the file cited) read 144 documents and reported 45 findings
it is confident about and 132 for a human to look at.

**The money checker** (`scripts/check_single_source.py`, which asks whether every
dollar figure traces back to the compute ledger) read 143 documents and reported
88 findings it is confident about, plus 234 figures that are right but point at
nothing and 13 figures that appear in four or more documents.

That is 499 lines of report. Sorted and with repeats collapsed, it is **21 items**,
of which **five** are things somebody should act on.

A note on counts: the brief for this pass quoted the programmes' author reporting
54 money findings, 44 of them one repeat. The main line moved between that run and
this one — two long proposals of 2026-09-21 landed on it — so the money checker now
reports 88 confident findings rather than 54, and the single largest repeat is 13
instances rather than 44. The numbers below are this session's own run, not the
author's.

---

## The four piles at a glance

| Pile | What it means | Items | Findings covered |
|---|---|---|---|
| **A** | False alarm | 16 | about 490 |
| **B** | Real, fixable with no judgment | 1 | 5 |
| **C** | Real, and an existing ruling already settles it | 3 | 10 |
| **D** | Real, and needs John | 3 | about 250 (almost all of one class) |

The two things the brief asked for above all are in piles C and D. Pile A is
listed as classes with counts, because a list of 490 lines is a list nobody reads.

---

## Pile B — real, mechanical, no judgment needed

### B1. Three script pointers in the reserve-bank notes say `src/` when the scripts sit in the same folder

**Where:** `experiments/03-retained-independence/reserve-bank/authoring-notes.md`,
the notes on how the reserve item bank was written — lines 30, 31, 32, 39 and 43.
Five references, three distinct files.

**What is wrong:** the notes name the three programmes that built and checked the
bank as `src/scripts_shared.py`, `src/validate_items.py` and
`src/verify_a_answers.py`. There is a `src/` folder in that experiment and it does
not contain any of the three. All three sit in the reserve-bank folder itself,
beside the notes that name them.

**Established, not assumed:** the three files exist at
`experiments/03-retained-independence/reserve-bank/scripts_shared.py`,
`.../validate_items.py` and `.../verify_a_answers.py`. Checking every commit in
this repository's history shows the three have only ever lived at two addresses —
inside `src/`, and inside the reserve bank — and they were moved to the reserve
bank by the commit titled "Stage 3 bank fork reconciled: batteries/ primary
(machine-verified + audited), second bank to reserve pool" (`2bb6971`). The notes
kept the old address.

**The exact fix:** delete the three `src/` prefixes, so each reference reads
`scripts_shared.py`, `validate_items.py` and `verify_a_answers.py` — a plain file
name beside the notes that name it, which is how the rest of that folder writes
them. Nothing else in the sentences changes.

**Nothing else reached this pile.** In particular, the one mechanical fix the
brief for this pass expected — that the ruling of 2026-09-21 on review
verification and staged spending points at a successor proposal which is not on
the main line — **is already fixed**. `docs/successor-experiment-proposal-2026-09-21.md`
is on the main line, landed by the commit titled "Successor proposal: the
rehearsal buys a rented slice, and the second release is bound to what it
measures" (`d8ceba9`). The pointer-and-figure checker does not report it missing,
and this session confirmed the file's presence in the main line's history rather
than only on disk.

---

## Pile C — real, and precedent already settles what to do

All three of these are handled the same way and for the same reason: a filed
review, a filed ruling annotation and a filed proposal are records of what
somebody said at a moment. John ruled on 2026-09-21 — item 20 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, on a count of
record keys that would not reproduce — that a filed review carrying a wrong
measured claim is **annotated with a dated note, not edited**, so the reviewer's
own wording survives. The repository already does this for proposals too: the
control-clause proposal of 2026-09-19 carries two dated rulings stacked in
blockquotes at its top, the second of which says of the first, in as many words,
"Nothing below is rewritten" and "It is left unedited."

So all three fixes are: **add a dated note, change no existing sentence.**

### C1. Red-team pass 3's chance floor of 0.0769 — the reviewer was right, and the file moved under them

**Where:** `experiments/06-mvm-0a-constructed-self-index/red-team-pass-3.md`,
line 742 — the pass of 2026-09-15 on Amendment A3 before its registration commit.
The sentence reads: "`batteries-a3/batteries_meta.json` records a single chance
floor of 0.0769 for the battery."

**What the checker said:** that 0.0769 is nowhere in the file cited. That is true
of the file as it stands today, which records a floor of 0.0909 for the
cross-turn state battery.

**What this session established, which changes the shape of it:** the review was
**correct when it was filed**. The record of frozen batteries as first committed —
by the commit titled "Gate 1 complete: the grammar passes both cue gates at $0; K1
does not fire" (`7995382`, 2026-09-15) — records the state battery's chance floor
as 0.07692307692307693, which is the 0.0769 the review quotes, and is one
thirteenth, which is exactly what the review says it is. The battery was rebuilt
later the same day by the commit titled "Shortcut sweep finds a second fatal leak;
three drafts map the real trade-off; revision proposal drafted" (`e76d0d4`), which
changed the number of turns per episode from twelve to ten and moved the floor to
0.0909. The reviewer did not misread anything; the file was regenerated under them.

**This matters beyond the number.** The finding's substance — that the recorded
floor is a single value for a battery that is a mixture of two question forms, and
is taken from the first frozen item only — survives the rebuild untouched: the
current record still carries one floor per battery. A future reader who opens the
cited file, fails to find 0.0769 and stops there would drop a live finding because
of a stale digit.

**The fix, by precedent:** a dated note appended to the pass, saying that the
figure was correct against the battery record as first committed, that the record
was regenerated hours later and now carries 0.0909, and that the finding's
substance is unaffected. The reviewer's sentence is not touched.

### C2. Amendment A4's draft and its scoring programme were withdrawn, and four pointers still name them

**Where, four references in two files:**

- `docs/control-clause-proposal-2026-09-19.md`, line 96 — inside the first of two
  stacked ruling annotations, which records John's ruling of 2026-09-19 and says
  the amendment was "Drafted at
  `experiments/06-mvm-0a-constructed-self-index/amendment-a4.md`".
- `experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`, line 3 — the
  independent review of 2026-09-19, naming the same amendment file.
- The same review, line 25, naming it again and also naming its scoring
  programme, `src/separation_a4.py`.

**Established:** both files existed and were deliberately removed, by the commit
titled "WITHDRAWN: Amendment A4 draft and its scoring script, parked, never
registered" (`a6576d3`). This is not a broken pointer in the ordinary sense — it is
a record of a thing that was withdrawn on purpose — but nothing in either document
says so, and the withdrawal is findable only by searching the repository's history.

**One mitigating fact:** the control-clause proposal's later annotation, stacked
above the earlier one, already says the earlier annotation is superseded and left
unedited. A careful reader is warned that the text below is historical. They are
not told the amendment was withdrawn.

**The fix, by precedent:** one dated note in each of the two files, saying the
amendment draft and its scoring programme were withdrawn and naming the commit
that withdrew them. No existing sentence changes.

### C3. Two live proposals say the project data file still carries the stale spend figure; it was corrected five minutes after one of them was written

**Where, five references in two files:**

- `docs/preauthorised-spending-proposal-2026-09-21.md`, line 119 —
  "`data/project.toml` still carries the stale 215.70 in its `[[spend.lines]]`
  block and should be corrected in the same session that lands any ruling on this
  proposal."
- The same proposal, line 131, resting an argument on that state.
- The same proposal, line 778, listing as a thing to do: "**Correct
  `data/project.toml`**, whose `[[spend.lines]]` block still carries $215.70 spent
  against the $400 envelope and $44.20 against the A3 stop."
- `docs/successor-experiment-proposal-2026-09-21.md`, line 844 — "The $215.70 came
  from the spend record in `data/project.toml`."
- The same proposal, line 1442 — naming that record as "stale … being corrected in
  a separate session".

**Established, with times:** the project data file was corrected by the commit
titled "data: match the site's spend figures to the corrected compute ledger"
(`4b4ec99`) at 19:56 Pacific on 2026-09-21. The pre-authorised spending proposal
was committed at 19:51 the same evening — five minutes earlier. The file today
records 225.7 spent against the $400 envelope and 44.3 against the Amendment A3
stop, which is what the compute ledger says. So a task one proposal asks John to
order is already done, and a second proposal describes a figure as being corrected
that has been corrected.

**Why this is not trivial:** both proposals are waiting on a ruling. John reading
either one tonight would be told to order something that has happened, and the
second proposal's reasoning about which figure is the live one reads as more
unsettled than it is.

**The fix, by precedent:** a dated note at the top of each proposal — the form the
control-clause proposal already uses — recording that the project data file was
corrected on 2026-09-21 and naming the commit. The bodies stay as written, because
what they said was true when they were written.

---

## Pile D — real, and needs a ruling

### D1. The cue-detector figure in the registered pre-registration: the value is right, the pointer is not

This is the item the brief named, and the facts turn out to be the opposite way
round from how it was framed. **The number is not wrong. It is not even
unsupported. It is uncited, and the checker attached it to the nearest citation,
which belongs to a different clause of the same sentence.**

**The sentence**, at `experiments/06-mvm-0a-constructed-self-index/pre-registration.md`,
line 203 and following, in registered text:

> **Registered values (adjudicated 2026-08-07): N = 4 agents, 8 turns per
> episode** — the configuration cue-detector gate run (i) actually certified
> (AUC 0.5008 [0.477, 0.524]), with the frozen batteries' chance floors
> (`batteries/batteries_meta.json`: T_sr/T_si 0.125, T_state 0.042, T_syntax
> 0.100) feeding the chance-corrected `d` [RT-14].

There are two claims and one pointer. The pointer sits inside the brackets that
belong to the second claim.

**What the checker reported:** three figures — an area under the detection curve of
0.5008 and the two ends of its uncertainty range, 0.477 and 0.524 — absent from the
one file the sentence names.

**What this session established, by opening the files:**

1. The record of frozen batteries the sentence names
   (`experiments/06-mvm-0a-constructed-self-index/batteries/batteries_meta.json`)
   contains **no detection figure of any kind**. It carries the seed, the counts,
   and the four chance floors: 0.125, 0.125, 0.041666…, 0.100. Those are exactly
   the four numbers the sentence attributes to it, to the rounding it uses. **The
   citation is correct for the clause it belongs to.**
2. The detection figure lives one directory up, in
   `experiments/06-mvm-0a-constructed-self-index/cue_detector_gate.json`, which is
   committed. Its first run — "(i) curriculum text", 4,000 episodes, seed
   20260804 — records a clean area under the curve of **0.5008** with a
   95% range of **[0.4773, 0.5242]**, inside the equivalence band of 0.45 to 0.55,
   and the gate marked PASS. The registered text's [0.477, 0.524] is that range
   rounded to three places.

**So the ruling question is much smaller than "correct a measured value in
registered text", and it is this:** the closure rule in
`docs/outside-review-protocol.md` says every sentence in registered text that says
verified, measured, calibrated or attacked cites the committed record by file
name. "Certified" is that family of word. The record exists and agrees; the
sentence does not name it. **May registered text be given a dated note adding the
missing pointer, or does adding a pointer to registered text require an
amendment?**

**Why precedent does not settle it.** The annotate-don't-edit ruling of 2026-09-21
(item 20) is about a **filed review**, whose whole value is that the reviewer's
wording is preserved. Registered text is preserved for a different reason — it is
binding — and the repository's way of changing it is a registered amendment, of
which there have been three. Nobody has yet had to add a pointer that changes no
claim. The question is whether "supply a missing citation" is a change to
registered text at all.

**What this session would recommend if asked**, offered as a recommendation and not
as a finding: an annotation, on the ground that the registered claim is unchanged
and an amendment for a citation would make amendments cheap, which is the one thing
they must not be. The strongest case the other way is that "registered text may be
annotated when the annotation does not change a claim" is a judgement each writer
would then make about their own text, which is the shape of every drift this
programme has recorded.

### D2. Figures got by subtraction — should they be banned, allowed, or allowed with their arithmetic shown?

This is the convention question the brief asked for a view on, and it is also, by a
wide margin, the largest single class the money checker reports.

**The size of it, measured in this run:**

- **13 instances** are the strict case: a headroom figure got by taking spend away
  from a cap. Ten of them are "$174.30", which is $400 less $225.70; two are
  "$55.70" and one "$55.73", which is the Amendment A3 stop of $100 less its spend.
  They appear in
  `docs/december-result-roadmap-2026-09-20.md` (lines 229 twice and 249),
  `docs/preauthorised-spending-proposal-2026-09-21.md` (lines 119, 131 twice and 315),
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (line 84),
  `docs/successor-experiment-proposal-2026-09-21.md` (lines 869 and 1092), and
  `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md` (line 532).
  Every one is arithmetically right and none is in the ledger.
- **234 further figures** are the same defect one step milder: right, in the ledger,
  and with no pointer at all. The checker files these as things to look at rather
  than as findings, and it is right to.
- One instance is **already ruled on and open**: finding RT-147 in
  `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md` says of "the
  programme at about $226 of its $400 ceiling" that "the figure is arithmetically
  right and is not in the ledger", accepts it as serious, and closes it by putting
  the programme's running total back on the ledger's two most recent rows — that is,
  **by making the derived figure a recorded one**, not by annotating the sentence
  that derived it.

**My view, which the brief asked for.** Requiring the subtraction to be shown —
"$174.30 left ($400 envelope less $225.70 spent, compute ledger)" — is better than
banning derived figures, and I would adopt it, with one change: it should be the
**second** choice, not the first. Where the derived figure is one a reader will want
again — the programme's headroom, most of all — the right answer is the one RT-147
already reached, which is to put the total in the ledger so there is nothing to
derive. The shown-subtraction form is for figures that are genuinely one-off.

Two things about the documents pushed me here. The first is that the form already
appears in the wild and reads well: the pre-authorised spending proposal's own
correction paragraph writes out "$400 minus $215.70 is $184.30" and then gives the
corrected chain, and it is the clearest money paragraph in the repository. The
second is that a ban is unenforceable in the documents as they stand — a proposal
pricing an experiment is arithmetic from end to end, and 46 of the 77 money findings
in this run are forecasts of that kind, not records at all.

**The strongest case against it**, which I think is genuinely strong: showing the
subtraction makes a stale figure *more* convincing, not less. "$174.30 left" is
plainly a number that might have moved. "$174.30 left ($400 envelope less $225.70
spent, compute ledger)" carries its own proof and reads as checked, so a reader who
meets it three weeks later is less likely to go and look — and the inputs go stale
exactly as fast as the output did. That is the failure this programme has already
had once: the $215.70 figure survived in two documents after the ledger had
corrected it, and it survived because it looked sound where it stood. A convention
that makes derived figures look sounder is a convention that makes that failure
more likely, not less. If the convention is adopted, it should carry a second
sentence requiring the date of the inputs, not only their source.

### D3. Two measured figures in a findings file that exist in no record anywhere

**Where:** `experiments/06-mvm-0a-constructed-self-index/fingerprint-gate-findings.md`,
line 3 — the findings of the third cue-detector gate run, 2026-08-08.

**The sentence:** "Numbers below are the pre-committed n = 4000 record
(`cue_detector_gate.json`); the n = 300 shakeout agreed (A 0.668 [0.590, 0.749],
B 0.885 [0.857, 0.912]) — the verdict never depended on n."

**What the checker reported:** six figures absent from the file cited. That much is
a false alarm of the ordinary kind — the citation belongs to the 4,000-episode
record, and the six figures belong to the clause after the semicolon.

**But the six figures are in no committed file at all.** This session searched the
repository for them; they appear in that sentence and nowhere else. The detection
record the sentence cites contains only the 4,000-episode runs. So a sentence that
says a second measurement "agreed" rests on numbers no reader can check.

**Why this needs a ruling and not a fix.** Under the closure rule as it now stands,
a measured claim with no record behind it is a fatal finding. But this file was
written on 2026-08-08, more than six weeks before the outside-review protocol
existed, and it is a findings file rather than registered text. Whether the closure
rule reaches backwards into findings files written before it — and if it does, what
the disposition is for a record that can no longer be produced because the run was a
shakeout nobody saved — has no precedent here. It is the smallest of the three and
could reasonably be declined with its reason recorded, which is itself a valid
outcome.

---

## Pile A — false alarms, by class

Sixteen classes, covering about 490 of the 499 reported findings. Each is given
with what it is and how many findings it accounts for, and none of them needs
anyone to do anything.

**From the pointer-and-figure checker, part (a): do the pointers land?**

| # | Class | Count |
|---|---|---|
| A1 | A file not written yet, named on purpose — the amendment that the control-clause proposal says its section 5 "can be lifted into", the restart note the roadmaps plan, the rehearsal folder and rehearsal findings the rehearsal method describes in advance, and the measuring programme that rehearsal will contain | 8 |
| A2 | Files deliberately deleted by the registered branch-draft procedure — the two amendment branch drafts pre-written before the 30-million-parameter verdict, one folded into the pre-registration and one deleted unused. The pre-registration's own sentence says so | 3 |
| A3 | Run outputs this repository does not commit, named as run outputs | 20 |
| A4 | Filing templates and patterns with a gap or a wildcard in them, which were never meant to land on a file: the protocol's own filing paths, `probe_target_diagnostic_a3_*.json`, `<checkpoint>` placeholders | 42 |
| A5 | References to other repositories in the workspace and to the public site's own web addresses, which the checker lists rather than resolves by design | 47 |
| A6 | Paths the ignore file keeps out of the repository, named as such | 50 |
| A7 | A bare file name matching several files — four pre-registrations, three red-team ledgers, two model files. The checker files these as disambiguation rather than as defects, and in every instance the document's subject settles which is meant. Worth a convention only if John wants one; it is not a defect today | 44 |

**From the pointer-and-figure checker, part (b): is a cited figure in the file?**

| # | Class | Count |
|---|---|---|
| A8 | A figure sitting beside a citation it was never sourced from — the checker reads one sentence at a time and cannot tell which clause a bracket belongs to. Instances: the 3.5-times billing overrun in the December-result roadmap, whose citation points at the ruling's halt-don't-trim item, not at the figure; "$184.30" in the pre-authorised spending proposal, in a sentence that performs the subtraction in front of the reader; the 6.7-cent checkpoint recovery in the staged-spending ruling; a section number ("12.3") in the successor proposal's source list; the parameter count and two balances in the compute ledger's own rows, whose citations belong to other clauses; and the six shakeout figures in the third gate run's findings (see D3 above, which is about something else) | 16 |
| A9 | A number written in the cited file with a size suffix — "102,000 steps" in red-team pass 3 against "≈ 102k steps" in the ledger row it cites. A stated blind spot of the checker | 1 |
| A10 | A figure worked out from the cited file rather than quoted from it — the null band "at ~2 items (0.067)" in the first experiment's threshold table, and the margin of "1.94 episodes in four thousand" in the fourth version of the A3 closure text, whose own sentence already says the margin is "computed in the review of that run and not stated in its findings file" | 3 |
| A11 | Superseded drafts of a text that has a later version — the third version of the A3 closure text, and figures inside the control-clause proposal's first, superseded ruling annotation | 4 |
| A12 | Rounded or hedged matches: 0.042 for a floor recorded as 0.041666…, "about $226" for a total the ledger states in parts, "about $281 to $300" sourced to a TimeAssembler decision and to the ledger at a named earlier commit | 27 |

**From the money checker**

| # | Class | Count |
|---|---|---|
| A13 | A forecast the sorter failed to catch — a price for a run nobody has made. Proposals and planning documents are arithmetic from end to end, and the checker's own note says the sorting is done on wording alone and will get some wrong in both directions. Largest single family: the "seven runs at about $130, about $219 remaining" planning figures that the two wave-3 option documents already flag as conflicting | 46 |
| A14 | A running balance in an append-only narrative, correct on its own date and superseded since — the August 2026 entries in `STATUS.md` and the cap adjudication memo | 5 |
| A15 | A spend review's own reconciliation arithmetic, in `docs/w37-spend-review-2026-09-16.md`, which exists precisely to derive figures from the console and the ledger | 10 |
| A16 | Money that is not this programme's compute spend at all — the embodiment experiment's estimated interface budget, and a model price comparison in the first experiment | 3 |
| A17 | A figure that is in the ledger and names no source. The checker files these as things to look at, and it is right: a sentence naming a cap it has just introduced does not need a footnote. These are the tail of the question in D2, not separate findings | 234 |
| A18 | The same figure in four or more documents — headed by the $400 envelope in 25 documents and the $100 Amendment A3 stop in 21. A cap is meant to be quoted widely | 13 |

---

## What this pass did not check, and what a clean run would not prove

Both programmes carry a list of what they are blind to, and those lists are the
honest part of them. Neither reads meaning: a figure being present in a cited file
is not that file supporting the claim. Neither can see a claim with no number in
it — "the gates were clean", "the attack sweep verified both ceilings" — which is
the exact shape of the defect the closure rule was written for. Neither can tell a
pointer at the right file but the wrong part of it.

This session's sorting inherits all of that. It also did not attempt to judge
whether any money figure is *correct*; the ledger is taken as the record, as the
money checker takes it.

**On tuning.** The programmes' author reports roughly 40% false alarms on the
pointer check, 70% on the figure check and 20% on money, and deliberately did not
tune them. This run bears that out and suggests where the cheapest gains are, for
whoever picks that up: teaching the figure check that a bracket belongs to its own
clause would remove most of class A8; excluding forecast wording more aggressively
would remove much of A13; and treating a wildcard or a placeholder as a pattern
rather than a pointer would remove all 42 of A4. None of that is this session's to
do.
