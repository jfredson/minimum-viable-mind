# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 3 of 22: The inside reviewer's findings, part 1 of 3

*This is file 3 of 22 of one review packet, pasted into a single conversation.
It contains the inside reviewer's findings on the previous version of that
text (part 1 of 3). Reply with one short line saying you have it, and wait for
the rest: the brief you are answering is in file 1, and your review comes only
after file 22 arrives. If this file looks cut short, say so now.*

---

===== RECORD 4 of 23, part 1 of 3 - the inside reviewer's findings on the previous version of that text - COMPLETE FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-claude-worktree.md =====

*This part is its opening and part 1, feasibility. The other parts of this
record are in file 04 and file 05.*

# Gate A, tier 1 — the Amendment A3 closure text, version 2

*Filed 2026-09-21 (Pacific) by a fresh Claude Code session in its own
worktree (`worktree-a3-closure-tier1-review`), reading at commit `49fb59c`
on `main`, under `docs/outside-review-protocol.md` and the packet
`reviews/2026-09-21-a3-closure-packet.md`. Filed verbatim and not edited
after filing.*

*Ledger numbering: the last red-team number on the main line at the time of
filing was **RT-142** (the last row of the Gate B review of the two
follow-up localization runs, ruled 2026-09-21). This review runs **RT-143
to RT-171**.*

*Lookup: none used. No web search, no external reference. Every finding
below is checked against files in this repository at the commit named
above.*

---

## What was opened, and what was not

**Opened, all at commit `49fb59c` (the committed version, never the
working copy):**

In `experiments/06-mvm-0a-constructed-self-index/`: the amendment itself
(`amendment-a3.md`), the original pre-registration (`pre-registration.md`),
the two ceiling documents (`ceiling-measurement-findings.md`,
`ceiling-defect-2026-09-17.md`), the three-seed endpoint record
(`seeds-endpoint-findings.md`), the first pilot's record
(`gate2-pilot-findings.md`), the control-battery pilot's pre-statement and
its result (`control-learnability-pilot.md`,
`control-learnability-pilot-findings.md`), the requirements document for a
separation clause (`separation-clause-requirements.md`), the four
localization sweeps and the correction note
(`fitted-position-sweep-findings.md`,
`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`,
`other-index-position-sweep-findings.md`, `standardised-refit-findings.md`,
`powered-position-sweep-findings.md`), the red-team ledger
(`red_team_ledger.md`) from the block beginning at RT-33 to the end, and the
compute ledger (`compute-ledger.md`), running totals only.

In `docs/`: the target (`a3-closure-text-draft-2026-09-21-v2.md`), the
earlier draft it supersedes (`a3-closure-text-draft-2026-09-20.md`), the
control-battery proposal (`step4-control-battery-proposal-2026-09-20-v2.md`),
the ruling that a load-bearing self-index is a center
(`rulings/2026-09-20-center-as-degree.md`), the competing-mechanisms page
(`competing-mechanisms-2026-09-20.md`), and the review protocol
(`outside-review-protocol.md`).

**Not opened, deliberately:** `STATUS.md`; every chat transcript; every
uncommitted file.

**Two departures from the packet's file list, both forced, both reported
here rather than worked around.**

*First, the packet grants the December-result ruling
(`docs/rulings/2026-09-20-december-result-roadmap.md`) and it is not in the
repository's history — it exists only as an untracked file in the shared
checkout.* The packet also says "do not open any uncommitted file", and the
protocol makes that mandatory rather than advisory: tier 1's isolation rule
is "no uncommitted files from the shared checkout", and the protocol calls
context isolation "the non-negotiable part". I did not open it. The cost is
that I cannot check the closure block's successor paragraph against the
ruling it cites; the benefit is that the check I *can* make is the one that
matters, which is that a registration commit would cite a file no second
reader can find. That is finding RT-145. The same applies to the eight
uncommitted lines sitting on top of the center-as-degree ruling in the
shared checkout; I read that ruling as committed and ignored the working
copy.

