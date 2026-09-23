# Check of the three repairs: the rebuilt reviewer packets, the file split, and the packet check

*Filed 2026-09-22 (Pacific) by a fresh Claude Code session in its own worktree
(`worktree-agent-a6e776e07ce297658`). Filed verbatim and not edited after
filing.*

*What was checked: three commits on the branch `worktree-agent-aaa22379d64337c97`
— the correction to the handoff document (`7338b60`), the packet rebuild that
gave the ledger excerpt its correcting rows (`d932977`), and the change that
makes the packet check read the committed files (`1263890`). They sit on top of
the already-accepted spend correction (`775fa3b`). The check that demanded these
repairs is the spend-correction check (`1d63aa0`) on the branch
`worktree-agent-aec457e8cc1f311bb`.*

*This session did not write any of those three commits. It fixed nothing. No
file in the repository was edited except this review. The compute ledger was not
edited, no ruled item was edited, no registered text was edited. No machine was
rented and nothing was launched.*

*Method note, stated because it matters for what the results below are worth:
the branch could not be merged into this worktree — the permission system
refused the merge twice — so the three commits were read out of the repository
into a throwaway copy of the whole tree under a temporary directory, and every
check below was run against that copy. The copy is a faithful extract of the
branch's tree. It was also the place where files were deliberately damaged to
exercise the packet check, and it has been deleted. Nothing in the repository
was touched by any of it.*

*Lookup: none used. No web search, no external reference. Every finding below
was produced by reading files in the repository or running code over them.*

---

# The short version

The material that goes to the two outside reviewers is identical between the two
packets and true against the records it claims to reproduce. I confirmed both by
my own method rather than by running the builder's own check. The file split was
the right call and left nothing behind. The handoff document's corrected sentence
is true and sits where that file's own rule allows editing. The sentence left
alone in the inside reviewer's findings was rightly left alone.

The packet check now does what the repair says it does: I broke the packets four
different ways and it caught all four, naming the files, and passed clean again
on restore. But its closing statement about its own coverage claims more than it
delivers, and I demonstrated the gap: the four excerpt records are compared
against the packet document that holds the hand-copied text, not against the
files they name as their sources. A drifted ledger row is exactly what that gap
hides, and it is exactly the failure the excerpt exists to prevent. That is the
one thing I would put right before this merges, and it is one sentence of
printed prose with no rebuild behind it.

**Merge: yes**, once that sentence is corrected.

---

# Part 1 — the packets

## 1.1 Both packets carry the same records — checked my own way

I wrote my own reader for the packet files rather than calling the builder's
check, so that a mistake in the builder's reader could not hide a mistake in the
packets. My reader walks each file, takes everything between a line beginning
`===== RECORD` and the matching line beginning `===== END OF RECORD`, drops the
packet's own prose (the source note and the part note, which are packet
scaffolding and differ between the two deliveries by design), and stitches the
parts of a split record back together.

Result:

- The single-document packet carries 23 record blocks, one per record, numbered
  1 to 23 with none missing and none repeated.
- The 22 pasted files carry 32 record blocks, which are those same 23 records
  with five of them cut into parts — the inside findings, the amendment, the
  registration, the red team ledger and the compute ledger, adding nine blocks.
  No part appears twice.
- Record by record, all 23 are character for character the same in the two
  packets. Not one differs.
- Concatenated in order, the material is **425,871 characters** in each packet,
  and both give the fingerprint
  `33abfc1a582e687a040c8f16983c00ac4e8f195a0be95b94744d5d46f9005879`.

That is the same character count and the same fingerprint the repair reports and
the same pair printed in the operator's instruction sheet. Arrived at
independently, it agrees.

*One false alarm, recorded because it is the kind of thing that wastes an hour.*
My first reader trimmed every blank line from the end of a record part. That is
one line too many: where a record is cut in two, the blank line before the cut
belongs to the record, and the packet restores it when the parts rejoin. The
first run therefore reported the two packets differing by eight characters at
eight seams. The fault was mine, not the packets'. Corrected, the two agree
exactly. The builder gets this right, and its own reader is documented as
removing exactly the lines the renderer adds and no more.

## 1.2 Every whole record matches the file it came from

For each of the 18 records marked as a complete file, I read the source file
named in the record's own header and compared it with the text inside the
packet. All 18 match byte for byte. That covers the text under review, the
inside reviewer's findings, the registered amendment, the registration, the four
measurement records, the five localization records, the three rulings, the
successor design note and the optional background.

