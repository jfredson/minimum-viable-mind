"""Is the competing solver's acting-channel vector untrained? (2026-10-04 check)

Rebuilds each model's starting weights from its training seed, as
training.train_arm does (torch.manual_seed(seed), then the free model's
architecture), and compares the starting acting-channel vector with the one
stored in the committed model file. Processor only; $0.

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python <path to this file>
"""
import os
import sys

import torch

sys.path.insert(0, os.getcwd())
import arms as A  # noqa: E402

for s in (0, 1, 2):
    torch.manual_seed(s)
    start = A.Arm(A.Config(arm="F")).act_vec.detach()
    stored = torch.load(f"../out-repairs/models/ckpt_blind_base_seed{s}.pt", map_location="cpu")["act_vec"]
    cos = float(stored @ start / (stored.norm() * start.norm()))
    print(f"seed {s}: length at start {float(start.norm()):.4f}, stored {float(stored.norm()):.4f}, "
          f"ratio {float(stored.norm() / start.norm()):.4f}, cosine {cos:.6f}")
