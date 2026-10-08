#!/usr/bin/env python3
"""Independent check of the tier 2 packet for successor proposal version 4.

Imports nothing from scripts/build_successor_v4_tier2_packets.py. Reads the
packet files and the sources from a git commit (default 6279573) with
`git show`, never from the working tree, so an uncommitted edit cannot help or
hurt. Records are rebuilt from the marker lines alone: the text of a record (or
of one part of it) is everything after the newline that ends its
`===== RECORD` line and before the start of its `===== END OF RECORD` line.
Parts are joined in part order. Each record is then compared with:
  - a whole file: the whole file at the commit;
  - whole sections: the protocol from the named "## " heading up to the next
    "## " heading, trailing blank lines dropped, one newline kept;
  - lines a to b: those lines of the file at the commit.

Run from the top of the repository:
    python3 <this file> [commit]
"""
import hashlib
import re
import subprocess
import sys

COMMIT = sys.argv[1] if len(sys.argv) > 1 else "6279573"
PK = "experiments/06-mvm-0a-constructed-self-index/reviews/packets/"
STAMP = "2026-10-04-successor-v4-tier2"
LIMIT = 28000


def show(path):
    return subprocess.run(["git", "show", "{}:{}".format(COMMIT, path)],
                          capture_output=True, check=True).stdout.decode("utf-8")


listing = subprocess.run(["git", "ls-tree", "--name-only", COMMIT, PK],
                         capture_output=True, text=True, check=True).stdout.split()
files = sorted(p for p in listing if p.split("/")[-1].startswith(STAMP))
gem_path = [p for p in files if p.endswith("-gemini.md")][0]
chat_paths = sorted(p for p in files if "-chatgpt-" in p)

problems = []

# --- numbering and size of the ChatGPT files
nums = []
for p in chat_paths:
    m = re.search(r"-chatgpt-(\d\d)-of-(\d\d)-", p)
    nums.append((int(m.group(1)), int(m.group(2))))
print("ChatGPT files:", len(chat_paths))
print("numbered 1..N with nothing missing:",
      [a for a, _ in nums] == list(range(1, len(chat_paths) + 1)),
      "| 'of' values:", sorted(set(b for _, b in nums)))
sizes = {p: len(show(p).encode("utf-8")) for p in chat_paths}
big = max(sizes, key=sizes.get)
print("largest ChatGPT file: {:,} bytes ({}); files over {:,} bytes: {}".format(
    sizes[big], big.split("/")[-1][:60], LIMIT, [p for p, s in sizes.items() if s > LIMIT]))

OPEN = re.compile(r"^===== RECORD (\d+) of (\d+)(?:, part (\d+) of (\d+))? - (.*) - "
                  r"`([^`]+)` \((.*)\) =====$", re.M)
CLOSE = re.compile(r"^===== END OF RECORD (\d+)(?:, part (\d+))? =====$", re.M)


def parse(text, name):
    recs, outside, pos = {}, [], 0
    while True:
        m = OPEN.search(text, pos)
        if not m:
            outside.append(text[pos:])
            break
        outside.append(text[pos:m.start()])
        n = int(m.group(1))
        c = CLOSE.search(text, m.end())
        if not c or int(c.group(1)) != n:
            problems.append("{}: record {} opened but the next close is {}".format(
                name, n, c and c.group(0)))
            break
        if OPEN.search(text, m.end(), c.start()):
            problems.append("{}: an opening marker inside record {}".format(name, n))
        body = text[m.end() + 1:c.start()]
        part = (int(m.group(3)), int(m.group(4))) if m.group(3) else None
        cpart = int(c.group(2)) if c.group(2) else None
        if (part[0] if part else None) != cpart:
            problems.append("{}: record {} part numbers disagree".format(name, n))
        r = recs.setdefault(n, dict(path=m.group(6), desc=m.group(7), title=m.group(5),
                                    parts=[]))
        if (r["path"], r["title"]) != (m.group(6), m.group(5)):
            problems.append("{}: record {} parts name different files".format(name, n))
        r["parts"].append((part, body))
        pos = c.end()
    return recs, outside


gem_text = show(gem_path)
chat_text = "".join(show(p) for p in chat_paths)
G, gout = parse(gem_text, "Gemini")
C, cout = parse(chat_text, "ChatGPT")


def joined(r):
    ks = [p for p, _ in r["parts"]]
    if ks != [None]:
        K = ks[0][1]
        if [k for k, _ in ks] != list(range(1, K + 1)) or any(x[1] != K for x in ks):
            problems.append("parts out of order or missing: {}".format(ks))
    return "".join(b for _, b in r["parts"])


