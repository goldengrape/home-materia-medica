# Mapping｜flavored-yogurt

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: flavored-yogurt
research_ref: references/entries/flavored-yogurt/research.md
summary_ref: references/entries/flavored-yogurt/summary.md
summary_sha256: 87212c2a669e4461dfb354fd595642887da2fd61dbdd721ce34393ce84dea532
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:55.259544+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/flavored-yogurt.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.19 | M-IV | 发酵酸味常与果香、甜味并存；各商品差异较大，仅作感官描述。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.40 | M-IV | 甜度取决于乳糖、添加糖或甜味剂，不能从名称判断。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴+ | 0.11 | 0.25 | 0.33 | 0.18 | 0.24 | M-0 |
| 肝 | 0.04 | 阴- | 0.30 | 0.47 | 0.10 | 0.30 | 0.13 | M-0 |
| 脾 | 0.09 | 阳+ | 0.21 | 0.34 | 0.24 | 0.02 | 0.40 | M-0 |
| 肺 | 0.04 | 阴+ | 0.27 | 0.38 | 0.45 | 0.09 | 0.08 | M-0 |
| 肾 | 0.05 | 阴+ | 0.30 | 0.39 | 0.47 | 0.05 | 0.09 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：本条直接人体健康结局证据不足（E-0）。直接产品资料为3国3,724种产品横断面调查（D0，成分/标签而非干预）：调查样本中酸奶类产品总糖均值约11.5 g/100 g，产品差异显著；不构成疾病效应证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
