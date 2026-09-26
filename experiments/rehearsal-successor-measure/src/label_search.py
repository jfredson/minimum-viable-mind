"""The free-arm label search of 2026-09-26 (RT-212 route b): the driver.

UNREGISTERED. Runs the method committed at
`docs/2026-09-26-free-arm-label-search-method.md` before any of this was
written. It retrains nothing: it loads the rehearsal repairs' `base`
checkpoints, fits straight-line reads of candidate labels at every site set of
the registered site-set rule (15 contiguous layer sets x 4 position sets), and
scores them on held-out development episodes against a label-permutation null.
It imports the repairs' helpers and changes none of them. Local, toy scale, no
network, no rented machine, $0 [C1/C2].

    ../../../.venv/bin/python label_search.py --stage verify --ckpt-dir <dir>
    ../../../.venv/bin/python label_search.py --stage fit --label own-turn-pair --arms F --ckpt-dir <dir>
    ../../../.venv/bin/python label_search.py --stage verdict --label own-turn-pair

Outputs go to `../out-label-search/`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
import warnings

import numpy as np
import torch
from joblib import Parallel, delayed
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression

import arms as A
import grammar as G
import repairs as R
import training as T
import transplant as X

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "out-label-search"))
COMMITTED = os.path.abspath(os.path.join(HERE, "..", "out-repairs"))

ARMS = ("F", "T", "C", "M")
SEEDS = (0, 1, 2)
RECIPE = "base"

# Method file, section 2: the candidates in the order they run, and the
# reference row (the ruled label) that is not a candidate.
LABELS = {
    "own-turn-pair": "candidate 1: which two assignment turns are the model's own",
    "own-source-turn": "candidate 2: which assignment turn holds the model's own value on the asked item",
    "own-value": "candidate 3: the model's own value on the asked item",
    "marker-word": "reference: which marker word is the model's own (the ruled label)",
}

# Method file, section 3: the registered site-set rule at toy scale.
N_STATES = 5
LAYER_SETS = [tuple(range(a, b + 1)) for a in range(N_STATES) for b in range(a, N_STATES)]
POSITION_SETS = ("action", "action+ans", "action+3", "post-identity")
FIXED_EXTENT = ("action", "action+ans", "action+3")
FIXED_OFFSETS = {"action": (0,), "action+ans": (-1, 0), "action+3": (-3, -2, -1, 0)}
SITE_SETS = [(L, P) for L in LAYER_SETS for P in POSITION_SETS]
assert len(LAYER_SETS) == 15 and len(SITE_SETS) == 60

# Method file, section 4.
DEV_PAIRS, DEV_SEED = 600, 4242
TRAIN_SHARE = 0.7
PERMS_F, PERMS_OTHER = 100, 20

# Method file, section 5.
FLOOR = 0.8


def log(*a):
    print(*a, flush=True)


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(arm: str, seed: int, ckpt_dir: str):
    path = os.path.join(ckpt_dir, f"ckpt_{arm}_{RECIPE}_seed{seed}.pt")
    m = R.build_for(arm)()
    m.load_state_dict(torch.load(path, map_location="cpu"))
    return m.eval(), path


def dev_data():
    pairs, _ = T.make_data(DEV_PAIRS, seed=DEV_SEED, pool="dev", device="cpu")
    recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), "cpu")
    return pairs, recip


# ------------------------------------------------------------------ labels

def labels(pairs: list, recip: dict, name: str) -> np.ndarray:
    """Facts about each recipient episode, from the generator's own records.
    (n,) integers, or (n, 2) turn numbers for the pair label."""
    if name == "marker-word":
        return R.read_labels(recip, "own")
    out = []
    for p in pairs:
        e, c = p["recipient"], p["content"]
        model = e["model"]
        if name == "own-turn-pair":
            turns = sorted(t for t, code in enumerate(c["order"])
                           if code // G.N_ITEMS_PER_EPISODE == model)
            assert len(turns) == 2
            out.append(turns)
        elif name == "own-source-turn":
            out.append(int(e["source_turn"][G.OWN]))
        elif name == "own-value":
            out.append(int(e["values"][model, e["own_item"]]))
        else:
            raise ValueError(name)
    return np.array(out, dtype=np.int64)


# ---------------------------------------------------------------- features

def per_layer_features(model, recip: dict) -> dict:
    """{(layer, position set): (n, width) float32}. Fixed-length sets: the
    state at each position laid end to end, earliest first. post-identity: the
    average over its positions (method file, section 3)."""
    with torch.no_grad():
        _, states = model(recip, capture=True)
    assert len(states) == N_STATES, len(states)
    ap = recip["action_pos"][:, G.OWN]
    n = ap.shape[0]
    rows = torch.arange(n)
    # the fixed-length sets are exactly transplant.position_mask's positions
    for P, offs in FIXED_OFFSETS.items():
        mask = X.position_mask(recip, P)
        idx = torch.zeros_like(mask)
        for o in offs:
            idx[rows, ap + o] = True
        assert torch.equal(mask, idx), P
    post = X.position_mask(recip, "post-identity").float()
    feats = {}
    for li, st in enumerate(states):
        for P, offs in FIXED_OFFSETS.items():
            feats[(li, P)] = torch.cat([st[rows, ap + o] for o in offs], dim=-1).numpy()
        pooled = (st * post[..., None]).sum(1) / post.sum(1, keepdim=True)
        feats[(li, "post-identity")] = pooled.numpy()
    return feats


def site_features(feats: dict, L: tuple, P: str) -> np.ndarray:
    return np.concatenate([feats[(l, P)] for l in L], axis=-1)


# ------------------------------------------------------------------ fitter

def fit_score(Xtr, ytr, Xte, yte) -> float:
    """The ruled fitter (`repairs.fit_reads`), unchanged. For the pair label,
    one softmax over the eight turns, each training episode entered once per
    own turn; the prediction is the two highest-scoring turns, right only if
    that pair is exactly the model's pair (method file, section 2)."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        clf = LogisticRegression(max_iter=3000, C=1.0)
        if ytr.ndim == 1:
            clf.fit(Xtr, ytr)
            return float(clf.score(Xte, yte))
        clf.fit(np.repeat(Xtr, 2, axis=0), ytr.reshape(-1))
        proba = clf.predict_proba(Xte)
        top2 = clf.classes_[np.argsort(-proba, axis=1)[:, :2]]
        return float(np.mean([set(a.tolist()) == set(b.tolist()) for a, b in zip(top2, yte)]))


