# Disk clean-up of the Minimum Viable Mind repo, 2026-10-25

John's Mac (Apple M4, 256 GB drive) was 96% full with 9.6 GB free. John approved this plan
and asked for it to run on 2026-10-25. It ran after the independent check of the frozen
successor code (the pull request that closed it was merged the same day), because that check needed the model
cache and the Python environment.

## Space before and after

| | Free space | Drive full |
|---|---|---|
| Before | 9.6 GB | 96% |
| After deleting the cache and environment, and removing the originals of the two moved folders | 16 GB | 92% |

The second figure does not yet include the benefit of the move. The two moved folders (6.2 GB)
still sit on the Mac inside iCloud Drive until iCloud has finished uploading them. See "iCloud
status" below.

## What happened to each path

All paths are under `~/Code/minimum-viable-mind/` unless stated.

| Path | Size | Action | Where it is now |
|---|---|---|---|
| `.hf-cache.nosync` | 4.9 GB | Deleted | Gone. Downloads again on demand (see below). |
| `.venv` | 1.5 GB | Deleted | Gone. Rebuilt from `.venv-lock-2026-08-28.txt` (see below). |
| `experiments/archive/` | 1.5 GB | Moved | `~/Library/Mobile Documents/com~apple~CloudDocs/MVM-archive/experiments/archive/` |
| `experiments/06-mvm-0a-constructed-self-index/artifacts/` | 4.6 GB | Moved | `~/Library/Mobile Documents/com~apple~CloudDocs/MVM-archive/experiments/06-mvm-0a-constructed-self-index/artifacts/` |
| `~/.cache/huggingface` (speech-to-text models) | 4.5 GB | Kept, not touched | Unchanged. |

Before deleting the cache and the environment, nothing was running from either one (no open
files under either folder, and no Python process using this repo's environment).

## How the move was checked

Both moved folders are ignored by git, so they were the only copies. Every file (227 in all) was
copied, then the checksum (SHA-256) of every copy was compared with the checksum of its
original. All 227 matched. Only then were the originals deleted.

The checksum list of the originals is not stored in the repo; the copy in iCloud can be
re-checked any time by hashing the files in `MVM-archive/` and comparing them with each other
(the two folders keep their original relative paths).

### Duplicates

None of the 15 large `.pt` files (the saved trained models) are duplicates of each other, so
all of them were kept. A few small files do repeat byte for byte across the folders (marker
files ending `.DONE`, copied training logs and results files in `a3_30m_seed0`, `a3_30m_seed1`,
`a3_30m_seed2` and the `pilot_a1_*` folders, and one `watch.log` that appears twice in the
reruns archive). They were copied as they are, to keep the folder structure exactly as it was.
The largest group is 25 identical `.DONE` marker files, each a few bytes.

## iCloud status

- **Upload:** iCloud had started uploading when checked (`brctl status` showed the files as
  queued for upload, with the upload active). It had not finished.
- **Optimize Mac Storage:** the setting reads as ON (`com.apple.bird optimize-storage` is `1`).
  With it on, iCloud can replace local copies of fully uploaded files with placeholders, which is
  what frees the space. It decides when to do this, usually when the drive is short of room, so
  the 6.2 GB may take a while to come back. The setting was not changed.
- **Until the upload finishes** the files are on this Mac only. To confirm they are safely
  online, open iCloud Drive in Finder and check that the `MVM-archive` folder shows the cloud
  icon with no spinner.

## The three worktrees with unsaved changes

None of the three has a copy of the two moved folders. Nothing was removed from any of them.

| Worktree (`.claude/worktrees/`) | Total size | Unsaved changes | What takes the space |
|---|---|---|---|
| `footer-social-to-about-2026-10-24` | 372 MB | A `site/node_modules` folder (untracked) | 357 MB under `experiments/`, mostly the saved models tracked in git |
| `jolly-tereshkova-9552e1` | 1.7 GB | An untracked folder `experiments/08-successor-degree/out-dev-10m/` | 1.5 GB in `experiments/08-successor-degree/out-freeze-tests/` (git-ignored saved models and logs, possibly the only copy), plus about 150 MB of tracked models |
| `optimistic-wescoff-de031c` | 191 MB | Two edited rulings in `docs/rulings/` | 183 MB under `experiments/`, mostly tracked models |

The other worktrees (without unsaved changes) are each about 370 MB, because git tracks 30
saved models in `experiments/rehearsal-successor-measure/out-grammar-c/models/`. Two
temporary worktrees in other sessions' scratch folders (`icons-minimum-viable-mind` and
`lic-minimum-viable-mind`) are about 371 MB each for the same reason. `reddit-link-2026-10-24`
is 725 MB. Removing finished worktrees is what would recover this, and that is John's call.

## How to rebuild

**Python environment (`.venv`).** Run these from the repo root:

    python3 -m venv .venv
    .venv/bin/pip install -r .venv-lock-2026-08-28.txt

The lock file lists the 117 package versions the environment had on 2026-08-28. (The Mac had
Python 3.14.5 at the time of the clean-up; an older environment may have used a different
version, which the lock file does not record.)

**Model cache (`.hf-cache.nosync`).** Nothing needs doing. `src/mvm/config.py` points the
download folder (`HF_HOME`) at `.hf-cache.nosync` and the first run downloads what it needs
again, about 4.9 GB. That includes the Gemma 2 2B instruction-tuned model
(`google/gemma-2-2b-it`) and the sparse-autoencoder files from GemmaScope. Gemma models are
gated on Hugging Face, so the Mac needs to be logged in to a Hugging Face account that has
accepted Google's terms; the login is already stored in `~/.cache/huggingface/token`. Keep
the `.nosync` ending on the folder name, so iCloud does not sync it.

**Bringing the archives back.** Copy `MVM-archive/experiments/archive/` and
`MVM-archive/experiments/06-mvm-0a-constructed-self-index/artifacts/` from iCloud Drive back to
the same places in the repo. If a file shows as a cloud placeholder, opening or copying it
downloads it first.
