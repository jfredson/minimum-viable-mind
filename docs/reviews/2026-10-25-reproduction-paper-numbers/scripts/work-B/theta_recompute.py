"""Recompute the locked thresholds from the committed A3 null-calibration record using the committed summarize()."""
import json, sys, os
E = sys.argv[1]
sys.path.insert(0, os.path.join(E, 'src'))
import null_calibration_a3 as NC
rec = json.load(open(os.path.join(E, 'null-calibration/a3_pilot_seed0.json')))
# recompute d from raw acc + ceilings, then summarise with the committed function
ceil = rec['ceilings_used']; base = rec['baseline']
bad = 0
for x in rec['draws']:
    for b in base:
        if rec['floor'][b]: continue
        dd = round((base[b]-x['acc'][b])/(base[b]-ceil[b]), 4)
        if abs(dd - x['d'][b]) > 1e-4: bad += 1
print('draws', len(rec['draws']), 'd mismatches vs recomputed:', bad)
s = NC.summarize(rec)
print(json.dumps(s['theta'], indent=0)); print(json.dumps(s['delta']))
