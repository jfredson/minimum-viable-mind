"""Closure check of the fatal finding RT-237: the main line's OWN gate code,
run on the twelve committed toy models, so that the code's figures for the
ownership-free line come from the code under check and not from a copied
record. Then its fields are compared with the independent recount
(`recount_from_models.json`, written by `recount_from_models.py`) and judged
by the decision code (`measure.seed_gate`).

This is the one script here that imports the code under check, on purpose.
It writes `code_gate_on_toy.json`: the gate field of each row, as
`procedure.gate` writes it (a checker's record, not a registered row).

    ~/Code/minimum-viable-mind/.venv/bin/python \
        docs/reviews/2026-10-09-rt237-closure-check-scripts/code_gate_on_toy.py
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "experiments/08-successor-degree/src"))
import measure as MS    # noqa: E402
import procedure as P   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.join(ROOT, "experiments/rehearsal-successor-measure/out-repairs/models")


def main():
    data = P.EvalData(1.0)
    mine = json.load(open(os.path.join(HERE, "recount_from_models.json")))
    out, bad = {}, 0
    keys = ("own_correct", "other_correct", "lesioned_own_correct", "lesioned_other_correct",
            "lesioned_candidate_own_correct")
    for arm in ("T", "C", "M", "F"):
        for s in (0, 1, 2):
            m, _ = P.load_model(os.path.join(MODELS, f"ckpt_{arm}_base_seed{s}.pt"), arm, "toy")
            g = P.gate(m, arm, data)
            g.pop("route_in_use", None)      # the in-use check is not part of this closure
            g.pop("own_by_route", None)
            out[f"{arm}/{s}"] = g
            diff = [k for k in keys if g[k] != mine[f"{arm}/{s}"][k]]
            bad += bool(diff)
            sg = MS.seed_gate(g, arm)
            print(f"{arm}/{s}: code writes lesioned_candidate_own_correct={g['lesioned_candidate_own_correct']}, "
                  f"lesioned_candidate_other_correct={g['lesioned_candidate_other_correct']}, "
                  f"ownership_free_line={g['ownership_free_line']}, bar={g['bar']}; "
                  f"independent recount {'same on all five counts' if not diff else 'DIFFERENT on ' + str(diff)}; "
                  f"decision code's clause states {sg['checks']}")
    json.dump(out, open(os.path.join(HERE, "code_gate_on_toy.json"), "w"), indent=1, sort_keys=True)
    print("RESULT:", "the code's counts equal the independent recount on every model" if bad == 0
          else f"{bad} models DIFFERENT")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
