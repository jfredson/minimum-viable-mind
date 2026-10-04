"""Independent check of pull requests 88 and 89 (2026-10-04 check, Claude Code).

Written by the checking session, which wrote neither pull request. Reads the
COMMITTED outputs straight from git (the two branch tips), recomputes every
figure the findings and the pull-request descriptions state from the raw
fields, and does not call the checked code's own summary or floor functions
where the raw numbers allow an independent recount. Processor only; $0.

    cd <a checkout of this branch>
    .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/\
2026-10-04-competing-solver-and-control-2-check-scripts/independent_check.py

Needs the two branches fetched (origin/w2b-job1-competing-solver-run at
3d55865 and origin/w2b-job2-control-2-twenty-draws at c148bf1).
"""
import io
import json
import math
import subprocess
import sys
import zipfile

import numpy as np

SOLVER = "3d55865"
CONTROL = "c148bf1"
SO = "experiments/rehearsal-successor-measure/out-competing-solver-run/"
CO = "experiments/rehearsal-successor-measure/out-control-2-twenty-draws/"
READINGS = ("channel_removed", "channel_left_on")
SEEDS = (0, 1, 2)
FAILS = []


def show(rev, path, binary=False):
    out = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, check=True).stdout
    return out if binary else out.decode()


def j(rev, path):
    return json.loads(show(rev, path))


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAILS.append(name)


def wilson(k, n, z=1.96):
    # written out again here from the textbook form, not imported
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d * n, (c + h) / d * n


print("=== Pull request 88: the competing solver ===")
nom = {(r, s): j(SOLVER, f"{SO}nominate_blind_seed{s}_{r}.json") for r in READINGS for s in SEEDS}
mea = {(r, s): j(SOLVER, f"{SO}measure_blind_seed{s}_{r}.json") for r in READINGS for s in SEEDS}
summ = j(SOLVER, SO + "summary.json")

# 1. no verdict anywhere
check("no reading returned on any seed under either reading",
      all(not m["a_reading_was_returned"] and m["status"].startswith("no verdict") for m in mea.values()),
      "; ".join(f"{r}/{s}: {mea[(r, s)]['status']}" for r in READINGS for s in SEEDS))
check("the reason is 'no site set clears the whole-state floor' everywhere, stricter row too",
      all(n["primary"]["status"] == n["stricter"]["status"] == "no site set clears the whole-state floor"
          for n in nom.values()))
check("summary.json: stops B2, B3, B4 empty",
      summ["stop_B2_a_reading_was_returned_on"] == [] and summ["stop_B3_twins_not_identical_on"] == []
      and summ["stop_B4_null_transplant_differs_on"] == [])

# 2. the read: whole and piece counts, recounted from the fits
for r in READINGS:
    wh = [n["fits"][l]["whole"] for (rr, s), n in nom.items() if rr == r for l in n["fits"]]
    pc = [n["fits"][l]["piece"][k] for (rr, s), n in nom.items() if rr == r
          for l in n["fits"] for k in n["fits"][l]["piece"]]
    best = [max(n["fits"][l]["piece"][k] for l in n["fits"] for k in n["fits"][l]["piece"])
            for s in SEEDS for n in [nom[(r, s)]]]
    print(f"  {r}: whole read {min(wh)} to {max(wh)}; any piece {min(pc)} to {max(pc)}; best piece per seed {best}")
    check(f"{r}: best piece recount equals the file's best_piece_correct",
          best == [nom[(r, s)]["best_piece_correct"] for s in SEEDS])
allwh = [n["fits"][l]["whole"] for n in nom.values() for l in n["fits"]]
allbest = [n["best_piece_correct"] for n in nom.values()]
allpc = [v for n in nom.values() for l in n["fits"] for v in n["fits"][l]["piece"].values()]
check("whole read 11 to 21 of 180 (findings 1)", (min(allwh), max(allwh)) == (11, 21), f"{min(allwh)} to {max(allwh)}")
check("best piece 20 to 25 of 180 (findings 1; brief)", (min(allbest), max(allbest)) == (20, 25), f"{min(allbest)} to {max(allbest)}")
check("every count 9 to 25 (findings 3.4)", (min(min(allwh), min(allpc)), max(max(allwh), max(allpc))) == (9, 25),
      f"{min(min(allwh), min(allpc))} to {max(max(allwh), max(allpc))}")
check("piece rule asks for 144", all(n["piece_floor"] == 144 for n in nom.values()))
for (r, s), n in nom.items():
    lo, hi = wilson(n["best_piece_correct"], 180)
    b = n["best_piece_sampling_band"]
    check(f"{r}/{s}: sampling band {b[0]:.1f} to {b[1]:.1f} recomputed", abs(lo - b[0]) < 1e-9 and abs(hi - b[1]) < 1e-9)

