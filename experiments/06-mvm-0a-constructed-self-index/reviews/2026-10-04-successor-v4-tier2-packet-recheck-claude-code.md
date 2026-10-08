# Re-check of the fixes to the outside-review packet (Gate A, tier 2) for successor proposal version 4

*Filed by the Claude Code session that wrote the first check
(`reviews/2026-10-04-successor-v4-tier2-packet-check-claude-code.md`, commit
`19aa404`). That first check is left unedited. This session did not write the
fixes. Written under the workspace plain-language rule. Every finding is
MEASURED (a command was run and its output is given) unless it is marked
ARGUED.*

## 2026-10-04 (Pacific): re-check of commit `26159e5` at branch tip `6f7c337`

**What was checked.** Commit `26159e5`, "Tier 2 packet: fix the two
opening-note sentences the packet check found wrong, and four smaller points".
It sits on `origin/gate-a-registration-review-successor-v4`, whose tip is
`6f7c337`, the merge that brings in the first check. My branch
`check-tier2-packet-successor-v4` was fast-forwarded to `6f7c337`.

**What was opened.** I opened the diff `6279573..26159e5` for ChatGPT file 1,
ChatGPT file 33, the Gemini document and the instruction sheet, read in full.
Everything else was read by script. I did not open the diff of the builder,
because its output is what was checked. Nothing was rented or spent, and the
packet and the builder were not edited.

**New script.** `recheck_fixes.py`, in
`reviews/2026-10-04-successor-v4-tier2-packet-check-scripts/`, imports
nothing from the builder. That folder also holds the outputs of the
first-check scripts, re-run at the new commits:
`rebuild_records_6f7c337.out.txt`, `packet_claims_6f7c337.out.txt` and
`builder_verify_6f7c337.out.txt`.

### Verdict

**Yes: the packet is fit to hand to John now.**
- Both must-fix defects from the first check are fixed, and every sentence of
  the new opening note matches the record.
- The repeated brief is the review protocol's text unchanged. It sits outside
  every record marker.
- The 25 records and their checksum are unchanged.
- Every ChatGPT file is within 28,000 bytes, and the instruction sheet's file
  table is right.
- One small leftover can wait: `README.md` in the list of files not carried
  still names the repository's top-level README. Version 4 means a README
  inside an output folder. This is part of the first check's defect 4, and the
  list is information only.

