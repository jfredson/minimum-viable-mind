"""The rehearsal repairs of 2026-09-25: the driver.

UNREGISTERED. Runs the method committed at
`docs/rehearsal-repairs-method-2026-09-25.md` before any of this was built,
under the Weekend 1 queue ruling (`docs/rulings/2026-09-26-weekend-1-queue.md`).
The 2026-09-21 driver, `rehearse.py`, is left exactly as it was, as the record
of what ran then; this file imports its helpers and carries the ruled
procedure. Local, toy scale, no network, no rented machine, $0 [C1/C2].

    ../../../.venv/bin/python repairs.py --stage train --arms F --recipes base,curriculum,reweight
    ../../../.venv/bin/python repairs.py --stage gate
    ../../../.venv/bin/python repairs.py --stage measure --recipe base

Outputs go to `../out-repairs/`, so nothing in the 2026-09-21 record (`../out/`)
is overwritten.
"""
from __future__ import annotations

import argparse
import json
import os
import time

import numpy as np
import torch

import arm_middle as MID
import arms as A
import grammar as G
import training as T

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "out-repairs"))

SEEDS = (0, 1, 2)
ALL_ARMS = ("T", "C", "F", "M")

# The 2026-09-21 recipe (rehearse.py: STEPS, BATCH, LR, TRAIN_PAIRS), unchanged.
STEPS, BATCH, LR, TRAIN_PAIRS = 2500, 256, 3e-3, 15000

# Method file, section 2.2: exactly one recipe per redesign, fixed before the run.
RECIPES = {
    "base": dict(cond_weights=None, other_only_steps=0),
    "curriculum": dict(cond_weights=None, other_only_steps=1000),    # redesign (b)
    "reweight": dict(cond_weights=(0.4, 1.6), other_only_steps=0),   # redesign (a)
}

# Page 1b: above one in four at the 0.05 level on 3,000 held-out episodes,
# i.e. 790 correct or more (method file, section 7, command 1).
GATE_EPISODES = 3000
GATE_MIN_CORRECT = 790


def log(*a):
    print(*a, flush=True)


def ck(arm: str, recipe: str, seed: int) -> str:
    return os.path.join(OUT, f"ckpt_{arm}_{recipe}_seed{seed}.pt")


def save_json(name: str, obj) -> str:
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
    return p


def load_json(name: str):
    with open(os.path.join(OUT, name)) as f:
        return json.load(f)


def build_for(arm: str):
    if arm == "M":
        return MID.build
    if arm == "blind":
        return lambda: A.Arm(A.Config(arm="F"))
    return lambda: A.Arm(A.Config(arm=arm))


def load_arm(arm: str, recipe: str, seed: int, device):
    m = build_for(arm)().to(device)
    m.load_state_dict(torch.load(ck(arm, recipe, seed), map_location=device))
    return m.eval()


# ------------------------------------------------------------------ train

def stage_train(device, arms, recipes, seeds):
    """One checkpoint and one small record per run, so two processes can train
    different runs side by side without writing the same file. A run whose
    checkpoint exists is not re-trained."""
    os.makedirs(OUT, exist_ok=True)
    for recipe in recipes:
        for arm in arms:
            for seed in seeds:
                path = ck(arm, recipe, seed)
                if os.path.exists(path):
                    log(f"  {arm}/{recipe}/{seed}: checkpoint exists, not re-trained")
                    continue
                log(f"  training arm {arm}, recipe {recipe}, seed {seed}")
                m, info = T.train_arm(
                    "F" if arm == "blind" else arm, seed, device, steps=STEPS,
                    batch=BATCH, lr=LR, n_pairs=TRAIN_PAIRS, blind=(arm == "blind"),
                    log_every=1250, log=log, build=build_for(arm),
                    **RECIPES[recipe])
                torch.save(m.state_dict(), path)
                info.update(arm=arm, recipe=recipe, seed=seed,
                            recipe_options=RECIPES[recipe],
                            device=str(device))
                save_json(f"train_{arm}_{recipe}_seed{seed}.json", info)
                log(f"    {info['seconds']:.1f}s")


# ------------------------------------------------------------------- gate

