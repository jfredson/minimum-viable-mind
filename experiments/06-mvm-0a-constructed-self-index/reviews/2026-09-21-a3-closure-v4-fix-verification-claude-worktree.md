# Verification of the fixes to the Amendment A3 closure text, version 4

*Filed 2026-09-21 (Pacific) by a Claude Code session in its own worktree
(`worktree-agent-ac91e682df92a2357`). This is the reviewer-owned verification
required by the amended outside-review protocol (`docs/outside-review-protocol.md`,
the closure rule, as amended by the commit `93c9cb2` that carries the three changes
John ruled on 2026-09-20). This session did not write version 3, version 4, the
findings, or the fixes it is checking.*

*What I read.* The fixes on the branch `worktree-agent-a9915df1f2edb2233` — three
commits (`4b4ec99`, matching the site's spend figures to the ledger; `bf79ed2`,
fixing citations and unrecorded claims; `41d44ea`, citing the correction note for
the reach figure) on top of `8ebf9f3`. The amended protocol I verify under. The
independent closure check I verify against, on the branch
`worktree-agent-aaccf55dd43fe5aab`
(`reviews/2026-09-21-a3-closure-v4-closure-check-claude-worktree.md`).

*What I did not do.* I edited no closure text, no ledger, no registered file and no
project data. I ran no compute and spent no money. I pushed nothing, merged nothing
and opened no pull request. Nothing below is committed outside my own worktree branch.

*Lookup: none. No web search. Every check is run against files committed in this
repository.*

*The two words, kept apart.* **Checked** means I ran a command against the committed
record and the output is printed below. **Accepted** means no decisive command exists
and the judgement rests on reading committed texts against each other, which is said
where it happens. I treated every claim in the fixes and in the findings as a claim
to test, including the findings' own measurements.

*One correction to the brief I was given.* It said the amended protocol was ruled but
not yet merged. It is now on the main line: `git merge-base --is-ancestor 93c9cb2 main`
returns yes, through the merge commit `c63d960` (pull request 13). The rule I verify
under is therefore live on main, not only on a branch.

---

## Verdict in one table

| what was fixed | verdict |
|---|---|
| 1. The successor's schedule cited the wrong item of the December-result ruling | **CLOSED** (checked) |
| 2. "The validity gates were clean" — a claim the record contradicts | **CLOSED in substance** (checked) — but the fix's own stated measurement does not reproduce, and one added clause reaches past its source. See below. |
| 3. The figure of 1.94 episodes in four thousand cited a file that lacks it | **CLOSED** (checked), one residual |
| 4. Two "never run" claims carried no record | **CLOSED** (checked) |
| 5. The deferred marker-word read was carried without a reason | **CLOSED** (checked) |
| 6. "Registration revision 8" named no file | **CLOSED** (checked) |
| 7. The compute ledger credited the wrong finding | **CLOSED** (checked); the edit was appropriate |
| 8. The reach figure of one legible episode in eleven cited nothing | **CLOSED** (checked) |
| 9. The project data's spend figures disagreed with the ledger | **CLOSED** (checked), one small residual |
| 10. Sweep: did the fixes break anything or leave anything newly uncited | **Nothing broken** (checked). One pre-existing gap is still open. |

**Nine of the ten items close on measurement.** The tenth, the validity-gate
sentence, closes in substance — the sentence that now stands is true and is a large
improvement on the one it replaces — but two things about it should go on the record
before a registration commit, and they are in item 2.

---

## 1. The successor's schedule now cites the item that carries the facts

**What the fix claims.** The sentence cited item 7 of
`docs/rulings/2026-09-20-december-result-roadmap.md` for facts that live in item 1.
It now cites item 1 for all four facts, and notes that item 7 restates the
2026-10-18 date and adds the 2026-11-01 one.

**Check run.**

    sed -n '/^1\. \*\*The successor registers now/,/^2\. /p' \
      docs/rulings/2026-09-20-december-result-roadmap.md
    sed -n '/^7\. \*\*/,/^8\. /p' \
      docs/rulings/2026-09-20-december-result-roadmap.md

