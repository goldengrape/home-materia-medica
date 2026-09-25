# Mapping｜seasoned-dried-tofu

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 24-processed-meat-chinese-snacks
entry_id: seasoned-dried-tofu
research_ref: references/entries/seasoned-dried-tofu/research.md
summary_ref: references/entries/seasoned-dried-tofu/summary.md
summary_sha256: e0a13e3e7fa95fe8bfa5ea627730703904dd277b7332150e9a25a16abecdb0a5
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T07:35:05.995521+00:00
workflow_run_id: 36108366692
workflow_artifact_id: 10851932295
native_result_ref: qa/jev-entry-batches/24-processed-meat-chinese-snacks/raw/seasoned-dried-tofu.json

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
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.20 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.14 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.38 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴- | 0.11 | 0.34 | 0.09 | 0.28 | 0.29 | M-0 |
| 肝 | 0.06 | 阴- | 0.31 | 0.48 | 0.11 | 0.27 | 0.14 | M-0 |
| 脾 | 0.11 | 阳+ | 0.42 | 0.35 | 0.07 | 0.02 | 0.56 | M-0 |
| 肺 | 0.05 | 阴- | 0.45 | 0.59 | 0.14 | 0.12 | 0.15 | M-0 |
| 肾 | 0.05 | 阴- | 0.50 | 0.63 | 0.20 | 0.05 | 0.12 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：资料来自对应队列、商品抽检、监管规范或近似熟食研究；各条限制按原研究和抽样范围保留。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
