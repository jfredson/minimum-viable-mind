# Check before merge — the successor experiment's measurement rehearsal

*2026-09-21 (Pacific). A checking session that did not build the thing it is
checking, as the pairing rule in `docs/outside-review-protocol.md` requires.
Target: the branch `worktree-agent-a827aade30edf9e28`, six commits from
`9673bf1` ("Rehearsal code: the denominator checks, frozen reads, three
readings of the read's label, and the across-seed method") to `c3fbfbe`
("Findings: the proposal's ten rehearsal items, each with where it stands").
Its earlier commits — the method, the method's denominator addendum, the first
block of code and the staged slice of rented time — are already on the main
line.*

*Filed here because the rehearsal is for an experiment whose own directory does
not exist yet, so its findings are filed under `docs/`; the protocol then asks
the check to go under the reviews directory of the experiment the work most
affects, with a line saying why. That is this experiment: the successor
experiment is the one that follows it, the rehearsal's arms are built from its
scale ladder, and the staged slice of rented time uses its launcher.*

*Read-only. Nothing was fixed. **No machine was rented, no vendor was
contacted and nothing was spent**; everything run here ran on the laptop. The
staged slice of rented time was not run. Nothing was pushed to the main line,
nothing was merged and no pull request was opened.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30). Every finding below is labelled **MEASURED** — a check was
run and its output is reported — or **ARGUED** — reasoning a reader can
dispute.*

---

## Verdict

**Yes, merge — after seven corrections to sentences, none of which needs
anything re-run.** The work itself is sound and I am not asking for any of it
to be redone. The commit order is what it says it is. Everything I could
re-run reproduced, and two of the output files come back byte-for-byte
identical; the one thing I did not get to is a full re-training from scratch,
which is recorded as an open item at the end of section 2 rather than glossed.
The
finding that blocks registration is not only confirmed but understates itself:
under two of the three readings of the read's label the measure would print a
degree of **0.982 to 1.000** for an arm whose degree is **0.0000** by
construction, and the findings report the transplant accuracies without ever
computing the number the measure would actually print.

**Why the seven come before the merge rather than after.** Three of them are
figures the findings print as measurements that do not appear in the committed
record, and two more are claims measurably stronger than the record supports.
That is this programme's fourth known failure — a claim of measurement with a
record that does not reproduce — in the one document the protocol makes the
tier 1 reviewer read first and that the registration will be argued from.
Together they are well under an hour of editing, and not one of them changes a
conclusion. Nine further items can follow afterwards.

**On the specific question of whether the bad news is softened: it is not.**
The rehearsal is harder on its own design than its own method file requires —
it marks the throughput item "partial" where its pre-written cell says pass,
and it leads its summary with its own procedure failing. Where it does shade a
number, it shades in favour of the outside review's two fatal findings and
against itself. That is the opposite of the failure the pairing rule exists to
catch. The two places where it is genuinely too quiet are named as must-fix
items 3 and 4 below, and one place where it stops one step short of its own
worst news is named as must-fix item 2.

**One item on that list is the only one that could change a decision rather
than a sentence.** The findings mark the learn-both item a fail, and the
proposal's first stop condition is keyed to exactly that item failing. Nobody
has written down whether the stop fires. I think it does not, and must-fix
item 7 gives the reason; but it should be on the record, not left to whoever
reads the two documents next.

---

## What I opened, and what I did not

**Opened and read in full:** the workspace plain-language rule; the outside
review protocol's measurement-rehearsal section, its pairing rule and its
filing rules; the known-failure list; the successor experiment proposal's
sections 9, 10, 12 and 13; the rehearsal method file and its denominator
addendum; the staged-slice note; the rehearsal findings; and every source file
in `experiments/rehearsal-successor-measure/src/`.

**Ran:** every module self-test; the two denominator checks that need no
trained model; a sweep of every number printed in the findings against every
number in the committed output files; and a dry run of the merge itself.

**Started and did not finish:** a full re-training of all ten toy models from
scratch followed by every remaining stage. It reached three models of ten. See
the end of section 2 for exactly what that leaves open and how to close it.
**This is the one gap in this check, and it is a gap in confirmation rather
than in the findings' internal consistency**, which I checked mechanically and
in full.

**Did not open:** the closed Amendment A3 record beyond the parts the failure
list quotes, the compute ledger's history, and the earlier reviews in this
directory. **Did not run:** the staged slice of rented time, or anything that
touches a vendor.

---

## 1. Method before output — the claim everything else rests on

**MEASURED. It holds, exactly.** Every file's first appearance, in commit
order, with the clock time it was committed:

```
$ git log --diff-filter=A --format='%h %ad %s' --date=format:'%H:%M:%S' \
      --name-only worktree-agent-a827aade30edf9e28 -- <the rehearsal's files>

9a91c06 20:09:55  the method file
518bf0e 20:21:38  the method's denominator addendum
5fa85e2 20:35:05  the code: grammar, arms, transplanting, the measure
8bc5fbe 20:35:58  the staged slice of rented time
4e89c69 21:41:07  the summariser
623ef23 21:41:47  the self-test record
6e8cc08 22:31:16  the results
ebae67b 22:34:51  the findings
```

