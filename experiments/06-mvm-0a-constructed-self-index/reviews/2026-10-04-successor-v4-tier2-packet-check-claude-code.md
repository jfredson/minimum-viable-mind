# Check of the outside-review packet (Gate A, tier 2) for successor proposal version 4

*Written 2026-10-04 (Pacific) by a Claude Code checking session, in its own git
worktree, on branch `check-tier2-packet-successor-v4`, cut from
`origin/gate-a-registration-review-successor-v4` at `6279573` (the commit that
added the packet: "Gate A tier 2 packet for proposal version 4"). This is a
paired check under "The pairing rule" of `docs/outside-review-protocol.md`. It
did not build the packet, has no chat history, and worked only from files
committed at `6279573`. Nothing was rented or spent: $0, laptop only. The
packet, its builder, version 4, the rulings and the reviews were not edited.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run; the command and its output are below or in the
folder beside this file) or **ARGUED** (reasoning a reader can dispute).*

## What this session opened, and what it did not

**Read in full:** the plain-language section of `~/Code/CLAUDE.md`; the
repository's `CLAUDE.md`; in `docs/outside-review-protocol.md`, the sections
"The pairing rule", "Two tiers", "The brief", "The closure rule" and "Rebuild a
document when new binding text starts to depend on it", and the amendments
section by search; the builder `scripts/build_successor_v4_tier2_packets.py`
(read, never imported); the instruction sheet
`reviews/packets/2026-10-04-successor-v4-tier2-INDEX-how-to-run-these-sessions.md`;
the orientation and record list at the start of ChatGPT file 1 and of the
Gemini document; `docs/rulings/2026-10-04-registration-review-opened.md`.

**Read in part:** the inside review
`reviews/2026-10-04-successor-v4-gate-a-claude-code.md` (its opening, verdict,
"What this review opened", findings table, "The registration text as
reviewed", RT-239, RT-241, RT-242, and "For the outside reviewers"); version 4
(its opening lines 1 to 60, section headings, and sections 12.1 to 12.4 on
money); the head of each 2026-10-03 and 2026-10-04 ruling file; the head of
the check of version 4; the heads and tails of ChatGPT files 2, 3, 13 and 33;
the ends of the two grammar headers; the headers of the two outside responses
of 2026-09-21 (for the label and size precedent).

**Not opened:** the body of any record beyond the above (the records were
compared by script, not read), `STATUS.md`, `data/project.toml`, the site, any
pull request, TimeAssembler, any chat.

**Scripts and outputs** are in
`reviews/2026-10-04-successor-v4-tier2-packet-check-scripts/`:
`rebuild_records.py` (part 1), `cited_files.py` (part 2), `packet_claims.py`
(part 3), `stale_test.py` (part 4), each with its `.out.txt`, plus
`builder_verify.out.txt`. None imports the builder. The first three read every
file through `git show 6279573:<path>`, so the working tree cannot help or hurt.

---

## Verdict

**No, not quite as it stands; two sentences of the orientation must change
first, and then the packet is fit to hand to John.** The material itself is
exactly right: rebuilt from the marker lines alone, by code that shares
nothing with the builder, all 25 records match their sources character for
character in both deliveries, the fingerprint in the instruction sheet is
what the sources give, the 33 ChatGPT files are numbered 1 to 33 with none
over 28,000 bytes, the selection carries every ruling and check that changes
version 4 before registration, and the builder's `--verify` passes on the
commit and fails when one character of a carried source changes. What must
change is in the orientation that both reviewers read first: **(1)** it says
the runs cost "about $108 of rented compute", a figure that appears nowhere in
version 4, whose own total for the successor is "about $192 to $204"
(section 12.4); and **(2)** it says records 6 to 15 are rulings and checks
"made after it was written" that "say what must be changed in it", when
records 6 to 8 were committed before version 4 and are already written into
it, and records 9 to 11 were committed with it and carried into it. Fix both
in the builder's `ORIENTATION` text (suggested wording in defects 1 and 2),
rebuild, run `--verify`, and have the next check re-run
`rebuild_records.py` and `packet_claims.py`. Only ChatGPT file 1 and the Gemini
document should change (plus the instruction sheet's size column); the
fingerprint of the material should not. Everything else below can wait,
though defect 3 is worth John's attention before he starts the ChatGPT session.

---

## Defects

### 1. must-fix-before-handing-over (MEASURED). "About $108 of rented compute" is not in version 4

The orientation says, of version 4: "the runs it describes (about $108 of
rented compute) are launched against it." Version 4 never says $108. Its own
table in section 12.4 gives "The successor, all in: about $192 to $204"; the
first release is "about $44" and the second "about $119" on the ruled split.

    $ python3 .../packet_claims.py        (section 5 of the output)
    5. '$108' in version 4: False | '108' anywhere in v4 money sections: False
       version 4's own total for the successor: about $192 to $204

    $ git grep -n -E "\$108" 6279573 -- . (packets and builder excluded)
    docs/december-result-roadmap-2026-09-20.md:331:nine registered runs ($108), one re-run ($12), ...
    docs/preauthorised-spending-proposal-2026-09-21.md:108:(that is $108, not "about $110") ...
    docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:901:at the proposal's $12 planning figure would be $108, a different basis.
    docs/successor-experiment-proposal-2026-09-21.md:804:   it saves about $96 of the $108 wave. ...
    (and five lines of a 2026-09-25 packet check, one calling $108 "a different basis")

So $108 is version 1's old figure (nine runs at $12 each), which later records
call a different basis. ARGUED, why it matters: the brief's first part asks
the reviewer about feasibility and cost, and a reviewer who finds the
orientation and the text disagreeing by about $90 will spend time on a
discrepancy the packet made, or report it as a finding in the text. *Fix:*
"(about $192 to $204 of rented compute in all, by version 4's section 12.4,
released in two parts)".

