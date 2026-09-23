# Check of the spend correction that moves the programme to about $227.60 — 2026-09-22

*A checking pass by a Claude Code session working in its own copy of the
repository. This session did not write the correction, and it fixed nothing:
no file the correction touched was edited here, the compute ledger was not
edited, and no machine was rented and no money spent for this check. It exists
because of the first of the four rules John authorised on 2026-09-21 — item 22
of the ruling on review verification and staged spending
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`), which
says a session that writes binding text is always paired with a different
session that checks it.*

*What was checked: the branch `worktree-agent-ad5a9b316eb87451f` at its single
commit `775fa3b`, "Correct the programme spend to the ledger", six files. The
source it propagates from is the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`), which the
correction does not touch. Every total below was re-derived from the ledger's
own rows in this copy of the repository. Nothing was taken from the correcting
session's table, its commit message, or any summary sentence.*

*Every finding is marked **MEASURED** (a command was run and its output is
reported) or **ARGUED** (reasoning from the documents, which a reader can
dispute).*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## The short answer

The arithmetic is right. Every figure the correction states, and every knock-on
figure it worked out, reproduces exactly from the ledger's rows. The reasoning
that rescues the old gap in the earliest rows is also right, and is in fact
better founded than the correction's own explanation of it.

Two things are missing, and one of them is serious.

The serious one: the living handoff document `STATUS.md` still says, in the
section it calls the current state, that the two follow-up reads of 2026-09-21
were "both local, no money spent". That is the exact false sentence this whole
correction exists to undo, it sits in the most-read orientation document in the
repository, and the audit of 2026-09-21 named it as the *first* of the two
record defects to correct. The correction did not touch it and does not mention
leaving it.

The second: the frozen reviewer packets, which are about to go to two outside
reviewers, show those reviewers the superseded figures in three places and give
them a ledger excerpt that appears to confirm the figures. They should not go
out as they stand.

---

## 1. The totals, derived independently

**MEASURED.** Walking the ledger's rows from the 2026-08-11 anchor, adding each
row's actual and nothing else:

| step | added | running |
|---|---|---|
| anchor after the lost 30-million-parameter pilot, 2026-08-11 | — | $105.62 |
| the 30-million re-run, 2026-08-15 | $18.90 | $124.52 |
| wave 1, 2026-08-16 | $25.29 | $149.81 |
| wave 2, 2026-08-17 | $31.63 | $181.44 |
| the two local gate runs, 2026-09-14 and 2026-09-15 | $0.00 | $181.44 |
| the learnability pilot that opened Amendment A3, 2026-09-15 | $13.92 | $195.36 |
| the test of whether a rented machine can delete itself, 2026-09-16 | $0.29 | $195.65 |
| seeds 1 and 2 run as one wave, 2026-09-17 | $20.10 | $215.75 |
| the run that asked whether the control question can be learned when it is taught properly, 2026-09-19/20 | $9.90 | $225.65 |
| recovering that run's final checkpoint, 2026-09-20 | $0.067 | $225.72 |
| the two follow-up reading runs refused by the instrument, 2026-09-20 | $1.904 | $227.62 |
| the measurement rehearsal, 2026-09-21 | $0.02 | $227.64 |

**Programme: $227.64 of $400, headroom $172.36.** Amendment A3's own line, which
begins at zero on 2026-09-14, comes to **$46.20 of its $100 stop, leaving
$53.80**.

The correction reports about $227.60 and about $172.40 for the programme, and
about $46.20 and $53.80 for Amendment A3. **CONFIRMED** at the precision the
ledger carries these figures.

One presentational point, and it is not a defect. **ARGUED.** The stated
headroom of $172.40 is $400 less the *rounded* $227.60, not $400 less the
derived $227.64, which is $172.36. Four cents, in figures the ledger itself
writes as "about". Worth knowing if anyone ever needs the headroom to the cent;
not worth changing.

Corroboration that does not depend on my addition at all: the ledger's own row
for the measurement rehearsal of 2026-09-21 already states, in the ledger and
before this correction was written, "A3 cumulative about **$46.2 / $100**,
programme about **$227.6 / $400**". So does the dated correction of 2026-09-21
inside the launch-outcome note on the two refused runs. The correction did not
invent these numbers; it carried them out of the ledger into the places that
still disagreed with it. **MEASURED.**

