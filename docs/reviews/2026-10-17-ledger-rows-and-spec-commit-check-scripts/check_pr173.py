#!/usr/bin/env python3
"""Checks of pull request 173 (ledger rows RT-283 to RT-304, and section 2
version 3 written into the spec), run under the pairing rule of
docs/outside-review-protocol.md by a session that wrote none of it.

Reads only committed git objects (by commit id), plus one file beside this
script: pr165_last_comment.md, John's rulings of 2026-10-12 as posted on pull
request 165 (saved with `gh pr view 165 --json comments --jq
'.comments[-1].body'`). Writes nothing. Calls no model. Run from any checkout
of the repository:

    python3 -I check_pr173.py > check_pr173.out.txt

Each check is built so that its output comes out wrong if the writing were
wrong: counts are printed, not just pass/fail, and every expected value is
printed beside the observed one.
"""
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True, check=True).stdout.strip()

BASE = "a99e8e9"      # main line where the branch was cut
ROWS = "2271b7d"      # commit 1: the ledger rows
HEAD = "1a9752e"      # commit 2: the spec write-in (branch head under check)
V3 = "bfd1d5d"        # version 3 as merged (pull request 170)
CLOSURE = "00b272e"   # closure checks of 2026-10-17 (pull request 171 head)

LEDGER = "experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md"
SPEC = "spec/minimum-viable-mind-proposal-v0.1.md"
V3F = "docs/rulings/2026-10-12-two-sided-question-section-2-v3.md"
CLOSE_MD = "docs/reviews/2026-10-17-section-2-v3-closure-checks-claude-code.md"
CLOSE_OUT = "docs/reviews/2026-10-17-section-2-v3-closure-checks-scripts/closure_checks_v3.out.txt"
INDEX = "docs/reviews/2026-10-09-two-sided-question-gate-a-INDEX.md"
TIER1 = "docs/reviews/2026-10-09-two-sided-question-gate-a-tier1-claude-code.md"
GEMINI = "docs/reviews/2026-10-09-two-sided-question-gate-a-gemini.md"
GPT = "docs/reviews/2026-10-09-two-sided-question-gate-a-gpt.md"
RULINGS_1007 = "docs/rulings/2026-10-07-two-sided-question-rulings.md"
EXP1 = "experiments/01-self-indexing-removal-test/removal-test-findings.md"
ROUTER = "docs/outside-perspective/2026-10-07-router-control-check.md"

EXPECTED_SHA = "3d0baaca5fbf1af08d86652e455ca4e0462c98f7fb424fde09292623256df119"


def show(rev, path):
    return subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"],
                          capture_output=True, check=True).stdout


def text(rev, path):
    return show(rev, path).decode("utf-8")


def git(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True,
                          text=True, check=True).stdout


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    s = s.replace("**", "").replace("`", "")
    s = re.sub(r"(?m)^\s*>\s?", "", s)        # blockquote markers
    s = re.sub(r"\s+", " ", s)
    s = s.replace("'", '"')                   # a quotation inside a quotation flips its marks
    return s.lower()


RANGE = range(283, 305)
ROW_RE = re.compile(r"^\| RT-(\d+)\b")

# ---------------------------------------------------------------------------
head("C1. One row per number RT-283 to RT-304, none before")
base_l = text(BASE, LEDGER).splitlines()
head_l = text(HEAD, LEDGER).splitlines()
rows_l = text(ROWS, LEDGER).splitlines()


def row_counts(lines):
    c = {}
    for i, ln in enumerate(lines, 1):
        m = ROW_RE.match(ln)
        if m:
            c.setdefault(int(m.group(1)), []).append(i)
    return c


bc = row_counts(base_l)
hc = row_counts(head_l)
print(f"  ledger lines: base {len(base_l)}, commit 1 {len(rows_l)}, head {len(head_l)}")
print(f"  highest row number at base: RT-{max(bc)}; at head: RT-{max(hc)}")
print(f"  rows numbered 283..304 at base: {sum(len(bc.get(n, [])) for n in RANGE)} (expected 0)")
mention = [i for i, ln in enumerate(base_l, 1)
           if re.search(r"RT-(28[3-9]|29\d|30[0-4])\b", ln)]
