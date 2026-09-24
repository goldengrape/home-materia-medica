# Mapping｜sunflower-seed-kernels

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 12-seeds-and-butters
entry_id: sunflower-seed-kernels
research_ref: references/entries/sunflower-seed-kernels/research.md
summary_ref: references/entries/sunflower-seed-kernels/summary.md
summary_sha256: dda0644c66dc4a8abba8b0bc40f0fbc1301ca68fd4134cfaea1a0b2f6fbb72e0
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T13:36:14.563068+00:00
workflow_run_id: 36006762786
workflow_artifact_id: 10810717078
native_result_ref: qa/jev-entry-batches/12-seeds-and-butters/raw/sunflower-seed-kernels.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.22 | M-IV | 籽仁有烘烤坚果香与油润感；加盐/烘烤改变风味和钠含量。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.08 | 阴- | 0.02 | 0.27 | 0.27 | 0.25 | 0.21 | M-0 |
| 肝 | 0.09 | 阴+ | 0.15 | 0.33 | 0.37 | 0.17 | 0.13 | M-0 |
| 脾 | 0.11 | 阳+ | 0.28 | 0.28 | 0.24 | 0.02 | 0.46 | M-0 |
| 肺 | 0.06 | 阴- | 0.16 | 0.37 | 0.35 | 0.13 | 0.15 | M-0 |
| 肾 | 0.08 | 阴+ | 0.39 | 0.32 | 0.54 | 0.04 | 0.10 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Richmond 等随机交叉喂养试验为 D0（葵花籽仁），22 名绝经后 2 型糖尿病女性、30 g/日、每期 3 周、洗脱 4 周；与杏仁比较时 HDL-C、TG、apoA1 与 apoB100 较低，TC/LDL 两阶段均较基线下降但组间无差。小样本短期指标（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
