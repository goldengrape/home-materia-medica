# Mapping｜italian-pasta

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 20-grains-rice-pasta-legumes
entry_id: italian-pasta
research_ref: references/entries/italian-pasta/research.md
summary_ref: references/entries/italian-pasta/summary.md
summary_sha256: 24f6f731ce7976a80e9113a456ede7e8df84dd44e8c07af251c0bdcbc11065b6
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:37:37.729669+00:00
workflow_run_id: 36103697354
workflow_artifact_id: 10850271525
native_result_ref: qa/jev-entry-batches/20-grains-rice-pasta-legumes/raw/italian-pasta.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.33 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.28 | 0.22 | 0.06 | 0.26 | 0.46 | M-0 |
| 肝 | 0.04 | 阴- | 0.24 | 0.44 | 0.03 | 0.25 | 0.28 | M-0 |
| 脾 | 0.18 | 阳+ | 0.72 | 0.17 | 0.03 | 0.01 | 0.79 | M-0 |
| 肺 | 0.06 | 阴- | 0.17 | 0.38 | 0.18 | 0.12 | 0.32 | M-0 |
| 肾 | 0.04 | 阴- | 0.26 | 0.45 | 0.15 | 0.09 | 0.31 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：普通意面的直接证据为14名健康成人、单品牌No.7细意面的急性GI试验；没有长期临床结局。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
