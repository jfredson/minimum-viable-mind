"""Could the other session's code change (branch `ruled-code-changes-2026-10-09`:
the fitting limit, the outcome words, the summary wording for fewer than three
seeds) affect the three verdicts? Compares, function by function, the parts of
the frozen code each verdict rests on, on main and on that branch.

    ~/Code/minimum-viable-mind/.venv/bin/python \
        docs/reviews/2026-10-09-serious-findings-closure-check-scripts/other_branch_effect.py
"""
from __future__ import annotations

import ast
import subprocess

BRANCH = "origin/ruled-code-changes-2026-10-09"
SRC = "experiments/08-successor-degree/src"

# what each verdict rests on
RESTS_ON = {
    "the floor's missing condition (RT-238)": {
        "measure.py": ["floor_check", "reading"],
        "procedure.py": ["grid", "pick", "pick_sensitivity", "measure_at", "site_family"],
    },
    "the episode format (RT-239)": {
        "grammar.py": ["_content", "render", "make_pairs", "eligible_models", "successor", "build_vocab"],
    },
    "control 6 (RT-251)": {
        "procedure.py": ["measure_at", "table"],
        "measure.py": ["withhold", "arm_outcome", "outcome"],
    },
}


def show(rev, path):
    return subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True, check=True).stdout


def funcs(text):
    tree = ast.parse(text)
    return {n.name: ast.get_source_segment(text, n) for n in ast.walk(tree)
            if isinstance(n, (ast.FunctionDef, ast.ClassDef))}


def main():
    print("branch at", subprocess.run(["git", "rev-parse", "--short", BRANCH], capture_output=True,
                                      text=True).stdout.strip())
    cache = {}
    for verdict, files in RESTS_ON.items():
        print(f"\n== {verdict}")
        for f, names in files.items():
            if f not in cache:
                cache[f] = (funcs(show("main", f"{SRC}/{f}")), funcs(show(BRANCH, f"{SRC}/{f}")),
                            show("main", f"{SRC}/{f}"), show(BRANCH, f"{SRC}/{f}"))
            a, b, ta, tb = cache[f]
            for n in names:
                if n not in a:
                    print(f"   {f}:{n}: not a function on main")
                    continue
                same = a.get(n) == b.get(n)
                print(f"   {f}:{n}: {'identical' if same else 'CHANGED'} on the branch")
    # the grammar's two named self-tests, line by line
    ta, tb = cache["grammar.py"][2], cache["grammar.py"][3]
    for key in ("matched pairs are token-for-token identical", "no name badge"):
        la = [l for l in ta.splitlines() if key in l]
        lb = [l for l in tb.splitlines() if key in l]
        print(f"   grammar.py self-test line '{key}': {'identical' if la == lb else 'CHANGED'}")
    for const in ("SEQ_LEN = ", "POOLS = ", "N_AGENTS = ", "N_SLOTS = "):
        la = [l for l in ta.splitlines() if l.startswith(const)]
        lb = [l for l in tb.splitlines() if l.startswith(const)]
        print(f"   grammar.py constant {const.strip(' =')}: {'identical' if la == lb else 'CHANGED'}")
    # the control-6 label the branch prints
    tb_p = cache["procedure.py"][3]
    print("\n   control 6 lines on the branch's procedure.py:")
    for l in tb_p.splitlines():
        if "control 6" in l or "c['6']" in l or 'c["6"]' in l:
            print("     ", l.strip()[:150])
    # the branch brings in the outcome words "instrument discriminates ...";
    # list any line with a word of discrimination that is not one of those
    print("   branch lines with a word of discrimination outside the outcome words:")
    n = 0
    for f in ("measure.py", "procedure.py", "grammar.py"):
        for i, l in enumerate(show(BRANCH, f"{SRC}/{f}").splitlines(), 1):
            low = l.lower()
            if ("discriminat" in low or "distinguish" in low) and "mechanism" not in low:
                n += 1
                print(f"      {f}:{i}: {l.strip()[:150]}")
    print(f"   ({n} such lines)")


if __name__ == "__main__":
    main()
