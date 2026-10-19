**Verdict: PASS WITH CONDITIONS.** The title, the router paragraph and the two Discussion changes match the wording John ruled on, word for word. The spelling pass changed spelling only and altered no quotation, code span, path or label. Nothing else in the draft moved. Two changes remain:
1. **Two American spellings are left in the paper's own prose.** They are "*favorably*" at line 205 and "HOT-favorable" at line 777. They should read "*favourably*" and "HOT-favourable".
2. **The Limitations sentence (lines 818 to 822) adds a clause that was not ruled, and its citation does not support that clause.** The clause is 'so its nulls say "not testable", never "absent"'. It is not in the ruling, which reads "the constructed line's locating instruments are unvalidated at 30 million parameters", nor in the dated note's proposal. The file it cites, `blind-arm-findings.md`, never says "not testable": that word count is 0. Its registered sub-bin is "instrument failure to locate". End the sentence at "(…; John's ruling of 2026-09-16)." If the clause is wanted, it needs John's word, because the Discussion is a place he reserved. In that case, give the registered term in full and cite where it is: "*not testable (localization)*, read as instrument failure, not absence (`amendment-a3.md`, "Closure of Amendment A3, 2026-09-25")".

# Pairing-rule check of pull request 190: John's four rulings of 2026-10-18 applied to the paper draft

*Filed 2026-10-18 (Pacific). Written under the workspace plain-language rule.*

## Who checked, and what was opened

This check was done by the Claude Code session that checked pull request 175: `docs/reviews/2026-10-17-paper-fold-check-claude-code.md` and its re-check. It wrote none of the paper and did not apply these rulings. The master session for the project applied them in commit `855ea36`.

The check ran in its own worktree, `.claude/worktrees/check-190`, on branch `check-paper-reserved-places`, cut from `origin/paper-reserved-places-2026-10-18` at `855ea36`. The comparison is against the main line at `e2b0825`, which is the branch's parent. Nothing under check was edited, no model was called, and nothing was spent.

**Opened:**
- the pull request body;
- the ruling file `docs/rulings/2026-10-18-paper-reserved-places-ruling.md`, in full;
- the diff of the paper against the main line, in full;
- the paper's dated note of 2026-10-17, whose proposals were the wording John was shown;
- `experiments/06-mvm-0a-constructed-self-index/blind-arm-findings.md`, where the Limitations sentence cites it;
- the closure block of `amendment-a3.md`.

**Not opened:** the rest of the paper beyond the lines the diff and the scans hit.

The scripts and their outputs are in `docs/reviews/2026-10-18-paper-reserved-places-check-scripts/`. `sh docs/reviews/2026-10-18-paper-reserved-places-check-scripts/run_all.sh` re-runs them. Every finding is labelled MEASURED (a command was run and its output is reported) or ARGUED (a judgment from reading).

## 1. The title is option (b), word for word. MEASURED. Passes.

`ruled_wording.py` compares the paper's first line with the ruling's option (b) and with the dated note's proposal. Line wraps and bold marks are collapsed on both sides; nothing else is normalised.

```
1. title == ruling option (b): True | == note's proposal: True
   title : Instruments that can lose: a registered removal test, a constructed self-index and a successor stopped by its own rule, in the measurement of self-indexed integration
   opt b : Instruments that can lose: a registered removal test, a constructed self-index and a successor stopped by its own rule, in the measurement of self-indexed integration
```

## 2. The router paragraph and the two Discussion changes are the proposed wording, word for word. MEASURED. Passes.

The applied text is taken from the body, after the dated notes, so that a proposal is never compared with its own copy. (The first run of the script made exactly that mistake; it is fixed in the committed version.) Where the two sides differ, the script prints the difference word by word.

```
2. router passage minus the kept bootstrap clause == note's proposal: True
   bootstrap clause present on branch: True | same clause on main: True
   word diff proposal -> applied: ['identical']
   old first sentence gone: True
3a. Discussion ¶1 == proposal (proposal's nested 'self' read as "self"): True
   word diff: ['identical']
3b. Discussion addition == proposal (after a joining comma): True
   applied: , and the control's own margin, re-read two months later, turned out to span zero; the programme reports both the verdict as registered and the reassessment, dated, and does not replace one with the other.
   word diff: ['identical']
```

