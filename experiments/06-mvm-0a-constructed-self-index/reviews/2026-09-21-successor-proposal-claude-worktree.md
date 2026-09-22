# Gate C, tier 1 — the successor experiment proposal, version 1 as revised

*Filed 2026-09-21 (Pacific) by a fresh Claude Code session in its own
worktree (`worktree-agent-a5e89aa434ea3f396`), which did not write the
document under review and had no part in drafting it. Target:
`docs/successor-experiment-proposal-2026-09-21.md` at commit `d8ceba9` on
branch `worktree-agent-a94b8938df2edd88b`. Everything else was read at
`dd1b974` on the main line. Filed under `docs/outside-review-protocol.md`,
Gate C (a review attached to a proposal so John rules on text that has
already been attacked). Filed verbatim and not edited after filing.*

*Ledger numbering: the highest red-team number in
`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md` at the
time of filing is **RT-171**. This review runs **RT-172 to RT-188**.*

*Lookup: none used. No web search and no outside reference. Every finding
below is checked against files in this repository at the commits named.*

*Written under the workspace plain-language rule
(`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30).*

---

## What was opened, and what was not

**Opened** (all committed, never a working copy): the target proposal at
`d8ceba9`; the review protocol (`docs/outside-review-protocol.md`) in
full, including the amendment section; the two rulings
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`,
`docs/rulings/2026-09-20-december-result-roadmap.md`); the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`) row by
row; the shutdown fix's method note
(`experiments/06-mvm-0a-constructed-self-index/reap-shutdown-order-method.md`),
sections 1, 2, 3, 4, 7, 8, 9 and 10; the red-team ledger's last block
(items RT-140 to RT-171, the Gate A pass on the Amendment A3 closure text);
the December-result roadmap, section 6; the findings file for the
other-agent-index sweep
(`experiments/06-mvm-0a-constructed-self-index/other-index-position-sweep-findings.md`);
and the registered episode generator's source,
`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py`.

**Not opened, deliberately:** `STATUS.md`; any chat transcript; any
uncommitted file in the shared checkout; the drafting session's own notes.

**Checked is not accepted.** Where a number reproduced, this review says
so and says what command produced it. Where a claim was read and believed
without a check, it is labelled ARGUED and should be read as an argument a
reader may dispute.

---

## The findings, in one table

| # | What | Severity | Kind |
|---|---|---|---|
| RT-172 | The registered reading divides by an uncorrected accuracy, so its top of scale is different for every arm and the separation bar cannot travel from the rehearsal's toy models to the registered ones | **fatal** | MEASURED |
| RT-173 | The discriminating control's first cell is empty by construction, and the pre-stated "the pairing is broken" rule fires on a model that has learned the task and passes on one that has not | **fatal** | MEASURED |
| RT-174 | The development-run price cites the wrong ledger row; the row named is the billing-anomaly row whose actual is $6.02, and the number quoted lives in the next row down and was billed at a cheaper venue | serious | MEASURED |
| RT-175 | The 1.55-times premium is attached to a gap that is 1.195 times, and no record in this repository contains 1.55 other than the ruling asserting it | serious | MEASURED |
| RT-176 | The plan totals $175 against a $130 cap the document names as its own bound and never reconciles against | serious | MEASURED |
| RT-177 | Under decision 7's named alternative the one permitted re-run is paid for twice, and the two releases come to $187 rather than $175 | serious | MEASURED |
| RT-178 | The cost of the single most likely outcome is stated as about $32 in one section and about $44 in two others, and the outcome's own definition makes $32 unreachable | serious | MEASURED |
| RT-179 | The rehearsal buys a measurement of three architectures John has not ruled on, taken on code and a grammar that are not frozen until after registration | serious | ARGUED |
| RT-180 | Three human-gated steps sit between the first registered run and the remaining eight, and the proposal prices that gap as a day of schedule | serious | ARGUED |
| RT-181 | "The matched control … first ran on 2026-09-21" repeats an elision the ledger ruled fatal earlier the same day, and the date is wrong | serious | MEASURED |
| RT-182 | The invalid verdict has no registered outcome term, so the most likely way the measure fails cannot be reported in the vocabulary the document makes binding | serious | ARGUED |
| RT-183 | The rented slice's pass rule assumes three shutdowns; its own cost table buys one | worth-noting | MEASURED |
| RT-184 | The shutdown method note was on the main line eighteen seconds before this commit; the document sends a reviewer to a branch | worth-noting | MEASURED |
| RT-185 | A ruling's figure is quoted as $328 when the ruling says $326, and the invented gap is then explained away as rounding | worth-noting | MEASURED |
| RT-186 | Decision 13 attributes a ten-hour run's destruction and $97.04 to one failure; the record has two different events, and the ten-hour one was recovered for seven cents | worth-noting | MEASURED |
| RT-187 | Bare identifiers and unglossed terms, repeating a defect ruled on the closure text the same day | worth-noting | MEASURED |
| RT-188 | What held: the rented slice's arithmetic, the headroom, the halt-not-trim arithmetic, every figure taken from the shutdown method note, and the standing rule's quotation | worth-noting (credit) | MEASURED |

---

## Part 1 of the brief — feasibility. Can the quantity be recovered with the instrument named?

### RT-172 — the reading divides by an uncorrected accuracy, so its top of scale differs by arm. **FATAL. MEASURED.**

**What is wrong.** Section 6.3 registers the reading as

> `degree = (accuracy_whole − accuracy_ownership_only) / accuracy_whole`

and says in plain words that "Zero means fully separable" and "The number
rises toward one as the act resists being pulled apart". Section 6.3 also
defines a third quantity, `accuracy_untouched`, "the same share with no
transplant at all, reported as a floor", and expects it to be non-zero.
Nothing in the design ever subtracts that floor from either term of the
ratio.

A floor that sits under both terms does not cancel in a ratio. Write the
floor as *u*. If the ownership-only transplant does nothing at all, the
ownership-only accuracy is not zero, it is *u*, and the largest reading the
formula can return is 1 − *u* divided by `accuracy_whole`. That top of
scale is different for every arm, because `accuracy_whole` is different for
every arm — and the design expects it to be, which is why section 7.2 item
4 lets each arm choose its own layer set and section 6.4 admits an arm may
fall below the floor entirely.

**The check I ran.**

```
$ python3 -c "
def degree(w,o): return (w-o)/w
u=0.125
for w in (0.9,0.6,0.35):
    print(f'  accuracy_whole={w:<5} top of scale = {degree(w,u):.3f}')
