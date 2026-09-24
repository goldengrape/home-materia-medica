# Mapping｜natto

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: natto
research_ref: references/entries/natto/research.md
summary_ref: references/entries/natto/summary.md
summary_sha256: f00c3010cf159d82818f8550fee42d248691eea0169c39cf00ecadd84761b637
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:14:21.355865+00:00
workflow_run_id: 36019837801
workflow_artifact_id: 10816226594
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/natto.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.18 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.07 | 阳- | 0.07 | 0.29 | 0.12 | 0.31 | 0.28 | M-0 |
| 肝 | 0.09 | 阴- | 0.20 | 0.40 | 0.14 | 0.31 | 0.15 | M-0 |
| 脾 | 0.12 | 阴- | 0.29 | 0.46 | 0.09 | 0.02 | 0.43 | M-0 |
| 肺 | 0.06 | 阴- | 0.22 | 0.42 | 0.28 | 0.17 | 0.13 | M-0 |
| 肾 | 0.22 | 阴+ | 0.31 | 0.24 | 0.49 | 0.02 | 0.25 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：纳豆骨骼证据来自73名绝经前女性一年试验，骨硬度指数无显著差异、仅部分替代性骨转换指标变化（E-C）；未测骨折获益。维生素K—华法林相互作用属于明确照护边界。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
