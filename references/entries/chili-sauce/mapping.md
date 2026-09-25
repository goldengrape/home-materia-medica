# Mapping｜chili-sauce

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 29-seasonings
entry_id: chili-sauce
research_ref: references/entries/chili-sauce/research.md
summary_ref: references/entries/chili-sauce/summary.md
summary_sha256: faa1a7cf12cfd72481056342f2a59e5d3c92abf5171dd0cc08909d9aaf7b89f6
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T08:05:18.924497+00:00
workflow_run_id: 36111002019
workflow_artifact_id: 10852594602
native_result_ref: qa/jev-entry-batches/29-seasonings/raw/chili-sauce.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.73 | M-0 |
| 温 | 0.13 | M-0 |
| 热 | 0.14 | M-0 |

Jev Choice：**平**（Choice confidence 0.66）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.47 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.31 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阳+ | 0.67 | 0.07 | 0.00 | 0.17 | 0.76 | M-0 |
| 肝 | 0.07 | 阳+ | 0.49 | 0.14 | 0.00 | 0.24 | 0.62 | M-0 |
| 脾 | 0.10 | 阳+ | 0.59 | 0.24 | 0.00 | 0.06 | 0.70 | M-0 |
| 肺 | 0.06 | 阳+ | 0.41 | 0.26 | 0.01 | 0.18 | 0.55 | M-0 |
| 肾 | 0.05 | 阳+ | 0.46 | 0.28 | 0.01 | 0.12 | 0.59 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据来自中国商品营养标签数据库及英中酱料标签横断面调查；数据按原分类报告，不能代替实验室检测、单品数据或实际食用剂量。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
