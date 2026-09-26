# Ruling 2026-09-25: dispositions of the tier 1 reviewer-owned check of the A3 closure text, version 5

*Recorded 2026-09-25 (Pacific), by the Claude Code session "MVM W1 A3
registration commit", from John's message to it. The dispositions were given by
John on 2026-09-25, in the session that asked for version 5's revisions, and
passed in his words first to the re-checking session (which quotes them in the
Re-check section of the check file named below) and then to this one. The
choices are his; none of the wording here is his drafting. The findings are the
tier 1 reviewer's; the sentences are this session's. No compute was launched and
no money was spent under this ruling.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30), in the form of
`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`.*

*The check ruled on is the tier 1 reviewer-owned check of closure text version 5
that item 22 of that dispositions ruling and the closure rule
(`docs/outside-review-protocol.md`, "The closure rule") require before a
registration commit. It is filed at
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-closure-v5-tier1-check-claude-worktree.md`
(on the main line at commit `0e9cd4a`, pull request 45; its Re-check section,
which closes RT-204 and adds RT-211, landed as commit `cc26bbd`, pull request
47). It found one serious finding (RT-204), six minor ones (RT-205 to RT-210)
and, in the Re-check, one more minor one (RT-211). Nothing fatal. Its section 6
also read the two proposed annotations. The numbers RT-204 to RT-211 are the
ones the check assigned, and they are now the red team ledger's rows.*

---

## The ruling

1. **RT-204 (serious): accepted, and closed by the clause the reviewer
   proposed.** The successor paragraph's schedule sentence cited a ruling whose
   stated consequence for a missed kill date — dropping the roadmap to outcome
   R4, hibernation with a registered design and a rehearsal — had been withdrawn
   by item 23 of `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`,
   which the sentence did not cite. The check's proposed clause is added after
   the citation, word for word, plus a gloss on "R4" in item 23's own words.
   Landed in version 5 at commit `3393f7d` (pull request 43, merged as
   `ea52a02`); checked by the reviewer, not the writer, in the check's Re-check
   section "RT-204, closed: the clause as landed", MEASURED. That check is the
   closure.
2. **RT-205 (minor): accepted as wording.** The 135 tests per target is derived
   from the cited findings file's 270, not stated in it. A parenthesis says so
   and cites `powered-position-sweep-method.md` for the arithmetic. ChatGPT's
   adopted sentences are unchanged.
3. **RT-206 (minor): a ledger note, not a text defect.** The $450 programme
   ceiling (`docs/rulings/2026-09-26-weekend-1-queue.md`, page 6) had no line in
   the compute ledger. A dated ceiling note goes into `compute-ledger.md` with
   the registration commit, beside the stale $200 cap sentence, which is
   annotated and never rewritten. Version 5 changes nothing for it.
4. **RT-207 (minor): accepted as wording.** The gloss on "L1 subspace" names
   section 3.1 of `amendment-a3.md`, where L1 is defined, not 3.2, where it is
   localized.
5. **RT-208 (minor): accepted as wording.** The "causal patching" gloss, added
   inside a version 4 sentence that item 2 of the tier 2 ruling did not replace,
   is declared in the change table's item 2 row. No change to the block.
6. **RT-209 (minor): stays as recorded.** Version 4's clause that a blind-arm
   re-run would be a $0 side item stays out of the block, as item 14's
   replacement left it; the fact remains in the two rulings the block cites. No
   change.
7. **RT-210 (minor): accepted as wording.** The successor's description now
   cites item 5 of `docs/rulings/2026-09-20-center-as-degree.md` for its name,
   `docs/rulings/2026-09-23-range-and-direction-only.md` for "learn-both", and
   keeps `docs/competing-mechanisms-2026-09-20.md` for the contrast cases.
8. **RT-211 (minor): a citation fix outside the block.** The version 5 file
   cited the check as commit `99b8b64`, which the squash merge of pull request
   45 left off the main line; the check is on the main line at `0e9cd4a`. Both
   citations (the preamble and the change table's header of
   `docs/a3-closure-text-draft-2026-09-25-v5.md`) are changed to `0e9cd4a` in
   the registration commit. The closure block does not carry either.
9. **The annotation beside RT-164 stays as written.** The check (section 6)
   noted that the proposed row (`docs/proposed-annotation-rt164-2026-09-25.md`)
   carries more than the one sentence item 1 of the tier 2 ruling asks for. It
   lands whole, as a new row directly under RT-164 in the red team ledger, the
   RT-164 row itself unedited.
10. **The ChatGPT annotation's "not verified either way" reading stands.** The
    check (section 6) asked which of two readings of item 20's "no lookup
    verified" was meant. The proposed file
    (`docs/proposed-annotation-chatgpt-review-2026-09-25.md`) reads it as not
    verified either way, and that is the reading. It lands as proposed, as a
    separate dated file beside the ChatGPT review, which is never edited.
11. **The registration commit.** With the Re-check filed and its closing line
    reading that version 5 at `3393f7d` may be appended, the closure block is
    appended to `amendment-a3.md`, verbatim from the main-line file, by a session
    that neither wrote version 5 nor checked it, with the date placeholder
    filled and the compute ledger re-read that day. The red team ledger rows
    RT-204 to RT-211, the two annotations, the compute ledger's ceiling note
    and this file go in the same pull request. John's merge of that pull
    request is the registration commit.

## What this file does not do

It does not edit the check, the reviews, version 5's closure block, or any
protocol text. It does not rule on the tier 2 findings, which
`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md` already did, and it
does not reconcile RT-172 to RT-203 (item 21 of that ruling); the red team
ledger now carries a dated note listing what those numbers refer to, and the
reconciliation itself still waits on a later session.
