"""Gate A tier 1: figures version 4 quotes from records older than 2026-10-03,
recomputed from the committed output files. The check of version 4 (pull
request 86, its section 5) says it did not re-derive these; this does.

Reads committed files only; loads no model; $0. Run from the root of the
checkout with the project's Python.
"""
import json
import re

B = "experiments/rehearsal-successor-measure/"
R = "experiments/06-mvm-0a-constructed-self-index/reviews/"


def j(p):
    return json.load(open(B + p))


def line(label, v4, got):
    print(f"{label:<74} v4: {v4:<28} file: {got}")


print("--- section 6.3 (v4 lines 1088 to 1092): two made-up systems, true share 0.5")
d = j("out/denominator_simulated.json")["cases"]
line("strong transplant, version 1 form / chance-corrected form", "0.4323 / 0.5018",
     f"{d['strong transplant']['registered_mean']:.4f} / {d['strong transplant']['floor_corrected_mean']:.4f}")
line("weak transplant, version 1 form / chance-corrected form", "0.3222 / 0.5013",
     f"{d['weak transplant']['registered_mean']:.4f} / {d['weak transplant']['floor_corrected_mean']:.4f}")

print("--- section 6.4 item 3 (v4 lines 1185 to 1188): the largest measured miss against (1 - p) / 7")
f = j("out/denominator_floor.json")["arms"]
miss = {k: v["measured_untouched"] - v["prediction_from_the_review"] for k, v in f.items()}
k = max(miss, key=lambda x: abs(miss[x]))
line("largest |measured - formula|, and where", "0.017536, free arm, one seed", f"{abs(miss[k]):.6f} at {k}")

print("--- section 7.3 item 6 (v4 lines 1959 to 1972): control 6's empty cell and the relaxed set")
c6 = j("out/denominator_control6.json")
line("same-value trials, distinct grammar", "0 of 4,000",
     f"{c6['distinctness_preserving_grammar']['same_value_trials']} of {c6['distinctness_preserving_grammar']['trials']}")
line("blind solver, strict set to relaxed set", "0.2467 to 0.3095",
     f"{c6['relaxed_grammar']['blind_solver_on_the_strict_set']} to {c6['relaxed_grammar']['blind_solver_on_the_relaxed_set']}")

print("--- section 7.1 (v4 lines 1254 to 1258): the unseen-vocabulary diagnostic")
t = j("out/transplant.json")["held_out_accuracy"]
line("arm T own-directed on unseen marker words, seeds 0/1/2", "0.7612, 0.6512, 0.6512",
     ", ".join(f"{t['T/' + s]['unseen_vocabulary']['own']:.5f}" for s in "012"))
n = j("out/negative_case.json")["arms"]
line("negative readings on that pool (rehearsal R-4)", "-0.1706 and -0.2755",
     f"{n['T/0']['registered_degree']:.4f} and {n['T/2']['registered_degree']:.4f} (version 1 form)")
g = j("out-grammar-c/outcomes.json")["negative_at_nomination"]["T/base/0"]["reading"]["degree"]
line("arm T seed 0 on the grammar attempt's unseen pool (v4 line 2387)", "-0.1870", f"{g:.4f}")

print("--- section 4.4 (v4 lines 597 to 626): the named-other condition")
for rec in ("curriculum", "reweight"):
    gg = j(f"out-repairs/gate_{rec}.json")
    v = gg["verdicts"][f"F/{rec}"]
    cnt = [gg["runs"][f"F/{rec}/{s}"]["other_correct"] for s in "012"]
    line(f"{rec}: named-other seeds clearing, counts", "0 of 3", f"{v['other_seeds_clearing']} of {v['seeds']}, {cnt}")
p = j("out-grammar-c/passline.json")
line("grammar attempt: named-other counts; own-directed mean; level", "774, 730, 759; 0.5654; 0.5513",
     f"{p['named_other_correct']}; {p['own_directed_mean']:.4f}; {p['own_level']}")
txt = open(R + "2026-09-26-grammar-attempt-check-claude-worktree.md").read()
line("the grammar check's own re-run (its line 38)", "750, 809, 739",
     re.search(r"\*\*750, 809 and 739\*\*", txt) is not None and "750, 809 and 739 found" or "not found")

print("--- section 5.3 (v4 lines 855 to 860): arm M's entangled share")
m = j("out-repairs/measure_base_M.json")["arms"]
line("fourth_arm.entangled_share, seeds 0/1/2", "0.60375 (483 of 800)",
     ", ".join(str(m["M/base/" + s]["fourth_arm"]["entangled_share"]) for s in "012"))

print("--- section 9 and W8: the rented slice")
b = j("out/rented-slice-2026-09-25-attempt-2/bench_arms.json")["arms"]
line("ms per step T / C / F", "13.08 / 13.52 / 12.53",
     " / ".join(f"{1000 * b[a]['seconds_per_step']:.2f}" for a in "TCF"))
line("arm C slowest step over its median", "2.9%",
     f"{100 * (b['C']['slowest'] / b['C']['median_seconds_per_step'] - 1):.1f}%")

print("--- section 7.2 item 1 (v4 lines 1384 to 1389, 1414 to 1418): the route (b) label search, arm F")
for c in ("own-turn-pair", "own-source-turn", "own-value", "marker-word"):
    v = json.load(open(B + f"out-label-search/verdict_{c}.json"))["arms"]["F"]
    best = max(v["best_fit_per_seed"].values())
    fixed = max(v["best_fixed_extent_fit_per_seed"].values())
    print(f"  {c:<16} best over all 60 site sets {best:.3f}; best over the fixed-extent 45 {fixed:.3f}; "
          f"per seed {[round(x, 3) for x in v['best_fit_per_seed'].values()]}; clears: {v['clears_over_all_60']}")

print("--- section 10: the thirty models' fingerprints")
s = j("out-v3-rules/models_sha256_check.json")
line("out-v3-rules/models_sha256_check.json all_agree", "true", s.get("all_agree"))
