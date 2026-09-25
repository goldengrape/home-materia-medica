# Mapping｜raspberry

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: raspberry
research_ref: references/entries/raspberry/research.md
summary_ref: references/entries/raspberry/summary.md
summary_sha256: b8f2ddc66320cf93f26cdddea12efebd332b6592d85c23b310d96eeb3afd45db
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:43.287337+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/raspberry.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.03 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.96）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.17 | M-IV | 红树莓通常有酸甜味，成熟度和品种会改变酸度；只记感官，不推成传统分类。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.46 | M-IV | 红树莓的甜味随成熟度和品种变化；只记感官，不推成传统分类。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.46 | 0.14 | 0.59 | 0.21 | 0.06 | M-0 |
| 肝 | 0.06 | 阴+ | 0.34 | 0.23 | 0.51 | 0.24 | 0.02 | M-0 |
| 脾 | 0.11 | 阴+ | 0.24 | 0.40 | 0.43 | 0.02 | 0.15 | M-0 |
| 肺 | 0.06 | 阴+ | 0.64 | 0.16 | 0.73 | 0.09 | 0.02 | M-0 |
| 肾 | 0.06 | 阴+ | 0.53 | 0.28 | 0.65 | 0.05 | 0.02 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：红树莓整果的人体随机证据目前有限；一项小型8周试验未见主要空腹代谢指标显著改善（E-C）。研究对象有代谢风险，份量较大，不能外推为减重或糖尿病治疗。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
