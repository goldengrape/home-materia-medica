# Mapping｜fermented-chili-sauce

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: fermented-chili-sauce
research_ref: references/entries/fermented-chili-sauce/research.md
summary_ref: references/entries/fermented-chili-sauce/summary.md
summary_sha256: b02379cd38afe183118ac7590ece140cccc0b95cf98fffd2c5ba08ee133a4b8e
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:14:23.608412+00:00
workflow_run_id: 36018666716
workflow_artifact_id: 10815098771
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/fermented-chili-sauce.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.73 | M-0 |
| 温 | 0.15 | M-0 |
| 热 | 0.12 | M-0 |

Jev Choice：**平**（Choice confidence 0.66）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.24 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.49 | M-IV | 辣味主要取决于辣椒类型与用量。 |
| 咸 | 0.32 | M-IV | 盐量和产品配方决定咸度。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.40 | 0.18 | 0.01 | 0.26 | 0.55 | M-0 |
| 肝 | 0.07 | 阴- | 0.13 | 0.34 | 0.01 | 0.31 | 0.34 | M-0 |
| 脾 | 0.09 | 阴- | 0.40 | 0.55 | 0.01 | 0.04 | 0.40 | M-0 |
| 肺 | 0.06 | 阴- | 0.16 | 0.37 | 0.02 | 0.26 | 0.35 | M-0 |
| 肾 | 0.05 | 阴- | 0.30 | 0.47 | 0.02 | 0.12 | 0.39 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：广义发酵辣椒酱的人体结局证据不足（E-0）；Kochujang小型比较试验为D2相邻产品，低盐酱研究是食品工艺而非人体证据，均不能证明本条广义功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
