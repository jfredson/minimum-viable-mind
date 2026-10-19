**Verdict: PASS WITH CONDITIONS.** Eight changes, each small, all to text written on 2026-10-17; none reopens a ruling or touches a reserved place:
1. **Explainer, line 31: "each with its uncertainty interval above zero" is wrong for the middle figure.** The drop on the self-relevant tasks, 0.10, has the interval 0.000 to 0.200 (`experiments/01-self-indexing-removal-test/removal_ci.json`, `T_self_relevant`, `"lo": 0.0`). Say that two of the three intervals sit above zero and the self-relevant one reaches down to zero.
2. **Paper, line 650: "Four unregistered development runs … were registered in advance as a pipeline and throughput check" contradicts itself and the record.** On 2026-10-04 nothing about experiment C was registered: version 4 of the proposal says "Nothing here is registered and nothing here binds" (`docs/successor-experiment-proposal-2026-10-03-v4.md`, header), and the registration came on 2026-10-09. Write "were stated in advance, in version 4 of the proposal (not registered), as a pipeline and throughput check". If the registered text's own phrase "registered as such in advance" (version 5, section 11, step 4) is wanted, quote it as the registration's wording, with the date of version 4 beside it.
3. **Paper, line 649, and the pull request body: the per-arm costs of the development runs do not match the rows cited.** The cited ledger rows give $0.4744, $0.3347, $0.3341 and $0.3223 for arms M, T, C and F (`compute-ledger.md`, lines 96 to 99 and the table at lines 141 to 144). Rounded to the cent that is $0.47, $0.33, $0.33 and $0.32. The text carries $0.47, $0.34, $0.33 and $0.33, which is the registered proposal's rounding (version 5, line 3726). Either quote the ledger's four figures or cite version 5 for the rounded ones. The total of $1.47 is right either way ($1.4655).
4. **Explainer, line 51: the closure's outcome sentence is in quotation marks but its punctuation is changed.** The closure block reads "not testable — the registered comparison was undefined for every possible model. Separately, removing …" (`amendment-a3.md`, line 565). The explainer has a colon in place of the dash, a semicolon in place of the full stop, and a lower-case "separately". Quote it exactly, as the paper does at line 589 (a dash inside a quotation is allowed, as the Voice Calibration record itself notes for the paper), or take the quotation marks off.
5. **Explainer: three of the five runs the record calls unregistered carry no label.** These are the ceiling measurement (line 47, "A measurement on 2026-09-17"), the fitted detector (line 49) and experiment C's development runs (line 57). None of them is called registered, so the standing rule holds. But the Voice Calibration record says each of the five "are each labelled unregistered where they appear" across all three pieces, and in the explainer that is true of two. Add the word at each of the three places.
6. **Approach note, line 42: the third attempt reads as validated.** "a transplant-ratio measure … validated on hand-set reference systems" says the measure was validated, and the ruled ending is "the measure was not reached". Write "to be validated on".
7. **The paper's header (line 5) and the approach note's header (line 14) say the new text "passed" the two protocols.** Both passes were self-passes, as their own records say. Say "was run through the Voice Calibration Protocol and the Cold Reader pass by the session that wrote it (records beside this file), and checked by a separate session (`docs/reviews/2026-10-17-paper-fold-check-claude-code.md`)". Conditions 2 and 3 sit inside the paper text that header says passed.
8. **The citation of the 2026-10-17 ruling that experiment C stays stopped is out of date.** The explainer (line 61) and the paper (lines 743 to 744) cite it as "on pull request 172". Pull request 172 was merged into the main line on 2026-10-18 (merge commit `abd80e0`), and the file is there (`git show origin/main:docs/rulings/2026-10-17-experiment-c-stays-stopped-ruling.md`). Drop the qualifier, and drop it from the pull request body's figures list too.

# Pairing-rule check of pull request 175: the explainer refresh, paper draft version 0.3, the two pass records and the outside-reader approach note

*Filed 2026-10-18 (Pacific) for a pull request written on 2026-10-17. Filed under `docs/reviews/` rather than an experiment's reviews folder, because the target spans experiment 1 (the removal test), experiment 06 (MVM-0a and Amendment A3) and experiment C (the successor), and the earlier checks of cross-experiment drafts were filed here. Written under the workspace plain-language rule.*

