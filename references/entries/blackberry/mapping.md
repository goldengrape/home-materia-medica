# Mapping｜blackberry

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: blackberry
research_ref: references/entries/blackberry/research.md
summary_ref: references/entries/blackberry/summary.md
summary_sha256: cb2a7da314b39789c1caf297434dcefcc8c686506a6bc34ce9b21e5a2798a9c9
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:43.707308+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/blackberry.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.06 | M-0 |
| 平 | 0.92 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.91）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.16 | M-IV | 黑莓成熟度不同，常有酸甜变化；这里只记录感官，不推成传统分类。 |
| 苦 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.27 | M-IV | 成熟黑莓可有甜味，品种和储存影响明显；这里只记录感官，不推成传统分类。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.46 | 0.14 | 0.59 | 0.24 | 0.03 | M-0 |
| 肝 | 0.08 | 阴+ | 0.33 | 0.20 | 0.50 | 0.29 | 0.01 | M-0 |
| 脾 | 0.11 | 阴+ | 0.25 | 0.36 | 0.44 | 0.03 | 0.17 | M-0 |
| 肺 | 0.06 | 阴+ | 0.53 | 0.17 | 0.65 | 0.16 | 0.02 | M-0 |
| 肾 | 0.07 | 阴+ | 0.66 | 0.18 | 0.75 | 0.06 | 0.01 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：黑莓整果直接人体证据很有限（E-D至E-C）：一项小型短期控制膳食试验的主要信号来自替代指标；对血糖和长期临床结局未证实。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
