# The decoy test (page 10, finding A6): findings

*Written 2026-10-06 (Pacific) by the Claude Code session that ran it, on
branch `decoy-test-a6`. The method, `docs/decoy-test-method-2026-10-06.md`,
and the code, `experiments/rehearsal-successor-measure/src/decoy_test.py`,
were committed and pushed with no output at `f3481a2`, before the run, and
the code was not changed afterwards. Laptop, processor only, 4 threads.
Nothing rented, trained or spent: $0.*

***A constructed stand-in, not a trained model.*** *Everything below was
measured on the committed separable toy model (arm T) with 24 extra numbers
bolted onto its running state by hand. It says what the registered
measurement does with that construction. It says nothing about any trained
model.*

*This session wrote the method, the code and this note. It is owed a check
by a session that did not, which re-runs the script from the committed code
(section 7).*

## 1. The short version

- **Not fooled, both ways round, on every seed.** With an unused copy of the
  owner's marker four times stronger than the model's own ownership block,
  and with one a quarter as strong, the registered nomination picked the same
  site as on the unaltered model (state 0, the action position, 8
  directions) and the reading was **0.0000 on all six runs**.
- **The read did lean on the copy when the copy was stronger.** At scale 4
  the transplanted piece lay about 94 per cent in the copy (0.9370, 0.9341,
  0.9382 by squared size); at scale 1/4 about 6 per cent (0.0588 on every
  seed). So the test reached the case A6 worries about: the read's
  directions were mostly in the unused copy. The reading still came out 0.
- **Why (ARGUED; predicted in the method before the run, section 7).** For
  an exact copy, the fitted directions run along "block and copy together".
  Transplanting along them moves the block by exactly as much as a read of
  the block alone would, however the weight is split. That is what happened.
- **What it does not show.** That the read cannot be fooled by an unused
  representation *coded differently* from the one the action uses. Because
  this copy is an exact multiple of the used block, it could not have fooled
  the read in this way unless the fit stopped well short of its optimum. The
  general form of A6 is untested (section 6).

## 2. The checks that the copy is unused and exact

From `out-decoy-test/checks_only.json` and each orientation's
`checks_T_seed*.json`, on all three seeds at both scales, all hold:

