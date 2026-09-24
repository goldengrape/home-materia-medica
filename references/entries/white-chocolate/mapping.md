# Mapping｜white-chocolate

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 06-nuts-cocoa-chocolate
entry_id: white-chocolate
research_ref: references/entries/white-chocolate/research.md
summary_ref: references/entries/white-chocolate/summary.md
summary_sha256: c46ac3b2b61febc00cb259e94e69a84d6829c8f9bb9d9a23c3d920ddaf554616
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T10:44:21.250880+00:00
workflow_run_id: 35988940964
workflow_artifact_id: 10803037445
native_result_ref: qa/jev-entry-batches/06-nuts-cocoa-chocolate/raw/white-chocolate.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.46 | M-IV | 糖与乳成分构成主要甜味，产品间甜度不同，仅作感官描述。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳- | 0.15 | 0.16 | 0.18 | 0.36 | 0.30 | M-0 |
| 肝 | 0.04 | 阴- | 0.18 | 0.39 | 0.10 | 0.32 | 0.19 | M-0 |
| 脾 | 0.07 | 阳+ | 0.14 | 0.28 | 0.33 | 0.03 | 0.36 | M-0 |
| 肺 | 0.04 | 阴- | 0.14 | 0.35 | 0.29 | 0.23 | 0.13 | M-0 |
| 肾 | 0.04 | 阴- | 0.16 | 0.38 | 0.33 | 0.13 | 0.16 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：2026 年试验里白巧克力组有单一皮肤血流指标下降，其他多项指标未见一致改善；样本和随访都不足以判断长期效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
