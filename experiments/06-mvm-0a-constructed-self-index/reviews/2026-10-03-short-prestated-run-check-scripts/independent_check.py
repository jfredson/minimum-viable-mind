"""Independent check of the short pre-stated run of 2026-10-03.

Written by the checking session, after the run's outputs were committed. It
does not import short_prestated_run.py. It reads the committed outputs only to
compare against them. Laptop, processor only, $0.

    cd experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-scripts
    <repo>/.venv/bin/python independent_check.py > independent_check_output.txt
"""
import json
import os
import sys

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "..", "rehearsal-successor-measure", "src"))
sys.path.insert(0, SRC)
import arms as A            # noqa: E402
import grammar as G         # noqa: E402
import rehearse as RH       # noqa: E402
import repairs as R         # noqa: E402
import rerun_controls as C  # noqa: E402
import rerun_v3 as V        # noqa: E402
import training as T        # noqa: E402
import transplant as X      # noqa: E402

OUT = os.path.join(SRC, "..", "out-short-prestated-run")
dev_cpu = torch.device("cpu")
summ = json.load(open(os.path.join(C.OUT, "summary.json")))["arms"]
theirs_a = json.load(open(os.path.join(OUT, "part_a.json")))["models"]
theirs_b = json.load(open(os.path.join(OUT, "part_b.json")))["models"]

dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=dev_cpu)
fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=dev_cpu)
dev = A.to_torch(G.batch([p["recipient"] for p in dev_pairs]), dev_cpu)
recip = A.to_torch(G.batch([p["recipient"] for p in fresh_pairs]), dev_cpu)
donor = A.to_torch(G.batch([p["donor"] for p in fresh_pairs]), dev_cpu)

print("== 1. The pairs: what differs between the twins, and where")
B, S = recip["tokens"].shape
idx = torch.arange(S)[None].expand(B, -1)
fr, fd = recip["acting"].float().argmax(1), donor["acting"].float().argmax(1)
early = idx < torch.minimum(fr, fd)[:, None]
for k in sorted(recip):
    if recip[k].shape[:2] == (B, S):
        same_all = bool(torch.equal(recip[k], donor[k]))
        same_early = bool(torch.equal(recip[k][early], donor[k][early]))
        print(f"  per-position field {k!r}: identical everywhere {same_all}; identical before both first own turns {same_early}")
n = early.sum(1)
print(f"  positions before both first own turns, per pair: min {int(n.min())}, mean {float(n.float().mean()):.3f}, max {int(n.max())}")
print(f"  share of pairs where the donor's first own turn comes first: {float((fd < fr).float().mean()):.4f}")

print("== 2. Part (a) by a different route, every model")
print("  (i) twins' states identical at those positions at EVERY layer, not only the nominated one")
print("  (ii) outputs are logits at the two action positions only; their shape is printed")
print("  (iii) teeth: the same transplant with random noise added to the donor's state must change the outputs")
noise_gen = torch.Generator().manual_seed(20261003)
for arm in C.ARMS:
    for seed in C.SEEDS:
        m = V.load_model(arm, seed, dev_cpu)
        with torch.no_grad():
            clean, rs = m(recip, capture=True)
            _, ds = m(donor, capture=True)
        all_layers = all(bool(torch.equal(rs[l][early], ds[l][early])) for l in range(len(rs)))
        L = tuple(summ[f"{arm}/{seed}"]["primary"]["site_set"]["layers"])

        def patch(layer, state):
            if layer in L:
                state = torch.where(early[..., None], ds[layer], state)
            return state

        noise = torch.randn(ds[L[0]].shape, generator=noise_gen)

        def patch_shifted(layer, state):
            if layer in L:
                state = torch.where(early[..., None], ds[layer] + noise, state)
            return state

        with torch.no_grad():
            moved = m(recip, patch_fn=patch)
            shifted = m(recip, patch_fn=patch_shifted)
        ident = bool(torch.equal(clean, moved))
        d_tgt = donor["targets"][:, G.OWN]
        share = float((X.predictions(moved, G.OWN) == d_tgt).float().mean())
        t = theirs_a[f"{arm}/{seed}"]
        print(f"  {arm}/{seed}: output shape {tuple(clean.shape)} | states identical at all {len(rs)} layers {all_layers} | "
              f"own-written transplant bit-identical {ident} (theirs {t['outputs_bit_identical']}) | donor-value share "
              f"{share:.4f} (theirs {t['donor_value_share']:.4f}) | noised donor changes outputs "
              f"{not torch.equal(clean, shifted)}, largest change {float((clean - shifted).abs().max()):.3f}, own-directed actions changed "
              f"{int((X.predictions(shifted, G.OWN) != X.predictions(clean, G.OWN)).sum())} of {B}")

print("== 3. Part (b): what the ten named positions are")
rows = torch.arange(dev["tokens"].shape[0])
ap, fo = dev["action_pos"][:, G.OWN], dev["acting"].float().argmax(1)
own_marker = torch.as_tensor(R.read_labels(dev, "own"))
slot = torch.as_tensor(G.SLOT_IDS)
inv = {v: k for k, v in G.VOCAB.items()}
def describe(where):
    tok = dev["tokens"][rows, where]
    kinds = sorted({inv[int(x)] for x in tok})
    return (f"acting on {float(dev['acting'][rows, where].float().mean()):.3f} | is own marker word "
            f"{float((tok == own_marker).float().mean()):.3f} | is a value word {float(torch.isin(tok, slot).float().mean()):.3f} | "
            f"{len(kinds)} distinct tokens" + (f": {kinds}" if len(kinds) <= 4 else ""))