**Output.**

    1. **The successor registers now.** Item 5 of
       `docs/rulings/2026-09-20-center-as-degree.md` ("registered after the
       hibernation condition") is amended: the matched-role causal-interchange
       experiment is registered in 2026, through Gate A with both tiers.
       Registration commit target 2026-10-11; kill date 2026-10-18.

    7. **The two kill dates are accepted**: registration committed by 2026-10-18;
       registered runs launched by 2026-11-01. Missing either drops the roadmap to
       R4 (a schedule failure, named as such in STATUS.md).

**Does the output match the claim?** Yes, on every part. Item 1 carries all four
facts the sentence states — that the successor registers in 2026, that it goes
through Gate A with both tiers, the 2026-10-11 registration commit target, and the
2026-10-18 kill date — and item 1 is also the item that amends item 5 of the
centers-as-degree ruling, which is the other thing the sentence attributes to it.
Item 7 restates 2026-10-18 and adds 2026-11-01 for the launch of registered runs,
with either date missed recorded as a schedule failure, exactly as the new
parenthesis says.

A checker who now opens the named file and finds the named item lands on a paragraph
containing what the sentence promises. That is the whole point of the finding this
closes.

**Verdict: CLOSED, checked.**

---

## 2. The validity-gate sentence

This is the one that needed the most care, and it is the one with something to report.

**What the old sentence said.** "This is the loss condition's sense of the phrase,
not the validity-gate bin of the same name: the validity gates were clean and no
instrument breached them."

**What stands now.**

> This is the loss condition's sense of the phrase, not the validity-gate bin of the
> same name — the bin for an ablation that damages the model so broadly that no
> reading of it can be trusted. That bin did not fire, and it was also never tested:
> those gates have no code written for this design and were never applied to any
> lesion on any seed (the independent review of 2026-09-19 searched the source and
> the three endpoint records and found neither — `red-team-a4.md`, its seventeenth
> finding, labelled there F17), and the subspace ablation they were written to guard
> never ran, because no subspace was ever localized.

### 2a. The measurement the fix says it ran does not reproduce

The fix session reports reproducing the record by checking that
`a3-gates/endpoint_a3_30m_seed1.json` has 110 keys and that none of them matches
nll, degen, rep, ood, gate or valid. I ran that check.

**Check run.**

    python3 -c "
    import json,re
    d=json.load(open('endpoint_a3_30m_seed1.json'))
    ks=list(d.keys())
    print('KEY COUNT:', len(ks))
    pat=re.compile(r'nll|degen|rep|ood|gate|valid', re.I)
    print('MATCHING KEYS:', [k for k in ks if pat.search(k)])
    print('KEYS:', ks)
    "

**Output.**

    KEY COUNT: 15
    MATCHING KEYS: []
    KEYS: ['read', 'checkpoint', 'checkpoint_md5', 'checkpoint_step', 'tokens',
           'lock', 'theta_primary', 'theta_all', 'eval_n', 'metric',
           'ceilings_used', 'default_seed', 'across_seeds', 'across_seeds_note',
           'per_seed']

The file has 15 keys, not 110. Because "110 keys" might have meant something other
than top-level keys, I counted it every way I could construct.

**Check run.** A recursive walk counting, for the same file, the top-level keys, every
key path in the nested structure, the distinct key names, and the leaf values.

**Output.**

    endpoint_a3_30m_seed1.json -> top=15 flatpaths=206 names=29 leaves=165 matches=[]
    endpoint_a3_30m_seed2.json -> top=15 flatpaths=206 names=29 leaves=165 matches=[]
    endpoint_a3ctl_30m_seed0.json -> top=15 flatpaths=206 names=29 leaves=165 matches=[]
    endpoint_validation_pilot.json -> top=15 flatpaths=206 names=29 leaves=165 matches=[]
    pilot_endpoint.json -> top=7 distinct=17 matches=[]

No reading gives 110. I then swept every record in the gate directory for any of
those three counts equal to 110 and found none. I also checked the file's history, in
case it had been larger when the finding was written.

**Check run.**

    git log --oneline --all -- \
      experiments/06-mvm-0a-constructed-self-index/a3-gates/endpoint_a3_30m_seed1.json
    git show 5f176a5:...endpoint_a3_30m_seed1.json | (the same recursive count)

**Output.**

    5f176a5 Seeds 1 and 2 endpoint: learnability replicates, the control fails on all three
    AT ORIGINAL COMMIT: top=15 flatpaths=206 names=29

The file has had exactly one committed version and has never had 110 keys under any
counting.

**Where the number comes from.** Not from the fix session's invention. It is in the
finding itself: the red team pass of 2026-09-19 (`red-team-a4.md`, its seventeenth
finding, labelled there F17) says "The endpoint records for seeds 0 to 2 carry no
such field among their 110 keys", and that finding is labelled **MEASURED**. So a
finding labelled measured carries a number that does not reproduce, and a later
session reported reproducing it.

**Does the output match the claim? Partly.** The load-bearing half — that no key in
any endpoint record has anything to do with the validity gates — reproduces
decisively, on all five records, under every counting. The count does not reproduce
at all.

**What saves this.** The wrong number is **not** in the registered text. I checked:

    grep -n "110" (the fixed closure text)   ->  no output

The closure text says only that the review "searched the source and the three
endpoint records and found neither", which is true. So the error is confined to the
fix session's account of its own check, and does not travel into the text that would
be registered. Under the amended rule, though, the reviewer's job is to say when a
stated measurement does not come out as stated, and this one does not.

### 2b. The substance of the replacement, checked independently

I did not rely on the finding, since the finding is itself a claim.

**Check run.** Search this design's own source folder for the three gate instruments
that section 3.3 of `amendment-a3.md` names — the neutral-episode likelihood bound,
the long-generation degeneracy probe, and the out-of-distribution branch.

    grep -rn -i -E "neutral.episode|degeneracy|out.of.distribution|\bood\b|validity gate" src/
    grep -rn -i "neutral" src/
    grep -rn -i "long.generation|long_gen" src/

**Output.** No neutral-episode likelihood bound and no long-generation degeneracy
probe anywhere in `src/`. The single "neutral" hit is unrelated
(`curriculum.py` line 133, on forced revisions being agent- and position-neutral).
No long-generation hit at all. Every "degeneracy" hit is a zero-spread guard or a
probe precondition inside the control diagnostic, the blind control, the position
sweeps and the known-answer test — none of them the Δrep-4 probe section 3.3
carries over.

So the first clause of the replacement — that the gates have no code written for
this design — is true, and I established it without the finding.

**Check run.** The requirement the gates were carried over from, and the standing
note in the separation-clause requirements.

    sed -n '/^### 3.3/,/^### 3.4/p' amendment-a3.md
    sed -n '211,220p' separation-clause-requirements.md

**Output.** Section 3.3 reads "Neutral-episode ΔNLL under a null-calibrated bound
..., the long-generation degeneracy probe (Δrep-4), and the OOD-inconclusive branch
for any ablation that breaches them." The separation-clause requirements, at their
fifth item under H (labelled there H5, and drawn from the same seventeenth finding),
read: "The neutral-episode likelihood bound and the long-generation degeneracy probe
have no A3 implementation and have never been applied to the input-channel lesion on
any seed."

**Does the output match the claim?** For the first two clauses, yes, and the fix's
phrasing is if anything stronger than its sources in the honest direction: where the
sources say the gates were never applied to the input-channel lesion, the closure
text says they were never applied to **any** lesion on **any** seed, which is true
because the input-channel lesion is the only lesion that ever ran.

### 2c. Where the replacement reaches past its source

The trailing clause — "and the subspace ablation they were written to guard never
ran, because no subspace was ever localized" — is the one I would not let through as
written.

The facts in it are true. No subspace ablation ran, and no subspace was localized.
But the clause supplies a **reason** that the finding it cites does not support and
that the finding's own argument runs against. The seventeenth finding's complaint is
precisely that the input-channel lesion **did** run, on three seeds, and that the
gates were owed on it and were missing: "So the input-channel lesion has never been
tested against these gates on any seed ... Either the gates are implemented and run
on the seen seeds before registration, with the result reported, or (f) should say
what it actually binds." Section 3.3's own wording is "any ablation that breaches
them", not "the subspace ablation".

There is textual support on the other side: section 3.5 lists "OOD gates clean" among
the conditions of the L1 subspace-ablation signature, so reading the gates as attached
to that ablation is not invented. But that support is section 3.5, and the sentence
cites the seventeenth finding, which says the opposite about the occasion. The effect
of the clause is to tell the reader there was never an occasion for the gates to fire,
when the record says there was one and it was missed.

**Is the replacement the most conservative true statement available? No — it is one
clause short of it.** The most conservative true statement stops after "were never
applied to any lesion on any seed", with its citation. That version says everything
that is known and claims nothing about why. The added clause is the only part of the
rewrite that leans toward excusing the gap rather than recording it, and a closure
block is the wrong place to lean.

**On whether the rewrite overreaches or understates overall: it does neither in its
main body, and overreaches slightly in that one trailing clause.** The replacement
of "the validity gates were clean and no instrument breached them" — a positive
validity result the record cannot support — with "that bin did not fire, and it was
also never tested" is a real and large improvement, and the "never tested" half is
the half that matters. My recommendation is to cut the trailing clause, or to
re-attribute it to section 3.5 of the amendment and drop the word "because".

**Verdict: CLOSED in substance, checked.** The defect the finding named — a measured
claim with no record, contradicted by the record — is gone. Two things go on the
record: the fix's stated key count does not reproduce (and the error originates in a
finding labelled measured), and the trailing clause should be trimmed before a
registration commit.

