"""WITHDRAWN 2026-09-19 — the clause this computes was never registered.

John ruled against Amendment A4 on 2026-09-19 after an independent
red-team pass returned fatal findings F1, F2, F6, F14 and F15
(`red-team-a4.md`). This file is parked, not maintained, and is NOT a
draft awaiting repair. Two of the three calibration substrates it was
written for cannot run at all: the twin checkpoints use a different
tokenizer (70 of 103 shared tokens carry different ids, two A3 tokens
have no id at all, embedding table 103 wide against 105).

The one thing here that may be worth salvaging is `per_cell`, which
scores the registered quantities while keeping the episode index and is
checked to reproduce `train_a3.eval_heldout` to the digit. Red-team
finding F19 applies to it: it is a NEW INSTRUMENT, and its first run
must not also be a verdict.

The Amendment A4 separation clause, and the machinery that computes it.

DRAFT, NOT REGISTERED. This file becomes registered when the A4
registration commit is made, which John is holding until an independent
red-team pass reports (his ruling of 2026-09-19). Nothing here spends
money: it is local inference on checkpoints already fetched [C1/C2].

What this computes, and why it exists
-------------------------------------
The registered A3 clause asked for the primary battery's damage MINUS the
control battery's. That comparison divides by the distance from a
battery's score to its ownership-blind ceiling, and the control's ceiling
was measured at 1.0 on 2026-09-17, so a defined figure for it needs an
accuracy of 1.10. The clause was unsatisfiable from registration.

A4 replaces it with a matched contrast that has no ceiling anywhere in
it. Every episode in the frozen batteries already carries BOTH queries --
the self-directed one scored at the model's own revision position, and
the other-directed one asking the same rule's verdict for a named other
agent. Same turns, same items, same rule, same episode; only the agent
whose commitment is queried differs. So per matched cell e:

    dself(e) = self-directed  intact - self-directed  under lesion
    dother(e) = other-directed intact - other-directed under lesion
    D(e)      = dself(e) - dother(e)

    S(L) = mean_e D(e) / spread(L)
    spread(L) = max( null spread , standard error of the paired mean )

THE FLOOR UNDER THE DENOMINATOR IS LOAD-BEARING. Matched-strength random
damage is chosen precisely because it should not move behaviour, so its
spread can be very small and in a degenerate case approach zero -- and a
denominator that can reach zero is exactly how the A3 clause died.
Taking the larger of the two cannot vanish, and taking the larger is
conservative in the right direction: it makes the clause harder to
satisfy, never easier. Every record states which term governed.

Per-cell scoring, and why it is not `train_a3.eval_heldout`
-----------------------------------------------------------
`eval_heldout` accumulates counts and throws away which episode each
outcome came from, so it cannot pair a self-directed outcome with the
other-directed outcome from the SAME episode. `per_cell` below scores the
identical quantities and keeps the episode index. It is checked against
`eval_heldout` by `--verify-parity`, which requires the per-cell means to
reproduce the aggregate to the digit before any separation number is
reported -- the same discipline `endpoint_a3.py` follows against the
pilot's published endpoint.

    ../../../.venv/bin/python separation_a4.py --self-test
    ../../../.venv/bin/python separation_a4.py --ckpt <ckpt> --verify-parity
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics as st
from pathlib import Path

import torch
import torch.nn.functional as F

import curriculum_a3 as A
import encoding_a3 as E
import null_calibration as NC0
import null_calibration_a3 as NC3
import train_a3 as T
from model import MVM0aModel, Config, to_torch

# Amendment A4 section 3.1: 1,600 episodes, about 800 matched cells. The
# self-directed query exists only where the model revises, which is half
# of episodes, so 800 episodes would give only ~400 matched cells and the
# 2026-09-19 ruling's "at least 800 paired" would be met in episodes but
# not in the cells the statistic is computed over.
EVAL_EPISODES = 1600
SIGNFLIP_DRAWS = 1000
SELF = "T_act"
MATCHED_COMPARATOR = "T_other"      # content-matched, never learned
LEARNED_COMPARATOR = "T_state"      # learned, not content-matched
# Amendment A4 section 10: reported, NEVER binding on this wave.
LADDER_RETAIN = (1.00, 0.75, 0.50, 0.25, 0.00)


# ------------------------------------------------------------- per cell

@torch.no_grad()
def per_cell(model: MVM0aModel, device: str, n: int, seed: int) -> dict:
    """Per-episode correctness, keeping the episode index so the
    self-directed and other-directed outcomes can be paired within an
    episode. Scores exactly what `train_a3.eval_heldout` scores."""
    model.eval()
    eps = A.generate_balanced(n, seed)
    eps, act = T.enact_batched(model, eps, device, random.Random(seed + 1))
    out: dict[str, dict[int, int]] = {b: {} for b in A.BATTERIES}

    # self-directed: no query appended, scored at the own revision
    # position, and only in episodes where the model actually revises
    for i in range(0, len(eps), 50):
        chunk = eps[i:i + 50]
        batch = to_torch(E.collate([E.encode_episode(e) for e in chunk]),
                         device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[i:i + 50]
        logits = model.forward(batch, act_inject=a)
        p = batch["act_pos"]
        keep = (p >= 0).nonzero().flatten()
        if keep.numel() == 0:
            continue
        pk = p[keep]
        al, at = logits[keep, pk - 1], batch["input_ids"][keep, pk]
        ids = torch.tensor(T.SLOT_IDS, device=al.device)
        pick = ids[al[:, ids].argmax(dim=-1)]
        for row, ok in zip(keep.tolist(), (pick == at).tolist()):
            out[SELF][i + row] = int(ok)

    # the appended queries, including the other-directed one
    pairs = [(ei, q) for ei, e in enumerate(eps) for q in e.queries]
    for i in range(0, len(pairs), 50):
        chunk = pairs[i:i + 50]
        batch = to_torch(E.collate([E.encode_episode(eps[ei], query=q)
                                    for ei, q in chunk]), device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[[ei for ei, _ in chunk]]
        cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
        picks = model.score_choices(batch, cids, act_inject=a)
        for p_, (ei, q) in zip(picks, chunk):
            out[q.battery][ei] = int(p_ == E.VOCAB[q.answer])
    model.train()
    return out


def means(cells: dict) -> dict:
    return {b: round(sum(v.values()) / max(1, len(v)), 3)
            for b, v in cells.items()}


# ------------------------------------------------------- the statistics

def paired(intact: dict, lesioned: dict, comparator: str) -> list[float]:
    """D(e) over matched cells: episodes carrying BOTH the self-directed
    query and the comparator's query, in both readings."""
    keys = (set(intact[SELF]) & set(lesioned[SELF])
            & set(intact[comparator]) & set(lesioned[comparator]))
    return [(intact[SELF][k] - lesioned[SELF][k])
            - (intact[comparator][k] - lesioned[comparator][k])
            for k in sorted(keys)]


