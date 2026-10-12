# Gate A on the two-sided question text: what was run, what it found, what it cost

*Covering note, written 2026-10-09 (Pacific) by the session that ran tier 1
and sent the tier 2 packet. It summarises the four files below and says what
John is asked to read. It is not itself a review, and where it and a filed
review differ, the review stands.*

## The four files

| File | What it is |
|---|---|
| `2026-10-09-two-sided-question-gate-a-tier1-claude-code.md` | Tier 1, the inside pass: findings RT-283 to RT-295, the failure-mode pass on all six entries of the known-failure list, the decisive measured check, the kill case |
| `2026-10-09-two-sided-question-gate-a-gemini.md` | Tier 2, Gemini 3.1 Pro, findings G1 to G9, filed word for word |
| `2026-10-09-two-sided-question-gate-a-gpt.md` | Tier 2, GPT-6 Astra, findings A1 to A14, filed word for word |
| `packets/2026-10-09-two-sided-question-gate-a-tier2-packet.md` | The packet both outside models read (13 records, about 30,000 words), rebuilt from pinned commits by the script beside the tier 1 file |

The text reviewed is section 2 of the refounding proposal, version 2
(`docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md`, lines 99 to
199 on the main line at `d60ff2e`). Nothing has been written into the spec.

## How tier 2 was run, and the one departure from the protocol

The protocol says tier 2 is "run by John through their apps". This time a
script sent the packet by API, one message per model, no tools, no web, the
same way the 2026-10-07 poll was run on John's go
(`docs/outside-perspective/2026-10-07-poll-method.md`), reusing that poll's
client code and key sources. The same two labs as every earlier Gate A tier 2
(Google and OpenAI); the same model ids as the poll. The replies' headers say
so. If John wants tier 2 run his usual way, the packet file is ready to paste,
and its first section tells the reader how it was sent, which he would edit.

Both outside models were given the tier 1 findings, as the protocol requires,
so their agreement with tier 1 is not independent confirmation. Gemini's
reply mostly agrees with tier 1. GPT's adds most of what is new.

## What it cost

| Call | Tokens in | Tokens out (thinking included) | Price used | About |
|---|---|---|---|---|
| Gemini 3.1 Pro | 45,014 | 5,476 | $2 and $12 per million, Google's published rates, as recorded in `agi-zeitgeist/docs/vanguard/model-cost-quote-2026-10-03.md` | $0.16 |
| GPT-6 Astra | 42,780 | 11,393 | $10 and $40 per million, **an assumption**: no price for this model is recorded anywhere in the workspace, so a deliberately high one was used | $0.88 at most |
| **Both** | | | | **about $1.04 at most** |

Tier 1 cost nothing. Token counts are from the providers' replies, saved in
`2026-10-09-two-sided-question-gate-a-scripts/tier2_manifest.json`; the
dollar figures are worked out from them, and the real GPT charge is on
OpenAI's billing page. The Gemini call used the key in this repository's
`.env`, the one the poll used; the GPT call used the key the AGI Zeitgeist
scripts read. If the Gemini key bills to the same Google account as the AGI
Zeitgeist coding, October's figure there moves from about $22.03 to about
$22.19, inside John's limit of about $22.50 for that account. API spend goes
in the worklog, as the poll's did, not the compute ledger (which records
rented machines).

## What the three reviewers found

**All three: do not write section 2 into the spec as it stands.** None of
them objects to the turn the project made; all three object to sentences.

**Where they agree (and tier 2 had tier 1's findings in front of it):**

- The observer loss condition ("no better than chance") is fatal under the
  protocol's rehearsal rule and closes by stating ruling 10 instead (RT-283;
  G1; A1).
- "Passes the battery" and "smallest" have no rule behind them (RT-286; G5;
  A3, which adds that a minimum over an unbounded family is not decidable
  without a finite size grid and a "none found within the search" outcome).
- The spec as assembled would contradict itself (RT-284; A10).
- The "What Would Count Against It" paragraph is not written, and the
  suspension it describes leaves no way to lose (RT-285; G6; A9, A13).
- Section 2's "only" rule leaves out the battery's corroborated-report rule
  (RT-287; G4; A10).
- "Damage spread across every task" overstates experiment 1 (RT-292; G7; A14).
- The indicator list is not chapter 6's (RT-291; G9).

