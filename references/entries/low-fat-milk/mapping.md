# Mapping｜low-fat-milk

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: low-fat-milk
research_ref: references/entries/low-fat-milk/research.md
summary_ref: references/entries/low-fat-milk/summary.md
summary_sha256: e8fe9617c10a442866093cd53b0b5e7b3567c0687aaf86edee9365bbe70967fc
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:37.587474+00:00
workflow_run_id: 36010531585
workflow_artifact_id: 10812197530
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/low-fat-milk.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.36 | M-IV | 乳糖仍提供轻微甜味，去除部分乳脂会改变口感；仅作感官描述。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.07 | 阴+ | 0.41 | 0.12 | 0.56 | 0.11 | 0.21 | M-0 |
| 肝 | 0.06 | 阴+ | 0.15 | 0.30 | 0.35 | 0.22 | 0.13 | M-0 |
| 脾 | 0.12 | 阴+ | 0.44 | 0.13 | 0.58 | 0.01 | 0.28 | M-0 |
| 肺 | 0.06 | 阴+ | 0.63 | 0.17 | 0.72 | 0.05 | 0.06 | M-0 |
| 肾 | 0.07 | 阴+ | 0.52 | 0.26 | 0.64 | 0.02 | 0.08 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：1%低脂液态奶：一项55人、每日3份、6周RCT未见日间血压差异；甘油三酯较无乳对照高、HDL较低（D0，单项短期试验，E-C）。将奶、奶酪和酸奶合用的研究属D2，不能归因于牛奶。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
