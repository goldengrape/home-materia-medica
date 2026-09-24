# Mapping｜pumpkin-seeds

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 12-seeds-and-butters
entry_id: pumpkin-seeds
research_ref: references/entries/pumpkin-seeds/research.md
summary_ref: references/entries/pumpkin-seeds/summary.md
summary_sha256: 23e4562f9dff405231798529b4972e70f5e8764a9223f94694db02743836c64f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T13:36:14.244041+00:00
workflow_run_id: 36006762786
workflow_artifact_id: 10810717078
native_result_ref: qa/jev-entry-batches/12-seeds-and-butters/raw/pumpkin-seeds.json

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
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.17 | M-IV | 籽仁有烘烤后的坚果香与油润感；盐焗会改变感官与钠摄入。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阳- | 0.29 | 0.15 | 0.13 | 0.47 | 0.25 | M-0 |
| 肝 | 0.08 | 阴- | 0.15 | 0.36 | 0.26 | 0.26 | 0.12 | M-0 |
| 脾 | 0.10 | 阳+ | 0.26 | 0.27 | 0.27 | 0.02 | 0.44 | M-0 |
| 肺 | 0.06 | 阴- | 0.27 | 0.45 | 0.30 | 0.12 | 0.13 | M-0 |
| 肾 | 0.09 | 阴+ | 0.30 | 0.35 | 0.47 | 0.06 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Maiya 学位论文研究为 D0/D1（南瓜籽 vs 籽油主动对照），27 名非高血压绝经后女性、4.1 g/日、12 周；无安慰剂组，报告 SBP/DBP 组内变化。单项小样本学位研究仅为低确定性信号（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
