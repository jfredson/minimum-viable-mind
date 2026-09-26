# Amendment A3 closure text, version 5 (DRAFT for the Gate A tier 1 closure check)

*2026-09-25 (Pacific). Amendment A3 is the third registered design change to
the first constructed self-index experiment
(`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`); its "closure
text" is the dated block that closes it out, appended to that file once the
review before registration (Gate A) is done. Version 5 is version 4
(`docs/a3-closure-text-draft-2026-09-21-v4.md`, left on disk unedited, as are
versions 1 to 3) with the outside review's findings applied exactly as John
ruled them on 2026-09-25
(`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`, items 1, 2, 5 to
9, 11, 12 and 14 to 19). The outside review ("tier 2") was two models from other
labs reading version 4 by hand: Gemini 3.1 Pro
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-gemini.md`)
and ChatGPT 6 Astra Medium
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-chatgpt.md`).
Neither filed a fatal finding. Where the ruling adopts a reviewer's
replacement wording, that wording is used as the reviewer wrote it, with a
citation or a plain-language gloss added and nothing else changed; every such
place is listed, item by item, in the section after the block.*

*Written by a Claude Code session that did not draft the dispositions, as item
22 of the ruling requires. That session did not verify its own changes. The
closure rule gives that to a tier 1 reviewer who is not the writer of this
version (`docs/outside-review-protocol.md`, "The closure rule"), and item 22 of
the ruling makes that check the next step.*

*The dated note of 2026-09-22 that sat beside version 4's money paragraph is not
carried into this version: item 8 of the ruling puts the ledger's corrected
figures into the block itself, so the note has nothing left to correct. It stays
where it was, beside version 4.*

