"""Finding 9: the fast comparison and rules S and D recomputed from the alarm's committed state file, by own arithmetic."""
import json, sys
s = json.load(open(sys.argv[1])); R, M = s["readings"], s["machines"]
b0, t0 = R[0]["balance"], R[0]["t"]
for i, r in enumerate(R):
    t = r["t"]; exp = 0.01 * (t - t0) / 3600
    for m in M.values():
        a, e = max(t0, m["created"]), min(t, m["gone"])
        if e > a: exp += m["rate"] * (e - a) / 3600
    dr = b0 - r["balance"]
    print(i, r.get("source"), f"{(t - t0) / 60:.1f} min; drawn {dr:.4f}; predicted {exp:.4f}; ratio",
          round(dr / exp, 3) if exp > 0 else None,
          "| over rule S line" if exp >= 0.25 and dr >= 1.25 * exp + 0.05 else "",
          "| over rule D line" if exp >= 0.10 and dr >= 1.25 * exp + 0.02 else "")
for m in M.values():
    print(m["pod"], m["out"], f"existed {(m['gone'] - m['created']) / 3600:.4f} h at ${m['rate']}", "recorded by", m["gone_by"], "inferred" if m["gone_inferred"] else "not inferred")
