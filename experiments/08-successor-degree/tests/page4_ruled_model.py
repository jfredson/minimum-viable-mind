"""The page 4 toy pass under the code ruled 2026-10-08: the frozen procedure,
run directly, on one committed toy model.

Method: `docs/2026-10-09-ruled-code-changes-and-page4-rerun-method.md`,
section 3. NOT A RESULT about the scientific question. Laptop processor, $0.

Unlike the page 4 re-run of 2026-10-06, nothing is changed at run time: the
frozen procedure now fits every read on 1,800 of 1,980 development episodes
itself. The one exception is `--limit 3000`, used ONLY for pass A, the
reproduction check, which sets the iteration limit back to the old 3,000 so
the output can be compared with the checked 1,800-fitted record.

    python tests/page4_ruled_model.py --arm T --seed 0 --out DIR [--limit 3000] [--threads 3]
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))
import procedure as P   # noqa: E402

MODELS = os.path.abspath(os.path.join(HERE, "..", "..", "rehearsal-successor-measure", "out-repairs", "models"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True, choices=("T", "C", "M", "F"))
    ap.add_argument("--seed", required=True, type=int, choices=(0, 1, 2))
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=None, choices=(3000,),
                    help="pass A only: the old iteration limit, for the reproduction check")
    ap.add_argument("--threads", type=int, default=3)
    a = ap.parse_args()
    torch.set_num_threads(a.threads)
    if a.limit is not None:
        P.MS.FIT_MAX_ITER = a.limit
    want = dict(reversed(line.split()) for line in open(os.path.join(MODELS, "SHA256SUMS")))
    path = os.path.join(MODELS, f"ckpt_{a.arm}_base_seed{a.seed}.pt")
    got = hashlib.sha256(open(path, "rb").read()).hexdigest()
    assert got == want[os.path.basename(path)], f"stop: {path} does not match SHA256SUMS"
    if a.arm != "T":
        assert os.path.exists(os.path.join(a.out, f"row_T_seed{a.seed}.json")), \
            "run arm T's same seed first: the rider reads its site set"
    print(f"[{a.arm}/{a.seed}] iteration limit {P.MS.FIT_MAX_ITER}; torch threads {torch.get_num_threads()}",
          flush=True)
    P.run_model(path, a.out, a.arm, "toy", a.seed)


if __name__ == "__main__":
    main()
