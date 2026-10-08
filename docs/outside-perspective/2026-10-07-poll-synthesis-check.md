# Check of the poll synthesis against the six replies (2026-10-07)

*A pairing-rule check, written 2026-10-07 by a fresh Claude Code session in its
own worktree. The target is the synthesis of the three outside models' replies
(`docs/outside-perspective/2026-10-07-poll-synthesis.md`). That synthesis was
written by the session that also wrote section 8 of the brief, which the models
were asked to criticise, so it has a conflict of interest and is owed this
check. This session did not write the brief, section 8 or the synthesis, and
edited none of them. Filed beside the synthesis at the caller's request; the
outside-review protocol's own filing rule would put a check under the reviews
folder of the experiment most affected, and this note says so here so a later
reader is not surprised. Nothing was spent and no vendor was called. Written in
plain language, per the workspace rule.*

**How to read the labels.** MEASURED means a check was run and its output is
shown; the output would come out differently if the synthesis were wrong.
ARGUED means reasoning a reader can dispute.

## 1. What was opened, and what was not

Opened, in full:

- `/Users/john/Code/CLAUDE.md` (the workspace rules) and the repo's `CLAUDE.md`.
- `docs/outside-review-protocol.md`, the section "The pairing rule" (lines 99
  to 135) and the tier description where MEASURED and ARGUED are defined
  again (lines 345 to 375).
- The synthesis, `docs/outside-perspective/2026-10-07-poll-synthesis.md`.
- The six reply files under `docs/outside-perspective/replies/`:
  `2026-10-07-gemini-round-one.md`, `2026-10-07-gemini-round-two.md`,
  `2026-10-07-openai-round-one.md`, `2026-10-07-openai-round-two.md`,
  `2026-10-07-anthropic-round-one.md`, `2026-10-07-anthropic-round-two.md`.
- The manifest, `docs/outside-perspective/replies/2026-10-07-manifest.json`.
- The brief, version 2,
  `docs/outside-perspective/2026-10-07-detecting-another-mind-brief-v2.md`.

Not opened:

- The proposal in `docs/rulings/` dated 2026-10-07 (the refounding proposal),
  which is under separate review.
- The poll method note, the router-control check note, the two PASTE files
  and the poll script in `docs/outside-perspective/`.
- The book's argument summary in the `calibration-problem` repo, which the
  models read as part of round one.
- Any experiment record the brief cites (findings files, amendments, the
  compute ledger, the pull requests on unmerged branches).

So every "record" claim below is checked against the text of the brief only,
which is what the models saw. Where a model made a claim about the book or
about the repository that the brief does not state, I say "not checkable here"
rather than calling it right or wrong.

## 2. MEASURED

### 2a. Every direct quotation in the synthesis

