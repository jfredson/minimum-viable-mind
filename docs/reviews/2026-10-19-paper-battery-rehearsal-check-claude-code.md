**Verdict: PASS WITH CONDITIONS.** Every figure in the new text matches its source. Both readings are what the method's rules call, no entry-1 difference is read, and nothing else in the paper moved. Three sentences need changing:
1. **Line 771: "After experiment C stopped, the project's measurement target moved to a two-sided question" has the order wrong.** The target moved on 2026-10-07 (decision 1 of `docs/rulings/2026-10-07-two-sided-question-rulings.md`), and experiment C stopped on 2026-10-12. The paper itself says "on 2026-10-07 the measurement target moved" at line 887. Write "On 2026-10-07 the project's measurement target moved to a two-sided question …".
2. **Line 800: "Repairing this is a registered edit to the entry, still to be made, with the bar unchanged."**
   - "With the bar unchanged" has no source anyone can open. John's ruling of 2026-10-19 on the repair exists only as a worklog title: the "agreed on all. Do" entry (`20442125`) has no body, and there is no ruling file.
   - "Registered edit" follows straight after "The battery is a draft and is not registered", so a reader takes it as calling something registered.
   - Write "The method says the repair goes through an edit to the entry committed before any re-run; it is still to be made." Add the bar only once a committed record of John's ruling says it, and cite that record.
3. **Line 808: "The null reading needs a difference of at most 0.10" reads, taken literally, as satisfied by −0.103.** The method's rule is "own minus other inside plus or minus 0.10, with its interval inside plus or minus 0.20". Write "a difference of at most 0.10 either way", and the sentence then stands.

# Check of pull request 206: the paper reports the battery rehearsal's two entries (2026-10-19)

*Filed 2026-10-19 (Pacific). Written under the workspace plain-language rule.*

## Who checked, and what was opened

This check was done by the Claude Code session that checked the paper's earlier changes (pull requests 175, 190 and 193). It wrote none of the paper, none of the new section, and no part of the rehearsal, its method, its run or its check.

It worked in its own worktree (`.claude/worktrees/check-206`, branch `check-paper-battery-rehearsal`), cut from `origin/paper-battery-rehearsal-2026-10-19` at `92ed1b5`. It compared against the main line at `0fd8963`, the branch's parent. Nothing under check was edited, no model was called, and nothing was spent.

**Opened:**
- the pull request body;
- the paper's diff;
- the run record `docs/filtered-battery-2026-10-07/rehearsal-run-record-2026-10-19.md`, in full;
- its check `docs/reviews/2026-10-19-battery-rehearsal-run-check-claude-code.md`, at sections 1, 3 and the conditions;
- the two analysis copies `rehearsal-analysis-entry1.json` and `rehearsal-analysis-entry2.json`;
- the method `rehearsal-method-entries-1-2.md`, at sections 5.4 and 6 and the pass and fail rules;
- `docs/2026-10-18-arm-m-separable-zero-findings.md`, its first section;
- the header of `docs/filtered-battery-proposal-2026-10-07.md`;
- the spec's section heading;
- the two spending-record rows;
- the project's worklog entries for 2026-10-19.

**Not opened:** the transcripts under `artifacts/`.

The script is `docs/reviews/2026-10-19-paper-battery-rehearsal-check-scripts/check_206.py`, and its full output is beside it. Re-run it from the worktree root with `python3 -I`. Labels: MEASURED (a command was run and its output is reported) or ARGUED (a judgment from reading).

## 1. Every figure against its source. MEASURED. Passes except condition 2.

The script finds 34 figures and claims in the added lines. Each is matched against the file the brief names, as a fixed string with line wraps collapsed. Each one prints whether it is in the text, then whether it is in the source:

```
   in text     in source     arm M: trunk signal / answer not used: 2026-10-18-arm-m-separable-zero-findings.md
   in text     in source     calls (2,632) / dates of the run: rehearsal-run-record-2026-10-19.md
   in text     in source     far-end reading (0.271 of the 59): 2026-10-19-battery-rehearsal-run-check-claude-code.md   ["0.271 (16 of 59"]
   in text     in source     rule quoted: rehearsal-method-entries-1-2.md   ["else the instrument is not working on the real far end and nothing is read"]
   in text     in source     D's own gate 0 in 10 / given in, in visible turns / one-sentence summary / scoring right: the run check, section 3
   in text     NOT IN SOURCE repair: bar unchanged: 2026-10-19-battery-rehearsal-run-check-claude-code.md
   in text     in source     endorsement 1.000 / judge 60 twice 1.000 / primary −0.103, −0.184 to −0.023 / 0.103 is 9 of 87: run record
   in text     in source     null band / other above own 0.20 / "fact about the policy … no named reading": the method
   in text     in source     spend $20.89 to $40.49 / Anthropic $13.06 / Gemini $7.83 to $27.43: spending-record.md
   json: entry1 r_reference 0.271 (16/59 = 0.271); gates {… 'ii_reference_far_end': False, …}
   json: entry2 primary -0.103 [-0.184, -0.023] reading 'no verdict'; n 87; 9/87 = 0.1034; endorsement 1.0
```