### (a) The opening note

    $ python3 .../recheck_fixes.py            (old 6279573, new 26159e5)
    spend sentence in orientation: describes (about $192 to $204 of rented compute in all, released in two parts, by version 4's section 12.4)
    version 4 section 12.4 total: about $192 to $204 | '## 12.4' or '### 12.4' heading present: True
    '$108' left anywhere in the new packet files: []
    opening ruling exists at 26159e5 : True
    'not in this packet' entries: 81 | heading says: 81 | entries that are not tracked paths: []

- **The spend figure (defect 1): fixed.** The note now says "about $192 to
  $204 ... by version 4's section 12.4". That matches version 4's table, and
  "$108" appears in no packet file. "Released in two parts" matches
  section 12.3 (the first release) and section 12.4 (the second).
- **Records 6 to 15 (defect 2): fixed.** Each sentence of the new paragraph
  against the record:
  - "6 to 8 came before it": true. The first check's commit list shows
    records 6 to 8 added at `56a5a86`, `fe5df65` and `f32ba0c`, all before
    version 4's commit `41b0bd3` (19:25 on 2026-10-03).
  - "9 to 11 were committed with it": true. They were added in `41b0bd3`.
  - "Records 12 and 13 (two later rulings)": true. They were added at
    `2ba5d18` and `03b7cd5`, after version 4.
  - "The wording fixes listed in the two checks (records 14 and 15) are not
    yet written in": true. Version 4 is unchanged since `41b0bd3`
    (`packet_claims` section 6).
  - "The inside review (record 5) lists every one of those changes in its
    section 'The registration text as reviewed'": true. That table has a row
    for each, read in the first check.
- **The opening ruling (defect 5): fixed.** The note names
  `docs/rulings/2026-10-04-registration-review-opened.md`, which exists at
  the commit. "Changes nothing in version 4" matches that ruling's last
  section: it "does not commit the registration, launch any run, or spend any
  money".
- **Smaller points.**
  - The marker description now includes "a range of its lines". True for
    records 24 and 25.
  - The list of files not carried now has 81 entries, all real tracked paths.
    Its heading now says that ambiguous short names are left off and that a
    file cited some other way may be missing. Both are true: the four cited
    check scripts named in the first check's defect 4 are still absent, and
    the heading now says so.
  - The instruction sheet's re-paste sentence is replaced by "use the rebuilt
    files from the start". True and clear.
  - The new size warning in the sheet (step 5) repeats the first check's
    estimate, which is still uncounted. It says so: "a rough estimate, not
    counted".

### (b) The repeated brief

    $ python3 .../recheck_fixes.py
    Gemini: text after the last record ends with the brief exactly: True | brief starts 174 characters into the tail | anything after the brief: ''
       lead-in line: *End of the packet. Answer the brief now. Label your findings G1, G2, G3 and so on. The brief is record 1; it is repeated here, unchanged, so it is fresh when you answer:*
    ChatGPT file 33: text after the last record ends with the brief exactly: True | brief starts 121 characters into the tail | anything after the brief: ''
       lead-in line: *End of the packet. The brief is record 1, in file 1; it is repeated here, unchanged, so it is fresh when you answer:*

"The brief exactly" means the protocol's section "The brief, fixed, sent
unchanged with every packet", cut at the next `## ` heading, compared
character for character. The repeated brief follows `===== END OF RECORD 25`
and carries no marker, so it is not a 26th record.

    $ python3 .../rebuild_records.py 6f7c337
    ChatGPT files: 33
    numbered 1..N with nothing missing: True | 'of' values: [33]
    largest ChatGPT file: 26,827 bytes (...-chatgpt-20-of-33-records-14.md); files over 28,000 bytes: []
    (25 rows, every one "True/True")
    characters: 785,686 | bytes: 786,335
    sha256 from sources:         2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    sha256 from Gemini doc:      2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    sha256 from ChatGPT files:   2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    sha256 in instruction sheet: 2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    Text outside every record, ChatGPT: 34 chunks (expected 33: file 1's orientation and 32 file headers)
    No problems found.

The 34th piece of text outside the records is the repeated brief at the end of
file 33. It is expected, and the "expected 33" printed by the script predates
it. The independent rebuild gives the same 25 records and the same checksum.

### (c) Sizes and the instruction sheet's table

    $ python3 .../packet_claims.py 6f7c337
    2. last ChatGPT file opens with the answer-now instruction: True
       files 2..32 each open with 'reply with one short line ... wait': True
    3. ... ChatGPT headers: 'A1, A2, A3' x 2 | 'G1' anywhere in headers: False
    4. index rows: 33 | rows whose size or record list is wrong: none
       Gemini size in index: 808 KB; actual 808,787 bytes

The largest ChatGPT file is 26,827 bytes, and file 33 grew to 20.2 KB. Every
row of the table gives the right size and records, and the Gemini size is
right. The finding labels are unchanged: G1… for Gemini, A1… for ChatGPT.

### (d) Nothing else changed in the material

    $ python3 .../recheck_fixes.py
    same set of packet file names: True | 35 files
    changed: 2026-10-04-successor-v4-tier2-INDEX-how-to-run-these-sessions.md       records region identical: (no records)
    changed: 2026-10-04-successor-v4-tier2-chatgpt-01-of-33-start-here-and-records- records region identical: True
    changed: 2026-10-04-successor-v4-tier2-chatgpt-33-of-33-records-23-to-25.md     records region identical: True
    changed: 2026-10-04-successor-v4-tier2-gemini.md                                records region identical: True

ChatGPT files 2 to 32 are byte-identical to `6279573`. In the three packet
files that changed, everything from the first record marker to the last
end-of-record marker is byte-identical. Only the opening note, the closing
lines and the instruction sheet changed.

    $ python3 scripts/build_successor_v4_tier2_packets.py --verify      (at 6f7c337)
    material carried: 785,686 characters
    Gemini material sha256:  2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    ChatGPT material sha256: 2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5
    OK: every record matches its source, character for character, in both packets; every ChatGPT file is within 28,000 bytes
    exit status: 0
