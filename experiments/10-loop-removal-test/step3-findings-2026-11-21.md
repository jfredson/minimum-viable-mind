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
