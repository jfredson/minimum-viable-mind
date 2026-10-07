"""Independent recompute of the A2 cases' outcomes, written from the ruling
text (2026-10-06 rulings, pages 1, 5, 7, 8, 9 and addendum; the adopted drafted
texts RT-241, A10, A9, RT-237). Does NOT import measure.py or procedure.py.
It imports only a2_cases.py, for the case definitions (the edits to the toy
rows), which is the input under test, not the logic.

Usage: python recompute.py [veto_off ...]
"""
import copy, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
EXP = os.path.join(REPO, "experiments", "08-successor-degree")
sys.path.insert(0, os.path.join(EXP, "tests"))
import a2_cases as K  # case definitions only

TOY = os.path.join(EXP, "out-freeze-tests", "t3a-committed-reads")
LINE = 1546          # page 1: 1,546 of 3,000
SEP = 0.5            # separation bar
OFF = set(sys.argv[1:])


def load():
    rows, sums = {}, {}
    for f in sorted(os.listdir(TOY)):
        if f.startswith("row_") and f.endswith(".json"):
            b = open(os.path.join(TOY, f), "rb").read()
            sums[f] = hashlib.sha256(b).hexdigest()
            r = json.loads(b)
            rows[(r["arm"], r["seed"])] = r
    return rows, sums


def learns(arm, row):
    if "gate" in OFF:
        return True
    g = row["gate"]
    ok = g["own_correct"] >= g["bar"]
    if arm == "F":
        ok = ok and g["other_correct"] >= g["bar"]
    return ok


def channel_removal(arm, row):
    """Arm F only (page 1 and RT-220): collapse below the bar, and the
    ownership-free line; absent field = not evaluable = fails (stop S8)."""
    if arm != "F":
        return []
    g, bad = row["gate"], []
    if "collapse" not in OFF and not g["lesioned_own_correct"] < g["bar"]:
        bad.append("collapse")
    c = g.get("lesioned_candidate_own_correct")
    if "line" not in OFF and (c is None or c < LINE):
        bad.append("line")
    return bad


def withholds(arm, row):
    bad = []
    if "piece" not in OFF and row.get("nomination_status") != "nominated":
        bad.append("nomination")
    p = row.get("primary") or {}
    if p.get("described_only", True) and "piece" not in OFF:
        bad.append("described only")
    r = p.get("reading")
    if r is None:
        bad.append("no reading")
        return bad
    if "fresh" not in OFF and not r.get("floor", {}).get("clears"):
        bad.append("fresh floor")
    if "dev" not in OFF and not p.get("dev_floor_clears"):
        bad.append("dev floor")
    c = p.get("controls", {})
    def holds(k):
        return c.get(k, {}).get("holds") is True
    if "c7" not in OFF and not holds("7"):
        bad.append("control 7")
    if arm == "T" and "c1" not in OFF and not holds("1"):
        bad.append("control 1")
    if "c4" not in OFF and not holds("4"):
        bad.append("control 4")
    # page 8: no-transplant check withholds nothing (deliberately absent)
    if "notransplant_on" in OFF and not p.get("no_transplant", {}).get("inside_allowance", True):
        bad.append("no-transplant")
    return bad


def arm_state(arm, rows):
    seeds = {s: rows[(arm, s)] for s in (0, 1, 2) if (arm, s) in rows}
    if not seeds:
        return None
    learn = {s: learns(arm, r) for s, r in seeds.items()}
    reasons = {s: ([] if learn[s] else ["gate"]) + channel_removal(arm, r) + withholds(arm, r)
               for s, r in seeds.items()}
    if "seedrule" in OFF:
        # the frozen rule page 7 closed: the arm's gate and each channel-removal
        # condition counted separately on two of three seeds; a seed reads if it
        # passes the withholding checks alone
        gate2 = sum(learn.values()) >= 2
        cr_ok = all(sum(c in channel_removal(arm, r) for r in seeds.values()) < 2
                    for c in ("collapse", "line"))
        counting = [s for s, r in seeds.items() if not withholds(arm, r)]
        reads = gate2 and cr_ok and len(counting) >= 2
    else:
        counting = [s for s in seeds if not reasons[s]]
        reads = len(counting) >= 2
    gate_ok = sum(learn.values()) >= 2
    degs = [seeds[s]["primary"]["reading"]["degree"] for s in counting]
    return dict(gate_ok=gate_ok, learn=learn, reads=reads, degs=degs, reasons=reasons)


def outcome(rows, steps):
    A = {a: arm_state(a, rows) for a in "TCMF"}
    F = A["F"]
    s5a = (steps or {}).get("arm_F_step_5a_seed")
    # stop S4: arm F failing at step 5a is R3, nothing else launches
    if F is not None and s5a is not None and not F["learn"].get(s5a, False):
        return "R3"
    for a in "TC":
        if A[a] is None or not A[a]["gate_ok"]:
            return "R3"
    if F is not None and not F["gate_ok"] and s5a is None:
        return "R3"          # author's reading 2: no record of a step 5a pass
    T, C = A["T"], A["C"]
    if not T["reads"]:
        return "not_validated"
    f_reads = F is not None and F["gate_ok"] and F["reads"]
    if not C["reads"]:
        return "fallback_read" if f_reads else "fallback_not_read"
    if min(C["degs"]) - max(T["degs"]) < SEP:
        return "R2"
    return "R1" if f_reads else "fifth"


def main():
    toy, sums = load()
    out = {}
    for case in K.CASES:
        rows = copy.deepcopy(toy)
        case["build"](rows)
        out[case["name"]] = outcome(rows, case["steps"])
    print(json.dumps(dict(off=sorted(OFF), sums=sums, outcomes=out), indent=1))


if __name__ == "__main__":
    main()
