# Mapping｜a2-milk

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: a2-milk
research_ref: references/entries/a2-milk/research.md
summary_ref: references/entries/a2-milk/summary.md
summary_sha256: 8f45592a865cdb0cc94db54c9d518674365ba4fd52cf1512b2a409b9c0436ea4
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:38.498871+00:00
workflow_run_id: 36009889022
workflow_artifact_id: 10812190966
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/a2-milk.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.34 | M-IV | A2奶仍是牛乳，乳糖通常仍在；味觉取决于脂肪、热处理和商品配方。此处仅感官描述。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴+ | 0.37 | 0.15 | 0.53 | 0.12 | 0.20 | M-0 |
| 肝 | 0.06 | 阴- | 0.20 | 0.39 | 0.23 | 0.26 | 0.12 | M-0 |
| 脾 | 0.29 | 阴- | 0.16 | 0.38 | 0.27 | 0.02 | 0.33 | M-0 |
| 肺 | 0.05 | 阴+ | 0.44 | 0.24 | 0.58 | 0.10 | 0.08 | M-0 |
| 肾 | 0.06 | 阴+ | 0.55 | 0.24 | 0.67 | 0.03 | 0.06 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：A2奶与常规奶的部分胃肠症状比较：600人多中心交叉试验及小型单餐试验报告部分症状差异；2026年70人试验也有部分症状差别，但并非所有症状一致（D0，产品特异研究；偏倚、异质性与重复性限制结论，E-C）。A2不代表无乳糖或低过敏。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
