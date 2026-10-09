"""The Gate A tier 1 reviewer's failure-mode pass on version 5 of the
successor experiment's registration text: every entry of
`docs/known-failure-modes.md`, run against the design.

Written 2026-10-08 by the reviewing session, which wrote none of version 5,
none of its checks and none of the work it cites. Reads committed files only;
loads no model, trains nothing, rents nothing; $0.

    .venv/bin/python -I failure_mode_pass_v5.py --v5 <version 5 as on the
        branch under review, extracted with git show> --part all

The main-line records it reads (all at origin/main 93f4e90):
  experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000/
      the toy pass under the registered code (pull request 151), the one
      record of the twelve toy models produced by the code section 7.4 names
  experiments/08-successor-degree/out-dev-10m-check/
      the four 10-million development checkpoints read by the procedure
  experiments/08-successor-degree/out-sharpness-fix/inuse-cases/
  experiments/08-successor-degree/out-decoy-w18/
  experiments/rehearsal-successor-measure/out-competing-solver-run/
and the frozen generator `experiments/08-successor-degree/src/grammar.py`,
imported (it is the registered generator, not a stand-in).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
EXP08 = os.path.join(ROOT, "experiments", "08-successor-degree")
PASSB = os.path.join(EXP08, "out-ruled-code-changes", "passB-limit10000")
DEV10 = os.path.join(EXP08, "out-dev-10m-check")
SOLVER = os.path.join(ROOT, "experiments", "rehearsal-successor-measure", "out-competing-solver-run")
ARMS, SEEDS = "TCFM", (0, 1, 2)


def rel(p):
    return os.path.relpath(p, ROOT)


def row(arm, seed, base=PASSB):
    return json.load(open(os.path.join(base, f"row_{arm}_seed{seed}.json")))


def head(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ----------------------------------------------------------------- failure 1
def failure1():
    head("FAILURE 1. A comparison whose denominator was zero")
    print("Part one: every no-transplant rate and accuracy below is read from a named field of a")
    print(f"committed row ({rel(PASSB)}/row_<arm>_seed<s>.json, primary.reading.*), none typed in.")
    print("Part two: the denominator (whole - untouched), what the floor needs, and the top of the")
    print("scale (the reading when the ownership-only transplant does nothing, o = u), on fresh")
    print("episodes and on the development episodes the nomination used.")
    print()
    print("arm/seed  untouched  whole   own-acc | denom   needs   need>0 | top | dev denom  dev needs | "
          "recomputed reading = stored? | status")
    smallest = []
    for a in ARMS:
        for s in SEEDS:
            d = row(a, s)
            r = d["primary"]["reading"]
            w, o, u, p = (r["accuracy_whole"], r["accuracy_ownership_only"],
                          r["accuracy_untouched"], r["arm_own_accuracy"])
            den, need = w - u, 0.8 * (p - u)
            top = (w - u) / (w - u) if den else float("nan")
            mine = (w - o) / den if den > 0 else None
            stored = r["degree"]
            same = (mine is None and stored is None) or (stored is not None and abs(mine - stored) < 1e-12)
            nd, nu = d["nomination"]["dev_accuracy"], d["nomination"]["dev_untouched"]
            described = d["primary"].get("described_only")
            status = "described only" if described else "reads" if stored is not None else "no reading"
            if not described:
                smallest.append((den, f"{a}/{s}"))
            print(f"{a}/{s}       {u:.4f}    {w:.4f}  {p:.4f} | {den:.4f}  {need:.4f}  {str(need > 0):5}  | "
                  f"{top:.0f}   | (dev acc {nd:.4f}, untouched {nu:.4f}, needs {0.8 * (nd - nu):.4f}) | "
                  f"{str(same):5} ({'none' if mine is None else f'{mine:.4f}'}) | {status}")
    print(f"smallest fresh denominator among the rows that read: {min(smallest)[0]:.4f} ({min(smallest)[1]})")

    print()
    print(f"The 10-million development checkpoints ({rel(DEV10)}), same fields:")
    for a in ARMS:
        d = row(a, 0, DEV10)
        r = d["primary"]["reading"]
        w, u, p = r["accuracy_whole"], r["accuracy_untouched"], r["arm_own_accuracy"]
        print(f"  {a}/0 10M: whole {w:.4f}, untouched {u:.4f}, own-acc {p:.4f} -> denominator {w - u:.4f}, "
              f"needs {0.8 * (p - u):.4f}")

    print()
    print(f"The competing solver, development grids ({rel(SOLVER)}/nominate_blind_seed*_*.json):")
    for s in SEEDS:
        for mode in ("channel_removed", "channel_left_on"):
            d = json.load(open(os.path.join(SOLVER, f"nominate_blind_seed{s}_{mode}.json")))
            need = 0.8 * (d["dev_accuracy"] - d["dev_untouched"])
            print(f"  seed {s} {mode:15}: own-directed {d['dev_accuracy']:.4f}, untouched {d['dev_untouched']:.4f}, "
                  f"floor needs {need:+.4f} -> requirement above zero: {need > 0}; site sets clearing: "
                  f"{d['site_sets_clearing']}")

    print()
    print("How small can the denominator be on a seed that passes every registered rule? The gate")
    print("on learning asks 790 of 3,000 own-directed (0.2633) on the gate episodes; the floor asks")
    print("whole - untouched >= 0.8 x (p - untouched) > 0 on the fresh 800 pairs; the no-transplant")
    print("rate no longer withholds (page 8). Two error patterns for a model at own-directed p:")
    print("errors spread over the seven other values, untouched = (1-p)/7; errors spread over the")
    print("other three agents' values, untouched = (1-p)/3 (section 6.4, item 3's own example).")
    print("'pairs' is the smallest denominator in matched pairs of 800; 'band' is the half-width of a")
    print("95 per cent binomial band on a middling reading (0.5) resting on that many pairs.")
    print()
    print("  own-directed p | untouched even  min denom  pairs  band  | untouched owner-confusing  min denom  pairs  band")
    for p in (0.2633, 0.28, 0.30, 0.35, 0.45, 0.55, 0.80):
        out = []
        for u in ((1 - p) / 7, (1 - p) / 3):
            dmin = 0.8 * (p - u)
            n = dmin * 800
            band = 1.96 * math.sqrt(0.25 / n) if n > 0 else float("inf")
            out.append(f"{u:.4f}  {dmin:.4f}  {n:5.1f}  {band:.3f}")
        print(f"  {p:.4f}         | {out[0]}   | {out[1]}")


# ----------------------------------------------------------------- failure 2
ROUTE_PATTERN = r"route by which|reaches the model's states|carried by the token|is the input token|forced by the loss"


def failure2(v5_path):
    head("FAILURE 2. A probe target that cannot be recovered in principle")
    text = open(v5_path).read().split("\n## 17. ")[0].splitlines()
    print(f"Part one: the route sentence, sections 0 to 16 of version 5, pattern /{ROUTE_PATTERN}/i:")
    for i, line in enumerate(text, 1):
        if re.search(ROUTE_PATTERN, line, re.I):
            print(f"  {i}: {line.strip()}")
    print()
    print("Part two, from the registered code's toy pass: the target run (the ownership read at the")
    print("action position, whole read | best piece, per running state 0..4) against a quantity the")
    print("input guarantees, read by the same fitter on the same split: the whole state at the first")
    print("token of the model's first own turn, which IS the model's own marker word (only printed")
    print("where the nominated site spans it), and the named agent's read of control 2, whose label")
    print("is an input token of the named-other action turn.")
    for a in ARMS:
        for s in SEEDS:
            d = row(a, s)
            fits = d["fits"]
            states = " ".join(f"{fits[k]['whole']:3d}|{max(fits[k]['piece'].values()):3d}"
                              for k in sorted(fits, key=int))
            pe = d["primary"]["piece_elsewhere"]
            first = [x for x in pe.get("other_positions", []) if x["position"].startswith("first own turn, token 1")]
            g = f"; marker token itself, whole {first[0]['whole']}" if first else ""
            c2 = d.get("control2") or {}
            cands = c2.get("candidates") or []
            named = max((c["piece_correct"] for c in cands), default=None)
            nm = f"; named agent's best piece {named}" if named is not None else ""
            print(f"  {a}/{s}: {states}  -> {d['nomination_status']}{g}{nm}")
    print()
    print("The same at 10 million parameters (development checkpoints, states 0..8):")
    for a in ARMS:
        d = row(a, 0, DEV10)
        fits = d["fits"]
        states = " ".join(f"{fits[k]['whole']:3d}|{max(fits[k]['piece'].values()):3d}"
                          for k in sorted(fits, key=int))
        pe = d["primary"]["piece_elsewhere"]
        first = [x for x in pe.get("other_positions", []) if x["position"].startswith("first own turn, token 1")]
        g = (f"; marker token itself, whole {first[0]['whole']} at state {d['primary']['site_set']['layers']}"
             if first else "")
        cands = (d.get("control2") or {}).get("candidates") or []
        nm = f"; named agent's best piece {max(c['piece_correct'] for c in cands)}" if cands else ""
        print(f"  {a}/0: {states} -> {d['nomination_status']}{g}{nm}")


# ----------------------------------------------------------------- failure 3
def failure3():
    head("FAILURE 3. A cell that is empty by construction")
    sys.path.insert(0, os.path.join(EXP08, "src"))
    import numpy as np
    import grammar as G       # the registered generator, not a stand-in

    print("Part one: what the registered generator puts in each pre-stated cell, at the registered")
    print("counts, generated here from the frozen grammar.py (no record read):")
    rel_pairs = G.eval_pairs("relaxed")
    same = diff = 0
    for p in rel_pairs:
        r, dn = p["recipient"], p["donor"]
        j = p["content"]["own_item"]
        rv, dv = int(r["values"][r["model"], j]), int(dn["values"][dn["model"], j])
        if rv == dv:
            same += 1
        else:
            diff += 1
    print(f"  control 6, relaxed set (800 pairs, seed {G.EVAL_SETS['relaxed'][1]}): same-value {same}, different-value {diff}")
    fr = G.eval_pairs("fresh")
    same_f = sum(int(p["recipient"]["values"][p["recipient"]["model"], p["content"]["own_item"]]) ==
                 int(p["donor"]["values"][p["donor"]["model"], p["content"]["own_item"]]) for p in fr)
    print(f"  the same split on the fresh set (distinct values): same-value {same_f} of {len(fr)} (empty by construction, "
          "which is why control 6 runs on the relaxed set)")
    # control 4: positions before both twins' first own turns
    npos = []
    for p in fr:
        fa = int(np.argmax(p["recipient"]["acting"] > 0))
        fb = int(np.argmax(p["donor"]["acting"] > 0))
        npos.append(min(fa, fb))
    print(f"  control 4, positions before both twins' first own turns, fresh set: min {min(npos)}, "
          f"mean {sum(npos) / len(npos):.4f}, max {max(npos)}; pairs with none: {sum(n == 0 for n in npos)}")
    # control 4: are the twins' token sequences identical (the property it rests on)?
    ident = sum(bool((p["recipient"]["tokens"] == p["donor"]["tokens"]).all()) for p in fr)
    print(f"  twins token-for-token identical on the fresh set: {ident} of {len(fr)}")
    # the in-use check's routes on arm M: items it0 and it4 separable, it1 to it3 entangled
    gate = G.episodes_from_pairs(G.eval_pairs("gate"))
    sep = sum(G.ITEMS[_item_of(e, G)] in ("it0", "it4") for e in gate)
    print(f"  in-use check on arm M, gate episodes ({len(gate)}): own-directed actions on the separable items "
          f"(it0, it4) {sep}, on the stirred-in items (it1 to it3) {len(gate) - sep}")
    rr = row("M", 0)["gate"]["route_in_use"]["routes"]
    print(f"    the registered code's own row (M/0) counts: separable {rr['separable']['actions']}, "
          f"stirred-in {rr['entangled_items']['actions']}")
    # the named-other condition's trials: one per episode
    print(f"  named-other actions on the gate set: {len(gate)} (one per episode); own-directed: {len(gate)}")

    print()
    print("Part two: the generator properties that empty a cell, every file the generator is spread over:")
    src = os.path.join(EXP08, "src", "grammar.py")
    pat = re.compile(r"replace=False|\.permutation|\.shuffle\(|set\(|distinct|unique|without replacement|collide")
    for i, line in enumerate(open(src), 1):
        if pat.search(line):
            print(f"  grammar.py:{i}: {line.rstrip()}")

    print()
    print("Part three: every threshold at both ends of the range it faces.")
    from scipy.stats import binom
    k = next(k for k in range(3001) if binom.sf(k - 1, 3000, 0.25) <= 0.05)
    print(f"  learning gate: smallest k with P(X >= k | 3,000, 1/4) <= 0.05: {k} (tail {binom.sf(k - 1, 3000, 0.25):.4f}); "
          f"a fully collapsed arm read as not collapsed, per seed: {binom.sf(789, 3000, 0.25):.4f}")
    k2 = next(k for k in range(1500, 3001) if binom.sf(k - 1, 3000, 0.5) <= 0.05)
    print(f"  ownership-free line: smallest k with P(X >= k | 3,000, 1/2) <= 0.05: {k2} (tail {binom.sf(k2 - 1, 3000, 0.5):.4f})")
    print("  ownership-free line on the registered code's toy rows (gate.lesioned_candidate_own_correct):")
    for a in ARMS:
        vals = [row(a, s)["gate"].get("lesioned_candidate_own_correct") for s in SEEDS]
        print(f"    arm {a}: {vals} against 1,546 -> {[v >= 1546 for v in vals]}")
    print("  in-use check, part A (weight on the true agent >= 0.9). The built answer is a softmax of")
    print("  sharpness x tally; at the action the model's own agent has tally 2 (two assignment turns),")
    print("  the others 0, so weight = e^(2s) / (e^(2s) + 3):")
    for sh in (4.0, 1.947, 1.65, 0.70, 0.0, -0.089):
        w = math.exp(2 * sh) / (math.exp(2 * sh) + 3)
        print(f"    sharpness {sh:6.3f}: weight {w:.4f} -> {'passes' if w >= 0.9 else 'fails'}")
    print(f"    the bar is crossed at sharpness ln(27)/2 = {math.log(27) / 2:.4f}; with the number fixed at 4.0 as a")
    print("    buffer, part A can fail only on a model saved before the fix")
    print("  in-use check, part B (route use >= 0.5 on every built route), registered code's toy rows:")
    for a in "TCM":
        out = []
        for s in SEEDS:
            ru = row(a, s)["gate"]["route_in_use"]
            out.append(f"s{s} " + ", ".join(f"{n} {v['route_use']:.3f}" for n, v in ru["routes"].items())
                       + f" (sharpness {ru['sharpness']:.2f}, {ru['state']})")
        print(f"    arm {a}: " + "; ".join(out))
    ic = json.load(open(os.path.join(EXP08, "out-sharpness-fix", "inuse-cases", "inuse_cases.json")))
    print("    the made-up and 10-million cases of the in-use check (out-sharpness-fix/inuse-cases/inuse_cases.json):")
    for c in ic["cases"]:
        if "10-million" in c["about"] or "untrained" in c["about"] or "flat" in c["about"]:
            print(f"      case {c['case']}, {c['about']}: weight {c['weight']:.3f}, route use {c['route_use']} -> "
                  f"{c['got']} (expected {c['expected']})")
    print("  piece floor (144 of 180), both ends, registered code's toy rows: best piece anywhere per model")
    for a in ARMS:
        best = [max(max(f["piece"].values()) for k, f in row(a, s)["fits"].items() if k != "0") for s in SEEDS]
        print(f"    arm {a}: {best}")
    print("  control 1 on arm T (complement donor share <= untouched + 0.018), both ends:")
    t = [row("T", s)["primary"]["controls"]["1"] for s in SEEDS]
    print("    working end, registered toy rows: " + ", ".join(f"{c['complement_donor_share']:.4f} (holds {c['holds']})" for c in t))
    tab = open(os.path.join(EXP08, "out-decoy-w18", "table.md")).read().splitlines()
    v1 = [l for l in tab if l.startswith("| V1 ")]
    print(f"    broken end, the decoy of W18 at four times (out-decoy-w18/table.md, V1): {len(v1)} rows, "
          + "; ".join(l.split("|")[3].strip() for l in v1))
    print("  separation bar (0.5) and arm M's band, both ends: see the decision-procedure cases (decision_cases.out.txt)")


def _item_of(e, G):
    """The item word the own-directed action names, for one rendered episode."""
    j = int(e["action_item"][G.OWN])
    tok = int(e["tokens"][int(e["action_pos"][G.OWN]) - 2])   # act, revise, who, ITEM, ans, MASK
    w = G.IVOCAB[tok]
    assert w.startswith("it"), w
    return G.ITEMS.index(w)


# ----------------------------------------------------------------- failure 4
WORDS = (r"verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|"
         r"observed|recorded|returns|returned|yield|result")
NUM = r"[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}"


def failure4(v5_path, ledger_path):
    head("FAILURE 4. A claim of measurement with no record, or a record that does not reproduce")
    full = open(v5_path).read()
    body = full.split("\n## 17. ")[0].splitlines()
    print(f"Part one, the two sweeps on sections 0 to 16 ({len(body)} lines):")
    print(f"  lines matching the word list: {sum(bool(re.search(WORDS, l, re.I)) for l in body)}")
    print(f"  lines matching the number sweep: {sum(bool(re.search(NUM, l)) for l in body)}")
    print(f"  MEASURED labels: {sum(l.count('MEASURED') for l in body)}; ARGUED labels: {sum(l.count('ARGUED') for l in body)}")
    print()
    print("Part two (a): figures new in version 5, regenerated from the file each sentence names:")
    m0 = row("M", 0)
    print(f"  arm M gate episodes on the stirred-in route, '1,810 of 3,000' (section 5.3): the registered code's M/0 row "
          f"counts {m0['gate']['route_in_use']['routes']['entangled_items']['actions']}")
    ru = {a: [round(row(a, s)['gate']['route_in_use']['routes'][('entangled' if a == 'C' else 'entangled_items')]['route_use'], 3)
              for s in SEEDS] for a in "CM"}
    print(f"  route use before the fix, 'arm C 0.269, 0.233, 0.221; arm M 0.071, 0.090, 0.109' (section 5.6): rows give C {ru['C']}, M {ru['M']}")
    rd = {a: [row(a, s)['primary']['reading']['degree'] for s in SEEDS] for a in "TCM"}
    print("  toy readings at 1,800, 'T 0.0000; C 1.0026, 1.0000, 1.0000; M 0.5252, 0.4793, 0.5208' (sections 3, 9): rows give "
          + "; ".join(f"{a} " + ", ".join(f"{v:.4f}" for v in rd[a]) for a in "TCM"))
    sep = min(rd["C"]) - max(rd["T"])
    print(f"  separation 'lowest C minus highest T = 1.0000': {sep:.4f}")
    bestF = [max(max(f["piece"].values()) for f in row("F", s)["fits"].values()) for s in SEEDS]
    print(f"  arm F's best piece '40, 19 and 36 of 180' (section 3): rows give {bestF}")
    ts = [row("M", s)["primary"]["true_slot"]["reading"]["degree"] for s in SEEDS]
    print("  arm M within its true-slot reading '0.0252, 0.0033, 0.0288' (section 9): "
          + ", ".join(f"{abs(a - b):.4f}" for a, b in zip(rd["M"], ts)))
    lc = [row("F", s)["gate"]["lesioned_candidate_own_correct"] for s in SEEDS]
    print(f"  arm F ownership-free count '2,100, 2,238 and 2,324' (section 8.2, from a separate measurement): "
          f"the registered code's rows give {lc}")
    d10 = {a: row(a, 0, DEV10) for a in "CM"}
    print("  10-million 'best pieces 41 and 45 of 180' for arms C and M (sections 5.6 and 17): rows give best piece "
          + ", ".join(f"{a} {max(max(f['piece'].values()) for f in d10[a]['fits'].values())}" for a in "CM")
          + "; best whole read "
          + ", ".join(f"{a} {max(f['whole'] for f in d10[a]['fits'].values())}" for a in "CM"))
    v1 = [l.split("|") for l in open(os.path.join(EXP08, "out-decoy-w18", "table.md")) if l.startswith("| V1 ")]
    print("  W18 withheld readings '0.1488, 0.2137 and 0.1162' at 8 directions (section 13): table gives "
          + ", ".join(x[9].strip().split(", ")[-1] for x in v1))
    print()
    print("Part two (b): the red-team ledger rows the text says are owed or exist:")
    led = open(ledger_path).read()
    have = [n for n in range(237, 257) if re.search(rf"^\| \*{{0,2}}RT-{n}\b", led, re.M)]
    print(f"  ledger rows present for RT-237 to RT-256: {len(have)} of 20")
    print("  section 17's printed block for the same rows says:")
    for l in full.split("\n## 17. ")[1].split("\n## 18. ")[0].splitlines():
        if "ledger rows for RT-2" in l:
            print("   " + l.rstrip())
    print()
    print("Part two (c): files version 5 names that are not on the main line at this commit:")
    names = sorted(set(re.findall(r"`((?:docs|experiments)/[\w./-]+\.(?:md|py|txt|json|sh|toml))`", full)))
    missing = [n for n in names if not os.path.exists(os.path.join(ROOT, n))]
    print(f"  full paths named: {len(names)}; not on the main line: {len(missing)}")
    for n in missing:
        print(f"  {n}")
    print()
    print("Part two (d): the withheld figure. Section 6.4, item 5 says the figure the arithmetic would")
    print("have given 'appears nowhere in the output'. The registered code's toy pass, for the seeds")
    print("its own summary withholds:")
    summ = json.load(open(os.path.join(PASSB, "summary.json")))
    table = open(os.path.join(PASSB, "table.md")).read()
    sumtxt = json.dumps(summ)
    for a in "CMF":
        for s in SEEDS:
            r = row(a, s)["primary"]["reading"]
            if str(s) in summ["arms"][a]["no_verdict"]:
                fig = r["degree"]
                print(f"  {a}/{s}: withheld in summary.json ({summ['arms'][a]['no_verdict'][str(s)][0][:60]}...); "
                      f"row file primary.reading.degree = {fig!r}, status {r['status']!r}; "
                      f"in summary.json: {repr(fig) in sumtxt}; in table.md: {f'{fig:.4f}' in table.split(f'| {a}/{s} |')[1].split(chr(10))[0]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v5", required=True)
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--part", default="all")
    a = ap.parse_args()
    parts = {"1": failure1, "2": lambda: failure2(a.v5), "3": failure3,
             "4": lambda: failure4(a.v5, a.ledger)}
    for k in (parts if a.part == "all" else a.part.split(",")):
        parts[k]()


if __name__ == "__main__":
    main()
