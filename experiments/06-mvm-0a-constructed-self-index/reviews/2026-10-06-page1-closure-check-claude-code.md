# Page 1 closure check: the free model's battery clause (inside review of proposal version 4, finding RT-237, fatal)

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree, on
branch `check-page1-closure`, cut from the branch that records John's
2026-10-06 rulings (`rulings-2026-10-06-gate-a-v4`, pull request 103) at
`5a4b45b`. The method and the script were committed and pushed at `f8c6be8`
before the script ran on any model:
`docs/2026-10-06-page1-closure-check-method.md`. Laptop only, on the
processor. Nothing was trained, rented or spent: $0.*

*This session wrote none of: the inside review, the drafted fix (the inside
dispositions file), its first check (pull request 96), the ruling record
(pull request 103), its check (pull request 104), or the decision code on
pull request 105. It did not write version 5 and changed no ruling, proposal
or code file.*

## The verdict, in one paragraph

**The numbers behind the ruling reproduce exactly, and the ruled sentence
claims no more than the count shows. Page 1 cannot be marked closed yet.**
What blocks it is that the fix has not landed anywhere: version 5, the
registration text, does not exist on any branch, so there is no commit that
carries the new clause, and the closure rule needs one. Part 1 of the owed
check (every clause of the gate tied to a named output field, and no sentence
setting a condition on batteries) can only be run on that text. The ruling
record already says so: page 1's closure check runs on version 5 (its "What
is now owed" list, item 6). One thing version 5's writer must also settle:
page 1's adopted text gives the new line its own "two seeds of three" clause,
and page 7, ruled the same day, abolished separate per-condition seed counts.

## 1. Do 1,546 of 3,000 and "two seeds of three" reproduce? Yes, exactly

`check_counts.py` (beside this file) imports neither the author's script
(`lesion_content_check.py`) nor the first check's (`candidate_counts_independent.py`).
It finds the line with whole-number arithmetic only, reads the four allowed
answers off each episode's words rather than its stored values, runs its own
forward pass, and re-checks every model file's fingerprint. Full output:
`check_counts.out.txt` and `check_counts.json`.

- **The line: 1,546.** It is the smallest count of 3,000 that a model
  guessing among the eight value words (right half the time on this count)
  would reach no more than one time in twenty. One fewer would not meet that.
- **Counts with the acting channel zeroed, own-directed answers that are one
  of the four allowed (of 3,000):**

| Model | Seeds 0 / 1 / 2 | At or over 1,546 | Same as the author's file |
|---|---|---|---|
| Arm T | 3,000 / 3,000 / 3,000 | 3 of 3 | yes |
| Arm C | 2,236 / 2,160 / 2,132 | 3 of 3 | yes |
| Arm M | 2,770 / 2,686 / 2,660 | 3 of 3 | yes |
| **Arm F, the free model** | **2,100 / 2,238 / 2,324** | **3 of 3** | yes |
| Competing solver | 2,784 / 2,880 / 2,768 | 3 of 3 | yes |
| Untrained weights | 0 / 620 / 726 | 0 of 3 | yes |

18 of 18 counts, and the 18 correct-answer counts beside them, equal
`out-lesion-content-check/lesion_content_check.json`. The free model clears
the line by 554 to 778 episodes; the untrained models miss it by 820 or more.
"Two seeds of three": every trained arm holds on 3 of 3, the untrained on 0
of 3, so no verdict depends on how the seed rule is worded.

**On the words "two seeds of three".** The ruling says "on two seeds of
three"; the adopted drafted text says "on at least two seeds of three, the
third reported", which matches version 4's wording for the collapse line
(line 2270). So the intent is "at least two", not "exactly two". But page 7
(split seeds, outside finding A10), ruled the same day, says a seed counts
only if it passes **every** gate condition, and "separate two-of-three counts
per condition are not used". Page 1's text changes 1, 3 and 4 were drafted
before page 7 and each give the new line its own two-of-three clause (change
4 says "each with its two-of-three clause"). Version 5 should write the line
as a per-seed condition, counted under page 7's single seed rule. On the toy
this changes nothing: arm F's three seeds each pass both the collapse (528,
555 and 582 correct, under the bar of 790) and the new line. The decision
code on pull request 105 already does it page 7's way.

## 2. The 2,257 caveat, and whether the ruled sentence over-claims. It does not

**What the caveat is.** The first check of the dispositions (pull request 96,
section 6) found that a model which has lost track of *which item* the action
names, and answers the step-on of any of the eight values shown in the
episode, would score about 2,257 of 3,000. That clears 1,546 and beats the
free model's lowest seed (2,100). So the count cannot show that the model
still finds the right item. Reproduced here: **2,256.8**.

**Does the sentence "the model still answers with the successor of a value it
was shown" claim more than that?** It was tested two ways.

| Answer rule (no model run) | Expected count of 3,000 | Clears 1,546? |
|---|---|---|
| Guess among the eight value words | 1,500.0 | no |
| Step on any of the eight values shown (the caveat) | 2,256.8 | **yes** |
| Step on one of the four values on the other item | 1,513.5 | no |
| Copy a value on the named item without stepping it on | 1,261.5 | no |
| Copy any value shown without stepping it on | 1,372.5 | no |

