# Mapping｜mozzarella-cheese

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: mozzarella-cheese
research_ref: references/entries/mozzarella-cheese/research.md
summary_ref: references/entries/mozzarella-cheese/summary.md
summary_sha256: 8e7a1c0999c25a7ece8cc22d5ccb24861f1d5c909f679643c7b70596f9a432db
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:55.935005+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/mozzarella-cheese.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.11 | M-IV | 乳香和微咸、微甘可随水分、盐分及成熟程度变化；仅为感官描述。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.22 | M-IV | 咸味随盐水、盐渍方式与品牌变化。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴- | 0.04 | 0.28 | 0.24 | 0.20 | 0.28 | M-0 |
| 肝 | 0.04 | 阴- | 0.33 | 0.50 | 0.13 | 0.23 | 0.14 | M-0 |
| 脾 | 0.06 | 阴- | 0.24 | 0.44 | 0.20 | 0.04 | 0.32 | M-0 |
| 肺 | 0.04 | 阴- | 0.23 | 0.42 | 0.37 | 0.10 | 0.11 | M-0 |
| 肾 | 0.04 | 阴- | 0.35 | 0.52 | 0.30 | 0.07 | 0.11 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：马苏里拉的长期临床结局为E-0；直接产品证据主要是美国零售样品钠含量调查（D0成分资料），并非人体干预。硬质奶酪对照试验只能作D2类别背景。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
