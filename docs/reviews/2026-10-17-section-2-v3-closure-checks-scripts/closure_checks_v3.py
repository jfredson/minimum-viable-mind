#!/usr/bin/env python3
"""Closure checks on the three fatal findings of the Gate A pass on section 2
(RT-283, RT-284, RT-289), run against section 2 VERSION 3
(docs/rulings/2026-10-12-two-sided-question-section-2-v3.md) as it would read
once written into spec/minimum-viable-mind-proposal-v0.1.md.

Everything is read from the main line of the repository at a named commit, so
the output is reproducible. The check C4 assembly and its four search patterns
are the tier 1 reviewer's own
(docs/reviews/2026-10-09-two-sided-question-gate-a-scripts/gate_a_checks.py,
lines 106 to 135), carried over unchanged so that the closure check is "the same
command on the revised spec" as the tier 1 note asks.

Run from the repository root:  python3 closure_checks_v3.py <main-line commit>
"""
import hashlib
import re
import subprocess
import sys

REV = sys.argv[1] if len(sys.argv) > 1 else "main"
V3 = "docs/rulings/2026-10-12-two-sided-question-section-2-v3.md"
SPEC = "spec/minimum-viable-mind-proposal-v0.1.md"
RULINGS = "docs/rulings/2026-10-07-two-sided-question-rulings.md"


def show(rev, path):
    return subprocess.run(["git", "show", f"{rev}:{path}"], check=True,
                          capture_output=True, text=True).stdout


def sha(t):
    return hashlib.sha256(t.encode()).hexdigest()


def head(t):
    print(); print("=" * 78); print(t); print("=" * 78)


commit = subprocess.run(["git", "rev-parse", "--short", REV], check=True,
                        capture_output=True, text=True).stdout.strip()
v3 = show(REV, V3)
spec = show(REV, SPEC)
vlines = v3.splitlines()
slines = spec.splitlines()

head(f"C0. The text under check, at main-line commit {commit}")
print(f"  {V3}: SHA-256 {sha(v3)}")
print(f"  {SPEC}: SHA-256 {sha(spec)}")

# Section 2 version 3's three pieces of text for the spec.
s_start = next(i for i, l in enumerate(vlines) if l.startswith("### The Question This Project Measures"))
floor_h = next(i for i, l in enumerate(vlines) if l.startswith('**The sentence added to "The Floor"**'))
para_h = next(i for i, l in enumerate(vlines) if l.startswith('**The paragraph added to "What Would Count Against It"**'))
log_h = next(i for i, l in enumerate(vlines) if l.startswith("## Change log"))
# the spec section proper ends at the horizontal rule before the Floor sentence heading
rule_before_floor = max(i for i in range(s_start, floor_h) if vlines[i].strip() == "---")
spec_block = vlines[s_start:rule_before_floor]
while spec_block and spec_block[-1].strip() == "":
    spec_block.pop()
floor_quote = [l for l in vlines[floor_h:para_h] if l.startswith(">")]
para_quote = [l for l in vlines[para_h:log_h] if l.startswith(">")]
floor_sentence = " ".join(l.lstrip("> ").strip() for l in floor_quote)
para_text = " ".join(l.lstrip("> ").strip() for l in para_quote)
print(f"  section 2 proper: v3 lines {s_start + 1} to {rule_before_floor} "
      f"({len(spec_block)} lines, {len(' '.join(spec_block).split())} words)")
print(f"  Floor sentence: {len(floor_quote)} quoted lines, {len(floor_sentence.split())} words")
print(f"  'What Would Count Against It' paragraph: {len(para_quote)} quoted lines, {len(para_text.split())} words")

