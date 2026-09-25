# Mapping｜coffee-with-chocolate

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 36-afternoon-and-night-scenes
entry_id: coffee-with-chocolate
research_ref: references/entries/coffee-with-chocolate/research.md
summary_ref: references/entries/coffee-with-chocolate/summary.md
summary_sha256: 35e014aa7b9b1142088bf944e74a92d1f77a77243e61bb0468ff98df43ca57a1
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T09:33:00.698641+00:00
workflow_run_id: 36119043810
workflow_artifact_id: 10856616929
native_result_ref: qa/jev-entry-batches/36-afternoon-and-night-scenes/raw/coffee-with-chocolate.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.99 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.00 | M-0 |

Jev Choice：**平**（Choice confidence 0.98）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.15 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.19 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.07 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.09 | 阳+ | 0.53 | 0.10 | 0.01 | 0.24 | 0.65 | M-0 |
| 肝 | 0.05 | 阳- | 0.33 | 0.28 | 0.02 | 0.50 | 0.20 | M-0 |
| 脾 | 0.05 | 阴- | 0.25 | 0.44 | 0.05 | 0.12 | 0.39 | M-0 |
| 肺 | 0.05 | 阳- | 0.17 | 0.29 | 0.04 | 0.38 | 0.29 | M-0 |
| 肾 | 0.05 | 阴- | 0.19 | 0.39 | 0.04 | 0.24 | 0.33 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：证据限于所列配方、食品组合、人群、进食时间和结局；本条是生活场景条目，不代表固定份量或长期健康效果。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
