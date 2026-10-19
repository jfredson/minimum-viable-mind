#!/usr/bin/env python3
"""Check 1, ledger part. For each 2026-10-04 and 2026-10-09 row of the compute
ledger, print the run name the row is for (`succ_<arm>_10m_seed0`, first one in
the row) and the per-run actual the row gives ("$X by arithmetic" for the
2026-10-04 rows, "$X from the vendor's own bill" for the 2026-10-09 rows), then
the sums, then the same figures rounded to cents. What the new text carries:
$1.47 = $0.47 / $0.34 / $0.33 / $0.33 for arms M, T, C, F; $1.3032 = $0.5045 /
$0.3980 / $0.4007 for arms M, T, C. A cent that differs prints DIFFERS."""
import re
carried = {"2026-10-04": {"m": "0.47", "t": "0.34", "c": "0.33", "f": "0.33"},
           "2026-10-09": {"m": "0.5045", "t": "0.3980", "c": "0.4007"}}
rows = [l for l in open("experiments/06-mvm-0a-constructed-self-index/compute-ledger.md", encoding="utf-8")
        if re.match(r"\| 2026-10-0[49] \|", l)]
tot = {}
for l in rows:
    date = l[2:12]
    run = re.search(r"`succ_([tcmf])_10m_seed0(?:_rerun)?`", l)
    actual = re.search(r"\$([0-9.]+) (by arithmetic|from the vendor's own bill)", l)
    arm = run.group(1) if run else "?"
    val = actual.group(1) if actual else None
    want = carried[date].get(arm)
    shown = val if date == "2026-10-09" else f"{float(val):.2f}"
    flag = "matches" if want == shown else "DIFFERS"
    print(f"{date} succ_{arm}_10m_seed0  ledger ${val} ({actual.group(2)})  carried ${want}  ledger rounded ${shown}  {flag}")
    tot[date] = tot.get(date, 0) + float(val)
for d, v in tot.items(): print("sum", d, f"${v:.4f}")
