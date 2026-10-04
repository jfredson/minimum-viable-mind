"""Check of proposal version 4: run the site-set rule and compare with the
list printed in its section 18; redo its arithmetic on thresholds and money.

Run from the root of the checkout:
    .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/site_sets_and_arithmetic.py

Written separately from the command in section 18: it builds every site set
as a (layers, position set) pair and then applies the exclusions, instead of
counting row by row. Reads one file (version 4). Spends nothing.
"""
import re
from fractions import Fraction as Fr
from math import comb, sqrt

V4 = 'docs/successor-experiment-proposal-2026-10-03-v4.md'
POS = ['action', 'action+ans', 'action+3', 'post-identity']


def family(n_states):
    """Every contiguous run of running states, at every named position set."""
    return [(tuple(range(a, b + 1)), p) for a in range(n_states) for b in range(a, n_states) for p in POS]


def registered(fam):   # layer 0 kept at the action position set only
    return [(L, p) for L, p in fam if 0 not in L or p == 'action']


def narrower(fam):     # decision 20's alternative: layer 0 removed at post-identity only
    return [(L, p) for L, p in fam if 0 not in L or p != 'post-identity']


def stricter(fam):     # the sensitivity row: layer 0 removed everywhere
    return [(L, p) for L, p in fam if 0 not in L]


print('=== 1. The site-set rule, run')
print('states | contiguous layer sets | full family | registered | x4 | narrower | x4 | stricter | x4')
for n in (5, 13):
    f = family(n)
    print(f'{n:>6} | {len(f)//4:>21} | {len(f):>11} | {len(registered(f)):>10} | {4*len(registered(f)):>4} | '
          f'{len(narrower(f)):>8} | {4*len(narrower(f)):>4} | {len(stricter(f)):>8} | {4*len(stricter(f)):>4}')
print('version 4 prints: toy 60 / 45 and 180 / 55 and 220 / 40 and 160; registered model 91 layer sets, 364 / 325 and 1,300 / 351 and 1,404 / 312 and 1,248')

print('\n=== 2. The list printed in section 18, parsed and compared set for set')
text = open(V4).read()
sec18 = text[text.index('## 18. The printed site list'):text.index('## 19. The seven questions')]
for label, n, head in (('registered model', 13, 'registered model: 13 running states'), ('toy model', 5, 'toy model: 5 running states')):
    block = sec18[sec18.rindex(head):]
    printed = set()
    for line in block.splitlines()[1:]:
        m = re.match(r'\s+first state\s+\d+ \| at (.+?) \| layer sets: (.+?) \| ', line)
        if not m:
            if line.strip().startswith('total'):
                total_line = line.strip()
                break
            continue
        for ls in m.group(2).split(', '):
            a, _, b = ls.partition('-')
            L = tuple(range(int(a), int(b or a) + 1))
            for p in m.group(1).split(', '):
                printed.add((L, p))
    mine = set(registered(family(n)))
    print(f'{label}: printed list holds {len(printed)} site sets; the rule gives {len(mine)}; '
          f'in the list and not the rule: {len(printed - mine)}; in the rule and not the list: {len(mine - printed)}')
    print('   its own total line:', total_line)

print('\n=== 3. What the toy code asserts')
src = open('experiments/rehearsal-successor-measure/src/rerun_controls.py').read()
for m in re.finditer(r'.*\b(45|180)\b.*', src):
    if 'assert' in m.group(0) or 'FAMILY' in m.group(0).upper():
        print('   rerun_controls.py:', m.group(0).strip()[:150])

print('\n=== 4. Thresholds')
n = 3000
tail = lambda k: Fr(sum(comb(n, i) * 3 ** (n - i) for i in range(k, n + 1)), 4 ** n)
k = min(k for k in range(760, 820) if tail(k) <= Fr(1, 20))
print(f'gate bar: smallest count with a one-sided tail at or under 0.05 at one in four, of 3,000: {k} (share {k/n:.4f}, tail {float(tail(k)):.4f})')
print('four fifths of 180:', Fr(4, 5) * 180, '| one episode of 180:', round(1 / 180, 4))
sd = sqrt(180 * 0.8 * 0.2)
print(f'sampling spread of a count of 180 at a true share of 0.8: one standard deviation {sd:.2f} episodes ({sd/180:.4f}); '
      f'two {2*sd:.1f} episodes ({2*sd/180:.3f})')
