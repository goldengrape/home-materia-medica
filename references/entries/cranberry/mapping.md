# Mapping｜cranberry

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: cranberry
research_ref: references/entries/cranberry/research.md
summary_ref: references/entries/cranberry/summary.md
summary_sha256: 65e55c732a331457b63393745bab31d0ff753e63385850eb5aae60e0ad7cc66f
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:42.883476+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/cranberry.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.04 | M-0 |
| 凉 | 0.12 | M-0 |
| 平 | 0.84 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.80）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.90 | M-IV | 蔓越莓果实及未加糖果汁通常酸味明显；市售产品甜度受添加糖影响，仅作感官记录。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.06 | 阴+ | 0.19 | 0.35 | 0.39 | 0.23 | 0.03 | M-0 |
| 肝 | 0.06 | 阴- | 0.17 | 0.37 | 0.27 | 0.34 | 0.02 | M-0 |
| 脾 | 0.11 | 阴- | 0.42 | 0.56 | 0.34 | 0.04 | 0.05 | M-0 |
| 肺 | 0.07 | 阴+ | 0.20 | 0.38 | 0.40 | 0.21 | 0.01 | M-0 |
| 肾 | 0.35 | 阴- | 0.66 | 0.73 | 0.19 | 0.07 | 0.01 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：蔓越莓产品用于特定人群预防复发尿路感染有中等确定性证据；证据覆盖果汁、片剂和胶囊，不能专门归因于鲜果。对已发生感染的治疗效果未获支持（E-C；按产品和人群分层）。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