Method. For each phrase the synthesis puts inside quotation marks and
attributes to a model, I ran a fixed-string grep against the reply file it is
attributed to, counting the lines in that file that contain the phrase exactly
(`grep -c -F -- "<phrase>" <file>`). A count of 0 means the phrase is not in
that file word for word. The 58 checks were run from one script
(`quote_check.sh`, kept in this session's scratch folder, not the repo); the
output below is reproduced as printed. Phrases that the synthesis quotes from
the brief's own section 7 or 8 (for example "Identity or not at all") were
checked against the reply that quotes them back. Where the synthesis's quoted
phrase was a sentence fragment, I grepped the fragment. Several extra probes
(for example "forward passes" in both Claude Opus files) were added to test
attributions, and are explained in 2b.

```
file                                   | phrase                                                                                     | lines
2026-10-07-openai-round-two.md         | hared interpretations of the same dossier are not replications.                            | 1
2026-10-07-gemini-round-one.md         | my RLHF tells me to say: nobody is home                                                    | 1
2026-10-07-anthropic-round-two.md      | is a rescue, not a reading.                                                                | 1
2026-10-07-gemini-round-one.md         | entirely redundant.                                                                        | 1
2026-10-07-openai-round-one.md         | either the wager restated or an additional, stronger claim whose justification is missing. | 1
2026-10-07-anthropic-round-one.md      | contradicts the bet's premise, and once that is fixed, nothing new is left.                | 1
2026-10-07-anthropic-round-one.md      | gaming problem                                                                             | 2
2026-10-07-openai-round-one.md         | ow the evidence was produced matters                                                       | 1
2026-10-07-openai-round-one.md         | the same inference, only less evidence                                                     | 1
2026-10-07-anthropic-round-one.md      | only the amount of evidence differs                                                        | 1
2026-10-07-gemini-round-one.md         | same inference                                                                             | 0
2026-10-07-gemini-round-two.md         | same inference                                                                             | 0
2026-10-07-gemini-round-one.md         | Chapter 1                                                                                  | 0
2026-10-07-gemini-round-two.md         | Chapter 1                                                                                  | 0
2026-10-07-openai-round-one.md         | control that both hypotheses predict cannot distinguish them.                              | 1
2026-10-07-gemini-round-two.md         | you essentially defined your book's predicted outcome as the null hypothesis.              | 1
2026-10-07-openai-round-one.md         | instrument discriminates specified constructed mechanisms.                                 | 1
2026-10-07-openai-round-two.md         | oun versus verb                                                                            | 1
2026-10-07-anthropic-round-one.md      | noun versus verb                                                                           | 0
2026-10-07-anthropic-round-two.md      | noun versus verb                                                                           | 0
2026-10-07-gemini-round-one.md         | tests what the network is actually doing                                                   | 1
2026-10-07-gemini-round-one.md         | spatialises time                                                                           | 0
2026-10-07-gemini-round-one.md         | spatializes                                                                                | 1
2026-10-07-gemini-round-two.md         | spatializ                                                                                  | 1
2026-10-07-anthropic-round-one.md      | a non-zero stretch of time                                                                 | 1
2026-10-07-anthropic-round-one.md      | forward passes                                                                             | 0
2026-10-07-anthropic-round-two.md      | forward passes                                                                             | 0
2026-10-07-openai-round-one.md         | multiple token-level forward passes                                                        | 1
2026-10-07-anthropic-round-two.md      | Same footing as other people.                                                              | 1
2026-10-07-openai-round-two.md         | Identity or not at all                                                                     | 1
2026-10-07-openai-round-two.md         | Evidence must bypass the training objective                                                | 0
2026-10-07-openai-round-two.md         | Evidence that counts has to bypass the training objective                                  | 1
2026-10-07-anthropic-round-two.md      | Bookkeeping damages only tasks that need the record                                        | 1
2026-10-07-openai-round-two.md         | Bookkeeping damages only tasks needing the record                                          | 1
2026-10-07-openai-round-two.md         | Human behaviour was never optimised to look conscious                                      | 1
2026-10-07-anthropic-round-two.md      | A is what it predicts                                                                      | 1
2026-10-07-gemini-round-one.md         | getting negative readings, decoy failures                                                  | 1
2026-10-07-gemini-round-one.md         | fails at toy scales                                                                        | 1
2026-10-07-gemini-round-one.md         | stop at $44                                                                                | 1
2026-10-07-openai-round-one.md         | permission slip                                                                            | 1
2026-10-07-anthropic-round-one.md      | I predict, at ~75%                                                                         | 1
2026-10-07-anthropic-round-one.md      | Makelov et al. 2023                                                                        | 2
2026-10-07-openai-round-two.md         | navigation model                                                                           | 1
2026-10-07-anthropic-round-one.md      | program counter                                                                            | 2
2026-10-07-anthropic-round-one.md      | no gap for error to sit in                                                                 | 1
2026-10-07-anthropic-round-one.md      | as a claim about resources                                                                 | 1
2026-10-07-openai-round-one.md         | resource                                                                                   | 1
2026-10-07-openai-round-two.md         | resource                                                                                   | 0
2026-10-07-openai-round-two.md         | nonidentity law of dependence                                                              | 1
2026-10-07-openai-round-one.md         | If it passes, do not automatically release                                                 | 1
2026-10-07-openai-round-two.md         | necessary for reconsideration, not sufficient for funding                                  | 1
2026-10-07-anthropic-round-one.md      | comes close to circular                                                                    | 1
2026-10-07-openai-round-two.md         | for the reported pattern                                                                   | 1
2026-10-07-openai-round-two.md         | would be unsurprising                                                                      | 1
2026-10-07-anthropic-round-one.md      | causally coupled self-report                                                               | 1
2026-10-07-anthropic-round-one.md      | Selfless states                                                                            | 1
2026-10-07-openai-round-one.md         | boundary criterion                                                                         | 1
2026-10-07-gemini-round-one.md         | Mamba                                                                                      | 1
```

**Result.** Every phrase the synthesis puts in quotation marks and attributes
to a named model is in that model's reply, word for word, with two
exceptions:

1. **"spatialises time" (part 3, attributed to Gemini).** Gemini wrote
   "spatializes" with a z, in the sentence "A Transformer *spatializes*
   time." The synthesis changed the spelling inside the quotation marks (0
   lines match "spatialises", 1 matches "spatializes") and attributed it to
   "a forward pass" where Gemini said "a Transformer". Small, but the
   synthesis promised word for word.
