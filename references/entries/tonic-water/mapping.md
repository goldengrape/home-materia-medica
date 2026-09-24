# Mapping｜tonic-water

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 05-functional-beverages
entry_id: tonic-water
research_ref: references/entries/tonic-water/research.md
summary_ref: references/entries/tonic-water/summary.md
summary_sha256: bb66681839a4d1a876770d3a9147babc54f50c4a7b762211d0db4fd0ec3d9771
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:16:18.795963+00:00
workflow_run_id: 35986228691
workflow_artifact_id: 10802148312
native_result_ref: qa/jev-entry-batches/05-functional-beverages/raw/tonic-water.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.02 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.95）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.15 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.29 | M-IV | 奎宁带苦味；具体强度因配方而异，仅属感官类推。 |
| 甘 | 0.35 | M-IV | 含糖款有甜味；无糖款的甜感来自代糖，仅属感官类推。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.50 | 0.24 | 0.03 | 0.62 | 0.11 | M-0 |
| 肝 | 0.06 | 阳- | 0.56 | 0.27 | 0.02 | 0.67 | 0.04 | M-0 |
| 脾 | 0.05 | 阴- | 0.36 | 0.52 | 0.08 | 0.14 | 0.26 | M-0 |
| 肺 | 0.04 | 阳- | 0.34 | 0.37 | 0.07 | 0.51 | 0.05 | M-0 |
| 肾 | 0.05 | 阴- | 0.32 | 0.48 | 0.05 | 0.39 | 0.08 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：直接饮用汤力水的人体临床结局证据未检得；奎宁药物用途、风险和饮料低剂量不能混作一类证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
