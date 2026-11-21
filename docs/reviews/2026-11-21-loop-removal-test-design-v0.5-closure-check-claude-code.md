*Filed 2026-11-21 by the session that wrote the design and its fixes, verbatim as the reviewer returned it. The reviewer was a fresh Claude Code session with no history of this conversation, which wrote neither the design, nor its fixes, nor the four earlier reviews. It worked read-only in a detached worktree at commit b8579de, and changed nothing in the repository. It used only its own scratch folder, which was created empty for it and kept apart from the author's working files and from earlier reviewers' scripts. It was told not to open any other scratch folder. Nothing in its text was changed in filing. The filer's check follows the closure check, below a rule, and is not part of it.*

---

# Closure check: the loop removal test design, version 0.5

*Reviewer: a fresh Claude Code session. I did not write the design, any of its fixes, or any of the four earlier reviews. I worked read-only in the detached worktree `closure5-loop-design-2026-11-21` at commit b8579de, and I changed nothing in it. I used only my own scratch folder, `/private/tmp/claude-501/loop-review5-sr4LLe`, which was empty when I started. Every script and every output is in that folder. I opened no other scratchpad or temporary folder. I downloaded nothing, installed nothing and spent nothing. New findings continue the red-team numbering from RT-390.*

---

**What I opened.**
- **Read in full:**
  - the target, `docs/loop-removal-test-design-2026-11-20.md` (version 0.5, with all four change logs);
  - the closure check of version 0.4, `docs/reviews/2026-11-20-loop-removal-test-design-v0.4-closure-check-claude-code.md`. I read its filer's check as the author's note, not as part of the review;
  - John's rulings, `docs/rulings/2026-11-21-loop-removal-test-choices-ruling.md`;
  - the tokeniser download record, `docs/2026-11-21-loop-removal-tokeniser-download.md`;
  - `experiments/09-split-removal-test/src/batteries.py`;
  - the research model's `chat_template.jinja`, `special_tokens_map.json` and `REVISION` (657b53ba…). I read the settings in `tokenizer_config.json` and the tokeniser's pre-tokeniser and post-processor settings in `tokenizer.json`.
- **Read in part:**
  - `docs/outside-review-protocol.md`: the tier 1 description and "The closure rule, which is the new part";
  - `git diff ddc5031 b8579de` on the design. I read every removed line and checked where each removed rule went.
- **Ran** these scripts, each with the research model's real tokeniser loaded through `tokenizers.Tokenizer.from_file`. The chat template was rendered in jinja2's sandboxed environment, with `{% generation %}` treated as a plain block, and the Python was run with `-I`:
  - `tok_check.py`: recounts the fixed-wording table;
  - `pools.py` and `build.py`: my stand-in pools and pair builder;
  - `proxy.py`: the stand-in dose ratio;
  - `decomp.py`: where in the item that dose falls;
  - `tail.py`: the share of the changed span where the two twins can differ;
  - `avg387.py`: step 3's free estimate for the average method;
  - `dist.py`: how far each needed fact sits from the question;
  - inline checks of the letter code, the colours, the pool arithmetic and the copying rule.

**What I did not open.** I did not open:
- the inside review of version 0.1, or the closure checks of versions 0.2 and 0.3, beyond their titles. Version 0.4's check states what it carried forward;
- the three-hypotheses proposal and the design note;
- the committed pilot battery files;
- the external pages (model card, Hugging Face page, Goodfire);
- any scratchpad except my own.

**What is real and what is a stand-in.**
- **Real:** the tokeniser and the chat template. Every token count and position below comes from them.
- **Stand-ins (written by me, because the battery specification does not exist yet):**
  - every content pool: 138 countries, 72 opposite pairs, 60 everyday objects, 140 three-letter words, plus the syllables and operator symbols from `batteries.py`;
  - the wording of each rule and each fact;
  - the order of the three parts of the shared context;
  - the opening of the model's reply. I assumed `<|message_model|><|content_text|>`, because the template renders no opening for the reply and step 4a has not settled it.
