# Mapping｜pistachio

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 10-confections-nuts
entry_id: pistachio
research_ref: references/entries/pistachio/research.md
summary_ref: references/entries/pistachio/summary.md
summary_sha256: 63d1e64b5d5e52ff4c8bea5e161b0a76e950f1ed6383bc40fbb87f98f0135ffb
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T12:22:59.064339+00:00
workflow_run_id: 35998620791
workflow_artifact_id: 10807635500
native_result_ref: qa/jev-entry-batches/10-confections-nuts/raw/pistachio.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.07 | M-0 |
| 温 | 0.93 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**温**（Choice confidence 0.91）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.14 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.59 | M-IV | 传统《饮膳正要》“必思答”记味甘；《本草纲目》转引《本草拾遗》记辛、温、涩。现代食用感受依生/烘烤和调味而变，不能把传统记载合并成唯一现代分类。 |
| 辛 | 0.64 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.09 | 阳+ | 0.51 | 0.10 | 0.08 | 0.19 | 0.63 | M-0 |
| 肝 | 0.13 | 阳+ | 0.57 | 0.11 | 0.05 | 0.17 | 0.67 | M-0 |
| 脾 | 0.45 | 阳+ | 0.82 | 0.12 | 0.01 | 0.00 | 0.87 | M-0 |
| 肺 | 0.07 | 阳+ | 0.47 | 0.25 | 0.08 | 0.07 | 0.60 | M-0 |
| 肾 | 0.19 | 阳+ | 0.81 | 0.08 | 0.04 | 0.02 | 0.86 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：RCT直接研究为 D0。2014、2025试验部分阳性，2024夜间方案对主要代谢指标为阴性；人群均为糖尿病前期、剂量偏高、时机与对照不同。系统综述存在基础试验重叠和异质，支持对特定心代谢标志物作有限表述（E-B），但无临床事件证明（E-0）。传统原文可证明历史记载，不自动等于现代食品功效或明确归经。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
