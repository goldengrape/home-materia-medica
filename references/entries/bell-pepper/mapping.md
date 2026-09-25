# Mapping｜bell-pepper

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 17-modern-fruits-and-vegetables
entry_id: bell-pepper
research_ref: references/entries/bell-pepper/research.md
summary_ref: references/entries/bell-pepper/summary.md
summary_sha256: 4431776a4b3b8cfeb6d9c5b2b96722fe37c9e598268f44e360ac466115dbec70
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:57:25.281254+00:00
workflow_run_id: 36100718549
workflow_artifact_id: 10849536041
native_result_ref: qa/jev-entry-batches/17-modern-fruits-and-vegetables/raw/bell-pepper.json

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
| 酸 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.28 | M-IV | 成熟甜椒通常有清甜味，颜色和成熟度会影响味道；仅作为食味记录。 |
| 辛 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.00 | 0.25 | 0.25 | 0.25 | 0.25 | M-0 |
| 肝 | 0.06 | 阴- | 0.17 | 0.38 | 0.18 | 0.33 | 0.11 | M-0 |
| 脾 | 0.07 | 阳+ | 0.13 | 0.34 | 0.27 | 0.04 | 0.35 | M-0 |
| 肺 | 0.06 | 阴+ | 0.19 | 0.33 | 0.40 | 0.18 | 0.09 | M-0 |
| 肾 | 0.04 | 阴- | 0.35 | 0.51 | 0.29 | 0.10 | 0.10 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：常见鲜彩椒单品的人体临床结局证据不足（E-0）；辣椒、辣椒素和特殊试验品种不作为等同证据。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