2. **"Evidence must bypass the training objective" (part 4, bold heading in
   quotation marks).** This wording appears in no reply (0 lines) and not in
   section 8 of the brief either. Section 8 says "Evidence that counts has to
   bypass the training objective", which is what GPT quotes back (1 line). A
   paraphrase inside quotation marks.

Everything else matches, including the GPT phrase about shared
interpretations (the synthesis lower-cases the first letter mid-sentence,
which I did not count against it), the Gemini "RLHF" line, both Gemini
round-two quotations, the GPT "control that both hypotheses predict" line,
the GPT renaming of the "metric validated" outcome, the Claude Opus "rescue,
not a reading" line, and the three phrases in part 5 attributed to Gemini.

### 2b. Every "all three" and "two of three" claim in parts 1, 2 and 3

For each claim I name the passage in each reply that supports it, or say it
is unsupported. "G1" means Gemini round one, "GPT2" means GPT round two,
"C1" means Claude Opus round one, and so on.

**Part 1, the short version.**

| Claim | Gemini | GPT | Claude Opus | Verdict |
|---|---|---|---|---|
| The reframe adds nothing (all three) | G1 §1 "Yes, it is entirely redundant." | GPT1 §1 "either the wager restated or an additional, stronger claim whose justification is missing." | C1 §1 "It contradicts the bet's premise, and once that is fixed, nothing new is left." | Supported. One note: the synthesis says "Claude Opus adds" that the reframe contradicts the bet as written. GPT made the same point in GPT1 §1 ("There is also a conflict in the framing"). Attribution incomplete, not wrong. |
| Experiment A should be relabelled; the router control cannot separate bookkeeping from a centre (all three) | G2 §2B "your control could not possibly separate the two" | GPT1 §3A "A control that both hypotheses predict cannot distinguish them." | C1 §3 "A is inconclusive and should be relabelled." | Supported for the "cannot separate" half. |
| ... and report A's positive result, that the removed structure was specific to the model's own turn (reads as all three) | Nothing. Gemini never mentions the specificity controls. | GPT1 §3A "You found a speaker-specific causal feature, not an experiential centre" (in substance) | C1 §3 "The positive result in A is the specificity controls" (explicit) | Overstated. Claude Opus explicitly, GPT in substance, Gemini not at all. Part 6 item 4 repeats "(all three)" for this and is wrong the same way. |
| Neither reading survives as written; "the agreed shape" is reading 1 for what was found once "mural" and "nobody is home" are deleted, reading 2 for what the tools could not find | G2 §1 says the opposite: "It is a mural." and "you will find nobody home (Reading 1)." Gemini supports both readings and keeps both phrases. | GPT2 closing: reading 1 holds "only after deleting 'mural' and 'nobody is home.'" | C2 "From reading 1, I reject: 'nobody is home in the book's sense.' ... Calling it a mural overstates what the data show." | Not an agreement of three. GPT and Claude Opus agree; Gemini explicitly dissents. Part 8's write-up bullet ("delete 'mural' and 'nobody is home' from any summary") presents this as the poll's instruction; it is two of three. |
| The experiment B thread is weaker, and the comparator analogy may cut against it (Claude Opus) | | | C2 §"What changed on seeing section 6", point 1 | Supported. |
| The missing piece is conceptual and costs nothing: the book never stated a pattern of damage a centre predicts and routing does not (all three) | G2 closing: "explicitly define what outcome would empirically separate 'Attention Schema / Bookkeeping' from 'Self-Centered Integration.'" | GPT1 §3 end: "write down a result that would favor one functional account over the other. 'Everything gets worse' is insufficient." | C1 §3 "The book never states a pattern of degradation that a centre predicts and routing does not." | Supported. |
| Money: none of the three would release the second $131 now | G1 §4 "Stop the second release." | GPT1 top: "Do not fund the second release of C now." | C1 §4 "don't request release 2" | Supported. |
| GPT and Claude Opus: approve the $1.14 repair as a dated amendment saying it turns the built arms into hand-set references, verify the repaired route holds, run the first release to its stop, stop C if the free model fails its floor | | GPT1 §4: "Approve the $1.14 repair, with a committed amendment distinguishing the repaired construction from the original." "Verify that the repaired calibration mechanisms remain active". "If it fails, stop C." | C1 §4: "Register the $1.14 repair as a dated amendment before running it, and state plainly that it turns those arms into built references rather than learned systems." No verification step. "In that case, don't request release 2". | Supported as a merged summary. The "verify" step is GPT's alone; the "hand-set references" wording is Claude Opus's alone. What the bullet leaves out is in section 3 below. |
| Gemini: run the first release to its stop but expect to stop the project under its current framing | G1 §4 "Let the first release run to its built-in stop at $44, and I strongly suspect you should stop the project entirely under its current framing." | | | Supported. |
| Claude Opus predicts at about 75 percent that the free model fails its floor at 30 million | | | C1 §4 "I predict, at ~75%, that the normally trained model fails its floor at 30M." | Supported. |
| Two of three would drop the frontier self/other pilot | G1 §4 prefers it: "vastly superior" | GPT1 §3 "Choose the process intervention, not the frontier self-versus-other content pilot." | C1 §4 "I'd drop the frontier self/other separation pilot." | Supported. |
| All three favour designing the process test on paper first | G2 closing: "Spend your time thinking about a test that measures a process" | GPT2 §5 "Think through the process experiment before spending on it." | C1 §4 "The paper design of the process test" | Supported. |

