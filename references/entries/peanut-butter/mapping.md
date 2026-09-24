# Mapping｜peanut-butter

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 12-seeds-and-butters
entry_id: peanut-butter
research_ref: references/entries/peanut-butter/research.md
summary_ref: references/entries/peanut-butter/summary.md
summary_sha256: 2f62ef6b0624324626a1ff8d09c37e58fbb1bf222873cb99c97fab9148f326b2
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T13:36:15.551113+00:00
workflow_run_id: 36006762786
workflow_artifact_id: 10810717078
native_result_ref: qa/jev-entry-batches/12-seeds-and-butters/raw/peanut-butter.json

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
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.26 | M-IV | 烘烤花生酱味浓、略甜或略咸；添加配料和研磨程度改变感官特征。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳+ | 0.47 | 0.12 | 0.18 | 0.09 | 0.61 | M-0 |
| 肝 | 0.06 | 阳+ | 0.10 | 0.30 | 0.24 | 0.13 | 0.33 | M-0 |
| 脾 | 0.15 | 阳+ | 0.64 | 0.11 | 0.15 | 0.01 | 0.73 | M-0 |
| 肺 | 0.05 | 阴- | 0.18 | 0.39 | 0.30 | 0.07 | 0.24 | M-0 |
| 肾 | 0.06 | 阴+ | 0.22 | 0.27 | 0.41 | 0.06 | 0.26 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Kohler 等试点 RCT 为 D0（花生酱），40 名消防员、7 周、每周至少 5 次睡前一份；血压与身体组成未见显著组别×时间差异。样本极小、几乎全男性、时间短（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
