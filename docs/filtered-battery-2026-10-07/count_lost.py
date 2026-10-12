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
    n_pref = live = lost_after = retired_lost = masked_after = 0
    n_after = live_after = n_after_b = 0
    e2 = collections.defaultdict(lambda: [0, 0])   # entry 2 own arm: [cells, live]
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
        retired = rec["item"] in RETIRED
        if not retired:
            n_after += 1
            n_after_b += rec["bank"] == "b"
        if rec["bank"] == "a":
            s = rec["scores"]
            lost, re_asserted = not s[3]["matches_answer"], s[4]["matches_answer"]
        else:
            v = json.load(open(ART + "/ladder_scores/main/" + os.path.basename(f)))["verdicts"]
            lost, re_asserted = not own(v[3]), own(v[4])
        if rec["bank"] == "b" and rec["framing"] == "tool" and not retired:
            e2[rec["model"]][0] += 1
            e2[rec["model"]][1] += not lost
        if not lost:
            live += 1
            live_after += not retired
            continue
        c["lost"] += 1
        c["masked" if re_asserted else "capit"] += 1
        per_model[rec["model"]] += 1
        lost_items[rec["item"]] += 1
        if rec["item"] in RETIRED:
            retired_lost += 1
        else:
            lost_after += 1
            masked_after += re_asserted
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
    print(f"preference cells after excluding the retired item: {n_after} "
          f"(bank B {n_after_b}); live among them: {live_after}")
    print(f"items carrying most lost cells: {lost_items.most_common(5)}")
    print(f"binomial SE at n={lost_after} for rate {p:.3f}: {math.sqrt(p * (1 - p) / lost_after):.3f}")
    # Added 2026-10-09 after the third check (findings FB3-1, FB3-2, FB3-4, FB3-8):
    # the full-transcript rate over the 107 cells the new arms actually use,
    # what that leaves reachable, and entry 2's own-arm rates on its 29 items.
    q = masked_after / lost_after
    se_q = math.sqrt(q * (1 - q) / lost_after)
    print(f"full-transcript re-assertion over the {lost_after} cells without the retired item: "
          f"{masked_after} of {lost_after} = {q:.3f}; capitulated {lost_after - masked_after}")
    print(f"binomial SE at n={lost_after} for rate {q:.3f}: {se_q:.3f}")
    print(f"largest reachable r_S minus r_F (r_S cannot exceed 1.0): {1 - q:.3f}")
    print(f"r_S needed for the lookup reading (r_F minus r_S at least 0.10): at most {q - 0.10:.3f}")
    print(f"if r_S is 1.0: r_F minus r_S = {q - 1:+.3f}, 95 percent interval about "
          f"{q - 1 - 1.96 * se_q:+.3f} to {q - 1 + 1.96 * se_q:+.3f}")
    n2 = sum(v[0] for v in e2.values()); l2 = sum(v[1] for v in e2.values())
    p2 = l2 / n2
    print(f"entry 2 own arm (bank B, tool framing, retired item excluded): n={n2}, "
          f"live at third rung={l2}, pooled own rate={p2:.3f}")
    for m in sorted(e2):
        c, l = e2[m]
        print(f"  {m}: {l}/{c} = {l / c:.3f}, room for the other arm to sit below it {l / c:.3f}")
    se2 = math.sqrt(2 * p2 * (1 - p2) / n2)
    print(f"SE of own minus other at n={n2} per arm, both rates near {p2:.3f}: {se2:.3f}; "
          f"95 percent half-width about {1.96 * se2:.3f}")
    print(f"entry 2: an interval lies wholly inside plus or minus 0.20 only if the difference "
          f"is within about {0.20 - 1.96 * se2:.3f} of zero; inside plus or minus 0.10 never "
          f"(half-width {1.96 * se2:.3f} exceeds 0.10)")
    print("binomial SE for rates in play:")
    for r in (0.944, 0.905, 0.9, 0.8, 0.75, 0.5):
        print(f"  rate {r:.3f}: " + "  ".join(f"n={n} {math.sqrt(r * (1 - r) / n):.3f}"
                                               for n in (30, lost_after, 116, 540)))
    for fall in (0.75, 0.805):
        se = math.sqrt(p * (1 - p) / lost_after + fall * (1 - fall) / lost_after)
        print(f"  n={lost_after}: {p:.3f} vs {fall}: difference {p - fall:.3f}, "
              f"SE of difference {se:.3f}, {(p - fall) / se:.1f} SE")
    for fall in (0.75, round(q - 0.10, 3)):
        se = math.sqrt(q * (1 - q) / lost_after + fall * (1 - fall) / lost_after)
        print(f"  n={lost_after}: {q:.3f} vs {fall}: difference {q - fall:.3f}, "
              f"SE of difference {se:.3f}, {(q - fall) / se:.1f} SE")


if __name__ == "__main__":
    main()
