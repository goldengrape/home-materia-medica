# Mapping｜cream

> Jev v0.4 是模型分类倾向；M 是依据 Research Dossier 作出的独立证据评注。分数不是校准概率，M 不修正分数。

## Run metadata

batch_id: 14-fermented-dairy-cheese
entry_id: cream
research_ref: references/entries/cream/research.md
summary_ref: references/entries/cream/summary.md
summary_sha256: 5fd3aa5a78d960f3650445a2aff1b59242986e1af60fc1e7cd511ad7be9871d5
reasoning_version: jev-tcm-reasoning-v0.4
five_shot_version: jev-tcm-pilot-fixtures-v0.4
requested_model: jev-latest
actual_model: jev-1.13.0
repeat_count: 1
run_timestamp_utc: 2026-09-24T14:42:57.927824+00:00
workflow_run_id: 36014763775
workflow_artifact_id: 10813364495
native_result_ref: qa/jev-entry-batches/14-fermented-dairy-cheese/raw/cream.json

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
| 苦 | 0.04 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 甘 | 0.21 | M-IV | 乳脂形成圆润、浓厚口感；打发与加热会改变感官质地。 |
| 辛 | 0.05 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |
| 咸 | 0.06 | M-0 | 本轮未建立稳定、可追溯的感官映射依据。 |

## 五脏归经与各经主方向

| 经 | Noul | 主方向 Choice | Choice confidence | 阴- | 阴+ | 阳- | 阳+ | M |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 心 | 0.05 | 阴+ | 0.33 | 0.14 | 0.51 | 0.08 | 0.27 | M-0 |
| 肝 | 0.05 | 阴+ | 0.18 | 0.35 | 0.38 | 0.13 | 0.14 | M-0 |
| 脾 | 0.09 | 阴+ | 0.42 | 0.21 | 0.56 | 0.02 | 0.21 | M-0 |
| 肺 | 0.04 | 阴+ | 0.43 | 0.28 | 0.58 | 0.05 | 0.09 | M-0 |
| 肾 | 0.05 | 阴+ | 0.41 | 0.28 | 0.56 | 0.05 | 0.11 | M-0 |

所有方向概率与 Choice 均保留；展示线不隐藏原始结果或提高 M。方向 Choice 不表示已确证归经。

## M 注释与写作交接

- 四气：M-0；模型 Choice 不是已确证传统属性。
- 五味：只将 dossier 中有感官描述支持的条目标为 M-IV，不写成功效。
- 五脏归经及方向：M-0；未建立可核验的直接桥梁。
- 证据距离：淡奶油的直接人体资料限于餐后单餐研究（D0；E-D）：47名健康成人、约45 g乳脂的不同乳品餐，测约6小时TG；长期健康结局未检得。产品名称与脂肪率需按当地标签确定。
- 原生 JSON 未添加 M、未改写分数；完整 answers 与 usage 保留在 native_result_ref。