*This is registered text once it lands in
`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` as a dated
closure block. It has not landed. The tier 1 reviewer-owned check that item 22
of the ruling requires has been run and filed
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-closure-v5-tier1-check-claude-worktree.md`,
commit `99b8b64`, pull request 45). It found one serious finding (RT-204) and
six minor ones (RT-205 to RT-210). John ruled on them on 2026-09-25, and this
version was revised the same day to apply those rulings; the revisions are the
last rows of the change table after the block. Those revisions are binding text
written by this version's writer, so they wait on a re-check by a different
session. Nothing is appended until that re-check is filed. The session that appends it re-reads the compute ledger that day, as
item 8 of the ruling asks, and changes the money paragraph only if a row has
been added since.*

---

## Closure of Amendment A3, [date of the Gate A pass]

*The date above is a placeholder and is filled with the date of the commit
that appends this block to `amendment-a3.md`. It cannot be written before
that commit exists, so it is still open here.*

**Outcome: not testable — the registered comparison was undefined for every
possible model. Separately, removing the ownership-input channel reduced
primary-battery accuracy on all three trained seeds.** This is the loss
condition's sense of the phrase, not the validity-gate bin of the same name —
the bin for an ablation that damages the model so broadly that no reading of it
can be trusted. The validity-gate bin was not evaluated: its gates were
unimplemented and unapplied. No code for them was written for this design, and
they were never applied to the input-channel lesion, the only lesion A3 ran, on
any seed (the independent review of 2026-09-19 searched the source and the
three endpoint records and found neither — `red-team-a4.md`, its seventeenth
finding, labelled there F17).

The pre-registered loss condition fired: *no non-self cross-turn control
can be built that is state-requiring at ceiling — then the differential
discriminator is dead here and the honest report is "not testable"*
(`pre-registration.md`, under "Loss conditions"). The control battery's
ownership-blind ceiling was measured at 1.0
(`ceiling-measurement-findings.md`, 2026-09-17), so the registered
differential clause had no computable value for any model from the day it
was registered. The same measurement shows why this is structural rather than a
defect of this control alone: the ceiling-corrected metric is incompatible by
construction with any control fully determined by the visible episode and not
requiring ownership, because every such control has an ownership-blind ceiling
of 1.0. The number the registration recorded as that ceiling had not been
attacked before registration, which is registered separately as a defect in the
instrument (`ceiling-defect-2026-09-17.md`). An unregistered pilot giving the
control its own loss term, per-row gradient weight quadrupled, did not make it
usable — 0.3125 against a bar of 0.60 that was pre-stated before the code
existed (`control-learnability-pilot-findings.md`). The clause is not repaired;
a successor grammar is a new registration. A successor must demonstrate both its
control ceiling and a usable comparison metric; measuring the ceiling alone does
not resolve this defect.

**What A3 measured.** On three seeds trained from scratch, the primary
battery learned (intact 0.5683, 0.5633, 0.5738) and collapsed when the
ownership input channel was zeroed (0.1988, 0.2015, 0.1447), while the
syntax battery was unchanged. The state drop was 0.0769 on seed 2, versus
0.0018 and 0.0002 on the other seeds; all were below the locked 0.1172
threshold. The six primary-battery scores are means across six evaluation
seeds, paired within seed, and every figure in this paragraph is recorded at
`seeds-endpoint-findings.md`. The ownership input is load-bearing **for the
primary battery**. The matched contrast against a non-self control could not be
run.

**What A3 did not measure.** Whether the network built an internal
structure around the ownership input — a center in the sense of something
the network acquired — is not testable with these instruments. The section
of the amendment that defines what is ablated (§3.1) says why: the
input-channel lesion removes a sense organ, not a structure the network
built. The registration concedes a second limit alongside it: attending
back to marked positions is a re-readable pointer rather than a carried
binding, both routes need the channel, and so the wire lesion cannot
separate them (`amendment-a3.md`, the file this block lands in, registration
revision 8 of 2026-09-15, "The central claim is narrowed").
The instrument the registration names as the discriminator for that
question, the mid-episode re-indexing probe, has never run (the red team
ledger's finding `RT-114`, which lists it among the registered discriminators
that have never fired).

Four localization runs bear on where ownership sits, and none of them
localizes it. A fitted linear classifier at eleven positions and five
layers found the register index — the four-way rank of the marker, not the
registered target itself — nowhere except where its marker is the input
(`fitted-position-sweep-findings.md`, with its sensitivity corrected at
`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`). A standardised
refit, a different estimator on the same states, was run next
(`standardised-refit-findings.md`). The second estimator produced one nominal
crossing; its folds and permutation draws also differed, so the change cannot be
attributed to scaling alone. (The folds are the way the episodes were split
between fitting and testing; the permutation draws are the shuffled-label runs
the bar is built from. That both differed is shown from the refit's code and its
three committed output files, not from its findings file, in the check of
2026-09-25, `reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`,
section 3.) The crossing sits at the third checkpoint, at the **other** agent's
revision value, at layer 3. It is an accuracy margin of 0.000484, equivalent to
1.94 of 4,000 episodes — a margin computed in the review of that run and not
stated in its findings file (`red_team_ledger.md`, finding `RT-128`, which ruled
that the number and its fragility travel together or neither travels) — and is
recorded as a sub-bar pattern measured twice, not a clearance. The registered
matched control (§L2(a), the other-agent index) had its **probe half** run for
the first time, with rank matched by design and accuracy matched as observed;
it excluded the exclusion confound in the form proposed, a four-way rank of the
other agent that this probe could decode (`other-index-position-sweep-findings.md`).
A purely relational encoding remains open as a route that would produce both the
pattern and this null (the red team ledger's finding `RT-125`, carried open).
The control's **lesion half** — a localized other-agent subspace whose
ablation leaves the self-directed condition intact — remains unavailable,
because no such subspace was found and there is nothing to ablate; running
the probe half does not discharge the registered requirement. All the
rulings in this paragraph are the Gate B rulings of 2026-09-21 on the two
follow-up runs (ledger RT-120 to RT-142).

The registered probe target, the model's own marker word, has been read at
these positions only by the weaker difference-of-averages method. The
difference-of-averages sweep found no discovery-position clearance for either
target: 135 tests read the registered marker-word target and 135 read the
register index. Positive-control detections occurred where the answer was
supplied by the input token (`powered-position-sweep-findings.md`). (That file
states 270 tests across the two targets; the 135 per target is derived from it,
as nine testable positions × five layers × three checkpoints, the arithmetic
`powered-position-sweep-method.md` sets out.) (The
discovery positions are the positions under test; the positive controls are
the positions where the answer is the input token, which any working read should
find.) Reading the registered target with a sensitive instrument is one unrun
job of about seventy processor-hours at no money cost (both the price and the
fact that the job was dropped before that run rather than after it are recorded
in the red team ledger's finding `RT-89`), and until it runs, only the narrower
sentence above is available. Causal patching — copying internal activity from
one run into another to test whether it causes the behaviour — which the
section on how the ablation is localized (§3.2) requires alongside the probe
before anything counts as localized or as absent, was never run and has no code
for this design (the ruling of 2026-09-20 that patching is new code rather than
existing machinery, ledger RT-96). Because causal patching was never run,
agreement between probe and patching could not be tested and no L1 subspace
(§3.1's name for the located region of the network's internal activity that
carries which marker is its own) was ever localized; so the registered
uncarvable signature H_diffuse was never reachable either: it requires a carved
subspace to compare against the matched controls, and none was carved.

**Hard kill K5 is not reached.** A hard kill is a registered stop condition
with a named consequence. K5 (`amendment-a3.md`, §4.2, its list of hard kill criteria: "Probe-patching
convergence fails on all three seeds: *not testable (localization)*, reported
as such; no further seeds") tests whether two instruments agree. Causal
patching was never built for this design (ruling of 2026-09-20, ledger RT-96),
so the test was never run, and this closure does not report a measured K5
failure. The term *not testable (localization)* rests instead on §3.2's
convergence requirement, that nothing counts as localized until probe and
patching agree, and A3 closes under the pre-registration's loss condition
above, with no further A3 seeds. This reading of the registered kill list is
John's, ruled on 2026-09-25
(`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`, item 1).

**The registered term for the line is therefore *not testable
(localization)*, and the registered reading of this null is instrument
failure, not absence.** The registration reads "ownership is known to be
load-bearing and the instruments cannot find it" as a failure of the
instruments until causal patching has run, and that reading stands. What
can be said descriptively, and separately from it, is limited to each read
above and its own target. The fitted register-index read had a heuristic
reach of approximately one episode in eleven, calculated using its
positive-control accuracy. This is not measured detection power at the
discovery positions and does not establish the sensitivity of the unrun
fitted marker-word read
(`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`, which John ruled
on 2026-09-20 must be cited wherever that figure is used). What may not be
said is that the structure is absent, or that these nulls make it less
likely, because every number in these runs is conditional on this stack being
able to recover such a structure. Ownership-channel dependence was established;
recovery of an acquired internal representation by this stack was not.
John ruled the 2026-09-16 blind arm (the registered blind-localization run,
meant to show the instruments can find something known to be there)
discharged, so it does not block this closure. That disposition does not
establish successful recovery of an acquired ownership representation on the
A3 design. The unmet sensitivity requirement carries into the successor's
rehearsal (`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`,
reconciling the December-result ruling's item 3 with the step 4 ruling).

**Where this sits on the project's gradient.** Under the ruling of
2026-09-20 that a load-bearing self-index is a center
(`docs/rulings/2026-09-20-center-as-degree.md`), "center" has a second and
weaker sense than the one used above: a pointer that is causally
load-bearing for the act is a center at the bottom of the gradient, with no
requirement that the network built a structure to hold it. In that weaker
sense — and only in it — what the lesion measured puts these checkpoints
above zero. "Above zero" is the project's classification under its 2026-09-20
definition of a load-bearing input, not a measured integration score. A3 does
not establish that binding specifies its center in the same act, and it
provides no licensed verdict about consciousness or experience. (The first of
those two limits is the one `pre-registration.md` requires every write-up to
state, under "Scope: this is Q5, not the removal test".) Their degree on the
integration axis, how much of the act is organized around the ownership
signal rather than consulting it, is unmeasured, because the metric for that
axis (Stage 2) does not yet exist. The sentence this experiment supports in
public is: Removing the ownership-input channel reduced primary-battery
accuracy on three trained seeds. The matched comparison was unavailable;
whether an acquired internal ownership structure exists was not established,
and integration degree was not measured. The above-zero classification may
follow it only when expressly attributed to the ruling of 2026-09-20. No
result of A3 is described as "a structural signature of self-indexing" or
"a structural signature of ownership-specific learning".

**Successor.** A matched-role causal-interchange experiment with a
learn-both eligibility gate, whose purpose is to develop and validate the
Stage 2 degree metric on contrast cases known by construction. The name
"matched-role causal-interchange" is the one item 5 of
`docs/rulings/2026-09-20-center-as-degree.md` gives the successor; "learn-both"
is the name `docs/rulings/2026-09-23-range-and-direction-only.md` uses for the
eligibility check; the contrast cases are set out in
`docs/competing-mechanisms-2026-09-20.md`. It registers in 2026
(`docs/rulings/2026-09-20-december-result-roadmap.md`, item 1, which amends
item 5 of `docs/rulings/2026-09-20-center-as-degree.md`). The successor
proceeds through Gate A with both tiers as soon as its prerequisites are
complete. The operative deadlines remain registration by 2026-10-18 and
launch of the registered runs by 2026-11-01; missing either is recorded as a
schedule failure (`docs/rulings/2026-09-20-december-result-roadmap.md`,
including its 2026-09-21 annotation). Since item 23 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, a missed
date no longer moves the roadmap to outcome R4 (hibernating with a registered
design and a rehearsal) by itself, and launching past one takes a fresh ruling
naming what comes off the back end; the second date binds the launch of the
remaining eight registered runs, not the single free-arm run before them. Three
things the successor inherits and must carry: measuring the control's
ceiling properly is a precondition of any successor amendment (John,
2026-09-17, `ceiling-defect-2026-09-17.md`); nothing counts as localized or
as absent until both instruments, probe and causal patching, agree; and the
successor's whole purpose is a measurement that does not yet exist, so the
rehearsal requirement — that a full measurement procedure be demonstrated
before it is registered (`docs/outside-review-protocol.md`, its section on
the measurement rehearsal required before any Gate A) — applies to it even
though it does not apply to this closure.

**Open items carried on this closure.** The instrument-sensitivity
requirement the blind arm served, carried into the successor's rehearsal
(the arm itself is discharged, above). The registered
probe target, the marker word, unread by a sensitive instrument at these
positions — deferred because reading it was priced at about seventy
processor-hours against about eleven for the register-index read done in its
place, and dropped before that run rather than because of anything the run
found (the red team ledger's finding `RT-89`); whether it runs before the
paper draft is one of the questions the ruling of 2026-09-20 on centers as a
matter of degree expressly leaves undecided
(`docs/rulings/2026-09-20-center-as-degree.md`, "What this ruling does not
decide"). Causal patching, unwritten and unrun. The mid-episode re-indexing
probe, the registered discriminator for pointer against carried binding,
unrun. The lesion half of the registered other-agent control, unavailable.
The relational-encoding route at the other agent's revision value, untested.

Patching is not scheduled for A3; the December-result ruling assigns its
construction to the successor (`docs/rulings/2026-09-20-december-result-roadmap.md`,
item 2). No further investigation of the other-agent revision-value position is
authorised under the follow-up ruling
(`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, item 3). The
marker-word fitted read remains deferred, and whether it runs before the paper
remains undecided. These limitations do not imply that the missing measurements
have been satisfied.

