"""Page 4 toy re-run: the reproduction checks, and the old run against the new.

UNREGISTERED rehearsal code. NOT A RESULT about the scientific question.
Method, committed before anything was run:
`docs/2026-10-06-page4-toy-rerun-1800-method.md`, sections 4 to 6.

    cd experiments/rehearsal-successor-measure/src
    ~/Code/minimum-viable-mind/.venv/bin/python page4_compare.py

Reads (all relative to the repository):
  old, twelve models  experiments/08-successor-degree/out-freeze-tests/t3b-fresh-fit/   (420 fitted)
  old, solver         experiments/rehearsal-successor-measure/out-competing-solver-run/ (420 fitted)
  new                 experiments/rehearsal-successor-measure/out-page4-rerun-1800/{models,solver}-{420,1800}/
Writes out-page4-rerun-1800/comparison.json and comparison.md, and prints both checks.
"""
from __future__ import annotations

import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REH = os.path.abspath(os.path.join(HERE, ".."))
OLD_M = os.path.abspath(os.path.join(REH, "..", "08-successor-degree", "out-freeze-tests", "t3b-fresh-fit"))
OLD_S = os.path.join(REH, "out-competing-solver-run")
NEW = os.path.join(REH, "out-page4-rerun-1800")
ARMS, SEEDS = ("T", "C", "M", "F"), (0, 1, 2)
READINGS = ("channel_removed", "channel_left_on")
VOLATILE = {"seconds", "checkpoint", "versions", "page4", "torch"}   # timing, paths, library list, this run's own note


def load(*p):
    with open(os.path.join(*p)) as f:
        return json.load(f)


def leaves(a, b, path=""):
    """Every leaf of two JSON values, compared exactly; volatile keys skipped."""
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            if k in VOLATILE:
                continue
            if k not in a or k not in b:
                out.append((f"{path}/{k}", a.get(k, "<missing>"), b.get(k, "<missing>"), False))
            else:
                out += leaves(a[k], b[k], f"{path}/{k}")
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [(path, f"list of {len(a)}", f"list of {len(b)}", False)]
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out += leaves(x, y, f"{path}[{i}]")
        return out
    return [(path, a, b, a == b)]


def reproduction(kind):
    """Section 4: the 420 output of this run's code against the committed one."""
    res = []
    if kind == "models":
        d = os.path.join(NEW, "models-420")
        for arm in ARMS:
            for s in SEEDS:
                f = f"row_{arm}_seed{s}.json"
                res += [(f + p, x, y, e) for p, x, y, e in leaves(load(d, f), load(OLD_M, f))]
                za, zb = np.load(os.path.join(d, f"reads_{arm}_seed{s}.npz")), np.load(os.path.join(OLD_M, f"reads_{arm}_seed{s}.npz"))
                for k in sorted(set(za.files) | set(zb.files)):
                    eq = k in za.files and k in zb.files and np.array_equal(za[k], zb[k])
                    res.append((f"reads_{arm}_seed{s}.npz:{k}", "array", "array", eq))
    else:
        d = os.path.join(NEW, "solver-420")
        for f in sorted(os.listdir(OLD_S)):
            if f.endswith(".json"):
                res += [(f + p, x, y, e) for p, x, y, e in leaves(load(d, f), load(OLD_S, f))]
            elif f.endswith(".npz"):
                za, zb = np.load(os.path.join(d, f)), np.load(os.path.join(OLD_S, f))
                for k in sorted(set(za.files) | set(zb.files)):
                    eq = k in za.files and k in zb.files and np.array_equal(za[k], zb[k])
                    res.append((f"{f}:{k}", "array", "array", eq))
            elif f == "table.md":
                eq = open(os.path.join(d, f)).read() == open(os.path.join(OLD_S, f)).read()
                res.append((f, "text", "text", eq))
    return res


def best_piece(row):
    return max(max(v["piece"].values()) for v in row["fits"].values())


