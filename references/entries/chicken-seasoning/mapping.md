# Mapping｜chicken-seasoning

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 29-seasonings
entry_id: chicken-seasoning
research_ref: references/entries/chicken-seasoning/research.md
summary_ref: references/entries/chicken-seasoning/summary.md
summary_sha256: f6feb1313f7317b7468de4c3436e62c6bad25834c9a82d66df842e7c6c0483af
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T08:05:19.802289+00:00
workflow_run_id: 36111002019
workflow_artifact_id: 10852594602
native_result_ref: qa/jev-entry-batches/29-seasonings/raw/chicken-seasoning.json

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
| 甘 | 0.18 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.46 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.36 | 0.27 | 0.05 | 0.16 | 0.52 | M-0 |
| 肝 | 0.05 | 阴- | 0.19 | 0.39 | 0.04 | 0.29 | 0.28 | M-0 |
| 脾 | 0.09 | 阳+ | 0.43 | 0.37 | 0.04 | 0.02 | 0.57 | M-0 |
| 肺 | 0.05 | 阴- | 0.30 | 0.47 | 0.08 | 0.13 | 0.32 | M-0 |
| 肾 | 0.05 | 阴- | 0.46 | 0.60 | 0.07 | 0.06 | 0.27 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据来自中国商品营养标签数据库及英中酱料标签横断面调查；数据按原分类报告，不能代替实验室检测、单品数据或实际食用剂量。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
