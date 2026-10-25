# Check of the paper's new paragraph on the map (commit aea2bb7)

*Checked 2026-10-25 by a Claude Code session that did not write the paragraph. Read-only, at commit `aea2bb7` on branch `claude/paper-map-paragraph-2026-10-25`. Saved by the session that wrote the paragraph; the report below is the checker's, unedited, and what was done about each finding is at the end.*

**What was checked.** The paragraph "What the removal test means under the map", added to the Discussion of `drafts/paper-removal-test-nature-draft.md`, and the dated note added to the header. The paragraph implements John's ruling 3a of 2026-10-24 (`docs/rulings/2026-10-24-revised-theory-next-steps-ruling.md`). It was checked against the re-reading's findings, method and output (`experiments/01-self-indexing-removal-test/reread-under-the-map-findings-2026-10-24.md`, `...-method-2026-10-24.md`, `reread-under-the-map-2026-10-24.json`), section 2 of `docs/next-steps-2026-10-24.md`, and the rest of the paper.

## 1. Numbers and claims against their sources: passes, with two small fixes

Every figure matches the output file for the registered removal: the flexible tasks that never mention the model lost 0.250 (6 of 24); the routine tasks lost 0.125 (1 of 8); the gap is +0.125, with a 95% interval from −0.167 to +0.375; all six flexible failures fall in multi-step reasoning, and the other two flexible categories lost nothing. The four needs for a future test are faithful to the findings' list. The description of the revised account matches section 2 of the next-steps document.

**Finding 1.** *"Because there were only eight routine items, that interval is wider than the limit of 0.5 the method set for a readable gap."* The method's rule is about the interval's span, here 0.54. **Fix:** "that interval spans 0.54, more than the 0.5 the method set as the widest a readable gap may have."

**Finding 2.** *"...with the method committed before the analysis ran..."* The findings file's dated note (review points RT-305 and RT-306) records that the method and output were committed 51 seconds apart, so commit order alone does not prove the method came first; what the record shows is that the method's commit (8530a8d) holds no output and the script groups items only as the method fixes. **Fix:** "with the grouping fixed in a method written down before the analysis, whose commit holds no output".

## 2. Claims nothing the re-reading does not support: fix needed (one sentence)

The paragraph rightly leaves out the cross-check's opposite tilt and the comparison of the two groups of tasks about turns, which the findings' dated note says are description only.

**Finding 3.** *"As description only, all six flexible failures were multi-step reasoning items, so the damage sat in one kind of task rather than across flexible response. The removal test is therefore silent on the split."* "Therefore" straight after the description makes the verdict read as if it followed from the description; the only conclusion the method allows comes from the width rule. **Fix:** put the verdict right after the width sentence and drop "therefore".

**Finding 4.** *"...and the items it treated as flexible were familiar task shapes..."* The July test never sorted its items into flexible and routine; the re-reading did, after the fact. **Fix:** "the items the re-reading counted as flexible".

## 3. No registered number, verdict or label changes, and the paragraph fits the paper: passes

Nothing contradicts Table 1 or the verdict sections. It fits "six of the seven flipped self-irrelevant items" and the 0.219 drop (7 of 32; the seventh failure is the one routine item); saying so would be optional. The method said nothing in the paper would change "beyond a sentence pointing to it"; John's ruling 3a calls for a paragraph, so the ruling governs.

## 4. Plain language and British spelling: passes

Connecting words are kept and no new shorthand is coined. The new text is in British spelling. Older parts of the draft still have American spellings ("centralized", "localization"), outside this commit; the British-spelling pass on the whole draft still has to catch them.

## 5. Header note: passes, on one condition

Accurate about placement, ruling, date, and that the Voice Calibration Protocol and Cold Reader pass are still owed. It cites this report, which did not exist at `aea2bb7`; it becomes true once the report is saved here, and if findings 1 to 4 are applied first, the note should say so.

## Note on the cited path for the revised theory (no change made)

`editorial/2026-10-23-assembled-time-revised-theory.md` in the sentient-horizons repository is correct: pull request 119 is merged and the file is on `origin/master`. The next-steps document's "on its pull request 119" is now out of date.

## Overall verdict

**Fix needed, minor.** The figures are right, and the paragraph keeps to the one conclusion the re-reading allows: the comparison cannot be read. All four fixes are wording changes; finding 3 matters most.

---

## What was done (2026-10-25, by the session that wrote the paragraph)

- Findings 1 to 4: applied as suggested. Finding 3's fix also takes the optional sentence from section 3: "the seventh failure on these tasks was a routine item".
- Section 5: the header note now cites this report and says the four fixes were applied after the check, changing no number.
- The American spellings in older parts of the draft and the out-of-date "on its pull request 119" in `docs/next-steps-2026-10-24.md` are left for the paper's readiness steps; not changed here.
