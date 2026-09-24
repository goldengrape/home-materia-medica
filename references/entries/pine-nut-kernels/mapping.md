# Mapping｜pine-nut-kernels

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: pine-nut-kernels
research_ref: references/entries/pine-nut-kernels/research.md
summary_ref: references/entries/pine-nut-kernels/summary.md
summary_sha256: 8114c75dfe20d03654292084fcd98ada1f7c3abe0e2f7fea3cd84e04aac7a985
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:20.062391+00:00
workflow_run_id: 36003283893
workflow_artifact_id: 10809600316
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/pine-nut-kernels.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.25 | M-IV | 松仁有脂香和轻甜感；烘烤可加强香气，盐焗品另有咸味。 |
| 辛 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.54 | 0.16 | 0.65 | 0.08 | 0.11 | M-0 |
| 肝 | 0.08 | 阴+ | 0.63 | 0.17 | 0.73 | 0.06 | 0.04 | M-0 |
| 脾 | 0.10 | 阴+ | 0.61 | 0.17 | 0.70 | 0.01 | 0.12 | M-0 |
| 肺 | 0.08 | 阴+ | 0.71 | 0.16 | 0.78 | 0.03 | 0.03 | M-0 |
| 肾 | 0.10 | 阴+ | 0.79 | 0.11 | 0.84 | 0.02 | 0.03 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：现有人体资料属于 D3（松子油/分离甘油三酯），对整粒松仁没有直接外推效力；一项小型油剂研究与另一项无显著结果研究方向不一。整仁临床效应证据未建立（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
