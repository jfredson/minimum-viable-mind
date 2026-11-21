# Cold-reader test, first reader: a Claude model, 2026-11-21

A fresh subagent (Claude Opus), given only the two screenshots `01-home-light-desktop.png` and
`03-home-light-phone.png`, told to open no other file or page, and asked: what is the site about;
does it read as about the theories of consciousness, an AI product or a build log, and why; what
confused it. Its answer, word for word:

> 1. **What the site is about.** It compares about ten scientific theories of consciousness. For each one it shows how far that theory has actually been tested so far. Three bars score each theory: how well studies back it, how clearly it is stated, and how much of it is still untested. The site also counts its own theory, the "Sentient Horizons account", among the ten.
>
> 2. **Which of the three it is.** I read it as being about the theories of consciousness. The big headline asks how far the science has got in testing its theories. Below that is a ranked table of named theories, such as Integrated information theory and Global workspace theory, with study counts beside each. Nothing on the screen looks like a product or a sign-up. Nothing says "I built this" either, so I didn't read it as a build log. The name "Minimum Viable Mind" made me half-expect an AI or startup project, but the page didn't back that up.
>
> 3. **What confused me.**
>    - The "67%" box is the most eye-catching thing, and on the phone it comes before the theories it describes. Its sentence about "predictions that set these theories apart" took me two reads.
>    - The labels are dense: "=1", "past the bar", "a support score", "Check it by hand", "rests on 3 studies from 3 groups". The column headers "How well the evidence backs it (50 = even)" and "how much is left to test" need a key before I can read the bars.
>    - I couldn't tell who "Sentient Horizons" is, or why the site's own theory is in the list. That makes me wonder whether the scoring is fair.
>    - The "weekly reading" and "Who is asking" mean nothing to a newcomer.
>
>    I'd stay for the headline question, but the table's jargon might make me leave.

The second reader (Gemini) is prepared in `scripts/cold_reader_gemini.py` and not run: it is a spend.