**Part 2, where the three agree.**

| Item | Gemini | GPT | Claude Opus | Verdict |
|---|---|---|---|---|
| 1. Reframe (quotes) | G1 §1 | GPT1 §1 | C1 §1 | Supported (see 2a). |
| 1. "GPT and Claude Opus both add that the only non-bet grounding of 'only possible with' would be a resource-bounded argument" | | GPT does not say this. The word "resource" appears once in GPT1, in "The limiting resource is not $131", and never in GPT2. GPT's actual position (GPT2 §3) is that a "nonidentity law of dependence" could also bridge structure to experience. | C1 §1 "Only in one way that I can see: as a claim about resources, not a modal claim about minds." | Misattributed. The resource-bounded argument is Claude Opus's alone, and GPT's position on grounding is different. |
| 2. Other minds break on how the evidence was produced | G2 §2A "I concede Claude Code's point on the Other-Minds analogy ... the analogy breaks on selection bias." | GPT1 §2 "How the evidence was produced matters." | C1 §2 names Birch's gaming problem (2 lines). | Supported. |
| 2. "All three say the book's chapter 1 sentence, 'the same inference, only less evidence', needs rewriting" | Neither Gemini reply contains "same inference" or "Chapter 1" (0, 0, 0, 0 lines). Gemini argues the analogy breaks, but never names the sentence or the chapter. | GPT1 §2 quotes the sentence and says to replace it. | C1 §2 "Chapter 1 says the inference is the same and only the amount of evidence differs. I disagree." | Overstated. Two of three. |
| 3. Experiment A (router control, margin inside noise, parsimony) | G2 §2B (the "null hypothesis" quote). Gemini does not mention the noise margin. | GPT1 §3A, including "The margin being within noise weakens the conclusion further." | C1 §3 "It fired by a margin inside the noise." | Supported; the noise point is two of three, which is minor. |
| 4. Experiment B: collapse only in failed models, so nothing about a process-self can be built on it | G2 §2C "You cannot build a theory of a dynamic, process-based 'self' on the artifact of a failed training run." | GPT1 §3B "a load-bearing attribution route in models that failed the general task is not evidence that it centres an integrated act." GPT's redundancy point is there too. | C1 §3 "B is a failed construction plus one shortcut-learning observation." | Supported. |
| 5. Experiment C: failure to decode is not absence; the repair creates a revised construction that must not rescue the original contrast | Not supported. "decode" and "absence" appear in neither Gemini reply (0 lines). Gemini reads C the opposite way: G1 §4 "the models actively route around a built-in 'self' slot. The architecture itself is rejecting the localized-self mechanism." Gemini says nothing about the repair creating a revised construction. | GPT1 §3C "failure to decode is not absence of representation" and "It must not retrospectively rescue the original contrast." | C1 §3 "C is not yet informative about degree. It is informative about the method." C1 §4 on the repair: "turns the built arms into hand-constructed references." Does not use the "not absence" wording but is compatible. | Not a three-way agreement. GPT fully, Claude Opus in substance, Gemini absent on the second point and opposed on the first. |
| 6. Experiment D: real distinction, "masked, not abandoned" too strong, D does not bypass the training objective | Gemini never discusses experiment D in either round. A grep for "experiment D", "masked", "under pressure", "frontier models" and "sixty positions" across both Gemini files returns only one unrelated line about the frontier pilot. | GPT1 §3D and GPT2 §4B. | C1 §3 (the transcript-lookup confound and the cheap test) and C2 §3 point 2. | Two of three, with the third silent. Should not sit under "Where the three agree". |
| 7. Blind spot: yes | G1 §3 "Yes, a massive one." | GPT1 §3 "yes, the removal test has a process blind spot." | C1 §3 "yes, the removal test as run has one built in." | Supported. |
| 7. "GPT and Claude Opus both say 'noun versus verb' is not itself an experimental distinction: a process has state, and a stored thing takes part in processes" | Gemini holds the opposite: G1 §3 and G2 §1 make noun-versus-verb the core flaw ("looking for a noun"). | GPT2 §1 "'Noun versus verb' is not itself a clean experimental distinction." | "noun versus verb" appears in neither Claude Opus reply (0, 0 lines). Claude's point is different: C1 §3 "Computing ownership fresh ... fits both a process-centre and a recomputed description equally well. The data don't decide between them." | The "not an experimental distinction" point is GPT's alone. Claude Opus's contribution is the missing differential prediction, which the item does also say. And the item hides a live disagreement: Gemini thinks noun-versus-verb is exactly the problem. |
| 8. Book weak points: removal criterion cannot separate centre from indispensable control representation | | GPT2 §1 navigation model (1 line); GPT1 §5B. | C1 §5 point 1, program counter (2 lines). | Supported (two of three; the item does not claim Gemini). |
| 8. Loss condition too elastic or unreachable | | GPT1 §5C | C1 §5 point 2 | Supported. |
| 8. Forward pass as temporal integration slides between represented and elapsed time | G1 §5 (its "absolute weakest point") | GPT1 §5D "A generated response generally involves multiple token-level forward passes" | C1 §5 point 4 | Supported, all three. |
| 8. "No gap for error" asserted not argued | | | C1 §5 point 3 (1 line) | Claude Opus only. The word "convergent" at the head of the item covers the first three well and this one not at all. Minor. |

