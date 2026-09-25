# Mapping｜protein-shake-breakfast

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 36-afternoon-and-night-scenes
entry_id: protein-shake-breakfast
research_ref: references/entries/protein-shake-breakfast/research.md
summary_ref: references/entries/protein-shake-breakfast/summary.md
summary_sha256: 032cd2b372f3bb9b80fb8d13c99f4c789ccc0a0fd4069efbb029a73273cf1ce0
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:32:58.877953+00:00
workflow_run_id: 36119043810
workflow_artifact_id: 10856616929
native_result_ref: qa/jev-entry-batches/36-afternoon-and-night-scenes/raw/protein-shake-breakfast.json

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
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.22 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.11 | 0.19 | 0.15 | 0.32 | 0.34 | M-0 |
| 肝 | 0.04 | 阳- | 0.18 | 0.35 | 0.05 | 0.38 | 0.22 | M-0 |
| 脾 | 0.12 | 阳+ | 0.43 | 0.31 | 0.07 | 0.05 | 0.57 | M-0 |
| 肺 | 0.04 | 阴- | 0.14 | 0.36 | 0.30 | 0.21 | 0.13 | M-0 |
| 肾 | 0.05 | 阴- | 0.22 | 0.42 | 0.30 | 0.10 | 0.18 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列配方、食品组合、人群、进食时间和结局；本条是生活场景条目，不代表固定份量或长期健康效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
