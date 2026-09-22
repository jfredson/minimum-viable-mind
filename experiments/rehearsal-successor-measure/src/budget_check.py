"""Is the named-other condition's shortfall a limit of the task or a limit of
the training budget?

UNREGISTERED. Rehearsal item R-1 asks whether both matched conditions are
learnable at tiny scale. On the rehearsal's own budget the own-directed
condition clears the one-in-four reference comfortably and the
named-other-directed condition sits on top of it, clearing it on only one seed
in three. That is exactly the shape the successor proposal's own honest prior
predicts for the whole experiment, so it matters whether it is the task or the
budget.

This trains the free arm once more at roughly twice the budget and reports the
same two numbers, so the answer is a measurement rather than an opinion.
Local, free, nothing rented.

    ../../../.venv/bin/python budget_check.py
"""
from __future__ import annotations

import rehearse as R
import training as T

BIGGER = dict(steps=5000, batch=256, lr=3e-3, n_pairs=20000)


def main():
    device = T.pick_device()
    _, dev_b = T.make_data(1500, seed=99, pool="dev", device=device)
    out = {"budget": BIGGER, "rehearsal_budget": dict(steps=R.STEPS, batch=R.BATCH,
                                                      lr=R.LR, n_pairs=R.TRAIN_PAIRS),
           "arms": {}}
    for arm in ("F",):
        m, info = T.train_arm(arm, 0, device, log_every=2500, log=print, **BIGGER)
        acc = T.accuracy(m, dev_b)
        les = T.accuracy(m, dev_b, lesion=True)
        out["arms"][f"{arm}/0"] = dict(accuracy=acc, lesioned=les, **info)
        print(f"arm {arm} at roughly twice the budget: own {acc['own']:.4f}  "
              f"named-other {acc['other']:.4f}  "
              f"(lesioned own {les['own']:.4f} named-other {les['other']:.4f})")
    print(f"wrote {R.save_json('budget_check.json', out)}")


if __name__ == "__main__":
    main()