### 2. must-fix-before-handing-over (MEASURED). Records 6 to 8 were not "made after it was written"

The orientation: "Several rulings and two checks made after it was written say
what must be changed in it before it is committed (records 6 to 15)." The
commits that added each record:

    $ git log --diff-filter=A --format='%h %ad %s' --date=format:'%m-%d %H:%M' -- <the eight ruling files> <version 4>
    03b7cd5 10-03 20:48 Record John's ruling on the seven questions from the competing-solver run, ...   (record 13)
    2ba5d18 10-03 19:47 Record John's ruling on the two questions raised by the check of proposal version 4   (record 12)
    41b0bd3 10-03 19:25 Version 4 of the proposal, both records of the seven-question ruling, and John's ruling on which stands   (version 4, records 9 to 11)
    f32ba0c 10-03 18:29 Check of the two ruling packets of 2026-10-03 ...   (record 8)
    fe5df65 10-03 17:22 Ruling packet and John's three rulings of 2026-10-03 after the controls re-run (#77)   (record 7)
    56a5a86 10-03 16:53 Ruling packet and John's rulings of 2026-10-03 on the review of successor proposal version 3 (#75)   (record 6)

Version 4 says of itself (line 5 onward) that it is version 3 "with John's
three sets of rulings of 2026-10-03 written in", and its notice at lines 41 to
53 says the seven-question rulings (records 9 to 11) were written in and
reconciled. So the rulings still waiting to be written into version 4 are
records 12 and 13 and the wording fixes in the two checks (records 14 and 15),
and the inside review (record 5) already lists every one of them in its
section "The registration text as reviewed". ARGUED, why it matters: a
reviewer told that records 6 to 11 are pending changes will look for edits
that were already made, and may report as a conflict something version 4
already carries. *Fix:* "Version 4 already carries the rulings made before and
with it (records 6 to 11). Two later rulings (records 12 and 13) and the two
checks (records 14 and 15) say what must still be changed in it before it is
committed; the inside reviewer's section 'The registration text as reviewed'
(record 5) lists every such change in one table."

### 3. can-wait, but John should know before the ChatGPT session (ARGUED). The ChatGPT packet is nearly twice the size of the last one that worked, and the brief is only in file 1

    $ cat ...-successor-v4-tier2-chatgpt-*.md | wc -c -w
      135915  827876
    $ cat ...-a3-closure-tier2-chatgpt-*.md | wc -c -w
       74760  464538

