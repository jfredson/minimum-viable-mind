#!/bin/zsh
# Author's run of docs/known-failure-modes.md against the grammar-attempt method.
cd /Users/john/Code/minimum-viable-mind/.claude/worktrees/w1c-grammar-attempt
PY=/Users/john/Code/minimum-viable-mind/.venv/bin/python
echo '### failure 1: denominators, from the measured file'
$PY -c "
import json
d = json.load(open('experiments/rehearsal-successor-measure/out-grammar-c/measure_base_F_T_C.json'))['arms']
for k in sorted(d):
    r = d[k]['reading']; f = r['floor']
    print(f\"{k}: room (whole - untouched) {f['room']:.4f}, required {f['required_room']:.4f}, clears {f['clears']}, top of scale when ownership-only = untouched: {(r['accuracy_whole']-r['accuracy_untouched'])/f['room'] if f['room'] else float('nan'):.4f}\")
"
echo '### failure 2: route sentence for the named-other target'
grep -n -iE 'three tokens before the scored position|is the input token|carried by the token' docs/grammar-attempt-method-2026-09-25.md
echo '### failure 3: trials in every pre-stated cell'
$PY -c "
import json
g = json.load(open('experiments/rehearsal-successor-measure/out-grammar-c/gate_base.json'))
print('gate cells, episodes per condition per run:', sorted({v['n'] for v in g['runs'].values()}))
d = json.load(open('experiments/rehearsal-successor-measure/out-grammar-c/measure_base_F_T_C.json'))['arms']
for k in sorted(d):
    c = d[k]['controls']
    print(k, 'control 6 same-value trials', c['6a same-value cell: trials'], 'different-value trials', c['6b different-value cell: trials'], 'reading trials', d[k]['n_trials'])
"
echo '### failures 5 and 6: anything that creates, rents or reaches a remote machine'
grep -n -iE 'ssh|runpod|vast|curl|requests\.|subprocess|launch|nohup' experiments/rehearsal-successor-measure/src/grammar_attempt.py experiments/rehearsal-successor-measure/src/repairs.py experiments/rehearsal-successor-measure/src/grammar.py || echo 'no matches'