def _one(Xs, y, n_tr, perm_seed):
    ytr = y[:n_tr]
    if perm_seed is not None:
        ytr = ytr[np.random.default_rng(perm_seed).permutation(n_tr)]
    return fit_score(Xs[:n_tr], ytr, Xs[n_tr:], y[n_tr:])


def null_summary(real: float, null: list) -> dict:
    a = np.array(null)
    return dict(n=len(a), mean=float(a.mean()), p95=float(np.percentile(a, 95)),
                p99=float(np.percentile(a, 99)), max=float(a.max()),
                share_at_or_above_real=float(np.mean(a >= real)),
                values=[float(v) for v in a])


# ------------------------------------------------------------------ stages

def stage_verify(ckpt_dir: str) -> None:
    """Method file, section 4: the ruled label at the action position, layer by
    layer, must reproduce the committed fit accuracies to within 1e-9."""
    pairs, recip = dev_data()
    y = labels(pairs, recip, "marker-word")
    n_tr = int(TRAIN_SHARE * len(y))
    committed = {}
    for f in sorted(os.listdir(COMMITTED)):
        if f.startswith(f"nominate_{RECIPE}_") and f.endswith(".json"):
            with open(os.path.join(COMMITTED, f)) as fh:
                committed.update(json.load(fh)["arms"])
    rec = {"checkpoints": {}, "pairs": {}, "all_match": True}
    for arm in ARMS:
        for seed in SEEDS:
            m, path = load(arm, seed, ckpt_dir)
            rec["checkpoints"][f"{arm}/{seed}"] = dict(path=path, sha256=sha256(path))
            feats = per_layer_features(m, recip)
            got = {str(l): _one(feats[(l, "action")], y, n_tr, None) for l in range(N_STATES)}
            want = committed[f"{arm}/{RECIPE}/{seed}"]["fit_accuracy"]["own"]
            gap = max(abs(got[k] - want[k]) for k in want)
            ok = gap <= 1e-9
            rec["pairs"][f"{arm}/{seed}"] = dict(refit=got, committed=want, largest_gap=gap, match=ok)
            rec["all_match"] &= ok
            log(f"  {arm}/{seed}: " + " ".join(f"{got[k]:.4f}" for k in sorted(got))
                + f"   largest gap to committed {gap:.2e}  {'MATCH' if ok else 'DIFFERS'}")
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "verify.json"), "w") as f:
        json.dump(rec, f, indent=2, sort_keys=True)
    log("  identity check: " + ("all twelve match" if rec["all_match"] else "FAILED — stop"))
    if not rec["all_match"]:
        raise SystemExit(1)