print(f"  base lines mentioning any of RT-283..RT-304 in any form (heading, prose, row): {len(mention)} {mention[:10]}")
per = {n: len(hc.get(n, [])) for n in RANGE}
print("  rows per number at head:", " ".join(f"{n}:{per[n]}" for n in RANGE))
print(f"  numbers with exactly one row: {sum(1 for n in RANGE if per[n] == 1)} of 22; "
      f"with none: {[n for n in RANGE if per[n] == 0]}; with two or more: {[n for n in RANGE if per[n] > 1]}")
print(f"  rows numbered above 304 at head: {sum(len(v) for k, v in hc.items() if k > 304)}")
dups = {k: v for k, v in hc.items() if len(v) > 1}
print(f"  any number at head with two rows (whole ledger): {dups if dups else 'none'}")
sec_start = next(i for i, ln in enumerate(head_l, 1) if ln.startswith("# Rows from the Gate A pass on section 2"))
new_lines = [hc[n][0] for n in RANGE if n in hc]
print(f"  new section heading at line {sec_start}; the 22 rows sit at lines {min(new_lines)}..{max(new_lines)}; "
      f"contiguous and in number order: {new_lines == list(range(min(new_lines), min(new_lines) + 22))}")
cells = sorted({ln.count("|") - 1 for i, ln in enumerate(head_l, 1) if i in new_lines})
print(f"  cells per new row (pipes minus one): {cells} (expected [5])")
d1 = git("diff", "--numstat", BASE, ROWS, "--", LEDGER).split()
d2 = git("diff", "--numstat", ROWS, HEAD, "--", LEDGER).split()
print(f"  ledger diff base..commit 1: +{d1[0]} -{d1[1]} (expected -0: append only); commit 1..head: {d2 or 'no change'}")
print(f"  base ledger is a prefix of head ledger: {head_l[:len(base_l)] == base_l}")

# parse the new rows into cells
rows = {}
for n in RANGE:
    ln = head_l[hc[n][0] - 1]
    c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
    rows[n] = c
section_text = "\n".join(head_l[sec_start - 1:])

# ---------------------------------------------------------------------------
head("C2. Each row's ruling cell: 'all as recommended', and a ruling of 2026-10-12 that exists in both sources")
pr = open(os.path.join(HERE, "pr165_last_comment.md"), encoding="utf-8").read()
print(f"  pr165_last_comment.md SHA-256 {hashlib.sha256(pr.encode()).hexdigest()}")
print(f"  'all as recommended' in the pull request 165 comment: {pr.count('all as recommended')}")
pr_rulings = {}
for m in re.finditer(r"(?m)^(\d)\. \*\*(.+?)\*\*(.*)$", pr):
    pr_rulings[int(m.group(1))] = m.group(2) + m.group(3)
print(f"  numbered rulings in the comment: {sorted(pr_rulings)}")
v3 = text(V3, V3F)
cl = v3[v3.index("## Change log"):]
cl_par = cl[:cl.index("**Numbering.**")]
v3_rulings = sorted({int(x) for x in re.findall(r"\((\d)\)", cl_par)})
print(f"  numbered rulings in version 3's change-log list: {v3_rulings}")
closing = "a session that did not write section 2 or this pass applies the fixes to a version 3"
print(f"  the 'closing line' quoted by the rows, in the comment: {closing in pr}")
idx = text(HEAD, INDEX)
print(f"  \"everything else is the author's to fix\" in the covering note (any case): "
      f"{'everything else is the author' in idx.lower()}")

t2id = {}
for n in RANGE:
    m = re.search(r"\((GPT|Gemini) ([AG]\d+):", rows[n][0])
    if m:
        t2id[n] = m.group(2)