def model_line(row):
    p = row.get("primary") or {}
    s = row["nomination"]["primary"]["site_set"] or (p.get("site_set") if p else None)
    c = p.get("controls", {})
    return dict(
        status=row["nomination_status"],
        site_set=None if s is None else [s["layers"], s["positions"], s["rank"]],
        piece_correct=None if s is None else s["piece_correct"],
        whole_read_correct=None if s is None else s["whole_read_correct"],
        reading=(p.get("reading") or {}).get("degree"),
        described_only=p.get("described_only"),
        control1_complement=c.get("1", {}).get("complement_donor_share"),
        control1_holds=c.get("1", {}).get("holds"),
        control3_below_equal_above=None if "3" not in c else [c["3"]["below"], c["3"]["equal"], c["3"]["above"]],
        control4_holds=c.get("4", {}).get("holds"),
        control7_holds=c.get("7", {}).get("holds"),
        true_slot=(p.get("true_slot") or {}).get("reading", {}).get("degree"),
        rider=(row.get("rider_at_arm_T_site_set") or {}).get("reading", {}).get("degree"),
        stricter=None if not row["nomination"]["stricter"]["site_set"] else
        [row["nomination"]["stricter"]["site_set"][k] for k in ("layers", "positions", "rank", "piece_correct")],
        best_piece_anywhere=best_piece(row),
        control2=row["control2"]["status"])


def fmt(x):
    if x is None:
        return "—"
    if isinstance(x, float):
        return f"{x:.4f}"
    if isinstance(x, list) and len(x) == 3 and isinstance(x[0], list):
        return f"states {tuple(x[0])} at {x[1]}, {x[2]} directions"
    return str(x)