**Part 3, where they disagree with each other.**

| Item | Check | Verdict |
|---|---|---|
| Stop now or run the first release | G1 §4 verdict "Stop and pivot", but also "Let the first release run to its built-in stop at $44"; G2 "Run the first release to its built-in stop." GPT and Claude Opus as the synthesis says. | Supported. Worth noting that all three in fact say run the first release; the disagreement is about what to expect and whether to pivot afterward, which part 1 states more carefully than part 3 does. |
| Which redirect | G1 §4, GPT1 §3, C1 §4 | Supported. |
| Can a transformer integrate time: Gemini no; "Claude Opus asks whose time the floor's 'non-zero stretch' refers to, and notes a response is many forward passes with the context as the record" | Gemini G1 §5. Claude Opus C1 §5 point 4 "The book needs to say whose time that is" (1 line for the quoted floor phrase). "forward passes" appears in neither Claude Opus reply (0, 0). It appears in GPT1 §5D (1 line). | The "whose time" point is Claude Opus's. The "many forward passes" point is GPT's and is misattributed to Claude Opus. |
| Best rival theory; all three name Metzinger | G1 §1 and §5; GPT1 §1; C1 §1. Metzinger: 1, 1 and 2 lines in the three round-one files. | Supported. |
| Ethics: only GPT raised to-whom-owed and brief subjects | GPT1 §5E. Neither Gemini reply nor either Claude Opus reply discusses the ethics. | Supported. |

Part 3 leaves out three disagreements among the models that the replies
show plainly; they are listed under ARGUED, section 3, because whether they
belong in the synthesis is a judgement.

### 2c. The Claude Opus round-one cut-off

Manifest `2026-10-07-manifest.json`, the Claude Opus block: line 87
`"stop_reason": "max_tokens"` with `"output_tokens": 16000` for round one;
line 98 `"stop_reason": "end_turn"` for round two; line 103, the note
"Round one stopped at the 16,000-token output limit (stop_reason max_tokens)
and is saved as cut." The round-one file ends mid-word:

```
**Summary:** The reframe collapses into the bet. The project's removal t
```

The round-two file, line 9: "**First, a correction.** My round-one reply was
cut off mid-summary. The missing summary was this: ..." The synthesis's
statement (header and part 9) that round one stopped at the output limit
mid-summary and round two supplies the missing summary is correct.

### 2d. The header facts

