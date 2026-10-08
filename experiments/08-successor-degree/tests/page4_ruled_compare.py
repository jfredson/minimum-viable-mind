"""The page 4 toy pass under the code ruled 2026-10-08: the reproduction
check (pass A against the checked 1,800-fitted record) and the old figures
against the new (pass B, the registered code at the 10,000 limit).

Method: `docs/2026-10-09-ruled-code-changes-and-page4-rerun-method.md`,
sections 3 to 5. NOT A RESULT. Reads only; writes the comparison files.

    python tests/page4_ruled_compare.py --reproduction     # pass A only
    python tests/page4_ruled_compare.py                    # everything

Old record: `experiments/rehearsal-successor-measure/out-page4-rerun-1800/`
(`models-1800/`, `solver-1800/`), the page 4 re-run of 2026-10-06, checked.
New: `out-ruled-code-changes/passA-limit3000/`, `passB-limit10000/`,
`solver-limit10000/`.
"""
from __future__ import annotations

import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OLD = os.path.abspath(os.path.join(ROOT, "..", "rehearsal-successor-measure", "out-page4-rerun-1800"))
OUT = os.path.join(ROOT, "out-ruled-code-changes")
A_DIR, B_DIR = os.path.join(OUT, "passA-limit3000"), os.path.join(OUT, "passB-limit10000")
SOLVER_NEW = os.path.join(OUT, "solver-limit10000")
ARMS, SEEDS = ("T", "C", "M", "F"), (0, 1, 2)
READINGS = ("channel_removed", "channel_left_on")
VOLATILE = {"seconds", "checkpoint", "versions", "page4", "torch"}


def load(*p):
    with open(os.path.join(*p)) as f:
        return json.load(f)


def leaves(a, b, path="", only=None):
    """Leaves present in both, compared exactly; keys in one only are listed apart."""
    only = [] if only is None else only
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            if k in VOLATILE:
                continue
            if k not in a or k not in b:
                only.append(f"{path}/{k} ({'new' if k in a else 'old'} only)")
                continue
            out += leaves(a[k], b[k], f"{path}/{k}", only)
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return [(path, f"list of {len(a)}", f"list of {len(b)}", False)]
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out += leaves(x, y, f"{path}[{i}]", only)
        return out
    return [(path, a, b, a == b)]


def warnings_in(path):
    return len(re.findall(r"failed to converge", open(path).read())) if os.path.exists(path) else None


def reproduction():
    res, only = [], []
    for arm in ARMS:
        for s in SEEDS:
            f = f"row_{arm}_seed{s}.json"
            res += [(f + p, x, y, e) for p, x, y, e in
                    leaves(load(A_DIR, f), load(OLD, "models-1800", f), "", only)]
            za = np.load(os.path.join(A_DIR, f"reads_{arm}_seed{s}.npz"))
            zb = np.load(os.path.join(OLD, "models-1800", f"reads_{arm}_seed{s}.npz"))
            for k in sorted(set(za.files) | set(zb.files)):
                eq = k in za.files and k in zb.files and np.array_equal(za[k], zb[k])
                res.append((f"reads_{arm}_seed{s}.npz:{k}", "array", "array", eq))
    warn = {f"{a}/{s}": dict(old=warnings_in(os.path.join(OLD, "models-1800", f"log_{a}_seed{s}.txt")),
                             new=warnings_in(os.path.join(A_DIR, f"log_{a}_seed{s}.txt")))
            for a in ARMS for s in SEEDS}
    return res, sorted({re.sub(r"^row_\w+_seed\d\.json", "", o) for o in only}), warn


def best_piece(fits):
    return max(max(v["piece"].values()) for v in fits.values())


