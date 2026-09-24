# Mapping｜wafer

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 07-baked-sweets
entry_id: wafer
research_ref: references/entries/wafer/research.md
summary_ref: references/entries/wafer/summary.md
summary_sha256: ff7d536ce1d4b4cfb9df9a91e6d52201a96478e706839fafa7adfcfa75903345
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:06:33.632974+00:00
workflow_run_id: 35991084364
workflow_artifact_id: 10803294243
native_result_ref: qa/jev-entry-batches/07-baked-sweets/raw/wafer.json

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
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.39 | M-IV | 无夹心威化的味道可能较淡，糖脂馅和涂层常增加甜味与香气。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳+ | 0.14 | 0.24 | 0.07 | 0.33 | 0.36 | M-0 |
| 肝 | 0.04 | 阴- | 0.21 | 0.41 | 0.04 | 0.37 | 0.18 | M-0 |
| 脾 | 0.07 | 阳+ | 0.31 | 0.39 | 0.08 | 0.05 | 0.48 | M-0 |
| 肺 | 0.04 | 阴- | 0.35 | 0.51 | 0.11 | 0.22 | 0.16 | M-0 |
| 肾 | 0.03 | 阴- | 0.40 | 0.55 | 0.10 | 0.13 | 0.22 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：政府采购规格和 FDC 夹心威化分别为 D0（规格/单一数据库类型），不能代表全部市场配方；成品临床结局证据不足（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
