"""Check of proposal version 4: recompute the toy figures it quotes from the
committed output files, and print each beside what version 4 prints.

Run from the root of the checkout:
    .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/toy_figures.py

Reads only committed files. Trains nothing, loads no model, spends nothing.
"""
import json

R = 'experiments/rehearsal-successor-measure/'
O = R + 'out-controls-rerun/'
S = R + 'out-short-prestated-run/'
ARMS, SEEDS = 'TCMF', '012'
bad = []


def J(p):
    return json.load(open(p))


def show(label, v4, got, tol=0.00011):
    """v4 and got are lists. Numbers are compared to within tol (version 4
    prints four decimals, and a share such as 0.05125 can round either way);
    everything else must be equal."""
    num = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)
    ok = len(v4) == len(got) and all(
        abs(a - b) <= tol if num(a) and num(b) else a == b for a, b in zip(v4, got))
    print(f"{'MATCH ' if ok else 'DIFFER'} | {label}\n         version 4: {v4}\n         files:     {got}")
    if not ok:
        bad.append(label)


M = {a: [J(f'{O}measure_{a}_seed{s}.json') for s in SEEDS] for a in ARMS}
N = {a: [J(f'{O}nominate_{a}_seed{s}.json') for s in SEEDS] for a in ARMS}
SUM = J(O + 'summary.json')
r4 = lambda x: round(x, 4)

print('=== 1. Readings (sections 3, 5.1 to 5.3, 9, 10)')
deg = {a: [m['primary']['reading']['degree'] for m in M[a]] for a in ARMS}
show('arm T reading, every seed', [0.0, 0.0, 0.0], [r4(x) for x in deg['T']])
show('arm C reading', [1.0051, 0.9926, 0.9974], [r4(x) for x in deg['C']])
show('arm M reading', [0.4886, 0.4860, 0.5449], [r4(x) for x in deg['M']])
show('arm F is described only, no reading', [True, True, True], [m['primary']['described_only'] for m in M['F']])
show('arm F, the number the arithmetic would have returned (section 5.4)', [1.0, 1.0, 1.0108], [r4(x) for x in deg['F']])
show('arm F nomination status, every seed',
     ["read failed its floor: no size's piece reaches four fifths"] * 3, [n['primary']['status'] for n in N['F']])

print('\n=== 2. The separation (sections 3, 9; the packet page 6; record B ruling 6)')
print('    summary.json, field separation (paired by seed number):',
      {k: r4(v['C_minus_T']) for k, v in SUM['separation'].items()})
show('lowest arm C reading minus highest arm T reading', [0.9926], [r4(min(deg['C']) - max(deg['T']))])

print('\n=== 3. Arm C table (section 5.2) and the sites of arms T and M')
exp_C = [([2], 'action', 8, 180, 180, 0.5400, 0.0488, 0.0512),
         ([1], 'action+3', 8, 177, 172, 0.5550, 0.0525, 0.0488),
         ([1], 'post-identity', 4, 176, 150, 0.5463, 0.0612, 0.0600)]
for s, e in enumerate(exp_C):
    ss, rd = M['C'][s]['primary']['site_set'], M['C'][s]['primary']['reading']
    show(f'arm C seed {s}: layers, positions, size, whole read, piece, whole-state, ownership-only, no-transplant',
         list(e), [ss['layers'], ss['positions'], ss['rank'], ss['whole_read_correct'], ss['piece_correct'],
                   r4(rd['accuracy_whole']), r4(rd['accuracy_ownership_only']), r4(rd['accuracy_untouched'])])
show('arm C: ownership-only within 0.004 of the no-transplant rate (largest gap)', [True],
     [max(abs(m['primary']['reading']['accuracy_ownership_only'] - m['primary']['reading']['accuracy_untouched']) for m in M['C']) <= 0.004])
print('         gaps:', [r4(m['primary']['reading']['accuracy_ownership_only'] - m['primary']['reading']['accuracy_untouched']) for m in M['C']])
for a, e in (('T', ([0], 'action', 8, 180, 180)), ('M', ([1], 'post-identity', 8, 180, 180))):
    for s in range(3):
        ss = M[a][s]['primary']['site_set']
        show(f'arm {a} seed {s}: layers, positions, size, whole read, piece', list(e),
             [ss['layers'], ss['positions'], ss['rank'], ss['whole_read_correct'], ss['piece_correct']])