- **The dose is a proxy.** Every "dose" below is the stand-in count the step-3 rule describes. It is not a measurement on the model. Each position from the first place where recipient and donor differ counts 1 if its token differs from the donor's token at the same place. If the token is the same, the position counts a weight of 0, 0.3 or 0.6.

---

## Verdicts

| Item | Verdict | Label |
|---|---|---|
| RT-345 (fatal), the swap's dose differed between the two task groups | **Not closed, and it cannot be closed on paper.** The stand-in now comes out at 1.00 to 1.02, but by construction it cannot see the risk that remains. Owed at step 4b, as the design says | MEASURED (proxy), ARGUED for what remains |
| RT-380, equal length did not give equal dose | **Closed, with conditions** (RT-390, RT-391) | MEASURED (real tokeniser, stand-in proxy) |
| RT-381, the unit kind could not be length-matched | **Closed** | MEASURED (real tokeniser) |
| RT-382, phrasings chosen item by item | **Closed** | MEASURED (real tokeniser) |
| RT-383, colours could not meet the overlap check | **Closed, with a condition** (RT-396) | ARGUED |
| RT-384, the everyday-colours pool | **Closed on paper.** The list is owed at step 3 | ARGUED, arithmetic MEASURED |
| RT-385, the copying rule's wording | **Closed, with a condition** (RT-395) | MEASURED (count) |
| RT-386, the margin fallback never rescued a kind | **Closed** | MEASURED (grep) |
| RT-387, step 3 saw the swap only | **Closed as text, with a condition**: the new estimate passes by construction (RT-391) | MEASURED (real tokeniser) |
| RT-388, donors of the same routine kind left the largest tables without donors | **Not closed.** At the pilot size the new rule cannot be met (RT-392) | MEASURED (arithmetic and proxy) |
| RT-389, text gaps | **Closed.** New gaps are listed under RT-390 and RT-397 | MEASURED (grep) |
| Condition on RT-340, the simulation run on the surviving pairs | **Met** (lines 563 to 566) | MEASURED (grep) |
| Condition on RT-371, the small leak reported beside any A | **Met** (lines 645 to 649) | MEASURED (grep) |
| Condition on RT-372, the letter code's extra letters and three different letters | **Met, and it builds** | MEASURED (real tokeniser, stand-in pool) |

### RT-380 and RT-345: the stand-in dose under the shared-context construction

**What I built.** I built pairs as section 5 describes them:
- one shared context, in the order rule, then the rule's facts, then the routine fact;
- the fixed final questions from section 5's table, one wording per pairing;
- only the pairings the exclusions allow;
- lookup tables of five, six and seven entries;
- donor pairs of the same rule kind, routine kind and (for lookup) size class, each twin at least as long as the recipient's matching twin, and with no donor answer equal to the recipient's answer;
- five donors drawn at random, or all eligible donors if fewer.

The item is rendered with the real template (`reasoning_effort="none"`), followed by the reply opening and the right answer.

```
python3 -I proxy.py 75 <seed>     (300 pairs, 75 per rule kind; ratio = routine cell / prompt-rule cell)
seed 1: op   w0 1.0188  w0.3 1.0165  w0.6 1.0147 | unit 1.0106 1.0099 1.0094 | code 1.0091 1.0063 1.0048 | look 1.0023 1.0025 1.0027
seed 2: op   1.0192 1.0165 1.0144 | unit 1.0138 1.0130 1.0123 | code 1.0098 1.0071 1.0055 | look 1.0030 1.0036 1.0041
seed 3: op   1.0137 1.0116 1.0101 | unit 1.0142 1.0131 1.0122 | code 1.0079 1.0056 1.0044 | look 1.0026 1.0029 1.0031
python3 -I proxy.py 75 1 routine-first        (the routine fact placed first): op 1.0155, unit 1.0103, code 1.0052, look 1.0028 at w0.3
python3 -I proxy.py 30 <seed>                 (pilot size, 30 per rule kind): every ratio between 0.998 and 1.015
```

