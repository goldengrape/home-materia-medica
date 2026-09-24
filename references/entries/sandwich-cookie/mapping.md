# Mapping｜sandwich-cookie

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 07-baked-sweets
entry_id: sandwich-cookie
research_ref: references/entries/sandwich-cookie/research.md
summary_ref: references/entries/sandwich-cookie/summary.md
summary_sha256: 0a11b988de68c10fbb499a8e9c58adc61297889024b0b54eab589aef85125227
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:06:33.904457+00:00
workflow_run_id: 35991084364
workflow_artifact_id: 10803294243
native_result_ref: qa/jev-entry-batches/07-baked-sweets/raw/sandwich-cookie.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.02 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.56 | M-IV | 夹心糖脂馅通常强化甜味；可可或香料会改变苦香与气味。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.20 | 0.20 | 0.22 | 0.18 | 0.40 | M-0 |
| 肝 | 0.04 | 阴- | 0.18 | 0.38 | 0.09 | 0.31 | 0.22 | M-0 |
| 脾 | 0.10 | 阳+ | 0.27 | 0.30 | 0.22 | 0.02 | 0.46 | M-0 |
| 肺 | 0.04 | 阴- | 0.35 | 0.52 | 0.18 | 0.14 | 0.16 | M-0 |
| 肾 | 0.04 | 阴- | 0.25 | 0.43 | 0.25 | 0.11 | 0.21 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Fineli 食谱计算记录对该指定食谱为 D0；对其他夹心饼干仅属间接参照。普通夹心饼干长期临床结局证据不足（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