print("  row | 'all as recommended' | 'Ruled by John 2026-10-12' | rulings cited | each cited ruling in comment / in v3 list | cited ruling names this finding")
bad = 0
for n in RANGE:
    disp = rows[n][3]
    aar = '"all as recommended"' in disp
    rbj = "Ruled by John 2026-10-12" in disp
    cited = sorted({int(x) for x in re.findall(r"\bruling (\d)\b(?![\d])(?! of 2026-10-07)", disp)})
    cited = [c for c in cited if not re.search(rf"ruling {c} of 2026-10-07", disp)]
    closing_line = "closing line" in disp
    in_both = all(c in pr_rulings and c in v3_rulings for c in cited)
    ids = [f"RT-{n}"] + ([t2id[n]] if n in t2id else [])
    names = {c: any(re.search(rf"\b{re.escape(i)}\b", pr_rulings[c]) for i in ids) for c in cited}
    # numbered rulings that name this finding although the row does not cite them
    uncited = [k for k, v in pr_rulings.items() if k not in cited
               and any(re.search(rf"\b{re.escape(i)}\b", v) for i in ids)]
    ok = aar and rbj and (cited or closing_line) and in_both and all(names.values()) and not uncited
    bad += not ok
    print(f"  RT-{n} | {aar} | {rbj} | {cited or '-'}{' + closing line' if closing_line else ''} | {in_both} | "
          f"{names or '-'}{' | NAMED BUT NOT CITED: ' + str(uncited) if uncited else ''}")
print(f"  rows failing any part: {bad} of 22")

# ---------------------------------------------------------------------------
head("C3. The three closure lines against the closure-check file and its output")
cmd = text(CLOSURE, CLOSE_MD)
cout = text(CLOSURE, CLOSE_OUT)
print(f"  closure-check file at {CLOSURE} equals main's copy: "
      f"{show(CLOSURE, CLOSE_MD) == show('origin/main', CLOSE_MD)}; output file too: "
      f"{show(CLOSURE, CLOSE_OUT) == show('origin/main', CLOSE_OUT)}")
src = norm(cmd + "\n" + cout)
for n in (283, 284, 289):
    cell = rows[n][4]
    print(f"\n  RT-{n} closure cell, first words: {rows[n][4][:60]!r}")
    sents = re.split(r"(?<=[.;])\s+(?=[A-Z*`\"(])", cell)
    for k, s in enumerate(sents, 1):
        toks = re.findall(r'"([^"]+)"', s) + re.findall(r"`([^`]+)`", s) + re.findall(r"\b\d[\d,.]*\b", s)
        missing = [t for t in toks if norm(t).strip(" .,") not in src]
        print(f"   s{k}: {s[:110]}{'...' if len(s) > 110 else ''}")
        print(f"       tokens {len(toks)}, not found in the closure file or its output: {missing}")

print("\n  RT-284: how many unchanged-spec hits the closure check's output lists, and how many pass its strict test")
t = cout.count("named in the supersession paragraph: True")
f_ = cout.count("named in the supersession paragraph: False")
print(f"    'named ... True': {t}; 'named ... False': {f_}; total hits: {t + f_}")
print(f"    rows of the closure file's table: {len(re.findall(r'(?m)^\| (what|removal|floor)', cmd))}")
print(f"    the row says: {re.findall(r'(nine hits|three of the nine|six are covered|six of the nine)', rows[284][4])}")
print("\n  RT-283: where the one 'no better than' hit sits in version 3 as merged")
v3l = v3.splitlines()
hits = [i for i, ln in enumerate(v3l, 1) if "no better than" in ln and i < 300]
print(f"    file line(s) in v3 at {V3} (section text only, lines 75..293): {hits}")
print(f"    the same as a line number counted from the section's first line (75 = 1): {[h - 74 for h in hits]}")
print(f"    the row says lines: {re.findall(r'lines (\d+ to \d+)', rows[283][4])}; "
      f"the closure file says: {re.findall(r'version 3, lines (\d+ to \d+)', re.sub(r"\s+", " ", cmd))}")
spec_h = text(HEAD, SPEC)
print("    the same comparison elsewhere in the spec at head, under other wording:")
for i, ln in enumerate(spec_h.splitlines(), 1):
    for pat in ("no better than", "no more presence"):
        if pat in ln:
            j = ln.index(pat)
            print(f"      spec line {i}: {pat!r}: ...{ln[max(0, j - 90):j + 70]}...")