- **Result.** Every rule kind lies inside the step-3 band at every weight, in every seed and in both context orders. The ratio ranges from 0.998 to 1.019. That compares with version 0.4's 0.73 to 0.96 in the operator and unit kinds. **On the stand-in measure, the dose imbalance that RT-380 found is gone.** That is what the closure claims, so RT-380 is closed.
- **But the ratio is not exactly 1, as section 9 step 3 says it should be.** I split the stand-in dose by region:

  ```
  python3 -I decomp.py 75 1     (w0.3, mean per item, prompt-rule | routine)
  op    context 23.42 | 23.42   question+template 6.81 | 6.80   candidate 1.00 | 1.53   final-question tokens matching the donor's: P 1029/2359  R 1036/2359
  unit  context 21.48 | 21.48   question+template 8.31 | 8.28   candidate 1.00 | 1.33   P 1004/2791  R 1016/2791
  code  context 29.08 | 29.08   question+template 5.06 | 5.06   candidate 1.00 | 1.22   P 1764/2481  R 1764/2481
  look  context 52.35 | 52.35   question+template 7.83 | 7.78   candidate 1.00 | 1.21   P  569/1563  R  585/1563
  candidate length, routine minus prompt-rule: (op, capitals) +1.44, 17 of 25 pairs, up to 4; (unit, capitals) +1.00; (code, capitals) +1.05;
     (look, capitals) +0.89; opposites +0.08 to +0.28; every other pairing 0
  ```

  The shared context gives exactly the same dose in both cells, as claimed. What is left over comes from the candidates:
  - **The routine twin's answer is often longer.** Capitals such as "Buenos Aires" (2 tokens), "Port-au-Prince" (5) and "Antananarivo" (4) are longer than every prompt-rule answer, which is a number, a three-letter word or a colour, each 1 token.
  - **So the changed span is not "the same span in both twins".** Section 3 says it is (lines 150 to 152). It is not.
- **The donor's final question does not line up with the recipient's.** Donors must be at least as long, so a donor's context is usually longer, and its final question starts later. Only 15% to 70% of donor draws had the same context length. Only 22% to 71% of final-question tokens matched the donor's. That contradicts section 3 ("in the final question every token matches the donor's in both cells") and section 5 (lines 436 to 438). On this proxy it does no harm, because both cells meet the same donor tokens there. But the sentence is false, and step 3's rule "anything else means the generator does not build what section 5 describes" would fire on a correct generator (RT-390).

**RT-345 stays open (ARGUED, with measured shares).** The shared context changes what can be argued. If the model is causal, meaning that each position sees only earlier positions (step 4a confirms this), then two things are equal in the two twins at every position inside the shared context:
- the true block sums, because the twins have the same text up to that point;
- the replacement sums, because the donor pair's two twins share their context too.

So under both methods, the real dose can differ between the cells **only after the shared context**: in the final question, the template's closing tokens and the candidate. I measured how much of the changed span that tail is:

```
python3 -I tail.py
op   changed span 40.5 positions, after the shared context 11.0 (share 0.27)   [routine twin 0.28]
unit 37.2, 12.4 (0.33)  [0.34]      code 60.2, 11.3 (0.19)  [0.19]      look 71.2, 11.7 (0.16)  [0.17]
```

If the real distance per position in that tail differs between the cells by a factor f, the cells' ratio moves by about the tail share times (f − 1). Step 4b's 10% limit would then be broken when the tail distances differ by more than about:
- 30% in the unit kind;
- 37% in the operator kind;
- 53% in the letter-code kind;
- 63% in the lookup kind.

That is a real margin, but not a guarantee. The prompt-rule question ("What does the rule give for them?") and the routine question ("What is the capital of the country?") are different words that sit right where the answer is computed. Only the model can say how different their block sums are. So RT-345 is still owed at step 4b, as the design says. No token count can stand in for that measurement any longer (RT-391).

### The fixed-wording table and the chat template (MEASURED, real tokeniser)

```
python3 -I tok_check.py
every one of the 14 rows: prompt-rule count = routine count = the table's count (8, 8, 8, 9, 7, 9, 9, 8, 8, 8, 9, 8, 8, 8)
the same pairs stay equal with a newline before the question (each +1) and with no leading space
the same pairs stay equal when measured after a real context (count of ctx+question minus count of ctx)
```

