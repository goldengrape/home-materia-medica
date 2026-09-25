# Mapping｜insect-protein-food

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 35-new-foods-and-breakfast
entry_id: insect-protein-food
research_ref: references/entries/insect-protein-food/research.md
summary_ref: references/entries/insect-protein-food/summary.md
summary_sha256: 32df38ce76eac82d68cc89430b27068982497efa263bbf27ab8d634af52639e1
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:25:23.690492+00:00
workflow_run_id: 36118326153
workflow_artifact_id: 10856380611
native_result_ref: qa/jev-entry-batches/35-new-foods-and-breakfast/raw/insect-protein-food.json

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
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.14 | 0.24 | 0.11 | 0.36 | 0.29 | M-0 |
| 肝 | 0.04 | 阳- | 0.21 | 0.40 | 0.04 | 0.41 | 0.15 | M-0 |
| 脾 | 0.06 | 阳+ | 0.38 | 0.33 | 0.10 | 0.04 | 0.53 | M-0 |
| 肺 | 0.04 | 阴- | 0.25 | 0.43 | 0.11 | 0.32 | 0.14 | M-0 |
| 肾 | 0.04 | 阴- | 0.28 | 0.46 | 0.25 | 0.13 | 0.16 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列研究对象、食品形态、人群、剂量与结局；本条是类别或场景条目，不代表固定品牌配方或已证实的长期功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