for k in range(5):
    print(f"  first own turn, token {k + 1}: {describe(fo + k)}")
for k in range(5, 0, -1):
    print(f"  {k} before the action: {describe(ap - k)}")
print(f"  the action position: {describe(ap)}")
span = (ap - fo + 1)
print(f"  length of the span from first own turn to action: min {int(span.min())}, mean {float(span.float().mean()):.2f}, max {int(span.max())}; "
      f"so the ten named positions are on average {10 / (float(span.float().mean()) - 1):.2f} of the other positions")

print("== 4. Part (b) recomputed with this session's own indexing, every cell")
y = R.read_labels(dev, "own")
def count(h):
    ntr = int(0.7 * len(y))
    clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:ntr], y[:ntr])
    return int((clf.predict(h[ntr:]) == y[ntr:]).sum())
bad = 0
cells = 0
for arm in C.ARMS:
    for seed in C.SEEDS:
        spec = summ[f"{arm}/{seed}"]["primary"]["site_set"]
        (l,) = spec["layers"]
        m = V.load_model(arm, seed, dev_cpu)
        with torch.no_grad():
            _, st = m(dev, capture=True)
        h = st[l].numpy()
        coef = R.load_reads(arm, "base", seed, dev_cpu)["own"][l]["coef"]
        Q = RH.basis_for(coef, spec["rank"], dev_cpu).numpy()
        t = theirs_b[f"{arm}/{seed}"]
        a, f = ap.numpy(), fo.numpy()
        r = np.arange(len(a))
        mine = {"action": (count(h[r, a]), count(h[r, a] @ Q))}
        P = spec["positions"]
        where = {}
        if P == "action+ans":
            where = {"1 before the action": a - 1}
        elif P == "action+3":
            where = {f"{k} before the action": a - k for k in (1, 2, 3)}
        elif P == "post-identity":
            where = {f"first own turn, token {k + 1} of 5": f + k for k in range(5)}
            where.update({f"{k} before the action": a - k for k in range(5, 0, -1)})
        for name, w in where.items():
            mine[name] = (count(h[r, w]), count(h[r, w] @ Q))
        if P != "action":
            lo = {"action+ans": a - 1, "action+3": a - 3, "post-identity": f}[P]
            avg = np.stack([h[i, lo[i]:a[i]].mean(0) for i in r])     # the site without the action position
            mine["mean"] = (count(avg), count(avg @ Q))
            h64 = h.astype(np.float64)
            avg64 = np.stack([h64[i, lo[i]:a[i]].mean(0) for i in r])
            print(f"    {arm}/{seed} average over the other positions, whole / piece: summed per episode in single precision "
                  f"{mine['mean']}; in double precision {(count(avg64), count(avg64 @ Q.astype(np.float64)))}; committed "
                  f"{(t['mean_over_the_other_positions']['whole'], t['mean_over_the_other_positions']['piece'])}")
        their = {"action": (t["at_the_action_position"]["whole"], t["at_the_action_position"]["piece"])}
        for e in t["other_positions"]:
            their[e["position"]] = (e["whole"], e["piece"])
        if t["mean_over_the_other_positions"]:
            their["mean"] = (t["mean_over_the_other_positions"]["whole"], t["mean_over_the_other_positions"]["piece"])
        diffs = {k: (mine[k], their.get(k)) for k in mine if mine[k] != their.get(k)}
        if set(mine) != set(their):
            diffs["keys"] = (sorted(mine), sorted(their))
        cells += len(mine)
        bad += len(diffs)
        print(f"  {arm}/{seed}: {len(mine)} cells, differing from the committed figures: {diffs if diffs else 'none'}")
print(f"  total cells {cells} (each a whole-state and a piece count), differing {bad}")

print("== 5. Part (c): the re-run's gate figure, and whether the floor was the only thing in the way")
gate = json.load(open(os.path.join(V.OUT, "gate.json")))
print(f"  F/0 named-other correct in gate.json: {gate['runs']['F/0']['other_correct']} (the control needs {C.OTHER_BAR})")
c2 = json.load(open(os.path.join(C.OUT, "summary.json")))["arms"]["F/0"].get("control2")
print(f"  the re-run's own control 2 on F/0: status {c2.get('status')!r}, reason {c2.get('reason')!r}")
pc = json.load(open(os.path.join(OUT, "part_c_NOT_A_RESULT.json")))
cand = pc["returned"]["candidates"]
print(f"  candidates with the floor off: {len(cand)}; best piece count among them {max(c['piece_correct'] for c in cand)}; "
      f"any at or above 144: {any(c['piece_correct'] >= 144 for c in cand)}")
print(f"  'status' key present in the committed output: {'status' in pc['returned']}")
print(f"  PIECE_MIN in the module after import: {C.PIECE_MIN}")
