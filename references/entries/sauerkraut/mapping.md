# Mapping｜sauerkraut

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 15-fermented-foods-and-avocado
entry_id: sauerkraut
research_ref: references/entries/sauerkraut/research.md
summary_ref: references/entries/sauerkraut/summary.md
summary_sha256: 3732c6a8d1ca1877efe5719f4d0dcd605c5be3b69fe66b168630159f92e25a52
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T15:14:22.448207+00:00
workflow_run_id: 36018666716
workflow_artifact_id: 10815098771
native_result_ref: qa/jev-entry-batches/15-fermented-foods-and-avocado/raw/sauerkraut.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.07 | M-0 |
| 平 | 0.90 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.89）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.41 | M-IV | 发酵程度影响酸味。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.26 | M-IV | 配方和盐渍过程影响咸味与钠。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳- | 0.29 | 0.36 | 0.04 | 0.46 | 0.14 | M-0 |
| 肝 | 0.07 | 阴- | 0.54 | 0.65 | 0.02 | 0.28 | 0.04 | M-0 |
| 脾 | 0.14 | 阴- | 0.66 | 0.74 | 0.02 | 0.02 | 0.22 | M-0 |
| 肺 | 0.06 | 阴- | 0.57 | 0.68 | 0.09 | 0.18 | 0.05 | M-0 |
| 肾 | 0.06 | 阴- | 0.74 | 0.80 | 0.05 | 0.09 | 0.06 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：新鲜/巴氏德国酸菜短期RCT为D0；n=87，100 g/day、各4周并洗脱。报告有小幅收缩压变化和部分替代指标，未见肠屏障变化，作者认为健康成人中无可观系统效益（E-C）。两篇报告同一队列，不作独立重复计数。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
