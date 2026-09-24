# Mapping｜danish-pastry

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 08-cakes-frozen-desserts
entry_id: danish-pastry
research_ref: references/entries/danish-pastry/research.md
summary_ref: references/entries/danish-pastry/summary.md
summary_sha256: e1b96eb44fef84f459e0804216b1903d19ebd043435bd86eb0fce0d6308b22f6
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:33:56.696873+00:00
workflow_run_id: 35993741889
workflow_artifact_id: 10804164780
native_result_ref: qa/jev-entry-batches/08-cakes-frozen-desserts/raw/danish-pastry.json

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
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.43 | M-IV | 糖、果馅、卡仕达和糖霜通常提供甜味，发酵香与油脂香会改变整体风味。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.17 | 0.20 | 0.06 | 0.36 | 0.38 | M-0 |
| 肝 | 0.04 | 阳- | 0.25 | 0.38 | 0.03 | 0.43 | 0.16 | M-0 |
| 脾 | 0.06 | 阳+ | 0.33 | 0.40 | 0.05 | 0.05 | 0.50 | M-0 |
| 肺 | 0.04 | 阴- | 0.28 | 0.46 | 0.11 | 0.22 | 0.21 | M-0 |
| 肾 | 0.04 | 阴- | 0.32 | 0.50 | 0.09 | 0.18 | 0.23 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据以具体食品数据库记录为主（D0，仅限所列食品）；整类成品的人体健康结局证据未建立（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
