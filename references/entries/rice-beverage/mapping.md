# Mapping｜rice-beverage

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 06-nuts-cocoa-chocolate
entry_id: rice-beverage
research_ref: references/entries/rice-beverage/research.md
summary_ref: references/entries/rice-beverage/summary.md
summary_sha256: 8f677f51c633e1e7622cabf356aa4bdb927ea1e623b63420e201e8e9fdd6174f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:44:18.618649+00:00
workflow_run_id: 35988940964
workflow_artifact_id: 10803037445
native_result_ref: qa/jev-entry-batches/06-nuts-cocoa-chocolate/raw/rice-beverage.json

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
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.27 | M-IV | 米淀粉经制浆/酶解后可呈谷物甜味；添加糖另看标签，仅作感官描述。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴+ | 0.12 | 0.21 | 0.34 | 0.17 | 0.28 | M-0 |
| 肝 | 0.04 | 阴- | 0.25 | 0.43 | 0.14 | 0.24 | 0.19 | M-0 |
| 脾 | 0.10 | 阳+ | 0.41 | 0.16 | 0.27 | 0.01 | 0.56 | M-0 |
| 肺 | 0.05 | 阴+ | 0.35 | 0.28 | 0.51 | 0.05 | 0.16 | M-0 |
| 肾 | 0.05 | 阴- | 0.35 | 0.51 | 0.30 | 0.04 | 0.15 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：2026 年意大利 25 款米饮样品均符合欧盟无机砷最高限量，但该研究也提示早幼儿高摄入情境需留意暴露。英国官方仍建议 5 岁以下儿童不要用米饮替代母乳、配方奶或牛奶。植物饮料 RCT 综合结果整体有限，不能将类别比较写成米浆的治疗作用。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