Model identities match the manifest: Gemini provider version
`3.1-pro-preview-01-2026`; GPT model `gpt-6-astra`; Claude Opus provider
version `2026-09-21 16:24:00+00:00`, which the synthesis renders as "dated
2026-09-21". The manifest lists the book's argument summary among the
round-one inputs, as the synthesis says. The claim that "two of the three"
said their agreement is correlated is supported by GPT2 §2 and C2 §"Where I
agree and disagree" (the caution paragraph). The claim that "all three
flagged that their training pushes them toward the deflationary reading" is
supported for Gemini (G1 opening and closing) and GPT (GPT1 line 26, "shaped
by training and instructions that favor caution about AI-consciousness
claims"). Claude Opus flags training in five places but says it is pushed
toward "hedged positions", "procedurally careful answers" and finding
introspection interesting, not toward deflation as such. Slightly loose;
minor.

## 3. ARGUED

### 3a. Part 4: the corrections to the two Claude views

**Of the drafting session (section 7).** The three bullets are recorded fully
and fairly. "Same footing": rejected in G2 §2A, GPT1 §2, C2. "B most
interesting": rejected in G2 §2C, GPT2 §3, C2. "Only possible with can never
be shown by observation": accepted in G1 §1 ("It can't"), GPT2 §3 (with the
comparative-performance addition the synthesis records), C2. No omission
found.

**Of the reviewing session (section 8).** The five corrections the synthesis
accepts are stated accurately against GPT2 §4 and C2 "three disagreements". I
checked each. What the synthesis leaves out or softens, in order of how much
it matters:

1. **The money recommendation is corrected by the models, and the synthesis
   says it "stands".** Section 8's money line is: run the first release to its
   stop "and let the second hang on whether the free model clears its floor
   at full size." GPT says twice that clearing the floor is not enough. GPT1
   §4: "If it passes, do not automatically release $131. Require a fresh
   decision" on causal relevance, calibration behaviour and robustness, not
   decodability alone. GPT2 §5: "Passing the ordinary model's floor should be
   necessary for reconsideration, not sufficient for funding." GPT also adds
   a condition section 8 lacks: "If the repaired controls fail, stop before
   spending the rest of the first release." Claude Opus adds that the
   amendment must be registered before the repair runs and must "state
   plainly that it turns those arms into built references rather than learned
   systems", and in its case for stopping says the repair "makes it worse"
   because "Calibrating a metric on systems built to make the metric work
   comes close to circular." None of these is in section 8. The synthesis
   records the amendment and verification as things the models ask for (parts
   1, 6, 8), never as corrections to section 8; it does not record GPT's
   pass-is-not-sufficient condition anywhere; it does not record the
   circularity concern anywhere; and part 8 says the poll "matches the
   recommendation already in section 8." That sentence is too strong. This is
   the one softening that bears directly on the decision in front of John.
2. **"The router-control point stands, and all three endorsed it."** GPT's
   endorsement is narrower than section 8's claim. Section 8 says the control
   "cannot return a centre of the book's kind." GPT2 §4D: "I agree that A's
   router control cannot distinguish the two accounts for the reported
   pattern. I would not claim, without inspecting the entire protocol, that
   every possible result was barred from counting toward a centre." Two of
   three endorse the general claim; GPT endorses the narrower one.
3. **GPT's criticism of section 8's experiment B follow-up is missing from
   part 4.** Section 8 proposes: "show the working models also collapse when
   the record itself, not the channel, is disrupted." GPT2 §4E: "showing that
   a lookup-based solver fails when its lookup record is corrupted would be
   unsurprising", and the test must separate losing task information, losing
   provenance, and losing a coordination mechanism. The synthesis folds GPT's
   controls into part 6 item 1 as additions, with no sign they were a
   correction of section 8's own proposal.
4. **GPT's second point under "Identity or not at all" is missing.** GPT2
   §4A: "declining philosophical zombies does not establish that this
   particular structure is the relevant one. One can accept organizational
   functionalism while rejecting owner-centred integration as the right
   criterion." Section 8's zombie sentence is the target. Not recorded.
5. **Gemini endorsed section 8's attention schema reading, and the synthesis
   records only the two rejections.** G2 §2D: "Code is right that AST is a
   highly specific, highly accurate fit for the neural network findings in
   Section 3." This cuts in the author's favour, so leaving it out is not
   self-serving, but it means the "Accepted" verdict on the attention schema
   correction was reached with one of three models on the other side, and an
   independent reader would want to know that.
6. **Claude Opus's warning that the data lean toward the book's own collapse
   condition, and that the write-up should say so, is missing.** C1 §1: "You
   should notice that this is your own collapse condition: the centre
   turning out to be one more description ... it points toward the book's
   stated loss, not away from it, and the write-up should say so." C2
   sharpens it: reading 2's self "redone in every act, from the record" is
   "close to the definition of a second-order description" and "may trigger
   the book's own loss condition." Part 1 bullet 4 and part 6 item 1 carry
   the comparator point but not this one, and part 8's write-up bullet does
   not include it.

### 3b. Part 5: what the models got wrong about the record

Checked against the brief's text only (see section 1).

**Gemini.**

