# Mapping｜grass-jelly

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 09-chilled-confections
entry_id: grass-jelly
research_ref: references/entries/grass-jelly/research.md
summary_ref: references/entries/grass-jelly/summary.md
summary_sha256: 1d53b3b368a1ad716d1c768699044c374ecf518fa8f68401aafe554f8d05ee68
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:48:45.010025+00:00
workflow_run_id: 35995198753
workflow_artifact_id: 10805867273
native_result_ref: qa/jev-entry-batches/09-chilled-confections/raw/grass-jelly.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.06 | M-0 |
| 凉 | 0.02 | M-0 |
| 平 | 0.92 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.90）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.28 | M-IV | 仙草本身带有草本/微苦感，市售甜品常配糖浆或甜味材料，整体甜味取决于配方。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳- | 0.26 | 0.27 | 0.21 | 0.44 | 0.08 | M-0 |
| 肝 | 0.05 | 阳- | 0.28 | 0.40 | 0.11 | 0.46 | 0.03 | M-0 |
| 脾 | 0.08 | 阴- | 0.34 | 0.50 | 0.24 | 0.07 | 0.19 | M-0 |
| 肺 | 0.06 | 阴+ | 0.18 | 0.33 | 0.39 | 0.26 | 0.02 | M-0 |
| 肾 | 0.06 | 阴- | 0.36 | 0.52 | 0.31 | 0.14 | 0.03 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：该人体试验为 D1（指定仙草液/凝胶和葡萄糖共摄），但小样本和单一急性指标；普通仙草冻成品的长期临床结局证据未建立。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
