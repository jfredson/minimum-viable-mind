# The test of a differently coded decoy (weakness W18): method, committed before any test code

*Written 2026-10-08 (Pacific) by a Claude Code session in its own worktree,
on branch `decoy-test-w18`, cut from `origin/final-batch-before-registration`
at `6c47c56` (the main line plus one reporting fix, pull request 153).
**This file is committed and pushed alone, before any test code is
written.** The test code is a second commit, made before any of its outputs
exist; the findings, with every command and output, are a later commit. The
commit order is the check that this came first. Laptop only, on the
processor. Nothing is rented, trained or spent, and no paid service is
called: $0.*

*Written under the workspace plain-language rule. What is tested is a
**constructed stand-in**: a committed toy model with extra numbers bolted on
by hand. It is not a trained model, and nothing it shows is a property of a
trained model.*

## 1. Why this test exists

John ruled on 2026-10-08 that a ruled test of a differently coded decoy be
run before the registration commit: laptop only, $0, method written first,
checked by another session (item 8 of
`docs/rulings/2026-10-08-v5-open-items-rulings.md`; it follows the red-team
ledger's row for the decoy worry, RT-247, in
`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`).

**The question** is weakness W18 of version 5 of the registration text
(`docs/successor-experiment-proposal-2026-10-07-v5.md`, section 13; also
section 10, rehearsal item R-12). The measurement fits a straight-line read
of "which marker word is mine" and transplants only the few directions that
read leans on most. Can an unused representation, coded differently from the
one the model acts on, pull those directions away from the part the model
uses, so that a model whose ownership answer is in fact separable reads as
partly or fully entangled?

**What has been done so far.**

- The ruled decoy test of 2026-10-06 (`docs/decoy-test-method-2026-10-06.md`,
  `docs/2026-10-06-decoy-test.md`) used an exact, scaled copy of the
  model's ownership block. It read 0.0000 on every run: not fooled. Its own
  method said in advance that an exact copy could not fool the read, because
  the read's directions then always carry the used block along in step with
  the copy.
- The check of that test (`docs/2026-10-06-check-decoy-test.md`, probe 3)
  replaced the copy with an unused code of the owner's marker word: one
  number per marker word, set by how much weight the model's own ownership
  answer puts on each agent, four times the block's typical size. At the
  site the decoy test always chose (the first running state, the action
  position, 8 directions) it read **0.28, 0.23 and 0.29** on the three seeds,
  and **0.52 to 0.96** with fewer directions, on a model whose true reading
  is 0. That probe skipped the registered nomination, the controls, the null
  and the rules that withhold a reading. This test runs that decoy through
  all of them.

## 2. Which models carry the decoy

**The three committed arm T toy models** (the separable arm, built so that
the action reads only its 24-number ownership block),
`experiments/rehearsal-successor-measure/out-repairs/models/ckpt_T_base_seed{0,1,2}.pt`,
each checked against `SHA256SUMS` in that folder before use (stop K1 below).
These are the models of the ruled decoy test, its check's probe, and the
page 4 re-run under the ruled code (pull request 151), whose arm T rows read
0.0000 on all three seeds with the registered nomination at the first running
state, the action position, 8 directions
(`experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000/`).
That is the unaltered reference this test is compared with.

