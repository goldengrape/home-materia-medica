# Mapping｜durian

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: durian
research_ref: references/entries/durian/research.md
summary_ref: references/entries/durian/summary.md
summary_sha256: 52713699229c3f18d943fdde2e2efadb82f34bcfc8d3b8dc61eea7b0800770a9
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:46.171343+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/durian.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.95 | M-0 |
| 温 | 0.04 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.94）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.28 | M-IV | 成熟榴莲果肉常有甜味，品种和成熟度会改变香气与甜度；只作感官描述。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.10 | 阳+ | 0.57 | 0.05 | 0.10 | 0.17 | 0.68 | M-0 |
| 肝 | 0.06 | 阳+ | 0.12 | 0.25 | 0.24 | 0.18 | 0.33 | M-0 |
| 脾 | 0.13 | 阳+ | 0.43 | 0.13 | 0.29 | 0.01 | 0.57 | M-0 |
| 肺 | 0.05 | 阴+ | 0.22 | 0.32 | 0.42 | 0.09 | 0.17 | M-0 |
| 肾 | 0.06 | 阴+ | 0.16 | 0.29 | 0.38 | 0.04 | 0.29 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：榴莲整果仅有小样本急性交叉研究；血压、心率和血脂是短时餐后指标（E-D），无长期疾病结局证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
