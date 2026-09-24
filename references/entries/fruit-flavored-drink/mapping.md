# Mapping｜fruit-flavored-drink

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 05-functional-beverages
entry_id: fruit-flavored-drink
research_ref: references/entries/fruit-flavored-drink/research.md
summary_ref: references/entries/fruit-flavored-drink/summary.md
summary_sha256: be5d144aad7a689b1d9737b289fe7773ca0bab67e82abf8383d1914a5a948059
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:16:20.671682+00:00
workflow_run_id: 35986228691
workflow_artifact_id: 10802148312
native_result_ref: qa/jev-entry-batches/05-functional-beverages/raw/fruit-flavored-drink.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.17 | M-IV | 果酸或酸味剂可能带酸，实际由配方决定，仅属感官类推。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.42 | M-IV | 糖/代糖与果汁比例改变甜味，产品间差异明显，仅属感官类推。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.16 | 0.28 | 0.19 | 0.37 | 0.16 | M-0 |
| 肝 | 0.04 | 阳- | 0.24 | 0.41 | 0.11 | 0.43 | 0.05 | M-0 |
| 脾 | 0.07 | 阴- | 0.33 | 0.51 | 0.21 | 0.05 | 0.23 | M-0 |
| 肺 | 0.04 | 阴+ | 0.18 | 0.37 | 0.38 | 0.20 | 0.05 | M-0 |
| 肾 | 0.04 | 阴- | 0.44 | 0.58 | 0.27 | 0.10 | 0.05 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：含糖饮料替代试验是类别邻近证据；果味饮料配方与 100% 果汁之间身份差异大。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