## Who checked, and what was opened

This record comes from a separate Claude Code session. It wrote none of the texts under check, none of the records they quote and neither pass record, and it read no session's chat. It worked in its own worktree (`.claude/worktrees/check-175`, branch `check-paper-fold`, cut from `origin/paper-fold-experiment-06-and-c` at `fe53cd9`). It compared that against the main line at `53bb84a`. The paper and the explainer are byte-identical between the branch's merge base (`a99e8e9`) and `53bb84a`, so "the main line" means the same text whichever of the two is meant. Nothing under check was edited. No model was called, nothing was rented and nothing was spent.

**Opened, in full:** the pull request body; `explainer.md` on the branch and on the main line; the diff of `drafts/paper-removal-test-nature-draft.md` against the main line, and both versions of the file; the two pass records (`drafts/2026-10-17-voice-calibration-pass-explainer-and-paper-v0.3.md`, `drafts/2026-10-17-cold-reader-report-explainer-and-paper-v0.3.md`); `docs/outside-reader-approach-note-2026-10-17.md`; the Cold Reader protocol and the review-process and pattern sections of the Voice Calibration Protocol (master version 2026-10-12, `~/Code/calibration-problem/editorial/`); the pairing-rule section of `docs/outside-review-protocol.md`; the project's `CLAUDE.md`; the candidates list of `docs/outside-reader-shortlist-2026-09-19.md`.

**Opened at the lines the checks hit, not read whole:** every source file named in the pull request body's figures list (listed in `check_figures.py`); `removal_ci.json`; the compute ledger's 2026-10-04 and 2026-10-09 rows and annotation table; version 4's header and version 5's sections 5.6, 11 and the line 3726 table; the closure block of `amendment-a3.md`; the A3 closure dispositions ruling; the stop ruling of 2026-10-12; the two-sided-question rulings of 2026-10-07 and section 2 version 3; the K0 entries of `gate0-null-calibration-findings.md`; `src/model.py` line 78.

**Not opened:** the corpus-positions ledger in the Sentient Horizons repository (the self-pass reports reading it; this check did not repeat that read, and says so under the substance gate below); the paper's v0.2 sections beyond the reserved places and the figures the explainer takes from them; the outside reviewers' own files; the Sentient Horizons essays.

Every finding is labelled MEASURED (a command was run and its output is reported) or ARGUED (a judgment from reading, which a reader can dispute). The scripts and their outputs are in `docs/reviews/2026-10-17-paper-fold-check-scripts/`. `sh docs/reviews/2026-10-17-paper-fold-check-scripts/run_all.sh` re-runs all of them from the worktree root with the system Python (3.14.5, run with `-I`).

## 1. Every listed figure in its named source. MEASURED.

`check_figures.py` holds a table of 164 figures: each figure the body lists, plus the standard deviations of Table 2. Beside each it names the source file the body names and the forms allowed for it (for example "7.6 × 10⁻⁸", or "0.93 to 0.94" for "0.93 → 0.94"). It greps each figure as a fixed string, collapsing line wraps only on a second try, and prints HIT with the line and context, or MISS.

```
$ python3 -I docs/reviews/2026-10-17-paper-fold-check-scripts/check_figures.py | tail -1
160 hit, 4 miss, 164 figures
$ grep MISS …/check_figures.out.txt
MISS  route use T 2,918 (body cites run record)   2026-10-09-reruns-10m-run-record.md
MISS  route use C 0 of 3,000 (body cites run record)
MISS  route use M 33 of 1,387
MISS  route use M 0 of 1,190
```

The four misses are the counts behind experiment C's route-use shares. They are not in the run record the body names. They are in the stop ruling, and the same table holds the HITs `2026-10-12-experiment-c-stop-ruling.md:27` "0.986 (2,918 of 2,959)" and `:29` "(33 of 1,387) … (0 of 1,190)". The paper's Table 3 cites both files, so the paper is right and the slip is the body's alone. Note, not a condition.

