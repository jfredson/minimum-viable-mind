# Program-level outside review, 2026-09-20

*Assembled 2026-09-20 (Pacific) in a Cowork session at John's request:
"outside eyes from another model on the work we have been doing on MVM and
whether or not we are on the right track to actually finding a meaningful
result or whether we might need to look at changing anything in our
process." Two reviewers, Gemini and ChatGPT (Astra), the tier-2 pair named
in `docs/outside-review-protocol.md`.*

## What this is and is not

This is not a Gate A, B or C review under the protocol. Those review one
document against the registered text it must be read against. This asks
the program-level question the protocol does not: whether the program as
designed and as run can produce a result that would mean something
outside it, and what should change. It is advisory. Its findings feed the
2026-10-04 step 4 decision and are ruled on in the ledger like any other
tier-2 findings (labelled G-n and A-n; they take RT numbers only if
adopted).

## Files

| file | what it is |
|---|---|
| `brief.md` | The fixed brief, sent unchanged to both reviewers. Five questions, the response format, what happens to the response. |
| `cover-gemini.md`, `cover-chatgpt-astra.md` | The short model-specific cover notes (what is attached, how to read it, finding prefix). |
| `PASTE-gemini.md`, `PASTE-chatgpt-astra.md` | Cover note plus brief in one file, the thing John pastes as the first message. Generated. |
| `bundle-1-design.md` | Verbatim: spec, theory ledger, corrigibility commitments, experiment ladder, roadmaps, all three pre-registrations, Amendment A3, the pilot pre-statement, the public-path roadmap. |
| `bundle-2-record.md` | Verbatim: STATUS.md current-state sections, every findings memo the current state cites, the full red-team ledger RT-01 to RT-93, the review protocol, the step 4 proposal, the follow-up brief. |
| `bundle-3-appendix.md` | Verbatim: the A3 and A4 proposals and their red teams, the three tier-1 reviews on file with their packets, the compute ledger, research notes, the explainer, the experiment 7 pre-registration. |
| `make-bundles.sh` | Rebuilds the bundles and the PASTE files from the committed sources. The bundle file lists are the selection record. |
| `response-gemini.md`, `response-chatgpt-astra.md` | To be added: each reviewer's response, filed verbatim, never edited, with model, version, date and mode at the top. |

## Selection rule

Everything a reviewer needs to check the record's claims against the
record: every registered or pre-stated document, every findings memo that
the current state of `STATUS.md` cites, the whole ledger of findings and
rulings, and the protocol the program says it follows. All verbatim.
Chat transcripts, code, raw JSON outputs and the paper drafts are left
out: the findings memos quote the numbers the JSON holds, the drafts are
downstream of the claims under review, and the code cannot be run by the
reviewer anyway. `STATUS.md` is trimmed to its current-state sections
because the older entries restate what the findings memos say and would
triple the bundle.

What the brief itself contains from outside the record: the framing of
the five questions and the "what has happened" summary. That summary was
written to state facts with file citations and no evaluation; if a
reviewer finds a place where it editorializes, that is a finding.

## Running it

1. `cd ~/Code/minimum-viable-mind && bash docs/reviews/2026-09-20-program-review/make-bundles.sh`
   (already run once at assembly; re-run if any source file changes before
   the sessions).
2. Gemini app: new chat, attach the three bundles, paste `PASTE-gemini.md`.
3. ChatGPT app, Astra: new chat, attach the three bundles, paste
   `PASTE-chatgpt-astra.md`. If it reports seeing excerpts rather than the
   whole files, paste bundles 1 and 2 into the chat in sections and ask it
   to confirm each before continuing.
4. Save each response verbatim as `response-gemini.md` and
   `response-chatgpt-astra.md` here, with the header the brief asks for.
5. Then a disagreement map (where the two reviewers differ, and where both
   differ from the record) and rulings in `red_team_ledger.md`.
