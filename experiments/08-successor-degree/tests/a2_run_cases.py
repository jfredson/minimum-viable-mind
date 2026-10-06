"""Run the A2 made-up failure cases through the whole summarise path.

Method: `docs/2026-10-06-successor-a2-decision-procedure-method.md`. The cases
and their expected outcomes are in `a2_cases.py`, committed before this ran.
No model is loaded: only the committed toy rows, copied and edited. $0.

    ~/Code/minimum-viable-mind/.venv/bin/python a2_run_cases.py
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, HERE)
import procedure as P   # noqa: E402
import a2_cases as K    # noqa: E402

TOY = os.path.join(ROOT, "out-freeze-tests", "t3a-committed-reads")
OUT = os.path.join(ROOT, "out-a2-cases")


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_toy():
    rows, sums = {}, {}
    for f in sorted(os.listdir(TOY)):
        if f.startswith("row_") and f.endswith(".json"):
            p = os.path.join(TOY, f)
            sums[f] = sha(p)
            r = json.load(open(p))
            rows[(r["arm"], r["seed"])] = r
    return rows, sums


def figure_strings(x):
    """The figure at full precision and as the table prints it."""
    return {repr(x), f"{x:.4f}"}


def main():
    toy, sums = load_toy()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    results = []
    for case in K.CASES:
        rows = copy.deepcopy(toy)
        case["build"](rows)
        d = os.path.join(OUT, case["name"])
        os.makedirs(d)
        for (a, s), r in rows.items():
            with open(os.path.join(d, f"row_{a}_seed{s}.json"), "w") as f:
                json.dump(r, f, indent=1, sort_keys=True)
        if case.get("steps") is not None:
            with open(os.path.join(d, "steps.json"), "w") as f:
                json.dump(case["steps"], f)
        res = P.summarise(d)
        o = res["outcome"]
        summary_txt = open(os.path.join(d, "summary.json")).read()
        table_txt = open(os.path.join(d, "table.md")).read()
        checks = {}
        checks["outcome code"] = o.get("code") == case["expect"]
        for t in case.get("reason_has", []):
            checks[f"reason has '{t}'"] = t in (o.get("reason") or "")
        for t in case.get("sentence_has", []):
            checks[f"sentence has '{t}'"] = t in (o.get("sentence") or "") + " ".join(o.get("notes") or [])
        for key, texts in case.get("seed_reasons_have", {}).items():
            a, s = key.split("/")
            listed = res["per_seed"][a][int(s)]["reasons"]
            for t in texts:
                checks[f"{key} lists '{t}'"] = any(t in x for x in listed)
        leaks, elsewhere = [], []
        table_lines = table_txt.splitlines()
        for a, s in case.get("withheld", []):
            w = res["per_seed"][a][s]
            checks[f"{a}/{s} withheld"] = w["status"] == "no verdict" and w["degree"] is None
            p = rows[(a, s)].get("primary") or {}
            x = (p.get("reading") or {}).get("degree")
            if x is None:
                continue
            # where the figure would be written if it leaked: the seed's own
            # entry in summary.json, its arm's readings, and its table row
            if w.get("degree") is not None or s in res["arms"][a]["readings"]:
                leaks.append(f"{a}/{s} figure in summary.json readings")
            own_row = [ln for ln in table_lines if ln.startswith(f"| {a}/{s} |")]
            pat = re.compile(r"(?<![0-9.])(" + "|".join(re.escape(f) for f in figure_strings(x)) + r")(?![0-9])")
            for ln in own_row:
                if pat.search(ln):
                    leaks.append(f"{a}/{s} figure in its own table row")
            # anywhere else: listed for the checker, with where it was found
            for name, txt in (("summary.json", summary_txt), ("table.md", table_txt)):
                for m in pat.finditer(txt):
                    ctx = txt[max(0, m.start() - 60):m.end() + 10].replace("\n", " ")
                    elsewhere.append(f"{a}/{s} {m.group(0)} in {name}: ...{ctx}")
        for name, txt in (("summary.json", summary_txt), ("table.md", table_txt)):
            if "arithmetic_withheld" in txt:
                leaks.append(f"field arithmetic_withheld in {name}")
        terms_ok = o.get("registered_term") in P.MS.OUTCOME_TERMS.values()
        checks["term is a registered term"] = terms_ok
        results.append(dict(name=case["name"], about=case["about"], expected=case["expect"],
                            got=o.get("code"), term=o.get("term"), sentence=o.get("sentence"),
                            notes=o.get("notes"), checks=checks, leaks=leaks,
                            same_number_elsewhere=elsewhere,
                            matches=all(checks.values()),
                            per_seed_reasons={f"{a}/{s}": w["reasons"]
                                              for a, ss in res["per_seed"].items() for s, w in ss.items()
                                              if w["reasons"]}))
    out = dict(inputs_sha256=sums, toy_dir=os.path.relpath(TOY, ROOT), cases=results)
    with open(os.path.join(OUT, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    lines = ["# A2 made-up cases: expected against actual", "",
             "| # | case | expected | got | all checks | withheld figure found in outputs | term as reported |",
             "|---|---|---|---|---|---|---|"]
    for i, r in enumerate(results, 1):
        failed = [k for k, v in r["checks"].items() if not v]
        lines.append(f"| {i} | {r['name']} | {r['expected']} | {r['got']} | "
                     f"{'yes' if r['matches'] else 'NO: ' + '; '.join(failed)} | "
                     f"{'; '.join(r['leaks']) or 'none'} | {r['term']} |")
    lines += ["", "Input rows (SHA-256):", ""] + [f"- `{k}` {v}" for k, v in sums.items()]
    with open(os.path.join(OUT, "results.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines[:len(results) + 4]))
    bad = [r["name"] for r in results if not r["matches"] or r["leaks"]]
    print(f"\n{len(results)} cases; {len(bad)} differ from expectation or leak: {bad}")


if __name__ == "__main__":
    main()
