#!/usr/bin/env python3
"""Re-check of the fixes to the tier 2 packet (old 6279573, new 26159e5 by
default). Imports nothing from the builder; reads everything with `git show`.

    python3 <this file> [old] [new]
"""
import re
import subprocess
import sys

OLD = sys.argv[1] if len(sys.argv) > 1 else "6279573"
NEW = sys.argv[2] if len(sys.argv) > 2 else "26159e5"
PK = "experiments/06-mvm-0a-constructed-self-index/reviews/packets/"
STAMP = "2026-10-04-successor-v4-tier2"


def show(c, p):
    return subprocess.run(["git", "show", "{}:{}".format(c, p)], capture_output=True,
                          check=True).stdout.decode()


def names(c):
    out = subprocess.run(["git", "ls-tree", "--name-only", c, PK], capture_output=True,
                         text=True, check=True).stdout.split()
    return sorted(p for p in out if p.split("/")[-1].startswith(STAMP))


old, new = names(OLD), names(NEW)
print("same set of packet file names:", old == new, "|", len(new), "files")

# (d) which files changed, and whether the part from the first record marker to
# the last end marker is byte-identical
first = re.compile(r"^===== RECORD ", re.M)
last = re.compile(r"^===== END OF RECORD \d+(?:, part \d+)? =====$", re.M)
for p in new:
    a, b = show(OLD, p), show(NEW, p)
    if a == b:
        continue
    def mid(t):
        m = first.search(t)
        if not m:
            return None
        e = list(last.finditer(t))[-1]
        return t[m.start():e.end()]
    print("changed: {:<70} records region identical: {}".format(
        p.split("/")[-1][:70], mid(a) == mid(b) if mid(a) is not None else "(no records)"))

# (b) the repeated brief equals the protocol section, character for character
proto = show(NEW, "docs/outside-review-protocol.md").split("\n")
i = proto.index("## The brief, fixed, sent unchanged with every packet")
j = next(k for k in range(i + 1, len(proto)) if proto[k].startswith("## "))
brief = "\n".join(proto[i:j]).rstrip("\n") + "\n"
gem = show(NEW, [p for p in new if p.endswith("-gemini.md")][0])
f33 = show(NEW, [p for p in new if "-chatgpt-33-" in p][0])
f01 = show(NEW, [p for p in new if "-chatgpt-01-" in p][0])
for name, t in (("Gemini", gem), ("ChatGPT file 33", f33)):
    tail = t.split("===== END OF RECORD 25 =====\n", 1)[1]
    k = tail.find("## The brief")
    print("{}: text after the last record ends with the brief exactly: {} | "
          "brief starts {} characters into the tail | anything after the brief: {!r}".format(
              name, tail[k:] == brief, k, tail[k + len(brief):]))
    print("   lead-in line:", tail[:k].strip())

# (c) sizes
for p in new:
    if "-chatgpt-" in p:
        n = len(show(NEW, p).encode())
        if n > 28000:
            print("OVER LIMIT:", p, n)
print("largest ChatGPT file (bytes):", max(len(show(NEW, p).encode()) for p in new if "-chatgpt-" in p))
print("file 1 first line still the title; file 33 first line still says 'Answer the brief':",
      f01.startswith("# Review packet"), "Answer the brief" in f33.split("\n")[0])

# (a) the orientation's new sentences
v4 = show(NEW, "docs/successor-experiment-proposal-2026-10-03-v4.md")
print()
print("spend sentence in orientation:", re.search(r"describes \(about[^)]*\)", f01.replace("\n", " ")).group(0))
print("version 4 section 12.4 total:", re.search(r"The successor, all in\*\* \| \*\*(.*?)\*\*", v4).group(1),
      "| '## 12.4' or '### 12.4' heading present:", bool(re.search(r"^#+ 12\.4 ", v4, re.M)))
print("'$108' left anywhere in the new packet files:",
      [p.split("/")[-1] for p in new if "$108" in show(NEW, p)])
print("opening ruling exists at", NEW, ":",
      "docs/rulings/2026-10-04-registration-review-opened.md" in subprocess.run(
          ["git", "ls-tree", "-r", "--name-only", NEW, "docs/rulings/"], capture_output=True,
          text=True).stdout.split())
listed = re.findall(r"^- `([^`]+)`$", f01, re.M)
tracked = set(subprocess.run(["git", "ls-tree", "-r", "--name-only", NEW], capture_output=True,
                             text=True).stdout.split())
print("'not in this packet' entries:", len(listed), "| heading says:",
      re.search(r"\((\d+) of them", f01).group(1), "| entries that are not tracked paths:",
      [x for x in listed if x not in tracked])