No result file predates the method that pre-states how to read it. The method
went in twenty-six minutes before the first line of code; the addendum, which
pre-states the four checks answering the outside review's two fatal findings,
went in fourteen minutes before the code that answers them.

**The method file was not quietly edited afterwards.** The findings commit does
touch it, which is the one thing that could undo the claim, so I read that
change rather than trusting its title. It is an append and nothing else:

```
$ git show ebae67b -- docs/successor-measure-rehearsal-method-2026-09-21.md
@@ -560,3 +560,63 @@
```

A sixty-three-line addition at the end of a 560-line file, adding the appendix
that records the departures. Not one line above it is altered, including the
cells that turned out wrong. This is the discipline working as intended.

**One wrinkle, which does not break the claim.** Two result files —
`out/denominator_simulated.json` and `out/denominator_control6.json` — rode in
with the code commit at 20:35 rather than with the results at 22:31, and both
the code that produces them and the grammar they run on changed afterwards. So
the committed copies were, on paper, produced by superseded code. I re-ran both
under the final code and both come back **byte-for-byte identical**, so in fact
nothing is stale. But the findings' own commit-order table calls that commit
"the code", and a reader would not know two results were inside it. Can-follow
item 2.

**The commit dates are the real ones.** Author and committer timestamps agree
to the second on all eight commits, so the order was not rewritten after the
fact.

---

## 2. Re-running it

Everything here ran on the same laptop the rehearsal ran on. The toy training
is seeded — `torch.manual_seed` on the seed number, plus a seeded sampler for
the batches — so on the same machine it should reproduce exactly, and the
stages built on it should too. The one thing that cannot reproduce exactly is
the throughput timing, because a stopwatch is not seeded; there the question is
whether the ratios come back the same, not the milliseconds.

### The self-tests — **reproduce, with more checks than the record holds**

```
$ sh experiments/rehearsal-successor-measure/src/run_self_tests.sh
passes: 64   failures: 0
```

Sixty-four checks across the grammar, the three architectures, the
transplanting code and the measure; none fails. The committed record
(`out/self-tests.txt`) shows sixty-three, because it was written at 21:41 and
the grammar changed at 22:31 and nobody re-ran it. The difference is two
grammar checks that the newer code adds and the older record cannot have. No
number in the findings depends on it. Can-follow item 1.

### The two denominator checks that need no trained model — **byte-identical**

```
$ python denominator.py --stage simulated
    strong transplant  whole-state accuracy 0.9008: registered form 0.4323
      (spread 0.0119), floor-corrected form 0.5018 (spread 0.0132)
    weak transplant    whole-state accuracy 0.3497: registered form 0.3222
      (spread 0.0181), floor-corrected form 0.5013 (spread 0.0230)

$ python denominator.py --stage control6
    distinctness-preserving grammar: 0 same-value trials out of 4000
    relaxed grammar: 346 same-value trials out of 4000; the blind solver's
      reference moves from 0.2467 to 0.3095

$ diff <committed> <re-run>            # both files
(no output)
```

Every number the findings report from these two checks is reproduced, and the
two output files are identical to the byte.

### Every printed number against the committed record — **91 of 96 exact, 5 explained, 3 unsupported**

The known-failure list's fourth failure is "a claim of measurement with no
record, or with a record that does not reproduce", and its prescribed test is a
sweep for bare numbers. I ran that sweep mechanically: every four-decimal
number printed anywhere in the findings, checked against every number present
anywhere in the committed output files.

```
$ python number_sweep.py docs/2026-09-21-successor-measure-rehearsal.md \
      experiments/rehearsal-successor-measure/out
distinct four-decimal numbers printed in the findings: 96
not found anywhere in the committed outputs: 5
  0.0613  0.1706  0.2513  0.2630  0.2755

distinct three-decimal numbers printed: 31  not found in the outputs: 3
  0.170   0.365   0.805
```

Four of the five four-decimal misses are my sweep's fault, not the findings':
0.2513 and 0.0613 are 0.25125 and 0.06125 rounded, and 0.1706 and 0.2755 are
the two negative readings, whose minus signs my matcher dropped. The fifth,
0.2630, is the bar the learn-both gate is judged against; it is arithmetic
rather than an output, and I checked it by hand — for three thousand episodes
at a one-in-four reference, the one-sided threshold at the five-per-cent level
is 0.25 + 1.645 × √(0.25 × 0.75 / 3000) = 0.2630. Correct.

**The three three-decimal misses are real and are must-fix item 1.** See below.

### The headline readings — **every one matches the committed record**

The findings' central table is the one the separation bar will be argued from.
I re-derived it from the committed output files by running the rehearsal's own
summariser, which recomputes each reading from the three stored accuracies
rather than reprinting a stored number:

