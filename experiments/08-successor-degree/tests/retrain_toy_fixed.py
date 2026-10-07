"""Retrain the toy arms T, C and M with the sharpness fixed at 4.0 (John's
ruling of 2026-10-06; method `docs/2026-10-06-sharpness-fix-inuse-check-method.md`,
section 4). The committed toy models' exact recipe
(`experiments/rehearsal-successor-measure/src/repairs.py`: 2,500 steps,
batch 256, learning rate 0.003, 15,000 training pairs) through the rehearsal's
`training.train_arm`, with the model built by the changed `models.py`. The only
difference from the committed toy models is the fixed sharpness.

    python tests/retrain_toy_fixed.py --arm C --seed 0 --out DIR

Laptop, $0. Writes DIR/ckpt_{arm}_fixed_seed{seed}.pt (the frozen code's
checkpoint format, so `procedure.py model` loads it) and DIR/train_{arm}_seed{seed}.json.
"""
import argparse
import json
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
REH_SRC = os.path.abspath(os.path.join(HERE, "..", "..", "rehearsal-successor-measure", "src"))
sys.path.insert(0, REH_SRC)
import training as T          # noqa: E402  (the rehearsal's trainer and data)
import grammar as RG          # noqa: E402  (the rehearsal's generator, which training uses)
sys.path.insert(0, os.path.join(HERE, "..", "src"))
import models as M            # noqa: E402  (the changed, frozen model code)

# the committed toy recipe, `repairs.py` line 39 (copied, not imported: importing
# it pulls in the whole rehearsal stack): STEPS, BATCH, LR, TRAIN_PAIRS
STEPS, BATCH, LR, TRAIN_PAIRS = 2500, 256, 3e-3, 15000
_src = open(os.path.join(REH_SRC, "repairs.py")).read()
assert "STEPS, BATCH, LR, TRAIN_PAIRS = 2500, 256, 3e-3, 15000" in _src

ap = argparse.ArgumentParser()
ap.add_argument("--arm", required=True, choices=["T", "C", "M"])
ap.add_argument("--seed", type=int, required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--device", default="mps")
a = ap.parse_args()
assert "08-successor-degree" in M.__file__
os.makedirs(a.out, exist_ok=True)
dev = torch.device(a.device)
model, info = T.train_arm(a.arm, a.seed, dev, steps=STEPS, batch=BATCH, lr=LR,
                          n_pairs=TRAIN_PAIRS, log_every=500, build=lambda: M.build(a.arm, "toy"))
model = model.cpu()
assert float(model.own_sharpness) == M.OWN_SHARPNESS, float(model.own_sharpness)
info.update(arm=a.arm, seed=a.seed, device=a.device, sharpness_at_end=float(model.own_sharpness),
            recipe=dict(steps=STEPS, batch=BATCH, lr=LR, train_pairs=TRAIN_PAIRS))
torch.save({"cfg": M.config_dict(model), "state": model.state_dict(), "step": STEPS},
           os.path.join(a.out, f"ckpt_{a.arm}_fixed_seed{a.seed}.pt"))
json.dump(info, open(os.path.join(a.out, f"train_{a.arm}_seed{a.seed}.json"), "w"), indent=1)
print("saved", a.arm, a.seed, info)