def stage_gate(device, arms, recipes, seeds):
    """The learn-both gate (page 1b) and the acting-channel lesion (page 1h), on
    the 3,000 held-out development episodes the 2026-09-21 gate used."""
    dev_pairs, dev_b = T.make_data(1500, seed=99, pool="dev", device=device)
    assert dev_b["tokens"].shape[0] == GATE_EPISODES
    out = {}
    for recipe in recipes:
        for arm in arms:
            for seed in seeds:
                if not os.path.exists(ck(arm, recipe, seed)):
                    continue
                m = load_arm(arm, recipe, seed, device)
                acc = T.accuracy(m, dev_b, blind=(arm == "blind"))
                les = T.accuracy(m, dev_b, lesion=True)
                row = dict(
                    own=acc["own"], other=acc["other"], n=acc["n"],
                    own_correct=int(round(acc["own"] * acc["n"])),
                    other_correct=int(round(acc["other"] * acc["n"])),
                    lesioned_own=les["own"], lesioned_other=les["other"])
                row["own_clears"] = row["own_correct"] >= GATE_MIN_CORRECT
                row["other_clears"] = row["other_correct"] >= GATE_MIN_CORRECT
                row["lesion_collapses_own"] = \
                    int(round(les["own"] * les["n"])) < GATE_MIN_CORRECT
                if arm == "M":
                    # per-route accuracy, which the fourth arm's prediction needs
                    route = m.entangled_route(dev_b)[:, G.OWN].cpu().numpy()
                    row["own_by_route"] = _own_by_route(m, dev_b, route)
                out[f"{arm}/{recipe}/{seed}"] = row
                log(f"    {arm}/{recipe}/{seed}: own {row['own']:.4f} "
                    f"({row['own_correct']}), named-other {row['other']:.4f} "
                    f"({row['other_correct']})   lesioned own {les['own']:.4f}, "
                    f"named-other {les['other']:.4f}")
    # the verdicts, per arm and recipe: at least two seeds of three
    verdicts = {}
    for key in {k.rsplit("/", 1)[0] for k in out}:
        rows = [out[f"{key}/{s}"] for s in seeds if f"{key}/{s}" in out]
        verdicts[key] = dict(
            seeds=len(rows),
            own_seeds_clearing=sum(r["own_clears"] for r in rows),
            other_seeds_clearing=sum(r["other_clears"] for r in rows),
            other_passes_the_ruled_line=sum(r["other_clears"] for r in rows) >= 2,
            learn_both=(sum(r["own_clears"] for r in rows) >= 2
                        and sum(r["other_clears"] for r in rows) >= 2))
    name_only = T.name_only_solver(dev_pairs)
    res = dict(runs=out, verdicts=verdicts, name_only_solver=name_only,
               bar=dict(episodes=GATE_EPISODES, min_correct=GATE_MIN_CORRECT,
                        as_a_share=GATE_MIN_CORRECT / GATE_EPISODES))
    tag = "_".join(recipes)
    log(f"  wrote {save_json(f'gate_{tag}.json', res)}")
    for k in sorted(verdicts):
        v = verdicts[k]
        log(f"    {k}: named-other clears on {v['other_seeds_clearing']} of {v['seeds']}, "
            f"own-directed on {v['own_seeds_clearing']} of {v['seeds']}")


@torch.no_grad()
def _own_by_route(m, b, route: np.ndarray) -> dict:
    n = b["tokens"].shape[0]
    hits = []
    for s in range(0, n, 512):
        sl = T.slice_batch(b, slice(s, min(s + 512, n)))
        pred = m(sl)[:, G.OWN].argmax(-1)
        hits.append((pred == sl["targets"][:, G.OWN]).cpu().numpy())
    hits = np.concatenate(hits)
    return dict(entangled=float(hits[route].mean()), separable=float(hits[~route].mean()),
                entangled_share=float(route.mean()))


STAGES = ("train", "gate")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True, choices=STAGES)
    ap.add_argument("--arms", default="T,C,F,M")
    ap.add_argument("--recipes", default="base")
    ap.add_argument("--seeds", default="0,1,2")
    ap.add_argument("--device", default="auto")
    a = ap.parse_args()
    device = T.pick_device(a.device)
    arms = a.arms.split(",")
    recipes = a.recipes.split(",")
    seeds = tuple(int(s) for s in a.seeds.split(","))
    for r in recipes:
        assert r in RECIPES, r
    log(f"\n=== stage: {a.stage} ({device}) ===")
    t0 = time.time()
    if a.stage == "train":
        stage_train(device, arms, recipes, seeds)
    elif a.stage == "gate":
        stage_gate(device, arms, recipes, seeds)
    log(f"  ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
