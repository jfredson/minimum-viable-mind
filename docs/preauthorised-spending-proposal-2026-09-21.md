# Pre-authorised spending for the successor experiment

*Proposal, 2026-09-21 (Pacific). Drafted by a Claude Code session in its own
worktree, for John to rule on once. Nothing here has been spent, launched or
rented; this is a document. Written under the workspace plain-language rule
(`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30) and under the standing rule on
spend in `docs/rulings/2026-09-20-december-result-roadmap.md`, which says that
when the right next step costs more than the cap in force, the recommendation
says so and proposes the increase with the number.*

*This proposal goes to Gate C of `docs/outside-review-protocol.md` — a review
pass attached to the proposal before it reaches John — so it is written to be
attacked. Every measured number cites the file it came from by name, because
the protocol's closure rule makes an uncited measured claim a fatal finding on
its own. Every judgment call is flagged, with the strongest case against it
named next to it.*

**"Pre-authorised" means one ruling given in advance that covers several
purchases, instead of a separate spoken go before each one.** That is the whole
of the idea; everything below is about where the line should sit.

---

> **Note added afterwards, 2026-09-21, by a later Claude Code session — not
> John's ruling, and not part of the proposal, which is left unedited below.**
> Section 1.3, and **item 7 of section 7**, say the project's structured status
> file (`data/project.toml`) still carries the old spend figures. It has since
> been corrected, so **item 7 needs no ruling: it is already satisfied.** Items
> 1 to 6 are untouched. The dates, commit names and exact figures are in "Note
> added afterwards: the detail" at the end of this document.

> **Second note added afterwards, 2026-09-22, by a later Claude Code session —
> not John's ruling, and not part of the proposal, which is still left unedited
> below.** The envelope position measured in section 2 has moved by $1.90 and
> this one does change numbers. The two follow-up reading runs of 2026-09-20
> were recorded as costing nothing; they cost a measured $1.9040, and the
> compute ledger carries the correction. **The programme has spent about
> $227.60 of $400, leaving about $172.40, not $174.30**, and Amendment A3 stands
> at about $46.20 of its $100 stop, leaving about $53.80. Every finding in this
> proposal survives and each one gets slightly worse: the successor still does
> not fit the envelope, and the gap is $1.90 wider at every configuration in the
> table in section 3.5. The derivation and the knock-on figures are in "Second
> note added afterwards: the detail" at the end of this document.

---

## 0. What this asks John to do, in one page

The December-result roadmap (`docs/december-result-roadmap-2026-09-20.md`)
runs the successor experiment from the week of 2026-09-28 to the week of
2026-11-02. Under the practice in force, that stretch needs John to say "go" in
his own words at least eight separate times: once for the rehearsal, once for
the small development runs, once for each launch wave of the nine registered
runs, once for the one permitted re-run, and once for each file-copy recovery
pod. The recent record shows what that costs in real time — five separate gos
inside six days, on 2026-09-15, 2026-09-16, 2026-09-17, 2026-09-19 and
2026-09-20, every one of them quoted in `compute-ledger.md`.

This proposal asks for four things.

1. **A correction.** The $130 cap in section 6 of the roadmap does not cover
   its own stated contents. Its four listed items sum to $142. It is $12 short
   before any billing surprise, and the "anomaly margin" it claims to hold is
   a negative number. Confirmed below, and two further citation errors in the
   same paragraph are confirmed with it.
2. **A new cap: $225**, with every line justified from measured rows in
   `compute-ledger.md`, against a proposed rise in the programme envelope from
   $400 to $460. The successor as designed does not fit the current envelope at
   any seed count that preserves three arms. That is the finding, stated rather
   than worked around.
3. **A pre-authorisation scheme**: five kinds of purchase pre-authorised with
   per-item ceilings, six kinds that still need John's own words, five that are
   never pre-authorised. Crucially, this needs **no change to the corrigibility
   commitments** — commitment C2 already provides for a go covering "a specific
   registered batch", and that provision has simply never been used.
4. **A billing tripwire** that is a mechanical check rather than a person
   noticing, because pre-authorisation removes the person. The arithmetic below
   shows the roadmap's existing fallback — drop a seed from each constructed
   arm — does not protect the cap and was never a spend control.

---

## 1. The cap arithmetic problem

### 1.1 The $12 shortfall is real

Section 6 of `docs/december-result-roadmap-2026-09-20.md` reads, in full:

> Proposed cap for the successor: **$130**, covering rehearsal (up to $10),
> development runs (up to $10), nine registered 30M runs (about $110) and one
> re-run (about $12) with the balance as the anomaly margin.

The four items sum to $142:

| Item | Roadmap figure |
|---|---|
| Rehearsal (week 40) | $10 |
| Development runs at 10 million parameters (week 42) | $10 |
| Nine registered 30-million-parameter runs (week 43) | $110 |
| One permitted re-run (week 44) | $12 |
| **Sum** | **$142** |

$142 against a $130 cap is **$12 over**. The sentence's own closing clause —
"with the balance as the anomaly margin" — describes a balance of **minus $12**.
The margin does not exist. **The claim in the brief I was given is confirmed.**

Taking the nine runs as exactly nine times the $12 per run the roadmap names
(that is $108, not "about $110") makes the sum $140 and the shortfall $10. The
cap is over either way.

### 1.2 The one reading that softens it, and why it still fails

The strongest defence of the roadmap's number, and it deserves to be stated
because a Gate C reviewer will find it: two of the four lines are written as
ceilings, not expectations. "Rehearsal (up to $10)" and "development runs (up to
$10)" are maxima. Section 4 of the roadmap prices the rehearsal as "~$0 to $10".
If the rehearsal costs nothing and development runs cost $5, the sum is $127 and
$3 of margin exists.

Three reasons that does not rescue the number.

- **A margin that only exists if two lines come in at zero is not a margin.** It
  is a hope about two lines, offered as protection against a risk on a third.
- **The line most likely to move is the nine runs, and it moves upward.** See
  §3.2: two of the three arms are, by construction, more expensive per run than
  anything the ledger has measured, and the roadmap prices all nine identically.
- **The $12-per-run figure is sourced wrongly.** The roadmap attributes it to
  "the ledger's $12 per run". The ledger's phase budget guide prices
  "Registered training, 5 seeds x full+twin" — that is ten runs — at "~$12 (30M)"
  in total, and the ledger's own 2026-08-12 reconciliation note flags that guide
  as **known-stale**: "it prices the 5-seed 30M at ~$12, but the measured 30M
  pilot alone cost ~$97". The roadmap's per-run number happens to land close to
  what the ledger's recent rows actually measure (§3.1), but it does not come
  from where the roadmap says it comes from, and under the closure rule of
  `docs/outside-review-protocol.md` that is a citation that does not hold.

### 1.3 Two further errors in the same paragraph

Both were found while checking the above, and both are in John's favour to know
before he rules again on a number.

**The envelope figure is stale by $10.** Section 6 says "The program envelope is
$400 (raised 2026-08-16; $215.70 spent per data/project.toml), with about $184
unspent as of 2026-09-20." The arithmetic is internally fine — $400 minus
$215.70 is $184.30 — but the input was already out of date when it was written.
`compute-ledger.md` now carries a correction on its 2026-09-19 row, made
2026-09-21 on a Gate A finding: "this row had carried the pre-run figure". The
corrected chain runs ~$215.70, plus ~$9.90 for the control-learnability pilot of
2026-09-19, plus $0.067 for the checkpoint recovery of 2026-09-20, to
**~$225.70**. Unspent headroom is **$174.30**, not $184. `data/project.toml`
still carries the stale 215.70 in its `[[spend.lines]]` block and should be
corrected in the same session that lands any ruling on this proposal.

**Closing Amendment A3 does not release money into the pool.** Section 6 says
"A3's own $100 stop has about $56 left and A3 closes, so its remainder returns
to the program pool." A3's spend is already inside the $225.70 — every A3 row in
`compute-ledger.md` carries both totals side by side, for example the 2026-09-17
row's "$14.21 + $20.1 → $34.31 / $100 A3 stop" alongside its corrected
"~$195.6 + $20.1 = ~$215.7 / $400". A3's unspent $55.70 was never spent, so it is
already part of the $174.30 of headroom and returning it creates nothing. The
sentence reads as if $56 becomes newly available. It does not. **Headroom is
$174.30 whether or not A3 closes.**

---

## 2. The envelope position, measured

All figures from `compute-ledger.md` unless stated. The ledger's running-total
column is self-consistent across its rows and I have followed its own chain
rather than re-deriving a total from the individual actuals, which are a mix of
console-reconciled, balance-implied and computed-from-wall-clock figures.

| Measure | Amount | Source |
|---|---|---|
| Programme envelope (Amendment A2, raised from $200 on 2026-08-16) | $400.00 | `compute-ledger.md`, 2026-08-16 top-up note and 2026-08-15 row |
| Programme spent to date | ~$225.70 | `compute-ledger.md`, 2026-09-20 checkpoint-recovery row |
| **Programme headroom** | **~$174.30** | arithmetic on the two above |
| Amendment A3 hard stop | $100.00 | `compute-ledger.md`, 2026-09-14 row onward |
| A3 spent | ~$44.30 | `compute-ledger.md`, 2026-09-20 row |
| A3 remaining (inside the headroom above, not additional to it) | ~$55.70 | arithmetic |
| RunPod prepaid balance | $79.82 | `data/project.toml` `[spend]`, as of 2026-09-20 |
| Account spend limit John set | $80 | `data/project.toml` `[spend]` |
| Money lost to pods billing after they finished | ~$10.30 across four occasions | `compute-ledger.md`, 2026-09-19 annotation |

**What the successor at $130 leaves.** Authorised in full and spent in full,
$225.70 + $130.00 = $355.70, leaving **$44.30** of the $400 envelope. That fits.
The roadmap's cap is affordable; it is simply not enough to buy what the
roadmap says it buys.

**One thing worth naming here, because it matters for §4 and §5.** The account
holds $79.82 and John's own limit on it is $80. Neither the roadmap's $130 nor
the $225 proposed below can be spent without John topping the account up by
hand, more than once. `compute-ledger.md` rule 5 calls this the hard backstop:
"the RunPod account is funded by prepaid credits with auto-reload OFF... The
account physically cannot overspend what the ledger permits." **The top-up, not
the spoken go, is the load-bearing human gate on this programme's money**, and
this proposal does not touch it.

---

## 3. A proposed cap

### 3.1 What a run actually costs, measured

Three recent 30-million-parameter runs on the registered venue (RTX 5090 secure,
data centre EU-RO-1, $0.99 an hour), all from `compute-ledger.md`:

| Run | Pod time | Cost | Note |
|---|---|---|---|
| Control-learnability pilot, 2026-09-19 | ~10.0h | ~$9.90 | Zero idle billing, the first run in the programme's history with none |
| Seeds 1 and 2 together, 2026-09-17 | 20.28h | $20.08 | ~$10.04 each; ~$0.76 idle across the pair |
| A3 Gate 2 pilot, 2026-09-15 | — | $13.92 | Includes $3.80 of idle billing; ~$10.12 without it |

**A clean 30-million-parameter run costs about $10.20**, and I use that figure
below. It is the top of the measured range plus a few cents for the minute or
two between pod creation and the watchdog starting, which the 2026-09-17 row
notes is not in its arithmetic.

### 3.2 Why two of the three arms will cost more, and by how much

*This is the largest judgment call in the document and I want a reviewer to hit
it first.*

The roadmap prices all nine runs the same. But section 3 of the roadmap
specifies three architectures, not one. Arm F (free) is an ordinary transformer
and is the closest thing to the runs measured above. Arm T (tracker by
construction) adds "an explicit agent-item-value table and a separable pointer
slot". Arm C (entangled by construction) adds "multiplicative conditioning of
every block's residual stream". Both add work inside the forward pass.

The programme has measured exactly this kind of premium once. In Amendment A2,
the register-bearing model and the register-less twin were the same size on the
same task, differing by the architectural self-register and the work of enacting
it. From `compute-ledger.md`:

- Wave 1, 2026-08-16: twin 0.35 seconds a step, full 0.53 — a ratio of **1.51**.
- Wave 2, 2026-08-17: twin 0.34 seconds a step, full 0.54 — a ratio of **1.59**.

Mean **1.55**. Applied to the $10.20 base, a constructed arm's run costs about
**$15.81**.

Nine runs, three seeds on each of three arms:

- 3 free runs at $10.20 = $30.60
- 6 constructed runs at $15.81 = $94.86
- **Total $125.46**

Against the roadmap's $110 for the same nine runs, that is $15.46 more.

**The case against this number, stated as strongly as I can make it.** The 1.55
ratio was measured on a different architectural addition, on a different task
grammar, on an earlier codebase. Arm T's table lookup is cheap and may cost
almost nothing; arm C's per-block conditioning is a handful of extra elementwise
operations on a tensor already in memory and might be under 10%. Neither arm
exists yet, so 1.55 is an inference from a precedent, not a measurement of the
thing. If both constructed arms in fact run at the free arm's pace, nine runs
cost $91.80 and the roadmap's $110 was generous, not tight.

**How to settle it rather than argue it:** section 4 of the roadmap already
schedules the week-40 rehearsal to measure "throughput of the new grammar". I
propose that the rehearsal is required to report measured seconds-per-step for
all three arms, and that the nine-run line is re-costed from those measurements
and recorded in the ledger before the registration commit of 2026-10-11. The cap
is a ceiling, not a budget to exhaust: if the rehearsal measures cheaper arms,
the money is not spent and the ledger records the lower figure.

### 3.3 Three costs the roadmap's cap omits entirely

**Storage.** The network volume the runs read and write, `mvm-models-ro`, is
100 gigabytes in EU-RO-1 at about $7 a month (`compute-ledger.md`, 2026-08-16
row). It drips continuously whether or not a pod is running — the ledger's
2026-09-19 annotation records deleting the *other* volume precisely because it
had been "dripping about $0.014/hr (roughly $10.50/mo) against the account since
2026-08-12". Across the successor's active window, roughly the week of 2026-10-12
through the week of 2026-12-07, that is about two months: **$14**.

*Judgment call, flagged:* the volume exists and is billing today regardless of
whether the successor is authorised, so charging it to the successor's cap is
arguably double-counting programme overhead. **The alternative** is to carry it
as a separate standing line against the envelope, outside the successor cap. I
prefer charging it in, because a cap that omits a cost the experiment cannot
avoid is how the $130 got into trouble, but John may reasonably rule the other
way and the cap then drops to $211.

**Checkpoint recovery pods.** The 2026-09-19 row documents a defect that is not
bad luck: the trainer deletes its own pod when it finishes, and it now races the
laptop watchdog's final fetch. The ledger states it plainly — "This will recur on
every future run that finishes normally". Each recovery is a file copy on the
cheapest available pod and the one measured on 2026-09-20 cost **$0.067**. Nine
runs plus development runs: budget **$1**.

**Idle billing.** Finished pods that go on billing because nothing reaped them
have cost ~$10.30 across four occasions (`compute-ledger.md`, 2026-09-19
annotation). The pod-side reaper that would end this was armed in production for
the first time on 2026-09-19 and worked — zero idle on that run. But the
programme has been here before: the same ledger records that a pod **cannot**
delete itself without a credential placed on it (2026-09-16 row), that the
laptop watchdog "is the ONLY reap" historically, and that three of the four
occasions were a laptop sleeping. Budget **$8** across nine runs — below the
historical rate, above the zero that one good run would tempt.

### 3.4 The proposed cap

| Line | Amount | Basis |
|---|---|---|
| Measurement rehearsal, week 40 | $10.00 | roadmap §4, unchanged |
| Development runs at 10M parameters, week 42 | $10.00 | roadmap §4, unchanged. For scale, the 10M pilot of 2026-08-09 trued up to $1.943 (`compute-ledger.md`, 2026-08-12 reconciliation), so this buys three or four |
| Nine registered 30M runs (3 free at $10.20, 6 constructed at $15.81) | $125.46 | §3.1 and §3.2 |
| One permitted re-run, priced as a constructed arm | $15.81 | roadmap §4 week 44; priced at the worst arm, not the cheapest |
| Network volume `mvm-models-ro`, ~2 months at ~$7/mo | $14.00 | §3.3 |
| Checkpoint recovery pods, up to 10 at $0.067 | $1.00 | §3.3 |
| Idle-billing allowance | $8.00 | §3.3 |
| Billing-anomaly margin | $40.00 | §5.4 — this is exactly the exposure the tripwire permits before it halts |
| **Proposed cap** | **$225** | rounded up from $224.27 |

**Sensitivity, so John can see the shape of the number.** If both constructed
arms run at the free arm's pace, every line above recomputes to about **$171**.
If the anomaly margin is set to zero and the funded balance is relied on instead
(§5.5), the nine-run cap is about **$184**. The $225 is the honest ceiling under
the measured precedent, not a prediction of what will be spent.

### 3.5 The envelope position after it, and the ask that follows

$225.70 already spent plus a $225 cap is **$450.70**. The $400 envelope does not
hold it. Under the standing rule of 2026-09-20 I am required to say so and
propose the increase with the number rather than shrink the experiment quietly,
so:

> **Proposed: the MVM-0a programme envelope rises from $400 to $460.**

At full draw that leaves $9.30. That is not a margin and should not be described
as one; it is the rounding. If John wants the envelope to hold a real remainder,
the number is $475 and I would rather he chose it deliberately than that I
padded it here.

**This is not a cap problem that a smaller experiment solves.** I checked:

| Configuration | Successor cost | Fits $174.30 headroom? |
|---|---|---|
| Nine runs (3 per arm), with anomaly margin | $224.27 | No, over by $49.97 |
| Seven runs (3 free, 2 each constructed), with margin | $192.64 | No, over by $18.34 |
| Six runs (2 per arm), with margin | $182.45 | No, over by $8.15 |
| Six runs (2 per arm), no anomaly margin at all | $142.45 | Yes, leaves $31.85 |

So the design fits the current envelope only at two seeds an arm **and** with
the anomaly margin deleted. Two seeds an arm is thin for what outcome R1 in
section 2 of the roadmap requires — "a reading with paired uncertainty across
seeds" — and deleting the margin is what section 6 already did by accident. That
is the case for raising the envelope rather than cutting the experiment, and it
is the recommendation.

**The strongest alternative, named:** hold the envelope at $400, run six
registered runs (two seeds an arm), carry no anomaly margin, and accept that the
first billing surprise stops the experiment rather than being absorbed. That is
a coherent, defensible choice — it keeps a ceiling John already ruled, and a
stopped experiment with a registered reason is outcome R3 and still a result. I
do not recommend it, because the seed count is the thing the result definition
leans on and the margin is the thing that lets a surprise be survived rather
than fatal. But it is a real option and John may prefer it.

---

## 4. The pre-authorisation scheme

### 4.1 What is being replaced

Under the practice the ledger records, the successor needs John's own words at
least eight times between the week of 2026-09-28 and the week of 2026-11-02: the
rehearsal, the development runs, five launch waves at two pods concurrent, and
the one permitted re-run — plus a go for each recovery pod, of which 2026-09-20
is the precedent. The five gos of 2026-09-15 through 2026-09-20, all quoted in
`compute-ledger.md`, show what that costs in elapsed days when John is
available; the roadmap's own week-48 row ("Thanksgiving week; expect John's time
to be short") shows what it costs when he is not.

### 4.2 This needs no change to the corrigibility commitments

Worth establishing before proposing anything, because a reviewer will ask.
Commitment C2 in `spec/corrigibility-commitments.md`, version 1.1, reads: "No
training run starts without John's explicit go for that run **or that registered
batch**", and its condition (a) accepts a go "naming the specific run(s) — seed,
twin/full, scale — **or a specific registered batch**".

**Batch-level authorisation is already inside C2 and has simply never been
used.** Every go in the ledger names individual runs or a single wave. So this
proposal asks John to use a provision he already ratified on 2026-08-16, not to
loosen one.

*One judgment call, flagged because it is the load-bearing reading.* C2 also
says a delegated go "authorizes exactly the named runs, once: it does not carry
over to resumes... re-launches, retries that change venue or recipe, **or any
later wave**." I read "any later wave" as meaning a wave outside the authorised
batch — otherwise the words "or that registered batch" earlier in the same
commitment have no work to do at all, since every batch larger than one wave
contains later waves. **The alternative reading** is that C2 requires a fresh go
per wave regardless, in which case a nine-run batch go is not available under
C2 as written and C2 would need amending to version 1.2 before any of this can
happen. That is John's call on his own text and I am not making it for him. If
he takes the second reading, the amendment is one sentence and the rest of this
proposal is unchanged.

**One hard boundary this proposal does not cross.** C2 also says: "No automation
may launch, extend, or re-launch training on its own; scheduled or unattended
training loops remain out of scope for MVM entirely." Nothing here creates a
script that launches the next wave when the last one finishes. Every launch is
still executed by a Claude session working live, with the batch go standing
behind it instead of a fresh spoken one. **Pre-authorised is not automatic.**

### 4.3 Pre-authorised, with per-item ceilings

All five are conditional on the four mechanical preconditions in §4.6. All five
lapse the moment the tripwire in §5 fires.

| # | What | Ceiling | Conditions |
|---|---|---|---|
| 1 | The measurement rehearsal, week 40 | **$10 total**, no single pod above $2 | Rehearsal work only; no pod above $1.00/hr |
| 2 | Development runs at 10M parameters, week 42 | **$10 total**, no single run above $4 | Registered launcher, registered venue |
| 3 | The nine registered 30M runs | **$16 per run**, **$32 per wave**, **$135 for the nine**, at most two pods running at once | Only after the registration text is committed and its Gate A is closed. RTX 5090 secure, EU-RO-1, posted rate at or below $0.99/hr, confirmed from the pod record before creation and not assumed |
| 4 | Checkpoint recovery pods | **$0.25 each**, at most one per run | Cheapest available secure pod in the volume's region, file copy only, no training. This is the 2026-09-20 operation, which cost $0.067 |
| 5 | The one permitted re-run, if an arm fails the eligibility gate | **$16**, once | Same venue and rate conditions as #3 |

Ceilings 1 through 5 sum to $171 and sit inside the $225 cap; the difference is
the volume drip, the idle allowance and the anomaly margin, none of which is a
purchase anyone decides to make.

### 4.4 Still needs John's own words, every time

1. **Any pod above $0.99 an hour, or in any venue other than EU-RO-1 secure.**
   Venue and rate drift is the single most expensive pattern in this ledger. The
   2026-08-08 billing anomaly happened on a *community* pod. The $97.04 loss
   happened on a pod that "launched 23:54Z at **$3.29/hr** (above the remembered
   $2.99)" — a 10% rate error that the go did not catch because nobody knew it
   yet. Rate is the one number that turns a small mistake into a large one, so
   it keeps a human.
2. **Any account top-up.** John is the only person who can add funds, and under
   §5.5 the size of each top-up is the real ceiling on any surprise.
3. **Any launch after the tripwire has fired**, without exception.
4. **Any run whose estimate would take the successor's cumulative past the
   cap.** This is already rule 2 of `compute-ledger.md` — "A run whose pre-run
   estimate would take the running total past $200 does not launch" — restated
   against the new number.
5. **Restarting or resuming a run that crashed.** C2 names this explicitly ("a
   crash-resume needs a fresh go") and the 2026-08-09 ledger row practised it.
6. **Anything outside the rehearsal, the development runs, the nine registered
   runs, the one re-run and the recovery pods.** Any diagnostic, any unregistered
   pilot, any exploratory run. Precedent: the control-learnability pilot of
   2026-09-19 was unregistered by design and got its own go, with John's words
   changing the run.

### 4.5 Never pre-authorised

1. **Creating or deleting a network volume.** Already outside Claude's envelope
   by precedent — `compute-ledger.md`, 2026-08-16: "volume creation is outside
   Claude's permission envelope."
2. **Placing any RunPod credential on a rented machine beyond the existing
   dedicated reaper key.** The 2026-09-16 row records that widening this "is
   John's call and was not taken"; the 2026-09-19 row records the narrow reaper
   key being armed. Widening it further is a separate ruling.
3. **Turning auto-reload on, or raising the $80 account spend limit.** These are
   the backstop described in rule 5 of the ledger, the one thing that held on
   2026-08-12.
4. **Any spend at all after 2026-12-21**, the ruled wrap-up start.
5. **Any spend that would take the programme past its envelope**, cap or no cap.

### 4.6 Four mechanical preconditions, checked before every pre-authorised pod

Pre-authorisation removes a human reader. These put four checkable things in his
place. Each is drawn from something the ledger already does; none is new
machinery.

1. **The ledger row exists first, with its estimate, committed, quoting this
   ruling as the authorisation.** Rule 1 and rule 2 of `compute-ledger.md`
   already require the row and the estimate before spend. The programme's only
   existing precedent for pre-authorised spend used exactly this — John's words
   on 2026-09-16 were "Write its ledger row before spend quoting this sentence
   as the authorization, delete the pod yourself if self-terminate fails, and
   report the actual cost." That test is the model for this whole scheme.
2. **The funding rule passes**: balance is at least the in-flight estimate plus
   $10, the form C2(c) requires and every recent row records.
3. **Zero pods confirmed immediately before creation**, and the posted hourly
   rate read from the pod record rather than remembered. Both are already
   practice; the 2026-09-19 row is the cleanest example of both.
4. **The tripwire check in §5 has run and returned a number.** A check that
   could not run is a trip, not a skip. See §5.3.

Plus one thing that is not a precondition but a replacement for something real:
**a written notice to John within the hour of each pre-authorised launch** — not
a request, a notice — naming the run, the estimate and the rate. The gos are not
only permission; they are the moments John sees the state of play. Removing the
permission should not remove the visibility.

### 4.7 What is lost by moving the gate

The human gate on spend in this programme is long-standing and load-bearing and
I am proposing to move it, not remove it. Honestly, this is what goes.

- **A second reader of the staging text.** The go is currently the only moment
  another mind reads the description of what is about to run. It has done work:
  John's go of 2026-09-19 was not a "yes" but a correction — "Weight and batch
  split stay as you set them. Confirm zero pods and EU-RO-1 stock right before
  creation, and keep the flag out of launch_a3.sh." Three constraints added at
  the gate. **A committed ledger row is a weaker check than a human reply, and I
  will not claim otherwise.** It catches a missing estimate; it does not catch a
  bad estimate.
- **Five natural pauses.** A go takes hours or days to arrive, and that delay
  has repeatedly been when someone noticed something. Removing it removes the
  pauses as well as the waiting.
- **The chance to change course mid-experiment.** Eight gos are eight chances to
  say "actually, stop". One batch go is one. The tripwire and the kill dates
  are what replace that, and they are narrower: they fire on billing and on the
  calendar, not on a change of mind.

The honest summary is that this trades a small amount of safety for three weeks
of schedule. §6 says how small.

---

## 5. The billing tripwire

The roadmap's week-43 row says: "the 3.5x RunPod anomaly of 2026-08-08 is the
risk; if it recurs, seeds drop to two on T and C, three on F". With spending
pre-authorised there is nobody in that loop, so the check has to be mechanical.
It also has to actually work, and the arithmetic below says the existing
fallback does not.

### 5.1 What the anomaly was

From `compute-ledger.md`, the 2026-08-08 reconciliation note: the pod "bills
**8.47 h against ~2.42 h of pod existence (~3.5x, $5.86 vs ~$1.67 expected)**;
nvidia-smi showed one GPU". The pod was not left running — "deleted 2.4h after
creation, zero pods confirmed; the discrepancy is inside the billed row." John
waived the support ticket the same day and the ledger priced the risk forward:
"5-seed-run estimates below assume the ~3.5x rate may recur". 8.47 divided by
2.42 is 3.50 exactly.

**Two things about it that the roadmap does not say, and that change the risk
picture.** First, it happened on a **community** pod. The very next row, the
2026-08-09 10M pilot, was also a community pod, and the ledger records that "the
08-08 anomaly did NOT recur on it". Second, every pod since 2026-08-15 has been
**secure**, which is the venue the successor uses, and the ledger shows no
billing anomaly on any of them — the 2026-08-12 reconciliation found "no billing
inflation this time" on the H100 row, and the rule-4 check passed to within 8
cents on a $106.88 total. So the anomaly has **one observation, in a venue the
successor does not use, unreproduced across roughly ten secure pods since.** It
is a real risk that has never been explained; it is not a common one.

### 5.2 What the anomaly would cost across nine runs, and whether the seed fallback holds

At the §3.2 pricing, nine runs cost $125.46 nominal.

| Scenario | Nominal | At the 3.5x rate | Excess |
|---|---|---|---|
| Nine runs (3 per arm) | $125.46 | **$439.11** | $313.65 |
| Roadmap's fallback: 3 free, 2 tracker, 2 entangled | $93.84 | **$328.44** | $234.60 |

**The seed fallback saves $110.67 in the anomaly case and still spends $328.44.**
That is 1.46 times the entire proposed $225 cap, and it is 82% of the whole
existing $400 envelope on its own — more, on its own, than this programme has
spent in its entire history. **The existing fallback is not sufficient and
was never a spend control.** It is a scientific decision — how many seeds the
result rests on — dressed as a budget one. Dropping two runs from a plan whose
unit cost has tripled does not address the tripling.

*Worth saying, in the fallback's defence:* it is not useless. $110.67 is real
money and fewer runs is genuinely cheaper. The objection is only that it cannot
keep the experiment inside any cap the programme has, so it must not be the
thing relied on.

**What is sufficient is stopping, not trimming.** If the check fires on the
first anomalous pod and halts, exposure is one pod's overrun: at 3.5x, a
constructed arm's run costs $55.34 instead of $15.81, an excess of **$39.52**.
That is where the $40 anomaly margin in §3.4 comes from — **the margin is
exactly the exposure the tripwire permits**, which is the only principled way I
can think of to size it. If John wants a smaller margin, the lever is a tighter
threshold or a smaller funded balance, not a smaller number.

### 5.3 The check, specified

**What is measured.** Two ratios, because the good one is slow and the fast one
is rough.

- **Ratio A, the authoritative one: billed hours divided by pod-existence
  hours**, per pod, from RunPod's own billing rows. This is exactly what rule 4
  of `compute-ledger.md` already requires at phase boundaries, and it is the
  quantity the 2026-08-08 note recorded (8.47 against 2.42).
- **Ratio B, the fast one: account-balance drawdown per elapsed hour, divided by
  the posted hourly rate times the number of pods running.** Available within
  minutes of launch from the balance query the ledger already uses.

**What it is measured against.** The posted hourly rate for the venue read from
the pod record at creation, not remembered. The 2026-09-19 row is the standard:
"$0.99/hr (confirmed from the pod record, not assumed)".

**The threshold: 1.25.** Either ratio at or above 1.25 is a trip.

*Why 1.25 and not 3.5.* Waiting for 3.5 means the anomaly must arrive at full
observed strength before anything happens; a 1.5x or 2x overrun would run all
nine runs and quietly spend $60 to $125 extra without ever tripping. And 1.25
is far clear of ordinary reconciliation noise: the 2026-08-12 rule-4 check
reconciled a console total of $106.88 against a balance-implied $106.80, a
disagreement of 0.07%. **The strongest alternative is 1.5**, which roughly halves
the chance of a false trip on a short or oddly-billed pod, at the price of
tolerating a 50% silent overrun — about $63 across nine runs. I prefer 1.25
because a false trip costs one message to John and a real trip costs hundreds of
dollars, but this is a judgment call and either number is defensible.

**When it runs.** Three times, and the first is the important one.

1. **In flight, hourly, on ratio B**, from the first hour of the first pod. This
   is the check that gates the next launch, because the billing row is not
   trustworthy early: the 2026-08-09 row records "billing row incomplete at
   fetch", and the 2026-08-08 row "grew overnight, 8.47h->9.41h / $5.86->$6.52".
   A check that reads the billing row at pod deletion will under-read.
2. **Before the second pod of the first wave is created**, and before every
   later wave, on whichever ratio is available.
3. **At each wave boundary, on ratio A**, cumulative billed against cumulative
   estimate for the whole successor, reconciled to the ledger as rule 4 already
   requires.

**A check that cannot run is a trip.** The balance query returned HTTP 403 with
the stored key during the 2026-09-17 wave, and the ledger says so: the figures
in that row are "COMPUTED FROM MEASURED POD LIFETIMES, not balance-confirmed".
Under pre-authorisation, a silently skipped check is the whole failure mode, so
a failed measurement is treated as a trip and the next launch waits for John.

### 5.4 What happens automatically when it trips

1. **Halt, not trim.** No further pod is created under pre-authorisation. All
   five pre-authorised lines in §4.3 lapse at once.
2. **A pod already in flight is left to finish** if its own projected total is
   inside its estimate times the measured ratio and the funded balance covers
   it. Killing a running pod forfeits its checkpoint, and forfeiting checkpoints
   is what cost $97.04 on 2026-08-12. The exception: if the projected drawdown
   would exhaust the funded balance before the checkpoint and its DONE marker
   are written, the pod is killed and the run is written off. That decision is
   arithmetic, not taste, and C2 permits it — Claude "may kill but never
   restart".
3. **A ledger row is written with the measured ratio, both hours, and the
   balance reading, before anything else happens.**
4. **John is notified with the number**, and every subsequent launch needs his
   own words.
5. **The seed drop is still available, as a scientific decision** — the
   roadmap's week-43 fallback stands on its own merits about statistical power.
   It is simply not what protects the cap, and it is John's call after the halt,
   not an automatic consequence of it.

### 5.5 The control that actually bounds the loss

The tripwire bounds the loss to about $40 if it works. The thing that bounds it
if the tripwire itself fails is the funded balance, and that is the mechanism
which has already been tested in the worst case this programme has had: on
2026-08-12 "the Layer-3 prepaid backstop held (no card charge, stopped at $0)".

So, proposed alongside everything above: **fund the account per wave, not per
cap.** Before each wave, John tops the balance up to that wave's estimate plus
$20, and no further. A two-pod wave of constructed arms is $31.62, so the
account would hold about $52 and **no anomaly, of any size, could cost more than
$52** — because there is physically nothing else there to spend.

This is the strongest recommendation in the document, and it is worth noticing
why: it puts John's hand on the only control that has ever actually stopped an
overrun in this programme, while taking it off the five gos that have never
stopped one. That is the trade this whole proposal is making, stated in one
sentence.

---

## 6. Honest risk

### 6.1 The largest loss in this programme's history happened under a human gate

$97.04, on the 30-million-parameter pilot of 2026-08-09, reconciled against
RunPod's console as $0.254 + $78.96 + $17.821 (`compute-ledger.md`, 2026-08-12
reconciliation note). That is **43.0% of the $225.70 this programme has spent**,
and it produced nothing: "checkpoint, eval results, and train.log all LOST".

*A note on that percentage, since the number matters.* Against the stale
$215.70 figure it is 45.0%, which is where the 45% in circulation comes from.
Against the corrected $225.70 total in the ledger's 2026-09-20 row it is 43.0%.
Both are the same loss; the second is the current one.

**The gate was given and it was valid.** John said "Fire it" on 2026-08-09,
quoted in the row. What happened afterwards:

- The pod launched at $3.29 an hour, above the $2.99 the estimate assumed.
- `--terminate-after` never fired. The audit log's last event for that pod is
  its creation: "no delete event from any actor".
- No session ran between the launch and 2026-08-12, so nobody was watching.
- The pod billed 29.5 hours and drained the account. About $17.82 of the bill is
  past the backstop that was supposed to stop it.
- Nothing was recovered, because checkpoints were on container disk and the
  fetch never happened.

### 6.2 What the gate does and does not protect against

**What it protects.** Launching the wrong thing. The gate is a check on
intent and on the staging description — what will run, on what, at what rate,
for how long. It demonstrably works at that: the 2026-09-19 go changed three
things about the run it authorised.

**What it does not protect.** Anything that happens after the word "go". Every
dollar this programme has lost was lost after a valid authorisation:

| Loss | Amount | Cause | A gate failure? |
|---|---|---|---|
| The 30M pilot, 2026-08-09 | $97.04 | A terminate window that never fired; no fetch; nobody watching for three days | No |
| Idle billing, four occasions | ~$10.30 | Finished pods billing while a laptop slept or rebooted | No |
| Checkpoint recovery, 2026-09-20 | $0.067 | Two reaping mechanisms built a month apart defeating each other | No |

**Not one of these was a decision failure. All of them were mechanism
failures.** The ledger reaches the same conclusion in its own words about the
idle billing: "Three times is a design problem, not a habit problem — the reap
should not depend on a laptop being awake."

### 6.3 What pre-authorisation changes, and what it does not

**Changes.** It removes eight intent checks and puts per-item ceilings, a
committed-estimate precondition and a mechanical ratio check in their place. It
buys roughly three weeks of not waiting across the successor's critical path,
which on a thirteen-week roadmap with two kill dates and exactly one week of
slack is the difference between outcome R1 and outcome R4.

**Does not change.** The failure mode that has cost 43% of this programme's
money is untouched, because it was never a gate failure to begin with.
Pre-authorisation neither helps it nor hurts it. **A reviewer who says "this
proposal would not have prevented a single dollar of what this ledger records as
lost" is correct, and I want that written down here rather than discovered at
Gate C.** What has actually reduced that risk since August is engineering, all
of it recorded in `compute-ledger.md`: checkpoints on a network volume rather
than container disk, atomic saves with a DONE marker, checksum verification
before any deletion, the trainer refusing to delete a pod unless the output file
exists on the volume, and a pod-side reaper verified in production on
2026-09-19. None of that came from a gate and none of it is affected by this
proposal.

**Might make marginally worse, and I would rather name it than be told it.**
Three things.

- The gate is the only moment a second mind reads the staging text, and it has
  changed runs. A committed ledger row cannot do that. The mitigation in §4.6 —
  the row and the same-hour notice — is a weaker check and I am not claiming
  parity.
- Pre-authorisation plus a tripwire creates a stretch where no human is in the
  spending loop for up to three weeks. If the tripwire's own instrument fails,
  nothing is watching. That is why a failed check is a trip rather than a skip
  (§5.3), and it is the single most important line in §5.
- Eight gos are eight chances for John to change his mind about the experiment
  itself, not just about the spending. One batch go is one. The kill dates of
  2026-10-18 and 2026-11-01 and the wrap-up of 2026-12-21 are the only remaining
  scheduled moments, and they are calendar checks, not judgment ones.

### 6.4 The honest claim for this proposal

Narrow, and worth stating narrowly: **this saves calendar time and takes John
out of eight moments he does not need to be in. It does not make the programme
safer.** The programme becomes safer through the funded-balance rule in §5.5 and
through engineering that already exists, both of which would be worth doing if
John rejected every other word of this document.

### 6.5 The case against this proposal, made as well as I can make it

The programme has thirteen weeks, two kill dates and one week of slack, and it
is proposing to reduce the number of times a human looks at its spending — in a
programme that has already lost $97 to a pod nobody looked at for three days,
that has burned $10.30 on four separate occasions because a laptop slept, and
that discovered as recently as 2026-09-20 that two of its own safety mechanisms
defeat each other. The measured saving is three weeks of calendar on a schedule
that could equally be protected by John batching his gos into two sittings a
week, which costs nothing and changes no commitment. The proposed cap is 73%
larger than the one he approved on 2026-09-20, and rests on a 1.55 cost
multiplier inferred from a different architecture on a different task. The
envelope increase asked for is real money on a research programme with no
release date. The strongest version of "no" is: **approve the corrected cap
arithmetic and the tripwire, decline the pre-authorisation, and batch the gos
instead** — that captures most of the schedule benefit and gives up none of the
human check.

I do not think that is right, mostly because §5.5 moves John's attention to the
control that actually works rather than merely reducing it. But it is close, and
it is the argument I would want a reviewer to press hardest.

---

## 7. What this asks for, as a list to rule on

1. **Note the corrected arithmetic** in §1: the $130 cap is $12 short of its own
   contents; programme headroom is $174.30, not $184; closing A3 releases
   nothing into the pool.
2. **Successor cap $225** (§3.4), with the nine-run line re-costed from the
   week-40 rehearsal's measured throughput before the registration commit, and
   the ledger recording the lower figure if the arms come in cheaper.
3. **Programme envelope $400 to $460** (§3.5). The alternative — hold $400, six
   runs, no margin — is set out there and is a real option.
4. **The pre-authorisation scheme** in §4.3, §4.4 and §4.5, subject to John's own
   reading of "or any later wave" in commitment C2 (§4.2).
5. **The tripwire** in §5.3 and §5.4, at a threshold of 1.25, replacing the
   week-43 seed fallback as the spend control while leaving the seed drop
   available as a scientific decision.
6. **Fund the account per wave, not per cap** (§5.5): top up to the wave's
   estimate plus $20 and no further.
7. **Correct `data/project.toml`**, whose `[[spend.lines]]` block still carries
   $215.70 spent against the $400 envelope and $44.20 against the A3 stop.

Nothing above is spent, launched or rented. If John rules on items 1, 2 and 3
and declines 4, the roadmap still works; it just costs him eight conversations
instead of one.

---

## Note added afterwards: the detail

*This is the backing for the short note at the top of this document.*

**Added 2026-09-21, later the same evening, by a later Claude Code session
working in its own worktree. This is not John's ruling and it is not part of
the proposal. Nothing in the proposal above is rewritten; it is left
unedited, exactly as it was committed.**

**What the proposal still says.** In three places this document says that the
project's structured status file, `data/project.toml`, still carries the old
spend figures. Twice in section 1.3 — the paragraph headed "The envelope
figure is stale by $10", which says the file "should be corrected in the same
session that lands any ruling on this proposal" — and once as **item 7 of
section 7**, the list of things John is asked to rule on.

**The file was corrected five minutes after this proposal was written.** The
proposal was committed at 19:51:27 Pacific on 2026-09-21, in the commit whose
message is "Proposal: pre-authorised spending for the successor experiment"
(`176efad`). The correction landed at 19:56:05 Pacific the same evening, in
the commit whose message is "data: match the site's spend figures to the
corrected compute ledger" (`4b4ec99`). `data/project.toml` now reads
**`spent = 225.7`** against the $400 programme envelope and **`spent = 44.3`**
against the $100 Amendment A3 hard stop, and both of the explanations beside
those figures were rewritten to match the compute ledger — the file that is
the record of money spent, at
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`.

**So item 7 of section 7 needs no ruling: it is already satisfied, and John
should not spend a decision on it.** Items 1 to 6 are untouched by this note,
and so is everything in the body. Section 1.3's arithmetic was right, and the
correction it asked for is exactly what happened.

The correction was owed in any case. Item 16 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md` — the item
that orders the stale spend figures brought into line with the compute ledger —
names this same file.

One related fact, checked while writing this note and recorded here rather
than edited into the body: section 6 of the December-result roadmap
(`docs/december-result-roadmap-2026-09-20.md`), which section 1.3 quotes as
saying "$215.70 spent per data/project.toml" and "about $184 unspent", has
also since been corrected, at 20:16:39 Pacific on 2026-09-21, in the commit
whose message is "Land the ruled spend correction in the December roadmap"
(`5ad79a0`). It now reads about $225.70 spent and about $174.30 left. The
quotation in section 1.3 is accurate about what the roadmap said when this
proposal was written, and is no longer a description of what it says today.

**Why a note and not an edit.** This repository already handles a superseded
claim this way: the two stacked dated blockquotes at the top of
`docs/control-clause-proposal-2026-09-19.md` say in terms "Nothing in this memo
is rewritten" and "It is left unedited", and `STATUS.md` carries a dated block
marked "ANNOTATION 2026-09-16" above a paragraph it leaves standing. No ruling
of John's puts that practice into words. The nearest is item 20 of the ruling
file named above — the one about a measured count of record keys that does not
reproduce, which chooses to correct the record later rather than chase it that
night — and it does not say "annotate, never edit". The practice here rests on
precedent, not on any wording of his.

---

## Second note added afterwards: the detail

*This is the backing for the second short note at the top of this document.*

**Added 2026-09-22 by a later Claude Code session working in its own worktree.
This is not John's ruling and it is not part of the proposal. Nothing in the
proposal above is rewritten; it is left unedited, exactly as it was committed.**

**What moved.** Section 1.3 and section 2 take the programme total as about
$225.70, drawn from the compute ledger, which is the right file to draw it from.
The ledger has since been corrected again. The two follow-up reading runs of
2026-09-20 — the matched control of Amendment A3 and the standardised refit at
the same positions — were described in several places as costing nothing,
because neither produced a result: both machines were created, both were refused
by the instrument's own reproducibility check when a recorded accuracy failed to
reproduce on rented hardware, and both were deleted inside half an hour. They
still cost money. The account balance moved from **$79.7159 to $77.8119** while
they ran, a measured **$1.9040**, split between the two rows by how long each
machine lived. The ledger's launch-outcome annotation of 2026-09-20 carries a
dated correction of 2026-09-21 folding it in.

**The corrected chain, derived from the ledger's rows rather than copied from
any summary sentence.** $215.70 after the wave of seeds 1 and 2 on 2026-09-17,
plus about $9.90 for the run that asked whether the control question can be
learned when it is taught properly, plus $0.07 to recover that run's final
checkpoint, plus the $1.90 above, plus about two cents for the measurement
rehearsal of 2026-09-21, giving about **$227.60**.

**Section 2's table, with only the rows that move.** Everything not listed here
is unchanged.

| Measure | As section 2 has it | Corrected |
|---|---|---|
| Programme spent to date | ~$225.70 | **~$227.60** |
| Programme headroom | ~$174.30 | **~$172.40** |
| Amendment A3 spent | ~$44.30 | **~$46.20** |
| A3 remaining (inside the headroom, not additional to it) | ~$55.70 | **~$53.80** |
| RunPod prepaid balance | $79.82 | **$77.3451**, the last reading the ledger records, on 2026-09-21 |

**The knock-on figures, worked here so nobody has to re-derive them.**

- **What the successor at $130 leaves** (section 2): $227.60 plus $130.00 is
  $357.60, leaving **$42.40** of the $400 envelope rather than $44.30. It still
  fits, and section 2's point — that the roadmap's cap is affordable but does
  not buy what the roadmap says it buys — is unchanged.
- **The envelope position after a $225 cap** (section 3.5): $227.60 plus $225 is
  **$452.60**. The $400 envelope still does not hold it, so the ask stands. At
  full draw against the proposed $460 envelope the remainder is **$7.40**, not
  $9.30 — which strengthens section 3.5's own words, that this is the rounding
  and not a margin, and makes its alternative of $475 the more honest number.
- **The fit table** (section 3.5): each overshoot grows by $1.90. Nine runs are
  over by **$51.87**, seven by **$20.24**, six with an anomaly margin by
  **$10.05**; six runs with no margin at all still fit, leaving **$29.95**. No
  row changes side, so section 3.5's conclusion — that this is not a cap problem
  a smaller experiment solves — is unchanged.
- **The largest loss as a share of programme spend** (section 6.1): $97.04
  against $227.60 is **42.6%**, not 43.0%. Same loss, current denominator.
- **The two spending releases of the ruling of 2026-09-21**: about $175 against
  $172.40 is about **$2.60** over, not about seventy cents over. That question
  was left open for the rehearsal's measurement to answer and is still open; it
  simply has more to answer.

**What this does not touch.** Not the pre-authorisation scheme, which is about
who says go rather than how much is left. Not the corrigibility commitments.
Not section 1.3's finding about the $130 cap not covering its own contents. Not
section 1.3's other finding, that closing Amendment A3 releases no money into
the pool — that argument is unaffected by the size of the totals, and the A3
remainder is still inside the headroom rather than additional to it.

**One earlier statement is now doubly overtaken.** The first note at the top of
this document says `data/project.toml` has been corrected and that item 7 of
section 7 therefore needs no ruling. That remains true — the file has been
corrected again, on 2026-09-22, to the figures above, so item 7 is still
satisfied. What has changed is which pair of numbers the file carries.

**Why a note and not an edit.** The same reason the first note gives, and it is
worth repeating that this rests on precedent rather than on any wording of
John's: this repository handles a superseded claim with a dated note that leaves
the text standing, as the stacked blockquotes at the top of
`docs/control-clause-proposal-2026-09-19.md` and the dated annotation block in
`STATUS.md` both do. No ruling of his puts that practice into words.

Source for every figure above:
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, which is the
system of record for money and which is not edited by this note. No money was
spent and no machine rented for it.