A fixed-string HIT on a short number can be a coincidence, so every HIT on a figure of four characters or fewer was read in its printed context. Five turned out to have matched the wrong line. All five were then found on the right line by hand:

- the twin's "T_sr_rev 1.00": `twin-binding-anomaly.md:54`;
- "one in twenty-seven": `fitted-position-sweep-findings.md:129`;
- the development runs' "$0.34" and "$0.33": these are the subject of condition 3;
- "0.106": the paper's toy figure is at `successor-experiment-proposal-2026-10-07-v5.md:1303` and `:1539`.

**The ledger rows.** `ledger_rows.py` reads each 2026-10-04 and 2026-10-09 row of the compute ledger, takes the per-run actual, and compares it to the cent with what the new text carries:

```
2026-10-04 succ_m_10m_seed0  ledger $0.4744 (by arithmetic)  carried $0.47  ledger rounded $0.47  matches
2026-10-04 succ_t_10m_seed0  ledger $0.3347 (by arithmetic)  carried $0.34  ledger rounded $0.33  DIFFERS
2026-10-04 succ_c_10m_seed0  ledger $0.3341 (by arithmetic)  carried $0.33  ledger rounded $0.33  matches
2026-10-04 succ_f_10m_seed0  ledger $0.3223 (by arithmetic)  carried $0.33  ledger rounded $0.32  DIFFERS
2026-10-09 succ_m_10m_seed0  ledger $0.5045 (from the vendor's own bill)  carried $0.5045  …  matches
2026-10-09 succ_t_10m_seed0  ledger $0.3980 (from the vendor's own bill)  carried $0.3980  …  matches
2026-10-09 succ_c_10m_seed0  ledger $0.4007 (from the vendor's own bill)  carried $0.4007  …  matches
sum 2026-10-04 $1.4655
sum 2026-10-09 $1.3032
```

That is condition 3. The rounded figures come from the registered proposal (version 5, line 3726: "$1.47: $0.47, $0.34, $0.33 and $0.33 for arms M, T, C and F … the four 2026-10-04 rows (lines 96 to 99)"). So the registered text itself carries two cents that its own cited rows do not support. That text is registered and is not this pull request's to edit. It is said here so the next reader of version 5 knows.

**Figures in the new text that the body does not list.** `unlisted_numbers.py` takes every number in the lines the pull request adds to the paper, and in the whole explainer. It skips dates, commit ids and section numbers, and prints each number that does not appear in the body (85 file-and-number pairs). Each one was traced. 45 of them carry a claim that needs a source, and `check_figures.py unlisted` greps those in the file the text cites or, where it cites none, the file this check found them in:

```
$ python3 -I docs/reviews/2026-10-17-paper-fold-check-scripts/check_figures.py unlisted | tail -1
45 hit, 0 miss, 45 figures
```

They include:

- the explainer's experiment 1 figures, from `removal_ci.json` and the v0.2 paper;
- the ceilings 0.2921 and 0.3227, chance 0.125 and the 0.10 floor rule;
- the architecture facts: width 448 in `gate0-null-calibration-findings.md`, 12 blocks at `src/model.py:78`, the 103-token vocabulary in `amendment-a3.md`, and 585,552,384 tokens;
- the pilot's $13.92, which the paper states with no citation and which is in `gate2-pilot-findings.md:7`;
- $12, $150 to $172, the 1.25 alarm, the software versions, "Approved.", and "15 serious findings, all closable by rewording".

The other 40 are Table 2's standard deviations and the toy figures, both already in the first table, or counts that carry no claim (layer numbers, "6 of 8" inside a quoted v0.2 passage). The approach note's "a real structure on the 2-billion and 8-billion models" is in `blind-arm-findings.md:108`. **Nothing untraced remains.**

## 2. "Registered", "verified", "measured" and the five unregistered runs. MEASURED, with each hit read.

`status_words.py` splits the new text into sentences. That is the paper's added or changed paragraphs, the explainer and the approach note. It prints every sentence containing registered, pre-registered, registration, pre-stated, verified, verification, measured, calibrated or calibration, tagged SENT if the sentence cites a committed file by name, PARA if only its paragraph does, NONE if neither.

