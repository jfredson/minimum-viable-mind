# The loop removal test: findings of the free step-3 checks on the pilot set

*Written 2026-11-21 by the session that wrote the design, the specification and the generator. This is
step 3 of section 9 of the design (`docs/loop-removal-test-design-2026-11-20.md`, version 0.8). It reports
the checks of section 12 of the battery specification (`battery-authoring-spec.md`, commit 178b7b5).*

*They were run on the pilot set generated from the committed code (commit c02b763), with half A and seed 1,
using the research model's real tokeniser at revision 657b53ba. The raw figures are in
`batteries/pilot/step3-results.json`, `batteries/pilot/build-report.json` and
`batteries/pilot/overlap-check.json`. Nothing was run on the model, and nothing was spent.*

*These checks were run by the author. Under the review protocol they are owed a check by a session that
did not write them. **What they can and cannot show:** they check that the generator builds what the design
describes. They cannot forecast RT-345, the finding that the swap's dose may differ between the two task
groups, which only step 4b on the model can measure.*

## What was generated

| Part | Count |
|---|---|
| Scored pairs | 120: 30 for each rule kind; 15 sums, 15 products, 30 capitals, 30 opposites, 30 everyday colours |
| Donor-only pairs, never scored | 212 |
| Chained-lookup items | 40, with chains of two to six steps |
| Neutral passages, half A | 200: 100 to build the average, 100 to measure its damage |

Context order: 57 pairs put the rule's facts last, and 63 put the routine fact last. The balance is set
within each group, so it is uneven overall where groups have odd counts.

## The ten checks

1. **Single-token counts** (both halves of every list):
   - capitals: 85 of 165 are one token at the answer position, and 80 once the capitals whose names overlap
     their country's are removed. Half A has 44 usable capitals;
   - opposites: 151 of 160 words;
   - everyday-object colours: 122 of 122;
   - three-letter words: 95 of 95;
   - colours: 11 of 11;
   - numbers 0 to 999: all 1,000.

   The capitals figure agrees with the sixth and seventh checks (about 84 to 90 worldwide).
2. **The fixed-wording table.** All fourteen rows recount equal with the real tokeniser. **Pass.**
3. **Twin lengths.** In all 120 pairs, the two twins have the same token length. **Pass.**
4. **Generation drops and spreads.**
   - **Drops while building.**
     - 30 draws were dropped because the right answer copied a word of the question.
     - 32 draws were dropped because the copying and cross-cell rules left fewer than four wrong answers.
     - 35 capitals were dropped as not one token, and 3 because their names overlap their country's.
     - 4 opposite answers were dropped as not one token.
   - **Capitals by region.** The capitals used as right answers come from: Middle East 7, Northern Europe 4,
     Western Europe 4, South America 4, Southern Europe 3, and Eastern Europe, East Asia, Southeast Asia and
     North Africa 2 each. **None comes from Africa south of the Sahara, Central America, the Caribbean or
     Oceania.** That is the skew the design states as a cost (RT-399, RT-408).
   - **Where the wrong capitals came from.** Across every attempt to build a capitals item, scored and
     donor-only, four wrong capitals came from:
     - the same region in 633 attempts;
     - the nearest neighbouring region in 877 attempts;
     - nowhere, so the item was dropped, in 378 attempts.

     So with this region map, the neighbouring region is needed more often than not.
   - **Distinct right answers.** 30 capitals, 30 opposites, 11 everyday colours, 15 sums and 12 products.
     The lookup kind's right answers cover all eleven colours.
5. **Donors.**
   - **The donor-only pairs.** 212 were added.
   - **Every scored pair has at least one eligible donor.** One pair has fewer than five. The mean is 9.5
     eligible donors per pair.
   - **Why drawing stopped.** Drawing stopped because every pair had five donors in 13 of the 14 groups. In
     the letter code with everyday colours, it stopped at the draw budget.
   - **No scored pair was dropped for want of a donor.**
6. **The stand-in dose ratio** (routine cell divided by prompt-rule cell):

   | Rule kind | weight 0 | weight 0.3 | weight 0.6 |
   |---|---|---|---|
   | Operator | 0.994 | 0.996 | 0.998 |
   | Unit | 0.997 | 0.998 | 0.999 |
   | Letter code | 1.000 | 1.000 | 1.000 |
   | Lookup | 0.999 | 1.000 | 1.000 |

   Every kind lies inside the band, at 0.95 to 1.05 at weight 0.3 and 0.90 to 1.10 at weights 0 and 0.6, and
   inside the design's "about 0.99 to 1.03" for a correct build. **Pass.** As the design says, this shows
   only that the generator builds the shared context correctly.
