#!/usr/bin/env python3
"""Does the right skill fire? Runs each prompt through headless Claude Code with only this pack loaded and scores the
first skill it invokes. Usage: python3 scripts/trigger-eval.py [--model sonnet] [--jobs 5] [--prompts evals/triggers/prompts.json]"""
import argparse, json, os, subprocess, sys, tempfile, concurrent.futures as cf
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser(); ap.add_argument("--model", default="sonnet"); ap.add_argument("--jobs", type=int, default=5)
ap.add_argument("--prompts", default=os.path.join(ROOT, "evals/triggers/prompts.json")); A = ap.parse_args()
P = json.load(open(A.prompts)); cwd = tempfile.mkdtemp()
def run(row):
    try:
        out = subprocess.run(["claude", "-p", row["p"], "--plugin-dir", ROOT, "--setting-sources", "", "--strict-mcp-config", "--output-format", "stream-json",
                              "--verbose", "--model", A.model, "--max-turns", "1", "--allowedTools", "Skill"], capture_output=True, text=True, cwd=cwd, timeout=240).stdout
    except Exception as e:
        return row, None, f"error: {e}"
    got = None; text = ""
    for l in out.splitlines():
        try: e = json.loads(l)
        except ValueError: continue
        if e.get("type") == "assistant":
            for c in e["message"]["content"]:
                if c["type"] == "tool_use" and c["name"] == "Skill" and got is None: got = c["input"].get("skill", "").split(":")[-1]
                if c["type"] == "text": text += c["text"]
    return row, got, text[:160]
res = list(cf.ThreadPoolExecutor(A.jobs).map(run, P)); ok = 0; ours = {d for d in os.listdir(os.path.join(ROOT, "skills"))}
for row, got, text in res:
    want = row["want"]
    if want: good = got in want
    else: good = got not in ours
    ok += good
    if not good: print(f"MISS  want {want or 'none'}  got {got}  | {row['p'][:70]} | {text!r}")
print(f"{ok} of {len(res)} correct")
sys.exit(0 if ok == len(res) else 1)
