# Mapping｜muffin

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 07-baked-sweets
entry_id: muffin
research_ref: references/entries/muffin/research.md
summary_ref: references/entries/muffin/summary.md
summary_sha256: f1254682e2278d5549cd47f5334cc1e2234647bc84f29404aad6532588dab063
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:06:34.940153+00:00
workflow_run_id: 35991084364
workflow_artifact_id: 10803294243
native_result_ref: qa/jev-entry-batches/07-baked-sweets/raw/muffin.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.01 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.50 | M-IV | 糖、果干、巧克力和糖霜可贡献主要甜味；面粉和油脂配方改变口感。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.28 | 0.21 | 0.07 | 0.47 | 0.25 | M-0 |
| 肝 | 0.04 | 阳- | 0.31 | 0.32 | 0.04 | 0.49 | 0.15 | M-0 |
| 脾 | 0.12 | 阳+ | 0.34 | 0.28 | 0.05 | 0.16 | 0.51 | M-0 |
| 肺 | 0.05 | 阴- | 0.16 | 0.38 | 0.16 | 0.27 | 0.19 | M-0 |
| 肾 | 0.04 | 阴- | 0.25 | 0.44 | 0.15 | 0.22 | 0.19 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：两项试验均为 D0/D1（具体马芬配方、单次餐后指标），但对整个市售马芬类别只能外推为 D2；样本小、观察时间短，长期临床结局仍未知。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
