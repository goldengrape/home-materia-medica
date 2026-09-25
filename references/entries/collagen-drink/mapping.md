# Mapping｜collagen-drink

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 32-microbiome-sports-nutrition
entry_id: collagen-drink
research_ref: references/entries/collagen-drink/research.md
summary_ref: references/entries/collagen-drink/summary.md
summary_sha256: d50ba250068c81ac42ea331253bfe409959c797db57047b0a53e65ec7de28144
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T08:34:04.854591+00:00
workflow_run_id: 36113611688
workflow_artifact_id: 10853449193
native_result_ref: qa/jev-entry-batches/32-microbiome-sports-nutrition/raw/collagen-drink.json

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
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.26 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.47 | 0.15 | 0.60 | 0.10 | 0.15 | M-0 |
| 肝 | 0.05 | 阴+ | 0.48 | 0.19 | 0.61 | 0.13 | 0.07 | M-0 |
| 脾 | 0.11 | 阴+ | 0.35 | 0.11 | 0.52 | 0.02 | 0.35 | M-0 |
| 肺 | 0.07 | 阴+ | 0.73 | 0.14 | 0.80 | 0.03 | 0.03 | M-0 |
| 肾 | 0.09 | 阴+ | 0.81 | 0.09 | 0.86 | 0.02 | 0.03 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列菌株、成分、剂量、人群和结局；本条是商品类别，不代表任一品牌的固定配方或已证实功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
