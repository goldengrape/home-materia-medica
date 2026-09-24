# Mapping｜hazelnut

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 11-tree-nut-snacks
entry_id: hazelnut
research_ref: references/entries/hazelnut/research.md
summary_ref: references/entries/hazelnut/summary.md
summary_sha256: edf86254dda6ecf3dd4e9e062accb95d40b75149fa066f4741ae120692bff264
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:58:19.573688+00:00
workflow_run_id: 36003283893
workflow_artifact_id: 10809600316
native_result_ref: qa/jev-entry-batches/11-tree-nut-snacks/raw/hazelnut.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.98 | M-0 |
| 温 | 0.02 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.75 | M-IV | 榛仁有坚果香和油脂感；烘烤可增强香气，调味品则另有盐或糖。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.14 | 阳+ | 0.49 | 0.08 | 0.15 | 0.15 | 0.62 | M-0 |
| 肝 | 0.11 | 阳+ | 0.19 | 0.18 | 0.35 | 0.08 | 0.39 | M-0 |
| 脾 | 0.35 | 阳+ | 0.88 | 0.02 | 0.06 | 0.00 | 0.92 | M-0 |
| 肺 | 0.07 | 阴+ | 0.19 | 0.21 | 0.40 | 0.03 | 0.36 | M-0 |
| 肾 | 0.16 | 阳+ | 0.37 | 0.08 | 0.37 | 0.02 | 0.53 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：Tey 等为 D0（榛子摄入）系统综述，随机研究的 LDL 合并结果较小且区间接近零；Bamberger 等综述提示部分指标但保留研究质量限制。加工比较同时改变烘烤与盐，结果不支持单独归因（E-C）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
