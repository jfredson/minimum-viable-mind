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
# The label the straight-line read is fitted to. The proposal says "fit a
# straight-line read for 'which agent is acting'" and does not say what the
# label IS. In a grammar whose marker words are drawn afresh every episode
# that phrase has at least three readings, and the rehearsal found that the
# choice decides whether the nomination can find the answer at all.
#
#   agent-slot   the model's index in the episode's list of agents. This is
#                the pre-stated reading, and it is arbitrary per episode: no
#                state can carry it, because nothing in the episode defines it.
#   marker-rank  the rank of the model's own marker word among the four in the
#                episode, in vocabulary order. This is the programme's own
#                existing convention, from the eleven-position fitted read.
#   marker-word  which marker word is the model's own, out of the whole pool.
READ_LABELS = ("agent-slot", "marker-rank", "marker-word")

RANK_CAPS = [1, 2, 4, 8, 16, 24]
# The pre-stated family, as the method file fixed it before anything ran:
# nine layer sets, five position sets, five rank caps, one reading of the
# read's label. The rank caps and the labels were widened after the pre-stated
# procedure failed on the arm whose answer is in a known place; both the
# widening and its reason are on the record in the findings.
PRE_STATED_FAMILY_SIZE = 9 * 5 * 5
FAMILY_SIZE = (len(CANDIDATE_LAYER_SETS) * len(CANDIDATE_POSITIONS)
               * len(RANK_CAPS) * len(READ_LABELS))

# Floors swept, so the record carries the curve a floor would be chosen
# against. NONE of these is the registered floor; that is John's to fix.
FLOOR_SWEEP = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80]

# A floor used INSIDE the rehearsal, to decide whether a made-up case landed
# where the method said it would. It is fixed here, before anything ran, and
# it is NOT the registered floor: that is an output of this rehearsal and
# John's to fix.
REHEARSAL_FLOOR = 0.30


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


def _donor_hits(logits, donor_target):
    """Per-trial: did the action land on the value the donor's identity
    dictates? Kept per trial, not just averaged, because the across-seed
    uncertainty method has to be demonstrated on matched pairs."""
    pred = X.predictions(logits, G.OWN)
    return (pred == donor_target).detach().cpu().numpy().astype(np.int8)


def _donor_share(logits, donor_target) -> float:
    return float(_donor_hits(logits, donor_target).mean())





def _labels(b, which: str) -> np.ndarray:
    idx = _model_identity(b).detach().cpu().numpy()
    markers = b["agent_marker_tok"].detach().cpu().numpy()
    own = markers[np.arange(len(idx)), idx]
    if which == "agent-slot":
        return idx
    if which == "marker-rank":
        return (np.sort(markers, axis=1) == own[:, None]).argmax(axis=1)
    if which == "marker-word":
        return own
    raise ValueError(which)


