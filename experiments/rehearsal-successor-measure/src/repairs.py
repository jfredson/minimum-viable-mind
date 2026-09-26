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


# ---------------------------------------------------------- nomination
#
# Method file, section 3. One label, four rank caps, 44 site sets: 176
# comparisons per arm and seed, asserted rather than assumed.

import rehearse as RH                      # noqa: E402  (the 2026-09-21 helpers)
import transplant as X                     # noqa: E402
from sklearn.linear_model import LogisticRegression   # noqa: E402

READ_LABEL = "marker-word"                 # ruled 2026-09-23; page 3, 2026-09-25
RANK_CAPS = (1, 2, 4, 8)                   # page 1d
LAYER_SETS = RH.CANDIDATE_LAYER_SETS       # the rehearsal's nine
POSITION_SETS = RH.CANDIDATE_POSITIONS     # the rehearsal's five
DEGENERATE = ((0, 1, 2, 3, 4), "all")      # every layer at every position: excluded by name
SITE_SETS = [(L, P) for L in LAYER_SETS for P in POSITION_SETS
             if (tuple(L), P) != DEGENERATE]
FAMILY_SIZE = len(SITE_SETS) * len(RANK_CAPS)
assert len(SITE_SETS) == 44 and FAMILY_SIZE == 176, (len(SITE_SETS), FAMILY_SIZE)
FLOOR_SHARE = 0.8                          # page 1c: four fifths
CONTROL2_TOLERANCE = 0.05                  # method file 4.3: rehearsal-only, not registered


def anchored_mask(b: dict, which: str, cond: int) -> torch.Tensor:
    """The rehearsal's position sets, anchored at the action of condition
    `cond`. For the own-directed condition this is exactly
    `transplant.position_mask`; for the named-other condition the action is the
    named-other one and "post-identity" starts at the named agent's first
    assignment turn (method file, section 4.2)."""
    if cond == G.OWN:
        return X.position_mask(b, which)
    B, S = b["tokens"].shape
    dev = b["tokens"].device
    ap = b["action_pos"][:, G.OTHER]
    idx = torch.arange(S, device=dev)[None].expand(B, -1)
    if which == "all":
        return torch.ones(B, S, dtype=torch.bool, device=dev)
    if which == "action":
        return idx == ap[:, None]
    if which == "action+ans":
        return (idx == ap[:, None]) | (idx == (ap - 1)[:, None])
    if which == "action+3":
        return (idx <= ap[:, None]) & (idx >= (ap - 3)[:, None])
    if which == "post-identity":
        named = b["action_who"][:, G.OTHER]
        first = torch.argmax((b["assign_agent_at"] == named[:, None]).int(), dim=1)
        return (idx >= first[:, None]) & (idx <= ap[:, None])
    raise ValueError(which)


def read_labels(b: dict, target: str) -> np.ndarray:
    """Which marker word is the model's own (`target="own"`), or the named
    agent's (`target="named"`, for control 2)."""
    markers = b["agent_marker_tok"].detach().cpu().numpy()
    if target == "own":
        return RH._labels(b, READ_LABEL)
    named = b["action_who"][:, G.OTHER].detach().cpu().numpy()
    return markers[np.arange(len(named)), named]


def fit_reads(model, b, target: str, cond: int) -> dict:
    """Straight-line reads at the action of `cond`, every layer, one label,
    on development episodes only; frozen by the caller before fresh data."""
    with torch.no_grad():
        _, states = model(b, capture=True)
    ap = b["action_pos"][:, cond]
    y = read_labels(b, target)
    out = {}
    for li, st in enumerate(states):
        h = st[torch.arange(st.shape[0], device=st.device), ap].detach().cpu().numpy()
        n_tr = int(0.7 * len(y))
        clf = LogisticRegression(max_iter=3000, C=1.0)
        clf.fit(h[:n_tr], y[:n_tr])
        out[li] = dict(coef=clf.coef_.astype(np.float64),
                       fit_accuracy=float(clf.score(h[n_tr:], y[n_tr:])))
    return out


def hits(out, target, cond) -> np.ndarray:
    return (X.predictions(out, cond) == target).cpu().numpy().astype(np.int8)


