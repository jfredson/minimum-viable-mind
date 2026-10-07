"""The in-use check's made-up cases on real models (method
`docs/2026-10-06-sharpness-fix-inuse-check-method.md`, section 3, cases 1 to
13; expectations written there before this ran). Committed toy models
(checked against SHA256SUMS) with named weights changed, and the real
10-million-parameter development checkpoints on the laptop.

    python tests/inuse_cases.py --out DIR

Laptop processor, $0. Writes DIR/inuse_cases.json and prints a table.
"""
import argparse
import hashlib
import json
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))
import grammar as G      # noqa: E402
import models as M       # noqa: E402
import measure as MS     # noqa: E402
import procedure as P    # noqa: E402

REH = os.path.abspath(os.path.join(HERE, "..", "..", "rehearsal-successor-measure", "out-repairs", "models"))
TEN = os.path.expanduser("~/Code/minimum-viable-mind/experiments/08-successor-degree/artifacts")
WANT = dict(reversed(line.split()) for line in open(os.path.join(REH, "SHA256SUMS")))


def toy(arm, seed):
    p = os.path.join(REH, f"ckpt_{arm}_base_seed{seed}.pt")
    assert hashlib.sha256(open(p, "rb").read()).hexdigest() == WANT[os.path.basename(p)], p
    m = M.build(arm, "toy")
    m.load_state_dict(torch.load(p, map_location="cpu"), strict=True)
    return m.eval()


def ten(arm):
    p = os.path.join(TEN, f"succ_{arm.lower()}_10m_seed0", f"succ_{arm.lower()}_10m_seed0.pt")
    m, _ = P.load_model(p, None, None)
    return m.eval(), hashlib.sha256(open(p, "rb").read()).hexdigest()


def zero(*mods):
    with torch.no_grad():
        for mod in mods:
            for prm in mod.parameters():
                prm.zero_()


def sharp(m, v):
    m.own_sharpness.data = torch.tensor(float(v))


def film(m):
    return [blk.to_scale for blk in m.blocks] + [blk.to_shift for blk in m.blocks] + [m.bind]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    pairs = G.make_pairs(G.EVAL_SETS["gate"][0], seed=G.EVAL_SETS["gate"][1],
                         pool=G.EVAL_SETS["gate"][2], collide=G.EVAL_SETS["gate"][3])
    b = M.to_torch(G.batch(G.episodes_from_pairs(pairs)), "cpu")
    assert b["tokens"].shape[0] == MS.GATE_EPISODES
    cases = []

    def run(n, about, arm, m, expect, extra=None):
        rec = P.route_in_use(m, arm, b)
        got = rec["state"]
        ok = (got == expect) if isinstance(expect, str) else (got in expect)
        cases.append(dict(case=n, about=about, arm=arm, expected=expect, got=got, matches=ok,
                          sharpness=rec["sharpness"], weight=rec["weight_on_true_agent"],
                          route_use={k: v["route_use"] for k, v in rec["routes"].items()},
                          reasons=rec["reasons"], **(extra or {})))
        print(f"{n:>3} {'ok ' if ok else 'NO '} {arm} {got:<24} w={rec['weight_on_true_agent']:.3f} "
              f"use={ {k: (None if v['route_use'] is None else round(v['route_use'], 3)) for k, v in rec['routes'].items()} } "
              f"| {about}", flush=True)
        return rec

    F_, P_, NA = MS.FAILED, MS.PASSED, MS.NOT_APPLICABLE
    run(1, "committed toy arm T seed 0, unchanged", "T", toy("T", 0), P_)
    m = toy("T", 0); sharp(m, 0.0)
    run(2, "toy arm T seed 0, sharpness set to 0 (flat)", "T", m, F_)
    m = toy("T", 0); sharp(m, -0.09)
    run(3, "toy arm T seed 0, sharpness -0.09", "T", m, F_)
    m = toy("C", 0); sharp(m, 4.0); zero(*film(m))
    rec4 = run(4, "toy arm C seed 0, sharpness 4.0, scale-and-shift and binding zeroed (route round it)", "C", m, F_)
    m = toy("T", 0); zero(m.read_own)
    run(5, "toy arm T seed 0, slot reader zeroed", "T", m, F_)
    m = toy("M", 0); sharp(m, 4.0); zero(m.read_own)
    run(6, "toy arm M seed 0, sharpness 4.0, separable slot reader zeroed", "M", m, F_)
    m = toy("M", 0); sharp(m, 4.0); zero(*film(m))
    run(7, "toy arm M seed 0, sharpness 4.0, scale-and-shift and binding zeroed", "M", m, F_)
    for s in (1, 2):
        run(8, f"committed toy arm C seed {s}, unchanged", "C", toy("C", s), F_)
    run(9, "committed toy arm F seed 0 (not judged; reference)", "F", toy("F", 0), NA)
    for arm, n in (("C", 10), ("M", 11), ("T", 12)):
        if os.path.exists(os.path.join(TEN, f"succ_{arm.lower()}_10m_seed0")):
            m, h = ten(arm)
            run(n, f"real 10-million arm {arm}", arm, m, F_ if arm != "T" else P_, dict(checkpoint_sha256=h))
        else:
            print(f"{n:>3} SKIPPED: the 10-million arm {arm} checkpoint is not on this laptop")
    torch.manual_seed(0)
    run(13, "untrained toy arm C (nothing right to lose)", "C", M.build("C", "toy").eval(),
        (MS.NOT_EVALUATED, F_))
    json.dump(dict(cases=cases, toy_sha256=WANT), open(os.path.join(a.out, "inuse_cases.json"), "w"), indent=1)
    bad = [c["case"] for c in cases if not c["matches"]]
    print(f"\n{len(cases)} checks; differ from expectation: {bad}")


if __name__ == "__main__":
    main()
