# Print, per arm, the range across seeds of every control figure and the no-transplant
# rule's miss, from the committed measure files at e0626b2.
import json, sys
base = sys.argv[1]
keys = None
by_arm = {}
for f in ('measure_base_T_C.json', 'measure_base_F.json', 'measure_base_M.json'):
    for k, r in json.load(open(base + f))['arms'].items():
        arm = k.split('/')[0]
        row = dict(r['controls'])
        row['untouched'] = r['accuracy_untouched']
        row['no-transplant miss'] = abs(r['no_transplant_rate_miss'])
        row['own accuracy fresh'] = r['arm_own_accuracy_fresh']
        by_arm.setdefault(arm, []).append(row)
for arm in 'TCFM':
    rows = by_arm[arm]
    print(f'arm {arm} ({len(rows)} seeds)')
    for key in rows[0]:
        vals = [x[key] for x in rows]
        if isinstance(vals[0], bool):
            print(f'   {key}: {vals}')
        else:
            print(f'   {key}: {min(vals):.4f} to {max(vals):.4f}   {[round(v, 4) for v in vals]}')
allmiss = [x['no-transplant miss'] for a in by_arm.values() for x in a]
print('largest no-transplant miss across all 12 pairs: %.4f' % max(allmiss))
