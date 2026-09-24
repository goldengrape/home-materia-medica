# Mapping｜almond-beverage

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 05-functional-beverages
entry_id: almond-beverage
research_ref: references/entries/almond-beverage/research.md
summary_ref: references/entries/almond-beverage/summary.md
summary_sha256: 42895abc8dac02ba2316e06fd801f5005e706bd08e81cf73900c0fed4ba7e48a
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:16:20.930031+00:00
workflow_run_id: 35986228691
workflow_artifact_id: 10802148312
native_result_ref: qa/jev-entry-batches/05-functional-beverages/raw/almond-beverage.json

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
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.20 | M-IV | 杏仁香与甜味受原料、糖和香料影响，仅属感官类推。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.13 | 0.26 | 0.35 | 0.24 | 0.15 | M-0 |
| 肝 | 0.05 | 阴- | 0.18 | 0.38 | 0.28 | 0.27 | 0.07 | M-0 |
| 脾 | 0.07 | 阴+ | 0.13 | 0.32 | 0.34 | 0.03 | 0.31 | M-0 |
| 肺 | 0.07 | 阴+ | 0.54 | 0.25 | 0.66 | 0.06 | 0.03 | M-0 |
| 肾 | 0.06 | 阴+ | 0.32 | 0.38 | 0.49 | 0.06 | 0.07 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：没有杏仁饮直接人体临床效果证据；市场/标签分析和工艺研究不能证明人体结局。2026 年 RCT 网络荟萃分析未包含杏仁饮。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
