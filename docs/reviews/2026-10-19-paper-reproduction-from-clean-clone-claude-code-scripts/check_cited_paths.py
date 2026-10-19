"""List every file path the paper draft cites in backticks and say whether it exists in the clone.
Usage: python check_cited_paths.py REPO_ROOT"""
import re, sys
from pathlib import Path
repo = Path(sys.argv[1]); draft = repo/"drafts/paper-removal-test-nature-draft.md"
text = draft.read_text()
cites = sorted(set(re.findall(r"`([^`\s]+\.(?:md|json|py|toml|txt|png|sh))`", text)))
exp06 = repo/"experiments/06-mvm-0a-constructed-self-index"
exp01 = repo/"experiments/01-self-indexing-removal-test"
exp08 = repo/"experiments/08-successor-degree"
beside = {  # bare names the draft resolves by saying 'in experiments/06.../' or 'beside this file'
}
def find(c):
    if (repo/c).exists(): return str(c)
    for base in (exp06, exp01, exp08, repo/"drafts"):
        if (base/c).exists(): return str((base/c).relative_to(repo))
    hits = list(repo.rglob(Path(c).name))
    hits = [h for h in hits if ".venv" not in h.parts and ".git" not in h.parts]
    return str(hits[0].relative_to(repo)) + " (found elsewhere)" if hits else None
missing = []
for c in cites:
    r = find(c)
    print(("ok       " if r and "elsewhere" not in r else "ELSEWHERE " if r else "MISSING  ") + c + (("  ->  " + r) if r else ""))
    if not r or "elsewhere" in (r or ""): missing.append((c, r))
print(f"\n{len(cites)} cited paths; {sum(1 for c in cites if find(c) and 'elsewhere' not in find(c))} found where cited; {len(missing)} not found where cited")
