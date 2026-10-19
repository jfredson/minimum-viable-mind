#!/usr/bin/env python3
"""Check 1, second half: every number in the new text that the pull request
body does not list. New text = the lines pull request 175 adds to the paper
draft (git diff origin/main...HEAD) and the whole refreshed explainer. A number
is any run of digits with optional commas, decimal point and sign. Dates
(YYYY-MM-DD), commit hashes and section numbers after "section"/"§" are skipped.
Prints each unlisted number with the file and line where it appears, so each
one can be traced by hand (the trace is in the review record)."""
import re, subprocess
body = open("docs/reviews/2026-10-17-paper-fold-check-scripts/pr175-body.md", encoding="utf-8").read()
NUM = re.compile(r"(?<![\w.])[+−-]?\d[\d,]*(?:\.\d+)?")
def norm(n): return n.replace("−", "-").lstrip("+").replace(",", "")
listed = {norm(n) for n in NUM.findall(body)}
def strip(line):
    line = re.sub(r"\d{4}-\d{2}-\d{2}", " ", line)
    line = re.sub(r"`[0-9a-f]{7,}`", " ", line)
    line = re.sub(r"(section|sections|§|decision|item|revisions?|step|Fig\.|Figs\.|Table|Q|K|S|L|RT-|A|v)\s?\d+(\.\d+)?", " ", line)
    line = re.sub(r"`[^`]*`", " ", line)  # file names and code
    return line
diff = subprocess.run(["git", "diff", "-U0", "origin/main...HEAD", "--", "drafts/paper-removal-test-nature-draft.md"],
                      capture_output=True, text=True).stdout
added = [(i, l[1:]) for i, l in enumerate(diff.splitlines()) if l.startswith("+") and not l.startswith("+++")]
expl = list(enumerate(open("explainer.md", encoding="utf-8").read().splitlines(), 1))
seen = {}
for src, lines in (("paper (added lines)", added), ("explainer.md", expl)):
    for i, l in lines:
        for n in NUM.findall(strip(l)):
            k = norm(n)
            if k in listed or k in {"0", "1", "2", "3", "4", "5"}: continue
            seen.setdefault((src, k), []).append(l.strip()[:110])
for (src, k), ls in sorted(seen.items()):
    print(f"{src:<20} {k:<14} {ls[0]}")
print(f"\n{len(seen)} unlisted (file, number) pairs")
