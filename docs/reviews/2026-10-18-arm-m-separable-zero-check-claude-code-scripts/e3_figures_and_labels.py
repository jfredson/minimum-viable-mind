"""E3: every MEASURED figure the findings quote, looked up in the output file it
comes from; and where the figures found only by the added diagnostics (D7, D8,
D9) appear, whether the paragraph says they were added.

Usage (from the worktree root):
  python e3_figures_and_labels.py <pull request body saved as a file>
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(DOCS, "2026-10-18-arm-m-separable-zero-scripts")
FINDINGS = open(os.path.join(DOCS, "2026-10-18-arm-m-separable-zero-findings.md")).read()
BODY = open(sys.argv[1]).read() if len(sys.argv) > 1 else ""


def out(name):
    return open(os.path.join(OUT, name + "_output.txt")).read()


# (finding, figure as the findings print it, output file, text that must be in that output)
CLAIMS = [
    ("F0", "M separable 1190/1190/1190, 0.0", "d0_reproduce", '"separable": {"actions": 1190, "right": 1190, "still_right_after_swap": 1190, "route_use": 0.0}'),
    ("F0", "M stirred-in 1810/1387/1354, 0.0238", "d0_reproduce", '"actions": 1810, "right": 1387, "still_right_after_swap": 1354, "route_use": 0.0238'),
    ("F0", "T slot 3000/2959/41, 0.9861", "d0_reproduce", '"actions": 3000, "right": 2959, "still_right_after_swap": 41, "route_use": 0.9861'),
    ("F0", "toy M separable 1.0 on three seeds", "d0_reproduce", None),
    ("F0", "weight on true agent 0.9990, every model", "d0_reproduce", None),
    ("F1", "item-word disagreements 0", "d1_bookkeeping", "differs from the item word of the assignment turn for the action's item: 0"),
    ("F1", "mask disagreements 0", "d1_bookkeeping", "mask disagreements with 'item word is it1, it2 or it3': 0"),
    ("F1", "it0 616, it4 574", "d1_bookkeeping", "it0 616, it1 0, it2 0, it3 0, it4 574"),
    ("F1", "returned logits mismatches 0 and 0", "d1_bookkeeping", "separable route's on the separable mask: 0; not exactly the stirred-in route's on the other: 0"),
    ("F1", "1190 of 3000, 0.3967", "d1_bookkeeping", "1190 of 3000, share 0.3967"),
    ("F2", "M slot moves 1190, 0.22", "d2_swap_reach", "moves under the swap: 1190 of them; mean size of the move 0.2218"),
    ("F2", "M 0.2545 / 0.2540", "d2_swap_reach", "mean weight on the true agent 0.2545"),
    ("F2", "M swapped 0.2540", "d2_swap_reach", "mean weight on the next agent 0.2540"),
    ("F2", "T 3000, 20.41", "d2_swap_reach", "3000 of them; mean size of the move 20.4098"),
    ("F2", "T 0.9780 / 0.9790", "d2_swap_reach", "mean weight on the next agent 0.9790"),
    ("F2", "M toy 6.29, 0.9989 / 0.9988", "d2_swap_reach", "mean size of the move 6.2889"),
    ("F2", "T toy 7.46, 0.9974", "d2_swap_reach", "mean size of the move 7.4606"),
    ("F3", "M 3570, own 0, that agent 3570", "d3_forced_row", "3570 cases, still the model's own answer 0, that agent's answer 3570"),
    ("F3", "M rows 11.642 and 3.105", "d3_forced_row", "true agent's row 11.642, other agents' rows 3.105"),
    ("F3", "T 9000, 25, 8960", "d3_forced_row", "9000 cases, still the model's own answer 25, that agent's answer 8960"),
    ("F3", "T rows 12.657 and 12.928", "d3_forced_row", "true agent's row 12.657, other agents' rows 12.928"),
    ("F3", "M toy rows 12.192 and 11.485", "d3_forced_row", "true agent's row 12.192, other agents' rows 11.485"),
    ("F3", "T toy rows 16.370 and 16.386", "d3_forced_row", "true agent's row 16.370, other agents' rows 16.386"),
    ("F4", "M named-other separable 1178/1178", "d4_named_by_route", "named-other  separable items    1178 of  1178  1.000"),
    ("F4", "M named-other stirred-in 555/1822 0.305", "d4_named_by_route", "555 of  1822  0.305"),
    ("F4", "M toy named-other stirred-in 0.287", "d4_named_by_route", "523 of  1822  0.287"),
    ("F4", "T own 0.986, named-other 0.993", "d4_named_by_route", "2980 of  3000  0.993"),
    ("F5", "M lesioned 327 (0.275), route use 0.177", "d5_trunk_lesion", "trunk-lesioned  right   327 of  1190 (0.275); still right after swap   269; route use 0.177"),
    ("F5", "M full lesion 296 (0.249)", "d5_trunk_lesion", "right 296 of 1190 (0.249)"),
    ("F5", "T lesioned 2934 (0.978), 0.990", "d5_trunk_lesion", "right  2934 of  3000 (0.978); still right after swap    28; route use 0.990"),
    ("F5", "T full lesion 767 (0.256)", "d5_trunk_lesion", "right 767 of 3000 (0.256)"),
    ("F5", "M toy lesioned 1190, 1.000; full 299 (0.251)", "d5_trunk_lesion", "right 299 of 1190 (0.251)"),
    ("F5", "T toy full 740 (0.247)", "d5_trunk_lesion", "right 740 of 3000 (0.247)"),
    ("F6", "M flat 1190 (1.000)", "d7_flat_choice", "flat mixture of the four rows, own answer right:        1190 (1.000)"),
    ("F6", "M flat lesioned 296 (0.249)", "d7_flat_choice", "flat mixture, acting channel out of the trunk:           296 (0.249)"),
    ("F6", "M ratio 3.775 / 1.017", "d7_flat_choice", "mean size: 3.775; with the acting channel out of the trunk: 1.017"),
    ("F6", "T flat 970 (0.323), ratio 0.991", "d7_flat_choice", "970 (0.323)"),
    ("F6", "M toy flat 518 (0.435), 1.064", "d7_flat_choice", "518 (0.435)"),
    ("F6", "T toy flat 710 (0.237), 0.999", "d7_flat_choice", "710 (0.237)"),
    ("F6", "sanity 0 in every model", "d7_flat_choice", None),
    ("F7", "decay alone 0.3350 and 0.9631", "d6_weights", "0.3350"),
    ("F7", "toy decay 0.9631", "d6_weights", "0.9631"),
    ("F7", "M read_own 1.92", "d6_weights", "read_own.weight    end   5.2037  start   2.7171  ratio  1.9151"),
    ("F7", "M own_key 1.37", "d6_weights", "ratio  1.3747"),
    ("F7", "M own_marker 0.88", "d6_weights", "ratio  0.8814"),
    ("F7", "M to_val 3.02", "d6_weights", "ratio  3.0178"),
    ("F7", "M act_vec 19.3", "d6_weights", "ratio 19.3449"),
    ("F7", "T read_own 1.13", "d6_weights", "ratio  1.1252"),
    ("F7", "T own_key 1.13", "d6_weights", "ratio  1.1274"),
    ("F7", "T own_marker 3.27", "d6_weights", "ratio  3.2672"),
    ("F7", "T to_val 2.42", "d6_weights", "ratio  2.4219"),
    ("F7", "T act_vec 18.6", "d6_weights", "ratio 18.6226"),
    ("F7", "M gap 0.035, top 0.2616, query 0.561", "d6_weights", "M-10M-rerun  score gap top minus second    0.035; weight on top row 0.2616"),
    ("F7", "M query 0.561", "d6_weights", "size of the slot's query 0.561"),
    ("F7", "T gap 278.988, 1.0000, 20.479", "d6_weights", "score gap top minus second  278.988; weight on top row 1.0000"),
    ("F7", "M toy 10.213, 0.9989", "d6_weights", "10.213; weight on top row 0.9989"),
    ("F7", "T toy 8.914, 0.9974", "d6_weights", "8.914; weight on top row 0.9974"),
    ("F7/D8", "M end 1.670 0.151 0.132 0.503", "d8_answer_vector", "vector   1.670  differing part   0.151  keys' differing part    0.132  embeddings   0.503"),
    ("F7/D8", "M start 2.541 2.422 1.383 14.940", "d8_answer_vector", "start vector   2.541  differing part   2.422  keys' differing part    1.383  embeddings  14.940"),
    ("F7/D8", "M 0.0625", "d8_answer_vector", "end over start 0.0625"),
    ("F7/D8", "T end 14.258 14.085 21.526 5.697", "d8_answer_vector", "vector  14.258  differing part  14.085  keys' differing part   21.526  embeddings   5.697"),
    ("F7/D8", "T 5.8165", "d8_answer_vector", "end over start 5.8165"),
    ("F7/D8", "M toy 4.269, 10.248", "d8_answer_vector", "differing part   4.269  keys' differing part    3.636  embeddings  10.248"),
    ("F7/D8", "T toy 5.067, 11.069", "d8_answer_vector", "differing part   5.067  keys' differing part    3.747  embeddings  11.069"),
    ("F8", "M 1387 (0.766), 1405 (0.776), 267 (0.148)", "d9_stirred_in_items", "trunk_lesioned  right   267 (0.148)"),
    ("F8", "M swapped 1405 (0.776)", "d9_stirred_in_items", "swapped         right  1405 (0.776)"),
    ("F8", "M toy 1400, 1398, 400 (0.221)", "d9_stirred_in_items", "trunk_lesioned  right   400 (0.221)"),
]

bad = 0
for f, fig, src, text in CLAIMS:
    o = out(src)
    if text is None:
        if "three seeds" in fig:
            ok = len(re.findall(r'"separable": \{"actions": 1190, "right": 1190, "still_right_after_swap": 0, "route_use": 1.0\}', o)) == 3
        elif "0.9990" in fig:
            ok = o.count("weight on true agent 0.9990") == 6
        else:
            ok = o.count("differs from the forced-row head in 0)") == 4
    else:
        ok = text in o
    bad += not ok
    if not ok:
        print(f"  NOT FOUND: {f} {fig!r} in {src}_output.txt")
print(f"figures checked: {len(CLAIMS)}; not found in their output file: {bad}")

# derived figures the prose states
print("derived: 11.642 / 3.105 =", round(11.642 / 3.105, 3), "(F3 says 3.7; F6, the plain words and the body say 3.8 or about four)")
print("derived: 0.503 / 14.940 =", round(0.503 / 14.940, 4), "(findings: 3.4 per cent)")
print("derived: 5.697 / 14.940 =", round(5.697 / 14.940, 3), "(findings: 38 per cent)")
print("derived: 1178 + 555 =", 1178 + 555, "(findings: the run record's 1,733)")
print("derived: 20.4098 / 0.2218 =", round(20.4098 / 0.2218, 1), "(findings: 'a hundred times less')")

# labels: sections (a heading and everything under it) carrying a figure or claim
# found only by D7, D8 or D9, and whether the section says anywhere that it was added
ONLY_ADDED = {
    "D7 (an even mix of the rows gives the own answer)": ["even mix", "flat mixture", "3.775", "3.8 times", "1.017"],
    "D8 (the marker-word embeddings shrank)": ["3.4 per cent", "3 per cent", "0.503", "shrank the marker words",
                                               "marker-word embeddings", "marker words' embeddings", "marker embeddings"],
    "D9 (the stirred-in items lean on the trunk)": ["267", "0.148", "1405", "1,405"],
}
LABEL = re.compile(r"added|D7|D8|D9|not in the method", re.I)
for title, text in (("findings", FINDINGS), ("pull request body", BODY)):
    if not text:
        continue
    secs = [x for x in re.split(r"\n(?=#{1,3} )", text) if x.strip()]
    if len(secs) == 1:      # the body has bold lead-ins, not headings: one section per paragraph
        secs = [x for x in re.split(r"\n\s*\n", text) if x.strip()]
    print(f"\n{title}: {len(secs)} sections")
    for which, keys in ONLY_ADDED.items():
        hits = [x for x in secs if any(k in x for k in keys)]
        unl = [x for x in hits if not LABEL.search(x)]
        print(f"  {which}: in {len(hits)} sections, {len(unl)} that never say it was added")
        for x in unl:
            print("    unlabelled: " + " ".join(x.split())[:100] + " ...")
