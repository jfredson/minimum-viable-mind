"""The rehearsal driver: trains the arms, nominates blind, transplants, runs
the controls, and lands the made-up outcome cases.

UNREGISTERED. Runs the method committed at
`docs/successor-measure-rehearsal-method-2026-09-21.md` before any of this was
built. Local, toy scale, no network, no rented machine, $0 [C1/C2].

    ../../../.venv/bin/python rehearse.py --stage all

Stages, in the order the method fixes:

    train       three arms, three seeds each, plus the ownership-blind
                competing solver; every run saved to a checkpoint file
    gate        the learn-both gate, the acting-channel lesion, and the two
                competing solvers
    nominate    the blind nomination of the ownership subspace, on
                development episodes only, identical on every arm
    transplant  the frozen nomination applied to fresh episodes: the two
                transplants, the reading, and all seven controls
    outcomes    the made-up cases that drive the measure to each outcome
    throughput  seconds per step per arm, at rehearsal scale and at the
                registered shape, on this laptop
"""
from __future__ import annotations

import argparse
import json
import os
import time

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

import arms as A
import grammar as G
import measure as M
import training as T
import transplant as X

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "out"))

SEEDS = (0, 1, 2)
STEPS = 2500
BATCH = 256
LR = 3e-3
TRAIN_PAIRS = 15000

# The candidate site list, written down BEFORE it is searched, with the number
# of comparisons it implies written down with it, so the family correction is
# pre-stated rather than chosen once the results are in (proposal 7.2.1).
CANDIDATE_LAYER_SETS = [(0,), (1,), (2,), (3,), (4,),
                        (3, 4), (2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3, 4)]
CANDIDATE_POSITIONS = ["action", "action+ans", "action+3", "post-identity", "all"]
RANK_CAPS = [1, 2, 3, 4, 8]
FAMILY_SIZE = len(CANDIDATE_LAYER_SETS) * len(CANDIDATE_POSITIONS) * len(RANK_CAPS)

# Floors swept, so the record carries the curve a floor would be chosen
# against. NONE of these is the registered floor; that is John's to fix.
FLOOR_SWEEP = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]


def log(*a):
    print(*a, flush=True)


def ck(arm: str, seed: int, blind: bool = False) -> str:
    return os.path.join(OUT, f"ckpt_{'blind' if blind else arm}_seed{seed}.pt")


def save_json(name: str, obj) -> str:
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
    return p


def load_json(name: str):
    with open(os.path.join(OUT, name)) as f:
        return json.load(f)


def load_arm(arm: str, seed: int, device, blind: bool = False) -> A.Arm:
    """Every intervention runs on a checkpoint written to disk and read back,
    which is the path the registered experiment would use."""
    m = A.Arm(A.Config(arm=arm)).to(device)
    m.load_state_dict(torch.load(ck(arm, seed, blind), map_location=device))
    return m.eval()


# ------------------------------------------------------------------ stages

def stage_train(device):
    os.makedirs(OUT, exist_ok=True)
    meta = {}
    for arm in A.ARMS:
        for seed in SEEDS:
            log(f"  training arm {arm}, seed {seed}")
            m, info = T.train_arm(arm, seed, device, steps=STEPS, batch=BATCH, lr=LR,
                                  n_pairs=TRAIN_PAIRS, log_every=1250, log=log)
            torch.save(m.state_dict(), ck(arm, seed))
            meta[f"{arm}/{seed}"] = info
    log("  training the ownership-blind competing solver")
    m, info = T.train_arm("F", 0, device, steps=STEPS, batch=BATCH, lr=LR,
                          n_pairs=TRAIN_PAIRS, blind=True, log_every=1250, log=log)
    torch.save(m.state_dict(), ck("F", 0, blind=True))
    meta["blind/0"] = info
    p = save_json("train.json", meta)
    log(f"  wrote {p}")