## 2. The $2.56 in the earliest rows, and whether it travels

The correction reports a gap that predates it: the first two rows state actuals
of $6.02 and $97.04, which come to $103.06, against a running total of $105.62 —
a difference of $2.56. It attributes this to a 10-million-parameter pilot row
written mid-billing and out of date order, and says everything downstream is
anchored on $105.62 rather than re-added, so the current figure is unaffected.

**The conclusion is right. CONFIRMED, and on firmer ground than the correction
gives for it.**

**MEASURED.** The ledger's own reconciliation note of 2026-08-12 records what
the vendor's console finally charged for each of those early rows, once the
billing had settled: the first row trues up to **$6.645** (it was written at
$6.02 while the anomalous row was still growing), the 10-million pilot row trues
up to **$1.943** (it was written at "$1.26 accruing", mid-billing), and the
30-million row to **$97.035**. Those three come to **$105.623**. That is the
$105.62 anchor, exactly. The gap decomposes as **$1.943** of the 10-million
pilot row plus **$0.625** of the first row's own true-up.

So the correction names the larger of two contributors and not the smaller one.
The mechanism it describes — a row written before its bill had landed — is the
right mechanism and covers both. **ARGUED:** this is an imprecision in the
correction's explanation, not an error in its result.

Two independent checks that the anchor is real money and not a slip:

- **MEASURED.** The account's own balance says the same thing. The baseline was
  $106.73 on 2026-08-07 and the account was parked at minus $0.07 when it ran
  dry, so $106.80 was actually spent. The ledger's $105.62 of machine time plus
  the $1.255 of storage the same reconciliation note records comes to $106.875 —
  agreement inside the dollar that the ledger's own rule 4 asks for. The sum of
  the *written* row values, $103.06, does not come close.
- **MEASURED.** Nothing downstream re-adds the early rows. The 2026-08-15 row
  reads "$105.62 + $18.9", and every row after it chains from the row above.
  There is no point at which the three early `$ actual` cells are summed again,
  so the difference between what those cells say and what the anchor says has no
  route into the current figure.

**The gap does not propagate. The corrected figure stands.**

## 3. The $1.90 and the two rows that carry it

**MEASURED.** Both rows exist, dated 2026-09-20, and they say what the
correction says they say.

- The matched control of Amendment A3 carries "**~$1.06 of a measured $1.904
  combined** … the pair is measured from the account balance, $79.7159 →
  $77.8119, and split between the two rows by pod runtime rather than billed
  separately. **The run did not happen: the pod was refused by the instrument
  check and deleted after about 28 minutes.**"
- The standardised refit carries "**~$0.84 of a measured $1.904 combined** (same
  measurement and same apportioning as the row above). **The run did not happen:
  refused by the same instrument check and deleted after about 27 minutes.**"

The ledger's launch-outcome note of 2026-09-20 gives the rest: two machines in
the same data centre at $2.28 an hour, created about 19:33Z and both gone by
about 20:01Z; both passed their own self-tests on arrival; then a recorded
classifier accuracy failed to come back within one episode in 400, missing by as
much as eleven episodes in 400, on every checkpoint and on both runs. The
machines were repeatable — the same command twice gave bit-identical output — so
the difference is between machines rather than random. No tolerance was widened
and no result was taken from a machine that failed the check. Both machines'
output was checksummed before deletion and zero machines were left running.

So the two runs really were, as several documents said, redone locally and
producing nothing on rented hardware — and they really did cost $1.904. Both
halves are true, which is why the false sentence was easy to write.

**One pre-existing imprecision in the ledger, which the correction may not touch
and neither may I. ARGUED.** The split of $1.904 into $1.06 and $0.84 is 56% and
44%, which at $2.28 an hour implies lifetimes of about 28 and about 22 minutes.
The rows themselves say about 28 and about 27 minutes, which would split almost
evenly, about $0.97 each. The combined $1.904 is the measured figure and is not
in doubt; the apportionment between two rows that roll into the same totals is,
and it moves no total by a cent. Left on the record here for whoever next edits
the ledger.

## 4. `data/project.toml`

**MEASURED.** The two figures match my derivation: Amendment A3's line moves
from 44.3 to **46.2** and the programme envelope from 225.7 to **227.6**. The
explanations beside them are rewritten to the ledger's rows and each one names
what it is counting in plain words. A sweep of the whole file finds no other
live money figure, and the superseded numbers survive in it only inside the new
explanations, as history, which is what they are.

