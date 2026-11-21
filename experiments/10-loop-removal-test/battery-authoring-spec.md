# The loop removal test: authoring specification for its task batteries

*Written 2026-11-21 and committed before any content list, generator or item exists. This is step 3 of
section 9 of the design (`docs/loop-removal-test-design-2026-11-20.md`, version 0.8, commit 38148b1).
The design was cleared for this step by its eighth closure check
(`docs/reviews/2026-11-21-loop-removal-test-design-v0.8-closure-check-claude-code.md`). Every rule here
follows a section of the design, and the section is named beside the rule. Where this specification
settles a point the design left to it, it says so. That covers the eighth check's findings RT-409 to
RT-414, and the region map that RT-396 requires.*

*The model's tokeniser is the research model's own, from `.hf-cache.nosync/tml-d24-varloop-research-tokenizer/`
at revision 657b53ba (`docs/2026-11-21-loop-removal-tokeniser-download.md`). Every token count here
means a count under that tokeniser. A count "at the answer position" means a count of the string with no
leading space, as it would follow the reply opening `<|message_model|><|content_text|>`. Step 4a has not yet
confirmed that opening. If it differs, section 9 of this specification applies.*

## 1. What is generated, and in what order

1. **This specification is committed.** Nothing else exists yet.
2. **The content lists and the region map are committed** in `experiments/10-loop-removal-test/data/`,
   together with the generator and the overlap check, before any item is generated (section 3).
3. **The pilot set is generated** from half A with seed 1 and committed in
   `experiments/10-loop-removal-test/batteries/pilot/`.
4. **The free step-3 checks are run** on the pilot with the real tokeniser, and their findings are committed
   (design, section 9, step 3).
5. **The test set is generated only after the registration commit,** from half B, with a seed written in
   the registration. It is not generated now.

## 2. The halves

- **One fixed split.** Every content list is split into half A (pilot) and half B (test) once, by a
  shuffle with seed 0, which is fixed here and used for every list. An odd item goes to half B.
- **What is split.** Countries, adjective pairs, everyday objects, three-letter words, the syllables that
  build invented words, and the neutral passages. Operands and unit factors are not drawn from lists.
  Instead, they are split by numeric range (section 4).
- **What is shared.** The eleven colour names and the operator symbols are one shared pool, used by both
  halves (design, section 5, RT-383, RT-396). The fixed final questions and the rule wordings are the
  same in both halves.
- **Wrong answers** for a test item are drawn only from half B's lists, except colours (design, section 5,
  RT-341, RT-396).

## 3. The content lists (design, section 5)

Each list is a JSON file in `data/`. Every entry is checked for the single-token rule at generation, and
entries that fail are left out and counted (design, section 5, "Every candidate is a single token").

- **`countries.json`.** Countries with their capital and a region tag from the region map. Countries whose
  name contains its capital's name, or the other way round ("Tunis" and "Tunisia"), are marked, and their
  capitals are never used as right answers (design, section 5, copying rule).
- **`regions.json`, the region map** (RT-396). It names each region and, for each, its nearest
  neighbouring region. Wrong capitals are drawn in this order: neighbouring countries are not modelled,
  so the first source is the same region, then the nearest neighbouring region. An item for which four
  single-token wrong capitals cannot be found in that order is dropped. The counts of items served by the
  same region, by the neighbouring region, and dropped are reported at step 3.
- **`opposites.json`.** Pairs of common adjectives that are each other's opposites. No prefix opposites
  ("happy" and "unhappy"), and no word that sits in two pairs ("light" with "dark" and with "heavy")
  (design, section 5, RT-407). Each pair gives two questions, one for each direction. A question counts
  once.
- **`objects.json`.** Everyday objects with one typical colour, and the other colours each is commonly seen
  in. No object whose typical colour differs by country. The colour word never appears in the object's
  name (design, section 5, RT-384). Other common colours never appear among an object's wrong answers.
- **`words3.json`.** Common three-letter English words, each with three different letters (design,
  section 5, RT-372).
- **`colours.json`.** The eleven basic colour names: black, white, red, green, blue, yellow, orange, brown,
  pink, purple, grey. Shared by both halves.
- **The syllables** that build invented words are those of the split test's `batteries.py`, `SYLL_A` and
  `SYLL_B`, each split into halves. An invented word is one syllable from each list.

