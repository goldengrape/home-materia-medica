# Mapping｜fresh-milk

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: fresh-milk
research_ref: references/entries/fresh-milk/research.md
summary_ref: references/entries/fresh-milk/summary.md
summary_sha256: b3fbd4deb9ba430364d3b6d59da37a4d69bec03f69fa3b3dcb009f79275398b7
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:37.179157+00:00
workflow_run_id: 36010531585
workflow_artifact_id: 10812197530
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/fresh-milk.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.10 | M-0 |
| 凉 | 0.73 | M-0 |
| 平 | 0.17 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**凉**（Choice confidence 0.65）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.94 | M-IV | 乳糖带来轻微甜味，脂肪等级会影响口感；此处是感官描述，不等于传统药味或功效。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.10 | 阴+ | 0.53 | 0.01 | 0.65 | 0.33 | 0.01 | M-0 |
| 肝 | 0.06 | 阴+ | 0.42 | 0.07 | 0.57 | 0.35 | 0.01 | M-0 |
| 脾 | 0.44 | 阴+ | 0.67 | 0.01 | 0.76 | 0.08 | 0.15 | M-0 |
| 肺 | 0.14 | 阴+ | 0.63 | 0.02 | 0.72 | 0.26 | 0.00 | M-0 |
| 肾 | 0.17 | 阴+ | 0.82 | 0.02 | 0.86 | 0.11 | 0.01 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：全脂液态奶与脱脂奶的短期对比：17名完成者、0.5升/日、每期3周，HDL有组间差异，其余所测指标未见显著差异（D0，单个小型RCT，E-C）。长期健康结局和具体鲜奶加工方式仍不明。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
