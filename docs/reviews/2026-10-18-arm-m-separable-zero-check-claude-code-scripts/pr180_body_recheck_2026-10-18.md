Explains why arm M's separable half (the half-and-half built model's it0 and it4 actions) reads 0.000 route use in the in-use check at 10 million parameters, while the toy models read 1.000 and arm T's slot reads 0.986. This is the explanation the 2026-10-17 ruling (experiment C stays stopped) says the write-up owes. Nothing about C's ending changes. **$0**: forward passes of the saved checkpoints on the laptop's processor; nothing trained, rented or called by API. The frozen code, registered texts, figures, rulings, `STATUS.md` and `data/project.toml` are not edited.

- **Method, committed first:** `docs/2026-10-18-arm-m-separable-zero-method.md` (commit `cb3b9ee`, before any diagnostic ran)
- **Findings:** `docs/2026-10-18-arm-m-separable-zero-findings.md` (commit `8fa464d`; four reporting changes from the check applied in `ca2140c`, with no figure, script or output changed)
- **Check by a session that did not write it:** pull request 185, PASS WITH CONDITIONS, merged into this branch (`docs/reviews/2026-10-18-arm-m-separable-zero-check-claude-code.md`)
- **Scripts and their outputs:** `docs/2026-10-18-arm-m-separable-zero-scripts/` (`dN_*.py` with `dN_*_output.txt`; `checks_output.txt` for the checksums and the empty diff of the frozen folder against `6c47c56`)

## What was found, in plain words

Arm M's separable half at 10 million parameters takes its answer from the "this turn is yours" signal in the shared trunk, not from its built-in ownership answer (D5, planned). The row choice has gone flat: about a quarter on each agent (weight on the top row 0.26), whatever the built-in answer says (D2, planned). So swapping that answer changes nothing. The trunk makes the model's own row of the lookup table about 3.8 times the size of the other rows, and an even mix of the four rows then gives the model's own answer, 1,190 of 1,190 (D7, a diagnostic added after the planned ones had printed).

The row choice is flat because the marker-word embeddings, which both the built-in answer and the row keys are made from, shrank to 3.4 per cent of their start (D8, added after the planned ones had printed). Weight decay alone takes a weight to 33.5 per cent over this run (pull request 112's arithmetic), so training pushed them down. The row-choice weights themselves grew (1.9 and 1.4 times their start).

Take the acting signal out of the trunk only, keeping the built-in answer correct, and arm M's separable answers fall to chance (0.275). Arm T's stay at 0.978 and the toy arm M's at 1.000.

**Hypotheses** (stated in the method before any output): **H1** (the trunk carries the acting signal, so the built-in answer is not consulted) has a three-part result. Its first claim is **supported by D5**, which was planned. The mechanism the method gave for it ("right whichever row the slot selects") is **rejected by D3**, which was planned: forcing a wrong row gives that agent's answer, 3,570 of 3,570. The mechanism that replaces it, a flat row choice over a large own row, comes from **D7, added later**. **H2** (the check is wired differently for arm M) is **rejected**: the swap moves arm M's slot on every action, through the same code path as arm T's. **H3** (a bookkeeping error over which items count as separable) is **rejected**: zero mismatches, and the returned answers are exactly the separable head's. **H4** (weight decay drove the row-choice weights to zero): **D6 matched neither planned pattern.** The weights grew, which is not the "supported" pattern, but the row choice is flat, which is not the "rejected" pattern. Calling H4 rejected as stated, because the weights it named grew, is the writing session's reading, not the planned one. What collapsed is the marker embeddings those weights read from, about ten times further than decay alone could take them (D8, added later).

**Not settled:** why training shrank arm M's marker embeddings at 10 million and not arm T's or the toy's, and whether the trunk took over first or the row choice went flat first. Only final checkpoints exist; settling either would need training. One seed.

## What a session that did not write this must check

1. **The order of commits:** the method (`cb3b9ee`) comes before any output file (`8fa464d`), and the method's predictions are read as written. In particular, F3 says D3's pre-stated reading rejects one form of H1. Check that this is reported honestly, not explained away.
2. **D7, D8 and D9 were added after D0 to D6 printed.** Check that they are labelled as added everywhere, and that the verdict on H1's first claim rests on D5, which was pre-stated. Two parts of the account rest on added diagnostics alone: the even mix being enough (D7) and the marker embeddings shrinking (D8).
3. **Rerun the scripts** from `docs/2026-10-18-arm-m-separable-zero-scripts/` with `~/Code/minimum-viable-mind/.venv/bin/python`. Each takes seconds to a few minutes. Compare the output with the committed `_output.txt` files, and check `git diff 6c47c56 -- experiments/08-successor-degree/src/` is empty.
4. **The in-memory lesion in D5, D7 and D9** (wrapping `_own_vec` on the loaded object) does what the findings say: the trunk sees acting set to zero, and the built-in answer still reads the real acting channel. Also check it is put back after each chunk.
5. **The starting weights in D6 and D8** are rebuilt with `torch.manual_seed(0)` and `models.build`, not read from a saved start (none exists). Check that the argument for why the ratios stand anyway holds.
6. **Every MEASURED figure** in the findings matches its output file, and every ARGUED step follows from the measured figures and the code.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

