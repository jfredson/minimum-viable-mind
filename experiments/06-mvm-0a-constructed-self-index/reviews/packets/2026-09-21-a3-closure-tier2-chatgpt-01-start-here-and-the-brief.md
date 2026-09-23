# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 1 of 22: Start here: what this is, and the brief

*This packet arrives as 22 files pasted into this one conversation, in order.
This is file 1. Do not begin your review until file 22 has arrived: reply to
each file with one short line saying you have it, and nothing else. Give your
full answer only after the last file. Read each file as text, start to finish,
rather than searching it. The brief you are answering is in this file, below.
Label your findings A1, A2, A3 and so on.*

*If a file arrives cut short, or the app turns one into an attachment you can
only search rather than read, say so at once and name the file, before going
on.*


## What you are looking at, from a standing start

You are reviewing one short document - about 2,300 words - before it is
committed to a record that cannot afterwards be edited. With it you have been
given every record that document cites: whole where the file was short enough
to reproduce, and as a marked excerpt where it was not.

**The program.** Minimum Viable Mind is a small independent research program,
run by one person on a budget of a few hundred dollars. It asks whether a
machine can be built so that a model of itself is load-bearing: so that the
system cannot do its task well without using a signal telling it which of the
things in front of it are its own. The way it asks is to train small language
models - about 30 million parameters, small enough to train from scratch for a
few dollars - on tasks built for the question rather than borrowed, and to
write down in advance what would count as a result and what would count as a
failure. That written-in-advance document is called a *registration* here.
Once committed, a registration is never edited; a change to it is a numbered
amendment, also committed before anything runs. It is the discipline a
clinical trial uses when it registers its endpoints before it enrols anyone,
and for the same reason: it stops the question being quietly replaced by the
one the data happened to answer.

**Amendment A3** is the registered amendment whose experiment is being closed
here. Under it, four agents take turns revising a shared piece of text, and the
model is given an *ownership* input: a signal saying which of the four agents'
revisions are its own. Three sets of tasks are scored - a primary set the
design intends to be impossible to do well without using that signal, a syntax
set that should not need it, and a state set that needs memory of what has
happened but not ownership. The registered test was a comparison, not a single
number: the ownership input is zeroed, and what would have counted is not that
performance falls, but that it falls on the primary set and not on a matched
control set built to demand everything the primary set demands *except*
ownership. That matched control is the part that could not be built, and that
is what the document you are reviewing is about.

**A closure text** is the block appended to a registration to say how the
experiment ended: which registered condition fired, what was measured, what was
never run, and what the result may and may not be read as claiming. It is the
last thing a registration receives. Once appended it is registered text, and
the program's own rules forbid editing it afterwards. That is why this review
happens now, before it is appended, and not after.

**"Not testable" is a registered outcome here, not a shrug.** Before anything
ran, the registration named the conditions under which the experiment would
have to be abandoned rather than reported. One of them says that if no control
condition can be built that is free of ownership and still demanding at its
own ceiling, then the comparison at the heart of the design is dead and the
honest report is "not testable". The document says that condition fired, and
says why: the control set's ownership-blind ceiling was measured at 1.0, which
leaves the registered metric dividing by zero - the arithmetic saying,
correctly, that there is nothing left to measure. Awkwardly, the same phrase
"not testable" is also the name of a different registered bin, for a lesion
that damages the model so broadly that no reading of it can be trusted. The
document distinguishes the two; whether it does so clearly enough is fair game
for you.

**Why you and not somebody inside the program.** Review here runs in two
tiers. The inside tier is a fresh session of the same model family that wrote
the text, cut off from the conversation that produced it, given the repository
and able to run code - which is why its findings can report a command and the
output it gave. You are the outside tier: at least two models from other labs,
shown documents rather than a running checkout, so every finding you make is an
argued one rather than a measured one. Two outside reviewers are used because
the disagreement between them is the signal. Do not assume the other reviewer
was shown something you were not; you have both been given the same material.

**What has already been done to this text.** An inside reviewer read the
previous version against the registration and found six fatal problems and many
smaller ones. Every finding was ruled on and the text was rewritten. You are
reading the rewrite, and you have that reviewer's findings in full. You may
agree with them, disagree with them, or find that answering one of them created
a new problem.