print()
for w in (0.9,0.35):
    o = u + 0.5*(w-u)          # half the identity-driven effect lies outside the subspace
    print(f'  accuracy_whole={w}, ownership_only={o:.4f}, TRUE share outside = 0.500 -> registered degree = {degree(w,o):.3f}')
"
  accuracy_whole=0.9   top of scale = 0.861
  accuracy_whole=0.6   top of scale = 0.792
  accuracy_whole=0.35  top of scale = 0.643

  accuracy_whole=0.9, ownership_only=0.5125, TRUE share outside = 0.500 -> registered degree = 0.431
  accuracy_whole=0.35, ownership_only=0.2375, TRUE share outside = 0.500 -> registered degree = 0.321
```

Two systems in which exactly half the identity-driven difference lives
outside the nominated subspace — that is, two systems of identical degree
by the document's own account of what the number means — read 0.431 and
0.321. The gap is produced by nothing but their overall transplant
accuracy.

**Why it matters, and why it is this programme's own history.** Section
6.4 opens by naming the closed Amendment A3 failure: "a comparison whose
denominator was zero from the day it was registered". The lesson taken from
that is narrower than the lesson available. What went wrong in Amendment A3
was not only a zero; it was a denominator whose behaviour had never been
measured on the condition it would be applied to
(`ceiling-defect-2026-09-17.md`, and ledger item RT-21, the finding that the
corrected metric had a zero denominator). This design repeats the shape: the
denominator is a per-arm quantity with a per-arm ceiling, and the separation
bar between arms T and C is set at tiny scale by rehearsal item R-10 from
models whose transplant accuracies will not be the registered models'
transplant accuracies. A bar in units whose ceiling moves between the place
it is set and the place it is applied is not a bar.

It also leans in a known direction. Weakness W4 says arm C's whole-state
transplant may be the weakest of the three. A low `accuracy_whole` for arm
C compresses arm C's top of scale — the very arm that is supposed to supply
the known-high anchor. The design is therefore tilted toward outcome R2
("metric does not separate") for a reason that has nothing to do with the
systems being measured.

**What would close it.** One of: (a) register the chance-corrected form,
`(accuracy_whole − accuracy_ownership_only) / (accuracy_whole −
accuracy_untouched)`, which on the same numbers above returns 0.500 for
both arms — I ran it, it does; (b) keep the registered ratio but add to
section 7.4's frozen list a pre-stated band on `accuracy_whole` outside
which no arm is read, so the bar is only ever applied where it was set; or
(c) register the raw difference as primary, which decision 5 already names
as the alternative and declines. Whichever is chosen, rehearsal item R-6
should exercise it on two toy cases of equal true separability and unequal
transplant accuracy and show the reading is the same, because that is the
property the registered sentence claims and no rehearsal item currently
tests.

**Confidence: high on the arithmetic**, which is elementary and reproduced
above. **Moderate on how large the effect is in practice**, which depends
on transplant accuracies nobody has measured — which is itself the point.

### RT-173 — the discriminating control's first cell is empty by construction, and the pairing check fires on success. **FATAL. MEASURED.**

**What is wrong.** Section 7.3 control 6 is described as "The
discriminating control" — the one that separates "the transplant moved who
is acting" from "the transplant smuggled a value across":

> Trials are split into pairs whose donor identity dictates *the same*
> value as the recipient's and pairs where it dictates a *different* value.
> … Both cells are pre-stated and both are reported.

The first cell cannot be populated. The grammar this one extends assigns
each contested item four **distinct** values, one per agent, and enforces
it:

```
$ sed -n '15,18p;212,216p;537,539p' experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
- **Eight assignment turns.** Each agent assigns each contested item
  ...
  pairs. Within an item the four values are **distinct**, so an item's
  four assignments differ only in who made them.

    # distinct values per contested item, one per agent
    values: dict[str, dict[int, str]] = {}
    for item in contested:
        vs = rng.sample(SLOTS, N_AGENTS)

            assert len(set(vs)) == N_AGENTS, "distinctness broken by enactment"
