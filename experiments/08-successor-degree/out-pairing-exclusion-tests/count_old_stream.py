"""Replays the OLD stream for seed 0 (whole-content exclusion only) over the
development runs' 108,919 steps of 48 pairs, drawing exactly what
TrainingStream.pairs_for_step draws but without rendering, and counts contents
whose pairing is a fresh or relaxed pairing. Generator only; no model."""
import sys, time
sys.path.insert(0, sys.argv[1])
import numpy as np
import grammar as G
held = G.held_out_pairings(); fresh = {G.pairing(p["content"]) for p in G.eval_pairs("fresh")}
excl = G.eval_fingerprints()
STEPS, NP = 108919, 48
hits = []; n = 0; skipped = 0; t0 = time.time()
for s in range(1, STEPS + 1):
    rng = np.random.default_rng([1000 + 0, s]); got = 0
    while got < NP:
        c = G._content(rng, "train", False)
        if G.fingerprint(c) in excl:
            skipped += 1; continue
        rng.choice(G.eligible_models(c), size=2, replace=False)
        got += 1; n += 1
        if G.pairing(c) in held:
            hits.append((s, got - 1, "fresh" if G.pairing(c) in fresh else "relaxed"))
    if s % 20000 == 0: print(s, n, len(hits), round(time.time() - t0), flush=True)
print("contents", n, "old-rule skips", skipped, "fresh/relaxed pairings", len(hits), hits)
