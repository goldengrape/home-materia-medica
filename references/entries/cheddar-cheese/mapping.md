# Mapping｜cheddar-cheese

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: cheddar-cheese
research_ref: references/entries/cheddar-cheese/research.md
summary_ref: references/entries/cheddar-cheese/summary.md
summary_sha256: 5b32e7f4bcb2d1466dffe975e5ddd37cd4735a6c98077af7244786b54576d1dd
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:56.277486+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/cheddar-cheese.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.03 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.09 | M-IV | 熟成带来的酸香与乳香可并存，仅作感官描述。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.14 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.29 | M-IV | 咸味与成熟、盐分及品牌有关。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.09 | 阳+ | 0.22 | 0.20 | 0.12 | 0.26 | 0.42 | M-0 |
| 肝 | 0.06 | 阴- | 0.22 | 0.42 | 0.08 | 0.30 | 0.20 | M-0 |
| 脾 | 0.09 | 阳+ | 0.26 | 0.32 | 0.22 | 0.02 | 0.44 | M-0 |
| 肺 | 0.04 | 阴- | 0.31 | 0.48 | 0.25 | 0.10 | 0.17 | M-0 |
| 肾 | 0.05 | 阴- | 0.24 | 0.43 | 0.35 | 0.04 | 0.18 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：特定切达试验提供直接短期血脂证据（D0；E-C），但研究期限为6周且终点为风险标志物。硬质奶酪与黄油的系统综述是类别级支持，不外推为临床事件或所有切达品牌的功效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
