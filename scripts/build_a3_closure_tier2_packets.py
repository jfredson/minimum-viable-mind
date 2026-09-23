#!/usr/bin/env python3
"""Build the two tier 2 review packets for the Amendment A3 closure text.

Both packets carry the same records, in the same order, byte for byte. The
Gemini packet is one document. The ChatGPT packet is the same material split
into numbered files small enough that the app takes each one as pasted text
rather than converting it into an attachment it only searches.

    python3 scripts/build_a3_closure_tier2_packets.py          # build and check
    python3 scripts/build_a3_closure_tier2_packets.py --verify # check only

Re-run it after any source record changes; the packets are generated, never
hand-edited.

--verify reads the packet files as they are committed and compares them with a
build made from today's sources, so a source record that changed after the
packets were last built is reported as stale, by file name. It used to compare a
fresh build against itself, which could only ever agree, and so reported a clean
run over packets that were out of date; that is what this mode exists to catch.
"""

import bisect
import hashlib
import os
import re
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
E = "experiments/06-mvm-0a-constructed-self-index/"
OUT = E + "reviews/packets/"
PACKET = E + "reviews/2026-09-21-a3-closure-tier2-packet.md"

STAMP = "2026-09-21-a3-closure-tier2"

LEDGER_EXCERPT_1 = (
    '*Excerpt 1 of 4 — the review of the fitted linear read (2026-09-20). '
    'The section as the ledger has it, then the one row the closure text cites, '
    'the deferred marker-word read. Rows RT-70 to RT-88 and RT-90 to RT-93 are '
    'not reproduced.*')

LEDGER_EXCERPT_2 = (
    '*Excerpt 2 of 4 — the review of the step 4 proposal (2026-09-20). The '
    'section as the ledger has it, then the two rows the closure text cites: '
    'causal patching as new code, and the count of registered discriminators '
    'that have fired. The other rows of that review are not reproduced.*')

LEDGER_EXCERPT_3 = (
    '*Excerpt 3 of 4 \u2014 the review of the two follow-up localization runs '
    '(2026-09-21), reproduced whole. This is the range the closure text cites as '
    '"ledger RT-120 to RT-142".*')

LEDGER_EXCERPT_4 = (
    '*Excerpt 4 of 4 \u2014 the tier 1 review of this closure text (2026-09-21), '
    'reproduced whole. This is the range the closure text preamble cites as '
    '"ledger RT-143 to RT-171".*')


def read(path):
    with open(os.path.join(ROOT, path), "r", encoding="utf-8") as fh:
        return fh.read()


def lines_of(path):
    return read(path).rstrip("\n").split("\n")


def section(path, start_after, end_before=None):
    """The text between two headings, found by the headings themselves.

    Line numbers would break the moment anybody added a line to the top of the
    source file, and one of these sources is a document people still annotate.
    Both anchors must appear exactly once.
    """
    L = lines_of(path)
    def find(anchor):
        hits = [i for i, line in enumerate(L) if line == anchor]
        if len(hits) != 1:
            raise ValueError("anchor {!r} appears {} times in {}".format(
                anchor, len(hits), path))
        return hits[0]
    a = find(start_after) + 1
    b = find(end_before) if end_before else len(L)
    out = L[a:b]
    while out and out[0].strip() == "":
        out.pop(0)
    while out and (out[-1].strip() == "" or out[-1].strip() == "---"):
        out.pop()
    return "\n".join(out)


def commas(n):
    return "{:,}".format(n)


# ---------------------------------------------------------------------------
# The records. The order here is the order in both packets.
#   whole   - a complete file, reproduced unedited
#   excerpt - part of a file, with the source named and the omission stated
# `parts` splits a record for the ChatGPT packet only; the parts concatenate
# back into the record exactly.
# An excerpt also declares how the check tells the lines it reproduces from the
# packet's own words: `first_line` is the first line it reproduces, so everything
# above that line is the paragraphs introducing the excerpt; `editorial` lists
# the labels the packet writes in among the reproduced lines, such as the row of
# ellipses saying which rows are left out; and `quoted_with` is the prefix the
# packet adds where it reproduces its source as a block quote. Every other
# non-blank line has to be in the source file, character for character.
# ---------------------------------------------------------------------------