The ChatGPT packet is about 828,000 bytes and 136,000 words, which is very
roughly 200,000 to 230,000 tokens (no tokenizer was available here to count
exactly). The last ChatGPT packet, which ChatGPT reported reading in full
(`reviews/2026-09-21-a3-closure-chatgpt.md`, line 5), was 465,000 bytes. If the
model John uses holds less than the whole conversation, the earliest messages
are the ones dropped, and file 1 holds the orientation and the brief. File 33
says "Answer the brief (record 1, in file 1)" but does not carry it. This
session could not measure the app's limit, so this is not a must-fix. Two
cheap guards: John checks the model's stated context size before starting,
and, when file 33 is acknowledged, asks the model to quote the four part
headings of record 1 and the first line of record 4 before it answers; if it
cannot, the session has lost its start and should stop, as the instruction
sheet already says for a length limit. A builder change that repeats record 1
at the head of the last file would remove the risk; it is the protocol's text
unchanged, so it would not break the "sent unchanged" rule.

### 4. can-wait (MEASURED). The list of "files version 4 cites that are not in this packet" has six names that are not file paths, one wrong path, and misses six cited files

From `cited_files.py`, which reads version 4 more widely than the builder (any
extension, inside or outside backticks):

    (a) listed as not in the packet, but not a tracked file path at this commit:
        .venv-lock-2026-08-28.txt  (tracked files ending in /.venv-lock-2026-08-28.txt: 0)
        diagnose_named_other.json  (tracked files ending in /diagnose_named_other.json: 2)
        gate_base.json  (tracked files ending in /gate_base.json: 2)
        summary.json  (tracked files ending in /summary.json: 3)
        summary_base.json  (tracked files ending in /summary_base.json: 2)
        table.md  (tracked files ending in /table.md: 5)
    (b) listed as not in the packet, but carried as a record: none
    (c) cited by version 4, a tracked file, neither carried nor listed (6):
        experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
        experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
        experiments/06-mvm-0a-constructed-self-index/src/launch_a3.sh   <- cited as ['launch_a3.sh']
        experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
        scripts/check_citations.py
        scripts/check_single_source.py

What happens to cited names that do not resolve: the builder keeps a bare
name as written when it matches no tracked file or more than one, so five
ambiguous short names (each also present elsewhere in the list under its full
path) and one file that is not committed at all (`.venv-lock-2026-08-28.txt`;
the inside review found it is ignored by `.gitignore`) are listed under the
heading "named so you know they exist". And `README.md` is listed as the
repository's top-level README, but version 4 (lines 2324 and 3413) means the
README inside an output folder. The count "85" is the length of the list as
printed and is right for that list. ARGUED, why it can wait: the list is
information, not material; nothing in it is something a reviewer needs, and
the orientation already tells a reviewer to name any file a finding turns on.
A one-line note that bare names are short forms of the paths above would do.

### 5. can-wait (MEASURED). The orientation does not say where "John opened this review on 2026-10-04" is recorded

