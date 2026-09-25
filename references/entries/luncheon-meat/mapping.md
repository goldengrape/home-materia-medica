# Mapping｜luncheon-meat

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 24-processed-meat-chinese-snacks
entry_id: luncheon-meat
research_ref: references/entries/luncheon-meat/research.md
summary_ref: references/entries/luncheon-meat/summary.md
summary_sha256: 6a1def4d552dcdd06223d3c93699986c88f759c0e4d29b3392ee646e33657f5e
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T07:35:04.515989+00:00
workflow_run_id: 36108366692
workflow_artifact_id: 10851932295
native_result_ref: qa/jev-entry-batches/24-processed-meat-chinese-snacks/raw/luncheon-meat.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.03 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.42 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.44 | 0.20 | 0.06 | 0.15 | 0.59 | M-0 |
| 肝 | 0.04 | 阴- | 0.15 | 0.37 | 0.06 | 0.21 | 0.36 | M-0 |
| 脾 | 0.08 | 阳+ | 0.54 | 0.28 | 0.04 | 0.02 | 0.66 | M-0 |
| 肺 | 0.04 | 阴- | 0.32 | 0.49 | 0.04 | 0.14 | 0.33 | M-0 |
| 肾 | 0.05 | 阴- | 0.30 | 0.48 | 0.06 | 0.04 | 0.42 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：资料来自对应队列、商品抽检、监管规范或近似熟食研究；各条限制按原研究和抽样范围保留。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