def sections(text, heading):
    lines = text.split("\n")
    a = [i for i, l in enumerate(lines) if l == "## " + heading]
    assert len(a) == 1, heading
    b = next(i for i in range(a[0] + 1, len(lines)) if lines[i].startswith("## "))
    return "\n".join(lines[a[0]:b]).rstrip("\n") + "\n", lines[b]


print()
print("rec | how cut | source | parts G/C | equal to source G/C")
material = []
for n in range(1, 26):
    g, c = G.get(n), C.get(n)
    if not g or not c:
        problems.append("record {} missing (Gemini {}, ChatGPT {})".format(n, bool(g), bool(c)))
        continue
    path, desc = g["path"], g["desc"]
    src = show(path)
    if desc.startswith("complete file"):
        kind, want = "whole file", src
        claimed = int(re.search(r"([\d,]+) characters", desc).group(1).replace(",", ""))
        if claimed != len(src):
            problems.append("record {}: marker says {} characters, source has {}".format(
                n, claimed, len(src)))
    elif desc.startswith("whole sections"):
        h = re.search(r'heading "([^"]+)"', desc).group(1)
        want, nexth = sections(src, h)
        claimed = int(re.search(r"; ([\d,]+) of", desc).group(1).replace(",", ""))
        total = int(re.search(r"file's ([\d,]+) characters", desc).group(1).replace(",", ""))
        if claimed != len(want) or total != len(src):
            problems.append("record {}: marker counts {}/{} vs {}/{}".format(
                n, claimed, total, len(want), len(src)))
        kind = "section '{}...' up to '{}...'".format(h[:22], nexth[3:25])
    elif desc.startswith("lines"):
        a, b, tot = map(int, re.match(r"lines (\d+) to (\d+) of the file's (\d+)", desc).groups())
        L = src.splitlines(keepends=True)
        want = "".join(L[a - 1:b])
        kind = "lines {}-{} of {}".format(a, b, len(L))
        if tot != len(L):
            problems.append("record {}: marker says {} lines, file has {}".format(n, tot, len(L)))
    else:
        problems.append("record {}: unknown description {}".format(n, desc))
        continue
    if not want.endswith("\n"):
        problems.append("record {}: source text does not end in a newline".format(n))
    gj, cj = joined(g), joined(c)
    ok_g, ok_c = gj == want, cj == want
    if not (ok_g and ok_c):
        problems.append("record {} ({}) differs from source: Gemini {} ChatGPT {}".format(
            n, path, ok_g, ok_c))
    if g["path"] != c["path"] or g["desc"] != c["desc"]:
        problems.append("record {}: the two packets label it differently".format(n))
    material.append(want)
    print("{:>3} | {} | {} | {}/{} | {}/{}".format(n, kind, path, len(g["parts"]),
                                                   len(c["parts"]), ok_g, ok_c))

extra = sorted(set(G) - set(range(1, 26))) + sorted(set(C) - set(range(1, 26)))
if extra:
    problems.append("records outside 1..25: {}".format(extra))
m = "".join(material)
gm = "".join(joined(G[n]) for n in sorted(G))
cm = "".join(joined(C[n]) for n in sorted(C))
print()
print("material = the 25 records cut from source at this commit, joined in record order, utf-8")
print("characters: {:,} | bytes: {:,}".format(len(m), len(m.encode("utf-8"))))
print("sha256 from sources:        ", hashlib.sha256(m.encode()).hexdigest())
print("sha256 from Gemini doc:     ", hashlib.sha256(gm.encode()).hexdigest())
print("sha256 from ChatGPT files:  ", hashlib.sha256(cm.encode()).hexdigest())
idx = show(PK + STAMP + "-INDEX-how-to-run-these-sessions.md")
print("sha256 in instruction sheet:", re.search(r"^    ([0-9a-f]{64})$", idx, re.M).group(1))

print()
print("Text outside every record, Gemini (first 100 characters of each chunk):")
for x in [x.strip() for x in gout if x.strip()]:
    print("   ", x[:100].replace("\n", " "))
cn = [x.strip() for x in cout if x.strip()]
print("Text outside every record, ChatGPT: {} chunks (expected 33: file 1's"
      " orientation and 32 file headers)".format(len(cn)))
print()
print("PROBLEMS:" if problems else "No problems found.")
for p in problems:
    print("  -", p)
