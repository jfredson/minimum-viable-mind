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

## 16. Redesigning the chained lookups: a calibration trial (2026-11-21)

*Added 2026-11-21 on John's choice ("Redesign the lookups"), before any code for it was written. The scoring
trial (`scoring-trial-findings-2026-11-21.md`) found that the answer-only instruction makes the paired
questions work, but that the chained lookups stay at chance in every version, even at two steps. The bites
check (design, section 5) cannot be met while that is so. This section sets out a trial of easier chained
lookups. It is a trial on half A only. It changes nothing in the registered design unless John rules so
afterwards.*

1. **What is kept.** The task stays the one the design names: follow a chain of lookups in a shuffled list
   to a colour, with five colour candidates, scored as the first token of the reply. These rules of section
   14, item 1 are kept:
   - every candidate colour appears in the text and is reached by some chain, so the answer cannot be found
     without following the chain from the start name;
   - no name is shared between chains, and all rows are shuffled.
2. **What is varied: two things, each with two settings, so four versions.**
   - **The names.** Either the invented names used so far (two syllables, such as "pashnix", several tokens
     each), or common English nouns of one token each, from a new list (`data/chain_names.json`). The new list
     shares no word with any other list, and is split into halves with seed 0 like every list. A model can
     hold a one-token familiar word more easily than a run of invented syllables, so this is the likelier fix.
   - **The other four chains.** Either the length drawn from two to six as now, or one step each ("X points to
     Y; Y is red"). Short distractor chains make the list much shorter while keeping every candidate in the
     text.
3. **The instruction.** Every version carries the answer-only instruction at the start of the message, the
   placement that leaves the tail after the shared context as it was (section 15, item 2). Which placement
   the test uses is still John's to rule; this only fixes the trial.
4. **The size.** 16 items per target length from two to six steps, so 80 items per version, 320 in all. That
   doubles the scoring trial's count per length, which had only 8. The same half A and seed 1 are used,
   with each version drawn from its own random stream (seed 1 plus the version's number), so the versions do
   not share draws. No donors and no neutral passages are built, because the trial does no swap.
5. **What the trial measures,** at 16-bit, on each version: accuracy at 1, 2 and 3 passes by target length,
   and the one-pass loss (three passes minus one pass) on chains of four to six steps.
6. **Which version is chosen,** stated now, before the run. A version qualifies if, on chains of four to six
   steps:
   - it is right on at least 50% at three passes; and
   - three passes beat one pass by at least 0.15 in accuracy. This is the bites check's own size, used here
     as a plain accuracy difference on pilot items. The real check is made later on the normalised scale on
     half B, so choosing on half A does not decide it.

   Among the versions that qualify, the one closest to the current task is chosen, in this order: invented
   names with full-length distractors (the current task), invented names with one-step distractors, one-token
   names with full-length distractors, then one-token names with one-step distractors. Each step down the
   order moves further from the task the design names, so the least change that works is preferred.

   If no version qualifies, the trial reports that and the next choice goes to John. The options then
   include requiring only three steps or more for the bites check, which would change the design.
7. **What is checked for free,** before anything is rented:
   - every name and colour is one token where the version says so, and every candidate is one token;
   - in every item, each of the five candidates ends a chain, each chain's length is as drawn, and no name
     appears in two chains;
   - the new name list shares no word with the other lists;
   - the prompt lengths, by version and target length, are reported.

## 17. The rebuild for design version 0.12 and John's choices 6 to 8 (2026-11-21)

*Added 2026-11-21 on John's instruction ("Yes, write it"), before any code for it was written. It rebuilds
the specification for design version 0.12 (`docs/loop-removal-test-design-2026-11-20.md`) and John's
rulings on choices 6 to 8 (`docs/rulings/2026-11-21-loop-removal-test-choices-6-to-8-ruling.md`). It
settles the seven points the closure check of version 0.12 left for the specification (RT-466 to RT-472).
Where this section and sections 1 to 16 differ, this section governs. The chained lookups of sections 10
and 14 are no longer built: the bites check uses held-out rule problems (item 5). Sections 15 and 16
describe trials and stand as a record.*

1. **The rule kinds** (choice 8). Three: operator, unit and lookup. The letter-code kind is not built. The
   pairings allowed are unchanged for the three kinds:
   - operator and unit pair with capitals, opposites and everyday colours;
   - lookup pairs with sums, products, capitals and opposites.
2. **The pilot's pairs.** 120, 40 for each rule kind, under the 25% cap on each routine kind (30 of 120):

   | Rule kind | Capitals | Opposites | Everyday colours | Sums | Products |
   |---|---|---|---|---|---|
   | operator | 13 | 13 | 14 | | |
   | unit | 14 | 13 | 13 | | |
   | lookup | | | | 20 | 20 |

   So the routine cell holds 27 capitals, 26 opposites, 27 everyday colours, 20 sums and 20 products. The
   lookup kind takes only sums and products because operator and unit can take nothing else, and the cap
   is then met by every routine kind. The test half uses the same shares at the size step 4b's simulation
   sets.
3. **The instruction** (choice 6). "Answer with the single word or number only." goes at the start of the
   user's message in every scored item, donor-only item and bites item, before the rule. The neutral passages
   carry none (design, section 5). The generator's `--instruction start` builds this. The build report names
   it.
4. **The numbers, and the split between halves** (design version 0.12, section 5; RT-460, RT-468). Four
   numeric kinds share one range in both halves. Every right answer has two digits.
   - **The pools.** A kind's pool is every item it can make in that range:
     - **Operator:** every rule shape (four of them) with operands a and b from 2 to 15 whose answer has two
       digits. The answers run from 10 to 45 (RT-468; version 0.12 said 49).
     - **Unit:** every factor k from 2 to 9 with every count n from 2 to 12 whose product has two digits.
     - **Sums:** every pair of operands a ≤ b, from 2 to 49, whose sum has two digits. The answers run from 10
       to 98.
     - **Products:** every pair a ≤ b, from 2 to 12, whose product has two digits.
   - **The value split.** For each kind, the answer values are dealt decade by decade (10 to 19, 20 to 29, and
     so on), in order, with a random stream seeded by the kind's split seed:
     - The value ending in 0 goes to one half, and the value ending in 5 to the other. Which half gets the 0
       alternates from one decade to the next, starting with a half drawn from the stream. If a decade holds
       only one of the two, that one goes to the half due the 0.
     - The values ending in 2, 4, 6 or 8 present in the decade are shuffled and dealt alternately to the two
       halves, starting with a half drawn from the stream. The values ending in 1, 3, 7 or 9 are dealt the same
       way. So in a full decade each half gets two of each.
     - **Short decades** (RT-468): the operator's forties hold 40 to 45, and the sums' nineties hold 90 to 98.
       Their values are dealt by the same rule, which leaves the halves at most one value apart in each group.
   - **The tolerances are on the pools** (RT-468). Each half's pool is the items of the kind whose answer is in
     that half. The pools are fixed before any item is drawn and do not depend on the generator's draws, so
     the seed chosen cannot be tuned to a particular pilot. Within each kind, a split is accepted only if:
     - the shares of pool items whose answer ends in 0 differ between the halves by at most 0.05, and
       likewise for answers ending in 5;
     - the mean answers of the two pools differ by at most 2;
     - the shares of even operands (both operands of each item counted) differ by at most 0.05;
     - for the unit kind and products, the number of distinct facts (item 6) in the smaller pool is at least
       80% of the larger.

     The same figures are also computed on the drawn pilot items and reported beside the pool figures, as a
     description.
   - **The seed rule.** For each kind, split seeds are tried from 1 upward. The first that meets every
     tolerance is used. Seeds are tried up to 1,000; if none meets them, the design returns to John. All of
     this uses the lists only, never the model. The seeds and every figure are written into the build
     report.
   - **How items are drawn.** Each item is drawn uniformly from its half's pool, so that the drawn items follow
     the pool the tolerances were checked on. The right answer's place among the five candidates is drawn
     first, as before (section 14, item 2). The wrong answers lie within five of the right one, and within 12
     for products, with the same number of digits. Wrong answers may come from the other half's values
     (design, RT-452).
5. **The bites items** (design version 0.12, section 5). 80 in the pilot:

   | Rule kind | Capitals | Opposites | Everyday colours |
   |---|---|---|---|
   | operator | 13 | 13 | 14 |
   | unit | 13 | 14 | 13 |

   - **How each is built.** It is built as the prompt-rule side of a pair: the instruction, the rule
     sentence, the shared context with its routine content, and the prompt-rule question. Its routine twin
     is not kept. Routine content may repeat routine questions already used.
   - **What it may not repeat.** A bites item may not repeat a scored pair's or a donor's whole content,
     meaning its rule content and its routine content together. No two bites items share a rule content.
   - **Donors.** Each bites item gets donors among bites items of the same rule kind and routine kind. A
     donor must be at least one token longer than the item. Its right answer must not be among the item's
     candidates. It must not share the item's rule content.
   - **Donor-only bites items** are added on the terms of section 8. They are aimed at items short of five
     donors, with a budget of 200 draws per item and a cap of three times the scored count.
6. **What a fact is** (RT-469). For the unit kind, a fact is the unordered multiplication of the factor and
   the count, so "1 X is 3 Ys; you have 7 Xs" and "1 X is 7 Ys; you have 3 Xs" share a fact. For products
   too, a fact is the unordered multiplication. The design resamples by fact in the unit kind only. A unit
   of resampling there is every pair and every bites item that uses the fact. The unit pool holds 81 items,
   which make 55 facts. Step 3 reports each half's count of facts and how often each is used.
7. **The change ratio** (RT-466). The design's definition is computed as follows.
   - **The swap.** For each donor, the positions run from the first position where the item's and the
     donor's prompts differ, through the answer position. The item's change ratio under the swap is the
     mean of its five donors' ratios, each computed over that donor's positions.
   - **The average.** The average method has no donor. It replaces the sums at every position of the item's
     text span, so its positions are those positions plus the answer position.
   - **The two block sums.** They are weighted equally, as the design says. Each is also reported alone,
     because the readers draw mostly on block 3.
   - **What 0.5 means.** After both sums are scaled to a root-mean-square of 1, a ratio of 0.5 means a cosine
     of 0.875 between the true and the given sum. An average is likely to sit closer to most true sums than
     another input's sum does, so 0.5 is likely harder to clear under the average method. That is known
     now. Step 4b's return-to-John rule covers it, and the threshold is not changed after seeing results.
     Step 4b reports each method's mean, spread and distance from 0.5.
8. **How the analysis reads three outcome rules.** These are the specification's readings of the design's
   outcome rules. Each is marked for the registration review, which must adopt or reject it before
   registration.
   - **The disagreement rename** (RT-467). For the rename, "does not bite" means the removal's own-loss
     conditions only (conditions 1 and 2), without the change ratio. The rename catches a contradiction
     between losses: the pairs' operator and unit items lose while the held-out problems do not. Whether the
     message changed a lot does not bear on that contradiction. The design text gates it on all three
     conditions.
   - **F's per-kind rule** (RT-470). It applies only inside the no-excess branch, never to an A, B or C.
     There, if the own-loss condition holds pooled but not in one kind, two cases follow:
     - if that kind's point estimate is at or above a quarter of its one-pass cost, the outcome is
       **Depends on one kind**;
     - if its point estimate is below that but its interval reaches above it, the outcome is **Too weak to
       read**. Imprecision is not reported as a loss carried by one kind.

     If the simulation finds that no bites set the pools allow, up to 300 per kind, gives an 80% chance of
     "does not bite" in each kind, the design returns to John before registration.
   - **F's sentence and its gates** (RT-471). F's sentence says the removal cost neither cell of the pairs
     "more than δ beyond matched comparisons", which is what the cells' condition shows. Each bites kind's
     one-pass cost is reported, and F needs each kind's one-pass point estimate to be above zero, which its
     per-kind condition already implies. The pairs' own losses against the unaltered run are reported beside
     F as a description.
9. **Errors in the design's text, to be fixed in the registration text** (RT-472, and items found here). The
   design is closed, so its text is not edited for these. The registration text carries the corrections:
   - the old pair counts "196 to 220" and "196 to 236", which should read about 216 to 236;
   - the sentence on widening the unit range;
   - "serves as well" in the description of F, which should be "costs those problems little";
   - section 1's sentence that B and C need nothing from the bites check, which should name the narrowed
     rename;
   - the overstated reason under choice 6;
   - the pilot and test-half figures in choice 8, which carry no labels;
   - the operator's answers, which run 10 to 45, not 49.
10. **What step 3 runs and reports** for this rebuild, into `batteries/pilot-v0.12/`. The earlier pilot stays
    as a record.
    - The overlap check, rewritten for the split. It fails if:
      - any numeric right answer of a kind lies outside its half's values;
      - any operator content repeats across halves;
      - any non-numeric candidate comes from the other half's pools.
    - The free checks of section 12, for the three kinds, with the chained items replaced by the bites items:
      their counts, single-token candidates, donors and lengths.
    - The split report: each kind's seed, the pool and drawn-item figures for every tolerance, and the facts.

    Nothing is spent, and nothing goes to the model.

## 18. Fixes after the independent check of the rebuilt pilot (2026-11-23)

*Added 2026-11-23 on John's instruction ("Yes, fix it"), before any code for it was written. It answers the
independent check of the rebuilt pilot (`independent-check-pilot-v0.12-2026-11-21.md`). That check found the
pilot rebuilt byte for byte, and one serious problem: the drawn items do not follow the pools (RT-473). This
section governs where it differs from section 17.*

1. **The item is drawn first, then its place** (RT-473). Section 17, item 4 asked for two things that
   conflict at the edges of the range: items drawn uniformly from the half's pool, and the right answer's
   place among the five drawn first (section 14, item 2). An answer of 10 can only be the lowest of five
   two-digit numbers, so drawing the place first made edge answers about a fifth as common as the pool. The
   halves then drifted apart, as drawn, past three tolerances. From now on:
   - the item is drawn uniformly from the half's pool;
   - its place is then drawn uniformly among the places it can fill, given the wrong answers available
     within the kind's spread;
   - an item that can fill no place is redrawn, and the generator counts how often that happens.

   So the drawn items follow the pool on which the tolerances were checked. The places are no longer quite
   uniform for edge answers, and step 3 reports the place counts by kind, for the pairs and the bites items.
   Section 14, item 2's "place drawn first" is replaced by this. The split seeds are unchanged, because they
   depend only on the pools.
2. **The operator's no-reuse rule keys on the problem, not the symbol** (RT-475). Two operator items with
   the same shape and operands are the same problem, whatever symbol names the rule. Among the scored pairs,
   and among the bites items, no operator problem repeats. A bites item may still repeat a scored pair's
   problem, as the design allows.
3. **The bites items have their own random stream** (RT-476), seeded by the build seed plus 1,000, as the
   design asks. Changing the pairs then does not change the bites items.
4. **A bites item's discarded routine twin** (RT-477). The generator builds the bites item through the pair
   builder, so its routine twin is built and then discarded. That twin can still cause a candidate item to be
   rejected: when its length differs from the bites item's, or when a candidate clashes with the routine
   question. This is a small filter with no effect on the answer, and it is kept, so that a bites item has
   exactly the form of a pair's prompt-rule item.
5. **A bites donor may not repeat its item's routine fact** (RT-478), as for the pairs (RT-412).
6. **The lookup allocation, restated** (RT-481). The lookup kind takes only sums and products by choice:
   that keeps capitals and opposites, which the operator and unit kinds need, below the cap with room to
   spare, and it is stated here as a choice, not as something forced.
7. **The neutral passages reach the longest item** (RT-483, carrying RT-425). Their lengths are spread from
   the shortest to the longest of every item: the scored pairs, the donor-only pairs, the bites items and
   their donors. Each passage is built up to at least its target length, so the longest passage is at least
   as long as the longest item.
8. **Step 3 fails on any broken condition** (RT-474, RT-479). The step-3 script exits with a failure if any of
   these is broken:
   - the instruction starts every scored, donor-only, bites and bites-donor text, and no neutral passage;
   - only the three rule kinds are present;
   - every right answer, recomputed from the item's own content, matches the stated answer;
   - every candidate is one token;
   - all twins are of equal length;
   - no two bites items share a problem;
   - no bites item repeats a scored pair's or donor's whole content.

   It also reports:
   - the right number's place counts for the bites items, as well as for the pairs;
   - how often each fact is used;
   - why the drawing of donor-only bites items stopped.
9. **Settled before any test set, not now** (RT-480, RT-484). These two do not bear on the pilot:
   - the rule for the test half's shares above about 160 pairs, where half B's capitals and products run short;
   - the overlap check's comparison of objects, invented words, prompts and tables between pilot and test.

   They stay on the roadmap with the earlier open list checks (RT-417 and the others). The thin margin of
   the products seed (RT-482) is noted; the seeds do not change here.
