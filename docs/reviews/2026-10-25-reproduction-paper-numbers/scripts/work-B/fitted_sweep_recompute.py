"""Recompute the fitted-position-sweep figures the paper cites from the committed per-test records."""
import json, sys, os
from scipy.stats import norm
G = sys.argv[1]
print('family bar: one-sided Bonferroni z for 0.05/135 =', round(norm.isf(0.05/135),3), ' two-sided =', round(norm.isf(0.025/135),3))
pc=[]
for s in (0,1,2):
    d = json.load(open(os.path.join(G, f'fitted_position_sweep_a3_a3_30m_seed{s}.json')))
    testable = set(d['settings']['testable_positions'])
    r = d['results']
    tests = [(k,v) for k,v in r.items() if k.split('|')[1] in testable]
    best = max(tests, key=lambda kv: kv[1]['margin_sd'])
    ctrl = [(k,v['margin_sd']) for k,v in r.items() if k.split('|')[1] not in testable]
    found = [k for k,v in tests if v['margin_sd'] >= 3.38]
    print(f'seed{s}: n testable tests {len(tests)}; best {best[0]} acc {best[1]["accuracy"]} margin {best[1]["margin_sd"]}; >=3.38: {found}')
    for k,m in sorted(ctrl, key=lambda x:-x[1]): print('    control', k, m)
