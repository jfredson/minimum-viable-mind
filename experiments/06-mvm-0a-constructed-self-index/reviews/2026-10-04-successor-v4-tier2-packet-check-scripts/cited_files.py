#!/usr/bin/env python3
"""Independent check of the packet's list "Files version 4 cites that are not in
this packet". Imports nothing from the builder.

Derives the list from version 4 itself, more widely than the builder does: every
token in backticks that looks like a file path, with any extension, plus every
path-like token outside backticks that contains a slash and an extension. Each
is resolved against the files tracked at the commit: an exact path, else a
unique tracked path ending in "/<token>", else the token is called unresolved
(with the number of tracked files it could mean). Then compared with the list
printed in the packet's file 1 and with the 25 records' paths.

    python3 <this file> [commit]
"""
import re
import subprocess
import sys

COMMIT = sys.argv[1] if len(sys.argv) > 1 else "6279573"
TARGET = "docs/successor-experiment-proposal-2026-10-03-v4.md"
PK = "experiments/06-mvm-0a-constructed-self-index/reviews/packets/"
FILE1 = PK + "2026-10-04-successor-v4-tier2-chatgpt-01-of-33-start-here-and-records-1-to-3.md"


def show(p):
    return subprocess.run(["git", "show", "{}:{}".format(COMMIT, p)], capture_output=True,
                          check=True).stdout.decode()


tracked = subprocess.run(["git", "ls-tree", "-r", "--name-only", COMMIT], capture_output=True,
                         text=True, check=True).stdout.split()
tset = set(tracked)
v4 = show(TARGET)
f1 = show(FILE1)

head, tail = f1.split("**Files version 4 cites that are not in this packet**", 1)
listed = re.findall(r"^- `([^`]+)`$", tail.split("*This packet arrives")[0], re.M)
records = re.findall(r"^\d+\. .* - `([^`]+)` \(", head, re.M)
included = set(records)
print("records in the packet's list:", len(records), "| distinct files:", len(included))
print("files in the 'not in this packet' list:", len(listed))

EXT = r"\.(?:md|py|toml|json|jsonl|csv|txt|sh|yaml|yml|pt|npz|npy|log|out|lock|cfg|ini|html|js|ts)"
tokens = set(re.findall(r"`([A-Za-z0-9_.~/\-]+" + EXT + r")`", v4))
tokens |= set(re.findall(r"(?<![`A-Za-z0-9_./-])((?:[A-Za-z0-9_.~\-]+/)+[A-Za-z0-9_.\-]+" + EXT + r")\b", v4))


def resolve(tok):
    t = tok
    for pre in ("~/Documents/Code/minimum-viable-mind/", "~/Code/minimum-viable-mind/", "./"):
        if t.startswith(pre):
            t = t[len(pre):]
    if t in tset:
        return t, 1
    hits = [x for x in tracked if x.endswith("/" + t)]
    return (hits[0], 1) if len(hits) == 1 else (None, len(hits))


resolved, unresolved = {}, {}
for tok in sorted(tokens):
    p, k = resolve(tok)
    if p:
        resolved.setdefault(p, set()).add(tok)
    else:
        unresolved[tok] = k

print("distinct path-like names in version 4:", len(tokens))
print("  resolve to one tracked file:", len(resolved), "distinct files")
print("  do not resolve to one tracked file:", len(unresolved))

print()
print("(a) listed as not in the packet, but not a tracked file path at this commit:")
for x in listed:
    if x not in tset:
        print("    {}  (tracked files ending in /{}: {})".format(
            x, x, sum(1 for t in tracked if t.endswith("/" + x))))
print("(b) listed as not in the packet, but carried as a record:",
      [x for x in listed if x in included] or "none")
missing = sorted(p for p in resolved if p not in included and p not in listed)
print("(c) cited by version 4, a tracked file, neither carried nor listed ({}):".format(len(missing)))
for p in missing:
    print("    {}   <- cited as {}".format(p, sorted(resolved[p])))
print("(d) names in version 4 that resolve to no single tracked file ({}):".format(len(unresolved)))
for tok, k in sorted(unresolved.items()):
    print("    {}   ({} tracked files end with it){}".format(
        tok, k, "  [listed in packet]" if tok in listed else ""))
partial = [r for r in included if r.endswith(".py")]
print("(e) records carried only in part:", partial)
