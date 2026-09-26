# Both readings of "the smallest layer set that clears the floor", recomputed on the
# committed development grids with every all-positions site set removed (the widened
# exclusion of the repairs rulings, item 3). Tie-breaks copied from repairs.py nominate().
import json, sys
base = sys.argv[1]
POS = ['action', 'action+ans', 'action+3', 'post-identity', 'all']


def pick(grid):
    clr = [g for g in grid if g['floor']['clears'] and g['positions'] != 'all']
    if not clr:
        return None, None, 0
    sm = {}
    for g in clr:
        k = (len(g['layers']), g['layers'])
        if g['positions'] not in sm or k < sm[g['positions']]:
            sm[g['positions']] = k
    c = [g for g in clr if (len(g['layers']), g['layers']) == sm[g['positions']]]
    best = min(c, key=lambda g: (-g['accuracy_ownership_only'], g['rank'], POS.index(g['positions'])))
    sens = min(clr, key=lambda g: (-g['accuracy_ownership_only'], len(g['layers']), g['rank'],
                                   POS.index(g['positions']), g['layers']))
    return best, sens, len({(tuple(g['layers']), g['positions']) for g in clr})


cfg = lambda g: (tuple(g['layers']), g['positions'], g['rank'])
nd = nz = ch = 0
for f in ('nominate_base_T_C.json', 'nominate_base_F.json', 'nominate_base_M.json'):
    for key, r in sorted(json.load(open(base + f))['arms'].items()):
        o = r['ownership']
        b, s, c = pick(o['grid'])
        d = cfg(b)[:2] != cfg(s)[:2]
        gap = s['accuracy_ownership_only'] - b['accuracy_ownership_only']
        moved = cfg(b) != cfg(o['nomination'])
        nd += d; nz += gap > 0; ch += moved
        print(f"{key:10s} clearing={c:2d} nominated={cfg(b)} {b['accuracy_ownership_only']:.4f} | "
              f"other={cfg(s)} {s['accuracy_ownership_only']:.4f} | differs={d} gap={gap:.4f} | "
              f"nomination changed by widening={moved}")
print('site sets differ:', nd, 'of 12; ownership-only share differs:', nz, 'of 12; '
      'nominations changed by the widening:', ch, 'of 12')
