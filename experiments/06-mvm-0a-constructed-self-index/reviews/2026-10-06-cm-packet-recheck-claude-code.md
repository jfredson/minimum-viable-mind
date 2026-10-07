# Re-check of the revised ruling packet on arms C and M (pull request 109)

*Written 2026-10-06 (Pacific) by the session that wrote the first check
(`2026-10-06-cm-packet-check-claude-code.md`, same folder). It covers the
revised packet at commits `8367c13` (applying the eight findings) and
`2db4435` (tightening page 1), and the revised pull request text. $0: nothing
run beyond reading and counting days; no project code changed. The same
sources as the first check (its method, `docs/2026-10-06-cm-packet-check-method.md`).*

## Verdict

**Ready to rule from.** All eight findings are fixed. Nothing is presented as
ruled. Two small wording points remain. Neither changes a figure John would
rule on, and both can be corrected in place.

## The eight findings

| Finding | Fixed? | Where |
|---|---|---|
| 1. "10-million-step" wording; 30-million registered size | yes: "10-million-parameter models, each trained for 108,919 steps" in the header and the pull request text; "10-million-parameter" on page 1 and page 12; 30 million stated twice | lines 7 to 11, 26, 72 to 73 |
| 2. Decay argument by size, not sign | yes, with one overstatement (point A below) | lines 36 to 39 |
| 3. Option 2 as its source had it; floor option | yes: option 2 is now exemption plus a minimum check; option 3 is "learned, never below a minimum" | table rows 2 and 3 |
| 4. Whether arm T is included | yes: 1(a) $0.81, 1(b) $1.14 plus re-reading arm T. Checked: $0.3341 + $0.4744 = $0.8085; plus arm T $0.3347 = $1.1432 (ledger rows, pull request 98) | table row 1 |
| 5. Time cost; option 5 is version 4's plan; drops arm M | yes, with one wording slip (point B below). "Rather than a repair" is quoted correctly from W3; dropping arm M matches version 4, section 9 | table row 5, lines 56, 60 to 64 |
| 6. Toy trend; one seed | yes: toy arm C 1.73, 0.70, 0.93; arm T fell to 1.95; one seed each | lines 33 to 36 |
| 7. Page 12: John's words; decoy-test limit | yes: John's words quoted exactly from the rulings record (pull request 103); the condition is "continue if not fooled"; the exact-copy limit matches pull request 108; it says plainly that it "changes the condition you endorsed" | lines 66 to 74 |
| 8. Deadline timer is the cost backstop | yes: "deletes it if it reaches its spending cap: the last line of defence"; stops "only on a confirmed deletion ... never on a failed or empty reading" | lines 107 to 114 |

The newly explained terms are right: the pass mark of 144 is four fifths of
180; "frozen" is the code fixed and tested on 2026-10-04; the $8.53 is left of
the $10 approved for development runs; "blocks of spending you approved in
advance" for the two releases; the alarm's ratio is "spending divided by what
the posted rate predicts (1.0 means billed as posted)"; the decoy test is
glossed correctly. "Registration" is still not glossed, which is minor
because John uses the word himself.

Nothing is presented as ruled. The only ruled items cited are ruled: the
2026-09-20 fallback, the page 12 deferral and its wording, and sections 12.5
and 12.7 of version 4. "A correction" on page 2 is the packet's own proposed
classification, and it says those fixes need John's go.

## Two remaining wording points

**A. "So decay explains about two-thirds of the fall" (line 39).** This
overstates what the arithmetic shows. Decay alone would have taken the
sharpness from 4.0 to about 1.34, which is about two-thirds of the way down.
But decay and the training pressure act together, and arm T, under the same
decay, kept 1.95, so the share of the fall that decay "explains" cannot be
read off. The pull request text has it right ("Weight decay alone would have
left it at about 1.34; training pushed it the rest of the way"). *Correction:*
replace the clause with "decay alone accounts for a fall to about 1.34 at
most, and cannot take it to zero, so training pushed it there."

**B. "Several working days of the twelve left" (line 63).** Twelve is
calendar days, not working days: 2026-10-07 to 2026-10-18 is twelve days, of
which eight are weekdays (10-18 is a Sunday). *Correction:* "several working
days, of the twelve calendar days left before the registration deadline
(2026-10-18)". "Several working days" itself is the author's estimate and is
labelled as one, which is fair.

## Nothing else new

The rest of the packet was re-read against the sources:
- the sharpness values, 41 and 45 of 180, 0.40 against 0.99, $1.46 against
  $1.47, 29 minutes;
- $194 to $206, the deadline, and sections 12.5 and 12.7.

No new errors.
