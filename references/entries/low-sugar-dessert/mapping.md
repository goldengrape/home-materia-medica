# Mapping｜low-sugar-dessert

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 10-confections-nuts
entry_id: low-sugar-dessert
research_ref: references/entries/low-sugar-dessert/research.md
summary_ref: references/entries/low-sugar-dessert/summary.md
summary_sha256: 0e6fda40baad09ea13819011c70384d7aaaa19b81410f685688bcf86d2c782a6
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:07:09.448652+00:00
workflow_run_id: 35997042911
workflow_artifact_id: 10806612454
native_result_ref: qa/jev-entry-batches/10-confections-nuts/raw/low-sugar-dessert.json

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
| 甘 | 0.15 | M-IV | 低糖产品仍可能通过高倍甜味剂、糖醇、乳品或水果提供甜味；甜度不直接反映糖克数。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.34 | 0.26 | 0.07 | 0.51 | 0.16 | M-0 |
| 肝 | 0.04 | 阳- | 0.38 | 0.35 | 0.04 | 0.54 | 0.07 | M-0 |
| 脾 | 0.05 | 阴- | 0.32 | 0.49 | 0.08 | 0.11 | 0.32 | M-0 |
| 肺 | 0.03 | 阴- | 0.20 | 0.39 | 0.15 | 0.39 | 0.07 | M-0 |
| 肾 | 0.03 | 阴- | 0.35 | 0.51 | 0.16 | 0.20 | 0.13 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：GB 28050 是 D0（标签声称规则，不是健康效应）；Argiana 等急性试验为 D0/D1（2型糖尿病患者、两款具体甜点、不同份量和短时血糖终点）。不能据此推断低糖甜点类别长期控糖或减重（E-0/E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
