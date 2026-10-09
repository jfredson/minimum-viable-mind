import sys, os
def cells(line): return len(line.rstrip('\n').strip().strip('|').split('|'))
def rows(p): return [l for l in open(p) if l.startswith('|')]
def check(new, old=None):
    n = rows(new); h = cells(n[0]); bad = [l[:30] for l in n if cells(l) != h]
    out = f"{new}: header {h} cells, {len(n)} rows, mismatched {len(bad)}"
    if old:
        o = rows(old); changed = 0; ok = True
        lo = [l for l in open(old)]; ln = [l for l in open(new)]
        if len(lo) != len(ln): ok = False
        for a, b in zip(lo, ln):
            if a != b:
                changed += 1
                if not (a.replace('| withheld ', '', 1) == b and a.count('withheld') - b.count('withheld') == 1): ok = False
        out += f"; vs old: {changed} lines differ, all exactly one withheld cell dropped: {ok}; old header {cells(o[0])}, old withheld row cells {sorted(set(cells(l) for l in o if 'withheld' in l))}"
    print(out); return bad
for a in sys.argv[1:]:
    new, _, old = a.partition(':')
    check(new, old or None)
