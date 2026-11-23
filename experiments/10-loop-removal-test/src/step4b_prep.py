"""Step 4b, preparation on the Mac (free): token ids for the baseline variants, which the pilot stores as text.

    .venv/bin/python -I src/step4b_prep.py --pilot batteries/pilot-v0.12 --tokdir <dir>

Writes baseline_ids.jsonl into the pilot folder: for each scored pair, the ids of
- P without its rule ("the rule is needed"),
- P with only its rule, facts and question (the mirror check),
- R with only its routine fact and question ("the rule does not get in the way"),
each rendered exactly as the generator renders an item (chat template, reasoning "none", the reply opening).
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import Model  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot", required=True)
    ap.add_argument("--tokdir", required=True)
    a = ap.parse_args()
    m = Model(a.tokdir)
    out = []
    for line in open(os.path.join(a.pilot, "pairs.jsonl")):
        p = json.loads(line)
        # a check that the stored ids are what this renderer makes
        assert m.ids(m.render(p["P"]["text"])) == p["P"]["prompt_ids"], p["id"]
        out.append({"id": p["id"],
                    "P_without_rule": m.ids(m.render(p["P"]["without_rule"])),
                    "P_baseline": m.ids(m.render(p["P"]["baseline_variant"])),
                    "R_baseline": m.ids(m.render(p["R"]["baseline_variant"]))})
    with open(os.path.join(a.pilot, "baseline_ids.jsonl"), "w") as f:
        for x in out:
            f.write(json.dumps(x) + "\n")
    print(f"{len(out)} pairs written")


if __name__ == "__main__":
    main()
