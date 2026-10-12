# Page 1 closure check (the free model's battery clause): method, committed before any output

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree, on
branch `check-page1-closure`, cut from the branch that records John's
2026-10-06 rulings (`rulings-2026-10-06-gate-a-v4`, pull request 103) at
`5a4b45b`, because the files this check reads exist only there and on the
branches under it. **This file and the script beside it are committed and
pushed before the script is run on any model.** The output, with what it
printed, is a later commit. Laptop only, on the processor. Nothing is
trained, rented or spent: $0.*

*Written under the workspace plain-language rule. This session wrote none of:
the inside review of proposal version 4, the drafted fix (the inside
dispositions file), its first check (pull request 96), the ruling record
(pull request 103) or its check (pull request 104). It does not write
version 5, the registration text, and changes no ruling, proposal or code
file.*

## What is being checked

Page 1 of the registration-review packet on proposal version 4 dealt with the
review's only fatal finding (RT-237): the free model's channel-removal check
ends with "the ownership-free batteries must hold", and the successor's task
has no batteries, so the check could never be passed and the free model could
never be read. John ruled on 2026-10-06, option (a): replace the clause with
a count, a line of 1,546 of 3,000, on two seeds of three, and have the
registered sentence claim only that the model still answers with the
successor of a value it was shown (the "2,257 caveat").

The closure rule (`docs/outside-review-protocol.md`, "The closure rule") says
a fatal finding is closed only by a commit that lands the fix plus a measured
check, by another session, that the fix does what it says. This check does
the parts of that which can be done before version 5 exists, and says what
cannot.

## The four questions, and how each is answered

**1. Do 1,546 of 3,000, and "two seeds of three", reproduce exactly from
committed code and data?**

A new script, `check_counts.py`, in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-06-page1-closure-check-scripts/`.
It does not import the author's script (`lesion_content_check.py`) or the
first checker's (`candidate_counts_independent.py`, pull request 96). It uses
only the shared episode generator (`grammar.py`), the model builder
(`repairs.build_for`) and the committed model files, and differs from both
earlier scripts on purpose:

- **The line** is found with whole-number arithmetic only: the smallest k
  for which the number of ways to get k or more heads in 3,000 fair tosses,
  times 20, is at most 2 to the power 3,000. No floating point, no scipy, no
  fractions library. It must come out at 1,546.
- **The four allowed answers** are worked out by turning each episode's
  tokens back into words and reading the words: the item word in the action
  turn marked as the model's own, then the four assignment turns for that
  item word, then each value word's successor by its number. Neither the
  episode's stored `values` field nor token-position arithmetic is used.
- **The model's answers** are taken with a forward pass written here, from
  `G.batch` on the episodes, not through `training.make_data`.
- **The fingerprints** of the model files are recomputed against
  `out-repairs/models/SHA256SUMS`, and any mismatch stops the script.

It runs on the 3,000 gate episodes (1,500 development pairs, generator seed
99), with the acting channel zeroed, for the fifteen trained models (arms T,
C, M and F and the competing solver, seeds 0 to 2) and three untrained
models of the free model's build (seeds 1000, 1001, 1002, as the author
drew them). For each it prints the count of own-directed answers that are
one of the four allowed answers, and compares every count with
`out-lesion-content-check/lesion_content_check.json`. Then it applies "two
seeds of three" as a rule (at least two of the three seeds at or over the
line) and prints the verdict per arm.

*What would count against the ruling's numbers:* a line other than 1,546; any
count differing from the committed file; the free model holding on fewer
than two seeds; any untrained model holding on two or more.

*What "two seeds of three, exactly" will also be checked for:* the words.
The ruling says "on two seeds of three"; the drafted text says "on at least
two seeds of three, the third reported". This check will read version 4's
existing two-of-three wording for the collapse line and say whether the new
line's wording matches it, or could be read as "exactly two".

**2. What is the 2,257 caveat, and does the ruled sentence claim no more than
the count shows?**

The same script computes, on the same episodes and without running a model,
the count each of these answer rules would get:

- guessing uniformly among the eight value words (expected 1,500);
- the successor of one of the eight values shown, any item (the caveat; the
  first check reported about 2,257);
- the successor of one of the four values on the other item;
- the value shown on the named item, **without** taking the successor;
- the value shown on any item, without the successor.

The last two test the word "successor" in the ruled sentence: if a model that
copies a shown value without stepping it on would also pass 1,546, the
sentence claims more than the count shows. It also counts, for each trained
model with the channel zeroed, how many own-directed answers are the
successor of **any** of the eight values shown, which is the ruled sentence
measured directly on the models.

*What would count against the ruled sentence:* a rule that does not take
successors clearing 1,546; or the free model's answers, with the channel
zeroed, being the successor of a shown value on fewer than 1,546 of 3,000
(the sentence would then say more than the models do).

**3. Where does the old battery clause still stand?**

A search of every tracked file on this branch (the ruling branch, which
carries version 4, the dispositions and the rulings) and on `origin/main`,
for `batter` (any case), plus "ownership-free" and "state and syntax". Every
hit is read and sorted into one of:

- **must change**: it sets or repeats the old clause as a condition on the
  successor's free model;
- **history**: it records, quotes or rules on the clause (rulings, reviews,
  dispositions, checks) and stays as written;
- **unrelated**: the closed design's own batteries, or "control battery".

The code is searched the same way, and the rehearsal's gate code
(`repairs.py`, the gate stage) is read to see whether it evaluates any
battery, writes the new count, or neither. Registration drafts are looked for
under `drafts/`, `docs/` and `experiments/` (any version 5 or registration
draft of the successor).

**4. Can page 1 be marked closed?**

Measured against the closure rule's three parts, as the inside dispositions
file lists them (its "measured check another session must run", items 1 to
4): a commit that lands the fix in the registration text; every clause of the
gate tied to a named field of a committed output file; the figures recomputed
by independent code; both ends (trained models pass, untrained fail). Each is
marked done, not done, or not yet possible, with the reason.

## Command

From `experiments/rehearsal-successor-measure/src/`:

    ~/Code/minimum-viable-mind/.venv/bin/python \
      ../../06-mvm-0a-constructed-self-index/reviews/2026-10-06-page1-closure-check-scripts/check_counts.py

Its output is saved as `check_counts.out.txt` and `check_counts.json` beside
it, and the searches as `battery_search.out.txt`.