---

## 3. The figure of 1.94 episodes in four thousand now cites where it lives

**What the fix claims.** The figure now points at the red team ledger's finding
RT-128 (the one clearing cell clears the bar by a margin inside its own estimation
noise), instead of at a findings file that does not contain it.

**Check run.**

    grep -n "1\.94" standardised-refit-findings.md
    grep -n "^| RT-128 " red_team_ledger.md

**Output.** The first returns nothing — the findings file does not contain the
figure. The second returns the row, whose opening clause reads "The one clearing cell
clears the bar by 0.000484 in accuracy, which is 1.94 episodes in 4,000", and whose
closing clause reads "The number and its fragility must travel together or neither
travels."

**Does the output match the claim?** Yes. The number is in the ledger row the
sentence now names, and the sentence is honest that the margin was "computed in the
review of that run and not stated in its findings file", which is exactly what I
measured. A checker following the citation now arrives somewhere the number is.

**One residual, not blocking.** The finding's own ruling is that the number and its
fragility travel together. The new sentence names that ruling but does not carry the
fragility as a number — that moving the null spread by one standard error puts the
cell on either side of the bar. It carries it in words instead, through John's ruled
phrase "a sub-bar pattern measured twice, not a clearance", which does communicate
that the cell is not a clearance. I record this as satisfied in substance and thin in
form, not as open.

**Verdict: CLOSED, checked.**

---

## 4. The two "never run" claims now carry their records

**What the fix claims.** The mid-episode re-indexing probe's never-run status now
cites the red team ledger's finding RT-114, and the seventy-processor-hour figure
now cites its finding RT-89.

**Check run.**

    grep -n "^| RT-114 " red_team_ledger.md
    grep -n "^| RT-89 " red_team_ledger.md

**Output** (the load-bearing clauses).

    RT-114 | "Partial discriminators" reads as "some discriminators fired". None has:
    the matched other-agent lesion has never run, the swap probe is patching and has
    never run, the mid-episode re-indexing probe has never run, the random matched
    subspaces are a null rather than a discriminator ... The count of registered
    discriminators bearing on the A3 claim is zero

    RT-89 | ... the marker-word target was priced at about 70 processor-hours against
    11 and dropped before the run, openly ...

**Does the output match the claim?** Yes, on both, and precisely.

The closure text describes the first as the finding "which lists it among the
registered discriminators that have never fired". That is what the row does: the
probe appears in a list of registered discriminators, none of which has fired.

The closure text uses the second twice. In the body it says the price "and the fact
that the job was dropped before that run rather than after it are recorded in" that
finding — and the row carries both, in those terms. In the open-items list it says
the read was "priced at about seventy processor-hours against about eleven for the
register-index read done in its place, and dropped before that run rather than
because of anything the run found" — the row's "about 70 processor-hours against 11"
matches exactly, "dropped before the run, openly" matches, and the row confirms that
what was run in its place was the register-index read.

Worth crediting: the body sentence attributes only the price and the dropped-before
fact to that finding, and does **not** attribute the "no money cost" claim to it. The
finding says nothing about money, so that careful split is correct rather than
convenient. The no-money claim is separately on the record, in the centers-as-degree
ruling's list of what it does not decide ("$0 compute, Mac time"), which the same
paragraph now cites.

**Verdict: CLOSED, checked.**

---

## 5. The carried marker-word read now gives a reason and points where the question is parked

**What the fix claims.** The open item now says why the read was deferred, and cites
the centers-as-degree ruling's section on what it does not decide.

**Check run.**

    grep -n -i "does not decide" docs/rulings/2026-09-20-center-as-degree.md
    sed -n '/does not decide/,/^## /p' docs/rulings/2026-09-20-center-as-degree.md

**Output.**

    86:## What this ruling does not decide (still open from the draft rulings)

    - Astra A10: whether the blind-localization arm (ran 2026-09-16, NOT FLAGGED) is
      discharged ...
    - Gemini's Q5: whether the ~70-hour marker-word fitted read runs before the paper
      draft. $0 compute, Mac time.
    - The three protocol amendments ...

**Does the output match the claim?** Yes. The section exists under that heading, and
its second item is the question the closure text says it leaves undecided, in the
same terms: whether the roughly seventy-hour marker-word read runs before the paper
draft. The closure text's sentence — "whether it runs before the paper draft is one
of the questions the ruling of 2026-09-20 on centers as a matter of degree expressly
leaves undecided" — is accurate.

The reason for the deferral is now given too, and it is a real reason drawn from a
committed record rather than an assertion: the read was priced at about seventy
processor-hours against about eleven for the read done in its place, and dropped
before that run rather than because of anything the run found. Both halves check out
against the ledger row in item 4 above.

This is what the original check asked for, in one sentence, and it answers the
question that check said a reader in six months would ask.

**Verdict: CLOSED, checked.**

---

## 6. "Registration revision 8" now names its file

**What the fix claims.** The reference now reads "`amendment-a3.md`, the file this
block lands in, registration revision 8 of 2026-09-15, 'The central claim is
narrowed'", and section 8 of that file says what the block paraphrases.

**Check run.**

    grep -n "^## " amendment-a3.md          (to locate section 8)
    sed -n '508,520p' amendment-a3.md
    sed -n '335,343p' amendment-a3.md       (for the date of the revisions block)

**Output.**

    ## 8. The central claim is narrowed (decision 9)

    **Ratified text:** §2.2, that the only route from the ceiling to full accuracy is
    to bind the act to the item when acting and carry that binding forward.

    **Registered:** that claim is too strong and was false of two of the three
    drafts. The acting channel marks positions, and attending back to marked
    positions is a re-readable pointer rather than a carried binding. Both routes
    need the channel, so the wire lesion cannot separate them. The mid-episode
    re-indexing probe, already registered for the tag bin, is the discriminator.

    ... All fourteen were ruled by John on 2026-09-15 after Gate 0, Gate 1, red-team
    pass 3 and an ownership-blind attack sweep ...

**Does the output match the claim?** Yes, and closely. Section 8 exists in
`amendment-a3.md` under the title the citation quotes. The closure text's paraphrase
— "attending back to marked positions is a re-readable pointer rather than a carried
binding, both routes need the channel, and so the wire lesion cannot separate them" —
reproduces the section's own two sentences almost word for word. The date is right:
the revisions block states that all fourteen were ruled on 2026-09-15.

The added phrase "the file this block lands in" also removes the specific confusion
the original check flagged, which was that a later reader might take the reference
for a section of the pre-registration.

**Verdict: CLOSED, checked.**

---

## 7. The compute ledger now credits the finding that actually made the point

**What the fix claims.** A ledger row credited its correction to "Gate A finding
RT-143's companion, the money citation". The money finding is RT-147. The row now
names RT-147 and says what it previously read.

