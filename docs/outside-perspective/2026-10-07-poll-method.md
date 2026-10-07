# The outside-model poll on the brief: method (2026-10-07)

*Written before the poll ran, by the Claude Code session that revised the
brief. John's go, in his words: "Go", given after the session proposed
automating the poll with the Gemini, OpenAI and Anthropic access the
workspace already has. $0 of rented computing; API spend of cents to a few
dollars per model, logged in the worklog rather than the compute ledger.*

## What runs

`docs/outside-perspective/run_poll.py`, from the repository root, with the
repository's own Python environment. For each of three model families, in one
conversation each:

1. **Round one.** The round-one paste file (`PASTE-round-one.md`, the brief's
   round one) followed by the book's argument summary
   (`calibration-problem/editorial/argument-summary-2026-10-07.md`), with a
   three-sentence preface saying what the two documents are and asking the
   model to answer as the brief asks.
2. **Round two.** The round-two paste file (`PASTE-round-two.md`: the author's
   two readings, the drafting session's view, the reviewing session's view),
   sent into the same conversation, asking which reading the first answer
   supports and whether anything changed.

Models, pinned in the script: `gemini-3.1-pro-preview`, `gpt-6-astra`,
`claude-opus-5-5`. Each is asked at its provider's default settings except
that the OpenAI call asks for high reasoning effort, and every call allows up
to 16,000 output tokens. No system prompt, no tools, no web access, no memory
of John. The Claude reply is a fresh conversation with none of this session's
context, and is marked in the record as the same family as the two Claude
views in round two.

## What is saved

- Every reply, word for word, at
  `docs/outside-perspective/replies/<date>-<family>-round-<one|two>.md`, with
  a header giving the model id, the provider's reported version, start and
  finish times, token usage and the SHA-256 of the exact message sent.
- A manifest, `replies/<date>-manifest.json`, with the SHA-256 and word count
  of each input file and of each assembled message, and per family the model
  id, provider version, timings, usage and any error.

## What counts as a stop

- A key missing, or a provider refusing the pinned model: that family is
  recorded as an error in the manifest and the others continue.
- A reply that fails after the built-in retries (three attempts, 0, 60 and
  180 seconds apart, on rate limits and server faults): recorded as an error;
  the family's round two is not sent.
- Nothing is edited after it is saved. If a reply is cut off by the output
  limit, the header's usage line shows it and it stays as saved.

## What this is not

Not a registered run and not evidence about any model's inside. It is the
record of what four or five frontier models said when asked the brief's
questions cold, kept so that the synthesis note can be checked against it.
Models that misread the record are left uncorrected; where they misread it is
itself a finding about the brief.
