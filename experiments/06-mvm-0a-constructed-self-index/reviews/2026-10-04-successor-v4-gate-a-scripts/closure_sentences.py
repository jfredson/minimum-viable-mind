"""Gate A tier 1, the closure rule's sentence check: every paragraph of
version 4 (at d19f914, sections 0 to 16, before the author's own pass) that
uses verified / measured / calibrated / attacked, and whether that paragraph
names a committed record (a file path, a commit, or a ledger item). Paragraphs
that name none are printed in full for reading. Reads the text only.
"""
import re
import subprocess

text = subprocess.run(["git", "show", "d19f914:docs/successor-experiment-proposal-2026-10-03-v4.md"],
                      capture_output=True, text=True, check=True).stdout.splitlines()
cut = next(i for i, l in enumerate(text) if l.startswith("## 17. "))
WORDS = re.compile(r"verif|measur|calibrat|attack", re.I)
CITE = re.compile(r"`[^`]*(\.md|\.json|\.py|\.txt|\.sh|/)[^`]*`|`[0-9a-f]{7}`|RT-\d+|section \d|page \d|ruling \d|item \d", re.I)
paras, start = [], 0
for i in range(cut + 1):
    if i == cut or not text[i].strip():
        if i > start:
            paras.append((start + 1, i, " ".join(t.strip() for t in text[start:i])))
        start = i + 1
hits = [(a, b, p) for a, b, p in paras if WORDS.search(p)]
bare = [(a, b, p) for a, b, p in hits if not CITE.search(p)]
print(f"paragraphs in sections 0 to 16: {len(paras)}; using one of the four words: {len(hits)}; "
      f"of those, naming no file, commit, ledger item, section, page, ruling or item: {len(bare)}")
for a, b, p in bare:
    print(f"\n--- lines {a} to {b}\n{p}")
