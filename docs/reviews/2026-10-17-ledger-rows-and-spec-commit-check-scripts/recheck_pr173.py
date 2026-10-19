#!/usr/bin/env python3
"""Re-check of pull request 173 after the five conditions of the check were
applied (commit 950dfe1, 2026-10-18), with John's two answers of the same day.

Reads committed git objects only. Writes nothing. Calls no model.

    python3 -I recheck_pr173.py > recheck_pr173.out.txt
"""
import difflib
import hashlib
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True, check=True).stdout.strip()

CHECKED = "38133fc"   # the branch head this check last read (commit 3, RT-283 ruling)
MERGE = "92bc33b"     # pull request 179 (this check's record) merged into the branch
FIX = "950dfe1"       # the five conditions applied, with John's two answers
V3C = "bfd1d5d"       # version 3 as merged
LEDGER = "experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md"
SPEC = "spec/minimum-viable-mind-proposal-v0.1.md"
V3F = "docs/rulings/2026-10-12-two-sided-question-section-2-v3.md"
RULING = "docs/rulings/2026-10-18-rt283-closure-ruling.md"
CI = "experiments/01-self-indexing-removal-test/removal_ci.json"
OLD_SHA = "3d0baaca5fbf1af08d86652e455ca4e0462c98f7fb424fde09292623256df119"
NEW_SHA = "c824cd81b53b3cebc3a0dda350b63ece66c54c6dd77e6580eb132466eb7d0413"
# John's two answers as the requesting session relayed them on 2026-10-18
RELAYED_283 = "his RT-283 reading and its rehearsal condition cover both copies of the observer comparison"
RELAYED_CLAUSE = "the first and third intervals above zero and the second, from 0.00 to 0.20, touching it"


def show(rev, path):
    return subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"],
                          capture_output=True, check=True).stdout


def text(rev, path):
    return show(rev, path).decode()


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True, check=True).stdout


