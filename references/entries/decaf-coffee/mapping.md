# Mapping｜decaf-coffee

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

entry_id: decaf-coffee
research_ref: references/entries/decaf-coffee/research.md
summary_ref: references/entries/decaf-coffee/summary.md
summary_sha256: 9dbf254d5af4b741c260e5525097d384173a3ddab43185d74406ba2cff8a1664
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T09:30:30.566070+00:00
workflow_run_id: 35981638241
workflow_artifact_id: 10800875453
native_result_ref: qa/jev-coffee-soda-batch/raw/decaf-coffee.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 苦 | 0.20 | M-IV | 脱因咖啡仍是咖啡饮品，可有苦味，仅作感官类推。 |
| 甘 | 0.07 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 辛 | 0.09 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.12 | 阳- | 0.53 | 0.08 | 0.01 | 0.65 | 0.26 | M-0 |
| 肝 | 0.06 | 阳- | 0.56 | 0.19 | 0.01 | 0.68 | 0.12 | M-0 |
| 脾 | 0.06 | 阴- | 0.23 | 0.42 | 0.02 | 0.21 | 0.35 | M-0 |
| 肺 | 0.06 | 阳- | 0.23 | 0.33 | 0.05 | 0.43 | 0.19 | M-0 |
| 肾 | 0.05 | 阴- | 0.32 | 0.49 | 0.03 | 0.30 | 0.18 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 明确支持的感官类推标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：小型交叉试验只比较特定晚间咖啡剂量与脱因样品，不代表所有脱因产品统一睡眠效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