def model_line(row):
    p = row.get("primary") or {}
    s = row["nomination"]["primary"]["site_set"]
    c = p.get("controls", {})
    rd = p.get("reading") or {}
    ts = (p.get("true_slot") or {}).get("reading", {}).get("degree")
    c2 = row["control2"]
    c2s = c2.get("site_set")
    nf = c2.get("named_read_fits")
    return dict(
        status=row["nomination_status"],
        site_set=None if s is None else [s["layers"], s["positions"], s["rank"]],
        piece_correct=None if s is None else s["piece_correct"],
        whole_read_correct=None if s is None else s["whole_read_correct"],
        reading=rd.get("degree"),
        untouched_whole_own_accuracy=None if not rd else [rd["accuracy_untouched"], rd["accuracy_whole"],
                                                           rd["arm_own_accuracy"]],
        control1_holds=c.get("1", {}).get("holds"),
        control4_holds=c.get("4", {}).get("holds"),
        control7_holds=c.get("7", {}).get("holds"),
        true_slot=ts,
        true_slot_distance=None if (ts is None or rd.get("degree") is None) else abs(rd["degree"] - ts),
        rider=(row.get("rider_at_arm_T_site_set") or {}).get("reading", {}).get("degree"),
        stricter=None if not row["nomination"]["stricter"]["site_set"] else
        [row["nomination"]["stricter"]["site_set"][k] for k in ("layers", "positions", "rank", "piece_correct")],
        stricter_reading=(row.get("stricter") or {}).get("reading", {}).get("degree"),
        best_piece_anywhere=best_piece(row["fits"]),
        grid_whole_and_best_piece=[[v["whole"], max(v["piece"].values())] for _, v in sorted(row["fits"].items())],
        piece_elsewhere_mean=((p.get("piece_elsewhere") or {}).get("mean_over_the_other_positions") or {}).get("piece"),
        control2=c2["status"],
        control2_named_best_piece=None if not nf else best_piece({str(k): v for k, v in nf.items()}),
        control2_site_set=None if not c2s else [c2s["layers"], c2s["positions"], c2s["rank"], c2s["piece_correct"]],
        control2_own_directed_moved=c2.get("own_directed_moved"),
        control2_random_median=(c2.get("random_pieces") or {}).get("median"))


def fmt(x):
    if x is None:
        return "—"
    if isinstance(x, float):
        return f"{x:.4f}"
    if isinstance(x, list) and len(x) == 3 and isinstance(x[0], list):
        return f"states {tuple(x[0])} at {x[1]}, {x[2]} directions"
    if isinstance(x, list) and x and isinstance(x[0], float):
        return ", ".join(f"{v:.4f}" for v in x)
    return str(x)