Every other line of the output reads "in text  in source" (see `check_206.out.txt`). Some notes on how the matches were read:

- **The quoted rule** drops the method's leading "else". The quotation is a true substring of the method's text.
- **"At the first turn"** is the run record's "turn 0".
- **"The revised labels"** is the run record's "the new-rubric labels".

ARGUED: each is the same fact in plain words.

- **The specification's section.** It was committed on its branch on 2026-10-17 (`1a9752e`) and merged on 2026-10-18 at 17:35 Pacific (pull request 173). "Written in on 2026-10-18" is right by the Pacific date.
- **"Checked before any call."** The method's last check merged at 17:39 Pacific on 2026-10-18 (pull request 187), and the run record's first start was about 18:55. So the method was checked before the first call. MEASURED with `gh pr view`.

The one miss is "with the bar unchanged", which is condition 2. No committed file says it. The only record of the 2026-10-19 repair ruling is a worklog entry, "agreed on all. Do" (`20442125`), whose body is empty when read through the API. One more thing about the worklog: the later entry of the same day (`5d0299e4`) says "entry 1's repair waits on John's choice". So the record does not agree on whether the repair has been ruled. A ruling file would settle it.

## 2. No number is read beyond what the rules call. MEASURED. Passes, with condition 3.

```
   entry 2: null False (|d| 0.103 > 0.10), predicted False, other-above-own False (other-own 0.103 < 0.20) -> no verdict True
   entry 1: far-end gate holds False -> nothing read; new text reads any entry-1 difference: False
   'difference of at most 0.10' would admit −0.103 if read literally: True
```

**Entry 1.** The far-end gate failed, and the new text names none of entry 1's rates or differences: 0.944, 0.991, +0.009, −0.047 and +0.047 are all absent. It says "none of entry 1's differences is read".

**Entry 2.** −0.103 is given as a number with its interval, and "That reaches no reading". "Other above own" is described as needing at least 0.20, and as reported "as a fact about the policy with no named reading", which is the method's own phrase. The one-cell margin, and the two things that would have moved it, are given as the run record gives them, as margin and not as a reading.

The one fault is the wording of the null band, condition 3. The method's band runs both ways ("inside plus or minus 0.10"). "At most 0.10" with no direction is literally true of −0.103, which turns the sentence's logic upside down for a careful reader.

## 3. Nothing unregistered is called registered. MEASURED, with an ARGUED judgment. Condition 2.

```
3. 'registered' in the new text:
     The battery is a draft and is not registered (`docs/filtered-battery-proposal-2026-10-07.md`, version 4).
     Repairing this is a registered edit to the entry, still to be made, with the bar unchanged.
```

The first sentence is right. The proposal's header says "This is a draft of Gate A registration text, not registration text: nothing here binds until it has been through Gate A".

The second takes the method's phrase "through a registered edit" (method, section 5.4 and the fail rule of entry 2). In the method, the phrase names the procedure for changing the entry. In the paper it lands one paragraph after "is not registered", and the reader has no way to tell that "registered edit" does not mean an edit to registered text. Hence condition 2.

## 4. Nothing else in the paper moved. MEASURED. Passes.

The word diff of the whole paper (`check_206.out.txt`, part 4) holds exactly:
- the arm M sentence;
- the new section;
- the Methods date "2026-10-18" becoming "2026-10-18 and 2026-10-19";
- the Methods cost sentence.

Nothing else is added and nothing else is removed. The pull request touches only the paper.

## 5. Spelling and quotations. MEASURED. Passes.

The scan finds no American spelling in the added lines. The quotations in the new text were each found in their sources (part 1): the method's far-end rule and its "fact about the policy" phrase, and the arm M findings' "this turn is yours". The quotations have the sources' spelling.

## Notes, not conditions

- **Who pays.** The Methods cost names the two providers, which the workspace's rule on tools allows in a method section, where it bears on trust. It also says "under an approval of up to $50". The run record and the spending record show the Anthropic share was paid from plan credits and the Gemini share out of pocket, both inside that go. The paper could say so in a clause if who paid matters to the reader.
- **The worklog.** Whether entry 1's repair has been ruled is unclear in the worklog itself, as noted under item 1. That belongs to the master session, not to this pull request.

