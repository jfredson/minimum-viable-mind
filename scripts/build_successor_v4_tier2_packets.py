#!/usr/bin/env python3
"""Build the two tier 2 review packets for successor proposal version 4.

Gate A (the registration review), tier 2: the outside pass, run by John in the
Gemini and ChatGPT apps under docs/outside-review-protocol.md. Both packets carry
the same records, in the same order, byte for byte. The Gemini packet is one
document. The ChatGPT packet is the same material split into numbered files small
enough that the app takes each one as pasted text rather than turning it into an
attachment it only searches (the 28,000-character limit learned on the Amendment
A3 closure packets of 2026-09-21).

    python3 scripts/build_successor_v4_tier2_packets.py           # build, write, check
    python3 scripts/build_successor_v4_tier2_packets.py --verify  # check what is on disk

The packets are generated, never hand-edited. --verify rebuilds from today's
sources and compares with the files as committed, so a source that changed after
the packets were built is reported as stale, by file name.

Every record is either a whole file reproduced unedited, or (for the review
protocol only) whole sections of it, cut at its own headings. Nothing is
paraphrased, and the check below proves it record by record.
"""

import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
E = "experiments/06-mvm-0a-constructed-self-index/"
OUT = E + "reviews/packets/"
STAMP = "2026-10-04-successor-v4-tier2"
TARGET = "docs/successor-experiment-proposal-2026-10-03-v4.md"
TIER1 = E + "reviews/2026-10-04-successor-v4-gate-a-claude-code.md"
INDEX = OUT + "2026-10-04-successor-v4-tier2-INDEX-how-to-run-these-sessions.md"
PROTOCOL = "docs/outside-review-protocol.md"
LIMIT = 28000  # bytes per ChatGPT file

# The order here is the order in both packets.
#   whole    - a complete file, reproduced unedited
#   sections - whole sections of a file, from one heading up to the next heading
#              named, reproduced unedited
RECORDS = [
    dict(kind="sections", source=PROTOCOL,
         start="## The brief, fixed, sent unchanged with every packet",
         end="## The closure rule, which is the new part",
         title="THE BRIEF - the questions you are answering (fixed protocol text, sent unchanged to every reviewer)"),
    dict(kind="sections", source=PROTOCOL,
         start="## The closure rule, which is the new part",
         end="## Rebuild a document when new binding text starts to depend on it",
         title="the closure rule this text is being reviewed under"),
    dict(kind="sections", source=PROTOCOL,
         start="## The measurement rehearsal, required before any Gate A",
         end="## The failure-mode pass: the known failures are run against the design, not cited",
         title="the rule that a full measurement rehearsal comes before any registration review"),
    dict(kind="whole", source=TARGET,
         title="THE TEXT UNDER REVIEW - successor experiment proposal, version 4"),
    dict(kind="whole", source=TIER1,
         title="the inside reviewer's findings on version 4 (Gate A, tier 1)"),
    dict(kind="whole", source="docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md",
         title="John's rulings of 2026-10-03 on the review of version 3 (binding on version 4)"),
    dict(kind="whole", source="docs/rulings/2026-10-03-controls-rerun-rulings.md",
         title="John's three rulings of 2026-10-03 after the controls re-run"),
    dict(kind="whole", source="docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md",
         title="John's evening ruling of 2026-10-03: the fifth outcome and the figure printed both ways"),
    dict(kind="whole", source="docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md",
         title="first record of John's ruling on version 4's seven questions"),
    dict(kind="whole", source="docs/rulings/2026-10-03-version-4-questions-rulings.md",
         title="second record of the same ruling, which stands where the two differ"),
    dict(kind="whole", source="docs/rulings/2026-10-03-seven-questions-reconciliation.md",
         title="John's ruling on which of the two records stands"),
    dict(kind="whole", source="docs/rulings/2026-10-03-version-4-check-questions-rulings.md",
         title="John's ruling on the two questions raised by the check of version 4"),
    dict(kind="whole", source="docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md",
         title="John's ruling of 2026-10-04 on seven questions from the competing-solver run and the twenty-piece control"),
    dict(kind="whole", source=E + "reviews/2026-10-03-proposal-v4-check-claude-code.md",
         title="the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry)"),
    dict(kind="whole", source=E + "reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md",
         title="the check of the competing-solver run and the twenty-piece control"),
    dict(kind="whole", source="docs/2026-09-21-successor-measure-rehearsal.md",
         title="the measurement rehearsal on small stand-in models"),
    dict(kind="whole", source="docs/2026-09-26-rehearsal-repairs.md",
         title="the repairs to the rehearsal"),
    dict(kind="whole", source="docs/2026-09-26-toy-rerun-v3-rules.md",
         title="the toy re-run under version 3's rules"),
    dict(kind="whole", source="docs/2026-10-03-controls-rerun.md",
         title="the controls re-run under the registered rules (source of every toy figure in version 4)"),
    dict(kind="whole", source="docs/2026-10-03-short-prestated-run.md",
         title="the short pre-stated run"),
    dict(kind="whole", source="docs/2026-10-03-competing-solver-run.md",
         title="the ordinary competing solver put through the measurement"),
    dict(kind="whole", source="docs/2026-10-03-control-2-twenty-draws.md",
         title="the other-agent control against twenty random pieces (NOT A RESULT: a code test)"),
    dict(kind="whole", source="docs/known-failure-modes.md",
         title="the list of what has gone wrong in this program before, which the inside reviewer ran against version 4"),
    dict(kind="lines", source=E + "src/curriculum_a3.py", first=1, last=118,
         title="the opening description of the closed design's task grammar, which version 4 says its grammar extends (inside finding RT-239)"),
    dict(kind="lines", source="experiments/rehearsal-successor-measure/src/grammar.py", first=1, last=70,
         title="the opening description of the rehearsal's task grammar (inside finding RT-239)"),
]

