#!/usr/bin/env python3
"""Check 3. The three ruled sentences, quoted exactly. For each, count exact
occurrences (line wraps collapsed) in the ruling it comes from and in each new
text, and print every place a new text uses a fragment of it ("not references",
"not reached", "could not discriminate", "cheaper account", "accept the stop")
so a paraphrase or a near-miss shows up beside the exact quotes."""
import re, subprocess
def flat(path):
    try: t = open(path, encoding="utf-8").read()
    except FileNotFoundError: t = subprocess.run(["git", "show", "origin/main:" + path], capture_output=True, text=True).stdout
    return re.sub(r"\s+", " ", t.replace("**", ""))
RULED = [("the built arms as designed are not references; the measure was not reached", "docs/rulings/2026-10-08-december-result-restatement-rulings.md", ["not references", "not reached"]),
         ("the test could not discriminate routing from a centre; the cheaper account was taken in advance", "docs/rulings/2026-10-07-two-sided-question-rulings.md", ["could not discriminate", "cheaper account", "unable to discriminate"]),
         ("accept the stop", "docs/rulings/2026-10-12-experiment-c-stop-ruling.md", ["accept the stop", "accepted the stop"])]
TEXTS = ["explainer.md", "drafts/paper-removal-test-nature-draft.md", "docs/outside-reader-approach-note-2026-10-17.md"]
for s, src, frags in RULED:
    print(f"== {s!r}\n   in its ruling ({src}): {flat(src).count(s)} exact")
    for t in TEXTS:
        ft = flat(t)
        print(f"   {t}: {ft.count(s)} exact")
        for fr in frags:
            for m in re.finditer(re.escape(fr), ft):
                print(f"      '{fr}': …{ft[max(0, m.start()-90):m.end()+40]}…")