**Check run.**

    grep -n "^| RT-147 " red_team_ledger.md
    grep -n "^| RT-143 " red_team_ledger.md

**Output** (the opening clauses).

    RT-147 | "The programme at about $226 of its $400 ceiling (`compute-ledger.md`)"
    — the figure is arithmetically right and is not in the ledger. The last programme
    total the ledger states is ~$215.7/$400; the two most recent rows carry only the
    Amendment A3 figure

    RT-143 | The paragraph headed "What A3 measured" states nine measured numbers —
    three intact scores, three lesioned scores, the state battery's movement on one
    seed and its locked threshold — and names no file

**Does the output match the claim?** Yes. RT-147 is the money finding: it is entirely
about a programme total the ledger did not contain. RT-143 is the nine-measured-scores
finding and has nothing to do with money. The old attribution was wrong and the new
one is right.

**Was the edit appropriate at all?** I was asked to judge this, because the ledger is
the system of record. **Yes, and it was done the right way.** Three reasons, each
measured.

First, no money moved. I extracted every dollar figure from the ledger before and
after the edit and compared them.

    grep -o '\$[0-9][0-9.,]*' (old ledger) | sort | uniq -c   >  a
    grep -o '\$[0-9][0-9.,]*' (new ledger) | sort | uniq -c   >  b
    diff a b

**Output.** No difference. The file is 169 lines before and after. The edit changed a
finding number inside a row's explanation and nothing else.

Second, the edit discloses itself in place. The row now ends "The row earlier read
'RT-143's companion', which is the finding about the nine measured numbers, not the
money one." A reader of the ledger alone can see what changed and why, which is the
property that makes a system of record trustworthy after a correction.

Third, this is the ledger's own established practice, not a new liberty taken with it.
The ledger already carries in-place corrections in exactly this form, for example a
row beginning "CORRECTION: an earlier version of this row called the fetched
checkpoint truncated and silently corrupt. That was a misreading ...". Correcting in
place and stating the prior wording is how this file has handled its own errors
before.

The alternative — leaving a knowingly wrong attribution in the budget instrument
because the instrument is sacred — would make the record worse, not more faithful. A
system of record should not be frozen around a known error; it should be corrected
visibly. That is what happened.

**Verdict: CLOSED, checked. The edit was appropriate.**

---

## 8. The reach figure now cites the note that produced it

**What the fix claims.** The figure of roughly one legible episode in eleven now
cites `fitted-position-sweep-findings-CORRECTION-2026-09-20.md`; that note exists,
contains the recalibration from one in twenty-seven, and carries the ruling that the
figure must cite it.

**Check run.**

    cat experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings-CORRECTION-2026-09-20.md

**Output** (the whole note is short; these are its load-bearing parts).

    # Correction note — the sensitivity figure in `fitted-position-sweep-findings.md`

    *2026-09-20 (Pacific). ... Ruled by John 2026-09-20 on Gate B review finding
    RT-74 (ledger numbering; RT-56 in the review file), "agreed on all".*

    The findings state that the run would have detected the register index if it were
    legible in about one episode in twenty-seven. That figure assumes a perfectly
    legible episode scores 1.0. This read never does ... Recalibrated against that
    ceiling, the run's reach is a signal legible in about **one episode in eleven**.

    Anywhere the one-in-twenty-seven figure has been quoted (STATUS.md, the step 4
    proposal, the paper draft), it reads one in eleven and cites this note.

**Does the output match the claim?** Yes, on all three counts. The note exists. It
carries the recalibration from one in twenty-seven to one in eleven, with the reason
(the earlier figure assumed a perfectly legible episode scores 1.0, and this read's
measured ceiling is 0.539 to 0.567). And it carries the ruling, twice over — in its
header as John's ruling of 2026-09-20, and in its closing instruction that the figure
"reads one in eleven and cites this note" wherever it is quoted.