TITLE = "Review packet - the registration text of the successor experiment (Minimum Viable Mind), Gate A, outside pass"

ORIENTATION = """\
## What you are looking at, from a standing start

**The program.** Minimum Viable Mind is a small independent research program,
run by one person on a budget of a few hundred dollars. It trains small language
models from scratch on tasks built for one question, and writes down in advance
what would count as a result and what would count as a failure. That
written-in-advance document is called a *registration*. Once committed it is
never edited; a change is a numbered amendment, committed before anything runs.
It is the discipline a clinical trial uses when it registers its endpoints
before it enrols anyone.

**The text under review** is version 4 of the proposal for the "successor
experiment" (record 4 below, about 290,000 characters). In its own words
(section 0): the experiment builds systems whose degree of entanglement is fixed
by construction - one where "which agent am I" sits in a slot that can be
swapped on its own, one where it is stirred into everything, one that mixes the
two by item - plus one ordinary freely trained system, and asks whether a
transplant-based measure can tell the built systems apart. If it can, the freely
trained system gets a reading. You are reviewing it **as registration text**:
once this review closes, it becomes the binding registration, and the runs it
describes (about $192 to $204 of rented compute in all, released in two parts,
by version 4's section 12.4) are launched against it.

**What the registration will actually say.** Version 4 is not quite the final
wording. Records 6 to 15 are the rulings and checks that bear on it. Records 6
to 11 are already written into version 4: 6 to 8 came before it, and 9 to 11
were committed with it. Records 12 and 13 (two later rulings) and the wording
fixes listed in the two checks (records 14 and 15) are **not yet** written in.
The inside review (record 5) lists every one of those changes in its section
"The registration text as reviewed". Read version 4 together with them. Where
version 4 conflicts with a ruling, or a ruled change cannot be written in as
described, that is in scope.

**Version 4's opening says it "cannot go to the registration review yet"** and
lists three things in front of it: a check of version 4 by another session, a
run of an ordinary competing solver, and John opening the review. All three are
done: the check is record 14, the solver run is record 21 with its check in
record 15, and John opened this review on 2026-10-04 (recorded in
`docs/rulings/2026-10-04-registration-review-opened.md`, not carried here
because it changes nothing in version 4). That opening paragraph is
history, not a live condition.

**Who has already looked.** An inside reviewer - a separate Claude session with
code access, which could run checks - reviewed version 4 first. Its findings are
record 5. You are given them so you can look elsewhere: you are not asked to
re-derive them, and you may disagree with them. Any fatal finding in them is
**not yet fixed** in the text you are shown: fixes are written only after both
tiers report and John rules, so you are reading the text as it stood when the
inside review ran. The inside reviewer's findings
are labelled MEASURED (a check was run and the output reported) or ARGUED
(reasoning). Yours will all be ARGUED, because you see documents and not the
running code, and that is expected.

**What you are not shown.** Version 4 cites many more files than any reader can
be handed in one sitting (code, output files, older reviews and rulings). The
records here are the text, the inside findings, every ruling that changes the
text, the two checks of it, and the run records its numbers come from. The
other files it cites are listed at the end of this note. If a finding of yours
turns on one of them, say which, and say what you would need it to contain:
that is a useful finding, not a failure of the review.

**How the material is marked.** Every record opens with a line beginning
`===== RECORD` that names it, says whether it is a complete file, whole
sections of one, or a range of its lines, and gives its path in the repository, and closes with a line
beginning `===== END OF RECORD`. Cite records by that path, and version 4 by its
section numbers.

**How to answer.** Answer the brief (record 1) in its four parts, a table first
in each, severity marked fatal, serious or worth-noting, and a one-paragraph
kill case at the end whether or not you think the text should be registered.
Plain language. Looking things up is allowed; say when you did. Do not soften
findings to be polite, and do not manufacture severity to look thorough. A
review that finds nothing fatal is a valid result, reported as what was checked
and what held.
"""