## 1.3 The rebuild was needed, and by more than the money

Running the same comparison against the packets **as they stood before these
three commits** shows three whole records that had drifted from their sources:

| record | source file | in the frozen packet | in the repository |
|---|---|---|---|
| the text under review | the version 4 closure text draft | 14,958 characters | 16,650 |
| the registration | the pre-registration document | 44,613 characters | 50,533 |
| the ruling carrying the successor plan | the December-result roadmap ruling | 4,066 characters | 5,885 |

After the rebuild: none. Zero records out of date.

Only the first of those three is the money correction. The other two are source
records that had grown since the packets were frozen and had never been picked
up — the registration and one of the rulings. The old packet check could not see
any of this, because it built a fresh copy in memory and compared it with itself,
which can only ever agree. So the reviewers would have been shown a registration
missing about 6,000 characters and a ruling missing about 1,800, with a check
reporting clean over both. That is worth stating plainly: the staleness this
repair caught was wider than the $1.90.

The operator's instruction sheet does say the rebuild "picked up source records
that had grown since the packets were last frozen, which is why more files than
those two changed". True, but it does not say which. For a packet whose whole
discipline is saying exactly what changed, naming the registration and the
roadmap ruling would be better. Follow-up, not a blocker.

## 1.4 The ledger excerpt is byte-identical to the live ledger

This is the check the repair most needed an outside pair of eyes on, because the
three rows and the dated note were copied in by hand and byte equality was
claimed rather than enforced.

I took the excerpt as it appears in the packet, split it into lines, and for
every line asked whether that exact line exists in the compute ledger. Of 177
lines, **148 are found in the ledger character for character**. The 29 that are
not are the framing paragraphs the packet writes for the reviewer (lines 1 to 30)
and one editorial marker — the row of ellipses that says in so many words
"*(the rows dated 2026-08-07 to 2026-09-18 are not reproduced in this excerpt)*".
Nothing else. No reproduced line differs from the ledger by a single character.

I then checked the order. Walking the excerpt and recording where each line sits
in the ledger gives a strictly increasing sequence from the ledger's first line
to its line 293. Nothing is reordered, nothing is repeated, nothing is moved.

The same test on the other three excerpt records — the closure rule, the red team
ledger and the review of the later draft clause — comes back the same way: every
reproduced line verbatim, in the source's own order, with only the packet's own
framing and two short editorial labels unaccounted for.

So the hand copying is clean. As of this branch, the excerpt is what it says it
is.

## 1.5 The framing paragraph is true, and its figures are mine as well

The framing says five ledger rows and one dated note are reproduced. Checked
against the ledger: the reproduced rows are the five dated 2026-09-19,
2026-09-20 (three of them) and 2026-09-21, and they are the last five rows in the
table. The rows left out are the eleven dated 2026-08-07 through 2026-09-17, so
the framing's "the rows dated 2026-08-07 to 2026-09-18 are not reproduced" covers
them correctly. The dated note reproduced is the ledger's launch-outcome note of
2026-09-20.

I re-derived the corrected figures from the rows rather than reading them off the
framing:

- The row for the checkpoint recovery of 2026-09-20 states the programme running
  total at about **$225.7 of $400** and Amendment A3 at about **$44.3 of $100**.
- The two follow-up runs of 2026-09-20 cost, in the ledger's own words, a
  **measured $1.904** combined — about $1.06 on the first and about $0.84 on the
  second.
- $225.7 plus $1.904 is $227.60. $44.3 plus $1.904 is $46.20.
- The row for the measurement rehearsal of 2026-09-21 states, in its
  running-total column, Amendment A3 at about **$46.2 of $100** and the programme
  at about **$227.6 of $400** — which is where the framing says the ledger states
  the corrected pair, and it does.

That is the pair the framing gives, arrived at two ways. It agrees with the
corrected programme figure of about $227.6 of $400 and Amendment A3 at about
$46.20 of $100.

Every other factual claim in the framing checks out against the ledger's own
note: two machines were created, both were refused by the instrument's check that
a rented machine reproduces a reading already on the record, and both were gone
about 28 minutes after they were made — "deleted inside half an hour" is right.

