# Closure checks on the three fatal findings of the Gate A pass on section 2 (RT-283, RT-284, RT-289), against version 3

*Filed 2026-10-17 (Saturday, Pacific) by a Claude Code session that wrote
none of: version 1 or version 2 of the refounding proposal, the Gate A pass
of 2026-10-09 (tier 1, tier 2 or the packet), the six rulings of 2026-10-12,
or version 3 of section 2. It read no session's chat. Filed here, beside the
Gate A pass it closes, because section 2 belongs to the spec and the Gate A
files on it already sit in `docs/reviews/`. $0: no model called, nothing
rented, nothing spent. Everything was read from the main line at commit
`a99e8e9`; the script and its output are in
`2026-10-17-section-2-v3-closure-checks-scripts/`.*

**Verdict: two of the three fatal findings close by the letter of their
closure checks (RT-289 and, with one reading given below, RT-284). RT-283's
check does not pass by the letter: one of its two forbidden phrases appears
once, in a different sentence from the one the finding was about. Whether
that sentence reintroduces the finding's defect is for the ledger session to
put to John; it is stated plainly below and not decided here.**

## What this is, and what it is not

The protocol's closure rule (`docs/outside-review-protocol.md`, "The closure
rule") says every fatal finding at Gate A needs a closure line in the ledger
naming the commit that lands the fix and a MEASURED check by a session other
than the one that wrote the fix. The fix here is version 3 of section 2
(`docs/rulings/2026-10-12-two-sided-question-section-2-v3.md`, merged as pull
request 170, merge commit `03df5e3`). The closure checks for RT-283 and
RT-284 are the ones the tier 1 reviewer wrote under those findings
(`2026-10-09-two-sided-question-gate-a-tier1-claude-code.md`); the check for
RT-289 is the one version 3 names under that finding in its change log. This
file runs each of them and reports the output. It does not write ledger
rows, does not edit the spec, does not edit version 3, and rules on nothing.

Every finding below is labelled MEASURED (a command was run and its output is
given) or ARGUED (reasoning a reader can dispute).

## What was opened, and what was not

Opened: version 3 of section 2 (the file above); the spec as it stands
(`spec/minimum-viable-mind-proposal-v0.1.md`, 153 lines); the tier 1 note's
text under RT-283, RT-284 and RT-289 and its check C4 script
(`2026-10-09-two-sided-question-gate-a-scripts/gate_a_checks.py`, lines 106
to 135, whose assembly and four search patterns are reused unchanged); the
2026-10-07 rulings file, to confirm ruling 10 is there; the six rulings of
2026-10-12 as posted on pull request 165; the protocol's closure and pairing
rules. Not opened: the battery draft, the Gemini and GPT replies, the tier 2
packet, the founding wager, the book's summary.

## How the spec was assembled

Version 3 gives three pieces of text to insert and nothing else: the section
"The Question This Project Measures: Two Sides" (version 3's lines 75 to 294,
2,454 words), to go after Scope and before "What This Proposal Is"; a
sentence (214 words) appended after The Floor's "A self-model that can be
lopped off while the computation runs was a description all along"; and a
paragraph (223 words) after the fourth condition of "What Would Count Against
It". The script finds each anchor exactly once in the spec (lines 21, 41 and
141) and builds the spec as it would read after the commit: 377 lines, 224
inserted, one line changed in place (the Floor anchor line, by appending the
sentence). SHA-256 of the assembled text
`3d0baaca5fbf1af08d86652e455ca4e0462c98f7fb424fde09292623256df119`. MEASURED.

## RT-289 (fatal by ruling 6). "Degree measured" and "placed on the axes at a degree". CLOSES.

Version 3's closure check: on the spec text, `grep -c "degree measured"` and
`grep -c "at a degree"` return 0; `grep -c "non-zero"` returns 1, and the hit
is the sentence saying what Scope's "non-zero" is and is not.

