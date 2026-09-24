# Mapping｜sugar-substitute-dessert

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 10-confections-nuts
entry_id: sugar-substitute-dessert
research_ref: references/entries/sugar-substitute-dessert/research.md
summary_ref: references/entries/sugar-substitute-dessert/summary.md
summary_sha256: bbf2925fe87c5296be45d4f20287ee9002b4ee2595a535622cc157553223f089
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:07:09.063245+00:00
workflow_run_id: 35997042911
workflow_artifact_id: 10806612454
native_result_ref: qa/jev-entry-batches/10-confections-nuts/raw/sugar-substitute-dessert.json

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
| 甘 | 0.30 | M-IV | 甜味来自所用糖醇、非糖甜味剂或仍保留的糖；后味与甜味持续时间因配方而异。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.39 | 0.21 | 0.08 | 0.54 | 0.17 | M-0 |
| 肝 | 0.04 | 阳- | 0.27 | 0.43 | 0.04 | 0.45 | 0.08 | M-0 |
| 脾 | 0.11 | 阴- | 0.54 | 0.65 | 0.04 | 0.06 | 0.25 | M-0 |
| 肺 | 0.04 | 阴- | 0.21 | 0.41 | 0.19 | 0.30 | 0.10 | M-0 |
| 肾 | 0.04 | 阴- | 0.42 | 0.57 | 0.14 | 0.18 | 0.11 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：scFOS试验为 D0/D1（特定替糖和两种成品的急性人体反应），研究结果受食品基质影响；非糖甜味剂长期指导与某一产品临床作用属于不同问题。整个代糖甜点类别暂无可稳定归纳的长期结局（E-0/E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