def fit_reads(model, recip, device) -> dict:
    """Fitted straight-line reads for 'which agent is acting', at every
    candidate layer and under every reading of that phrase, on development
    episodes only. Used ONLY to propose candidate directions; nothing is
    concluded from how well a read fits."""
    with torch.no_grad():
        _, states = model(recip, capture=True)
    ap = recip["action_pos"][:, G.OWN]
    reads = {}
    for label in READ_LABELS:
        y = _labels(recip, label)
        for li, s in enumerate(states):
            h = s[torch.arange(s.shape[0], device=s.device), ap].detach().cpu().numpy()
            n_tr = int(0.7 * len(y))
            clf = LogisticRegression(max_iter=3000, C=1.0)
            clf.fit(h[:n_tr], y[:n_tr])
            reads[(label, li)] = dict(coef=clf.coef_.astype(np.float64),
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


def reads_path(arm: str, seed: int) -> str:
    return os.path.join(OUT, f"reads_{arm}_seed{seed}.npz")


def save_reads(arm: str, seed: int, reads: dict) -> None:
    """The fitted straight-line reads are FROZEN here, on development episodes,
    and reloaded afterwards. Re-fitting them on fresh episodes would be
    choosing on the data the reading is taken from, which is the one thing the
    data split exists to prevent."""
    np.savez(reads_path(arm, seed),
             **{f"{lab}|{li}": reads[(lab, li)]["coef"] for lab, li in reads})


def load_reads(arm: str, seed: int) -> dict:
    z = np.load(reads_path(arm, seed))
    out = {}
    for k in z.files:
        lab, li = k.split("|")
        out[(lab, int(li))] = dict(coef=z[k])
    return out


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
            save_reads(arm, seed, reads)
            grid = []
            for layers in CANDIDATE_LAYER_SETS:
                for posname in CANDIDATE_POSITIONS:
                    sites = X.Sites(layers=layers, positions=posname)
                    mask = X.position_mask(recip, posname)
                    whole = _donor_share(
                        X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
                    for label in READ_LABELS:
                        for rank in RANK_CAPS:
                            basis = {l: basis_for(reads[(label, l)]["coef"], rank, device)
                                     for l in layers}
                            own = _donor_share(
                                X.transplanted_logits(m, recip, d_states, sites, mask,
                                                      basis), d_tgt)
                            grid.append(dict(
                                layers=list(layers), positions=posname, rank=rank,
                                label=label, accuracy_whole=whole,
                                accuracy_ownership_only=own,
                                in_the_pre_stated_family=(label == "agent-slot"
                                                          and rank in (1, 2, 4, 8))))
            # nominated by causal effect, not by how well the read fits
            best = max(grid, key=lambda g: g["accuracy_ownership_only"])
            pre = [g for g in grid if g["in_the_pre_stated_family"]]
            best_pre = max(pre, key=lambda g: g["accuracy_ownership_only"])
            out["arms"][key] = dict(
                nomination=best,
                nomination_within_the_pre_stated_family=best_pre,
                fit_accuracy={f"{lab}|{li}": reads[(lab, li)]["fit_accuracy"]
                              for lab, li in reads},
                grid=grid)
            log(f"    {key:8s} nominated {best['positions']} layers {best['layers']} "
                f"label {best['label']} rank {best['rank']}: "
                f"ownership-only {best['accuracy_ownership_only']:.4f}, "
                f"whole {best['accuracy_whole']:.4f}   "
                f"(best inside the pre-stated family: "
                f"{best_pre['accuracy_ownership_only']:.4f})")
    p = save_json("nominate.json", out)
    log(f"  wrote {p}  ({FAMILY_SIZE} comparisons per arm and seed; "
        f"{PRE_STATED_FAMILY_SIZE} of them inside the pre-stated family)")


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
            reads = load_reads(arm, seed)          # frozen on development data
            basis = {l: basis_for(reads[(spec["label"], l)]["coef"], spec["rank"],
                                  device)
                     for l in sites.layers}
            D = m.cfg.d_model

            with torch.no_grad():
                untouched = m(recip)
            acc_untouched = _donor_share(untouched, d_tgt)
            acc_whole = _donor_share(
                X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
            acc_own = _donor_share(
                X.transplanted_logits(m, recip, d_states, sites, mask, basis), d_tgt)

            # both candidate forms at every floor swept: the rehearsal
            # reports, it does not choose
            readings = {f"{f:.2f}": M.both_forms(acc_whole, acc_own,
                                                 acc_untouched, f)
                        for f in FLOOR_SWEEP}

            # ---------------------------------------------------- controls
            controls = {}

            # 1. content transplant: the complement of the nominated subspace
            comp = {}
            for l in sites.layers:
                b = basis[l].detach().cpu().numpy()
                u, sv, _ = np.linalg.svd(np.eye(D) - b @ b.T)
                comp[l] = torch.as_tensor(np.ascontiguousarray(u[:, sv > 1e-6]),
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
                per_trial=dict(
                    untouched=_donor_hits(untouched, d_tgt).tolist(),
                    whole=_donor_hits(X.transplanted_logits(
                        m, recip, d_states, sites, mask, None), d_tgt).tolist(),
                    ownership_only=_donor_hits(X.transplanted_logits(
                        m, recip, d_states, sites, mask, basis), d_tgt).tolist()),
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

    def case(name, arm, seed, sites, rank, expect, label="marker-word"):
        m = load_arm(arm, seed, device)
        recip, donor, d_states, d_tgt = _states_and_targets(m, fresh_pairs, device)
        mask = X.position_mask(recip, sites.positions)
        reads = load_reads(arm, seed)              # frozen on development data
        basis = {l: basis_for(reads[(label, l)]["coef"], rank, device)
                 for l in sites.layers}
        w = _donor_share(X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
        o = _donor_share(X.transplanted_logits(m, recip, d_states, sites, mask, basis), d_tgt)
        with torch.no_grad():
            u = _donor_share(m(recip), d_tgt)
        both = M.both_forms(w, o, u, floor=REHEARSAL_FLOOR)
        r = both["registered"]
        res[name] = dict(arm=arm, seed=seed, sites=sites.label(), rank=rank,
                         label=label, accuracy_untouched=u,
                         accuracy_whole=w, accuracy_ownership_only=o,
                         status=r["status"], degree=r["degree"],
                         floor_corrected_status=both["floor_corrected"]["status"],
                         floor_corrected_degree=both["floor_corrected"]["degree"],
                         expected=expect)
        log(f"    {name}: whole {w:.4f} ownership-only {o:.4f} -> {r['status']}"
            + (f", degree {r['degree']:.4f}" if r["degree"] is not None else "")
            + f"   (expected {expect})")

    for seed in SEEDS:
        s = nom["arms"][f"T/{seed}"]["nomination"]
        case(f"positive, near zero — arm T seed {seed}", "T", seed,
             X.Sites(tuple(s["layers"]), s["positions"]), s["rank"],
             "near zero, valid", s["label"])
        s = nom["arms"][f"C/{seed}"]["nomination"]
        case(f"high — arm C seed {seed}", "C", seed,
             X.Sites(tuple(s["layers"]), s["positions"]), s["rank"],
             "high, valid", s["label"])
        case(f"no verdict — arm T seed {seed} at the failing site set", "T", seed,
             X.Sites((0,), "pre-identity"), 2, "no verdict")

    # the negative: searched for across arms and site sets, because a negative
    # reading is only a real outcome of this instrument if some configuration
    # of it produces one
    neg = []
    search_pairs = fresh_pairs[:400]
    for arm in A.ARMS:
        for seed in SEEDS[:1]:          # one seed: the search is over site sets,
            m = load_arm(arm, seed, device)   # not over seeds
            recip, donor, d_states, d_tgt = _states_and_targets(m, search_pairs, device)
            reads = load_reads(arm, seed)          # frozen on development data
            for layers in CANDIDATE_LAYER_SETS:
                for posname in CANDIDATE_POSITIONS:
                    sites = X.Sites(layers, posname)
                    mask = X.position_mask(recip, posname)
                    w = _donor_share(
                        X.transplanted_logits(m, recip, d_states, sites, mask, None), d_tgt)
                    if w < REHEARSAL_FLOOR:
                        continue
                    for label in READ_LABELS:
                        for rank in RANK_CAPS:
                            basis = {l: basis_for(reads[(label, l)]["coef"], rank, device)
                                     for l in layers}
                            o = _donor_share(
                                X.transplanted_logits(m, recip, d_states, sites, mask,
                                                      basis), d_tgt)
                            if o > w:
                                neg.append(dict(arm=arm, seed=seed, sites=sites.label(),
                                                rank=rank, label=label,
                                                accuracy_whole=w,
                                                accuracy_ownership_only=o,
                                                degree=(w - o) / w))
    neg.sort(key=lambda d: d["degree"])
    res["negative — searched over every arm and site set"] = dict(
        found=len(neg), most_negative=neg[:5],
        searched=("every architecture at seed 0, over all nine layer sets, all "
                  "five position sets, all three readings of the read's label "
                  "and all six rank caps, keeping only configurations whose "
                  "whole-state transplant cleared the rehearsal floor"))
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
    # the registered configuration's shape, timed by the same code that
    # would run on a rented machine, so the two figures are comparable
    import bench_arms as B
    for arm in A.ARMS:
        r = B.bench(arm, device, B.REGISTERED_SHAPE, batch=32, steps=20)
        out["registered_shape_on_this_laptop"][arm] = r
        log(f"    arm {arm} at the registered shape: "
            f"{r['seconds_per_step'] * 1000:.1f} ms/step "
            f"(median {r['median_seconds_per_step'] * 1000:.1f}), "
            f"{r['parameters']:,} parameters")
    base = out["registered_shape_on_this_laptop"]["F"]["seconds_per_step"]
    out["ratio_to_arm_F"] = {a: out["registered_shape_on_this_laptop"][a]["seconds_per_step"] / base
                             for a in A.ARMS}
    out["what_this_cannot_answer"] = (
        "Seconds per step on this laptop does not predict seconds per step on "
        "a rented graphics card, and no arithmetic here can make it. What is "
        "measured locally is the RATIO between the three architectures. The "
        "absolute figure the second release of money rests on needs the staged "
        "rented slice, which has not been run.")
    p = save_json("throughput.json", out)
    log(f"  wrote {p}")


def stage_uncertainty(device=None):
    """Rehearsal item R-9: two candidate ways of putting an uncertainty on a
    reading, computed on the same data, with the arithmetic for how many seeds
    each implies. **The method is not chosen here and the seed count is not
    set here**; both are handed to John with the numbers behind them."""
    tr = load_json("transplant.json")
    rng = np.random.default_rng(20260921)
    out = {"arms": {}, "half_widths": [0.05, 0.10, 0.15]}
    for arm in A.ARMS:
        per_seed_raw, per_seed_reg, per_seed_cor, boot = [], [], [], []
        for seed in SEEDS:
            v = tr["arms"][f"{arm}/{seed}"]
            pt = v["per_trial"]
            w = np.array(pt["whole"]); o = np.array(pt["ownership_only"])
            u = np.array(pt["untouched"])
            per_seed_raw.append(float(w.mean() - o.mean()))
            reg = M.reading(float(w.mean()), float(o.mean()), REHEARSAL_FLOOR)
            cor = M.reading_corrected(float(w.mean()), float(o.mean()),
                                      float(u.mean()), REHEARSAL_FLOOR)
            per_seed_reg.append(reg["degree"])
            per_seed_cor.append(cor["degree"])
            # method two: resample matched pairs within the seed
            n = len(w)
            draws = []
            for _ in range(2000):
                idx = rng.integers(0, n, n)
                draws.append(float(w[idx].mean() - o[idx].mean()))
            boot.append(dict(seed=seed, mean=float(np.mean(draws)),
                             standard_error=float(np.std(draws))))
        raw = np.array(per_seed_raw)
        across = dict(mean=float(raw.mean()),
                      standard_deviation=float(raw.std(ddof=1)) if len(raw) > 1 else None,
                      standard_error=float(raw.std(ddof=1) / np.sqrt(len(raw)))
                      if len(raw) > 1 else None, seeds=len(raw))
        within = dict(mean=float(np.mean([b["mean"] for b in boot])),
                      typical_standard_error=float(np.mean([b["standard_error"] for b in boot])),
                      per_seed=boot)
        seeds_needed = {}
        if across["standard_deviation"]:
            for hw in out["half_widths"]:
                # the ordinary arithmetic: how many seeds for a half-width,
                # using the measured across-seed spread and a coverage factor
                # of two. Reported, not adopted.
                seeds_needed[f"{hw:.2f}"] = int(np.ceil((2 * across["standard_deviation"] / hw) ** 2))
        out["arms"][arm] = dict(
            per_seed_raw_difference=per_seed_raw,
            per_seed_registered_form=per_seed_reg,
            per_seed_floor_corrected_form=per_seed_cor,
            across_seed_method=across, within_seed_bootstrap=within,
            seeds_for_a_given_half_width=seeds_needed)
        log(f"    arm {arm}: raw difference per seed "
            f"{[round(x, 4) for x in per_seed_raw]}, across-seed spread "
            f"{across['standard_deviation']}, typical within-seed spread "
            f"{within['typical_standard_error']:.4f}")
        if seeds_needed:
            log(f"      seeds implied by the across-seed method: {seeds_needed}")
    log(f"  wrote {save_json('uncertainty.json', out)}")


STAGES = dict(train=stage_train, gate=stage_gate, nominate=stage_nominate,
              transplant=stage_transplant, outcomes=stage_outcomes,
              uncertainty=stage_uncertainty, throughput=stage_throughput)


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
