#!/usr/bin/env python3
"""Render post-Jev Mapping records from raw outputs; keep native JSON untouched."""
from __future__ import annotations

import json
from pathlib import Path

from build_tea_coffee_batch_stage12 import PROFILES

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/jev-tea-coffee-batch/raw"
WORKFLOW_RUN_ID = 35977224331
WORKFLOW_ARTIFACT_ID = 10798164414


def render(entry_id: str, profile: dict) -> str:
    data = json.loads((RAW / f"{entry_id}.json").read_text(encoding="utf-8"))
    run = data["runs"][0]
    answers = run["native_answers"]
    qi = answers["qi"]
    sensory = profile["taste_m"]
    taste_names = {"sour": "酸", "bitter": "苦", "sweet": "甘", "pungent": "辛", "salty": "咸"}
    organs = {"heart": "心", "liver": "肝", "spleen": "脾", "lung": "肺", "kidney": "肾"}

    qi_rows = "\n".join(
        f"| {label} | {qi['probabilities'].get(label, 0):.2f} | M-0 |"
        for label in ["寒", "凉", "平", "温", "热"]
    )
    taste_rows = []
    for key, label in [("sour", "酸"), ("bitter", "苦"), ("sweet", "甘"), ("pungent", "辛"), ("salty", "咸")]:
        score = answers[f"taste_{key}"]["noul"]
        grade = "M-IV" if label in sensory else "M-0"
        note = sensory.get(label, "没有稳定、可追溯到本条整体的映射依据。")
        taste_rows.append(f"| {label} | {score:.2f} | {grade} | {note} |")

    meridian_rows = []
    for key, label in organs.items():
        answer = answers[f"meridian_{key}"]
        direction = answers[f"{key}_direction"]
        probs = direction["probabilities"]
        meridian_rows.append(
            f"| {label} | {answer['noul']:.2f} | {direction['choice']} | {direction['confidence']:.2f} | "
            f"{probs['阴-']:.2f} | {probs['阴+']:.2f} | {probs['阳-']:.2f} | {probs['阳+']:.2f} | M-0 |"
        )

    qi_note = (
        "模型必须选择一项，但共享母页、感官或饮用温度不足以证明本条成品四气。"
    )
    return f"""# Mapping｜{entry_id}

> Jev v0.4 是模型分类倾向；M 是随后根据 Research Dossier 所做的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

```yaml
entry_id: {entry_id}
research_ref: references/entries/{entry_id}/research.md
summary_ref: references/entries/{entry_id}/summary.md
summary_sha256: {data['summary_sha256']}
reasoning_version: {data['reasoning_version']}
five_shot_version: {data['five_shot_version']}
requested_model: {data['requested_model']}
actual_model: {run['actual_model']}
repeat_count: {len(data['runs'])}
run_timestamp_utc: {data['run_timestamp_utc']}
workflow_run_id: {WORKFLOW_RUN_ID}
workflow_artifact_id: {WORKFLOW_ARTIFACT_ID}
native_result_ref: qa/jev-tea-coffee-batch/raw/{entry_id}.json
```

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
{qi_rows}

Jev Choice：**{qi['choice']}**（Choice confidence {qi['confidence']:.2f}）。{qi_note}

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
{chr(10).join(taste_rows)}

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
{chr(10).join(meridian_rows)}

最高归经 Noul 及全部方向概率均保留；项目 0.5 只作读者层展示线，不隐藏原生输出，也不提高 M。方向 Choice 是模型回答，不表示已确认归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不等于已确证传统属性，制法/温度/配方不可自动替代证据。
- 五味：只有 dossier 明确记录感官依据的味作 M-IV 类推；不把感官推成传统功效。
- 五脏归经及方向：全部 M-0；本轮未建立可核验的直接桥梁。
- 证据距离：{profile['evidence_body']}
- 正文最大表述强度：保留样品、设计、剂量或工艺限制，不写成已证实的临床防病/治疗效果。
- 原生 JSON 未添加 M、未改写分数；全部 native answers 与 usage 均保留在 `native_result_ref`。
"""


def main() -> None:
    for entry_id, profile in PROFILES.items():
        path = ROOT / "references/entries" / entry_id / "mapping.md"
        path.write_text(render(entry_id, profile), encoding="utf-8")
    print(f"Rendered {len(PROFILES)} post-Jev Mapping records; raw JSON unchanged.")


if __name__ == "__main__":
    main()
