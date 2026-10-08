# Two $0 measurements behind the proposed dispositions of the inside review of proposal version 4: what they printed

*Written 2026-10-04 (Pacific) by the Claude Code session on branch
`gate-a-v4-dispositions` that wrote the method. The method, with both
scripts, was committed and pushed at `f13f28d` before either script ran on
any committed model: `docs/2026-10-04-gate-a-v4-dispositions-measurements-method.md`.
Laptop only, on the processor (torch 2.12.1). Nothing was trained, rented or
spent: $0.*

*Written under the workspace plain-language rule. Rehearsal records on the
committed toy models, NOT RESULTS about the scientific question. They inform
two proposed dispositions in
`docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`. They
are owed a check by a session that did not run them.*

## Part A. The ownership-free part of the act, with the acting channel zeroed (for the battery clause, RT-237)

**Command** (from `experiments/rehearsal-successor-measure/src/`):

    ~/Code/minimum-viable-mind/.venv/bin/python lesion_content_check.py

Full output: `experiments/rehearsal-successor-measure/out-lesion-content-check/stdout.txt`
and `lesion_content_check.json`. It took 91 seconds. Thirty of thirty model
files matched `out-repairs/models/SHA256SUMS` before loading.

**The line, computed and not typed:** a candidate count of **1,546 or more
of 3,000** (above one half at the 0.05 level, one-sided, exact binomial).
The method expected about 1,546.

