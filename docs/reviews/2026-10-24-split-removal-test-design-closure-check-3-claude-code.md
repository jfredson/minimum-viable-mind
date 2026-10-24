# Third closure check: the split removal test design, version 0.5

*Filed 2026-10-24 by the design's author, verbatim as the reviewer returned it. The reviewer is the same isolated session as before, working at commit fec24bc. New findings continue the numbering as RT-331 to RT-334.*

---

**What I opened:** the changes from version 0.4 to version 0.5. **What I ran:** one simulation, shown below.

| Finding | Verdict |
|---|---|
| RT-328 (T3, the condition with the role headers removed, could not run as defined) | **CLOSED WITH CONDITIONS** (RT-331, RT-332) |
| RT-329 (what "size" meant for the normal-range bound) | CLOSED |
| RT-325's condition (say the renames use point estimates) | CLOSED |
| RT-330 (how "methods disagree" is reported) | CLOSED |

**RT-328, the measured check (MEASURED).** T3 now keeps the model's own sampled words and reads the directions already located, so it can run. It no longer decides whether a result can be read. I added T3 to the version 0.4 simulation as a random draw that reports "depends on the headers" in a set share of runs:

```
.venv/bin/python -I scratchpad/outcomes_v05.py scratchpad/outcomes_v04.py
T3 header-driven rate 0.0: C/D/E moved {'C': 0, 'D': 0, 'E': 0}; A or B renamed 0/591; ...
T3 header-driven rate 0.3: C/D/E moved {'C': 0, 'D': 0, 'E': 0}; A or B renamed 165/588; ...
T3 header-driven rate 1.0: C/D/E moved {'C': 0, 'D': 0, 'E': 0}; A or B renamed 604/604; ...
```

- T3 never moves an outcome C, D or E. It can only rename A or B.
- So the escape named in RT-320, a null filed as "not against the theory", stays closed.

**The probe threshold is not yet defined well enough to run.** That is RT-331.

## New problems

**RT-331 (serious, ARGUED).** The T3 probe is missing what it needs to run. The text does not say:
- **which layers it reads.** If the best of many layers counts, the 0.65 limit is too easy to reach.
- **which token positions it reads.**
- **how its data is split.** "Trained on held-out T3 inputs" names no separate set to score it on.
- **what chance looks like.** Experiment 01 judged every probe against shuffled labels; T3 names no such baseline.

**Fix:** use the layers where the removal is applied and require the limit at each of them. Name the positions, keep separate training and scoring sets, and report accuracy as a margin over the shuffled-label baseline.

**RT-332 (serious, ARGUED). Style and order are not handled, and should be named.** Without headers, and processed afresh inside a user turn, the model has no information about who wrote a paragraph except two things:
- **style:** its sampled paragraphs read like an assistant;
- **order:** the paragraphs alternate.

So T3 reaching 0.65 shows that the located directions carry style or order. It does not show that the model uses its own authorship. A false "survives" keeps outcome A from being renamed Template. That is the incautious direction, the opposite of the design's stated lean toward renaming. **Fix:** add two controls.
1. Both sides sampled from the model (the user side from a separate run). If accuracy stays at 0.65 or more, the probe is reading order.
2. Model and user paragraphs swapped into each other's positions. If accuracy follows the text rather than the position, the probe is reading style.

If either fires, T3 counts as "depends on the headers".

**RT-333 (worth-noting, ARGUED).** If T3 lands between the two limits (0.55 to 0.65, "unresolved"), outcome A is not renamed. The text should state whether an unresolved T3 lets A stand, or whether such an A is reported with T3's result attached.

**RT-334 (worth-noting, MEASURED).** The line opening the T3 paragraph starts with `****A third condition`, four asterisks where two were meant.
