#!/usr/bin/env python3
"""Check 7. Word counts of the refreshed explainer, three ways, each rule stated:
 A. whole file as `wc -w` counts it (whitespace-separated tokens, markdown marks included);
 B. "with citations": the body only (everything after the first '---' rule, so the
    title and the italic header note are out), markdown marks (#, *, ---) dropped;
 C. "prose": B with every parenthetical that contains a backticked file name removed,
    and any other backticked span removed.
The pull request body says about 2,900 words of prose and 3,050 with citations;
the brief asked for under about 2,500. Also the main-line explainer, for the change."""
import re, subprocess
def counts(t):
    a = len(t.split())
    body = t.split("\n---\n", 1)[1] if "\n---\n" in t else t
    body = re.sub(r"[#*]", " ", body)
    b = len(body.split())
    prose = body
    for _ in range(3):  # nested parentheses, innermost first
        prose = re.sub(r"\([^()]*`[^()]*\)", " ", prose)
    prose = re.sub(r"`[^`]*`", " ", prose)
    c = len(prose.split())
    return a, b, c
new = open("explainer.md", encoding="utf-8").read()
old = subprocess.run(["git", "show", "origin/main:explainer.md"], capture_output=True, text=True).stdout
for name, t in (("explainer.md, this branch", new), ("explainer.md, origin/main", old)):
    a, b, c = counts(t)
    print(f"{name}: A whole file {a}; B body with citations {b}; C body prose {c}")