head("C1. The three insertion points, in the spec as it stands")
anchors = {
    'heading "## What This Proposal Is" (section 2 goes before it, after Scope)': r"^## What This Proposal Is",
    'Floor sentence anchor "...was a description all along"': r"A self-model that can be lopped off while the computation runs was a description all along",
    'fourth condition "And if the depth mechanisms produced systems..."': r"^And if the depth mechanisms produced systems that pass the five external indicators",
}
for name, pat in anchors.items():
    hits = [i + 1 for i, l in enumerate(slines) if re.search(pat, l)]
    print(f"  {len(hits)} match(es) for {name}: lines {hits}")

# Assemble the spec as it would read after the commit.
scope_end = next(i for i, l in enumerate(slines) if l.startswith("## What This Proposal Is")) - 1
assembled = list(slines)
anchor_i = next(i for i, l in enumerate(assembled) if "was a description all along" in l)
assembled[anchor_i] = assembled[anchor_i] + " " + floor_sentence
fourth_i = next(i for i, l in enumerate(assembled) if l.startswith("And if the depth mechanisms produced"))
assembled = assembled[:fourth_i + 1] + ["", para_text] + assembled[fourth_i + 1:]
assembled = assembled[:scope_end] + spec_block + ["", "---", ""] + assembled[scope_end:]
assembled_text = "\n".join(assembled) + "\n"
block_set = set(spec_block)
sec2_text = "\n".join(spec_block) + "\n" + floor_sentence + "\n" + para_text + "\n"
print(f"  assembled spec: {len(assembled)} lines (spec as it stands: {len(slines)} lines)")
print(f"  SHA-256 of the assembled spec: {sha(assembled_text)}")

head("RT-283 closure check (tier 1 note, under RT-283): on the revised text, "
     "'no better than' 0, 'fluency measures' 0, and the rulings file cited where ruling 10 is stated")
for needle in ("no better than", "fluency measures"):
    n_sec2 = sec2_text.count(needle)
    n_all = assembled_text.count(needle)
    print(f"  grep -c \"{needle}\"  -> section 2 text: {n_sec2}; whole assembled spec: {n_all}")
hits = [l for l in spec_block if "ruling 10" in l.lower() or "ruling 10" in l]
print(f"  lines of section 2 that mention ruling 10: {len(hits)}")
for l in hits:
    print("    | " + l.strip()[:160])
cited = [l for l in spec_block if RULINGS in l]
print(f"  lines of section 2 citing {RULINGS} by path: {len(cited)}")
# the rulings file is cited across a line break if the path spans two lines; check the joined text too
joined = " ".join(l.strip() for l in spec_block)
print(f"  the path appears in the joined section text: {joined.count(RULINGS)} time(s)")
r10_ctx = [m.start() for m in re.finditer(r"ruling 10", joined)]
for pos in r10_ctx:
    window = joined[max(0, pos - 400): pos + 200]
    print(f"  within 400 characters before a 'ruling 10' mention, the path appears: {RULINGS in window}")

head("RT-289 closure check (v3 file, under RT-289): 'degree measured' 0, 'at a degree' 0, "
     "'non-zero' 1 in the section text and the hit is the sentence about Scope's 'non-zero'")
for needle in ("degree measured", "at a degree"):
    print(f"  grep -c \"{needle}\"  -> section 2 text: {sec2_text.count(needle)}; whole assembled spec: {assembled_text.count(needle)}")
nz_sec2 = [l for l in (spec_block + [floor_sentence, para_text]) if "non-zero" in l]
print(f"  grep -c \"non-zero\"  -> section 2 text (the three inserts): {len(nz_sec2)}")
for l in nz_sec2:
    print("    | " + l.strip()[:200])
