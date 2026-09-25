# Mapping｜sweet-breakfast-cereal

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 19-breads-and-breakfast-grains
entry_id: sweet-breakfast-cereal
research_ref: references/entries/sweet-breakfast-cereal/research.md
summary_ref: references/entries/sweet-breakfast-cereal/summary.md
summary_sha256: 12b8558fa8b4a29898369abf7a2e79dd5cd56773749998df6e3f9e444c2b481f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:23:34.361924+00:00
workflow_run_id: 36102634097
workflow_artifact_id: 10849314949
native_result_ref: qa/jev-entry-batches/19-breads-and-breakfast-grains/raw/sweet-breakfast-cereal.json

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
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.03 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.50 | M-IV | 甜味来自不同的糖或甜味配料，实际甜度和糖量因商品而异；仅记录感官。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.20 | 0.26 | 0.15 | 0.19 | 0.40 | M-0 |
| 肝 | 0.03 | 阴- | 0.20 | 0.40 | 0.04 | 0.35 | 0.21 | M-0 |
| 脾 | 0.11 | 阳+ | 0.47 | 0.28 | 0.08 | 0.03 | 0.61 | M-0 |
| 肺 | 0.04 | 阴- | 0.28 | 0.45 | 0.22 | 0.15 | 0.18 | M-0 |
| 肾 | 0.04 | 阴- | 0.38 | 0.54 | 0.14 | 0.09 | 0.23 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：甜味即食麦片类别的直接临床结局证据不足（E-0）；燕麦粥试验不作为本条直接证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
