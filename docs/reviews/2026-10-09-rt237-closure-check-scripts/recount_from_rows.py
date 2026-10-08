"""Closure check of the fatal finding RT-237 (the free model's gate named
question sets the task does not have): an independent recount from the
committed gate rows.

Imports nothing from the project. Standard library only. It

  (a) derives the two lines of arm F's gate from the exact binomial tail in
      integer arithmetic: the learning bar (above one in four at the 0.05
      level, one-sided, on 3,000) and the ownership-free line (above one half
      at the same level);
  (b) lists, for every committed arm F row under experiments/08-successor-degree,
      whether each field the gate clauses need is present, and its value;
  (c) judges each clause of arm F's gate from the raw counts by the text's
      rule (version 5, sections 8.1 and 8.2) and compares the result, seed by
      seed and at the arm level, with what the decision code wrote in the
      summary.json beside the rows;
  (d) checks that the clauses that are only reported (the named-other count
      with the channel zeroed, and its candidate count) never appear among
      the checks the code gated on;
  (e) compares the candidate counts in the made-up decision cases with the
      committed rehearsal record they were copied from.

Run from the repository root:
    python3 docs/reviews/2026-10-09-rt237-closure-check-scripts/recount_from_rows.py
"""
from __future__ import annotations

import glob
import json
import math
import os
import sys

ROOT = os.getcwd()
EXP = os.path.join(ROOT, "experiments/08-successor-degree")
LESION_RECORD = os.path.join(
    ROOT, "experiments/rehearsal-successor-measure/out-lesion-content-check/lesion_content_check.json")


# ----------------------------------------------------------- (a) the lines

def smallest_count_above(n: int, num: int, den: int) -> tuple[int, float]:
    """Smallest k with P(X >= k) <= 0.05 for X ~ Binomial(n, num/den), exact,
    in integers: P(X >= k) = sum_{i>=k} C(n,i) num^i (den-num)^(n-i) / den^n."""
    total = den ** n
    tail = 0
    terms = [math.comb(n, i) * num ** i * (den - num) ** (n - i) for i in range(n + 1)]
    # walk down from the top, keeping the tail from k upward
    best = None
    for k in range(n, -1, -1):
        tail += terms[k]
        if 20 * tail <= total:     # tail / total <= 0.05
            best = (k, tail)
        else:
            break
    k, t = best
    return k, t / total


def lines():
    bar, bar_tail = smallest_count_above(3000, 1, 4)
    ofl, ofl_tail = smallest_count_above(3000, 1, 2)
    # the count one below each line must fail the 0.05 test, or the line is not the smallest
    print("(a) the lines, exact binomial tail, integer arithmetic")
    print(f"    learning bar on 3,000 at one in four: {bar} (tail {bar_tail:.5f})")
    print(f"    ownership-free line on 3,000 at one half: {ofl} (tail {ofl_tail:.5f})")
    for n in (750,):
        b2, _ = smallest_count_above(n, 1, 4)
        o2, _ = smallest_count_above(n, 1, 2)
        print(f"    the same rule on {n} episodes (the scaled pipeline rows): bar {b2}, ownership-free line {o2}")
    return bar, ofl


# ----------------------------------------------------------- (b), (c), (d)

NEEDED = ["episodes", "bar", "own_correct", "other_correct", "lesioned_own_correct",
          "lesioned_other_correct", "lesioned_candidate_own_correct",
          "lesioned_candidate_other_correct", "ownership_free_line"]

GATED = {  # the clause name the code writes -> my plain name
    "own-directed learning": "L1 own-directed learning",
    "named-other learning": "L2 named-other learning",
    "channel-removal collapse": "C1 collapse with the channel zeroed",
    "ownership-free line": "C4 ownership-free line",
}


