# Closure check of the two fatal findings: the split removal test design, version 0.2

*Filed 2026-10-24 by the design's author, verbatim as the reviewer returned it. The reviewer is the same isolated session that made the Gate C inside pass (`2026-10-24-split-removal-test-design-gate-c-tier1-claude-code.md`), run at commit 9ef0918. Under the closure rule the check is the reviewer's to make, not the author's. The only change in filing is that the escaped "&gt;" in the returned text is restored to ">". New findings continue the numbering as RT-322 to RT-327.*

---

**What I opened.**
- **Read:** version 0.2 of the target, from section 2 to the end, including the change log.
- **Searched for this check:** `removal-test-findings.md`, `red_team_ledger.md`, `thresholds.md` and `prelock-findings.md`, in experiment 01's folder.
- **Not re-opened:** the theory documents.
- **Run:** one simulation script in a scratch folder, shown below.

## The two fatal findings

| Finding | Verdict |
|---|---|
| RT-307 (the second removal method had no record of working) | **CLOSED WITH CONDITIONS** |
| RT-317 (the outcomes did not cover every case, and two overlapped) | **CLOSED** |

**RT-307 (ARGUED, lookup).** Swapping out the dictionary-feature method removes the method the record showed did not converge.
- **What the record supports.** Rows 19 and 20 of `removal-test-findings.md` do show both replacement methods inside the bound for staying in the normal range:
  - mean-ablation at +0.0867 against 0.0893, a margin of +0.0026 nats that the record itself calls marginal;
  - projection at +0.0856.
- **What the record does not support.** "A record of working" is true only of that normal-range bound and of moving behaviour. I found no committed record of either method making the own/user signal unreadable after the removal.
- **Why the new removal check may fail.** Version 0.2 requires accuracy of at most 0.55 at every later layer, from both a linear and a nonlinear probe. That has never been measured. The record points against it passing: on the 8-billion-parameter model the signal decodes perfectly by layer 3, after one pass over the role headers, which stay in the input. So the later layers can probably rebuild the signal from the headers.
- **Is the fallback enough?** Returning to John is a sound stop. It is enough only if both of the following hold:
  1. The text should say "a record of staying in the normal range" instead of "a record of working".
  2. The 0.55 limit and the half-of-baseline limit should not be loosened after the rehearsal without a dated ruling from John that is logged as a change made after seeing results.

**RT-317 (MEASURED).** I wrote a script that simulates item-level results and classifies them by section 5's rules. Run:

```
.venv/bin/python -I scratchpad/outcomes_v02.py
outcome counts: {'A': 969, 'B': 963, 'C': 716, 'D': 114, 'E': 238} | cases in no outcome after step 5: 0 by construction
cases meeting two or more step conditions (first-match decides): 819
A with P's interval not above zero (no excess loss on prompt-rule problems): 35
A with routines' excess loss >= delta and interval above zero (routines did not carry on): 308
template gap 0.40 vs split gap 0.20 -> renamed Template? False
true null (split = random = 0.05) -> {'D': '92%', 'methods disagree': '8%'}
small real loss (split 0.10, random 0.05) -> {'C': '3%', 'D': '4%', 'E': '36%', 'methods disagree': '57%'}
```

- **Every case lands in exactly one outcome.** This holds by construction: the steps are taken in order and the first that applies decides, with E catching everything left. In 3,000 simulated results none was left over and none was given two outcomes.
- **The order of the steps now does real work.** In 819 of the 3,000 results the conditions for two outcomes held at once, and the first one listed decided. See RT-322 below.
- **The escape named in RT-320 is closed.** Under a true null, 92% of runs land in D, which now counts against the prediction, and 8% land in "methods disagree". No null was filed as "not against the theory".
- **The Template and Not-specific checks cannot turn a null into "no reading".** As written they apply only to A and B. A small real loss still mostly ends in "no reading" (36% E, 57% methods disagree). That is an honest "could not decide", not an escape.

## The serious findings

On paper, RT-308 to RT-311, RT-314 to RT-316 and RT-318 to RT-321 are answered, with fixed numbers and named rules.
- RT-313 is answered only in part, because of RT-324 and RT-326 below.
- RT-314 is answered only in part, because of RT-327 below.

## New problems in version 0.2

**RT-322 (serious, MEASURED).** Outcome A ("the prediction held") requires only that the gap G be at least δ. It does not require routines to carry on.
- In 308 of the 3,000 simulated results, routines lost at least δ beyond the random comparison, with an interval above zero, and the result was still filed as A.
- The theory predicts that routines carry on, so these cases are general losses tilted one way.
- **Fix:** A should also require that R's upper end is below δ. Otherwise A should fall through to C.

**RT-323 (worth-noting, MEASURED).** In 35 results, outcome A held even though the prompt-rule problems lost nothing beyond the random comparison: P's interval was not above zero. The gap came from routines doing better than under random. **Fix:** A should also require P's interval to lie above zero.

**RT-324 (serious, MEASURED).** The Template rename fires only if the template-only gap is "within δ of G".
- A template-only gap of 0.40 against a split gap of 0.20 is not renamed. So the stronger the template effect, the more easily A survives it.
- **Fix:** rename whenever the template-only gap is at least G − δ. The Not-specific check has the same wording and needs the same fix.

**RT-325 (serious, ARGUED).** G is defined as the split removal's loss minus the matched random comparison's. The template-only conditions remove nothing inside the model, so they have no random comparison, and their "gap" is undefined. The text must say how it is computed. The obvious choice is the loss against baseline, which is on a different scale from G.

**RT-326 (serious, ARGUED, lookup).** The design locates its target "as experiment 01 located its structure".
- In July, that structure tripped its own registered loss condition for a chat-format router: "RT-05 router control: the loss condition FIRES" (`removal-test-findings.md`). The turn-format tasks lost 0.133 against 0.100 on the tasks about the model.
- So the reused structure has a committed record of behaving like bookkeeping for the chat format. Version 0.2 does not mention this.
- The template-only conditions test the input, not the located structure.

**RT-327 (serious, ARGUED, lookup).** The normal-range bound is 0.09, and comparison removals must be matched within 20% of the split removal's damage. Both are reasonable on their own, but together they may leave no room.
- In July the split removal sat at +0.0867, close to the bound, and the comparison removal of matched size reached +0.124.
- Comparisons matched to damage near 0.087 will cluster at the 0.09 bound, so "a needed comparison is lost" may be the usual way the run ends: not testable.
- The 0.0893 figure was also calibrated on a different setup: `thresholds.md` re-registered it as a cut-off taken from the spread of matched-strength comparison removals. Carrying it over as a fixed number is not justified.
- **Fix:** the rehearsal should report how much room is left under the bound, and the bound should be re-derived on the bench model.