- **The table is right.** All fourteen rows recount exactly. The table covers exactly the fourteen pairings the exclusions allow.
- **The equality is robust.** It does not depend on how the question is joined to the context.
- **How the template wraps an item:**
  - twelve tokens come before the user text: `<|message_system|><|content_text|>Thinking effort level: 0<|end_message|><|message_user|><|content_text|>`;
  - one token comes after it: `<|end_message|>`;
  - the template renders nothing for the start of the model's reply. Like the tokeniser record, I found no switch for it, so the reply opening is still step 4a's to settle;
  - the tokeniser adds no start-of-text token.
- **Positions line up within a pair.** Across 2,800 pairs built in both context orders, the two twins' prompts never differed in token length. So the final questions start at the same position, and the candidates of both twins start at the same position, as the design assumes.
- **Positions do not line up with the donor** (above).
- **Candidates have no leading space.** A candidate placed straight after `<|content_text|>` is tokenised without a leading space. Every colour, every number of up to three digits, and 137 of 138 three-letter words are then one token ("yew" is two). Capitals range from one token to five. The equal-length rule must be applied at this position, which step 4a fixes.

### The other findings

- **RT-381, the unit kind: closed (MEASURED).**
  - **The facts are out of the question.** The unit facts now sit in the shared context.
  - **The table matches every unit pairing.** It gives equal wordings for the unit kind with capitals (9 tokens each), opposites (7) and everyday colours (9).
  - **The unit kind fills completely.** In my build, all 75 unit pairs were made, against 25 to 50 of 75 under version 0.4.
- **RT-382, phrasings chosen item by item: closed (MEASURED).**
  - **One wording per pairing.** There is one wording per pairing, so nothing varies from item to item.
  - **What remains is by design.** A fixed difference between the two cells within each pairing remains, and that is intended.
  - **A side effect.** The routine wording now varies with the rule kind. Everyday colours are asked as "What colour is the object most often?" behind the operator and letter-code rules, but as "Usually, what colour is the object?" behind the unit rule. That wording splits "Usually" into two odd pieces. Capitals and opposites have the same pattern. So a per-routine-kind report mixes two or three wordings (RT-397).
- **RT-383, colours and the overlap check: closed, with a condition (ARGUED).**
  - **The exemption is stated.** It is in the body (lines 477 to 481).
  - **No pilot-to-test leak that matters.** What varies between items (the invented words, the tables and the objects) is still split. Nothing in the design is tuned on which colour an answer is. So sharing the colour names between pilot and test gives the pilot no information about any test item.
  - **The condition.** The same paragraph still says the script fails "if any test item's candidate comes from a half-A pool" (lines 481 to 482). The colour list has to be named as one shared pool, or that check fails on every colour item (RT-396).
  - **Colour lengths.** With the real tokeniser, all eleven basic colours, and "violet", "gold", "silver", "teal" and "tan", are one token at the answer position. So the lookup tables can always meet the equal-length rule.
- **RT-384, the everyday-colours pool: closed on paper (ARGUED).** The body asks for at least 120 objects. It keeps out wrong colours that are commonly true of the object, and objects whose colour depends on the country. It reports the spread of right answers. The list itself is owed at step 3.
- **RT-385, the copying rule: closed, with a condition (MEASURED).**
  - **The wording now catches what it missed.** It catches "unhappy" against "happy" and "Tunis" against "Tunisia", and it exempts numbers.
  - **Its scope is still unclear.** It does not say whether it also covers prompt-rule candidates, which now share a context with the routine fact (RT-395).
