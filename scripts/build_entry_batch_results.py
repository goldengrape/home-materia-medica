#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORGANS = {"heart": "心", "liver": "肝", "spleen": "脾", "lung": "肺", "kidney": "肾"}
TASTES = {"sour": "酸", "bitter": "苦", "sweet": "甘", "pungent": "辛", "salty": "咸"}

def mapping(entry_id, p, r, batch_id, run_id, artifact_id):
    a = r["runs"][0]["native_answers"]
    qi = a["qi"]
    qrows = "\n".join(f"| {x} | {qi['probabilities'].get(x, 0):.2f} | M-0 |" for x in ["寒", "凉", "平", "温", "热"])
    taste_rows = []
    for key, label in TASTES.items():
        group = "M-IV" if label in p["taste_m"] else "M-0"
        note = p["taste_m"].get(label, "本轮未建立稳定、可追溯的感官映射依据。")
        taste_rows.append(f"| {label} | {a['taste_' + key]['noul']:.2f} | {group} | {note} |")
    meridian_rows = []
    for key, label in ORGANS.items():
        m = a["meridian_" + key]
        direction = a[key + "_direction"]
        z = direction["probabilities"]
        meridian_rows.append(
            f"| {label} | {m['noul']:.2f} | {direction['choice']} | {direction['confidence']:.2f} | "
            f"{z['阴-']:.2f} | {z['阴+']:.2f} | {z['阳-']:.2f} | {z['阳+']:.2f} | M-0 |"
        )
    return f"""# Mapping｜{entry_id}

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: {batch_id}
entry_id: {entry_id}
research_ref: references/entries/{entry_id}/research.md
summary_ref: references/entries/{entry_id}/summary.md
summary_sha256: {r['summary_sha256']}
reasoning_version: {r['reasoning_version']}
five_shot_version: {r['five_shot_version']}
requested_model: {r['requested_model']}
actual_model: {r['runs'][0]['actual_model']}
repeat_count: {len(r['runs'])}
run_timestamp_utc: {r['run_timestamp_utc']}
workflow_run_id: {run_id}
workflow_artifact_id: {artifact_id}
native_result_ref: qa/jev-entry-batches/{batch_id}/raw/{entry_id}.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
{qrows}

Jev Choice：**{qi['choice']}**（Choice confidence {qi['confidence']:.2f}）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
{chr(10).join(taste_rows)}

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
{chr(10).join(meridian_rows)}

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：{p['evidence_body']}
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
"""

def reader(p, r):
    a = r["runs"][0]["native_answers"]
    taste_names = {"sour": "酸", "bitter": "苦", "sweet": "甘", "pungent": "辛", "salty": "咸"}
    top = sorted(
        ((taste_names[k[6:]], v["noul"]) for k, v in a.items() if k.startswith("taste_")),
        key=lambda x: -x[1]
    )[:2]
    top_text = "、".join(f"{name} {score:.2f}" for name, score in top)
    highest = max((a["meridian_" + key]["noul"], label) for key, label in ORGANS.items())
    qi = a["qi"]
    sensory = "、".join(f"{name} M-IV" for name in p["taste_m"]) or "各味 M-0"
    tradition = p.get("tradition", "本条是现代加工饮料，不能将共享食品资料写成古籍对具体商品的专门分类。")
    return (
        f"Jev v0.4 的四气 Choice 为**{qi['choice']}**（原生倾向分数 "
        f"{qi['probabilities'][qi['choice']]:.2f}；Choice confidence {qi['confidence']:.2f}），该项 M：M-0。"
        f"五味原生分数靠前的是{top_text}；感官类推标为（{sensory}）。最高归经 Noul 为"
        f"{highest[1]} {highest[0]:.2f}，完整方向结果见 Mapping 与 raw JSON。模型分数不是现实世界概率，也不能推成临床效应。\n\n"
        f"{tradition}"
    )

