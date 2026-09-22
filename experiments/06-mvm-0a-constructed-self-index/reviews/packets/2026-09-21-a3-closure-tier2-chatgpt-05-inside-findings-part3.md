# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 5 of 20: The inside reviewer's findings, part 3 of 3

*This is file 5 of 20 of one review packet, pasted into a single conversation.
It contains the inside reviewer's findings on the previous version of that
text (part 3 of 3). Reply with one short line saying you have it, and wait for
the rest: the brief you are answering is in file 1, and your review comes only
after file 20 arrives. If this file looks cut short, say so now.*

---

===== RECORD 4 of 23, part 3 of 3 - the inside reviewer's findings on the previous version of that text - COMPLETE FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-claude-worktree.md =====

*This part is its parts 3 and 4, no verdict and over-reading, and its kill
case. The other parts of this record are in file 03 and file 04.*

# Part 3 — No verdict

*Every way the block could be registered and still leave the paper unable to
say what Amendment A3 supports, or the successor unable to inherit what it
needs.*

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-161 | The registered reading of this null is instrument failure, and the block does not say so | **fatal** | MEASURED |
| RT-162 | The registered blind-localization arm appears nowhere, including the ordering John ruled the same day | serious | MEASURED |
| RT-163 | The ceiling precondition is not handed to the successor | serious | MEASURED |
| RT-164 | The block does not say whether the registered hard kill K5 fired | serious | MEASURED |
| RT-165 | The deferred marker-word read is not carried as an open item | serious | MEASURED |
| RT-166 | No registered bin is named, and the closest fit is not addressed | worth-noting | MEASURED |

### RT-161 — the registered reading is instrument failure, and the block substitutes an inference pointing the other way — **fatal**, MEASURED

This is the most consequential omission in the block.

What the block says: *"This is a status, not a finding of absence: these
probes did not localize this target at these positions, and strong, readily
recoverable versions of it are less plausible than before; other
implementations and instrument limits remain open."*

What the registered text says, as three accepted rulings put it:

- RT-50: *"The registration reads 'known load-bearing, instruments cannot
  find it' as **instrument failure**; the interpretation reads the same
  pattern as absence without saying so. … Under the registered text it is
  instrument failure until patching has run."*
- RT-102: *"a null against a centre known to be load-bearing is registered as
  instrument failure, not absence."*
- RT-92, repeating both deliberately, *"because it is the clause most likely
  to be dropped when the paragraph is shortened."*

The paragraph has been shortened and the clause has been dropped. "Instrument
limits remain open" is in the sentence, and it is not the same thing: it lists
instrument failure as one of several open possibilities, where the registered
text makes it the standing reading until causal patching runs.

Worse, the sentence that replaces it points the other way. "Strong, readily
recoverable versions of it are less plausible than before" is an inference
from the nulls toward absence, and its warrant is that these instruments would
have found the thing if it were there. The ruling of 2026-09-21 that ordered
the blind arm first (RT-141) says exactly what that warrant needs and that it
does not exist: *"every number in both runs is conditional on this stack
recovering a center known by construction to be there, **which has never been
established on this design**, and the registration states that if it cannot,
the null was instrument failure."*

So the block draws the one inference the registered text forbids drawing
until a measurement that has never been made on this design is made, and
omits the reading the registered text mandates in its place. The paper,
reading only this block, cannot say what Amendment A3 supports about
localization, because the block has given it the opposite of the registered
answer.

**Closure:** put the registered reading in the block, in its own clause, and
either drop "less plausible than before" or attach the condition it depends
on. My version 3 does the former and keeps a weaker, defensible sentence.

### RT-162 — the registered blind-localization arm appears nowhere — serious, MEASURED

The block never mentions the blind-localization arm. Three reasons that is a
gap the successor cannot fill for itself:

1. **It is the measurement that makes every localization number in the block
   readable.** RT-141, quoted above, and `separation-clause-requirements.md`
   Part 3 item 1, which requires before any clause is read on a localized
   lesion *"a positive control the stack recovers, **on this design**, not a
   synthetic one"*.
