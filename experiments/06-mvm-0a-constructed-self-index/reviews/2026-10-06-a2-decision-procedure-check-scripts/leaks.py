"""Point 2: for every seed MY rules withhold that has a computed figure, list
every place that figure (full precision, or 4 places) appears in summary.json
and table.md, with its JSON path or table cell, so coincidences can be told
apart from leaks by where they sit."""
import copy, json, os, sys
sys.argv = [sys.argv[0]]
import recompute as R
OUTD = os.path.join(R.EXP, "out-a2-cases")

def walk(x, path=""):
    if isinstance(x, dict):
        for k, v in x.items(): yield from walk(v, f"{path}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from walk(v, f"{path}[{i}]")
    else: yield path, x

toy, _ = R.load()
bad = 0
for case in R.K.CASES:
    rows = copy.deepcopy(toy); case["build"](rows)
    d = os.path.join(OUTD, case["name"])
    summ = json.load(open(os.path.join(d, "summary.json")))
    raw = open(os.path.join(d, "summary.json")).read()
    tab = open(os.path.join(d, "table.md")).read().splitlines()
    if "arithmetic_withheld" in raw or "arithmetic_withheld" in "\n".join(tab):
        print(case["name"], "FIELD arithmetic_withheld PRESENT"); bad += 1
    for a in "TCMF":
        st = R.arm_state(a, rows)
        if st is None: continue
        for s, why in st["reasons"].items():
            if not why: continue
            r = rows[(a, s)]["primary"].get("reading")
            if r is None: continue
            x = r["degree"]
            # summary.json: any value equal to x at a path naming this arm and seed's reading
            hits = [p for p, v in walk(summ) if isinstance(v, (int, float)) and not isinstance(v, bool)
                    and abs(v - x) < 1e-12]
            sus = [p for p in hits if (f".{a}." in p or f"arm_{a}" in p) and (f".{s}" in p) and ("reading" in p or "degree" in p)]
            # table.md: this seed's row, reading column (2nd cell)
            row = [l for l in tab if l.startswith(f"| {a}/{s} |")]
            cell = row[0].split("|")[2].strip() if row else "(no row)"
            leak_t = cell == f"{x:.4f}" or cell == repr(x)
            if sus or leak_t: bad += 1
            print(f"{case['name']:28s} {a}/{s} figure={x!r:22} summary hits={len(hits):2d} at this seed's reading={sus} table cell='{cell[:40]}'")
print("LEAKS:", bad)
