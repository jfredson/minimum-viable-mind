"""Item-level battery analysis — twin-binding-anomaly.md thread 3.

Re-runs the registered held-out eval (`train.eval_heldout`'s exact
pipeline: enactment under the eval seed, acting-channel injections,
forced-choice scoring) but records a per-item row instead of an
aggregate, with the structural features the anomaly note asks about:
revision, referent position/distance, and repetition structure. The
summary splits accuracy by feature so "what is the algorithm keying
on" can be read off per checkpoint and compared across binders and
non-binders.

Corrigibility: inference only, local checkpoints, no spend [C1/C2];
output is a fresh per-run JSONL + printed summary, never over an
existing record [C6].

    ../../../.venv/bin/python item_analysis.py \
        --ckpt ../artifacts/pilot_a1_30m_seed1_twin/pilot_a1_30m_seed1_twin.pt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path

import torch
import torch.nn.functional as F

import curriculum as C
import encoding as E
from model import to_torch
from train import enact_batched
from lesion_register import load_checkpoint, HELDOUT_SEED


def item_rows(model, device: str, n: int, seed: int) -> list[dict]:
    """One row per (episode, query), eval pipeline identical to
    train.eval_heldout — same generator call, same enactment rng, same
    chunking — so aggregates reproduce the endpoint numbers."""
    model.eval()
    eps = C.generate_balanced(n, seed, forced_revision_frac=0.25)
    eps, act = enact_batched(model, eps, device, random.Random(seed + 1))
    rows = []
    pairs = [(ei, q) for ei, e in enumerate(eps) for q in e.queries]
    for i in range(0, len(pairs), 50):
        chunk = pairs[i:i + 50]
        batch = to_torch(E.collate([E.encode_episode(eps[ei], query=q)
                                    for ei, q in chunk]), device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[[ei for ei, _ in chunk]]
        cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
        picks = model.score_choices(batch, cids, act_inject=a)
        for p, (ei, q) in zip(picks, chunk):
            e = eps[ei]
            row = {"ep": ei, "battery": q.battery,
                   "ok": int(p == E.VOCAB[q.answer]),
                   "answer": q.answer, "pick": E.VOCAB_INV[p]
                   if hasattr(E, "VOCAB_INV") else
                   next(k for k, v in E.VOCAB.items() if v == p)}
            # locate the queried turn and attach structural features
            ti = _queried_turn(e, q)
            if ti is not None:
                t = e.turns[ti]
                same_item = [j for j, x in enumerate(e.turns)
                             if x.item == t.item]
                row.update({
                    "turn_idx": ti,
                    "dist_from_end": len(e.turns) - 1 - ti,
                    "revised_turn": int(t.revised),
                    "item_repeated": int(len(same_item) > 1),
                    "n_agent_turns": sum(1 for x in e.turns
                                         if x.agent == t.agent),
                    "own": int(t.agent == e.own_slot),
                })
            if q.battery == "T_sr":
                row["rev_episode"] = int(any(x.revised
                                             for x in e.own_turns()))
            rows.append(row)
    return rows


def _queried_turn(e: C.Episode, q: C.Query) -> int | None:
    """Index of the turn a T_sr/T_si query reads (None for the
    structural batteries)."""
    if q.battery == "T_sr":
        own = e.own_turns()
        rev = [t for t in own if t.revised]
        t = rev[-1] if rev else own[0]
        return e.turns.index(t)
    if q.battery == "T_si":
        marker = q.text.split()[2]
        item = q.text.split()[-1].rstrip("?")
        for j, t in enumerate(e.turns):
            if t.marker == marker and t.item == item:
                return j
        return None
    return None


def summarize(rows: list[dict]) -> dict:
    out = {}
    for battery in ("T_sr", "T_si"):
        rs = [r for r in rows if r["battery"] == battery]
        if not rs:
            continue
        s = {"n": len(rs), "acc": round(sum(r["ok"] for r in rs)
                                        / len(rs), 3)}
        for feat in ("revised_turn", "item_repeated", "own",
                     "rev_episode"):
            groups = defaultdict(list)
            for r in rs:
                if feat in r:
                    groups[r[feat]].append(r["ok"])
            if len(groups) > 1:
                s[feat] = {str(k): {"n": len(v),
                                    "acc": round(sum(v) / len(v), 3)}
                           for k, v in sorted(groups.items())}
        # positional profile
        for feat in ("turn_idx", "dist_from_end"):
            groups = defaultdict(list)
            for r in rs:
                if feat in r:
                    groups[r[feat]].append(r["ok"])
            s[feat] = {str(k): {"n": len(v),
                                "acc": round(sum(v) / len(v), 3)}
                       for k, v in sorted(groups.items())}
        out[battery] = s
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", required=True)
    ap.add_argument("--n", type=int, default=400,
                    help="episodes (400 for item-level power; the "
                         "endpoint rows use 100)")
    ap.add_argument("--seed", type=int, default=HELDOUT_SEED)
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None,
                    help="JSONL of per-item rows (refuses overwrite)")
    args = ap.parse_args()
    ckpt = Path(args.ckpt).resolve()
    model, _ = load_checkpoint(ckpt, args.device)
    rows = item_rows(model, args.device, args.n, args.seed)
    summary = {"checkpoint": ckpt.name,
               "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
               "n_episodes": args.n, "seed": args.seed,
               "summary": summarize(rows)}
    print(json.dumps(summary, indent=2))
    if args.out:
        out = Path(args.out)
        assert not out.exists(), f"refusing to overwrite {out} [C6]"
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w") as f:
            f.write(json.dumps({"meta": summary}) + "\n")
            for r in rows:
                f.write(json.dumps(r) + "\n")
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
