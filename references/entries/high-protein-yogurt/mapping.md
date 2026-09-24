# Mapping｜high-protein-yogurt

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: high-protein-yogurt
research_ref: references/entries/high-protein-yogurt/research.md
summary_ref: references/entries/high-protein-yogurt/summary.md
summary_sha256: 1c7ec0e252bda979ad49baf5571760e1dc033d39b6a339fecba94ab14e42ad04
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:40.252493+00:00
workflow_run_id: 36009889022
workflow_artifact_id: 10812190966
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/high-protein-yogurt.json

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
| 酸 | 0.18 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.21 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.18 | 0.23 | 0.30 | 0.09 | 0.38 | M-0 |
| 肝 | 0.04 | 阴- | 0.24 | 0.44 | 0.11 | 0.27 | 0.18 | M-0 |
| 脾 | 0.13 | 阳+ | 0.53 | 0.20 | 0.14 | 0.01 | 0.65 | M-0 |
| 肺 | 0.04 | 阴+ | 0.21 | 0.36 | 0.41 | 0.10 | 0.13 | M-0 |
| 肾 | 0.05 | 阴+ | 0.34 | 0.34 | 0.50 | 0.05 | 0.11 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：高蛋白希腊式酸奶：32名健康女性、14克对5克蛋白、等能量急性对照，食欲及随后摄食未见差异（D0，单次试验，E-C）。Kashk研究有低能量饮食和益生菌等共干预（D1），不能归因于普通高蛋白酸奶。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
