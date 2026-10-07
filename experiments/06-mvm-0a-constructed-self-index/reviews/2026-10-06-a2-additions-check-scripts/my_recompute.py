"""My own recompute of the made-up cases' outcomes, written from the ruling
text (2026-10-06 rulings: page 1, the ownership-free line; pages 5 and 9, the
outcome table and its precedence; page 7, the seed rule; page 8, the
no-transplant check does not withhold; follow-up items 2 and 7, the scope
phrases). It does NOT import measure.py or procedure.py, and it does not
import the earlier check's recompute.py. It imports only tests/a2_cases.py,
for the edits each case makes to the toy records (the input under test).

    python my_recompute.py              # all rules on
    python my_recompute.py --sweep      # each rule off in turn, and the R3 condition/seed lists

Rule switches (names): c7, c1T, c4, fresh, dev, nomination, descr, noreading,
gate_own, gate_other, collapse, line, seedrule, s5a, nostep, sep.
"""
import copy, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
EXP = os.path.join(REPO, "experiments", "08-successor-degree")
sys.path.insert(0, os.path.join(EXP, "tests"))
import a2_cases as K  # case definitions only

TOY = os.path.join(EXP, "out-freeze-tests", "t3a-committed-reads")
OWNERSHIP_FREE_LINE = 1546   # page 1: 1,546 of 3,000
SEPARATION = 0.5             # arm C's lowest minus arm T's highest
RULES = ["c7", "c1T", "c4", "fresh", "dev", "nomination", "descr", "noreading",
         "gate_own", "gate_other", "collapse", "line", "seedrule", "s5a", "nostep", "sep"]


def load():
    rows, sums = {}, {}
    for f in sorted(os.listdir(TOY)):
        if f.startswith("row_") and f.endswith(".json"):
            b = open(os.path.join(TOY, f), "rb").read()
            sums[f] = hashlib.sha256(b).hexdigest()
            r = json.loads(b)
            rows[(r["arm"], r["seed"])] = r
    return rows, sums


def learning_failures(arm, row, off):
    """Gate on learning, from the counts (not the stored true/false flags).
    Own-directed for every arm; named-other too on arm F (page 1)."""
    g, out = row["gate"], []
    if "gate_own" not in off and g["own_correct"] < g["bar"]:
        out.append("own-directed")
    if arm == "F" and "gate_other" not in off and g["other_correct"] < g["bar"]:
        out.append("named-other")
    return out


def other_failures(arm, row, off):
    """Every other gate condition and every check that withholds (page 7)."""
    g, bad = row["gate"], []
    if arm == "F":   # the channel-removal check, arm F only
        if "collapse" not in off and not g["lesioned_own_correct"] < g["bar"]:
            bad.append("collapse")
        c = g.get("lesioned_candidate_own_correct")    # absent: not evaluable, counts against (stop S8)
        if "line" not in off and (c is None or c < OWNERSHIP_FREE_LINE):
            bad.append("ownership-free line")
    if "nomination" not in off and row.get("nomination_status") != "nominated":
        bad.append("nomination")
    p = row.get("primary") or {}
    if "descr" not in off and p.get("described_only", True):
        bad.append("description only")
    r = p.get("reading")
    if r is None:
        if "noreading" not in off:
            bad.append("no reading")
        return bad
    if "fresh" not in off and r.get("floor", {}).get("clears") is not True:
        bad.append("fresh floor")
    if "dev" not in off and p.get("dev_floor_clears") is not True:
        bad.append("development floor")
    ctl = p.get("controls", {})
    holds = lambda k: (ctl.get(k) or {}).get("holds") is True   # absent = not run = counts against
    if "c7" not in off and not holds("7"):
        bad.append("control 7")
    if arm == "T" and "c1T" not in off and not holds("1"):
        bad.append("control 1")
    if "c4" not in off and not holds("4"):
        bad.append("control 4")
    return bad      # page 8: the no-transplant rate withholds nothing


