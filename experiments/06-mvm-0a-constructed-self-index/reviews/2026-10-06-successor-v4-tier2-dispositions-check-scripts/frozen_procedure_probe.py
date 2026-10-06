#!/usr/bin/env python3
"""Checks 2 and 3 of the paired check of pull request 101: what the frozen
successor code on origin/main actually does, confirmed by running it.

This imports the FROZEN SUCCESSOR CODE (experiments/08-successor-degree/src on
origin/main, written by the freeze session, pull request 97). It does not
import or read the PR author's script `tier2_dispositions_check.py`. It
extracts a fresh copy of main's `src/` and the committed toy rows of freeze
test T3a into a temporary directory, so nothing in the repository is written.

Parts:
  A. measure.py --self-test, from the copy.
  B. procedure.summarise on the committed T3a rows: must equal the committed
     summary.json outcome.
  C. procedure.summarise on constructed copies of the T3a rows (named fields
     changed), each with the landing written beside it before it runs.
  D. The three gate-counting rules over every pass/fail pattern of arm F's
     three gate conditions on three seeds.
  E. The toy gates (Part C of the author's measurement) recomputed from the
     raw counts in out-repairs/gate_base.json, not its true/false fields.

Run from the repository root with the project Python (needs torch, numpy,
scipy, sklearn), after `git fetch`:
  python <this file>
"""
import copy
import io
import itertools
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from contextlib import redirect_stdout