**Money.** As of the compute ledger's 2026-09-21 row (the measurement
rehearsal's rented slice), about $46.2 was counted against Amendment A3's $100
stop and about $227.6 had been spent across the programme, including $1.904
spent on the two follow-up machines of 2026-09-20 that the instrument's own
reproducibility check refused (`compute-ledger.md`). The programme ceiling
those figures count against was raised from $400 to $450 on 2026-09-25
(`docs/rulings/2026-09-26-weekend-1-queue.md`, page 6). The ledger was re-read
on 2026-09-25 and carries no row after 2026-09-21.

---

## Changes from version 4, item by item (not part of the closure block)

Each line names the ruling item (`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`),
the reviewer finding it answers, and what changed. "Verbatim" means the
reviewer's replacement wording is used unchanged; any gloss or citation added
beside it is named.

| Ruling item | Reviewer finding | What changed |
|---|---|---|
| 1 | Gemini G5, ChatGPT A7 | New paragraph "Hard kill K5 is not reached", in the ruling's words: K5 tests whether two instruments agree; patching was never built (RT-96), so the test was never run; *not testable (localization)* rests on §3.2's convergence requirement; A3 closes under the loss condition with no further A3 seeds; stated as John's interpretation. The annotation beside RT-164 in the red team ledger is drafted separately, not made here. |
| 2 | Gemini G4, G6 | "Because the two instruments never converged on any seed" replaced with Gemini's G6 rewrite, in the ruling's words ("agreement between probe and patching could not be tested"). Gloss added for "L1 subspace". Gloss also added for "causal patching" ("copying internal activity from one run into another to test whether it causes the behaviour") in the version 4 sentence before it, which item 2 did not replace (declared after the tier 1 check; see the RT-208 row below). |
| 5 | Gemini G3 | "never applied to any lesion" becomes "never applied to the input-channel lesion, the only lesion A3 ran, on any seed". |
| 6 | ChatGPT A1 | "at quadrupled weight" becomes "per-row gradient weight quadrupled". |
| 7 | ChatGPT A2 | The 270-test sentence replaced with ChatGPT's replacement, verbatim. Gloss added for "discovery positions" and "positive controls". |
| 8 | ChatGPT A3 | Money paragraph rewritten to the ruling's figures: about $46.2 of $100 and about $227.6, as of the ledger's 2026-09-21 row, against a ceiling raised from $400 to $450 on 2026-09-25. The $1.904 is ChatGPT's A3 wording. Ledger re-read on 2026-09-25. |
| 9 | ChatGPT A4 | The 2026-10-11 target is dropped. ChatGPT's replacement, verbatim, for the schedule sentence. The ruling's item 1 citation is kept for "registers in 2026". |
| 11 | ChatGPT A6 (main point) | The restriction "any control fully determined by the visible episode and not requiring ownership" restored to the structural sentence. ChatGPT's successor sentence added, verbatim. Sub-point declined, so no change for it. |
| 12 | ChatGPT A8 | "excluded the exclusion confound that had been proposed for that pattern" becomes "excluded the exclusion confound in the form proposed, a four-way rank of the other agent that this probe could decode", followed by the existing relational-route sentence, now citing RT-125. |
| 14 | ChatGPT A10 | The blind-arm sentences replaced with ChatGPT's replacement, verbatim, keeping version 4's ruling citation. Gloss added for "blind arm". |
| 15 | ChatGPT A11 | ChatGPT's paragraph added, verbatim, after the open items, with the two rulings cited by item. |
| 16 | ChatGPT A12 | Headline replaced with ChatGPT's, verbatim. |
| 17 | ChatGPT A13 | ChatGPT's two sentences added to the gradient paragraph, verbatim; its public sentence used, verbatim; the pre-registration's "every write-up" requirement cited by section; its note that the classification may follow only when attributed to the ruling carried as a sentence. |
| 18 | ChatGPT A14 | The one-in-eleven sentence replaced with ChatGPT's, verbatim, scoped to the fitted register-index read; the required citation of the correction file kept. The lead-in "these probes did not localize this target" is replaced by "limited to each read above and its own target". |
| 19(a) | ChatGPT A15 | "That bin did not fire, and it was also never tested" becomes "The validity-gate bin was not evaluated: its gates were unimplemented and unapplied." |
| 19(b) | ChatGPT A15 | "was itself never attacked" becomes "had not been attacked before registration", with no claim about what the later measurement invalidated. |
| 19(c) | ChatGPT A15 | The state battery's drops given as ChatGPT wrote them: 0.0769 on seed 2 versus 0.0018 and 0.0002, all below 0.1172. "All six scores" becomes "The six primary-battery scores", since the paragraph now also gives three state-battery figures. |
| 19(d) | ChatGPT A15 | "1.94 episodes in four thousand" becomes "an accuracy margin of 0.000484, equivalent to 1.94 of 4,000 episodes", citing `red_team_ledger.md` beside RT-128. |
| 19(e) | ChatGPT A15 | "found the same thing everywhere but one cell" replaced with ChatGPT's sentence, verbatim. Cited to the dispositions check of 2026-09-25, section 3, not to `standardised-refit-findings.md`, as the ruling requires. Glosses added for "folds" and "permutation draws". |
| 19(f) | ChatGPT A15 | "a center that is known to be there" replaced; ChatGPT's sentence added, verbatim. |