The other two of version 4's three opening conditions are tied to records 14,
21 and 15. The third is true and is recorded in
`docs/rulings/2026-10-04-registration-review-opened.md` (commit `f96c9eb`,
"Record John's ruling that the registration review of proposal version 4 is
opened", authorship John), which is neither carried nor named:

    $ python3 .../packet_claims.py   (section 5)
       ruling that opened the review is in the packet: False

It changes nothing in version 4, so it need not be carried; naming its path in
that sentence would let the reviewer check the claim like the other two.

### 6. can-wait (MEASURED). Two small wording slips in the packet's description of itself

- The orientation says each marker line "says whether it is a complete file or
  whole sections of one". Records 24 and 25 say a third thing, "lines 1 to 118
  of the file's 650, unedited". Add "or a range of lines".
- The instruction sheet's last paragraph says that after a rebuild "only the
  files that changed need re-pasting". Before a session starts nothing has
  been pasted, and a change to an early record moves every later cut, so the
  sentence can only mislead. "Start both sessions from the rebuilt files"
  would say it.

### 7. can-wait (MEASURED). `--verify` checks the working tree, and its check of the instruction sheet needs the git history

Run in a copy made with `git archive` (no history), `--verify` reported the
instruction sheet stale although nothing had changed, because the sheet names
the last commit that touched version 4 and the inside review, which a copy
without history cannot find. In a full clone it passes (part 4 below). It also
reads the working tree, not a commit, so on a checkout with uncommitted edits
it checks the edits. Neither is a defect in the packet; both are worth a line
in the builder's description for whoever runs it next.

### Not defects, said so they are not looked for again

- The finding labels: G1, G2... for Gemini and A1, A2... for ChatGPT, used
  consistently in the Gemini document (start and end), in ChatGPT files 1 and
  33, and in the instruction sheet (MEASURED, `packet_claims.py` section 3).
  "A3" also appears 31 times in the material, as Amendment A3; ChatGPT's
  finding A3 will share that name. The same labels were used on 2026-09-21
  without trouble, so this is noted only.
- The two code records run to lines 118 and 70, not the 115 and 65 the inside
  review suggested; both end exactly at the closing quotes of the file's
  opening description, so the extra lines finish the description and add
  nothing else.

---

## The checks, one by one

### Part 1. The material is what it says (MEASURED)

Method: `rebuild_records.py` reads the 33 ChatGPT files joined in filename
order and the Gemini document, and takes each record (and each part of a
record) to be everything after the newline that ends its `===== RECORD` line
and before its `===== END OF RECORD` line, joining parts in part order. Each
record is compared with: the whole file at `6279573`; for "whole sections",
the protocol from the named `## ` heading up to the next `## ` heading, trailing
blank lines dropped and one newline kept; for line ranges, those lines. The
"material" whose fingerprint is taken is the 25 records cut from source, joined
in record order, as UTF-8; that is well defined because every source ends in a
newline and no marker text is added inside a record.

    $ python3 experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-tier2-packet-check-scripts/rebuild_records.py
    ChatGPT files: 33
    numbered 1..N with nothing missing: True | 'of' values: [33]
    largest ChatGPT file: 26,827 bytes (2026-10-04-successor-v4-tier2-chatgpt-20-of-33-records-14.md); files over 28,000 bytes: []

    rec | how cut | source | parts G/C | equal to source G/C
      1 | section 'The brief, fixed, sent...' up to 'The closure rule, whic...' | docs/outside-review-protocol.md | 1/1 | True/True
      2 | section 'The closure rule, whic...' up to 'Rebuild a document whe...' | docs/outside-review-protocol.md | 1/1 | True/True
      3 | section 'The measurement rehear...' up to 'The failure-mode pass:...' | docs/outside-review-protocol.md | 1/1 | True/True
      4 | whole file | docs/successor-experiment-proposal-2026-10-03-v4.md | 1/12 | True/True
      5 | whole file | .../reviews/2026-10-04-successor-v4-gate-a-claude-code.md | 1/4 | True/True
      6-23 | whole file | (the 18 rulings, checks and run records) | ... | True/True on every one
     24 | lines 1-118 of 650 | experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py | 1/1 | True/True
     25 | lines 1-70 of 485 | experiments/rehearsal-successor-measure/src/grammar.py | 1/1 | True/True

    material = the 25 records cut from source at this commit, joined in record order, utf-8
    characters: 785,686 | bytes: 786,335
    sha256 from sources:         2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    sha256 from Gemini doc:      2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    sha256 from ChatGPT files:   2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    sha256 in instruction sheet: 2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    Text outside every record, ChatGPT: 33 chunks (expected 33: file 1's orientation and 32 file headers)
    No problems found.

(Rows 6 to 23 are condensed here; the full table is in `rebuild_records.out.txt`.)
The script also checks that every marker's character and line counts match the
source, that no opening marker sits inside another record, that parts are
numbered 1 to N with none missing, and that the two packets label each record
the same way. **Matches:** every record equals its source in both packets; the
files are 1 to 33, all under 28,000 bytes; the fingerprint and the 785,686
characters in the instruction sheet are what the sources give. Had any record
been cut, reordered, edited or wrongly split, its row would read False.

### Part 2. The selection (MEASURED for the lists, ARGUED for what matters)

Derived from version 4's citations, the inside review's "For the outside
reviewers", and the files dated 2026-10-03 or 2026-10-04:

    $ git ls-tree -r --name-only HEAD | grep -E "2026-10-0[34]" (rulings and reviews, packets excluded)
    docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md         not carried: a proposal; the ruling (record 7) states what was ruled
    docs/rulings/2026-10-03-controls-rerun-rulings.md                record 7
    docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md record 8
    docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md   record 9
    docs/rulings/2026-10-03-seven-questions-reconciliation.md        record 11
    docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md    not carried: a proposal; record 6 states the rulings
    docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md           record 6
    docs/rulings/2026-10-03-version-4-check-questions-rulings.md     record 12
    docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md          not carried: its suggestions are in version 4's section 19
    docs/rulings/2026-10-03-version-4-questions-rulings.md           record 10
    docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md record 13
    docs/rulings/2026-10-04-registration-review-opened.md            not carried: opens the review, changes nothing in version 4 (defect 5)
    reviews/2026-10-03-proposal-v4-check-claude-code.md              record 14
    reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md record 15
    reviews/2026-10-04-successor-v4-gate-a-claude-code.md            record 5
    reviews/2026-10-03-{controls-rerun,short-prestated-run,rulings-2026-10-03}-check-claude-code.md,
    reviews/2026-10-03-successor-v3-gate-c-claude-code.md            not carried, listed; version 4 says it already follows each (its table, lines 69 to 76)

- **Rulings or checks that change version 4 before registration:** none
  missing. Every row of the inside review's table "The registration text as
  reviewed" names a source that is a record here (10, 12, 13, 14, 15).
- **Records a tier 1 finding turns on:** the inside review's own list (its
  "For the outside reviewers", items 1 to 7) is carried in full, and
  every ruling its findings cite is carried (RT-241's "page 11" is in records 6
  and 8). Not carried, and named in the "not in this packet" list: the label
  search's findings (`docs/2026-09-26-free-arm-label-search.md`, on which
  worth-noting RT-242 turns; the inside review quotes the row it needs),
  Amendment A3's text (`amendment-a3.md`, where the batteries of fatal RT-237
  come from), and the code behind RT-238's unwritten floor clause
  (`src/repairs.py`). ARGUED: none of these is needed to weigh the findings,
  since the inside review quotes what it relies on, and a reviewer who wants
  them is told to say so. Not a gap that matters for the brief.
