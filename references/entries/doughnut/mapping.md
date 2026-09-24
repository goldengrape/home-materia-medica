# Mapping｜doughnut

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 07-baked-sweets
entry_id: doughnut
research_ref: references/entries/doughnut/research.md
summary_ref: references/entries/doughnut/summary.md
summary_sha256: 3bf31a5de3117abf240dccf693355fa0a3f7d381e3d95dfb99057a1b87aef549
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:06:34.702267+00:00
workflow_run_id: 35991084364
workflow_artifact_id: 10803294243
native_result_ref: qa/jev-entry-batches/07-baked-sweets/raw/doughnut.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.96 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.03 | M-0 |

Jev Choice：**平**（Choice confidence 0.94）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.41 | M-IV | 面团本身与糖霜/馅料共同提供甜味，油炸香气会随配方变化。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.19 | 0.30 | 0.04 | 0.27 | 0.39 | M-0 |
| 肝 | 0.04 | 阴- | 0.25 | 0.44 | 0.02 | 0.37 | 0.17 | M-0 |
| 脾 | 0.07 | 阴- | 0.32 | 0.49 | 0.04 | 0.04 | 0.43 | M-0 |
| 肺 | 0.04 | 阴- | 0.38 | 0.54 | 0.09 | 0.20 | 0.17 | M-0 |
| 肾 | 0.04 | 阴- | 0.37 | 0.53 | 0.09 | 0.19 | 0.19 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：数据库记录对指定蛋糕型甜甜圈为 D0；豆渣/纤维强化研究为 D2 实验配方，不是常规商品或人体试验。普通成品临床结局证据不足（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