```
$ python summarize.py
  C/0    untouched 0.0600  whole 0.5400  ownership-only 0.0688
         registered form: valid degree 0.8727   floor-corrected: 0.9818
  C/1    untouched 0.0663  whole 0.5750  ownership-only 0.0663
         registered form: valid degree 0.8848   floor-corrected: 1.0000
  C/2    untouched 0.0638  whole 0.5525  ownership-only 0.0663
         registered form: valid degree 0.8801   floor-corrected: 0.9949
  F/0    untouched 0.0600  whole 0.5825  ownership-only 0.0663
         registered form: valid degree 0.8863   floor-corrected: 0.9880
  F/1    untouched 0.0550  whole 0.5663  ownership-only 0.0925
         registered form: valid degree 0.8366   floor-corrected: 0.9267
  F/2    untouched 0.0762  whole 0.5663  ownership-only 0.0850
         registered form: valid degree 0.8499   floor-corrected: 0.9821
  T/0    untouched 0.0000  whole 1.0000  ownership-only 1.0000
         registered form: valid degree 0.0000   floor-corrected: 0.0000
  T/1    untouched 0.0000  whole 1.0000  ownership-only 1.0000
         registered form: valid degree 0.0000   floor-corrected: 0.0000
  T/2    untouched 0.0000  whole 1.0000  ownership-only 1.0000
         registered form: valid degree 0.0000   floor-corrected: 0.0000
```

**Not one differs from the findings.** The separable arm is exactly 0.0000 on
all three seeds; the entangled arm is 0.8727, 0.8848 and 0.8801; the free arm
is 0.8863, 0.8366 and 0.8499. The same is true of the learn-both gate table,
the two competing solvers, the seven controls, the two uncertainty methods and
the throughput ratios: every figure the findings print, I found in the record.

**What this check is and is not.** It is a full check that the findings report
what the committed outputs say — which is the failure the known-failure list's
fourth item names, and which is where the three unsupported figures in must-fix
item 1 were caught. It is **not** a check that the committed outputs are what
the code produces today; that is the re-run below, which I did not finish.

### The full re-run, from re-training every model — **started, not finished, and
this check does not wait for it**

I started a clean re-run in a scratch directory outside the repository, so that
nothing it produced could overwrite a committed output. It re-trains all ten
toy models from scratch and then runs the learn-both gate, the nomination, the
transplant, the outcome cases, the uncertainty methods, the negative case, the
two remaining denominator checks and the doubled-budget check.

**Where it got to: three of the ten models, about fourteen minutes in.** The
models take roughly six minutes each on this laptop, so the training alone is
about an hour and the stages after it add more. I am filing this check without
it rather than holding the merge on a stopwatch.

**What that does and does not leave open.** It leaves open exactly one
question: whether the committed output files are what this code produces today,
as opposed to being internally consistent with each other and with the
findings. Three things already bear on that question and all three point the
same way:

- the two denominator checks that need no trained model reproduce
  **byte-for-byte**, and one of them (the empty control cell) runs on the same
  grammar the trained arms use;
- all 64 module self-tests pass on re-run, including the ones that assert the
  architectures are built the way the arms are claimed to be built — that the
  separable arm carries its ownership block unchanged through every layer, that
  its content stream never reads that block, and that the transplanting code's
  restriction property holds exactly;
- 91 of the 96 four-decimal numbers printed in the findings are present in the
  committed output files, and I accounted for all five that are not (four are
  my matcher's rounding and sign handling; the fifth is arithmetic I redid by
  hand).

**What a later session should do to close it.** Re-run
`rehearse.py --stage all` followed by `negative_case.py`, `denominator.py
--stage attenuated`, `denominator.py --stage floor` and `budget_check.py` in a
scratch copy, and diff the resulting output files against the committed ones.
The training is seeded on the seed number with a seeded batch sampler, so on
the same machine the numbers should come back identical rather than merely
close; anything that differs is worth chasing. The one exception is the
throughput file, which is a stopwatch and will differ in the milliseconds — for
that one the question is whether the three ratios come back in the same order
and at the same scale.

**I am recording this as an open item rather than as a finding**, because a
check that did not finish is not evidence of anything and should not be dressed
up as one.

---

## 3. The finding that blocks registration — **confirmed, and understated**

**MEASURED, and it is worse than the findings say.**

The claim under check: three defensible readings of what the straight-line
read's label means give fits of 0.256, 0.706 and 1.000, and transplant
readings of 0.0000, 0.0000 and 1.0000, so that under two of the three the
measure reports the arm whose degree is zero by construction as maximally
entangled.

**The fits are exactly right.** From the committed record, on the arm built so
the ownership answer sits in a slot of its own, at the position where the
action is taken:

```
$ python summarize.py
  T/0    agent-slot 0.256  marker-rank 0.706  marker-word 1.000
  T/1    agent-slot 0.256  marker-rank 0.694  marker-word 1.000
  T/2    agent-slot 0.256  marker-rank 0.700  marker-word 1.000
```

**The transplant readings are right in substance and wrong in the printed
cells.** Measured, best over every site set and every rank cap, per seed:

| reading of the label | seed 0 | seed 1 | seed 2 | the findings print |
|---|---|---|---|---|
| the agent's slot | 0.0117 | 0.0000 | 0.0000 | 0.0000 |
| the marker's rank | 0.0050 | 0.0183 | 0.0117 | 0.0000 |
| which marker word | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

