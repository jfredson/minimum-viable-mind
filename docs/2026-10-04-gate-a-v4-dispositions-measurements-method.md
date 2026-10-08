# Two $0 measurements behind the proposed dispositions of the inside review of proposal version 4: method, committed before any output

*Written 2026-10-04 (Pacific) by a Claude Code session on branch
`gate-a-v4-dispositions`, cut from the review branch
`gate-a-registration-review-successor-v4` at `0fcc25c` (pull request 94).
**Committed and pushed before either script is run on any committed model.**
The commit that carries this file and the two scripts carries no output; the
output, with the command and what it printed, is a later commit. Laptop only,
on the processor. Nothing is trained, rented or spent: $0.*

*Written under the workspace plain-language rule. These are rehearsal records
on the committed toy models, made to inform two proposed dispositions. They
are not results about the scientific question, and no number here is a bar
for anything until John rules it into the registration text.*

**What this session opened before writing this.** The inside review of
version 4,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`,
in full, and two of its scripts (`width_vs_count.py` and its output); the
passages of version 4 those findings cite (sections 1, 3, 4.1, 5.2, 5.4, 6.4,
7.2 item 1, 7.3 item 4, 7.4, 8, 9, 11 and 12.3, read in full); the ruling
files of 2026-10-04 and the page 1h ruling of 2026-09-26; the rehearsal code
the scripts call (`grammar.py`'s header and episode fields, `training.py`'s
`accuracy` and `make_data`, `repairs.py`'s gate stage and model builders,
`rerun_v3.py`'s model loader, `rehearse.basis_for`); the gate file's field
list. It has not run either script, and has not seen any figure either
prints. It wrote none of the code it calls.

## Part A. Can the free model's channel-removal check carry an ownership-free part that this task can evaluate? (for the fatal finding RT-237)

**Why.** Version 4, section 8.2, gates the free model's reading on a check
that zeroes its acting channel (the input that tells the model "this turn is
yours"), and ends: "the ownership-free state and syntax batteries must hold".
Those batteries are the closed design's end-of-episode question sets; the
successor's task has none. The proposed disposition replaces the clause with
something this task does have. What the clause was for, read from the
proposal of 2026-09-26 that John ruled on (page 1h): to show the lesion
removed the ownership answer and not the model's whole grip on the episode.
In this task the part of the act that needs no ownership is: find the item
the action names, take the four agents' earlier values on it, and apply the
successor rule. A model that has lost only "which agent am I" still picks
among those four answers and is right about one time in four, which is
exactly the collapse level the gate already assumes (the competing solver
with no channel scores 0.234 to 0.238). A model whose lesion broke the rest
of the act does not.

**The quantity (pre-stated).** On the 3,000 held-out gate episodes the
learn-both gate uses (`repairs.stage_gate`: 1,500 development pairs,
generator seed 99), with the acting channel zeroed, the **candidate count**:
the number of own-directed actions whose answer is the successor of one of
the four agents' values on the item named. Printed beside it: the correct
count, the count of answers that are any of the eight value words, the same
three for the named-other condition, and all six with the channel on.

**The line (pre-stated, from chance, not from any toy figure).** A model
guessing among the eight value words lands on one of the four candidates
half the time. The ownership-free part "holds" on a seed if the candidate
count is above one half at the 0.05 level, one-sided, by the exact binomial
tail on 3,000 episodes (the same construction as the learn-both bar of 790);
the script computes the count and prints it, and this session expects it to
be about 1,546. It holds for a model if it holds on at least two seeds of
three, the clause the collapse already uses.

**On which models.** The twelve committed toy models of the base recipe
(arms T, C, M and F, seeds 0 to 2), checked against
`out-repairs/models/SHA256SUMS` before loading; the ordinary competing
solver's three models (no acting channel at all; "zeroed" changes nothing
for them); and, as the negative control, three models of the free model's
architecture with freshly drawn, untrained weights (seeds 1000 to 1002).

**What this session expects, said now.** Every trained model, and the
competing solver, holds by a wide margin with the channel zeroed (candidate
counts near 3,000), on both conditions. The untrained models do not hold.
The correct counts with the channel zeroed match the gate file's
`lesioned_own` to within a few episodes (the gate file was computed on the
graphics chip; this runs on the processor).

**What would count against the proposed repair.** Any free-model seed
whose candidate count with the channel zeroed falls below the line: the
repair would then be a new way for the free model to go unread, for a reason
nobody has looked at, and the disposition would recommend striking the
clause instead. An untrained model that holds: the check would not detect a
broken model, and is worthless as a gate. Either is reported as found.

**Script.** `experiments/rehearsal-successor-measure/src/lesion_content_check.py`.
Output: `experiments/rehearsal-successor-measure/out-lesion-content-check/`.

## Part B. Which repair keeps the fit floor reachable at the registered width? (for the serious finding RT-240)

**Why.** The ruled counts fit every read on 420 development episodes and
score it on 180. The toy's state is 160 wide; the registered model's is 448.
The inside review appended 288 coordinates of independent noise to the
committed toy states and found the entangled model's read fell under 144 of
180 on two seeds of three. It named three repairs: more development episodes
for the read; regularisation fixed in advance; or a rehearsal at width 448.
The first two can be compared on the same stand-in at $0. The third needs a
trained 448-wide model and is not run here.

**What is run.**

1. The review's stand-in reproduced exactly: the same 600 episodes, the same
   five noise draws (generator seed 20261004), the same five models and
   layers (arm C seeds 0 to 2 at layers 2, 1 and 1; arm M seed 0 and arm T
   seed 0 at layer 1). **Pre-stated check:** the counts equal the review's
   committed output (`width_vs_count.out.txt`) exactly. If they do not, the
   script is not measuring what the review measured, and parts 2 to 4 are
   reported as unusable.
2. A pool of 1,980 development episodes (the same generator, seed 4242), the
   last 180 held out for every fit, so that every count below is on the same
   180 episodes. The read is fitted on the first 420, 900 and 1,800, with the
   registered regularisation (scikit-learn's default, C = 1.0); five noise
   draws each; the whole read's count and the 8-direction piece's count.
3. On the same pool, at 420 fitting episodes, the read fitted with C = 0.1
   and C = 0.01.
4. With no noise, the toy's own 160 coordinates: every one of the twelve toy
   models, at every layer 1 to 4, the whole read and the piece at each of the
   three fitting sizes.

**What this session expects, said now.** At width 448, 1,800 fitting
episodes bring every entangled seed's piece back above 144 on every draw;
900 brings most of them back; stronger regularisation at 420 helps less and
less evenly. At width 160 nothing changes a verdict: arms T, C and M stay
above 144 and the free model stays far below it at every size, as it does at
420 (best piece 34 of 180 on the committed record).

**What would count against the repair the disposition is likely to
propose (more fitting episodes).** If 1,800 does not restore the entangled
seeds above the floor on the stand-in, more episodes are not shown to help
and the disposition says so. If the free model's read clears 144 at width
160 with more fitting episodes, the toy's recorded verdict for the free
model ("no verdict, read failed its floor") would change under the repair,
and the repair then needs the toy re-run before registration rather than
after; that is reported, not hidden.

**What this cannot show.** A wider model's extra coordinates carry
structured content, not independent noise. So part 2 and part 3 show only
which repair copes with the failure the review's stand-in produces; they do
not show what a trained 448-wide model does. That is said beside every
figure taken from them.

**Script.** `experiments/rehearsal-successor-measure/src/width_fit_pool_standin.py`.
Output: `experiments/rehearsal-successor-measure/out-width-fit-pool-standin/`.

## What is owed after this

The output is committed with the command and what it printed, and the
dispositions cite it. Both measurements are owed a check by a session that
did not run them (`docs/outside-review-protocol.md`, "The pairing rule"),
which is named in the disposition file as part of the check owed on it.
