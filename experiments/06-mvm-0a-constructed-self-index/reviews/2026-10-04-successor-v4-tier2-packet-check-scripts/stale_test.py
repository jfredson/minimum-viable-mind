#!/usr/bin/env python3
"""Does the builder's --verify catch a stale packet? Run inside a throwaway clone
of the branch (never in the real checkout): for each case, change one character
of one source file in the clone's working tree, run --verify, record its exit
status and the problem lines it prints, then restore the file byte for byte.

    cd <scratch clone> && python3 <this file>
"""
import subprocess

CASES = [
    # (what, path, line number (1-based), should the packet go stale?)
    ("a ruling carried whole (record 13), line 10",
     "docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md", 10, True),
    ("version 4 (record 4), line 2223",
     "docs/successor-experiment-proposal-2026-10-03-v4.md", 2223, True),
    ("the brief in the protocol (record 1), line 390",
     "docs/outside-review-protocol.md", 390, True),
    ("grammar.py inside the cut (record 25), line 40",
     "experiments/rehearsal-successor-measure/src/grammar.py", 40, True),
    ("grammar.py outside the cut, line 300",
     "experiments/rehearsal-successor-measure/src/grammar.py", 300, False),
    ("the protocol outside the three carried sections, line 30",
     "docs/outside-review-protocol.md", 30, False),
]

for what, path, ln, expect in CASES:
    with open(path, "rb") as fh:
        orig = fh.read()
    lines = orig.decode("utf-8").split("\n")
    while not any(ch.isalpha() for ch in lines[ln - 1]):
        ln += 1  # the first line at or after the one named that has a letter in it
    s = lines[ln - 1]
    i = next(k for k, ch in enumerate(s) if ch.isalpha())
    new = s[:i] + ("X" if s[i] != "X" else "Y") + s[i + 1:]
    lines[ln - 1] = new
    with open(path, "wb") as fh:
        fh.write("\n".join(lines).encode("utf-8"))
    r = subprocess.run(["python3", "scripts/build_successor_v4_tier2_packets.py", "--verify"],
                       capture_output=True, text=True)
    with open(path, "wb") as fh:
        fh.write(orig)
    probs = [l.strip() for l in r.stdout.splitlines() if l.startswith("  - ")]
    went_stale = r.returncode != 0
    print("{}: changed {!r} -> {!r}".format(what, s[i], new[i]))
    print("   exit status {}; expected to fail: {}; {}".format(
        r.returncode, expect, "AS EXPECTED" if went_stale == expect else "NOT AS EXPECTED"))
    for p in probs[:6]:
        print("     " + p)
    if len(probs) > 6:
        print("     ... and {} more".format(len(probs) - 6))

clean = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
print("clone working tree clean after the test:", clean.strip() == "")
