# Mapping｜protein-bar

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 10-confections-nuts
entry_id: protein-bar
research_ref: references/entries/protein-bar/research.md
summary_ref: references/entries/protein-bar/summary.md
summary_sha256: a4478364c9c937d42b2094624e851663518f3e890b7add76a97776d2ec363a96
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:07:09.801128+00:00
workflow_run_id: 35998620791
workflow_artifact_id: 10807635500
native_result_ref: qa/jev-entry-batches/10-confections-nuts/raw/protein-bar.json

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
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.09 | M-IV | 蛋白棒可由糖浆、巧克力、糖醇或风味料提供甜味；蛋白源与纤维会影响口感和饱腹感。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.16 | 0.25 | 0.07 | 0.31 | 0.37 | M-0 |
| 肝 | 0.04 | 阴- | 0.22 | 0.42 | 0.03 | 0.41 | 0.14 | M-0 |
| 脾 | 0.09 | 阴- | 0.39 | 0.54 | 0.04 | 0.02 | 0.40 | M-0 |
| 肺 | 0.04 | 阴- | 0.40 | 0.55 | 0.18 | 0.16 | 0.11 | M-0 |
| 肾 | 0.04 | 阴- | 0.37 | 0.53 | 0.17 | 0.14 | 0.16 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：一项小型急性人体试验为 D0（与特定配方直接相关），但同时改变蛋白和纤维，只测单次餐后摄入与替代指标；长期体重、训练表现及一般商品蛋白棒结局证据不足（E-C/E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
