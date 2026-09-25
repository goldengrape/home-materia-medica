# Mapping｜pre-workout-coffee

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 37-office-and-fitness-scenes
entry_id: pre-workout-coffee
research_ref: references/entries/pre-workout-coffee/research.md
summary_ref: references/entries/pre-workout-coffee/summary.md
summary_sha256: b90d5109f9947bd03e0dec24c20b762cbc692ab0a5c69bf621abc50272544789
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:44:07.034681+00:00
workflow_run_id: 36120250267
workflow_artifact_id: 10857540243
native_result_ref: qa/jev-entry-batches/37-office-and-fitness-scenes/raw/pre-workout-coffee.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.88 | M-0 |
| 温 | 0.10 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.85）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.18 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.16 | 阳+ | 0.78 | 0.02 | 0.00 | 0.14 | 0.84 | M-0 |
| 肝 | 0.07 | 阳+ | 0.32 | 0.17 | 0.01 | 0.34 | 0.48 | M-0 |
| 脾 | 0.05 | 阳+ | 0.34 | 0.32 | 0.01 | 0.17 | 0.50 | M-0 |
| 肺 | 0.05 | 阳+ | 0.31 | 0.24 | 0.02 | 0.26 | 0.48 | M-0 |
| 肾 | 0.06 | 阳+ | 0.24 | 0.31 | 0.02 | 0.24 | 0.43 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列配方、食品组合、人群、进食时间和结局；本条是生活场景条目，不代表固定份量或长期健康效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
