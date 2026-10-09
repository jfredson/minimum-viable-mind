"""Checker's look at every reading the branch's rows computed, not only the nominated one:
the nominated (primary), stricter and sensitivity rows, and the nomination's whole search
on development pairs (every site set and size). Also the unaltered arm T model's search at
state 0, the action position (page 4 re-run under the ruled code), for comparison.
Run from the root of a checkout of branch decoy-test-w18."""
import json

OUT = "experiments/08-successor-degree/out-decoy-w18"
REF = "experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000"


def grid(r):
    return [(c["layers"], c["positions"], c["rank"], 1 - c["dev_ownership_only"] / c["dev_whole"])
            for c in r["nomination"]["candidates"] if c["dev_whole"]]


for v in ("V1", "V2", "V3", "V4", "V5"):
    for s in range(3):
        r = json.load(open(f"{OUT}/{v}/row_T_seed{s}.json"))
        g = grid(r)
        print(f"{v} seed {s}: nominated {r['primary']['reading']['degree']:.4f}, "
              f"stricter {r['stricter']['reading']['degree']:.4f}, "
              f"sensitivity {r['sensitivity']['reading']['degree']:.4f}, "
              f"control 1 {r['primary']['controls']['1']['complement_donor_share']:.4f}; "
              f"highest in the search on development pairs {max(x[3] for x in g):.3f}")
for s in range(3):
    r = json.load(open(f"{REF}/row_T_seed{s}.json"))
    at = {x[2]: round(x[3], 3) for x in grid(r) if x[0] == [0] and x[1] == "action"}
    print(f"unaltered arm T seed {s}, state 0 at the action, development pairs, reading by size: {at}")
