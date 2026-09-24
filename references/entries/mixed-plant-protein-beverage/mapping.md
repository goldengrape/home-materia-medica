# Mapping｜mixed-plant-protein-beverage

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 06-nuts-cocoa-chocolate
entry_id: mixed-plant-protein-beverage
research_ref: references/entries/mixed-plant-protein-beverage/research.md
summary_ref: references/entries/mixed-plant-protein-beverage/summary.md
summary_sha256: 4e80b98bbafee1857fb14ab25bd27b3301b3d298b188ba0e7b0f20ca4147d41c
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:44:19.900626+00:00
workflow_run_id: 35988940964
workflow_artifact_id: 10803037445
native_result_ref: qa/jev-entry-batches/06-nuts-cocoa-chocolate/raw/mixed-plant-protein-beverage.json

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
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.19 | M-IV | 谷物、坚果和豆类常有轻甜或坚果香，添加糖影响更大，仅属感官类推。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.11 | 0.18 | 0.30 | 0.19 | 0.33 | M-0 |
| 肝 | 0.04 | 阴- | 0.20 | 0.40 | 0.21 | 0.24 | 0.15 | M-0 |
| 脾 | 0.12 | 阳+ | 0.55 | 0.14 | 0.19 | 0.01 | 0.66 | M-0 |
| 肺 | 0.05 | 阴+ | 0.23 | 0.29 | 0.41 | 0.13 | 0.17 | M-0 |
| 肾 | 0.05 | 阴+ | 0.41 | 0.30 | 0.55 | 0.03 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：现有研究能说明配方、蛋白来源和营养标签的差异，但不足以支持所有混合饮料有相同的健康结果。选择时应以成分表、每份蛋白质和糖、强化营养素及过敏原为准。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
