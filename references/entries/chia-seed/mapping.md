# Mapping｜chia-seed

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 12-seeds-and-butters
entry_id: chia-seed
research_ref: references/entries/chia-seed/research.md
summary_ref: references/entries/chia-seed/summary.md
summary_sha256: d5bd4b4c306189d6551c5a2bee1acf4cecc8136d396e6523d042e684d3b77e2d
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T13:36:13.559892+00:00
workflow_run_id: 36006762786
workflow_artifact_id: 10810717078
native_result_ref: qa/jev-entry-batches/12-seeds-and-butters/raw/chia-seed.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 1.00）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.19 | M-IV | 种子味淡、带轻微坚果感；此为现代感官描述，不等同于传统性味。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.07 | 阴+ | 0.16 | 0.26 | 0.37 | 0.27 | 0.10 | M-0 |
| 肝 | 0.07 | 阴- | 0.22 | 0.41 | 0.34 | 0.21 | 0.04 | M-0 |
| 脾 | 0.13 | 阴- | 0.37 | 0.52 | 0.25 | 0.01 | 0.22 | M-0 |
| 肺 | 0.07 | 阴+ | 0.51 | 0.31 | 0.63 | 0.03 | 0.03 | M-0 |
| 肾 | 0.08 | 阴+ | 0.38 | 0.40 | 0.53 | 0.04 | 0.03 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Salba-chia RCT 为 D0，77 名超重/肥胖且患 2 型糖尿病成人、限能量饮食中 30 g/1000 kcal、6 个月；对比 36 g/1000 kcal 燕麦麸，体重和腰围下降较多。综述结果不一致且确定性有限（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
