# Mapping｜popcorn-chicken

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 26-fried-baked-meals
entry_id: popcorn-chicken
research_ref: references/entries/popcorn-chicken/research.md
summary_ref: references/entries/popcorn-chicken/summary.md
summary_sha256: daec765d8f1455810e7187269e412c39f5af546a92b574b8da55e4ff01ae11d8
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T07:49:36.727519+00:00
workflow_run_id: 36109625604
workflow_artifact_id: 10852765535
native_result_ref: qa/jev-entry-batches/26-fried-baked-meals/raw/popcorn-chicken.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.89 | M-0 |
| 温 | 0.05 | M-0 |
| 热 | 0.06 | M-0 |

Jev Choice：**平**（Choice confidence 0.86）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.13 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.16 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.57 | 0.14 | 0.07 | 0.11 | 0.68 | M-0 |
| 肝 | 0.04 | 阴- | 0.18 | 0.39 | 0.03 | 0.23 | 0.35 | M-0 |
| 脾 | 0.08 | 阳+ | 0.55 | 0.28 | 0.03 | 0.02 | 0.66 | M-0 |
| 肺 | 0.04 | 阴- | 0.24 | 0.43 | 0.04 | 0.14 | 0.39 | M-0 |
| 肾 | 0.04 | 阳+ | 0.27 | 0.39 | 0.09 | 0.08 | 0.44 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：资料来自食物成分数据库、商品及餐馆钠监测或食品污染物抽检；研究年份、食品类别和样品范围均按原来源保留。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
