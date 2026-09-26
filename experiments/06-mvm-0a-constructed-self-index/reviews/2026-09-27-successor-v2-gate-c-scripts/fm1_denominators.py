# Failure 1, run on the committed repairs outputs: the chance-corrected denominator
# (whole - untouched) per arm and seed, the floor's required room beside it, and the top
# of scale when the ownership-only transplant does nothing (ownership_only = untouched),
# under the registered form and under version 1's form.
import json, sys
base = sys.argv[1]
print('arm/seed    untouched  whole   own-acc | denominator  floor-needs | top of scale: registered  version-1')
for f in ('measure_base_T_C.json', 'measure_base_F.json', 'measure_base_M.json'):
    for k, r in sorted(json.load(open(base + f))['arms'].items()):
        rd = r['reading']
        u, w, a = rd['accuracy_untouched'], rd['accuracy_whole'], rd['arm_own_accuracy']
        den = w - u
        need = 0.8 * (a - u)
        top_reg = (w - u) / den if den else float('nan')
        top_v1 = (w - u) / w if w else float('nan')
        print(f'{k:10s}  {u:.4f}    {w:.4f}  {a:.4f} |  {den:.4f}       {need:.4f}    |  {top_reg:.4f}                  {top_v1:.4f}')