def deltas(intact: dict, lesioned: dict, battery: str,
           keys: set | None = None) -> list[float]:
    ks = set(intact[battery]) & set(lesioned[battery])
    if keys is not None:
        ks &= keys
    return [intact[battery][k] - lesioned[battery][k] for k in sorted(ks)]


def paired_se(xs: list[float]) -> float:
    """Standard error of the paired mean -- the floor under the
    denominator (A4 section 3)."""
    if len(xs) < 2:
        return float("inf")
    return st.stdev(xs) / math.sqrt(len(xs))


def separation(D: list[float], null_spread: float | None) -> dict:
    """S(L), with the floor that stops the denominator degenerating."""
    se = paired_se(D)
    ns = null_spread if null_spread is not None else 0.0
    governed = "null_spread" if ns >= se else "sampling_floor"
    spread = max(ns, se)
    if not spread or not math.isfinite(spread):
        return {"S": None, "spread": None, "governed_by": None,
                "why": "degenerate spread; no separation score defined"}
    return {"S": round(st.mean(D) / spread, 4),
            "mean_D": round(st.mean(D), 5),
            "spread": round(spread, 6),
            "null_spread": round(ns, 6),
            "sampling_floor": round(se, 6),
            "governed_by": governed,
            "n_cells": len(D)}


def signflip_band(D: list[float], draws: int = SIGNFLIP_DRAWS,
                  seed: int = 20260919) -> dict:
    """The within-run paired test (A4 section 4(b)).

    Randomly flips the SIGN of each cell's paired difference. This tests
    the null the clause needs -- the damage falls equally on both
    conditions, so the paired difference is centred on zero -- and assumes
    NOTHING about the two conditions having equal base rates.

    A label shuffle would be WRONG here and an earlier draft of the
    proposal specified one. The conditions are not exchangeable: intact,
    the self-directed query scores about 0.57 and the other-directed about
    0.30, so shuffling their labels would test whether those two LEVELS
    are exchangeable -- which they plainly are not, and which nobody
    asked. Corrected by red-team pass 1, item RT-A4-03.
    """
    rng = random.Random(seed)
    ms = []
    for _ in range(draws):
        ms.append(st.mean([d if rng.random() < 0.5 else -d for d in D]))
    ms.sort()
    lo = ms[int(0.025 * len(ms))]
    hi = ms[min(len(ms) - 1, int(0.975 * len(ms)))]
    obs = st.mean(D)
    return {"draws": draws, "lo": round(lo, 5), "hi": round(hi, 5),
            "observed_mean_D": round(obs, 5),
            "outside_band": bool(obs < lo or obs > hi)}


