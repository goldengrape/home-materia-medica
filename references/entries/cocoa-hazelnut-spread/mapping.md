# Mapping｜cocoa-hazelnut-spread

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 06-nuts-cocoa-chocolate
entry_id: cocoa-hazelnut-spread
research_ref: references/entries/cocoa-hazelnut-spread/research.md
summary_ref: references/entries/cocoa-hazelnut-spread/summary.md
summary_sha256: 49b973c3d63c74453eeb9100ec350b95414e2d6a1080d296c15f3f9735c044e4
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:44:22.500243+00:00
workflow_run_id: 35988940964
workflow_artifact_id: 10803037445
native_result_ref: qa/jev-entry-batches/06-nuts-cocoa-chocolate/raw/cocoa-hazelnut-spread.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.13 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.63 | M-IV | 糖是常见主要甜味来源，烘焙榛子和可可提供香气，依品牌而异。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.25 | 0.17 | 0.24 | 0.15 | 0.44 | M-0 |
| 肝 | 0.06 | 阴- | 0.05 | 0.28 | 0.23 | 0.25 | 0.24 | M-0 |
| 脾 | 0.10 | 阳+ | 0.34 | 0.25 | 0.23 | 0.02 | 0.50 | M-0 |
| 肺 | 0.05 | 阴- | 0.18 | 0.39 | 0.31 | 0.14 | 0.16 | M-0 |
| 肾 | 0.05 | 阴- | 0.17 | 0.38 | 0.37 | 0.06 | 0.19 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：没有足以支持普通可可榛子酱临床功效的直接人体证据。已登记的减糖抹酱对照研究属于特定替代配方和糖尿病人群，不能当作常规抹酱结果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