**MEASURED.** `python3 scripts/export_site.py --check`, run offline, output in
full:

    export_site: data/project.toml is valid (8 stages, 7 questions, 12 ideas,
    13 findings, 10 next steps, 27 timeline rows)

Exit status 0.

**The account balance, which the correcting session flagged as possibly beyond
its brief: changing it was right. ARGUED.** The old value, $79.82, was a reading
taken on 2026-09-20 immediately after the checkpoint recovery. The whole subject
of this correction is $1.90 that left the account after that reading. Leaving
$79.82 beside a spend figure that now includes the $1.90 would have made the file
contradict itself in the one place a reader would go to check the correction —
and the correction also moved the as-of date to 2026-09-22, which would have
made the old balance wrong by its own label rather than merely out of date. The
new value, $77.35, is the last balance the ledger records being read from the
account ($77.3451, on 2026-09-21), and the note beside it says so explicitly
rather than passing it off as a fresh reading. That is the honest form of the
change.

The one thing it cannot do is make the balance current: the storage volume drips
about a cent an hour whether or not anything is running, so the true balance on
2026-09-22 is a little lower, around $77.11. The note discloses the reading's
date, which is the right way to handle a number nobody can refresh without
querying the account. Not a defect.

## 5. The note on the ruling file — the first flagged judgement call

