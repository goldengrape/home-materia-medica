# Mapping｜mixed-grain-rice

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 20-grains-rice-pasta-legumes
entry_id: mixed-grain-rice
research_ref: references/entries/mixed-grain-rice/research.md
summary_ref: references/entries/mixed-grain-rice/summary.md
summary_sha256: 825564321bd38b912704b2716e3689cfaf3be4cc7ee1709c42dd6d3622cfd0af
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:37:36.580107+00:00
workflow_run_id: 36103697354
workflow_artifact_id: 10850271525
native_result_ref: qa/jev-entry-batches/20-grains-rice-pasta-legumes/raw/mixed-grain-rice.json

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
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.36 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.12 | 0.28 | 0.05 | 0.33 | 0.34 | M-0 |
| 肝 | 0.05 | 阴- | 0.29 | 0.47 | 0.04 | 0.30 | 0.19 | M-0 |
| 脾 | 0.21 | 阳+ | 0.48 | 0.33 | 0.02 | 0.04 | 0.61 | M-0 |
| 肺 | 0.05 | 阴- | 0.21 | 0.41 | 0.13 | 0.16 | 0.30 | M-0 |
| 肾 | 0.06 | 阴- | 0.34 | 0.51 | 0.12 | 0.18 | 0.19 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：杂粮饭邻近证据来自13名成人对一种60/40白米、豆类、坚果和种子配方的单餐试验；不适用于所有杂粮组合。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