**Where tier 2 rates more severely:**

- "Degree measured" (RT-289, serious in tier 1): **fatal** to both outside
  models (G2, A2), as an unsupported measurement claim in binding text. GPT
  also asks that the automatic "non-zero" go, since an honest output rule has
  to allow zero.
- The spec contradicting itself (RT-284, serious in tier 1): **fatal** to
  Gemini, which reads it as a no-verdict failure because two pass-fail rules
  would bind at once. GPT keeps it serious.

**Where tier 2 disagrees with tier 1:**

- GPT rejects tier 1's argument that a smallest passing size collides with
  the battery's capacity loss condition (part of RT-286): the two can
  coexist. It keeps the missing pass rule serious.

**What tier 2 found that tier 1 did not (all ARGUED, GPT unless marked):**

- **A12, the router argument has a missing step.** The router-control note,
  which section 2's Floor sentence cites, argues that a real centre damages
  every battery, so the router control must read it as routing. That does
  not follow: the control fires only when the turn-tracking drop is at least
  the self-relevant drop, and damage everywhere says nothing about which drop
  is larger. GPT's made-up example (drops of 0.20, 0.30 and 0.10) damages all
  three and does not fire the control. So the record supports "the result was
  ambiguous" (+0.033, interval spanning zero), not "the instrument could
  never return the other answer". This bears on the Floor sentence and on
  decision 2's wording.
- **A11.** "No instrument aimed at the floor can return anything the identity
  does not already say" overreaches: an unsettled identity claim does not
  make the structure unmeasurable. GPT offers replacement wording.
- **A13.** The old loss condition (depth indicators without self-indexed
  binding underneath) is about architecture, not only about experience, so
  suspending it removes more than an unmeasurable verdict. GPT offers a
  standing loss condition to keep.
- **A4.** Calling a frontier model's readings "the cheaper routes" because
  its state is weights plus transcript confuses where state is held with what
  the computation does.
- **A5, A6.** An ordinary adaptive controller with a commitment table, a cost
  for change and a reset could pass the Depth rows; and where the system's
  boundary is drawn (weights or a memory module) can decide the fresh-instance
  test before it runs. Both ask each construction registration to fix the
  system's boundary and test an ordinary competing solver.
- **A7.** Knowing what was built is ground truth for the build, not for what
  observers detected: observers can tell arms apart by length, competence or
  errors.
- **A8.** A "smallest passing system" search needs a final confirmation on
  data not used to choose the system or the rule.
- **G8 (Gemini).** The Floor sentence turns the spec's instrument into "a
  definition" on the strength of an argued note; readers will take it as a
  measured result.

## What John is asked to read, and to decide

Nothing here waits on John to proceed with other work. Before section 2 can
be fixed and written into the spec, these are his calls:

1. **The founding wager** (RT-290). Review it through its own Gate A first
   (with its "found a router" sentence brought into line with decision 2 and
   its owed degree sentence added), or have section 2 state the one premise
   it needs in its own words.
2. **How section 2 sits beside Scope, The Floor and The Build** (RT-284; A10).
   Those are his text; either section 2 names what it supersedes, or the
   earlier sentences get dated notes.
3. **Whether to keep the old depth loss condition** (RT-285; A13) rather than
   suspend it.
4. **Whether the router-control wording changes** (A12): the Floor sentence,
   and possibly the description ruled in decision 2, rest on an argument GPT
   says has a missing step.
5. **Whether tier 2 by API is acceptable** for Gate A from now on, or should
   be re-run in the apps.
6. **Severity calls** where the tiers differ (RT-284, RT-289), and which tier
   2 findings take RT numbers (the protocol gives tier 2 findings RT numbers
   only when he adopts them).

Everything else is the author's to fix and a different session's to check.

## What happens next, in order

1. John's calls above.
2. A session that did not write section 2 or this pass applies the fixes to
   a version 3 of section 2 (the author may run the known-failure list first).
3. The closure checks: each fatal finding's fix checked by a session other
   than the one that wrote it, with the command and its output, as the
   closure rule requires; tier 1's closure checks are written under RT-283
   and RT-284.
4. Ledger rows for every adopted finding, with John's ruling on each.
5. Then, and only then, the commit into the spec.

No ledger row is written here, nothing is written into the spec, and the
proposal, the battery draft and `STATUS.md` are untouched.