def report_block(intact: dict, lesioned: dict, battery: str,
                 keys: set | None = None) -> dict:
    """A4 section 8, John's second addition: a comparator that did not
    fall must be a NUMBER, not a sentence. Every verdict carries the
    intact score, the damaged score, the mean change, the spread across
    matched cells, the standard error of the paired mean, and the count.
    """
    ks = set(intact[battery]) & set(lesioned[battery])
    if keys is not None:
        ks &= keys
    ks = sorted(ks)
    d = [intact[battery][k] - lesioned[battery][k] for k in ks]
    return {
        "battery": battery,
        "intact": round(sum(intact[battery][k] for k in ks) / max(1, len(ks)), 4),
        "lesioned": round(sum(lesioned[battery][k] for k in ks) / max(1, len(ks)), 4),
        "mean_change": round(st.mean(d), 5) if d else None,
        "sd_across_cells": round(st.stdev(d), 5) if len(d) > 1 else None,
        "se_of_paired_mean": round(paired_se(d), 6) if len(d) > 1 else None,
        "n_matched_cells": len(ks),
    }


# ------------------------------------------------------------- self-test

def self_test() -> None:
    # the denominator floor: a null spread of zero must NOT produce an
    # infinite score -- this is the A3 failure mode and the whole reason
    # the floor exists
    D = [1.0, 0.0, 1.0, 0.0] * 25
    r = separation(D, 0.0)
    assert r["S"] is not None and math.isfinite(r["S"]), "zero null spread"
    assert r["governed_by"] == "sampling_floor", r
    r2 = separation(D, 10.0)
    assert r2["governed_by"] == "null_spread", r2
    assert abs(r2["S"]) < abs(r["S"]), "a wider null must LOWER the score"

    # the floor is conservative: it can only shrink the score
    assert separation(D, 0.0)["S"] >= separation(D, 1e9)["S"]

    # sign-flip band: centred data stays inside, shifted data goes outside
    centred = [1.0, -1.0] * 100
    assert not signflip_band(centred)["outside_band"], "centred is inside"
    shifted = [1.0] * 200
    assert signflip_band(shifted)["outside_band"], "all-positive is outside"

    # pairing keeps only episodes present in all four readings
    i = {SELF: {0: 1, 1: 1, 2: 0}, "T_other": {0: 1, 1: 0, 3: 1},
         "T_state": {}, "T_syntax": {}}
    l = {SELF: {0: 0, 1: 1, 2: 0}, "T_other": {0: 1, 1: 0, 3: 0},
         "T_state": {}, "T_syntax": {}}
    assert paired(i, l, "T_other") == [1.0, 0.0], paired(i, l, "T_other")

    rb = report_block(i, l, "T_other")
    assert rb["n_matched_cells"] == 3 and rb["mean_change"] == 0.33333, rb

    # per-cell scoring reproduces the aggregate on a tiny random model
    cfg = Config(vocab=len(E.VOCAB), d_model=64, n_layers=4, n_heads=2,
                 max_len=512, use_register=False)
    torch.manual_seed(0)
    m = MVM0aModel(cfg)
    cells = per_cell(m, "cpu", n=24, seed=7)
    torch.manual_seed(0)
    m2 = MVM0aModel(cfg)
    agg = T.eval_heldout(m2, "cpu", n=24, seed=7)
    for b in A.BATTERIES:
        assert abs(means(cells)[b] - agg[b]) < 1e-9, (b, means(cells)[b], agg[b])
    print("separation_a4 self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--verify-parity", action="store_true")
    ap.add_argument("--ckpt")
    ap.add_argument("--n", type=int, default=EVAL_EPISODES)
    ap.add_argument("--seed", type=int, default=T.HELDOUT_SEED)
    ap.add_argument("--device", default="cpu")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if a.verify_parity:
        ck = torch.load(a.ckpt, map_location=a.device, weights_only=True)
        m = MVM0aModel(Config(**ck["cfg"])).to(a.device).eval()
        m.load_state_dict(ck["state"])
        cells = per_cell(m, a.device, a.n, a.seed)
        m2 = MVM0aModel(Config(**ck["cfg"])).to(a.device).eval()
        m2.load_state_dict(ck["state"])
        agg = T.eval_heldout(m2, a.device, n=a.n, seed=a.seed)
        print(json.dumps({"per_cell_means": means(cells), "eval_heldout": agg,
                          "match": means(cells) == agg}, indent=2))
        return
    ap.error("nothing to do: pass --self-test or --verify-parity")


if __name__ == "__main__":
    main()
