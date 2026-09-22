# Check of the repairs to the pointer notes — 2026-09-21

*A checking pass by a Claude Code session in its own worktree. This session did
not write any of the repairs and fixed nothing here. It exists because of the
first of the four rules John authorised on 2026-09-21 — item 22 of the ruling on
review verification and staged spending
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`): a session
that writes binding text is paired with a different session that checks it.*

*What was brought in: the repair branch `worktree-agent-a40613957351e5986` at its
tip commit `57eb09d` ("Pre-registration note: give the question John was shown
and the option he picked, word for word"), which sits on the four-commit branch
`worktree-agent-a7f48557f8b8238dd`, which sits on four earlier commits. Also
opened: the earlier checking pass this repair answers, commit `5a28a2b` on
`worktree-agent-aa90bea25ea7b1958` ("Check of the six pointer notes: two
findings, one fatal, the trim is clean"), the registered file itself, the two
committed data records the note rests on, and the repository's history back to
July.*

*Every finding is marked **MEASURED** (a command was run and its output is
reported) or **ARGUED** (reasoning from the documents, which a reader can
dispute).*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## Verdict in one paragraph

**Merge it.** Both findings of the earlier pass are closed, and closed properly
rather than papered over. The fatal one — a plain-English gloss that renamed two
registered battery keys and inverted one of them — is gone, replaced by the keys
as the registration itself writes them and by the registration's own words for
what each is; every quoted phrase is lifted verbatim from the registered battery
table, and nothing is renamed. The serious one — a silent edit to a record that
was correct when written — now carries a dated block that says what changed, when,
why, and that the original was right; every history claim in it re-derived to the
minute here. Both worth-noting items are closed too: the wrong interval in a bold
headline is now right, and the note no longer splits a registered list. The
registered text is untouched by the strongest test available: strip the annotation
out of the after file and it hashes identical to the file before any note existed.
Four small items are worth recording and none of them should hold the merge.

---

## Findings

| # | Item | Where | Severity | Kind |
|---|---|---|---|---|
| A | The battery-key gloss is fixed, and fixed by quotation | note on the pre-registration, `eeedb2f` | closed | MEASURED |
| B | The authority paragraph stays inside what John actually did | note on the pre-registration, `57eb09d` | closed | ARGUED |
| C | Registered text byte-identical; note clear of the list | note on the pre-registration | closed | MEASURED |
| D | The reserve-bank edit is now disclosed and dated | reserve-bank authoring notes, `eb2bb05` | closed | MEASURED |
| E | "Rebuilt hours later" is now "nine and a half minutes later" | note on red-team pass 3, `7b77266` | closed | MEASURED |
| F | "the two task batteries" is the note's grouping, not a registered phrase | note on the pre-registration | can follow | ARGUED |
| G | The banner still says the note "does one thing" | note on the pre-registration | can follow | ARGUED |
| H | "to the rounding the sentence uses" is followed by an unrounded figure | note on the pre-registration | can follow | ARGUED |
| I | The repair's own commit message says "this one paragraph"; it is two | commit message of `57eb09d` | can follow | MEASURED |

---

### A — the battery keys. The fatal finding is closed. **MEASURED.**

The earlier pass found the note calling the two chance floors of 0.125 "the
self-report and self-identification batteries" — wrong on both, inverted on one,
and both names already belonging to other things in the same registered file.

The note now reads:

> 0.125 for the two task batteries `T_sr` and `T_si`, 0.041666… for the
> cross-turn state control `T_state`, and 0.100 for the floor check `T_syntax`.
> Those are the four keys exactly as the registered sentence writes them, and
> this note does not rename them. What each one is, the registration itself says,
> in its battery table further down this file: `T_sr` is "self-relevant binding",
> `T_si` is "self-irrelevant integration" — "matched-difficulty integration over
> episode content with **no self-reference**" — `T_state` is the "cross-turn
> state, ownership-free" control that replaced `T_syntax`, and `T_syntax` is
> "kept as a floor check only".

**What the four keys actually are.** I opened the registration's own battery
table rather than taking the note's account of it. It is at lines 334–338 of the
file as the branch leaves it:

- `T_sr` — "self-relevant binding": multi-turn binding of the model's own prior
  outputs.
- `T_si` — "self-irrelevant integration": "matched-difficulty integration over
  episode content with **no self-reference**", binding a named *other* agent's
  commitment.
- `T_state` — "the real control, replacing T_syntax": "**cross-turn state,
  ownership-free**".
- `T_syntax` — "retained, demoted": "kept as a floor check only".

**Every quoted phrase is verbatim.** Each of the five quoted strings was matched
against the file as a fixed string, not a pattern:

    grep -c -F 'self-relevant binding'        → 4 hits, one of them the table row
    grep -c -F 'self-irrelevant integration'  → 2 hits, one of them the table row
    grep -c -F 'matched-difficulty integration over episode content with **no self-reference**'
                                              → 1 hit, the table row
    grep -c -F 'cross-turn state, ownership-free'
                                              → 1 hit, the table row
    grep -c -F 'kept as a floor check only'   → 1 hit, the table row

All five are lifted from the table, bold markers included where the table has
them. The note renames nothing: the four keys it prints are the four keys the
registered sentence prints (`T_sr/T_si 0.125, T_state 0.042, T_syntax 0.100`, at
line 209–210), and the plain phrase attached to each is either the registration's
own parenthetical or a quotation of the registration's own cell.

**The two wrong names are gone from the note**, and the things they actually name
are left alone. The registration retires a battery called `S (self-report)` and
keeps a "**forced-choice self-identification**" probe that it says is "explicitly
not a report channel and never scored as one"; the note no longer borrows either
name.

**The grep the brief asked for.** MEASURED:

    git grep -n 'T_sr.*self-report' main -- '*.md'
    → no output, exit status 1

Nowhere on the main line does a line put `T_sr` before the phrase "self-report".
The repair's commit message describes a search "for the two names together"
returning seven hits, all of them the retired-battery row. That is the earlier
pass's search, which had an alternation in it, and it does reproduce exactly:

    git grep -n 'T_sr.*self-report\|self-report.*T_sr' main -- '*.md'
    → 7 hits, every one the same retired-battery table row, in the
      pre-registration and in six copies of it inside review bundles

So the repair's reading of those hits is right, and the narrower search the brief
asked for makes the same point more strongly: there is no line anywhere in the
repository where `T_sr` is glossed as self-report. The seven hits are all the row
that *separates* the retired `S (self-report)` battery from `T_sr` — it says the
forced-choice substitute "draws on the same information as T_sr, so it cannot
dissociate", which is a statement that they are different things.

**The rest of that paragraph re-checked from the records, not from the note.**
MEASURED. `experiments/06-mvm-0a-constructed-self-index/batteries/batteries_meta.json`
holds a seed, four battery counts, four chance floors — `T_sr` 0.125, `T_si`
0.125, `T_state` 0.041666666666666664, `T_syntax` 0.1 — and a one-line note. It
holds no detection figure of any kind, as the annotation says.
`experiments/06-mvm-0a-constructed-self-index/cue_detector_gate.json` holds, for
its first run, `"(i) curriculum text"`, 4,000 episodes, seed 20260804, a clean
area under the curve of 0.5008 with a 95% range of [0.4773, 0.5242], an
equivalence band of [0.45, 0.55], a planted-leak control at 0.8627 and `GATE`
`PASS`. Every figure the note quotes is exact, and [0.477, 0.524] is that range
rounded to three places.

**Verdict: closed.** The repair does the thing the earlier pass prescribed — stop
translating, quote the registration — and it does it without adding a word of its
own about what the batteries are.

---

### B — the authority paragraph. **ARGUED, and this is the part I looked at hardest.**

This paragraph is the one that could do real damage, because it puts words on a
page and says John was shown them. The question is whether it claims more than
happened. He did not speak or write a sentence; he was offered a question with
three options and picked one, and every word of all four was the asking session's.

**Is the paragraph honest about that?** Yes, and unusually so. It opens:

> On 2026-09-21, in the session that ordered this note, John did not say or write
> a sentence that could be quoted. He was shown a question with three options
> under it, each option carrying the consequence of choosing it, and he selected
> one. The wording of the question and of all three options was that session's,
> not his; what is his is the selection.

It then says the house form — quoting the words John used, as item 22 of the
ruling on review verification and staged spending does — "cannot take that form,
because there were no words of his to quote", and gives the question and the
chosen option as blockquotes inside the note's blockquote, labelled "word for word
as it was put to him". Nothing is attributed to John except the act of choosing.

**Does it claim he stated a condition?** No, and this is the specific thing the
earlier version got wrong. The previous text said "He chose the dated note, on the
condition he stated — that the claim does not change", which quietly turned a
line of the session's own option description into a condition John had
articulated. MEASURED: searching the file for "on the condition", "he stated",
"John ruled" and "John said" returns nothing. The phrase is gone. What remains in
its place is the option's own text — "Claim unchanged, nothing rewritten" — sitting
inside a quotation clearly marked as the asking session's wording. That is the
right repair, and I agree with the writing session's stated reason for making it.

**Does it still say plainly that not one word is John's drafting?** Yes, and the
bolded limits sentence is carried over unchanged. MEASURED: in the diff of
`57eb09d` these lines appear as context, not as insertions or deletions, which
means they are byte-identical to the previous version:

> **What he authorised is the act — a dated note naming a committed record, where
> no registered claim changes. It does not authorise restating a registered label
> in other words, describing registered content, or annotating registered text
> for any other purpose, and it does not settle any particular wording.** Not one
> word of this note is John's drafting; the wording is this session's, and his to
> overturn.

Nothing was softened. The clause "restating a registered label in other words" is
notable: the permission now names, in bold, the exact failure the earlier pass
caught, and rules it out.

**What was dropped, and whether it should have been.** Two limits went: that his
exact words are carried nowhere, and that the note reports rather than quotes.
Both were statements about a gap that the repair fills, so dropping them is right;
leaving them would make the note contradict itself. The limit that still bites
stays, and stays in the same plain form: the ruling is not yet carried in any
filed ruling under `docs/rulings/`, what is filed there is about annotating
rulings rather than registered text, and "until it is filed, this paragraph is the
whole record of it". MEASURED: the earlier pass's search of the filed rulings for
this subject returned eight hits, all about annotating a *ruling*. I re-ran the
question from the other side and the option text appears nowhere in the repository
except in this note itself:

    git grep -n -F 'Dated note on the registered text' -- '*.md'
    → one hit, the pre-registration note

So a reader cannot check the quotation against anything. The note does not pretend
otherwise — it says this paragraph is the whole record — and I do not think more
is owed here, but it is worth a reader knowing.

**The two deliberate roughnesses.** I agree with keeping both.

- The quoted option says "this program", where the repository everywhere else
  writes "programme". The note's own prose, four lines above, writes "programme".
  Leaving the spelling as it was shown is right: the paragraph exists to let a
  reader see exactly what was in front of John, and a quotation silently
  regularised to house spelling is a quotation the reader can no longer trust. The
  spelling difference is also the visible sign that the quote is foreign text, not
  the note's own voice, which is a small bonus.
- The straight apostrophes in "'annotation that changes no claim'" are likewise
  as shown. I note in passing that the note's own prose uses straight apostrophes
  too, so this one is less distinctive than the writing session seems to have
  thought — but keeping it costs nothing and the principle is the right one.

**The one thing I want on the record.** Quoting the two options John turned down
is a genuine improvement, not padding: the strictest option ("Registered
amendment") and the do-nothing option ("Leave it, record the defect") together
show that the choice was not between annotating and nothing, which is the reading
a bare "he approved it" would leave. And keeping the risk sentence unedited —
the one that says a permission turning on "the claim does not change" becomes a
judgement each writer makes about their own text — means the note carries the
case against itself, from the page John saw. That is the shape this programme
should want.

**Verdict: closed. The note stays inside the permission it was written under.**

---

### C — registered text byte-identical, and the note clear of the list. **MEASURED.**

Every claim reproduces, and the strongest one reproduces exactly.

**Claim: 46 insertions and 18 deletions.**

    git diff --shortstat 7b77266 57eb09d
     1 file changed, 46 insertions(+), 18 deletions(-)

**Claim: all 18 deletions inside the note's own paragraph.**

    git diff 7b77266 57eb09d -- .../pre-registration.md | grep -c '^-[^-]'      → 18
    git diff 7b77266 57eb09d -- .../pre-registration.md | grep '^-[^-]' \
      | grep -vc '^-> '                                                          → 0
    git diff 7b77266 57eb09d -- .../pre-registration.md | grep '^@@'
      @@ -258,30 +258,58 @@

Eighteen deleted lines, every one of them a quoted line of the note, in a single
hunk covering thirty lines of the authority passage. Nothing outside that passage
was reachable by this diff at all.

**Claim: strip the annotation from before and after and the content is
identical.** I stripped the contiguous annotation blockquote — the run of lines
beginning `> **ANNOTATION, 2026-09-21` and continuing while lines start with `>` —
plus the one blank line inserted with it, from three versions, and hashed the
result:

    version                                            sha256 of stripped file
    73aa7e3 (before any note existed)                  ff0a8455…069c14
    7b77266 (the note as it stood before this repair)  ff0a8455…069c14
    57eb09d (the note as it stands now)                ff0a8455…069c14

All three identical, and `diff` reports no differences. This is stronger than the
claim made: the after file with the note removed is byte-identical not just to the
before file but to the registered file as it stood before any note was written at
all. The annotation block is 94 lines now against 66 before; the file grows from
745 lines to 840; not one registered character moves.

**Confirming it from the other direction:**

    git diff --numstat 73aa7e3 57eb09d -- .../pre-registration.md
    95      0

Ninety-five insertions, zero deletions, across the whole branch. A diff with no
deletion lines means every original line survives unchanged and in order.

**Claim: the note sits clear of the registered list.** MEASURED. The original
note, commit `285903e`, inserted itself at the hunk `@@ -216,6 +216,45 @@`, ahead
of the bullet "**Held-out evaluation episodes**" — between two items of the
registered list of design elements. Today the curriculum bullet ends at line 218,
the held-out-episodes bullet runs at 219–220, and the note begins at line 222,
after the list and before the next heading. The two bullets it used to separate
are adjacent again. The note says so itself, in its banner: "It is placed after
the list of design elements rather than between two of its items, so that the
registered list is not broken in two."

**Verdict: closed.**

---

### D — the reserve-bank file. **MEASURED, with an ARGUED judgement at the end.**

An earlier pass, commit `2086036` ("Reserve-bank notes: point the three programmes
at the folder they live in"), deleted five `src/` prefixes from three programme
names in `experiments/03-retained-independence/reserve-bank/authoring-notes.md`
with no note and no date. The paths it produced are right; the paths it deleted
were also right when they were written, because the notes file had moved too.

**The history claims, re-derived here.** MEASURED.

| Claim in the new block | Command | Result |
|---|---|---|
| The notes were written by the commit "Stage 3 item bank authored + audited (pre-baseline): 60 items, rubric, validator" (`cc76ad8`), 2026-07-19 at 09:08 Pacific | `git log -1 cc76ad8` | title exact; 09:08:38 Pacific; author and commit times agree |
| At that commit the notes file sat at the experiment's top folder and the three programmes sat in `src/` beneath it | `git ls-tree -r --name-only cc76ad8 -- experiments/03-retained-independence/` | `.../authoring-notes.md`, and `.../src/scripts_shared.py`, `.../src/validate_items.py`, `.../src/verify_a_answers.py` |
| Eighteen minutes later the commit "Stage 3 bank fork reconciled: batteries/ primary (machine-verified + audited), second bank to reserve pool" (`2bb6971`), 09:26 Pacific, moved the notes **and** the three programmes into `reserve-bank/` | `git log -1 2bb6971`; `git ls-tree -r --name-only 2bb6971 -- …` | title exact; 09:26:49 Pacific, which is 18 minutes 11 seconds later; all four files in `reserve-bank/` at that commit |
| All four sit side by side today | `git ls-tree -r --name-only HEAD -- …/reserve-bank/` | notes plus the three programmes, no `src/` folder there |
| Five `src/` prefixes were deleted, at three programme names | `git show 2086036 -- …` | five replaced lines: three in the file list, two in the audit steps |
| The pointer to `../src/batteries/` names a different folder and is still correct | `git ls-tree -r --name-only HEAD -- …/src/batteries/` | four files there, including the two item banks and the rubric |
| No other word of the record was touched | `git diff --numstat c04fddd eb2bb05` | 18 insertions, 0 deletions on this file |

Every claim holds, to the minute. The full history of the file is four commits —
written, moved, paths edited, note added — so "the only change made to this file
since it was filed" is fair, the move aside, and the move is what the block is
about.

**Keeping the corrected paths with a note, or restoring them with a note?** The
repair kept them, and I think that is right. ARGUED, and the reason the writing
session gives is the correct one and worth repeating: a file path is not a claim
about the world at the time it was written, it is how a reader reaches a
programme, and a pointer that no longer reaches it has failed at its only job. The
chance floor on red-team pass 3 is a different kind of thing — a number a reviewer
measured, where the reviewer's own wording is the value of the filed review — so
that one had to stand and be annotated around. Restoring `src/` here would buy
historical fidelity in a working notes file at the cost of three pointers that go
nowhere, and would need the same dated block anyway to explain why. The earlier
pass recommended exactly this resolution, in those words: "That keeps the
corrected paths and stops the record claiming it was always so." The repair did
what the check asked.

**Does it read as a later addition?** Yes. The block opens "*PATHS UPDATED
(2026-09-21, by a later session — the only change made to this file since it was
filed, and it changes no claim)*" and states in bold "**Those were correct when
this file was written.**" It is an italic block matching the file's existing
status block rather than the blockquote form the other five notes use, which is a
deliberate match to the house style of this particular file and reads fine. One
cosmetic point: it sits between two blocks dated 2026-07-19, so the file now runs
July, September, July. Placing it after both would read slightly better. Not worth
a commit on its own.

**Verdict: closed.**

---

### E — the headline on red-team pass 3. **MEASURED.**

The bold headline said the battery record was "rebuilt hours later" where the body
said "the same afternoon". It now reads:

> **ANNOTATION, 2026-09-21. The figure quoted above was right when this pass was
> filed. The battery record was rebuilt nine and a half minutes later and now
> reads 0.0909. Nothing in the finding is edited, and its substance is
> untouched.**

MEASURED. The pass was filed by the commit "Red-team pass 3 kills the certified
grammar; the fix is free" (`30cab76`), the only commit that adds the file, at
15:51:16 Pacific on 2026-09-15. The rebuild, the commit "Shortcut sweep finds a
second fatal leak; three drafts map the real trade-off; revision proposal drafted"
(`e76d0d4`), is at 16:00:48 Pacific. That is nine minutes and thirty-two seconds —
"nine and a half minutes" is right, and it is the only remaining use of an
interval in the note. The body's "the same afternoon" now agrees with it. The
change was two insertions and one deletion, entirely inside the note.

**Verdict: closed.**

---

### F — "the two task batteries" is the note's own grouping. **CAN FOLLOW. ARGUED.**

The note writes "0.125 for the two task batteries `T_sr` and `T_si`". The
registration heads the table "Task batteries" and puts all four keys under it, and
in one place it calls `T_si` a control: "Control: T_si is instantiated as binding
a *named other agent's* commitment". So "the two task batteries" is a grouping the
note supplies, not a phrase the registration uses of those two keys.

It does no harm. The note gives the registration's own words for `T_si` in the
very next sentence, including "no self-reference", so no reader can come away
thinking `T_si` involves the model's own commitments — which is the failure the
fatal finding was about. This is a different and much smaller thing: a category
word rather than a substituted name. Dropping the word "task" would remove it
entirely. Worth doing whenever this file is next open; not worth another round.

---

### G — the banner still says the note "does one thing". **CAN FOLLOW. ARGUED.**

The banner reads: "This note does one thing: it names the committed record that
holds the detection figure that bullet quotes, which the bullet does not name."
The note now also quotes the registration's glosses for four keys and records at
length where its permission comes from. Both are in service of the one thing, and
both are defensible — quoting the registration inside the registration is the
narrowest possible form of saying what a key is — but "does one thing" is now a
little smaller than the note. A phrase like "does one thing, and says under what
permission" would cover it. Cosmetic.

---

### H — "to the rounding the sentence uses", followed by an unrounded figure. **CAN FOLLOW. ARGUED.**

The note says the record holds the four chance floors "to the rounding the
sentence uses", then lists "0.041666… for the cross-turn state control
`T_state`". The registered sentence renders that floor 0.042; 0.041666… is the
record's raw value. Read one way — the file's floors agree with the sentence once
rounded, and here they are — the sentence is fine, and the ellipsis signals a
truncated exact value. Read the other way it contradicts itself in the same
breath. This predates the repair, was passed by the earlier check, and changes
nothing about whether the pointer is right. Worth half a sentence one day.

---

### I — "this one paragraph". **CAN FOLLOW. MEASURED.**

The commit message of `57eb09d` says "the diff's eighteen deletions all fall
inside this one paragraph". They fall inside one hunk and one passage, but two
paragraphs: nine lines from the paragraph beginning "**The authority for this
note…**" and nine from the tail of the paragraph beginning "**What he authorised
is the act…**". The substance of the claim is true and I verified it above — all
eighteen are quoted lines of the note, none touch registered text or any other
part of the annotation. This is a commit message, not the record itself, and it
cannot be fixed without rewriting history. Recorded for accuracy only.

---

## Plain language, and whether every note reads as a later addition

**Plain language: holds.** MEASURED on identifiers — I scanned the whole
annotation on the pre-registration for bare identifiers and the only bare-looking
string is "seed 20260804", which carries the word "seed" and is a value inside the
record being described. Every commit identifier in the reserve-bank block and the
pass-3 note carries its commit title. The ruling is cited as "item 22 of the
ruling on review verification and staged spending" with its path, never as a bare
item number. The technical terms are handled the way the rule asks: "the area
under the cue detector's curve" before any short form, "95% range" for the
confidence interval, "programmes" for scripts. The repair to the battery keys is
itself a plain-language decision made correctly — a registered label is a name,
not a term of art, and the plain move on a name is to quote the definition rather
than invent a friendlier word. That distinction is now stated in the note.

**They read as later additions: yes, all six, unmistakably.** The five blockquote
notes each open with a bold dated banner, say in their first lines that a later
session added them and that nothing is edited, and close by saying what they did
and did not change. The sixth, the reserve-bank block, was the one that carried no
marker at all; it now opens "*PATHS UPDATED (2026-09-21, by a later session…)*"
and is the first thing after the status block a reader meets. The gap the earlier
pass found is closed.

---

## Does the note stay inside the permission it was written under?

Yes. ARGUED, and this is the question the whole repair turns on.

The permission is: a dated note naming a committed record, where no registered
claim changes. Three tests.

1. **Does any registered claim change?** No, and this is settled by measurement
   rather than argument. Strip the annotation and the file is byte-identical to
   the registered file before any note existed. Ninety-five insertions, zero
   deletions. The note is additive in the strictest sense available.
2. **Does the note describe registered content in its own words?** No longer. It
   gives the keys as the registration writes them and quotes the registration's
   own cells for what each is. Where it must group them, it uses the
   registration's own roles — control, floor check. The one place it adds a word
   of its own is finding F above, and that word is a category, not a name.
3. **Is the authority honestly stated, and are its limits stated?** Yes. The
   paragraph says exactly what John did — selected one of three options whose
   wording was not his — quotes what he was shown including the argument against
   it, states in bold what the permission does not cover, says in terms that not
   one word of the note is his drafting, and records that the ruling is still
   unfiled so this paragraph is the whole record of it.

The note is now a better record of its own authority than the practice it rests
on. That is the right direction.

---

## Merge

    git merge-tree --write-tree main worktree-agent-a40613957351e5986
    ba6186b7179e417eab192bd483eb66227500d13f

A tree, no conflict report. The branch merges into the main line cleanly. Across
the whole branch against the pre-note base `73aa7e3`, every file is pure insertion
except the reserve-bank authoring notes, which is 23 insertions and 5 deletions —
the five corrected paths and the dated block that now discloses them. That is the
only existing sentence changed anywhere on the branch, and it is the one the
disclosure is about.

**Must fix before merge: nothing.**

**Can follow afterwards:** findings F, G and H, all in the note on the
pre-registration and all one-line edits worth folding into whatever next opens
that file; finding I is a commit message and is recorded rather than fixed; and
the cosmetic placement point in finding D.

**Merge: yes.**