2. **John ruled its ordering on 2026-09-21**, as one of the three decisions
   at the head of that ledger block: *"The registered blind-localization arm
   runs before any further work on that position."* Registered text that does
   not carry a ruled ordering will not deliver it to whoever reads the
   amendment next.
3. **Its status is formally unreconciled** in the last committed ruling on it
   ("No run until reconciled"), and the reconciliation lives in a file this
   review may not open (RT-152).

The earlier Gate C review already made this finding against the step 4
proposal (RT-99), and its accepted closure was *"the step 4 text says where
step 3 stands"*. The closure block is the registered descendant of that text
and it says nothing.

### RT-163 — the ceiling precondition is not handed to the successor — serious, MEASURED

The brief names this as one of three things the successor must inherit. It is
not in the block.

The precondition is John's, recorded in the registered defect note of
2026-09-17: *"**If A4 opens, measuring the control's ceiling properly is a
precondition of the amendment** (John, 2026-09-17). An amendment built on an
unverified denominator would inherit this defect."* The ledger carried it
twice (RT-69, and RT-115 which credits the step 4 proposal for carrying it,
while noting the staleness that only a new grammar's control turn would need
measuring again).

The successor the block schedules is exactly that case: a new design with new
contrast cases, registering on 2026-10-11. The block hands it the successor's
purpose and its date and not the one precondition John attached to any
successor amendment. One sentence.

### RT-164 — the block does not say whether the registered hard kill fired — serious, MEASURED

The amendment registers seven hard kill criteria, each of which *"halts spend
and sends the finding to John"*. The fifth reads:

> **K5.** Probe-patching convergence fails on all three seeds: *not testable
> (localization)*, reported as such; no further seeds.

Causal patching has never run, so the convergence requirement of §3.2 item 4
cannot be met on any seed, and the block adopts K5's exact consequence — the
term *not testable (localization)* — without ever saying that K5 fired, or
that it did not, or which.

This is not pedantry about a label. A hard kill firing is a registered event
with consequences attached ("no further seeds"), and a closure block that
adopts a kill criterion's outcome while leaving the criterion unnamed makes
the amendment's own kill list unauditable. Either K5 fired and the block
should record it, or the convergence requirement was never reached in a way
that triggers K5 and the block should say why the same term applies anyway.

Relatedly, the two-instrument requirement — probe **and** patching, §3.2 item
4 — appears in the block only as an explanation of why patching's absence
matters for A3. It is not stated as the standing requirement the successor
inherits, which is the second of the three things the brief asks about.

### RT-165 — the deferred marker-word read is not carried as an open item — serious, MEASURED

The block correctly makes the narrow statement: the registered probe target
has been read only by the weaker method. What it does not say is that the
wider statement is one run away.

The record is emphatic and repeated. The ledger's ruling on this (RT-89,
fatal to a sentence) says the registered target has only ever been read by
the difference-of-averages read. The step 4 review (RT-112) draws the
consequence for closure: it *"can only make the narrower sentence until it
runs"*. And the outside reviewer's fifth question is carried open **for
John**: *"the marker-word read is the only sensitive-instrument test of the
registered probe target, and closure can only make the narrower sentence
until it runs … $0 compute."* The price is about seventy processor-hours,
stated three times in the records.

The protocol's closure rule is explicit about this case: *"Serious findings
are closed the same way or **carried as an open item named in the registered
text**, with John's ruling and reason."* This is a serious finding carried
open in the ledger and not named in the registered text. Without it, a reader
of `amendment-a3.md` cannot tell whether the linear-read line is parked one
cheap run short of its registered target or finished.

### RT-166 — no registered bin is named, and the closest fit is not addressed — worth-noting, MEASURED

The amendment registers six pre-stated signatures — H_self-location (the
registered prediction), H_self-reference-only, H_generic-binding, H_tag, and
H_diffuse (present but uncarvable), plus the inherited bins. The block names
none of them and does not say which, if any, A3 landed in.