RECORDS = [
    dict(key="closure-rule", kind="excerpt",
         title="the closure rule this text is being reviewed under",
         source="docs/outside-review-protocol.md",
         text_from=(PACKET,
                    "## Block 1, part 2 — the closure rule this text is being reviewed under",
                    "## Block 1, part 3 — the brief (fixed text, sent unchanged to each reviewer)"),
         first_line="> Before a registration commit at Gate A:",
         quoted_with="> ",
         note=("excerpted from `%s` (%s characters in full), which also sets out the "
               "three review gates, the two tiers and the measurement rehearsal. Only "
               "the closure rule is reproduced, because it is the only part of that "
               "file the text under review cites.")),
    dict(key="brief", kind="protocol",
         title="the brief - fixed protocol text, sent unchanged to every reviewer",
         source=PACKET,
         text_from=(PACKET,
                    "## Block 1, part 3 — the brief (fixed text, sent unchanged to each reviewer)",
                    "## Block 19 — Appendix A: the red team ledger, excerpted"),
         note=("the four-part brief as it goes to every reviewer. Its wording is fixed by "
               "`docs/outside-review-protocol.md` and it is carried here from the packet "
               "file that already held it, unchanged. It is not rewritten for either "
               "reviewer, and not rewritten between passes.")),
    dict(key="closure-text", kind="whole",
         title="THE TEXT UNDER REVIEW - the Amendment A3 closure text, version 4",
         source="docs/a3-closure-text-draft-2026-09-21-v4.md"),
    dict(key="tier1", kind="whole",
         title="the inside reviewer's findings on the previous version of that text",
         source=E + "reviews/2026-09-21-a3-closure-claude-worktree.md",
         parts=[("its opening and part 1, feasibility", None),
                ("its part 2, satisfied by the wrong thing",
                 "# Part 2 — Satisfied by the wrong thing"),
                ("its parts 3 and 4, no verdict and over-reading, and its kill case",
                 "# Part 3 — No verdict")]),
    dict(key="amendment", kind="whole",
         title="the registered amendment this block will be appended to",
         source=E + "amendment-a3.md",
         parts=[("its opening, its glossary and its section 1", None),
                ("its sections 2 and 3, the design and the lesion protocol",
                 "## 2. The design: an objective where self-indexing is load-bearing"),
                ("its sections 4 to 7, and the registration revisions of 2026-09-15",
                 "## 4. Budget, gates, and kill criteria")]),
    dict(key="pre-registration", kind="whole",
         title="the registration the amendment belongs to, including the loss conditions",
         source=E + "pre-registration.md",
         parts=[("from its opening through the task batteries and the procedure", None),
                ("from the pre-registered metric and decision rule to the end, including "
                 "the loss conditions, the adjudicated decisions and amendments A1 and A2",
                 "## Pre-registered metric and decision rule")]),
    dict(key="seeds", kind="whole",
         title="the three-seed endpoint scores",
         source=E + "seeds-endpoint-findings.md"),
    dict(key="ceiling", kind="whole",
         title="the ownership-blind ceiling measured at 1.0",
         source=E + "ceiling-measurement-findings.md"),
    dict(key="ceiling-defect", kind="whole",
         title="the registered defect in that ceiling",
         source=E + "ceiling-defect-2026-09-17.md"),
    dict(key="pilot", kind="whole",
         title="the control-learnability pilot reading of 0.3125",
         source=E + "control-learnability-pilot-findings.md"),
    dict(key="fitted", kind="whole",
         title="the fitted eleven-position sweep",
         source=E + "fitted-position-sweep-findings.md"),
    dict(key="fitted-correction", kind="whole",
         title="the correction note carrying the one-legible-episode-in-eleven figure",
         source=E + "fitted-position-sweep-findings-CORRECTION-2026-09-20.md"),
    dict(key="refit", kind="whole",
         title="the standardised refit of that read",
         source=E + "standardised-refit-findings.md"),
    dict(key="other-index", kind="whole",
         title="the other-agent control's probe half",
         source=E + "other-index-position-sweep-findings.md"),
    dict(key="powered", kind="whole",
         title="the difference-of-averages read of the marker word",
         source=E + "powered-position-sweep-findings.md"),
    dict(key="ruling-centre", kind="whole",
         title="the ruling that a load-bearing self-index is a centre",
         source="docs/rulings/2026-09-20-center-as-degree.md"),
    dict(key="ruling-roadmap", kind="whole",
         title="the ruling carrying the successor experiment's plan",
         source="docs/rulings/2026-09-20-december-result-roadmap.md"),
    dict(key="ruling-blind", kind="whole",
         title="the ruling reconciling the blind arm",
         source="docs/rulings/2026-09-21-followup-runs-and-blind-arm.md"),
    dict(key="successor", kind="whole",
         title="the successor experiment's design note",
         source="docs/competing-mechanisms-2026-09-20.md"),
    dict(key="ledger", kind="excerpt",
         title="the red team ledger - every row and range the text under review cites",
         source=E + "red_team_ledger.md",
         text_from=(PACKET,
                    "## Block 19 — Appendix A: the red team ledger, excerpted",
                    "## Block 20 — Appendix B: the independent review of the Amendment A4 clause, excerpted"),
         first_line=("# Gate B review of the fitted linear read (2026-09-20) — rulings on "
                     "RT-70 to RT-93 (filed as RT-52 to RT-75 in the review file)"),
         editorial=[LEDGER_EXCERPT_1, LEDGER_EXCERPT_2,
                    LEDGER_EXCERPT_3, LEDGER_EXCERPT_4],
         note=("excerpted from `%s` (%s characters in full), which records every "
               "adversarial pass the program has run since 2026-08-04 and the ruling on "
               "every finding. Reproduced here: two review sections whole and three "
               "individual rows from two others - that is, every row and every range the "
               "text under review cites. The rows in between, and the four earlier "
               "reviews, are left out. Nothing is edited, softened or reordered."),
         parts=[("the reviews of the fitted linear read and of the step 4 proposal", None),
                ("the review of the two follow-up localization runs, reproduced whole",
                 LEDGER_EXCERPT_3),
                ("the inside review of this closure text, reproduced whole",
                 LEDGER_EXCERPT_4)]),
    dict(key="a4-review", kind="excerpt",
         title="the independent review of a later draft clause - the finding the text cites",
         source=E + "red-team-a4.md",
         text_from=(PACKET,
                    "## Block 20 — Appendix B: the independent review of the Amendment A4 clause, excerpted",
                    "## Block 21 — Appendix C: the compute ledger, excerpted"),
         first_line=("# Red-team pass on the Amendment A4 clause — §5 of the "
                     "control-clause proposal, read as registerable text"),
         editorial=["*The summary-table row for this finding, as that review's summary has it:*",
                    "*The finding in full:*"],
         note=("excerpted from `%s` (%s characters in full), twenty-two findings from a "
               "separate isolated session on 2026-09-19 on a later draft clause. "
               "Reproduced here: that review's front matter, its summary row for the one "
               "finding the text under review cites (its seventeenth, labelled F17 there) "
               "and that finding in full. The other twenty-one findings are left out.")),
    dict(key="compute-ledger", kind="excerpt",
         title=("the compute ledger - its rules, its baseline, the rows the text cites "
                "and the rows that correct them"),
         source=E + "compute-ledger.md",
         text_from=(PACKET,
                    "## Block 21 — Appendix C: the compute ledger, excerpted"),
         first_line="# MVM-0a compute ledger",
         editorial=["| … | … | *(the rows dated 2026-08-07 to 2026-09-18 are not "
                    "reproduced in this excerpt)* | … | … | … | … | … |"],
         note=("excerpted from `%s` (%s characters in full), which carries a row for every "
               "rented-machine session since 2026-08-07. Reproduced here: the ledger's "
               "opening, its rules, its reconciliation baseline, its column headings, five "
               "rows in full and one dated note. The five rows are the two dated 2026-09-19 "
               "and 2026-09-20 that the text under review cites for its money figures, the "
               "two follow-up runs of 2026-09-20 that carry the $1.90 those figures are "
               "stale by, and the measurement rehearsal of 2026-09-21, whose running-total "
               "column is where the ledger states the corrected figures. The dated note is "
               "the ledger's launch-outcome note of 2026-09-20 on those two follow-up runs. "
               "The other rows are left out, so the cited rows and the correcting rows can "
               "both be checked but the running total cannot be re-added from the "
               "beginning."),
         parts=[("its framing, the ledger's opening, its rules, its reconciliation "
                 "baseline and the first of the two rows the text under review cites",
                 None),
                ("the second row the text cites, and the two follow-up runs of "
                 "2026-09-20 that carry the $1.90 correcting it",
                 "| 2026-09-20 | checkpoint recovery (UNREGISTERED) |"),
                ("the measurement rehearsal of 2026-09-21, whose running total states "
                 "the corrected figures, and the ledger's dated note on the two "
                 "follow-up runs",
                 "| 2026-09-21 | measurement rehearsal ")]),
    dict(key="separation-clause", kind="whole",
         title=("OPTIONAL BACKGROUND, not cited by the text under review - what the "
                "separation clause requires"),
         source=E + "separation-clause-requirements.md",
         note=("the text under review does not cite this file. It is here because the red "
               "team ledger excerpt refers to it, and because the packet would rather hand "
               "a record over than have a reviewer guess at one. Nothing in the review "
               "depends on it.")),
]

