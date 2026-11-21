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
