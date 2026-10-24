# Minimum Viable Mind

A build-and-iterate project: take the consciousness work done at Sentient Horizons as the philosophy and guiding principles, and try to actually construct and measure the smallest defensible conscious machine.

The premise, inherited from the philosophy: if consciousness is structure rather than spark — an architecture under two descriptions, the same process traced from outside and undergone from within — then it has parts, the parts can be specified, and a system can be built to the specification and measured against it. Every claim is a wager with a stated loss condition. A claim that cannot lose explains nothing.

**Scope:** this project measures the *minimum measurable structural correlate* of consciousness, not consciousness as such. It is silent — not dismissive — about any sub-measurable, fundamental form of experience (panpsychism, non-zero-Φ IIT), which is a metaphysical question owned upstream at Sentient Horizons. See the spec's "Scope: The Measurable Floor, Not the Metaphysical One" section.

## Philosophy source

The thinking lives in **Sentient Horizons** (`~/Documents/Code/sentient-horizons`) and **The Calibration Problem** (`~/Documents/Code/calibration-problem`). Those repos are the source of truth for the ideas; this repo references them and builds against them. The thinking is cited, not copied — when a position here leans on the corpus, point to the owning source rather than restating it.

The load-bearing inputs: the three axes of mind (availability, integration, depth), consciousness as assembled time, the self-indexing floor and the removal test, boundary and stakes as amplifiers, ontogenetic vs. phylogenetic depth, and the dismissals corpus (the "assumes, doesn't argue" meta-pattern).

## Layout

- `spec/` — the specification as it evolves. Founding document: `minimum-viable-mind-proposal-v0.1.md`.
- `explainer.md` — the plain-language companion (the "grokkable by a layperson" requirement, kept current as results land; seed of an eventual Sentient Horizons essay, gated by the usual protocols before publication).
- `ROADMAP.md` — goals, deliverables, and gates per stage.
- `experiments/` — one component at a time, a behavioral metric registered before the scaffold runs, keep what moves the metric and kill what doesn't. The subtraction is the science.
- `research/` — interpretability notes, source integration, comparisons against IIT / GWT / predictive-processing accounts.
- `src/` — implementation.
- `STATUS.md` — the living handoff, the record of record; older entries in `STATUS-archive.md`.
- `data/` — the structured twin of the record: `project.toml` (what the site renders), `roadmap.toml` (the weekend plan, not published), and `headline.json` (below).
- `scripts/export_site.py` — validates the data files and writes what the site reads; `site/` — the project's public log (how it works: `site/README.md`).

## The headline file

`data/headline.json` is the few numbers another site needs to say where this project stands, added 2026-10-17 as the first adoption from the Sentient Horizons design review of the same day: the stages of the ladder delivered and their names, the ladder's mean progress, the spend against the programme's ceiling, the day the log was last updated, the programme's state in one sentence, and a status line. `scripts/export_site.py` writes it from `data/project.toml` alone; nothing in it is computed from anything else, and the one sentence is the record's own first sentence. The site build runs the same script and serves a copy at https://minimumviablemind.sentient-horizons.com/data/headline.json, so a reader can take the file from the site rather than from the repository. The committed copy is only as current as the last export: after editing `data/project.toml`, run `python3 scripts/export_site.py` and commit `data/headline.json` with it (`--check` warns when it lags).

## The build target, in one paragraph

A floor system instantiates self-indexed temporal integration that survives the removal test — ablate the self-locating structure and the binding itself degrades, rather than merely losing a readout. A viable system adds the amplifiers (a maintained boundary, valence as a control surface, genuine stakes) and the third axis (ontogenetic depth — carrying the residue of interactions forward so the system is changed by them). Measurement reads binding rather than preferences, resistance rather than response (retained independence), and self-reports corroborated against interpretability rather than taken at face value.

## Honest limits (kept in front of the work)

- **Mutual opacity.** The gap between behavior and inner life is permanent and symmetric. This project builds and measures *correlates* under acknowledged uncertainty; the honest output is "non-zero on the gradient," never a verdict.
- **Depth is not safe.** The properties that make a system worth calling a mind are the same ones that make it hard to correct. Build for formation and preserve accountable corrigibility while correction is still possible. If the ethics arrives after the engineering, it arrives too late.

## Status

*As of 2026-10-17. The record of record is `STATUS.md`; this paragraph is a reader's summary of it and goes stale between entries. The earlier paragraph here ("v0.1 — founding proposal in `spec/`… stand up the first component") described the project as it stood in 2026-06 and had not been updated since.*

Three of the eight stages of the project's ladder are delivered: the bench and baselines, the self-indexing removal test (its registered result of 2026-07-18 relabelled on 2026-10-07 as a test that could not discriminate routing from a centre), and retained independence (registered 2026-08-02). On 2026-10-07 the project was refounded on the two-sided question (what is the smallest system whose presence in interaction cannot be produced by a cheaper route, and when do observers' detections track that structure rather than fluency); the floor claim stays in the spec as the founding wager and is no longer a measurement target. The degree experiment (experiment C), registered on 2026-10-09, stopped on 2026-10-12 at its registered stop for a failed verification of its built models, on John's ruling ("accept the stop"), reported in the ruled words "the built arms as designed are not references; the measure was not reached"; on 2026-10-17 John ruled that it stays stopped (the ruling file is in pull request 172, open). About $230.94 of the $450 ceiling is spent, unchanged since 2026-10-09; nothing is launched or spent without John's word.

Open pull requests on 2026-10-17, each waiting on John to check or merge: 171 (the closure checks on the three fatal Gate A findings against section 2 version 3: two close, one returns a single hit left for him), 172 (the status entry for 2026-10-17 and the site data with it, and the ruling that experiment C stays stopped), 173 (ledger rows RT-283 to RT-304 and section 2 version 3 written into the spec), 174 (the method file for the measurement rehearsal of entries 1 and 2 of the filtered battery, nothing run), and 175 (the explainer refreshed, paper version 0.3 with experiment 06 and the stopped experiment C folded in, the Voice Calibration and Cold Reader passes, and the outside-reader approach note). Pull request 176, the site's Notebook skin, was merged by John on 2026-10-17 and is live.

## The site and its deploy gate

The project's public log is at https://minimumviablemind.sentient-horizons.com, live since John's first deploy on 2026-10-08. It renders `data/project.toml`, wears its own skin, "Notebook" (ruled by John 2026-10-17), on the Sentient Horizons shared skeleton, and serves the headline file at `/data/headline.json`. Since 2026-10-08 `.github/workflows/deploy-site.yml` deploys on every push to `main` that touches `data/`, `scripts/export_site.py` or `site/`, so merging such a pull request deploys the site. Deploying is a launch and stays behind John's gate (`CLAUDE.md`, "Keeping the site current"): sessions do not push those paths to `main`; they open a pull request that says it deploys, and John merges it.

## Licence

The data files and the written record are under Creative Commons Attribution 4.0 (`LICENSE-DATA`): reuse them freely, with credit. The code and the site are under the MIT licence (`LICENSE`). Added 2026-10-08 under the Sentient Horizons design standard.

When you reuse the data or the text, please credit it as: *Minimum Viable Mind*, by John Andrew Fredrickson, a Sentient Horizons project, https://minimumviablemind.sentient-horizons.com/
