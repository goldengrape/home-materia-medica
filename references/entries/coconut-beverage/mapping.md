# Mapping｜coconut-beverage

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 05-functional-beverages
entry_id: coconut-beverage
research_ref: references/entries/coconut-beverage/research.md
summary_ref: references/entries/coconut-beverage/summary.md
summary_sha256: a02d719cbccd12b24d128d7ea0204f08c8c05b164cd0eaaed6f59a8717a4c266
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:16:21.413439+00:00
workflow_run_id: 35986228691
workflow_artifact_id: 10802148312
native_result_ref: qa/jev-entry-batches/05-functional-beverages/raw/coconut-beverage.json

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
| 甘 | 0.24 | M-IV | 椰香与甜味受椰基浓度和添加糖影响，仅属感官类推。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.16 | 0.26 | 0.37 | 0.17 | 0.20 | M-0 |
| 肝 | 0.05 | 阴- | 0.24 | 0.44 | 0.25 | 0.21 | 0.10 | M-0 |
| 脾 | 0.08 | 阴- | 0.15 | 0.35 | 0.32 | 0.02 | 0.31 | M-0 |
| 肺 | 0.05 | 阴+ | 0.34 | 0.33 | 0.50 | 0.09 | 0.08 | M-0 |
| 肾 | 0.06 | 阴+ | 0.28 | 0.39 | 0.46 | 0.05 | 0.10 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：现有证据以市场组成分析和产品定义资料为主；2026 年 RCT 网络荟萃分析不含椰奶饮料，不能据此作统一健康效果判断。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
