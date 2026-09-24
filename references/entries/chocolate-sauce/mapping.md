# Mapping｜chocolate-sauce

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 06-nuts-cocoa-chocolate
entry_id: chocolate-sauce
research_ref: references/entries/chocolate-sauce/research.md
summary_ref: references/entries/chocolate-sauce/summary.md
summary_sha256: 65c7ac94b91021403bdfccd4a9d9000c5dad09b2d81b912fb182b1f62d4f991c
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:44:22.072156+00:00
workflow_run_id: 35988940964
workflow_artifact_id: 10803037445
native_result_ref: qa/jev-entry-batches/06-nuts-cocoa-chocolate/raw/chocolate-sauce.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.10 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.82 | M-IV | 糖浆和糖提供主要甜味，可可粉仅调节苦香，具体比例依配方。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.13 | 0.19 | 0.35 | 0.12 | 0.34 | M-0 |
| 肝 | 0.05 | 阴- | 0.15 | 0.36 | 0.21 | 0.25 | 0.18 | M-0 |
| 脾 | 0.14 | 阴+ | 0.28 | 0.21 | 0.46 | 0.02 | 0.31 | M-0 |
| 肺 | 0.05 | 阴+ | 0.26 | 0.34 | 0.45 | 0.11 | 0.10 | M-0 |
| 肾 | 0.05 | 阴+ | 0.20 | 0.40 | 0.40 | 0.07 | 0.13 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：未找到巧克力酱成品带来健康结局的直接人体试验。可可粉或巧克力中的成分研究不能越级证明甜酱具有相同作用。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
