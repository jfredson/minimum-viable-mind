"""Control-battery failure-mode diagnostic.

**The decision rule for this module was written and committed BEFORE it
ran**, at `control-diagnostic-rule.md`, commit `c3e9bc1`, on John's
instruction. This module implements that rule and adds nothing to it.

UNREGISTERED and post hoc: these checkpoints have already been read, and
the diagnostic was designed after seeing the control battery fail. Local,
inference only, no spend, no network.

WHY IT ASKS NO NEW QUESTION. The models were trained on three question
forms and a plain name-keyed lookup is not one of them. Asking one would
confound "cannot retrieve" with "has never seen this question", and the
confound is not separable afterwards. So this uses the control question
unchanged and reads the models' existing answer distribution against
different targets.

THE FIVE CELLS, disjoint and exhaustive, tested in this order. With `o`
the queried agent, `x` the queried item, `v` that agent's value on it and
`t = successor(v)` the registered answer:

  CORRECT                  p == t
  UNTRANSFORMED            p == v                 (right agent, no rule)
  WRONG_AGENT_TRANSFORMED  p == successor(v_a)    (rule, wrong name)
  WRONG_AGENT_RAW          p == v_a               (wrong name, no rule)
  OFF_STRUCTURE            none of the above

THE NULL. Keep the model's prediction fixed and recompute every cell as
if a DIFFERENT agent had been named, drawn uniformly from the other three.
That is the rate each cell reaches by coincidence given the item's value
structure, with no real name-keyed retrieval.

PRECONDITION, carried from the two rule defects found this week: a
zero-spread null, or a cell rate matching what a constant predictor gives,
assigns NO bin and reports DEGENERATE.

    ../../../.venv/bin/python control_diagnostic_a3.py --self-test
    ../../../.venv/bin/python control_diagnostic_a3.py --run
"""
from __future__ import annotations

import argparse
import json
import random
import statistics as st
from pathlib import Path

import torch
import torch.nn.functional as F

import curriculum_a3 as A
import encoding_a3 as E
import train_a3 as T
from model import MVM0aModel, Config, to_torch

CELLS = ["CORRECT", "UNTRANSFORMED", "WRONG_AGENT_TRANSFORMED",
         "WRONG_AGENT_RAW", "OFF_STRUCTURE"]
N_PERM = 200
SD_BAR = 3.0
EVAL_SEEDS = [771000, 771037, 771074]
ART = Path('/Users/john/Code/minimum-viable-mind/experiments/'
           '06-mvm-0a-constructed-self-index/artifacts')
CHECKPOINTS = [
    ("pilot (seed 0)", ART / 'a3_30m_seed0/a3_30m_seed0.pt'),
    ("seed 1", ART / 'a3_30m_seed1/a3_30m_seed1.pt'),
    ("seed 2", ART / 'a3_30m_seed2/a3_30m_seed2.pt'),
]


def classify(pred_word, o, item, ep):
    """The five cells, in the committed order. Returns a cell name."""
    v = ep.values[item][o]
    t = A.successor(v)
    if pred_word == t:
        return "CORRECT"
    if pred_word == v:
        return "UNTRANSFORMED"
    others = [a for a in range(ep.n_agents) if a != o]
    if any(pred_word == A.successor(ep.values[item][a]) for a in others):
        return "WRONG_AGENT_TRANSFORMED"
    if any(pred_word == ep.values[item][a] for a in others):
        return "WRONG_AGENT_RAW"
    return "OFF_STRUCTURE"


