# Mapping｜high-protein-milk

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: high-protein-milk
research_ref: references/entries/high-protein-milk/research.md
summary_ref: references/entries/high-protein-milk/summary.md
summary_sha256: 72222140f781dbc32d8f2ed5f52455d28d56c7f0bbe228fd7681f2324821d633
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:38.928347+00:00
workflow_run_id: 36010531585
workflow_artifact_id: 10812197530
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/high-protein-milk.json

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
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.28 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.33 | 0.07 | 0.50 | 0.04 | 0.39 | M-0 |
| 肝 | 0.05 | 阴+ | 0.15 | 0.24 | 0.36 | 0.08 | 0.32 | M-0 |
| 脾 | 0.19 | 阳+ | 0.62 | 0.04 | 0.23 | 0.01 | 0.72 | M-0 |
| 肺 | 0.05 | 阴+ | 0.63 | 0.14 | 0.73 | 0.03 | 0.10 | M-0 |
| 肾 | 0.11 | 阴+ | 0.54 | 0.16 | 0.66 | 0.03 | 0.15 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：特定高蛋白乳饮在老年人肌肉结局上的RCT结果有限：37人12周、30克额外蛋白/日的研究显示阻力训练是主要作用来源；50人随机、36人完成的强化奶研究未见肌肉量/力量/功能的组间优势（D1，产品异质、样本小，E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