- **The list of cited files not carried:** see defect 4.

### Part 3. The packet's own words (MEASURED unless marked)

    $ python3 .../packet_claims.py
    1. orientation and record list identical in Gemini doc and ChatGPT file 1: True
    2. last ChatGPT file opens with the answer-now instruction: True
       Gemini document ends with: '*End of the packet. Answer the brief (record 1) now. Label your findings G1, G2, G3 and so on.*'
       files 2..32 each open with 'reply with one short line ... wait': True
    3. ... ChatGPT headers: 'A1, A2, A3' x 2 | 'G1' anywhere in headers: False
    4. index rows: 33 | rows whose size or record list is wrong: none
       Gemini size in index: 806 KB; actual 806,670 bytes
    5. '$108' in version 4: False | ...  version 4's own total for the successor: about $192 to $204
       version 4 length in characters: 292,507 (orientation: 'about 290,000')
       v4 opening quote present: True
    6. successor-experiment-proposal-2026-10-03-v4.md: index names 41b0bd3 (True); content at 41b0bd3 same as at 6279573: True; last commit touching it: 41b0bd3
    6. 2026-10-04-successor-v4-gate-a-claude-code.md: index names 135c1f7 (True); content at 135c1f7 same as at 6279573: True; last commit touching it: 135c1f7

Sentence by sentence:

- "Record 4 below, about 290,000 characters": 292,507. Holds.
- "In its own words (section 0) ... 'which agent am I' sits in a slot ...":
  version 4 lines 96 to 102. Holds.
- "About $108 of rented compute": does not hold (defect 1).
- "Several rulings and two checks made after it was written ... (records 6 to
  15)": does not hold for records 6 to 11 (defect 2).
- "Version 4's opening says it 'cannot go to the registration review yet' and
  lists three things": line 15 and items 1 to 3. Holds. "The check is record 14,
  the solver run is record 21 with its check in record 15": each record is what
  its title says (rebuild above). Holds. "John opened this review on
  2026-10-04": holds, recorded in a file the packet does not name (defect 5).