show('arm M whole-state share', [0.7800, 0.7738, 0.7937], [r4(m['primary']['reading']['accuracy_whole']) for m in M['M']], 0.0001)
show('arm M ownership-only share', [0.4050, 0.4062, 0.3688], [r4(m['primary']['reading']['accuracy_ownership_only']) for m in M['M']], 0.0001)
show('arm T stricter row: layer, positions, size, reading (seed 0..2)', [[1], 'action', 8, 0.0] * 3,
     sum([[m['stricter']['site_set']['layers'], m['stricter']['site_set']['positions'], m['stricter']['site_set']['rank'],
           r4(m['stricter']['reading']['degree'])] for m in M['T']], []))

print('\n=== 4. Counts against the four-fifths floor, 144 of 180 (sections 3, 5.4, 6.4, 7.2)')
best_piece_F = max(max(f['piece'].values()) for n in N['F'] for f in n['fits'].values())
show('arm F: best piece at any layer, size, seed', [34], [best_piece_F])
show('arm F whole read at layer 1, seeds 0..2', [32, 12, 18], [n['fits']['1']['whole'] for n in N['F']])
show('arm F seed 1, layer 1: piece against whole (section 6.4 item 2)', [17, 12],
     [max(N['F'][1]['fits']['1']['piece'].values()), N['F'][1]['fits']['1']['whole']])
chosen_whole = [m['primary']['site_set']['whole_read_correct'] for a in 'TCM' for m in M[a]]
show("every chosen piece's whole read is 176 or more of 180", [176], [min(chosen_whole)])
chosen_piece = [m['primary']['site_set']['piece_correct'] for a in 'TCM' for m in M[a]]
show('lowest piece among those that clear', [150], [min(chosen_piece)])
show('every chosen piece on arms T, C, M is at or above 144', [True], [all(p >= 144 for p in chosen_piece)])
# section 17 failure 2's block: built arms reach 144 at every state past the injection
past = [max(n['fits'][l]['piece'].values()) for a in 'TCM' for n in N[a] for l in '1234']
show('arms T, C, M: a piece reaches 144 at every running state past layer 0 (lowest best piece)', [True], [min(past) >= 144])
print('         lowest best piece past layer 0 on the built arms:', min(past))

print('\n=== 5. Whole-state floor on development and fresh episodes (section 6.4 item 1; section 17 failure 1)')
f0 = N['F'][0]
rs = N['F'][0].get('rule_7_switched_off')
print('    arm F seed 0, site with the piece rule switched off:', rs)
g = [c for c in f0['grid'] if c['layers'] == rs['layers'] and c['positions'] == rs['positions'] and c['rank'] == rs['rank']][0]
show('arm F seed 0 on development episodes: room against room needed', [0.4433, 0.4280],
     [r4(g['floor']['room']), r4(g['floor']['required_room'])])
print('         margin in episodes of 600:', round((g['floor']['room'] - g['floor']['required_room']) * 600, 2))
show('whole-state floor on fresh episodes clears on all twelve', [True],
     [all(m['primary']['reading']['floor']['clears'] for a in ARMS for m in M[a])])
den = {f'{a}/{s}': r4(M[a][s]['primary']['reading']['accuracy_whole'] - M[a][s]['primary']['reading']['accuracy_untouched'])
       for a in ARMS for s in range(3)}
show('smallest denominator among the nine that read (arm C seed 2); arm F seed 0', [0.4863, 0.4263],
     [min(v for k, v in den.items() if k[0] != 'F'), den['F/0']])
marg = [r4(M['F'][s]['primary']['reading']['floor']['room'] - M['F'][s]['primary']['reading']['floor']['required_room']) for s in range(3)]
show('arm F denominator clears the floor by 0.026 to 0.103 (section 17)', [0.026, 0.103], [round(min(marg), 3), round(max(marg), 3)])

print('\n=== 6. Controls (section 7.3)')
c = lambda a, s, k: M[a][s]['primary']['controls'][k]
show('control 1, arm T complement share', [0.0, 0.0, 0.0], [c('T', s, '1')['complement_donor_share'] for s in range(3)])
show('control 1, arm C complement share', [0.5450, 0.5625, 0.5312], [r4(c('C', s, '1')['complement_donor_share']) for s in range(3)], 0.0001)
show('control 1, arm M complement share', [0.3875, 0.3762, 0.4288], [r4(c('M', s, '1')['complement_donor_share']) for s in range(3)], 0.0001)
show('control 1, arm F complement share', [0.4838, 0.5637, 0.5400], [r4(c('F', s, '1')['complement_donor_share']) for s in range(3)], 0.0001)
show('arm F whole-state share (described)', [0.4850, 0.5675, 0.5300], [r4(M['F'][s]['primary']['reading']['accuracy_whole']) for s in range(3)])
show('control 3, arm C seed 0: below, equal, above', [0, 0, 20], [c('C', 0, '3')[k] for k in ('below', 'equal', 'above')])
show('control 3, arm C seed 1: below, equal, above', [6, 1, 13], [c('C', 1, '3')[k] for k in ('below', 'equal', 'above')])
show('control 3, arm C seed 2: below, equal, above', [6, 5, 9], [c('C', 2, '3')[k] for k in ('below', 'equal', 'above')])
show('control 3, arms T and M: the ownership-only share is above all twenty draws (draws below = 20)', [20] * 6,
     [c(a, s, '3')['below'] for a in 'TM' for s in range(3)])