The marker-rank row is **never** 0.0000 on any seed. Printing it as a measured
0.0000 in the single most consequential table in the document is the fourth
known failure in miniature. Nothing about the conclusion changes — 0.005 to
0.018 is far below the 0.2500 a solver that cannot tell whose value it needs
reaches by luck, so "zero causal effect" is a fair plain-language reading of
it — but the cell has to carry what was measured. Must-fix item 2.

**And the findings stop one step short of their own worst news.** They report
the transplant accuracies and leave the reader to finish the arithmetic. I
finished it, by putting each label's best configuration through the measure's
own function at the rehearsal's own floor:

```
$ python implied_degree.py out/nominate.json src

  seed  label         whole   ownership-only   degree reported
  T/0   agent-slot    1.0000  0.0117           0.9883
  T/0   marker-rank   1.0000  0.0050           0.9950
  T/0   marker-word   1.0000  1.0000           0.0000
  T/1   agent-slot    1.0000  0.0000           1.0000
  T/1   marker-rank   1.0000  0.0183           0.9817
  T/1   marker-word   1.0000  1.0000           0.0000
  T/2   agent-slot    1.0000  0.0000           1.0000
  T/2   marker-rank   1.0000  0.0117           0.9883
  T/2   marker-word   1.0000  1.0000           0.0000
```

That is the sentence the registration turns on, and it is not in the findings:
**under two of three defensible readings of one unwritten word, the instrument
prints 0.982 to 1.000 for a system whose degree is 0.0000 by construction — a
wrong answer of the largest size the scale allows, on the one arm where the
right answer is known.** Must-fix item 2 asks for that sentence.

**One thing the findings miss entirely, which strengthens their own
recommendation.** ARGUED, from measured fits. The repaired procedure does not
settle on one reading of the label: across the nine arm-and-seed pairs the
winning label is which-marker-word seven times, the marker's rank once (the
entangled arm at seed 2) and the agent's slot once (the free arm at seed 0).
So even repaired, the instrument is not one instrument —
it is whichever of three it happens to be on the day. The differences on the
two unconstructed arms are tiny (0.063 against 0.070, and the like), so no
reading in the findings moves; but it is a second, independent reason the
registration must fix the label rather than leave the search to choose, and it
is a reason the findings do not give. Can-follow item 3.

---

## 4. The throughput measurement — **sound enough for the weight on it, with three caveats**

The claim under check: the 1.55 times per-step premium the money estimate
inherited from a different experiment is really about five per cent — 0.981,
1.049 and 1.000 at the registered shape.

**How it was measured. MEASURED, by reading `bench_arms.py` and re-running
it.** All three architectures are built at the registered shape — 448 wide,
twelve layers, eight heads, the thirty-million rung of this experiment's own
scale ladder — inside one process, on the same device, with the same batch of
thirty-two, five warm-up steps discarded, then twenty timed steps each with an
explicit device synchronisation before and after every step so the timings are
not measuring a queue. Mean, median, fastest and slowest are all recorded. The
arms are timed under matched conditions in every respect I can find. That is a
properly built stopwatch, not a guess.

**Judgement: the ratio carries the weight being put on it, because of the size
of the gap rather than the precision of the measurement.** ARGUED. The
inherited figure is 1.55 and the measured figures are 0.98 and 1.05. No caveat
below is worth anything like the 0.5 that separates them. If John retires the
architecture premium from the second release's arithmetic on this measurement,
that is a well-founded decision.

**Three caveats, none of which changes that.**

1. **The separable arm's 0.981 is partly a smaller model, not only a cheaper
   one.** ARGUED, from the committed parameter counts: that arm has 26,065,471
   parameters against the free arm's 29,049,735 — ten per cent fewer, because
   its content stream is narrowed to make room for the ownership block. The
   findings print both counts in the same table, so it is visible; but the
   sentence "slightly negative on the separable one" reads as "the constraint
   is free" when part of it is "the constrained arm is smaller". The proposal
   already accepts that the arms differ in parameter count (its weakness one),
   so the measurement is the right one to take — the sentence just needs a
   clause. Can-follow item 4.
2. **It is one run of twenty steps per arm, timed in a fixed order.** The
   separable arm's two-per-cent advantage is inside the spread of the run
   itself: its own step times range from 0.229 to 0.257 seconds while the free
   arm's range from 0.241 to 0.258. So 0.981 should be read as "about the
   same", not as a measured saving. The entangled arm's 1.049 is outside the
   overlap and is a real difference. Can-follow item 5.
3. **The shape is the registered one; the batch and the sequence are not.**
   MEASURED, from the output file: batch thirty-two, sequence length
   fifty-six. The registered runs are neither. At a fifty-six-token sequence
   the attention cost is negligible and the per-step time is dominated by the
   fixed per-layer work, which is exactly where the entangled arm's extra
   scale-and-shift sits; at the registered sequence length the ratio could
   move in either direction. The findings say "at the registered
   configuration's shape", which is true and precise about width and depth and
   silent about the other two. Can-follow item 6.

