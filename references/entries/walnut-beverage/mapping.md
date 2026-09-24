# Mapping｜walnut-beverage

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 06-nuts-cocoa-chocolate
entry_id: walnut-beverage
research_ref: references/entries/walnut-beverage/research.md
summary_ref: references/entries/walnut-beverage/summary.md
summary_sha256: 10d4751e80ba60e1452cb4cbcaaa6d013b68775c64a6b7bfb9f6862614e6695b
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:44:19.493187+00:00
workflow_run_id: 35988940964
workflow_artifact_id: 10803037445
native_result_ref: qa/jev-entry-batches/06-nuts-cocoa-chocolate/raw/walnut-beverage.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.03 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.24 | M-IV | 核桃仁的坚果香常伴轻甜感，糖的甜度依产品而异，仅属感官类推。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.29 | 0.11 | 0.46 | 0.08 | 0.35 | M-0 |
| 肝 | 0.08 | 阴+ | 0.42 | 0.19 | 0.57 | 0.06 | 0.18 | M-0 |
| 脾 | 0.10 | 阴+ | 0.23 | 0.15 | 0.42 | 0.02 | 0.41 | M-0 |
| 肺 | 0.06 | 阴+ | 0.61 | 0.17 | 0.71 | 0.04 | 0.08 | M-0 |
| 肾 | 0.12 | 阴+ | 0.67 | 0.08 | 0.76 | 0.02 | 0.14 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：没有找到可代表市售核桃乳的直接人体健康结局试验。整核桃的临床研究不能越过过滤、稀释和加料过程直接转写为核桃乳功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
