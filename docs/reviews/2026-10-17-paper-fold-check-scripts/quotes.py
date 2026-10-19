#!/usr/bin/env python3
"""Every double-quoted passage of four words or more in the new text (the whole
explainer; the paper's new paragraphs, as in status_words.py), searched for
verbatim in every committed .md and .json file of the repository except the
three files under check and the pass records. Line wraps and ** are collapsed on
both sides; nothing else is normalised, so a changed comma or dash shows as NOT
FOUND, which is the point."""
import re, subprocess, glob
def flat(s): return re.sub(r"\s+", " ", s.replace("**", "").replace("*", "")).strip()
skip = {"explainer.md", "drafts/paper-removal-test-nature-draft.md", "docs/outside-reader-approach-note-2026-10-17.md",
        "drafts/2026-10-17-voice-calibration-pass-explainer-and-paper-v0.3.md", "drafts/2026-10-17-cold-reader-report-explainer-and-paper-v0.3.md"}
files = [f for f in subprocess.run(["git", "ls-files", "*.md", "*.json"], capture_output=True, text=True).stdout.split() if f not in skip and "paper-fold-check" not in f]
corpus = {}
for f in files:
    try: corpus[f] = flat(open(f, encoding="utf-8").read())
    except Exception: pass
corpus["origin/main:docs/rulings/2026-10-17-experiment-c-stays-stopped-ruling.md"] = flat(subprocess.run(["git", "show", "origin/main:docs/rulings/2026-10-17-experiment-c-stays-stopped-ruling.md"], capture_output=True, text=True).stdout)
corpus["origin/main:" + "drafts/paper-removal-test-nature-draft.md (v0.2)"] = flat(subprocess.run(["git", "show", "origin/main:drafts/paper-removal-test-nature-draft.md"], capture_output=True, text=True).stdout)
paper = open("drafts/paper-removal-test-nature-draft.md", encoding="utf-8").read()
diff = subprocess.run(["git", "diff", "-U0", "origin/main...HEAD", "--", "drafts/paper-removal-test-nature-draft.md"], capture_output=True, text=True).stdout
added = {l[1:].strip() for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++") and len(l[1:].strip()) > 25}
paper_new = "\n\n".join(p for p in re.split(r"\n\s*\n", paper) if any(l.strip() in added for l in p.splitlines()))
for name, text in (("explainer.md", open("explainer.md", encoding="utf-8").read()), ("paper new paragraphs", paper_new)):
    # a quotation opens after a space or "(" and closes before a space or punctuation
    for q in sorted(set(re.findall(r'(?:(?<=\s)|(?<=\())"([^"]{12,}?)"(?=[\s.,;:)\]]|$)', flat(text)))):
        if len(q.split()) < 4: continue
        core = q.rstrip(".,;")
        where = [f for f, t in corpus.items() if core in t]
        print(f"{'FOUND    ' if where else 'NOT FOUND'} [{name}] \"{q[:110]}\"" + (f"  in {where[0]}" + (f" (+{len(where)-1})" if len(where) > 1 else "") if where else ""))