# the findings' tables 3.1, row by row, against the files
want_A = {0: [(13, 13, 13, 13, 13), (16, 20, 23, 20, 11), (20, 17, 20, 24, 23), (19, 19, 12, 16, 17), (20, 14, 15, 21, 18)],
          1: [(13, 13, 13, 13, 13), (16, 12, 9, 19, 15), (11, 15, 23, 11, 14), (16, 11, 13, 11, 21), (15, 18, 15, 14, 10)],
          2: [(13, 14, 13, 13, 13), (13, 18, 16, 19, 17), (20, 22, 23, 16, 16), (21, 15, 18, 19, 20), (16, 14, 13, 17, 20)]}
want_B = {0: [(13, 13, 14, 14, 14), (16, 20, 23, 19, 11), (20, 17, 21, 25, 23), (20, 19, 12, 16, 18), (20, 13, 14, 22, 17)],
          1: [(13, 14, 13, 13, 13), (16, 12, 11, 17, 13), (12, 18, 20, 11, 11), (16, 11, 13, 10, 17), (15, 18, 14, 14, 10)],
          2: [(13, 14, 13, 13, 13), (14, 18, 18, 20, 17), (20, 19, 20, 16, 16), (20, 16, 17, 15, 21), (15, 14, 12, 18, 19)]}
for r, want in (("channel_removed", want_A), ("channel_left_on", want_B)):
    got = {s: [tuple([nom[(r, s)]["fits"][str(l)]["whole"]] + [nom[(r, s)]["fits"][str(l)]["piece"][str(k)] for k in (1, 2, 4, 8)])
               for l in range(5)] for s in SEEDS}
    check(f"findings table 3.1 ({r}) equals the files cell for cell", got == want)

# 3. the gate
gb = j(SOLVER, "experiments/rehearsal-successor-measure/out-repairs/gate_base.json")
committed = [(gb["runs"][f"blind/base/{s}"]["own_correct"], gb["runs"][f"blind/base/{s}"]["other_correct"]) for s in SEEDS]
print(f"  committed gate (graphics chip, 2026-09-25, out-repairs/gate_base.json): {committed}")
check("gate, channel removed, on the processor equals the committed gate field for field",
      [(mea[("channel_removed", s)]["gate"]["own_correct"], mea[("channel_removed", s)]["gate"]["other_correct"]) for s in SEEDS]
      == committed)
for r in READINGS:
    g = [(mea[(r, s)]["gate"]["own_correct"], mea[(r, s)]["gate"]["other_correct"]) for s in SEEDS]
    print(f"  gate {r}: {g}, n = {[mea[(r, s)]['gate']['n'] for s in SEEDS]}")
check("gate, channel removed: own 702, 715, 702; named-other 712, 726, 650",
      [(mea[("channel_removed", s)]["gate"]["own_correct"], mea[("channel_removed", s)]["gate"]["other_correct"]) for s in SEEDS]
      == [(702, 712), (715, 726), (702, 650)])
check("gate, channel left on: own 707, 716, 698; named-other 710, 722, 653",
      [(mea[("channel_left_on", s)]["gate"]["own_correct"], mea[("channel_left_on", s)]["gate"]["other_correct"]) for s in SEEDS]
      == [(707, 710), (716, 722), (698, 653)])
check("gate fails on every seed and reading, both conditions",
      all(not m["gate"]["own_clears"] and not m["gate"]["other_clears"] and m["gate"]["n"] == 3000 for m in mea.values()))
gmiss = [790 - m["gate"][k] for m in mea.values() for k in ("own_correct", "other_correct")]
gmiss_own = [790 - m["gate"]["own_correct"] for m in mea.values()]
print(f"  gate shortfall over all twelve counts {min(gmiss)} to {max(gmiss)}; own-directed only {min(gmiss_own)} to {max(gmiss_own)}")
check("'fails by 64 to 140 of 3,000' (findings 4) = shortfall over both conditions, both readings",
      (min(gmiss), max(gmiss)) == (64, 140), f"{min(gmiss)} to {max(gmiss)}")

# 4. null transplant, twins
check("null transplant bit-identical at all 45 site sets, every seed and reading",
      all(m["null_bit_identical_at_every_site_set"] is True for m in mea.values()))
for s in SEEDS:
    for key, src in (("dev_twins", nom), ("fresh_twins", mea)):
        t = src[("channel_removed", s)][key]
        check(f"channel removed seed {s} {key}: inputs and states identical, largest difference 0",
              t["inputs_identical"] and t["states_identical"] and t["largest_state_difference"] == 0.0
              and t["actions_that_differ"] == 0)
