# Proposal: the design and first copy of the Minimum Viable Mind tracker

*Written 2026-11-20 by a working session, for John to rule on. **Ruled by John the same day: all six
decisions in section 7, as leaned, with one change to the line above the title** (section 7 has his
words). Two facts changed after it was written: the six decisions are ruled, and the first list of
theories now has ten entries (nine theories plus the Sentient Horizons account; John raised this
tracker's limit to ten). The pictures were not redrawn and still show eight invented rows. Nothing is
built, deployed, merged or pushed. The pictures are in `2026-11-20-tracker-design-proposal/` beside this file. They are static
mock pages, rendered in a browser and captured at 1280 pixels wide (desktop) and 390 (phone), in
both themes. The mock pages themselves and the script that writes them are in that folder's
`mock/` subfolder, so they can be reopened and changed.*

**Every theory name and every number in the pictures is invented.** No theory has been scored, and
the theory list is not settled. Each picture carries a striped banner saying so, and every
invented number has a dotted underline. "Relay theory", "Lantern theory", "Echo theory", "Tide
theory", "Mirror theory", "Loom theory" and "Threshold theory" are made-up names standing in for
real theories. The Sentient Horizons account appears under its own name because the first screen
has to show where the site's own account sits; its bars are invented too. This document states no
fact about any real theory or study.

## 1. What this is for

The kickoff proposal (`docs/2026-11-20-consciousness-tracker-kickoff-proposal.md`, in the
three-hypotheses working copy, not yet on main) turns Minimum Viable Mind into a public tracker. It
ranks the active theories of consciousness, the Sentient Horizons account among them, on three
scores: how well published studies back each one (support), how sharply it is stated so that a
study could prove it wrong (testability), and how much of it no study has touched (left to test).
John has ruled the scoring rules and the ranking rules (kickoff section 4). The site today is a
programme log on the "Notebook" skin, ruled 2026-10-17. This proposal answers the questions the
kickoff leaves for design:

1. what the first screen holds, in the tracker pattern's order;
2. what a theory's page, a prediction's page and the three side sections look like;
3. what to keep from Notebook and what to replace, and why;
4. two or three directions, with a lean;
5. draft copy for the first screen and the About page.

The design standard and the tracker pattern this follows are in `sentient-horizons/design/`
(`README.md`, `tracker-pattern.md`, `lessons.md`), read on `origin/master` on 2026-11-20.

## 2. What I took from the sibling sites

Looked at on 2026-11-20 in a browser, at 1280 pixels wide.

| site | what its first screen does | what this site takes from it |
|---|---|---|
| [The Belt Equation](https://beltequation.com) | one huge number, the question under it as the title, one control (the year dial), the latest news on the right | the reference order of the first screen (pattern rule 1.3); the monospace for the number |
| [The Quiet Galaxy](https://thequietgalaxy.com) | the question first ("Where is everybody?"), the equation's seven factors drawn as a row beneath, the number in a card on the right | **the main lesson here:** when the thing to hold is a set of parts, not one number, the parts can take the left column and the number can sit in a card on the right |
| [The Upgrade Tree](https://theupgradetree.com) | the count "28 of 35" big, a five-number breakdown row, the human figure on the right | a count with its parts beside it; the figure as the clickable picture of the branches |
| [Outrunning Ageing](https://outrunningageing.com) | a year, a range, the chart of the spread on the right | showing how much a number rests on, beside the number |
| [The AGI Zeitgeist](https://agizeitgeist.com) | the share first, then the answer ("Not yet."), with four gauge bars | bars measured against a fixed line, with the line drawn on the bar (its red tick); the answer before the question is allowed where the answer leads |
| [Beyond the Window](https://beyondthewindow.org) | a sentence as the headline, a row of developer boxes, the record in one column | that a tracker with several things to compare can lead with a table instead of one big number |
| [Minimum Viable Mind today](https://minimumviablemind.sentient-horizons.com) (pictures 1 and 2) | "3 of 8" stages delivered, a long paragraph in the first person, an at-a-glance box of days, findings, decisions waiting and spend | the paper, the grid and the monospace labels hold up well; the first screen's content belongs to the project's own tests now, not to the site's front |

The pattern is the same everywhere: one thing to hold on the left, large; the question as the
title; a paragraph for a stranger; the last-checked line; two buttons; the latest news on the
right. The question for this site is what "the thing to hold" is. The kickoff says it is the
ranking, with the headline number beside it (kickoff section 3).

## 3. The first screen (pictures 3 to 7)

In the lean, top to bottom on the left:

1. **The line above the title**, the kickoff's draft as written: "**What is the least a mind
   needs?** Every theory of consciousness gives an answer. Here is how each is holding up." It
   sits where the eyebrow sits on the other trackers, set larger than an eyebrow (16-pixel sans,
   the question in bold) because it is a sentence, not a label. It is what says the subject to a
   stranger, since the name does not (kickoff section 11).
2. **The question as the title:** "How far has the science of consciousness got in testing its
   theories?" (the trunk question from kickoff section 3, still ruling 3).

   *Ruled 2026-11-20, after this was written:* the line above the title now reads "What is the least
   a mind needs? Every theory of consciousness gives an answer. Here is how ten of them are holding
   up." The number comes from the records at build time and is never typed in (section 7, decision 6).
3. **The ranking**, in its three ruled groups, one row per theory, three bars per row:
   - **Ranked.** Past the bar, with a support score, highest support first. A rank shared under
     rule 5 shows as "=1" for both theories, a thin rule joins the two rows, and one line under
     them says "Shown as tied: one study going the other way would swap these two." A theory the
     evidence goes against keeps its place and carries "the evidence so far leans against it"
     (rule 6; the invented Tide theory).
   - **Testable, too little tested to rank.** Support shows as "none" on a dashed empty track,
     with the reason: "no studies yet from two separate groups". The Sentient Horizons account is
     drawn here with a small "this site's own" tag, which is the kickoff's own first guess and
     not a score.
   - **Not yet defined sharply enough to rank.** Each row says what it needs, for example "needs:
     a prediction that could fail for 2 more of its 5 core claims".
4. **"Read it this way"**, one line under the ranking: the order is set by the first bar only; the
   second gets a theory in; the third says where the work is and a long one is not a fault; the
   three are never added up.

On the right, top to bottom: the **headline card**, the **paragraph for a newcomer**, the
**last-checked line**, the **two buttons**, then the **latest news** (pattern rule 4.22). On a
phone the headline card moves up to sit between the title and the ranking (picture 6), so the
number is not left below eight rows of bars.

**The three bars are drawn differently on purpose**, all in the data colour (the slate), since
the standard allows no colour by meaning except yes and no:

- *How well the evidence backs it* is drawn from a centre line at 50, the even point. The fill
  runs right from the centre when the evidence leans for, and left when it leans against. A plain
  fill from zero would make 50, "even", look like half a success.
- *How sharply it is defined* is a plain fill from zero.
- *How much is left to test* is hatched, not solid, so it reads as work ahead rather than as an
  amount of something good or bad.

Each bar has its number beside it in monospace on desktop. On a phone each row gives its three
bars a line each, labelled "backed", "sharp" and "left to test".

**The headline is a placeholder.** It is not ruled (kickoff ruling 3). The card shows "18%", marked
"placeholder · not ruled", for what the kickoff proposes it holds: **the share of the theories'
sharp predictions that have been put to a test at all**, across every theory on the site, with
its count under it ("41 of 228 predictions · 8 theories", invented). It would be worked out from
the prediction records by the same build step that scores the theories, and written to the
site's headline file (pattern rule 1.6). If John rules a different headline, the card holds it
unchanged in shape; nothing else on the screen depends on it.

## 4. The inner pages

**A theory's page** (pictures 8, 9, 10). The plain name and one paragraph; the three scores as
three boxes, each with its number, a sentence saying what it rests on ("14 studies from 6
groups, total weight 31", "4 of 5 core claims come with a prediction that could fail") and its
bar; the tie note with a link to check it by hand. Then **its core claims**, quoted from the one
named publication (ruled), each with a dot: filled when a proponent states a prediction that could
fail, half filled when only the site has inferred one, empty when nobody has. The dots are the
testability score made visible, and they show the ranking's bar directly: a theory is ranked when
more than half its dots are filled. Then **its predictions**, the ones that separate it from a
rival, with who says so, the state as a badge (supported and contradicted in the standard's yes
and no colours, mixed dashed, untested muted) and the study count. A later rescue is its own row,
marked "the loss above stands" (rule 4). Under the table, one line links the studies "explained
afterwards, not counted" (the stage 1 rule). On the right: **what would move this** (pattern rule
2.3), computed from the rules ("a study by an outside group on the fourth prediction, registered in
advance: 68 → 72 if it came out for, 68 → 61 against"); support run by run as a small chart with
the 50 line dotted; the last readings; the disagree link.

**A prediction's page** (pictures 11, 12). The prediction as the title; one plain paragraph;
**counts for it / counts against it** side by side, written before any study was read; then four
facts in a list: whose it is (with the first dated statement, and full or half weight), whether
it separates theories (naming which rival predicts otherwise), who settles it, and its state with
a date. Then **the studies**, each with its outcome, its four protections written out with the
ones it has in full ink ("registered · outside group · rival agreed · replicated"), its weight
from 1 to 5, and what the two readers said. A study the readers disagree on shows "waiting", and
a study that came before the prediction was on record shows "explained afterwards, not counted",
with weight 0. Then its dated record. On the right: a plain note on the two readers, the open
questions it bears on, the last readings, and the disagree link.

**The open questions** (picture 13). The five questions from kickoff section 3, each with one
plain line, how many predictions bear on it and how many are tested, a thin stacked bar (tested
one way, tested mixed, not yet tested), and on the right each theory's answer in a line. The
eyebrow says "Beside the ranking · moves no score" (pattern rule 1.2).

**Our working positions, against the evidence** (pictures 14, 15). The page opens with the plain
notice that this site ranks its author's own account, and what is done about it: the rules were
written before any theory was scored, an outside reader judges first on every row of this account,
and a result against it stands. Then each working position, its "What would change my mind" as
published, and a badge on the right: evidence has gone its way, against it, mixed, or none yet,
with what it rests on. The positions' wording in the pictures is placeholder; the built page quotes
the public Working Positions page.

**Our own tests** (pictures 16, 17). What Minimum Viable Mind does today, moved to one side: one
paragraph, then the project's three habits as three small boxes (registered first; measured or
argued; spending capped), then the tests as a table with what each bears on and its result. On
the right, where the project stands (stages, the pause from 2027-01-04) and the spend. The present
site's ladder, learned and story pages would live under this page, at their present addresses.

**The top bar** (pattern rule 4.21): Theories · Questions · Our Positions · Our Tests · News · About
| Family. It holds one row at 1280 pixels. This week's reading, disagree and the source go in the
footer, as on the other trackers.

## 5. Notebook: what to keep and what to replace

The Notebook proposal of 2026-10-17 (`sentient-horizons/design/proposals/minimum-viable-mind-skin-2026-10-17.md`)
rested its choices on two facts. It said Minimum Viable Mind "is not a tracker and not an essay"
but a programme log, so the look should say "a record kept by instrument". And it said the site
"is the parent's own programme", so its accent should be the parent's ink violet rather than a
colour of its own. **The first fact has changed in a way that keeps the look; the second has
changed in a way that undoes the accent.**

**Keep, with the reason:**

- **The cool paper, light by default, and the graphite dark theme.** A site that scores theories
  against studies is read like a results table, in daylight. Nothing about the new subject asks
  for a sky, and the family already has two sky sites.
- **The graph-paper grid behind the first screen.** It says "measured" without a word, and a
  ranking set on squared paper reads as a results sheet. It costs two gradient lines.
- **The monospace on every label and number.** The site's whole claim is that its numbers are
  worked out by fixed rules; the instrument's typeface says so.
- **The slate as the data colour**, for every bar. It is quiet enough that eight rows of three
  bars do not shout.
- **No display typeface.** Nothing in the new subject needs one.

**Replace, with the reason:**

- **The accent: from the parent's ink violet to a colour of the site's own.** The violet was
  chosen because the site belonged to the parent. The site now ranks the parent's own account as
  one rival among several, and says on its first screen that it does so by the same rules. An
  accent borrowed from the parent ties the whole page, every link and button, to one of the
  contestants. The lean's replacement is a **mulberry** (`#8e2f63` on paper, `#e9a6c8` on
  graphite), a hue no other family site uses (read from the six sibling skins on 2026-11-20: rust,
  ice-blue, plate green, clinical blue, glass green, newsprint red). Its contrast against the page
  is 7.0 in light and 9.2 in dark. It is still only for links and the one action; the data stays
  slate.
- **The first screen's object: from the count of the project's stages and the at-a-glance box to
  the ranking.** That is content, not skin; it follows from the kickoff.
- **The tone of the front page: from the first person to the site's voice.** Today's first screen
  opens "On 2026-10-23 I revised the theory...". A ranking that includes the author's account
  reads more fairly in the third person ("this site's own"), with the first person kept for the
  positions page, where it is the author's to speak.

## 6. The directions

Three, with my lean marked. All three use the same pages and the same ranking component; they
differ in the skin and in what leads the first screen.

### Direction A: Notebook kept as ruled (pictures 18, 19)

The skin of 2026-10-17 unchanged, the violet included, with the new pages. **For:** no skin
change to rule, and it was ruled a month ago. **Against:** the accent's reason no longer holds
(section 5), and the site that ranks the parent's account wears the parent's colour.

### Direction B, my lean: Notebook re-inked, ranking first (pictures 3 to 17)

Notebook with one token family changed (the accent to mulberry), and the first screen led by the
ranking in the left column, the headline in a card on the right, as The Quiet Galaxy leads with its
seven factors and puts its number in a card.

**Its weakest step: the ranking comes after the title, not before it.** Pattern rule 1.3 puts the
thing to hold first and the question second (the Belt Equation's big number above its question).
A table of eight rows does not read without its question above it, so the lean puts the title
first, which is the AGI Zeitgeist's allowed order turned around. It needs John's ruling as a
departure from rule 1.3. The second weakness: on a 1280 by 800 screen only the first four rows of
the ranking are above the fold, so a reader sees the "Ranked" group whole but has to scroll for the
other two groups (picture 3; picture 5 has the whole page). The pictures show eight rows; the first
list now has ten, so the fold check has to be redone with ten rows once the page is built.

**The same skin, number first** (pictures 20, 21) is the variant that follows rule 1.3 exactly: the
headline huge on the left, the ranking squeezed into the right-hand card with no numbers. It
matches the siblings most closely. I set it aside for two reasons that the pictures show. The
ranking, which is what a reader came for, shrinks to bars too small to compare and names that wrap
onto two lines. And the face of the site becomes the one number that is not yet ruled and is
expected to start low, so a stranger's first reading would be "18%: of what?" before they know
the site ranks theories at all.

### Direction C: Dark room (pictures 22 to 25)

A new skin, dark by default: a near-black neutral field, one small cross at the left of the first
screen like the cross a person fixes their eyes on in a perception test, a pale phosphor
yellow-green accent (`#c8d46a`), the slate kept for data; the light theme is "the lights up", a
grey page with an olive accent. **For:** it is the most distinctive of the three, and dark suits the
subject's mood. **Against, and why it is not the lean:** the family's dark sites are its skies (The
Belt Equation, The Quiet Galaxy) and the parent's Deep Field, so a dark Minimum Viable Mind would
read either as a third sky site or as the parent, the second of which is the same problem the
violet has. A dark, hushed look also leans toward mystery on a site whose rule is to calibrate
between inflating and dismissing. And the cross is too small to carry a skin on its own.

## 7. Decisions for John (all six ruled 2026-11-20)

John ruled on all six the same day, through the master session. Each is marked *(ruled)* with his
words; the wording of each row is this session's.

| # | The choice | Lean | Strongest alternative, and its cost | Ruling |
|---|---|---|---|---|
| 1 | The skin | **B: Notebook re-inked**, the accent changed to mulberry, everything else kept | A: Notebook as ruled; no new skin ruling, and the site wears the colour of one of the theories it ranks | *(ruled)* "Yes, re-inked" |
| 2 | What leads the first screen | **The ranking, under the title, the headline in a card on the right** (a departure from pattern rule 1.3) | Number first, as the siblings do; follows the rule exactly, and shrinks the ranking to a sidebar and leads with an unruled number | *(ruled)* "Yes, ranking first" |
| 3 | How the three bars are drawn | **Support from a centre line at 50; testability a plain fill; left to test hatched; all in the data colour** | Three plain fills; simpler, and "even" then looks like half a success, while "left to test" looks like a score to be proud of | *(ruled)* "Yes, as drawn" |
| 4 | Where the own account sits on the first screen | **In its group by the rules, tagged "this site's own", and named in the newcomer paragraph** | Pinned in a row of its own above the ranking; more visible, and a special place for the author's own account is exactly what the rules refuse it | *(ruled)* "Yes, in its group" |
| 5 | The top bar | **Theories · Questions · Our Positions · Our Tests · News · About · Family** | "Our Tests" in the footer, so the bar is five pages as rule 4.21 suggests; the project's own work then drops out of sight | *(ruled)* "Yes, six pages". The weakest step, put to him when he ruled: "Our" brings back the first person after the front page moved to the site's voice. The wording of the labels is settled with the copy. |
| 6 | The line above the title | **The kickoff's draft as written** | The shorter form in section 8, if the cold-reader test (kickoff section 11) finds the draft too long | *(ruled)* "Yes, with ten", accepting the master session's change: "What is the least a mind needs? Every theory of consciousness gives an answer. Here is how ten of them are holding up." "Each" after "every theory" promised a completeness the page does not have. The number comes from the records at build time, never typed in. It is still draft copy, under the voice checks and the cold-reader test. |

Not for this proposal, and not decided by it: the headline (kickoff ruling 3), the theory list,
the address, and the rename (kept, and reopened only on evidence). The pictures are drawn so that
any answer to those four drops in without a change to the design.

## 8. Draft copy

**Draft, not ruled. It passes the Voice Calibration Protocol and the cold-reader passes before it
goes on a public page** (Minimum Viable Mind's `CLAUDE.md`, "Public-facing writing"). Named
things are linked at first mention when built (workspace rule "Link what you name"); no tool is
named (workspace rule "Tools are not advertised").

### The first screen

> **What is the least a mind needs?** Every theory of consciousness gives an answer. Here is how
> [ten] of them are holding up.
>
> *(The line as ruled 2026-11-20; "[ten]" is the count of entries on the ranking, taken from the
> records at build time.)*
>
> # How far has the science of consciousness got in testing its theories?
>
> *[the ranking]*
>
> **Read it this way.** The order is set by the first bar only. The second bar gets a theory into
> the ranking; the third says where the work is, and a long one is not a fault. The three are
> never added up. How the numbers are worked out.
>
> *[the headline card, placeholder]* **[N]%** of the sharp predictions these theories make have
> been put to a test at all. [n] of [m] predictions · [k] theories.
>
> Each theory is scored three ways, by rules written down before any theory was scored: how well
> published studies back it, how sharply it is stated so that a study could prove it wrong, and
> how much of it no study has touched yet. One of the theories is this site's own, the account
> argued on Sentient Horizons; it is scored by the same rules, and an outside reader makes the
> first judgement on every one of its rows.
>
> Last checked [date]: [n] open predictions read against new papers, none moved. See the week's
> reading.
>
> [Why so little is settled] [Who is asking]

A shorter line above the title, if the draft proves too long in the cold-reader test: "Every
theory of consciousness, held to the same evidence."

### The About page

> # About Minimum Viable Mind
>
> **Why this site exists.** There are many theories of what makes something conscious, and each
> says the evidence is on its side. This site asks a plainer question: how much of each theory has
> actually been tested, and how have the tests gone? It ranks the theories by the answer, and it
> shows its working, so that you can disagree with one judgement at a time.
>
> **What is scored.** Each theory is boiled down to between three and seven core claims, quoted
> from one publication by the people who hold it. For each claim, the site records the
> predictions that could prove it wrong and that set it apart from a rival. Then it records every
> published study that tested one of those predictions, and whether the result went for or
> against.
>
> **The three scores.** *How well the evidence backs it* runs from 0 to 100, and 50 means the
> evidence is even. A study counts for more when it has more protections against bias: its
> predictions were registered before the data came in, it was run by people outside the theory's
> own camp, a rival camp agreed in advance what would count against each side, or another group
> repeated it. *How sharply it is defined* is the share of its core claims that come with a
> prediction that could fail. *How much is left to test* is the share of those predictions no
> study has touched. A theory is ranked only when more than half its core claims can be tested,
> and only once studies from at least two separate groups exist. The order is set by the first
> score alone. The three are never added together, because adding them would reward a theory for
> being vague or for being little tested.
>
> **What does not count.** A study that explained its result afterwards, against a prediction the
> theory had not yet made, is listed and moves nothing. A failed prediction stays failed; a later
> reading of the theory that softens the loss becomes a new prediction, which needs its own test.
>
> **Who judges.** Someone has to decide what a theory predicts and whether a study's result
> supports it. Every such decision is its own record, with the study, the passage and the reason,
> and every outcome is read twice, by two readers who do not see each other's answer. Where they
> disagree, the score waits.
>
> **This site's own account is on the list.** The account of consciousness argued on Sentient
> Horizons is scored as one theory among the others. That is a conflict of interest, and the site
> handles it in three ways: the rules were fixed before any theory was scored, an outside reader
> makes the first judgement on every row of that account, and a result against it stands once
> recorded. Where it loses, the page says so.
>
> **Our own tests.** This project also runs small experiments of its own. They count toward a
> score only by the same rules as anyone's study, at the weight their method earns.
>
> **The story so far.** *[the dated entries, as on the other trackers]*
>
> **How to disagree.** *[the three forms: name a missing prediction, question a judgement, argue
> a score]*

## 9. What building it would take, once ruled

- **The skin:** in `site/src/styles/skin.css`, the accent family's seven values in each theme
  (`--accent`, `--accent-hover`, `--link`, `--link-hover`, `--on-accent`, `--glow`,
  `--callout-bg`); the mock's `skin-reinked.css` has them. The favicon takes the new accent; the
  parent's projects list changes this site's colour.
- **The pages:** a ranking component, a theory page and a prediction page built from the scoring
  records once stage 2 produces them; the three side pages; the present ladder, learned and story
  pages moved under Our Tests at their present addresses (every old address keeps working). The
  mock's `site.css` is a starting point for the component styles, tokens only.
- **Checks:** the site's existing public-text check (`scripts/check_site.py`) runs on the new
  pages; the theme and phone widths were checked only in the mock, not in the real site.
- **Order:** the skin can land on its own; the pages wait for stage 3 (kickoff section 10), and the
  first screen's line above the title waits for the cold-reader test.

## 10. What was checked and what was not

Checked: the mock pages at 1280 and 390 pixels in both themes; the top bar on one row at 1280;
the accent contrast (mulberry 7.0 on the paper, 9.2 on graphite; the slate data colour 3.8 on the
paper, which passes for bars and not for text, so it is never used for text). The seven sibling
first screens were looked at in a browser on 2026-11-20. Not checked: a real phone browser; a
screen reader; the ranking with ten rows (the first list's size since John raised the limit to ten;
the pictures show eight) or with long real names; how the first screen reads
to a stranger (the cold-reader test belongs to stage 3).

## 11. The pictures

| file | what it shows |
|---|---|
| `01-today-light-desktop.jpg` | the live home page today, light (the default) |
| `02-today-dark-desktop.jpg` | the same, dark |
| `03-lean-home-light-desktop.jpg` | **the lean**: the first screen, light |
| `04-lean-home-dark-desktop.jpg` | the same, dark |
| `05-lean-home-light-desktop-whole-page.jpg` | the whole home page, all three groups |
| `06-lean-home-light-phone.jpg` | the first screen on a phone, light, the headline card above the ranking |
| `07-lean-home-dark-phone.jpg` | the same, dark |
| `08-lean-theory-light-desktop.jpg` | a theory's page, light |
| `09-lean-theory-dark-desktop.jpg` | the same, dark |
| `10-lean-theory-light-phone.jpg` | the same on a phone |
| `11-lean-prediction-light-desktop.jpg` | a prediction's page, light |
| `12-lean-prediction-dark-phone.jpg` | the same on a phone, dark |
| `13-lean-open-questions-light-desktop.jpg` | the open questions |
| `14-lean-positions-light-desktop.jpg` | our working positions against the evidence, light |
| `15-lean-positions-dark-phone.jpg` | the same on a phone, dark |
| `16-lean-own-tests-light-desktop.jpg` | our own tests, light |
| `17-lean-own-tests-dark-desktop.jpg` | the same, dark |
| `18-A-notebook-kept-light-desktop.jpg` | direction A: the same first screen in Notebook as ruled, light |
| `19-A-notebook-kept-dark-desktop.jpg` | the same, dark |
| `20-number-first-light-desktop.jpg` | the lean's skin with the number first, light |
| `21-number-first-light-phone.jpg` | the same on a phone |
| `22-C-dark-room-dark-desktop.jpg` | direction C: Dark room, dark (its default) |
| `23-C-dark-room-light-desktop.jpg` | the same, light |
| `24-C-dark-room-dark-phone.jpg` | the same on a phone |
| `25-C-dark-room-theory-dark-desktop.jpg` | a theory's page in Dark room |

To redraw them: `cd mock && python3 build.py`, then open any page with `?skin=reinked`,
`?skin=notebook` or `?skin=darkroom` and `&theme=light` or `&theme=dark`. `shoot.sh` and
`shootphone.sh` are the capture commands used.