The router paragraph keeps the bootstrap clause byte for byte from the main line: "(and the reason the coarser category-level bootstrap widens the d(T_si) interval to [0.000, 0.594]; Methods §Statistics)". It sits after "which neither account rules out" and before "These data do not separate", which is where the proposal's own "The bootstrap-widening clause and its Methods pointer stay" puts it.

Two allowances are made, and each is stated in the script's output:
- **Quotation marks.** The proposal wrote 'self' in single quotation marks because it sat inside a quotation. The paper has "self" in double marks, as the main line had.
- **A joining comma.** The addition to the third paragraph is joined to "before any data existed" with a comma, where the main line's sentence ended.

ARGUED: both are punctuation the change needs, not changes to the wording. The Discussion's first paragraph also drops the italics on *report-generating*, as the proposal did.

## 3. The Limitations sentence. MEASURED, with an ARGUED judgment. Condition 2.

```
3c. Limitations sentence: The constructed line's instruments for locating the ownership structure are unvalidated at 30 million parameters (`experiments/06-mvm-0a-constructed-self-index/blind-arm-findings.md`; John's ruling of 2026-09-16), so its nulls say "not testable", never "absent".
    note's proposal: saying that the constructed line's localization instruments are unvalidated at 30 million parameters (`experiments/06-mvm-0a-constructed-self-index/blind-arm-findings.md`, John's ruling of 2026-09-16)
    ruling item 3 option (b): the constructed line's locating instruments are unvalidated at 30 million parameters
    cited file blind-arm-findings.md contains 'the localization stack is unvalidated at 30': True
    cited file blind-arm-findings.md contains "John's ruling": True
    cited file blind-arm-findings.md contains '2026-09-16': True
    there: … So the correct scope is narrow: the localization stack is unvalidated at 30M. That is a real and reportable limitation of the A2 and A3 work …
    'not testable' in blind-arm-findings.md: 0 | 'instrument failure to locate': 2
```

Up to its citation, the sentence says what the ruling says, and the cited file contains it: "the localization stack is unvalidated at 30M", under John's annotations of 2026-09-16. "Instruments for locating the ownership structure" in place of the note's "localization instruments" is a plain-words rewording that keeps the ruled substance.

The trailing clause is the problem: 'so its nulls say "not testable", never "absent"'.
- **The cited file does not contain it.** MEASURED: 0 hits for "not testable".
- **The ruling did not ask for it.** It sits in the Discussion, a place John reserved.
- **The idea is in the record, but under a longer term.** The A3 closure gives "the registered term for the line is therefore *not testable (localization)*, and the registered reading of this null is instrument failure, not absence".

So the clause is supported somewhere in the record, but not where it points, and not in the shortened form it quotes. Hence condition 2.

## 4. The spelling pass changed spelling only. MEASURED. Passes, apart from condition 1.

`spelling_only.py` takes git's word diff of the paper, main line against branch, and pairs each removed run of words with its added run. It normalises both sides the same way, British endings back to American (-ise, -isation, -yse, centre, -our, licence, artefact, programme, modell-). A pair whose two sides then match is SPELLING; anything else prints as OTHER.

```
   59 spelling-only groups, 37 other groups
```

All 37 OTHER groups were read (`spelling_only.out.txt`, part a). Every one belongs to a ruled change:

| Ruled change | OTHER groups |
|---|---|
| the title | 3 |
| the new dated note of 2026-10-18 | 5 |
| the router paragraph | 16 |
| the Discussion's first paragraph | 4 |
| the Discussion's third paragraph | 4 |
| the Limitations sentence | 5 |
| **total** | **37** |

The two "licenses" changed to "licences" are both the noun ("outcome licences"). The verb ("licenses claims") is left as it is, which is right in British spelling.