**What happens to what you write.** It is filed in the repository word for
word, never edited, with your model, your version as the app reports it, the
date and the mode at the top. Each finding is ruled on one at a time: accepted,
accepted with a change, declined with the reason on the record, or carried as
an open item. A ruling to keep the text over your objection is a valid outcome
and goes on the record with its reason. Nothing is appended to the registration
until both outside responses are filed, every item is ruled on, and the closure
rule below is satisfied.

**How to report something you were not given.** When you cannot check a claim,
say which of two things is true: the record was not shown to you, or the record
was shown to you and does not contain what the sentence says. The second is a
finding about the text. The first is a defect in this packet - worth reporting,
but not a mark against the document. Name the file either way.

**A note on the excerpts.** Three files were too long to reproduce whole. Each
appears below as an excerpt that names its source file, gives that file's full
length, and states what was left out; the part reproduced is the part the
citation points at, quoted unedited. If an excerpt has been cut in a way that
flatters the text under review, say so - that is a finding about this packet,
and it is worth having.

**How the material is marked.** Every record below opens with a line beginning
`===== RECORD` that names it, says whether it is a complete file or an excerpt,
and gives its path in the repository, and closes with a line beginning
`===== END OF RECORD`. Cite records by that path.


## The records you have, in the order they appear

Every record in this table is in this packet. "Complete" means the whole file,
reproduced unedited. "Excerpt" means part of a file, with the source named, the
full length given and the omission stated where the excerpt appears.

| # | record | complete or excerpt | source file |
|---|---|---|---|
| 1 | the closure rule this text is being reviewed under | excerpt | `docs/outside-review-protocol.md` |
| 2 | the brief - fixed protocol text, sent unchanged to every reviewer | complete, and fixed by the protocol | `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-tier2-packet.md` |
| 3 | THE TEXT UNDER REVIEW - the Amendment A3 closure text, version 4 | complete | `docs/a3-closure-text-draft-2026-09-21-v4.md` |
| 4 | the inside reviewer's findings on the previous version of that text | complete | `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-claude-worktree.md` |
| 5 | the registered amendment this block will be appended to | complete | `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` |
| 6 | the registration the amendment belongs to, including the loss conditions | complete | `experiments/06-mvm-0a-constructed-self-index/pre-registration.md` |
| 7 | the three-seed endpoint scores | complete | `experiments/06-mvm-0a-constructed-self-index/seeds-endpoint-findings.md` |
| 8 | the ownership-blind ceiling measured at 1.0 | complete | `experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md` |
| 9 | the registered defect in that ceiling | complete | `experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md` |
| 10 | the control-learnability pilot reading of 0.3125 | complete | `experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot-findings.md` |
| 11 | the fitted eleven-position sweep | complete | `experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings.md` |
| 12 | the correction note carrying the one-legible-episode-in-eleven figure | complete | `experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings-CORRECTION-2026-09-20.md` |
| 13 | the standardised refit of that read | complete | `experiments/06-mvm-0a-constructed-self-index/standardised-refit-findings.md` |
| 14 | the other-agent control's probe half | complete | `experiments/06-mvm-0a-constructed-self-index/other-index-position-sweep-findings.md` |
| 15 | the difference-of-averages read of the marker word | complete | `experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-findings.md` |
| 16 | the ruling that a load-bearing self-index is a centre | complete | `docs/rulings/2026-09-20-center-as-degree.md` |
| 17 | the ruling carrying the successor experiment's plan | complete | `docs/rulings/2026-09-20-december-result-roadmap.md` |
| 18 | the ruling reconciling the blind arm | complete | `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md` |
| 19 | the successor experiment's design note | complete | `docs/competing-mechanisms-2026-09-20.md` |
| 20 | the red team ledger - every row and range the text under review cites | excerpt | `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md` |
| 21 | the independent review of a later draft clause - the finding the text cites | excerpt | `experiments/06-mvm-0a-constructed-self-index/red-team-a4.md` |
| 22 | the compute ledger - its rules, its baseline, the rows the text cites and the rows that correct them | excerpt | `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md` |
| 23 | OPTIONAL BACKGROUND, not cited by the text under review - what the separation clause requires | complete | `experiments/06-mvm-0a-constructed-self-index/separation-clause-requirements.md` |


---

===== RECORD 1 of 23 - the closure rule this text is being reviewed under - EXCERPT: docs/outside-review-protocol.md =====

*Source note: excerpted from `docs/outside-review-protocol.md` (46,763
characters in full), which also sets out the three review gates, the two tiers
and the measurement rehearsal. Only the closure rule is reproduced, because it
is the only part of that file the text under review cites.*