**MEASURED.** The change to
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md` is **59
lines added and 0 removed**. It is appended at the end of the file, after the
existing correction note of 2026-09-21. No ruled item is edited, reworded,
renumbered or moved.

**It stays on the bookkeeping side. ARGUED, and I agree with the call.**

The test I applied is whether the note changes anything John decided. It does
not. It releases no money. It changes no amount he authorised — the first
release is still about $44 and the second about $131. It does not answer the
question item 19 explicitly left open. What it does is report that the file the
ruling itself nominated as governing has moved, and state by how much.

That is the same shape as the precedent, though it is a longer reach than the
precedent's own example. What John authorised on 2026-09-21 was annotating
"claims about where text landed, cross-references and the like", and the note
that established it corrected a pointer. This note instead corrects a figure
quoted *inside* a ruled item — item 16's "about $225.70 of $400 spent, headroom
$174.30" — and that figure is also the denominator item 10 measures a release
against. A stricter reader could call that substance.

Three things make me come down on the side of bookkeeping anyway. Item 16's
ruling content is *which file governs*, and that is untouched and still governs;
the amounts inside it were the ledger's own figures on the day and the note says
so plainly rather than calling them wrong. The note states the risk in its own
words — that the line is drawn by whoever is writing — and tells a reader who
disagrees to treat the ruled items as governing and strike the note. And the
alternative, leaving a ruling file quoting a headroom the system of record no
longer supports, is the failure the ruling was written to prevent.

**One small imprecision. ARGUED.** The note says item 19 "moves money between
the releases and does not add any, so it is unaffected". The first half is
right. The second is not quite: item 19 also states that the fold "still leaves
roughly $130 unauthorised", and against the corrected headroom that residual is
about $128.40. It survives item 19's own "roughly", so nothing said there becomes
false — but "unaffected" is a shade stronger than the facts. A follow-up point,
not a blocker.

## 6. The note on the Amendment A3 closure draft — the second flagged judgement call

This was outside the four documents the correcting session's brief named, and it
flagged that.

**Annotating it was right. ARGUED, and this is the clearest call of the two.**

**MEASURED.** The draft's closing paragraph reads: "**Money.** Amendment A3
closed at ~$44.3 of its $100 hard stop, and the programme at ~$225.7 of its $400
ceiling (`compute-ledger.md`, the running totals on the rows dated 2026-09-19 and
2026-09-20)." The second half of that is a present-tense claim about the
programme, cited to the ledger, and the ledger no longer says it.

Three reasons the annotation earns its place. It is a sentence that cites a file
for a number the file contradicts, which is the precise failure the repository's
own citation checker was built to catch. The text is about to be read by two
outside reviewers whose time is the scarcest thing in the review protocol, and a
reviewer who does the honest thing — open the cited file and check — burns an
hour discovering a bookkeeping lag rather than reviewing the science. And the
note draws the distinction the paragraph itself blurs: the $44.3 was right about
the moment Amendment A3 closed, because the follow-up runs came after, while the
$225.7 is simply out of date. That is a genuinely useful thing to have written
down, and neither figure is edited.

The note is fenced as a quotation block, dated, signed as not John's ruling, and
says the closure text above it is left unedited. Nothing about the science, the
verdict or the reasoning is touched.

## 7. What it left alone

**Right to leave. ARGUED.**

- **The filed reviews** under `experiments/06-mvm-0a-constructed-self-index/reviews/`
  and the review bundles under `docs/reviews/2026-09-20-program-review/`. These
  are dated records of what a session found on a day. Their figures were true on
  their dates and a record of a past reading is not made wrong by a later one.
- **The session audit of 2026-09-21** (`docs/reviews/2026-09-21-session-audit-cowork.md`),
  for the same reason — and it is the document that *prescribed* this correction,
  so annotating it would be circular.
- **The two checking scripts' worked examples** (`scripts/check_citations.py` and
  `scripts/check_single_source.py`). **MEASURED:** the superseded figures appear
  there only inside explanatory comments describing the *shape* of a problem —
  "a figure of $215.70 survived in two documents after the ledger had corrected
  it to about $225.70" — not as claims about current spend. Updating them would
  make the illustrations worse and the documents noisier.
- **`STATUS.md`'s older sections**, including the one that says "the whole program
  about $216 of $400". That sits under a 2026-09-19 heading in a file whose own
  header says everything below the top section "is the older record, newest first,
  and is left exactly as written."
- **The superseded earlier drafts of the closure text** (the 2026-09-20, second
  and third versions). Version 4 is the live one and the one the packets carry.
- **`docs/control-clause-proposal-2026-09-19.md`**, which still carries $34.31 and
  $215.70. Those were correct on its date and the 2026-09-21 money correction
  left it alone for the same reason.

**MEASURED, on completeness.** Running `scripts/check_single_source.py` and
reading its list of figures with many homes: the superseded $225.70 appears in
four documents and the superseded $174.30 in four, and between them that is
exactly the set of live documents this correction annotated, plus `data/project.toml`
which it edited. No live document carrying a present-tense programme total was
missed — with the one exception in section 8 below, which carries no number at
all and so does not show up in that list.

### The frozen reviewer packets — these should not go out as they stand

This is the one "left alone" I disagree with, and it is the reason for the
second must-fix.

**MEASURED.** The packets under
`experiments/06-mvm-0a-constructed-self-index/reviews/packets/` show the outside
reviewers "~$44.3" and "~$225.7" in three separate places: the closure text under
review itself, a sentence in the inside reviewer's findings, and the framing
paragraph that introduces the ledger excerpt. A search of every packet file for
any trace of the correction — the balance $79.7159, the balance $77.8119, or the
figure $1.904 — returns nothing. The reviewers would see the superseded figures,
see an excerpt of the ledger that appears to confirm them, and have no way at all
to reach the correction.

**MEASURED.** The packets are generated, and the builder's own instructions say
so: "Re-run it after any source record changes; the packets are generated, never
hand-edited." The closure draft the correction annotated is one of those source
records. It was annotated and the packets were not rebuilt.

**MEASURED, and this is the part that makes it easy to miss.** The builder's
`--verify` mode does not check the files on disk. It builds the packets fresh in
memory from the sources and then compares that fresh build against itself, so it
reports "matches source" for every record no matter how stale the committed files
are. Running it prints a reassuring clean report while the packets on disk are
out of date. Two figures show the drift: `--verify` at this commit computes
395,675 characters of material with one fingerprint, while the packets' own index
file records 386,244 characters with a different one.

**MEASURED, and in fairness to the correcting session: the packets were already
stale before this commit.** Rebuilding the packets from the parent commit's tree
in a scratch copy and comparing against the committed files shows six files
already differing, including the main single-document packet. The drift predates
this correction by roughly 7,700 characters — source records grew after the
packets were frozen. This correction widens an existing hole rather than opening
one.

**ARGUED, on the remedy, because it is not as simple as re-running the builder.**
A rebuild would carry the new note into the closure text the reviewers read,
which is the most important of the three places. It would not fix the other two.
The framing paragraph that introduces the ledger excerpt, and the ledger excerpt
itself, are not read from the live ledger at all — the builder takes them from
a hand-maintained record
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-tier2-packet.md`),
and that record's copy of the ledger is the pre-correction text. Whoever fixes
this needs to touch that file as well as re-run the builder.