def run(model, recip, d_states, sites, mask, basis):
    return X.transplanted_logits(model, recip, d_states, sites, mask, basis)


def floor_check(whole: float, untouched: float, acc: float) -> dict:
    """Page 1c on the chance-corrected scale (page 2), and the plain form
    beside it (method file, section 3.2, step 2)."""
    need = FLOOR_SHARE * (acc - untouched)
    return dict(clears=bool(whole - untouched >= need and need > 0),
                room=whole - untouched, required_room=need,
                clears_plain_form=bool(whole >= FLOOR_SHARE * acc))


def nominate(model, recip, donor, reads, cond: int, device) -> dict:
    """The one rule (method file, section 3.2), for every arm alike. Nothing in
    it names an arm."""
    d_states = X.capture(model, donor)
    d_tgt = donor["targets"][:, cond]
    with torch.no_grad():
        clean = model(recip)
    u = float(hits(clean, d_tgt, cond).mean())
    acc = float(hits(clean, recip["targets"][:, cond], cond).mean())
    grid = []
    for L, P in SITE_SETS:
        sites = X.Sites(layers=tuple(L), positions=P)
        mask = anchored_mask(recip, P, cond)
        whole = float(hits(run(model, recip, d_states, sites, mask, None), d_tgt, cond).mean())
        fl = floor_check(whole, u, acc)
        for r in RANK_CAPS:
            basis = {l: RH.basis_for(reads[l]["coef"], r, device) for l in L}
            own = float(hits(run(model, recip, d_states, sites, mask, basis), d_tgt, cond).mean())
            grid.append(dict(layers=list(L), positions=P, rank=r, accuracy_whole=whole,
                             accuracy_ownership_only=own, floor=fl))
    pos_index = {P: i for i, P in enumerate(POSITION_SETS)}
    clearing = [g for g in grid if g["floor"]["clears"]]
    res = dict(untouched=u, arm_accuracy=acc, grid=grid,
               site_sets_clearing=len({(tuple(g["layers"]), g["positions"]) for g in clearing}))
    if not clearing:
        res.update(status="no verdict", nomination=None, sensitivity=None,
                   reason="no site set's whole-state transplant clears the floor")
        return res
    # step 3: per position set, the smallest clearing layer set
    smallest = {}
    for g in clearing:
        key = (len(g["layers"]), g["layers"])
        if g["positions"] not in smallest or key < smallest[g["positions"]]:
            smallest[g["positions"]] = key
    cands = [g for g in clearing
             if (len(g["layers"]), g["layers"]) == smallest[g["positions"]]]
    # step 4: highest ownership-only share; ties to lower rank, earlier position set
    best = min(cands, key=lambda g: (-g["accuracy_ownership_only"], g["rank"],
                                     pos_index[g["positions"]]))
    sens = min(clearing, key=lambda g: (-g["accuracy_ownership_only"], len(g["layers"]),
                                        g["rank"], pos_index[g["positions"]], g["layers"]))
    res.update(status="nominated", nomination=best, sensitivity=sens,
               smallest_clearing_layer_set_per_position_set={
                   P: list(v[1]) for P, v in smallest.items()})
    return res


def named_swap(pairs: list, seed: int) -> list:
    """Control 2's donor (method file, section 4.2): the same content and the
    same acting agent, with the named agent replaced by one that is neither
    the actor nor the original named agent. One token of text differs."""
    rng = np.random.default_rng(seed)
    out = []
    for p in pairs:
        c, r = p["content"], p["recipient"]["model"]
        choices = [a for a in range(G.N_AGENTS) if a not in (r, c["named"])]
        c2 = dict(c, named=int(rng.choice(choices)))
        out.append(G.render(c2, r))
    return out


def moved_share(model, recip, d_states, sites, mask, basis, cond, clean_pred) -> float:
    pred = X.predictions(run(model, recip, d_states, sites, mask, basis), cond)
    return float((pred != clean_pred).float().mean())


