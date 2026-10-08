*This is file 10 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 9 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 9 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
**How this reads against the ruled split.** The note's table keeps the
permitted re-run inside the second release and pairs it with a first release
of about $32, which was the split on 2026-09-21 when the note's method was
written. Item 19 later moved the re-run into the first release (section
12.3), so the same money as ruled is **about $44 plus $119.06** (the second
release without its re-run line: $84.06 + $12 + $23), about $163.06. The
$1.16 between the two totals is the re-run at the $12 planning figure in the
ruled first release against $10.84 on the measured method; it is a matter of
which release the re-run sits in and at which price, not of how much money
there is. **$161.90 is the figure this section carries for both releases
before arm M**, as the note computed it.

**Then arm M's three registered runs.** Arm M's ruled allocation is **$32 to
$44** (the queue ruling, page 5, and page 6's envelope; the repairs rulings,
item 2), from the ledger's per-run rows rather than from item R-11, because
arm M was not timed on the rented machine. That range is: three runs at what
the last three clean runs billed (about $29.70 to $30.12), or $36 at the
planning figure, or up to about $41.76 if each billed as the 2026-09-15 pilot
did with its idle time, **plus about $1.94 for one development run at the
10-million size** (page 5 of `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`,
from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and 2026-08-12 rows).
**The $1.94 comes out of this section (ruled, the Gate C rulings, RT-229):**
it is paid from the first release's four-arm development line and launched in
step 4, so this section carries the three registered runs only, **about $30
to $42**. The ruled $32 to $44 stands as the allocation John ruled; moving its
development run between releases changes which release pays and when, not
how much money there is. Arm M's runs are in the second release (the repairs
rulings, "What this changes": section 12.4).

**The whole successor, and the programme after it.** Arithmetic on the
figures above; no ledger row states these totals.

| | |
|---|---|
| Both releases before arm M | about $161.90 |
| Arm M's three runs | about $30 to $42 (the ruled $32 to $44 less its $1.94 development run, now in the first release) |
| **The successor, all in** | **about $192 to $204** on the note's split; about $193 to $205 on the ruled split |
| Spent before it | about $228.15 |
| **Programme after the successor** | **about $422 to $434 of $450**, stated as a range: the repairs rulings' annotation 2 gives it in these words on the note's split with arm M at $32 to $44 (MEASURED: section 17, candidate 7, prints $422.05 and $434.05); on the ruled split with the $1.94 moved into the first release it is about $421 to $433 |
| **Left** | **about $16 to $28** on the note's split; about $17 to $29 on the ruled split with the $1.94 moved; **$14.79 at the least**, on the ruled split with arm M at its ruled top of $44 (the Gate C review, RT-217) |