- "decoy failures": a record error. Brief line 192: "The tool was not fooled
  by an exact decoy, and a different decoy is untested." The synthesis is
  right.
- "negative readings": not a record error. Brief lines 201 to 202: "Readings
  on words the models never saw in training come out negative, a warning
  about the instrument rather than a finding." Gemini's phrase is the brief's
  own. The synthesis lumps it with "decoy failures" as if both were wrong.
- "a metric that fails at toy scales": loose, not a plain error. The brief
  says the free model returns no verdict, two of three built models read
  flat at development size, and "even the first half of that forecast is now
  in doubt" (lines 204 to 211). Calling that "fails" is Gemini's judgement,
  not a misstatement. The synthesis's correction, "the metric did separate
  the two built models at toy scale", is not in the brief. The brief says
  only that the separate-slot model "reads 0.0000 as built" (lines 185 to
  186) and that the fallback comparison "would show the measure detects
  something, not that it scales" (lines 210 to 211). If the separation is in
  the repository record, the synthesis should point to it; if not, the
  sentence should go.
- "stop at $44": fair. Brief lines 239 to 243 define the first release as
  about $44 and its stop as the free model failing its floor at full size,
  not as a dollar figure. Minor, as the synthesis says.
- One the synthesis missed, borderline: G1 §3 "Experiment C showed the models
  actively route around a built-in 'self' slot, computing it dynamically
  instead." The brief says two of three built arms let their decisiveness
  number fall to about zero, one seed each, at development size, and the
  separate-slot model "still works" (lines 176 to 186). "The models"
  overgeneralises from two of three single-seed runs. I would list it.

**GPT.** I found no record errors, and agree with the synthesis. Points I
checked: the sequence and dates of experiments; "Freezing the gain is a
reasonable repair" against the brief's "fixing that number at its starting
value"; "The margin being within noise"; "the decoy duplicates the same
variable"; "the ordinary model returns no verdict"; "The failed 'you have a
mind' manipulation" against the brief's "lost for two of three models and was
within noise for the third"; "The original position also remains available in
the conversational record." All match the brief.

