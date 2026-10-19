#!/usr/bin/env python3
"""Check of pull request 193 (the cost sentence and three "programme" sentences,
on John's "Yes to both"). Run from the worktree root; compares HEAD with origin/main.
1. the cost sentence against this checker's proposal (pull request 192) plus "of rented compute";
2. the three "programme" changes, by main-line line number, against lines 301, 357 and 1107 as named;
3. the Methods addition against compute-ledger.md: what every ledger row is, and what the ledger says it covers;
4. every word the paper's diff changes (word diff), so nothing else can hide;
5. the ruling file's added section against John's relayed words."""
import re, subprocess
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
def flat(t): return re.sub(r"\s+", " ", t).strip()
P = "drafts/paper-removal-test-nature-draft.md"
new = flat(open(P, encoding="utf-8").read())
REC = flat(open("docs/reviews/2026-10-18-paper-reserved-places-check-claude-code.md", encoding="utf-8").read())
prop = re.search(r"> … (and note that this experiment ran for about \$10 to \$20 .*?not resources\.)", REC).group(1)
want = prop.replace("about $230.94 (Methods", "about $230.94 of rented compute (Methods")
print("1. proposal (from the check of 190):", prop)
print("   proposal + 'of rented compute' found in the paper:", want in new)
print("   old sentence gone ('entire programme ran for under $20'):", "entire programme ran for under $20" not in new)
hunks = re.findall(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)", sh("git", "diff", "-U0", "origin/main", "HEAD", "--", P), re.M)
print("2. changed main-line lines (start, count):", hunks)
oldlines = sh("git", "show", "origin/main:" + P).splitlines()
for n in (301, 357, 1107):
    print(f"   main line {n}: {oldlines[n-1].strip()[:90]}")
print("4. word diff of the paper:")
for l in sh("git", "diff", "--word-diff=porcelain", "origin/main", "HEAD", "--", P).splitlines():
    if l[:1] in "-+" and not l.startswith(("---", "+++")): print("   ", l[:160])
L = open("experiments/06-mvm-0a-constructed-self-index/compute-ledger.md", encoding="utf-8").read()
rows = [l for l in L.splitlines() if re.match(r"\| 20\d\d-\d\d-\d\d", l)]
gpu = [r.split("|")[4].strip()[:28] for r in rows]
print(f"3. ledger rows: {len(rows)}; GPU column of each:")
for r, g in zip(rows, gpu): print(f"     {r[2:14]} {g}")
print("   rows naming a model-provider API call as spend:", sum(bool(re.search(r"judge|OpenRouter|Anthropic API|OpenAI|tokens billed", r, re.I)) for r in rows))
i = L.find("RunPod balance at adjudication"); print("   ledger baseline:", flat(L[i:i+230]))
a3 = flat(open("experiments/06-mvm-0a-constructed-self-index/amendment-a3.md", encoding="utf-8").read())
j = a3.find("the Amendment A2 ceiling of $400 covers"); print("   John's ruling of 2026-08-30, as amendment-a3.md quotes it:", a3[j:j+140])
print("   ledger running total on 2026-08-17 (just before that ruling):", re.search(r"~\$149\.8 \+ \$31\.6 → \*\*~\$181\.4", L) is not None)
for k in ["Whole programme to the stop of experiment C: about $230.94", "That figure is rented machine time only.", "whole programme of three registered experiments for about $230.94 of rented compute"]:
    print(f"   paper says {k!r}: {k in new}")
R = flat(open("docs/rulings/2026-10-18-paper-reserved-places-ruling.md", encoding="utf-8").read())
print('5. ruling quotes John: "Yes to both" ->', '"Yes to both"' in R, "| authorship mixed ->", "authorship mixed" in R)
print("   ruling's added section says the $230.94 is rented machine time 'to the stop of experiment C':", "rented machine time to the stop of experiment C" in R)
