# Ruling: RT-283, the observer loss condition, closes on John's reading (2026-10-18)

*Recorded 2026-10-18 (Sunday, Pacific) by the Claude Code session that
worked the programme on 2026-10-17 and 2026-10-18 and put the question to
John. It wrote none of the Gate A pass, version 3 of section 2, the closure
checks or the ledger rows. Authorship **mixed**: the session recommended
closing on reading; the fifth master session for the tracker sites added
the condition on the observer study's rehearsal; John approved both, to the
master and then in this session's chat. Records only: nothing run, nothing
spent. Written under the workspace plain-language rule.*

## The question put to him

RT-283 is the fatal finding of the 2026-10-09 Gate A pass on the two-sided
question text: section 2 pre-stated a loss condition for the observer side,
that observers "track the fluency measures no better than chance", with no
instrument and no rehearsal, describing an option ruling 10 of 2026-10-07
had already closed. Version 3 of section 2 deleted that sentence. Its
closure check (`docs/reviews/2026-10-17-section-2-v3-closure-checks-claude-code.md`)
asks for `grep -c "no better than"` to return 0; it returns 1. The hit is
not the deleted sentence. It is the sixth loss condition of "How this
question loses", which RT-285's fix added: "the observer side's premise
fails if observers, blind to construction and never shown the battery's
readings, detect presence in the constructed systems no better than in the
frontier reference profile", followed by "Until the construction line
produces a system that can be read, this is a question and not a finding".
The question was whether that hit means the fault survives, or whether the
check closes on reading.

## The recommendation, as given

Close on reading. The finding was about pre-stating a threshold for an
option already ruled out. The surviving sentence is not that option,
carries no number, compares against the frontier reference profile and not
chance, is one of six loss conditions the reviewers themselves asked for
(RT-285), and is guarded in the text as a question and not a finding. The
alternative, rewording the sentence to avoid the phrase, would change
nothing of substance. The condition the master added: whenever the observer
study is designed (it is deferred by decision 7 of 2026-10-07), its
comparison, presence against the frontier reference profile, gets its
instrument and is rehearsed before it is registered, so the protocol's
rehearsal rule binds then.

## John's words

To the fifth master session, 2026-10-18, relayed to this session: "Ok
sounds good. Go ahead and close it."

In this session's chat, 2026-10-18: "RT-283 closes on reading: the
surviving sentence is a different comparison, guarded as a question and not
a finding. Record the count of 1 and why in the ledger row, with the
condition that the observer loss condition gets its instrument and
rehearsal when the observer study is designed."

## What is ruled

1. **RT-283 is closed, on John's reading, not on the letter of its check.**
   The ledger row says which of the two happened, as the closure rule asks:
   the claim was checked (the count is 1 against an expected 0), and the
   argument that the hit is a different sentence was accepted by John.
2. **The sentence stands** as the sixth loss condition, unchanged. Section 2
   as written into the spec is not edited.
3. **The condition:** when the observer study is designed, its comparison
   (presence against the frontier reference profile) gets an instrument and
   a measurement rehearsal before it is registered; until then the loss
   condition stays a question and not a finding, as its own text says.

## Added the same day: both copies

The pairing-rule check of the ledger rows found the same comparison stated a
second time, in the paragraph added to "What Would Count Against It": observers
"may detect no more presence in the constructed systems than in the frontier
reference profile". Put to John; his words, in this session's chat,
2026-10-18: "my RT-283 reading and its rehearsal condition cover both copies of
the observer comparison". So item 1 and the condition in item 3 cover both
sentences. In the same answer he ruled that the removal-test interval clause
in the Floor sentence is corrected before the spec merges (ledger row RT-292),
in his words: "fix the removal-test interval sentence in the spec before it
merges, with the wording you proposed". The wording proposed to him, and now
in the spec, is "the first and third intervals above zero and the second,
from 0.00 to 0.20, touching it". His whole answer: "Yes to both: my RT-283
reading and its rehearsal condition cover both copies of the observer
comparison, and fix the removal-test interval sentence in the spec before it
merges, with the wording you proposed."

## Where it lands

- This file, beside the ledger rows on pull request 173.
- The RT-283 row of `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`:
  its closure cell changes from open to closed on reading, with the count,
  the reason and the condition.
- A dated line in the note at the head of
  `docs/rulings/2026-10-12-two-sided-question-section-2-v3.md`.
- `STATUS.md` and `data/project.toml` when pull request 173 lands; the
  TimeAssembler worklog as a decision entry with authorship mixed.
