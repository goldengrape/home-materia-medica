# Mapping｜broccoli

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 17-modern-fruits-and-vegetables
entry_id: broccoli
research_ref: references/entries/broccoli/research.md
summary_ref: references/entries/broccoli/summary.md
summary_sha256: 33e6676e3b032857597a0b42fa6dadc97ebd8819e5529757a38f6454ef6e9eb4
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:57:24.396466+00:00
workflow_run_id: 36100718549
workflow_artifact_id: 10849536041
native_result_ref: qa/jev-entry-batches/17-modern-fruits-and-vegetables/raw/broccoli.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.02 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.11 | M-IV | 西兰花不同部位和烹调程度可带轻微苦味；只作食味记录，不推为功效。 |
| 甘 | 0.17 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.10 | 阳- | 0.18 | 0.38 | 0.14 | 0.39 | 0.09 | M-0 |
| 肝 | 0.09 | 阳- | 0.29 | 0.45 | 0.05 | 0.47 | 0.03 | M-0 |
| 脾 | 0.10 | 阴- | 0.47 | 0.61 | 0.12 | 0.04 | 0.23 | M-0 |
| 肺 | 0.07 | 阴- | 0.17 | 0.38 | 0.30 | 0.29 | 0.03 | M-0 |
| 肾 | 0.06 | 阴- | 0.36 | 0.52 | 0.24 | 0.20 | 0.04 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：高萝卜硫苷西兰花对LDL-C的证据来自两项12周随机研究（E-C）；效应受品种影响，且终点为风险标志物，不是疾病发生率。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