**The added annotation checks out too.** The new parenthesis also says the figure "is
a rough reach and not measured detection power". That wording is owed to the ledger's
finding RT-169 (the block's one inference rests on a number it does not give), whose
row says the figure "is not measured detection power" and "is to be annotated as
heuristic". The annotation matches its source.

**Sweep.** I checked that the figure is not quoted anywhere else in the closure text
without the citation:

    grep -n -i "in eleven|twenty-seven" (the fixed closure text)

returns two lines — the body sentence, which carries the citation, and the correction
paragraph, which is describing the fix. No uncited use remains.

**Verdict: CLOSED, checked.**

---

## 9. The project data now matches the ledger

**What the fix claims.** `data/project.toml` reads about $225.7 of $400 and about
$44.3 of $100, as of 2026-09-21; the previous note misstated the control pilot as
$9.97 and omitted a $0.29 operations test.

**What the note now says.** For the Amendment A3 hard stop: "the A3 learnability
pilot ($13.92), the self-terminate ops test ($0.29), seeds 1 and 2 ($20.10), the
control-learnability pilot (about $9.90) and the checkpoint recovery ($0.07)."

**Check run.** Every component against the ledger's own running-total cells.

    grep -o "A3 cumulative[^|]\{0,220\}" compute-ledger.md
    grep -o "ACTUAL[^|]\{0,180\}" compute-ledger.md

**Output.**

    A3 cumulative $13.92 / $100 hard stop
    A3 cumulative $13.92 + $0.29 ops = **$14.21 / $100 stop**
    $14.21 + $20.1 → **$34.31 / $100 A3 stop**
    ACTUAL ~$9.9 → A3 cumulative ~$44.2 / $100 ... **Programme running total:
      ~$215.7 + $9.9 = ~$225.6 / $400**
    A3 cumulative ~$44.2 / $100 before this → **~$44.3 / $100** with the $0.07
      recovery; **programme running total ~$225.6 + $0.07 = ~$225.7 / $400**

**Does the output match the claim?** Yes, on every figure, and the arithmetic closes.
$13.92 + $0.29 = $14.21, as the ledger states. $14.21 + $20.10 = $34.31, as the
ledger states. $34.31 + $9.90 = $44.21, which the ledger records as about $44.2.
$44.21 + $0.07 = $44.28, which the ledger records as about $44.3 and which the
project data now carries. On the wider envelope, $215.7 + $9.9 = $225.6 and
+ $0.07 = $225.7, again exactly as the ledger's two most recent rows state and as the
project data now carries.

**The $9.97 was a units error, and the fix is right to call it one.** I found where
it came from.

    grep -o ".\{200\}9\.97.\{250\}" compute-ledger.md

**Output.**

    ... **Estimate CONFIRMED, not revised: 9.97h training, ~10.3–10.5h pod,
    $10.17–10.37**, inside the $9–13 band. ...

The only 9.97 in the ledger is **9.97 hours of training time**. The control pilot's
actual cost is recorded as "ACTUAL ~$9.9". So the previous project-data note had
carried an hours figure into a dollars field. The correction to about $9.90 is right,
and it is the difference between the old $44.2 and the corrected $44.3 reading
cleanly rather than by luck: $34.31 + $9.97 would have given $44.28, the right total
by the wrong route.

**The omitted operations test is real.** The ledger carries a row where the A3
cumulative goes from $13.92 to "$13.92 + $0.29 ops = $14.21", and the old note listed
no such item. The new note lists it.

**One small residual, recorded and not blocking.** The fix moved `as_of` from
2026-09-20 to 2026-09-21, which asserts the whole spend block is current as of that
date, but left `account_balance = 79.82` unchanged and unre-verified. The balance is
not a figure the closure text cites, and the two spend lines that it does cite are
both correct, so this does not bear on the registration. It is worth a line the next
time someone touches that file.

**Verdict: CLOSED, checked.**

---

## 10. Sweep — did the fixes break anything, or leave anything newly uncited

### The preamble's claims are now true

**What the fix claims.** The preamble's old sentence said flatly that the difference
from version 3 was confined to three things. It now reads: "As first written, the
diff against version 3 was confined to the successor's registration date, the
blind-arm sentences, and the money paragraph; the correction recorded in the next
paragraph added to it." The new correction paragraph then enumerates what was added.

**Check run.** Count and read every change the fix made to the closure text.

    git diff 8ebf9f3 worktree-agent-a9915df1f2edb2233 \
      -- docs/a3-closure-text-draft-2026-09-21-v4.md
    grep -c "^@@"

**Output.** Eight changed passages, 169 diff lines. They are: the preamble sentence
and the new correction paragraph; the heading's placeholder plus its new note; the
validity-gate sentence; the registration-revision-8 citation together with the
re-indexing probe's citation; the 1.94 citation; the seventy-processor-hour citation;
the reach-figure citation; the successor's item number; and the open-items entry for
the marker-word read.

**Does the output match the claim?** Yes. Every one of the eight is named in the
correction paragraph, and the correction paragraph names nothing that is not in the
diff. The preamble is complete about what changed and no longer over-claims about
what did not. The original check's verification of the "as first written" half —
that the body changes against version 3 were confined as stated — is preserved by the
new hedge rather than contradicted by it.

### Nothing the earlier check verified has been broken

**Check run.** I re-ran the decisive greps behind the five findings the original
check closed, against the fixed text, to confirm the fixes did not disturb them.

**Output.**

    must be ABSENT
    these checkpoints have one                absent (ok)
    less plausible                            absent (ok)
    readily recoverable                       absent (ok)
    validity gates were clean                 present — see note

    must be PRESENT
    rank matched by design and accuracy matched as observed   present (ok)
    does not discharge the registered requirement             present (ok)
    not testable (localization)                               present (ok)
    instrument failure, not absence                           present (ok)
    seeds-endpoint-findings.md                                present (ok)
    ceiling-measurement-findings.md                           present (ok)
    ceiling-defect-2026-09-17.md                              present (ok)
    powered-position-sweep-findings.md                        present (ok)
    standardised-refit-findings.md                            present (ok)
    other-index-position-sweep-findings.md                    present (ok)

The one flag is not a regression. The phrase "validity gates were clean" survives only
at line 27, inside the new correction paragraph, which quotes the old sentence in
order to say it was replaced. That is correct disclosure, not a surviving claim. The
two entries I first read as missing — the registered term and the registered reading —
are present and simply wrap across lines; I confirmed both by reading the paragraph.

The bolded sentence carrying the registered term and the registered instrument-failure
reading is intact and still at the head of its own paragraph, which is the position
the finding behind it asked for.

### One pre-existing gap the fixes did not address, still open

The original check's fifth "smaller thing" was that the rehearsal requirement in the
closure text cites nothing. It still cites nothing.

**Check run.**

    grep -n -i "rehearsal" (the fixed closure text)

**Output.** The sentence stands as before: "the successor's whole purpose is a
measurement that does not yet exist, so the rehearsal requirement — that a full
measurement procedure be demonstrated before it is registered — applies to it even
though it does not apply to this closure." No file is named.

**Status of the underlying record has improved, though.** When the original check was
filed, that requirement's protocol text did not exist anywhere. It now exists and is
on the main line:

    git merge-base --is-ancestor 93c9cb2 main   ->  YES

So the sentence could now cite the protocol's new section on the measurement
rehearsal, and the December-result ruling's sixth item that ordered it. Three or four
words. This is a sentence asserting a binding requirement with nothing to open, which
is the defect class the closure rule exists for, though it is not a sentence saying
verified, measured, calibrated or attacked, so it falls outside the strict letter of
the rule's second clause. **I leave it open**, at worth-noting severity, because the
fix session did not touch it and because a finding nobody has checked does not close
by being small.

### Nothing newly uncited

Every citation the fixes added, I opened and read. All eight land on text that says
what the sentence says. No fix introduced a new claim without a record. The one added
sentence that goes beyond its record is the validity-gate trailing clause in item 2,
which is a reason rather than a fact and is covered there.

---

## Is the closure text now fit for a registration commit?

**Yes, once one clause is trimmed — and it is much closer than it was.**

The fatal finding that stopped it is closed on measurement: the successor's schedule
now cites the item that carries the facts, and I opened the file and confirmed it. The
three uncited claims the original check raised — the validity gates, the
1.94-in-four-thousand figure, and the re-indexing probe's never-run status — all now
carry records, and all three records say what the sentences say. Two further citations
nobody had asked for were added and both check out. The project data matches the ledger
to the cent, and the one wrong number in it turned out to be an hours figure that had
been read as dollars. The ledger's mis-attribution is corrected without moving a
dollar and with the prior wording disclosed in place. Nothing that earlier passes
verified has been disturbed.

**What I would want changed before the commit.** One thing, and it is a deletion, not
a rewrite: cut the trailing clause of the validity-gate sentence — "and the subspace
ablation they were written to guard never ran, because no subspace was ever localized"
— or re-attribute it away from the seventeenth finding, which does not support it. The
sentence is stronger and more conservative without it, and a closure block that is
about to be registered should not carry its one exculpatory inference in the same
breath as the record that cuts against it.

**Two things for the record rather than for the text.** The key count behind the
validity-gate check does not reproduce, and the error originates in a finding labelled
MEASURED — a reminder that a label is not a measurement, which is the reasoning the
amended rule rests on. And the rehearsal requirement still cites nothing, which is now
a three-word fix because the protocol text it would cite has reached main.

**On the rule I verified under.** Every item above is a command I ran with its output,
not a reading of the fix session's reasoning. I accepted nothing on argument alone. The
one item where a measurement was available and disagreed with the claim is reported as
disagreeing, which is the case the rule was written for.

---

# Addendum, added 2026-09-21 after the original filing

*The two changes this verification asked for were made by another session on the
branch `worktree-agent-a53dc49a926581fe8` (work commit `628686f`). The closure rule
leaves their check to a session that did not write them, which is again this one. I
was also asked to look at a third sentence that session noticed and deliberately left
alone. Everything above this line is as originally filed and is unedited.*

*One thing about the base is worth recording, because it is the first time it is
true. That branch's setup commit `25f11c7` merged the closure-text fixes onto the
current main tip, so the amended protocol from pull request 13 and the closure fixes
now sit on one branch together. I confirmed that the merge-base check reports both the
protocol amendment commit (`c63d960`) and the closure fixes commit (`41d44ea`) as
ancestors of the branch I am checking. The rule and the text it governs are finally in
one place.*

## A1. The trim removed exactly the clause and nothing adjacent

**Check run.** The complete difference between the version I verified above and the
version after the trim.

    diff (the version verified above) (the trimmed version)

**Output.**

    67,70c67
    < neither — `red-team-a4.md`, its seventeenth finding, labelled there F17), and
    < the subspace ablation
    < they were written to guard never ran, because no subspace was ever
    < localized.
    ---
    > neither — `red-team-a4.md`, its seventeenth finding, labelled there F17).

    214,215c211,213
    < before it is registered — applies to it even though it does not apply to
    < this closure.
    ---
    > before it is registered (`docs/outside-review-protocol.md`, its section on
    > the measurement rehearsal required before any Gate A) — applies to it even
    > though it does not apply to this closure.