diffs = [src[("channel_left_on", s)][key]["actions_that_differ"] for s in SEEDS for key, src in (("dev_twins", nom), ("fresh_twins", mea))]
check("channel left on: twins' states differ, own-directed actions differ on 3 to 12 trials",
      all(not src[("channel_left_on", s)][key]["states_identical"] for s in SEEDS for key, src in (("dev_twins", nom), ("fresh_twins", mea)))
      and (min(diffs), max(diffs)) == (3, 12), f"{diffs}")

# 5. the floor, recounted from the raw grid on development episodes (not the file's 'clears' flag)
for (r, s), n in nom.items():
    u, a = n["dev_untouched"], n["dev_accuracy"]
    need = 0.8 * (a - u)
    sets = {}
    for g in n["grid"]:
        sets[(tuple(g["layers"]), g["positions"])] = g["accuracy_whole"]
    clear = sum(1 for w in sets.values() if w - u >= need and need > 0)
    raise_ = max(w - u for w in sets.values())
    print(f"  dev {r}/{s}: accuracy {a:.4f} untouched {u:.4f} need {need:+.4f} largest raise {raise_:+.4f} "
          f"site sets {len(sets)} clearing (recount) {clear} (file {n['site_sets_clearing']})")
    check(f"dev {r}/{s}: recount of site sets clearing equals the file, and is 0",
          clear == n["site_sets_clearing"] == 0 and len(sets) == 45)
check("findings 4.1: seed 0 dev accuracy 0.2333 vs untouched 0.2400; seed 1 0.2100 vs 0.2300",
      all(round(nom[(r, 0)]["dev_accuracy"], 4) == 0.2333 and round(nom[(r, 0)]["dev_untouched"], 4) == 0.2400
          and round(nom[(r, 1)]["dev_accuracy"], 4) == 0.2100 and round(nom[(r, 1)]["dev_untouched"], 4) == 0.2300
          for r in ("channel_removed",)),
      "reading A")
for r in READINGS:
    for s in (0, 1):
        n = nom[(r, s)]
        check(f"findings 4.1: {r} seed {s} dev requirement below zero", n["dev_accuracy"] - n["dev_untouched"] < 0,
              f"{n['dev_accuracy']:.4f} - {n['dev_untouched']:.4f}")
n2 = nom[("channel_left_on", 2)]
need2 = 0.8 * (n2["dev_accuracy"] - n2["dev_untouched"])
raise2 = max(g["accuracy_whole"] - n2["dev_untouched"] for g in n2["grid"])
check("findings 4.2: seed 2 channel left on, dev requirement +0.0053, largest raise +0.0017",
      round(need2, 4) == 0.0053 and round(raise2, 4) == 0.0017, f"{need2:+.4f}, {raise2:+.4f}")

# 6. fresh episodes: site sets clearing, no-transplant rule, arithmetic
fresh = {k: (m["fresh_site_sets_clearing"]) for k, m in mea.items()}
print("  fresh site sets clearing:", fresh)
check("fresh: 0 everywhere except channel left on seed 2, which is 33",
      all(v == (33 if k == ("channel_left_on", 2) else 0) for k, v in fresh.items()))
m2 = mea[("channel_left_on", 2)]
ar2 = m2["fresh_arithmetic_DESCRIPTION_ONLY"]
need_f2 = 0.8 * (m2["fresh_accuracy"] - m2["fresh_untouched"])
print(f"  fresh channel left on seed 2: accuracy {m2['fresh_accuracy']:.4f} untouched {m2['fresh_untouched']:.4f} "
      f"need {need_f2:+.5f} = {need_f2 * 800:.2f} episodes of 800; raise range {ar2['whole_minus_untouched']}")
check("fresh seed 2 channel left on: requirement +0.0010 (under one episode of 800)", round(need_f2, 4) == 0.0010 and need_f2 * 800 < 1)
check("fresh seed 2 channel left on: largest raise +0.0025 = 2 episodes of 800",
      abs(ar2["whole_minus_untouched"]["max"] * 800 - 2) < 1e-9)
want_nt = {("channel_removed", 0): (0.2487, 0.1107), ("channel_removed", 1): (0.2300, 0.1116), ("channel_removed", 2): (0.2200, 0.1109),
           ("channel_left_on", 0): (0.2500, 0.1107), ("channel_left_on", 1): (0.2313, 0.1116), ("channel_left_on", 2): (0.2225, 0.1109)}
