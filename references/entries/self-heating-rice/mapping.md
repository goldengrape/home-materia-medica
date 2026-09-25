# Mapping｜self-heating-rice

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 21-noodles-instant-meals
entry_id: self-heating-rice
research_ref: references/entries/self-heating-rice/research.md
summary_ref: references/entries/self-heating-rice/summary.md
summary_sha256: 32d0d383b4e6d1e305b66a3c97b9b50047c5551ef153b333a8381a7580d52c83
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:52:14.563836+00:00
workflow_run_id: 36104825568
workflow_artifact_id: 10850886738
native_result_ref: qa/jev-entry-batches/21-noodles-instant-meals/raw/self-heating-rice.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.12 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.12 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.21 | 0.21 | 0.03 | 0.35 | 0.41 | M-0 |
| 肝 | 0.04 | 阳- | 0.23 | 0.42 | 0.02 | 0.42 | 0.14 | M-0 |
| 脾 | 0.08 | 阳+ | 0.48 | 0.32 | 0.03 | 0.03 | 0.62 | M-0 |
| 肺 | 0.04 | 阴- | 0.28 | 0.46 | 0.09 | 0.23 | 0.22 | M-0 |
| 肾 | 0.04 | 阴- | 0.37 | 0.52 | 0.04 | 0.15 | 0.29 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：自热米饭缺少直接人体研究；广义预制菜标签统计和常温杀菌米饭加工研究均不能代替该品类的健康效果证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
