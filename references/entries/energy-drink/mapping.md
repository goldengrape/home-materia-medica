# Mapping｜energy-drink

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 05-functional-beverages
entry_id: energy-drink
research_ref: references/entries/energy-drink/research.md
summary_ref: references/entries/energy-drink/summary.md
summary_sha256: 0bab8ded3100a5782b7dc0df0f82528c21fbc2f61b4cb3f2e9301c39be0dc5ad
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:16:19.063062+00:00
workflow_run_id: 35986228691
workflow_artifact_id: 10802148312
native_result_ref: qa/jev-entry-batches/05-functional-beverages/raw/energy-drink.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.68 | M-0 |
| 温 | 0.13 | M-0 |
| 热 | 0.19 | M-0 |

Jev Choice：**平**（Choice confidence 0.60）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.11 | M-IV | 咖啡因及植物提取物可能带苦，配方常用甜味掩盖，仅属感官类推。 |
| 甘 | 0.22 | M-IV | 含糖款或代糖款可呈甜味，配方差异大，仅属感官类推。 |
| 辛 | 0.12 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.31 | 阳+ | 0.92 | 0.00 | 0.00 | 0.06 | 0.94 | M-0 |
| 肝 | 0.08 | 阳+ | 0.60 | 0.08 | 0.00 | 0.22 | 0.70 | M-0 |
| 脾 | 0.06 | 阳+ | 0.47 | 0.26 | 0.03 | 0.10 | 0.61 | M-0 |
| 肺 | 0.06 | 阳+ | 0.44 | 0.19 | 0.02 | 0.22 | 0.57 | M-0 |
| 肾 | 0.06 | 阳+ | 0.55 | 0.19 | 0.01 | 0.14 | 0.66 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：人体证据针对急性摄入和特定产品；样本较小、观察时间短，不能据此推断所有配方或罕见事件的发生率。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
