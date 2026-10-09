"""Checker: the pull request's `procedure.row_choice` on the 10-million arm T
development checkpoint (not committed; on John's laptop at
experiments/08-successor-degree/artifacts/succ_t_10m_seed0/succ_t_10m_seed0.pt),
against the development-runs check's figures (2,586 of 3,000 right row;
experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-scripts/arm_t_errors_output.txt).
Run from the root of a checkout of the branch:  python row_choice_10m.py CKPT
"""
import json
import os
import sys

import torch

sys.path.insert(0, os.path.join(os.getcwd(), "experiments/08-successor-degree/src"))
import procedure as P  # noqa: E402

torch.set_num_threads(2)
m, meta = P.load_model(sys.argv[1], "T", "10M")
d = P.EvalData(1.0)
print(json.dumps(P.row_choice(m, d.gate), indent=1))
