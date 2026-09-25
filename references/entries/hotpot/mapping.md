# Mapping｜hotpot

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 27-cheese-chinese-meals
entry_id: hotpot
research_ref: references/entries/hotpot/research.md
summary_ref: references/entries/hotpot/summary.md
summary_sha256: 9991a0ed6fbc7088b6124b6841253c8ffdb91ddfb82934f95237f277ff93c116
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T07:55:20.521405+00:00
workflow_run_id: 36110123486
workflow_artifact_id: 10853240341
native_result_ref: qa/jev-entry-batches/27-cheese-chinese-meals/raw/hotpot.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.96 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.03 | M-0 |

Jev Choice：**平**（Choice confidence 0.95）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.37 | 0.20 | 0.04 | 0.24 | 0.52 | M-0 |
| 肝 | 0.05 | 阴- | 0.15 | 0.35 | 0.02 | 0.36 | 0.27 | M-0 |
| 脾 | 0.08 | 阳+ | 0.40 | 0.38 | 0.02 | 0.05 | 0.55 | M-0 |
| 肺 | 0.04 | 阴- | 0.27 | 0.45 | 0.05 | 0.23 | 0.27 | M-0 |
| 肾 | 0.04 | 阴- | 0.29 | 0.47 | 0.04 | 0.08 | 0.41 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据分别来自餐厅菜品配方估算、现场食物称重、官方食物成分数据库或污染物样品检测；类别、样本和研究目的的限制按来源保留。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