GEMINI_DELIVERY = """\
*This is the whole packet in one document. Read it from start to finish before
answering - do not search it for passages that match the questions. Then answer
the brief, which is record 1. Label your findings G1, G2, G3 and so on.*
"""

CHATGPT_DELIVERY = """\
*This packet arrives as {n} files pasted into this one conversation, in order.
This is file 1. Do not begin your review until file {n} has arrived: reply to
each file with one short line saying you have it, and nothing else. Read each
file as text, start to finish, rather than searching it. The brief you are
answering is record 1, in this file. Label your findings A1, A2, A3 and so on.*

*If a file arrives cut short, or the app turns one into an attachment you can
only search rather than read, say so at once and name the file, before going
on.*
"""

CHATGPT_MIDFILE = (
    "*This is file {i} of {n} of one review packet, pasted into a single "
    "conversation. It contains {what}. Reply with one short line saying you have "
    "it, and wait for the rest: the brief is record 1, in file 1, and your review "
    "comes only after file {n} arrives. If this file looks cut short, say so now.*")

CHATGPT_LASTFILE = (
    "*This is file {i} of {n}, the last one, of a review packet pasted into a "
    "single conversation. It contains {what}. You now have the whole packet. "
    "Answer the brief (record 1, in file 1) now, in its four parts, with the kill "
    "case at the end, labelling your findings A1, A2, A3 and so on. If any file "
    "was missing or cut short, name it at the top of your answer.*")


def read(path):
    with open(os.path.join(ROOT, path), "r", encoding="utf-8") as fh:
        return fh.read()


def sections(path, start, end):
    """Whole lines from the heading `start` up to (not including) heading `end`.
    Both headings must appear exactly once."""
    lines = read(path).split("\n")
    def find(h):
        hits = [i for i, l in enumerate(lines) if l == h]
        if len(hits) != 1:
            raise SystemExit("heading {!r} appears {} times in {}".format(h, len(hits), path))
        return hits[0]
    a, b = find(start), find(end)
    out = lines[a:b]
    while out and out[-1].strip() == "":
        out.pop()
    return "\n".join(out) + "\n"


def record_body(rec):
    if rec["kind"] == "whole":
        return read(rec["source"])
    if rec["kind"] == "lines":
        lines = read(rec["source"]).splitlines(keepends=True)
        return "".join(lines[rec["first"] - 1:rec["last"]])
    return sections(rec["source"], rec["start"], rec["end"])


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def nbytes(s):
    return len(s.encode("utf-8"))


def label(rec, body):
    if rec["kind"] == "whole":
        return "complete file, {:,} characters".format(len(body))
    if rec["kind"] == "lines":
        return "lines {} to {} of the file's {}, unedited".format(
            rec["first"], rec["last"], len(read(rec["source"]).splitlines()))
    full = len(read(rec["source"]))
    return ("whole sections of the file, from the heading \"{}\" up to the next "
            "heading quoted in the protocol; {:,} of the file's {:,} characters"
            .format(rec["start"].lstrip("# "), len(body), full))


def open_line(i, n, rec, body, part=None):
    p = "" if part is None else ", part {} of {}".format(*part)
    return "===== RECORD {} of {}{} - {} - `{}` ({}) =====".format(
        i, n, p, rec["title"], rec["source"], label(rec, body))