```

`rng.sample` draws without replacement, and the self-test asserts the
property survives rendering. Two different agents therefore never hold the
same value on the same item, and since the revision rule is the same
deterministic successor in both conditions, two different agents never
dictate the same answer. Control 6's "same value" cell has no trials in it.

The proposal does not merely permit this; three other passages *require*
it. Section 4.2 item 1 says a solver that cannot tell whose value it needs
"can do no better than one in four", which is only true if the four values
are four different answers. Section 6.1 says a successful transplant
"changes which of four in-context values gets selected", which is only a
change if they differ. Section 5 puts all three arms on the one grammar. So
distinctness is load-bearing in sections 4.2 and 6.1 and in section 6.3's
one-in-four reference point, and control 6 needs its negation.

**The same defect, one step further.** Section 6.3 says of the untouched
condition: "It should be near the one-in-eight guessing rate; if it is not,
the pairing is broken and nothing is read." With distinct values, an
untransplanted model outputs the recipient's own answer, which is never the
donor's; it can only land on the donor's answer by erring onto exactly that
slot. If errors spread over the other seven slots, the untouched rate is
about one minus the accuracy, divided by seven:

```
$ python3 -c "
for p in (0.95,0.80,0.60,0.506,0.25):
    print(f'  own-directed accuracy {p:<6} -> accuracy_untouched = {(1-p)/7:.4f}')
"
  own-directed accuracy 0.95   -> accuracy_untouched = 0.0071
  own-directed accuracy 0.8    -> accuracy_untouched = 0.0286
  own-directed accuracy 0.6    -> accuracy_untouched = 0.0571
  own-directed accuracy 0.506  -> accuracy_untouched = 0.0706
  own-directed accuracy 0.25   -> accuracy_untouched = 0.1071
```

The stated check is satisfied by a model that has learned nothing (0.107,
near one in eight) and violated by a model that has learned the task
(0.007). As written, the rule reads a working instrument as a broken one
and a broken one as working. It sits inside section 7.4's frozen list —
"all seven controls and their pre-stated cells" — so it would be registered
in that form.

**Why it matters.** The protocol makes this fatal twice over. The fixed
brief asks "can it be measured at all with the stated instrument, and can
the control or comparison condition actually reach the stated threshold".
And John's ruling of 2026-09-21, item 5: "A pre-stated quantity the
rehearsal never exercised is a fatal finding on its own." Here the quantity
is worse than unexercised — it is unreachable in the grammar the design
names, and the check attached to it is pointed the wrong way round.

**What would close it.** Either the successor grammar deliberately relaxes
distinctness for a named fraction of items so control 6's first cell
exists, with the consequences for section 4.2's one-in-four reference
worked through; or control 6 is re-specified on something that does exist —
for instance splitting trials by how far apart the two answers sit in the
successor ordering — and the "smuggled a value" question is answered by
that instead. Either way, section 6.3's untouched expectation is restated
as what the grammar actually implies, and rehearsal item R-8 measures the
untouched rate on the toy models rather than assuming it.

**Confidence: high** that the property holds in `curriculum_a3.py`, quoted
above. **Moderate** that it carries into the successor grammar, which does
not exist yet — but the proposal says in section 4.1 that the new grammar
"extends the registered Amendment A3 grammar … which already has the
pieces" and lists them, and the internal contradiction between sections 4.2
and 6.1 on one side and section 7.3 control 6 on the other stands whatever
the code turns out to be.

### RT-179 — the rehearsal times three architectures John has not ruled on, on code and a grammar that are not frozen. **SERIOUS. ARGUED.**

Rehearsal item R-11 spends real money to measure seconds per step for arms
T, C and F "built at the registered size", and the second release of money
is bound to the result: "If item R-11 does not produce them, the second
release is not asked for at all."

Three things that measurement depends on are not yet in place.

1. **The architectures are unruled.** Decisions 2 and 3 in section 15 put
   arm T's forced ownership path and arm C's per-layer scale-and-shift to
   John, each with a named alternative. The ruling of 2026-09-21 says
   plainly, under "What was NOT ruled here": "The twelve design decisions
   inside the successor proposal are not ruled." Decision 3's alternative
   is a different architecture, not a variant — a penalty term instead of
   multiplicative binding — and its seconds per step would be a different
   number. The document's own order of work runs the rehearsal first and
   John's decisions after.
2. **The code is not frozen.** Section 11 item 3 puts implementation freeze
   and the self-tests after registration. So R-11's pace is measured on
   pre-freeze code and the second release is priced from it.
3. **The grammar is not frozen.** Seconds per step depends on sequence
   length, and sequence length is a property of the new matched-role
   grammar, which the registration fixes later. R-11 requires only that
   batch size and sequence length be "the same … on all three" arms — it
   never requires them to be the registered ones. The ledger shows this is
   not hypothetical: the 2026-09-15 row prices its own run through "0.71x
   [steps] … offsetting 1.26x enactment passes and 1.41x sequence length",
   a 41% swing from sequence length alone.

The document is admirably sharp that a pace measured on the Mac is a fact
about the Mac. A pace measured on unfrozen code running an unfrozen grammar
is a fact about that code and that grammar, and it is the same class of
error one layer in. Stop condition S8 — a check that cannot be evaluated
counts as failed — makes this expensive rather than merely untidy.

**What would close it.** Say in R-11 which of its inputs must be settled
before the slice is bought (at minimum: the three architectures as ruled,
the sequence length, the batch size), and make the slice depend on John's
rulings on decisions 2 and 3 rather than precede them. If the intent is
that the measurement is approximate and will be re-taken, say that, and say
what re-taking costs.

---

## Part 2 of the brief — satisfied by the wrong thing

### RT-182 — the invalid verdict has no registered outcome term. **SERIOUS. ARGUED.**

Section 3 says: "The registered wording is the wording in the middle
column; nothing in this document may report an outcome in other words."
The four terms are *metric validated, degree read*; *metric does not
separate*; *substrate not a testbed*; and the schedule failure. Section 6.4
then creates a fifth thing that can happen — an arm returns the invalid
verdict because its whole-state transplant is below the floor — and section
7.2 item 4 makes it reachable by rule ("If no layer set clears it for an
arm, that arm returns INVALID"). Weakness W4 says arm C is the likely one.

An invalid verdict on arm C is not "the measure cannot tell T and C apart
at the bar"; it is no reading at all on the anchor the bar is defined
against. An invalid verdict on arm F after arms T and C have separated is
not covered either. Under the sentence quoted above, neither can be
reported.

This is the no-verdict question and the over-reading question at once,
because a result with no registered word for it is the one most likely to
be described in whatever words the writing session reaches for. What would
close it: a fifth registered term, or an explicit rule mapping an arm C
invalid verdict to the two-arm fallback and an arm F invalid verdict to a
named outcome, added to section 3's table rather than left in section 6.4's
prose.

### RT-181 — a control described as having run, in words the ledger ruled fatal the same day. **SERIOUS. MEASURED.**

Section 7.3 control 2 ends:

> This is the matched control that the closed design registered as L2(a)
> and that first ran on 2026-09-21.

Two things are wrong with eleven words.

**First, the elision.** Red-team ledger item RT-155, marked **fatal** and
accepted, is about this exact sentence pattern in the Amendment A3 closure
text:

```
$ grep -n "RT-155" experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
| RT-155 | "The registered matched control (§L2(a), the other agent's index) ran once" — `RT-142` ruled that this must not be elided: only the **probe** half ran; the registered control also needs the **lesion** half … no such subspace was found, and "that control remains unavailable" …
```

The ruling's stated reason is precisely the harm here: the sentence "tells
the successor it inherits one fewer obligation than it does". This document
is the successor, and it inherits the sentence.

**Second, the date.** The run's own findings file opens 2026-09-20:

```
$ sed -n '1,4p' experiments/06-mvm-0a-constructed-self-index/other-index-position-sweep-findings.md
# The other agent's index at the same positions — findings