The one that reads closest to what happened is H_diffuse, registered as:
*"L0 collapses T_act (ownership is load-bearing) but no L1 subspace at k ≤ 16
beats the L2 controls, and probe-patching convergence fails."* The first
conjunct happened, the third happened. The second did not, in the strict
sense — no subspace was ever localized, so none was compared against the
matched controls at any rank. That is a real reason H_diffuse did not fire and
it is the kind of reason a closure block should give, because the registered
signature and the actual outcome are one missing run apart.

Also in this category and easily fixed: the block's heading still reads
"Closure of Amendment A3, **[date of Gate A pass]**". Fine in a draft; the
registration commit cannot carry a placeholder, and the closure rule's commit
line should name the commit that fills it.

---

# Part 4 — Over-reading

*What each sentence will be read as claiming, in the paper and in public.*

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-167 | "Outcome: not testable" will be read as "Amendment A3 found nothing" | serious | ARGUED |
| RT-168 | The public sentence drops "for the primary battery" | serious | ARGUED |
| RT-169 | "Strong, readily recoverable versions" is unquantified, and its only number is one the record calls heuristic | serious | ARGUED |
| RT-170 | Bare identifiers in registered text, against the workspace rule and a ruling already made | worth-noting | ARGUED |
| RT-171 | The refusals are drafted in the form that survives quotation | worth-noting (credit) | ARGUED |

### RT-167 — "Outcome: not testable" will be read as "A3 found nothing" — serious, ARGUED

The outcome line is the first thing anyone reads and, for most readers, the
only thing. It is the registered word and John ruled it, so it stays. But
sitting alone at the top, it says the experiment did not work — and the
strongest result the programme has produced sits three lines below it: an
input dependence measured on three seeds trained from scratch, replicating to
within 0.011 on the intact score and collapsing by seven to nine times the
locked threshold under the lesion.

The reading that follows is "they ran it and got nothing", which is wrong in
a way that will be hard to correct later, because a summary table carries the
outcome word and not the paragraph. The fix is not to soften the word. It is
to let the outcome line carry both halves — what fired, and what was measured
anyway — so that the sentence a reader lifts contains the result. My version 3
does that in one added clause.

### RT-168 — the public sentence drops "for the primary battery" — serious, ARGUED

The block's body says, correctly, *"The ownership input is load-bearing for
the primary battery."* Its public sentence says *"the ownership input is
load-bearing on three seeds"*.

The center-as-degree ruling words it the same way the public sentence does, so
this is not a deviation from a ruling, and I am not calling it one. It is a
finding about what happens when the sentence travels. The ruling's wording was
written to sit next to the block's body; the public sentence is designed to be
quoted alone. Quoted alone, "the ownership input is load-bearing" reads as a
claim about the model's behaviour in general, when what was measured is one
battery of four — the other three being the control battery (which never
learned), the state battery (which moved on one seed, inside its threshold)
and the syntax battery (which did not move at all).

The step 4 ruling's own wording of what A3 supports includes the qualifier:
*"the ownership input is load-bearing **for the primary battery** on three
seeds and the matched contrast could not be run."* Four words, and the
sentence survives being quoted.

### RT-169 — the only inference in the block is unquantified, and its number is one the record calls heuristic — serious, ARGUED

*"Strong, readily recoverable versions of it are less plausible than before"*
is the block's single inferential claim, and it carries no number. A reader
cannot tell whether "strong" means a signal in one episode in three or one in
fifty.

The record has a figure and it has a warning attached. The correction note of
2026-09-20 recalibrates the sweeps' reach: not one episode in twenty-seven,
which assumed a perfect score this read never reaches, but **about one episode
in eleven**, measured against the instrument's own ceiling, and the same
figure holds for all three fitted runs. And the outside review's eleventh
finding, accepted, says that figure *"is not measured detection power"* and
that existing figures are to be annotated as heuristic.