**How the lists were written, and what that means.** The lists were written by the author from general
knowledge, on 2026-11-21. Before the registration, the countries and capitals list is checked against a
public source a reader can open, such as the United Nations' list of member states and the Wikipedia list
of national capitals, and any correction is committed with its source. The model's own baseline checks
(design, section 5) also drop any item the model does not answer right, so an error in a list cannot
enter the scored set as a right answer the model rejects. It could still enter as a wrong candidate, which
is why the check against a source is owed.

## 4. The rule kinds (design, section 5, "The kinds, rebuilt for no written reasoning")

Each rule is stated in the shared context, followed by its facts. The wordings below are fixed.

- **`p_operator`.** Rule: "In this puzzle, a {sym} b means {expr}." The shapes of {expr} are "2 times a, plus b",
  "a plus 2 times b", "3 times a, minus b" and "a times 2, minus b, plus 1", each written in words. Facts:
  "Here a is {a} and b is {b}." The operands come from half A's range 2 to 15, or half B's range 25 to 99.
  The answer must lie between 10 and 999, and an item whose answer falls outside that range is redrawn
  (design, section 5, RT-399).
- **`p_unit`.** Rule: "In this puzzle, 1 {u1} is {k} {u2}." Facts: "You have {n} {u1}s." The answer is k × n.
  Half A uses k from 2 to 5 and n from 2 to 9. Half B uses k from 6 to 9 and n from 11 to 99. The two units
  are invented words.
- **`p_code`.** Rule: "In this code, each letter stands for another: " followed by eight rows of the form
  "{c} stands for {p}", in shuffled order. Facts: "The coded word is {cipher}." The plain word is a
  three-letter word from the half's list. Five extra rows are chosen so that at least four other
  three-letter words from the half's list can be spelled using only the table's plain letters. Those words
  become the wrong answers (RT-372). No code letter is the same as its plain letter. The coded string is
  never a candidate.
- **`p_lookup`.** Rule: "In this table, each name has a colour: " followed by six rows of the form
  "a {name} is {colour}", with six different colours from the shared list. Facts: "The name to look up is
  {name}." The wrong answers are four of the other five colours in the table (design, section 5, RT-377).
  Every table has six entries, at the pilot and at the test (RT-398).

## 5. The routine kinds (design, section 5, "The routine kinds, enlarged")

The routine fact is one sentence, and the routine question is fixed (section 6).

- **Sums.** Fact: "The two numbers are {a} and {b}." with a at most b. Half A uses answers below 50, and
  half B answers of 50 to 99. Wrong answers are within 5 of the right one, with the same number of digits.
- **Products.** Fact as for sums, with a and b from 2 to 12, a at most b. Half A uses answers below 40,
  and half B answers of 40 or more. A multiplication counts once (RT-407). Wrong answers are other
  products from 2 to 144, within 12 of the right one, with the same number of digits.
- **Capitals.** Fact: "The country is {country}." Wrong answers: section 3, `regions.json`.
- **Opposites.** Fact: "The word is {word}." Wrong answers are the opposites of other adjectives in the
  half's list.
- **Everyday colours.** Fact: "The object is {object}." Wrong answers are colours from the shared list
  that are neither the object's typical colour nor one of its other common colours.

**The cap and the exclusions** (design, section 5).
- **The cap.** No routine kind makes up more than 25% of the routine cell.
- **The exclusions.** The arithmetic rules (operator, unit) are never paired with sums or products. The
  letter code is never paired with opposites. The lookup is never paired with everyday colours.
- **The order of allocation.** Pairs are allocated to pairings after the cap and the pool sizes are
  applied, and then as evenly as possible across the allowed routine kinds of each rule kind.

## 6. The shared context and the fixed final questions (design, section 5)

**The context.**
- **Its parts.** An item's context is the rule, then the rule's facts and the routine fact in one of two
  orders.
- **The order.** In each group of rule kind and routine kind, half the pairs, chosen by the seed, put the
  rule's facts last, and the other half put the routine fact last. An odd pair's order is set by the seed
  (RT-394).
- **The final question.** It follows the context after one space.
- **The twins.** The prompt-rule item and its routine twin carry the identical context, and they differ
  only in the final question.

**The fixed final questions**, one wording on each side for each pairing, from the design's table and
recounted with the real tokeniser before this specification was committed:

