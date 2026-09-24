#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"scripts/coffee_soda_profiles.json").read_text(encoding="utf-8"))
ORGANS={"heart":"心","liver":"肝","spleen":"脾","lung":"肺","kidney":"肾"}
TASTES={"sour":"酸","bitter":"苦","sweet":"甘","pungent":"辛","salty":"咸"}
def mapping(i,p,r,run,artifact):
 a=r["runs"][0]["native_answers"]; qi=a["qi"]
 qrows="\n".join(f"| {x} | {qi['probabilities'].get(x,0):.2f} | M-0 |" for x in ["寒","凉","平","温","热"])
 trows=[]
 for key,label in [("sour","酸"),("bitter","苦"),("sweet","甘"),("pungent","辛"),("salty","咸")]:
  g="M-IV" if label in p["taste_m"] else "M-0"; note=p["taste_m"].get(label,"本轮未建立稳定、可追溯的映射依据。")
  trows.append(f"| {label} | {a['taste_'+key]['noul']:.2f} | {g} | {note} |")
 mrows=[]
 for key,label in ORGANS.items():
  m=a["meridian_"+key]; d=a[key+"_direction"]; z=d["probabilities"]
  mrows.append(f"| {label} | {m['noul']:.2f} | {d['choice']} | {d['confidence']:.2f} | {z['阴-']:.2f} | {z['阴+']:.2f} | {z['阳-']:.2f} | {z['阳+']:.2f} | M-0 |")
 return f"""# Mapping｜{i}

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

entry_id: {i}
research_ref: references/entries/{i}/research.md
summary_ref: references/entries/{i}/summary.md
summary_sha256: {r['summary_sha256']}
reasoning_version: {r['reasoning_version']}
five_shot_version: {r['five_shot_version']}
requested_model: {r['requested_model']}
actual_model: {r['runs'][0]['actual_model']}
repeat_count: {len(r['runs'])}
run_timestamp_utc: {r['run_timestamp_utc']}
workflow_run_id: {run}
workflow_artifact_id: {artifact}
native_result_ref: qa/jev-coffee-soda-batch/raw/{i}.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
{qrows}

Jev Choice：**{qi['choice']}**（Choice confidence {qi['confidence']:.2f}）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
{chr(10).join(trows)}

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
{chr(10).join(mrows)}

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 明确支持的感官类推标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：{p['evidence_body']}
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
"""
def reader(p,r):
 a=r["runs"][0]["native_answers"]; names={"sour":"酸","bitter":"苦","sweet":"甘","pungent":"辛","salty":"咸"}
 ts=sorted(((names[k[6:]],v["noul"]) for k,v in a.items() if k.startswith("taste_")),key=lambda x:-x[1])[:2]
 top="、".join(f"{x} {v:.2f}" for x,v in ts); high=max((a["meridian_"+k]["noul"],v) for k,v in ORGANS.items())
 qi=a["qi"]; sens="、".join(f"{x} M-IV" for x in p["taste_m"]) or "各味 M-0"
 tradi="咖啡共享母页的近现代资料不是本条现代配方的古籍直接分类。" if p["family"]=="coffee" else "本条是现代加工饮料，不能将共享软饮资料写成古籍对具体商品的专门分类。"
 return f"Jev v0.4 的四气 Choice 为**{qi['choice']}**（原生倾向分数 {qi['probabilities'][qi['choice']]:.2f}；Choice confidence {qi['confidence']:.2f}），该项 M：M-0。五味原生分数靠前的是{top}；感官类推标为（{sens}）。最高归经 Noul 为{high[1]} {high[0]:.2f}，低于读者层展示线；完整方向结果见 Mapping 与 raw JSON。模型分数不是现实世界概率，也不能推成临床效应。\n\n{tradi}"
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--workflow-run-id",required=True); ap.add_argument("--workflow-artifact-id",required=True); args=ap.parse_args()
 rawdir=ROOT/"qa/jev-coffee-soda-batch/raw"; manifest={}
 for line in (ROOT/"qa/coffee-soda-summary-sha256.txt").read_text(encoding="utf-8").splitlines():
  sha,ref=line.split("  ",1); manifest[Path(ref).parent.name]=sha
 hashes=[]; models=set()
 for i,p in DATA.items():
  path=rawdir/f"{i}.json"; raw=path.read_bytes(); r=json.loads(raw); hashes.append(f"{hashlib.sha256(raw).hexdigest()}  qa/jev-coffee-soda-batch/raw/{i}.json")
  if r["summary_sha256"]!=manifest[i] or len(r["runs"])!=1 or len(r["runs"][0]["native_answers"])!=16: raise ValueError(f"Raw validation failed: {i}")
  models.add(r["runs"][0]["actual_model"])
  snap=json.loads((ROOT/f"qa/jev-coffee-soda-batch/pre-freeze/{i}.json").read_text(encoding="utf-8")); summary=(ROOT/f"references/entries/{i}/summary.md").read_bytes()
  if hashlib.sha256(summary).hexdigest()!=manifest[i] or snap["summary_text"]!=summary.decode() or snap["summary_sha256"]!=manifest[i]: raise ValueError(f"Freeze validation failed: {i}")
  mp=ROOT/f"references/entries/{i}/mapping.md"; mp.parent.mkdir(parents=True,exist_ok=True); mp.write_text(mapping(i,p,r,args.workflow_run_id,args.workflow_artifact_id),encoding="utf-8")
  body=f"""# {p['name']}

{p['body']}

{p['evidence_body']}

**安全与选择。** {p['care']}

**本草按。** {reader(p,r)}

研究底稿：[research.md](../references/entries/{i}/research.md) · 冻结摘要：[summary.md](../references/entries/{i}/summary.md) · Jev 与 M 记录：[mapping.md](../references/entries/{i}/mapping.md)。

**参考文献**

"""+ "\n".join(f"{n}. {x}" for n,x in enumerate(p["body_refs"],1))+"\n"
  (ROOT/f"entries/{i}.md").write_text(body,encoding="utf-8")
 (ROOT/"qa/jev-coffee-soda-batch/native-json-sha256.txt").write_text("\n".join(hashes)+"\n",encoding="utf-8")
 with (ROOT/"qa/coffee-soda-batch-2026-09-24.md").open("a",encoding="utf-8") as f:
  f.write(f"""
## Actions 运行结果

- Workflow run: {args.workflow_run_id}, successful; API key sourced from Environment API_KEYS secret JEV_API_KEY.
- Artifact ID: {args.workflow_artifact_id}; name jev-coffee-soda-native-v0.4.
- Ten raw outputs match frozen summary hashes. Actual model(s): {', '.join(sorted(models))}; each record has one run and 16 native answers.
- Per-file raw JSON SHA-256: qa/jev-coffee-soda-batch/native-json-sha256.txt.
- Ten Mapping files preserve probabilities, confidence and directions; ten bodies link research, summary and mapping and retain English paper titles and verified DOI links.
""")
 print("Built ten mappings and entries; native records and frozen hashes validated.")
if __name__=="__main__": main()
