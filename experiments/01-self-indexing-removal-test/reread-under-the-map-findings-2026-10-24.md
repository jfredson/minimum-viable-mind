# Re-reading the July removal test under the revised theory's map: the findings

*Written 2026-10-24 (Saturday, Pacific), after the output. This is an unregistered re-reading done after the theory changed. The method (`reread-under-the-map-method-2026-10-24.md`) was committed first, as commit 8530a8d. The script is `src/reread_under_map.py`, and the output is `reread-under-the-map-2026-10-24.json`. It cost $0 and ran no model. The July test's registered verdict and its relabel of 2026-10-07 both stand unchanged.*

## The answer in one paragraph

By the rule stated in advance, **the comparison cannot be read**. The question was whether the removal hit flexible, multi-step tasks harder than routine one-step tasks on problems that never mention the model.

- Under the registered removal, the flexible group lost 0.25 and the routine group 0.125.
- The difference of +0.125 has an interval from −0.167 to +0.375. That interval spans 0.54, and the method said in advance that a span over 0.5 cannot be read.
- Beyond that rule, nothing in the July data looks like the selective loss the revised theory predicts:
  - every one of the flexible group's six failures falls in a single category;
  - the registered cross-check removal shows the opposite tilt;
  - on tasks that use the model's own earlier words, multi-step items lost no more than simple turn lookups.

The July test neither supports nor counts against the split. Its value is in what it says the split removal test needs.

## The figures

Every one of the 92 items was right at baseline, so each figure is the fraction answered wrongly after the removal. The intervals are 95%, from resampling items.

| Removal | G1 flexible, not about turns (24) | G2 routine, not about turns (8) | G3 flexible, about turns (30) | G4 routine, about turns (30) | Gap G1 − G2 |
|---|---|---|---|---|---|
| Registered removal of the self-tracking structure | 6 (0.250; 0.083 to 0.417) | 1 (0.125; 0 to 0.375) | 3 (0.100; 0 to 0.233) | 4 (0.133; 0.033 to 0.267) | +0.125 (−0.167 to +0.375) |
| Registered cross-check (same structure, one direction) | 2 (0.083; 0 to 0.208) | 2 (0.250; 0 to 0.625) | 2 (0.067; 0 to 0.167) | 4 (0.133; 0.033 to 0.267) | −0.167 (−0.500 to +0.125) |
| Removal of the narrative self-description | 2 (0.083; 0 to 0.208) | 0 (0.000) | 1 (0.033; 0 to 0.100) | 2 (0.067; 0 to 0.167) | +0.083 (0.000 to +0.208) |
| Control removal of an unrelated structure at matched strength | 1 (0.042; 0 to 0.125) | 1 (0.125; 0 to 0.375) | 0 (0.000) | 3 (0.100; 0 to 0.233) | −0.083 (−0.375 to +0.125) |

Group G1 joins three categories: multi-step reasoning, coreference and finding a fact in a passage. All six of its failures under the registered removal are multi-step reasoning items, and the other two categories lost nothing (`reread-under-the-map-2026-10-24.json`, per category). So the July concentration noted in the paper draft is a concentration in one task type, not across flexible tasks as a group.

## What it means, read against the rule stated in advance

1. **The selectivity gap cannot be read.** With 8 routine items not about turns, the interval is wider than the method allowed (0.54 against 0.5). The theory's prediction concerns that gap, so the July test is silent on it.
2. **Even if the rule had allowed a reading, three things argue against a selective-loss pattern:**
   - The flexible damage sits in one category, multi-step reasoning, and not in the two other flexible categories.
   - The registered cross-check removal, which removes the same structure a different way, tilts the other way (−0.167).
   - On tasks that need the model's own earlier words, the multi-step items (G3, 0.100) lost no more than the one-step turn lookups (G4, 0.133).
3. **The essay's sentence stands, with a qualification the record can now give.** The essay says no one has run the experiment of removing the signal that marks which words are the model's own and comparing tasks about the model with tasks that are not. In July this project removed a structure specific to the model's own turn and compared exactly those two kinds of task. It did not compare routine with new problems, which is the comparison the revised theory's prediction turns on, and its items could not support that comparison. So the July test is a near relative of the split test, not the split test. This is consistent with John's ruling that the essay stays as it is for now.

## What the split removal test needs, from this re-reading

- **Many more routine items not about turns.** With about 40 items in each of the routine and flexible groups not about turns, a 0.2 difference would have an interval of roughly ±0.18, which is readable. Eight was never enough.
- **Problems that are actually new to the model,** not familiar task shapes with fresh content. The July items are all short and familiar, so "flexible" could mean only "needs more steps". That is a weaker proxy than the theory's "something new".
- **Several flexible categories, read separately.** A loss concentrated in one task type, as here, should not count as a loss across flexible response.
- **A removal target that the cross-check agrees with.** The registered removal and its cross-check produced different patterns. The split test should require two ways of removing the same thing to agree before any pattern is read.
- **Routine tasks that do not depend on who said what.** Turn lookups read the removed signal directly, so damage to them is expected under any reading and cannot stand in for "routine".

These go into the design of the split removal test (`docs/split-removal-test-design-2026-10-24.md`).

---

*Dated note, 2026-10-24, later the same day, after the Gate C inside pass (`docs/reviews/2026-10-24-split-removal-test-design-gate-c-tier1-claude-code.md`, RT-305 and RT-306). The reviewer re-ran the script and got output identical to the byte, and confirmed the "cannot be read" call at every seed from 0 to 19. It raised two points; both are fair, and the text above is not edited.*
- *The method said that when the width rule fires, the re-reading "draws nothing from the gap". The summary paragraph and point 2 above still lean on the cross-check's gap of −0.167. Read those sentences as description only. The one conclusion this re-reading supports is the one its rule allows: the comparison cannot be read.*
- *The method and the output were committed 51 seconds apart, so commit order alone does not prove the method came first. What the record can show is this. The method's commit (8530a8d) contains no output file. The script reads the scores file only through the grouping that the method fixes. The method also discloses the one outcome already known when it was written: six of seven failures fell in multi-step reasoning.*