7. **The tail shares and what step 4b can absorb.** This is the share of the changed span that lies after
   the shared context: the final question, the template's closing tokens and the answer.

   | Rule kind | Tail share | Difference per position step 4b's 10% limit can absorb |
   |---|---|---|
   | Operator | 0.28 | about 36% |
   | Unit | 0.34 | about 30% |
   | Letter code | 0.17 | about 61% |
   | Lookup | 0.17 | about 58% |

   These agree with the sixth and seventh checks' estimates. They are the figures step 4b is to read
   against.
8. **The average-method counts.** In every rule kind, the two twins of every pair have the same number of
   final-question tokens and the same number of invented-word or symbol tokens (largest difference 0).
   **Pass.**
9. **Candidate words named in donors' contexts** (RT-411). This is the share of a recipient's five donors
   whose context names the recipient's right answer, and each wrong candidate.
   - **Lookup, prompt-rule cell:** right answer 48% to 68% of the time, wrong candidates 48% to 51%.
   - **Lookup, routine cell:** 0% to 4%.
   - **Operator and unit, prompt-rule cell:** 3% to 19%. Donors' operands and counts are small numbers that
     sometimes equal the recipient's candidates.
   - **Letter code:** 0%.
   - **Other routine cells:** 0% to 8%.

   The lookup difference between the cells is as the seventh and eighth checks forecast. It is to be noted
   beside the reading with lookup left out at step 4b.
10. **The average is defined at every position.**
    - **Template positions.** All 240 scored items and all 200 neutral passages carry the same 12 template
      tokens before the user text and the same 3 after it, the reply opening included. So every template
      position has a slot average.
    - **Text positions.** These are pooled from the 100 build passages, which give 5,326 text positions.
    - **Pass,** under the assumed reply opening (section 9 of the specification).

**The chained-lookup items.** All 40 have five single-token colour candidates, and chain lengths of two to six
steps.

**The overlap check.** It passes: no list entry, answer value or candidate crosses between the halves. It
caught two real faults in a trial run during debugging. First, some three-letter words were also colours or
opposites, such as "red", "hot" and "raw", so they crossed the halves through the other list. Second, the
operator kind's answer values could fall in both halves. Both were fixed in the lists and the generator
before the pilot was generated, and the commit message of c02b763 records them.

## Points for the record

- **The neutral passages stop a little short.** The longest is 95 tokens, against 98 for the longest scored
  item, because the generator stops at whole sentences. The pooled average does not depend on length. The
  ten-bin fallback uses relative position, so it does not need equal lengths either. The specification asked
  for lengths "up to the longest item", and this falls three tokens short.
- **The opposites list holds some verbs.** It includes pairs such as "buy" and "sell", and "push" and
  "pull", while section 3 of the specification calls them adjectives. Every pair is a common opposite, and the
  routine question asks only for "the opposite of the word", so the cell is unchanged in kind. The
  specification's wording should be corrected at the next revision.
- **The lists were written from general knowledge.** The countries and capitals are still owed a check
  against a public source a reader can open, before registration (specification, section 3).
- **The reply opening is assumed.** It is still `<|message_model|><|content_text|>`. If step 4a finds
  otherwise, the pools and the pilot are rebuilt before anything is scored (specification, section 9).
- **These checks are the author's own,** and they are owed a check by a session that did not write the
  generator.

## What this means for the next step

The pilot set is built as the design describes, and every free check that can pass on paper passes. The
next step, 4a, is the first on a rented machine:
- load the model and confirm the hooks;
- settle the reply opening and how to suppress written reasoning;
- measure the noise floor, and run the identity and bypass checks.

That step needs John's go, with a price and a ceiling, and the design records what he is to be told then:
these free checks passed by construction, and they settle nothing about the real dose of the swap (design,
RT-391).

---

## Addendum, 2026-11-21: the pilot regenerated after the independent check