```
grep -c "degree measured"  -> section 2 text: 0; whole assembled spec: 0
grep -c "at a degree"      -> section 2 text: 0; whole assembled spec: 0
grep -c "non-zero"         -> section 2 text (the three inserts): 1
   | reach is unchanged, and its "non-zero on the gradient, never a verdict" is
'non-zero' in the spec as it stands (John's unchanged text): 3 line(s): [10, 14, 149]
'non-zero' in the whole assembled spec: 4 line(s)
'degree' in the section text at all: 1 hit(s)
   | The honest sentence changes with the instrument: named construction
     contrasts, row by row, with their margins and uncertainty; the route
     named; no validated degree on any axis yet; never a verdict.
```

MEASURED. The output matches what the closure claims. The one "non-zero" in
the inserted text is the supersession paragraph's sentence about Scope's
phrase ("its 'non-zero on the gradient, never a verdict' is its statement
about that bracketed question, not an output rule for the battery, whose
readings may be zero"), and the one "degree" left is the sentence that says
there is no validated degree. The three other "non-zero" lines in the
assembled spec are John's unchanged text (Scope, lines 10 and 14; The
Limits, line 149), which version 3 says it does not edit, so the check is
read on the inserted text, as version 3 words it ("on the spec text" of the
section). The automatic "non-zero" that A2 asked to go is gone and zero is
stated as a permitted reading.

## RT-284 (fatal by ruling 6). Section 2 contradicts unchanged sentences. CLOSES, with the reading below.

The tier 1 closure check: "the same command on the revised spec" (check C4,
the four paragraph-by-paragraph searches), with every hit in the unchanged
groups either carrying a dated note or reworded; under ruling 2 of
2026-10-12 the earlier sentences get no notes and section 2 instead names
what it supersedes, so version 3 states the expected result as: every hit in
the "unchanged" groups is named in the supersession paragraph.

The four searches, with the same patterns as the tier 1 script, return these
hits in John's unchanged text (the section each sits in is given):

| Group | Unchanged sentence (spec line, section) | How the supersession paragraph covers it |
|---|---|---|
| what "minimum viable" names | line 17, Scope: "'Minimum viable' names the smallest system that clears the *measurable* floor" | quoted verbatim, as Scope's last sentence, and re-read ("'minimum viable' means the outcome of the registered search above") |
| what "minimum viable" names | line 45, The Floor: "This gives the minimum viable conscious machine a two-part definition. The **floor system**…" | named by section and by its term: "The Floor's account of the floor … stand as the definition of the floor; its 'floor system' … remains the definition of the floor system" |
| removal test as instrument or criterion | line 10, Scope: "subject to a removal test" | quoted verbatim, as Scope's first sentence |
| removal test as instrument or criterion | line 39, The Floor: "settled by removal" | named by section and substance: "the removal test as the line between a centre and a description of one, stand as the definition of the floor" |
| removal test as instrument or criterion | line 45, The Floor: "survives the removal test" | quoted verbatim |
| removal test as instrument or criterion | line 68, The Build: "The pass-fail criterion is the removal test made mechanical" | quoted verbatim and re-read ("was the criterion of experiments 1 to 4 and of the successor experiment's registration") |
| removal test as instrument or criterion | line 105, Grokkable by a Layperson: "Use the removal test as the intuition for 'someone home'" | named by section and phrase: "The removal test stays in 'Grokkable by a Layperson' as the intuition for 'someone home'" |
| floor or binding measured | line 10, Scope: "targets the **minimum measurable structural correlate**" | quoted verbatim |
| floor or binding measured | line 87, Measuring It: "The measurement that speaks to an inside is a different one" and "Interpretability is the route" | named by section: "Measuring It is unchanged: its four instruments stand, and its corroborated report is the second of the two ways a reading discriminates" |

