# Mapping｜overnight-oats-cup

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 36-afternoon-and-night-scenes
entry_id: overnight-oats-cup
research_ref: references/entries/overnight-oats-cup/research.md
summary_ref: references/entries/overnight-oats-cup/summary.md
summary_sha256: 84cfd2170b8b8f5c0a237faa33cc78c5c4b266435258de85f677481ef12c9793
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:32:59.321276+00:00
workflow_run_id: 36119043810
workflow_artifact_id: 10856616929
native_result_ref: qa/jev-entry-batches/36-afternoon-and-night-scenes/raw/overnight-oats-cup.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.01 | M-0 |
| 凉 | 0.08 | M-0 |
| 平 | 0.91 | M-0 |
| 温 | 0.00 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.89）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.34 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.17 | 0.25 | 0.18 | 0.37 | 0.20 | M-0 |
| 肝 | 0.04 | 阳- | 0.21 | 0.39 | 0.07 | 0.41 | 0.13 | M-0 |
| 脾 | 0.16 | 阳+ | 0.57 | 0.22 | 0.07 | 0.03 | 0.68 | M-0 |
| 肺 | 0.05 | 阴+ | 0.22 | 0.34 | 0.41 | 0.15 | 0.10 | M-0 |
| 肾 | 0.04 | 阴- | 0.30 | 0.47 | 0.35 | 0.08 | 0.10 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列配方、食品组合、人群、进食时间和结局；本条是生活场景条目，不代表固定份量或长期健康效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
