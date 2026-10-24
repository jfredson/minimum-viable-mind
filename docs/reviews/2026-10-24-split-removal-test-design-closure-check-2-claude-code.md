# Second closure check: the split removal test design, version 0.4

*Filed 2026-10-24 by the design's author, verbatim as the reviewer returned it. The reviewer is the same isolated session as the Gate C inside pass and the first closure check, working at commit 5a59650. The only change in filing is that the escaped "&gt;" in the returned text is restored to ">". New findings continue the numbering as RT-328 to RT-330.*

---

**What I opened.**
- **Read:** the changes from version 0.2 to version 0.4 of the target, and section 5's first stage, which decides whether a result can be read at all.
- **Searched:** line 30 of experiment 01's `pre-registration.md`, for the July third-party speaker condition.
- **Run:** one simulation, shown below.

## Verdicts

| Finding | Verdict |
|---|---|
| RT-307, condition 1 (say "staying in the normal range", not "working") | CLOSED |
| RT-307, condition 2 (no loosening the limits after seeing results) | CLOSED |
| RT-322 (outcome A must require routines to carry on) | CLOSED (MEASURED) |
| RT-323 (outcome A must require a loss on prompt-rule problems) | CLOSED (MEASURED) |
| RT-324 (a stronger template effect must rename more easily) | CLOSED (MEASURED) |
| RT-325 (the template conditions' gap was undefined) | CLOSED WITH CONDITIONS |
| RT-326 (the reused July structure behaved like chat-format bookkeeping) | **NOT CLOSED**: see RT-328 |
| RT-327 (the normal-range bound may leave no room) | CLOSED WITH CONDITIONS: see RT-329 |

**The measured check (MEASURED).** I re-ran the outcome simulation with version 0.4's rules for outcomes A and B and its new rename rules. The T1 and T2 template conditions were simulated with no real effect, and the other-distinction removal was simulated as acting like a random one. Command and output:

```
.venv/bin/python -I scratchpad/outcomes_v04.py
outcomes: {'A': 441, 'B': 434, 'C': 1451, 'D': 140, 'E': 500, 'Not specific': 15, 'Template': 19} | results meeting 2+ step conditions: 27
'routines lost too' results still in A: 0
template gap 0.40 vs G 0.20 renamed? True
true null, n=120 -> D 92%, E 1%, methods disagree 7%
small real loss (both cells +0.05), n=120 -> C 6%, D 4%, E 34%, methods disagree 56%
true selective G=0.20 (P .25, R .05), n=120 -> A 85%, methods disagree 15%
true selective G=0.12 (P .17, R .05), n=120 -> A 29%, E 10%, Not specific 1%, Template 1%, methods disagree 60%
```

- **Exactly one outcome.** Every simulated result still lands in exactly one outcome. The steps are taken in order and the first that applies decides; now only 27 of 3,000 results meet two conditions, against 819 before.
- **Routines lost too.** None of these cases lands in A any more (308 did under version 0.2).
- **Template rename.** A template gap of 0.40 against a split gap of 0.20 is now renamed.
- **True null.** 92% of runs land in D, which now counts against the prediction.
- **Small real loss.** Mostly "no reading": 34% E and 56% methods disagree.
- **True gap of 0.20 at 120 items per cell.** 85% of runs land in A, consistent with section 4's 80% target.

**RT-325, the condition.** The text should state that the renames compare point estimates only, with no interval.

## New problems

**RT-328 (fatal, ARGUED).** T3 cannot run as defined, and it reopens the escape named in RT-320.
- **What T2-style inputs are.** They are "a transcript inside one user turn". That is the third-party speaker condition experiment 01 already used: "a transcript between two named third parties embedded in a single user turn, so … the model participates in neither" (`pre-registration.md`, line 30).
- **Why the target cannot be found there.** On such inputs no word is the model's own, so the difference between own words and user words is absent by construction (failure mode 3, a cell that is empty by construction).
- **Read strictly.** "Cannot be located there at all" then fires on every model, and every model's result becomes "not testable: the target depends on the template".
- **Read loosely.** Whatever is located there is general tracking of who is speaking. That is the structure the design's own third-party control rules out, and in July it was nearly unrelated to the self-tracking structure (overlap of 0.148 on a 0-to-1 scale, against the July rule's threshold of 0.5).
- **What the text does not say.**
  - whether T3 reuses the directions already located or locates new ones;
  - what threshold counts as "cannot be located";
  - T3 is missing from section 5's list of the conditions under which a result cannot be read.
- **How it reopens the escape.** That readability check runs first. So T3 can turn a D, the outcome that counts against the theory, into "not testable".
- **Fix:** keep the model's own earlier words, sampled by the model itself, but remove the role headers some other way, for example by giving the conversation as plain text. Then apply the directions already located, with a stated probe threshold. List the result among the conditions in section 5 under which a result cannot be read, with a rule saying it cannot void a D or C unless the removal check also fails there.

**RT-329 (serious, ARGUED).** The re-derived normal-range bound uses "random removals of the split removal's size", and "size" is not defined.
- If size means the same damage, the bound is circular: removals matched to the split removal's damage set the limit the split removal is judged by.
- If size means the same number of directions with the same replacement rule, it is July's re-registered cut-off, which `thresholds.md` (Pass 5) defines as taken from the spread of matched-strength random removals. The text should say so.

**RT-330 (worth-noting, MEASURED, from the output above).** For a true gap just above δ (0.12), "methods disagree" is the most common result, at 60%. Summaries must report disagreement as "could not decide", never as the prediction failing.
