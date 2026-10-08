# Check of the decoy test (pull request 108): method, committed before any recompute

*Written 2026-10-06 (Pacific) by a Claude Code session that did not write the
decoy test, in its own worktree on branch `check-decoy-test-a6`, cut from the
decoy test's branch `decoy-test-a6` at `6794155`. **This note and the probe
script below are committed and pushed before anything is re-run.** Laptop,
processor only, $0: nothing rented, trained or spent.*

The test being checked is page 10 of the Gate A addendum (finding A6 of the
ChatGPT outside review of version 4: "a readable but unused copy of the
owner's marker could make a separable model read as entangled"). Its method
is `docs/decoy-test-method-2026-10-06.md`, its findings
`docs/2026-10-06-decoy-test.md`. John's ruling on page 10 is recorded in
`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md` on branch
`rulings-2026-10-06-gate-a-v4` (the record of John's twelve-page rulings,
pull request 103); the test it adopts is drafted in the A6 section of
`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`
(lines 375 to 397) on branch `gate-a-v4-tier2-dispositions`.

## 1. The three questions

1. **Do the numbers reproduce?** Re-run the decoy test's own commands from
   its committed code and compare.
2. **Is the test as built the test John ruled, and was its method really
   first?** Read the ruling against the method and code; read the git
   history.
3. **Did the test have power?** Could the decoy, as built, have produced a
   "fooled" result at all? And is there anything that would change "not
   fooled", or wording that claims more than was shown?

## 2. Reproduction (question 1)

From `experiments/rehearsal-successor-measure/src/`, with
`/Users/john/Code/minimum-viable-mind/.venv/bin/python` (torch 2.12.1,
scikit-learn 1.9.0, numpy 2.5.0, scipy 1.18.0, Python 3.12, confirmed before
writing this note), code unchanged from the decoy test's branch:

    python decoy_test.py --checks-only
    python decoy_test.py --scale 4         # these two in parallel, as the original ran
    python decoy_test.py --scale 0.25
    python decoy_test.py --scale 16        # supplementary, then
    python decoy_test.py --scale 0.0625
    python decoy_test.py --report

These overwrite the committed files in `out-decoy-test/` in this worktree
only; `git diff` against `6794155` is then the comparison.

**Pass:** every check (a), (b), (b'), (c), (d), (e) gives the same value;
for every scale and seed, the reading, the "reading or no verdict" status,
the site set chosen, and the piece and read-weight shares agree to the four
places printed in `table.md`; `verdicts.json` is identical. Any difference in
those is reported as a failure to reproduce, with the figures. Differences
only in timings or absolute paths are reported but are not failures. I will
also say whether the `row_T_seed*.json` files and `.npz` reads are
byte-identical (not required to pass).

## 3. Ruling and history (question 2)

No compute. I check, and report each as holds / does not hold:

- The ruling's adopted test (exact unused copy, arm T toy models, registered
  nomination and reading unchanged, both ways round with the copy at larger
  then smaller scale than the slot, at the same states and positions, method
  first, $0, checked) against the method note and `decoy_test.py`.
- That `decoy_test.py` substitutes only `procedure.load_model`, and that the
  frozen folder `experiments/08-successor-degree/` is unchanged between main
  at `53ae82c` and the branch tip.
- That `DecoyArmT` discards the decoy before every block and the head.
- That the method-and-code commit `f3481a2` holds no output, comes before
  every output commit, and that the code is unchanged after it; and what the
  commit times, push events and logs say about whether any run began before
  the method was committed.
- Any departure between what the method said would be run and what was run.

## 4. Power (question 3)

**The argument to be tested (ARGUED here, before measuring).** The
registered read is a logistic regression with a penalty on squared weight
size. At its optimum its weights are a combination of the training states
themselves (the representer property of such penalised fits). If the decoy
is any fixed straight-line function of the ownership block (decoy = A times
block), then every fitted weight vector has the form (content part, A v, v),
so it can never put weight on the decoy without the matching weight on the
block. A transplant along such directions moves the block by its full
donor-minus-recipient difference whenever that difference lies in the chosen
directions' span, whatever A is. An exact copy is the case A = s times the
identity. So the test as built **could not** have come out "fooled" unless
the fit stopped well short of its optimum; the scale only moves where the
piece's length sits, not what it does to the block.

A further consequence I will test: arm T's ownership block at the action is
(nearly) one of 20 fixed 24-number marker vectors, one per marker word. If
those 20 vectors are linearly independent, then **any** code of the owner's
marker word (for example a one-of-20 code, the kind the findings note
suggests as a "differently coded" follow-up) is also a straight-line
function of the block, and is predicted to be equally powerless on arm T.

**Probes** (script `experiments/rehearsal-successor-measure/src/check_decoy_power.py`,
committed with this note; output only to `out-decoy-check/`; not part of the
frozen procedure and not a ruled test, reported beside the reproduction):

- **P1, the transplant's effect on the block.** For every scale (4, 1/4, 16,
  1/16) and seed, using the reproduced reads, the chosen piece at the chosen
  site (state 0, action, 8 directions as nominated): on the 800 fresh pairs,
  the share of the block's donor-minus-recipient difference that the
  transplant leaves unmoved, by squared size, pooled over pairs; and the same
  for the piece fitted on the unaltered model at the same site. **Predicted:**
  below 0.01 in every case, and the same to within 0.01 with and without the
  decoy.