- "An inside reviewer ... Any fatal finding in them is not yet fixed": the
  inside review reports one fatal (RT-237), four serious and five worth-noting,
  and version 4 is unchanged since `41b0bd3`, before that review. Holds.
- "Files version 4 cites that are not in this packet (85 of them)": 85 lines
  printed; their accuracy is defect 4.
- The instruction sheet: "806 KB", "33 files, none bigger than 28 KB",
  "785,686 characters", the fingerprint, "20 whole files, 3 whole sections, 2
  opening lines", every row of the file table (size and records), and the two
  commits in "What was built from what": all hold.
- **The brief is in file 1 and is the protocol's text unchanged:** record 1
  sits in ChatGPT file 1 and at the start of the Gemini document's records,
  and equals the protocol's section "The brief, fixed, sent unchanged with every
  packet" character for character (part 1, row 1). Holds.
- **Closing instruction:** in the first line of ChatGPT file 33 and the last
  line of the Gemini document. Holds.
- **Clear enough to run cold (ARGUED):** yes, for both people. The reviewer is
  told what the program is, what is under review, what has been ruled since,
  what the inside reviewer found and that it is not fixed, what is not shown
  and what to do about it, how records are marked and how to answer. John is
  told both sessions step by step, what to do if a paste becomes an attachment
  or is cut short, where to file the answers and how to head them, and not to
  cross-show the reviewers. The gaps are defects 2, 3 and 6. Plain language:
  the sheet explains Gate A, tier 2 and sha256 on first use; the orientation's
  title says "Gate A" without explaining it, which an outside reader can
  ignore. No bare identifier in either is left without a plain label.

### Part 4. The builder's own check (MEASURED)

    $ python3 scripts/build_successor_v4_tier2_packets.py --verify
    records: 25
       23,332 bytes  2026-10-04-successor-v4-tier2-chatgpt-01-of-33-start-here-and-records-1-to-3.md
       ... (33 ChatGPT files and the Gemini document, sizes as in the instruction sheet)
    cited by version 4 but not in the packet: 85
    material carried: 785,686 characters
    Gemini material sha256:  2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    ChatGPT material sha256: 2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    OK: every record matches its source, character for character, in both packets; every ChatGPT file is within 28,000 bytes
    exit status: 0

Whether it catches a stale packet: the branch was cloned into this session's
scratch folder, and `stale_test.py` changed one letter of one source in the
clone at a time, ran `--verify`, and put the file back. Four changes inside
carried material should fail; two outside it should not.

    $ cd <scratch clone of the branch> && python3 .../stale_test.py
    a ruling carried whole (record 13), line 10: changed 's' -> 'X'
       exit status 1; expected to fail: True; AS EXPECTED
         - .../2026-10-04-successor-v4-tier2-gemini.md is stale
         - .../2026-10-04-successor-v4-tier2-chatgpt-19-of-33-records-13-to-14.md is stale
         - record 13 differs from its source in the Gemini packet (docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md)
         - record 13 differs from its source in the ChatGPT packet (docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md)
    version 4 (record 4), line 2223: changed 't' -> 'X'
       exit status 1; expected to fail: True; AS EXPECTED   (names Gemini and ChatGPT file 08 stale; record 4 differs in both)
    the brief in the protocol (record 1), line 390: changed 'N' -> 'X'
       exit status 1; expected to fail: True; AS EXPECTED   (names Gemini and ChatGPT file 01 stale; record 1 differs in both)
    grammar.py inside the cut (record 25), line 40: changed 'a' -> 'X'
       exit status 1; expected to fail: True; AS EXPECTED   (names Gemini and ChatGPT file 33 stale; record 25 differs in both)
    grammar.py outside the cut, line 300: changed 's' -> 'X'
       exit status 0; expected to fail: False; AS EXPECTED
    the protocol outside the three carried sections, line 30: changed 'P' -> 'X'
       exit status 0; expected to fail: False; AS EXPECTED
    clone working tree clean after the test: True

**Matches:** `--verify` passes on the commit, fails on a one-character change
to any carried source, names the exact file to re-paste, and stays quiet on
changes outside the carried material. What it cannot catch, by design: a new
ruling that ought to be carried but is not on its list. That is what part 2
of this check is for.
