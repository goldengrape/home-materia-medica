# Mapping｜skim-milk

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: skim-milk
research_ref: references/entries/skim-milk/research.md
summary_ref: references/entries/skim-milk/summary.md
summary_sha256: 9c2a2d367edfb946ee22564ec9ab5c7e833483d837df9f8394e3e703766191db
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:38.057584+00:00
workflow_run_id: 36010531585
workflow_artifact_id: 10812197530
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/skim-milk.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.02 | M-0 |
| 平 | 0.95 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.94）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.44 | M-IV | 乳糖仍在，味道常有轻微甜感；脂肪减少会令口感较清淡。仅作感官描述。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.53 | 0.16 | 0.65 | 0.05 | 0.14 | M-0 |
| 肝 | 0.05 | 阴+ | 0.19 | 0.35 | 0.38 | 0.16 | 0.11 | M-0 |
| 脾 | 0.16 | 阴+ | 0.37 | 0.15 | 0.53 | 0.01 | 0.31 | M-0 |
| 肺 | 0.07 | 阴+ | 0.63 | 0.20 | 0.73 | 0.02 | 0.05 | M-0 |
| 肾 | 0.08 | 阴+ | 0.64 | 0.20 | 0.73 | 0.02 | 0.05 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：脱脂与全脂对比：17人完成、0.5升/日、每期3周；除全脂奶HDL较高外，其他所测指标未见显著差异（D0，短期小型RCT，E-C）。强化铁/维生素D脱脂奶试验的组间差异不支持归因于脱脂本身。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