**No quotation, italic span, code span, path or label was altered by the spelling pass.** Part (b) splits both files into paragraphs, 96 on each side, and compares each changed paragraph's double-quoted passages, italic spans and code spans. Only these differ:

```
   ¶5 italic: main []  branch ['*(Dated note, 2026-10-18: John ruled all three as proposed below, with']
   ¶5 code: main []  branch ['`docs/rulings/2026-10-18-paper-reserved-places-ruling.md`']
   ¶36 italic: main ['*self-irrelevant*']  branch []
   ¶67 italic: main ['*report-generating*']  branch []
   ¶70 quoted: main []  branch ['"not testable"']
   ¶70 code: main []  branch ['`experiments/06-mvm-0a-constructed-self-index/blind-arm-findings.md`']
```

Each of these is in a ruled change: the new dated note, the router paragraph, the Discussion's first paragraph, and the Limitations sentence. None comes from the spelling pass. In particular, these all keep their own spelling:
- the registered loss condition RT-05, quoted as committed (*"… H_center result on it is void — report the router reading, do not report a center."*);
- the registered term *not testable (localization)*;
- the labels `H_center` and C_self-index;
- the path `docs/rulings/2026-09-20-center-as-degree.md`;
- the quoted old title "No removable center";
- the cited reference title "Discovering language model behaviors".

**American spellings left on the branch** (part c). There are 14 hits. Each is tagged with where it sits:
- 12 are in places the ruling, or the pull request's stated choice, exempts. Those are the quotations and the code span above, plus lines 101 to 118, the dated note of 2026-10-17, which quotes the v0.2 paragraph verbatim and records what John was shown.
- Two are in the paper's own prose: "*favorably*" (line 205, the Introduction) and "HOT-favorable" (line 777, the Discussion's first paragraph). The pass missed the -our ending in "favour". That is condition 1.

## 5. Nothing else in the draft moved. MEASURED. Passes.

```
$ git diff --stat origin/main HEAD
 .../2026-10-18-paper-reserved-places-ruling.md     |  66 +++++++++
 drafts/paper-removal-test-nature-draft.md          | 164 +++++++++++----------
 2 files changed, 155 insertions(+), 75 deletions(-)
```

The pull request touches two files: the new ruling and the paper. Inside the paper, every changed word is either one of the 59 spelling-only pairs or one of the 37 groups attributed above. Nothing is left over. The dated note of 2026-10-17 is unchanged apart from the inserted note of 2026-10-18.

## The sentence the pull request flags: "the entire programme ran for under $20 of compute". ARGUED.

The sentence is at line 807, in the Discussion's third paragraph:

> We suggest this is the minimum standard assessment claims in this area should meet, and note that the entire programme ran for under $20 of compute on rented consumer GPUs: the barrier is discipline, not resources.

**Why it is now wrong.** In version 0.2, "the program" meant the removal test's own work. In version 0.3 the paper's new sections use "programme" for all three experiments. The paper's own Methods put that programme at "about $230.94 of a $450 ceiling" (line 1031). Even for the removal test alone, "under $20 of compute" is only the rented-GPU part: Methods (line 1029) gives "≈ $10–20 of rented GPU time plus low tens of dollars of judge-API calls".

