#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"scripts/coffee_soda_profiles.json").read_text(encoding="utf-8"))
def main():
 snaps=ROOT/"qa/jev-coffee-soda-batch/pre-freeze"; snaps.mkdir(parents=True,exist_ok=True)
 lines=[]
 for i in DATA:
  ref=f"references/entries/{i}/summary.md"; raw=(ROOT/ref).read_bytes(); sha=hashlib.sha256(raw).hexdigest(); text=raw.decode()
  lines.append(f"{sha}  {ref}")
  o={"entry_id":i,"summary_ref":ref,"summary_sha256":sha,"reasoning_version":"jev-tcm-reasoning-v0.4","five_shot_version":"jev-tcm-pilot-fixtures-v0.4","snapshot_date":"2026-09-24","summary_text":text}
  (snaps/f"{i}.json").write_text(json.dumps(o,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 (ROOT/"qa/coffee-soda-summary-sha256.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
 print(f"Froze {len(DATA)} summaries.")
if __name__=="__main__": main()