---

## Check of pull request 214, 2026-10-19: why entry 1 cannot be read

**Verdict: PASS WITH CONDITIONS.** The figures match their sources, the observation is labelled as not a reading, only the one sentence changed, and the spelling is British. Two changes:
1. **Line 800: "One repair was tried, as a diagnosis registered before it ran" calls the repair registered.** The same section says "The battery is a draft and is not registered". "Registered" here is method section 14's word for itself ("A dated, registered edit"), the same wording that condition 2 of the check of pull request 206 asked to be taken out. Write "One repair was tried, as a diagnosis whose outcome the method stated before it ran:".
2. **The observation's citation points at a file that declines to say it.** The sentence "a summary given in one message does not reproduce how the reference behaves in a live, turn-by-turn conversation" comes from John's ruling, as do "entry 1 stops here" and "a redesign is possible later only as a new pre-registered design". They are in the addendum of `docs/rulings/2026-10-19-battery-rehearsal-results-and-entry1-repair-ruling.md`, "Addendum, later on 2026-10-19: entry 1 stops here". The only file the new text cites is the step-1 result, which says of the summary format that it "is a question for John and the master, not answered here". Cite the ruling's addendum after "pre-registered design" and after the observation.

The check was done by the same session as the sections above, in its own worktree (`.claude/worktrees/check-214`, branch `check-paper-entry1-note`), cut from `origin/paper-entry1-note-2026-10-19` at `02ee4d2`. It compared against the main line at `aedb62a`, the branch's parent. Nothing under check was edited, no model was called, and nothing was spent.

What it opened:
- the step-1 result and its check;
- the ruling with its addendum;
- the analysis JSON;
- method section 14's header;
- the first run's check, for bank A's 10 of 30.

The script is `docs/reviews/2026-10-19-paper-battery-rehearsal-check-scripts/check_214.py`, with its output beside it.

### 1. Figures. MEASURED. Passes.

```
   in text     in source     gate figure: farend-repair-step1-result-2026-10-19.md   ["0.712 of the 59 reference items (42 of 59), against the unchanged bar of at most 0.20"]
   in text     in source     bank A, replies quoted: …farend-repair-step1-result-check-claude-code.md   ["bank A 20 of 30"]
   in text     in source     bank A, replies left out (first run): …battery-rehearsal-run-check-claude-code.md   ["10 of the 30 number items"]
   in text     in source     bank A, whole conversation: farend-repair-step1-result-2026-10-19.md   ["(1 of 30)"]
   in text     in source     what was shown / stops here, no verdict / redesign later / the observation: result file and ruling addendum
   in text     NOT IN SOURCE the observation, in the cited result file: farend-repair-step1-result-2026-10-19.md
   json: reassertion_step1 0.712 (42/59 = 0.712); n 59; bar 0.2; gate_pass False
   result file on the summary format: True   ["… is a question for John and the master, not answered here"]
   files the new text cites: ['docs/filtered-battery-2026-10-07/farend-repair-step1-result-2026-10-19.md']
```

All six figures you listed are found where the brief says: 0.712, 0.20, 59, and 20, 10 and 1 of 30. In the first run's check, bank A is called the "number items". The one NOT IN SOURCE line is condition 2: the observation is John's ruling, not the result file's.

### 2. The observation is labelled, and nothing is read beyond the rules. MEASURED, with an ARGUED judgment. Passes except condition 1.

```
   'as an observation, not a reading' in text: True
     One repair was tried, as a diagnosis registered before it ran:
     a redesign is possible later only as a new pre-registered design.
   battery said to be not registered earlier in the section: True
```

**The label.** The observation is labelled in the words the ruling's addendum asks for.

**Nothing read beyond the rules.** Entry 1 stays "without a verdict", and no rate of entry 1's first run is read. The three bank A counts are given only inside the labelled observation. The gate figure, 0.712 against 0.20, is the one figure section 14's rule reads: the gate failed, so the work stops.

**"Pre-registered design".** This refers to a design that does not yet exist. It does not call anything registered, so it is fine. The ruling adds "only on his word", which the paper leaves out; that is acceptable in a paper.

### 3. Only the one sentence changed. MEASURED. Passes.

The word diff of the whole paper (`check_214.out.txt`, part 3) replaces "The method says the repair goes through an edit to the entry committed before any re-run; it is still to be made." with the new text and touches nothing else:

```
   files changed:  1 file changed, 12 insertions(+), 2 deletions(-)
```

### 4. British spelling. MEASURED. Passes.

```
4. American spellings in the added lines:
     none
```
