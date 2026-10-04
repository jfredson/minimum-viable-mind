"""The controls re-run under the registered rules (2026-10-03).

UNREGISTERED rehearsal code. Method, committed before this was run:
docs/controls-rerun-method-2026-10-03.md. Section numbers in comments are
that file's. Loads the twelve committed base-recipe toy models; trains
nothing but small logistic regressions; processor only; $0.

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python rerun_controls.py

Writes ../out-controls-rerun/{nominate,measure}_{arm}_seed{seed}.json,
summary.json and table.md.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arms as A            # noqa: E402
import grammar as G         # noqa: E402
import rehearse as RH       # noqa: E402
import repairs as R         # noqa: E402
import rerun_v3 as V        # noqa: E402
import training as T        # noqa: E402
import transplant as X      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "out-controls-rerun"))
DEVICE = torch.device("cpu")                     # section 3, and finding RT-232
ARMS, SEEDS, RANKS = ("T", "C", "F", "M"), (0, 1, 2), (1, 2, 4, 8)
N_STATES = 5
CONTIG = [tuple(range(a, b + 1)) for a in range(N_STATES) for b in range(a, N_STATES)]
POS = ["action", "action+ans", "action+3", "post-identity"]
FAMILY = [(L, P) for L in CONTIG for P in POS if not (0 in L and P != "action")]   # rule 4
STRICT = [(L, P) for (L, P) in FAMILY if 0 not in L]                                # rule 10
assert len(FAMILY) == 45 and len(FAMILY) * len(RANKS) == 180 and len(STRICT) == 40
HELD_OUT, PIECE_MIN = 180, 144                   # rule 7: four fifths of 180
ROOM = 0.018
C2_TOL = 0.05
OTHER_BAR = 790


def log(*a):
    print(*a, flush=True)


def save(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as f:
        json.dump(obj, f, indent=1, sort_keys=True, default=lambda o: list(o))
    return name


def check_sha(arm, seed):
    """K1."""
    path = V.ckpt(arm, seed)
    want = {}
    with open(os.path.join(V.CKPT_DIR, "SHA256SUMS")) as f:
        for line in f:
            h, n = line.split()
            want[n] = h
    got = V.sha256(path)
    assert want[os.path.basename(path)] == got, f"K1: {path} does not match SHA256SUMS"
    return got


def batches(pairs):
    recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), DEVICE)
    donor = A.to_torch(G.batch([p["donor"] for p in pairs]), DEVICE)
    return recip, donor


def correct_count(h, y):
    """Held-out correct, of 180, of a fresh read on features h (rule 2's split)."""
    if h.ndim == 1:
        h = h[:, None]
    n_tr = int(0.7 * len(y))
    clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], y[:n_tr])
    return int(round(clf.score(h[n_tr:], y[n_tr:]) * (len(y) - n_tr)))


def accuracies(m, recip, coefs, target, cond):
    """Per layer: the whole read's held-out count, and each size's piece count."""
    with torch.no_grad():
        _, states = m(recip, capture=True)
    ap = recip["action_pos"][:, cond]
    y = R.read_labels(recip, target)
    assert len(y) - int(0.7 * len(y)) == HELD_OUT
    out = {}
    for l, st in enumerate(states):
        h = st[torch.arange(st.shape[0]), ap].numpy()
        out[l] = dict(whole=correct_count(h, y),
                      piece={r: correct_count(h @ RH.basis_for(coefs[l], r, DEVICE).numpy(), y)
                             for r in RANKS})
    return out


def grid(m, recip, donor, coefs, cond):
    """Every site set of the family at every size, on development episodes."""
    d_states = X.capture(m, donor)
    d_tgt = donor["targets"][:, cond]
    with torch.no_grad():
        clean = m(recip)
    u = float(R.hits(clean, d_tgt, cond).mean())
    acc = float(R.hits(clean, recip["targets"][:, cond], cond).mean())
    rows = []
    for L, P in FAMILY:
        sites = X.Sites(layers=tuple(L), positions=P)
        mask = R.anchored_mask(recip, P, cond)
        whole = float(R.hits(R.run(m, recip, d_states, sites, mask, None), d_tgt, cond).mean())
        fl = R.floor_check(whole, u, acc)
        for r in RANKS:
            basis = {l: RH.basis_for(coefs[l], r, DEVICE) for l in L}
            own = float(R.hits(R.run(m, recip, d_states, sites, mask, basis), d_tgt, cond).mean())
            rows.append(dict(layers=list(L), positions=P, rank=r, accuracy_whole=whole,
                             accuracy_ownership_only=own, floor=fl))
    return dict(untouched=u, arm_accuracy=acc, grid=rows)