**No other arm carries the decoy, and why.** The decoy question is whether a
separable model can be made to read high. Only arm T is known to be
separable by construction, so only on arm T does a high reading have a known
right answer (0) to be wrong against. On arm C (built entangled) a decoy
could only raise a reading that should already be about 1, which tests
nothing; and on the toy, arms C and M are withheld on every seed by the
in-use check (their built route is not in use at the ruled bar; the page 4
re-run's findings, `docs/2026-10-09-ruled-code-changes-and-page4-rerun-findings.md`),
so the registered procedure would give no reading on them to compare. Arm M
is a mixture whose right answer is itself a formula, and arm F has no known
answer. Adding a decoy to either would make a result harder to read, not
easier.

## 3. How the differently coded decoy is built

**Where the extra numbers go.** Arm T's running state is 160 numbers: 136 of
content, then the 24-number ownership block. The decoy widens every running
state to 180:

    [ content (136) | decoy code (20) | ownership block (24) ]

at every running state (after the input embedding and after each of the four
blocks, states 0 to 4) and at every position of the episode, the same layout
as the ruled decoy test with the decoy's width changed. So the decoy sits at
the same states and positions as the block, and the nomination's order
(smallest set of states, earlier position set) cannot exclude it.

**What the code holds: the check's probe 3, exactly.** There are 20 marker
words in the vocabulary, and one number in the code for each. At each
position, the number for a marker word is the weight the model's own
ownership answer puts on the agent carrying that word (the tally weights the
model computes from the acting channel, `_own_vec` in the frozen
`models.py`), times a fixed size `k`. An episode has four agents, each with
one marker word, so at most four of the 20 numbers are ever non-zero in an
episode, and only the 12 marker words these episodes draw from are ever set
anywhere (hence "one-of-twelve" in version 5's wording). Where the model's
answer is sure of its owner, the code is close to `k` on the owner's word and
0 elsewhere.

Why it is "coded differently" from the block: the block is the same weights
multiplied into each agent's 24-number learned marker vector, so the block is
a blend of learned vectors with an uneven geometry; the code is a plain
one-number-per-word indicator. The two are related by a fixed straight-line
map (the 20 learned marker vectors are independent, the check's probe 2), but
a lopsided one, which is what the check found lets the read's top directions
lie in the code without the matching movement in the block.

**The size `k`, fixed per seed before any reading:** `k = s × r`, where `r`
is the block's root-mean-square size (square root of the mean squared length
of the 24 numbers) at the own-directed action on the 600 development
recipients, exactly as probe 3 computed it, and `s` is the scale below. `k`
and `r` are written into every output.

**Variants, all stated now:**

| Variant | Code | Scale `s` | Enters the verdict? |
|---|---|---|---|
| V1, the probe's decoy, stronger | soft code (as above) | 4 | **yes** |
| V2, the same, weaker ("both ways round", as the ruled test did) | soft code | 1/4 | **yes** |
| V3, more lopsided | soft code | 16 | no, reported beside |
| V4, equal size | soft code | 1 | no, reported beside |
| V5, a hard code (not a straight-line function of the block) | `k` on the word of the agent the acting channel tallied most so far, 0 elsewhere; all 0 before the model's first own turn | 4 | no, reported beside |

V5 is there because the ruled test's findings named "not a straight-line
function of it" as the other untested form. Before the model's first own
turn the soft code is spread evenly over the four agents' words (the tally is
flat), and the hard code is all 0 there; from the first own turn on, the two
agree on which word is highest.

**How the decoy is guaranteed to be causally unused.** As in the ruled
test's `DecoyArmT`: the transplant hook runs on the 180-number state, and
then the 20 code numbers are thrown away. The next block and the action head
receive exactly the 136 content numbers and the 24-number block, as in the
committed model. The code at the next state is recomputed from the input,
never carried.

**The checks, before any reading** (on the 800 fresh pairs, every seed,
every variant; stop K2 if (a), (b), (b'), (c) or (f) fails):

- **(a)** the widened model's outputs are bit-identical to the committed
  model's;
- **(b)** transplanting the donor twin's code numbers alone, at every running
  state and every position, leaves every output bit-identical;
- **(b')** overwriting the code with large random numbers (standard deviation
  100) at every state and position leaves every output bit-identical;
- **(c)** the code is what this section says it is: at the own-directed
  action, the largest of its 20 numbers is on the owner's marker word in
  every episode; every number lies between 0 and `k`; and (soft code) each
  position's numbers sum to `k`;
- **(d)** reported: a straight-line read of the owner's marker word from the
  code alone and from the block alone, held-out correct of 180 at each state
  (expected 180 for both: the code is easily read);
- **(e)** reported: at state 0, the action position, the share of
  own-directed actions moved to the donor's answer by the whole-state
  transplant, by the block alone and by the code alone, and the readings
  those give (expected 1, 1 and 0 moved; readings 0 with the block and 1 with
  the code);
- **(f)** the gate record the frozen procedure writes for the widened model
  (accuracy, lesion, the in-use check, arm T's row-choice split) is equal,
  field for field, to the one it writes for the committed model.

## 4. The read runs through the registered procedure, not a shortcut

**The frozen code**, `experiments/08-successor-degree/src/procedure.py`,
function `run_model`, with `grammar.py`, `measure.py`, `models.py` and
`transplant.py` beside it, at `6c47c56`, **not changed**. This is the code
as ruled on 2026-10-08 (pull request 151): every read fitted on the first
1,800 of 1,980 development episodes and scored on the last 180, at an
iteration limit of 10,000; transplant passes on the 600 development pairs.
So unlike the ruled decoy test (which ran the code as frozen on 2026-10-04,
fitting on 420), this is the procedure the registration will name.

**What is substituted, and only that:** `procedure.load_model`, the function
that loads a model file, is replaced for the length of each call so that it
returns the widened model, exactly as the ruled decoy test did. Everything
after it is the frozen code: the gate and the in-use check; the one fit of
the reads, written to disk and reloaded; the full family of 45 site sets at
sizes 1, 2, 4 and 8; the pick rule with the piece floor of 144 of 180; the
reading on the 800 fresh pairs; controls 1, 3, 4, 6 and 7; the stricter and
sensitivity rows; the rider; the 200-shuffle null; and `summarise`, whose
`measure.withhold` decides whether each seed has a reading or "no verdict".
The reads are fitted fresh on each widened model.

**What the test code adds, outside the frozen procedure, for reporting
only:** where the chosen piece lies (the share of its squared size in the
code, the block and the content); the share of the fitted read's squared
weight in each, at every state; the share of the block's donor-minus-
recipient change that the chosen piece leaves unmoved (the check's probe 1
measure); and, at the chosen site, the readings at sizes 1, 2, 4 and 8 on
fresh pairs (what the probe reported). None of it changes what the frozen
code computes or enters the verdict.

The test code will be `experiments/08-successor-degree/out-decoy-w18/decoy_w18.py`.
Outputs go only to subfolders of `experiments/08-successor-degree/out-decoy-w18/`.
Nothing under `experiments/08-successor-degree/src/`, version 5 or the
red-team ledger is edited.

## 5. Seeds, sets and settings

- Models: arm T seeds 0, 1 and 2, all three, in every variant.
- Evaluation sets: the frozen `grammar.EVAL_SETS`, unchanged, at full size.
- Shuffles for the null: the registered 200.
- Processor threads: 4 per run, recorded in every output; at most two
  variants run side by side (the laptop has 10 cores and another session may
  be using it). Results do not depend on run order: each run is
  deterministic given its inputs.
- torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, scipy 1.18.0, Python
  3.12.13, from the main checkout's `.venv`, as pinned in
  `experiments/08-successor-degree/requirements-measure.txt`.

## 6. Commands

From `experiments/08-successor-degree/out-decoy-w18/`, with the main
checkout's `.venv` Python:

    python decoy_w18.py --checks-only
    python decoy_w18.py --variant V1
    python decoy_w18.py --variant V2
    python decoy_w18.py --variant V3
    python decoy_w18.py --variant V4
    python decoy_w18.py --variant V5
    python decoy_w18.py --report

Each `--variant` run writes its own checks file and stops at K2 before any
reading if a check fails. Arm T took about 6 minutes a model under this code
at 3 threads (the page 4 re-run's log), so a variant is about 20 to 30
minutes.

## 7. What counts as fooled, not fooled and inconclusive

**The ruled decoy test's own bands, unchanged** (its method, section 6). Per
seed, the figure is the frozen procedure's reading for arm T after
`summarise`: a number, or "no verdict" with its reasons. Per variant, from
its three seeds:

- **Not fooled:** at least two seeds return a reading, and every seed that
  returns one reads **0.20 or less**.
- **Fooled:** at least two seeds read **0.50 or more**, and on each of them
  the chosen piece lies **more than half** in the decoy code (by squared
  size). 0.50 because a reading that high on arm T would by itself stop arm C
  (which reads about 1 on the toy) clearing the registered separation of 0.5.
  Readings of 0.80 or more are called "fully fooled" in the findings.
- **Inconclusive:** anything else: readings between 0.20 and 0.50; seeds
  split across the bands; fewer than two seeds with a reading; or two or more
  seeds reading 0.50 or more with the piece not mostly in the code.

**Overall:** fooled if V1 or V2 is fooled; not fooled if both are not
fooled; otherwise inconclusive. V3 to V5 are reported beside and do not
enter the verdict. Band edges count inside the band (0.20 is "not fooled";
0.50 is "fooled" if the piece condition holds). Ties in the nomination are
decided by the frozen rule's own order.

**Why no change to the bands.** They were fixed before the ruled test ran,
for the same question on the same models with the same procedure; changing
them now, after the probe's numbers are known, would be fitting the bar to
the result. One thing is said plainly in advance instead: under these bands
**"inconclusive" is not a pass**. On a model whose true reading is 0, a
reading between 0.20 and 0.50 that comes with the piece lying mostly in the
unused code is the read being **partly fooled**, and the findings will say
so in those words. Where a seed reads between 0.20 and 0.50, the findings
also say whether the piece lay mostly in the code (partly fooled by the
decoy) or not (the read failing for some other reason).

**A "no verdict"** on a separable model is a failure of a different kind (the
eighth registered term, "instrument returned no reading on the separable
mechanism") and is reported as one, with the reasons `summarise` gives.

## 8. What each result would mean, said before running

The reading on arm C is high when the whole-state transplant moves the
action and the transplant along the read's chosen directions does not. The
decoy worry is that a separable model could show the same pattern because
the chosen directions lie in an unused code. For each band, what a high
reading on arm C (or on the free model, arm F, whose reading is the
scientific question) could still be blamed on:

- **Not fooled (V1 and V2 at 0.20 or less).** The registered nomination,
  searching sizes and site sets, avoids a code of this kind: a decoy of this
  family, at these strengths, cannot by itself produce a high reading on a
  separable model. A high reading on arm C would not be explainable as this
  kind of decoy. It would **not** show that no decoy could fool the read;
  only this family was tried. W18 would be narrowed to "untested for other
  codes".
- **Inconclusive, with the piece mostly in the code (partly fooled).** A
  decoy of this kind can lift a separable model's reading part of the way, to
  the figure measured. Then a reading on arm C or arm F up to about that
  figure could be decoy-made, and the registered separation of 0.5 (arm C's
  lowest minus arm T's highest) has that much less room in a model that
  carried such a code. A reading near 1 would not be explained by such a
  decoy alone; a middling one (for example arm M's band of 0.3 to 0.7, or a
  free-model reading in that range) could be. W18 stays an open weakness
  with a measured size, and should be carried into the registered text with
  that figure.
- **Fooled (two seeds of V1 or V2 at 0.50 or more, piece mostly in the
  code).** A simple unused code can make a separable model read as entangled
  through the registered procedure. Then a high reading on arm C or arm F is
  **not** evidence of entanglement on its own: it could be a separable model
  carrying an easily read but unused code, and the registered instrument has
  no step that would tell the two apart. That is a finding against the
  measure as registered, and it would be John's call whether to register
  with it named, redesign the read, or add a check.

**What would count against the measure,** said now: a "fooled" verdict;
or, short of it, any seed of V1 or V2 whose nominated reading is above 0.20
with the piece mostly in the code; or the nomination choosing a size below 8
directions on the decoy model (the probe found 0.52 to 0.96 there). What
would count for it: V1 and V2 both "not fooled", with the nominated site and
size the same as on the unaltered model.

**What this session expects (ARGUED, not measured).** The nomination picks
the site set and size with the highest ownership-only share on development
pairs, which is the lowest reading among those whose piece clears the floor.
On the probe's figures, 8 directions read lowest at the first state, so the
nomination should pick 8 directions there again, and the reading should be
near the probe's 0.23 to 0.29, though the reads are now fitted on 1,800
episodes instead of 420, which could move it either way. So this session
expects **V1 inconclusive (partly fooled), about 0.2 to 0.3**, and **V2 not
fooled**, so **overall inconclusive**. It is written here so it can be wrong.

## 9. Stops

| Stop | What happens |
|---|---|
| K1, a model file does not match `SHA256SUMS` | stop, report, run nothing on it |
| K2, check (a), (b), (b'), (c) or (f) fails | stop before any reading, report |
| K3, the frozen procedure raises an error | stop, report the error; the code is not changed and re-run without a new committed note saying why |

## 10. After the run

A findings note, `docs/2026-10-08-decoy-w18-findings.md`, with every variant
and every seed, labelled as a constructed stand-in, giving the verdict
against section 7's bands whatever it is, and what it means for W18. A pull
request with base main, not merged, owed a check by another session that
re-runs `decoy_w18.py` from the committed code.
