#!/usr/bin/env python3
"""Check 4. The three places John reserved on 2026-10-09, compared byte for byte
between the main line (origin/main, version 0.2 as relabelled) and this branch:
(1) the title line; (2) the Discussion, every paragraph from "## Discussion" up
to the next "## " heading, paragraph by paragraph; (3) the paragraph that begins
"The damage pattern independently supports the router reading twice over".
Then (4) the v0.2 "constructive turn" paragraph on the main line against the
copy the dated note quotes (markdown bold and line wraps collapsed on both
sides, which is the only normalisation), and (5) the header's statement that the
v0.2 text has not passed the protocols. Prints SAME or DIFFERENT for each."""
import re, subprocess, hashlib
P = "drafts/paper-removal-test-nature-draft.md"
main = subprocess.run(["git", "show", "origin/main:" + P], capture_output=True, text=True, check=True).stdout
head = open(P, encoding="utf-8").read()
def paras(t): return [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]
def section(t, name):
    m = re.search(r"^## " + re.escape(name) + r"\n(.*?)(?=^## )", t, re.S | re.M); return m.group(1) if m else ""
def h(s): return hashlib.md5(s.encode()).hexdigest()[:10]
def flat(s): return re.sub(r"\s+", " ", s.replace("**", "")).strip()
print("(1) title:", "SAME" if main.splitlines()[0] == head.splitlines()[0] else "DIFFERENT")
print("    ", head.splitlines()[0])
dm, dh = paras(section(main, "Discussion")), paras(section(head, "Discussion"))
print(f"(2) Discussion: {len(dm)} paragraphs on main, {len(dh)} on branch")
for i, (a, b) in enumerate(zip(dm, dh), 1):
    print(f"    ¶{i} {'SAME     ' if a == b else 'DIFFERENT'} main {h(a)} branch {h(b)}  {flat(b)[:70]}")
for needle in ["is conversational infrastructure", "was voided by a control committed before any data existed"]:
    pm = [p for p in dm if needle in flat(p)]; ph = [p for p in dh if needle in flat(p)]
    print(f"    paragraph with '{needle}':", "SAME" if pm and pm == ph else "DIFFERENT or missing")
key = "The damage pattern independently supports the router reading twice over"
# the passage sits inside a longer paragraph: compare from the key sentence to "Methods §Statistics)."
def passage(t):
    i = t.find(key); j = t.find("Methods §Statistics).", i)
    return t[i:j + len("Methods §Statistics).")] if i >= 0 and j >= 0 else ""
rm, rh = passage(main), passage(head)
print("(3) 'router reading twice over' passage (key sentence to 'Methods §Statistics).'):", "SAME" if rm and rm == rh else "DIFFERENT or missing", f"main {h(rm)} branch {h(rh)}, {len(rm)} chars")
old = [p for p in dm if p.startswith("**The constructive turn.**")]
note = flat(head)
old_flat = flat(old[0]) if old else ""
first, _, rest = old_flat.partition(" A parallel behavioral program")
note_region = flat(head[head.find("*Dated note, 2026-10-17"):head.find("**Authors:**")])
print("(4) v0.2 'constructive turn', up to the retained-independence sentence, quoted in the dated note:", "SAME (verbatim)" if first and first in note_region else "DIFFERENT")
print("    main-line text compared:", first[:80], "…", first[-60:])
print("    retained-independence sentence on main kept in the new paragraph:", "SAME" if ("A parallel behavioral program" + rest) in flat(section(head, "Discussion")) else "DIFFERENT")
hdr = flat(head[:3000])
print("(5) header says the v0.2 text has NOT passed:", "YES" if "the v0.2 text has NOT" in hdr else "NO")
