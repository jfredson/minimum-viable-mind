"""Recompute the 'one episode in 27' and 'one in 11' sensitivity figures from the committed fitted-sweep records."""
import json, sys, os, statistics as st
G = sys.argv[1]
for s in (0,1,2):
    d = json.load(open(os.path.join(G, f'fitted_position_sweep_a3_a3_30m_seed{s}.json')))
    testable = set(d['settings']['testable_positions']); r = d['results']
    sh = [v['smallest_detectable_share_vs_no_information'] for k,v in r.items() if k.split('|')[1] in testable]
    need = [v['accuracy_needed_for_bar'] for k,v in r.items() if k.split('|')[1] in testable]
    ceil = [v['accuracy'] for k,v in r.items() if k.split('|')[1]=='own_revision_marker']
    c_lo, c_hi = min(ceil), max(ceil)
    m = st.median(need)
    print(f'seed{s}: share vs no-info median {st.median(sh):.4f} (1 in {1/st.median(sh):.1f}); ceiling range {c_lo}-{c_hi}; '
          f'recalibrated share (need-0.25)/(ceil-0.25): {(m-0.25)/(c_hi-0.25):.4f}-{(m-0.25)/(c_lo-0.25):.4f} -> 1 in {(c_hi-0.25)/(m-0.25):.1f} to {(c_lo-0.25)/(m-0.25):.1f}')
