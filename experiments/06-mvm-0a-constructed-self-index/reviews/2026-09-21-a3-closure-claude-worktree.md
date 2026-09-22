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

# Part 2 — Satisfied by the wrong thing

*Every way this block could close Amendment A3 while leaving something the
registration requires undone or misnamed.*

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-153 | The block uses "center" in two incompatible senses, two paragraphs apart | **fatal** | ARGUED |
| RT-154 | The registration's own concession that the wire lesion cannot separate a pointer from a carried binding is absent, and so is the discriminator it names | serious | MEASURED |
| RT-155 | The registered matched control is described as having run when only its probe half ran, against two rulings that say not to | **fatal** | MEASURED |
| RT-156 | The one cell that crossed the bar is described without naming its target, which a ruling requires | serious | MEASURED |
| RT-157 | "Excluded the one proposed confound" closes a question the ledger carries open | serious | MEASURED |
| RT-158 | "A standardised refit of the same read agreed" is wrong on all three counts | serious | MEASURED |
| RT-159 | A discriminator that ran is not named: the powered eleven-position sweep | serious | MEASURED |
| RT-160 | The rulings the block does honour, checked one by one | worth-noting (credit) | MEASURED |

### RT-153 — "center" means two different things in one registered block — **fatal**, ARGUED

Two paragraphs, two senses of one word.

In "**What A3 did not measure**": *"Whether the network built an internal
center around the ownership input is not testable with these instruments."*
Here a center is **an internal structure the network built**. That is
§3.1's sense, and §3.1 is cited in the next sentence: the lesion *"removes a
sense organ, not a structure the network built"*.

In "**Where this sits on the project's gradient**": *"a causally
load-bearing ownership pointer is a center at the bottom of the gradient.
These checkpoints have one."* Here a center is **anything the act depends
on causally**, with no requirement that the network built a structure. That
is the center-as-degree ruling's sense, where the removal test alone defines
a center and the corpus *"no longer owes an observable that separates
address from marking as kinds"*.

Each sentence is defensible on its own and each has a ruling behind it.
Together, in one registered block, they say the checkpoints have a center
and that whether they have a center is not testable. A reader is not being
careless when they notice that; the block does not give them the two senses.

Why fatal rather than serious. This is registered text, and it is the exact
sentence the paper will quote, because it is the only sentence in the block
that says what the models *have* rather than what could not be measured. Part
2 of the brief asks for "a sentence that hands the paper a claim the
registered text withholds", and names the ledger's two rulings on claim scope
(RT-113, the finding that "a structural signature of ownership-specific
learning" is the claim the registration withholds, and RT-119, the finding
that the original claim scope was unearned). The block is careful to refuse
both forbidden phrases by name. Then "These checkpoints have one" delivers
the substance of the thing the phrases were forbidden for — an internal
possession — three sentences later, and the registered text's own words
against it are quoted two paragraphs earlier.

It is also worth saying that the ruling the sentence leans on does not
contain it. The center-as-degree ruling's item 4 dictates what the closure
text should say, and its wording is: *"the ownership input is load-bearing
on three seeds; whether the network built an internal center around it is
not testable with these instruments; its degree on the integration axis is
unmeasured because the metric does not yet exist."* No "these checkpoints
have one". Item 7's public sentence is conditional in form — *"a
30-million-parameter transformer **with** a causally load-bearing ownership
pointer sits above zero"* — and the draft converts the conditional into an
assertion about these three checkpoints.

**Closure:** name the two senses, or use only one. The version 3 I have
drafted in part 4 keeps the gradient paragraph and makes it conditional in
the ruling's own form, so the block says what the ruling says and no more.

### RT-154 — the registration's own concession about pointers is missing, and so is its named discriminator — serious, MEASURED

The block gives one limit on the input-channel lesion, §3.1's: it *"removes
a sense organ, not a structure the network built"*. The registration carries
a second, separate limit that the block does not give. Registration revision
8, "The central claim is narrowed", registered text:

> The acting channel marks positions, and attending back to marked positions
> is a **re-readable pointer rather than a carried binding**. Both routes
> need the channel, so **the wire lesion cannot separate them**. The
> mid-episode re-indexing probe, already registered for the tag bin, is the
> discriminator.

