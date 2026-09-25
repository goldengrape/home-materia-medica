# Mapping｜hot-pot-base

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 29-seasonings
entry_id: hot-pot-base
research_ref: references/entries/hot-pot-base/research.md
summary_ref: references/entries/hot-pot-base/summary.md
summary_sha256: 04ca76844fb513983936227bad3038e8913392644022c82e08e627bb1dd2df80
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T08:05:19.367512+00:00
workflow_run_id: 36111002019
workflow_artifact_id: 10852594602
native_result_ref: qa/jev-entry-batches/29-seasonings/raw/hot-pot-base.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.79 | M-0 |
| 温 | 0.08 | M-0 |
| 热 | 0.13 | M-0 |

Jev Choice：**平**（Choice confidence 0.74）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.42 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.45 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.43 | 0.20 | 0.01 | 0.22 | 0.57 | M-0 |
| 肝 | 0.06 | 阳- | 0.13 | 0.31 | 0.01 | 0.34 | 0.34 | M-0 |
| 脾 | 0.09 | 阴- | 0.40 | 0.56 | 0.01 | 0.07 | 0.36 | M-0 |
| 肺 | 0.05 | 阴- | 0.25 | 0.43 | 0.02 | 0.27 | 0.28 | M-0 |
| 肾 | 0.05 | 阴- | 0.45 | 0.59 | 0.01 | 0.08 | 0.32 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据来自中国商品营养标签数据库及英中酱料标签横断面调查；数据按原分类报告，不能代替实验室检测、单品数据或实际食用剂量。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
