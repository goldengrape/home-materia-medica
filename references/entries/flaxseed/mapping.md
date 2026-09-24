# Mapping｜flaxseed

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 12-seeds-and-butters
entry_id: flaxseed
research_ref: references/entries/flaxseed/research.md
summary_ref: references/entries/flaxseed/summary.md
summary_sha256: 2e3b520e2bb0c6120e95f176a207e225f8fb16588d1587f5374cd0ed2d9e38c4
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T13:36:13.873008+00:00
workflow_run_id: 36006762786
workflow_artifact_id: 10810717078
native_result_ref: qa/jev-entry-batches/12-seeds-and-butters/raw/flaxseed.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.29 | M-0 |
| 温 | 0.71 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**温**（Choice confidence 0.63）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.76 | M-IV | 籽粒有淡淡坚果香和油润感；感官记录与古籍药性分别呈现。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.17 | 阳+ | 0.31 | 0.06 | 0.10 | 0.36 | 0.48 | M-0 |
| 肝 | 0.11 | 阳+ | 0.16 | 0.14 | 0.26 | 0.23 | 0.37 | M-0 |
| 脾 | 0.19 | 阳+ | 0.59 | 0.18 | 0.12 | 0.00 | 0.70 | M-0 |
| 肺 | 0.09 | 阴+ | 0.22 | 0.23 | 0.41 | 0.04 | 0.32 | M-0 |
| 肾 | 0.12 | 阳+ | 0.26 | 0.23 | 0.25 | 0.08 | 0.44 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Rodriguez-Leyva 等 RCT 为 D0（磨碎亚麻籽食品）：110 名外周动脉疾病患者，30 g/日，6 个月；收缩压约 −10 mmHg、舒张压约 −7 mmHg，较高基线 SBP 亚组约 −15/−7 mmHg。适用范围窄，且研究剂量高（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