One small thing, and it is an improvement the repair made rather than a defect:
the old framing said the ledger was "about 49,000 characters", a number written
in by hand that would have gone wrong the moment the ledger grew. The new framing
drops it and points at the length the builder computes, which today reads 86,441
characters and is right.

## 1.6 The corrected figures are findable, and the old one is nowhere claimed as current

Searching both packets:

- The corrected programme total and the corrected Amendment A3 figure appear in
  the text under review, in the ledger excerpt, and in the excerpt's framing.
- The measured **$1.904** appears in the text under review and in two parts of
  the ledger excerpt. The rounded $1.90 appears more widely.
- The superseded $225.7 appears five times in the single-document packet. I read
  every one. Two are inside the closure text's money paragraph and the dated note
  that immediately follows it and corrects it. One is inside the inside
  reviewer's findings, a dated record (see Part 4). One is the ledger's own row,
  which is where that figure legitimately lives. One is inside the ledger's own
  correction note, which supersedes it on the spot.
- The older $215.7 appears seven times, all of them inside dated records — the
  inside findings, the red team ledger's own row on the money finding, and the
  compute ledger's rows and notes, each of which carries its own correction.

**Nothing in the packets' own voice asserts a superseded figure as the current
one.** Every appearance is either a quoted dated record or is corrected in the
sentence beside it.

---

# Part 2 — the file split

**Verdict: the split was right, the new parts are safe, and the renaming left
nothing behind. One readability cost was introduced and is worth knowing about.**

## 2.1 Was splitting right

Adding the three rows and the dated note pushed the file that held the review of
the later draft clause and the whole compute ledger to about 56 KB. The largest
other file in the packet is about 28 KB. The split exists for one reason: a
pasted block small enough to be read rather than turned into an attachment the
app only searches. A file at twice the largest tested size is a real risk to the
one thing the split is for, and it would have failed silently — the reviewer
would have searched the ledger instead of reading it, and nobody would have
known. Splitting was right.

## 2.2 Are the new parts within the sizing precedent

The precedent is an upper bound, not a target, so the question is whether
anything is too big. Nothing is.

- Part 1, with the review of the later draft clause: **24.7 KB** — inside the
  22–29 KB band the larger files sit in.
- Part 2: **16.7 KB**.
- Part 3: **17.4 KB**.

Parts 2 and 3 are below the 22–29 KB band, but they are not below the packet's
range: the existing files run from about 12.4 KB to about 28.4 KB, and six of
them were already between 15 and 17 KB. So the new parts are ordinary by this
packet's own standards. Cutting into three rather than two costs the operator two
extra pastes and buys more headroom under the ceiling; two parts of about 27 KB
each would have been tighter to precedent and closer to the edge. Three is the
more conservative call and I would have made it too.

The seams are at rows the ledger already has — the checkpoint-recovery row of
2026-09-20 and the measurement-rehearsal row of 2026-09-21. The builder refuses a
seam marker that matches more than one line or that lands on a record's first
line, and it asserts that the parts rejoin into the record with nothing added and
nothing lost. My own reader confirms that independently: the three parts stitched
together are character for character the single unsplit record in the other
packet.

## 2.3 Did the renaming leave anything behind

No. Two files were renamed — the one holding the review of the later draft clause
became part 1, and the optional background moved from position 20 to position 22 —
and two were added. The output directory holds exactly 24 files: 22 numbered
files, the single-document packet and the operator's instruction sheet. Searching
the entire repository tree for either old filename returns nothing. The
instruction sheet's file table was regenerated and lists all 22 under their new
names with their new sizes.

## 2.4 Is the sentence telling a reviewer which file holds what correct

Yes. The last file's orientation now reads: the orientation, closure rule and
brief in file 1; the text under review in file 2; the inside reviewer's findings
in files 3 to 5; the registered text in files 6 to 10; and the records the text
cites in files 11 to 21. Checked against what each file actually holds, all five
ranges are right, and stopping the cited range at 21 correctly leaves out file 22,
which holds the background the closure text does not cite. That sentence is
computed from the file list rather than written by hand, which is why it moved
from 19 to 21 by itself.

## 2.5 The one cost the split introduced

The compute ledger is a table with eight columns, and its column headings sit in
part 1. Parts 2 and 3 therefore open on bare table rows with no headings above
them. The red team ledger's parts do not have this problem, because that record
splits at document headings and each part opens with one.

