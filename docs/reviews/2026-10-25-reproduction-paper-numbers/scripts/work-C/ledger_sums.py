"""Recompute experiment C's ledger sums and the programme total from the
compute-ledger rows (experiments/06-mvm-0a-constructed-self-index/compute-ledger.md).
Each figure below is copied from the row or annotation named beside it."""
dev = {"M": 0.4744, "T": 0.3347, "C": 0.3341, "F": 0.3223}          # rows 105-108 (2026-10-04)
rr = {"M": 0.5045, "T": 0.3980, "C": 0.4007}                       # rows 109-111 (2026-10-09)
billed_h = {"M": 0.4239, "T": 0.3345, "C": 0.3367}                 # same rows
life_h = {"M": 25*60+25, "T": 20*60+4, "C": 20*60+12}               # run record, machine lives in s
life_h = {k: v/3600 for k, v in life_h.items()}
print("dev sum", round(sum(dev.values()), 4))
print("rerun sum", round(sum(rr.values()), 4))
print("billed hours", round(sum(billed_h.values()), 4), "x1.19 =", round(sum(billed_h.values())*1.19, 4))
for k in rr: print(" ", k, "billed*1.19", round(billed_h[k]*1.19, 4), "row", rr[k], "ratio A billed/life", round(billed_h[k]/life_h[k], 3), "life h", round(life_h[k], 4))
print("lifetimes x0.99", round(sum(life_h.values())*0.99, 4), " x1.19", round(sum(life_h.values())*1.19, 4))
print("rerun / approved 1.14:", round(sum(rr.values())/1.14, 3))
# programme chain, as the ledger's own running totals carry it
chain = [("to 2026-08-10 (6.645+1.943+97.035, the console figures)", 6.645+1.943+97.035),
 ("2026-08-15", 18.9), ("2026-08-16", 25.29), ("2026-08-17", 31.63), ("2026-09-15", 13.92),
 ("2026-09-16", 0.29), ("2026-09-17", 20.1), ("2026-09-19 control pilot (annotation ~9.9)", 9.9),
 ("2026-09-20 recovery", 0.067), ("2026-09-20 two refused runs", 1.904), ("2026-09-21 slice (settled 0.0077)", 0.0077),
 ("2026-09-25 slice attempt 1 (settled 0.5162)", 0.5162), ("2026-09-25 attempt 2", 0.0525)]
t = 0
for n, v in chain:
    t += v; print(f"  {n:60s} +{v:8.4f} -> {t:8.4f}")
t += sum(dev.values()); print("after dev runs", round(t, 4))
t += sum(rr.values()); print("after reruns", round(t, 4), "of 450")
print("from the ledger's annotated base 228.17:", round(228.17+sum(dev.values())+sum(rr.values()), 4))
print("without the 2026-10-06 settled-billing correction (base 228.15):", round(228.15+sum(dev.values())+sum(rr.values()), 4))
