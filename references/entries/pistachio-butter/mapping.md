# Mapping｜pistachio-butter

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 13-pistachio-and-dairy
entry_id: pistachio-butter
research_ref: references/entries/pistachio-butter/research.md
summary_ref: references/entries/pistachio-butter/summary.md
summary_sha256: cbbfd00b47438e15f27764c3ea1f3c5f21b00799bfd49bafc8794f004d4648ea
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:02:36.294961+00:00
workflow_run_id: 36009889022
workflow_artifact_id: 10812190966
native_result_ref: qa/jev-entry-batches/13-pistachio-and-dairy/raw/pistachio-butter.json

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
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.20 | M-IV | 未加糖的开心果酱通常有坚果香、微甘；烘烤和配方会改变味感。此处仅为感官描述。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阳+ | 0.09 | 0.19 | 0.31 | 0.19 | 0.31 | M-0 |
| 肝 | 0.07 | 阴+ | 0.13 | 0.29 | 0.34 | 0.19 | 0.18 | M-0 |
| 脾 | 0.10 | 阳+ | 0.35 | 0.24 | 0.24 | 0.02 | 0.50 | M-0 |
| 肺 | 0.05 | 阴- | 0.18 | 0.38 | 0.37 | 0.13 | 0.12 | M-0 |
| 肾 | 0.07 | 阴+ | 0.43 | 0.27 | 0.58 | 0.05 | 0.10 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：开心果酱本身：本轮未检得D0人体试验，成品健康效应为E-0。邻近证据是一项54名糖尿病前期成人的整粒开心果交叉试验（57克/日、每期4个月；D2），不能据此断言酱品有效。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