The count does test the "successor" part: a model that copies a shown value
without stepping it on fails. It does not test the item part: the item-blind
rule passes. That is what the ruled sentence says, no more.

Measured on the models directly, with the channel zeroed, the free model's
answers are the step-on of some value shown on 2,778, 3,000 and 3,000 of
3,000 (seeds 0, 1, 2); every other trained model is at 2,946 or more. So the
sentence is true of the models it will be written about.

One wording caution for version 5: the sentence is about a count over 3,000
episodes, not every answer. Drafted text change 2 already words it that way
("It shows that the model still answers with the successor of a value it was
shown; it does **not** show that the model still uses the right item").
Keep the second half; dropping it would be the over-claim.

## 3. Where the old clause still stands: the list for version 5's writer

Searches and their full output: `battery_search.out.txt`. No version 5 or
registration draft of the successor exists on any branch, so the places are
in version 4 (`docs/successor-experiment-proposal-2026-10-03-v4.md`) and the
code.

**In version 4, must change (covered by the adopted drafted text, inside
dispositions lines 140 to 196):**

1. **Line 2223**, section 8.2, last bullet: "the ownership-free state and
   syntax batteries **must hold**." The clause itself (text change 1).
2. **Line 2270**, section 9, the row "Ownership-lesion collapse threshold":
   "the ownership-free batteries must hold" (text change 3; page 7 also
   rewrites this row's seed wording).
3. **Lines 2063 to 2065**, section 7.4, the list of what is frozen: "the
   ownership-lesion rule with its two-of-three clause" (text change 4, to be
   reconciled with page 7 as in part 1 above).
4. **Line 2246**, end of section 8.2's paragraph "On the toy, described
   honestly": add the toy figures and the caveat (text change 2).
5. **Section 8.2 after its bullets, and section 11, step 3 (line 2483)**: the
   sentence saying the gate code writes the lesioned own-directed count and
   the lesioned candidate count (text change 5).

**In version 4, should change but no drafted text covers it:**

6. **Lines 2203 to 2205**, section 8.2's opening, which credits the rule to
   "the queue ruling, page 1h; refined by the Gate C rulings, RT-220". It
   should also cite John's ruling of 2026-10-06 on RT-237, which replaced
   part of page 1h.
7. **Lines 3141 to 3144**, the list of ruled decisions, item 10: "Its shape
   was ruled on 2026-09-25 (the queue ruling, page 1h)". Same addition.
8. **Line 2133**, the report list, item 15, "the ownership-lesion result":
   optional. Adding "with the ownership-free count" would make the report
   list match the gate.

**In version 4, not to change:** lines 263 and 436 to 438 (the closed design's
own question sets, as history) and line 1769 ("the control battery", a
different thing).

**In the code:**

9. **The frozen successor code on main**,
   `experiments/08-successor-degree/src/procedure.py`: the gate (lines 180 to
   189) writes no candidate count, and the rule for reading arm F (lines 739
   to 750) checks only the collapse. It never coded the battery clause, which
   is why the clause could never be evaluated, so there is nothing to delete.
   The missing line is added on pull request 105 (`measure.py` lines 74 and
   160 to 200; `procedure.py` lines 207 to 219), which is open, unmerged, and
   owed its check (pull request 107). Until it merges, the registered code
   cannot evaluate the new line.
10. **Not to change:** the rehearsal's gate (`experiments/rehearsal-successor-measure/src/repairs.py`,
    line 137), which is the rehearsal and not the registered code; and the
    launcher comment "no frozen batteries (the successor has none)"
    (`launch_successor.sh` line 28), which is correct.

**In the rulings and records, nothing to change.** The page 1h ruling of
2026-09-26 (`docs/rulings/2026-09-26-weekend-1-queue.md`, lines 66 to 76)
and the Gate C ruling of the same day (`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`,
line 170) already carry dated notes. Earlier proposals (versions 1 to 3), the
review, the packets, the dispositions and STATUS.md record the clause as
history and stay as written.

## 4. Can page 1 be marked closed? Not yet

Against the owed check (inside dispositions lines 232 to 267) and the closure
rule (`docs/outside-review-protocol.md`, "The closure rule"):

| What closure needs | State | Why |
|---|---|---|
| A commit that lands the fix in the registration text | **not done** | Version 5 does not exist |
| Check item 1: every gate clause has a named output field; no sentence sets a condition on batteries | **not yet possible** | Needs version 5's text. The field exists in the code on pull request 105 (`lesioned_candidate_own_correct`), not on main |
| Check item 2: the figures recompute from independent code, the line computed and not typed | **done** | 18 of 18 counts equal; line 1,546 |
| Check item 3: both ends, trained models pass and untrained fail | **done** | Every trained model 3 of 3; untrained 0 of 3 |
| Check item 4: the registered gate code writes the two fields | **owed later** | Pull request 105, once checked and merged |

**So what is left is: version 5 written (with items 1 to 7 above and page
7's seed rule), pull request 105 checked and merged, then a session that
wrote neither re-runs check item 1 on version 5.** Items 2 and 3 need not be
repeated unless version 5 changes the episodes, the models or the line.

## What this session did not do

It did not write version 5, change any ruling or proposal, or run the code on
pull request 105. It did not repeat the first check's token-position method;
it used a third way of reading the episodes on purpose.
