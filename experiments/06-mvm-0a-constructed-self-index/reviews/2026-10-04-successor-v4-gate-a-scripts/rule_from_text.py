"""Gate A tier 1, decisive check: the registration text's rule, written from
the text alone, run on the committed development grids, compared with what
the committed code chose; then the reading, the controls that hold, the
two-of-three rule, the separation and the outcome term, all from the text.

Written 2026-10-04 by the Gate A tier 1 reviewer of version 4. Reads committed
output files only; loads no model; trains nothing; $0.

The rule is taken from version 4 at d19f914, section 6.4 item 1 (the
whole-state floor, as its formula is printed), section 7.2 items 2 to 5 (the
family, the smallest clearing layer set per position set, the piece rule
applied after the layers, nomination by the highest development
ownership-only share, ties to the smaller size then the earlier position
set), section 6.4 items 3 and 5 (the no-transplant rule with its 0.018 room;
the controls that hold), section 3 (two seeds of three; the separation as the
lowest reading of arm C minus the highest of arm T; the outcome terms).

Nothing in it imports the checked code. If the text describes a different
rule from the one that ran, the nominations below come out different.

Run from the root of the checkout:
    .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/rule_from_text.py
"""
import json
import os

B = "experiments/rehearsal-successor-measure/"
CR = B + "out-controls-rerun/"
CS = B + "out-competing-solver-run/"
SP = B + "out-short-prestated-run/part_a.json"
POS = ["action", "action+ans", "action+3", "post-identity"]
SIZES = [1, 2, 4, 8]
PIECE_MIN = 144          # four fifths of 180 held-out episodes (section 7.4)
ROOM = 0.018             # the no-transplant allowance (section 6.4, item 3)
N_STATES = 5             # the toy: four blocks, five running states


def family(strict=False):
    contig = [tuple(range(a, b + 1)) for a in range(N_STATES) for b in range(a, N_STATES)]
    fam = [(L, P) for L in contig for P in POS if not (0 in L and P != "action")]
    if strict:
        fam = [(L, P) for (L, P) in fam if 0 not in L]
    return fam


def floor_text(whole, untouched, acc):
    """Section 6.4, item 1, exactly as printed:
    accuracy_whole - accuracy_untouched >= 0.8 * (own_directed_accuracy - accuracy_untouched)"""
    return whole - untouched >= 0.8 * (acc - untouched)


def floor_code(whole, untouched, acc):
    """What repairs.floor_check does (read from the code, for comparison only)."""
    need = 0.8 * (acc - untouched)
    return whole - untouched >= need and need > 0


def nominate(n, strict=False, floor=floor_text):
    u, acc = n["dev_untouched"], n["dev_accuracy"]
    fits = n["fits"]
    fam = set(family(strict))
    rows = [g for g in n["grid"] if (tuple(g["layers"]), g["positions"]) in fam]
    clearing = [g for g in rows if floor(g["accuracy_whole"], u, acc)]
    n_clear = len({(tuple(g["layers"]), g["positions"]) for g in clearing})
    if not clearing:
        return None, "no site set clears the whole-state floor", n_clear
    smallest = {}
    for g in clearing:                                   # item 4: fewest layers, earliest
        key = (len(g["layers"]), g["layers"])
        if g["positions"] not in smallest or key < smallest[g["positions"]]:
            smallest[g["positions"]] = key
    cands = [g for g in clearing if (len(g["layers"]), g["layers"]) == smallest[g["positions"]]]
    ok = [g for g in cands                               # item 3: worst layer's piece >= 144
          if min(fits[str(l)]["piece"][str(g["rank"])] for l in g["layers"]) >= PIECE_MIN]
    if not ok:
        return None, "read failed its floor: no size's piece reaches four fifths", n_clear
    best = min(ok, key=lambda g: (-g["accuracy_ownership_only"], g["rank"], POS.index(g["positions"])))
    return (tuple(best["layers"]), best["positions"], best["rank"]), "nominated", n_clear


def spec(s):
    return None if s is None else (tuple(s["layers"]), s["positions"], s["rank"])


print("=== 1. Nomination: the text's rule against the committed code's choice, twelve toy models")
agree = 0
for strict in (False, True):
    for a in "TCFM":
        for s in "012":
            n = json.load(open(f"{CR}nominate_{a}_seed{s}.json"))
            mine, why, nc = nominate(n, strict)
            ref = n["stricter" if strict else "primary"]
            same = (mine == spec(ref["site_set"])) and (why == ref["status"])
            agree += same
            print(f"{'stricter' if strict else 'primary '} {a}/{s}: text -> {why}, {mine}; "
                  f"code -> {ref['status']}, {spec(ref['site_set'])}; same: {same}")