@torch.no_grad()
def predictions(model, device, n, seed):
    """The model's predicted slot on every control query, with the episode
    facts needed to classify it. Uses the registered scoring path."""
    eps = A.generate_balanced(n, seed)
    eps, act = T.enact_batched(model, eps, device, random.Random(seed + 1))
    out = []
    pairs = [(i, q) for i, e in enumerate(eps)
             for q in e.queries if q.battery == "T_other"]
    for s in range(0, len(pairs), 50):
        chunk = pairs[s:s + 50]
        batch = to_torch(E.collate([E.encode_episode(eps[i], query=q)
                                    for i, q in chunk]), device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[[i for i, _ in chunk]]
        cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
        picks = model.score_choices(batch, cids, act_inject=a)
        for p, (i, q) in zip(picks, chunk):
            ep = eps[i]
            toks = q.text.split()
            marker, item = toks[2], toks[4]
            o = ep.markers.index(marker)
            out.append({"pred": E.IVOCAB[int(p)], "o": o, "item": item,
                        "ep": ep})
    return out


def rates(recs, agent_of=None):
    """Cell rates. `agent_of` supplies a substitute queried agent per
    record, which is how the permutation null is built."""
    counts = {c: 0 for c in CELLS}
    for k, r in enumerate(recs):
        o = r["o"] if agent_of is None else agent_of(k, r)
        counts[classify(r["pred"], o, r["item"], r["ep"])] += 1
    n = max(1, len(recs))
    return {c: counts[c] / n for c in CELLS}


def permutation_null(recs, rng):
    """Keep each prediction, rename the agent the question asked about."""
    draws = []
    for _ in range(N_PERM):
        def other(k, r, _rng=rng):
            alt = [a for a in range(r["ep"].n_agents) if a != r["o"]]
            return _rng.choice(alt)
        draws.append(rates(recs, agent_of=other))
    return {c: {"mean": st.mean(d[c] for d in draws),
                "sd": st.stdev([d[c] for d in draws])} for c in CELLS}


def margins(real, null):
    out = {}
    for c in CELLS:
        sd = null[c]["sd"]
        out[c] = None if sd == 0 else (real[c] - null[c]["mean"]) / sd
    return out


def verdict(real, null, marg):
    """The committed rule. Nothing here was written after the numbers."""
    degenerate = [c for c in CELLS if null[c]["sd"] == 0]
    if degenerate:
        return {"verdict": "DEGENERATE — no bin assigned",
                "why": f"zero-spread null on {degenerate}"}

    def clears(c):
        return marg[c] is not None and marg[c] >= SD_BAR

    untr, wrong = "UNTRANSFORMED", "WRONG_AGENT_TRANSFORMED"
    if clears(untr) and real[untr] > real["CORRECT"]:
        return {"verdict": "OPEN A4 — SUPERVISION ROUTE",
                "means": ("the right agent's value is retrieved and the "
                          "rule is not applied to it; binding works and "
                          "the transform is the missing piece")}
    if clears(wrong) and real[wrong] > real[untr]:
        return {"verdict": "OPEN A4 — SCAFFOLDING ROUTE",
                "means": ("the rule is applied to the wrong agent's value; "
                          "the transform is learned and the binding by "
                          "name is not")}
    dominant = max(CELLS, key=lambda c: real[c])
    if dominant == "OFF_STRUCTURE" and not clears(untr) and not clears(wrong):
        return {"verdict": "CLOSE A3",
                "means": ("the answers bear no relation to the item's "
                          "values; nothing about the question was learned, "
                          "which the registration already fences as "
                          "unlearnable at this scale under this curriculum")}
    return {"verdict": "AMBIGUOUS — decides nothing",
            "means": ("the diagnostic failed to separate the causes and "
                      "must not be reported as pointing anywhere; the "
                      "October decision rests on the evidence already in "
                      "hand")}


def run_one(label, ckpt, device, n):
    cks = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**cks["cfg"])).to(device).eval()
    model.load_state_dict(cks["state"])
    per_seed, all_recs = [], []
    for sd in EVAL_SEEDS:
        recs = predictions(model, device, n, sd)
        all_recs += recs
        per_seed.append({"seed": sd, "n": len(recs), "rates": rates(recs)})
    real = rates(all_recs)
    null = permutation_null(all_recs, random.Random(20260917))
    marg = margins(real, null)
    return {"checkpoint": label, "file": ckpt.name,
            "n_queries": len(all_recs), "eval_seeds": EVAL_SEEDS,
            "cell_rates": {c: round(real[c], 4) for c in CELLS},
            "null": {c: {"mean": round(null[c]["mean"], 4),
                         "sd": round(null[c]["sd"], 4)} for c in CELLS},
            "margins_sd": {c: (None if marg[c] is None else round(marg[c], 2))
                           for c in CELLS},
            "verdict": verdict(real, null, marg),
            "per_seed": per_seed}


def self_test() -> None:
    eps = A.generate_balanced(8, 4242)
    ep = eps[0]
    q = [q for q in ep.queries if q.battery == "T_other"][0]
    toks = q.text.split()
    o, item = ep.markers.index(toks[2]), toks[4]
    v = ep.values[item][o]
    assert classify(A.successor(v), o, item, ep) == "CORRECT"
    assert classify(v, o, item, ep) == "UNTRANSFORMED"
    assert q.answer == A.successor(v), "target matches the curriculum"
    # a synthetic verdict check for each committed branch
    z = {c: 0.0 for c in CELLS}
    nz = {c: {"mean": 0.1, "sd": 0.02} for c in CELLS}
    r = dict(z, UNTRANSFORMED=0.5, CORRECT=0.2)
    assert verdict(r, nz, margins(r, nz))["verdict"].endswith("SUPERVISION ROUTE")
    r = dict(z, WRONG_AGENT_TRANSFORMED=0.5, UNTRANSFORMED=0.1)
    assert verdict(r, nz, margins(r, nz))["verdict"].endswith("SCAFFOLDING ROUTE")
    r = dict(z, OFF_STRUCTURE=0.9, UNTRANSFORMED=0.02)
    assert verdict(r, nz, margins(r, nz))["verdict"] == "CLOSE A3"
    r = dict(z, CORRECT=0.9)
    assert verdict(r, nz, margins(r, nz))["verdict"].startswith("AMBIGUOUS")
    deg = {c: {"mean": 0.1, "sd": 0.0} for c in CELLS}
    assert verdict(r, deg, margins(r, deg))["verdict"].startswith("DEGENERATE")
    print("self-test OK — cells, all four branches and the degeneracy "
          "guard; no checkpoint read")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n", type=int, default=800)
    ap.add_argument("--out", type=Path,
                    default=Path("../a3-gates/control_diagnostic_a3.json"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if a.out.exists():
        raise SystemExit(f"{a.out} exists; refusing to overwrite")
    res = {"diagnostic": "control-battery failure mode",
           "rule_committed_before_running": "control-diagnostic-rule.md, c3e9bc1",
           "registered": False,
           "post_hoc": True,
           "n_permutations": N_PERM, "sd_bar": SD_BAR,
           "checkpoints": [run_one(l, p, a.device, a.n)
                           for l, p in CHECKPOINTS]}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