# ---------------------------------------------------------------------------
head("C4. Tier 2 findings G1..G9 and A1..A14: each a numbered row or a duplicate, none missing, none twice")
gem = text(HEAD, GEMINI)
gpt = text(HEAD, GPT)
src_ids = sorted(set(re.findall(r"(?m)^\| (G\d+) \|", gem)), key=lambda x: int(x[1:])) + \
    sorted(set(re.findall(r"(?m)^\| \*\*(A\d+)\*\* \|", gpt)), key=lambda x: int(x[1:]))
print(f"  ids in the two replies' finding tables: {len(src_ids)}: {' '.join(src_ids)}")
numbered = [t2id[n] for n in RANGE if n in t2id]
note = re.sub(r"\s+", " ", section_text[section_text.index("*Duplicates, decided here"):section_text.index("*Severity.")])
dup_ids = re.findall(r"\b([AG]\d+) \(", note)
print(f"  ids with a numbered row: {len(numbered)}: {' '.join(numbered)}")
print(f"  ids recorded as duplicates in the section note: {len(dup_ids)}: {' '.join(dup_ids)}")
allc = numbered + dup_ids
print(f"  missing from both: {[i for i in src_ids if i not in allc]}")
print(f"  appearing more than once across both: {sorted({i for i in allc if allc.count(i) > 1})}")
print(f"  in the rows but not in the replies: {[i for i in allc if i not in src_ids]}")
print(f"  ruling 6's named list {re.findall(r'[AG]\d+', pr_rulings[6])} == the numbered rows' ids in order: "
      f"{re.findall(r'[AG]\d+', pr_rulings[6]) == numbered}")

print("\n  duplicate pairings: rows' note against version 3's change log")
v3dup = re.sub(r"[ \t]*\n[ \t]*", " ", cl[cl.index("### Tier 2 findings applied as duplicates"):cl.index("### What this file does not do")])
v3map = {}
for m in re.finditer(r"\*\*([AG]\d+)\*\*: (.*?)(?=\*\*[AG]\d+\*\*:|- \*\*A1\*\*|\Z)", v3dup, re.S):
    v3map[m.group(1)] = sorted(set(re.findall(r"RT-\d+", m.group(2))))
rowmap = {}
for m in re.finditer(r"\b([AG]\d+) \((.*?)\) (?:is|asks for) (.*?)(?=\. [A-Z]|\.\*|$)", note, re.S):
    rowmap[m.group(1)] = sorted(set(re.findall(r"RT-\d+", m.group(3))))
for i in dup_ids:
    a, b = rowmap.get(i), v3map.get(i)
    print(f"    {i}: rows {a}  v3 {b}  {'same' if a == b else 'DIFFERENT'}")

print("\n  severities: each row's cell against the sources")
t1 = text(HEAD, TIER1)
t1sev = {int(m.group(1)): m.group(2) for m in re.finditer(r"(?m)^\| RT-(\d+) \| (fatal|serious|worth-noting) \|", t1)}
gsev = {m.group(1): m.group(2).strip("*").lower() for m in re.finditer(r"(?m)^\| (G\d+) \| (\S+) \|", gem)}
asev = {m.group(1): m.group(2).strip("*").lower() for m in re.finditer(r"(?m)^\| \*\*(A\d+)\*\* \| (\S+) \|", gpt)}
dup_of = {}
for i, rts in rowmap.items():
    for r in rts:
        dup_of.setdefault(int(r[3:]), []).append(i)
for n in RANGE:
    final = rows[n][2]
    if n in t2id:
        i = t2id[n]
        srcsev = gsev.get(i) or asev.get(i)
        exp = srcsev
        info = f"{i} {srcsev}"
    else:
        exp = "fatal" if n in (284, 289) else t1sev[n]
        info = f"tier 1 {t1sev[n]}; " + ", ".join(f"{i} {gsev.get(i) or asev.get(i)}" for i in dup_of.get(n, []))
    got = re.match(r"\**(fatal|serious|worth-noting)", final).group(1)
    print(f"    RT-{n}: row '{got}', expected '{exp}' {'ok' if got == exp else 'DIFFERENT'} | sources: {info}")