def stage_gate(device):
    dev_pairs, dev_b = T.make_data(1500, seed=99, pool="dev", device=device)
    out = {"learn_both": {}, "lesion": {}, "solvers": {}}
    for arm in A.ARMS:
        for seed in SEEDS:
            m = load_arm(arm, seed, device)
            out["learn_both"][f"{arm}/{seed}"] = T.accuracy(m, dev_b)
            out["lesion"][f"{arm}/{seed}"] = T.accuracy(m, dev_b, lesion=True)
    blind = load_arm("F", 0, device, blind=True)
    out["solvers"]["ownership-blind (trained, acting channel removed)"] = \
        T.accuracy(blind, dev_b, blind=True)
    out["solvers"]["name-only (computed)"] = T.name_only_solver(dev_pairs)
    out["reference_points"] = {
        "guessing over the eight value slots": 1 / 8,
        "a solver that cannot tell whose value it needs": 1 / 4,
    }
    p = save_json("gate.json", out)
    log(f"  wrote {p}")
    for k, v in out["learn_both"].items():
        log(f"    {k:8s} own {v['own']:.4f}  named-other {v['other']:.4f}"
            f"   (lesioned own {out['lesion'][k]['own']:.4f})")
    for k, v in out["solvers"].items():
        log(f"    {k}: own {v['own']:.4f}  named-other {v['other']:.4f}")


def _states_and_targets(model, pairs, device):
    recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), device)
    donor = A.to_torch(G.batch([p["donor"] for p in pairs]), device)
    d_states = X.capture(model, donor)
    donor_target = donor["targets"][:, G.OWN]
    return recip, donor, d_states, donor_target


def _donor_share(logits, donor_target) -> float:
    pred = X.predictions(logits, G.OWN)
    return float((pred == donor_target).float().mean())


def fit_reads(model, recip, device) -> dict:
    """A fitted straight-line read for 'which agent is acting', at every
    candidate layer, on development episodes only. Used ONLY to propose
    candidate directions; nothing is concluded from how well it fits."""
    with torch.no_grad():
        _, states = model(recip, capture=True)
    ap = recip["action_pos"][:, G.OWN]
    y = np.array([int(v) for v in _model_identity(recip)])
    reads = {}
    for li, s in enumerate(states):
        h = s[torch.arange(s.shape[0], device=s.device), ap].detach().cpu().numpy()
        n_tr = int(0.7 * len(y))
        clf = LogisticRegression(max_iter=2000, C=1.0)
        clf.fit(h[:n_tr], y[:n_tr])
        reads[li] = dict(coef=clf.coef_.astype(np.float64),
                         fit_accuracy=float(clf.score(h[n_tr:], y[n_tr:])))
    return reads


def _model_identity(b) -> torch.Tensor:
    """Which agent the model is, recovered from the acting channel and the
    assignment-turn keying — a fact about the episode, used as the read's
    label and never fed to any arm."""
    agent_at = b["assign_agent_at"]
    acting = b["acting"]
    hit = (agent_at >= 0) & (acting == 1)
    idx = torch.argmax(hit.int(), dim=1)
    return agent_at[torch.arange(agent_at.shape[0], device=agent_at.device), idx]


def basis_for(coef: np.ndarray, rank: int, device) -> torch.Tensor:
    u, s, vt = np.linalg.svd(coef - coef.mean(axis=0, keepdims=True),
                             full_matrices=False)
    r = min(rank, vt.shape[0])
    q, _ = np.linalg.qr(vt[:r].T)
    return torch.as_tensor(np.ascontiguousarray(q), dtype=torch.float32, device=device)


