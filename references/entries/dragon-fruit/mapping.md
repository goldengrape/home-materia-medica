# Mapping｜dragon-fruit

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 16-berries-and-tropical-fruits
entry_id: dragon-fruit
research_ref: references/entries/dragon-fruit/research.md
summary_ref: references/entries/dragon-fruit/summary.md
summary_sha256: 2eec766c64b7f5750d60dc915979124a09bc0abf0e210e89996291d3e6c5696b
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T05:31:45.194840+00:00
workflow_run_id: 36098927772
workflow_artifact_id: 10848946258
native_result_ref: qa/jev-entry-batches/16-berries-and-tropical-fruits/raw/dragon-fruit.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.02 | M-0 |
| 凉 | 0.05 | M-0 |
| 平 | 0.93 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.92）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.08 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.35 | M-IV | 火龙果果肉多为清甜，甜度因物种、成熟度而异；只记录感官，不推成传统分类。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.19 | 阳+ | 0.13 | 0.06 | 0.34 | 0.26 | 0.34 | M-0 |
| 肝 | 0.10 | 阴+ | 0.22 | 0.21 | 0.42 | 0.31 | 0.06 | M-0 |
| 脾 | 0.09 | 阴+ | 0.37 | 0.29 | 0.52 | 0.02 | 0.17 | M-0 |
| 肺 | 0.06 | 阴+ | 0.62 | 0.16 | 0.72 | 0.10 | 0.02 | M-0 |
| 肾 | 0.07 | 阴+ | 0.48 | 0.26 | 0.62 | 0.09 | 0.03 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：红肉火龙果冻干全果粉有一项小型14天人体交叉试验，观察到部分血管功能替代指标变化（E-D）；血压无显著变化，长期疾病结局未知。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