def pick(rows, fits, family, require_piece=True):
    """Rules 5 to 9. Returns (spec or None, reason, candidates considered)."""
    fam = {(tuple(L), P) for L, P in family}
    pos_index = {P: i for i, P in enumerate(POS)}
    clearing = [g for g in rows if g["floor"]["clears"] and (tuple(g["layers"]), g["positions"]) in fam]
    if not clearing:
        return None, "no site set clears the whole-state floor", []
    smallest = {}
    for g in clearing:
        key = (len(g["layers"]), g["layers"])
        if g["positions"] not in smallest or key < smallest[g["positions"]]:
            smallest[g["positions"]] = key
    cands = [dict(g, piece_correct=min(fits[l]["piece"][g["rank"]] for l in g["layers"]),
                  whole_read_correct=min(fits[l]["whole"] for l in g["layers"]))
             for g in clearing if (len(g["layers"]), g["layers"]) == smallest[g["positions"]]]
    ok = [g for g in cands if g["piece_correct"] >= PIECE_MIN] if require_piece else cands
    if not ok:
        return None, "read failed its floor: no size's piece reaches four fifths", cands
    best = min(ok, key=lambda g: (-g["accuracy_ownership_only"], g["rank"], pos_index[g["positions"]]))
    return best, "nominated", cands


def spec_of(g):
    return None if g is None else dict(layers=list(g["layers"]), positions=g["positions"],
                                       rank=g["rank"], piece_correct=g["piece_correct"],
                                       whole_read_correct=g["whole_read_correct"])


