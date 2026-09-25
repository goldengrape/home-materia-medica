# Mapping｜erythritol

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 30-seasonings-sweeteners
entry_id: erythritol
research_ref: references/entries/erythritol/research.md
summary_ref: references/entries/erythritol/summary.md
summary_sha256: 1cecada470a4d63d5ad961d1efe32e7e5b678ca39c930fd82d71d859d5a28d6f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T08:14:29.346552+00:00
workflow_run_id: 36111832219
workflow_artifact_id: 10852887506
native_result_ref: qa/jev-entry-batches/30-seasonings-sweeteners/raw/erythritol.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.48 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.17 | 0.37 | 0.12 | 0.37 | 0.14 | M-0 |
| 肝 | 0.05 | 阴- | 0.36 | 0.52 | 0.04 | 0.39 | 0.05 | M-0 |
| 脾 | 0.29 | 阴- | 0.80 | 0.85 | 0.05 | 0.02 | 0.08 | M-0 |
| 肺 | 0.06 | 阴- | 0.47 | 0.60 | 0.11 | 0.22 | 0.07 | M-0 |
| 肾 | 0.05 | 阴- | 0.73 | 0.80 | 0.06 | 0.09 | 0.05 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据主要来自商品标签、食品标准或监管评估，不能据此断言该单品具有临床疗效；人群摄入结果与单品成分分析分别解读。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
