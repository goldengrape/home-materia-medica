# Mapping｜poke-bowl

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 18-vegetables-and-salads
entry_id: poke-bowl
research_ref: references/entries/poke-bowl/research.md
summary_ref: references/entries/poke-bowl/summary.md
summary_sha256: 01764eec300ee1fd2c5e60f5d57e63a8f0785ab44c542034df039b2dc05bff2b
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:14:09.819409+00:00
workflow_run_id: 36101936949
workflow_artifact_id: 10848839478
native_result_ref: qa/jev-entry-batches/18-vegetables-and-salads/raw/poke-bowl.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.15 | M-IV | 酱油、腌料和海藻可能使整餐偏咸；配方差异大，仅作感官描述。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.09 | 0.22 | 0.20 | 0.32 | 0.26 | M-0 |
| 肝 | 0.05 | 阴- | 0.20 | 0.40 | 0.19 | 0.33 | 0.08 | M-0 |
| 脾 | 0.08 | 阳+ | 0.47 | 0.33 | 0.03 | 0.03 | 0.61 | M-0 |
| 肺 | 0.04 | 阴- | 0.33 | 0.50 | 0.09 | 0.29 | 0.12 | M-0 |
| 肾 | 0.04 | 阴- | 0.31 | 0.48 | 0.30 | 0.11 | 0.11 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：直接健康结局证据不足（E-0）；海鲜安全建议来自FDA，不能理解为每份波奇饭均有污染。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