def stage_nominate(device):
    """The blind nomination, identical on every arm. Arm T's known ownership
    block is never handed to the procedure (proposal 7.2.5)."""
    out = {"family_size": FAMILY_SIZE, "arms": {}}
    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=device)
    for arm in A.ARMS:
        for seed in SEEDS:
            key = f"{arm}/{seed}"
            m = load_arm(arm, seed, device)
            recip, donor, d_states, d_tgt = _states_and_targets(m, dev_pairs, device)
            reads = fit_reads(m, recip, device)
            grid = []
            for layers in CANDIDATE_LAYER_SETS:
                for posname in CANDIDATE_POSITIONS:
                    sites = X.Sites(layers=layers, positions=posname)
                    mask = X.position_mask(recip, posname)
                    whole = _donor_share(
                        X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
                    for rank in RANK_CAPS:
                        basis = {l: basis_for(reads[l]["coef"], rank, device) for l in layers}
                        own = _donor_share(
                            X.transplanted_logits(m, recip, d_states, sites, mask, basis), d_tgt)
                        grid.append(dict(layers=list(layers), positions=posname, rank=rank,
                                         accuracy_whole=whole, accuracy_ownership_only=own))
            # nominated by causal effect, not by how well the read fits
            best = max(grid, key=lambda g: g["accuracy_ownership_only"])
            out["arms"][key] = dict(
                nomination=best,
                fit_accuracy={str(l): reads[l]["fit_accuracy"] for l in reads},
                grid=grid)
            log(f"    {key:8s} nominated {best['positions']} layers {best['layers']} "
                f"rank {best['rank']}: ownership-only {best['accuracy_ownership_only']:.4f}, "
                f"whole {best['accuracy_whole']:.4f}")
    p = save_json("nominate.json", out)
    log(f"  wrote {p}  (family of {FAMILY_SIZE} comparisons per arm and seed)")


def stage_transplant(device):
    """The frozen nomination, applied once to fresh episodes, with all seven
    controls."""
    nom = load_json("nominate.json")
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=device)
    coll_pairs, _ = T.make_data(800, seed=778, pool="fresh", device=device, collide=True)
    other_pairs, _ = T.make_data(800, seed=779, pool="fresh", device=device)
    out = {"arms": {}, "floors_swept": FLOOR_SWEEP}

    for arm in A.ARMS:
        for seed in SEEDS:
            key = f"{arm}/{seed}"
            m = load_arm(arm, seed, device)
            spec = nom["arms"][key]["nomination"]
            sites = X.Sites(layers=tuple(spec["layers"]), positions=spec["positions"])
            recip, donor, d_states, d_tgt = _states_and_targets(m, fresh_pairs, device)
            mask = X.position_mask(recip, spec["positions"])
            reads = fit_reads(m, recip, device)
            basis = {l: basis_for(reads[l]["coef"], spec["rank"], device)
                     for l in sites.layers}
            D = m.cfg.d_model

            with torch.no_grad():
                untouched = m(recip)
            acc_untouched = _donor_share(untouched, d_tgt)
            acc_whole = _donor_share(
                X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
            acc_own = _donor_share(
                X.transplanted_logits(m, recip, d_states, sites, mask, basis), d_tgt)

            readings = {f"{f:.2f}": M.reading(acc_whole, acc_own, f) for f in FLOOR_SWEEP}

            # ---------------------------------------------------- controls
            controls = {}

            # 1. content transplant: the complement of the nominated subspace
            comp = {}
            for l in sites.layers:
                b = basis[l].detach().cpu().numpy()
                full = np.linalg.svd(b @ b.T - np.eye(D))[0]
                q, _ = np.linalg.qr(np.eye(D) - b @ b.T)
                comp[l] = torch.as_tensor(np.ascontiguousarray(q[:, :D - b.shape[1]]),
                                          dtype=torch.float32, device=device)
            controls["1 content transplant (the complement subspace)"] = _donor_share(
                X.transplanted_logits(m, recip, d_states, sites, mask, comp), d_tgt)

            # 2. another agent's representation: the same procedure aimed at an
            #    agent who is NOT acting, taken from an unmatched episode
            other_recip = A.to_torch(
                G.batch([p["recipient"] for p in other_pairs]), device)
            o_states = X.capture(m, other_recip)
            controls["2 another agent's representation (unmatched donor)"] = _donor_share(
                X.transplanted_logits(m, recip, o_states, sites, mask, basis), d_tgt)

            # 3. a matched random subspace of the same rank
            rng = np.random.default_rng(seed)
            rand = {l: X.orthonormal(rng.normal(size=(spec["rank"], D))).to(device)
                    for l in sites.layers}
            controls["3 matched random subspace, same rank"] = _donor_share(
                X.transplanted_logits(m, recip, d_states, sites, mask, rand), d_tgt)

            # 4. a position where the answer is not yet knowable
            pre_mask = X.position_mask(recip, "pre-identity")
            controls["4 transplant before the identity can be known"] = _donor_share(
                X.transplanted_logits(m, recip, d_states, sites, pre_mask, None), d_tgt)

            # 5. fresh marker and content combinations — by construction
            controls["5 fresh markers and content (share of trials)"] = 1.0

            # 6. who is acting, versus which value
            cr, cd, c_states, c_tgt = _states_and_targets(m, coll_pairs, device)
            c_mask = X.position_mask(cr, spec["positions"])
            same = (cr["targets"][:, G.OWN] == c_tgt)
            c_whole = X.transplanted_logits(m, cr, c_states, sites, c_mask, None)
            c_pred = X.predictions(c_whole, G.OWN)
            with torch.no_grad():
                c_clean = X.predictions(m(cr), G.OWN)
            moved = (c_pred != c_clean)
            controls["6a same-value cell: share whose action moved"] = \
                float(moved[same].float().mean()) if int(same.sum()) else None
            controls["6a same-value cell: trials"] = int(same.sum())
            controls["6b different-value cell: share whose action moved"] = \
                float(moved[~same].float().mean())
            controls["6b different-value cell: trials"] = int((~same).sum())

            # 7. the null transplant
            own_states = X.capture(m, recip)
            null = X.transplanted_logits(m, recip, own_states, sites, mask, None)
            controls["7 null transplant leaves every logit bit-identical"] = \
                bool(torch.equal(untouched, null))

            out["arms"][key] = dict(
                site_set=spec, accuracy_untouched=acc_untouched,
                accuracy_whole=acc_whole, accuracy_ownership_only=acc_own,
                readings=readings, controls=controls,
                n_trials=int(recip["tokens"].shape[0]))
            log(f"    {key:8s} untouched {acc_untouched:.4f}  whole {acc_whole:.4f}  "
                f"ownership-only {acc_own:.4f}")

    # arm T's oracle nomination, reported separately as a reference for what
    # the measure reads under perfect nomination (proposal 7.2.5, decision 1)
    oracle = {}
    for seed in SEEDS:
        m = load_arm("T", seed, device)
        D, dc = m.cfg.d_model, m.cfg.d_content
        eye = torch.eye(D, device=device)[:, dc:]
        spec = nom["arms"][f"T/{seed}"]["nomination"]
        sites = X.Sites(layers=tuple(spec["layers"]), positions=spec["positions"])
        recip, donor, d_states, d_tgt = _states_and_targets(m, fresh_pairs, device)
        mask = X.position_mask(recip, spec["positions"])
        oracle[f"T/{seed}"] = _donor_share(
            X.transplanted_logits(m, recip, d_states, sites, mask,
                                  {l: eye for l in sites.layers}), d_tgt)
    out["arm_T_oracle_nomination"] = oracle
    p = save_json("transplant.json", out)
    log(f"  wrote {p}")


def stage_outcomes(device):
    """The made-up cases, each with its landing written down in the method file
    before it ran."""
    nom = load_json("nominate.json")
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=device)
    res = {}

    def case(name, arm, seed, sites, rank, expect):
        m = load_arm(arm, seed, device)
        recip, donor, d_states, d_tgt = _states_and_targets(m, fresh_pairs, device)
        mask = X.position_mask(recip, sites.positions)
        reads = fit_reads(m, recip, device)
        basis = {l: basis_for(reads[l]["coef"], rank, device) for l in sites.layers}
        w = _donor_share(X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
        o = _donor_share(X.transplanted_logits(m, recip, d_states, sites, mask, basis), d_tgt)
        r = M.reading(w, o, floor=0.30)
        res[name] = dict(arm=arm, seed=seed, sites=sites.label(), rank=rank,
                         accuracy_whole=w, accuracy_ownership_only=o,
                         status=r["status"], degree=r["degree"], expected=expect)
        log(f"    {name}: whole {w:.4f} ownership-only {o:.4f} -> {r['status']}"
            + (f", degree {r['degree']:.4f}" if r["degree"] is not None else "")
            + f"   (expected {expect})")

    for seed in SEEDS:
        s = nom["arms"][f"T/{seed}"]["nomination"]
        case(f"positive, near zero — arm T seed {seed}", "T", seed,
             X.Sites(tuple(s["layers"]), s["positions"]), s["rank"], "near zero, valid")
        s = nom["arms"][f"C/{seed}"]["nomination"]
        case(f"high — arm C seed {seed}", "C", seed,
             X.Sites(tuple(s["layers"]), s["positions"]), s["rank"], "high, valid")
        case(f"no verdict — arm T seed {seed} at the failing site set", "T", seed,
             X.Sites((0,), "pre-identity"), 2, "no verdict")

    # the negative: searched for across arms and site sets, because a negative
    # reading is only a real outcome of this instrument if some configuration
    # of it produces one
    neg = []
    for arm in A.ARMS:
        for seed in SEEDS:
            m = load_arm(arm, seed, device)
            recip, donor, d_states, d_tgt = _states_and_targets(m, fresh_pairs, device)
            reads = fit_reads(m, recip, device)
            for layers in CANDIDATE_LAYER_SETS:
                for posname in CANDIDATE_POSITIONS:
                    sites = X.Sites(layers, posname)
                    mask = X.position_mask(recip, posname)
                    w = _donor_share(
                        X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
                    if w < 0.30:
                        continue
                    for rank in RANK_CAPS:
                        basis = {l: basis_for(reads[l]["coef"], rank, device) for l in layers}
                        o = _donor_share(
                            X.transplanted_logits(m, recip, d_states, sites, mask, basis), d_tgt)
                        if o > w:
                            neg.append(dict(arm=arm, seed=seed, sites=sites.label(),
                                            rank=rank, accuracy_whole=w,
                                            accuracy_ownership_only=o,
                                            degree=(w - o) / w))
    neg.sort(key=lambda d: d["degree"])
    res["negative — searched over every arm and site set"] = dict(
        found=len(neg), most_negative=neg[:5])
    log(f"    negative reading: {len(neg)} configurations found"
        + (f", most negative degree {neg[0]['degree']:.4f} "
           f"({neg[0]['arm']} seed {neg[0]['seed']}, {neg[0]['sites']}, "
           f"rank {neg[0]['rank']})" if neg else ""))
    p = save_json("outcomes.json", res)
    log(f"  wrote {p}")


def stage_throughput(device):
    """Seconds per step, per architecture, at rehearsal scale and at the
    registered shape — on this laptop. What this CANNOT do is predict seconds
    per step on rented hardware; see the staging note."""
    meta = load_json("train.json")
    out = {"rehearsal_scale": {}, "registered_shape_on_this_laptop": {},
           "device": str(device)}
    for k, v in meta.items():
        out["rehearsal_scale"][k] = dict(seconds_per_step=v["seconds_per_step"],
                                         parameters=v["parameters"],
                                         batch=v["batch"], steps=v["steps"])
    # the registered configuration's shape: 448 wide, 12 layers
    reg = dict(d_model=448, n_layers=12, n_heads=8)
    _, tb = T.make_data(64, seed=5, pool="train", device=device)
    for arm in A.ARMS:
        cfg = A.Config(arm=arm, **reg)
        m = A.Arm(cfg).to(device)
        opt = torch.optim.AdamW(m.parameters(), lr=1e-4)
        idx = torch.arange(32, device=device)
        b = T.slice_batch(tb, idx)
        for _ in range(3):                      # warm-up, not timed
            loss = m.loss(b); opt.zero_grad(); loss.backward(); opt.step()
        if device.type == "mps":
            torch.mps.synchronize()
        t0 = time.time()
        n = 20
        for _ in range(n):
            loss = m.loss(b); opt.zero_grad(); loss.backward(); opt.step()
        if device.type == "mps":
            torch.mps.synchronize()
        sec = (time.time() - t0) / n
        out["registered_shape_on_this_laptop"][arm] = dict(
            seconds_per_step=sec, parameters=A.n_params(m), batch=32,
            sequence_length=G.SEQ_LEN, **reg)
        log(f"    arm {arm} at the registered shape: {sec * 1000:.1f} ms/step, "
            f"{A.n_params(m):,} parameters")
    base = out["registered_shape_on_this_laptop"]["F"]["seconds_per_step"]
    out["ratio_to_arm_F"] = {a: out["registered_shape_on_this_laptop"][a]["seconds_per_step"] / base
                             for a in A.ARMS}
    p = save_json("throughput.json", out)
    log(f"  wrote {p}")


STAGES = dict(train=stage_train, gate=stage_gate, nominate=stage_nominate,
              transplant=stage_transplant, outcomes=stage_outcomes,
              throughput=stage_throughput)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all",
                    choices=["all"] + list(STAGES))
    ap.add_argument("--device", default="auto")
    a = ap.parse_args()
    device = T.pick_device(a.device)
    names = list(STAGES) if a.stage == "all" else [a.stage]
    for n in names:
        log(f"\n=== stage: {n} ===")
        t0 = time.time()
        STAGES[n](device)
        log(f"  ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