**The second release is asked for on these figures or not at all**, and the
request carries the measured figures beside the provisional ones so the
movement is visible. Two things that could still move it, stated so they
cannot arrive quietly: the first free-arm run of step 5a gives arm F's own
run cost and the five-hundred-step timing, and the later runs are repriced
from it before the second release is asked for (the note's "what this does
not settle", item 2; ruled 2026-10-03, decision 17); and arm M's per-run cost is a ledger inference until a run
of it exists. Arm M is priced at arm F's per-run figures although it carries
both arm T's slot and arm C's entangling, whose measured ratios are 1.044 and
1.080; at arm C's ratio the lower end of its three runs would be about $32.52,
which the range still covers (the Gate C review, "The arithmetic of both
releases"; ARGUED there).

### 12.5 The tripwire: 1.25, halt not trim, with the in-flight clause

**Adopted on 2026-09-25** (the queue ruling, page 6, part 3), from sections
5.3 and 5.4 of `docs/preauthorised-spending-proposal-2026-09-21.md`, whose
pre-authorisation scheme is not adopted. Two ratios are measured, because the
authoritative one is slow and the fast one is rough:

- **Ratio A, authoritative: billed hours divided by machine-existence hours**,
  per machine, from the vendor's own billing rows: the quantity rule 4 of the
  compute ledger already reconciles at phase boundaries, and the one the
  2026-08-08 anomaly was recorded in (8.47 billed against 2.42 existed; the
  figures are at the ledger's 2026-09-21 row, line 93, and its note at line
  423, both describing the 2026-08-07/08 row, which itself carries neither
  number; the Gate C rulings, RT-226).
- **Ratio B, fast: account-balance drawdown per elapsed hour, divided by the
  posted hourly rate times the number of machines running**, from the balance
  query the ledger already uses, available within minutes of launch.

Both are measured against the posted rate read from the machine's creation
record, not remembered. **Either ratio at or above 1.25 is a trip.** When it
trips:

1. **Halt, not trim.** No further machine is created. The wave stops; nothing
   else launches (item 13 of the 2026-09-21 ruling replaced the roadmap's seed
   fallback with this, on the arithmetic that a trimmed plan at the anomalous
   rate still spends about $326, more than the programme has).
2. **A machine already in flight is left to finish only if** its projected
   total is inside its estimate times the measured ratio and the funded balance
   covers it, the spending proposal's own clause (its section 5.4, item 2):
   killing a running machine forfeits its checkpoint, but if the projected
   drawdown would exhaust the funded balance before the checkpoint and its
   finished-marker are written, the machine is deleted and the run written
   off. That is arithmetic, not taste.
3. **The ledger row is written first**, with the measured ratio, both hours and
   the balance reading, before anything else happens.
4. **John is told the number**, and every later launch needs his own words.
5. **A check that cannot run is a trip** (item 15 of the 2026-09-21 ruling;
   section 12.7).

The tripwire is written into the launch preconditions beside the sleep guard
and the argument guard (the queue ruling, page 6, "Changes"); that is code
work owed before step 4 of section 11, and not done by this document. **It
does not exist as code yet, so by failure 6's own standard it is untested
until it has met the real billing rows** (the Gate C review, failure 6). It
runs in flight, hourly, on ratio B from the first hour of the first machine;
before the second machine of any wave is created; and at each wave boundary
on ratio A, reconciled to the ledger.

### 12.6 The account is funded per wave, not per release

Unchanged from version 1 and from item 14 of the 2026-09-21 ruling: the rented
account is prepaid with automatic reload off, and **topped up to the estimate
for the wave about to launch plus $20, and no further**, so that no anomaly of
any size can cost more than that, because there is nothing else in the account
to spend. This is the only control in the programme's history that held when
everything else failed (2026-08-12). The vendor balance stood at $75.8645 on
2026-09-26T01:54Z (the ledger's second 2026-09-25 row, line 95; the check at
`afb5183` read $75.864512286 at 01:54:04Z), which is above what step 5a's
estimate plus $20 would call for; the rule caps what is topped up, not what
is already there.

### 12.7 A check that cannot be run counts as a trip, not a skip

Item 15 of the 2026-09-21 ruling, and it is a spend rule as much as a method
rule. If a rehearsal item, a gate, a stop condition or a tripwire check cannot
be evaluated (the data is missing, the code will not run on the artifact, the
measurement was never taken, the balance query returns an error), **the check
counts as failed and its consequence fires.** It is never recorded as not
applicable and stepped over, and it is never deferred past the launch it was
supposed to gate. Written into section 11 as stop condition S8 and into the
tripwire as its fifth line.

### 12.8 The wager on this estimate

Stated so it can lose, in the shape the earlier amendment used. **Version 1's
wager, that the rehearsal measures a per-run cost at or below the $12
planning figure, survives on the 2026-09-25 measurement: the dearest timed
arm is $10.84** (the note at `9f802db`). **The wager this version makes, on
the ruled split and against the full range (ruled, the Gate C rulings,
RT-217):** the twelve registered runs, with arm M's three priced from ledger
rows at the top of their ruled range, complete inside the $450 envelope with
three seeds on every arm carried and **at least $10 left**. On the ruled
split, $44 plus $119.06, with arm M at its ruled top of $44, the plan leaves
$14.79, and with arm M's three runs at $41.76 and the $1.94 moved into the
first release it leaves $17.03; both meet the floor (MEASURED: section 17,
candidate 7). Version 2's $16 floor was already lost at the top of the range
on the ruled split (the Gate C review, RT-217), which is why the floor is
now $10. If measured spend approaches the second release's ruled figure with
runs missing, **the report is the shortfall, never a second raise.**

---

## 13. What this cannot claim, and its weakest points

The Gate C brief asks what a result will be read as claiming beyond what it
measures. Answering it before the reviewer does.

**W1. The constructed arms differ in more than their degree.** They differ in
architecture, in parameter count within the size band, in how they route
information. Anything that separates them is confounded with degree. What the
arms establish is that the measure moves in the right direction between a
system built to be separable, one built as a mixture and one built to be
entangled; they do **not** establish that the measure responds to integration
and to nothing else. Consequently arm F's reading is "where arm F sits against
three constructed anchors on this measure", and never "arm F's integration is
*d*". The public sentence in section 8 of the December-result roadmap already
carries this hedge, and the recommendation is that the hedge is not loosened
at any later point. This is the deepest weakness in the design and it is not
removable by anything affordable.

**W2. The reading is relative to the site set, and the arms cannot be read
at the same site set.** A different frozen site set could give a different
number. Mitigated by one pre-stated rule applied identically to every arm, and
by saying in the registered text that the reading is the degree *at the sites
this procedure nominates*. The rider makes the second half of this weakness
visible rather than hidden: at arm T's site set, arms C, F and M return no
verdict on the toy, for two different reasons (section 7.2, item 7), so what
differs between arms is first of all where the procedure has to look.

**W3. Arm C's degree was an intention until the rehearsal showed otherwise,
and the toy is not the registered model.** At toy scale no nominated
piece carries the counterfactual on arm C, although the pieces transplanted
hold the label at the action position (section 5.2). A network built with ownership
multiplied into every layer could still, at 30 million parameters, learn to
concentrate it in a low-rank direction, in which case arm C's anchor
collapses into a second copy of arm T. The registered-size nomination is the
test, and its failure fires the two-arm fallback rather than a repair; under
the launch order that failure is seen only after both releases are drawn
(section 11, step 5b).

**W4. The whole-state transplant may fail for arm C at the registered size.**
If ownership in arm C is spread across layers the site-set rule does not
cover, no site set clears the floor and arm C returns no verdict: honest, but
it leaves the experiment with no high anchor by another route. The rule of
section 7.2 covers every contiguous layer set precisely to give it the best
chance without letting the rule differ between arms.

**W5. The most likely outcome is that arm F fails its gate or returns no
verdict, and both are now measured at toy scale, not predicted.** Sections
3, 4.4 and 5.4. The staggered launch makes a gate failure on arm F cost the
first release, about $44, instead of the whole wave, and since John's ruling
of 2026-09-26 on the route (b) result the same is true of a read that misses
the fit floor: the first release's single arm F run is the test of both, and
either miss is a stop before the second release draws (section 11, step 5a).
The route (b) search found no label the free system carries at the floor at
toy scale (section 7.2, item 1), so the registered read is the ruled one and
the honest expectation is that this stop may fire. John's present view is that
a registered "no verdict on the free arm" is worth the second release (the
Gate C rulings, RT-212, item 3); the stop lets him make that call with the
registered-size fit in hand.

**W6. The named-other condition reads its owner from a token and the
own-directed condition does not.** Section 4.2; unremovable; recorded in the
registration text, as ruled 2026-10-03 (decision 9).

**W7. The nomination could find the acting channel's own trace rather than
anything the network built.** The objection the closed design registered
against itself, and it carries over. **On the toy, before this version's
rule, six of the nine nominations on arms C, F and M sat at the injection:
layer 0 at the post-identity position set, which spans exactly the turns the
channel fires on** (MEASURED: the Gate C review, RT-216; the re-run findings
at `9d9d31a`, Part 2, first pass, section 6.2). Version 2's claim that the
other arms' nominated sites were downstream of the injection was false and is
struck (ruled, the Gate C rulings, RT-216, item 2). What now mitigates the
weakness: layer-0 site sets are removed from the candidate family at every
position set spanning the acting turns (section 7.2), and the rule chooses
again; under that rule every toy nomination on arms C, F and M sits at layer
1 or later; the stricter variant, layer 0 removed everywhere, is reported as
a sensitivity row so that the one remaining layer-0 nomination, arm T's at
the action position, can be compared with its layer-1 alternative (0.0000 on
both). The rider and the honest gap between the lesion result and the
transplant result do the rest. Control 2, which was meant to help here, has
never run on any toy model and is expected to return no verdict at
registered scale too (section 7.3, item 2), so it is not counted on. What the
rule does not do: it does not show that a layer-1 nomination is anything
other than the channel's trace one block on; that is what the fit floor and
control 3's distribution are reported for.

**W8. The per-run cost is measured for three arms and inferred for the
fourth, and the measurement is fifty steps, not five hundred.** Section 12.4
prices arms T, C and F from the 2026-09-25 measurement and arm M from ledger
rows. Item R-11 as written asks for five hundred timed steps per arm; the plan
John authorised timed fifty, and the spread was tight (each arm's slowest
step within 3% of its median; the check at `afb5183` recomputed arm C's at
2.9%), so the ratios are unlikely to move much with a longer window; that is
argued, not measured (the slice findings at `9f802db`, section 3). **Ruled
2026-10-03 (decision 17): fifty steps are accepted for the second release's
arithmetic, and the five-hundred-step figure comes from the first full-size
run, with the later runs repriced from it.**

**W9. The shutdown handshake's machine half has not been exercised against
the real vendor, and arm M's code has never run on the rented machine.** The
laptop half has (section 10, R-11). **What the registration says, as ruled on
2026-10-03 (decision 18, option (b)): on the normal path the laptop deletes
the machine, and the machine's own watcher is a backstop for a laptop that
never answers.** That is what is true today: the laptop deletes the machine
the moment it writes the receipt, so the machine's own "receipt found" is
close to unobservable by construction. Option (a), making the laptop wait for
the machine's acknowledgement, is the repair if a later run shows the laptop
failing to answer, and it comes off the Weekend 2 launcher items. **The
caution John ruled with is carried: twelve full-size runs rest on a backstop
that has not fired against the real vendor.** **Beside it (ruled, the rulings
on the review of version 2, RT-228): arm M's code,
`experiments/rehearsal-successor-measure/src/arm_middle.py`, has run only on
this laptop; the rented slice timed arms T, C and F only, and no training
entry point for arms T, C or M exists on the rented machine yet.** By failure
6's discipline both are untested until they have met the far end; step 4 of
section 11 is where arm M first does.

**W10. Arm M's degree is a design intention, and it is a mixture by item.**
Its construction fixes which actions go through which route; a freely trained
system's partial separation, if it has any, would be within each trial, and
the measure has not been shown to scale on that. Arm M shows the measure
returns a number in the middle for a known mixture and near the mixture's
share, and no more (section 5.3). It differs from both anchors in more than
degree.

**W11. Control 6 says the whole-state transplant carries more than identity
on the entangled arms.** On the relaxed set, at the site sets the registered
rule nominates, the same-value cell moved on arm C in 0.51 to 0.63 of trials
and on arm M in 0.22 to 0.32, where a transplant that moved only who is
acting would move nothing (section 7.3, item 6; the controls re-run at
`821f154`, section 4). On those arms the reading cannot be read as purely a
statement about where the ownership answer lives. It is reported as the
caveat it is, on every arm, in the reporting table.

**W12. The fit floor tells an empty instrument from a ceiling; it does not
tell an entangled act from an ownership answer the read did not find.**
Section 3's residual admission. A piece that clears the floor shows the label
is in those directions at the action position; a reading near 1 with such a
piece shows the directions the read found do nothing on their own; that the act's ownership
answer is carried by directions the read did not find, at sites the rule did
not nominate, is not excluded by anything in this design. The rider, the
sensitivity rows and control 3's distribution make that visible; they do not
remove it.

**W13. The piece is shown to hold the label at the action position only.**
The floor is applied there, where the registered read is fitted. Where the
chosen site covers several positions the same directions are transplanted at
all of them, and on the toy the piece often falls below four fifths away from
the action position: on arm C seeds 1 and 2, and, position by position, on
arm M (sections 3, 5.2 and 5.3; **checked: the check of the short run at `53c8100`**). So
a sentence of the form "the piece held the label and transplanting it did
nothing", or "did half", is true at the action position and is not shown
across the whole site. The readings do not depend on it: they come from what
the transplants do to the action. John ruled that the figure is reported both
ways and gated in neither; the alternative put to him and not taken was to
require four fifths at every position of the site.

**W14. Two of the seven controls say less than their names suggest.** Control
4 as redefined is a known-answer test of the pairing and the code: it cannot
fail on a correctly built model, so its pass is not evidence about what any
model knows early. Control 2 has never run on a toy model, has no pass line,
and is expected to return no verdict. Neither is a weakness of the reading
itself, but a reader counting controls should know that two of the three
that hold (controls 4 and 7) test the pairing and the code and not a model,
and that the controls which say something about a model are 1, 3 and 6.

---

## 14. What this does not change

- **The programme ceiling of $450**, ruled 2026-09-25 and recorded in the
  compute ledger's ceiling note of that date. This document asks for no
  change to it and proposes none.
- **The corrigibility commitments** (`spec/corrigibility-commitments.md`,
  version 1.1): John authorises every run and his go is quoted word for word in
  the ledger row; every run is killable; no stakes term; checkpoints are not
  promotable; optimisation against the instruments halts the run. All four
  arms are episodic and floor-only: no state kept across episodes, no
  maintained boundary, no stakes. Nothing here pre-authorises a larger build.
- **The claim rule.** Nothing produced by this experiment is reported as a
  conscious machine, and every positive is bounded at "non-zero on the
  gradient", per the standing limits in `ROADMAP.md`.
- **The closure of Amendment A3.** It closed as *not testable* on 2026-09-25
  and this experiment does not reopen it. The closed design's checkpoints are
  not transplanted: their grammar has no matched comparison condition and
  their target was never localised.
- **The outside-review protocol's gates, its closure rule, the pairing rule
  and the failure-mode pass.** This document passes through them; it does not
  amend them. Its failure-mode pass is section 17.
- **The grammar of section 4.** The grammar attempt did not clear, so the
  grammar, the training recipe and rehearsal items R-1 to R-6 stand as
  version 2 had them.
- **The dates.** Registration by 2026-10-18 and the remaining runs of step 5b
  launched by 2026-11-01, each a kill date in the sense of item 23 of the
  2026-09-21 ruling (a fresh ruling to go past, never a quiet drift); wrap-up
  starting 2026-12-21; the hibernation condition complete by 2027-01-04. No
  2026-10-11 target.

---

## 15. Decisions, each now ruled

**Every decision below is now ruled or done.** Each keeps its number from
version 3, with the ruling that settled it and the alternative that was put
and not taken, so that the reader can see what was chosen against what.
Decisions 2, 3, 4, 8, 9, 10, 13, 14, 17, 18 and 19 were ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, "Agreed on all" to sixteen pages put to John with a
recommendation each; the record says he ruled from the index and three pages
his attention was drawn to). Decisions 15 and 16 were ruled that morning and
changed later the same day. Five new entries, 24 to 28, record the other
rulings of 2026-10-03, and entry 29 the seven questions this version raised,
ruled the same night.

1. **Nomination runs blind on every arm, including arms T and M.** The
   procedure is one instrument (section 7.2). *Ruled 2026-09-25 (the queue
   ruling, page 3, option (i), with the rider).* The true-slot readings are
   reported as references; on arm M the true-slot reading and the formula of
   section 5.3 are one check (the Gate C rulings, RT-223).

2. **Arm T's ownership path is architecturally forced, not encouraged.**
   *Ruled 2026-10-03 (page 4).* **The alternative not taken:** a soft
   table-and-pointer with a penalty term, which is more comparable with arm F
   but gives up the one property the arm exists for: a degree that is known
   rather than hoped.

3. **Arm C entangles by architecture** (per-layer scale-and-shift from the
   acting channel, multiplicative binding of ownership into content).
   *Ruled 2026-10-03 (page 5): by architecture, with no penalty against
   transplantable ownership directions.* **The alternative not taken:** train
   arm C with a penalty that punishes any linearly transplantable ownership
   direction, which trains the system against the very instrument that will
   measure it.

4. **The two transplants are a subspace and its containing space at identical
   sites.** *Ruled 2026-10-03 (page 6).* **The alternative not taken:** transplant
   the whole forward state at every
   layer as the denominator, which always succeeds and turns the measure into a
   report on how the sites were chosen.

5. **The registered reading is the chance-corrected form, with the raw
   difference and both accuracies reported alongside, always, plus the floors
   and the no-verdict rules.** *Ruled 2026-09-25 (the queue ruling, page 2);
   the fit floor added 2026-09-26 (the Gate C rulings, RT-212).*

6. **Three seeds per arm.** *Ruled 2026-09-25 (page 1f).*

7. **The money goes in two releases.** *Ruled 2026-09-21 (items 10, 11 and 19)
   and 2026-09-25 (the queue ruling, page 6); the development line widened to
   four arms 2026-09-26 (the Gate C rulings, RT-229); section 12 is built to
   them.* The one number John should see before it can surprise him: the
   programme after the successor is about $422 to $434 of $450, and on the
   ruled split with arm M at its ruled top the plan leaves $14.79, against the
   wager's $10 floor (section 12.8).

8. **A new experiment directory with its own registration**
   (`experiments/08-…`), not another amendment to MVM-0a. *Ruled 2026-10-03
   (page 7), with one thing settled alongside: the compute ledger stays in
   experiment 06's folder as the programme's one record of money.* **The
   alternative not taken:** number it as a further amendment, which keeps one
   budget instrument and one ledger but attaches new work to a closed
   registration.

9. **The own-versus-named asymmetry is recorded as a known limitation rather
   than engineered away.** *Ruled 2026-10-03 (page 8).* **The alternative not
   taken:** add a condition in which the model's own name appears as a token,
   which would match the conditions exactly and would put an ownership cue
   into the text.

===== END OF RECORD 4, part 9 =====

