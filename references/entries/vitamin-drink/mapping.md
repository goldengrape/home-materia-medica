# Mapping｜vitamin-drink

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 05-functional-beverages
entry_id: vitamin-drink
research_ref: references/entries/vitamin-drink/research.md
summary_ref: references/entries/vitamin-drink/summary.md
summary_sha256: 2195f5281a3f44b063e60bf3af510a92dbbdc619565cbf6aab4b3bae5dc806e3
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:16:20.160149+00:00
workflow_run_id: 35986228691
workflow_artifact_id: 10802148312
native_result_ref: qa/jev-entry-batches/05-functional-beverages/raw/vitamin-drink.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 1.00）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-IV | 果汁或酸味剂可产生酸感，配方不同，仅属感官类推。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.23 | M-IV | 甜味可能来自糖或代糖；添加量随产品改变，仅属感官类推。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳- | 0.13 | 0.20 | 0.19 | 0.36 | 0.25 | M-0 |
| 肝 | 0.04 | 阳- | 0.33 | 0.36 | 0.05 | 0.50 | 0.09 | M-0 |
| 脾 | 0.06 | 阳+ | 0.22 | 0.41 | 0.12 | 0.06 | 0.41 | M-0 |
| 肺 | 0.04 | 阴- | 0.15 | 0.36 | 0.25 | 0.31 | 0.08 | M-0 |
| 肾 | 0.04 | 阴- | 0.35 | 0.50 | 0.25 | 0.13 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：人群强化食品研究不等于特定维生素饮料试验；成人 B6 UL 针对总日摄入，不是每瓶限值。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