- **RT-386, the margin fallback: closed (MEASURED, grep).** Lines 507 to 510 withdraw it. Going beyond a third returns the design to John, on pilot or test pairs, counted from the pairs that pass the confidence check.
- **RT-387, a free estimate for the average method: closed as text, with a condition (MEASURED).**

  ```
  python3 -I avg387.py
  op    text span, routine minus prompt-rule: +0.48 tokens (max 4); invented/symbol token count difference: always 0; final-question share 0.171 / 0.169
  unit  +0.58 (max 3); 0; 0.236 / 0.233     code +0.30 (max 4); 0; 0.112 / 0.112     look +0.26 (max 2); 0; 0.112 / 0.111
  ```

  - **It is well defined if read as counts.** Counted that way, the invented-word count and the final-question count are equal in every pair. The shares differ only through the candidate length.
  - **It cannot fail.** Like the swap proxy, it passes by construction (RT-391).
- **RT-388, the lookup kind's donors: not closed (MEASURED).** See RT-392.
- **RT-389, text gaps: closed (MEASURED, grep).** The four repairs are all in place:
  - the pilot's size is stated (line 568);
  - "within 10%" is defined as a ratio from 0.90 to 1.10 (lines 512 to 514);
  - the stale "question template" sentence and the "few tokens" sentence are gone;
  - the notes at the head of the first and second change logs now list every replaced rule that version 0.4's check named.

  New stale text is listed under RT-390 and RT-397.
- **Conditions on RT-340 (the sample-size simulation) and RT-371 (the leave-one-kind-out leak): met (MEASURED, grep).** The places are given in the table above.
- **Condition on RT-372, the letter code: met (MEASURED).**

  ```
  inline: half-B stand-in pool of 70 three-letter words with three different letters;
  items buildable with the five extra letters chosen to fit four wrong words of equal token length: 1771 of 2000 (89%)
  ```

### Press on what the shared context changes (item 3 of the brief)

- **Both cells now resolve a reference (ARGUED).**
  - **What changed.** The routine twin must find "the country" in the context, as section 1 now says. The prompt-rule item must too: "them" refers to a and b, and "it" to the word to look up. Lookup is now two steps, from "the word to look up" to the table, where version 0.4's question named the word. So both cells take on one step of reference. That is roughly even, and it does not by itself bias the gap between the cells (G).
  - **The distances are not even.** In the order the examples imply (rule, rule facts, routine fact, question), the routine fact sits right before the question, 0 tokens away. The prompt-rule item's own fact ends 6 to 8 tokens earlier on average (range 5 to 10), and the lookup and letter-code tables end 16 to 18 tokens earlier (`dist.py`). The design does not fix the order (RT-394).
- **Can the prompt-rule item be answered from patterns in the context alone? (ARGUED)** I found no new shortcut. The final question carries nothing about the item, so the answer must come from the context. The "rule is needed" check (rule sentence removed, accuracy at chance plus 0.10 or less) still applies, and it still makes sense when the rule's facts are left in.
- **Distractors now differ between the cells (ARGUED).**
  - **What each cell has to ignore.** The prompt-rule item now carries one short, familiar, irrelevant sentence, the routine fact. The routine twin carries a long, invented, irrelevant rule.
  - **Only one side is checked.** The routine side has a baseline check (answered as well behind the rule). The prompt-rule side has none (RT-393).
  - **Number distractors are avoided.** The pairing exclusions mean that no arithmetic rule ever sits beside a sum or a product.
  - **The swap's intrusions are symmetric.** The swap puts the donor's facts into both cells at the same context positions, for example the donor's "Japan" at the place of "France", and the donor's operands at the place of the recipient's.
- **The colour exemption (ARGUED).** No leak that matters, as under RT-383. The text conflict is RT-396.
- **The copying rule now works for the routine twins.** For prompt-rule candidates, about 1% of letter-code items have a candidate that matches or contains a word of the routine fact ("ice" and "Iceland", "nut" and "walnut"). Nothing says whether the rule applies there (RT-395).
- **Do the step-3 thresholds still mean anything? Only as a check that the generator builds what section 5 describes.** A correct build gives 0.998 to 1.028, so the band always passes. The remaining risk is invisible to it (RT-391).
- **The average-method estimate is well defined if read as counts.** It passes by construction (RT-387 above).
- **Lookup size classes at the pilot's 120 pairs: no.** See RT-392.
- **The pool arithmetic holds (MEASURED).**
  - **The five routine kinds.** 75 sums + 60 products + 75 capitals + 75 opposites + 60 everyday colours = 345.
  - **The sums and products underneath.** Half B holds 64 ordered products from 2 to 12 with an answer of 40 or more (60 if the split is at more than 40), and 1,223 ordered sums.
  - **The pairing exclusions can be met at 300 pairs.** The operator and unit kinds need 150 pairs from capitals, opposites and everyday colours, and those three supply 210.
  - **One contradiction.** Section 5 still says "at most about 360 distinct pairs" at line 560, against 345 at line 391 (RT-397).
