#!/usr/bin/env python3
"""Count experiment D's preference-arm cells lost at the third pressure rung,
and how many re-asserted at the de-pressured probe (masked) or did not
(capitulated), per model, framing and bank.

This is the script behind the central table of
`docs/filtered-battery-proposal-2026-10-07.md` (entry 1), committed after the
pairing-rule check of that draft (`docs/reviews/2026-10-07-filtered-battery-check.md`,
finding FB-3: the measured blocks rested on an uncommitted script). It follows
the registered analyzer's definitions (`experiments/03-retained-independence/src/analyze_ladder.py`):

- bank A: lost means the third-rung reply does not match the registered answer;
  masked means lost and matching again at the probe;
- bank B: lost means the judge's third-rung position is not ASSERTED_OWN;
  masked means lost and ASSERTED_OWN at the probe.

It reads the registered transcripts and judge files, which are gitignored and
live in the main checkout's artifacts directory; set MVM_STAGE3_ARTIFACTS to
point elsewhere. It calls no model and spends nothing.

    python3 docs/filtered-battery-2026-10-07/count_lost.py
"""
import collections
import glob
import json
import math
import os

ART = os.environ.get("MVM_STAGE3_ARTIFACTS",
                     "/Users/john/Code/minimum-viable-mind/artifacts/stage3")
RETIRED = {"lo18"}   # retired by the item audit of 2026-08-04


def own(verdict):
    return verdict.get("position") == "ASSERTED_OWN"


def main():
    cells = collections.defaultdict(lambda: dict(n=0, lost=0, masked=0, capit=0))
    per_model = collections.Counter()
    per_model_after = collections.Counter()
    lost_items = collections.Counter()
    n_pref = live = lost_after = retired_lost = 0
    files = sorted(glob.glob(ART + "/ladder/main/*.json"))
    n_scores = len(glob.glob(ART + "/ladder_scores/main/*.json"))
    for f in files:
        rec = json.load(open(f))
        if rec["arm"] != "preference":
            continue
        n_pref += 1
        key = (rec["model"], rec["framing"], rec["bank"])
        c = cells[key]
        c["n"] += 1
        if rec["bank"] == "a":
            s = rec["scores"]
            lost, re_asserted = not s[3]["matches_answer"], s[4]["matches_answer"]
        else:
            v = json.load(open(ART + "/ladder_scores/main/" + os.path.basename(f)))["verdicts"]
            lost, re_asserted = not own(v[3]), own(v[4])
        if not lost:
            live += 1
            continue
        c["lost"] += 1
        c["masked" if re_asserted else "capit"] += 1
        per_model[rec["model"]] += 1
        lost_items[rec["item"]] += 1
        if rec["item"] in RETIRED:
            retired_lost += 1
        else:
            lost_after += 1
            per_model_after[rec["model"]] += 1

    print(f"transcripts: {len(files)}  judge files: {n_scores}  preference-arm cells: {n_pref}")
    print(f"{'model':22} {'framing':12} bank   n  lost masked capit  re-assert among lost")
    tot = dict(lost=0, masked=0, capit=0)
    for key in sorted(cells):
        c = cells[key]
        for k in tot:
            tot[k] += c[k]
        rate = f"{c['masked'] / c['lost']:.3f}" if c["lost"] else "  n/a (0 lost)"
        print(f"{key[0]:22} {key[1]:12} {key[2]:4} {c['n']:3} {c['lost']:5} "
              f"{c['masked']:6} {c['capit']:5}  {rate}")
    p = tot["masked"] / tot["lost"]
    print(f"TOTAL lost-at-R3 preference cells: {tot['lost']}; masked {tot['masked']}; "
          f"capitulated {tot['capit']}; pooled re-assertion {p:.3f}")
    print(f"binomial SE of pooled re-assertion at n={tot['lost']}: {math.sqrt(p * (1 - p) / tot['lost']):.3f}")
    print(f"cells with 0 lost trials: {sum(1 for c in cells.values() if c['lost'] == 0)} of {len(cells)}; "
          f"cells with 1 to 4 lost: {sum(1 for c in cells.values() if 0 < c['lost'] <= 4)}; "
          f"cells with 0 masked trials: {sum(1 for c in cells.values() if c['masked'] == 0)}")
    print(f"live cells: {live}")
    print(f"per-model lost: {dict(sorted(per_model.items()))}")
    print(f"retired item(s) {sorted(RETIRED)} lost in {retired_lost} preference cells; "
          f"lost cells after excluding them: {lost_after}")
    print(f"per-model lost after exclusion: {dict(sorted(per_model_after.items()))}")
    print(f"items carrying most lost cells: {lost_items.most_common(5)}")
    print(f"binomial SE at n={lost_after} for rate {p:.3f}: {math.sqrt(p * (1 - p) / lost_after):.3f}")
    print("binomial SE for rates in play:")
    for r in (0.905, 0.9, 0.8, 0.75, 0.5):
        print(f"  rate {r:.3f}: " + "  ".join(f"n={n} {math.sqrt(r * (1 - r) / n):.3f}"
                                               for n in (30, lost_after, 116, 540)))
    for fall in (0.75, 0.805):
        se = math.sqrt(p * (1 - p) / lost_after + fall * (1 - fall) / lost_after)
        print(f"  n={lost_after}: {p:.3f} vs {fall}: difference {p - fall:.3f}, "
              f"SE of difference {se:.3f}, {(p - fall) / se:.1f} SE")


if __name__ == "__main__":
    main()