This matters a little more than it sounds, because parts 2 and 3 are precisely
where the money lives: the two rows carrying the $1.904 and the row whose
running-total column states the corrected pair. A reviewer who wants to know
which cell is the actual cost and which is the running total has to go back to
part 1 and count.

Against that: each part carries a note saying what it is and where the other parts
are, and the ledger's cells are heavily self-labelling prose — the cost cell says
"**$0.067** (balance $79.8897 → $79.8228, measured not inferred)" and the running
total cell says "programme running total ~$225.6 + $0.07 = ~$225.7 / $400". A
reviewer can read the figures without the headings. So this is a scratch, not a
wound, and the fix — naming the columns in the part note — would be a change to
packet prose only, which does not disturb the identical-material guarantee.
Follow-up.

---

# Part 3 — the packet check

I exercised it rather than trusting the report. All five runs below were made in
the throwaway copy of the tree, never in the repository.

**Run 0, the baseline.** Checking mode over the branch as committed: exits 0, all
24 files up to date, all 23 records identical in both packets and matching their
sources, 425,871 characters, and the fingerprint matching the one I had computed
independently.

**Run 1, a changed source record.** I added one line to the three-seed endpoint
findings. The check **exits 1** and names the three files that go stale by it —
the file holding the measurement records, the single-document packet, and the
instruction sheet — giving the committed length against the rebuilt length for
each. The record-level table then flags the three-seed record as differing, with
the source fingerprint distinct from both packets' matching fingerprints. This is
exactly the failure the old check could not see, and it now sees it.

**Run 2, a missing packet file.** I removed the second part of the compute
ledger. The check **exits 1**, prints `NOT ON DISK` beside that file's name, and
then **refuses to run the record-by-record check at all**, saying in so many words
that nothing above should be read as saying the committed packets are current.
That refusal is the right behaviour and better than I expected: a partial clean
result is how a check starts lying.

**Run 3, a leftover file.** I put a file back in the output directory under the
old name the optional background used to carry — the precise leftover this
rename could have produced. The check **exits 1** and prints
`NOT BUILT BY THIS SCRIPT - left over from an older build?` beside it.

**Run 4, restore.** With everything put back, the check **exits 0** and its
output is byte-identical to the baseline run.

All four failures are caught, all four name the file, all four exit non-zero, and
the clean run comes back clean. The repair does what it says.

## 3.1 The closing statement claims more than the check delivers

The check ends with a paragraph on what it covers and what it does not. One
clause of it is wrong, and the operator's instruction sheet repeats the same
claim in the same words.

It says it checks "that every record inside the committed packets is character
for character the text in the file it was taken from". The instruction sheet says
"Each of the 23 records was also checked one at a time against the file it came
from".

For the 18 whole-file records that is exactly true. For the **four excerpt
records it is not.** An excerpt's text is not read from the file the record names
as its source — it is read from the packet document that holds the hand-copied
text. So the check compares a hand copy with itself. The named source file is
never opened for comparison at all; it is opened only to count its characters for
the source note.

I demonstrated it rather than inferring it. In the throwaway copy I changed the
ledger's own annotation from a measured spend of $1.904 to $1.914 — a change of
one character, chosen to keep the file the same length so the character count in
the source note would not move. The check then **exits 0 and reports a fully
clean run**: every file up to date, every record identical in both packets and
matching its source, the two packets carrying the same material. Meanwhile the
packet going to two outside reviewers says $1.904 and the ledger says $1.914.

That is the drifted ledger row the excerpt exists to prevent, and the check waves
it through while printing a sentence that says it would not.

Two things to hold on to:

- **It does not mean the packets are wrong today.** I checked the byte equality
  myself, by hand, in section 1.4, and it holds for all four excerpt records.
  What is missing is the tripwire, not the truth.
- **The four excerpt records are not a corner of the packet.** They are 111,894
  of the 425,871 characters of material — **26 per cent** — and they include both
  ledgers.

There is an accidental half-tripwire: because the source note prints the source
file's length, a change that alters the length would show the packet as stale for
the wrong reason. My test defeated it deliberately by keeping the length the
same, and a real edit to a ledger row could easily preserve length by accident.
It is a side effect, not a check.

The rest of the closing statement is accurate, and its "does not check" paragraph
is honest about the things it names — that it cannot say whether the records are
true or current, whether an excerpt flatters the text under review, or whether
anything outside the packets agrees. It simply does not name this one.

