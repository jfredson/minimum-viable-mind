# The candidate seventh failure, run on version 2: for each pre-stated line, evaluate it
# exactly as the proposal words it, on the committed toy outputs at e0626b2, and say
# whether the path the design expects can produce what the line needs.
import json, sys
base = sys.argv[1]
M = {}
for f in ('measure_base_T_C.json', 'measure_base_F.json', 'measure_base_M.json'):
    M.update(json.load(open(base + f))['arms'])
G = json.load(open(base + 'gate_base.json'))
ROOM = 0.0175
key = lambda a, s: f'{a}/base/{s}'

print('1. Holding controls (section 7.3): control 7 bit-identical; control 3 <= untouched + 0.0175;'
      ' control 1 on arm T <= untouched + 0.0175. A failure means no reading for that arm.')
for a in 'TCFM':
    for s in '012':
        r = M[key(a, s)]; c = r['controls']; u = r['accuracy_untouched']
        c7 = c['7 null transplant leaves every logit bit-identical']
        c3 = c['3 matched random subspace, same rank']
        c1 = c['1 content transplant (the complement subspace)']
        ok = c7 and c3 <= u + ROOM and (a != 'T' or c1 <= u + ROOM)
        flag = '' if ok else '   <-- a holding control fails: no reading'
        print(f'   {a}{s}: control 3 {c3:.4f} vs limit {u + ROOM:.4f}; control 7 {c7}; reading made: {ok}{flag}')

print('2. Arm M pass line (section 5.3): 0.3 <= reading <= 0.7 on EVERY seed, with holding controls applied.')
vals = []
for s in '012':
    r = M[key('M', s)]; c = r['controls']; u = r['accuracy_untouched']
    made = c['3 matched random subspace, same rank'] <= u + ROOM
    vals.append(r['reading']['degree'] if made else None)
print(f'   readings made: {vals} -> pass on every seed: {all(v is not None and 0.3 <= v <= 0.7 for v in vals)}')

print('3. R1 needs every arm carried to pass the learn-both gate (section 3); the toy gate:')
for a in 'TCFM':
    v = G['verdicts'][f'{a}/base']
    print(f'   arm {a}: named-other clears on {v["other_seeds_clearing"]} of 3, own on {v["own_seeds_clearing"]} of 3,'
          f' learn-both {v["learn_both"]}')

print('4. The rider (section 7.2 item 7): a reading at arm T\'s site set for every arm and seed.')
for a in 'CFM':
    st = [M[key(a, s)]['rider_at_arm_T_site_set']['reading']['status'] for s in '012']
    wh = [round(M[key(a, s)]['rider_at_arm_T_site_set']['reading']['accuracy_whole'], 4) for s in '012']
    print(f'   arm {a}: {st}; whole-state at that site {wh}')

print('5. The lesion description (section 8.2): "all three collapse" (arms T, C, M) on the toy.')
for a in 'TCM':
    print(f'   arm {a}:', [G['runs'][key(a, s)]['lesion_collapses_own'] for s in '012'],
          [round(G['runs'][key(a, s)]['lesioned_own'], 4) for s in '012'])

print('6. The wager (section 12.8): at least $16 left of $450.')
spent, note_split, ruled_split = 228.15, 161.90, 44 + 84.06 + 12 + 23
for label, both in (('note split, as the proposal carries it', note_split), ('ruled split', ruled_split)):
    for m in (32, 44):
        left = 450 - spent - both - m
        print(f'   {label}, arm M ${m}: left ${left:.2f}  meets $16: {left >= 16}')