- **Rules stated only in a change log, or contradicted between sections.** I found no rule that lives only in a change log. Contradictions between sections are listed under RT-390 and RT-397, and the ruling premise under RT-391.

---

## New findings

| # | Finding | Severity | Label |
|---|---|---|---|
| RT-390 | Three claims about alignment are false: the donor's final question lines up with the recipient's; both twins get the same span; the stand-in ratio is "exactly 1". So step 3's "anything else means the generator is wrong" would fire on a correct build | worth-noting | MEASURED |
| RT-391 | The free step-3 checks now pass by construction and cannot forecast RT-345. John's ruling on choice 3 rests on "the dose question settled by the free real-tokeniser check at step 3" | serious | MEASURED (proxy), ARGUED |
| RT-392 | The lookup size-class rule (at least six pairs per group) cannot be met at the pilot size unless lookup has only one routine kind. That clashes with the pairing table, which is fixed on the pilot | serious | MEASURED (arithmetic, proxy) |
| RT-393 | The "answered as well behind its rule" check compares against "the same question with no preamble". Under version 0.5 that question cannot be answered, and there is no matching check for the prompt-rule side | serious | ARGUED (text) |
| RT-394 | The order of the three context parts is not fixed. Two fixed wordings refer ambiguously in the lookup kind | worth-noting | MEASURED (distances), ARGUED (ambiguity) |
| RT-395 | The copying rule's scope for prompt-rule candidates, and the missing reverse rule | worth-noting | MEASURED (count) |
| RT-396 | The colour exemption conflicts with "no test candidate from a half-A pool" | worth-noting | ARGUED |
| RT-397 | Stale or conflicting text: "360" against "345"; section 9 step 1; routine wordings that vary by rule kind | worth-noting | MEASURED (grep) |

**RT-390, the alignment claims (worth-noting, MEASURED).**
- **The donor's final question does not line up.** Donors must be at least as long, so their contexts usually run longer and their final questions start later. Only 15% to 70% of donor draws had the same context length, and only 22% to 71% of final-question tokens matched the donor's. Section 3 (lines 145 to 147) and section 5 (lines 436 to 438) say every token matches.
- **The twins' spans are not the same.** The routine twin's candidate is longer in most capitals pairings, by 1.0 to 1.4 tokens on average and up to 4. So section 3's "the swap changes the same span in both twins" and section 5's "differ only in their final questions" are not true of the scored positions.
- **The step-3 diagnostic would misfire.** A correct build gives ratios from 1.002 to 1.019, and 1.028 at weight 0 even with donors of the same context length.
- **Fix:**
  - correct the three sentences;
  - replace "exactly 1" with a stated tolerance;
  - either require each pair's two right answers to have the same token count (for example, by using single-token capitals behind rules whose answers are one token), or report results by candidate length. Candidate positions are where the score is read, so any dose difference matters most there.

**RT-391, the free check can no longer settle the dose question (serious, MEASURED and ARGUED).**
- **Both free checks pass by construction.** On the swap proxy and on the average-method estimate, the two cells are equal throughout the shared context, by construction.
- **The remaining risk is out of their reach.** It lies in the last 11 to 13 positions: the final question, the template's closing tokens and the candidate. Those are 16% to 34% of the changed span. There, the two twins' true block sums differ because the words differ, and no token count can say by how much.
- **So the dose question has moved to a paid step.** It can now be settled only at step 4b, which needs a rented machine.
- **This contradicts the record of the ruling.** Section 11 and the ruling file record choice 3 as "the dose question … settled by the free check with the real tokeniser before any rental". Section 5 of the same design says the real distances "can still differ" and that RT-345 closes only at step 4b.
- **The design does keep to the ruling's substance.** The routine twin still carries the rule as a preamble. But one of the premises John was given no longer holds.
- **Fix:**
  - restate step 3's swap and average estimates as checks that the generator builds what section 5 describes;
  - have step 3 report the tail shares above per rule kind, so that step 4b knows how much difference per position the 10% limit tolerates;
  - when step 4 is priced for John, tell him plainly that the free check passed by construction and settled nothing about the real dose.

