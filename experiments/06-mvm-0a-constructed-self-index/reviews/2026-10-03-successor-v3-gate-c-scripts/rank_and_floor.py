"""Gate C tier 1 review of successor proposal version 3 (2026-10-03).

Two prints, from committed models and files only, $0:
 1. Arm C on the 800 fresh episodes at its nominated layer and position set,
    at every rank cap: the reading, so a reader can see whether the reading
    depends on the rank the rule happened to pick.
 2. Every arm and seed: whether the whole-state floor clears on development
    episodes (where the nomination applies it) and on fresh episodes (where
    the reading applies it), with the margin.
Run from experiments/rehearsal-successor-measure/src.
"""
import json, os, sys
import torch
sys.path.insert(0, os.getcwd())
import rerun_v3 as V, repairs as R, rehearse as RH, transplant as X, grammar as G

dev = torch.device("cpu")
recip, donor = V.fresh_batches(dev)
d_tgt = donor["targets"][:, G.OWN]
summ = json.load(open(os.path.join(V.OUT, "pass2_summary.json")))["arms"]
print("blocks in the toy model:", V.load_model("F", 0, dev).cfg.n_layers, "| running states:", V.N_STATES)
print("1. arm C, fresh episodes, reading by rank at the nominated layer and position set")
for seed in V.SEEDS:
    spec = summ[f"C/{seed}"]["primary"]["site_set"]
    m = V.load_model("C", seed, dev); reads = V.committed_reads("C", seed)
    with torch.no_grad():
        clean = m(recip)
    u = float(R.hits(clean, d_tgt, G.OWN).mean())
    acc = float(R.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
    ds = X.capture(m, donor)
    L = tuple(spec["layers"]); sites = X.Sites(L, spec["positions"]); mask = X.position_mask(recip, spec["positions"])
    w = float(R.hits(R.run(m, recip, ds, sites, mask, None), d_tgt, G.OWN).mean())
    cells = []
    for k in R.RANK_CAPS:
        o = float(R.hits(R.run(m, recip, ds, sites, mask, {l: RH.basis_for(reads[l], k, dev) for l in L}), d_tgt, G.OWN).mean())
        cells.append(f"rank {k}: ownership-only {o:.4f}, reading {R.reading(w, o, u, acc)['degree']:.4f}")
    print(f"C/{seed} layers {L} at {spec['positions']} (nominated rank {spec['rank']}); whole {w:.4f}, untouched {u:.4f} | " + " | ".join(cells))
print("2. whole-state floor, development (nomination) and fresh (reading)")
for arm in V.ARMS:
    for seed in V.SEEDS:
        p = summ[f"{arm}/{seed}"]["primary"]; spec = p["site_set"]
        nom = json.load(open(os.path.join(V.OUT, f"nominate_{arm}_seed{seed}.json")))
        g = [x for x in nom["grid"] if x["layers"] == spec["layers"] and x["positions"] == spec["positions"] and x["rank"] == spec["rank"]][0]
        fd, ff = g["floor"], p["reading"]["floor"]
        print(f"{arm}/{seed} development: clears {fd['clears']} (room {fd['room']:.4f}, needed {fd['required_room']:.4f}) | "
              f"fresh: clears {ff['clears']} (room {ff['room']:.4f}, needed {ff['required_room']:.4f})")