def head(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("’", "'")
    return re.sub(r"\s+", " ", s.replace("**", "").replace("`", "")).lower()


def rows(rev):
    out = {}
    for ln in text(rev, LEDGER).splitlines():
        m = re.match(r"^\| RT-(\d+)\b", ln)
        if m:
            out[int(m.group(1))] = [c.strip() for c in ln.strip().strip("|").split(" | ")]
    return out


head(f"R0. What the fix commit {FIX} touches")
print(f"  parent of {FIX}: {git('rev-parse', '--short', FIX + '^').strip()} (expected {MERGE})")
print("  files:", git("diff", "--name-status", MERGE, FIX).split("\n")[:-1])
ra, rb = rows(CHECKED), rows(FIX)
changed = {n: [i + 1 for i, (x, y) in enumerate(zip(ra[n], rb[n])) if x != y] for n in rb if ra.get(n) != rb[n]}
print(f"  ledger rows changed {CHECKED}..{FIX}, with the cells changed: {changed}")
print(f"  rows added or removed: {sorted(set(ra) ^ set(rb))}")
la, lb = text(CHECKED, LEDGER).splitlines(), text(FIX, LEDGER).splitlines()
sm = difflib.SequenceMatcher(None, la, lb, autojunk=False)
other = [(op, i1 + 1, i2, j1 + 1, j2) for op, i1, i2, j1, j2 in sm.get_opcodes()
         if op != "equal" and not all(re.match(r"^\| RT-(283|284|292|304)\b", l) for l in la[i1:i2] + lb[j1:j2])]
print(f"  ledger changes other than those four rows: {other}")
for op, i1, i2, j1, j2 in other:
    print("    first added line:", lb[j1 - 1][:90] if j2 >= j1 else "-")

head("R1. Condition 1: RT-284's counts are the closure output's")
c = norm(rb[284][4])
for p in ("ten hits", "nine rows in the check file's table; line 87 holds two",
          "four pass the script's strict substring test and six are flagged", "nine hits", "three of the nine"):
    print(f"  {p!r} in RT-284's closure cell: {norm(p) in c}")

head("R2. Condition 2 and John's first answer: RT-283 covers both copies")
c = norm(rb[283][4])
ru = text(FIX, RULING)
print(f"  RT-283 names spec line 365: {'spec line 365' in c}; quotes the second copy: "
      f"{norm('may detect no more presence in the constructed systems than in the frontier reference profile') in c}")
q283 = re.findall(r'"(my RT-283 reading[^"]*)"', rb[283][4])
qru = re.findall(r'"(my RT-283 reading[^"]*)"', re.sub(r"\s+", " ", ru))
print(f"  John's words in the row:          {q283}")
print(f"  John's words in the ruling file:  {qru}")
print(f"  row == ruling file: {q283 == qru}; equal to the relayed words with 'his' for 'my': "
      f"{[q.replace('my ', 'his ', 1) for q in q283] == [RELAYED_283]}")
print(f"  ruling file diff {CHECKED}..{FIX}: removed lines "
      f"{sum(1 for l in git('diff', '-U0', CHECKED, FIX, '--', RULING).splitlines() if l.startswith('-') and not l.startswith('---'))}")
print(f"  the earlier ruling quote is still in the row: "
      f"{norm('RT-283 closes on reading: the surviving sentence is a different comparison, guarded as a question and not a finding.') in c}")

head("R3. Condition 3 and John's second answer: RT-292 and the Floor sentence's interval clause")
sa, sb = show(CHECKED, SPEC), show(FIX, SPEC)
print(f"  spec SHA-256 at {CHECKED}: {hashlib.sha256(sa).hexdigest()} (expected {OLD_SHA[:12]}…: {hashlib.sha256(sa).hexdigest() == OLD_SHA})")
print(f"  spec SHA-256 at {FIX}: {hashlib.sha256(sb).hexdigest()} (expected {NEW_SHA[:12]}…: {hashlib.sha256(sb).hexdigest() == NEW_SHA})")
al, bl = sa.decode().split("\n"), sb.decode().split("\n")
diff_lines = [i + 1 for i in range(max(len(al), len(bl))) if i >= len(al) or i >= len(bl) or al[i] != bl[i]]
print(f"  spec lines {len(al)} -> {len(bl)}; lines that differ: {diff_lines}")
for i in diff_lines:
    m = difflib.SequenceMatcher(None, al[i - 1], bl[i - 1], autojunk=False)
    ops = [(op, al[i - 1][i1:i2], bl[i - 1][j1:j2]) for op, i1, i2, j1, j2 in m.get_opcodes() if op != "equal"]
    print(f"  line {i}: {len(ops)} change(s)")
    for op, x, y in ops:
        print(f"    {op}: {x!r} -> {y!r}")
old_clause, new_clause = "each interval above zero", RELAYED_CLAUSE
rebuilt = sa.decode().replace(old_clause, new_clause, 1).encode()
print(f"  the spec at {CHECKED} with only {old_clause!r} replaced by the relayed wording equals the spec at {FIX}: {rebuilt == sb}")
print(f"  counts at {FIX}: {old_clause!r} {sb.decode().count(old_clause)}; relayed wording {sb.decode().count(new_clause)}")
ci = json.loads(text(FIX, CI))["cells"]["idxres_mean_k16"]
iv = [(k, ci[k]["point"], ci[k]["lo"], ci[k]["hi"]) for k in ("T_self_irrelevant", "T_self_relevant", "T_syntax")]
print("  removal_ci.json, primary condition (the C8 read re-run):")
for k, p, lo, hi in iv:
    print(f"    {k}: {p:.4f} [{lo:.4f}, {hi:.4f}]  lower bound above zero: {lo > 0}; equal to zero: {lo == 0}")
print(f"  the clause's order matches the sentence's figures (0.22, 0.10, 0.13 = self-irrelevant, self-relevant, syntax): "
      f"{[round(p, 2) for _, p, _, _ in iv] == [0.22, 0.10, 0.13]}")
print(f"  'first and third above zero': {iv[0][2] > 0 and iv[2][2] > 0}; "
      f"'second, from 0.00 to 0.20, touching it': {(round(iv[1][2], 2), round(iv[1][3], 2)) == (0.0, 0.2) and iv[1][2] == 0}")
c4, c5 = norm(rb[292][3]), norm(rb[292][4])
print(f"  RT-292 closure cell starts 'Open': {rb[292][4].startswith('**Open')}; records 0.0000 to 0.2000: "
      f"{'[0.0000, 0.2000]' in rb[292][4]}; gives the corrected wording: {norm(new_clause) in c5}")
print(f"  RT-292 disposition marks 'each interval above zero' as version 3's words the record contradicts: "
      f"{norm('version 3' + chr(39) + 's words \"each interval above zero\"') in c4 and 'contradicts' in c4}")
qj = re.findall(r'"(fix the removal-test[^"]*)"', rb[292][4])
print(f"  words the RT-292 row quotes as John's: {qj}")
hits = git("grep", "-l", "-F", "fix the removal-test interval sentence", FIX).split()
print(f"  committed files at {FIX} containing them: {hits}")

head("R4. Condition 4: RT-304 quotes the Floor sentence as it reads")
q = "treats the test as its definition of the floor and not as an instrument for it"
print(f"  RT-304 disposition: {re.findall(r'\"[^\"]*definition of the floor[^\"]*\"', rb[304][3])}")
frags = [f.strip(" .") for f in re.split(r"\.\.\.|…", re.findall(r'"([^"]*definition of the floor[^"]*)"', rb[304][3])[0])]
fl = norm(bl[262])
print(f"  each fragment of that quote is in the Floor line at {FIX}: {[(f, norm(f) in fl) for f in frags]}")
print(f"  {q!r} in the Floor line: {norm(q) in fl}")

head("R5. Condition 5: a dated note on the count, and does it match the rows")
words = {}
for n in range(283, 305):
    m = re.match(r"\*\*(Open|Closed: the claim was checked|Closed: the argument was accepted|Closed on John's reading)", rb[n][4])
    words.setdefault(m.group(1) if m else "UNMATCHED", []).append(n)
print("  closure words over the 22 rows at", FIX + ":", "; ".join(f"{k}: {len(v)} {v}" for k, v in words.items()))
note = re.sub(r"\s+", " ", "\n".join(lb[lb.index(next(l for l in lb if l.startswith("*Dated note, 2026-10-18 (Pacific), after the pairing-rule check"))):][:13]))
print(f"  the dated note on the count is present: {bool(note)}")
for lab, p in (("checked 2", "closed with the claim checked 2 (RT-289, RT-284)"), ("accepted 17", "closed with the argument accepted 17"),
               ("reading 1", "closed on John's reading 1 (RT-283)"), ("open 2", "open 2 (RT-292 until its re-check, and RT-302")):
    print(f"    {lab}: {norm(p) in norm(note)}")

head("R6. Version 3 below its notes still equals bfd1d5d")
v = show(FIX, V3F).split(b"\n")
body = next(i for i in range(1, len(v)) if v[i].startswith(b"*Written 2026-10-12"))
print(f"  version 3 at {FIX} with its lines 3..{body} (its three dated notes) removed equals {V3C}: "
      f"{b'\n'.join(v[:2] + v[body:]) == show(V3C, V3F)}")
d = git("diff", "-U0", CHECKED, FIX, "--", V3F)
print(f"  diff {CHECKED}..{FIX}: blocks {re.findall(r'(?m)^@@.*@@', d)}; removed "
      f"{sum(1 for l in d.splitlines() if l.startswith('-') and not l.startswith('---'))}")
n3 = norm(b"\n".join(v[30:body]).decode())
print(f"  the new note gives the corrected wording: {norm(RELAYED_CLAUSE) in n3}; the new checksum: {NEW_SHA in n3}")
sec = b"\n".join(show(V3C, V3F).split(b"\n")[74:293])
print(f"  the section in the spec still equals version 3 lines 75..293: {sec in sb}")