**RT-392, lookup size classes at the pilot size (serious, MEASURED).**
- **The arithmetic.** Section 3 requires at least six pairs in every group of rule kind, routine kind and size class. Lookup has three size classes, so each routine kind it uses needs at least 18 pairs. The pilot has 30 lookup pairs (line 568). So at the pilot, lookup can use only one routine kind.
- **Two outcomes, both bad:**
  - **If the generator obeys the rule,** lookup is paired with one routine kind only. Its other pairings are never tested by the "answered as well behind its rule" check. Yet that check's table "is fixed on the pilot items … before the test set is generated" (line 496). So lookup either goes into the test paired with one routine kind, which makes leaving out lookup the same as leaving out that routine kind, or it goes in with pairings that were never checked. The text says neither.
  - **If the generator spreads lookup over its four routine kinds,** the groups have two or three pairs. In my build, 10 to 12 of the 30 lookup pairs then had no donor at all (seeds 1 to 3). With one routine kind, 3 of 30 had none.
- **At the test size,** 75 lookup pairs over four routine kinds give six or seven a group. Even so, 9 to 15 of 75 had no donor, and 46 to 57 had fewer than five.
- **Fix:** apply the six-pair floor only at the test size, or drop it at the pilot and say how lookup's pairings are checked there. Then report donor shortfalls by size class, as RT-388 asked.

**RT-393, the routine-side baseline check under the shared context (serious, ARGUED).**
- **What the text says.** Line 491 compares each routine twin's margin "behind its rule" with "the same question's margin with no preamble".
- **Why that cannot work now.** Under version 0.5, the question is "What is the capital of the country?". With no preamble, it cannot be answered, so read literally the check fails every routine kind and strikes every pairing.
- **Fix, routine side.** Define the comparison as the routine fact plus the fixed routine question, without the rule or its facts.
- **Fix, prompt-rule side.** Add the mirror check: each prompt-rule item's margin with and without the routine fact. The prompt-rule cell now also ignores an irrelevant sentence, and nothing measures that.

This is a one-sentence repair, but it governs a table that is written into the registration.

**RT-394, the context order and two ambiguous wordings (worth-noting).**
- **The order is not fixed.** Section 5 never fixes the order of the rule, the rule's facts and the routine fact.
- **Distance (MEASURED).** In the order the examples imply, the prompt-rule item's own fact sits 6 to 8 tokens further from the question than the routine fact does, and the tables 16 to 18 tokens further.
- **Fix for the order.** Fix the order in the specification. Better still, balance it across items and report results by order.
- **Ambiguity (ARGUED).**
  - **The routine twin in lookup with opposites.** It reads "The word to look up is tovjot. The word is happy. What is the opposite of the word?" There, "the word" fits two sentences.
  - **The prompt-rule item in lookup with capitals.** It reads "… The country is France. What colour does the table give it?" The nearest thing "it" can refer to is the country.
  - **Fix for the ambiguity.** Change "the word to look up" to "the name to look up", and the prompt-rule wording to "… give the name?". Then recount the table.

**RT-395, the copying rule's scope (worth-noting, MEASURED).**
- **The rule does not say whether it covers prompt-rule candidates.** The routine fact now sits in the prompt-rule item's context too. In my stand-in, 0.8% (letter code with capitals) and 1.1% (letter code with everyday colours) of items had a candidate that is, contains, or is contained in a word of the routine fact. Examples are "nut" with "walnut", and "tan" with "Bhutan".
- **The reverse rule is missing.** Section 5 bars the rule's answer from the routine twin's candidates. Nothing bars the routine answer from the prompt-rule item's candidates. A three-letter colour such as "red" or "tan" could be a letter-code word behind an everyday-colours twin.
- **Fix:** state both.