**What it printed, own-directed condition, with the acting channel zeroed**
(of 3,000; "candidate" is an answer that is the successor of one of the four
agents' values on the item named; "legal" is any of the eight value words):

| Model | Correct | Legal | Candidate | Holds (1,546 or more)? | With the channel on: correct, candidate |
|---|---|---|---|---|---|
| Arm T, seeds 0 / 1 / 2 | 740 / 753 / 820 | 3,000 each | 3,000 each | yes, yes, yes | 3,000, 3,000 each |
| Arm C | 534 / 549 / 511 | 3,000 each | 2,236 / 2,160 / 2,132 | yes, yes, yes | 1,711 / 1,703 / 1,727; 2,328 / 2,247 / 2,289 |
| Arm M | 669 / 657 / 661 | 3,000 each | 2,770 / 2,686 / 2,660 | yes, yes, yes | 2,592 / 2,584 / 2,600; 2,794 / 2,788 / 2,785 |
| **Arm F, the free model** | 528 / 555 / 582 | 3,000 each | **2,100 / 2,238 / 2,324** | **yes, yes, yes** | 1,679 / 1,654 / 1,664; 2,289 / 2,197 / 2,274 |
| Competing solver (no channel) | 702 / 715 / 702 | 3,000 each | 2,784 / 2,880 / 2,768 | yes, yes, yes | (the same: it has no channel) |
| **Untrained weights (negative control)** | 0 / 157 / 181 | 0 / 1,262 / 1,536 | **0 / 620 / 726** | **no, no, no** | (the same within a few episodes) |

Verdict on two seeds of three: holds for arms T, C, M and F and for the
competing solver; does not hold for the untrained models. The named-other
condition, printed beside it in the output, holds on every trained model too
(candidate counts 2,070 to 3,000 with the channel zeroed).

**Does the check reproduce the committed gate file?** Yes. The correct counts
with the channel on and zeroed equal `out-repairs/gate_base.json`
(`own_correct`, `other_correct`, and `lesioned_own` times 3,000) on all
twelve arm models and the solver's three, episode for episode, though that
file was computed on the graphics chip:

    $ python -c "...compare out-repairs/gate_base.json runs with lesion_content_check.json models..."
    T 0 gate file lesioned own 740 this run 740 | gate own 3000 this run 3000 | other 3000 3000
    ...
    F 2 gate file lesioned own 582 this run 582 | gate own 1664 this run 1664 | other 746 746
    blind 0 702 702   blind 1 715 715   blind 2 702 702

**Against what the method expected.** The verdicts are as expected. One
expectation was wrong in size: the method expected candidate counts "near
3,000" on every trained model. Arms T and M are near it; arms C and F are at
2,100 to 2,330 with the channel zeroed, and only 2,197 to 2,328 **with it
on**. So even intact, the entangled and free models answer with a value
outside the four candidates about one time in four. The free model's margin
over the line is 554 to 778 episodes, about twenty to twenty-eight times the
binomial spread at one half (27 episodes). Nothing in the method's "what
would count against" list happened: no free-model seed fell below the line,
and no untrained model cleared it.

**What it shows.** The successor's task has an ownership-free part of the act
that can be evaluated with the channel zeroed, on a field every gate run can
record, against a line set from chance. It refuses a broken model (untrained
weights, 0 to 726 against 1,546) and passes every trained toy model and the
solver with a wide margin. **What it does not show:** anything about the
registered size; and the line was set from chance, not tuned, so a lesion
that halves a model's content-tracking would still pass. It is a check that
the lesion did not break the act wholesale, which is what the clause it
would replace was for, and not more.

## Part B. More fitting episodes against stronger regularisation, on the inside review's width stand-in (for RT-240)

**Command** (from the same directory):

    ~/Code/minimum-viable-mind/.venv/bin/python width_fit_pool_standin.py

Full output: `experiments/rehearsal-successor-measure/out-width-fit-pool-standin/stdout.txt`
and `width_fit_pool_standin.json`. It took 87 seconds. scikit-learn printed
twenty "failed to converge after 3000 iterations" warnings; the script does
not record which fits they came from, and the registered read uses the same
iteration limit. This is a limit of the record, stated.

**1. The review's stand-in reproduces exactly.** All five cases, every count
(width 160 whole and piece; five draws of whole and piece at width 448),
equal `width_vs_count.out.txt` beside the review:

    C/0 True  C/1 True  C/2 True  M/0 True  T/0 True
    cases identical to the review: 5 of 5

**2 and 3. On a fixed 180 held-out episodes** (the last 180 of 1,980), the
smallest of five noise draws for the 8-direction piece, against the floor of
144 (NOT A RESULT: independent noise stands in for a wider model's own
coordinates):

| Model, layer | Fit on 420 (as ruled) | Fit on 900 | Fit on 1,800 | 420, C = 0.1 | 420, C = 0.01 |
|---|---|---|---|---|---|
| Arm C seed 0, layer 2 | 157 | 174 | 179 | 159 | 162 |
| **Arm C seed 1, layer 1** | **74** (pieces 74 to 87) | **120** (120 to 131) | **156** (156 to 162) | 78 | 85 |
| **Arm C seed 2, layer 1** | **129** (129 to 148) | 168 | 177 | 140 | 141 |
| Arm M seed 0, layer 1 | 180 | 180 | 180 | 180 | 180 |
| Arm T seed 0, layer 1 | 180 | 180 | 180 | 180 | 180 |

The whole read moves the same way (arm C seed 1: 87 to 97 at 420, 121 to 134
at 900, 165 to 170 at 1,800).

**4. At the toy's own width, more fitting episodes change no verdict.** Best
piece at any layer, fit on 420 / 900 / 1,800: arms T and M 180 on every seed; arm C 180 / 180 / 180, 177 / 178 / 180,
179 / 180 / 180; **arm F 28 / 37 / 41, 18 / 20 / 19, 23 / 26 / 37**, far
below 144 at every size. (These are on the pool's held-out 180, not the
registered toy's, so they differ by a few episodes from the committed
figures, which are 34 at most for arm F.)

**Against what the method expected.** Partly as expected, partly not.
1,800 fitting episodes brought every entangled seed above the floor on every
draw, as expected. **900 did not**: arm C seed 1 stays at 120 to 131, so the
method's "900 brings most of them back" was wrong for the seed that matters.
**Stronger regularisation did not help on the seed that fails worst** (78 to
93 on arm C seed 1 at the two settings) and did not bring arm C seed 2 to the
floor; the method said it would help "less and less evenly", which
understates how little it did. Nothing at width 160 changed a verdict, and
the free model stayed far below the floor, as expected.

**What it shows, and what it does not.** On the review's stand-in, the
failure the review found is a shortage of fitting episodes for the number of
coordinates, and fitting on 1,800 removes it where fitting on 900 or
regularising harder does not. It does not show what a trained 448-wide model
does: its extra coordinates are not independent noise, and could make things
better or worse. And 1,800 is the smallest of three sizes tried that worked,
not a size derived from anything.

## What is owed

A check of both parts by a session that did not run them: rerun both scripts
and compare value for value with the committed JSON files; and, for part A,
recompute the candidate counts from code that does not import
`lesion_content_check.py`.