# ---------------------------------------------------------------------------
head("C5. The spec at the branch head: checksum, and a diff against the main line")
spec_b = show(HEAD, SPEC)
print(f"  SHA-256 at {HEAD}: {hashlib.sha256(spec_b).hexdigest()}")
print(f"  expected:          {EXPECTED_SHA}  equal: {hashlib.sha256(spec_b).hexdigest() == EXPECTED_SHA}")
print(f"  spec unchanged on the main line since the branch point ({BASE}..origin/main): "
      f"{git('diff', '--numstat', BASE, 'origin/main', '--', SPEC).strip() or 'yes, no diff'}")
diff = git("diff", "-U0", BASE, HEAD, "--", SPEC)
hunks = re.findall(r"(?m)^@@.*@@", diff)
print(f"  hunks: {len(hunks)}: {hunks}")
minus = [ln[1:] for ln in diff.splitlines() if ln.startswith("-") and not ln.startswith("---")]
plus = [ln[1:] for ln in diff.splitlines() if ln.startswith("+") and not ln.startswith("+++")]
print(f"  lines removed: {len(minus)}; lines added: {len(plus)}")


def quoted_block(s, start_marker):
    i = s.index(start_marker)
    lines = s[i:].splitlines()[1:]
    out = []
    started = False
    for ln in lines:
        if ln.startswith(">"):
            started = True
            out.append(ln[1:].strip())
        elif started:
            break
    return " ".join(out)


floor = quoted_block(v3, '**The sentence added to "The Floor"**')
para = quoted_block(v3, '**The paragraph added to "What Would Count Against It"**')
section = v3l[74:293]
print(f"  version 3 pieces: section {len(section)} lines; Floor sentence {len(floor.split())} words; paragraph {len(para.split())} words")
base_spec = text(BASE, SPEC).splitlines()
anchor = "A self-model that can be lopped off while the computation runs was a description all along"
for r in minus:
    rep = [p for p in plus if p.startswith(r)]
    print(f"  removed line is the Floor anchor line: {anchor in r}; its replacement is the old line + ' ' + "
          f"the Floor sentence de-quoted and joined: {r + ' ' + floor in plus}")
classes = {"section": 0, "floor line": 0, "paragraph": 0, "blank": 0, "rule ---": 0, "other": 0}
sec_set = list(section)
others = []
k = 0
for p in plus:
    if k < len(sec_set) and p == sec_set[k]:
        classes["section"] += 1
        k += 1
    elif minus and p == minus[0] + " " + floor:
        classes["floor line"] += 1
    elif p == para:
        classes["paragraph"] += 1
    elif p == "":
        classes["blank"] += 1
    elif p == "---":
        classes["rule ---"] += 1
    else:
        classes["other"] += 1
        others.append(p[:80])
print(f"  added lines by kind: {classes}  (section lines matched in order: {k} of {len(sec_set)})")
print(f"  added lines matching none of the three inserts or layout: {others}")
# where each insert sits
hl = spec_b.decode().splitlines()
print(f"  spec at head: {len(hl)} lines; section heading at line {hl.index(section[0]) + 1}; "
      f"line before it: {hl[hl.index(section[0]) - 1]!r}; "
      f"'## What This Proposal Is' at line {hl.index('## What This Proposal Is') + 1}, preceded by "
      f"{next(j for j in range(1, 10) if hl[hl.index('## What This Proposal Is') - j] != '') - 1} blank line(s)")
pi = hl.index(para)
print(f"  paragraph at line {pi + 1}; two lines up starts: {hl[pi - 2][:60]!r}")
print(f"  heading levels in the spec at head: {sorted({ln.split(' ')[0] for ln in hl if ln.startswith('#')})}; "
      f"the inserted heading: {section[0]!r}")