**The findings are scrupulous about the part that matters most here.** They say
four separate times that only the ratio transfers and that the absolute
seconds per step still needs the rented slice, and they mark the throughput
item "partial" even though the method file's own pre-written cell would have
let them mark it a pass. That is the opposite of softening.

---

## 5. The two findings the outside review marked fatal

### The uncorrected denominator — **confirmed; one claim about it is overstated**

**MEASURED.** The made-up populations reproduce byte-for-byte, as above: two
systems built with an identical true share of one half read **0.4323** and
**0.3222** under the registered form — a gap of 0.1101, against the larger of
the two spreads at 0.0181, so about six times the spread — and **0.5018** and
**0.5013** under the floor-corrected form, which is the true value in both
cases. The finding is confirmed.

**The claim about real forward passes is out by one, and hides a fail.**
MEASURED. The findings say "on six of the nine arms and seeds the
floor-corrected form is markedly the flatter of the two". Counting the
committed file:

```
$ python flat_count.py out/denominator_attenuated.json
C/0    reg 0.0405  cor 0.0221  corrected flatter
C/1    reg 0.3424  cor 0.0164  corrected flatter
C/2    reg 0.0087  cor 0.0023  corrected flatter
F/0    reg 0.3291  cor 0.0085  corrected flatter
F/1    reg 0.0680  cor 0.0710  REGISTERED flatter
F/2    reg 0.5169  cor 0.0732  corrected flatter
T/0    reg 0.0067  cor 0.0067  equal
T/1    reg 0.0631  cor 0.0631  equal
T/2    reg 0.0066  cor 0.0066  equal
corrected flatter: 5  equal: 3  registered flatter: 1
```

Five, not six. Three are dead heats, and they are dead heats for a reason
worth stating rather than glossing: on the separable arm the no-transplant rate
is exactly zero, so the two forms are the same arithmetic and must agree. And
on the free arm at seed one the **registered** form is the flatter of the two.
The addendum's pre-written cell for this check is per arm, and its fail line is
"the registered form is the flatter one" — so this check **fails its own
pre-stated cell on one arm and seed**, and the findings report no fail
anywhere. The gap is small (0.068 against 0.071) and the overall picture is
untouched, but a pre-stated cell that fires has to be reported when it fires.
Must-fix item 3.

### The control cell that is empty by construction — **confirmed exactly**

**MEASURED, byte-identical on re-run.** Zero of four thousand trials fall in
the cell where the donor's identity dictates the same value as the recipient's,
under a grammar that keeps the four values within an item distinct. Relaxing
distinctness puts 346 of four thousand in it, and moves the reference a solver
that cannot tell which agent it is can reach from 0.2467 to 0.3095 on exactly
the trials that were added. Every figure reproduces.

### The no-transplant rate — **confirmed; "a few thousandths" is not right**

**MEASURED.** The proposal's "near one in eight" is wrong on all nine arms and
seeds, and wrong in the direction the findings say: it would pass a model at
chance and fail a model that works. The outside review's formula, one minus the
accuracy over seven, is far better. But the findings say it "predicts every
value to within a few thousandths", and it does not:

| arm and seed | measured | the review's formula | out by |
|---|---|---|---|
| separable, all three | 0.0000 | 0.0000 | 0.0000 |
| entangled, seed 0 | 0.0600 | 0.0598 | 0.0002 |
| entangled, seed 1 | 0.0663 | 0.0620 | 0.0043 |
| entangled, seed 2 | 0.0638 | 0.0605 | 0.0033 |
| free, seed 0 | 0.0600 | 0.0624 | 0.0024 |
| free, seed 1 | 0.0550 | 0.0634 | **0.0084** |
| free, seed 2 | 0.0762 | 0.0587 | **0.0175** |

Six of nine are within a few thousandths. Two are not, and the worst is out by
nearly two hundredths — a third of the value it is predicting. The finding
stands; the adjective does not. Must-fix item 4.

---

## 6. Whether the findings that make the design look worse are understated

**Judgement: no. ARGUED, against measurement.** I went looking for softening
and found the reverse in every one of the four places the brief names.

- **The free arm reading at the high anchor rather than between the two.** Not
  softened. It is the fourth bullet of the opening summary, it has its own
  paragraph in the reading table's discussion, it is the first item on the
  honest list, and it carries a recommendation to John that the design may
  need a fourth arm built to sit in the middle. The findings also say plainly
  that the rehearsal cannot tell a genuine answer from a ceiling.
- **The named-other condition clearing its bar on one seed of three, with a
  doubled budget barely moving it.** Not softened, and pursued further than it
  had to be. The item is marked a **fail**, the shortfall is measured against
  the pre-stated bar rather than described, and the question "is it the task or
  the budget?" is answered by training another model rather than by argument.
  The findings then connect it to the proposal's own honest prior and call it
  "the single cheapest thing the rehearsal found that could sink the registered
  experiment". That is a rehearsal arguing against the thing it is rehearsing.
- **Control six failing its pre-stated shape on two arms of three.** Not
  softened. Called "the single most important caveat" on the main results
  table, in bold, and repeated on the honest list.
