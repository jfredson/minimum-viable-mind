# Ruling 2026-09-25: the Weekend 1 queue of registration-blocking decisions, nine pages ruled

*Recorded 2026-09-25 (Pacific), in a Cowork planning session. The file keeps the
name the weekend roadmap, the proposal packet and the Weekend 1 session prompts
all point at (`docs/rulings/2026-09-26-weekend-1-queue.md`); the rulings were
made a day earlier than planned, on the evening of 2026-09-25, under the
roadmap's clause that a Friday evening with three hours moves Saturday's queue a
day earlier (`docs/weekend-roadmap-2026-09-24.md`, section 7). Mixed authorship:
every recommendation was proposed by the session that wrote
`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md` (checked on pull request
35), each page was put to John in plain language with its strongest argument
against, and he chose. The choices are his; none of the wording is his drafting.
No compute was launched and no money was spent under this ruling.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).
Every number below is the proposal packet's, which cites the committed file each
one was read from; none is new. Nothing here edits registered text, a protocol
file or an earlier ruling file; where an earlier ruling is affected, the change
is a dated annotation beside it, as its own preamble allows.*

---

## What was ruled

John's words, in order, on 2026-09-25: page 1, "Agreed on all 8"; page 2,
"Agreed"; page 3, "Agree, and yes to the rider"; page 4, "Agree" (to both
questions put); page 5, "Agree"; page 6, "Sure that works" (to the three parts
put); page 7, "yes"; page 8, "yes" (to option (i) on both items); page 9,
"Agree" was not spoken as a go; the go itself is separate, see page 9.

### Page 1 — the eight numbers. Ruled as recommended, all eight.

- **1a.** Separation bar 0.5: the minimum gap between the entangled arm's
  reading and the separable arm's reading, on the chance-corrected form
  page 2 registers.
- **1b.** Learn-both threshold, per condition: the rehearsal's pre-stated cell,
  above the one-in-four level at the 0.05 level under a binomial test on at
  least two seeds of three (0.2630 on 3,000 held-out episodes, or the same rule
  at the registered episode count). The ownership-blind and name-only solvers
  are reported beside it as references, not thresholds.
- **1c.** Whole-state transplant floor: four fifths of the arm's own
  own-directed accuracy on the same fresh episodes; the whole-state layer set
  is the smallest that clears it; the set of every layer at every position is
  excluded by name.
- **1d.** Rank cap 8 on every arm, with the search family reporting caps 1, 2,
  4 and 8.
- **1e.** The candidate site list is registered as the rule that generates it
  (the action position and the positions between the source assignment and the
  action; all contiguous layer sets; one label, which marker word, per the
  ruling of 2026-09-23), the degenerate all-sites set excluded; the registration
  prints the list the rule produces for the registered 12-layer architecture,
  with the toy's count (176 comparisons per arm and seed) beside it.
- **1f.** Three seeds per arm; the registration says in terms that the toy
  arithmetic implying one seed was not carried across.
- **1g.** Across-seed spread of the raw difference as the registered
  uncertainty, the within-seed bootstrap reported beside it, and the
  registration says neither method measures drift between runs of one seed.
- **1h.** Lesion collapse: own-directed accuracy falls below the 1b bar; the
  named-other clause is reported and not gated; the ownership-free batteries
  must hold. Gates arm F only, as proposal section 8.2 has it.

*Changes:* successor proposal version 2, sections 6.4, 7.2, 7.4, 8.1, 8.2.

### Page 2 — the form of the reading. Ruled: the chance-corrected form.

`(accuracy_whole − accuracy_ownership_only) / (accuracy_whole −
accuracy_untouched)`, with the raw difference and both accuracies always
reported beside it. The 1a bar and the 1c floor are written on this scale.
Proposal section 6.4's sentence "No normalisation by an ownership-blind ceiling
anywhere" is replaced in version 2 by a sentence that permits subtraction of the
measured no-transplant rate and nothing wider; the registered rule for that
rate carries room for the miss of up to 0.0175 the rehearsal measured.

*Changes:* proposal version 2, sections 6.3, 6.4, 7.4, and the no-transplant
sanity rule.

### Page 3 — one instrument for the nomination step. Ruled: option (i), plus the rider.

The label is fixed to which marker word in the code as well as the text (the
rehearsal code's label tuple; the successor's measurement code when written;
proposal section 7.2, item 2). The site set and rank stay one blind rule
applied identically to every arm, and the registration says in one sentence
that the rule's outputs differ per arm. **Rider, John's addition:** for every
arm, the registration also reports the reading at arm T's nominated site set
and rank beside the reading at the arm's own, so a reader can see whether what
differs between arms is their degree or where the procedure looked.

*Changes:* proposal version 2, section 7.2 and the reporting table; the
rehearsal code if re-run for the weekend's repairs.

### Page 4 — the named-other condition. Ruled: S1 did not fire; attempt (b) and (a), with (d) as the fallback.

Stop condition S1 did not fire: it asks whether the grammar is learnable at
tiny scale even in principle, and the separable arm learned both conditions to
1.0000. This is John's ruling, adopting the rehearsal's adjudication. This
weekend, at toy scale on the laptop at $0, session (c) attempts redesign (b),
a curriculum, and (a), loss re-weighting, alongside it if the laptop has the
hours, with the pass line pre-stated before the run: the named-other condition
above the 1b bar on at least two seeds of three on the free toy arm. If neither
clears it by Sunday 2026-09-27, (d) is ruled: the registration text records
that the named-other condition failed its bar on two of three toy arms, that
doubling the budget did not fix it, and that the staggered first run reads the
learn-both result of one free-arm run before the remaining eight are committed.