def my_states(g: dict, bar_full: int, ofl_full: int) -> dict:
    """Each gated clause of arm F, judged from the raw counts by the text.
    A field that is absent means the clause never ran (stop S8 counts it as
    failed; the code labels it 'not run')."""
    n = g.get("episodes")
    bar = g.get("bar")
    # the text: the bar is 790 on 3,000; at other sizes the same rule
    expect_bar = bar_full if n == 3000 else smallest_count_above(n, 1, 4)[0]
    expect_line = ofl_full if n == 3000 else smallest_count_above(n, 1, 2)[0]
    out = {"_bar_matches_rule": bar == expect_bar, "_line_used": expect_line}
    if "ownership_free_line" in g:
        out["_row_line_matches_rule"] = g["ownership_free_line"] == expect_line

    def st(key, test):
        if key not in g:
            return "not run"
        if g[key] is None:
            return "could not be evaluated"
        return "passed" if test(g[key]) else "failed"

    out["L1 own-directed learning"] = st("own_correct", lambda v: v >= bar)
    out["L2 named-other learning"] = st("other_correct", lambda v: v >= bar)
    out["C1 collapse with the channel zeroed"] = st("lesioned_own_correct", lambda v: v < bar)
    out["C4 ownership-free line"] = st("lesioned_candidate_own_correct", lambda v: v >= expect_line)
    return out


def rows_and_summaries():
    dirs = sorted({os.path.dirname(p) for p in glob.glob(os.path.join(EXP, "**/row_F_seed*.json"), recursive=True)})
    return dirs


