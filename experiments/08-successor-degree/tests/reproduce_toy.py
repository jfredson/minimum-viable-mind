"""Test T3 of `docs/successor-code-freeze-method-2026-10-04.md`: the frozen
procedure, run on the twelve committed toy models, against the committed toy
figures.

    python tests/reproduce_toy.py --mode committed-reads --out DIR   # T3a: has a pass line
    python tests/reproduce_toy.py --mode fresh-fit --out DIR         # T3b: differences reported

T3a takes the straight-line reads from the files the controls re-run used and
must reproduce, to the printed precision, what was committed in
`experiments/rehearsal-successor-measure/out-controls-rerun/`,
`out-short-prestated-run/`, `out-control-2-twenty-draws/` and
`out-v3-rules/gate.json`. T3b fits the reads once on the processor, as the
registered run will, and reports every difference from the committed figures
with no pass line.

Laptop, processor, $0. Writes into DIR and prints a comparison; the
comparison is also written to DIR/comparison.json.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src")
sys.path.insert(0, SRC)
import numpy as np          # noqa: E402
import measure as MS        # noqa: E402
import procedure as P       # noqa: E402

REH = os.path.abspath(os.path.join(HERE, "..", "..", "rehearsal-successor-measure"))
MODELS = os.path.join(REH, "out-repairs", "models")
ARMS, SEEDS = ("T", "C", "M", "F"), (0, 1, 2)     # arm T first: the rider reads its site set
TOL = 5e-5          # "to the printed precision": every committed share is printed to four places


def load(*p):
    with open(os.path.join(REH, *p)) as f:
        return json.load(f)


def sha_ok(arm, seed):
    want = dict(reversed(line.split()) for line in open(os.path.join(MODELS, "SHA256SUMS")))
    path = os.path.join(MODELS, f"ckpt_{arm}_base_seed{seed}.pt")
    return hashlib.sha256(open(path, "rb").read()).hexdigest() == want[os.path.basename(path)], path


def close(a, b):
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool):
        return bool(a) == bool(b)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) <= TOL
    return a == b


def compare(arm, seed, row, results):
    m = load("out-controls-rerun", f"measure_{arm}_seed{seed}.json")
    n = load("out-controls-rerun", f"nominate_{arm}_seed{seed}.json")
    pa = load("out-short-prestated-run", "part_a.json")["models"][f"{arm}/{seed}"]
    pb = load("out-short-prestated-run", "part_b.json")["models"][f"{arm}/{seed}"]
    g = load("out-v3-rules", "gate.json")["runs"][f"{arm}/{seed}"]
    key = f"{arm}/{seed}"
    out = []

    def eq(name, ours, theirs):
        out.append(dict(model=key, field=name, ours=ours, committed=theirs, equal=close(ours, theirs)))

    eq("gate own correct", row["gate"]["own_correct"], g["own_correct"])
    eq("gate named-other correct", row["gate"]["other_correct"], g["other_correct"])
    eq("nomination status", row["nomination_status"], n["primary"]["status"])
    ours_s, theirs_s = row["nomination"]["primary"]["site_set"], n["primary"]["site_set"]
    for f in ("layers", "positions", "rank", "piece_correct", "whole_read_correct"):
        eq(f"site set: {f}", None if ours_s is None else ours_s[f], None if theirs_s is None else theirs_s[f])
    ours_st, theirs_st = row["nomination"]["stricter"]["site_set"], n["stricter"]["site_set"]
    eq("stricter site set", None if ours_st is None else [ours_st["layers"], ours_st["positions"], ours_st["rank"]],
       None if theirs_st is None else [theirs_st["layers"], theirs_st["positions"], theirs_st["rank"]])
    eq("whole-read counts at every state", [row["fits"][str(l)]["whole"] for l in range(5)],
       [n["fits"][str(l)]["whole"] for l in range(5)])
    eq("piece counts at every state and size",
       [[row["fits"][str(l)]["piece"][str(r)] if str(r) in row["fits"][str(l)]["piece"]
         else row["fits"][str(l)]["piece"][r] for r in (1, 2, 4, 8)] for l in range(5)],
       [[n["fits"][str(l)]["piece"][str(r)] for r in (1, 2, 4, 8)] for l in range(5)])
    p, q = row.get("primary"), m.get("primary")
    eq("a reading was computed", p is not None, q is not None)
    if p and q:
        for f in ("accuracy_whole", "accuracy_ownership_only", "accuracy_untouched", "degree"):
            eq(f"reading: {f}", p["reading"][f], q["reading"][f])
        eq("described only", p["described_only"], q["described_only"])
        eq("no-transplant rate", p["no_transplant"]["rate"], q["no_transplant"]["rate"])
        eq("no-transplant inside allowance", p["no_transplant"]["inside_allowance"], q["no_transplant"]["inside_allowance"])
        eq("control 1 complement share", p["controls"]["1"]["complement_donor_share"], q["controls"]["1"]["complement_donor_share"])
        if arm == "T":
            eq("control 1 holds on arm T", p["controls"]["1"]["holds"], q["controls"]["1"]["holds_on_arm_T"])
        for f in ("median", "p95", "below", "equal", "above"):
            eq(f"control 3 {f}", p["controls"]["3"][f], q["controls"]["3"][f])
        for f in ("same_value_trials", "different_value_trials", "same_value_moved", "different_value_moved"):
            eq(f"control 6 {f}", p["controls"]["6"][f], q["controls"]["6"][f])
        eq("control 7 holds", p["controls"]["7"]["holds"], q["controls"]["7"]["bit_identical"])
        for f, h in (("holds", "holds"), ("donor_value_share", "donor_value_share"),
                     ("trials_whose_action_changed", "trials_whose_action_changed"),
                     ("twins_states_identical_at_the_sites", "twins_states_identical_at_the_sites")):
            eq(f"control 4 (redefined) {f}", p["controls"]["4"][h], pa[h])
        if "true_slot" in q:
            eq("true-slot reading", p["true_slot"]["reading"]["degree"], q["true_slot"]["reading"]["degree"])
            if "route_formula" in q["true_slot"]:
                eq("route formula", p["true_slot"]["route_formula"], q["true_slot"]["route_formula"])
        pe = p["piece_elsewhere"]
        eq("piece and whole at the action position", pe["at_the_action_position"], pb["at_the_action_position"])
        eq("piece and whole at each other position",
           [(e["position"], e["whole"], e["piece"]) for e in pe["other_positions"]],
           [(e["position"], e["whole"], e["piece"]) for e in pb["other_positions"]])
        eq("piece and whole on the average over the other positions",
           pe["mean_over_the_other_positions"], pb["mean_over_the_other_positions"])
        if "rider_at_arm_T_site_set" in m:
            eq("rider reading", row.get("rider_at_arm_T_site_set", {}).get("reading", {}).get("degree"),
               m["rider_at_arm_T_site_set"]["reading"]["degree"])
    if m.get("stricter") and row.get("stricter"):
        eq("stricter reading", row["stricter"]["reading"]["degree"], m["stricter"]["reading"]["degree"])
    eq("control 2 status", row["control2"]["status"], m["control2"]["status"])
    if "candidates" in m["control2"]:
        eq("control 2 candidates", [(c["layers"], c["positions"], c["rank"], c["piece_correct"])
                                    for c in row["control2"].get("candidates", [])],
           [(c["layers"], c["positions"], c["rank"], c["piece_correct"]) for c in m["control2"]["candidates"]])
    results.extend(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("committed-reads", "fresh-fit"), required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--shuffles", type=int, default=None)
    ap.add_argument("--reuse", action="store_true",
                    help="reuse rows this test already wrote in --out (they are deterministic)")
    a = ap.parse_args()
    shuffles = a.shuffles if a.shuffles is not None else (0 if a.mode == "committed-reads" else MS.N_SHUFFLES)
    data = P.EvalData(1.0)
    results, rows = [], {}
    for arm in ARMS:
        for seed in SEEDS:
            ok, path = sha_ok(arm, seed)
            assert ok, f"{path} does not match SHA256SUMS: stop"
            reads = (os.path.join(REH, "out-repairs", f"reads_{arm}_base_seed{seed}.npz")
                     if a.mode == "committed-reads" else None)
            done = os.path.join(a.out, f"row_{arm}_seed{seed}.json")
            if a.reuse and os.path.exists(done):
                rows[(arm, seed)] = json.load(open(done))      # a row already written by this test
                print(f"[{arm}/{seed}] reusing the row this test already wrote", flush=True)
            else:
                rows[(arm, seed)] = P.run_model(path, a.out, arm, "toy", seed, reads, shuffles, 1.0, False, data)
            compare(arm, seed, rows[(arm, seed)], results)
    # control 2 against twenty random pieces, arm F seed 0, piece rule switched off (NOT A RESULT)
    m, _ = P.load_model(os.path.join(MODELS, "ckpt_F_base_seed0.pt"), "F", "toy")
    reads = P.load_reads(os.path.join(a.out, "reads_F_seed0.npz"))
    fam, _ = P.check_family(5)
    c2 = P.control2(m, "F", 0, reads, data, rows[("F", 0)]["gate"]["other_correct"], 790, fam, 0)
    ref = load("out-control-2-twenty-draws", "code_test_NOT_A_RESULT.json")["returned"]
    for f in ("own_directed_moved", "named_other_moved", "trials"):
        results.append(dict(model="F/0 control 2, piece rule off", field=f, ours=c2.get(f),
                            committed=ref.get(f), equal=close(c2.get(f), ref.get(f))))
    results.append(dict(model="F/0 control 2, piece rule off", field="site set",
                        ours=c2.get("site_set", {}).get("layers"), committed=ref["site_set"]["layers"],
                        equal=c2.get("site_set", {}).get("layers") == ref["site_set"]["layers"]))
    for f in ("median", "p95", "below", "equal", "above"):
        results.append(dict(model="F/0 control 2, piece rule off", field=f"random pieces {f}",
                            ours=c2.get("random_pieces", {}).get(f), committed=ref["random_pieces"][f],
                            equal=close(c2.get("random_pieces", {}).get(f), ref["random_pieces"][f])))
    # the summary: separation and outcome
    summ = P.summarise(a.out)
    sep_ref = load("out-controls-rerun", "summary.json")["separation"]
    for s in SEEDS:
        ours = None
        if summ["per_seed"]["C"][s]["status"] == "reading" and summ["per_seed"]["T"][s]["status"] == "reading":
            ours = summ["per_seed"]["C"][s]["degree"] - summ["per_seed"]["T"][s]["degree"]
        results.append(dict(model=f"seed {s}", field="arm C minus arm T", ours=ours,
                            committed=sep_ref[str(s)]["C_minus_T"],
                            equal=close(ours, sep_ref[str(s)]["C_minus_T"])))
    # Reported, not part of the pass line (the method note's T3a list does not
    # include it): version 4, section 3, says the toy lands on the fifth term,
    # while its rules applied as written give R3, because arm F fails its gate
    # on two seeds of three. The findings report it for the registration text.
    reported = dict(model="all", field="outcome term (reported; not part of the pass line)",
                    ours=summ["outcome"]["term"],
                    version_4_section_3_says="metric validated, degree not read: (reason)",
                    gates=summ["gates"])
    bad = [r for r in results if not r["equal"]]
    with open(os.path.join(a.out, "comparison.json"), "w") as f:
        json.dump(dict(mode=a.mode, compared=len(results), differ=len(bad), results=results,
                       outcome_reported=reported), f,
                  indent=1, default=P._json_default)
    print(f"\n{a.mode}: {len(results)} figures compared, {len(bad)} differ")
    for r in bad:
        print(f"  DIFFERS {r['model']} {r['field']}: ours {r['ours']} committed {r['committed']}")
    print(f"outcome, reported and not part of the pass line: {summ['outcome']['term']} "
          f"(gates: {summ['gates']}); version 4 section 3 describes the toy as the fifth term")
    if a.mode == "committed-reads":
        print("T3a " + ("PASSES" if not bad else "FAILS"))
        raise SystemExit(0 if not bad else 1)


if __name__ == "__main__":
    main()
