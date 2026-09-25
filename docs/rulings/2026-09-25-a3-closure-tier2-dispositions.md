# Ruling 2026-09-25: dispositions of the two outside (tier 2) reviews of the A3 closure text, version 4

*Recorded 2026-09-25 (Pacific), in a Cowork planning session. Mixed authorship:
the draft dispositions were proposed by the Claude Code session "MVM W1 A3
dispositions" in `docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md`
(pull request 37, checked by a separate session before merge); the judgment
calls were put to John in plain language with their strongest alternatives, and
he ruled "Agreed on all". The choices are his; none of the wording is his
drafting. No compute was launched and no money was spent under this ruling.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).
The two reviews are filed verbatim at
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-gemini.md`
(Gemini 3.1 Pro) and `…/2026-09-21-a3-closure-chatgpt.md` (ChatGPT 6 Astra
Medium, run in the Codex app), both dated 2026-09-25, and are never edited.
Neither reviewer filed a fatal finding; between them, 15 serious findings, all
closable by rewording, none needing a run or money.*

---

## The ruling

**All 22 items of the proposal are ruled as recommended**, with the judgment
calls stated in John's name below. The item numbers are the proposal's.

1. **K5 is not reached.** Hard kill K5 of `amendment-a3.md` ("probe-patching
   convergence fails on all three seeds") tests whether two instruments agree.
   Causal patching was never built for this design (ruling of 2026-09-20,
   ledger RT-96), so the test was never run. Version 5 names K5 and says so.
   The term *not testable (localization)* rests on §3.2's convergence
   requirement, and A3 closes under the pre-registration's loss condition, with
   no further A3 seeds. A dated annotation goes beside RT-164's line in the red
   team ledger saying "Done in version 3" was not so; the line itself is not
   edited. This is John's interpretation of registered text, stated here in so
   many words.
2. "Never converged" is replaced by Gemini's wording: patching was never run,
   so agreement could not be tested and no L1 subspace was ever localized.
3. Gemini G1 accepted as credit for the citations and endpoint numbers, not
   for the money (see 8).
4. Gemini G2 accepted as credit, read with 13.
5. "Never applied to any lesion" becomes "never applied to the input-channel
   lesion, the only lesion A3 ran, on any seed".
6. ChatGPT A1 accepted as credit; "quadrupled weight" becomes "per-row gradient
   weight quadrupled".
7. The 270-test sentence is replaced by ChatGPT's, naming the two targets (135
   each) and "at the discovery positions".
8. In the money paragraph, version 5 states about $46.2 of Amendment A3's
   $100 stop and about $227.6 spent as of the ledger's 2026-09-21 row, against
   a programme ceiling raised from $400 to $450 on 2026-09-25
   (`docs/rulings/2026-09-26-weekend-1-queue.md`, page 6), re-read on the day
   version 5 lands.
9. The 2026-10-11 target is dropped; the two kill dates (2026-10-18, 2026-11-01)
   stay, citing the ruling's annotation.
10. ChatGPT A5 accepted as a record of the packet's limits; no text change; the
    next packet's brief carries every protocol section the text cites.
11. Main point accepted: restore the restriction "any control fully determined
    by the visible episode and not requiring ownership" and adopt ChatGPT's
    successor sentence. **Sub-point declined:** the ceiling findings file
    contrasts the state battery with the ownership-free control and does not
    call it ownership-free (proposal check C10).
12. **The narrower form.** The ruled phrase of the 2026-09-21 Gate B ruling is
    kept and bounded: "excluded the exclusion confound in the form proposed, a
    four-way rank of the other agent that this probe could decode", followed by
    the existing sentence that a relational route remains open (RT-125). The
    Gate B ruling is not re-ruled inside a closure text.
13. ChatGPT A9 accepted as credit; see 22.
14. The blind-arm sentence is replaced by ChatGPT's: discharged so it does not
    block closure; that does not establish recovery on this design; the
    requirement carries into the successor's rehearsal.
15. ChatGPT's paragraph on the two decisions (patching not built for A3;
    no further work on the other agent's revision-value position) is added,
    citing both rulings by item.
16. **ChatGPT's headline is adopted:** "Outcome: not testable — the registered
    comparison was undefined for every possible model. Separately, removing
    the ownership-input channel reduced primary-battery accuracy on all three
    trained seeds."
17. The same-act limit the pre-registration requires of every write-up (line
    84) is added in ChatGPT's two sentences, and its public sentence is used.
18. The one-in-eleven sentence is replaced by ChatGPT's, scoped to the fitted
    register-index read, keeping the citation of the correction file.
19. Of the six small changes: (a), (c), (d), (f) accepted; (b) becomes "had
    not been attacked before registration"; **(e) adopted** (John, 2026-09-25,
    on the check's evidence; the proposal had held it): the proposal held it
    pending a check, and the check of the dispositions
    (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`,
    pull request 40) showed from the refit code and the run's three output
    files ("no test shares a split with the unscaled run's") that the refit
    used different fold splits and shuffled draws. The findings file
    `standardised-refit-findings.md` does not show it and its "by nothing
    else" sentence overstates what its anchor check proves; version 5 cites
    the check, not the findings file, for this point.
20. A dated annotation beside the ChatGPT review file (not in it): run in the
    Codex app; model as the app reported it, "ChatGPT 6 Astra Medium"; the
    body's self-description "Codex" is the app's name; documents pasted in 22
    parts in one conversation; no lookup verified.
21. Adopted findings are numbered from **RT-204**. A later session reconciles
    RT-172 to RT-203, which appear in filed reviews but have no ledger rows;
    not on this weekend's critical path.
22. **Process.** Version 5 is written by a session that did not draft the
    dispositions, from items 1, 2, 5 to 9, 11, 12 and 14 to 19 as ruled. A
    tier 1 reviewer that is not the version 5 writer then runs the closure
    rule's reviewer-owned check on version 5 and files it. The registration
    commit (appending the closure block to `amendment-a3.md`) follows only
    then. No second outside round, since nothing fatal came back.

## What this file does not do

It does not edit the closure text (version 5 is a new file), the reviews, the
ledger, `amendment-a3.md` or any protocol text. Version 5 is not registered by
this ruling; the registration commit waits on item 22.
