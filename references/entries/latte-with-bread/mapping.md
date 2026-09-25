# Mapping｜latte-with-bread

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 35-new-foods-and-breakfast
entry_id: latte-with-bread
research_ref: references/entries/latte-with-bread/research.md
summary_ref: references/entries/latte-with-bread/summary.md
summary_sha256: c04fd70a293d3eed4cbf7d3afaf0ef131cc34524f64b2a829218629e9f5b74e8
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:25:23.976648+00:00
workflow_run_id: 36118326153
workflow_artifact_id: 10856380611
native_result_ref: qa/jev-entry-batches/35-new-foods-and-breakfast/raw/latte-with-bread.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.13 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.24 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.07 | 阳+ | 0.54 | 0.10 | 0.02 | 0.23 | 0.65 | M-0 |
| 肝 | 0.05 | 阳- | 0.30 | 0.30 | 0.02 | 0.47 | 0.21 | M-0 |
| 脾 | 0.08 | 阴- | 0.24 | 0.43 | 0.11 | 0.09 | 0.37 | M-0 |
| 肺 | 0.04 | 阴- | 0.16 | 0.37 | 0.08 | 0.33 | 0.22 | M-0 |
| 肾 | 0.04 | 阴- | 0.20 | 0.41 | 0.11 | 0.26 | 0.22 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列研究对象、食品形态、人群、剂量与结局；本条是类别或场景条目，不代表固定品牌配方或已证实的长期功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