Two changed passages in the whole file and nothing else — four lines added, six
removed, matching what was reported.

**Does the output match the claim?** Yes. The removal is exactly the clause I named
and stops at exactly the point I recommended. The sentence now reads:

> That bin did not fire, and it was also never tested: those gates have no code
> written for this design and were never applied to any lesion on any seed (the
> independent review of 2026-09-19 searched the source and the three endpoint records
> and found neither — `red-team-a4.md`, its seventeenth finding, labelled there F17).

Nothing adjacent moved. The preceding clauses — the plain gloss of the bin, "that bin
did not fire, and it was also never tested", the no-code clause, the never-applied
clause and the citation — are all intact and unaltered. The paragraph that follows
begins exactly where it did.

This is now the most conservative true statement the record supports: it says what is
known, cites where that is recorded, and claims nothing about why. A side benefit is
that the awkward mid-clause line wrap I noted in passing is gone with the clause.

**Verdict: CLOSED, checked.**

## A2. The rehearsal requirement now cites a section that exists on main

**Check run.** Search the protocol on the main line for the section heading the
citation names.

**Output.**

    98:## The measurement rehearsal, required before any Gate A

**Does the output match the claim?** Yes. The citation reads "`docs/outside-review-protocol.md`,
its section on the measurement rehearsal required before any Gate A", and the section
heading on main is "The measurement rehearsal, required before any Gate A" — the same
words. A checker following the citation lands on the section that carries the
requirement the sentence asserts, including its six named checks.

The sentence it sits in is otherwise unchanged, and the citation is placed inside the
dashes so the sentence still reads straight through.

This closes the last item I left open above. It is worth saying plainly why it could
be closed now and not before: the requirement was ruled on 2026-09-20 but its protocol
text did not exist until pull request 13 merged. The sentence was asserting a real
rule with nothing to point at. Now it points at it.

**Verdict: CLOSED, checked.**

## A3. The other sentence, on whether it makes the same move

The sentence flagged, at line 154 before the trim and line 151 after it (the trim
removed three lines above it; I confirmed the text at both line numbers is identical):

> Because the two instruments never converged on any seed, no L1 subspace was ever
> localized, and so the registered uncarvable signature H_diffuse was never reachable
> either: it requires a subspace that beats the matched controls, and none was carved
> to compare.

**The question.** Does this supply an absence-of-occasion reason the record argues
against, as the trimmed clause did?

**Check run.** Every place the registered signature is defined, and every ruling on it
— a search for the signature's name across the amendment, the pre-registration and the
red team ledger, then the registered signature itself, the convergence requirement it
depends on, and the ledger row that ruled on it.

**Output.**

    amendment-a3.md, line 227:
    - **H_diffuse (present but uncarvable).** L0 collapses T_act (ownership is
      load-bearing) but no L1 subspace at k ≤ 16 beats the L2 controls, and
      probe-patching convergence fails. ...

    amendment-a3.md, line 206:
    4. **Convergence requirement**, inherited: L1 counts as localized only when probe
       and patching agree on a confound-controlled design; otherwise the outcome is
       *not testable (localization)*, as Experiment 1 registered.

    red_team_ledger.md, line 758:
    | RT-166 | No registered bin or signature is named. The closest fit, H_diffuse, is
    not addressed: its first and third conjuncts happened and its second did not,
    because no subspace was ever localized to compare against the matched controls.
    ... | worth-noting | ACCEPT (drafted) | Why a registered signature did not fire is
    the kind of thing a closure block should say, especially when the signature and
    the outcome are one missing run apart. ... Done in version 3. |

**Answer: no, it is not the same defect, and I would not cut it.** Three reasons,
each from the output above.

**Its premise is the registration's own rule, not the text's own inference.** The
trimmed clause asserted, on its own authority, what the gates were "written to guard".
This sentence's premise — that without convergence nothing counts as localized — is
the registered convergence requirement at section 3.2 item 4, word for word: "L1
counts as localized only when probe and patching agree ...; otherwise the outcome is
*not testable (localization)*". Applying a registered definition is not the same act
as inventing a reason.

**Its reason is the ruled position, not one the record argues against.** This is the
decisive difference. The trimmed clause gave a reason its cited source contradicted.
This sentence gives the reason the ledger's finding RT-166 gives, accepted on
2026-09-21, in the same terms: "its second did not, because no subspace was ever
localized to compare against the matched controls". The closure text is carrying out
a ruling, not working around one.

**It points the other way.** The trimmed clause used an absence to say nothing was
missed — it excused a gap. This sentence uses an absence to say a registered outcome
was not even available to the experiment. It widens the admission of failure instead
of narrowing it. A sentence that costs the closure something is not the failure mode
the trimmed clause was an instance of.

### One separate and smaller problem in that sentence, which is a wording fault

Having said it is not the same defect, there is something else wrong with it, and
since the text is about to be registered it should be said.

The sentence describes the signature as one that "requires a subspace that beats the
matched controls". The registered second conjunct reads "**no** L1 subspace at k ≤ 16
beats the L2 controls". Read literally, the closure text states the inverse of the
registered condition: the signature fires when nothing beats the controls, not when
something does.