```
$ python3 -I docs/reviews/2026-10-17-paper-fold-check-scripts/status_words.py | tail -1
 {'SENT': 47, 'PARA': 55, 'NONE': 38}
```

All 38 NONE hits and all 55 PARA hits were read (`status_words.out.txt`). The NONE hits are:

- the dated note;
- the abstract, which by form carries no citations, and every sentence of which restates a cited section below it;
- the "What the constructed line licenses" paragraph, which sums up the cited paragraphs above it;
- two sentences of the explainer;
- the approach note, which cites in a sources list at its end by design.

One limit: the script's "changed paragraph" test also picked up two v0.2 paragraphs that happen to share a line with the additions (the abstract's first half and the registered-verdict paragraph). They were read and are unchanged v0.2 text.

Two of the hits are wrong on the record:

- **Paper, line 650 (condition 2).** "Four unregistered development runs … were registered in advance". Experiment C was registered on 2026-10-09 (`docs/rulings/2026-10-09-registration-commit-ruling.md`). The runs were on 2026-10-04, under version 4, whose header says "Nothing here is registered and nothing here binds". MEASURED: `head -12 docs/successor-experiment-proposal-2026-10-03-v4.md`. The paper inherits the phrase from version 5's own "registered as such in advance" (line 3519), so the defect starts in the registered text. Its reach into the paper is this pull request's.
- **Approach note, line 42 (condition 6).** "validated on hand-set reference systems". The word "validated" does not appear in the status list, so the script did not flag the line; it came to light on reading the "pre-stated verification" hit beside it.

