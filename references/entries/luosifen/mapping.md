# Mapping｜luosifen

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 21-noodles-instant-meals
entry_id: luosifen
research_ref: references/entries/luosifen/research.md
summary_ref: references/entries/luosifen/summary.md
summary_sha256: bd9eff1a771e50303847f184fd23359ba3a20f23ba7674b91c93439b7686cc52
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:52:12.987755+00:00
workflow_run_id: 36104825568
workflow_artifact_id: 10850886738
native_result_ref: qa/jev-entry-batches/21-noodles-instant-meals/raw/luosifen.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.94 | M-0 |
| 温 | 0.03 | M-0 |
| 热 | 0.03 | M-0 |

Jev Choice：**平**（Choice confidence 0.93）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.22 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.27 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.16 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.23 | 0.29 | 0.02 | 0.27 | 0.42 | M-0 |
| 肝 | 0.05 | 阴- | 0.23 | 0.42 | 0.02 | 0.40 | 0.16 | M-0 |
| 脾 | 0.09 | 阳+ | 0.32 | 0.45 | 0.02 | 0.04 | 0.49 | M-0 |
| 肺 | 0.05 | 阴- | 0.36 | 0.52 | 0.07 | 0.26 | 0.15 | M-0 |
| 肾 | 0.04 | 阴- | 0.45 | 0.59 | 0.04 | 0.11 | 0.26 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：螺蛳粉目前以产品组成和标准化资料为主，未见直接人体健康效果试验；调味包每100克数据不能替代整包每份数据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