# ---------------------------------------------------------------------------
# Which records go in which ChatGPT file: (record key, part index or None).
# ---------------------------------------------------------------------------

CHATGPT_FILES = [
    ("01-start-here-and-the-brief", "Start here: what this is, and the brief",
     [("closure-rule", None), ("brief", None)]),
    ("02-the-text-under-review", "The text under review",
     [("closure-text", None)]),
    ("03-inside-findings-part1", "The inside reviewer's findings, part 1 of 3",
     [("tier1", 0)]),
    ("04-inside-findings-part2", "The inside reviewer's findings, part 2 of 3",
     [("tier1", 1)]),
    ("05-inside-findings-part3", "The inside reviewer's findings, part 3 of 3",
     [("tier1", 2)]),
    ("06-registered-amendment-part1", "The registered amendment, part 1 of 3",
     [("amendment", 0)]),
    ("07-registered-amendment-part2", "The registered amendment, part 2 of 3",
     [("amendment", 1)]),
    ("08-registered-amendment-part3", "The registered amendment, part 3 of 3",
     [("amendment", 2)]),
    ("09-registration-part1", "The registration, part 1 of 2",
     [("pre-registration", 0)]),
    ("10-registration-part2", "The registration, part 2 of 2",
     [("pre-registration", 1)]),
    ("11-measurement-records", "The four measurement records behind the outcome",
     [("seeds", None), ("ceiling", None), ("ceiling-defect", None), ("pilot", None)]),
    ("12-localization-fitted-sweep",
     "The localization records, 1 of 3: the fitted sweep and its correction",
     [("fitted", None), ("fitted-correction", None)]),
    ("13-localization-refit",
     "The localization records, 2 of 3: the standardised refit",
     [("refit", None)]),
    ("14-localization-controls",
     "The localization records, 3 of 3: the other-agent control and the marker-word read",
     [("other-index", None), ("powered", None)]),
    ("15-rulings-and-successor",
     "The three rulings the text cites, and the successor experiment's design note",
     [("ruling-centre", None), ("ruling-roadmap", None), ("ruling-blind", None),
      ("successor", None)]),
    ("16-ledger-part1", "The red team ledger, part 1 of 3", [("ledger", 0)]),
    ("17-ledger-part2", "The red team ledger, part 2 of 3", [("ledger", 1)]),
    ("18-ledger-part3", "The red team ledger, part 3 of 3", [("ledger", 2)]),
    ("19-a4-review-and-compute-ledger-part1",
     "The A4 review finding, and the compute ledger, part 1 of 3",
     [("a4-review", None), ("compute-ledger", 0)]),
    ("20-compute-ledger-part2", "The compute ledger, part 2 of 3",
     [("compute-ledger", 1)]),
    ("21-compute-ledger-part3", "The compute ledger, part 3 of 3",
     [("compute-ledger", 2)]),
    ("22-optional-background", "Optional background, and the end of the packet",
     [("separation-clause", None)]),
]

# ---------------------------------------------------------------------------
# Prose. Everything in STANDING_START and the record list is identical in both
# packets; only the delivery note differs, because the delivery differs.
# ---------------------------------------------------------------------------

KIND_LABEL = {"whole": "COMPLETE FILE",
              "excerpt": "EXCERPT",
              "protocol": "PROTOCOL TEXT, CARRIED UNCHANGED, from"}
KIND_COLUMN = {"whole": "complete",
               "excerpt": "excerpt",
               "protocol": "complete, and fixed by the protocol"}

TITLE = "Review packet - the closure text of Amendment A3 (Minimum Viable Mind)"

