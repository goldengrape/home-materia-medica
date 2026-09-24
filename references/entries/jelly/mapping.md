# Mapping｜jelly

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 09-chilled-confections
entry_id: jelly
research_ref: references/entries/jelly/research.md
summary_ref: references/entries/jelly/summary.md
summary_sha256: 5f9e2ad8d982e37d5ee7183be5b2fdacde1234ac3e961dedee60b070522bb29c
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:48:44.539014+00:00
workflow_run_id: 35995198753
workflow_artifact_id: 10805867273
native_result_ref: qa/jev-entry-batches/09-chilled-confections/raw/jelly.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 1.00）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.03 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.40 | M-IV | 糖、果汁或甜味剂提供甜味，酸度与香精会改变感官表现。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴- | 0.20 | 0.40 | 0.18 | 0.20 | 0.22 | M-0 |
| 肝 | 0.04 | 阴- | 0.37 | 0.53 | 0.14 | 0.26 | 0.07 | M-0 |
| 脾 | 0.16 | 阴- | 0.46 | 0.60 | 0.11 | 0.03 | 0.26 | M-0 |
| 肺 | 0.05 | 阴- | 0.36 | 0.52 | 0.28 | 0.13 | 0.07 | M-0 |
| 肾 | 0.04 | 阴- | 0.57 | 0.68 | 0.22 | 0.05 | 0.05 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：该试验为 D1（特定琼脂果汁凝冻），短期胃排空和食欲指标；对不同凝胶剂的商业果冻仅为 D2。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