**What it should read** (this session's proposal):

> … and note that this experiment ran for about $10 to $20 of rented consumer GPU time, plus low tens of dollars of judge calls, and the whole programme of three registered experiments for about $230.94 (Methods, "Compute and cost"): the barrier is discipline, not resources.

The sentence is in the Discussion, which John reserved. The pull request was right not to change it unasked. It is a factual correction, not a choice of wording, so it can go to John as a one-line yes or no.

**The same shift touches three more sentences** (`twenty_dollars.out.txt`). There, the v0.2 "program" became "programme" while still meaning the removal test:
- line 301, "the only S drop ever observed in the programme";
- line 357, "not reduced by any readable intervention in the entire programme";
- line 1107, the Fig. 4 caption, "across every intervention in the programme".

Read beside the new sections, each now reaches over all three experiments. Experiments 06 and C never measured judged self-report, so line 357 in particular claims more than was run. "In this experiment" fixes each one. This is a note, not a condition: the spelling change is correct, and the shift of meaning began in v0.3. Lines 301 and 357 are outside the reserved places. Line 1107 is in a figure caption.

## What this check did not do

- It did not re-read the paper for anything other than these four rulings and the spelling pass.
- It did not re-check figures. The first check of pull request 175 did that, and nothing numeric changed here. Every spelling-only pair is the same word on both sides, so no number in those lines moved. The only numbers the ruled changes add are the router paragraph's 0.219, [0.000, 0.594], +0.033 and −0.133 to +0.200, which are the main line's own figures from the same section; "30 million" in the Limitations sentence; and dates.
- It did not judge whether British spelling should also apply to the dated notes, which the pull request leaves as they were.

---

## Check of pull request 193, 2026-10-18: the cost sentence and the three "programme" sentences

**Verdict: PASS WITH CONDITIONS.** All five things asked hold:
- the cost sentence is this checker's proposal plus "of rented compute";
- the three "programme" changes sit exactly where they were named;
- nothing else in the paper moved;
- the ruling file quotes John as relayed;
- the Methods addition is true of the ledger, whose every row is a rented machine or a $0 local run.

But the figure both sentences carry is not the whole programme's, and that error began in this checker's own proposal in the check of pull request 190. The compute ledger opened at $0 on 2026-08-07. It says experiment 1's rented spend "predates this cap", so the $230.94 covers experiment 06 and experiment C only. The two changes:
1. **Methods, "Compute and cost" (line 1030).** "Whole programme to the stop of experiment C: about $230.94" should read: "Experiment 06 and experiment C, from 2026-08-07, when the ledger opened, to the stop of experiment C: about $230.94 of a $450 ceiling, every row in `…compute-ledger.md`. That figure is rented machine time only; experiment 1's rented time predates the ledger and is the figure given above." The sentence about calls to model providers by API follows unchanged. Methods is not a reserved place.
2. **Discussion (line 807).** "the whole programme of three registered experiments for about $230.94 of rented compute" should read "the two constructed-line experiments that followed for about $230.94 of rented compute". John approved the sentence as proposed, so this goes back to him as a correction of the proposal he said yes to. It is a fact about scope, not a new choice of wording.

Checked by the same session as the two sections above, in its own worktree (`.claude/worktrees/check-193`, branch `check-paper-cost-sentence`, cut from `origin/paper-cost-sentence-2026-10-18` at `67f55d7`), against the main line at `6c19b01`, the branch's parent. Nothing under check was edited, no model was called and nothing was spent. The script is `docs/reviews/2026-10-18-paper-reserved-places-check-scripts/check-193/check_193.py`, and its output is beside it.

### 1. The cost sentence. MEASURED. Passes.

The script takes the proposal text from this record's own section above, adds "of rented compute" after "$230.94", and looks for the result in the paper:

```
1. proposal (from the check of 190): and note that this experiment ran for about $10 to $20 of rented consumer GPU time, plus low tens of dollars of judge calls, and the whole programme of three registered experiments for about $230.94 (Methods, "Compute and cost"): the barrier is discipline, not resources.
   proposal + 'of rented compute' found in the paper: True
   old sentence gone ('entire programme ran for under $20'): True
```

### 2. The three "programme" changes sit where they were named. MEASURED. Passes.

```
2. changed main-line lines (start, count): [('301', '', '301'), ('357', '', '357'), ('806', '3', '806'), ('1031', '', '1032'), ('1106', '', '1110')]
   main line 301: the only S drop ever observed in the programme, and it was coherence-borne, not
   main line 357: was not reduced by any readable intervention in the entire programme — not by
```

The Fig. 4 caption's sentence is at line 1106 on this main line. It was named as line 1107 on the branch of pull request 190. Between the two, the cut Limitations clause (pull request 192's condition 2) moved it up one line. It is the same sentence, "across every intervention in the programme". The other two hunks are the cost sentence (806) and the Methods addition (1031).