STANDING_START = """\
## What you are looking at, from a standing start

You are reviewing one short document - about 2,300 words - before it is
committed to a record that cannot afterwards be edited. With it you have been
given every record that document cites: whole where the file was short enough
to reproduce, and as a marked excerpt where it was not.

**The program.** Minimum Viable Mind is a small independent research program,
run by one person on a budget of a few hundred dollars. It asks whether a
machine can be built so that a model of itself is load-bearing: so that the
system cannot do its task well without using a signal telling it which of the
things in front of it are its own. The way it asks is to train small language
models - about 30 million parameters, small enough to train from scratch for a
few dollars - on tasks built for the question rather than borrowed, and to
write down in advance what would count as a result and what would count as a
failure. That written-in-advance document is called a *registration* here.
Once committed, a registration is never edited; a change to it is a numbered
amendment, also committed before anything runs. It is the discipline a
clinical trial uses when it registers its endpoints before it enrols anyone,
and for the same reason: it stops the question being quietly replaced by the
one the data happened to answer.

**Amendment A3** is the registered amendment whose experiment is being closed
here. Under it, four agents take turns revising a shared piece of text, and the
model is given an *ownership* input: a signal saying which of the four agents'
revisions are its own. Three sets of tasks are scored - a primary set the
design intends to be impossible to do well without using that signal, a syntax
set that should not need it, and a state set that needs memory of what has
happened but not ownership. The registered test was a comparison, not a single
number: the ownership input is zeroed, and what would have counted is not that
performance falls, but that it falls on the primary set and not on a matched
control set built to demand everything the primary set demands *except*
ownership. That matched control is the part that could not be built, and that
is what the document you are reviewing is about.

**A closure text** is the block appended to a registration to say how the
experiment ended: which registered condition fired, what was measured, what was
never run, and what the result may and may not be read as claiming. It is the
last thing a registration receives. Once appended it is registered text, and
the program's own rules forbid editing it afterwards. That is why this review
happens now, before it is appended, and not after.

**"Not testable" is a registered outcome here, not a shrug.** Before anything
ran, the registration named the conditions under which the experiment would
have to be abandoned rather than reported. One of them says that if no control
condition can be built that is free of ownership and still demanding at its
own ceiling, then the comparison at the heart of the design is dead and the
honest report is "not testable". The document says that condition fired, and
says why: the control set's ownership-blind ceiling was measured at 1.0, which
leaves the registered metric dividing by zero - the arithmetic saying,
correctly, that there is nothing left to measure. Awkwardly, the same phrase
"not testable" is also the name of a different registered bin, for a lesion
that damages the model so broadly that no reading of it can be trusted. The
document distinguishes the two; whether it does so clearly enough is fair game
for you.

**Why you and not somebody inside the program.** Review here runs in two
tiers. The inside tier is a fresh session of the same model family that wrote
the text, cut off from the conversation that produced it, given the repository
and able to run code - which is why its findings can report a command and the
output it gave. You are the outside tier: at least two models from other labs,
shown documents rather than a running checkout, so every finding you make is an
argued one rather than a measured one. Two outside reviewers are used because
the disagreement between them is the signal. Do not assume the other reviewer
was shown something you were not; you have both been given the same material.

**What has already been done to this text.** An inside reviewer read the
previous version against the registration and found six fatal problems and many
smaller ones. Every finding was ruled on and the text was rewritten. You are
reading the rewrite, and you have that reviewer's findings in full. You may
agree with them, disagree with them, or find that answering one of them created
a new problem.

**What happens to what you write.** It is filed in the repository word for
word, never edited, with your model, your version as the app reports it, the
date and the mode at the top. Each finding is ruled on one at a time: accepted,
accepted with a change, declined with the reason on the record, or carried as
an open item. A ruling to keep the text over your objection is a valid outcome
and goes on the record with its reason. Nothing is appended to the registration
until both outside responses are filed, every item is ruled on, and the closure
rule below is satisfied.

**How to report something you were not given.** When you cannot check a claim,
say which of two things is true: the record was not shown to you, or the record
was shown to you and does not contain what the sentence says. The second is a
finding about the text. The first is a defect in this packet - worth reporting,
but not a mark against the document. Name the file either way.

**A note on the excerpts.** Three files were too long to reproduce whole. Each
appears below as an excerpt that names its source file, gives that file's full
length, and states what was left out; the part reproduced is the part the
citation points at, quoted unedited. If an excerpt has been cut in a way that
flatters the text under review, say so - that is a finding about this packet,
and it is worth having.

**How the material is marked.** Every record below opens with a line beginning
`===== RECORD` that names it, says whether it is a complete file or an excerpt,
and gives its path in the repository, and closes with a line beginning
`===== END OF RECORD`. Cite records by that path.
"""

RECORD_LIST_HEADING = """\
## The records you have, in the order they appear

Every record in this table is in this packet. "Complete" means the whole file,
reproduced unedited. "Excerpt" means part of a file, with the source named, the
full length given and the omission stated where the excerpt appears.
"""

GEMINI_DELIVERY = """\
*This is the whole packet in one document: the closure rule, the brief, the
text under review, the inside reviewer's findings, the registered text it must
be read against, and every record the text cites. Read it from start to finish
before answering - do not search it for passages that match the questions.
Then answer the brief, which is the second record below. Label your findings
G1, G2, G3 and so on.*
"""

CHATGPT_DELIVERY = """\
*This packet arrives as {n} files pasted into this one conversation, in order.
This is file 1. Do not begin your review until file {n} has arrived: reply to
each file with one short line saying you have it, and nothing else. Give your
full answer only after the last file. Read each file as text, start to finish,
rather than searching it. The brief you are answering is in this file, below.
Label your findings A1, A2, A3 and so on.*

*If a file arrives cut short, or the app turns one into an attachment you can
only search rather than read, say so at once and name the file, before going
on.*
"""

CHATGPT_MIDFILE = (
    "*This is file {i} of {n} of one review packet, pasted into a single "
    "conversation. It contains {what}. Reply with one short line saying you "
    "have it, and wait for the rest: the brief you are answering is in file 1, "
    "and your review comes only after file {n} arrives. If this file looks cut "
    "short, say so now.*")

CHATGPT_LASTFILE = (
    "*This is file {i} of {n}, the last one, of a review packet pasted into a "
    "single conversation. It contains {what}. You now have the whole packet: "
    "the orientation, the closure rule and the brief in file 1, the text under "
    "review in file 2, the inside reviewer's findings in files 3 to 5, the "
    "registered text in files 6 to 10, and the records the text cites in files "
    "11 to {last_cited}. Answer the brief from file 1 now, in its four parts, labelling "
    "your findings A1, A2, A3 and so on. If any file was missing or cut short, "
    "name it at the top of your answer.*")


def wrap(text):
    return textwrap.fill(" ".join(text.split()), width=78)


def record_text(rec):
    if "text_from" in rec:
        return section(*rec["text_from"])
    return read(rec["source"]).rstrip("\n")


def split_point(text, marker, key):
    """Where in the record the line the marker names begins.

    The marker is a whole line, or the start of one. The second form is there
    for the compute ledger, whose rows are single lines thousands of characters
    long: writing one out here to split on would be unreadable and would break
    the moment anybody added a word to the row. Either way the marker must
    match exactly one line, so a split never lands somewhere unintended, and
    the line it names is never the record's first line.
    """
    lines = text.split("\n")
    hits = [i for i, line in enumerate(lines) if line == marker]
    if not hits:
        hits = [i for i, line in enumerate(lines) if line.startswith(marker)]
    if len(hits) != 1:
        raise ValueError("split marker {!r} matches {} lines in record {}".format(
            marker, len(hits), key))
    if hits[0] == 0:
        raise ValueError("split marker {!r} is the first line of record {}".format(
            marker, key))
    return sum(len(line) + 1 for line in lines[:hits[0]])


def record_parts(rec):
    """List of (label, text); one entry when the record is not split.

    A record is split at a heading it already has, so the parts concatenate
    back into the record with nothing added and nothing lost.
    """
    if "parts" not in rec:
        return [(None, record_text(rec))]
    text = record_text(rec)
    cuts = []
    for label, marker in rec["parts"]:
        if marker is None:
            cuts.append((label, 0))
            continue
        cuts.append((label, split_point(text, marker, rec["key"])))
    out = []
    for i, (label, start) in enumerate(cuts):
        end = cuts[i + 1][1] - 1 if i + 1 < len(cuts) else len(text)
        out.append((label, text[start:end]))
    assert "\n".join(t for _l, t in out) == text, "the parts do not rejoin into the record"
    return out