| Pairing | Prompt-rule question | Routine question | Tokens |
|---|---|---|---|
| operator, capitals | What does the rule give for them? | What is the capital of the country? | 8 |
| operator, opposites | What does the rule give for them? | What is the opposite of the word? | 8 |
| operator, everyday colours | What does the rule give for them? | What colour is the object most often? | 8 |
| unit, capitals | How many of the second unit is that? | What is the capital city of the country? | 9 |
| unit, opposites | How many of the second unit? | Give the opposite of the word. | 7 |
| unit, everyday colours | How many of the second unit is that? | Usually, what colour is the object? | 9 |
| letter code, sums | What word is the coded word here? | What is the sum of the two numbers? | 9 |
| letter code, products | What word is the coded word? | What do the two numbers multiply to? | 8 |
| letter code, capitals | What word is the coded word? | What is the capital of the country? | 8 |
| letter code, everyday colours | What word is the coded word? | What colour is the object most often? | 8 |
| lookup, sums | What colour does the table give the name? | What is the sum of the two numbers? | 9 |
| lookup, products | What colour does the table give the name? | What is the product of the two numbers? | 9 |
| lookup, capitals | What colour does the table give the name? | What is the capital city of the country? | 9 |
| lookup, opposites | What colour does the table give the name? | What is the opposite of the given word? | 9 |

Results for each routine kind are also reported by wording (RT-397).

**The chat format.** Each item is rendered with the research model's chat template, with the reasoning
setting "none", as one user message. The reply opening is taken to be `<|message_model|><|content_text|>`,
followed directly by the candidate. Section 9 applies if step 4a finds otherwise.

## 7. Candidates (design, section 5)

- **Five per item.** Each item has the right answer and four wrong ones, all single tokens at the answer
  position.
- **The copying rule** (RT-385, RT-395). It works on whole content words of the routine fact and the final
  question, ignoring the rule's text. No candidate in either cell may contain, or be contained in, such a
  word. Numbers are exempt.
- **The cross-cell rules** (RT-395).
  - The routine twin's right answer is never one of the prompt-rule item's candidates.
  - The prompt-rule item's right answer is never one of the routine twin's candidates.
  - The value the rule would give if applied to the routine question is never one of the routine twin's
    candidates. This applies where it can be computed, that is, an operator or unit rule applied to the
    routine fact's numbers. The exclusions already keep arithmetic rules away from number facts, so in
    practice it never fires.
- **The order of the candidates** is shuffled with the item's seed.
- **The without-rule version.** Each prompt-rule item also carries a version with the rule sentence
  removed, for the "rule is needed" check (design, section 5).
- **The two baseline variants** (RT-393, RT-402).
  - Each routine twin carries a variant with only its routine fact and final question.
  - Each prompt-rule item carries a variant with only the rule, its facts and its final question.

## 8. Donor-only pairs (design, section 3)

- **Built like scored pairs.** They come from the same half, and are kept only for their unaltered runs.
- **They may reuse content.** They may reuse any routine question, rule content or invented word from the
  half (RT-403). They sit outside the no-reuse rule, the pool budget and the cap.
- **Never a copy of their own recipient** (RT-412). A donor-only pair is never kept as a donor for a
  recipient whose rule content (the rule sentence and its facts) or routine fact it repeats.
- **Aimed** (RT-404). A candidate donor-only pair is kept only if it is an eligible donor for at least one
  scored pair in its group that still has fewer than five eligible donors.
- **Eligibility.**
  - Length: each of the donor pair's twins is at least as long as the matching recipient's prompt plus one
    token.
  - Answers: neither twin's right answer is among the matching recipient twin's candidates.
  - Groups: donors come from the same group of rule kind and routine kind.
- **The draw budget** (RT-409).
  - **The limits.** Drawing in a group stops at whichever comes first:
    - every scored pair has five eligible donors;
    - the group holds three times as many donor-only pairs as scored pairs;
    - 200 draws have been made per scored pair in the group.
  - **What is reported.** For each group: the draws made, the donor-only pairs kept, and, for each scored
    pair left with no donor, its content and its place by length within its group.
- **Never scored.** Donor-only pairs are never scored. The overlap check counts them with the set they serve
  (RT-403).

## 9. If step 4a finds a different reply opening (RT-400)

If step 4a finds that the tokens before the answer differ from `<|message_model|><|content_text|>`, the
single-token counts, the pools and the pilot are rebuilt under the true opening, and the step-3 checks are
run again, before any pilot item is scored.

## 10. The pilot set (design, section 5, "The pilot's size")

The pilot set is generated from half A with seed 1. It holds:
- **Scored pairs.** 120, with 30 for each rule kind.
- **Donor-only pairs.** As many as section 8 adds.
- **Chained-lookup items.** 40 of them. Each gives chains of two to six lookups through invented tables,
  with five colour candidates.
