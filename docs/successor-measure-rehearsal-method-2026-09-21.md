# The successor experiment's measurement rehearsal — method, committed before any of it was built

*2026-09-21 (Pacific), written in its own worktree branch. **UNREGISTERED.**
Nothing here is a ruling, nothing here registers anything, and no number
below is a bar for the successor experiment. This file says what will be
built, what each check will show, and — before anything runs — what counts
as passing, what counts as failing, and what counts as no verdict at all.*

*Committed **before** the code it describes, which is this programme's
standing discipline and the thing whose absence caused its worst failure: a
fix marked adopted with nobody having run anything to confirm it.*

*Written under the workspace plain-language rule
(`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30): the plain word before the
term of art, and no identifier without a phrase saying what it is. The
rental service's word for one rented machine is not used; this file says
**rented machine**.*

*Everything in section 2 to section 8 runs **locally, on the laptop, at toy
scale, for no money**. Section 9 stages one short slice of rented time and
**does not run it**: that needs John's spoken go naming the run, and it has
not been given.*

---

## 1. What this is, and what it is not

The outside-review protocol (`docs/outside-review-protocol.md`, amended by
pull request 13 and ruled on 2026-09-21) now makes a complete measurement
rehearsal a hard precondition for any registration review. This is its first
application: the rehearsal for the successor experiment described in
`docs/successor-experiment-proposal-2026-09-21.md`.

**What a rehearsal is for.** It shows, on tiny stand-in systems and before
anything is registered, that the experiment is actually constructible and
that its measure actually reads. It is not a pilot and it is not evidence
about the scientific question. Nothing measured here is a result about
whether a small transformer has an ownership answer.

**What this rehearsal is judged against.** Two lists, and they are both
specifications, not suggestions:

- the **six checks** the protocol's rehearsal section names, each of which
  needs its command and its output in the committed record. They are
  numbered **P-1 to P-6** below;
- the **ten rehearsal items** in section 10 of the successor proposal,
  numbered there **R-1 to R-10** and kept under those numbers here.

**What this rehearsal must not do.** The separation bar between the two
built systems, the learn-both threshold, the floor under the whole-state
transplant, the rank cap, the seed count and the across-seed uncertainty
method are **outputs** of this rehearsal, not inputs to it. Section 9 of the
proposal lists them and says so; the proposal's own words are that inventing
a plausible value would be "a fatal finding waiting to happen". This file
therefore states, for each of them, **the measurement that will be produced
and handed to John**, and states explicitly that the number itself is left
for him to fix. Where a threshold is needed *inside the rehearsal* to decide
whether a rehearsal item passed, it is called a **rehearsal reachability
threshold**, it is written down here before running, and it is marked as not
being the registered number.

---

## 2. The stand-in system

### 2.1 The grammar: matched-role revisions, shrunk

Section 4 of the proposal describes a grammar in which the model acts in two
matched roles at the same kind of position: an **own-directed revision**
(emit the successor of the model's own earlier value on an item) and a
**named-other-directed revision** (emit the successor of a named agent's
earlier value on an item). The rehearsal builds a small version of exactly
that.

One episode:

- **Four agents**, each with a marker word drawn without replacement from a
  pool, so no marker word is attached to any agent across episodes.
- **Two items.** For each item, the four agents assign four **distinct**
  values out of eight value slots, so a solver that cannot tell whose value
  it needs faces four candidates, and pure guessing faces eight.
- **Eight assignment turns** — every agent assigns every item exactly once —
  in a uniformly random order. Rendered `<marker> assign <item> <value>`.
- **Two action turns**, last, in a random order between them, rendered
  `<act> revise <who> <item> <ans> <value>`, where `<who>` is the special
  word meaning *your own* in the own-directed condition and a marker word in
  the named-other condition. The two action turns are the same length and
  the same shape, and differ in exactly one token.
- **The acting channel** — the wire that tells the model, at the moment it
  acts, that this turn is its own — fires on the model's own assignment
  turns and on both action turns. It is the only honest source of ownership
  in the episode.

**One deliberate departure from the registered A3 grammar, and it is
load-bearing.** In the A3 grammar the model's own turn carries its own
marker word, so a model can read a name badge at the moment it acts instead
of having carried a binding — `curriculum_a3.py` records this in its own
header as an honest limit on the design's central claim. The rehearsal's
action turns carry **no marker**, only the word meaning *your own*. Two
consequences, both wanted:

1. the only route to the ownership answer is the acting channel, so the
   stand-in is cleaner than the thing it stands in for;
2. a matched pair of episodes — the same content with a different agent
   being the model — comes out **token-for-token identical**, differing only
   in which positions the acting channel fires on. That is what makes a
   transplant between the two a clean comparison, because nothing but
   ownership can differ anywhere in the state.

Whether the registered grammar should adopt the same departure is a question
for the registration text, and section 10 of this file says what the
rehearsal found about it.

**What is matched, and how it is checked** (proposal section 4.2, checked
rather than asserted):

1. **Candidate count** — four earlier values in context in both conditions.
2. **Distance** — the gap in turns between the source assignment and the
   action, drawn from the same distribution in both conditions.
3. **Supervision** — exactly one supervised position of each kind per
   episode, one scored token each, equal loss weight.
4. **Transformation** — the same successor rule in both conditions.

**Carried-forward rules that run on the built generator**, both from the
red-team ledger of experiment 06: the **even-split rule** (ledger item
`RT-58`, the batch-split bias check, which found that splitting rows by
condition must leave an even number of rows or the generator's matched pairs
are cut) and the **one-scored-token self-test** (ledger item `RT-59`, the
check that exactly one token per supervised position is scored and that the
check survives the shift the loss function applies).

### 2.2 The three architectures, plus two made-up ones

All arms share one trunk: token embedding, learned position embedding, a
learned acting-channel vector added where the channel fires, four
pre-normalised self-attention and feed-forward blocks, and a head over the
vocabulary scored only at the two supervised positions. Roughly one to three
million parameters. What differs between arms is **only how the ownership
answer is allowed to exist**.

- **Arm T — the ownership answer kept separable.** The running state is
  split by construction into content dimensions and a small block of
  **ownership dimensions**. The blocks read and write content only; nothing
  in the trunk may touch the ownership block. An ownership module builds
  "which agent am I" causally from the acting channel — a running,
  acting-masked pool of the marker representations of the turns the channel
  fired on — and writes it, and nothing else, into the ownership
  dimensions. The action head reads the ownership block as the row selector
  into a lookup over the assignment turns, and applies a learned map over
  the eight value slots. The factoring into (lookup table, ownership
  answer, selection) is the architecture, not something the network may or
  may not discover. **Its degree is zero by construction, and there is one
  place to patch.**
- **Arm C — the ownership answer entangled.** The same trunk with the same
  ownership signal, and **no block of its own anywhere**. It enters as a
  scale-and-shift on the whole running state at every block, and it
  multiplies the item and value representations at the point where they are
  bound, so that "which item, whose value" is one quantity rather than two.
  No dedicated position exists and nothing reads ownership alone. **Its
  degree should be high, and there should be no single site to patch.**
- **Arm F — the freely trained system.** The trunk and the acting channel,
  nothing else, no constraint on where the ownership answer lives.
- **Arm B — a made-up broken system, built to produce a negative reading.**
  Arm T with a second, sign-flipped copy of the ownership answer written
  into a content sub-block that the head reads with an opposite weight.
  Transplanting the whole state swaps both copies and they cancel;
  transplanting only the ownership block swaps one and works. So the
  ownership-only accuracy should **exceed** the whole-state accuracy and the
  reading should come out **negative**. This arm exists solely so that
  rehearsal item R-4's negative outcome is demonstrated on a real forward
  pass rather than only in arithmetic.
- **Arm N — no made-up system; a made-up *site set*.** To demonstrate the no
  verdict outcome, arm T is measured at a site set chosen to fail: the
  earliest layer, at a position before the model's identity can be known.
  The whole-state transplant there should be below any floor, so the measure
  should return **no verdict**.

---

## 3. The measure, exactly as the proposal defines it

Matched pairs of episodes: the **recipient** is the episode the model runs;
the **donor** is its twin in which the model is a different agent. Because
all four agents assigned the item, the value the donor's identity dictates
is already sitting in the recipient's own context, so a successful
transplant does not import an answer from outside — it changes which of four
in-context values gets selected.

A **site set** — a list of token positions and a list of layers — is fixed
before anything is read. At those sites:

- **whole-state transplant**: replace the entire running-state vector with
  the donor's;
- **ownership-only transplant**: at the same sites, replace only the part of
  that vector lying in the nominated ownership subspace.

The second is a restriction of the first to a subspace, at identical sites —
not a smaller or different intervention. Three numbers per arm:
`accuracy_whole`, `accuracy_ownership_only`, and `accuracy_untouched` with
no transplant at all. The reading is

    degree = (accuracy_whole - accuracy_ownership_only) / accuracy_whole

with an explicit no-verdict rule attached: below a floor on
`accuracy_whole`, no degree is reported and the reason is recorded; if the
ownership-only accuracy exceeds the whole-state accuracy, the reading is
negative and is reported as observed rather than quietly clipped to zero.

**The floor's value is not set here.** What is produced is the measured
curve of `accuracy_whole` against site set, per arm, which is what a floor
has to be chosen against.

---

## 4. The six checks the protocol requires

Each is listed with the command that will produce it and, **before it runs**,
what counts as passing, failing, and no verdict. Commands are given relative
to `experiments/rehearsal-successor-measure/src/`, run with the repository's
own Python interpreter.

### P-1. The target can be found

*The quantity the pre-statement names is recovered in the stand-in by the
stated instrument, with a number to show for it.*

Command: `rehearse.py --stage nominate`

The stated instrument is the proposal's own two-step nomination (section
7.2): fit a straight-line read for "which agent is acting" at every
candidate site, take its leading directions up to a rank cap, then
**nominate by causal effect, not by how well the read fits** — the nominated
subspace is the one with the highest ownership-only transplant accuracy on
development episodes. The procedure runs **blind** on every arm: arm T's
known ownership block is never handed to it.

- **Pass** — on arm T, blind nomination returns a subspace whose
  ownership-only transplant accuracy on development episodes is at least
  **0.50** (the *rehearsal reachability threshold*, fixed here, **not** the
  registered floor), and the overlap between the nominated subspace and arm
  T's true ownership block is reported alongside.
- **Fail** — blind nomination cannot find a subspace above that threshold on
  arm T, the arm whose answer is in a known place by construction. If the
  procedure cannot find the answer where the answer is known to be, it
  cannot be trusted where it is not.
- **No verdict** — arm T does not reach the learn-both gate, so there is no
  trained system to nominate on. Recorded as no verdict, and R-1's failure
  fires instead.

### P-2. The comparison has room to move

*Every control, baseline or comparison condition is scored and its ceiling
is measured rather than assumed.*

Command: `rehearse.py --stage solvers` and `rehearse.py --stage controls`

Two ordinary competing solvers are built and scored on both conditions (this
is also R-5), and all seven controls of proposal section 7.3 are run and
scored on every arm.

- **Pass** — every control produces a number, and the two competing solvers
  produce measured accuracies on both conditions so that the learn-both
  threshold can later be set against something that was built rather than
  against arithmetic.
- **Fail** — any comparison condition cannot be scored, or a competing
  solver reaches the arms' own accuracy, meaning the comparison is already
  saturated and has no room to move.
- **No verdict** — a control cannot be evaluated at all. Under stop
  condition S8 of the proposal (John's ruling of 2026-09-21: a check that
  cannot run counts as a trip, not a skip) this is recorded as a **fail**,
  not stepped over.

### P-3. The arithmetic is finite

*The metric is computed on those scores and returns a number: no zero
denominator, no formula that only survives on the values its author had in
mind.*

Command: `measure.py --self-test`

The measure is exercised on made-up score pairs chosen to break it: a zero
whole-state accuracy, a whole-state accuracy just above and just below a
floor, an ownership-only accuracy above the whole-state accuracy, both
accuracies equal, and both zero.

- **Pass** — every case returns either a finite number or the explicit
  no-verdict outcome with its reason, and no case raises, divides by zero,
  or returns a value outside the range the rule allows.
- **Fail** — any case returns a number that the rule should have refused, or
  raises.
- **No verdict** — not reachable; the self-test either runs or does not, and
  not running is a fail under S8.

### P-4. The interventions run end to end

*Every lesion, patch, swap or other intervention the design leans on runs to
completion on a saved checkpoint and moves the output it is supposed to
move.*

Command: `rehearse.py --stage transplant`

Every arm is trained, **saved to a checkpoint file, and re-loaded from that
file** before any intervention runs, so what is exercised is the same path
the registered experiment would use. Interventions: the whole-state
transplant, the ownership-only transplant, the null transplant, the
content-complement transplant, the matched random-subspace transplant, the
non-acting named agent's transplant, the not-yet-knowable position
transplant, and the acting-channel lesion.

- **Pass** — all eight run to completion on a re-loaded checkpoint, and the
  two that are supposed to move the output (whole-state and, on arm T,
  ownership-only) move it: donor-dictated accuracy rises above the untouched
  level by more than the across-seed spread.
- **Fail** — any intervention does not run, or the whole-state transplant
  does not move the output on any arm at any site set.
- **No verdict** — an arm exists but never reaches the learn-both gate, so
  there is no output worth moving; recorded per arm.

### P-5. All three outcomes are reachable

*Made-up cases are built that drive the procedure to a positive verdict, to
a negative one, and to no verdict at all, and each lands where it was
meant to.*

Command: `rehearse.py --stage outcomes`

Four made-up cases, each with its expected landing written here first:

| made-up case | what it is | expected landing |
|---|---|---|
| arm T at its nominated site set | the answer in a known place | reading near **zero**, valid |
| arm C at its nominated site set | the answer stirred through everything | reading **high**, valid, *or* no verdict — see R-3 |
| arm B, the deliberately broken arm | two sign-flipped copies of the answer | reading **negative** |
| arm T at the failing site set | earliest layer, before identity is knowable | **no verdict** |

- **Pass** — each case lands where the table says, on a real forward pass.
- **Fail** — any case lands somewhere else, and in particular: if the
  negative case cannot be produced, then a negative reading is not a real
  outcome of this instrument and the proposal's rule about negative readings
  is decoration.
- **No verdict** — arm B fails to train. Then the negative outcome is
  demonstrated in arithmetic only (P-3) and that partial state is reported
  as such, not as a pass.

### P-6. An ordinary competing solver is built and scored

*A system with none of the structure the target claims to detect is
constructed and put through the same measurement.*

Command: `rehearse.py --stage solvers`

Two are built, because "the wrong thing" has two shapes here:

- **the ownership-blind solver** — it reads the item and the four candidate
  values and has no access to the acting channel at all;
- **the name-only solver** — it uses the name token where there is one and
  guesses among the four candidates where there is not.

Both are scored on both conditions, and the ownership-blind one is **also
put through the whole measurement**, transplants and all, so the question
"could this measure be satisfied by something with no ownership structure?"
has a number behind it.

- **Pass** — both solvers are scored on both conditions, and the
  ownership-blind solver put through the measurement returns either no
  verdict (its whole-state transplant cannot move an action it never
  conditioned on) or a reading, and either way the number is on the record.
- **Fail** — the ownership-blind solver produces a reading indistinguishable
  from arm T's. That would mean the measure reads near-zero degree off a
  system with no ownership answer at all, which would make a near-zero
  reading on arm F uninterpretable.
- **No verdict** — the solver cannot be scored; a fail under S8.

---

## 5. The proposal's ten rehearsal items, with their cells fixed first

| item | what it has to show | **pass** | **fail** | **no verdict** |
|---|---|---|---|---|
| **R-1** grammar works, both conditions learnable at tiny scale | both matched conditions above the one-in-four level; the four matched properties hold in the generated data | both conditions above 0.25 on held-out episodes, significantly under a binomial test at the 0.05 level, on at least two of three seeds; all four matched properties pass their self-test | either condition at or below 0.25 on a majority of seeds, or any matched property fails | training does not complete; counts as fail under S8 |
| **R-2** arm T constructible, its pointer patchable on its own | blind nomination finds the ownership block without being told where it is; the ownership-only transplant reproduces the counterfactual | blind nomination reaches at least the 0.50 reachability threshold on development episodes, and the reading on fresh episodes is below 0.5 — nearer zero than one | nomination below the threshold, or the reading above 0.5 on the arm built to read zero | arm T does not pass R-1 |
| **R-3** arm C constructible, its degree genuinely known by construction | blind nomination over the frozen site set finds **no** subspace reproducing the counterfactual, while the whole-state transplant at the same sites **does** | whole-state accuracy at or above the 0.50 reachability threshold **and** the best blind-nominated subspace below half of it — reading above 0.5 | a subspace is found that reproduces the counterfactual: the arm is not entangled and **the two-arm fallback fires**, which John pre-approved on 2026-09-20 | whole-state transplant below the threshold at every site set: no verdict on arm C, reported as such, and it has the same consequence as a fail — the fallback fires |
| **R-4** all four outcomes reachable | near-zero, high, negative, no verdict | the table in P-5 lands as written | any cell lands elsewhere | arm B untrainable: partial, reported as partial |
| **R-5** ordinary competing solver built and measured | a solver that cannot use ownership and a solver that uses only the name token, both scored on both conditions | both scored, both numbers recorded | either cannot be built or cannot be scored | — |
| **R-6** the arithmetic is finite | floor rule and no-verdict rule exercised on cases chosen to break them | P-3 passes | P-3 fails | — |
| **R-7** throughput measured per arm | seconds per step and projected wall-clock and money for each architecture at the registered size | seconds per step measured for all three arms at tiny scale **and** at the registered shape on this laptop, with the ratios between arms reported | any arm cannot be timed | **the absolute figure for rented hardware cannot be obtained locally at all.** See section 9: this is the one place the rehearsal reaches a question only a rented machine can answer |
| **R-8** transplanting code passes its known-answer tests | null transplant changes nothing; a transplant on the arm T toy moves the action to the donor's value; the ownership-only transplant is verified to be the restriction of the whole-state transplant to a subspace | null transplant leaves every logit bit-identical; the arm T transplant moves the action; the restriction property holds exactly, checked as an identity on tensors and not by eye | any of the three fails | — |
| **R-9** paired-uncertainty method chosen and demonstrated | the method, and the seed count following from it | two candidate methods computed on the same data — the across-seed paired spread and a bootstrap over matched pairs within a seed — with the arithmetic for how many seeds each implies for a given half-width | neither can be computed | — |
| **R-10** the separation bar set | the observed separation between arms T and C and its spread, with the reasoning written out | the separation and its spread are measured and reported, with the arithmetic a bar would be derived from **laid out for John to rule on** | the separation cannot be measured | — |

**Two of those cells deserve saying out loud before anything runs.**

- **R-10 is written as a measurement, not as a bar.** The brief for this work
  and section 9 of the proposal both say the bar is an output. This file
  will not name one. It will produce the separation, its spread across
  seeds, and the arithmetic that turns those into a bar, and it will say
  that fixing the bar is John's.
- **R-7 cannot be finished on this laptop.** Seconds per step on an Apple
  M4 predicts nothing about seconds per step on a rented graphics card, and
  the whole point of John's second-release ruling is that the estimate rests
  on measurement rather than on inference from a different machine. So R-7
  comes back as **measured locally, incomplete for the registered
  estimate**, and section 9 stages what would finish it.

---

## 6. The order the stages run in

1. Build the grammar; run its self-tests, including the even-split rule and
   the one-scored-token check.
2. Build the arms; run each one's self-test, including the structural claims
   — that arm T's trunk cannot write the ownership block, that arm C has no
   block that carries ownership alone.
3. Train every arm on three seeds, saving a checkpoint per run.
4. Score the learn-both gate and the two competing solvers.
5. Nominate blind, on development episodes only, per arm.
6. Freeze the nomination; run the transplants and all seven controls on
   fresh episodes with marker and content combinations that appear in
   neither of the other two sets.
7. Compute the measure; run the made-up outcome cases.
8. Time every arm at tiny scale and at the registered shape.
9. Write the findings file with every command and every output in it.

---

## 7. What would make this rehearsal report a problem rather than a result

Written down now so that finding one of them is not later dressed up as a
success. Any of these is a finding, and a finding is worth more than a clean
report that hides it:

- **The degenerate site set.** Because a matched pair differs only in the
  acting channel, transplanting the whole state at *every* position and
  *every* layer is not an intervention at all — it is the donor's forward
  pass, and the whole-state accuracy would be 1 by definition. If the only
  site set at which the whole-state transplant clears a floor is that
  degenerate one, then the measure's denominator is guaranteed by
  construction and the reading means nothing. The rehearsal measures the
  whole-state accuracy **as a curve against site set size** for exactly this
  reason, and reports where on that curve each arm's reading sits.
- **The untouched floor's stated value.** The proposal says
  `accuracy_untouched` "should be near the one-in-eight guessing rate; if it
  is not, the pairing is broken". For a *trained* arm that is wrong: an arm
  that has learned its own answer will emit its own value, which is never
  the donor's, so the untouched donor-dictated accuracy should be near
  **zero**, not near one in eight. If the rehearsal measures near zero, the
  proposal's sentence needs correcting before registration.
- **Arm C's whole-state transplant failing.** If the ownership signal is
  re-applied by every block above the patch site, a whole-state patch at a
  restricted site set may never reproduce the counterfactual, and arm C
  returns no verdict at every site set. That fires the two-arm fallback, and
  the honest reading is that the measure has one anchor, not two.
- **Arm F's learnability.** The honest prior in section 3 of the proposal is
  that the most likely outcome of the whole experiment is that the arms do
  not learn both conditions. If arm F cannot learn them at tiny scale, that
  is not proof it cannot at the registered size, but it is worth reporting
  in the same sentence as the prior it agrees with.

---

## 8. Corrigibility and cost

Local, on the laptop, inference and toy training only. **No machine is
rented, no vendor is contacted, no money is spent** by anything in sections
2 to 8. Nothing registered is edited: not `launch_a3.sh`, not the compute
ledger, not `data/project.toml`, not any ruling. Nothing is pushed to the
main line, nothing is merged, and no pull request is opened. Output files
are fresh per run and nothing is overwritten.

---

## 9. The rented slice, staged and not run

John has ruled that a short slice of rented time will happen so that seconds
per step is measured on the hardware the estimates rest on rather than
inferred from another machine. **That ruling is not a go.** This programme
requires his spoken go naming the specific run, and it has not been given.
So the slice is built, its pass and fail lines are written down here, its
cost is estimated, and **it is not launched**.

The slice answers two questions for one rent, which is why it is worth the
few cents it costs.

### 9.1 Question one — how fast is each of the three architectures

Three short runs, one per architecture, at the registered shape, each long
enough to time a few hundred steps after warm-up and no longer.

- **Pass** — seconds per step recorded for all three, with the spread over
  the timed steps, so the second release's estimate rests on measurement.
- **Fail** — any architecture will not run at the registered shape on the
  rented hardware, for instance because it runs out of memory. That is a
  finding about the design, not about the machine.
- **No verdict** — the rented machine is unavailable or bills anomalously.
  Under stop condition S9 the wave halts and the billed row goes to John
  beside the estimate.

### 9.2 Question two — does the shutdown handshake work against the real vendor

A separate session finished the fix for the race between the trainer
deleting its own machine and the laptop taking the final copy. Its method
note is
`experiments/06-mvm-0a-constructed-self-index/reap-shutdown-order-method.md`
on branch `worktree-reap-race-fix`, and its own section 10 says the right
place to test it for real is this rehearsal. **This staging does not change
that fix and does not duplicate it.** It exercises it.

The fix is verified against local stand-ins only — twenty-six checks
including a negative control that reproduces the old ordering and correctly
fails — and its author is explicit that the machine-side process check, the
credential handling and the command form are **inferred, not measured**.
That matters more than it looks, because the one thing this programme has
actually measured on a real rented machine (2026-09-16, a paid test costing
$0.29) is that **a rented machine carries no usable credential and does not
know its own identifier**. The fix's answer is that the launcher supplies
both — a dedicated reaper key and the machine's own identifier written to a
file. Whether that answer works has never been tried.

Pre-stated signals, which are the fix author's own:

- **Pass** — `receipt written on the machine` in the laptop's log, then
  `receipt found` in the machine's log, then a deletion within seconds of
  it, in that order; and the copied model file matches the one on the
  machine by checksum.
- **Fail (bounded-wait path)** — the machine's log says `grace ran out`.
  The receipt path did not work and only the bounded wait ended the
  billing. The run is treated as unsafe to leave unattended until it is
  understood, and the registration cannot lean on the handshake.
- **Fail (credential path)** — the machine cannot delete itself even after
  the bounded wait, because the supplied key or identifier does not work.
  This is the 2026-09-16 measurement repeating, and it means the laptop is
  still the only reap.
- **No verdict** — the slice does not run. Then the handshake is exercised
  against local stand-ins only, and the registration says so in its own
  text.

### 9.3 What it would cost

Timing a few hundred steps on three architectures, plus one toy run carried
to completion so the finished-marker, the receipt and the deletion all
happen for real, is well under an hour of rented time. At the $0.99 per hour
rate of the most recent registered runs (the 2026-09-17 row of the compute
ledger: two machines, 20.28 machine-hours, $20.08), **the estimate is about
$0.75 to $1.00, with a hard cap of $2.00.** The precedent for a short
deliberately-capped test is the self-delete test of 2026-09-16, authorised
at a $0.50 cap and billed at $0.29.

That sits inside the first release of money John authorised on 2026-09-21,
whose rehearsal line is up to $10.

**It is staged. It is not run. It needs his go, naming the run.**

---

## 10. Where the record goes

The findings, with every command and its output, go to
`docs/2026-09-21-successor-measure-rehearsal.md`, which is the filing path
the protocol names for a rehearsal whose experiment directory does not exist
yet. The code lives under `experiments/rehearsal-successor-measure/`, which
is a rehearsal directory and not an experiment: nothing in it is registered
and nothing in it may be cited as a result about the scientific question.