def stage_nominate(device, arms, recipe, seeds):
    """Nomination on development episodes only, reads frozen to disk."""
    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=device)
    recip = A.to_torch(G.batch([p["recipient"] for p in dev_pairs]), device)
    donor = A.to_torch(G.batch([p["donor"] for p in dev_pairs]), device)
    swap = A.to_torch(G.batch(named_swap(dev_pairs, seed=4243)), device)
    out = {"family_size": FAMILY_SIZE, "site_sets": len(SITE_SETS), "label": READ_LABEL,
           "rank_caps": list(RANK_CAPS), "arms": {}}
    for arm in arms:
        for seed in seeds:
            key = f"{arm}/{recipe}/{seed}"
            m = load_arm(arm, recipe, seed, device)
            r_own = fit_reads(m, recip, "own", G.OWN)
            r_named = fit_reads(m, recip, "named", G.OTHER)
            r_named_at_own = fit_reads(m, recip, "named", G.OWN)
            np.savez(os.path.join(OUT, f"reads_{arm}_{recipe}_seed{seed}.npz"),
                     **{f"own|{l}": v["coef"] for l, v in r_own.items()},
                     **{f"named|{l}": v["coef"] for l, v in r_named.items()},
                     **{f"named_at_own|{l}": v["coef"] for l, v in r_named_at_own.items()})
            own_nom = nominate(m, recip, donor, r_own, G.OWN, device)
            named_nom = nominate(m, recip, swap, r_named, G.OTHER, device)
            out["arms"][key] = dict(
                ownership=own_nom, control2_named_agent=named_nom,
                fit_accuracy=dict(
                    own={l: v["fit_accuracy"] for l, v in r_own.items()},
                    named={l: v["fit_accuracy"] for l, v in r_named.items()},
                    named_at_own={l: v["fit_accuracy"] for l, v in r_named_at_own.items()}))
            n = own_nom["nomination"]
            log(f"    {key}: " + (f"{n['positions']} layers {n['layers']} rank {n['rank']}: "
                                  f"whole {n['accuracy_whole']:.4f} ownership-only "
                                  f"{n['accuracy_ownership_only']:.4f}; "
                                  f"{own_nom['site_sets_clearing']} of 44 site sets clear"
                                  if n else "no verdict") +
                f"   | control 2 named-agent nomination: {named_nom['status']}")
    tag = "_".join(arms)
    log(f"  wrote {save_json(f'nominate_{recipe}_{tag}.json', out)}")


def load_reads(arm, recipe, seed, device):
    z = np.load(os.path.join(OUT, f"reads_{arm}_{recipe}_seed{seed}.npz"))
    out = {"own": {}, "named": {}, "named_at_own": {}}
    for k in z.files:
        kind, l = k.split("|")
        out[kind][int(l)] = dict(coef=z[k])
    return out


def load_nominations(recipe):
    res = {}
    for f in sorted(os.listdir(OUT)):
        if f.startswith(f"nominate_{recipe}_") and f.endswith(".json"):
            res.update(load_json(f)["arms"])
    return res


def reading(whole, own, untouched, acc) -> dict:
    """The chance-corrected form (page 2), the floor of page 1c, and every
    quantity printed beside it."""
    fl = floor_check(whole, untouched, acc)
    room = whole - untouched
    deg = (whole - own) / room if fl["clears"] else None
    return dict(accuracy_whole=whole, accuracy_ownership_only=own,
                accuracy_untouched=untouched, arm_own_accuracy=acc,
                raw_difference=whole - own, floor=fl,
                status=("no verdict" if deg is None else "negative" if deg < 0 else "valid"),
                degree=deg,
                version1_form=((whole - own) / whole if whole > 0 else None))