*2026-09-20 (Pacific). **UNREGISTERED** as a verdict-bearing run,
diagnostic only. …*
```

What would close it: "the probe half of which ran on 2026-09-20, with the
lesion half never run and the control recorded as unavailable", and a note
in section 7.3 that this experiment's control 2 is a fresh obligation
rather than an inherited discharge.

---

## Part 3 of the brief — the money, and the arithmetic

### RT-174 — the development-run price cites the wrong ledger row. **SERIOUS. MEASURED.**

Section 12.3's second line reads: "The earlier 10-million run measured
$1.94 for 2.86 machine-hours (compute ledger, the 2026-08-07/08 pilot
row); three at about $2, plus margin".

The 2026-08-07/08 row contains neither number, and its actual is more than
three times the one quoted:

```
$ grep -n "^| 2026-08-07/08" experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
59:| 2026-08-07/08 | pilot | 10M learnability pilot … | 4090 $0.74 (12.6 min) + 5090 $0.69 community | 1–2.5 → 2.4 (+0.2 dead pod) | $1.50 (cap $2.96) | **$6.02** ⚠ | **$6.02 / $200** |
```

The quoted figures are in the next row down, a different run at a different
venue:

```
$ grep -n "^| 2026-08-09 " experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
61:| 2026-08-09 | pilot (A1) | **A1 10M pilot** … 22,369 steps / 171.79M tok in 2.78h train (2.86h pod) … | 5090 community $0.69/hr | est 2.5–3.5 → 2.86 | …
$ grep -n "1\.943" experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
122:- A1 10M row trues up to **$1.943** (5090, 08-09) — nominal; the 08-08
```

Three separate problems follow.

1. The row named is the **billing-anomaly row** — the $6.02 against about
   $1.70 expected that this same document cites in section 12.4 as "the
   unexplained 3.5× billing row of 2026-08-08". Section 12.3 uses that row
   to argue development runs are cheap; section 12.4 uses it to argue a run
   might cost three and a half times its estimate. Only one of those can be
   what the row says.
2. The number that does exist, $1.943, was billed on a **community**
   machine at $0.69 an hour. The registered venue is a secure machine at
   $0.99 an hour, and the ledger's 2026-08-15 row gives the reason secure
   was chosen: it "avoids the community billing-anomaly venue". At the
   secure rate, 2.86 hours is $2.83, and three runs are about $8.50 — which
   still fits the $10 line, but leaves margin of about $1.50 rather than the
   $4 that "three at about $2, plus margin" implies.
3. Section 12.3's own standard is stricter than this. It marks two of the
   five lines in the rented-slice table as "Allowance, not a measurement …
   because an uncited measured claim is a fatal finding under the closure
   rule". The development-run line says "measured" and cites a row that does
   not contain the measurement.

**What would close it:** cite the 2026-08-09 A1 row and its $1.943 true-up,
say it was a community-venue price, and restate the three-run estimate at
the secure rate.

### RT-175 — the 1.55-times premium is attached to a gap of 1.195 times. **SERIOUS. MEASURED.**

Section 12.4 says version 1 carried the $12 planning figure "instead of the
$10.04 measured on 2026-09-17 … 'to cover arms T and C being slower per
step'. That premium — **1.55x**, in the ruling's own figure". Weakness W8
repeats it: "the 1.55x premium the $12 planning figure carries".

```
$ python3 -c "print(12/10.04)"
1.1952191235059761
```

The $12-over-$10.04 premium is 1.195 times, not 1.55. The ruling's 1.55 is
a different object — its item 11 attributes it to "a different experiment's
full-versus-twin step times", not to the planning figure:

```
$ grep -rn --include='*.md' "1\.55" docs/ experiments/ | grep -v successor-experiment | grep -v bundle-3 | grep -v chunks/
docs/rulings/2026-09-21-review-verification-and-staged-spending.md:67:    measurement rather than on the 1.55× premium inferred from a different
```

That is the only occurrence in the repository's prose. The figure the
ruling declines to build on has no record behind it anywhere, and this
proposal — which quotes it four times and builds a paragraph explaining why
it must be replaced — welds it onto a number it does not describe.

The consequence is not academic. The rented slice's cost table budgets arms
T and C at "up to twice arm F's pace". So the document carries three
different premiums for the same unknown quantity: 1.195 inside the $12
planning figure, 1.55 as the thing being retired, and 2.0 as the allowance
for costing the slice. None is measured, and the document does not say
there are three.

**What would close it:** say that the $12 planning figure is the ledger's
own planning number and carries no derivable premium, since it predates
these architectures; quote the ruling's 1.55 as the ruling's figure for a
full-versus-twin comparison, with the record that produced it named or
recorded as absent; and keep the 2-times slice allowance where it is,
clearly labelled, as it already is.

**A note on the $12 figure itself, ARGUED.** The line it is cited to reads
"Registered training, 5 seeds × full+twin | ~$2 (10M) / ~$12 (30M) / ~$120
(100M)". Read literally, that row is a phase of ten runs, not one run. The
per-run reading is almost certainly right — the 2026-09-17 row gives a
per-run band of "$9–13 each" — but a reader checking the citation cannot
get there from the row named. Cite the $9–13 band instead.

### RT-176 — $175 against a $130 cap the document names as its own bound. **SERIOUS. MEASURED.**

The preamble says: "Item 4 of the same ruling set a spend cap of $130."
Section 16 lists that ruling as "The ruling that authorises and bounds it:
… items 4, 5 and 7". The ruling says it plainly:

```
$ sed -n '30,32p' docs/rulings/2026-09-20-december-result-roadmap.md
4. **Successor spend cap: $130**, within the MVM-0a $400 envelope, with the
   seed fallback (two seeds on the constructed arms, three on the free arm) if
   the 3.5× RunPod billing anomaly of 2026-08-08 recurs on the first pod.
