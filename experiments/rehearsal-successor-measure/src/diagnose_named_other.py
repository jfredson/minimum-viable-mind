"""What the free arm answers at the named-other position, when it is wrong.

UNREGISTERED, and **not pre-stated**: written after the curriculum runs came
back below one in four on the named-other condition, to find out what they
answer instead. Reported in the findings as an exploratory diagnostic, not as a
check with a pass line. Local, toy scale, $0.

For every held-out episode of the gate set, the prediction at the named-other
position is classed as:

- **named**: the named agent's value's successor (the right answer);
- **own**: the model's OWN value's successor on the same item (the
  own-directed rule applied at the wrong turn);
- **other in item**: one of the item's two remaining agents' values;
- **not in item**: none of the item's four values.

    ../../../.venv/bin/python diagnose_named_other.py --recipes base,curriculum,reweight
"""
from __future__ import annotations

import argparse

import numpy as np
import torch

import grammar as G
import repairs as R
import training as T


@torch.no_grad()
def classify(m, pairs, b) -> dict:
    eps = G.episodes_from_pairs(pairs)
    pred = []
    n = b["tokens"].shape[0]
    for s in range(0, n, 512):
        sl = T.slice_batch(b, slice(s, min(s + 512, n)))
        pred.append(m(sl)[:, G.OTHER].argmax(-1).cpu().numpy())
    pred = np.concatenate(pred)
    counts = dict(named=0, own=0, other_in_item=0, not_in_item=0)
    for e, p in zip(eps, pred):
        j = e["other_item"]
        succ = {a: G.VOCAB[G.SLOTS[G.successor(int(e["values"][a, j]))]]
                for a in range(G.N_AGENTS)}
        if p == succ[e["named"]]:
            counts["named"] += 1
        elif p == succ[e["model"]]:
            counts["own"] += 1
        elif p in succ.values():
            counts["other_in_item"] += 1
        else:
            counts["not_in_item"] += 1
    return {k: v / len(eps) for k, v in counts.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--recipes", default="base,curriculum,reweight")
    ap.add_argument("--arms", default="F")
    a = ap.parse_args()
    device = T.pick_device("auto")
    pairs, b = T.make_data(1500, seed=99, pool="dev", device=device)
    out = {}
    for recipe in a.recipes.split(","):
        for arm in a.arms.split(","):
            for seed in R.SEEDS:
                try:
                    m = R.load_arm(arm, recipe, seed, device)
                except FileNotFoundError:
                    continue
                key = f"{arm}/{recipe}/{seed}"
                out[key] = classify(m, pairs, b)
                print(f"    {key}: " + "  ".join(f"{k} {v:.4f}" for k, v in out[key].items()),
                      flush=True)
    print(f"  wrote {R.save_json('diagnose_named_other.json', out)}")


if __name__ == "__main__":
    main()