*Second, the packet says version 1 sits beside the target "for the diff
only", and no file named version 1 exists.* The target's own opening
paragraph names its predecessor as `a3-closure-text-draft-2026-09-20.md`,
which is committed, so I treated that as version 1 and diffed against it.
Recorded so the tier 2 packet can name the file rather than the version.

**One thing the packet asked me to check that I cannot check.** The
preamble rests one of its three preconditions — the blind-arm
reconciliation — on `STATUS.md`, which the same packet forbids me to open.
That is finding RT-152.

---

## Summary in one line

Every number in the block reproduces, the outcome word is the registered
one and John has ruled that it fired, and the block honours the hardest
rulings aimed at it — and it is not registerable as written, because it
uses the word "center" in two incompatible senses in adjacent paragraphs,
describes a registered control as having run when only half of it ran, drops
the registered reading of its own central null, cites a file that is not in
the record, and states nine measured numbers without naming the file they
come from.

**Six fatal findings.** Naming the file the three-seed numbers come from
(RT-143); naming the record behind "never run" (RT-144); the successor
paragraph's citation of a file that is not committed (RT-145); the two
senses of "center" (RT-153); the other-agent control described as the
registered control having run (RT-155); and the omission of the registered
instrument-failure reading (RT-161).

---

# Part 1 — Feasibility

*Every number and every "measured", "verified" or "ran" claim in the block,
against the committed record.*

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-143 | The "What A3 measured" paragraph states nine measured numbers and names no file | **fatal** | MEASURED |
| RT-144 | "Never run and has no code" names no record, and the closure rule lists "never run" by name | **fatal** | MEASURED |
| RT-145 | The successor paragraph cites a ruling that is not in the repository, to override a committed ruling that says the opposite | **fatal** | MEASURED |
| RT-146 | Five committed findings files stand behind the localization sentences and none is named | serious | MEASURED |
| RT-147 | The programme's money figure is right by arithmetic and is not in the ledger it cites | serious | MEASURED |
| RT-148 | Everything else reproduces, including the block's choice of the honest number over the flattering one | worth-noting (credit) | MEASURED |
| RT-149 | "Not testable" is the registered word for the loss condition that fired, and the loss condition is quoted correctly | worth-noting (credit) | MEASURED |
| RT-150 | There are two registered senses of "not testable" and the block does not say which it means | serious | MEASURED |
| RT-151 | The packet's reading of the rehearsal rule is right about this block and wrong about what this block schedules | worth-noting | ARGUED |
| RT-152 | One of the three preconditions rests on a file this reviewer is forbidden to open | serious | MEASURED |

### RT-143 — the three-seed numbers have a record and the block does not name it — **fatal**, MEASURED

The paragraph headed "**What A3 measured**" states nine numbers: three
intact scores (0.5683, 0.5633, 0.5738), three lesioned scores (0.1988,
0.2015, 0.1447), the state battery's movement on one seed (0.0769), that
battery's locked threshold (0.1172), and that the syntax battery did not
move. It names no file.

All nine reproduce exactly against the three-seed endpoint record
(`seeds-endpoint-findings.md`), which I checked line by line. That is not
the problem. The problem is the closure rule, which the packet states and
the protocol states in the same words: *"Every sentence in the registered
text that says verified, measured, calibrated, or attacked cites the
committed record by file name."* This paragraph's own heading is the word
"measured", and the file is absent. The protocol's part 1 is explicit that
this is fatal on its own: *"A 'verified' or 'measured' claim in the text
with no record behind it is a fatal finding."*

This is also the exact failure the protocol was written to stop. Its own
account of what went wrong says the registered text of the amendment
claimed both ceilings were "verified by the attack sweep" when only one had
been, and concludes: *"Had this rule been in force on 2026-09-15, RT-21's
closure check would have gone looking for the control battery's attack
record and found none."* A closure block that states nine measured numbers
without naming their record is that rule not being in force on the first
document it applies to.

