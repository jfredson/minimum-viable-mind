"""Gate A tier 1: the sentence about the ordinary competing solver that John
ruled into the registration text (docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md,
ruling 2), set against the committed outputs it describes. Reads files only.

Ruled sentence: "On the toy, the ordinary competing solver returned no verdict
because no site set cleared the floor at nomination; behind that, its best
piece missed the piece rule by 119 or more of 180 and its untouched rate
missed the no-transplant rule by 0.11 or more, and it would have failed the
gate on learning had it been gated as the free model is."
"""
import json

B = "experiments/rehearsal-successor-measure/out-competing-solver-run/"
ROOM = 0.018
short, vs_formula, vs_rule, gate_short = [], [], [], []
for s in "012":
    for rd in ("channel_removed", "channel_left_on"):
        n = json.load(open(f"{B}nominate_blind_seed{s}_{rd}.json"))
        m = json.load(open(f"{B}measure_blind_seed{s}_{rd}.json"))
        nt = m["no_transplant"]
        short.append(144 - n["best_piece_correct"])
        vs_formula.append(nt["rate"] - nt["formula"])
        vs_rule.append(abs(nt["rate"] - nt["formula"]) - ROOM)
        g = m["gate"]
        gate_short.append(min(g["bar"] - g["own_correct"], g["bar"] - g["other_correct"]))
        print(f"seed {s} {rd:<16} best piece {n['best_piece_correct']:>3} (short of 144 by {144 - n['best_piece_correct']}); "
              f"untouched {nt['rate']:.4f} vs formula {nt['formula']:.4f}: miss {nt['rate'] - nt['formula']:.4f}, "
              f"beyond the 0.018 room {abs(nt['rate'] - nt['formula']) - ROOM:.4f}; "
              f"gate own {g['own_correct']}, named-other {g['other_correct']} of {g['n']} (bar {g['bar']})")
print(f"piece rule missed by: {min(short)} to {max(short)} of 180  -> '119 or more': {min(short) >= 119}")
print(f"untouched rate against the formula: {min(vs_formula):.4f} to {max(vs_formula):.4f}  -> '0.11 or more': {min(vs_formula) >= 0.11}")
print(f"untouched rate beyond the rule's room: {min(vs_rule):.4f} to {max(vs_rule):.4f}  -> '0.11 or more': {min(vs_rule) >= 0.11}")
