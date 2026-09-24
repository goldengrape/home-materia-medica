# Mapping｜ice-cream

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 08-cakes-frozen-desserts
entry_id: ice-cream
research_ref: references/entries/ice-cream/research.md
summary_ref: references/entries/ice-cream/summary.md
summary_sha256: bfd6b24764d969e0b71e99ea87dd46b18f56ce057e11d3464ad005ec9145510a
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:33:58.164650+00:00
workflow_run_id: 35993741889
workflow_artifact_id: 10804164780
native_result_ref: qa/jev-entry-batches/08-cakes-frozen-desserts/raw/ice-cream.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.11 | M-0 |
| 凉 | 0.04 | M-0 |
| 平 | 0.85 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.81）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.36 | M-IV | 冰淇淋可含糖、甜味剂或甜味配料；低温和脂肪会影响感官甜度。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.30 | 0.18 | 0.20 | 0.47 | 0.15 | M-0 |
| 肝 | 0.04 | 阳- | 0.32 | 0.38 | 0.06 | 0.49 | 0.07 | M-0 |
| 脾 | 0.07 | 阴- | 0.25 | 0.44 | 0.21 | 0.14 | 0.21 | M-0 |
| 肺 | 0.04 | 阳- | 0.19 | 0.35 | 0.20 | 0.40 | 0.05 | M-0 |
| 肾 | 0.05 | 阴- | 0.11 | 0.33 | 0.32 | 0.28 | 0.07 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：该研究为 D0（指定品牌成品）且为短时人体交叉试验，但仅 12 人、单公司产品、固定大份量与 120 分钟观察；长期结局及品类外推证据不足。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