def arm(arm_name, rows, off):
    seeds = {s: rows[(arm_name, s)] for s in (0, 1, 2) if (arm_name, s) in rows}
    lf = {s: learning_failures(arm_name, r, off) for s, r in seeds.items()}
    of = {s: other_failures(arm_name, r, off) for s, r in seeds.items()}
    learned = [s for s in seeds if not lf[s]]
    if "seedrule" in off:
        # the closed rule: each condition counted separately, two of three
        gate_ok = len(learned) >= 2
        reads = gate_ok and len([s for s in seeds if not of[s]]) >= 2
        counted = [s for s in seeds if not of[s]]
    else:
        counted = [s for s in seeds if not lf[s] and not of[s]]
        gate_ok = len(learned) >= 2
        reads = len(counted) >= 2
    degs = [seeds[s]["primary"]["reading"]["degree"] for s in counted]
    by_cond = {}
    for s in sorted(seeds):
        for c in lf[s]:
            by_cond.setdefault(c, []).append(s)
    return dict(gate_ok=gate_ok, learned=learned, reads=reads, degs=degs,
                learn_fail_by_condition=by_cond, lf=lf, of=of)


def outcome(rows, steps, off=frozenset()):
    A = {a: arm(a, rows, off) for a in "TCMF" if any(k[0] == a for k in rows)}
    s5a = (steps or {}).get("arm_F_step_5a_seed")
    F = A.get("F")
    # pages 5 and 9: arm F failing at step 5a (after its re-run) is R3, stop S4
    if "s5a" not in off and F and s5a is not None and F["lf"].get(s5a):
        return dict(code="R3", r3=[("F", {c: [s5a] for c in F["lf"][s5a]})])
    failed = [a for a in "TC" if a not in A or not A[a]["gate_ok"]]
    # no record that arm F passed at step 5a, and arm F fails its gate: R3
    if "nostep" not in off and F and not F["gate_ok"] and s5a is None:
        failed.append("F")
    if failed:
        return dict(code="R3", r3=[(a, A[a]["learn_fail_by_condition"] if a in A else "no records") for a in failed])
    T, C = A["T"], A["C"]
    f_reads = bool(F and F["gate_ok"] and F["reads"])
    if not T["reads"]:
        return dict(code="not_validated")
    if not C["reads"]:
        return dict(code="fallback_read" if f_reads else "fallback_not_read")
    if "sep" not in off and min(C["degs"]) - max(T["degs"]) < SEPARATION:
        return dict(code="R2")
    return dict(code="R1" if f_reads else "fifth")


def run(off=frozenset()):
    toy, sums = load()
    res = {}
    for i, case in enumerate(K.CASES, 1):
        rows = copy.deepcopy(toy)
        case["build"](rows)
        o = outcome(rows, case["steps"], off)
        res[case["name"]] = dict(n=i, expect=case["expect"], **o)
    return res, sums


def main():
    base, sums = run()
    if "--sweep" not in sys.argv:
        print(json.dumps(dict(input_sha256=sums, outcomes=base), indent=1, default=list))
        return
    print("base: " + ", ".join(f"{v['n']} {k}={v['code']}" for k, v in base.items()))
    agree = [k for k, v in base.items() if v["code"] == v["expect"]]
    print(f"agree with written expectation: {len(agree)} of {len(base)}")
    print("\nR3 sentences, condition and seeds from the records:")
    for k, v in base.items():
        if v["code"] == "R3":
            print(f"  {v['n']} {k}: {v['r3']}")
    print("\nEach rule turned off in turn (case number, name, outcome with rule on -> off):")
    for rule in RULES:
        res, _ = run(frozenset([rule]))
        ch = [f"{res[k]['n']} {k}: {base[k]['code']} -> {res[k]['code']}"
              for k in base if res[k]["code"] != base[k]["code"]]
        print(f"  {rule:11s} " + ("; ".join(ch) if ch else "NO CASE CHANGES"))


if __name__ == "__main__":
    main()
