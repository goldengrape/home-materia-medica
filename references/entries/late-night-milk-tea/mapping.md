# Mapping｜late-night-milk-tea

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 37-office-and-fitness-scenes
entry_id: late-night-milk-tea
research_ref: references/entries/late-night-milk-tea/research.md
summary_ref: references/entries/late-night-milk-tea/summary.md
summary_sha256: 5c9a04db101d533adf02d103aee63fac2c2e3ada6bea231d195e01e05596497b
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:44:05.715632+00:00
workflow_run_id: 36120250267
workflow_artifact_id: 10857540243
native_result_ref: qa/jev-entry-batches/37-office-and-fitness-scenes/raw/late-night-milk-tea.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.27 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.10 | 阳+ | 0.49 | 0.08 | 0.02 | 0.28 | 0.62 | M-0 |
| 肝 | 0.05 | 阳- | 0.44 | 0.26 | 0.02 | 0.57 | 0.15 | M-0 |
| 脾 | 0.07 | 阴- | 0.19 | 0.38 | 0.21 | 0.07 | 0.34 | M-0 |
| 肺 | 0.06 | 阳- | 0.22 | 0.31 | 0.06 | 0.42 | 0.21 | M-0 |
| 肾 | 0.05 | 阴- | 0.18 | 0.38 | 0.10 | 0.38 | 0.14 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列配方、食品组合、人群、进食时间和结局；本条是生活场景条目，不代表固定份量或长期健康效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
