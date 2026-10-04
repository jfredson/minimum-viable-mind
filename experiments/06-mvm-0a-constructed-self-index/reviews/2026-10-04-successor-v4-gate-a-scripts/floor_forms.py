"""Gate A tier 1: version 4, section 6.4 item 1 (lines 1120 to 1125) says the
two forms of the whole-state floor (the chance-corrected form that is
registered, and the plain form printed beside it) "on the toy ... never" disagree.
Count disagreements in every committed grid that records both. Reads files only.
"""
import glob
import json

B = "experiments/rehearsal-successor-measure/"


def rows(x):
    if isinstance(x, dict):
        if "clears" in x and "clears_plain_form" in x:
            yield x
        for v in x.values():
            yield from rows(v)
    elif isinstance(x, list):
        for v in x:
            yield from rows(v)


for pat in ("out-repairs/nominate_base_*.json", "out-repairs/measure_base_*.json",
            "out-v3-rules/nominate_*.json", "out-v3-rules/measure_*.json",
            "out-controls-rerun/nominate_*.json", "out-controls-rerun/measure_*.json",
            "out-grammar-c/nominate_base_F_T_C.json", "out-grammar-c/measure_base_F_T_C.json",
            "out-grammar-c/outcomes.json",
            "out-competing-solver-run/nominate_*.json"):
    n = d = 0
    for f in sorted(glob.glob(B + pat)):
        for r in rows(json.load(open(f))):
            n += 1
            d += r["clears"] != r["clears_plain_form"]
    print(f"{pat:<45} floor records {n:>6}; the two forms disagree on {d}")
