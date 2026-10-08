"""Gate A tier 1 failure-mode pass on version 4 (at d19f914): the tests of
docs/known-failure-modes.md, entries 1 to 3, run on the committed outputs.
Entries 4 to 6 are run by the other scripts and commands named in the review.
Reads files only; loads no model; $0. Run from the root of the checkout.
"""
import json
import re
import subprocess
from fractions import Fraction as Fr
from math import comb

B = "experiments/rehearsal-successor-measure/"
CR, CS, SP = B + "out-controls-rerun/", B + "out-competing-solver-run/", B + "out-short-prestated-run/"
v4 = subprocess.run(["git", "show", "d19f914:docs/successor-experiment-proposal-2026-10-03-v4.md"],
                    capture_output=True, text=True, check=True).stdout.splitlines()

print("=== failure 1, part one: where every no-transplant rate the denominator uses comes from")
for a in "TCFM":
    for s in "012":
        r = json.load(open(f"{CR}measure_{a}_seed{s}.json"))["primary"]["reading"]
        print(f"  {a}/{s}: accuracy_untouched {r['accuracy_untouched']:.4f}  <- {CR}measure_{a}_seed{s}.json, primary.reading")
print("=== failure 1, part two: denominator and top of scale at the chosen site set (registered form)")
low = []
for a in "TCFM":
    for s in "012":
        m = json.load(open(f"{CR}measure_{a}_seed{s}.json"))["primary"]
        r = m["reading"]
        den = r["accuracy_whole"] - r["accuracy_untouched"]
        top = (r["accuracy_whole"] - r["accuracy_untouched"]) / den
        low.append((den, a, s, m["described_only"]))
        print(f"  {a}/{s}: denominator {den:.4f}; top of scale {top:.4f}; {'described only' if m['described_only'] else 'reads'}")
print("  smallest denominator among those that read:", min((d, f'{a}/{s}') for d, a, s, x in low if not x))
print("=== failure 1, the case the text's floor admits: a model whose own-directed accuracy is at or under its no-transplant rate")
for s in "012":
    for rd in ("channel_removed", "channel_left_on"):
        n = json.load(open(f"{CS}nominate_blind_seed{s}_{rd}.json"))
        u, acc = n["dev_untouched"], n["dev_accuracy"]
        dens = [g["accuracy_whole"] - u for g in n["grid"]]
        need = 0.8 * (acc - u)
        admitted = [d for d in dens if d >= need]
        print(f"  solver seed {s} {rd:<16}: floor asks {need:+.4f}; rows the printed formula admits {len(admitted)} of {len(dens)}; "
              f"denominators among them {min(admitted) if admitted else float('nan'):+.4f} to {max(admitted) if admitted else float('nan'):+.4f}")

print()
print("=== failure 2, part one: a route sentence in sections 0 to 16, this design's own words")
cut = next(i for i, l in enumerate(v4) if l.startswith("## 17. "))
pat = re.compile(r"route by which|carried by the token|forced by the loss|is the input token", re.I)
for i, l in enumerate(v4[:cut]):
    if pat.search(l):
        print(f"  {i + 1}: {l.strip()}")
print("=== failure 2, part two: the same read, the same bar (144 of 180), at the position where the marker word")
print("    IS the input token (the first token of the model's first own turn) and at the registered action position")
b = json.load(open(SP + "part_b.json"))["models"]
for a in "TCFM":
    for s in "012":
        mm = b[f"{a}/{s}"]
        tok = [p for p in mm["other_positions"] if p["position"] == "first own turn, token 1 of 5"]
        tok_whole = tok[0]["whole"] if tok else "(single-position site: not reported)"
        act = mm["at_the_action_position"]["whole"]
        print(f"  {a}/{s}: whole state at the marker's own token {tok_whole}; whole read at the action position {act}"
              f" -> {'second clears, first does not' if tok and tok_whole >= 144 and act < 144 else 'both clear' if act >= 144 else 'see figures'}")
print("  the named agent's read (control 2) on the one model that learned the named-other condition, arm F seed 0:")
c2 = json.load(open(CR + "measure_F_seed0.json"))["control2"]
fits = c2["named_read_fits"]
print("   ", {l: (v["whole"], max(v["piece"].values())) for l, v in fits.items()}, "-> best", max(max(v['piece'].values()) for v in fits.values()), "of 144 needed")

print()
print("=== failure 3, part one: every pre-stated cell, counted")
for a in "TCFM":
    c = json.load(open(f"{CR}measure_{a}_seed0.json"))["primary"]["controls"]["6"]
    print(f"  control 6, {a}/0: same-value {c['same_value_trials']}, different-value {c['different_value_trials']}")
print("  control 4 as redefined, positions per pair:", json.load(open(SP + "part_a.json"))["positions_per_pair"])
n_c2 = sum(json.load(open(f"{CR}measure_{a}_seed{s}.json"))["control2"]["status"] not in ("no verdict", "not applicable")
           for a in "TCFM" for s in "012")
print("  control 2: toy models on which it returned a figure:", n_c2, "of 12")
seed_split = 0
for a in "TCFM":
    st = [json.load(open(f"{CR}measure_{a}_seed{s}.json"))["primary"]["described_only"] for s in "012"]
    seed_split += len(set(st)) > 1
print("  the two-of-three rule: arms whose three seeds disagree on the toy:", seed_split, "of 4")
gb = json.load(open(B + "out-repairs/gate_base.json"))
keys = sorted({k for r in gb["runs"].values() for k in r})
print("  the lesion clause 'the ownership-free state and syntax batteries must hold': fields the gate file records:", keys)
print("  grep of the rehearsal code for a state or syntax battery:",
      subprocess.run("grep -rlE '\\bT_(state|syntax)\\b|([Ss]tate|[Ss]yntax) batter' "
                     "experiments/rehearsal-successor-measure/src || true",
                     shell=True, capture_output=True, text=True).stdout.strip() or "(no file)")
print("=== failure 3, part three: thresholds at both ends")
n = 3000


def tail(k):
    return Fr(sum(comb(n, i) * 3 ** (n - i) for i in range(k, n + 1)), 4 ** n)


k = min(k for k in range(760, 820) if tail(k) <= Fr(1, 20))
print(f"  gate bar {k} of 3,000; a model at one in four clears it with probability {float(tail(k)):.4f}")
for p in (1.0, 0.8712, 0.56, 0.2633):
    print(f"  no-transplant rule at own-directed {p}: formula {(1 - p) / 7:.4f}; a broken pairing (0.125) flagged: {abs(0.125 - (1 - p) / 7) > 0.018}")
print("  piece floor at 144 of 180: the competing solver's best piece 20 to 25, arm F's 34, the built arms' chosen pieces 150 to 180")
print("  whole-state floor, printed formula, at the broken end (solver seeds 0 and 1): admits every site set (above); at the working end: section 1 of rule_from_text.out.txt")