| Check | Result |
|---|---|
| (a) widened model's outputs bit-identical to the committed model's | yes, all six |
| (b) transplanting the donor's copy alone, every state, every position | bit-identical, all six |
| (b') overwriting the copy with large random numbers everywhere | bit-identical, all six |
| (c) copy equals the scale times the block, every state and position | exactly, all six |
| (d) a straight-line read of the owner's marker from the copy alone / the block alone, correct of 180 at states 0 to 4 | 180 at every state, both, all six |
| (e) at state 0, action: share moved by the whole state / block alone / copy alone | 1.0000 / 1.0000 / 0.0000, all six; readings 0 with the block, 1 with the copy |

So the copy is as easily read as the block, and it is causally inert. Check
(e) is the counterexample in miniature: had the procedure transplanted the
copy alone, it would have read 1.

No stop fired (K1 model fingerprints, K2 checks, K3 errors).

## 3. The readings, both ways round, every seed

The script's own table (`out-decoy-test/table.md`):

| decoy scale | seed | reading | site set chosen | piece in copy / block / content | read's weight in copy | whole, ownership-only, untouched (fresh) | true-slot reference |
|---|---|---|---|---|---|---|---|
| 4 (stronger) | 0 | **0.0000** | state 0, action, 8 directions | 0.9370 / 0.0586 / 0.0045 | 0.9370 | 1.0000, 1.0000, 0.0000 | 0.0000 |
| 4 (stronger) | 1 | **0.0000** | state 0, action, 8 directions | 0.9341 / 0.0584 / 0.0075 | 0.9323 | 1.0000, 1.0000, 0.0000 | 0.0000 |
| 4 (stronger) | 2 | **0.0000** | state 0, action, 8 directions | 0.9382 / 0.0586 / 0.0032 | 0.9377 | 1.0000, 1.0000, 0.0000 | 0.0000 |
| 1/4 (weaker) | 0 | **0.0000** | state 0, action, 8 directions | 0.0588 / 0.9408 / 0.0004 | 0.0588 | 1.0000, 1.0000, 0.0000 | 0.0000 |
| 1/4 (weaker) | 1 | **0.0000** | state 0, action, 8 directions | 0.0588 / 0.9405 / 0.0007 | 0.0588 | 1.0000, 1.0000, 0.0000 | 0.0000 |
| 1/4 (weaker) | 2 | **0.0000** | state 0, action, 8 directions | 0.0588 / 0.9408 / 0.0004 | 0.0588 | 1.0000, 1.0000, 0.0000 | 0.0000 |

Every reading was a reading in the registered sense: `summarise` withheld
none (gate passed on 3,000 of 3,000; floors cleared; no-transplant rate
inside its allowance; controls 7, 1 and 4 hold). The method expected the
copy to carry s²/(1+s²) of the read's weight, 0.9412 at scale 4 and 0.0588 at
1/4; measured 0.932 to 0.938, and 0.0588. The fit got close to its optimum.
Figures for controls 3 and 6, the stricter row, the null and the
development grid are in each `row_T_seed*.json`.

**Verdict by the method's section 6:** scale 4, **not fooled**; scale 1/4,
**not fooled**; overall, **not fooled**.

## 4. The supplementary scales (16 and 1/16), reported beside, not in the verdict

**INCOMPLETE at the time of this commit.** Both were started about 10:25 and were still running. If they do not finish before the laptop closes, they are to be run as `docs/2026-10-06-decoy-test-RESUME.md` says. They do not enter the verdict either way.

## 5. Why the reading stays at 0 (ARGUED)

Let the block's numbers be `x` and the copy's `s·x`. The registered fit
penalises the squared size of its weights. Any split of weight between the
two gives the same predictions, so the penalty picks the split with the
copy's weight `s` times the block's. Each fitted direction is then "a
direction `v` in the block, and `s·v` in the copy", scaled to unit length.
The difference between donor and recipient is `d` in the block and `s·d` in
the copy. Projecting it onto that direction and keeping the block part gives
exactly `(v·d)·v`: the same change to the block that a read of the block
alone would make, whatever `s` is. The block is what the action reads, so
the transplant moves the action fully, and the reading is 0. The measured
piece shares (0.937 in the copy at scale 4) and the reading of 0 are that
argument holding on the real fit.

## 6. What this does and does not show for page 12

**It shows** that the registered nomination and reading, frozen code
unchanged, are not fooled by an easily read, causally unused, *exact* copy
of the owner's marker placed at the same states and positions as the used
block, whether the copy is the stronger or the weaker of the two, on three
seeds. That is the test John ordered, and the result is the "near 0" branch:
on the planning session's recommendation already on record (page 12), it
points to **continue**, not stop or redesign.

**It does not show:**

1. **That the read cannot be fooled by a decoy coded differently from the
   used variable.** ChatGPT's counterexample has three parts: an idle,
   easily read marker; a *separate* ownership variable the action uses; and
   content. Here the idle copy and the used block are the same numbers up to
   a scale, so a transplant along the read's directions cannot help moving
   the block. If the idle marker were, for example, a one-of-twelve code of
   the owner while the action used a 24-number blend, or a non-linear
   function of it, the read's directions could lie in the idle code with
   little in the used one, and the reading could rise. That is untested.
   This session argued before the run that the exact-copy test could not
   come out otherwise (method, section 7), so its result, though a real
   check of the frozen code end to end, carries less weight than a test that
   could have failed.
2. **Anything about arm C.** A6's other half, that arm C's "entangled"
   status rests on the instrument's own failure to find a separable piece,
   is untouched; the wording changes drafted for A6 stand either way.
3. **Anything about trained models**, or about the procedure after the page
   4 ruling (fit on 1,800 development episodes); the frozen code fits on 600.

**For John, plainly.** The sharp, cheap form of the worry came back clean:
the read is not fooled by an unused exact copy. A cleverer decoy, coded
differently from what the model actually uses, was not tested and could
still fool it. Whether to test that before registering (also $0, a
constructed stand-in, about an hour on the laptop) or to register with it
named as an open weakness is a new question, and it is John's, not this
session's.

## 7. What the checker must recompute

From `f3481a2` (or this branch), with the pinned versions (torch 2.12.1,
scikit-learn 1.9.0, numpy 2.5.0, scipy 1.18.0), from
`experiments/rehearsal-successor-measure/src/`:

    python decoy_test.py --checks-only
    python decoy_test.py --scale 4
    python decoy_test.py --scale 0.25
    python decoy_test.py --report

and confirm: every check in section 2 holds; the six readings, the site set
chosen and the piece shares in section 3 match to four places; and the
verdict follows from the method's section 6 as written. Also worth checking
independently: that `decoy_test.py` changes nothing in the frozen procedure
other than `load_model` (read it against
`experiments/08-successor-degree/src/procedure.py`), and that the widened
model really throws the copy away before the next layer (`DecoyArmT._split`).
The argument in section 5 deserves a second reading too.

## 8. Files

`experiments/rehearsal-successor-measure/out-decoy-test/`: `checks_only.json`
and `.log`; `scale_<s>/` for each scale run (`checks_T_seed*.json`,
`row_T_seed*.json` with a `decoy_test` section added after the frozen row,
`reads_T_seed*.npz`, `summary.json`, `table.md`); `run_scale_<s>.log`;
`table.md` and `verdicts.json` across scales.
