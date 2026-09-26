# The two readings of "the smallest layer set that clears the floor", as the committed
# nomination files at e0626b2 record them: `nomination` (smallest clearing layer set per
# position set, then the highest ownership-only share) against `sensitivity` (the highest
# ownership-only share over every clearing site set). Usage: recount_readings.py <out-repairs/>
import json, sys
base = sys.argv[1]
site = lambda g: (tuple(g['layers']), g['positions'])
cfg = lambda g: (tuple(g['layers']), g['positions'], g['rank'])
rows = []
for f in ('nominate_base_T_C.json', 'nominate_base_F.json', 'nominate_base_M.json'):
    for key, r in json.load(open(base + f))['arms'].items():
        o = r['ownership']
        rows.append((key, o['nomination'], o['sensitivity'], o['site_sets_clearing']))
ds = dc = dz = 0
gaps = []
for key, n, x, c in sorted(rows):
    a = site(n) != site(x); b = cfg(n) != cfg(x)
    g = x['accuracy_ownership_only'] - n['accuracy_ownership_only']
    ds += a; dc += b; dz += g > 0; gaps.append(g)
    print(f"{key:10s} clearing={c:2d} nominated={cfg(n)} own={n['accuracy_ownership_only']:.4f} | "
          f"other={cfg(x)} own={x['accuracy_ownership_only']:.4f} | site differs={a} gap={g:.4f}")
print('pairs:', len(rows), '| site set differs:', ds, '| site set or rank differs:', dc,
      '| ownership-only share differs:', dz, '| largest gap: %.4f' % max(gaps))
