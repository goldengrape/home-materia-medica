# Mapping｜oat-latte

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

entry_id: oat-latte
research_ref: references/entries/oat-latte/research.md
summary_ref: references/entries/oat-latte/summary.md
summary_sha256: d99600b90250a767131d303b794c2ceac83139e265beba9288715cade2d66a68
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T09:30:29.430188+00:00
workflow_run_id: 35981638241
workflow_artifact_id: 10800875453
native_result_ref: qa/jev-coffee-soda-batch/raw/oat-latte.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 苦 | 0.17 | M-IV | 咖啡基底可呈苦，燕麦饮影响口感，仅作类推。 |
| 甘 | 0.17 | M-IV | 燕麦饮或添加糖可带甜感，产品不同，仅作类推。 |
| 辛 | 0.09 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阳+ | 0.46 | 0.10 | 0.02 | 0.28 | 0.60 | M-0 |
| 肝 | 0.05 | 阳- | 0.37 | 0.30 | 0.04 | 0.53 | 0.13 | M-0 |
| 脾 | 0.08 | 阳+ | 0.38 | 0.31 | 0.12 | 0.03 | 0.54 | M-0 |
| 肺 | 0.05 | 阳- | 0.13 | 0.29 | 0.18 | 0.35 | 0.18 | M-0 |
| 肾 | 0.04 | 阴- | 0.31 | 0.49 | 0.16 | 0.19 | 0.16 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 明确支持的感官类推标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：未找到燕麦拿铁成品人体试验；燕麦饮替代研究属相邻证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