`status_words.py unreg` then prints every sentence that names one of the five runs the record calls unregistered (the positive control, the fitted sweep, the ceiling measurement, the control-learnability pilot, experiment C's development runs) with its label:

```
[ceiling measurement | says unregistered]       paper ¶19
[control-learnability pilot | says unregistered] paper ¶19
[positive control | says unregistered]          paper ¶22
[fitted sweep | says unregistered]              paper ¶23
[C development runs | says unregistered]        paper ¶28, ¶38
[ceiling measurement | SAYS REGISTERED]         explainer ¶24
[control-learnability pilot | says unregistered] explainer ¶24
[positive control | says unregistered]          explainer ¶25
[fitted sweep | no label]                       explainer ¶25
[C development runs | no label]                 explainer ¶29, ¶31
```

The explainer ¶24 hit marked SAYS REGISTERED is "the registered metric divides by the distance …". The word attaches to the metric, which was registered, and not to the measurement. Read in full, the sentence does not call the measurement registered. The paper's other three SAYS REGISTERED hits are also correct on reading:

- ¶14 is the primary battery's registered ceiling of 0.2921;
- ¶24 is gate 1's positive controls, which are a different thing from the unregistered positive control;
- ¶28 is the registered procedure applied to the development checkpoints.

So **nothing the record calls unregistered is called registered**, in any of the three pieces. The explainer leaves three of the five unlabelled, which is condition 5.

## 3. The ruled sentences, quoted exactly. MEASURED. Passes.

`ruled_sentences.py` collapses line wraps and bold marks on both sides and counts exact occurrences of each ruled sentence in its ruling and in each text, printing every fragment-level use beside them:

```
== 'the built arms as designed are not references; the measure was not reached'
   in its ruling (…2026-10-08-december-result-restatement-rulings.md): 1 exact
   explainer.md: 1 exact   paper: 3 exact   approach note: 1 exact
== 'the test could not discriminate routing from a centre; the cheaper account was taken in advance'
   in its ruling (…2026-10-07-two-sided-question-rulings.md): 1 exact
   explainer.md: 1 exact   paper: 2 exact   approach note: 1 exact
== 'accept the stop'
   in its ruling (…2026-10-12-experiment-c-stop-ruling.md): 1 exact
   explainer.md: 1 exact   paper: 1 exact   approach note: 0 exact
```

Every use in quotation marks is exact. The only near-misses are paraphrases not presented as quotations: the approach note's "relabelled the result as unable to discriminate routing from a centre", twice, in John's first person, and the dated note's "the test could not discriminate routing from a centre, which is weaker". ARGUED: both are acceptable as paraphrase. The first version of the approach note never quotes the second half of the relabel ("the cheaper account was taken in advance"), which a mechanism reader would not miss.

A wider pass over every quotation of four words or more in the explainer and the paper's new paragraphs (`quotes.py`) searched each one verbatim across the repository's committed files. It found condition 4, the explainer's altered closure sentence. That form is in other records (the version 3 proposal and four more), but not in the closure block the explainer cites. It also found one paraphrase in quotation marks: the paper's "report subtracted, processing intact" branch (`pre-registration.md` line 60 reads "the report subtracted and processing intact"). Note, not a condition.

## 4. The three reserved places, the replaced paragraph and the header. MEASURED. Passes.

`reserved_places.py` compares the branch with the main line byte for byte:

```
(1) title: SAME
(2) Discussion: 7 paragraphs on main, 7 on branch
    ¶1 SAME  ¶2 SAME  ¶3 SAME  ¶4 SAME  ¶5 SAME
    ¶6 DIFFERENT main f34b09a113 branch aec433dea5  The constructive turn, as it ran. …
    ¶7 SAME
    paragraph with 'is conversational infrastructure': SAME
    paragraph with 'was voided by a control committed before any data existed': SAME
(3) 'router reading twice over' passage (key sentence to 'Methods §Statistics).'): SAME … 704 chars
(4) v0.2 'constructive turn', up to the retained-independence sentence, quoted in the dated note: SAME (verbatim)
    retained-independence sentence on main kept in the new paragraph: SAME
(5) header says the v0.2 text has NOT passed: YES
```

The check can tell a change: it flags the one Discussion paragraph that was replaced, and only that one. The diff's removed lines (`paper_removed_lines.out.txt`, 17 lines) are:

- the header;
- the abstract's last line, extended in place;
- the replaced paragraph;
- the first and last lines of "Compute and cost".

Nothing else in the v0.2 text was taken out. The rewording of "Compute and cost" ("Whole program" becomes "Experiment 1") is a v0.2 sentence the dated note does not list among its changes. It is a correct narrowing, and the note could name it. Note, not a condition.

## 5. The two protocols, applied by this session. ARGUED unless marked.

The filed passes are self-passes, and both say so. What follows is this session's own run of the Voice Calibration substance gate and the Cold Reader's five checks on the explainer and on the paper's two new results sections. It applies the protocols as written (the master copies named above) and does not grade the self-passes line by line.

### Voice Calibration, substance gate

- **Receipts.** MEASURED, by checks 1 to 3 and `quotes.py`. Four receipts fail: conditions 1, 2, 3 and 4. The rest hold.
- **Ground truth.** Every cited source behind a figure was reopened at the line, by script.
- **Adversarial read.** The self-pass named three objections and the texts meet them: three endings with no positive called a deliverable; the relabel as a rescue after the fact; nulls dressed as instrument failure. Two more a hostile expert would raise:
  - *The relabel concedes a design fault in the registered control.* The control's rule ("drops as much as") was read on point estimates, and its margin's interval was computed on 2026-08-04, so the rule could never have told the two readings apart. That is the same thing as "the test could not discriminate", so the texts already concede it; they meet the objection.
  - *Why run, for $1.3032, a check the registration said would very likely fail?* Neither text answers. The record's answer, as this session reads it, is that only the registered check could stop experiment C by its own rule rather than by judgment. The texts could say that in one clause. Option for the author.
- **Corpus coherence.** Not run against the corpus-positions ledger by this session. One inside-the-project tension was checked. The explainer's "zero is a permitted reading" follows section 2 version 3 (line 262, "Zero is a permitted reading"), which also says how Scope's "non-zero on the gradient" is to be read (line 277). But this repository's `CLAUDE.md` still states the standing rule as "The honest output is non-zero on the gradient, never a verdict". MEASURED with grep. The texts follow the later ruling and are right. `CLAUDE.md` is the file out of date, which is outside this pull request.

### Voice Calibration, passes 1 to 6, the mechanical part

`voice_scan.py`:

```
== explainer.md (3037 words)
   em dashes outside quotes: 0; inside quotes: 0
   flagged words: none
   ', not ...' outside quotes: 5; 'not ... but': 1; 'rather than': 2
== paper, two new results sections (3897 words)
   em dashes outside quotes: 1; inside quotes: 0   [the one hit is inside the closure quotation, which spans a line break the scan did not join]
   flagged words: none
   ', not ...' outside quotes: 8; 'not ... but': 0; 'rather than': 2
```

Those figures agree with the self-pass. The contrastive pairs are over Pattern 4's "one per piece" in both texts. The self-pass logs most of them as ruled wording, which is a defensible deliberate choice, and the protocol leaves the choice to the author.

### What this read finds beyond the self-pass

- **The paper's new section uses three battery names it never defines.** "T_si", "T_sr" and "T_sr_rev" appear at line 402, the A2 pilot endpoint, and again at lines 413, 416 and 504. The self-pass lists the defined terms as T_act, T_other, T_state, T_syntax, L0, L1, θ and δ, so its claim is accurate. But T_si also names experiment 1's self-irrelevant battery in the v0.2 Results, where it is defined, and a specialist will carry that meaning over. The pre-registration says it is the analogous battery (`pre-registration.md` line 335, "T_si (self-irrelevant integration)"), so the carry-over is right. T_sr_rev is defined nowhere in the paper. Option: one clause at line 402.
- **Internal shorthand in the paper's new sections** (Pattern 14's "internal project shorthand"): "Q5 of the post-removal-test roadmap", "the December-result roadmap", "the first release" and "the second release" (a release here means one approved tranche of money), "the free-arm run", and "step 4b". A specialist reader can decode most of them from context. "Release" is borrowed staged-spending vocabulary that the workspace rule asks to be translated.
- **Explainer, line 29: "substituting at a ratio of 0.006 against 0.348".** The uninformed reader cannot say what the ratio is a ratio of. This is the first number in the piece that carries no plain anchor. Option: "copying it into another run moved the behaviour 0.006 as much as copying the self-tracking structure did, against 0.348".
- **Explainer: "episodes"** (lines 41 and 49; one invented dialogue) **and the "× 10⁻⁸" notation** are unglossed for the father lens. "Standard deviations" and "transformer" were already reported as open options by the self-pass.
- **Explainer, line 31: "The model's ability to report on itself did not fall (+0.059 …)".** The point estimate is a fall of 0.059 with an interval that spans zero. The v0.2 paper's wording, "within control wobble", is more exact. Option: "did not fall measurably".
- **Explainer, line 49, the noise calibration.** "Random damage of matched strength moved the deciding batteries by 0.006 and 0.0095 on the models that learned" is one battery (T_si) on two models, and the figures are the 95th percentile of 120 random ablations, not a typical move. The sentence also omits what the paper discloses at line 509: K0's number was applied after the measurement was seen ("RULED 2026-09-16", `gate0-null-calibration-findings.md` line 347). The explainer's selection-pressure claim would be stronger with that clause. Option, strongly recommended.
- **Final check (Pattern 8 and Pattern 3).** The explainer's last sentence, "say what would count as evidence, build the instruments, and let the results land where they land", is a triplet closing on an aphorism. To this reader it still performs a little. The author's call.

