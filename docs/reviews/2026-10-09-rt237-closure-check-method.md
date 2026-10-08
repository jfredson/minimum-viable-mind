# Closure check of the fatal finding RT-237: method, written before the check ran

*2026-10-09. Claude Code, as the checker. Laptop only, $0. This session wrote
neither the repair under check (the gate code in
`experiments/08-successor-degree/src/measure.py` and `procedure.py`) nor the
registration text (version 5 of the successor experiment's proposal,
`docs/successor-experiment-proposal-2026-10-07-v5.md`). It checks the main line
as it stood when the check began, commit `760deef`.*

## What is being closed

The inside review of version 4 (the Gate A tier 1 review,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md`)
filed one fatal finding, RT-237: the free model's gate (arm F, the freely
trained system) required "the ownership-free state and syntax batteries" to
hold. Those batteries were end-of-episode question sets in the closed earlier
design. The successor's task has none, the clause set no line, and nothing had
ever measured it, so by the design's own rule that a gate which cannot be
evaluated counts as failed (stop condition S8), the free model could never be
read.

John ruled the repair on 2026-10-06 (`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`,
page 1, "(a), go with the recommendation"): the clause is replaced by a count
the task can produce. With the acting channel zeroed, the free model's
own-directed answer must still be the successor of one of the four agents'
earlier values on the item named, on 1,546 or more of the 3,000 held-out gate
episodes, on two seeds of three.

The closure rule (`docs/outside-review-protocol.md`, "The closure rule") says
the decisive check on a fatal finding's fix belongs to a reviewer, not to the
fix's author, and must be a measurement that would come out wrong if the fix
were wrong. The roadmap states what this closure needs: **every clause of the
free model's gate is evaluated on a named field of a committed output file,
and the counts behind the new gate line recompute from independent code.**

## What I will do, in order

1. **List every clause of arm F's gate as version 5 states it.** Sources:
   section 8.1 (the gate on learning), section 8.2 (the channel-removal check),
   section 5.4 (what arm F must pass before it is read), section 7.4 (what is
   frozen), section 7.5 (the reporting table), the section 9 rows for the gate
   and the channel-removal check, and section 3's rule that a seed counts only
   if it passes everything. Each clause is quoted with its line number and
   given a short plain name.

2. **For each clause, find the field the code reads.** Read `measure.seed_gate`,
   `measure.withhold`, `measure.arm_outcome` and `procedure.gate`, name the
   field of the gate row each clause is judged on, and show, by a script that
   lists the field's presence and values, that the field exists in committed
   output files: the decision-procedure cases in
   `experiments/08-successor-degree/out-a2-cases/`, the toy's rows beside them,
   and the development and pipeline-test rows. I will say plainly which of
   those files were written by the gate code itself and which were made up by
   hand from other records (the cases are built by `tests/a2_cases.py` from
   the toy's rows with fields changed).

3. **Recompute the counts behind the gate line with independent code.** A
   script of my own, which does not import `measure.py`, `procedure.py` or the
   rehearsal's `lesion_content_check.py`:
   - (a) derives both lines (790 for learning, 1,546 for the ownership-free
     line) from the exact binomial tail with integer arithmetic, not scipy;
   - (b) reads every committed arm F row and judges each clause from the raw
     counts by the text's rule, then compares my per-seed states and my
     arm-level result with what the code wrote in each case's `summary.json`;
   - (c) compares the candidate counts written into the made-up cases with the
     committed rehearsal record they were copied from
     (`experiments/rehearsal-successor-measure/out-lesion-content-check/lesion_content_check.json`);
   - (d) recomputes the candidate counts themselves from the twelve committed
     toy models of arms T, C, M and F
     (`experiments/rehearsal-successor-measure/out-repairs/models/`, checked
     against `SHA256SUMS`) on the 3,000 gate episodes. For this part I use the
     project's episode generator and model definitions (`grammar.py`,
     `models.py`) as the instrument, because rewriting the network is not a
     check of the gate, but I build the four candidates from the token
     sequence itself (reading the item on the action turn and the four values
     assigned to it), not from the generator's stored values or from the
     code's `candidate_ids`.
   - (e) runs the main line's own `procedure.gate` on the same twelve models,
     so that the code's figures come from the code under check and not from a
     copied record, and compares them field for field with (d) and with the
     rehearsal record.

4. **Check the text and the code agree, clause for clause:** the comparison
   used (at least, or below), the line, which condition is gated and which
   only reported, which arms the clause applies to, and how seeds are counted.

## What would make the verdict "not closed"

- A clause of arm F's gate with no field the code reads, or a field that is in
  no committed output file.
- Any recomputed count, line or per-seed state that differs from the code's.
- A clause the text states one way and the code evaluates another way.
- A sentence in the text that still sets a condition on something the task
  does not produce. (The search for "batter" is a way to find candidates, not
  the test; each hit is read.)

A difference that does not change any decision but leaves a claim in the text
unsupported would make the verdict "closed with named conditions".

## What I did not open

No chat history, no uncommitted files from the shared checkout. The earlier
check of the drafted repair (pull request 96, the dispositions check) did its
own independent recount; I read its result lines to know what it found, but my
script is written from the text and the token format, not from its code.

## The parallel change

Another session is changing `measure.py` and `procedure.py` on branch
`ruled-code-changes-2026-10-09`: the fitting limit, the outcome wording, and
the summary's wording when fewer than three seeds are present. I check main as
it stands, and the findings say which parts of the verdict that change could
reach.
