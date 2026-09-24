# Mapping｜chocolate-energy-bar

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 07-baked-sweets
entry_id: chocolate-energy-bar
research_ref: references/entries/chocolate-energy-bar/research.md
summary_ref: references/entries/chocolate-energy-bar/summary.md
summary_sha256: e8718b269441afc14726a2af2b526f46847a4d90708e68c24e9b851c589900ab
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:06:32.777710+00:00
workflow_run_id: 35991084364
workflow_artifact_id: 10803294243
native_result_ref: qa/jev-entry-batches/07-baked-sweets/raw/chocolate-energy-bar.json

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
| 苦 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.41 | M-IV | 糖浆、果干和巧克力风味/涂层常提供甜味；不同产品的甜度和可可苦味不同。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.58 | 0.12 | 0.07 | 0.12 | 0.69 | M-0 |
| 肝 | 0.05 | 阳+ | 0.09 | 0.31 | 0.05 | 0.32 | 0.32 | M-0 |
| 脾 | 0.12 | 阳+ | 0.68 | 0.19 | 0.04 | 0.01 | 0.76 | M-0 |
| 肺 | 0.04 | 阴- | 0.15 | 0.36 | 0.18 | 0.11 | 0.35 | M-0 |
| 肾 | 0.05 | 阳+ | 0.22 | 0.36 | 0.14 | 0.09 | 0.41 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：运动交叉试验为 D2：棒状运动食品与目标品类相邻，但配方、人群和结局都有限；FDC 记录为 D0，但只对应特定历史产品。未找到普通巧克力能量棒长期临床健康结局的直接证据（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
