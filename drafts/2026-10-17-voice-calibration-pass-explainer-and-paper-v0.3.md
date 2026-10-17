# Voice Calibration pass: the refreshed explainer and the new text of paper draft v0.3 (2026-10-17)

*Run 2026-10-17 (Pacific) under
`~/Code/calibration-problem/editorial/voice-calibration-protocol.md` (master
version 2026-10-12) on three pieces of new text: `explainer.md` as refreshed
today (whole document); the text added to
`drafts/paper-removal-test-nature-draft.md` for version 0.3 (the two results
sections "The constructed line" and "The successor", the two Methods
paragraphs, the abstract's four new sentences, the replacement Discussion
paragraph and the dated note of 2026-10-17); and
`docs/outside-reader-approach-note-2026-10-17.md`. The v0.2 text of the paper
was not passed and still carries its own header note saying so. Run by the
Claude Code session that wrote all three, so this is a self-pass; the
protocol's own warning applies, that a draft cannot see the blind spot it is
built around, and the Cold Reader report filed beside this one is the second
read. The counts below are from mechanical scans (grep on the files) and the
judgments from a full read. Every change listed was applied in the same
commit as this record.*

## Pass 0, the substance gate: claims and receipts

**Receipts.** Every figure in the three pieces carries the record file it
was copied from, named beside it, as the brief required. Checked on the
record during the pass: the gate 1 positive controls had been quoted from
the compute ledger's rounded 0.943 and were corrected to the findings file's
0.9433 and 1.0000 (`gate1-curriculum-findings.md`); the register-lesion
figures (T_si 0.93 to 0.94 with the injection removed) are quoted from
section 1 of `amendment-a3.md`, which quotes the findings file's thread 4,
and the citation now says so, because the table at line 111 of
`register-lesion-findings.md` is the acting-channel table, not the register
table; the Methods' architecture facts (12 blocks, width 448, a 103-token
closed vocabulary, 585,552,384 tokens per A3 seed, the threshold lock at
commit `6ad4362`, the learn-both bar of 790) were each found in their source
(`gate0-null-calibration-findings.md`, `amendment-a3.md`,
`control-learnability-pilot-findings.md`, `docs/public-path-roadmap-2026-09-16.md`,
`docs/2026-10-09-reruns-10m-run-record.md`). One claim was wrong and is
fixed: the paper said three alternatives to the 0.5 bar were declined and
"the fourth" was the rebuild of arms C and M; the registration's section 5.6
lists four options of which (a) was taken and (b), (c) and (d) declined, so
the rebuild is one of the three declined, kept on the record as the named
route. Nothing is called registered that was not: the positive control, the
fitted position sweep, the ceiling measurement, the control-learnability
pilot and experiment C's four development runs are each labelled
unregistered where they appear.

**Ground truth.** The relabel is quoted exactly from decision 2 of
`docs/rulings/2026-10-07-two-sided-question-rulings.md`; the stop sentence
exactly from decision 2 of
`docs/rulings/2026-10-08-december-result-restatement-rulings.md` and the
stop ruling of 2026-10-12; John's words ("accept the stop", "Approved.",
"Ok, that works for me") from their ruling files. The 2026-10-17 ruling that
C stays stopped is on pull request 172's branch, not yet on the main line,
and both texts say so.

**Adversarial read.** The strongest objection a hostile expert raises is
that the paper now reports three designs that each ended without a positive
and calls that the deliverable. The texts meet it by stating each ending in
its registered terms and by saying, in the explainer's last section and the
paper's "What the constructed line licenses" paragraph, exactly what is and
is not licensed. A second objection, that the relabel of experiment 1 is a
post hoc rescue, is met by reporting the registered verdict and the dated
reassessment side by side and never replacing one with the other; both
texts do this. A third, that the nulls on the constructed model are
evidence of absence dressed as instrument failure, is met by the
registration's own rule (nothing counts as absent until causal patching has
run, and it never ran), which both texts quote.

