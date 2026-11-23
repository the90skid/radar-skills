#!/bin/bash
# Copies shared/radar-data.md into every skill that links it, so each skill folder is complete when installed alone, and
# writes shared/rules-block.md between the <!-- rules --> and <!-- /rules --> markers of every SKILL.md.
set -e
cd "$(dirname "$0")/.."
python3 - <<'PY'
import glob, re
block = open("shared/rules-block.md").read().strip()
for p in sorted(glob.glob("skills/*/SKILL.md")):
    t = open(p).read()
    n = re.sub(r"<!-- rules -->.*?<!-- /rules -->", lambda m: "<!-- rules -->\n" + block + "\n<!-- /rules -->", t, flags=re.S)
    if n != t: open(p, "w").write(n)
PY
for d in skills/*/; do
  if grep -q "references/radar-data.md" "$d/SKILL.md"; then mkdir -p "$d/references"; cp shared/radar-data.md "$d/references/radar-data.md"; fi
done
echo "synced: $(ls skills/*/references/radar-data.md | wc -l | tr -d ' ') skills, rules block in $(grep -l '<!-- rules -->' skills/*/SKILL.md | wc -l | tr -d ' ')"
