"""Apply the proposed text changes that add or remove the word "batteries"
(RT-237 changes 1 and 3; RT-239's replacement of section 4.1's first
paragraph) to version 4 as committed, then search the result, sections 0 to
16, for "batter", as the closure check under RT-237 item 1 says to.

Replacement text is lifted from the PROPOSAL's quoted blocks by line range
(read from the file, not retyped), with the "> " quote markers removed.
Run from the repository root."""
import re, subprocess
V4 = "docs/successor-experiment-proposal-2026-10-03-v4.md"
P = "docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md"
v4 = open(V4).read()
prop = open(P).read().split("\n")


def quoted_block_after(marker):
    i = next(n for n, l in enumerate(prop) if marker in l)
    while not prop[i].startswith(">"):
        i += 1
    out = []
    while i < len(prop) and (prop[i].startswith(">")):
        out.append(prop[i][2:] if prop[i].startswith("> ") else prop[i][1:])
        i += 1
    return "\n".join(out)

# RT-237 change 1: section 8.2 bullet. The PROPOSAL quotes old, then new.
old1 = "- the ownership-free state and syntax batteries **must hold**."
i = next(n for n, l in enumerate(prop) if l.startswith("**Text change 1, section 8.2"))
blocks, cur, n = [], [], i
while len(blocks) < 2:
    l = prop[n]
    if l.startswith(">"):
        cur.append(l[2:] if l.startswith("> ") else l[1:])
    elif cur:
        blocks.append("\n".join(cur)); cur = []
    n += 1
assert blocks[0] == old1, blocks[0]
assert v4.count(old1) == 1
v5 = v4.replace(old1, blocks[1])

# RT-237 change 3: section 9 row
old3 = "the ownership-free batteries must hold"
assert v5.count(old3) == 1
v5 = v5.replace(old3, "with the channel zeroed, the own-directed answer is one of the four "
                      "candidate values on **1,546 or more of 3,000** gate episodes, on two seeds of three")

# RT-239: section 4.1 first paragraph
start = v5.index("The grammar extends the registered Amendment A3 grammar")
end = v5.index("shrunken version of it is `experiments/rehearsal-successor-measure/src/grammar.py`.")
end += len("shrunken version of it is `experiments/rehearsal-successor-measure/src/grammar.py`.")
v5 = v5[:start] + quoted_block_after("**Text change, section 4.1, its first paragraph") + v5[end:]

lines = v5.split("\n")
s0 = next(n for n, l in enumerate(lines) if l.startswith("## 0."))
s17 = next(n for n, l in enumerate(lines) if l.startswith("## 17."))
hits = [(n + 1, l) for n, l in enumerate(lines[s0:s17], start=s0) if re.search("batter", l, re.I)]
print(f"proposed text: sections 0 to 16 are lines {s0 + 1} to {s17}; hits for 'batter': {len(hits)}")
for n, l in hits:
    print(f"  {n}: {l.strip()}")
