#!/usr/bin/env python3
"""Check 2. Every sentence in the new text that says registered, pre-registered,
pre-stated, verified, measured or calibrated, with whether it (or, failing that,
its paragraph) cites a committed file by name. New text = the paragraphs of the
paper draft that pull request 175 adds or changes (any paragraph containing an
added line), the whole refreshed explainer, and the approach note. A citation is
a backticked name ending .md/.json/.py or a backticked path; a paragraph-level
citation is marked PARA so the reader can judge whether it covers the sentence.
Also prints every sentence that names one of the five runs the record calls
unregistered, so it can be read for the word "registered" beside it."""
import re, subprocess, sys
WORDS = re.compile(r"\b(pre-registered|pre-registration|registered|registration|pre-stated|verified|verification|measured|calibrated|calibration)\b", re.I)
CITE = re.compile(r"`[^`]*(\.md|\.json|\.py|/)[^`]*`")
UNREG = {"positive control": re.compile(r"positive control", re.I),
         "fitted sweep": re.compile(r"fitted (linear|detector|position)|fitted read", re.I),
         "ceiling measurement": re.compile(r"ceiling (was )?(then )?measur|measured (ownership-blind )?ceiling|ceiling of 1\.0|ceiling-measurement|A measurement on 2026-09-17", re.I),
         "control-learnability pilot": re.compile(r"quadrupled|control-learnability", re.I),
         "C development runs": re.compile(r"development runs?", re.I)}
def paragraphs(text): return [p for p in re.split(r"\n\s*\n", text) if p.strip()]
def sentences(p):
    flat = re.sub(r"\s+", " ", p)
    return re.split(r"(?<=[.!?])\s+(?=[A-Z*(\"“])", flat)
paper = open("drafts/paper-removal-test-nature-draft.md", encoding="utf-8").read()
diff = subprocess.run(["git", "diff", "-U0", "origin/main...HEAD", "--", "drafts/paper-removal-test-nature-draft.md"], capture_output=True, text=True).stdout
added = {l[1:].strip() for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++") and l[1:].strip()}
paper_new = [p for p in paragraphs(paper) if any(l.strip() in added for l in p.splitlines() if l.strip())]
docs = {"paper (new paragraphs)": paper_new,
        "explainer.md": paragraphs(open("explainer.md", encoding="utf-8").read()),
        "approach note": paragraphs(open("docs/outside-reader-approach-note-2026-10-17.md", encoding="utf-8").read())}
n = {"SENT": 0, "PARA": 0, "NONE": 0}
mode = sys.argv[1] if len(sys.argv) > 1 else "words"
for name, paras in docs.items():
    for pi, p in enumerate(paras):
        pc = bool(CITE.search(p))
        for s in sentences(p):
            if mode == "words":
                m = WORDS.findall(s)
                if not m: continue
                tag = "SENT" if CITE.search(s) else ("PARA" if pc else "NONE")
                n[tag] += 1
                print(f"[{tag}] {name} ¶{pi+1} {sorted(set(w.lower() for w in m))}: {s[:230]}")
            else:
                for k, rx in UNREG.items():
                    if rx.search(s):
                        lab = "says unregistered" if re.search(r"unregistered|UNREGISTERED|not registered", s) else ("SAYS REGISTERED" if re.search(r"\bregistered\b", s, re.I) else "no label")
                        print(f"[{k} | {lab}] {name} ¶{pi+1}: {s[:260]}")
if mode == "words": print("\n", n)