print(f"agree on {agree} of 24 (twelve primary, twelve stricter)")

print()
print("=== 2. The reading on fresh episodes, from the text, against the committed degree")
part_a = json.load(open(SP))["models"]
reads = {}
for a in "TCFM":
    for s in "012":
        m = json.load(open(f"{CR}measure_{a}_seed{s}.json"))
        p = m["primary"]
        r = p["reading"]
        w, o, u, acc = r["accuracy_whole"], r["accuracy_ownership_only"], r["accuracy_untouched"], r["arm_own_accuracy"]
        fl = floor_text(w, u, acc)
        deg = (w - o) / (w - u) if fl else None
        nt_ok = abs(u - (1 - acc) / 7) <= ROOM
        c = p["controls"]
        c7 = c["7"]["bit_identical"]
        c1 = (c["1"]["complement_donor_share"] <= u + ROOM) if a == "T" else True
        c4 = part_a[f"{a}/{s}"]["outputs_bit_identical"]
        gate = m["gate"]["passes"]
        described = p["described_only"]
        reads_here = (not described) and gate and fl and nt_ok and c7 and c1 and c4
        reads[(a, s)] = deg if reads_here else None
        why = ("reads" if reads_here else
               "no verdict: " + ", ".join(x for x, bad in (("read failed its floor (described only)", described),
                                                           ("fails its gate", not gate),
                                                           ("floor missed on fresh episodes", not fl),
                                                           ("no-transplant rate outside its room", not nt_ok),
                                                           ("a control that holds failed", not (c7 and c1 and c4))) if bad))
        cd = r["degree"]
        print(f"{a}/{s}: text degree {('%.4f' % deg) if deg is not None else 'none'}; committed {('%.4f' % cd) if cd is not None else 'none'}; "
              f"no-transplant miss {u - (1 - acc) / 7:+.4f}; controls 7/1/4 {c7}/{c1}/{c4}; gate {gate} -> {why}")

print()
print("=== 3. Two seeds of three, the separation, and the outcome term (section 3)")
arm_reads = {a: [reads[(a, s)] for s in "012" if reads[(a, s)] is not None] for a in "TCFM"}
for a in "TCFM":
    print(f"arm {a}: reads on {len(arm_reads[a])} of 3 seeds: {[round(x, 4) for x in arm_reads[a]]}")
ok_T, ok_C = len(arm_reads["T"]) >= 2, len(arm_reads["C"]) >= 2
sep = (min(arm_reads["C"]) - max(arm_reads["T"])) if (ok_T and ok_C) else None
print(f"separation, lowest of arm C minus highest of arm T: {sep:.4f}; clears 0.5: {sep >= 0.5}")
if ok_T and ok_C and sep >= 0.5:
    outcome = "R1, metric validated, degree read" if len(arm_reads["F"]) >= 2 else \
        "the fifth term, metric validated, degree not read"
else:
    outcome = "not settled by this script"
print("outcome by the text's rules:", outcome)

print()
print("=== 4. The ordinary competing solver: the text's floor against the code's floor, development episodes")
for s in "012":
    for rd in ("channel_removed", "channel_left_on"):
        n = json.load(open(f"{CS}nominate_blind_seed{s}_{rd}.json"))
        u, acc = n["dev_untouched"], n["dev_accuracy"]
        rows = [g for g in n["grid"] if (tuple(g["layers"]), g["positions"]) in set(family())]
        rooms = sorted({round(g["accuracy_whole"] - u, 6) for g in rows})
        t_mine, t_why, t_n = nominate(n, floor=floor_text)
        c_mine, c_why, c_n = nominate(n, floor=floor_code)
        print(f"seed {s}, {rd}: own-directed {acc:.4f}, untouched {u:.4f}, floor asks for {0.8 * (acc - u):+.4f}; "
              f"whole - untouched over the family: {rooms[0]:+.4f} to {rooms[-1]:+.4f}")
        print(f"    text's floor: {t_n} of 45 site sets clear -> {t_why}")
        print(f"    code's floor: {c_n} of 45 site sets clear -> {c_why}   (committed: {n['primary']['status']})")
