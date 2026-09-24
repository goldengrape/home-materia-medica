# Mapping｜miso

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: miso
research_ref: references/entries/miso/research.md
summary_ref: references/entries/miso/summary.md
summary_sha256: 81562a62181a9d22d5d342dde019dc57e4142d4351bf6ed94e249620e04e508b
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:14:22.835747+00:00
workflow_run_id: 36018666716
workflow_artifact_id: 10815098771
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/miso.json

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
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.13 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.58 | M-IV | 咸度主要受盐量、类型和冲调比例影响。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.10 | 阳- | 0.46 | 0.16 | 0.03 | 0.60 | 0.21 | M-0 |
| 肝 | 0.08 | 阳- | 0.29 | 0.40 | 0.03 | 0.46 | 0.11 | M-0 |
| 脾 | 0.12 | 阴- | 0.38 | 0.53 | 0.03 | 0.02 | 0.42 | M-0 |
| 肺 | 0.05 | 阴- | 0.46 | 0.60 | 0.06 | 0.19 | 0.15 | M-0 |
| 肾 | 0.09 | 阴- | 0.50 | 0.62 | 0.06 | 0.20 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：味噌直接人体资料有限：小型特定配方试验报告夜间血压变化，日间血压无变化且比较食品钠量不同；横断面研究未见血压关联。不能归纳为降压功效（E-C/E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
