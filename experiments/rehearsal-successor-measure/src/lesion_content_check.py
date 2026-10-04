"""Does the free model's channel-removal check have an ownership-free part that
can be evaluated on the successor's task? A measurement for the proposed
disposition of the inside review's fatal finding RT-237 (the battery clause).

UNREGISTERED. NOT A RESULT about the scientific question. Method committed
before this was run on any committed model:
`docs/2026-10-04-gate-a-v4-dispositions-measurements-method.md`, part A.

Version 4 of the successor proposal (section 8.2) says the free model is read
only if, with its acting channel zeroed, "the ownership-free state and syntax
batteries must hold". The successor's task has no such batteries. This script
measures the nearest thing the task does have: with the channel zeroed, is the
model's answer at the action still one of the four values that the
ownership-free part of the act allows (the successor of *some* agent's earlier
value on the item named), even though it can no longer tell whose? A model
that has lost only "which agent am I" picks among those four, and lands on the
right one about one time in four, which is exactly the collapse level the gate
already assumes. A model whose lesion broke the rest of the act does not.

For every committed toy model of the base recipe (arms T, C, M and F, seeds
0 to 2), the ordinary competing solver (no channel at all, seeds 0 to 2), and
three models with freshly drawn, untrained weights (the negative control),
on the 3,000 held-out gate episodes the learn-both gate uses, it prints, per
condition, with the channel on and with it zeroed:

- correct: the answer is the right value;
- legal: the answer is one of the eight value words;
- candidate: the answer is the successor of one of the four agents' values on
  the item named (the pre-stated quantity);

and the pre-stated line for "holds": a candidate count above one half (the
share a model guessing among the eight value words reaches) at the 0.05
level, one-sided, exact binomial, on at least two seeds of three.

Processor only. Nothing is trained, rented or spent: $0. Outputs go to
`../out-lesion-content-check/`. Run from this directory:

    ~/Code/minimum-viable-mind/.venv/bin/python lesion_content_check.py
"""
from __future__ import annotations

import hashlib
import json
import os
import time

import numpy as np
import torch
from scipy.stats import binom

import arms as A
import grammar as G
import repairs as R
import training as T

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.join(HERE, "..", "out-repairs", "models")
OUT = os.path.join(HERE, "..", "out-lesion-content-check")
DEV = torch.device("cpu")
N_PAIRS, DATA_SEED = 1500, 99          # the gate's own episodes (repairs.stage_gate)
SEEDS = (0, 1, 2)
P_CHANCE = 0.5                          # four candidate successors among eight value words


def line(n: int, p: float = P_CHANCE, alpha: float = 0.05) -> int:
    """Smallest count k with P(X >= k) <= alpha for X ~ Binomial(n, p)."""
    k = int(n * p)
    while binom.sf(k - 1, n, p) > alpha:
        k += 1
    return k


def check_sums() -> dict:
    want = {}
    with open(os.path.join(MODELS, "SHA256SUMS")) as f:
        for row in f:
            if row.strip():
                h, name = row.split()
                want[name.lstrip("*")] = h
    got = {}
    for name in want:
        p = os.path.join(MODELS, name)
        if os.path.exists(p):
            with open(p, "rb") as fh:
                got[name] = hashlib.sha256(fh.read()).hexdigest() == want[name]
    return got


def candidates(episodes: list[dict]) -> np.ndarray:
    """Per episode and condition, the vocabulary ids of the four successors of
    the four agents' values on the item that condition's action names."""
    out = np.zeros((len(episodes), 2, G.N_AGENTS), dtype=np.int64)
    for i, e in enumerate(episodes):
        for c, item in ((G.OWN, e["own_item"]), (G.OTHER, e["other_item"])):
            for a in range(G.N_AGENTS):
                out[i, c, a] = G.VOCAB[G.SLOTS[G.successor(int(e["values"][a, item]))]]
    return out


@torch.no_grad()
def predictions(model, b: dict, zero_channel: bool, chunk: int = 500) -> np.ndarray:
    if zero_channel:
        b = dict(b)
        b["acting"] = torch.zeros_like(b["acting"])
    n = b["tokens"].shape[0]
    preds = []
    for s in range(0, n, chunk):
        logits = model(T.slice_batch(b, slice(s, min(s + chunk, n))))
        preds.append(logits.argmax(dim=-1).cpu().numpy())      # (batch, 2)
    return np.concatenate(preds)