Against all this, the honest argument for leaving the packets frozen: both
reviewers must receive identical material, and rebuilding changes the fingerprint
the index records. That argument would be decisive if a packet had already gone
out. Nothing in the repository indicates either session has been run — there is
no filed tier 2 review — and the correcting session's own case for annotating the
draft was that the text is about to go to reviewers. The same fact that justified
annotating the draft requires rebuilding the packets. Doing the first without the
second leaves the note where the reviewers will not see it.

## 8. The one thing that is plainly missing: `STATUS.md`

**MEASURED.** Line 17 of `STATUS.md`, inside the section headed "WHERE THINGS
STAND 2026-09-21" — which the file's own preamble calls "the current state", as
distinct from everything below it — reads:

> **Two follow-up reads, 2026-09-21 (both local, no money spent).**

That is false in its second half, and it is the specific false sentence this
correction exists to undo.

**MEASURED.** The session audit of 2026-09-21 already found it and already said
what to do. Its step 2 reads: "Correct the two record defects that merge exposes:
the 'no money spent' sentence in `STATUS.md`, and the headroom figure of $174.30
wherever it is quoted, which is `data/project.toml`, section 6 of the
December-result roadmap, and item 16 of the 2026-09-21 ruling. Annotate the
ruling rather than rewriting it, per its own convention."

The correction did the second half of that list, all three places, and annotated
the ruling exactly as instructed. It did not do the first half, and its commit
message neither mentions `STATUS.md` nor explains leaving it.

**ARGUED, on why this is the most serious finding here rather than a tidy-up.**
`STATUS.md` describes itself as the living handoff document, the thing a fresh
session reads to find out where the work stands. It is the document a person or
a session goes to *first*. Every other place the superseded figures lived is now
annotated, which means the one uncorrected statement is also the only one left —
and it is in the most-read file. It is not a stale total, which is a small thing;
it is a flat statement that no money was spent, in the file that orients everyone,
about the money this entire correction is about.

The fix is small and its shape is already settled by the audit's own wording: the
reads themselves were redone locally, so "both local" is true and only "no money
spent" is wrong. A dated note, in the same form as the five the correction
already wrote, would close it.

## 9. Plain language

