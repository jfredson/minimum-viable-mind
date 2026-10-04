"""Checking session, 2026-10-03. Two things, no model loaded, $0.

1. Compare the committed outputs of the controls re-run (a copy set aside
   before the re-run overwrote the folder) with what this session's re-run of
   the committed script produced, value by value.
2. Recompute, from the committed output files, each figure the findings
   (docs/2026-10-03-controls-rerun.md) state in prose.

    python compare_and_verify.py <folder of the committed copy> <folder this session's run wrote>
"""
import json
import os
import sys

OLD, NEW = sys.argv[1], sys.argv[2]


def walk(a, b, path, diffs):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                diffs.append((path + "/" + k, "present in one only", ""))
            else:
                walk(a[k], b[k], path + "/" + k, diffs)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            diffs.append((path, f"length {len(a)}", f"length {len(b)}"))
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                walk(x, y, f"{path}[{i}]", diffs)
    elif a != b:
        diffs.append((path, a, b))


print("== 1. committed outputs against this session's re-run")
files = sorted(f for f in os.listdir(OLD))
print(f"files in the committed copy: {len(files)}; in this run's folder: {len(os.listdir(NEW))}; "
      f"same names: {files == sorted(os.listdir(NEW))}")
total_values, all_diffs = 0, []
for f in files:
    if f.endswith(".json"):
        a, b = json.load(open(os.path.join(OLD, f))), json.load(open(os.path.join(NEW, f)))
        d = []
        walk(a, b, f, d)
        total_values += len(json.dumps(a).split(","))
        all_diffs += d
    else:
        same = open(os.path.join(OLD, f)).read() == open(os.path.join(NEW, f)).read()
        print(f"{f}: byte-identical {same}")
        if not same:
            all_diffs.append((f, "text differs", ""))
timing = [d for d in all_diffs if d[0].endswith("/seconds")]
real = [d for d in all_diffs if not d[0].endswith("/seconds")]
print(f"json values compared (approximate count): {total_values}")
print(f"differences other than the run's own wall-clock time: {len(real)}")
for p, x, y in real[:200]:
    print(f"  {p}: committed {x!r} | this run {y!r}")
for p, x, y in timing:
    print(f"  (wall-clock) {p}: committed {x:.0f}s | this run {y:.0f}s")

print("\n== 2. the findings' prose figures, recomputed from the committed output files")
S = json.load(open(os.path.join(OLD, "summary.json")))
arms = S["arms"]
keys = [f"{a}/{s}" for a in "TCFM" for s in (0, 1, 2)]
N = {k: json.load(open(os.path.join(OLD, f"nominate_{k[0]}_seed{k[2]}.json"))) for k in keys}

print("section 1/2: readings:", {k: arms[k]["primary"]["reading"]["degree"] for k in keys})
print("section 1: described only:", {k: arms[k]["primary"]["described_only"] for k in keys})
print("section 1: separation:", S["separation"])
print("section 1/3: arm F, best piece at any layer and size, of 180:",
      {k: max(v for l in N[k]["fits"].values() for v in l["piece"].values()) for k in keys if k[0] == "F"})
print("section 3: arm F, whole read by layer:", {k: [N[k]["fits"][l]["whole"] for l in sorted(N[k]["fits"])] for k in keys if k[0] == "F"})
print("section 3: C/1 candidates:")
for c in N["C/1"]["candidates"]:
    print("   ", c)
print("section 3: C/1 primary:", N["C/1"]["primary"])
print("section 4: control 7, primary:", sum(arms[k]["primary"]["controls"]["7"]["bit_identical"] for k in keys), "of",
      len(keys), "| stricter rows present:", sum("stricter" in arms[k] for k in keys), ", identical:",
      sum(arms[k]["stricter"]["controls"]["7"]["bit_identical"] for k in keys if "stricter" in arms[k]),
      "| described-only primaries:", sum(arms[k]["primary"]["described_only"] for k in keys))
miss = {k: arms[k]["primary"]["no_transplant"]["miss"] for k in keys}
print("section 4: no-transplant rule, inside allowance:", sum(arms[k]["primary"]["no_transplant"]["inside_allowance"] for k in keys),
      "of 12 | largest miss:", max(miss.items(), key=lambda kv: abs(kv[1])))
print("section 4: control 1:", {k: round(arms[k]["primary"]["controls"]["1"]["complement_donor_share"], 4) for k in keys})
print("section 4: control 3 below/equal/above:", {k: tuple(arms[k]["primary"]["controls"]["3"][x] for x in ("below", "equal", "above")) for k in keys})
print("section 4: control 6 same moved:", {k: arms[k]["primary"]["controls"]["6"]["same_value_moved"] and round(arms[k]["primary"]["controls"]["6"]["same_value_moved"], 4) for k in keys})
print("section 4: true slot:", {k: (round(arms[k]["primary"]["true_slot"]["reading"]["degree"], 4),
                                    round(arms[k]["primary"]["true_slot"].get("route_formula", float("nan")), 4),
                                    round(abs(arms[k]["primary"]["reading"]["degree"] - arms[k]["primary"]["true_slot"]["reading"]["degree"]), 4))
                                for k in keys if "true_slot" in arms[k]["primary"]})
print("section 4: rider:", {k: (arms[k]["rider_at_arm_T_site_set"]["reading"]["degree"],
                                round(arms[k]["rider_at_arm_T_site_set"]["reading"]["accuracy_whole"], 4),
                                round(arms[k]["primary"]["reading"]["accuracy_untouched"], 4)) for k in keys})
print("section 4: stricter row site sets and readings:")
for k in keys:
    st = arms[k].get("stricter")
    p = arms[k]["primary"]
    print("   ", k, "none" if not st else (st["site_set"]["layers"], st["site_set"]["positions"], st["site_set"]["rank"], st["reading"]["degree"]),
          "| same site as primary:", bool(st) and st["site_set"] == p["site_set"],
          "| nomination's stricter status:", N[k]["stricter"]["status"])
print("section 4: whole-state floor on fresh episodes clears:", sum(arms[k]["primary"]["reading"]["floor"]["clears"] for k in keys), "of 12")
c2 = arms["F/0"]["control2"]
print("section 5: F/0 control 2:", {x: c2[x] for x in ("status", "reason", "named_other_correct", "dev_named_other_accuracy", "dev_untouched")})
for l in sorted(c2["named_read_fits"]):
    f = c2["named_read_fits"][l]
    print(f"    layer {l}: {f['whole']} | " + " / ".join(str(f["piece"][r]) for r in ("1", "2", "4", "8")))
print("section 5: control 2 on the rest:", {k: (arms[k]["control2"]["status"], arms[k]["control2"].get("named_other_correct")) for k in keys if k != "F/0"})
print("section 6: control 4 above no transplant:", {k: round(arms[k]["primary"]["controls"]["4"]["above_untouched"], 4) for k in keys})
print("section 6: site sets:", {k: (arms[k]["primary"]["site_set"]["layers"], arms[k]["primary"]["site_set"]["positions"]) for k in keys})
