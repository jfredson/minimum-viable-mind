"""Section 11 of battery-authoring-spec.md: pilot and test are kept apart.

Run now on the lists and ranges; run again on a test set after registration:
    .venv/bin/python -I experiments/10-loop-removal-test/src/check_overlap.py [--pilot <dir>] [--test <dir>]
Exits non-zero on any failure.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import SYLL_A, SYLL_B, halves, load_lists  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot")
    ap.add_argument("--test")
    a = ap.parse_args()
    L = load_lists()
    fails = []

    def disjoint(name, items, key=lambda x: x):
        h = halves(items)
        A, B = {key(x) for x in h["A"]}, {key(x) for x in h["B"]}
        both = A & B
        if both:
            fails.append(f"{name}: in both halves: {sorted(both)[:10]}")
        return h

    disjoint("countries", L["countries"], lambda x: x["country"])
    disjoint("capitals", L["countries"], lambda x: x["capital"])
    disjoint("objects", L["objects"], lambda x: x["object"])
    disjoint("words3", L["words3"])
    disjoint("syllables A", SYLL_A)
    disjoint("syllables B", SYLL_B)
    h = halves(L["opposites"])
    wa = {w for p in h["A"] for w in (p["a"], p["b"])}
    wb = {w for p in h["B"] for w in (p["a"], p["b"])}
    if wa & wb:
        fails.append(f"opposite words in both halves: {sorted(wa & wb)}")

    # answer values within each numeric kind (ranges from the specification, section 4 and 5)
    ranges = {
        "sum": (set(range(4, 50)), set(range(50, 100))),
        "prod": ({x * y for x in range(2, 13) for y in range(x, 13) if x * y < 40},
                 {x * y for x in range(2, 13) for y in range(x, 13) if x * y >= 40}),
        "unit": ({k * n for k in range(2, 6) for n in range(2, 10)}, {k * n for k in range(6, 10) for n in range(11, 100)}),
    }
    for kind, (A, B) in ranges.items():
        if A & B:
            fails.append(f"{kind}: answer values possible in both halves: {sorted(A & B)[:10]}")
    # operator: operands 2-15 versus 25-99 are disjoint; answers can coincide, which the specification does not forbid
    # for operands, so report it for the record rather than fail.
    def op_vals(lo, hi, amin, amax):
        s = set()
        for a in range(lo, hi + 1):
            for b in range(lo, hi + 1):
                for v in (2 * a + b, a + 2 * b, 3 * a - b, 2 * a - b + 1):
                    if amin <= v <= amax:
                        s.add(v)
        return s
    op_shared = op_vals(2, 15, 10, 45) & op_vals(25, 99, 100, 999)
    if op_shared:
        fails.append(f"operator: answer values possible in both halves: {sorted(op_shared)[:10]}")
    # words that sit in two lists cross the halves through the other list
    cols = set(L["colours"])
    opp_words = {w for p in L["opposites"] for w in (p["a"], p["b"])}
    cross = [w for w in L["words3"] if w in cols or w in opp_words]
    if cross:
        fails.append(f"words3 entries that are also colours or opposites: {cross}")

    def load(d, name):
        p = os.path.join(d, name)
        return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

    for label, d, other in (("pilot", a.pilot, "B"), ("test", a.test, "A")):
        if not d:
            continue
        other_h = halves(L["countries"])[other]
        bad_caps = {c["capital"] for c in other_h}
        bad_words = set(halves(L["words3"])[other])
        for f in ("pairs.jsonl", "donor_only.jsonl"):
            for p in load(d, f):
                for t in ("P", "R"):
                    for c in p[t]["candidates"]:
                        if c in bad_caps or c in bad_words:
                            fails.append(f"{label} {f} {p['id']}: candidate {c!r} from the other half")

    report = {"fails": fails, "operator_answer_values_shared_between_ranges": len(op_shared)}
    print(json.dumps(report, indent=1))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