The ruling's own wording avoids this. RT-166 says "no subspace was ever localized **to
compare against** the matched controls" — the comparison sense, which is right: what
the second conjunct needs is a carved subspace and a comparison, and neither existed.
The closure text has compressed "a subspace to compare against the matched controls"
into "a subspace that beats the matched controls", and in compressing it has inverted
the test.

The clause "and none was carved to compare" pulls the reader back toward the intended
sense, so a charitable reader gets there. But a hostile reader doing exactly what the
closure rule is designed to make possible — open the registered signature at section
3.5 and check — finds a condition stated in the negative where the closure text states
it in the positive, and cannot tell whether the closure has misread its own
registration. That is a small fault of the same family as the item number: not a false
conclusion, but a pointer that does not survive being followed.

**The fix is a few words**, and it is the ruling's own: "it requires a carved subspace
to compare against the matched controls, and none was carved". No substance changes.
The conclusion — that the signature was not reachable — is unaffected and remains
correct.

**Verdict: not the same defect, and sound in substance. One wording fault recorded,
at worth-noting severity.** I record it rather than closing it because I did not write
the text and cannot fix it, and because a sentence that inverts a registered condition
should be looked at by whoever holds the pen before the commit, not after.

## Is the closure text fit for a registration commit now?

**Yes.** The clause I asked to be cut is cut, exactly and with nothing adjacent
disturbed. The last uncited assertion now cites a section that exists on main under
the heading the citation names. Every one of the ten items checked above stands
closed, and the two follow-up changes introduced nothing new: the complete difference
from the version I verified is two passages, both of which I have just checked.

**What remains is one wording fault and one thing that is not about this text.**

The wording fault is the inverted conjunct in item A3. It does not make the closure
say anything false and it does not block a registration commit in my judgement, but it
is three words from being right and the right three words are already written in the
ruling it implements. If the pen is still in someone's hand, this is the moment.

The thing that is not about this text: the key count behind the validity-gate finding
still does not reproduce, and the finding carrying it is labelled MEASURED. That error
never entered the closure text and is now further away from it than ever, since the
clause that leaned on the finding is gone. But the finding itself is a committed record
that a future session may cite, and it says something measurable that measurement does
not support. Correcting it belongs to whoever owns `red-team-a4.md`, not to this
closure.

One last note on the placeholder, which is not a defect but will become one. The
heading still reads "[date of the Gate A pass]" and the text under it says so plainly.
That is correct for a draft and cannot survive the commit that appends the block, which
is the same point the ledger's finding RT-166 makes at its end. The commit that files
this block is the one that fills it.

---

# Second addendum, added 2026-09-21 after the first

*The wording fault recorded at worth-noting severity in the first addendum has been
corrected by another session on the branch `worktree-agent-a5b280b93c1ba5e41`
(correction commit `a4c754e`). The closure rule leaves the check to a session that did
not write it, which is again this one. Everything above this line is as originally
filed and is unedited. That branch's setup commit `5fa8a4c` merges the trimmed text
with current main; I confirmed that both the trim (`628686f`) and the protocol
amendment (`c63d960`) are ancestors of it.*

*Main has moved since the first addendum — two further merges (pull requests 14 and
15) are now in the base. I checked what they touch before relying on anything above:
`git diff --stat c63d960 dd1b974` returns seven files, six of them new (a ruling file,
a method note and four launcher and reaper scripts) and one modified
(`watch_run_a3.sh`). **No record any check above relied on was modified.** The
rulings, the red team ledger, the amendment, the separation-clause requirements, the
compute ledger, the project data, the correction note and the gate records are all
untouched. Every verdict above still stands on the evidence it was given.*

## B1. The correction is exactly one change, and it is the right one

**Check run.** The complete difference between the version verified in the first
addendum and the corrected version.

**Output.**

    153c153,154
    < subspace that beats the matched controls, and none was carved to compare.
    ---
    > carved subspace to compare against the matched controls, and none was
    > carved.

One changed passage in the whole file and nothing else.

**Does the output match the claim?** Yes, and the coordinator's note that it is more
than a three-word swap is right — I said three words and I was wrong. What actually
happens is that one clause is rewritten: "that beats" comes out, "carved" and "to
compare against" go in, and the trailing "to compare" moves up into the requirement
clause where it belongs. Judged as what it is rather than as what I predicted, it is
the correct edit: the estimate was mine and it was low, and the size of the change is
not a mark against it.

The sentence now reads:

> ...and so the registered uncarvable signature H_diffuse was never reachable either:
> it requires a carved subspace to compare against the matched controls, and none was
> carved.

The inversion is gone. A reader who opens section 3.5 of the amendment now finds a
condition about comparing a carved subspace against the controls, and a closure text
that says the same thing. The claim I could not check before — whether the closure had
misread its own registration — is now answerable by opening the file, which is the
whole point.

**Verdict: CLOSED, checked.**

## B2. "Matched controls" loses no precision, and is better than I expected

The session chose "matched controls" over the registration's "L2 controls" on three
grounds: it is the ledger's finding RT-166's own phrase, it matches the surrounding
paragraphs, and it is plainer under the workspace rule. I was asked to confirm it
loses no precision against the registered wording.

**Check run.** How the registration itself names L2, at section 3.1 of the amendment.

