#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,os,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"scripts/coffee_soda_profiles.json").read_text(encoding="utf-8"))
EXP=ROOT/"experiments/jev-rule-fewshot-pilot"; MANIFEST=ROOT/"qa/coffee-soda-summary-sha256.txt"; SNAPS=ROOT/"qa/jev-coffee-soda-batch/pre-freeze"; RAW=ROOT/"qa/jev-coffee-soda-batch/raw"
def load_module(path,name):
 spec=importlib.util.spec_from_file_location(name,path); assert spec and spec.loader
 m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def main():
 key=os.environ.get("JEV_API_KEY")
 if not key: print("JEV_API_KEY unavailable; no Jev results were produced.",file=sys.stderr); return 2
 v04=load_module(EXP/"run_pilot_v04.py","jev_v04_coffee_soda_batch"); base=v04.load_module(v04.BASE_RUNNER); fixtures=v04.load_json(v04.FIXTURE_PATH); questions=v04.build_questions(base)
 model=os.environ.get("JEV_MODEL","jev-latest"); repeats=int(os.environ.get("JEV_REPEATS","1"))
 if not 1<=repeats<=3: raise ValueError("JEV_REPEATS must be 1 to 3")
 rows=[]
 for line in MANIFEST.read_text(encoding="utf-8").splitlines():
  sha,ref=line.split("  ",1); path=ROOT/ref; i=path.parent.name
  if hashlib.sha256(path.read_bytes()).hexdigest()!=sha: raise ValueError(f"Summary changed: {ref}")
  snap=json.loads((SNAPS/f"{i}.json").read_text(encoding="utf-8")); text=path.read_text(encoding="utf-8")
  if snap.get("summary_sha256")!=sha or snap.get("summary_text")!=text: raise ValueError(f"Snapshot mismatch: {i}")
  rows.append((i,sha,path,v04.build_state(fixtures,{"document":text})))
 if len(rows)!=10 or set(x[0] for x in rows)!=set(DATA): raise ValueError("Expected ten frozen summaries")
 RAW.mkdir(parents=True,exist_ok=True)
 for i,sha,path,state in rows:
  out=RAW/f"{i}.json"
  if out.exists(): raise FileExistsError(f"Existing raw; preserve before rerun: {out}")
  runs=[]
  for n in range(1,repeats+1):
   response=base.api_json("POST","/v1/systemone",key,{"state":state,"model":model,"questions":questions})
   v04.validate_answers(base,response["answers"]); runs.append({"index":n,"actual_model":response["model"],"native_answers":response["answers"],"usage":response.get("usage")})
  record={"entry_id":i,"summary_ref":str(path.relative_to(ROOT)),"summary_sha256":sha,"reasoning_version":"jev-tcm-reasoning-v0.4","five_shot_version":"jev-tcm-pilot-fixtures-v0.4","requested_model":model,"run_timestamp_utc":datetime.now(timezone.utc).isoformat(),"runs":runs}
  out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(f"Saved {i}")
 return 0
if __name__=="__main__": raise SystemExit(main())