def close_line(i, part=None):
    p = "" if part is None else ", part {}".format(part[0])
    return "===== END OF RECORD {}{} =====".format(i, p)


def cited_not_included():
    """Every repository file version 4 names that this packet does not carry."""
    text = read(TARGET)
    names = set(re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|py|sh|toml|json|csv|txt))`", text))
    tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout.split()
    included = {r["source"] for r in RECORDS}
    out = set()
    for n in names:
        if n in tracked:
            path = n
        else:
            hits = [t for t in tracked if t.endswith("/" + n)]
            if len(hits) != 1:
                continue  # a short name matching no committed file, or several
            path = hits[0]
        if path not in included:
            out.add(path)
    return sorted(out)


def split_body(body, room):
    """Cut a record into pieces of at most `room` bytes, only after a blank line
    outside a code fence. The pieces concatenate back to the record exactly."""
    lines = body.splitlines(keepends=True)
    pieces, cur, size, last_ok, fence = [], [], 0, None, False
    for ln in lines:
        if cur and size + nbytes(ln) > room and last_ok:
            pieces.append("".join(cur[:last_ok]))
            cur = cur[last_ok:]
            size = sum(nbytes(x) for x in cur)
            last_ok = None
        cur.append(ln)
        size += nbytes(ln)
        if ln.strip().startswith("```"):
            fence = not fence
        if ln.strip() == "" and not fence:
            last_ok = len(cur)
    pieces.append("".join(cur))
    assert "".join(pieces) == body, "split lost or added material"
    return [p for p in pieces if p]


def build():
    n = len(RECORDS)
    bodies = [record_body(r) for r in RECORDS]
    missing = cited_not_included()

    head = "# " + TITLE + "\n\n" + ORIENTATION
    head += "\n**The records in this packet, in order.**\n\n"
    for i, (r, b) in enumerate(zip(RECORDS, bodies), 1):
        head += "{}. {} - `{}` ({})\n".format(i, r["title"], r["source"],
                                             {"whole": "complete", "sections": "whole sections",
                                              "lines": "lines {} to {}".format(r.get("first"), r.get("last"))}[r["kind"]])
    head += ("\n**Files version 4 cites that are not in this packet** ({} of them; "
             "named so you know they exist, not because you need them; found by looking for "
             "file names in version 4, so a short name that matches several files, or none, is "
             "left off, and a file cited in some other way may be missing):\n\n".format(len(missing)))
    head += "\n".join("- `{}`".format(m) for m in missing) + "\n"

    # Gemini: one document.
    gem = [head, "\n", GEMINI_DELIVERY, "\n"]
    for i, (r, b) in enumerate(zip(RECORDS, bodies), 1):
        gem += [open_line(i, n, r, b), "\n", b, "\n" if not b.endswith("\n") else "",
                close_line(i), "\n\n"]
    gem.append("*End of the packet. Answer the brief now. Label your findings G1, G2, G3 and so on. "
               "The brief is record 1; it is repeated here, unchanged, so it is fresh when you answer:*\n\n")
    gem.append(bodies[0])
    gemini = "".join(gem)

    # ChatGPT: the same, cut into files of at most LIMIT bytes, only at record
    # boundaries or blank lines. File 1 opens with the orientation; each file is
    # filled before the next is started, so John has as few pastes as possible.
    HEADROOM = 1200   # the file's own instruction line, and the marker lines
    MARKERS = 700     # one record's opening and closing marker lines
    files, cur, cur_size = [], [], nbytes(head) + nbytes(CHATGPT_DELIVERY) + 200
    for i, (r, b) in enumerate(zip(RECORDS, bodies), 1):
        rest = b
        pieces = []
        while rest:
            room = LIMIT - HEADROOM - cur_size - MARKERS
            if nbytes(rest) <= room:
                pieces.append(rest)
                cur.append([i, rest, r])
                cur_size += nbytes(rest) + MARKERS
                rest = ""
            elif room > 4000 and len(split_body(rest, room)) > 1 \
                    and nbytes(split_body(rest, room)[0]) <= room:
                first = split_body(rest, room)[0]
                pieces.append(first)
                cur.append([i, first, r])
                rest = rest[len(first):]
                files.append(cur)
                cur, cur_size = [], 0
            else:
                if not cur:
                    raise SystemExit("record {} has no place to cut within {} bytes"
                                     .format(i, room))
                files.append(cur)
                cur, cur_size = [], 0
        # number the parts of this record
        k = len(pieces)
        n_seen = 0
        for fl in files + [cur]:
            for u in fl:
                if u[0] == i and len(u) == 3:
                    n_seen += 1
                    u.append(None if k == 1 else (n_seen, k))
    files.append(cur)
    files = [[(u[0], u[3], u[1], u[2]) for u in fl] for fl in files if fl]
    nfiles = len(files)
    out = {}

    def what(fl):
        seen = []
        for (i, part, _, r) in fl:
            d = "record {} ({})".format(i, r["title"]) if part is None else \
                "record {} part {} of {} ({})".format(i, part[0], part[1], r["title"])
            seen.append(d)
        return "; ".join(seen)

    def render(fl):
        txt = []
        for (i, part, body, r) in fl:
            txt += [open_line(i, n, r, bodies[i - 1], part), "\n", body,
                    "" if body.endswith("\n") else "\n", close_line(i, part), "\n\n"]
        return "".join(txt)

    for j, fl in enumerate(files, 1):
        recs = sorted({u[0] for u in fl})
        slug = "records-{}".format(recs[0]) if len(recs) == 1 else \
            "records-{}-to-{}".format(recs[0], recs[-1])
        if j == 1:
            top = head + "\n" + CHATGPT_DELIVERY.format(n=nfiles) + "\n"
            slug = "start-here-and-" + slug
        else:
            tmpl = CHATGPT_LASTFILE if j == nfiles else CHATGPT_MIDFILE
            top = tmpl.format(i=j, n=nfiles, what=what(fl)) + "\n\n"
        tail = ""
        if j == nfiles:
            tail = ("*End of the packet. The brief is record 1, in file 1; it is repeated "
                    "here, unchanged, so it is fresh when you answer:*\n\n" + bodies[0])
        out[j] = (slug, top + render(fl) + tail)

    paths = {}
    paths[OUT + STAMP + "-gemini.md"] = gemini
    for j, (slug, txt) in out.items():
        paths[OUT + "{}-chatgpt-{:02d}-of-{:02d}-{}.md".format(STAMP, j, nfiles, slug)] = txt
    return paths, bodies, missing