---

# Part 4 — the handoff document, and the sentence left alone

## 4.1 The edited sentence

**The judgement to edit rather than annotate was right.** The handoff document's
current-state section opens by saying, in its own words, "*This section is the
current state. Everything below it is the older record, newest first, and is left
exactly as written.*" That sentence draws the line itself: below it is a record,
inside it is a live statement of where things stand. A live statement that is
wrong is simply wrong, and a note saying "the sentence above is untrue" in the
section whose job is to tell the next session what is true would be worse than
fixing it. Annotating is the right move for a dated record; this is not one.

**The new sentence is true.** Checked clause by clause against the ledger's own
launch-outcome note:

| the sentence says | the ledger says |
|---|---|
| no result came off a rented machine | "Neither follow-up run produced a single sweep number on rented hardware" |
| two machines were rented | two machines in one region, named individually, one carrying each run |
| refused by the instrument's own check that a machine reproduces a known reading | the check re-runs a recorded accuracy and demands it return within one episode in 400; on the rented processor it came back off by as much as eleven episodes in 400 |
| deleted inside half an hour | both made at about 19:33 and both gone by about 20:01 — 28 minutes |
| about $1.90 | "Total measured spend $1.904" |

All five hold.

**Nothing below the current-state section was touched.** The change is a single
block at line 14, inside a current-state section that runs to line 112. The file
is 2,335 lines long and holds 54 dated sections below that one. Not one of them
is altered.

One thing I would tidy later: the corrected sentence hangs off a heading reading
"Two follow-up reads, 2026-09-21", and the machines were rented on 2026-09-20.
The sentence itself gives no date, so it says nothing false — but a reader could
carry the heading's date down into it. A follow-up, and a small one.

## 4.2 The sentence deliberately left alone

The sentence is in the inside reviewer's filed findings, in the finding about
whether the programme's money figure could be found in the ledger it cites. It
reads: the block's figure "is right — $215.7 plus the control pilot's $9.9 plus
the $0.067 checkpoint recovery is about $225.7 — but a reader has to do that sum
across two rows that omit the programme total to get there."

**Leaving it is right, for three reasons that stack.**

First, the arithmetic was right on its date. $215.7 plus $9.9 plus $0.067 is
$225.667. "About $225.7" is correct, and it was correct on 2026-09-21.

Second, the finding is not a claim about current spend. It is a claim about
whether a figure could be located in the ledger the closure text cites, and its
closure asks for the running total to be put back on two rows. The number is
working material inside that argument, not an assertion of where the programme
stands.

Third — and this is the one that decides it — the packet tells both reviewers, in
the orientation they read before anything else, that what a reviewer writes "is
filed in the repository word for word, never edited". The findings document
itself says at the top that it was "Filed verbatim and not edited after filing."
Editing it to keep a superseded number tidy would break the rule the packet
advertises to the very people about to rely on it, and it would do so in the one
document that proves the rule is kept. That trade is not close.

**Could a reviewer be misled? A little, and less than it first appears.**

The exposure is real: the finding also says "The last programme running total the
ledger states is ~$215.7 / $400" and "The string '226' does not appear in the
file". Both were true on 2026-09-21 and neither is true of the ledger now — the
excerpt the reviewer is holding shows rows stating $225.7 and $227.6. A reviewer
could spend a finding reporting that.

Four things cut it down. The findings document is headed with its date, the
commit it was read at, and the note that it was filed verbatim — so it announces
itself as a snapshot. The packet's orientation tells the reviewer this is a review
of *the previous version* of the text, already ruled on. The corrected figures
arrive in file 2, before the findings arrive in file 3, so the reviewer meets the
correction first. And the brief expressly invites "the record was shown to you and
does not contain what the sentence says" as a reportable finding, so a reviewer
who trips on it has a cheap, correct way to say so.

The residual risk is a reviewer spending some minutes on a stale figure in a
record already framed as stale. That is worth one sentence somewhere — but the
sentence belongs in the dated note beside the money paragraph, which is packet
prose and freely editable, not in the filed findings. Follow-up.

---

# Findings

## Must fix before this merges

