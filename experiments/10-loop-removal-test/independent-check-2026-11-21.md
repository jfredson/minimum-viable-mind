*Filed 2026-11-21 by the session that wrote the specification, the generator and the pilot set, verbatim as the checker returned it. The checker was a fresh Claude Code session with no history of this conversation, which wrote none of the design, the specification, the lists, the generator, the pilot or any earlier review. It worked read-only in a detached worktree at commit 889f9e4, using only its own scratch folder, which was created empty for it, and it had no web access. Nothing in its text was changed in filing. The filer's check follows, below a rule, and is not part of it.*

---

# Independent check: the loop removal test's battery specification, generator and pilot set

*Checked 2026-11-21 by a session that wrote none of the design, the specification, the generator, the content lists, the pilot set or any earlier review. Commit checked: 889f9e4, in the read-only worktree `.claude/worktrees/check-pilot-2026-11-21`. Nothing was run on the model, nothing was downloaded and nothing was spent.*

## What I opened

- `experiments/10-loop-removal-test/battery-authoring-spec.md` (the specification), all of it.
- All six content files in `data/`: countries, region map, opposites, objects, three-letter words and colours. I read every entry.
- `src/build.py` (the generator), `src/check_overlap.py` (the overlap check) and `src/step3_checks.py` (the step-3 checks), all of them line by line.
- The pilot folder `batteries/pilot/`. I read `build-report.json`, `step3-results.json` and `overlap-check.json` in full. I parsed every line of the four item files with scripts and read a sample of items in full: 30 capitals, 30 opposites and 30 everyday-colour pairs (their facts, answers and wrong answers), four whole pairs with every variant, the donor-only pairs that offer the word "give", and the first chained lookup.
- `step3-findings-2026-11-21.md` (the author's findings), all of it.
- The design, `docs/loop-removal-test-design-2026-11-20.md`: sections 3 and 5 in full, section 9 in full, and a few change-log lines found by searching.
- The research model's `chat_template.jinja`, its first 20 lines and lines 120 to 150 only, to see how the "none" reasoning setting is rendered.
- The split test's `experiments/09-split-removal-test/src/batteries.py`, only the two syllable lists, to compare them with the generator's copy. They match.
- The message of the generator commit (c02b763).

## What I did not open

- `docs/outside-review-protocol.md`, the earlier closure checks and reviews, and every other review folder.
- Design sections 1, 2, 4, 6, 7, 8, 10 and 11, and most of the change logs.
- `tokenizer.json` itself (I used it only through the `tokenizers` library) and the `tiktoken` folder.
- Any outside source. I had no web access, so every factual doubt about capitals, regions or colours below is marked "to check against a source".

**Where I worked.** I used only my own scratch folder, `/private/tmp/claude-501/loop-review9-2pkL6c`, for every script and output. I opened no other scratchpad or tmp folder.

## What is reproduced, and what is judgement

**Reproduced exactly (MEASURED).**
- I reran `build.py --half A --seed 1` with the real tokeniser into my scratch folder. All five output files (the pairs, the donor-only pairs, the chained lookups, the neutral passages and the build report) are byte-identical to the committed ones.
- `check_overlap.py` on my copy passes (exit 0), and its output is identical to the committed `overlap-check.json`.
- `step3_checks.py` on my copy writes a `step3-results.json` that is byte-identical to the committed one.
- Every figure in the findings that I checked agrees with those results. That covers the dropped entries, the pools, the donor counts, the dose ratios, the tail shares and the rates of check 9.

**Also measured by my own scripts.** These are the counts behind findings RT-415, RT-416, RT-418, RT-421, RT-422, RT-425, RT-426, RT-428 and RT-429: where the right answer sits among the numbers, the chained-lookup shortcut, letters shared at the same position in the letter code, the neutral passages, the capitals' sources counted per country, and donors for the chained items.

**Judgement (ARGUED).** Whether a given wrong answer is "also right", whether a model would use a cue, and how serious each fault is.

## Checks that passed

These were checked and found to match the specification:
- **The split into halves.** One shuffle with seed 0, and the odd entry goes to half B.
- **The rule wordings**, apart from the units sentence (RT-424).
- **The letter code.** In all 73 letter-code items (scored and donor-only), there are eight shuffled rows, no letter codes to itself, every wrong answer is spelled only with the table's plain letters, and the coded string is never a candidate and never a word from the list.
- **The lookup.** All 102 lookup items have six different colours, and every candidate comes from the table.
- **The pairing exclusions and the 25% cap.**
- **The fixed final questions.** All fourteen recount equal, as the specification states.
- **The twins.** Twin lengths are equal, and the without-rule and baseline variants are built as stated.
- **The cross-cell rules.** No pair offers either twin's right answer to the other twin.
- **Donor-only pairs.** Same half, reuse allowed, aimed at pairs short of donors, exact copies of the recipient barred, and the draw budget applied.
- **Template slots.** They match for every scored item, every neutral passage and, by my own run, all 40 chained items.

## Findings

**RT-415 (serious, MEASURED): every chained lookup can be solved in one step, and one of its five candidates never appears in the text.**

The generator (`build_chained`) draws `hops + 4` names and gives `hops + 1` of them to the chain. Only three names are left over as distractors, while four extra colours are drawn. So the fifth colour candidate is never in the passage. That holds for 40 of 40 items.

The distractor rows are also all of the form "X is colour". No distractor row has the form "X points to Y". So the right answer is always the colour of the only coloured name that some "points to" row names. In all 40 items, that gives the answer without following the chain.

The bites check (design, section 5) needs the chains of four or more lookups to require the loop. As built, they do not. So the one-pass run may fail to cost them, and the result would be called "not testable" for a wrong reason. Or the main removal may fail to bite them, and then outcome D could not be read.

Fix before step 4b:
- draw four distractor names;
- give the distractors chains of their own, with "points to" rows, so that the target's chain cannot be told apart by form;
- follow the design's "several lookup tables".

**RT-416 (serious, MEASURED rates, ARGUED effect): the right number usually sits in the middle of the five candidates.**

For operator, unit, sum and product items, `near_numbers` draws the four wrong numbers evenly from within 5 (or 12, for products) of the right answer. So the right answer is often the middle value of the five. Measured on the pilot:
- operator items: 13 of 30 (43%);
- unit items: 12 of 30 (40%);
- sums: 8 of 15 (53%);
- products: 7 of 15 (47%).

By chance it would be 20%. In the unit items the right answer is never the lowest candidate.

A model that picks the middle value, or the most plausible size of number, beats chance by more than 0.10 without the rule. That can fail the "rule is needed" check (design, section 5) for the operator and unit kinds. It also gives a damaged model a way to answer prompt-rule items without the rule, which would understate the prompt-rule cell's loss.

Fix: draw wrong numbers so that the right answer's rank is uniform. For example, choose the rank first and then draw the offsets.

**RT-417 (serious, MEASURED by reading the code): the overlap check does less than the design and the specification require.**

- When it is pointed at a set of items, `check_overlap.py` looks at candidates only, and only for capitals and three-letter words.
- It does not check:
  - opposite candidates;
  - objects, countries, invented words or tables used in the items' text;
  - whether any pilot prompt, table or operand pair appears in the test set (design, section 5);
  - the design's requirement that every letter-code wrong answer is spelled only with the table's plain letters. That requirement is not in the specification's section 11 either. The pilot happens to satisfy it (see "Checks that passed").
- Its check for "a donor-only pair from the other half" (specification, section 11) looks only at candidates, not at the content the pair uses.

None of this matters for the pilot, which is all half A. It must be fixed before the test set is generated and checked.

**RT-418 (serious for the test set, MEASURED): the copying rule skips words it should cover.**

The generator's list of words that the copying rule ignores (`STOP`) includes content words of the final questions: "capital", "city", "colour", "opposite", "sum", "product", "multiply", "word", "give", "given", "object", "country" and "usually". So the copying rule (specification, section 7: no candidate may contain, or be contained in, a content word of the routine fact or the final question) does not apply to them.

- **In the pilot.** "give" is offered as a candidate in four donor-only "lookup with opposites" items, whose routine question ends "...of the given word?". The "unit with opposites" routine question begins "Give the opposite...", so "give" could be offered there too. The pilot's scored pairs happen to avoid it.
- **In the test set.** Half B's three-letter list holds "sum" and "cap". So scored test items pairing the letter code with sums or with capitals can offer a candidate that is copied from the routine question.

The specification is silent on a list of ignored words; the code chose one. Fix: shrink the list to true function words ("the", "of", "is" and the like), or state and defend the list in the specification.

**RT-419 (serious for the test set, worth noting for the pilot; ARGUED): the opposites list has pairs whose words are also opposites of words in other pairs.**

The rule that no word sits in two pairs holds, but near-synonyms in different pairs make a wrong candidate a valid opposite:
- **Half A.** "noisy/silent" sits beside "loud/quiet". "above/below" sits beside "upper/lower", and pilot pair A-0039 ("above", answer "below") offers "lower".
- **Half B.** "dark/bright" sits beside "heavy/light", and "light" is the usual opposite of "dark". "enter/exit" sits beside "arrive/leave".

Some pairs are not the common opposites:
- "tall/stubby", where the common opposite is "short", which is in the other half;
- "fat/lean" (common: "thin");
- "cheap/costly" (common: "expensive");
- "brave/timid" (common: "cowardly");
- "calm/angry".

About 30 of the 80 pairs are not adjectives: verbs, nouns, prepositions and adverbs. The findings mention only the verbs.

Also, the two directions of one pair both count as questions. In the pilot, 6 pairs supply 12 of the 30 scored opposites items: long/short, laugh/cry, simple/complex, open/shut, fat/lean and kind/cruel. The specification allows this. But it sits uneasily with the design's own reasoning that "5 × 8" and "8 × 5" are one question (RT-407).

**RT-420 (worth noting, ARGUED; to check against a source): the everyday-objects list breaks its own rules in places, and some colours are doubtful.**

- **Colour words in names.** "a blueberry" and "a blackberry" contain their colour word, against the specification's section 3. The generator's copying rule drops them, so they never reach an item, but the list still breaks the rule.
- **Colour that differs by place.** "a squirrel" (red or grey depending on country) goes against the rule "no object whose typical colour differs by country".
- **Doubtful typical colours, or common colours missing from the "also" list.** Six scored pilot items offer a wrong colour that a careful reader would accept:
  - A-0029, "a seal" (offers brown and black);
  - A-0056, "a lavender flower" (offers blue);
  - A-0053, "a potato skin" (offers red);
  - A-0058, "a raspberry" (offers black);
  - A-0059, "a watermelon rind" (offers white);
  - A-0022, "a vanilla flower" (offers green; the typical colour itself is to check).

  Others, to check against a source:
  - "a jellyfish" (white, though jellyfish are usually see-through);
  - "a watermelon inside" (pink is missing from its other colours);
  - "a lobster after cooking" (orange is missing);
  - "a papaya inside" (red and pink are missing);
  - "a pineapple" (inside or outside?);
  - "a grape" (green as the typical colour).
- **Near-duplicates across halves.** "a lime" and "a lime leaf"; "a pumpkin" and "a pumpkin seed"; "a lump of charcoal" and "a lump of coal"; "a chilli pepper" and "a bell pepper".
- **Near-duplicates within a half.** "an aubergine" and "a ripe aubergine skin" (half B, both purple); the two walnut entries and the two watermelon entries (half A).

The model's confidence check will drop items it does not answer confidently, which limits the harm. But these items shrink the pools.

**RT-421 (worth noting, MEASURED): the region map, not only tokenisation, keeps African, Caribbean and Central American capitals out, and the counts are per attempt rather than per item.**

- **Capitals lost to the region map.** 9 of half A's 44 one-token capitals can never be right answers. Their region plus its nearest neighbouring region holds fewer than four one-token capitals. They are Kigali, Kinshasa, Luanda, Abuja, Maputo, Havana, Managua, Male and Astana.
- **The findings blame the wrong cause.** They put the absence of sub-Saharan, Caribbean and Central American capitals down to the single-token cost (RT-399, RT-408, the design's stated costs of that rule). Here a third fallback, such as the whole continent, would restore most of them.
- **Counts per attempt.** The reported counts (633 same region, 877 neighbouring region, 378 dropped) count every draw, scored and donor-only, so countries drawn repeatedly are counted many times. Per country, the counts are 14 same region, 21 neighbouring region and 9 dropped. For the 30 scored capitals they are 11 same region and 19 neighbouring region.
- **Regions to check against a source.** Georgia, Armenia and Azerbaijan are placed in the Middle East; Cyprus in Southern Europe; Mongolia in Central Asia; Zambia, Zimbabwe, Malawi, Mozambique and Madagascar in Southern Africa.
- **Capitals with a dual or disputed status, to check.** Bern, Amsterdam, Porto-Novo, Dodoma, Gitega, Sanaa and Kuala Lumpur. "Washington" is also the name of a state.
- **A near-copy the copying rule misses.** "Brasilia" for "Brazil" (scored pair A-0004). The whole-word rule does not catch it.

**RT-422 (worth noting, MEASURED): the extra pair in an odd group always goes the same way.**

The specification says an odd group's extra pair has its order set by the seed. In `build_scored`, it always gets "routine fact last". All six odd groups go that way, which gives 57 against 63. Fix: assign the extra pair's order with the seeded random stream.

**RT-423 (worth noting, ARGUED from a measured pool): the pilot allocation is typed in by hand, not computed, and is not as even as the pools allow.**

- The allocation (`PILOT_ALLOCATION`) gives the operator and unit kinds 7, 11 and 12 pairs across capitals, opposites and everyday colours.
- 10, 10 and 10 fits both the 25% cap and the pools. Half A has 35 reachable capitals, and the code and lookup kinds could take 5 capitals each.
- The specification asks for "as evenly as possible across the allowed routine kinds of each rule kind" but gives no method. No method exists for the test set either.

**RT-424 (worth noting, MEASURED): places where the code departs from the specification's wording, or chose where the specification is silent.**

- **Departures from the specification's wording.**
  - The unit rule reads "1 {u1} is {k} {u2}s." The fixed wording has no "s".
  - Operator answers are held to 10 to 45 in half A and 100 to 999 in half B. The specification says 10 to 999. In the pilot this leaves the four operator shapes at 11, 9, 6 and 4 items.
  - Candidate order is shuffled with the builder's single random stream, not with "the item's seed".
  - The neutral passages alternate between building the average and measuring damage. The specification says the first 100 build.
- **Choices where the specification is silent.**
  - The operator and unit wrong answers are numbers within 5 of the right answer.
  - Every colour, three-letter-word and opposite candidate is lowercase, while capitals are capitalised. The capitalised forms are single tokens too: 11 of 11 colours, 47 of 47 three-letter words and 69 of 76 opposite answers. At the start of a reply, case may change the baseline margins. Pairings such as the letter code with capitals mix lowercase prompt-rule candidates with capitalised routine candidates. This should be settled at step 4a together with the reply opening.
- **Numbers crossing the halves.** Numeric wrong answers are not held to their half's range. Half A sums of 45 to 49 can get wrong answers of 50 to 54, and half A products can get up to 48. The design says test candidates are drawn only from half B's pools.

**RT-425 (worth noting, MEASURED): the neutral set is thin and does not cover the full range of lengths.**

- The 200 passages are built from only 20 sentences, and 75 of them repeat a sentence within themselves.
- The passages that build the average and those that measure its damage are made of the same 20 sentences. That weakens the separation RT-376 sought (judging the average on passages it did not come from).
- The lengths fall short at both ends: 39 to 95 tokens, against scored items of 50 to 98. The generator stops before the target length, and the findings report only the top end.
- They also fall well short of the chained items, which run from 78 to 116 tokens and are scored under both methods.

**RT-426 (serious, MEASURED, with the specification silent): the chained lookups have no donor rule.**

The bites check runs the swap on chained items. Yet neither the specification nor the generator says where their donors come from. Under the items' own rules (at least one token longer, and the donor's answer not among the recipient's five colours), 3 of the 40 have no eligible donor and 11 have fewer than five. No step-3 check reports this. It must be settled before step 4b.

**RT-427 (worth noting, MEASURED): what some step-3 checks actually measure.**

- **Check 9 (RT-411, candidate words in donors' contexts)** uses the first five eligible donors in file order, which are mostly scored pairs. Check 6 and step 4b use five drawn at random. The rates are plausible but are not those of the donors that will be used.
- **Check 8 (the average-method counts).** The invented-word counter also counts English tokens such as " to" in "The name to look up" as invented-word pieces. Because the twins share every token before the final question, and check 3 already forces equal lengths, check 8 can only ever see the fixed questions. Like check 3, it passes by construction.
- **The "absorbable difference" (0.10 divided by the tail share).** The arithmetic is right, but only if tail positions carry the same average distance per position as the shared context. The findings present the figures as "the figures step 4b is to read against" without that condition. They also say the figures "agree" with the sixth check, yet the letter code moved from 49% to 61%.
- **The stand-in dose ratio (check 6)** is close to 1 by construction, as the findings say.
- **The generation counts (check 4)** mix scored and donor-only draws, are not split by kind, and do not show the spread of right answers before and after the single-token rule, which the design asks for.

**RT-428 (worth noting, MEASURED): the letter code leaves a cue, and its answers repeat.**

No letter may code to itself, so the right answer never shares a letter in the same position with the coded string. Wrong answers can. In 13 of the 30 scored letter-code items, one or two wrong answers can be ruled out that way without decoding.

Separately, the 30 scored letter-code items have only 20 different answer words. The same word is reused with a new table.

**RT-429 (worth noting, MEASURED): wrong numbers can copy the item's own numbers.**

In 11 scored operator and unit items, a wrong number equals a number in the item's own text. With small unit answers (4 to 9), the item's own k and n become wrong candidates. The specification exempts numbers from the copying rule, so this is allowed. But it is a copying lure, and it feeds the operator and unit rates of check 9.

## RT-345 (the swap's dose may differ between the cells)

It stays open. Nothing here bears on it, and these checks cannot close it.

## Verdict

The pilot set is exactly what the committed generator produces. The free checks reproduce to the byte, and the parts at the heart of the pairs (shared context, equal twin lengths, the letter-code and lookup tables, the cross-cell rules and the donor-only pairs) are built as specified.

**Step 4a.** The pilot set is fit for step 4a as it stands: loading the model, checking the hooks, the noise floor, and the identity and bypass checks. Those do not depend on item quality.

**Step 4b.** It is not fit for step 4b until these are fixed and the step-3 checks rerun:
- the chained lookups, which can be solved in one step and offer a candidate absent from the text (RT-415), and which have no donor rule (RT-426);
- where the right number sits among the candidates (RT-416);
- the copying-rule exemptions (RT-418);
- the odd-group order (RT-422).

Before any test set is generated, the overlap check must be completed (RT-417), and the opposites and objects lists corrected (RT-419, RT-420). The capitals, regions and doubtful colours must be checked against a source a reader can open.

The remaining points are corrections to the specification or to the reporting. RT-345 stays open regardless.
---

## The filer's check (not part of the independent check)

*Written by the author of the generator, 2026-11-21. It closes nothing.*

- **RT-415, the chained lookups.** Confirmed with a one-line count: in 40 of 40 committed chained items, one of the five candidate colours never appears in the text. This is a plain bug in `build_chained`. It draws `hops + 4` names and uses `hops + 1` of them for the chain, which leaves three distractors for four extra colours.
- **The reproduction.** The checker reran the committed generator and found the output byte-identical. That confirms the pilot was generated from commit c02b763, as the findings say.
- **Where things stand.** The checker finds the pilot fit for step 4a (load the model, confirm the hooks, the noise floor, and the identity and bypass checks). It is not fit for step 4b until four things are fixed and the step-3 checks rerun:
  - the chained lookups (RT-415, RT-426);
  - where the right number sits among the candidates (RT-416);
  - the copying-rule exemptions (RT-418);
  - the order of an odd group's extra pair (RT-422).

  The overlap check (RT-417) and the lists (RT-419, RT-420, and the capitals and regions to check against a source) must be put right before any test set is generated. RT-345 stays open.