def stage_fit(ckpt_dir: str, label: str, arms: list, n_jobs: int) -> None:
    with open(os.path.join(OUT, "verify.json")) as f:
        if not json.load(f)["all_match"]:
            raise SystemExit("identity check has not passed")
    pairs, recip = dev_data()
    y = labels(pairs, recip, label)
    n_tr = int(TRAIN_SHARE * len(y))
    for arm in arms:
        n_perm = PERMS_F if (arm == "F" and label != "marker-word") else PERMS_OTHER
        for seed in SEEDS:
            path = os.path.join(OUT, f"fit_{label}_{arm}_seed{seed}.json")
            if os.path.exists(path):
                log(f"  {label} {arm}/{seed}: exists, not refitted")
                continue
            t0 = time.time()
            m, ck = load(arm, seed, ckpt_dir)
            feats = per_layer_features(m, recip)
            jobs, keys = [], []
            for L, P in SITE_SETS:
                Xs = site_features(feats, L, P)
                for k in [None] + list(range(n_perm)):
                    # shuffles seeded by site set and shuffle number, so a rerun
                    # draws the same ones
                    ps = None if k is None else 1_000_003 * (SITE_SETS.index((L, P)) + 1) + k
                    jobs.append(delayed(_one)(Xs, y, n_tr, ps))
                    keys.append((L, P, k))
            res = Parallel(n_jobs=n_jobs, batch_size=8)(jobs)
            by_site = {}
            for (L, P, k), v in zip(keys, res):
                d = by_site.setdefault((L, P), dict(real=None, null=[]))
                if k is None:
                    d["real"] = v
                else:
                    d["null"].append(v)
            sites = []
            for (L, P), d in by_site.items():
                ns = null_summary(d["real"], d["null"])
                cc = (d["real"] - ns["mean"]) / (1 - ns["mean"])
                sites.append(dict(layers=list(L), positions=P, fit=d["real"],
                                  chance_corrected=cc, null=ns,
                                  clears=bool(d["real"] >= FLOOR and d["real"] > ns["max"])))
            out = dict(label=label, description=LABELS[label], arm=arm, seed=seed,
                       checkpoint=ck, checkpoint_sha256=sha256(ck), n_train=n_tr,
                       n_heldout=len(y) - n_tr, shuffles=n_perm, floor=FLOOR,
                       seconds=time.time() - t0, sites=sites)
            with open(path, "w") as f:
                json.dump(out, f, indent=1, sort_keys=True)
            best = max(sites, key=lambda s: s["fit"])
            log(f"  {label} {arm}/{seed}: best fit {best['fit']:.4f} at layers "
                f"{best['layers']} {best['positions']}; {sum(s['clears'] for s in sites)} "
                f"of 60 site sets clear; {out['seconds']:.0f}s")


def stage_verdict(label: str) -> dict:
    """Method file, section 5."""
    with open(os.path.join(COMMITTED, "gate_base.json")) as f:
        gate = json.load(f)
    verdict = {"label": label, "description": LABELS[label], "arms": {}}
    for arm in ARMS:
        runs = {}
        for seed in SEEDS:
            p = os.path.join(OUT, f"fit_{label}_{arm}_seed{seed}.json")
            if os.path.exists(p):
                with open(p) as f:
                    runs[seed] = {(tuple(s["layers"]), s["positions"]): s
                                  for s in json.load(f)["sites"]}
        if len(runs) < len(SEEDS):
            continue
        all_seeds = [k for k in runs[0] if all(runs[s][k]["clears"] for s in SEEDS)]
        fixed = [k for k in all_seeds if k[1] in FIXED_EXTENT]
        some_site = sum(any(v["clears"] for v in runs[s].values()) for s in SEEDS)
        some_fixed = sum(any(v["clears"] for k, v in runs[s].items() if k[1] in FIXED_EXTENT)
                         for s in SEEDS)
        verdict["arms"][arm] = dict(
            clears_over_all_60=bool(all_seeds),
            site_sets_clearing_on_all_seeds=[[list(k[0]), k[1]] for k in all_seeds],
            clears_over_fixed_extent_45=bool(fixed),
            fixed_extent_site_sets_clearing_on_all_seeds=[[list(k[0]), k[1]] for k in fixed],
            seeds_with_some_clearing_site=some_site,
            seeds_with_some_clearing_fixed_extent_site=some_fixed,
            best_fit_per_seed={s: max(v["fit"] for v in runs[s].values()) for s in SEEDS},
            best_fixed_extent_fit_per_seed={
                s: max(v["fit"] for k, v in runs[s].items() if k[1] in FIXED_EXTENT)
                for s in SEEDS},
            own_directed_accuracy={s: gate["runs"][f"{arm}/{RECIPE}/{s}"]["own_correct"]
                                   / R.GATE_EPISODES for s in SEEDS})
        v = verdict["arms"][arm]
        log(f"  {arm}: clears over all 60: {v['clears_over_all_60']} "
            f"({len(all_seeds)} site sets); over the 45 fixed-extent: "
            f"{v['clears_over_fixed_extent_45']} ({len(fixed)}); seeds with some "
            f"clearing site {some_site}/3, fixed-extent {some_fixed}/3; best fixed-extent "
            f"fit per seed {[round(x, 4) for x in v['best_fixed_extent_fit_per_seed'].values()]}")
    if "F" in verdict["arms"]:
        verdict["fails_the_floor_on_arm_F"] = not verdict["arms"]["F"]["clears_over_fixed_extent_45"]
    with open(os.path.join(OUT, f"verdict_{label}.json"), "w") as f:
        json.dump(verdict, f, indent=2, sort_keys=True)
    return verdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=("verify", "fit", "verdict"), required=True)
    ap.add_argument("--label", choices=tuple(LABELS))
    ap.add_argument("--arms", default=",".join(ARMS))
    ap.add_argument("--ckpt-dir")
    ap.add_argument("--jobs", type=int, default=8)
    a = ap.parse_args()
    torch.set_num_threads(4)
    if a.stage == "verify":
        stage_verify(a.ckpt_dir)
    elif a.stage == "fit":
        stage_fit(a.ckpt_dir, a.label, a.arms.split(","), a.jobs)
    else:
        stage_verdict(a.label)


if __name__ == "__main__":
    main()
