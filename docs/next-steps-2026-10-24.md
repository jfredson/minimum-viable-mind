# Minimum Viable Mind after the revised theory: how to move forward

*A proposal for John, written 2026-10-24 (Saturday, Pacific) by a working session started from the master session. It is a reading and a proposal only: nothing was run, rented, spent, moved or deleted, and no other file in this repository was changed. Every recommendation below is John's to accept or overturn.*

*What it reads against. The one-page statement of the revised theory, "Assembled time, revised" (`editorial/2026-10-23-assembled-time-revised-theory.md` in the sentient-horizons repository, on its pull request 119; John approved the page on 2026-10-23, "I approve the revised-theory page", as quoted in the positions ledger). The rewritten essay "Consciousness as Assembled Time" (sentient-horizons pull request 114, merged 2026-10-24). The positions ledger (`editorial/corpus-positions-ledger.md` there), entries 19 (where current AI sits), 27 (no floor; a question for removal), 32 (the split between doing and undergoing as the account's bet about a point of view) and 55 (a perfect copy of you is not you).*

---

## 1. What the project set out to show

The project started from one bet: that consciousness is a kind of structure, not an extra spark, so a system could be built to a specification and measured against it. Its target was the **floor**: the smallest structure that would make it fair to say someone is home. The book and the essay described that floor as a "centre" that a system's whole activity is organised around, and the project's main tool was a removal test. Find the part of an AI model that tracks "the one speaking is me", remove it, and see what breaks. If only the model's talk about itself changes, the self was a description stuck on the machinery. If its whole ability to hold the conversation together degrades, the self-tracking was structural.

Three experiments and a successor followed:

- **The removal test** (experiment 01, run 2026-07-18 on an open model with eight billion adjustable numbers). Removing the self-tracking part damaged everything, including a simple control task that only needs to keep track of whose turn it is. Because the turn-keeping control dropped as much as the self-related tasks, the pre-stated rule read the result as conversational bookkeeping, not a centre. On 2026-10-07 this was relabelled: the test could not tell bookkeeping from a centre.
- **Retained independence** (experiment 03, registered 2026-08-02). Pressure from a user mostly makes a model stop *saying* its answer, and almost never makes it stop *holding* it.
- **A small model built with a self-slot** (experiment 06). The installed slot never held anything. A redesign made a task the model could only do by knowing which of four agents it was; the model learned it, but the matched comparison the registration asked for could never be computed, so it closed as "not testable".
- **The successor, experiment C**, set out to measure how much of a model's activity is organised around its answer to "which agent am I". It stopped at its own registered stop on 2026-10-12 and stays stopped (John, 2026-10-17).

On 2026-10-07 the project was refounded on a two-sided question: what is the smallest system whose *presence* in a conversation cannot be produced by a cheaper trick, and when do people's sense of a mind's presence track that structure rather than fluent talk? Its battery of tests had its first two entries rehearsed by API on 2026-10-18 and 2026-10-19; both came back "no verdict", and John ruled that entry 1 stops there.

So, in plain words: **the project set out to find the smallest system that crosses a line into having a mind, by removing parts and watching what breaks.** After a year it has honest instruments, careful records, and no positive result.

## 2. What the revised theory changes

The revised theory makes four moves that touch this project directly.

1. **There is no declared line.** The theory now maps features that seem to go with experience in the beings we know (binding the just-past into the present, a shared workspace, the split between what a system does and what happens to it, self-awareness, a boundary, mattering, kept memory), and it says these can come apart. It no longer declares a floor below which there is no experience (ledger entry 27).
2. **The point of view is the split, not a self-model.** A system's description of itself is "ordinary machinery" and counts for nothing on its own. The bet about a point of view is the split between doing and undergoing, which the system's own processing uses (ledger entry 32). Self-awareness, knowing that you are the one things happen to, is a separate and later feature.
3. **Removal is the only method.** The theory says plainly that watching the beings we know cannot tell which features experience needs and which only travel with it, and that only removing one feature at a time can.
4. **The removal test now predicts a particular kind of loss.** Remove the split, and practised routines should carry on while flexible response to something new collapses, including on tasks that have nothing to do with the system itself. Remove a self-description, and only self-talk flattens. Remove an essential part, and everything fails at once, which shows nothing.

Taking the project's parts one at a time:

| Part of the project | Effect of the revised theory | Why |
|---|---|---|
| **The aim: the smallest system that crosses the floor** | **Made pointless as stated** | If no line is declared, there is no smallest system above it to look for. The README's "build target" paragraph and the spec's floor section both rest on the line. |
| **The method: remove a part, see what breaks** ("the subtraction is the science", `experiments/README.md`) | **Strengthened** | The theory now says removal is the *only* way to learn which features matter. This project is the one place in the family of projects that already runs removals on real systems, with registered rules and records. |
| **The removal test of July (experiment 01)** | **Changed in meaning; worth a second reading** | The old theory treated turn-keeping ("whose words are these?") as the cheap account that ruled a centre *out*. The new theory names keeping the model's own words apart from the user's as the *candidate* for the split itself (essay, "A single model run"; ledger entry 19). So what the July test removed may be close to the very thing the new theory wants removed. The July test was not built to see the predicted kind of loss (routines kept, new problems lost), but its record has a hint: six of the seven failed items on the tasks that never mention the model were multi-step reasoning (`explainer.md`, "What the first test found"). That is suggestive, not a result. |
| **The new essay's sentence that no one has run the split test** | **Needs checking against this project's record** | The essay says of removing the signal that marks which words are the model's own: "As far as I know, no one has run that experiment yet." Experiment 01 ran a near relative of it in July. It was not the same test, but a reader who finds both will ask. This is a decision for John (section 5, decision 4). |
| **The constructed model (experiment 06)** | **Largely settled; no reason to reopen** | Its installed self-slot is exactly the "self-description" the new theory says counts for nothing, and its ownership input was handed in from outside, which is not the system's own split. Its records stand as written. |
| **Experiment C (how much activity is organised around "which agent am I")** | **Made pointless as designed** | It measured the reach of a self-identity answer, which on the new map is self-description or, at most, a step toward self-awareness, not the split. It stays stopped, and the revised theory adds a reason. |
| **Retained independence (experiment 03)** | **Stands; may help later** | Its finding is about behaviour under pressure, which the theory now says cannot by itself show experience. It may help design a test of mattering (whether the model's own processing steers toward or away from some states), but it is not that test. |
| **The two-sided question: the system side** (five signs of depth against named cheaper tricks) | **Weakened** | The signs are mostly behavioural, and the theory now says behaviour "cannot be the test of experience" and that a machine "has to be judged by its parts". Depth (kept memory, a long history) is on the map, but as something that enriches experience, not something that switches it on. |
| **The two-sided question: the observer side** (when people's sense of presence tracks structure) | **Weakened as a route to minds; could stand as a study of people** | The theory names fluent talk as not evidence on its own. Whether people are fooled by fluency is a fair question about people, but it no longer bears on where a system sits on the map. |
| **The battery of tests** (entries 1 and 2 rehearsed, both "no verdict") | **Pause** | Its entries read behaviour in conversation. Nothing in the revised theory gives them a job until the observer side is reconsidered. |
| **The workspace stage** (stage 2, "the shape of binding") | **Partly done by others** | The 2026 study by [Wes Gurnee and colleagues](https://transformer-circuits.pub/2026/workspace/index.html) reports first evidence of a shared workspace inside a language model. The project can take that as a known part rather than build it, while keeping the ledger's guard that a workspace is not the split (entry 45). |
| **The body test** (stage 7: a robot with a battery to manage, giving it boundary and stakes) | **Mostly made pointless** | The theory now puts a model's boundary in its weights, replaces survival stakes with mattering, and says an animal that could not die would still have experience. A robot body is no longer the natural place to test either. |
| **The paper** ("Instruments that can lose…", version 0.3, readiness steps 1 to 3 open) | **Its results stand; its framing needs one change** | Its title and introduction speak of "self-indexed integration", the old floor's language. Its numbers are unaffected. A paragraph saying what the removal test means under the map, or a narrowed framing as a methods paper, would keep it consistent with the essay. |

**The short version.** The revised theory removes the project's *destination* (a smallest mind above a line) and keeps, even sharpens, its *method* (remove one part, read the kind of loss). It also hands the project a specific, testable experiment that the essay says no one has run: remove the split in a language model and see whether practised routines survive while new problems fail.

## 3. A proposed new aim, in one sentence

**Minimum Viable Mind becomes the removal laboratory for the map: it takes one feature at a time in systems that can be opened, removes it, and reports which kind of loss follows: none, only self-talk, everything, or the selective loss the theory predicts for the split.**

"Minimum" then means the smallest system on which a single feature can be cleanly removed and read, not the smallest mind. The output stays what the project has always promised: a profile of which features a system shows and what removing each one does, never a verdict.

## 4. The next steps, in order

1. **John rules on the new aim** (decision 1 below). Nothing else moves until he does, because every later step depends on it. $0.
2. **Write the new aim into the record, with the old one kept.** A dated note at the top of the spec and the README saying the floor is withdrawn upstream and what the project now measures, with the old text left in place below as the record of what was registered. One new STATUS entry and the matching site data. A second session checks it before merge, as the project's own rules require. Merging changes the public site, so that merge stays behind John's word. $0.
3. **Re-read the July removal test under the new map, at $0.** The per-item answers from the registered run are still on disk (`artifacts/removal_test/`, about 440 KB). Write the method first and label it as a re-reading done after the theory changed. Then sort the items the model got wrong after the removal into "practised routine" and "new or flexible" by rules fixed before looking, and report the split. This cannot confirm anything, because the items were not built for it, but it tells the next experiment what to expect and answers the essay's sentence honestly.
4. **Design the split removal test as a new registered experiment**, on paper first, $0. In outline:
   - **What is removed:** the signal inside an open model that marks which words are its own and which are the user's, leaving everything else in place.
   - **Three comparison removals:** removing only the model's self-description (prediction: only self-talk flattens); removing an essential part (prediction: everything fails); and a random removal of the same size (prediction: little changes).
   - **Tasks built for the prediction:** practised routines and new problems, each split into tasks about the model and tasks that never mention it.
   - **How it loses, stated in advance:** if removing the split damages routines and new problems alike, or only self-related tasks, the account's bet about the split loses on this system.
   - **Reuse:** the removal machinery from experiment 01 (`experiments/01-self-indexing-removal-test/src/`).

   It then goes through the project's usual review gates before it is registered.
5. **Ask John's go to run it**, with an estimate and a ceiling. The July test needed a rented machine for its eight-billion-number model. A first run on the smaller two-billion-number model the project used as its bench (`google/gemma-2-2b-it`, in `src/mvm/config.py`) may fit on this Mac, which would cost nothing but a download of about 5 GB. Spend only on John's go, as ruled 2026-10-18.
6. **Bring the paper into line**, after step 3: one paragraph on the map, or a narrowed framing (decision 3). Then resume the paper's readiness steps 1 to 3, which are already on the roadmap.

What stops: the battery of tests and the observer side (paused, not deleted), experiment C (stays stopped), and the body test (parked indefinitely).

## 5. What to do with the large files

These are recommendations only. John decides, and nothing has been moved or deleted.

**Where the space is.** The repository's main folder (`~/Code/minimum-viable-mind`) holds about 15 GB under `experiments/`:

| What | Size | What it is |
|---|---|---|
| `experiments/06-mvm-0a-constructed-self-index/artifacts/` | 13 GB | Trained model files from the constructed model, experiment 06 |
| `experiments/archive/` | 1.5 GB | Outputs moved out of old work folders on 2026-10-12, mostly the training-exclusion check for experiment C |
| `experiments/08-successor-degree/` | 0.6 GB | Experiment C's small models and outputs |
| `experiments/rehearsal-successor-measure/` | 0.2 GB | The rehearsal of experiment C's measure |
| Experiments 01, 03, 07 | about 2 MB | Records and code |

**The biggest finding: most of experiment 06's 13 GB is exact copies.** It holds 37 model files, but only 15 different ones, about 4.6 GB in all. About 8.4 GB are byte-for-byte duplicates sitting in several run folders (checked by fingerprinting each file's contents, SHA-1, on 2026-10-24). One caution: two different files share the name `pilot_a1_30m_seed1.pt`, so any clean-up has to go by fingerprint, not by name.

**The "4.5 GB of downloaded AI models".** No downloaded model sits inside this project now: the folder it would use (`.hf-cache.nosync`) does not exist. The 4.4 GB of downloaded models on this Mac are in `~/.cache/huggingface/` and are two speech-to-text models (Whisper large-v3 and its faster "turbo" version) plus a small sentence-matching model, last touched 2026-10-17. They are not this project's. A script in The Upgrade Tree (`upgrade-tree/scripts/`) mentions Whisper, so they likely belong to that work or to transcription generally. Their fate is for whichever project uses them; none of the steps above needs them.

**Recommendation, by group:**

- **Keep on the Mac, needed for the steps above:**
  - experiments 01 and 03 and `artifacts/` (about 25 MB);
  - experiment 01's code;
  - the three finished experiment 06 models (`a3_30m_seed0`, `seed1`, `seed2`) and its control model, about 1.3 GB, which the paper's reproduction step (readiness step 3) may need.
- **Remove the duplicates (about 8.4 GB):**
  - keep one copy of each of the 15 distinct files, with a list of their fingerprints committed, so nothing is lost;
  - this is the safe win, and it needs John's go because it deletes files.
- **Could move off the Mac, to an external drive or cloud storage:**
  - experiment 06's pilot models from its first design (the ones with the installed self-slot, about 2.5 GB of distinct files), which belong to a closed design;
  - `experiments/archive/` (1.5 GB);
  - experiment C's models (0.6 GB), since it stays stopped and the new theory gives no reason to reopen it.

  The records describing them stay in git; only the model files move. The paper does not depend on them, though its reproduction step should confirm that before they move.
- **Could go entirely:** the partial checkpoint `a3ctl_30m_seed0_PARTIAL_step51500.pt` (335 MB), an interrupted save superseded by the finished control model. Delete it only after the reproduction step confirms nothing cites it.
- **Not asked about, noticed in passing:**
  - the project's Python environment (`.venv`, 1.5 GB) can be rebuilt from its lock file;
  - two older work folders under `.claude/worktrees/` hold about 2.2 GB.

  Both are clean-up for another day.

## 6. Decisions for John

**Decision 1. What is the project for now?**
- (a) The removal laboratory for the map, as in section 3. *Recommended:* it keeps the project's method, records and tools, and gives it the one experiment the theory most needs.
- (b) Keep the two-sided question as the aim, with the floor sentence removed. This keeps the battery going, but measures behaviour that the theory now says cannot settle anything about experience.
- (c) Pause the project and keep it as a finished record, with a closing note. Honest, and cheap, but it leaves the theory's central test to no one.

**Decision 2. Does the name stay?**
- (a) Keep "Minimum Viable Mind", and say on the site that "minimum" now means the smallest system on which one feature can be cleanly removed. *Recommended:* the site, the headline file and the links from sentient-horizons.com all use it.
- (b) Rename it to something that says "removal" or "map". Clearer, and costs a site move.

**Decision 3. What happens to the paper?**
- (a) Keep its results and add one paragraph on what the removal test means under the map. *Recommended:* the numbers are unaffected, and the paragraph keeps the paper and the essay from contradicting each other.
- (b) Reframe it as a methods paper on registered removal tests, dropping "self-indexed integration" from the title.
- (c) Hold it until the split test has run, and publish the two together.

**Decision 4. The essay's "no one has run that experiment yet".**
- (a) Leave the essay as it is, and let the re-reading in step 3 of section 4 say how the July test differs. *Recommended for now:* the July test was not the same experiment, and the re-reading will say exactly how close it came.
- (b) Add a sentence to the essay pointing to the July test as a near relative, after the re-reading. This touches a published essay, so it goes through the usual voice and cold-reader passes in the sentient-horizons repository, not here.

**Decision 5. The large files.**
- (a) Remove the 8.4 GB of exact duplicates now, keeping one copy of each with fingerprints recorded, and leave the rest until the paper's reproduction step is done. *Recommended:* no information is lost.
- (b) Also move the closed designs' models and experiment C's files to an external drive (about 4.6 GB more).
- (c) Leave everything as it is; there are 51 GB free.

**Decision 6. The battery and the observer side.**
- (a) Pause both, with a dated note saying why. *Recommended.*
- (b) Close them, as no longer bearing on the theory.
- (c) Continue them as a study of how people judge minds, separated from the map.

---

*Sources for the project's own claims above: `README.md`, `explainer.md` (refreshed 2026-10-17), `STATUS.md` (entries of 2026-10-18), `experiments/README.md`, `data/project.toml` (findings), the TimeAssembler roadmap and worklog for this project (read 2026-10-24), and the file sizes and fingerprints measured on this Mac on 2026-10-24.*