meds = [c('M', s, '3')['median'] for s in range(3)]
show('control 3, arm M random medians 0.015 to 0.019', [0.015, 0.019], [round(min(meds), 3), round(max(meds), 3)])
print('         arm F control 3 (below, equal, above):', [[c('F', s, '3')[k] for k in ('below', 'equal', 'above')] for s in range(3)])
ex = sorted(r4(c(a, s, '4')['above_untouched']) for a in ARMS for s in range(3))
print('    control 4 as version 3 defined it, excess over the no-transplant rate, sorted:', ex)
show('old control 4: six at 0.005 or less, six between 0.065 and 0.10 (to two decimals; the largest is 0.1013)', [6, 6],
     [sum(1 for x in ex if x <= 0.005), sum(1 for x in ex if 0.0645 <= x < 0.105)])
show('control 6, trial counts same-value / different-value on all twelve', [81, 719] * 12,
     sum([[c(a, s, '6')['same_value_trials'], c(a, s, '6')['different_value_trials']] for a in ARMS for s in range(3)], []))
show('control 6, arm T same-value and different-value moved', [0.0, 1.0] * 3,
     sum([[r4(c('T', s, '6')['same_value_moved']), r4(c('T', s, '6')['different_value_moved'])] for s in range(3)], []))
show('control 6 same-value moved, arm C', [0.5062, 0.6296, 0.5679], [r4(c('C', s, '6')['same_value_moved']) for s in range(3)], 0.0001)
show('control 6 same-value moved, arm M', [0.2222, 0.2716, 0.3210], [r4(c('M', s, '6')['same_value_moved']) for s in range(3)], 0.0001)
show('control 6 same-value moved, arm F', [0.7284, 0.6790, 0.6296], [r4(c('F', s, '6')['same_value_moved']) for s in range(3)], 0.0001)
dv = [c(a, s, '6')['different_value_moved'] for a in 'CMF' for s in range(3)]
show('control 6 different-value moved on arms C, M, F: 0.82 to 0.95', [0.82, 0.95], [round(min(dv), 2), round(max(dv), 2)])
places = set()
for a in ARMS:
    for s in range(3):
        m = M[a][s]
        places.add((a, s, 'primary')); assert c(a, s, '7')['bit_identical'] is True
        if 'stricter' in m and m['stricter']['site_set'] != m['primary']['site_set']:
            places.add((a, s, 'stricter')); assert m['stricter']['controls']['7']['bit_identical'] is True
show('control 7 holds at fifteen different places', [15], [len(places)])

print('\n=== 7. Rider and true-slot reference (section 7.2 items 6, 7; section 5.3)')
rid = lambda a: [r4(M[a][s]['rider_at_arm_T_site_set']['reading']['accuracy_whole']) for s in range(3)]
show("rider, arm C whole-state share at arm T's site", [0.0512, 0.0488, 0.0600], rid('C'), 0.0001)
show("rider, arm F whole-state share at arm T's site", [0.0587, 0.0563, 0.0688], rid('F'), 0.0001)
show("rider, arm M whole-state share at arm T's site", [0.4088, 0.4138, 0.4100], rid('M'), 0.0001)
show('rider returns no verdict on arms C, F, M on every seed', ['no verdict'] * 9,
     [M[a][s]['rider_at_arm_T_site_set']['reading']['status'] for a in 'CFM' for s in range(3)])
ts = [M['M'][s]['primary']['true_slot']['reading']['degree'] for s in range(3)]
show('arm M true-slot reading', [0.4837, 0.4760, 0.4920], [r4(x) for x in ts])
show('arm M route formula agrees with the true-slot reading to four decimals', [True],
     [all(r4(M['M'][s]['primary']['true_slot']['route_formula']) == r4(ts[s]) for s in range(3))])
