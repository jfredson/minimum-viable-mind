"""Print every number the findings document reports, from the committed
result files. Reads only; computes nothing new.

    ../../../.venv/bin/python summarize.py
"""
from __future__ import annotations

import numpy as np

import arms as A
import rehearse as R


def line(t):
    print(f"\n--- {t} " + "-" * max(0, 68 - len(t)))


def main():
    g = R.load_json("gate.json")
    line("learn-both gate (held-out), and the acting-channel lesion")
    for k, v in g["learn_both"].items():
        les = g["lesion"][k]
        print(f"  {k:6s} own {v['own']:.4f}  named-other {v['other']:.4f}   "
              f"lesioned: own {les['own']:.4f} named-other {les['other']:.4f}  "
              f"(n={v['n']})")
    line("the competing solvers, measured")
    for k, v in g["solvers"].items():
        print(f"  {k}: own {v['own']:.4f}  named-other {v['other']:.4f}")
    print(f"  references: guessing {g['reference_points']['guessing over the eight value slots']:.4f}, "
          f"whose-value-blind {g['reference_points']['a solver that cannot tell whose value it needs']:.4f}")

    n = R.load_json("nominate.json")
    line("blind nomination: the procedure AS PRE-STATED against the repaired one")
    for k, v in n["arms"].items():
        b, p = v["nomination"], v["nomination_within_the_pre_stated_family"]
        print(f"  {k:6s} pre-stated family best: ownership-only "
              f"{p['accuracy_ownership_only']:.4f} (label {p['label']}, rank {p['rank']}, "
              f"{p['positions']}, layers {p['layers']}, whole {p['accuracy_whole']:.4f})")
        print(f"         widened family best:    ownership-only "
              f"{b['accuracy_ownership_only']:.4f} (label {b['label']}, rank {b['rank']}, "
              f"{b['positions']}, layers {b['layers']}, whole {b['accuracy_whole']:.4f})")
    line("how well each reading of the read's label FITS, at the action position")
    for k, v in n["arms"].items():
        fa = v["fit_accuracy"]
        top = {lab: max(fa[x] for x in fa if x.startswith(lab))
               for lab in R.READ_LABELS}
        print(f"  {k:6s} " + "  ".join(f"{lab} {top[lab]:.3f}" for lab in R.READ_LABELS))
    line("whole-state transplant against site set (arm T seed 0), the floor curve")
    grid = n["arms"]["T/0"]["grid"]
    seen = {}
    for row in grid:
        key = (tuple(row["layers"]), row["positions"])
        seen[key] = row["accuracy_whole"]
    for (layers, pos), w in sorted(seen.items(), key=lambda kv: (len(kv[0][0]), kv[0][1])):
        print(f"  layers {str(list(layers)):16s} at {pos:14s} whole {w:.4f}")

    t = R.load_json("transplant.json")
    line("the reading on fresh episodes, both candidate forms")
    for k, v in t["arms"].items():
        r = v["readings"]["0.30"]
        reg, cor = r["registered"], r["floor_corrected"]
        print(f"  {k:6s} untouched {v['accuracy_untouched']:.4f}  "
              f"whole {v['accuracy_whole']:.4f}  ownership-only "
              f"{v['accuracy_ownership_only']:.4f}")
        print(f"         registered form: {reg['status']}"
              + (f" degree {reg['degree']:.4f}" if reg["degree"] is not None else "")
              + f"   floor-corrected: {cor['status']}"
              + (f" degree {cor['degree']:.4f}" if cor["degree"] is not None else ""))
    line("arm T under perfect nomination (its true ownership block)")
    for k, v in t["arm_T_oracle_nomination"].items():
        print(f"  {k}: ownership-only {v:.4f}")
    line("the seven controls")
    for k, v in t["arms"].items():
        print(f"  {k}:")
        for name, val in v["controls"].items():
            print(f"     {name}: {val}")
        break
    print("  (all arms and seeds in transplant.json; one shown here)")
    line("control 6 across every arm and seed")
    for k, v in t["arms"].items():
        c = v["controls"]
        print(f"  {k:6s} same-value cell {c['6a same-value cell: trials']} trials, "
              f"moved {c['6a same-value cell: share whose action moved']}; "
              f"different-value cell {c['6b different-value cell: trials']} trials, "
              f"moved {c['6b different-value cell: share whose action moved']}")

    o = R.load_json("outcomes.json")
    line("the made-up outcome cases")
    for k, v in o.items():
        if k.startswith("negative"):
            print(f"  negative: {v['found']} configurations found")
            for row in v["most_negative"][:3]:
                print(f"     arm {row['arm']} {row['sites']} label {row['label']} "
                      f"rank {row['rank']}: whole {row['accuracy_whole']:.4f} "
                      f"ownership-only {row['accuracy_ownership_only']:.4f} "
                      f"degree {row['degree']:.4f}")
            continue
        print(f"  {k}: whole {v['accuracy_whole']:.4f} ownership-only "
              f"{v['accuracy_ownership_only']:.4f} -> {v['status']}"
              + (f" degree {v['degree']:.4f}" if v["degree"] is not None else "")
              + f"  (expected {v['expected']})")

    u = R.load_json("uncertainty.json")
    line("the two candidate uncertainty methods, and the seeds each implies")
    for arm, v in u["arms"].items():
        a = v["across_seed_method"]
        w = v["within_seed_bootstrap"]
        print(f"  arm {arm}: raw difference per seed "
              f"{[round(x, 4) for x in v['per_seed_raw_difference']]}")
        print(f"     across-seed spread {a['standard_deviation']}, "
              f"typical within-seed spread {w['typical_standard_error']:.4f}")
        print(f"     seeds implied by half-width: {v['seeds_for_a_given_half_width']}")

    th = R.load_json("throughput.json")
    line("throughput, measured on this laptop")
    print(f"  device: {th['device']}")
    for arm in A.ARMS:
        r = th["registered_shape_on_this_laptop"][arm]
        print(f"  arm {arm} at the registered shape ({r['d_model']} wide, "
              f"{r['n_layers']} layers, {r['parameters']:,} parameters): "
              f"{r['seconds_per_step'] * 1000:.1f} ms/step "
              f"(median {r['median_seconds_per_step'] * 1000:.1f})")
    print(f"  ratios to the free arm: "
          + ", ".join(f"{k} {v:.3f}" for k, v in th["ratio_to_arm_F"].items()))
    line("the denominator checks")
    d1 = R.load_json("denominator_simulated.json")
    for k, v in d1["cases"].items():
        print(f"  {k:18s} whole {v['accuracy_whole']:.4f}: registered "
              f"{v['registered_mean']:.4f} (spread {v['registered_sd']:.4f}), "
              f"floor-corrected {v['floor_corrected_mean']:.4f} "
              f"(spread {v['floor_corrected_sd']:.4f})")
    print(f"  true share was {d1['true_outside_share']}; {d1['verdict']}")
    d3 = R.load_json("denominator_floor.json")
    print("  the no-transplant rate, measured against both predictions:")
    for k, v in d3["arms"].items():
        print(f"     {k:6s} measured {v['measured_untouched']:.4f}  "
              f"proposal says {d3['prediction_in_the_proposal']:.4f}  "
              f"the review's formula says {v['prediction_from_the_review']:.4f}")
    d4 = R.load_json("denominator_control6.json")
    print(f"  {d4['verdict']}")
    print(f"     distinctness kept: {d4['distinctness_preserving_grammar']['same_value_trials']} "
          f"same-value trials of {d4['distinctness_preserving_grammar']['trials']}")
    print(f"     distinctness relaxed: {d4['relaxed_grammar']['same_value_trials']} of "
          f"{d4['relaxed_grammar']['trials']}; blind solver moves from "
          f"{d4['relaxed_grammar']['blind_solver_on_the_strict_set']:.4f} to "
          f"{d4['relaxed_grammar']['blind_solver_on_the_relaxed_set']:.4f}")
    d2 = R.load_json("denominator_attenuated.json")
    line("attenuating the transplant: which form holds still")
    for k, v in d2["arms"].items():
        print(f"  {k:6s} whole-state accuracy across attenuation "
              f"{[round(r['accuracy_whole'], 3) for r in v['rows']]}")
        print(f"         registered form {[None if r['registered'] is None else round(r['registered'], 3) for r in v['rows']]}"
              f"  spans {v['registered_range']}")
        print(f"         floor-corrected {[None if r['floor_corrected'] is None else round(r['floor_corrected'], 3) for r in v['rows']]}"
              f"  spans {v['floor_corrected_range']}")


if __name__ == "__main__":
    main()
