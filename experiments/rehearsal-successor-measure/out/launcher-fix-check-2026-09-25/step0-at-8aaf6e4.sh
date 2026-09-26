#!/bin/bash
# Step 0 of the regenerated plan, run against this branch's launcher behind stand-ins.
W=/Users/john/.claude/jobs/1a8d030f/tmp/fix
T=/Users/john/.claude/jobs/1a8d030f/tmp/step0; rm -rf "$T"; mkdir -p "$T/bin" "$T/home"
printf '#!/bin/bash\necho "$*" >> %s/runpodctl.calls\nexit 1\n' "$T" > "$T/bin/runpodctl"
printf '#!/bin/bash\necho "$*" >> %s/ssh.calls\nexit 1\n' "$T" > "$T/bin/ssh"
cat > "$T/pmset" <<'FAKE'
#!/bin/bash
case "$1 $2" in
  "-g batt") echo "Now drawing from 'AC Power'"; echo " -InternalBattery-0 (id=1)	100%; charged; 0:00 remaining present: true" ;;
  "-g custom") printf 'Battery Power:\n sleep 15\nAC Power:\n sleep 15\n' ;;
  "-g "|"-g") printf 'System-wide power settings:\n SleepDisabled\t\t1\n' ;;
esac
FAKE
chmod +x "$T/bin/"* "$T/pmset"
TODAY=$(TZ=America/Los_Angeles date +%Y-%m-%d)
printf '## Ledger\n\n| date | phase | what ran | GPU | hrs | $ est | $ actual | total |\n|---|---|---|---|---|---|---|---|\n| %s | test | stand-in row, OUT=slice_handshake | 5090 | est 1h | $0.75-1.00 | — | — |\n' "$TODAY" > "$T/ledger.md"
echo "runpodctl resolves to: $(PATH="$T/bin:$PATH" command -v runpodctl)"
echo "\$ DRYRUN=1 SCALE=10M MAXTOK=2000000 OUT=slice_handshake GRACE_S=600 RUN_SUBDIR=slice_handshake CLEAR_RUN_SUBDIR=1 HARD_CAP_USD=2.00 RATE_PER_HOUR_USD=0.99 PRE_TRAIN_DIR=… PRE_TRAIN_CMD=\"python bench_arms.py …\" launch_a3_fetch_first.sh"
env PY_LOCAL=/Users/john/Code/minimum-viable-mind/.venv/bin/python PATH="$T/bin:$PATH" HOME="$T/home" PMSET="$T/pmset" LEDGER="$T/ledger.md" \
  DRYRUN=1 SCALE=10M MAXTOK=2000000 OUT=slice_handshake \
  GRACE_S=600 RUN_SUBDIR=slice_handshake CLEAR_RUN_SUBDIR=1 \
  HARD_CAP_USD=2.00 RATE_PER_HOUR_USD=0.99 \
  PRE_TRAIN_DIR="$W/experiments/rehearsal-successor-measure/src" \
  PRE_TRAIN_CMD="python bench_arms.py --device cuda --steps 50 --batch 32 --out /workspace/mvm-out/slice_handshake/bench_arms.json" \
  "$W/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh"
echo "exit=$?"
echo "stand-in runpodctl calls: $(cat "$T/runpodctl.calls" 2>/dev/null | wc -l | tr -d ' ')"
echo "stand-in ssh calls: $(cat "$T/ssh.calls" 2>/dev/null | wc -l | tr -d ' ')"