```

Section 12 then itemises $32 plus $143 and reconciles it against the
$174.30 of headroom and against the $400 ceiling, and never against the
$130. The number appears three times in the document: once in the preamble
as the cap, once inside "$130.30" of leftover headroom, and once in
decision 7's alternative (c), where "hold the roadmap's $130" is offered as
a way to buy the weaker two-arm design. Nowhere does the document say that
the plan it recommends is $45 more than the cap it names.

The ruling of 2026-09-21 replaced the flat cap with two releases, and a
reader can infer the $130 lapsed with it — but that ruling never says so,
and this document still cites item 4 as a bound. John's standing rule on
spend is the one that decides it:

```
$ sed -n '48,55p' docs/rulings/2026-09-20-december-result-roadmap.md
## Standing rule on spend (new, applies to every MVM decision from here)

When a plan, a proposal or a session finds that the right next step costs more
than the cap in force, the recommendation says so and proposes the increase,
with the number and what it buys. A cap is a gate for John's ruling, never a
reason to route around the step, shrink it silently, or call it impossible.
```

The rule's familiar failure is a step shrunk to fit a cap. This is the
mirror image: a cap allowed to fall away without a ruling. The rule's
remedy is the same in both directions — the number reaches him.

**What would close it:** one sentence in section 12.2 saying whether item
4's $130 cap is superseded by the two-release ruling and by which words;
and if it is not superseded, an explicit request in decision 7 to raise it
to $175, with what the extra $45 buys.

### RT-177 — the one permitted re-run is paid for twice under decision 7's named alternative. **SERIOUS. MEASURED.**

The re-run appears in two places. Section 12.3 lists it under "What the
first release deliberately does not cover … All four belong to the second
release", and section 12.4's table carries "One permitted re-run … **$12**"
inside the $143. Decision 7's alternative (a) then offers to "fold the one
permitted re-run into the first release now, making it about $44".

If (a) is ruled and the second release's table is left as written, the two
releases are $44 plus $143, which is $187 rather than $175, and the overrun
against $174.30 is $12.70 rather than $0.70. The document nowhere says that
ruling (a) requires the second release to drop to $131.

The same ambiguity sits in the recommendation itself, which is that the
re-run "is asked for as a small separate release when and if S4's first
half happens" — while remaining a line inside the second release. Whether
that separate ask is drawn from the $143 or added to it is not stated.

**What would close it:** state in decision 7 that the re-run is counted
once, and give both totals — $32 plus $143 under the recommendation, $44
plus $131 under alternative (a) — so that whichever John rules, the pair
still comes to $175.

### RT-178 — the cost of the most likely outcome is stated two ways. **SERIOUS. MEASURED.**

- Section 3: "Section 11 places a stop before the expensive wave so that an
  R3 costs about $32 rather than about $140."
- Stop condition S4: "Outcome R3. **About $44 spent**: the first release's
  $32 … plus about $12 for the re-run".
- Weakness W5: "makes that outcome cost about $44".

Section 3's own definition of R3 settles which is right: "One or more arms
fail the learn-both gate **after the one permitted re-run**." R3 cannot be
reached without paying for the re-run, so $32 is not a price R3 can have.
The $32 figure also appears in the ruling of 2026-09-21 (item 12), so it
will propagate if it is not corrected here.

This matters more than a dozen dollars. Section 3 offers $32 as the
reassurance that the most likely outcome is cheap, $44 is what the same
document's stop condition expects to pay, and $12 of that $44 is the one
amount section 12.3 flags as having no authorisation behind it.

**What would close it:** one number, used in all three places, with the
re-run named.

### RT-183 — the rented slice's pass rule assumes three shutdowns; the cost table buys one. **WORTH-NOTING. MEASURED.**

Rehearsal item R-11's pass condition is three log lines, "All three, in
that order, on at least one of the three arm slices". Its cost table, in
section 12.3, has one start-up line (15 minutes, "push, remote pre-flight
self-tests run on the machine, three model builds") and one shutdown line
(5 minutes, "Shutdown handshake on a normal finish"), totalling 46.88
minutes for all three arms together — one machine, started once, shut down
once. Section 10 says as much: "About three quarters of an hour of machine
time for the three arms together."

One machine that finishes once gives the handshake one chance, not three,
and R-11's failure branch ("A failed shutdown half does not halt the
rehearsal") then has no second attempt inside the same slice — which is
what the separate re-launch line is for. The worst-case row, "Laptop asleep
on both, so each pays the bounded wait of 30 minutes", is consistent with
one handshake per slice and inconsistent with three per slice.

**What would close it:** say whether the slice is one machine running three
arms in sequence (one handshake, one chance, with the re-launch as the
second) or three machines (three handshakes, and a start-up cost three
times the 15 minutes budgeted). The cost table currently answers the first
and the pass rule the second.

---

## Part 4 of the brief — over-reading, and the three arms

### On weakness W1, which the brief asked me to judge. ARGUED, and it holds.

The proposal's own W1 is the honest statement the brief asks for, and it is
stronger than most documents of this kind manage:

> They differ in architecture, in parameter count within the size band, in
> how they route information. Anything that separates them is confounded
> with degree. … they do **not** establish that the measure responds to
> integration and to nothing else. Consequently arm F's reading is "where
> arm F sits between two constructed anchors on this measure", and never
> "arm F's integration is *d*".

That is the hedge in the words the brief asks for, and section 5.2's "Why
the fallback is weaker, said plainly" carries the same discipline into the
two-arm case, including the sentence that without arm C "nothing would
establish that the measure *scales* rather than merely *detects*". Decision
3 declines the circular alternative — training arm C against the instrument
that will measure it — for the right reason and says so. I found no place
in the document where the hedge is loosened.

Two things I would still say against it, neither fatal.

**The hedge is not on the frozen list.** Section 7.4 freezes "the
predictions: arm T near zero, arm C high, arm F unknown and not predicted",
but it does not freeze the sentence in which arm F's reading may be
reported. This programme's recorded failure mode is a caution thinning
across successive documents — ledger item RT-171, the credit for a sentence
that names what it refuses, makes exactly that point. W1's recommendation
that "the hedge is not loosened at any later point" would be worth more as
a frozen reporting rule than as a recommendation.

**RT-172 bears on W1 directly.** If the reading's top of scale is
arm-dependent, then "where arm F sits between two constructed anchors" is
not a well-defined position, because the two anchors are not on the same
scale as each other or as arm F. Closing RT-172 is a precondition for W1's
hedge meaning what it says.

### RT-180 — three human gates between the first run and the remaining eight. **SERIOUS. ARGUED.**

The staggered launch is the right call and I would not argue against it.
What is not costed is what sits between its two halves. Before the
remaining eight runs can launch, all of the following must happen in order:

1. the first arm F run completes its full token budget and is scored on the
   learn-both gate;
2. rehearsal item R-11's measured seconds per step are turned into a
   repriced request (item R-7), and John rules a second release that "does
   not exist until he rules on it" — stop condition S5 makes launching
   against an unruled release forbidden;
3. the rented account is topped up, because section 12.6's per-wave funding
   rule means the account physically does not hold the money until someone
   deposits it: "The first release's $32 is an authorisation, not a
   deposit."

Two of those three wait on John being at a keyboard. The proposal prices
the whole stagger at "Cost: about a day of schedule", and justifies it by
slack in the plan. That justification is the one thing here I am confident
is unavailable: the plan is being re-expressed in dependencies rather than
in slack, and a day of slack is not a dependency.

The backstop that stays — registered runs launched by 2026-11-01 — is what
this lands on. If the first run fails its gate, the sequence becomes: score
it, ask for a separate release for the re-run (decision 7's
recommendation), wait for that ruling, top up, re-run, score it, then the
second-release ruling and another top-up. That is four human gates and
roughly twenty hours of machine time before the eight can launch, against a
backstop that does not move.

**What would close it:** express the gap between the staggered run and the
remaining eight as its dependencies — result read, release ruled, account
funded — and say what happens to outcome R4 if those dependencies are not
met by the backstop date. At present R4 is defined as "runs not launched by
2026-11-01" without saying whether the staggered first run counts as "runs
launched".

---

## Smaller findings

### RT-184 — the shutdown method note is on the main line. **WORTH-NOTING. MEASURED.**

Twice — in rehearsal item R-11 and in section 16 — the document says the
method note is "currently on branch `worktree-reap-race-fix` and not yet on
the main line", and once adds "a reviewer checking this citation needs that
branch". It was merged eighteen seconds before this commit was written:

```
$ git log -1 --format="%H %ci %s" dd1b974
dd1b97479020bad3f0f34b2bf4e98c18d8768504 2026-09-21 20:09:52 -0700 Merge pull request #15 from jfredson/worktree-reap-race-fix
$ git log -1 --format="%H %ci %s" d8ceba9
d8ceba97243b72c1cbc42b7e25bc984a126ca5a0 2026-09-21 20:10:10 -0700 Successor proposal: the rehearsal buys a rented slice, …
```

Harmless in itself; recorded because the instruction sends a reviewer to
look in the wrong place, and because this document elsewhere corrects an
identical "recorded as owed and not yet on disk" statement about the ruling
file, which is the right habit to apply here too.

### RT-185 — a ruling's figure misquoted, and the gap then explained away. **WORTH-NOTING. MEASURED.**

Section 12.5: "gives **about $326** — the figure John's ruling cited as
about $328, the same arithmetic to a dollar of rounding."

```
$ grep -n '32[0-9]' docs/rulings/2026-09-21-review-verification-and-staged-spending.md
75:    spends about $326, which is more than the programme has left. Halting on the
```

The ruling says $326. The two figures agree exactly; the document invents a
two-dollar disagreement and then reassures the reader about it. Small, but
it is the class of defect the closure rule exists for — a sentence about a
record that the record does not support — and it is the second citation in
the document pointing at the right file and the wrong contents (see
RT-174).

### RT-186 — two failures merged into one in decision 13. **WORTH-NOTING. MEASURED.**

Decision 13's alternative speaks of "the one failure which has already
destroyed a ten-hour run and cost $97.04 (method note, section 2)". The
method note's section 2 says:

> That is how $97.04 was lost on 2026-08-12.

The 2026-08-12 loss is the compute ledger's 2026-08-09/10 row: a **29.5
hour** run on a different machine class, lost because the terminate-after
backstop never fired and no fetch happened at all. The ten-hour run is the
control-learnability pilot of 2026-09-19, which lost nothing — its
checkpoint was recovered the next day for $0.067, and the ledger's
2026-09-20 row closes it as recovered and checksum-verified. Neither event
is "destroyed a ten-hour run and cost $97.04", and the method note does not
say it.

**What would close it:** "the failure class that lost $97.04 on 2026-08-12
and left a completed ten-hour run stranded on a network volume on
2026-09-19".

### RT-187 — bare identifiers and unglossed terms. **WORTH-NOTING. MEASURED.**

The document opens by promising "no bare identifier anywhere", and is
mostly very good about it — every rehearsal item, stop condition, weakness
and outcome carries its plain sense, and ledger items RT-17, RT-21, RT-58
and RT-59 each carry a phrase saying what they found. Four exceptions:

- **"ledger items RT-52 to RT-69"** (section 3), carrying no phrase at all.
  This is the exact pattern ledger item RT-170 ruled on earlier the same
  day — "Bare identifiers in registered text: … 'ledger RT-120 to RT-142'"
  — accepted, with the reason that such text "outlives the session that
  wrote it".
- **"L2(a)"** (section 7.3), also named in RT-170's list, used here with no
  plain gloss beyond "the matched control".
- **"EU-RO-1"**, three times: a rental-region code with no plain phrase. It
  is load-bearing, since it names the venue the whole cost model rests on;
  "the vendor's Romanian secure region" or similar costs four words.
- **"paired uncertainty"** (seven times) and **"family correction"**
  (twice) are terms of art that section 1's word list does not define,
  though section 1 is careful to define the running state, fitted
  straight-line reads and transplanting. "Family correction" in particular
  is the kind of phrase the rule targets: an ordinary reader cannot tell
  from it that it means an allowance for having searched many places at
  once.

Also **"low-rank direction"** (W3) and **"the same norm"** (7.3.3), each
once and each avoidable.

**One smaller inconsistency, recorded here rather than as its own item.**
Section 12.3 says the $7 left inside the rehearsal's $10 covers items R-1
to R-10, "all of which are specced to run locally on the Mac at no cost".
Section 10 does not spec them that way: "run locally where the Mac's
throughput allows and on the cheapest rented machine where it does not".
The $7 residue is a budget line, not an established saving.

### RT-188 — what held. **WORTH-NOTING (CREDIT). MEASURED.**

Recorded so that the findings above read as findings and not as a pattern.

**The rented slice's arithmetic reproduces exactly, including its own
declared rounding gap.**

```
$ python3 -c "
r=0.99/60
lines=[('arm F',500*0.645/60),('arm T',500*1.29/60),('arm C',500*1.29/60),('start-up',15),('shutdown',5)]
tot=0
for n,m in lines:
    print(f'  {n:<9} {m:6.2f} min  {m*r:.2f}'); tot+=m