nz_spec = [(i + 1, l) for i, l in enumerate(slines) if "non-zero" in l]
print(f"  'non-zero' in the spec as it stands (John's unchanged text): {len(nz_spec)} line(s): {[i for i, _ in nz_spec]}")
print(f"  'non-zero' in the whole assembled spec: {sum(1 for l in assembled if 'non-zero' in l)} line(s)")
# "non-zero" split over a line break in the v3 file
print(f"  'non-zero' with the hyphen split across a line break in section 2: {len(re.findall(r'non-\n\s*zero', chr(10).join(spec_block)))}")
print(f"  'degree' in the section text at all: {len(re.findall(r'\bdegree\b', sec2_text))} hit(s)")
for m in re.finditer(r"[^.]*\bdegree\b[^.]*\.", " ".join(sec2_text.split())):
    print("    | " + m.group(0).strip()[:220])

head("RT-284 closure check (tier 1 note, under RT-284; check C4 on the revised spec): the same four searches, "
     "every hit in the unchanged groups named in the supersession paragraph")
paras, cur, origin = [], [], []
for l in assembled:
    if l.strip() == "":
        if cur:
            paras.append(" ".join(x.strip() for x in cur))
            origin.append("section 2" if all(x in block_set for x in cur) else "spec")
        cur = []
    else:
        cur.append(l)
if cur:
    paras.append(" ".join(x.strip() for x in cur)); origin.append("spec")
print(f"  assembled spec: {len(paras)} paragraphs")
checks = [
    ("what 'minimum viable' names", r"[Mm]inimum viable\" names|minimum viable conscious machine a two-part definition|[Mm]inimum viable mind is"),
    ("the removal test used as an instrument or pass-fail criterion", r"subject to a removal test|pass-fail criterion is the removal test|removal test as the intuition|settled by removal|survives the removal test"),
    ("the removal test called a definition, not an instrument", r"definition and not an instrument|definition, not an instrument"),
    ("whether the floor or the binding is measured", r"does not measure the floor|targets the \*\*minimum measurable|Interpretability is the route|measurement that speaks to an inside|floor is not measured"),
]
sup_i = next(i for i, l in enumerate(spec_block) if l.startswith("**What this section supersedes.**"))
supersession = " ".join(l.strip() for l in spec_block[sup_i:])
supersession_plain = supersession.replace("**", "")
print(f"  the supersession paragraph: {len(supersession_plain.split())} words")
unnamed = []
for label, pat in checks:
    print(f"  {label}:")
    for o, ptxt in zip(origin, paras):
        for m in re.finditer(pat, ptxt):
            where = o
            if o == "spec" and floor_sentence[:40] in ptxt and m.start() > ptxt.find(floor_sentence[:40]) >= 0:
                where = "Floor sentence (added)"
            elif o == "spec" and ptxt.startswith(para_text[:40]):
                where = "paragraph (added)"
            elif o == "section 2" and ptxt.startswith("What this section supersedes"):
                where = "section 2, supersession paragraph"
            elif o == "spec":
                where = "spec, unchanged"
            s = max(0, m.start() - 60); e = min(len(ptxt), m.end() + 60)
            snippet = ptxt[s:e].replace("\n", " ")
            print(f"    [{where}] ...{snippet}...")
            if where == "spec, unchanged":
                # is this unchanged sentence named (quoted) in the supersession paragraph?
                key = ptxt[m.start():m.end()].replace("**", "")
                named = key in supersession_plain
                print(f"        named in the supersession paragraph: {named}")
                if not named:
                    unnamed.append((label, key))
print()
print(f"  unchanged-spec hits NOT named in the supersession paragraph: {len(unnamed)}")
for label, key in unnamed:
    print(f"    - [{label}] \"{key}\"")
print("  the supersession paragraph's closing rule:")
m = re.search(r"Where any sentence[^.]*\.", supersession_plain)
print("    | " + (m.group(0) if m else "NOT FOUND"))

head("Also: the one other thing the v3 file says the spec commit changes")
print("  v3 says Scope, The Floor and The Build are not edited or annotated; the commit inserts three pieces of text only.")
print(f"  lines of the spec as it stands that the assembly changed in place: 1 (the Floor anchor line, by appending the sentence)")
print(f"  lines inserted: {len(assembled) - len(slines)}")