**Closure:** add `seeds-endpoint-findings.md` to that paragraph. One
citation, nine numbers.

### RT-144 — "never run and has no code" names no record — **fatal**, MEASURED

The block says: *"causal patching, which §3.2 requires alongside the probe,
was never run and has no code for this design."*

The claim is true. The ledger's ruling on it (RT-96, the finding that
patching is not free, local and already built) says the experiment's source
folder holds no patching script and the only patching code in the
repository is Experiment 1's, written for a different model, vocabulary and
grammar. That ruling was accepted as fatal on 2026-09-20.

The packet's closure rule names this case specifically: *"Every 'verified',
'measured', 'ran' or 'never run' in the registered block cites the
committed record by file name."* This is a "never run" with no file. It is
also the single sentence in the block that a hostile reader is most likely
to test, because it is the sentence that explains why the localization line
has no verdict.

**Closure:** cite the ledger row by name and in words — the ruling of
2026-09-20 that patching is new code for this design, not existing
machinery (ledger RT-96).

### RT-145 — the successor paragraph cites a file that is not in the record, and it overrides a committed ruling — **fatal**, MEASURED

The block says the successor *"registers in 2026, through Gate A with both
tiers, registration commit target 2026-10-11
(`docs/rulings/2026-09-20-december-result-roadmap.md`, which amends item 5
of the center-as-degree ruling)."*

Two checks, both run:

1. `docs/rulings/2026-09-20-december-result-roadmap.md` does not exist at
   any commit in this repository's history. It is an untracked file in the
   shared checkout.
2. The ruling it claims to amend is committed and says the opposite. Item 5
   of the center-as-degree ruling reads: the successor is *"registered
   **after the hibernation condition** and through Gate A with both
   tiers."*

So the registered block would land in `amendment-a3.md` asserting a
schedule that the record contradicts, on the authority of a file the record
does not contain. Under the closure rule this cannot be checked by a second
reader, which is the whole point of the rule. Under part 1 of the brief it
is a claim with no record behind it.

I want to be fair about what this is and is not. I have no reason to doubt
that John ruled the December-result roadmap, and the packet's own header
says he did, on 2026-09-20, and lists three protocol amendments from it. The
finding is not that the ruling is fictitious. It is that a registration
commit is the one kind of commit that may not rest on an uncommitted file,
and this one does — twice, because the packet's governing amendments come
from the same place.

**Closure:** commit the December-result ruling before the registration
commit, and have a session other than the one that wrote it check that its
item on the successor's date says what this sentence says. Until it is
committed, neither this block nor the tier 2 packet can be checked against
it.

### RT-146 — five committed findings files stand behind the localization sentences and none is named — serious, MEASURED

The paragraph headed "**What A3 did not measure**" makes five factual
claims about runs. Its only citations are two section numbers from the
registered text and one ledger range. The five committed records it does
not name:

| the claim in the block | the record it comes from |
|---|---|
| "a fitted linear classifier at eleven positions and five layers found the register index nowhere except where its marker is the input" | `fitted-position-sweep-findings.md` |
| "a standardised refit of the same read agreed" | `standardised-refit-findings.md` |
| "the registered matched control … ran once and excluded the one proposed confound" | `other-index-position-sweep-findings.md` |
| "the marker word has been read only by the weaker difference-of-averages method at those positions" | `powered-position-sweep-findings.md` |
| the sensitivity behind "strong, readily recoverable versions … less plausible" | `fitted-position-sweep-findings-CORRECTION-2026-09-20.md` |

The ledger range that is cited (the Gate B rulings of 2026-09-21, RT-120 to
RT-142) covers two of these four runs and none of the correction note. This
is not fatal in the way RT-143 is, because "found", "ran" and "read" are
the softer verbs and the ledger range does point somewhere real. It is
serious because the localization paragraph is the part of the block the
successor and the paper will lean on hardest, and it is the part with the
least of its record attached.

