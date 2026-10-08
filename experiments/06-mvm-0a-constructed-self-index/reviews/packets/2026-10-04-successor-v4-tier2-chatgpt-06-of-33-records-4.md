*This is file 6 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 5 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 5 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
2. **Candidate sites: the rule, the printed list, and what is removed from the
   family.** The site list is registered as the rule that generates it
   (ruled, the queue ruling, page 1e), and the registration prints the list
   the rule produces for the registered 12-layer architecture beside the rule,
   with the count of comparisons it implies, so the family correction is
   pre-stated. **The rule has now been run at toy scale exactly as registered
   (ruled, the Gate C rulings, RT-215; MEASURED: the re-run findings at
   `9d9d31a`, Part 1), so every toy nomination, reading and control figure in
   this version comes from the family the rule generates**, which meets the
   review's objection that version 2's figures came from a hand-listed
   44-set family the rule never produced (the Gate C review, RT-215). The
   rule:
   - **Positions**, grouped into the position sets the rehearsal used and
     registered here by name (`experiments/rehearsal-successor-measure/src/rehearse.py`,
     `CANDIDATE_POSITIONS`; positions in `src/transplant.py`): the action
     position alone (`action`); **the action position and the answer-marker
     token just before it** (`action+ans`; version 2 described this set
     backwards, the Gate C review, RT-224); the action position and the three
     positions before it (`action+3`); every position from the model's first
     own turn to the action (`post-identity`). (The rehearsal's fifth set,
     every position, is excluded by the rule below.) **Ruled 2026-10-03 (decision 19): the
     position sets are the rehearsal's four, by name.**
   - **Layers**: every contiguous set of the model's running states, counting
     the state after the input embedding as one (layer 0) and each of the
     twelve blocks' outputs as one more: 13 states, 91 contiguous sets.
   - **The all-positions exclusion** (ruled, the repairs rulings, item 3):
     **any site set whose positions are all positions is excluded**, at any
     layer. The reason is section 6.2's: copying all positions at a layer
     hands the donor's whole forward pass downstream. On the four named
     position sets no site set spans every position in any episode (MEASURED:
     the re-run's `out-v3-rules/nominate_*_seed*.json`, field
     `family.share_of_episodes_where_position_set_spans_every_position`; the
     check at `70be9fb`, section 4.3), so on this family the exclusion removes
     nothing further.
   - **The layer-0 exclusion, as removal from the family (ruled, the Gate C
     rulings, RT-216, item 1, as clarified by refinement item 2).** Layer 0 is
     the state the acting channel is added to. **Every site set whose layers
     include layer 0 is removed from the candidate family before nomination
     at every position set other than `action`**, and the rule chooses again
     from what remains, in the way the all-positions exclusion works. Layer 0
     stays a candidate at the action position set only, where the constructed
     anchors' slot sits by construction. The reason: at position sets
     spanning the turns the channel fires on, the twins differ at layer 0 only
     by the channel's own input, so a whole-state transplant there is a
     transplant of the acting channel and not of anything the network built,
     and the subspace compared against it was, on arms C and F, a read fitted
     at 0.072 (the Gate C review, RT-216). **This reading of the ruling, that
     "excluded" means removed from the family and chosen again, was clarified
     after the re-run of 2026-09-26, with the re-run's figures in hand, and is
     not called pre-stated here**: the re-run's first pass read "excluded" as
     "reported as no verdict", recorded the removal reading as its own column
     before it ran, and put the choice to John, who ruled the removal reading
     on the same day (the re-run findings, Part 2; the check at `70be9fb`,
     sections 1.3 and 4.6). Under it, six of the nine toy nominations on arms
     C, F and M that the first pass had left at the injection move off layer
     0, every one to a single later layer (the re-run findings, Part 1,
     section 1.5). *Two readings of which position sets "span the acting
     turns" exist, and they give the same twelve toy nominations:* the ruling's
     first sentence keeps layer 0 at `action` only, which the re-run applied;
     its parenthesis names `post-identity` and any set including the marked
     turns, which on this grammar is `post-identity` alone (MEASURED: the check
     at `70be9fb`, section 4.4, by a script printed in its appendix C and not
     committed as a file). **This version registers the reading as run, layer
     0 kept at `action` only, 45 site sets on the toy and 325 on the
     registered model (ruled 2026-09-26 on decision 20)**; the narrower
     reading is recorded beside it as the alternative that was put and not
     taken. On the separable arms layer 0 inside
     the action turn does move the action (arm T's whole-state share there is
     1.000 against 0.000 untouched; arm M's about 0.40, short of its floor),
     so it is the rule's position-set order, `action` first, that decides the
     tie on arm T and not any property of the states (the check at `70be9fb`,
     section 5). Version 2's argument that those states are identical in the
     twins was wrong for arms T and M and is not repeated.
   - **The count.** With every contiguous layer set at the four position sets,
     the family is 60 site sets on the toy and 364 on the registered model;
     with the layer-0 sets removed at the three position sets other than
     `action`, **45 site sets and 180 comparisons on the toy, and 325 site
     sets and 1,300 comparisons on the registered model** at four rank caps.
     The narrower reading of decision 20 gives 55 and 220 on the toy, 351 and
     1,404 on the registered model; the stricter variant below gives 40 and
     160, and 312 and 1,248 (MEASURED: the review of version 3, "What was
     checked and held", recomputed all eight site-set counts by arithmetic
     on the rule; section 18 prints the registered list with its command). The ruled figures before the
     all-positions widening, 296 and 1,816, and version 2's 60 and 364, are
     superseded by these; the repairs rulings' annotation 4 records the first
     supersession. The list and the rule have to agree, and the registration
     prints both: **the list for the registered model is printed in section
     18**, generated by the rule and not typed by hand, with the command that
     generated it.
   - **The stricter variant, as a sensitivity row (ruled, the Gate C rulings,
     RT-216, item 3).** Every layer-0 site set removed at every position set,
     `action` included, then choose again. Reported beside the primary
     reading for every arm and seed, so John can switch to it with figures in
     hand before Gate A. On the toy it differs from the primary row only on
     arm T, whose site moves from layer 0 to layer 1 at the action position,
     rank 8, with fit 1.000 and reading 0.0000 on every seed; on arms C, F
     and M the primary nominations contain no layer 0, so the row is the same
     pick with the same numbers (MEASURED: the re-run findings, Part 1,
     section 1.3; the check at `70be9fb`, section 3.7). The reason recorded
     for not ruling it blind: it may move arm T's anchor read off the layer
     its slot was built at, which on the toy is exactly what it does.
3. **Candidate directions, and the read that supplies them, registered.**
   **The read the rule uses is one fitted straight-line read per layer, on
   the running state at the mask token of the own-directed action (the
   `action` position), labelled with the model's own marker word, fitted on
   the development episodes and scored on the held-out part of them** (in the
   rehearsal code, `repairs.fit_reads`: one logistic regression per layer, the
   same read whatever site set is later nominated). At each site set the
   directions transplanted are that read's leading directions at each layer
   in the set, at each of the rank caps **1, 2, 4 and 8**; **the registered
   cap is 8** and the search family reports all four (ruled, the queue ruling,
   page 1d).

   **The piece rule (ruled 2026-10-03, page 1; the review of version 3,
   RT-230, option (b)).** For each candidate site set and each size, the
   piece's own accuracy is computed: a fresh straight-line read given only
   the state's coordinates inside the piece, **at the action position**, on
   the same development episodes and the same split as the whole read; for a
   site set with more than one layer, the worst layer's. **A size is a
   candidate only if its piece is right on at least four fifths of the
   held-out episodes** (on the toy, 144 of 180). An arm and seed with site
   sets that clear the whole-state floor and no size that reaches four fifths
   returns "no verdict, read failed its floor". The alternative that was put
   to John and not taken: fixing the size at 8 directions with the smaller
   sizes as extra rows. **The requirement is applied after the layer set is
   chosen (item 4), so it decides which sizes may be chosen and never changes
   which layers are used (ruled 2026-10-03, late evening, ruling 2).** The
   re-run's method had marked that as its own reading, for John to overturn
   (`docs/controls-rerun-method-2026-10-03.md`, rule 7; the check at
   `e184a6e`, section 4, item 6); he confirmed it. The alternative that was
   put and not taken: letting the piece's accuracy also decide between layer
   sets, which has not been run. **Reconciled 2026-10-03 (night): what this
   order can miss, stated as the ruling requires.** The earliest layers at
   which the whole-state transplant works need not be layers at which the
   label can be read where the model acts. A model whose label is readable
   only at later layers returns "no verdict, read failed its floor" although
   a later layer might have passed. The report for the first full-size
   free-model run prints the accuracy at every layer and the candidates the
   rule chose among (section 11), so such a miss is visible when John rules
   at that stop (`docs/rulings/2026-10-03-version-4-questions-rulings.md`,
   ruling 2; `docs/rulings/2026-10-03-seven-questions-reconciliation.md`).

   **The piece's accuracy at the other positions of its site: reported both
   ways, gated in neither (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3, and
   `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`,
   ruling 2).** Where the chosen site set covers more than the action
   position, the same directions are transplanted at every position of it,
   and the four fifths above was established at one of them. So the
   reporting table prints, beside the piece's count at the action position,
   **(i) its count at each other position of the site, and (ii) its count on
   the average over those positions.** Neither has a pass line; the rule is
   unchanged. Each is computed as the short pre-stated run's method states
   (`docs/2026-10-03-short-prestated-run-method.md` at `9e978d9`, section 4):
   - **A count at a position** is computed exactly as at the action position,
     with only the position changed: the model's state at that position on
     the development episodes, its coordinates inside the piece, **a fresh
     read fitted at that position** on the same split, and the number of
     held-out episodes it gets right. It is not the action-position read
     carried over. The same count for the whole state at that position is
     printed beside it, so that a low piece figure can be told apart from a
     position where the label is not in the state at all.
   - **Which positions are reported one by one.** For the action position and
     the token before it: that one position. For the action position and the
     three before it: each of the three. For a site that runs from the
     model's first own turn to the action, whose length differs from episode
     to episode: **the five tokens of the model's first own turn, and the
     five tokens before the action**; the positions between them do not line
     up from one episode to the next and **are covered by the average only**.
     A site at the action position alone is printed as "single position".
   - **The count on the average** is the same count taken on the state
     averaged over every position of the site except the action position.
     **In the registered code that average is taken in 64-bit arithmetic.**
     The reason is the check of the short run, finding 11: on the toy, the
     same average of the same numbers added up in a different order moved the
     count by one episode of 180 on three of the eight figures (arm F seed
     0's whole state, 90 against 91; arm F seed 2's, 74 against 73; arm M
     seed 0's piece, 164 against 163), and in 64-bit arm F seed 0 gives 92
     and 24. The check offered two ways to deal with it, saying the figure is
     good to an episode or two, or fixing the arithmetic; this draft does
     both, and the choice of 64-bit is this draft's. **The toy figures on the
     average quoted in this version are therefore good to an episode or
     two.** The per-position counts did not move.
   - For a site set with more than one layer, the worst layer's figure.
   - **How much of a span the ten named positions cover:** a span from the
     first own turn to the action runs 16 to 53 positions on the toy, 39.2 on
     average, so the ten positions reported one by one are about a quarter of
     it, and the rest is seen only through the average (the check of the
     short run, finding 14).

   **This computation rests on John's own words.** The evening ruling
   recorded it as ruled from "print both figures", which accepts it by
   implication only; the check of that record said so (its finding 19), John
   was asked, and he answered "Yes, section 4 of the method is what I meant"
   (a dated note beside item 3 of the ruling record, main line at `53c8100`).

   *What the toy shows (MEASURED, **checked: the check of the short run at `53c8100`**:
   `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 4, from
   `out-short-prestated-run/part_b.json`; each cell is whole state then
   piece, right of 180).* Arm T on every seed and arm C seed 0: single
   position. Arm C seed 1: 180 and 139, 179 and 139, 179 and 33 at one, two
   and three positions before the action; 179 and 113 on the average. Arm C
   seed 2: the piece between 30 and 139 at the ten positions, the whole state
   between 149 and 180; 180 and 123 on the average. Arm M: the piece at 144
   or more at four, four and seven of the ten positions on seeds 0, 1 and 2,
   and as low as 34, 71 and 33 at the fourth token of the first own turn;
   180 and 163, 180 and 174, 180 and 175 on the average. Arm F, described
   only: the piece between 11 and 36 everywhere except the first token of
   the first own turn on seed 2 (145), which is the model's own marker word
   itself. The action-position counts recomputed by that run equal the
   controls re-run's on all twelve. **A limit of these figures, from the
   run's own findings:** each is a fresh read fitted on 420 episodes with
   twelve possible answers, in a piece of 4 or 8 directions; a figure like
   139 against 144 is a few episodes and should not be read finely. **A nominated site set's fit, for the floor of item 1, is the
   fit of the worst layer in the set**, as the re-run's verdict code reports
   it; on the toy no nomination has more than one layer, so this has not yet
   bitten. **What is not the registered read:** a read fitted per site set,
   with the states of every layer and every position in the set laid end to
   end and a multi-position span averaged over its positions, which is what
   the route (b) label search fitted (its `site_features`). That is a
   different quantity, it can score far higher on the same models (0.556
   against 0.172 on arm F seed 0, item 1), and nothing in this design uses it
   (the label-search check at `ecd2b6c`, section 2, which traced both reads
   through the code).
4. **The layer set for the whole-state transplant: "the smallest that clears
   the floor", in one reading** (ruled, the repairs rulings, item 4). For each
   position set, the layer set with the fewest layers that clears the
   four-fifths floor of section 6.4, ties going to the earliest layers; a
   position set with no clearing layer set drops out. The other reading, the
   highest ownership-only share over every clearing site set, is computed and
   printed beside it as a sensitivity row, **and that repairs-style row is the
   sensitivity row this version means** (the check at `70be9fb`, section 4.3,
   asked for the row to be named). On the repairs run's 44-set family the two
   readings picked different site sets on **8 of 12 arm-and-seed pairs, and
   the ownership-only shares they reached differed on 7 of 12**, by 0.02 or
   less (MEASURED: the Gate C review, RT-218, which resolved version 2's two
   counts; the repairs rulings' annotation 3, which adds that the check's
   re-run gave 6 of 12, so about half the pairs, by about 0.02, is what both
   runs support). On the re-run's 60-set family, no primary nomination is a
   multi-layer set, and the sensitivity reading picks a multi-layer set on five
   of twelve pairs (MEASURED: the re-run findings at `9d9d31a`, Part 2, first
   pass, section 5). The ruling's condition, that a nomination moving to a
   multi-layer set the hand list never tried be reported, did not fire.
5. **Nominate by causal effect, not by how well the read fits.** Over the
   surviving (position set, its smallest clearing layer set) pairs and the
   sizes whose piece clears the floor (item 3), the nominated configuration
   is the one with the highest *development-set ownership-only transplant
   accuracy*; ties go to the smaller size, then the earlier position set.
   This is the main lesson of the closed design: a representation that a
   straight-line read recovers beautifully can do nothing when you intervene
   on it. **What changed on 2026-10-03:** version 3 applied the fit floor to
   the nominated configuration afterwards; under the piece rule the floor is
   applied before the choice, as a limit on which sizes may be chosen. Among
   the sizes that pass, the choice is still blind to how well any read fits.
   **On an arm where nothing moves the action, that choice is made among
   sampling noise, and the registration says so** (the review of version 3,
   RT-230 and RT-235): on arm C the development shares at different sizes and
   sites differ by one or two episodes of 600, and on seed 1 one episode
   decided the site (section 5.2). What the piece rule secures is that
   whichever candidate wins, its piece holds the label at the action
   position. It does not make the pick stable.
6. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
   procedure and not just the arithmetic at the end. The reading obtained by
   handing the procedure arm T's true slot, and arm M's, is computed and
   reported separately as a reference; on arm M that reference is the formula
   of section 5.3 written in route accuracies, one check and not two (the Gate
   C rulings, RT-223). On the toy the true-slot reading is 0.0000 on arm T
   and 0.4837, 0.4760 and 0.4920 on arm M (the controls re-run at `821f154`,
   section 4). Ruled 2026-09-25 (decision 1).
7. **The rider, in the reporting table** (ruled: John's addition, the queue
   ruling, page 3; kept in the table by the repairs rulings). For every arm
   and seed, the reading is also taken at **arm T's** nominated site set and
   rank for the same seed, using that arm's own read fitted at those sites,
   and reported beside the reading at the arm's own nomination, so a reader
   can see whether what differs between arms is their degree or where the
   procedure looked. **Where the whole-state transplant at arm T's site set
   misses the floor, the rider returns "no verdict", and the report says
   which of two things that means.** On the toy it returned no verdict for
   arms C, F and M on every seed, for two different reasons (ruled, the Gate C
   rulings, RT-225): on arms C and F, at layer 0 at the action position,
   nothing about ownership has yet reached those arms' running states, and
   the whole-state transplant lands on the no-transplant rate (0.0512 to
   0.0600 on arm C, 0.0563 to 0.0688 on arm F); on arm M, which carries arm
   T's slot, the whole-state transplant there moves the action in about 0.41
   of trials against about 0.01 untouched, and the no verdict is **a miss of
   the four-fifths floor**, not nothing reaching the state (MEASURED: the
   repairs findings at `882f252`, section 3, "The rider"; the Gate C review,
   RT-225; the repairs rulings' annotation 5). Arm T's site set is layer 0 at
   the action position on every seed under the registered rule, the same site
   the repairs run nominated, so these rider figures stand under the rule,
   and the controls re-run found them again: the whole-state share at arm T's
   site is 0.0512, 0.0488 and 0.0600 on arm C, 0.0587, 0.0563 and 0.0688 on
   arm F, each the no-transplant rate, and 0.4088, 0.4138 and 0.4100 on arm M
   (the controls re-run at `821f154`, section 2, the last column).

### 7.3 Controls

Every one of these is run on every arm. **Three of them hold**, and a failure
means the reading is not made for that arm and seed: control 7 (the null
transplant), control 1 on arm T only, and control 4 (the too-early-position
control, as redefined on 2026-10-03). **The rest are reported** beside the
reading and cannot veto it. Version 2 made control 3 hold as well, and
version 3 made control 4 reported; this version does neither, for the reasons
under items 3 and 4. **The registered code withholds a reading when a control
that holds fails; it does not only print true or false** (section 6.4, item
5).

**All of them now have figures under the registered rules.** Version 3 had
none for controls 1, 2, 4 and 6 on arms C, F and M at the site sets the rule
nominates, and the review of version 3 made that a precondition of the
registration review (RT-233; ruled 2026-10-03, page 2). The controls re-run
of 2026-10-03 ran controls 1, 3, 4, 6 and 7, the true-slot reference, the
rider and the stricter row on all twelve toy models, with its method and code
committed before its output (`docs/2026-10-03-controls-rerun.md` at
`821f154`); a session that did not run it ran it again from the committed
code and found every one of about 26,700 values equal (the check at
`e184a6e`, section 3). Control 2 has no figure and cannot have one at toy
scale (item 2). Arm F's figures are taken at the site the rule would choose
with the piece requirement switched off and are labelled "reported for
description; no reading" (the re-run's method, rule 12).

===== END OF RECORD 4, part 5 =====

