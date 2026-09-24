# Mapping｜shelf-stable-yogurt

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: shelf-stable-yogurt
research_ref: references/entries/shelf-stable-yogurt/research.md
summary_ref: references/entries/shelf-stable-yogurt/summary.md
summary_sha256: 58bdcdec3da16bcd1dd9c70420fc207152fc4ce9baed3127f9f85960dbe6584f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:55.592038+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/shelf-stable-yogurt.json

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
| 酸 | 0.19 | M-IV | 酸味随菌种与发酵、后处理而异，品牌配方差别较大。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.19 | M-IV | 甜度按配料与营养标签判断；仅为感官描述。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.08 | 0.23 | 0.30 | 0.20 | 0.27 | M-0 |
| 肝 | 0.04 | 阴- | 0.29 | 0.47 | 0.09 | 0.31 | 0.13 | M-0 |
| 脾 | 0.10 | 阳+ | 0.36 | 0.33 | 0.14 | 0.01 | 0.52 | M-0 |
| 肺 | 0.05 | 阴+ | 0.27 | 0.35 | 0.45 | 0.10 | 0.10 | M-0 |
| 肾 | 0.05 | 阴+ | 0.30 | 0.37 | 0.48 | 0.06 | 0.09 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：鲜/巴氏酸奶随机试验提供D2邻近证据：125 g、每日3次、8周，测量免疫细胞/细胞因子而非疾病预防；对常温零售产品的长期临床结局仍为E-0。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
