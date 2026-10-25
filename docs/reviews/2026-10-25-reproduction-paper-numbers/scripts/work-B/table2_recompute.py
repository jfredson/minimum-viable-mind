"""Recompute Table 2 of the paper from the per-evaluation-seed records committed in a3-gates/."""
import json, statistics as st, sys, os
G = sys.argv[1]
CEIL = {'T_act':0.2921,'T_state':0.06761742424242424,'T_syntax':0.08333333333333331}
TH = 0.1777
files = {'pilot (seed 0)':'endpoint_validation_pilot.json','seed 1':'endpoint_a3_30m_seed1.json','seed 2':'endpoint_a3_30m_seed2.json','ctl pilot':'endpoint_a3ctl_30m_seed0.json'}
for name,f in files.items():
    d = json.load(open(os.path.join(G,f)))
    ps = d['per_seed']
    print(f'== {name}  ({f}) eval seeds: {[p["seed"] for p in ps]}  n_eval={d["eval_n"]}')
    for b in ['T_act','T_other','T_state','T_syntax']:
        it=[p['intact'][b] for p in ps]; le=[p['lesioned'][b] for p in ps]
        line=f'  {b}: intact {st.mean(it):.4f} (sd {st.stdev(it):.4f})  lesioned {st.mean(le):.4f} (sd {st.stdev(le):.4f})'
        if b in CEIL:
            dd=[(i-l)/(i-CEIL[b]) for i,l in zip(it,le)]
            line+=f'  d mean {st.mean(dd):.4f} (sd {st.stdev(dd):.4f})  committed d per seed {[p["d"][b] for p in ps]}'
            if b=='T_act': line+=f'  d/theta {st.mean(dd)/TH:.2f}x'
        print(line)
    print('  committed across_seeds T_act d:', d['across_seeds']['T_act']['d'], ' T_state d:', d['across_seeds']['T_state']['d']['mean'])
