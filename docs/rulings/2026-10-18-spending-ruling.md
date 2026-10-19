# Ruling: every new spend gets its own go; the running total is a record, not a budget (2026-10-18)

*Recorded 2026-10-18 (Sunday evening, Pacific) by the session that worked the
programme that day. John ruled; authorship **john**. Records only: nothing
run, nothing spent. Written under the workspace plain-language rule.*

## Why it came up

The check of the paper's cost sentence (pull request 194) found that the
figure used everywhere for the programme's spend, "about $230.94 of $450",
was the compute ledger alone: rented machines from 2026-08-07, when the
ledger opened, to the stop of experiment C. It leaves out the removal test's
spend, which predates the ledger, and every API call, which the worklog
records. The question was what the $450 ceiling should count.

A status entry merged earlier the same evening (pull request 195) said that
John had ruled every vendor counts against the $450. He had not; the fifth
master session corrected its own relay, and this file records what he did
rule.

## John's words

To the fifth master session for the tracker sites, 2026-10-18 about 20:15
Pacific, relayed to this session: "I'm not so worried about the $450
ceiling, I just want to make sure we are keeping track of any new spending.
Any new spending needs to get ruled on rather than counted against some long
term cap."

## What is ruled

1. **Every new spend needs its own go from John before it happens**, with its
   estimate and its ceiling, as the battery rehearsal of 2026-10-18 had. This
   covers every vendor: rented machines, API calls, outside reviews by API,
   anything that costs money. A go covers what it names and nothing else.
2. **Every dollar actually spent is tracked in one place, all vendors
   together, with the go it was spent under**:
   `docs/spending-record.md`. The compute ledger stays the detailed record
   of rented machines, and the worklog keeps its before and after rows for
   API runs; the spending record is where they add up.
3. **The $450 figure stops being the control.** It stays on the record as the
   registered envelope of Amendment A2 for rented machines, with its history,
   but the running total across vendors is kept as a record, not as a budget
   to spend down.
4. **The open question of what the $450 ceiling counts is answered by this**:
   it no longer needs to count anything, because spending is controlled go by
   go.

## Where it lands

- This file; `docs/spending-record.md`, started with what the record holds.
- The compute ledger's rules (`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`),
  as a dated rule.
- `STATUS.md`: the evening entry's wrong sentence is corrected in place,
  with a dated note.
- `data/project.toml` and the headline: the spend line is the registered
  envelope again, and the headline gives the total spent across every vendor.
- The TimeAssembler worklog, as a decision entry with authorship john.
