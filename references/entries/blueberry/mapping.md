# Mapping｜blueberry

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: blueberry
research_ref: references/entries/blueberry/research.md
summary_ref: references/entries/blueberry/summary.md
summary_sha256: 51e727d9eda76e328e26809252383563826d7bfe58b666086a500ed9e7d443f3
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:42.347712+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/blueberry.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.02 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.14 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.31 | M-IV | 成熟蓝莓通常呈甜味，品种、成熟度及酸甜平衡会影响感官描述；仅记录食味，不推为传统药味或功效。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.15 | 阴+ | 0.54 | 0.08 | 0.65 | 0.18 | 0.09 | M-0 |
| 肝 | 0.08 | 阴+ | 0.39 | 0.19 | 0.53 | 0.26 | 0.02 | M-0 |
| 脾 | 0.07 | 阴+ | 0.31 | 0.32 | 0.49 | 0.02 | 0.17 | M-0 |
| 肺 | 0.06 | 阴+ | 0.59 | 0.17 | 0.70 | 0.12 | 0.01 | M-0 |
| 肾 | 0.07 | 阴+ | 0.69 | 0.18 | 0.77 | 0.04 | 0.01 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：鲜蓝莓具体长期健康结局证据有限（E-C至E-0）。系统综述混合了不同浆果和加工制品，主要结局是认知任务、血管功能或风险标志物，不是疾病发生率。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