**Corpus coherence.** The positions touched are the premise (the book's
identity claim, chapter 5, as section 2 version 3 states it), "never a
verdict", and the zombie, which the corpus declines. The old explainer's
sentence "every test a system passes could in principle be passed with
nobody home" conceded the zombie (named as such in
`docs/founding-wager-proposal-2026-09-20.md`) and is removed; the new text
says the gap "does not close by measurement; the premise above bridges it".
The corpus-positions ledger (`sentient-horizons/editorial/corpus-positions-ledger.md`)
was read for those terms; no contradiction, no term used against its fixed
sense, no over-commitment found. The explainer's "zero is a permitted
reading" follows section 2 version 3 and does not conflict with Scope's
"non-zero on the gradient", which that section reads as a statement about
the bracketed question.

## Pass 1, vocabulary

Flagged-word scan on all three pieces: no hits (none of *delve, nuanced,
crucial, pivotal, vital, navigate, landscape, realm, ecosystem, tapestry,
transformative, comprehensive, worth noting, at its core, in many ways, more
than ever, the fact that, indeed, certainly, undoubtedly, stands as, a
testament to, is real*). "Load-bearing" appears in all three, in its precise
structural sense; it is fine outside social posts and the protocol says so.

Load-bearing jargon (pattern 14) and unintroduced references (pattern 27),
explainer: "parameters" is glossed at first use; "battery" was not and is
now ("the record calls each set of test questions a battery"); "seeds" is
now glossed ("three different random starting points"); "shuffled-label
baseline" is now "the score you get with the labels shuffled"; "fitted
classifier" is now "a fitted detector read the model's internal numbers";
"causal patching" now carries its gloss in the explainer as the closure
block gives it; "weight on the true agent" and "route use" are now written
out in plain words where the bars are stated; "John" is introduced once
("the project's author, who rules on every registered decision"). "Row",
from the spec's table vocabulary, is replaced by "indicator" in the
how-it-loses sentence. Paper: T_act, T_other, T_state, T_syntax, L0, L1,
θ and δ are defined where they first appear in the new sections; "sharpness"
is glossed; the two outside reviewers are introduced as "frontier models of
other families". Approach note: "belief-state geometry" and "the external
commentary on the global-workspace paper" are the readers' own work and
are left as references they will recognise; the sources list names the
commentary.

## Pass 2, patterns

**Finite-verb scan.** Explainer: two fragments, both logged as deliberate
and both within the cap: "Never a verdict, and zero is a permitted reading"
(the second clause carries a verb; the first is the project's standing
phrase) and the opening of "Why bother", "Because both mistakes are live",
carried from the original explainer. Paper new text: one fragment found and
fixed ("Three sentences, each bounded by its registration" is now a
sentence). Approach note: clean.

**Em dashes.** Explainer: 0. Paper new text: 6, every one inside quoted
material (the closure's headline as ruled, the v0.2 paragraph quoted in
the dated note, the Authors line), none in prose this pass wrote. Approach
note: 0.

**Negative parallelism and contrastive pairs (patterns 2 and 4).** The
explainer carries several "X, not Y" constructions. Those that quote ruled
wording are kept as quotations: "instrument failure, not absence" (the
closure block), "not a failure of the year" (the restatement ruling), "a
question and not a finding" and "its definition of the floor and not as its
instrument" (section 2 version 3), "a sense organ wired in by design, not a
structure the network built" (Amendment A3, section 3.1). Of the session's
own: "The bet is a premise, not a result" is cut to "The bet is a premise";
"not a slot for any speaker" is cut; "not whether a centre is present, but
how much" is rewritten as a plain question; the closing "is not a positive
result. It is..." is rewritten as "has no positive result to show. It
has...". The thesis sentence "not a spark added to the machinery but a kind
of structure" is the one kept on purpose. Paper new text: the same ruled
phrases are quoted; "rather than" appeared seven times in 5,500 words and
is cut to three (one is the registered metric's "rather than to chance",
one the ruled "halts rather than trims"). Approach note: two "rather than",
both carrying a claim.

**Triplets.** The explainer's list of cheaper routes and the five
indicators are the spec's own lists, content not rhythm. The closing
sentence's four items (the removal test, the constructed model, the
successor, the ledger) are the claim. No decorative triplet found in any of
the three pieces.

**Meta-commentary family (5, 5b, 5c, 13).** One signpost was added on
purpose in the explainer, the italic note at the head of "Building one
instead" telling a reader which two paragraphs carry the outcomes; it is
pattern 21's structural aid, not a transition, and is logged here as a
choice. No "that's the claim" labels, no announced pivots.