def append_catalog(data, cutoff):
    path = ROOT / "catalog" / "entries.yaml"
    text = path.read_text(encoding="utf-8")
    additions = []
    for entry_id, p in data.items():
        if f"- id: {entry_id}\n" in text:
            continue
        additions += [
            f"- id: {entry_id}",
            f"  name: {p['name']}",
            f"  volume: {p.get('volume', '饮品部')}",
            f"  entry_type: {p.get('entry_type', 'beverage')}",
            f"  research_depth: {p['research_depth']}",
            f"  status: summary_frozen_{p['research_depth']}",
            f"  evidence_cutoff: {cutoff}",
        ]
    if additions:
        if not text.endswith("\n"):
            text += "\n"
        text += "\n".join(additions) + "\n"
        path.write_text(text, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-id", required=True)
    ap.add_argument("--workflow-run-id", required=True)
    ap.add_argument("--workflow-artifact-id", required=True)
    args = ap.parse_args()
    cfg = json.loads((ROOT / "scripts" / "entry_batches" / f"{args.batch_id}.json").read_text(encoding="utf-8"))
    data, batch = cfg["entries"], cfg["batch"]
    raw_dir = ROOT / "qa" / "jev-entry-batches" / args.batch_id / "raw"
    manifest_path = ROOT / "qa" / "entry-batches" / f"{args.batch_id}-summary-sha256.txt"
    manifest = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        sha, ref = line.split("  ", 1)
        manifest[Path(ref).parent.name] = sha
    if set(manifest) != set(data):
        raise ValueError("Summary manifest does not contain exactly the configured entries")

    hashes = []
    models = set()
    for entry_id, p in data.items():
        path = raw_dir / f"{entry_id}.json"
        raw = path.read_bytes()
        r = json.loads(raw)
        if r.get("summary_sha256") != manifest[entry_id] or len(r.get("runs", [])) != 1:
            raise ValueError(f"Raw metadata validation failed: {entry_id}")
        answers = r["runs"][0].get("native_answers", {})
        if len(answers) != 16:
            raise ValueError(f"Expected 16 native answers for {entry_id}, got {len(answers)}")
        models.add(r["runs"][0]["actual_model"])
        snap = json.loads((ROOT / "qa" / "jev-entry-batches" / args.batch_id / "pre-freeze" / f"{entry_id}.json").read_text(encoding="utf-8"))
        summary_raw = (ROOT / f"references/entries/{entry_id}/summary.md").read_bytes()
        if (
            hashlib.sha256(summary_raw).hexdigest() != manifest[entry_id]
            or snap.get("summary_sha256") != manifest[entry_id]
            or snap.get("summary_text") != summary_raw.decode("utf-8")
        ):
            raise ValueError(f"Freeze validation failed: {entry_id}")
        hashes.append(f"{hashlib.sha256(raw).hexdigest()}  qa/jev-entry-batches/{args.batch_id}/raw/{entry_id}.json")
        mp = ROOT / f"references/entries/{entry_id}/mapping.md"
        mp.write_text(mapping(entry_id, p, r, args.batch_id, args.workflow_run_id, args.workflow_artifact_id), encoding="utf-8")
        body = f"""# {p['name']}

{p['body']}

{p['evidence_body']}

**安全与选择。** {p['care']}

**本草按。** {reader(p, r)}

研究底稿：[research.md](../references/entries/{entry_id}/research.md) · 冻结摘要：[summary.md](../references/entries/{entry_id}/summary.md) · Jev 与 M 记录：[mapping.md](../references/entries/{entry_id}/mapping.md)。

**参考文献**

""" + "\n".join(f"{n}. {citation}" for n, citation in enumerate(p["body_refs"], 1)) + "\n"
        (ROOT / f"entries/{entry_id}.md").write_text(body, encoding="utf-8")

    hash_path = ROOT / "qa" / "jev-entry-batches" / args.batch_id / "native-json-sha256.txt"
    hash_path.write_text("\n".join(hashes) + "\n", encoding="utf-8")
    append_catalog(data, batch["research_cutoff"])
    qa_path = ROOT / "qa" / "entry-batches" / f"{args.batch_id}.md"
    with qa_path.open("a", encoding="utf-8") as f:
        f.write(f"""
## 判与写完成记录

- Workflow run: {args.workflow_run_id}; Jev API key sourced from GitHub Environment API_KEYS, secret JEV_API_KEY.
- Native artifact ID: {args.workflow_artifact_id}; uploaded by this run with 30-day retention.
- Ten raw outputs match frozen summary hashes; actual model(s): {', '.join(sorted(models))}; each file has one run and 16 native answers.
- Per-file raw JSON SHA-256: qa/jev-entry-batches/{args.batch_id}/native-json-sha256.txt.
- Ten Mapping files preserve original probabilities, Noul, confidence and all direction probabilities; M annotations remain separate.
- Ten reader entries link research, frozen summary and Mapping; English paper titles and verified DOI links are retained.
- catalog/entries.yaml updated with this batch's ten frozen entries.
""")
    print(f"Built ten mappings and reader entries; validated raw outputs and frozen summaries for {args.batch_id}.")

if __name__ == "__main__":
    main()