**Output.**

    - **L2, matched controls.** (a) The *other-index* subspace: the same localization
      run for a named non-self agent ("which marker is agent B's"), matched in rank
      and probe accuracy; (b) random subspaces of matched rank and norm (Experiment
      1's null-calibration move); (c) on the five existing register-bearing
      checkpoints only, the register lesions already run, as a $0 reference. ...

**It loses nothing, and there is a fourth ground the session did not claim: "matched
controls" is the registration's own name for L2.** Section 3.1 defines the level as
"**L2, matched controls**" in those words. So the closure text is not paraphrasing a
registered term into a looser one; it is using the registration's own plain name for
exactly the same object. "L2" is the label and "matched controls" is what the
registration says the label means. Under the workspace rule, which asks for the plain
word rather than the term of art, using the name over the code is right, and here it
does not even cost the precision that choice sometimes costs.

**One thing the new wording does not carry, recorded and immaterial.** The registered
conjunct is "no L1 subspace **at k ≤ 16** beats the L2 controls" — the rank cap of
sixteen, set at section 3.2 to match Experiment 1's primary condition. The closure
sentence does not mention it. This costs nothing here, because the sentence's point is
that no subspace was carved **at all**, at any rank, so the cap never becomes
relevant. Had the sentence claimed that subspaces were carved and none beat the
controls, the cap would have to travel with it. It does not make that claim.

**Verdict: no precision lost, checked.**

## B3. On the vacuity question, and whether sidestepping is the right side of the line

The session flagged that a pedantic reading of the registration would hold the second
condition satisfied vacuously — if nothing was carved then trivially no subspace beats
the controls — while the ledger's finding RT-166 holds that the condition did not hold
because there was nothing to compare against. It says the new wording states what the
signature *requires* rather than asserting whether the condition was met, and judges
that this sidesteps the question rather than answering it wrongly. It calls this the
one judgment in the edit and asks whether I agree.

**I agree with the edit. I do not agree with the description of it, and the difference
is in the text's favour.**

**The sentence does not sidestep. It takes a position, in the word "unreachable".**
Work the vacuous reading through. RT-166 records that the first and third conditions
happened. I checked the first independently rather than taking the finding's word:

    grep -n "0.5683\|0.1988" seeds-endpoint-findings.md
    25:| pilot (seed 0) | 0.5683 (sd 0.0076) | 0.1988 (sd 0.0173) | 1.337 | 7.5× |

L0 collapses the primary battery from 0.5683 to 0.1988, and the same holds on the
other two seeds, so ownership is load-bearing — the first condition. The third,
probe-patching convergence failing, holds because patching never ran. Now grant the
vacuous reading of the second. All three conditions are then met, and **H_diffuse
would have fired** — it would be the registered outcome of the experiment, not an
unreachable one. The sentence says it was never reachable. That is flatly inconsistent
with vacuity. The text has already chosen RT-166's side; what it declines to do is
argue for the choice.

**Stating the conclusion and leaving the argument in the ledger is the right division
of labour, and that is a better defence than sidestepping would be.** A closure block
summarises; the ledger carries reasoning. RT-166 is where the argument belongs and is
where it is. Asking the closure text to adjudicate a point about vacuous truth would
put a logic aside into a paragraph that is doing something else.

**And the position it takes is the right one, so the text is not resting on a
coin-flip.** This matters, because "we sidestepped it" would be a weak defence if the
ruled side were wrong. It is not. The signature means "present but uncarvable".
Uncarvability is a claim about what happened when someone tried to carve. Letting it
be satisfied by never trying would let an experiment that never ran the comparison
claim a registered finding — which is the same move as the sentence I had struck two
addenda ago, where gates that were never built were reported as clean. The programme's
whole discipline is against it. RT-166 is right on the merits, and a hostile reader who
presses the point arrives where the text already is.

**Where I would push back, and it is not a defect.** A text about to be registered
should take a position when the position is already ruled and the alternative would let
the experiment claim something it did not earn. The session framed its edit as
declining to take one. Its sentence takes one anyway, correctly. So the judgment call
was sounder than the session gave itself credit for, and nothing needs to change.

**Should the text say more?** No. Adding "and this did not hold vacuously, because..."
would be an argument in a summary. The conclusion plus the fact that does the work —
"and none was carved" — is enough, and the reader who wants the reasoning can find it.

**Verdict on the judgment: sidestepping would have been acceptable; taking the
position, which is what the sentence actually does, is better. Sound as it stands.**

## B4. One thing I considered raising and decided not to, recorded so the next pass need not rediscover it

The sentence makes an interpretive claim — that a registered signature was never
reachable — which rests on a contested reading, and it does not name RT-166. The
citations this verification asked for elsewhere (the never-run claims, the
1.94-in-four-thousand figure) were exactly of this shape, so the question is fair.

**I am not raising it as a finding, and here is the honest reason.** The preamble
already says John ruled all twenty-nine tier 1 findings, the ledger's RT-143 to
RT-171, accepted as drafted, and RT-166 sits inside that range — so a document-level
attribution does cover it. The sentence uses none of the four words the closure rule's
second clause triggers on (verified, measured, calibrated, attacked). And the finding
is one search away: I found it by searching the ledger for the signature's name, in a
single command. Naming RT-166 in the sentence would be a small improvement and I would
take it if the pen were open, but it does not meet the bar for a finding, and the
amended protocol is explicit that severity is not to be manufactured to look thorough.
Recorded as considered and declined.

## B5. Nothing else moved

**Check run.** The sweep behind every earlier verdict, re-run against the corrected
text.

**Output.** The four phrases that must be absent are absent, including the inverted
one just removed. Every citation and ruled phrase that must be present is present: the
other-agent control's two ruled phrasings, the never-applied-to-any-lesion clause, the
rehearsal citation, the successor's item 1, the three ledger findings behind the
never-run and margin claims, the endpoint findings file and the correction note. The
one entry my sweep flagged, the registered instrument-failure reading, is present and
wraps across lines 157 and 158, which I confirmed by reading it.

## Is the closure text fit for a registration commit, with nothing outstanding in the text itself?

**Yes. Nothing in the text is outstanding.**

Every item raised across this verification is now closed on measurement: the wrong
item number, the validity-gate sentence and its overreaching clause, the margin
figure's citation, the two never-run claims, the deferred read's reason, the
registration revision, the ledger's attribution, the reach figure's citation, the
project data's arithmetic, the rehearsal requirement's citation, and now the inverted
conjunct. The complete difference from the version I verified at each stage has been
two passages, then one, then one — each checked, none introducing anything new.

**Two things remain on the record, neither of them in the text.**

The key count in `red-team-a4.md`'s seventeenth finding still does not reproduce — the
endpoint record has 15 top-level keys and has never had 110 — and that finding is
labelled MEASURED. It never entered the closure text, and the clause that leaned on it
is gone, so it cannot reach the registration. It remains a committed record asserting
something measurable that measurement does not support, and correcting it belongs to
whoever owns that file.

**One new item, found while checking what had moved on main, and reported because it
is a ruled correction that appears not to have landed.** The ruling of 2026-09-21 on
review verification and staged spending
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, item 16) rules
that the stale spend figures are corrected to the compute ledger, and names two places
that carried $215.70: `data/project.toml` and section 6 of the December-result roadmap.
The project data was corrected, and I verified it above. The roadmap was not:

    grep -n "215\.7\|225\.7" docs/december-result-roadmap-2026-09-20.md
    135:**Spend.** The program envelope is $400 (raised 2026-08-16; $215.70 spent per
    data/project.toml), with about $184 ...

It still carries $215.70, and it attributes that figure to the project data file, which
no longer says it. Its headroom figure is stale too — about $184 against the $174.30
the ruling states. This is outside the closure text and outside everything I was asked
to verify, so it changes no verdict above. It is a ruled correction that looks
unlanded, and the next session to touch that file should close it.

**One note that is not a defect and will become one.** The heading still reads "[date
of the Gate A pass]" and the paragraph under it says so plainly. That is right for a
draft. The commit that appends this block to `amendment-a3.md` is the commit that fills
it.

*A closing note on the rule I have been working under. The ruling of 2026-09-21 item 3
extends reviewer-owned verification to every Gate A pass, whether or not a fatal
finding exists, on the reasoning that the programme's worst failure was not a missed
finding but that nobody ever ran anything to confirm a fix. Every verdict in this file
and its two addenda is a command with its output. Where a measurement was available and
disagreed with a claim — once, on the key count — it is reported as disagreeing.*