- **Neutral passages.** Half A's 200, rendered in the chat template. The first 100 build the average and the
  other 100 measure its damage (design, section 3).

**The neutral passages** are ordinary prose made by joining common sentences from a fixed list, with
lengths spread from the shortest to the longest scored item. They are split into halves like everything
else.

## 11. The overlap check (design, section 5, "Pilot and test are kept apart")

`src/check_overlap.py` fails if any of these holds:
- **Words in both halves.** Any country, adjective, object, three-letter word or syllable appears in both
  halves of its list.
- **Answers in both halves.** Any answer value of a kind is possible in both halves of that kind. This is
  checked within each kind, from the numeric ranges and the lists. Colours are exempt.
- **A test candidate from half A.** Any test item's candidate comes from a half-A list, colours excepted.
  This is checked once a test set exists.
- **A donor-only pair from the other half.** Any donor-only pair uses content from the other half.

Now, with no test set generated, the check runs on the lists and the ranges. It runs again on the test set
after registration.

## 12. The free step-3 checks (design, section 9, step 3)

`src/step3_checks.py` runs on the pilot and reports:
1. **Single-token counts** for every list, and the entries dropped.
2. **The fixed-wording table recount.** Every row must match.
3. **Twin lengths.** In every pair, the two twins must have the same token length.
4. **Generation drops by kind.** The equal-length and single-token drops, and the spread of right answers.
   For capitals, the spread by region and the counts served by the same region, by the neighbouring region,
   and dropped.
5. **Donors.** Eligible donors per scored pair by group, the donor-only pairs added, and the scored pairs
   left with no donor, with their content and their place by length (RT-409).
6. **The stand-in dose ratio** per rule kind at weights 0, 0.3 and 0.6, against the band of 0.95 to 1.05 at
   0.3 and 0.90 to 1.10 at 0 and 0.6. A correct build gives about 0.99 to 1.03 (design, section 9).
7. **The tail shares** per rule kind, and the difference in real distance per position that step 4b's 10%
   limit can absorb (RT-391).
8. **The average-method estimate.** Per rule kind, each cell's count of final-question tokens and of
   invented-word or symbol tokens, which should be equal within one token per item (RT-387).
9. **Candidate words in donors' contexts** (RT-411). Per kind and cell, how often a donor's context names
   the recipient's right answer, and each wrong candidate.
10. **The average is defined at every position.** For every position of every pilot item, candidates
    included, there must be a slot average or a text average from the neutral set (design, section 3,
    RT-335 condition 3).

The findings are committed as `experiments/10-loop-removal-test/step3-findings-2026-11-21.md`. **What these
checks cannot do:** they check that the generator builds what the design describes. They cannot forecast
RT-345, the finding that the swap's dose differs between the cells, which only step 4b can measure
(design, RT-391).

## 13. Settled here for the eighth check

- **RT-409, the draw budget:** section 8.
- **RT-410, the ceiling:** about 255 to 285 pairs on the stated pools. The pilot needs 120, and the expected
  test size of 120 to 200 fits. The design's storage and run-count figures that are pegged to 300 pairs are
  read as upper bounds.
- **RT-411, colours named in donors' tables:** reported per kind (section 12, item 9). The lookup case is
  noted beside the reading with lookup left out at step 4b.
- **RT-412, donors copying their own recipient:** barred (section 8).
- **RT-413, wording faults:**
  - "a fifth of a kind" in the design's pilot paragraph means "a fifth of a pairing's pairs that pass the
    confidence check";
  - the ruling note's "these quotations" refers to the option wording, whose source is the session;
  - the cost sentence's figure of donor-only pairs per scored pair is replaced by section 12's measured
    count.
- **RT-414, the capitals-out reading:** any outcome A, wherever its sentence is used (STATUS.md, the site,
  public summaries), carries two readings beside it. One is its reading with the capitals pairs left out.
  The other is, at the smaller sizes, the sentence about the small leak of RT-371 (design, section 6). This
  is to be written into the design's section 7 at its next version.
- **RT-396, the region map:** section 3, `regions.json`.

## 14. Amendments after the independent check (2026-11-21)

*Added 2026-11-21, before the generator was changed. The independent check
(`independent-check-2026-11-21.md`) reproduced the pilot exactly. It found four faults that must be fixed
before step 4b, and they are fixed here first and then in the code. Where this section and an earlier one
differ, this section governs. The pilot generated from commit c02b763 is replaced by one generated from
the amended code.*