These are two different limits. The first says the lesion is not evidence of
an acquired structure. The second says that even granting a structure, the
lesion cannot tell a binding carried forward from a pointer re-read each
time — and names the registered instrument that could.

That instrument has never run. The ledger's ruling on the count of
discriminators (RT-114) says so: *"the mid-episode re-indexing probe has
never run … the count of registered discriminators bearing on the A3 claim
is zero."*

This matters for the block specifically, because the gradient paragraph
turns on the word "pointer", and revision 8 is the registered text saying
that this experiment cannot establish a pointer as against the alternative.
The block reaches for exactly the distinction the registration says it
cannot make, and does not carry the registration's warning or the unrun
instrument that would settle it.

### RT-155 — the registered matched control did not run; half of it did — **fatal**, MEASURED

The block says: *"the registered matched control (§L2(a), the other agent's
index) ran once and excluded the one proposed confound."*

Two rulings, both from the Gate B review of 2026-09-21, say that this is the
wrong description, and one of them says so in those words.

**The ledger's closing row (RT-142)**, on how the result may honestly be
written, says: *"One point that must not be elided: the other-agent run is
the first execution of the **probe** half of the registered other-index
control; Part 3 item 2 asks for the **lesion** half, a localized other-index
subspace whose ablation leaves the self-directed condition intact. The run
found no such subspace at any testable position, so there is nothing to
ablate and **that control remains unavailable**. Running the probe half does
not discharge the requirement."*

I checked the requirement it points at. `separation-clause-requirements.md`,
Part 3, item 2, lists among the things a localized lesion still needs: *"the
other-index control, a subspace localized for a named non-self agent, matched
in rank and probe accuracy, **that does not hurt the self-directed
condition**"*. That is a lesion, not a probe. The registered definition in
the amendment's §3.1 agrees: L2 is a list of **matched controls** for the L1
**ablation**.

**The ledger's ruling on the match (RT-121)** adds the second half:
*"Record it as 'rank matched by design, accuracy matched as observed', not
as the registered control run to specification."* The block says "the
registered matched control … ran", which is the description that ruling
forbids.

So the sentence tells the paper that a registered control has been
discharged when the record says it remains unavailable, and tells the
successor that it inherits one fewer obligation than it does. That is part
2's question in its purest form — a registration closed while something it
requires is left undone and misnamed — and it is fatal for the same reason
RT-153 is: it is what a summary table will carry.

**Closure:** say the probe half ran. The phrasing the two rulings license is
in my version 3.

### RT-156 — the clearing cell is described without naming its target — serious, MEASURED

The block says: *"one cell of the refit crossed the family bar by two
episodes in four thousand and is recorded as a sub-bar pattern, not a
clearance."*

The phrase "a sub-bar pattern, not a clearance" is John's own ruled wording,
word for word, from the decisions at the head of the 2026-09-21 Gate B block
— so the block is right to use it, and the apparent tension between "crossed
the bar" and "sub-bar" is the ruling's, not the draft's. No finding there.

The finding is what the sentence leaves out, against a ruling that says not
to. The ledger's ruling on naming the target (RT-138): *"Any STATUS.md
sentence about the clearing cell **must name the target**, or it reads as the
registered target having been found."* The block's sentence names no target.
It also omits the position, the checkpoint and the layer. The record is
specific: the third checkpoint, the **other agent's** revision value, layer 3.

Two consequences, both bad in the same direction. A reader takes the cell to
be about the model's own identity, when the position is one that concerns the
other agent. And a reader takes the target to be the registered one, when it
is the register index — the very confusion RT-138 was written to prevent, and
which the ledger calls *"the mirror of this ledger's fatal ruling on the same
point"*.

Nine words fix it: name the target and the position.

### RT-157 — "excluded the one proposed confound" closes a question the ledger carries open — serious, MEASURED