# ---------------------------------------------------------------------------
head("C6. Inserted section against version 3 lines 75..293, byte for byte; version 3 below its note against bfd1d5d")
v3_b = show(V3, V3F)
sec_bytes = b"\n".join(v3_b.split(b"\n")[74:293])
spec_lines_b = spec_b.split(b"\n")
s0 = spec_lines_b.index(section[0].encode())
spec_sec = b"\n".join(spec_lines_b[s0:s0 + 219])
print(f"  version 3 lines 75..293: {len(sec_bytes)} bytes, SHA-256 {hashlib.sha256(sec_bytes).hexdigest()}")
print(f"  spec lines {s0 + 1}..{s0 + 219}: {len(spec_sec)} bytes, SHA-256 {hashlib.sha256(spec_sec).hexdigest()}")
print(f"  identical: {sec_bytes == spec_sec}")
print(f"  version 3 line 294 is blank: {v3_b.split(b'\n')[293] == b''}; line 295: {v3_b.split(b'\n')[294][:40]!r}")
v3_head = show(HEAD, V3F)
print(f"  version 3 unchanged between {V3} and the branch point {BASE}: {show(BASE, V3F) == v3_b}")
d = git("diff", "-U0", V3, HEAD, "--", V3F)
print(f"  diff {V3}..{HEAD} on version 3: hunks {re.findall(r'(?m)^@@.*@@', d)}; "
      f"lines removed {sum(1 for ln in d.splitlines() if ln.startswith('-') and not ln.startswith('---'))}; "
      f"lines added {sum(1 for ln in d.splitlines() if ln.startswith('+') and not ln.startswith('+++'))}")
hl3 = v3_head.split(b"\n")
note_end = next(i for i in range(1, len(hl3)) if hl3[i].startswith(b"*Written 2026-10-12"))
rebuilt = b"\n".join(hl3[:2] + hl3[note_end:])
print(f"  head's version 3 with its lines 3..{note_end} (the dated note and its blank line) removed equals {V3}'s file: "
      f"{rebuilt == v3_b} ({note_end - 2} lines removed)")

# ---------------------------------------------------------------------------
head("C7. Every double-quoted phrase in the new section, looked for in the sources")
corpus = {
    "v3 section+inserts": norm("\n".join(section) + "\n" + floor + "\n" + para),
    "v3 file": norm(v3),
    "PR 165 comment": norm(pr),
    "covering note": norm(idx),
    "tier 1": norm(t1),
    "Gemini": norm(gem),
    "GPT": norm(gpt),
    "closure file+output": src,
    "rulings 2026-10-07": norm(text(HEAD, RULINGS_1007)),
    "experiment 1 findings": norm(text(HEAD, EXP1)),
    "router-control note": norm(text(HEAD, ROUTER)),
    "spec at base": norm(text(BASE, SPEC)),
    "ledger before the rows": norm(text(BASE, LEDGER)),
}
quotes = re.findall(r'"([^"]{3,})"', section_text)
nf = 0
for q in quotes:
    frags = [f.strip(" .,;:") for f in re.split(r"\.\.\.|…", q) if f.strip(" .,;:")]
    where = [k for k, v in corpus.items() if all(norm(f) in v for f in frags)]
    if not where:
        nf += 1
        # nearest: which fragments are found anywhere
        found = [(f, [k for k, v in corpus.items() if norm(f) in v]) for f in frags]
        print(f"  NOT FOUND whole: \"{q[:100]}\"  fragments: {found}")
print(f"  quoted phrases: {len(quotes)}; found whole in at least one source: {len(quotes) - nf}; not found: {nf}")
print("\n  quotes the rows attribute to the applied text ('Applied ...' clauses) that are not in the applied text:")
for n in RANGE:
    disp = rows[n][3]
    if "Applied" not in disp:
        continue
    applied = disp[disp.index("Applied"):]
    for q in re.findall(r'"([^"]{3,})"', applied):
        frags = [f.strip(" .,;:") for f in re.split(r"\.\.\.|…", q) if f.strip(" .,;:")]
        if not all(norm(f) in corpus["v3 section+inserts"] for f in frags):
            others_ = [k for k, v in corpus.items() if all(norm(f) in v for f in frags)]
            print(f"    RT-{n}: \"{q[:90]}\" -> found instead in: {others_}")

print("\n  RT-304's quoted phrase, against the Floor sentence it names and against section 2:")
q = "this project's definition of the floor and not"
print(f"    {q!r} in the Floor sentence: {norm(q) in norm(floor)}; in section 2: "
      f"{norm(q) in norm(chr(10).join(section))}; in version 3's change log: {norm(q) in norm(cl)}")
