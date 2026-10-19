#!/usr/bin/env python3
"""Check 5, the mechanical part of the independent Voice Calibration read.
Counts in the explainer and in the paper's two new results sections (from
"### The constructed line" to "## Discussion"): em dashes outside quotation
marks, the protocol's flagged words (section 7), contrastive "X, not Y" and
"not X but Y" forms, "rather than", and a list of specialist or internal terms
with the line of first use, so each first use can be read for a plain anchor."""
import re
FLAG = ["delve", "nuanced", "crucial", "pivotal", "vital", "navigate", "landscape", "realm", "ecosystem", "tapestry",
        "transformative", "comprehensive", "worth noting", "at its core", "in many ways", "more than ever", "the fact that",
        "indeed", "certainly", "undoubtedly", "stands as", "a testament to", "is real", "obviously", "of course", "clearly", "surely"]
TERMS = ["parameters", "transformer", "seed", "battery", "standard deviation", "permutation", "residual", "subspace",
         "checkpoint", "causal patching", "ablat", "lesion", "Amendment A3", "MVM-0a", "S4b", "step 4b", "release",
         "free-arm", "December-result", "Q5", "route use", "sharpness", "hand-set", "in-use check", "fit floor",
         "θ", "δ", "T_act", "T_other", "T_state", "T_syntax", "L0", "L1", "K0", "K5", "RTX 5090", "Gemini", "ChatGPT",
         "Sentient Horizons", "John", "two-sided question", "cheaper route", "floor"]
def strip_quotes(t): return re.sub(r'"[^"\n]*"', '""', t)
expl = open("explainer.md", encoding="utf-8").read()
paper = open("drafts/paper-removal-test-nature-draft.md", encoding="utf-8").read()
new = paper[paper.find("### The constructed line"):paper.find("## Discussion")]
for name, t in (("explainer.md", expl), ("paper, two new results sections", new)):
    words = len(t.split()); nq = strip_quotes(t)
    print(f"== {name} ({words} words)")
    print(f"   em dashes outside quotes: {nq.count('—')}; inside quotes: {t.count('—') - nq.count('—')}")
    hits = {w: len(re.findall(r"\b" + re.escape(w) + r"\b", t, re.I)) for w in FLAG}
    print("   flagged words:", {k: v for k, v in hits.items() if v} or "none")
    cp = re.findall(r"[^.;:]{0,60}, not [^.;:,]{0,50}", nq)
    nb = re.findall(r"not [^.;]{0,60}\bbut\b[^.;]{0,40}", nq)
    print(f"   ', not ...' outside quotes: {len(cp)}; 'not ... but': {len(nb)}; 'rather than': {len(re.findall(r'rather than', t))}")
    for c in cp: print("      , not:", c.strip()[:120])
    lines = t.splitlines()
    for term in TERMS:
        for i, l in enumerate(lines, 1):
            if term.lower() in l.lower():
                k = l.lower().index(term.lower())
                print(f"   first use of {term!r:<22} line {i}: …{l[max(0,k-60):k+70]}…"); break