**MEASURED.** Scanning every line the commit adds for bare identifiers: three
hits, "item 7" twice and "Item 16" once, each carrying a plain phrase saying what
it is ("Item 16 ruled that the stale spend figures are corrected to the compute
ledger"). No bare commit names, no bare finding numbers, no unexplained
shorthand. The added prose consistently prefers the plain description to the term
of art — "the run that asked whether the control question can be learned when it
is taught properly" rather than the run's internal name, "a rented machine"
rather than the vendor's word for it. The rule is met.

## 10. Every knock-on figure, recomputed

**MEASURED.** Each one re-derived from the numbers in the documents the
correction annotates, not from the correction's own working.

| claim | check | verdict |
|---|---|---|
| the successor at $130 leaves $42.40 | $227.60 + $130 = $357.60; $400 − $357.60 = $42.40 | correct |
| and $44.30 was the old figure | $225.70 + $130 = $355.70; $400 − $355.70 = $44.30 | correct, and matches the proposal's own sentence |
| a $225 cap puts the programme at $452.60 | $227.60 + $225 = $452.60 | correct |
| leaving $7.40 of a $460 envelope, not $9.30 | $460 − $452.60 = $7.40; $460 − $450.70 = $9.30 | correct, and matches the proposal's own $450.70 and $9.30 |
| nine runs over by $51.87 | cost $224.27 − headroom $172.40 = $51.87 (was $49.97) | correct |
| seven runs over by $20.24 | $192.64 − $172.40 = $20.24 (was $18.34) | correct |
| six runs with margin over by $10.05 | $182.45 − $172.40 = $10.05 (was $8.15) | correct |
| six runs with no margin still fit, leaving $29.95 | $172.40 − $142.45 = $29.95 (was $31.85) | correct |
| no row of that table changes side | the only fitting row still fits | correct |
| the $97.04 loss is 42.6%, not 43.0% | 97.04 ÷ 227.60 = 42.64%; 97.04 ÷ 225.70 = 43.00% | correct, and the document's own note that it was 45.0% against $215.70 also checks out (44.99%) |
| the two releases are $2.60 over, not $0.70 | $175 − $172.40 = $2.60; $175 − $174.30 = $0.70 | correct |
| Amendment A3 leaves $53.80, not $55.70 | $100 − $46.20 = $53.80; $100 − $44.30 = $55.70 | correct |

Twelve for twelve. Each was checked against the original sentence in the
document being annotated, so the starting numbers are the documents' own and not
the correction's restatement of them.

---

## Findings, sorted

### Must fix before this is merged

1. **`STATUS.md` still says the two follow-up reads cost nothing.** Line 17, in
   the section the file calls the current state: "Two follow-up reads, 2026-09-21
   (both local, no money spent)." It is the exact claim this correction undoes,
   it is in the repository's most-read orientation document, and the audit of
   2026-09-21 listed it as the first of the two record defects to correct. The
   correction did the audit's other three places and left this one, without
   saying why. A dated note in the same form as the five it already wrote would
   close it. **MEASURED.**

2. **The frozen reviewer packets must not go to the two outside reviewers as they
   stand.** They show the superseded figures in three places, with a ledger
   excerpt that appears to confirm them and no trace of the correction anywhere.
   The builder's instructions say to re-run it after any source record changes,
   and the annotated closure draft is a source record. The builder's `--verify`
   will not catch this: it compares a fresh build against itself and never reads
   the committed files, so it reports a clean run over stale packets. Note two
   things for whoever fixes it: the packets were already stale before this commit,
   by about 7,700 characters, so this is a pre-existing hole that the correction
   widens rather than opens; and re-running the builder alone is not enough,
   because the framing paragraph and the ledger excerpt come from the
   hand-maintained packet record rather than from the live ledger. **MEASURED.**

   If John would rather merge now and fix the packets separately, that is a
   reasonable call — the correction itself is sound and merging it is what makes
   the note official. What is not reasonable is the packets going out before this
   is dealt with. I put it in this tier because merging it silently is how it
   gets forgotten.

### Can follow afterwards

3. **The explanation of the $2.56 names one of two causes.** The gap is $1.943
   of the 10-million-parameter pilot row plus $0.625 of the first row's own
   console true-up. The mechanism the correction describes covers both; its
   sentence names only the pilot. The conclusion is unaffected. **MEASURED.**

4. **"Item 19 is unaffected" is a shade strong.** Item 19's stated residual,
   "roughly $130 unauthorised", is about $128.40 against the corrected headroom.
   It survives item 19's own "roughly", so nothing there becomes false.
   **ARGUED.**

5. **The stated headroom is the complement of the rounded total.** $172.40 is
   $400 less $227.60; $400 less the derived $227.64 is $172.36. Four cents, in
   figures written as "about". **MEASURED.**

6. **A pre-existing imprecision in the ledger, for whoever next edits it.** The
   split of the measured $1.904 into $1.06 and $0.84 implies machine lifetimes of
   about 28 and 22 minutes, while the two rows say about 28 and about 27. The
   combined figure is measured and is not in doubt, and the split moves no total.
   Outside this correction's reach, and outside mine. **MEASURED.**

7. **The recorded balance cannot be current.** $77.35 is the last reading the
   ledger holds, from 2026-09-21; the storage volume drips about a cent an hour,
   so the real figure on 2026-09-22 is nearer $77.11. The note beside it
   discloses the reading's date, which is the right handling. **ARGUED.**

8. **The builder's `--verify` gives false reassurance.** It never reads the
   committed packet files. Worth fixing on its own account, independently of
   this correction, because it is the check that should have caught finding 2.
   **MEASURED.**

### Verdict

**Yes, merge — once finding 1 is in.** The arithmetic is sound in every
particular I could test, the reasoning about the old gap is right and better
founded than its own explanation, both flagged judgement calls were called
correctly, and every one of the twelve knock-on figures reproduces. Finding 1 is
a one-line omission in the most-read file in the repository, on exactly the point
the correction is about, and it was already on the audit's list; merging a spend
correction while the handoff document still says no money was spent would undo a
good part of what the correction buys. Finding 2 does not have to block the
merge, but it must be on the record and settled before either reviewer session is
run.
