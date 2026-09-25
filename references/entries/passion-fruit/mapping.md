# Mapping｜passion-fruit

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: passion-fruit
research_ref: references/entries/passion-fruit/research.md
summary_ref: references/entries/passion-fruit/summary.md
summary_sha256: cd1c519ee4968f2e41b7b45b484d4481d6f21d9e4db4d03782ca0e814ba3d657
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:45.608691+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/passion-fruit.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.03 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.73 | M-IV | 百香果果浆通常酸味明显，成熟度和加糖会改变整体酸甜感；仅为感官描述。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.24 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.33 | 0.20 | 0.50 | 0.26 | 0.04 | M-0 |
| 肝 | 0.07 | 阳- | 0.17 | 0.32 | 0.28 | 0.37 | 0.03 | M-0 |
| 脾 | 0.09 | 阴+ | 0.25 | 0.39 | 0.44 | 0.03 | 0.14 | M-0 |
| 肺 | 0.06 | 阴+ | 0.50 | 0.25 | 0.62 | 0.11 | 0.02 | M-0 |
| 肾 | 0.06 | 阴+ | 0.35 | 0.37 | 0.51 | 0.09 | 0.03 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：普通百香果整果果肉的直接健康结局证据不足（E-0）。混合饮品和果皮粉试验分别存在共同干预与食品形态不匹配，不能作为整果功效证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