### Revisions after the tier 1 check (2026-09-25)

These rows apply John's rulings of 2026-09-25 on the tier 1 reviewer-owned check
of this version at commit `432e966`
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-closure-v5-tier1-check-claude-worktree.md`,
commit `99b8b64`, pull request 45; "section 3" below is that file's findings
section). The rulings were given in the session that asked for these revisions
and are not yet in a committed ruling file. They were written by this version's
writer and are owed a re-check by a different session.

| Check finding | Severity as filed | John's ruling, 2026-09-25 | What changed |
|---|---|---|---|
| RT-204 (section 3) | serious | Accepted; closed by the clause the check proposes | In the successor paragraph, after the citation of the December-result ruling's 2026-09-21 annotation, the check's proposed clause is added: since item 23 of `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, a missed date no longer moves the roadmap to outcome R4 by itself, and launching past one takes a fresh ruling naming what comes off the back end; the second date binds the launch of the remaining eight registered runs, not the single free-arm run before them. Gloss added for R4 ("hibernating with a registered design and a rehearsal"), from item 23's own words. |
| RT-205 (section 3) | minor | Accepted: state 135 as derived from the cited 270 | ChatGPT's two sentences are unchanged. A parenthesis after the citation says the findings file states 270 across the two targets and that 135 per target is derived, as nine testable positions × five layers × three checkpoints, citing `powered-position-sweep-method.md`. |
| RT-207 (section 3) | minor | Accepted: fix the gloss's section | "§3.2's name" becomes "§3.1's name" in the gloss on "L1 subspace". Section 3.1 of `amendment-a3.md` defines L1; section 3.2 says how it is localized. |
| RT-208 (section 3) | minor | Accepted: declare the undeclared gloss | No change to the block. The "causal patching" gloss is now declared in the item 2 row above. |
| RT-209 (section 3) | minor | Accepted: the removal of the "$0 side item" clause stays as recorded | No change. Version 4's clause that a blind-arm re-run would be a $0 side item stays out of the block, as item 14's replacement left it. The fact is still in the December-result ruling's item 3 and in `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, both cited in the block. |
| RT-210 (section 3) | minor | Accepted: correct the inherited phrase's citation | The successor's description, unchanged from version 4, cited only `docs/competing-mechanisms-2026-09-20.md`, which does not contain "causal-interchange" or "learn-both". It now cites item 5 of `docs/rulings/2026-09-20-center-as-degree.md` for the name, `docs/rulings/2026-09-23-range-and-direction-only.md` for "learn-both", and keeps the competing-mechanisms document for the contrast cases. |

RT-206 (minor, section 3: the $450 ceiling is not yet in the compute ledger) was
not part of the rulings passed to this session, and the check says itself that
it is not a defect in this text. It is a note for the ledger, and nothing here
changes for it.

Not applied here, because the ruling gives them no text change: items 3, 4,
10 and 13 (credit or records), item 20 (an annotation beside the ChatGPT
review file, drafted separately), item 21 (finding numbers from RT-204, which
this version does not assign) and item 22 (the process this version follows).
Not applied because the ruling did not adopt it: ChatGPT's suggestion under
A15 that the refit paragraph also give the two reasons the crossing is reported
as sub-bar.
