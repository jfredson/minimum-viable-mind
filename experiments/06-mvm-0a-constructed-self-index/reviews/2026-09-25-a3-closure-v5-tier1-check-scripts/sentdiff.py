"""Sentence-level diff of the v4 closure block against the v5 closure block.
Prints every sentence removed (-) or added (+); unchanged sentences are not printed."""
import difflib, re, sys

def block(path, start, end):
    lines = open(path).read().split('\n')[start-1:end]
    text = ' '.join(l.strip() for l in lines)
    text = re.sub(r'\s+', ' ', text)
    # split on sentence end followed by space and capital/quote/asterisk/paren
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z"*(“])', text)
    return [s.strip() for s in sents if s.strip()]

v4 = block('docs/a3-closure-text-draft-2026-09-21-v4.md', 53, 234)
v5 = block(sys.argv[1], 43, 280)
print(f'v4 block: {len(v4)} sentences; v5 block: {len(v5)} sentences')
sm = difflib.SequenceMatcher(None, v4, v5, autojunk=False)
n = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        continue
    n += 1
    print(f'\n=== hunk {n}: {tag} v4[{i1}:{i2}] -> v5[{j1}:{j2}] ===')
    for s in v4[i1:i2]:
        print('- ' + s)
    for s in v5[j1:j2]:
        print('+ ' + s)
print(f'\n{n} hunks')