INDEX_HEAD = """\
# How to run the two outside-review sessions on successor proposal version 4

*For John. Gate A (the registration review), tier 2 (the outside pass), under
`docs/outside-review-protocol.md`. Every packet file named below was generated
by `scripts/build_successor_v4_tier2_packets.py` from committed files, and is
never hand-edited. Re-running that script rebuilds them and re-checks them;
`--verify` checks the committed files without rewriting them.*

## The short version

Two sessions, one per outside reviewer, run by you in their apps. Both get
exactly the same material: the brief, version 4 of the proposal, the inside
reviewer's findings, every ruling and check that changes version 4 before it is
registered, and the run records its numbers come from. Only the delivery
differs:

- **Gemini** gets one document, {gem_kb:,} KB.
- **ChatGPT** gets the same material as {nfiles} files, none bigger than
  {limit_kb} KB, pasted into **one** conversation, in order.

The material in the two packets was compared character by character after they
were built and is the same: {nchar:,} characters of records in each, with the
same fingerprint (a sha256 checksum, the standard way of showing two texts are
identical to the byte):

    {sha}

Each of the {nrec} records was also compared with the file it comes from,
character for character: {nwhole} are whole files, 3 are whole sections of
the review protocol, cut at its own headings, and 2 are the opening lines of two
code files, by line number.

## Session 1 - Gemini, one document

1. New chat. Give it `{gem_name}` whole: paste it if the app takes the paste,
   attach the file if it does not.
2. The document tells it what to do, including to read start to finish rather
   than search, and to label its findings G1, G2, G3 and so on.
3. When it answers, check that it refers to records by file name and to version
   4 by section number. If it says it saw only part of the document, stop and
   give it the ChatGPT files instead, in one conversation, in order: they carry
   identical material.

## Session 2 - ChatGPT, one conversation, {nfiles} pastes

**This is one session, not {nfiles} sessions.** A reviewer who sees part of the
record in each of several chats has reviewed nothing.

1. New chat.
2. **Paste the contents** of file 01, then 02, and so on, one message each. Do
   not attach them: an attachment may be searched rather than read.
3. Each file tells it to reply with one short line and wait. After file {nfiles}
   it gives the review. If it starts early, tell it to wait for the rest.
4. The files are numbered in their names; filename order is the right order.
5. **This packet is large**: roughly 200,000 to 230,000 tokens (a rough
   estimate, not counted), nearly twice the packet ChatGPT read in full on
   2026-09-21. Use the model with the largest memory the app offers. The last
   file repeats the brief, so it is fresh when the model answers. Before it
   gives its review, ask it to quote the four part headings of the brief and
   the first line of record 4. If it cannot, it has lost the start of the
   packet: stop and say so, rather than filing a review of part of it.

## If the app balks

- **A paste is turned into an attachment anyway.** Undo it, split that one file
  in half at a line beginning `===== RECORD` or at a blank line, and paste the
  halves as two messages, saying "part 1 of 2 of file N" in front of each.
- **A file comes back cut short.** Paste it again; if it happens twice, split it
  as above.
- **The conversation reaches its length limit before the last file.** Do not
  carry on in a second chat. Stop, note which file you reached, and say so. A
  review of part of the record reads as disagreement with the other reviewer
  when it is really a difference in what each was shown.

## File each response before you start the next session

Paste each answer, word for word, into
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-<model>.md`
(for example `...-gemini.md`, `...-chatgpt.md`), with the model, its version as
the app reports it, the date and the mode (documents shown, lookup allowed) at
the top. Never edit it afterwards. Do not show either reviewer what the other
said; the disagreement between them is the thing being bought. A Claude session
can do the filing from a paste if you prefer.

## What happens next

The findings keep their labels (G1... from Gemini, A1... from ChatGPT). A
session drafts a ruling packet on every item from both tiers; you rule on each
(accept, accept with change, decline, carry open). Any fatal finding gets a fix
and then a measured check of that fix by a session that did not write it, before
the registration is committed. The registration text - version 4 with every
ruled change written in - is then written, checked, and committed, and the
first registered run can launch.

## The files

| order | file | size | what is in it |
|---|---|---|---|
"""


