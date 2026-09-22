"""Scratch: peek at the checkpoints saved so far."""
import os

import rehearse as R
import training as T

device = T.pick_device("cpu")
_, db = T.make_data(600, seed=99, pool="dev", device=device)
for arm in ("T", "C", "F"):
    for seed in (0, 1, 2):
        if not os.path.exists(R.ck(arm, seed)):
            continue
        m = R.load_arm(arm, seed, device)
        a = T.accuracy(m, db)
        les = T.accuracy(m, db, lesion=True)
        print(f"{arm}/{seed}: own {a['own']:.4f}  named-other {a['other']:.4f}"
              f"   lesioned own {les['own']:.4f} named-other {les['other']:.4f}")
