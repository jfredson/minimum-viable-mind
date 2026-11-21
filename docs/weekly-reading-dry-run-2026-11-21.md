# The weekly reading: a dry run, 2026-11-21

*Run by hand in a working session, with no Gemini call and nothing written into the records. It
ran against the scoring branch's records (`claude/stage3-scoring-eadbbf`, which holds the 37
searches and their baseline run), copied to a scratch folder.*

**1. The fixed searches, as a reading dated 2026-11-22.**
`python3 scripts/tracker_weekly.py search --date 2026-11-22 --data <copy> --out <scratch>` reran all
37 searches against Europe PMC, saved their raw results and compared them with the baseline run of
2026-11-21. **0 new results**, which is what should happen: the baseline ran the same day, so
nothing it had not seen could have appeared yet. The rerun took about 12 minutes, including
Europe PMC's pauses.

**2. What a real week would add.** To show the screen at work, I treated every baseline result
first published in the past seven days (2026-11-15 to 2026-11-21) as new. There were 5, and **none
qualifies**, so a reading of this week would add no waiting row. Its items would be `noted`, with
these reasons:
- *Damasio, no consciousness without feeling:* a case report of a drug briefly restoring
  responsiveness in a person with locked-in syndrome. It does not measure feelings of the body's
  state.
- *Damasio, no consciousness without a nervous system:* a review of herbicides and soil microbes. A
  review, and not about consciousness.
- *Damasio, feelings come from nerves and body tissue together:* a plant extract tested as a calcium
  channel blocker. Not about feeling.
- *Orchestrated Objective Reduction, microtubule vibrations:* mild oxygen loss at birth and the
  wiring of the cortex. It does not measure microtubule vibration.
- *Seth's view, conventional AI won't become conscious:* an AI tool that screens dogs' teeth. Not
  about machine consciousness.

This is the typical yield of name-free, per-prediction searches: most new hits are off-topic
because the terms are broad, and the screen catches them. A busy week might bring one or two papers
that qualify.

**3. ConTraSt.** `python3 scripts/tracker_weekly.py contrast` against the seen list (444 DOIs, from
the 2026-11-21 export): the live export has 494 rows and **0 new papers** marked as designed to test
any of the four families.

**4. The count.** `python3 scripts/tracker_weekly.py count`: 0 studies waiting; no reading yet.

**What it shows.** The mechanics work end to end: rerunning the searches, finding what is new,
the ConTraSt comparison, the count. The screen and the first reading are the routine's own reading,
step 3 and step 4 of `docs/weekly-reading-prompt.md`.
