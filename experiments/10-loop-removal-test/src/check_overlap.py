"""Sections 11 and 17 (item 10) of battery-authoring-spec.md: pilot and test are kept apart.

Run now on the lists and ranges; run again on a test set after registration:
    .venv/bin/python -I experiments/10-loop-removal-test/src/check_overlap.py [--pilot <dir>] [--test <dir>]
Exits non-zero on any failure.
"""
import argparse
import ast
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

    # answer values within each numeric kind: the split of section 17, item 4
    import split
    S = split.splits()
    for kind, v in S.items():
        if v["A"] & v["B"]:
            fails.append(f"{kind}: answer values in both halves: {sorted(v['A'] & v['B'])[:10]}")
        keysA = {it[0] for it in split.half_pool(kind, "A")}
        keysB = {it[0] for it in split.half_pool(kind, "B")}
        if keysA & keysB:
            fails.append(f"{kind}: items in both halves' pools: {sorted(keysA & keysB)[:5]}")
    op_shared = set()
    # words that sit in two lists cross the halves through the other list
    cols = set(L["colours"])
    opp_words = {w for p in L["opposites"] for w in (p["a"], p["b"])}
    cross = [w for w in L["words3"] if w in cols or w in opp_words]
    if cross:
        fails.append(f"words3 entries that are also colours or opposites: {cross}")

    def load(d, name):
        p = os.path.join(d, name)
        return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

    shape_index = {name: i for i, (name, _) in enumerate(split.OP_SHAPES)}
    for label, d, half, other in (("pilot", a.pilot, "A", "B"), ("test", a.test, "B", "A")):
        if not d:
            continue
        other_h = halves(L["countries"])[other]
        bad_caps = {c["capital"] for c in other_h}
        bad_words = set(halves(L["words3"])[other])
        bad_opp = {w for p in halves(L["opposites"])[other] for w in (p["a"], p["b"])}
        own = {k: v[half] for k, v in S.items()}
        for f in ("pairs.jsonl", "donor_only.jsonl", "bites.jsonl", "bites_donor_only.jsonl"):
            for p in load(d, f):
                for t in ("P", "R"):
                    if t not in p:
                        continue
                    kind = p["rule_kind"] if t == "P" else p["routine_kind"]
                    ans = p[t]["answer"]
                    # numeric right answers lie in the half's own values (section 17, item 10)
                    if kind in own and int(ans) not in own[kind]:
                        fails.append(f"{label} {f} {p['id']}: {kind} answer {ans} not in half {half}'s values")
                    # non-numeric candidates from the other half's pools; numeric wrong answers are exempt
                    for c in p[t]["candidates"]:
                        if not c.isdigit() and (c in bad_caps or c in bad_words or c in bad_opp):
                            fails.append(f"{label} {f} {p['id']}: candidate {c!r} from the other half")
                if p["rule_kind"] == "op":
                    _, _, name, x, y = ast.literal_eval(p["rule_content"])
                    if (shape_index[name], x, y) not in {it[0] for it in split.half_pool("op", half)}:
                        fails.append(f"{label} {f} {p['id']}: operator content outside half {half}'s pool")

    report = {"fails": fails, "split_seeds": {k: v["report"]["seed"] for k, v in S.items()}}
    print(json.dumps(report, indent=1))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
