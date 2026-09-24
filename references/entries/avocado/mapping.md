# Mapping｜avocado

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: avocado
research_ref: references/entries/avocado/research.md
summary_ref: references/entries/avocado/summary.md
summary_sha256: 7d5d9d3c5203f87e2fd5642114ed972dc308483a9c5088913a7422fb5fa10c11
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:14:23.967168+00:00
workflow_run_id: 36019837801
workflow_artifact_id: 10816226594
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/avocado.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.21 | M-IV | 成熟果肉可有轻微甘味和乳脂样口感，品种与成熟度影响明显；仅作感官描述。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.10 | 阴+ | 0.38 | 0.18 | 0.54 | 0.18 | 0.10 | M-0 |
| 肝 | 0.09 | 阴+ | 0.43 | 0.24 | 0.57 | 0.15 | 0.04 | M-0 |
| 脾 | 0.12 | 阴+ | 0.32 | 0.24 | 0.48 | 0.02 | 0.26 | M-0 |
| 肺 | 0.05 | 阴+ | 0.51 | 0.27 | 0.63 | 0.06 | 0.04 | M-0 |
| 肾 | 0.06 | 阴+ | 0.49 | 0.29 | 0.61 | 0.04 | 0.06 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：全果牛油果RCT结果按结局并不一致：控制喂养试验报告LDL-C变化，12周自由生活替代试验的主要胰岛素敏感性终点未显著且体重无变化（E-C）。结论限于研究膳食方案，不外推为减重或疾病治疗。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
