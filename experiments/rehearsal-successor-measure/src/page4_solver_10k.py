"""The page 4 solver pass at the iteration limit ruled 2026-10-08 (10,000):
`page4_solver_1800.py`, unmodified on disk, with its straight-line fitter's
limit raised from 3,000 at run time and nothing else.

UNREGISTERED rehearsal code. NOT A RESULT. Method:
`docs/2026-10-09-ruled-code-changes-and-page4-rerun-method.md`, section 3.
The solver is rehearsal code, not the frozen successor code, so the ruling's
change is applied here by wrapping, not by editing it. Laptop processor, $0.

    cd experiments/rehearsal-successor-measure/src
    ~/Code/minimum-viable-mind/.venv/bin/python page4_solver_10k.py --pool 1980 --out OUTDIR
"""
from __future__ import annotations

import os
import sys

from sklearn.linear_model import LogisticRegression

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import page4_solver_1800 as S   # noqa: E402

LIMIT = 10_000
hits = {"fits": 0, "stopped_at_limit": 0}


class _Limited(LogisticRegression):
    def __init__(self, max_iter=LIMIT, C=1.0):
        super().__init__(max_iter=LIMIT, C=C)

    def fit(self, *a, **kw):
        out = super().fit(*a, **kw)
        hits["fits"] += 1
        hits["stopped_at_limit"] += int(max(self.n_iter_) >= LIMIT)
        return out


S.LogisticRegression = _Limited
S.CS.LogisticRegression = _Limited

if __name__ == "__main__":
    print(f"solver: iteration limit {LIMIT} (was 3,000)", flush=True)
    S.main()
    print(f"solver fits: {hits['fits']}, stopped at the limit of {LIMIT}: {hits['stopped_at_limit']}", flush=True)