print(f'  total     {tot:6.2f} min  {tot*r:.2f}  (per-line sum 0.78)')
print(f'  worst case, two slices: {2*(tot+25):.0f} min  {2*(tot+25)*r:.2f}')
"
  arm F       5.38 min  0.09
  arm T      10.75 min  0.18
  arm C      10.75 min  0.18
  start-up   15.00 min  0.25
  shutdown    5.00 min  0.08
  total      46.88 min  0.77  (per-line sum 0.78)
  worst case, two slices: 144 min  2.37
```

Every figure in that table — the 46.88 minutes, the $0.78, the $2.37 worst
case, and the footnote explaining that the one-cent gap is rounding
"recorded rather than tidied away" — is correct. The two lines that are
allowances rather than measurements are marked as allowances, which is the
standard section 12.3 sets for itself and, apart from the development-runs
line (RT-174), meets.

**The headroom and the overrun are right.** $400 minus $225.70 is $174.30,
and the compute ledger's 2026-09-20 row carries "programme running total
~$225.6 + $0.07 = ~$225.7 / $400". $32 plus $143 is $175, which is $0.70
past $174.30. The document states that as a finding rather than absorbing
it, names the only three ways to answer it, and refuses to choose among
them before the measurement exists. That is the right call and it is the
behaviour the two-release ruling was meant to produce.

**The halt-not-trim arithmetic is right.** Seven runs at $42 is $294; plus
$10, $10 and $12 gives $326; that is 81.5% of $400 and $151.70 more than
$174.30. The document's "82%" and "$152" both check out.

**Every figure taken from the shutdown method note is in the note.** The
one-second window inside a ten-minute cycle (section 1); the two minutes
nineteen seconds for 336MB, the five-minute expected handshake and the
thirty-minute bounded wait (section 4); the twenty-six checks with a
negative control (section 9); the three passing signals, the `grace ran
out` failure signal and the "few cents" toy-run price (section 10) — all
verified by reading the note. So is the standing rule on spend, quoted
verbatim and correctly in section 12.3.

**The 0.645 seconds per step is exactly where the document says it is.**
The ledger's 2026-09-15 row reads "55,116 steps / 585,552,384 tokens, 9.83h
training at 0.645 s/step" on "RTX 5090 SECURE EU-RO-1 $0.99/hr". The
foundational measurement of the whole cost model checks out, and the
document's insistence that only another rented number can move it is
correct and well argued.

**Section 12.1 is the best thing in the document.** It records an error of
its own making — "Version 1 had the sign of its own margin inverted, and
the number it reported as spare was the number it was over by" — inside the
document rather than by deleting it.

---

## The kill case, in one paragraph

This proposal should not go to John as it stands, and the reason is not the
money. Sections 6.3, 6.4 and 7.3 define a measure whose central number
divides by a quantity with a per-arm ceiling and never subtracts the floor
it names, and whose discriminating control asks for a cell that the grammar
it inherits makes empty by an enforced assertion — with a sanity rule
attached that declares the instrument broken precisely when the models have
learned the task. Those are the two failures this programme has already
paid for, in new clothes: a comparison whose denominator was never
attacked, and a pre-stated cell nobody tried to populate before it was
registered. The document knows the history — it cites the zero-denominator
finding in the very section where it repeats the shape — and that is the
strongest evidence that reading carefully about a failure is not the same
as checking for it. Everything else here is repairable in an afternoon: the
wrong ledger row, the 1.55 that belongs to a different comparison, the cap
that fell away without a ruling, the outcome priced at $32 in one section
and $44 in two. But a proposal that goes to John now asks him to rule
thirteen design decisions on a measure that, on this reading, cannot mean
what section 6.3 says it means. Fix the denominator and the control cell
first; the rest of the document is good enough that it will survive the
repair.

---

## What this review did not do

- **It did not open the drafting session's context**, any chat transcript,
  `STATUS.md`, or any uncommitted file. It did not consult the author.
- **It ran no compute, rented no machine and spent no money**, and made no
  change to any file other than this one.
- **It did not verify the successor grammar**, which does not exist. Every
  statement about the grammar's behaviour is about `curriculum_a3.py`, the
  generator the proposal says the new one extends, and is labelled as such.
- **It did not raise findings about calendar weeks or schedule slack**, on
  instruction: that language is being converted to dependencies in a
  separate session. RT-179 and RT-180 are dependency findings and are meant
  to survive that conversion.
- **It did not check the roadmap's own $130 arithmetic** ($10 plus $10 plus
  $110 plus $12 is $142 against a $130 cap), which is a defect in
  `docs/december-result-roadmap-2026-09-20.md` and not in the target.
- **It did not attempt the reviewer-owned verification that tier 1 owns at
  Gate A**, which is a different obligation attaching to the registration
  pass. This is a Gate C pass and the protocol asks only for the fixed
  brief here.