def source_note(rec, full_len):
    note = rec.get("note")
    if note is None:
        return None
    if "%s" in note:
        return note % (rec["source"], commas(full_len))
    return note


def build():
    total = len(RECORDS)
    by_key = {r["key"]: r for r in RECORDS}
    full_len = {}
    for r in RECORDS:
        try:
            full_len[r["key"]] = len(read(r["source"]))
        except (IOError, OSError):
            full_len[r["key"]] = 0

    rows = ["| # | record | complete or excerpt | source file |", "|---|---|---|---|"]
    for i, r in enumerate(RECORDS, 1):
        rows.append("| {} | {} | {} | `{}` |".format(
            i, r["title"], KIND_COLUMN[r["kind"]], r["source"]))
    record_list = RECORD_LIST_HEADING + "\n" + "\n".join(rows) + "\n"

    holder = {}
    for fi, (_stem, _t, items) in enumerate(CHATGPT_FILES, 1):
        for key, part in items:
            holder[(key, part)] = fi

    def render(r, n, part_index=None, for_chatgpt=False):
        """One record, or one part of one.

        In the Gemini packet (part_index None) a record is written whole, with
        no seams, however many parts the ChatGPT packet cuts it into.
        """
        parts = record_parts(r)
        note = source_note(r, full_len[r["key"]])
        multi = len(parts) > 1 and part_index is not None
        if part_index is None:
            chosen = [(0, (None, "\n".join(text for _label, text in parts)))]
        else:
            chosen = [(part_index, parts[part_index])]
        chunks = []
        for pi, (label, text) in chosen:
            head = "===== RECORD {} of {}".format(n, total)
            if multi:
                head += ", part {} of {}".format(pi + 1, len(parts))
            head += " - {} - {}: {} =====".format(
                r["title"], KIND_LABEL[r["kind"]], r["source"])
            block = [head, ""]
            if note and (pi == 0 or for_chatgpt):
                block += [wrap("*Source note: {}*".format(note)), ""]
            if multi:
                line = "*This part is {}.".format(label)
                if for_chatgpt:
                    others = sorted(holder[(r["key"], j)] for j in range(len(parts)) if j != pi)
                    line += " The other parts of this record are in {}.".format(
                        " and ".join("file {:02d}".format(x) for x in others))
                block += [wrap(line + "*"), ""]
            block += [text, "", "===== END OF RECORD {}{} =====".format(
                n, ", part {}".format(pi + 1) if multi else "")]
            chunks.append("\n".join(block))
        return "\n\n".join(chunks)

    outputs = {}

    doc = ["# " + TITLE, "",
           "*Prepared under `docs/outside-review-protocol.md`: Gate A, tier 2, the "
           "outside pass. Everything after the brief is a record from the repository, "
           "reproduced unedited.*", "",
           GEMINI_DELIVERY, "", STANDING_START, "", record_list, "", "---", ""]
    for i, r in enumerate(RECORDS, 1):
        doc += [render(r, i), ""]
    doc.append("===== END OF PACKET =====")
    outputs[OUT + STAMP + "-gemini.md"] = "\n".join(doc).rstrip("\n") + "\n"

    n_files = len(CHATGPT_FILES)
    for fi, (stem, title, items) in enumerate(CHATGPT_FILES, 1):
        what = "; ".join(
            by_key[k]["title"] + ("" if p is None else " (part {} of {})".format(
                p + 1, len(by_key[k]["parts"]))) for k, p in items)
        body = ["# " + TITLE + " - file {} of {}: {}".format(fi, n_files, title), ""]
        if fi == 1:
            body += [CHATGPT_DELIVERY.format(n=n_files), "", STANDING_START, "",
                     record_list, "", "---", ""]
        elif fi == n_files:
            body += [wrap(CHATGPT_LASTFILE.format(i=fi, n=n_files, what=what,
                                                 last_cited=n_files - 1)),
                     "", "---", ""]
        else:
            body += [wrap(CHATGPT_MIDFILE.format(i=fi, n=n_files, what=what)),
                     "", "---", ""]
        for key, part in items:
            r = by_key[key]
            body += [render(r, RECORDS.index(r) + 1, part_index=part, for_chatgpt=True), ""]
        if fi == n_files:
            body.append("===== END OF PACKET =====")
        outputs[OUT + STAMP + "-chatgpt-" + stem + ".md"] = "\n".join(body).rstrip("\n") + "\n"

    outputs[OUT + STAMP + "-INDEX-how-to-run-these-sessions.md"] = build_index(outputs)
    return outputs


