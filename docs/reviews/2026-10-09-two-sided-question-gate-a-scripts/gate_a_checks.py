"""Gate A tier 1 checks on the two-sided question text (section 2 of the
refounding proposal, version 2), and the failure-mode pass's sweeps.

Written 2026-10-09 by the tier 1 reviewing session, which wrote none of the
proposal, the battery draft, the spec or the founding-wager proposal. Reads
committed files only (git show at pinned commits, plus the book summary by
path and checksum); calls no model, rents nothing, spends nothing.

    python3 -I gate_a_checks.py            # from anywhere inside the checkout

Pinned inputs:
  main line            d60ff2e  (the merge of pull request 158)
  battery draft v4     3eee588  (branch felt-features-table-2026-10-09, pull request 164)
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

MAIN = "d60ff2e"
BATTERY = "3eee588"
PROPOSAL = "docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md"
RULINGS = "docs/rulings/2026-10-07-two-sided-question-rulings.md"
SPEC = "spec/minimum-viable-mind-proposal-v0.1.md"
WAGER = "docs/founding-wager-proposal-2026-09-20.md"
BATTERY_FILE = "docs/filtered-battery-proposal-2026-10-07.md"
EXP1_CI = "experiments/01-self-indexing-removal-test/removal_ci.json"
EXP1_FINDINGS = "experiments/01-self-indexing-removal-test/removal-test-findings.md"
BOOK = Path.home() / "Code" / "calibration-problem" / "editorial" / "argument-summary-2026-10-07.md"
BOOK_SHA_CITED = "73881ae66e233b7ccf9037a9855614f6c003de473e15f16198666b7bf2847ecb"


def show(rev: str, path: str) -> str:
    return subprocess.run(["git", "show", f"{rev}:{path}"], check=True, capture_output=True, text=True).stdout


def sha(t: str) -> str:
    return hashlib.sha256(t.encode()).hexdigest()


def head(t: str) -> None:
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


prop = show(MAIN, PROPOSAL)
plines = prop.splitlines()
s2_start = next(i for i, l in enumerate(plines) if l.startswith("## 2. "))
s2_end = next(i for i, l in enumerate(plines) if l.startswith("## 3. "))
sec2 = plines[s2_start:s2_end]
sec2_text = "\n".join(sec2)
# the spec text proper: between the first and second '---' rules inside section 2
rules = [i for i, l in enumerate(sec2) if l.strip() == "---"]
spec_block = sec2[rules[0] + 1:rules[1]]
after_block = sec2[rules[1] + 1:]
spec = show(MAIN, SPEC)
slines = spec.splitlines()
battery = show(BATTERY, BATTERY_FILE)
wager = show(MAIN, WAGER)
rulings = show(MAIN, RULINGS)

head("C0. The text under review")
print(f"proposal {PROPOSAL} at {MAIN}: section 2 is lines {s2_start + 1} to {s2_end} ({len(sec2)} lines)")
print(f"  SHA-256 of section 2 as extracted: {sha(sec2_text + chr(10))}")
print(f"  the spec section proper (between the two rules): lines {s2_start + rules[0] + 2} to "
      f"{s2_start + rules[1]} ({len(spec_block)} lines, {len(' '.join(spec_block).split())} words)")
print(f"  the two additions after the second rule: lines {s2_start + rules[1] + 2} to {s2_end} "
      f"({len(after_block)} lines)")

head("C1. The insertion points named by section 2, in the spec as it stands")
anchors = {
    'heading "The Founding Wager" (section 2 goes after it)': r"^#+ .*Founding Wager",
    'Floor sentence anchor "A self-model that can be lopped off while the computation runs was a description all along"':
        r"A self-model that can be lopped off while the computation runs was a description all along",
    'heading "What Would Count Against It"': r"^#+ What Would Count Against It",
}
for name, pat in anchors.items():
    hits = [i + 1 for i, l in enumerate(slines) if re.search(pat, l)]
    print(f"  {len(hits)} match(es) for {name}: lines {hits}")

head("C2. Is each addition given as text to insert, or only described?")
floor_idx = next(i for i, l in enumerate(after_block) if 'The sentence added to "The Floor"' in l)
para_idx = next(i for i, l in enumerate(after_block) if 'The paragraph added to "What Would Count Against It"' in l)
floor_quote = [l for l in after_block[floor_idx:para_idx] if l.startswith(">")]
para_quote = [l for l in after_block[para_idx:] if l.startswith(">")]
print(f"  Floor sentence: {len(floor_quote)} quoted line(s) of text to insert")
print(f"  'What Would Count Against It' paragraph: {len(para_quote)} quoted line(s) of text to insert")
print("  what stands under the paragraph's heading instead (first words of each sentence):")
body = " ".join(after_block[para_idx:]).replace("**", "")
for s in re.split(r"(?<=[.:])\s+", body)[:8]:
    print("    - " + s[:110])

head("C3. Proposal-internal references inside the text that would go into the spec")
block_text = "\n".join(spec_block)
for pat, label in ((r"RT-\d+", "red-team finding numbers"), (r"\bsection 10\b", "'section 10' (a proposal section)"),
                   (r"Decision 7", "'Decision 7' (a ruling item, no file named)"),
                   (r"chapter \d+", "book chapters")):
    hits = re.findall(pat, block_text)
    print(f"  {label}: {len(hits)} {sorted(set(hits)) if hits else ''}")

head("C4. The spec as it would read after insertion: competing statements")
# Build it: section 2's spec block placed after Scope (where the wager would go, since the
# wager's own heading does not exist), and the Floor sentence appended to the paragraph that
# holds its anchor. Then search the assembled text paragraph by paragraph, so that a phrase
# broken across two lines is still found.
scope_end = next(i for i, l in enumerate(slines) if l.startswith("## What This Proposal Is")) - 1
floor_sentence = " ".join(l.lstrip("> ").strip() for l in floor_quote)
spec_with_floor = list(slines)
anchor_i = next(i for i, l in enumerate(slines) if "was a description all along" in l)
spec_with_floor[anchor_i] = spec_with_floor[anchor_i] + " " + floor_sentence
assembled = spec_with_floor[:scope_end] + spec_block + ["", "---", ""] + spec_with_floor[scope_end:]
paras, cur, origin = [], [], []
block_set = set(spec_block)
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
print(f"  assembled spec: {len(assembled)} lines, {len(paras)} paragraphs")
checks = [
    ("what 'minimum viable' names", r"[Mm]inimum viable\" names|minimum viable conscious machine a two-part definition|[Mm]inimum viable mind is"),
    ("the removal test used as an instrument or pass-fail criterion", r"subject to a removal test|pass-fail criterion is the removal test|removal test as the intuition|settled by removal|survives the removal test"),
    ("the removal test called a definition, not an instrument", r"definition and not an instrument|definition, not an instrument"),
    ("whether the floor or the binding is measured", r"does not measure the floor|targets the \*\*minimum measurable|Interpretability is the route|measurement that speaks to an inside|floor is not measured"),
]
for label, pat in checks:
    print(f"  {label}:")
    for o, ptxt in zip(origin, paras):
        for m in re.finditer(pat, ptxt):
            if o == "spec" and floor_sentence[:40] in ptxt and m.start() > ptxt.find(floor_sentence[:40]) >= 0:
                o2 = "Floor sentence (added)"
            else:
                o2 = o if o == "section 2" else "spec, unchanged"
            s0 = max(0, m.start() - 50)
            print(f"    [{o2}] ...{ptxt[s0:m.end() + 90]}...")

head("C5. Ruling 10 against section 2's observer paragraph")
r10 = re.search(r"10\. \*\*The observer side.*?\*Ruled as recommended\.\*", rulings, re.S).group(0)
print("  ruling 10 (rulings file):", " ".join(r10.split())[:420])
for l in spec_block:
    if "option put to John" in l or "Decision 7" in l or "authorises" in l:
        print("  section 2:", l.strip())

head("C6. The indicators section 2 lists against the book's five and the spec's five")
book = BOOK.read_text()
print(f"  book summary SHA-256 now: {sha(book)}  matches the cited one: {sha(book) == BOOK_SHA_CITED}")
m = re.search(r"There are \*\*five indicators\*\*: (.*?)\. A model", book)
print("  book, chapter 6:", m.group(1))
m2 = re.search(r"five external indicators — (.*?) — without", spec)
print("  spec, What Would Count Against It:", m2.group(1))
m3 = re.search(r"the indicators of chapter 6: (.*?)\n\n", block_text, re.S)
print("  section 2:", " ".join(m3.group(1).split()))

head("C7. The battery draft (version 4, 3eee588) against section 2's operational terms")
for pat in (r"passes the battery|pass the battery|passing the battery", r"\bsmallest\b", r"parameter count",
            r"construction family|\bfamily\b", r"minimum viable", r"10-million and 30-million"):
    hits = [i + 1 for i, l in enumerate(battery.splitlines()) if re.search(pat, l, re.I)]
    print(f"  /{pat}/: {len(hits)} line(s) {hits[:8]}")
m = re.search(r"a discriminating reading can also live\s+in \*\*(.*?)\*\*", battery, re.S)
print("  battery section 0, the second clause:", " ".join(m.group(1).split()))
for l in spec_block:
    if "discriminates only where" in l or "two systems built alike" in l:
        print("  section 2:", l.strip())

head("C8. Experiment 1's record against section 2's description of it")
ci = json.loads(show(MAIN, EXP1_CI))
prim = ci["cells"]["idxres_mean_k16"]
for k in ("T_self_irrelevant", "T_self_relevant", "T_syntax"):
    c = prim[k]
    print(f"  primary condition, drop on {k:17}: {c['point']:.4f} [{c['lo']:.4f}, {c['hi']:.4f}]")
g = ci["derived"]["router_gap_idxres_mean_k16"]
print(f"  router gap (syntax drop minus self-relevant drop): {g['point']:+.4f} [{g['lo']:+.4f}, {g['hi']:+.4f}]")
f1 = show(MAIN, EXP1_FINDINGS)
m = re.search(r"\(4\) per-item view:(.*?)\.\n", f1, re.S)
print("  findings addendum, item (4):", " ".join(m.group(1).split()))
for l in spec_block:
    if "spread across every task" in l or "same spread" in l:
        print("  section 2:", l.strip())

head("C9. The founding wager text (which section 2 presupposes) against the later rulings")
for pat in (r"found a router", r"Stage 2|degree unmeasured|integration axis", r"removal-test"):
    hits = [(i + 1, l.strip()) for i, l in enumerate(wager.splitlines()) if re.search(pat, l)]
    print(f"  /{pat}/: {len(hits)}")
    for n, l in hits:
        print(f"    {n}: {l[:120]}")
m = re.search(r"2\. \*\*Experiment A is relabelled\*\*(.*?)\*Ruled", rulings, re.S)
print("  ruling, decision 2:", " ".join(m.group(1).split())[:260])

head("C10. Does any committed rehearsal cover the two-sided question?")
files = subprocess.run(["git", "ls-tree", "-r", "--name-only", MAIN], capture_output=True, text=True, check=True).stdout.split()
reh = [f for f in files if re.search(r"rehears", f, re.I)]
hit = [f for f in reh if re.search(r"two-sided|question|battery|observer|presence", f, re.I)]
print(f"  files with 'rehears' in the name at {MAIN}: {len(reh)}; of those naming the two-sided question, battery, observer or presence: {hit}")
fl = [i + 1 for i, l in enumerate(battery.splitlines()) if re.search(r"fluency", l, re.I)]
print(f"  'fluency' in the battery draft: {len(fl)} line(s) {fl}; a defined fluency measure: "
      f"{bool(re.search(r'fluency (measure|score|rating)s? (is|are|=)', battery, re.I))}")

head("C11. The book's own treatment of indispensable bookkeeping")
m = re.search(r"\*\*The removal test, examined\.\*\*(.*?)\n", book)
print("  book summary, appendix A:", m.group(1).strip())

# ------------------------------------------------------------- failure-mode pass sweeps
head("FMP-1. Failure 1 (zero denominator): every ratio, rate or division in section 2")
pat1 = r"\bratio|\bdivid|denominator|per cent|percent|\brates?\b|\bshare\b|\bchance\b|fraction|\bsmallest\b|\bdegree\b"
for i, l in enumerate(sec2, s2_start + 1):
    if re.search(pat1, l, re.I):
        print(f"  {i}: {l.strip()[:130]}")

head("FMP-2. Failure 2 (unrecoverable target): route sentences in section 2, widened for behaviour")
pat2 = (r"route to the states|carried by the token|forced by the loss|is the input token|produced by|"
        r"what in the system|reaches the (model|system)|positive control|built to have|on purpose|"
        r"put there")
for i, l in enumerate(sec2, s2_start + 1):
    if re.search(pat2, l, re.I):
        print(f"  {i}: {l.strip()[:130]}")
print("  (end of hits)")
st = [i + 1 for i, l in enumerate(battery.splitlines()) if re.search(r"neither toy pipeline|built to carry state", l, re.I)]
print(f"  battery v4 lines saying no state-carrying construction exists yet, or naming the positive control: {st}")

head("FMP-3. Failure 3 (empty cell): the cells section 2's two sides need, and what is in them")
pat3 = r"known construction|built alike|anchors built|with and without|ground truth|none does yet|frontier models"
for i, l in enumerate(sec2, s2_start + 1):
    if re.search(pat3, l, re.I):
        print(f"  {i}: {l.strip()[:130]}")

head("FMP-4. Failure 4 (claim with no record): the list's two sweeps on section 2")
pat4 = (r"verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|"
        r"recorded|returns|returned|yield|result")
w = [(i, l) for i, l in enumerate(sec2, s2_start + 1) if re.search(pat4, l, re.I)]
print(f"  word sweep: {len(w)} line(s)")
for i, l in w:
    print(f"    {i}: {l.strip()[:120]}")
n = [(i, l) for i, l in enumerate(sec2, s2_start + 1) if re.search(r"[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}", l)]
print(f"  number sweep: {len(n)} line(s)")
for i, l in n:
    print(f"    {i}: {l.strip()[:120]}")
d = [(i, l) for i, l in enumerate(sec2, s2_start + 1) if re.search(r"\b20\d\d-\d\d-\d\d\b|\$\d", l)]
print(f"  dates and money: {len(d)} line(s)")
for i, l in d:
    print(f"    {i}: {l.strip()[:120]}")

head("FMP-5. Failure 5 (a command that creates something): commands, runs and spend in section 2")
pat5 = r"```|\$ |\.py\b|\.sh\b|launch|spend|\$\d|API|authoris|authoriz|runs?\b"
for i, l in enumerate(sec2, s2_start + 1):
    if re.search(pat5, l):
        print(f"  {i}: {l.strip()[:130]}")
print("  (end of hits)")

head("FMP-6. Failure 6 (remote step tested only on stand-ins): remote words in section 2")
pat6 = r"\bssh\b|nohup|\brent|vendor|\bmachine|\bpod\b|\bcloud\b|remote|GPU|\bserver\b"
h6 = [(i, l) for i, l in enumerate(sec2, s2_start + 1) if re.search(pat6, l, re.I)]
print(f"  {len(h6)} line(s)")
for i, l in h6:
    print(f"    {i}: {l.strip()[:130]}")

head("C12. 'Degree' in section 2 against the battery draft")
for i, l in enumerate(sec2, s2_start + 1):
    if re.search(r"\bdegree\b", l):
        print(f"  section 2, {i}: {l.strip()}")
bd = [(i + 1, l.strip()) for i, l in enumerate(battery.splitlines()) if re.search(r"\bdegree\b", l, re.I)]
print(f"  battery v4, lines with 'degree' as a word: {len(bd)}")
for n, l in bd:
    print(f"    {n}: {l[:110]}")

head("C13. The record section 2's Floor sentence cites, and whether it has been checked")
rc = "docs/outside-perspective/2026-10-07-router-control-check.md"
print(f"  {rc} exists at {MAIN}: {rc in files}")
txt = show(MAIN, rc)
print("  its own status line:", " ".join([l for l in txt.splitlines() if re.search(r'ARGUED|owed a check|Status', l)][:2])[:300])
chk = [f for f in files if re.search(r"router-control", f) and f != rc]
print(f"  other committed files naming the router-control check in their path: {chk}")
