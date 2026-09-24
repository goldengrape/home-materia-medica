# Mapping｜butter

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: butter
research_ref: references/entries/butter/research.md
summary_ref: references/entries/butter/summary.md
summary_sha256: bbd1c8a56fcc793bd98fe3c9f15a6f92943815fb830dbbb0e6cf30aee26aa1a9
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:57.588026+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/butter.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.91 | M-0 |
| 温 | 0.08 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.89）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.19 | M-IV | 乳脂带来浓郁、柔和的感官口感；有盐/发酵款风味不同。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.12 | M-IV | 有盐黄油的咸味随商品配方变化。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阳+ | 0.38 | 0.15 | 0.17 | 0.14 | 0.54 | M-0 |
| 肝 | 0.06 | 阳+ | 0.12 | 0.29 | 0.26 | 0.11 | 0.34 | M-0 |
| 脾 | 0.10 | 阳+ | 0.36 | 0.17 | 0.30 | 0.01 | 0.52 | M-0 |
| 肺 | 0.04 | 阴+ | 0.19 | 0.30 | 0.39 | 0.08 | 0.23 | M-0 |
| 肾 | 0.05 | 阴+ | 0.16 | 0.28 | 0.38 | 0.04 | 0.30 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：黄油对短期血脂有直接随机比较证据（D0；E-C）：50 g/d、4周时LDL-C高于橄榄油和椰子油组；不等于临床事件证据。观察性结局综述不能单独解释因果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
