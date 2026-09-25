# Mapping｜vegetable-chips

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 23-snacks-dried-meat
entry_id: vegetable-chips
research_ref: references/entries/vegetable-chips/research.md
summary_ref: references/entries/vegetable-chips/summary.md
summary_sha256: af21e2c58bf4f7b638b3c6f864e31412db023e7bdcd56d469d530132bef73123
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-25T07:26:43.683118+00:00
workflow_run_id: 36107650022
workflow_artifact_id: 10851348589
native_result_ref: qa/jev-entry-batches/23-snacks-dried-meat/raw/vegetable-chips.json

## 四气

| 候选 | 原生 probability | M |
|---|---:|---|
| 寒 | 0.00 | M-0 |
| 凉 | 0.00 | M-0 |
| 平 | 0.97 | M-0 |
| 温 | 0.01 | M-0 |
| 热 | 0.02 | M-0 |

Jev Choice：**平**（Choice confidence 0.97）。模型分类倾向不替代本条传统直接证据。

## 五味

| 候选 | 原生 Noul | M | 注释 |
|---|---:|---|---|
| 酸 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 苦 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.09 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 辛 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.11 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.04 | 阳- | 0.19 | 0.34 | 0.04 | 0.39 | 0.23 | M-0 |
| 肝 | 0.04 | 阴- | 0.38 | 0.54 | 0.02 | 0.35 | 0.09 | M-0 |
| 脾 | 0.06 | 阴- | 0.45 | 0.58 | 0.03 | 0.04 | 0.35 | M-0 |
| 肺 | 0.04 | 阴- | 0.44 | 0.58 | 0.08 | 0.24 | 0.10 | M-0 |
| 肾 | 0.04 | 阴- | 0.55 | 0.66 | 0.05 | 0.15 | 0.14 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：现有证据限于所述样品、配方或人群；不能将近似商品资料视为整个目录品类的临床结论。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