def main():
    import sys
    only = "--reproduction-only" in sys.argv
    out = {}
    lines = ["# Page 4 toy re-run: comparison (written by page4_compare.py)", ""]
    # ---- reproduction checks (section 4)
    for kind in ("models", "solver"):
        r = reproduction(kind)
        bad = [x for x in r if not x[3]]
        out[f"reproduction_{kind}"] = dict(compared=len(r), differ=len(bad),
                                           differences=[dict(field=f, ours=a, committed=b) for f, a, b, _ in bad])
        verdict = "PASSES" if not bad else "FAILS"
        msg = f"reproduction check, {kind} at 420 fitted: {len(r)} values compared, {len(bad)} differ: {verdict}"
        print(msg)
        lines += [f"- {msg}"]
        for f, a, b, _ in bad[:40]:
            print(f"   DIFFERS {f}: ours {a} committed {b}")
            lines.append(f"   - DIFFERS `{f}`: ours {a}, committed {b}")
    lines.append("")
    if only:
        failed = any(out[k]["differ"] for k in out)
        print("stop: a reproduction check failed; the 1,800 run is not made" if failed else "both reproduction checks pass")
        raise SystemExit(1 if failed else 0)
    # ---- old against new, twelve models (section 5)
    new_d = os.path.join(NEW, "models-1800")
    rows = {}
    lines += ["## The twelve toy models: fitted on 420 (old) against 1,800 (new)", "",
              "| model | field | old, 420 fitted | new, 1,800 fitted | same? |", "|---|---|---|---|---|"]
    for arm in ARMS:
        for s in SEEDS:
            o = model_line(load(OLD_M, f"row_{arm}_seed{s}.json"))
            n = model_line(load(new_d, f"row_{arm}_seed{s}.json"))
            rows[f"{arm}/{s}"] = dict(old=o, new=n)
            for k in o:
                lines.append(f"| {arm}/{s} | {k} | {fmt(o[k])} | {fmt(n[k])} | {'yes' if o[k] == n[k] else '**no**'} |")
    out["models"] = rows
    so, sn = load(OLD_M, "summary.json"), load(new_d, "summary.json")
    sep = {}
    for s in SEEDS:
        def d(S):
            ps = S["per_seed"]
            c, t = ps["C"][str(s)], ps["T"][str(s)]
            both = c["status"] == "reading" and t["status"] == "reading"
            return c["degree"] - t["degree"] if both else None
        sep[s] = dict(old=d(so), new=d(sn))
    out["separation_C_minus_T"] = sep
    out["outcome"] = dict(old=so.get("outcome"), new=sn.get("outcome"), gates_old=so["gates"], gates_new=sn["gates"])
    lines += ["", "| seed | separation, arm C minus arm T: old | new |", "|---|---|---|"]
    lines += [f"| {s} | {fmt(v['old'])} | {fmt(v['new'])} |" for s, v in sep.items()]
    lines += ["", f"Outcome term, old: {so.get('outcome', {}).get('term')}; new: {sn.get('outcome', {}).get('term')}. "
              f"Gates old {so['gates']}, new {sn['gates']}.", ""]
    # ---- the solver
    sv = {}
    lines += ["## The competing solver: fitted on 420 (old) against 1,800 (new)", "",
              "| reading / seed | old: best piece of 180, nomination, status | new: best piece of 180, nomination, status |",
              "|---|---|---|"]
    for rd in READINGS:
        for s in SEEDS:
            def one(d):
                nm = load(d, f"nominate_blind_seed{s}_{rd}.json")
                me = load(d, f"measure_blind_seed{s}_{rd}.json")
                return dict(best_piece=nm["best_piece_correct"], nomination=nm["primary"]["status"],
                            status=me["status"], reading_returned=me["a_reading_was_returned"])
            o, n = one(OLD_S), one(os.path.join(NEW, "solver-1800"))
            sv[f"{rd}/{s}"] = dict(old=o, new=n)
            lines.append(f"| {rd} / {s} | {o['best_piece']}, {o['nomination']}, {o['status']} | "
                         f"{n['best_piece']}, {n['nomination']}, {n['status']} |")
    out["solver"] = sv
    # ---- the pre-stated concerns (section 6), checked mechanically
    N = {k: v["new"] for k, v in rows.items()}
    concerns = {
        "A: a built model (arm T, C or M) loses its nomination":
            [k for k, v in N.items() if k[0] in "TCM" and v["status"] != "nominated"],
        "B: arm T's reading is not 0.0000, or its control 1 does not hold":
            [k for k, v in N.items() if k[0] == "T" and (v["reading"] != 0.0 or v["control1_holds"] is not True)],
        "C: the separation (arm C minus arm T) is below 0.5 or missing on a seed":
            [s for s, v in sep.items() if v["new"] is None or v["new"] < 0.5],
        "D: arm M's reading is outside 0.3 to 0.7 on a seed":
            [k for k, v in N.items() if k[0] == "M" and (v["reading"] is None or not 0.3 <= v["reading"] <= 0.7)],
        "E: the free model's read reaches the floor (a piece of 144 or more anywhere)":
            [k for k, v in N.items() if k[0] == "F" and (v["status"] == "nominated" or v["best_piece_anywhere"] >= 144)],
        "F: the solver returns a reading":
            [k for k, v in sv.items() if v["new"]["reading_returned"]],
        "G: control 7 or control 4 fails anywhere":
            [k for k, v in N.items() if v["control7_holds"] is False or v["control4_holds"] is False],
    }
    changed_site = [k for k, v in rows.items() if v["old"]["site_set"] != v["new"]["site_set"]]
    out["concerns"] = concerns
    out["site_set_or_size_changed_on"] = changed_site
    lines += ["", "## The pre-stated concerns (method, section 6)", ""]
    for k, v in concerns.items():
        lines.append(f"- {k}: {'**YES** on ' + ', '.join(map(str, v)) if v else 'no'}")
    lines.append(f"- Reported, not a concern on its own: the chosen site set or size changed on "
                 f"{', '.join(changed_site) if changed_site else 'no model'}")
    with open(os.path.join(NEW, "comparison.json"), "w") as f:
        json.dump(out, f, indent=1, sort_keys=True, default=str)
    with open(os.path.join(NEW, "comparison.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines[lines.index("## The pre-stated concerns (method, section 6)"):]))


if __name__ == "__main__":
    main()
