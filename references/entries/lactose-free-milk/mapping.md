# Mapping｜lactose-free-milk

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: lactose-free-milk
research_ref: references/entries/lactose-free-milk/research.md
summary_ref: references/entries/lactose-free-milk/summary.md
summary_sha256: f1474d81448b8866f769e890119a2347ad37516104829c3d6f00ed1e07c60f33
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:39.383293+00:00
workflow_run_id: 36009889022
workflow_artifact_id: 10812190966
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/lactose-free-milk.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.36 | M-IV | 乳糖酶水解后甜味可能更明显；具体感受取决于产品及添加物。仅作感官描述。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴+ | 0.39 | 0.20 | 0.54 | 0.08 | 0.18 | M-0 |
| 肝 | 0.05 | 阴- | 0.26 | 0.44 | 0.18 | 0.24 | 0.14 | M-0 |
| 脾 | 0.31 | 阴- | 0.28 | 0.46 | 0.25 | 0.01 | 0.28 | M-0 |
| 肺 | 0.06 | 阴+ | 0.41 | 0.32 | 0.56 | 0.05 | 0.07 | M-0 |
| 肾 | 0.07 | 阴+ | 0.42 | 0.33 | 0.56 | 0.03 | 0.08 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：乳糖水解奶：30名自述严重不耐受者、其中21名为乳糖吸收不良者，在240毫升/日、各1周条件下未见乳糖水解奶与普通奶的总体症状差异（D0，短期小样本，E-C）。2025年产品比较受A2酪蛋白因素影响；无乳糖不等于无牛奶过敏原。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