So the block's one inference rests on a number it does not give, which the
record says is heuristic, and which — at one episode in eleven — is a good
deal less impressive than "strong … less plausible" implies. Either give the
figure with its caveat, or drop the word "strong" and claim only what a
heuristic bound supports. Combined with RT-161, which says this sentence is
in the wrong direction to begin with, my version 3 replaces it.

### RT-170 — bare identifiers in registered text — worth-noting, ARGUED

The workspace rule is that no identifier appears without a plain phrase
saying what it is, because John has said he cannot hold identifiers in his
head and should not be asked to. The block carries several bare: "§3.1",
"§3.2", "§L2(a)", "ledger RT-120 to RT-142", and in the preamble "RT-58 and
RT-59" and "PR 10".

This has already been ruled once, on the step 4 proposal (RT-116), where the
finding was that John was *"asked to rule that three things happen and is not
told what any of them is"*. Registered text is the place this matters most,
because it is the text that outlives the session that wrote it. Each of these
takes four or five words: "the section on what is ablated (§3.1)", "the
matched other-agent control (§L2(a))", "the Gate B rulings of 2026-09-21 on
the two follow-up runs (ledger RT-120 to RT-142)".

### RT-171 — the refusals are drafted in the form that survives quotation — worth-noting (credit), ARGUED

Worth recording because it is the hardest part of this block to get right and
it is right. The two claim phrases the registration withholds are not simply
left out; they are named and refused inside the registered text: *"No result
of A3 is described as 'a structural signature of self-indexing' or 'a
structural signature of ownership-specific learning'."*

An omission can be undone by a later writer who does not know it was
deliberate. A refusal that names what it refuses cannot. Given that the
programme's recorded failure mode is a caveat drifting to nothing across
successive documents, this sentence is the single best-designed thing in the
block, and it should be the template for the other limits the block currently
only implies.

---

## The closure block as it should be registered

Written out in full as **version 3**, filed beside version 2 at
`docs/a3-closure-text-draft-2026-09-21-v3.md`, citing this review. It changes
nothing John has ruled: the outcome word stays, the gradient position stays,
the successor stays, the refusals stay. What it changes is what the block
cites, what it says about the other-agent control, which sense of "center" it
means where, and whether the registered instrument-failure reading is in the
text. The successor paragraph is left with a marked gap where the
December-result ruling is cited, because that ruling is not in the record and
I will not write a citation to a file I cannot check (RT-145).

---

## Kill case

Amendment A3 should close, it should close as *not testable*, and this block
is close to the text that should do it — but it must not be committed as
version 2. The case against committing is not that any number is wrong;
every one reproduces, and the block takes the corrected figure over the
flattering one without being asked. It is that a registration commit is
governed by a closure rule requiring each claim to point at a committed record
a second reader can check, and this block states nine measured numbers with no
file behind them, says "never run" with no record, and rests its successor
schedule on a ruling that is not in the repository at all — so the first
document to face the rule the programme wrote after registering an
unsatisfiable clause would be committed in breach of it. Underneath the
citations, two substantive things would go into the registered record wrong:
the block tells the paper that the registered matched control has run when
only its probe half ran and the control itself remains unavailable, and it
drops the registration's own reading of its central null — instrument failure
until causal patching runs — replacing it with an inference toward absence
whose warrant the blind arm has never established on this design. Both are
failures in the same direction, toward a tidier result than the record
supports, and both land in the one paragraph the paper will quote, where the
word "center" is used in two incompatible senses two paragraphs apart. None
of this is expensive to fix: five citations, four sentences rewritten, one
ruling committed. The version 3 filed beside this review does all of it
without touching a single thing John has ruled, and the six fatal findings
each close with a commit and a check by a session other than the one that
writes the fix.

---

*Filed by the tier 1 reviewer. Findings RT-143 to RT-171, continuing from
RT-142 on `main`. Drafted rulings are in `red_team_ledger.md` and are the
reviewer's; none is ruled. Nothing is appended to `amendment-a3.md` by this
review.*

===== END OF RECORD 4, part 3 =====
