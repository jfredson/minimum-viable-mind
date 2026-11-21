# Ruling, 2026-11-21: whether the loop removal test goes ahead, and its five choices

*Recorded 2026-11-21 by the session that wrote the design. Authorship is mixed. The design recommended
an answer to each question, and John chose that answer in every case, picking among offered options in a
question form in the session. TimeAssembler worklog decision entry "John rules the loop removal test's
five choices, and paper work only for now (2026-11-21)".*

**John's answers**, 2026-11-21, given as the options he picked. Each question was put in the words shown
in section 10 of `docs/loop-removal-test-design-2026-11-20.md`, version 0.4 (commit ddc5031). The design
had been cleared for these rulings by the closure check of version 0.4
(`docs/reviews/2026-11-20-loop-removal-test-design-v0.4-closure-check-claude-code.md`), with RT-345, the
finding that the swap's dose differed between the two task groups, carried as an open fatal item.

**Whether the test goes ahead.** John picked "Yes, paper work now". The design work continues at no cost
before the project's pause from 2027-01-04. That covers:
- version 0.5;
- the battery specification;
- the free check with the model's real tokeniser at step 3.

Any step on a rented machine still comes to John first, with a price and a ceiling. Treating the test as
a live experiment to rehearse and run, rented steps included, was offered and not chosen.

**The five choices:**

1. **Scoring.** John picked "Five options". Each answer is scored by which of five fixed candidates the
   model rates most likely, not by a generated answer, because the swap needs every position of the
   answer known in advance.
2. **No written reasoning.** John picked "No written reasoning". Answers are scored straight after the
   prompt. A run that allows reasoning may be added later as a separate, descriptive condition.
3. **Routine twins.** John picked "Twins". Each routine question carries its rule-following partner's
   invented rule as a preamble, so that both groups have the same length and layout. He was told the
   cost in the question: the routine group then measures a practised answer given while ignoring a rule.
   He was also told that the latest check found the twins still do not get an equal swap. The dose
   question is to be settled by the free check with the real tokeniser before any rental.
4. **Second model.** John picked "Add it, descriptive". Inkling 2 Mini is added as a second model. It is
   reported with the same statistics, labelled descriptive, with no outcome of its own, and always noted
   as sharing pretraining with the main model.
5. **If the averaging method fails.** John picked "Stop the test". If both versions of the averaging method
   (the pooled average, then the ten-bin fallback) differ from the swap's damage by more than a factor of
   two, the test stops. It does not rest on the swap alone.

**What still comes back to John first:**
- any download beyond the tokeniser (the tokeniser itself comes as a file action first);
- any spending, including any rented machine;
- the registration itself;
- any merge that deploys the site.

---

*Dated note, added 2026-11-21 after the design's sixth closure check
(`docs/reviews/2026-11-21-loop-removal-test-design-v0.6-closure-check-claude-code.md`, finding RT-401).
John's answers above are unchanged. Two things in this record need correcting.*

- **The wording John saw.** The record says each question "was put in the words shown in section 10" of
  version 0.4. That is true of the questions. The options John picked from, though, carried their own
  descriptions in the session's question form. For choice 3, the option "Twins (Recommended)" read: "Keep
  the twin design and settle the dose question with the free real-word-splitter check before any rental."
  Section 10 of version 0.4 said instead that the dose question was "first estimated for free at step 3
  and then measured on the model at step 4b".
- **A premise that no longer holds.** Under the design's version 0.5 and later, the free check passes by
  construction and settles nothing about the real dose. The dose question is first answered at step 4b,
  on a rented machine. The substance of choice 3, routine twins, is kept. John was told of this in the
  session on 2026-11-21. That telling is also recorded in the TimeAssembler worklog entry "Loop removal
  test: the fifth check confirms the shared-context fix with the real tokeniser, but finds the free check
  can no longer settle the dose question", and in section 11 of the design.