for pat in (r"treats the test as its definition of the floor and not as an instrument for it",
            r"this project's definition of the floor, not its instrument for it"):
    print(f"    {pat!r}: Floor sentence {norm(pat) in norm(floor)}; section 2 {norm(pat) in norm(chr(10).join(section))}")

# ---------------------------------------------------------------------------
head("C8. Other claims the rows make, each against its source")
words = {}
for n in RANGE:
    m = re.match(r"\*\*(Open|Closed: the claim was checked|Closed: the argument was accepted)", rows[n][4])
    words.setdefault(m.group(1) if m else "UNMATCHED", []).append(n)
print("  closure words over the 22 rows: " + "; ".join(f"{k}: {len(v)} {v}" for k, v in words.items()))
print(f"  the section's count line says: {re.findall(r'Closed with the claim checked: (\d+)|Closed with the argument accepted: (\d+)|Open: (\d+)', re.sub(chr(10), ' ', section_text))}")
v3num = re.findall(r"\*\*RT-(\d+), which is ([AG]\d+)\*\*", v3)
print(f"  version 3's numbers for the tier 2 findings: {v3num}")
print(f"  rows' numbers for them: {[(str(n), t2id[n]) for n in RANGE if n in t2id]}  same: "
      f"{v3num == [(str(n), t2id[n]) for n in RANGE if n in t2id]}")
a10 = gpt[gpt.index("### A10"):gpt.index("## 4. Over-reading")]
print(f"  GPT's A10 names the founding wager (the rows pair A10 with RT-290 too; version 3 does not): "
      f"{'founding-wager' in a10}")
hl_ledger = [ln.split(" ")[0] for ln in head_l if re.match(r"#+ ", ln)]
print(f"  ledger headings at head: '#' {hl_ledger.count('#')} (lines "
      f"{[i for i, ln in enumerate(head_l, 1) if ln.startswith('# ')]}), '##' {hl_ledger.count('##')}, '###' {hl_ledger.count('###')}")
print("  RT-284's line numbers in John's unchanged text, against the spec at the branch point:")
bs = text(BASE, SPEC).splitlines()
for ln_no, phrase in ((10, "subject to a removal test"), (10, "minimum measurable structural correlate"),
                      (17, "\"Minimum viable\" names the smallest system"), (39, "settled by removal"),
                      (45, "survives the removal test"), (45, "minimum viable conscious machine a two-part definition"),
                      (68, "pass-fail criterion is the removal test"), (87, "measurement that speaks to an inside"),
                      (87, "Interpretability is the route"), (105, "removal test as the intuition")):
    found = [i for i, ln in enumerate(bs, 1) if phrase in ln]
    print(f"    {phrase!r}: line(s) {found} (row/closure file: {ln_no}) {'ok' if found == [ln_no] else 'DIFFERENT'}")
print("  RT-292's figures, read from experiment 1's committed interval file at the branch head:")
import json
ci = json.loads(text(HEAD, "experiments/01-self-indexing-removal-test/removal_ci.json"))
cells = ci["cells"]["idxres_mean_k16"]
for k in ("T_self_irrelevant", "T_self_relevant", "T_syntax"):
    c = cells[k]
    print(f"    drop on {k}: {c['point']:.4f} [{c['lo']:.4f}, {c['hi']:.4f}]  lower bound above zero: {c['lo'] > 0}")
g = ci["derived"]["router_gap_idxres_mean_k16"]
print(f"    router gap: {g['point']:+.4f} [{g['lo']:+.4f}, {g['hi']:+.4f}]")
fl = norm(floor)
print(f"    the Floor sentence (now spec line 263) says 'each interval above zero': {'each interval above zero' in fl}")
print(f"    the RT-292 row says it too: {'each interval above zero' in rows[292][3]}")
exp1 = text(HEAD, EXP1)
print(f"    the findings file's own word for a lower bound of 0.000: "
      f"{re.findall(r'lower bound touches zero', exp1)}")
