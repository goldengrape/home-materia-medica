# Mapping｜quinoa

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 20-grains-rice-pasta-legumes
entry_id: quinoa
research_ref: references/entries/quinoa/research.md
summary_ref: references/entries/quinoa/summary.md
summary_sha256: af2ccee2d0d2cd1adcf03579b17b2c43e8e53f407313f232d974e9febcc7642a
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:37:34.665583+00:00
workflow_run_id: 36103697354
workflow_artifact_id: 10850271525
native_result_ref: qa/jev-entry-batches/20-grains-rice-pasta-legumes/raw/quinoa.json

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
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.29 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴- | 0.10 | 0.33 | 0.17 | 0.18 | 0.32 | M-0 |
| 肝 | 0.08 | 阴- | 0.42 | 0.56 | 0.07 | 0.26 | 0.10 | M-0 |
| 脾 | 0.18 | 阳+ | 0.51 | 0.28 | 0.08 | 0.01 | 0.63 | M-0 |
| 肺 | 0.05 | 阴- | 0.23 | 0.42 | 0.35 | 0.04 | 0.19 | M-0 |
| 肾 | 0.07 | 阴- | 0.30 | 0.48 | 0.34 | 0.05 | 0.13 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：一项50人、12周随机试验报告50克/日藜麦种子组甘油三酯下降，但多个其他代谢结局无显著变化，尚不足以推断日常藜麦饭的长期临床效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