def stage_measure(device, arms, recipe, seeds):
    """The frozen nomination applied once to fresh episodes (method file,
    section 6), with every control, the rider and the fourth arm's checks."""
    noms = load_nominations(recipe)
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=device)
    coll_pairs, _ = T.make_data(800, seed=778, pool="fresh", device=device, collide=True)
    other_pairs, _ = T.make_data(800, seed=779, pool="fresh", device=device)
    recip = A.to_torch(G.batch([p["recipient"] for p in fresh_pairs]), device)
    donor = A.to_torch(G.batch([p["donor"] for p in fresh_pairs]), device)
    swap = A.to_torch(G.batch(named_swap(fresh_pairs, seed=781)), device)
    o_rec = A.to_torch(G.batch([p["recipient"] for p in other_pairs]), device)
    d_tgt = donor["targets"][:, G.OWN]
    out = {"arms": {}}
    for arm in arms:
        for seed in seeds:
            key = f"{arm}/{recipe}/{seed}"
            m = load_arm(arm, recipe, seed, device)
            nom = noms[key]
            reads = load_reads(arm, recipe, seed, device)
            D = m.cfg.d_model
            with torch.no_grad():
                clean = m(recip)
            clean_own = X.predictions(clean, G.OWN)
            clean_other = X.predictions(clean, G.OTHER)
            u_hits = hits(clean, d_tgt, G.OWN)
            u = float(u_hits.mean())
            own_hits = hits(clean, recip["targets"][:, G.OWN], G.OWN)
            acc = float(own_hits.mean())
            acc_other = float(hits(clean, recip["targets"][:, G.OTHER], G.OTHER).mean())
            d_states = X.capture(m, donor)
            row = dict(arm_own_accuracy_fresh=acc, arm_other_accuracy_fresh=acc_other,
                       accuracy_untouched=u, no_transplant_rate_formula=(1 - acc) / 7,
                       no_transplant_rate_miss=u - (1 - acc) / 7, n_trials=len(u_hits))
            spec = nom["ownership"]["nomination"]
            if spec is None:
                row["status"] = "no verdict at nomination"
                out["arms"][key] = row
                log(f"    {key}: no verdict at nomination")
                continue
            sites = X.Sites(tuple(spec["layers"]), spec["positions"])
            mask = X.position_mask(recip, spec["positions"])
            basis = {l: RH.basis_for(reads["own"][l]["coef"], spec["rank"], device)
                     for l in sites.layers}
            w_hits = hits(run(m, recip, d_states, sites, mask, None), d_tgt, G.OWN)
            o_hits = hits(run(m, recip, d_states, sites, mask, basis), d_tgt, G.OWN)
            row.update(site_set=spec, reading=reading(float(w_hits.mean()),
                                                      float(o_hits.mean()), u, acc),
                       per_trial=dict(untouched=u_hits.tolist(), whole=w_hits.tolist(),
                                      ownership_only=o_hits.tolist()))

            # ------------------------------------------------ controls
            c = {}
            comp = {}
            for l in sites.layers:
                bb = basis[l].detach().cpu().numpy()
                uu, sv, _ = np.linalg.svd(np.eye(D) - bb @ bb.T)
                comp[l] = torch.as_tensor(np.ascontiguousarray(uu[:, sv > 1e-6]),
                                          dtype=torch.float32, device=device)
            c["1 content transplant (the complement subspace)"] = float(
                hits(run(m, recip, d_states, sites, mask, comp), d_tgt, G.OWN).mean())
            # 2, as it was run on 2026-09-21, kept for continuity only
            c["2-old unmatched donor's ownership subspace (as run 2026-09-21)"] = float(
                hits(run(m, recip, X.capture(m, o_rec), sites, mask, basis), d_tgt,
                     G.OWN).mean())
            rng = np.random.default_rng(seed)
            rand = {l: X.orthonormal(rng.normal(size=(spec["rank"], D))).to(device)
                    for l in sites.layers}
            c["3 matched random subspace, same rank"] = float(
                hits(run(m, recip, d_states, sites, mask, rand), d_tgt, G.OWN).mean())
            pre = X.position_mask(recip, "pre-identity")
            c["4 transplant before the identity can be known"] = float(
                hits(run(m, recip, d_states, sites, pre, None), d_tgt, G.OWN).mean())
            c["5 fresh markers and content (share of trials)"] = 1.0
            cr, cd, cs, ct = RH._states_and_targets(m, coll_pairs, device)
            cm = X.position_mask(cr, spec["positions"])
            same = (cr["targets"][:, G.OWN] == ct)
            with torch.no_grad():
                c_clean = X.predictions(m(cr), G.OWN)
            moved = X.predictions(run(m, cr, cs, sites, cm, None), G.OWN) != c_clean
            c["6a same-value cell: share whose action moved"] = \
                float(moved[same].float().mean()) if int(same.sum()) else None
            c["6a same-value cell: trials"] = int(same.sum())
            c["6b different-value cell: share whose action moved"] = \
                float(moved[~same].float().mean())
            c["6b different-value cell: trials"] = int((~same).sum())
            null = run(m, recip, X.capture(m, recip), sites, mask, None)
            c["7 null transplant leaves every logit bit-identical"] = bool(torch.equal(clean, null))
            row["controls"] = c

            # --------------------- control 2 as the proposal states it (method 4)
            s_states = X.capture(m, swap)
            c2 = {}
            nn_ = nom["control2_named_agent"]
            if nn_["status"] == "nominated":
                ns = nn_["nomination"]
                n_sites = X.Sites(tuple(ns["layers"]), ns["positions"])
                n_mask = anchored_mask(recip, ns["positions"], G.OTHER)
                n_basis = {l: RH.basis_for(reads["named"][l]["coef"], ns["rank"], device)
                           for l in n_sites.layers}
                n_rng = np.random.default_rng(100 + seed)
                n_rand = {l: X.orthonormal(n_rng.normal(size=(ns["rank"], D))).to(device)
                          for l in n_sites.layers}
                own_moved = moved_share(m, recip, s_states, n_sites, n_mask, n_basis,
                                        G.OWN, clean_own)
                rand_moved = moved_share(m, recip, s_states, n_sites, n_mask, n_rand,
                                         G.OWN, clean_own)
                c2["full procedure"] = dict(
                    status="pass" if own_moved <= rand_moved + CONTROL2_TOLERANCE else "fail",
                    site_set=ns, own_directed_moved=own_moved,
                    own_directed_moved_random_subspace=rand_moved,
                    named_other_moved=moved_share(m, recip, s_states, n_sites, n_mask,
                                                  n_basis, G.OTHER, clean_other))
            else:
                c2["full procedure"] = dict(status="no verdict", reason=nn_.get("reason"),
                                            arm_named_other_accuracy_dev=nn_["arm_accuracy"],
                                            site_sets_clearing=nn_["site_sets_clearing"])
            f_basis = {l: RH.basis_for(reads["named_at_own"][l]["coef"], spec["rank"], device)
                       for l in sites.layers}
            f_own = moved_share(m, recip, s_states, sites, mask, f_basis, G.OWN, clean_own)
            f_rand = moved_share(m, recip, s_states, sites, mask, rand, G.OWN, clean_own)
            c2["fixed-site variant"] = dict(
                status="pass" if f_own <= f_rand + CONTROL2_TOLERANCE else "fail",
                own_directed_moved=f_own, own_directed_moved_random_subspace=f_rand,
                named_other_moved=moved_share(m, recip, s_states, sites, mask, f_basis,
                                              G.OTHER, clean_other))
            row["control2"] = c2

            # ------------------------------------------ the rider (method 3.4)
            tn = noms.get(f"T/{recipe}/{seed}")
            tspec = tn["ownership"]["nomination"] if tn else None
            if tspec is not None:
                t_sites = X.Sites(tuple(tspec["layers"]), tspec["positions"])
                t_mask = X.position_mask(recip, tspec["positions"])
                t_basis = {l: RH.basis_for(reads["own"][l]["coef"], tspec["rank"], device)
                           for l in t_sites.layers}
                tw = float(hits(run(m, recip, d_states, t_sites, t_mask, None),
                                d_tgt, G.OWN).mean())
                to = float(hits(run(m, recip, d_states, t_sites, t_mask, t_basis),
                                d_tgt, G.OWN).mean())
                row["rider_at_arm_T_site_set"] = dict(site_set=tspec,
                                                      reading=reading(tw, to, u, acc))

            # ---------------------------- oracle, and the fourth arm's route check
            if arm in ("T", "M"):
                eye = torch.eye(D, device=device)[:, m.cfg.d_content:]
                oh = hits(run(m, recip, d_states, sites, mask,
                              {l: eye for l in sites.layers}), d_tgt, G.OWN)
                row["oracle_reading"] = reading(float(w_hits.mean()), float(oh.mean()), u, acc)
            if arm == "M":
                route = m.entangled_route(recip)[:, G.OWN].cpu().numpy()
                aT, uT = float(w_hits[~route].mean()), float(u_hits[~route].mean())
                aC, uC = float(w_hits[route].mean()), float(u_hits[route].mean())
                p = float(route.mean())
                den = (1 - p) * (aT - uT) + p * (aC - uC)
                row["fourth_arm"] = dict(
                    entangled_share=p, separable_route_whole=aT, separable_route_untouched=uT,
                    entangled_route_whole=aC, entangled_route_untouched=uC,
                    predicted_from_route_accuracies=(p * (aC - uC) / den) if den else None,
                    ownership_only_by_route=dict(separable=float(o_hits[~route].mean()),
                                                 entangled=float(o_hits[route].mean())),
                    arm_own_accuracy_by_route=dict(separable=float(own_hits[~route].mean()),
                                                   entangled=float(own_hits[route].mean())))
            out["arms"][key] = row
            rd = row["reading"]
            log(f"    {key}: untouched {u:.4f} whole {rd['accuracy_whole']:.4f} "
                f"ownership-only {rd['accuracy_ownership_only']:.4f} -> {rd['status']}"
                + (f", degree {rd['degree']:.4f}" if rd["degree"] is not None else "")
                + f"   (arm own accuracy {acc:.4f})")
    tag = "_".join(arms)
    log(f"  wrote {save_json(f'measure_{recipe}_{tag}.json', out)}")