def main():
    bar, ofl = lines()
    print()
    print("(b) the fields, in every committed arm F row")
    print("    columns: own, other, lesioned own, lesioned other, lesioned candidate own, "
          "lesioned candidate other, ownership_free_line  ('-' = field absent)")
    dirs = rows_and_summaries()
    mismatches = 0
    states_by_dir = {}
    for d in dirs:
        rel = os.path.relpath(d, EXP)
        cells = []
        for s in (0, 1, 2):
            p = os.path.join(d, f"row_F_seed{s}.json")
            if not os.path.exists(p):
                continue
            g = json.load(open(p))["gate"]
            cells.append((s, g))
        def fmt(g):
            return "/".join("-" if k not in g else str(g[k]) for k in NEEDED[2:])
        print(f"    {rel}: n={cells[0][1].get('episodes')} bar={cells[0][1].get('bar')}  "
              + "  ".join(f"s{s} {fmt(g)}" for s, g in cells))
        states_by_dir[d] = {s: my_states(g, bar, ofl) for s, g in cells}

    print()
    print("(c) each gated clause judged from the counts, against the decision code's summary.json")
    total_compared = 0
    for d, by_seed in states_by_dir.items():
        rel = os.path.relpath(d, EXP)
        sp = os.path.join(d, "summary.json")
        if not os.path.exists(sp):
            print(f"    {rel}: no summary.json (rows only)")
            continue
        summ = json.load(open(sp))
        if not any("checks" in (v or {}) for v in summ.get("per_seed", {}).get("F", {}).values()):
            print(f"    {rel}: summary.json written by earlier code, with no per-seed clause states; "
                  f"nothing to compare (my states: "
                  + " ".join(f"s{s}:" + "".join("P" if m[n] == "passed" else ("-" if m[n] == "not run" else "F")
                                                 for n in GATED.values()) for s, m in by_seed.items()) + ")")
            continue
        per_seed = summ.get("per_seed", {}).get("F", {})
        arm = summ.get("arms", {}).get("F", {})
        line_bits = []
        for s, mine in by_seed.items():
            code = (per_seed.get(str(s)) or {}).get("checks", {})
            for code_name, my_name in GATED.items():
                total_compared += 1
                if code.get(code_name) != mine[my_name]:
                    mismatches += 1
                    print(f"    MISMATCH {rel} seed {s} {my_name}: mine {mine[my_name]}, code {code.get(code_name)}")
            # (d) the reported-only clauses must not be gated
            for k in code:
                if "named-other" in k and "learning" not in k:
                    mismatches += 1
                    print(f"    GATED A REPORTED-ONLY CLAUSE {rel} seed {s}: {k}")
            if not mine["_bar_matches_rule"]:
                mismatches += 1
                print(f"    BAR NOT BY THE RULE {rel} seed {s}")
            if mine.get("_row_line_matches_rule") is False:
                mismatches += 1
                print(f"    ROW'S LINE NOT BY THE RULE {rel} seed {s}")
            gate_all = all(mine[n] == "passed" for n in GATED.values())
            line_bits.append(f"s{s}:" + "".join("P" if mine[n] == "passed" else
                                                  ("-" if mine[n] == "not run" else "F")
                                                  for n in GATED.values()))
            # a seed that fails any gated clause must be a no-verdict seed in the code
            if not gate_all and (per_seed.get(str(s)) or {}).get("status") == "reading":
                mismatches += 1
                print(f"    SEED READ DESPITE A FAILED CLAUSE {rel} seed {s}")
        # arm level: seeds passing learning (L1 and L2), and read only with two seeds counting
        my_learn = sorted(s for s, m in by_seed.items()
                          if m["L1 own-directed learning"] == m["L2 named-other learning"] == "passed")
        if my_learn != arm.get("seeds_passing_learning"):
            mismatches += 1
            print(f"    MISMATCH {rel} seeds passing learning: mine {my_learn}, code {arm.get('seeds_passing_learning')}")
        my_gate_ok = sorted(s for s, m in by_seed.items() if all(m[n] == "passed" for n in GATED.values()))
        read = arm.get("read")
        if read and len(my_gate_ok) < 2:
            mismatches += 1
            print(f"    ARM F READ WITH FEWER THAN TWO SEEDS PASSING EVERY GATE CLAUSE: {rel}")
        if read and not set(map(int, arm.get("readings", {}))) <= set(my_gate_ok):
            mismatches += 1
            print(f"    A READING SEED FAILS A GATE CLAUSE: {rel}")
        print(f"    {rel}: clauses L1 L2 C1 C4 per seed {' '.join(line_bits)}; "
              f"seeds passing every gate clause (mine) {my_gate_ok}; code: learning {arm.get('seeds_passing_learning')}, "
              f"read {read}, seeds read {sorted(map(int, arm.get('readings', {})))}; outcome {summ.get('outcome', {}).get('code')}")
    print(f"    clause states compared: {total_compared}; mismatches of any kind: {mismatches}")

    print()
    print("(e) the candidate counts in the made-up cases against the committed rehearsal record")
    rec = json.load(open(LESION_RECORD))
    print(f"    the record's line: {rec['line']}")
    bad = 0
    for arm_ in ("T", "C", "M", "F"):
        for s in (0, 1, 2):
            m = rec["models"][f"{arm_}/{s}"]["channel_zeroed"]
            rowp = os.path.join(EXP, f"out-a2-cases/r1/row_{arm_}_seed{s}.json")
            g = json.load(open(rowp))["gate"]
            toy = json.load(open(os.path.join(EXP, f"out-a2-cases/toy/row_{arm_}_seed{s}.json")))["gate"]
            ok = (g["lesioned_candidate_own_correct"] == m["own"]["candidate"]
                  and toy["lesioned_own_correct"] == m["own"]["correct"]
                  and toy["lesioned_other_correct"] == m["other"]["correct"])
            bad += not ok
            print(f"    {arm_}/{s}: case row candidate {g['lesioned_candidate_own_correct']}, record {m['own']['candidate']}; "
                  f"toy row lesioned own/other correct {toy['lesioned_own_correct']}/{toy['lesioned_other_correct']}, "
                  f"record {m['own']['correct']}/{m['other']['correct']}  {'same' if ok else 'DIFFERENT'}")
    for k in ("blind/0", "blind/1", "blind/2", "untrained-F/0", "untrained-F/1", "untrained-F/2"):
        if k in rec["models"]:
            print(f"    {k} (record only, no case row): candidate own {rec['models'][k]['channel_zeroed']['own']['candidate']}")
    print(f"    differences: {bad}")
    print()
    print("RESULT:", "every recount matches" if mismatches == 0 and bad == 0 else "DIFFERENCES FOUND")
    return 0 if mismatches == 0 and bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