### Cold Reader, the five checks, this session's own reading

1. **The ninety-second test.** The skeptical reader's first contact is the italic header, which names `ROADMAP.md`, a spec path and two protocols before the first sentence of prose. For an internal companion that is acceptable. As the essay's seed it is the first thing to go. In the body, the self-pass's reading holds, that attention wobbles at "The bet is a premise". The uninformed reader stops earlier than the self-pass found, at line 29's ratio, before "transformer" at line 39.
2. **Coinage budget.** This session counts about twenty terms a newcomer must hold. Beyond the self-pass's dozen: the acting channel or authorship input, the loss condition, the ceiling, the detector, the shuffled baseline, the kill, the noise calibration, hand-set references, the five signs of depth. The verdict is the same as the self-pass's: a deep-context piece. It signposts itself, at line 37, and has no on-ramp to link yet.
3. **Closed-loop check.** Every inline citation in the explainer points into the repository, and none points outside. That agrees with the self-pass. Its option 1, one named outside voice, is the highest-value change for the essay version.
4. **Genre pattern-match.** The self-pass found that the premise paragraph could screenshot as the genre. "Why bother" (line 79, "Believe too easily and you hand moral standing to autocomplete; dismiss too easily and you risk building minds without noticing, at industrial scale") could too: balanced antithesis with stakes and no number. Everything between those two paragraphs could not. Agreed with the self-pass that the explainer shows selection pressure and stakes strongly. The paper's new sections do not read as the genre.
5. **The journey test.** The self-pass names one turn the reader takes on trust, the move to the two-sided question. There is a second one, at line 55. "The closure left one question open: how much of a model's act is organised around its answer" moves from *whether* a centre is there to *how much*. The reason is the ruling of 2026-09-20 that a centre is a matter of degree (`docs/rulings/2026-09-20-center-as-degree.md`), which the explainer never mentions. A cold reader cannot say why the question changed shape. Option: one sentence.