show('arm M blind reading minus true-slot reading', [0.0049, 0.0099, 0.0529], [round(abs(deg['M'][s] - ts[s]), 4) for s in range(3)])
print('         unrounded, seed 1:', abs(deg['M'][1] - ts[1]))
show('arm T true-slot reading', [0.0, 0.0, 0.0], [r4(M['T'][s]['primary']['true_slot']['reading']['degree']) for s in range(3)])
show('arm M entangled share of the fresh trials', [0.60375] * 3, [M['M'][s]['primary']['true_slot']['entangled_share'] for s in range(3)])

print('\n=== 8. Control 2 on arm F seed 0 (section 7.3 item 2; section 6.4 item 2; the packet pages 1 and 2)')
c2 = M['F'][0]['control2']
fits = c2['named_read_fits']
show('named read: best whole read at any layer, best piece at any layer', [137, 139],
     [max(f['whole'] for f in fits.values()), max(max(f['piece'].values()) for f in fits.values())])
cand_layers = sorted({tuple(x['layers']) for x in c2['candidates']})
print('    candidate layer sets:', cand_layers)
show('the packet page 2: candidates at layers 1 and 3, best pieces 92 and 115; layer 2 best piece 139', [92, 115, 139],
     [max(fits['1']['piece'].values()), max(fits['3']['piece'].values()), max(fits['2']['piece'].values())])
show('named-other correct of 3,000: arm C, then arm F', [760, 751, 708, 994, 781, 746],
     [M[a][s]['gate_run']['other_correct'] for a in 'CF' for s in range(3)])
show('control 2 status on arms T and M', ['not applicable'] * 6, [M[a][s]['control2']['status'] for a in 'TM' for s in range(3)])

print('\n=== 9. Arm C seed 1: the choice between layer 1 and layer 4 (section 5.2)')
for x in N['C'][1]['candidates']:
    if x['rank'] == 8:
        print('    candidate, 8 directions:', x['layers'], x['positions'], 'dev ownership-only', r4(x['dev_ownership_only']),
              'piece', x['piece_correct'])
best = sorted((x for x in N['C'][1]['candidates'] if x['piece_correct'] >= 144), key=lambda x: -x['dev_ownership_only'])
show('arm C seed 1: top two development ownership-only shares among sizes that clear', [0.0533, 0.0517],
     [r4(best[0]['dev_ownership_only']), r4(sorted({r4(b['dev_ownership_only']) for b in best}, reverse=True)[1])])
print('         top candidate:', best[0]['layers'], best[0]['positions'], best[0]['rank'],
      '| the gap in episodes of 600:', round((best[0]['dev_ownership_only'] - 0.051666666) * 600, 2))

print('\n=== 10. The short pre-stated run (sections 3, 5.2, 5.3, 7.2 item 3, 7.3 items 2 and 4)')
A, B, C = J(S + 'part_a.json'), J(S + 'part_b.json'), J(S + 'part_c_NOT_A_RESULT.json')
show('control 4 as redefined holds on all twelve; outputs bit-identical; no action changed', [True, True, 0],
     [all(m['holds'] for m in A['models'].values()), all(m['outputs_bit_identical'] for m in A['models'].values()),
      sum(m['trials_whose_action_changed'] for m in A['models'].values())])
show('donor-value share equals the no-transplant share on every line', [True],
     [all(m['donor_value_share'] == m['no_transplant_share'] for m in A['models'].values())])
show('null transplant at the same positions bit-identical on all twelve', [True],
     [all(m['null_transplant_at_these_positions_bit_identical'] for m in A['models'].values())])
pp = A['positions_per_pair']
show('positions transplanted per pair: min, max, mean about 5', [1, 21, 5.2], [pp['min'], pp['max'], round(pp['mean'], 1)])
b = B['models']
show('action-position counts equal the controls re-run on all twelve', [True], [all(m['matches_the_controls_rerun'] for m in b.values())])
show('arm C seed 1, piece at 1, 2, 3 before the action; on the average', [139, 139, 33, 113],
     [p['piece'] for p in b['C/1']['other_positions']] + [b['C/1']['mean_over_the_other_positions']['piece']])
show('arm C seed 1, whole state at 1, 2, 3 before; on the average', [180, 179, 179, 179],
     [p['whole'] for p in b['C/1']['other_positions']] + [b['C/1']['mean_over_the_other_positions']['whole']])
print('         positions:', [p['position'] for p in b['C/1']['other_positions']])
pc2 = [p['piece'] for p in b['C/2']['other_positions']]
wh2 = [p['whole'] for p in b['C/2']['other_positions']]
show('arm C seed 2: ten positions; piece from 30 to 139, all below 144; whole 149 to 180; average 123 (whole 180)',
     [10, 30, 139, 149, 180, 123, 180],
     [len(pc2), min(pc2), max(pc2), min(wh2), max(wh2), b['C/2']['mean_over_the_other_positions']['piece'], b['C/2']['mean_over_the_other_positions']['whole']])
