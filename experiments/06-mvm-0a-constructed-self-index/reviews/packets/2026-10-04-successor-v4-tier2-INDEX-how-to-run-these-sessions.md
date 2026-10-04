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

- **Gemini** gets one document, 806 KB.
- **ChatGPT** gets the same material as 33 files, none bigger than
  28 KB, pasted into **one** conversation, in order.

The material in the two packets was compared character by character after they
were built and is the same: 785,686 characters of records in each, with the
same fingerprint (a sha256 checksum, the standard way of showing two texts are
identical to the byte):

    2e9d1a9180a922b2eb7cf0b473549049507d9671817e1b2d6d3e42e96710d1f5

Each of the 25 records was also compared with the file it comes from,
character for character: 20 are whole files, 3 are whole sections of
the review protocol, cut at its own headings, and 2 are the opening lines of two
code files, by line number.

## Session 1 - Gemini, one document

1. New chat. Give it `2026-10-04-successor-v4-tier2-gemini.md` whole: paste it if the app takes the paste,
   attach the file if it does not.
2. The document tells it what to do, including to read start to finish rather
   than search, and to label its findings G1, G2, G3 and so on.
3. When it answers, check that it refers to records by file name and to version
   4 by section number. If it says it saw only part of the document, stop and
   give it the ChatGPT files instead, in one conversation, in order: they carry
   identical material.

## Session 2 - ChatGPT, one conversation, 33 pastes

**This is one session, not 33 sessions.** A reviewer who sees part of the
record in each of several chats has reviewed nothing.

1. New chat.
2. **Paste the contents** of file 01, then 02, and so on, one message each. Do
   not attach them: an attachment may be searched rather than read.
3. Each file tells it to reply with one short line and wait. After file 33
   it gives the review. If it starts early, tell it to wait for the rest.
