"""Reference only, not a pre-stated case: the in-use check on every committed
toy model, unchanged (learned sharpness). $0, processor."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tests"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "src"))
import inuse_cases as K, grammar as G, models as M, procedure as P
pairs = G.make_pairs(*G.EVAL_SETS["gate"][:2], pool=G.EVAL_SETS["gate"][2], collide=G.EVAL_SETS["gate"][3])
b = M.to_torch(G.batch(G.episodes_from_pairs(pairs)), "cpu")
out = {}
for arm in "TCMF":
    for s in range(3):
        r = P.route_in_use(K.toy(arm, s), arm, b)
        out[f"{arm}/{s}"] = dict(state=r["state"], sharpness=r["sharpness"], weight=r["weight_on_true_agent"],
                                 route_use={k: v["route_use"] for k, v in r["routes"].items()})
        print(arm, s, r["state"], round(r["sharpness"], 3), round(r["weight_on_true_agent"], 3),
              {k: round(v["route_use"], 3) for k, v in r["routes"].items()}, flush=True)
json.dump(out, open(os.path.join(HERE, "committed_toy_reference.json"), "w"), indent=1)
