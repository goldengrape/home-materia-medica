# Mapping｜ice-slush

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 09-chilled-confections
entry_id: ice-slush
research_ref: references/entries/ice-slush/research.md
summary_ref: references/entries/ice-slush/summary.md
summary_sha256: 0ac7573edd81e4b831d729316ddca07fde86131dc62e4e836c8102834a1b4182
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T11:48:43.246419+00:00
workflow_run_id: 35995198753
workflow_artifact_id: 10805867273
native_result_ref: qa/jev-entry-batches/09-chilled-confections/raw/ice-slush.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.14 | M-0 |
| 凉 | 0.03 | M-0 |
| 平 | 0.83 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.79）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.03 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.16 | M-IV | 产品可能以糖、果汁、糖浆或甜味剂调味；半冻结温度也会影响感官甜度。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.13 | 阳- | 0.47 | 0.21 | 0.07 | 0.60 | 0.12 | M-0 |
| 肝 | 0.05 | 阳- | 0.29 | 0.43 | 0.05 | 0.47 | 0.05 | M-0 |
| 脾 | 0.08 | 阴- | 0.40 | 0.55 | 0.13 | 0.17 | 0.15 | M-0 |
| 肺 | 0.04 | 阳- | 0.18 | 0.37 | 0.20 | 0.38 | 0.05 | M-0 |
| 肾 | 0.06 | 阴- | 0.35 | 0.51 | 0.19 | 0.24 | 0.06 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：病例系列为 D0（与含甘油 slush 饮品直接相关的临床病例），但无对照组、病例选择和剂量信息不完整，不能估计一般风险；FSA 风险评估的重点是特定添加剂、儿童体重与份量。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
