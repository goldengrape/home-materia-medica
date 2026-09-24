# Mapping｜three-in-one-coffee

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

entry_id: three-in-one-coffee
research_ref: references/entries/three-in-one-coffee/research.md
summary_ref: references/entries/three-in-one-coffee/summary.md
summary_sha256: 71e0c9dc0ce909df7083f9822ff5359ebf136397f4ba7c6d83b7fe09de0f7bb5
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T09:30:30.292053+00:00
workflow_run_id: 35981638241
workflow_artifact_id: 10800875453
native_result_ref: qa/jev-coffee-soda-batch/raw/three-in-one-coffee.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.95 | M-0 |
| 温 | 0.04 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.94）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 苦 | 0.21 | M-IV | 咖啡底可能呈苦，配料改变强度，仅作类推。 |
| 甘 | 0.41 | M-IV | 该类预混包常含糖，甜感随品牌变化，仅作类推。 |
| 辛 | 0.15 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阳+ | 0.56 | 0.12 | 0.01 | 0.20 | 0.67 | M-0 |
| 肝 | 0.07 | 阳- | 0.23 | 0.26 | 0.01 | 0.43 | 0.30 | M-0 |
| 脾 | 0.08 | 阳+ | 0.30 | 0.39 | 0.08 | 0.06 | 0.47 | M-0 |
| 肺 | 0.06 | 阳+ | 0.27 | 0.30 | 0.03 | 0.22 | 0.45 | M-0 |
| 肾 | 0.06 | 阳+ | 0.26 | 0.40 | 0.02 | 0.14 | 0.44 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 明确支持的感官类推标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：产品成分抽样不是人体试验，也不代表现售全球品牌。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