**M1 — the check's closing statement, and the instruction sheet, claim a coverage
the check does not have.** Both say every record is compared with the file it came
from. For the four excerpt records — 26 per cent of the material, including both
ledgers — the comparison is against the packet document holding the hand copy, not
against the named source. Demonstrated in section 3.1: a one-character change to
the ledger that preserves its length produces a fully clean run with an exit code
of 0 while the packet and the ledger disagree.

Why this one blocks. The entire purpose of the change being merged (`1263890`) is
to stop this check reporting clean over material that is out of date. Merging it
with a closing statement that overclaims re-creates the same defect in a softer
form, and the next session to run it will reasonably believe the ledger excerpt
was checked. The repair's own commit message describes the old behaviour as
reporting "a clean run over packets that were out of date"; this is that, narrowed
to excerpts.

What it costs to fix: one sentence in the printed closing statement, and the
matching sentence in the instruction sheet. The closing statement is printed to
the terminal and never written into a packet, so correcting it needs no rebuild.
The instruction sheet is generated, so correcting its sentence means re-running the
builder, which changes that one file and nothing a reviewer reads. Saying plainly
that whole-file records are checked against their sources and excerpt records
against the packet document that holds them would be accurate and would take
nothing away from what the check genuinely does.

Note what M1 is *not*: it is not a claim that anything in the packets is wrong. I
verified the byte equality of all four excerpts by hand and it holds. M1 is about
the tripwire, not the material.

## Can follow afterwards

**F1 — teach the check to compare an excerpt with the file it names.** The real
fix behind M1. Every line of an excerpt that is not packet framing should be
required to appear in the named source, in order — which is the test in section
1.4 and took a few lines to write. That would make the hand-copied ledger rows
self-enforcing rather than checked once by hand. Worth doing before the ledger is
touched again.

**F2 — the ledger's later parts open without column headings.** Parts 2 and 3 of
the compute ledger begin on bare table rows; the eight column names are in part 1.
These are the parts carrying the money. Naming the columns in each part's note
would fix it without disturbing the identical-material guarantee. Section 2.5.

**F3 — say which records the rebuild swept in.** The instruction sheet notes that
source records had grown without naming them. Two did: the registration and the
December-result roadmap ruling, together about 7,700 characters of material the
reviewers will now see and would not have before. Section 1.3.

**F4 — the dated note could say the inside findings carry the older arithmetic.**
One sentence in the note beside the money paragraph, pointing out that the inside
reviewer's findings were filed before the correction and still show the earlier
sum, would spare a reviewer the trip. The findings themselves stay untouched.
Section 4.2.

**F5 — the corrected handoff sentence sits under a heading dated 2026-09-21; the
machines were rented on 2026-09-20.** The sentence gives no date of its own and so
states nothing false. Section 4.1.

**F6 — two rounding statements that pre-date this branch.** The instruction sheet
says none of the 22 files is bigger than 28 KB; the largest is 28.4 KB. The
framing of the review of the later draft clause calls that file "about 47,000
characters"; it is 49,063, and the source note four lines above prints the right
number. Neither was introduced by these three commits and neither changes a
conclusion.

---

# What I checked, and what I did not

Checked: that the two packets carry identical material, by my own reader and my
own fingerprint; that all 18 whole records match their source files byte for byte;
that all four excerpt records reproduce only lines that exist verbatim in the files
they name, in those files' own order; that the ledger excerpt's framing is true and
its corrected figures follow from the ledger's rows by my own arithmetic; that the
corrected figures and the measured $1.904 are findable in both packets and no
superseded figure is asserted as current; that the split parts rejoin exactly, are
within the packet's size range, and left no old filename anywhere in the tree; that
the orientation sentence naming which file holds what is right; that the check
catches a changed source, a missing file and a leftover file, and passes clean on
restore; that the handoff document's new sentence is true in all five of its
clauses and that nothing below its current-state section moved.

Not checked, and out of scope: whether the closure text is right, whether the
inside reviewer's findings were correctly ruled on, whether the ledger's own
figures are right about what was actually spent, whether the excerpts were cut in
a way that flatters the text under review, and whether the packet is the right
packet to send. A clean result here means the packets faithfully reproduce the
records as those records stand today. It does not mean the records are right.

# Verdict

**Merge: yes**, with M1 corrected first. M1 is one sentence of printed prose and
its twin in the instruction sheet; it does not touch what the reviewers are given.
The three commits do what they set out to do, the material going to the two
reviewers is identical and true, and the rebuild caught two stale records nobody
had asked about.