INDEX_HEAD = """\
# How to run the two outside-review sessions on the Amendment A3 closure text

*Written for John, 2026-09-21 (Pacific). Gate A, tier 2, under
`docs/outside-review-protocol.md`. Everything here was generated by
`scripts/build_a3_closure_tier2_packets.py` from the committed records; the
packets are never hand-edited. Re-running that script rebuilds them and
re-checks them.*

## The short version

Two sessions, one for each outside reviewer, run by you in their apps. Both
reviewers get exactly the same material - the closure text, the inside
reviewer's findings, the registered text, and every record the closure text
cites. Only the delivery differs, because the two apps behave differently:

- **Gemini** gets one document, {gem_kb} KB.
- **ChatGPT** gets the same material as {n} files, none of them bigger than
  {max_kb} KB, pasted into **one** conversation in order.

That is the whole difference. The material in the two packets was compared
character by character after they were built, and it is the same: {chars}
characters of records in each, in the same order, with the same fingerprint
(a sha256 checksum, the standard way of showing two files are identical to
the byte):

    {digest}

Each of the {records} records was also checked one at a time, in the way it was
made. The {whole_n} that reproduce a whole file were compared with that file,
character for character. The {excerpt_n} that are excerpts are put together by
hand in the packet, so every line each one reproduces had to be found in the
file it names, character for character and in that file's own order; the
paragraphs the packet writes around an excerpt to introduce it are its own words
and are compared with nothing. The one remaining record is the brief, which is
protocol text carried over unchanged from the earlier packet, and whose amended
sentence is the one checked word for word against the protocol above. So neither
packet has quietly lost or reworded anything a reviewer will read as quoted.

## Session 1 - Gemini, one document

1. New chat. Give it `{gem}`
   whole: paste it if the app takes the paste, attach the file if it does not.
2. The document tells it what to do, including to read start to finish rather
   than search, and to label its findings G1, G2, G3 and so on. You should not
   need to add anything.
3. When it answers, check the answer refers to records by file name. If it says
   it only saw parts of the document, or its answer never touches the registered
   text, stop and hand it the {n} ChatGPT files instead, in the same one
   conversation, in order - they carry the identical material.

## Session 2 - ChatGPT, one conversation, {n} pastes

**This is one session, not {n} sessions.** A reviewer who sees a third of the
record in each of three chats has reviewed nothing, and the two-reviewer
comparison is ruined without anybody noticing.

1. New chat.
2. **Paste the contents** of file 01, then 02, and so on in order, one message
   each. Do not attach the files. The whole point of the split is that an
   attachment may be searched rather than read, and a pasted block of this size
   is read.
3. Each file tells it to reply with one short line and wait. After file {n} it
   gives the review. If it starts reviewing early, tell it to wait for the rest.
4. Files are numbered in their names, so pasting them in filename order is the
   right order.
5. The last file holds background the closure text does not cite - it is there
   so that nothing a reviewer might reach for is missing - and it also carries
   the instruction to begin the review. Paste it even if you would rather skip
   the background.

## If the app still balks

- **A paste is turned into an attachment anyway.** Undo it, split that one file
  in half at a line beginning `===== RECORD`, and paste the halves as two
  messages, saying "part 1 of 2 of file N" in front of each. Never split inside
  a record: those marker lines are where the seams are.
- **A file comes back cut short.** It is asked to tell you. Paste that file
  again, and if it is cut short twice, split it as above.
- **The conversation gets to its length limit before file {n}.** Do not start a
  second chat and carry on there. Stop, write down which file you reached, and
  say so - a review of part of the record is worse than no review, because it
  reads as disagreement with the other reviewer when it is really a difference
  in what each was shown.
- **It asks for the files as uploads.** Decline and keep pasting.

## File each response before you start the next session

Paste each reviewer's answer, word for word, into
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-<model>.md`,
with the model, its version as the app reports it, the date and the mode
(documents shown, lookup allowed) at the top. Do that **before** the second
session starts, and never edit it afterwards. That is what the Belt Equation
review did, and it is why nothing from those sessions got lost or quietly
paraphrased.

Do not show either reviewer what the other said. The disagreement between them
is the thing being bought.

## What it costs you, and what happens next

Two sessions. One paste for Gemini; {n} pastes plus the answer for ChatGPT.

After both answers are filed: the findings get labels (G1... from Gemini,
A1... from ChatGPT), you rule on every one of them, and the fatal ones get a
closure line in the red team ledger with a check run by somebody other than
whoever wrote the fix. The closure block is appended to the registered
amendment only once that is done - as soon as it is done, not on any date.

## The files
"""

INDEX_TAIL = """
## What was built from what

{built_from}

## If the closure text changes before you run the sessions

Run `python3 scripts/build_a3_closure_tier2_packets.py` from the top of the
repository. It rebuilds both packets from the committed files and prints the
check that they still carry identical material. Only the files that changed
need re-pasting; the closure text lives in exactly one place in each packet.
"""

BUILT_FROM = """\
- The closure text under review is version 4 as of commit `a4c754e` on branch
  `worktree-agent-a5b280b93c1ba5e41` (the trim, the citation of the rehearsal
  rule, and the correction that states the uncarvable signature's second
  condition the way it was registered).
- The record list and the excerpts come from the rebuilt tier 2 packet, commit
  `184a42f` on branch `worktree-agent-a1a9e113c8f410ce2`, which is the pass that
  established that every record the closure text cites has to be in the packet.
- The brief and the closure rule are the protocol as amended, from `main` at
  commit `dd1b974`, which includes the amendment that struck the word
  "unlikely".
- The earlier closure-text trim, commit `628686f` on branch
  `worktree-agent-a53dc49a926581fe8`, is an ancestor of the commit above and is
  carried through it.
- Rebuilt 2026-09-22 after the correction that moves the programme spend to
  about $227.60 of $400. Two things changed in the material: the closure text
  now carries a dated note beside its money paragraph saying the programme
  figure it states is stale by $1.90, and the compute-ledger excerpt now
  reproduces the rows that carry that $1.90 and the ledger's own note on them,
  so a reviewer can check the corrected figures against the record rather than
  taking them on trust. The rebuild also picked up source records that had
  grown since the packets were last frozen, which is why more files than those
  two changed."""


def build_index(outputs):
    gem = [p for p in outputs if p.endswith("-gemini.md")][0]
    cgs = sorted(p for p in outputs if "-chatgpt-" in p)
    def kb(p):
        return len(outputs[p].encode()) / 1024.0

    material = "\n".join(v for _k, v in sorted(extract(outputs[gem]).items()))
    head = INDEX_HEAD.format(
        n=len(cgs), gem=os.path.basename(gem),
        gem_kb=int(round(kb(gem))), max_kb=int(round(max(kb(p) for p in cgs))),
        chars=commas(len(material)), records=len(RECORDS),
        whole_n=sum(1 for r in RECORDS if r["kind"] == "whole"),
        excerpt_n=sum(1 for r in RECORDS if r["kind"] == "excerpt"),
        digest=hashlib.sha256(material.encode()).hexdigest())
    rows = ["| order | file | size | what is in it |", "|---|---|---|---|",
            "| Gemini session | `{}` | {:.0f} KB | the whole packet in one document |".format(
                os.path.basename(gem), kb(gem))]
    by_key = {r["key"]: r for r in RECORDS}
    for fi, (stem, title, items) in enumerate(CHATGPT_FILES, 1):
        what = "; ".join(
            by_key[k]["title"] + ("" if p is None else " (part {} of {})".format(
                p + 1, len(by_key[k]["parts"]))) for k, p in items)
        path = [p for p in cgs if ("-chatgpt-" + stem + ".md") in p][0]
        rows.append("| ChatGPT {} of {} | `{}` | {:.1f} KB | {} |".format(
            fi, len(cgs), os.path.basename(path), kb(path), what))
    return head + "\n" + "\n".join(rows) + "\n" + INDEX_TAIL.format(built_from=BUILT_FROM)


def write(outputs):
    for path, text in sorted(outputs.items()):
        with open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
            fh.write(text)
    return sorted(outputs)


RECORD_RE = re.compile(r"^===== RECORD (\d+) of \d+(?:, part (\d+) of (\d+))? - ", re.M)
END_RE = re.compile(r"^===== END OF RECORD \d+(?:, part \d+)? =====$", re.M)