**Rhetorical questions (6).** The explainer's two section openers under
"What the project measures now" are the two-sided question's own two
questions, quoted as the content; the opening "Ask 'is this AI conscious?'"
is the original explainer's first line, kept. Logged as deliberate.

**False intimacy (9).** The explainer uses "we" for the project's own acts
("We rebuilt the materials", "We call this the removal test"), which is the
original document's voice and a literal we. The approach note is in "I",
as John's letter; its opening was changed from "I ran three registered
attempts" to "I put one structural claim ... through three registered
attempts", since the sessions ran them and John ruled every step.

**Staccato and stacked fragments (10, 12, 19).** None found beyond the two
logged above.

**Verdicts where diagnoses belong (11).** "It never held anything" (the
register) is a measured fact with its figure beside it. "The control also
did not learn" carries its numbers and the bar. No bare verdicts found.

**Abstraction as actor (22).** "The closure handed one question on" is
rewritten in both the explainer and the paper ("The closure left one
question"); "The question states how it loses" is now "The specification
states how the question loses". Left as they are, because in the project's
own model the documents do act: "the registration said in advance", "the
registered procedure printed".

**Telegraphic compression and orphaned lists (24, 25).** None found.

**Redundant instance lists (26).** The explainer's "lookup from the record,
imitation of a corpus about minds, routing of who is speaking, a trained
response policy, external memory, and the rest" is the spec's named list,
where the items are the claim; kept.

## Pass 3, read aloud

The explainer's "What came out" and "The nulls and the kills" paragraphs
read as a report, which is what they are; the figures are the point and
the sentences are kept short around them. The paper's nulls paragraph ran
to about 600 words in one block and is now four paragraphs, one per run.
Nothing in any of the three pieces reads as a speech.

## Pass 4, texture (essays only; run on the explainer)

Grounding: the ship and the mural, the melody, the sticker on the
machinery, the sense organ, the bridge and the hull. The experiment 06 and
experiment C sections run on numbers for three paragraphs each and are the
densest stretch; the signpost at their head is the structural aid the
protocol allows rather than a flattening of the figures. Controlling
metaphor: deletion (the mural and the one steering), carried from the
original and returned to at "a sense organ wired in by design" and "the
centre that cannot be deleted without the act dissolving"; the melody is
the one other image and appears once, as the premise's picture. No
competing metaphor family was added.

## Pass 5, lay read

The uninformed reader's stops, found on this read and fixed as listed under
pass 1: "battery", "seeds", "shuffled-label", "fitted classifier", "row",
"John". Two stops remain and are reported as options rather than fixed,
because fixing them would lengthen a document already over its target:
"standard deviations" (used twice without a gloss; a common-enough term
that the gloss would condescend to most readers) and "transformer" (used
once, as the model type, with no gloss; the sentence stands without it).
Density: the explainer introduces more than two terms in each of its two
dense sections, which is over pattern 21's working ceiling; the signpost at
their head is the escape hatch, and the Cold Reader report says what that
makes the document.

## Final check, openings and closings

Explainer: the opening is the original's and earns attention. The closing
sentence had ended "including on the floor", a pun that performed; it now
ends "let the results land where they land". Paper: the new sections end on
"What the constructed line licenses", three bounded sentences, which is a
landing and not a summary; the replaced Discussion paragraph ends by naming
where the measurement target went, with the two rulings beside it. Approach
note: each version ends on the one question the reader is asked, as the
shortlist specified.

## Mechanics

Chicago as the default: spelled-out small numbers in prose, numerals for
every measured figure; dates year-month-day throughout, which is the
workspace rule and overrides Chicago's written-out form for this project.
British spelling ("centre", "organised", "behaviour") follows the record
these texts quote; the v0.2 paper text is American ("center"), so the paper
now mixes the two across its old and new sections. **Flagged for John**,
since the protocol says to flag a mechanical choice that changes anything
visible: the fold did not re-spell either half, and one of them has to move
before the draft leaves the repository.

## Length

The explainer is about 2,900 words of prose, about 3,050 with its
citations, against the brief's "under about 2,500"; the glosses this pass
added cost about seventy words. The pass cut what it
could without dropping a required figure; the remaining overrun is reported
in the pull request as John's to settle.
