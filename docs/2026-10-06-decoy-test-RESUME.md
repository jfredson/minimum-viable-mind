# Decoy test (page 10, finding A6): resume note — SUPERSEDED, everything finished at 10:42; nothing to resume or discard

*Written 2026-10-06 about 10:10 Pacific, because the laptop is being closed
at about 10:50 and the run may be cut off. Branch `decoy-test-a6`. The method
and code were committed and pushed at `f3481a2`, before any output; the
method is `docs/decoy-test-method-2026-10-06.md`.*

## What finished

- **The checks** (`python decoy_test.py --checks-only`), all six (seeds 0, 1
  and 2 at decoy scales 4 and 1/4): every check holds. The widened model's
  outputs are bit-identical to the committed model's; transplanting the
  decoy alone, or overwriting it with large random numbers, changes no output
  bit; the decoy equals the scale times the ownership block exactly; the
  decoy alone and the block alone are each read 180 of 180 at every state;
  at state 0, `action`, the block alone moves everything (reading 0) and the
  decoy alone moves nothing (reading 1). Output:
  `experiments/rehearsal-successor-measure/out-decoy-test/checks_only.json`
  and `checks_only.log`. No stop fired.

## Update, about 10:26

**The two ruled orientations finished** (scale 4 and 1/4, three seeds each,
committed at `0ac3f7e`); findings at `docs/2026-10-06-decoy-test.md`. Only the
supplementary scales (16 and 1/16), which do not enter the verdict, were
started about 10:25 and may be cut off. Restart them with the commands below;
discard their folders `out-decoy-test/scale_16/` and `scale_0.0625/` unless
they hold `summary.json` (then they finished).

## What was running when this note was first written

Started about 10:09, in parallel, from
`experiments/rehearsal-successor-measure/src/`:

    python decoy_test.py --scale 4      # stronger copy -> out-decoy-test/scale_4/
    python decoy_test.py --scale 0.25   # weaker copy   -> out-decoy-test/scale_0.25/

The supplementary scales (16 and 1/16) were **not started**.

## How to tell what is safe to keep

A seed is finished only if `out-decoy-test/scale_<s>/row_T_seed<n>.json`
exists **and contains a `decoy_test` key** (added after the frozen procedure
writes the row). An orientation is finished only if its `summary.json` and
`table.md` exist (written after all three seeds). **Discard** anything else
in a `scale_*` folder: a `reads_T_seed<n>.npz` without a finished row, a row
without `decoy_test`, or a `summary.json` from fewer than three seeds. The
runs are deterministic, so re-running a seed from the start is always safe.

## Exact commands to restart

With the main checkout's environment
(`/Users/john/Code/minimum-viable-mind/.venv/bin/python`), from
`experiments/rehearsal-successor-measure/src/`:

    python decoy_test.py --scale 4    --seeds <the seeds not finished>
    python decoy_test.py --scale 0.25 --seeds <the seeds not finished>
    # if only some seeds were re-run, re-summarise the folder (writes summary.json and table.md):
    python -c "import decoy_test as D; D.P.summarise(D.out_dir(4.0))"     # or 0.25
    python decoy_test.py --scale 16                                       # supplementary
    python decoy_test.py --scale 0.0625                                   # supplementary
    python decoy_test.py --report                                         # table.md and verdicts.json

Then write `docs/2026-10-06-decoy-test.md` (findings), open the pull request
(not merged, owed a check by another session), and delete this file or mark
it superseded.
