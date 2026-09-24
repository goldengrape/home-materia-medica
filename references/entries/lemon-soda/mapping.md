# Mapping｜lemon-soda

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

entry_id: lemon-soda
research_ref: references/entries/lemon-soda/research.md
summary_ref: references/entries/lemon-soda/summary.md
summary_sha256: fd57cf58c14aaa5c64412de5029e93351b9adc50a9491bb3279b431c9d07eb4a
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T09:30:31.098802+00:00
workflow_run_id: 35981638241
workflow_artifact_id: 10800875453
native_result_ref: qa/jev-coffee-soda-batch/raw/lemon-soda.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.04 | M-0 |
| 凉 | 0.10 | M-0 |
| 平 | 0.86 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.82）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.45 | M-IV | 柠檬风味/酸味剂可形成酸感，强度依配方，仅作类推。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 甘 | 0.30 | M-IV | 许多商业款含甜味来源，但无糖款存在，仅作类推。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.29 | 0.31 | 0.12 | 0.47 | 0.10 | M-0 |
| 肝 | 0.06 | 阳- | 0.36 | 0.36 | 0.08 | 0.53 | 0.03 | M-0 |
| 脾 | 0.06 | 阴- | 0.44 | 0.58 | 0.16 | 0.15 | 0.11 | M-0 |
| 肺 | 0.05 | 阴- | 0.25 | 0.44 | 0.21 | 0.32 | 0.03 | M-0 |
| 肾 | 0.04 | 阴- | 0.43 | 0.57 | 0.17 | 0.21 | 0.05 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 明确支持的感官类推标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：指定品牌的体外样品不能代表全品类，也没有临床结局。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
