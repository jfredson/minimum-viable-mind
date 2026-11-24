"""The split of the numeric kinds between halves: battery-authoring-spec.md, section 17, item 4.

Model-free. For each numeric kind it deals the answer values decade by decade between halves A and B, then
checks the tolerances on each half's pool of items, trying split seeds from 1 upward.

    python -I split.py        # prints the seeds and every figure
"""
import json
import random

# Specification, section 19, item 1: single-step shapes, each with one written constant (design version 0.14).
OP_SHAPES = [("a plus b, plus 3", lambda a, b: a + b + 3), ("a plus b, plus 5", lambda a, b: a + b + 5),
             ("a plus b, plus 7", lambda a, b: a + b + 7), ("a plus b, minus 2", lambda a, b: a + b - 2)]
KINDS = ("op", "unit", "sum", "prod")
MAX_SEED = 1000


def two_digit(v):
    return 10 <= v <= 99


def pool(kind):
    """Every item of the kind: (key, answer, operands, fact or None)."""
    items = []
    if kind == "op":
        for s, (_, f) in enumerate(OP_SHAPES):
            for a in range(2, 16):
                for b in range(2, 16):
                    v = f(a, b)
                    if two_digit(v):
                        items.append(((s, a, b), v, (a, b), None))
    elif kind == "unit":
        for k in range(2, 10):
            for n in range(2, 13):
                if two_digit(k * n):
                    items.append(((k, n), k * n, (k, n), tuple(sorted((k, n)))))
    elif kind == "sum":
        for a in range(2, 50):
            for b in range(a, 50):
                if two_digit(a + b):
                    items.append(((a, b), a + b, (a, b), None))
    elif kind == "prod":
        allp = {x * y for x in range(2, 13) for y in range(2, 13)}
        for a in range(2, 13):
            for b in range(a, 13):
                v = a * b
                # section 18, item 1: an item that can fill no place is left out (only 99 = 9 x 11)
                near = [x for x in allp if x != v and len(str(x)) == len(str(v)) and abs(x - v) <= 12]
                if two_digit(v) and len(near) >= 4:
                    items.append(((a, b), v, (a, b), (a, b)))
    return items


def deal(values, seed):
    """Item 4, 'The value split': returns the set of values in half A."""
    rng = random.Random(seed)
    A = set()
    zero_to_A = rng.random() < 0.5
    for d in range(1, 10):
        dec = sorted(v for v in values if v // 10 == d)
        if not dec:
            continue
        r0 = [v for v in dec if v % 10 == 0]
        r5 = [v for v in dec if v % 10 == 5]
        if r0 and r5:
            (A.add(r0[0]) if zero_to_A else A.add(r5[0]))
        elif r0 or r5:
            if zero_to_A:
                A.add((r0 or r5)[0])
        zero_to_A = not zero_to_A
        for grp in ([v for v in dec if v % 2 == 0 and v % 5 != 0], [v for v in dec if v % 2 == 1 and v % 5 != 0]):
            rng.shuffle(grp)
            first_A = rng.random() < 0.5
            for i, v in enumerate(grp):
                if (i % 2 == 0) == first_A:
                    A.add(v)
    return A


def figures(items):
    n = len(items)
    ops = [o for it in items for o in it[2]]
    facts = {it[3] for it in items if it[3] is not None}
    return {"items": n, "share_end0": sum(it[1] % 10 == 0 for it in items) / n,
            "share_end5": sum(it[1] % 10 == 5 for it in items) / n,
            "mean_answer": sum(it[1] for it in items) / n,
            "share_even_operands": sum(o % 2 == 0 for o in ops) / len(ops), "facts": len(facts)}


def check(kind, figA, figB):
    ok = {"end0": abs(figA["share_end0"] - figB["share_end0"]) <= 0.05,
          "end5": abs(figA["share_end5"] - figB["share_end5"]) <= 0.05,
          "mean": abs(figA["mean_answer"] - figB["mean_answer"]) <= 2,
          "even_operands": abs(figA["share_even_operands"] - figB["share_even_operands"]) <= 0.05}
    if kind in ("unit", "prod"):
        lo, hi = sorted((figA["facts"], figB["facts"]))
        ok["facts"] = lo >= 0.8 * hi
    return ok


def split_for(kind, seed):
    items = pool(kind)
    A = deal({it[1] for it in items}, seed)
    pa = [it for it in items if it[1] in A]
    pb = [it for it in items if it[1] not in A]
    return A, pa, pb


def choose(kind):
    """Item 4, 'The seed rule'. Returns (seed, values in A, values in B, report) or raises."""
    for seed in range(1, MAX_SEED + 1):
        A, pa, pb = split_for(kind, seed)
        if not pa or not pb:
            continue
        fa, fb = figures(pa), figures(pb)
        ok = check(kind, fa, fb)
        if all(ok.values()):
            values = {it[1] for it in pool(kind)}
            return seed, A, values - A, {"seed": seed, "half_A_pool": fa, "half_B_pool": fb, "tolerances_met": ok,
                                         "values_A": sorted(A), "values_B": sorted(values - A)}
    raise RuntimeError(f"{kind}: no split seed up to {MAX_SEED} meets the tolerances; the design returns to John")


_CACHE = {}


def splits():
    """{kind: {"A": set, "B": set, "report": dict}} for every numeric kind; computed once."""
    if not _CACHE:
        for k in KINDS:
            seed, A, B, rep = choose(k)
            _CACHE[k] = {"A": A, "B": B, "report": rep}
    return _CACHE


def half_pool(kind, half):
    S = splits()[kind][half]
    return [it for it in pool(kind) if it[1] in S]


if __name__ == "__main__":
    print(json.dumps({k: v["report"] for k, v in splits().items()}, indent=1, default=str))