def measure_at(m, arm, seed, spec, coefs, fresh, coll_pairs, described_only):
    """Section 4, everything at one site set, on fresh episodes."""
    recip, donor = fresh
    D = m.cfg.d_model
    d_tgt = donor["targets"][:, G.OWN]
    with torch.no_grad():
        clean = m(recip)
    u_hits = R.hits(clean, d_tgt, G.OWN)
    u = float(u_hits.mean())
    acc = float(R.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
    d_states = X.capture(m, donor)
    L = tuple(spec["layers"])
    sites = X.Sites(L, spec["positions"])
    mask = X.position_mask(recip, spec["positions"])
    basis = {l: RH.basis_for(coefs[l], spec["rank"], DEVICE) for l in L}
    w_hits = R.hits(R.run(m, recip, d_states, sites, mask, None), d_tgt, G.OWN)
    o_hits = R.hits(R.run(m, recip, d_states, sites, mask, basis), d_tgt, G.OWN)
    w, o = float(w_hits.mean()), float(o_hits.mean())
    row = dict(site_set=spec, described_only=described_only,
               reading=R.reading(w, o, u, acc),
               no_transplant=dict(rate=u, formula=(1 - acc) / 7, miss=u - (1 - acc) / 7,
                                  inside_allowance=abs(u - (1 - acc) / 7) <= ROOM))
    c = {}
    # control 1: the complement of the piece
    comp = {}
    for l in L:
        bb = basis[l].numpy()
        uu, sv, _ = np.linalg.svd(np.eye(D) - bb @ bb.T)
        comp[l] = torch.as_tensor(np.ascontiguousarray(uu[:, sv > 1e-6]), dtype=torch.float32)
    c1 = float(R.hits(R.run(m, recip, d_states, sites, mask, comp), d_tgt, G.OWN).mean())
    c["1"] = dict(complement_donor_share=c1, whole=w, untouched=u,
                  holds_on_arm_T=(c1 <= u + ROOM) if arm == "T" else None)
    # control 3: twenty random pieces
    rand = [float(R.hits(R.run(m, recip, d_states, sites, mask, rb), d_tgt, G.OWN).mean())
            for rb in V.random_bases(spec["rank"], L, seed, D, DEVICE)]
    c["3"] = dict(median=float(np.median(rand)), p95=float(np.percentile(rand, 95)),
                  ownership_only=o, below=sum(x < o for x in rand),
                  equal=sum(x == o for x in rand), above=sum(x > o for x in rand))
    # control 4: before the identity can be known
    pre = X.position_mask(recip, "pre-identity")
    c4 = float(R.hits(R.run(m, recip, d_states, sites, pre, None), d_tgt, G.OWN).mean())
    c["4"] = dict(donor_share=c4, untouched=u, above_untouched=c4 - u)
    # control 6: same value against different value, on the relaxed set
    cr, cd, cs, ct = RH._states_and_targets(m, coll_pairs, DEVICE)
    cm = X.position_mask(cr, spec["positions"])
    same = (cr["targets"][:, G.OWN] == ct)
    with torch.no_grad():
        c_clean = X.predictions(m(cr), G.OWN)
    moved = X.predictions(R.run(m, cr, cs, sites, cm, None), G.OWN) != c_clean
    c["6"] = dict(same_value_trials=int(same.sum()), different_value_trials=int((~same).sum()),
                  same_value_moved=float(moved[same].float().mean()) if int(same.sum()) else None,
                  different_value_moved=float(moved[~same].float().mean()))
    # control 7: the null transplant
    null = R.run(m, recip, X.capture(m, recip), sites, mask, None)
    c["7"] = dict(bit_identical=bool(torch.equal(clean, null)))
    row["controls"] = c
    # the true-slot reference, arms T and M
    if arm in ("T", "M"):
        eye = torch.eye(D)[:, m.cfg.d_content:]
        oh = float(R.hits(R.run(m, recip, d_states, sites, mask, {l: eye for l in L}),
                          d_tgt, G.OWN).mean())
        row["true_slot"] = dict(reading=R.reading(w, oh, u, acc))
    if arm == "M":
        route = m.entangled_route(recip)[:, G.OWN].numpy()
        aT, uT = float(w_hits[~route].mean()), float(u_hits[~route].mean())
        aC, uC = float(w_hits[route].mean()), float(u_hits[route].mean())
        p = float(route.mean())
        row["true_slot"]["route_formula"] = p * (aC - uC) / ((1 - p) * (aT - uT) + p * (aC - uC))
        row["true_slot"]["entangled_share"] = p
    return row, dict(recip=recip, d_states=d_states, d_tgt=d_tgt, u=u, acc=acc, clean=clean)


def control2(m, arm, seed, reads, dev, dev_swap, fresh_recip, fresh_swap, other_correct):
    """Section 4, control 2, by the identical procedure with the named label."""
    if arm in ("T", "M"):
        return dict(status="not applicable", reason="ruled: the named agent is held outside the running state")
    if other_correct < OTHER_BAR:
        return dict(status="no verdict", named_other_correct=other_correct,
                    reason="the arm has not learned the named-other condition")
    coefs = {l: v["coef"] for l, v in reads["named"].items()}
    fits = accuracies(m, dev, coefs, "named", G.OTHER)
    g = grid(m, dev, dev_swap, coefs, G.OTHER)
    best, why, cands = pick(g["grid"], fits, FAMILY)
    out = dict(named_other_correct=other_correct, named_read_fits=fits,
               dev_untouched=g["untouched"], dev_named_other_accuracy=g["arm_accuracy"],
               candidates=[spec_of(c) | dict(dev_ownership_only=c["accuracy_ownership_only"],
                                             dev_whole=c["accuracy_whole"]) for c in cands])
    if best is None:
        out.update(status="no verdict", reason=why)
        return out
    spec = spec_of(best)
    L = tuple(spec["layers"])
    sites = X.Sites(L, spec["positions"])
    mask = R.anchored_mask(fresh_recip, spec["positions"], G.OTHER)
    basis = {l: RH.basis_for(coefs[l], spec["rank"], DEVICE) for l in L}
    rng = np.random.default_rng(100 + seed)
    rand = {l: X.orthonormal(rng.normal(size=(spec["rank"], m.cfg.d_model))) for l in L}
    s_states = X.capture(m, fresh_swap)
    with torch.no_grad():
        clean = m(fresh_recip)
    own_clean, oth_clean = X.predictions(clean, G.OWN), X.predictions(clean, G.OTHER)
    own_moved = R.moved_share(m, fresh_recip, s_states, sites, mask, basis, G.OWN, own_clean)
    rand_moved = R.moved_share(m, fresh_recip, s_states, sites, mask, rand, G.OWN, own_clean)
    out.update(status="pass" if own_moved <= rand_moved + C2_TOL else "fail", site_set=spec,
               own_directed_moved=own_moved, own_directed_moved_random_piece=rand_moved,
               named_other_moved=R.moved_share(m, fresh_recip, s_states, sites, mask, basis,
                                               G.OTHER, oth_clean))
    return out


def main():
    t0 = time.time()
    gate = json.load(open(os.path.join(V.OUT, "gate.json")))
    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEVICE)
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=DEVICE)
    coll_pairs, _ = T.make_data(800, seed=778, pool="fresh", device=DEVICE, collide=True)
    dev = batches(dev_pairs)
    fresh = batches(fresh_pairs)
    dev_swap = A.to_torch(G.batch(R.named_swap(dev_pairs, seed=4243)), DEVICE)
    fresh_swap = A.to_torch(G.batch(R.named_swap(fresh_pairs, seed=781)), DEVICE)
    summary = {}
    noms = {}
    # ---- pass 1: nomination on development episodes, every arm and seed
    for arm in ARMS:
        for seed in SEEDS:
            sha = check_sha(arm, seed)
            m = V.load_model(arm, seed, DEVICE)
            reads = R.load_reads(arm, "base", seed, DEVICE)
            coefs = {l: v["coef"] for l, v in reads["own"].items()}
            fits = accuracies(m, dev[0], coefs, "own", G.OWN)
            g = grid(m, dev[0], dev[1], coefs, G.OWN)
            best, why, cands = pick(g["grid"], fits, FAMILY)
            sbest, swhy, _ = pick(g["grid"], fits, STRICT)
            unfiltered, _, _ = pick(g["grid"], fits, FAMILY, require_piece=False)
            nom = dict(arm=arm, seed=seed, checkpoint_sha256=sha, fits=fits,
                       dev_untouched=g["untouched"], dev_accuracy=g["arm_accuracy"],
                       site_sets_clearing=len({(tuple(x["layers"]), x["positions"])
                                               for x in g["grid"] if x["floor"]["clears"]}),
                       candidates=[spec_of(c) | dict(dev_ownership_only=c["accuracy_ownership_only"],
                                                     dev_whole=c["accuracy_whole"]) for c in cands],
                       primary=dict(status=why, site_set=spec_of(best)),
                       stricter=dict(status=swhy, site_set=spec_of(sbest)),
                       rule_7_switched_off=spec_of(unfiltered), grid=g["grid"])
            noms[(arm, seed)] = nom
            save(f"nominate_{arm}_seed{seed}.json", nom)
            log(f"nominate {arm}/{seed}: primary {why} {spec_of(best)} | stricter {swhy} "
                f"{spec_of(sbest)} | rule 7 off {spec_of(unfiltered)}")
    # ---- pass 2: fresh episodes
    for arm in ARMS:
        for seed in SEEDS:
            m = V.load_model(arm, seed, DEVICE)
            reads = R.load_reads(arm, "base", seed, DEVICE)
            coefs = {l: v["coef"] for l, v in reads["own"].items()}
            nom = noms[(arm, seed)]
            out = dict(arm=arm, seed=seed, gate=gate["verdicts"][arm], gate_run=gate["runs"][f"{arm}/{seed}"])
            spec = nom["primary"]["site_set"]
            described = spec is None
            if described:
                spec = nom["rule_7_switched_off"]
            out["nomination_status"] = nom["primary"]["status"]
            if spec is not None:
                out["primary"], ctx = measure_at(m, arm, seed, spec, coefs, fresh, coll_pairs, described)
            sspec = nom["stricter"]["site_set"]
            if sspec is not None:
                out["stricter"], _ = measure_at(m, arm, seed, sspec, coefs, fresh, coll_pairs, False)
            # the rider: arm T's site set and size for the same seed, this arm's own read
            tspec = noms[("T", seed)]["primary"]["site_set"]
            if tspec is not None and spec is not None:
                tL = tuple(tspec["layers"])
                ts = X.Sites(tL, tspec["positions"])
                tm = X.position_mask(ctx["recip"], tspec["positions"])
                tb = {l: RH.basis_for(coefs[l], tspec["rank"], DEVICE) for l in tL}
                tw = float(R.hits(R.run(m, ctx["recip"], ctx["d_states"], ts, tm, None), ctx["d_tgt"], G.OWN).mean())
                to = float(R.hits(R.run(m, ctx["recip"], ctx["d_states"], ts, tm, tb), ctx["d_tgt"], G.OWN).mean())
                out["rider_at_arm_T_site_set"] = dict(site_set=dict(layers=list(tL), positions=tspec["positions"],
                                                                    rank=tspec["rank"]),
                                                      reading=R.reading(tw, to, ctx["u"], ctx["acc"]))
            out["control2"] = control2(m, arm, seed, reads, dev[0], dev_swap, fresh[0], fresh_swap,
                                       gate["runs"][f"{arm}/{seed}"]["other_correct"])
            save(f"measure_{arm}_seed{seed}.json", out)
            summary[f"{arm}/{seed}"] = out
            p = out.get("primary")
            log(f"measure {arm}/{seed}: {out['nomination_status']}"
                + (f" | degree {p['reading']['degree']} | c7 {p['controls']['7']['bit_identical']}" if p else "")
                + f" | control 2 {out['control2']['status']}")
    sep = {}
    for seed in SEEDS:
        t = summary[f"T/{seed}"].get("primary"), summary[f"C/{seed}"].get("primary")
        if all(x and not x["described_only"] and x["reading"]["degree"] is not None for x in t):
            d = t[1]["reading"]["degree"] - t[0]["reading"]["degree"]
            sep[seed] = dict(C_minus_T=d, clears_0_5=d >= 0.5)
        else:
            sep[seed] = None
    save("summary.json", dict(separation=sep, arms=summary, seconds=time.time() - t0,
                              torch=torch.__version__, device=str(DEVICE)))
    # ---- the table
    def site(s):
        return f"layers {tuple(s['layers'])} at {s['positions']}, {s['rank']} directions"
    lines = ["| arm/seed | status | site set | whole read / piece, correct of 180 | whole, ownership-only, untouched | reading | control 1 complement | control 3 median, 95th; below/equal/above | control 4 share (minus untouched) | control 6 same moved (n), different moved (n) | control 7 | control 2 | true slot | rider |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for arm in ARMS:
        for seed in SEEDS:
            o = summary[f"{arm}/{seed}"]
            p = o.get("primary")
            if not p:
                lines.append(f"| {arm}/{seed} | {o['nomination_status']} | | | | | | | | | | {o['control2']['status']} | | |")
                continue
            s, r, c = p["site_set"], p["reading"], p["controls"]
            deg = "none" if r["degree"] is None else f"{r['degree']:.4f}"
            if p["described_only"]:
                deg = f"({deg}) reported for description; no reading"
            elif r["degree"] is None:
                deg = "no verdict: floor missed on fresh episodes"
            ts = p.get("true_slot")
            tsl = "" if not ts else (f"{ts['reading']['degree']:.4f}" + (f"; formula {ts['route_formula']:.4f}" if "route_formula" in ts else ""))
            rd = o.get("rider_at_arm_T_site_set")
            rdl = "" if not rd else ("no verdict" if rd["reading"]["degree"] is None else f"{rd['reading']['degree']:.4f}") + f" (whole {rd['reading']['accuracy_whole']:.4f})"
            c2 = o["control2"]
            c2l = c2["status"] + (f": own moved {c2['own_directed_moved']:.4f}, random {c2['own_directed_moved_random_piece']:.4f}" if "own_directed_moved" in c2 else "")
            sv = c["6"]["same_value_moved"]
            lines.append(
                f"| {arm}/{seed} | {o['nomination_status']} | {site(s)} | {s['whole_read_correct']} / {s['piece_correct']} | "
                f"{r['accuracy_whole']:.4f}, {r['accuracy_ownership_only']:.4f}, {r['accuracy_untouched']:.4f} | {deg} | "
                f"{c['1']['complement_donor_share']:.4f}" + (f" (holds: {c['1']['holds_on_arm_T']})" if arm == 'T' else "") + " | "
                f"{c['3']['median']:.4f}, {c['3']['p95']:.4f}; {c['3']['below']}/{c['3']['equal']}/{c['3']['above']} | "
                f"{c['4']['donor_share']:.4f} ({c['4']['above_untouched']:+.4f}) | "
                f"{'none' if sv is None else f'{sv:.4f}'} ({c['6']['same_value_trials']}), {c['6']['different_value_moved']:.4f} ({c['6']['different_value_trials']}) | "
                f"{'identical' if c['7']['bit_identical'] else 'DIFFERS'} | {c2l} | {tsl} | {rdl} |")
    lines.append("")
    lines.append("separation, arm C minus arm T: " + json.dumps(sep))
    with open(os.path.join(OUT, "table.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    log("\n".join(lines))
    log(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