### RT-147 — the programme's money is right and is not in the ledger it cites — serious, MEASURED

The block says: *"Amendment A3 closed at about $44 of its $100 hard stop;
the programme at about $226 of its $400 ceiling (`compute-ledger.md`)."*

The first figure is in the ledger, stated: the last row carries *"A3
cumulative ~$44.2 / $100"*. Correct, cited, checkable.

The second is not in the ledger. The string "226" does not appear in the
file. The last programme running total the ledger states is **~$215.7 /
$400**, in the correction attached to the three-seed row. The block's figure
is right — $215.7 plus the control pilot's $9.9 plus the $0.067 checkpoint
recovery is about $225.7 — but a reader has to do that sum across two rows
that omit the programme total to get there.

That omission is itself on the record as a known failure mode. The ledger's
own correction note, written on 2026-09-17, says: *"Two consecutive rows
without a running total is how a cap stops being watched; the second was
mine."* The two most recent rows — the control pilot and the checkpoint
recovery — again carry only the Amendment A3 figure and not the programme
one. So the thing that note warned about has recurred, and the closure block
is the first document to have to paper over it.

**Closure:** put the programme running total back on the two rows that lack
it, so that `compute-ledger.md` contains the figure the closure block says
it contains.

### RT-148 — everything else reproduces, and the block chose the honest number — worth-noting (credit), MEASURED

Checked and correct, each against the record named:

- The control battery's ownership-blind ceiling of 1.0, dated 2026-09-17,
  and the consequence that a defined drop would need a baseline of 1.10
  (`ceiling-measurement-findings.md`).
- That the clause therefore had no computable value "from the day it was
  registered" — the record says the same, in the same direction: *"The
  clause was unsatisfiable the day it was registered, months before any
  checkpoint existed."*
- The control pilot's 0.3125 against a pre-stated bar of 0.60. I checked
  that the 0.60 bar was genuinely pre-stated: it is in the pilot's
  pre-statement, committed before the code existed, as the "LEARNED"
  boundary. The block leans on 0.60 rather than on the 0.3227 boundary,
  which is the right choice and not the obvious one — the pilot's own
  findings warn that the 0.3227 reading is thin ("individual draws land on
  both sides of that boundary") while 0.60 is twelve standard deviations
  away. The block took the robust bar.
- "Two episodes in four thousand" for the one cell that crossed the family
  bar. The ledger's ruling puts it at 1.94 episodes in 4,000 (RT-128, the
  finding that the clearing cell's margin is inside its own estimation
  noise). Rounding 1.94 to two is fair.
- Eleven positions and five layers: correct for all three fitted sweeps.
- Amendment A3 at about $44 of $100.

One credit worth stating on its own. The block reports the primary
battery's intact score as **0.5683**, not the **0.506** that the first
pilot published. The first pilot's own record
(`gate2-pilot-findings.md`) carries a correction saying the published
figure came from a single lucky evaluation seed and *"flatters twice"*. The
block uses the six-seed figure. That is the corrected number being carried
into registered text without anyone having to ask, which is the behaviour
the protocol exists to produce.

### RT-149 — "not testable" is the registered word, and it is quoted correctly — worth-noting (credit), MEASURED

The brief asks me to check this against the pre-registration and quote it. I
did. The final loss condition in `pre-registration.md`, under the heading
"Loss conditions (what would retire or rebuild this experiment)", reads in
full:

> No non-self cross-turn control can be built that is state-requiring at
> ceiling — then the differential discriminator is dead here and the honest
> report is "not testable" [RT-05].

The block's first sentence is: *"The pre-registered loss condition fired: no
non-self cross-turn control can be built that is state-requiring at
ceiling."* That is the registered condition almost word for word, and "not
testable" is the registered consequence.

Its antecedent is also satisfied on the record rather than by assertion. The
2026-09-17 ceiling measurement does not merely report that this control
failed; it argues the general case — *"the ceiling-corrected metric and the
concept of an ownership-free control are incompatible by construction, not
by accident"* — which is the loss condition's "cannot be built" in its own
terms.

