"""Does the training stream ever draw one of the 1,380 development episodes
the reads' set added on 2026-10-08? If not, adding them to the exclusion list
changes no training step.

Replays exactly what `grammar.TrainingStream.pairs_for_step` draws for a run
seed over the registered 108,919 steps of 48 pairs, under the exclusion as it
stood BEFORE the change (every other evaluation set and the fresh and relaxed
pairings), without rendering, and counts drawn contents that are one of the
1,380. Generator only; no model. Laptop, $0. Method:
`docs/2026-10-09-ruled-code-changes-and-page4-rerun-method.md`, section 2.

    python tests/replay_stream_dev_reads.py SEED
"""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import numpy as np      # noqa: E402
import grammar as G     # noqa: E402

seed = int(sys.argv[1])
extra = {G.fingerprint(p["content"]) for p in G.eval_pairs("dev_reads")[600:]}
old_excl = set()
for name in G.EVAL_SETS:
    if name != "dev_reads":
        old_excl |= {G.fingerprint(p["content"]) for p in G.eval_pairs(name)}
held = G.held_out_pairings()
assert len(extra) == 1380 and not (extra & old_excl)
STEPS, NP = 108919, 48
n = skipped = 0
hits = []
t0 = time.time()
for s in range(1, STEPS + 1):
    rng = np.random.default_rng([1000 + seed, s])
    got = 0
    while got < NP:
        c = G._content(rng, "train", False)
        f = G.fingerprint(c)
        if f in old_excl or G.pairing(c) in held:
            skipped += 1
            continue
        rng.choice(G.eligible_models(c), size=2, replace=False)
        got += 1
        n += 1
        if f in extra:
            hits.append((s, got - 1))
    if s % 20000 == 0:
        print(s, n, len(hits), round(time.time() - t0), flush=True)
print(f"seed {seed}: {n} training contents over {STEPS} steps; skipped by the old exclusion {skipped}; "
      f"drawn contents that are one of the 1,380 new development episodes: {len(hits)} {hits}")
