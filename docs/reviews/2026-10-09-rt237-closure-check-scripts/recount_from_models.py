"""Closure check of the fatal finding RT-237: the candidate count behind the
ownership-free line, recounted from the committed toy models.

What this imports from the project, and why: the episode generator
(`experiments/08-successor-degree/src/grammar.py`) to build the 3,000 gate
episodes, and the model definitions (`models.py`) to run the committed
weights. Those are the instrument. It does NOT import `measure.py`,
`procedure.py` or the rehearsal's `lesion_content_check.py`, which hold the
code under check.

The four candidates are built here from the TOKEN SEQUENCE, not from the
generator's stored values and not by the code's `candidate_ids`: on the
own-directed action turn (the one whose third token is the word meaning "your
own"), read the item named; find the four assignment turns that assign that
item; take each one's value word; the candidates are those values' successors
(v_i -> v_(i+1 mod 8)). The model's answer is the arg-max over the whole
vocabulary at that action, with the acting channel zeroed.

Run with the project's environment from the repository root:
    ~/Code/minimum-viable-mind/.venv/bin/python \
        docs/reviews/2026-10-09-rt237-closure-check-scripts/recount_from_models.py
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

import numpy as np
import torch

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "experiments/08-successor-degree/src"))
import grammar as G  # noqa: E402  (the instrument: episodes)
import models as M   # noqa: E402  (the instrument: the network)

MODELS = os.path.join(ROOT, "experiments/rehearsal-successor-measure/out-repairs/models")
RECORD = os.path.join(ROOT, "experiments/rehearsal-successor-measure/out-lesion-content-check/lesion_content_check.json")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recount_from_models.json")

V = G.VOCAB
SELF_ID, ACT_ID, ASSIGN_ID = V[G.SELF], V[G.ACT], V["assign"]
VALUE_IDS = [V[f"v{i}"] for i in range(8)]
VALUE_OF = {t: i for i, t in enumerate(VALUE_IDS)}
ITEM_IDS = {V[f"it{i}"] for i in range(8)}


def candidates_from_tokens(tokens: np.ndarray) -> list[tuple[int, set]]:
    """Per episode: (index of the own-directed action among the two, its four
    candidate answer ids), read from the tokens alone."""
    out = []
    for row in tokens:
        row = list(map(int, row))
        assigns = []           # (item token, value token)
        for p in range(len(row) - 3):
            if row[p + 1] == ASSIGN_ID and row[p + 2] in ITEM_IDS and row[p + 3] in VALUE_OF:
                assigns.append((row[p + 2], row[p + 3]))
        acts = [p for p, t in enumerate(row) if t == ACT_ID]
        assert len(assigns) == 8 and len(acts) == 2, (len(assigns), len(acts))
        own = [k for k, p in enumerate(acts) if row[p + 2] == SELF_ID]
        assert len(own) == 1
        p = acts[own[0]]
        item = row[p + 3]
        vals = [VALUE_OF[v] for it, v in assigns if it == item]
        assert len(vals) == 4, vals
        out.append((own[0], {VALUE_IDS[(v + 1) % 8] for v in vals}))
    return out


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def load(arm, seed):
    path = os.path.join(MODELS, f"ckpt_{arm}_base_seed{seed}.pt")
    obj = torch.load(path, map_location="cpu", weights_only=True)
    if isinstance(obj, dict) and "state" in obj and "cfg" in obj:
        m = M.build_from_config(obj["cfg"])
        m.load_state_dict(obj["state"], strict=True)
    else:
        m = M.build(arm, "toy")
        m.load_state_dict(obj, strict=True)
    return m.eval(), path


@torch.no_grad()
def answers(m, b, lesion: bool):
    b = dict(b)
    if lesion:
        b["acting"] = torch.zeros_like(b["acting"])
    preds = []
    n = b["tokens"].shape[0]
    for s in range(0, n, 500):
        sl = {k: v[s:s + 500] for k, v in b.items()}
        preds.append(m(sl).argmax(-1).numpy())     # (B, 2): the answer at each action, conditions in the fixed order
    return np.concatenate(preds)


def main():
    torch.set_num_threads(max(1, torch.get_num_threads()))
    sums = dict(l.split()[::-1] for l in open(os.path.join(MODELS, "SHA256SUMS")) if l.strip())
    print("gate episodes: the generator's evaluation-set digest matches the committed one:",
          G.eval_sets_digest() == G.EVAL_SETS_DIGEST)
    n_pairs, seed, pool, relaxed = G.EVAL_SETS["gate"]
    pairs = G.make_pairs(n_pairs, seed=seed, pool=pool, collide=relaxed)
    eps = G.episodes_from_pairs(pairs)
    arr = G.batch(eps)
    b = M.to_torch(arr, "cpu")
    print(f"gate episodes: {len(eps)} (from {n_pairs} pairs, generator seed {seed}, pool {pool!r})")
    cands = candidates_from_tokens(arr["tokens"])
    # the condition index of the own-directed answer in the model's output is fixed (grammar.OWN);
    # cross-check that the target the generator scores is one of my four candidates
    tgt_in = sum(int(arr["targets"][i, G.OWN]) in c for i, (_, c) in enumerate(cands))
    print(f"the scored own-directed answer is one of my four candidates on {tgt_in} of {len(eps)} episodes")
    record = json.load(open(RECORD))["models"]
    res, bad = {}, 0
    for arm in ("T", "C", "M", "F"):
        for s in (0, 1, 2):
            m, path = load(arm, s)
            ok_hash = sums.get(os.path.basename(path)) == sha256(path)
            on = answers(m, b, lesion=False)
            off = answers(m, b, lesion=True)
            own_on = int((on[:, G.OWN] == arr["targets"][:, G.OWN]).sum())
            oth_on = int((on[:, G.OTHER] == arr["targets"][:, G.OTHER]).sum())
            own_off = int((off[:, G.OWN] == arr["targets"][:, G.OWN]).sum())
            oth_off = int((off[:, G.OTHER] == arr["targets"][:, G.OTHER]).sum())
            cand_off = sum(int(off[i, G.OWN]) in c for i, (_, c) in enumerate(cands))
            r = record[f"{arm}/{s}"]
            rec = (r["channel_on"]["own"]["correct"], r["channel_on"]["other"]["correct"],
                   r["channel_zeroed"]["own"]["correct"], r["channel_zeroed"]["other"]["correct"],
                   r["channel_zeroed"]["own"]["candidate"])
            mine = (own_on, oth_on, own_off, oth_off, cand_off)
            same = mine == rec
            bad += (not same) or (not ok_hash)
            res[f"{arm}/{s}"] = dict(checkpoint_sha256_matches=ok_hash, own_correct=own_on, other_correct=oth_on,
                                     lesioned_own_correct=own_off, lesioned_other_correct=oth_off,
                                     lesioned_candidate_own_correct=cand_off, passes_1546=cand_off >= 1546)
            print(f"{arm}/{s}: weights match SHA256SUMS {ok_hash}; own/other {own_on}/{oth_on}; zeroed own/other "
                  f"{own_off}/{oth_off}; zeroed own-directed candidate count {cand_off} "
                  f"({'passes' if cand_off >= 1546 else 'FAILS'} 1,546); record {rec}: {'same' if same else 'DIFFERENT'}")
    # the two ends the text cites beside the trained arms: the ordinary competing
    # solver (arm F's architecture trained with the channel always zeroed), and three
    # models of arm F's architecture with untrained weights (drawn after
    # torch.manual_seed(1000 + seed), as the record says it drew them)
    for kind in ("blind", "untrained-F"):
        for s in (0, 1, 2):
            if kind == "blind":
                path = os.path.join(MODELS, f"ckpt_blind_base_seed{s}.pt")
                m = M.build("F", "toy")
                m.load_state_dict(torch.load(path, map_location="cpu", weights_only=True), strict=True)
                ok_hash = sums.get(os.path.basename(path)) == sha256(path)
            else:
                torch.manual_seed(1000 + s)
                m = M.build("F", "toy")
                ok_hash = None
            m.eval()
            off = answers(m, b, lesion=True)
            cand_off = sum(int(off[i, G.OWN]) in c for i, (_, c) in enumerate(cands))
            rec_c = record[f"{kind}/{s}"]["channel_zeroed"]["own"]["candidate"]
            same = cand_off == rec_c
            if kind == "blind":
                bad += (not same) or (not ok_hash)
            res[f"{kind}/{s}"] = dict(checkpoint_sha256_matches=ok_hash,
                                      lesioned_candidate_own_correct=cand_off, passes_1546=cand_off >= 1546,
                                      record=rec_c)
            print(f"{kind}/{s}: zeroed own-directed candidate count {cand_off} "
                  f"({'passes' if cand_off >= 1546 else 'fails'} 1,546); record {rec_c}: "
                  f"{'same' if same else 'DIFFERENT'}"
                  + ("" if kind == "blind" else
                     " (untrained weights: a difference would mean the draw is not reproduced here, "
                     "not that the count is wrong; it is not counted as a failure)"))
    json.dump(res, open(OUT, "w"), indent=1, sort_keys=True)
    print("arm F candidate counts:", [res[f"F/{s}"]["lesioned_candidate_own_correct"] for s in (0, 1, 2)],
          "lowest margin over 1,546:", min(res[f"F/{s}"]["lesioned_candidate_own_correct"] for s in (0, 1, 2)) - 1546)
    print("RESULT:", "every count equals the committed record" if bad == 0 else f"{bad} DIFFERENT")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