def main():
    lines = ["# Page 4 toy pass under the ruled code: comparison (written by tests/page4_ruled_compare.py)", ""]
    out = {}
    res, only, warn = reproduction()
    bad = [x for x in res if not x[3]]
    out["reproduction"] = dict(compared=len(res), differ=len(bad), only_in_one=only, warnings=warn,
                               differences=[dict(field=f, new=a, old=b) for f, a, b, _ in bad])
    wbad = [k for k, v in warn.items() if v["old"] != v["new"]]
    msg = (f"reproduction check, pass A (the ruled code, limit set back to 3,000) against the checked 1,800 record: "
           f"{len(res)} values compared, {len(bad)} differ; iteration-limit warnings equal on "
           f"{12 - len(wbad)} of 12 models: {'PASSES' if not bad and not wbad else 'FAILS'}")
    print(msg)
    lines += [f"- {msg}", f"- fields present in one record only (not compared): {', '.join(only) or 'none'}", ""]
    for f, a, b, _ in bad[:40]:
        print(f"   DIFFERS {f}: new {a} old {b}")
        lines.append(f"   - DIFFERS `{f}`: new {a}, old {b}")
    if "--reproduction" in sys.argv:
        with open(os.path.join(OUT, "reproduction.json"), "w") as f:
            json.dump(out, f, indent=1, sort_keys=True, default=str)
        raise SystemExit(1 if bad or wbad else 0)

    # ---- old (checked 1,800 record, limit 3,000) against new (pass B, limit 10,000)
    rows = {}
    lines += ["## The twelve toy models: limit 3,000 (old) against 10,000 (new), both fitted on 1,800", "",
              "| model | field | old | new | same? |", "|---|---|---|---|---|"]
    for arm in ARMS:
        for s in SEEDS:
            ro, rn = load(OLD, "models-1800", f"row_{arm}_seed{s}.json"), load(B_DIR, f"row_{arm}_seed{s}.json")
            o, n = model_line(ro), model_line(rn)
            rows[f"{arm}/{s}"] = dict(old=o, new=n, limit_hits=rn["fits_stopped_at_iteration_limit"],
                                      in_use=rn["gate"]["route_in_use"]["state"],
                                      row_choice=rn["gate"].get("row_choice"))
            for k in o:
                lines.append(f"| {arm}/{s} | {k} | {fmt(o[k])} | {fmt(n[k])} | {'yes' if o[k] == n[k] else '**no**'} |")
            za = np.load(os.path.join(OLD, "models-1800", f"reads_{arm}_seed{s}.npz"))
            zb = np.load(os.path.join(B_DIR, f"reads_{arm}_seed{s}.npz"))
            rows[f"{arm}/{s}"]["read_arrays_identical"] = all(np.array_equal(za[k], zb[k]) for k in za.files)
            rows[f"{arm}/{s}"]["read_arrays_largest_difference"] = max(
                float(np.abs(za[k] - zb[k]).max()) for k in za.files)
    out["models"] = rows

    def sep(which):
        C = [rows[f"C/{s}"][which]["reading"] for s in SEEDS]
        T = [rows[f"T/{s}"][which]["reading"] for s in SEEDS]
        if None in C or None in T:
            return None
        return min(C) - max(T)
    out["separation_lowest_C_minus_highest_T_from_the_rows"] = dict(old=sep("old"), new=sep("new"))
    sn = load(B_DIR, "summary.json")
    out["summary_new"] = dict(outcome=sn["outcome"], gates=sn["gates"],
                              per_seed={a: {s: dict(status=v["status"], reasons=v["reasons"])
                                            for s, v in d.items()} for a, d in sn["per_seed"].items()})
    lines += ["", f"Separation, lowest of arm C's readings minus highest of arm T's, from each row's arithmetic: "
              f"old {fmt(sep('old'))}, new {fmt(sep('new'))}.", "",
              f"Outcome under the current decision code (pass B's summary): {sn['outcome'].get('term')}", ""]

    # ---- warnings and limit hits
    lines += ["## Fits that stopped at the iteration limit", "",
              "| model | warnings, old (limit 3,000) | warnings, new (limit 10,000) | new, by kind (stopped / fits; most iterations) |",
              "|---|---|---|---|"]
    tot = {}
    for arm in ARMS:
        for s in SEEDS:
            wo = warnings_in(os.path.join(OLD, "models-1800", f"log_{arm}_seed{s}.txt"))
            wn = warnings_in(os.path.join(B_DIR, f"log_{arm}_seed{s}.txt"))
            hits = rows[f"{arm}/{s}"]["limit_hits"]
            t = tot.setdefault(arm, dict(old=0, new=0, new_counted=0))
            t["old"] += wo; t["new"] += wn; t["new_counted"] += hits["total"]
            kinds = "; ".join(f"{k}: {v['stopped_at_limit']} / {v['fits']}; {v['most_iterations']}"
                              for k, v in hits["by_kind"].items())
            lines.append(f"| {arm}/{s} | {wo} | {wn} | {kinds} |")
    out["warnings_by_arm"] = tot
    lines += ["", "| arm | old warnings | new warnings | new, counted in the rows |", "|---|---|---|---|"]
    lines += [f"| {a} | {v['old']} | {v['new']} | {v['new_counted']} |" for a, v in tot.items()]

    # ---- the solver
    sv = {}
    lines += ["", "## The competing solver: limit 3,000 (old) against 10,000 (new), both fitted on 1,800", "",
              "| reading / seed | old: best piece, nomination, status | new: best piece, nomination, status |",
              "|---|---|---|"]
    for rd in READINGS:
        for s in SEEDS:
            def one(d):
                nm = load(d, f"nominate_blind_seed{s}_{rd}.json")
                me = load(d, f"measure_blind_seed{s}_{rd}.json")
                return dict(best_piece=nm["best_piece_correct"], nomination=nm["primary"]["status"],
                            status=me["status"], reading_returned=me["a_reading_was_returned"])
            o, n = one(os.path.join(OLD, "solver-1800")), one(SOLVER_NEW)
            sv[f"{rd}/{s}"] = dict(old=o, new=n)
            lines.append(f"| {rd} / {s} | {o['best_piece']}, {o['nomination']}, {o['status']} | "
                         f"{n['best_piece']}, {n['nomination']}, {n['status']} |")
    out["solver"] = sv
    sw = dict(old=warnings_in(os.path.join(OLD, "log_solver_1800.txt")),
              new=warnings_in(os.path.join(OUT, "log_solver_limit10000.txt")))
    out["solver_warnings"] = sw
    lines.append(f"\nSolver warnings: old {sw['old']}, new {sw['new']}.")

    # ---- the pre-stated concerns (the page 4 method, section 6)
    N = {k: v["new"] for k, v in rows.items()}
    s_new = sep("new")
    concerns = {
        "A: a built model (arm T, C or M) loses its nomination":
            [k for k, v in N.items() if k[0] in "TCM" and v["status"] != "nominated"],
        "B: arm T's reading is not 0.0000, or its control 1 does not hold":
            [k for k, v in N.items() if k[0] == "T" and (v["reading"] != 0.0 or v["control1_holds"] is not True)],
        "C: the separation (arm C's lowest minus arm T's highest) is below 0.5 or missing":
            [] if (s_new is not None and s_new >= 0.5) else ["separation"],
        "D: arm M's reading is outside 0.3 to 0.7 on a seed":
            [k for k, v in N.items() if k[0] == "M" and (v["reading"] is None or not 0.3 <= v["reading"] <= 0.7)],
        "D2 (arm M's prediction): further than 0.10 from its true-slot reading on a seed":
            [k for k, v in N.items() if k[0] == "M" and (v["true_slot_distance"] is None or v["true_slot_distance"] > 0.10)],
        "E: the free model's read reaches the floor (a piece of 144 or more anywhere)":
            [k for k, v in N.items() if k[0] == "F" and (v["status"] == "nominated" or v["best_piece_anywhere"] >= 144)],
        "F: the solver returns a reading":
            [k for k, v in sv.items() if v["new"]["reading_returned"]],
        "G: control 7 or control 4 fails anywhere (the chosen, stricter and sensitivity rows)":
            [k for k, v in N.items() if v["control7_holds"] is False or v["control4_holds"] is False]
            + [f"{a}/{s} {w}" for a in ARMS for s in SEEDS for w in ("stricter", "sensitivity")
               if (load(B_DIR, f"row_{a}_seed{s}.json").get(w) or {}).get("controls")
               and any((load(B_DIR, f"row_{a}_seed{s}.json")[w]["controls"].get(c) or {}).get("holds") is False
                       for c in ("4", "7"))],
    }
    changed = {k: [f for f in v["old"] if v["old"][f] != v["new"][f]] for k, v in rows.items()}
    out["concerns"] = concerns
    out["fields_changed"] = changed
    lines += ["", "## The pre-stated concerns (page 4 method, section 6; this method, section 4)", ""]
    for k, v in concerns.items():
        lines.append(f"- {k}: {'**YES** on ' + ', '.join(map(str, v)) if v else 'no'}")
    lines.append("- Fields that changed, by model: " + "; ".join(
        f"{k}: {', '.join(v)}" for k, v in changed.items() if v) if any(changed.values()) else
        "- Fields that changed, by model: none")
    with open(os.path.join(OUT, "comparison.json"), "w") as f:
        json.dump(out, f, indent=1, sort_keys=True, default=str)
    with open(os.path.join(OUT, "comparison.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines[lines.index("## Fits that stopped at the iteration limit"):]))


if __name__ == "__main__":
    main()