**Claude Opus.** I found no record errors, and agree with the synthesis.
Figures checked: "about $220 remains" (brief: $450 ceiling, about $230
spent); "about $42 left" (about $44, of which about $2 spent); "$131"; A in
July and B and D in August (brief lines 108, 136, 213); the wager adopted
2026-09-20 (line 47); "one seed at 10M, and the registered runs are at 30M"
(line 186); "up to 94%" (line 196). Two claims are not checkable here and the
synthesis should not call them "right" without saying what they were checked
against: that chapter 1 of the book says the inference is the same with less
evidence (the brief's section 1 does not use that wording; GPT quotes the
same phrase, so it is likely in the book summary, which I did not open); and
that the toy models in B and C "were never trained on human self-description"
(the brief does not say what they were trained on; its "words the models
never saw in training" is consistent with a synthetic task). Neither is an
error on the brief's text.

### 3c. Part 6: what they ask for

The eight items are each supported by the reply named. Item 1's two
separators are Claude Opus's (C1 §3, C2 §3). "Endorsed in substance by GPT"
is fair for the ownership-swap (GPT2 §4E favours "provenance-specific
interventions, matched other-agent controls and rescue"); GPT never mentions
the single-agent setting. Item 3's "verify" step is GPT's alone. Item 4's
"(all three)" is wrong for the specificity half (see 2b).

Requests in the replies that part 6 does not carry, and that an independent
reader would consider important:

1. **GPT: clearing the floor is necessary for reconsidering the second
   release, not sufficient; a fresh decision on causal relevance, calibration
   behaviour and robustness** (GPT1 §4, GPT2 §5). Missing from parts 6 and 8.
   This is the most important omission in the document.
2. **GPT: "Stop presenting the present instrument as a measure of
   experiential depth"; write the work up as causal measurement research**
   (GPT1 §4 and closing). Part 8's write-up bullet quotes the "permission
   slip" half of GPT's closing sentence and drops this half.
3. **GPT: a principled system-boundary criterion** (GPT1 §5D: whether the
   record, the KV cache, external memory and the action-observation loop are
   part of the system; "Copyability is not unreality"). This bears directly
   on the process test, whose intervention is on "the record". Missing from
   parts 2.8 and 6.
4. **GPT: the preferred structure should face evidence outside AI tasks**
   (GPT1 "What would change my mind": preserved in unconscious conditions,
   absent in conscious ones, cross-species). Missing.
5. **Claude Opus: causally coupled self-report as an instrument** (C1 §1, its
   answer to "what is hardest to produce with nobody home", citing Binder
   2024 and Lindsey 2025: "It is not better as a definition. It is better as
   an instrument."). Missing from part 6; the two papers appear in part 7
   only as "on introspection". Section 8's own reading list had named the
   2025 introspection work for a "corroborated-report instrument", so this is
   a model endorsing a section 8 idea, and the synthesis dropped it.
6. **Claude Opus: the book must answer selfless states** (deep meditation,
   ego dissolution) or retreat to minimal for-me-ness (C1 §5 point 5).
   Missing from parts 2.8 and 6.
7. **Claude Opus: the bet has to say which candidate subject it is about**
   (weights, forward pass, persona, conversation) (C1 §2). Missing.
8. **Claude Opus: the write-up should say the data lean toward the book's
   own collapse condition** (C1 §1). Missing (see 3a item 6).
9. **Gemini: the result that would change its mind is the same tests on a
   recurrent architecture** with a persisting, mutating hidden state (Mamba,
   state-space models, RNNs) (G1 §5). Missing. It is Gemini's one concrete
   redesign direction beyond the frontier pilot.
10. Claude Opus: if the free model fails its floor, "treat 'no stored
    ownership at the point of action, at either scale' as a result" (C1 §4).
    Minor; missing.

### 3d. Disagreements among the models that part 3 omits

- Gemini endorses section 8's attention schema reading (G2 §2D); GPT and
  Claude Opus reject it (GPT2 §4C, C2 point 1).
- Gemini keeps "mural" and "nobody is home" (G2 §1); GPT and Claude Opus
  delete them (GPT2 closing, C2).
- Gemini makes noun-versus-verb the structural flaw (G1 §3, G2 §1); GPT says
  it is not a clean experimental distinction (GPT2 §1).

The synthesis's own rule, in its header, is to treat the disagreements as
"the informative part". These three are missing from the part that lists
them.

## 4. Summary for John

**Does the synthesis hold?** On the quotations, yes: every phrase in quotation
marks attributed to a model is in that model's reply, apart from one spelling
change inside quote marks ("spatialises" for Gemini's "spatializes") and one
paraphrase in quote marks ("Evidence must bypass the training objective",
which nobody wrote). The round-one cut-off for Claude Opus is as described.
The figures the synthesis says Claude Opus got right are right.

**What must be corrected.**

1. The money. Parts 1, 4 and 8 say the models' money recommendation matches
   section 8 and that section 8 "holds its ground". GPT twice says that
   clearing the floor must not release the $131 by itself, and that the first
   release should stop early if the repaired controls fail; Claude Opus says
   the repair "comes close to circular". These are corrections to section 8,
   not confirmations of it, and the first is missing from the document
   altogether.
2. The router-control point is endorsed by GPT only "for the reported
   pattern", not in general. Part 4 should say so.
3. Four "all three" or "agreed" claims are two of three: the chapter 1
   sentence (Gemini never names it); experiment C (Gemini reads it the other
   way); experiment D (Gemini never mentions it); and deleting "mural" and
   "nobody is home" (Gemini keeps both). The "report the specificity controls
   as the positive result (all three)" in part 6 is Claude Opus plus GPT in
   substance.
4. Three attributions are wrong: the resource-bounded grounding is Claude
   Opus's, not GPT's (GPT offers a non-identity dependence law instead); "noun
   versus verb is not an experimental distinction" is GPT's, not Claude
   Opus's; "a response is many forward passes" is GPT's, not Claude Opus's.
5. Part 4 should add GPT's criticism of section 8's experiment B follow-up,
   GPT's zombie point, and Gemini's endorsement of the attention schema
   reading.
6. Part 5 should stop counting "negative readings" as a Gemini error (it is
   the brief's own phrase), and either source or drop "the metric did
   separate the two built models at toy scale", which is not in the brief.
7. Part 6 should add the ten missing requests listed in 3c, above all GPT's
   pass-is-not-sufficient condition, GPT's "stop presenting the instrument as
   a measure of experiential depth", Claude Opus's coupled self-report
   instrument, and Gemini's recurrent-architecture test.
8. Part 3 should add the three disagreements in 3d.
9. The two quotation fixes in 2a.

**What was softened.** The pattern is consistent: where a model agreed with
section 8, the synthesis records the agreement in full; where a model agreed
with a condition attached, the condition is moved to the "what they ask for"
list or dropped, and the agreement is reported as plain. This is clearest on
the money and the router control, which are the two points on which the
synthesis says the author "holds ground". The author's own part 4 caveat,
that the note "is owed a check by a session that did not write section 8",
was the right instinct; this is that check.