1. **The chained lookups** (RT-415, RT-426). Section 10's chained items are rebuilt.
   - **Each item has five chains.** The target chain runs from a start name, through "X points to Y"
     rows, to a colour row, "Z is colour". The other four chains are built the same way, each ending in
     one of the other four candidate colours.
   - **Chain lengths.** The target chain has two to six steps, as before. Each distractor chain's length
     is drawn independently from two to six.
   - **No name is shared** between chains in an item, and all rows are shuffled.
   - **What this fixes.** Every candidate colour then appears in the text, and every colour is reached by
     some chain. So the answer cannot be found without following the chain from the start name.
   - **Donors** (new; the specification was silent). A chained item's donor is another chained item of the
     same number of steps. It must be at least one token longer than the recipient's prompt, and its right
     answer must not be among the recipient's candidates. Donor-only chained items are added on the rules
     of section 8: aimed, with a budget of 200 draws per scored chained item, up to three times the scored
     count. They are reported the same way.
2. **Where the right number sits** (RT-416). For every numeric kind (operator, unit, sums, products), the
   right answer's place among the five candidates, in numeric order, is drawn uniformly from the five places
   first. The four wrong numbers are then drawn below and above it to fit, within the kind's spread and with
   the same number of digits. An item whose drawn place cannot be filled is redrawn. Step 3 reports the
   count of right answers at each place, by kind.
3. **The copying rule ignores only function words** (RT-418). Section 7's rule works on the content words
   of the routine fact and the final question. The words it ignores are only these: a, an, the, is, of, and,
   to, do, does, that, what, how, many, for, them, it, in, this, each, be. Every other word of three or more
   letters is a content word, including "capital", "colour", "opposite", "sum", "give", "word", "country"
   and "object".
4. **The order of an odd group's extra pair** (RT-422). In a group with an odd number of pairs, the extra
   pair's order is drawn from the seeded stream, not fixed. This is what section 6 already says.

The other findings of the independent check concern the test set, the lists, the overlap check or the
wording of this specification. They are carried to the roadmap, and are not settled here.

## 15. A scoring trial: the answer-only instruction (2026-11-21)

*Added 2026-11-21 on John's choice ("Answer-only instruction"), before any code for it was written. Step 4a
(`step4a-findings-2026-11-21.md`) found that the model, when its answer is forced as the first token of its
reply, is near chance on many kinds of task. The model always starts its own replies with written reasoning.
This section sets out a trial of one remedy. It is a trial on the pilot only. It changes nothing in the
registered design unless John rules so afterwards.*

1. **The instruction.** One fixed sentence is added to every item: "Answer with the single word or number
   only." (9 tokens, with a leading space, under the model's tokeniser). The two twins of a pair carry it
   word for word, so their lengths stay equal, and every donor carries the same sentence in the same place.
2. **Two placements**, each a separate trial set, because where an instruction sits can matter:
   - **"end":** after the final question, as the last sentence of the user's message;
   - **"start":** before the rule, as the first sentence of the user's message.

   The "end" placement lengthens the tail after the shared context by 9 identical tokens in both cells. The
   "start" placement leaves the tail as it was.
3. **What does not change.** Everything else stays as in sections 1 to 14:
   - the same half A, seed 1 and generator;
   - the same forced reply opening, `<|message_model|><|content_text|>`;
   - the same single-token candidates, scored at the first answer position.

   The chained lookups carry the instruction in the same place. The neutral passages are unchanged.
4. **What the trial measures,** on each trial set and on the original pilot for comparison, all at 16-bit as
   in step 4a:
   - **accuracy** at 1, 2 and 3 passes, by kind;
   - **the share of items passing the confidence filter** at three passes: a margin of at least 2.2 between
     the right candidate and the best wrong one;
   - **the bites figure:** the one-pass loss on chains of four to six steps, against three passes.

   These are descriptive pilot figures for John's choice of scoring method. No outcome is read from them, and
   no threshold is set from them.
5. **What would count as a working fix,** stated now, before the run:
   - at three passes, routine twins reach at least 80% accuracy;
   - at least half of all pilot items pass the confidence filter;
   - chained lookups of four to six steps reach at least 50% at three passes.

   If neither placement meets all three, the trial reports that, and the next choice goes to John, for
   example option (b), a fixed lead-in, or (c), scoring a reasoned answer.
