#!/usr/bin/env python3
"""Checks 1 to 3 of the check of pull request 190. Each ruled change against the
wording John was shown: the ruling file's option (b) for the title, and the
proposals in the paper's own dated note of 2026-10-17 (which this pull request
keeps unchanged) for the router paragraph and the two Discussion changes. Line
wraps and markdown bold/italic marks are collapsed on both sides; nothing else.
Where the applied text differs from a proposal, the difference is printed word
by word (difflib) so it can be judged."""
import re, subprocess, difflib
P = "drafts/paper-removal-test-nature-draft.md"
R = "docs/rulings/2026-10-18-paper-reserved-places-ruling.md"
def flat(t): return re.sub(r"\s+", " ", t.replace("**", "").replace("*", "")).strip()
new = open(P, encoding="utf-8").read(); old = subprocess.run(["git", "show", "origin/main:" + P], capture_output=True, text=True).stdout
fn, fo, fr = flat(new), flat(old), flat(open(R, encoding="utf-8").read())
note = fn[fn.find("Dated note, 2026-10-17"):fn.find("Authors:")]
body = fn[fn.find("Authors:"):]  # the applied text: everything after the dated notes, so a proposal is never compared with itself
def between(t, a, b): i = t.find(a); j = t.find(b, i + len(a)); return t[i + len(a):j] if i >= 0 and j >= 0 else None
def wdiff(a, b):
    out = [("-" if op in "rd" else "") + " ".join(a.split()[i1:i2]) + ("  +" + " ".join(b.split()[j1:j2]) if op in "ri" else "")
           for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a.split(), b.split()).get_opcodes() if op != "equal"]
    return out or ["identical"]
# 1 title
title = new.splitlines()[0].lstrip("# ").strip()
opt_b = between(fr, '(b) "', '"; (c)')
print("1. title == ruling option (b):", title == opt_b, "| == note's proposal:", ('Proposed: "' + title + '"') in note)
print("   title :", title); print("   opt b :", opt_b)
# 2 router paragraph
prop = between(note, 'two "First"/"Second" clauses: "', '" The bootstrap-widening clause')
start = body.find("The damage pattern is consistent with the router reading")
applied = body[start:body.find("tell from nothing.", start) + len("tell from nothing.")]
boot_new = re.search(r" \(and the reason the coarser category-level bootstrap widens the d\(T_si\) interval to \[0\.000, 0\.594\]; Methods §Statistics\)", applied)
boot_old = "(and the reason the coarser category-level bootstrap widens the d(T_si) interval to [0.000, 0.594]; Methods §Statistics)" in fo
without = applied.replace(boot_new.group(0), "") if boot_new else applied
print("2. router passage minus the kept bootstrap clause == note's proposal:", without == prop)
print("   applied passage:", applied)
print("   bootstrap clause present on branch:", bool(boot_new), "| same clause on main:", boot_old)
print("   word diff proposal -> applied:", wdiff(prop or "", without))
print("   old first sentence gone:", "independently supports the router reading twice over. First" not in fn)
# 3 Discussion first paragraph
p1 = between(note, 'Proposed for the first: "', '" Proposed addition')
s1 = body[body.find("in an aligned 8B transformer, the most locatable"):]
s1 = s1[:s1.find("aim at it.") + len("aim at it.")]
print("3a. Discussion ¶1 == proposal (proposal's nested 'self' read as \"self\"):", s1 == p1.replace("'self'", '"self"'))
print("   word diff:", wdiff(p1.replace("'self'", '"self"'), s1))
# 3b Discussion third paragraph
p3 = between(note, 'after "before any data existed": "', '" The Discussion')
s3 = body[body.find("before any data existed") + len("before any data existed"):]
s3 = s3[:s3.find("other.") + len("other.")]
print("3b. Discussion addition == proposal (after a joining comma):", s3 == ", " + p3)
print("   applied:", s3); print("   word diff:", wdiff(p3, s3.lstrip(", ")))
# 3c Limitations
lim = body[body.find("The constructed line's instruments for locating"):]
lim = lim[:lim.find('"absent".') + len('"absent".')]
pl = between(note, "a sentence in \"Limitations\" saying that ", ", which the new results section states")
print("3c. Limitations sentence:", lim)
print("    note's proposal: saying that", pl)
print("    ruling item 3 option (b):", between(fr, "with an optional sentence in Limitations that ", ". Recommended"))
bf = flat(open("experiments/06-mvm-0a-constructed-self-index/blind-arm-findings.md", encoding="utf-8").read())
for k in ["the localization stack is unvalidated at 30", "John's ruling", "2026-09-16"]:
    print(f"    cited file blind-arm-findings.md contains {k!r}: {k in bf}")
i = bf.find("the localization stack is unvalidated at"); print("    there:", bf[i-60:i+160])
print("    'not testable' in blind-arm-findings.md:", bf.lower().count("not testable"), "| 'instrument failure to locate':", bf.count("instrument failure to locate"))