def score(pred: np.ndarray, b: dict, cand: np.ndarray) -> dict:
    tgt = b["targets"].cpu().numpy()
    slots = set(int(x) for x in G.SLOT_IDS)
    row = {}
    for c, name in ((G.OWN, "own"), (G.OTHER, "other")):
        p = pred[:, c]
        row[name] = dict(
            correct=int((p == tgt[:, c]).sum()),
            legal=int(sum(int(x) in slots for x in p)),
            candidate=int((p[:, None] == cand[:, c, :]).any(axis=1).sum()))
    return row


def main():
    t0 = time.time()
    os.makedirs(OUT, exist_ok=True)
    torch.manual_seed(0)
    sums = check_sums()
    pairs, b = T.make_data(N_PAIRS, seed=DATA_SEED, pool="dev", device=DEV)
    episodes = G.episodes_from_pairs(pairs)
    n = b["tokens"].shape[0]
    assert n == len(episodes) == 3000
    cand = candidates(episodes)
    # the candidates are four distinct value words, and the right answer is one of them
    assert all(len(set(cand[i, c])) == 4 for i in range(n) for c in (0, 1))
    tgt = b["targets"].cpu().numpy()
    assert all(tgt[i, c] in cand[i, c] for i in range(n) for c in (0, 1))
    k = line(n)
    res = dict(n=n, line=dict(chance=P_CHANCE, alpha=0.05, min_candidate_count=k),
               fingerprints_match=sums, models={}, torch=torch.__version__,
               device=str(DEV))
    print(f"episodes {n}; line for 'holds': candidate count >= {k} "
          f"(above {P_CHANCE} at the 0.05 level, one-sided exact binomial)")
    print(f"model fingerprints checked against SHA256SUMS: "
          f"{sum(sums.values())} of {len(sums)} match")

    cases = [(arm, s) for arm in ("T", "C", "M", "F") for s in SEEDS]
    cases += [("blind", s) for s in SEEDS]
    cases += [("untrained-F", s) for s in SEEDS]
    for arm, seed in cases:
        if arm == "untrained-F":
            torch.manual_seed(1000 + seed)
            m = R.build_for("F")().to(DEV).eval()
        else:
            name = f"ckpt_{arm}_base_seed{seed}.pt"
            assert sums.get(name) is True, f"{name}: fingerprint does not match"
            m = R.build_for(arm)().to(DEV)
            m.load_state_dict(torch.load(os.path.join(MODELS, name), map_location=DEV),
                              strict=True)
            m.eval()
        on = score(predictions(m, b, zero_channel=(arm == "blind")), b, cand)
        off = score(predictions(m, b, zero_channel=True), b, cand)
        holds = {c: off[c]["candidate"] >= k for c in ("own", "other")}
        res["models"][f"{arm}/{seed}"] = dict(channel_on=on, channel_zeroed=off,
                                             holds_own=holds["own"],
                                             holds_other=holds["other"])
        print(f"{arm:>11}/{seed}  channel on : own {on['own']['correct']:4d} correct, "
              f"{on['own']['legal']:4d} legal, {on['own']['candidate']:4d} candidate | "
              f"other {on['other']['correct']:4d}, {on['other']['legal']:4d}, "
              f"{on['other']['candidate']:4d}")
        print(f"{'':>13}  zeroed     : own {off['own']['correct']:4d} correct, "
              f"{off['own']['legal']:4d} legal, {off['own']['candidate']:4d} candidate | "
              f"other {off['other']['correct']:4d}, {off['other']['legal']:4d}, "
              f"{off['other']['candidate']:4d}   -> own-directed part holds: {holds['own']}")
    verdicts = {}
    for arm in ("T", "C", "M", "F", "blind", "untrained-F"):
        h = [res["models"][f"{arm}/{s}"]["holds_own"] for s in SEEDS]
        verdicts[arm] = dict(seeds_holding=int(sum(h)), holds=sum(h) >= 2)
        print(f"verdict {arm:>11}: holds on {sum(h)} of 3 seeds -> "
              f"{'holds' if sum(h) >= 2 else 'does not hold'}")
    res["verdicts"] = verdicts
    res["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(OUT, "lesion_content_check.json"), "w") as f:
        json.dump(res, f, indent=2, sort_keys=True)
    print(f"wrote {os.path.join(OUT, 'lesion_content_check.json')} in {res['seconds']}s")


if __name__ == "__main__":
    main()