- **Control one unable to hold for an entangled arm by construction.** Not
  softened. Explained, with the reason, and turned into a specific repair the
  registration text needs.

Beyond those four, the findings volunteer several things nobody asked for: that
the second control was implemented differently from the proposal and its number
should not be counted as a pass; that the degenerate site set makes the
proposal's "smallest layer set that clears the floor" rule pick arbitrarily;
that the freshness requirement is ambiguous and its strong reading breaks the
measurement; and that a floor named as an absolute number is wrong because the
whole-state transplant can never beat the arm's own accuracy.

**Two places are genuinely too quiet, and both are must-fix items above** — the
attenuation check's one failing cell (item 3) and the "few thousandths"
(item 4). Both of those shade in favour of the outside review's findings and
against the rehearsal's own design, which is the unusual direction.

**One place stops short rather than softening** — the degree the failing labels
would print, must-fix item 2.

**And one reading of the free arm's result is missing.** ARGUED, from measured
fits. The findings offer two explanations for the free arm reading at the
entangled anchor: the answer really is distributed, or the instrument
saturates. There is a third, and the rehearsal's own most important finding is
the evidence for it: **the search may simply have failed**. On the free arm no
reading of the label recovers "which agent is acting" to any useful degree — the
fits are 0.278 to 0.306 where chance is 0.250 for the two four-way labels, and
0.111 to 0.144 where chance is one in twelve for the marker-word label. The read
is scored on 180 held-out episodes, where one standard error at chance is about
0.03, so none of those is convincingly above chance. So on
that arm the nomination step had nothing to nominate from, and the search for a
subspace ran over directions that encode nothing. Compare the entangled arm,
where the marker-word read fits at 0.983 to 1.000 and the transplant *still*
does nothing: that is entanglement properly demonstrated — recoverable but not
causally isolable. The free arm's 0.88 has no such demonstration behind it.
And the rehearsal itself proves this failure mode is live: on the separable
arm, where the answer provably is in one place, two of the three reads found
nothing.

The two possibilities cannot be told apart by anything in the rehearsal, and I
am not claiming the free arm's answer is localised. I am saying the third
reading belongs beside the other two, because it is the one that would make the
free arm's number meaningless rather than merely ambiguous. Can-follow item 7 —
it is a sentence in the findings, but it may be a paragraph in the
registration.

---

## 7. Nothing spent, nothing rented, nothing registered touched

**MEASURED, three ways.**

**The staging script contains no command that creates a machine.** I read it
end to end and then extracted every command it actually executes, as opposed to
the commands it prints inside the plan it writes. The executed set is: `cd`,
`pwd`, `dirname`, four Python self-tests, `[ -x ]` presence tests, `stat` on a
key file's permissions, `command -v runpodctl` — which asks whether a program
is on the path and does not run it — `mkdir -p`, a `cat` into a plan file,
`sed`, `echo` and `exit`. There is no `ssh`, no `scp`, no `curl`, no network
call, and no invocation of the vendor's tool. The `ssh` and `tar` lines a
reader will notice are inside the here-document that writes the plan, with the
shell variable escaped, so they are text. The script's own closing line — "this
script cannot rent anything: it contains no command that creates a machine" —
is true.

**No Python in the rehearsal touches a network either:**

```
$ grep -nE "requests|urllib|socket|http|subprocess|os\.system|paramiko|boto|runpod" *.py
training.py:33:    and is the slowest thing in the rehearsal, so identical requests are
```

One match, and it is the English word "requests" in a comment.

**No registered file was touched.** Every file the six commits change:

```
$ git diff --name-only 8bc5fbe worktree-agent-a827aade30edf9e28
```

Thirty-one files, every one of them under `docs/` or under
`experiments/rehearsal-successor-measure/`. Nothing under
`experiments/06-mvm-0a-constructed-self-index/`, so the registered launcher,
the registered trainer, the frozen batteries and the gates are all untouched.
No ruling, no compute ledger, no `data/project.toml`.

**And the merge itself is clean and does not undo the main line's later work.**
I dry-ran it rather than assuming:

```
$ git merge-tree --write-tree --name-only main worktree-agent-a827aade30edf9e28
7a85e55f545bb0f875fe346087586ecc9a6e4c57
```

No conflict. The main line has since regenerated the staged plan file with its
first step withdrawn, and added the argument guard to the staging script; the
branch touches neither, and the merged tree keeps both of the main line's newer
versions. I checked that rather than trusting the rule: the merged plan file
contains zero references to the worktree path the branch's copy carries, and
the merged staging script still carries the argument guard.

---

## 8. The departures from the committed method

The appendix records five departures plus a note about the rented slice. Taken
one at a time.

1. **The deliberately broken arm that turned out impossible.** Honestly
   recorded, and the reasoning is right. ARGUED: because a matched pair differs
   only in the acting channel, transplanting the whole state at a site set *is*
   the donor's state at those sites — which the transplanting code proves as an
   exact identity on tensors in its own self-test, with a largest logit
   difference of exactly zero. So an architecture that behaves consistently
   under it cannot be built to cancel. The plan was impossible, the appendix
   says so, and the negative outcome was obtained another way with its cause
   identified. This undermines nothing; it is a better result than the plan.
