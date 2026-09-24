# Mapping｜milkshake

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 09-chilled-confections
entry_id: milkshake
research_ref: references/entries/milkshake/research.md
summary_ref: references/entries/milkshake/summary.md
summary_sha256: 62f578dc7d870599d44d1404a19666f563bfefddbe346e31de37991727cd7e78
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:48:43.669512+00:00
workflow_run_id: 35995198753
workflow_artifact_id: 10805867273
native_result_ref: qa/jev-entry-batches/09-chilled-confections/raw/milkshake.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.01 | M-0 |
| 平 | 0.96 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.03 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.65 | M-IV | 糖浆、冰淇淋、果泥或甜味植物饮可提供甜味，配方决定甜度。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阴+ | 0.28 | 0.16 | 0.46 | 0.13 | 0.25 | M-0 |
| 肝 | 0.04 | 阴- | 0.12 | 0.34 | 0.21 | 0.30 | 0.15 | M-0 |
| 脾 | 0.08 | 阴+ | 0.24 | 0.27 | 0.43 | 0.03 | 0.27 | M-0 |
| 肺 | 0.04 | 阴+ | 0.40 | 0.30 | 0.55 | 0.07 | 0.08 | M-0 |
| 肾 | 0.05 | 阴+ | 0.47 | 0.29 | 0.60 | 0.04 | 0.07 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：USDA 记录为 D0（限定数据库食品）；医疗/代餐型 shakes 与普通奶昔身份不同，至多为邻近类别证据。普通奶昔临床健康结局证据本轮未建立（E-0）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