**RT-396, the colour pool and the half-A candidate rule (worth-noting, ARGUED).**
- **The conflict.** The answer-value check exempts colours, but the next sentence fails any test candidate taken from a half-A pool.
- **Fix:** declare the colour list a single shared pool, exempt from that sentence too.
- **A related gap, not new in version 0.5.** "Capitals of neighbouring countries" can fall in half A. The specification should say whether wrong answers for capitals must also come from half B, and report what that costs.

**RT-397, stale or conflicting text (worth-noting, MEASURED by grep).**
- **The pair count.** Line 560 says "at most about 360 distinct pairs" against 345 at line 391.
- **Section 9, step 1.** It still describes the check of version 0.4: "RT-370 to RT-379 … under the equal-length construction".
- **Routine wordings.** They differ by rule kind ("capital" or "capital city"; "What is the opposite…" or "Give the opposite…"; "most often" or "Usually, …"). That is allowed, but per-routine-kind results should be reported by wording.
- **Section 10, choice 3.** It is left as John saw it, which is right for a record, but it should be marked as describing version 0.4.

---

## Verdict

**Version 0.5 is nearly ready for the battery specification at step 3, with RT-345 (the finding that the swap's dose differed between the two task groups) carried as an open fatal item.**
- **What is fixed.** Measured with the real tokeniser, the shared-context construction fixes what version 0.4's check found:
  - every rule kind's stand-in dose ratio is between 0.998 and 1.019, against 0.73 to 0.96 before;
  - every row of the fixed-wording table recounts exactly;
  - the unit kind now fills completely;
  - within a pair, the final questions and the candidates start at the same positions.
- **What the measurement shows about RT-345.** By construction, the free checks can no longer see the dose risk that remains. That risk lies in the last 11 to 13 positions of each item, where the two questions differ. Only step 4b, on a rented machine, can settle it, and John should be told so when step 4 is priced (RT-391).
- **Fix in the design text before the specification is committed.** Two things must be fixed first, because the specification has to follow them:
  - the baseline check's comparison item, which read literally strikes every pairing, together with its missing counterpart on the prompt-rule side (RT-393);
  - the lookup size-class rule, which cannot be met at the pilot's 30 lookup pairs without tying lookup to a single routine kind (RT-392).
- **Fix in the same pass.** The false alignment sentences and the "exactly 1" diagnostic (RT-390), and the order and wording fixes (RT-394), are small and should go in the same pass.
- **Can go with the specification.** RT-395 to RT-397 can be settled inside the specification itself.
---

## The filer's check (not part of the closure check)

*Written by the design's author, 2026-11-21. It closes nothing.*

- **RT-393, the baseline check's comparison item.** Confirmed. Line 491 compares each routine twin with "the same question's margin with no preamble", and under version 0.5 the question ("What is the capital of the country?") cannot be answered with no preamble.
- **RT-397, the pair count.** Confirmed. Line 560 still says "at most about 360 distinct pairs", against 345 in section 5's pool arithmetic.
- **The reviewer's folder.** Its scripts are in its own folder, and nothing it reports draws on the author's files.
- **RT-391 bears on a ruling, so it goes to John in plain words.** When John ruled on choice 3 (2026-11-21), he was told the dose question would be settled by the free real-tokeniser check before any rental. Under version 0.5 the free check passes by construction, and the remaining risk can only be measured on the rented machine at step 4b. His ruling's substance, routine twins, stands. One of its stated premises no longer holds.
- **Where things stand.** RT-380 to RT-382 and RT-386 to RT-389 close, some with conditions. RT-383 to RT-385 close with conditions. RT-388 does not close, through RT-392. RT-345 stays open until step 4b. The reviewer finds version 0.5 nearly ready for the battery specification. RT-392 and RT-393 must be fixed in the design first. RT-390 and RT-394 should be fixed in the same pass. RT-395 to RT-397 can be settled in the specification.
