# Mapping｜teriyaki-sauce

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 28-condiments
entry_id: teriyaki-sauce
research_ref: references/entries/teriyaki-sauce/research.md
summary_ref: references/entries/teriyaki-sauce/summary.md
summary_sha256: 669d83432f0975d06c6e61b70f9c067a6ef904b4a2d293c63d0f7d411ff70695
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T08:00:44.904680+00:00
workflow_run_id: 36110585806
workflow_artifact_id: 10852880984
native_result_ref: qa/jev-entry-batches/28-condiments/raw/teriyaki-sauce.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.52 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.61 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.12 | 0.29 | 0.07 | 0.30 | 0.34 | M-0 |
| 肝 | 0.05 | 阳- | 0.20 | 0.37 | 0.04 | 0.40 | 0.19 | M-0 |
| 脾 | 0.07 | 阳+ | 0.27 | 0.36 | 0.14 | 0.04 | 0.46 | M-0 |
| 肺 | 0.04 | 阴- | 0.25 | 0.44 | 0.09 | 0.25 | 0.22 | M-0 |
| 肾 | 0.04 | 阴- | 0.46 | 0.59 | 0.06 | 0.11 | 0.24 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：调味料证据主要来自商品包装营养标签汇总和餐馆菜品配方估算；数据不等同于每个品牌的实验室检测、人体试验或实际用量。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