*Added after the independent check (`independent-check-2026-11-21.md`) found four generator faults that had
to be fixed before step 4b. The fixes were written into the specification first (section 14, commit
5fc2f0c) and then into the code. The pilot files above are replaced by a pilot generated from the fixed
code, with the same half A and seed 1. Every figure in this addendum comes from the regenerated
`batteries/pilot/step3-results.json`. The figures in the sections above describe the first pilot, from
commit c02b763, and are kept as the record.*

**The four fixes, and what the regenerated pilot shows.**
- **Chained lookups** (RT-415, RT-426).
  - **The fix.** Each item now has five chains of "points to" rows. Each chain ends in one of the five
    candidate colours, and the distractor chains run two to six steps, drawn independently.
  - **The text.** In all 40 items, every candidate appears in the text and is reached by a chain. Before,
    one candidate was missing in 40 of 40.
  - **Donors.** Donor-only chained items were added under the aimed rule. No chained item is without a
    donor, and none has fewer than five.
  - **Length.** The items now run 195 to 284 tokens, well beyond the scored pairs and the neutral passages
    (RT-425).
- **Where the right number sits** (RT-416). The right number's place in numeric order is now drawn first, and
  it is kept while the numbers are redrawn. Counts of right answers at places 1 to 5, lowest to highest:

  | Kind | Place counts |
  |---|---|
  | Operator (30) | 7, 4, 6, 7, 6 |
  | Unit (30) | 7, 3, 5, 5, 10 |
  | Sums (15) | 2, 5, 2, 3, 3 |
  | Products (15) | 3, 6, 3, 3, 0 |

  Before, the middle place held 40% to 53%. Every place can be filled for every kind: for half-A products,
  14 to 18 of the 22 answers fit each place. So the products' 0 at the top place is chance, which happens
  about 3.5% of the time with 15 items.

  **One step taken during the fix, recorded.** The first version of this fix drew the place uniformly but
  drew a new place whenever an item could not fill it. That still put 11 of 30 unit answers in the middle
  place, because middle places are easier to fill for small answers. The code was changed to keep the drawn
  place while redrawing the numbers, which is what section 14 says. Only that version's output is
  committed.
- **The copying rule** (RT-418). It now ignores only function words.
  - **Drops.** More draws are dropped as a result: 103 for a right answer that copies a question word,
    against 30 before, and 145 for too few wrong answers left, against 32. Every group still filled.
  - **Pools.** No candidate now contains, or is contained in, a content word of the routine fact or final
    question. That includes "give", "sum" and "capital".
- **The order of an odd group's extra pair** (RT-422). It is now drawn from the seed. The counts are 59 with
  the rule's facts last and 61 with the routine fact last.

**Everything else, rerun on the regenerated pilot.**
- **The overlap check** passes.
- **The wording table** recounts equal.
- **Twin lengths.** All 120 twins are equal.
- **The stand-in dose ratio** is 0.994 to 1.000 in every rule kind, inside the band.
- **Tail shares:** 0.28, 0.34, 0.17 and 0.17.
- **The average-method counts** are equal.
- **The average is defined** at every position under the assumed reply opening.
- **Donors for the scored pairs.**
  - 204 donor-only pairs were added.
  - One scored pair has no eligible donor, and four have fewer than five. The mean is 10.2.
  - The pair with no donor is listed in `build-report.json` with its content. Before the fix, every pair had
    a donor. The change follows from the new draws, not from a change in the donor rule.
- **Check 9 now draws donors at random,** as step 4b will (RT-427). In the lookup kind, a donor's table
  still names the recipient's candidate colours about 40% to 70% of the time in the prompt-rule cell.

**Still open from the independent check, before any test set:**
- completing the overlap check (RT-417);
- the opposites and objects lists (RT-419, RT-420), with the capitals, regions and doubtful colours checked
  against a source;
- a wider fallback for capitals (RT-421);
- the smaller specification and reporting points (RT-423 to RT-425, RT-427 to RT-429).

**Still owed:** an independent check of these fixes. RT-345 stays open.

**An ordering fault, recorded.** The code change that keeps the drawn place was used to generate the pilot
committed in d4171f1, but it was committed only afterwards, in 54fa782. The pilot was then regenerated from
54fa782, together with its overlap and step-3 results, and every file came out byte-identical to the
committed one. So the committed pilot is exactly what the committed code produces.
