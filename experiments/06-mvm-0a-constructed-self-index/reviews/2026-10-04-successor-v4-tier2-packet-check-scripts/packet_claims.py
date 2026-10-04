#!/usr/bin/env python3
"""Checks of the packet's own words against the packet files and the record.
Imports nothing from the builder.

    python3 <this file> [commit]
"""
import re
import subprocess
import sys

COMMIT = sys.argv[1] if len(sys.argv) > 1 else "6279573"
PK = "experiments/06-mvm-0a-constructed-self-index/reviews/packets/"
STAMP = "2026-10-04-successor-v4-tier2"


def show(p):
    return subprocess.run(["git", "show", "{}:{}".format(COMMIT, p)], capture_output=True,
                          check=True).stdout.decode()


def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True, check=True).stdout


names = sorted(p for p in git("ls-tree", "--name-only", COMMIT, PK).split()
               if p.split("/")[-1].startswith(STAMP))
gem = show([p for p in names if p.endswith("-gemini.md")][0])
chats = [p for p in names if "-chatgpt-" in p]
ctext = {p: show(p) for p in chats}
idx = show([p for p in names if "INDEX" in p][0])
v4 = show("docs/successor-experiment-proposal-2026-10-03-v4.md")

# 1. the orientation is the same in both deliveries
g_head = gem.split("\n===== RECORD 1 of")[0]
c_head = ctext[chats[0]].split("\n===== RECORD 1 of")[0]
g_core = g_head.split("\n*This is the whole packet")[0]
c_core = c_head.split("\n*This packet arrives")[0]
print("1. orientation and record list identical in Gemini doc and ChatGPT file 1:", g_core == c_core)
print("   Gemini delivery note:", g_head[len(g_core):].strip().replace("\n", " "))

# 2. the closing instruction
last = ctext[chats[-1]]
print("2. last ChatGPT file opens with the answer-now instruction:",
      last.startswith("*This is file 33 of 33, the last one") and "Answer the brief" in last.split("\n")[0])
print("   Gemini document ends with:", repr(gem.rstrip().split("\n")[-1]))
mids = [ctext[p].split("\n")[0] for p in chats[1:-1]]
print("   files 2..32 each open with 'reply with one short line ... wait':",
      all("Reply with one short line" in m and "wait for the rest" in m for m in mids))

# 3. labels G... and A...
def labels(t):
    return sorted(set(re.findall(r"\b([GA])1, \1?2", t)))
outside_g = gem.split("\n===== RECORD 1 of")[0] + gem.split("===== END OF RECORD 25 =====")[1]
print("3. finding labels asked for, Gemini (outside the records):", re.findall(r"G1, G2, G3", outside_g).__len__(),
      "x 'G1, G2, G3'; any 'A1, A2' outside records:", "A1, A2" in outside_g)
outside_c = "".join(re.split(r"^===== RECORD", t, maxsplit=1, flags=re.M)[0]
                    for t in ctext.values())
print("   ChatGPT headers: 'A1, A2, A3' x", outside_c.count("A1, A2, A3"),
      "| 'G1' anywhere in headers:", "G1" in outside_c)
print("   index: G1 mentions", idx.count("G1"), "| A1 mentions", idx.count("A1"))

# 4. the instruction sheet's table: size and contents of every file
rows = re.findall(r"^\| ChatGPT (\d+) of 33 \| `([^`]+)` \| ([\d.]+) KB \| (.*) \|$", idx, re.M)
bad = []
for n, fname, kb, what in rows:
    p = PK + fname
    if p not in ctext:
        bad.append((n, "file not found")); continue
    size = len(ctext[p].encode())
    if "{:.1f}".format(size / 1000) != kb:
        bad.append((n, "size", kb, size))
    recs = sorted(set(int(x) for x in re.findall(r"^===== RECORD (\d+) of", ctext[p], re.M)))
    said = [int(x) for x in re.findall(r"(?:^|; )(\d+)\. ", what)]
    if recs != said:
        bad.append((n, "records", said, recs))
print("4. index rows:", len(rows), "| rows whose size or record list is wrong:", bad or "none")
gkb = re.search(r"Gemini session \| `[^`]+` \| ([\d,]+) KB", idx).group(1)
print("   Gemini size in index: {} KB; actual {:,} bytes".format(gkb, len(gem.encode())))
print("   index says files in filename order are 01..33; sorted names give numbers:",
      [int(re.search(r"chatgpt-(\d+)-of", p).group(1)) for p in chats] == list(range(1, 34)))

# 5. the orientation's factual statements
print("5. '$108' in version 4:", "$108" in v4, "| '108' anywhere in v4 money sections:",
      bool(re.search(r"\$\s?108\b", v4)))
for m in re.finditer(r"The successor, all in\*\* \| \*\*(.*?)\*\*", v4):
    print("   version 4's own total for the successor:", m.group(1))
print("   version 4 length in characters:", f"{len(v4):,}", "(orientation: 'about 290,000')")
print("   v4 opening quote present:", "cannot go to the registration review yet" in v4)
for n, word in [(14, "check of version 4"), (15, "competing-solver"), (21, "competing solver")]:
    line = re.search(r"^{}\. (.*)$".format(n), g_core, re.M).group(1)
    print("   record {}: {}".format(n, line[:150]))
print("   ruling that opened the review is in the packet:",
      "2026-10-04-registration-review-opened" in gem)

# 6. commits named in "What was built from what"
for path, said in [("docs/successor-experiment-proposal-2026-10-03-v4.md", "41b0bd3"),
                   (PK.replace("packets/", "") + "2026-10-04-successor-v4-gate-a-claude-code.md", "135c1f7")]:
    named = said in idx
    same = git("diff", "--stat", said, COMMIT, "--", path).strip() == ""
    last = git("log", "-1", "--format=%h", COMMIT, "--", path).strip()
    print("6. {}: index names {} ({}); content at {} same as at {}: {}; last commit touching it: {}".format(
        path.split("/")[-1], said, named, said, COMMIT, same, last))
