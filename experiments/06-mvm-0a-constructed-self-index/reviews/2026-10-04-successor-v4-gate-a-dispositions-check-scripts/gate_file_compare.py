"""Compare this check's independent counts with the committed gate file
out-repairs/gate_base.json (computed on the graphics chip, before the pull
request under check). Reads candidate_counts_independent.json."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
g = json.load(open(os.path.join(H, "../../../rehearsal-successor-measure/out-repairs/gate_base.json")))
mine = json.load(open(os.path.join(H, "candidate_counts_independent.json")))["models"]
print("gate file keys:", sorted(g["runs"]))
bad = 0
for key, r in sorted(g["runs"].items()):
    arm, _, seed = key.split("/")
    m = mine.get(f"{arm}/{seed}")
    if m is None:
        print(key, "not in this check"); continue
    rows = [("own_correct", r.get("own_correct"), m["channel_on"]["own"]["correct"]),
            ("other_correct", r.get("other_correct"), m["channel_on"]["other"]["correct"])]
    if "lesioned_own" in r:
        rows.append(("lesioned_own x n", round(r["lesioned_own"] * r["n"]), m["channel_zeroed"]["own"]["correct"]))
    if "lesioned_other" in r:
        rows.append(("lesioned_other x n", round(r["lesioned_other"] * r["n"]), m["channel_zeroed"]["other"]["correct"]))
    for nm, a, b in rows:
        ok = a == b
        bad += not ok
        print(f"{key:12s} {nm:20s} gate file {a}  this check {b}  {'same' if ok else 'DIFFERENT'}")
print("differing:", bad)