And it has been ruled. The step 4 ruling of 2026-09-20, item 3, says the
loss condition *"HAS FIRED; the registered word for the outcome is not
testable, and the closure text uses it."* The center-as-degree ruling of the
same day repeats it. So the outcome word is not this draft's choice; it is
John's, twice.

### RT-150 — two registered senses of "not testable", and the block does not say which — serious, MEASURED

There are two registered uses of the phrase and they mean different things.

**As a bin**, in the pre-registration's list of registered bins:
*"**Not-testable:** validity gates breached, as in Experiment 1."* The
amendment carries the same bin forward as *"Not-testable (OOD or
localization)"*.

**As a loss condition**, in the sentence quoted at RT-149, where it is the
honest report when the differential discriminator is dead.

The block's headline — "**Outcome: not testable.**" — is the loss-condition
sense, correctly, and John ruled it so. But the validity gates were *not*
breached, and the block does not say that. A reader who goes to the
registered bin list to find out what "not testable" means will land on
"validity gates breached" and conclude that something went wrong with the
instruments that did not go wrong. The block's own later use of the narrower
term for the localization line — *not testable (localization)* — is
qualified and unambiguous, which makes the unqualified headline read as the
bin.

This is a clause, not a rewrite. Something like: the outcome word is the
loss condition's, not the validity-gate bin's; the gates were clean.

### RT-151 — the rehearsal reading is right about this block and misses what this block schedules — worth-noting, ARGUED

The packet invites me to contest its reading that the measurement-rehearsal
requirement does not apply, because this closure block pre-states no
measurement. I mostly agree, and I contest one part.

Agreed: the block pre-states nothing. It reports finished work, assigns a
registered term, and records a limit. There is no measurement in it for a
rehearsal to rehearse.

Contested: the block is also the document that schedules a registration
whose entire purpose is a measurement that does not exist. Its successor
paragraph commits to a registration whose stated purpose is *"to develop and
validate the Stage 2 degree metric"*, and the competing-mechanisms page
already names a candidate for that metric. The rehearsal rule exists because,
in the accepted words of the outside review (Astra's eighth finding),
*"registration repeatedly preceded a demonstration that the full measurement
procedure existed"*. The successor is the clearest instance of that risk the
programme has ever scheduled. So the rehearsal requirement does not bind this
block, and this block is the natural and cheapest place to say that it binds
the thing this block schedules. One sentence in the successor paragraph.

### RT-152 — a precondition resting on a file the reviewer is forbidden to open — serious, MEASURED

The preamble lists three preconditions as met, and the third is *"the
blind-arm status reconciled (Astra A10, no re-run; STATUS.md 2026-09-21)"*.
The packet's instruction is "Do not open: STATUS.md". So the packet asserts
a precondition is met and forbids the reviewer to check it.

This matters more than a packet-assembly slip, because of what is being
reconciled. The center-as-degree ruling lists this among the things it does
**not** decide: *"Astra A10: whether the blind-localization arm (ran
2026-09-16, NOT FLAGGED) is discharged, which would void the first item of
the 2026-09-20 localization order, or whether a rerun with a new target was
meant. **No run until reconciled.**"* And on 2026-09-21 John ruled RT-141:
the blind arm *"runs before any further work on that position"*. Those two
have to be made to agree — if there is no re-run, then RT-141's ordering is
satisfied by the 2026-09-16 run or it is satisfiable by nothing — and the
document that reportedly makes them agree is the one I may not read.

Under the closure rule, a precondition whose record the reviewer cannot
reach is not closed. I am not saying it is wrong. I am saying nobody outside
the authoring session has checked it, which is the condition the closure rule
was written to end.

**Closure:** either put the reconciliation in a file the tier 2 packet can
carry, or state it in the closure block itself, where it is registered text
and checkable.

---


===== END OF RECORD 4, part 1 =====
