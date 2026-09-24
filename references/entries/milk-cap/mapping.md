# Mapping｜milk-cap

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: milk-cap
research_ref: references/entries/milk-cap/research.md
summary_ref: references/entries/milk-cap/summary.md
summary_sha256: b708ed7f03919b7a93be49b19d793225375ea6487bcfb30478c041e0d2dda7ec
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:14:20.621957+00:00
workflow_run_id: 36018666716
workflow_artifact_id: 10815098771
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/milk-cap.json

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
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.15 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴+ | 0.08 | 0.23 | 0.31 | 0.19 | 0.27 | M-0 |
| 肝 | 0.04 | 阴- | 0.21 | 0.41 | 0.13 | 0.32 | 0.14 | M-0 |
| 脾 | 0.06 | 阴- | 0.18 | 0.39 | 0.33 | 0.03 | 0.25 | M-0 |
| 肺 | 0.04 | 阴- | 0.16 | 0.36 | 0.34 | 0.17 | 0.13 | M-0 |
| 肾 | 0.04 | 阴- | 0.24 | 0.43 | 0.36 | 0.09 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：本条无奶盖成品的直接长期人体结局证据（E-0）。47名健康成人的含打发奶油餐交叉试验为D2邻近资料，暴露是约45 g脂肪的单餐，终点为餐后甘油三酯而非疾病结局。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
