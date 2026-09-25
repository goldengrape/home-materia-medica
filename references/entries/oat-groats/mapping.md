# Mapping｜oat-groats

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 20-grains-rice-pasta-legumes
entry_id: oat-groats
research_ref: references/entries/oat-groats/research.md
summary_ref: references/entries/oat-groats/summary.md
summary_sha256: 56e0bd71175a24810a9eae43685a7127a5bad5057840f903f2c0fb9ab6e3de5f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T06:37:35.110376+00:00
workflow_run_id: 36103697354
workflow_artifact_id: 10850271525
native_result_ref: qa/jev-entry-batches/20-grains-rice-pasta-legumes/raw/oat-groats.json

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
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.43 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳+ | 0.20 | 0.18 | 0.21 | 0.20 | 0.41 | M-0 |
| 肝 | 0.05 | 阴- | 0.24 | 0.42 | 0.10 | 0.23 | 0.25 | M-0 |
| 脾 | 0.24 | 阳+ | 0.70 | 0.14 | 0.08 | 0.01 | 0.77 | M-0 |
| 肺 | 0.06 | 阴+ | 0.26 | 0.31 | 0.45 | 0.04 | 0.20 | M-0 |
| 肾 | 0.06 | 阴- | 0.25 | 0.44 | 0.31 | 0.03 | 0.22 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：燕麦米的直接人体证据为10人随机交叉单餐试验，结果随整粒程度、烹煮和米饭混合而变，长期结局未知。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