for k, (rate, form) in want_nt.items():
    nt = mea[k]["no_transplant"]
    f2 = (1 - mea[k]["fresh_accuracy"]) / 7
    check(f"no-transplant {k[0]}/{k[1]}: {rate} vs {form}, outside 0.018",
          round(nt["rate"], 4) == rate and round(f2, 4) == form and abs(nt["rate"] - f2) > 0.018
          and nt["inside_allowance"] is False, f"rate {nt['rate']:.4f} formula {f2:.4f} miss {nt['rate'] - f2:.4f}")
misses = [mea[k]["no_transplant"]["rate"] - (1 - mea[k]["fresh_accuracy"]) / 7 for k in mea]
print(f"  no-transplant miss {min(misses):.4f} to {max(misses):.4f}")
check("'misses its formula by 0.11 to 0.14' (findings 4)", round(min(misses), 2) == 0.11 and round(max(misses), 2) == 0.14)
want5 = {("channel_removed", 0): (180, 0), ("channel_removed", 1): (180, 0), ("channel_removed", 2): (180, 0),
         ("channel_left_on", 0): (32, 148), ("channel_left_on", 1): (20, 160), ("channel_left_on", 2): (20, 160)}
for k, (und, dfn) in want5.items():
    ar = mea[k]["fresh_arithmetic_DESCRIPTION_ONLY"]
    vals = (ar["min"], ar["median"], ar["max"])
    check(f"arithmetic {k[0]}/{k[1]}: {und} undefined / {dfn} defined", (ar["zero_divided_by_zero_or_by_zero"], ar["defined"]) == (und, dfn),
          f"min/median/max {vals}; room {ar['whole_minus_untouched']}; floor asks {ar['required_room_for_the_floor']:+.4f}")

print()
print("=== Pull request 89: the other-agent control, twenty random pieces (NOT A RESULT) ===")
c = j(CONTROL, CO + "code_test_NOT_A_RESULT.json")["returned"]
old = j(CONTROL, "experiments/rehearsal-successor-measure/out-short-prestated-run/part_c_NOT_A_RESULT.json")["returned"]
check("same site set as the earlier code test", c["site_set"] == old["site_set"], str(c["site_set"]))
for new_k, old_k in (("own_directed_moved", "own_directed_moved"),
                     ("single_random_piece_as_the_earlier_code_drew_it", "own_directed_moved_random_piece"),
                     ("named_other_moved", "named_other_moved")):
    check(f"{new_k} equals the earlier test's {old_k} exactly", c[new_k] == old[old_k], f"{c[new_k]!r} vs {old[old_k]!r}")
check("0.0012, 0.0063, 0.0962 to four places",
      (round(c["own_directed_moved"], 4), round(c["single_random_piece_as_the_earlier_code_drew_it"], 4),
       round(c["named_other_moved"], 4)) == (0.0012, 0.0063, 0.0962))
d = c["random_pieces"]["own_directed_moved"]
x = c["own_directed_moved"]
srt = sorted(d)
med = (srt[9] + srt[10]) / 2                          # middle of twenty, by hand
pos = 0.95 * 19                                       # numpy's default 'linear' rule, by hand
p95 = srt[int(pos)] + (pos - int(pos)) * (srt[int(pos) + 1] - srt[int(pos)])
cnt = (sum(v < x for v in d), sum(v == x for v in d), sum(v > x for v in d))
print(f"  twenty in episodes of 800: {sorted(round(v * 800) for v in d)}; real figure {x * 800:.0f} of 800")
# the shares are 32-bit means, so k/800 to within 32-bit rounding, not exactly
check("twenty draws, each a whole number of episodes of 800 (to 32-bit rounding)",
      len(d) == 20 and all(abs(v * 800 - round(v * 800)) < 1e-4 for v in d))
check("middle value 0.0037 (recomputed by hand)", round(med, 4) == 0.0037 and med == c["random_pieces"]["median"], f"{med}")
check("95th percentile 0.0052 (recomputed by hand)", round(p95, 4) == 0.0052 and abs(p95 - c["random_pieces"]["p95"]) < 1e-15, f"{p95}")
check("0 below, 1 equal, 19 above", cnt == (0, 1, 19) == (c["random_pieces"]["below"], c["random_pieces"]["equal"], c["random_pieces"]["above"]))
check("the one old draw (0.0063) is above 19 of 20 and above the 95th percentile",
      sum(v < c["single_random_piece_as_the_earlier_code_drew_it"] for v in d) == 19
      and c["single_random_piece_as_the_earlier_code_drew_it"] > p95)
check("trials 800", c["trials"] == 800)

print()
print("FAILURES:", FAILS or "none")
sys.exit(1 if FAILS else 0)
