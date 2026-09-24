# Mapping｜pound-cake

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 07-baked-sweets
entry_id: pound-cake
research_ref: references/entries/pound-cake/research.md
summary_ref: references/entries/pound-cake/summary.md
summary_sha256: 895baefafbb0cb1c4ab1664fdbcf0b900b436abbfdcb724f7c98857dc350179e
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:06:35.234850+00:00
workflow_run_id: 35991084364
workflow_artifact_id: 10803294243
native_result_ref: qa/jev-entry-batches/07-baked-sweets/raw/pound-cake.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.62 | M-IV | 糖形成主要甜味，黄油或其他油脂增加浓郁感；配方与烘烤程度会改变香气。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.29 | 0.15 | 0.23 | 0.15 | 0.47 | M-0 |
| 肝 | 0.04 | 阴- | 0.17 | 0.38 | 0.09 | 0.27 | 0.26 | M-0 |
| 脾 | 0.10 | 阳+ | 0.38 | 0.28 | 0.16 | 0.02 | 0.53 | M-0 |
| 肺 | 0.05 | 阴- | 0.27 | 0.46 | 0.23 | 0.13 | 0.18 | M-0 |
| 肾 | 0.04 | 阴- | 0.22 | 0.42 | 0.26 | 0.08 | 0.24 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：FDC 为 D0（指定数据库食品记录）；FSANZ 食谱计算是 D0/D1 的配方成分信息。两者都不是健康结局证据；成品人体临床证据不足（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
