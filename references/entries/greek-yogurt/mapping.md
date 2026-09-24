# Mapping｜greek-yogurt

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: greek-yogurt
research_ref: references/entries/greek-yogurt/research.md
summary_ref: references/entries/greek-yogurt/summary.md
summary_sha256: 9a3c7669b84939d6fc03fb1fb4c185d0671e554d7060e714318a43cff12a3ae1
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:39.803076+00:00
workflow_run_id: 36009889022
workflow_artifact_id: 10812190966
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/greek-yogurt.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.02 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.30 | M-IV | 原味发酵酸奶有酸味，甜味与酸度受菌种、过滤及加糖影响；这是味觉描述。 |
| 苦 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.27 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.27 | 0.30 | 0.45 | 0.10 | 0.15 | M-0 |
| 肝 | 0.05 | 阴- | 0.26 | 0.44 | 0.23 | 0.22 | 0.11 | M-0 |
| 脾 | 0.14 | 阳+ | 0.32 | 0.30 | 0.20 | 0.01 | 0.49 | M-0 |
| 肺 | 0.06 | 阴+ | 0.42 | 0.31 | 0.57 | 0.06 | 0.06 | M-0 |
| 肾 | 0.07 | 阴+ | 0.50 | 0.31 | 0.61 | 0.03 | 0.05 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：原味2%希腊酸奶：60名年轻与较年长成人单份随机交叉试验显示餐后主观食欲AUC低于两种牛奶；仅属急性替代比较，不支持长期体重/疾病效果（D0，单餐，E-C）。乳制品NMA与一般酸奶综述为D2背景。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
