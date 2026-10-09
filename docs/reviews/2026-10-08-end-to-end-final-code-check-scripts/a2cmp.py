import os, sys, filecmp
sys.path.insert(0, os.path.dirname(__file__))
N, O = sys.argv[1], sys.argv[2]
print("results.md identical:", filecmp.cmp(f"{N}/results.md", f"{O}/results.md", False))
print("results.json identical:", filecmp.cmp(f"{N}/results.json", f"{O}/results.json", False))
def cells(l): return len(l.rstrip('\n').strip().strip('|').split('|'))
cases = sorted(d for d in os.listdir(N) if os.path.isdir(f"{N}/{d}"))
print("case folders:", len(cases), "old:", len([d for d in os.listdir(O) if os.path.isdir(f"{O}/{d}")]))
sdiff = [f"{c}/{f}" for c in cases for f in ("summary.json", "steps.json")
         if (os.path.exists(f"{N}/{c}/{f}") or os.path.exists(f"{O}/{c}/{f}")) and not filecmp.cmp(f"{N}/{c}/{f}", f"{O}/{c}/{f}", False)]
print("summary/steps differing:", sdiff)
rowdiff = [f"{c}/{f}" for c in cases for f in os.listdir(f"{N}/{c}") if f.startswith("row_") and not filecmp.cmp(f"{N}/{c}/{f}", f"{O}/{c}/{f}", False)]
print("row files differing:", rowdiff)
total = 0; allok = True; mism = 0
for c in cases:
    a = open(f"{O}/{c}/table.md").readlines(); b = open(f"{N}/{c}/table.md").readlines()
    if len(a) != len(b): allok = False
    for x, y in zip(a, b):
        if x != y:
            total += 1
            if not (x.replace('| withheld ', '', 1) == y): allok = False
    rows = [l for l in b if l.startswith('|')]
    mism += sum(cells(l) != cells(rows[0]) for l in rows)
print("table lines changed:", total, "each exactly one withheld cell dropped:", allok, "rows whose cell count differs from header:", mism)