The script's own strict test (is the matched phrase a substring of the
supersession paragraph?) flagged six of these as not named; on reading, that
is the test's crudeness, not the text's: Scope's last sentence is quoted but
carries `*measurable*` in the spec, the Grokkable sentence is named with the
phrase inverted, and the Floor and Measuring It sentences are named by
section rather than quoted. MEASURED for the hits and their sections; ARGUED
for the reading that "named by section" meets "named in the supersession
paragraph". The third group ("the removal test called a definition, not an
instrument") now returns no hit at all: version 3's Floor sentence says the
project "treats the test as its definition of the floor and not as an
instrument for it", which the tier 1 pattern does not match, so the
competing statement the tier 1 pass found twice is gone in that form. The
paragraph's closing rule is present: "Where any sentence of those sections
and this one disagree about what the project measures or how a run passes,
this section binds."

What this does and does not show. The check shows that each unchanged
sentence the tier 1 pass found in competition with section 2 is now
addressed by name or by section in the supersession paragraph, with a
precedence rule, which is what ruling 2 chose over dated notes. It does not
show that a reader of Scope alone will know to look for the supersession
paragraph; Gemini's point under RT-284 (two pass-fail rules binding at once)
is answered by the precedence rule, and GPT's A10 by the naming. Whether that
is enough is the author's and John's call and is already ruled (ruling 2).

## RT-283 (fatal). The observer loss condition "no better than chance". DOES NOT CLOSE BY THE LETTER.

The tier 1 closure check: on the revised text, `grep -c "no better than"`
returns 0, `grep -c "fluency measures"` returns 0, and the rulings file is
cited by path where ruling 10 is stated.

```
grep -c "no better than"    -> section 2 text: 1; whole assembled spec: 1
grep -c "fluency measures"  -> section 2 text: 0; whole assembled spec: 0
lines of section 2 that mention ruling 10: 1
   | 2026-10-07 (ruling 10 of
the path docs/rulings/2026-10-07-two-sided-question-rulings.md appears in the
   joined section text: 2 time(s)
within 400 characters before the 'ruling 10' mention, the path appears: True
```

MEASURED. Two of the three parts pass: "fluency measures" is gone and ruling
10 is stated with the rulings file cited by path beside it. The first part
does not: "no better than" appears once. The hit (version 3, lines 176 to
178, in "How this question loses"):

> And the observer side's premise fails if observers, blind to construction
> and never shown the battery's readings, detect presence in the constructed
> systems no better than in the frontier reference profile. Until the
> construction line produces a system that can be read, this is a question
> and not a finding, and the project says so wherever it describes it.

ARGUED. This is not the sentence RT-283 was about. That sentence pre-stated
"no better than chance" against fluency measures, the option ruling 10 had
closed; it is gone, and ruling 10 is stated in its place. The sentence that
remains is the sixth of the loss conditions RT-285's fix added ("observers,
blind to construction, may detect no more presence in the constructed
systems than in the frontier reference profile"), and it compares against
the frontier reference profile, not chance. What it shares with the deleted
sentence is the thing RT-283 named as the defect: a pre-stated comparison
for an observer study with no instrument and no rehearsal, and a study that
decision 7 of 2026-10-07 deferred. Version 3 guards it with "this is a
question and not a finding" until a system can be read. Whether that
guard is enough, or whether the protocol's rehearsal rule (a pre-stated
threshold with no rehearsal is fatal on its own) bites again, is a call for
the ledger session to put to John when it writes RT-283's closure line; it
is not made here. The letter of the check is a count of 1 against an
expected 0, and that is what the ledger line should say.

## What the next session needs to do

1. Write the ledger rows (`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`, from RT-283 on, plus the tier 2 findings ruling 6 gives numbers to), carrying John's six rulings of 2026-10-12 and, for the three fatal findings, closure lines that name version 3's commit (`bfd1d5d`, merged at `03df5e3`) and this file as the check, with RT-283's line stating the count above and what John rules on it.
2. Only then the commit into the spec, as version 3's "Where it goes" and "What else changes in the spec" set out; the assembled spec's checksum above is what that commit should produce if nothing else changes.
3. A session that wrote neither the rows nor the commit checks both.