4. The files are numbered in their names; filename order is the right order.

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
| Gemini session | `2026-10-04-successor-v4-tier2-gemini.md` | 806 KB | the whole packet in one document |
| ChatGPT 1 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-01-of-33-start-here-and-records-1-to-3.md` | 23.3 KB | orientation, the list of records, and how to answer; 1. THE BRIEF - the questions you are answering (fixed protocol text, sent unchanged to every reviewer); 2. the closure rule this text is being reviewed under; 3. the rule that a full measurement rehearsal comes before any registration review |
| ChatGPT 2 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-02-of-33-records-4.md` | 26.4 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 3 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-03-of-33-records-4.md` | 25.8 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 4 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-04-of-33-records-4.md` | 26.7 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 5 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-05-of-33-records-4.md` | 25.3 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 6 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-06-of-33-records-4.md` | 23.7 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 7 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-07-of-33-records-4.md` | 24.2 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 8 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-08-of-33-records-4.md` | 24.7 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 9 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-09-of-33-records-4.md` | 26.3 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 10 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-10-of-33-records-4.md` | 26.5 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 11 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-11-of-33-records-4.md` | 25.3 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 12 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-12-of-33-records-4.md` | 26.0 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 |
| ChatGPT 13 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-13-of-33-records-4-to-5.md` | 26.3 KB | 4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4; 5. the inside reviewer's findings on version 4 (Gate A, tier 1) |
| ChatGPT 14 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-14-of-33-records-5.md` | 26.7 KB | 5. the inside reviewer's findings on version 4 (Gate A, tier 1) |
| ChatGPT 15 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-15-of-33-records-5.md` | 26.5 KB | 5. the inside reviewer's findings on version 4 (Gate A, tier 1) |
| ChatGPT 16 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-16-of-33-records-5.md` | 22.8 KB | 5. the inside reviewer's findings on version 4 (Gate A, tier 1) |
| ChatGPT 17 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-17-of-33-records-6-to-8.md` | 22.1 KB | 6. John's rulings of 2026-10-03 on the review of version 3 (binding on version 4); 7. John's three rulings of 2026-10-03 after the controls re-run; 8. John's evening ruling of 2026-10-03: the fifth outcome and the figure printed both ways |
| ChatGPT 18 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-18-of-33-records-9-to-12.md` | 24.6 KB | 9. first record of John's ruling on version 4's seven questions; 10. second record of the same ruling, which stands where the two differ; 11. John's ruling on which of the two records stands; 12. John's ruling on the two questions raised by the check of version 4 |
| ChatGPT 19 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-19-of-33-records-13-to-14.md` | 26.0 KB | 13. John's ruling of 2026-10-04 on seven questions from the competing-solver run and the twenty-piece control; 14. the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry) |
| ChatGPT 20 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-20-of-33-records-14.md` | 26.8 KB | 14. the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry) |
| ChatGPT 21 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-21-of-33-records-14-to-15.md` | 25.6 KB | 14. the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry); 15. the check of the competing-solver run and the twenty-piece control |
| ChatGPT 22 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-22-of-33-records-15.md` | 24.0 KB | 15. the check of the competing-solver run and the twenty-piece control |
| ChatGPT 23 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-23-of-33-records-15-to-16.md` | 22.2 KB | 15. the check of the competing-solver run and the twenty-piece control; 16. the measurement rehearsal on small stand-in models |
| ChatGPT 24 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-24-of-33-records-16.md` | 26.5 KB | 16. the measurement rehearsal on small stand-in models |
| ChatGPT 25 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-25-of-33-records-16-to-17.md` | 26.1 KB | 16. the measurement rehearsal on small stand-in models; 17. the repairs to the rehearsal |
| ChatGPT 26 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-26-of-33-records-17.md` | 25.6 KB | 17. the repairs to the rehearsal |
| ChatGPT 27 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-27-of-33-records-17-to-18.md` | 25.8 KB | 17. the repairs to the rehearsal; 18. the toy re-run under version 3's rules |
| ChatGPT 28 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-28-of-33-records-18-to-19.md` | 22.7 KB | 18. the toy re-run under version 3's rules; 19. the controls re-run under the registered rules (source of every toy figure in version 4) |
| ChatGPT 29 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-29-of-33-records-19-to-20.md` | 26.2 KB | 19. the controls re-run under the registered rules (source of every toy figure in version 4); 20. the short pre-stated run |
| ChatGPT 30 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-30-of-33-records-20-to-22.md` | 25.7 KB | 20. the short pre-stated run; 21. the ordinary competing solver put through the measurement; 22. the other-agent control against twenty random pieces (NOT A RESULT: a code test) |
| ChatGPT 31 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-31-of-33-records-22-to-23.md` | 26.0 KB | 22. the other-agent control against twenty random pieces (NOT A RESULT: a code test); 23. the list of what has gone wrong in this program before, which the inside reviewer ran against version 4 |
| ChatGPT 32 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-32-of-33-records-23.md` | 26.6 KB | 23. the list of what has gone wrong in this program before, which the inside reviewer ran against version 4 |
| ChatGPT 33 of 33 | `2026-10-04-successor-v4-tier2-chatgpt-33-of-33-records-23-to-25.md` | 18.7 KB | 23. the list of what has gone wrong in this program before, which the inside reviewer ran against version 4; 24. the opening description of the closed design's task grammar, which version 4 says its grammar extends (inside finding RT-239); 25. the opening description of the rehearsal's task grammar (inside finding RT-239) |

## What was built from what

- Version 4 of the proposal: `docs/successor-experiment-proposal-2026-10-03-v4.md`, last changed at commit `41b0bd3`.
- The inside reviewer's findings: `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`, last changed at commit `135c1f7`.
- The brief, the closure rule and the rehearsal rule: `docs/outside-review-protocol.md`, as committed.
- Every other record: the file named in its marker line, as committed.

## If version 4, the findings, or any record changes before you run the sessions

Run `python3 scripts/build_successor_v4_tier2_packets.py` from the top of the
repository. It rebuilds both packets and this page and prints the check. Only
the files that changed need re-pasting.
