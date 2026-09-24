# Mapping｜kimchi

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: kimchi
research_ref: references/entries/kimchi/research.md
summary_ref: references/entries/kimchi/summary.md
summary_sha256: 6cb6ce9377b4291053de5d8126b875ef85add0f07d53c7f822a3c7657d06a8e4
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:23:45.009934+00:00
workflow_run_id: 36019837801
workflow_artifact_id: 10816226594
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/kimchi.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.06 | M-0 |
| 平 | 0.90 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.88）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.39 | M-IV | 酸味随发酵阶段变化。 |
| 苦 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.32 | M-IV | 辣度由辣椒及配方决定。 |
| 咸 | 0.37 | M-IV | 盐渍工艺与品牌使咸度差异明显。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴- | 0.27 | 0.45 | 0.04 | 0.30 | 0.21 | M-0 |
| 肝 | 0.08 | 阴- | 0.47 | 0.60 | 0.02 | 0.31 | 0.07 | M-0 |
| 脾 | 0.13 | 阴- | 0.60 | 0.70 | 0.02 | 0.02 | 0.26 | M-0 |
| 肺 | 0.06 | 阴- | 0.50 | 0.63 | 0.10 | 0.20 | 0.07 | M-0 |
| 肾 | 0.06 | 阴- | 0.78 | 0.84 | 0.04 | 0.06 | 0.06 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：特定泡菜粉RCT为D0但属于产品特异研究：n=90、3 g/day、12周、体脂量为结局；对普通零售/家制泡菜的长期疾病效果仍不确定（E-C/E-0）。短期7天剂量对照不能证明临床获益。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
