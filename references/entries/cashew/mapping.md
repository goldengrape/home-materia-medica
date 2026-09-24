# Mapping｜cashew

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 10-confections-nuts
entry_id: cashew
research_ref: references/entries/cashew/research.md
summary_ref: references/entries/cashew/summary.md
summary_sha256: 3466f439e36fe920518ac45b3bb7b39f2b87a7e23e15aa0aef915829145844cc
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:07:10.649770+00:00
workflow_run_id: 35997042911
workflow_artifact_id: 10806612454
native_result_ref: qa/jev-entry-batches/10-confections-nuts/raw/cashew.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 1.00 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.99）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.12 | M-IV | 腰果仁味淡甜、油脂感明显；烘烤、盐渍和调味会改变感官与营养暴露。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳- | 0.14 | 0.23 | 0.18 | 0.35 | 0.24 | M-0 |
| 肝 | 0.06 | 阴- | 0.09 | 0.31 | 0.25 | 0.31 | 0.13 | M-0 |
| 脾 | 0.07 | 阳+ | 0.18 | 0.30 | 0.28 | 0.03 | 0.39 | M-0 |
| 肺 | 0.04 | 阴+ | 0.16 | 0.36 | 0.37 | 0.14 | 0.13 | M-0 |
| 肾 | 0.06 | 阴+ | 0.28 | 0.35 | 0.46 | 0.07 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：2017与2019年研究为 D0（腰果直接摄入/替代），但均为短期、小样本并限定代谢风险人群；对照和替代物不同，主要是血脂/胰岛素代理指标（E-C），不能推出疾病事件降低。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