### 4. Nothing else in the paper moved. MEASURED. Passes.

The word diff of the whole paper is every change there is:

```
    -the programme,          +this experiment,
    -the entire programme    +this experiment
    -the entire programme    +this experiment
    -under                   +about $10 to
    -compute on  -GPUs:      +GPU time, plus low tens of dollars of judge calls, and the whole programme of
                             +three registered experiments for about $230.94 of rented compute (Methods,
                             +"Compute and cost"):
                             +That figure is rented machine time only. Calls to model providers by API (judge calls, the
                             +outside reviews, and the measurement rehearsal of the filtered battery run on
                             +2026-10-18) are recorded in the project's worklog and are not in it.
    -the programme.          +this experiment.
```

Apart from the paper, the pull request changes only the ruling file.

### 3. The Methods addition against the ledger. MEASURED, with an ARGUED judgment. Conditions 1 and 2.

```
3. ledger rows: 25; GPU column of each: [every one a rented machine (4090, H100, 5090, A40), or "none — local M4" for the two $0 gate runs]
   rows naming a model-provider API call as spend: 0
   ledger baseline: RunPod balance at adjudication (John, checked 2026-08-07): **$106.73** (prior spend from $150 predates this cap — Experiment 1 / Stage 3 work; this ledger starts at $0). …
   John's ruling of 2026-08-30, as amendment-a3.md quotes it: the Amendment A2 ceiling of $400 covers all Minimum Viable Mind compute across every vendor, true spend to date is about $281 to $300, so th…
   ledger running total on 2026-08-17 (just before that ruling): True   [~$181.4]
   paper says 'Whole programme to the stop of experiment C: about $230.94': True
   paper says 'That figure is rented machine time only.': True
   paper says 'whole programme of three registered experiments for about $230.94 of rented compute': True
```

**What is true.** "That figure is rented machine time only" holds: every ledger row is a rented machine or a $0 local run, and none is a call to a model provider. The worklog does hold the battery rehearsal's calls. Its entry of 2026-10-18 is titled "Before the first call: the measurement rehearsal of battery entries 1 and 2 starts on John's go "Go up to $50"". That was found by listing the project's worklog entries for 2026-10-18.

**What is not.** The figure is not the whole programme's rented time:
- The ledger's baseline opens at $0 on 2026-08-07, with experiment 1's earlier spend put outside it by name.
- On 2026-08-30 John put "true spend to date" across every vendor at about $281 to $300. The ledger then read about $181.

So "the whole programme of three registered experiments for about $230.94 of rented compute", and Methods' "Whole programme to the stop of experiment C", overstate what the $230.94 covers. The new sentence makes this sharper, not weaker: it says the $230.94 is rented machine time only, which invites the reader to take it as all of it.

This checker wrote "the whole programme of three registered experiments for about $230.94" into its proposal in the check of pull request 190, without opening the ledger's baseline. The error is the checker's and is said so here.

**Notes, not conditions:**
- The $450 ceiling was ruled on 2026-08-30 to cover "all Minimum Viable Mind compute across every vendor". The paper's "about $230.94 of a $450 ceiling" therefore sets a figure for rented machines against a ceiling for every vendor.
- No record opened here reconciles the all-vendor total since 2026-08-30.
- The same "programme stands at about $230.94" phrase is in `STATUS.md` (four places) and the explainer (line 61). That is outside this pull request, and it is worth one line in each when they are next touched.

### 5. The ruling file's added section. MEASURED. Passes.

```
5. ruling quotes John: "Yes to both" -> True | authorship mixed -> True
   ruling's added section says the $230.94 is rented machine time 'to the stop of experiment C': True
```

John's words are quoted as relayed, and authorship is recorded as mixed. The section's own description of the figure ("rented machine time to the stop of experiment C") has the same scope gap as conditions 1 and 2. A dated line under it, saying the figure starts at 2026-08-07 and excludes experiment 1, would close it without editing what John approved.
