# Mapping｜spicy-nuts

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: spicy-nuts
research_ref: references/entries/spicy-nuts/research.md
summary_ref: references/entries/spicy-nuts/summary.md
summary_sha256: 9a32cde42ea29057c7f0aaa03fe3ed4f3502fe02292faf84c23f8421bfdea1a8
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:20.899637+00:00
workflow_run_id: 36002836267
workflow_artifact_id: 10808628357
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/spicy-nuts.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.91 | M-0 |
| 温 | 0.06 | M-0 |
| 热 | 0.03 | M-0 |

Jev Choice：**平**（Choice confidence 0.88）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.14 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.43 | M-IV | 辣味来自辣椒或复合香辛料，感受与实际辣椒素含量及个人耐受有关；不等同传统药味或功效。 |
| 咸 | 0.17 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.46 | 0.12 | 0.01 | 0.27 | 0.60 | M-0 |
| 肝 | 0.06 | 阳+ | 0.22 | 0.23 | 0.03 | 0.33 | 0.41 | M-0 |
| 脾 | 0.08 | 阳+ | 0.34 | 0.38 | 0.02 | 0.10 | 0.50 | M-0 |
| 肺 | 0.05 | 阳+ | 0.19 | 0.31 | 0.02 | 0.28 | 0.39 | M-0 |
| 肾 | 0.04 | 阳+ | 0.21 | 0.36 | 0.04 | 0.19 | 0.41 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：辣味树坚果直接人体干预证据未建立（E-0）。辣椒素、辣椒或其他辛味食品仅属 D3/D4 邻近证据，不据此推断整类产品的食欲、体重或代谢效应。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
