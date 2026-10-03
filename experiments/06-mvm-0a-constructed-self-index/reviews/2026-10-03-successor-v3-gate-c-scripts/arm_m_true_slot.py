"""Gate C tier 1 review of successor proposal version 3 (2026-10-03).

Proposal section 5.3 says one check is owed: arm M's blind reading against its
true-slot reading "within 0.10" at the site sets the registered rule
nominates (layer 1, post-identity, rank 8 on every seed). This runs it, on the
same 800 fresh episodes (seed 777) and the committed models and reads, with
the true-slot reading computed two ways as repairs.stage_measure does: the
oracle transplant of the slot's own dimensions, and the route formula.

Reads only committed files, trains nothing. $0.
Run from experiments/rehearsal-successor-measure/src.
"""
import json, os, sys
import numpy as np, torch
sys.path.insert(0, os.getcwd())
import rerun_v3 as V, repairs as R, rehearse as RH, transplant as X, grammar as G

dev = torch.device("cpu")
recip, donor = V.fresh_batches(dev)
d_tgt = donor["targets"][:, G.OWN]
summ = json.load(open(os.path.join(V.OUT, "pass2_summary.json")))["arms"]
print("seed | site set | blind reading (committed) | blind reading (this run) | oracle true-slot reading | route formula | blind minus oracle | blind minus formula | within 0.10")
for seed in V.SEEDS:
    spec = summ[f"M/{seed}"]["primary"]["site_set"]
    committed = summ[f"M/{seed}"]["primary"]["reading"]["degree"]
    m = V.load_model("M", seed, dev)
    reads = V.committed_reads("M", seed)
    D = m.cfg.d_model
    with torch.no_grad():
        clean = m(recip)
    u_hits = R.hits(clean, d_tgt, G.OWN); u = float(u_hits.mean())
    acc = float(R.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
    d_states = X.capture(m, donor)
    L = tuple(spec["layers"]); sites = X.Sites(L, spec["positions"])
    mask = X.position_mask(recip, spec["positions"])
    basis = {l: RH.basis_for(reads[l], spec["rank"], dev) for l in L}
    w_hits = R.hits(R.run(m, recip, d_states, sites, mask, None), d_tgt, G.OWN)
    o_hits = R.hits(R.run(m, recip, d_states, sites, mask, basis), d_tgt, G.OWN)
    eye = torch.eye(D)[:, m.cfg.d_content:]
    oh = R.hits(R.run(m, recip, d_states, sites, mask, {l: eye for l in L}), d_tgt, G.OWN)
    blind = R.reading(float(w_hits.mean()), float(o_hits.mean()), u, acc)["degree"]
    oracle = R.reading(float(w_hits.mean()), float(oh.mean()), u, acc)["degree"]
    route = m.entangled_route(recip)[:, G.OWN].cpu().numpy()
    aT, uT = float(w_hits[~route].mean()), float(u_hits[~route].mean())
    aC, uC = float(w_hits[route].mean()), float(u_hits[route].mean())
    p = float(route.mean())
    formula = p * (aC - uC) / ((1 - p) * (aT - uT) + p * (aC - uC))
    print(f"{seed} | layers {L} at {spec['positions']}, rank {spec['rank']} | {committed:.4f} | {blind:.4f} | "
          f"{oracle:.4f} | {formula:.4f} | {blind-oracle:+.4f} | {blind-formula:+.4f} | "
          f"{abs(blind-oracle) <= 0.10 and abs(blind-formula) <= 0.10}")
    print(f"      separable route: whole {aT:.4f}, untouched {uT:.4f}; entangled route: whole {aC:.4f}, untouched {uC:.4f}; entangled share {p:.5f}")
