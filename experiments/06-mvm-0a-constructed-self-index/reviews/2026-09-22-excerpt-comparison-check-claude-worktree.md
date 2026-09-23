# Check of the excerpt comparison: does the packet check still report clean over material that disagrees with its source?

*Filed 2026-09-22 (Pacific) by a fresh Claude Code session in its own worktree
(`worktree-agent-a0a04be4ca93fbc37`). Filed word for word and not edited after
filing.*

*What was checked: the commit that adds the excerpt comparison
(`92f0061`, "Check the four excerpts against the files they name, and stop
overclaiming") on the branch `worktree-agent-ade459041561e5e48`. It touches two
files: the packet builder `scripts/build_a3_closure_tier2_packets.py` and the
generated instruction sheet
`experiments/06-mvm-0a-constructed-self-index/reviews/packets/2026-09-21-a3-closure-tier2-INDEX-how-to-run-these-sessions.md`.
It sits on earlier repair commits: the spend correction (`775fa3b`), the
handoff correction (`7338b60`), the packet rebuild that gave the ledger excerpt
its correcting rows (`d932977`) and the change that made the check read the
committed files (`1263890`). The check that demanded this repair is the packet
rebuild check (`56f76b5`) on the branch `worktree-agent-a6e776e07ce297658`,
whose finding M1 and section 1.4 said the four excerpts were compared with the
hand copy in the packet document rather than with the files they name.*

*This session did not write that commit. It fixed nothing. The branch was
brought into this worktree as a fast-forward, so every result below was produced
against the real tree at `92f0061`, not against a copy.*

*Files deliberately damaged to exercise the check, all restored and every
restoration proved by a sha256 checksum against the value recorded before the
damage: the red team ledger, the independent review of the Amendment A4 clause,
the three-seed endpoint findings, the outside-review protocol, and the packet
files. The compute ledger was not edited. No registered text, no ruled item and
no filed review was edited. Nothing was rented and nothing was launched. At the
end `git status` is empty and the full check run is byte-identical to the run
taken before any test.*

*Lookup: none used. Every finding below came from reading files in the
repository or running code over them.*

---

# The short version

The thing this repair exists to prevent no longer happens. I damaged the
material eleven different ways, including four ways the writing session did not
try, and the check caught every drift that is on the page and named the file,
the line and the text. The two cases it does not catch are the two it says out
loud it cannot catch.

The design decision that carries the whole thing — that what counts as the
packet's own words is written down in the script rather than worked out from
whether a line happens to match — is right, and I checked the thing that would
make it wrong. Every single line now excluded from comparison, in all four
excerpts, is absent from the file that excerpt names. There is no reproduced
line hiding in the excluded set. A fabricated ledger row put in the place of an
excluded label is reported twice over, not waved through.

The closing statement is true in every particular I could test but one, and that
one is a matter of which check earns a claim rather than whether the claim
holds. It says the two packets carrying the same records **in the same order**
is shown by the matching checksum. The checksum does not show order: I moved two
whole records past each other inside the one-document packet and the checksum
still matched. The run still failed, loudly and by file name, because a
different check caught it — so nothing was reported clean that was not clean.
The sentence gives the credit to the wrong check.

**Merge: yes.** Nothing I found must be fixed first.

---

# Part 1 — does the excerpt comparison actually detect drift?

I did not replay the writing session's tests. I devised eleven of my own. Four
of them are kinds of damage it did not try: drift that is only whitespace, drift
in a file it never touched, a reproduced line deleted rather than altered, and a
line whose only change is a trailing space.

Every test below was run against the real tree. The ones marked "in memory" fed
a damaged copy of a record's text straight to the comparison in a scratch script
and touched no file at all; the rest damaged a real file, which was then
restored and its checksum re-checked.

## 1.1 The baseline

`python3 scripts/build_a3_closure_tier2_packets.py --verify` exits 0. Every one
of the 24 packet files reads "up to date". The four excerpts report 27, 253, 71
and 134 reproduced lines against the outside-review protocol, the red team
ledger, the independent review of the Amendment A4 clause and the compute ledger
respectively. The material comes to 425,871 characters under the fingerprint
(a sha256 checksum) `33abfc1a582e687a040c8f16983c00ac4e8f195a0be95b94744d5d46f9005879`.
Those are the figures the writing session reports, and I got them by running it
myself, not by reading them.

## 1.2 Drift that is only whitespace, and keeps the line the same length — caught

In the red team ledger I turned one space into a tab, inside a line the excerpt
reproduces. The line is the same length, so the packet files still match a fresh
build and the file-level check has nothing to say. This isolates the excerpt
comparison as the only thing that could catch it.

    every committed packet file matches a fresh build: YES

    20  the red team ledger - every row and range the text under review cites
         DOES NOT MATCH `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`:
           line 33 of the record is nowhere in the source file:
           'interpretation of the fitted eleven-position sweep (FOUND NOWHERE, not'

Exit code 1. This is the test that matters most, because a tab and a space look
the same to a reader and the file length gives nothing away.

## 1.3 One character changed in a file the writing session never damaged — caught

The writing session exercised the compute ledger, the red team ledger and the
outside-review protocol. It did not touch the fourth excerpt's source, the
independent review of the Amendment A4 clause. I changed a commit identifier
there from `df039ca` to `df039cb` — one character, same length, and exactly the
sort of drift nobody would see by eye.

    every committed packet file matches a fresh build: YES

    21  the independent review of a later draft clause - the finding the text cites
         DOES NOT MATCH `experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`:
           line 14 of the record is nowhere in the source file:
           '(the 2026-09-19 control-clause proposal, at commit `df039ca`), which i'

Exit code 1. All four excerpts are live, not just the three already tested.

## 1.4 A change inside a line the packet treats as its own label — caught twice

I changed the label `*The finding in full:*` to `*The finding, in full:*` in both
packets — one comma.

    the declared packet label is no longer in the record: '*The finding in full:*'
    line 75 of the record is nowhere in the source file: '*The finding, in full:*'

Two separate complaints: the label the script was told to expect has gone, and
the line that replaced it is not in the source file. This is the right shape. A
label that is edited stops being excluded and immediately falls under the
comparison, so the exclusion cannot be inherited by whatever replaces it.

## 1.5 A fabricated ledger row in the place of an excluded label — caught (in memory)

The strongest form of the worry behind the declared-editorial design. In the
compute ledger excerpt I replaced the row of ellipses that says which rows are
left out with a plausible-looking money row,
`| 2026-09-05 | fabricated run | $0.00 | - | - | - | - | $227.60 |`.

    the declared packet label is no longer in the record: '| … | … | *(the rows dated 2026-08-07 to 2026-09-18 are not '
    line 90 of the record is nowhere in the source file: '| 2026-09-05 | fabricated run | $0.00 | - | - | - | - | $227.60 |'

The fabricated row does not inherit the exclusion. This is the case the design
is for, and it holds.

## 1.6 A trailing space added to a quoted line — caught (in memory)

In the closure-rule excerpt, which the packet reproduces as a block quote, I
added a single trailing space to one quoted line. Rendered as markdown the two
versions are indistinguishable. Reported as nowhere in the source file. The same
line with the `> ` prefix stripped, and the same line with one letter changed,
are both reported the same way.

## 1.7 A fabricated sentence among the reproduced lines — caught (in memory)

`and the gates were in fact applied to all three seeds.` inserted between two
reproduced lines of the A4 review excerpt: reported as nowhere in the source
file. A reviewer cannot be handed an invented sentence dressed as a quotation.

## 1.8 Two reproduced lines swapped, and the same line reproduced twice — both caught (in memory)

Swapping two adjacent reproduced lines is reported as out of order. Reproducing
the same source line twice is also reported as out of order. More on the second
in part 5.

## 1.9 The declared first reproduced line altered — caught (in memory)

If the first line an excerpt reproduces is edited, the script can no longer tell
the excerpt from the paragraphs introducing it, and says so:

    the declared first reproduced line matches 0 lines of the record, so the
    excerpt cannot be told from its framing

It reports nothing as checked rather than checking what it can and calling the
rest clean. That is the right failure.

## 1.10 A reproduced line deleted rather than altered — not caught by this comparison, and it says so

I deleted one reproduced line from both packets. The excerpt comparison reported
no problem at all — 70 reproduced lines instead of 71, and a clean line:

    21  the independent review of a later draft clause - the finding the text cites
         70 lines reproduced, every one of them in `...red-team-a4.md`

The deletion was caught, but by two other checks: the committed packets no
longer matched a fresh build, and the record no longer matched the packet
document. The run exited 1.

The same is true of a reproduced line replaced by spaces (in memory, no problem
reported), because a blank line reproduces nothing and is skipped.

This is not a defect. It is the limit the closing statement states in so many
words: "Nor can it see what an excerpt leaves out: it tests every line that is
on the page, not whether a line that should have been kept is missing." I
tested that sentence and it is exactly true, including the part where something
else catches the omission today. The uncovered case is the one where the
omission is made further upstream, in the packet document, and the packets are
then rebuilt from it — nothing in this script would notice.

## 1.11 Restoration

Every damaged file was restored and every restoration proved:

- the red team ledger, before and after: `db5c38ef6c1a6d74f86469e0500f12833d3aaf1dcda87c4d5b8629566f8315e1`
- the independent review of the Amendment A4 clause, before and after: `6e9ecf081661a0644ae748e8098ed99fc6716b550d467e5e0507ae5e63b7e919`
- the outside-review protocol, before and after: `b72c4d1bfc5db33a785580a275252dd4383f7406055d92dd53b4330a2f685b0c`
- the three-seed endpoint findings, restored, `git status` clean
- all 24 packet files: the list of their 24 checksums is character-identical to
  the list taken before any test, checked after each of the three tests that
  touched them and again at the end

At the end, `git status` reports nothing changed, and the output of
`--verify` is byte-identical to the baseline run taken before the first test,
exit code 0.

---

# Part 2 — the design decision: declaring the packet's own words rather than inferring them

The reasoning the writing session gives is that inferring would let a drifted
ledger row excuse itself by failing to match, which is the exact failure this
repair exists to end. I agree, and section 1.5 shows the declared version
refusing that excuse.

The question asked of me is the opposite one: is any line now excluded from
comparison in fact reproduced from a source? That would be a hole hiding in
plain sight — content a reviewer reads as quoted, never checked against
anything.

I listed every excluded line in all four excerpts and looked each one up in the
file that excerpt names, in both its plain form and, where the packet quotes as
a block quote, with the `> ` taken off. The excluded lines are 64 lines of
introducing paragraphs across the four excerpts and 7 declared labels — 70
distinct lines in all, because one of the labels also stands among the
introducing paragraphs. That matches the counts the check itself prints beside
the four excerpts (2, 28, 11 and 29).

**Not one of the 70 appears in the file its excerpt names.** They read as what
they claim to be: the packet telling the reviewer what the excerpt is, which
rows are left out, and where the omissions fall. Nothing quoted is sitting among
them.

I also checked the reverse: none of the 7 declared labels appears in its source
file either, so a declaration cannot be swallowing a real source line by
coincidence.

The verdict is that the declarations are right, today, line for line.

One structural note, for the record rather than as an objection. The three
declarations on each excerpt — the first reproduced line, the labels, and the
block-quote prefix — exist only in the script. Changing them changes no packet
file, so a future editor could widen what is excluded and the run would stay
green. What stands against that is the line counts the check prints beside each
excerpt, which is why they are printed, and which the closing statement points
at. A cheap way to close it entirely would be for the check to complain if a
line it was told to exclude turns out to be in the source file after all — I
confirmed such a complaint would be silent today. That is a suggestion, not a
finding.

---

# Part 3 — is the closing statement true?

The closing statement is long and specific, so I tested its claims rather than
reading them. Claim by claim:

**"a record that changed after the packets were last built is reported as
stale, by file name"** — true. I appended a line to the three-seed endpoint
findings. The instruction sheet, the measurement-records file and the
one-document packet were each named as stale, with committed and rebuilt lengths
side by side, and the three-seed record was marked as differing. Exit 1.

**"no packet file is missing"** — true, and better than the sentence says. I
moved one of the 22 pasted files out of the folder. It was named `NOT ON DISK`,
and the check then stopped:

    Stopping here. The record-by-record check needs every packet file on
    disk, and 1 of them is missing, so it cannot be run. Nothing above
    should be read as saying the committed packets are current.

The record-by-record block did not run at all — I confirmed by counting: zero
lines of it were printed. It refuses rather than checking what is left and
calling that a result.

**"none is left over from an older build"** — true. I put a stray file in the
folder; it was named, with the reason, and exit 1.

**"the two packets carry the same records in the same order, shown by a matching
sha256 checksum"** — the first half is true, the words "in the same order" are
not shown by the checksum. See part 4.

**"the brief's amended sentence is word for word the protocol's"** — true. I
changed "polite" to "genial" in the protocol, keeping the length so the
file-level check stayed clean, and the run reported
`the amended sentence of the brief is word for word the protocol's: NO`,
exit 1.

**"A record that reproduces a whole file is compared with that file, character
for character"** — true; the three-seed test above is the demonstration.

**"An excerpt ... every line it reproduces has to be in the file the record
names, character for character, and those lines have to run strictly forward
through that file - nothing reordered, nothing repeated, nothing quietly
reworded"** — true in all four clauses; parts 1.2, 1.3, 1.6, 1.7 and 1.8 between
them exercise each one.

**"It does not compare: the words the packet writes around an excerpt - the
paragraphs introducing it and the labels saying which rows are left out"** —
true, and genuinely uncovered. I put a fabricated sentence that reads like a
quotation above the declared first reproduced line of the A4 excerpt; it was
counted as one of the packet's own lines and compared with nothing, no problem
reported. That is precisely what the sentence says will happen.

**"and the brief, whose source is the packet document that already held it"** —
true. The brief record names the earlier packet document as its source, so the
comparison that prints "matches source" for it is comparing that document with
itself. The statement says so plainly, and so does the instruction sheet.

**"Nor can it see what an excerpt leaves out"** — true; part 1.10.

**Is anything else quietly uncovered?** I went looking. The record titles, the
source notes, the record list and the orientation prose are all generated, so a
hand edit to any of them shows up as a stale file — covered, if not by the
sentence then by the check. The instruction sheet is itself one of the files
compared against a fresh build, so it cannot drift unnoticed. The excerpt
comparison reads only the one-document packet's copy of each record, but the
pasted files' copy is required to hash identically to it, so a difference there
fails the run. The only uncovered things I could find are the three the
statement already names.

---

# Part 4 — the one thing the closing statement gets wrong

The sentence reads: "that the two packets carry the same records in the same
order, shown by a matching sha256 checksum".

The fingerprint is taken over the records sorted by their record numbers, not
over the order they physically appear in. So it cannot show order. I proved it:
I moved record 8 and record 9 past each other inside the one-document packet,
keeping the file the same length.

    2026-09-21-a3-closure-tier2-gemini.md   STALE - committed 444,026 characters,
                                            rebuild 444,026, same length but different text
    Gemini  sha256 33abfc1a582e687a040c8f16983c00ac4e8f195a0be95b94744d5d46f9005879
    ChatGPT sha256 33abfc1a582e687a040c8f16983c00ac4e8f195a0be95b94744d5d46f9005879
    the two packets carry the same material: YES

The checksum shrugged. The reorder was caught, by the comparison against a fresh
build, which named the file and said in as many words that it was the same
length but different text. Exit 1.

So this is not the overclaim the last round found. Nothing was reported clean
that was not clean, and the reviewers cannot be handed a reordered packet
without the check failing. What is wrong is only which check gets the credit:
the order is held by the rebuild comparison, and the checksum shows that the
same records with the same content are in both packets. A truer sentence would
say the checksum shows the two packets carry the same records, and leave the
order to the sentence about the fresh build that already carries it.

I am not asking for that before merge. It is a sentence of printed prose about a
guarantee that does exist, attributed to the wrong half of the run.

---

# Part 5 — the limitation flagged for me: reproduced lines must run strictly forward

The question is whether it is an acceptable limitation or a trap for a future
editor. I confirmed the behaviour first: a source line reproduced twice on
purpose is reported as `out of order`, not as a repeat. None of the four
excerpts does this today, which is why the run is clean.

The rule bites in two ways, not one. Beyond repeating a line, it also requires
an excerpt's pieces to appear in the order the source file has them. The red
team ledger excerpt is four separate stretches of one file, and the check passes
today, which is itself the proof that those four are in the ledger's own order.
An editor who reordered them for readability would fail the check.

My judgement: acceptable, and not a trap, for three reasons.

It fails loudly and in the safe direction. A future editor who repeats a line
gets a hard stop with the file, the line number and the text, not a silent pass.
The bad outcome for a checking tool is the green run over bad material, and this
is the opposite of it.

It is disclosed. The closing statement already says the reproduced lines have to
run strictly forward through the source file with "nothing reordered, nothing
repeated". An editor who reads the statement the check itself prints has been
told.

It is defensible on its own merits. Reproducing the same source line twice in
one excerpt, or presenting pieces of a record out of the record's own order, is
worth stopping to think about in material that goes to an outside reviewer as a
faithful reproduction.

The one thing I would soften, if anyone is touching this file again anyway, is
the wording of the complaint. "Out of order" is the wrong words for a line that
is deliberately repeated, and an editor could lose a little time on it. A phrase
like "out of order, or reproduced more than once" would cost nothing. Again a
suggestion, not a finding.

---

# Part 6 — the packets themselves are unchanged

Verified independently of the writing session's report.

The commit changes exactly two files: the builder script and the instruction
sheet. The 22 pasted files and the one-document packet are not among them, so
they are unchanged to the byte.

The instruction sheet's change is one paragraph, replacing two lines that said
each of the 23 records was checked against the file it came from with ten lines
that say how the 18 whole files, the 4 excerpts and the 1 carried-over brief are
each checked, in the way each is made. Those counts are right: I counted the
records and got 18 whole, 4 excerpts and 1 protocol text, 23 in total.

The material still comes to 425,871 characters under the fingerprint
`33abfc1a582e687a040c8f16983c00ac4e8f195a0be95b94744d5d46f9005879`, which I got
by running the check rather than by reading the report. The part of the script
that assembles the material and the part that reads the records back out of a
built file are both untouched by this commit, and the one-document packet is
unchanged to the byte, so the fingerprint could not have moved.

---

# Part 7 — findings

## Must fix before merge

None.

## Can follow

**Finding 1 — the closing statement gives the checksum credit for showing
order, which it does not show.** Part 4. Demonstrated by moving two records past
each other inside the one-document packet and watching the checksum stay
matched. The guarantee itself holds — the rebuild comparison caught the reorder
and the run failed — so nothing is reported clean that is not clean. One
sentence of printed prose.

**Finding 2 — the instruction sheet names only half of what goes uncompared
around an excerpt.** Its new paragraph says the paragraphs introducing an
excerpt are the packet's own words and are compared with nothing. It does not
mention the 7 labels written in among the reproduced lines, which are also
uncompared. The closing statement the check prints does name both. The gap
matters least for the italic labels in the A4 excerpt and most for the compute
ledger's row of ellipses, which is laid out as a table row. Low severity: the
row is in italics and says in plain words that rows are not reproduced, so no
reviewer would read it as a ledger entry.

**Finding 3 — a stale figure in the packet's own words, which this design
leaves uncompared.** In the A4 review excerpt the packet's introducing paragraph
says the source file is "about 47,000 characters". The file is 49,063
characters, and the generated source note eight lines above it in the same
record says so. A reviewer reads two different lengths for one file.

This is not caused by the commit under check, and it cannot be fixed inside it:
the packet material is required to stay byte-identical, and that paragraph lives
in the hand-maintained packet document. I raise it because part 2 asked whether
anything excluded from comparison is hiding something, and this is the one thing
I found there — not a quotation hiding among the packet's own words, but a
number in the packet's own words that has gone out of date. It is the
predictable cost of the declared-editorial design and it argues for the same
cheap safeguard part 2 suggests, or for having the introducing paragraph cite
the length the way the compute ledger's paragraph does, by pointing at the
source note instead of restating the figure.

**Finding 4 — the word "repeated" would read better than "out of order" when a
line is reproduced twice.** Part 5. Cosmetic.

**Finding 5 — nothing checks that a line declared as the packet's own words is
absent from the source file.** Part 2. True of all 70 such lines today; I
checked every one. A future widening of a declaration would not be caught except
by a reader noticing the printed line counts move.

## The thing that had to be true

A checking tool that overclaims is worse than none. The failure that brought
this round about — a clean run and an exit code of 0 over a packet and a ledger
that disagreed by one character — does not happen any more. I reproduced the
shape of it four ways, including a whitespace-only change and a change to a file
the writing session never exercised, and the check named the file, the line and
the text and exited 1 every time. Its statement of what it does not cover is
accurate, and I confirmed each uncovered case is genuinely uncovered rather than
being quietly covered or quietly broader than stated.

**Merge: yes.**
