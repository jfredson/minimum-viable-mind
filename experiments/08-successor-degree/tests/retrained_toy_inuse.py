"""The retrained toy built models (sharpness fixed at 4.0): learning gate
counts and the in-use check, beside the committed toy models' figures
(method `docs/2026-10-06-sharpness-fix-inuse-check-method.md`, section 4,
concerns 1 and 2). Processor, $0.

    python tests/retrained_toy_inuse.py --models DIR --out FILE.json [--seeds 0,1,2]
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))
sys.path.insert(0, HERE)
import grammar as G        # noqa: E402
import models as M         # noqa: E402
import procedure as P      # noqa: E402
import inuse_cases as K    # noqa: E402

COMMITTED_ROWS = os.path.join(HERE, "..", "out-freeze-tests", "t3b-fresh-fit")

ap = argparse.ArgumentParser()
ap.add_argument("--models", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--seeds", default="0,1,2")
a = ap.parse_args()
pairs = G.make_pairs(*G.EVAL_SETS["gate"][:2], pool=G.EVAL_SETS["gate"][2], collide=G.EVAL_SETS["gate"][3])
b = M.to_torch(G.batch(G.episodes_from_pairs(pairs)), "cpu")
out = {}
for s in [int(x) for x in a.seeds.split(",")]:
    for arm in "TCM":
        p = os.path.join(a.models, f"ckpt_{arm}_fixed_seed{s}.pt")
        if not os.path.exists(p):
            print(arm, s, "not trained yet"); continue
        m, _ = P.load_model(p, None, None)
        own, oth, n = P._accuracy(m, b)
        r = P.route_in_use(m, arm, b)
        old = json.load(open(os.path.join(COMMITTED_ROWS, f"row_{arm}_seed{s}.json")))["gate"]
        ref = P.route_in_use(K.toy(arm, s), arm, b)
        out[f"{arm}/{s}"] = dict(
            retrained=dict(own_correct=own, other_correct=oth, sharpness=r["sharpness"],
                           weight=r["weight_on_true_agent"], state=r["state"],
                           route_use={k: v["route_use"] for k, v in r["routes"].items()},
                           right_with_true_answer={k: v["right_with_true_answer"] for k, v in r["routes"].items()}),
            committed=dict(own_correct=old["own_correct"], other_correct=old["other_correct"],
                           sharpness=ref["sharpness"], weight=ref["weight_on_true_agent"], state=ref["state"],
                           route_use={k: v["route_use"] for k, v in ref["routes"].items()}))
        R, C = out[f"{arm}/{s}"]["retrained"], out[f"{arm}/{s}"]["committed"]
        print(f"{arm}/{s}: own {C['own_correct']} -> {R['own_correct']}, named-other {C['other_correct']} -> "
              f"{R['other_correct']}; sharpness {C['sharpness']:.2f} -> {R['sharpness']:.2f}; weight "
              f"{C['weight']:.3f} -> {R['weight']:.3f}; route use "
              f"{ {k: round(v, 3) for k, v in C['route_use'].items()} } -> "
              f"{ {k: round(v, 3) for k, v in R['route_use'].items()} }; check {C['state']} -> {R['state']}",
              flush=True)
json.dump(out, open(a.out, "w"), indent=1)