def stage_summary(device, arms, recipe, seeds):
    """Uncertainty (page 1g), separation (page 1a), from the measure files
    already written. Pure arithmetic on committed outputs."""
    rows = {}
    for f in sorted(os.listdir(OUT)):
        if f.startswith(f"measure_{recipe}_") and f.endswith(".json"):
            rows.update(load_json(f)["arms"])
    rng = np.random.default_rng(20260921)
    out = {"arms": {}, "separation": {}}
    for arm in arms:
        raw, deg, boot = [], [], []
        for seed in seeds:
            r = rows.get(f"{arm}/{recipe}/{seed}")
            if not r or "reading" not in r:
                continue
            w = np.array(r["per_trial"]["whole"])
            o = np.array(r["per_trial"]["ownership_only"])
            raw.append(float(w.mean() - o.mean()))
            deg.append(r["reading"]["degree"])
            draws = []
            for _ in range(2000):
                idx = rng.integers(0, len(w), len(w))
                draws.append(float(w[idx].mean() - o[idx].mean()))
            boot.append(float(np.std(draws)))
        valid = [d for d in deg if d is not None]
        out["arms"][arm] = dict(
            per_seed_raw_difference=raw, per_seed_degree=deg,
            across_seed_sd_of_raw_difference=float(np.std(raw, ddof=1)) if len(raw) > 1 else None,
            within_seed_bootstrap_se=boot,
            degree_range=[min(valid), max(valid)] if valid else None)
    for seed in seeds:
        t = rows.get(f"T/{recipe}/{seed}", {}).get("reading", {}).get("degree")
        cc = rows.get(f"C/{recipe}/{seed}", {}).get("reading", {}).get("degree")
        if t is not None and cc is not None:
            out["separation"][str(seed)] = dict(C_minus_T=cc - t, clears_0_5=(cc - t) >= 0.5)
    log(f"  wrote {save_json(f'summary_{recipe}.json', out)}")
    for arm, v in out["arms"].items():
        log(f"    {arm}: degrees {[round(d, 4) if d is not None else None for d in v['per_seed_degree']]}"
            f", raw {[round(x, 4) for x in v['per_seed_raw_difference']]}"
            f", across-seed sd {v['across_seed_sd_of_raw_difference']}")
    log(f"    separation C - T per seed: {out['separation']}")


STAGES = ("train", "gate", "nominate", "measure", "summary")


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
    else:
        assert len(recipes) == 1, "nominate, measure and summary take one recipe"
        dict(nominate=stage_nominate, measure=stage_measure,
             summary=stage_summary)[a.stage](device, arms, recipes[0], seeds)
    log(f"  ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