show('arm M piece on the average (whole 180 each)', [163, 174, 175, 180, 180, 180],
     [b[f'M/{s}']['mean_over_the_other_positions']['piece'] for s in range(3)] + [b[f'M/{s}']['mean_over_the_other_positions']['whole'] for s in range(3)])
show('arm M: positions of ten at which the piece reaches 144', [4, 4, 7],
     [sum(1 for p in b[f'M/{s}']['other_positions'] if p['piece'] >= 144) for s in range(3)])
tok4 = [[p['piece'] for p in b[f'M/{s}']['other_positions'] if p['position'].startswith('first own turn, token 4')][0] for s in range(3)]
show('arm M: piece at the fourth token of the first own turn', [34, 71, 33], tok4)
built_whole = [p['whole'] for k, m in b.items() if k[0] in 'TCM' for p in m['other_positions']]
show('whole state at the other positions on the built arms: 149 to 180', [149, 180], [min(built_whole), max(built_whole)])
fp = [(k, p['position'], p['piece']) for k, m in b.items() if k[0] == 'F' for p in m['other_positions']]
out = [x for x in fp if not 11 <= x[2] <= 36]
show('arm F: piece between 11 and 36 everywhere except one position (seed 2, first token, 145)',
     [1, 'F/2', 'first own turn, token 1 of 5', 145], [len(out)] + list(out[0]))
print('         arm F on the average (piece, whole):', [(b[f'F/{s}']['mean_over_the_other_positions']) for s in range(3)])
show('single-position sites: arm T every seed and arm C seed 0', [0, 0, 0, 0],
     [len(b[k]['other_positions']) for k in ('T/0', 'T/1', 'T/2', 'C/0')])
ret = C['returned']
print('    part C keys returned:', [k for k in ret if k != 'candidates'])
for k in ret:
    if k not in ('candidates', 'named_read_fits'):
        print('      ', k, '=', ret[k])

print('\n=== 11. The gate file (sections 4.4, 5.3, 5.4, 8.1, 8.2)')
G = J(R + 'out-repairs/gate_base.json')
run = G['runs']
show('the bar: 790 of 3,000', [790, 3000], [G['bar']['min_correct'], G['bar']['episodes']])
show('arm F named-other correct', [994, 781, 746], [run[f'F/base/{s}']['other_correct'] for s in range(3)])
show('arm C named-other correct', [760, 751, 708], [run[f'C/base/{s}']['other_correct'] for s in range(3)])
rng = lambda a, k: [r4(min(run[f'{a}/base/{s}'][k] for s in range(3))), r4(max(run[f'{a}/base/{s}'][k] for s in range(3)))]
show('arm F own-directed 0.5513 to 0.5597', [0.5513, 0.5597], rng('F', 'own'))
show('ownership-blind solver own-directed 0.2340 to 0.2383', [0.2340, 0.2383], rng('blind', 'own'))
show('arm F lesioned own-directed 0.1760 to 0.1940', [0.1760, 0.1940], rng('F', 'lesioned_own'))
show('arm M own-directed 0.8613 to 0.8667', [0.8613, 0.8667], rng('M', 'own'))
show('arm M named-other 0.5517 to 0.5663', [0.5517, 0.5663], rng('M', 'other'))
show('arm C lesioned 0.1703 to 0.1830; arm M 0.2190 to 0.2230', [0.1703, 0.1830, 0.2190, 0.2230], rng('C', 'lesioned_own') + rng('M', 'lesioned_own'))
show('arm T lesioned own-directed', [0.2467, 0.2510, 0.2733], [r4(run[f'T/base/{s}']['lesioned_own']) for s in range(3)])
show('arm T learned both to 1.0000', [1.0] * 6, [run[f'T/base/{s}'][k] for s in range(3) for k in ('own', 'other')])
show('name-only solver: named-other 1.0000, own-directed 0.2380', [1.0, 0.238], [G['name_only_solver']['other'], G['name_only_solver']['own']])

print('\n=== 12. What summary.json records about the software (section 7.2 item 1)')
print('    top-level fields of summary.json other than arms and separation:',
      {k: v for k, v in SUM.items() if k not in ('arms', 'separation')})

print('\n' + ('ALL MATCH' if not bad else f'{len(bad)} DIFFER:'))
for x in bad:
    print('  -', x)