p_pass = float(sum(Fr(comb(180, i) * 4 ** i, 5 ** 180) for i in range(144, 181)))
p_band = float(sum(Fr(comb(180, i) * 4 ** i, 5 ** 180) for i in range(139, 150)))
print(f'a piece whose true accuracy is exactly 0.8 reaches 144 of 180 with probability {p_pass:.3f}; lands in 139 to 149 with probability {p_band:.3f}')
sd3 = sqrt(540 * 0.8 * 0.2)
print(f'at three times as many held-out episodes (540): one standard deviation {sd3/540:.4f}')
for p in (0.78, 0.82):
    q = Fr(int(p * 100), 100)
    pp = float(sum(comb(180, i) * q ** i * (1 - q) ** (180 - i) for i in range(144, 181)))
    print(f'   a piece whose true accuracy is {p} reaches 144 of 180 with probability {pp:.3f}')
for p in (0.2633, 0.56):
    f = (1 - p) / 7
    print(f'no-transplant formula at own-directed {p}: {f:.4f}; a broken pairing (0.1250) misses by {0.125-f:.4f}; margin over 0.018: {0.125-f-0.018:.4f}')
print('graphics-chip fits as shares of 180: 31, 12, 19 ->', [round(x / 180, 3) for x in (31, 12, 19)])
print('407 of 800 =', 407 / 800, '| 483 of 800 =', 483 / 800, '| 1810 of 3000 =', round(1810 / 3000, 4))
print('permutation null 0.111 to 0.128 of 180 =', round(0.111 * 180, 1), 'to', round(0.128 * 180, 1), '| 0.072 of 180 =', round(0.072 * 180, 1))
print('ten positions of a span of 39.2 on average =', round(10 / 39.2, 3))

print('\n=== 5. Money (section 12), from the figures version 4 cites to the ledger and the note')
spent, ceiling = 228.15, 450.0
print(f'headroom: {ceiling} - {spent} = {ceiling-spent:.2f}')
print(f'rehearsal line: 0.02 + 0.50 + 0.05 = {0.02+0.50+0.05:.2f}; 10 - 0.57 = {10-0.57:.2f}')
print(f'four development runs at 1.943: {4*1.943:.2f}')
print(f'a registered-size run: 20.28 hours x 0.99 / 2 = {20.28*0.99/2:.2f}')
F, T, C = 10.04, round(10.04 * 1.044, 2), round(10.04 * 1.080, 2)
print(f'per run from the measured ratios: F {F}, T {T}, C {C}')
eight = 2 * F + 3 * T + 3 * C
print(f'eight runs (two F, three T, three C): {eight:.2f}; + re-run at C {C} + 12 + 23 = {eight+C+12+23:.2f}; with a first release of 32: {eight+C+12+23+32:.2f}')
second = 84.06 + 12 + 23
print(f'ruled split: 44 + {second:.2f} = {44+second:.2f}; difference from 161.90: {44+second-161.90:.2f}')
for m in (29.70, 30.12, 36, 41.76, 32, 44):
    print(f'   ruled split with arm M at {m}: programme after {spent+44+second+m:.2f}, left {ceiling-spent-44-second-m:.2f}')
for m in (30, 42, 32, 44):
    print(f"   the note's split (161.90) with arm M at {m}: successor {161.90+m:.2f}, programme after {spent+161.90+m:.2f}, left {ceiling-spent-161.90-m:.2f}")
print(f'arm M at arm C\'s ratio, lower end: 29.70 x 1.080 = {29.70*1.080:.2f}; three runs at 10.04 = {3*10.04:.2f}')
print(f'whole successor on the ruled split: {44+second+30:.0f} to {44+second+42:.0f}; with arm M at 32 to 44 less 1.94: {44+second+32-1.94:.2f} to {44+second+44-1.94:.2f}')