*Quoted from `docs/outside-review-protocol.md` as amended 2026-09-21. It is the
standard part 1 of the brief applies.*

> Before a registration commit at Gate A:
>
> - Every fatal finding from either tier has a closure line in the ledger, in
>   the form: finding, the commit that lands the fix, and a MEASURED check by a
>   session other than the one that wrote the fix, showing the fix does what
>   the closure says. "Adopted" is a disposition, not a closure.
> - **That check belongs to the reviewer, not to the author.** The tier 1
>   reviewer of the Gate A pass owns it and runs it: reproduce the denominator,
>   build the competing solver, re-run the intervention, recompute the number —
>   whichever single measurement would come out wrong if the fix were wrong.
>   Reading the fix and finding it convincing is not the check. What the
>   reviewer produces is a MEASURED finding in the filed review: the command
>   run, the output it gave, and a plain sentence saying whether that output
>   matches what the closure claims. If the reviewer cannot run the check, the
>   reason goes on the record and the finding stays open.
> - **The ledger says which of the two happened.** A fatal item's ruling line
>   states either that the argument was accepted or that the claim was checked,
>   and, when it was checked, names the reviewer and the check. Agreement and
>   verification are not the same thing, and the record should not let them read
>   as if they were.
> - Every sentence in the registered text that says verified, measured,
>   calibrated, or attacked cites the committed record by file name, and the
>   closure check confirms the record contains what the sentence says it does.
> - Serious findings are closed the same way or carried as an open item named
>   in the registered text, with John's ruling and reason.
> - A declined finding keeps its reason on the record so the next pass can see
>   it was considered.

===== END OF RECORD 1 =====

===== RECORD 2 of 23 - the brief - fixed protocol text, sent unchanged to every reviewer - PROTOCOL TEXT, CARRIED UNCHANGED, from: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-tier2-packet.md =====

*Source note: the four-part brief as it goes to every reviewer. Its wording is
fixed by `docs/outside-review-protocol.md` and it is carried here from the
packet file that already held it, unchanged. It is not rewritten for either
reviewer, and not rewritten between passes.*

You are reviewing the closure text of a pre-registered experiment. The
experiment, Amendment A3 of a program called Minimum Viable Mind, trained
a small transformer (about 30 million parameters) on a constructed
multi-agent task and pre-registered a test of whether the model's behaviour
depends on an "ownership" input, a signal telling it which of four agents'
revisions are its own. The text you are reviewing is the block that will
be appended to the registration to close the experiment. It says the
experiment's outcome is *not testable*, in the sense the registration
defined for that phrase before the experiment ran, and it says what was and
was not measured. Once appended, the text is registered and cannot be
edited, so the review happens now.

Your job is critique, not agreement. Answer in four parts, in this order,
with a table at the top of each part, marking every finding fatal,
serious, or worth-noting, and say for each whether you measured it (you
checked a number or a quotation against the documents shown) or argued it
(reasoning a reader can dispute). Plain language throughout; a reader
outside the field should follow every sentence.

Part 1, feasibility. For every number and every claim that something was
measured, verified, run, or never run: does the record shown to you
contain it? Is "not testable" the registered word for the loss condition
the text says fired? Quote the registration.

Part 2, satisfied by the wrong thing. Every way this block could close the
experiment while leaving something the registration requires undone or
misnamed: a registered control described as run when only part of it
ran; a result placed in the wrong registered bin; a sentence that reads as
a finding of absence when the registration reads the same pattern as
instrument failure; a claim handed to a future paper that the registered
text withholds.

Part 3, no verdict. Every way the block could be registered and still
leave the future paper unable to say what the experiment supports, or the
successor experiment unable to inherit what it needs.

Part 4, over-reading. What each paragraph will be read as claiming by a
reader who has not followed the program, in a paper and in public. If a
sentence should be rewritten, write the sentence.

The tier 1 review you have been shown found six fatal problems in the
previous version and this version answers them; you may agree, disagree,
or find that an answer created a new problem. You may look things up; if
you do, say where, so facts from lookup can be told from your judgment.
Do not soften findings to be polite, and do not manufacture severity to
look thorough. A pass that finds nothing fatal is a valid result, reported
as what was checked and what held. End with a one-paragraph statement of
the strongest case for not registering this text as written.

===== END OF RECORD 2 =====