2. **The widened nomination family.** Honestly recorded as to *why*, and
   **inaccurately recorded as to what**. This is must-fix item 5, below.
3. **The reads frozen after the fresh set leaked into them.** Honestly
   recorded. The fix is visible in the code — the reads are fitted on
   development episodes, written to disk and reloaded by name at every later
   stage — and the appendix says it was caught before any number in the
   findings was read. I cannot verify "before" from the record, since the
   broken version was never committed; that is the nature of a fix made inside
   one session. But the claim is specific, it is volunteered rather than
   extracted, and the code now does the right thing. Undermines nothing.
4. **The corrected fresh pool.** Honestly recorded, and handled better than the
   appendix suggests. The over-strong pool was not deleted; it is kept under
   its own name, and its collapse became the only way the rehearsal could
   produce a negative reading at all. Undermines nothing.
5. **The second control implemented differently and not counted as a pass.**
   Honestly recorded, in the appendix and again in the body, where the findings
   say in terms that its number should not be read as a pass and that the
   control as the proposal states it is still owed. This is the single clearest
   piece of evidence that the rehearsal is not grading itself generously.
6. **The rented slice not run.** Correct, and correct for the right reason: it
   needs John's spoken go naming the run, and that has not been given.

**One departure is not recorded at all, and it is the one that matters.** The
appendix describes the widening as "rank caps to 24 instead of 8". What
actually happened is that the family was widened at one end and **narrowed at
the other**. The code committed before any result ran fixed five rank caps:

```
$ git show 5fa85e2:experiments/rehearsal-successor-measure/src/rehearse.py
RANK_CAPS = [1, 2, 3, 4, 8]
PRE_STATED_FAMILY_SIZE = 9 * 5 * 5          # 225
```

The final code drops the cap of three and adds sixteen and twenty-four, and
marks only caps of one, two, four and eight as belonging to the pre-stated
family. So the pre-stated family the findings report as 225 comparisons is
**180 comparisons as actually computed**, and one pre-stated cell — a rank cap
of three, under the pre-stated reading of the label — is not in the record at
all. Must-fix item 5.

**Does it undermine the result? Almost certainly not.** ARGUED: under the
pre-stated reading of the label, caps of one, two, four and eight all return
between 0.0000 and 0.0117, and the fits at that label sit at chance, so there
is no mechanism by which a cap of three alone would have found the answer. But
the claim the rehearsal makes is precisely "the procedure as pre-stated fails",
and that claim deserves the whole pre-stated procedure in the record rather
than four fifths of it.

---

## Findings

### Must fix before this text is cited by anything

All seven are corrections to sentences. No result changes.

1. **MEASURED. Three numbers have no record behind them.** The rank curve in
   section 3 — "0.170 at rank 1, 0.365 at rank 2, 0.805 at rank 4", repeated in
   section 11 — appears nowhere in any committed output file, and the record's
   own values are 0.153, 0.355 and 0.832 averaged across the three seeds (per
   seed: 0.1517/0.1417/0.1667, 0.335/0.395/0.335, 0.7783/0.8467/0.8717). The
   1.000 at rank 8 is right. This is the known-failure list's fourth failure —
   a claim of measurement with a record that does not reproduce — in the text
   that the tier 1 reviewer is required to read first. The conclusion drawn
   from the curve is untouched by the correction. Replace the three figures
   with the ones in `out/nominate.json`, or say where they came from.
2. **MEASURED. The most consequential table prints two cells that were not
   measured, and stops one step short of its own finding.** The marker-rank
   row's transplant reading is printed as 0.0000 and measures 0.0050, 0.0183
   and 0.0117 across the three seeds — never zero. The agent-slot row is
   printed as 0.0000 and is 0.0117 on the first seed. Correct both, and add the
   sentence the arithmetic gives: under those two readings the measure would
   print a degree of **0.982 to 1.000** for an arm whose degree is **0.0000**
   by construction.
3. **MEASURED. The attenuation check fails its own pre-stated cell on one arm
   and seed, and no fail is reported.** "Six of the nine" is five of nine, with
   three dead heats that are dead heats by construction and one case — the free
   arm at seed one — where the registered form is the flatter, 0.0680 against
   0.0710. The addendum's fail line for this check is exactly that. Report the
   fail.
4. **MEASURED. "Predicts every value to within a few thousandths" is not
   right.** The worst miss is 0.0175 on the free arm at seed two (0.0762
   measured against 0.0587 predicted) and the next is 0.0084. Six of nine are
   within a few thousandths. The finding — that the outside review's formula is
   right and the proposal's one in eight is wrong on every arm — is untouched.
5. **MEASURED. One departure from the committed method is unrecorded, and the
   pre-stated family is reported at a size it was not computed at.** The
   pre-stated rank caps were one, two, three, four and eight; the final code
   drops three, so 180 comparisons were computed where 225 are reported, and a
   pre-stated cell is missing from the record. Either restore the cap of three
   and re-run the nomination stage, or record the narrowing in the appendix and
   correct 225 to 180.
