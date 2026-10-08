# Ruling confirmed 2026-10-08: the decisions of 2026-10-06 on the two built models that lost their ownership route, and on the spending alarm

*Written 2026-10-08 (Thursday evening, Pacific) by a Claude Code session.
Authorship: **mixed.** A session wrote the packet these decisions answer and
drafted the sentence below; John chose it. This file is dated today and
**confirms** decisions first made on 2026-10-06; it is not a ruling first made
today.*

## Why this file exists

On 2026-10-06 John ruled on the packet about the two built models that lost
their ownership route
(`docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`, checked in pull
request 112). The work that carried those decisions out reported them as
ruled in its method notes, but no rulings file recorded John's words. Version
5 of the registration text (`docs/successor-experiment-proposal-2026-10-07-v5.md`,
section 21, open item 2) asked for one before the registration commit, so
that section 5.6 and section 12.5 cite a ruling and not a method note.

## John's words

The session offered three wordings. John answered "1", choosing this one:

> "I confirm the 2026-10-06 rulings as the method notes record them: option
> 1(b) plus option 4 on the flat models, the four alarm fixes, and the three
> follow-up alarm rulings."

## What that confirms, as the method notes record it

**On the two built models (the packet's page 1), as recorded in
`docs/2026-10-06-sharpness-fix-inuse-check-method.md`, "What John ruled":**

- **Option 1(b).** The number that sets how decisive the built-in "which
  agent am I" answer is (the sharpness) is fixed at 4.0, not learned, in all
  three built models: arm T, arm C and arm M.
- **Option 4.** A check, run on every trained model, fails a built model
  whose ownership route has gone flat; such a seed gets "no verdict",
  recorded as "construction did not hold".
- The three reruns at the 10-million-parameter size are approved, to run only
  after that code change and its independent check pass. The condition for
  going on, which had been "continue if the decoy test is not fooled",
  became "continue only if the built route is shown to hold in those
  reruns" (the packet, page 1, "Page 12"). The bar for "holds" was ruled
  separately on 2026-10-08 (`docs/rulings/2026-10-08-verification-bar-ruling.md`).

**On the spending alarm (the packet's page 2), as recorded in
`docs/2026-10-06-tripwire-fixes-method.md`, section 1:**

1. The alarm reads the vendor balance every few minutes while machines run,
   with a rule that can act on less than an hour of readings, plus a
   comparison at each machine's deletion. This replaces version 4's
   "hourly" (section 12.5).
2. The step that deletes a machine writes the deletion time into the alarm's
   records.
3. Empty, not-yet-posted bills count as "cannot be checked yet", which is a
   trip.
4. Each laptop deadline timer stops itself only on a confirmed deletion,
   never on a failed or empty reading.

**The three follow-up alarm rulings, made after the first check of those
fixes, as recorded in `docs/2026-10-06-tripwire-fixes-recheck-method.md`,
item 3:**

1. A bill covering less than 0.90 of a machine's life counts as "cannot be
   checked yet".
2. The 3-hour rule for whoever runs a launch is written where that person
   reads it.
3. A rise in the balance (a top-up) restarts the in-flight comparison, is
   logged, and does not trip.

## What it does not do

It changes no decision. It adds nothing the method notes did not already
report. John's own words of 2026-10-06 are in no rulings file on the main
line; this confirmation is what the record cites in their place. It closes open item 2
of version 5's section 21.