The exclusion reading was tested and is not supported; the block is right
about that, and right to say the pattern was not explained away rather than
that it is "unexplained" (which the ledger's RT-139 ruled against). But the
ledger carries a second route open, and the block reads as though the
confound question is finished.

The ruling (RT-125), accepted and **carried open**: *"A purely relational
encoding — 'the value at this token belongs to someone other than me' —
would support the exclusion without ever representing agent B's rank as a
four-way quantity, and would produce the own-index pattern and this exact
null together. The run does not close that route and the findings do not name
it."* Its severity line calls it *"the one way FOUND NOWHERE could be
returned with the confound still live"*, and names the cheap check: a
two-answer target at that position.

"The one proposed confound" is accurate about what was proposed. It is
misleading about what is settled, in registered text that the successor will
read as a closed item.

### RT-158 — "a standardised refit of the same read agreed" is wrong three ways — serious, MEASURED

**It is not the same read.** `standardised-refit-findings.md` says so
directly: *"A standardised fit is a different estimator."* Its own part B
anchor deliberately does not reproduce the unscaled numbers and is not read
as failing for that.

**It is not even a paired comparison.** The ruling on this (RT-131): *"'Exactly
one thing changes' is false of the sweep"* — the per-test seed includes the
arm name, so every test in the refit uses a different fold split and a
different set of 200 shuffled draws. The ruling adds that the fold split alone
can account for a meaningful part of the move at the cell in question.

**It did not simply agree.** It moved a cell across the family bar. The block
does report that cell in the next clause, so this is not concealment — it is
that "agreed" is the wrong verb for a run whose single notable result is a
disagreement, and the word does the work of making the disagreement sound
like noise before the reader reaches it.

Two ruled cautions are also dropped. The refit is the **less** well-behaved
instrument of the two (RT-134: three degeneracy hits against none, and a
negative control running to +2.65 where nothing can be there, with the ruling
noting that *"the one cell it moved across the bar is at the bottom of its
range"*). And its bar is contested (RT-130: 3.38 *"was computed for a family
that no longer describes what has been run"*; RT-123: the refit imported the
bar as a fixed number instead of recomputing it).

None of this changes the block's conclusion. It changes how much the
conclusion is worth, which is what registered text is for.

### RT-159 — a discriminator that ran and is not named — serious, MEASURED

Part 2 of the brief asks specifically for "a discriminator that was run and
is not named". Here is one: the powered eleven-position sweep
(`powered-position-sweep-findings.md`). Two arms, eleven positions, five
layers, three checkpoints, 270 tests, 1,000 draws per test, a family bar of
3.56, and a clean negative on both arms.

The block alludes to it — *"the marker word has been read only by the weaker
difference-of-averages method at those positions"* — and never names it. It
is the only run that read the registered probe target at these positions, so
it is the run the block's most load-bearing localization sentence actually
rests on. Calling it "the weaker method" without naming it also understates
it: it is the run with the most draws and the strictest bar of the four, and
its negative control result is a small positive finding in its own right (the
acting channel does not leak the marker identity into the position where it
injects, which is what lets the other 270 numbers be read at all).

### RT-160 — the rulings the block honours, checked one by one — worth-noting (credit), MEASURED

Against the standard the previous review was credited with (a caveat drifting
to nothing across four findings files), this block holds up well. Checked
individually:

- **The two forbidden claim phrases** are not merely absent; they are named
  and refused in the registered text — "No result of A3 is described as 'a
  structural signature of self-indexing' or 'a structural signature of
  ownership-specific learning'." That is the form that survives being quoted
  (the rulings on claim scope, RT-113 and RT-119, and the amendment at
  RT-118).
- **"Partial discriminators" does not appear**, as step 4 ruling 5 required
  and the ledger's RT-114 asked.
- **The three statements the outside review asked to be kept separate** —
  registered status, observation, inference — are kept separate, in that
  order, in one sentence (Astra's fourth finding, accepted).
- **"Three independent lines now point at that one position" is absent**, as
  the 2026-09-21 ruling required (RT-135).
- **"Unexplained" is absent**, and the narrower sentence RT-139 licensed is
  the one used.
- **The register index is named as the fitted target and the marker word as
  the registered one** — the distinction the ledger twice ruled fatal to
  sentences that blurred it (RT-89, RT-112). The block gets this right, which
  is why RT-156's omission is a gap rather than a pattern.
- **Patching is described as new code**, per RT-96.
- **The state battery's one moving seed is reported** rather than rounded
  away, including its threshold — carrying forward the three-seed record's own
  statement that a write-up showing the other two without it *"would be
  flattering"*.

---

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
