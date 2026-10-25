"""Best whole read and best piece per arm from the committed dev-10m check rows (fits). Usage: python dev_best_reads.py ROWDIR"""
import json, sys, os
d = sys.argv[1]
for a in "TCMF":
    r = json.load(open(os.path.join(d, f"row_{a}_seed0.json")))
    f = r["fits"]
    bw = max((v["whole"], k) for k, v in f.items())
    bp = max((max(v["piece"].values()), k) for k, v in f.items())
    print(a, "best whole", bw, "best piece", bp, "floor", f["0"]["band"]["floor"], "gate", r["gate"]["own_correct"], r["gate"]["other_correct"], "lesioned own", r["gate"]["lesioned_own_correct"])
