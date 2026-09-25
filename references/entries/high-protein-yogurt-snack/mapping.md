# Mapping｜high-protein-yogurt-snack

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 38-final-fitness-scenes
entry_id: high-protein-yogurt-snack
research_ref: references/entries/high-protein-yogurt-snack/research.md
summary_ref: references/entries/high-protein-yogurt-snack/summary.md
summary_sha256: 9616b2522bec92cdd862e4085b2571f5b937c2ca3d53381ab744b2c0d71f3a19
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:51:18.252398+00:00
workflow_run_id: 36120745831
workflow_artifact_id: 10857510344
native_result_ref: qa/jev-entry-batches/38-final-fitness-scenes/raw/high-protein-yogurt-snack.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.15 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.28 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳+ | 0.37 | 0.11 | 0.30 | 0.06 | 0.53 | M-0 |
| 肝 | 0.05 | 阳+ | 0.22 | 0.28 | 0.16 | 0.14 | 0.42 | M-0 |
| 脾 | 0.14 | 阳+ | 0.78 | 0.06 | 0.10 | 0.01 | 0.83 | M-0 |
| 肺 | 0.05 | 阴+ | 0.36 | 0.21 | 0.51 | 0.06 | 0.22 | M-0 |
| 肾 | 0.08 | 阴+ | 0.43 | 0.12 | 0.58 | 0.02 | 0.28 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列食品、人群、剂量、运动方式和观察结局；本条是运动饮食场景，不代表固定补充方案或长期健康效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
