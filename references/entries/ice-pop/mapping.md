# Mapping｜ice-pop

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 08-cakes-frozen-desserts
entry_id: ice-pop
research_ref: references/entries/ice-pop/research.md
summary_ref: references/entries/ice-pop/summary.md
summary_sha256: db8aa1331ed2edce1b5caac7e8bbb6e234f3a54bc85edd8a88ab1910f57695a0
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:33:58.973279+00:00
workflow_run_id: 35993741889
workflow_artifact_id: 10804164780
native_result_ref: qa/jev-entry-batches/08-cakes-frozen-desserts/raw/ice-pop.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.07 | M-0 |
| 凉 | 0.03 | M-0 |
| 平 | 0.90 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.88）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.37 | M-IV | 糖、果汁或甜味剂可提供甜味；酸度和冻结温度会改变感官甜度。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.56 | 0.16 | 0.09 | 0.67 | 0.08 | M-0 |
| 肝 | 0.04 | 阳- | 0.42 | 0.31 | 0.09 | 0.56 | 0.04 | M-0 |
| 脾 | 0.06 | 阴- | 0.31 | 0.49 | 0.15 | 0.20 | 0.16 | M-0 |
| 肺 | 0.05 | 阳- | 0.32 | 0.24 | 0.24 | 0.49 | 0.03 | M-0 |
| 肾 | 0.05 | 阴- | 0.16 | 0.38 | 0.22 | 0.35 | 0.05 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：现有来源主要用于宽品类分类与数据库检索（D2/D0，不能代表具体现售冰棒）；成品临床健康结局证据未建立（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