ROOT = os.getcwd()
TMP = tempfile.mkdtemp(prefix="frozen-probe-")
SRC = "experiments/08-successor-degree/src"
T3A = "experiments/08-successor-degree/out-freeze-tests/t3a-committed-reads"
blob = subprocess.run(["git", "archive", "origin/main", SRC, T3A], capture_output=True, check=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
main_sha = subprocess.run(["git", "rev-parse", "origin/main"], capture_output=True, text=True).stdout.strip()
print(f"frozen code and T3a rows extracted from origin/main at {main_sha}")
sys.path.insert(0, os.path.join(TMP, SRC))
os.chdir(os.path.join(TMP, SRC))
import measure as MS      # noqa: E402  (frozen code, not the author's)
import procedure as PR    # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(f"  [{'AS EXPECTED' if ok else 'NOT AS EXPECTED'}] {name}" + (f"  -> {detail}" if detail else ""))
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------- A
print("\n== A. measure.py --self-test, run from the copy of main")
r = subprocess.run([sys.executable, "measure.py", "--self-test"], capture_output=True, text=True)
last = r.stdout.strip().splitlines()[-1]
n_pass = r.stdout.count("[PASS]")
n_fail = r.stdout.count("[FAIL]")
check("self-test passes", r.returncode == 0 and last == "all checks passed",
      f"{n_pass} PASS, {n_fail} FAIL, last line '{last}'")

# ---------------------------------------------------------------- B
rows_dir = os.path.join(TMP, T3A)
base_rows = {}
for f in sorted(os.listdir(rows_dir)):
    if f.startswith("row_") and f.endswith(".json"):
        base_rows[f] = json.load(open(os.path.join(rows_dir, f)))
committed = json.load(open(os.path.join(rows_dir, "summary.json")))


def run_case(mutate):
    d = tempfile.mkdtemp(dir=TMP)
    rows = copy.deepcopy(base_rows)
    mutate(rows)
    for f, r in rows.items():
        json.dump(r, open(os.path.join(d, f), "w"))
    with redirect_stdout(io.StringIO()):
        res = PR.summarise(d)
    return res, d


print("\n== B. summarise on the committed T3a rows")
res, d = run_case(lambda rows: None)
check("toy lands on R3, as the committed summary.json does",
      res["outcome"]["code"] == "R3" == committed["outcome"]["code"],
      f"{res['outcome']['term']}; reason: {res['outcome']['reason']}; gates {res['gates']}")
check("every arm F seed withheld, three reasons each",
      all(len(res["per_seed"]["F"][s]["reasons"]) == 3 for s in res["per_seed"]["F"]),
      "; ".join(f"F/{s}: {len(w['reasons'])}" for s, w in res["per_seed"]["F"].items()))
withheld_vals = {s: w.get("arithmetic_withheld") for s, w in res["per_seed"]["F"].items()}
summ_text = open(os.path.join(d, "summary.json")).read()
check("(defect probe) the withheld arm F arithmetic is still written to summary.json",
      all(v is not None for v in withheld_vals.values()) and '"arithmetic_withheld": 1.0' in summ_text,
      f"arithmetic_withheld = {withheld_vals}")
table_text = open(os.path.join(d, "table.md")).read()
f_rows = [ln for ln in table_text.splitlines() if ln.startswith("| F/")]
check("the table does not print the withheld F reading to four places",
      not any(f"{v:.4f}" in ln.split("|")[2] for v, ln in zip(withheld_vals.values(), f_rows)),
      "column 2 of each F row is 'no verdict: ...'; the three accuracies the reading is made from are "
      "printed in column 6: " + "; ".join(ln.split("|")[6].strip() for ln in f_rows))


def setg(rows, arm, seed, **kw):
    g = rows[f"row_{arm}_seed{seed}.json"]["gate"]
    g.update(kw)
    g["seed_passes"] = g["own_clears"] and (arm != "F" or g["other_clears"])


def setc(rows, arm, seed, key, val):
    rows[f"row_{arm}_seed{seed}.json"]["primary"]["controls"][key]["holds"] = val


print("\n== C. constructed cases through summarise (landing written before each runs)")
# C1: arm T returns no verdict (control 7 fails on T seeds 0 and 1); C reads; F gate made to pass.
def c1(rows):
    for s in range(3):
        setg(rows, "F", s, own_clears=True, other_clears=True)
    setc(rows, "T", 0, "7", False)
    setc(rows, "T", 1, "7", False)
res, _ = run_case(c1)
check("C1 arm T no verdict, arm C reads -> frozen code gives R2 (RT-241 calls this a hole)",
      res["outcome"]["code"] == "R2", f"{res['outcome']['code']}: {res['outcome']['term']}; T read {res['arms']['T']['read']}")

# C2: arm C seed 2 fails the gate on its own (own-directed below the bar); arm passes on seeds 0, 1.
def c2(rows):
    setg(rows, "C", 2, own_clears=False)
res, _ = run_case(c2)
check("C2 a seed that itself failed the gate still reads when its arm passed (arm-level gate applied to every seed)",
      res["gates"]["C"] and res["per_seed"]["C"][2]["status"] == "reading",
      f"C gate {res['gates']['C']}; C/2 {res['per_seed']['C'][2]['status']} {res['per_seed']['C'][2].get('degree')}")

# C3: the review's A10 table on arm F (own, named-other, collapse):
#     seed 0 P F P; seed 1 P P F; seed 2 F P P.
def c3(rows):
    for s, (o, n, l) in enumerate([(1, 0, 1), (1, 1, 0), (0, 1, 1)]):
        setg(rows, "F", s, own_clears=bool(o), other_clears=bool(n), lesion_collapses_own=bool(l))
res, _ = run_case(c3)
check("C3 the review's own split table: frozen code already FAILS arm F's gate (own and named-other "
      "are joint per seed; only seed 1 passes both)", res["gates"]["F"] is False and res["outcome"]["code"] == "R3",
      f"F gate {res['gates']['F']}; outcome {res['outcome']['code']}")

# C4: a split the frozen code admits but the joint rule would not:
#     seed 0 P P F; seed 1 P P P; seed 2 F P P  (one seed passes everything).
def c4(rows):
    for s, (o, n, l) in enumerate([(1, 1, 0), (1, 1, 1), (0, 1, 1)]):
        setg(rows, "F", s, own_clears=bool(o), other_clears=bool(n), lesion_collapses_own=bool(l))
res, _ = run_case(c4)
check("C4 one seed of three passes everything: frozen code passes arm F's gate and the collapse",
      res["gates"]["F"] is True, f"F gate {res['gates']['F']}; outcome {res['outcome']['code']} "
      f"(F still unread here because the toy F read failed its floor)")

# C5: the two-model fallback (arm C no verdict) with arm F unread -> fifth term with a note, not R1.
def c5(rows):
    for s in range(3):
        setg(rows, "F", s, own_clears=True, other_clears=True)
        setc(rows, "C", s, "4", False)
res, _ = run_case(c5)
check("C5 two-model fallback with arm F unread -> the fifth term with the fallback note (not R1)",
      res["outcome"]["code"] == "fifth" and any("two-arm fallback" in n for n in res["outcome"]["notes"]),
      f"{res['outcome']['code']}: {res['outcome']['term'][:60]}...; notes {len(res['outcome']['notes'])}")

# C6: arms T and C both no verdict -> R2.
def c6(rows):
    for s in range(3):
        setg(rows, "F", s, own_clears=True, other_clears=True)
        setc(rows, "C", s, "4", False)
        setc(rows, "T", s, "7", False)
res, _ = run_case(c6)
check("C6 arms T and C both no verdict -> frozen code gives R2", res["outcome"]["code"] == "R2",
      f"{res['outcome']['code']}")

# C7: does withhold list EVERY reason? Arm F passes its gate, its collapse fails on two seeds,
#     and its read failed its floor at nomination (as on the toy).
def c7(rows):
    for s in range(3):
        setg(rows, "F", s, own_clears=True, other_clears=True, lesion_collapses_own=(s == 0))
res, _ = run_case(c7)
reasons = res["per_seed"]["F"][1]["reasons"]
check("C7 (defect probe) a failed collapse is NOT listed when the seed is already withheld for another reason",
      not any("lesion" in x for x in reasons), "; ".join(reasons))

# C8: arm M reads but outside its band on two seeds -> term unchanged; prediction_met False.
def c8(rows):
    for s in range(3):
        setg(rows, "F", s, own_clears=True, other_clears=True)
    for s in (0, 1):
        r = rows[f"row_M_seed{s}.json"]["primary"]["reading"]
        # the row stores the reading as computed; summarise uses the stored degree, so both are set
        r["accuracy_ownership_only"] = r["accuracy_whole"] - 0.95 * (r["accuracy_whole"] - r["accuracy_untouched"])
        r["degree"] = 0.95
res, _ = run_case(c8)
check("C8 arm M reads outside 0.3 to 0.7 -> outcome term unchanged (fifth), prediction_met False, "
      "nothing about it in the term or notes", res["outcome"]["code"] == "fifth"
      and res["outcome"]["arm_M"]["prediction_met"] is False and not res["outcome"]["notes"],
      f"{res['outcome']['code']}; M readings {[round(v, 3) for v in res['arms']['M']['readings'].values()]}")

# ---------------------------------------------------------------- D
print("\n== D. arm F's three gate conditions (own, named-other, collapse), every pattern on three seeds")
pats = list(itertools.product(itertools.product((0, 1), repeat=3), repeat=3))
sep = lambda P: all(sum(P[s][c] for s in range(3)) >= 2 for c in range(3))
frozen = lambda P: sum(P[s][0] and P[s][1] for s in range(3)) >= 2 and sum(P[s][2] for s in range(3)) >= 2
joint = lambda P: sum(all(P[s]) for s in range(3)) >= 2
allpass = lambda P: sum(all(P[s]) for s in range(3))
print(f"  patterns: {len(pats)}")
print(f"  separate majorities pass, no seed passes all three: {sum(sep(P) and allpass(P) == 0 for P in pats)}")
print(f"  frozen rule passes, no seed passes all three:       {sum(frozen(P) and allpass(P) == 0 for P in pats)}")
print(f"  frozen rule passes, exactly one seed passes all:    {sum(frozen(P) and allpass(P) == 1 for P in pats)}")
print(f"  frozen rule passes, joint rule fails:               {sum(frozen(P) and not joint(P) for P in pats)}")
print(f"  separate passes, frozen fails:                       {sum(sep(P) and not frozen(P) for P in pats)}")

# ---------------------------------------------------------------- E
print("\n== E. the toy gates from raw counts (out-repairs/gate_base.json), bar 790 of 3,000")
os.chdir(ROOT)
g = json.load(open("experiments/rehearsal-successor-measure/out-repairs/gate_base.json"))["runs"]
les = json.load(open("experiments/rehearsal-successor-measure/out-lesion-content-check/lesion_content_check.json"))["models"]
for arm in "TCMF":
    per = []
    for s in range(3):
        r = g[f"{arm}/base/{s}"]
        own = r["own_correct"] >= 790
        oth = round(r["other"] * r["n"]) >= 790
        col = round(r["lesioned_own"] * r["n"]) < 790
        per.append((own, oth, col, bool(les[f"{arm}/{s}"]["holds_own"]) if f"{arm}/{s}" in les else None))
    if arm == "F":
        P = [p[:3] for p in per]
        print(f"  F per seed (own, named-other, collapse, ownership-free line): {per}; separate {sep(P)}, "
              f"frozen {frozen(P)}, joint {joint(P)}")
    else:
        print(f"  {arm} own-directed per seed: {[p[0] for p in per]}")

print(f"\n{len(fails)} not as expected" if fails else "\nevery case landed as written beside it")