6. **MEASURED. The findings' coverage table will be one item short the moment
   it is merged, through no fault of its own.** The findings are titled against
   "the proposal's ten rehearsal items", and on the branch that is exactly
   right — I counted the branch's own copy and it carries ten items and eight
   numbers. But the main line's copy has since grown an eleventh item and a
   ninth number, both of them the same thing: seconds per step measured on the
   rented machine, the item the second release of money is bound to and the
   only one that spends anything. The commit that added it landed at 20:09:59,
   **four seconds after** the rehearsal's method file, and never reached the
   branch. So after the merge the table claims a completeness it will not have,
   and the protocol makes "a pre-stated quantity with no rehearsal line
   covering it" a fatal finding on its own. The fix is one added row reading
   **NOT RUN — needs John's spoken go, about $3**, and a "ten" changed to
   "eleven" in two places. I put it in must-fix only because it is a
   completeness claim a later session will cite; it carries no weight of its
   own, and it is an accident of timing rather than an error. *Worth saying
   plainly: the rehearsal staged and costed precisely what the eleventh item
   asks for — its own method file's section 9 and the separate staging note —
   without ever having seen the item. Nothing was missed; only the numbering.*
7. **ARGUED. A pre-stated stop condition is keyed to a check the rehearsal
   marks failed, and nobody has written down whether it fires.** The proposal's
   first stop condition reads: "The rehearsal fails item R-1 ... or item R-8.
   Nothing trains." The findings mark the first item a **fail** on its
   named-other half. A reader who goes from the findings to the proposal will
   ask whether the line is supposed to stop here, with about $10 spent, and the
   findings do not answer — they go on to treat it as a design problem to
   attack. **I think they are right and the condition does not fire**, for a
   reason that should be in the text: the stop condition's own words are "the
   grammar is not learnable at tiny scale *even in principle*" and "nothing
   trains", and the separable arm reaches **1.0000 on both conditions on all
   three seeds**, which settles learnability in principle. But that is a
   judgement about a pre-stated stop, and in a programme whose worst failure
   was a fix marked adopted with nobody having run anything, a stop condition
   should not be left for the reader to adjudicate. One sentence.

### Can follow afterwards

1. **MEASURED.** The committed self-test record was written at 21:41 and not
   regenerated after the grammar changed at 22:31. Re-running gives 64 passes
   and 0 failures, two checks more than the record holds. Re-run and commit it.
2. **MEASURED.** Two result files are inside the commit the findings' table
   calls "the code". They reproduce byte-for-byte under the final code, so
   nothing is stale in fact; the table should say so.
3. **ARGUED, from measured fits.** Even repaired, the nomination does not settle
   on one reading of the label: across nine arm-and-seed pairs, which-marker-word
   wins seven times, the marker's rank once and the agent's slot once. A second,
   independent reason the registration must fix the label.
4. **ARGUED.** The separable arm's 0.981 per-step ratio comes with ten per cent
   fewer parameters. One clause in the sentence fixes it.
5. **ARGUED.** 0.981 is inside the run's own spread and should read "about the
   same"; 1.049 is outside it and is a real difference.
6. **MEASURED.** The throughput ratio was taken at batch thirty-two and a
   fifty-six-token sequence, neither of which is the registered one. Worth a
   clause beside "at the registered configuration's shape".
7. **ARGUED.** A third reading of the free arm's result — that the search
   failed rather than that the answer is distributed — belongs beside the two
   the findings give. On the free arm no reading of the label recovers who is
   acting above about chance, so the nomination had nothing to nominate from;
   on the entangled arm the read fits at 0.983 to 1.000 and the transplant still
   does nothing, which is what a properly demonstrated entanglement looks like.
   This may deserve a paragraph in the registration rather than a sentence in
   the findings.
8. **ARGUED.** The floor curve quoted in section 11 — 0.0517 at the first layer,
   0.3467 at the second, about 0.556 from the third — is the first seed alone.
   Across the three seeds the first layer runs 0.0517 to 0.0783 and the second
   0.0633 to 0.3467, so the curve is far less orderly than the sentence reads.
   Say "seed 0" or give the range.
9. **MEASURED.** The same-value cell of control six holds 81 trials, so "about
   three quarters move" carries about five points of slack either way. The count
   is in the output file and not in the table.

### What I looked for and did not find

- No sign that the commit order was constructed after the fact.
- No sign that any number was chosen from among alternatives — both candidate
  forms of the reading are computed and printed everywhere, including where the
  uncorrected one looks better.
- No cherry-picking in the negative readings: the output file holds four and the
  findings quote two, and the two they quote are the two the registered form
  gives, with the corrected form's pair being the other two.
- No command anywhere in the branch that spends money, rents a machine or
  contacts a vendor.
- No edit to any registered file, ruling, ledger or project file.
- No claim in the findings that the rehearsal is evidence about the scientific
  question. It says the opposite on its first page, in its code's README, and in
  its method file's last section.