def extract(text):
    """Pull {(record number, part number): body} back out of a built file.

    The builder writes a fixed prefix - the marker line, a blank line, then at
    most one source note and one part note, each followed by a blank line - and
    one blank line before the closing marker. Exactly that much is removed, so
    a blank line that belongs to the record itself survives.
    """
    found = {}
    pos = 0
    while True:
        m = RECORD_RE.search(text, pos)
        if not m:
            return found
        start = text.index("\n", m.end()) + 1
        end = END_RE.search(text, start)
        lines = text[start:end.start()].split("\n")
        assert lines and lines[0] == "", "marker line is not followed by a blank line"
        lines.pop(0)
        for prefix in ("*Source note:", "*This part is"):
            if lines and lines[0].startswith(prefix):
                while lines and lines[0] != "":   # the note may be wrapped over
                    lines.pop(0)                  # several lines
                assert lines, "note is not followed by a blank line"
                lines.pop(0)
        for _ in range(2):  # the blank line before the closing marker, and the
            assert lines and lines[-1] == "", "record does not end with a blank line"
            lines.pop()     # empty string the final newline leaves behind
        key = (int(m.group(1)), int(m.group(2)) if m.group(2) else 1)
        found[key] = "\n".join(lines)
        pos = end.end()


AMENDED_SENTENCE = (
    "Do not soften findings to be polite, and do not manufacture severity to "
    "look thorough. A pass that finds nothing fatal is a valid result, reported "
    "as what was checked and what held.")


def flat(text):
    """One space for any run of whitespace, so line wrapping stops mattering."""
    return " ".join(text.split())


def unquoted(line, prefix):
    """The line as it has to read in the source file.

    One excerpt reproduces its source as a block quote, so the "> " the packet
    adds comes back off before comparing and nothing else is touched. A line
    that does not carry the prefix cannot have come from the source, and comes
    back as None so the check reports it rather than passing it.
    """
    if prefix is None:
        return line
    if line == prefix.rstrip():
        return ""
    if line.startswith(prefix):
        return line[len(prefix):]
    return None


def excerpt_against_source(rec, text):
    """One excerpt record against the file it names as its source.

    An excerpt is assembled by hand in the packet document, so reading its text
    back out of that document compares the hand copy with itself and a copied
    row that has since drifted from the ledger goes through clean. This opens
    the file the record names instead and requires every line the excerpt
    reproduces to be in it character for character, and those lines to run
    strictly forward through it, so nothing is reordered, repeated or reworded.

    What is not a reproduced line is declared on the record, not inferred from
    whether it happens to match: the paragraphs introducing the excerpt, which
    are everything above `first_line`, and the labels in `editorial`, which the
    packet writes in among the reproduced lines. A line that drifts therefore
    cannot excuse itself by failing to match. Blank lines are counted as
    neither, since a blank line reproduces nothing.

    Returns (reproduced lines, the packet's own lines, problems).
    """
    lines = text.split("\n")
    hits = [i for i, line in enumerate(lines) if line == rec["first_line"]]
    if len(hits) != 1:
        return 0, 0, ["the declared first reproduced line matches {} lines of the "
                      "record, so the excerpt cannot be told from its framing: {!r}"
                      .format(len(hits), rec["first_line"][:60])]
    editorial = list(rec.get("editorial", ()))
    body = lines[hits[0]:]
    problems = ["the declared packet label is no longer in the record: {!r}".format(
        label[:60]) for label in editorial if label not in lines]

    where = {}
    for i, line in enumerate(lines_of(rec["source"])):
        where.setdefault(line, []).append(i)

    at = -1
    reproduced = 0
    own = len([line for line in lines[:hits[0]] if line.strip() != ""])
    for n, line in enumerate(body, hits[0] + 1):
        if line.strip() == "":
            continue
        if line in editorial:
            own += 1
            continue
        want = unquoted(line, rec.get("quoted_with"))
        spots = where.get(want, []) if want is not None else []
        nxt = spots[bisect.bisect_right(spots, at):]
        if not nxt:
            problems.append("line {} of the record is {} in the source file: {!r}"
                            .format(n, "out of order" if spots else "nowhere",
                                    line[:70]))
        else:
            at = nxt[0]
            reproduced += 1
    return reproduced, own, problems


def excerpts(rec_texts):
    """Every excerpt record against the file it names, line by line."""
    print("")
    print("The excerpt records, against the file each one names. Their text is")
    print("assembled by hand in the packet document, so reading it back out of that")
    print("document would only compare the hand copy with itself:")
    ok = True
    for i, r in enumerate(RECORDS, 1):
        if r["kind"] != "excerpt":
            continue
        reproduced, own, problems = excerpt_against_source(r, rec_texts[i])
        ok = ok and not problems
        print("")
        print("{:<3} {}".format(i, r["title"]))
        if problems:
            print("     DOES NOT MATCH `{}`:".format(r["source"]))
            for p in problems:
                print("       " + p)
        else:
            print("     {} lines reproduced, every one of them in `{}`".format(
                reproduced, r["source"]))
            print("     character for character and in that file's own order; {} lines "
                  "the packet".format(own))
            print("     writes itself, which reproduce nothing and are not compared.")
    return ok


