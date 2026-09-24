# Mapping｜cinnamon-roll

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 08-cakes-frozen-desserts
entry_id: cinnamon-roll
research_ref: references/entries/cinnamon-roll/research.md
summary_ref: references/entries/cinnamon-roll/summary.md
summary_sha256: 774d8c1c123538d5fbdedf0bfa313db2bf7383620b9012322294bb54e9a3bba2
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:33:57.327653+00:00
workflow_run_id: 35993741889
workflow_artifact_id: 10804164780
native_result_ref: qa/jev-entry-batches/08-cakes-frozen-desserts/raw/cinnamon-roll.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.92 | M-0 |
| 温 | 0.08 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.89）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.46 | M-IV | 馅料和糖霜通常提供甜味，肉桂香气并不等同于传统药性或临床作用。 |
| 辛 | 0.18 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.54 | 0.12 | 0.03 | 0.19 | 0.66 | M-0 |
| 肝 | 0.04 | 阳+ | 0.38 | 0.20 | 0.02 | 0.25 | 0.53 | M-0 |
| 脾 | 0.08 | 阳+ | 0.55 | 0.21 | 0.08 | 0.05 | 0.66 | M-0 |
| 肺 | 0.04 | 阳+ | 0.31 | 0.25 | 0.05 | 0.22 | 0.48 | M-0 |
| 肾 | 0.05 | 阳+ | 0.60 | 0.18 | 0.03 | 0.09 | 0.70 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：该证据为 D0（测试清单中的单款 cinnamon swirl bun），但研究目的为急性血糖/胰岛素预测，样本和终点不支持对肉桂卷整类或长期疾病结局的结论。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