- **P2, are the 20 marker vectors independent?** Per seed, the rank of the
  20 by 24 matrix of the model's marker vectors (`own_marker(tok(m_i))`),
  and its smallest singular value relative to its largest. **Predicted:**
  rank 20.
- **P3, a differently coded decoy, one-of-20.** Arm T widened with 20 extra
  numbers holding a one-of-20 code of the owner's marker word (computed as
  the acting-channel tally's softmax weights times the one-of-20 codes of
  each agent's marker word, the same way the block is built, so it is an
  exact code of the same answer), multiplied by a scale `k` and discarded
  before the next layer, exactly as in `DecoyArmT`. `k` = 4 times the
  block's root-mean-square size at the action, per seed, so the code is the
  "stronger" one. Then, using the frozen functions only: the frozen fit
  (`procedure.fit_reads`) on the 600 development episodes; the piece of the
  fitted ownership read at state 0, action, with 1, 2, 4 and 8 directions
  (`transplant.basis_for`); the whole, ownership-only and untouched rates on
  the 800 fresh pairs; and the frozen `measure.reading`. Also where the
  8-direction piece lies (code / block / content) and the P1 quantity.
  **This skips the frozen nomination, controls and null** (it fixes the site
  at the one the nomination chose in every run of the decoy test), so it is
  a probe of power, not a reading in the registered sense. **Predicted:**
  reading 0.20 or less at 8 directions on every seed. If it reads 0.50 or
  more on two or more seeds, I report it as a major finding (a cheap decoy
  that does fool the read) and recommend it be run through the full frozen
  procedure under its own committed method; I will not run that myself.
- Same checks as the decoy test's (a) and (b') for the one-of-20 model
  (outputs bit-identical to the committed model; overwriting the code with
  noise changes nothing). Stop and report if either fails.

Seeds 0, 1 and 2; 4 processor threads.

## 5. Wording

I read the pull request description, the findings note and the resume note
for claims stronger than the evidence, in particular any wording that
presents "not fooled" as evidence about A6 beyond what an exact copy can
show, or as a basis for page 12 (continue or stop), and propose plain
corrections.

## 6. Verdicts this check can return

- **Confirmed:** numbers reproduce, test matches the ruling, history in
  order.
- **Confirmed with corrections:** as above, but wording or power problems
  that change how the result should be used.
- **Not confirmed:** a decision-relevant number fails to reproduce, the
  history shows output before method, or the test is not the ruled one.

Severity of each problem found: blocking (changes the verdict or its use for
page 12), significant (changes what may be claimed), minor (record-keeping).

## 7. Commands for the probes

    python check_decoy_power.py --p1
    python check_decoy_power.py --p2
    python check_decoy_power.py --p3

after the reproduction has finished (P1 uses the reproduced reads).