*Changes:* under (a) or (b), the rehearsal training recipe and proposal
section 5.4, with the rehearsal findings extended by a dated section; under
(d), a sentence beside the prior in section 3 and the gate in section 8.1.

### Page 5 — the middle of the scale. Ruled: option (iii).

The admission goes into the registration text regardless: a free-arm reading
at the entangled anchor cannot be told from the instrument's ceiling. A fourth,
partially separable arm is attempted at toy scale this weekend at $0, with its
predicted reading stated before it runs, and is folded into the main
registration only on the pre-stated pass: a chance-corrected reading between
0.3 and 0.7 on all three seeds. Otherwise it is carried as extension E0 on the
weekend roadmap, a separate registration later. If folded in, its three
registered runs ($32 to $44 at the ledger's per-run rows) come from the
envelope ruled on page 6.

*Changes:* proposal version 2, sections 3 and 13 (the admission); if the arm
passes, section 5, every arm table, rehearsal items R-2 and R-3, and section
12.4.

### Page 6 — spend. Ruled in three parts.

1. **The cap.** The flat successor cap of $130 in item 4 of
   `docs/rulings/2026-09-20-december-result-roadmap.md` is superseded by the
   two releases of `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`
   (items 10, 11 and 19, with the correction note of 2026-09-22: about $44
   and about $131). This sentence is the closure of RT-176. A dated annotation
   saying so goes beside item 4 of the 2026-09-20 ruling.
2. **The envelope.** The programme envelope is raised from $400 to **$450**.
   What it buys, on the ledger rows the packet cites: the base plan of about
   $175 on top of about $227.63 spent (about $402.63), plus one extension of
   $32 to $44 (page 5's fourth arm) or about $36 (E1 or E3), with $3 to $15
   left. It does not hold two extensions. The second release's number still
   waits on the rented slice's seconds per step, as item 11 says; this ruling
   changes the ceiling, not the gate.
3. **The tripwire.** Both ratios of the spending proposal's sections 5.3 and
   5.4 (billed hours over machine-existence hours; balance drawdown per hour
   over posted rate times machines running) are adopted at **1.25**. Either at
   or above 1.25 is a trip: halt, not trim; ledger row first; John told the
   number; every later launch needs his words. A check that cannot run is a
   trip. The pre-authorisation scheme of the spending proposal is not adopted
   by this ruling.

*Changes:* the annotation on the 2026-09-20 ruling; proposal version 2,
sections 12.2 and 12.4; the compute ledger's header (the stale "$200" line and
a new envelope line); `data/project.toml`; the tripwire written into the launch
preconditions beside the sleep guard and the argument guard.

### Page 7 — the Wittgenstein criteria. Ruled: option (ii).

Test 1's rationale (an internal variable belongs to the game only if
intervening on it changes what the model does) goes into proposal section 2 as
motivation, marked non-binding, citing the TimeAssembler note by its document
id. Tests 2 and 3 wait for resumption after May 2027; test 2 is named on the
weekend roadmap's extension list so it is not lost.

*Changes:* proposal version 2, section 2; weekend roadmap section 4, one line.

### Page 8 — two record corrections. Ruled: option (i) on both.

- **8a.** A dated note beside finding F17 in
  `experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`, in the form
  the file already carries, giving the measured counts (15, 15 and 7 top-level
  keys) and saying the 110 is unsupported; the original sentence untouched.
  Item 20 of the 2026-09-21 ruling is discharged.
- **8b.** Ratified in John's own words: a dated note naming a committed record,
  where no registered claim changes, is how a missing pointer in registered
  text is supplied, and nothing wider. The note already beside the
  cue-detector figure in `pre-registration.md` (commits `285903e`, `eeedb2f`,
  `57eb09d`) stands as filed. The TimeAssembler task is closed.

### Page 9 — the rented slice. Ruled: the shape and the order, option (i).

The go is spoken only after (1) a filed check of the regenerated plan file
(`experiments/rehearsal-successor-measure/out/rented-slice-plan.txt` at commit
`60d1496`) by a session that did not regenerate it, (2) the never-sleep
override on and the Mac on wall power with the lid open, and (3) in a shape
that names the plan by commit hash, the derived launcher
`launch_a3_fetch_first.sh`, the flags, the estimate ($0.75 to $1.00), the hard
cap ($2.00) and the override. The verbatim shape on page 9 of the proposal is
adopted. The plan check was commissioned as session "MVM W1f plan check" on
2026-09-25. **No go is issued by this file.** When spoken, the go is quoted in
the compute ledger row before anything is created.

---

## Two TimeAssembler tasks closed by earlier rulings, noted here

Per the packet's disagreement 8: "DECIDE (John): the entangled and free arms'
numbers are one sample, not a measurement" was answered by the ruling of
2026-09-23 (range and direction only); "DECIDE (John): how to correct a
measured value in REGISTERED text …" is page 8b above. Both close.

## What this file does not do

It does not edit the proposal (version 2 carries the changes), the 2026-09-20
ruling (annotated beside), the ledger, `red-team-a4.md`, `pre-registration.md`
or any protocol text. It issues no go. Under the pairing rule of
`docs/outside-review-protocol.md` it is checked by a session that did not write
it before sessions (c) and (d) rely on it.
