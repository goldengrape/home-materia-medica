# Mapping｜cream-cheese

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: cream-cheese
research_ref: references/entries/cream-cheese/research.md
summary_ref: references/entries/cream-cheese/summary.md
summary_sha256: f4a1c153a0bd0ac9a9662b490fcd6bd4bf91bdb72de2c66edf6da26b9bab1755
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:56.914783+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/cream-cheese.json

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
| 酸 | 0.18 | M-IV | 轻微酸味与乳香取决于发酵/酸化及配方。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.20 | M-IV | 乳脂带来的圆润感是感官描述，不是药性判断。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.15 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.13 | 0.21 | 0.35 | 0.13 | 0.31 | M-0 |
| 肝 | 0.05 | 阴- | 0.17 | 0.38 | 0.27 | 0.18 | 0.17 | M-0 |
| 脾 | 0.09 | 阴+ | 0.23 | 0.27 | 0.42 | 0.02 | 0.29 | M-0 |
| 肺 | 0.04 | 阴+ | 0.20 | 0.37 | 0.40 | 0.10 | 0.13 | M-0 |
| 肾 | 0.05 | 阴+ | 0.35 | 0.32 | 0.51 | 0.06 | 0.11 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：奶油奶酪有一项直接急性随机交叉试验（D0；E-D）：单餐33 g乳脂，n=43，测8小时甘油三酯；各餐iAUC无显著差异。长期疾病结局仍未检得。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
