"""Independent check of the page 4 toy re-run (pull request 121): rebuild the
1,980-episode development pool and refit chosen reads WITHOUT the re-run's
drivers (`page4_*.py`) and without the frozen procedure's fitting functions.

UNREGISTERED check code. NOT A RESULT about the scientific question.
Method, committed before this was run: `docs/2026-10-07-page4-rerun-check-method.md`.

It imports only the frozen grammar (episode generator), the frozen model code,
and the frozen `transplant.basis_for` (the definition of a piece: the top
directions of the read). Everything else -- the pool, the labels, the states at
the action position, the fit on recipients 1 to 1,800 and the count on 1,801 to
1,980 -- is written here.

    cd experiments/rehearsal-successor-measure/src
    ~/Code/minimum-viable-mind/.venv/bin/python check_page4_refit.py C2 M0 T0 F0 ...

Each argument is arm letter + seed. Laptop, processor, $0.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

HERE = os.path.dirname(os.path.abspath(__file__))
REH = os.path.abspath(os.path.join(HERE, ".."))
FROZEN = os.path.abspath(os.path.join(REH, "..", "08-successor-degree", "src"))
sys.path.insert(0, FROZEN)
import grammar as G      # noqa: E402
import models as M       # noqa: E402
import transplant as X   # noqa: E402

MODELS = os.path.join(REH, "out-repairs", "models")
COMMITTED = os.path.join(REH, "out-page4-rerun-1800", "models-1800")
N_POOL, N_FIT = 1980, 1800
RANKS = (1, 2, 4, 8)


def key(p):
    return json.dumps(p, sort_keys=True, default=str)


def build_pool():
    assert G.EVAL_SETS["dev"] == (600, 4242, "dev", False), G.EVAL_SETS["dev"]
    pool = G.make_pairs(N_POOL, seed=4242, pool="dev", collide=False)
    frozen = G.make_pairs(600, seed=4242, pool="dev", collide=False)
    same = sum(key(a) == key(b) for a, b in zip(pool[:600], frozen))
    print(f"pool: {len(pool)} pairs; first 600 equal to the frozen 600: {same} of 600", flush=True)
    assert same == 600
    # and the held-out tail is new episodes, not repeats of the fitting set
    fit_keys = {key(p["recipient"]) for p in pool[:N_FIT]}
    rep = sum(key(p["recipient"]) in fit_keys for p in pool[N_FIT:])
    print(f"held-out recipients 1,801-1,980 that repeat a fitting recipient exactly: {rep}", flush=True)
    return M.to_torch(G.batch([p["recipient"] for p in pool]), torch.device("cpu"))


def own_labels(b):
    """The model's own marker word: the marker of the agent assigned at the
    first acting position (written here from the episode fields)."""
    markers = b["agent_marker_tok"].numpy()
    agent_at, acting = b["assign_agent_at"].numpy(), b["acting"].numpy()
    out = np.empty(len(markers), dtype=markers.dtype)
    for i in range(len(markers)):
        first = np.flatnonzero((agent_at[i] >= 0) & (acting[i] == 1))[0]
        out[i] = markers[i, agent_at[i, first]]
    return out


def load(arm, seed):
    path = os.path.join(MODELS, f"ckpt_{arm}_base_seed{seed}.pt")
    want = {l.split()[1]: l.split()[0] for l in open(os.path.join(MODELS, "SHA256SUMS"))}
    got = hashlib.sha256(open(path, "rb").read()).hexdigest()
    assert got == want[os.path.basename(path)], f"fingerprint differs: {path}"
    obj = torch.load(path, map_location="cpu", weights_only=True)
    if isinstance(obj, dict) and "cfg" in obj:
        m = M.build_from_config(obj["cfg"])
        m.load_state_dict(obj["state"], strict=True)
    else:                                   # the toy files are bare weights
        m = M.build(arm, "toy")
        m.load_state_dict(obj, strict=True)
    return m.eval()


def count(h, y):
    clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:N_FIT], y[:N_FIT])
    return int((clf.predict(h[N_FIT:]) == y[N_FIT:]).sum()), clf


def main():
    pool = build_pool()
    y = own_labels(pool)
    ap = pool["action_pos"][:, G.OWN]
    rows = torch.arange(pool["tokens"].shape[0])
    total = mism = 0
    report = {}
    for tag in sys.argv[1:]:
        arm, seed = tag[0], int(tag[1:])
        m = load(arm, seed)
        with torch.no_grad():
            _, states = m(pool, capture=True)
        row = json.load(open(os.path.join(COMMITTED, f"row_{arm}_seed{seed}.json")))
        z = np.load(os.path.join(COMMITTED, f"reads_{arm}_seed{seed}.npz"))
        rep = {}
        for l, st in enumerate(states):
            h = st[rows, ap].numpy()
            whole, clf = count(h, y)
            # the read itself, refitted here, against the committed reads file
            coef_max_diff = float(np.abs(clf.coef_.astype(np.float64) - z[f"own|{l}"]).max())
            pieces = {}
            for r in RANKS:
                q = X.basis_for(z[f"own|{l}"], r).numpy()
                pieces[str(r)] = count(h @ q, y)[0]
            c = row["fits"][str(l)]
            ok_w = whole == c["whole"]
            ok_p = {r: pieces[r] == c["piece"][r] for r in pieces}
            total += 1 + len(pieces)
            mism += (not ok_w) + sum(not v for v in ok_p.values())
            rep[l] = dict(whole=whole, committed_whole=c["whole"], piece=pieces,
                          committed_piece=c["piece"], read_max_abs_diff=coef_max_diff)
            print(f"{arm}/{seed} state {l}: whole {whole} (committed {c['whole']}); pieces {pieces} "
                  f"(committed {c['piece']}); refitted read vs committed read, largest difference "
                  f"{coef_max_diff:.2e}", flush=True)
        sp = row["nomination"]["primary"]["site_set"]
        print(f"{arm}/{seed} committed chosen site set: {sp}", flush=True)
        report[tag] = rep
    print(f"\n{total} counts compared, {mism} differ", flush=True)
    out = os.path.join(REH, "out-page4-check", "refit.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(dict(compared=total, differ=mism, models=report), open(out, "w"), indent=1)


if __name__ == "__main__":
    main()
