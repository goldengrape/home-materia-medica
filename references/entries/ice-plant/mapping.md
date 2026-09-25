# Mapping｜ice-plant

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 18-vegetables-and-salads
entry_id: ice-plant
research_ref: references/entries/ice-plant/research.md
summary_ref: references/entries/ice-plant/summary.md
summary_sha256: 12234c75fbe559a415370219a0e8504c879ed260b88db80603bc1afd2097d5ae
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:14:06.935316+00:00
workflow_run_id: 36101936949
workflow_artifact_id: 10848839478
native_result_ref: qa/jev-entry-batches/18-vegetables-and-salads/raw/ice-plant.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.19 | M-IV | 冰草叶常有咸鲜感，实际味道受栽培与清洗影响；仅记录食味。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.24 | 0.32 | 0.16 | 0.44 | 0.08 | M-0 |
| 肝 | 0.05 | 阳- | 0.26 | 0.44 | 0.09 | 0.44 | 0.03 | M-0 |
| 脾 | 0.06 | 阴- | 0.42 | 0.56 | 0.16 | 0.07 | 0.21 | M-0 |
| 肺 | 0.05 | 阴- | 0.19 | 0.39 | 0.36 | 0.22 | 0.03 | M-0 |
| 肾 | 0.05 | 阴- | 0.52 | 0.64 | 0.19 | 0.13 | 0.04 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：鲜冰草叶没有可用的直接人体临床结果（E-0）。已登记提取物试验未公布结果；细胞实验不构成人体疗效证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