The verdict on the protocols, as this session's judgment: the two pieces are fit to stay working documents once conditions 1 to 5 are made. Neither is ready to leave the repository, which neither claims to be: the explainer's header says it becomes an essay only after the protocols, and the paper's v0.2 text has not passed.

## 6. The approach note names no reader and sends nothing. MEASURED. Passes.

`approach_note.sh` greps the note, case-insensitively, for every name and organisation on the shortlist's candidates list, for words that would mean it went out, and for a salutation line:

```
Shai: 0  Riechers: 0  Simplex: 0  Shiller: 0  Butlin: 0  Nanda: 0  DeepMind: 0  Berg: 0
Reciprocal: 0  Long: 0  Sebo: 0  Chis-Ciure: 0  Sussex: 0  Seth: 0  Ren: 0  Center for AI Safety: 0
Eleos: 1     151:- The external commentary the second version refers to is the Eleos
Anthropic: 1 152:  commentary on the Anthropic global-workspace paper, linked in
--- sending words
9:registrations it describes; nothing here has been sent. Every figure is
--- salutation lines
none
```

No person is named and the salutation is blank. The two hits are in the sources list and name a published work, not an addressee. ARGUED: each version is written to a reader identifiable by their work: version 1 by "belief-state geometry", version 2 by "the distinction you drew". That is what the shortlist asked for. Before either goes out, the workspace's link rule of 2026-10-18 applies to an email. The global-workspace paper, the commentary and the belief-state-geometry work are named in the body without links, and need links that John has opened.

## 7. Word counts of the explainer. MEASURED.

`word_counts.py` counts whitespace-separated words, three ways, each rule stated in the script:

```
explainer.md, this branch: A whole file 3037; B body with citations 2934; C body prose 2864
explainer.md, origin/main: A whole file 1682; B body with citations 1582; C body prose 1582
    3037 explainer.md
```

"Prose" means the body after the header, without any parenthetical that contains a backticked file name and without backticked spans. The body's "about 2,900 words of prose (3,050 with citations)" matches these: 2,864 by rule C, and 3,037 for the whole file. The explainer is about 360 words of prose over the brief's "under about 2,500", and 1,282 over the main line's 1,582. The overrun is disclosed in the body and is John's to settle.

## Notes for the author and for John (not conditions)

- **Tool names in the paper's Results.** "Gemini 3.1 Pro and ChatGPT 6 Astra" appear in the A3 closure paragraph, line 587. The workspace rule on tools, ruled 2026-10-18 and so after this pull request was written, keeps disclosure where it bears on trust and out of essay text. That outside models of other families reviewed the closure does bear on trust. Whether the names belong in the Results prose or in Methods is John's call. The v0.2 text already names the models of experiment 1's review, at line 890.
- **"Closed by rewording".** The source says "closable by rewording" (`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md` line 16). The same ruling rules all 22 items as recommended, so "closed" is supported. No change is needed.
- **The spelling split** (American in v0.2, British in v0.3) is already flagged in the self-pass, and is real.

## What this check did not do

- It did not re-derive any figure from raw run output. Every figure was checked against the committed findings, ledger and ruling files the texts cite, which is what the pull request claims.
- It did not run the corpus-coherence read against the Sentient Horizons ledger.
- It did not check the v0.2 text, which is not under check and still says it has not passed.
- It did not open the outside reviewers' files.
