"""Recompute paper Table 2 (Amendment A3 endpoint, three seeds) from the committed per-evaluation-seed records.

Reads experiments/06-mvm-0a-constructed-self-index/a3-gates/{endpoint_validation_pilot,endpoint_a3_30m_seed1,endpoint_a3_30m_seed2}.json
and recomputes, from the six per-evaluation-seed rows in each, the means, standard deviations and the
ceiling-corrected drop, then compares with the paper's table (hand-copied below) and with the ratios to theta.
Usage: python recompute_table2.py REPO_ROOT
"""
import json, statistics, sys
from pathlib import Path
repo = Path(sys.argv[1]); g = repo/"experiments/06-mvm-0a-constructed-self-index/a3-gates"
CEIL = 0.2921; THETA = 0.1777; THETA_STATE = 0.1172
paper = {  # name: (intact mean, sd, lesioned mean, sd, corrected drop, sd, x theta, state drop, syntax drop, T_other intact, sd)
 "pilot (seed 0)": (0.5683,0.0076,0.1988,0.0173,1.337,0.057,7.5,0.0018,0.0,0.2877,0.0302),
 "seed 1":         (0.5633,0.0316,0.2015,0.0215,1.342,0.103,7.6,0.0002,0.0,0.3057,0.0281),
 "seed 2":         (0.5738,0.0284,0.1447,0.0127,1.528,0.068,8.6,0.0769,0.0,0.3195,0.0150),
}
files = {"pilot (seed 0)":"endpoint_validation_pilot.json","seed 1":"endpoint_a3_30m_seed1.json","seed 2":"endpoint_a3_30m_seed2.json"}
def r(x, n=4): return round(x, n)
bad = 0
for name, f in files.items():
    d = json.loads((g/f).read_text())
    rows = d["per_seed"]
    assert len(rows) == 6 and d["eval_n"] == 800
    ia = [x["intact"]["T_act"] for x in rows]; la = [x["lesioned"]["T_act"] for x in rows]
    dd = [(i-l)/(i-CEIL) for i, l in zip(ia, la)]
    io = [x["intact"]["T_other"] for x in rows]
    st = [(x["intact"]["T_state"]-x["lesioned"]["T_state"])/(x["intact"]["T_state"]-d["ceilings_used"]["T_state"]) for x in rows]
    sx = [x["intact"]["T_syntax"]-x["lesioned"]["T_syntax"] for x in rows]
    mine = (statistics.mean(ia), statistics.stdev(ia), statistics.mean(la), statistics.stdev(la), statistics.mean(dd), statistics.stdev(dd),
            statistics.mean(dd)/THETA, statistics.mean(st), statistics.mean(sx), statistics.mean(io), statistics.stdev(io))
    p = paper[name]
    tol = (5e-4,5e-4,5e-4,5e-4,2e-3,2e-3,0.06,6e-4,1e-9,5e-4,5e-4)
    labels = ("T_act intact","sd","T_act lesioned","sd","corrected drop","sd","x theta","state drop","syntax drop","T_other intact","sd")
    print("==", name)
    for lab, m, pp, t in zip(labels, mine, p, tol):
        ok = abs(m-pp) <= t
        bad += (not ok)
        print(("  OK     " if ok else "  DIFFER "), f"{lab:15} recomputed {m:.4f}  paper {pp}")
    print("   stored across_seeds in the file:", {k: d["across_seeds"]["T_act"][k]["mean"] for k in ("intact","lesioned","d")},
          "state d", d["across_seeds"]["T_state"]["d"]["mean"], "| default-draw d", d["default_seed"]["d"]["T_act"],
          "intact/lesioned", d["default_seed"]["intact"]["T_act"], d["default_seed"]["lesioned"]["T_act"])
print("cells differing:", bad)
print("state theta check: seed 2 state drop 0.0769 inside", THETA_STATE, "; ratio vs seed 0/1:", round(0.0769/0.0018,1), round(0.0769/0.0002,1))
e = json.loads((g/"eval_noise_a3.json").read_text())["per_size"]["400"]["batteries"]["T_act"]
print("evaluation noise, 12 draws at 400 episodes: sd", e["sd"], "range", e["range"], "(paper: sd 0.0284, range 0.079)")
