#!/usr/bin/env python3
"""Check 4 (and 5) of the check of pull request 190: did the spelling pass change
spelling only, and did anything else in the draft move?

(a) Word diff of the paper, main line against the branch (git's own word diff,
    tokens split on whitespace). Each removed/added pair is normalised the same
    way on both sides (British -> American endings: -ise/-isation/-yse, centre,
    -our, licence, artefact, programme, modell-). A pair whose two sides
    normalise to the same word is SPELLING; anything else is printed as OTHER
    so it can be matched by hand to one of the ruled edits.
(b) Every double-quoted passage, *italic* span and `code` span in the main-line
    file and in the branch file, compared as sets: a quotation, path or label
    the pass altered shows up as present on one side only.
(c) American spellings left on the branch, with whether each sits inside a
    quotation, a code span or a label (has an underscore)."""
import re, subprocess
P = "drafts/paper-removal-test-nature-draft.md"
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
old, new = sh("git", "show", "origin/main:" + P), open(P, encoding="utf-8").read()
def norm(w):
    w = w.lower()
    for a, b in [("isation", "ization"), ("ising", "izing"), ("ised", "ized"), ("ises", "izes"), ("ise", "ize"),
                 ("yse", "yze"), ("centre", "center"), ("behaviour", "behavior"), ("favour", "favor"), ("colour", "color"),
                 ("licence", "license"), ("artefact", "artifact"), ("programme", "program"), ("modell", "model"), ("labell", "label")]:
        w = w.replace(a, b)
    return w
lines = sh("git", "diff", "--word-diff=porcelain", "-U0", "origin/main", "HEAD", "--", P).splitlines()
groups, cur = [], {"-": [], "+": []}
for l in lines:
    if l.startswith(("---", "+++", "@@", "diff", "index")): continue
    if l and l[0] in "-+": cur[l[0]].append(l[1:])
    else:
        if cur["-"] or cur["+"]: groups.append(cur)
        cur = {"-": [], "+": []}
if cur["-"] or cur["+"]: groups.append(cur)
spell = other = 0
print("(a) word-diff groups")
for g in groups:
    a, b = " ".join(g["-"]), " ".join(g["+"])
    if a.split() and len(a.split()) == len(b.split()) and all(norm(x) == norm(y) for x, y in zip(a.split(), b.split())):
        spell += 1
    else:
        other += 1
        print(f"   OTHER  - {a[:160]!r}\n          + {b[:160]!r}")
print(f"   {spell} spelling-only groups, {other} other groups")
def paras(t): return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", t) if p.strip()]
def spans(p):
    q = p.replace("**", "")
    return {"quoted": re.findall(r'"[^"]+"', q), "italic": re.findall(r"(?<![\w*])\*[^*\s][^*]*?\*(?![\w*])", q),
            "code": re.findall(r"`[^`]+`", p)}
po, pn = paras(old), paras(new)
print(f"\n(b) paragraphs: {len(po)} on main, {len(pn)} on branch; quoted, italic and code spans that differ, paragraph by paragraph")
for i, (a, b) in enumerate(zip(po, pn), 1):
    if a == b: continue
    sa, sb = spans(a), spans(b)
    for k in sa:
        if sa[k] != sb[k]:
            print(f"   ¶{i} {k}: main {[x[:70] for x in sa[k] if x not in sb[k]]}  branch {[x[:70] for x in sb[k] if x not in sa[k]]}")
print("\n(c) American spellings left on the branch")
AM = re.compile(r"\b\w*(?:iz(?:e|ed|es|ing|ation|ations)|yz(?:e|ed|es|ing))\b|\bcenter\w*|\bbehavior\w*|\b\w*favor\w*|\bcolor\w*|\bartifact\w*|\bprogram\b|\bprograms\b|\blicense\b|\bmodeling\b|\banalog\b|\bdefense\b|\boffense\b|\bcatalog\w*|\bdialog\b|\bgray\b|\bskeptic\w*|\bfulfill\w*|\benroll\b|\b\w+(?:eled|eling)\b|\bjudgment\w*|\bcounselor\b|\bmaneuver\w*", re.I)
for i, l in enumerate(new.splitlines(), 1):
    for m in AM.finditer(l):
        w = m.group(0)
        if w.lower() in {"size", "sized", "sizes", "prize", "seize", "capsize", "feeling", "wheeled", "peeled", "steeled"}: continue
        before = l[:m.start()]
        where = ("code" if before.count("`") % 2 else "quote" if before.count('"') % 2 else "label" if "_" in w or re.search(r"\w_$", before) else "PROSE")
        print(f"   {where:<5} line {i}: {w}  …{l[max(0, m.start()-50):m.end()+30]}…")