def build_index(paths, nchar, digest, nfiles):
    gem = [p for p in paths if p.endswith("-gemini.md")][0]
    rows = ["| Gemini session | `{}` | {:,} KB | the whole packet in one document |".format(
        os.path.basename(gem), nbytes(paths[gem]) // 1000)]
    chats = sorted(p for p in paths if "-chatgpt-" in p)
    for j, p in enumerate(chats, 1):
        recs = sorted(set(int(x) for x in re.findall(r"^===== RECORD (\d+) of", paths[p], re.M)))
        what = "; ".join("{}. {}".format(r, RECORDS[r - 1]["title"]) for r in recs)
        if j == 1:
            what = "orientation, the list of records, and how to answer; " + what
        rows.append("| ChatGPT {} of {} | `{}` | {:.1f} KB | {} |".format(
            j, nfiles, os.path.basename(p), nbytes(paths[p]) / 1000, what))
    text = INDEX_HEAD.format(
        gem_kb=nbytes(paths[gem]) // 1000, nfiles=nfiles, limit_kb=LIMIT // 1000,
        nchar=nchar, sha=digest, nrec=len(RECORDS),
        nwhole=sum(1 for r in RECORDS if r["kind"] == "whole"),
        gem_name=os.path.basename(gem))
    text += "\n".join(rows) + "\n"
    text += BUILT_FROM.format(target_commit=git_head(TARGET), tier1_commit=git_head(TIER1))
    return text


BUILT_FROM = """
## What was built from what

- Version 4 of the proposal: `{target}`, last changed at commit `{{target_commit}}`.
- The inside reviewer's findings: `{tier1}`, last changed at commit `{{tier1_commit}}`.
- The brief, the closure rule and the rehearsal rule: `{protocol}`, as committed.
- Every other record: the file named in its marker line, as committed.

## If version 4, the findings, or any record changes before you run the sessions

Run `python3 scripts/build_successor_v4_tier2_packets.py` from the top of the
repository. It rebuilds both packets and this page and prints the check. Then
use the rebuilt files from the start: a change to an early record can move every
later cut between files. Do not mix files from two builds.
""".format(target=TARGET, tier1=TIER1, protocol=PROTOCOL)


def git_head(path):
    r = subprocess.run(["git", "log", "-1", "--format=%h", "--", path], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout.strip() or "(not yet committed)"



RECORD_RE = re.compile(r"^===== RECORD (\d+) of (\d+)(?:, part (\d+) of (\d+))? - .*=====$")
END_RE = re.compile(r"^===== END OF RECORD (\d+)(?:, part (\d+))? =====$")


def extract(text):
    """Pull each record (joining parts) out of packet text, using only the marker
    lines. Returns {record number: body}."""
    recs, cur, buf = {}, None, []
    for ln in text.split("\n"):
        m = RECORD_RE.match(ln)
        if m and cur is None:
            cur, buf = int(m.group(1)), []
            continue
        e = END_RE.match(ln)
        if e and cur is not None and int(e.group(1)) == cur:
            chunk = "\n".join(buf) + "\n"
            recs[cur] = recs.get(cur, "") + chunk
            cur = None
            continue
        if cur is not None:
            buf.append(ln)
    return recs


def verify(paths, bodies):
    problems = []
    gem = [t for p, t in paths.items() if p.endswith("-gemini.md")][0]
    chat = "".join(t for p, t in sorted(paths.items()) if "-chatgpt-" in p)
    g, c = extract(gem), extract(chat)
    for i, b in enumerate(bodies, 1):
        want = b if b.endswith("\n") else b + "\n"
        for name, got in (("Gemini", g), ("ChatGPT", c)):
            if got.get(i) != want:
                problems.append("record {} differs from its source in the {} packet ({})"
                                .format(i, name, RECORDS[i - 1]["source"]))
    for p, t in paths.items():
        if "-chatgpt-" in p and nbytes(t) > LIMIT:
            problems.append("{} is {:,} bytes, over the {:,} limit".format(p, nbytes(t), LIMIT))
    gm = "".join(g.get(i, "") for i in range(1, len(bodies) + 1))
    cm = "".join(c.get(i, "") for i in range(1, len(bodies) + 1))
    return problems, sha(gm), sha(cm), len(gm)


def main():
    verify_only = "--verify" in sys.argv
    paths, bodies, missing = build()
    if verify_only:
        stale = []
        on_disk = sorted(f for f in os.listdir(os.path.join(ROOT, OUT)) if f.startswith(STAMP))
        want = sorted(os.path.basename(p) for p in paths)
        if [f for f in on_disk if not f.endswith("INDEX-how-to-run-these-sessions.md")] != want:
            stale.append("the set of packet files on disk differs from a fresh build")
        for p, t in paths.items():
            full = os.path.join(ROOT, p)
            if os.path.exists(full) and read(p) != t:
                stale.append("{} is stale".format(p))
        disk = {p: read(p) for p in paths if os.path.exists(os.path.join(ROOT, p))}
        problems, gs, cs, nchar = verify(disk, bodies)
        nfiles = sum(1 for p in paths if "-chatgpt-" in p)
        if not os.path.exists(os.path.join(ROOT, INDEX)) or \
                read(INDEX) != build_index(paths, nchar, gs, nfiles):
            stale.append("{} is stale".format(INDEX))
        problems = stale + problems
    else:
        os.makedirs(os.path.join(ROOT, OUT), exist_ok=True)
        for f in os.listdir(os.path.join(ROOT, OUT)):
            if f.startswith(STAMP):
                os.remove(os.path.join(ROOT, OUT, f))
        for p, t in paths.items():
            with open(os.path.join(ROOT, p), "w", encoding="utf-8") as fh:
                fh.write(t)
        problems, gs, cs, nchar = verify(paths, bodies)
        nfiles = sum(1 for p in paths if "-chatgpt-" in p)
        with open(os.path.join(ROOT, INDEX), "w", encoding="utf-8") as fh:
            fh.write(build_index(paths, nchar, gs, nfiles))
        print("wrote " + INDEX)

    print("records: {}".format(len(bodies)))
    for p in sorted(paths):
        print("  {:>9,} bytes  {}".format(nbytes(paths[p]), os.path.basename(p)))
    print("cited by version 4 but not in the packet: {}".format(len(missing)))
    print("material carried: {:,} characters".format(nchar))
    print("Gemini material sha256:  {}".format(gs))
    print("ChatGPT material sha256: {}".format(cs))
    if gs != cs:
        problems.append("the two packets do not carry the same material")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print("OK: every record matches its source, character for character, in both packets; "
          "every ChatGPT file is within {:,} bytes".format(LIMIT))


if __name__ == "__main__":
    main()