def verify(outputs):
    ok = True
    gem = [p for p in outputs if p.endswith("-gemini.md")][0]
    cgs = sorted(p for p in outputs if "-chatgpt-" in p)
    g_rec = extract(outputs[gem])
    c_rec = {}
    for p in cgs:
        for k, v in extract(outputs[p]).items():
            if k in c_rec:
                print("DUPLICATE record part {} in {}".format(k, p))
                ok = False
            c_rec[k] = v

    print("record blocks in the Gemini packet: {} (one per record), in the ChatGPT "
          "packet: {} (records, some in parts)".format(len(g_rec), len(c_rec)))
    if sorted(set(k[0] for k in g_rec)) != sorted(set(k[0] for k in c_rec)):
        print("MISMATCH in which records are present: {}".format(
            set(k[0] for k in g_rec) ^ set(k[0] for k in c_rec)))
        ok = False
    if len(set(k[0] for k in g_rec)) != len(RECORDS):
        print("MISMATCH: the Gemini packet does not carry every record once")
        ok = False
    print("")
    print("{:<3} {:<58} {:>9} {:>6}  {}".format("#", "record", "chars", "parts", "check"))
    in_packets = {}
    for i, r in enumerate(RECORDS, 1):
        want = record_text(r)
        g = "\n".join(v for k, v in sorted(g_rec.items()) if k[0] == i)
        c = "\n".join(v for k, v in sorted(c_rec.items()) if k[0] == i)
        in_packets[i] = g
        hw, hg, hc = (hashlib.sha256(x.encode()).hexdigest()[:10] for x in (want, g, c))
        good = hw == hg == hc
        ok = ok and good
        # An excerpt's text is taken from the packet document, not from the file
        # the record names, so this row cannot claim the source for one. The
        # excerpt block below is what compares those against their sources.
        print("{:<3} {:<58} {:>9} {:>6}  {}".format(
            i, r["title"][:58], commas(len(want)), len(record_parts(r)),
            ("identical in both, matches the packet document"
             if r["kind"] == "excerpt" else "identical in both, matches source") if good
            else "DIFFERS source {} gemini {} chatgpt {}".format(hw, hg, hc)))

    ok = excerpts(in_packets) and ok

    all_g = "\n".join(v for _k, v in sorted(g_rec.items()))
    all_c = "\n".join(v for _k, v in sorted(c_rec.items()))
    hg = hashlib.sha256(all_g.encode()).hexdigest()
    hc = hashlib.sha256(all_c.encode()).hexdigest()
    print("")
    print("all material, concatenated in order: {} characters".format(commas(len(all_g))))
    print("  Gemini  sha256 {}".format(hg))
    print("  ChatGPT sha256 {}".format(hc))
    print("  the two packets carry the same material: {}".format("YES" if hg == hc else "NO"))
    ok = ok and hg == hc

    in_proto = AMENDED_SENTENCE in flat(read("docs/outside-review-protocol.md"))
    in_packets = all(AMENDED_SENTENCE in flat(outputs[p]) for p in [gem, cgs[0]])
    ok = ok and in_proto and in_packets
    print("  the amended sentence of the brief is word for word the protocol's: {}"
          .format("YES" if in_proto else "NO"))
    print("  and appears in both packets: {}".format("YES" if in_packets else "NO"))
    return ok


def sizes(outputs):
    print("")
    print("{:<66} {:>9}".format("file", "bytes"))
    for p in sorted(outputs):
        print("{:<66} {:>9}".format(os.path.basename(p), commas(len(outputs[p].encode()))))


def on_disk(outputs):
    """The packet files as they are committed, plus what is missing or spare.

    Returns (files, missing, spare): the paths that were read and their text,
    the paths this script would write that are not there, and the files sitting
    in the output directory that this script does not write - which is what an
    older build leaves behind when a file is renamed.
    """
    files, missing = {}, []
    for path in sorted(outputs):
        try:
            files[path] = read(path)
        except (IOError, OSError):
            missing.append(path)
    folder = os.path.join(ROOT, OUT)
    present = set(os.listdir(folder)) if os.path.isdir(folder) else set()
    spare = sorted(present - set(os.path.basename(p) for p in outputs))
    return files, missing, spare


def against_disk(outputs):
    """Compare the committed packet files with a fresh build from the sources.

    This is the check that catches a stale packet: a source record that changed
    after the packets were last built makes the fresh build differ from what is
    committed, and that difference is reported here by name.
    """
    files, missing, spare = on_disk(outputs)
    ok = True
    print("The committed packet files, against a build made from today's sources:")
    print("")
    for path in sorted(outputs):
        name = os.path.basename(path)
        if path in missing:
            print("  {:<62} NOT ON DISK".format(name))
            ok = False
        elif files[path] == outputs[path]:
            print("  {:<62} up to date".format(name))
        else:
            same_length = len(files[path]) == len(outputs[path])
            print("  {:<62} STALE - committed {} characters, rebuild {}{}".format(
                name, commas(len(files[path])), commas(len(outputs[path])),
                ", same length but different text" if same_length else ""))
            ok = False
    for name in spare:
        print("  {:<62} NOT BUILT BY THIS SCRIPT - left over from an older build?"
              .format(name))
        ok = False
    print("")
    print("  every committed packet file matches a fresh build: {}".format(
        "YES" if ok else "NO - run this script without --verify to rebuild them"))
    return ok, files, missing


WHAT_IS_CHECKED = """\
What this check covers, and what it does not.

It does check: that every packet file on disk is what this script builds from
today's source records, so a record that changed after the packets were last
built is reported as stale, by file name; that no packet file is missing and
none is left over from an older build; that the two packets carry the same
records in the same order, shown by a matching sha256 checksum; and that the
brief's amended sentence is word for word the protocol's.

It checks the records themselves in two ways, because they are made in two ways.
A record that reproduces a whole file is compared with that file, character for
character. An excerpt is put together by hand in the packet document, so every
line it reproduces has to be in the file the record names, character for
character, and those lines have to run strictly forward through that file -
nothing reordered, nothing repeated, nothing quietly reworded. The line counts
beside each excerpt above are what that came to.

It does not compare: the words the packet writes around an excerpt - the
paragraphs introducing it and the labels saying which rows are left out - which
reproduce nothing and so have no source to be compared with; and the brief,
whose source is the packet document that already held it, so comparing the two
shows only that it was carried over unchanged, its one amended sentence being
checked against the protocol separately. Nor can it see what an excerpt leaves
out: it tests every line that is on the page, not whether a line that should
have been kept is missing.

It does not check whether the records themselves are true or current, whether
an excerpt was cut in a way that flatters the text under review, or whether
anything outside the packets agrees with them. A clean result here means the
packets match the source records as those records stand today. It does not mean
the source records are right."""


if __name__ == "__main__":
    built = build()
    checking_only = "--verify" in sys.argv

    if not checking_only:
        for path in write(built):
            print("wrote " + path)
        sizes(built)
        print("")
        print("Checking what was just written.")
        print("")
        good = verify(built)
        print("")
        print(WHAT_IS_CHECKED)
        sys.exit(0 if good else 1)

    sizes(built)
    print("")
    fresh_ok, files, missing = against_disk(built)
    print("")
    if missing:
        print("Stopping here. The record-by-record check needs every packet file on")
        print("disk, and {} of them {} missing, so it cannot be run. Nothing above".format(
            len(missing), "is" if len(missing) == 1 else "are"))
        print("should be read as saying the committed packets are current.")
        sys.exit(1)
    print("Now the records inside the committed files - read from disk, not from the")
    print("build above - each against the file it was taken from:")
    print("")
    good = verify(files) and fresh_ok
    print("")
    print(WHAT_IS_CHECKED)
    sys.exit(0 if good else 1)
